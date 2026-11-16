---
id: DPT-PLAN-010-ADR
project: DoomParfum By TK
type: adr_proposal
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, adr, alternatives]
source_of_truth: "../../README.md"
---

# Architecture alternatives and ADR proposal

ADR identity: **ADR-ARCH-POST28-1**. Status: **PROPOSED / NOT ACCEPTED**. This refines the discussion after [[ADR_Post_PR27_Local_Private_Integration_Proposed]] without modifying that historical exact proposal or POST27-ODP-1. No implementation stack, framework, provider, ORM/driver, specification version, port, cookie protocol, numeric transport budget or container image is selected.

## Evidence and decision problem

The current code is Python operator tooling, PostgreSQL schema/guards, an internal trusted-callback reader, pure fixed-fixture M1/B1/primitives, and image/source validation. There is no application API, frontend/authentication/session service, real-data scorer adapter, asset HTTP service or browser private-data runtime. Exact inventory and limitations are in [[Function_Interface_and_DTO_Contracts]]. The old 194-method result is historical scoped evidence on unchanged code, not a running application test.

Research used official Python/FastAPI/Pydantic/OpenAPI, PostgreSQL/OWASP/RFC/Docker, and Next.js/W3C/C4 pages, recorded with exact URLs/observed versions in [[Architecture_Technical_Research_Python]], [[Architecture_Technical_Research_Security]] and [[Architecture_Technical_Research_UX]]. Living documentation is not an installed version or an Owner choice. For example, dependency injection/scopes can organize a future Python request boundary but cannot establish a genuine PostgreSQL user or enforce object ownership by themselves. Server/client component placement likewise does not replace object/field/rights authorization. Those are project inferences from the source and cited documentation, not framework guarantees.

## Four genuine alternatives

| Dimension | A — existing CLI only | B — local Python application service | C — TypeScript application backend | D — Python backend with logically separate UI layer |
|---|---|---|---|---|
| Matching-code reuse | Existing fixed-fixture harness unchanged | Direct Python primitives/types reuse after separate real-contract approval; no fixture disguise | Requires exact rational port/parity proof, or a separately secured Python worker protocol | Same Python reuse with a clear versioned UI/domain boundary |
| Application authorization | No browser surface; existing operator authority is not a user service | New trusted auth/principal/field-rights design required | Same genuine-principal problem; language/ORM does not solve it | Same backend responsibility; UI never owns credentials/authority |
| Connections/sessions | Operator tools only | Per-approved-principal genuine LOGIN lease/pool and clean transactions | Equivalent native driver/credential/lease discipline; extra cross-language choices if Python worker used | Backend owns leases; separate UI/BFF must not invent or forward user IDs as authority |
| Frontend complexity | No web UX | Can begin with a small accessible UI presentation while preserving layer separation | Potential shared UI language but extra domain duplication/bridge work | Explicit DTO/state/transport boundary; UI framework and physical co-hosting remain unselected |
| Operations/deployment | Lowest new surface; retains current limits | One future service plus existing DB/storage; host/container not selected | Node runtime plus DB; optional Python worker adds another trust/runtime boundary | Browser static/UI layer plus Python service; a separate UI server is optional, not required by the model |
| Type/validation safety | Existing typed domain validation only | Typed input at transport plus explicit domain/provenance mapping; no implicit coercion | Strict wire schemas and BigInt/rational parity or worker protocol required | One authoritative backend domain with versioned strict wire DTOs |
| Test cost | Current scoped suites only | New request/session/RLS/rights/private/error/pool tests and later domain-real tests | All same tests plus port/IPC/serialization parity and dual-runtime failure tests | Backend tests plus accessible UI/async-state/transport/privacy tests; domain tests remain independent |
| Performance considerations | Bounded local/operator workflows; no app SLA | Avoid duplicate math implementation; still measure DB queries, projection/scoring and cancellation later | TypeScript port may be viable but cannot replace exact arithmetic with JS Number; IPC may add cost | UI latency/cancellation/serialization and backend costs measurable independently; no current benchmark claim |
| Maintenance/migration | No immediate product UI progress | Builds on current language but adds application lifecycle and security ownership | Larger migration/port surface; possible team familiarity benefit must be evidenced | Clear ownership/replaceable UI, at cost of explicit contract/version discipline |
| Security review surface | Narrowest; still no real user app | New HTTP/auth/credential/pool/rights/media boundary | Same plus potential cross-runtime trust and serialization | Explicit browser/service/DB/media/data-review boundaries; no security from separation alone |
| Rollback | Stay on CLI | Disable future service without changing old operator ownership/source evidence | Disable service/worker; retain old Python reference code and data | Disable future UI/service independently; no private browser-cache fallback |

