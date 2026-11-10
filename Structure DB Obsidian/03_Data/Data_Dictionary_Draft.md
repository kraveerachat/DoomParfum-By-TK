---
id: DPT-DAT-002
project: DoomParfum By TK
type: data_dictionary
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - dictionary
  - schema
source_of_truth: "../../README.md"
---

# Data Dictionary Draft — P1 Evidence-Based Proposal

PROPOSED logical PostgreSQL design, not DDL or an implemented/final schema. See [[ERD_Draft]],
[[P1_Source_to_Canonical_Mapping]], [[P1_Data_Profiling_Findings]] and [[Tech_Stack_and_ADRs]].
This revision supersedes the baseline dictionary proposal, especially mandatory country/position,
concentration on packaging, fixed THB defaults and coarse source booleans.

## Notation and shared rules

Every table has `id uuid PK` unless a composite PK is expressly listed. This post-review revision proposes 47 logical tables (44 original + access_scopes, scope_members, asset_permissions). Entity IDs use generated UUIDv4;
UUIDs do not replace authorization. `!` means NOT NULL; `?` means nullable. Every non-key column below
has a proposed type and nullability. All tables additionally have `created_at timestamptz !`; mutable
canonical/private rows have `updated_at timestamptz !`. No raw image bytes belong in PostgreSQL.

Use `text` with nonempty checks for required names/URLs, `date` for user dates, `timestamptz` for audit
and observations, exact `numeric` for volume/money, `jsonb` only for qualified source claims/staging.
`code` fields are text with versioned lookup/CHECK domains; do not use permanent SQL enums while
vocabularies are unsettled. FK references below are real FK proposals; optional relationships stay nullable.
Foreign-key child columns receive B-tree indexes unless an existing leading index already covers them.

## Access scope and inherited constraints — PROPOSED post-review revision

Every table below except `users`, `countries`, `brand_tags`, `families`, `field_definitions`,
`access_scopes` and `scope_members` additionally has `access_scope_id uuid ! FK access_scopes(id)`.
Every such table with a UUID id declares UNIQUE(access_scope_id,id). Composite-PK tables include
access_scope_id in the keys specified below. These are column/constraint declarations, not only RLS advice.
Vocabulary tables are curator-managed public data; `users` is private identity data, never public directory.

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `access_scopes` | `kind text !`, `owner_user_id uuid ? FK users` | kind public/shared/user_private; CHECK public requires null owner, shared/private requires owner; UNIQUE(id,kind,owner_user_id); one public scope (partial UNIQUE kind); one private scope per owner (partial UNIQUE owner_user_id); ownership/kind immutable |
| `scope_members` | `access_scope_id uuid ! FK access_scopes`, `user_id uuid ! FK users`, `role text !`, `revoked_at timestamptz ?` | PK(access_scope_id,user_id), no UUID; role reader/editor; shared scopes only (trigger); index(user_id,access_scope_id); scope owner administers membership, no self-enrollment |

Use the non-null scope UUID in FKs/uniqueness; do not rely on nullable user IDs to enforce public/private
keys. Parent tuples UNIQUE(access_scope_id,source_id,id) are required on rights_assessments and
source_records. Standard provenance FKs carry access_scope_id and, where relevant, source_id.
Sources, record versions, claims, conflicts, batches, permissions and audit payloads cannot change scope
in place. Visibility changes require reviewed copy/redaction with a new ID, source rights and audit trail.

Reference compatibility for catalogue targets: target scope is public OR equals the row's scope.
This cross-row predicate requires a transactionally enforced constraint trigger on all affected writes,
not a CHECK or a guess from the target's public identity. Derived provenance stays in its source scope.
A private observation may reference a public perfume; that does not publish the observation or source.
Public rows cannot reference private/shared claims/assets. Shared rows cannot reference another shared
scope or a user's private row. Personal shopping/history stays user_private and is not group-shared.

Typed entity subtypes (brands/perfumes/variants/notes/accords/images/relations/listings) additionally use
FK(access_scope_id,id,entity_kind) → entities(access_scope_id,id,kind), backed by a UNIQUE tuple there.
Links to public catalogue parents use ordinary identity FKs plus the compatibility trigger; source,
conflict, selection, asset-permission and private-owner joins use exact scoped composite FKs instead.
Row type/nullability/ownership checks must accompany FKs; RLS is independent and mandatory.

