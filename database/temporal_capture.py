"""Bounded diagnostic-only operand capture. No production/importer/migration change.

Run once for new diagnostic evidence, not as an ETL retry mechanism. All target data
are SYNTHETIC. A deliberate future control proves captureability, not historical cause.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
from pathlib import Path
import re
import secrets
import subprocess
import time
import uuid

import etl_benchmark as bench
import local
import recovery

TASK = 'IMP-P1-04-TEMPORAL'
DB = 'dpt_temporal_test'
ORIGINAL_SHA = 'c7a0a152b5d6b072168f3c439f9f033fc0e5f6bcf66aebb1104a347959000441'
PREDICATE = "IF NEW.reviewed_at>clock_timestamp() THEN RAISE EXCEPTION 'Future review timestamp' USING ERRCODE='23514'; END IF;"
MARKER = 'DPT_TEMPORAL_OPERANDS_V1'
TRIAL_LIMIT = 128
WALL_SECONDS = 240


def uid(key):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, 'doomparfum:synthetic:temporal:'+key))


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def instrument(original):
    """Sample exactly once where the original comparison samples; never offset time."""
    if digest(original) != ORIGINAL_SHA or original.count(PREDICATE) != 1:
        raise ValueError('Original guard pin/predicate differs; refusing instrumentation')
    declaration = 'DECLARE obs dpt.source_observations;'
    if original.count(declaration) != 1:
        raise ValueError('Original declaration differs')
    details = """jsonb_build_object('marker','DPT_TEMPORAL_OPERANDS_V1',
      'entity_id',NEW.entity_id,'observation_id',NEW.observation_id,
      'field_path',NEW.field_path,'operation',TG_OP,
      'reviewed_at',NEW.reviewed_at,'comparison_clock',comparison_clock,
      'statement_clock',statement_timestamp(),'transaction_clock',transaction_timestamp(),
      'delta_microseconds',extract(epoch FROM NEW.reviewed_at-comparison_clock)*1000000,
      'review_equals_statement',NEW.reviewed_at=statement_timestamp())::text"""
    replacement = """comparison_clock:=clock_timestamp();
  IF NEW.reviewed_at>comparison_clock THEN
    RAISE EXCEPTION 'Future review timestamp' USING ERRCODE='23514', DETAIL="""+details+""";
  END IF;
  RAISE NOTICE '%', """+details+';'
    return original.replace(declaration, declaration+' comparison_clock timestamptz;').replace(
        PREDICATE, replacement)


def operands(stderr):
    rows = []
    for line in stderr.splitlines():
        if MARKER not in line or '{' not in line:
            continue
        row = json.loads(line[line.index('{'):])
        required = {'marker','entity_id','observation_id','field_path','operation','reviewed_at',
            'comparison_clock','statement_clock','transaction_clock','delta_microseconds',
            'review_equals_statement'}
        if set(row) != required or row['marker'] != MARKER:
            raise ValueError('Unexpected diagnostic fields')
        for key in ['entity_id','observation_id']:
            uuid.UUID(row[key])
        reviewed = datetime.datetime.fromisoformat(row['reviewed_at'])
        compared = datetime.datetime.fromisoformat(row['comparison_clock'])
        statement = datetime.datetime.fromisoformat(row['statement_clock'])
        transaction = datetime.datetime.fromisoformat(row['transaction_clock'])
        if any(value.utcoffset() is None for value in [reviewed,compared,statement,transaction]):
            raise ValueError('Diagnostic clocks must have timezone')
        if (type(row['review_equals_statement']) is not bool
            or row['review_equals_statement'] != (reviewed==statement)
            or row['operation'] not in {'INSERT','UPDATE'}
            or not isinstance(row['field_path'],str) or not row['field_path'].strip()
            or type(row['delta_microseconds']) not in {int,float}
            or not math.isfinite(row['delta_microseconds'])):
            raise ValueError('Invalid diagnostic clock metadata')
        actual = (reviewed-compared)//datetime.timedelta(microseconds=1)
        if actual != row['delta_microseconds']:
            raise ValueError('Diagnostic delta differs from captured operands')
        rows.append(row)
    return rows


def mount_sources(path):
    """Exact local path and the observed Docker Desktop drive translation only."""
    resolved = path.resolve()
    result = {str(resolved)}
    posix = resolved.as_posix()
    if re.match(r'^[A-Za-z]:/',posix):
        result.add('/run/desktop/mnt/host/'+posix[0].lower()+posix[2:])
    return result


class Target:
    def __init__(self, nonce, state):
        if not re.fullmatch('[0-9a-f]{24}', nonce):
            raise ValueError('Invalid ownership nonce')
        self.nonce = nonce
        self.container = 'doomparfum-p104-temporal-'+nonce
        self.volume = self.container+'-data'
        self.state = recovery.private_path(state)
        self.password = self.state/'postgres-password'
        self.deadline = time.monotonic()+WALL_SECONDS
        self.cleaning = False
        self.cleanup_deadline = None

    def command(self, *args, input=None, check=True):
        deadline = self.cleanup_deadline if self.cleaning else self.deadline
        remaining = deadline-time.monotonic()
        if remaining <= 0:
            raise TimeoutError('Bounded diagnostic deadline exhausted')
        endpoint = subprocess.run(['docker','--context','desktop-linux','context','inspect',
            'desktop-linux','--format','{{.Endpoints.docker.Host}}'],capture_output=True,
            text=True,timeout=min(5,remaining),check=True).stdout.strip()
        if not endpoint.startswith(('npipe:////./pipe/','unix:///')):
            raise ValueError('Non-local Docker endpoint refused')
        remaining = deadline-time.monotonic()
        if remaining <= 0:
            raise TimeoutError('Bounded diagnostic deadline exhausted')
        result = subprocess.run(['docker','--context','desktop-linux',*args],input=input,
            text=True,encoding='utf-8',capture_output=True,timeout=min(20,remaining))
        if check and result.returncode:
            raise RuntimeError('Owned temporal command failed; no generic retry')
        return result

    def attest(self):
        info = json.loads(self.command('inspect',self.container).stdout)[0]
        host = info['HostConfig']
        labels = info['Config'].get('Labels',{})
        mounts = info['Mounts']
        requested_mounts = host.get('Mounts',[])
        if (labels.get('com.doomparfum.task') != TASK or labels.get('com.doomparfum.run') != self.nonce
            or info['Config']['Image'] != local.IMAGE or host['NetworkMode'] != 'none'
            or host.get('PortBindings') or host['Memory'] != 512*1024**2
            or host['NanoCpus'] != 1_000_000_000 or len(mounts) != 2
            or not any(m.get('Type')=='bind' and m.get('Source') in mount_sources(self.password)
                and m.get('Target')=='/run/secrets/postgres-password' and m.get('ReadOnly')
                for m in requested_mounts)
            or not any(m.get('Type')=='volume' and m.get('Name')==self.volume
                and m.get('Destination')=='/var/lib/postgresql/data' for m in mounts)
            or not any(m.get('Type')=='bind' and m.get('Source') in mount_sources(self.password)
                and m.get('Destination')=='/run/secrets/postgres-password' and not m.get('RW') for m in mounts)):
            raise RuntimeError('Temporal target differs from owned isolated resource contract')
        volume = json.loads(self.command('volume','inspect',self.volume).stdout)[0]
        if volume.get('Labels',{}).get('com.doomparfum.task') != TASK or volume['Labels'].get('com.doomparfum.run') != self.nonce:
            raise RuntimeError('Temporal volume ownership differs')
        manifest = json.loads((self.state/'ownership.json').read_text())
        if manifest != {'nonce':self.nonce,'container':self.container,'volume':self.volume,'image':local.IMAGE}:
            raise RuntimeError('Local ownership record differs')

    def start(self):
        # Fresh unique names only. Never adopt, reset or evict a preexisting target.
        for args in [('inspect',self.container),('volume','inspect',self.volume)]:
            if self.command(*args,check=False).returncode == 0:
                raise RuntimeError('Preexisting target name refused')
        self.state.mkdir(parents=True,exist_ok=False)
        recovery.persist_private(self.password,secrets.token_urlsafe(40).encode('ascii'))
        recovery.persist_private(self.state/'ownership.json',json.dumps({
            'nonce':self.nonce,'container':self.container,'volume':self.volume,'image':local.IMAGE}).encode())
        labels = ['--label','com.doomparfum.task='+TASK,'--label','com.doomparfum.run='+self.nonce]
        self.command('volume','create',*labels,self.volume)
        self.command('run','-d','--pull=never','--name',self.container,*labels,
            '--network','none','--memory','512m','--cpus','1',
            '--mount','type=volume,source='+self.volume+',target=/var/lib/postgresql/data',
            '--mount','type=bind,source='+str(self.password)+',target=/run/secrets/postgres-password,readonly',
            '-e','POSTGRES_PASSWORD_FILE=/run/secrets/postgres-password','-e','POSTGRES_DB='+DB,local.IMAGE)
        self.attest()
        for _ in range(20):
            if self.command('exec',self.container,'pg_isready','-U','postgres',check=False).returncode == 0:
                return
            time.sleep(.2)
        raise RuntimeError('Temporal target readiness deadline exhausted')

    def sql(self, text, *, user='postgres'):
        if user not in {'postgres','dpt_temporal_guest'}:
            raise ValueError('Unexpected diagnostic role')
        self.attest()
        return self.command('exec','-i','--user','postgres',self.container,
            'psql','-X','-q','-A','-t','-v','ON_ERROR_STOP=1','-v','VERBOSITY=verbose',
            '-U',user,'-d',DB,input="SET statement_timeout='5s';SET lock_timeout='1s';\n"+text,check=False)

    def checked(self, text):
        r = self.sql(text)
        if r.returncode:
            raise RuntimeError('Temporal SQL failed: '+r.stderr.strip())
        return r.stdout.strip()


def fixture():
    scope,source,right,record,brand,obs = [uid(k) for k in ['scope','source','right','record','brand','obs']]
    return f"""BEGIN;
