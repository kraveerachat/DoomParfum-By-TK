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

## Verified baseline and parallel work

Fresh origin/main and merged PR #2: **9636ee740cdcd3d60633ac11745366814d1af05c**.
PR #2 head: 2e0c0611b17bf2b13840c305fa03a90c4066cf31; 47 domain tables and eight migrations are
implemented. Its recorded 79-test result is historical implementation evidence, not tests rerun here.
PR #3 is OPEN/DRAFT at inspected head **69255b0ec2d4bff61c0cc3f5707ba0bc00a16f16** on
plan/p2-focused-brand-discovery-automation. It owns catalogue acquisition, source permissions,
popularity and progressive enrichment. This plan branches independently from main on
plan/p2-dual-mode-matching. No implementation approval follows from either Draft PR.

Baseline README/matching examples mix evidence into a 40/25/15/20 composite called structural
similarity; some UX examples imply unverified real product facts. This proposal preserves that text
as legacy draft context and proposes a separate versioned structural model, data confidence and
pairwise evidence. PR #3 NEW-08 raises the same semantic issue; neither proposal accepts the other.
Its NEW-07..11 acquisition/evidence decisions remain for that workstream's Owner review.

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
| IMP-MATCH-01 | Read-only authorized profile adapter; alias/identity/coverage audit and canonical input contract | Gate P; merged PR #2; completed IMP-P1-02 baseline ETL and rights-approved mappings |
| IMP-MATCH-02 | Pure deterministic A scorer + golden/property tests + explanations | 01; accepted DM-01..04; no production service |
| IMP-MATCH-03 | B1 note query normalization/hard rules + oracle/unknown tests | 01; DM-05; reusable math utilities from 02 where appropriate |
| IMP-MATCH-04 | B2 numeric and presence fallback scorers; reject incompatible strengths | 01; DM-04/05; numeric mode blocked until compatible observed scales exist; presence pilot can proceed independently of numeric enrichment |
| IMP-MATCH-05 | Scoped read-only search API/candidate retrieval/pagination/cache revocation | 02/03/04 for enabled routes; DB/API isolation and bounds tests; disable unavailable routes |
| IMP-MATCH-06 | A/B1/B2 screens and compare explanations, keyboard/mobile/placeholder tests | 05 and explicit app-stack decision; rights-approved imagery optional |
| IMP-MATCH-07 | Authorized 12 then 1,479 plus synthetic 10k performance/relevance audit | Enabled 05/06 paths; measured data coverage; no N-squared precompute |

PR #3 does not have to merge before this Planning PR. Its merge is required only for implementing
behavior relying on its acquisition/status/role contracts; source-specific rights and actual data are
independent gates. Baseline licensed matching need not wait for broad regional ingestion or images.
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
[Draft PR #3](https://github.com/kraveerachat/DoomParfum-By-TK/pull/3).
No external site/Fragrantica endpoint was accessed for this planning task. Handoff references to third-party
terms, pricing or feature internals are not treated as independently reverified facts or grants.
