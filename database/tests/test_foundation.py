"""Live PostgreSQL contracts; synthetic authorization fixtures only unless stated."""
import sys
from pathlib import Path
import unittest
import json
import hashlib
import csv
import tempfile
import concurrent.futures
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import local
from fixtures import uid, q, insert, source, entity, observation, select, note_join, image, baseline


class FoundationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        local.recreate("dpt_schema_test")
        local.migrate("dpt_schema_test")
        local.sql(baseline())

    def scalar(self, text, user="postgres"):
        return local.sql(text, user=user).stdout.strip()

    def succeeds(self, text, user="postgres"):
        return local.sql("BEGIN;\n"+text+"\nSET CONSTRAINTS ALL IMMEDIATE;\nROLLBACK;", user=user)

    def rejects(self, text, state="23514", user="postgres"):
        result = local.sql("BEGIN;\n"+text+"\nCOMMIT;", user=user, check=False)
        self.assertNotEqual(result.returncode, 0, "Invalid transaction unexpectedly committed")
        self.assertIn(state, result.stderr)
        return result

    def test_approved_47_table_model(self):
        count = local.sql("SELECT count(*) FROM information_schema.tables WHERE table_schema='dpt' AND table_type='BASE TABLE';").stdout.strip()
        self.assertEqual(count, "47")

    def test_model_names_match_approved_dictionary(self):
        import re
        dictionary = (local.ROOT / "Structure DB Obsidian/03_Data/Data_Dictionary_Draft.md").read_text(encoding="utf-8")
        expected = set(re.findall(r"^\| `([a-z_]+)` \|", dictionary, re.M))
        actual = set(self.scalar("SELECT tablename FROM pg_tables WHERE schemaname='dpt';").splitlines())
        self.assertEqual(actual, expected)

    def test_every_table_has_pk_rls_and_force_rls(self):
        self.assertEqual(self.scalar("SELECT count(*) FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='dpt' AND c.relkind='r' AND c.relrowsecurity AND c.relforcerowsecurity AND EXISTS(SELECT FROM pg_constraint p WHERE p.conrelid=c.oid AND p.contype='p');"), "47")

    def test_primary_key_and_dangling_fk(self):
        self.rejects(insert("users",id=uid("alice"),auth_subject="duplicate"),"23505")
        self.rejects(entity("bad-perfume","perfume","perfumes",brand_id=uid("absent"),name="Toy",slug="bad"))
        self.rejects(f"UPDATE dpt.brands SET country_code='ZZ' WHERE id={q(uid('brand'))};","23503")

    def test_entity_kind_and_incomplete_subtype(self):
        self.rejects(insert("entities",id=uid("orphan"),access_scope_id=uid("public"),kind="note"))
        self.rejects(insert("entities",id=uid("wrong-kind"),access_scope_id=uid("public"),kind="brand")+insert("notes",id=uid("wrong-kind"),access_scope_id=uid("public"),name="Wrong",slug="wrong"),"23503")
        self.rejects(f"DELETE FROM dpt.notes WHERE id={q(uid('jasmine'))};")

    def test_check_values_and_nullable_unknowns(self):
        for change in ["release_year=0","concentration_code=''","review_status='invented'"]:
            with self.subTest(change=change): self.rejects(f"UPDATE dpt.perfumes SET {change} WHERE id={q(uid('perfume2'))};")
        self.succeeds(f"UPDATE dpt.perfumes SET release_year=NULL,concentration_code=NULL WHERE id={q(uid('perfume2'))};")

    def test_obs01_structured_and_prose_same_capture_survive(self):
        script=observation("structured",value=["Toy Rose"],locator="structured/heart")+observation("prose",value=["Toy Jasmine"],locator="prose/heart")
        script+=insert("data_conflicts",id=uid("conflict"),access_scope_id=uid("public"),entity_id=uid("perfume"),entity_kind="perfume",field_path="notes.heart",status="open")
        for obs in ["structured","prose"]:
            script+=insert("conflict_members",access_scope_id=uid("public"),entity_id=uid("perfume"),entity_kind="perfume",field_path="notes.heart",conflict_id=uid("conflict"),observation_id=uid(obs))
        script+=f"SELECT count(*) FROM dpt.conflict_members WHERE conflict_id={q(uid('conflict'))};"
        self.assertEqual(self.succeeds(script).stdout.strip(),"2")

    def test_obs02_occurrences_exact_replay_and_changed_extraction(self):
        original=observation("occ1",value=["Toy Rose"],locator="same/locator",key="occ-0")
        self.succeeds(original+observation("occ2",value=["Toy Rose"],locator="same/locator",key="occ-1"))
        replay=original.replace(uid("occ1"),uid("replay")).replace(");\n",") ON CONFLICT DO NOTHING;\n")
        self.assertEqual(self.succeeds(original+replay+f"SELECT count(*) FROM dpt.source_observations WHERE claim_locator='same/locator';").stdout.strip(),"1")
        changed=replay.replace('["Toy Rose"]','["Toy Jasmine"]')
        self.rejects(original+changed)

    def test_obs03_nonempty_locator_key_type_and_scoped_selection(self):
        for field in ["claim_locator","claim_key","transform_version"]:
            with self.subTest(field=field):
                text=observation("invalid",value=["Toy Rose"]).replace(q("invalid") if field=="claim_locator" else q("list-1") if field=="claim_key" else q("synthetic-v1"),q("  "))
                self.rejects(text)
        self.rejects(observation("wrong-type",path="release_year",value="2022"))
        self.rejects(observation("wrong-observation-kind",kind="note",path="name",value="Toy",target="perfume"),"23503")
        self.rejects(select("top",path="notes.heart"),"23503")
        self.rejects(select("private-description",path="description"),"23503")
        self.rejects(select("top",target="perfume2",path="notes.top"),"23503")

    def conflict_setup(self):
        text=""
        for name,label in [("c1","Toy Rose"),("c2","Toy Jasmine"),("c3","Toy Rose")]: text+=observation(name,value=[label])
        text+=insert("data_conflicts",id=uid("conflict"),access_scope_id=uid("public"),entity_id=uid("perfume"),entity_kind="perfume",field_path="notes.heart",status="open")
        for name in ["c1","c2"]: text+=insert("conflict_members",access_scope_id=uid("public"),entity_id=uid("perfume"),entity_kind="perfume",field_path="notes.heart",conflict_id=uid("conflict"),observation_id=uid(name))
        return text

    def test_obs04_resolution_member_and_minimum_count(self):
        resolve=f"UPDATE dpt.data_conflicts SET status='resolved',resolution_observation_id={q(uid('c2'))},resolved_by='postgres',resolved_at=now(),rationale='Explicit synthetic choice' WHERE id={q(uid('conflict'))};"
        self.succeeds(self.conflict_setup()+resolve+select("c2")+note_join(note="jasmine"))
        self.rejects(self.conflict_setup()+resolve.replace(uid("c2"),uid("c3"))+select("c3")+note_join(),"23503")
        self.rejects(self.conflict_setup()+f"DELETE FROM dpt.conflict_members WHERE conflict_id={q(uid('conflict'))} AND observation_id={q(uid('c2'))};")
        self.rejects(self.conflict_setup()+resolve+f"DELETE FROM dpt.conflict_members WHERE observation_id={q(uid('c2'))};")
        third=insert("conflict_members",access_scope_id=uid("public"),entity_id=uid("perfume"),entity_kind="perfume",field_path="notes.heart",conflict_id=uid("conflict"),observation_id=uid("c3"))
        self.rejects(self.conflict_setup()+third+resolve+select("c2")+note_join(note="jasmine")+f"DELETE FROM dpt.conflict_members WHERE observation_id={q(uid('c2'))};","23503")

    def test_selection_does_not_silently_resolve_conflict(self):
        self.assertEqual(self.succeeds(self.conflict_setup()+select("c2")+note_join(note="jasmine")+f"SELECT status FROM dpt.data_conflicts WHERE id={q(uid('conflict'))};").stdout.strip(),"open")

    def test_immutable_claims_rights_and_capture(self):
        self.rejects(f"UPDATE dpt.source_observations SET value='[\"Changed\"]' WHERE id={q(uid('top'))};")
        self.rejects(f"DELETE FROM dpt.source_observations WHERE id={q(uid('top'))};")
        self.rejects(f"UPDATE dpt.source_records SET source_url='https://example.invalid/changed' WHERE id={q(uid('recordpublic'))};")
        self.rejects(f"UPDATE dpt.rights_assessments SET display_use='restricted' WHERE id={q(uid('rightpublic'))};")

    def test_materialization_and_audit_are_atomic(self):
        self.rejects(f"UPDATE dpt.perfumes SET name='Unselected' WHERE id={q(uid('perfume'))};")
        self.rejects(f"DELETE FROM dpt.perfume_notes WHERE id={q(uid('top-join'))};")
        self.rejects(f"UPDATE dpt.perfume_notes SET source_record_id={q(uid('recordunknown'))} WHERE id={q(uid('top-join'))};")
        self.assertGreater(int(self.scalar(f"SELECT count(*) FROM dpt.audit_events WHERE entity_id={q(uid('perfume'))};")),0)
        self.assertEqual(self.scalar(f"SELECT name FROM dpt.perfumes WHERE id={q(uid('perfume'))};"),"Toy Perfume")

    def test_repeated_raw_occurrences_preserved_and_promotion_blocked(self):
        text=observation("repeat-list",value=["Toy Rose","Toy Rose"])
        text+=observation("repeat-0",path="notes.heart",value=["Toy Rose"],locator="/heart_notes/0",key="ordinal-0")
        text+=observation("repeat-1",path="notes.heart",value=["Toy Rose"],locator="/heart_notes/1",key="ordinal-1")
        self.assertEqual(self.succeeds(text+f"SELECT jsonb_array_length(value) FROM dpt.source_observations WHERE id={q(uid('repeat-list'))};").stdout.strip(),"2")
        self.rejects(text+select("repeat-list")+note_join())

    def test_canonical_note_unique_and_cross_layer_identity(self):
        self.rejects(note_join(layer="top",name="exact-duplicate"),"23505")
        self.succeeds(observation("heart",value=["Toy Rose"])+select("heart")+note_join(name="heart-join"))

    def test_alias_collision_is_retained_ambiguous_mapping_blocked(self):
        text=""
        for note in ["rose","jasmine"]:
            text+=observation("alias-"+note,target=note,kind="note",path="aliases",value=["Shared Label"])+select("alias-"+note,target=note,kind="note",path="aliases")
            text+=insert("note_aliases",access_scope_id=uid("public"),note_id=uid(note),alias="Shared Label",normalized_alias="shared label",language="und",source_record_id=uid("recordpublic"))
        self.assertEqual(self.succeeds(text+"SELECT count(*) FROM dpt.note_aliases WHERE normalized_alias='shared label';").stdout.strip(),"2")
        self.rejects(text+observation("ambiguous",value=["Shared Label"])+select("ambiguous")+note_join())

    def test_active_rights_and_cross_source_fk(self):
        self.rejects(observation("unknown-grant",value=["Toy Rose"],source_suffix="unknown"))
        self.rejects(insert("source_records",access_scope_id=uid("public"),source_id=uid("srcpublic"),external_key="wrong",payload_sha256="c"*64,source_url="https://example.invalid",retrieved_at="2026-01-01",rights_id=uid("rightunknown")),"23503")

    def test_acl01_real_nonowner_sessions_private_overlay(self):
        self.assertEqual(self.scalar("SELECT session_user,current_user;",user="dpt_test_alice"),"dpt_test_alice|dpt_test_alice")
        self.assertEqual(self.scalar("SELECT rolsuper,rolbypassrls FROM pg_roles WHERE rolname=current_user;",user="dpt_test_alice"),"f|f")
        for who,expected in [("alice","1"),("bob","0")]:
            self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.canonical_selections WHERE access_scope_id={q(uid('alice'))};",user="dpt_test_"+who),expected)
        self.assertEqual(self.scalar(f"SELECT description IS NULL FROM dpt_public.perfumes WHERE id={q(uid('perfume'))};",user="dpt_test_guest"),"t")

    def test_acl02_private_overlay_does_not_mutate_public(self):
        for who in ["dpt_test_alice","dpt_test_bob","dpt_test_guest"]:
            self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt_public.perfumes WHERE description='SYNTHETIC PRIVATE A';",user=who),"0")
        self.rejects(select("private-description",scope="public",path="description"),"23503")

    def test_acl03_scope_owner_and_editable_identity_spoof(self):
        self.rejects(f"UPDATE dpt.sources SET access_scope_id={q(uid('public'))} WHERE id={q(uid('srcalice'))};")
        self.rejects(insert("user_lists",access_scope_id=uid("alice"),user_id=uid("bob"),name="Spoof",list_type="custom"),"23503")
        self.assertEqual(self.scalar(f"SET app.user_id={q(uid('alice'))}; SET app.scope_id={q(uid('alice'))}; SELECT count(*) FROM dpt.sources WHERE id={q(uid('srcalice'))};",user="dpt_test_bob"),"0")
        self.rejects("SET ROLE dpt_curator;","42501",user="dpt_test_bob")

    def test_acl04_shared_membership_revocation_and_no_private_inheritance(self):
        self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.sources WHERE id={q(uid('srcshared'))};",user="dpt_test_bob"),"1")
        local.sql(f"UPDATE dpt.scope_members SET revoked_at=now() WHERE access_scope_id={q(uid('shared'))} AND user_id={q(uid('bob'))};")
        try:
            self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.sources WHERE id={q(uid('srcshared'))};",user="dpt_test_bob"),"0")
        finally: local.sql(f"UPDATE dpt.scope_members SET revoked_at=NULL WHERE access_scope_id={q(uid('shared'))} AND user_id={q(uid('bob'))};")
        self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.retail_listings WHERE user_id={q(uid('alice'))};",user="dpt_test_bob"),"0")
        self.rejects(insert("scope_members",access_scope_id=uid("alice"),user_id=uid("bob"),role="reader"))

    def test_acl05_private_owner_perfume_variant_and_history(self):
        self.rejects(f"UPDATE dpt.retail_listings SET variant_id={q(uid('variant2'))} WHERE id={q(uid('listingalice'))};","23503")
        text=insert("purchase_records",id=uid("purchase"),access_scope_id=uid("alice"),user_id=uid("alice"),perfume_id=uid("perfume"),listing_id=uid("listingalice"),status="received")
        text+=insert("inventory_items",access_scope_id=uid("alice"),user_id=uid("alice"),perfume_id=uid("perfume"),purchase_record_id=uid("purchase"),status="finished")
        self.assertEqual(self.succeeds(text+f"DELETE FROM dpt.user_lists WHERE id={q(uid('listalice'))}; SELECT count(*) FROM dpt.purchase_records WHERE id={q(uid('purchase'))};").stdout.strip(),"1")
        self.rejects(insert("purchase_records",access_scope_id=uid("alice"),user_id=uid("alice"),perfume_id=uid("perfume"),listing_id=uid("listingbob"),status="ordered"),"23503")

    def test_acl06_grants_raw_staging_and_actual_force_owner(self):
        self.rejects("SELECT raw_payload FROM dpt.staging_records;","42501",user="dpt_test_guest")
        self.assertEqual(self.scalar("SELECT count(*) FROM dpt.source_records;",user="dpt_test_bob"),"2")  # Bob + shared; public raw denied.
        self.assertEqual(self.scalar("SET ROLE dpt_owner; SELECT count(*) FROM dpt.perfumes;"),"0")
        self.assertEqual(self.scalar("SELECT rolname,rolsuper,rolbypassrls FROM pg_roles WHERE rolname='dpt_owner';"),"dpt_owner|f|f")

    def test_acl07_untrusted_dml_and_hidden_reference_boolean(self):
        self.rejects(insert("user_lists",access_scope_id=uid("alice"),user_id=uid("alice"),name="Probe",list_type="custom"),"42501",user="dpt_test_alice")
        self.assertEqual(self.scalar(f"SELECT dpt_guard.can_use_asset({q(uid('private-image'))},'display'),dpt_guard.can_use_asset({q(uid('nonexistent'))},'display');",user="dpt_test_bob"),"f|f")
        self.rejects("SELECT dpt_guard.validate_model();","42501",user="dpt_test_alice")

    def test_with_check_prevents_new_scope_spoof_under_trusted_writer_grant(self):
        # Temporarily grant the isolated test login the trusted writer role to test RLS separately from grants.
        local.sql("GRANT dpt_writer TO dpt_test_alice;")
        try:
            self.succeeds(insert("user_lists",access_scope_id=uid("alice"),user_id=uid("alice"),name="Own",list_type="custom"),user="dpt_test_alice")
            self.rejects(insert("user_lists",access_scope_id=uid("bob"),user_id=uid("bob"),name="Other",list_type="custom"),"42501",user="dpt_test_alice")
        finally: local.sql("REVOKE dpt_writer FROM dpt_test_alice;")

    def test_img01_exact_capture_asset_assessment_binding(self):
        self.rejects(f"UPDATE dpt.image_assets SET rights_id={q(uid('rightunknown'))} WHERE id={q(uid('public-image'))};","23503")
        self.rejects(f"UPDATE dpt.image_assets SET asset_permission_id={q(uid('private-image-permission'))} WHERE id={q(uid('public-image'))};","23503")

    def test_img02_metadata_allowed_acquisition_missing_permission_rejected(self):
        text=entity("metadata","image","image_assets",source_id=uid("srcunknown"),source_record_id=uid("recordunknown"),rights_id=uid("rightunknown"),source_page_url="https://example.invalid",state="reference_only",checked_at="2026-01-01")
        self.succeeds(text)
        self.rejects(text+f"UPDATE dpt.image_assets SET state='acquired' WHERE id={q(uid('metadata'))};")
        self.rejects(image("unknown-source-acquire",source_suffix="unknown"))
        self.rejects(image("unknown-asset-acquire").replace("'original','allowed','allowed','allowed','allowed'","'original','unknown','allowed','allowed','allowed'"))

    def test_img03_derivative_exact_parent_and_output_obligations(self):
        self.succeeds(image("derivative",parent="public-image"))
        self.rejects(image("derivative",parent="public-image").replace("'TEST-ONLY'","'INCOMPATIBLE'"))
        self.rejects(image("derivative",parent="public-image").replace("Synthetic resize contract fixture",""))
        denied_parent=image("denied-parent").replace("'original','allowed','allowed','allowed','allowed'","'original','allowed','allowed','restricted','allowed'")
        self.rejects(denied_parent+image("denied-child",parent="denied-parent"))
        self.rejects(source("public","other-image-source")+image("other-source-child",source_suffix="other-image-source",parent="public-image"))

    def test_img04_hash_locator_and_immutable_capture(self):
        self.rejects(image("bad-hash").replace(q("b"*64),q("c"*64),1))
        self.rejects(f"UPDATE dpt.image_assets SET sha256={q('c'*64)} WHERE id={q(uid('public-image'))};")
        self.rejects(f"UPDATE dpt.image_assets SET original_url='https://example.invalid/swapped' WHERE id={q(uid('public-image'))};")

    def test_img05_revocation_descendants_and_expiry_operation_gate(self):
        text=image("child",parent="public-image")+f"UPDATE dpt.asset_permissions SET revoked_at=now() WHERE id={q(uid('public-image-permission'))};"
        text+=f"SELECT string_agg(state,',' ORDER BY id) FROM dpt.image_assets WHERE id IN ({q(uid('child'))},{q(uid('public-image'))});"
        self.assertEqual(self.succeeds(text).stdout.strip(),"rights_pending,rights_pending")
        # Expiry is evaluated at operation time, without a data-change trigger.
        expiry=image("expired").replace("reviewer,checked_at)","reviewer,checked_at,review_after)").replace("'Synthetic test','2026-01-01T00:00:00Z');","'Synthetic test','2026-01-01T00:00:00Z','2026-01-02T00:00:00Z');")
        self.rejects(expiry)

    def test_img06_public_link_cannot_reference_private_asset(self):
        self.rejects(insert("perfume_images",access_scope_id=uid("public"),perfume_id=uid("perfume"),asset_id=uid("private-image"),role="bottle",sort_order=0))
        self.assertEqual(self.scalar("SELECT count(*) FROM dpt.perfume_images;",user="dpt_test_guest"),"0")
        self.assertEqual(self.scalar("SELECT count(*) FROM dpt.perfume_images;",user="dpt_test_alice"),"1")

    def test_image_cycle_rejected(self):
        # New metadata IDs permit cycle setup; immediate FK is satisfied by inserting parent then updating.
        text=""
        for name in ["cycle1","cycle2"]: text+=entity(name,"image","image_assets",source_id=uid("srcpublic"),source_record_id=uid("recordpublic"),rights_id=uid("rightpublic"),source_page_url="https://example.invalid",state="reference_only",checked_at="2026-01-01")
        # In-place lineage change is deliberately rejected before a cycle can be committed.
        text+=f"UPDATE dpt.image_assets SET parent_asset_id={q(uid('cycle2'))} WHERE id={q(uid('cycle1'))};"
        self.rejects(text)

    def test_purchase_numeric_and_currency_checks(self):
        for values in [{"paid_price":1},{"volume_ml":0},{"paid_price":-1,"currency":"USD"},{"currency":"usd"},{"currency":"ZZZ"}]:
            with self.subTest(values=values): self.rejects(insert("purchase_records",access_scope_id=uid("alice"),user_id=uid("alice"),perfume_id=uid("perfume"),status="ordered",**values))

    def test_matching_rating_separation_and_null_score(self):
        text=entity("relation","relation","perfume_relations",reference_perfume_id=uid("perfume"),candidate_perfume_id=uid("perfume2"),relation_type="similar_to",directionality="directed")
        text+=insert("matching_results",access_scope_id=uid("public"),relation_id=uid("relation"),algorithm_version="synthetic-v1",input_sha256=self.scalar("SELECT dpt_guard.matching_hash("+q(uid("public"))+",'synthetic-v1',"+q({"policy_version":"synthetic","observation_ids":[]})+");"),coverage={"policy_version":"synthetic","observation_ids":[]},explanation={},computed_at="2026-01-01")
        self.succeeds(text)
        self.rejects(text+f"UPDATE dpt.matching_results SET similarity=101;")
        self.rejects(insert("rating_observations",access_scope_id=uid("public"),perfume_id=uid("perfume"),source_record_id=uid("recordpublic"),value=6,scale_min=1,scale_max=5,observed_at="2026-01-01"))

    def test_failed_transaction_leaves_no_partial_rows(self):
        name="rollback-user"
        self.rejects(insert("users",id=uid(name),auth_subject="synthetic-rollback")+"SELECT 1/0;","22012")
        self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.users WHERE id={q(uid(name))};"),"0")

    def test_migration_replay_is_noop_and_failed_migration_recovers(self):
        before=self.scalar("SELECT count(*) FROM dpt_ops.schema_migrations;")
        local.migrate("dpt_schema_test")
        self.assertEqual(self.scalar("SELECT count(*) FROM dpt_ops.schema_migrations;"),before)
        with tempfile.TemporaryDirectory(prefix="dpt-local-migration-") as directory:
            bad=Path(directory)/"999_failure_probe.sql"
            bad.write_text("CREATE TABLE dpt.failure_probe(id integer); SELECT 1/0;",encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError,"22012"): local.migrate("dpt_schema_test",extra=bad)
        self.assertEqual(self.scalar("SELECT to_regclass('dpt.failure_probe') IS NULL;"),"t")
        self.assertEqual(self.scalar("SELECT count(*) FROM dpt_ops.schema_migrations;"),before)
        local.migrate("dpt_schema_test")

    def test_local_data_package_hashes_and_duplicate_investigation(self):
        package=local.ROOT.parent/"DoomParfum Local Data/P1/20261110-221751"
        manifest=json.loads((package/"package_manifest.json").read_text(encoding="utf-8"))
        for record in manifest["files"]:
            data=(package/record["path"]).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(),record["sha256"])
        profiles=[json.loads(v) for v in (package/"raw/perfumes.jsonl").read_text(encoding="utf-8").splitlines()]
        import collections
        repeated=[(v["id"],layer,label,[i for i,x in enumerate(v[layer]) if x==label]) for v in profiles for layer in ["top_notes","heart_notes","base_notes"] for label,count in collections.Counter(v[layer]).items() if count>1]
        self.assertEqual(len(repeated),40);self.assertEqual(len({v[0] for v in repeated}),39)
        selected=[json.loads(v) for v in (package/"pilot/perfumes_12.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(selected),12)
        self.assertFalse({v["id"] for v in selected}&{v[0] for v in repeated})
        # Exact raw array, ordinal and stable source claim key remain representable without deduplication.
        profile=next(v for v in profiles if v["id"]==repeated[0][0]); layer=repeated[0][1]
        text=observation("real-repeated-array",value=profile[layer],locator="/"+layer)
        self.assertEqual(int(self.succeeds(text+f"SELECT jsonb_array_length(value) FROM dpt.source_observations WHERE id={q(uid('real-repeated-array'))};").stdout.strip()),len(profile[layer]))

    def test_exact_12_real_profiles_fit_draft_schema_without_persisting(self):
        package=local.ROOT.parent/"DoomParfum Local Data/P1/20261110-221751"
        rows=[json.loads(v) for v in (package/"pilot/perfumes_12.jsonl").read_text(encoding="utf-8").splitlines()]
        text=""
        with (package/"pilot/houses_5.csv").open(encoding="utf-8",newline="") as f: houses=list(csv.DictReader(f))
        with (package/"pilot/materials_candidates_58.csv").open(encoding="utf-8",newline="") as f: materials=list(csv.DictReader(f))
        self.assertEqual(len(houses),5);self.assertEqual(len(materials),58)
        for house in houses:
            text+=entity("shape-house-"+house["id"],"brand","brands",name=house["name"],slug="fixture-"+house["id"],country_code=None)
        for material in materials:
            key="shape-material-"+material["id"]
            text+=entity(key,"note","notes",name=material["name"],slug="fixture-"+material["id"])
            text+=observation("aliases-"+key,target=key,kind="note",path="aliases",value=[v.strip() for v in material["aliases"].split(';') if v.strip()])
        for row in rows:
            # This is a rollback-only shape test, not a canonical import/crosswalk or approved note mapping.
            text+=entity("real-shape-"+row["id"],"perfume","perfumes",brand_id=uid("shape-house-"+row["house_id"]),name=row["name"],slug="fixture-"+row["id"],release_year=row["year"],concentration_code=row["concentration"] or None)
            for field in ["top_notes","heart_notes","base_notes","notes"]:
                text+=observation("shape-"+row["id"]+field,target="real-shape-"+row["id"],path="notes."+{"top_notes":"top","heart_notes":"heart","base_notes":"base","notes":"general"}[field],value=row[field])
        text+="SELECT count(*) FROM dpt.perfumes WHERE slug LIKE 'fixture-%';"
        self.assertEqual(self.succeeds(text).stdout.strip(),"12")
        self.assertEqual(self.scalar("SELECT count(*) FROM dpt.perfumes WHERE slug LIKE 'fixture-%';"),"0")

    def test_approved_scalar_selection_cannot_be_deleted(self):
        self.rejects(f"DELETE FROM dpt.canonical_selections WHERE entity_id={q(uid('perfume'))} AND field_path='name';")

    def test_raw_staging_payload_and_capture_identity_cannot_change(self):
        batch=insert("ingestion_batches",id=uid("batch"),access_scope_id=uid("public"),source_id=uid("srcpublic"),rights_id=uid("rightpublic"),source_revision="synthetic",batch_sha256="e"*64,adapter_version="synthetic",state="pending",started_at="2026-01-01")
        staging=insert("staging_records",id=uid("stage"),access_scope_id=uid("public"),batch_id=uid("batch"),external_key="syntheticpublic",payload_sha256="a"*64,raw_payload={"notes":["Toy Rose","Toy Rose"]},state="pending")
        self.succeeds(batch+staging)
        self.rejects(batch+staging+f"UPDATE dpt.staging_records SET raw_payload='{{}}' WHERE id={q(uid('stage'))};")

    def test_child_validation_failure_cannot_leave_promoted_parent(self):
        text=insert("ingestion_batches",id=uid("batch"),access_scope_id=uid("public"),source_id=uid("srcpublic"),rights_id=uid("rightpublic"),source_revision="synthetic",batch_sha256="e"*64,adapter_version="synthetic",state="pending",started_at="2026-01-01")
        text+=insert("staging_records",id=uid("stage"),access_scope_id=uid("public"),batch_id=uid("batch"),external_key="syntheticpublic",payload_sha256="a"*64,source_record_id=uid("recordpublic"),raw_payload={"notes":["Toy Rose"]},state="promoted")
        for rule in ["shape","identity","rights","notes"]:
            text+=insert("validation_results",access_scope_id=uid("public"),staging_record_id=uid("stage"),rule_code=rule,severity="error",result="pass")
        text+="SET CONSTRAINTS ALL IMMEDIATE; SET CONSTRAINTS ALL DEFERRED;"
        self.succeeds(text)
        self.rejects(text+f"UPDATE dpt.validation_results SET result='fail' WHERE staging_record_id={q(uid('stage'))} AND rule_code='notes';")

    def test_alias_selection_cannot_survive_deleted_materialization(self):
        text=observation("alias-solo",target="rose",kind="note",path="aliases",value=["Rose Alias"])+select("alias-solo",target="rose",kind="note",path="aliases")
        text+=insert("note_aliases",id=uid("alias-solo"),access_scope_id=uid("public"),note_id=uid("rose"),alias="Rose Alias",normalized_alias="rose alias",language="und",source_record_id=uid("recordpublic"))
        self.succeeds(text)
        self.rejects(text+f"DELETE FROM dpt.note_aliases WHERE id={q(uid('alias-solo'))};")

    def test_null_image_mime_cannot_bypass_acquired_state(self):
        self.rejects(f"UPDATE dpt.image_assets SET mime_type=NULL WHERE id={q(uid('public-image'))};")

    def test_public_matching_cannot_use_private_observation(self):
        text=entity("private-input-relation","relation","perfume_relations",reference_perfume_id=uid("perfume2"),candidate_perfume_id=uid("perfume"),relation_type="similar_to",directionality="directed")
        coverage={"policy_version":"synthetic","observation_ids":[uid("private-description")]}
        valid_hash=self.scalar("SELECT dpt_guard.matching_hash("+q(uid("public"))+",'synthetic',"+q(coverage)+");")
        text+=insert("matching_results",access_scope_id=uid("public"),relation_id=uid("private-input-relation"),algorithm_version="synthetic",input_sha256=valid_hash,coverage=coverage,explanation={},computed_at="2026-01-01")
        self.rejects(text)

    def test_shared_reader_cannot_write_or_self_enroll_even_with_table_grant(self):
        local.sql("GRANT dpt_writer TO dpt_test_bob;")
        try:
            self.rejects(f"UPDATE dpt.sources SET name='Spoof' WHERE id={q(uid('srcshared'))}; SELECT 1/(SELECT CASE WHEN name='Spoof' THEN 1 ELSE 0 END FROM dpt.sources WHERE id={q(uid('srcshared'))});","22012",user="dpt_test_bob")
            self.rejects(insert("scope_members",access_scope_id=uid("shared"),user_id=uid("bob"),role="editor"),"42501",user="dpt_test_bob")
        finally: local.sql("REVOKE dpt_writer FROM dpt_test_bob;")

    def test_expiry_is_rechecked_after_clock_passes(self):
        text=image("clock-expiry").replace("reviewer,checked_at)","reviewer,checked_at,review_after)").replace("'Synthetic test','2026-01-01T00:00:00Z');","'Synthetic test','2026-01-01T00:00:00Z',clock_timestamp()+interval '2 seconds');")
        local.sql("BEGIN;"+text+"COMMIT;")
        try:
            self.assertEqual(self.scalar(f"SELECT dpt_guard.can_use_asset({q(uid('clock-expiry'))},'display');",user="dpt_test_alice"),"t")
            time.sleep(2.1)
            self.assertEqual(self.scalar(f"SELECT dpt_guard.can_use_asset({q(uid('clock-expiry'))},'display');",user="dpt_test_alice"),"f")
        finally: local.sql(f"UPDATE dpt.image_assets SET state='rights_pending' WHERE id={q(uid('clock-expiry'))};")

    def test_parent_selected_permission_change_invalidates_derivative(self):
        text=image("replacement-child",parent="public-image")
        text+=insert("asset_permissions",id=uid("replacement-permission"),access_scope_id=uid("public"),asset_id=uid("public-image"),source_id=uid("srcpublic"),source_record_id=uid("recordpublic"),rights_id=uid("rightpublic"),asset_locator="asset:"+uid("public-image"),content_sha256="b"*64,permission_kind="original",acquire_use="allowed",display_use="allowed",transform_use="restricted",redistribution_use="allowed",evidence_locator="Synthetic renewed grant",output_license="TEST-ONLY",reviewer="Synthetic test",checked_at="2026-01-01")
        text+=f"UPDATE dpt.image_assets SET asset_permission_id={q(uid('replacement-permission'))} WHERE id={q(uid('public-image'))};"
        self.assertEqual(self.succeeds(text+f"SELECT state FROM dpt.image_assets WHERE id={q(uid('replacement-child'))};").stdout.strip(),"rights_pending")

    def test_same_source_different_capture_permission_rejected(self):
        text=insert("source_records",id=uid("recordpublic2"),access_scope_id=uid("public"),source_id=uid("srcpublic"),external_key="other-capture",payload_sha256="c"*64,source_url="https://example.invalid/second-capture",retrieved_at="2026-01-01",rights_id=uid("rightpublic"))
        text+=insert("asset_permissions",access_scope_id=uid("public"),asset_id=uid("public-image"),source_id=uid("srcpublic"),source_record_id=uid("recordpublic2"),rights_id=uid("rightpublic"),asset_locator="asset:"+uid("public-image"),content_sha256="b"*64,permission_kind="original",acquire_use="allowed",display_use="allowed",transform_use="allowed",redistribution_use="allowed",evidence_locator="Synthetic mismatched capture",reviewer="Synthetic test",checked_at="2026-01-01")
        self.rejects(text,"23503")

    def test_shared_owner_can_grant_editor_without_public_write_access(self):
        local.sql("GRANT dpt_writer TO dpt_test_alice,dpt_test_bob;")
        try:
            local.sql(f"UPDATE dpt.scope_members SET role='editor' WHERE access_scope_id={q(uid('shared'))} AND user_id={q(uid('bob'))};",user="dpt_test_alice")
            self.assertEqual(self.succeeds(f"UPDATE dpt.sources SET name='Edited shared fixture' WHERE id={q(uid('srcshared'))}; SELECT name FROM dpt.sources WHERE id={q(uid('srcshared'))};",user="dpt_test_bob").stdout.strip(),"Edited shared fixture")
            self.assertEqual(self.succeeds(f"UPDATE dpt.sources SET name='Spoofed public' WHERE id={q(uid('srcpublic'))}; SELECT count(*) FROM dpt.sources WHERE name='Spoofed public';",user="dpt_test_bob").stdout.strip(),"0")
        finally:
            local.sql(f"UPDATE dpt.scope_members SET role='reader' WHERE access_scope_id={q(uid('shared'))} AND user_id={q(uid('bob'))}; REVOKE dpt_writer FROM dpt_test_alice,dpt_test_bob;")

    def test_shadowed_temp_schema_cannot_spoof_principal(self):
        text=f"CREATE TEMP TABLE users(id uuid,auth_subject text); INSERT INTO users VALUES({q(uid('alice'))},'dpt_test_bob'); SET search_path=pg_temp,public; SELECT dpt_guard.principal_id();"
        self.assertEqual(self.scalar(text,user="dpt_test_bob"),uid("bob"))
        self.rejects("SET SESSION AUTHORIZATION dpt_test_alice;","42501",user="dpt_test_bob")

    def test_all_declared_fks_are_validated_and_indexed(self):
        self.assertEqual(self.scalar("SELECT count(*) FROM pg_constraint c JOIN pg_namespace n ON n.oid=c.connamespace WHERE n.nspname='dpt' AND NOT c.convalidated;"),"0")
        query="""SELECT count(*) FROM pg_constraint c JOIN pg_namespace n ON n.oid=c.connamespace
          WHERE n.nspname='dpt' AND c.contype='f' AND NOT EXISTS(SELECT FROM pg_index i
          WHERE i.indrelid=c.conrelid AND i.indisvalid AND i.indpred IS NULL
          AND (i.indkey::smallint[])[0:cardinality(c.conkey)-1]=c.conkey);"""
        self.assertEqual(self.scalar(query),"0")

    def test_audit_events_are_append_only(self):
        self.rejects("DELETE FROM dpt.audit_events;")
        self.rejects("UPDATE dpt.audit_events SET actor='spoof';")

    def test_promoted_staging_needs_complete_validation_contract(self):
        text=insert("ingestion_batches",id=uid("incomplete-batch"),access_scope_id=uid("public"),source_id=uid("srcpublic"),rights_id=uid("rightpublic"),source_revision="synthetic-incomplete",batch_sha256="e"*64,adapter_version="synthetic",state="pending",started_at="2026-01-01")
        text+=insert("staging_records",id=uid("incomplete-stage"),access_scope_id=uid("public"),batch_id=uid("incomplete-batch"),external_key="syntheticpublic",payload_sha256="a"*64,source_record_id=uid("recordpublic"),raw_payload={},state="promoted")
        text+=insert("validation_results",access_scope_id=uid("public"),staging_record_id=uid("incomplete-stage"),rule_code="shape",severity="error",result="pass")
        self.rejects(text)

    def test_unknown_rights_cannot_store_raw_staging(self):
        text=insert("ingestion_batches",id=uid("unknown-batch"),access_scope_id=uid("public"),source_id=uid("srcunknown"),rights_id=uid("rightunknown"),source_revision="unknown",batch_sha256="e"*64,adapter_version="synthetic",state="pending",started_at="2026-01-01")
        text+=insert("staging_records",access_scope_id=uid("public"),batch_id=uid("unknown-batch"),external_key="syntheticunknown",payload_sha256="a"*64,raw_payload={},state="pending")
        self.rejects(text)

    def test_conflicted_profile_cannot_be_matching_eligible(self):
        self.rejects(self.conflict_setup()+f"UPDATE dpt.perfumes SET matching_eligible=true WHERE id={q(uid('perfume'))};")

    def test_write_isolation_contract_rejects_stale_snapshot_mode(self):
        result=local.sql("BEGIN ISOLATION LEVEL REPEATABLE READ; "+insert("users",auth_subject="stale-snapshot")+"COMMIT;",check=False)
        self.assertNotEqual(result.returncode,0);self.assertIn("25001",result.stderr)

    def test_reset_recreate_matches_current_schema(self):
        local.recreate("dpt_migration_probe")
        local.migrate("dpt_migration_probe")
        signature="""SELECT jsonb_build_object('tables',(SELECT count(*) FROM pg_tables WHERE schemaname='dpt'),
          'constraints',(SELECT jsonb_agg(conname ORDER BY conname) FROM pg_constraint c JOIN pg_namespace n ON n.oid=c.connamespace WHERE n.nspname='dpt'),
          'policies',(SELECT count(*) FROM pg_policies WHERE schemaname='dpt'));"""
        self.assertEqual(json.loads(local.sql(signature,db="dpt_migration_probe").stdout),json.loads(self.scalar(signature)))
        self.assertEqual(local.sql("SELECT count(*) FROM dpt.users;",db="dpt_migration_probe").stdout.strip(),"0")

    def test_z_concurrent_member_deletions_cannot_write_skew(self):
        text=self.conflict_setup()
        text+=insert("conflict_members",access_scope_id=uid("public"),entity_id=uid("perfume"),entity_kind="perfume",field_path="notes.heart",conflict_id=uid("conflict"),observation_id=uid("c3"))
        local.sql("BEGIN;"+text+"COMMIT;")
        first=f"BEGIN; DELETE FROM dpt.conflict_members WHERE conflict_id={q(uid('conflict'))} AND observation_id={q(uid('c2'))}; SELECT pg_sleep(0.8); COMMIT;"
        second=f"BEGIN; DELETE FROM dpt.conflict_members WHERE conflict_id={q(uid('conflict'))} AND observation_id={q(uid('c3'))}; COMMIT;"
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(local.sql,first,check=False);time.sleep(0.2);b=pool.submit(local.sql,second,check=False)
            results=[a.result(),b.result()]
        self.assertEqual(sum(v.returncode==0 for v in results),1)
        self.assertTrue(any("23514" in v.stderr for v in results))
        self.assertEqual(self.scalar(f"SELECT count(*) FROM dpt.conflict_members WHERE conflict_id={q(uid('conflict'))};"),"2")
        local.sql(f"BEGIN; DELETE FROM dpt.conflict_members WHERE conflict_id={q(uid('conflict'))}; DELETE FROM dpt.data_conflicts WHERE id={q(uid('conflict'))}; COMMIT;")

    def test_review_guard_resolved_conflict_requires_matching_selection(self):
        text=self.conflict_setup()+f"UPDATE dpt.data_conflicts SET status='resolved',resolution_observation_id={q(uid('c2'))},resolved_by='postgres',resolved_at=now(),rationale='Explicit synthetic choice' WHERE id={q(uid('conflict'))};"
        self.rejects(text)

    def test_review_guard_private_variant_of_public_perfume_is_not_shared(self):
        text=entity("private-variant-b","variant","product_variants",scope="bob",perfume_id=uid("perfume"),volume_ml=100)
        text+=f"UPDATE dpt.retail_listings SET variant_id={q(uid('private-variant-b'))} WHERE id={q(uid('listingalice'))};"
        self.rejects(text)

    def test_taxonomy_namespace_and_usage_materialization(self):
        text=insert("families",id=uid("scento-family"),scheme="scento",code="toy-amber",label="Synthetic amber")
        text+=insert("families",id=uid("other-family"),scheme="other",code="toy-amber",label="Synthetic alternate taxonomy")
        text+=observation("family",path="families.primary",value={"scheme":"scento","code":"toy-amber"})+select("family",path="families.primary")
        text+=insert("perfume_families",access_scope_id=uid("public"),perfume_id=uid("perfume"),family_id=uid("scento-family"),role="primary",source_record_id=uid("recordpublic"))
        self.succeeds(text)
        self.rejects(text.replace(q(uid("scento-family"))+",'primary'",q(uid("other-family"))+",'primary'"))
        usage=observation("usage",path="usage.season",value=[{"scheme":"scento","label":"winter"}])+select("usage",path="usage.season")
        usage+=insert("perfume_usage_tags",access_scope_id=uid("public"),perfume_id=uid("perfume"),category="season",label="winter",scheme="scento",source_record_id=uid("recordpublic"))
        self.succeeds(usage)

    def test_two_row_image_cycle_fails_deferred_lineage_validation(self):
        text="".join(insert("entities",id=uid(name),access_scope_id=uid("public"),kind="image") for name in ["cycle-a","cycle-b"])
        columns="id,access_scope_id,source_id,source_record_id,rights_id,source_page_url,state,checked_at,parent_asset_id"
        values=[]
        for name,parent in [("cycle-a","cycle-b"),("cycle-b","cycle-a")]:
            values.append("("+",".join(q(v) for v in [uid(name),uid("public"),uid("srcpublic"),uid("recordpublic"),uid("rightpublic"),"https://example.invalid/cycle","reference_only","2026-01-01",uid(parent)])+")")
        text+="INSERT INTO dpt.image_assets ("+columns+") VALUES "+",".join(values)+";"
        result=self.rejects(text)
        self.assertIn("Cyclic image lineage",result.stderr)

    def test_approved_flanker_requires_reviewed_source_evidence(self):
        text=entity("unbacked-flanker","relation","perfume_relations",reference_perfume_id=uid("perfume"),candidate_perfume_id=uid("perfume2"),relation_type="flanker_of",directionality="directed")
        for path,value in [('reference_perfume_id',uid('perfume')),('candidate_perfume_id',uid('perfume2')),('relation_type','flanker_of'),('directionality','directed')]:
            text+=observation('flanker-'+path,target='unbacked-flanker',kind='relation',path=path,value=value)+select('flanker-'+path,target='unbacked-flanker',kind='relation',path=path)
        text+=f"UPDATE dpt.perfume_relations SET review_status='approved' WHERE id={q(uid('unbacked-flanker'))};"
        self.rejects(text)
        self.succeeds(text+insert('comparison_evidence',access_scope_id=uid('public'),relation_id=uid('unbacked-flanker'),source_record_id=uid('recordpublic'),claim_type='synthetic relationship source'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
