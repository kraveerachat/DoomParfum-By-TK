# Exact mathematical primitives — SYNTHETIC verification only

This is partial IMP-MATCH-02 progress after Owner-merged Planning PR4 at
aa55f8b59acb0872b3b40273a8cdd25198f3ba27. All DM01–07 remain PROPOSED. The current explicit owner
request allows decision-independent mathematics/SYNTHETIC fixtures; it does not accept draft
weights, minimum comparable layers, missing-component redistribution, confidence bands or ranking
groups. This package implements none of Mode A/B1/B2, real-data retrieval, rights/auth checks or UI.

## Interfaces and interpretation

All numeric values are exact int/Fraction inputs; booleans, floating-point values (including finite
floats), expressions, NaN and infinity are refused. Results are Fractions in [0,1] or explicit null
Measure values/reasons. No display rounding, percentages or smell-perception claims are produced.

| Primitive | Contract |
|---|---|
| SetInput / set_jaccard | Explicit canonical frozenset, caller-supplied complete flag and exact domain ID; unknown/incomplete/domain mismatch/null; empty/empty undefined; known empty/nonempty zero |
| VectorInput / weighted_jaccard | Finite immutable sorted unique pairs with explicit complete/domain/scale metadata; identical full keys required; no zero extension, rank conversion or strength guessing; unknown values/null; all-zero denominator undefined |
| weighted_mean | Explicit positive weights for identical keys; every component must be known; an unknown component returns null without weight redistribution |
| coverage | Explicit known reliability values and positive weights for identical keys; original total-weight denominator, no default thresholds |
| RankItem / stable_order | Finite immutable tuple, unique canonical lowercase UUIDs; known exact values descending, UUID tie order, undefined last; no currentness/coverage/method-group policy |

The complete/domain/scale fields are mathematical assertions supplied by the caller, not proof of
reviewed source completeness, taxonomy compatibility, source permissions or eligibility. A future
application must establish those independently before any separately authorized scorer. This package
does not authorize reuse of any source data and is not an application-stack decision.

Raw repeated occurrences are not accepted or deduplicated here: SetInput requires a preconstructed
canonical frozenset. Raw claims, ordinals, held profiles and source observations remain upstream.
Numeric vectors must explicitly include the same full key domain; missing keys or NULL strengths
cannot become zero. There is no presence fallback or automatic normalization.

~~~python
from fractions import Fraction as F
from matching_math.primitives import SetInput, set_jaccard

# Explicitly SYNTHETIC finite complete sets, not perfume claims.
a = SetInput(frozenset({"S-x", "S-y"}), True, "synthetic-domain-v1")
b = SetInput(frozenset({"S-x", "S-z"}), True, "synthetic-domain-v1")
assert set_jaccard(a, b).value == F(1, 3)
~~~

## Executed evidence and limits

Run from this repository root:

    python -m unittest discover -s matching_math/tests -v

24/24 focused methods pass, no failures/errors/skips. Small-domain exhaustive checks cover256set
pairs,729vector pairs and24UUID-order permutations; these are cases inside methods, not additional
test-method counts. Golden7/15 observed-vector and3/5 explicit-extra-dimension cases are arithmetic
controls only. Initial test import failed because primitives.py had not yet been created; no test
methods executed at that RED checkpoint. [Exact report and hashes](evidence/unit_results.json).

No dependencies installed; no filesystem/database/network service is accessed by the primitive
source. No existing shared runtime, migration, test or catalogue file is edited. DB/API/UI,
real-data ranking, performance/relevance and complete Mode A/B1/B2 acceptance are NOT RUN.

Full IMP-MATCH-02 scorer behavior remains blocked by verified IMP-MATCH-01 and accepted DM01–04.
IMP-MATCH-03/04 are separate tasks, not implemented here. Real matching stays off; all1479current
flags and44holds are unchanged. Structural fit, Data Confidence and direct pair evidence must remain
separate. Generic mathematical ability to combine values is not approval to blend those categories.
No final receipt for a complete Mode A task is created by this partial primitives checkpoint.
