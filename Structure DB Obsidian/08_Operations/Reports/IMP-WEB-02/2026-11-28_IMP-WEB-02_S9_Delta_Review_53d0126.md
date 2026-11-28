---
id: IMP-WEB-02-S9-REVIEW-53D0126
project: DoomParfum By TK
type: independent_review
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, routing, review, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S9 — independent re-assessment of `3b93945..53d0126` at runtime (verbatim)

PUBLIC_SAFE. Reviewer: the same read-only sub-agent as [[2026-11-28_IMP-WEB-02_S9_Delta_Review_3b93945]], resumed with the review follow-up and the restarted preview (image `sha256:568cc3b3…` built from `53d0126`). Same-vendor (Anthropic Claude), separate context; not human, not cross-vendor, not Owner acceptance. The two items under "Not verified" are covered by the implementer's evidence: the image's own output scan is clean and the image was built from a clean `web/` tree at `53d0126` ([[2026-11-28_IMP-WEB-02_S9_Report]]). The report follows unedited apart from this header.

---

## IMP-WEB-02 S9: re-assessment of the 404 correction at 53d0126, checked at runtime

**VERDICT: PASS.** Every point I left unverified last time now passes on the running preview at 127.0.0.1:3000 (image built from 53d0126, as reported). The full e2e suite passes 305/305, the unit tests pass 122/122, and my own raw-HTTP checks found no defect. What remains are nits, none of them blocking.

### What changed in 3b93945..53d0126 (web/, 3 files)
- **`src/proxy.ts`:** comments only, no logic change.
  - The rewrite-target comment now gives the verified cause: Next 16.4.6 runs the proxy a second time on a rewrite target that matches no route, and that pass derives the locale header again from the target path.
  - A new comment says the proxy's slug set must stay the same set the detail view looks up.
  - Even on that second pass the locale still comes from the path only, so no client header is ever trusted. The per-locale targets (`/_unavailable`, `/th/_unavailable`) are the correct fix. A direct request to `/th/_unavailable` getting Thai is also path-derived, so that is acceptable.
- **`tests/proxy.test.ts`:** a new unit test checks that every validated fixture slug passes the proxy, without a rewrite, in both locales.
- **`e2e/locale.spec.ts`:** three new tests:
  - repeated and interleaved 404s each get the right `lang` and a fresh nonce that matches their CSP;
  - HEAD on a 404 returns 404 with an empty body, the nonce CSP, `no-store` and noindex;
  - escaped valid slugs return 200 in the right language.

### Findings
1. **Former should-fix (unexplained locale behaviour): resolved.**
   - The root cause is now documented at `src/proxy.ts:8-14`.
   - At runtime, 108 GET checks found no reused nonce and no script without the response's nonce, including the same paths requested repeatedly and en/th interleaved.
2. **Former nit (test gaps): resolved.**
   - New e2e tests cover HEAD on a 404 and escaped valid slugs.
   - My own run: HEAD on `/nope`, `/th/perfume/nope`, `/th/%E0%B8` and `/perfume/nope` gives 404 with an empty body, `private, no-cache, no-store, max-age=0, must-revalidate`, a nonce CSP and `X-Robots-Tag: noindex, nofollow`.
   - `/perfume/paper%2Dstudy-a` and `/th/perfume/%70aper-study-a` return 200 with the right `lang`.
