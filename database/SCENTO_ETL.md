# Pinned Scento local ETL — IMP-P1-02

Approved scope: owner-merged Planning PR #1 (`bffb2fab1918dc5221a6c5da7920168bcae263ca`),
schema PR #2 (`9636ee740cdcd3d60633ac11745366814d1af05c`) and acquisition Planning PR #3
(`a908711fb4f37a12fbec3665a461b75c288c7dab`). Matching Planning PR #4 is still Draft.
This implements local source intake/review and exact-transcription catalogue materialization, not
matching, a search API/UI, image acquisition, hosted services or an unattended update center.

## Inputs and reviewed mapping

`scento_etl.py` reads only an already-downloaded snapshot at Scento revision
`086769ecf1add770ea6646bd4d88d39f0e7cddeb`. It verifies Git blob hashes and counts for all six
artifacts: perfumes.csv (1,479), houses.csv (160), materials.csv (420), LICENSE, README.md and
datapackage.json. Source files stay outside Git; no network/remote database argument exists.
Missing/tampered artifacts fail before database preparation. Original CSV cells, file digest and logical
record ordinal are retained in immutable scoped captures/staging. The external original42-file P1
package and all1,479 CSV/JSONL ordered note arrays were independently reconciled.

Attribution: Scento — https://www.scento.com/perfume-database ;
license: https://creativecommons.org/licenses/by/4.0/ . Local normalization/CSV-cell-to-JSON and
materialization are changes, not publisher assertions. Source image URLs do not license image bytes.

The approved P1 twelve IDs are a frozen cohort:12 profiles,5 houses,58 materials,93 note occurrences.
The handoff's separate research sample12/11/46/84 is preserved but is not the importer pilot.
`--plan-only` emits a proposed mapping; it cannot promote. Promotion requires the independently
reviewed exact-source policy and original proposal/report hashes plus canonical policy-content hashes.
Windows JSON line endings do not change policy-content identity; raw source hashes stay byte-exact.
Changing keys, source bindings, held sets or mapping values invalidates review. Arbitrary `reviewed`
flags or a nonempty reviewer name alone cannot authorize another mapping.

Private-local exact source names/IDs/house linkage/concentration labels/year and unambiguous note lists
are the reviewed boundary. Country, family/accord inference, aliases, translations, chemical composition,
semantic brand merges, media and public publication are not approved. Each canonical scent identity is
derived from its distinct source key; Balmain edition keys are never merged by name. Empty year and
concentration remain NULL. All `matching_eligible` flags remain false.

Khamrah is held for the previously documented external notes conflict; no unlicensed official-site
claim or fabricated second claim is imported to manufacture a conflict group. Full policy holds43
profiles with repeated source note lists plus Khamrah:44 review profiles,1,435 eligible for exact-source
promotion. The43 comprise39 pyramid profiles and4 general-list profiles. Historical40 extra occurrences
in39 profiles counted only pyramid layers; including general adds5 occurrences, for45 total. No source
occurrence is deduplicated. Both canonical-layer candidates and unselected flat-list claims survive.

## Local trust and database boundaries

Use the existing guarded [local harness](README.md): pinned task container/image/volume/loopback,
READ COMMITTED, serializer/advisory lock, original eight migrations and every deferred invariant/RLS
policy remain. Import targets are **only dpt_scento_test or dpt_scento_pilot**. `prepare_database` creates
a missing allowlisted database and replays existing migrations; it does not reset a data-bearing pilot.
The reset helper permits the dedicated test database but explicitly refuses dpt_scento_pilot.
Foundation and production targets are rejected before SQL execution.

The local Docker-admin/postgres adapter is an explicit trusted pilot boundary, not production/provider
authentication. Source/captures/claims/catalogue outputs use one private operator scope, not a public
source scope. Source use assessment cites the actual pinned LICENSE and OD-01/06. Replay checks active
automation/storage rights and source/artifact binding; expiry/revocation cannot be bypassed by a cached
capture. No new grant is created to evade revocation. Other runtime users cannot see private intake.
Source redistribution remains restricted by local operating policy; no public raw export is provided.

## Atomic intake, replay and evidence

- Stable IDs bind source/capture payload hashes, input cohort, adapter and reviewed mapping version.
  Raw CSV representations are lossless as parsed cells; pinned originals retain byte-level authority.
