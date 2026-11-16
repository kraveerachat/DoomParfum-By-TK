---
id: DPT-ARCH-UX-IA
project: DoomParfum By TK
type: architecture_information_architecture
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, ux, routes, proposed]
source_of_truth: "../../README.md"
---

# Unified information architecture — proposed amendment

This is the single proposed page/navigation model for DPT-PLAN-010 at base `168715bc9bc5fff968524074257dc106a8a63638`. It reconciles the historical six-screen product with later matching pages. It is a planning amendment awaiting Owner review and merge, not a statement that a browser application exists. Every route, UI handler, service binding and acceptance scenario below is **PROPOSED**; future UI/security/accessibility feature tests are **NOT RUN**.

The machine-readable companion is [[Architecture_Routes_and_States.json]]. [[UI_Element_Function_Matrix]] owns interaction-level handler/event mappings. [[Function_Interface_and_DTO_Contracts]] owns exact versioned input/output schemas. These page routes are not API paths and do not grant authorization. [[System_Architecture_Refinement]] owns architecture boundaries and [[Architecture_Owner_Review_Packet]] owns new decisions.

## Reconciliation and retained product requirements

| Existing requirement/source | Proposed home | Reconciliation |
|---|---|---|
| [[Site_Map_and_Screens]] Catalogue and [[Perfume_Detail_Pyramid]] | R-CATALOGUE, R-DETAIL and focused R-PYRAMID | Keep browse, brand origin versus positioning, exact edition, top/heart/base and general notes, note-chip navigation, provenance and media placeholders. |
| [[Compare_View]] and R15 in [[Requirements_Register]] | R-COMPARE | Exactly two distinct authorized real perfume profiles. Preserve swap, change candidate and save alternative. No accepted three-profile requirement was found. |
| [[Dual_Mode_Scent_Search_UX]] | R-MATCH and R-RESULTS | Preserve independent A reference search, B1 note clauses and B2 accord controls, explicit submit, private drafts and partitioned results. Real execution remains blocked. |
| [[Shopping_Tracker]] and [[My_Cart_and_Ownership]] | R-CART | Keep wishlist, research, to-buy/cart, ordered, tried/skipped and history views; multiple buying links, observed prices, notes, duplicate warning and manual receipt. These are list/status panels, not silently removed pages. |
| [[Collection_Dashboard]] Collection/History | R-COLLECTION and R-COLLECTION-ITEM | Keep independent bottles and purchase history, repeated purchases, Owned/Finished/Sold/Gifted, optional remaining level and private notes. |
| [[Collection_Dashboard]] Dashboard | R-DASHBOARD | Keep Currently Owned versus Ever Purchased, brand/family/note breakdowns and coverage. R31 advanced spending, cost-per-mL and consumption analytics remain deferred. |
| New private review surface | R-SYSTEM and four child routes | Future review/status projections only. Application reviewer is not the database operator; no browser bridge to CLI/admin functions. |
| Account/session shell | R-SETTINGS and R-SIGNIN | Own preferences and future authentication entry; no provider/ORM/framework selected. |
| R09 user input and R20 missing perfumes | R-CART private proposal/intake-request panels | Preserve manual private URL/note input and future screenshot intent; request metadata is not binary intake, source acquisition or canonical promotion. |
| R12 research assistant and R19 AI ETL | Gated P5 roadmap dependency, contextual future capability only | Preserve product intent without adding an unapproved assistant/provider/API or treating AI as a matching dependency. No current assistant function exists. Evidence explanations are not an AI service. |

Private purchase history has separate proposed read and write operations. `IF-PURCHASE-RECORD-READ-1` supplies bounded paginated caller-own history, including records without a bottle link; ownership precedes counts/cursors/pages. `IF-PURCHASE-RECORD-WRITE-1` handles explicit record/edit and optional actual paid price, date, volume and seller. `IF-COLLECTION-READ-1` reads physical inventory and cannot substitute for purchase-history read; no inventory foreign key, paid fact or relationship may be inferred. A bottle-page history panel requires a separately accepted explicit linkage policy and independent authorization; until then its contextual history is Unavailable, never Valid Empty. Unlinked history remains accessible independently in the proposed general history panel. Unknown optional paid facts remain unknown.

`IF-PURCHASE-STATUS-WRITE-1` records only the manual Ordered stamp/bookmark status. `IF-COLLECTION-WRITE-1` changes physical bottle inventory, personal bottle notes, remaining units and bottle lifecycle. A user may explicitly link permitted existing records, but neither a bookmark status nor a browser buying-link click automatically creates an order, purchase record or bottle. Personal-interest/cart reads cannot stand in for Ordered-state or purchase-history read: panels use the interface that owns each datum. All application operations remain unimplemented and PROPOSED. R31 advanced analytics remain deferred.

The older matching UX's all/any/minimum controls are retained as blocked future alternatives, not accepted B1 behavior. Exact synthetic B1 requires every required term under its accepted contract; no UI toggle loosens that required-all rule. A later real-data or alternative method needs its own exact contract, domain/closure semantics, Owner approval and tests. A generic future real-data contract cannot become a wrapper that feeds real identities into the accepted synthetic boundary.

Historical `/`, `/explore`, `/cart`, `/explore/similar?...`, `/explore/scent-profile?...` and slug/query mockups are conceptual predecessors. Proposed canonical page names are `/catalogue`, `/my-cart`, `/matching` and the inventory below. This task implements neither aliases nor redirects. An eventual approved transport/router ADR must choose ID/slug handling without serializing private profile IDs or draft bodies into public/shareable URLs. `/compare` keeps selection in authenticated in-memory context by default; a private query is never encoded merely to recreate an old mockup.

Older mockup percentages, prices, review snippets and chemical/performance narratives are illustrative and unverified. They are not product data or accepted formulas. Family-related or cross-layer annotations need their own reviewed identity/domain rules; color does not establish canonical equality. Older offline-first PWA/local-cache language conflicts with PR28's conservative private ephemeral direction. The proposed resolution is an in-memory private session with no persistent private offline results or queued writes; static assets are addressed separately in the cache architecture. This amendment does not enable a service worker.

