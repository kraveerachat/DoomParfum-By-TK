"""Clearly synthetic fixtures: not product facts, actual licenses, users or image bytes."""
import json
import uuid


def uid(name):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "doomparfum:synthetic:" + name))


def q(value):
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return "'" + json.dumps(value, ensure_ascii=False).replace("'", "''") + "'::jsonb"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def insert(table, **values):
    return f"INSERT INTO dpt.{table} ({','.join(values)}) VALUES ({','.join(q(v) for v in values.values())});\n"


def source(scope, suffix, allowed="allowed"):
    return (insert("sources", id=uid("src"+suffix), access_scope_id=uid(scope), name="Synthetic fixture source",
                   kind="user", entry_url="https://example.invalid/synthetic", publisher="SYNTHETIC TEST ONLY")
            + insert("rights_assessments", id=uid("right"+suffix), access_scope_id=uid(scope), source_id=uid("src"+suffix),
                     scope="SYNTHETIC, not an actual third-party grant", evidence_url="https://example.invalid/test-grant",
                     license_code="TEST-ONLY", research_use=allowed, automation_use=allowed, cache_use=allowed,
                     storage_use=allowed, display_use=allowed, redistribution_use=allowed, ai_use="unknown",
                     attribution="Synthetic fixture", checked_at="2026-01-01T00:00:00Z", reviewer="Synthetic test")
            + insert("source_records", id=uid("record"+suffix), access_scope_id=uid(scope), source_id=uid("src"+suffix),
                     external_key="synthetic"+suffix, payload_sha256="a"*64, source_url="https://example.invalid/capture",
                     locator="synthetic-document", source_revision="synthetic-v1", retrieved_at="2026-01-01T00:00:00Z",
                     rights_id=uid("right"+suffix)))


def entity(fixture_key, kind, table, scope="public", **values):
    return insert("entities", id=uid(fixture_key), access_scope_id=uid(scope), kind=kind) + insert(
        table, id=uid(fixture_key), access_scope_id=uid(scope), **values)


def observation(name, target="perfume", kind="perfume", path="notes.heart", value=None,
                scope="public", source_suffix="public", locator=None, key="list-1", status="present", transform="synthetic-v1"):
    # JSON scalars need JSON encoding, not a plain SQL string.
    value_sql = "NULL" if value is None else q(json.dumps(value, ensure_ascii=False)) + "::jsonb"
    text = insert("source_observations", id=uid(name), access_scope_id=uid(scope), entity_id=uid(target),
                  entity_kind=kind, field_path=path, source_record_id=uid("record"+source_suffix),
                  claim_locator=locator or name, claim_key=key, value_status=status, transform_version=transform)
    return text.replace(") VALUES (", ",value) VALUES (", 1).replace(");\n", ","+value_sql+");\n", 1)


def select(name, target="perfume", kind="perfume", path="notes.heart", scope="public", reviewer="postgres"):
    return insert("canonical_selections", access_scope_id=uid(scope), entity_id=uid(target), entity_kind=kind,
                  field_path=path, observation_id=uid(name), reviewed_by=reviewer,
                  reviewed_at="2026-01-01T00:00:00Z", rationale="Synthetic explicit review; not a product decision")


def note_join(note="rose", layer="heart", scope="public", source_suffix="public", order=0, name="note-join"):
    return insert("perfume_notes", id=uid(name), access_scope_id=uid(scope), perfume_id=uid("perfume"),
                  note_id=uid(note), layer=layer, sort_order=order, source_record_id=uid("record"+source_suffix))


def image(name, scope="public", source_suffix="public", parent=None, permission=None, state="validated"):
    perm = permission or name+"-permission"
    text = entity(name, "image", "image_assets", scope=scope, source_id=uid("src"+source_suffix),
                  source_record_id=uid("record"+source_suffix), rights_id=uid("right"+source_suffix),
                  source_page_url="https://example.invalid/synthetic-image", state="rights_pending",
                  checked_at="2026-01-01T00:00:00Z", parent_asset_id=uid(parent) if parent else None,
                  transform_spec={"changes":"Synthetic resize contract fixture"} if parent else None)
    text += insert("asset_permissions", id=uid(perm), access_scope_id=uid(scope), asset_id=uid(name),
                   source_id=uid("src"+source_suffix), source_record_id=uid("record"+source_suffix),
                   rights_id=uid("right"+source_suffix), asset_locator="asset:"+uid(name), content_sha256="b"*64,
                   permission_kind="derivative" if parent else "original", acquire_use="allowed", display_use="allowed",
                   transform_use="allowed", redistribution_use="allowed", evidence_locator="synthetic-proof-only",
                   output_license="TEST-ONLY", parent_asset_id=uid(parent) if parent else None,
                   parent_permission_id=uid(parent+"-permission") if parent else None,
                   reviewer="Synthetic test", checked_at="2026-01-01T00:00:00Z")
    text += f"UPDATE dpt.image_assets SET state={q(state)},asset_permission_id={q(uid(perm))},provider='synthetic',bucket='test-only',object_key={q(name)},mime_type='image/png',byte_size=1,width=1,height=1,sha256={q('b'*64)},attribution='SYNTHETIC; no real image',acquired_at='2026-01-01' WHERE id={q(uid(name))};\n"
    return text


