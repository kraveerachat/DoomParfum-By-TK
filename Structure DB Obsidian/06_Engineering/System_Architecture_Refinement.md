---
id: DPT-PLAN-010-SYSTEM
project: DoomParfum By TK
type: architecture_amendment
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, system, amendment]
source_of_truth: "../../README.md"
---

# System architecture refinement after PR28

## Authority and outcome

This is a proposed architecture amendment under [[DPT-PLAN-010_System_Architecture_Refinement]], based on main `168715bc9bc5fff968524074257dc106a8a63638`. PR26, PR27 and PR28 are verified Human Owner merges. PR28 merged at UTC `2026-11-15T17:39:38Z` from head `6521c5201f4f4d0e85c4fd8542db222284e96e9e`; its merge tree is identical to that publication tree. The Owner accepts the direction but has not accepted the exact POST27 A/B/I preview contract. IMP-ENR-01 is not started by this task.

All new services, routes, UI handlers, interfaces, DTO schemas, policy recommendations and deployment choices in this package are **PROPOSED**, not implemented or selected. Existing exact synthetic M1/B1 approvals remain unchanged. No application API/frontend/authentication, database/role/migration/identity, acquisition, image bytes, canonical promotion, normalization, 44-hold release, eligibility, cache/service worker, cloud or Production operation is authorized or performed. PR8 stays OPEN/DRAFT/BLOCKED at `84dccb117971ab65e0bf39fa3d1d84a12d344f8d`; its temporal experiment is not repeated.

## Actual implemented architecture

| Existing source | Actual responsibility | What it does not establish |
|---|---|---|
| `database/local.py` and operator entrypoints | Guarded local PostgreSQL/Docker/SQL/operator tooling | Ordinary user authentication, a web server, genuine multi-user app sessions or current service availability |
| Eight migrations and schema contract | Existing scoped schema, RLS, immutable provenance/selection/conflict/rights and integrity functions | A currently queried database, new role policy or app authorization bridge |
| `database.matching_input.read_profile` | Trusted execute-callback SQL/DTO profile read; internal guards and bounded decoding | Browser authentication, connection ownership/pooling, public API or a real scorer input builder |
| `matching_math.synthetic_m1.score_synthetic_notes_layered` | Accepted fixed-fixture pure typed notes-layered scorer | Full Mode A, app ranking or permission to relabel real catalogue rows as fixtures |
| `matching_math.synthetic_b1.score_synthetic_b1` | Accepted fixed-fixture pure typed required/optional/excluded positive-domain scorer | Real B1, B2, alternative any/minimum hard-rule policy, API/UI/transport parsing |
| `matching_math.primitives` | Exact deterministic math/set operations | Source quality, rights, identity, completeness or eligibility |
| `database.image_validation.inspect_png` | Pure bounded static-PNG inspection | Copyright, canonical subject binding, asset permissions or serving bytes |
| `database.image_validation.validate_registered_asset` | Local registered-asset rights/binding/technical validation with a caller-controlled trusted loader | HTTP delivery, safe browser-supplied db/user/callback, or a returned byte stream |
| Existing ETL/research/image/test tooling | Approved operator workflows and scoped synthetic/offline tests | New acquisitions, source adaptation/import, real matching or application acceptance |

[[Function_Interface_and_DTO_Contracts]] records exact signatures and source bindings. The inventory distinguishes 117 top-level public runtime/operator definitions (73 functions and 44 types) from all 593 AST definitions, which also include test/internal/method definitions. Those totals are not application endpoints. The 26 Python files and existing eight migrations are inventoried; live DB/roles/rights/runtime state is NOT VERIFIED in this architecture task.

The prior 194-method scoped offline result is historical evidence on identical canonical code from main8eef through main168. No implementation suite is rerun or claimed for diagrams. Function-level or live authorization coverage is never inferred from a source inventory or module name.

## Proposed target architecture and responsibilities

