---
id: DPT-DOC-003-FIELD-APP-UNLOCK
project: DoomParfum By TK
type: implementation_gate_delta
status: proposed-review-pending
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, completeness, normalization, private-application, gates]
source_of_truth: "../../README.md"
---

# Field readiness, normalization queue and private application gates

## Current boundary and evidence provenance

This is a review checkpoint on existing Draft PR25, not a new generic plan or an implementation
unlock. Verified merged main remains `8c6a8376680c7a10cc3eb4b5cf80afe4376a9282`. PR22–25 remain
OPEN/DRAFT. The current Master Prompt explicitly requires exact Owner acceptance before dependent
implementation. Conservative direction is confirmed; no exact DM/OP, normalization, source-use,
session or stack answer is inferred. The coordinator records the one consolidated decision batch.

Merged [[Private_Application_Architecture_Plan]],
[[Private_Operation_Contracts_and_UX_Acceptance]] and
[[Normalization_Closure_and_Materialization_Transition]] remain the applicable proposed contracts.
The quantitative source below is **unmerged PR23 candidate evidence**, reviewed at exact head
`50adb60f487690510c8f4e189f5e072698845198`; source/media context is unmerged PR24 at
`8c04fcdc9384955d2e49eefcd9f54c1ebd462378`. Their independent reviews support bounded evidence
assessment, not a new permission, accepted transformation or runtime dependency on an unmerged PR.

The last observed PostgreSQL audit, **T0**, is 2026-11-13T20:04:07Z–20:04:20Z, or
2026-11-14 03:04 Bangkok. Public aggregate SHA-256:
`3480c8da292ee633b28bad6e4955b0890b175cbc392b13782fd2b0682ca6d09d`.
At T0 all49 table/data/security/application-role fingerprints matched before/after and the prior
baseline. This lane consumed that report and made **zero database/network calls**.

The coordinator's new read-only Docker status attempt failed because the
`dockerDesktopLinuxEngine` named pipe was absent. **Current DB count, rights-time and application-role
revalidation: BLOCKED / NOT RUN. Current live counts are UNKNOWN.** No service was started or
restarted. No T0 value below is reported as a new live observation or assumed unchanged.

## Twenty-four-field completeness and impact checklist

All numeric values in this table are **HISTORICAL T0 observations** or their explicitly identified
frozen source-file cohort. The pinned Scento revision is
`086769ecf1add770ea6646bd4d88d39f0e7cddeb`; file counts are1,479 perfumes/160 houses/420 materials.

- **Raw available** means a populated source cell, not a canonical, reviewed, permitted or complete fact.
- **Canonical populated/gap** uses the row's denominator. A missing field is unknown, not proven absence.
- **Selected/reviewed** is the measured approved selection population; approved profile status alone
  does not approve every field or make it matching-eligible.
- **Rights-usable** below is only measured existing local-use evidence at T0. It is not a current
  expiry/revocation check or an application, image, publication, derivative or redistribution grant.
- **Application-accessible H0** means no approved real-catalogue nonadmin application binding at T0.
  Current application contracts still lack an approved binding choice;current SQL/role state is not rechecked.
- **Complete-as-reported NE** means no accepted exact capture/edition/layer/domain assertion is
  established. It is not a count of rows in an implemented closure table. Populated lists are not closure.
- Impacts identify the unavailable field/component. They do not require an otherwise authorized
  partial detail page to invent a value or hide all known fields. All real application operations
  independently remain blocked by session/authorization and exact operation gates.

Impact keys: **S** search/filter for that field; **D** detail field; **P** pyramid presentation;
**A** real Mode A selected component/identity; **B1** real note-query behavior;
**B2** real accord-profile matching; **UX** private application presentation/authorization.

