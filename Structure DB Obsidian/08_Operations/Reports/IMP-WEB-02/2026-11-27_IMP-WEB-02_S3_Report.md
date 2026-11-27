---
id: IMP-WEB-02-S3-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-27
tags: [doomparfum, frontend, design-review, verification, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S3 — design-tool passes, focus-path reproduction, CP5 rerun

PUBLIC_SAFE. Agent: Claude Code. Intake class A (continuation of [[IMP-WEB-02_Frontend_V1_1]], same branch, no PR). The Owner re-sent the full CP4/CP5 instruction on 2026-11-27, naming `733c59da` / `bd477f2` as the last checkpoints. Verified state at start: local branch at `3966115` (S2 records), code `5d63f88`, four commits past the named checkpoints, nothing on the remote; remote `main` = `3e87027`. S2 had already implemented T1–T8 and run CP5, so this session closed the gaps between the instruction and S2's record instead of rebuilding: real execution of the requested design commands, every Notes focus path, a fresh CP5 run on a new candidate.

Final candidate **`689b177b4908cd84bec1ac2c81fc9a17963224d3`**. Preview image **`sha256:a324a06dffc304cc3b2eeb48748dc3dc2e083bcc02a7e526d98b7722e441f1d2`** (tag `preview`, also `s3-candidate2`), built `--no-cache` from the committed `web/` tree.

## T1–T8 state on the final candidate

Unchanged from S2 except T3 alignment (below). T1 Fahkwang 300 Thai display; T2 centred hero; T3 record sheet; T4 compact toolbar, first catalogue picture at 522px (English) and 535px (Thai) at both 1440×900 and 1280×900 (limit 560; CP4 Thai was 563); T5 stable header; T6 compact language link; T7 equal columns; T8 square corners; BY TK 11px. Thai wording unchanged since S2 and still draft ([[IMP-WEB-02_CP5_Translation_Review]]).

## Defects confirmed and fixed

| Defect | Found by | Fix | Test |
|---|---|---|---|
| T3 record sheet: each value began after its own label, so six values started at six positions (1440 and 390, both languages) | Impeccable critique, Assessment A (visual) | Rows are a two-column grid with a shared label column, kept only where the sheet is at least 21rem wide; below that (320px, enlarged text) the label sits above its value | `s3-alignment.spec.ts`: fails on the S2 image, passes on the candidate |
| First grid version: at 320px with 200% text a note name ran 4px past the viewport | A08 reflow test on the first candidate | Container query above; `overflow-wrap: break-word` on values | A08 reflow and a new stacked-at-200% test |
| Footer language names 8px outside the footer column (a pull meant for 44px code boxes) | Assessment A | Pull removed for the footer's full names | `s3-alignment.spec.ts` |
| S2 full-page screenshots showed an empty right half in the navy folio | Assessment A | Not a UI defect: the folio drawings are lazy images that full-page capture never loaded. S3 captures scroll each page first | Visual check, `S3/screens` |

Commits: `ee34142` (grid, footer, tests), `689b177` (narrow and enlarged-text stacking). Files: `web/src/views/detail.tsx`, `web/src/app/globals.css`, `web/e2e/focus-paths.spec.ts`, `web/e2e/s3-alignment.spec.ts`.

## Notes heading outline (Owner item 11)

New `focus-paths.spec.ts` drives each path through real pointer or keyboard input on the candidate: pointer to Notes then Shift, letters, Control, Meta, PrintScreen, Ctrl+Shift+S and Win+Shift+S chords (no ring); tab switch and back (no ring); Thai pointer (no ring) and Thai keyboard (ring); English keyboard (ring); Back and Forward after a pointer navigation (no ring); language switch by pointer and by keyboard (no heading ring on the new document); alphabet jump link by keyboard (ring) and by pointer (no ring, V13); note link from a perfume entry (no ring); mobile drawer (no ring); Search dialog closed by pointer (no ring) and by Escape (ring on the trigger). Skip link by keyboard keeps its ring (V13).

Result: no pointer path draws a ring; every keyboard path does. Sensitivity: the S2 V13 test that simulates a screenshot tool's blur fails on the CP4 image (`cp4-rollback`) and passes on the candidate, so S2's fix is the change that removed the Owner's outline. The new tab-switch test passes on both images and does not reproduce an OS screenshot shortcut; Playwright cannot press Win+Shift+S at the OS level. NOT RUN: the Owner's exact physical path (click Notes, press Win+Shift+S, Escape) on a real desktop. No outline rule was disabled globally.

## Design tools (actually executed)

| Tool / command | Execution | Outcome |
|---|---|---|
| Impeccable `doctor --json` | Run | One finding `hook-not-installed` (severity route). Not acted on: hooks need Owner approval |
| Impeccable `context` | Run | No DESIGN.md; no incumbent visual implementation detected; detector hook inactive (manual detect required); not signed in (login forbidden by project rule); PRODUCT.md still calls DPT-PLAN-013 "proposed until merged" although PR #37 merged on 2026-11-26 (truth drift; reported, not edited) |
| Impeccable `critique` | Run **⚠️ DEGRADED: single-context**. The two isolated sub-agents were refused twice by the auto-mode classifier because the context-mode plugin hook rewrites every Agent call; not retried. Assessment A (visual review of the rendered build at 1440 and 390, both languages) finished before B | Heuristics 30/40 (Good): status 3, real world 3, control 3, consistency 3, error prevention 3, recognition 3, flexibility 2, aesthetic 3, recovery 3, help 3. Priority issues: P2 record-sheet alignment (fixed), P3 footer language offset (fixed), P3 lazy drawings missing from S2 evidence (re-captured), P3 second columns start at three positions on Home (504/660/732px at 1440) because the approved 5/7 hero and 6/6 folio grids differ (recorded, not changed). Questions skipped: one open priority issue, and the Owner barred reopening approved layouts. Snapshot not saved under `.impeccable/` (degraded run; this report is the record) |
| Impeccable `detect` | Run: source `web/src` and 10 routes × 1440×900 and 390×844 of the candidate | Source: 0 findings. Rendered: only `cream-palette` (`#F7F5F0`) on all 20 views, the Owner-approved ivory. The detector did not catch the record-sheet misalignment |
| Impeccable `audit` | Run inline (same sub-agent refusal), scored from this session's measurements and suites | 18/20 (Excellent): accessibility 3 (axe AA and keyboard suites pass; screen reader, Safari, Firefox not run), performance 4, theming 3 (tokens throughout; dark mode out of scope; hard-coded values not re-audited this session), responsive 4, implementation integrity 4 |
| Impeccable typeset, layout, adapt, harden, distill, polish, colorize | Read as references for the fixes above and checked against the render (alignment, measure, 320/200% reflow, states, palette use) | No further violation found; colorize confirmed only approved tokens appear on rendered surfaces (detector palette scan) |
| Taste Skill `consistency.mjs` (read-only checker) | Run with `--quick` at 1440 and 390 on `/`, `/perfume/paper-study-a`, `/th/explore` of the candidate | FAILs are its house rules contradicting the approved design or mock disclosure (captions under visuals, photographs, one section per screen, 64–120px margins, hero-fill, its 7:1 body contrast against the project's AA target: measured 6.32:1). Nothing actionable beyond Assessment A. Its photo/icon fetchers, `start.mjs deal` and `gate.mjs` were not run |
| UI Craft, UI UX Pro Max | Not used | No measurable benefit over the above |
| bolder, overdrive, delight, animate, live, generate | Not used | As instructed |

## CP5 rerun (final candidate `689b177`, image `a324a06d…`)

| Check | Result |
|---|---|
| `typecheck:gen`, `eslint . --max-warnings 0`, `validate:fixtures` | Exit 0; 12 studies, 9 notes, 3 families, 4 accords, 2 articles |
| `npm test` | PASS 117 / FAIL 0 (worktree, clean clone and inside the image) |
| Playwright Chrome, full suite on the preview | PASS 279 / FAIL 0 / SKIP 0 |
| Playwright Edge, full suite on the preview | PASS 279 / FAIL 0 / SKIP 0 |
| Clean clone at `689b177`, `npm ci` with an empty cache, `npm run build` | PASS |
| Uncached image build (`--no-cache --target runner`) | PASS |
| `scan-output` on the image's `/app` | 325 files outside node_modules, 22 immutable scripts; no boundary violation |
| `npm audit` (all; `--omit=dev`) | 0 vulnerabilities each |
| Initial JS (suite, English routes) | 171.4–175.1 KiB (budget 200) |
| CLS (suite) | ≤ 0.0234 (budget 0.1) |
| Fonts, ten routes | 101.5 KiB on English pages; +9.6 KiB Fahkwang on Thai pages and English Explore (Paper study L) |
| External requests, storage, cookies, ten routes | 0 |
| Headers, methods, no-script, reduced motion, widths 320–1920, 200% text, 400% zoom equivalent, forced colours | Covered by the passing suites above (same specs as S2 plus 20 new tests) |

Evidence: [S3 performance](../../Test_Evidence/IMP-WEB-02/S3/IMP-WEB-02_S3_Performance.json); screens in `Test_Evidence/IMP-WEB-02/S3/screens/` (ten routes at 1440 and 390 with lazy drawings loaded; sticky header EN and TH, desktop and mobile language controls, Search TH and Profile dialogs, menu drawer, unknown/empty/unavailable detail, invalid filter TH, 404 EN and TH); comparison `S3/IMP-WEB-02_S3_Comparison_CP5_vs_S3.png` (record sheet before/after, EN 1440 and TH 390). S2's CP5 sheets (CP4 vs final, Fahkwang beside Bodoni, hero, toolbar, corners) still describe the selections.

NOT RUN: screen reader, physical phone, Safari, Firefox, second-machine LAN probe, Docker development mode and recovery drills (Compose files unchanged since IMP-WEB-01 A11). A05 stays PARTIAL. No WCAG conformance claim.

## Independent review

**BLOCKED this session.** A fresh-context reviewer needs the Agent tool, which auto mode refused because the context-mode hook alters the call after review. Not substituted by a self-review. The last independent review (S2, same-vendor sub-agent) covered `76dcb1c`; `5d63f88`, `ee34142` and `689b177` have not been independently reviewed. To unblock: disable the context-mode hook for one session or approve the Agent call outside auto mode, then commission a read-only review of `689b177` and image `a324a06d…`.

## Preview and protected resources

`http://127.0.0.1:3000/`, container `doomparfum-web` recreated with `docker compose up --no-build --force-recreate` (web service only), image `a324a06d…`, healthy, loopback, read-only, user `node`, capabilities dropped. Docker Desktop was stopped at session start and was started for this task. Rollback tags: `cp5-s2-rollback` (`3a155e44`, S2 final), `s3-candidate` (`da5ec288`, first S3 build, superseded), `cp5-candidate1`, `cp4-rollback`, `v1-rollback`. Temporary probe containers on 127.0.0.1:3100 ran with `--rm` and are gone. The four protected containers stayed stopped; no volume, prune, PR #8, U01/r14, database, matching or ETL change.

## Result and next action

Agent side PASS on the final candidate; **ACCEPTANCE PENDING**. Open: the independent review of the final candidate (blocked, above); the Owner's review of the site and of the draft Thai lines; the Owner's stage-specific A05 deferral; the Owner's physical check of the Notes path; publication authority. Local publication package: [[IMP-WEB-02_Draft_PR_Package]]. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`. No receipt.
