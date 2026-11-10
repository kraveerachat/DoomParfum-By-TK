-- RLS identity is the authenticated PostgreSQL login (session_user), never an editable GUC.
CREATE FUNCTION dpt_guard.entity_visible(entity uuid) RETURNS boolean LANGUAGE plpgsql STABLE SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE e dpt.entities; scope_kind text; status text; tbl text;
BEGIN
 SELECT * INTO e FROM dpt.entities WHERE id=entity;
 IF NOT FOUND OR NOT dpt_guard.can_read_scope(e.access_scope_id) THEN RETURN false; END IF;
 SELECT kind INTO scope_kind FROM dpt.access_scopes WHERE id=e.access_scope_id;
 -- A private/shared ACL or curator role is not permission to display expired/revoked selected facts.
 IF EXISTS(SELECT FROM dpt.canonical_selections cs JOIN dpt.source_observations ob ON ob.id=cs.observation_id
   WHERE cs.entity_id=e.id AND cs.access_scope_id=e.access_scope_id AND
    (NOT dpt_guard.record_allowed(ob.source_record_id,'display') OR NOT dpt_guard.record_allowed(ob.source_record_id,'storage'))) THEN RETURN false; END IF;
 IF scope_kind<>'public' OR dpt_guard.is_curator() THEN RETURN true; END IF;
 IF e.kind='image' THEN RETURN dpt_guard.asset_use_valid(e.id,'display'); END IF;
 IF e.kind='listing' THEN RETURN false; END IF;
 tbl:=dpt_guard.kind_table(e.kind);
 EXECUTE format('SELECT review_status FROM dpt.%I WHERE id=$1',tbl) INTO status USING e.id;
 RETURN status='approved' AND NOT EXISTS(SELECT FROM dpt.canonical_selections s JOIN dpt.source_observations o ON o.id=s.observation_id
  WHERE s.entity_id=e.id AND s.access_scope_id=e.access_scope_id AND NOT dpt_guard.record_allowed(o.source_record_id,'display'));
END $$;
CREATE FUNCTION dpt_guard.matching_visible(result_id uuid) RETURNS boolean LANGUAGE sql STABLE SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT EXISTS(SELECT FROM dpt.matching_results m WHERE m.id=result_id AND dpt_guard.can_read_scope(m.access_scope_id)
  AND dpt_guard.matching_inputs_valid(m.access_scope_id,m.coverage,true))
$$;
CREATE SCHEMA dpt_public;
REVOKE ALL ON SCHEMA dpt_public FROM PUBLIC;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON ALL TABLES IN SCHEMA dpt FROM PUBLIC;
REVOKE ALL ON ALL FUNCTIONS IN SCHEMA dpt_guard FROM PUBLIC;
REVOKE ALL ON SCHEMA dpt_ops FROM PUBLIC;
GRANT USAGE ON SCHEMA dpt,dpt_guard TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;
GRANT USAGE ON SCHEMA dpt_public TO dpt_runtime,dpt_anonymous,dpt_curator;
GRANT SELECT ON ALL TABLES IN SCHEMA dpt TO dpt_runtime,dpt_curator;
GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA dpt TO dpt_writer;
-- No TRUNCATE/REFERENCES/trigger/DDL privileges for any runtime group.


GRANT EXECUTE ON FUNCTION dpt_guard.principal_id() TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;

GRANT EXECUTE ON FUNCTION dpt_guard.is_curator() TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;

GRANT EXECUTE ON FUNCTION dpt_guard.can_read_scope(uuid) TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;

GRANT EXECUTE ON FUNCTION dpt_guard.can_write_scope(uuid) TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;

GRANT EXECUTE ON FUNCTION dpt_guard.entity_visible(uuid) TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;

GRANT EXECUTE ON FUNCTION dpt_guard.can_use_asset(uuid,text) TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;

