CREATE TABLE dpt.brands (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'brand' CONSTRAINT brands_kind CHECK (entity_kind='brand'),
    name dpt.nonempty NOT NULL,
    slug dpt.nonempty NOT NULL,
    country_code char(2),
    website_url text,
    review_status dpt.review_state NOT NULL DEFAULT 'draft',
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT brands_pkey PRIMARY KEY (id),
    CONSTRAINT brands_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT brands_k1 UNIQUE(access_scope_id,slug)
);

CREATE TABLE dpt.perfumes (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'perfume' CONSTRAINT perfumes_kind CHECK (entity_kind='perfume'),
    brand_id uuid NOT NULL,
    name dpt.nonempty NOT NULL,
    slug dpt.nonempty NOT NULL,
    edition_label text,
    concentration_code text,
    release_year smallint,
    gender_label text,
    description text,
    review_status dpt.review_state NOT NULL DEFAULT 'draft',
    matching_eligible boolean NOT NULL DEFAULT false,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT perfumes_pkey PRIMARY KEY (id),
    CONSTRAINT perfumes_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT perfumes_k1 UNIQUE(access_scope_id,slug),
    CONSTRAINT perfumes_k2 CHECK(release_year IS NULL OR release_year BETWEEN 1000 AND 9999),
    CONSTRAINT perfumes_k3 CHECK(concentration_code IS NULL OR btrim(concentration_code)<>'')
);

CREATE TABLE dpt.product_variants (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'variant' CONSTRAINT product_variants_kind CHECK (entity_kind='variant'),
    perfume_id uuid NOT NULL,
    volume_ml numeric(8,3),
    packaging_code text,
    sku text,
    gtin text,
    review_status dpt.review_state NOT NULL DEFAULT 'draft',
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT product_variants_pkey PRIMARY KEY (id),
    CONSTRAINT product_variants_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT product_variants_k1 CHECK(volume_ml IS NULL OR volume_ml>0),
    CONSTRAINT product_variants_k2 UNIQUE(perfume_id,id)
);

CREATE UNIQUE INDEX product_variants_known_sku ON dpt.product_variants(access_scope_id,perfume_id,sku) WHERE sku IS NOT NULL;

CREATE TABLE dpt.notes (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'note' CONSTRAINT notes_kind CHECK (entity_kind='note'),
    name dpt.nonempty NOT NULL,
    slug dpt.nonempty NOT NULL,
    name_th text,
    material_origin text,
    description text,
    review_status dpt.review_state NOT NULL DEFAULT 'draft',
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT notes_pkey PRIMARY KEY (id),
    CONSTRAINT notes_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT notes_k1 UNIQUE(access_scope_id,slug),
    CONSTRAINT notes_k2 CHECK(material_origin IS NULL OR material_origin IN ('natural','synthetic','both','accord'))
);

CREATE TABLE dpt.accords (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'accord' CONSTRAINT accords_kind CHECK (entity_kind='accord'),
    scheme dpt.nonempty NOT NULL,
    code dpt.nonempty NOT NULL,
    label dpt.nonempty NOT NULL,
    review_status dpt.review_state NOT NULL DEFAULT 'draft',
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT accords_pkey PRIMARY KEY (id),
    CONSTRAINT accords_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT accords_k1 UNIQUE(access_scope_id,scheme,code)
);

CREATE TABLE dpt.perfume_relations (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_kind text NOT NULL DEFAULT 'relation' CONSTRAINT perfume_relations_kind CHECK (entity_kind='relation'),
    reference_perfume_id uuid NOT NULL,
    candidate_perfume_id uuid NOT NULL,
    relation_type dpt.nonempty NOT NULL,
    directionality text NOT NULL,
    review_status dpt.review_state NOT NULL DEFAULT 'draft',
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT perfume_relations_pkey PRIMARY KEY (id),
    CONSTRAINT perfume_relations_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT perfume_relations_k1 CHECK(reference_perfume_id<>candidate_perfume_id),
    CONSTRAINT perfume_relations_k2 CHECK(directionality IN ('directed','symmetric')),
    CONSTRAINT perfume_relations_k3 CHECK(directionality<>'symmetric' OR reference_perfume_id<candidate_perfume_id),
    CONSTRAINT perfume_relations_k4 UNIQUE(access_scope_id,reference_perfume_id,candidate_perfume_id,relation_type),
    CONSTRAINT perfume_relations_k5 CHECK(relation_type NOT IN ('inspired_by','flanker_of') OR directionality='directed')
);

ALTER TABLE dpt.brands ADD CONSTRAINT brands_fk5 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.brands ADD CONSTRAINT brands_fk6 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.brands ADD CONSTRAINT brands_fk7 FOREIGN KEY (country_code) REFERENCES dpt.countries (code);

ALTER TABLE dpt.perfumes ADD CONSTRAINT perfumes_fk8 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.perfumes ADD CONSTRAINT perfumes_fk9 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.perfumes ADD CONSTRAINT perfumes_fk10 FOREIGN KEY (brand_id) REFERENCES dpt.brands (id);

ALTER TABLE dpt.product_variants ADD CONSTRAINT product_variants_fk11 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.product_variants ADD CONSTRAINT product_variants_fk12 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.product_variants ADD CONSTRAINT product_variants_fk13 FOREIGN KEY (perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.notes ADD CONSTRAINT notes_fk14 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.notes ADD CONSTRAINT notes_fk15 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.accords ADD CONSTRAINT accords_fk16 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.accords ADD CONSTRAINT accords_fk17 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.perfume_relations ADD CONSTRAINT perfume_relations_fk18 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.perfume_relations ADD CONSTRAINT perfume_relations_fk19 FOREIGN KEY (access_scope_id,id,entity_kind) REFERENCES dpt.entities (access_scope_id,id,kind);

ALTER TABLE dpt.perfume_relations ADD CONSTRAINT perfume_relations_fk20 FOREIGN KEY (reference_perfume_id) REFERENCES dpt.perfumes (id);

ALTER TABLE dpt.perfume_relations ADD CONSTRAINT perfume_relations_fk21 FOREIGN KEY (candidate_perfume_id) REFERENCES dpt.perfumes (id);
