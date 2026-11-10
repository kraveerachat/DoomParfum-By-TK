CREATE TABLE dpt.sources (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    name dpt.nonempty NOT NULL,
    kind text NOT NULL,
    entry_url dpt.nonempty NOT NULL,
    publisher dpt.nonempty NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT sources_pkey PRIMARY KEY (id),
    CONSTRAINT sources_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT sources_k1 CHECK(kind IN ('dataset','api','official','user','media','review'))
);

CREATE TABLE dpt.rights_assessments (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    source_id uuid NOT NULL,
    scope dpt.nonempty NOT NULL,
    evidence_url text,
    license_code text,
    license_url text,
    terms_url text,
    terms_digest dpt.sha256,
    research_use dpt.use_state NOT NULL,
    automation_use dpt.use_state NOT NULL,
    cache_use dpt.use_state NOT NULL,
    storage_use dpt.use_state NOT NULL,
    display_use dpt.use_state NOT NULL,
    redistribution_use dpt.use_state NOT NULL,
    ai_use dpt.use_state NOT NULL,
    attribution text,
    checked_at timestamptz NOT NULL,
    review_after timestamptz,
    revoked_at timestamptz,
    reviewer dpt.nonempty NOT NULL,
    restrictions jsonb,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT rights_assessments_pkey PRIMARY KEY (id),
    CONSTRAINT rights_assessments_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT rights_assessments_k1 UNIQUE(access_scope_id,source_id,id),
    CONSTRAINT rights_assessments_k2 CHECK(review_after IS NULL OR review_after>checked_at),
    CONSTRAINT rights_assessments_k3 CHECK(revoked_at IS NULL OR revoked_at>=checked_at),
    CONSTRAINT rights_assessments_k4 CHECK(NOT ('allowed' IN (research_use,automation_use,cache_use,storage_use,display_use,redistribution_use,ai_use)) OR (evidence_url IS NOT NULL AND btrim(evidence_url)<>''))
);

CREATE TABLE dpt.source_records (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    source_id uuid NOT NULL,
    external_key dpt.nonempty NOT NULL,
    payload_sha256 dpt.sha256 NOT NULL,
    source_url dpt.nonempty NOT NULL,
    locator text,
    source_revision text,
    retrieved_at timestamptz NOT NULL,
    rights_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT source_records_pkey PRIMARY KEY (id),
    CONSTRAINT source_records_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT source_records_k1 UNIQUE(access_scope_id,source_id,external_key,payload_sha256),
    CONSTRAINT source_records_k2 UNIQUE(access_scope_id,source_id,id)
);

CREATE TABLE dpt.entity_source_links (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_id uuid NOT NULL,
    source_record_id uuid NOT NULL,
    review_status dpt.review_state NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT entity_source_links_pkey PRIMARY KEY (id),
    CONSTRAINT entity_source_links_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT entity_source_links_k1 UNIQUE(access_scope_id,source_record_id,entity_id)
);

CREATE TABLE dpt.source_observations (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_id uuid NOT NULL,
    entity_kind text NOT NULL,
    field_path dpt.nonempty NOT NULL,
    source_record_id uuid NOT NULL,
    claim_locator dpt.nonempty NOT NULL,
    claim_key dpt.nonempty NOT NULL,
    value jsonb,
    value_status text NOT NULL,
    transform_version dpt.nonempty NOT NULL,
    observed_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT source_observations_pkey PRIMARY KEY (id),
    CONSTRAINT source_observations_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT source_observations_k1 UNIQUE(access_scope_id,source_record_id,entity_id,entity_kind,field_path,claim_locator,claim_key,transform_version),
    CONSTRAINT source_observations_k2 UNIQUE(access_scope_id,entity_id,entity_kind,field_path,id),
    CONSTRAINT source_observations_k3 CHECK(value_status IN ('present','not_recorded','not_supplied','explicit_none','withheld','not_applicable')),
    CONSTRAINT source_observations_k4 CHECK((value_status='present' AND value IS NOT NULL AND value<>'null'::jsonb) OR (value_status='explicit_none' AND (value IS NULL OR value='null'::jsonb)) OR (value_status NOT IN ('present','explicit_none') AND value IS NULL))
);

CREATE TABLE dpt.canonical_selections (
    access_scope_id uuid NOT NULL,
    entity_id uuid NOT NULL,
    entity_kind text NOT NULL,
    field_path dpt.nonempty NOT NULL,
    observation_id uuid NOT NULL,
    reviewed_by dpt.nonempty NOT NULL,
    reviewed_at timestamptz NOT NULL,
    rationale dpt.nonempty NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT canonical_selections_pkey PRIMARY KEY (access_scope_id,entity_id,entity_kind,field_path)
);