CREATE FUNCTION dpt_guard.readable_record(record uuid) RETURNS boolean LANGUAGE sql STABLE SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT EXISTS(SELECT FROM dpt.source_records r WHERE r.id=record AND dpt_guard.can_read_scope(r.access_scope_id)
  AND dpt_guard.record_allowed(r.id,'display'))
$$;
REVOKE ALL ON FUNCTION dpt_guard.readable_record(uuid) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION dpt_guard.readable_record(uuid) TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;

ALTER TABLE dpt.users ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.users FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.users FOR SELECT TO dpt_runtime,dpt_curator USING (id=dpt_guard.principal_id());

CREATE POLICY insert_scope ON dpt.users FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.is_curator());

CREATE POLICY update_scope ON dpt.users FOR UPDATE TO dpt_writer USING (id=dpt_guard.principal_id()) WITH CHECK (id=dpt_guard.principal_id());

CREATE POLICY delete_scope ON dpt.users FOR DELETE TO dpt_writer USING (id=dpt_guard.principal_id());

ALTER TABLE dpt.users OWNER TO dpt_owner;

ALTER TABLE dpt.access_scopes ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.access_scopes FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.access_scopes FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(id));

CREATE POLICY insert_scope ON dpt.access_scopes FOR INSERT TO dpt_writer WITH CHECK ((kind='public' AND dpt_guard.is_curator()) OR (kind<>'public' AND owner_user_id=dpt_guard.principal_id()));

CREATE POLICY update_scope ON dpt.access_scopes FOR UPDATE TO dpt_writer USING (owner_user_id=dpt_guard.principal_id()) WITH CHECK (owner_user_id=dpt_guard.principal_id());

CREATE POLICY delete_scope ON dpt.access_scopes FOR DELETE TO dpt_writer USING (owner_user_id=dpt_guard.principal_id());

ALTER TABLE dpt.access_scopes OWNER TO dpt_owner;

ALTER TABLE dpt.scope_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.scope_members FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.scope_members FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.scope_members FOR INSERT TO dpt_writer WITH CHECK (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.owner_user_id=dpt_guard.principal_id()));

CREATE POLICY update_scope ON dpt.scope_members FOR UPDATE TO dpt_writer USING (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.owner_user_id=dpt_guard.principal_id())) WITH CHECK (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.owner_user_id=dpt_guard.principal_id()));

CREATE POLICY delete_scope ON dpt.scope_members FOR DELETE TO dpt_writer USING (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.owner_user_id=dpt_guard.principal_id()));

ALTER TABLE dpt.scope_members OWNER TO dpt_owner;

ALTER TABLE dpt.countries ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.countries FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.countries FOR SELECT TO dpt_runtime,dpt_curator USING (true);

CREATE POLICY insert_scope ON dpt.countries FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.is_curator());

CREATE POLICY update_scope ON dpt.countries FOR UPDATE TO dpt_writer USING (dpt_guard.is_curator()) WITH CHECK (dpt_guard.is_curator());

CREATE POLICY delete_scope ON dpt.countries FOR DELETE TO dpt_writer USING (dpt_guard.is_curator());

ALTER TABLE dpt.countries OWNER TO dpt_owner;

GRANT SELECT ON dpt.countries TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.countries FOR SELECT TO dpt_anonymous USING (true);

ALTER TABLE dpt.brand_tags ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.brand_tags FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.brand_tags FOR SELECT TO dpt_runtime,dpt_curator USING (true);

CREATE POLICY insert_scope ON dpt.brand_tags FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.is_curator());

CREATE POLICY update_scope ON dpt.brand_tags FOR UPDATE TO dpt_writer USING (dpt_guard.is_curator()) WITH CHECK (dpt_guard.is_curator());

CREATE POLICY delete_scope ON dpt.brand_tags FOR DELETE TO dpt_writer USING (dpt_guard.is_curator());

ALTER TABLE dpt.brand_tags OWNER TO dpt_owner;

