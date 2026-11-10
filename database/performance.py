"""Bounded synthetic-only deferred-validation measurements; never a dataset importer."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import sys
import time

import local
sys.path.insert(0,str(Path(__file__).parent/'tests'))
from fixtures import baseline, uid, q

DB='dpt_migration_probe'
TRACKED=['validate_all_deferred','validate_model','validate_images','serialize_write','check_active_row']


def prepare(phase):
    local.recreate(DB)
    if phase=='before':
        local.sql('CREATE SCHEMA dpt_ops;',db=DB)
        # The published baseline SQL remains immutable; additive008 is intentionally excluded.
        for file in sorted((local.ROOT/'database/migrations').glob('00[1-7]_*.sql')):
            local.sql('BEGIN;\n'+file.read_text(encoding='utf-8')+'\nCOMMIT;',db=DB)
    else:
        local.migrate(DB)
    local.sql(baseline(),db=DB)


def workload(count):
    ids=[uid('SYNTHETIC-PERF-'+str(i)) for i in range(count)]
    entities=','.join('('+q(i)+','+q(uid('public'))+",'brand')" for i in ids)
    brands=','.join('('+q(i)+','+q(uid('public'))+",'SYNTHETIC performance brand',"+q('synthetic-perf-'+str(n))+')' for n,i in enumerate(ids))
    return 'INSERT INTO dpt.entities(id,access_scope_id,kind) VALUES '+entities+';\nINSERT INTO dpt.brands(id,access_scope_id,name,slug) VALUES '+brands+';\n'


def measure(count,operation='insert'):
    if operation!='insert':
        local.sql('BEGIN;'+workload(count)+'COMMIT;',db=DB)
    body=workload(count) if operation=='insert' else "UPDATE dpt.brands SET name='SYNTHETIC measured update' WHERE slug LIKE 'synthetic-perf-%';" if operation=='update' else "DELETE FROM dpt.brands WHERE slug LIKE 'synthetic-perf-%';DELETE FROM dpt.entities WHERE id IN ("+','.join(q(uid('SYNTHETIC-PERF-'+str(i))) for i in range(count))+');'
    sql="""BEGIN;
SET LOCAL statement_timeout='45s';
SET LOCAL lock_timeout='5s';
SET LOCAL track_functions='pl';
SELECT clock_timestamp() AS started \gset
"""+body+"""
COMMIT;
SELECT clock_timestamp() AS finished \gset
SELECT pg_stat_force_next_flush();
SELECT jsonb_build_object('backend_seconds',extract(epoch FROM :'finished'::timestamptz-:'started'::timestamptz),
 'calls',(SELECT jsonb_object_agg(funcname,calls) FROM pg_stat_user_functions WHERE schemaname='dpt_guard'
 AND funcname IN ('validate_all_deferred','validate_model','validate_images','serialize_write','check_active_row')));
"""
    started=time.perf_counter();r=local.sql(sql,db=DB,check=False);elapsed=time.perf_counter()-started
    if r.returncode:
        return {'operation':operation,'records':count,'domain_row_events':count if operation=='update' else count*2,'status':'FAILED_OR_BOUNDED_TIMEOUT','wall_seconds':round(elapsed,6),'error':r.stderr.strip()}
    lines=[line for line in r.stdout.splitlines() if line.strip().startswith('{')]
    result=json.loads(lines[-1]);result.update(operation=operation,records=count,domain_row_events=count if operation=='update' else count*2,status='COMMITTED',wall_seconds=round(elapsed,6))
    # A second backend independently confirms flushed committed function statistics.
    stats=local.sql("SELECT jsonb_object_agg(funcname,calls) FROM pg_stat_user_functions WHERE schemaname='dpt_guard' AND funcname IN ("+','.join(q(x) for x in TRACKED)+");",db=DB).stdout.strip()
    result['calls']=json.loads(stats)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--phase',choices=['before','after'],required=True)
    parser.add_argument('--sizes',nargs='+',type=int,default=[25,100,250]);args=parser.parse_args()
    if any(n<1 or n>250 for n in args.sizes):raise ValueError('Synthetic bound is1..250')
    results=[]
    cases=[('insert',n) for n in args.sizes]+[('update',100),('delete',100)]
    for operation,count in cases:
        prepare(args.phase);row=measure(count,operation);results.append(row);print(json.dumps(row),flush=True)
        if row['status']!='COMMITTED':break  # Do not hide failure or disable constraints to continue.
    report={'task':'IMP-P1-01 performance correction','phase':args.phase,'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'fixture':'SYNTHETIC draft brand+typed entity, no source/product dataset;2 domain rows per record',
      'database':DB,'image':local.IMAGE,'limits':{'records_max':250,'statement_timeout_seconds':45,'container_cpu':2,'memory_mib':768},
      'measurement':'backend wall time around DML+natural COMMIT; session-local track_functions=pl; committed stats force-flushed and read from second backend',
      'results':results,'original_migration_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((local.ROOT/'database/migrations').glob('00[1-7]_*.sql'))},
      'limitations':['One local run per size, not production capacity or full-dataset benchmark','Function tracking and loopback/local client overhead present','Setup/recreate/baseline excluded from backend_seconds; wall_seconds includes harness/connection overhead','No concurrent benchmark load; concurrency correctness separately tested']}
    output=local.ROOT/'database/evidence'/('performance_'+args.phase+'.json');output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    return 0 if all(r['status']=='COMMITTED' for r in results) else 1


if __name__=='__main__':sys.exit(main())