## Catalogue and controlled vocabularies

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `entities` | `kind text !`, `archived_at timestamptz ?` | UNIQUE(id,kind), UNIQUE(access_scope_id,id,kind); registry for attributable entities; no polymorphic UUID without FK |
| `countries` | `code char(2) PK`, `name text !` (no UUID) | Country reference vocabulary, not inferred from manufacture |
| `brands` | `id uuid PK/FK entities`, `entity_kind text !` fixed brand, `name text !`, `slug text !`, `country_code char(2) ? FK countries.code`, `website_url text ?` | UNIQUE(access_scope_id,slug); composite FK(id,entity_kind) → entities(id,kind); index normalized name for search, no name-only identity uniqueness |
| `brand_aliases` | `brand_id uuid ! FK brands`, `alias text !`, `normalized_alias text !`, `language text !` (und when unknown), `source_record_id uuid ! FK source_records` | UNIQUE(access_scope_id,brand_id,normalized_alias,language); nonunique lookup index(normalized_alias,language) allows ambiguity |
| `brand_tags` | `code text !`, `label text !`, `scheme text !` | UNIQUE(scheme,code); positioning distinct from country |
| `brand_tag_links` | `brand_id uuid ! FK brands`, `tag_id uuid ! FK brand_tags`, `source_record_id uuid ! FK source_records` | UNIQUE(access_scope_id,brand_id,tag_id); only reviewed mappings |
| `perfumes` | `id uuid PK/FK entities`, `entity_kind text !` fixed perfume, `brand_id uuid ! FK brands`, `name text !`, `slug text !`, `edition_label text ?`, `concentration_code text ?`, `release_year smallint ?`, `gender_label text ?`, `description text ?`, `review_status text !`, `matching_eligible boolean !` default false | UNIQUE(access_scope_id,slug); composite entity FK; CHECK year 1000..9999 when known; index(brand_id,name); no unique brand/name/concentration with unknown edition |
| `product_variants` | `id uuid PK/FK entities`, `entity_kind text !` fixed variant, `perfume_id uuid ! FK perfumes`, `volume_ml numeric(8,3) ?`, `packaging_code text ?`, `sku text ?`, `gtin text ?` | composite entity FK; CHECK volume > 0; UNIQUE(perfume_id,id) for composite FKs; partial UNIQUE(access_scope_id,perfume_id,sku) when SKU supplied; no uniqueness that treats unknown size as known |
| `notes` | `id uuid PK/FK entities`, `entity_kind text !` fixed note, `name text !`, `slug text !`, `name_th text ?`, `material_origin text ?`, `description text ?` | UNIQUE(access_scope_id,slug); composite entity FK; material_origin natural/synthetic/both/accord or null; name is not chemical identity |
| `note_aliases` | `note_id uuid ! FK notes`, `alias text !`, `normalized_alias text !`, `language text !`, `source_record_id uuid ! FK source_records` | UNIQUE(access_scope_id,note_id,normalized_alias,language); ambiguity permitted across note IDs |
| `perfume_notes` | `perfume_id uuid ! FK perfumes`, `note_id uuid ! FK notes`, `layer text !`, `sort_order smallint ?`, `source_record_id uuid ! FK source_records` | UNIQUE(access_scope_id,perfume_id,note_id,layer); layer top/heart/base/general; sort_order >= 0; index(note_id,layer,perfume_id) |
| `accords` | `id uuid PK/FK entities`, `entity_kind text !` fixed accord, `scheme text !`, `code text !`, `label text !` | UNIQUE(access_scope_id,scheme,code); composite entity FK; distinct from note labels |
| `perfume_accords` | `perfume_id uuid ! FK perfumes`, `accord_id uuid ! FK accords`, `strength numeric(6,5) ?`, `source_record_id uuid ! FK source_records` | UNIQUE(access_scope_id,perfume_id,accord_id); CHECK strength 0..1; null means not measured |
| `families` | `scheme text !`, `code text !`, `label text !` | UNIQUE(scheme,code); Scento taxonomy retained |
| `perfume_families` | `perfume_id uuid ! FK perfumes`, `family_id uuid ! FK families`, `role text !`, `source_record_id uuid ! FK source_records` | UNIQUE(access_scope_id,perfume_id,family_id,role); role primary/secondary; index(family_id,perfume_id) |
| `perfume_usage_tags` | `perfume_id uuid ! FK perfumes`, `category text !`, `label text !`, `scheme text !`, `source_record_id uuid ! FK source_records` | UNIQUE(access_scope_id,perfume_id,category,scheme,label); category season/time/occasion; source label retained |

