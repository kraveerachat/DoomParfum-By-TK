-- Trusted validation functions are not application RPCs. Execution grants are revoked in 007.
-- Local pilot writes serialize cross-row invariants. Read-committed is the supported write isolation.
CREATE FUNCTION dpt_guard.serialize_write() RETURNS trigger
LANGUAGE plpgsql SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
  IF current_setting('transaction_isolation') <> 'read committed' THEN
    RAISE EXCEPTION 'Local contract writes require read committed isolation' USING ERRCODE='25001';
  END IF;
  PERFORM pg_advisory_xact_lock(1900147);
  IF TG_OP='DELETE' THEN RETURN OLD; END IF;
  RETURN NEW;
END $$;

CREATE FUNCTION dpt_guard.principal_id() RETURNS uuid LANGUAGE sql STABLE SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT id FROM dpt.users WHERE auth_subject=session_user::text
$$;
CREATE FUNCTION dpt_guard.is_curator() RETURNS boolean LANGUAGE sql STABLE
SET search_path=pg_catalog,pg_temp AS $$
 SELECT pg_has_role(session_user,'dpt_curator','MEMBER')
$$;
CREATE FUNCTION dpt_guard.can_read_scope(scope_id uuid) RETURNS boolean LANGUAGE sql STABLE SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=scope_id AND
   (s.kind='public' OR s.owner_user_id=dpt_guard.principal_id() OR
    (s.kind='shared' AND EXISTS(SELECT FROM dpt.scope_members m WHERE m.access_scope_id=s.id
      AND m.user_id=dpt_guard.principal_id() AND m.revoked_at IS NULL))))
$$;
CREATE FUNCTION dpt_guard.can_write_scope(scope_id uuid) RETURNS boolean LANGUAGE sql STABLE SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT EXISTS(SELECT FROM dpt.access_scopes s WHERE s.id=scope_id AND
   ((s.kind='public' AND dpt_guard.is_curator()) OR s.owner_user_id=dpt_guard.principal_id() OR
    (s.kind='shared' AND EXISTS(SELECT FROM dpt.scope_members m WHERE m.access_scope_id=s.id
      AND m.user_id=dpt_guard.principal_id() AND m.role='editor' AND m.revoked_at IS NULL))))
$$;

CREATE FUNCTION dpt_guard.right_allowed(right_id uuid, operation text) RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT EXISTS(SELECT FROM dpt.rights_assessments r WHERE r.id=right_id AND
  r.revoked_at IS NULL AND r.checked_at<=statement_timestamp() AND
  (r.review_after IS NULL OR r.review_after>statement_timestamp()) AND
  r.evidence_url IS NOT NULL AND CASE operation
    WHEN 'storage' THEN r.storage_use='allowed' WHEN 'display' THEN r.display_use='allowed'
    WHEN 'automation' THEN r.automation_use='allowed' WHEN 'redistribution' THEN r.redistribution_use='allowed'
    WHEN 'cache' THEN r.cache_use='allowed' WHEN 'research' THEN r.research_use='allowed'
    WHEN 'ai' THEN r.ai_use='allowed' ELSE false END)
$$;
CREATE FUNCTION dpt_guard.record_allowed(record_id uuid, operation text) RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
 SELECT EXISTS(SELECT FROM dpt.source_records r WHERE r.id=record_id AND dpt_guard.right_allowed(r.rights_id,operation))
$$;

