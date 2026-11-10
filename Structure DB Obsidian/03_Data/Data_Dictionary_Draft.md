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

Every table has `id uuid PK` unless a composite PK is expressly listed. Entity IDs use generated UUIDv4;
UUIDs do not replace authorization. `!` means NOT NULL; `?` means nullable. Every non-key column below
has a proposed type and nullability. All tables additionally have `created_at timestamptz !`; mutable
canonical/private rows have `updated_at timestamptz !`. No raw image bytes belong in PostgreSQL.

Use `text` with nonempty checks for required names/URLs, `date` for user dates, `timestamptz` for audit
and observations, exact `numeric` for volume/money, `jsonb` only for qualified source claims/staging.
`code` fields are text with versioned lookup/CHECK domains; do not use permanent SQL enums while
vocabularies are unsettled. FK references below are real FK proposals; optional relationships stay nullable.
Foreign-key child columns receive B-tree indexes unless an existing leading index already covers them.

## Catalogue and controlled vocabularies

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `entities` | `kind text !`, `archived_at timestamptz ?` | UNIQUE(id,kind); registry for attributable entities; no polymorphic UUID without FK |
| `countries` | `code char(2) PK`, `name text !` (no UUID) | Country reference vocabulary, not inferred from manufacture |
| `brands` | `id uuid PK/FK entities`, `entity_kind text !` fixed brand, `name text !`, `slug text !`, `country_code char(2) ? FK countries.code`, `website_url text ?` | UNIQUE slug; composite FK(id,entity_kind) → entities(id,kind); index normalized name for search, no name-only identity uniqueness |
| `brand_aliases` | `brand_id uuid ! FK brands`, `alias text !`, `normalized_alias text !`, `language text !` (und when unknown), `source_record_id uuid ! FK source_records` | UNIQUE(brand_id,normalized_alias,language); nonunique lookup index(normalized_alias,language) allows ambiguity |
| `brand_tags` | `code text !`, `label text !`, `scheme text !` | UNIQUE(scheme,code); positioning distinct from country |
| `brand_tag_links` | `brand_id uuid ! FK brands`, `tag_id uuid ! FK brand_tags`, `source_record_id uuid ! FK source_records` | UNIQUE(brand_id,tag_id); only reviewed mappings |
| `perfumes` | `id uuid PK/FK entities`, `entity_kind text !` fixed perfume, `brand_id uuid ! FK brands`, `name text !`, `slug text !`, `edition_label text ?`, `concentration_code text ?`, `release_year smallint ?`, `gender_label text ?`, `description text ?`, `review_status text !`, `matching_eligible boolean !` default false | UNIQUE slug; composite entity FK; CHECK year 1000..9999 when known; index(brand_id,name); no unique brand/name/concentration with unknown edition |
| `product_variants` | `id uuid PK/FK entities`, `entity_kind text !` fixed variant, `perfume_id uuid ! FK perfumes`, `volume_ml numeric(8,3) ?`, `packaging_code text ?`, `sku text ?`, `gtin text ?` | composite entity FK; CHECK volume > 0; UNIQUE(perfume_id,id) for composite FKs; partial UNIQUE(perfume_id,sku) when SKU supplied; no uniqueness that treats unknown size as known |
| `notes` | `id uuid PK/FK entities`, `entity_kind text !` fixed note, `name text !`, `slug text !`, `name_th text ?`, `material_origin text ?`, `description text ?` | UNIQUE slug; composite entity FK; material_origin natural/synthetic/both/accord or null; name is not chemical identity |
| `note_aliases` | `note_id uuid ! FK notes`, `alias text !`, `normalized_alias text !`, `language text !`, `source_record_id uuid ! FK source_records` | UNIQUE(note_id,normalized_alias,language); ambiguity permitted across note IDs |
| `perfume_notes` | `perfume_id uuid ! FK perfumes`, `note_id uuid ! FK notes`, `layer text !`, `sort_order smallint ?`, `source_record_id uuid ! FK source_records` | UNIQUE(perfume_id,note_id,layer); layer top/heart/base/general; sort_order >= 0; index(note_id,layer,perfume_id) |
| `accords` | `id uuid PK/FK entities`, `entity_kind text !` fixed accord, `scheme text !`, `code text !`, `label text !` | UNIQUE(scheme,code); composite entity FK; distinct from note labels |
| `perfume_accords` | `perfume_id uuid ! FK perfumes`, `accord_id uuid ! FK accords`, `strength numeric(6,5) ?`, `source_record_id uuid ! FK source_records` | UNIQUE(perfume_id,accord_id); CHECK strength 0..1; null means not measured |
| `families` | `scheme text !`, `code text !`, `label text !` | UNIQUE(scheme,code); Scento taxonomy retained |
| `perfume_families` | `perfume_id uuid ! FK perfumes`, `family_id uuid ! FK families`, `role text !`, `source_record_id uuid ! FK source_records` | UNIQUE(perfume_id,family_id,role); role primary/secondary; index(family_id,perfume_id) |
| `perfume_usage_tags` | `perfume_id uuid ! FK perfumes`, `category text !`, `label text !`, `scheme text !`, `source_record_id uuid ! FK source_records` | UNIQUE(perfume_id,category,scheme,label); category season/time/occasion; source label retained |