Canonical row review_status: draft/reviewed/approved/archived. Catalogue approval does not guarantee
matching eligibility; unresolved identity/notes/rights may keep that false. Family/tag/note joins
require approved whole-field selections on the parent entity; promotion writes both atomically.
A general note means unlayered, not a fourth volatility phase. No forced synthetic synonyms.

## Sources, claims, conflicts and ingestion

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `sources` | `name text !`, `kind text !`, `entry_url text !`, `publisher text !` | inherited access_scope_id; kind dataset/api/official/user/media/review; publisher identity is not access ownership; private captures use a separate scoped source row even when publisher/URL matches public source |
| `rights_assessments` | `source_id uuid !`, `scope text !` (license content scope, not ACL), `evidence_url text ?`, `license_code text ?`, `license_url text ?`, `terms_url text ?`, `terms_digest char(64) ?`, `research_use text !`, `automation_use text !`, `cache_use text !`, `storage_use text !`, `display_use text !`, `redistribution_use text !`, `ai_use text !`, `attribution text ?`, `checked_at timestamptz !`, `review_after timestamptz ?`, `revoked_at timestamptz ?`, `reviewer text !`, `restrictions jsonb ?` | FK(access_scope_id,source_id) → sources(access_scope_id,id); UNIQUE(access_scope_id,source_id,id); uses allowed/restricted/unknown; evidence required before allowed; content versioned append-only except one-way revocation timestamp; asset-specific permission is additionally required for images |
| `source_records` | `source_id uuid !`, `external_key text !`, `payload_sha256 char(64) !`, `source_url text !`, `locator text ?` (capture-level), `source_revision text ?`, `retrieved_at timestamptz !`, `rights_id uuid !` | UNIQUE(access_scope_id,source_id,external_key,payload_sha256); UNIQUE(access_scope_id,source_id,id); FK(access_scope_id,source_id) → sources; FK(access_scope_id,source_id,rights_id) → rights_assessments(access_scope_id,source_id,id); immutable source/capture version; index(access_scope_id,source_id,external_key,retrieved_at) |
| `entity_source_links` | `entity_id uuid ! FK entities`, `source_record_id uuid !`, `review_status text !` | UNIQUE(access_scope_id,source_record_id,entity_id); FK(access_scope_id,source_record_id) → source_records; entity compatibility trigger; linking a public entity cannot widen link/source visibility |
| `field_definitions` | `entity_kind text !`, `path text !`, `value_type text !`, `mapping_version text !` | UNIQUE(entity_kind,path); allowlist paths/types, not arbitrary executable JSON paths |
| `source_observations` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `source_record_id uuid !`, `claim_locator text !`, `claim_key text !`, `value jsonb ?`, `value_status text !`, `transform_version text !`, `observed_at timestamptz ?` | FK(access_scope_id,source_record_id) → source_records; FK(entity_id,entity_kind) → entities(id,kind) plus visibility compatibility; FK(entity_kind,field_path) → field_definitions; UNIQUE(access_scope_id,source_record_id,entity_id,entity_kind,field_path,claim_locator,claim_key,transform_version); UNIQUE(access_scope_id,entity_id,entity_kind,field_path,id); CHECK btrim(claim_locator), btrim(claim_key) and btrim(transform_version) are nonempty; never unique by record/field alone |
| `canonical_selections` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `observation_id uuid !`, `reviewed_by text !`, `reviewed_at timestamptz !`, `rationale text !` | PK(access_scope_id,entity_id,entity_kind,field_path), no UUID; FK(access_scope_id,entity_id,entity_kind,field_path,observation_id) → source_observations matching UNIQUE; private/shared overlays cannot overwrite public selection; reviewer authorization and active rights validated |
| `data_conflicts` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `status text !`, `resolution_observation_id uuid ?`, `resolved_by text ?`, `resolved_at timestamptz ?`, `rationale text ?` | FK(entity_id,entity_kind) → entities(id,kind), FK(entity_kind,field_path) → field_definitions plus visibility contract; UNIQUE(access_scope_id,entity_id,entity_kind,field_path,id); scoped resolution observation FK; deferred FK(access_scope_id,id,resolution_observation_id) → conflict_members(access_scope_id,conflict_id,observation_id) guarantees selected resolution is a member; resolved requires reviewer/time/rationale/member; unresolved status index |
| `conflict_members` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `conflict_id uuid !`, `observation_id uuid !` | PK(access_scope_id,conflict_id,observation_id), no UUID; FK(access_scope_id,entity_id,entity_kind,field_path,conflict_id) → data_conflicts matching UNIQUE; FK(access_scope_id,entity_id,entity_kind,field_path,observation_id) → source_observations matching UNIQUE; distinct locators from the SAME source_record are allowed |
| `ingestion_batches` | `source_id uuid !`, `rights_id uuid !`, `source_revision text !`, `batch_sha256 char(64) !`, `adapter_version text !`, `state text !`, `started_at timestamptz !`, `finished_at timestamptz ?`, `retention_until timestamptz ?` | scoped source and assessment composite FKs; UNIQUE(access_scope_id,source_id,source_revision,batch_sha256,adapter_version); index(access_scope_id,state,started_at); raw staging restricted even for public source (service-only grant) |
| `staging_records` | `batch_id uuid ! FK ingestion_batches`, `external_key text !`, `payload_sha256 char(64) !`, `raw_payload jsonb ?`, `source_record_id uuid ? FK source_records`, `state text !`, `error_codes jsonb ?` | UNIQUE(batch_id,external_key,payload_sha256); index(batch_id,state); raw retention rights required |
| `validation_results` | `staging_record_id uuid ! FK staging_records`, `rule_code text !`, `severity text !`, `result text !`, `detail jsonb ?` | UNIQUE(access_scope_id,staging_record_id,rule_code); index(result,severity) |
| `audit_events` | `entity_id uuid ? FK entities`, `batch_id uuid ? FK ingestion_batches`, `actor text !`, `action text !`, `before_selection jsonb ?`, `after_selection jsonb ?`, `reason text !`, `occurred_at timestamptz !` | require entity or batch; append-only, rights-aware/redacted payload; index(entity_id,occurred_at) |

