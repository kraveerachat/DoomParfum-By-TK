---
id: IMP-P1-01-EVIDENCE
project: DoomParfum By TK
type: implementation_evidence
status: local-verified-review-pending
owner: project
updated: 2026-11-10
tags: [doomparfum, postgres, tests, security]
source_of_truth: "../../../README.md"
---

# IMP-P1-01 — Implementation Evidence

Approved plan: [PR #1](https://github.com/kraveerachat/DoomParfum-By-TK/pull/1), owner-merged at
`bffb2fab1918dc5221a6c5da7920168bcae263ca`. Branch `impl/p1-01-local-postgres-schema`.
Source/evidence checkpoint will be recorded after commit; no self-referential tracked SHA invented.
Human review/merge required. PRODUCTION_MUTATION=NO. [[IMP-P1-01_Local_PostgreSQL_Schema]].

## Exact local implementation

Seven ordered migrations in `database/migrations/`, bounded local harness and integration tests.
PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2), UTF-8, collation en_US.utf8; Docker Desktop 4.43.2 / Engine 28.3.2,
Python 3.11.9. Image `postgres@sha256:f1c3376c26f2609ab9f29f71f824103fe2fcd8ee0346485cb6122a4f93df6f94`. No extension beyond built-in PostgreSQL/PLpgSQL required.
Task-labeled container/volume, 127.0.0.1:55431, 768 MiB / 2 CPUs; development password ignored and not logged.
No global install, host setting/account/provider change, other-container stop/reset or production access.
The internal trusted Unix-socket adapter is a local test boundary; real provider authentication is unimplemented.

Actual catalogue inventory: **47 logical tables**; **47 PK, 141 FK, 91 UNIQUE, 82 table CHECK**
constraints plus **59 deferred constraint-trigger constraints**, **5 domain CHECKs**,
**396 NOT NULL columns**, **244 indexes**, **203 RLS policies**,
**196 user triggers**. ENABLE/FORCE RLS on all 47 tables. The separate dpt_ops migration ledger
is infrastructure, not a 48th logical model table. All declared FKs are validated and have a leading index.
Detailed named definitions: `database/evidence/schema_inventory.json`. Model parity: ERD/dictionary/manifest.

`dpt_foundation` migrations applied: all 47 tables, 53 fixed field definitions, zero other domain rows.
No product/source/user imports. Test DBs are separate: dpt_schema_test and dpt_migration_probe.

## Commands and verified results

`python database/local.py start` — exit 0, existing pinned local Docker image, loopback-only readiness.
`python database/verify.py` — **69/69 passed, 0 failed, 0 errors, 0 skipped**, exit 0;
105.453 seconds, checked 2026-11-10T16:56:02.929458+00:00. Exact test IDs and source SHA-256 in
`database/evidence/test_results.json`; schema-only inventory contains no row data/secrets.
`python database/local.py migrate` — exit 0 on empty dpt_foundation; replay/checksum behavior tested.
Documentation/frontmatter/wiki/local-link/model-parity/secret-pattern/Git checks are separately recorded
in `database/evidence/documentation_checks.json` after validation, not inferred from DB tests.

Tests exercise actual non-owner logins dpt_test_alice/dpt_test_bob and guest/curator, explicit role flags,
FORCE RLS as the real non-superuser table owner, old/new scope checks, reader/editor/revocation, private
source/overlay/media access, no arbitrary untrusted mutation or helper execution, temp/GUC identity spoof.
Wrong-owner same-perfume variant, missing currency, history preservation, ratings/matching separation,
namespace-qualified taxonomy, raw staging/validation transitions, selected scalar/join deletion, immutable
claims/audits, rights/asset tuples/parents/hash/expiry and cycles have actual positive/negative controls.
Concurrent member deletions yield one success/one rejected transaction and retain >=2 members.
Failed migration DDL/ledger and failed transactions roll back; fresh recreate matches current schema.

## RED / failures / fixes observed (not fabricated retrospectively)

