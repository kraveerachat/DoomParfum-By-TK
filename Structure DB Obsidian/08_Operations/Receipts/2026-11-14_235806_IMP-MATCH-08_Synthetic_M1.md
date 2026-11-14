---
id: IMP-MATCH-08-RECEIPT
project: DoomParfum By TK
type: implementation_receipt
status: agent-review-ready
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, synthetic, matching, receipt]
source_of_truth: "../../../README.md"
---

# IMP-MATCH-08 — immutable synthetic M1 agent-readiness receipt

TASK_ID: IMP-MATCH-08. TYPE: implementation. PURPOSE: exact synthetic notes-layered M1 only.
CREATED_AT_UTC: 2026-11-14T16:58:06.985123+00:00. TIMEZONE: Asia/Bangkok; local date 2026-11-14.
APPROVED_PLAN_PR: #4 plus merged method-contract/unlock plans in PR13/25; merged plan authority is
separate from the explicit Human Owner exact-contract approval recorded2026-11-14 Asia/Bangkok.
APPROVED_PLAN_SHA / BASE_SHA: 0da217671ec6473716eea5947f013d44e6fd91cb.
ACCEPTED_CONTRACT: M1-NL-TYPED-1 SHA-256 a57f4c56e1068a3d86a99e562b31e5c3923e2d369cb4e812c1dd5f5550a5ada3.
METHOD/CONFIG: mc-a-notes-layered-p1 / m1-nl-typed-config-1.
BRANCH: codex/imp-match-08-synthetic-m1. FINAL_REVIEW_SHA: 207d18a2740c56c10dddfc8b1fbd35da3b2b097e.
PUBLICATION_HEAD_AT_RECEIPT: 3b7421dba12db05691b80c69668b9fb3dc94f35f; later closeout commit adds only this
receipt/docs/evidence. Exact final published HEAD belongs to the PR/task checkpoint registry,
not a self-referential rewrite of this immutable receipt.
PR_URL: https://github.com/kraveerachat/DoomParfum-By-TK/pull/26. PR_STATE_AT_RECEIPT: OPEN / DRAFT, not merged.

## Implemented scope and decisions

One pure typed Python entry point with exact frozen schemas, mandatory approved configuration,
bounded synthetic UUID/vocabulary/lineage inputs, strict type/count/bit validation and fixed errors.
Exact set Jaccard per layer, weights1/4,3/8,3/8,minimum2 comparable layers, rational fit and separate
coverage/support. Missing/incomplete/domain/empty states remain distinct. Partitioned results use
exact-before-rounded scores and canonical ID ties; explanations omit full note lists and keep
Data Confidence/pair evidence separate. No hidden defaults, method fallback or external service.
The five preparation documents and approved contract remain byte-for-byte unchanged. Their old
pending text is historical; [[M1_Exact_Owner_Acceptance]] records the separate explicit approval.

## Actual tests, negative controls and independent review

Actual RED:43setup failures because scorer module absent; feature bodies did not execute then.
Actual shape-negative RED:49methods,1AttributeError. Targeted validation correction returns bounded
ValueError for malformed missing-field exact objects. Original logs/source snapshots remain preserved.
Focused45+bounded-property4=49/49 PASS,0failures/errors/skips,1.3121663999918383s.
Coordinator combined111/111 PASS,0failures/errors/skips,1.9161620999802835s: existing62 plus new49.
Independent reviewer /root/m1_independent_review read all397runtime lines and both test files at
FINAL_REVIEW_SHA, completed167/167 review assertions,0findings, reran111/111 PASS in2.0721475999744143s,
and separately executed49layer-state pairs/13negative probes. Property examples4096complete pairs,
250seeded pairs,24permutations and5unsupported configs are internal cases, not additional methods.
Review completed 2026-11-14T16:52:15.709474+00:00 before this receipt. Public report SHA-256 25ffc4c0043bb392f479168df16168256b97cd9d229c484c83c31ae0f7a23936.

Commands: python .local/m1-implementation/run_regressions.py (ignored coordinator runner);
python .local/m1-independent-review/run_review.py (ignored independent runner).
Portable focused command: python -m unittest discover -s matching_math/tests -p "test_synthetic_m1*.py" -v.
The guide documents equivalent existing offline component commands. Public m1_* reports bind exact
source/test bytes and actual results. Python3.11.9; no Hypothesis installation, bounded stdlib properties.
Negative cases include unknown/known-zero/empty, incomplete pyramids, insufficient layers, wrong method/
config/types/subclasses, bad UUID/vocabulary/fingerprint/lineage, bounds, numeric precision and ordering.
Existing53protected source/governance blobs,21oldreceipts,8migrations and5preparation files preserved.
Documentation/frontmatter/local/Wiki links,47-table ERD/dictionary/schema parity, diff and common-secret
patterns are checked in the final documentation report; no exhaustive scanner or URL/rendering claim.

