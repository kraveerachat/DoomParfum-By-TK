"""Only SYNTHETIC IDs/vectors. These are mathematical controls, not perfume claims."""
from fractions import Fraction as F
import itertools
import unittest

from matching_math.primitives import (
    SetInput, VectorInput, RankItem, set_jaccard, weighted_jaccard,
    weighted_mean, coverage, stable_order,
)


def sets(items=(), complete=True, domain="synthetic-note-domain-v1"):
    return SetInput(frozenset(items), complete, domain)


def vector(values, complete=True, domain="synthetic-accord-domain-v1", scale="synthetic-scale-v1"):
    return VectorInput(tuple(sorted(values.items())), complete, domain, scale)


def uuid(number):
    return f"00000000-0000-0000-0000-{number:012x}"


class SetComparisonTests(unittest.TestCase):
    def test_synthetic_golden_partial_overlap_is_exact(self):
        self.assertEqual(set_jaccard(sets(["S-x", "S-y"]), sets(["S-x", "S-z"])).value, F(1, 3))

    def test_known_empty_union_is_undefined_not_perfect(self):
        self.assertEqual(set_jaccard(sets(), sets()).reason, "empty_union")
        self.assertIsNone(set_jaccard(sets(), sets()).value)

    def test_known_empty_against_nonempty_is_zero(self):
        self.assertEqual(set_jaccard(sets(), sets(["S-x"])).value, F(0))

    def test_unknown_and_incomplete_are_explicit_null_states(self):
        self.assertEqual(set_jaccard(None, sets()).reason, "missing_input")
        self.assertEqual(set_jaccard(sets(["S-x"], False), sets(["S-x"])).reason, "incomplete_input")

    def test_incompatible_domains_do_not_compare(self):
        result = set_jaccard(sets(["S-x"]), sets(["S-x"], domain="other-synthetic-domain"))
        self.assertIsNone(result.value)
        self.assertEqual(result.reason, "domain_mismatch")

    def test_raw_sequences_are_not_silently_deduplicated(self):
        with self.assertRaises(TypeError):
            SetInput(["S-x", "S-x"], True, "synthetic-domain")

    def test_invalid_ids_or_nonboolean_closure_are_rejected(self):
        for members, complete, domain in [
            (frozenset([""]), True, "S"), (frozenset([" S-x"]), True, "S"),
            (frozenset([1]), True, "S"), (frozenset(), 1, "S"), (frozenset(), True, ""),
        ]:
            with self.subTest(members=members, complete=complete, domain=domain), self.assertRaises((TypeError, ValueError)):
                SetInput(members, complete, domain)

    def test_all_small_subsets_have_symmetry_range_and_identity(self):
        subsets = [sets(k for k, flag in zip("abcd", flags) if flag)
                   for flags in itertools.product([False, True], repeat=4)]
        for a, b in itertools.product(subsets, repeat=2):
            left, right = set_jaccard(a, b), set_jaccard(b, a)
            self.assertEqual(left, right)
            if left.value is not None:
                self.assertTrue(F(0) <= left.value <= F(1))
            if a == b and a.members:
                self.assertEqual(left.value, F(1))


