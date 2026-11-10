CREATE TABLE dpt.brand_aliases (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    brand_id uuid NOT NULL,
    alias dpt.nonempty NOT NULL,
    normalized_alias dpt.nonempty NOT NULL,
    language dpt.nonempty NOT NULL,
    source_record_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT brand_aliases_pkey PRIMARY KEY (id),
    CONSTRAINT brand_aliases_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT brand_aliases_k1 UNIQUE(access_scope_id,brand_id,normalized_alias,language)
);

CREATE INDEX brand_aliases_lookup ON dpt.brand_aliases(normalized_alias,language);

CREATE TABLE dpt.note_aliases (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    note_id uuid NOT NULL,
    alias dpt.nonempty NOT NULL,
    normalized_alias dpt.nonempty NOT NULL,
    language dpt.nonempty NOT NULL,
    source_record_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT note_aliases_pkey PRIMARY KEY (id),
    CONSTRAINT note_aliases_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT note_aliases_k1 UNIQUE(access_scope_id,note_id,normalized_alias,language)
);

CREATE INDEX note_aliases_lookup ON dpt.note_aliases(normalized_alias,language);

CREATE TABLE dpt.brand_tag_links (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    brand_id uuid NOT NULL,
    tag_id uuid NOT NULL,
    source_record_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT brand_tag_links_pkey PRIMARY KEY (id),
    CONSTRAINT brand_tag_links_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT brand_tag_links_k1 UNIQUE(access_scope_id,brand_id,tag_id)
);

CREATE TABLE dpt.perfume_notes (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    perfume_id uuid NOT NULL,
    note_id uuid NOT NULL,
    layer text NOT NULL,
    sort_order smallint,
    source_record_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT perfume_notes_pkey PRIMARY KEY (id),
    CONSTRAINT perfume_notes_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT perfume_notes_k1 UNIQUE(access_scope_id,perfume_id,note_id,layer),
    CONSTRAINT perfume_notes_k2 CHECK(layer IN ('top','heart','base','general')),
    CONSTRAINT perfume_notes_k3 CHECK(sort_order IS NULL OR sort_order>=0)
);

CREATE TABLE dpt.perfume_accords (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    perfume_id uuid NOT NULL,
    accord_id uuid NOT NULL,
    strength numeric(6,5),
    source_record_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT perfume_accords_pkey PRIMARY KEY (id),
    CONSTRAINT perfume_accords_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT perfume_accords_k1 UNIQUE(access_scope_id,perfume_id,accord_id),
    CONSTRAINT perfume_accords_k2 CHECK(strength IS NULL OR strength BETWEEN 0 AND 1)
);

CREATE TABLE dpt.perfume_families (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    perfume_id uuid NOT NULL,
    family_id uuid NOT NULL,
    role text NOT NULL,
    source_record_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT perfume_families_pkey PRIMARY KEY (id),
    CONSTRAINT perfume_families_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT perfume_families_k1 UNIQUE(access_scope_id,perfume_id,family_id,role),
    CONSTRAINT perfume_families_k2 CHECK(role IN ('primary','secondary'))
);

CREATE TABLE dpt.perfume_usage_tags (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    perfume_id uuid NOT NULL,
    category text NOT NULL,
    label dpt.nonempty NOT NULL,
    scheme dpt.nonempty NOT NULL,
    source_record_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT perfume_usage_tags_pkey PRIMARY KEY (id),
    CONSTRAINT perfume_usage_tags_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT perfume_usage_tags_k1 UNIQUE(access_scope_id,perfume_id,category,scheme,label),
    CONSTRAINT perfume_usage_tags_k2 CHECK(category IN ('season','time','occasion'))
);