Recommend retaining the CLI baseline while defining a **Python-first application/domain boundary with a separate UI layer**. This is a direction for Owner review, not a selection of FastAPI, Next.js, React, Drizzle, an ORM/driver/auth provider, a port, container image or host. Logical UI separation does not require a second server process or microservices. A later exact ADR/task must select the actual implementation stack and budgets.

| Layer | Owns | Must not own |
|---|---|---|
| UI | Accessible events, local drafts/view generation and safe presentation of authorized DTOs | Business scoring, database identity/credentials, source rights decisions, canonical promotion or direct SQL/filesystem/operator commands |
| Request boundary | Strict transport/schema/budget checks, accepted proof verification, controlled dispatch and sanitized errors | Browser-supplied user/role authority, implicit coercion, hidden policy defaults or admin impersonation |
| Application | Object/action/field/use authorization, use-case orchestration, transactions, snapshots, capability/eligibility checks and output projection | Invented source facts, raw-data publication or framework-specific math |
| Domain | Canonical/version/domain value objects, exact accepted method semantics, partitioning and rational explanations | UI/HTTP/database connection/storage/provider dependency |
| Infrastructure | Genuine principal leases, approved scoped repositories, original-byte storage, audit adapters and policy configuration | New policy acceptance or uncontrolled browser-selected db/user/path/callback |
| PostgreSQL | Existing constraints/RLS/provenance/selection/integrity under genuine sessions | Authentication of a browser merely because it sends a valid UUID or user-ID header |
| Operator/review lane | Separately approved source/asset capture and explicit human review transitions | A generic privileged HTTP endpoint or automatic approval/hold release |

The 30-component contract and 53-edge source dependency DAG are in [[Component_and_Dependency_Registry]]. The 29 proposed operation interfaces and 58 operation input/output schemas are separate from implemented callables. Proposed UI handler IDs/callable names are registered alongside all 110 interaction contracts in [[UI_Element_Function_Matrix]]. The framework-independent model is `Architecture_Unified_Model.json`, schema identity `architecture-amendment-model-1`, status PROPOSED. Purchase history has a distinct bounded read contract, including own records without a source or inventory link; inventory context never implies an undeclared purchase foreign key.

## Coherent documentation map

| Concern | Canonical proposed refinement for this amendment |
|---|---|
| Context/container/component/data/trust and three request/review sequences | [[C4_Context_and_Container_Design]] — DGM-A through DGM-H |
| Component contracts and acyclic dependency edges | [[Component_and_Dependency_Registry]] |
| Full navigation, routes, hierarchy and journeys | [[Unified_Information_Architecture]] |
| Every meaningful control's 19-field event/use-case/service/source/state/test relationship | [[UI_Element_Function_Matrix]] |
| Implemented source versus future interfaces/DTOs | [[Function_Interface_and_DTO_Contracts]] |
| Genuine principals and object/field/action/rights gates | [[Authorization_and_Trust_Boundaries]] |
| Source, selection, eligibility and media lifecycle | [[Data_and_Media_Lifecycle_Architecture]] |
| Operation-specific offline/cache privacy | [[Cache_Offline_and_Privacy_Policy]] |
| Shared safe UI/domain states and accessibility | [[State_and_Error_Contracts]] |
| Four genuine stack alternatives and unselected details | [[Architecture_Alternatives_and_ADR]] |
| Future units, prerequisites, code surfaces, rollback and acceptance | [[Dependency_Based_Implementation_Roadmap]] |
| Existing A–I impact, new versioned design choices and reply form | [[Architecture_Owner_Review_Packet]] |

Existing notes remain preserved as dated history and roadmap intent. This refinement is canonical **within the proposed amendment**, not an already accepted override. Relevant older notes receive additive reconciliation links; accepted contracts and POST27-ODP-1 are not edited.

## Unified product scope

