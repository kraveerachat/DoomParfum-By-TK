"""Owned synthetic recovery-manifest and isolated-target negative controls."""
import copy
import hashlib
import json
import subprocess
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import recovery

RIGHTS_CHECK_FORMS = (
    "CHECK (((NOT ((((((('allowed'::text = (research_use)::text) OR ('allowed'::text = (automation_use)::text)) OR ('allowed'::text = (cache_use)::text)) OR ('allowed'::text = (storage_use)::text)) OR ('allowed'::text = (display_use)::text)) OR ('allowed'::text = (redistribution_use)::text)) OR ('allowed'::text = (ai_use)::text))) OR ((evidence_url IS NOT NULL) AND (btrim(evidence_url) <> ''::text))))",
    "CHECK (((NOT (('allowed'::text = (research_use)::text) OR ('allowed'::text = (automation_use)::text) OR ('allowed'::text = (cache_use)::text) OR ('allowed'::text = (storage_use)::text) OR ('allowed'::text = (display_use)::text) OR ('allowed'::text = (redistribution_use)::text) OR ('allowed'::text = (ai_use)::text))) OR ((evidence_url IS NOT NULL) AND (btrim(evidence_url) <> ''::text))))",
)


class RecoveryOfflineTests(unittest.TestCase):
    def setUp(self):
        base=recovery.local.ROOT/'.local/recovery-offline';base.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=base)
        self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
        self.data=b'SYNTHETIC agent-owned recovery bytes\n'
        (self.root/'owned.bin').write_bytes(self.data)
        self.manifest=[{'path':'owned.bin','bytes':len(self.data),'sha256':hashlib.sha256(self.data).hexdigest()}]
        self.denials={}
        for owner,name in [(recovery,'command'),(recovery.local,'sql'),(recovery.local,'docker'),
                           (recovery.local,'guard'),(recovery.local,'assert_local_endpoint'),(recovery.subprocess,'run')]:
            item=patch.object(owner,name,side_effect=AssertionError('DENIED live '+name))
            self.denials[name]=item.start();self.addCleanup(item.stop)

    def test_owned_object_exact_roundtrip_and_empty_actual_image_set(self):
        self.assertEqual(recovery.validate_objects(self.root,self.manifest)['objects'],1)
        self.assertEqual(recovery.validate_objects(self.root,[])['objects'],0)

    def test_corrupt_same_size_bytes_and_wrong_size_fail(self):
        (self.root/'owned.bin').write_bytes(b'X'+self.data[1:])
        with self.assertRaisesRegex(ValueError,'hash mismatch'):recovery.validate_objects(self.root,self.manifest)
        (self.root/'owned.bin').write_bytes(self.data+b'x')
        with self.assertRaisesRegex(ValueError,'size mismatch'):recovery.validate_objects(self.root,self.manifest)

    def test_missing_object_fails(self):
        (self.root/'owned.bin').unlink()
        with self.assertRaisesRegex(ValueError,'missing'):recovery.validate_objects(self.root,self.manifest)

    def test_relative_absolute_drive_escape_and_ambiguous_paths_rejected(self):
        for path in ['../owned.bin','/owned.bin','C:/owned.bin','folder\\owned.bin','./owned.bin','x/../owned.bin','x//owned.bin','']:
            with self.subTest(path=path),self.assertRaises(ValueError):
                recovery.validate_objects(self.root,[dict(self.manifest[0],path=path)])

    def test_duplicate_casefolded_paths_rejected(self):
        with self.assertRaisesRegex(ValueError,'Duplicate'):
            recovery.validate_objects(self.root,[*self.manifest,dict(self.manifest[0],path='OWNED.BIN')])

    def test_bad_manifest_type_count_size_and_digest_rejected(self):
        for value in [{},None,'bad',[self.manifest[0]]*101]:
            with self.subTest(value=type(value)),self.assertRaises(ValueError):recovery.validate_objects(self.root,value)
        for change in [{'bytes':True},{'bytes':-1},{'bytes':16*1024**2+1},{'sha256':'X'*64},{'sha256':'a'*63}, {'path':None}]:
            with self.subTest(change=change),self.assertRaises(ValueError):
                recovery.validate_objects(self.root,[dict(self.manifest[0],**change)])

    def test_linked_file_rejected_before_content_read(self):
        original=Path.is_symlink
        def linked(path):return path.name=='owned.bin' or original(path)
        with patch.object(Path,'is_symlink',linked),self.assertRaisesRegex(ValueError,'Linked'):
            recovery.validate_objects(self.root,self.manifest)

    def test_object_rehearsal_checks_independent_copy_and_negatives(self):
        report=recovery.object_rehearsal(self.root)
        self.assertEqual(report['positive']['objects'],2)
        self.assertEqual(report['real_image_assets'],0)
        self.assertTrue(all(report['negative'].values()))

    def test_source_or_arbitrary_database_and_user_rejected_before_docker(self):
        for kwargs in [{'db':'dpt_scento_pilot'},{'db':'production'},{'user':'unapproved'}]:
            with self.subTest(kwargs=kwargs),patch.object(recovery,'command') as command,self.assertRaises(ValueError):
                recovery.target_sql('SELECT 1;',**kwargs)
            command.assert_not_called()

    def test_public_output_or_existing_directory_refused_before_source_access(self):
        for path in [recovery.local.ROOT/'forbidden-public-backup',self.root]:
            with self.subTest(path=path),patch.object(recovery.local,'guard') as guard,self.assertRaises(ValueError):recovery.run(path)
            guard.assert_not_called()

    def target_info(self):
        return {'Config':{'Labels':{'com.doomparfum.task':'IMP-P1-04'},'Image':recovery.local.IMAGE},
                'HostConfig':{'NetworkMode':'none','PortBindings':{},'Memory':512*1024**2,'NanoCpus':1_000_000_000},
                'Mounts':[{'Type':'volume','Name':recovery.VOLUME,'Destination':'/var/lib/postgresql/data'}]}

    def test_exact_isolated_target_resource_identity_accepted(self):
        results=[Mock(stdout=json.dumps([self.target_info()]).encode()),Mock(stdout=b'[{"Labels":{"com.doomparfum.task":"IMP-P1-04"}}]')]
        with patch.object(recovery,'command',side_effect=results):recovery.guard_target()

    def test_wrong_image_label_network_port_volume_or_resources_refused(self):
        for category in ['image','label','network','port','memory','cpu','volume']:
            info=self.target_info()
            if category=='image':info['Config']['Image']='postgres:latest'
            if category=='label':info['Config']['Labels']['com.doomparfum.task']='unrelated'
            if category=='network':info['HostConfig']['NetworkMode']='bridge'
            if category=='port':info['HostConfig']['PortBindings']={'5432/tcp':[{'HostIp':'0.0.0.0','HostPort':'5432'}]}
            if category=='memory':info['HostConfig']['Memory']=0
            if category=='cpu':info['HostConfig']['NanoCpus']=0
            if category=='volume':info['Mounts'][0]['Name']='unrelated'
            with self.subTest(category=category),patch.object(recovery,'command',return_value=Mock(stdout=json.dumps([info]).encode())),self.assertRaises(RuntimeError):
                recovery.guard_target()

    def roles(self):
        return {'roles':[dict(name=name,**{flag:False for flag in recovery.ROLE_FLAGS},
            rolinherit=True,rolconnlimit=-1,rolvaliduntil=None,rolconfig=[])
            for name in sorted(recovery.APP_ROLES)],'memberships':[]}

    def completed(self,stdout=b'',stderr=b'',returncode=0):
        return subprocess.CompletedProcess([],returncode,stdout,stderr)

    def test_role_manifest_excludes_passwords_and_non_application_logins(self):
        expected=self.roles();sql=Mock(return_value=json.dumps(expected))
        self.assertEqual(recovery.application_roles(sql),expected)
        query=sql.call_args.args[0]
        self.assertNotIn('rolpassword',query);self.assertNotIn('pg_authid',query)
        self.assertNotIn('dpt_restore_outsider',query)
        self.assertIn('pg_auth_members',query)
        for role in recovery.APP_ROLES:self.assertIn("'"+role+"'",query)

    def test_unsafe_role_flags_configuration_and_extra_roles_fail_closed(self):
        for field,value in [*[(flag,True) for flag in recovery.ROLE_FLAGS],
                            ('rolconnlimit',10),('rolvaliduntil','2099-01-01'),('rolconfig',['search_path=public'])]:
            row=self.roles();row['roles'][0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):recovery.validate_role_manifest(row)
        for change in ['name','password','missing']:
            row=self.roles()
            if change=='name':row['roles'][0]['name']='dpt_restore_outsider'
            if change=='password':row['roles'][0]['password']='SYNTHETIC forbidden field'
            if change=='missing':row['roles'].pop()
            with self.subTest(change=change),self.assertRaises(ValueError):recovery.validate_role_manifest(row)
        self.denials['command'].assert_not_called()

    def test_membership_options_are_exact_safe_and_recreated_explicitly(self):
        manifest=self.roles()
        manifest['memberships']=[dict(role='dpt_writer',member='dpt_curator',grantor='postgres',
            admin_option=False,inherit_option=True,set_option=False)]
        recovery.validate_role_manifest(manifest)
        sql=recovery.role_creation_sql(manifest)
        self.assertIn('WITH ADMIN FALSE GRANTED BY postgres',sql)
        self.assertIn('WITH INHERIT TRUE GRANTED BY postgres',sql)
        self.assertIn('WITH SET FALSE GRANTED BY postgres',sql)
        self.assertNotIn('IF NOT EXISTS',sql);self.assertNotIn('PASSWORD',sql)
        for field,value in [('admin_option',True),('grantor','unapproved'),('member','other'),('set_option',1)]:
            wrong=copy.deepcopy(manifest);wrong['memberships'][0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError):recovery.validate_role_manifest(wrong)

    def test_existing_role_subset_must_be_safe_and_compatible(self):
        expected=self.roles();existing=copy.deepcopy(expected);existing['roles']=existing['roles'][:2]
        recovery.compatible_existing_roles(existing,expected)
        existing['roles'][0]['rolinherit']=False
        with self.assertRaisesRegex(ValueError,'differ'):recovery.compatible_existing_roles(existing,expected)

    def test_fingerprint_includes_schema_relation_column_and_function_acls_and_roles(self):
        sql=Mock(side_effect=[json.dumps(['dpt.perfumes']),json.dumps([]),json.dumps({}),json.dumps(self.roles())])
        record=recovery.fingerprint(sql)
        security=sql.call_args_list[2].args[0]
        for field in ['nspacl','relacl','attacl','proacl','aclexplode','privilege_type','is_grantable','PUBLIC']:
            self.assertIn(field,security)
        self.assertIn('ORDER BY pg_get_userbyid',security)
        self.assertEqual(record['application_roles'],self.roles())

    def test_archive_exclusive_persistence_and_verified_disk_readback(self):
        path=self.root/'pilot.dump';payload=b'PGDMP'+self.data
        with patch.object(recovery.os,'fsync') as sync:recovery.persist_private(path,payload)
        sync.assert_called_once()
        metadata={'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest()}
        self.assertEqual(recovery.stored_archive(path,metadata),payload)
        with self.assertRaises(FileExistsError):recovery.persist_private(path,b'overwrite')
        self.assertEqual(path.read_bytes(),payload)
        path.write_bytes(payload[:5]+b'X'+payload[6:])
        with self.assertRaisesRegex(ValueError,'hash differs'):recovery.stored_archive(path,metadata)
        path.write_bytes(payload[:10])
        with self.assertRaisesRegex(ValueError,'size differs'):recovery.stored_archive(path,metadata)

    def test_invalid_archive_metadata_refused_without_live_access(self):
        for metadata in [{'bytes':True,'sha256':'a'*64},{'bytes':recovery.MAX_DUMP_BYTES+1,'sha256':'a'*64},
                         {'bytes':10,'sha256':'bad'},{'bytes':0,'sha256':'a'*64}]:
            with self.subTest(metadata=metadata),self.assertRaises(ValueError):recovery.stored_archive(self.root/'missing.dump',metadata)
        self.denials['command'].assert_not_called()

    def test_output_and_password_links_rejected_before_docker(self):
        original=Path.is_symlink
        linked=self.root/'linked'
        with patch.object(Path,'is_symlink',lambda p:p==linked or original(p)),self.assertRaises(ValueError):
            recovery.run(linked/'output')
        def private(value):
            if Path(value).name=='restore-password':raise ValueError('SYNTHETIC linked password')
            return Path(value)
        with patch.object(recovery,'private_path',side_effect=private),self.assertRaisesRegex(ValueError,'linked password'):
            recovery.start_target()
        self.denials['command'].assert_not_called()

    def test_reparse_ancestor_is_refused(self):
        original=Path.stat
        def stat(path,*args,**kwargs):
            value=original(path,*args,**kwargs)
            if path==self.root:
                return Mock(st_file_attributes=0x400,st_mode=value.st_mode,st_size=value.st_size)
            return value
        with patch.object(Path,'stat',stat),self.assertRaisesRegex(ValueError,'Reparse'):
            recovery.private_path(self.root/'new.dump')

    def missing_role_mocks(self,existing,missing):
        from contextlib import ExitStack
        stack=ExitStack();self.addCleanup(stack.close)
        events=[]
        guard=stack.enter_context(patch.object(recovery,'guard_target',side_effect=lambda:events.append('guard')))
        fresh=stack.enter_context(patch.object(recovery,'fresh_target',side_effect=lambda:events.append('fresh')))
        roles=stack.enter_context(patch.object(recovery,'application_roles',side_effect=[existing,{'roles':[],'memberships':[]},self.roles()]))
        sql=stack.enter_context(patch.object(recovery,'target_sql',side_effect=lambda text,**kw:events.append(text) or self.completed()))
        stack.enter_context(patch.object(recovery,'persist_private'))
        restore=Mock(side_effect=lambda:events.append('restore') or missing)
        return stack,events,guard,fresh,roles,sql,restore

    def test_missing_role_pg_restore_control_repeats_with_existing_or_empty_roles(self):
        missing=self.completed(stderr=b'pg_restore: error: role "dpt_owner" does not exist',returncode=1)
        for existing in [{'roles':[],'memberships':[]},self.roles()]:
            with self.subTest(existing_count=len(existing['roles'])):
                stack,events,guard,fresh,roles,sql,restore=self.missing_role_mocks(existing,missing)
                self.assertTrue(recovery.missing_role_control(self.roles(),restore,self.root))
                self.assertEqual(events[0],'guard');self.assertEqual(events[1],'fresh')
                self.assertIn('DROP ROLE IF EXISTS',events[2]);self.assertEqual(events[3],'restore')
                self.assertEqual(fresh.call_count,2);restore.assert_called_once()
                text=''.join(call.args[0] for call in sql.call_args_list)
                self.assertNotIn('CASCADE',text);self.assertNotIn('DROP OWNED',text);self.assertNotIn('FORCE',text)
                for role in recovery.APP_ROLES:self.assertIn('DROP ROLE IF EXISTS "'+role+'"',text)
                stack.close()

    def test_missing_role_control_rejects_unrelated_error_or_unexpected_success(self):
        for failure in [self.completed(stderr=b'23514 unrelated failure',returncode=1),self.completed(stderr=b'role "dpt_owner" does not exist')]:
            stack,_,_,_,_,_,restore=self.missing_role_mocks(self.roles(),failure)
            with self.assertRaisesRegex(RuntimeError,'absent role'):recovery.missing_role_control(self.roles(),restore,self.root)
            stack.close()

    def test_unsafe_retained_role_refused_before_database_reset(self):
        bad=self.roles();bad['roles'][0]['rolsuper']=True
        with patch.object(recovery,'guard_target'),patch.object(recovery,'application_roles',return_value=bad),patch.object(recovery,'fresh_target') as fresh:
            with self.assertRaises(ValueError):recovery.missing_role_control(self.roles(),Mock(),self.root)
        fresh.assert_not_called();self.denials['command'].assert_not_called()

    def test_role_drop_dependency_failure_does_not_cascade_or_restore(self):
        restore=Mock()
        with patch.object(recovery,'guard_target'),patch.object(recovery,'application_roles',return_value=self.roles()),patch.object(recovery,'fresh_target'),patch.object(recovery,'target_sql',side_effect=RuntimeError('dependent objects')) as sql:
            with self.assertRaisesRegex(RuntimeError,'dependent objects'):recovery.missing_role_control(self.roles(),restore,self.root)
        restore.assert_not_called();self.assertNotIn('CASCADE',sql.call_args.args[0])

    def test_recreated_roles_must_match_source_exactly(self):
        failure=self.completed(stderr=b'role "dpt_owner" does not exist',returncode=1)
        stack,_,_,_,roles,_,restore=self.missing_role_mocks(self.roles(),failure)
        wrong=self.roles();wrong['roles'][0]['rolinherit']=False
        roles.side_effect=[self.roles(),{'roles':[],'memberships':[]},wrong]
        with self.assertRaisesRegex(RuntimeError,'differ from source'):
            recovery.missing_role_control(self.roles(),restore,self.root)
        stack.close()

    def test_nonowner_probe_requires_42501_and_rolls_back_even_if_allowed(self):
        for code,stderr,expected in [(1,b'ERROR: 42501: permission denied',True),(1,b'ERROR: 23514: other constraint',False),(0,b'',False)]:
            def target(text):
                if "'unsafe'" in text:return '{"count":1,"unsafe":0}'
                if text.startswith('SELECT count(*) FROM dpt.users'):return '0'
                return ''
            with self.subTest(code=code,stderr=stderr),patch.object(recovery,'target_sql',side_effect=[self.completed(b'0'),self.completed(stderr=stderr,returncode=code)]) as sql:
                checks=recovery.nonowner_controls(target)
                self.assertIs(checks['nonowner_mutation_denied'],expected)
                self.assertTrue(checks['nonowner_probe_preserved_rows'])
                probe=sql.call_args_list[1].args[0]
                self.assertTrue(probe.startswith('BEGIN;'));self.assertTrue(probe.endswith('ROLLBACK;'))
                self.assertNotIn('COMMIT',probe)

    def test_unsafe_synthetic_outsider_blocks_probe(self):
        target=Mock(side_effect=['','{"count":1,"unsafe":1}'])
        with patch.object(recovery,'target_sql') as sql,self.assertRaisesRegex(RuntimeError,'outsider role is unsafe'):
            recovery.nonowner_controls(target)
        sql.assert_not_called()

    def test_target_psql_emits_verbose_permission_sqlstate(self):
        with patch.object(recovery,'guard_target'),patch.object(recovery,'command',return_value=self.completed()) as command:
            recovery.target_sql('SELECT 1;')
        self.assertIn('VERBOSITY=verbose',command.call_args.args)

    def run_fixture(self,corrupt_stored=False):
        from contextlib import ExitStack
        stack=ExitStack();self.addCleanup(stack.close)
        directory=self.root/'run'
        stack.enter_context(patch.object(recovery.benchmark,'common_repository_root',return_value=self.root))
        stack.enter_context(patch.object(recovery.local,'guard'))
        security={'rls_tables':[['perfumes',True,True,'dpt_owner']],'policies':[],'constraints':[],'triggers':[],'functions':[]}
        snapshot={'tables':[{'relation':'dpt.perfumes','rows':1,'sha256':'a'*64}],'security':security,'application_roles':self.roles()}
        stack.enter_context(patch.object(recovery,'fingerprint',side_effect=[snapshot,copy.deepcopy(snapshot),copy.deepcopy(snapshot),copy.deepcopy(snapshot)]))
        stack.enter_context(patch.object(recovery,'start_target'))
        stack.enter_context(patch.object(recovery,'guard_target'))
        stack.enter_context(patch.object(recovery,'fresh_target'))
        stack.enter_context(patch.object(recovery,'missing_role_control',return_value=True))
        stack.enter_context(patch.object(recovery,'nonowner_controls',return_value={'nonowner_private_perfumes_hidden':True,'nonowner_mutation_denied':True,'nonowner_probe_preserved_rows':True}))
        stack.enter_context(patch.object(recovery,'target_sql',return_value=self.completed(b'["perfumes",false,true,"dpt_owner"]')))
        payload=b'PGDMP'+b'SYNTHETIC owned dump fixture '*20
        captured=[]
        def command(*args,**kwargs):
            captured.append((args,kwargs))
            if 'pg_dump' in args:return self.completed(payload)
            content=kwargs['input']
            return self.completed(stderr=b'truncated synthetic archive',returncode=1) if len(content)==100 else self.completed()
        stack.enter_context(patch.object(recovery,'command',side_effect=command))
        original=recovery.stored_archive;readbacks=[]
        def disk(path,metadata):
            readbacks.append(path)
            if corrupt_stored and len(readbacks)==3:
                contents=path.read_bytes();path.write_bytes(contents[:-1]+b'X')
            return original(path,metadata)
        stack.enter_context(patch.object(recovery,'stored_archive',side_effect=disk))
        return directory,payload,captured,readbacks

    def test_orchestration_restores_verified_disk_bytes_and_records_exact_code_hash(self):
        directory,payload,captured,reads=self.run_fixture()
        report=recovery.run(directory)
        self.assertEqual(len(reads),3)
        restores=[kw['input'] for args,kw in captured if 'pg_restore' in args]
        self.assertEqual(restores,[payload[:100],payload])
        self.assertEqual(report['source_code_sha256'],hashlib.sha256(Path(recovery.__file__).read_bytes()).hexdigest())
        self.assertTrue(all(value is True for value in report['checks'].values()))
        self.assertEqual(json.loads((directory/'recovery_report.json').read_text())['status'],'VERIFIED_LOCAL_DB_AND_SYNTHETIC_OBJECT_SUBSET')
        self.assertFalse(list(directory.glob('*.tmp')));self.denials['sql'].assert_not_called()

    def test_corrupt_saved_archive_blocks_positive_restore_and_reports_failure(self):
        directory,_,captured,_=self.run_fixture(corrupt_stored=True)
        with self.assertRaisesRegex(ValueError,'hash differs'):recovery.run(directory)
        self.assertEqual(sum('pg_restore' in args for args,_ in captured),1)
        self.assertEqual(json.loads((directory/'recovery_report.json').read_text())['status'],'FAILED_STOPPED')

    def test_not_run_control_can_never_be_reported_verified(self):
        directory,_,_,_=self.run_fixture()
        with patch.object(recovery,'missing_role_control',return_value='NOT RUN: synthetic skip'):
            with self.assertRaisesRegex(RuntimeError,'control was not run'):recovery.run(directory)
        self.assertEqual(json.loads((directory/'recovery_report.json').read_text())['status'],'FAILED_STOPPED')

    def test_shared_benchmark_lease_blocks_recovery_before_output_or_docker(self):
        directory=self.root/'blocked'
        with recovery.benchmark.RunLease(self.root),patch.object(recovery.benchmark,'common_repository_root',return_value=self.root):
            with self.assertRaises(FileExistsError):recovery.run(directory)
        self.assertFalse(directory.exists());self.denials['command'].assert_not_called()

    def test_report_is_reserved_before_resource_access_and_failure_is_atomic(self):
        directory=self.root/'failure'
        def denied():
            reserved=json.loads((directory/'recovery_report.json').read_text())
            self.assertIn('owner_nonce',reserved)
            raise RuntimeError('SYNTHETIC source guard failure')
        with patch.object(recovery.benchmark,'common_repository_root',return_value=self.root),patch.object(recovery.local,'guard',side_effect=denied):
            with self.assertRaisesRegex(RuntimeError,'source guard failure'):recovery.run(directory)
        self.assertEqual(json.loads((directory/'recovery_report.json').read_text())['status'],'FAILED_STOPPED')
        self.assertFalse(list(directory.glob('*.tmp')))


class RecoveryAclDatabaseTests(unittest.TestCase):
    """Read-only PostgreSQL regression for empty ACLs versus default privileges."""
    def evaluate(self, expression, kind):
        owner="(SELECT oid FROM pg_roles WHERE rolname='postgres')"
        sql='SELECT '+recovery.normalized_acl(expression,kind,owner)+';'
        return json.loads(recovery.local.sql(sql,'postgres').stdout)

    def test_empty_explicit_relation_acl_stays_empty(self):
        self.assertEqual(self.evaluate("'{}'::aclitem[]",'r'),[])

    def test_null_or_empty_column_acl_has_no_explicit_grants(self):
        for expression in ["NULL::aclitem[]","'{}'::aclitem[]"]:
            with self.subTest(expression=expression):self.assertEqual(self.evaluate(expression,None),[])

    def test_null_relation_acl_keeps_postgresql_owner_defaults(self):
        grants=self.evaluate('NULL::aclitem[]','r')
        self.assertTrue(any(row[1]=='postgres' and row[2]=='SELECT' for row in grants))

    def rights_manifest(self,expression):
        return {'constraints':[['rights_assessments','rights_assessments_k4','c',True,expression]],
                'other_security':'SYNTHETIC unchanged control'}

    def test_known_check_associativity_is_proven_against_independent_rule(self):
        source=self.rights_manifest(RIGHTS_CHECK_FORMS[0])
        restored=self.rights_manifest(RIGHTS_CHECK_FORMS[1])
        result=recovery.security_equivalence(source,restored,lambda sql:recovery.local.sql(sql,'postgres').stdout)
        self.assertTrue(result['equal']);self.assertEqual(result['proof']['cases'],8748)

    def test_wrong_rights_check_cannot_pass_equivalence_exception(self):
        correct="CHECK (NOT (research_use='allowed' OR automation_use='allowed' OR cache_use='allowed' OR storage_use='allowed' OR display_use='allowed' OR redistribution_use='allowed' OR ai_use='allowed') OR (evidence_url IS NOT NULL AND btrim(evidence_url)<>''))"
        result=recovery.security_equivalence(self.rights_manifest(correct),self.rights_manifest('CHECK (true)'),lambda sql:recovery.local.sql(sql,'postgres').stdout)
        self.assertFalse(result['equal'])


class SecurityComparisonOfflineTests(unittest.TestCase):
    def test_unrelated_security_or_constraint_differences_fail_before_sql(self):
        left={'constraints':[['other','other_check','c',True,'CHECK (true)']],'policies':[]}
        for right in [dict(left,policies=['wrong']),dict(left,constraints=[]),dict(left,constraints=[['other','other_check','c',True,'CHECK (false)']])]:
            query=Mock();self.assertFalse(recovery.security_equivalence(left,right,query)['equal']);query.assert_not_called()

    def test_incomplete_truth_table_or_failed_predicate_is_rejected(self):
        key=['rights_assessments','rights_assessments_k4','c',True]
        left={'constraints':[[*key,RIGHTS_CHECK_FORMS[0]]]};right={'constraints':[[*key,RIGHTS_CHECK_FORMS[1]]]}
        for proof in [{'cases':8747,'source_equivalent':True,'restored_equivalent':True},
                      {'cases':8748,'source_equivalent':True,'restored_equivalent':False}]:
            self.assertFalse(recovery.security_equivalence(left,right,Mock(return_value=json.dumps(proof)))['equal'])

    def test_unsampled_whitespace_bypass_is_rejected_before_truth_table(self):
        key=['rights_assessments','rights_assessments_k4','c',True]
        altered="CHECK ("+RIGHTS_CHECK_FORMS[0][6:]+" OR (evidence_url IS NOT DISTINCT FROM '   '))"
        query=Mock(return_value=json.dumps({'cases':8748,'source_equivalent':True,'restored_equivalent':True}))
        result=recovery.security_equivalence({'constraints':[[*key,RIGHTS_CHECK_FORMS[0]]]}, {'constraints':[[*key,altered]]},query)
        self.assertFalse(result['equal']);query.assert_not_called()


if __name__=='__main__':unittest.main()