CREATE FUNCTION dpt_guard.identity_guard() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE n jsonb:=to_jsonb(NEW); o jsonb:=to_jsonb(OLD); key text;
BEGIN
  FOREACH key IN ARRAY ARRAY['id','access_scope_id','user_id','access_kind','entity_kind'] LOOP
    IF o ? key AND n->key IS DISTINCT FROM o->key THEN
      RAISE EXCEPTION 'Immutable identity/ownership' USING ERRCODE='23514';
    END IF;
  END LOOP;
  IF TG_TABLE_NAME='access_scopes' AND (n->'kind' IS DISTINCT FROM o->'kind' OR n->'owner_user_id' IS DISTINCT FROM o->'owner_user_id') THEN
    RAISE EXCEPTION 'Immutable access scope' USING ERRCODE='23514';
  ELSIF TG_TABLE_NAME='entities' AND n->'kind' IS DISTINCT FROM o->'kind' THEN
    RAISE EXCEPTION 'Immutable entity kind' USING ERRCODE='23514';
  ELSIF TG_TABLE_NAME='users' AND n->'auth_subject' IS DISTINCT FROM o->'auth_subject' THEN
    RAISE EXCEPTION 'Immutable authenticated subject' USING ERRCODE='23514';
  ELSIF TG_TABLE_NAME='image_assets' THEN
    FOREACH key IN ARRAY ARRAY['source_id','source_record_id','original_url','source_page_url','parent_asset_id'] LOOP
      IF n->key IS DISTINCT FROM o->key THEN RAISE EXCEPTION 'Immutable image capture identity' USING ERRCODE='23514'; END IF;
    END LOOP;
    IF OLD.sha256 IS NOT NULL AND NEW.sha256 IS DISTINCT FROM OLD.sha256 THEN
      RAISE EXCEPTION 'Changed image bytes require new asset identity' USING ERRCODE='23514';
    END IF;
  END IF;
  NEW.updated_at:=clock_timestamp();
  RETURN NEW;
END $$;

CREATE FUNCTION dpt_guard.append_only() RETURNS trigger LANGUAGE plpgsql
SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
  IF TG_OP='UPDATE' AND TG_TABLE_NAME IN ('rights_assessments','asset_permissions') AND
    (to_jsonb(OLD)->>'revoked_at') IS NULL AND (to_jsonb(NEW)->>'revoked_at') IS NOT NULL AND
    (to_jsonb(OLD)-'revoked_at'-'updated_at')=(to_jsonb(NEW)-'revoked_at'-'updated_at') THEN RETURN NEW; END IF;
  RAISE EXCEPTION 'Immutable evidence: append new version; only one-way permission revocation allowed'
    USING ERRCODE='23514';
END $$;

CREATE FUNCTION dpt_guard.compatible_targets() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE col text; target uuid; target_scope uuid; kind text; body jsonb:=to_jsonb(NEW);
BEGIN
  FOREACH col IN ARRAY TG_ARGV LOOP
    target:=(body->>col)::uuid;
    IF target IS NULL THEN CONTINUE; END IF;
    SELECT e.access_scope_id,s.kind INTO target_scope,kind FROM dpt.entities e JOIN dpt.access_scopes s ON s.id=e.access_scope_id WHERE e.id=target;
    IF NOT FOUND OR (kind<>'public' AND target_scope<>NEW.access_scope_id) THEN
      RAISE EXCEPTION 'Reference unavailable in this scope' USING ERRCODE='23514';
    END IF;
  END LOOP;
  RETURN NEW;
END $$;

CREATE FUNCTION dpt_guard.observation_guard() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE prev dpt.source_observations; expected text;
BEGIN
  SELECT * INTO prev FROM dpt.source_observations o WHERE
    (o.access_scope_id,o.source_record_id,o.entity_id,o.entity_kind,o.field_path,o.claim_locator,o.claim_key,o.transform_version)=
    (NEW.access_scope_id,NEW.source_record_id,NEW.entity_id,NEW.entity_kind,NEW.field_path,NEW.claim_locator,NEW.claim_key,NEW.transform_version);
  IF FOUND AND (prev.value IS DISTINCT FROM NEW.value OR prev.value_status IS DISTINCT FROM NEW.value_status) THEN
    RAISE EXCEPTION 'Deterministic claim identity produced different value/status' USING ERRCODE='23514';
  END IF;
  SELECT value_type INTO expected FROM dpt.field_definitions WHERE entity_kind=NEW.entity_kind AND path=NEW.field_path;
  IF NEW.value_status='present' AND (jsonb_typeof(NEW.value) IS DISTINCT FROM CASE WHEN expected='integer' THEN 'number' ELSE expected END
     OR (expected='integer' AND NEW.value::text !~ '^-?[0-9]+$')) THEN
    RAISE EXCEPTION 'Observation type differs from allowlisted field' USING ERRCODE='23514';
  END IF;
  IF NOT dpt_guard.record_allowed(NEW.source_record_id,'storage') THEN
    RAISE EXCEPTION 'Active source storage rights required for claim value' USING ERRCODE='23514';
  END IF;
  RETURN NEW;