| # / field and denominator | Raw available | Canonical populated / exact gap at T0 | Selected / reviewed at T0 | Rights-usable evidence | Application-accessible | Complete-as-reported | Unknown / blocked impact |
|---|---|---|---|---|---|---|---|
| 01 Perfume name /1,479 |1,479|1,479 /0|1,435 selected;44held|1,435 selected passed measured local-use checks|H0;current not revalidated|NE for identity/edition equivalence|44 lack approved selected names;S/D/UX require permitted projection |
| 02 Brand name /160 |160|160 /0|160 selected|160 measured selected local-use values|H0;current not revalidated|NE for cross-source identity|No name-slot gap;brand verification/aliases and UX authorization remain separate |
| 03 Edition/flanker /1,479 coverage |No dedicated raw columns|Edition labels0 /1,479;directed flanker_of modeled with0rows /1,479 linked-profile gaps|0 recorded facts|0 usable selected facts|H0;current not revalidated|NE|S/D/A identity/edition filters unavailable;do not infer flanker from name/shared notes |
| 04 Concentration /1,479 |1,228|1,228 /251|1,188 selected;40held populated;291 without approved selection|1,188 measured selected local-use values|H0;current not revalidated|NE|251 raw/canonical gaps;S/D/A compatibility must retain unknown and EDT/EDP distinctions |
| 05 Release year /1,479 |80|80 /1,399|76 selected;4held populated;1,403 without approved selection|76 measured selected local-use values|H0;current not revalidated|NE|S/D optional year unavailable for1,399;year never proves lifecycle/stock |
| 06 Gender/intended audience /1,479 |No dedicated supported column|0 /1,479|0|0 usable selected facts|H0;current not revalidated|NE|S/D/UX field unsupported;no inference from name,brand or notes |
| 07 Top notes /1,479 |1,388 source profiles|1,348 /131|1,348 profiles;3,693 links|1,348 measured selected local-use profiles|H0;current not revalidated|NE|P missing131;S/A/B1 need accepted domains/selected-use rules;absence unknown |
| 08 Middle/Heart notes /1,479 |1,388|1,348 /131|1,348 profiles;3,742 links|1,348 measured selected local-use profiles|H0;current not revalidated|NE|P missing131;S/A/B1 domains/closure unresolved |
| 09 Base notes /1,479 |1,388|1,348 /131|1,348 profiles;4,150 links|1,348 measured selected local-use profiles|H0;current not revalidated|NE|P missing131;S/A/B1 domains/closure unresolved |
| 10 General notes /1,479 |91 flat-only;all1,479 also contain flattened source strings|87 /1,392|87 profiles;387 links|87 measured selected local-use profiles|H0;current not revalidated|NE|D/S/B1 need explicit general domain;do not assign general notes to Top/Heart/Base |
| 11 Note aliases /420 note entities |327 source records;1,635 tokens/1,626 literal-distinct/9repeats|0 canonical alias rows;420 entities without aliases|0 selected aliases|0 usable canonical aliases|H0;current not revalidated|NE|S/B1 alias resolution unavailable;literal audit predicate is not accepted semantic normalization |
| 12 Note descriptions /420 |420 smell strings;not an accepted description mapping|0 /420|0 selected descriptions|0 usable selected descriptions|H0;current not revalidated|NE|D/UX descriptions missing;source smell/material-family/origin remain distinct fields |
| 13 Main accords /1,479 |No compatible structured accord/strength field|0 entities/links/values;1,479 profile gaps|0|0 usable selected accords|H0;current not revalidated|NE|A full-component/B2 blocked;no strength from names,order,repetition or prose |
| 14 Perfume families /1,479 |1,479 primary/1,075 secondary;404 raw secondary gaps|0 associations;1,479 canonical gaps|0|0 usable selected families|H0;current not revalidated|NE|S/A family component unsupported until taxonomy/mapping/use review |
| 15 Brand country /160 |158 publisher country claims;2raw gaps;17labels|0 country_code /160|0 selected country_code|0 usable canonical country codes|H0;current not revalidated|NE|S/D regional-origin field unavailable;origin is not sales-market coverage |
| 16 Source provenance /2,059 source records |Locators/revisions2,059;1,479 distinct perfume captures|2,059 source records;10,489 observations;8,845 selections are separate units|Not one blanket profile/field approval|2,059 bound to existing local assessments at T0;current expiry/use not rechecked|H0;internal provenance not browser DTO|NE for factual completeness|D/UX safe attribution projection required;never expose private source/actor/capture details |
| 17 Bottle images /1,479 profiles |5 identity leads,not acquired assets|0 links/assets;1,479 gaps|0 asset permissions|0 verified usable assets/grants|H0;current not revalidated|NE|D/UX use placeholders;new acquisition/display/derivative scope blocked |
| 18 Note illustrations /420 notes |15 historical research leads;3 page bindings|0 links/assets;420 gaps|0 asset permissions|0 verified usable assets/grants|H0;current not revalidated|NE|D/P/UX placeholders;page identity not binary/license/chemical identity proof |
| 19 Similarity/pair evidence /1,479 coverage |5 unpromoted evidence leads|0 comparison_evidence/relations;1,479 profile-coverage gaps|0 reviewed canonical pairs|0 usable canonical pair evidence|H0;current not revalidated|NE|D/A explanation evidence unavailable;never blend a lead/rating into Structural Fit |
| 20 Purchase-source references /1,479 coverage |No licensed pinned listing field|0 retail_listings;1,479 coverage gaps|0|0 usable selected listing facts|H0;current not revalidated|NE|S/D/UX saved-source/listing surfaces need separate private scope;not checkout/account automation |
| 21 Price observations /1,479 coverage |No pinned price field|0 prices;1,479 coverage gaps|0|0 usable selected price facts|H0;current not revalidated|NE|S/D/UX price/budget filters unsupported;unknown is not0;currency/market/time need accepted contract |
| 22 Regional coverage /220 seed;160 source houses |12 seed-region labels;158 source country claims;15Thai A priorities|Regional-market model/total not established;canonical country codes0|0 regional identity/market approvals by audit|All220 seed source-rights states permission_pending in that registry|H0;current not revalidated|NE;global/regional product universe UNKNOWN|S/UX regional completeness cannot be claimed;226candidates ≠160canonical brands |
| 23 SKU/edition coverage /1,479 profile coverage;0 variants |No dedicated raw SKU/GTIN/size columns|0 variants;1,479 profiles without variant association;SKU denominator UNKNOWN|0|0 usable variant facts|H0;current not revalidated|NE|S/D/A edition/packaging filters unavailable;per-SKU missing percentage is inapplicable |
| 24 Field-level permissions /per selected field,use,scope |1source/1current-at-T0 assessment;not an image or public grant|2,059 source records assessed locally;asset_permissions0|8,845 selections,not8,845independent grants|Only field-specific measured local counts above;new app/media/public uses unaccepted|H0;current not revalidated|NE;rights do not establish factual closure|All real S/D/P/A/B1/B2/UX operations recheck exact active use/scope/selection/conflicts at execution |