- Initial test against empty DB: 0 vs 47 tables, exit 1; later migration/table-count GREEN.
- Introduced PLpgSQL variable/column ambiguities and a fixture argument collision failed setup; repaired.
- Initial expanded suite exposed replay-fixture syntax/rejection precedence assumptions; repaired tests
  to assert the actual intended guard, not relax validation. A staged full run then passed.
- Adversarial RED exposed approved selection deletion, validation child back-transition and public
  private-input matching gaps; added final-state parent/child and scope/hash contracts. One following
  raw-staging probe hit a duplicate from that deliberately defective committed test fixture; fresh
  test DB recreation removed contamination. No real dataset/database was affected.
- Two focused REDs proved resolved selection disagreement and another user's private variant of a public
  perfume could slip through; fixed both, focused GREEN. Approved flanker without source evidence had
  its own RED; reviewed field selections + source evidence now required and tested positively.
- Image nullable CHECK review added explicit MIME non-null; isolated source/asset/parent-denial controls
  verify permission gates without relying on missing metadata failures.
- A 62-test GREEN run initially failed report inventory because lc_collate was not a recognized setting;
  replaced with pg_database.datcollate query and reran end-to-end successfully. Final current result is
  the current 69-test command above. No failure is hidden as a production/environment success.

## Approved data and duplicate investigation

External package `DoomParfum Local Data/P1/20261110-221751` reverified: 42 file hashes plus manifest;
raw 1,479/160/420 rows and P1 SHA-256 match. Exact real pilot 12 perfumes / 5 houses / 58 material candidates
and 93 occurrences fits draft scalar/claim types in rollback-only test fixtures. No canonical mapping
approval, sample ETL or full import is performed. Synthetic captures/grants in those shape tests are
clearly test scaffolding, not actual upstream capture/permission evidence.

All 40 within-layer repeated groups / 39 profiles (top 16, heart 12, base 12; 40 extra occurrences) were
re-read from original arrays with exact source line/pointer/ordinals. Detailed derived rows stay ignored
locally, not public Git. No repetition in the 12 pilot. Raw occurrences remain immutable; canonical
perfume_notes uniqueness stays scope/perfume/note/layer. Repetition/alias ambiguity requires review/
quarantine reasons, never silent DISTINCT/merge/weights. SQL nfkc-lower-v1 does not assert equivalence
to preflight casefold/space candidate matching. See [[Data_Quality_and_Provenance]].

## Coverage matrix — full specifications are not all PASS

