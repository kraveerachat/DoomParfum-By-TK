"""Scoped read-only local reference adapter; no scoring/public export or DB writes.

The trusted transport executes the ENTIRE script on one authenticated PostgreSQL
connection, stops on the first error, and returns its sole JSON object. It must not
retry under an administrator, change role, or accept SQL from an application caller.
Application authentication, API and public serialization remain separate gates.
"""
from __future__ import annotations

from dataclasses import dataclass
import datetime
from enum import Enum
import json
from typing import Callable
import unicodedata
import uuid

VERSION = 'matching-input-local-v1'
LAYERS = ('top','heart','base','general')
FIELDS = ('name','brand_id','concentration_code','release_year',*(f'notes.{x}' for x in LAYERS))


class State(str, Enum):
    USABLE = 'known_usable'
    INCOMPLETE = 'known_incomplete'
    UNKNOWN = 'unknown'
    HELD = 'conflicted_or_held'
    RIGHTS = 'rights_unavailable'
    ELIGIBILITY = 'eligibility_unavailable'


class InputUnavailable(ValueError):
    """Uniform missing/unauthorized/malformed ID; no existence or source details."""


class AdapterUnavailable(RuntimeError):
    """Transport/authentication contract failure, without private SQL/data in errors."""


@dataclass(frozen=True)
class Provenance:
    observation_id: str
    source_record_id: str
    rights_id: str
    source_url: str
    source_revision: str | None
    payload_sha256: str
    claim_locator: str
    transform_version: str
    reviewed_at: str
    source_id: str
    publisher: str
    license_code: str | None
    license_url: str | None
    attribution: str | None
    usage_scope: str
    rights_checked_at: str
    rights_review_after: str | None


@dataclass(frozen=True)
class Field:
    state: State
    value: object = None
    provenance: Provenance | None = None
    reason: str = ''


@dataclass(frozen=True)
class Note:
    id: str
    name: str
    provenance: Provenance


@dataclass(frozen=True)
class ProfileInput:
    id: str
    state: State
    review_status: str
    matching_eligible: bool
    fields: tuple[tuple[str,Field], ...]
    brand_name: Field
    layers: tuple[tuple[str,Field], ...]
    ranking_allowed: bool = False
    completeness: str = 'unknown_no_accepted_closure_contract'
    aliases: str = 'unavailable_no_reviewed_alias_contract'
    accords: str = 'unavailable_no_reviewed_scale_or_presence_contract'
    family: str = 'unavailable_no_selected_taxonomy_contract'
    currentness: str = 'unknown_no_selected_lifecycle_contract'
    data_confidence: str = 'not_evaluated_policy_pending'
    pairwise_evidence: str = 'not_queried_separate_contract'
    version: str = VERSION


def canonical_id(value):
    try:
        if not isinstance(value,str):
            raise ValueError()
        result=str(uuid.UUID(value))
        if result != value.lower():
            raise ValueError()
        return result
    except (ValueError,AttributeError,TypeError):
        raise InputUnavailable('Input unavailable') from None


def normalized(value):
    return unicodedata.normalize('NFKC',value).lower()


def _rights(alias):
    # Alias names are internal constants, never request values. No dynamic use downgrade.
    return f"""({alias}.id IS NOT NULL AND {alias}.evidence_url IS NOT NULL
      AND btrim({alias}.evidence_url)<>'' AND {alias}.revoked_at IS NULL
      AND {alias}.checked_at<=statement_timestamp()
      AND ({alias}.review_after IS NULL OR {alias}.review_after>statement_timestamp())
      AND {alias}.storage_use='allowed' AND {alias}.display_use='allowed'
      AND {alias}.automation_use='allowed')"""


