---
id: IMP-MATCH-03-DESIGN
project: DoomParfum By TK
type: implementation_design
status: in-progress
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, synthetic, b1, typed]
source_of_truth: "../../README.md"
---

# Synthetic B1 implementation guide

Authority: [[B1_Exact_Owner_Acceptance]], complete frozen [[B1_Positive_Domain_Typed_Contract]]
revision2/hash77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977.
This guide describes the accepted binding, not a new policy. Actual status/evidence:
[[IMP-MATCH-03_Synthetic_B1]] / [[IMP-MATCH-03_Synthetic_B1_Evidence]].

## Pure typed boundary

```python
from matching_math.synthetic_b1 import score_synthetic_b1

# Explicit exact approved frozen objects; every field and argument is required.
# No dictionaries, alias resolver, transport decoder or default configuration.
result = score_synthetic_b1(query, candidates, vocabulary=vocabulary, config=config)
```

Inputs are the contract's B1Query/B1Clause, B1Profile/B1Layer, B1Vocabulary and B1Config classes,
plus unchanged SetInput for declared fixture sets. Canonical UUID namespaces/vocabulary fingerprint,
expected domains/snapshot/scope/lineage and all policy/version fields are explicit. There is no
reference perfume or new catalogue record. No alias/fuzzy/source normalization is implemented.

Raw30clause cap is enforced before duplicate collapse; candidate64,per-candidate512membership,
vocabulary512,token128ASCII/numeric128bit and total32768limits are fixed explicit configuration.
Incomplete/irrelevant memberships count too. All candidates validate before any result. Existing
M1/primitives/adapter/SQL are unchanged; no runtime I/O, network, clock, random state or mutable defaults.
Caller object-construction memory and API byte budgets are outside this pure function's bound.

## Gates, exact values and explanations

Required clauses all need verified matches in complete compatible requested domains. Optional
clauses are soft but unmatched weight remains in Q denominator. Excluded weight is None; compatible
observed presence fails even in incomplete previews, while absence passes only when every searched
domain is closed. any_pyramid searches all3layers, never whichever rows exist. Missing/unknown is
not a zero. Shape/config/identity/lineage errors reject the batch with bounded fixed messages.

Identical canonical query clauses collapse once; same-selector role/weight conflicts and same-ID
any-plus-exact queries reject. Disjoint exact-layer clauses remain independent; witness priority
is Top/Heart/Base without positive occurrence reuse. Raw source repeats are not transformed here.

Positive search domain D includes all memberships only in positive layers. Q=verified matched
weight/all normalized positive weight; H=distinct verified positive witnesses/|D|. Q/H/Dsize remain
None unless all positive domains are complete. Complete-empty D has diagnostic Q=H=0, but no fit.
Numeric fit4/5Q+1/5H requires strict gates plus positive minimum1. Known diagnostics do not rescue
a rejected/unverified candidate. Observed subset counts and Data Confidence/pair evidence stay separate.

Results are exact immutable contract records. Canonical query/config/context/domain identity forms
one comparable numeric partition at most; candidates sort by exact unrounded fit then UUID, while
unranked candidates sort separately by UUID. Half-up one-decimal display follows exact ordering.
Explanations copy bounded declared fields only, never full candidate sets or arbitrary payloads.
Display percentages are query-fit model values, not scientific smell similarity or accuracy.

## Reproduction and limits

From repository root:

```text
python -m unittest matching_math.tests.test_synthetic_b1 matching_math.tests.test_synthetic_b1_properties -v
python -m unittest discover -s matching_math/tests -v
python -m unittest discover -s database/tests -p "test_research_audit.py" -v
```

For the existing offline adapter class in PowerShell, without the live test class:

```powershell
Push-Location database/tests
python -m unittest test_matching_input.AdapterOfflineTests -v
Pop-Location
```

Actual test counts/timings/source hashes/RED failures and independent review are recorded only
after execution in matching_math/evidence/b1_* and the evidence note. A reproduction command is
not evidence of a PASS. No dependency installation is required by this module.

Synthetic completeness/UUID/lineage is caller-declared and does not prove real rights, closure,
source review, authorization or eligibility. No real-data ranking, Full Mode A/B2, API/UI,
transport8KiB parser, source/image acquisition, normalization promotion,44hold/eligibility change,
database/Production/cloud mutation or agent merge. Current DB/rights/roles are not revalidated.
PR8 historical failures remain blocked and untouched. Data/media research has separate gates;
B1 code approval does not approve asset bytes, source samples, imports or app delivery.
