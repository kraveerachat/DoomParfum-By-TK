---
id: DPT-PLAN-010-COMPONENTS
project: DoomParfum By TK
type: component_registry
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, contracts, planning]
source_of_truth: "../../README.md"
---

# Component and dependency registry

This is the component contract for [[System_Architecture_Refinement]]. IMPLEMENTED means source exists at the pinned main, not a deployed or currently verified service. All new application components, ports, DTOs and choices remain PROPOSED or BLOCKED. Existing operator commands are not browser services. See [[Function_Interface_and_DTO_Contracts]] for exact signatures and [[C4_Context_and_Container_Design]] for request and trust diagrams.

Dependency arrows below mean consumer → dependency. Request/lifecycle arrows in sequence diagrams are different. UI/transport depend inward through application contracts; domain logic never imports UI/HTTP. Infrastructure implements inward ports and composition selects approved adapters. A separately checked DAG rejects missing IDs and cycles; an intentional review workflow loop is not a dependency cycle.

## C-UI-SHELL

| Contract | Value |
|---|---|
| responsibility | Proposed browser navigation and accessible chrome; contains no data authorization authority. |
| owner_module | Future UI layer |
| inputs | NavigationIntent |
| outputs | LocalViewState.v1 |
| dependencies | C-DTO |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Render static navigation; route through guards before any data request. |
| error_conditions | Unknown route or unapproved UI contract; no private prefetch. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-05 |

## C-UI-PAGES

| Contract | Value |
|---|---|
| responsibility | Proposed pages and an internal UI transport-client subcomponent depend on wire contracts, not server controllers or domain implementation. |
| owner_module | Future UI layer |
| inputs | Validated local event |
| outputs | proposed operation DTO / safe presentation state |
| dependencies | C-UI-SHELL; C-DTO |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Invoke only declared wire contracts after their gates; network request arrows are not source-module dependencies. No direct SQL, filesystem or operator command. |
| error_conditions | Unavailable capability, denied projection, stale response generation. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-06 |

## C-TRANSPORT

| Contract | Value |
|---|---|
| responsibility | Proposed service controllers and strict boundary mapping; no route/API implementation exists. |
| owner_module | Future backend boundary |
| inputs | Explicit schema/session proof |
| outputs | application use case / safe response |
| dependencies | C-DTO; C-AUTHN; C-PRINCIPAL; C-PORTS |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Enforce accepted schema/resource policy and verified context before dispatch. |
| error_conditions | Missing policy, malformed input, unauthenticated or unsupported operation. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-04 |

## C-DTO

| Contract | Value |
|---|---|
| responsibility | Proposed versioned input/output/state/envelope schemas; never automatic domain or authority coercion. |
| owner_module | Future contract module |
| inputs | Declared typed fields |
| outputs | strictly validated transport/domain projection |
| dependencies |  |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Preserve unknown, versions and exact rational wire values; reject undeclared/coerced fields. |
| error_conditions | Unknown schema/version, excessive bytes/count/numeric bounds, invalid state combination. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-04 |

## C-AUTHN

| Contract | Value |
|---|---|
| responsibility | Proposed trusted application authentication/session authority; no provider or cookie mechanism selected. |
| owner_module | Future authentication adapter |
| inputs | Provider proof |
| outputs | verified server session / safe denial |
| dependencies | C-PORTS |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Validate server-side proof and session freshness; never accept browser user IDs as proof. |
| error_conditions | Forged/expired proof, unsupported provider, revoked session. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-03 |

## C-PRINCIPAL

| Contract | Value |
|---|---|
| responsibility | Proposed lease factory for a genuine nonadmin PostgreSQL LOGIN tied to the approved immutable subject. |
| owner_module | Future infrastructure/session adapter |
| inputs | Verified session |
| outputs | internal principal/connection lease, never browser credentials |
| dependencies | C-AUTHN; C-PORTS; C-PG-SCHEMA |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Verify initial login and effective privileges, session_user=current_user, scope binding and fresh transaction. |
| error_conditions | Admin/BYPASSRLS/role reuse/owner mismatch; discard or reject, never impersonate. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-03 |

## C-AUTHZ

