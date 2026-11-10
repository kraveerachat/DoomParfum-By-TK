"""Run local integration tests and publish sanitized schema/test evidence only."""
import collections
import datetime
import hashlib
import io
import json
from pathlib import Path
import sys
import time
import unittest

import local


def inventory():
    query = """SELECT jsonb_build_object(
      'server_version',current_setting('server_version'),
      'server_encoding',current_setting('server_encoding'),
      'collation',(SELECT datcollate FROM pg_database WHERE datname=current_database()),
      'tables',(SELECT jsonb_agg(tablename ORDER BY tablename) FROM pg_tables WHERE schemaname='dpt'),
      'constraints',(SELECT jsonb_agg(jsonb_build_object('table',r.relname,'name',c.conname,'type',c.contype,
         'validated',c.convalidated,'definition',pg_get_constraintdef(c.oid)) ORDER BY r.relname,c.conname)
        FROM pg_constraint c JOIN pg_class r ON r.oid=c.conrelid JOIN pg_namespace n ON n.oid=r.relnamespace WHERE n.nspname='dpt'),
      'domain_checks',(SELECT count(*) FROM pg_constraint c JOIN pg_type t ON t.oid=c.contypid JOIN pg_namespace n ON n.oid=t.typnamespace WHERE n.nspname='dpt'),
      'not_null_columns',(SELECT count(*) FROM pg_attribute a JOIN pg_class c ON c.oid=a.attrelid JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='dpt' AND c.relkind='r' AND a.attnum>0 AND NOT a.attisdropped AND a.attnotnull),
      'indexes',(SELECT count(*) FROM pg_indexes WHERE schemaname='dpt'),
      'rls_policies',(SELECT count(*) FROM pg_policies WHERE schemaname='dpt'),
      'user_triggers',(SELECT count(*) FROM pg_trigger t JOIN pg_class c ON c.oid=t.tgrelid JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='dpt' AND NOT t.tgisinternal),
      'enabled_force_rls',(SELECT count(*) FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='dpt' AND c.relkind='r' AND c.relrowsecurity AND c.relforcerowsecurity));"""
    result=json.loads(local.sql(query).stdout)
    result['constraint_counts']=dict(collections.Counter(c['type'] for c in result['constraints']))
    result['image']=local.IMAGE
    result['migrations']=[{'name':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in sorted((local.ROOT/'database/migrations').glob('*.sql'))]
    return result


def investigate_duplicates():
    package=local.ROOT.parent/'DoomParfum Local Data/P1/20261110-221751'
    raw=package/'raw/perfumes.jsonl'
    profiles=[json.loads(line) for line in raw.read_text(encoding='utf-8').splitlines()]
    groups=[]
    for line,row in enumerate(profiles,1):
        for layer in ['top_notes','heart_notes','base_notes']:
            for label,count in collections.Counter(row[layer]).items():
                if count>1:
                    ordinals=[i for i,x in enumerate(row[layer]) if x==label]
                    groups.append({'source_id':row['id'],'source_jsonl_line':line,'source_field':layer,'source_label':label,
                                   'ordinals':ordinals,'locators':['/'+layer+'/'+str(i) for i in ordinals],
                                   'disposition':'REVIEW_REQUIRED_DUPLICATE_OCCURRENCE; preserve raw array, never silently dedup'})
    assert len(groups)==40 and len({v['source_id'] for v in groups})==39
    private={'source_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'groups':groups}
    local.STATE.mkdir(parents=True,exist_ok=True)
    (local.STATE/'duplicate-note-investigation.json').write_text(json.dumps(private,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'groups':len(groups),'perfumes':len({v['source_id'] for v in groups}),'by_layer':dict(collections.Counter(v['source_field'] for v in groups)),
            'extra_occurrences':sum(len(v['ordinals'])-1 for v in groups),'source_sha256':private['source_sha256'],
            'detailed_rows':'LOCAL ONLY: .local/p1-01/duplicate-note-investigation.json','canonical_imported':0}


def main():
    started=time.monotonic()
    loader=unittest.TestLoader()
    suite=loader.discover(str(local.ROOT/'database/tests'))
    names=[]
    def collect(test):
        if isinstance(test,unittest.TestSuite):
            for child in test:collect(child)
        else:names.append(test.id())
    collect(suite)
    stream=io.StringIO()
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    local.STATE.mkdir(parents=True,exist_ok=True)
    (local.STATE/'test-output.log').write_text(stream.getvalue(),encoding='utf-8')
    print(stream.getvalue())
    if not result.wasSuccessful():
        print('No passing evidence published; inspect local-only test log.')
        return 1
    inv=inventory()
    report={'task':'IMP-P1-01','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'command':'python database/verify.py','environment':'isolated Docker Desktop PostgreSQL 16.15; real non-owner logins',
            'tests_run':result.testsRun,'passed':result.testsRun-len(result.skipped),'failed':len(result.failures),'errors':len(result.errors),
            'skipped':len(result.skipped),'exit_code':0,'seconds':round(time.monotonic()-started,3),'test_ids':names,
            'source_file_sha256':{f.relative_to(local.ROOT).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((local.ROOT/'database').rglob('*')) if f.is_file() and (f.suffix in {'.py','.sql'} or f.name=='schema_contract.json')},
            'duplicate_investigation':investigate_duplicates(),
            'not_run':['IMP-P1-02 ETL/idempotent real sample import','API/JWT/cache/search/export/error masking',
                       'IMP-P1-03 byte acquisition/decoder/SSRF/object delivery','IMP-P1-04 benchmark and independent DB/object restore',
                       'IMP-P1-05 hosted readiness/provisioning','application build/e2e: no application in scope']}
    output=local.ROOT/'database/evidence';output.mkdir(exist_ok=True)
    for name,value in [('schema_inventory.json',inv),('test_results.json',report)]:
        (output/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':report['passed'],'tables':len(inv['tables']),'constraints':inv['constraint_counts'],'rls_policies':inv['rls_policies'],'exit_code':0}))
    return 0


if __name__=='__main__':
    sys.exit(main())