Canonical row review_status: draft/reviewed/approved/archived. Catalogue approval does not guarantee
matching eligibility; unresolved identity/notes/rights may keep that false. Family/tag/note joins
require approved whole-field selections on the parent entity; promotion writes both atomically.
A general note means unlayered, not a fourth volatility phase. No forced synthetic synonyms.

## Sources, claims, conflicts and ingestion

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `sources` | `name text !`, `kind text !`, `entry_url text !`, `publisher text !` | kind dataset/api/official/user/media/review; private owner sources permitted |
| `rights_assessments` | `source_id uuid ! FK sources`, `scope text !`, `evidence_url text ?`, `license_code text ?`, `license_url text ?`, `terms_url text ?`, `terms_digest char(64) ?`, `research_use text !`, `automation_use text !`, `cache_use text !`, `storage_use text !`, `display_use text !`, `redistribution_use text !`, `ai_use text !`, `attribution text ?`, `checked_at timestamptz !`, `review_after timestamptz ?`, `reviewer text !`, `restrictions jsonb ?` | each use allowed/restricted/unknown; allowed requires recorded evidence/rationale; versioned append-only; index(source_id,checked_at) |
| `source_records` | `source_id uuid ! FK sources`, `external_key text !`, `payload_sha256 char(64) !`, `source_url text !`, `locator text ?`, `source_revision text ?`, `retrieved_at timestamptz !`, `rights_id uuid ! FK rights_assessments` | UNIQUE(source_id,external_key,payload_sha256); composite FK(source_id,rights_id) to same-source assessment via UNIQUE(source_id,id); index(source_id,external_key,retrieved_at) |
| `entity_source_links` | `entity_id uuid ! FK entities`, `source_record_id uuid ! FK source_records`, `review_status text !` | UNIQUE(source_record_id,entity_id); versioned crosswalk, no source ID as canonical PK |
| `field_definitions` | `entity_kind text !`, `path text !`, `value_type text !`, `mapping_version text !` | UNIQUE(entity_kind,path); allowlist paths/types, not arbitrary executable JSON paths |
| `source_observations` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `source_record_id uuid ! FK source_records`, `value jsonb ?`, `value_status text !`, `transform_version text !`, `observed_at timestamptz ?` | composite FK(entity_id,entity_kind) → entities(id,kind); FK(entity_kind,field_path) → field_definitions; UNIQUE(entity_id,entity_kind,field_path,source_record_id); UNIQUE(entity_id,entity_kind,field_path,id) for selection/member FKs |
| `canonical_selections` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `observation_id uuid !`, `reviewed_by text !`, `reviewed_at timestamptz !`, `rationale text !` | PK(entity_id,entity_kind,field_path), no UUID; composite FK(entity_id,entity_kind,field_path,observation_id) → source_observations, prevents wrong-target selection |
| `data_conflicts` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `status text !`, `resolution_observation_id uuid ?`, `resolved_by text ?`, `resolved_at timestamptz ?`, `rationale text ?` | composite FK entity/field as above; UNIQUE(entity_id,entity_kind,field_path,id); resolution FK to matching observation; resolved status requires reviewer/time/rationale; partial index unresolved status |
| `conflict_members` | `entity_id uuid !`, `entity_kind text !`, `field_path text !`, `conflict_id uuid !`, `observation_id uuid !` | PK(conflict_id,observation_id), no UUID; matching composite FKs to conflict and observation; cannot attach unrelated field/entity |
| `ingestion_batches` | `source_id uuid ! FK sources`, `rights_id uuid ! FK rights_assessments`, `source_revision text !`, `batch_sha256 char(64) !`, `adapter_version text !`, `state text !`, `started_at timestamptz !`, `finished_at timestamptz ?`, `retention_until timestamptz ?` | UNIQUE(source_id,source_revision,batch_sha256,adapter_version); same-source rights composite FK; index(state,started_at) |
| `staging_records` | `batch_id uuid ! FK ingestion_batches`, `external_key text !`, `payload_sha256 char(64) !`, `raw_payload jsonb ?`, `source_record_id uuid ? FK source_records`, `state text !`, `error_codes jsonb ?` | UNIQUE(batch_id,external_key,payload_sha256); index(batch_id,state); raw retention rights required |
| `validation_results` | `staging_record_id uuid ! FK staging_records`, `rule_code text !`, `severity text !`, `result text !`, `detail jsonb ?` | UNIQUE(staging_record_id,rule_code); index(result,severity) |
| `audit_events` | `entity_id uuid ? FK entities`, `batch_id uuid ? FK ingestion_batches`, `actor text !`, `action text !`, `before_selection jsonb ?`, `after_selection jsonb ?`, `reason text !`, `occurred_at timestamptz !` | require entity or batch; append-only, rights-aware/redacted payload; index(entity_id,occurred_at) |

