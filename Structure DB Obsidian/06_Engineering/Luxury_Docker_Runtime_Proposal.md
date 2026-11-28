---
id: DPT-ENG-LUXURY-DOCKER
project: DoomParfum By TK
type: architecture_proposal
status: proposed
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, docker, nextjs, runtime, mock-only]
source_of_truth: "../../README.md"
---

# Docker-first mock frontend runtime proposal

Documentation only, under [[DPT-PLAN-012_Luxury_Frontend_Editorial]]. No Dockerfile, Compose file, app source, package installation, image build, container or server was created. This selects no real-data backend, ORM, authentication provider or production host. Prior [[System_Architecture_Refinement]], [[Post_PR30_First_Readonly_Web_Slice_ADR]] and all POST30-ODP-1 decisions remain unchanged. The new Owner preference is proposed for this isolated mock frontend only.

## Alternatives and bounded recommendation

| Choice | Benefit | Cost / disposition |
|---|---|---|
| Framework-free static HTML/CSS/JS | Fewest dependencies, smallest demonstration | Valid prior alternative; does not rehearse the Owner's requested App Router/Docker model. Not selected by this proposal. |
| Next.js App Router + TypeScript + Tailwind | Requested route/layout model; component reuse; standalone Node image | Recommended for mock-only review; dependency, CSP and server-rendering complexity require exact compatibility verification. No approved stack exists yet. |
| Full application connected to Python/DB | Eventual real-data workflows | OUT OF SCOPE; waits on separate dependencies and security gates. |

Selective shadcn/ui dialog primitives and custom editorial components are proposed. No wholesale generator, UI kit installation or animation library is needed. Pin exact stable compatible Next.js/React/TypeScript/Tailwind, primitive and package-manager versions plus lockfile during the first authorized implementation task, after checking current official support/security guidance. Pin Node base image tag and digest then. No `latest` image or floating dependency range should define a reproducible preview. This planning task deliberately makes no unsupported current-version claim.

## Runtime contract

| Property | Proposed exact value / behavior |
|---|---|
| App directory / build context | `web/`, isolated; never repository-root context |
| Compose service | `web` |
| Container name | `doomparfum-web` (one local instance; conflicts must stop rather than rename silently) |
| Container listener | `0.0.0.0:3000` inside container only |
| Published host binding | `127.0.0.1:3000:3000` (IPv4 loopback only) |
| Fixed entry URL | `http://localhost:3000`; if IPv6 localhost resolution differs, fix host resolution/network configuration within approved task, never broaden binding |
| First host | Windows Desktop / Docker Desktop using Linux containers |
| Later host | Ubuntu Mini Server under a separately approved host-readiness task |
| Restart | `no` for local review; no automatic host-boot service |
| Data services / credentials | None; no DB, Redis, queues, auth, environment file or Docker socket mount |
| Runtime storage | No catalogue volume; ephemeral `/tmp` only if required by tested runtime |
| Scaling | One replica; fixed container name/port intentionally preclude parallel local stacks |