| Contract | Value |
|---|---|
| responsibility | Proposed application object/field/action/rights authorizer and safe projection policy. |
| owner_module | Future application security adapter |
| inputs | Verified lease, target and action |
| outputs | allowed projection / uniform unavailable |
| dependencies | C-PORTS; C-PG-READ; C-CONFIG |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Check scope and current selected provenance/rights before lookup, counts, pagination, scoring or bytes. |
| error_conditions | Missing/unknown/revoked permissions; public identity cannot publish private related records. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-03 |

## C-APP-CATALOGUE

| Contract | Value |
|---|---|
| responsibility | Proposed catalogue, profile, canonical vocabulary and capability use cases. |
| owner_module | Future application catalogue module |
| inputs | Authorized query |
| outputs | bounded field-level projection |
| dependencies | C-PORTS; C-DOMAIN-TYPES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Query only authorized scoped inputs with stable order and explicit completeness/page scope. |
| error_conditions | Unavailable selected fields, incompatible vocabulary or denied cursor. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-04 |

## C-APP-MATCH

| Contract | Value |
|---|---|
| responsibility | Proposed query validation and real matching orchestration; currently blocked. |
| owner_module | Future application matching module |
| inputs | Authorized query and versioned evidence |
| outputs | partitioned result or unavailable |
| dependencies | C-PORTS; C-DOMAIN-TYPES; C-DOMAIN-REAL |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Require accepted real contract, selected fields, rights, closure, normalization and eligibility. |
| error_conditions | Held/conflicting/unknown/incompatible inputs; never wrap real rows as synthetic fixtures. |
| status | BLOCKED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-08 |

## C-APP-COMPARE

| Contract | Value |
|---|---|
| responsibility | Proposed two-profile factual comparison, independent of ranking capability. |
| owner_module | Future application comparison module |
| inputs | Exactly two distinct authorized profile projections |
| outputs | labelled factual columns |
| dependencies | C-PORTS; C-DOMAIN-TYPES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Compare only visible facts; absence requires closure, unknown remains unknown. |
| error_conditions | Unauthorized profile/field, stale selection, unavailable factual projection. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-06 |

## C-APP-MEDIA

| Contract | Value |
|---|---|
| responsibility | Proposed per-asset rights resolution and authorized original PNG delivery. |
| owner_module | Future application media module |
| inputs | Asset reference and permitted use |
| outputs | safe metadata/bytes envelope or placeholder |
| dependencies | C-PORTS; C-DOMAIN-TYPES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Reauthorize before loading and delivery; server owns path, database, user and callback. |
| error_conditions | Unknown rights/asset lineage, invalid PNG, changed hash or revocation. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-07 |

## C-APP-PRIVATE

| Contract | Value |
|---|---|
| responsibility | Proposed separate personal-state, saved-source, purchase and physical-inventory use cases. |
| owner_module | Future application private-data module |
| inputs | Owner-scoped commands with expected version |
| outputs | private acknowledgement/projection |
| dependencies | C-PORTS; C-DOMAIN-TYPES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Manual records only; keep interest, source links, purchases and bottles distinct. |
| error_conditions | Cross-user object, stale version, reused idempotency key with different command, invalid lifecycle. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-09 |

## C-APP-REVIEW

| Contract | Value |
|---|---|
| responsibility | Proposed permission/intake/review decision use cases; not a browser wrapper around operator commands. |
| owner_module | Future curator/application module |
| inputs | Versioned proposal/evidence and authorized reviewer |
| outputs | recorded review/request status |
| dependencies | C-PORTS; C-DOMAIN-TYPES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | A private manual proposal is not capture authority; curator rights do not create a copyright grant. |
| error_conditions | Unapproved acquisition, authority/evidence gap, held conflict or stale reviewed proposal. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-02 |

## C-PORTS

| Contract | Value |
|---|---|
| responsibility | Proposed inward-facing repository, authorization, principal, audit and storage contracts. |
| owner_module | Future domain/application contracts |
| inputs | Versioned request contracts |
| outputs | explicitly typed results |
| dependencies | C-DOMAIN-TYPES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Dependency inversion only; declare required capabilities, not infrastructure/UI implementation. |
| error_conditions | Unimplemented port, missing accepted policy or incompatible schema. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-04 |

## C-DOMAIN-TYPES

