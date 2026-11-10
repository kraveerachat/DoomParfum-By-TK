CREATE FUNCTION dpt_guard.asset_use_valid(asset uuid,operation text,require_active boolean DEFAULT true) RETURNS boolean
LANGUAGE plpgsql STABLE SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE a dpt.image_assets; p dpt.asset_permissions; parent dpt.image_assets;
  prior dpt.asset_permissions; seen uuid[]:='{}'; first boolean:=true; needed text:=operation;
BEGIN
  LOOP
    IF asset=ANY(seen) THEN RETURN false; END IF;
    seen:=array_append(seen,asset);
    SELECT * INTO a FROM dpt.image_assets WHERE id=asset;
    IF NOT FOUND OR a.state NOT IN ('acquired','validated') THEN RETURN false; END IF;
    SELECT * INTO p FROM dpt.asset_permissions WHERE id=a.asset_permission_id;
    IF NOT FOUND OR (require_active AND (p.revoked_at IS NOT NULL OR p.checked_at>statement_timestamp() OR
       (p.review_after IS NOT NULL AND p.review_after<=statement_timestamp()))) OR
       (p.access_scope_id,p.asset_id,p.source_id,p.source_record_id,p.rights_id) IS DISTINCT FROM
       (a.access_scope_id,a.id,a.source_id,a.source_record_id,a.rights_id) OR
       p.content_sha256 IS NULL OR p.content_sha256 IS DISTINCT FROM a.sha256 OR
       p.asset_locator IS DISTINCT FROM COALESCE(a.original_url,'asset:'||a.id::text) OR
       p.acquire_use<>'allowed' OR NOT dpt_guard.right_permitted(a.rights_id,'storage',require_active) OR
       NOT dpt_guard.record_permitted(a.source_record_id,'storage',require_active) THEN RETURN false; END IF;
    IF needed='display' AND (p.display_use<>'allowed' OR NOT dpt_guard.right_permitted(a.rights_id,'display',require_active) OR
        NOT dpt_guard.record_permitted(a.source_record_id,'display',require_active)) THEN RETURN false;
    ELSIF needed='transform' AND (p.transform_use<>'allowed' OR NOT dpt_guard.right_permitted(a.rights_id,'storage',require_active)) THEN RETURN false;
    ELSIF needed='redistribution' AND (p.redistribution_use<>'allowed' OR NOT dpt_guard.right_permitted(a.rights_id,'redistribution',require_active) OR
        NOT dpt_guard.record_permitted(a.source_record_id,'redistribution',require_active)) THEN RETURN false;
    ELSIF needed NOT IN ('acquire','display','transform','redistribution') THEN RETURN false; END IF;
    IF a.parent_asset_id IS NULL THEN RETURN p.permission_kind='original'; END IF;
    SELECT * INTO parent FROM dpt.image_assets WHERE id=a.parent_asset_id;
    SELECT * INTO prior FROM dpt.asset_permissions WHERE id=p.parent_permission_id;
    IF p.permission_kind<>'derivative' OR p.parent_asset_id IS DISTINCT FROM a.parent_asset_id OR
      (parent.access_scope_id,parent.source_id,parent.source_record_id) IS DISTINCT FROM
      (a.access_scope_id,a.source_id,a.source_record_id) OR
      parent.asset_permission_id IS DISTINCT FROM p.parent_permission_id OR
      p.output_license IS NULL OR btrim(p.output_license)='' OR
      p.output_license IS DISTINCT FROM prior.output_license OR
      a.attribution IS NULL OR btrim(a.attribution)='' OR a.transform_spec IS NULL OR
      NULLIF(btrim(a.transform_spec->>'changes'),'') IS NULL THEN RETURN false; END IF;
    -- Intended child display/redistribution must also be permitted through the ancestor chain.
    IF operation='display' AND (prior.display_use<>'allowed' OR NOT dpt_guard.right_permitted(parent.rights_id,'display',require_active)) THEN RETURN false; END IF;
    IF operation='redistribution' AND (prior.redistribution_use<>'allowed' OR NOT dpt_guard.right_permitted(parent.rights_id,'redistribution',require_active)) THEN RETURN false; END IF;
    asset:=a.parent_asset_id; needed:='transform'; first:=false;
  END LOOP;