class VectorComparisonTests(unittest.TestCase):
    def test_synthetic_golden_observed_vector_comparison(self):
        left = vector({"S-a": F(1), "S-b": F(1, 2)})
        right = vector({"S-a": F(1, 5), "S-b": F(1, 2)})
        self.assertEqual(weighted_jaccard(left, right).value, F(7, 15))

    def test_explicit_extra_dimension_is_in_denominator(self):
        left = vector({"S-a": F(1), "S-b": F(1, 2), "S-c": F(0)})
        right = vector({"S-a": F(1), "S-b": F(1, 2), "S-c": F(1)})
        self.assertEqual(weighted_jaccard(left, right).value, F(3, 5))

    def test_mismatched_keys_do_not_infer_absent_means_zero(self):
        result = weighted_jaccard(vector({"S-a": F(1)}), vector({"S-a": F(1), "S-b": F(1)}))
        self.assertIsNone(result.value)
        self.assertEqual(result.reason, "domain_mismatch")

    def test_unknown_strength_is_not_zero_or_presence_fallback(self):
        result = weighted_jaccard(vector({"S-a": None}), vector({"S-a": F(1)}))
        self.assertIsNone(result.value)
        self.assertEqual(result.reason, "unknown_value")

    def test_missing_incomplete_domain_and_scale_states_are_null(self):
        known = vector({"S-a": F(1)})
        for other, reason in [
            (None, "missing_input"),
            (vector({"S-a": F(1)}, complete=False), "incomplete_input"),
            (vector({"S-a": F(1)}, domain="other-domain"), "domain_mismatch"),
            (vector({"S-a": F(1)}, scale="other-scale"), "scale_mismatch"),
        ]:
            with self.subTest(reason=reason):
                self.assertEqual(weighted_jaccard(known, other).reason, reason)

    def test_all_zero_and_empty_vectors_are_undefined(self):
        self.assertIsNone(weighted_jaccard(vector({}), vector({})).value)
        self.assertIsNone(weighted_jaccard(vector({"S-a": F(0)}), vector({"S-a": F(0)})).value)

    def test_nonfinite_float_boolean_and_out_of_range_values_rejected(self):
        for value in [True, 0.5, float("nan"), float("inf"), F(-1, 2), F(3, 2), "1/2"]:
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                vector({"S-a": value})

    def test_duplicate_unsorted_or_malformed_vector_pairs_rejected(self):
        for pairs in [(("S-a", F(1)), ("S-a", F(0))), (("S-b", F(1)), ("S-a", F(1))), (("", F(1)),)]:
            with self.subTest(pairs=pairs), self.assertRaises((TypeError, ValueError)):
                VectorInput(pairs, True, "synthetic-domain", "synthetic-scale")

    def test_exhaustive_small_vectors_have_symmetry_range_and_identity(self):
        vectors = [vector(dict(zip(["S-a", "S-b", "S-c"], values)))
                   for values in itertools.product([F(0), F(1, 2), F(1)], repeat=3)]
        for a, b in itertools.product(vectors, repeat=2):
            result = weighted_jaccard(a, b)
            self.assertEqual(result, weighted_jaccard(b, a))
            if result.value is not None:
                self.assertTrue(F(0) <= result.value <= F(1))
            if a == b and any(value for _, value in a.values):
                self.assertEqual(result.value, F(1))


class WeightAndOrderingTests(unittest.TestCase):
    def test_explicit_weights_give_exact_mean_and_coverage(self):
        weights = {"S-a": F(2), "S-b": F(1)}
        self.assertEqual(weighted_mean({"S-a": F(1), "S-b": F(0)}, weights).value, F(2, 3))
        self.assertEqual(coverage({"S-a": F(1, 2), "S-b": F(0)}, weights), F(1, 3))

    def test_missing_component_is_null_without_weight_redistribution(self):
        self.assertEqual(weighted_mean({"S-a": F(1), "S-b": None}, {"S-a": F(2), "S-b": F(1)}).reason,
                         "unknown_value")

    def test_bad_weights_reliabilities_or_domains_are_rejected(self):
        for weights in [{}, {"S-a": F(0)}, {"S-a": F(-1)}, {"S-a": True}, {"S-a": 0.5}]:
            with self.subTest(weights=weights), self.assertRaises((TypeError, ValueError)):
                weighted_mean({"S-a": F(1)}, weights)
        with self.assertRaises(ValueError):
            coverage({"S-a": F(1), "S-b": F(1)}, {"S-a": F(1)})
        with self.assertRaises(TypeError):
            coverage({"S-a": None}, {"S-a": F(1)})

    def test_explicit_weight_scale_and_input_order_do_not_change_result(self):
        first = weighted_mean({"S-a": F(1), "S-b": F(1, 3)}, {"S-a": F(2), "S-b": F(3)})
        second = weighted_mean({"S-b": F(1, 3), "S-a": F(1)}, {"S-b": F(30), "S-a": F(20)})
        self.assertEqual(first, second)

    def test_uuid_ties_nulls_and_input_permutations_are_deterministic(self):
        rows = (RankItem(uuid(3), F(1, 3)), RankItem(uuid(1), F(1, 3)),
                RankItem(uuid(2), F(1)), RankItem(uuid(4), None))
        expected = (rows[2], rows[1], rows[0], rows[3])
        for order in itertools.permutations(rows):
            self.assertEqual(stable_order(order), expected)
        self.assertEqual(rows[0].value, F(1, 3))

    def test_near_scores_sort_by_exact_value_not_display_rounding(self):
        a, b = RankItem(uuid(1), F(9999, 10000)), RankItem(uuid(2), F(1))
        self.assertEqual(stable_order((a, b)), (b, a))

    def test_duplicate_noncanonical_ids_mutable_or_infinite_input_refused(self):
        for candidate in ["S-not-uuid", "00000000-0000-0000-0000-00000000000A"]:
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                RankItem(candidate, F(1))
        with self.assertRaises(ValueError):
            stable_order((RankItem(uuid(1), F(1)), RankItem(uuid(1), F(0))))
        with self.assertRaises(TypeError):
            stable_order(iter(()))


if __name__ == "__main__":
    unittest.main()
