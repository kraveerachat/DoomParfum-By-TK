"""Synthetic transactional regression controls for coalesced deferred validation."""
import concurrent.futures
import json
import sys
from pathlib import Path
import time
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import local
from fixtures import baseline, uid, q, insert
from performance import workload


class DeferredPerformanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local.recreate('dpt_schema_test');local.migrate('dpt_schema_test');local.sql(baseline())

    def scalar(self,text,user='postgres'):
        return local.sql(text,user=user).stdout.strip()

    def reject(self,text,user='postgres'):
        result=local.sql('BEGIN;'+text+'COMMIT;',user=user,check=False)
        self.assertNotEqual(result.returncode,0,'Invalid transaction committed')
        self.assertIn('23514',result.stderr)

    def empty_queue(self):
        self.assertEqual(self.scalar('SELECT count(*) FROM dpt_ops.validation_pending;'),'0')

    def counts(self,text):
        query="""SELECT jsonb_object_agg(funcname,calls) FROM pg_stat_xact_user_functions
          WHERE schemaname='dpt_guard' AND funcname IN ('validate_model','validate_images','validate_all_deferred');"""
        out=local.sql("BEGIN;SET LOCAL track_functions='pl';"+text+'SET CONSTRAINTS ALL IMMEDIATE;'+query+'ROLLBACK;').stdout.strip()
        return json.loads(out)

    def test_bulk_insert_update_delete_coalesces_both_global_scans(self):
        text=workload(25)+"UPDATE dpt.brands SET name='SYNTHETIC updated' WHERE slug LIKE 'synthetic-perf-%';"
        text+="DELETE FROM dpt.brands WHERE slug LIKE 'synthetic-perf-%'; DELETE FROM dpt.entities WHERE id IN ("+','.join(q(uid('SYNTHETIC-PERF-'+str(i))) for i in range(25))+');'
        counts=self.counts(text)
        self.assertEqual(counts['validate_model'],1);self.assertEqual(counts['validate_images'],1)
        self.assertGreater(counts['validate_all_deferred'],100)
        self.empty_queue()

    def test_later_writes_after_explicit_flush_rearm_validation(self):
        first=insert('users',id=uid('epoch-user'),auth_subject='SYNTHETIC epoch user')
        text=first+"SET CONSTRAINTS ALL IMMEDIATE;SET CONSTRAINTS ALL DEFERRED;"
        text+=f"UPDATE dpt.perfumes SET name='SYNTHETIC new epoch' WHERE id={q(uid('perfume2'))};"
        counts=self.counts(text)
        self.assertEqual(counts['validate_model'],2);self.assertEqual(counts['validate_images'],2)
        for bad in [insert('entities',id=uid('late-orphan'),access_scope_id=uid('public'),kind='note'),
                    f"UPDATE dpt.perfumes SET name='Unselected' WHERE id={q(uid('perfume'))};",
                    f"DELETE FROM dpt.perfume_notes WHERE id={q(uid('top-join'))};"]:
            with self.subTest(bad=bad[:45]):self.reject(first+'SET CONSTRAINTS ALL IMMEDIATE;SET CONSTRAINTS ALL DEFERRED;'+bad)
        self.empty_queue()

    def test_actual_commit_and_rollback_cleanup_transaction_state(self):
        text=insert('users',id=uid('committed-user'),auth_subject='SYNTHETIC committed user')
        local.sql('BEGIN;'+text+'COMMIT;')
        self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.users WHERE id={q(uid('committed-user'))};"),'1')
        self.empty_queue()
        local.sql('BEGIN;'+insert('users',id=uid('rolled-user'),auth_subject='SYNTHETIC rolled user')+'ROLLBACK;')
        self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.users WHERE id={q(uid('rolled-user'))};"),'0')
        self.empty_queue()

    def test_noop_replay_and_zero_row_statements_leave_no_queue_rows(self):
        replay=insert('users',id=uid('alice'),auth_subject='dpt_test_alice').replace(');\n',') ON CONFLICT DO NOTHING;\n')
        for mode in ['', 'SET CONSTRAINTS ALL IMMEDIATE;', 'SET CONSTRAINTS dpt_ops.validation_pending_flush IMMEDIATE;']:
            with self.subTest(mode=mode):
                local.sql('BEGIN;'+mode+replay+f"UPDATE dpt.users SET display_name='none' WHERE id={q(uid('absent'))};COMMIT;")
                self.empty_queue()

    def test_named_queue_immediate_cannot_flush_before_domain_mutation(self):
        self.reject('SET CONSTRAINTS dpt_ops.validation_pending_flush IMMEDIATE;'+insert('entities',id=uid('queue-immediate-orphan'),access_scope_id=uid('public'),kind='brand'))
        local.sql('BEGIN;SET CONSTRAINTS dpt_ops.validation_pending_flush IMMEDIATE;'+f"UPDATE dpt.perfumes SET name='SYNTHETIC valid immediate' WHERE id={q(uid('perfume2'))};ROLLBACK;")
        self.empty_queue()

    def test_named_domain_immediate_mode_keeps_old_invariant(self):
        self.reject('SET CONSTRAINTS dpt.z_model_contract IMMEDIATE;'+insert('entities',id=uid('domain-immediate-orphan'),access_scope_id=uid('public'),kind='brand'))
        self.empty_queue()

    def test_savepoint_rollback_restores_dirty_epoch_and_pending_events(self):
        good=insert('users',id=uid('savepoint-user'),auth_subject='SYNTHETIC savepoint user')
        bad=insert('entities',id=uid('savepoint-orphan'),access_scope_id=uid('public'),kind='note')
        local.sql('BEGIN;'+good+'SAVEPOINT s;'+bad+'ROLLBACK TO s;COMMIT;')
        self.empty_queue()
        self.reject('SET CONSTRAINTS ALL IMMEDIATE;SET CONSTRAINTS ALL DEFERRED;SAVEPOINT s;'+good.replace('savepoint user','another user').replace(uid('savepoint-user'),uid('savepoint-user2'))+'ROLLBACK TO s;'+bad)
        self.empty_queue()

    def test_caught_failed_flush_cannot_mark_invalid_transaction_clean(self):
        bad=insert('entities',id=uid('caught-orphan'),access_scope_id=uid('public'),kind='note')
        catch="DO $$BEGIN BEGIN SET CONSTRAINTS ALL IMMEDIATE; EXCEPTION WHEN check_violation THEN NULL; END; END$$;"
        self.reject(bad+catch)
        repair=insert('notes',id=uid('caught-orphan'),access_scope_id=uid('public'),name='SYNTHETIC repaired',slug='synthetic-repaired')
        local.sql('BEGIN;'+bad+catch+repair+'COMMIT;')
        self.empty_queue()

    def test_queue_and_helpers_are_not_client_mutation_capabilities(self):
        for query in ['SELECT * FROM dpt_ops.validation_pending;', 'DELETE FROM dpt_ops.validation_pending;',
                      'SELECT dpt_guard.schedule_validation();','SELECT dpt_guard.serialize_write();','SELECT dpt_guard.validate_all_deferred();']:
            result=local.sql(query,user='dpt_test_alice',check=False)
            self.assertNotEqual(result.returncode,0);self.assertIn('42501',result.stderr)
        script="GRANT dpt_writer TO dpt_test_alice;SET SESSION AUTHORIZATION dpt_test_alice;SET app.validation_clean='true';"
        script+='CREATE TEMP TABLE validation_pending(transaction_id xid8,generation bigint);'
        script+=insert('entities',id=uid('spoofed-clean-orphan'),access_scope_id=uid('alice'),kind='note')
        self.reject(script)
        self.empty_queue()

    def test_two_transactions_do_not_share_dirty_state(self):
        valid='BEGIN;'+insert('users',id=uid('parallel-valid'),auth_subject='SYNTHETIC parallel valid')+'SELECT pg_sleep(0.5);COMMIT;'
        invalid='BEGIN;'+insert('entities',id=uid('parallel-invalid'),access_scope_id=uid('public'),kind='note')+'COMMIT;'
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(local.sql,valid,check=False);time.sleep(0.15);b=pool.submit(local.sql,invalid,check=False)
            first,second=a.result(),b.result()
        self.assertEqual(first.returncode,0);self.assertNotEqual(second.returncode,0);self.assertIn('23514',second.stderr)
        self.empty_queue()


if __name__=='__main__':unittest.main(verbosity=2)
