"""Original timestamp guard controls; future dates/revocation are SYNTHETIC, rolled back.

These tests do not simulate or prove the historical intermittent wall-clock defect.
"""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import local
import recovery
import scento_etl as etl


class ReviewTimestampTests(unittest.TestCase):
    DB = 'dpt_scento_test'

    @classmethod
    def setUpClass(cls):
        source = local.ROOT.parent / ('DoomParfum Local Data/Master Handoff/'
            'DoomParfum_Master_Handoff_2026-11-11/09_LOCAL_LICENSED_SOURCE/scento_pinned')
        snapshot = etl.load_snapshot(source)
        plan = etl.build_plan(snapshot, 'pilot')
        mapping = etl.mapping_proposal(plan, snapshot)
        mapping.update(status='reviewed', reviewed_by='Independent exact-source mapping review',
            review_evidence={'report_sha256': etl.MAPPING_REVIEW_SHA256,
                'proposal_sha256': etl.REVIEWED_PROPOSAL_SHA256['pilot']})
        etl.validate_mapping(mapping, plan, snapshot)
        # Normal DROP refuses competing sessions; only this disposable test DB is reset.
        local.sql('DROP DATABASE IF EXISTS dpt_scento_test;', 'postgres')
        local.sql('CREATE DATABASE dpt_scento_test;', 'postgres')
        local.migrate(cls.DB)
        etl.run_import(snapshot, 'pilot', cls.DB, mapping)
        cls.where = "entity_id=" + etl.q(etl.entity_id('perfume', 'dior-jadore')) + " AND field_path='name'"
        if int(cls.sql('SELECT count(*) FROM dpt.canonical_selections WHERE ' + cls.where)) != 1:
            raise AssertionError('Expected exactly one reviewed control row')
        cls.original_guard = cls.sql("SELECT pg_get_functiondef('dpt_guard.selection_guard()'::regprocedure);")
        if 'IF NEW.reviewed_at>clock_timestamp()' not in cls.original_guard:
            raise AssertionError('Expected the original future-review guard')

    @classmethod
    def sql(cls, text):
        return local.sql(text, cls.DB).stdout

    def insert_existing(self, timestamp):
        return ('INSERT INTO dpt.canonical_selections SELECT (jsonb_populate_record('
            'NULL::dpt.canonical_selections,to_jsonb(s)||jsonb_build_object('
            "'reviewed_at'," + timestamp + '))).* FROM dpt.canonical_selections s WHERE '
            + self.where + ' ON CONFLICT DO NOTHING;')

    def check_transaction(self, body, expected_error=None, *, rollback=False):
        before = recovery.fingerprint(self.sql)
        result = local.sql('BEGIN;' + body + ('ROLLBACK;' if expected_error or rollback else 'COMMIT;'),
            self.DB, check=False)
        if expected_error:
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('23514', result.stderr)
            self.assertIn(expected_error, result.stderr)
        else:
            self.assertEqual(result.returncode, 0, result.stderr)
        # Includes original review times, rationale, observations, audit, roles and security.
        self.assertEqual(before, recovery.fingerprint(self.sql))
        self.assertEqual(self.original_guard,
            self.sql("SELECT pg_get_functiondef('dpt_guard.selection_guard()'::regprocedure);"))

    def test_current_statement_conflict_preserves_original_review_and_audit(self):
        self.check_transaction(self.insert_existing('statement_timestamp()'))

    def test_current_update_is_validated_then_explicitly_rolled_back(self):
        self.check_transaction('UPDATE dpt.canonical_selections SET reviewed_at=statement_timestamp() WHERE '
            + self.where + ';', rollback=True)

    def test_future_update_is_rejected_and_fully_rolled_back(self):
        self.check_transaction("UPDATE dpt.canonical_selections SET reviewed_at="
            "clock_timestamp()+interval '1 day' WHERE " + self.where + ';', 'Future review timestamp')

    def test_future_insert_is_rejected_before_conflict_suppression(self):
        self.check_transaction(self.insert_existing("statement_timestamp()+interval '1 day'"),
            'Future review timestamp')

    def test_revoked_source_rights_still_reject_conflict_replay(self):
        self.check_transaction('UPDATE dpt.rights_assessments SET revoked_at=clock_timestamp() WHERE id='
            + etl.q(etl.RIGHTS_ID) + ';' + self.insert_existing('statement_timestamp()'),
            'Selection requires active storage/display rights')


if __name__ == '__main__':
    unittest.main()
