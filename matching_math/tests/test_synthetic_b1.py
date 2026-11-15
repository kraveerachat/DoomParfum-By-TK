"""Owner-frozen B1 contract examples and adversarial typed-boundary tests.

All IDs and declarations here are synthetic. Expected fractions are manual
contract examples, not a duplicate scoring implementation.
"""
import dataclasses as dc
import hashlib
import inspect
from fractions import Fraction as F
import unittest

from matching_math import synthetic_b1 as b
from matching_math.primitives import SetInput


def note(i):
    return f"20000000-0000-4000-8000-{i:012x}"


def perfume(i):
    return f"10000000-0000-4000-8000-{i:012x}"


LAYERS = ("top", "heart", "base")
DOMAINS = tuple(b.B1LayerDomain(x, f"synth-{x}-b1-v1") for x in LAYERS)


def vocabulary(size=5):
    ids = frozenset(note(i) for i in range(1, size + 1))
    digest = hashlib.sha256("\n".join(sorted(ids)).encode("ascii")).hexdigest()
    return b.B1Vocabulary("synth-notes-b1-v1", digest, "synth-pyramid-domains-b1-v1",
                          "canonical-set-fixture-b1-v1", "canonical-id-only-b1-v1",
                          "canonical-clause-set-b1-v1", "synth-selection-b1-v1",
                          "synth-scope-b1-v1", DOMAINS, ids)


def config():
    return b.B1Config("mc-b1-pyramid-positive-domain-p1", "b1-pd-typed-config-1",
                      "b1-pd-typed-schema-1", "required-all-optional-soft-b1-v1",
                      "pyramid-exact-any-b1-v1", "positive-int-1-5-excluded-none-b1-v1",
                      "synthetic-closed-domains-b1-v1", "one-to-one-top-heart-base-b1-v1",
                      "positive-layers-only-b1-v1", 1, (F(4, 5), F(1, 5)),
                      30, 30, 64, 512, 512, 1, 5, 128, 128, 32768)


def clause(i=1, selector="top", role="optional", weight=1):
    return b.B1Clause(note(i), selector, role, weight)


def layer(ids=(), name="top", complete=True, domain=None):
    return b.B1Layer(SetInput(frozenset(note(i) for i in ids), complete,
                             domain or f"synth-{name}-b1-v1"),
                     "assertion-1" if complete else None, "claim-1", "capture-1",
                     "revision-1", "synth-selection-b1-v1", "synth-scope-b1-v1")


def profile(i=1, top=None, heart=None, base=None):
    return b.B1Profile(perfume(i), top, heart, base)


def run(clauses=(None,), candidates=(), **kwargs):
    if clauses == (None,):
        clauses = (clause(),)
    return b.score_synthetic_b1(b.B1Query(clauses), candidates,
                               vocabulary=kwargs.pop("vocabulary", vocabulary()),
                               config=kwargs.pop("config", config()), **kwargs)


def one(clauses, p, **kwargs):
    batch = run(clauses, (p,), **kwargs)
    return (batch.groups[0].results if batch.groups else batch.unranked)[0]


def forged(cls, **attrs):
    value = object.__new__(cls)
    for name, item in attrs.items():
        object.__setattr__(value, name, item)
    return value