END $$;

CREATE FUNCTION dpt_guard.member_guard() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
  IF NOT EXISTS(SELECT FROM dpt.access_scopes WHERE id=NEW.access_scope_id AND kind='shared') THEN
    RAISE EXCEPTION 'Membership applies only to shared scopes' USING ERRCODE='23514';
  END IF;
  RETURN NEW;
END $$;

CREATE FUNCTION dpt_guard.selection_guard() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE obs dpt.source_observations;
BEGIN
  SELECT * INTO obs FROM dpt.source_observations WHERE id=NEW.observation_id;
  IF NOT dpt_guard.is_curator() AND (NOT dpt_guard.can_write_scope(NEW.access_scope_id) OR NEW.reviewed_by<>session_user::text) THEN
    RAISE EXCEPTION 'Authorized reviewer required' USING ERRCODE='42501';
  END IF;
  IF NOT dpt_guard.record_allowed(obs.source_record_id,'storage') OR NOT dpt_guard.record_allowed(obs.source_record_id,'display') THEN
    RAISE EXCEPTION 'Selection requires active storage/display rights' USING ERRCODE='23514';
  END IF;
  IF NEW.reviewed_at>clock_timestamp() THEN RAISE EXCEPTION 'Future review timestamp' USING ERRCODE='23514'; END IF;
  RETURN NEW;
END $$;

CREATE FUNCTION dpt_guard.selection_audit() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE item jsonb; scope_id uuid; ent uuid;
BEGIN
  item:=CASE WHEN TG_OP='DELETE' THEN to_jsonb(OLD) ELSE to_jsonb(NEW) END;
  scope_id:=(item->>'access_scope_id')::uuid; ent:=(item->>'entity_id')::uuid;
  INSERT INTO dpt.audit_events(access_scope_id,entity_id,actor,action,before_selection,after_selection,reason)
  VALUES(scope_id,ent,session_user::text,TG_TABLE_NAME||':'||TG_OP,
    CASE WHEN TG_OP<>'INSERT' THEN to_jsonb(OLD) END,CASE WHEN TG_OP<>'DELETE' THEN to_jsonb(NEW) END,
    COALESCE(NULLIF(item->>'rationale',''),'Reviewed contract change'));
  RETURN NULL;
END $$;

-- Only this explicit scalar projection map can materialize a claim. Other paths remain source-specific.
CREATE FUNCTION dpt_guard.scalar_column(kind text,path text) RETURNS text LANGUAGE sql IMMUTABLE
SET search_path=pg_catalog,pg_temp AS $$
 SELECT CASE WHEN (kind,path) IN (('brand','name'),('brand','country_code'),('brand','website_url'),
 ('perfume','name'),('perfume','brand_id'),('perfume','edition_label'),('perfume','concentration_code'),('perfume','release_year'),
 ('perfume','gender_label'),('perfume','description'),('note','name'),('note','name_th'),('note','material_origin'),
 ('note','description'),('variant','perfume_id'),('variant','volume_ml'),('variant','packaging_code'),('variant','sku'),('variant','gtin'),
 ('accord','label'),('relation','relation_type'),('relation','directionality'),('relation','reference_perfume_id'),('relation','candidate_perfume_id')) THEN path ELSE NULL END
