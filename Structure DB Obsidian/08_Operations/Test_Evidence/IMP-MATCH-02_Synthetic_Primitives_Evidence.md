---
id: DPT-EVD-IMP-MATCH-02-PRIMITIVES
project: DoomParfum By TK
type: test_evidence
status: partial-primitives-verified-scorer-gated
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, matching, math, synthetic]
source_of_truth: "../../../README.md"
---

# IMP-MATCH-02 — Exact primitive evidence

Base/approved-plan merge aa55f8b59acb0872b3b40273a8cdd25198f3ba27; branch
codex/imp-match-02-synthetic-primitives. This is partial decision-independent work, not a completed
Mode A scorer or implicit acceptance of DM01–07. [[IMP-MATCH-02_Synthetic_Primitives]] records scope.

## Actual tests

Command: python -m unittest discover -s matching_math/tests -v.
24methods/24passed,0failed/errors/skips,0.050117s recorded focused run under Python3.11.9.
Initial RED is observed ModuleNotFoundError matching_math.primitives before implementation:
1loader error,0test methods executed. No retrospective assertion-failure claim.

Golden exact Fraction oracles,256set-pair and729vector-pair exhaustive properties,24UUID-order
permutations, range/symmetry/identity, input-order invariance and exact-score-before-display ordering.
Negatives cover missing/incomplete/incompatible domains/scales, empty/all-zero denominators, unknown
strengths/components, absence of implicit zero padding, invalid/duplicate IDs, raw list deduplication
refusal, NaN/infinity/float/Boolean/out-of-range/expression inputs, weight/key mismatch and iterator
refusal. Coverage uses explicit weights and original denominator. Unknown mean components return
null without renormalization; no missing-component policy is selected.

[Guide](../../../matching_math/README.md), [executed report](../../../matching_math/evidence/unit_results.json).
Canonical UTF8/LF SHA256 source bindings:

- matching_math/__init__.py:52787f3b39a18013db9db0d042b53c2fa0ad559f85c73f2bcc677e5a9f25c61f
- matching_math/primitives.py:c1b69bdc74a4a060f6559a182306618f02c595b16e27f3ebb5e4bcca4ff7b735
- matching_math/tests/test_primitives.py:777b2e2b04d0f67ab32a279940faa2488ba59cc70050cacc4b487fcecacbde30

## Not run and remaining gate

No DB/Docker/integration/API/UI/real-data scoring/benchmark/source acquisition. Existing database
regression is not rerun: no shared source, SQL or database runtime is imported or edited. Source
stdlib imports are collections.abc/dataclasses/fractions/uuid only. Exact completeness/domain/scale
assertions in math inputs do not establish accepted source rights/completeness or matching eligibility.
The future adapter/scorer must enforce those externally. No confidence/evidence values are blended.

Full IMP-MATCH-02 requires IMP-MATCH-01 and accepted DM01–04 before affected behavior. Minimum layers,
component defaults, missing-component distribution, percent labels/confidence bands/grouping are not
implemented. All44held profiles,1479matching flags, source provenance and old receipts remain unchanged.
Parent coordinator owns shared status/logs/decision register/D1–D9/ZIP; no final receipt while complete
Mode A behavior remains gated. Independent exact-source review and dedicated Draft publication pending.


## Independent source review and publication checkpoint

Parent independently inspected sourcecheckpointa5c82df4800b1e46dec147d1b274c001dd2936cd and reran24/24
focused methods PASS0.036s,0fail/errors. No blocking finding in exactpureSYNTHETICprimitives scope.
No DB/API/UI or real ranking test claimed. matching_math/evidence/independent_review.json records
sourcebindings/outcomes/limits. Metadata closeout leaves all3executedsource/test hashes unchanged.
Dedicated DraftPR is partialimplementation progress, not complete ModeA/DMacceptance. No finalreceipt
while fullscorer behavior remains gated; HumanOwner alone reviews/merges. Resulting publicationHEAD
and PR URL are verified after actualpush/readback in externalhandoff/PR description.