`value_status` vocabulary is defined in [[Data_Quality_and_Provenance]]. Non-present values normally
have SQL NULL value; explicit_none may encode JSON null with an explicit state. JSON type/rights and
cross-row visibility checks require reviewed transaction/constraint-trigger logic, not cross-table CHECKs.

### Observation identity, conflicts and selection contract

`source_records` describes a captured document/version; do not split it into fake records merely to
satisfy uniqueness. `claim_locator` locates the section/JSON pointer/row and field within that version;
`claim_key` identifies a distinct assertion occurrence within that locator (nonempty deterministic key,
for example list identity or ordinal, not the normalized value). Both are mandatory, even for one-claim
CSV cells. Adapter and locator versioning is included in transform_version. Store claims append-only;
changed capture digest or transform version creates new observations, not overwritten old claims.

Khamrah example (identifiers only, not a newly imported payload): a single captured source record can
hold field `notes.heart` at `structured/fragrance-notes/heart` + `list-1` and
`prose/product-information/heart` + `list-1`. They have different observation UUIDs even if values agree.
If a locator contains two conflicting assertions, use distinct claim_key values and queue review.
Repeated extraction of the same complete identity must be idempotent; different value/status under the
same identity is a deterministic-extraction failure, never an upsert overwrite or hash-based dedup.

