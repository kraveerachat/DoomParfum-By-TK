"""Executable acceptance oracles for Owner-approved M1-NL-TYPED-1; synthetic only."""
from dataclasses import FrozenInstanceError, fields, replace
from decimal import Decimal
from fractions import Fraction
import hashlib
import importlib
import inspect
import unittest

from matching_math.primitives import SetInput

try:
    m = importlib.import_module('matching_math.synthetic_m1')
except ModuleNotFoundError as error:
    if error.name != 'matching_math.synthetic_m1':
        raise
    m = None


def nid(value):
    return f'20000000-0000-4000-8000-{value:012x}'


def pid(value):
    return f'10000000-0000-4000-8000-{value:012x}'


def config(**changes):
    values = dict(method_id='mc-a-notes-layered-p1', config_id='m1-nl-typed-config-1',
                  schema_id='m1-nl-typed-schema-1', layer_weights=(Fraction(1, 4), Fraction(3, 8), Fraction(3, 8)),
                  min_comparable_layers=2, note_support_budget=Fraction(1, 2), max_candidates=64,
                  max_memberships_per_profile=512, max_vocabulary_notes=512,
                  max_identifier_chars=128, max_numeric_bits=128, max_total_memberships=33280)
    values.update(changes)
    return m.M1Config(**values)


def vocabulary(count=7, **changes):
    members = frozenset(nid(i) for i in range(1, count + 1))
    values = dict(vocabulary_version='synth-notes-m1-v1',
                  vocabulary_fingerprint=hashlib.sha256('\n'.join(sorted(members)).encode('ascii')).hexdigest(),
                  domain_version='synth-pyramid-domains-m1-v1', transform_version='canonical-set-fixture-m1-v1',
                  selection_snapshot_id='synth-selection-m1-v1', scope_id='synth-scope-m1-v1', note_ids=members)
    values.update(changes)
    return m.FixtureVocabulary(**values)


def layer(numbers, domain='pyramid-domain', complete=True, **changes):
    values = dict(notes=SetInput(frozenset(nid(i) for i in numbers), complete, domain),
                  completeness_assertion_id='assertion' if complete else None,
                  selected_claim_id='claim', capture_id='capture', revision_id='revision',
                  selection_snapshot_id='synth-selection-m1-v1', scope_id='synth-scope-m1-v1')
    values.update(changes)
    return m.FixtureLayer(**values)


def profile(identity=1, top=(1, 2), heart=(4,), base=(5, 6)):
    return m.FixtureProfile(pid(identity), *(None if v is None else layer(v) for v in (top, heart, base)))


def batch(reference=None, candidates=None, *, context=None, settings=None):
    return m.score_synthetic_notes_layered(profile() if reference is None else reference,
        (profile(2, (1, 3), (4,), (6, 7)),) if candidates is None else candidates,
        vocabulary=vocabulary() if context is None else context, config=config() if settings is None else settings)


def pair(result):
    return result.groups[0].results[0] if result.groups else result.unranked[0]


