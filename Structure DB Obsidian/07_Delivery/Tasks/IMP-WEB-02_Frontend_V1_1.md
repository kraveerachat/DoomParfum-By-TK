---
id: IMP-WEB-02
project: DoomParfum By TK
type: implementation_task
status: acceptance-pending
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
- State: ACCEPTANCE PENDING. The Owner answered CP4 (2026-11-26); S2 built the selections and ran CP5 and an independent review. Waiting for the Owner's review, the A05 deferral for this stage and publication authority.
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
| S1 | CP0–CP4 | CLOSED | CP4 answered by the Owner | code `733c59da80fb22f8164859d756f1f24c1bcd008f`; records `bd477f2` | [[2026-11-26_IMP-WEB-02_S1_Report]] |
| S2 | CP4 selections, CP5, independent review | CLOSED | PASS agent side; ACCEPTANCE PENDING | code `5d63f8809523b5d31b7888852fd44b1f57956874`; records commit follows | [[2026-11-26_IMP-WEB-02_S2_Report]] |

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

### Session S2 — CP4 selections and CP5

State: CLOSED. Agent: Claude Code. Class A. Start `bd477f2`.

- Owner decisions (chat, 2026-11-26): T1 Fahkwang 300; T2 C centred hero; T3 B record sheet; T4 B compact toolbar; T5 A stable header; T6 A compact link; T7 A equal columns; T8 B square corners; BY TK 11px; Thai terminology ท็อปโน้ต / ฮาร์ตโน้ต / เบสโน้ต, โน้ตทั่วไป, ตระกูลกลิ่น, แอคคอร์ด, โครงสร้างกลิ่น 3 ระดับ, สำรวจตามตระกูลกลิ่น, เกี่ยวกับเรา, ไม่ได้ระบุ, ไม่มีรายการ; fictional names, family and accord labels unchanged; Paper study L unchanged. The direction is approved; each Thai line stays draft.
- Work, fixes, tools, tests and limits: [[2026-11-26_IMP-WEB-02_S2_Report]]. Final candidate `5d63f8809523b5d31b7888852fd44b1f57956874`; preview `sha256:3a155e442df0f172604a68a44ba55e81a61684e0ca032756f0f07e407a97ca90`.
- Tests: unit 117/0; Chrome 259/0; Edge 259/0; clean clone and uncached image builds PASS; audit 0; scans clean.
- Independent review: same-vendor fresh sub-agent, CONDITIONAL; blockers fixed and retested; report SHA-256 `c05a9682ad7793c27ebd94b7f0fcdb34b2c2f65b0ca50b2ea258b0ebcf9df3ef` kept outside Git.
- Not run: screen reader, physical phone, Safari, Firefox, LAN probe, Docker dev and recovery drills. A05 PARTIAL.
- Next: Owner review of the site and [[IMP-WEB-02_CP5_Translation_Review]]; Owner deferral of the A05 manual checks for this stage; publication authority. Then the receipt and Draft PR.

## Reports

| File | Session | SHA-256 (LF bytes) | Classification |
|---|---|---|---|
| [[2026-11-26_IMP-WEB-02_S1_Report]] | S1 | `5c4e1d4d0c7fa6860da88b5e050a1ee183cd84cbcc3851072d6d9c9cd89826da` | PUBLIC_SAFE |
| [[2026-11-26_IMP-WEB-02_S1_Summary]] | S1 | `775c73624eae13940c0361e4d723849311cdf172cf71f4bd356856f026fa38ea` | PUBLIC_SAFE |

| [[2026-11-26_IMP-WEB-02_S2_Report]] | S2 | `38d75c19aa0c070dcb9177a4d0312228962c49ebb95da2679c8a620c473f4a69` | PUBLIC_SAFE |
| [[2026-11-26_IMP-WEB-02_S2_Summary]] | S2 | `87bbc8c9a1642a01d05a7792238917cd53d7508ad754a9dee4a0a4000f104ca8` | PUBLIC_SAFE |
| Independent review (outside Git; names local paths) | S2 | `c05a9682ad7793c27ebd94b7f0fcdb34b2c2f65b0ca50b2ea258b0ebcf9df3ef` | PRIVATE_EVIDENCE_NOT_PUBLISHED |

Owner packets: [[IMP-WEB-02_CP4_Owner_Review]], [[IMP-WEB-02_Translation_Review]] (CP4); [[IMP-WEB-02_CP5_Translation_Review]] (CP5). No receipt yet: acceptance pending.