The IA retains three areas: **Discovery & Matching**, **Personal Shopping & Collection**, and **System / Private Administration**. Seventeen proposed page routes include catalogue/details/pyramid/matching/results/two-column comparison, personal lists/sources/manual statuses/physical bottles/history/dashboard, reviewer/source/rights/operations/settings and sign-in. Routes are not implemented API endpoints.

No legacy requirement disappears to fit a smaller screen count. R09 private URL/screenshot intake remains a metadata-only future request until its separate privacy/rights/task approval; R20 manual missing-perfume proposals remain private unselected claims. R11 personal interest/cart state is distinct from buying links, purchases and physical bottles. R25 Ordered is a manual record, not a transaction. R26 preserves EverPurchased after a bottle finishes/is sold/gifted. R29 unknown optional prices are not zero. R31 spending analytics remains DEFERRED. R12/R19 AI-assisted research/intake intent remains a separately gated P5 lane with no selected model/provider/interface, paid API, implementation or matching dependency.

## Capability matrix

| Capability | Current status | Required data/policy | Authorization | Required future proof / block condition |
|---|---|---|---|---|
| M1 synthetic | IMPLEMENTED; exact Owner-approved contract; historical scoped tests | Accepted fixture identity/vocabulary/domains/config and typed inputs only | Fixture harness scope; no app/real data authority | Existing golden/property/negative evidence; invalid fixture/config/bounds rejected; never real rows disguised as fixtures |
| B1 synthetic | IMPLEMENTED; exact Owner-approved revision2 contract; historical tests | Accepted synthetic required/optional/excluded, positive domain, exact coverage/focus rules | Same fixed-fixture boundary | Unknown is not zero; incomplete cannot establish excluded-note absence; no alternative hard-rule fallback |
| Real Mode A | BLOCKED / NOT IMPLEMENTED | Exact new real method/config/schema, reviewed identities/vocabulary/normalization, selected claims/rights, domains/closure, eligibility and snapshot | Genuine accessible principal, RLS plus use-specific field authorization before candidate expansion | All applicable domain/rights/revocation/partition tests NOT RUN; absent real contract or any required proof denies |
| Real Mode B1 | BLOCKED / NOT IMPLEMENTED | Separate exact real query/hard-rule/coverage/focus/domain contract and same evidence gates | Same genuine caller/object/field/use constraints | Required/excluded incomplete/unknown domains never pass; no fake SYNTHETIC context; tests NOT RUN |
| B2 accords | BLOCKED / NOT IMPLEMENTED | Compatible reviewed taxonomy/observed scale/strengths and exact distinct method; preference sliders are not observed perfume strengths | Same rights and eligibility gates | No note-order/repetition/material-category intensity inference; presence-only fallback is a separate unapproved method |
| Two-column factual comparison | PROPOSED / NOT IMPLEMENTED | Two distinct accessible identities and permitted selected facts; completeness labels preserved | Each profile and field independently authorized | Does not require or fabricate a score; unknown/unselected/conflicting facts stay unavailable/partial; UI/app tests NOT RUN |

Structural/Query Fit, Data Confidence and Direct Pairwise Evidence are separate channels. No model percentage is scientifically measured smell similarity. A missing valid fit is Unavailable, not 0%; a valid computed zero can be rendered only after all method gates pass. No float conversion precedes ordering, and no total rank crosses incompatible method/config/vocabulary/domain/query/selection partitions.

## Request, provenance and revocation contracts

An untrusted browser event can only request a declared operation. The server must validate exact schema/resource policy and proof, establish an approved genuine nonadmin LOGIN lease, verify initial/effective identity and scope, and authorize before restricted lookup/count/page/scoring/asset bytes. A valid UUID proves neither ownership nor permission. Source/field rights, selected claims and materialization remain separate from matching eligibility.

For real inputs, preserve canonical perfume/note identity, source capture/locator/hash, selected observation IDs, source-use/audience rights revisions, vocabulary/normalization/closure versions, conflict/hold state, selection snapshot, exact method/config and trusted caller context. Required missing values stop the operation; no coercion or fallback creates evidence. The application cannot point an admin query at the old operator-private pilot and filter afterward, rewrite immutable ownership, or turn a mutable GUC/header into genuine session identity.