## Navigation tree and page hierarchy

```text
Application shell (C-UI-SHELL)
  DISCOVERY & MATCHING
    Catalogue /catalogue [R-CATALOGUE]
      Perfume /perfumes/:id [R-DETAIL]
        Note Pyramid /perfumes/:id/notes [R-PYRAMID]
    Matching Search /matching [R-MATCH]
      Mode A: Similar to a perfume
      Build a scent profile: B1 Notes / B2 Accords
      Results /matching/results [R-RESULTS]
    Compare /compare [R-COMPARE]
  PERSONAL SHOPPING & COLLECTION
    My Cart /my-cart [R-CART]
      Wishlist / Research / To Buy / Ordered / Tried / Skipped / History panels
      Saved-source and manual-status dialogs
    Collection /collection [R-COLLECTION]
      Current Inventory / Purchase History panels
      Private bottle /collection/:id [R-COLLECTION-ITEM]
    Dashboard /dashboard [R-DASHBOARD]
  SYSTEM / PRIVATE ADMINISTRATION
    System /system [R-SYSTEM] (explicit permission only)
      Sources /system/sources [R-SOURCES]
      Reviews /system/reviews [R-REVIEWS]
      Rights & Media /system/rights-media [R-RIGHTS-MEDIA]
      Operations status /system/operations [R-OPERATIONS]
    Own Settings /settings [R-SETTINGS]
    Sign in /sign-in [R-SIGNIN] (safe unauthenticated entry)
```

Group headings are navigation categories, not permission groups. Hide System navigation unless dedicated application-review permissions are present, and independently gate every request. Ordinary authenticated users see own Settings; sign-in remains a safe entry. A role label alone does not establish a genuine PostgreSQL session principal. No anonymous catalogue counts, private vocabulary, suggestions, thumbnails, prefetch or hidden-DOM data are permitted.

## Component hierarchy and dependency direction

`C-UI-SHELL` contains skip link, landmarks, role-filtered navigation, global search, account/session controls and accessible status/error regions. `C-UI-PAGES` contains the 17 page compositions and reusable presentation components: labeled form controls, tabs, comboboxes, chips, perfume cards, pyramid sections, evidence/coverage panels, media placeholders, two-profile table, saved-source dialogs, private bottle/history panels, chart tables and authorized review forms. These names describe view compositions, not additional architecture component IDs.

Each operation follows a proposed page event/handler in [[UI_Element_Function_Matrix]], a versioned logical interface through `C-TRANSPORT`/`C-DTO`, server authentication and genuine principal binding, operation/object/field/rights authorization, the relevant application use case, ports and infrastructure. UI never selects a database login, calls operator CLI, directly queries PostgreSQL or invokes a synthetic scorer on a real profile. Domain logic has no dependency on UI, HTTP or routes. Existing source modules do not become application services merely because an interaction needs them.

Route dependencies below reference common component IDs; the common component registry owns exact acyclic wiring. Child presentation widgets are not independent backends. Browser component hiding, a disabled button and a route guard are convenience layers; authorization must also precede restricted queries, counts, cursors, scoring and media bytes in the service/data boundary.

## Route authorization matrix

All rows are proposed. “Owner” below means owner of a private application record, not PostgreSQL owner/admin. “Reviewer” means explicitly delegated application review permissions, independently scoped to each object and operation.

| Route ID | Anonymous | Ordinary authenticated user | Explicit reviewer | Before data/count/media access |
|---|---|---|---|---|
| R-CATALOGUE | No protected data; safe sign-in/generic denial | Only authorized selected profiles/fields | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-DETAIL | No protected data; safe sign-in/generic denial | Only authorized selected profiles/fields | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-PYRAMID | No protected data; safe sign-in/generic denial | Only authorized selected profiles/fields | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-MATCH | No protected data; safe sign-in/generic denial | Only authorized selected profiles/fields | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-RESULTS | No protected data; safe sign-in/generic denial | Only authorized selected profiles/fields | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-COMPARE | No protected data; safe sign-in/generic denial | Only authorized selected profiles/fields | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-CART | No protected data; safe sign-in/generic denial | Own records only | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-COLLECTION | No protected data; safe sign-in/generic denial | Own records only | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-COLLECTION-ITEM | No protected data; safe sign-in/generic denial | Own records only | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-DASHBOARD | No protected data; safe sign-in/generic denial | Own records only | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-SYSTEM | No protected data; safe sign-in/generic denial | No access by default | Dedicated operation + object + evidence/rights permission | Fresh session/principal, scope, current rights, field/object permission |
| R-SOURCES | No protected data; safe sign-in/generic denial | No access by default | Dedicated operation + object + evidence/rights permission | Fresh session/principal, scope, current rights, field/object permission |
| R-REVIEWS | No protected data; safe sign-in/generic denial | No access by default | Dedicated operation + object + evidence/rights permission | Fresh session/principal, scope, current rights, field/object permission |
| R-RIGHTS-MEDIA | No protected data; safe sign-in/generic denial | No access by default | Dedicated operation + object + evidence/rights permission | Fresh session/principal, scope, current rights, field/object permission |
| R-OPERATIONS | No protected data; safe sign-in/generic denial | No access by default | Dedicated operation + object + evidence/rights permission | Fresh session/principal, scope, current rights, field/object permission |
| R-SETTINGS | No protected data; safe sign-in/generic denial | Own records only | No extra private-user access; same object gate | Fresh session/principal, scope, current rights, field/object permission |
| R-SIGNIN | Safe authentication UI only | Own session only | No extra private-user access; same object gate | No private projection |

Nonexistent and denied private identifiers share a safe response envelope. HTTP code, response-size/timing equivalence, streaming, prefetch and browser cache handling need later transport/browser tests; this document does not claim those tests have run. Only a known authorized object can expose a detailed conflict/hold/revocation reason. Review users cannot infer another user's purchase history or protected source merely from a badge, count, alt text or disabled control.