class B1Goldens(unittest.TestCase):
    def assert_metrics(self, result, q, h, fit, display):
        self.assertEqual((result.query_coverage, result.focus, result.fit,
                          result.query_fit_percent_display), (q, h, fit, display))
        self.assertEqual(result.confidence_state, "not_evaluated_policy_pending")
        self.assertEqual(result.pair_evidence_state, "not_evaluated_synthetic_only")

    def test_mc_b01(self):
        r = one((clause(role="required"), clause(2)), profile(top=layer((1, 2, 3, 4))))
        self.assert_metrics(r, F(1), F(1, 2), F(9, 10), "90.0")

    def test_mc_b02(self):
        self.assert_metrics(one((clause(), clause(2)), profile(top=layer((1, 3)))),
                            F(1, 2), F(1, 2), F(1, 2), "50.0")

    def test_mc_b03(self):
        r = one((clause(role="required", weight=2), clause(2, "heart")),
                profile(top=layer((1, 3)), heart=layer((5,), "heart")))
        self.assert_metrics(r, F(2, 3), F(1, 3), F(3, 5), "60.0")
        self.assertEqual(r.query_weight_denominator, 3)

    def test_mc_b04(self):
        r = one((clause(selector="any_pyramid"),), profile(top=layer((1,)),
                heart=layer((), "heart"), base=layer((1,), "base")))
        self.assert_metrics(r, F(1), F(1, 2), F(9, 10), "90.0")
        self.assertEqual(r.clauses[0].witness, b.B1Occurrence(note(1), "top"))

    def test_mc_b05(self):
        r = one((clause(role="required"),), profile(top=layer(), base=layer((1,), "base")))
        self.assertEqual(r.reason, "rejected_missing_required")
        self.assert_metrics(r, F(0), F(0), None, None)
        self.assertEqual(r.positive_domain_size, 0)

    def test_mc_b06(self):
        r = one((clause(role="required"),), profile(top=layer((1,), complete=False)))
        self.assertEqual(r.reason, "unverified_required_domain")
        self.assert_metrics(r, None, None, None, None)
        self.assertIsNone(r.clauses[0].witness)

    def test_mc_b07_b08_b13(self):
        for excluded_note, base_members in ((1, ()), (2, (3,))):
            with self.subTest(excluded_note=excluded_note):
                cs = (clause(role="required"), clause(excluded_note, "base", "excluded", None))
                r = one(cs, profile(top=layer((1,)), base=layer(base_members, "base")))
                self.assert_metrics(r, F(1), F(1), F(1), "100.0")
                self.assertEqual(r.positive_layer_mask, ("top",))
                self.assertEqual(r.strict_layer_mask, ("top", "base"))
        r = one((clause(2, role="required"), clause(1, "any_pyramid", "excluded", None)),
                profile(top=layer((2,)), base=layer((), "base")))
        self.assertEqual(r.reason, "unverified_exclusion_domain")

    def test_mc_b09_conflicts_and_alias(self):
        for cs in ((clause(), clause(selector="any_pyramid")),
                   (clause(), clause(weight=2)), (clause(), clause(role="required")),
                   (clause(), clause(role="excluded", weight=None))):
            with self.subTest(cs=cs), self.assertRaisesRegex(ValueError, "^Invalid query$"):
                run(cs)
        with self.assertRaisesRegex(ValueError, "^Invalid identifier$"):
            run((dc.replace(clause(), note_id="ambiguous-rose"),))

    def test_mc_b10_empty_and_zero(self):
        for cs in ((), (clause(role="excluded", weight=None),), (clause(weight=0),),
                   (clause(weight=0), clause(2, weight=0))):
            with self.subTest(cs=cs), self.assertRaisesRegex(ValueError, "^Invalid empty positive query$"):
                run(cs)
        with self.assertRaisesRegex(ValueError, "^Invalid query$"):
            run((clause(weight=0), clause(2)))

    def test_mc_b11_and_x09(self):
        cs = (clause(), clause(), clause(2, "base", "excluded", None),
              clause(2, "base", "excluded", None))
        batch = run(cs, (profile(top=layer((1,)), base=layer((), "base")),))
        self.assertEqual((batch.raw_clause_count, batch.normalized_clause_count,
                          batch.positive_clause_count, batch.query_weight_denominator), (4, 2, 1, 1))
        self.assertEqual(batch.groups[0].results[0].fit, F(1))
        self.assertIsNone(batch.query_key.clauses[1].weight)

    def test_mc_b12(self):
        cs = (clause(role="required"), clause(1, "base"))
        p = profile(top=layer((1,)), base=layer((), "base"))
        self.assert_metrics(one(cs, p), F(1, 2), F(1), F(3, 5), "60.0")
        self.assertEqual(one(cs, p).unique_positive_note_count, 1)
        r = one((cs[0], dc.replace(cs[1], role="required")), p)
        self.assertEqual(r.reason, "rejected_missing_required")
        self.assertIsNone(r.fit)

    def test_mc_b14(self):
        r = one((clause(),), profile(top=layer()))
        self.assertEqual(r.reason, "rejected_no_positive_match")
        self.assert_metrics(r, F(0), F(0), None, None)

    def test_mc_b15_flat_unsupported(self):
        with self.assertRaisesRegex(ValueError, "^Unsupported configuration$"):
            run(config=dc.replace(config(), method_id="mc-b1-flat-positive-domain-p1"))
        for selector in ("general", "flat", "middle", "any_flat"):
            with self.subTest(selector=selector), self.assertRaisesRegex(ValueError, "^Invalid query$"):
                run((clause(selector=selector),))

    def test_x01_domain_mismatch_precedes_incomplete(self):
        for complete in (True, False):
            r = one((clause(),), profile(top=layer((1,), complete=complete, domain="other-domain")))
            self.assertEqual(r.reason, "unverified_positive_domain")
            self.assert_metrics(r, None, None, None, None)
            self.assertEqual(r.layers[0].state, "domain_mismatch")
            self.assertFalse(r.layers[0].domain_compatible)

    def test_x02_any_requires_all_three(self):
        r = one((clause(selector="any_pyramid"),),
                profile(top=layer((1,)), heart=layer((), "heart")))
        self.assertEqual(r.reason, "unverified_positive_domain")
        self.assertEqual(r.clauses[0].unverified_domains, ("base",))
        self.assertIsNone(r.clauses[0].witness)

    def test_x03_x04_x05(self):
        cs = (clause(role="required"), clause(2, "base", "excluded", None))
        for tops, bases, reason, diagnostic in (((), (2,), "rejected_excluded", F(0)),
                ((1,), (2,), "rejected_excluded", F(1)),
                ((1,), (), "unverified_exclusion_domain", F(1))):
            with self.subTest(tops=tops, bases=bases):
                r = one(cs, profile(top=layer(tops), base=layer(bases, "base", False)))
                self.assertEqual(r.reason, reason)
                self.assert_metrics(r, diagnostic, diagnostic, None, None)
                self.assertEqual(r.clauses[1].unverified_domains, ("base",))
                self.assertEqual(r.clauses[1].state, "excluded_present" if bases else "unverified")

    def test_x06_known_subset(self):
        r = one((clause(), clause(2, "base")), profile(top=layer((1,))))
        self.assertEqual(r.gates.positive_minimum, "passed")
        self.assertEqual(r.reason, "unverified_positive_domain")
        self.assert_metrics(r, None, None, None, None)
        self.assertIsNone(r.positive_domain_size)
        self.assertEqual((r.verified_matched_weight, r.verified_matched_positive_count), (1, 1))

    def test_x07_empty_candidates_still_validate(self):
        batch = run()
        self.assertEqual((batch.groups, batch.unranked), ((), ()))
        with self.assertRaisesRegex(ValueError, "^Invalid empty positive query$"):
            run(())

    def test_x08_distinct_layer_witnesses(self):
        r = one((clause(role="required"), clause(selector="base", role="required")),
                profile(top=layer((1,)), base=layer((1,), "base")))
        self.assertEqual((r.verified_matched_occurrence_count, r.unique_positive_note_count), (2, 1))
        self.assertEqual(tuple(e.witness.layer for e in r.clauses), ("top", "base"))
        self.assert_metrics(r, F(1), F(1), F(1), "100.0")

    def test_x10_sort_exact_and_ids(self):
        ps = tuple(profile(i, top=layer((1,))) for i in (3, 1, 2))
        self.assertEqual(tuple(r.candidate_id for r in run(candidates=ps).groups[0].results),
                         tuple(perfume(i) for i in (1, 2, 3)))
        cs = (clause(), clause(512))
        ps = (profile(1, top=layer(range(1, 502))), profile(2, top=layer(range(1, 501))))
        rs = run(cs, ps, vocabulary=vocabulary(512)).groups[0].results
        self.assertEqual(tuple(r.candidate_id for r in rs), (perfume(2), perfume(1)))
        self.assertEqual(tuple(r.fit for r in rs), (F(1001, 2500), F(1003, 2505)))
        self.assertEqual(tuple(r.query_fit_percent_display for r in rs), ("40.0", "40.0"))

    def test_half_up_display_reachable(self):
        # Sixteen query notes; one matched among sixteen declared memberships.
        cs = tuple(clause(i) for i in range(1, 17))
        r = one(cs, profile(top=layer((1,) + tuple(range(17, 32)))), vocabulary=vocabulary(31))
        self.assertEqual((r.fit, r.query_fit_percent_display), (F(1, 16), "6.3"))

    def test_excluded_incompatible_preview_is_not_witness(self):
        r = one((clause(), clause(2, "base", "excluded", None)),
                profile(top=layer((1,)), base=layer((2,), "base", False, "other")))
        self.assertEqual(r.reason, "unverified_exclusion_domain")
        self.assertIsNone(r.clauses[1].witness)

    def test_reason_precedence_and_all_explanations(self):
        cs = (clause(role="required"), clause(2, "base", "required"),
              clause(3, "heart", "excluded", None))
        p = profile(top=layer(), heart=layer((3,), "heart", False))
        r = one(cs, p)
        self.assertEqual(r.reason, "rejected_excluded")
        self.assertEqual(tuple(e.state for e in r.clauses), ("unmatched", "unverified", "excluded_present"))
        self.assertEqual(r.gates.required, "failed")
        r = one(cs[:-1], p)
        self.assertEqual(r.reason, "rejected_missing_required")


