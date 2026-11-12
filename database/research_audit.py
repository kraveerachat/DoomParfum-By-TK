"""Offline research preparation, never an ETL/canonical/rights approval path.

Row-level artifacts are restricted to the external handoff. No network, SQL, image
acquisition, fuzzy identity merge, hold promotion or approved transformation occurs.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.parse import unquote, urlsplit

import scento_etl as etl

POLICY = 'DPT-NOTE-MEMBERSHIP-PROPOSAL-1'
INPUTS = {
    'brands': '08_OUTPUTS_APPROVED/research/brands/D1_brand_registry_reviewed_220.csv',
    'new_brands': '08_OUTPUTS_APPROVED/research/brands/D1_new_brand_candidates_6.csv',
    'conflicts': '08_OUTPUTS_APPROVED/research/brands/D1_identity_conflicts.csv',
    'brand_qa': '08_OUTPUTS_APPROVED/research/brands/D1_DELIVERY_QA.json',
    'held': '08_OUTPUTS_APPROVED/post_PR5/held_profiles/HELD_44_FORENSIC_REPORT.json',
    'assets': '08_OUTPUTS_APPROVED/bounded_temporal_capture/research/D5_COMBINED_REVIEW_CANDIDATES_15_PROPOSED.csv',
    'asset_extra': '08_OUTPUTS_APPROVED/bounded_temporal_capture/research/D5_NEW_CANDIDATES_3.json',
    'asset_manifest': '08_OUTPUTS_APPROVED/bounded_temporal_capture/research/OUTPUT_MANIFEST.json',
    'pairs': '08_OUTPUTS_APPROVED/research/relations/D7_pairwise_candidate_queue.csv',
}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require_equal(actual, expected, label):
    if actual != expected:
        raise ValueError('Unexpected research cohort/accounting: '+label)


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def safe_path(path):
    path = Path(path).absolute()
    for item in (path, *path.parents):
        if item.is_symlink() or (item.exists() and getattr(item.stat(), 'st_file_attributes', 0) & 0x400):
            raise ValueError('Linked/reparse research paths refused')
    return path.resolve()


def brand_crosswalk(seed, additions, houses):
    by_name = defaultdict(list)
    for house in houses:
        by_name[etl.normalize(house['name'])].append(house)
    rows = []
    codes = set()
    for original in [*seed, *additions]:
        code = original['candidate_code']
        if code in codes:
            raise ValueError('Duplicate research candidate code')
        codes.add(code)
        name = original.get('canonical_name', original.get('proposed_name', ''))
        aliases = [v.strip() for v in original.get('aliases', '').split(';') if v.strip()]
        labels = [('primary', name), *[('alias', v) for v in aliases]]
        suggestions = []
        for kind, label in labels:
            for house in by_name[etl.normalize(label)]:
                suggestions.append({'label_kind': kind, 'literal_label': label,
                    'house_source_id': house['id'], 'publisher_name': house['name'],
                    'canonical_brand_id_target': etl.entity_id('brand', house['id']),
                    'publisher_country_claim': house['country'], 'publisher_type_claim': house['type'],
                    'state': 'literal_candidate_only_not_identity_approval'})
        rows.append({'candidate_code': code, 'raw_candidate': dict(original), 'name': name,
            'aliases_preserved': original.get('aliases', ''),
            'parent_or_related_claim': original.get('parent_brand_candidate_code',
                original.get('parent_or_related_seed', '')),
            'parent_disposition': 'separate_claim_not_alias_or_parent_merge',
            'candidate_origin_country': original.get('origin_country',
                original.get('origin_country_claim', '')),
            'candidate_market_position': original.get('market_position',
                original.get('market_position_claim', '')),
            'candidate_catalogue_role': original.get('catalogue_role',
                original.get('proposed_catalogue_role', '')),
            'publisher_suggestions': suggestions,
            'previous_crosswalk_claim': original.get('d1_scento_house_ids', ''),
            'previous_crosswalk_kind': original.get('d1_scento_match_kind', ''),
            'identity_accepted': False, 'canonical_mutation': False,
            'normalization': 'NFKC+lower exact text only; no punctuation/diacritic/fuzzy equivalence'})
    return rows


def proposed_membership(row, note_lookup):
    """Keep every original occurrence; compute only an explicitly unapproved sidecar."""
    occurrences, memberships, repeats = [], [], []
    for layer, labels in etl.note_lists(row).items():
        grouped = defaultdict(list)
        for ordinal, label in enumerate(labels):
            matches = note_lookup.get(etl.normalize(label), [])
            if len(matches) != 1:
                raise ValueError('Unknown/ambiguous material cannot enter membership proposal')
            material = matches[0]
            occurrence = {'layer': layer, 'ordinal': ordinal, 'raw_label': label,
                'material_source_id': material, 'canonical_note_id_target': etl.entity_id('note', material)}
            occurrences.append(occurrence)
            grouped[material].append(occurrence)
        for material, values in grouped.items():
            memberships.append({'layer': layer, 'material_source_id': material,
                'canonical_note_id_target': etl.entity_id('note', material),
                'all_original_ordinals': [v['ordinal'] for v in values],
                'all_original_labels': [v['raw_label'] for v in values],
                'original_source_locator': '/notes' if layer == 'general' else '/'+layer+'_notes',
                'proposed_derived_locator': 'derived:'+POLICY+'/'+layer,
                'accepted': False})
            if len(values) > 1:
                repeats.append({'layer': layer, 'material_source_id': material,
                    'ordinals': [v['ordinal'] for v in values], 'extras': len(values)-1})
    return {'source_profile_id': row['id'], 'policy_version': POLICY, 'policy_status': 'PROPOSED_NOT_APPROVED',
        'publisher_source_url': row.get('url'), 'source_revision': etl.REV,
        'parsed_source_fields_sha256': etl.digest(row),
        'original_source_fields': {k: row[k] for k in ['top_notes','heart_notes','base_notes','notes']},
        'reported_lists': etl.note_lists(row), 'occurrences': occurrences, 'proposed_memberships': memberships,
        'repeated_groups': repeats, 'completeness': 'UNKNOWN_NO_ABSENCE_INFERENCE',
        'hold_status': 'UNCHANGED', 'canonical_writes': 0, 'matching_eligibility_change': False}


def held_proposals(snapshot, plan, prior):
    prior_rows = {r['source_id']: r for r in prior['records']}
    held = set(plan['review']) | set(plan['quarantined'])
    if held != set(prior_rows):
        raise ValueError('Held profile membership differs from preserved forensic report')
    proposals, excluded = [], []
    for ordinal, row in enumerate(snapshot['rows']['perfumes.csv'], 1):
        if row['id'] not in held:
            continue
        if etl.note_lists(row) != prior_rows[row['id']]['raw_note_lists']:
            raise ValueError('Preserved source arrays differ')
        item = proposed_membership(row, snapshot['note_lookup'])
        if item['repeated_groups']:
            item['source_data_record_ordinal'] = ordinal
            proposals.append(item)
        else:
            excluded.append({'source_profile_id': row['id'],
                'reason': 'EXTERNAL_CONFLICT_NOT_DUPLICATE_POLICY',
                'source_data_record_ordinal': ordinal, 'hold_status': 'UNCHANGED',
                'next_action': 'Permissioned independent field/section claims and explicit review required'})
    return proposals, excluded


def false_flag(value):
    return value in (False, None, '', 'False', 'false', '0', 0)


def asset_audit(candidates, extras):
    extra_by_id = {r['asset_candidate_id']: r for r in extras}
    rows, ids = [], set()
    for original in candidates:
        key = original['asset_candidate_id']
        if key in ids:
            raise ValueError('Duplicate asset candidate ID')
        ids.add(key)
        if not all(false_flag(original.get(k)) for k in
            ['asset_bytes_acquired','asset_reuse_approved','application_display_approved']):
            raise ValueError('Unexpected asset acquisition/grant outside metadata-only scope')
        if original.get('downloaded_file_sha256') or original.get('downloaded_file_path'):
            raise ValueError('Unexpected acquired file identity')
        parsed = urlsplit(original['source_page_url'])
        if parsed.scheme != 'https' or parsed.netloc != 'commons.wikimedia.org':
            raise ValueError('Unexpected source page; no implicit fetch or permission')
        title = unquote(parsed.path).rsplit('File:', 1)[-1]
        extension = Path(title).suffix.lower()
        extra = extra_by_id.get(key, {})
        width, height = extra.get('reported_width'), extra.get('reported_height')
        pixels = width*height if type(width) is int and type(height) is int else None
        reported_pixels = extra.get('reported_pixel_count')
        if reported_pixels is not None and pixels != reported_pixels:
            raise ValueError('Reported dimension arithmetic differs')
        rows.append({'asset_candidate_id': key, 'subject_note_name': original['subject_note_name'],
            'raw_candidate_metadata': dict(original), 'additional_metadata': dict(extra),
            'reported_file_title': title, 'extension_hint': extension,
            'format_state': 'PNG_NAME_HINT_ONLY_BYTES_NOT_VALIDATED' if extension=='.png'
                else 'UNSUPPORTED_CURRENT_STATIC_PNG_VALIDATOR',
            'reported_width': width, 'reported_height': height, 'reported_pixels': pixels,
            'pixel_bound_state': 'UNKNOWN' if pixels is None else
                ('REPORTED_OVER_LIMIT' if pixels > 4_000_000 else 'REPORTED_WITHIN_LIMIT_NOT_BYTE_VERIFIED'),
            'byte_identity': 'NOT_ACQUIRED_NOT_VERIFIED', 'mime_dimensions_hash_verified': False,
            'creator_ownership_verified': False,
            'immutable_revision_contents_verified_by_this_audit': False,
            'revision_state': extra.get('source_revision_fetch_status',
                'UNVERIFIED_BY_THIS_OFFLINE_AUDIT; preserve historical metadata observation'),
            'license_attribution_state': 'OBSERVED_METADATA_ONLY_NOT_CURRENT_LEGAL_OR_OWNERSHIP_VERIFICATION',
            'derivative_state': 'NO_TRANSFORMATION_AUTHORIZED; retain candidate obligations for review',
            'effective_operation_permissions': {k: 'UNKNOWN_NOT_APPROVED_BLOCKED' for k in
                ['automate','cache','store','display','transform','AI_use','commercial_use','redistribute','retain']},
            'usable_asset': False})
    if set(extra_by_id)-ids:
        raise ValueError('Unbound extra media metadata')
    return rows


def pair_queue(candidates):
    result, ids = [], set()
    for original in candidates:
        key = original['candidate_id']
        if key in ids:
            raise ValueError('Duplicate pair lead ID')
        ids.add(key)
        if not false_flag(original.get('usable_relation')) or not false_flag(original.get('verified_dupe')):
            raise ValueError('Unexpected usable-pair promotion in blocked lead queue')
        if original.get('sensory_similarity_percentage') or original.get('structural_overlap_score'):
            raise ValueError('Unreviewed numeric relation evidence')
        result.append({'candidate_id': key, 'raw_lead_metadata': dict(original),
            'evidence_state': 'PUBLISHER_LEAD_ONLY_NOT_INDEPENDENT_SENSORY_EVIDENCE',
            'rights_state': 'BLOCKED_NO_SOURCE_FIELD_USE_GRANT',
            'identity_state': 'EXACT_PERFUME_EDITION_BINDING_REQUIRES_REVIEW',
            'source_independence_group': original['publisher_group'],
            'required_steps': ['exact pair/edition review','source/field/use permission',
                'permitted independent comparison and opposition review','explicit canonical evidence review'],
            'canonical_relation_created': False, 'usable_pair': False})
    return result


def enrichment_index(snapshot, plan):
    rows = []
    for row in plan['perfumes']:
        lists = etl.note_lists(row)
        rows.append({'profile_source_id': row['id'],
            'canonical_perfume_id_target': etl.entity_id('perfume', row['id']),
            'house_source_id': row['house_id'], 'source_revision': etl.REV,
            'publisher_source_url': row.get('url'),
            'parsed_source_fields_sha256': etl.digest(row),
            'review_bucket': 'PRESERVED_HELD_SOURCE_PROFILE' if row['id'] in plan['review'] or row['id'] in plan['quarantined']
                else 'SOURCE_PROMOTABLE_UNDER_MERGED_RULES_NOT_NEW_APPROVAL',
            'source_note_representation': 'general' if set(lists)=={'general'} else 'layered',
            'reported_occurrences': sum(map(len, lists.values())),
            'completeness': 'UNKNOWN', 'matching_activation_authorized_by_this_audit': False,
            'required_enrichment': ['selected-field/domain completeness review','explicit matching eligibility',
                'permissioned observed accord/family/alias/currentness inputs if required',
                'exact per-asset use rights before image acquisition','permitted direct pairwise evidence'],
            'scope': 'PINNED_LOCAL_EXPORT_ONLY_NOT_WORLDWIDE_COVERAGE'})
    return rows


def run(bundle, output):
    code_sha = sha(Path(__file__).read_bytes())
    bundle, output = safe_path(bundle), safe_path(output)
    allowed = bundle/'08_OUTPUTS_APPROVED/post_PR4/research'
    if not output.is_relative_to(allowed) or output == allowed:
        raise ValueError('Use a fresh external research subdirectory')
    common = Path(subprocess.check_output(['git','rev-parse','--path-format=absolute','--git-common-dir'],
        cwd=Path(__file__).resolve().parents[1],timeout=10).decode().strip()).parent.resolve()
    if output.is_relative_to(common):
        raise ValueError('Row-level outputs must stay outside the public repository')
    if output.exists():
        raise ValueError('Existing research output refused')
    paths = {k: safe_path(bundle/v) for k,v in INPUTS.items()}
    initial = {k: {'path': INPUTS[k], 'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size}
        for k,p in paths.items()}
    brand_qa = json.loads(paths['brand_qa'].read_text())
    for key in ['brands','new_brands','conflicts']:
        if initial[key]['sha256'] != brand_qa['file_sha256'][paths[key].name]:
            raise ValueError('Preserved brand artifact hash mismatch')
    media_manifest = json.loads(paths['asset_manifest'].read_text())
    for key in ['assets','asset_extra']:
        if initial[key]['sha256'] != media_manifest['files'][paths[key].name]['sha256']:
            raise ValueError('Preserved media artifact hash mismatch')
    snapshot = etl.load_snapshot(bundle/'09_LOCAL_LICENSED_SOURCE/scento_pinned')
    plan = etl.build_plan(snapshot, 'full')
    seed, added, conflicts = [read_csv(paths[k]) for k in ['brands','new_brands','conflicts']]
    candidates = read_csv(paths['assets'])
    extra = json.loads(paths['asset_extra'].read_text())['new_candidates']
    prior = json.loads(paths['held'].read_text())
    brands = brand_crosswalk(seed, added, snapshot['rows']['houses.csv'])
    proposals, excluded = held_proposals(snapshot, plan, prior)
    assets = asset_audit(candidates, extra)
    pairs = pair_queue(read_csv(paths['pairs']))
    profiles = enrichment_index(snapshot, plan)
    require_equal((len(seed),len(added),len(conflicts),len(brands)),(220,6,21,226),'brands')
    require_equal((len(snapshot['rows']['houses.csv']),len(profiles)),(160,1479),'pinned cohort')
    require_equal((len(proposals),[r['source_profile_id'] for r in excluded]),
        (43,['lattafa-khamrah']),'held profiles')
    require_equal(sum(len(r['repeated_groups']) for r in proposals),44,'repeated groups')
    require_equal(sum(g['extras'] for r in proposals for g in r['repeated_groups']),45,'extra occurrences')
    require_equal((len(assets),len(pairs)),(15,5),'media/pair queues')
    require_equal(sum(r['reported_occurrences'] for r in profiles),12448,'raw selected occurrences')
    data = {'brand_review_226.json': brands, 'membership_policy_43_PROPOSED.json': proposals,
        'held_conflict_exclusion.json': excluded, 'media_review_15.json': assets,
        'pairwise_evidence_queue_5.json': pairs, 'progressive_enrichment_index_1479.json': profiles}
    metrics = {'brand_candidates': len(brands), 'publisher_houses': 160, 'preserved_identity_conflict_rows': len(conflicts),
        'primary_literal_suggestion_candidates': sum(any(s['label_kind']=='primary' for s in r['publisher_suggestions']) for r in brands),
        'alias_literal_suggestion_candidates': sum(any(s['label_kind']=='alias' for s in r['publisher_suggestions']) for r in brands),
        'no_literal_suggestion_candidates': sum(not r['publisher_suggestions'] for r in brands),
        'previous_publisher_crosswalk_claims_preserved': sum(bool(r['previous_crosswalk_claim']) for r in brands),
        'duplicate_hold_profiles': 43, 'repeated_groups': 44, 'extra_occurrences': 45, 'held_total': 44,
        'general_duplicate_profiles': sum(set(r['reported_lists'])=={'general'} for r in proposals),
        'normalization_approved': False, 'holds_resolved': 0, 'media_candidates': len(assets),
        'media_extension_hints': dict(sorted(Counter(r['extension_hint'] for r in assets).items())),
        'media_reported_dimensions_available': sum(r['reported_pixels'] is not None for r in assets),
        'media_reported_over_pixel_bound': sum(r['pixel_bound_state']=='REPORTED_OVER_LIMIT' for r in assets),
        'usable_assets': 0, 'bytes_acquired': 0, 'new_source_or_asset_grants': 0,
        'pairwise_leads': len(pairs), 'publisher_independence_groups': len(set(r['source_independence_group'] for r in pairs)),
        'usable_pairs': 0, 'indexed_source_profiles': len(profiles), 'raw_selected_note_occurrences': 12448,
        'matching_eligibility_approvals': 0, 'canonical_writes': 0, 'network_requests': 0, 'DB_calls': 0}
    summary = {'task': 'DPT-DATA-002', 'mode': 'OFFLINE_RESEARCH_AUDIT_NO_PROMOTION',
        'base_main': 'aa55f8b59acb0872b3b40273a8cdd25198f3ba27',
        'source_revision': etl.REV, 'policy_version': POLICY, 'policy_status': 'PROPOSED_NOT_APPROVED',
        'attribution': etl.ATTRIBUTION,
        'license_url': 'https://creativecommons.org/licenses/by/4.0/',
        'change_notice': 'Offline literal crosswalk and unapproved membership/enrichment projections; original arrays/labels preserved; no canonical writes.',
        'source_artifacts': snapshot['artifacts'], 'research_input_artifacts': initial, 'metrics': metrics,
        'limits': ['Deterministic canonical-ID targets from merged importer, no live DB lookup',
            'NFKC+lower literal crosswalk differs from historical accent/punctuation-stripping research normalization; neither proves identity',
            'All original candidate claims/arrays/ordinals preserved in external row-level artifacts; not public Git',
            'Media metadata only; no binary/MIME/dimension/ownership/current license/pinned-page authentication',
            'Existing observed revision-fetch failures remain unverified; this offline audit adds no live verification',
            'All matching flags/holds/rights unchanged; no global catalogue coverage claim']}
    data['AUDIT_SUMMARY.json'] = summary
    # Verify every source again before publishing any output.
    if any(sha(p.read_bytes()) != initial[k]['sha256'] for k,p in paths.items()):
        raise ValueError('Research inputs changed during audit')
    if etl.load_snapshot(bundle/'09_LOCAL_LICENSED_SOURCE/scento_pinned')['artifacts'] != snapshot['artifacts']:
        raise ValueError('Pinned source changed during audit')
    if sha(Path(__file__).read_bytes()) != code_sha:
        raise ValueError('Audit source changed during execution')
    output.mkdir(parents=True,exist_ok=False)
    for name,value in data.items():
        with (output/name).open('x',encoding='utf-8',newline='\n') as stream:
            stream.write(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    manifest = {name: {'sha256': sha((output/name).read_bytes()), 'bytes': (output/name).stat().st_size}
        for name in sorted(data)}
    (output/'OUTPUT_MANIFEST.json').write_text(json.dumps({'files': manifest,
        'source_code_sha256': code_sha,'raw_data_publication':'NONE'},
        sort_keys=True,indent=2)+'\n',encoding='utf-8',newline='\n')
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle-root',required=True)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.bundle_root,args.output)['metrics'],indent=2))


if __name__ == '__main__':
    main()
