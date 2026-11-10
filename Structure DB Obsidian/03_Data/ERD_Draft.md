---
id: DPT-DAT-001
project: DoomParfum By TK
type: erd_draft
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - erd
  - schema
source_of_truth: "../../README.md"
---

# ERD Draft — P1 Proposed Relationships

PROPOSED, not final/implemented. Post-review revision: 47 logical tables (44 original plus access_scopes, scope_members and asset_permissions). Column types, nullability, composite FKs and uniqueness are defined
in [[Data_Dictionary_Draft]]. Research drivers: [[P1_Data_Profiling_Findings]] and [[P1_Data_Conflict_Matrix]].
This replaces the baseline single-source-perfume association with versioned field-level claims.
Diagrams show the logical relationships; composite ownership/type guards remain mandatory even where
the diagram uses a single edge. No database was created.

## Catalogue, identity and taxonomy

```mermaid
erDiagram
    ENTITIES ||--o| BRANDS : typed_identity
    ENTITIES ||--o| PERFUMES : typed_identity
    ENTITIES ||--o| PRODUCT_VARIANTS : typed_identity
    ENTITIES ||--o| NOTES : typed_identity
    ENTITIES ||--o| ACCORDS : typed_identity
    COUNTRIES o|--o{ BRANDS : optional_origin
    BRANDS ||--o{ BRAND_ALIASES : has
    BRANDS ||--o{ BRAND_TAG_LINKS : positioned_as
    BRAND_TAGS ||--o{ BRAND_TAG_LINKS : vocabulary
    BRANDS ||--o{ PERFUMES : publishes
    PERFUMES ||--o{ PRODUCT_VARIANTS : packaged_as
    NOTES ||--o{ NOTE_ALIASES : has
    PERFUMES ||--o{ PERFUME_NOTES : declares
    NOTES ||--o{ PERFUME_NOTES : referenced_by
    PERFUMES ||--o{ PERFUME_ACCORDS : expresses
    ACCORDS ||--o{ PERFUME_ACCORDS : vocabulary
    PERFUMES ||--o{ PERFUME_FAMILIES : classified_as
    FAMILIES ||--o{ PERFUME_FAMILIES : scheme
    PERFUMES ||--o{ PERFUME_USAGE_TAGS : usage_claim
    SOURCE_RECORDS ||--o{ PERFUME_NOTES : provenance
    SOURCE_RECORDS ||--o{ PERFUME_ACCORDS : provenance
    SOURCE_RECORDS ||--o{ PERFUME_FAMILIES : provenance
    SOURCE_RECORDS ||--o{ PERFUME_USAGE_TAGS : provenance
    SOURCE_RECORDS ||--o{ BRAND_ALIASES : provenance
    SOURCE_RECORDS ||--o{ NOTE_ALIASES : provenance
    SOURCE_RECORDS ||--o{ BRAND_TAG_LINKS : provenance
```

A PERFUME is a concentration/edition-specific scent profile; EDP and EDT can have separate notes.
A PRODUCT_VARIANT is size/packaging/SKU. Flankers/reformulations use explicit evidence-backed relations,
not inferred name parsing. Unknown concentration/edition stays unknown. Country and positioning are
separate. Flat notes use general; notes represent declarations/perceptions, not a chemical formula.

## Provenance, conflict and ingestion