CREATE TABLE dpt.image_assets (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'image' CONSTRAINT image_assets_kind CHECK (entity_kind='image'),
    source_id uuid NOT NULL,
    source_record_id uuid NOT NULL,
    rights_id uuid NOT NULL,
    asset_permission_id uuid,
    source_page_url dpt.nonempty NOT NULL,
    original_url text,
    creator text,
    attribution text,
    alt_text text,
    state text NOT NULL,
    provider text,
    bucket text,
    object_key text,
    mime_type text,
    byte_size bigint,
    width integer,
    height integer,
    sha256 dpt.sha256,
    parent_asset_id uuid,
    transform_spec jsonb,
    acquired_at timestamptz,
    checked_at timestamptz NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT image_assets_pkey PRIMARY KEY (id),
    CONSTRAINT image_assets_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT image_assets_k1 UNIQUE(access_scope_id,id,source_id,source_record_id),
    CONSTRAINT image_assets_k2 CHECK(state IN ('reference_only','rights_pending','acquired','validated','rejected','archived')),
    CONSTRAINT image_assets_k3 CHECK(parent_asset_id IS NULL OR parent_asset_id<>id),
    CONSTRAINT image_assets_k4 CHECK(state NOT IN ('acquired','validated') OR (asset_permission_id IS NOT NULL AND provider IS NOT NULL AND btrim(provider)<>'' AND bucket IS NOT NULL AND btrim(bucket)<>'' AND object_key IS NOT NULL AND btrim(object_key)<>'' AND mime_type IS NOT NULL AND mime_type IN ('image/jpeg','image/png','image/webp','image/avif') AND byte_size>0 AND byte_size IS NOT NULL AND width>0 AND width IS NOT NULL AND height>0 AND height IS NOT NULL AND sha256 IS NOT NULL AND acquired_at IS NOT NULL AND attribution IS NOT NULL AND btrim(attribution)<>'')),
    CONSTRAINT image_assets_k5 CHECK(byte_size IS NULL OR byte_size>0),
    CONSTRAINT image_assets_k6 CHECK(width IS NULL OR width>0),
    CONSTRAINT image_assets_k7 CHECK(height IS NULL OR height>0)
);

CREATE UNIQUE INDEX image_assets_object_locator ON dpt.image_assets(provider,bucket,object_key) WHERE object_key IS NOT NULL;

CREATE TABLE dpt.asset_permissions (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    asset_id uuid NOT NULL,
    source_id uuid NOT NULL,
    source_record_id uuid NOT NULL,
    rights_id uuid NOT NULL,
    asset_locator dpt.nonempty NOT NULL,
    content_sha256 dpt.sha256,
    permission_kind text NOT NULL,
    acquire_use dpt.use_state NOT NULL,
    display_use dpt.use_state NOT NULL,
    transform_use dpt.use_state NOT NULL,
    redistribution_use dpt.use_state NOT NULL,
    evidence_locator dpt.nonempty NOT NULL,
    output_license text,
    parent_asset_id uuid,
    parent_permission_id uuid,
    reviewer dpt.nonempty NOT NULL,
    checked_at timestamptz NOT NULL,
    review_after timestamptz,
    revoked_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT asset_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT asset_permissions_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT asset_permissions_k1 UNIQUE(access_scope_id,asset_id,source_id,source_record_id,rights_id,id),
    CONSTRAINT asset_permissions_k2 UNIQUE(access_scope_id,asset_id,id),
    CONSTRAINT asset_permissions_k3 CHECK((permission_kind='original' AND parent_asset_id IS NULL AND parent_permission_id IS NULL) OR (permission_kind='derivative' AND parent_asset_id IS NOT NULL AND parent_permission_id IS NOT NULL)),
    CONSTRAINT asset_permissions_k4 CHECK(review_after IS NULL OR review_after>checked_at),
    CONSTRAINT asset_permissions_k5 CHECK(revoked_at IS NULL OR revoked_at>=checked_at)
);

CREATE TABLE dpt.perfume_images (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    perfume_id uuid NOT NULL,
    asset_id uuid NOT NULL,
    role text NOT NULL,
    sort_order smallint NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT perfume_images_pkey PRIMARY KEY (id),
    CONSTRAINT perfume_images_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT perfume_images_k1 UNIQUE(access_scope_id,perfume_id,asset_id,role),
    CONSTRAINT perfume_images_k2 CHECK(role IN ('bottle','packaging','other')),
    CONSTRAINT perfume_images_k3 CHECK(sort_order>=0)
);

