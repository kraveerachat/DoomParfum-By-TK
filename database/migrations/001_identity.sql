-- IMP-P1-01. PostgreSQL 16; no cloud/auth-provider dependencies.
CREATE SCHEMA dpt;
CREATE SCHEMA dpt_guard;
REVOKE ALL ON SCHEMA dpt, dpt_guard FROM PUBLIC;
CREATE DOMAIN dpt.nonempty AS text CONSTRAINT nonempty_text CHECK (btrim(VALUE) <> '');
CREATE DOMAIN dpt.sha256 AS text CONSTRAINT sha256_hex CHECK (VALUE ~ '^[0-9a-f]{64}$');
CREATE DOMAIN dpt.use_state AS text CONSTRAINT use_state_allowed CHECK (VALUE IN ('allowed','restricted','unknown'));
CREATE DOMAIN dpt.currency_code AS char(3) CONSTRAINT local_currency_v1 CHECK (VALUE IN ('USD','THB','IDR','EUR','GBP','AED','OMR','SAR','SGD','JPY','AUD','CAD','CHF','CNY','HKD','MYR'));
CREATE DOMAIN dpt.review_state AS text CONSTRAINT review_state_allowed CHECK (VALUE IN ('draft','reviewed','approved','archived'));
DO $$ BEGIN
 IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='dpt_owner') THEN CREATE ROLE dpt_owner NOLOGIN NOSUPERUSER NOBYPASSRLS; END IF;
 IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='dpt_runtime') THEN CREATE ROLE dpt_runtime NOLOGIN NOSUPERUSER NOBYPASSRLS; END IF;
 IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='dpt_writer') THEN CREATE ROLE dpt_writer NOLOGIN NOSUPERUSER NOBYPASSRLS; END IF;
 IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='dpt_curator') THEN CREATE ROLE dpt_curator NOLOGIN NOSUPERUSER NOBYPASSRLS; END IF;
 IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='dpt_anonymous') THEN CREATE ROLE dpt_anonymous NOLOGIN NOSUPERUSER NOBYPASSRLS; END IF;
END $$;

CREATE TABLE dpt.users (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    auth_subject dpt.nonempty NOT NULL,
    display_name text,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_k1 UNIQUE(auth_subject)
);

CREATE TABLE dpt.access_scopes (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    kind text NOT NULL,
    owner_user_id uuid,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT access_scopes_pkey PRIMARY KEY (id),
    CONSTRAINT access_scopes_k1 CHECK (kind IN ('public','shared','user_private')),
    CONSTRAINT access_scopes_k2 CHECK ((kind='public' AND owner_user_id IS NULL) OR (kind IN ('shared','user_private') AND owner_user_id IS NOT NULL)),
    CONSTRAINT access_scopes_k3 UNIQUE(id,kind,owner_user_id)
);

CREATE UNIQUE INDEX access_scopes_one_public ON dpt.access_scopes(kind) WHERE kind='public';
CREATE UNIQUE INDEX access_scopes_one_private ON dpt.access_scopes(owner_user_id) WHERE kind='user_private';

CREATE TABLE dpt.scope_members (
    access_scope_id uuid NOT NULL,
    user_id uuid NOT NULL,
    role text NOT NULL,
    revoked_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT scope_members_pkey PRIMARY KEY (access_scope_id,user_id),
    CONSTRAINT scope_members_k1 CHECK(role IN ('reader','editor'))
);

CREATE TABLE dpt.countries (
    code char(2) NOT NULL,
    name dpt.nonempty NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT countries_pkey PRIMARY KEY (code),
    CONSTRAINT countries_k1 CHECK(code ~ '^[A-Z]{2}$')
);

CREATE TABLE dpt.brand_tags (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    scheme dpt.nonempty NOT NULL,
    code dpt.nonempty NOT NULL,
    label dpt.nonempty NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT brand_tags_pkey PRIMARY KEY (id),
    CONSTRAINT brand_tags_k1 UNIQUE(scheme,code)
);

CREATE TABLE dpt.families (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    scheme dpt.nonempty NOT NULL,
    code dpt.nonempty NOT NULL,
    label dpt.nonempty NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT families_pkey PRIMARY KEY (id),
    CONSTRAINT families_k1 UNIQUE(scheme,code)
);

CREATE TABLE dpt.field_definitions (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    entity_kind dpt.nonempty NOT NULL,
    path dpt.nonempty NOT NULL,
    value_type text NOT NULL,
    mapping_version dpt.nonempty NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT field_definitions_pkey PRIMARY KEY (id),
    CONSTRAINT field_definitions_k1 UNIQUE(entity_kind,path),
    CONSTRAINT field_definitions_k2 CHECK(entity_kind IN ('brand','perfume','variant','note','accord','image','relation','listing')),
    CONSTRAINT field_definitions_k3 CHECK(value_type IN ('string','integer','number','boolean','array','object'))
);

CREATE TABLE dpt.entities (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    access_scope_id uuid NOT NULL,
    kind text NOT NULL,
    archived_at timestamptz,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT entities_pkey PRIMARY KEY (id),
    CONSTRAINT entities_scope_id_key UNIQUE (access_scope_id,id),
    CONSTRAINT entities_k1 CHECK(kind IN ('brand','perfume','variant','note','accord','image','relation','listing')),
    CONSTRAINT entities_k2 UNIQUE(id,kind),
    CONSTRAINT entities_k3 UNIQUE(access_scope_id,id,kind)
);

ALTER TABLE dpt.access_scopes ADD CONSTRAINT access_scopes_fk1 FOREIGN KEY (owner_user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.scope_members ADD CONSTRAINT scope_members_fk2 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);

ALTER TABLE dpt.scope_members ADD CONSTRAINT scope_members_fk3 FOREIGN KEY (user_id) REFERENCES dpt.users (id);

ALTER TABLE dpt.entities ADD CONSTRAINT entities_fk4 FOREIGN KEY (access_scope_id) REFERENCES dpt.access_scopes (id);