| Contract | Value |
|---|---|
| responsibility | Proposed framework-neutral canonical IDs, evidence/domain/version/availability value objects. |
| owner_module | Future domain contracts |
| inputs | Reviewed typed values |
| outputs | immutable domain context |
| dependencies |  |
| trust_boundary | Pure typed domain only; no I/O or browser/database authority. |
| authorized_operations | No HTTP/UI/database connection dependency; no implicit identity/alias/closure conversion. |
| error_conditions | Unknown identity/version, invalid exact value, unsupported domain. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-02 |

## C-DOMAIN-REAL

| Contract | Value |
|---|---|
| responsibility | Future separately approved real-data method entry boundary, not an existing scorer. |
| owner_module | Future matching domain module |
| inputs | Accepted real method/config + eligible evidence |
| outputs | exact partitioned fit |
| dependencies | C-DOMAIN-TYPES; C-MATH-PRIMITIVES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Reject missing real contracts or evidence; ordering remains rational before display rounding. |
| error_conditions | No valid score -> unavailable, never 0%; incompatible partitions never merged. |
| status | BLOCKED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-08 |

## C-SYNTHETIC-M1

| Contract | Value |
|---|---|
| responsibility | Implemented fixed-fixture notes-layered pure typed scorer; no application or real-data boundary. |
| owner_module | matching_math.synthetic_m1.score_synthetic_notes_layered |
| inputs | FixtureProfile/FixtureVocabulary/M1Config |
| outputs | M1BatchResult |
| dependencies | C-MATH-PRIMITIVES |
| trust_boundary | Pure typed domain only; no I/O or browser/database authority. |
| authorized_operations | Only exact accepted M1 synthetic contract and explicit configuration. |
| error_conditions | Invalid fixture/domain/config/input bounds; no fallback real method. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | Existing IMP-MATCH-08; future real task remains separate |

## C-SYNTHETIC-B1

| Contract | Value |
|---|---|
| responsibility | Implemented fixed-fixture positive-domain B1 pure typed scorer; no application boundary. |
| owner_module | matching_math.synthetic_b1.score_synthetic_b1 |
| inputs | B1Query/B1Profile/B1Vocabulary/B1Config |
| outputs | B1BatchResult |
| dependencies | C-MATH-PRIMITIVES |
| trust_boundary | Pure typed domain only; no I/O or browser/database authority. |
| authorized_operations | Only exact accepted synthetic required/optional/excluded and rational fit rules. |
| error_conditions | Unknown is not zero; incomplete cannot prove exclusion; invalid fixture/config/query rejected. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | Existing IMP-MATCH-03; no B2/real extension authorized |

## C-MATH-PRIMITIVES

| Contract | Value |
|---|---|
| responsibility | Implemented deterministic arithmetic/set primitives; not a full real ranking feature. |
| owner_module | matching_math.primitives |
| inputs | Explicit set/vector inputs |
| outputs | exact arithmetic results |
| dependencies |  |
| trust_boundary | Pure typed domain only; no I/O or browser/database authority. |
| authorized_operations | Mathematical operation only; does not create rights, identity, evidence or eligibility. |
| error_conditions | Invalid domains, types or unsupported numeric inputs per existing contract. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | Existing primitives scope; reuse only through accepted future methods |

## C-PG-READ

| Contract | Value |
|---|---|
| responsibility | Implemented internal read_profile SQL/DTO adapter with a trusted execute callback; future service wrapper absent. |
| owner_module | database.matching_input.read_profile |
| inputs | Trusted executor + profile UUID |
| outputs | ProfileInput |
| dependencies | C-PG-SCHEMA |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | SQL and DTO guards are internal; caller must establish genuine session and authorized execution. |
| error_conditions | Admin/role/scope/rights/shape failures; no authentication, pool or transport supplied. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | Existing IMP-MATCH-01; future AM-04 adapter/composition |

## C-PG-WRITE

| Contract | Value |
|---|---|
| responsibility | Future repository for exact approved private/reviewer commands; not currently an application write service. |
| owner_module | Future infrastructure write adapter |
| inputs | Verified command/context |
| outputs | atomic write acknowledgement |
| dependencies | C-PORTS; C-PG-SCHEMA |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | RLS/FKs/deferred checks remain active; accepted command scope and exact least privilege required. |
| error_conditions | Unauthorized write, invalid relationship, conflict, stale version, failed commit -> rollback. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-02 / AM-09 only after separate approval |