CREATE ROLE dpt_temporal_guest LOGIN NOSUPERUSER NOBYPASSRLS;
GRANT dpt_runtime,dpt_writer TO dpt_temporal_guest;
INSERT INTO dpt.access_scopes(id,kind) VALUES('{scope}','public');
INSERT INTO dpt.sources(id,access_scope_id,name,kind,entry_url,publisher)
 VALUES('{source}','{scope}','SYNTHETIC temporal fixture','user','https://example.invalid/temporal','SYNTHETIC ONLY');
INSERT INTO dpt.rights_assessments(id,access_scope_id,source_id,scope,evidence_url,license_code,
 research_use,automation_use,cache_use,storage_use,display_use,redistribution_use,ai_use,attribution,checked_at,reviewer)
 VALUES('{right}','{scope}','{source}','SYNTHETIC not a grant','https://example.invalid/test','TEST-ONLY',
 'allowed','allowed','allowed','allowed','allowed','restricted','unknown','SYNTHETIC',statement_timestamp(),'SYNTHETIC');
INSERT INTO dpt.source_records(id,access_scope_id,source_id,external_key,payload_sha256,source_url,locator,source_revision,retrieved_at,rights_id)
 VALUES('{record}','{scope}','{source}','SYNTHETIC-temporal','{'a'*64}','https://example.invalid/capture','SYNTHETIC','SYNTHETIC',statement_timestamp(),'{right}');
