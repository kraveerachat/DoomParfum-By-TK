"""Pinned licensed-data ETL tests; malformed controls are explicitly synthetic."""
import copy
import concurrent.futures
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import scento_etl as etl
import local

SOURCE = local.ROOT.parent / 'DoomParfum Local Data/Master Handoff/DoomParfum_Master_Handoff_2026-11-11/09_LOCAL_LICENSED_SOURCE/scento_pinned'


class ScentoOfflineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = etl.load_snapshot(SOURCE)

    def test_pinned_artifacts_and_approved_pilot_are_exact(self):
        p = etl.build_plan(self.snapshot, 'pilot')
        self.assertEqual((len(p['perfumes']),len(p['houses']),len(p['materials']),p['note_occurrences']), (12,5,58,93))
        self.assertIn('lattafa-khamrah',p['review'])
        self.assertEqual(len(p['promotable']),11)
        self.assertEqual(len(self.snapshot['artifacts']),6)

    def test_source_and_plan_replay_are_deterministic(self):
        a=etl.build_plan(self.snapshot,'full');b=etl.build_plan(etl.load_snapshot(SOURCE),'full')
        self.assertEqual(etl.canonical(a),etl.canonical(b))
        self.assertEqual(len(a['perfumes']),1479)
        self.assertEqual(len(a['promotable'])+len(a['review'])+len(a['quarantined']),1479)
        self.assertEqual(a['note_occurrences'],12448)

    def test_tampered_license_or_csv_fails_before_staging(self):
        for name in ['LICENSE','perfumes.csv','datapackage.json']:
            with self.subTest(name=name), tempfile.TemporaryDirectory(dir=local.ROOT/'.local') as tmp:
                p=Path(tmp)
                for file in SOURCE.iterdir():
                    if file.name in etl.EXPECTED:p.joinpath(file.name).write_bytes(file.read_bytes())
                p.joinpath(name).write_bytes(p.joinpath(name).read_bytes()+b'\nSYNTHETIC TAMPER')
                with self.assertRaisesRegex(ValueError,'Pinned source hash'):
                    etl.load_snapshot(p)

    def test_synthetic_malformed_unknown_and_duplicate_notes_are_not_promoted(self):
        row=copy.deepcopy(etl.build_plan(self.snapshot,'pilot')['perfumes'][0])
        for change,reason in [({'year':'not-a-year'},'shape'),({'top_notes':'SYNTHETIC unknown label'},'notes'),
                              ({'top_notes':'Rose;Rose'},'notes')]:
            with self.subTest(change=change):
                altered=dict(row,**change)
                result=etl.classify(altered,self.snapshot)
                self.assertNotEqual(result['state'],'promotable');self.assertIn(reason,result['reasons'])
        self.assertIsNone(etl.optional_year(''))
        self.assertNotEqual(etl.entity_id('perfume','balmain-bleu-infini'),etl.entity_id('perfume','balmain-bleu-infini-toilette'))

    def test_mapping_manifest_requires_review_and_exact_source_binding(self):
        plan=etl.build_plan(self.snapshot,'pilot');mapping=etl.mapping_proposal(plan,self.snapshot)
        with self.assertRaisesRegex(ValueError,'reviewed mapping'):
            etl.validate_mapping(mapping,plan,self.snapshot)
        mapping['status']='reviewed';mapping['reviewed_by']='Independent exact-source mapping review'
        mapping['review_evidence']={'report_sha256':etl.MAPPING_REVIEW_SHA256,
                                    'proposal_sha256':etl.REVIEWED_PROPOSAL_SHA256['pilot']}
        etl.validate_mapping(mapping,plan,self.snapshot)
        mapping['notes'][0]['canonical_id']=etl.entity_id('note','SYNTHETIC wrong')
        with self.assertRaisesRegex(ValueError,'mapping content'):
            etl.validate_mapping(mapping,plan,self.snapshot)

    def test_forged_review_marker_and_unapproved_database_are_refused(self):
        plan=etl.build_plan(self.snapshot,'pilot');mapping=etl.mapping_proposal(plan,self.snapshot)
        mapping.update(status='reviewed',reviewed_by='SYNTHETIC forged reviewer',review_evidence={'report_sha256':'a'*64})
        with self.assertRaisesRegex(ValueError,'hash-bound'):
            etl.validate_mapping(mapping,plan,self.snapshot)
        for target in ['dpt_foundation','postgres','unapproved_remote_database']:
            with self.subTest(target=target),self.assertRaisesRegex(ValueError,'allowlist'):
                etl.run_import(self.snapshot,'pilot',target)

    def test_existing_output_is_refused_before_database_access(self):
        with tempfile.TemporaryDirectory(dir=local.ROOT/'.local') as temp:
            report=Path(temp)/'review.json';report.write_text('SYNTHETIC existing reviewer evidence')
            argv=['scento_etl.py','--source-dir',str(SOURCE),'--report',str(report)]
            with mock.patch.object(sys,'argv',argv),mock.patch.object(etl,'prepare_database') as prepare:
                with self.assertRaisesRegex(ValueError,'overwrite'):
                    etl.main()
                prepare.assert_not_called()
            self.assertEqual(report.read_text(),'SYNTHETIC existing reviewer evidence')