class SyntheticM1Tests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(m, 'Approved synthetic M1 scorer is not implemented')

    def test_golden_rational_and_display(self):
        p = pair(batch())
        self.assertEqual((p.fit, p.scoring_coverage, p.observed_layer_support, p.structural_fit_percent_display),
                         (Fraction(7, 12), Fraction(1, 2), Fraction(1), '58.3'))
        self.assertEqual(tuple(x.jaccard for x in p.layers), (Fraction(1, 3), Fraction(1), Fraction(1, 3)))
        self.assertEqual(p.note_score_denominator, Fraction(1))

    def test_missing_top_golden(self):
        p = pair(batch(reference=replace(profile(), top=None)))
        self.assertEqual((p.fit, p.scoring_coverage, p.structural_fit_percent_display), (Fraction(2, 3), Fraction(3, 8), '66.7'))
        self.assertEqual(p.comparable_layer_mask, ('heart', 'base'))
        self.assertEqual(p.layers[0].reason, 'missing_input')

    def test_known_zero_contributes(self):
        p = pair(batch(profile(1, (), (4,), (5,)), (profile(2, (1,), (4,), (5,)),)))
        self.assertEqual((p.fit, p.scoring_coverage), (Fraction(3, 4), Fraction(1, 2)))
        self.assertEqual(p.layers[0].jaccard, Fraction(0))

    def test_incomplete_is_unknown_not_zero(self):
        r = replace(profile(1, (1,), (4,), (5,)), top=layer((1,), complete=False))
        p = pair(batch(r, (profile(2, (2,), (4,), (5,)),)))
        self.assertEqual((p.fit, p.scoring_coverage, p.structural_fit_percent_display), (Fraction(1), Fraction(3, 8), '100.0'))
        self.assertEqual(p.layers[0].reason, 'incomplete_input')
        self.assertIsNone(p.layers[0].intersection_count)

    def test_two_layer_minimum(self):
        p = pair(batch(profile(1, (1,), None, None), (profile(2, (1,), None, None),)))
        self.assertEqual((p.fit, p.scoring_coverage, p.observed_layer_support), (None, Fraction(0), Fraction(1, 4)))
        self.assertEqual(p.reason, 'insufficient_layers')
        self.assertIsNone(p.note_score_denominator)
        self.assertIsNone(p.partition_key)
        self.assertIsNone(p.structural_fit_percent_display)

    def test_complete_empty_union_unavailable(self):
        p = pair(batch(profile(1, (), (4,), (5,)), (profile(2, (), (4,), (5,)),)))
        self.assertEqual((p.fit, p.scoring_coverage), (Fraction(1), Fraction(3, 8)))
        self.assertEqual((p.layers[0].reason, p.layers[0].intersection_count, p.layers[0].union_count), ('empty_union', 0, 0))

    def test_all_known_zero_rankable(self):
        p = pair(batch(profile(1, (1,), (1,), (1,)), (profile(2, (2,), (2,), (2,)),)))
        self.assertEqual((p.fit, p.scoring_coverage, p.structural_fit_percent_display), (Fraction(0), Fraction(1, 2), '0.0'))
        self.assertIsNotNone(p.partition_key)

    def test_all_empty_is_unranked(self):
        out = batch(profile(1, (), (), ()), (profile(2, (), (), ()),))
        self.assertFalse(out.groups)
        self.assertEqual((out.unranked[0].fit, out.unranked[0].observed_layer_support), (None, Fraction(0)))

    def test_domain_mismatch_is_unknown(self):
        c = replace(profile(2, (1,), (4,), (5,)), top=layer((1,), domain='different'))
        p = pair(batch(profile(1, (1,), (4,), (5,)), (c,)))
        self.assertEqual((p.fit, p.scoring_coverage), (Fraction(1), Fraction(3, 8)))
        self.assertEqual(p.layers[0].reason, 'domain_mismatch')
        self.assertIsNone(p.layers[0].union_count)

    def test_reason_precedence(self):
        r = profile(1, (), (1,), (1,))
        bad_domain = layer((), domain='other')
        for left, right, reason in [(None, layer((), complete=False), 'missing_input'),
                                   (layer((), complete=False), bad_domain, 'incomplete_input'),
                                   (layer(()), bad_domain, 'domain_mismatch')]:
            p = pair(batch(replace(r, top=left), (replace(profile(2), top=right),)))
            self.assertEqual(p.layers[0].reason, reason)
            self.assertIsNone(p.layers[0].jaccard)
            self.assertIsNone(p.layers[0].union_count)

    def test_partitions_are_not_global_score_order(self):
        r = profile(1, (1,), (4,), (5,))
        candidates = (profile(2, None, (4,), (5,)), profile(3, (2,), (6,), None),
                      profile(4, (1,), None, (5,)), profile(5, (1,), (4,), (5,)))
        out = batch(r, candidates)
        self.assertEqual(tuple(g.key.comparable_layer_mask for g in out.groups),
                         (('top', 'heart'), ('top', 'base'), ('heart', 'base'), ('top', 'heart', 'base')))
        self.assertEqual(out.groups[0].results[0].fit, Fraction(0))

    def test_claim_identity_does_not_create_partitions(self):
        c = profile(2)
        d = replace(profile(3), top=replace(c.top, selected_claim_id='other-claim', capture_id='other-capture',
                                          revision_id='other-revision', completeness_assertion_id='other-assertion'))
        out = batch(candidates=(c, d))
        self.assertEqual(len(out.groups), 1)
        self.assertEqual(len(out.groups[0].results), 2)

    def test_candidate_permutation_and_canonical_id_ties(self):
        c, d = profile(3), profile(2)
        self.assertEqual(batch(candidates=(c, d)), batch(candidates=(d, c)))
        self.assertEqual(tuple(p.candidate_id for p in batch(candidates=(c, d)).groups[0].results), (pid(2), pid(3)))

    def test_exact_fit_sort_before_rounding(self):
        r = profile(1, range(1, 340), (341, 342), (343, 344))
        high = profile(3, range(1, 171), (341,), (343,))
        low = profile(2, range(1, 172), (341,), (343,))
        low = replace(low, top=layer(tuple(range(1, 171)) + (340,)))
        rows = batch(r, (low, high), context=vocabulary(344)).groups[0].results
        self.assertEqual(tuple(x.fit for x in rows), (Fraction(1357, 2712), Fraction(1, 2)))
        self.assertEqual(tuple(x.structural_fit_percent_display for x in rows), ('50.0', '50.0'))
        self.assertEqual(tuple(x.candidate_id for x in rows), (pid(3), pid(2)))

    def test_display_half_up_boundary(self):
        r = profile(1, range(1, 17), range(1, 17), range(1, 17))
        p = pair(batch(r, (profile(2, (1,), (1,), (1,)),), context=vocabulary(16)))
        self.assertEqual((p.fit, p.structural_fit_percent_display), (Fraction(1, 16), '6.3'))

    def test_explanation_schema_and_role_lineage(self):
        r = replace(profile(), top=replace(profile().top, selected_claim_id='left-claim'))
        p = pair(batch(r))
        self.assertEqual(tuple(x.layer for x in p.layers), ('top', 'heart', 'base'))
        self.assertEqual(p.layers[0].left.lineage.selected_claim_id, 'left-claim')
        self.assertEqual(p.layers[0].right.lineage.selected_claim_id, 'claim')
        self.assertEqual((p.confidence_state, p.pair_evidence_state),
                         ('not_evaluated_policy_pending', 'not_evaluated_synthetic_only'))
        self.assertEqual(tuple(f.name for f in fields(p)), ('method_id','config_id','schema_id','reference_id',
            'candidate_id','fit','reason','scoring_coverage','observed_layer_support','note_score_denominator',
            'comparable_layer_mask','partition_key','structural_fit_percent_display','confidence_state','pair_evidence_state','layers'))
        self.assertNotIn('members', repr(p))

    def test_output_and_inputs_are_frozen(self):
        out = batch()
        for value, field in [(out, 'reference_id'), (pair(out), 'fit'), (pair(out).layers[0], 'reason'),
                             (profile(), 'perfume_id'), (config(), 'config_id')]:
            with self.assertRaises(FrozenInstanceError):
                setattr(value, field, None)
        self.assertIs(type(out.groups), tuple)
        self.assertIs(type(pair(out).fit), Fraction)

    def test_missing_config_no_defaults(self):
        with self.assertRaises(TypeError):
            m.score_synthetic_notes_layered(profile(), (), vocabulary=vocabulary())
        for c in [None, {}, config(method_id='mc-a-full'), config(config_id='other'), config(schema_id='other')]:
            with self.assertRaises((TypeError, ValueError)):
                batch(settings=c) if c is not None else m.score_synthetic_notes_layered(profile(), (), vocabulary=vocabulary(), config=None)
        self.assertTrue(all(p.default is inspect.Parameter.empty for p in inspect.signature(m.score_synthetic_notes_layered).parameters.values()))

    def test_input_top_level_types_and_subclasses(self):
        class ProfileSubclass(m.FixtureProfile):
            pass
        class TupleSubclass(tuple):
            pass
        for reference, candidates, context, settings in [(None, (), vocabulary(), config()),
            (ProfileSubclass(pid(1), None, None, None), (), vocabulary(), config()),
            (profile(), [], vocabulary(), config()), (profile(), TupleSubclass(), vocabulary(), config()),
            (profile(), iter(()), vocabulary(), config()), (profile(), (), {}, config()),
            (profile(), (object(),), vocabulary(), config())]:
            with self.assertRaises(TypeError):
                m.score_synthetic_notes_layered(reference, candidates, vocabulary=context, config=settings)

    def test_all_candidates_validated_no_partial_output(self):
        with self.assertRaises(ValueError):
            batch(candidates=(profile(2), replace(profile(3), perfume_id='bad')))

    def test_candidate_count_limits_early(self):
        self.assertEqual(batch(candidates=()).groups, ())
        with self.assertRaisesRegex(ValueError, 'bound'):
            batch(candidates=(object(),) * 65)
        self.assertEqual(sum(len(g.results) for g in batch(candidates=tuple(profile(i) for i in range(2, 66))).groups), 64)

    def test_max_memberships_and_total_at_bound(self):
        r = profile(1, range(1, 171), range(171, 342), range(342, 513))
        candidates = tuple(replace(r, perfume_id=pid(i)) for i in range(2, 66))
        out = batch(r, candidates, context=vocabulary(512))
        self.assertEqual(len(out.groups[0].results), 64)
        self.assertTrue(all(x.fit == 1 for x in out.groups[0].results))
        self.assertEqual(config().max_total_memberships, 65 * 512)

    def test_reference_and_candidate_over_membership_bound(self):
        over = profile(1, range(1, 258), range(1, 257), None)
        for r, cs in [(over, (profile(2),)), (profile(), (replace(over, perfume_id=pid(2)),))]:
            with self.assertRaisesRegex(ValueError, 'bound'):
                batch(r, cs, context=vocabulary(257))

    def test_incomplete_preview_counts_and_cross_layer_repeats(self):
        over = replace(profile(1, range(1, 258), range(1, 257), None), top=layer(range(1, 258), complete=False))
        with self.assertRaises(ValueError):
            batch(over, (), context=vocabulary(257))

    def test_vocabulary_bounds_before_members_or_fingerprint(self):
        with self.assertRaisesRegex(ValueError, 'bound'):
            batch(context=vocabulary(513))
        self.assertFalse(batch(profile(1, (), (), ()), (), context=vocabulary(0)).groups)

    def test_vocabulary_fingerprint_and_versions(self):
        for context in [vocabulary(vocabulary_fingerprint='0' * 64), vocabulary(vocabulary_fingerprint='A' * 64),
                        vocabulary(vocabulary_version='other'), vocabulary(domain_version='other'),
                        vocabulary(transform_version='other'), vocabulary(selection_snapshot_id='other'), vocabulary(scope_id='other')]:
            with self.assertRaises(ValueError):
                batch(context=context)

    def test_canonical_uuid_identity_rules(self):
        for value in ['bad', pid(0), pid(10).upper(), nid(2), pid(2) + ' ', 2]:
            expected = TypeError if type(value) is not str else ValueError
            with self.assertRaises(expected):
                batch(candidates=(replace(profile(2), perfume_id=value),))
        with self.assertRaises(ValueError):
            batch(candidates=(profile(1),))
        with self.assertRaises(ValueError):
            batch(candidates=(profile(2), profile(2)))

    def test_invalid_note_ids_and_unlisted_notes(self):
        bad = replace(layer((1,)), notes=SetInput(frozenset({pid(1)}), True, 'pyramid-domain'))
        with self.assertRaises(ValueError):
            batch(replace(profile(), top=bad))
        with self.assertRaises(ValueError):
            batch(replace(profile(), top=layer((8,))))

    def test_token_lengths_and_ascii_content(self):
        self.assertTrue(batch(reference=replace(profile(), top=replace(layer((1,)), selected_claim_id='x' * 128))).groups)
        for value in ['', 'x' * 129, 'has space', 'ไทย', 'https://example.test', '_bad']:
            with self.assertRaises(ValueError):
                batch(reference=replace(profile(), top=replace(layer((1,)), selected_claim_id=value)))

    def test_lineage_scope_snapshot_and_assertion(self):
        for changes in [dict(scope_id='other'), dict(selection_snapshot_id='other'),
                        dict(completeness_assertion_id=None), dict(capture_id=''), dict(revision_id='')]:
            with self.assertRaises(ValueError):
                batch(reference=replace(profile(), top=replace(layer((1,)), **changes)))
        with self.assertRaises(ValueError):
            batch(reference=replace(profile(), top=layer((1,), complete=False, completeness_assertion_id='wrong')))

    def test_layer_and_set_declared_types(self):
        class LayerSubclass(m.FixtureLayer):
            pass
        values = (object(), SetInput(frozenset(), True, 'domain'),
                  LayerSubclass(SetInput(frozenset(), True, 'domain'), 'a', 'c', 'p', 'r', 'synth-selection-m1-v1', 'synth-scope-m1-v1'))
        for value in values:
            with self.assertRaises(TypeError):
                batch(reference=replace(profile(), top=value))
        malformed = SetInput(frozenset(), True, 'domain')
        object.__setattr__(malformed, 'members', [])
        with self.assertRaises(TypeError):
            batch(reference=replace(profile(), top=replace(layer(()), notes=malformed)))

    def test_malformed_set_types_revalidated(self):
        for field, value in [('complete', 1), ('domain_id', 9), ('members', frozenset({4}))]:
            malformed = SetInput(frozenset(), True, 'domain')
            object.__setattr__(malformed, field, value)
            with self.assertRaises(TypeError):
                batch(reference=replace(profile(), top=replace(layer(()), notes=malformed)))

    def test_config_types_numeric_bounds_and_values(self):
        for value in [True, 0.25, Decimal('0.25'), '1/4', float('nan'), float('inf')]:
            with self.assertRaises(TypeError):
                batch(settings=config(layer_weights=(value, Fraction(3, 8), Fraction(3, 8))))
        for value in [1 << 128, Fraction(1, 1 << 128), -1, Fraction(1, 3)]:
            with self.assertRaises(ValueError):
                batch(settings=config(layer_weights=(value, Fraction(3, 8), Fraction(3, 8))))
        with self.assertRaises(ValueError):
            batch(settings=config(layer_weights=(1 << 127, Fraction(3, 8), Fraction(3, 8))))
        for field in ['min_comparable_layers', 'max_candidates', 'max_memberships_per_profile', 'max_vocabulary_notes',
                      'max_identifier_chars', 'max_numeric_bits', 'max_total_memberships']:
            with self.assertRaises(TypeError):
                batch(settings=config(**{field: True}))
            with self.assertRaises(ValueError):
                batch(settings=config(**{field: 1 << 128}))
        with self.assertRaises(TypeError):
            batch(settings=config(layer_weights=[Fraction(1, 4), Fraction(3, 8), Fraction(3, 8)]))
        with self.assertRaises(ValueError):
            batch(settings=config(layer_weights=(Fraction(1, 4),)))
        with self.assertRaises(ValueError):
            batch(settings=config(note_support_budget=Fraction(1)))

    def test_every_config_field_required_and_no_hidden_defaults(self):
        from dataclasses import MISSING
        for record in [m.M1Config, m.FixtureVocabulary, m.FixtureProfile, m.FixtureLayer]:
            self.assertTrue(all(f.default is MISSING and f.default_factory is MISSING for f in fields(record)))
        for field, value in [('max_candidates', 63), ('max_memberships_per_profile', 511), ('max_vocabulary_notes', 511),
            ('max_identifier_chars', 127), ('max_numeric_bits', 127), ('max_total_memberships', 33279), ('min_comparable_layers', 1)]:
            with self.assertRaises(ValueError):
                batch(settings=config(**{field: value}))

    def test_errors_are_bounded_fixed_categories(self):
        marker = 'sensitive-payload-' + 'x' * 1000
        with self.assertRaises(ValueError) as caught:
            batch(reference=replace(profile(), perfume_id=marker))
        self.assertNotIn(marker, str(caught.exception))
        self.assertLessEqual(len(str(caught.exception)), 80)

    def test_empty_batch_still_validates_reference(self):
        with self.assertRaises(ValueError):
            batch(reference=replace(profile(), perfume_id='bad'), candidates=())
        out = batch(candidates=())
        self.assertEqual((out.groups, out.unranked), ((), ()))

    def test_field_construction_order_and_set_iteration(self):
        r = profile()
        alternate = m.FixtureProfile(base=r.base, heart=r.heart, top=r.top, perfume_id=r.perfume_id)
        alternate = replace(alternate, top=replace(r.top, notes=SetInput(frozenset(reversed(tuple(r.top.notes.members))), True, r.top.notes.domain_id)))
        self.assertEqual(batch(r), batch(alternate))

    def test_reference_candidate_symmetry_of_numeric_metrics(self):
        r, c = profile(), profile(2, (1, 3), (4,), (6, 7))
        a, b = pair(batch(r, (c,))), pair(batch(c, (r,)))
        self.assertEqual((a.fit, a.scoring_coverage, a.observed_layer_support), (b.fit, b.scoring_coverage, b.observed_layer_support))

    def test_unranked_candidates_order_and_conservation(self):
        out = batch(candidates=(profile(4, None, None, None), profile(3), profile(2, None, None, None)))
        self.assertEqual(tuple(p.candidate_id for p in out.unranked), (pid(2), pid(4)))
        all_ids = [p.candidate_id for g in out.groups for p in g.results] + [p.candidate_id for p in out.unranked]
        self.assertEqual(sorted(all_ids), [pid(2), pid(3), pid(4)])

    def test_exact_type_subclasses_rejected_at_each_boundary(self):
        class ConfigSubclass(m.M1Config):
            pass
        class VocabularySubclass(m.FixtureVocabulary):
            pass
        class StringSubclass(str):
            pass
        class IntSubclass(int):
            pass
        class FractionSubclass(Fraction):
            pass
        class FrozenSetSubclass(frozenset):
            pass
        c, v = config(), vocabulary()
        for settings, context, reference in [
            (ConfigSubclass(**{f.name: getattr(c, f.name) for f in fields(c)}), v, profile()),
            (c, VocabularySubclass(**{f.name: getattr(v, f.name) for f in fields(v)}), profile()),
            (config(max_candidates=IntSubclass(64)), v, profile()),
            (config(note_support_budget=FractionSubclass(1, 2)), v, profile()),
            (c, replace(v, note_ids=FrozenSetSubclass(v.note_ids)), profile()),
            (c, v, replace(profile(), perfume_id=StringSubclass(pid(1))))]:
            with self.assertRaises(TypeError):
                m.score_synthetic_notes_layered(reference, (), vocabulary=context, config=settings)

    def test_missing_declared_fields_are_bounded_shape_errors(self):
        for broken in [object.__new__(m.FixtureProfile), object.__new__(m.FixtureLayer),
                       object.__new__(m.FixtureVocabulary), object.__new__(m.M1Config),
                       object.__new__(SetInput)]:
            arguments = dict(reference=profile(), candidates=(), vocabulary=vocabulary(), config=config())
            if type(broken) is m.FixtureProfile:
                arguments['reference'] = broken
            elif type(broken) is m.FixtureVocabulary:
                arguments['vocabulary'] = broken
            elif type(broken) is m.M1Config:
                arguments['config'] = broken
            else:
                arguments['reference'] = replace(profile(), top=broken if type(broken) is m.FixtureLayer else replace(layer(()), notes=broken))
            with self.assertRaisesRegex(ValueError, 'shape'):
                m.score_synthetic_notes_layered(**arguments)

    def test_no_set_comparison_before_complete_validation(self):
        from unittest.mock import patch
        with patch.object(m, 'set_jaccard', side_effect=AssertionError('scoring started before validation')):
            with self.assertRaises(ValueError):
                batch(candidates=(profile(2), replace(profile(3), top=replace(layer((1,)), capture_id='bad value'))))
            with self.assertRaises(ValueError):
                batch(candidates=(profile(2),) * 65)

    def test_output_record_field_sets_are_exact(self):
        expected = {
            m.M1BatchResult: ('method_id','config_id','schema_id','reference_id','vocabulary_version','vocabulary_fingerprint','domain_version','transform_version','selection_snapshot_id','scope_id','groups','unranked'),
            m.LayerDomain: ('layer','domain_id'),
            m.PartitionKey: ('method_id','config_id','schema_id','component_mask','comparable_layer_mask','vocabulary_version','vocabulary_fingerprint','domain_version','transform_version','selection_snapshot_id','scope_id','layer_domains'),
            m.PartitionResult: ('key','results'),
            m.FixtureLineage: ('completeness_assertion_id','selected_claim_id','capture_id','revision_id','selection_snapshot_id','scope_id'),
            m.LayerSide: ('state','declared_complete','domain_id','lineage'),
            m.LayerExplanation: ('layer','left','right','reason','jaccard','intersection_count','union_count','original_weight')}
        for record, names in expected.items():
            self.assertEqual(tuple(f.name for f in fields(record)), names)
        p = pair(batch())
        self.assertEqual(p.partition_key.component_mask, ('notes',))
        self.assertEqual(tuple(d.layer for d in p.partition_key.layer_domains), ('top','heart','base'))
        self.assertNotIn('20000000-', repr(p))

    def test_missing_incomplete_complete_sides_are_explicit(self):
        r = replace(profile(), top=None, heart=layer((4,), complete=False))
        p = pair(batch(r))
        self.assertEqual((p.layers[0].left.state, p.layers[0].left.declared_complete,
                          p.layers[0].left.domain_id, p.layers[0].left.lineage), ('missing',None,None,None))
        self.assertEqual((p.layers[1].left.state, p.layers[1].left.declared_complete,
                          p.layers[1].left.lineage.completeness_assertion_id), ('incomplete',False,None))
        self.assertEqual((p.layers[2].left.state, p.layers[2].left.declared_complete), ('complete',True))

    def test_domain_ids_remain_part_of_partition_identity(self):
        r = replace(profile(), top=layer((1,2), domain='top-domain'), heart=layer((4,), domain='heart-domain'))
        c = replace(profile(2), top=layer((1,2), domain='top-domain'), heart=layer((4,), domain='heart-domain'))
        p = pair(batch(r, (c,)))
        self.assertEqual(tuple((d.layer,d.domain_id) for d in p.partition_key.layer_domains),
                         (('top','top-domain'),('heart','heart-domain'),('base','pyramid-domain')))


if __name__ == '__main__':
    unittest.main()
