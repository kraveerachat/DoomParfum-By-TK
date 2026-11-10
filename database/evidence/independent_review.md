# Independent database review — IMP-P1-01

Reviewed source checkpoint: `d25083c67ea73384ab13068bf41fb70755c0a0d0`.
Original reviewed checkpoint: `42ae1df46285b1f42772d92e13181dc16a55ac89`.

The separate database reviewer inspected actual migration/runner/test semantics and performed bounded
rollback-only synthetic probes in dpt_schema_test. No source/Git/Obsidian/foundation/other-container or
production changes were made. Probe rows and temporary writer grants were verified removed.

| Finding at original checkpoint | Severity | Correction and independent confirmation |
|---|---|---|
| Private/shared selected materialized scalar readable after source revocation | HIGH | Grant gate now precedes scope/curator shortcuts; private revoked fact count0 independently probed; all-scope expiry/revocation regressions passed |
| Untouched expired private asset blocks unrelated tenant write | MEDIUM | Structural deferred binding checks separated from dynamic per-use/per-changed-image checks; expired Alice asset display=false and Bob list write succeeds |
| NaN passes positive volume/nonnegative money | MEDIUM | Every numeric measurement/amount rejects non-finite values; NaN variant update independently rejected23514 |
| CRLF working files vs LF Git checksums | MEDIUM | Scoped .gitattributes, LF source and canonical executable SQL checksum; committed/working bytes and CRLF/LF equivalence independently confirmed |
| Direct operations do not recheck local endpoint | LOW | Guard now checks local endpoint before SQL/migration/reset; mocked remote context refused before connection |

Re-review conclusion: **all five findings addressed; no remaining code/security blocker found in the
reviewed fixes**. Evidence hashes match actual source, machine evidence records69/69 passing tests.
Reviewer did not rerun the full suite. A remaining LOW documentation count (82 vs actual93 table CHECKs)
was corrected during metadata-only closeout. Current evidence and receipt use the measured93 count.
No source code/migration changed after the reviewed checkpoint; final commit adds documentation only.

Scope limits: no API/JWT/cache/export/error masking, actual image byte/SSRF/proxy/storage, ETL/import,
benchmark, independent DB/object restore or hosted/production behavior was tested by this review.
Human Owner must review and merge the Draft Implementation PR; review is not owner acceptance/deployment.

## S2 performance correction independent review — 2026-11-11

Exact reviewed checkpoint: aa59b3d9e29e88697124d78e2f30e97271360586, starting from published
3d377e0d78ec3af86e4c6ca03302b633c4ff11a7. No blocking correctness, integrity, security or
performance-correction finding identified. Ready for Human Owner review; owner alone decides merge.

Reviewer inspected008, performance harness, focused tests, old validators/security and recorded evidence.
Git confirms001–007 unchanged. Live metadata confirms47 tables retain serialization/row deferred triggers
and gain the statement scheduler. Ops state/helpers are postgres-owned and unavailable to client roles.

Eight bounded independent checks passed in dpt_schema_test: bulk12 brands/entities plus updates gave
validate_model1/validate_images1/dispatcher61; rollback to a savepoint before flush restored dirty state;
named queue IMMEDIATE after no-op still rejected an orphan23514; caught flush exceptions could not mark
invalid rows clean; client state access and helper invocation each failed42501; concurrent valid rollback/
invalid flush stayed independent23514; cleanup pending0/reviewer users0/reviewer entities0. No reset,
foundation/other-container/source/Git/Obsidian mutation or persistent grant/data change was performed.

All16 recorded source hashes match79/79 suite evidence (including10 new focused tests). Reviewer did
not rerun the full suite or benchmark. Five before/after single-run cases, including INSERT250
5.841950→0.051123s and500→1 calls per global validator, agree with recorded harness/evidence.

Remaining limits: full scans once per dirty epoch; O(row) dispatcher callbacks and marker writes;
global advisory serialization; no full licensed-data/image workload or capacity claim. API/storage/bytes/
ETL/cloud/production/independent DB-object restore remain outside review. Parent closeout edits metadata
only; executable source remains the exact reviewed checkpoint. No second receipt or automatic merge.
