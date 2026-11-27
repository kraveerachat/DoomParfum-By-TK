---
id: IMP-WEB-02-S7-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, routing, verification, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S7 — 404 language investigation (blocked on an Owner decision)

PUBLIC_SAFE. Agent: Claude Code. Intake class A (continuation of [[IMP-WEB-02_Frontend_V1_1]]). Owner instruction "IMP-WEB-02 — Targeted Final Acceptance Correction" (2026-11-28). Verified at start: HEAD `e755f07`, `web/` equal to `253bf48`, preview `dedbba40…` healthy, nothing on the remote.

**Result: the 404 behavior does not meet the contract, and no correction within the approved architecture exists. The tested compliant correction needs changes the Owner reserved (experimental `globalNotFound`, a routing change, proxy rules beyond 4.2). No application code was changed.** Candidate stays `253bf485d40a9e4367db8968cf0d0d59faf8f127`; preview unchanged.

## Actual behavior of the candidate (raw HTTP)

Every case below returns **status 404** with a nonce CSP, `no-store` and `noindex`, and the body is Next.js's fallback error document `<html id="__next_error__">` with **no `lang`, no heading and no mock disclosure**. With JavaScript disabled the page is **empty** (0 characters). With JavaScript the browser renders the correct unavailable view after hydration (`lang` en or th, localized heading), which is all the existing browser test checked.

| Case | Targets |
|---|---|
| Unknown English paths and slugs | `/does-not-exist`, `/a/b/c`, `/perfume/no-such-study` |
| Unknown Thai paths and slugs | `/th/does-not-exist`, `/th/perfume/no-such-study` |
| Unsupported locale prefixes | `/en`, `/en/explore`, `/TH`, `/fr` |
| Malformed addresses (proxy rewrite) | `/%E0%B8`, `/th/%E0%B8` |
| Rewrite targets | `/unavailable`, `/th/unavailable` |

Evidence: [S7 404 investigation](../../Test_Evidence/IMP-WEB-02/S7/IMP-WEB-02_S7_404_Investigation.json).

## Contract reconciliation

| Clause | Status |
|---|---|
| 4.2: two root layouts chosen because they give "the right `<html lang>` from the server"; spike must show "Server `lang` on first byte" | **Not met for 404 documents** |
| V01: unknown slugs and paths "return 404 in the right language" | 404 met; language only after hydration, none in the server document: **not met** |
| 4.3: 404 text is localized | Localized in the browser only; empty without scripting |
| V02: Thai pages contain only Thai or marked text | No violation (the 404 document has no text) |
| V15: CSP, noindex, no-store, method refusal, origin and network isolation on both 404 views | **Met** (raw headers) |
| V1 baseline | V1 served unmatched URLs as a full English 404 (`lang="en"`, heading, readable without scripting); its unknown-slug 404 already used the error document. V1.1 extended the error document to every 404: a regression |

Record correction: the S1 spike row says the 404 cases were "proven"; S1's own limitations line already stated that 404 first bytes had no `lang`. The spike requirement was therefore not met, and the browser test (`locale.spec.ts`, "is a real 404 in its language") checks only the hydrated page. S1 and S6 records are left unchanged; this report corrects them.

## Root cause

All 404s come from `notFound()` thrown inside a page: the per-tree catch-all `[...missing]`, the detail page for an unknown slug, and the `/unavailable` route the proxy rewrites malformed addresses to. React server rendering does not run error boundaries, so the not-found boundary cannot render on the server; Next.js 16.4.6 sends its fallback error document with the 404 status and the browser renders the view after hydration (`next/dist/server/app-render/app-render.js`, error shell `id: '__next_error__'`). V1 served unmatched URLs through the root `/_not-found` route, which renders the view as a page; with two root layouts that route has no layout to compose with. The bundled Next.js documentation says exactly this and names `global-not-found.js` (experimental) as the answer for multiple root layouts.

## Corrections tested (scratch clone outside the repository only)

| ID | Change | Result |
|---|---|---|
| E1 | Remove `htmlLimitedBots` | No change |
| E2 | `dynamic = "force-dynamic"` instead of `connection()` | No change |
| E3a | `<Suspense>` around page content | Server `lang`, but **status 200**: rejected |
| E3b | Proxy rewrite with `status: 404` to a page that renders the view | Full localized server HTML, but Next.js **ignores the rewrite status (200)**: rejected |
| E4 | `experimental.globalNotFound` + `app/global-not-found.tsx` (shared shell and unavailable view, language from a proxy path header), catch-alls removed | Unmatched URLs fixed; unknown slugs and malformed addresses not |
| E5 | E4 + `dynamicParams = false` on detail; malformed rewrite to an unmatched path | Malformed fixed; unknown slugs not |
| **E6** | **E4 + the proxy rewrites malformed addresses and unknown detail slugs to an unmatched path** | **All 11 user-facing cases: 404, server `<html lang>` en/th, localized heading and disclosure, nonce CSP, no-store, noindex, readable without scripting; valid pages 200** |

## Blocker and options for the Owner

Within the approved design (two root layouts, catch-all calling `notFound()`, no proxy change beyond undecodable addresses, no `globalNotFound`), no change gives a server-rendered localized 404 with a real 404 status (E1–E3). Per the instruction, nothing was applied.

1. **Approve option E6 (recommended).** Enable the experimental `globalNotFound` flag; add `app/global-not-found.tsx` rendering the existing shell and unavailable view in the language of the path; remove the two catch-alls and the two `/unavailable` routes; extend `proxy.ts` to send a path header and to rewrite undecodable addresses and unknown detail slugs to an unmatched path. Cost: an experimental Next.js flag (re-check on every Next.js upgrade), the proxy now knows the fixture slugs, a deviation from 4.2's stated mechanism that needs a recorded Owner decision (or a small planning amendment), then the full CP5 regression, Docker build and independent review. The localized 404 `<title>` and the Thai-page coverage test would need confirming in that work.
2. **Accept the current behavior for this stage** as a recorded deviation (404 status, headers and browser view correct; server document without `lang` and empty without scripting), and plan the fix separately.
3. **The contract's fallback architecture** (one `[locale]` root layout with an allowlisted rewrite): a larger routing change, not tested here. It would still need a separate answer for unknown slugs.

## Verification and records

No application change, so no new code test, build, suite run or review was due; the candidate's S6 results stand (unit 119, Chrome 283, Edge 283, review PASS). The scratch experiments ran `next build` and `next start` on 127.0.0.1:3300 from a clean clone outside the repository; every server was stopped. Temporary loopback containers of the V1 and CP4 rollback images (3100, 3200) were removed. The preview, rollback images, 32 volumes and the four unrelated containers are unchanged; no prune. A11 evidence stands (no runtime change).

## Result

**ACCEPTANCE BLOCKED** on the Owner's decision about the 404 documents (options above), in addition to the physical Notes check and publication authority. A05 PARTIAL with the Owner's stage deferral. No receipt. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`.
