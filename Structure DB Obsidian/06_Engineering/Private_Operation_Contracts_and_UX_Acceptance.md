---
id: DPT-PRIVATE-OPERATION-CONTRACTS
project: DoomParfum By TK
type: planning_specification
status: proposed
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, application, operations, ux, privacy, planning]
source_of_truth: "../../README.md"
---

# Private operation contracts and UX acceptance — PROPOSED

## Baseline and incremental purpose

Planning only at `1f2f53f97dff39bc4f3094e4ad82653e8b03f52c`. GitHub readback verified Human Owner
merged PR15 at that SHA on 2026-11-13 14:59:48Z; its final head was
`cef7f5729ed2e71bf774e133f19b5975bf2d661a`. This is an architecture artifact merge, not selection
of a framework, identity route, numeric budget, publication policy, source grant or DM/OP answer.

[[Private_Application_Architecture_Plan]] already compares stacks and establishes proposed private
boundaries. This document fills operation-level gaps: validated input, authorized projection,
unknown/denial behavior, future personal writes, UI acceptance and testable API/UI task boundaries.
It defines logical contracts, **not HTTP routes, executable schemas, SQL or an application DTO**.
All new choices remain PROPOSED. The existing adapter's engineering DTO is not promoted into a
browser/public contract. No real catalogue matching, role, database pilot, account, service, UI,
image acquisition, dependency, cloud or Production resource is created.

The coordinator owns fresh read-only catalogue verification. Historical 1,479 private profiles /
1,435 approved / 44 held / matching 0 and missing images/accords/families/pairs/listings/prices are
expectations requiring its current evidence, not new database measurements by this planning lane.
All 44 holds, independent Khamrah conflict and unapproved normalization remain unchanged.

## Existing security semantics that future operations must preserve

Actual migration005 principal mapping is `users.auth_subject = session_user::text`. It forbids
changes to authenticated subject, scope kind/private owner and row ownership/identity. Membership
permits shared-scope access only; it cannot share an existing user_private scope. A single genuine
service login resolves to one database principal, not an arbitrary browser user.

The reference adapter requests READ COMMITTED READ ONLY, rejects incompatible isolation, role
changes, owner/superuser/BYPASSRLS sessions and checks genuine runtime membership. Forced RLS and
the selected-claim/source-permission predicates remain applicable. Neither this contract nor a
private loopback listener authorizes administrator fetch-and-filter, headers/client role IDs/GUC
identity claims, SET SESSION AUTHORIZATION impersonation or broad curator/writer grants.

OP05 still needs an explicit choice: a separately approved clean application-private intake/pilot,
an accepted authentication-model amendment with independent security tests, or deferral. Do not
rewrite the operator pilot's immutable subject/scope to serve an application. Ordinary runtime
provenance restrictions are a capability boundary, not a reason to broaden privileges. A future
driver, pool and browser authentication route must prove actual effective privileges and identity.

### Common authorization sequence — proposed contract

1. Bound transport input and parse its fixed grammar without catalogue access. Authentication may
   fail before any private lookup. Public syntax checks must not consult ID existence or vocabularies.
2. Establish an approved trusted identity/session outside client-controlled operation fields. Derive
   permitted scope, never accept a client-selected owner or scope override.
3. In a fresh bounded transaction, apply RLS, entity visibility, selected observation/materialization,
   conflict/hold status and operation-specific active source rights **before** field retrieval,
   existence-dependent messages, candidate counts, score/explanations, private provenance or media bytes.
4. For scoring, additionally require accepted normalization/domain closure, explicit eligibility,
   method/version and its approved policy. A profile's approved status or matching boolean alone
   cannot substitute for these gates.
5. Produce only the permitted display projection. Recheck any independently selected media or
   private listing/collection association. Public perfume visibility never publishes its private overlay.

Reading for local computation, displaying a fact, caching it and redistributing it are different
operations. Check each actual use against applicable active assessments. If mandatory attribution,
license/change notices or provenance cannot be displayed lawfully, withhold the affected display.
Do not infer display/public rights from the pinned dataset's local pilot approval or a linked URL.

## Logical read operations