## Security, source rights and Production

DB_CALLS=0; NETWORK_CALLS=0 for scorer/tests. PRODUCTION_MUTATION=NO. AGENT_MERGE=NO.
No Full Mode A/B1/B2, API/UI, transport/8KiB parser, DB/SQL mutation, real-data ranking, source/image
acquisition, normalization promotion, 44-hold release, eligibility change, cloud or app-session change.
Fixture metadata is caller-declared and does not establish real rights, closure, authenticity or
authorization. Structural fit percentages are display values, not measured smell similarity.
PR8 historical timestamp evidence/guards stay unchanged and blocked; no equivalent experiment/fix.

## Limits and next Owner action

This receipt records agent readiness for the exact approved synthetic M1 milestone only. It does
not close the old full Mode A task or assert real-data/API/DB/security/publication acceptance.
Live RLS, replay/recovery, transport, UI and performance/SLA tests NOT RUN. Current DB counts/rights
at now NOT REVALIDATED. No new source/image rights. B1 exact contract and80/20 remain separate.
REVIEW_READINESS: READY FOR HUMAN OWNER REVIEW; PR remains OPEN/DRAFT. Human Owner alone accepts
implementation and merges. After any Owner merge, append facts to task/logs; never rewrite this receipt.

## Obsidian and exact changed files

[[IMP-MATCH-08_Synthetic_M1]], [[IMP-MATCH-08_Synthetic_M1_Evidence]], [[Synthetic_M1_Implementation]],
[[M1_Exact_Owner_Acceptance]], additive decision/task/status/index/roadmap/backlog/change/run records,
and preserved preparation annexes are included below. This receipt is the sole new receipt.

- `Structure DB Obsidian/00_Home/Project_Index.md`
- `Structure DB Obsidian/00_Home/Project_Status.md`
- `Structure DB Obsidian/03_Data/M1_Parallel_Data_Readiness_Checkpoint.md`
- `Structure DB Obsidian/04_Matching/M1_Next_B1_Owner_Packet.md`
- `Structure DB Obsidian/04_Matching/M1_Notes_Layered_Typed_Contract.md`
- `Structure DB Obsidian/04_Matching/Synthetic_Implementation_Unlock_Checklist.md`
- `Structure DB Obsidian/04_Matching/Synthetic_M1_Implementation.md`
- `Structure DB Obsidian/06_Engineering/Matching_Owner_Decision_Register.md`
- `Structure DB Obsidian/07_Delivery/Backlog.md`
- `Structure DB Obsidian/07_Delivery/Roadmap.md`
- `Structure DB Obsidian/07_Delivery/Tasks/IMP-MATCH-08_Synthetic_M1.md`
- `Structure DB Obsidian/07_Delivery/Tasks/M1_Contract_Preparation.md`
- `Structure DB Obsidian/08_Operations/Agent_Run_Log.md`
- `Structure DB Obsidian/08_Operations/Change_Log.md`
- `Structure DB Obsidian/08_Operations/Decision_Log.md`
- `Structure DB Obsidian/08_Operations/M1_Exact_Owner_Acceptance.md`
- `Structure DB Obsidian/08_Operations/M1_Preparation_Preflight_and_Gate.md`
- `Structure DB Obsidian/08_Operations/Next_Wave_Owner_Decision_Form.md`
- `Structure DB Obsidian/08_Operations/Receipts/2026-11-14_235806_IMP-MATCH-08_Synthetic_M1.md`
- `Structure DB Obsidian/08_Operations/Test_Evidence/IMP-MATCH-08_Synthetic_M1_Evidence.md`
- `matching_math/README.md`
- `matching_math/evidence/m1_documentation_checks.json`
- `matching_math/evidence/m1_file_manifest.json`
- `matching_math/evidence/m1_focused_results.json`
- `matching_math/evidence/m1_independent_review.json`
- `matching_math/evidence/m1_owner_contract.json`
- `matching_math/evidence/m1_red_results.json`
- `matching_math/evidence/m1_regression_results.json`
- `matching_math/evidence/m1_shape_red_results.json`
- `matching_math/synthetic_m1.py`
- `matching_math/tests/test_synthetic_m1.py`
- `matching_math/tests/test_synthetic_m1_properties.py`