def baseline():
    text = "BEGIN;\nDO $$ BEGIN\n"
    for role, groups in [("alice","dpt_runtime"),("bob","dpt_runtime"),("curator","dpt_runtime,dpt_writer,dpt_curator"),("guest","dpt_anonymous")]:
        name="dpt_test_"+role
        text += f"IF NOT EXISTS(SELECT FROM pg_roles WHERE rolname='{name}') THEN CREATE ROLE {name} LOGIN NOSUPERUSER NOBYPASSRLS; END IF; GRANT {groups} TO {name};\n"
    text += "END $$;\n"
    for user in ["alice","bob"]:
        text += insert("users", id=uid(user), auth_subject="dpt_test_"+user, display_name="SYNTHETIC "+user)
    text += insert("access_scopes", id=uid("public"), kind="public")
    for user in ["alice","bob"]:
        text += insert("access_scopes", id=uid(user), kind="user_private", owner_user_id=uid(user))
    text += insert("access_scopes", id=uid("shared"), kind="shared", owner_user_id=uid("alice"))
    text += insert("scope_members", access_scope_id=uid("shared"), user_id=uid("bob"), role="reader")
    for scope in ["public","alice","bob","shared"]:
        text += source(scope,scope)
    text += source("public","unknown",allowed="unknown")
    text += entity("brand","brand","brands",name="Toy Brand",slug="toy-brand")
    text += entity("perfume","perfume","perfumes",brand_id=uid("brand"),name="Toy Perfume",slug="toy-perfume")
    text += entity("perfume2","perfume","perfumes",brand_id=uid("brand"),name="Other Toy",slug="other-toy")
    for name,label in [("rose","Toy Rose"),("jasmine","Toy Jasmine")]:
        text += entity(name,"note","notes",name=label,slug=name)
    text += entity("variant","variant","product_variants",perfume_id=uid("perfume"),volume_ml=50)
    text += entity("variant2","variant","product_variants",perfume_id=uid("perfume2"),volume_ml=30)
    for name,kind,label in [("brand","brand","Toy Brand"),("perfume","perfume","Toy Perfume"),("rose","note","Toy Rose"),("jasmine","note","Toy Jasmine")]:
        claim="name-"+name
        text += observation(claim,target=name,kind=kind,path="name",value=label)+select(claim,target=name,kind=kind,path="name")
    text += observation("brand-ref",path="brand_id",value=uid("brand"))+select("brand-ref",path="brand_id")
    for table,name in [("brands","brand"),("perfumes","perfume"),("notes","rose"),("notes","jasmine")]:
        text += f"UPDATE dpt.{table} SET review_status='approved' WHERE id={q(uid(name))};\n"
    text += observation("top",path="notes.top",value=["Toy Rose"])+select("top",path="notes.top")+note_join(layer="top",name="top-join")
    text += observation("private-description",path="description",value="SYNTHETIC PRIVATE A",scope="alice",source_suffix="alice")
    text += select("private-description",path="description",scope="alice")
    for who in ["alice","bob"]:
        text += insert("user_lists",id=uid("list"+who),access_scope_id=uid(who),user_id=uid(who),name="Synthetic cart",list_type="cart")
        text += entity("listing"+who,"listing","retail_listings",scope=who,user_id=uid(who),perfume_id=uid("perfume"),
                       variant_id=uid("variant"),platform="synthetic",product_url="https://example.invalid/bookmark",source_record_id=uid("record"+who))
    text += image("public-image")+image("private-image",scope="alice",source_suffix="alice")
    text += insert("perfume_images",access_scope_id=uid("alice"),perfume_id=uid("perfume"),asset_id=uid("private-image"),role="bottle",sort_order=0)
    return text+"COMMIT;\n"