def query(profile_id):
    ident=canonical_id(profile_id)
    return """BEGIN READ ONLY;
SET LOCAL statement_timeout='3s';
SET LOCAL lock_timeout='1s';
SET LOCAL row_security=on;
DO $gate$ BEGIN
 IF current_setting('transaction_read_only')<>'on'
 OR session_user<>current_user OR NOT pg_has_role(session_user,'dpt_runtime','MEMBER')
 OR pg_has_role(session_user,'dpt_owner','MEMBER')
 OR EXISTS(SELECT FROM pg_roles WHERE rolname IN (session_user,current_user) AND (rolsuper OR rolbypassrls))
 THEN RAISE EXCEPTION 'Adapter session unavailable' USING ERRCODE='42501'; END IF;
END $gate$;
WITH profile AS MATERIALIZED (
 SELECT p.id,p.access_scope_id,p.brand_id,p.name,p.concentration_code,p.release_year,
        p.review_status,p.matching_eligible
 FROM dpt.perfumes p WHERE p.id='"""+ident+"""'::uuid
 AND dpt_guard.can_read_scope(p.access_scope_id)
), note_links AS MATERIALIZED (
 SELECT a.* FROM dpt.perfume_notes a JOIN profile p
 ON (a.perfume_id,a.access_scope_id)=(p.id,p.access_scope_id)
 ORDER BY a.layer,a.sort_order NULLS LAST,a.id LIMIT 513
), targets AS MATERIALIZED (
 SELECT p.id FROM profile p
 UNION SELECT p.brand_id FROM profile p
 UNION SELECT note_id FROM note_links
), meta AS MATERIALIZED (
 SELECT s.entity_id,s.entity_kind,s.field_path,s.observation_id,s.reviewed_at,
        o.source_record_id,o.claim_locator,o.transform_version,o.value_status,
        r.rights_id,r.source_url,r.source_revision,r.payload_sha256,r.source_id,src.publisher,
        g.license_code,g.license_url,g.attribution,g.scope AS usage_scope,
        g.checked_at AS rights_checked_at,g.review_after AS rights_review_after,
        """+_rights('g')+""" AS allowed,
        EXISTS(SELECT FROM dpt.data_conflicts c WHERE
          (c.access_scope_id,c.entity_id,c.entity_kind,c.field_path)=
          (s.access_scope_id,s.entity_id,s.entity_kind,s.field_path)
          AND (c.status='open' OR (c.status='resolved' AND c.resolution_observation_id<>s.observation_id))) AS conflicted
 FROM dpt.canonical_selections s
 JOIN dpt.entities e ON (e.id,e.access_scope_id,e.kind)=(s.entity_id,s.access_scope_id,s.entity_kind)
 JOIN targets t ON t.id=e.id
 JOIN dpt.source_observations o ON (o.access_scope_id,o.entity_id,o.entity_kind,o.field_path,o.id)=
   (s.access_scope_id,s.entity_id,s.entity_kind,s.field_path,s.observation_id)
 JOIN dpt.source_records r ON (r.access_scope_id,r.id)=(o.access_scope_id,o.source_record_id)
 JOIN dpt.rights_assessments g ON (g.access_scope_id,g.source_id,g.id)=(r.access_scope_id,r.source_id,r.rights_id)
 JOIN dpt.sources src ON (src.access_scope_id,src.id)=(r.access_scope_id,r.source_id)
 WHERE EXISTS(SELECT FROM profile WHERE review_status='approved')
 AND ((s.entity_kind='perfume' AND s.field_path IN ('name','brand_id','concentration_code','release_year',
   'notes.top','notes.heart','notes.base','notes.general')) OR
   (s.entity_kind IN ('brand','note') AND s.field_path='name'))
), safe AS MATERIALIZED (
 SELECT m.*,o.value,jsonb_build_object('observation_id',m.observation_id,
  'source_record_id',m.source_record_id,'rights_id',m.rights_id,'source_url',m.source_url,
  'source_revision',m.source_revision,'payload_sha256',m.payload_sha256,'claim_locator',m.claim_locator,
  'transform_version',m.transform_version,'reviewed_at',m.reviewed_at,
  'source_id',m.source_id,'publisher',m.publisher,'license_code',m.license_code,
  'license_url',m.license_url,'attribution',m.attribution,'usage_scope',m.usage_scope,
  'rights_checked_at',m.rights_checked_at,'rights_review_after',m.rights_review_after) AS provenance
 FROM meta m JOIN dpt.source_observations o ON o.id=m.observation_id
 WHERE m.allowed AND NOT m.conflicted AND m.value_status='present'
 AND octet_length(o.value::text)<=65536
 AND octet_length(concat_ws('',m.source_url,m.source_revision,m.claim_locator,m.transform_version,
     m.publisher,m.license_code,m.license_url,m.attribution,m.usage_scope))<=8192
), fields AS (
 SELECT m.field_path,CASE WHEN m.conflicted THEN 'conflicted_or_held'
  WHEN NOT m.allowed THEN 'rights_unavailable'
  WHEN s.observation_id IS NULL THEN 'unknown'
  WHEN m.field_path='name' AND s.value<>to_jsonb(p.name) THEN 'conflicted_or_held'
  WHEN m.field_path='brand_id' AND s.value<>to_jsonb(p.brand_id::text) THEN 'conflicted_or_held'
  WHEN m.field_path='concentration_code' AND s.value IS DISTINCT FROM to_jsonb(p.concentration_code) THEN 'conflicted_or_held'
  WHEN m.field_path='release_year' AND s.value IS DISTINCT FROM to_jsonb(p.release_year) THEN 'conflicted_or_held'
  ELSE 'known_usable' END AS state,s.value,s.provenance
 FROM profile p JOIN meta m ON m.entity_id=p.id AND m.entity_kind='perfume'
 LEFT JOIN safe s ON s.observation_id=m.observation_id
), memberships AS (
 SELECT a.layer,a.sort_order,n.id,n.name,s.provenance
 FROM profile p JOIN note_links a ON (a.perfume_id,a.access_scope_id)=(p.id,p.access_scope_id)
 JOIN safe l ON l.entity_id=p.id AND l.entity_kind='perfume' AND l.field_path='notes.'||a.layer
   AND l.source_record_id=a.source_record_id
 JOIN dpt.notes n ON n.id=a.note_id AND n.review_status='approved'
 JOIN safe s ON s.entity_id=n.id AND s.entity_kind='note' AND s.field_path='name' AND s.value=to_jsonb(n.name)
), brand AS (
 SELECT n.name,s.provenance FROM profile p
 JOIN fields f ON f.field_path='brand_id' AND f.state='known_usable'
 JOIN dpt.brands n ON n.id=p.brand_id AND n.review_status='approved'
 JOIN safe s ON s.entity_id=n.id AND s.entity_kind='brand' AND s.field_path='name' AND s.value=to_jsonb(n.name)
), assembled AS (
SELECT jsonb_build_object('over_bound',(SELECT count(*)>512 FROM note_links),
 'profile',(SELECT jsonb_build_object('id',id,'review_status',review_status,
 'matching_eligible',matching_eligible) FROM profile),
 'fields',(SELECT coalesce(jsonb_agg(jsonb_build_object('path',field_path,'state',state,
  'value',CASE WHEN state='known_usable' THEN value END,
  'provenance',CASE WHEN state='known_usable' THEN provenance END) ORDER BY field_path),'[]'::jsonb) FROM fields),
 'memberships',(SELECT coalesce(jsonb_agg(jsonb_build_object('layer',layer,'id',id,'name',name,
  'provenance',provenance) ORDER BY layer,sort_order NULLS LAST,id),'[]'::jsonb) FROM memberships),
 'brand',(SELECT jsonb_build_object('name',name,'provenance',provenance) FROM brand)) AS body
)
SELECT CASE WHEN octet_length(body::text)>2097152 THEN
 jsonb_build_object('over_bound',true,'profile',NULL,'fields','[]'::jsonb,'memberships','[]'::jsonb,'brand',NULL)
 ELSE body END FROM assembled;
COMMIT;"""