Every row below is a proposed operation, not an implemented endpoint. Request identity is supplied
by approved transport, not by these payloads. Output IDs are opaque authorized application references;
their relationship to database IDs requires a reviewed projection decision. Never serialize raw
source records, private actor IDs, SQL, capture payloads, filesystem paths or source-restricted URLs.

| Operation | Input and validation | Authorized output | Refusal/unknown behavior |
|---|---|---|---|
| O01 Catalogue browse/name search | bounded text; canonical brand/edition filters; explicit sort/version and optional opaque cursor; no raw SQL/regex/URL | bounded authorized page: opaque perfume reference, permitted name/brand/edition label and safe availability badges; no private totals | global unsupported filter is rejected as unsupported; unavailable private candidates do not contribute to counts, suggestions or hints |
| O02 Perfume detail | one well-formed opaque perfume reference; no requested owner/scope | allowlisted permitted identity fields, declared layer/general-note states, source-use compliant attribution and media placeholder | missing and inaccessible reference share one unavailable result; no disclosure of a hidden profile's held/rights state |
| O03 Note vocabulary/presence filter | reviewed canonical note reference; explicit top/heart/base/general or accepted any-layer domain; permitted brand/text filters | only authorized vocabulary and positive reviewed membership matches, with field coverage limitations | alias ambiguity is a request problem without silent alias merging; general notes are not assigned to a pyramid layer; absent from incomplete data is unknown |
| O04 Note query search, B1 | reviewed required/optional/excluded clauses with explicit domains, accepted method/config version | query fit separate from coverage, Data Confidence and pair evidence; candidate explanations limited to authorized claims | reject contradictions before evaluation; strict required/excluded conditions cannot pass from unknown membership or unknown closure; B1 stays unavailable before its policy/full implementation/data gates |
| O05 Side-by-side structural view | two separately authorized references, explicit requested layers; scoring requested separately | permitted positive note overlaps plus explicit unavailable/incomplete fields; optional independent evidence section when lawful | side-by-side facts do not imply a score or proven absence; both sides must authorize; do not return the accessible half when the other reference is inaccessible |
| O06 Mode A structural comparison/ranking | reference, accepted method/version, permitted filters, cursor | structural fit, coverage, Data Confidence and direct evidence as separate named fields, exact method then approved display rounding | generic primitives do not enable this operation; no inferred accord strengths, zero-filled missing components or unnamed notes-only fallback |
| O07 Availability/capabilities | fixed capability request or an already authorized profile context | global supported/not-yet-implemented methods; authorized per-field unknown/partial/usable states | global capabilities must be caller-independent product facts; no per-ID privilege/rights/held discovery probe |
| O08 Private lists, saved sources, purchases, inventory reads | approved current principal; optional authorized list/reference/cursor and exact supported filters | only caller-owned approved private projections; individually permitted source URLs/price observations and manual statuses | deny cross-user source/list/link/count access even for a public perfume; unknown date/price/ownership stays unknown, never zero or inferred purchase |

Brand/country/edition/family/accord/price filters require actual selected, compatible, permissioned
fields. Unsupported catalogue dimensions must be explicitly unavailable rather than empty result
sets pretending complete coverage. Raw country/family strings are not reviewed regional-market or
canonical family coverage. A future budget filter must specify currency, market, observed-at and
shipping assumptions under a separate accepted price policy; the confirmed adjustable ฿2,000 product
budget requirement is not a permission to invent current seller prices or exchange rates.

O03 positive presence browsing is distinct from B1 ranking and strict absence. Accepted note-list
closure must state source revision, field/layer, normalization version, reviewer and use scope.
Complete-as-reported never means a chemical formula or measured smell absence. Repeated occurrences
are not intensity; top/base memberships remain distinct. Do not apply the 43 proposed transforms or
resolve Khamrah for any operation until its separate policy/claim/rights review passes.

## Synthetic interaction examples — not adapter DTOs or executable fixtures

All references, labels and values in these examples are invented. They do not refer to real perfumes,
database users or catalogue IDs. A future accepted serializer may use different names. No source
fact or engineering DTO is implicitly approved for publication by showing these examples.

An authorized O02 request might use:

