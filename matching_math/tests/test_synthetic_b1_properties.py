"""Eight bounded standard-library property families; no optional installations."""
import dataclasses as dc
from fractions import Fraction as F
import itertools
import random
import unittest

from matching_math import synthetic_b1 as b
from matching_math.tests.test_synthetic_b1 import clause, config, layer, note, one, perfume, profile, run, vocabulary


class B1Properties(unittest.TestCase):
    def test_family_1_exhaustive_complete_subsets_and_seeded_states(self):
        # 8*8*3 = 192 complete cases; 128 seeded unavailable-domain cases.
        subsets = [tuple(i + 1 for i in range(3) if mask & (1 << i)) for mask in range(8)]
        for tops, bases, role in itertools.product(subsets, subsets, ("optional", "required", "excluded")):
            cs = (clause(), clause(2, "base", role, None if role == "excluded" else 2))
            r = one(cs, profile(top=layer(tops), base=layer(bases, "base")))
            self.assertIs(type(r.query_coverage), F)
            self.assertIs(type(r.focus), F)
            self.assertTrue(0 <= r.query_coverage <= 1 and 0 <= r.focus <= 1)
            if r.fit is None:
                self.assertIsNone(r.partition_key)
                self.assertIsNone(r.query_fit_percent_display)
            else:
                self.assertTrue(0 < r.fit <= 1)
                self.assertEqual(r.fit, F(4, 5) * r.query_coverage + F(1, 5) * r.focus)
                self.assertEqual(r.reason, "computed")
        rng = random.Random(20261115)
        for _ in range(128):
            selected = [None if rng.randrange(4) == 0 else layer((1,), name, rng.choice((True, False)),
                        "mismatch" if rng.randrange(4) == 0 else None) for name in ("top", "heart", "base")]
            r = one((clause(selector="any_pyramid"),), profile(top=selected[0], heart=selected[1], base=selected[2]))
            if any(s.state != "complete" for s in r.layers):
                self.assertIsNone(r.fit)
                self.assertIsNone(r.query_coverage)
                self.assertIsNone(r.focus)
                self.assertIsNone(r.positive_domain_size)

    def test_family_2_permutations_and_duplicates(self):
        cs = (clause(2, "base"), clause(), clause(3, "heart", "excluded", None))
        ps = (profile(2, top=layer((1, 4)), heart=layer((), "heart"), base=layer((2,), "base")),
              profile(1, top=layer((1,)), heart=layer((), "heart"), base=layer((2,), "base")))
        expected = run(cs, ps)
        for terms, candidates in itertools.product(itertools.permutations(cs), itertools.permutations(ps)):
            self.assertEqual(run(terms, candidates), expected)
            dup = run(terms + (terms[0],), candidates)
            self.assertEqual(dc.replace(dup, raw_clause_count=3), expected)
        for order in itertools.permutations((1, 2, 3)):
            self.assertEqual(layer(order).notes.members, layer((1, 2, 3)).notes.members)

    def test_family_3_normalization_conflicts_assignment(self):
        cs = (clause(1, "base"), clause(1, "top"), clause(2, "any_pyramid"))
        p = profile(top=layer((1, 2)), heart=layer((2,), "heart"), base=layer((1, 2), "base"))
        result = run(cs, (p,))
        self.assertEqual(run(result.query_key.clauses, (p,)), result)
        witnesses = [e.witness for e in result.groups[0].results[0].clauses]
        self.assertEqual(len(set(witnesses)), 3)
        self.assertEqual(witnesses[-1].layer, "top")
        for a, c in itertools.product((clause(), clause(role="required")),
                (clause(weight=2), clause(selector="any_pyramid"))):
            for terms in ((a, c), (c, a)):
                with self.assertRaisesRegex(ValueError, "^Invalid query$"):
                    run(terms)

    def test_family_4_positive_and_excluded_domain_monotonicity(self):
        # 2 roles * 3 initial sizes * 2 match states = 12 exact comparisons.
        for role, size, matched in itertools.product(("optional", "required"), range(3), (False, True)):
            initial = tuple(range(2, 2 + size)) + ((1,) if matched else ())
            a = one((clause(role=role),), profile(top=layer(initial)))
            c = one((clause(role=role),), profile(top=layer(initial + (5,))))
            self.assertEqual(a.query_coverage, c.query_coverage)
            self.assertLessEqual(c.focus, a.focus)
            if matched:
                self.assertLess(c.focus, a.focus)
                self.assertLess(c.fit, a.fit)
            else:
                self.assertEqual(c.focus, F(0))
                self.assertIsNone(c.fit)
        cs = (clause(), clause(2, "base", "excluded", None))
        a = one(cs, profile(top=layer((1,)), base=layer((), "base")))
        c = one(cs, profile(top=layer((1,)), base=layer((3,), "base")))
        self.assertEqual((a.query_coverage, a.focus, a.fit), (c.query_coverage, c.focus, c.fit))
        self.assertEqual(one(cs, profile(top=layer((1,)), base=layer((2,), "base"))).reason, "rejected_excluded")

    def test_family_5_closure_cannot_manufacture_pass(self):
        for selector in ("top", "heart", "base", "any_pyramid"):
            cs = (clause(selector=selector, role="required"),)
            for missing in ("top", "heart", "base"):
                fields = {name: layer((1,), name) for name in ("top", "heart", "base")}
                fields[missing] = None
                r = one(cs, profile(**fields))
                if selector in (missing, "any_pyramid"):
                    self.assertIsNone(r.fit)
                    self.assertEqual(r.gates.required, "unverified")
        for observed in ((), (2,)):
            r = one((clause(), clause(2, "base", "excluded", None)),
                    profile(top=layer((1,)), base=layer(observed, "base", False)))
            self.assertEqual(r.gates.excluded, "failed" if observed else "unverified")
            self.assertIsNone(r.fit)

    def test_family_6_order_conservation_partition_identity(self):
        ps = tuple(profile(i, top=layer((1,) if i % 2 else ())) for i in range(1, 17))
        rng = random.Random(88)
        for _ in range(32):
            shuffled = list(ps)
            rng.shuffle(shuffled)
            result = run(candidates=tuple(shuffled))
            numeric = result.groups[0].results
            self.assertEqual(tuple(r.candidate_id for r in numeric), tuple(perfume(i) for i in range(1, 17, 2)))
            self.assertEqual(tuple(r.candidate_id for r in result.unranked), tuple(perfume(i) for i in range(2, 17, 2)))
            self.assertEqual(len(numeric) + len(result.unranked), 16)
            self.assertEqual(len(result.groups), 1)
            self.assertTrue(all(r.partition_key == result.groups[0].key for r in numeric))
        self.assertNotEqual(run().query_key, run((clause(weight=2),)).query_key)
        self.assertNotEqual(run().query_key, run(vocabulary=vocabulary(6)).query_key)
        a = run(candidates=(profile(top=layer((1,))),))
        changed = profile(top=dc.replace(layer((1,)), capture_id="other-capture"))
        self.assertEqual(a.query_key, run(candidates=(changed,)).query_key)
        self.assertEqual(a.groups[0].key, run(candidates=(changed,)).groups[0].key)

    def test_family_7_frozen_schema_types_bounded_no_payload(self):
        r = run((clause(), clause(2, "base", "excluded", None)),
                (profile(top=layer((1,)), base=layer((), "base")),))
        visited = []
        def visit(value):
            if dc.is_dataclass(value):
                visited.append(value)
                self.assertTrue(type(value).__dataclass_params__.frozen)
                for f in dc.fields(value):
                    self.assertIs(f.default, dc.MISSING)
                    visit(getattr(value, f.name))
                with self.assertRaises(dc.FrozenInstanceError):
                    setattr(value, dc.fields(value)[0].name, None)
            elif type(value) is tuple:
                for child in value:
                    visit(child)
            else:
                self.assertIn(type(value), (str, int, bool, F, type(None)))
        visit(r)
        names = {type(x).__name__ for x in visited}
        self.assertEqual(names, {"B1BatchResult", "B1QueryKey", "B1Config", "B1ContextKey", "B1LayerDomain",
            "B1Clause", "B1PartitionResult", "B1PartitionKey", "B1CandidateResult", "B1GateSummary",
            "B1ClauseEvaluation", "B1Occurrence", "B1LayerStatus", "B1Lineage"})
        self.assertNotIn("B1Profile", names)
        self.assertNotIn("SetInput", names)

    def test_family_8_no_fallback_and_directional_weights(self):
        for f in ("method_id", "config_id", "schema_id", "role_policy_id", "selector_policy_id"):
            with self.assertRaisesRegex(ValueError, "^Unsupported configuration$"):
                run(config=dc.replace(config(), **{f: "unknown-version"}))
        p = profile(top=layer((1,)))
        a = one((clause(weight=5), clause(2)), p)
        c = one((clause(), clause(2, weight=5)), p)
        self.assertEqual((a.query_coverage, c.query_coverage), (F(5, 6), F(1, 6)))
        self.assertNotEqual(a.fit, c.fit)


if __name__ == "__main__":
    unittest.main()
