"""Local-only independent PostgreSQL restore and owned synthetic object rehearsal.

Reads dpt_scento_pilot; writes only an isolated no-network task container and ignored
.local artifacts. No provider, remote database, password export or image acquisition.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import secrets
import shutil
import subprocess
import time
import unicodedata

import local
import etl_benchmark as benchmark

TARGET = 'doomparfum-p1-04-restore'
VOLUME = 'doomparfum-p1-04-restore-data'
LABEL = 'com.doomparfum.task=IMP-P1-04'
DATABASE = 'dpt_restore_test'
APP_ROLES = ('dpt_owner','dpt_runtime','dpt_writer','dpt_curator','dpt_anonymous')
MAX_DUMP_BYTES = 50 * 1024**2
ROLE_FLAGS = ('rolsuper','rolcreatedb','rolcreaterole','rolreplication','rolbypassrls','rolcanlogin')
# Exact PostgreSQL16.15 definitions: approved source inventory and its pg_dump
# reparse. Unknown text is never certified by a finite sample of predicates.
KNOWN_RIGHTS_CHECK_HASHES = frozenset({
    'ca15a4e47a119bdcc92b080a2714b0983f85eb412bc8eccb18cdbf65d4b06e59',
    'f8cd8c84c22a1dd48700e986b4e5102d21af8a1bee893afca964c704217f128b',
})


def private_path(value):
    path = benchmark.report_path(value)
    # Refuse all Windows reparse points, including types other than junctions.
    for item in (Path(value).absolute(), *Path(value).absolute().parents):
        if item.exists() and getattr(item.stat(), 'st_file_attributes', 0) & 0x400:
            raise ValueError('Reparse recovery paths are refused')
    return path


def persist_private(path, content):
    path = private_path(path)
    with path.open('xb') as stream:
        stream.write(content); stream.flush(); os.fsync(stream.fileno())


def stored_archive(path, metadata):
    path = private_path(path)
    size, digest = metadata.get('bytes'), metadata.get('sha256')
    if type(size) is not int or not 5 <= size <= MAX_DUMP_BYTES or not isinstance(digest, str) or not re.fullmatch('[0-9a-f]{64}', digest):
        raise ValueError('Stored dump metadata rejected')
    if not path.is_file() or path.stat().st_size != size:
        raise ValueError('Stored dump missing or size differs')
    with path.open('rb') as stream: content = stream.read(size+1)
    if len(content) != size or not content.startswith(b'PGDMP') or hashlib.sha256(content).hexdigest() != digest:
        raise ValueError('Stored dump format/hash differs')
    return content


def application_roles(sql):
    """Only the five application groups; never query/export passwords or test logins."""
    names = ','.join("'"+x+"'" for x in APP_ROLES)
    return json.loads(sql("""SELECT jsonb_build_object('roles',
      (SELECT coalesce(jsonb_agg(jsonb_build_object('name',rolname,'rolsuper',rolsuper,
        'rolcreatedb',rolcreatedb,'rolcreaterole',rolcreaterole,'rolreplication',rolreplication,
        'rolbypassrls',rolbypassrls,'rolcanlogin',rolcanlogin,'rolinherit',rolinherit,
        'rolconnlimit',rolconnlimit,'rolvaliduntil',rolvaliduntil::text,
        'rolconfig',coalesce(to_jsonb(rolconfig),'[]'::jsonb)) ORDER BY rolname),'[]'::jsonb)
       FROM pg_roles WHERE rolname IN ("""+names+""")), 'memberships',
      (SELECT coalesce(jsonb_agg(jsonb_build_object('role',r.rolname,'member',u.rolname,
        'grantor',pg_get_userbyid(m.grantor),'admin_option',m.admin_option,
        'inherit_option',m.inherit_option,'set_option',m.set_option)
        ORDER BY r.rolname,u.rolname,pg_get_userbyid(m.grantor)),'[]'::jsonb)
       FROM pg_auth_members m JOIN pg_roles r ON r.oid=m.roleid JOIN pg_roles u ON u.oid=m.member
       WHERE r.rolname IN ("""+names+") AND u.rolname IN ("+names+")));"))


def validate_role_manifest(manifest, *, complete=True):
    if not isinstance(manifest, dict) or set(manifest) != {'roles','memberships'} or not all(isinstance(manifest[k], list) for k in manifest):
        raise ValueError('Application role manifest shape rejected')
    names = set()
    expected_fields = {'name', *ROLE_FLAGS, 'rolinherit','rolconnlimit','rolvaliduntil','rolconfig'}
    for row in manifest['roles']:
        if not isinstance(row, dict) or set(row) != expected_fields or row['name'] not in APP_ROLES or row['name'] in names:
            raise ValueError('Unexpected/duplicate application role')
        names.add(row['name'])
        if any(row[k] is not False for k in ROLE_FLAGS) or type(row['rolinherit']) is not bool or row['rolconnlimit'] != -1 or row['rolvaliduntil'] is not None or row['rolconfig'] != []:
            raise ValueError('Unsafe or configured application role: '+row['name'])
    if complete and names != set(APP_ROLES): raise ValueError('Application roles are incomplete')
    edges = set()
    fields = {'role','member','grantor','admin_option','inherit_option','set_option'}
    for edge in manifest['memberships']:
        if not isinstance(edge, dict) or set(edge) != fields or edge['role'] not in names or edge['member'] not in names or edge['role'] == edge['member']:
            raise ValueError('Application membership rejected')
        key = edge['role'], edge['member'], edge['grantor']
        if key in edges or edge['grantor'] != 'postgres' or edge['admin_option'] is not False or any(type(edge[k]) is not bool for k in ('inherit_option','set_option')):
            raise ValueError('Unsafe or duplicate application membership')
        edges.add(key)
    if manifest['roles'] != sorted(manifest['roles'], key=lambda x:x['name']) or manifest['memberships'] != sorted(manifest['memberships'], key=lambda x:(x['role'],x['member'],x['grantor'])):
        raise ValueError('Role manifest must use stable name ordering')


def compatible_existing_roles(existing, expected):
    validate_role_manifest(expected); validate_role_manifest(existing, complete=False)
    names = {r['name'] for r in existing['roles']}
    if existing['roles'] != [r for r in expected['roles'] if r['name'] in names] or existing['memberships'] != [e for e in expected['memberships'] if e['role'] in names and e['member'] in names]:
        raise ValueError('Existing target application roles differ from source manifest')


def role_creation_sql(manifest):
    validate_role_manifest(manifest)
    statements = ['BEGIN;']
    for row in manifest['roles']:
        statements.append('CREATE ROLE "'+row['name']+'" NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS '+('INHERIT' if row['rolinherit'] else 'NOINHERIT')+' CONNECTION LIMIT -1;')
    for edge in manifest['memberships']:
        for option, value in [('ADMIN',False),('INHERIT',edge['inherit_option']),('SET',edge['set_option'])]:
            statements.append('GRANT "'+edge['role']+'" TO "'+edge['member']+'" WITH '+option+' '+str(value).upper()+' GRANTED BY postgres;')
    return ''.join([*statements, 'COMMIT;'])


def normalized_acl(expression, kind, owner):
    type_sql = "CASE WHEN c.relkind='S' THEN 's'::\"char\" ELSE 'r'::\"char\" END" if kind == 'relation' else "'"+str(kind)+"'::\"char\""
    default = "'{}'::aclitem[]" if kind is None else "acldefault("+type_sql+","+owner+")"
    if kind == 'relation':
        default = "CASE WHEN c.relkind IN ('i','I') THEN '{}'::aclitem[] ELSE "+default+" END"
    acl = "coalesce("+expression+","+default+")"
    # PostgreSQL rejects a zero-dimensional empty ACL in aclexplode. Empty explicit
    # grants stay empty; NULL relation/schema ACLs still use their proper defaults.
    return "(CASE WHEN cardinality("+acl+")=0 THEN '[]'::jsonb ELSE (SELECT coalesce(jsonb_agg(jsonb_build_array(pg_get_userbyid(a.grantor),CASE WHEN a.grantee=0 THEN 'PUBLIC' ELSE pg_get_userbyid(a.grantee) END,a.privilege_type,a.is_grantable) ORDER BY pg_get_userbyid(a.grantor),CASE WHEN a.grantee=0 THEN 'PUBLIC' ELSE pg_get_userbyid(a.grantee) END,a.privilege_type,a.is_grantable),'[]'::jsonb) FROM aclexplode("+acl+") a) END)"


def command(*args, input=None, check=True, timeout=120):
    local.assert_local_endpoint()
    result=subprocess.run(['docker','--context','desktop-linux',*args],input=input,
                          capture_output=True,timeout=timeout)
    if check and result.returncode:
        raise RuntimeError('Local recovery command failed; preserve private stderr for diagnosis')
    return result


def guard_target():
    info=json.loads(command('inspect',TARGET).stdout)[0]
    config=info['HostConfig']
    if (info['Config'].get('Labels',{}).get('com.doomparfum.task')!='IMP-P1-04'
        or info['Config']['Image']!=local.IMAGE or config['NetworkMode']!='none'
        or config.get('PortBindings') or config['Memory']!=512*1024**2 or config['NanoCpus']!=1_000_000_000
        or not any(m.get('Type')=='volume' and m.get('Name')==VOLUME and
                   m.get('Destination')=='/var/lib/postgresql/data' for m in info['Mounts'])):
        raise RuntimeError('Independent restore target differs from pinned isolated task identity')
    volume=json.loads(command('volume','inspect',VOLUME).stdout)[0]
    if volume.get('Labels',{}).get('com.doomparfum.task')!='IMP-P1-04':
        raise RuntimeError('Independent restore volume is unrelated')


def start_target():
    state=private_path(local.ROOT/'.local/p1-04')
    password=private_path(state/'restore-password')
    exists=command('inspect',TARGET,check=False)
    if exists.returncode==0:
        guard_target();command('start',TARGET)
    else:
        state.mkdir(parents=True,exist_ok=True)
        private_path(state);private_path(password)
        if not password.exists():
            persist_private(password,secrets.token_urlsafe(40).encode('ascii'))
        elif not password.is_file() or not 40 <= password.stat().st_size <= 256:
            raise ValueError('Existing private restore password file has unexpected shape')
        volume=command('volume','inspect',VOLUME,check=False)
        if volume.returncode:
            command('volume','create','--label',LABEL,VOLUME)
        elif json.loads(volume.stdout)[0].get('Labels',{}).get('com.doomparfum.task')!='IMP-P1-04':
            raise RuntimeError('Refusing unrelated volume')
        command('run','-d','--pull=never','--name',TARGET,'--label',LABEL,'--network','none',
                '--memory','512m','--cpus','1','--mount',f'type=volume,source={VOLUME},target=/var/lib/postgresql/data',
                '--mount',f'type=bind,source={password.resolve()},target=/run/secrets/postgres-password,readonly',
                '-e','POSTGRES_PASSWORD_FILE=/run/secrets/postgres-password',local.IMAGE)
        guard_target()
    for _ in range(60):
        if command('exec',TARGET,'pg_isready','-U','postgres',check=False).returncode==0:return
        time.sleep(0.25)
    raise RuntimeError('Independent restore PostgreSQL not ready')


def target_sql(sql, *, db=DATABASE, user='postgres', check=True):
    if db not in {DATABASE,'postgres'} or user not in {'postgres','dpt_restore_outsider'}:
        raise ValueError('Restore target/user outside task allowlist')
    guard_target()
    return command('exec','-i','--user','postgres',TARGET,'psql','-X','-qAt','-v','ON_ERROR_STOP=1','-v','VERBOSITY=verbose',
                   '-U',user,'-d',db,input=sql.encode('utf-8'),check=check)


def fresh_target():
    # No FORCE: an unexpected connection fails closed rather than being terminated.
    target_sql('DROP DATABASE IF EXISTS '+DATABASE+';',db='postgres')
    target_sql('CREATE DATABASE '+DATABASE+';',db='postgres')


def fingerprint(sql):
    names=json.loads(sql("SELECT jsonb_agg(n.nspname||'.'||c.relname ORDER BY n.nspname,c.relname) "
        "FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE c.relkind='r' "
        "AND n.nspname IN ('dpt','dpt_ops');"))
    values=[]
    for name in names:
        if not re.fullmatch(r'[a-z_]+\.[a-z_]+',name):raise ValueError('Unexpected relation identifier')
        schema,table=name.split('.')
        values.append("SELECT '"+name+"' AS relation,count(*) AS rows,encode(sha256(convert_to(coalesce("
                      "string_agg(to_jsonb(t)::text,E'\\n' ORDER BY to_jsonb(t)::text),''),'UTF8')),'hex') AS sha256 "
                      'FROM "'+schema+'"."'+table+'" t')
    rows=json.loads(sql('BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY;SELECT jsonb_agg(v ORDER BY relation) FROM ('+
                       ' UNION ALL '.join(values)+')v;COMMIT;'))
    security=json.loads(sql("""SELECT jsonb_build_object(
      'schemas',(SELECT jsonb_agg(jsonb_build_object('name',n.nspname,'owner',pg_get_userbyid(n.nspowner),
        'acl',"""+normalized_acl('n.nspacl','n','n.nspowner')+""") ORDER BY n.nspname) FROM pg_namespace n
        WHERE n.nspname IN ('dpt','dpt_guard','dpt_ops','dpt_public')),
      'relations',(SELECT jsonb_agg(jsonb_build_object('schema',n.nspname,'name',c.relname,'kind',c.relkind,
        'owner',pg_get_userbyid(c.relowner),'acl',"""+normalized_acl('c.relacl','relation','c.relowner')+""") ORDER BY n.nspname,c.relname,c.relkind)
        FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
        WHERE n.nspname IN ('dpt','dpt_guard','dpt_ops','dpt_public') AND c.relkind IN ('r','p','v','m','S','f','i','I')),
      'column_acls',(SELECT coalesce(jsonb_agg(jsonb_build_object('schema',n.nspname,'table',c.relname,'column',x.attname,
        'acl',"""+normalized_acl('x.attacl',None,None)+""") ORDER BY n.nspname,c.relname,x.attname),'[]'::jsonb)
        FROM pg_attribute x JOIN pg_class c ON c.oid=x.attrelid JOIN pg_namespace n ON n.oid=c.relnamespace
        WHERE n.nspname IN ('dpt','dpt_guard','dpt_ops','dpt_public') AND x.attnum>0 AND NOT x.attisdropped AND x.attacl IS NOT NULL),
      'rls_tables',(SELECT jsonb_agg(jsonb_build_array(c.relname,c.relrowsecurity,c.relforcerowsecurity,
        pg_get_userbyid(c.relowner)) ORDER BY c.relname) FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
        WHERE n.nspname='dpt' AND c.relkind='r'),
      'policies',(SELECT jsonb_agg(jsonb_build_object('table',tablename,'name',policyname,'roles',roles,
        'command',cmd,'permissive',permissive,'qual',qual,'check',with_check) ORDER BY tablename,policyname)
        FROM pg_policies WHERE schemaname='dpt'),
      'constraints',(SELECT jsonb_agg(jsonb_build_array(r.relname,c.conname,c.contype,c.convalidated,
        pg_get_constraintdef(c.oid)) ORDER BY r.relname,c.conname) FROM pg_constraint c
        JOIN pg_class r ON r.oid=c.conrelid JOIN pg_namespace n ON n.oid=r.relnamespace WHERE n.nspname='dpt'),
      'triggers',(SELECT jsonb_agg(pg_get_triggerdef(t.oid) ORDER BY c.relname,t.tgname) FROM pg_trigger t
        JOIN pg_class c ON c.oid=t.tgrelid JOIN pg_namespace n ON n.oid=c.relnamespace
        WHERE n.nspname IN ('dpt','dpt_ops') AND NOT t.tgisinternal),
      'functions',(SELECT jsonb_agg(jsonb_build_array(n.nspname,p.proname,pg_get_functiondef(p.oid),
        pg_get_userbyid(p.proowner),"""+normalized_acl('p.proacl','f','p.proowner')+""")
        ORDER BY n.nspname,p.proname,p.oid::regprocedure::text) FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace
        WHERE n.nspname IN ('dpt_guard','dpt_public')));"""))
    return {'tables':rows,'security':security,'application_roles':application_roles(sql)}


def validate_objects(root, manifest):
    root=Path(root).absolute()
    if not isinstance(manifest,list) or len(manifest)>100:raise ValueError('Object manifest rejected')
    seen=set()
    for item in manifest:
        if not isinstance(item,dict):raise ValueError('Object metadata rejected')
        path=item.get('path');size=item.get('bytes');sha=item.get('sha256')
        if not isinstance(path,str) or '\\' in path or ':' in path or not path or path.startswith('/'):
            raise ValueError('Object path rejected')
        parts=PurePosixPath(path).parts
        if any(x in {'','.','..'} for x in path.split('/')) or not parts:raise ValueError('Object path rejected')
        normalized=unicodedata.normalize('NFC',path).casefold()
        if normalized in seen:raise ValueError('Duplicate object path rejected')
        seen.add(normalized)
        if type(size) is not int or not 0<=size<=16*1024**2 or not isinstance(sha,str) or not re.fullmatch('[0-9a-f]{64}',sha):
            raise ValueError('Object size/hash rejected')
        file=root.joinpath(*parts)
        if not file.resolve().is_relative_to(root.resolve()):raise ValueError('Object path rejected')
        for parent in [file,*file.parents]:
            if parent.exists() and (parent.is_symlink() or getattr(parent.stat(),'st_file_attributes',0)&0x400):
                raise ValueError('Linked object paths rejected')
            if parent==root:break
        if not file.is_file() or file.stat().st_size!=size:raise ValueError('Object missing or size mismatch')
        with file.open('rb') as stream:content=stream.read(size+1)
        if len(content)!=size or hashlib.sha256(content).hexdigest()!=sha:raise ValueError('Object hash mismatch')
    return {'objects':len(manifest),'bytes':sum(x['bytes'] for x in manifest),'hashes_verified':True}


def security_equivalence(source, restored, sql):
    """Require exact contracts, with one exhaustively tested CHECK deparse exception.

    pg_dump/reparse can flatten associative OR nodes in rights_assessments_k4.
    No other text difference is waived. Both expressions must match the independent
    rights rule across every use-state combination and evidence-URL truth class.
    """
    if source==restored:return {'equal':True,'method':'exact_manifest'}
    if set(source)!=set(restored) or any(source[k]!=restored[k] for k in source if k!='constraints'):
        return {'equal':False,'reason':'Non-constraint security manifest differs'}
    left,right=source['constraints'],restored['constraints']
    if len(left)!=len(right):return {'equal':False,'reason':'Constraint inventory differs'}
    differences=[(a,b) for a,b in zip(left,right) if a!=b]
    expected_key=['rights_assessments','rights_assessments_k4','c',True]
    if len(differences)!=1 or differences[0][0][:4]!=expected_key or differences[0][1][:4]!=expected_key:
        return {'equal':False,'reason':'Unrecognized constraint difference'}
    definitions=[row[4] for row in differences[0]]
    if any(not text.startswith('CHECK (') or ';' in text or '--' in text or '/*' in text for text in definitions):
        return {'equal':False,'reason':'Unexpected check expression'}
    if {hashlib.sha256(text.encode('utf-8')).hexdigest() for text in definitions}!=KNOWN_RIGHTS_CHECK_HASHES:
        return {'equal':False,'reason':'Unreviewed rights CHECK text; exact known definitions required'}
    fields=['research_use','automation_use','cache_use','storage_use','display_use','redistribution_use','ai_use']
    aliases=[chr(ord('a')+i) for i in range(7)]
    selected=','.join(alias+'.v AS '+field for alias,field in zip(aliases,fields))
    relations=' CROSS JOIN '.join('uses '+alias for alias in aliases)
    independent="(NOT ("+' OR '.join(field+"='allowed'" for field in fields)+") OR (evidence_url IS NOT NULL AND btrim(evidence_url)<>''))"
    query="WITH uses(v) AS (VALUES('allowed'::text),('restricted'),('unknown')),urls(v) AS (VALUES(NULL::text),(''),('  '),('https://evidence.invalid/SYNTHETIC')),"\
          "cases AS (SELECT "+selected+",u.v AS evidence_url FROM "+relations+" CROSS JOIN urls u) "\
          "SELECT jsonb_build_object('cases',count(*),'source_equivalent',bool_and(("+definitions[0][6:]+") IS NOT DISTINCT FROM "+independent+"),"\
          "'restored_equivalent',bool_and(("+definitions[1][6:]+") IS NOT DISTINCT FROM "+independent+")) FROM cases;"
    proof=json.loads(sql(query))
    passed=proof=={'cases':8748,'source_equivalent':True,'restored_equivalent':True}
    return {'equal':passed,'method':'Only known rights CHECK;8748 exhaustive domain/evidence cases versus independent rule',
            'proof':proof,'other_security_fields_exact':True}


def object_rehearsal(directory):
    source=directory/'owned-synthetic-source';dest=directory/'independent-synthetic-restore'
    source.mkdir();dest.mkdir()
    payloads={'SYNTHETIC-object-a.bin':b'SYNTHETIC owned test bytes; not an image or perfume fact.\n'*100,
              'SYNTHETIC-object-b.bin':bytes(range(256))*16}
    manifest=[]
    for name,data in payloads.items():
        (source/name).write_bytes(data)
        manifest.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                         'rights':'Agent-authored SYNTHETIC fixture only; no third-party grant',
                         'access_scope':'SYNTHETIC-private','asset_lineage':'No real DB image asset or permission binding'})
    validate_objects(source,manifest)
    for item in manifest:shutil.copyfile(source/item['path'],dest/item['path'])
    positive=validate_objects(dest,manifest);negative={}
    first=dest/manifest[0]['path'];saved=first.read_bytes();first.unlink()
    try:validate_objects(dest,manifest)
    except ValueError:negative['missing_object_detected']=True
    first.write_bytes(b'X'+saved[1:])
    try:validate_objects(dest,manifest)
    except ValueError:negative['same_size_corruption_detected']=True
    first.write_bytes(saved);validate_objects(dest,manifest)
    if not all(negative.get(k) for k in ['missing_object_detected','same_size_corruption_detected']):
        raise RuntimeError('Object negative controls failed')
    (directory/'synthetic_object_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    return {'fixture':'Owned SYNTHETIC objects only, independent local folders on same host',
            'positive':positive,'negative':negative,'real_image_assets':0,
            'limits':['No actual image/DB permission-lineage recovery','No offsite failure domain/encryption/retention/RPO guarantee']}


def missing_role_control(expected, restore, directory):
    """Repeatable real pg_restore failure, confined to the guarded empty target."""
    guard_target()
    roles = lambda sql:target_sql(sql,db='postgres').stdout.decode('utf-8').strip()
    compatible_existing_roles(application_roles(roles), expected)
    fresh_target()
    # No DROP OWNED, CASCADE, arbitrary role names or source-cluster role writes.
    target_sql('BEGIN;'+''.join('DROP ROLE IF EXISTS "'+name+'";' for name in APP_ROLES)+'COMMIT;',db='postgres')
    if application_roles(roles) != {'roles': [], 'memberships': []}:
        raise RuntimeError('Target application roles remain before missing-role control')
    missing = restore()
    persist_private(directory/'missing_role.stderr', missing.stderr)
    cause = re.search(r'role "('+'|'.join(APP_ROLES)+r')" does not exist',missing.stderr.decode('utf-8',errors='replace'))
    if missing.returncode == 0 or cause is None:
        raise RuntimeError('Missing-role restore did not fail for an allowlisted absent role')
    fresh_target()
    target_sql(role_creation_sql(expected),db='postgres')
    actual = application_roles(roles)
    validate_role_manifest(actual)
    if actual != expected: raise RuntimeError('Recreated target roles differ from source manifest')
    return True


def nonowner_controls(target):
    target("DO $$BEGIN IF NOT EXISTS(SELECT FROM pg_roles WHERE rolname='dpt_restore_outsider') THEN CREATE ROLE dpt_restore_outsider LOGIN NOSUPERUSER NOBYPASSRLS NOCREATEDB NOCREATEROLE NOREPLICATION INHERIT;END IF;END$$;")
    unsafe = json.loads(target("SELECT jsonb_build_object('count',count(*),'unsafe',count(*) FILTER(WHERE rolsuper OR rolbypassrls OR rolcreatedb OR rolcreaterole OR rolreplication OR NOT rolcanlogin OR NOT rolinherit OR rolconfig IS NOT NULL OR rolvaliduntil IS NOT NULL OR rolconnlimit<>-1)) FROM pg_roles WHERE rolname='dpt_restore_outsider';"))
    if unsafe != {'count': 1, 'unsafe': 0}: raise RuntimeError('Synthetic outsider role is unsafe')
    target('GRANT dpt_runtime TO dpt_restore_outsider;')
    hidden=target_sql('SELECT count(*) FROM dpt.perfumes;',user='dpt_restore_outsider')
    count_sql="SELECT count(*) FROM dpt.users WHERE auth_subject='SYNTHETIC denied restore outsider';"
    before=target(count_sql)
    denied=target_sql("BEGIN;INSERT INTO dpt.users(auth_subject) VALUES('SYNTHETIC denied restore outsider');ROLLBACK;",user='dpt_restore_outsider',check=False)
    return {'nonowner_private_perfumes_hidden':hidden.stdout.strip()==b'0',
            'nonowner_mutation_denied':denied.returncode!=0 and bool(re.search(rb'ERROR:\s+42501:',denied.stderr)),
            'nonowner_probe_preserved_rows':target(count_sql)==before}


def run(output_dir):
    source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    directory=private_path(output_dir)
    if directory.exists():raise ValueError('Use a new ignored .local recovery directory')
    with benchmark.RunLease(benchmark.common_repository_root()) as lease:
        directory.mkdir(parents=True,exist_ok=False);private_path(directory)
        destination=benchmark.ReportFile(directory/'recovery_report.json',lease.nonce,source_hash)
        return run_owned(directory,destination,lease,source_hash)


def run_owned(directory,destination,lease,source_hash):
    report={'task':'IMP-P1-04','started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_database':'dpt_scento_pilot','target_container':TARGET,'target_database':DATABASE,
            'image':local.IMAGE,'source_code_sha256':source_hash,
            'benchmark_helper_sha256':hashlib.sha256(Path(benchmark.__file__).read_bytes()).hexdigest(),
            'lease_path':str(lease.path),'owner_nonce':lease.nonce,
            'checks':{},'limits':['Local same-host logical restore, not offsite disaster recovery',
            'Actual image bytes/permission-lineage/provider delivery restore blocked by IMP-P1-03 gate',
            'No accepted retention/RPO/RTO/cloud/production target']}
    started=time.monotonic()
    def save():
        private_path(directory);lease.assert_owned();destination.checkpoint(report)
    try:
        save();local.guard()
        source=lambda sql:local.sql(sql,'dpt_scento_pilot').stdout.strip()
        before=fingerprint(source)
        validate_role_manifest(before['application_roles'])
        report['application_role_manifest']=before['application_roles']
        dump=command('exec','--user','postgres',local.CONTAINER,'pg_dump','-U','postgres',
                     '--format=custom','--serializable-deferrable','--lock-wait-timeout=5s','dpt_scento_pilot')
        if not dump.stdout.startswith(b'PGDMP') or len(dump.stdout)>MAX_DUMP_BYTES:raise RuntimeError('Dump format/size rejected')
        persist_private(directory/'pilot.dump',dump.stdout)
        persist_private(directory/'pg_dump.stderr',dump.stderr)
        report['dump']={'bytes':len(dump.stdout),'sha256':hashlib.sha256(dump.stdout).hexdigest(),
                        'format':'custom','contains_private_data':'LOCAL ONLY; excluded from public Git and handoff ZIP'}
        stored_archive(directory/'pilot.dump',report['dump'])
        report['checks']['stored_archive_readback_verified']=True
        save();lease.assert_owned();start_target()
        def restore(truncated=False):
            lease.assert_owned()
            content=stored_archive(directory/'pilot.dump',report['dump'])
            if truncated:content=content[:100]
            guard_target()
            return command('exec','-i','--user','postgres',TARGET,'pg_restore','-U','postgres','--dbname',DATABASE,
                           '--single-transaction','--exit-on-error',input=content,check=False)
        report['checks']['missing_roles_restore_fails']=missing_role_control(before['application_roles'],restore,directory)
        corrupt=restore(truncated=True);persist_private(directory/'corrupt_dump.stderr',corrupt.stderr)
        report['checks']['truncated_dump_fails']=corrupt.returncode!=0
        fresh_target();result=restore();persist_private(directory/'pg_restore.stderr',result.stderr)
        if result.returncode:raise RuntimeError('Positive restore failed; inspect local-only pg_restore.stderr')
        target=lambda sql:target_sql(sql).stdout.decode('utf-8').strip()
        after=fingerprint(target)
        report['checks']['all_table_counts_and_sha256_equal']=before['tables']==after['tables']
        source_proof=security_equivalence(before['security'],after['security'],source)
        target_proof=security_equivalence(before['security'],after['security'],target)
        report['security_equivalence']={'source_server':source_proof,'target_server':target_proof}
        report['checks']['security_contracts_preserved']=source_proof['equal'] and target_proof['equal']
        report['checks']['application_role_manifest_equal']=before['application_roles']==after['application_roles']
        target('SELECT dpt_guard.validate_model();SELECT dpt_guard.validate_images();')
        report['checks']['original_full_validators_succeeded']=True
        report['tables']=after['tables']
        report['security_inventory']={'rls_tables':len(after['security']['rls_tables']),
            'policies':len(after['security']['policies']),'constraints':len(after['security']['constraints']),
            'triggers':len(after['security']['triggers']),'functions':len(after['security']['functions'])}
        report['checks'].update(nonowner_controls(target))
        # Intentional invalid-restore negative control, isolated transaction and target;
        # do not expose unprotected rows, and immediately roll back the metadata change.
        missing_rls=target_sql("BEGIN;ALTER TABLE dpt.perfumes DISABLE ROW LEVEL SECURITY;"
            "SELECT jsonb_build_array(c.relname,c.relrowsecurity,c.relforcerowsecurity,pg_get_userbyid(c.relowner)) FROM pg_class c WHERE c.oid='dpt.perfumes'::regclass;ROLLBACK;")
        wrong=json.loads(missing_rls.stdout)
        expected=next(row for row in after['security']['rls_tables'] if row[0]=='perfumes')
        report['checks']['missing_rls_control_detected']=wrong!=expected and wrong[1] is False
        final=fingerprint(target)
        report['checks']['negative_rls_change_rolled_back']=final['security']==after['security']
        report['checks']['negative_controls_preserved_data']=final['tables']==after['tables']
        report['checks']['negative_controls_preserved_application_roles']=final['application_roles']==before['application_roles']
        report['checks']['source_unchanged_after_export_restore']=fingerprint(source)==before
        report['synthetic_objects']=object_rehearsal(directory)
        if any(v is not True for v in report['checks'].values()):raise RuntimeError('Restore verification failed or a control was not run')
        report['status']='VERIFIED_LOCAL_DB_AND_SYNTHETIC_OBJECT_SUBSET'
        report['seconds']=round(time.monotonic()-started,6);save();return report
    except Exception as exc:
        report['status']='FAILED_STOPPED';report['failure']=str(exc);save();raise


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir',required=True)
    run(parser.parse_args().output_dir)


if __name__=='__main__':main()