$$;
CREATE FUNCTION dpt_guard.kind_table(kind text) RETURNS text LANGUAGE sql IMMUTABLE
SET search_path=pg_catalog,pg_temp AS $$ SELECT CASE kind WHEN 'brand' THEN 'brands' WHEN 'perfume' THEN 'perfumes'
 WHEN 'variant' THEN 'product_variants' WHEN 'note' THEN 'notes' WHEN 'accord' THEN 'accords'
 WHEN 'image' THEN 'image_assets' WHEN 'relation' THEN 'perfume_relations' WHEN 'listing' THEN 'retail_listings' END $$;

CREATE FUNCTION dpt_guard.materialize_scalar() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE col text; tbl text; ob dpt.source_observations; target_scope uuid; typ text;
BEGIN
  col:=dpt_guard.scalar_column(NEW.entity_kind,NEW.field_path);
  SELECT access_scope_id INTO target_scope FROM dpt.entities WHERE id=NEW.entity_id;
  IF col IS NULL OR target_scope<>NEW.access_scope_id THEN RETURN NULL; END IF;
  tbl:=dpt_guard.kind_table(NEW.entity_kind);
  SELECT * INTO ob FROM dpt.source_observations WHERE id=NEW.observation_id;
  typ:=CASE col WHEN 'release_year' THEN 'smallint' WHEN 'volume_ml' THEN 'numeric(8,3)' WHEN 'brand_id' THEN 'uuid' WHEN 'perfume_id' THEN 'uuid' WHEN 'reference_perfume_id' THEN 'uuid' WHEN 'candidate_perfume_id' THEN 'uuid' ELSE 'text' END;
  EXECUTE format('UPDATE dpt.%I SET %I=($1 #>> ''{}'')::%s WHERE id=$2',tbl,col,typ) USING ob.value,NEW.entity_id;
  RETURN NULL;
END $$;

-- Current active rows are checked, never a deferred trigger's stale NEW tuple.
CREATE FUNCTION dpt_guard.validate_model() RETURNS void LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE e record; n integer; sel record; val jsonb; scope_id uuid; col text; tbl text; actual jsonb;
  j record; expected text; chosen dpt.source_observations; ids uuid[]; raw_label text; expected_count integer;