## C-PG-SCHEMA

| Contract | Value |
|---|---|
| responsibility | Implemented eight migration sources, contract functions, scopes and RLS; live database state not verified here. |
| owner_module | database/migrations and schema_contract.json |
| inputs | Approved SQL/tooling |
| outputs | scoped data and integrity constraints |
| dependencies |  |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Existing approved operator use only; no new schema/role or app identity established by this diagram. |
| error_conditions | Live engine/version/persistence unknown; historical tests do not prove current service availability. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | Existing P1; future changes need their own approved task |

## C-OPERATOR-CLI

| Contract | Value |
|---|---|
| responsibility | Implemented local guarded Docker/SQL/migration tooling, outside the ordinary browser trust boundary. |
| owner_module | database.local and approved operator entrypoints |
| inputs | Explicit approved local operator action |
| outputs | guarded local result |
| dependencies | C-PG-SCHEMA |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | No HTTP handler may expose migration/start/reset/restore shell access. |
| error_conditions | Wrong target/labels/volume/database/approval or unavailable local engine. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | Existing operator tasks; AM-11 future recovery/deployment gate |

## C-SOURCE-CAPTURE

| Contract | Value |
|---|---|
| responsibility | Implemented pinned-source loader/ETL tooling; new acquisitions and field preview tasks remain gated. |
| owner_module | database.scento_etl and approved local source contracts |
| inputs | Pinned licensed files + exact approved plan |
| outputs | staging/capture workflow |
| dependencies | C-OPERATOR-CLI |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Do not invoke new import/capture or IMP-ENR-01 from this task or application request. |
| error_conditions | Pin/license/plan/ordinal mismatch, unapproved database/output or unresolved review. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | AM-01 / AM-02 under exact new gates |

## C-REVIEW-DATA

| Contract | Value |
|---|---|
| responsibility | Implemented provenance/selection/conflict/permission schema, not a completed web review service. |
| owner_module | sources/source_records/source_observations/canonical_selections/data_conflicts |
| inputs | Immutable observations and reviewer decisions |
| outputs | selected facts under existing constraints |
| dependencies | C-PG-SCHEMA |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Preserve 43 proposals, 44 holds and Khamrah conflicts; no automatic winner or hold release. |
| error_conditions | Conflicting membership, cross-scope/FK/selection/provenance violation. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | AM-02 future controlled transition |

## C-ASSET-VALIDATOR

| Contract | Value |
|---|---|
| responsibility | Implemented pure PNG inspection and registered local-asset validation callbacks; not an HTTP media service. |
| owner_module | database.image_validation.inspect_png / validate_registered_asset |
| inputs | Bytes / registered asset + server-owned loader and operation |
| outputs | ImageMetadata |
| dependencies | C-OPERATOR-CLI |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Current local-static-png-v1 only; technical PASS is not license, subject binding or browser authorization. |
| error_conditions | Byte/chunk/CRC/dimension/stream/rights/hash/source/ancestor mismatch; no silent conversion. |
| status | IMPLEMENTED |
| test_status | Historical source-bound evidence only; no runtime rerun. |
| future_task | Existing image scope; AM-07 future intake/delivery |

## C-ASSET-STORE

| Contract | Value |
|---|---|
| responsibility | Proposed private original-byte storage with immutable hash/source/rights lineage and no public webroot. |
| owner_module | Future local filesystem storage adapter |
| inputs | Approved scoped original |
| outputs | bytes |
| dependencies | C-PORTS |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | No arbitrary browser paths/URLs; no derivatives, codecs, image acquisition or service selected here. |
| error_conditions | Traversal, missing hash, incompatible rights, revoked access, stale restore. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-07 |

## C-AUDIT

| Contract | Value |
|---|---|
| responsibility | Existing audit schema plus a proposed redacted application event adapter; not a deployed logging service. |
| owner_module | audit_events schema / future application audit port |
| inputs | Permitted actor/operation/correlation/revision decision |
| outputs | scoped audit event |
| dependencies | C-PORTS |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | No secrets, raw shopping URLs/preferences, private result bodies or unapproved retention defaults. |
| error_conditions | Unapproved retention, excessive detail, restricted actor/object identifiers. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-03 / AM-04 policy and implementation |

## C-CONFIG