GRANT SELECT ON dpt.brand_tags TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.brand_tags FOR SELECT TO dpt_anonymous USING (true);

ALTER TABLE dpt.families ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.families FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.families FOR SELECT TO dpt_runtime,dpt_curator USING (true);

CREATE POLICY insert_scope ON dpt.families FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.is_curator());

CREATE POLICY update_scope ON dpt.families FOR UPDATE TO dpt_writer USING (dpt_guard.is_curator()) WITH CHECK (dpt_guard.is_curator());

CREATE POLICY delete_scope ON dpt.families FOR DELETE TO dpt_writer USING (dpt_guard.is_curator());

ALTER TABLE dpt.families OWNER TO dpt_owner;

GRANT SELECT ON dpt.families TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.families FOR SELECT TO dpt_anonymous USING (true);

ALTER TABLE dpt.field_definitions ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.field_definitions FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.field_definitions FOR SELECT TO dpt_runtime,dpt_curator USING (true);

CREATE POLICY insert_scope ON dpt.field_definitions FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.is_curator());

CREATE POLICY update_scope ON dpt.field_definitions FOR UPDATE TO dpt_writer USING (dpt_guard.is_curator()) WITH CHECK (dpt_guard.is_curator());

CREATE POLICY delete_scope ON dpt.field_definitions FOR DELETE TO dpt_writer USING (dpt_guard.is_curator());

ALTER TABLE dpt.field_definitions OWNER TO dpt_owner;

ALTER TABLE dpt.entities ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.entities FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.entities FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.entities FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.entities FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.entities FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.entities OWNER TO dpt_owner;

ALTER TABLE dpt.brands ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.brands FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.brands FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.brands FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.brands FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.brands FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.brands OWNER TO dpt_owner;

GRANT SELECT ON dpt.brands TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.brands FOR SELECT TO dpt_anonymous USING (dpt_guard.entity_visible(id));

ALTER TABLE dpt.perfumes ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.perfumes FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.perfumes FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.perfumes FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.perfumes FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.perfumes FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.perfumes OWNER TO dpt_owner;

GRANT SELECT ON dpt.perfumes TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.perfumes FOR SELECT TO dpt_anonymous USING (dpt_guard.entity_visible(id));

ALTER TABLE dpt.product_variants ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.product_variants FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.product_variants FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.product_variants FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.product_variants FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.product_variants FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.product_variants OWNER TO dpt_owner;

GRANT SELECT ON dpt.product_variants TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.product_variants FOR SELECT TO dpt_anonymous USING (dpt_guard.entity_visible(id));

ALTER TABLE dpt.notes ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.notes FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.notes FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.notes FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.notes FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.notes FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.notes OWNER TO dpt_owner;

GRANT SELECT ON dpt.notes TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.notes FOR SELECT TO dpt_anonymous USING (dpt_guard.entity_visible(id));

ALTER TABLE dpt.accords ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.accords FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.accords FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.accords FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.accords FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.accords FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.accords OWNER TO dpt_owner;

GRANT SELECT ON dpt.accords TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.accords FOR SELECT TO dpt_anonymous USING (dpt_guard.entity_visible(id));

ALTER TABLE dpt.perfume_relations ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.perfume_relations FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.perfume_relations FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.perfume_relations FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.perfume_relations FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.perfume_relations FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.perfume_relations OWNER TO dpt_owner;

ALTER TABLE dpt.sources ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.sources FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.sources FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.sources FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.sources FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.sources FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.sources OWNER TO dpt_owner;

ALTER TABLE dpt.rights_assessments ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.rights_assessments FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.rights_assessments FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()));

CREATE POLICY insert_scope ON dpt.rights_assessments FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.rights_assessments FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.rights_assessments FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.rights_assessments OWNER TO dpt_owner;

ALTER TABLE dpt.source_records ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.source_records FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.source_records FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()));

CREATE POLICY insert_scope ON dpt.source_records FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.source_records FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.source_records FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.source_records OWNER TO dpt_owner;

