---
id: DPT-EVD-IMP-P1-04
project: DoomParfum By TK
type: test_evidence
status: partial-blocked
owner: human-owner
updated: 2026-11-12
tags: [doomparfum, capacity, restore, evidence]
source_of_truth: "../../../README.md"
---

# IMP-P1-04 — Controlled measurements and independent recovery

Task [[IMP-P1-04_Local_Benchmark_and_Restore]], branch codex/imp-p1-04-local-benchmark-restore,
base main55d39cd619fa6c1ae70521720aa734d632a2083d after Owner merged PR5. OD03/05 authorize the
independent local subset. Full pilot/image integration remains separate from this measured subset.
Full replay is BLOCKED; this is not readiness to merge or a completed full-pilot acceptance claim.

## Benchmark outcomes — failures retained

| Case | Actual outcome | Backend seconds / limits |
|---|---|---|
| Attempt001 pilot fresh/replay,3pairs | Completed with original validation | Medians0.950582/0.465530; earlier harness, saved5d3a7742... source |
| Attempt001 fullfresh | FAILED23514 Future review timestamp | No passing full measurement; no automatic bypass/retry |
| Hardened002 pilot fresh/replay,3pairs | Completed with original validation | Medians0.545944/0.251596; warmup excluded |
| Hardened002 fullfresh1479 | COMMITTED | 246.226887; exactly1model/1image complete validation |
| Hardened002 fullreplay | FAILED23514 Future review timestamp | No completed replay duration; remains BLOCKED |

Exact pinned12/full1479 mappings and original SQL/migrations/rights remain unchanged. No fabricated
25/100/250 reviewed cohorts, artificial timestamp offset, backdate or disabled guard. Quiet/noncelease/
resource/report controls strengthened after independent review;30offline tests exercise their failure
paths. Same image768MiB/2CPU, session-local function tracking, warm environment; one full attempt is
descriptive, not a capacity curve or controlled comparison with the earlier452s/291s runs.

Fullfresh trace: validate_all_deferred109726calls/self132856.747ms, serialize_write65461/36974.653ms,
schedule_validation53110/31782.643ms, check_active_row19736/15163.568ms, validate_model1/8506.461ms.
Remaining callback/transaction-state overhead dominates this trace. No asymptotic claim. Original
full invariants remain enabled. Reported200000-clock-comparison probe saw0backward steps; no raw
independent trace or root-cause proof is supplied, and the future-review failure is not resolved.

Afterfailedreplay coreinventory exactly matched committedfullfresh and pendingmarkers0. Whole DB
56982551→57662487bytes afterVACUUMANALYZE (+679936), not a shrink claim. Freshfull1batch contains2059
staging/8236validations; persistentpilot's2batches retain75extra pilot staging/300validations, not
duplicate perfume identities. Heap/table/index/TOAST/counts/adminEXPLAIN are retained separately.

## Actual independent recovery004

Read-only consistent custom archive of dpt_scento_pilot, persisted/readback/hash-verified; separate
task-labelled pinned container/volume, networknone/noports/512MiB1CPU, fresh dpt_restore_test database.
All49tablecounts/contentSHA256s match. Five safe application roles/intra-group mappings, schema/
relation/column/function ACLs/owners,47RLS tables,203policies,244triggers (243domain+1ops),35functions
and431pg_constraint entries preserved:47PK/91unique/141FK/93CHECK/59constraint-trigger entries.
Private source unchanged; actual original model/image validators succeed on restored data.

All15verification controls passed: storedarchive, absentroles restore rejection, truncatedarchive,
data/security/role equality, fullvalidators, nonownerprivatecount0, write42501, probe rollback,
missingRLS detection/rollback, unchanged data/roles/source. Two ownedSYNTHETICobject copies total9896
bytes; missing and same-size corruption rejected. Real imagebytes0; no per-asset/provider/HTTP lineage
restore claim.29.656s includes the local workflow in a reused independent cluster with a fresh target
DB; it is not an accepted RTO/offsite/encryption/retention/RPO guarantee. Target stopped afterward,
labelledvolume retained. All dumps/passwords/rawstderr remain ignored.local, not public Git/ZIP.

Development failures preserved:001 empty-ACL fingerprint error;002 strict mismatch on the deparsed
rights CHECK;003 candidate success with an insufficiently narrow reusable comparator. Independent
review's three-space URL counterexample prompted exact known source/restore-definition SHA pins.
Only those two PostgreSQL16.15 forms can enter the additional8748-case proof on both servers; unknown
CHECK(true)/whitespace-bypass/other predicates reject before SQL. No source constraint/permission
was altered. All other security fields require exact equality.004 is final pinned-source execution.

## Tests, reviews and scope limits

Separate [regression](../../../database/evidence/capacity_test_results.json),
[schema](../../../database/evidence/capacity_schema_inventory.json),
[benchmark attempts](../../../database/evidence/capacity_benchmark_results.json),
[recovery attempts](../../../database/evidence/capacity_recovery_results.json).
Commands: `python database/verify_capacity.py`, focused test_etl_benchmark/test_recovery discovery,
and the two drivers in database/LOCAL_CAPACITY_RECOVERY.md. Passing unit/regression checks never
erase the failed full replay. Independent benchmark44file/hash/arithmetic checks passed; report
1670570bd60f273fcf34fb326d16c1ea80a037f9d8a369abd8d95bfd4f32e93e. Final pinned recovery review14
checks/37offline methods passed; e195412c8dd5c5ba830fa19314b90cc5ac3ee5368cf6688517fb19361adf041a.
Reviewer made0DB/Docker/network/Git calls; parent executed live tests. Exact commit/source-hash
publication verification follows in the task. Original migrations/importer/harness/receipts unchanged.

No final immutable receipt: IMP-P1-04 remains partial/blocked pending focused timestamp diagnosis and
full-replay acceptance, plus the separately gated actual-image integration. No owner decision, source
grant, cloud/provider, retention/RPO/RTO, production mutation or merge is approved here.

## Partial Draft publication — not ready to merge

[PR8](https://github.com/kraveerachat/DoomParfum-By-TK/pull/8) created OPEN/DRAFT on this taskbranch.
Source/evidencecheckpoint53fec48fd73ed4f1574c55e2b5535c56475d85f7 independentlyverified74/74checks;
all22tested sourcehashes match committedbytes. Report5fd8abd4186128dab276aa146abf9fff99c083b631c5e921b37601645c5846dc.
Protectedoriginals preserved; testCRLF→LF normalization independentlyverified text/AST-equivalent.
Finalmetadata source/evidenceblobs unchanged.8Markdown/5frontmatters/35wiki/9local/47table checks
passed0errors/0secretcandidates; exact18changedpaths in capacity_documentation_checks.json.
Fullreplay23514 remainsBLOCKED, no prematurefinalreceipt; recovery004subset/170regression evidence
isnot a waiver. Human Ownerreviews; resultingpublicationHEAD verified afterpush inPR/externalhandoff.