Docker documents that publishing without a specific host address can expose ports on host interfaces. Loopback binding is required, and actual LAN reachability remains a verification step; do not treat a YAML line as proof. [Docker port publishing](https://docs.docker.com/engine/network/port-publishing/), inspected 2026-11-23. No inbound firewall, router, tunnel or Cloudflare changes belong here.

## Multi-stage image specification

Stages: (1) pinned Node Linux base and lockfile-based dependencies; (2) builder containing only the web source and approved owned assets; (3) minimal production runner with non-root user. Use `output: 'standalone'`; copy its traced server output plus `public` and `.next/static` explicitly into the runner. Start the generated `server.js` with port 3000 and hostname 0.0.0.0. Expose documents the container port; only the Compose loopback mapping publishes it. These are proposed instructions, not executed commands. Standalone output omits public/static by default, so copying only the server directory is incomplete. [Next.js output documentation](https://nextjs.org/docs/app/api-reference/config/next-config-js/output), inspected 2026-11-23.

Exclude Git metadata, vault, database/matching sources, private files, `.env*`, logs, caches, node_modules and host build output from the `web/` build context. No secret build arguments. Copy no `.env` into standalone output. Preserve dependency/font notices. Run image as non-root, drop capabilities and disallow privilege escalation; prefer read-only root filesystem with bounded tmpfs after verifying the pinned framework can run. If a writable runtime cache is required, fail the gate and document the minimal approved exception; never mount the repository to the production-style runner. Runtime health check requests the existing `/about` route inside the container with a bounded timeout, avoiding an extra API route. No database readiness check.

Windows-to-Ubuntu portability: build inside Linux container rather than copying Windows standalone artifacts; check case-sensitive imports, LF scripts, exec permissions, native optional dependencies, CPU architecture and pinned image availability. A successful Desktop build is not proof of Ubuntu readiness. No deployment or automatic upgrade is authorized.

## Production-style preview versus development

| Concern | Production-style local preview | Local development / hot reload |
|---|---|---|
| Intended purpose | Verify the release build locally, not deploy Production | Author and debug UI inside Docker |
| Future config files | `web/compose.yaml`, `web/Dockerfile` | `web/compose.dev.yaml` used as a separate full config |
| Process | Generated standalone Node server | Pinned package manager's `next dev`, host 0.0.0.0, port 3000 inside container |
| Source mount | None | Only `web/` bind mounted; isolated dependency/build-cache volumes |
| Host port / container | Same `127.0.0.1:3000:3000`, `doomparfum-web` | Same; modes mutually exclusive |
| Headers / CSP | Enforced nonce CSP, no-store pages/RSC, noindex | Separate loopback-only development CSP permits necessary same-origin HMR/WebSocket and framework development evaluation only; never copied into preview |
| Reproducibility | Lockfile and pinned image, no runtime install | Same pins; no implicit install on startup |
| File watching | Not applicable | Verify Docker Desktop bind-mount watching; bounded polling only if needed and documented |
| Data/cache | Ephemeral fixtures, no persistent catalogue cache | Same boundary; dependency/build volumes contain no imported private data |

Future illustrative operator sequence, only after Gate P and implementation authorization: stop the currently running web mode; run Compose config validation for the desired full config; build preview or start development; verify the port and all five route types; stop with Compose down. Do not use `down --volumes` against shared volumes. If port 3000/container name is occupied, report the conflict and stop; do not kill another process, change the requested URL or start a second public listener. Failed build leaves prior image intact; stop failed container, restore the last verified image tag locally, recheck the same URL. No data migration or backup operation is needed for an ephemeral mock.

## Content security, cache and discoverability

Production proposal uses per-response nonces and dynamic rendering so framework inline bootstrap and approved styles can run without broad inline-script permission. Policy sources are self plus the generated nonce; no third-party origin, no unsafe-eval in preview, no object/embed, no frames, no form posts, self-only fonts/images/media, self-only connections, base-uri self and frame-ancestors none. Do not include `strict-dynamic` without assessing its source-trust implications. Nonce policy and generated markup must agree under the exact pinned framework; test full reload, navigation and every dialog/filter. Same-origin framework RSC requests are allowed, external runtime data is not. Dynamic no-store delivery also keeps fixture payloads out of persistent HTML/RSC caches. Avoid development policy exceptions in preview. [Next.js CSP guidance](https://nextjs.org/docs/app/guides/content-security-policy), inspected 2026-11-23.

All five routes, error pages and response variants must send noindex metadata (and proposed `X-Robots-Tag: noindex` for responses). Future public link access is a preference only; this task remains loopback. Do not block crawling with robots.txt while relying on a crawler to discover noindex. noindex does not authenticate users or protect private information, and its effect depends on crawler support. [Google noindex guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing), inspected 2026-11-23. No canonical URL pointing to an invented domain, social product claim or fake review schema.

Future Cloudflare exposure requires its own bounded deployment/security plan and explicit Owner approval. It may expose only the approved synthetic slice; connecting private records is a separate security/data task. A public mock cannot become a public private-data app by changing an environment variable.

## Amendment DPT-PLAN-013 — no runtime change (MERGED 2026-11-26, PR #37 `3e87027`)

Frontend V1.1 ([[DPT-PLAN-013_Frontend_V1_1_Amendment]]) keeps the loopback preview, container, port, CSP, no-store and no-egress rules above. The only request-handling change planned is that an undecodable address under `/th/` gets the Thai unavailable view. The Thai font specimen is Git-ignored local tooling and never enters an image. Any other proxy or Compose change needs its reason in the implementation PR.