ALTER TABLE dpt.entity_source_links ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.entity_source_links FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.entity_source_links FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()));

CREATE POLICY insert_scope ON dpt.entity_source_links FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.entity_source_links FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.entity_source_links FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.entity_source_links OWNER TO dpt_owner;

ALTER TABLE dpt.source_observations ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.source_observations FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.source_observations FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.source_observations FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.source_observations FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.source_observations FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.source_observations OWNER TO dpt_owner;

ALTER TABLE dpt.canonical_selections ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.canonical_selections FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.canonical_selections FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()));

CREATE POLICY insert_scope ON dpt.canonical_selections FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.canonical_selections FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.canonical_selections FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.canonical_selections OWNER TO dpt_owner;

ALTER TABLE dpt.data_conflicts ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.data_conflicts FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.data_conflicts FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()));

CREATE POLICY insert_scope ON dpt.data_conflicts FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.data_conflicts FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.data_conflicts FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.data_conflicts OWNER TO dpt_owner;

ALTER TABLE dpt.conflict_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.conflict_members FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.conflict_members FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()));

CREATE POLICY insert_scope ON dpt.conflict_members FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.conflict_members FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.conflict_members FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.conflict_members OWNER TO dpt_owner;

ALTER TABLE dpt.ingestion_batches ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.ingestion_batches FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.ingestion_batches FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()) AND dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.ingestion_batches FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.ingestion_batches FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.ingestion_batches FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.ingestion_batches OWNER TO dpt_owner;

ALTER TABLE dpt.staging_records ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.staging_records FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.staging_records FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()) AND dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.staging_records FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.staging_records FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.staging_records FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.staging_records OWNER TO dpt_owner;

ALTER TABLE dpt.validation_results ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.validation_results FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.validation_results FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()) AND dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.validation_results FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.validation_results FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.validation_results FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.validation_results OWNER TO dpt_owner;

ALTER TABLE dpt.audit_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.audit_events FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.audit_events FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()) AND dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.audit_events FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.audit_events FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.audit_events FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.audit_events OWNER TO dpt_owner;

ALTER TABLE dpt.brand_aliases ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.brand_aliases FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.brand_aliases FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(brand_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.brand_aliases FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.brand_aliases FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.brand_aliases FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.brand_aliases OWNER TO dpt_owner;

ALTER TABLE dpt.note_aliases ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.note_aliases FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.note_aliases FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(note_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.note_aliases FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.note_aliases FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.note_aliases FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.note_aliases OWNER TO dpt_owner;

ALTER TABLE dpt.brand_tag_links ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.brand_tag_links FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.brand_tag_links FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(brand_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.brand_tag_links FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.brand_tag_links FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.brand_tag_links FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.brand_tag_links OWNER TO dpt_owner;

ALTER TABLE dpt.perfume_notes ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.perfume_notes FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.perfume_notes FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.perfume_notes FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.perfume_notes FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.perfume_notes FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.perfume_notes OWNER TO dpt_owner;

GRANT SELECT ON dpt.perfume_notes TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.perfume_notes FOR SELECT TO dpt_anonymous USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

ALTER TABLE dpt.perfume_accords ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.perfume_accords FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.perfume_accords FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.perfume_accords FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.perfume_accords FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.perfume_accords FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.perfume_accords OWNER TO dpt_owner;

GRANT SELECT ON dpt.perfume_accords TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.perfume_accords FOR SELECT TO dpt_anonymous USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

ALTER TABLE dpt.perfume_families ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.perfume_families FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.perfume_families FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.perfume_families FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.perfume_families FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.perfume_families FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.perfume_families OWNER TO dpt_owner;

GRANT SELECT ON dpt.perfume_families TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.perfume_families FOR SELECT TO dpt_anonymous USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

ALTER TABLE dpt.perfume_usage_tags ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.perfume_usage_tags FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.perfume_usage_tags FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.perfume_usage_tags FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.perfume_usage_tags FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.perfume_usage_tags FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.perfume_usage_tags OWNER TO dpt_owner;

GRANT SELECT ON dpt.perfume_usage_tags TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.perfume_usage_tags FOR SELECT TO dpt_anonymous USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

ALTER TABLE dpt.image_assets ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.image_assets FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.image_assets FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.image_assets FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.image_assets FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.image_assets FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.image_assets OWNER TO dpt_owner;

ALTER TABLE dpt.asset_permissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.asset_permissions FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.asset_permissions FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND (EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind<>'public') OR dpt_guard.is_curator()));

CREATE POLICY insert_scope ON dpt.asset_permissions FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.asset_permissions FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.asset_permissions FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.asset_permissions OWNER TO dpt_owner;

ALTER TABLE dpt.perfume_images ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.perfume_images FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.perfume_images FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.can_use_asset(asset_id,'display'));