CREATE TABLE dpt.note_images (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    note_id uuid NOT NULL,
    asset_id uuid NOT NULL,
    role text NOT NULL,
    sort_order smallint NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT note_images_pkey PRIMARY KEY (id),
    CONSTRAINT note_images_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT note_images_k1 UNIQUE(access_scope_id,note_id,asset_id,role),
    CONSTRAINT note_images_k2 CHECK(role IN ('illustration')),
    CONSTRAINT note_images_k3 CHECK(sort_order>=0)
);

CREATE TABLE dpt.comparison_evidence (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    relation_id uuid NOT NULL,
    source_record_id uuid NOT NULL,
    claim_type dpt.nonempty NOT NULL,
    summary text,
    excerpt text,
    author text,
    published_at date,
    independence_group text,
    reported_similarity numeric(5,2),
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT comparison_evidence_pkey PRIMARY KEY (id),
    CONSTRAINT comparison_evidence_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT comparison_evidence_k1 CHECK(reported_similarity IS NULL OR reported_similarity BETWEEN 0 AND 100)
);

CREATE TABLE dpt.rating_observations (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    perfume_id uuid NOT NULL,
    source_record_id uuid NOT NULL,
    value numeric(10,4),
    scale_min numeric(10,4),
    scale_max numeric(10,4),
    rating_count integer,
    observed_at timestamptz NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT rating_observations_pkey PRIMARY KEY (id),
    CONSTRAINT rating_observations_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT rating_observations_k1 CHECK(rating_count IS NULL OR rating_count>=0),
    CONSTRAINT rating_observations_k2 CHECK((scale_min IS NULL AND scale_max IS NULL AND value IS NULL) OR (scale_min IS NOT NULL AND scale_max IS NOT NULL AND scale_max>scale_min AND (value IS NULL OR value BETWEEN scale_min AND scale_max)))
);

CREATE TABLE dpt.matching_results (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    relation_id uuid NOT NULL,
    algorithm_version dpt.nonempty NOT NULL,
    input_sha256 dpt.sha256 NOT NULL,
    similarity numeric(5,2),
    confidence numeric(6,5),
    coverage jsonb NOT NULL,
    explanation jsonb NOT NULL,
    computed_at timestamptz NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT matching_results_pkey PRIMARY KEY (id),
    CONSTRAINT matching_results_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT matching_results_k1 UNIQUE(access_scope_id,relation_id,algorithm_version,input_sha256),
    CONSTRAINT matching_results_k2 CHECK(similarity IS NULL OR similarity BETWEEN 0 AND 100),
    CONSTRAINT matching_results_k3 CHECK(confidence IS NULL OR confidence BETWEEN 0 AND 1),
    CONSTRAINT matching_results_k4 CHECK(jsonb_typeof(coverage)='object' AND jsonb_typeof(explanation)='object')
);

CREATE TABLE dpt.retail_listings (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'listing' CONSTRAINT retail_listings_kind CHECK (entity_kind='listing'),
    user_id uuid NOT NULL,
    access_kind text NOT NULL DEFAULT 'user_private' CONSTRAINT retail_listings_private CHECK (access_kind='user_private'),
    perfume_id uuid NOT NULL,
    variant_id uuid,
    platform dpt.nonempty NOT NULL,
    seller_name text,
    product_url dpt.nonempty NOT NULL,
    source_record_id uuid NOT NULL,
    archived_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT retail_listings_pkey PRIMARY KEY (id),
    CONSTRAINT retail_listings_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT retail_listings_k1 UNIQUE(access_scope_id,user_id,product_url),
    CONSTRAINT retail_listings_k2 UNIQUE(user_id,perfume_id,id),
    CONSTRAINT retail_listings_k3 UNIQUE(access_scope_id,user_id,perfume_id,id)
);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_owner_id_key UNIQUE(access_scope_id,user_id,id);

CREATE TABLE dpt.price_observations (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    user_id uuid NOT NULL,
    access_kind text NOT NULL DEFAULT 'user_private' CONSTRAINT price_observations_private CHECK (access_kind='user_private'),
    listing_id uuid NOT NULL,
    source_record_id uuid NOT NULL,
    amount numeric(14,4) NOT NULL,
    currency dpt.currency_code NOT NULL,
    observed_at timestamptz NOT NULL,
    locale text,
    availability text,
    shipping_included boolean,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT price_observations_pkey PRIMARY KEY (id),
    CONSTRAINT price_observations_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT price_observations_k1 CHECK(amount>=0),
    CONSTRAINT price_observations_k2 CHECK(currency ~ '^[A-Z]{3}$')
);