Conflict membership is scoped to one entity/kind/field and can include both observations from the same
record. Every persisted conflict requires at least two distinct observation IDs (deferred count validation). Status is open/resolved/dismissed; CHECK requires resolution_observation_id non-null exactly for resolved, and resolved/dismissed require reviewer/time/nonempty rationale. Open may have a provisional canonical selection, but no resolution pointer.
A resolved observation must be a member, not merely any observation for the field. Removing a selected
member is rejected unless resolution/selection is changed atomically and audited. Canonical selection
stores observation UUID, so it unambiguously chooses a section claim. An unresolved conflict may have
an explicitly reviewed provisional selection with rationale; unresolved status remains visible and
matching eligibility remains false for the affected field/profile until the accepted matching policy.
Selection changes cannot mark a conflict resolved automatically. Resolution/selection/materialized values
and audit changes commit together; original claims survive. No automatic structured-over-prose precedence.

For a public entity, public-scope selections materialize public catalogue columns/joins. Private/shared
scope selections are overlays visible only within that scope, and do not update those columns/joins.
The owner/member API may use an authorized overlay then public fallback. Public responses/exports/search,
counts, conflict flags, confidence and caches must depend only on public-scope inputs; even revealing a
private claim's existence is prohibited. Scope must be in selection/conflict/cache keys.

Deferred constraints still enforce subtype completeness and selection/materialization consistency.
Staging/source/batch and validation/audit rows carry the same access_scope_id as their source lineage;
all raw payload access is ETL/reviewer-only. Tests for every contract are specified, not executed here.

## Images and portable object metadata

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `image_assets` | `id uuid PK/FK entities`, `entity_kind text !` fixed image, `source_id uuid !`, `source_record_id uuid !`, `rights_id uuid !`, `asset_permission_id uuid ?`, `source_page_url text !`, `original_url text ?`, `creator text ?`, `attribution text ?`, `alt_text text ?`, `state text !`, `provider text ?`, `bucket text ?`, `object_key text ?`, `mime_type text ?`, `byte_size bigint ?`, `width integer ?`, `height integer ?`, `sha256 char(64) ?`, `parent_asset_id uuid ?`, `transform_spec jsonb ?`, `acquired_at timestamptz ?`, `checked_at timestamptz !` | UNIQUE(access_scope_id,id,source_id,source_record_id); scoped typed entity FK; FK(access_scope_id,source_id,source_record_id) → source_records; FK(access_scope_id,source_id,rights_id) → rights_assessments; deferred FK(access_scope_id,id,source_id,source_record_id,rights_id,asset_permission_id) → asset_permissions matching UNIQUE; FK(access_scope_id,parent_asset_id) → image_assets; acquired/validated state requires non-null selected permission and technical metadata; global partial UNIQUE(provider,bucket,object_key) allocates physical locators privately; parent != self |
| `asset_permissions` | `asset_id uuid !`, `source_id uuid !`, `source_record_id uuid !`, `rights_id uuid !`, `asset_locator text !`, `content_sha256 char(64) ?`, `permission_kind text !`, `acquire_use text !`, `display_use text !`, `transform_use text !`, `redistribution_use text !`, `evidence_locator text !`, `output_license text ?`, `parent_asset_id uuid ?`, `parent_permission_id uuid ?`, `reviewer text !`, `checked_at timestamptz !`, `review_after timestamptz ?`, `revoked_at timestamptz ?` | FK(access_scope_id,asset_id,source_id,source_record_id) → image_assets matching UNIQUE; FK(access_scope_id,source_id,rights_id) → rights_assessments; UNIQUE(access_scope_id,asset_id,source_id,source_record_id,rights_id,id); UNIQUE(access_scope_id,asset_id,id); CHECK original kind requires both parent columns null; derivative kind requires both non-null; FK(access_scope_id,parent_asset_id,parent_permission_id) → asset_permissions(access_scope_id,asset_id,id); original/derivative kind; uses allowed/restricted/unknown; permission content immutable except one-way revocation timestamp, selected binding must pass image contract |
| `perfume_images` | `perfume_id uuid ! FK perfumes`, `asset_id uuid ! FK image_assets`, `role text !`, `sort_order smallint !` | UNIQUE(access_scope_id,perfume_id,asset_id,role); target/asset compatibility trigger; public link only public asset; role bottle/packaging/other; sort_order >= 0 |
| `note_images` | `note_id uuid ! FK notes`, `asset_id uuid ! FK image_assets`, `role text !`, `sort_order smallint !` | UNIQUE(access_scope_id,note_id,asset_id,role); target/asset compatibility trigger; role illustration; sort_order >= 0 |