class B1Validation(unittest.TestCase):
    def check_error(self, exception, message, **kwargs):
        with self.assertRaisesRegex(exception, "^" + message + "$\n?"):
            run(**kwargs)

    def test_all_config_fields_required_and_fixed(self):
        for field in dc.fields(config()):
            with self.subTest(field=field.name):
                self.assertIs(field.default, dc.MISSING)
                value = getattr(config(), field.name)
                changed = "different" if type(value) is str else ((F(1, 2), F(1, 2)) if type(value) is tuple else value + 1)
                self.check_error(ValueError, "Unsupported configuration", config=dc.replace(config(), **{field.name: changed}))

    def test_numeric_types_and_bits(self):
        for value in (True, 1.0, "1", F(1)):
            with self.subTest(value=value):
                self.check_error(TypeError, "Invalid typed input", config=dc.replace(config(), max_candidates=value))
        for value in (True, 1.0, "1", F(1)):
            with self.subTest(weight=value):
                self.check_error(TypeError, "Invalid typed input", clauses=(clause(weight=value),))
        for value in (1 << 128, -(1 << 128)):
            self.check_error(ValueError, "Input bound exceeded", clauses=(clause(weight=value),))
        self.check_error(ValueError, "Invalid query", clauses=(clause(weight=(1 << 127)),))
        self.check_error(ValueError, "Input bound exceeded", config=dc.replace(config(), max_candidates=1 << 128))
        for value in (True, 0.8, "4/5"):
            self.check_error(TypeError, "Invalid typed input", config=dc.replace(config(), formula_weights=(value, F(1, 5))))
        self.check_error(ValueError, "Input bound exceeded", config=dc.replace(config(), formula_weights=(F(1 << 128), F(1, 5))))
        for numerator, denominator, error, message in ((True, 5, TypeError, "Invalid typed input"),
                (4, True, TypeError, "Invalid typed input"), (4, 0, ValueError, "Unsupported configuration"),
                (4, -5, ValueError, "Unsupported configuration"), (4, 1 << 128, ValueError, "Input bound exceeded")):
            malformed = forged(F, _numerator=numerator, _denominator=denominator)
            self.check_error(error, message, config=dc.replace(config(), formula_weights=(malformed, F(1, 5))))

    def test_weight_rules(self):
        for value in (-1, 6):
            self.check_error(ValueError, "Invalid query", clauses=(clause(weight=value),))
        self.check_error(TypeError, "Invalid typed input", clauses=(clause(weight=None),))
        for value in (0, 1):
            self.check_error(ValueError, "Invalid query", clauses=(clause(), clause(2, "base", "excluded", value)))
        self.check_error(TypeError, "Invalid typed input", clauses=(clause(), clause(2, "base", "excluded", False)))
        self.check_error(ValueError, "Invalid query", clauses=(clause(role="unknown"),))

    def test_raw_bounds_before_dedup_and_scan(self):
        self.assertEqual(run((clause(),) * 30).normalized_clause_count, 1)
        self.check_error(ValueError, "Input bound exceeded", clauses=(clause(),) * 31)
        self.check_error(ValueError, "Input bound exceeded", clauses=(object(),) * 31,
                         config=dc.replace(config(), method_id="bad"))
        self.check_error(ValueError, "Input bound exceeded", candidates=(object(),) * 65)
        batch = run(tuple(clause(i) for i in range(1, 31)), vocabulary=vocabulary(30))
        self.assertEqual(batch.normalized_clause_count, 30)

    def test_candidates_and_total_reachable_max(self):
        ps = tuple(profile(i, top=layer(range(1, 513))) for i in range(1, 65))
        batch = run(candidates=ps, vocabulary=vocabulary(512))
        self.assertEqual(len(batch.groups[0].results), 64)
        self.assertEqual(sum(r.positive_domain_size for r in batch.groups[0].results), 32768)
        # 64*512 is the total bound; no independently reachable excess exists.
        for complete in (True, False):
            p = profile(top=layer((1,)), base=layer(range(1, 513), "base", complete))
            self.check_error(ValueError, "Input bound exceeded", candidates=(p,), vocabulary=vocabulary(512))

    def test_vocabulary_and_token_limits(self):
        self.check_error(ValueError, "Input bound exceeded", vocabulary=vocabulary(513))
        self.check_error(ValueError, "Input bound exceeded", vocabulary=dc.replace(vocabulary(),
                         note_ids=frozenset(str(i) for i in range(513))))
        p = profile(top=dc.replace(layer((1,)), capture_id="a" * 128))
        self.assertEqual(one((clause(),), p).fit, F(1))
        for token in ("a" * 129, "é" * 129):
            self.check_error(ValueError, "Input bound exceeded", candidates=(profile(top=dc.replace(layer(), capture_id=token)),))
        for token in ("", " spaces", "a b", "é", "a/", "_bad"):
            self.check_error(ValueError, "Invalid identifier", candidates=(profile(top=dc.replace(layer(), capture_id=token)),))
        self.check_error(ValueError, "Input bound exceeded", clauses=(dc.replace(clause(), note_id="x" * 129),))

    def test_unknown_notes_and_fingerprint(self):
        self.check_error(ValueError, "Invalid fixture vocabulary", clauses=(clause(6),))
        self.check_error(ValueError, "Invalid fixture vocabulary", candidates=(profile(base=layer((6,), "base")),))
        self.check_error(ValueError, "Invalid fixture vocabulary", vocabulary=dc.replace(vocabulary(), vocabulary_fingerprint="0" * 64))
        self.check_error(ValueError, "Invalid identifier", vocabulary=dc.replace(vocabulary(), vocabulary_fingerprint="A" * 64))
        self.check_error(ValueError, "Invalid fixture vocabulary", vocabulary=vocabulary(0))

    def test_fixed_context_fields_and_domain_table(self):
        for f in dc.fields(vocabulary()):
            if f.name in ("note_ids", "vocabulary_fingerprint"):
                continue
            value = getattr(vocabulary(), f.name)
            replacement = tuple(reversed(value)) if type(value) is tuple else "different"
            with self.subTest(field=f.name):
                self.check_error(ValueError, "Unsupported fixture context", vocabulary=dc.replace(vocabulary(), **{f.name: replacement}))

    def test_lineage_fields_all_layers(self):
        for name in LAYERS:
            for field in ("selection_snapshot_id", "scope_id"):
                p = profile(**{name: dc.replace(layer(name=name), **{field: "other"})})
                self.check_error(ValueError, "Invalid fixture lineage", candidates=(p,))
            for complete, assertion in ((True, None), (False, "assertion")):
                p = profile(**{name: dc.replace(layer(name=name, complete=complete), completeness_assertion_id=assertion)})
                self.check_error(ValueError, "Invalid fixture lineage", candidates=(p,))

    def test_identifiers_and_duplicate_candidates(self):
        for value in (perfume(0), perfume(10).upper(), note(1), "not-a-uuid"):
            self.check_error(ValueError, "Invalid identifier", candidates=(profile(i=1).__class__(value, None, None, None),))
        self.check_error(ValueError, "Invalid identifier", candidates=(profile(), profile()))
        for value in (note(0), perfume(1), "rose", "20000000-0000-4000-8000-00000000000A"):
            self.check_error(ValueError, "Invalid identifier", clauses=(dc.replace(clause(), note_id=value),))

    def test_types_subclasses_containers(self):
        class QuerySubclass(b.B1Query):
            pass
        values = (([], (), vocabulary(), config()), (QuerySubclass((clause(),)), (), vocabulary(), config()),
                  (b.B1Query([clause()]), (), vocabulary(), config()),
                  (b.B1Query((clause(),)), [], vocabulary(), config()),
                  (b.B1Query((clause(),)), (), {}, config()),
                  (b.B1Query((clause(),)), (), vocabulary(), {}))
        for q, ps, v, c in values:
            with self.subTest(qtype=type(q), ptype=type(ps)), self.assertRaisesRegex(TypeError, "^Invalid typed input$"):
                b.score_synthetic_b1(q, ps, vocabulary=v, config=c)
        self.check_error(TypeError, "Invalid typed input", candidates=(object(),))
        self.check_error(TypeError, "Invalid typed input", candidates=(profile(top=object()),))
        self.check_error(TypeError, "Invalid typed input", candidates=(profile(top=dc.replace(layer(), notes=object())),))
        for attrs in ({"members": []}, {"complete": 1}, {"domain_id": 1}, {"members": frozenset({1})}):
            original = layer().notes
            fake = forged(SetInput, **{f.name: attrs.get(f.name, getattr(original, f.name)) for f in dc.fields(original)})
            self.check_error(TypeError, "Invalid typed input", candidates=(profile(top=dc.replace(layer(), notes=fake)),))

    def test_every_required_input_field_and_forged_missing(self):
        samples = (b.B1Query((clause(),)), clause(), profile(), layer(), DOMAINS[0], vocabulary(), config())
        for sample in samples:
            for field in dc.fields(sample):
                with self.subTest(cls=type(sample).__name__, field=field.name):
                    self.assertIs(field.default, dc.MISSING)
                    fake = forged(type(sample), **{f.name: getattr(sample, f.name) for f in dc.fields(sample) if f.name != field.name})
                    if type(sample) is b.B1Query:
                        args = (fake, (), vocabulary(), config())
                    elif type(sample) is b.B1Clause:
                        args = (b.B1Query((fake,)), (), vocabulary(), config())
                    elif type(sample) is b.B1Profile:
                        args = (b.B1Query((clause(),)), (fake,), vocabulary(), config())
                    elif type(sample) is b.B1Layer:
                        args = (b.B1Query((clause(),)), (profile(top=fake),), vocabulary(), config())
                    elif type(sample) is b.B1LayerDomain:
                        args = (b.B1Query((clause(),)), (), dc.replace(vocabulary(), layer_domains=(fake,) + DOMAINS[1:]), config())
                    elif type(sample) is b.B1Vocabulary:
                        args = (b.B1Query((clause(),)), (), fake, config())
                    else:
                        args = (b.B1Query((clause(),)), (), vocabulary(), fake)
                    with self.assertRaisesRegex(ValueError, "^Invalid typed input shape$"):
                        b.score_synthetic_b1(args[0], args[1], vocabulary=args[2], config=args[3])
        self.check_error(ValueError, "Invalid typed input shape", candidates=(profile(top=dc.replace(layer(), notes=forged(SetInput))),))

    def test_validation_precedence_and_last_candidate(self):
        self.check_error(TypeError, "Invalid typed input", clauses=(clause(),) * 31, vocabulary={})
        self.check_error(ValueError, "Unsupported configuration", clauses=(clause(999),), config=dc.replace(config(), config_id="bad"))
        self.check_error(ValueError, "Input bound exceeded", clauses=(clause(selector="bad"),), candidates=(profile(top=dc.replace(layer(), capture_id="x" * 129)),))
        self.check_error(ValueError, "Invalid fixture lineage", candidates=(profile(1, top=layer((1,))),
                         profile(2, base=dc.replace(layer(name="base"), scope_id="other"))))

    def test_signature_no_defaults(self):
        sig = inspect.signature(b.score_synthetic_b1)
        self.assertEqual(tuple(sig.parameters), ("query", "candidates", "vocabulary", "config"))
        self.assertTrue(all(p.default is inspect.Parameter.empty for p in sig.parameters.values()))

    def test_exact_all_declared_schema_fields(self):
        schemas = {
            "B1Query": "clauses",
            "B1Clause": "note_id selector role weight",
            "B1Profile": "perfume_id top heart base",
            "B1Layer": "notes completeness_assertion_id selected_claim_id capture_id revision_id selection_snapshot_id scope_id",
            "B1LayerDomain": "layer domain_id",
            "B1Vocabulary": "vocabulary_version vocabulary_fingerprint domain_version transform_version alias_version normalization_version selection_snapshot_id scope_id layer_domains note_ids",
            "B1Config": "method_id config_id schema_id role_policy_id selector_policy_id clause_weight_policy_id closure_policy_id assignment_policy_id focus_domain_policy_id positive_minimum formula_weights max_raw_clauses max_normalized_clauses max_candidates max_memberships_per_candidate max_vocabulary_notes min_positive_weight max_positive_weight max_identifier_chars max_numeric_bits max_total_memberships",
            "B1ContextKey": "vocabulary_version vocabulary_fingerprint domain_version transform_version alias_version normalization_version selection_snapshot_id scope_id layer_domains",
            "B1QueryKey": "config context clauses",
            "B1Lineage": "completeness_assertion_id selected_claim_id capture_id revision_id selection_snapshot_id scope_id",
            "B1LayerStatus": "layer state declared_complete domain_compatible domain_id lineage",
            "B1Occurrence": "note_id layer",
            "B1ClauseEvaluation": "clause domain_layers state witness unverified_domains",
            "B1GateSummary": "required excluded positive_domain positive_minimum",
            "B1PartitionKey": "query_key positive_layer_mask strict_layer_mask relevant_layer_mask layer_domains",
            "B1CandidateResult": "method_id config_id schema_id candidate_id query_key reason fit query_coverage focus query_weight_denominator verified_matched_weight verified_matched_positive_count verified_matched_occurrence_count positive_domain_size positive_layer_mask strict_layer_mask relevant_layer_mask closure_mask unique_positive_note_count gates clauses layers partition_key query_fit_percent_display confidence_state pair_evidence_state",
            "B1PartitionResult": "key results",
            "B1BatchResult": "method_id config_id schema_id query_key raw_clause_count normalized_clause_count positive_clause_count query_weight_denominator unique_positive_note_count positive_layer_mask strict_layer_mask relevant_layer_mask groups unranked",
        }
        for name, names in schemas.items():
            cls = getattr(b, name)
            with self.subTest(record=name):
                self.assertEqual(tuple(f.name for f in dc.fields(cls)), tuple(names.split()))
                self.assertTrue(cls.__dataclass_params__.frozen)
                self.assertTrue(all(f.default is dc.MISSING and f.default_factory is dc.MISSING for f in dc.fields(cls)))

    def test_forged_extra_payload_not_retained(self):
        c, v, term = config(), vocabulary(), clause()
        v = dc.replace(v, layer_domains=tuple(dc.replace(d) for d in v.layer_domains))
        for value in (c, v, term, v.layer_domains[0]):
            object.__setattr__(value, "private_extra_payload", {"secret": "synthetic-do-not-copy"})
        result = b.score_synthetic_b1(b.B1Query((term,)), (profile(top=layer((1,))),), vocabulary=v, config=c)
        def visit(value):
            if dc.is_dataclass(value):
                self.assertEqual(set(vars(value)), {f.name for f in dc.fields(value)})
                for f in dc.fields(value):
                    visit(getattr(value, f.name))
            elif type(value) is tuple:
                for item in value:
                    visit(item)
        visit(result)

    def test_precedence_stages_before_fingerprint_or_dedup(self):
        self.check_error(ValueError, "Input bound exceeded", clauses=(object(),) * 31, config=forged(b.B1Config))
        self.check_error(ValueError, "Input bound exceeded", candidates=(object(),) * 65, vocabulary=forged(b.B1Vocabulary))
        self.check_error(ValueError, "Invalid identifier", candidates=(dc.replace(profile(), perfume_id="malformed"),),
                         vocabulary=dc.replace(vocabulary(), vocabulary_version="different"))
        self.check_error(ValueError, "Invalid identifier", clauses=(dc.replace(clause(), note_id="rose"),),
                         vocabulary=dc.replace(vocabulary(), vocabulary_fingerprint="0" * 64))
        self.check_error(ValueError, "Invalid fixture vocabulary", clauses=(clause(99),), candidates=(profile(), profile()))

    def test_512_membership_cap_across_layers_and_extreme_uuid(self):
        p = profile(top=layer(range(1, 171)), heart=layer(range(171, 342), "heart"), base=layer(range(342, 513), "base"))
        r = one((clause(selector="any_pyramid"),), p, vocabulary=vocabulary(512))
        self.assertEqual(r.positive_domain_size, 512)
        self.assertEqual(r.focus, F(1, 512))
        huge_note = note((1 << 48) - 1)
        v = dc.replace(vocabulary(1), note_ids=frozenset({huge_note}),
                       vocabulary_fingerprint=hashlib.sha256(huge_note.encode("ascii")).hexdigest())
        l = dc.replace(layer(), notes=SetInput(frozenset({huge_note}), True, "synth-top-b1-v1"))
        self.assertEqual(one((dc.replace(clause(), note_id=huge_note),), profile(top=l), vocabulary=v).fit, F(1))

    def test_gate_precedence_required_over_exclusion_unknown(self):
        r = one((clause(role="required"), clause(2, "base", "excluded", None)), profile())
        self.assertEqual(r.reason, "unverified_required_domain")
        self.assertEqual(r.gates, b.B1GateSummary("unverified", "unverified", "unverified", "unverified"))
        self.assertEqual(r.closure_mask, ())
        self.assertTrue(all(s == b.B1LayerStatus(name, "missing", None, None, None, None)
                            for s, name in zip(r.layers, LAYERS)))

    def test_all_required_optional_any_need_closed_three_layers(self):
        for role in ("required", "optional"):
            for name in LAYERS:
                for unavailable in (None, layer((1,), name, False), layer((1,), name, True, "other")):
                    fields = {n: layer((1,), n) for n in LAYERS}
                    fields[name] = unavailable
                    r = one((clause(selector="any_pyramid", role=role),), profile(**fields))
                    self.assertIsNone(r.fit)
                    self.assertIsNone(r.query_coverage)
                    self.assertEqual(r.clauses[0].state, "unverified")
                    self.assertIsNone(r.clauses[0].witness)
                    self.assertEqual(r.clauses[0].unverified_domains, (name,))

    def test_exclusion_any_known_failure_wins_unknown_and_priority(self):
        r = one((clause(2, role="required"), clause(1, "any_pyramid", "excluded", None)),
                profile(top=layer((1, 2)), heart=layer((1,), "heart", False)))
        self.assertEqual(r.reason, "rejected_excluded")
        self.assertEqual(r.clauses[0].witness, b.B1Occurrence(note(1), "top"))
        self.assertEqual(r.clauses[0].unverified_domains, ("heart", "base"))
        self.assertEqual(r.gates.excluded, "failed")

    def test_formula_shape_and_fraction_subclass_refused(self):
        class FractionSubclass(F):
            pass
        for weights, error, message in (([], TypeError, "Invalid typed input"),
                ((), ValueError, "Unsupported configuration"), ((F(4, 5),), ValueError, "Unsupported configuration"),
                ((FractionSubclass(4, 5), F(1, 5)), TypeError, "Invalid typed input")):
            self.check_error(error, message, config=dc.replace(config(), formula_weights=weights))

    def test_all_membership_caps_precede_vocabulary_member_scan(self):
        # IR-B1-IMPL-01: later container lengths must win over early bad members.
        v = dc.replace(vocabulary(512), note_ids=frozenset({False}))
        p = profile(top=layer(range(1, 514)))
        self.check_error(ValueError, "Input bound exceeded", candidates=(p,), vocabulary=v)

    def test_all_membership_caps_precede_earlier_candidate_member_scan(self):
        bad_set = forged(SetInput, members=frozenset({False}), complete=True,
                         domain_id="synth-top-b1-v1")
        bad_first = profile(1, top=dc.replace(layer(), notes=bad_set))
        over_bound_last = profile(2, top=layer(range(1, 514)))
        self.check_error(ValueError, "Input bound exceeded", candidates=(bad_first, over_bound_last),
                         vocabulary=vocabulary(512))

    def test_all_membership_caps_precede_earlier_layer_member_scan(self):
        bad_set = forged(SetInput, members=frozenset({False}), complete=True,
                         domain_id="synth-top-b1-v1")
        p = profile(top=dc.replace(layer(), notes=bad_set), base=layer(range(1, 513), "base"))
        self.check_error(ValueError, "Input bound exceeded", candidates=(p,), vocabulary=vocabulary(512))
        # Valid exactly-at-bound control: 1 Top + 511 Base memberships.
        valid = profile(top=layer((1,)), base=layer(range(2, 513), "base"))
        r = one((clause(selector="any_pyramid"),),
                dc.replace(valid, heart=layer((), "heart")), vocabulary=vocabulary(512))
        self.assertEqual((r.positive_domain_size, r.focus), (512, F(1, 512)))


if __name__ == "__main__":
    unittest.main()
