---
id: IMP-WEB-02-S2-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, frontend, localization, verification, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S2 — CP4 selections, CP5 verification, independent review

PUBLIC_SAFE. Agent: Claude Code. Intake class A (continuation of [[IMP-WEB-02_Frontend_V1_1]], same branch). Start `bd477f2` (code `733c59da`), verified equal to the local branch; nothing on the remote. Final candidate **`5d63f8809523b5d31b7888852fd44b1f57956874`**, web tree in Git. Preview image **`sha256:3a155e442df0f172604a68a44ba55e81a61684e0ca032756f0f07e407a97ca90`**, built uncached from the same files.

## Owner decisions (2026-11-26, chat)

| ID | Selection | Result in code |
|---|---|---|
| T1 | Fahkwang 300 | Thai display roles use `Bodoni Moda, Fahkwang, Noto Sans Thai` at weight 300, no tracking, no optical-size setting; line heights hero 1.35–1.40, page 1.45, section 1.50, entry 1.50–1.55 (from the specimen marks measurements). Latin names on Thai pages stay Bodoni 400. Body, controls and navigation stay Noto Sans Thai |
| T2 | C centred hero | Text column centred on the art from 768px; text first on phones; no masthead copy |
| T3 | B record sheet | `dl` with Family, Top, Heart, Base, General notes, Accords from the same record fields and note views as the layer section; known names, italic "not supplied", "no entries". Sticky column evaluated and not used: the sheet already fills most of the art height and a sticky column risked hiding content at short heights |
| T4 | B compact toolbar | Family, Note and Sort on one row with visible labels beside full-bordered native selects, 44px; search label and help kept. First catalogue picture: see tests (≤560px at 1440×900 and 1280×900, both languages) |
| T5 | A stable header | Unchanged; BY TK never hidden |
| T6 | A compact link | Unchanged |
| T7 | A equal columns | Unchanged. The CP4 6/3/3 render was reported identical to the default and was not a fair comparison; the Owner chose the equal layout regardless; not rerun |
| T8 | B square | Radius tokens 0; icons keep their shapes; borders, focus rings and dialog shadow kept |
| — | BY TK 11px | `--text-signature: 0.6875rem` |
| — | Thai wording | Owner terminology (ท็อปโน้ต, ฮาร์ตโน้ต, เบสโน้ต, โน้ตทั่วไป, ตระกูลกลิ่น, แอคคอร์ด, โครงสร้างกลิ่น 3 ระดับ, สำรวจตามตระกูลกลิ่น, เกี่ยวกับเรา, ไม่ได้ระบุ, ไม่มีรายการ) applied in context; 81 interface strings and 9 overlay texts rewritten; all still **draft**. Names, family and accord labels unchanged; Paper study L unchanged |

## Font provenance (T1)

`@fontsource/fahkwang@5.3.0` npm `sha512-7jNeeht0…DFRQ==` re-verified against the registry; shipped file `fahkwang-thai-300-normal.woff2`, 9,816 bytes, SHA-256 `86cb1a4944422c53e628d8174253d483f8226481d8dcd4de24a16adfef5fccda`; license SIL OFL 1.1, text from google/fonts `ofl/fahkwang` at `a60a77e14f28abd4ef243a1b5dfc48df0cec5205` (SHA-256 `f2c0dfa0…2f01`, identical to the Fontsource LICENSE terms). Self-hosting is permitted by the OFL; the font is not sold or renamed. Only this face ships; Chonburi and Taviraj stay in Git-ignored local tooling. `NOTICE.md`, image `licenses/` and both About credits updated.

## Defects confirmed and fixed

| Defect | Evidence | Fix |
|---|---|---|
| Heading ring returned after a pointer navigation when the window lost focus (screenshot tool), the Owner's Notes screenshot | New test failed on the pre-fix build, passes after | The pointer state ends only when focus really leaves the heading |
| Detector `straggler` on Thai About | Impeccable detect | `text-wrap: pretty` on list items |
| Review B1: NOTICE without Fahkwang | Review | NOTICE row and license list |
| Review B2: footer "ภาษาไทย" letter-spaced | Review, 1.04px measured | Thai language names never tracked; test |
| Review m1: reviewed Thai text could never be searched from English pages | Review | English view built with the overlay; drafts change nothing; test |
| Review m4: header static below 336px | Review | Rule removed; the measured 20% rule covers two-row reflow; test |

Checked, no defect: the breadcrumb in the Owner's Detail screenshot. Forward navigation lands at the top with the breadcrumb at 171px below a 94px header (139/78 on a phone); Back restores the entry focused below the header. Content scrolling under a sticky header is expected.

Recorded, not changed: head `hreflang` alternates are omitted because Next.js resolves relative alternates against a default absolute origin without a configured `metadataBase`; links carry `hreflang` (DPT-PLAN-013 4.4 allows this). 404 views still reach the browser through the framework's error document (empty first byte, title and status correct), as noted in S1.

## Design tools

