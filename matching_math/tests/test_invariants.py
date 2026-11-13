"""Bounded SYNTHETIC invariants for accepted generic mathematical primitives.

These tests do not accept source completeness, note normalization, method weights,
source-scale conversion, Mode A/B1/B2, real-data ranking or application policies.
All compared vectors are explicitly supplied complete, with identical keys inside
each comparison. Joint zero-coordinate fixtures do not authorize runtime padding.
"""
from fractions import Fraction as F
import itertools
import unittest

from matching_math.primitives import (
    SetInput, VectorInput, set_jaccard, weighted_jaccard, weighted_mean, coverage,
)


def synthetic_set(items):
    return SetInput(frozenset(items), True, "S-invariant-set-domain")


def synthetic_vector(values, domain="S-invariant-vector-domain"):
    return VectorInput(tuple(sorted(values.items())), True, domain, "S-invariant-scale")


class PrimitiveInvariantTests(unittest.TestCase):
    def test_nonempty_set_jaccard_distance_satisfies_triangle_inequality(self):
        # 7 nonempty subsets; 343 triples. Pairwise symmetry alone does not
        # establish this three-input metric constraint.
        subsets = [synthetic_set(key for key, keep in zip(("S-a", "S-b", "S-c"), flags) if keep)
                   for flags in itertools.product((False, True), repeat=3) if any(flags)]
        for left, middle, right in itertools.product(subsets, repeat=3):
            with self.subTest(left=left.members, middle=middle.members, right=right.members):
                lm = set_jaccard(left, middle).value
                mr = set_jaccard(middle, right).value
                lr = set_jaccard(left, right).value
                self.assertIsNotNone(lm)
                self.assertIsNotNone(mr)
                self.assertIsNotNone(lr)
                self.assertLessEqual(F(1) - lr, (F(1) - lm) + (F(1) - mr))

    def test_weighted_jaccard_agrees_with_independent_l1_identity(self):
        # 80 numeric pairs from a 2-coordinate ternary grid. The joint zero
        # pair has no numeric identity denominator and is covered by old tests.
        coordinates = tuple(itertools.product((F(0), F(1, 3), F(2, 3)), repeat=2))
        for left, right in itertools.product(coordinates, repeat=2):
            total = sum(left + right, F(0))
            if not total:
                continue
            l1 = sum((abs(a - b) for a, b in zip(left, right)), F(0))
            expected = (total - l1) / (total + l1)
            with self.subTest(left=left, right=right):
                actual = weighted_jaccard(
                    synthetic_vector(dict(zip(("S-a", "S-b"), left))),
                    synthetic_vector(dict(zip(("S-a", "S-b"), right))),
                ).value
                self.assertEqual(actual, expected)

    def test_vector_common_scaling_and_explicit_joint_zero_axis_preserve_ratio(self):
        # 6 common positive scaling cases plus 3 explicit expanded-domain cases.
        # This is an algebraic relation across synthetic comparisons, not a
        # conversion of a real source scale or inference of missing values.
        fixtures = (
            ({"S-a": F(1), "S-b": F(1, 3)}, {"S-a": F(1, 3), "S-b": F(2, 3)}),
            ({"S-a": F(0), "S-b": F(2, 3)}, {"S-a": F(1), "S-b": F(0)}),
            ({"S-a": F(1, 3), "S-b": F(1, 3)}, {"S-a": F(1, 3), "S-b": F(1, 3)}),
        )
        for left, right in fixtures:
            expected = weighted_jaccard(synthetic_vector(left), synthetic_vector(right)).value
            for scale in (F(1, 3), F(2, 3)):
                with self.subTest(left=left, right=right, common_scale=scale):
                    actual = weighted_jaccard(
                        synthetic_vector({key: scale * value for key, value in left.items()}),
                        synthetic_vector({key: scale * value for key, value in right.items()}),
                    ).value
                    self.assertEqual(actual, expected)
            with self.subTest(left=left, right=right, explicit_zero_coordinate=True):
                actual = weighted_jaccard(
                    synthetic_vector(dict(left, **{"S-c": F(0)}), "S-explicit-expanded-domain"),
                    synthetic_vector(dict(right, **{"S-c": F(0)}), "S-explicit-expanded-domain"),
                ).value
                self.assertEqual(actual, expected)

    def test_complete_weighted_mean_is_affine_equivariant_within_unit_bounds(self):
        # 27 known-value tuples x 3 bounded affine maps. Constants are explicit
        # synthetic probes, never perfume component weights or missingness rules.
        keys = ("S-a", "S-b", "S-c")
        weights = dict(zip(keys, (F(1, 3), F(2), F(7, 5))))
        for values in itertools.product((F(0), F(1, 3), F(1)), repeat=3):
            original = weighted_mean(dict(zip(keys, values)), weights).value
            for scale, offset in ((F(1, 2), F(1, 4)), (F(1, 3), F(0)), (F(0), F(2, 3))):
                with self.subTest(values=values, scale=scale, offset=offset):
                    transformed = {key: scale * value + offset for key, value in zip(keys, values)}
                    actual = weighted_mean(transformed, weights).value
                    self.assertEqual(actual, scale * original + offset)

    def test_splitting_a_known_component_weight_preserves_mean(self):
        # 9 known-value pairs x 3 positive partitions of a supplied weight.
        # Every new component value is explicitly known. No missing component
        # is dropped and no source occurrence or alias is deduplicated.
        for left, right in itertools.product((F(0), F(1, 3), F(1)), repeat=2):
            expected = weighted_mean({"S-left": left, "S-right": right},
                                     {"S-left": F(5), "S-right": F(7)}).value
            for first, second in ((F(1), F(4)), (F(5, 2), F(5, 2)), (F(1, 3), F(14, 3))):
                with self.subTest(left=left, right=right, partition=(first, second)):
                    actual = weighted_mean(
                        {"S-left-a": left, "S-left-b": left, "S-right": right},
                        {"S-left-a": first, "S-left-b": second, "S-right": F(7)},
                    ).value
                    self.assertEqual(actual, expected)

    def test_coverage_of_complementary_known_reliabilities_sums_to_one(self):
        # 27 reliability tuples, preserving the same explicit original weights.
        keys = ("S-a", "S-b", "S-c")
        weights = dict(zip(keys, (F(1, 7), F(2), F(5))))
        for reliabilities in itertools.product((F(0), F(1, 3), F(1)), repeat=3):
            with self.subTest(reliabilities=reliabilities):
                supplied = dict(zip(keys, reliabilities))
                complement = {key: F(1) - value for key, value in supplied.items()}
                self.assertEqual(coverage(supplied, weights) + coverage(complement, weights), F(1))

    def test_public_comparisons_reject_wrong_operand_categories(self):
        known_set = synthetic_set(("S-a",))
        known_vector = synthetic_vector({"S-a": F(1)})
        # Four public function-boundary controls. Constructor validation alone
        # does not establish rejection of the wrong DTO category at the call.
        for function, left, right in (
            (set_jaccard, known_vector, known_set),
            (set_jaccard, known_set, ("S-a",)),
            (weighted_jaccard, known_set, known_vector),
            (weighted_jaccard, known_vector, {"S-a": F(1)}),
        ):
            with self.subTest(function=function.__name__, left_type=type(left), right_type=type(right)):
                with self.assertRaises(TypeError):
                    function(left, right)


if __name__ == "__main__":
    unittest.main()
