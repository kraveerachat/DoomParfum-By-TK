"""Scoped adapter unit/live tests. Every data record is explicitly SYNTHETIC."""
import copy
import json
from pathlib import Path
import sys
import unittest
import concurrent.futures
import time
from unittest import mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import local
import matching_input as adapter
from fixtures import baseline,uid,q,entity,observation,select,insert


class AdapterOfflineTests(unittest.TestCase):
    def empty(self):
        return {'profile':{'id':uid('perfume'),'review_status':'approved','matching_eligible':False},
            'fields':[],'memberships':[],'brand':None,'over_bound':False}

    def provenance(self):
        result={k:'SYNTHETIC' for k in adapter.Provenance.__dataclass_fields__}
        for k in ['observation_id','source_record_id','rights_id','source_id']:
            result[k]=uid('offline-'+k)
        result.update(payload_sha256='a'*64,reviewed_at='2026-01-01T00:00:00+00:00',
            rights_checked_at='2026-01-01T00:00:00+00:00',rights_review_after=None,
            license_code=None,license_url=None,attribution=None,source_revision=None)
        return result

    def selected(self,path='name',value='SYNTHETIC'):
        result=self.empty()
        result['fields']=[{'path':path,'state':'known_usable','value':value,'provenance':self.provenance()}]
        return result

    def test_invalid_ids_reject_before_transport(self):
        execute=mock.Mock()
        for value in ["';DROP TABLE x;--",'not-uuid',None,42,'']:
            with self.subTest(value=value),self.assertRaises(adapter.InputUnavailable):
                adapter.read_profile(execute,value)
        execute.assert_not_called()

    def test_missing_and_unauthorized_have_uniform_unavailable(self):
        r=self.empty();r['profile']=None
        for value in [r,copy.deepcopy(r)]:
            with self.assertRaisesRegex(adapter.InputUnavailable,'^Input unavailable$'):
                adapter.read_profile(lambda _:value,uid('absent'))

    def test_empty_inputs_do_not_become_empty_complete_domains(self):
        result=adapter.read_profile(lambda _:self.empty(),uid('perfume'))
        self.assertEqual(result.state,adapter.State.ELIGIBILITY)
        self.assertFalse(result.ranking_allowed)
        self.assertTrue(all(v.state is adapter.State.UNKNOWN for _,v in result.layers))
        self.assertIn('unknown',result.completeness)

    def test_eligible_boolean_is_not_a_policy_or_closure_approval(self):
        value=self.empty();value['profile']['matching_eligible']=True
        result=adapter.read_profile(lambda _:value,uid('perfume'))
        self.assertEqual(result.state,adapter.State.INCOMPLETE)
        self.assertFalse(result.ranking_allowed)
        self.assertIn('unavailable',result.accords)

    def test_over_bound_is_explicit_and_transport_errors_are_redacted(self):
        value=self.empty();value['over_bound']=True
        with self.assertRaisesRegex(adapter.AdapterUnavailable,'bound'):
            adapter.read_profile(lambda _:value,uid('perfume'))
        def fail(_):raise RuntimeError('SYNTHETIC sensitive SQL/URI')
        with self.assertRaises(adapter.AdapterUnavailable) as error:
            adapter.read_profile(fail,uid('perfume'))
        self.assertNotIn('sensitive',str(error.exception))

    def test_sql_gates_principal_before_catalogue_and_is_read_only(self):
        sql=adapter.query(uid('perfume'))
        self.assertLess(sql.index('END $gate$;'),sql.index('FROM dpt.perfumes'))
        self.assertIn('BEGIN ISOLATION LEVEL READ COMMITTED READ ONLY;',sql)
        self.assertIn("current_setting('transaction_isolation')<>'read committed'",sql)
        for token in ['rolsuper','rolbypassrls','session_user<>current_user',
                      "automation_use='allowed'","storage_use='allowed'","display_use='allowed'",
                      'revoked_at IS NULL','LIMIT 513','65536']:
            self.assertIn(token,sql)
        self.assertNotIn('staging_records',sql)
        self.assertNotIn('SET ROLE',sql)

    def test_malformed_transport_schema_is_uniformly_rejected(self):
        for change in [{'profile':{}},{'profile':{'id':uid('perfume'),'review_status':'made-up','matching_eligible':False}},
                       {'fields':[{'path':'name','state':'made-up'}]},{'memberships':None}]:
            value=self.empty();value.update(change)
            with self.subTest(change=change),self.assertRaises(adapter.AdapterUnavailable):
                adapter.read_profile(lambda _:value,uid('perfume'))

    def test_provenance_required_times_are_qualified_strings(self):
        for key in ['reviewed_at','rights_checked_at','rights_review_after']:
            for bad in [None,42,{},'','2026-01-01','2026-01-01T00:00:00','not-time']:
                if key=='rights_review_after' and bad is None:continue
                raw=self.selected();raw['fields'][0]['provenance'][key]=bad
                with self.subTest(key=key,bad=bad),self.assertRaisesRegex(adapter.AdapterUnavailable,'^Adapter input contract unavailable$'):
                    adapter.read_profile(lambda _:raw,uid('perfume'))

    def test_nullable_provenance_metadata_is_text(self):
        for key in ['license_code','license_url','attribution','source_revision']:
            for bad in [{},[],42,True]:
                raw=self.selected();raw['fields'][0]['provenance'][key]=bad
                with self.subTest(key=key,bad=bad),self.assertRaises(adapter.AdapterUnavailable):
                    adapter.read_profile(lambda _:raw,uid('perfume'))
        self.assertEqual(dict(adapter.read_profile(lambda _:self.selected(),uid('perfume')).fields)['name'].value,'SYNTHETIC')

    def test_internal_uuids_are_contract_errors_not_missing_inputs(self):
        cases=[]
        raw=self.empty();raw['profile']['id']='not-uuid';cases.append(raw)
        raw=self.selected('brand_id','not-uuid');cases.append(raw)
        for key in ['observation_id','source_record_id','rights_id','source_id']:
            raw=self.selected();raw['fields'][0]['provenance'][key]='not-uuid';cases.append(raw)
        raw=self.selected('notes.top',['SYNTHETIC note'])
        raw['memberships']=[{'layer':'top','id':'not-uuid','name':'SYNTHETIC note','provenance':self.provenance()}];cases.append(raw)
        for raw in cases:
            with self.subTest(raw=raw),self.assertRaisesRegex(adapter.AdapterUnavailable,'^Adapter input contract unavailable$'):
                adapter.read_profile(lambda _:raw,uid('perfume'))

    def test_nested_keys_and_field_states_are_strict(self):
        cases=[]
        raw=self.selected();raw['fields'][0]['unexpected']='SYNTHETIC';cases.append(raw)
        raw=self.selected();raw['fields'][0].pop('value');cases.append(raw)
        for state in ['known_incomplete','eligibility_unavailable','unknown']:
            raw=self.selected();raw['fields'][0]['state']=state;cases.append(raw)
        raw=self.selected();raw['fields'][0]['provenance']['unexpected']='SYNTHETIC';cases.append(raw)
        for raw in cases:
            with self.subTest(raw=raw),self.assertRaises(adapter.AdapterUnavailable):
                adapter.read_profile(lambda _:raw,uid('perfume'))

    def test_all_memberships_and_brand_dtos_are_validated(self):
        member={'layer':'top','id':uid('offline-note'),'name':'SYNTHETIC note','provenance':self.provenance()}
        for key,bad in [('layer','INVALID'),('id','not-uuid'),('name',{}),('provenance',None)]:
            raw=self.empty();raw['memberships']=[{**member,key:bad}]
            with self.subTest(key=key),self.assertRaises(adapter.AdapterUnavailable):
                adapter.read_profile(lambda _:raw,uid('perfume'))
        raw=self.empty();raw['memberships']=[member]
        with self.assertRaises(adapter.AdapterUnavailable):adapter.read_profile(lambda _:raw,uid('perfume'))
        for brand in [{},{'name':{},'provenance':self.provenance()},
                      {'name':'SYNTHETIC','provenance':self.provenance(),'extra':True}]:
            raw=self.empty();raw['brand']=brand
            with self.subTest(brand=brand),self.assertRaises(adapter.AdapterUnavailable):
                adapter.read_profile(lambda _:raw,uid('perfume'))

    def test_note_lists_are_typed_and_memberships_unique(self):
        for bad in [{},[''],[42],['SYNTHETIC',None]]:
            raw=self.selected('notes.top',bad)
            with self.subTest(bad=bad),self.assertRaises(adapter.AdapterUnavailable):
                adapter.read_profile(lambda _:raw,uid('perfume'))
        raw=self.selected('notes.top',['SYNTHETIC note'])
        member={'layer':'top','id':uid('offline-note'),'name':'SYNTHETIC note','provenance':self.provenance()}
        raw['memberships']=[member,copy.deepcopy(member)]
        with self.assertRaises(adapter.AdapterUnavailable):adapter.read_profile(lambda _:raw,uid('perfume'))

    def test_defensive_payload_provenance_and_relationship_bounds(self):
        raw=self.selected(value='x'*65537)
        with self.assertRaises(adapter.AdapterUnavailable):adapter.read_profile(lambda _:raw,uid('perfume'))
        raw=self.selected();raw['fields'][0]['provenance']['attribution']='x'*8193
        with self.assertRaises(adapter.AdapterUnavailable):adapter.read_profile(lambda _:raw,uid('perfume'))
        raw=self.empty();raw['memberships']=[{}]*513
        with self.assertRaisesRegex(adapter.AdapterUnavailable,'bound'):
            adapter.read_profile(lambda _:raw,uid('perfume'))
        raw=self.empty();raw['memberships']=[{'unexpected':'x'*2097153}]
        with self.assertRaisesRegex(adapter.AdapterUnavailable,'bound'):
            adapter.read_profile(lambda _:raw,uid('perfume'))


