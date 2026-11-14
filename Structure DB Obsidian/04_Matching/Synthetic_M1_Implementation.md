---
id: IMP-MATCH-08-DESIGN
project: DoomParfum By TK
type: implementation_design
status: in-progress
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, synthetic, matching, m1, typed]
source_of_truth: "../../README.md"
---

# Synthetic notes-layered M1 implementation

[[M1_Exact_Owner_Acceptance]] accepts the complete frozen [[M1_Notes_Layered_Typed_Contract]],
version M1-NL-TYPED-1, SHA-256 a57f4c56e1068a3d86a99e562b31e5c3923e2d369cb4e812c1dd5f5550a5ada3.
The new module is `matching_math/synthetic_m1.py`; existing generic primitives remain unchanged.
Current execution/evidence belong to [[IMP-MATCH-08_Synthetic_M1]] and
[[IMP-MATCH-08_Synthetic_M1_Evidence]]. This guide does not redefine or extend the accepted contract.

## Typed entry point and validation

```python
from matching_math.synthetic_m1 import score_synthetic_notes_layered

# All objects below must be explicitly constructed from the exact approved
# frozen classes and bounded synthetic fixture vocabulary/configuration.
# There are no configuration defaults or transport dictionary conversions.
result = score_synthetic_notes_layered(
    reference, candidates, vocabulary=vocabulary, config=config,
)
```

`FixtureProfile`, `FixtureLayer`, `FixtureVocabulary` and `M1Config` require all their fields.
Layer notes use the unchanged `SetInput` class, with an exact frozenset and explicit completeness
and domain ID. All top-level classes, nested containers, strings and numbers are checked without
coercion or custom iterable execution. The contract specifies every input/output field.

Only mc-a-notes-layered-p1/config m1-nl-typed-config-1/schema m1-nl-typed-schema-1 is accepted.
The caller must supply the exact configuration, including weights (1/4,3/8,3/8), minimum2 layers,
note support budget1/2, maximum64 candidates,512 memberships per profile including reference and
incomplete previews,512 vocabulary notes,128-character tokens,128-bit numbers and33280 total
memberships. The total cap follows from the per-profile/candidate caps; it is not an independently
reachable extra-negative case when every other cap is valid.

Validation checks exact top-level types/count, configuration types/bit sizes/equality, vocabulary
size, all profile/layer/set counts and token lengths before member validation or set arithmetic.
It then validates synthetic UUID namespaces, vocabulary fingerprint/membership and explicit
lineage/scope/snapshot/completeness assertions. Every candidate is validated before any result.
Invalid types raise TypeError; invalid values/configuration/bounds raise ValueError with fixed
bounded category text. No input repr, raw records, partial scores or fallback appears in errors.
Caller object construction cost is outside the function's resource bound; this is not a parser.

## Exact scoring and explanation

Each layer uses existing set Jaccard with precedence missing_input, incomplete_input,
domain_mismatch, empty_union. Unknown is never known zero. Complete empty/nonempty and disjoint
sets give numeric zero; complete empty/empty is unavailable. No preview score uses incomplete data.

For at least2 numeric layers, fit is the exact Fraction weighted mean over those layers.
Scoring coverage is half the original comparable layer-weight support. For fewer than2 layers,
fit is None, scoring coverage0 and the candidate is unranked; observed support remains a separate
diagnostic. No automatic full/flat/accord/family method or fallback is selected.

Ranked results are grouped by the exact method/config/schema/context, numeric layer mask and
comparable domains. Group presentation uses mask/domain metadata order, never cross-partition fit.
Inside a partition, exact unrounded fit descends and canonical UUID breaks exact ties. Null results
are separately UUID ordered. Display rounds exact fit percentages half-up to one decimal only
after ordering. Explanations retain all three role-labelled layer states and bounded lineage,
without full note sets, real pair evidence, confidence bands or a scientific smell-similarity claim.
Data Confidence and pair evidence remain the contract's separate not-evaluated constants.

## Verification and boundaries

From the implementation checkout:

```text
python -m unittest discover -s matching_math/tests -p "test_synthetic_m1*.py" -v
python -m unittest discover -s matching_math/tests -v
```

The coordinator additionally runs existing research and AdapterOfflineTests without a database.
Exact executed results, source hashes, bounded property case counts, RED history and independent
review are in the evidence note and `matching_math/evidence/m1_*.json`. Do not infer actual test
results from these reproduction commands; the evidence note records what ran.

Synthetic fixture metadata and UUID prefixes are caller declarations, not proof of real rights,
source review, ownership, completeness or eligibility. There is no real adapter connection,
transport/API/UI, database/SQL mutation, source/image acquisition, normalization/promotion,
hold release, application session, cloud or Production activation. Real A/B1 and the next B1
contract retain their own gates. PR8 historical timestamp diagnosis remains blocked and untouched.

## Offline regression reproduction

These commands select only the same offline components; do not run the live adapter test class.
Use this repository's existing Python dependencies; no new installation is required.

```text
python -m unittest discover -s matching_math/tests -v
python -m unittest discover -s database/tests -p "test_research_audit.py" -v
```

For the14offline adapter methods, from repository root in PowerShell:

```powershell
$env:PYTHONPATH = "database;database/tests"
python -m unittest test_matching_input.AdapterOfflineTests -v
Remove-Item Env:PYTHONPATH
```

The coordinator's combined runner selects these111methods in one process and records exact
source bindings/results. The commands above do not execute database/live adapter tests.
