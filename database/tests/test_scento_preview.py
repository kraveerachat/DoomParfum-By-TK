"""Offline preview contract tests. Malformed/raw-value controls are synthetic."""
import ast
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import random
import stat
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import scento_preview as preview

WORKSPACE = Path(__file__).resolve().parents[2]
# No dependency on database/local.py; source location is explicit test configuration.
CHECKOUT_ROOT = WORKSPACE
if (WORKSPACE/'.git').is_file():
    git_directory=Path((WORKSPACE/'.git').read_text(encoding='utf8').split(': ',1)[1].strip())
    if not git_directory.is_absolute():
        git_directory=WORKSPACE/git_directory
    common_directory=(git_directory/(git_directory/'commondir').read_text(encoding='utf8').strip()).resolve()
    CHECKOUT_ROOT=common_directory.parent
SOURCE = Path(os.environ['SCENTO_PREVIEW_SOURCE']) if 'SCENTO_PREVIEW_SOURCE' in os.environ else (
    CHECKOUT_ROOT.parent / 'DoomParfum Local Data/Master Handoff/'
    'DoomParfum_Master_Handoff_2026-11-11/09_LOCAL_LICENSED_SOURCE/scento_pinned')


def synthetic_csv(name='materials.csv', rows=None, header=None):
    fields = tuple(header or dict(preview.TABLES)[name].header)
    output = io.StringIO(newline='')
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(fields)
    for row in rows if rows is not None else [dict(id='synthetic', name='Synthetic')]:
        writer.writerow([row.get(field, '') for field in fields] if isinstance(row, dict) else row)
    return output.getvalue().encode('utf-8')


class PreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in SOURCE.iterdir() if p.is_file()}
        cls.audit_root = SOURCE.parents[1] / '08_OUTPUTS_APPROVED/post_PR4/research/audit_003'
        cls.sidecar_before = {name:hashlib.sha256((cls.audit_root/name).read_bytes()).hexdigest() for name in
                              ('progressive_enrichment_index_1479.json','membership_policy_43_PROPOSED.json','held_conflict_exclusion.json')}
        cls.snapshot = preview.load_snapshot(SOURCE)
        cls.payload = preview.build_preview(SOURCE)

    def setUp(self):
        self.sandbox = tempfile.TemporaryDirectory()
        self.addCleanup(self.sandbox.cleanup)
        self.workspace = Path(self.sandbox.name) / 'workspace'
        self.workspace.mkdir()
        (self.workspace / '.git').write_text('synthetic test workspace', encoding='utf8')
        (self.workspace / '.gitignore').write_text('.local/\n', encoding='utf8')

    def assert_rejected(self, code, call, *args, **kwargs):
        with self.assertRaises(preview.PreviewError) as raised:
            call(*args, **kwargs)
        self.assertEqual(raised.exception.code, code)

    def test_T01_exact_six_pins(self):
        self.assertEqual(len(self.snapshot.artifacts), 6)
        self.assertEqual(sum(len(item.data) for item in self.snapshot.artifacts), 905307)
        self.assertEqual(tuple((a.name, len(a.data), hashlib.sha256(a.data).hexdigest()) for a in self.snapshot.artifacts),
                         tuple((p.name, p.size, p.sha256) for p in preview.PINS))

    def test_T02_five_keys_and_logical_ordinals(self):
        actual = tuple((r['source_file'], r['source_key'], r['data_ordinal']) for r in self.payload['records'])
        self.assertEqual(actual, tuple((s.file, s.key, s.ordinal) for s in preview.SELECTIONS))

    def test_T03_exact_field_allowlists(self):
        self.assertEqual(sum(len(r['fields']) for r in self.payload['records']), 46)
        for record, selection in zip(self.payload['records'], preview.SELECTIONS):
            self.assertEqual(tuple(f['field_locator'] for f in record['fields']), dict(preview.TABLES)[selection.file].fields)

    def test_T04_sixth_record_rejected(self):
        rows = preview.parse_snapshot(self.snapshot)
        self.assert_rejected('SELECTION_SCOPE', preview.select_records, rows, preview.SELECTIONS + (preview.SELECTIONS[0],))

    def test_T05_altered_hash_and_missing_pin(self):
        first = self.snapshot.artifacts[0]
        changed = preview.Artifact(first.name, first.data[:-1] + bytes([first.data[-1] ^ 1]))
        altered = preview.Snapshot(self.snapshot.revision, (changed,) + self.snapshot.artifacts[1:])
        self.assert_rejected('PIN_MISMATCH', preview.transform_snapshot, altered)
        self.assert_rejected('ARTIFACT_SCOPE', preview.transform_snapshot,
                             preview.Snapshot(self.snapshot.revision, self.snapshot.artifacts[:-1]))

    def test_T06_wrong_ordinal_rejected(self):
        selections = list(preview.SELECTIONS)
        selections[0] = preview.Selection(selections[0].file, selections[0].key, selections[0].ordinal + 1)
        self.assert_rejected('SELECTION_SCOPE', preview.select_records, preview.parse_snapshot(self.snapshot), tuple(selections))

    def test_T07_wrong_key_rejected(self):
        rows = dict(preview.parse_snapshot(self.snapshot))
        entries = list(rows['perfumes.csv'])
        entries[643] = dict(entries[643], id='synthetic-wrong-key')
        rows['perfumes.csv'] = tuple(entries)
        self.assert_rejected('LOCATOR_MISMATCH', preview.select_records, tuple(rows.items()))

    def test_T08_header_duplicate_reordered_missing(self):
        header = dict(preview.TABLES)['materials.csv'].header
        for altered in (header[:-1], header + ('id',), tuple(reversed(header))):
            with self.subTest(shape=len(altered)):
                self.assert_rejected('CSV_HEADER', preview.parse_csv, 'materials.csv', synthetic_csv(header=altered), 1)

    def test_T09_extra_short_malformed_cells(self):
        header = dict(preview.TABLES)['materials.csv'].header
        for cells in (['x'] * (len(header)+1), ['x'] * (len(header)-1)):
            self.assert_rejected('CSV_SHAPE', preview.parse_csv, 'materials.csv', synthetic_csv(rows=[cells]), 1)
        malformed = (','.join(header) + '\n"unterminated').encode()
        self.assert_rejected('CSV_SYNTAX', preview.parse_csv, 'materials.csv', malformed, 1)
        for malformed in ((','.join(header)+'\nsynthetic"bare,,,,,,\n').encode(),
                          (','.join(header)+'\nsynthetic\x00,,,,,,\n').encode()):
            self.assert_rejected('CSV_SYNTAX',preview.parse_csv,'materials.csv',malformed,1)

    def test_T10_missing_year_concentration_aliases(self):
        for field in ('year', 'concentration', 'aliases'):
            evidence = preview.field_evidence(preview.SELECTIONS[3 if field == 'aliases' else 0], field, '')
            self.assertEqual((evidence['original_value_state'], evidence['raw_value'], evidence['occurrences']), ('MISSING', None, None))
            self.assertEqual(evidence['closure'], 'UNKNOWN')
        missing = [(r['source_file'], r['data_ordinal'], f['field_locator']) for r in self.payload['records']
                   for f in r['fields'] if f['original_value_state'] == 'MISSING']
        self.assertEqual(missing, [('perfumes.csv',644,'year'),('perfumes.csv',645,'year'),('houses.csv',3,'founded')])

    def test_T11_layers_and_general_separate(self):
        for field, layer in [('top_notes','Top'),('heart_notes','Heart'),('base_notes','Base'),('notes','General')]:
            evidence = preview.field_evidence(preview.SELECTIONS[0], field, 'Synthetic A;Synthetic B')
            self.assertEqual(evidence['domain'], layer)
            self.assertEqual(evidence['closure'], 'UNKNOWN')

    def test_T12_ordered_repeated_occurrences(self):
        evidence = preview.field_evidence(preview.SELECTIONS[0], 'notes', ' Synthetic A;Synthetic A;;Synthetic B ')
        self.assertEqual(evidence['occurrences'], [{'ordinal':1,'raw_token':' Synthetic A'}, {'ordinal':2,'raw_token':'Synthetic A'},
                                                {'ordinal':3,'raw_token':''}, {'ordinal':4,'raw_token':'Synthetic B '}])

    def test_T13_aliases_literal_no_normalization(self):
        evidence = preview.field_evidence(preview.SELECTIONS[3], 'aliases', ' Synthetic Alias;synthetic alias; Synthetic Alias')
        self.assertEqual(evidence['raw_value'], ' Synthetic Alias;synthetic alias; Synthetic Alias')
        self.assertEqual([x['raw_token'] for x in evidence['occurrences']], [' Synthetic Alias','synthetic alias',' Synthetic Alias'])

    def test_T14_no_canonical_selection_or_review(self):
        for record in self.payload['records']:
            self.assertIsNone(record['canonical_id'])
            for field in record['fields']:
                self.assertEqual((field['selection'],field['mapping'],field['review_outcome']), ('UNSELECTED','UNMAPPED','UNKNOWN'))
                self.assertIsNone(field['reviewed_at'])

    def test_T15_no_eligibility_or_fit(self):
        for record in self.payload['records']:
            self.assertEqual(record['matching_eligibility'], 'NOT_AUTHORIZED')
        self.assertNotIn('fit', self.payload)

    def test_T16_T17_T29_stdlib_only_no_architecture_bridge(self):
        tree = ast.parse(Path(preview.__file__).read_text(encoding='utf8'))
        imports = {node.module.split('.')[0] if isinstance(node, ast.ImportFrom) else alias.name.split('.')[0]
                   for node in ast.walk(tree) if isinstance(node,(ast.Import,ast.ImportFrom))
                   for alias in (node.names if isinstance(node,ast.Import) else [None])}
        forbidden = {'local','scento_etl','matching_input','matching_math','socket','urllib','requests','http','subprocess',
                     'psycopg','psycopg2','sqlite3','docker','fastapi','flask','django'}
        self.assertFalse(imports & forbidden)
        self.assertTrue(imports <= sys.stdlib_module_names | {'__future__'})

    def test_T16_T17_runtime_no_network_or_process_calls(self):
        forbidden=AssertionError('forbidden external call')
        with mock.patch('socket.socket',side_effect=forbidden), mock.patch('urllib.request.urlopen',side_effect=forbidden), \
                mock.patch('subprocess.Popen',side_effect=forbidden), mock.patch.object(os,'system',side_effect=forbidden):
            result=preview.publish_preview(SOURCE,self.workspace)
        self.assertEqual(result.payload_sha256,preview.payload_hash(self.payload))

    def test_T18_deterministic_replay(self):
        one = preview.canonical(self.payload)
        two = preview.canonical(preview.build_preview(SOURCE))
        self.assertTrue(one == two)
        self.assertEqual(preview.payload_hash(self.payload), hashlib.sha256(two).hexdigest())
        self.assertFalse(one.startswith(b'\xef\xbb\xbf'))
        self.assertEqual(one, json.dumps(self.payload, ensure_ascii=False, sort_keys=True, separators=(',',':'), allow_nan=False).encode('utf8'))

    def test_T19_execution_time_separate(self):
        a = preview.publish_preview(SOURCE, self.workspace, execution_time='synthetic time one')
        b = preview.publish_preview(SOURCE, self.workspace, execution_time='synthetic time two')
        self.assertEqual(a.payload_sha256,b.payload_sha256)
        self.assertNotEqual(a.bundle_name,b.bundle_name)
        root = self.workspace / preview.PRIVATE_RELATIVE
        self.assertFalse((root/a.bundle_name/'run.json').read_bytes() == (root/b.bundle_name/'run.json').read_bytes())

    def test_T20_windows_replace_failure_preserves_active(self):
        result = preview.publish_preview(SOURCE,self.workspace)
        root = self.workspace / preview.PRIVATE_RELATIVE
        before = (root/'active.json').read_bytes()
        with mock.patch.object(preview.os,'replace',side_effect=PermissionError('synthetic private path forbidden')):
            self.assert_rejected('PUBLICATION_FAILED',preview.publish_preview,SOURCE,self.workspace)
        self.assertTrue(before == (root/'active.json').read_bytes())
        self.assertTrue((root/result.bundle_name/'payload.json').is_file())
        failures = list(root.glob('failure-*.json'))
        self.assertEqual(len(failures),1)
        self.assertNotIn(b'synthetic private path',failures[0].read_bytes())

    def test_T20_partial_candidate_failure_preserves_active(self):
        preview.publish_preview(SOURCE,self.workspace)
        root = self.workspace / preview.PRIVATE_RELATIVE
        before = (root/'active.json').read_bytes()
        with mock.patch.object(preview,'_write_closed',side_effect=OSError('synthetic interruption')):
            self.assert_rejected('PUBLICATION_FAILED',preview.publish_preview,SOURCE,self.workspace)
        self.assertTrue(before == (root/'active.json').read_bytes())

    def test_T20_interruption_retains_failure_evidence_and_prior_pointer(self):
        preview.publish_preview(SOURCE,self.workspace)
        root=self.workspace/preview.PRIVATE_RELATIVE
        before=(root/'active.json').read_bytes()
        with mock.patch.object(preview,'_write_closed',side_effect=KeyboardInterrupt()):
            with self.assertRaises(KeyboardInterrupt):
                preview.publish_preview(SOURCE,self.workspace)
        self.assertTrue(before==(root/'active.json').read_bytes())
        self.assertEqual(len(list(root.glob('failure-*.json'))),1)

    def test_T20_rollback_restores_pointer_retains_history(self):
        first = preview.publish_preview(SOURCE,self.workspace)
        second = preview.publish_preview(SOURCE,self.workspace)
        preview.rollback_preview(SOURCE,self.workspace,first.bundle_name)
        root = self.workspace / preview.PRIVATE_RELATIVE
        self.assertEqual(json.loads((root/'active.json').read_bytes())['bundle'],first.bundle_name)
        self.assertTrue((root/second.bundle_name).is_dir())
        preview.rollback_preview(SOURCE,self.workspace,None)
        self.assertIsNone(json.loads((root/'active.json').read_bytes())['bundle'])

    def test_T21_traversal_source_output_rollback(self):
        self.assert_rejected('UNSAFE_PATH',preview.load_snapshot,SOURCE/'..'/'scento_pinned')
        self.assert_rejected('UNSAFE_PATH',preview.publish_preview,SOURCE,self.workspace/'..'/'workspace')
        preview.publish_preview(SOURCE,self.workspace)
        self.assert_rejected('UNSAFE_PATH',preview.rollback_preview,SOURCE,self.workspace,'../elsewhere')

    def test_T21_source_symlink_or_windows_reparse_rejected(self):
        fake = mock.Mock(st_file_attributes=stat.FILE_ATTRIBUTE_REPARSE_POINT, st_mode=stat.S_IFDIR)
        with mock.patch.object(preview.os,'lstat',return_value=fake):
            self.assert_rejected('UNSAFE_PATH',preview.load_snapshot,SOURCE)

    def test_T21_unc_source_rejected_before_filesystem_read(self):
        if os.name != 'nt':
            return  # Windows-specific drive grammar; no claim about POSIX UNC.
        with mock.patch.object(preview.os,'lstat',side_effect=AssertionError('network filesystem accessed')):
            self.assert_rejected('UNSAFE_PATH',preview.load_snapshot,Path('//synthetic-host/share/source'))

    def test_T21_output_symlink_or_reparse_rejected(self):
        with mock.patch.object(preview,'_is_reparse',return_value=True):
            self.assert_rejected('UNSAFE_PATH',preview.publish_preview,SOURCE,self.workspace)

    def test_T22_parse_verified_bytes_without_reopen(self):
        with mock.patch.object(Path,'read_bytes',side_effect=AssertionError('unverified reopen')):
            built = preview.transform_snapshot(self.snapshot)
        self.assertTrue(preview.canonical(built) == preview.canonical(self.payload))

    def test_T23_all_source_and_sidecars_unchanged(self):
        after = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in SOURCE.iterdir() if p.is_file()}
        self.assertTrue(self.before == after)
        self.assertEqual(len(after),7)

    def test_T24_T25_T26_no_promotion_or_rights_inheritance(self):
        self.assertEqual(self.payload['rights']['audience'],'PRIVATE_LOCAL_REVIEW_ONLY')
        self.assertEqual(self.payload['rights']['linked_content'],'NO_RIGHTS_GRANTED')
        self.assertEqual(self.payload['rights']['images'],'NO_RIGHTS_GRANTED')
        self.assertEqual(self.payload['effects'],{'canonical_writes':False,'normalization_promotion':False,'hold_release':False,'database_mutation':False})

    def test_T24_T25_actual_holds_proposals_sidecars_unchanged(self):
        preview.build_preview(SOURCE)
        after = {name:hashlib.sha256((self.audit_root/name).read_bytes()).hexdigest() for name in self.sidecar_before}
        self.assertTrue(self.sidecar_before == after)
        index=json.loads((self.audit_root/'progressive_enrichment_index_1479.json').read_bytes())
        proposals=json.loads((self.audit_root/'membership_policy_43_PROPOSED.json').read_bytes())
        conflict=json.loads((self.audit_root/'held_conflict_exclusion.json').read_bytes())
        self.assertEqual(sum(row['review_bucket']=='PRESERVED_HELD_SOURCE_PROFILE' for row in index),44)
        self.assertEqual(len(proposals),43)
        self.assertTrue(all(row['policy_status']=='PROPOSED_NOT_APPROVED' and row['hold_status']=='UNCHANGED'
                            and row['canonical_writes']==0 and row['matching_eligibility_change'] is False for row in proposals))
        self.assertEqual(len(conflict),1)
        self.assertTrue(all(row['hold_status']=='UNCHANGED' for row in conflict))
        self.assertTrue(all(row['matching_activation_authorized_by_this_audit'] is False for row in index))

    def test_T27_payload_fixed_private_path_and_no_raw_stdout(self):
        self.assertEqual(preview.PRIVATE_RELATIVE,Path('.local/imp-enr-01/preview-private'))
        with mock.patch('sys.stdout',new_callable=io.StringIO) as captured:
            preview.build_preview(SOURCE)
        self.assertEqual(captured.getvalue(),'')

    def test_T28_current_database_unknown(self):
        self.assertEqual(self.payload['current_database_status'],'NOT_QUERIED_UNKNOWN')
        self.assertEqual(self.payload['source_population'],{'perfumes.csv':1479,'houses.csv':160,'materials.csv':420})

    def test_T30_every_field_provenance_rights_and_versions(self):
        for record in self.payload['records']:
            for field in record['fields']:
                self.assertEqual(field['source_dataset'],'Scento Perfume Database')
                self.assertEqual(field['source_revision'],preview.REVISION)
                self.assertEqual(field['transform_version'],preview.TRANSFORM)
                self.assertEqual(field['schema_version'],preview.SCHEMA)
                self.assertEqual(field['source_key'],record['source_key'])
                self.assertEqual(field['data_ordinal'],record['data_ordinal'])
                self.assertEqual(field['source_file'],record['source_file'])
                pin = next(p for p in preview.PINS if p.name == record['source_file'])
                self.assertEqual(field['file_sha256'],pin.sha256)
        self.assertEqual(self.payload['rights']['license'],'CC BY 4.0')
        self.assertIn('Scento',self.payload['rights']['attribution'])
        self.assertIn('unchanged',self.payload['rights']['transformation_notice'])

    def test_wrong_revision_extra_artifact_and_order(self):
        self.assert_rejected('SOURCE_REVISION',preview.load_snapshot,SOURCE,'synthetic-revision')
        self.assert_rejected('ARTIFACT_SCOPE',preview.transform_snapshot,preview.Snapshot(preview.REVISION,self.snapshot.artifacts+(self.snapshot.artifacts[0],)))
        self.assert_rejected('ARTIFACT_SCOPE',preview.transform_snapshot,preview.Snapshot(preview.REVISION,tuple(reversed(self.snapshot.artifacts))))

    def test_unsupported_encoding_duplicate_id_count_blank_rows(self):
        self.assert_rejected('CSV_ENCODING',preview.parse_csv,'materials.csv',b'\xff',1)
        self.assert_rejected('CSV_DUPLICATE_ID',preview.parse_csv,'materials.csv',synthetic_csv(rows=[{'id':'synthetic'},{'id':'synthetic'}]),2)
        self.assert_rejected('CSV_COUNT',preview.parse_csv,'materials.csv',synthetic_csv(),2)
        self.assert_rejected('CSV_SHAPE',preview.parse_csv,'materials.csv',synthetic_csv()+b'\n',1)

    def test_synthetic_multiline_logical_ordinal(self):
        raw = synthetic_csv(rows=[{'id':'synthetic-a','smell':'Synthetic\nmultiline'}, {'id':'synthetic-b'}])
        parsed = preview.parse_csv('materials.csv',raw,2)
        self.assertEqual(parsed[1]['id'],'synthetic-b')
        self.assertEqual(parsed[0]['smell'],'Synthetic\nmultiline')

    def test_publisher_does_not_accept_payload_or_pin_override(self):
        with self.assertRaises(TypeError):
            preview.publish_preview(SOURCE,self.workspace,payload={'forged':'synthetic'})
        with self.assertRaises(TypeError):
            preview.load_snapshot(SOURCE,expected_pins=())

    def test_publisher_replay_mismatch_fails_closed(self):
        preview.publish_preview(SOURCE,self.workspace)
        root=self.workspace/preview.PRIVATE_RELATIVE
        prior=(root/'active.json').read_bytes()
        with mock.patch.object(preview,'payload_hash',return_value='0'*64):
            self.assert_rejected('PUBLICATION_FAILED',preview.publish_preview,SOURCE,self.workspace)
        self.assertTrue(prior == (root/'active.json').read_bytes())

    def test_concurrent_publisher_lock_fails_closed(self):
        preview.publish_preview(SOURCE,self.workspace)
        root=self.workspace/preview.PRIVATE_RELATIVE
        (root/'publisher.lock').write_bytes(b'synthetic stale lock')
        prior=(root/'active.json').read_bytes()
        self.assert_rejected('PUBLICATION_LOCKED',preview.publish_preview,SOURCE,self.workspace)
        self.assertTrue(prior == (root/'active.json').read_bytes())

    def test_cleanup_failure_after_commit_keeps_success_and_lock(self):
        original=Path.unlink
        def fail_lock(path,*args,**kwargs):
            if path.name=='publisher.lock':
                raise PermissionError('synthetic Windows lock cleanup failure')
            return original(path,*args,**kwargs)
        with mock.patch.object(Path,'unlink',fail_lock):
            result=preview.publish_preview(SOURCE,self.workspace)
        root=self.workspace/preview.PRIVATE_RELATIVE
        self.assertEqual(json.loads((root/'active.json').read_bytes())['bundle'],result.bundle_name)
        self.assertTrue((root/'publisher.lock').exists())
        self.assert_rejected('PUBLICATION_LOCKED',preview.publish_preview,SOURCE,self.workspace)

    def test_unapproved_field_and_locator_extraction_rejected(self):
        self.assert_rejected('FIELD_INPUT',preview.field_evidence,preview.SELECTIONS[0],'description','Synthetic')
        self.assert_rejected('FIELD_INPUT',preview.field_evidence,preview.Selection('perfumes.csv','synthetic-sixth',1),'id','synthetic')

    def test_T22_source_replacement_after_verify_uses_verified_snapshot(self):
        disposable=Path(self.sandbox.name)/'synthetic-replacement-control'
        disposable.mkdir()
        for artifact in self.snapshot.artifacts:
            (disposable/artifact.name).write_bytes(artifact.data)
        verifier=preview._verify_snapshot
        calls=[]
        def replace_after_verification(snapshot):
            verifier(snapshot)
            calls.append(True)
            if len(calls)==1:
                (disposable/'perfumes.csv').write_bytes(b'SYNTHETIC UNVERIFIED REPLACEMENT')
        with mock.patch.object(preview,'_verify_snapshot',replace_after_verification):
            result=preview.build_preview(disposable)
        self.assertTrue(preview.canonical(result)==preview.canonical(self.payload))
        self.assertEqual((disposable/'perfumes.csv').read_bytes(),b'SYNTHETIC UNVERIFIED REPLACEMENT')

    def test_all_six_pins_checked_before_any_parser(self):
        last=self.snapshot.artifacts[-1]
        changed=preview.Artifact(last.name,last.data+b'SYNTHETIC')
        snapshot=preview.Snapshot(preview.REVISION,self.snapshot.artifacts[:-1]+(changed,))
        with mock.patch.object(preview,'parse_csv',side_effect=AssertionError('parser called before all pins')):
            self.assert_rejected('PIN_MISMATCH',preview.transform_snapshot,snapshot)

    def test_numeric_strings_and_whitespace_remain_uninterpreted(self):
        for literal in ('0','0000','not-a-year',' ',' 2026 '):
            evidence=preview.field_evidence(preview.SELECTIONS[0],'year',literal)
            self.assertEqual((evidence['original_value_state'],evidence['raw_value']),('PRESENT',literal))

    def test_rollback_tampered_bundle_rejected(self):
        result=preview.publish_preview(SOURCE,self.workspace)
        root=self.workspace/preview.PRIVATE_RELATIVE
        prior=(root/'active.json').read_bytes()
        (root/result.bundle_name/'payload.json').write_bytes(b'{"synthetic":"forged"}')
        self.assert_rejected('PUBLICATION_FAILED',preview.rollback_preview,SOURCE,self.workspace,result.bundle_name)
        self.assertTrue(prior == (root/'active.json').read_bytes())