def _provenance(value):
    if not isinstance(value,dict) or set(value)!=set(Provenance.__dataclass_fields__):
        raise AdapterUnavailable('Adapter input contract unavailable')
    for key in ('observation_id','source_record_id','rights_id','source_id'):
        canonical_id(value[key])
    for key in ('reviewed_at','rights_checked_at','rights_review_after'):
        if value[key] is not None and datetime.datetime.fromisoformat(value[key]).utcoffset() is None:
            raise ValueError('Unqualified time')
    if len(value['payload_sha256'])!=64 or any(c not in '0123456789abcdef' for c in value['payload_sha256']):
        raise ValueError('Invalid hash')
    if any(not isinstance(value[k],str) or not value[k] for k in
           ('source_url','claim_locator','transform_version','publisher','usage_scope')):
        raise ValueError('Missing provenance')
    return Provenance(**value)


def read_profile(execute: Callable[[str],dict], profile_id: str) -> ProfileInput:
    """Trusted per-login transport only; no caller-provided identity/GUC/SQL/caching."""
    script=query(profile_id)
    try:
        raw=execute(script)
    except Exception:
        raise AdapterUnavailable('Adapter input unavailable') from None
    try:
        return _decode(raw,profile_id)
    except (InputUnavailable,AdapterUnavailable):
        raise
    except (ValueError,TypeError,KeyError,AttributeError,OverflowError):
        raise AdapterUnavailable('Adapter input contract unavailable') from None


