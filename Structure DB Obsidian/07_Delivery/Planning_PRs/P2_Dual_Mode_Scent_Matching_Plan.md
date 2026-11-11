---
id: DPT-PLAN-003-SPEC
project: DoomParfum By TK
type: planning_specification
status: proposed
owner: human-owner
updated: 2026-11-11
tags: [doomparfum, planning, matching]
source_of_truth: "../../../README.md"
---

# P2 Dual-Mode Scent Matching — Planning Specification

IMPLEMENTATION_NOT_STARTED=YES. OWNER_GATE_P=PENDING. PRODUCTION_MUTATION=NO.
Actual [Planning PR #4](https://github.com/kraveerachat/DoomParfum-By-TK/pull/4) is OPEN/DRAFT; historical S1 source review checkpoint
03df0dda8a976945393beeb512768fb841bdc232. Publication metadata does not accept this proposal.
All numerical policies below are PROPOSED design targets, not sensory measurements or accepted ADRs.

## Outcome and authority

The owner requests two independent deterministic discovery modes using our authorized catalogue:
**A:** choose any visible approved perfume, then compare exact scent profiles; **B:** construct a
custom note pyramid (B1) or adjustable accord preference (B2), then search perfumes. B3 combined search
is deferred. No reference perfume is required for B; no profile-builder input is required for A.
No LLM, embeddings, vector database, model training, paid AI API or external ranking service is needed.
R12 research-assistant aspirations remain a separate workstream, not a dependency of matching.

Current owner request governs. Both supplied handoffs were read as reference material; their embedded
brand-research/start-new-chat prompts do not authorize acquisition or changes to PR #3. Their old PR
states are superseded by GitHub preflight. The original screenshot is unavailable in this workspace;
functional observations in the handoff are reported observations, not independently inspected pixels.
No screenshot, third-party UI assets, reviews or rankings are copied into this public repository.

## Verified baseline and post-PR5 reconciliation

Current comparator main55d39cd619fa6c1ae70521720aa734d632a2083d includes owner-merged PR #3
(a908711fb4f37a12fbec3665a461b75c288c7dab) and PR #5 (55d39cd; published headce3510d).
PR #4 remains OPEN/DRAFT on its original plan/p2-dual-mode-matching branch from9636ee7; no rebase or
merge was performed. The earlier S1 checkpoint/receipt is historical, not the current data baseline.

PR #5 supplies the bounded private local ETL:1479 catalogue profiles,1435 exact-source approved/44
held draft,160 brands/420 notes/11972 ordered links, all12448 raw occurrences retained. Matching
eligibility remains0. Its98/98 tests establish ETL/schema evidence, not matching/API/UI acceptance.
No observed accord labels/strengths, selected family/lifecycle/market facts or accepted matching
completeness/absence policy is supplied by that adapter. Real A/B1 eligibility still requires review;
both real B2 methods lack inputs. Source permission and private scope do not widen with catalogue count.

[[P2_Post_PR5_Matching_Reconciliation]] is the current capability/gate and DM compatibility crosswalk.
PR #3 acquisition/evidence/partial-profile design is merged upstream context; its historical pending
status is superseded by the merge, while DM-01..07 weights/thresholds and application decisions remain
PROPOSED. Keep PR #3's evidence-graph/structural-search decomposition distinct from this plan's
perfume-reference/custom-query modes. Both separate structural fit from confidence/direct evidence.
Legacy40/25/15/20 blended examples remain historical drafts, not this proposal's accepted formula.

## Scope, traceability and task map

| Major topic / numbered subtasks | Requirements | Deliverable | Responsible role |
|---|---|---|---|
| 1. Contract: 1.1 two modes; 1.2 versions/weights; 1.3 missing data | R03/R05/R07/R16/R18 | [[Dual_Mode_Matching_Architecture]] | Planner now; owner approves |
| 2. Inputs: 2.1 identity/aliases; 2.2 notes/accords/families; 2.3 source/evidence gates | R01/R03/R06/R17/R21 | [[Dual_Mode_Matching_Data_Contract]] | Planner; later data implementer/reviewer |
| 3. UX: 3.1 A flow; 3.2 B1/B2 builder; 3.3 compare/share/accessibility | R04/R08/R13/R14/R15 | [[Dual_Mode_Scent_Search_UX]] | Planner; later UX implementer |
| 4. Verification: 4.1 formula oracles; 4.2 privacy/revocation; 4.3 scale | R16/R18/R21 | [[Dual_Mode_Matching_Acceptance_Tests]] | Later test implementer + independent reviewer |
| 5. Delivery: 5.1 dependency DAG; 5.2 owner ADR; 5.3 overlap/checks/receipt | Governance | This plan, [[Dual_Mode_Matching_Decisions]], task/evidence/handoff | Codex docs; human merges |

Owner-confirmed intent extends R05 from Designer/Niche references to any eligible perfume, and R14
single-note lookup to a multi-note/accord builder. Existing Rxx statuses are not silently changed;
new mechanics/weights/thresholds remain proposed extensions. Brand origin, alternative/reference role,
retail price and popularity are filters or explicitly separate sorts, never scent coefficients.
My Cart remains a private saved list with manual purchase status; no commerce flow changes.

## Product requirements and missing-data policy

- A accepts any visible catalogue identity for selection, including historical references; unavailable
  score inputs yield an insufficiency state, not invented metadata. Candidates exclude the same ID.
- B1 selects reviewed canonical notes by top/heart/base or explicit Any Layer, with must/prefer/exclude
  rules. B2 uses independent user-preference sliders; their units are not ingredient concentrations.
- Similarity/fit, data confidence, pairwise evidence and rating/popularity have separate fields and UI.
  No high percentage automatically creates a Dupe/Inspired By relation or a subjective wear claim.
- Unknown is not zero. Missing layers, incomplete lists, scale incompatibility, aliases, duplicates,
  unresolved source conflicts and absence of usable rights have explicit outcomes in the data contract.
- Current-first is a default **grouping**, not a declaration that unknown means available. Show verified
  current/in-market candidates first, unknown status next with a label; historical candidates require
  Include Historical. Strict availability excludes unknown with a visible explanation. References may
  remain historical. Status is market/time-specific; launch year and retailer stock do not prove lifecycle.
- Notes, flat-profile and accord fallback results occupy labeled method/coverage groups; a sparse 100
  must not outrank a well-supported result through hidden weight redistribution. No cross-method score
  comparison in one undifferentiated ranking. Missing assets use placeholders without blocking a score.

## Future implementation units and gates

IDs use IMP-MATCH-* to avoid PR #3's IMP-P2-01..05. Every unit below is NOT STARTED, requires this
Planning PR owner-merged SHA and a separate implementation branch/PR with independent code review.

| Unit | Reviewable behavior / exit evidence | Dependencies |
|---|---|---|
| IMP-MATCH-01 | Read-only authorized profile adapter; alias/identity/coverage audit and canonical input contract | This plan Gate P; PR #5 ETL merged; audit private scope,44 holds, eligibility/completeness and use-specific rights |
| IMP-MATCH-02 | Pure deterministic A scorer + golden/property tests + explanations | 01; accepted DM-01..04; no production service |
| IMP-MATCH-03 | B1 note query normalization/hard rules + oracle/unknown tests | 01; DM-05; reusable math utilities from 02 where appropriate |
| IMP-MATCH-04 | B2 numeric and presence fallback scorers; reject incompatible strengths | This Gate P; 01; DM-04/05; real numeric mode needs compatible observed scales, real presence mode needs reviewed labels and closure; current real cohort supports neither; synthetic scorer tests remain distinct |
| IMP-MATCH-05 | Scoped read-only search API/candidate retrieval/pagination/cache revocation | 02/03/04 for enabled routes; DB/API isolation and bounds tests; disable unavailable routes |
| IMP-MATCH-06 | A/B1/B2 screens and compare explanations, keyboard/mobile/placeholder tests | 05 and explicit app-stack decision; rights-approved imagery optional |
| IMP-MATCH-07 | Authorized 12 then 1,479 plus synthetic 10k performance/relevance audit | Enabled 05/06 paths; measured data coverage; no N-squared precompute |

PR #3 and PR #5 are now merged; the ETL prerequisite is satisfied within its bounded private local
scope. This plan's Gate P, eligible-input/completeness review and source-specific use checks remain.
Broad regional ingestion and images need not block a later authorized notes-only milestone. All
matching_eligible flags stay false until an explicitly scoped implementation establishes that contract.
Indices/schema changes require gap review within approved implementation scope; persisted custom
queries require a separate amendment if they expand the agreed design. No existing migration rewrite.

## Alternatives, rollout and owner acceptance

Prefer an independently specified structural weighted-set model with visible confidence. Reject
evidence-blended percentages as the default structural label; a later recommendation rank needs its
own policy/version. Cosine, inferred accord intensity, fuzzy note-family substitution and cross-layer
partial credit are deferred, not interchangeable formulas under one version. SQL-vs-application scoring
and web stack remain owner decisions; no provider commitment or new dependency is made here.

After Gate P, release behind separate A/B1/B2 capability flags: internal fixtures, licensed local pilot,
then user review. Rollback disables affected route/version and invalidates its scoped cache; retain
source claims and old versions. A failed numeric-accord gate must not disable note search. Weight
changes require recorded owner review/version change and regression comparison, never online training.

Owner checklist: review DM-01..07 in [[Dual_Mode_Matching_Decisions]], formula oracles, data gaps,
hard-filter unknown handling, current-first grouping and privacy/share contract. All implementation
acceptance tests are specifications / NOT RUN. Planning review readiness is documented in
[[DPT-PLAN-003_Documentation_Evidence]]; it is not owner acceptance or feature completion.

## Navigation and evidence

[[DPT-PLAN-003_Dual_Mode_Matching]], [[Dual_Mode_Matching_Architecture]],
[[Dual_Mode_Matching_Data_Contract]], [[Dual_Mode_Scent_Search_UX]],
[[Dual_Mode_Matching_Acceptance_Tests]], [[DPT-PLAN-003_Dual_Mode_Matching_Handoff]].
Existing context: [[Scent_Matching_Spec]], [[Review_Evidence_and_Confidence]],
[[Matching_Test_Cases]], [[P1_Pilot_Implementation_Plan]], [[Data_Dictionary_Draft]].

Primary project evidence: [merged PR #2](https://github.com/kraveerachat/DoomParfum-By-TK/pull/2),
[merged PR #3](https://github.com/kraveerachat/DoomParfum-By-TK/pull/3),
[merged PR #5](https://github.com/kraveerachat/DoomParfum-By-TK/pull/5).
No external site/Fragrantica endpoint was accessed for this planning task. Handoff references to third-party
terms, pricing or feature internals are not treated as independently reverified facts or grants.