ALTER TABLE dpt.price_observations ADD CONSTRAINT price_observations_owner_id_key UNIQUE(access_scope_id,user_id,id);

CREATE TABLE dpt.user_lists (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    user_id uuid NOT NULL,
    access_kind text NOT NULL DEFAULT 'user_private' CONSTRAINT user_lists_private CHECK (access_kind='user_private'),
    name dpt.nonempty NOT NULL,
    list_type text NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT user_lists_pkey PRIMARY KEY (id),
    CONSTRAINT user_lists_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT user_lists_k1 UNIQUE(user_id,id),
    CONSTRAINT user_lists_k2 CHECK(list_type IN ('cart','wishlist','custom'))
);

ALTER TABLE dpt.user_lists ADD CONSTRAINT user_lists_owner_id_key UNIQUE(access_scope_id,user_id,id);

CREATE UNIQUE INDEX user_lists_one_cart ON dpt.user_lists(access_scope_id,user_id,list_type) WHERE list_type='cart';

CREATE TABLE dpt.user_list_items (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    user_id uuid NOT NULL,
    access_kind text NOT NULL DEFAULT 'user_private' CONSTRAINT user_list_items_private CHECK (access_kind='user_private'),
    list_id uuid NOT NULL,
    perfume_id uuid NOT NULL,
    status text NOT NULL,
    notes text,
    added_at timestamptz NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT user_list_items_pkey PRIMARY KEY (id),
    CONSTRAINT user_list_items_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT user_list_items_k1 UNIQUE(access_scope_id,list_id,perfume_id),
    CONSTRAINT user_list_items_k2 UNIQUE(user_id,perfume_id,id),
    CONSTRAINT user_list_items_k3 UNIQUE(access_scope_id,user_id,perfume_id,id),
    CONSTRAINT user_list_items_k4 CHECK(status IN ('saved','ordered','received','archived'))
);

ALTER TABLE dpt.user_list_items ADD CONSTRAINT user_list_items_owner_id_key UNIQUE(access_scope_id,user_id,id);

CREATE TABLE dpt.saved_buying_sources (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    user_id uuid NOT NULL,
    access_kind text NOT NULL DEFAULT 'user_private' CONSTRAINT saved_buying_sources_private CHECK (access_kind='user_private'),
    perfume_id uuid NOT NULL,
    list_item_id uuid NOT NULL,
    listing_id uuid NOT NULL,
    user_notes text,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT saved_buying_sources_pkey PRIMARY KEY (id),
    CONSTRAINT saved_buying_sources_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT saved_buying_sources_k1 UNIQUE(access_scope_id,list_item_id,listing_id)
);

ALTER TABLE dpt.saved_buying_sources ADD CONSTRAINT saved_buying_sources_owner_id_key UNIQUE(access_scope_id,user_id,id);

CREATE TABLE dpt.purchase_records (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    user_id uuid NOT NULL,
    access_kind text NOT NULL DEFAULT 'user_private' CONSTRAINT purchase_records_private CHECK (access_kind='user_private'),
    perfume_id uuid NOT NULL,
    variant_id uuid,
    listing_id uuid,
    paid_price numeric(14,4),
    currency dpt.currency_code,
    volume_ml numeric(8,3),
    ordered_at date,
    received_at date,
    status text NOT NULL,
    notes text,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT purchase_records_pkey PRIMARY KEY (id),
    CONSTRAINT purchase_records_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT purchase_records_k1 UNIQUE(user_id,perfume_id,id),
    CONSTRAINT purchase_records_k2 UNIQUE(access_scope_id,user_id,perfume_id,id),
    CONSTRAINT purchase_records_k3 CHECK(paid_price IS NULL OR (paid_price>=0 AND currency IS NOT NULL)),
    CONSTRAINT purchase_records_k4 CHECK(currency IS NULL OR currency ~ '^[A-Z]{3}$'),
    CONSTRAINT purchase_records_k5 CHECK(volume_ml IS NULL OR volume_ml>0),
    CONSTRAINT purchase_records_k6 CHECK(received_at IS NULL OR ordered_at IS NULL OR received_at>=ordered_at),
    CONSTRAINT purchase_records_k7 CHECK(status IN ('ordered','received','cancelled','returned'))
);

