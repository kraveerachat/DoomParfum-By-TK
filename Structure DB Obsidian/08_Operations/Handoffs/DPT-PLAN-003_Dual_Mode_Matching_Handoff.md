---
id: DPT-PLAN-003-HANDOFF
project: DoomParfum By TK
type: continuity_handoff
status: proposed
owner: human-owner
updated: 2026-11-11
tags: [doomparfum, handoff, matching]
source_of_truth: "../../../README.md"
---

# DPT-PLAN-003 — Matching Planning Continuity

Read AGENTS.md, DEVELOPMENT_WORKFLOW.md, root/vault README, this task and the live Planning PR first.
Branch plan/p2-dual-mode-matching; base9636ee740cdcd3d60633ac11745366814d1af05c after owner-merged PR #2.
PR number/head/publication state are recorded in [[DPT-PLAN-003_Dual_Mode_Matching]] and live GitHub;
do not infer merge from a review-ready receipt. Human Owner Gate P for this feature remains PENDING.

## Delivered planning scope

[[P2_Dual_Mode_Scent_Matching_Plan]] is the canonical plan; [[Dual_Mode_Matching_Architecture]]
specifies deterministic A/B1/B2 formulas, null/missing cases, ordering/coverage/confidence/evidence and
bounded read-only architecture. [[Dual_Mode_Matching_Data_Contract]] reconciles47 existing tables:
matching_results requires a relation, so no persisted custom query/fake perfume is proposed. Accord
strengths require observed compatible scales. [[Dual_Mode_Scent_Search_UX]],
[[Dual_Mode_Matching_Acceptance_Tests]] and [[Dual_Mode_Matching_Decisions]] contain UX/tests and DM-01..07.
No runtime/SQL/API/UI/ETL/scraper/AI dependency/cloud/production changes. All feature tests NOT RUN.

## Parallel work and remaining decisions

PR #3 Brand Research at inspected69255b0ec2d4bff61c0cc3f5707ba0bc00a16f16 is separate OPEN/DRAFT;
do not edit it. Re-fetch before owner merge: its NEW-08/09/11 can affect score naming, sparse profile
eligibility and pair evidence. Dedicated matching files avoid its acquisition artifacts; shared-file
navigation addenda have explicit overlap evidence in [[DPT-PLAN-003_Documentation_Evidence]].
Do not combine PR #3 research cohort12/11/46/84 with P1 approved pilot12/5/58/93 without manifest audit.

Owner still chooses DM weights/naming/thresholds, accord fallback/scale policy, B hard-rule unknown
behavior, currentness grouping and implementation choices. Source/asset rights are separate gates.
OD-01..06 and all historical immutable receipts remain unchanged. Only one new receipt for this task
is created when planning review-ready; never amend that receipt for later publication/merge events.

## Exact next action / future agent bootstrap

Human Owner reviews the new Draft Planning PR; no automated implementation. After owner merge,
verify actual approved SHA and IMP-P1-02 data/rights readiness, then propose/start the approved
IMP-MATCH-* unit in a distinct implementation branch/PR. Do not reuse PR #3's IMP-P2-* task IDs.
Images, regional inputs, persisted queries and hosting remain gated independently.

TOOL RECOMMENDATION: existing GitHub/Git/Python/PostgreSQL tools for the appropriate future task;
no installer/AI service required. Planner/reviewer reads specs; implementer waits for verified Gate P.
PRODUCTION_MUTATION_ALLOWED=NO. HUMAN_MERGE_REQUIRED=YES. No Fragrantica scrape/internal endpoints.

If continuing this planning task: recheck current task/PR/head, read documentation evidence, keep changes
on the same planning branch, update logs and validate docs; do not recreate a receipt or claim runtime
tests from arithmetic checks. Current tool usage/verification/limitations are in the task/evidence.