CREATE TABLE dpt.data_conflicts (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_id uuid NOT NULL,
    entity_kind text NOT NULL,
    field_path dpt.nonempty NOT NULL,
    status text NOT NULL,
    resolution_observation_id uuid,
    resolved_by text,
    resolved_at timestamptz,
    rationale text,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT data_conflicts_pkey PRIMARY KEY (id),
    CONSTRAINT data_conflicts_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT data_conflicts_k1 UNIQUE(access_scope_id,entity_id,entity_kind,field_path,id),
    CONSTRAINT data_conflicts_k2 CHECK(status IN ('open','resolved','dismissed')),
    CONSTRAINT data_conflicts_k3 CHECK((status='resolved')=(resolution_observation_id IS NOT NULL)),
    CONSTRAINT data_conflicts_k4 CHECK((status='open' AND resolved_by IS NULL AND resolved_at IS NULL) OR (status IN ('resolved','dismissed') AND resolved_by IS NOT NULL AND btrim(resolved_by)<>'' AND resolved_at IS NOT NULL AND rationale IS NOT NULL AND btrim(rationale)<>''))
);

CREATE TABLE dpt.conflict_members (
    access_scope_id uuid NOT NULL,
    entity_id uuid NOT NULL,
    entity_kind text NOT NULL,
    field_path dpt.nonempty NOT NULL,
    conflict_id uuid NOT NULL,
    observation_id uuid NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT conflict_members_pkey PRIMARY KEY (access_scope_id,conflict_id,observation_id)
);

CREATE TABLE dpt.ingestion_batches (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    source_id uuid NOT NULL,
    rights_id uuid NOT NULL,
    source_revision dpt.nonempty NOT NULL,
    batch_sha256 dpt.sha256 NOT NULL,
    adapter_version dpt.nonempty NOT NULL,
    state text NOT NULL,
    started_at timestamptz NOT NULL,
    finished_at timestamptz,
    retention_until timestamptz,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT ingestion_batches_pkey PRIMARY KEY (id),
    CONSTRAINT ingestion_batches_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT ingestion_batches_k1 UNIQUE(access_scope_id,source_id,source_revision,batch_sha256,adapter_version),
    CONSTRAINT ingestion_batches_k2 CHECK(state IN ('pending','validating','review','quarantined','completed','failed')),
    CONSTRAINT ingestion_batches_k3 CHECK(finished_at IS NULL OR finished_at>=started_at)
);

CREATE TABLE dpt.staging_records (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    batch_id uuid NOT NULL,
    external_key dpt.nonempty NOT NULL,
    payload_sha256 dpt.sha256 NOT NULL,
    raw_payload jsonb,
    source_record_id uuid,
    state text NOT NULL,
    error_codes jsonb,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT staging_records_pkey PRIMARY KEY (id),
    CONSTRAINT staging_records_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT staging_records_k1 UNIQUE(batch_id,external_key,payload_sha256),
    CONSTRAINT staging_records_k2 CHECK(state IN ('pending','validating','review','quarantined','promoted','rejected')),
    CONSTRAINT staging_records_k3 CHECK(state NOT IN ('review','quarantined','rejected') OR (error_codes IS NOT NULL AND jsonb_typeof(error_codes)='array' AND jsonb_array_length(error_codes)>0))
);

CREATE TABLE dpt.validation_results (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    staging_record_id uuid NOT NULL,
    rule_code dpt.nonempty NOT NULL,
    severity text NOT NULL,
    result text NOT NULL,
    detail jsonb,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT validation_results_pkey PRIMARY KEY (id),
    CONSTRAINT validation_results_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT validation_results_k1 UNIQUE(access_scope_id,staging_record_id,rule_code),
    CONSTRAINT validation_results_k2 CHECK(severity IN ('info','warning','error')),
    CONSTRAINT validation_results_k3 CHECK(result IN ('pass','fail','review','not_run'))
);

CREATE TABLE dpt.audit_events (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    entity_id uuid,
    batch_id uuid,
    actor dpt.nonempty NOT NULL,
    action dpt.nonempty NOT NULL,
    before_selection jsonb,
    after_selection jsonb,
    reason dpt.nonempty NOT NULL,
    occurred_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT audit_events_pkey PRIMARY KEY (id),
    CONSTRAINT audit_events_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT audit_events_k1 CHECK(entity_id IS NOT NULL OR batch_id IS NOT NULL)
);

ALTER TABLE dpt.sources ADD CONSTRAINT sources_fk22 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.rights_assessments ADD CONSTRAINT rights_assessments_fk23 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.rights_assessments ADD CONSTRAINT rights_assessments_fk24 FOREIGN KEY (access_scope_id,source_id) REFERENCES dpt.sources (access_scope_id,id);

ALTER TABLE dpt.source_records ADD CONSTRAINT source_records_fk25 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.source_records ADD CONSTRAINT source_records_fk26 FOREIGN KEY (access_scope_id,source_id) REFERENCES dpt.sources (access_scope_id,id);