`value_status` vocabulary is defined in [[Data_Quality_and_Provenance]]. Non-present values normally
have SQL NULL value; explicit_none may encode JSON null with an explicit state. Application validation
checks JSON type against field_definitions; SQL CHECK alone cannot validate other-table values.
A deferred constraint trigger in the future migration must enforce subtype completeness, canonical
selection/materialized-value consistency, same-source staging/batch links and resolved-member inclusion.
These trigger behaviors require actual tests before schema approval; they are not implied by this document.
Promotion also rejects an observation whose rights assessment does not cover that record/use.

## Images and portable object metadata

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `image_assets` | `id uuid PK/FK entities`, `entity_kind text !` fixed image, `source_record_id uuid ! FK source_records`, `rights_id uuid ! FK rights_assessments`, `source_page_url text !`, `original_url text ?`, `creator text ?`, `attribution text ?`, `alt_text text ?`, `state text !`, `provider text ?`, `bucket text ?`, `object_key text ?`, `mime_type text ?`, `byte_size bigint ?`, `width integer ?`, `height integer ?`, `sha256 char(64) ?`, `parent_asset_id uuid ? FK image_assets`, `transform_spec jsonb ?`, `acquired_at timestamptz ?`, `checked_at timestamptz !` | composite entity FK; partial UNIQUE(provider,bucket,object_key) when stored; positive size/dimensions; stored state requires locator/MIME/bytes/dimensions/hash/acquired_at and permitted image rights; parent != self |
| `perfume_images` | `perfume_id uuid ! FK perfumes`, `asset_id uuid ! FK image_assets`, `role text !`, `sort_order smallint !` | UNIQUE(perfume_id,asset_id,role); role bottle/packaging/other; sort_order >= 0 |
| `note_images` | `note_id uuid ! FK notes`, `asset_id uuid ! FK image_assets`, `role text !`, `sort_order smallint !` | UNIQUE(note_id,asset_id,role); role illustration; sort_order >= 0 |

Asset states: reference_only/rights_pending/acquired/validated/rejected/archived. Reference-only
metadata may have unknown technical fields. URL is never a storage key; signed URLs are generated,
not persisted as identifiers. SHA-256 is not necessarily the object's ETag. Hash duplicates can share
bytes only when rights/ownership permit; do not globally deduplicate private assets across tenants.
Image assessment scope must cover the individual asset, not merely the dataset publisher. Parent chains
must be acyclic (future validation). A manifest exports portable keys, hashes, MIME, dimensions, rights
and transformations separately from DB dumps.

