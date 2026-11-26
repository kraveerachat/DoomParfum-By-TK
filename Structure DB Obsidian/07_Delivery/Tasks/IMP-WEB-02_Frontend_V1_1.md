---
id: IMP-WEB-02
project: DoomParfum By TK
type: implementation_task
status: owner-review
owner: human-owner
updated: 2026-11-26
requirements: [R01, R03, R04, R13, R14, R21]
planning_pr: 37
tags: [doomparfum, implementation, frontend, localization, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 — Frontend V1.1 design upgrade

## Current Task

- Type: IMPLEMENTATION, mock only. Agent: Claude Code. Gate C of the Owner's A, B, C order.
- State: CP4 OWNER REVIEW PENDING. S1 completed CP0 to CP4 on the agent side; nothing is accepted. CP5 follows the Owner's answers.
- Branch `feat/frontend-v1-1-design-upgrade`, worktree `.local/worktrees/imp-web-02-frontend-v1-1`, starting SHA `3e87027fbdbbb016c148a84ca33775e64cccf3e0` (PR #37 merge, equal to remote `main`, verified 2026-11-26).
- Approved plan: [[DPT-PLAN-013_Frontend_V1_1_Amendment]] (PR #37, merged 2026-11-26T13:30:40Z), amending [[DPT-PLAN-012_Luxury_Frontend_Editorial]].
- Intake class B. ID check: no IMP-WEB-02 branch, PR or task note existed; the ID appeared only as the proposed name in the merged plan.
- Implementation PR: NOT CREATED. Publication needs fresh scoped Owner authorization.
- Production mutation allowed: NO.

## Goal / Why

Build the merged V1.1 contract: English and Thai, sticky header and language selector, gold–bronze tokens, R1–R5 rules, typography foundation, page refinements, Thai font specimen, and one Owner comparison batch.

## In Scope

`web/`, the local preview on `127.0.0.1:3000`, the project-local design-tool rule file, this task's vault records and evidence.

## Out of Scope / Do-not-touch

Database, matching, ETL, migrations, receipts, PR #8, U01/r14, PostgreSQL containers and volumes, other worktrees, global tool configuration, real data, API, authentication, deployment. The Proposal v2 file stays outside Git.

## Dependencies

PR #37 merged (verified). Owner authorization of 2026-11-26: implementation, worktree, bounded candidate-font download (V11-OD-11), project-local tool-rule update, local tests, Docker build and preview replacement.

## Acceptance Criteria + Evidence Needed

A01–A12 in both languages and V01–V16 of the amendment. CP5 (full verification, independent review, receipt) follows the Owner's CP4 answers.

## Task Map

CP0 baseline · CP1 foundation and specimen · CP2 routing spike, localization, header · CP3 pages · CP4 Owner batch · CP5 verification (after Owner answers).

## Session Register

| Session | Purpose | State | Result | Checkpoint SHA | Evidence |
|---|---|---|---|---|---|
| S1 | CP0–CP4 | CLOSED | CP4 REVIEW PENDING | code `733c59da80fb22f8164859d756f1f24c1bcd008f`; records commit follows | [[2026-11-26_IMP-WEB-02_S1_Report]] |

### Session S1 — CP0 to CP4

State: CLOSED. Agent: Claude Code, implementation. Started 2026-11-26. Intake class B. Plan, scope and do-not-touch: as above.

CP0 (main `3e87027`, V1 image `sha256:43be51f1…` restarted without rebuild): `npm ci` clean; `npm test` PASS 85 / FAIL 0; Chrome suite PASS 189 / FAIL 0. Before screenshots of five routes at 1920, 1440, 1024, 768 and 390px kept outside Git.

#### Session S1 result

- Work: CP1 tokens, rules, type and specimen; CP2 routing spike, two-language shell, overlay, sticky header and language control; CP3 page refinements and heading-focus modality; CP4 Owner packet. Details and every finding: [[2026-11-26_IMP-WEB-02_S1_Report]].
- Files: `web/` (69 files at the code checkpoint) and this task's vault records. Project-local untracked rule `.claude/rules/doomparfum-frontend-design-tools.md` updated as authorized.
- Tests on the final preview image `sha256:177c02e5e5b9f82b7920a3adaddd51ba8bdd7fc2a83c8771c5db4fec91537eaf`: unit PASS 116 / 0; Chrome PASS 242 / 0; Edge PASS 242 / 0; type check and lint exit 0; boundary scan clean; detector only V1-baseline findings.
- Not run: screen reader, physical phone, Safari, Firefox, forced colours and 400% zoom on new pages, clean-clone build, independent review (CP5).
- Decisions: none made by the agent; T1–T8 and V11-OD-03, 04, 08, 10 wait in [[IMP-WEB-02_CP4_Owner_Review]].
- Security and privacy: no cookie, storage, external request or new dependency; candidate fonts downloaded under V11-OD-11 into Git-ignored local tooling only.
- Git: code `733c59da80fb22f8164859d756f1f24c1bcd008f`; records commit follows. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`.
- Next: Owner answers the CP4 form; then CP5.

## Reports

| File | Session | SHA-256 (LF bytes) | Classification |
|---|---|---|---|
| [[2026-11-26_IMP-WEB-02_S1_Report]] | S1 | `5c4e1d4d0c7fa6860da88b5e050a1ee183cd84cbcc3851072d6d9c9cd89826da` | PUBLIC_SAFE |
| [[2026-11-26_IMP-WEB-02_S1_Summary]] | S1 | `775c73624eae13940c0361e4d723849311cdf172cf71f4bd356856f026fa38ea` | PUBLIC_SAFE |

Owner packet: [[IMP-WEB-02_CP4_Owner_Review]], [[IMP-WEB-02_Translation_Review]]. No receipt yet (after CP5).