The selected representations account for1,435 profiles:1,348 layered plus87 general. The raw1,388
layered/91flat-only shapes are a different population. Canonical11,972 links equal3,693+3,742+4,150+
387; the raw12,448 occurrences include476 on44held profiles. Layer-profile rows overlap and must
not be added as distinct perfume totals. No table above proves complete-empty domains or smell absence.

## Missing fields and prioritized feature gates

| Priority / affected feature | Exact observed gap and safe next step | Gate before runtime/data change |
|---|---|---|
| P0 All private search/detail/pyramid/UX | Approved genuine nonadmin binding absent;live DB/role revalidation unavailable | OP05/OP06/APP-01 route/version;isolated genuine-session security tests;no operator fetch/filter |
| P0 Real A/B1 | Matching eligible0atT0;exact methods/closure/normalization/use unresolved | DM/OP method acceptance plus selected source/use,identity,conflict and relevance/security gates;flag alone insufficient |
| P0 Hold/normalization work |43projection proposals and independent Khamrah remain unresolved | OP03 separately from OP02closure/OP04selection/OP05app;no automatic hold release |
| P1 Partial detail/search fields | Raw description1,479/canonical0;raw country158/canonical0;raw families1,479+1,075/canonical0 | Accepted field mapping/taxonomy/source-use task;show unknown for unavailable fields |
| P1 Pyramid/query domains | Each131layer gaps;1,392withoutgeneral membership;no accepted closure | Preserve representation;review exact domains;do not manufacture missing layers or negative matches |
| P1 Vocabulary/UX |420Thai-name/alias/description/image target gaps | Reviewed language/alias/material mapping and exact image grant;no translation/chemical assertion by inference |
| P1 Media detail/pyramid |1,479bottle/420note-image gaps atT0 | Placeholders now;exact asset,creator,license,use,format and derivative task before intake |
| P1 Regional priorities |15Thai A entries preserved;14lack the audit's literal suggestion | Permissioned brand/edition evidence;literal matching does not verify origin or merge identities |
| P2 Exact edition/filtering |251concentration gaps/1,399year gaps/1,479edition gaps;flanker_of modeled-empty | Exact-edition/source evidence and reviewed identity;no name/shared-note duplicate inference |
| P2 B2/full A components |Canonical accords/families0;no compatible observed strength scale | DM04 taxonomy/scale/domain plus reviewed compatible observations;real B2 remains disabled |
| P2 Shopping/reference UX |Listings/prices0;live market denominator unknown | Separate source/price/manual bookmark read/write scopes;no invented stock/price or external account automation |

Missing optional detail/media fields can support honest unavailable labels or placeholders once
authorization and the relevant read contract are approved. They do not justify false zero scores,
invented fields, unsupported search filters or silently redistributing a full Mode A component weight.

## Normalization and44-hold resolution queue — proposed review contract

