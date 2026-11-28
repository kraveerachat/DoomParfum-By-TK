---
id: IMP-WEB-02
project: DoomParfum By TK
type: implementation_task
status: agent-verified-human-review-pending
owner: human-owner
updated: 2026-11-28
requirements: [R01, R03, R04, R13, R14, R21]
planning_pr: 37
tags: [doomparfum, implementation, frontend, localization, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 — Frontend V1.1 design upgrade

## Current Task

- Type: IMPLEMENTATION, mock only. Agent: Claude Code. Gate C of the Owner's A, B, C order.
- State: AGENT VERIFIED / HUMAN REVIEW PENDING (S10: Owner final acceptance recorded, single receipt written, one Draft PR authorized; the Owner reviews and merges). The Owner answered CP4 (2026-11-26); S2 built the selections and ran CP5 and an independent review; S3 (2026-11-27) ran the design commands, fixed two alignment defects and reran CP5; S4 (2026-11-27) obtained the independent review, fixed its two contract deviations and verified final candidate `c3f9688` (delta reviews PASS). S5 (2026-11-28) ran the A11 Docker drills with the Owner's authorization: PASS. S6 (2026-11-28) applied the Owner-approved Thai review (159 kept, 33 replaced) on candidate `253bf48`; independent review PASS; A05 deferred by the Owner for this stage. S7 (2026-11-28) found that every 404 document is sent without server `lang` and is empty without scripting (DPT-PLAN-013 4.2/V01 not met); no correction fits the approved design, so it waits for an Owner decision. S8 (2026-11-28): the Owner accepted the visual design as the initial frontend baseline; the Owner's Notes screenshot shows no unwanted outline (observation; exact Win+Shift+S sequence not confirmed). S9 (2026-11-28): with the Owner's bounded authorization, the 404 documents were fixed with experimental `globalNotFound` (Next.js 16.4.6, local mock only); final candidate `53d0126`, independent review PASS, preview restored on image `568cc3b3…`. S10 (2026-11-28): the Owner accepted Frontend V1.1 as the initial mock baseline and explicitly deferred the physical Notes shortcut check (NOT RUN / OWNER-DEFERRED, not PASS); final receipt [[2026-11-28_180705_IMP-WEB-02_Frontend_V1_1]]; one-time publication (one push, one Draft PR, Owner-login exception).
- Experimental dependency: `experimental.globalNotFound` (Owner-authorized S9 for the pinned Next.js 16.4.6 and the local mock only). **Reassess compatibility before any framework upgrade, live data or production deployment.**
- Branch `feat/frontend-v1-1-design-upgrade`, worktree `.local/worktrees/imp-web-02-frontend-v1-1`, starting SHA `3e87027fbdbbb016c148a84ca33775e64cccf3e0` (PR #37 merge, equal to remote `main`, verified 2026-11-26).
- Approved plan: [[DPT-PLAN-013_Frontend_V1_1_Amendment]] (PR #37, merged 2026-11-26T13:30:40Z), amending [[DPT-PLAN-012_Luxury_Frontend_Editorial]].
- Intake class B. ID check: no IMP-WEB-02 branch, PR or task note existed; the ID appeared only as the proposed name in the merged plan.
- Implementation PR: NOT CREATED at the S10 receipt commit. The Owner authorized one push and exactly one Draft PR (S10); it is created after that commit, and its number and verified state are in the S10 publication result below (LOCAL_ONLY until a later authorized push).
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
| S4 | Independent review, review fixes, acceptance reconciliation | CLOSED | Review CONDITIONAL then delta PASS; PASS agent side; ACCEPTANCE PENDING | code `c3f968853b64b4ee65df2d9cf8c6b94e0b13014b`; records `9f78099` | [[2026-11-27_IMP-WEB-02_S4_Report]] |
| S5 | A11 Docker drills, acceptance reconciliation | CLOSED | A11 PASS; ACCEPTANCE PENDING (Owner items) | code `c3f968853b64b4ee65df2d9cf8c6b94e0b13014b` (unchanged); records `9088837` | [[2026-11-28_IMP-WEB-02_S5_Report]] |
| S6 | Owner-approved Thai translations, regression, review, reconciliation | CLOSED | PASS agent side; review PASS; ACCEPTANCE PENDING (Notes check, publication) | code `253bf485d40a9e4367db8968cf0d0d59faf8f127`; records `e755f07` | [[2026-11-28_IMP-WEB-02_S6_Report]] |
| S7 | 404 language investigation | CLOSED | BLOCKED on an Owner decision (no code change) | code `253bf485d40a9e4367db8968cf0d0d59faf8f127` (unchanged); records `31d9e1d` | [[2026-11-28_IMP-WEB-02_S7_Report]] |
| S8 | Owner visual acceptance, closeout preparation, next-development handoff | CLOSED | Visual ACCEPTED; 404 decision open; no code change | code `253bf485d40a9e4367db8968cf0d0d59faf8f127` (unchanged); records `763b678` | [[2026-11-28_IMP-WEB-02_S8_Report]] |
| S9 | Authorized 404 correction, regression, review, preview restore, closeout, next-slice packet | CLOSED | 404 fixed; PASS agent side; review CONDITIONAL then PASS; ACCEPTANCE PENDING (Notes test, publication) | code `53d01265962059655764f8d65be5b71329e600c4`; records `519ee3f` | [[2026-11-28_IMP-WEB-02_S9_Report]] |
| S10 | Owner final acceptance, receipt, public-safety review, one-time publication | CLOSED | Accepted by the Owner; receipt written; Draft PR authorized; human review and merge PENDING | code `53d01265962059655764f8d65be5b71329e600c4` (unchanged); records commit follows | [[2026-11-28_IMP-WEB-02_S10_Report]] |

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

### Session S5 — A11 Docker drills

State: CLOSED. Agent: Claude Code. Class A. Start `9f78099` (code `c3f9688`), verified. Owner authorization (2026-11-28): A11 drills including temporary stop and replacement of the preview.

- A11 PASS: failed preview build kept the preview serving; dev-while-preview and preview-while-dev refused; host port conflict stopped dev safely; dev on the fixed URL with isolated dependency volumes; component hot reload 817 ms without reload at `http://localhost:3000`; dev syntax error recovered in 1.3 s without restart; stop/start without rebuild; teardown left no task container. Hot reload is blocked at `127.0.0.1` by the Next.js dev origin rule (documented dev URL is localhost); recorded, not changed.
- Preview restored without rebuild: `sha256:48748b9cc0ffb413d270a2cd75a5fcefac0a9b92796bafa67250c6d12f2e33cf`, healthy, same hardening; Chrome 283/0/0/0 on it. Volumes (32), unrelated containers and rollback tags unchanged; previous `dev` image kept as `dev-pre-a11`. `web/` identical to `c3f9688` after every drill.
- Navy folio `color-mix` rules (R1-N3): decorative, approved tokens on navy, about 2.2:1 against navy; compliant under the Owner's condition; retained.
- Not run: screen reader, physical phone, Safari, Firefox, LAN probe, the Owner's physical Win+Shift+S path. A05 PARTIAL.
- Next: Owner A05 deferral, Notes check, Thai line review, site review, publication authority ([[IMP-WEB-02_Draft_PR_Package]]); then the receipt.

### Session S6 — Thai localization finalized

State: CLOSED. Agent: Claude Code. Class A. Start `9088837` (code `c3f9688`), verified. Owner decisions (2026-11-28): approve the full Thai review of 192 entries (keep 159, replace 33); defer A05's remaining manual checks for this stage; family and accord labels stay English; navy folio colour accepted; T1–T8 and A11 evidence retained; Notes physical check pending; publication not authorized.

- Translations: 33 exact replacements (interface 26, prose 7) from `DoomParfum_IMP-WEB-02_Thai_Review_Recommendations.md` (SHA-256 `2e5abb68…`); reconciliation of the final code: 159 KEEP unchanged, 33 REPLACE exact, 192 English unchanged, 0 unapproved changes. The 32 prose texts carry the Owner's `reviewed` record (4.3), so English pages also find them for a Thai query (4.5). A unit test pins the approved wording (`5638f83b…`). Commits `2f8b78a`, `4633f21`, `253bf48`.
- Tests on image `sha256:dedbba40f81fa0e089da3cf17978bd47c480957447269139390b27d75511257a`: unit 119/0; Chrome 283/0/0/0; Edge 283/0/0/0; clean clone and uncached builds PASS; audit 0; scan clean; no Thai prose in immutable chunks; JS ≤ 175.2 KiB; CLS ≤ 0.0187; Explore first picture 522/535 px.
- Independent review (same-vendor, read-only): `2f8b78a` CONDITIONAL (stale browser tests), fixed; `253bf48` PASS. Reports: [[2026-11-28_IMP-WEB-02_S6_Delta_Review_2f8b78a]], [[2026-11-28_IMP-WEB-02_S6_Delta_Review_253bf48]].
- A05: PARTIAL, deferred by the Owner for this stage; screen reader, physical phone, Safari, Firefox NOT RUN (future validation). A11: S5 evidence inherited (no runtime configuration changed since `c3f9688`). A10 LAN probe NOT RUN.
- Preview: `dedbba40…` at http://127.0.0.1:3000/; rollback tag `c3f9688-rollback` (`48748b9c…`). Protected resources unchanged.
- Next: Owner physical Notes check; Owner review and publication authority ([[IMP-WEB-02_Draft_PR_Package]]); then the receipt.

### Session S7 — 404 language investigation

State: CLOSED (blocked). Agent: Claude Code. Class A. Start `e755f07` (code `253bf48`), verified.

- Raw HTTP on the candidate: unknown English and Thai paths and slugs, `/en`, `/en/explore`, `/TH`, `/fr`, malformed addresses and the `/unavailable` routes all return 404 with nonce CSP, no-store and noindex, but the body is the framework error document `<html id="__next_error__">` without `lang`, heading or disclosure; empty without scripting; localized only after hydration. V1 served unmatched URLs as a full English 404; CP4 and later do not.
- Contract: 4.2 server `lang` on first byte and V01 "404 in the right language" not met; V15 met. S1's spike row overstated the 404 result; its limitations line had recorded it.
- Cause: `notFound()` thrown inside a page cannot render on the server with two root layouts (React server rendering runs no error boundaries); Next.js sends its fallback error document.
- Tested in a scratch clone only: htmlLimitedBots, force-dynamic: no effect; Suspense: status 200; proxy rewrite status: ignored (200); experimental `globalNotFound` + global 404 page in the path's language + proxy rewrites for malformed addresses and unknown slugs: all cases fixed (404, server lang, localized content, headers, no-script).
- No application change (Owner-reserved changes needed). Candidate `253bf48` and preview `dedbba40…` unchanged; S6 verification stands. Evidence: `Test_Evidence/IMP-WEB-02/S7/IMP-WEB-02_S7_404_Investigation.json`.
- Next: Owner decision (approve the tested correction, record a deviation for this stage, or the fallback architecture); Owner physical Notes check; publication authority.

### Session S8 — Owner visual acceptance and closeout preparation

State: CLOSED. Agent: Claude Code. Class A. Start `31d9e1d` (code `253bf48`), verified.

- Owner (2026-11-28): accepts the Frontend V1.1 visual design as the initial baseline; no further UI/UX refinement; next priority real catalogue data and backend features.
- Notes outline: the Owner's screenshot shows no unwanted heading outline. Recorded as an Owner observation; the exact physical Win+Shift+S sequence was not confirmed. Keyboard focus indicators unchanged.
- 404 item: reconciled, still open. The instruction did not approve the experimental `globalNotFound` correction, so nothing was implemented ([[2026-11-28_IMP-WEB-02_S7_Report]]).
- Verification: no code change; S6 results stand. Read-only smoke on the preview: ten routes 200 with server lang, nonce CSP, no-store, noindex; POST 405.
- Handoff: [[IMP-WEB-02_Next_Development_Handoff]] (smallest real-data slice P30-U03 → U07 and its open Owner decisions). No task started.
- Next: Owner 404 decision; publication authority ([[IMP-WEB-02_Draft_PR_Package]]); then the receipt.

### Session S9 — authorized 404 correction and closeout

State: CLOSED. Agent: Claude Code. Class A. Start records `763b678` (code `253bf48`, base `3e87027`), verified 2026-11-28.

- Owner instruction "IMP-WEB-02 — Final 404 Resolution and Closeout" (2026-11-28): bounded authorization of the S7 E6 correction (experimental `globalNotFound`) for the pinned Next.js 16.4.6 and the local mock only; no dependency upgrade, no other experimental feature, no routing restructure.
- Work: `app/global-not-found.tsx` (shared shell and unavailable view, localized title); the proxy sets the locale header from the path only and rewrites malformed addresses and unknown slugs to `/_unavailable` or `/th/_unavailable`; catch-all and `/unavailable` routes removed; `experimental.globalNotFound` in `next.config.ts`. Per-locale targets are needed because Next.js 16.4.6 runs the proxy again on an unmatched rewrite target (verified with an instrumented scratch build). Code `3b93945` then review follow-up `53d0126` (comments and tests only).
- Tests: unit 122/0; Chrome and Edge 305/305 on the final preview image; new tests fail on the old candidate (e2e 18 of 19, unit 2 of 6); output scan clean; ten valid routes unchanged (text 20/20, deterministic screenshots identical); no-JS 404s readable in both languages; spoofed locale headers ignored. Evidence: `Test_Evidence/IMP-WEB-02/S9/IMP-WEB-02_S9_404_Verification.json`.
- Review: [[2026-11-28_IMP-WEB-02_S9_Delta_Review_3b93945]] CONDITIONAL (runtime unreachable; diagnosis and test gaps), all addressed; [[2026-11-28_IMP-WEB-02_S9_Delta_Review_53d0126]] PASS at runtime. Accepted nits recorded in [[2026-11-28_IMP-WEB-02_S9_Report]].
- Runtime: Docker Desktop stopped mid-session; the Owner approved restarting it. Preview `127.0.0.1:3000` = image `sha256:568cc3b30f8fef993d5db66e2e6f2bbfd5c6536c874b7786d3385d53c66f701e`, healthy, hardened, loopback only. Rollback tags `253bf48-rollback`/`s6-final` (`dedbba40…`), `s9-candidate1` (`10ded624…`). Other containers and 32 volumes unchanged.
- Preserved: T1–T8, approved translations, reviewed Thai search, A05 deferral, A11 evidence. Notes physical shortcut test: **not performed** (Owner to confirm or defer).
- Next development: [[IMP-WEB-02_Next_Slice_Decision_Packet]]; no task started.
- Git: code `53d01265962059655764f8d65be5b71329e600c4`; records commit follows. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`.
- Next: Owner confirms or defers the Notes test; publication authority ([[IMP-WEB-02_Draft_PR_Package]]); then the single final receipt.

### Session S10 — final acceptance, receipt and publication

State: CLOSED. Agent: Claude Code. Class A. Start records `519ee3f` (code `53d0126`, base `3e87027`), verified 2026-11-28.

- Owner instruction "IMP-WEB-02 Final Closeout and One-Time Publication Authorization" (2026-11-28):
  - Frontend V1.1 is accepted as the initial visual and functional mock baseline.
  - T1–T8 are final for this stage; all 192 Thai decisions are approved; proper names and family/accord labels stay as approved; the reviewed Thai search behavior is accepted.
  - The 404 correction is accepted for the pinned local mock scope. A05 stays PARTIAL (deferred); A11 evidence is accepted where applicable.
  - **The physical Notes Win+Shift+S check is explicitly deferred: NOT RUN / OWNER-DEFERRED, not PASS.** The S8 screenshot stays a separate observation.
  - No further visual refinement; no WCAG or production-readiness claim.
- Publication authority:
  - Granted once: local closeout commits, one normal push of this branch, and exactly one Draft PR to `main`.
  - Not covered: merge, force push, push to `main`, Ready for Review, other PRs, settings, deployment and later cycles.
  - Credential: no agent identity exists. The Owner confirmed in the session that their own login may be used once for this push and PR ([[Decision_Log]]).
- Verified before publication:
  - PR #37 merged; remote `main` `3e87027`.
  - No remote branch or PR of any state for this branch; repository PUBLIC.
  - `web/` tree `be5cea26…` identical at `53d0126` and `519ee3f`.
  - Preview image `568cc3b3…` healthy; four other containers, 32 volumes and rollback tags unchanged.
- Public-safety review of `3e87027..HEAD`: clean (details in [[2026-11-28_IMP-WEB-02_S10_Report]]). `CP4.zip` stays untracked.
- Evidence reused, no suites re-run: S9 (unit 122, Chrome/Edge 305, review PASS, 404 raw and no-JS checks, scan), S6 (clean clone, uncached build, audit, performance; same lockfile), S5 (A11; since then only the experimental flag in `next.config.ts`).
- Receipt: [[2026-11-28_180705_IMP-WEB-02_Frontend_V1_1]], the only one for this task.
- Experimental `globalNotFound`: unchanged limits; reassess before any Next.js upgrade, live data or production deployment; the mock-slug handling is not the live-data contract.
- Not done: merge, Ready for Review, Docker rebuild, installs, design tools, U01 review, new task.
- Git: records commit follows; push and Draft PR after it.
- Next: Owner reviews the Draft PR on GitHub, marks it Ready and merges, or requests corrections. Next development: [[IMP-WEB-02_Next_Slice_Decision_Packet]] (separate authorization).

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
| [[2026-11-28_IMP-WEB-02_S5_Report]] | S5 | `cd9f014c9a0a1f2a220e2bd53e27b5bd417de279f7f073216816d9ae2026b6d8` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S5_Summary]] | S5 | `643c7d987b01a4c63f93f3b135f3c0c376f7f71a60fc59fd3b8ea718fcb106e1` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] (revised) | S5 | `01535f8448802800b6710287d2326493013291220c78557e9aaf560a66f74c71` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S6_Report]] | S6 | `c63a27532e0a2762da8253ffac13dd3d824b6744bc97c6d55c4a5a8b9f0e8d13` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S6_Summary]] | S6 | `d211663bb27dc75452f7ed5c31195680787f3746f27d549819d9e140e529fee9` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S6_Delta_Review_2f8b78a]] | S6 | `3d6db3e8dd0020332d691460c84dadb76c81c65be0801435baf4f227c6cd47b3` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S6_Delta_Review_253bf48]] | S6 | `1844d8102e13af15bea0614a276945b299988db0349357fade95947e6f921809` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] (revised) | S6 | `0d0af39da1a4a1fbb104575bc6ac1cd0f5824537a9e29914e0c5fd4ea9d14877` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S7_Report]] | S7 | `c7261a7f93bf6f8e2be837c32ab811735242a71db0dd2085eb8f447de205b6f5` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S7_Summary]] | S7 | `25d102b439d7884e6bb085e2ce05a0fe139fd5c44642770c82dc5f026d22f220` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] (revised) | S7 | `5802d21b7da9f63323fee51ad31fc7d5a2e4ebd9a0c63001e337d0a520873c4d` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S8_Report]] | S8 | `d9cf26dc54d675ee938838c74081774c62596887ebbf6e71f905bf602f84dc58` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S8_Summary]] | S8 | `4080c176e141d01756aca4d6f9db9bde036cbeba7b0136f4eedcb5edaf5d1c0a` | PUBLIC_SAFE |
| [[IMP-WEB-02_Next_Development_Handoff]] | S8 | `7874cae96708d6051f02de5f52acbc5bbdcc85e7d59629fad1c20e90865a81b9` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] (revised) | S8 | `7f838598ebf1ac59c4c80b78bdbfa54a10744c035343f5dc9a9f1ad45d2876b9` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S9_Report]] | S9 | `19c8a95f25918ee303652dc7fc79ff0c8f689ee9ba6eb683be3807a3baeb3705` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S9_Summary]] | S9 | `74040423743d4fd44ae75f631b76542807dfe7336b6919ebe97c9ec27755f563` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S9_Delta_Review_3b93945]] | S9 | `f2e5a26c647aefd239bce5ab8cb02a2372e50eb0eddbb6281a80ee70fd9913b4` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S9_Delta_Review_53d0126]] | S9 | `26ed64ca3eec4775c3464098a585628d3681f86db8b811c3e8ccc0df2fd3c72f` | PUBLIC_SAFE |
| [[IMP-WEB-02_Next_Slice_Decision_Packet]] | S9 | `d81fca9526a1745d6dd1d1e60235f5742f3f366de62b66b21dff662c7e1b2835` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] (revised) | S9 | `7d78a6548e54c70a8781a5655d8a9842d5e48e0c9853fbb7d885bfa96a24a3b0` | PUBLIC_SAFE |
| `Test_Evidence/IMP-WEB-02/S9/IMP-WEB-02_S9_404_Verification.json` | S9 | `d1408b964c5e05c5fe117a49fee5008000f359ec59bbc38825f2776af4a17bdf` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S10_Report]] | S10 | `2821127e56019e50f2bebd70b17b80d71c5a183b5e8708a0d18e2336898a3854` | PUBLIC_SAFE |
| [[2026-11-28_IMP-WEB-02_S10_Summary]] | S10 | `6ecfc96d7055122e3da28e84abfe0916d64267664ab1f44e29cd69c8a1ac5c0f` | PUBLIC_SAFE |
| [[IMP-WEB-02_Draft_PR_Package]] (final) | S10 | `f4224b18fefd4c066b1f3b68a3224ffe41e0011aa9e991daba6061b1ee4fd34b` | PUBLIC_SAFE |
| [[2026-11-28_180705_IMP-WEB-02_Frontend_V1_1]] (final receipt) | S10 | `60870cf31d0f98409d9165103410db6aabfe0a4381cfbc3754d9cc9356489a99` | PUBLIC_SAFE |

Owner packets: [[IMP-WEB-02_CP4_Owner_Review]], [[IMP-WEB-02_Translation_Review]] (CP4); [[IMP-WEB-02_CP5_Translation_Review]] (CP5). Final receipt (S10): [[2026-11-28_180705_IMP-WEB-02_Frontend_V1_1]].