```json
{"operation":"detail","perfume_ref":"00000000-0000-0000-0000-000000000001"}
```

An authorized, rights-permitted illustrative projection could be:

```json
{
  "state":"available",
  "perfume_ref":"00000000-0000-0000-0000-000000000001",
  "display_name":"SYNTHETIC Example",
  "layers":{
    "top":{"state":"reported_incomplete","notes":["SYNTHETIC NOTE-A"]},
    "heart":{"state":"unknown","notes":null},
    "base":{"state":"unknown","notes":null}
  },
  "media":{"state":"placeholder"},
  "matching":{"state":"unavailable","structural_fit":null},
  "attribution":[{"label":"SYNTHETIC permitted credit"}]
}
```

Unknown arrays are null, not an empty asserted-complete domain. A known usable empty list could only
be represented after accepted closure defines that state. No score value is shown as zero. An
inaccessible and a missing reference both produce the same fixed shape, for example:

```json
{"state":"unavailable","message":"Item unavailable"}
```

Do not echo inaccessible IDs, hidden row counts, source identity, actor, SQL, field locators, rights
reason, timing diagnostics or private URLs in this response. Ordinary authentication failure can
request sign-in, but must not reveal ID existence. Same body shape is necessary, not proof of timing
noninterference; future testing must also examine status codes, sizes, timing classes, logs and
cache/cursor behavior. Resource-bound and syntax errors must remain independent of private data.

An illustrative B1 request (still unavailable before approvals) may be:

```json
{
  "operation":"note_query",
  "method_version":"SYNTHETIC-unaccepted-v0",
  "clauses":[
    {"note_ref":"00000000-0000-0000-0000-000000000010","layer":"top","rule":"required"},
    {"note_ref":"00000000-0000-0000-0000-000000000011","layer":"any","rule":"excluded"}
  ]
}
```

If candidate closure for the excluded domain is unknown, it cannot satisfy that strict exclusion.
Do not drop the clause, silently broaden the domain, treat unknown as absent or return a fabricated
zero fit. Both real B2 routes remain unavailable without actual reviewed compatible accord data.

## Private state: read now is still gated; writes are separate future scope

Existing migration004 already separates user_lists, user_list_items, retail_listings,
saved_buying_sources, price_observations, purchase_records and inventory_items. These table shapes
are not an implemented application or authorization to expose/write them. Lists, listings, prices,
purchases and inventory are user_private, with owner/user/scope and same-entity FK contracts.

| Future command family | Proposed business contract | Existing shape / additional gate |
|---|---|---|
| W01 Save wishlist/cart item | genuine current user chooses a permitted perfume and owned list; derive owner/scope server-side; no public list | user_lists type wishlist/cart/custom, user_list_items unique scope/list/perfume; duplicate should be disclosed only to owner; merge-versus-return-existing behavior needs an accepted policy |
| W02 Save buying source | attach an explicitly user-supplied permitted listing to an owned list item of the same perfume; keep source provenance/rights and optional private notes | listing platform/product URL/source record are required; same-user/perfume/optional variant bindings must pass; URL text is not a grant or automatic fetch instruction |
| W03 Record observed price | append an accurately dated private observation to an owned listing, not a fabricated live price | amount nonnegative with explicit currency; observed_at and source required; unknown shipping/availability stays unknown; no seller polling or currency conversion implied |
| W04 Record purchase manually | explicitly record an external order/received/cancelled/returned event; optional paid amount/currency, dates, volume and listing only as supported | purchase_records separates repeat purchases; amount needs currency, positive supplied volume and ordered/received date ordering; this never places an order or confirms payment |
| W05 Record inventory manually | owned/finished/sold/gifted/lost/archived bottle state with optional known remaining fraction/dates/purchase association | inventory_items remains separate from purchase history; changing bottle status does not erase purchase history or prove purchase; existing 0–100 remaining percentage bound must hold |
| W06 Amend/archive private records | owner-only permitted transition with bounded reason/version precondition, independently revalidated relationships | accepted transition matrix, provenance/retention/deletion rules, optimistic concurrency/idempotency design and independent rollback tests required; no physical deletion/cascade policy chosen here |