Asset states: reference_only/rights_pending/acquired/validated/rejected/archived. rights_id can point
to a same-source assessment with unknown uses for metadata-only states; that is not acquisition consent.
For acquired/validated states, asset_permission_id is mandatory: the selected binding must match the
EXACT scope, image ID, source, source record and rights assessment. A tuple with null permission cannot
bypass state checks. Asset-specific evidence must identify asset_locator and, once known, the image
hash; these are verified against source locator/bytes by validation before storage/display. For acquired/validated state, selected permission content_sha256 must be non-null and equal image sha256; a hash unknown before acquisition is finalized through a new permission version before that state transition. Being the
same publisher is insufficient. URLs/object keys/license labels alone are not permission proof.

Derivatives have new image IDs/hashes and their own selected permission binding. This pilot requires
same scope, source and captured source record as the parent (no implicit scope widening or source
substitution). Parent binding must authorize transformation and equal the parent image current selected permission at validation; child binding must reference that exact
parent asset/permission and match image_assets.parent_asset_id. Output license, attribution and intended
acquire/display/redistribution must satisfy parent obligations AND child assessment; denial/unknown on
either side blocks the requested use. Revalidate ancestors (acyclic) and expiry/revocation when selecting,
fetching, transforming and issuing an object URL. Later change-of-source or cross-scope derivatives need
an explicit reviewed copy/provenance proposal; do not silently relax these pilot constraints.

The tuple FKs enforce relationship identity; deferred trigger/transaction validation enforces per-use
rights, evidence/locator/hash applicability, parent lineage, expiry and output license compatibility.
A human assesses whether the evidence genuinely grants permission; SQL cannot establish copyright truth.
Revocation timestamps disable future use and invalidate related caches without rewriting grant evidence. Image scope/source/capture identity is immutable; changed bytes/capture use a new image ID. Parent-selected-permission changes invalidate descendants pending re-review. Source/rights/asset changes cannot leave an acquired asset with an unrelated/stale binding; disable use
and queue review. Restore validates this contract again before serving any asset.

Reference-only metadata may lack technical fields. Signed URLs are generated, not identities; storage
paths include scope and asset UUID, buckets are private by default, and no cross-scope hash dedup or
existence API is exposed. Global physical-locator uniqueness is allocated by trusted storage code with
generic failure responses, not exposed as an oracle. Manifests preserve scope, selected permission,
parent lineage and bytes separately from DB dumps; private manifests never enter public Git.

## Relations, reviews, ratings and matching

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `perfume_relations` | `id uuid PK/FK entities`, `entity_kind text !` fixed relation, `reference_perfume_id uuid ! FK perfumes`, `candidate_perfume_id uuid ! FK perfumes`, `relation_type text !`, `directionality text !` | composite entity FK; endpoints unequal; UNIQUE(access_scope_id,reference_perfume_id,candidate_perfume_id,relation_type); symmetric pairs sorted, directed inspired_by/flanker_of retain order |
| `comparison_evidence` | `relation_id uuid ! FK perfume_relations`, `source_record_id uuid ! FK source_records`, `claim_type text !`, `summary text ?`, `excerpt text ?`, `author text ?`, `published_at date ?`, `independence_group text ?`, `reported_similarity numeric(5,2) ?` | CHECK reported_similarity 0..100 if explicitly provided; text rights required; evidence can be URL-only when text reuse disallowed; index(relation_id,claim_type) |
| `rating_observations` | `perfume_id uuid ! FK perfumes`, `source_record_id uuid ! FK source_records`, `value numeric(10,4) ?`, `scale_min numeric(10,4) ?`, `scale_max numeric(10,4) ?`, `rating_count integer ?`, `observed_at timestamptz !` | scale_max > scale_min; value within known scale when supplied; count >= 0; no value invented from count |
| `matching_results` | `relation_id uuid ! FK perfume_relations`, `algorithm_version text !`, `input_sha256 char(64) !`, `similarity numeric(5,2) ?`, `confidence numeric(6,5) ?`, `coverage jsonb !`, `explanation jsonb !`, `computed_at timestamptz !` | UNIQUE(access_scope_id,relation_id,algorithm_version,input_sha256); score 0..100, confidence 0..1; null scores allowed when insufficient data |