ALTER TABLE dpt.purchase_records ADD CONSTRAINT purchase_records_owner_id_key UNIQUE(access_scope_id,user_id,id);

CREATE TABLE dpt.inventory_items (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    user_id uuid NOT NULL,
    access_kind text NOT NULL DEFAULT 'user_private' CONSTRAINT inventory_items_private CHECK (access_kind='user_private'),
    perfume_id uuid NOT NULL,
    variant_id uuid,
    purchase_record_id uuid,
    status text NOT NULL,
    remaining_percentage smallint,
    acquired_at date,
    finished_at date,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT inventory_items_pkey PRIMARY KEY (id),
    CONSTRAINT inventory_items_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT inventory_items_k1 CHECK(status IN ('owned','finished','sold','gifted','lost','archived')),
    CONSTRAINT inventory_items_k2 CHECK(remaining_percentage IS NULL OR remaining_percentage BETWEEN 0 AND 100),
    CONSTRAINT inventory_items_k3 CHECK(finished_at IS NULL OR acquired_at IS NULL OR finished_at>=acquired_at)
);

ALTER TABLE dpt.inventory_items ADD CONSTRAINT inventory_items_owner_id_key UNIQUE(access_scope_id,user_id,id);

ALTER TABLE dpt.brand_aliases ADD CONSTRAINT brand_aliases_fk56 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.brand_aliases ADD CONSTRAINT brand_aliases_fk57 FOREIGN KEY (brand_id) REFERENCES dpt.brands (id);

ALTER TABLE dpt.brand_aliases ADD CONSTRAINT brand_aliases_fk58 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.note_aliases ADD CONSTRAINT note_aliases_fk59 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.note_aliases ADD CONSTRAINT note_aliases_fk60 FOREIGN KEY (note_id) REFERENCES dpt.notes (id);

ALTER TABLE dpt.note_aliases ADD CONSTRAINT note_aliases_fk61 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.brand_tag_links ADD CONSTRAINT brand_tag_links_fk62 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.brand_tag_links ADD CONSTRAINT brand_tag_links_fk63 FOREIGN KEY (brand_id) REFERENCES dpt.brands (id);

ALTER TABLE dpt.brand_tag_links ADD CONSTRAINT brand_tag_links_fk64 FOREIGN KEY (tag_id) REFERENCES dpt.brand_tags (id);

ALTER TABLE dpt.brand_tag_links ADD CONSTRAINT brand_tag_links_fk65 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.perfume_notes ADD CONSTRAINT perfume_notes_fk66 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.perfume_notes ADD CONSTRAINT perfume_notes_fk67 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.perfume_notes ADD CONSTRAINT perfume_notes_fk68 FOREIGN KEY (note_id) REFERENCES dpt.notes (id);

ALTER TABLE dpt.perfume_notes ADD CONSTRAINT perfume_notes_fk69 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.perfume_accords ADD CONSTRAINT perfume_accords_fk70 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.perfume_accords ADD CONSTRAINT perfume_accords_fk71 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.perfume_accords ADD CONSTRAINT perfume_accords_fk72 FOREIGN KEY (accord_id) REFERENCES dpt.accords (id);

ALTER TABLE dpt.perfume_accords ADD CONSTRAINT perfume_accords_fk73 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.perfume_families ADD CONSTRAINT perfume_families_fk74 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.perfume_families ADD CONSTRAINT perfume_families_fk75 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.perfume_families ADD CONSTRAINT perfume_families_fk76 FOREIGN KEY (family_id) REFERENCES dpt.families (id);

ALTER TABLE dpt.perfume_families ADD CONSTRAINT perfume_families_fk77 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.perfume_usage_tags ADD CONSTRAINT perfume_usage_tags_fk78 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.perfume_usage_tags ADD CONSTRAINT perfume_usage_tags_fk79 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.perfume_usage_tags ADD CONSTRAINT perfume_usage_tags_fk80 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.image_assets ADD CONSTRAINT image_assets_fk81 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.image_assets ADD CONSTRAINT image_assets_fk82 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.image_assets ADD CONSTRAINT image_assets_fk83 FOREIGN KEY (access_scope_id,source_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,source_id,id);

