---
id: DPT-PLAN-010-OWNER-PACKET
project: DoomParfum By TK
type: owner_decision_packet
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, decisions, amendment]
source_of_truth: "../../README.md"
---

# Architecture Owner review packet

Packet identity: **POST28-ARCH-ODP-1**. All choices below are **PROPOSED / UNANSWERED**. The verification record binds the frozen file SHA-256 after authoring. This is a design-amendment request, not an implementation contract or recorded Owner answer. A Planning PR merge does not select unchecked policies or grant source/image/database/application/Production authority.

## Preserved authority

Main `168715bc9bc5fff968524074257dc106a8a63638` contains Owner-merged PR26 synthetic M1, PR27 synthetic B1 and PR28 next-wave planning. Exact M1/B1 contracts remain unchanged and accepted only for fixed-fixture pure typed Python. The current Owner accepts PR28's direction and explicitly requests architecture refinement before implementation; that is **CONFIRMED DIRECTION**, not exact A/B/I acceptance.

POST27-ODP-1 remains byte-preserved in its canonical Git representation, SHA-256 `0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c`. Its original local artifact is retained. The exact five-record proposal note remains SHA-256 `053a7583d33beaa103e4cb94781991504aa6eee4b380fefe7cc1d2095f2c71d5`. Neither document is edited by this architecture amendment. IMP-ENR-01 is **NOT STARTED**. New G/H/F refinements are versioned here rather than silently editing historical choices.

## Effect on existing A–I rows

| Existing row | Effect and reason | Alternative / consequence | Exact approval status |
|---|---|---|---|
| A first bounded preview | No change to the five source inputs or preview-only boundary | Accept/defer the original exact proposal separately; no service-stack dependency added | PROPOSED / UNANSWERED; no execution |
| B selected fields/rights | No change to original field allowlist, pins, source-use or attribution contract | Narrow/defer fields through a new exact answer; architecture cannot grant rights | PROPOSED; new use-specific source rights still independently required |
| C completeness | Clarify real field/domain/edition/version closure is separate from synthetic fixture completeness and factual display | Defer absence-sensitive real methods; show unknown/incomplete rather than invent absence | PROPOSED for real sources; no assertion made |
| D normalization/holds | No change to 43 proposals, 44 holds or independent Khamrah conflicts | Continue review-only evidence work under separate scope; no silent deduplication or winner | PROPOSED transitions; no promotion/release |
| E two-PNG verification | No change to exact 021/022 metadata-verification-only proposal | Defer; any later binary intake needs separate exact permission/task | NOT approved for image bytes |
| F media use/storage/display | Refined with same-byte validation/delivery, private projection, cache, revocation and per-use lineage boundaries | Keep placeholders/metadata only; later exact intake/delivery and retention contract required | PROPOSED design; REQUIRES EXTERNAL PERMISSION where actual rights are absent |
| G stack | Refined from three general choices to four explicit architectural alternatives and phased Python/UI separation | Retain CLI; choose another direction with exact port/bridge/maintenance proof | PROPOSED; no framework/driver/ORM/provider/image/port selected |
| H genuine principal | Refined with verified initial LOGIN, effective privileges, per-principal leases and cancellation/pool cleanup; simple equal session/current user is not initial-login provenance | Defer app access or separately review an explicit binding-model amendment | PROPOSED; no auth bridge, role, schema or identity mutation |
| I first implementation | Original independent offline preview remains unchanged; a later private-web vertical slice has its own principal/rights/transport/UI dependencies | Continue CLI/approved preparation; choose future slice only after exact contract/task acceptance | Original A/B/I not accepted; no new implementation starts |

The amendment preserves product requirements, not implementation approvals. R12/R19 future research-assistance/AI-intake intent and R31 deferred spending analytics are retained without selecting a service or introducing a matching dependency.

## New design questions and exact scope

