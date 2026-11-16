---
id: DPT-PLAN-010-PYTHON-RESEARCH
project: DoomParfum By TK
type: architecture_research
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, python, transport, research]
source_of_truth: "../../README.md"
---

# Python service, typing and transport research

This research supports [[System_Architecture_Refinement]] and [[Function_Interface_and_DTO_Contracts]]. It does not select a framework, package, specification dialect, auth provider, port, container image or deployment. [[Component_and_Dependency_Registry]] owns the proposed dependency direction; [[UI_Element_Function_Matrix]] maps logical operations; [[Architecture_Owner_Review_Packet]] owns exact proposed decisions.

## Evidence and versions

The workstation reports Python **3.11.9**. The historical 194-method offline report also records Python3.11.9 at source8eef8f13265adc14db0cae82ff77cfc4863853ce. Official `/3.11/` pages retrieved for this task display documentation3.11.18: that is a documentation maintenance version, not a runtime upgrade. No package installation, configuration, Python upgrade, type-checker run, server or DB operation occurred. All research was retrieved through the existing search_service web connector using primary official documentation.

Each source below separates official findings from project inference. Retrieval timestamps use UTC. Living documentation is recorded as living rather than assigned a fabricated package version. Summaries use brief paraphrases; no raw source pages or quoted blocks are stored.

## S-IF-01 — typing — Support for type hints