## Relations, reviews, ratings and matching

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `perfume_relations` | `id uuid PK/FK entities`, `entity_kind text !` fixed relation, `reference_perfume_id uuid ! FK perfumes`, `candidate_perfume_id uuid ! FK perfumes`, `relation_type text !`, `directionality text !` | composite entity FK; endpoints unequal; UNIQUE(reference_perfume_id,candidate_perfume_id,relation_type); symmetric pairs sorted, directed inspired_by/flanker_of retain order |
| `comparison_evidence` | `relation_id uuid ! FK perfume_relations`, `source_record_id uuid ! FK source_records`, `claim_type text !`, `summary text ?`, `excerpt text ?`, `author text ?`, `published_at date ?`, `independence_group text ?`, `reported_similarity numeric(5,2) ?` | CHECK reported_similarity 0..100 if explicitly provided; text rights required; evidence can be URL-only when text reuse disallowed; index(relation_id,claim_type) |
| `rating_observations` | `perfume_id uuid ! FK perfumes`, `source_record_id uuid ! FK source_records`, `value numeric(10,4) ?`, `scale_min numeric(10,4) ?`, `scale_max numeric(10,4) ?`, `rating_count integer ?`, `observed_at timestamptz !` | scale_max > scale_min; value within known scale when supplied; count >= 0; no value invented from count |
| `matching_results` | `relation_id uuid ! FK perfume_relations`, `algorithm_version text !`, `input_sha256 char(64) !`, `similarity numeric(5,2) ?`, `confidence numeric(6,5) ?`, `coverage jsonb !`, `explanation jsonb !`, `computed_at timestamptz !` | UNIQUE(relation_id,algorithm_version,input_sha256); score 0..100, confidence 0..1; null scores allowed when insufficient data |

No similarity score lives on the relation itself. Recompute/version results when selected claims change.
Ratings/popularity never become pairwise similarity. A flanker link requires evidence; no family grouping
or text parser may invent ancestry. Original creation is a source claim, not a self-relation.

## Private shopping, purchase history and physical bottles

| Table | Fields beyond shared columns | Keys / constraints / indexes |
|---|---|---|
| `users` | `auth_subject text !`, `display_name text ?` | UNIQUE auth_subject; provider adapter maps auth, no dependency on Supabase auth schema in domain FKs |
| `retail_listings` | `id uuid PK/FK entities`, `entity_kind text !` fixed listing, `user_id uuid ! FK users`, `perfume_id uuid ! FK perfumes`, `variant_id uuid ?`, `platform text !`, `seller_name text ?`, `product_url text !`, `source_record_id uuid ! FK source_records`, `archived_at timestamptz ?` | composite entity FK; variant FK(perfume_id,variant_id) → product_variants(perfume_id,id), requires UNIQUE there; UNIQUE(user_id,product_url); UNIQUE(user_id,perfume_id,id) |
| `price_observations` | `listing_id uuid ! FK retail_listings`, `source_record_id uuid ! FK source_records`, `amount numeric(14,4) !`, `currency char(3) !`, `observed_at timestamptz !`, `locale text ?`, `availability text ?`, `shipping_included boolean ?` | amount >= 0; currency validated vocabulary; index(listing_id,observed_at DESC); amount/currency/time never inferred |
| `user_lists` | `user_id uuid ! FK users`, `name text !`, `list_type text !` | UNIQUE(user_id,id); partial UNIQUE(user_id,list_type) for singleton cart |
| `user_list_items` | `user_id uuid ! FK users`, `list_id uuid !`, `perfume_id uuid ! FK perfumes`, `status text !`, `notes text ?`, `added_at timestamptz !` | FK(user_id,list_id) → user_lists(user_id,id); UNIQUE(list_id,perfume_id); UNIQUE(user_id,perfume_id,id); no external checkout |
| `saved_buying_sources` | `user_id uuid !`, `perfume_id uuid !`, `list_item_id uuid !`, `listing_id uuid !`, `user_notes text ?` | matching composite FKs(user_id,perfume_id,list_item_id/listing_id) to both parents; UNIQUE(list_item_id,listing_id) |
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