| P1 case | Current result | Actual DB test(s) | Deferred / not run boundary |
|---|---|---|---|
| OBS-01 | DB PASS | test_obs01_structured_and_prose_same_capture_survive | Actual adapter collection is IMP-P1-02 |
| OBS-02 | DB PASS | test_obs02_occurrences_exact_replay_and_changed_extraction | Full importer/idempotency and quarantine adapter NOT RUN |
| OBS-03 | DB PASS | test_obs03_nonempty_locator_key_type_and_scoped_selection | API validation NOT RUN |
| OBS-04 | DB PASS | test_obs04_resolution_member_and_minimum_count; test_review_guard_resolved_conflict_requires_matching_selection; concurrent test | Owner resolution UI NOT RUN |
| ACL-01 | PARTIAL: DB PASS | test_acl01_real_nonowner_sessions_private_overlay; test_img06_public_link_cannot_reference_private_asset | Detail/search/compare/export/cache/thumbnail API paths NOT RUN |
| ACL-02 | PARTIAL: DB PASS | test_acl02_private_overlay_does_not_mutate_public; test_public_matching_cannot_use_private_observation | Application cache replay / matching algorithm NOT RUN |
| ACL-03 | PARTIAL: DB PASS | test_acl03_scope_owner_and_editable_identity_spoof; test_active_rights_and_cross_source_fk | Verified HTTP/JWT scope adapter NOT RUN |
| ACL-04 | PARTIAL: DB PASS | test_acl04_shared_membership_revocation_and_no_private_inheritance; shared reader/editor tests | Product-facing shared mode NOT ACTIVATED; API NOT RUN |
| ACL-05 | DB PASS (schema only) | test_acl05_private_owner_perfume_variant_and_history; test_review_guard_private_variant_of_public_perfume_is_not_shared | P3 cart/purchase/bottle action workflows NOT RUN |
| ACL-06 | PARTIAL: DB PASS | test_acl06_grants_raw_staging_and_actual_force_owner; test_shadowed_temp_schema_cannot_spoof_principal; WITH CHECK test | API/RPC/worker/export services NOT IMPLEMENTED / NOT RUN |
| ACL-07 | PARTIAL: DB PASS | test_acl07_untrusted_dml_and_hidden_reference_boolean | Uniform API FK/unique error masking/rate limit NOT RUN; trusted SQL errors must not reach untrusted clients |
| IMG-01 | DB PASS | test_img01_exact_capture_asset_assessment_binding; test_same_source_different_capture_permission_rejected | Actual evidence/bytes applicability review NOT RUN |
| IMG-02 | DB PASS | test_img02_metadata_allowed_acquisition_missing_permission_rejected; test_null_image_mime_cannot_bypass_acquired_state | No acquisition or image bytes |
| IMG-03 | PARTIAL: DB PASS | test_img03_derivative_exact_parent_and_output_obligations; test_parent_selected_permission_change_invalidates_derivative | Legal compatibility review / actual transform/decoder NOT RUN |
| IMG-04 | PARTIAL: DB PASS | test_img04_hash_locator_and_immutable_capture | Actual binary hash/MIME/size/dimension verification NOT RUN |
| IMG-05 | PARTIAL: DB PASS | test_img05_revocation_descendants_and_expiry_operation_gate; test_expiry_is_rechecked_after_clock_passes; two-row cycle test | Proxy/cache/storage/URL replay/direct bucket/restore NOT RUN |
| IMG-06 | PARTIAL: DB PASS | test_img06_public_link_cannot_reference_private_asset | Actual EXIF/bytes/export/object manifest serving NOT RUN |
| REC-01 | NOT RUN | Schema/FK/RLS prerequisites only; migration recreate is not restore | Independent DB/object export/restore, corrupt/missing object/role/RLS rehearsal await IMP-P1-04 |

## Conservative findings and readiness

`database/schema_findings.md` records machine-inexpressible copyright truth, exact source/asset evidence
applicability, field/namespace formats, Unicode policy, local DB-role auth adapter, serialized READ COMMITTED
writes, conservative derivative license equality, retention deletion and matching input hash format.
These retain the approved model without weakening security/provenance. No new cloud/provider/source grant.

Schema is ready for a separately authorized IMP-P1-02 sample ETL **after Human Owner merges IMP-P1-01**;
review note/identity/rights mappings, implement actual adapter/validator/accounting/idempotency there.
No full dataset import, image acquisition, HTTP application/CI, benchmark, backup/restore or hosted readiness.
Regional imports still need rights AND samples. Final retention/RPO/RTO/external backup/cloud storage remain
DEFERRED. Review exact source checkpoint independently before the one final task receipt/publication.


## Independent review checkpoint 42ae1df — required fixes and rerun

Reviewer examined exact source `42ae1df46285b1f42772d92e13181dc16a55ac89` and performed three
rollback-only synthetic probes in dpt_schema_test; cleanup confirmed, no source/foundation changes.
The checkpoint was NOT accepted as ready: one HIGH (private/shared selected-rights display bypass),
three MEDIUM (expired private asset blocking unrelated writes; NaN positive amounts/volumes; CRLF/LF
checksums) and one LOW (endpoint check only at start) were recorded and corrected before publication.

Current regressions test public/private/shared selected-fact revocation and elapsed expiry, runtime
curator gating, unrelated Bob writes after Alice image expiry, active validation of changed images,
finite numeric values, canonical LF/CRLF checksums and refusal of remote contexts on direct SQL/reset/
migrate calls. Global structural image validation is now independent of dynamic use-time expiry;
source/per-asset use gates, exact bindings, revocation/parent invalidation and acyclicity are retained.
The unpublished empty foundation was verified empty (except field definitions) with no other connection,
recreated, migrated and replayed as no-op under canonical checksums. No dataset bytes were normalized,
no data-bearing/public/production migration rewritten. Source files are LF under scoped .gitattributes.
The updated checkpoint requires independent re-review; final review readiness is not claimed yet.