INSERT INTO dpt.entities(id,access_scope_id,kind) VALUES('{brand}','{scope}','brand');
INSERT INTO dpt.brands(id,access_scope_id,name,slug) VALUES('{brand}','{scope}','SYNTHETIC Temporal Brand','synthetic-temporal-brand');
INSERT INTO dpt.source_observations(id,access_scope_id,entity_id,entity_kind,field_path,source_record_id,
 claim_locator,claim_key,value,value_status,transform_version)
 VALUES('{obs}','{scope}','{brand}','brand','name','{record}','/name','SYNTHETIC','"SYNTHETIC Temporal Brand"','present','SYNTHETIC');
{selection('statement_timestamp()')}
COMMIT;"""


def selection(expression):
    if expression not in {'statement_timestamp()', "statement_timestamp()+interval '1 day'"}:
        raise ValueError('Unapproved diagnostic timestamp expression')
    return f"""INSERT INTO dpt.canonical_selections(access_scope_id,entity_id,entity_kind,field_path,
 observation_id,reviewed_by,rationale,reviewed_at) VALUES('{uid('scope')}','{uid('brand')}','brand','name',
 '{uid('obs')}','postgres','SYNTHETIC temporal diagnostic only',{expression}) ON CONFLICT DO NOTHING;"""


def controls(target, label):
    before = recovery.fingerprint(target.checked)
    result = []
    cases = [
        ('current_conflict',selection('statement_timestamp()'),None,'postgres'),
        ('future_SYNTHETIC',selection("statement_timestamp()+interval '1 day'"),'23514','postgres'),
        ('revoked_SYNTHETIC',f"UPDATE dpt.rights_assessments SET revoked_at=clock_timestamp() WHERE id='{uid('right')}';"+selection('statement_timestamp()'),'23514','postgres'),
        ('unauthorized_SYNTHETIC',selection('statement_timestamp()'),'42501','dpt_temporal_guest'),
        ('deferred_contrary_SYNTHETIC',f"UPDATE dpt.brands SET name='SYNTHETIC contrary' WHERE id='{uid('brand')}';",'23514','postgres')]
    for name,body,expected,user in cases:
        r = target.sql('BEGIN;'+body+'COMMIT;',user=user)
        if expected:
            if r.returncode == 0 or expected not in r.stderr:
                raise RuntimeError('Expected control rejection absent: '+name)
        elif r.returncode:
            raise RuntimeError('Current-time control rejected: '+r.stderr)
        if recovery.fingerprint(target.checked) != before:
            raise RuntimeError('Control changed data/security/roles: '+name)
        rows = operands(r.stderr)
        if label == 'instrumented' and name == 'future_SYNTHETIC':
            if len(rows)!=1 or rows[0]['delta_microseconds']<=0 or rows[0]['review_equals_statement']:
                raise RuntimeError('Synthetic future capture selftest failed')
        result.append({'name':name,'exit_code':r.returncode,'expected_sqlstate':expected,
            'message':next((x for x in r.stderr.splitlines() if 'ERROR:' in x),None),
            'operands':rows,'data_security_roles_unchanged':True})
    return result


def run(output, trials=8):
    if type(trials) is not int or not 1 <= trials <= TRIAL_LIMIT:
        raise ValueError('Use 1..128 trials; no automatic equivalent reruns')
    output = bench.report_path(output)
    code_hash = digest(Path(__file__).read_text(encoding='utf-8'))
    with bench.RunLease(bench.common_repository_root()) as lease:
        destination = bench.ReportFile(output,lease.nonce,code_hash)
        target = Target(lease.nonce,output.with_suffix('.state'))
        report = {'task':'IMP-P1-04','kind':'ISOLATED_SYNTHETIC_BOUNDED_CAPTURE','source_sha256':code_hash,
            'image':local.IMAGE,'trials_limit':trials,'whole_run_seconds':WALL_SECONDS,
            'observer_effect':'Decision semantics equivalent; instrumentation may alter timing/scheduling.',
            'historical_rootcause':'UNRESOLVED','natural_probe_rejections':[],'probe_operands':[],
            'target':target.container,'volume':target.volume,'all_data':'SYNTHETIC; no licensed/private source import'}
        original = None
        original_fp = None
        def save():
            lease.assert_owned()
            destination.checkpoint(report)
        save()
        try:
            target.start()
            target.checked("CREATE SCHEMA IF NOT EXISTS dpt_ops;"
                "CREATE TABLE dpt_ops.schema_migrations(name text PRIMARY KEY,sha256 text NOT NULL,"
                "applied_at timestamptz NOT NULL DEFAULT now());")
            migrations = []
            for path in sorted((local.ROOT/'database/migrations').glob('*.sql')):
                text = path.read_text(encoding='utf-8')
                # Pin against merged main before executing any SQL; never mutate originals.
                merged = subprocess.check_output(['git','show','origin/main:'+path.relative_to(local.ROOT).as_posix()],
                    cwd=local.ROOT,timeout=5).decode('utf-8')
                if text != merged:
                    raise ValueError('Original migration differs from merged main')
                target.checked('BEGIN;'+text+f"\nINSERT INTO dpt_ops.schema_migrations(name,sha256) VALUES('{path.name}','{digest(text)}');COMMIT;")
                migrations.append({'name':path.name,'sha256':digest(text)})
            report['migrations'] = migrations
            target.checked(fixture())
            original = target.checked("SELECT pg_get_functiondef('dpt_guard.selection_guard()'::regprocedure);")
            diagnostic = instrument(original)
            original_fp = recovery.fingerprint(target.checked)
            report['original_controls'] = controls(target,'original')
            target.checked(diagnostic)
            report['instrumented_controls'] = controls(target,'instrumented')
            if [(x['name'],x['expected_sqlstate'],x['message']) for x in report['original_controls']] != [
                (x['name'],x['expected_sqlstate'],x['message']) for x in report['instrumented_controls']]:
                raise RuntimeError('Original/instrumented control decisions differ')
            baseline = recovery.fingerprint(target.checked)
            for _ in range(trials):
                r = target.sql('BEGIN;'+selection('statement_timestamp()')+'COMMIT;')
                rows = operands(r.stderr)
                if len(rows)!=1:
                    raise RuntimeError('Expected exactly one actual operand pair per probe')
                row = rows[0]
                if r.returncode:
                    if ('23514' not in r.stderr or 'Future review timestamp' not in r.stderr
                        or not row['review_equals_statement'] or row['delta_microseconds']<=0):
                        raise RuntimeError('Unclassified probe failure; no retry')
                    report['natural_probe_rejections'].append(row)
                    break
                if row['delta_microseconds']>0 or not row['review_equals_statement']:
                    raise RuntimeError('Probe outcome/operands disagree')
                report['probe_operands'].append(row)
            if recovery.fingerprint(target.checked) != baseline:
                raise RuntimeError('Probe changed data/security/roles')
            if digest(Path(__file__).read_text(encoding='utf-8')) != code_hash:
                raise RuntimeError('Capture source changed during run')
            report['status']='CAPTURE_SELFTEST_VERIFIED'
            report['natural_failure_observed']=bool(report['natural_probe_rejections'])
            save()
        except Exception as exc:
            report['status']='FAILED_STOPPED'
            report['failure']=str(exc)
            raise
        finally:
            target.cleaning = True
            target.cleanup_deadline = time.monotonic()+45
            try:
                if original is not None:
                    target.checked(original)
                    if target.checked("SELECT pg_get_functiondef('dpt_guard.selection_guard()'::regprocedure);") != original:
                        raise RuntimeError('Original guard restore mismatch')
                    if recovery.fingerprint(target.checked) != original_fp:
                        raise RuntimeError('Restored data/security/roles differ')
                    report['original_function_data_security_roles_restored']=True
            except Exception as cleanup:
                report['cleanup_failure']=str(cleanup)
                report['status']='FAILED_CLEANUP_REQUIRES_INSPECTION'
            finally:
                try:
                    # Stop even if restore proof fails; refuse a target whose ownership changed.
                    target.attest()
                    target.command('stop','--time','3',target.container)
                    report['owned_target_stopped_volume_retained']=True
                except Exception as stop:
                    report['stop_failure']=str(stop)
                    report['status']='FAILED_CLEANUP_REQUIRES_INSPECTION'
            save()
        return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',required=True)
    parser.add_argument('--trials',type=int,default=8)
    args=parser.parse_args()
    result=run(args.report,args.trials)
    print(json.dumps({k:result.get(k) for k in ['status','natural_failure_observed',
        'original_function_data_security_roles_restored','owned_target_stopped_volume_retained']}))
    return 0 if result['status']=='CAPTURE_SELFTEST_VERIFIED' else 1


if __name__=='__main__':
    raise SystemExit(main())
