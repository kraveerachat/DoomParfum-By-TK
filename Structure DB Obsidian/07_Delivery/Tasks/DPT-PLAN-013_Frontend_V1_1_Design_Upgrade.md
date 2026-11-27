---
id: DPT-PLAN-013
project: DoomParfum By TK
type: task
status: merged
owner: human-owner
updated: 2026-11-27
requirements: [R01, R03, R04, R13, R14, R21]
tags: [doomparfum, planning, planning-amendment, frontend, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# DPT-PLAN-013 — Frontend V1.1 design upgrade planning amendment

## Current Task

- Type: PLANNING AMENDMENT, documentation only. Agent: Claude Code. Gate B of the Owner's A, B, C order.
- State: agent side ready for Owner review. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED` / `AGENT_CREDENTIAL_REQUIRED`.
- Branch `plan/frontend-v1-1-design-upgrade`, base and starting SHA `ab3351a8432d1d6664a6b4281784cfea56b0b9fa` (PR #36 merge, equal to remote `main`).
- Amends [[DPT-PLAN-012_Luxury_Frontend_Editorial]] (PR #35) after [[IMP-WEB-01_Luxury_Frontend_Docker]] (PR #36, MERGED).
- Intake class C. ID check: no DPT-PLAN-013 or IMP-WEB-02 on any fetched ref or pull request.
- Production mutation allowed: NO.

## Goal / Why

One reviewable contract for the V1.1 upgrade, because localization, sticky navigation and typography change the approved V1 contract.

## In Scope

[[DPT-PLAN-013_Frontend_V1_1_Amendment]], pointers in the affected contracts, status and decision records, a Draft PR text.

## Out of Scope

Application code, fonts, dependencies, containers, the font specimen, translations beyond a draft glossary, publication, Gate C.

## Dependencies

PR #36 merged (verified). Proposal v2 file present (verified by hash). Owner master instruction (recovered from the local session record).

## Safety / Do-not-touch

`web/`, Docker preview and resources, PostgreSQL containers and volumes, database, matching, ETL, PR #8, Security U01/r14, earlier reports, evidence and receipts, other worktrees, the primary checkout.

## Acceptance Criteria + Evidence Needed

KEEP, CHANGE and TEST boundaries explicit; every proposal section traced; superseded clauses listed; task map and criteria present; no font decision; documentation checks pass; `web/` unchanged.

## Task Map

1. Verify merge and inputs. 2. Measure the facts the plan depends on. 3. Write the amendment. 4. Update contracts and records. 5. Validate, checkpoint, prepare publication.

## Session Register

| Session | Purpose | State | Result | Checkpoint SHA | Evidence |
|---|---|---|---|---|---|
| S1 | Gate B amendment packet | CLOSED | PASS, agent side | Specification `49fb8c87f27e6430ee0c262a0660239706c96d0d`; records commit in Git and the PR | [[2026-11-26_DPT-PLAN-013_S1_Report]] |

### Session S1 — Gate B amendment

State: CLOSED. Agent: Claude Code, planning. Started 2026-11-26. Class C. Plan, changes, checks and limits: the S1 report. Decisions: [[Decision_Log]]. Security and privacy: documentation only; public repository; proposal text kept outside Git (V11-OD-12).

## Planned / Completed / Remaining

Completed: items 1 to 5 locally. Remaining: Owner publication authorization, Draft PR, Owner review and merge, then Gate C.

## Test / Evidence Ledger

| Check | Result |
|---|---|
| Documentation checks | See the S1 report |
| V1 measurements | [DPT-PLAN-013_V1_Baseline.json](../../08_Operations/Test_Evidence/DPT-PLAN-013/DPT-PLAN-013_V1_Baseline.json) |
| V01 to V16, A01 to A12 rerun, font specimen | NOT RUN (Gate C) |
| Independent review of this plan | NOT RUN |

## Reports

| File | Session | SHA-256 (LF bytes) | Classification |
|---|---|---|---|
| [[2026-11-26_DPT-PLAN-013_S1_Report]] | S1 | `0e037f9db5cc06b4e3336c07f3958400a1a76b9244bfd58687a14b79145bedaf` | PUBLIC_SAFE |
| [[2026-11-26_DPT-PLAN-013_S1_Summary]] | S1 | `daa658cd0abfded547488d47f0dc1e36a82c1123a223260b6cf69b2954c8f068` | PUBLIC_SAFE |

Receipt: [[2026-11-26_020413_DPT-PLAN-013_Frontend_V1_1_Planning]].

## Issues / Risks / Known Limitations

The CP2 routing approach is unproven. The doubled Explore rule is not reproduced. The untracked local design-tool rule file still names V1 token values. No independent reviewer.

## Latest Git Checkpoint / SHA

Local commits on the branch above; exact SHAs in Git, the receipt (source checkpoint) and the Owner handoff.

## Handoff / Next Action

Owner: authorize one push and one Draft PR with [[DPT-PLAN-013_Draft_PR_Description]]; then review and merge. After a verified merge, Gate C intake allocates the implementation task.

Post-merge (recorded 2026-11-27): PR #37 MERGED 2026-11-26 as `3e87027fbdbbb016c148a84ca33775e64cccf3e0` (verified equal to remote `main`). Gate B is closed; Gate C was allocated as [[IMP-WEB-02_Frontend_V1_1]]. The receipt and reports above are unchanged; earlier pre-merge statements are historical.
