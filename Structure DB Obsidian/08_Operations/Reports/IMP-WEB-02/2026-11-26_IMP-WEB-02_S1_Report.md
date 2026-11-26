---
id: IMP-WEB-02-S1-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, frontend, localization, implementation, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S1 — Frontend V1.1, CP0 to CP4

PUBLIC_SAFE. Agent: Claude Code. Intake class B. Task [[IMP-WEB-02_Frontend_V1_1]], contract [[DPT-PLAN-013_Frontend_V1_1_Amendment]] (PR #37 merged 2026-11-26T13:30:40Z as `3e87027fbdbbb016c148a84ca33775e64cccf3e0`, equal to remote `main`). Branch `feat/frontend-v1-1-design-upgrade`, worktree `.local/worktrees/imp-web-02-frontend-v1-1`. Code checkpoint `733c59da80fb22f8164859d756f1f24c1bcd008f`, web tree `1ea8043db440b68c7e239dd758a8e249f7f57ec3`. The records commit that adds this report is in Git.

## Authority

Owner instruction of 2026-11-26: implement the approved V1.1 scope; create the branch and worktree; bounded download of Chonburi, Fahkwang and Taviraj with verified licenses, pins and checksums (V11-OD-11); update the project-local design-tool rule; local tests, Docker builds and replacement of the preview on port 3000. Stop at the CP4 Owner review. No push, PR or merge.

## TOOL DECISION / EXECUTION

| Tool | Status | Use |
|---|---|---|
| Impeccable | USED | `context` (no DESIGN.md; scoped refinement, so no new-world flow), craft-floor read before edits, `detect` on changed source and nine rendered routes. Its `CONTEXT_STALE` hook finding is reported, not acted on (hooks need Owner approval) |
| Taste Skill | USED as reference | Composition and hierarchy only. Its photography, no-caption rule, presets, `start.mjs deal` and `gate.mjs --start` conflict with the approved mock design and the project rule; not run |
| UI Craft, UI UX Pro Max | NOT USED | No separate benefit over the two primaries for this scope; `ui-ux-pro-max:brand` out of project scope |
| Requested `critique`, `layout`, `bolder`, `overdrive`, `colorize`, `animate`, `adapt`, `harden`, `audit`, `polish`, `delight`, `distill` | Applied as lenses, not run as separate commands | Layout, colorize, adapt and harden shaped CP1–CP3; audit through the detector, axe and suites; `bolder`, `overdrive`, `delight` and extra animation rejected by the restrained contract; critique is the Owner's CP4 review |
| npm (lockfile), Node 24.22.3, Next 16.4.6, Playwright 1.65.1, Chrome 158.0.8127.38, Edge 158.0.4370.33, Docker 28.3.2, ffmpeg | USED | Build, tests, images, preview |
| npm registry, GitHub API | USED, bounded | Font candidates and license texts only |

Nothing installed globally; no hook, MCP or client setting changed. Project-local rule `.claude/rules/doomparfum-frontend-design-tools.md` (untracked, primary checkout) updated as authorized: SHA-256 before `3f37a8d1e30cc3a1144028b22f694936cba9a7c30b0f2b5bcfd8bd08d381c4d3`, after `44a5feb912c39f5bfe7215cd5e8f79d8e1f4ab015b65f6b6dd7e417baa83becd`; backup outside Git.

## CP0 baseline

`npm ci` clean; on `main` with the V1 image restarted: unit PASS 85 / 0, Chrome PASS 189 / 0. Before screenshots of five routes at 1920, 1440, 1024, 768 and 390 kept outside Git.

## Work performed

| Checkpoint | Result |
|---|---|
| CP1 foundation | Gold–bronze tokens with aliases; R1–R5 rules; display entry titles; Thai metrics per role; section rhythm; link and button states; decorative-only gold enforced by tests |
| CP1 specimen | Separate loopback specimen, Chrome and Edge, measurements and sheets in [CP4/T1](../../Test_Evidence/IMP-WEB-02/CP4/T1/T1_measurements.json) |
| CP2 spike | Two root layouts `(en)` and `th`. Proven on a production build: ten routes 200 with server `lang` and titles; `/en`, `/en/explore`, `/TH`, `/fr`, unknown paths and slugs, undecodable addresses: 404 with CSP, no-store, noindex and the right-language view |
| CP2 localization | Typed dictionaries (159 strings), server-only Thai overlay (32 texts, all draft) with validator, locale-aware links, search rule that leaves English unchanged |
| CP2 header | Sticky, stable, opaque, layer 20; R1; TH and EN after Profile; compact link on narrow screens; drawer segment and footer links; measured offset |
| CP3 pages | Home (rules, numerals, family counts, folio layout, journal arrows), Explore (spacing, chips, aligned titles), Detail (rules, numerals, italic unknowns, +/− record), Notes (live-letter index, bronze group letters), About (long-form size, sticky contents with scrollspy, narrow disclosure) |
| CP2/CP3 focus | Heading focused after pointer navigation shows no ring, even after a later key press; keyboard navigation keeps it |
| CP4 | [[IMP-WEB-02_CP4_Owner_Review]] with T1–T8 and [[IMP-WEB-02_Translation_Review]] |

Font candidates (not shipped): `@fontsource/chonburi@5.3.0`, `fahkwang@5.3.0`, `taviraj@5.3.0`, npm `sha512` matched the registry; licenses SIL OFL 1.1 from google/fonts at `3dd78844021e948ceb633d1dcee3f7885561b5d9`, `a60a77e14f28abd4ef243a1b5dfc48df0cec5205`, `037aad08f644fd50dcfac7724fee8bb07229cd0f`. File hashes in [T1_faces.json](../../Test_Evidence/IMP-WEB-02/CP4/T1/T1_faces.json).

## Findings and fixes during the session

| Finding | Fix |
|---|---|
| Header lost its 48px gutter (two container names on one element) | Separate containers |
| Thai hero broke inside "ส่วนตัว" at 390px | U+2060 in the dictionary string |
| `scroll-padding-top` made focusing a header control scroll the page (caught by the V1 scroll-lock tests) | `scroll-margin-top` on content in `main` and the footer |
| Undecodable address: 500 in Docker (catch-all parameter decoding) | Static `unavailable` route per language |
| 404 text existed only client-side | Server component view |
| axe: `role="group"` on a list; gold numeral at 70% folio opacity | Group wrapper; numeral at large-text size |
| Synthetic notice badge duplicated the Mock marker | Notice text kept as in V1 |
| Detector low-contrast on the gold placeholder letter | Back to the V1 colour |
| Latin labels in Thai `<select>` options | `lang="en"` on options |
| Explore first visual at 610px | Tighter gaps, labels and help kept: 554px EN, 563px TH |

## Tests and evidence (final image)

| Check | Result |
|---|---|
| `tsc --noEmit`, `eslint --max-warnings 0` | Exit 0 |
| `npm test` | PASS 116 / FAIL 0 (85 V1, 13 contrast and boundary additions, 18 locale) |
| Playwright Chrome on the preview | PASS 242 / FAIL 0 (189 V1, one narrowed with its reason; 53 new) |
| Playwright Edge on the preview | PASS 242 / FAIL 0 |
| Image build (type check, lint, tests, build inside) | PASS; preview `sha256:177c02e5e5b9f82b7920a3adaddd51ba8bdd7fc2a83c8771c5db4fec91537eaf`, healthy, `127.0.0.1:3000`, read-only, user `node` |
| `scan-output` on the image's `/app` | No boundary violation; no Thai fixture prose in static chunks |
| Impeccable `detect` | Source: none (regex only). Rendered: `cream-palette` (Owner-approved ivory) and `undersized-ui-text` (10px "BY TK", V11-OD-08) on every route |
| Explore first visual, 1440×900 | 554px EN, 563px TH (target 560; V1 653) |

Changed V1 tests, with reasons in the files: token values (amended), theme-colour location, membership place keys, drawer link scope. V1 image kept as `doomparfum-web:v1-rollback` (`sha256:43be51f1…`). Four protected containers stayed stopped; 32 volumes unchanged.

NOT RUN: screen reader, physical phone, Safari, Firefox, forced colours, 400% zoom on the new pages, clean-clone `npm ci` plus uncached image build, independent review, WCAG 1.4.12 spacing overrides on the new components. These belong to CP5.

## Limits

404 views reach the browser through the framework's error document, which hydrates into the view, so their first byte has no `lang` (V1's unknown-slug 404 behaved the same). Thai Explore is 3px over the 560px target. All Thai text is draft. A05 stays PARTIAL.

## Result and next action

CP0–CP4 complete on the agent side; **not accepted**. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`. Next: the Owner answers the CP4 form. Then CP5: apply the choices, remove unchosen variants (none are in code), full verification, independent review, records and receipt, then a fresh publication authorization.