BEGIN
  FOR e IN SELECT id,access_scope_id,kind FROM dpt.entities LOOP
    tbl:=dpt_guard.kind_table(e.kind);
    EXECUTE format('SELECT count(*) FROM dpt.%I WHERE id=$1 AND access_scope_id=$2',tbl) INTO n USING e.id,e.access_scope_id;
    IF n<>1 THEN RAISE EXCEPTION 'Entity requires exactly its matching subtype' USING ERRCODE='23514'; END IF;
  END LOOP;
  IF EXISTS(SELECT FROM dpt.data_conflicts c WHERE (SELECT count(*) FROM dpt.conflict_members m
      WHERE m.access_scope_id=c.access_scope_id AND m.conflict_id=c.id)<2) THEN
    RAISE EXCEPTION 'Conflict requires at least two distinct members' USING ERRCODE='23514';
  END IF;
  IF EXISTS(SELECT FROM dpt.data_conflicts dc LEFT JOIN dpt.canonical_selections cs ON
    (cs.access_scope_id,cs.entity_id,cs.entity_kind,cs.field_path)=(dc.access_scope_id,dc.entity_id,dc.entity_kind,dc.field_path)
    WHERE dc.status='resolved' AND cs.observation_id IS DISTINCT FROM dc.resolution_observation_id) THEN
    RAISE EXCEPTION 'Resolved conflict and canonical selection must agree atomically' USING ERRCODE='23514'; END IF;
  IF EXISTS(SELECT FROM dpt.perfumes p WHERE p.matching_eligible AND (p.review_status<>'approved' OR
      EXISTS(SELECT FROM dpt.data_conflicts c WHERE c.entity_id=p.id AND c.access_scope_id=p.access_scope_id AND c.status='open'))) THEN
    RAISE EXCEPTION 'Unapproved/conflicted profile cannot be matching eligible' USING ERRCODE='23514';
  END IF;
  -- Validate parent transitions AND removal of a selected child against final approved rows.
  FOR e IN SELECT id,access_scope_id,kind FROM dpt.entities WHERE kind IN ('brand','perfume','variant','note','accord','relation') LOOP
    tbl:=dpt_guard.kind_table(e.kind);
    EXECUTE format('SELECT to_jsonb(t) FROM dpt.%I t WHERE id=$1',tbl) INTO actual USING e.id;
    IF actual->>'review_status'='approved' THEN
      FOR col IN SELECT key FROM jsonb_each(actual) WHERE dpt_guard.scalar_column(e.kind,key) IS NOT NULL LOOP
        IF actual->col<>'null'::jsonb AND NOT EXISTS(SELECT FROM dpt.canonical_selections cs WHERE
          cs.access_scope_id=e.access_scope_id AND cs.entity_id=e.id AND cs.entity_kind=e.kind AND cs.field_path=col) THEN
          RAISE EXCEPTION 'Approved scalar requires retained reviewed selection' USING ERRCODE='23514'; END IF;
      END LOOP;
    END IF;
  END LOOP;
  IF EXISTS(SELECT FROM dpt.perfume_relations rel WHERE rel.review_status='approved' AND
    rel.relation_type IN ('flanker_of','inspired_by') AND NOT EXISTS(SELECT FROM dpt.comparison_evidence ce
      WHERE ce.relation_id=rel.id AND ce.access_scope_id=rel.access_scope_id)) THEN
    RAISE EXCEPTION 'Approved flanker/inspiration requires source evidence' USING ERRCODE='23514'; END IF;
  IF EXISTS(SELECT FROM dpt.staging_records st WHERE st.state='promoted' AND (st.source_record_id IS NULL OR
    EXISTS(SELECT FROM dpt.validation_results vr WHERE vr.staging_record_id=st.id AND vr.result<>'pass') OR
    EXISTS(SELECT FROM unnest(ARRAY['shape','identity','rights','notes']) rule WHERE NOT EXISTS(
      SELECT FROM dpt.validation_results vr WHERE vr.staging_record_id=st.id AND vr.rule_code=rule AND vr.result='pass')))) THEN
    RAISE EXCEPTION 'Promoted staging requires passing shape/identity/rights/notes validation' USING ERRCODE='23514'; END IF;
  IF EXISTS(SELECT FROM dpt.perfume_notes pn JOIN dpt.notes nt ON nt.id=pn.note_id WHERE nt.review_status<>'approved') THEN
    RAISE EXCEPTION 'Canonical joins require reviewed note vocabulary' USING ERRCODE='23514'; END IF;
  IF EXISTS(SELECT FROM dpt.matching_results mr WHERE NOT dpt_guard.matching_inputs_valid(mr.access_scope_id,mr.coverage,false)
    OR mr.input_sha256<>dpt_guard.matching_hash(mr.access_scope_id,mr.algorithm_version,mr.coverage)
    OR (mr.similarity IS NOT NULL AND jsonb_array_length(mr.coverage->'observation_ids')=0)) THEN
    RAISE EXCEPTION 'Invalid scope/policy/observation-bound matching input contract' USING ERRCODE='23514'; END IF;
  FOR sel IN SELECT s.*,o.value,o.value_status,ent.access_scope_id AS target_scope FROM dpt.canonical_selections s
      JOIN dpt.source_observations o ON o.id=s.observation_id JOIN dpt.entities ent ON ent.id=s.entity_id LOOP
    col:=dpt_guard.scalar_column(sel.entity_kind,sel.field_path);
    IF col IS NOT NULL AND sel.target_scope=sel.access_scope_id THEN
      tbl:=dpt_guard.kind_table(sel.entity_kind);
      EXECUTE format('SELECT to_jsonb(t)->%L FROM dpt.%I t WHERE id=$1',col,tbl) INTO actual USING sel.entity_id;
      val:=CASE WHEN sel.value_status='present' THEN sel.value ELSE 'null'::jsonb END;
      IF actual IS DISTINCT FROM val THEN RAISE EXCEPTION 'Scalar materialization differs from selected claim' USING ERRCODE='23514'; END IF;
    END IF;
    tbl:=CASE WHEN sel.entity_kind='brand' AND sel.field_path='aliases' THEN 'brand_aliases'
      WHEN sel.entity_kind='note' AND sel.field_path='aliases' THEN 'note_aliases'
      WHEN sel.entity_kind='brand' AND sel.field_path='tags' THEN 'brand_tag_links'
      WHEN sel.entity_kind='perfume' AND sel.field_path='accords' THEN 'perfume_accords'
      WHEN sel.entity_kind='perfume' AND sel.field_path LIKE 'families.%' THEN 'perfume_families'
      WHEN sel.entity_kind='perfume' AND sel.field_path LIKE 'usage.%' THEN 'perfume_usage_tags' END;
    IF tbl IS NOT NULL THEN
      col:=CASE WHEN sel.entity_kind='brand' THEN 'brand_id' WHEN sel.entity_kind='note' THEN 'note_id' ELSE 'perfume_id' END;
      expected:=CASE WHEN tbl='perfume_families' THEN ' AND role='||quote_literal(split_part(sel.field_path,'.',2))
        WHEN tbl='perfume_usage_tags' THEN ' AND category='||quote_literal(split_part(sel.field_path,'.',2)) ELSE '' END;
      EXECUTE format('SELECT count(*) FROM dpt.%I WHERE access_scope_id=$1 AND %I=$2%s',tbl,col,expected)
        INTO n USING sel.access_scope_id,sel.entity_id;
      expected_count:=CASE WHEN sel.value_status<>'present' THEN 0 WHEN jsonb_typeof(sel.value)='array' THEN jsonb_array_length(sel.value) ELSE 1 END;
      IF n<>expected_count THEN RAISE EXCEPTION 'Whole-field association set is incomplete' USING ERRCODE='23514'; END IF;
    END IF;
    IF sel.entity_kind='perfume' AND sel.field_path LIKE 'notes.%' THEN
      IF sel.value_status<>'present' OR jsonb_typeof(sel.value)<>'array' THEN
        IF EXISTS(SELECT FROM dpt.perfume_notes pn WHERE pn.access_scope_id=sel.access_scope_id AND pn.perfume_id=sel.entity_id AND 'notes.'||pn.layer=sel.field_path) THEN
          RAISE EXCEPTION 'Unknown note selection must not materialize notes' USING ERRCODE='23514'; END IF;
        CONTINUE;
      END IF;
      IF EXISTS(SELECT FROM jsonb_array_elements(sel.value) v WHERE jsonb_typeof(v)<>'string' OR btrim(v #>> '{}')='') THEN
        RAISE EXCEPTION 'Note list requires nonempty source labels' USING ERRCODE='23514'; END IF;
      IF (SELECT count(*) FROM jsonb_array_elements(sel.value))<>(SELECT count(DISTINCT v) FROM jsonb_array_elements(sel.value) v) THEN
        RAISE EXCEPTION 'Repeated source note labels require review/quarantine, not silent deduplication' USING ERRCODE='23514'; END IF;
      expected_count:=jsonb_array_length(sel.value);
      SELECT count(*) INTO n FROM dpt.perfume_notes pn WHERE pn.access_scope_id=sel.access_scope_id AND pn.perfume_id=sel.entity_id AND 'notes.'||pn.layer=sel.field_path;
      IF n<>expected_count THEN RAISE EXCEPTION 'Whole selected note list must materialize atomically' USING ERRCODE='23514'; END IF;
      FOR j IN SELECT pn.*,nt.name AS note_name FROM dpt.perfume_notes pn JOIN dpt.notes nt ON nt.id=pn.note_id
          WHERE pn.access_scope_id=sel.access_scope_id AND pn.perfume_id=sel.entity_id AND 'notes.'||pn.layer=sel.field_path LOOP
        IF j.source_record_id<>(SELECT source_record_id FROM dpt.source_observations WHERE id=sel.observation_id) OR
           j.sort_order IS NULL OR j.sort_order>=expected_count THEN
          RAISE EXCEPTION 'Note provenance/order differs from whole-list selection' USING ERRCODE='23514'; END IF;
        raw_label:=sel.value->>j.sort_order;
        SELECT array_agg(DISTINCT candidate) INTO ids FROM (
          SELECT nt.id AS candidate FROM dpt.notes nt JOIN dpt.access_scopes sc ON sc.id=nt.access_scope_id
            WHERE (sc.kind='public' OR sc.id=sel.access_scope_id) AND lower(normalize(nt.name,NFKC))=lower(normalize(raw_label,NFKC))
          UNION ALL
          SELECT na.note_id FROM dpt.note_aliases na JOIN dpt.access_scopes sc ON sc.id=na.access_scope_id
            WHERE (sc.kind='public' OR sc.id=sel.access_scope_id) AND na.normalized_alias=lower(normalize(raw_label,NFKC))
        ) q;
        IF cardinality(ids) IS DISTINCT FROM 1 OR ids[1]<>j.note_id THEN
          RAISE EXCEPTION 'Ambiguous/unmapped note label requires review/quarantine' USING ERRCODE='23514'; END IF;
      END LOOP;
    END IF;
  END LOOP;
  IF EXISTS(SELECT FROM dpt.perfume_notes p WHERE NOT EXISTS(SELECT FROM dpt.canonical_selections s
    WHERE s.access_scope_id=p.access_scope_id AND s.entity_id=p.perfume_id AND s.entity_kind='perfume' AND s.field_path='notes.'||p.layer)) THEN
    RAISE EXCEPTION 'Canonical note join requires whole-field selection' USING ERRCODE='23514'; END IF;
  IF EXISTS(SELECT FROM dpt.perfume_notes p GROUP BY access_scope_id,perfume_id HAVING
    bool_or(layer='general') AND bool_or(layer<>'general')) THEN
    RAISE EXCEPTION 'Flat/general and pyramid materializations cannot coexist' USING ERRCODE='23514'; END IF;
  -- Every source-backed association must match an explicit whole-field selection and its source record.
  FOR j IN
    SELECT 'brand_aliases' AS typ,access_scope_id,brand_id AS entity_id,source_record_id,'aliases' AS path,to_jsonb(alias) AS item FROM dpt.brand_aliases
    UNION ALL SELECT 'note_aliases',access_scope_id,note_id,source_record_id,'aliases',to_jsonb(alias) FROM dpt.note_aliases
    UNION ALL SELECT 'brand_tag_links',l.access_scope_id,l.brand_id,l.source_record_id,'tags',jsonb_build_object('scheme',t.scheme,'code',t.code) FROM dpt.brand_tag_links l JOIN dpt.brand_tags t ON t.id=l.tag_id
    UNION ALL SELECT 'perfume_families',l.access_scope_id,l.perfume_id,l.source_record_id,'families.'||l.role,jsonb_build_object('scheme',f.scheme,'code',f.code) FROM dpt.perfume_families l JOIN dpt.families f ON f.id=l.family_id
    UNION ALL SELECT 'perfume_usage_tags',access_scope_id,perfume_id,source_record_id,'usage.'||category,jsonb_build_object('scheme',scheme,'label',label) FROM dpt.perfume_usage_tags
    UNION ALL SELECT 'perfume_accords',access_scope_id,perfume_id,source_record_id,'accords',jsonb_build_object('accord_id',accord_id,'strength',strength) FROM dpt.perfume_accords
  LOOP
    SELECT o.* INTO chosen FROM dpt.canonical_selections s JOIN dpt.source_observations o ON o.id=s.observation_id
      WHERE s.access_scope_id=j.access_scope_id AND s.entity_id=j.entity_id AND s.field_path=j.path;
    IF NOT FOUND OR chosen.source_record_id<>j.source_record_id OR chosen.value_status<>'present' OR
       NOT (chosen.value=j.item OR (jsonb_typeof(chosen.value)='array' AND chosen.value @> jsonb_build_array(j.item))) THEN
      RAISE EXCEPTION 'Association differs from reviewed whole-field claim' USING ERRCODE='23514'; END IF;
  END LOOP;
  IF EXISTS(SELECT FROM dpt.note_aliases WHERE normalized_alias<>lower(normalize(alias,NFKC))) OR
     EXISTS(SELECT FROM dpt.brand_aliases WHERE normalized_alias<>lower(normalize(alias,NFKC))) THEN
    RAISE EXCEPTION 'Alias normalization differs from local nfkc-lower-v1 contract' USING ERRCODE='23514'; END IF;
END $$;

CREATE FUNCTION dpt_guard.validate_deferred() RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER
SET search_path=pg_catalog,dpt,pg_temp AS $$ BEGIN PERFORM dpt_guard.validate_model(); RETURN NULL; END $$;

CREATE FUNCTION dpt_guard.staging_capture_guard() RETURNS trigger LANGUAGE plpgsql
SET search_path=pg_catalog,dpt,pg_temp AS $$
BEGIN
 IF TG_OP='DELETE' OR (to_jsonb(NEW)-'state'-'error_codes'-'source_record_id'-'updated_at') IS DISTINCT FROM
    (to_jsonb(OLD)-'state'-'error_codes'-'source_record_id'-'updated_at') THEN
  RAISE EXCEPTION 'Raw staging occurrences/capture identity are immutable; retention deletion needs a separately reviewed operation' USING ERRCODE='23514';
 END IF;
 RETURN NEW;
END $$;
CREATE FUNCTION dpt_guard.matching_hash(scope_id uuid,algorithm text,coverage jsonb) RETURNS text
LANGUAGE sql IMMUTABLE SET search_path=pg_catalog,pg_temp AS $$
 SELECT encode(sha256(convert_to(jsonb_build_object('scope',scope_id,'algorithm',algorithm,'coverage',coverage)::text,'UTF8')),'hex')
$$;
CREATE FUNCTION dpt_guard.matching_inputs_valid(scope_id uuid,coverage jsonb,active boolean) RETURNS boolean
LANGUAGE plpgsql STABLE SECURITY DEFINER SET search_path=pg_catalog,dpt,pg_temp AS $$
DECLARE item jsonb; obs dpt.source_observations; source_kind text;
BEGIN
 IF jsonb_typeof(coverage->'policy_version') IS DISTINCT FROM 'string' OR NULLIF(btrim(coverage->>'policy_version'),'') IS NULL OR
    jsonb_typeof(coverage->'observation_ids') IS DISTINCT FROM 'array' THEN RETURN false; END IF;
 IF (SELECT count(*) FROM jsonb_array_elements(coverage->'observation_ids'))<>
    (SELECT count(DISTINCT v) FROM jsonb_array_elements(coverage->'observation_ids') v) THEN RETURN false; END IF;
 FOR item IN SELECT * FROM jsonb_array_elements(coverage->'observation_ids') LOOP
  IF jsonb_typeof(item)<>'string' OR (item #>> '{}') !~ '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$' THEN RETURN false; END IF;
  SELECT * INTO obs FROM dpt.source_observations WHERE id=(item #>> '{}')::uuid;
  IF NOT FOUND THEN RETURN false; END IF;
  SELECT kind INTO source_kind FROM dpt.access_scopes WHERE id=obs.access_scope_id;
  IF source_kind<>'public' AND obs.access_scope_id<>scope_id THEN RETURN false; END IF;
  IF active AND (NOT dpt_guard.record_allowed(obs.source_record_id,'display') OR NOT dpt_guard.record_allowed(obs.source_record_id,'storage')) THEN RETURN false; END IF;
 END LOOP;
 RETURN true;
END $$;