## Page contracts

“Available data” below describes a future authorized projection, not a currently deployed screen or live database verification. All interfaces and DTOs are logical proposals; exact contracts remain in [[Function_Interface_and_DTO_Contracts]].

### R-CATALOGUE — `/catalogue`

- **Purpose:** Browse and search caller-authorized perfume identities; independently filter brand origin, positioning and reviewed fields.
- **Group:** DISCOVERY & MATCHING
- **User role:** authenticated application user
- **Entry points:** global navigation; global search; note/brand chip; sign-in success
- **Exit points:** R-DETAIL; R-MATCH; R-COMPARE; R-CART
- **Child components:** search form; brand/origin/position filters; price/currentness filters; perfume cards; pagination; capability notices
- **Available data:** Future projection of authorized reviewed catalogue identity/profile fields with source/date/rights; actual Python/DB source presence is separate from a UI service.
- **Unavailable features:** All page handlers and services unimplemented; No anonymous private suggestions or counts; Unavailable region/stock/price fields cannot be advertised as complete filters
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-CATALOGUE-QUERY-1; IF-CAPABILITY-READ-1; IF-MEDIA-RESOLVE-1; IF-MEDIA-DELIVER-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-CATALOGUE; C-AUTHN; C-PRINCIPAL; C-AUTHZ
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-CATALOGUE-01`: Search/filter/pagination authorize before results and counts, including prefetch.
  - `UAT-CATALOGUE-02`: Unknown price is not zero; filter labels describe observed source/date/currency/size.
  - `UAT-CATALOGUE-03`: Keyboard card links and independent filters preserve origin versus brand-position distinction.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-DETAIL — `/perfumes/:id`

- **Purpose:** Inspect exact edition/concentration, notes, accords, provenance and separately permitted evidence.
- **Group:** DISCOVERY & MATCHING
- **User role:** authenticated application user
- **Entry points:** R-CATALOGUE; R-RESULTS; R-COMPARE; R-COLLECTION
- **Exit points:** R-PYRAMID; R-MATCH; R-COMPARE; R-CART; R-CATALOGUE
- **Child components:** identity header; bottle media; overview/notes/accords/evidence/source tabs; note chips; find-similar; seed-query; compare; save to cart
- **Available data:** Future caller-authorized selected observations; authorized media metadata and bytes are separately gated; no inferred formula.
- **Unavailable features:** UI unimplemented; No unreviewed normalization promotion; No invented layered notes, observed intensity, review score or live price
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-PROFILE-READ-1; IF-VOCABULARY-READ-1; IF-CAPABILITY-READ-1; IF-MEDIA-RESOLVE-1; IF-MEDIA-DELIVER-1; IF-PERSONAL-STATE-WRITE-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-CATALOGUE; C-APP-MEDIA; C-APP-PRIVATE; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-DETAIL-01`: Exact edition choice is explicit; a general list is not distributed into top/heart/base.
  - `UAT-DETAIL-02`: Missing image uses a semantic placeholder; note artwork does not prove composition.
  - `UAT-DETAIL-03`: Tabs expose independent structural fit, data confidence and direct pairwise evidence.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-PYRAMID — `/perfumes/:id/notes`

- **Purpose:** Provide a focused accessible view of reviewed layer assignments and All Listed Notes when layering is unknown.
- **Group:** DISCOVERY & MATCHING
- **User role:** authenticated application user
- **Entry points:** R-DETAIL notes tab; note section deep navigation
- **Exit points:** R-DETAIL; R-CATALOGUE; R-MATCH
- **Child components:** top/heart-middle/base sections; All Listed Notes section; note chip links; rights attribution; illustration placeholders; layer completeness badges
- **Available data:** Only authorized notes with selected source lineage, canonical IDs and explicit completeness; illustration and actual note assertion remain distinct.
- **Unavailable features:** UI unimplemented; No fabricated chemical formula or scent strength; No guessing layer assignments from order, name or image
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-PROFILE-READ-1; IF-VOCABULARY-READ-1; IF-MEDIA-RESOLVE-1; IF-MEDIA-DELIVER-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-CATALOGUE; C-APP-MEDIA; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-PYRAMID-01`: Partial layers and general notes remain separately labeled.
  - `UAT-PYRAMID-02`: Note-chip keyboard activation opens authorized catalogue filter or explicit query seed.
  - `UAT-PYRAMID-03`: Known absence needs a compatible complete closed domain; missing data never implies absence.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-MATCH — `/matching`

- **Purpose:** Author ephemeral Similar to a perfume (A) or Build a scent profile queries, retaining B1 Notes and B2 Accords as distinct tabs.
- **Group:** DISCOVERY & MATCHING
- **User role:** authenticated application user
- **Entry points:** global navigation; R-DETAIL Find similar; R-DETAIL seed reviewed notes; R-RESULTS edit
- **Exit points:** R-RESULTS; R-DETAIL; R-CATALOGUE
- **Child components:** mode selector; exact reference combobox; B1 must/prefer/exclude clauses; layer/Any Layer selector; blocked future all/any/minimum alternative controls; accepted synthetic B1 required-all remains exact; B2 accord selectors/sliders/numeric inputs; filters; add/remove/reset/clear/search/cancel; safe-link capability
- **Available data:** Authorized vocabulary and profile seeds only; exact synthetic M1/B1 source capability is not a real-data UI capability.
- **Unavailable features:** All handlers unimplemented; Real A/B1/B2 execution blocked pending exact approvals and eligibility; B3 deferred; Private/mixed query sharing unavailable; no synthetic substitution; Historical match-all/any/minimum alternatives remain blocked pending their own exact method contract; they do not loosen accepted B1 required-all semantics or authorize a generic real-data wrapper around synthetic contracts
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-CATALOGUE-QUERY-1; IF-PROFILE-READ-1; IF-VOCABULARY-READ-1; IF-CAPABILITY-READ-1; IF-MATCH-VALIDATE-1; IF-MATCH-EXECUTE-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-CATALOGUE; C-APP-MATCH; C-DOMAIN-REAL; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-MATCH-01`: Inactive tab draft never affects scoring; Clear empties active query, Reset restores its visible seed, Remove deletes one clause.
  - `UAT-MATCH-02`: Sliders update local user preferences only, with keyboard and numeric alternatives; they never fabricate measured candidate intensity.
  - `UAT-MATCH-03`: Explicit submit validates bounds/contradictions and capability; real matching stays unavailable without its gates.
  - `UAT-MATCH-04`: Seeded private draft remains private; no IDs, private notes or query body enter URLs/logs/shares.
  - `UAT-MATCH-REQUIRED-ALL`: Accepted B1 required-all semantics remain unchanged; historical all/any/minimum alternatives and any real-data method require separate exact approved contracts. No generic future real contract relabels real inputs as synthetic.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-RESULTS — `/matching/results`