3. **nit (accepted): two lookups still read the same data separately.** `src/proxy.ts:23` (the slug set) and `src/views/detail.tsx:14` (the view's lookup) both read the fixtures. The new comment and the unit test cover the drift risk. The test only checks that validated slugs pass the proxy, but both read the same object, so that is enough today.
4. **nit (accepted, unchanged):** the proxy imports the whole fixture module (`src/proxy.ts:2`). This is server-side only. As before, the local `.next/static` contained no fixture strings. I did not scan the Docker image's own build output, because I cannot read inside the container without touching it.
5. **nit (accepted, unchanged):** removing the two `global-error.tsx` lint-disable lines was needed to keep `npm run lint` green; the earlier evidence still applies.
6. **nit (informational, existed before this change, outside the delta):**
   - `GET //evil.example/` answers `308 Location: /evil.example/` with no `Cache-Control`. The framework collapses repeated slashes before the proxy runs. The Location stays on this site, so it is not an open redirect.
   - Encoded-slash addresses such as `/th%2Fnope` get an English 404, which fits the rule that only `/th` and `/th/...` are Thai.
7. **False alarm, not a finding:** my checker first flagged `/perfume/paper-study-a.rsc` as returning 200. It is the valid detail page in the framework's internal data format (`text/x-component`): the framework strips the `.rsc` suffix before the proxy sees the path, and the body contains "Paper study A". `/perfume/nope.rsc` and `/perfume/Paper-Study-A.rsc` return 404. RSC-header requests to unknown pages return 404 with the right language and no `__next_error__`.

### Runtime checks (all read-only)
- **Full e2e suite:** `E2E_ORIGIN=http://127.0.0.1:3000 npx --no-install playwright test` passed **305/305** (1.8 min). `e2e/locale.spec.ts` alone passed **95/95**.
  - I replaced the reporter with `--reporter=list` and pointed `--output` at the scratchpad, so `.artifacts/e2e.json` and `test-results/` were not written.
  - `git status` was clean afterwards.
- **Unit tests:** `node --test "tests/*.test.ts"` passed **122/122**.
- **Raw-HTTP sweep:** 36 paths, each sent three ways (no headers; spoofed `x-doomparfum-locale`, `Accept-Language` and cookie set to `th`; the same set to `en`). All 108 checks passed apart from the false alarm in finding 7. Each check covered:
  - the expected status;
  - the right `<html lang>`, with no `__next_error__`;
  - with scripts stripped, the localized title, h1 and synthetic-mock notice, plus the robots meta (readable without JavaScript);
  - at least one script, every one carrying the response's nonce, and no nonce reused across responses;
  - `no-store` and noindex;
  - no external `src` or `href`.
- **Addresses swept:**
  - **Unknown paths and slugs:** `/does-not-exist`, `/a/b/c`, `/perfume/no-such-study`, `/perfume/Paper-Study-A`, `/perfume/paper-study-a/x`, `/th/does-not-exist`, `/th/perfume/no-such-study`, `/th/perfume/PAPER-STUDY-A`, `/th/a/b`, `/th/perfume`.
  - **Unsupported locale prefixes:** `/en`, `/en/explore`, `/TH`, `/fr`, `/thx`, `/th%2Fnope`.
  - **Malformed addresses:** `/%E0%B8`, `/th/%E0%B8`, `/perfume/%E0%A4%A`.
  - **Rewrite targets requested directly:** `/_unavailable`, `/th/_unavailable`.
  - **Encoded slashes:** `/perfume/paper-study-a%2Fx`, `/th/perfume/paper-study-a%2F`.
  - **The ten valid routes:** all return 200, with the right `lang`, nonce, `no-store` and noindex.
- **Methods:** POST, PUT, DELETE, OPTIONS and PATCH on `/nope`, `/th/perfume/nope`, `/%E0%B8` and `/_unavailable` all return 405 with `Allow: GET, HEAD`.
- **Trailing slashes:** `/explore/`, `/th/`, `/th/perfume/paper-study-a/`, `/perfume/nope/` and `/th/perfume/nope/` each return 308 to the slash-less path on the same site, with `no-store`.
- **Bypass paths:**
  - `/_next/static/nope.js`, sent with a spoofed header, returns a plain-text 404 ("Not Found"), so no 404 page renders without the proxy.
  - A request with `sec-fetch-dest: image` also gets a plain-text 404.

### Not verified
- A fixture-string scan of the Docker image's own client chunks: I scanned only the local `.next` build, which came from the earlier head.
- That the image sha256:568cc3b30f8f… really was built from 53d0126: I took that from your message. Its behaviour matches the new tests, which all pass.

### Tool execution report
- **Used:** git read commands (diff, log, status); node with small raw-HTTP scripts I wrote under the session scratchpad's `review/rt` folder; Playwright (full suite, reporter and output overridden as above); `node --test`.
- **Requested but not used:** none.
- **Files changed:** none in the repository or the vault; scratch files only.
- **Git:** branch `feat/frontend-v1-1-design-upgrade` at 53d0126; I wrote nothing.
- **Next action:** findings 3–6 can be recorded as accepted nits; nothing blocks closeout.