ALTER TABLE dpt.image_assets ADD CONSTRAINT image_assets_fk84 FOREIGN KEY (access_scope_id,source_id,rights_id) REFERENCES dpt.rights_assessments (access_scope_id,source_id,id);

ALTER TABLE dpt.image_assets ADD CONSTRAINT image_assets_fk85 FOREIGN KEY (access_scope_id,parent_asset_id) REFERENCES dpt.image_assets (access_scope_id,id);

ALTER TABLE dpt.asset_permissions ADD CONSTRAINT asset_permissions_fk86 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.asset_permissions ADD CONSTRAINT asset_permissions_fk87 FOREIGN KEY (access_scope_id,asset_id,source_id,source_record_id) REFERENCES dpt.image_assets (access_scope_id,id,source_id,source_record_id);

ALTER TABLE dpt.asset_permissions ADD CONSTRAINT asset_permissions_fk88 FOREIGN KEY (access_scope_id,source_id,rights_id) REFERENCES dpt.rights_assessments (access_scope_id,source_id,id);

ALTER TABLE dpt.asset_permissions ADD CONSTRAINT asset_permissions_fk89 FOREIGN KEY (access_scope_id,parent_asset_id,parent_permission_id) REFERENCES dpt.asset_permissions (access_scope_id,asset_id,id);

ALTER TABLE dpt.image_assets ADD CONSTRAINT image_assets_fk90 FOREIGN KEY (access_scope_id,id,source_id,source_record_id,rights_id,asset_permission_id) REFERENCES dpt.asset_permissions (access_scope_id,asset_id,source_id,source_record_id,rights_id,id) DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE dpt.perfume_images ADD CONSTRAINT perfume_images_fk91 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.perfume_images ADD CONSTRAINT perfume_images_fk92 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.perfume_images ADD CONSTRAINT perfume_images_fk93 FOREIGN KEY (asset_id) REFERENCES dpt.image_assets (id);

ALTER TABLE dpt.note_images ADD CONSTRAINT note_images_fk94 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.note_images ADD CONSTRAINT note_images_fk95 FOREIGN KEY (note_id) REFERENCES dpt.notes (id);

ALTER TABLE dpt.note_images ADD CONSTRAINT note_images_fk96 FOREIGN KEY (asset_id) REFERENCES dpt.image_assets (id);

ALTER TABLE dpt.comparison_evidence ADD CONSTRAINT comparison_evidence_fk97 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.comparison_evidence ADD CONSTRAINT comparison_evidence_fk98 FOREIGN KEY (relation_id) REFERENCES dpt.perfume_relations (id);

ALTER TABLE dpt.comparison_evidence ADD CONSTRAINT comparison_evidence_fk99 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.rating_observations ADD CONSTRAINT rating_observations_fk100 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.rating_observations ADD CONSTRAINT rating_observations_fk101 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.rating_observations ADD CONSTRAINT rating_observations_fk102 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.matching_results ADD CONSTRAINT matching_results_fk103 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.matching_results ADD CONSTRAINT matching_results_fk104 FOREIGN KEY (relation_id) REFERENCES dpt.perfume_relations (id);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_fk105 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_fk106 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_fk107 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_fk108 FOREIGN KEY (access_scope_id,access_kind,user_id) REFERENCES dpt.access_scopes (id,kind,owner_user_id);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_fk109 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_fk110 FOREIGN KEY (perfume_id,variant_id) REFERENCES dpt.product_variants (perfume_id,id);

ALTER TABLE dpt.retail_listings ADD CONSTRAINT retail_listings_fk111 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.price_observations ADD CONSTRAINT price_observations_fk112 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.price_observations ADD CONSTRAINT price_observations_fk113 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.price_observations ADD CONSTRAINT price_observations_fk114 FOREIGN KEY (access_scope_id,access_kind,user_id) REFERENCES dpt.access_scopes (id,kind,owner_user_id);

