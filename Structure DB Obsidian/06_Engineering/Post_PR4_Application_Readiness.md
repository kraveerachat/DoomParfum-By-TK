---
id: DPT-POST-PR4-APP-READINESS
project: DoomParfum By TK
type: architecture_readiness
status: proposed
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, matching, api, privacy]
source_of_truth: "../../README.md"
---

# Post-PR4 application and decision readiness

## Current scoped source-review status — 2026-11-13

Reference adapter checkpoint9be247a independently accepted within its local trusted-transport scope;
28focused/157full tests pass and49pilot/security/role manifests unchanged. Both stale-snapshot and
malformed-DTO findings fixed. This does not supply the absent genuine nonadmin Scento owner binding,
accepted closure/DM policies or app/API/publication stack. Existing table entries below remain future
operation proposals, not enabled routes. [[Matching_Owner_Decision_Register]],
[[Matching_Nonadmin_Session_and_Publication_Proposal]] and [[Matching_Data_Readiness_and_Closure_Gates]]
provide explicit recommendations/alternatives/approval status and implementation acceptance criteria.
PR9full-task scope remains gated; all1479matching flags false,44holds unchanged and actual B2inputs
absent. No public projection or provider/auth decision accepted by the review.

Verified base main aa55f8b59acb0872b3b40273a8cdd25198f3ba27 includes Owner-merged PR4,6,7.
The tracked tree contains database Python/SQL tooling and documentation; no web application,
package manifest, Next.js/Drizzle runtime, API framework, authentication service or deployment
configuration was implemented. A proposed stack is not an installed stack. IMP-MATCH-01 is a local
reference adapter; framework/auth/provider selection is not implicit in that implementation.

## Owner decision register

Every DM row remains PROPOSED. The Owner's explicit request authorizes scoped adapter and generic
synthetic math work; it does not accept the numeric/policy alternatives in these rows.

| ID | Recommendation for Owner review | Implemented safely now | Still gated |
|---|---|---|---|
| DM-01 | Separate A, B1 and B2 milestones; defer B3 | separate adapter and mathematical-primitives branches | accept feature milestone boundaries before full scorers |
| DM-02 | Separate Structural/Query Fit, Data Confidence and pair evidence | adapter exposes no score or blended evidence | accept labels/policy; never measured smell-similarity claims |
| DM-03 | Evaluate proposed50/30/20 and25/37.5/37.5 in synthetic fixtures first | generic exact arithmetic only, no defaults | accept weights, closure, minimum layers, grouping and calibration |
| DM-04 | Observed compatible accord values only; separate presence fallback | accord capability unavailable | no selected accord presence or strength data; approve taxonomies/scales/fallbacks |
| DM-05 | Unknown cannot pass strict positive/negative rules | unknown/incomplete states retained | accept80/20, query contradictions, hard rules and absence/completeness semantics |
| DM-06 | Unknown currentness distinct from verified current/historical | lifecycle is unknown | selected lifecycle/market fields, freshness and filters need approval and evidence |
| DM-07 | Genuine nonadmin scoped read-only sessions; private ephemeral results first | local exact-identity adapter, no cache/API/public output | accept stack/auth, session-to-owner binding, retrieval/caps/pagination/cache/share and publication rules |

No legacy DEC/OD decision, source grant or receipt is changed. [[Dual_Mode_Matching_Decisions]]
retains the original proposals. Merged Planning Gate and per-row acceptance are separate events.

## Framework-neutral application contract proposal

All following endpoints are specifications, NOT IMPLEMENTED or enabled routes. Authentication must
bind a real nonadmin database principal or an explicitly reviewed equivalent; request user IDs/GUCs
are not authorization. Validate rights, scope, review/conflicts and eligibility before candidate
retrieval, scoring, total counts, pagination or cache access. Never admin-fetch then filter.

| Proposed operation | Input and response contract | Dependency |
|---|---|---|
| Profile capability | exact canonical UUID; internal typed field/layer states and authorized provenance; uniform missing/unauthorized | accepted session/owner contract and IMP-MATCH-01 final review |
| Mode A query | exact reference UUID, accepted method version and permitted filters; ephemeral bounded results with separate fit, coverage, confidence and evidence | IMP-MATCH-02 plus DM01–04/06/07 and selected inputs |
| Mode B1 query | reviewed canonical note IDs with explicit layers/any-layer, required/excluded rules; reject contradictions and ambiguous aliases | IMP-MATCH-03 plus DM05–07 and accepted closure/absence policy |
| Mode B2 capability | unavailable reason until reviewed compatible accords and policy pass; no invented slider intensities | IMP-MATCH-04 and DM04/05/07 |

Do not expose raw payloads, source-restricted field values, inaccessible counts or per-user source
identifiers in errors/public DTOs. An authorized internal DTO is not a sharing DTO. Responses need
explicit limits on request bytes, candidate/result counts, provenance and response size, stable
method-version plus canonical-UUID ties, and an opaque integrity-protected cursor bound to caller,
scope, filters, sort/method and security revision. Numeric caps and pagination mechanism remain
proposed; current adapter bounds do not accept future endpoint policy.

Prefer no cache initially. Any later cache key must include caller/scope, rights/review and membership
revisions, method/parameters and dataset version; revalidate authorization and revocation before each
hit or next page. No shared public cache or durable query history by default. Stale cursors/results
must fail closed after source/member revocation or eligibility change, without revealing removed
rows/counts. Test cross-user same-query requests, guessed IDs/cursors, shared-member removal,
source expiry/revocation between pages, unknown strict negatives, bounded-response failures and
private overlays on public entities. These application-level tests are NOT RUN because no API exists.

## UX and implementation dependencies

IMP-MATCH-05 waits for accepted DM07 architecture and the appropriate reviewed scorer/input gates.
IMP-MATCH-06 waits for explicit stack/auth approval and those API contracts. IMP-MATCH-07 measures
the accepted implementation using permissioned eligible data, meaningful relevance fixtures and
isolated performance/security tests; synthetic arithmetic is not relevance or capacity evidence.

Mode A should show method/version, covered and missing layers, fit separate from confidence and
direct evidence, and clear unavailable reasons without existence leaks. B1 should distinguish
required/excluded/optional notes and exact/any layer, reject contradictory selections, and say
that missing data cannot prove absence. B2 remains disabled with a data-unavailable explanation.
Use neutral placeholders for all unlicensed/unsupported images. No anonymous sharing/search of the
operator-private Scento catalogue, checkout, AI API, framework installation or cloud deployment.

Next: Owner records individual DM choices and a bounded application/session proposal; then review
the adapter's remaining authentication/provenance gaps before any real-data matching activation.