Review-manifest proposal **NQ-REVIEW-1** is a proposed checklist/version label, not an installed
transform, accepted policy or new database record. Reuse the existing43sidecars and original hashes;
do not rename or overwrite their historical transform identities. Exact accepted transform/version
must be recorded by Owner/reviewer in OP03 before a bounded implementation task starts.

| Review population / unit | Evidence state | Accepted / rejected / deferred decisions actually recorded | Unknown / blocked action |
|---|---|---|---|
|39layered repeated-membership profiles|Existing projection PROPOSED;all source arrays/ordinals retained|0accepted,0rejected,0explicitly deferred|39await exact policy and authorized reviewer;no within-layer collapse applied |
|4general repeated-membership profiles|Existing projection PROPOSED;general domain retained|0accepted,0rejected,0explicitly deferred|4await same separately accepted projection scope;never assign pyramid layers |
|Combined43proposals|44repeated groups/45extra occurrences;0transforms applied|0accepted,0rejected,0explicitly deferred|43unanswered proposals;blocking/dependency is not an Owner Defer answer |
|Khamrah /1held profile|Structured/prose contradiction,not a duplicate-only transform|No resolution accepted;do not count as a rejected/deferred projection|Independent exact-edition,section/field claims and permitted review evidence required;no newest/majority shortcut |
|All44held profiles|476raw occurrences retained;no hold release/eligibility change|0hold releases by these review artifacts|All remain held;current DB hold count itself is not revalidated in this unavailable environment |
|Material aliases /327raw records|1,635tokens/1,626literal-distinct/9repeats;canonical aliases0|No semantic alias transform accepted by this audit|Token duplicates are not the45perfume extras;unknown semantic equivalence needs its own review |
|Brand identity/aliases /226candidates|92literal suggestions/134none;68of160houses unsuggested|0identity approvals/merges by audit|Keep220seed and6discoveries separate;do not promote literal aliases or merge based on shared notes |

Reviewer acceptance must preserve source/capture/revision/hash,each token ordinal,layer/domain,
section/field locator,edition certainty,vocabulary and proposed transform identity. A future new
derived membership may reference multiple same-layer occurrences only under an accepted projection;
Top and Base occurrences remain distinct. Preserve every original immutable observation. Reject
foreign lineage,ambiguous aliases,mixed editions,source conflicts or missing active use rights.

Membership projection, closure, canonical selection/materialization, hold resolution and matching
eligibility are independent decisions. A projection success cannot set the other states. Do not
derive intensity or duplicate perfume identity from repeated/shared notes. Database conflict rows0
atT0 do not resolve externally recorded Khamrah claims. Unknown/rejected/deferred outcomes retain
their evidence and never become silent canonical deletion or a false complete-empty domain.

The existing NC01–NC15 transition tests remain **SPECIFIED, NOT RUN**:source-ordinal/cross-layer
retention,ambiguous aliases/editions,independent Khamrah,rights/scope/reviewer rejection,stale-review
and concurrent decision controls,derived-claim/selection/materialization consistency,idempotent
replay,rollback/compensating history and revocation-safe restore. This document adds no SQL/runtime
or closure table and claims no new test pass. Reviewer assignment/Owner answers remain unrecorded.

## Private application implementation gate delta

Do not duplicate the merged stack/operation plans. Their relative tradeoffs still apply to the
current source:Python reference adapter/math/test tooling exist;no selected web framework,driver,
browser auth provider,TypeScript app,ORM or application dependency manifest is established here.
Node used by agent tooling is not a selected application stack. Recommendation while exact choices
remain unanswered: **continue existing CLI/reference preparation**. This is a recommendation,not
an Owner selection or authorization to build a new catalogue-reading CLI bridge. After OP05/06,
the merged plan recommends a bounded Python read-only transport proof to reduce parity work.

| Surface | Existing CLI/reference continuation | Local Python service candidate | Local TypeScript service alternative |
|---|---|---|---|
| Code reuse/dependencies |Uses existing local tooling;no new service dependency |Can reuse reference types/SQL semantics after real driver/transport review;framework unselected |Requires driver/toolchain and reference-behavior parity port;no existing TS service is claimed |
| Authentication/session/RLS |No new genuine application principal is created |Same immutable subject/scope rules;approved principal and effective privilege checks first |Identical database boundary;type safety does not authorize a principal or bypass RLS |
| Transport/pooling |No HTTP/browser/pool introduced |Owner must choose transport and prove per-request login,read-only isolation,cancellation/cleanup |Same requirements plus cross-language UUID/time/unknown/bounds parity |
| Response bounds/cache |Existing reference defensive limits only;no search defaults installed |Explicit search/page/candidate/time budgets and authorized projection;no shared cache |Same budgets/private projection/no-cache boundary;no hidden ORM truncation or shared service-user impersonation |
| Security/tests |Continue bounded offline/source checks;not API acceptance |Genuine login/admin/other-user/revoked/pooled-principal and uniform unavailable tests |Same negatives plus port parity and driver lifecycle tests |
| Maintenance/UI |Least added surface;does not deliver browser UX |One local process/driver/framework lifecycle;private UI later,after accepted read API |Additional build/port maintenance;shared browser types may be useful only if Owner chooses it |