No similarity score lives on the relation itself. Recompute/version results when selected claims change.
Ratings/popularity never become pairwise similarity. A flanker link requires evidence; no family grouping
or text parser may invent ancestry. Original creation is a source claim, not a self-relation.

## Private shopping, purchase history and physical bottles

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `users` | `auth_subject text !`, `display_name text ?` | UNIQUE auth_subject; provider adapter maps auth, no dependency on Supabase auth schema in domain FKs |
| `retail_listings` | `id uuid PK/FK entities`, `entity_kind text !` fixed listing, `user_id uuid ! FK users`, `perfume_id uuid ! FK perfumes`, `variant_id uuid ?`, `platform text !`, `seller_name text ?`, `product_url text !`, `source_record_id uuid ! FK source_records`, `archived_at timestamptz ?` | composite entity FK; variant FK(perfume_id,variant_id) → product_variants(perfume_id,id), requires UNIQUE there; UNIQUE(access_scope_id,user_id,product_url); UNIQUE(user_id,perfume_id,id) |
| `price_observations` | `listing_id uuid ! FK retail_listings`, `source_record_id uuid ! FK source_records`, `amount numeric(14,4) !`, `currency char(3) !`, `observed_at timestamptz !`, `locale text ?`, `availability text ?`, `shipping_included boolean ?` | amount >= 0; currency validated vocabulary; index(listing_id,observed_at DESC); amount/currency/time never inferred |
| `user_lists` | `user_id uuid ! FK users`, `name text !`, `list_type text !` | UNIQUE(user_id,id); partial UNIQUE(access_scope_id,user_id,list_type) for singleton cart |
| `user_list_items` | `user_id uuid ! FK users`, `list_id uuid !`, `perfume_id uuid ! FK perfumes`, `status text !`, `notes text ?`, `added_at timestamptz !` | FK(user_id,list_id) → user_lists(user_id,id); UNIQUE(access_scope_id,list_id,perfume_id); UNIQUE(user_id,perfume_id,id); no external checkout |
| `saved_buying_sources` | `user_id uuid !`, `perfume_id uuid !`, `list_item_id uuid !`, `listing_id uuid !`, `user_notes text ?` | matching composite FKs(user_id,perfume_id,list_item_id/listing_id) to both parents; UNIQUE(access_scope_id,list_item_id,listing_id) |
| `purchase_records` | `user_id uuid ! FK users`, `perfume_id uuid ! FK perfumes`, `variant_id uuid ?`, `listing_id uuid ?`, `paid_price numeric(14,4) ?`, `currency char(3) ?`, `volume_ml numeric(8,3) ?`, `ordered_at date ?`, `received_at date ?`, `status text !`, `notes text ?` | variant/perfume composite FK; owner/perfume/listing composite FK; UNIQUE(user_id,perfume_id,id); amount >= 0 with currency if amount present; volume > 0; receipt >= order when both known; multiple same perfume purchases allowed |
| `inventory_items` | `user_id uuid ! FK users`, `perfume_id uuid ! FK perfumes`, `variant_id uuid ?`, `purchase_record_id uuid ?`, `status text !`, `remaining_percentage smallint ?`, `acquired_at date ?`, `finished_at date ?` | variant/perfume composite FK; FK(user_id,perfume_id,purchase_record_id) → purchase_records(user_id,perfume_id,id); percentage 0..100; finish >= acquired when known; gift can lack purchase |

Retail listing unknown size does not block a bookmark. Purchase seller, price, volume and dates remain
optional; currency cannot default to THB if unknown. A listing's latest observation never overwrites
historical paid price. Manual receipt must be idempotent and may create one or more physical bottles;
units/pack handling remains an owner decision before P3 implementation. Cart deletion or finished/sold/
gifted inventory must never cascade-delete purchases. Archive referenced catalogue/listing rows.
Restrict parent deletion for historical FKs; cascade only disposable joins/staging under approved retention.
Tenant ownership applies to listings, prices, lists, saved sources, purchases, inventory, associated
source records/assets and evidence. Server authorization plus database RLS/private schema must prevent
cross-user reads/writes; test both. Public catalogue provenance must not expose private source locators.