END $$;

CREATE FUNCTION dpt_guard.can_use_asset(asset uuid,operation text) RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT EXISTS(SELECT FROM dpt.image_assets a WHERE a.id=asset AND dpt_guard.can_read_scope(a.access_scope_id)
   AND dpt_guard.asset_use_valid(a.id,operation))
$$;

CREATE FUNCTION dpt_guard.validate_images() RETURNS void LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE a record; cursor_id uuid; next_id uuid; seen uuid[];
BEGIN
  FOR a IN SELECT * FROM dpt.image_assets LOOP
    cursor_id:=a.id; seen:='{}';
    WHILE cursor_id IS NOT NULL LOOP
      IF cursor_id=ANY(seen) THEN RAISE EXCEPTION 'Cyclic image lineage' USING ERRCODE='23514'; END IF;
      seen:=array_append(seen,cursor_id);
      SELECT parent_asset_id INTO next_id FROM dpt.image_assets WHERE id=cursor_id;
      cursor_id:=next_id;
    END LOOP;
    IF a.parent_asset_id IS NOT NULL AND NOT EXISTS(SELECT FROM dpt.image_assets p WHERE p.id=a.parent_asset_id
      AND (p.access_scope_id,p.source_id,p.source_record_id)=(a.access_scope_id,a.source_id,a.source_record_id)) THEN
      RAISE EXCEPTION 'Derivative requires same scope/source/capture as parent' USING ERRCODE='23514'; END IF;
    IF a.state IN ('acquired','validated') AND NOT dpt_guard.asset_use_valid(a.id,'acquire',false) THEN
      RAISE EXCEPTION 'Invalid selected asset grant/hash/locator/derivative contract' USING ERRCODE='23514'; END IF;
  END LOOP;
END $$;

CREATE FUNCTION dpt_guard.invalidate_assets() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
  -- Revoke/replace a grant without erasing the grant or original lineage. A future use rechecks expiry too.
  IF TG_TABLE_NAME='image_assets' THEN
    IF NEW.asset_permission_id IS NOT DISTINCT FROM OLD.asset_permission_id THEN RETURN NULL; END IF;
    WITH RECURSIVE descendants(id) AS (
      SELECT id FROM dpt.image_assets WHERE parent_asset_id=NEW.id
      UNION SELECT a.id FROM dpt.image_assets a JOIN descendants d ON a.parent_asset_id=d.id)
    UPDATE dpt.image_assets SET state='rights_pending' WHERE id IN (SELECT id FROM descendants) AND state IN ('acquired','validated');
  ELSE
    WITH RECURSIVE invalid(id) AS (
      SELECT a.id FROM dpt.image_assets a JOIN dpt.source_records r ON r.id=a.source_record_id
      WHERE (TG_TABLE_NAME='rights_assessments' AND (a.rights_id=NEW.id OR r.rights_id=NEW.id))
        OR (TG_TABLE_NAME='asset_permissions' AND a.asset_permission_id=NEW.id)
      UNION SELECT a.id FROM dpt.image_assets a JOIN invalid i ON a.parent_asset_id=i.id)
    UPDATE dpt.image_assets SET state='rights_pending' WHERE id IN (SELECT id FROM invalid) AND state IN ('acquired','validated');
  END IF;
  RETURN NULL;
END $$;

CREATE FUNCTION dpt_guard.check_active_row() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE body jsonb; s dpt.canonical_selections; o dpt.source_observations; b dpt.ingestion_batches;
  rec dpt.source_records; target uuid; field text; item record; col text; v jsonb;
