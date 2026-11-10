---
id: DPT-ENG-003
project: DoomParfum By TK
type: security_specification
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - engineering
  - security
  - privacy
source_of_truth: "../../README.md"
---

# Security and Privacy — P1 Post-Review Proposal

## Current local SQL evidence — IMP-P1-01

PR #1 is MERGED at bffb2fab1918dc5221a6c5da7920168bcae263ca. Local migrations implement scoped
provenance/private-owner FKs, immutable scope/identity, ENABLE/FORCE RLS and non-owner runtime groups.
Local authenticated DB logins map session_user to users.auth_subject; mutable GUCs, SET ROLE and temp
search-path shadowing cannot choose another principal. Ordinary test user logins have no mutation/DDL/
TRUNCATE grants; a separate trusted writer capability is used to test WITH CHECK and membership rules.

See [[IMP-P1-01_Implementation_Evidence]] for exact commands, both actual user sessions, owner FORCE RLS,
shared reader/editor/revocation, private overlay and source/image lineage evidence. Public-source raw
staging/captures/permission evidence are service/reviewer-only. Public source/catalogue projections use
invoker behavior and column allowlists. Public matching inputs require public scope; private overlays
never materialize public fields. Matching input identity includes scope/policy/version/observation IDs.

These are DB contracts and tests, not product authentication/authorization or deployed protection.
API/JWT/error masking, search/compare/export/cache paths, signed URL/proxy/bucket access, real image
bytes/EXIF/SSRF and restore tests are NOT RUN. Local shared primitives do not activate product sharing.
Source/asset rights require human evidence; SQL validates tuples and per-use gates, not legal truth.
All unimplemented portions below remain requirements for later approved tasks.


Controls below are the approved target; local DB coverage and unimplemented boundaries are distinguished above. Repository is PUBLIC at
https://github.com/kraveerachat/DoomParfum-By-TK; application data remains private-first. Workflow already
exists in AGENTS.md and DEVELOPMENT_WORKFLOW.md; PR #1 is owner-merged; IMP-P1-01 still requires Human Merge.
Public Git never contains secrets, .env files, private exports, orders, screenshots, tokens, cookies,
private source URLs, object manifests or permission evidence with personal data. Repository visibility
must not be used as the application's privacy boundary. No GitHub settings/Actions are changed here.

## Access ownership and read/write rules

`access_scopes` defines public, shared and user_private. Scope kind/owner is immutable. Private has one
owner; shared has an owner and explicit active `scope_members` with reader/editor roles; public has no
user owner and is curator-managed. Same publisher/URL/bytes can exist in several scopes without global
source/claim/hash dedup. Shared is a proposed design extension, not a feature enabled by the local pilot.
Default pilot uses public catalogue plus separate private scopes; shared writes remain disabled until
owner approval and membership/revocation tests. Users/identity data are private, not a public directory.

| Data class | Read | Write / deletion |
|---|---|---|
| Public approved catalogue and sanitized source/attribution metadata | Public API allowlist | Curator/reviewer only; no user request can set public ownership |
| Private sources, records, observations, conflicts, overlays, assets | Exact private-scope owner only | Owner through authorized API; source versions immutable; retention/rights rules still apply |
| Shared source/claim/asset rows | Shared owner and active members only | Owner/editor for data; owner alone for membership; reader cannot mutate |
| Shopping/listings/prices/purchases/inventory and their source captures | Exact private owner only, even if catalogue target is public | Matching private scope + owner + entity FKs; history-preserving lifecycle rules |
| Raw payloads/staging and sensitive permission evidence | Authorized ETL/reviewer within assigned scope, not all readers of public source | Bounded worker/admin transaction; no anonymous/raw dump endpoint |
| Backups/object manifests/audit payloads | Separate restricted operations role; exports retain scope | Encrypted private destination, approved retention/deletion, never Git |

`access_scope_id` is NOT NULL throughout provenance/media/private records and participates in composite
FKs. Same-scope ownership is enforced through the dictionary's inherited constraints; nullable owner
columns alone are insufficient. The personal owner tuple references access_scopes(id,kind,owner_user_id)
with kind=user_private. A caller cannot supply another user's scope or create membership for itself.

## Public catalogue is not a visibility grant

A private source observation can describe a public perfume. Keep private record/claim/selection/conflict
scope unchanged. Public canonical selections accept only public observations. Private/shared overlays
can override what an authorized viewer sees, never public columns/notes/accords, public search/counts,
conflict flags, matching confidence/explanations or caches. Public exports must never contain a private
claim locator or even a private-claim count. Cache keys include scope, verified principal/membership
version where needed and policy version; membership/rights revocation invalidates caches.