## Recommended phased direction

Recommend **A now, D as the proposed logical target**, with a minimal Python-backed read-only vertical slice once its exact prerequisites are accepted. D does not require microservices, a dedicated Next.js server or a separate deployment. A simple co-hosted presentation can satisfy the same UI/application/domain/infrastructure contracts if later selected. B is a valid simpler physical realization only when it preserves those logical boundaries. C remains a genuine alternative requiring explicit evidence for port/bridge and maintenance cost.

1. Preserve current CLI, accepted synthetic functions and immutable data/evidence. This task adds architecture only.
2. Agree on the exact genuine-principal path, selected-data/rights projection, typed transport/state/resource contract and actual stack ADR. No default provider/framework or admin shim.
3. Implement a separately approved private catalogue/detail read slice with genuine nonadmin sessions and safe unavailable/media placeholders. No real ranking or private writes are required to prove that slice.
4. Add accessible UI pages, media intake/delivery, real matching and personal mutations as separate gated units. The five-record offline data preview is independent and still needs exact A/B/I acceptance; it is not started by architecture approval.

Exact mathematical reuse means preserving rational semantics and approved method versions. Existing synthetic scorer inputs remain fixed-fixture inputs. A future real method needs its own accepted boundary/configuration/data proof rather than a wrapper that changes real IDs to synthetic metadata.

## Decisions deliberately not made

| Unselected detail | Required future decision/proof |
|---|---|
| FastAPI or another Python framework | Exact version, dependency/security composition, exception/cancellation behavior, support/testing surface; framework scopes do not become PG identity |
| Next.js/React/other UI | Exact version/rendering/deployment and serialization/auth/cache rules; no private data in client bundles/props without authorized projection |
| PostgreSQL driver/ORM/pool | Genuine initial-login credentials, effective privileges, role/transaction cleanup and policy compatibility; do not substitute a shared admin pool |
| Authentication provider/protocol | Exact trusted proof, server session/binding authority, lifecycle/revocation/CSRF/origin/TLS/secret handling; no account/login setup now |
| OpenAPI/transport serialization | Exact spec/schema/version and strict per-operation numeric/byte/count policies; no inherited 8KiB or internal 2MiB default |
| Cache/offline behavior | Approve the conservative operation-specific proposal; any persistent private cache/PWA data needs a separate reviewed privacy contract |
| Host/port/image/provider/storage | Explicit deployment/operations/rights/backup scope and budget; C4 container does not select Docker |
| Real method/configuration | Exact canonical/vocabulary/normalization/closure/selection/rights/eligibility/partition contract and tests; Full Mode A/B2 remain unapproved |

Observed documentation versions are research evidence, not these choices. PostgreSQL18 is a reference manual version, not proof of the live server. The source/research note distinguishes installed Python3.11.9 from the observed maintenance-series documentation. No package was installed to align versions.

## Acceptance, rollback and Owner decision

Architecture acceptance requires a consistent element/interface/component/state graph, no source-dependency cycles, preserved product scope, strict identity/rights/unknown boundaries, explicit unimplemented interfaces and a reviewable task DAG. It does not establish software/runtime acceptance. Future implementation must pass its own security/feature tests before Human review/merge; deployment remains a further gate.

Owner may choose **retain A/defer service**, **accept D as design direction**, **choose B with boundary constraints**, or **choose C with exact parity/bridge proposal**. Any choice here is design-only. Actual framework/identity/transport/task acceptance needs the later explicit ADR and applicable Planning/Implementation Gates. [[Architecture_Owner_Review_Packet]] binds this version and shows effects on POST27 G/H/F/I without rewriting POST27-ODP-1.

Rollback of this documentation amendment is a normal reviewed Git change; no schema/data/service rollback is needed because none is mutated. Future slice rollback disables its own UI/service and invalidates private session/view state; it never rewrites old subjects/owners, re-enables stale rights through a restored cache or discards immutable source/review evidence.