| Row | Recommended design choice | Alternatives | Benefit / risk / operational consequence | Prerequisites and acceptance evidence |
|---|---|---|---|---|
| ARC-01 logical architecture | `DIR-A-THEN-D`: keep CLI now; target Python application/domain with logically separate UI contracts | Retain CLI/defer; local Python realization B with separation; TypeScript C with exact rational port/worker parity | Reuses current language and isolates UI/domain; adds explicit contract/version discipline. No need for microservices or a second UI server | ADR-ARCH-POST28-1; 30-component DAG with no UI-to-domain/server-module coupling or cycles; actual framework/version/host decisions remain later |
| ARC-02 principal architecture | `PRINCIPAL-CLEAN`: separately approved clean application-private pilot with genuine nonadmin LOGIN established before intake | `PRINCIPAL-AMEND`: separate binding-model plan; or `PRINCIPAL-DEFER` | Avoids immutable operator-owner rewrite; requires trusted proof/credential mapping, privilege and pool lifecycle design. A shared admin login/filtering is not an option | Exact identity/provider/role/scope/credential/lease/transaction contract and source permissions; forged/admin/SET ROLE/GUC/impersonation/cross-user/revocation/pool tests before its future PR |
| ARC-03 full IA and element relationships | `IA-FULL-PRIVATE`: retain all three areas, 17 proposed routes and the explicit interaction inventory | Implement only a later approved slice while retaining the rest as planned/deferred product scope | Avoids dropping Cart/Collection/Dashboard or conflating personal state, source, purchase and bottles; larger roadmap is split into bounded units | Unified IA, state and matrix/IF/component refs consistent; route authorization and unavailable/A11Y cases specified. No frontend or API route implemented |
| ARC-04 typed contracts and resource policy | `CONTRACT-STRICT`: explicit IF/schema/version, genuine server context, no coercion/fallback, exact rational wire/order semantics | Defer transport; propose a different explicit encoding/policy contract | Prevents hidden 8KiB/internal2MiB inheritance and JS float sorting; numeric bounds/spec/provider selection remain exact future choices | 29 logical IFs and their proposed schemas; missing policy blocks; extra/malformed/coerced/cross-partition/stale inputs rejected in future tests. No executable API/schema framework selected |
| ARC-05 cache/offline privacy | `CACHE-CONSERVATIVE`: static non-personal UI content identity only; operational data request/authorized-render scoped, no-store/no shared or persistent private cache initially | Defer PWA/offline entirely; later separate rights/revocation-reviewed public projection cache | Preserves future offline-shell intent without stale private data revival. Cannot erase already delivered content | Eight operation-specific cache contracts, scope/revision binding, logout/revoke/offline/late-response/restore negatives; no service worker or storage implementation |
| ARC-06 personal command boundaries | `PRIVATE-SEPARATE`: own interest/cart state, buying sources, manual Ordered stamp, purchase history and physical bottles are distinct commands | Defer all private writes and implement read-only catalogue first | Preserves R25 non-commerce and R26 history; requires exact mutation/idempotency/known-unknown money/unit/date/retention policies | Cross-user/FK/lost-update/replay, no cascade history loss, no null-price0 or order/payment/fetch side effect; all future mutation tests NOT RUN |
| ARC-07 real matching boundary | `REAL-SEPARATE`: separately accepted real method/context after all identity/selected-field/right/vocabulary/normalization/domain/closure/hold/eligibility gates | Factual comparison only; defer real A/B1/B2 | Avoids disguising real records as fixtures; many inputs remain unavailable until actual data proof | Separate real method/config/partition/explanation contract, exact rational ordering and distinct confidence/evidence; no score/eligibility created by design acceptance |
| ARC-08 media boundary | `MEDIA-ORIGINAL-GATED`: per-asset approved original PNG, immutable bytes/hash/source/rights, same validated snapshot delivered after reauthorization | Placeholders/metadata only; later separate technical/derivative plan if other formats needed | Reuses pure inspection concept without mistaking metadata validation for HTTP delivery; actual authority/features/SHA remain unknown | Exact per-file permission/task and genuine app adapter; current PNG limits, path/use/scope/hash/ancestry/revocation/attribution negatives; no byte retrieval or codec change now |
| ARC-09 sequencing | `SLICE-READONLY`: later genuine-principal + authorized catalogue/detail + accessible shell, media placeholders and disabled real matching/private writes | Keep CLI; independently pursue original preview only after A/B/I; choose another explicitly bounded slice | Small vertical proof without coupling all roadmap work into one PR; not automatically enabled by this packet | Exact ADR/framework/principal/field-rights/transport/budget/UI/task contracts plus Planning/Implementation Gates. No unit in this task executes |