- **Purpose:** Present transient authorized results grouped by compatible method/domain/coverage partitions, with explicit incomplete-search limits.
- **Group:** DISCOVERY & MATCHING
- **User role:** authenticated application user
- **Entry points:** R-MATCH explicit validated submit
- **Exit points:** R-MATCH; R-DETAIL; R-COMPARE; R-CART
- **Child components:** query summary; partition groups; result cards; fit explanation disclosure; coverage/confidence/evidence panels; compare/save actions; cancel/retry/narrow filters
- **Available data:** Future authorized result DTO for an accepted real method; exact rational ordering retained through ranking; display rounding happens afterward.
- **Unavailable features:** Page/execution unimplemented; No real matching activation or synthetic fallback; No persisted query history or result deep link guarantee; No cross-partition total ranking
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-CAPABILITY-READ-1; IF-MATCH-EXECUTE-1; IF-PROFILE-READ-1; IF-MEDIA-RESOLVE-1; IF-MEDIA-DELIVER-1; IF-PERSONAL-STATE-WRITE-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-MATCH; C-APP-CATALOGUE; C-APP-MEDIA; C-APP-PRIVATE; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-RESULTS-01`: A valid computed zero can display 0%; no valid score displays Unavailable, never 0%.
  - `UAT-RESULTS-02`: Valid Empty requires completed authorized eligible search; missing/held capability does not become zero matches.
  - `UAT-RESULTS-03`: Stale responses after query change/session change are ignored; refresh with no memory draft returns to query authoring.
  - `UAT-RESULTS-04`: Fit, data confidence and direct pairwise evidence have separate labels and no scientifically measured smell claim.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-COMPARE — `/compare`

- **Purpose:** Compare two authorized real perfume profiles factually; show optional structural scoring only when its own method and eligibility gates pass.
- **Group:** DISCOVERY & MATCHING
- **User role:** authenticated application user
- **Entry points:** R-DETAIL; R-RESULTS; R-CATALOGUE compare selection
- **Exit points:** R-DETAIL; R-MATCH; R-CART; R-CATALOGUE
- **Child components:** two profile selectors; swap columns; change candidate; notes/accords table; shared/listed-only/unknown labels; evidence panel; score explanation; save alternative
- **Available data:** Future authorized profile projections and separately permissioned pairwise evidence; factual comparison does not require a valid score.
- **Unavailable features:** All UI unimplemented; No accepted three-column expansion; No custom B query masquerading as a perfume column; No evidence-blended percentage or fuzzy spelling treated as canonical equality
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-COMPARISON-READ-1; IF-CATALOGUE-QUERY-1; IF-CAPABILITY-READ-1; IF-MEDIA-RESOLVE-1; IF-MEDIA-DELIVER-1; IF-PERSONAL-STATE-WRITE-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-COMPARE; C-APP-CATALOGUE; C-APP-MEDIA; C-APP-PRIVATE; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-COMPARE-01`: Exactly two distinct authorized real profiles preserve R15 and Compare_View; swapping preserves identity-specific facts; a duplicate identity must be corrected explicitly.
  - `UAT-COMPARE-02`: Listed only is distinct from absent; highlight canonical ID/layer matches with text, not color alone.
  - `UAT-COMPARE-03`: Missing or blocked score leaves factual comparison available when both profiles remain authorized.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-CART — `/my-cart`