BEGIN
  IF TG_OP='DELETE' THEN RETURN NULL; END IF;
  IF TG_TABLE_NAME='canonical_selections' THEN
    SELECT * INTO s FROM dpt.canonical_selections WHERE access_scope_id=NEW.access_scope_id AND entity_id=NEW.entity_id AND entity_kind=NEW.entity_kind AND field_path=NEW.field_path;
    IF NOT FOUND THEN RETURN NULL; END IF;
    SELECT * INTO o FROM dpt.source_observations WHERE id=s.observation_id;
    IF NOT dpt_guard.record_allowed(o.source_record_id,'storage') OR NOT dpt_guard.record_allowed(o.source_record_id,'display') THEN
      RAISE EXCEPTION 'Final selection grant is inactive' USING ERRCODE='23514'; END IF;
  ELSIF TG_TABLE_NAME='staging_records' THEN
    SELECT to_jsonb(t) INTO body FROM dpt.staging_records t WHERE id=NEW.id;
    IF body IS NULL THEN RETURN NULL; END IF;
    SELECT * INTO b FROM dpt.ingestion_batches WHERE id=(body->>'batch_id')::uuid;
    IF body->'raw_payload'<>'null'::jsonb AND (NOT dpt_guard.right_allowed(b.rights_id,'storage') OR NOT dpt_guard.right_allowed(b.rights_id,'automation')) THEN
      RAISE EXCEPTION 'Raw staging needs active storage/automation rights' USING ERRCODE='23514'; END IF;
    IF body->>'source_record_id' IS NOT NULL THEN
      SELECT * INTO rec FROM dpt.source_records WHERE id=(body->>'source_record_id')::uuid;
      IF (rec.source_id,rec.external_key,rec.payload_sha256) IS DISTINCT FROM (b.source_id,body->>'external_key',(body->>'payload_sha256')::dpt.sha256) THEN
        RAISE EXCEPTION 'Staging/capture lineage differs' USING ERRCODE='23514'; END IF;
    END IF;
    IF body->>'state'='promoted' AND ((body->>'source_record_id') IS NULL OR
      NOT EXISTS(SELECT FROM dpt.validation_results v WHERE v.staging_record_id=(body->>'id')::uuid) OR
      EXISTS(SELECT FROM dpt.validation_results v WHERE v.staging_record_id=(body->>'id')::uuid AND v.result<>'pass')) THEN
      RAISE EXCEPTION 'Promotion requires linked capture and all recorded validation rules passing' USING ERRCODE='23514'; END IF;
  ELSIF TG_TABLE_NAME='image_assets' THEN
    SELECT to_jsonb(t) INTO body FROM dpt.image_assets t WHERE id=NEW.id;
    IF body->>'state' IN ('acquired','validated') AND NOT dpt_guard.asset_use_valid((body->>'id')::uuid,'acquire') THEN
      RAISE EXCEPTION 'Changed/acquired image requires current active grants' USING ERRCODE='23514'; END IF;
  ELSIF TG_TABLE_NAME='matching_results' THEN
    SELECT to_jsonb(t) INTO body FROM dpt.matching_results t WHERE id=NEW.id;
    IF body IS NOT NULL AND NOT dpt_guard.matching_inputs_valid((body->>'access_scope_id')::uuid,body->'coverage',true) THEN
      RAISE EXCEPTION 'Matching inputs need active applicable grants' USING ERRCODE='23514'; END IF;
  ELSIF TG_TABLE_NAME IN ('comparison_evidence','rating_observations') THEN
    EXECUTE format('SELECT to_jsonb(t) FROM dpt.%I t WHERE id=$1',TG_TABLE_NAME) INTO body USING NEW.id;
    IF body IS NOT NULL AND NOT dpt_guard.record_allowed((body->>'source_record_id')::uuid,'storage') THEN
      RAISE EXCEPTION 'Evidence storage grant required' USING ERRCODE='23514'; END IF;
    IF TG_TABLE_NAME='comparison_evidence' AND (body->>'summary' IS NOT NULL OR body->>'excerpt' IS NOT NULL) AND
      NOT dpt_guard.record_allowed((body->>'source_record_id')::uuid,'display') THEN
      RAISE EXCEPTION 'Text reuse needs display grant; URL-only evidence may remain' USING ERRCODE='23514'; END IF;
  ELSIF TG_TABLE_NAME IN ('brands','perfumes','notes','accords','product_variants','perfume_relations') THEN
    EXECUTE format('SELECT to_jsonb(t) FROM dpt.%I t WHERE id=$1',TG_TABLE_NAME) INTO body USING NEW.id;
    IF body IS NOT NULL AND body->>'review_status'='approved' THEN
      -- App UUID/slug/scheme/code are app metadata; every populated source scalar needs a selection.
      FOR col IN SELECT key FROM jsonb_each(body) WHERE dpt_guard.scalar_column(body->>'entity_kind',key) IS NOT NULL LOOP
        v:=body->col;
        IF v<>'null'::jsonb AND NOT EXISTS(SELECT FROM dpt.canonical_selections cs JOIN dpt.source_observations ob ON ob.id=cs.observation_id
          WHERE cs.access_scope_id=(body->>'access_scope_id')::uuid AND cs.entity_id=(body->>'id')::uuid AND cs.field_path=col
          AND ob.value_status='present' AND dpt_guard.record_allowed(ob.source_record_id,'storage') AND dpt_guard.record_allowed(ob.source_record_id,'display')) THEN
          RAISE EXCEPTION 'Approved imported scalar lacks active reviewed selection' USING ERRCODE='23514'; END IF;
      END LOOP;
    END IF;
  END IF;
  RETURN NULL;