No write command above is currently implemented or authorized by this plan. A readonly session
must reject every write attempt; it must never silently upgrade to dpt_writer. Future writes need
their own approved principal route, least privileges, source-use policy, transaction boundaries,
owner transition/retention choices and separate Implementation Gate. Existing write guards serialize
cross-row invariants and require read committed; deferred contracts must still be evaluated at
transaction completion. No trigger suppression, server-time backdating or original-migration edit.

Do not accept user_id/access_scope_id/auth_subject/can_display/reviewed_at/rights flags from a client
as authority. Where a legitimate user-entered observation date is allowed, it is a domain value
distinct from server review/audit timestamps; reject invalid/future dates according to the separately
accepted field rule without rewriting evidence. Preserve unknown historical dates rather than guess.

Retry safety and lost-update prevention need a reviewed design. An idempotency key must be scoped to
the genuine user, operation and exact payload; foreign keys/unique constraints alone do not prove
request replay safety. A stale version must fail without overwriting a newer manual purchase or
inventory change. No application version column, command ledger or key store is added here; if the
accepted design needs one, obtain the required amendment/new migration approval first.

URLs remain private data. Future input review must bound/parse an allowed scheme, reject dangerous
or credential-bearing links and escape display. Saving a link must not fetch it, follow redirects,
generate an external preview, submit cookies, place orders or synchronize a marketplace cart.
Any later outbound retrieval, display/export of a link or price has its own explicit permission and
privacy review. Cart totals, financial analytics and shipping/currency assumptions remain deferred.

## Freshness, bounds, pagination and local-browser controls — all PROPOSED

Reuse the merged architecture's proposed search caps only as review targets: 8 KiB serialized query,
30 note clauses, 20 accord IDs, <=50 rows/page, 10k candidates and 5s query bound. Additional operation
targets for review: <=256 Unicode code points in a name query; <=64 KiB display response; <=2 KiB
private note or saved URL; <=8 KiB future write payload. Enforce both encoded byte and typed domain
bounds where applicable. These are **unaccepted, unmeasured proposals**, not installed defaults or
evidence that the machine can support that load. Exact response-overhead behavior needs tests.

The reference adapter's separate limits remain factual: one exact UUID, 512 note links, 64 KiB
selected payload, 8 KiB variable provenance, 2 MiB transport, 3s statement/1s lock timeout. These do
not accept a web transport, bulk search or arbitrary output. Reject over-budget requests uniformly;
never silently truncate a candidate universe then claim global best matches. Escaped labels and
attribution still count toward response bounds; oversized facts must not bypass safe serializers.

Propose no total_count and no shared cache/query history initially. Authorized lookahead alone may
support has_more after approval. A cursor must be opaque and integrity-protected, bound to the
genuine caller/scope, normalized query/sort, accepted method/policy, dataset/selection and rights/
membership/review versions. No key, TTL or signing implementation is chosen. On stale cursor,
redact details and require refresh; never disclose which private row or permission disappeared.

Each operation/page uses a fresh authorized snapshot and current reviewed local rights. Member
revocation, expiry/revocation of selected source/asset permissions, selection conflict or eligibility
change must invalidate the next read, cursor use or media delivery. Revocation committed after a
statement snapshot cannot be claimed to retroactively erase an in-flight response; bound transaction
lifetime and reauthorize subsequent operations. Do not reuse an old repeatable-read snapshot or
pool connection with another principal's identity. Remote terms changes are not automatically
known: a permitted source-update/revocation intake process remains separately gated.

No-cache means no reusable shared responses, private URLs or scores in CDN, service worker, browser
history, analytics or debug logs by default proposal; no such components are created. Future caching
requires separately accepted use/retention rights, isolation, invalidation, revocation/restore tests
and caller/scope/security/data/method version keys. A private catalogue ID is not a public cache key.
Cache-control alone cannot prevent browser history or logging; future address/query, navigation,
referrer and log design must independently exclude sensitive values and avoid incidental disclosure.