- **Purpose:** Maintain personal bookmarks, multiple saved buying sources and manually recorded wishlist/research/cart/ordered/tried/skipped states.
- **Group:** PERSONAL SHOPPING & COLLECTION
- **User role:** authenticated record owner
- **Entry points:** global navigation; save from catalogue/detail/results/compare; R-COLLECTION re-buy
- **Exit points:** R-DETAIL; R-COLLECTION; R-COLLECTION-ITEM; external browser destination
- **Child components:** wishlist/research/to-buy/ordered/history views; item cards; duplicate warning; source add/edit/remove dialog; observed-price/source-note editor; open buying link; manual Ordered/Received forms; remove/move actions; informational budget; manual missing-perfume private proposal panel; future user-URL/screenshot intake request metadata panel; explicit own purchase-history record/edit form (optional paid price/date/volume/seller); bounded paginated own purchase-history panel, independent from physical inventory
- **Available data:** Only owner-scoped saved lists, listings and dated observed prices; exact source/variant/currency/date are retained; fields stay optional where specified.; IF-PURCHASE-RECORD-READ-1 supplies separately authorized bounded paginated caller-own history, including records with no bottle link; no collection foreign key, paid fact or relationship is inferred. Unknown paid price/date/volume/seller remain explicit unknowns.; Purchase-history optional paid price/date/volume/seller bind IF-PURCHASE-RECORD-WRITE-1; manual Ordered stamp binds IF-PURCHASE-STATUS-WRITE-1; physical bottle notes/remaining amount/lifecycle bind IF-COLLECTION-WRITE-1. No combined automatic operation is implied.
- **Unavailable features:** All handlers unimplemented; No checkout, payment, order placement or automatic Shopee/cart synchronization; No live seller polling, server-side URL fetching, URL previews/prefetch or automatic availability claims; R09 screenshot binary intake/OCR remains future and approval-gated; metadata request does not accept bytes; R20 missing-perfume request stays private unselected proposal; no canonical promotion or source acquisition; R12 AI assistance/R19 AI ETL remain gated P5 scope, not a matching prerequisite or implemented assistant; No automatic order, purchase-history or bottle creation; each permitted explicit intent uses its separate proposed interface
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Bind every list, purchase and bottle to the session owner; reviewer role grants no access to another user's private records.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-BUYING-SOURCES-READ-1; IF-BUYING-SOURCE-WRITE-1; IF-PURCHASE-STATUS-WRITE-1; IF-COLLECTION-WRITE-1; IF-PERSONAL-STATE-READ-1; IF-PERSONAL-STATE-WRITE-1; IF-SOURCE-INTAKE-REQUEST-1; IF-ASSET-INTAKE-REQUEST-1; IF-PURCHASE-RECORD-WRITE-1; IF-PURCHASE-RECORD-READ-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-PRIVATE; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-CART-01`: External URL activation is an explicit browser-only navigation; no application server fetch, commerce action, private query referrer or automatic state change.
  - `UAT-CART-02`: Duplicate bookmark offers open existing/add source; repeat real purchases remain separate history records.
  - `UAT-CART-03`: Manual Ordered stamp records the user report of an already external order only. Explicit purchase-history record/edit and explicit physical receipt/bottle recording are separate intents/interfaces; none automatically creates an order, purchase or bottle.
  - `UAT-CART-04`: Unknown price is not free and informational totals disclose coverage/currency.
  - `UAT-CART-05`: Personal wishlist/research/app_cart/tried/skipped state writes are separate from buying sources, actual purchases and bottle inventory.
  - `UAT-CART-06`: R09/R20 private intake request accepts only bounded permitted metadata and never fetches URLs, accepts screenshot bytes, acquires sources or promotes canonical identity.
  - `UAT-CART-PURCHASE-RECORD`: Explicit own purchase-history record/edit uses IF-PURCHASE-RECORD-WRITE-1, distinct from bookmark Ordered stamp and physical bottle writes; optional paid fields never overwrite inventory or create an order/purchase/bottle automatically.
  - `UAT-CART-PURCHASE-HISTORY-READ`: History panel uses IF-PURCHASE-RECORD-READ-1 with caller ownership before counts/cursors/pages; history without inventory linkage remains readable independently, optional paid facts stay unknown, and no bottle relationship is inferred.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-COLLECTION — `/collection`

- **Purpose:** Manage owner bottle inventory and independent purchase history, including repeat purchases and previously owned items.
- **Group:** PERSONAL SHOPPING & COLLECTION
- **User role:** authenticated record owner
- **Entry points:** global navigation; R-CART Received; R-DASHBOARD drill-down
- **Exit points:** R-COLLECTION-ITEM; R-DETAIL; R-CART; R-DASHBOARD
- **Child components:** current inventory/history tabs; owned/finished/sold/gifted filters; bottle cards; history rows; re-buy action; status/remaining-level dialogs; explicit own purchase-history record/edit form (optional paid price/date/volume/seller); bounded paginated own purchase-history panel, independent from physical inventory
- **Available data:** Future owner-authorized bottles and purchase records; observed remaining amount is user input, not predicted consumption.; IF-PURCHASE-RECORD-READ-1 supplies separately authorized bounded paginated caller-own history, including records with no bottle link; no collection foreign key, paid fact or relationship is inferred. Unknown paid price/date/volume/seller remain explicit unknowns.; Purchase-history optional paid price/date/volume/seller bind IF-PURCHASE-RECORD-WRITE-1; manual Ordered stamp binds IF-PURCHASE-STATUS-WRITE-1; physical bottle notes/remaining amount/lifecycle bind IF-COLLECTION-WRITE-1. No combined automatic operation is implied.
- **Unavailable features:** All UI unimplemented; No inferred purchase or deletion of historical purchase when bottle changes; No cross-user list/count projection; No automatic order, purchase-history or bottle creation; each permitted explicit intent uses its separate proposed interface
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Bind every list, purchase and bottle to the session owner; reviewer role grants no access to another user's private records.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-COLLECTION-READ-1; IF-COLLECTION-WRITE-1; IF-PERSONAL-STATE-WRITE-1; IF-PURCHASE-RECORD-WRITE-1; IF-PURCHASE-RECORD-READ-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-PRIVATE; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-COLLECTION-01`: Two purchases yield distinct purchase records; bottle and purchase cardinality are not forced one-to-one.
  - `UAT-COLLECTION-02`: Finished/sold/gifted bottle changes Currently Owned but preserves Ever Purchased history.
  - `UAT-COLLECTION-03`: Tabs and filters count only owner-authorized objects.
  - `UAT-COLLECTION-PURCHASE-RECORD`: Explicit own purchase-history record/edit uses IF-PURCHASE-RECORD-WRITE-1, distinct from bookmark Ordered stamp and physical bottle writes; optional paid fields never overwrite inventory or create an order/purchase/bottle automatically.
  - `UAT-COLLECTION-PURCHASE-HISTORY-READ`: History panel uses IF-PURCHASE-RECORD-READ-1 with caller ownership before counts/cursors/pages; history without inventory linkage remains readable independently, optional paid facts stay unknown, and no bottle relationship is inferred.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-COLLECTION-ITEM — `/collection/:id`