| Tool | Executed |
|---|---|
| Impeccable `doctor` | Yes: one finding, `hook-not-installed`; not acted on (hooks need Owner approval) |
| Impeccable `context`, `detect` (source and nine routes, twice) | Yes. Final: only `cream-palette` (Owner-approved ivory). `undersized-ui-text` cleared by 11px; `straggler` fixed |
| Impeccable typeset, layout, adapt, harden, audit, polish, distill, colorize | Their references guided the edits and checks; they are guidance commands without a separate executable step in this setup. Audit was carried out through detect, axe, the suites and the measurements below |
| Impeccable critique | Not run as a separate pass: the independent review below covered the critique scope with a fresh context |
| Taste Skill | Composition reference (loaded in S1); its scripts and gate not run (project rule) |
| UI Craft, UI UX Pro Max | Not used; no measurable benefit beyond the above; `brand` out of scope |
| bolder, overdrive, delight, animate | Not used, as instructed |

## CP5 verification (final candidate and image)

| Check | Result |
|---|---|
| `typecheck:gen`, `eslint --max-warnings 0`, `validate:fixtures` | Exit 0; 12 studies, 9 notes, 3 families, 4 accords, 2 articles |
| `npm test` | PASS 117 / FAIL 0 |
| Playwright Chrome 158.0.8127.38 on the preview | PASS 259 / FAIL 0 / SKIP 0 |
| Playwright Edge 158.0.4370.33 on the preview | PASS 259 / FAIL 0 / SKIP 0 |
| Clean clone at `5d63f88`, `npm ci` with an empty cache, `npm run build` | PASS |
| Uncached image build (`--no-cache`), type check, lint and tests inside | PASS |
| `scan-output` on the image | No boundary violation; no Thai or fixture prose in static chunks |
| `npm audit` (all, and production) | 0 vulnerabilities |
| Initial JS per route, ten routes | 171.4–175.1 KiB transfer (budget 200 KiB); the reviewer measured 164–168 KiB with another method |
| CLS | ≤ 0.023 (budget 0.1) |
| Fonts | English pages 103.0 KiB (unchanged); Thai pages and English Explore (lists the Thai-named Paper study L) +10.1 KiB Fahkwang |
| External requests, cookies, storage | 0 on all ten routes |
| Methods | POST/PUT/DELETE on Thai and English routes 405 with `Allow: GET, HEAD`; CSP and noindex present |
| Forced colours, reduced motion | No overflow; sticky header kept; transitions off under reduced motion |
| Widths and zoom | Suite covers 320, 375, 390, 640, 768, 1024, 1280, 1440, 1920, 812×375, 200% text, 400% zoom equivalent at 320 |

Evidence: [CP5 performance](../../Test_Evidence/IMP-WEB-02/CP5/IMP-WEB-02_CP5_Performance.json), screenshots in `Test_Evidence/IMP-WEB-02/CP5/screens/` (ten routes at 1440 and 390, states, dialogs, language controls, 404, empty, unknown and invalid states), comparison sheets `IMP-WEB-02_CP5_Comparison_CP4_vs_Final.png` and `IMP-WEB-02_CP5_Fahkwang_Bodoni.png`, translation review [[IMP-WEB-02_CP5_Translation_Review]].

NOT RUN: screen reader, physical phone, Safari, Firefox, second-machine LAN probe, Docker development mode and recovery drills (Compose files unchanged since IMP-WEB-01 A11). A05 stays PARTIAL. No WCAG conformance claim.

## Independent review

Fresh-context, read-only Claude sub-agent (same vendor), commissioned by the implementing agent; reviewed `76dcb1c` and the running image. Report kept outside Git (it names local paths): SHA-256 `c05a9682ad7793c27ebd94b7f0fcdb34b2c2f65b0ca50b2ea258b0ebcf9df3ef`. Verdict CONDITIONAL: blockers B1, B2; major M1 (records not yet showing the Owner's CP4 answers; resolved by this record set); minor m1–m4 (m1, m4 fixed; m2, m3 recorded above); notes N1–N9 (N2 test title corrected; N4, N5 are Thai wording points for the Owner's line review: "ไม่ทราบ" for an unknown family versus "ไม่ได้ระบุ" for unknown lists, and three drafts that shift meaning slightly: perfume-005 "for beginners", perfume-011 "durability", about lead "created for demonstration"). The reviewer reran unit, both browser suites, header and chunk checks; it did not check audit, clean build, Docker build, CLS, forced colours, zoom or manual accessibility. Fixes were not re-reviewed by the sub-agent; they are covered by new tests and the full rerun above. Not human, not cross-vendor.

## Preview and protected resources

`http://127.0.0.1:3000/`, container `doomparfum-web`, image `3a155e44…`, healthy, loopback, read-only, user `node`, all capabilities dropped. Rollback tags: `cp5-candidate1` (`bb505e6d`), `cp4-rollback` (`177c02e5`), `v1-rollback` (`43be51f1`). Four protected containers stopped, 32 volumes; PR #8 OPEN/DRAFT unchanged; U01/r14, database, matching and ETL untouched.

## Result and next action

CP4 selections implemented and CP5 verified on the agent side. **ACCEPTANCE PENDING**: no receipt, because A05 needs the Owner's stage-specific deferral and Thai text is draft. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`. Next: the Owner reviews the site and the translation sheet, confirms the A05 deferral for this stage, and authorizes publication; then the receipt and a Draft PR.