Loopback is not authentication. Before any browser connects, accept a concrete trusted-session and
host/origin policy, avoid wildcard credentialed CORS, review local-origin/DNS-rebinding and relevant
CSRF/session-fixation controls. A future write operation needs its own CSRF protection tied to that
chosen auth model; no state change through a read operation or unsolicited prefetch. Escape all
source/user strings; do not render untrusted HTML or fetch arbitrary local/network resource paths.
Read-only behavior, redacted errors and no secrets in logging must hold through failures/cancellation.

## UX acceptance journey — specifications, not a built UI

| Screen/action | Required honest behavior | Forbidden inference |
|---|---|---|
| Entry/catalogue browse | accepted identity first; show permitted catalogue entries or neutral unavailable state; explicit supported filters | localhost or public perfume identity exposes operator catalogue/private list |
| Perfume detail | selected authorized name/brand/edition plus unknown/partial labels and compliant attribution | a source-exact row means every domain/edition/currentness verified |
| Pyramid | Top / Middle(Heart) / Base and separate general notes; layer provenance/coverage where display permitted; keyboard/text equivalents | copy general notes into layers; list order/repeats imply measured intensity or chemical formula |
| Note illustration/click | safe placeholder until exact note/variant/rights/technical delivery approval; click opens only accepted positive membership search | Commons page/extension proves usable bytes; a note image is a product bottle image |
| Side-by-side | aligned available layers, positive overlaps and explicit incomplete/unknown states | unknown opposing membership highlighted as confirmed difference or absence |
| Matching panel | unavailable score displayed as unavailable/null; structural fit, confidence, evidence and coverage independent | null rendered as 0%, scientifically measured smell similarity or a real B2 slider |
| Wishlist/My Cart | owner-only saved perfumes and permitted buying-source bookmarks; save/read/write gates clearly explained | checkout, payment, order placement, Shopee cart/account synchronization |
| Purchased/Owned | manual external purchase and separate bottle state; repeats/history retained; unknown optional facts explicit | changing cart state proves payment/ownership, inventory archiving erases purchase history |
| Collection dashboard | only own authorized data with honest denominators and stale/partial flags; later accepted aggregates | inaccessible/private-other-user counts, invented price/stock/date or current market totals |

Unapproved controls should be visibly unavailable with a plain product reason, not a misleading
working button, fake score or technical SQL stack trace. This does not select layout, frontend
framework or publish a screenshot containing private data. Accessibility/text alternatives and
empty/unknown/error states require the eventual UI's independent implementation tests.

## Evidence-based stack recommendation without selection

The existing tracked Python/PostgreSQL adapter, primitives and test harness make a **local Python
read-only transport proof the recommended next implementation candidate after OP05/OP06 approval**.
This narrows parity work; it does not mean a Python web service, framework/driver lifecycle, browser
identity or deployment already exists. Current tracked inventory has no JS/TS app or dependency
manifest. No package compatibility, capacity, vendor cost or maintenance SLA was measured here.

TypeScript remains a viable Owner alternative if shared browser types justify porting and testing
exact UUID/time/unknown/bounds/session/transaction semantics against the Python reference. Continued
CLI-only work remains the conservative alternative while identity/rights/policy approvals are absent.
All three still require maintenance, real auth/driver error handling, least-privilege connection
management, security tests and a separately approved deployment boundary. Reuse the merged stack
comparison rather than invent a second stack decision table. No framework, ORM, auth vendor,
dependency, cloud provider or credential is selected or installed by this recommendation.

## Separate future task boundaries and acceptance matrix

| Proposed task boundary | Prerequisite evidence | Completion evidence before Human review |
|---|---|---|
| Identity/transport amendment or proof | explicit OP05/OP06 route/version/scope; Planning Amendment if material; approved isolated target | genuine login/effective privilege/isolation/pooling/adversarial tests; no operator-scope rewrite |
| Read API contract implementation | merged applicable architecture/operation plan plus exact identity/display/source/serializer/bounds decisions | TDD for O01/O02/O03/O07 and separately authorized O08 reads; independent security review; no implicit scorer or writer |
| Scorer integration | separately accepted DM/method/closure/normalization/selected-rights/eligibility and full Mode A/B1 implementation | synthetic golden/property tests plus separately approved real-data pilot evidence; B2 remains independently gated |
| Private read UI | accepted read API/auth/browser scope, permitted fields/media placeholders | UI authorization, keyboard/text, unknown/error/failure tests; no public publication |
| Personal writes then private write UI | explicit transition/idempotency/concurrency/retention/source-write policies and least-privilege session | separate TDD/rollback/replay/cross-user/CSRF tests and independent review before writes/UI controls |
| Publication/cache/source/media expansion | exact use permissions and dedicated accepted plan | independent security/rights/invalidation/restore tests; no inheritance from private-read acceptance |