- **Purpose:** Inspect one owner bottle and associated acquisition/history; edit personal notes, remaining amount and lifecycle with explicit validation.
- **Group:** PERSONAL SHOPPING & COLLECTION
- **User role:** authenticated record owner
- **Entry points:** R-COLLECTION bottle/history row; R-CART explicit receipt; R-DASHBOARD permitted drill-down
- **Exit points:** R-COLLECTION; R-DETAIL; R-CART
- **Child components:** bottle summary; linked purchase/history panel; optional price/date/volume/seller fields; personal notes; remaining amount input; finish/sell/gift controls; re-buy; explicit own purchase-history record/edit form (optional paid price/date/volume/seller); bounded paginated own purchase-history panel, independent from physical inventory
- **Available data:** Only authorized private bottle and purchase data, plus separately authorized catalogue links; history may exist without a current bottle.; IF-PURCHASE-RECORD-READ-1 supplies separately authorized bounded paginated caller-own history, including records with no bottle link; no collection foreign key, paid fact or relationship is inferred. Unknown paid price/date/volume/seller remain explicit unknowns.; Purchase-history optional paid price/date/volume/seller bind IF-PURCHASE-RECORD-WRITE-1; manual Ordered stamp binds IF-PURCHASE-STATUS-WRITE-1; physical bottle notes/remaining amount/lifecycle bind IF-COLLECTION-WRITE-1. No combined automatic operation is implied.; Bottle-context history requires a separately accepted explicit linkage policy and independent authorization; until that policy exists, the contextual panel is Unavailable, not Valid Empty. No collection foreign key or relationship is inferred. Independent caller-own history browsing remains proposed in R-COLLECTION, including unlinked purchases; absence of a bottle link is not absence of a past purchase.
- **Unavailable features:** All UI unimplemented; No exposing order references/private notes through public repository, URL, analytics or reviewer role; No automatic marketplace transaction; No automatic order, purchase-history or bottle creation; each permitted explicit intent uses its separate proposed interface; Bottle-context purchase-history linkage is unavailable until its separate exact policy/schema is approved; this page does not invent a collection-to-purchase foreign key
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Bind every list, purchase and bottle to the session owner; reviewer role grants no access to another user's private records.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-COLLECTION-READ-1; IF-COLLECTION-WRITE-1; IF-PERSONAL-STATE-WRITE-1; IF-PURCHASE-RECORD-WRITE-1; IF-PURCHASE-RECORD-READ-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-PRIVATE; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-COLLECTION-ITEM-01`: Cross-user ID and nonexistent bottle have indistinguishable denial; all linked records independently authorize.
  - `UAT-COLLECTION-ITEM-02`: Lifecycle edit retains history and detects stale concurrent edits.
  - `UAT-COLLECTION-ITEM-03`: Optional missing price/date/volume stays unknown; repeat purchase never overwrites prior history.
  - `UAT-COLLECTION-ITEM-PURCHASE-RECORD`: Explicit own purchase-history record/edit uses IF-PURCHASE-RECORD-WRITE-1, distinct from bookmark Ordered stamp and physical bottle writes; optional paid fields never overwrite inventory or create an order/purchase/bottle automatically.
  - `UAT-COLLECTION-ITEM-PURCHASE-HISTORY-READ`: History panel uses IF-PURCHASE-RECORD-READ-1 with caller ownership before counts/cursors/pages; history without inventory linkage remains readable independently, optional paid facts stay unknown, and no bottle relationship is inferred.
  - `UAT-COLLECTION-ITEM-HISTORY-LINKAGE`: Without a separately accepted linkage policy, bottle-context history is Unavailable rather than Valid Empty; independently authorized unlinked history remains readable through the general history panel without inferred foreign keys.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-DASHBOARD — `/dashboard`

- **Purpose:** Summarize Currently Owned and Ever Purchased separately, with evidence-aware brand/family/note breakdowns.
- **Group:** PERSONAL SHOPPING & COLLECTION
- **User role:** authenticated record owner
- **Entry points:** global navigation; R-COLLECTION
- **Exit points:** R-COLLECTION; R-COLLECTION-ITEM; R-DETAIL
- **Child components:** owned/purchased metrics; brand-origin/family/note charts; tabular chart alternatives; coverage/date labels; filters; authorized drill-down links
- **Available data:** Future aggregate of authorized owner records and authorized selected catalogue metadata; missing metadata contributes explicit coverage limits.
- **Unavailable features:** All UI unimplemented; R31 advanced cost-per-mL/consumption analytics remain deferred; No global sales metrics, inferred spending, mixed-currency sum or unavailable price rendered as zero
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Bind every list, purchase and bottle to the session owner; reviewer role grants no access to another user's private records.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-DASHBOARD-READ-1; IF-COLLECTION-READ-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-PRIVATE; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-DASHBOARD-01`: Currently Owned counts current owned bottles; Ever Purchased uses retained purchase records independent of disposal.
  - `UAT-DASHBOARD-02`: Charts have text/table alternatives, meaningful labels and counts only after authorization.
  - `UAT-DASHBOARD-03`: Any optional spending subtotal states known-price coverage and currency; deferred analytics are not launched.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-SYSTEM — `/system`

- **Purpose:** Expose a future permission-filtered private review landing page and capability summaries, keeping operator tooling separate.
- **Group:** SYSTEM / PRIVATE ADMINISTRATION
- **User role:** explicitly authorized application reviewer
- **Entry points:** role-filtered system navigation
- **Exit points:** R-SOURCES; R-REVIEWS; R-RIGHTS-MEDIA; R-OPERATIONS; R-CATALOGUE
- **Child components:** review task navigation; permitted queue summaries; capability notices; safe operator-status summary
- **Available data:** Future authorized review projections only; historical local diagnostics are evidence, not a live admin endpoint.
- **Unavailable features:** All UI unimplemented; No CLI runner, SQL console, role/identity management or admin database session; No unapproved hold release
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Hide navigation without explicit review permission, then independently enforce permission on server. No browser operator/admin identity or CLI invocation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-REVIEW-QUEUE-READ-1; IF-OPERATOR-STATUS-READ-1; IF-CAPABILITY-READ-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-REVIEW; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-SYSTEM-01`: Navigation hidden without review permission; direct access independently denied before queue counts.
  - `UAT-SYSTEM-02`: Application reviewer never inherits operator/admin database privileges.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-SOURCES — `/system/sources`

- **Purpose:** Review source provenance and submit bounded future intake requests; distinguish request from acquisition/approval.
- **Group:** SYSTEM / PRIVATE ADMINISTRATION
- **User role:** explicitly authorized source reviewer/requester
- **Entry points:** R-SYSTEM; R-REVIEWS permitted source link
- **Exit points:** R-SYSTEM; R-REVIEWS; R-RIGHTS-MEDIA
- **Child components:** source metadata list; rights/checked-at summary; intake request form; request status; validation summary
- **Available data:** Future authorized source records and review proposals; no raw restricted capture in browser unless independently permitted.
- **Unavailable features:** All UI unimplemented; No source acquisition/import/network job; No URL as implicit license grant or scrape instruction
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Hide navigation without explicit review permission, then independently enforce permission on server. No browser operator/admin identity or CLI invocation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-REVIEW-QUEUE-READ-1; IF-SOURCE-INTAKE-REQUEST-1; IF-RIGHTS-REVIEW-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-REVIEW; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-SOURCES-01`: Submit records a review request only; does not fetch URL or start IMP-ENR-01.
  - `UAT-SOURCES-02`: Rights scope/date and actor are explicit; rejected request leaves canonical selection unchanged.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-REVIEWS — `/system/reviews`

