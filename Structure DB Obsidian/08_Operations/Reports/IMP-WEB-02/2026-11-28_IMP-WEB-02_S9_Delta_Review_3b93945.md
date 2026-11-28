---
id: IMP-WEB-02-S9-REVIEW-3B93945
project: DoomParfum By TK
type: independent_review
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, routing, review, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S9 — independent review of `253bf48..3b93945` (verbatim)

PUBLIC_SAFE. Reviewer: a read-only same-vendor (Anthropic Claude) sub-agent with its own context, separate from the implementer's, told not to write to the repository, the vault or Docker. Not human, not cross-vendor, not Owner acceptance. The preview was down during this pass (Docker Desktop had stopped), so the verdict is CONDITIONAL on runtime checks; the follow-up is [[2026-11-28_IMP-WEB-02_S9_Delta_Review_53d0126]]. The report follows unedited apart from this header.

---

## IMP-WEB-02 S9: independent read-only review of 253bf48..3b93945 (web/, 14 files)

**VERDICT: CONDITIONAL.** I found no correctness or security defect in the code. The conditions are runtime checks I could not run: the preview at 127.0.0.1:3000 refused the connection (ECONNREFUSED), and I started nothing. Before PASS, the e2e suite must be re-run against the 3b93945 image, and finding 1 must be explained or confirmed harmless.

### Findings

1. **should-fix: unexplained locale behaviour is recorded, not diagnosed.** `web/src/proxy.ts:8-14` says that with a single rewrite target, a rewritten Thai address got an English 404 "observed on 16.4.6". The design picks the locale from the header the proxy sets (`proxy.ts:62`, `global-not-found.tsx:17-19`), and that header is derived from the original path. So the rewrite target should not affect the language. That it did means something else feeds into the render (for example dedupe or caching keyed by path), and that cause is still unknown.
   - Evidence: in the Next 16.4.6 code, `resolve-routes.js:415-440` replaces all request headers on rewrites too, and `_not-found` is not prerendered (absent from `prerender-manifest.json` in the local `.next`).
   - The per-locale targets work around it, but the e2e hits each direct (non-rewritten) path only once. A path-keyed cache of the HTML or nonce would therefore go unnoticed for direct paths.
   - Ask: add or run a runtime check of repeated and interleaved requests: the same path twice gets a fresh nonce that matches its CSP; `/nope` then `/th/nope` then `/perfume/nope` then `/th/perfume/nope` each get the right `lang`. Then record the root cause or reword the comment.

2. **nit: test gaps for two contract items.**
   - HEAD on a 404 has no e2e. Only the unit level shows HEAD is rewritten: my probe of `/th/perfume/nope` with HEAD returned the rewrite to `/th/_unavailable`.
   - A valid encoded slug (`/perfume/paper%2Dstudy-a`) returning 200 at runtime has no e2e. Only `tests/proxy.test.ts` asserts it is not rewritten.
   - If the framework ever stopped decoding params, that request would fall through to `notFound()` (`views/detail.tsx:98`) and get the defective S7 document back. Today it is consistent: Next's `shared/lib/router/utils/route-matcher.js:17-31` decodes params with `decodeURIComponent`, matching `proxy.ts:84`.

3. **nit: two sources of truth for "known slug".** `proxy.ts:18` reads the raw `fixtures`, while `views/detail.tsx:14` reads `fixtureSet` from `server/catalogue.ts`.
   - They are the same object today: `assertFixtures` returns its input (`fixtures/validate.ts:190-193`). So the legacy `app/(en)/not-found.tsx`, `app/th/not-found.tsx` and `notFound()` are unreachable for detail paths.
   - Any future filtering in the catalogue would make them diverge and reopen the S7 path. A shared helper or a comment would guard this.

4. **nit: the proxy import is heavier than needed and skips the guard.** `proxy.ts:2` pulls the whole fixture module (about 9 KB including descriptions) into the proxy bundle just for the slug set. It also bypasses the `import "server-only"` guard in `server/catalogue.ts`. This is server-side only: grep of the local `.next/static` for the `scripts/scan-output.ts` fixture pattern (plus `glass-study`) found no hits.

5. **nit (scope, acceptable): the `global-error.tsx` lint change was needed.** Linting the 253bf48 version of `web/src/app/global-error.tsx` against the current tree (`eslint --stdin --max-warnings 0`) fails with "Unused eslint-disable directive" at lines 32 and 36. Removing the two lines is therefore required to keep `npm run lint` green; it is not a design change. The optional headers parameter on `e2e/helpers.ts` `raw()` is test support for the spoofing test. I saw nothing else beyond the authorized change: there is no dependency change, and the only experimental flag is `globalNotFound` (`next.config.ts:24`).