CREATE POLICY insert_scope ON dpt.perfume_images FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.perfume_images FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.perfume_images FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.perfume_images OWNER TO dpt_owner;

GRANT SELECT ON dpt.perfume_images TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.perfume_images FOR SELECT TO dpt_anonymous USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.can_use_asset(asset_id,'display'));

ALTER TABLE dpt.note_images ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.note_images FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.note_images FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(note_id) AND dpt_guard.can_use_asset(asset_id,'display'));

CREATE POLICY insert_scope ON dpt.note_images FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.note_images FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.note_images FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.note_images OWNER TO dpt_owner;

GRANT SELECT ON dpt.note_images TO dpt_anonymous;

CREATE POLICY anonymous_approved ON dpt.note_images FOR SELECT TO dpt_anonymous USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(note_id) AND dpt_guard.can_use_asset(asset_id,'display'));

ALTER TABLE dpt.comparison_evidence ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.comparison_evidence FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.comparison_evidence FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(relation_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.comparison_evidence FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.comparison_evidence FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.comparison_evidence FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.comparison_evidence OWNER TO dpt_owner;

ALTER TABLE dpt.rating_observations ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.rating_observations FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.rating_observations FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(perfume_id) AND dpt_guard.readable_record(source_record_id));

CREATE POLICY insert_scope ON dpt.rating_observations FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.rating_observations FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.rating_observations FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.rating_observations OWNER TO dpt_owner;

ALTER TABLE dpt.matching_results ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.matching_results FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.matching_results FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id) AND dpt_guard.entity_visible(relation_id) AND dpt_guard.matching_visible(id));

CREATE POLICY insert_scope ON dpt.matching_results FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.matching_results FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.matching_results FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.matching_results OWNER TO dpt_owner;

ALTER TABLE dpt.retail_listings ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.retail_listings FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.retail_listings FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.entity_visible(id));

CREATE POLICY insert_scope ON dpt.retail_listings FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.retail_listings FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.retail_listings FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.retail_listings OWNER TO dpt_owner;

ALTER TABLE dpt.price_observations ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.price_observations FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.price_observations FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.price_observations FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.price_observations FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.price_observations FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.price_observations OWNER TO dpt_owner;

ALTER TABLE dpt.user_lists ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.user_lists FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.user_lists FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.user_lists FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.user_lists FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.user_lists FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.user_lists OWNER TO dpt_owner;

ALTER TABLE dpt.user_list_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.user_list_items FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.user_list_items FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.user_list_items FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.user_list_items FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.user_list_items FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.user_list_items OWNER TO dpt_owner;

ALTER TABLE dpt.saved_buying_sources ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.saved_buying_sources FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.saved_buying_sources FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.saved_buying_sources FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.saved_buying_sources FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.saved_buying_sources FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.saved_buying_sources OWNER TO dpt_owner;

ALTER TABLE dpt.purchase_records ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.purchase_records FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.purchase_records FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.purchase_records FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.purchase_records FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.purchase_records FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.purchase_records OWNER TO dpt_owner;