def _decode(raw,profile_id):
    if not isinstance(raw,dict) or set(raw)!= {'profile','fields','memberships','brand','over_bound'}:
        raise AdapterUnavailable('Adapter input contract unavailable')
    if len(json.dumps(raw,ensure_ascii=False).encode('utf-8'))>2097152:
        raise AdapterUnavailable('Adapter input bound exceeded')
    if raw['over_bound'] is not False:
        raise AdapterUnavailable('Adapter input bound exceeded')
    p=raw['profile']
    if p is None:
        raise InputUnavailable('Input unavailable')
    if (set(p)!= {'id','review_status','matching_eligible'} or canonical_id(p['id'])!=canonical_id(profile_id)
        or type(p['matching_eligible']) is not bool or p['review_status'] not in {'draft','reviewed','approved','archived'}
        or type(raw['fields']) is not list or len(raw['fields'])>8
        or type(raw['memberships']) is not list or len(raw['memberships'])>513):
        raise AdapterUnavailable('Adapter input contract unavailable')
    held=p['review_status']!='approved'
    result={}
    for row in raw['fields']:
        path=row['path']
        if path not in FIELDS or path in result:
            raise AdapterUnavailable('Adapter input contract unavailable')
        state=State(row['state'])
        if state is State.USABLE:
            value=row['value']
            if path in ('name','concentration_code') and (type(value) is not str or not value.strip()):
                raise ValueError('Invalid scalar')
            if path=='brand_id':canonical_id(value)
            if path=='release_year' and (type(value) is not int or not 1000<=value<=9999):
                raise ValueError('Invalid integer')
        result[path]=Field(state,row['value'] if state is State.USABLE else None,
            _provenance(row['provenance']) if state is State.USABLE else None)
    fields=tuple((path,Field(State.HELD,reason='review_hold') if held else
        result.get(path,Field(State.UNKNOWN,reason='selected_input_unavailable'))) for path in FIELDS)
    mapped=dict(fields)
    layers=[]
    for layer in LAYERS:
        selected=mapped['notes.'+layer]
        if selected.state is not State.USABLE:
            layers.append((layer,selected));continue
        labels=selected.value
        members=[n for n in raw['memberships'] if n['layer']==layer]
        if (not isinstance(labels,list) or any(not isinstance(v,str) for v in labels)
            or len({normalized(v) for v in labels})!=len(labels)
            or [normalized(v) for v in labels]!=[normalized(n['name']) for n in members]):
            layers.append((layer,Field(State.UNKNOWN,reason='vocabulary_or_provenance_unavailable')));continue
        notes=tuple(Note(canonical_id(n['id']),n['name'],_provenance(n['provenance'])) for n in members)
        layers.append((layer,Field(State.INCOMPLETE,notes,selected.provenance,'reported_membership_only_closure_unknown')))
    # List labels are never returned directly; only the rights-qualified canonical membership view.
    fields=tuple((k,v) for k,v in fields if not k.startswith('notes.'))
    brand=raw['brand']
    brand_field=Field(State.UNKNOWN,reason='selected_brand_unavailable')
    if not held and mapped['brand_id'].state is State.USABLE and brand:
        brand_field=Field(State.USABLE,brand['name'],_provenance(brand['provenance']))
    elif mapped['brand_id'].state is State.USABLE:
        fields=tuple((k,Field(State.UNKNOWN,reason='selected_brand_unavailable') if k=='brand_id' else v) for k,v in fields)
    conflicted=any(v.state is State.HELD for _,v in (*fields,*layers))
    return ProfileInput(canonical_id(p['id']),State.HELD if held or conflicted else State.ELIGIBILITY if not p['matching_eligible']
        else State.INCOMPLETE,p['review_status'],p['matching_eligible'],fields,brand_field,tuple(layers))