6. **nit (informational, existed before this change): encoded slashes.** The framework's static item lookup also tries the decoded path (`router-utils/filesystem.js:637-640`), so `/th%2Fexplore` probably serves the Thai Explore page. For 404s, `/th%2Fnope` gets an English 404. That fits the contract rule (only `/th` and `/th/...` are Thai). Both are from code reading only, not run.

### What I verified
- **Unit tests:** `node --test "tests/*.test.ts"` from `web/` gives 121/121 pass at 3b93945.
- **The new tests catch the old defect:** the 3b93945 test file run against the 253bf48 `proxy.ts` (in a scratch copy) fails 2/6. Both S9 tests fail and the 4 older ones pass. The tests are not tautological: they assert the forwarded `x-middleware-request-x-doomparfum-locale` header and the rewrite target.
- **The e2e assertions would catch it too (by reading):** they check status, the absence of `__next_error__`, `<html lang>`, the title, and the h1 and notice with scripts stripped.
- **Lint and types:** eslint with `--max-warnings 0 --report-unused-disable-directives` on the 8 changed TS/TSX files passes. `tsc --noEmit --incremental false` passes. The working tree was unchanged afterwards.
- **Proxy probe of 31 paths and 5 methods**, with a spoofed `x-doomparfum-locale: th` header:
  - The locale always comes from the path (`/TH`, `/thx`, `/th%2F...` give en; `/th`, `/th/...` give th).
  - `/perfume/x/y`, `/th/perfume`, `/TH/perfume/nope` are not rewritten. These are unmatched routes, so the global 404 page handles them.
  - These are rewritten to `/_unavailable` or `/th/_unavailable`: `/th/perfume/PAPER-STUDY-A`, `%2F`/`%2Fx` slugs, `.rsc`, `%00`, `%25`, `/%`, `/th/%`, `/perfume/%E0%A4%A`.
  - `%70aper-study-a` passes in both locales.
  - The decode on line 84 cannot throw, because the whole path is decoded first (line 73).
  - Trailing slashes still redirect 308 first, and `//evil.example/` redirects within the same origin.
  - POST, PUT, OPTIONS and DELETE return 405 with `Allow: GET, HEAD`.
  - Every answer has the CSP and noindex, and `Cache-Control: private, no-store`.
- **Next 16.4.6 internals (code reading):**
  - The proxy matcher is tested on both the raw and the decoded path (`resolve-routes.js:343-350`).
  - A missing `/_next/static/` file gets a plain-text 404 before any 404 page is rendered (`router-server.js:602-609`), so no 404 page can render without the proxy. Non-HTML `sec-fetch-dest` requests also get plain text.
  - The 404 path itself sets `no-store` (`router-server.js:589`).
  - Client-sent `x-middleware-*` control headers are filtered (`server-ipc/utils.js:62-81`).
  - Dynamic routes are matched on the raw path with `^/perfume/([^/]+?)(?:/)?$` and `^/th/perfume/([^/]+?)(?:/)?$`, which matches `DETAIL`.
- **No external requests in the bundle:** the local `.next/static` contains only framework or namespace URL strings (nextjs.org docs, w3.org, react.dev, core-js), no runtime endpoints. That build is from 2 minutes before the commit, so it is not proven identical to the Docker image.

### What I could not verify (needs the preview running)
- All runtime behaviour on the live server: real 404 status for every listed address, server-rendered `lang`, title, heading and notice, the no-JS rendering and the return link, the script nonce matching the response CSP, `no-store` and `X-Robots-Tag` on 404s, and 405 on a live 404.
- The ten valid routes returning 200 unchanged, and the trailing-slash 308s end to end.
- The reported 18/19 e2e failure against the old candidate.
- Interleaved and repeated-request locale and nonce behaviour (finding 1).
- A fixture scan of the Docker image's own `.next/static`.

### Tool execution report
- **USED:** git read commands, node `--test`, eslint, tsc (no-emit, non-incremental), a node proxy probe and the old-proxy test run in a scratch copy (with a node_modules junction to the worktree), and one HTTP request to the preview (refused).
- **NOT USED:** the UI design tools. This was a code and security review, so they did not apply.
- **FILES_CHANGED:** none in the repository or the vault. My scratch files are under the session scratchpad `review/old` folder.
- **GIT:** branch `feat/frontend-v1-1-design-upgrade` at 3b93945; I wrote nothing.
- **NEXT_ACTION:** start the 3b93945 preview, run `e2e/locale.spec.ts` plus a repeat/interleave check for finding 1, then re-assess for PASS.
