# Controlled local capacity and recovery — IMP-P1-04

Approved source: merged PR5 at55d39cd619fa6c1ae70521720aa734d632a2083d, P1 plan and OD03/05/06.
Current Owner request permits the independent local DB/performance subset while the image task is
reviewed separately. Actual image/provider/HTTP recovery is excluded; no migration is rewritten.
No cloud, remote host, original pilot reset, unlicensed image or production operation exists here.

## Controlled unchanged ETL workload

`etl_benchmark.py` uses only original reviewed12 and1479 policies. Arbitrary25/100/250 source slices
would not satisfy the fixed mapping review, so they are not manufactured as approved inputs. It
recreates only dpt_scento_test, applies all eight migrations outside timing, performs a pilot warmup,
three fresh/replay pilot pairs and one optional full pair. No constraints/triggers/RLS/rights checks
are disabled. The actual pinned image/container memory768MiB and2CPU are attested before mutation.

A common Git-checkout nonce lease coordinates this driver, recovery and the new regression runner
across worktrees. All other SQL client sessions, including idle, cause refusal. Normal DROP never
evicts clients; a new racing connection makes reset fail. The lease cannot exclude noncooperating
administrators or unrelated host load. Keep other test jobs quiescent. No cold-cache/parallel claim.
Reports reserve a new ignored path exclusively and checkpoint atomically with unique temp names.
Whole-client deadline900s cancels only its unique application and explicitly reports unknown commit
state if cancellation/readback cannot be confirmed; per-statement45s is not a whole-import deadline.

```powershell
python database/etl_benchmark.py --source-dir <pinned-folder> --pilot-mapping <reviewed-pilot.json> --full-mapping <reviewed-full.json> --report .local/p1-04/new-benchmark.json
python database/recovery.py --output-dir .local/p1-04/new-recovery
python database/verify_capacity.py
```

Backend wall time brackets the streamed original SQL through natural COMMIT. Client time includes
guarded Docker/psql overhead. Session-local PL-function call/total/self times are force-flushed and
read from a second backend; tracking adds overhead. Heap/table/index/TOAST/whole DB sizes and row
counts are separate: table_bytes already contains TOAST/FSM/VM, so do not add TOAST twice. Whole DB
includes system catalogues. Read-only admin EXPLAIN is not application/RLS search performance.

## Actual benchmark result and blocker

Two attempts preserved: attempt001 fullfresh failed23514 Future review timestamp; hardened002
completed fullfresh1479 in246.226887s with exactly1 validate_model and1 validate_images call, then
fullreplay again failed23514. Fullreplay acceptance is **BLOCKED**, not a passing idempotency benchmark.
Committed core inventory was unchanged on readback; pending markers0. Original guards/timestamps/
mapping policy remain intact. A separate200000-call clock probe observed no backward step; the cause
of the timestamp rejection is not established. No arbitrary offset/backdating or validation bypass.

Fullfresh callback trace: validate_all_deferred109726calls/self132856.747ms, serialize_write65461/
36974.653ms, schedule_validation53110/31782.643ms; complete model scan1/8506.461ms. These measurements
identify remaining row-callback/transaction-state overhead, not repeated full-model execution.
One full pair cannot establish a capacity curve or asymptotic complexity. Earlier452s/291s runs had
different conditions and are not an optimization comparison. Passing unit/regression results do not
erase the separately failed full replay. Future focused timestamp diagnosis and performance design
must preserve integrity and be separately reviewable; no migration/semantic fix is smuggled here.

After failed replay: whole DB56,982,551bytes before VACUUM ANALYZE,57,662,487after. A database need
not shrink after metadata/statistics changes. Fresh full has one batch2059 staging/8236 validations;
the persistent pilot retains its earlier75 pilot staging/300 validations as a separate historical batch.

## Independent local recovery boundary

The recovery driver reads the persistent dpt_scento_pilot via consistent custom pg_dump, writes the
private archive only under ignored.local, verifies the persisted bytes, and restores to a separate
pinned PostgreSQL container with network=none, no exposed port,512MiB/1CPU and a dedicated task volume.
It preserves safe application role mapping, owners, grants, RLS, constraints, guard functions and all
table row hashes/counts; it never exports role passwords or copies unrelated test login roles.

Actual negative controls cover missing required roles, corrupt/truncated archive, missing RLS,
non-owner reads/writes and independent object integrity. Intentionally invalid metadata exists only
inside a rolled-back transaction on the isolated restore target. A failed backup/restore is reported
and stopped, never relabeled success by ignoring errors or using --no-owner/--disable-triggers.

Owned SYNTHETIC local binary objects test independent copy/manifest hash/missing/corruption paths.
They are not real image assets, DB asset-permission lineage or third-party reuse grants. The source
pilot has0 actual image bytes; its DB-only recovery cannot prove image delivery. Same-host folders/
volumes are not an offsite failure domain. Dump encryption, retention, external backup, RPO/RTO and
provider selection are not implemented or accepted. Passwords, dumps, private source rows and raw
stderr remain ignored.local and must not enter the public repo or handoff ZIP. No signed URLs.

Actual recovery/full-suite results and exact current hashes belong to the canonical task and separate
capacity_* evidence; commands above are not PASS claims. Historical evidence and receipts stay intact.
Human Owner reviews the Draft PR; full image integration and the failed full replay remain explicit gates.

Final recovery004 completed29.656s using a fresh target database in the reused independent task cluster.
All49 table count/content hashes, five application-role mappings,47 RLS tables/203 policies/244 triggers/
431 constraints and35 functions checked; the source remained unchanged. Every one of15 verification
controls passed, including missing roles, truncated archive, non-owner42501 and rolled-back missing RLS.
Two owned synthetic objects total9,896bytes; missing/same-size corruption controls pass, real images0.
The restore container was then stopped with its labelled volume retained. This is not an accepted RTO.

Development failures are retained: empty ACL deconstruction needed an explicit empty-array branch;
the restored rights_assessments_k4 CHECK text flattened associative OR grouping. Final comparison
requires exact approved source/restored definition hashes before its additional8,748-case proof on
both servers; unknown predicates fail before SQL. An independent three-space-URL bypass counterexample
is rejected. No constraint/permission was changed to make comparison pass; all other security fields
remain exact. Intermediate successful execution with the earlier comparator is superseded by004.


## Current temporal follow-up (2026-11-12)

Current fullreplay succeeds with the original guard; historical intermittent23514rootcause remains
unresolved. See [diagnosis](../Structure%20DB%20Obsidian/08_Operations/Test_Evidence/IMP-P1-04_Temporal_Diagnosis.md)
and [exact execution evidence](evidence/temporal_followup_results.json). Original003fresh/replay
250.550492/106.022935s bothCOMMIT; post-run strictstaginghash comparison fails. Independently reviewed
004replay107.147241s verifies all49zero countdeltas/48exactcontenthashes/2059exactsubstantive staging
rows and exactly44strictlyadvancing held updated_at values. This is0newrecords, not0writes.
Full175/175pass150.422s; recovery00515/15pass30.093s,2SYNTHETICobjects9896bytes/0actualimages.
Prior capacity_* reports remain historical; temporal_* files are additive. The exact preservation
wrapper/diagnostic scripts and hashes are in the external consolidatedhandoff; fullsuite uses the
existing verify_capacity.main exclusivelease. No importer/migration/runtime/guardfix or hostclock
change. KeepPR8OPEN/DRAFT/BLOCKED/no finalreceipt until the requested exact diagnosis and justified
correction are complete. Current passing replay does not prove historical clock health.