- Intake without a reviewed mapping creates review-only staging, not catalogue facts. Reviewed intake
  creates brand/note/perfume entities and source-backed observations/selections/ordered joins atomically;
  held profiles stay draft and carry precise review reasons. A review hold is not a silently passed rule.
- Source/staging, canonical row/selection/join and validation evidence replays are compared before no-op.
  Contrary preexisting state raises a reconciliation error instead of overwriting it or retaining it
  unnoticed. New raw versions do not overwrite old source claims. Unexpected batch members are rejected.
- Existing DB guards enforce FK/source/scope/materialization and note-list cardinality/order. Exceptions
  or cancellation roll back the transaction; no partial canonical writes are reported complete.
- SQL counters are collected under the same transaction lock as writes. Concurrent replays report new
  rows once; post-lock before/after client snapshots are not used for inserted-row accounting. The
  report is emitted only after COMMIT succeeds. It includes actual catalogue/approved/review counts,
  source code hash, execution time and a separately labeled local-harness wall duration.
- Report paths must be outside public Git or under ignored .local. Exclusive creation protects existing
  review/evidence files, including files created while the import was running. Choose a new report name.
  If report writing fails after a successful DB commit, preserve the existing file and rerun with a new
  report path; stable identities make this a replay, not a second canonical import.

## Commands and status

```powershell
python database/local.py start
python database/scento_etl.py --source-dir <external-pinned-folder> --cohort pilot --plan-only --report <new-external-proposal.json>
python database/scento_etl.py --source-dir <external-pinned-folder> --cohort pilot --mapping <reviewed-pilot.json> --report <new-external-execution.json>
python -m unittest discover -s database/tests -p test_scento_etl.py -v
python -m unittest discover -s database/tests -v
python database/validate_docs.py --task IMP-P1-02
```

The reviewed manifest is an explicit local artifact after independent mapping review; the command does
not grant its own review. The exact full-cohort rehearsal follows successful pilot/replay and keeps
all44 holds. Full-cohort runtime outcome and final current-suite results belong to the canonical task
and execution evidence, not inferred from these commands. The test suite needs the external licensed
source and reviewed mapping; no substitute product facts are generated when they are absent.

No migration001–008 or original immutable receipt changes. Source/packaging/research outputs and
the single LATEST handoff ZIP remain external. See the Obsidian IMP-P1-02 task and evidence for exact
current code checkpoint, observed outcomes, independent review, remaining limits and owner merge gate.

## Observed rehearsal (2026-11-11)

The private local database contains1,479 perfume identities (1,435 exact-source approved,44 draft holds),
160 brands,420 notes and11,972 canonical ordered note links. The12,448 raw occurrences remain intact.
Two batch identities preserve pilot/full execution:2,059 captures,2,134 staging rows,8,536 validation
results,10,489 source observations and8,845 canonical selections. Full replay adds zero rows and retains
the same inventory. Matching eligibility stays zero. Full source index and research normalization are
available in the external handoff; research brand candidates are not merged into canonical identities.

Focused19/19 and full regression98/98 passed (zero failures/errors/skips). Separate sanitized evidence:
[execution](evidence/scento_execution_summary.json), [tests](evidence/scento_test_results.json),
[schema](evidence/scento_schema_inventory.json). Historical IMP-P1-01 evidence is retained.

Full first transaction452.016s and current-source replay291.219s are local-harness wall measurements,
including deferred COMMIT. Replay overlapped regression, so these are not controlled before/after
performance results. Statement timeout is per statement and was not a reliable whole-import deadline.
All original trigger callbacks/global scans and serialized writer costs remain. Capacity profiling,
safe bounded transaction design and independent DB/object restore belong to IMP-P1-04. Do not disable
validation or treat the earlier250-record synthetic benchmark as a full-catalogue capacity guarantee.

The first/pilot execution reports pin importer c90da7...; the later full replay pins current a9a392...
(full hashes in evidence). Reproducible tests require the external pinned snapshot/review manifests;
missing artifacts fail rather than substituting synthetic product data. The trusted local-admin adapter
and fixed review-policy hashes do not implement hosted authentication or an arbitrary reconciliation
service. Human Owner reviews the Draft implementation PR before merge.
