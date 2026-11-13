---
id: DPT-MATCH-SESSION-PUBLICATION
project: DoomParfum By TK
type: architecture_proposal
status: proposed
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, authentication, rls, privacy, application]
source_of_truth: "../../README.md"
---

# Nonadmin session, application stack and publication proposal

Status: PROPOSED, no Owner implementation/ownership/stack/publication approval recorded. This
document creates no login, grant, binding, schema, dataset, cloud resource or public endpoint.
See [[Matching_Owner_Decision_Register]] DM07 and [[Post_PR4_Application_Readiness]].

## Actual identity constraints

Migration005 principal_id resolves dpt.users.auth_subject from genuine PostgreSQL session_user.
That subject is immutable. Access-scope kind and owner are also immutable. Membership reads apply
to shared scopes only; inserting a member cannot share a user_private scope. A SET ROLE/GUC/header
claim is not a genuine authenticated login. All1479pilot profiles are operator-private and currently
have zero approved genuine nonadmin owner-session bindings. The adapter must reject an administrator
binding, not manufacture a usable owner by adding dpt_owner/curator membership or rewriting history.

Never change the existing auth_subject, downgrade the PostgreSQL administrator role, change source/
entity scope ownership, disable immutable guards, use SET SESSION AUTHORIZATION through a superuser
transport, or add a public/private bypass. These are not remedies within this adapter PR.

## Binding alternatives requiring explicit Owner choice

| Option | Proposal | Approval and implementation boundary |
|---|---|---|
| Recommended bounded pilot | Create a separate clean disposable application-private pilot after approval. Establish stable genuine nonadmin principal/immutable subject and private scope at intake, then perform a reviewed controlled import of the same licensed pinned data with complete new-scope provenance | separate approved task and importer/session contract; verify local rights and all SQL/RLS/replay/rollback tests; never silently copy or reassign existing pilot rows |
| Authentication-model amendment | Design a revocable audited server-side login-to-principal binding contract, with tight RLS/SECURITY DEFINER/search_path/grant controls and exact caller identity | Planning Amendment and new implementation migration/tests; preserve original eight migrations; no caller-editable identity or automatic privilege expansion |
| Defer application access | Keep operator catalogue private and exercise the adapter only with synthetic genuine sessions | current safe state; no real app capability or public catalogue claim |

No option is accepted here. New source capture/assessment/selection records must retain accurate
actor, scope, revision, hashes and source license. Existing operator observations/receipts remain
unchanged; source rights are reviewed for the chosen scope, not inherited through a public entity.

For a bounded genuine-session pilot, recommend LOGIN/NOSUPERUSER/NOBYPASSRLS/NOINHERIT with only
explicitly reviewed runtime capabilities, no owner/writer/curator/admin memberships and no CREATE
or role-management powers. Validate the exact inherited/effective privileges rather than trusting
role names. NOINHERIT and role provisioning details need actual compatibility tests; do not issue
GRANT statements from this proposal. If the existing runtime model needs INHERIT, approve and test
that narrow alternative instead. The adapter still requires session_user=current_user and a
fresh read-only transaction; one request must not carry another principal's connection or snapshot.

Public provenance currently requires curatorial policy under existing RLS. Do not give every app
login curator membership to hide that gap. A least-privilege selected-provenance/public DTO contract
requires separate security review; inaccessible fields remain unknown until then.

## Application-stack and authorization decision

Existing runtime is Python database tooling plus PostgreSQL, not an installed web application.
Recommended next step is framework-neutral transport/API contract approval before UI dependencies.
Owner alternatives: reviewed local Python service reusing the reference concepts; TypeScript/SQL
service with a reviewed ORM; continued local CLI only. Next.js/Drizzle/auth vendors are proposals,
not installed or accepted services. Cloud/provider/storage/login/secret handling requires a separate
bounded approval. No AI API, embeddings or paid AI service is needed for deterministic matching.

An API's authenticated application identity must bind to the approved database authorization model
before lookup, candidate counts, pagination, scoring or cache access. Reject cross-user connection
reuse, identity headers, forged cursors and role escalation. Errors must not distinguish guessed
private IDs from missing IDs. Internal selected provenance is not a public serialization format.

## Publication and cache boundary

Default proposal: authenticated local-private ephemeral results, no shared cache or durable query
history. Catalogue entity visibility does not publish a private source, retail listing, image or
collection entry. Public sharing/search remains disabled until each selected field and asset has
active explicit redistribution/display/storage/automation and any required cache/derivative rights,
plus a reviewed public projection. CC BY metadata attribution does not authorize unrelated images.

If later approved, cache/cursors must bind caller, scope and membership/rights/review revisions,
dataset/method/version, filters and ordering. Reauthorize before every hit/page and invalidate on
revocation/expiry. No private counts or explanation fragments in anonymous errors or caches.
Unsupported/unlicensed images remain placeholders. The Cart remains a personal bookmark, never
checkout/order placement or automatic Shopee synchronization.

## Required implementation acceptance before real app access

Test genuine owner/other-user/shared/revoked-member/anonymous/admin/BYPASSRLS/role-change sessions;
expired/revoked source rights; public identity with private overlay; reused transaction/snapshot;
connection-pool principal isolation; future and stale permission times; typed bounded malformed
responses; no raw staging/count/error/cache/publication leaks; full rollback/replay and unchanged
operator pilot hashes. These application-level tests are specifications, not executed app evidence.
Current adapter tests do not approve a production authentication design or publication boundary.