All task names are proposals for later allocation, not new approved implementation task IDs. Owner
must record actual choices/version/scope/date/reference. If choices materially change the merged
plan, create the docs-only amendment and wait for Human Owner merge. Approval gates apply before
implementation; tests passing cannot approve policy. Current dependent API/UI/write/scorer work
remains blocked, while independent documentation/source-quality/synthetic work may continue.

| Future test | Required assertion | Current status |
|---|---|---|
| OC01 | nonexistent/inaccessible/other-user lookup yields indistinguishable private-data envelopes/status/size/timing classes with no ID/count/rights discovery | SPECIFIED, NOT RUN |
| OC02 | genuine session/effective privilege/role-change/pool cases reject admin or spoofed subject/scope before fields/provenance/bytes | SPECIFIED, NOT RUN |
| OC03 | public entity plus private source/list/price/media/collection remains private across joins, explanations, counts and logs | SPECIFIED, NOT RUN |
| OC04 | selected observation, materialization, conflict/hold and exact active use rights independently gate returned fields | SPECIFIED, NOT RUN |
| OC05 | member/source/asset revoke/expiry/selection change invalidates next operation/page; old snapshot and reused pool cannot retain access | SPECIFIED, NOT RUN |
| OC06 | malformed UUID/enum/layer/cursor, duplicate/contradictory clauses, injection/HTML and encoded byte/domain limits fail bounded and redacted | SPECIFIED, NOT RUN |
| OC07 | general/incomplete/repeated notes preserve domains/evidence; unknown closure cannot satisfy strict B1 required/excluded semantics | SPECIFIED, NOT RUN |
| OC08 | side-by-side facts do not fabricate absent notes or scores; unavailable A/B1/B2 remains null and separate from confidence/evidence | SPECIFIED, NOT RUN |
| OC09 | accepted exact ordering/ties/authorized lookahead/cursors remain deterministic; response cap never creates silent best-result truncation | SPECIFIED, NOT RUN |
| OC10 | readonly transport rejects every personal write and never escalates; cancellation/failure cleans up transaction/principal state | SPECIFIED, NOT RUN |
| OC11 | future list/source/purchase/inventory writes derive owner, enforce same-perfume/user/FKs and reject private cross-user linkage | SPECIFIED, NOT RUN |
| OC12 | future write retries/stale versions/concurrent changes have accepted idempotency/lost-update semantics and atomic rollback; deferred checks stay active | SPECIFIED, NOT RUN |
| OC13 | saved URL never fetches/previews/orders; observed versus paid prices/dates stay distinct; manual status preserves repeat purchase/bottle history | SPECIFIED, NOT RUN |
| OC14 | accepted host/origin/session/CSRF policy rejects cross-origin state changes, DNS rebinding/session fixation and injection; read methods have no side effects | SPECIFIED, NOT RUN |
| OC15 | media remains placeholder absent exact-use rights; attribution/expiry/revocation and no-cache boundaries survive failed/private delivery | SPECIFIED, NOT RUN |
| OC16 | all nine UX surfaces retain accessible text/unknown/partial/unavailable states with no checkout or publication inference | SPECIFIED, NOT RUN |

No API/UI/security/RLS/DB/driver/replay/concurrency test above has been executed in this planning
lane. [[DPT-PLAN-008_Review_Evidence]] records actual source and documentation checks only. This plan
does not alter [[Post_Merge_Owner_Decision_Packet]], [[Matching_Nonadmin_Session_and_Publication_Proposal]],
[[Matching_Data_Readiness_and_Closure_Gates]] or the coordinator's single decision form. Their
unanswered DM/OP/rights/closure/normalization/session/publication choices remain PROPOSED.
