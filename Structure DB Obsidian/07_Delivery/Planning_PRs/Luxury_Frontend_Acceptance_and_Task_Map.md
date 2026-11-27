---
id: DPT-PLAN-012-ACCEPTANCE
project: DoomParfum By TK
type: acceptance_and_task_map
status: proposed
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, acceptance, task-map, mock-frontend]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# Luxury frontend acceptance and implementation task map

Parent [[DPT-PLAN-012_Luxury_Frontend_Editorial]]. Implementation is NOT STARTED. This map proposes review units, not allocated global task IDs or permission to run them. After Owner merges this Planning PR, re-read the merged exact SHA and obtain bounded implementation authority. Each allocated task has one branch, one Draft PR and one final receipt; dependent work cannot be merged by an agent. Small checkpoints remain in that task's branch/PR.

## Traceability and preservation

| Requirement / prior plan | Mock demonstration / evidence | What remains future |
|---|---|---|
| R01 discovery, R04 filter intent | Five routes; only fictional local browse/filter; tests A01/A03 | Real catalogue coverage and real metadata filters |
| R03 olfactory layers, R13 pyramid, R14 note navigation | Labelled Top/Heart/Base, separate general notes/accords, local note cross-links; A04 | Licensed note images, real taxonomy/data permissions; this slice does not satisfy real-data R03/R13 |
| R21 provenance intent | Synthetic ownership/version marker and no acquired data; A02/A06 | Real-source licensing/provenance acceptance |
| Unified IA / AM-05/AM-06 | Mock navigation, states and responsive presentation | Does not replace future compare/cart/collection/operator routes |
| APP-07 / conservative cache direction | Ephemeral runtime view model, no persistent catalogue cache; A06 | Offline PWA/cache and private-data policy remain gated |
| DPT-DOC-004 mock-shell proposal | New five-route expansion, original art, local-only shell | New Gate P required; no automatic approval from PR #34 |
| U01 / POST30 decisions | No authentication/private data, security gates preserved | U01 independent r14 review and real-data prerequisites unchanged |

R02/R06/R08/R22 real-brand/geography/budget features remain future. R05/R07/R15/R16/R17/R18 matching/compare/evidence are not implemented. R09–R11/R23–R31 private cart/purchase/collection remain future; Cart is never checkout. No prices, scores, match percentages or ownership are displayed. PR #8 remains deferred/open Draft and is not a prerequisite for this mock scope.

## Proposed implementation units and dependencies

| Local unit | Scope / role | Prerequisite | Exact evidence / acceptance | Do not touch |
|---|---|---|---|---|
| LF-01 | Codex implementation: pin stack, create isolated `web/` shell, semantic tokens and five route skeletons, fixture validator, minimal Docker preview/dev configs | Owner-merged DPT-PLAN-012 + bounded dependency setup and local image/container authority | Pinned lockfile/image records; TypeScript/build checks; A01/A02/A06 source checks; minimal loopback startup/stop proof before rendered evidence in LF-02 | Existing Python, DB, Matching, U01; no host-wide install/public exposure |
| LF-02 | Codex implementation: original synthetic content, header, Home, About, Search/Profile dialogs | LF-01 merged | A01/A03/A05/A07/A09, original asset/font notices; rendered desktop/mobile evidence | No auth, remote imagery or extra route types |
| LF-03 | Codex implementation: Explore, Detail, Notes, filter and field states | LF-02 merged | A02–A06/A08; known/unknown/empty negative controls, keyboard paths | No real imports, scores, personal state or API |
| LF-04 | Codex implementation/runtime: harden the LF-01 Docker configs, full preview/dev/recovery smoke tests | LF-03 merged + current bounded local image/container authorization | A10–A12; exact image digest, configs, binding, stop proof | No host-wide install, firewall, tunnel, cloud or Production |
| LF-05 | Independent read-only design/a11y/code reviewer; authorized docs agent reconciles findings | Exact LF-04 candidate SHA, all required evidence | Review exact source and all five routes; focused correction retests; one final receipt for the relevant task | Reviewer writes no repo files; Human Owner alone merges |

Units may be combined by the Owner into one coherent implementation task/PR to avoid unnecessary serial overhead; until then this is a proposed allocation. Independent reviewer does not self-approve implementation. No multi-agent implementation or automatic task execution is authorized by this map.

## Acceptance and future test plan

All Axx tests below are NOT RUN in this documentation session. Planning validation checks documents and proposals only.