All alternatives are valid deferrals. Design choices do not supply licensor authority, completeness facts, genuine credentials or a Production gate. The detailed task units are AM-01 through AM-11 in [[Dependency_Based_Implementation_Roadmap]]; those codes are not active implementation task allocations.

## Proposed Owner reply form

The following is a template, not an answer. Reply by exact packet version/hash, row and design-only scope. Changes to method, rights, identity, fields or other material contract choices require a revised version/hash and explicit review before implementation.

```text
Packet: POST28-ARCH-ODP-1
SHA-256: <copy exact frozen file hash from architecture verification record>
Scope: Architecture design only; no implementation, acquisition, DB/auth/cache or deployment action.

ARC-01: DIR-A-THEN-D / CLI-DEFER / B-SEPARATED / C-WITH-PARITY / MODIFIED(<exact text>)
ARC-02: PRINCIPAL-CLEAN / PRINCIPAL-AMEND / PRINCIPAL-DEFER
ARC-03: IA-FULL-PRIVATE / SLICE-ONLY-WITH-ROADMAP-RETAINED / DEFER
ARC-04: CONTRACT-STRICT / DEFER / MODIFIED(<exact encoding/policy design>)
ARC-05: CACHE-CONSERVATIVE / NO-OFFLINE / LATER-SEPARATE-CACHE-PLAN
ARC-06: PRIVATE-SEPARATE / DEFER-WRITES / MODIFIED(<exact design>)
ARC-07: REAL-SEPARATE / FACTUAL-COMPARE-ONLY / DEFER
ARC-08: MEDIA-ORIGINAL-GATED / PLACEHOLDER-METADATA-ONLY / DEFER
ARC-09: SLICE-READONLY / CLI-ONLY / ORIGINAL-PREVIEW-AFTER-ITS-EXACT-GATES / MODIFIED(<exact slice>)

Actual framework/driver/ORM/auth provider/protocol, spec version, numeric resource budgets,
port/image/host, credentials, source/asset permissions and future implementation task scope
remain unselected until a separate exact ADR/contract is supplied and accepted.

POST27-ODP-1 A/B/I exact preview approval: NOT GIVEN by this reply unless separately supplied
against that unchanged packet and preview note/version/hash. Do not start IMP-ENR-01 from this form.

Date/time and Owner reference: <Owner supplied>
No real-data ranking, hold release, source/image acquisition, Production mutation or agent merge.
```

## Readiness versus unresolved facts

The architecture may be ready for review while implementation remains blocked. Current live DB counts, role/session availability, rights, closure/eligibility and actual media bytes are NOT VERIFIED here. Current synthetic code is source-backed and historically tested, not a deployed application capability. All future application/security/accessibility/real-method/media tests are SPECIFIED / NOT RUN.

The amendment must preserve eight migrations, original receipts, accepted M1/B1 contracts, POST27-ODP-1, 43 proposals, 44 holds and Khamrah records. PR8 remains blocked, unchanged and unexperimented. No secret/private export/raw dataset/image binary belongs in the public PR. [[DPT-PLAN-010_Architecture_Verification]] records actual research/static checks, independent review, failures/corrections and exact publication/receipt/handoff bindings after they exist.