ALTER TABLE dpt.inventory_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE dpt.inventory_items FORCE ROW LEVEL SECURITY;

CREATE POLICY read_scope ON dpt.inventory_items FOR SELECT TO dpt_runtime,dpt_curator USING (dpt_guard.can_read_scope(access_scope_id));

CREATE POLICY insert_scope ON dpt.inventory_items FOR INSERT TO dpt_writer WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY update_scope ON dpt.inventory_items FOR UPDATE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id)) WITH CHECK (dpt_guard.can_write_scope(access_scope_id));

CREATE POLICY delete_scope ON dpt.inventory_items FOR DELETE TO dpt_writer USING (dpt_guard.can_write_scope(access_scope_id));

ALTER TABLE dpt.inventory_items OWNER TO dpt_owner;

-- A public source attribution projection excludes record locators, raw payloads and permission evidence.
GRANT SELECT(id,access_scope_id,name,kind,entry_url,publisher) ON dpt.sources TO dpt_anonymous;
CREATE POLICY anonymous_source_metadata ON dpt.sources FOR SELECT TO dpt_anonymous USING (
 EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=access_scope_id AND s.kind='public'));
-- No anonymous scope table access is needed: use a bounded helper instead of policy subquery recursion.
CREATE FUNCTION dpt_guard.public_scope(scope_id uuid) RETURNS boolean LANGUAGE sql STABLE SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$ SELECT EXISTS(SELECT FROM dpt.access_scopes WHERE id=scope_id AND kind='public') $$;
REVOKE ALL ON FUNCTION dpt_guard.public_scope(uuid) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION dpt_guard.public_scope(uuid) TO dpt_runtime,dpt_writer,dpt_curator,dpt_anonymous,dpt_owner;
ALTER POLICY anonymous_source_metadata ON dpt.sources USING(dpt_guard.public_scope(access_scope_id));
CREATE VIEW dpt_public.perfumes WITH (security_invoker=true,security_barrier=true) AS
 SELECT id,brand_id,name,slug,edition_label,concentration_code,release_year,description
 FROM dpt.perfumes WHERE dpt_guard.public_scope(access_scope_id) AND review_status='approved';
CREATE VIEW dpt_public.source_attribution WITH (security_invoker=true,security_barrier=true) AS
 SELECT id,name,kind,entry_url,publisher FROM dpt.sources WHERE dpt_guard.public_scope(access_scope_id);
GRANT SELECT ON dpt_public.perfumes,dpt_public.source_attribution TO dpt_runtime,dpt_anonymous,dpt_curator;


INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','name','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','country_code','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','website_url','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','aliases','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','tags','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','founded','integer','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','portrait','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','type','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('brand','perfume_count','integer','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','name','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','brand_id','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','edition_label','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','concentration_code','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','release_year','integer','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','gender_label','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','description','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','perfumers','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','character','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','popularity_rank','integer','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','accords','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','families.primary','object','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','families.secondary','object','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','usage.season','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','usage.time','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','usage.occasion','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','notes.top','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','notes.heart','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','notes.base','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','notes.general','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','name','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','name_th','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','material_origin','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','description','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','aliases','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','material_family','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','origin','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('note','smell','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('variant','perfume_id','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('variant','volume_ml','number','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('variant','packaging_code','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('variant','sku','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('variant','gtin','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('accord','label','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('relation','relation_type','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('listing','product_url','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('image','attribution','string','local-v1');

GRANT EXECUTE ON FUNCTION dpt_guard.matching_visible(uuid) TO dpt_runtime,dpt_curator;

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','family','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','secondary_family','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','seasons','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('perfume','times_of_day','array','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('relation','directionality','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('relation','reference_perfume_id','string','local-v1');

INSERT INTO dpt.field_definitions(entity_kind,path,value_type,mapping_version) VALUES('relation','candidate_perfume_id','string','local-v1');