- **Purpose:** Inspect authorized proposals/conflicts and design future explicit review decisions with audit and version checks.
- **Group:** SYSTEM / PRIVATE ADMINISTRATION
- **User role:** explicitly authorized reviewer
- **Entry points:** R-SYSTEM; R-SOURCES; R-RIGHTS-MEDIA
- **Exit points:** R-SYSTEM; R-SOURCES; R-RIGHTS-MEDIA
- **Child components:** review queue; proposal/current comparison; source evidence disclosure; approve/reject/hold forms; reason field; stale-version warning
- **Available data:** Future permissioned review proposals and current-selection references; field and source visibility checked independently.
- **Unavailable features:** All UI unimplemented; No approval conferred by this plan; 44 holds, 43 normalization proposals and Khamrah conflict remain unchanged; PR8 blocked
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Hide navigation without explicit review permission, then independently enforce permission on server. No browser operator/admin identity or CLI invocation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-REVIEW-QUEUE-READ-1; IF-REVIEW-DECISION-WRITE-1; IF-RIGHTS-REVIEW-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-REVIEW; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-REVIEWS-01`: Review decision requires dedicated permission, current version, reason and audit; stale decision is rejected without canonical mutation.
  - `UAT-REVIEWS-02`: Detailed hold/conflict data appears only after object and evidence authorization.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-RIGHTS-MEDIA — `/system/rights-media`

- **Purpose:** Review asset metadata, exact source bindings and intended-use rights independently from image bytes.
- **Group:** SYSTEM / PRIVATE ADMINISTRATION
- **User role:** explicitly authorized media/rights reviewer
- **Entry points:** R-SYSTEM; R-SOURCES; R-REVIEWS
- **Exit points:** R-SYSTEM; R-SOURCES; R-REVIEWS
- **Child components:** asset/rights metadata; use-scope/private-public-derivative fields; attribution review; intake request form; revocation review; authorized preview or placeholder
- **Available data:** Future authorized asset metadata and permission records; actual bytes require separate current rights resolution and delivery gate.
- **Unavailable features:** All UI unimplemented; No image acquisition or binary download in this task; No hotlink/public URL/license-label shortcut to approved asset; No public display or derivative rights inferred from private rights
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Hide navigation without explicit review permission, then independently enforce permission on server. No browser operator/admin identity or CLI invocation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-REVIEW-QUEUE-READ-1; IF-ASSET-INTAKE-REQUEST-1; IF-RIGHTS-REVIEW-1; IF-MEDIA-RESOLVE-1; IF-MEDIA-DELIVER-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-REVIEW; C-APP-MEDIA; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-RIGHTS-MEDIA-01`: Metadata visibility does not grant byte delivery; rights checked again at delivery.
  - `UAT-RIGHTS-MEDIA-02`: Revoked or unknown rights suppress preview without revealing protected existence.
  - `UAT-RIGHTS-MEDIA-03`: Note illustration, bottle photograph, validation and actual source formula evidence remain separate.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-OPERATIONS — `/system/operations`

- **Purpose:** Present a future sanitized status projection and manual runbook references for authorized reviewers.
- **Group:** SYSTEM / PRIVATE ADMINISTRATION
- **User role:** explicitly authorized operations-status viewer
- **Entry points:** R-SYSTEM
- **Exit points:** R-SYSTEM; R-SOURCES; R-REVIEWS
- **Child components:** sanitized status; last checked-at; capability/blocked notices; manual runbook links
- **Available data:** Future explicitly permitted summary only; historical receipts remain immutable documents, not automated operational controls.
- **Unavailable features:** All UI unimplemented; No browser CLI, database admin, shell, install, deployment, role changes or credential exposure
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Hide navigation without explicit review permission, then independently enforce permission on server. No browser operator/admin identity or CLI invocation.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-OPERATOR-STATUS-READ-1; IF-CAPABILITY-READ-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-REVIEW; C-AUTHZ; C-AUTHN; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-OPERATIONS-01`: Operation page is read-only and contains no operator execution bridge.
  - `UAT-OPERATIONS-02`: Unavailable diagnostics do not reveal filesystem paths, secrets or raw error traces.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-SETTINGS — `/settings`

- **Purpose:** Edit own bounded preferences and view private-session/privacy behavior; terminate session explicitly.
- **Group:** SYSTEM / PRIVATE ADMINISTRATION
- **User role:** authenticated application user for own settings
- **Entry points:** account menu
- **Exit points:** R-CATALOGUE; R-SIGNIN
- **Child components:** own preferences form; privacy/cache explanation; session status; sign-out
- **Available data:** Future owner-scoped settings DTO and safe own-session state only.
- **Unavailable features:** All UI unimplemented; No role grant, user impersonation, database-principal selection or auth-provider choice; No private offline persistence or service worker
- **Security constraints:** Authenticate; bind genuine nonadmin application principal; authorize scope/object/selected fields and current rights before restricted lookup, counts, pagination, scoring or bytes. UUID/path is not authority. Denial and nonexistent private objects have an indistinguishable safe presentation. Bind every list, purchase and bottle to the session owner; reviewer role grants no access to another user's private records.
- **Logical interfaces:** IF-AUTH-SESSION-1; IF-PRINCIPAL-LEASE-1; IF-PRIVATE-SETTINGS-1; IF-SESSION-END-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-APP-PRIVATE; C-AUTHN; C-AUTHZ; C-PRINCIPAL
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-SETTINGS-01`: Settings writes bind to session owner and reject unknown fields.
  - `UAT-SETTINGS-02`: Logout cancels requests and best-effort clears in-memory drafts/results; no erasure guarantee for previously viewed data.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

