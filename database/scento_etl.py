"""Local-only pinned Scento intake; reviewed exact-source mappings gate canonical promotion.

No downloader, arbitrary host, SQL migration, fuzzy identity merge or image acquisition. Raw files
remain external. Existing PostgreSQL constraints/RLS/deferred validation are always enabled.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime
import hashlib
import io
import json
from pathlib import Path
import unicodedata
import uuid
import time

import local

REV = '086769ecf1add770ea6646bd4d88d39f0e7cddeb'
BASE = 'https://raw.githubusercontent.com/Scento-com/perfume-dataset/'+REV+'/'
VERSION = 'scento-csv-local-v1'
ATTRIBUTION = 'Scento — https://www.scento.com/perfume-database'
EXPECTED = {
    'perfumes.csv': ('4dc99cc840566f98c57be5aa02437960371ca7de',1479),
    'houses.csv': ('797d58078969e63fad109bc84f400d5614255d3c',160),
    'materials.csv': ('60fa5f70a22bbe46de57f18ee59b2e61d134ab6a',420),
    'LICENSE': ('83674148f20fcfc8933a45783e5355188574c5b8',None),
    'README.md': ('e8a12b6437ab023a01e33177d9ff28eb61fedadf',None),
    'datapackage.json': ('fc901b154579e7cbe1d9a44e5948ed209db181c3',None),
}
PILOT = ('dior-jadore','dior-hypnotic-poison','dior-poison','parfums-de-marly-layton',
         'parfums-de-marly-delina','lattafa-khamrah','lattafa-yara','lattafa-asad',
         'amouage-reflection-man','lattafa-fakhar-black','balmain-bleu-infini','balmain-bleu-infini-toilette')
LOCAL_DBS = {'dpt_scento_test','dpt_scento_pilot'}
# Independently reviewed exact-source policy, not arbitrary client-supplied approval flags.
MAPPING_REVIEW_SHA256='33e7d06ef10a8f489f87f2a174122d17d7d36cf36c1c9ffb1aafb5daa0f30e80'
REVIEWED_PROPOSAL_SHA256={'pilot':'f3b6de194285b560073c2f6313c20ae204da07c1760434947140d493d2830dad',
                         'full':'5bc303ec860ef202287bf6aaef2b25f2777b4a1c1492ae4c8ab04fb062a9abf2'}
REVIEWED_POLICY_CONTENT_SHA256={'pilot':'d02d4a33b4500cdc3e153f6f998c7b1a7e2c8d93d390092106b5c2e5c754a819',
                               'full':'7a20fcb5dac501c55068fc910eb93442ed5139a9ce2fb3e4fb3db2772ea316de'}


def canonical(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'))


def digest(value):
    return hashlib.sha256(canonical(value).encode('utf-8')).hexdigest()


def entity_id(kind,key):
    return str(uuid.uuid5(uuid.NAMESPACE_URL,'https://github.com/Scento-com/perfume-dataset/'+REV+'#dpt:'+kind+':'+key))


SCOPE_ID=entity_id('scope','local-private');OPERATOR_ID=entity_id('operator','postgres')
SOURCE_ID=entity_id('source','licensed-snapshot');RIGHTS_ID=entity_id('rights','OD-01-06-local-v1')


def tokens(text):
    return [x.strip() for x in text.split(';') if x.strip()]


def normalize(text):
    # Matches merged PostgreSQL lower(normalize(label,NFKC)), not casefold/space/fuzzy aliases.
    return unicodedata.normalize('NFKC',text).lower()


def optional_year(text):
    if not text:return None
    if not text.isascii() or not text.isdecimal() or not 1000<=int(text)<=9999:
        raise ValueError('Invalid source year')
    return int(text)


def load_snapshot(path):
    root=Path(path).resolve();data={'artifacts':{},'rows':{}}
    for name,(blob,count) in EXPECTED.items():
        file=root/name
        if file.is_symlink():raise ValueError('Source symlink refused')
        raw=file.read_bytes()
        if len(raw)>5_000_000 or hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:
            raise ValueError('Pinned source hash mismatch: '+name)
        data['artifacts'][name]={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'git_blob_sha':blob}
        if count is not None:
            rows=list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'),newline='')))
            if len(rows)!=count or len({x['id'] for x in rows})!=count:raise ValueError('Source row identity/count mismatch')
            data['rows'][name]=rows
    data['houses']={x['id']:x for x in data['rows']['houses.csv']}
    data['materials']={x['id']:x for x in data['rows']['materials.csv']}
    data['note_lookup']=collections.defaultdict(set)
    for key,row in data['materials'].items():
        data['note_lookup'][normalize(row['name'])].add(key)
    # Return plain JSON-compatible state for reproducible plans.
    data['note_lookup']={key:sorted(vals) for key,vals in data['note_lookup'].items()}
    return data


def note_lists(row):
    layers={k:tokens(row[k+'_notes']) for k in ['top','heart','base']}
    return layers if any(layers.values()) else {'general':tokens(row['notes'])}


def classify(row,snapshot):
    reasons=[];state='promotable'
    try:
        optional_year(row['year'])
        if not row['name'].strip() or row['house_id'] not in snapshot['houses']:raise ValueError('shape')
    except (ValueError,KeyError):return {'state':'quarantined','reasons':['shape']}
    layers=note_lists(row)
    if not any(layers.values()):reasons.append('notes')
    for vals in layers.values():
        if len({normalize(x) for x in vals})!=len(vals):reasons.append('notes')
        if any(len(snapshot['note_lookup'].get(normalize(x),[]))!=1 for x in vals):reasons.append('notes')
    if row['id']=='lattafa-khamrah':reasons.append('external_conflict_pending')
    if reasons:state='review'
    return {'state':state,'reasons':sorted(set(reasons))}


def build_plan(snapshot,cohort):
    if cohort not in {'pilot','full'}:raise ValueError('Unknown cohort')
    rows=snapshot['rows']['perfumes.csv']
    perfumes=[p for p in rows if cohort=='full' or p['id'] in PILOT]
    if cohort=='pilot' and {p['id'] for p in perfumes}!=set(PILOT):raise ValueError('Approved P1 pilot missing')
    houses=[snapshot['houses'][k] for k in sorted({p['house_id'] for p in perfumes})]
    material_ids=set();count=0;states={'promotable':{},'review':{},'quarantined':{}}
    for row in perfumes:
        result=classify(row,snapshot);states[result['state']][row['id']]=result['reasons']
        for vals in note_lists(row).values():
            count+=len(vals)
            for label in vals:material_ids.update(snapshot['note_lookup'].get(normalize(label),[]))
    materials=[snapshot['materials'][k] for k in sorted(material_ids)]
    plan={'cohort':cohort,'perfumes':perfumes,'houses':houses,'materials':materials,'note_occurrences':count,**states}
    if cohort=='pilot' and (len(perfumes),len(houses),len(materials),count)!=(12,5,58,93):
        raise ValueError('Approved pilot12/5/58/93 accounting changed')
    return plan


def mapping_proposal(plan,snapshot):
    def entries(kind,rows):
        return [{'source_key':r['id'],'source_name':r['name'],'canonical_id':entity_id(kind,r['id'])} for r in rows]
    return {'policy_version':'scento-exact-identity-v1','status':'proposed','reviewed_by':'','review_evidence':'',
            'cohort':plan['cohort'],'revision':REV,'source_artifacts':snapshot['artifacts'],
            'brands':entries('brand',plan['houses']),'notes':entries('note',plan['materials']),
            'perfumes':entries('perfume',plan['perfumes']),
            'held_perfumes':{**plan['review'],**plan['quarantined']},
            'field_policy':'Exact names/brand linkage/source concentration/year and unambiguous note lists only; no country/family/accord/imagery inference; matching disabled'}


def validate_mapping(mapping,plan,snapshot):
    if mapping.get('status')!='reviewed' or not mapping.get('reviewed_by') or not mapping.get('review_evidence'):
        raise ValueError('Promotion requires independently reviewed mapping manifest')
    expected=mapping_proposal(plan,snapshot)
    proposal_sha=REVIEWED_PROPOSAL_SHA256[plan['cohort']]
    review=mapping.get('review_evidence')
    if (digest(expected)!=REVIEWED_POLICY_CONTENT_SHA256[plan['cohort']] or not isinstance(review,dict)
            or review.get('report_sha256')!=MAPPING_REVIEW_SHA256 or review.get('proposal_sha256')!=proposal_sha):
        raise ValueError('Promotion requires the hash-bound independently reviewed mapping policy')
    for key,value in expected.items():
        if key not in {'status','reviewed_by','review_evidence'} and mapping.get(key)!=value:
            raise ValueError('Reviewed mapping content/source/policy mismatch: '+key)


def q(value):
    if value is None:return 'NULL'
    if isinstance(value,bool):return 'true' if value else 'false'
    if isinstance(value,int):return str(value)
    if isinstance(value,(dict,list)):return "'"+canonical(value).replace("'","''")+"'::jsonb"
    return "'"+str(value).replace("'","''")+"'"


def insert(table,values):
    literals=[q(canonical(v))+'::jsonb' if table=='source_observations' and k=='value' else q(v)
              for k,v in values.items()]
    return 'INSERT INTO dpt.'+table+'('+','.join(values)+') VALUES('+','.join(literals)+') ON CONFLICT DO NOTHING;\n'


def capture_rows(snapshot,plan):
    results=[]
    for kind,name,rows in [('house','houses.csv',plan['houses']),('material','materials.csv',plan['materials']),('perfume','perfumes.csv',plan['perfumes'])]:
        ordinals={r['id']:n+1 for n,r in enumerate(snapshot['rows'][name])}
        for row in rows:
            payload={'source_file':name,'source_file_sha256':snapshot['artifacts'][name]['sha256'],
                     'csv_record_ordinal':ordinals[row['id']],'fields':row}
            sha=digest(payload);key=kind+':'+row['id']
            results.append({'kind':kind,'key':key,'id':entity_id('capture',key+':'+sha),'sha':sha,
                            'url':BASE+name,'locator':'csv-record:'+str(ordinals[row['id']]),'payload':payload})
    return results


def batch_identity(snapshot,plan,mapping):
    return entity_id('batch',digest({'cohort':plan['cohort'],'adapter':VERSION,'artifacts':snapshot['artifacts'],
                                    'reviewed_mapping':digest(mapping) if mapping else None}))


def import_sql(snapshot,plan,mapping=None,transaction=True):
    if mapping is not None:validate_mapping(mapping,plan,snapshot)
    batch=batch_identity(snapshot,plan,mapping);rows=capture_rows(snapshot,plan)
    text='BEGIN;SET LOCAL statement_timeout=\'45s\';SET LOCAL lock_timeout=\'5s\';\n' if transaction else ''
    text+='SELECT pg_advisory_xact_lock(1900147);\n'
    text+='CREATE TEMP TABLE dpt_scento_before ON COMMIT DROP AS SELECT (SELECT count(*) FROM dpt.source_records WHERE access_scope_id='+q(SCOPE_ID)+') AS source_records,(SELECT count(*) FROM dpt.staging_records WHERE access_scope_id='+q(SCOPE_ID)+') AS staging_records;\n'
    text+=insert('users',{'id':OPERATOR_ID,'auth_subject':'postgres','display_name':'Local licensed-data operator (Docker-admin test adapter)'})
    text+=insert('access_scopes',{'id':SCOPE_ID,'kind':'user_private','owner_user_id':OPERATOR_ID})
    text+=insert('sources',{'id':SOURCE_ID,'access_scope_id':SCOPE_ID,'name':'Pinned Scento local licensed snapshot',
                          'kind':'dataset','entry_url':BASE,'publisher':'Scento'})
    rights={'id':RIGHTS_ID,'access_scope_id':SCOPE_ID,'source_id':SOURCE_ID,'scope':'Owner OD-01/06 bounded local licensed pilot only',
            'evidence_url':BASE+'LICENSE','license_code':'CC-BY-4.0','license_url':'https://creativecommons.org/licenses/by/4.0/',
            'research_use':'allowed','automation_use':'allowed','cache_use':'allowed','storage_use':'allowed','display_use':'allowed',
            'redistribution_use':'restricted','ai_use':'unknown','attribution':ATTRIBUTION,
            'reviewer':'Codex: pinned license verified under Owner OD-01/06',
            'restrictions':{'revision':REV,'artifacts':snapshot['artifacts'],'no_image_grant':True,'no_public_raw_export':True}}
    text+=insert('rights_assessments',rights).replace(') VALUES(', ',checked_at) VALUES(',1).replace(') ON CONFLICT',',statement_timestamp()) ON CONFLICT',1)
    text+='DO $$BEGIN IF NOT EXISTS(SELECT FROM dpt.rights_assessments WHERE id='+q(RIGHTS_ID)+' AND access_scope_id='+q(SCOPE_ID)+' AND source_id='+q(SOURCE_ID)+" AND license_code='CC-BY-4.0' AND evidence_url="+q(BASE+'LICENSE')+" AND restrictions->'artifacts'="+q(snapshot['artifacts'])+") THEN RAISE EXCEPTION 'Existing assessment differs from pinned source binding' USING ERRCODE='23514';END IF;END$$;\n"
    text+="DO $$BEGIN IF NOT dpt_guard.right_allowed("+q(RIGHTS_ID)+",'storage') OR NOT dpt_guard.right_allowed("+q(RIGHTS_ID)+",'automation') THEN RAISE EXCEPTION 'Active local source rights required, including replay' USING ERRCODE='42501';END IF;END$$;\n"
    text+=insert('ingestion_batches',{'id':batch,'access_scope_id':SCOPE_ID,'source_id':SOURCE_ID,'rights_id':RIGHTS_ID,
                  'source_revision':REV,'batch_sha256':digest({'artifacts':snapshot['artifacts'],'cohort':plan['cohort']}),
                  'adapter_version':VERSION+(':'+digest(mapping) if mapping else ':review-only'),'state':'review'})\
          .replace(') VALUES(', ',started_at) VALUES(',1).replace(') ON CONFLICT',',statement_timestamp()) ON CONFLICT',1)
    # One bounded temp input set; preexisting captures/staging must match, not silently win DO NOTHING.
    temp=[]
    for row in rows:
        key=row['payload']['fields']['id']
        reasons=plan['review'].get(key,plan['quarantined'].get(key,[])) if row['kind']=='perfume' else []
        sid=entity_id('staging',batch+':'+row['key']+':'+row['sha'])
        promoted=mapping is not None and (row['kind']!='perfume' or key in plan['promotable'])
        expected_errors=None if promoted else (reasons if mapping else ['canonical_mapping_review_required',*reasons])
        temp.append(dict(row,staging_id=sid,errors=['canonical_mapping_review_required',*reasons],
                         expected_state='promoted' if promoted else 'review',expected_errors=expected_errors))
    text+='CREATE TEMP TABLE dpt_scento_input ON COMMIT DROP AS SELECT * FROM jsonb_to_recordset('+q(temp)+') AS r(kind text,key text,id uuid,sha text,url text,locator text,payload jsonb,staging_id uuid,errors jsonb,expected_state text,expected_errors jsonb);\n'
    text+='''DO $$BEGIN IF EXISTS(SELECT FROM pg_temp.dpt_scento_input i JOIN dpt.source_records s ON s.id=i.id
      WHERE s.access_scope_id<>'''+q(SCOPE_ID)+''' OR s.source_id<>'''+q(SOURCE_ID)+''' OR s.external_key<>i.key OR s.payload_sha256<>i.sha
      OR s.source_url<>i.url OR s.locator IS DISTINCT FROM i.locator OR s.source_revision<>'''+q(REV)+''' OR s.rights_id<>'''+q(RIGHTS_ID)+''')
      OR EXISTS(SELECT FROM pg_temp.dpt_scento_input i JOIN dpt.staging_records s ON s.id=i.staging_id
      WHERE s.raw_payload IS DISTINCT FROM i.payload OR s.payload_sha256<>i.sha OR s.source_record_id IS DISTINCT FROM i.id
      OR s.batch_id<>'''+q(batch)+''' OR s.external_key<>i.key OR s.access_scope_id<>'''+q(SCOPE_ID)+'''
      OR s.state IS DISTINCT FROM i.expected_state OR s.error_codes IS DISTINCT FROM i.expected_errors)
      THEN RAISE EXCEPTION 'Existing capture/staging does not match exact replay' USING ERRCODE='23514';END IF;END$$;
    INSERT INTO dpt.source_records(id,access_scope_id,source_id,external_key,payload_sha256,source_url,locator,source_revision,retrieved_at,rights_id)
      SELECT id,'''+q(SCOPE_ID)+','+q(SOURCE_ID)+''',key,sha,url,locator,'''+q(REV)+''',statement_timestamp(),'''+q(RIGHTS_ID)+''' FROM pg_temp.dpt_scento_input ON CONFLICT DO NOTHING;
    INSERT INTO dpt.staging_records(id,access_scope_id,batch_id,external_key,payload_sha256,raw_payload,source_record_id,state,error_codes)
      SELECT staging_id,'''+q(SCOPE_ID)+','+q(batch)+''',key,sha,payload,id,'review',errors FROM pg_temp.dpt_scento_input ON CONFLICT DO NOTHING;
    '''
    if mapping is not None:text+=promotion_sql(snapshot,plan,rows,batch,mapping)
    text+="DO $$BEGIN IF EXISTS(SELECT FROM pg_temp.dpt_scento_input i LEFT JOIN dpt.staging_records s ON s.id=i.staging_id WHERE s.id IS NULL OR s.state IS DISTINCT FROM i.expected_state OR s.error_codes IS DISTINCT FROM i.expected_errors) THEN RAISE EXCEPTION 'Staging final state differs from complete accounting' USING ERRCODE='23514';END IF;END$$;\n"
    text+='DO $$BEGIN IF EXISTS(SELECT FROM dpt.staging_records s WHERE s.batch_id='+q(batch)+" AND NOT EXISTS(SELECT FROM pg_temp.dpt_scento_input i WHERE i.staging_id=s.id)) THEN RAISE EXCEPTION 'Unexpected records in source batch' USING ERRCODE='23514';END IF;END$$;\n"
    text+='UPDATE dpt.ingestion_batches SET finished_at=clock_timestamp() WHERE id='+q(batch)+' AND finished_at IS NULL;\n'
    ids=','.join(q(entity_id('perfume',r['id'])) for r in plan['perfumes'])
    accounting="(SELECT jsonb_build_object('source_rows',count(*),'perfumes',count(*) FILTER(WHERE external_key LIKE 'perfume:%'),'promoted_perfumes',count(*) FILTER(WHERE external_key LIKE 'perfume:%' AND state='promoted'),'review_perfumes',count(*) FILTER(WHERE external_key LIKE 'perfume:%' AND state='review'),'quarantined_perfumes',count(*) FILTER(WHERE external_key LIKE 'perfume:%' AND state='quarantined')) FROM dpt.staging_records WHERE batch_id="+q(batch)+')'
    text+="SELECT jsonb_build_object('dpt_etl_metrics',true,'inventory',"+inventory_expression()+",'new_source_records',(SELECT count(*) FROM dpt.source_records WHERE access_scope_id="+q(SCOPE_ID)+")-(SELECT source_records FROM pg_temp.dpt_scento_before),'new_staging_records',(SELECT count(*) FROM dpt.staging_records WHERE access_scope_id="+q(SCOPE_ID)+")-(SELECT staging_records FROM pg_temp.dpt_scento_before),'approved',(SELECT count(*) FROM dpt.perfumes WHERE access_scope_id="+q(SCOPE_ID)+" AND review_status='approved' AND id IN ("+ids+")),'matching',(SELECT count(*) FROM dpt.perfumes WHERE access_scope_id="+q(SCOPE_ID)+" AND matching_eligible),'batch_accounting',"+accounting+');\n'
    text+='COMMIT;\n' if transaction else ''
    return text


def promotion_sql(snapshot,plan,rows,batch,mapping):
    records={r['key']:r for r in rows};text='';targets=[];selections=[];joins=[]
    def item(kind,key,table,values,capture):
        eid=entity_id(kind,key)
        targets.append({'id':eid,'kind':kind,'table_name':table,'expected':{'id':eid,'access_scope_id':SCOPE_ID,**values}})
        return (insert('entities',{'id':eid,'access_scope_id':SCOPE_ID,'kind':kind})+
                insert(table,{'id':eid,'access_scope_id':SCOPE_ID,**values})+
                insert('entity_source_links',{'id':entity_id('link',kind+':'+key),'access_scope_id':SCOPE_ID,
                       'entity_id':eid,'source_record_id':capture['id'],'review_status':'reviewed'}))
    def claim(kind,key,path,value,capture,selected=True,locator=None):
        oid=entity_id('observation',capture['id']+':'+kind+':'+key+':'+path+':'+VERSION)
        sql=insert('source_observations',{'id':oid,'access_scope_id':SCOPE_ID,'entity_id':entity_id(kind,key),
                   'entity_kind':kind,'field_path':path,'source_record_id':capture['id'],
                   'claim_locator':locator or '/'+path,'claim_key':'csv-field:'+path,'value':value,
                   'value_status':'present','transform_version':VERSION})
        if selected:
            selections.append({'entity_id':entity_id(kind,key),'entity_kind':kind,'field_path':path,'observation_id':oid})
            sql+=insert('canonical_selections',{'access_scope_id':SCOPE_ID,'entity_id':entity_id(kind,key),
                   'entity_kind':kind,'field_path':path,'observation_id':oid,'reviewed_by':'postgres',
                   'rationale':'Reviewed exact-source mapping '+digest(mapping)+'; independent review '+mapping['review_evidence']['report_sha256']})\
                   .replace(') VALUES(', ',reviewed_at) VALUES(',1).replace(') ON CONFLICT',',statement_timestamp()) ON CONFLICT',1)
        return sql
    for row in plan['houses']:
        key=row['id'];capture=records['house:'+key]
        text+=item('brand',key,'brands',{'name':row['name'],'slug':'scento-'+key,'review_status':'approved',
                                      'country_code':None,'website_url':None},capture)
        text+=claim('brand',key,'name',row['name'],capture)
    for row in plan['materials']:
        key=row['id'];capture=records['material:'+key]
        text+=item('note',key,'notes',{'name':row['name'],'slug':'scento-'+key,'review_status':'approved',
                                    'name_th':None,'material_origin':None,'description':None},capture)
        text+=claim('note',key,'name',row['name'],capture)
    for row in plan['perfumes']:
        key=row['id'];capture=records['perfume:'+key];eligible=key in plan['promotable']
        values={'brand_id':entity_id('brand',row['house_id']),'name':row['name'],'slug':'scento-'+key,
                'review_status':'approved' if eligible else 'draft','matching_eligible':False,
                'edition_label':None,'gender_label':None,'description':None,
                'concentration_code':row['concentration'] or None,'release_year':optional_year(row['year'])}
        text+=item('perfume',key,'perfumes',values,capture)
        for field in ['name','brand_id','concentration_code','release_year']:
            if values[field] is not None:
                locator='/'+{'brand_id':'house_id','concentration_code':'concentration','release_year':'year'}.get(field,field)
                text+=claim('perfume',key,field,values[field],capture,selected=eligible,locator=locator)
        for layer,labels in note_lists(row).items():
            if not labels:continue
            text+=claim('perfume',key,'notes.'+layer,labels,capture,selected=eligible,locator='/'+('notes' if layer=='general' else layer+'_notes'))
            if eligible:
                for order,label in enumerate(labels):
                    mid=snapshot['note_lookup'][normalize(label)][0]
                    join={'id':entity_id('note-join',key+':'+layer+':'+str(order)),
                        'access_scope_id':SCOPE_ID,'perfume_id':entity_id('perfume',key),'note_id':entity_id('note',mid),
                        'layer':layer,'sort_order':order,'source_record_id':capture['id']}
                    joins.append(join);text+=insert('perfume_notes',join)
        if any(row[k] for k in ['top_notes','heart_notes','base_notes']):
            text+=claim('perfume',key,'notes.general',tokens(row['notes']),capture,selected=False,locator='/notes')
    preflight='CREATE TEMP TABLE dpt_scento_targets ON COMMIT DROP AS SELECT * FROM jsonb_to_recordset('+q(targets)+') AS t(id uuid,kind text,table_name text,expected jsonb);\n'
    preflight+='CREATE TEMP TABLE dpt_scento_selections ON COMMIT DROP AS SELECT * FROM jsonb_to_recordset('+q(selections)+') AS t(entity_id uuid,entity_kind text,field_path text,observation_id uuid);\n'
    preflight+='CREATE TEMP TABLE dpt_scento_joins ON COMMIT DROP AS SELECT * FROM jsonb_to_recordset('+q(joins)+') AS t(id uuid,access_scope_id uuid,perfume_id uuid,note_id uuid,layer text,sort_order integer,source_record_id uuid);\n'
    preflight+='''DO $$DECLARE target_row record; actual jsonb; BEGIN
      FOR target_row IN SELECT * FROM pg_temp.dpt_scento_targets LOOP
        IF EXISTS(SELECT FROM dpt.entities e WHERE e.id=target_row.id AND (e.kind<>target_row.kind OR e.access_scope_id<>'''+q(SCOPE_ID)+'''))
          THEN RAISE EXCEPTION 'Canonical entity replay differs' USING ERRCODE='23514';END IF;
        EXECUTE format('SELECT to_jsonb(r) FROM dpt.%I r WHERE id=$1',target_row.table_name) INTO actual USING target_row.id;
        IF actual IS NOT NULL AND NOT actual @> target_row.expected THEN
          RAISE EXCEPTION 'Canonical row replay differs; explicit reconciliation required' USING ERRCODE='23514';END IF;
      END LOOP;
      IF EXISTS(SELECT FROM dpt.canonical_selections s JOIN pg_temp.dpt_scento_targets t ON t.id=s.entity_id
        LEFT JOIN pg_temp.dpt_scento_selections x ON (x.entity_id,x.entity_kind,x.field_path)=(s.entity_id,s.entity_kind,s.field_path)
        WHERE s.access_scope_id<>'''+q(SCOPE_ID)+''' OR x.observation_id IS DISTINCT FROM s.observation_id)
      OR EXISTS(SELECT FROM dpt.perfume_notes p JOIN pg_temp.dpt_scento_targets t ON t.id=p.perfume_id
        LEFT JOIN pg_temp.dpt_scento_joins j ON j.id=p.id WHERE j.id IS NULL OR NOT to_jsonb(p) @> to_jsonb(j))
      THEN RAISE EXCEPTION 'Canonical selection/join replay differs' USING ERRCODE='23514';END IF;
    END$$;
    '''
    validations=[]
    for r in rows:
        key=r['payload']['fields']['id'];good=r['kind']!='perfume' or key in plan['promotable']
        sid=entity_id('staging',batch+':'+r['key']+':'+r['sha'])
        for rule in ['shape','identity','rights','notes']:
            result='pass' if good or rule in {'shape','rights'} else 'review'
            validations.append({'id':entity_id('validation',sid+':'+rule),'access_scope_id':SCOPE_ID,
                 'staging_record_id':sid,'rule_code':rule,'severity':'info' if result=='pass' else 'warning',
                 'result':result,'detail':{'reviewed_mapping':digest(mapping),'source_kind':r['kind'],
                                          'hold_reasons':plan['review'].get(key,plan['quarantined'].get(key,[])) if not good else []}})
        if good:text+='UPDATE dpt.staging_records SET state=\'promoted\',error_codes=NULL WHERE id='+q(sid)+" AND state='review';\n"
        else:text+='UPDATE dpt.staging_records SET error_codes='+q(plan['review'].get(key,plan['quarantined'].get(key,['review_required'])))+' WHERE id='+q(sid)+" AND state='review';\n"
    # Validation evidence is checked in bulk before replay, never retained from a contrary prior result.
    preflight+='CREATE TEMP TABLE dpt_scento_validations ON COMMIT DROP AS SELECT * FROM jsonb_to_recordset('+q(validations)+') AS v(id uuid,access_scope_id uuid,staging_record_id uuid,rule_code text,severity text,result text,detail jsonb);\n'
    preflight+="DO $$BEGIN IF EXISTS(SELECT FROM dpt.validation_results v JOIN pg_temp.dpt_scento_validations x ON x.id=v.id WHERE NOT to_jsonb(v) @> to_jsonb(x)) THEN RAISE EXCEPTION 'Validation evidence replay differs' USING ERRCODE='23514';END IF;END$$;\n"
    # Validation records and promoted states commit together under existing deferred constraints.
    insert_validations='INSERT INTO dpt.validation_results(id,access_scope_id,staging_record_id,rule_code,severity,result,detail) SELECT id,access_scope_id,staging_record_id,rule_code,severity,result,detail FROM pg_temp.dpt_scento_validations ON CONFLICT DO NOTHING;\n'
    return preflight+text+insert_validations


def prepare_database(db):
    if db not in LOCAL_DBS:raise ValueError('ETL target outside local task database allowlist')
    exists=local.sql('SELECT count(*) FROM pg_database WHERE datname='+q(db)+';','postgres').stdout.strip()
    if exists=='0':local.sql('CREATE DATABASE "'+db+'";','postgres')
    local.migrate(db)


def inventory_expression():
    names=['source_records','staging_records','ingestion_batches','validation_results','entity_source_links',
           'brands','notes','perfumes','perfume_notes','canonical_selections','source_observations']
    return 'jsonb_build_object('+','.join(q(n)+',(SELECT count(*) FROM dpt.'+n+' WHERE access_scope_id='+q(SCOPE_ID)+')' for n in names)+')'


def inventory(db):
    if db not in LOCAL_DBS:raise ValueError('ETL target outside local task database allowlist')
    return json.loads(local.sql('SELECT '+inventory_expression()+';',db).stdout)


def run_import(snapshot,cohort,db,mapping=None):
    started=time.monotonic();source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if db not in LOCAL_DBS:raise ValueError('ETL target outside local task database allowlist')
    plan=build_plan(snapshot,cohort)
    if mapping is not None:validate_mapping(mapping,plan,snapshot)
    result=local.sql(import_sql(snapshot,plan,mapping),db)
    observed=next(json.loads(line) for line in result.stdout.splitlines() if line.strip().startswith('{') and '"dpt_etl_metrics"' in line)
    after=observed['inventory']
    batch=batch_identity(snapshot,plan,mapping)
    accounting=observed['batch_accounting']
    return {'cohort':cohort,'database':db,'revision':REV,'adapter_version':VERSION,'batch_id':batch_identity(snapshot,plan,mapping),
            'staged_perfumes':accounting['perfumes'],'batch_accounting':accounting,'source_records':after['source_records'],
            'new_source_records':observed['new_source_records'],'new_staging_records':observed['new_staging_records'],
            'catalogue_perfumes':after['perfumes'],'approved_perfumes':observed['approved'],
            'raw_note_occurrences':plan['note_occurrences'],'review_perfumes':plan['review'],
            'quarantined_perfumes':plan['quarantined'],'canonical_mapping_used':digest(mapping) if mapping else None,
            'inventory':after,'matching_eligible_count':observed['matching'],'matching_eligible_enabled':observed['matching']>0,
            'image_bytes_acquired':0,'verified_dupe_pairs':0,'source_code_sha256':source_hash,
            'executed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'local_harness_wall_seconds':round(time.monotonic()-started,6),
            'measurement':'Includes guarded SQL transaction/commit and in-lock SQL row accounting; excludes source download and database prepare'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-dir',required=True)
    p.add_argument('--cohort',choices=['pilot','full'],default='pilot');p.add_argument('--database',choices=sorted(LOCAL_DBS),default='dpt_scento_pilot')
    p.add_argument('--mapping',type=Path);p.add_argument('--report',type=Path,required=True);p.add_argument('--plan-only',action='store_true')
    args=p.parse_args();snapshot=load_snapshot(args.source_dir);plan=build_plan(snapshot,args.cohort)
    if args.report.exists():raise ValueError('Refusing to overwrite evidence/review output; choose a new report path')
    if args.report.resolve().is_relative_to(local.ROOT.resolve()) and not args.report.resolve().is_relative_to((local.ROOT/'.local').resolve()):
        raise ValueError('Raw-derived/review output must remain outside public Git or under ignored .local')
    if args.plan_only:result=mapping_proposal(plan,snapshot)
    else:
        mapping=json.loads(args.mapping.read_text(encoding='utf-8')) if args.mapping else None
        if mapping is not None:validate_mapping(mapping,plan,snapshot)
        prepare_database(args.database);result=run_import(snapshot,args.cohort,args.database,mapping)
    args.report.parent.mkdir(parents=True,exist_ok=True)
    # Exclusive creation also protects a reviewer file created while the DB transaction was running.
    with args.report.open('x',encoding='utf-8',newline='\n') as stream:
        stream.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'report':str(args.report),'cohort':args.cohort,'plan_only':args.plan_only,'database_mutation':not args.plan_only}))


if __name__=='__main__':main()
