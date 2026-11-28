---
id: IMP-WEB-02-S9-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, routing, verification, closeout, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S9 — authorized 404 correction and closeout

PUBLIC_SAFE. Agent: Claude Code. Intake class A (continuation of [[IMP-WEB-02_Frontend_V1_1]]). Owner instruction "IMP-WEB-02 — Final 404 Resolution and Closeout" (2026-11-28). Verified at start: HEAD `763b678` (records), `web/` equal to `253bf48`, base `3e87027` equal to remote `main`, preview `dedbba40…` healthy, branch not on the remote.

**Result: the 404 defect found in S7 is fixed, with the Owner-authorized experimental `globalNotFound` correction (S7 option E6) and nothing else. Final candidate `53d01265962059655764f8d65be5b71329e600c4`; preview restored on image `sha256:568cc3b30f8fef993d5db66e2e6f2bbfd5c6536c874b7786d3385d53c66f701e`. Independent review: CONDITIONAL on `3b93945` (runtime not reachable), then PASS on `53d0126`.**

## Owner authorization (recorded)

Bounded to the experimental `globalNotFound` correction tested in S7, on the pinned Next.js 16.4.6 and the local mock frontend only. Not authorized: dependency upgrades, other experimental features, routing restructure. Condition: the experimental dependency is documented and needs a compatibility reassessment before any framework upgrade or production deployment (recorded in `web/next.config.ts`, the task note, the Decision Log and the Draft PR package). The Owner's visual acceptance (S8) stands.

## Change (`253bf48` → `3b93945` → `53d0126`, `web/` only)

| File | Change |
|---|---|
| `next.config.ts` | `experimental: { globalNotFound: true }`, with the authorization and reassessment condition in a comment. The only experimental flag |
| `src/app/global-not-found.tsx` (new) | Full document: the existing `RootShell` and `UnavailableView` in the request's locale; localized title (`Unavailable · …` / `ไม่พบหน้านี้ · …`); noindex metadata; existing viewport |
| `src/proxy.ts` | Sets `x-doomparfum-locale` from the path on every request, replacing any client value; rewrites malformed addresses and unknown detail slugs to `/_unavailable` (English) or `/th/_unavailable` (Thai), paths no route uses; trailing-slash redirect, 405 and headers unchanged |
| `src/i18n/locale.ts` | `LOCALE_HEADER` constant |
| `src/app/(en)/[...missing]`, `src/app/th/[...missing]`, `src/app/(en)/unavailable`, `src/app/th/unavailable` | Removed (each only called `notFound()`) |
| `src/app/global-error.tsx` | Two eslint-disable lines removed; the rule no longer fires once the catch-alls are gone, so `--max-warnings 0` failed. Markup unchanged |
| `src/views/unavailable.tsx` | Comment only |
| `tests/boundaries.test.ts` | `proxy.ts` added to the fixture-import allowlist (server-only; `scan:output` still fails on fixture text in client assets) |
| `tests/proxy.test.ts`, `e2e/locale.spec.ts`, `e2e/helpers.ts` | Regression tests (below); `raw()` takes optional request headers |

Kept unchanged: `app/(en)/not-found.tsx`, `app/th/not-found.tsx` and `notFound()` in the detail view (now unreachable for detail paths: the proxy and the view read the same validated slugs, asserted by a unit test).

## Root cause of the per-locale targets (review finding 1)

With one rewrite target, rewritten Thai addresses rendered in English. An instrumented scratch build (outside the repository, stopped afterwards) showed why: Next.js 16.4.6 runs the proxy **a second time** on a rewrite target that matches no route, with the first pass's headers, and that pass derived the locale again from `/_unavailable`. Log: `proxy GET /th/perfume/nope incoming-locale=null` → `proxy GET /_unavailable incoming-locale=th` → `gnf header=en`. Per-locale targets keep the locale derived from a path the proxy controls. A client-sent value is overwritten on both passes.

## Verification

