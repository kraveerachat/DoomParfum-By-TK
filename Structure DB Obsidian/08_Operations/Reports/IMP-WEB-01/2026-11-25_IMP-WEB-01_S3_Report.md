---
id: IMP-WEB-01-S3-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-25
tags: [doomparfum, implementation, frontend, report, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-01 S3 execution report

**PUBLIC_SAFE / LOCAL_ONLY / NOT_PUSHED / PR_NOT_CREATED.** Task: [[IMP-WEB-01_Luxury_Frontend_Docker]]. Plan: [[DPT-PLAN-012_Luxury_Frontend_Editorial]] (PR #35). Branch `feat/imp-web-01-luxury-frontend`, start `b8383ecb76c4cd72e16129ea319f1f22938be550`, code checkpoint `449178093ed7616570cf651f8b5e4f3cc2d3001e` (after `ad7e1ea`, `32574e8`). Earlier records are unchanged: [[2026-11-24_IMP-WEB-01_S1_Report]], [[2026-11-24_IMP-WEB-01_S2_Report]].

Scope: the Owner's instruction to reconcile the LF-05 CONDITIONAL review and prepare publication. Intake class A (continuation). No design change other than the no-script header row.

## TOOL DECISION / EXECUTION

| Tool | Status | Use |
|---|---|---|
| Impeccable | USED, primary | Skill and the `harden` and `craft-floor` references; `detect` on `web/src` (no findings) and on five rendered routes (only the 10px signature and the ivory ground, both approved tokens). `impeccable context` was not run again |
| Requested Impeccable commands `critique`, `layout`, `bolder`, `overdrive`, `colorize`, `animate`, `adapt`, `audit`, `polish`, `delight`, `distill` | NOT USED | The same instruction forbids another broad polish round |
| UI Craft, UI UX Pro Max, Taste Skill | NOT USED | No further need; `brand` is out of scope by project rule |
| Docker, Playwright, axe, installed Chrome and Edge | USED | Existing installations |
| Read-only reviewer sub-agent | USED | Two rounds, below |

## Evidence preserved (LF-05)

The LF-05 reviewer hand-backs regenerate byte for byte from the reviewer's raw session record. Both are stored outside Git, in an ignored local folder. `PRIVATE_EVIDENCE_NOT_PUBLISHED`: they contain host paths.

| Item | Value |
|---|---|
| Report SHA-256 | `37852101f9ed8a0b9b4defab2c6d7fd6df0fd4aadc113e1282278a9fc6ade290` |
| Raw session record SHA-256 | `2e4be80d2e06a05022e346e9c318790b313963d5d54c90750f6704a3554cfc61` |
| Reviewed | `b8383ec` (code `9918a38`) |
| Reviewer | Claude Sonnet 5.5 sub-agent, fresh context, commissioned by the implementer. Same vendor, not human, not an authenticated independent acceptance |
| Declared limits | Task memory lines were preloaded (stated unused); part of the workflow document and one script unread; A11 not run; no Safari, Firefox, phone or screen reader. Scope was extended twice at the implementer's request, and severity of F-01 was lowered in that exchange |
| Result | CONDITIONAL, no P0 to P2 |

## LF-05 findings

| ID | Disposition in S3 |
|---|---|
| F-01 repeated-slash redirects | **Exception.** The framework answers before `proxy.ts`. Asserted as missing all four headers, same origin, full headers on every later hop |
| F-14 431 | **Exception.** Node's HTTP parser answers. Asserted |
| F-02 redirect test | **Corrected.** Exact status, location and headers from raw request targets; unit test for the origin guard |
| F-03 gutter test | **Corrected.** `scrollbar.spec.ts` runs with visible scrollbars and asserts that state first |
| F-04 fragment test | **Corrected.** The guard's removal now fails it |
| N-01 lock assertion | **Corrected.** Lock value, overflow, wheel, inert background, focus and position are asserted for Escape, Close, scrim and Back |
| F-05 no-script mobile navigation | **Corrected for disabled scripting.** The one primary navigation takes a row below the brand and Menu is not offered. **Recorded limits:** Search, Profile and filters need scripting; where scripts are enabled but fail to load, the narrow Menu does nothing |
| F-06 other methods | **Corrected.** 405 with `Allow: GET, HEAD`, empty body, same headers. Pages read the same afterwards and the container file system shows no change. Works in development mode |
| F-07 query form | **Retained.** `%20` becomes `+` and repeated keys are grouped by the framework. Each key's decoded values and their order are equal; tested |
| F-08 empty areas | **Retained.** Inspected at 1440 and 768; no clipping, orphan or overlap. The Owner proposed keeping the third entry |
| F-09 history fallback | **Retained, now tested** without the Navigation API. Limit: two visits to one URL share state there. Safari and Firefox NOT RUN |
| F-10 "Unknown" | **Not a defect.** The clause is in the Detail wireframe and Detail shows "Unknown". The reviewer withdrew it |
| N-03 unused title | **Corrected** (removed) |
| N-02 | **Record corrected here:** the S1 key `route_metrics_gzip_js_and_cls` holds encoded bytes with headers, not a gzip body |
| F-12 | **Corrected** in the task note ledger |
| N-04, N-05, N-06 | **No change.** Accord cap stays under deviation 5; the S1 and S2 contrast methods are not comparable; dialogs sit outside the page container, so `md:` is required there |
| F-11, F-13 | Closed by the reviewer in LF-05 |

Found in S3: a fragment focus test checked once instead of waiting and failed under repetition in Chrome and Edge; corrected. `next dev` can write its own `web/AGENTS.md`; disabled with `agentRules: false`. NOTICE did not name the unused `sharp`/`libvips` files in the image; added.

## Source and test changes

Source: `src/proxy.ts` (method refusal), `src/app/globals.css` (no-script header), `src/app/perfume/[slug]/page.tsx` (unused title), `next.config.ts` (`agentRules`). Tests: new `e2e/headers.spec.ts`, `e2e/scrollbar.spec.ts`, `tests/proxy.test.ts`; changed `access`, `content`, `helpers`, `isolation`, `refinement`, `regressions` and `playwright.config.ts` (`E2E_ORIGIN`). Documents: `README.md`, `NOTICE.md`. No dependency, route, token, fixture, image or Docker file changed.

RED first on the S2 preview: method refusal (5) and no-script navigation (2). Sixteen product mutations in a scratch copy were each detected by the test that protects them; list in the evidence file.

## Response-header coverage

Not universal. Proxied pages, 404s, RSC, redirects and 405s carry CSP, noindex, nosniff and no-store; owned images omit no-store on purpose. Answered before application code, without those headers: repeated-slash and absolute-form 308, 431, parser 400. Without CSP, noindex and nosniff: `TRACE` and `*` 500. Closed without a response: `CONNECT` and WebSocket upgrade. Hashed assets: noindex and nosniff only. The absolute-form 308 repeats the sender's own target, so "all redirects stay on this origin" holds only for origin-form requests; browsers do not send the other form to an origin server. Risk today: none on a loopback mock. Before any public link the edge must add these headers.

## Commands and results

Environment: Windows host, Node 24.22.3, npm 11.19.1, Docker 28.3.2, Chrome 158.0.8127.38, Edge 158.0.4370.33. Limits: one host, headless browsers.

| Scope / command | Passed | Failed | Skipped | Exit |
|---|---|---|---|---|
| Fresh clone at `4491780`: `npm ci --ignore-scripts` with an empty cache | n/a | n/a | n/a | 0 |
| Same clone: `typecheck:gen`, `lint`, `validate:fixtures`, `build` | n/a | n/a | n/a | 0 each |
| Same clone: `npm test` | 85 | 0 | 0 | 0 |
| Same clone: `docker build --no-cache --target runner` | 85 unit inside | 0 | 0 | 0 |
| `docker compose config --quiet`, preview and dev | n/a | n/a | n/a | 0 each |
| `docker compose up --build --force-recreate --detach` | n/a | n/a | n/a | 0 |
| `playwright test`, final preview, Chrome | 189 | 0 | 0 | 0 |
| Same, Edge (same engine family) | 189 | 0 | 0 | 0 |
| `playwright test --repeat-each 4`, before the review corrections | 748 | 0 | 0 | 0 |
| `scan:output` on the final image | 194 files, 17 scripts | 0 | n/a | 0 |
| `npm audit` / `npm audit signatures` (clone of `ad7e1ea`, same lockfile) | 0 vulnerabilities / 117 attestations | 0 | n/a | 0 |
| Stock `database/validate_docs.py` | n/a | stops at a binary file | n/a | 1, unusable on this branch |

Initial JavaScript 160.0 to 163.9 KiB, CLS at most 0.0235. The preview and the fresh-clone image have identical files under `.next/static` (23), `public` (18) and `.next/server` (140).

Scans: no secret, e-mail or host path in lines added since the base; no remote URL in application source; no forbidden file tracked; 463 of 463 lockfile entries from the npm registry with integrity; font hashes match NOTICE.

## Independent review of S3

Claude Sonnet 5.5 sub-agent, fresh context, read-only; same limits of independence as LF-05. Report SHA-256 `91c59dcc1e786d13977e00b913bcc54b6d2c1d99f8851497fee9a9eb06667f9c`, kept outside Git.

| Round | Commit | Result |
|---|---|---|
| 1 | `32574e8` | CONDITIONAL, no P0 to P2. Asked for F-05 wording, a parser-400 row, and tests of two CSS branches |
| 2, delta only | `4491780` | PASS for the code. Conditions recorded or closed; Owner items open |

Not done by the reviewer: visuals, axe, `npm ci`, Docker build, A10, A11. It is not human or cross-vendor and gives no Owner acceptance. The commit message of `ad7e1ea` lists F-05 without its limits; `4491780` and this report correct it.

## Acceptance matrix (S3)

| ID | Result | Evidence and limits |
|---|---|---|
| A01 | PASS | Suite |
| A02 | PASS | Suite, unit controls, fixture validation |
| A03 | PASS | Suite, unit |
| A04 | PASS | Suite |
| A05 | PARTIAL | Keyboard, trap, Escape, focus and history in Chrome and Edge; keyboard at real 200% and 400% zoom. Screen reader, real phone, Safari, Firefox NOT RUN |
| A06 | PASS with exceptions | HTML and RSC no-store, isolation and image scan. The pre-proxy exceptions above are not covered |
| A07 | PASS (automated) | axe, token pairs, forced colors emulated. Not a WCAG conformance claim |
| A08 | PASS | Widths, landscape, spacing, Thai (emulated); real Chrome zoom 200% and 400% on seven routes, 0px overflow |
| A09 | PASS | Suite |
| A10 | PASS | Compose config, uncached release build, non-root, read-only, no capabilities, no mounts, no other container on its network, healthy, loopback only; 11 non-loopback host addresses refused. Second-machine LAN probe NOT RUN (none available) |
| A11 | PASS | With the Owner's approval: dev on the fixed URL, hot reload 0.8 s without reload and reverted, both mode conflicts and a port conflict stopped safely, failed build kept the preview image, restart, teardown left no task container, preview policy checked after |
| A12 | PASS (local) | Budgets, reduced motion, rapid toggles, no-script |

## Owner decisions (all PENDING)

| Item | Agent recommendation |
|---|---|
| 1 Route loading keeps the current page | Retain |
| 2 Hero padding 32/40 on shorter desktops, 80/80 where it fits | Retain; 80/80 puts the Featured heading at y = 963 at 1440 x 900 |
| 3 Fixed optical size | Retain |
| 4 No Radix overlay part | Retain (required by the CSP) |
| 5 Four accord descriptors and two sort orders | Retain |
| 6 16px text links | Retain |
| 7 House label beside the marker | Retain |
| S2: tablet 4:3 visual, horizontal third entry, redirect in `proxy.ts` | Retain |
| S3: no-script navigation row; 405 for other methods | Accept |
| Header exceptions | Accept for the loopback mock; revisit before any public link |
| A05 manual checks | Run, or defer explicitly |

The S3 brief lists the first group as proposals and says to keep them PENDING until the Owner confirms.

## NOT RUN

Screen readers, physical phones, Safari, Firefox, real forced-colors hardware mode, second-machine LAN probe, Ubuntu host, load testing, database, matching, ETL and U01 suites, human or cross-vendor review. No CI workflow exists in the repository.

## Protected resources

The four protected or unrelated containers, all volumes, other worktrees and refs compare equal before and after. With the Owner's approval only `doomparfum-web` was stopped and recreated. Images now: `preview` (S3), `s2-rollback` (the previous preview), `dev` (rebuilt). Temporary S3 containers, network and volumes were removed by name. No prune.

## State

ACCEPTANCE PENDING. No push, PR, merge, deployment or receipt: A05 and the Owner decisions are open.
