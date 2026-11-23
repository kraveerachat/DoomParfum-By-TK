---
id: IMP-WEB-01-S1-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-24
tags: [doomparfum, implementation, frontend, report, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-01 S1 execution report

**PUBLIC_SAFE / LOCAL_ONLY / NOT_PUSHED / PR_NOT_CREATED.** Task: [[IMP-WEB-01_Luxury_Frontend_Docker]]. Approved plan: [[DPT-PLAN-012_Luxury_Frontend_Editorial]] (Planning PR #35, merge `61932bef147816272a06cbe6eba9363940fa4baf`). Branch `feat/imp-web-01-luxury-frontend`. Code checkpoint `a5ddd6fe421870d2adeeac70f3e7150eee798890`.

## TOOL DECISION / EXECUTION

| Tool | Status | Use |
|---|---|---|
| Impeccable (project skill) | AVAILABLE, USED as primary | `context` once; `craft-floor`, `operate`, `mode-persuade` and `new-work` references consulted; `detect` on `web/src` (no findings); shipped finish reviewer as an independent design reviewer. `live`, `generate`, hooks, login, asset producer and manual-edit applier NOT USED |
| Requested `/impeccable` lenses (critique, layout, bolder, overdrive, colorize, animate, adapt, harden, audit, polish, delight, distill) | USED as bounded review lenses | Not executed as twelve separate command runs, and no numeric score was produced. Overdrive stayed within the plan's restrained-motion rule |
| UI Craft (`ui-craft-editorial`) | AVAILABLE, consulted | Skill file read as a secondary editorial reference; its font, drop-cap and palette defaults conflict with the approved tokens and were not applied |
| `ui-ux-pro-max:brand` | AVAILABLE, REQUESTED_BUT_NOT_USED | The project rule places the `brand` skill out of scope for DoomParfum UI; the approved tokens are the brand authority |
| Taste Skill | AVAILABLE, NOT USED | No specific added benefit |
| Docker Desktop 28.3.2 | Started once on the Owner's explicit chat authorization | Only resources named `doomparfum-web*` were created, started or stopped |
| Playwright 1.65.1, axe 4.14.0, installed Chrome | USED | Pinned dev dependencies; no browser was downloaded |
| npm registry, OSV, GitHub advisories, Docker Hub | USED | Read-only version and advisory checks, dependency and image downloads |

## Work performed

- CP1 `f9dc22fa9afcbca128b32d1c7201aa4c8fd14feb`: pinned stack, fixtures, strict validator, five routes, original studies, nonce CSP, Dockerfile, preview and dev Compose files, first healthy startup.
- CP2/CP3 `f04d912731d3b631e9446804e265500af81a9b1e`: header, dialogs, Home, About, Explore, Detail, Notes, navigation memory, acceptance suite, fixes from the first render and the first run.
- CP4 `a5ddd6fe421870d2adeeac70f3e7150eee798890`: corrections from two independent reviews, 25 browser regressions, token-contrast test, README.

Exact files: `git diff --name-only 61932be a5ddd6f` (94 files, all under `web/` except the task note).

## Checks with results

| Check | Result |
|---|---|
| `tsc`, ESLint (zero warnings), fixture validation, `next build` | PASS, also enforced inside the image build |
| Unit, negative-control, boundary and contrast tests (`npm test`) | PASS 81, FAIL 0 |
| Browser acceptance suite against the Docker preview | PASS 117, FAIL 0, SKIPPED 0 |
| Review regressions before the fix, on `f04d912` | 22 FAIL, 3 PASS (RED); all 25 PASS after |
| `npm audit`; OSV batch for direct pins | 0 vulnerabilities; no advisories (2026-11-24) |
| Runtime image scan (`scan-output`) | PASS: 194 files outside `node_modules`, 17 immutable scripts; wrong-directory control exits 1 |
| Impeccable detector on `web/src` | No findings (not a conformance claim) |
| Display stem contrast, sampled from 1x renders of the Notes h1 | First version 1.52:1 at 1440 and 1024. Final 4.22:1 at 1440 and 1024, 3.89 to 5.28:1 at 375. 320 not measured validly |
| Initial JavaScript per route / CLS | 160.0 to 163.8 KiB compressed / 0.0235 maximum (budget 200 KiB / 0.1), one local headless Chrome run |

Machine-readable: [IMP-WEB-01_Acceptance.json](../../Test_Evidence/IMP-WEB-01/IMP-WEB-01_Acceptance.json), with seven screenshots beside it.

## Acceptance matrix

| ID | Result | Evidence and limits |
|---|---|---|
| A01 | PASS | Five routes, titles, noindex, 404s, invalid filters, reload, Back, link crawl. Limit: a malformed percent-encoded path returns a header-complete 404 with an empty body, not the unavailable view |
| A02 | PASS | 12 studies and details marked; 35 negative controls in unit tests; four field states distinct |
| A03 | PASS | Exact ids and counts, 120 code points, literal HTML, announcement once, no query in any request |
| A04 | PASS | Layers, general notes and accords separate; note counts match; unsupplied relationship never shown as zero |
| A05 | PARTIAL | Keyboard, trap, Escape, focus return, history and fragments PASS in Chrome. Screen reader, real phone with virtual keyboard, Safari and Firefox NOT RUN |
| A06 | PASS | CSP, no-store, noindex, same-origin, no storage or worker, no fixture in immutable assets, image scan. Limit: framework 308 redirects carry no noindex header |
| A07 | PASS (automated) | Tokens, pairs, composed scrim, axe on nine pages and all dialogs, blocked fonts, broken visual, render error. Automated checks do not prove WCAG conformance |
| A08 | PASS | Seven widths, landscape, 200% text at 1280/375/320, 320 CSS px reflow, text spacing, Thai. Emulated viewport; real browser zoom UI NOT RUN |
| A09 | PASS | Offset at most 1px at 1024, 1280 and 1440, with asymmetric stress and 200% fallback |
| A10 | PASS | Non-root, read-only, no capabilities, no mounts, `127.0.0.1:3000`, healthy; non-loopback host address refused. Second-host LAN probe NOT RUN |
| A11 | PASS | HMR 1.3 s without reload and reverted; mode and port conflicts stop safely; failed builds left the previous container serving; cold restart without rebuild; teardown left no task container |
| A12 | PASS (local) | Budgets above, no console or CSP error, reduced motion, rapid toggles, no-script content |

## Independent reviews (read-only, commit `f04d912`)

Both reviewers were subagents of this same session, separate from the implementer's context but not a different organization or model vendor. They are not the LF-05 gate and not an approval. Neither reviewed `a5ddd6f`; **independent closure is PENDING**.

- Code review: 0 BLOCKER, 2 HIGH, 6 MEDIUM, 4 LOW. All twelve addressed, except the redirect-header sub-item recorded as a limitation.
- Design review: 0 BLOCKER, 3 HIGH, 8 MEDIUM items and one LOW batch. Addressed, except the recorded deviations below.

## Deviations and limitations for the Owner

1. Route loading: placeholder boundaries broke forward focus and no-script content, so they were removed. A slow transition keeps the current page, sets `aria-busy` and shows a short status after 400 ms.
2. Home hero padding is 48/24px on desktop, not 80/80: the plan also requires the start of Featured to be visible at 1440 x 900, and both cannot hold.
3. Bodoni Moda optical size is fixed (6 to 18) because the automatic size made hairlines almost invisible. Family, weight and size are unchanged.
4. The Radix overlay part is not used; it injects a style element that the CSP rejects. Closing is immediate and an inert copy fades.
5. Four fictional accord descriptors exist because the contract requires descriptor IDs without a stated limit. Sort offers the two name orders only. The middle Featured item is offset by 64px.
6. Standalone text links stay at 16px on desktop; buttons and labels follow the 15px control role.
7. The house label sits beside the Mock marker, above the h1, at every width.
8. ESLint 9.39.5 is past upstream support; the React lint plugin does not yet accept ESLint 10. Development only.
9. The bridge network allows container egress. The application makes no outbound request; egress is not blocked at network level.
10. After a rebuild, Compose once kept the old container running. Documented commands use `--force-recreate`, and results here were accepted only when container and image ids matched.
11. Unit tests were written with the implementation, not before it. Only the review regressions have RED evidence.
12. The stock document validator cannot run on this branch: it decodes every changed file as UTF-8 and stops at the font binaries. Unmodified; a scoped document check was used instead.

## NOT RUN

Screen readers, physical devices, Safari, Firefox, browser zoom UI, forced-colors rendering, second-host LAN probe, Ubuntu host, load testing, database, matching, ETL and U01 suites (untouched), independent review of the final commit.

## State

No push, PR, merge, deployment, public port, credential, real data or external runtime request. Task state: ACCEPTANCE PENDING. Final receipt: NOT CREATED, because LF-05 and the A05 manual checks are open. Preview container left running on loopback for Owner review.