def private_fixture(key,scope='alice',record=None,status='approved'):
    record=record or uid('record'+scope)
    brand=key+'-brand';note=key+'-note'
    text=entity(brand,'brand','brands',scope=scope,name='SYNTHETIC '+brand,slug=brand)
    text+=entity(note,'note','notes',scope=scope,name='SYNTHETIC '+note,slug=note)
    text+=entity(key,'perfume','perfumes',scope=scope,brand_id=uid(brand),name='SYNTHETIC '+key,slug=key)
    for target,kind,value in [(brand,'brand','SYNTHETIC '+brand),(note,'note','SYNTHETIC '+note),
                               (key,'perfume','SYNTHETIC '+key)]:
        text+=observation('name-'+target,target=target,kind=kind,path='name',value=value,
            scope=scope,source_suffix=scope).replace(q(uid('record'+scope)),q(record))
        text+=select('name-'+target,target=target,kind=kind,path='name',scope=scope)
    text+=observation('brand-'+key,target=key,path='brand_id',value=uid(brand),scope=scope,
        source_suffix=scope).replace(q(uid('record'+scope)),q(record))
    text+=select('brand-'+key,target=key,path='brand_id',scope=scope)
    text+=observation('top-'+key,target=key,path='notes.top',value=['SYNTHETIC '+note],
        scope=scope,source_suffix=scope).replace(q(uid('record'+scope)),q(record))
    text+=select('top-'+key,target=key,path='notes.top',scope=scope)
    text+=insert('perfume_notes',id=uid('join-'+key),access_scope_id=uid(scope),perfume_id=uid(key),
        note_id=uid(note),layer='top',sort_order=0,source_record_id=record)
    text+=f"UPDATE dpt.brands SET review_status='approved' WHERE id={q(uid(brand))};"
    text+=f"UPDATE dpt.notes SET review_status='approved' WHERE id={q(uid(note))};"
    text+=f"UPDATE dpt.perfumes SET review_status={q(status)} WHERE id={q(uid(key))};"
    return text


class AdapterDatabaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Caller must hold common lease. Normal DROP never evicts another connection.
        local.sql('DROP DATABASE IF EXISTS dpt_schema_test;','postgres')
        local.sql('CREATE DATABASE dpt_schema_test;','postgres')
        local.migrate('dpt_schema_test')
        local.sql(baseline()+ 'BEGIN;'+private_fixture('private-a')+
            private_fixture('shared-p',scope='shared')+
            entity('held-a','perfume','perfumes',scope='alice',brand_id=uid('private-a-brand'),
                name='SYNTHETIC held',slug='held-a')+'COMMIT;')
        cls.cohort=local.sql("SELECT count(*) FROM dpt.perfumes;").stdout.strip()

    def read(self,key,user='dpt_test_alice'):
        def execute(script):
            r=local.sql(script,user=user,check=False)
            if r.returncode:raise RuntimeError(r.stderr)
            return json.loads(r.stdout)
        return adapter.read_profile(execute,uid(key))

    def isolated_right_fixture(self,key,automation='allowed',expiry=False):
        right,record=uid(key+'-right'),uid(key+'-record')
        extra=",'checked_at',statement_timestamp(),'review_after',statement_timestamp()+interval '5 seconds'" if expiry else ''
        sql=f"""BEGIN;
INSERT INTO dpt.rights_assessments SELECT (jsonb_populate_record(NULL::dpt.rights_assessments,
 to_jsonb(r)||jsonb_build_object('id','{right}','automation_use','{automation}'{extra}))).*
 FROM dpt.rights_assessments r WHERE id='{uid('rightalice')}';
INSERT INTO dpt.source_records SELECT (jsonb_populate_record(NULL::dpt.source_records,
 to_jsonb(r)||jsonb_build_object('id','{record}','external_key','SYNTHETIC-{key}','rights_id','{right}'))).*
 FROM dpt.source_records r WHERE id='{uid('recordalice')}';
{private_fixture(key,record=record)}
COMMIT;"""
        local.sql(sql)
        return right

    def test_admin_is_rejected_before_profile_query(self):
        with self.assertRaises(adapter.AdapterUnavailable):
            self.read('private-a','postgres')

    def test_automation_right_is_checked_before_returning_selected_values(self):
        self.isolated_right_fixture('automation-blocked','unknown')
        value=self.read('automation-blocked')
        self.assertEqual(dict(value.fields)['name'].state,adapter.State.RIGHTS)
        self.assertTrue(all(v.value is None for _,v in value.fields))
        self.assertNotIn('SYNTHETIC automation-blocked',repr(value))

    def test_existing_readwrite_transaction_is_rejected(self):
        captured=[]
        def execute(script):
            # BEGIN alone has not established a snapshot; PostgreSQL can still
            # switch it to READ ONLY. A used read/write transaction cannot.
            r=local.sql('BEGIN;SELECT 1;'+script,user='dpt_test_alice',check=False)
            captured.append(r.stderr)
            if r.returncode:raise RuntimeError(r.stderr)
            return json.loads(r.stdout)
        with self.assertRaises(adapter.AdapterUnavailable):
            adapter.read_profile(execute,uid('private-a'))
        self.assertIn('25001',captured[0])

    def stale_snapshot_control(self,key,user,revoke,application):
        """Two genuine sessions; wait for a known snapshot before committed revocation."""
        captured=[]
        def execute(script):
            prefix=(f"SET application_name={q(application)};BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY;"
                "SELECT count(*) FROM dpt.perfumes;SELECT pg_sleep(5);")
            r=local.sql(prefix+script,user=user,check=False);captured.append(r.stderr)
            if r.returncode:raise RuntimeError(r.stderr)
            return json.loads(r.stdout.strip().splitlines()[-1])
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            pending=pool.submit(adapter.read_profile,execute,uid(key))
            deadline=time.monotonic()+12
            while time.monotonic()<deadline:
                ready=local.sql("SELECT count(*) FROM pg_stat_activity WHERE application_name="+q(application)+
                    " AND wait_event='PgSleep';",'postgres').stdout.strip()
                if ready=='1':break
                if pending.done():self.fail('Snapshot worker ended before the revocation barrier')
                time.sleep(.05)
            else:self.fail('Snapshot worker did not reach the bounded barrier')
            local.sql(revoke)
            with self.assertRaises(adapter.AdapterUnavailable):pending.result(timeout=15)
        self.assertTrue(captured);self.assertIn('25001',captured[0])
        with self.assertRaisesRegex(adapter.InputUnavailable,'^Input unavailable$'):self.read(key,user)

    def test_reused_repeatable_read_rights_snapshot_is_rejected(self):
        right=self.isolated_right_fixture('rr-rights')
        self.read('rr-rights')
        self.stale_snapshot_control('rr-rights','dpt_test_alice',
            "BEGIN;UPDATE dpt.rights_assessments SET revoked_at=clock_timestamp() WHERE id="+q(right)+";COMMIT;",
            'SYNTHETIC-adapter-rr-rights')

    def test_reused_repeatable_read_shared_snapshot_is_rejected(self):
        self.read('shared-p','dpt_test_bob')
        revoke="BEGIN;UPDATE dpt.scope_members SET revoked_at=clock_timestamp() WHERE access_scope_id="+q(uid('shared'))+" AND user_id="+q(uid('bob'))+";COMMIT;"
        try:self.stale_snapshot_control('shared-p','dpt_test_bob',revoke,'SYNTHETIC-adapter-rr-shared')
        finally:
            local.sql("BEGIN;UPDATE dpt.scope_members SET revoked_at=NULL WHERE access_scope_id="+q(uid('shared'))+" AND user_id="+q(uid('bob'))+";COMMIT;")

    def test_expiry_is_revalidated_without_cache_or_source_mutation(self):
        self.isolated_right_fixture('expiring',expiry=True)
        self.assertEqual(dict(self.read('expiring').fields)['name'].state,adapter.State.USABLE)
        local.sql("SELECT pg_sleep(6);")
        with self.assertRaises(adapter.InputUnavailable):self.read('expiring')

    def test_relevant_open_conflict_withholds_value_and_provenance(self):
        local.sql('BEGIN;'+private_fixture('conflict-p')+
            observation('other-name',target='conflict-p',path='name',value='SYNTHETIC other',
                scope='alice',source_suffix='alice')+
            insert('data_conflicts',id=uid('name-conflict'),access_scope_id=uid('alice'),
                entity_id=uid('conflict-p'),entity_kind='perfume',field_path='name',status='open')+
            ''.join(insert('conflict_members',access_scope_id=uid('alice'),entity_id=uid('conflict-p'),
                entity_kind='perfume',field_path='name',conflict_id=uid('name-conflict'),observation_id=uid(x))
                for x in ['name-conflict-p','other-name'])+'COMMIT;')
        value=self.read('conflict-p');field=dict(value.fields)['name']
        self.assertEqual(value.state,adapter.State.HELD)
        self.assertEqual(field.state,adapter.State.HELD)
        self.assertIsNone(field.value);self.assertIsNone(field.provenance)

    def test_revoked_rights_remove_profile_on_next_request(self):
        right=self.isolated_right_fixture('revocation-p')
        self.read('revocation-p')
        local.sql("BEGIN;UPDATE dpt.rights_assessments SET revoked_at=clock_timestamp() WHERE id="+q(right)+";COMMIT;")
        with self.assertRaises(adapter.InputUnavailable):self.read('revocation-p')

    def test_owner_gets_selected_typed_inputs_and_provenance(self):
        value=self.read('private-a')
        self.assertEqual(value.state,adapter.State.ELIGIBILITY)
        self.assertEqual(dict(value.fields)['name'].value,'SYNTHETIC private-a')
        self.assertEqual(value.brand_name.value,'SYNTHETIC private-a-brand')
        top=dict(value.layers)['top']
        self.assertEqual(top.state,adapter.State.INCOMPLETE)
        self.assertEqual(top.value[0].id,uid('private-a-note'))
        self.assertTrue(top.provenance.source_record_id)
        self.assertFalse(value.ranking_allowed)
        self.assertEqual(dict(value.layers)['heart'].state,adapter.State.UNKNOWN)

    def test_other_user_and_missing_profile_are_uniform(self):
        for key in ['private-a','absent']:
            with self.subTest(key=key),self.assertRaisesRegex(adapter.InputUnavailable,'^Input unavailable$'):
                self.read(key,'dpt_test_bob')

    def test_private_overlay_does_not_affect_bob_public_view(self):
        a=self.read('perfume','dpt_test_bob')
        self.assertNotIn('SYNTHETIC PRIVATE A',repr(a))
        self.assertTrue(all(v.state is adapter.State.UNKNOWN for _,v in a.fields))
        self.assertEqual(a,self.read('perfume','dpt_test_alice'))

    def test_held_private_profile_returns_no_fact_values(self):
        value=self.read('held-a')
        self.assertEqual(value.state,adapter.State.HELD)
        self.assertTrue(all(v.value is None for _,v in (*value.fields,*value.layers)))

    def test_shared_member_then_revocation_is_revalidated(self):
        value=self.read('shared-p','dpt_test_bob')
        self.assertEqual(dict(value.fields)['name'].value,'SYNTHETIC shared-p')
        local.sql("BEGIN;UPDATE dpt.scope_members SET revoked_at=clock_timestamp() WHERE access_scope_id="+q(uid('shared'))+" AND user_id="+q(uid('bob'))+";COMMIT;")
        try:
            with self.assertRaises(adapter.InputUnavailable):self.read('shared-p','dpt_test_bob')
        finally:
            # Membership is mutable; restore fixture only, not a catalogue/source grant.
            local.sql("BEGIN;UPDATE dpt.scope_members SET revoked_at=NULL WHERE access_scope_id="+q(uid('shared'))+" AND user_id="+q(uid('bob'))+";COMMIT;")

    def test_repeated_reads_do_not_write_catalogue_or_eligibility(self):
        import hashlib
        def fingerprint():
            return local.sql("SELECT encode(sha256(convert_to(string_agg(to_jsonb(p)::text,E'\\n' ORDER BY id),'UTF8')),'hex') FROM dpt.perfumes p;").stdout
        before=fingerprint()
        self.read('private-a');self.read('perfume','dpt_test_bob')
        self.assertEqual(before,fingerprint())
        self.assertEqual(local.sql("SELECT count(*) FROM dpt.perfumes WHERE matching_eligible;").stdout.strip(),'0')


if __name__=='__main__':
    unittest.main()