### R-SIGNIN — `/sign-in`

- **Purpose:** Provide a future authentication entry independent of private route existence, with a bounded safe return destination.
- **Group:** SYSTEM / PRIVATE ADMINISTRATION
- **User role:** unauthenticated visitor; authenticated user returning to session flow
- **Entry points:** initial access; generic protected-route response; session expiry
- **Exit points:** R-CATALOGUE; authorized same-origin return destination
- **Child components:** authentication form placeholder; accessible validation/status; safe return navigation; generic failure
- **Available data:** No private catalogue, counts, source identity, vocabulary, collection data or prefetch. Only safe authentication UI state.
- **Unavailable features:** Authentication/page unimplemented; No provider/credential flow chosen; No anonymous private browsing or permission grant from successful authentication alone
- **Security constraints:** Authentication entry only; no protected data before authentication. Successful sign-in does not grant object access or choose a PostgreSQL identity from browser input.
- **Logical interfaces:** IF-AUTH-SESSION-1
- **Dependencies:** C-UI-SHELL; C-UI-PAGES; C-TRANSPORT; C-DTO; C-AUTHN; C-AUTHZ
- **Acceptance criteria (future; NOT RUN):**
  - `UAT-SIGNIN-01`: Unauthenticated shell performs no protected suggestions/counts/prefetch.
  - `UAT-SIGNIN-02`: Errors do not reveal account/private-object existence; return target is same-origin and reauthorized.
- **Status:** PROPOSED; no page, UI handler or application API implemented by this task.

## User journeys and failure exits

| Journey | Route/page steps and intended events | Gate and failure exit | Future acceptance |
|---|---|---|---|
| Discover a known perfume | R-SIGNIN, R-CATALOGUE search/filter, R-DETAIL exact edition, R-PYRAMID, note-chip return | Every read reauthorizes; unknown layering stays general; denial returns generic permitted navigation | UAT-JOURNEY-DISCOVER, NOT RUN |
| Reference matching | R-DETAIL Find similar or independent R-MATCH A, choose reference, explicit submit, R-RESULTS, R-COMPARE | Capability before execution; current real matching unavailable; never synthetic substitute | UAT-JOURNEY-A, NOT RUN |
| Build notes profile | R-MATCH B1, select canonical notes, must/prefer/exclude and layer/Any Layer, validate; historical all/any/minimum alternatives remain disabled pending an exact future method contract | Accepted B1 required-all remains exact; reject contradiction/bounds; incomplete domains cannot prove absence; no accepted real method means unavailable | UAT-JOURNEY-B1, NOT RUN |
| Build accords preference | R-MATCH B2, add/remove, slider or numeric preference, review local draft, explicit submit | User preference is not candidate measured intensity; observed compatible scale and presence-only partitions remain distinct; B2 unavailable | UAT-JOURNEY-B2, NOT RUN |
| Compare factual profiles | Select two permitted real profiles, R-COMPARE, swap/change candidate, inspect facts/evidence, save alternative | Both profiles/fields authorize independently; valid factual comparison does not require a score | UAT-JOURNEY-COMPARE, NOT RUN |
| Bookmark and manual purchase | R-DETAIL/RESULTS/COMPARE save, R-CART add source/notes/observed price, external browser link; user separately records Ordered, purchase history and physical bottle receipt through explicit forms | No commerce API/server URL fetch; click/status does not create order/history/bottle; purchase-history fields use IF-PURCHASE-RECORD-WRITE-1 independently from status/inventory writes | UAT-JOURNEY-CART, NOT RUN |
| Bottle and retained history | R-CART receipt, R-COLLECTION, R-COLLECTION-ITEM edit remaining level/Finished/Sold/Gifted, R-DASHBOARD | Purchase history survives bottle disposal; distinct repeat acquisitions, optional fields and aggregate coverage retained | UAT-JOURNEY-COLLECTION, NOT RUN |
| Review source or asset proposal | Role-filtered R-SYSTEM, R-SOURCES/R-RIGHTS-MEDIA, R-REVIEWS inspect/versioned decision, R-OPERATIONS status | No browser operator identity, network acquisition or privilege escalation; review proposal never silently grants rights/eligibility | UAT-JOURNEY-REVIEW, NOT RUN |
| Expiry, logout or offline interruption | Any page, safe session notice/R-SETTINGS logout, R-SIGNIN, new authorized journey | Cancel requests, discard stale responses and best-effort clear in-memory private state; no private offline fallback or queued writes | UAT-JOURNEY-SESSION, NOT RUN |

## Preservation and next decision

[[Post_PR27_Owner_Decision_Packet]] remains version POST27-ODP-1, SHA-256 `0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c`. General PR28 direction is not exact acceptance of A–I; A/B/I remain unapproved and IMP-ENR-01 is not started. Exact synthetic M1/B1 contracts remain synthetic-only. This amendment changes no 44 holds, 43 normalization proposals, Khamrah conflicts or eligibility; PR8 remains blocked.

Owner review should accept or amend this unified IA, conservative private state behavior and future page grouping alongside the architecture packet. No choice launches authentication, real matching, private CRUD, public sharing, source/media intake or offline storage. A later approved implementation slice must establish genuine nonadmin identity, rights-safe projections and transport acceptance before any page is connected.
