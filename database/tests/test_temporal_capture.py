"""Offline diagnostic safety/observability tests; Docker execution is denied."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import temporal_capture as capture


class TemporalCaptureOfflineTests(unittest.TestCase):
    def setUp(self):
        self.process=mock.patch.object(capture.subprocess,'run',
            side_effect=AssertionError('Unexpected process')).start()
        self.addCleanup(mock.patch.stopall)

    def sample(self, **changes):
        row={'marker':capture.MARKER,'entity_id':capture.uid('brand'),
            'observation_id':capture.uid('obs'),'field_path':'name','operation':'INSERT',
            'reviewed_at':'2026-11-12T01:00:00.000001+00:00',
            'comparison_clock':'2026-11-12T01:00:00+00:00',
            'statement_clock':'2026-11-12T01:00:00.000001+00:00',
            'transaction_clock':'2026-11-12T00:59:59+00:00',
            'delta_microseconds':1,'review_equals_statement':True}
        row.update(changes)
        return row

    def test_actual_compared_operands_and_microsecond_delta_are_parseable(self):
        row=self.sample()
        self.assertEqual(capture.operands('DETAIL: '+json.dumps(row)),[row])
        row=self.sample(reviewed_at='2026-11-12T00:59:59.999999+00:00',
            statement_clock='2026-11-12T00:59:59.999999+00:00',delta_microseconds=-1)
        self.assertEqual(capture.operands('NOTICE: '+json.dumps(row)),[row])

    def test_unknown_payload_fields_are_refused(self):
        with self.assertRaisesRegex(ValueError,'fields'):
            capture.operands('DETAIL: '+json.dumps(self.sample(raw_payload='SYNTHETIC forbidden')))

    def test_mismatched_delta_or_naive_clocks_are_refused(self):
        for row in [self.sample(delta_microseconds=0),
                    self.sample(comparison_clock='2026-11-12T01:00:00')]:
            with self.subTest(row=row),self.assertRaises(ValueError):
                capture.operands('DETAIL: '+json.dumps(row))

    def test_tampered_equality_operation_or_extra_clocks_are_refused(self):
        for changes in [{'review_equals_statement':False},{'review_equals_statement':1},
                        {'statement_clock':'2026-11-12T01:00:00.000001'},
                        {'transaction_clock':'invalid'},{'operation':'DELETE'},
                        {'field_path':''},{'delta_microseconds':True},{'delta_microseconds':float('nan')}]:
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                capture.operands('DETAIL: '+json.dumps(self.sample(**changes)))

    def original(self):
        return ('CREATE OR REPLACE FUNCTION SYNTHETIC() RETURNS trigger AS $$\n'
            'DECLARE obs dpt.source_observations;\nBEGIN\n'
            "IF SYNTHETIC_auth THEN RAISE EXCEPTION 'Authorized reviewer required'; END IF;\n"
            "IF SYNTHETIC_rights THEN RAISE EXCEPTION 'Selection requires active storage/display rights'; END IF;\n"
            +capture.PREDICATE+'\nRETURN NEW;\nEND $$;')

    def test_single_sample_rewrite_keeps_preceding_checks_and_return(self):
        original=self.original()
        with mock.patch.object(capture,'ORIGINAL_SHA',capture.digest(original)):
            changed=capture.instrument(original)
        prefix=original.split(capture.PREDICATE)[0].split('BEGIN',1)[1]
        self.assertIn(prefix,changed)
        self.assertEqual(changed.count('clock_timestamp()'),1)
        self.assertIn('IF NEW.reviewed_at>comparison_clock THEN',changed)
        self.assertIn("USING ERRCODE='23514'",changed)
        self.assertTrue(changed.endswith('\nRETURN NEW;\nEND $$;'))
        self.assertNotIn('interval',changed)

    def test_unpinned_or_repeated_predicate_is_refused(self):
        with self.assertRaisesRegex(ValueError,'pin'):
            capture.instrument(self.original())
        repeated=self.original()+capture.PREDICATE
        with mock.patch.object(capture,'ORIGINAL_SHA',capture.digest(repeated)):
            with self.assertRaisesRegex(ValueError,'predicate'):
                capture.instrument(repeated)

    def test_limits_refuse_before_any_process_or_lease(self):
        for count in [0,129,True,-1]:
            with self.subTest(count=count),self.assertRaises(ValueError):
                capture.run('unused',count)
        self.process.assert_not_called()

    def test_unsafe_timestamp_expression_is_refused(self):
        for value in ["clock_timestamp()-interval '1 second'","statement_timestamp());DROP TABLE x;"]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                capture.selection(value)

    def test_invalid_nonce_is_refused(self):
        for value in ['','../other','a'*23,'g'*24]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                capture.Target(value,Path('.local/not-created'))

    def test_expired_deadline_refuses_before_docker(self):
        t=capture.Target('a'*24,capture.local.ROOT/'.local/not-created')
        t.deadline=0
        with self.assertRaises(TimeoutError):
            t.command('inspect',t.container)
        self.process.assert_not_called()

    def test_remote_endpoint_is_refused_before_target_command(self):
        t=capture.Target('a'*24,capture.local.ROOT/'.local/not-created')
        self.process.side_effect=None
        self.process.return_value=subprocess.CompletedProcess([],0,'tcp://remote.invalid:2375','')
        with self.assertRaisesRegex(ValueError,'Non-local'):
            t.command('inspect',t.container)
        self.assertEqual(self.process.call_count,1)

    def test_attestation_rejects_resource_mount_and_ownership_drift(self):
        with tempfile.TemporaryDirectory(dir=capture.local.ROOT/'.local') as temp:
            t=capture.Target('a'*24,Path(temp))
            manifest={'nonce':t.nonce,'container':t.container,'volume':t.volume,'image':capture.local.IMAGE}
            (t.state/'ownership.json').write_text(json.dumps(manifest))
            labels={'com.doomparfum.task':capture.TASK,'com.doomparfum.run':t.nonce}
            info={'Config':{'Labels':labels,'Image':capture.local.IMAGE},
                'HostConfig':{'NetworkMode':'none','PortBindings':{},'Memory':512*1024**2,
                    'NanoCpus':1_000_000_000,'Mounts':[{'Type':'bind','Source':str(t.password),
                        'Target':'/run/secrets/postgres-password','ReadOnly':True}]},
                'Mounts':[{'Type':'volume','Name':t.volume,'Destination':'/var/lib/postgresql/data'},
                    {'Type':'bind','Source':str(t.password),'Destination':'/run/secrets/postgres-password','RW':False}]}
            volume={'Labels':labels}
            def command(*args,**kwargs):
                result=info if args[0]=='inspect' else volume
                return subprocess.CompletedProcess([],0,json.dumps([result]),'')
            with mock.patch.object(t,'command',side_effect=command):
                t.attest()
                for key,value in [('NetworkMode','bridge'),('Memory',1024),('NanoCpus',0)]:
                    old=info['HostConfig'][key];info['HostConfig'][key]=value
                    with self.subTest(key=key),self.assertRaises(RuntimeError):t.attest()
                    info['HostConfig'][key]=old
                info['Mounts'][1]['RW']=True
                with self.assertRaises(RuntimeError):t.attest()
                info['Mounts'][1]['RW']=False
                info['HostConfig']['Mounts'][0]['Source']='another/postgres-password'
                with self.assertRaises(RuntimeError):t.attest()


if __name__=='__main__':
    unittest.main()