class ScentoDatabaseTests(unittest.TestCase):
    DB='dpt_scento_test'

    @classmethod
    def setUpClass(cls):
        cls.snapshot=etl.load_snapshot(SOURCE);local.recreate(cls.DB);local.migrate(cls.DB)
        cls.plan=etl.build_plan(cls.snapshot,'pilot')

    def test_01_real_pilot_staging_replay_preserves_raw_and_creates_no_catalogue(self):
        first=etl.run_import(self.snapshot,'pilot',self.DB)
        second=etl.run_import(self.snapshot,'pilot',self.DB)
        self.assertEqual(first['staged_perfumes'],12)
        self.assertEqual(first['source_records'],75)
        self.assertEqual(second['new_source_records'],0);self.assertEqual(second['new_staging_records'],0)
        self.assertEqual(first['catalogue_perfumes'],0)
        self.assertEqual(first['raw_note_occurrences'],93)

    def test_02_unreviewed_mapping_refuses_promotion_without_writes(self):
        proposal=etl.mapping_proposal(self.plan,self.snapshot)
        with self.assertRaisesRegex(ValueError,'reviewed mapping'):
            etl.run_import(self.snapshot,'pilot',self.DB,mapping=proposal)
        self.assertEqual(local.sql('SELECT count(*) FROM dpt.perfumes;',self.DB).stdout.strip(),'0')

    def test_03_rights_revocation_and_expiry_cannot_be_bypassed_by_replay(self):
        for mutation in ['revoked_at=clock_timestamp()']:
            with self.subTest(mutation=mutation):
                script='BEGIN;UPDATE dpt.rights_assessments SET '+mutation+' WHERE id='+etl.q(etl.RIGHTS_ID)+';'
                if mutation.startswith('review_after'):script+='SELECT pg_sleep(0.05);'
                result=local.sql(script+etl.import_sql(self.snapshot,self.plan,transaction=False)+'ROLLBACK;',self.DB,check=False)
                self.assertNotEqual(result.returncode,0);self.assertIn('42501',result.stderr)

        expiring=etl.entity_id('SYNTHETIC-rights','elapsed-control')
        clone="""INSERT INTO dpt.rights_assessments SELECT (jsonb_populate_record(NULL::dpt.rights_assessments,
          to_jsonb(r)||jsonb_build_object('id',%s,'checked_at',clock_timestamp()-interval '1 second',
          'review_after',clock_timestamp()+interval '0.02 seconds','reviewer','SYNTHETIC expiry control'))).*
          FROM dpt.rights_assessments r WHERE id=%s;SELECT pg_sleep(0.05);""" % (etl.q(expiring),etl.q(etl.RIGHTS_ID))
        with mock.patch.object(etl,'RIGHTS_ID',expiring):
            result=local.sql('BEGIN;'+clone+etl.import_sql(self.snapshot,self.plan,transaction=False)+'ROLLBACK;',self.DB,check=False)
        self.assertNotEqual(result.returncode,0);self.assertIn('42501',result.stderr)

    def test_04_transaction_failure_rolls_back_capture_and_batch(self):
        before=etl.inventory(self.DB)
        text=etl.import_sql(self.snapshot,etl.build_plan(self.snapshot,'full'),transaction=False)
        result=local.sql('BEGIN;'+text+"SELECT 1/0;COMMIT;",self.DB,check=False)
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(before,etl.inventory(self.DB))

    def test_05_non_owner_cannot_read_staging_or_private_capture(self):
        setup="DO $$BEGIN IF NOT EXISTS(SELECT FROM pg_roles WHERE rolname='dpt_etl_outsider') THEN CREATE ROLE dpt_etl_outsider LOGIN NOSUPERUSER NOBYPASSRLS;END IF;END$$;GRANT dpt_runtime TO dpt_etl_outsider;"
        local.sql(setup,self.DB)
        for table in ['sources','rights_assessments','source_records','ingestion_batches','staging_records']:
            result=local.sql('SELECT count(*) FROM dpt.'+table+';',self.DB,user='dpt_etl_outsider',check=False)
            self.assertTrue(result.returncode!=0 or result.stdout.strip()=='0',table)

    def reviewed(self):
        file=SOURCE.parents[1]/'08_OUTPUTS_APPROVED/implementation/mapping/pilot_reviewed.json'
        return json.loads(file.read_text(encoding='utf-8'))

    def test_06_reviewed_private_pilot_promotes_eleven_and_retains_khamrah_hold(self):
        result=etl.run_import(self.snapshot,'pilot',self.DB,mapping=self.reviewed())
        self.assertEqual(result['catalogue_perfumes'],12)
        self.assertEqual(result['approved_perfumes'],11)
        self.assertEqual(result['matching_eligible_count'],0)
        held=local.sql("SELECT error_codes FROM dpt.staging_records WHERE batch_id="+
                       etl.q(result['batch_id'])+" AND external_key='perfume:lattafa-khamrah';",self.DB).stdout
        self.assertIn('external_conflict_pending',held)
        self.assertNotIn('canonical_mapping_review_required',held)
        self.assertEqual(local.sql('SELECT count(*) FROM dpt.perfume_notes WHERE perfume_id='+
                         etl.q(etl.entity_id('perfume','lattafa-khamrah'))+';',self.DB).stdout.strip(),'0')

    def test_07_promoted_pilot_replay_has_zero_new_rows_or_joins(self):
        before=etl.inventory(self.DB)
        result=etl.run_import(self.snapshot,'pilot',self.DB,mapping=self.reviewed())
        self.assertEqual(result['new_source_records'],0);self.assertEqual(result['new_staging_records'],0)
        self.assertEqual(before,etl.inventory(self.DB));self.assertEqual(result['approved_perfumes'],11)

    def test_08_contrary_existing_canonical_row_is_rejected_not_silently_retained(self):
        text="BEGIN;UPDATE dpt.perfumes SET name='SYNTHETIC contrary draft name' WHERE id="+etl.q(etl.entity_id('perfume','lattafa-khamrah'))+';'
        text+=etl.import_sql(self.snapshot,self.plan,self.reviewed(),transaction=False)+'ROLLBACK;'
        result=local.sql(text,self.DB,check=False)
        self.assertNotEqual(result.returncode,0);self.assertIn('Canonical row replay differs',result.stderr)

    def test_09_contrary_existing_selection_is_rejected_without_overwrite(self):
        target=etl.entity_id('perfume','dior-jadore');other=etl.entity_id('SYNTHETIC-observation','contrary-selection')
        text="""BEGIN;INSERT INTO dpt.source_observations
          SELECT (jsonb_populate_record(NULL::dpt.source_observations,to_jsonb(o)||jsonb_build_object(
          'id',%s,'claim_key','SYNTHETIC other extraction','claim_locator','/SYNTHETIC test'))).*
          FROM dpt.source_observations o JOIN dpt.canonical_selections s ON s.observation_id=o.id
          WHERE s.entity_id=%s AND s.field_path='name';
          UPDATE dpt.canonical_selections SET observation_id=%s WHERE entity_id=%s AND field_path='name';""" % (etl.q(other),etl.q(target),etl.q(other),etl.q(target))
        result=local.sql(text+etl.import_sql(self.snapshot,self.plan,self.reviewed(),transaction=False)+'ROLLBACK;',self.DB,check=False)
        self.assertNotEqual(result.returncode,0);self.assertIn('Canonical selection/join replay differs',result.stderr)

    def test_10_contrary_validation_evidence_cannot_silently_win_replay(self):
        text="BEGIN;UPDATE dpt.validation_results SET detail='{}'::jsonb WHERE id=(SELECT id FROM dpt.validation_results ORDER BY id LIMIT 1);"
        result=local.sql(text+etl.import_sql(self.snapshot,self.plan,self.reviewed(),transaction=False)+'ROLLBACK;',self.DB,check=False)
        self.assertNotEqual(result.returncode,0);self.assertIn('Validation evidence replay differs',result.stderr)

    def test_11_data_bearing_pilot_cannot_be_recreated_by_test_helper(self):
        with self.assertRaisesRegex(ValueError,'disposable test'):
            local.recreate('dpt_scento_pilot')

    def test_12_concurrent_full_intake_reports_actual_new_rows_once(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            futures=[pool.submit(etl.run_import,self.snapshot,'full',self.DB) for _ in range(2)]
            results=[future.result() for future in futures]
        self.assertEqual(sorted(r['new_source_records'] for r in results),[0,1984])
        self.assertEqual(sorted(r['new_staging_records'] for r in results),[0,2059])
        self.assertTrue(all(r['batch_accounting']['source_rows']==2059 for r in results))
        self.assertTrue(all(r['staged_perfumes']==1479 for r in results))
        self.assertTrue(all(r['catalogue_perfumes']==12 for r in results))


if __name__=='__main__':unittest.main(verbosity=2)