Use fresh bounded read-only scopes for reader operations, with separate explicit write contracts for private data/review. A long operation rechecks membership/rights/selection before publication. Changed evidence invalidates results rather than reusing a stale snapshot or silently retrying forever. Pool cancellation/failure/logout must clean up or discard the lease. Revocation affects future access and remaining delivery under its contract, not erasure of already delivered browser bytes.

## Source/media independence and cache resolution

Licensed records, immutable observations, canonical proposals, reviewed selections, eligibility, media rights and personal records remain independent. The ten-transition lifecycle preserves all 44 holds, 43 proposals and Khamrah evidence. No current task invokes a new import, acquisition, normalization or hold/eligibility change. Media metadata is not image bytes; a URL/CC label is not a project asset binding; PNG technical success is not a rights grant.

Resolve historical offline-first PWA intent conservatively: future cache of static non-personal UI assets may be separately allowed by content identity; operational private/catalogue overlays/matching/cart/collection/media/rights decisions initially remain request/authorized-render scoped, no-store and without shared/persistent private cache or service worker. Offline shell capability must not revive stale permissions or private data. This is a PROPOSED policy requiring Owner approval, not a PWA implementation or a guarantee of browser erasure. Full operation/location/key/scope/lifetime/invalidation/revocation/risk rules are in [[Cache_Offline_and_Privacy_Policy]].

## Documentation conflicts identified and disposition

| Earlier wording or gap | Evidence-backed reconciliation | Owner consequence |
|---|---|---|
| Six-screen matching slice versus original Cart/Collection/Dashboard | One 17-route three-area IA, with private state/source/purchase/bottle separation | No product requirement removed; route/task implementation remains unapproved |
| Generic all/any/minimum controls versus exact required-all synthetic B1 | Preserve alternatives as disabled future policy controls; never alter the accepted method silently | A distinct future exact contract is required |
| Offline-first PWA versus private ephemeral/no-shared-cache direction | Static-only potential offline shell; private operational data unavailable offline initially | F/G/H and a new cache decision require exact review |
| Server/client framework labels treated as security | Server-side code/UUID/cookie does not replace trusted principal/object/field/right checks | Framework/session/transport choices remain explicit future decisions |
| Synthetic scorers considered directly reusable for real rows | Reuse arithmetic knowledge/code only through a separately accepted real boundary; no fixture relabeling | Real methods remain BLOCKED |
| Registered PNG metadata validator considered media delivery | Future service must authorize and deliver the same validated immutable bytes with safe attribution | Intake/storage/display/auth/streaming remain separate gates |
| General PR28 acceptance versus exact A/B/I acceptance | POST27-ODP-1 and SHA remain unchanged and unanswered | IMP-ENR-01 is not started |
| Source presence or historical tests considered running app/current DB | Separate source/test/proposal/live-verification statuses | No current database/app/feature PASS is claimed |

## Verification and next gate

[[DPT-PLAN-010_Architecture_Verification]] records actual research, static model/ID/coverage/DAG/docs/preservation checks and independent architecture review, retaining failures and corrections. It distinguishes those from historical implementation evidence and all future feature/security/accessibility tests marked NOT RUN. Eight diagrams are design artifacts, not implementation tests. One immutable planning receipt is created only after genuine review readiness, followed by exact branch/PR/head and handoff binding.

Human Owner reviews the amendment, chooses or defers the versioned design questions, and later selects an exact implementation ADR/task. No merge or general direction automatically accepts unselected policies. The smallest future private-web slice is an authenticated, genuinely nonadmin, read-only catalogue/detail view with safe placeholders and disabled real matching, only after its principal/data/rights/transport/UI prerequisites. The separate existing five-record preview remains independently gated by exact A/B/I and its original contract; neither path is started now.