For catalogue reference compatibility, target is public OR in the same scope; this is checked at write
and cannot widen child visibility. Public cannot reference shared/private sources or assets; shared cannot
reference a different shared/private scope. Normalization and promotion cannot merge private facts into
public rows. Publication requires a separate owner/curator-reviewed copy with redaction, new source/claim
IDs, public-use rights and new public selections, preserving protected originals. No automatic publication
or scope conversion is implemented/authorized in this planning PR.

## FK, RLS and authorization enforcement

Use FK/UNIQUE for scoped identity joins; deferred triggers for compatible catalogue references, active
membership/type restrictions, per-use rights and selection/materialization consistency. Do not put
cross-row reads in a SQL CHECK. RLS and FK checks solve different problems: PostgreSQL integrity checks
may bypass row filtering, so error handling must not reveal private existence.

Future runtime roles: non-owner, non-superuser, no BYPASSRLS, least-privilege grants. Enable RLS on scoped,
identity and personal tables; default-deny without a policy; test FORCE RLS for owner roles where needed.
SELECT filters scope AND data class; use sanitized projections and column grants for sensitive evidence/locators because RLS does not hide individual columns. No anonymous full-row access to source/rights/permission tables. INSERT/UPDATE WITH CHECK enforces authorized scope, immutability
and referenced-row access; DELETE requires writer privilege and history/retention rules. Guard against
permissive policies combining with OR to widen access. Table-owner/service-role tests alone are invalid
proof of end-user isolation. Isolate migration/backup credentials; workers have explicit allowed scopes.

The server derives principal via verified auth_subject→users mapping and checks requested scope against
ownership/active membership. Never trust arbitrary client-supplied user_id, scope headers or editable
session variables. Recheck referenced record/asset authorization before writes and signing; return a
uniform not-found/denied response for inaccessible IDs rather than exposing FK/unique error details.
Untrusted clients have no arbitrary SQL or unrestricted table writes, membership administration or
service-role endpoint. Rate-limit lookup/mutation attempts. Audits retain scoped/redacted failures.

Views, RPCs, exports, search and workers must preserve RLS; use invoker behavior where supported or
explicit bounded authorization, fixed search paths and reviewed execution grants. No generic SECURITY
DEFINER helper/query can accept arbitrary scope IDs and return rows. Verify actual PostgreSQL/provider
role/view behavior in the future pilot; do not assume library/service credentials preserve RLS.

Primary technical basis: [PostgreSQL RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html),
[constraints](https://www.postgresql.org/docs/current/ddl-constraints.html). No migration or policy SQL
is created here; corresponding future tests are in [[P1_Pilot_Implementation_Plan]].

## Images and object boundary

Image rights do not grant application access and access membership does not grant copyright reuse.
`image_assets` → source_record → source and rights assessment must match by scoped composite FKs.
A selected `asset_permissions` binding additionally matches the exact image ID/capture/assessment;
source-level consent alone cannot authorize another image. Validate locator/hash/evidence, allowed use,
expiry/revocation, parent transformation grant, derivative output license and attribution on acquisition,
transform, display and restore. Unknown rights blocks that operation. Details: [[Rights_and_Attribution]].

Private buckets, non-guessable scoped object keys and separate server authorization are required.
For private/shared assets use an authenticated proxy that rechecks access/rights per request, including
range/thumbnail/original and cached delivery. Upstream short-lived signed URLs remain internal; do not
expose permanent bearer links or cache private bytes publicly. This allows membership revocation to
stop later requests; requests already in flight cannot be recalled. Public-approved assets may use
public delivery only after explicit rights and publication review. Do not infer access from a public
perfume_images link or deduplicate across tenants by hash. Test direct bucket access and URL replay.

## Other security controls and limits

No Shopee cookies, cart synchronization or checkout. No private exports/orders sent to AI providers
without specific authorization. Admin/ETL endpoints require authenticated scoped authorization, not
merely a global shared API key. Secrets stay outside Git/browser bundles, examples use placeholders.
External URLs require approved HTTPS host/size/MIME bounds, redirect/SSRF checks, sanitized metadata
and private EXIF removal for future derivatives. Outbound links use noopener/noreferrer and remove
known private/tracking tokens without blindly breaking product identifiers. Backup rights/scope and
restore tests follow [[P1_Storage_Hosting_and_Recovery]]. API/storage/byte/restore controls remain NOT RUN; current local DB evidence is recorded above.
