"""Offline research controls, with explicitly SYNTHETIC inputs and no network/DB."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import research_audit as audit


def perfume(**values):
    return {'id':'SYNTHETIC-perfume','top_notes':'','heart_notes':'','base_notes':'',
        'notes':'Rose;Rose;Jasmine',**values}


def asset(**values):
    return {'asset_candidate_id':'SYNTHETIC-asset','subject_note_name':'SYNTHETIC-note',
        'source_page_url':'https://commons.wikimedia.org/wiki/File:SYNTHETIC.jpg',
        'asset_bytes_acquired':'False','asset_reuse_approved':'False','application_display_approved':'False',
        'downloaded_file_sha256':'','downloaded_file_path':'',**values}


def pair(**values):
    return {'candidate_id':'SYNTHETIC-pair','publisher_group':'SYNTHETIC-same-publisher',
        'usable_relation':'False','verified_dupe':'False','sensory_similarity_percentage':'',
        'structural_overlap_score':'',**values}


class ResearchAuditTests(unittest.TestCase):
    def test_alias_and_country_parent_claims_do_not_become_identity(self):
        seed={'candidate_code':'SYNTHETIC-1','canonical_name':'SYNTHETIC Brand','aliases':'SYNTHETIC Alias',
            'origin_country':'SYNTHETIC origin','market_position':'SYNTHETIC position',
            'catalogue_role':'BOTH','parent_brand_candidate_code':'SYNTHETIC-parent'}
        houses=[{'id':'synthetic-a','name':'SYNTHETIC Alias','country':'OTHER claim','type':'publisher-type'}]
        r=audit.brand_crosswalk([seed],[],houses)[0]
        self.assertEqual(r['raw_candidate'],seed)
        self.assertFalse(r['identity_accepted'])
        self.assertFalse(r['canonical_mutation'])
        self.assertEqual(r['parent_or_related_claim'],'SYNTHETIC-parent')
        self.assertEqual(r['publisher_suggestions'][0]['label_kind'],'alias')
        self.assertEqual(r['candidate_origin_country'],'SYNTHETIC origin')
        self.assertEqual(r['publisher_suggestions'][0]['publisher_country_claim'],'OTHER claim')

    def test_literal_names_do_not_fuzzily_merge_punctuation(self):
        seed={'candidate_code':'SYNTHETIC-1','canonical_name':'SYNTHETIC & Brand'}
        houses=[{'id':'a','name':'SYNTHETIC Brand','country':'','type':''}]
        self.assertEqual(audit.brand_crosswalk([seed],[],houses)[0]['publisher_suggestions'],[])

    def test_ambiguous_publisher_labels_preserve_all_candidates(self):
        seed={'candidate_code':'SYNTHETIC-1','canonical_name':'Same'}
        houses=[{'id':i,'name':'Same','country':'','type':''} for i in ['a','b']]
        result=audit.brand_crosswalk([seed],[],houses)[0]
        self.assertEqual(len(result['publisher_suggestions']),2)
        self.assertFalse(result['identity_accepted'])

    def test_duplicate_research_codes_are_rejected(self):
        row={'candidate_code':'SYNTHETIC','canonical_name':'one'}
        with self.assertRaises(ValueError):
            audit.brand_crosswalk([row],[row],[])

    def test_proposal_preserves_every_duplicate_occurrence_and_raw_string(self):
        row=perfume(notes=' Rose ;Rose;Jasmine')
        result=audit.proposed_membership(row,{'rose':['rose'],'jasmine':['jasmine']})
        self.assertEqual(result['original_source_fields']['notes'],' Rose ;Rose;Jasmine')
        self.assertEqual(len(result['occurrences']),3)
        self.assertEqual(result['repeated_groups'][0]['ordinals'],[0,1])
        self.assertEqual(result['proposed_memberships'][0]['all_original_labels'],['Rose','Rose'])
        self.assertFalse(result['proposed_memberships'][0]['accepted'])
        self.assertEqual(result['hold_status'],'UNCHANGED')
        self.assertEqual(result['canonical_writes'],0)

    def test_same_note_across_layers_is_not_cross_layer_deduplication(self):
        result=audit.proposed_membership(perfume(top_notes='Rose',heart_notes='Rose'),
            {'rose':['rose']})
        self.assertEqual([(m['layer'],m['material_source_id']) for m in result['proposed_memberships']],
            [('top','rose'),('heart','rose')])
        self.assertEqual(result['repeated_groups'],[])
        self.assertEqual(result['completeness'],'UNKNOWN_NO_ABSENCE_INFERENCE')

    def test_unknown_or_ambiguous_material_fails_closed(self):
        for lookup in [{},{'rose':['a','b'],'jasmine':['jasmine']}]:
            with self.subTest(lookup=lookup),self.assertRaises(ValueError):
                audit.proposed_membership(perfume(),lookup)

    def test_held_membership_or_arrays_cannot_drift(self):
        row=perfume()
        snapshot={'rows':{'perfumes.csv':[row]},'note_lookup':{'rose':['rose'],'jasmine':['jasmine']}}
        plan={'review':{row['id']:['notes']},'quarantined':{}}
        prior={'records':[{'source_id':row['id'],'raw_note_lists':{'general':['Rose','Jasmine']}}]}
        with self.assertRaisesRegex(ValueError,'arrays'):
            audit.held_proposals(snapshot,plan,prior)
        with self.assertRaisesRegex(ValueError,'membership'):
            audit.held_proposals(snapshot,plan,{'records':[]})

    def test_format_hint_never_approves_bytes_and_reported_bound_is_separate(self):
        extra={'asset_candidate_id':'SYNTHETIC-asset','reported_width':4001,'reported_height':1000,
            'reported_pixel_count':4001000}
        r=audit.asset_audit([asset()], [extra])[0]
        self.assertEqual(r['pixel_bound_state'],'REPORTED_OVER_LIMIT')
        self.assertEqual(r['format_state'],'UNSUPPORTED_CURRENT_STATIC_PNG_VALIDATOR')
        self.assertFalse(r['mime_dimensions_hash_verified'])
        self.assertFalse(r['usable_asset'])
        png=audit.asset_audit([asset(source_page_url='https://commons.wikimedia.org/wiki/File:Toy.png')],[])[0]
        self.assertEqual(png['format_state'],'PNG_NAME_HINT_ONLY_BYTES_NOT_VALIDATED')
        self.assertEqual(png['pixel_bound_state'],'UNKNOWN')

    def test_svg_and_license_metadata_cannot_override_scope(self):
        r=audit.asset_audit([asset(source_page_url='https://commons.wikimedia.org/wiki/File:Toy.svg',
            license='CC0')],[])[0]
        self.assertFalse(r['usable_asset'])
        self.assertTrue(all(v=='UNKNOWN_NOT_APPROVED_BLOCKED'
            for v in r['effective_operation_permissions'].values()))

    def test_unreviewed_grant_or_downloaded_identity_is_rejected(self):
        for changes in [{'asset_reuse_approved':'True'},{'asset_bytes_acquired':1},
                        {'downloaded_file_sha256':'a'*64},{'application_display_approved':True}]:
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                audit.asset_audit([asset(**changes)],[])

    def test_wrong_source_and_dimension_arithmetic_are_rejected(self):
        with self.assertRaises(ValueError):
            audit.asset_audit([asset(source_page_url='file:///SYNTHETIC-private')],[])
        with self.assertRaises(ValueError):
            audit.asset_audit([asset()],[{'asset_candidate_id':'SYNTHETIC-asset',
                'reported_width':10,'reported_height':20,'reported_pixel_count':1}])

    def test_pair_overlap_or_claim_promotion_does_not_create_usable_pair(self):
        for changes in [{'verified_dupe':'True'},{'usable_relation':True},
                        {'structural_overlap_score':'0'},{'sensory_similarity_percentage':'99'}]:
            with self.subTest(changes=changes),self.assertRaises(ValueError):
                audit.pair_queue([pair(**changes)])
        result=audit.pair_queue([pair()])[0]
        self.assertFalse(result['usable_pair'])
        self.assertFalse(result['canonical_relation_created'])

    def test_numeric_accounting_checks_do_not_depend_on_python_assertions(self):
        with self.assertRaisesRegex(ValueError,'cohort'):
            audit.require_equal(43,44,'SYNTHETIC count')

    def test_enrichment_index_does_not_claim_a_fresh_database_eligibility_read(self):
        row=perfume(house_id='SYNTHETIC-house')
        result=audit.enrichment_index({}, {'perfumes':[row],'review':{},'quarantined':{}})[0]
        self.assertNotIn('matching_eligible',result)
        self.assertFalse(result['matching_activation_authorized_by_this_audit'])
        self.assertIn('NOT_NEW_APPROVAL',result['review_bucket'])

    def test_outputs_outside_approved_subdirectory_are_refused_before_process(self):
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(audit.subprocess,'check_output') as command:
            with self.assertRaisesRegex(ValueError,'subdirectory'):
                audit.run(Path(folder),Path(folder)/'elsewhere')
            command.assert_not_called()

    def test_json_encoding_is_deterministic_and_keeps_unicode(self):
        self.assertEqual(audit.canonical({'b':1,'a':['SYNTHETIC','กุหลาบ']}),
            audit.canonical({'a':['SYNTHETIC','กุหลาบ'],'b':1}))
        self.assertIn('กุหลาบ',audit.canonical({'note':'กุหลาบ'}))


if __name__=='__main__':
    unittest.main()
