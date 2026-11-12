"""Offline benchmark safety tests. Every Docker/SQL/process call is denied unless mocked."""
import concurrent.futures
import contextlib
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import etl_benchmark as bench


def result(stdout='', returncode=0, stderr=''):
    return subprocess.CompletedProcess([], returncode, stdout, stderr)


class BenchmarkOfflineTests(unittest.TestCase):
    def setUp(self):
        scratch = bench.local.ROOT/'.local'
        scratch.mkdir(exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.root_patch = mock.patch.object(bench.local, 'ROOT', self.root)
        self.root_patch.start(); self.addCleanup(self.root_patch.stop)
        self.denials = {}
        for name in ('sql', 'docker', 'guard', 'migrate', 'recreate'):
            patch = mock.patch.object(bench.local, name, side_effect=AssertionError('UNMOCKED '+name))
            self.denials[name] = patch.start(); self.addCleanup(patch.stop)
        patch = mock.patch.object(bench.subprocess, 'run', side_effect=AssertionError('UNMOCKED process'))
        self.process = patch.start(); self.addCleanup(patch.stop)
        self.output = self.root/'.local'/'report.json'
        self.source_hash = hashlib.sha256(Path(bench.__file__).read_bytes()).hexdigest()
        self.app = bench.APPLICATION+'_'+'a'*24

    def mappings(self):
        files = [self.root/'pilot.json', self.root/'full.json']
        for path in files: path.write_text('{}', encoding='utf-8')
        return files

    def resource_host(self):
        return {'Memory': bench.MEMORY_BYTES, 'MemorySwap': 2*bench.MEMORY_BYTES,
                'NanoCpus': bench.NANO_CPUS, 'CpuQuota': 0, 'CpuPeriod': 0, 'CpusetCpus': ''}

    def fake_resources(self, host):
        self.denials['guard'].side_effect = None
        self.denials['docker'].side_effect = None
        self.denials['docker'].return_value = result(json.dumps([{'HostConfig': host}]))

    def test_common_root_uses_git_common_directory_for_linked_worktree(self):
        common = self.root/'main'/'.git'; common.mkdir(parents=True)
        (common/'objects').mkdir(); (common/'HEAD').write_text('ref: refs/heads/main\n')
        worktree = self.root/'linked'; worktree.mkdir()
        with mock.patch.object(bench.local, 'ROOT', worktree):
            self.process.side_effect = [result(str(worktree)), result(str(common)), result(str(common))]
            self.assertEqual(bench.common_repository_root(), common.parent)
        self.assertEqual(self.process.call_args_list[-1].args[0][2], str(common.parent))

    def test_common_root_rejects_worktree_identity_mismatch(self):
        self.process.side_effect = [result(str(self.root/'other'))]
        with self.assertRaisesRegex(ValueError, 'verified Git worktree'): bench.common_repository_root()

    def test_common_root_rejects_non_git_common_directory(self):
        self.process.side_effect = [result(str(self.root)), result(str(self.root/'not-git'))]
        with self.assertRaisesRegex(ValueError, 'common Git directory'): bench.common_repository_root()

    def test_shared_lease_blocks_other_worktree_until_release(self):
        first, second = bench.RunLease(self.root), bench.RunLease(self.root)
        self.assertNotEqual(first.application, second.application)
        self.assertLessEqual(len(first.application), 63)
        with first:
            with self.assertRaises(FileExistsError): second.__enter__()
            first.assert_owned()
        with second: second.assert_owned()
        self.assertFalse(second.path.exists())

    def test_lease_is_released_after_exception(self):
        lease = bench.RunLease(self.root)
        with self.assertRaisesRegex(RuntimeError, 'synthetic'):
            with lease: raise RuntimeError('synthetic')
        self.assertFalse(lease.path.exists())

    def test_foreign_lease_is_never_deleted(self):
        lease = bench.RunLease(self.root); lease.__enter__()
        lease.path.write_text(json.dumps({'owner_nonce': 'foreign'}), encoding='utf-8')
        with self.assertRaisesRegex(RuntimeError, 'nonce differs'): lease.__exit__(None, None, None)
        self.assertTrue(lease.path.exists())

    def test_report_outside_ignored_root_is_refused(self):
        with self.assertRaises(ValueError): bench.ReportFile(self.root/'outside.json', 'n', 'hash')
        self.assertFalse((self.root/'outside.json').exists())

    def test_linked_report_path_refused_before_write(self):
        linked = self.root/'.local'/'linked'
        original = Path.is_symlink
        with mock.patch.object(Path, 'is_symlink', lambda p: p == linked or original(p)):
            with self.assertRaisesRegex(ValueError, 'Linked'): bench.ReportFile(linked/'x.json', 'n', 'hash')
        self.assertFalse(linked.exists())

    def test_report_reservation_is_exclusive_and_preserves_existing_bytes(self):
        self.output.parent.mkdir(); self.output.write_bytes(b'prior evidence')
        with self.assertRaises(FileExistsError): bench.ReportFile(self.output, 'n', 'hash')
        self.assertEqual(self.output.read_bytes(), b'prior evidence')

    def test_competing_report_reservations_have_one_owner(self):
        def reserve(nonce):
            try: bench.ReportFile(self.output, nonce, 'hash'); return nonce
            except FileExistsError: return None
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            winners = list(pool.map(reserve, ['first', 'second']))
        self.assertEqual(sum(x is not None for x in winners), 1)
        self.assertIn(json.loads(self.output.read_text())['owner_nonce'], [x for x in winners if x])

    def test_same_stem_reports_use_independent_atomic_temporary_files(self):
        a = bench.ReportFile(self.output, 'a', 'hash')
        b = bench.ReportFile(self.output.with_suffix('.txt'), 'b', 'hash')
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            list(pool.map(lambda pair: pair[0].checkpoint({'run': pair[1]}), [(a, 'A'), (b, 'B')]))
        self.assertEqual(json.loads(a.path.read_text())['run'], 'A')
        self.assertEqual(json.loads(b.path.read_text())['run'], 'B')
        self.assertEqual(list(a.path.parent.glob('*.tmp')), [])

    def test_checkpoint_rechecks_ownership_and_cleans_temporary_on_tamper(self):
        dest = bench.ReportFile(self.output, 'own', 'hash'); original = bench._owns
        calls = []
        def check(path, nonce):
            calls.append(path)
            if len(calls) == 2: path.write_text(json.dumps({'owner_nonce': 'foreign'}))
            original(path, nonce)
        with mock.patch.object(bench, '_owns', side_effect=check):
            with self.assertRaisesRegex(RuntimeError, 'nonce differs'): dest.checkpoint({'status': 'MEASURED'})
        self.assertEqual(json.loads(dest.path.read_text())['owner_nonce'], 'foreign')
        self.assertFalse(list(dest.path.parent.glob('*.tmp')))

    def test_failed_atomic_replace_preserves_reservation_and_cleans_temp(self):
        dest = bench.ReportFile(self.output, 'own', 'hash'); before = dest.path.read_bytes()
        with mock.patch.object(Path, 'replace', side_effect=OSError('synthetic replace failure')):
            with self.assertRaises(OSError): dest.checkpoint({'status': 'MEASURED'})
        self.assertEqual(dest.path.read_bytes(), before)
        self.assertFalse(list(dest.path.parent.glob('*.tmp')))

    def test_actual_resource_limits_are_returned(self):
        self.fake_resources(self.resource_host())
        self.assertEqual(bench.attest_resources(), self.resource_host())

    def test_wrong_missing_or_conflicting_resource_limits_fail_closed(self):
        for change in [{'Memory': 0}, {'Memory': None}, {'NanoCpus': 0},
                       {'NanoCpus': 1_000_000_000}, {'CpusetCpus': '0'}, {'CpuQuota': 100000, 'CpuPeriod': 100000}]:
            with self.subTest(change=change):
                self.fake_resources({**self.resource_host(), **change})
                with self.assertRaisesRegex(RuntimeError, 'resource bounds differ'): bench.attest_resources()
        self.denials['sql'].assert_not_called()

    def test_exact_quota_form_is_an_attested_two_cpu_bound(self):
        host = {**self.resource_host(), 'NanoCpus': 0, 'CpuQuota': 200000, 'CpuPeriod': 100000}
        self.fake_resources(host); self.assertEqual(bench.attest_resources(), host)

    def test_idle_client_also_blocks_quiet_precondition(self):
        self.denials['sql'].side_effect = None
        self.denials['sql'].return_value = result(json.dumps([{'database': bench.DB, 'state': 'idle'}]))
        with self.assertRaisesRegex(RuntimeError, 'including idle'): bench.assert_quiet()
        query = self.denials['sql'].call_args.args[0]
        self.assertNotIn("state<>", query); self.assertNotIn('datname IS NOT NULL', query)

    def test_prepare_drop_race_does_not_force_evict_or_continue(self):
        self.denials['sql'].side_effect = RuntimeError('database is being accessed by other users')
        with mock.patch.object(bench, 'owned_preflight'):
            with self.assertRaisesRegex(RuntimeError, 'being accessed'): bench.prepare(mock.Mock(), 'hash')
        self.assertEqual(self.denials['sql'].call_count, 1)
        self.assertNotIn('FORCE', self.denials['sql'].call_args.args[0])
        self.denials['recreate'].assert_not_called(); self.denials['migrate'].assert_not_called()

    def test_prepare_uses_only_normal_drop_and_rechecks_before_migrations(self):
        self.denials['sql'].side_effect = None; self.denials['migrate'].side_effect = None
        with mock.patch.object(bench, 'owned_preflight') as preflight:
            bench.prepare(mock.Mock(), 'hash')
        self.assertEqual(preflight.call_count, 2)
        self.assertEqual([x.args[0] for x in self.denials['sql'].call_args_list],
            ['DROP DATABASE IF EXISTS "'+bench.DB+'";', 'CREATE DATABASE "'+bench.DB+'";'])
        self.denials['migrate'].assert_called_once_with(bench.DB)

    def test_changed_benchmark_source_fails_before_resource_or_sql_access(self):
        with mock.patch.object(bench, 'attest_resources') as resources:
            with self.assertRaisesRegex(RuntimeError, 'source changed'): bench.owned_preflight(mock.Mock(spec=bench.RunLease), 'not-current')
        resources.assert_not_called(); self.denials['sql'].assert_not_called()

    def test_cancellation_requires_unique_application(self):
        with self.assertRaises(ValueError): bench.cancel_application(bench.APPLICATION)
        self.process.assert_not_called(); self.denials['sql'].assert_not_called()

    def test_cancellation_matches_exact_run_and_checks_session_exit(self):
        self.denials['guard'].side_effect = None
        self.process.side_effect = [result('[{"pid":123,"cancelled":true}]'), result('0')]
        observed = bench.cancel_application(self.app)
        self.assertEqual(observed['remaining_sessions'], 0)
        for call in self.process.call_args_list:
            self.assertIn("application_name='"+self.app+"'", call.kwargs['input'])
            self.assertNotIn('LIKE', call.kwargs['input']); self.assertEqual(call.kwargs['timeout'], 15)
            self.assertEqual(call.args[0][-1], 'postgres')

    def test_cancellation_control_failure_or_remaining_session_is_not_success(self):
        self.denials['guard'].side_effect = None
        for outputs in [[result('', 1, 'synthetic denied')],
                        [result('[{"pid":123,"cancelled":true}]'), result('1')],
                        [result('[{"pid":123,"cancelled":false}]'), result('0')]]:
            with self.subTest(outputs=outputs):
                self.process.side_effect = outputs
                with self.assertRaises(RuntimeError): bench.cancel_application(self.app)

    def measure_patches(self, proc_result):
        self.denials['sql'].side_effect = None; self.denials['sql'].return_value = result('0')
        self.denials['guard'].side_effect = None
        self.process.side_effect = proc_result if isinstance(proc_result, BaseException) else None
        self.process.return_value = proc_result
        stack = contextlib.ExitStack(); self.addCleanup(stack.close)
        stack.enter_context(mock.patch.object(bench, 'owned_preflight'))
        stack.enter_context(mock.patch.object(bench, 'assert_quiet'))
        stack.enter_context(mock.patch.object(bench.etl, 'build_plan', return_value={'perfumes': [{}]*12, 'note_occurrences': 93}))
        stack.enter_context(mock.patch.object(bench.etl, 'validate_mapping'))
        body = 'BEGIN;SELECT 1;COMMIT;\n'
        importer = stack.enter_context(mock.patch.object(bench.etl, 'import_sql', return_value=body))
        return mock.Mock(spec=bench.RunLease, application=self.app), importer, body

    def test_timeout_cleanup_failure_preserves_unknown_commit_state(self):
        lease, _, _ = self.measure_patches(subprocess.TimeoutExpired('synthetic docker', 900))
        with mock.patch.object(bench, 'cancel_application', side_effect=RuntimeError('synthetic cancellation failure')) as cancel:
            with self.assertRaises(bench.BenchmarkDeadlineError) as caught:
                bench.measure({}, 'pilot', {}, 'fresh', lease, self.source_hash)
        cancel.assert_called_once_with(self.app)
        self.assertEqual(caught.exception.cancellation['status'], 'FAILED_OR_UNCONFIRMED')
        self.assertEqual(caught.exception.cancellation['commit_state'], 'UNKNOWN')

    def test_original_sql_failure_is_not_relaxed_or_retried(self):
        lease, importer, _ = self.measure_patches(result('', 1, '23514 Future review timestamp'))
        with self.assertRaisesRegex(RuntimeError, '23514 Future review timestamp'):
            bench.measure({}, 'pilot', {}, 'fresh', lease, self.source_hash)
        importer.assert_called_once_with({}, mock.ANY, {})
        self.assertEqual(self.process.call_count, 1)

    def test_timed_sql_wraps_original_importer_body_unchanged(self):
        lease, importer, body = self.measure_patches(result('{"dpt_etl_metrics":true}\n{"p104_backend_seconds":2.5}\n'))
        with mock.patch.object(bench, 'function_stats', return_value={'validate_model': {'calls': 1}, 'validate_images': {'calls': 1}}):
            row = bench.measure({}, 'pilot', {}, 'fresh', lease, self.source_hash)
        script = self.process.call_args.kwargs['input']
        self.assertIn('bench_started \\gset\n'+body+'SELECT clock_timestamp() AS bench_finished', script)
        self.assertEqual(script.count(body), 1); self.assertIn(self.app, script)
        self.assertEqual(row['backend_seconds'], 2.5)
        importer.assert_called_once_with({}, mock.ANY, {})

    def run_patches(self):
        stack = contextlib.ExitStack(); self.addCleanup(stack.close)
        stack.enter_context(mock.patch.object(bench, 'common_repository_root', return_value=self.root))
        stack.enter_context(mock.patch.object(bench.etl, 'load_snapshot', return_value={'artifacts': {}}))
        stack.enter_context(mock.patch.object(bench.etl, 'build_plan', return_value={}))
        validate = stack.enter_context(mock.patch.object(bench.etl, 'validate_mapping'))
        return stack, validate

    def test_invalid_mapping_precedes_reservation_or_any_resource_mutation(self):
        mappings = self.mappings(); _, validate = self.run_patches()
        validate.side_effect = ValueError('unreviewed mapping')
        with self.assertRaisesRegex(ValueError, 'unreviewed'): bench.run('source', *mappings, self.output)
        self.assertFalse(self.output.exists()); self.denials['sql'].assert_not_called()
        self.denials['docker'].assert_not_called()

    def test_resource_failure_is_reported_after_reservation_before_prepare(self):
        mappings = self.mappings(); stack, _ = self.run_patches()
        stack.enter_context(mock.patch.object(bench, 'attest_resources', side_effect=RuntimeError('bad resource cap')))
        prepare = stack.enter_context(mock.patch.object(bench, 'prepare'))
        with self.assertRaisesRegex(RuntimeError, 'bad resource cap'): bench.run('source', *mappings, self.output)
        report = json.loads(self.output.read_text())
        self.assertEqual(report['status'], 'FAILED_STOPPED')
        self.assertEqual(report['benchmark_sha256_at_entry'], self.source_hash)
        prepare.assert_not_called(); self.denials['sql'].assert_not_called()
        self.assertFalse((self.root/'.local/p104/benchmark.lease.json').exists())

    def test_existing_report_prevents_even_resource_preflight(self):
        mappings = self.mappings(); stack, _ = self.run_patches()
        preflight = stack.enter_context(mock.patch.object(bench, 'owned_preflight'))
        self.output.parent.mkdir(); self.output.write_text('existing evidence')
        with self.assertRaises(FileExistsError): bench.run('source', *mappings, self.output)
        preflight.assert_not_called(); self.assertEqual(self.output.read_text(), 'existing evidence')

    def test_pilot_method_records_hash_limits_and_excludes_warmup_from_medians(self):
        mappings = self.mappings(); stack, validate = self.run_patches()
        stack.enter_context(mock.patch.object(bench, 'owned_preflight', return_value=self.resource_host()))
        prepare = stack.enter_context(mock.patch.object(bench, 'prepare'))
        stack.enter_context(mock.patch.object(bench, 'size_inventory', return_value={}))
        seconds = iter([100, 1, 2, 3, 4, 5, 6])
        def measure(snapshot, cohort, mapping, label, lease, source_hash):
            lease.assert_owned()
            self.assertEqual(source_hash, self.source_hash)
            self.assertEqual(json.loads(self.output.read_text())['owner_nonce'], lease.nonce)
            return {'label': label, 'backend_seconds': next(seconds), 'function_stats': {'validate_model': {'calls': 1}}}
        stack.enter_context(mock.patch.object(bench, 'measure', side_effect=measure))
        with mock.patch('builtins.print'):
            report = bench.run('source', *mappings, self.output, full=False)
        self.assertEqual(report['pilot_medians'], {'fresh': 3, 'replay': 4})
        self.assertEqual(report['observed_resources']['Memory'], bench.MEMORY_BYTES)
        self.assertEqual(report['benchmark_sha256_at_entry'], self.source_hash)
        self.assertEqual(report['limits']['full_repetitions'], 0)
        self.assertEqual(validate.call_count, 2); self.assertEqual(prepare.call_count, 4)
        self.assertEqual(report['status'], 'MEASURED'); self.assertEqual(len(report['runs']), 7)
        self.denials['sql'].assert_not_called(); self.denials['docker'].assert_not_called()


if __name__ == '__main__': unittest.main()