```mermaid
erDiagram
    USERS o|--o{ ACCESS_SCOPES : private_or_shared_owner
    ACCESS_SCOPES ||--o{ SCOPE_MEMBERS : explicit_shared_access
    USERS ||--o{ SCOPE_MEMBERS : member
    ACCESS_SCOPES ||--o{ ENTITIES : governs
    ACCESS_SCOPES ||--o{ SOURCES : governs
    ACCESS_SCOPES ||--o{ SOURCE_RECORDS : governs
    ACCESS_SCOPES ||--o{ SOURCE_OBSERVATIONS : governs
    ACCESS_SCOPES ||--o{ CANONICAL_SELECTIONS : scoped_overlay
    ACCESS_SCOPES ||--o{ DATA_CONFLICTS : governs
    SOURCES ||--o{ RIGHTS_ASSESSMENTS : reviewed_as
    SOURCES ||--o{ SOURCE_RECORDS : publishes_versions
    RIGHTS_ASSESSMENTS ||--o{ SOURCE_RECORDS : bounds_use
    ENTITIES ||--o{ ENTITY_SOURCE_LINKS : mapped_from
    SOURCE_RECORDS ||--o{ ENTITY_SOURCE_LINKS : maps_to
    ENTITIES ||--o{ SOURCE_OBSERVATIONS : subject
    FIELD_DEFINITIONS ||--o{ SOURCE_OBSERVATIONS : typed_path
    SOURCE_RECORDS ||--o{ SOURCE_OBSERVATIONS : asserts
    SOURCE_OBSERVATIONS ||--o| CANONICAL_SELECTIONS : chosen_for_field
    ENTITIES ||--o{ DATA_CONFLICTS : has
    DATA_CONFLICTS ||--o{ CONFLICT_MEMBERS : contains
    SOURCE_OBSERVATIONS ||--o{ CONFLICT_MEMBERS : competing_claim
    SOURCE_OBSERVATIONS o|--o{ DATA_CONFLICTS : optional_resolution
    SOURCES ||--o{ INGESTION_BATCHES : acquired_in
    RIGHTS_ASSESSMENTS ||--o{ INGESTION_BATCHES : bounds_use
    INGESTION_BATCHES ||--o{ STAGING_RECORDS : contains
    SOURCE_RECORDS o|--o{ STAGING_RECORDS : linked_after_parse
    STAGING_RECORDS ||--o{ VALIDATION_RESULTS : checked_by
    ENTITIES o|--o{ AUDIT_EVENTS : changed_subject
    INGESTION_BATCHES o|--o{ AUDIT_EVENTS : import_event
```

An entity has at most one current selection per access scope and field. Public selections materialize
public catalogue data; private/shared selections are authorized overlays, never public-column updates.
Composite FKs enforce identical scope/entity/kind/path for selections, conflicts and member observations. Sources and observations are not
one-to-one with perfumes. Whole-layer lists are claims; the canonical note join derives from the
approved list selection. claim_locator + claim_key preserve structured and prose claims from the SAME
captured source record; the observation UUID uniquely identifies a chosen claim. Resolution must reference
a member of its scoped conflict. Missing status and conflict status remain separate. No facts are auto-filled.

