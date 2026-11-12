---
id: IMP-MATCH-02
project: DoomParfum By TK
type: implementation_task
status: partial-primitives-verified-scorer-gated
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, matching, math, synthetic]
source_of_truth: "../../../README.md"
---

# IMP-MATCH-02 — Decision-independent synthetic mathematics

Branch codex/imp-match-02-synthetic-primitives; starting/main SHA
aa55f8b59acb0872b3b40273a8cdd25198f3ba27. Parent verified Owner merge of Planning PR4 at this SHA.
The latest explicit post-PR4 request authorizes generic primitives and SYNTHETIC tests while
requiring DM behavior gates. DM01–07 remain PROPOSED; merge is not acceptance of weights/policy.

## Scope and task map

1. Read merged matching specification/architecture/data contract/acceptance and actual Git state.
2. Build exact rational set/vector comparison, complete-input weighted mean/coverage and stable
   UUID tie ordering without defaults. Unknown/incomplete/incompatible data cannot become zero.
3. Run SYNTHETIC golden, exhaustive small-domain property, determinism and adversarial tests.
4. Record exact code/test hashes, docs/diff checks, independent review and a separate Draft PR.

The bounded artifact is reusable math only. Actual Mode A scorer behavior remains blocked by
IMP-MATCH-01 plus accepted DM01–04. B1/B2/query normalization/confidence/grouping are not implemented.
No real-data ranking, percentages, source/evidence blending, external AI/API, database access/write,
eligibility change, catalogue mutation, assets, migration, app stack or Production work.

## Ownership and protected surfaces

Own new matching_math package and its dedicated tests/guide, this task and dedicated evidence note.
Do not modify shared Project_Status/Decision/Change/AgentRun/Roadmap notes; coordinator integrates.
Original plans/decisions/source/rights/44 holds/receipts stay unchanged. Parent owns D1–D9 and ZIP.
Existing Python/Git/PowerShell only; no dependency install, DB or Docker call. Git/Obsidian writeYES;
PRODUCTION_MUTATION=NO; HUMAN_MERGE_REQUIRED=YES.

## Planned evidence and gate

Focused unittest discovery on matching_math/tests, exact Fraction oracles and finite exhaustive
properties; explicit invalid/unknown/empty/incompatible controls; no fabricated RED/PASS.
Independent review must inspect actual source checkpoint before readiness. No final receipt while
the full Mode A task remains incomplete; preserve partial-progress boundary in Draft description.


## Actual bounded implementation result

Implemented only exact rational primitives: closed-set/vectorJaccard, explicitweights complete-input
mean/coverage, stableUUIDties with undefined values last. No default weight or ModeA/B1/B2policy.
InitialRED import error beforemodulecreation; recorded24/24focused methods PASS0.050117s,0fail/error/
skip.256set-pair/729vector-pair/24ordering cases are internal cases, not extra methods. New executable
source has stdlib-only imports, no IO/database/network. Existing runtime/SQL/catalogue/receipts unchanged.
Full ModeA acceptance stillblocked by IMP-MATCH-01 and acceptedDM01–04; no feature-release readiness
or finalreceipt claimed. [[IMP-MATCH-02_Synthetic_Primitives_Evidence]] holds exact hashes/tests.
Independent source review, documentation checks and dedicated Draft publication follow.


## Independent source review and publication checkpoint

Parent independently inspected sourcecheckpointa5c82df4800b1e46dec147d1b274c001dd2936cd and reran24/24
focused methods PASS0.036s,0fail/errors. No blocking finding in exactpureSYNTHETICprimitives scope.
No DB/API/UI or real ranking test claimed. matching_math/evidence/independent_review.json records
sourcebindings/outcomes/limits. Metadata closeout leaves all3executedsource/test hashes unchanged.
Dedicated DraftPR is partialimplementation progress, not complete ModeA/DMacceptance. No finalreceipt
while fullscorer behavior remains gated; HumanOwner alone reviews/merges. Resulting publicationHEAD
and PR URL are verified after actualpush/readback in externalhandoff/PR description.
