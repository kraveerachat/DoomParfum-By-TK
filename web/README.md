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

`npm run scan:output -- <directory>` scans a copied-out `/app` directory for forbidden files, secret-like content, host paths and fixture data in immutable assets.

## Layout

| Path | Content |
|---|---|
| `src/fixtures/` | Synthetic records, strict validator, view model |
| `src/catalogue/search.ts` | Shared search, filter and URL rules |
| `src/server/catalogue.ts` | The only module that loads fixtures (server-only) |
| `src/proxy.ts` | Nonce CSP, no-store delivery, image-optimizer refusal |
| `src/components/`, `src/app/` | Interface and the five route types |
| `scripts/build-studies.mjs` | Draws the original SVG studies in `public/studies/` |
| `tests/`, `e2e/` | Unit, boundary, contrast and browser acceptance tests |

Licenses and font sources are in `NOTICE.md`.