## Ownership/FK/RLS enforcement ledger

All personal tables (retail_listings, price_observations, user_lists, user_list_items,
saved_buying_sources, purchase_records, inventory_items) inherit access_scope_id and additionally
`access_kind text !` fixed user_private and `user_id uuid ! FK users` (already-listed user_id is reused).
FK(access_scope_id,access_kind,user_id) → access_scopes(id,kind,owner_user_id) prevents assigning another
owner's private scope. Add UNIQUE(access_scope_id,user_id,id) on each personal UUID table and
UNIQUE(access_scope_id,user_id,perfume_id,id) on listings/list items/purchases. Extend the displayed
owner/perfume/listing/list/purchase FKs with access_scope_id; use them on price and saved-source joins.
Personal source_record_id references use FK(access_scope_id,source_record_id) → source_records.
A public listing URL saved by two users is two private source captures/listings, not global URL dedup.
Variants/catalogue targets remain public-or-same-scope and perfume-compatible. No personal record is
made shared merely because a group member can read its referenced public perfume.

All other source_record_id provenance FKs in table rows carry access_scope_id. Validation results
reference same-scope staging, audit batch refs same-scope batches, and each source-backed rating/evidence
row uses same-scope source records plus compatible catalogue targets. Scope applies also to matching
results; public computations use only public inputs, and cache/input identity includes scope and policy
version. Natural unique keys for scoped associations include access_scope_id, including overlays about public parents; a public parent ID alone never proves the child scope. Redundant UUID-parent reference tuples remain for the named composite FKs.

Public sanitized projections/column grants exclude raw payloads and sensitive permission evidence; row-level scope checks alone do not hide columns. No anonymous full-row table access. RLS proposed on every scoped/identity/personal table: SELECT requires allowed scope and row class;
INSERT/UPDATE use WITH CHECK for both old/new ownership and references; DELETE requires writer role
and history/retention rules. Public metadata/approved catalogue may be read publicly; public raw staging,
permission evidence secrets and raw snapshots remain service-only. Shared needs owner/active membership;
private needs exact owner, not catalogue read permission. Shared membership gives no write access to
public rows and no permission to change ACLs/source ownership. Public changes require curator/reviewer;
private writes require owner; shared edits require editor/owner. No user-controlled scope header/JWT claim
without server-verified auth_subject→user and authorized scope lookup.

Runtime DB roles are non-owner/non-superuser without BYPASSRLS; enable RLS and test FORCE RLS for
owners where applicable. Migration/admin/backup roles are isolated from application requests; no generic
service-role API accepting arbitrary IDs. Scope-aware views/search/evidence endpoints/exports/signed-URL
issuance authorize independently and avoid definer-view/RLS bypass. FK/unique checks do not enforce
read privacy and can expose existence through errors; revoke untrusted arbitrary SQL/table writes,
authorize references before trusted writes, return uniform not-found/denied responses, and test both
API and runtime roles. Storage remains a separate authorization boundary. Full rules:
[[Security_and_Privacy]]. Shared-mode activation is deferred until its tests and owner approval.

## Indexes, portability and migration readiness

Use unique indexes for explicit keys, B-tree FK/owner/time indexes above, and add pg_trgm/GIN search
only after EXPLAIN and size measurements justify it. Do not index every JSONB payload. Do not enforce
brand/name or name-only note identity by fuzzy normalization. PostgreSQL unique null semantics require
explicit partial predicates where intended; do not assume null values collapse.

Review SQL migrations in a future local pilot: tables and named constraints → limited sample staging →
backfill reviewed fields → validate constraints → promotion → restore rehearsal. Export migration ledger,
core schema/data, versioned rights/provenance and object manifests; rebuild provider auth/storage adapters
separately. No ORM/cloud-specific types in domain identifiers. New data sources add adapters and mapping
versions; new canonical attributes use migrations, not a rewrite of the catalogue.

Technical basis: [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html),
[logical backup](https://www.postgresql.org/docs/current/backup-dump.html). Future triggers, RLS, migration
compatibility, indexes and restore results are NOT VERIFIED by this documentation PR.
