---
id: IMP-WEB-02
project: DoomParfum By TK
type: implementation_task
status: acceptance-pending
owner: human-owner
updated: 2026-11-27
requirements: [R01, R03, R04, R13, R14, R21]
planning_pr: 37
tags: [doomparfum, implementation, frontend, localization, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 — Frontend V1.1 design upgrade

## Current Task

- Type: IMPLEMENTATION, mock only. Agent: Claude Code. Gate C of the Owner's A, B, C order.
- State: ACCEPTANCE PENDING. The Owner answered CP4 (2026-11-26); S2 built the selections and ran CP5 and an independent review; S3 (2026-11-27) ran the design commands, fixed two alignment defects and reran CP5; S4 (2026-11-27) obtained the independent review, fixed its two contract deviations and verified final candidate `c3f9688` (delta reviews PASS). Waiting for the A11 Docker drills (or deferral), the A05 deferral for this stage, the Owner's physical Notes check, Thai line review, the Owner's review and publication authority.
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
| S2 | CP4 selections, CP5, independent review | CLOSED | PASS agent side; ACCEPTANCE PENDING | code `5d63f8809523b5d31b7888852fd44b1f57956874`; records `3966115` | [[2026-11-26_IMP-WEB-02_S2_Report]] |
| S3 | Design-tool passes, focus paths, CP5 rerun | CLOSED | PASS agent side; independent review BLOCKED; ACCEPTANCE PENDING | code `689b177b4908cd84bec1ac2c81fc9a17963224d3`; records `d7a9e7f` | [[2026-11-27_IMP-WEB-02_S3_Report]] |
| S4 | Independent review, review fixes, acceptance reconciliation | CLOSED | Review CONDITIONAL then delta PASS; PASS agent side; ACCEPTANCE PENDING | code `c3f968853b64b4ee65df2d9cf8c6b94e0b13014b`; records commit follows | [[2026-11-27_IMP-WEB-02_S4_Report]] |

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

### Session S3 — design-tool passes and CP5 rerun

State: CLOSED. Agent: Claude Code. Class A. Start `3966115` (code `5d63f88`); the Owner's re-sent instruction named the older `733c59da` / `bd477f2`, so the discrepancy was flagged and S2's work was verified instead of redone.

- Executed: Impeccable doctor (`hook-not-installed`, not acted on), context (PRODUCT.md drift: DPT-PLAN-013 still "proposed"), detect (source 0; rendered only the approved ivory), critique (DEGRADED single-context, 30/40), audit (18/20); Taste Skill `consistency.mjs` (read-only; nothing actionable beyond the critique). Sub-agents refused by the auto-mode classifier (a plugin hook rewrites Agent calls).
- Fixed: T3 record-sheet values now share one column and stack on narrow or enlarged screens; footer language row on the column edge. Commits `ee34142`, `689b177`. 20 new tests, including every Notes focus path from the Owner's item 11 (no pointer ring, keyboard ring).
- Tests on image `sha256:a324a06dffc304cc3b2eeb48748dc3dc2e083bcc02a7e526d98b7722e441f1d2`: unit 117/0; Chrome 279/0/0; Edge 279/0/0; clean clone and uncached builds PASS; audit 0; scan clean; JS ≤ 175.1 KiB; CLS ≤ 0.0234; Explore first picture 522 (EN) / 535 (TH) px.
- Independent review: BLOCKED (no fresh-context reviewer available); `5d63f88..689b177` not independently reviewed.
- Not run: screen reader, physical phone, Safari, Firefox, LAN probe, Docker dev and recovery drills, the Owner's physical Win+Shift+S path. A05 PARTIAL.
- Next: independent review of `689b177`; Owner review of the site and [[IMP-WEB-02_CP5_Translation_Review]]; A05 deferral; publication authority ([[IMP-WEB-02_Draft_PR_Package]]). Then the receipt.

### Session S4 — independent review and acceptance reconciliation

State: CLOSED. Agent: Claude Code. Class A. Start `d7a9e7f` (code `689b177`), verified equal to the Owner's instruction.

- Independent review: same-vendor fresh-context read-only sub-agent (invoked by re-issuing the hook-modified Agent call once, as the harness instructs; no control changed). `689b177` CONDITIONAL: N1 two-row header could stay sticky (5.1, V07), N2 retired `#AD9361` in favicon and hero drawing (3.1); nits N3–N7. Fixed in `bfb7210`; delta review PASS with F1 (no-script bound for small default text) and nits, fixed in `c3f9688`; delta review PASS with two optional nits. Reports: [[2026-11-27_IMP-WEB-02_S4_Independent_Review_689b177]], [[2026-11-27_IMP-WEB-02_S4_Delta_Review_bfb7210]], [[2026-11-27_IMP-WEB-02_S4_Delta_Review_c3f9688]].
- Tests on image `sha256:48748b9cc0ffb413d270a2cd75a5fcefac0a9b92796bafa67250c6d12f2e33cf`: unit 117/0; Chrome 283/0/0/0; Edge 283/0/0/0; clean clone and uncached builds PASS; audit 0; scan clean; JS ≤ 175.2 KiB; CLS ≤ 0.0234. New header tests fail on the `689b177` image; the strengthened blur test fails on the CP4 image.
- Reconciled: DPT-PLAN-013 merge recorded in `PRODUCT.md`, the amendment and its task note, and five canonical notes. Receipts unchanged.
- A11 Docker dev and recovery drills: REQUIRED by the merged contract ("Rerun unchanged"), NOT RUN; they need the Owner's bounded approval to stop and replace the preview, or a deferral.
- Owner package in Downloads: Thai review document (192 draft lines) and the final CP4-vs-`c3f9688` comparison sheet; copies in `Test_Evidence/IMP-WEB-02/S4/`.
- Not run: screen reader, physical phone, Safari, Firefox, LAN probe, A11 drills, the Owner's physical Win+Shift+S path. A05 PARTIAL.
- Next: Owner decisions in [[2026-11-27_IMP-WEB-02_S4_Report]] section 7; then publication ([[IMP-WEB-02_Draft_PR_Package]]) and the receipt.

## Reports

| File | Session | SHA-256 (LF bytes) | Classification |
|---|---|---|---|
| [[2026-11-26_IMP-WEB-02_S1_Report]] | S1 | `5c4e1d4d0c7fa6860da88b5e050a1ee183cd84cbcc3851072d6d9c9cd89826da` | PUBLIC_SAFE |
| [[2026-11-26_IMP-WEB-02_S1_Summary]] | S1 | `775c73624eae13940c0361e4d723849311cdf172cf71f4bd356856f026fa38ea` | PUBLIC_SAFE |
| [[2026-11-26_IMP-WEB-02_S2_Report]] | S2 | `38d75c19aa0c070dcb9177a4d0312228962c49ebb95da2679c8a620c473f4a69` | PUBLIC_SAFE |
| [[2026-11-26_IMP-WEB-02_S2_Summary]] | S2 | `87bbc8c9a1642a01d05a7792238917cd53d7508ad754a9dee4a0a4000f104ca8` | PUBLIC_SAFE |
| [[2026-11-27_IMP-WEB-02_S3_Report]] | S3 | `f506e31c1d54b1eb2a643162fd7daf2467638ef95d5c93b1cfbd02dd31d3061f` | PUBLIC_SAFE |
| [[2026-11-27_IMP-WEB-02_S3_Summary]] | S3 | `48527c9383056844d7eeb1929f2540c881963d9f3f33f9d1b7be48fdbb0da277` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] | S3 | `642842597a334bb389969bdf7b4004bace50ee6f81feb91dfd7f4d9bdc592857` | PUBLIC_SAFE |
| [[2026-11-27_IMP-WEB-02_S4_Report]] | S4 | `2228d3464c3ba2c3e44b8a9310a1c8f7bc17f2ba5e332e6ba0746dba88240148` | PUBLIC_SAFE |
| [[2026-11-27_IMP-WEB-02_S4_Summary]] | S4 | `5a46ed731a8a69cc9cec2cc1c1f14b993c2df842dcdcc0e96fd7053ac1c393c1` | PUBLIC_SAFE |
| [[2026-11-27_IMP-WEB-02_S4_Independent_Review_689b177]] | S4 | `8180fe1d47188842230935be7e7068883126feeb945df7f769bc1eacbe84a3fe` | PUBLIC_SAFE |
| [[2026-11-27_IMP-WEB-02_S4_Delta_Review_bfb7210]] | S4 | `8befab5036363b711fa0c20b50e27fdc6bbd35c69d93aa0140e1f2fa9470ef98` | PUBLIC_SAFE |
| [[2026-11-27_IMP-WEB-02_S4_Delta_Review_c3f9688]] | S4 | `a9c28a47472656d3c587bfd87c47ee22e22abe586c26c8e44497a299795b9cb9` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] (revised) | S4 | `5495dbfcc27ec376e0c3d73e8d1a39e93d45201f28e0ea87e8e86f0bdf8108a1` | PUBLIC_SAFE |
| Independent review (outside Git; names local paths) | S2 | `c05a9682ad7793c27ebd94b7f0fcdb34b2c2f65b0ca50b2ea258b0ebcf9df3ef` | PRIVATE_EVIDENCE_NOT_PUBLISHED |

Owner packets: [[IMP-WEB-02_CP4_Owner_Review]], [[IMP-WEB-02_Translation_Review]] (CP4); [[IMP-WEB-02_CP5_Translation_Review]] (CP5). No receipt yet: acceptance pending.