END $$;

CREATE FUNCTION dpt_guard.validate_all_deferred() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
  PERFORM dpt_guard.validate_model(); PERFORM dpt_guard.validate_images(); RETURN NULL;
END $$;

-- Every scoped reference to catalogue identity uses public-or-exact-same-scope compatibility.
DO $$ DECLARE r record; cols text; names text; BEGIN
  FOR r IN SELECT c.relname FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace
    WHERE n.nspname='dpt' AND c.relkind='r' LOOP
    EXECUTE format('CREATE TRIGGER a_serialize BEFORE INSERT OR UPDATE OR DELETE ON dpt.%I FOR EACH ROW EXECUTE FUNCTION dpt_guard.serialize_write()',r.relname);
    EXECUTE format('CREATE TRIGGER b_identity BEFORE UPDATE ON dpt.%I FOR EACH ROW EXECUTE FUNCTION dpt_guard.identity_guard()',r.relname);
    EXECUTE format('CREATE CONSTRAINT TRIGGER z_model_contract AFTER INSERT OR UPDATE OR DELETE ON dpt.%I DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION dpt_guard.validate_all_deferred()',r.relname);
    IF r.relname IN ('source_records','source_observations','audit_events','rights_assessments','asset_permissions','field_definitions') THEN
      EXECUTE format('CREATE TRIGGER c_append_only BEFORE UPDATE OR DELETE ON dpt.%I FOR EACH ROW EXECUTE FUNCTION dpt_guard.append_only()',r.relname);
    END IF;
    IF r.relname IN ('canonical_selections','staging_records','comparison_evidence','rating_observations','matching_results','image_assets','brands','perfumes','notes','accords','product_variants','perfume_relations') THEN
      EXECUTE format('CREATE CONSTRAINT TRIGGER y_active_row AFTER INSERT OR UPDATE ON dpt.%I DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION dpt_guard.check_active_row()',r.relname);
    END IF;
    SELECT string_agg(quote_literal(a.attname),',') INTO cols FROM pg_attribute a
      WHERE a.attrelid=format('dpt.%I',r.relname)::regclass AND a.attnum>0 AND NOT a.attisdropped
      AND a.attname IN ('brand_id','perfume_id','note_id','accord_id','asset_id','relation_id','entity_id','reference_perfume_id','candidate_perfume_id','variant_id');
    IF cols IS NOT NULL THEN
      EXECUTE format('CREATE TRIGGER d_targets BEFORE INSERT OR UPDATE ON dpt.%I FOR EACH ROW EXECUTE FUNCTION dpt_guard.compatible_targets(%s)',r.relname,cols);
    END IF;
  END LOOP;