class PreviewPropertyTests(unittest.TestCase):
    def test_property_semicolon_occurrences_256_cases(self):
        rng=random.Random(20261117)
        alphabet=['Synthetic A',' Synthetic A','synthetic a ','','Synthetic B','é synthetic']
        for _ in range(256):
            tokens=[rng.choice(alphabet) for _ in range(rng.randint(1,24))]
            raw=';'.join(tokens)
            evidence=preview.field_evidence(preview.SELECTIONS[0],'notes',raw)
            if raw=='':
                self.assertIsNone(evidence['occurrences'])
            else:
                self.assertEqual([o['raw_token'] for o in evidence['occurrences']],tokens)
                self.assertEqual(evidence['raw_value'],raw)

    def test_property_csv_literal_roundtrip_128_cases(self):
        rng=random.Random(644645)
        alphabet=['synthetic',' synthetic ','synthetic;synthetic','synthetic,quoted','synthetic\nline','"synthetic"','é synthetic','']
        for i in range(128):
            row={field:rng.choice(alphabet) for field in dict(preview.TABLES)['materials.csv'].header}
            row['id']='synthetic-'+str(i)
            parsed=preview.parse_csv('materials.csv',synthetic_csv(rows=[row]),1)
            self.assertEqual(parsed[0],row)

    def test_property_canonical_object_permutation_128_cases(self):
        rng=random.Random(46)
        pairs=[('synthetic-'+str(i),{'value':'é ; '+str(i)}) for i in range(16)]
        baseline=preview.canonical(dict(pairs))
        for _ in range(128):
            rng.shuffle(pairs)
            self.assertEqual(preview.canonical(dict(pairs)),baseline)


if __name__=='__main__':
    unittest.main()