ALTER TABLE dpt.price_observations ADD CONSTRAINT price_observations_fk115 FOREIGN KEY (access_scope_id,user_id,listing_id) REFERENCES dpt.retail_listings (access_scope_id,user_id,id);

ALTER TABLE dpt.price_observations ADD CONSTRAINT price_observations_fk116 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.user_lists ADD CONSTRAINT user_lists_fk117 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.user_lists ADD CONSTRAINT user_lists_fk118 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.user_lists ADD CONSTRAINT user_lists_fk119 FOREIGN KEY (access_scope_id,access_kind,user_id) REFERENCES dpt.access_scopes (id,kind,owner_user_id);

ALTER TABLE dpt.user_list_items ADD CONSTRAINT user_list_items_fk120 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.user_list_items ADD CONSTRAINT user_list_items_fk121 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.user_list_items ADD CONSTRAINT user_list_items_fk122 FOREIGN KEY (access_scope_id,access_kind,user_id) REFERENCES dpt.access_scopes (id,kind,owner_user_id);

ALTER TABLE dpt.user_list_items ADD CONSTRAINT user_list_items_fk123 FOREIGN KEY (access_scope_id,user_id,list_id) REFERENCES dpt.user_lists (access_scope_id,user_id,id);

ALTER TABLE dpt.user_list_items ADD CONSTRAINT user_list_items_fk124 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.saved_buying_sources ADD CONSTRAINT saved_buying_sources_fk125 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.saved_buying_sources ADD CONSTRAINT saved_buying_sources_fk126 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.saved_buying_sources ADD CONSTRAINT saved_buying_sources_fk127 FOREIGN KEY (access_scope_id,access_kind,user_id) REFERENCES dpt.access_scopes (id,kind,owner_user_id);

ALTER TABLE dpt.saved_buying_sources ADD CONSTRAINT saved_buying_sources_fk128 FOREIGN KEY (access_scope_id,user_id,perfume_id,list_item_id) REFERENCES dpt.user_list_items (access_scope_id,user_id,perfume_id,id);

ALTER TABLE dpt.saved_buying_sources ADD CONSTRAINT saved_buying_sources_fk129 FOREIGN KEY (access_scope_id,user_id,perfume_id,listing_id) REFERENCES dpt.retail_listings (access_scope_id,user_id,perfume_id,id);

ALTER TABLE dpt.purchase_records ADD CONSTRAINT purchase_records_fk130 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.purchase_records ADD CONSTRAINT purchase_records_fk131 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.purchase_records ADD CONSTRAINT purchase_records_fk132 FOREIGN KEY (access_scope_id,access_kind,user_id) REFERENCES dpt.access_scopes (id,kind,owner_user_id);

ALTER TABLE dpt.purchase_records ADD CONSTRAINT purchase_records_fk133 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.purchase_records ADD CONSTRAINT purchase_records_fk134 FOREIGN KEY (perfume_id,variant_id) REFERENCES dpt.product_variants (perfume_id,id);

ALTER TABLE dpt.purchase_records ADD CONSTRAINT purchase_records_fk135 FOREIGN KEY (access_scope_id,user_id,perfume_id,listing_id) REFERENCES dpt.retail_listings (access_scope_id,user_id,perfume_id,id);

ALTER TABLE dpt.inventory_items ADD CONSTRAINT inventory_items_fk136 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.inventory_items ADD CONSTRAINT inventory_items_fk137 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.inventory_items ADD CONSTRAINT inventory_items_fk138 FOREIGN KEY (access_scope_id,access_kind,user_id) REFERENCES dpt.access_scopes (id,kind,owner_user_id);

ALTER TABLE dpt.inventory_items ADD CONSTRAINT inventory_items_fk139 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.inventory_items ADD CONSTRAINT inventory_items_fk140 FOREIGN KEY (perfume_id,variant_id) REFERENCES dpt.product_variants (perfume_id,id);

ALTER TABLE dpt.inventory_items ADD CONSTRAINT inventory_items_fk141 FOREIGN KEY (access_scope_id,user_id,perfume_id,purchase_record_id) REFERENCES dpt.purchase_records (access_scope_id,user_id,perfume_id,id);