END $$;
CREATE TRIGGER c_observation BEFORE INSERT ON dpt.source_observations FOR EACH ROW EXECUTE FUNCTION dpt_guard.observation_guard();
CREATE TRIGGER c_member BEFORE INSERT OR UPDATE ON dpt.scope_members FOR EACH ROW EXECUTE FUNCTION dpt_guard.member_guard();
CREATE TRIGGER c_selection BEFORE INSERT OR UPDATE ON dpt.canonical_selections FOR EACH ROW EXECUTE FUNCTION dpt_guard.selection_guard();
CREATE TRIGGER m_materialize AFTER INSERT OR UPDATE ON dpt.canonical_selections FOR EACH ROW EXECUTE FUNCTION dpt_guard.materialize_scalar();
CREATE TRIGGER n_selection_audit AFTER INSERT OR UPDATE OR DELETE ON dpt.canonical_selections FOR EACH ROW EXECUTE FUNCTION dpt_guard.selection_audit();
CREATE TRIGGER n_conflict_audit AFTER INSERT OR UPDATE OR DELETE ON dpt.data_conflicts FOR EACH ROW EXECUTE FUNCTION dpt_guard.selection_audit();
CREATE TRIGGER n_parent_permission AFTER UPDATE ON dpt.image_assets FOR EACH ROW EXECUTE FUNCTION dpt_guard.invalidate_assets();
CREATE TRIGGER n_asset_revocation AFTER UPDATE OF revoked_at ON dpt.asset_permissions FOR EACH ROW EXECUTE FUNCTION dpt_guard.invalidate_assets();
CREATE TRIGGER n_source_revocation AFTER UPDATE OF revoked_at ON dpt.rights_assessments FOR EACH ROW EXECUTE FUNCTION dpt_guard.invalidate_assets();

-- Only add an FK index if no valid leading-column index already covers that tuple.
DO $$ DECLARE f record; cols text; BEGIN
 FOR f IN SELECT c.oid,c.conrelid,c.conname,c.conkey FROM pg_constraint c JOIN pg_namespace n ON n.oid=c.connamespace
   WHERE n.nspname='dpt' AND c.contype='f' LOOP
  IF NOT EXISTS(SELECT FROM pg_index i WHERE i.indrelid=f.conrelid AND i.indisvalid AND i.indpred IS NULL
    AND (i.indkey::smallint[])[0:cardinality(f.conkey)-1]=f.conkey) THEN
    SELECT string_agg(quote_ident(a.attname),',' ORDER BY k.ord) INTO cols
      FROM unnest(f.conkey) WITH ORDINALITY k(num,ord) JOIN pg_attribute a ON a.attrelid=f.conrelid AND a.attnum=k.num;
    EXECUTE format('CREATE INDEX %I ON %s (%s)',f.conname||'_idx',f.conrelid::regclass,cols);
  END IF;
 END LOOP;
END $$;

CREATE TRIGGER c_staging_capture BEFORE UPDATE OR DELETE ON dpt.staging_records FOR EACH ROW EXECUTE FUNCTION dpt_guard.staging_capture_guard();

CREATE INDEX brands_name_lookup ON dpt.brands ((lower(normalize(name,NFKC))));
CREATE INDEX perfumes_brand_name ON dpt.perfumes(brand_id,name);
CREATE INDEX source_records_timeline ON dpt.source_records(access_scope_id,source_id,external_key,retrieved_at);
CREATE INDEX ingestion_batches_state_time ON dpt.ingestion_batches(access_scope_id,state,started_at);
CREATE INDEX staging_records_batch_state ON dpt.staging_records(batch_id,state);
CREATE INDEX validation_results_result_severity ON dpt.validation_results(result,severity);
CREATE INDEX audit_events_entity_time ON dpt.audit_events(entity_id,occurred_at);
CREATE INDEX perfume_notes_lookup ON dpt.perfume_notes(note_id,layer,perfume_id);
CREATE INDEX perfume_families_lookup ON dpt.perfume_families(family_id,perfume_id);
CREATE INDEX comparison_evidence_lookup ON dpt.comparison_evidence(relation_id,claim_type);
CREATE INDEX price_observations_timeline ON dpt.price_observations(listing_id,observed_at DESC);

-- PostgreSQL numeric NaN sorts above finite values; positivity alone is insufficient.
DO $$ DECLARE col record; BEGIN
 FOR col IN SELECT c.relname,a.attname FROM pg_attribute a JOIN pg_class c ON c.oid=a.attrelid
  JOIN pg_namespace n ON n.oid=c.relnamespace JOIN pg_type t ON t.oid=a.atttypid
  WHERE n.nspname='dpt' AND c.relkind='r' AND a.attnum>0 AND NOT a.attisdropped AND t.typname='numeric' LOOP
  EXECUTE format('ALTER TABLE dpt.%I ADD CONSTRAINT %I CHECK (%I IS NULL OR %I NOT IN (''NaN''::numeric,''Infinity''::numeric,''-Infinity''::numeric))',
    col.relname,col.relname||'_'||col.attname||'_finite',col.attname,col.attname);
 END LOOP;
END $$;