| Contract | Value |
|---|---|
| responsibility | Proposed explicit versioned method, bounds, rights-use and operation policy registry. |
| owner_module | Future accepted-policy configuration |
| inputs | Explicit accepted policy IDs/versions |
| outputs | immutable operation configuration |
| dependencies | C-DOMAIN-TYPES |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Missing policy disables operation; no hidden numeric limits, stack, provider, permissions or fallback. |
| error_conditions | Unknown/unaccepted configuration or inconsistent policy snapshot. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-03 / AM-04 / AM-08 exact contracts |

## C-COMPOSITION

| Contract | Value |
|---|---|
| responsibility | Proposed composition root wires implementations to contracts without domain-to-UI coupling. |
| owner_module | Future service composition layer |
| inputs | Accepted deployment/contract choices |
| outputs | configured future application |
| dependencies | C-TRANSPORT; C-APP-CATALOGUE; C-APP-MATCH; C-APP-COMPARE; C-APP-MEDIA; C-APP-PRIVATE; C-APP-REVIEW; C-AUTHZ; C-PG-WRITE; C-ASSET-STORE; C-AUDIT |
| trust_boundary | Browser has no authority; genuine session/scope/rights gate all data. Operator and future app are separate. |
| authorized_operations | Wire only approved genuine principals, adapters and policies; do not use operator tooling as app authority. |
| error_conditions | Missing implementation, incompatible contracts, absent approvals or circular wiring. |
| status | PROPOSED |
| test_status | NOT RUN; proposed architecture acceptance only. |
| future_task | AM-04 after exact ADR/principal decisions |

## Dependency edges

| Consumer | Dependencies |
|---|---|
| C-UI-SHELL | C-DTO |
| C-UI-PAGES | C-UI-SHELL; C-DTO |
| C-TRANSPORT | C-DTO; C-AUTHN; C-PRINCIPAL; C-PORTS |
| C-DTO | None; leaf contract/domain |
| C-AUTHN | C-PORTS |
| C-PRINCIPAL | C-AUTHN; C-PORTS; C-PG-SCHEMA |
| C-AUTHZ | C-PORTS; C-PG-READ; C-CONFIG |
| C-APP-CATALOGUE | C-PORTS; C-DOMAIN-TYPES |
| C-APP-MATCH | C-PORTS; C-DOMAIN-TYPES; C-DOMAIN-REAL |
| C-APP-COMPARE | C-PORTS; C-DOMAIN-TYPES |
| C-APP-MEDIA | C-PORTS; C-DOMAIN-TYPES |
| C-APP-PRIVATE | C-PORTS; C-DOMAIN-TYPES |
| C-APP-REVIEW | C-PORTS; C-DOMAIN-TYPES |
| C-PORTS | C-DOMAIN-TYPES |
| C-DOMAIN-TYPES | None; leaf contract/domain |
| C-DOMAIN-REAL | C-DOMAIN-TYPES; C-MATH-PRIMITIVES |
| C-SYNTHETIC-M1 | C-MATH-PRIMITIVES |
| C-SYNTHETIC-B1 | C-MATH-PRIMITIVES |
| C-MATH-PRIMITIVES | None; leaf contract/domain |
| C-PG-READ | C-PG-SCHEMA |
| C-PG-WRITE | C-PORTS; C-PG-SCHEMA |
| C-PG-SCHEMA | None; leaf contract/domain |
| C-OPERATOR-CLI | C-PG-SCHEMA |
| C-SOURCE-CAPTURE | C-OPERATOR-CLI |
| C-REVIEW-DATA | C-PG-SCHEMA |
| C-ASSET-VALIDATOR | C-OPERATOR-CLI |
| C-ASSET-STORE | C-PORTS |
| C-AUDIT | C-PORTS |
| C-CONFIG | C-DOMAIN-TYPES |
| C-COMPOSITION | C-TRANSPORT; C-APP-CATALOGUE; C-APP-MATCH; C-APP-COMPARE; C-APP-MEDIA; C-APP-PRIVATE; C-APP-REVIEW; C-AUTHZ; C-PG-WRITE; C-ASSET-STORE; C-AUDIT |

No framework, provider, database login, transport budget, port, Docker image or service is selected by this registry. [[Dependency_Based_Implementation_Roadmap]] uses AM codes as proposal units, not active implementation authorization.