Sources/records/observations share exact scope through composite FKs; a private observation can reference
a public catalogue entity via a visibility-compatibility trigger without publishing its source, flag or value.
Public-or-same-scope is a one-way allowed reference, never automatic access inheritance. Every scoped row
and private join follows [[Data_Dictionary_Draft#Access scope and inherited constraints — PROPOSED post-review revision]].
The scope edges above are representative; mandatory inherited scope FKs also apply to rights, staging,
audit/evidence/ratings/matching and media/link tables. RLS/access rules: [[Security_and_Privacy]].

## Media, evidence and personal records

```mermaid
erDiagram
    ENTITIES ||--o| IMAGE_ASSETS : typed_identity
    SOURCE_RECORDS ||--o{ IMAGE_ASSETS : source
    RIGHTS_ASSESSMENTS ||--o{ IMAGE_ASSETS : same_source_assessment
    ACCESS_SCOPES ||--o{ IMAGE_ASSETS : governs
    IMAGE_ASSETS ||--o{ ASSET_PERMISSIONS : exact_asset_capture
    RIGHTS_ASSESSMENTS ||--o{ ASSET_PERMISSIONS : same_source_grant
    ASSET_PERMISSIONS o|--o| IMAGE_ASSETS : selected_binding
    ASSET_PERMISSIONS o|--o{ ASSET_PERMISSIONS : parent_permission
    IMAGE_ASSETS o|--o{ IMAGE_ASSETS : derived_from
    PERFUMES ||--o{ PERFUME_IMAGES : depicted_by
    IMAGE_ASSETS ||--o{ PERFUME_IMAGES : asset
    NOTES ||--o{ NOTE_IMAGES : illustrated_by
    IMAGE_ASSETS ||--o{ NOTE_IMAGES : asset
    ENTITIES ||--o| PERFUME_RELATIONS : typed_identity
    PERFUMES ||--o{ PERFUME_RELATIONS : reference
    PERFUMES ||--o{ PERFUME_RELATIONS : candidate
    PERFUME_RELATIONS ||--o{ COMPARISON_EVIDENCE : supported_by
    SOURCE_RECORDS ||--o{ COMPARISON_EVIDENCE : provenance
    PERFUME_RELATIONS ||--o{ MATCHING_RESULTS : versioned_result
    PERFUMES ||--o{ RATING_OBSERVATIONS : rated_by_source
    SOURCE_RECORDS ||--o{ RATING_OBSERVATIONS : provenance
    ENTITIES ||--o| RETAIL_LISTINGS : typed_identity
    USERS ||--o{ RETAIL_LISTINGS : privately_saves
    PERFUMES ||--o{ RETAIL_LISTINGS : offered_at
    PRODUCT_VARIANTS o|--o{ RETAIL_LISTINGS : known_packaging
    SOURCE_RECORDS ||--o{ RETAIL_LISTINGS : provenance
    RETAIL_LISTINGS ||--o{ PRICE_OBSERVATIONS : observed_price
    SOURCE_RECORDS ||--o{ PRICE_OBSERVATIONS : provenance
    USERS ||--o{ USER_LISTS : owns
    USER_LISTS ||--o{ USER_LIST_ITEMS : contains
    PERFUMES ||--o{ USER_LIST_ITEMS : saved_perfume
    USER_LIST_ITEMS ||--o{ SAVED_BUYING_SOURCES : links
    RETAIL_LISTINGS ||--o{ SAVED_BUYING_SOURCES : source
    USERS ||--o{ PURCHASE_RECORDS : manually_records
    PERFUMES ||--o{ PURCHASE_RECORDS : purchased_profile
    PRODUCT_VARIANTS o|--o{ PURCHASE_RECORDS : known_packaging
    RETAIL_LISTINGS o|--o{ PURCHASE_RECORDS : optional_seller
    USERS ||--o{ INVENTORY_ITEMS : owns_bottle
    PERFUMES ||--o{ INVENTORY_ITEMS : scent_profile
    PRODUCT_VARIANTS o|--o{ INVENTORY_ITEMS : known_packaging
    PURCHASE_RECORDS o|--o{ INVENTORY_ITEMS : optional_purchase
```

The selected asset permission is nullable only for reference-only/rights-pending states; acquired or
validated state requires it. Composite FKs bind exact scope + image + source + source record + assessment
+ permission UUID. Parent/child derivative rights require separate validation; source/license labels are
not sufficient. Deferred validation enforces parent source/capture/scope consistency and license obligations.

All personal rows carry a user_private scope plus user_id; composite FKs prove that scope's owner and
preserve scope/owner/perfume across joins. Scope membership does not share purchases/inventory.
Private/shared image links about public perfumes remain private/shared; public image joins reject them.

Optional seller/variant/purchase links must not imply a transaction or a forced price/date/size.
Composite owner/perfume FKs prevent a saved source, purchase or bottle from linking another owner's
record or a different perfume's variant. Purchase history survives cart removal and inventory lifecycle
changes. No checkout or Shopee synchronization is proposed. Private records require authorization/RLS.

Images store portable metadata and object locators separately from the image bytes. Database backups
do not back up objects. Rating, source performance claims, pairwise review evidence and computed
similarity/confidence are distinct. Matching results are versioned and nullable when evidence is insufficient.

## Evolution and approval gate

First implementation uses reviewed migrations and a bounded local pilot; no hosted environment until
[[P1_Pilot_Implementation_Plan]] readiness evidence and owner decisions. New source adapters preserve
source-specific fields in observations before any new canonical columns are proposed. This proposal
is more detailed than the bootstrap draft but remains subject to owner schema/identity approval.