| Check | Result |
|---|---|
| Unit (`npm test`) | 122 / 0 (119 before + 3 new) |
| Type check, lint, `next build` | exit 0; build lists only `globalNotFound` under experiments |
| Chrome / Edge, scratch build 127.0.0.1:3300 | 305 / 305 each |
| Chrome / Edge, preview 127.0.0.1:3000 (final image) | 305 / 305 each (independent reviewer also 305/305) |
| `3b93945` image on a temporary hardened container 127.0.0.1:3100 | Chrome 302 / 302, Edge 302 / 302 |
| Output isolation scan of the final image's `/app` | No boundary violation (280 of 1403 files, 25 immutable scripts) |
| Raw-HTTP probe, final preview: 10 valid routes, 17 unknown addresses, header spoofing, methods | All checks pass: valid 200; every unknown 404 with server `lang`, localized title, heading and notice, no error document, nonce on every script, no-store, noindex, no external URL; locale ignores `x-doomparfum-locale`, `Accept-Language` and cookies; POST/PUT/DELETE 405, HEAD 404 |
| Same probe on the old preview `dedbba40` | 17/17 unknown addresses are the error document without `lang` |
| New tests against the old candidate | e2e 18 fail / 1 pass (the pass is the 405 check, already correct); proxy unit 2 fail / 4 pass |
| JavaScript disabled (Chrome) | 404 in both languages: lang, title, heading, notice, header; the return link reaches `/th/explore` in Thai |
| Ten valid routes, old vs candidate, 1440 and 390 px | Text, lang and title identical 20/20; screenshots identical on every page that is deterministic on the old image (the 4–5 differing pages differ old-vs-old too) |
| External runtime requests | None (isolation suite, probe, no-JS run) |

Regression tests that catch the S7 behavior: raw-HTTP 404 documents for 16 addresses (no `__next_error__`, server `lang`, title, h1 and notice without scripts, nonce, no-store, noindex); spoofed locale headers on direct and rewritten paths; repeated and interleaved requests (language and fresh nonce); HEAD on a 404; valid escaped slugs; writes refused; no-JS rendering; proxy unit tests for the locale header, rewrite targets and slug parity. Evidence: [S9 verification](../../Test_Evidence/IMP-WEB-02/S9/IMP-WEB-02_S9_404_Verification.json).

## Independent review

Same-vendor read-only sub-agent, separate context ([[2026-11-28_IMP-WEB-02_S9_Delta_Review_3b93945]], [[2026-11-28_IMP-WEB-02_S9_Delta_Review_53d0126]]). First pass on `3b93945`: **CONDITIONAL**, no code defect; one should-fix (undiagnosed locale behavior) and test gaps; runtime unreachable. All addressed in `53d0126`. Second pass at runtime: **PASS** (305/305, 122/122, 108 raw-HTTP checks). Accepted nits: the proxy imports the fixture module (server-only, image scan clean); two slug lookups read the same object (comment and unit test guard drift); `//host/` redirects to a same-site path without `Cache-Control` (pre-existing, framework collapses slashes); `/th%2F…` is English by the contract rule (pre-existing). The reviewer's two unverified items are covered here: the final image's scan is clean, and the image was built from a clean `web/` tree at `53d0126`.

## Preserved

T1–T8; all approved translations and the pinned Thai wording test; reviewed Thai search behavior; A05 PARTIAL with the Owner's deferral; A11 evidence (the runtime image, Compose files and Dockerfile are unchanged; the preview was rebuilt and recreated the same way). No design-tool cycle or cosmetic change.

## Runtime and do-not-touch surfaces

Docker Desktop stopped during the session; the Owner approved restarting it (2026-11-28, in this session). Preview `doomparfum-web` on `127.0.0.1:3000`: image `568cc3b3…`, healthy, read-only root, user `node`, all capabilities dropped, `no-new-privileges`, loopback only. Rollback tags: `253bf48-rollback` and `s6-final` (`dedbba40…`, the S6/S8 preview), `s9-candidate1` (`10ded624…`, `3b93945`); older tags unchanged. The temporary candidate container and scratch servers (3100, 3300, 3301) were stopped and removed. The four other containers (all exited) and the 32 volumes are unchanged; no prune. Database, PR #8, U01/r14, matching and ETL untouched.

## Not done

Physical Notes shortcut test (click Notes, Win+Shift+S, Escape): **not performed**; the S8 Owner screenshot is an observation, not this test. It stays open until the Owner confirms it or explicitly defers it. A05 manual checks (screen reader, phone, Safari, Firefox) remain deferred. No push, no PR, no merge, no receipt.

## State

**Acceptance status:** automated verification PASS and independent review PASS on `53d0126`; visual design ACCEPTED by the Owner; 404 item CLOSED (fixed). Open: the Notes physical test (Owner confirm or defer) and publication authority. A05 PARTIAL, deferred by the Owner. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`.

**Publication readiness:** ready to publish as a Draft PR ([[IMP-WEB-02_Draft_PR_Package]], head `53d0126` plus the S9 records commit; base `main` still `3e87027`). Needs fresh scoped publication authorization. The final receipt follows the Owner's Notes answer.

**Next development:** [[IMP-WEB-02_Next_Slice_Decision_Packet]] (not started).
