"""Bounded stdlib property checks; no external dependency or real catalogue input."""
from dataclasses import replace
from fractions import Fraction
from itertools import product, permutations
import random
import unittest

from matching_math.tests.test_synthetic_m1 import m, batch, config, layer, pair, pid, profile, vocabulary


class SyntheticM1PropertyTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(m, 'Approved synthetic M1 scorer is not implemented')

    def test_exhaustive_two_note_layered_sets(self):
        """All 4**6=4096 pairs of complete pyramids over a two-note domain."""
        options = ((), (1,), (2,), (1, 2))
        weights = (Fraction(1, 4), Fraction(3, 8), Fraction(3, 8))
        for choices in product(options, repeat=6):
            left, right = choices[:3], choices[3:]
            r, c = profile(1, *left), profile(2, *right)
            result = pair(batch(r, (c,), context=vocabulary(2)))
            ratios = tuple(None if not set(a) | set(b) else Fraction(len(set(a) & set(b)), len(set(a) | set(b)))
                           for a, b in zip(left, right))
            support = sum((w for w, j in zip(weights, ratios) if j is not None), Fraction(0))
            count = sum(j is not None for j in ratios)
            expected = sum((w * j for w, j in zip(weights, ratios) if j is not None), Fraction(0)) / support if count >= 2 else None
            self.assertEqual(result.fit, expected)
            self.assertEqual(result.observed_layer_support, support)
            self.assertEqual(result.scoring_coverage, support / 2 if count >= 2 else Fraction(0))
            self.assertTrue(result.fit is None or 0 <= result.fit <= 1)

    def test_seeded_missing_incomplete_domains_and_symmetry(self):
        """250 independent bounded generated fixture pairs; role metadata is not equated."""
        generator = random.Random(8012026)
        def generated(identity):
            layers = []
            for _ in range(3):
                state = generator.randrange(5)
                values = tuple(i for i in range(1, 8) if generator.randrange(2))
                layers.append(None if state == 0 else layer(values, domain='other' if state == 1 else 'domain', complete=state != 2))
            return m.FixtureProfile(pid(identity), *layers)
        for _ in range(250):
            r, c = generated(1), generated(2)
            a, b = pair(batch(r, (c,))), pair(batch(c, (r,)))
            self.assertEqual((a.fit, a.scoring_coverage, a.observed_layer_support), (b.fit, b.scoring_coverage, b.observed_layer_support))
            self.assertEqual(tuple(x.reason for x in a.layers), tuple(x.reason for x in b.layers))
            self.assertEqual(a.layers[0].left, b.layers[0].right)
            self.assertTrue(0 <= a.scoring_coverage <= Fraction(1, 2))
            self.assertEqual(batch(r, (c,)), batch(r, (c,)))

    def test_all_candidate_permutations_preserve_partitioned_results(self):
        r = profile(1, (1,), (4,), (5,))
        candidates = (profile(2, (1,), (4,), None), profile(3, (1,), None, (5,)),
                      profile(4, None, (4,), (5,)), profile(5, None, None, None))
        expected = batch(r, candidates)
        for ordering in permutations(candidates):
            self.assertEqual(batch(r, ordering), expected)

    def test_config_replacements_never_select_hidden_fallbacks(self):
        changes = ({'method_id': 'mc-a-full'}, {'config_id': 'm1-other'}, {'note_support_budget': Fraction(1)},
                   {'layer_weights': (Fraction(1, 3),) * 3}, {'min_comparable_layers': 1})
        for change in changes:
            with self.assertRaises(ValueError):
                batch(settings=replace(config(), **change))


if __name__ == '__main__':
    unittest.main()
