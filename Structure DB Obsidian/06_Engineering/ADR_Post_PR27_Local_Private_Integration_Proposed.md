---
id: ADR-POST27-LOCAL-PRIVATE-1
project: DoomParfum By TK
type: architecture_decision_proposal
status: proposed
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, adr, application, private, security]
source_of_truth: "../../README.md"
---

# ADR proposal: local-private integration after synthetic M1 and B1

**Status: PROPOSED. No stack, authentication, service, source, image or publication implementation is accepted by this ADR.** It consolidates the choices already documented in [[Private_Application_Architecture_Plan]] after PR26/27 merged. Detailed source boundaries and tests are in [[Post_PR27_Application_Integration_and_Security]]. The single Owner answer surface is [[Post_PR27_Owner_Decision_Packet]].

## Context

Main `8eef8f13265adc14db0cae82ff77cfc4863853ce` contains Python/PostgreSQL operator tooling, an internal guarded read-only profile adapter and two Owner-approved synthetic pure typed Python scorers. There is no installed application runtime, HTTP authentication/session bridge, API route, frontend, public projection or approved real-data matching contract in the tracked source inventory. A proposed technology name in an older document is not an installed dependency or an Owner choice.

The existing database identity derives from genuine PostgreSQL `session_user` and immutable application subject/scope records. A shared superuser connection with a user label cannot satisfy that identity contract. Existing synthetic fixture domains and versions must stay unchanged; catalogue records must not be disguised as fixtures to reuse a synthetic-only entrypoint.

## Alternatives

| Criterion | Continue CLI-only baseline | Proposed local Python service | Proposed TypeScript backend |
|---|---|---|---|
| Matching reuse | Direct use of current pure Python functions for approved synthetic work | Direct Python reuse once the relevant future real contract is separately approved | Requires a reviewed Python invocation boundary or a separately tested exact-rational port; no automatic formula parity |
| API/serialization | No new API; manual/operator process remains explicit | New typed transport, parser, response/error and cancellation contracts required | Same transport contracts plus cross-language wire/version parity |
| Authentication and database access | Existing operator tooling is not an application principal | Genuine per-principal nonadmin connection/session design still required; framework does not supply database entitlement | Same genuine identity requirement; ORM or server session does not replace PostgreSQL identity/RLS |
| Type safety | Existing Python typed dataclasses and runtime validation; no web DTO guarantee | Static typing plus explicit runtime transport validation; no implicit coercion/defaults | TypeScript types help callers, but erased types still require runtime checks and exact-rational handling |
| Maintenance | Least new runtime surface; limited end-user workflow | One primary language and reference implementation; service/auth/pool operations add maintenance | Additional language, package/ORM lifecycle and either a port or inter-process protocol increase surface |
| Security | Avoids creating a new network boundary, but operator credentials still must not be exposed to an app | Needs private host/origin/session, least privilege, pool isolation, bounded input/output and safe logs | Same controls; framework selection alone proves none of them |
| Future web/private deployment | Limited UX; does not block later service design | Can support a future private UI after separate approval and tests | Can support a future private web UI after the same gates; Next.js/Drizzle are not selected here |
| Testing cost | Existing offline regression plus separately authorized operator checks | New genuine-session, rights, transport, concurrency, revocation and browser integration suites | Those suites plus Python/TypeScript semantic, Fraction, ordering and explanation parity if code is ported |

## Recommended exact direction — not an accepted decision

Keep the CLI/operator baseline while the data and session gates are unresolved. If the Owner chooses to pursue a local service next, prefer **Python** for the first private service because the current deterministic reference functions and internal adapter are Python. Do not select a framework, driver, ORM, database role scheme, authentication provider, Docker image, port, cookie policy or transport byte budget by implication.

The first recommended implementation remains the separately bounded existing-local five-record data/claim-preview task in [[Post_PR27_Data_Readiness_and_Pilot]], after exact Owner scope acceptance and the applicable merged planning contract. That preview is independent of any API and does not create canonical selections, closure, eligibility, database writes or real rankings. A service is a later, separate implementation task.

For application identity, the existing clean disposable nonadmin-principal-before-intake option is a recommendation requiring explicit Owner selection and separate source/ingestion/session tests. Defer access is a valid alternative. A revised identity binding model requires its own reviewed amendment; rewriting old immutable subjects or using a superuser shim is not an alternative under this ADR.

## Operational implications and acceptance

An accepted stack direction alone must not enable access. Before a future service: prove the physical PostgreSQL identity, effective least privilege, authorized selected provenance, exact active operation rights, current review/hold state, private response projection and request/pool cleanup. Before real matching: approve compatible canonical vocabulary, selection snapshots, layer/domain closure and normalization, explicit eligibility and a separately versioned real-data entry boundary. Before media delivery: approve exact assets, storage/display uses, attribution, technical format and revocation behavior. Before public/cloud use: obtain a separate explicit gate.

Private catalogue display and real matching have different prerequisites. The six-screen map may remain a design while fields or matching are unavailable. Structural Fit, Data Confidence and Direct Pairwise Evidence must remain separate; no model percentage is scientifically measured smell similarity.

Negative controls must reject admin/BYPASSRLS/owner-role sessions, spoofed subject/GUC/role claims, cross-user overlays, reused caller state, stale permissions, conflicting/unselected/held inputs, malformed or excessive transport data, synthetic relabeling and unauthorized image delivery. Test in-flight and next-operation revocation semantics after they are explicitly chosen. These are **SPECIFIED / NOT RUN** by this planning lane.

## Owner answer required

Record version `ADR-POST27-LOCAL-PRIVATE-1`, date, reference, scope and one answer in the consolidated packet:

- **Recommended:** retain CLI now; select local Python as a future private-service direction, with implementation still blocked by exact session/data/transport decisions and Planning/Implementation Gates.
- **Alternative:** retain CLI and defer all service selection; or choose TypeScript with an explicit reviewed cross-language reuse/port plan and its extra tests.
- **Modified:** state the exact changed architecture and constraints for a revised proposal.

No checkbox has been answered. A Planning PR merge does not accept an unanswered G/H choice, approve a source/asset use, waive a completeness requirement or authorize implementation. Existing accepted M1/B1 synthetic contracts, receipts, eight migrations, 44 holds and unapproved normalization proposals remain unchanged.