The existing reference adapter requests **READ COMMITTED READ ONLY** and `ranking_allowed=False`.
Its current tested bounds are512note links,64KiB selected payload,8KiB variable provenance and2MiB
transport output,with3sstatement/1slock budgets. These bound that reference interface,not a future
search/API SLA or approved browser defaults. Future opaque cursors,host/origin/CSRF controls,
escaping,private projection,limits,transaction cleanup and principal-safe pooling need their own
accepted implementation/tests. Never return inaccessible totals or raw actor/source/capture details.

### Exact binding choice requested in the single Owner batch

| Owner option — none selected here | Exact scope/dependencies needed | Required future acceptance / limits |
|---|---|---|
|Clean application-private pilot|Approve a separate stable genuine nonadmin subject/scope at intake,exact permitted fields/source uses and controlled import target;retain operator pilot unchanged|Genuine owner/other-user/revoked/admin/BYPASSRLS/role-change/effective privileges;source/selection/conflict/rights tests;no operator owner rewrite |
|Reviewed authentication amendment|Accept a separately reviewed versioned revocable identity-binding design and applicable Planning Amendment before runtime changes|Prove authorization/revocation/isolation without editing old migrations or broad bypass;no client-controlled role/GUC/subject bridge |
|CLI-only continuation / defer application reads|Record explicit defer/continuation scope;no principal,transport,credential,service or application data copy is created|May continue allowed synthetic/local evidence work;does not satisfy private browser catalogue/read API acceptance |

Actual `dpt_guard.principal_id()` resolves `dpt.users.auth_subject=session_user`;authenticated
subject and private-scope kind/owner are immutable. Shared memberships do not share an existing
user_private scope. A shared service login is one principal under that model,not automatic multi-user
authorization. Never use administrator fetch-and-filter,SET SESSION AUTHORIZATION,role/user headers,
editable identity GUCs,default curator grants or a scope-owner rewrite to make app access appear ready.

Read families O01–O08 remain proposed contracts:catalogue/name search,detail,positive note lookup,
B1,side-by-side,Mode A,capabilities and caller-private list/source/history reads. A basic name or
positive-note read must still satisfy its genuine session,selection,use/projection and bounds gates;
it does not require inventing every absent optional family/image field. Scoring needs separate exact
method/data/completeness/eligibility/relevance gates. Unknown B2 remains unavailable,not a zero vector.

Future writes remain separate:list/wishlist membership,saved buying-source/price observations,
purchase/manual status records,collection inventory and related transitions need individually
accepted ownership,FKs,idempotency,concurrency,rollback,replay/recovery and UI security contracts.
Cart is a saved-source list,not checkout/order execution or external shopping-account automation.
Existing EA01–EA13 and OC01–OC16 are future API/UI/security acceptance specifications,**NOT RUN**.

Local-private first,no public endpoint,no shared cache,no cloud deployment remain required.
Public catalogue identity never publishes private source,media,shopping,price or collection records.
No API/UI,principal,pool,transport,credential,cache,framework,codec,SQL,normalization,rights or matching
eligibility changes are made here. Coordinator's existing Owner form remains the only answer entry;
no second decision form or duplicate Planning PR is created by this checklist.

## Evidence and verification scope

This lane inspected the full current Master,governance,merged plans005/008 and transition contract,
actual identity/flanker/adapter source and exact unmerged audit documents. It used local files and
read-only Git only. New numerical/runtime/DB/source-permission validation was not executed. Public
tables contain aggregates;private row/UUID/alias/hold registries remain ignored and outside Git/ZIP.
Current DB count/role/rights revalidation remains **BLOCKED**. Full matching/API/UI/normalization/
RLS/import/replay/recovery tests remain **NOT RUN**. Historical source/audit results remain dated.

Only this dedicated Markdown file is owned by this lane. Ignored source bindings/static checks are
under `.local/post2225-BE/`;coordinator owns canonical Task/Status/Decision/Change/Run/PR/ledger/handoff
reconciliation. No receipt,commit,push or PR was created by this worker. Existing tools only:
Caveman,Context Mode,Git/Python/static inspection;no install/configuration or Production mutation.