ALTER TABLE dpt.source_records ADD CONSTRAINT source_records_fk27 FOREIGN KEY (access_scope_id,source_id,rights_id) REFERENCES dpt.rights_assessments (access_scope_id,source_id,id);

ALTER TABLE dpt.entity_source_links ADD CONSTRAINT entity_source_links_fk28 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.entity_source_links ADD CONSTRAINT entity_source_links_fk29 FOREIGN KEY (entity_id) REFERENCES dpt.entities (id);

ALTER TABLE dpt.entity_source_links ADD CONSTRAINT entity_source_links_fk30 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.source_observations ADD CONSTRAINT source_observations_fk31 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.source_observations ADD CONSTRAINT source_observations_fk32 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.source_observations ADD CONSTRAINT source_observations_fk33 FOREIGN KEY (entity_id,entity_kind) REFERENCES dpt.entities (id,kind);

ALTER TABLE dpt.source_observations ADD CONSTRAINT source_observations_fk34 FOREIGN KEY (entity_kind,field_path) REFERENCES dpt.field_definitions (entity_kind,path);

ALTER TABLE dpt.canonical_selections ADD CONSTRAINT canonical_selections_fk35 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.canonical_selections ADD CONSTRAINT canonical_selections_fk36 FOREIGN KEY (access_scope_id,entity_id,entity_kind,field_path,observation_id) REFERENCES dpt.source_observations (access_scope_id,entity_id,entity_kind,field_path,id);

ALTER TABLE dpt.data_conflicts ADD CONSTRAINT data_conflicts_fk37 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.data_conflicts ADD CONSTRAINT data_conflicts_fk38 FOREIGN KEY (entity_id,entity_kind) REFERENCES dpt.entities (id,kind);

ALTER TABLE dpt.data_conflicts ADD CONSTRAINT data_conflicts_fk39 FOREIGN KEY (entity_kind,field_path) REFERENCES dpt.field_definitions (entity_kind,path);

ALTER TABLE dpt.data_conflicts ADD CONSTRAINT data_conflicts_fk40 FOREIGN KEY (access_scope_id,entity_id,entity_kind,field_path,resolution_observation_id) REFERENCES dpt.source_observations (access_scope_id,entity_id,entity_kind,field_path,id);

ALTER TABLE dpt.conflict_members ADD CONSTRAINT conflict_members_fk41 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.conflict_members ADD CONSTRAINT conflict_members_fk42 FOREIGN KEY (access_scope_id,entity_id,entity_kind,field_path,conflict_id) REFERENCES dpt.data_conflicts (access_scope_id,entity_id,entity_kind,field_path,id);

ALTER TABLE dpt.conflict_members ADD CONSTRAINT conflict_members_fk43 FOREIGN KEY (access_scope_id,entity_id,entity_kind,field_path,observation_id) REFERENCES dpt.source_observations (access_scope_id,entity_id,entity_kind,field_path,id);

ALTER TABLE dpt.data_conflicts ADD CONSTRAINT data_conflicts_fk44 FOREIGN KEY (access_scope_id,id,resolution_observation_id) REFERENCES dpt.conflict_members (access_scope_id,conflict_id,observation_id) DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE dpt.ingestion_batches ADD CONSTRAINT ingestion_batches_fk45 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.ingestion_batches ADD CONSTRAINT ingestion_batches_fk46 FOREIGN KEY (access_scope_id,source_id) REFERENCES dpt.sources (access_scope_id,id);

ALTER TABLE dpt.ingestion_batches ADD CONSTRAINT ingestion_batches_fk47 FOREIGN KEY (access_scope_id,source_id,rights_id) REFERENCES dpt.rights_assessments (access_scope_id,source_id,id);

ALTER TABLE dpt.staging_records ADD CONSTRAINT staging_records_fk48 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.staging_records ADD CONSTRAINT staging_records_fk49 FOREIGN KEY (access_scope_id,batch_id) REFERENCES dpt.ingestion_batches (access_scope_id,id);

ALTER TABLE dpt.staging_records ADD CONSTRAINT staging_records_fk50 FOREIGN KEY (access_scope_id,source_record_id) REFERENCES dpt.source_records (access_scope_id,id);

ALTER TABLE dpt.validation_results ADD CONSTRAINT validation_results_fk51 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.validation_results ADD CONSTRAINT validation_results_fk52 FOREIGN KEY (access_scope_id,staging_record_id) REFERENCES dpt.staging_records (access_scope_id,id);

ALTER TABLE dpt.audit_events ADD CONSTRAINT audit_events_fk53 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.audit_events ADD CONSTRAINT audit_events_fk54 FOREIGN KEY (entity_id) REFERENCES dpt.entities (id);

ALTER TABLE dpt.audit_events ADD CONSTRAINT audit_events_fk55 FOREIGN KEY (access_scope_id,batch_id) REFERENCES dpt.ingestion_batches (access_scope_id,id);