| ID | Test and fixtures | Observable pass condition |
|---|---|---|
| A01 Routes / navigation | `/`, `/explore`, `/perfume/paper-study-a`, `/notes`, `/about`; unknown slug and invalid URL filters; reload and Back | Five intended route types work with truthful titles/noindex; unknown slug returns 404 and unavailable view; no dead Journal link or fake auth route. |
| A02 Fixture truth | Known/unknown/empty layers, missing visual, duplicate slug/ID, invalid note, extra price/score/review/source field, synthetic false | Valid distinctions render accurately; invalid fixtures rejected before build. Every fixture entry and direct detail entry visibly says Mock/Synthetic. No invented real facts. |
| A03 Search / filters | Empty query, mixed case/Unicode, no results, 120-code-point boundary, HTML-looking text; family+note intersection; clear/reset; same-tab return | Shared deterministic semantics; exact fixture IDs/counts; no regex/HTML execution; focus retained; count announced once; no search network request or persistent query. |
| A04 Layer and note navigation | Known layered/general/accord fixtures and unknown membership | Top/Heart/Base and general notes/accords remain separate; note links reach actual local membership; no weights, recipe, confidence or similarity claim. |
| A05 Keyboard / screen reader | Tab/Shift+Tab/Enter/Space/Escape; Menu/Search/Profile; forward and history navigation; real phone virtual keyboard in portrait/landscape | Visible focus, correct names/current states, working skip link; one overlay, trapped focus only while open; Escape closes and trigger focus restores; forward navigation focuses destination h1, history restores entry focus/scroll; Search input/Close/results remain reachable with keyboard open. |
| A06 Isolation / cache / network | Source and production-output scan plus network recording on initial load, route transition, search, filters, profile/menu, notes and errors | No DB/matching/private imports, credential/env files, external runtime requests, persistent catalogue storage or service worker. HTML/RSC responses no-store, payload not embedded in immutable client chunks. Only same-origin framework/owned assets. |
| A07 Visual / contrast | All text/control token pairs, composed scrim, focused/hover/error/selected states; fonts loaded and blocked | Normal text ≥4.5:1, large text/control indicators ≥3:1; gold/divider restrictions respected; no clipping, overlap, invisible labels or missing artwork fallback. |
| A08 Reflow | 320, 375, 640, 768, 1024, 1280, 1440 CSS px; 812×375 landscape; 200% text; 400% zoom at 1280; long Latin and Thai labels; WCAG 1.4.12 spacing overrides (line-height 1.5×, paragraph spacing 2×, letter spacing .12em, word spacing .16em, using properties applicable to the script) | No horizontal page scroll, lost content, clipped controls or inaccessible action, including with spacing overrides; documented columns/order; ≥44px product targets; drawer scroll/close accessible in landscape. |
| A09 Header geometry | 1024/1280/1440px, fonts ready; asymmetric side-width stress and 200% text | Nav center within 1px of inner container center, equal side tracks, no overlap; narrow fallback when content cannot fit. |
| A10 Docker preview | Compose config, release image build, standalone assets, non-root process, health response, local browser all routes, LAN probe if available | `web`, `doomparfum-web`, container 3000, host `127.0.0.1:3000:3000`, fixed URL; all assets load; no other service/mount/data; no public listener. Record LAN probe not tested if no second host. |
| A11 Docker dev / recovery | Separate dev config, HMR on web source change, port conflict, failed build, stop/restart modes | Same fixed URL, only one mode active; dependency volumes isolated; conflict stops safely; preview policy not weakened; explicit teardown leaves no task container running. |
| A12 Performance / motion | Production build, five route smoke tests, reduced motion, rapid dialog toggles; recorded browser/tool versions and conditions | No render-blocking external asset; reserved visual dimensions; no console errors/CSP failures; reduced motion immediate; rapid changes leave correct focus/scroll state. Proposed budgets: ≤200KiB gzip initial client JS per route and ≤0.1 measured CLS under the recorded local run; failures require review, never a fabricated score. |

Use existing repo tooling only where applicable. Future test candidates: TypeScript/build checks, unit tests for fixture/filter/state logic, browser automation for routes/focus/geometry/network/storage, axe for automatable a11y plus manual keyboard/screen-reader checks, local production metrics. Pin and approve any new tool/dependency first. Automated a11y never proves WCAG conformance. No fake numeric design-health score for unbuilt screens.

## Bounded visual verification

After a complete implementation, one batched inspection round covers desktop/tablet/phone and all five routes plus representative states. Fix all observed defects in one batch, then at most one confirmation round. New unresolved accessibility/correctness failures block handoff and need a specifically scoped next task; do not report them as passed or polish indefinitely. No screenshots or metrics from this planning study are evidence that DoomParfum renders correctly.

## Owner decision packet

| ID | Proposed choice | Status / consequence |
|---|---|---|
| LF-OD-01 | Five-route mock scope and fixture boundaries in this packet | PROPOSED; needs Gate P merge |
| LF-OD-02 | Ivory/ink/gold/navy editorial direction, restrained motion | Owner confirmed brief direction in chat; exact token/layout implementation remains PROPOSED |
| LF-OD-03 | Next.js/TypeScript/Tailwind/selective primitives for `web/` only | PROPOSED; does not answer broader backend/framework decisions |
| LF-OD-04 | Docker-first loopback preview/dev contract | PROPOSED; no container-operation authorization yet |
| LF-OD-05 | Public link later with noindex, via separate Cloudflare plan | DEFERRED deployment; no privacy/auth boundary implied |

No blocker in PR #8, U01 or real-source permissions prevents reviewing the mock plan. Those gates remain mandatory before their own future scopes. Publish requires new scoped publication identity/authorization; this task stops at a local checkpoint and proposed Draft PR body. Human Owner reviews and merges both planning and implementation PRs.

## Amendment DPT-PLAN-013 — Frontend V1.1 (MERGED 2026-11-26, PR #37 `3e87027`)

LF-01 to LF-05 were delivered by [[IMP-WEB-01_Luxury_Frontend_Docker]] (PR #36, merged `ab3351a8432d1d6664a6b4281784cfea56b0b9fa`); A05 stays PARTIAL. Contract: [[DPT-PLAN-013_Frontend_V1_1_Amendment]], sections 9 to 11.

| ID | Extension for V1.1 |
|---|---|
| A01 | Ten URLs, both languages, both 404 views |
| A08 | Adds 390 and 1920px, Thai text at every width, two-row header reflow |
| A09 | Adds 1920px and both languages; right-side stress 200 to 260px |
| A02–A07, A10–A12 | Rerun unchanged, for both languages where text or routes are involved |
| V01–V16 | New, defined in the amendment; all NOT RUN |

Proposed unit: `IMP-WEB-02`, one branch and one PR, checkpoints CP0–CP5. Prerequisite: this amendment merged by the Owner and its SHA verified. Owner decisions: V11-OD-01 to V11-OD-12.
