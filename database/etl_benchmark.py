"""Controlled local rehearsal of unchanged, independently reviewed Scento cohorts.

Only the existing disposable dpt_scento_test database can be recreated. This is not an
optimization, a mapping approval mechanism or an arbitrary-size production importer.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import secrets
import re
import statistics
import subprocess
import tempfile
import time

import local
import scento_etl as etl

DB = 'dpt_scento_test'
APPLICATION = 'dpt_p1_04_controlled_benchmark'
DEADLINE_SECONDS = 900
MEMORY_BYTES = 768 * 1024 * 1024
NANO_CPUS = 2_000_000_000


def _no_links(path):
    for item in (path, *path.parents):
        if item.is_symlink() or (hasattr(item, 'is_junction') and item.is_junction()):
            raise ValueError('Linked report/lease paths are refused')


def common_repository_root():
    """Resolve the common checkout, not a worktree-local lock directory."""
    def git(*args, cwd=local.ROOT):
        return subprocess.run(['git', '-C', str(cwd), *args], check=True,
            capture_output=True, text=True, timeout=10).stdout.strip()
    if Path(git('rev-parse', '--show-toplevel')).resolve() != local.ROOT.resolve():
        raise ValueError('Benchmark root is not the verified Git worktree')
    common = Path(git('rev-parse', '--path-format=absolute', '--git-common-dir'))
    _no_links(common)
    common = common.resolve()
    if common.name != '.git' or not (common/'HEAD').is_file() or not (common/'objects').is_dir():
        raise ValueError('Expected a non-bare common Git directory')
    root = common.parent
    if Path(git('rev-parse', '--path-format=absolute', '--git-common-dir', cwd=root)).resolve() != common:
        raise ValueError('Common Git checkout identity differs')
    return root


def report_path(value):
    path = Path(value).absolute()
    _no_links(path)
    path = path.resolve()
    base = (local.ROOT/'.local').resolve()
    if path == base or not path.is_relative_to(base):
        raise ValueError('Use a new ignored .local report path')
    return path


def _exclusive_json(path, value):
    # Never truncate an existing reservation, even between existence check and open.
    with path.open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n'); stream.flush(); os.fsync(stream.fileno())


def _owns(path, nonce):
    _no_links(path)
    try:
        if path.stat().st_size > 1_000_000:
            raise ValueError('Ownership record is unexpectedly large')
        owned = json.loads(path.read_text(encoding='utf-8')).get('owner_nonce') == nonce
    except (OSError, ValueError, AttributeError) as exc:
        raise RuntimeError('Ownership record unavailable; refusing mutation') from exc
    if not owned:
        raise RuntimeError('Ownership nonce differs; refusing mutation')


class RunLease:
    def __init__(self, root):
        self.path = root/'.local'/'p104'/'benchmark.lease.json'
        self.nonce = secrets.token_hex(12)
        self.application = APPLICATION+'_'+self.nonce

    def __enter__(self):
        _no_links(self.path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        _no_links(self.path)
        _exclusive_json(self.path, {'owner_nonce': self.nonce, 'pid': os.getpid(),
            'application': self.application, 'created_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
        return self

    def assert_owned(self):
        _owns(self.path, self.nonce)

    def __exit__(self, kind, value, traceback):
        self.assert_owned()
        self.path.unlink()  # No stale/foreign lease reclamation or automatic override.


class ReportFile:
    def __init__(self, path, nonce, source_hash):
        self.path = report_path(path)
        self.nonce = nonce
        self.path.parent.mkdir(parents=True, exist_ok=True)
        _no_links(self.path)
        _exclusive_json(self.path, {'owner_nonce': nonce, 'status': 'RESERVED',
            'benchmark_sha256_at_entry': source_hash})

    def checkpoint(self, report):
        _owns(self.path, self.nonce)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8',
                    dir=self.path.parent, prefix=self.path.name+'.', suffix='.tmp', delete=False) as stream:
                temporary = Path(stream.name)
                json.dump({**report, 'owner_nonce': self.nonce}, stream, indent=2)
                stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
            _owns(self.path, self.nonce)
            temporary.replace(self.path)
        finally:
            if temporary is not None and temporary.exists():
                temporary.unlink()


def attest_resources():
    local.guard()
    info = json.loads(local.docker('inspect', local.CONTAINER).stdout)[0]
    host = info['HostConfig']
    observed = {key: host.get(key) for key in
        ('Memory', 'MemorySwap', 'NanoCpus', 'CpuQuota', 'CpuPeriod', 'CpusetCpus')}
    nano = host.get('NanoCpus', 0)
    quota, period = host.get('CpuQuota', 0), host.get('CpuPeriod', 0)
    quota_ok = quota in (0, -1) or (period > 0 and quota == 2 * period)
    cpu_ok = (nano == NANO_CPUS and quota_ok) or (nano == 0 and period > 0 and quota == 2 * period)
    if host.get('Memory') != MEMORY_BYTES or not cpu_ok or host.get('CpusetCpus'):
        raise RuntimeError('Current Docker resource bounds differ: '+json.dumps(observed))
    return observed


def assert_quiet():
    active = json.loads(local.sql("SELECT coalesce(jsonb_agg(jsonb_build_object('database',datname,"
        "'application',application_name,'state',state,'pid',pid)),'[]'::jsonb) FROM pg_stat_activity WHERE pid<>pg_backend_pid() "
        "AND backend_type='client backend';", 'postgres').stdout)
    if active:
        raise RuntimeError('Controlled benchmark requires no other DB client, including idle: '+json.dumps(active))


def size_inventory(db):
    if db not in {DB, 'dpt_scento_pilot', 'dpt_migration_probe'}:
        raise ValueError('Size target outside local task allowlist')
    tables = json.loads(local.sql("""SELECT jsonb_agg(jsonb_build_object(
      'schema',n.nspname,'table',c.relname,'heap_bytes',pg_relation_size(c.oid),
      'table_bytes_including_toast_aux',pg_table_size(c.oid),'index_bytes',pg_indexes_size(c.oid),
      'toast_total_bytes',CASE WHEN c.reltoastrelid=0 THEN 0 ELSE pg_total_relation_size(c.reltoastrelid) END,
      'total_bytes',pg_total_relation_size(c.oid)) ORDER BY n.nspname,c.relname)
      FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
      WHERE c.relkind='r' AND n.nspname IN ('dpt','dpt_ops');""",db).stdout)
    count_fields = []
    for row in tables:
        # Names come from the verified local catalogue, never a caller-controlled identifier.
        count_fields.extend([etl.q(row['schema']+'.'+row['table']),
            '(SELECT count(*) FROM "'+row['schema']+'"."'+row['table']+'")'])
    counts=json.loads(local.sql('SELECT jsonb_build_object('+','.join(count_fields)+');',db).stdout)
    return {'database_bytes':int(local.sql('SELECT pg_database_size(current_database());',db).stdout),
            'relations':tables,'row_counts':counts,
            'accounting':'table_bytes includes TOAST/FSM/VM; total=table+indexes. Do not add TOAST twice. Database includes system catalogues.'}


def function_stats():
    return json.loads(local.sql("""SELECT coalesce(jsonb_object_agg(funcname,jsonb_build_object(
      'calls',calls,'total_ms',total_time,'self_ms',self_time)),'{}'::jsonb)
      FROM pg_stat_user_functions WHERE schemaname='dpt_guard';""",DB).stdout)


def owned_preflight(lease, source_hash):
    lease.assert_owned()
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != source_hash:
        raise RuntimeError('Benchmark source changed during the run')
    resources = attest_resources()
    assert_quiet()
    return resources


def client_args(db):
    return ['docker','--context','desktop-linux','exec','-i','--user','postgres',local.CONTAINER,
            'psql','-X','-q','-A','-t','-v','ON_ERROR_STOP=1','-v','VERBOSITY=verbose','-U','postgres','-d',db]


def cancel_application(application):
    if not re.fullmatch(re.escape(APPLICATION)+r'_[0-9a-f]{24}', application):
        raise ValueError('Refusing cancellation without a unique benchmark identity')
    # The cancellation client itself has a bound and never matches a shared prefix.
    match = "datname="+etl.q(DB)+" AND application_name="+etl.q(application)+" AND backend_type='client backend'"
    def control(sql):
        local.guard()
        result = subprocess.run(client_args('postgres'), input=sql, text=True, encoding='utf-8',
            capture_output=True, timeout=15)
        if result.returncode:
            raise RuntimeError('Cancellation control failed: '+result.stderr.strip())
        return json.loads(result.stdout)
    requested = control("SELECT coalesce(jsonb_agg(jsonb_build_object('pid',pid,'cancelled',pg_cancel_backend(pid))),'[]'::jsonb) FROM pg_stat_activity WHERE "+match+';')
    remaining = control('SELECT count(*) FROM pg_stat_activity WHERE '+match+';')
    if remaining or any(not row['cancelled'] for row in requested):
        raise RuntimeError('Cancellation/exit unconfirmed; inspect inventory and sessions before retry')
    return {'status': 'REQUESTED_AND_NO_MATCHING_SESSION', 'requests': requested,
            'remaining_sessions': remaining, 'commit_state': 'UNKNOWN; cancellation does not prove rollback'}


class BenchmarkDeadlineError(RuntimeError):
    def __init__(self, cancellation):
        self.cancellation = cancellation
        super().__init__('Whole-client deadline exceeded; commit state unknown; '+json.dumps(cancellation))


def measure(snapshot, cohort, mapping, label, lease, source_hash):
    plan=etl.build_plan(snapshot,cohort)
    etl.validate_mapping(mapping,plan,snapshot)
    owned_preflight(lease, source_hash)
    local.sql('SELECT pg_stat_reset();',DB)
    body=etl.import_sql(snapshot,plan,mapping)
    script="SET application_name='"+lease.application+"';SET track_functions='pl';\n"
    script+="SELECT clock_timestamp() AS bench_started \\gset\n"+body
    script+="SELECT clock_timestamp() AS bench_finished \\gset\nSELECT pg_stat_force_next_flush();\n"
    script+="SELECT jsonb_build_object('p104_backend_seconds',extract(epoch FROM :'bench_finished'::timestamptz-:'bench_started'::timestamptz));\n"
    local.guard();started=time.perf_counter()
    args=client_args(DB)
    try:
        result=subprocess.run(args,input=script,text=True,encoding='utf-8',capture_output=True,
                              timeout=DEADLINE_SECONDS)
    except subprocess.TimeoutExpired as exc:
        try:
            cancellation = cancel_application(lease.application)
        except Exception as cleanup:
            cancellation = {'status': 'FAILED_OR_UNCONFIRMED', 'error': str(cleanup), 'commit_state': 'UNKNOWN'}
        # Cancellation is not evidence that an already-completed COMMIT was rolled back.
        raise BenchmarkDeadlineError(cancellation) from exc
    elapsed=time.perf_counter()-started
    if result.returncode:
        raise RuntimeError('Benchmark failed with original validation enabled: '+result.stderr.strip())
    lease.assert_owned()
    assert_quiet()
    objects=[json.loads(line) for line in result.stdout.splitlines() if line.strip().startswith('{')]
    observed=next(row for row in objects if row.get('dpt_etl_metrics'))
    backend=next(row['p104_backend_seconds'] for row in objects if 'p104_backend_seconds' in row)
    calls=function_stats()
    for name in ['validate_model','validate_images']:
        if calls.get(name,{}).get('calls')!=1:
            raise RuntimeError('Expected exactly one final full validator per intact transaction: '+name)
    if int(local.sql('SELECT count(*) FROM dpt_ops.validation_pending;',DB).stdout):
        raise RuntimeError('Pending validation marker after COMMIT')
    return {'label':label,'cohort':cohort,'perfumes':len(plan['perfumes']),
            'raw_note_occurrences':plan['note_occurrences'],'backend_seconds':float(backend),
            'guarded_client_seconds':round(elapsed,6),'function_stats':calls,'observed':observed,
            'outcome':'COMMITTED_FINAL_VALIDATORS_VERIFIED','pending_markers':0}


def prepare(lease, source_hash):
    owned_preflight(lease, source_hash)
    # A newly connected client makes normal DROP fail; never evict it with FORCE.
    local.sql('DROP DATABASE IF EXISTS "'+DB+'";', 'postgres')
    local.sql('CREATE DATABASE "'+DB+'";', 'postgres')
    owned_preflight(lease, source_hash)
    local.migrate(DB)


def run(source, pilot_mapping, full_mapping, output, full=True):
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output=report_path(output)
    snapshot=etl.load_snapshot(source)
    mappings={'pilot':json.loads(Path(pilot_mapping).read_text(encoding='utf-8')),
              'full':json.loads(Path(full_mapping).read_text(encoding='utf-8'))}
    # Fail before any test reset if either source/mapping policy is unreviewed or mismatched.
    for cohort,mapping in mappings.items():etl.validate_mapping(mapping,etl.build_plan(snapshot,cohort),snapshot)
    with RunLease(common_repository_root()) as lease:
        destination = ReportFile(output, lease.nonce, source_hash)
        return run_owned(snapshot, mappings, destination, lease, source_hash, full)


def run_owned(snapshot, mappings, destination, lease, source_hash, full):
    report={'task':'IMP-P1-04','started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'database':DB,'image':local.IMAGE,'source_revision':etl.REV,'source_artifacts':snapshot['artifacts'],
      'benchmark_sha256_at_entry':source_hash, 'application':lease.application,
      'lease_path':str(lease.path),
      'importer_sha256':hashlib.sha256(Path(etl.__file__).read_bytes()).hexdigest(),
      'mapping_sha256':{k:etl.digest(v) for k,v in mappings.items()},'runs':[],
      'limits':{'whole_client_deadline_seconds':DEADLINE_SECONDS,'per_statement_seconds':45,
                'memory_mib':768,'cpus':2,'pilot_repetitions':3,'full_repetitions':int(full)},
      'method':'Common-checkout exclusive lease for cooperating jobs; reject all other DB client sessions including idle. Normal DROP never forces eviction. One pilot warmup excluded from medians, three fresh pilot/import+replay pairs, optional one full pair; original SQL/security intact.',
      'setup_and_cache_method':{'fresh':'Recreate only dpt_scento_test and apply all original migrations outside timing; no FORCE drop',
        'replay':'Same intact reviewed cohort immediately after its fresh import; no reset between pair',
        'cache':'Warm OS/Docker/PostgreSQL environment; no cache flushing or cold-cache claim',
        'timing':'Backend wall timer brackets streamed original SQL including natural COMMIT; client timer includes Docker/psql, excludes preparation and statistics readback'},
      'limitations':['One full pair is descriptive, not statistical capacity or an optimization comparison',
        'Function tracking and Docker/local client overhead present; setup/statistics read excluded from backend timer',
        'READ COMMITTED and original global writer serialization retained; no parallel throughput claim',
        'Noncooperating external clients can ignore the lease; quiet snapshots are not a server-wide exclusion lock',
        'No image/provider/API/UI/production benchmark']}
    def checkpoint():
        lease.assert_owned()
        destination.checkpoint(report)
    try:
        report['observed_resources']=owned_preflight(lease, source_hash)
        checkpoint()  # Reserved/owned evidence and actual limits precede DB mutation.
        prepare(lease, source_hash);report['empty_sizes']=size_inventory(DB)
        row=measure(snapshot,'pilot',mappings['pilot'],'warmup',lease,source_hash);report['runs'].append(row);checkpoint()
        for n in range(1,4):
            prepare(lease, source_hash)
            for label in ['fresh','replay']:
                row=measure(snapshot,'pilot',mappings['pilot'],f'pilot_{label}_{n}',lease,source_hash);report['runs'].append(row)
                print(json.dumps({'label':row['label'],'seconds':row['backend_seconds'],'model_calls':row['function_stats']['validate_model']['calls']}),flush=True);checkpoint()
        if full:
            prepare(lease, source_hash)
            for label in ['fresh','replay']:
                row=measure(snapshot,'full',mappings['full'],'full_'+label,lease,source_hash);report['runs'].append(row)
                print(json.dumps({'label':row['label'],'seconds':row['backend_seconds'],'model_calls':row['function_stats']['validate_model']['calls']}),flush=True);checkpoint()
            report['full_sizes_before_analyze']=size_inventory(DB)
            owned_preflight(lease, source_hash)
            local.sql('VACUUM (ANALYZE);',DB)
            report['full_sizes_after_vacuum_analyze']=size_inventory(DB)
            report['explain_admin_read_only']=json.loads(local.sql("EXPLAIN (ANALYZE,BUFFERS,FORMAT JSON) SELECT id,name FROM dpt.perfumes WHERE access_scope_id="+etl.q(etl.SCOPE_ID)+" AND review_status='approved' ORDER BY name,id LIMIT 20;",DB).stdout)
        report['pilot_medians']={kind:statistics.median(row['backend_seconds'] for row in report['runs'] if row['label'].startswith('pilot_'+kind)) for kind in ['fresh','replay']}
        report['status']='MEASURED';report['finished_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();checkpoint()
    except Exception as exc:
        report['status']='FAILED_STOPPED';report['failure']=str(exc)
        if isinstance(exc, BenchmarkDeadlineError): report['cancellation']=exc.cancellation
        checkpoint();raise
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-dir',required=True)
    p.add_argument('--pilot-mapping',required=True);p.add_argument('--full-mapping',required=True)
    p.add_argument('--report',required=True);p.add_argument('--pilot-only',action='store_true');a=p.parse_args()
    run(a.source_dir,a.pilot_mapping,a.full_mapping,a.report,not a.pilot_only)


if __name__=='__main__':main()