Document version: **Python 3.11.18 documentation; /3.11 living maintenance series**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: Annotations are not runtime validation. Protocol supports structural interface descriptions. Runtime-checkable protocol checks do not validate complete function signatures. [Official source](https://docs.python.org/3.11/library/typing.html).

Project inference — PROPOSED: Keep ports/domain typed independently of HTTP and validate untrusted input separately. A Protocol sketch would describe a future port, not create an authenticated transport.

Limit: Installed Python observed3.11.9; no type checker installed/run; maintenance documentation version is not installed runtime version.

## S-IF-02 — dataclasses — Data Classes

Document version: **Python 3.11.18 documentation; /3.11 living maintenance series**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: Dataclasses generate methods from annotated fields. With limited exceptions the decorator does not inspect annotated field types. Frozen dataclasses emulate read-only instances. [Official source](https://docs.python.org/3.11/library/dataclasses.html).

Project inference — PROPOSED: Reuse existing frozen typed domain records without treating construction or frozen=True as proof of strict validation, rights, deeply immutable referenced objects or authorization.

Limit: No new dataclass or runtime validator implemented; source fields and generated methods must be distinguished.

## S-IF-03 — fractions — Rational numbers

Document version: **Python 3.11.18 documentation; /3.11 living maintenance series**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: Fraction supports exact rational arithmetic. Constructing from a binary float preserves that float value rather than the intended decimal ratio. [Official source](https://docs.python.org/3.11/library/fractions.html).

Project inference — PROPOSED: Preserve accepted exact int/Fraction inputs and rational comparison. Order within compatible partitions before proposed wire integer-string serialization and display rounding.

Limit: Python Fraction itself accepts formats the project forbids; a future transport must apply narrower explicit grammar and numeric bounds. No float coercion or limit_denominator repair.

## S-IF-04 — Dependencies — FastAPI

Document version: **UNVERSIONED / LIVING; no installed FastAPI version selected or verified**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: Dependency injection supplies declared shared dependencies and can organize authentication, role checks and database connections. [Official source](https://fastapi.tiangolo.com/tutorial/dependencies/).

Project inference — PROPOSED: If later selected, compose session verification, a genuine principal lease and per-use authorization through explicit dependencies. Domain modules must not import framework dependencies.

Limit: A dependency does not create PostgreSQL logins, verify all effective privileges, establish an immutable owner binding or prove RLS/pool isolation. Official page installer suggestions were not executed.

## S-IF-05 — OAuth2 scopes — FastAPI

Document version: **UNVERSIONED / LIVING; no installed FastAPI version selected or verified**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: OAuth2 scopes are integrated with OpenAPI. The application still enforces scopes and other security requirements in its own code. OAuth2 scopes are optional. [Official source](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).

Project inference — PROPOSED: Keep provider/session choice unresolved; scopes alone cannot authorize a private object, source use, asset or genuine database principal. Verify ownership/scope before lookup/count/pagination/scoring/bytes.

Limit: Research does not select OAuth2, JWT, an auth provider, the examples secret handling, or a browser password flow.

## S-IF-06 — Strict Mode — Pydantic Validation

Document version: **UNVERSIONED / LIVING latest; original https://docs.pydantic.dev/latest/concepts/strict_mode/ redirected here; exact package version not shown**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: Default validation can coerce input. Strict mode reduces coercion but JSON input can still accept representations such as date strings that strict Python validation rejects. [Official source](https://pydantic.dev/docs/validation/latest/concepts/strict_mode/).

Project inference — PROPOSED: If selected later, specify exact JSON grammar, forbid unknown keys/coercion and validate resource bounds plus domain semantics explicitly; a strict flag is insufficient. Never log rejected private values by default.

Limit: No Pydantic version selected, installed or tested. JSON and Python validation paths need separate acceptance cases.

## S-IF-07 — OpenAPI Specification latest

Document version: **Observed v3.2.1, published10 September2026; latest alias is mutable**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: OpenAPI describes HTTP interfaces. Multiple security requirement alternatives are OR; schemes within one requirement are AND. An empty requirement permits anonymous access. [Official source](https://spec.openapis.org/oas/latest.html).

Project inference — PROPOSED: Use explicit operation security and bounded schemas only after HTTP/stack ADR. Review generated contracts for accidental optional security; keep logical IF IDs independent of HTTP paths.

Limit: Latest published specification is not a selected runtime/framework contract version. No OpenAPI document or endpoints generated.

## S-IF-08 — OpenAPI Specification v3.2.1

Document version: **v3.2.1,10 September2026; explicit published version URL**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: The versioned specification describes HTTP operations, schemas and security requirements. Security scheme documentation does not itself enforce application policy. [Official source](https://spec.openapis.org/oas/v3.2.1.html).

Project inference — PROPOSED: A later explicit ADR must choose a supported published contract version and verify generator/client/server compatibility. This inventory remains framework-neutral.

Limit: No compatibility test or adoption of3.2.1; package versions cannot be inferred from this page.

## S-IF-09 — OpenAPI Specification v3.1.2

Document version: **v3.1.2,19 September2025; explicit published version URL**. Retrieved: `2026-11-16T13:27:17.256884+00:00`.

Official finding: An independently versioned published3.1-series specification remains available, distinct from the observed latest3.2.1. [Official source](https://spec.openapis.org/oas/v3.1.2.html).

Project inference — PROPOSED: Compare tooling support for versioned contracts after the stack ADR; do not equate an older supported contract with an implementation defect or silently upgrade.

Limit: No version choice, runtime acceptance or generated contract implied; compatibility remains untested.

## Architecture consequences — PROPOSED

Existing pure Python scorers can remain isolated domain modules. A future Python application service would reuse their language and exact arithmetic without a TypeScript rewrite or subprocess-per-request bridge. That advantage does not authorize real data in synthetic contracts. Real matching requires a separately accepted real context, closure, normalization, selected-field rights and eligibility contract. A TypeScript backend would require an explicit trusted Python boundary or a separately reviewed exact semantic port, increasing cross-language testing and operational work. Keeping the current CLI is the smallest current operational surface while application principal and transport policies remain unresolved. This is a reasoned project comparison, not a Python documentation recommendation of a particular architecture.

The proposed flow is transport validation, verified session, genuine principal lease, use-case authorization, ports, infrastructure, then typed authorized projection. Domain computation depends on domain types and explicit ports, not on browser handlers, framework dependencies or SQL. Authentication cannot be replaced by a DTO annotation, a dependency graph or an OpenAPI security declaration. A later ADR must decide sync/async execution, driver/pool, cancellation, time/resource bounds and authentication lifecycle with focused negative tests. None is selected here.

Strict transport validation must define exact accepted representations, unknown-field rejection, depth/string/list/numeric budgets and safe errors. `TransportBudgetPolicy.v1` in the proposed registry requires explicit owner-approved numbers. Missing policy blocks execution. Existing adapter2MiB internal bound, selected payload64KiB and synthetic64-candidate bounds do not silently become HTTP limits; an8KiB request budget is not approved or implemented.

Future exact-score wire projection uses canonical decimal integer strings for numerator and denominator only after exact rational ordering in compatible partitions. It is not a permission to accept fraction expressions, decimal/float inputs, exponent strings or coercion into existing synthetic typed calls. Display rounding remains presentation, never a sort key. Unknown/unavailable scores remain null/stateful, never0%.

## Required future acceptance — SPECIFIED / NOT RUN

Compare direct-Python and JSON validation paths for booleans-as-integers, numeric strings, floats, NaN/infinity, date/UUID coercion, unknown keys, duplicate JSON keys, nesting, collection limits, identifier length and exact numerator/denominator grammar. Confirm missing policy/version fails closed before domain work. Test rejection before expensive member/token scans where the accepted contract requires staged bounds.

Test real session binding, forged browser identity/role, stale membership/rights, effective admin/BYPASSRLS/owner inheritance, cancellation and cross-principal pool reuse. Confirm denial precedes restricted lookup/count/page/scoring/media bytes, errors mask private existence, and framework/security documentation never substitutes for those tests. No application runtime acceptance is claimed by documentation checks.

## Approval and preservation

POST27-ODP-1 remains unchanged at SHA-256`0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c`. New A–I choices remain unapproved. IMP-ENR-01 is not started. All43 normalization proposals,44 holds, Khamrah conflicts and PR8 BLOCKED status remain unchanged. This research neither acquires source/image data nor changes synthetic contracts, migrations, runtime files, existing receipts or Production.
