# DoomParfum By TK: mock frontend

A local, mock-only frontend for the plan `DPT-PLAN-012` (task `IMP-WEB-01`). Every record is fictional. It has no API, database, account, matching, price or external request, and it is not a deployment.

## Run in Docker

Run these from `web/`. Both modes use `http://localhost:3000`, the container name `doomparfum-web` and the loopback binding `127.0.0.1:3000`, so only one can run at a time. If the port or name is taken, Docker reports a conflict and nothing else is changed.

| Mode | Start | Stop |
|---|---|---|
| Preview (release build) | `docker compose up --build --force-recreate --detach` | `docker compose down` |
| Development (hot reload) | `docker compose -f compose.dev.yaml up --build --force-recreate` | `docker compose -f compose.dev.yaml down` |

`localhost` must resolve to IPv4. The container is not published on `::1`; use `http://127.0.0.1:3000` if a client does not fall back.

The preview image build runs type checks, lint, unit tests and fixture validation before `next build`. A failed build leaves the previous image in place.

## Checks

Host checks need Node 24 and an installed Chrome. The browser suite expects the preview to be running.

```text
npm ci --ignore-scripts
npm run typecheck:gen
npm run lint
npm test
npm run test:e2e
```

To test a candidate build without stopping the preview, serve it on another loopback port and set `E2E_ORIGIN`, for example `E2E_ORIGIN=http://localhost:3100 npm run test:e2e`.

`npm run scan:output -- <directory>` scans a copied-out `/app` directory for forbidden files, secret-like content, host paths and fixture data in immutable assets.

## Response headers and their limits

`src/proxy.ts` sets the nonce CSP, `X-Robots-Tag` and no-store on every page, error page, RSC response and redirect it produces, and answers any method other than GET and HEAD with 405. Coverage is not universal. These responses are produced before the proxy runs. `e2e/headers.spec.ts` asserts them as known exceptions, except the closed connections:

| Response | Produced by | Missing |
|---|---|---|
| 308 for repeated slashes or backslashes (`//explore`, `/about//`) | Next.js router | All four headers; the target stays on this origin and the page that follows has them |
| 308 for an absolute-form request line | Next.js router | All four headers; it repeats the sender's own target. Browsers do not send this form to an origin server |
| 431 for a request above the Node header limit (16 KiB) | Node HTTP parser | All headers; no body |
| 400 for a request Node cannot parse (unknown method, missing Host, malformed line or header) | Node HTTP parser | All headers; no page content |
| Connection closed for `CONNECT` and for a WebSocket upgrade | Node and Next.js server | No response at all |
| 500 for `TRACE` or the `*` target | Next.js server | CSP, noindex, nosniff; no page content |
| Hashed files in `/_next/static/` | Next.js static handler | CSP and no-store, on purpose |

## Without scripting

Pages and their links work, and the four routes stay in the header. Search, Profile and the Explore and Notes filters need scripting. Where scripting is enabled but the scripts fail to load, a narrow header keeps its Menu button, which then does nothing; the in-page and footer links still work.

## Layout

| Path | Content |
|---|---|
| `src/fixtures/` | Synthetic records, strict validator, view model |
| `src/catalogue/search.ts` | Shared search, filter and URL rules |
| `src/server/catalogue.ts` | The only module that loads fixtures (server-only) |
| `src/proxy.ts` | Nonce CSP, no-store delivery, reads only, trailing-slash redirects, image-optimizer refusal |
| `src/components/`, `src/app/` | Interface and the five route types |
| `scripts/build-studies.mjs` | Draws the original SVG studies in `public/studies/` |
| `tests/`, `e2e/` | Unit, boundary, contrast and browser acceptance tests |

Licenses and font sources are in `NOTICE.md`.
