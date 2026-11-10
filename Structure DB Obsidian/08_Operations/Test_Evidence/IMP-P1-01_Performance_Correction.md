---
id: IMP-P1-01-PERFORMANCE-CORRECTION
project: DoomParfum By TK
type: implementation_evidence
status: ready-for-review
owner: project
updated: 2026-11-11
tags: [doomparfum, postgres, performance, correction]
source_of_truth: "../../../README.md"
---

# IMP-P1-01 — Deferred Validation Performance Correction

Existing [PR #2](https://github.com/kraveerachat/DoomParfum-By-TK/pull/2), same branch
impl/p1-01-local-postgres-schema. Reviewed/START_HEAD3d377e0d78ec3af86e4c6ca03302b633c4ff11a7;
PR #1 approved merge bffb2fab1918dc5221a6c5da7920168bcae263ca. This is a correction checkpoint,
not a new task/PR/receipt. Original immutable implementation receipt is untouched and historical.
PRODUCTION_MUTATION=NO. Full regression and exact-source independent review passed; ready for Human Owner review.

## Confirmed root cause

Each of47 domain tables has row-level deferred z_model_contract. Every affected row previously called
validate_all_deferred(), which scanned the complete entity/selection/materialization/conflict/staging/
matching model through validate_model() and the complete image lineage through validate_images().
For N synthetic draft brands, two domain rows each produce2N callbacks and2N complete scans of each
validator at natural COMMIT. Entity/subtype scans grow with the data size, multiplying row-event count
by current model size; more expensive alias/note/image workloads can add further cost.
This is a confirmed repeated-global-scan risk, not an assertion of measured production capacity.

## Bounded method and actual measurements

Commands: `python database/performance.py --phase before` and `--phase after`.
Every case recreates only dpt_migration_probe in the existing task-labeled PostgreSQL16.15 container
(2CPU /768MiB,127.0.0.1:55431). Synthetic fixtures are explicitly named/labeled; no real dataset import.
Before uses exact published001–007; after applies additive008. All original constraints and validators
remain enabled. Each case starts with the same synthetic baseline; UPDATE/DELETE seed their target rows
outside the timed transaction. Statement timeout45s, lock timeout5s; no case failed/timed out.

Backend wall time brackets DML plus natural COMMIT. Function calls use session-local track_functions=pl,
force-flushed committed stats verified from a second backend. Docker/client wall time is separately
recorded in machine JSON. Setup/recreate/baseline cost is excluded from backend time. One observation per
case, local variance/profiling overhead apply; these timings are not an SLA or capacity extrapolation.

| Operation | Synthetic records | Before seconds | After seconds | Model scans | Image scans | Dispatcher calls |
|---|---:|---:|---:|---:|---:|---:|
| INSERT | 25 | 0.157388 | 0.033327 | 50 → 1 | 50 → 1 | 50 → 52 |
| INSERT | 100 | 1.167561 | 0.030732 | 200 → 1 | 200 → 1 | 200 → 202 |
| INSERT | 250 | 5.841950 | 0.051123 | 500 → 1 | 500 → 1 | 500 → 502 |
| UPDATE | 100 | 0.617120 | 0.031314 | 100 → 1 | 100 → 1 | 100 → 101 |
| DELETE | 100 | 0.383411 | 0.040310 | 200 → 1 | 200 → 1 | 200 → 202 |

Machine reports: `database/evidence/performance_before.json`, `performance_after.json`, with original
migration hashes, exact counts/status, backend and harness times, environment and limits. The25-record
after time need not be lower than100-record time because small timings include cold-plan/local noise.
Dispatchers still execute per row plus post-statement queue events; expensive global scans are coalesced.
The unchanged y_active_row calls for timed INSERT/UPDATE match their before counts; rights gates were
not removed to obtain these measurements.

## Exact equivalent correction and safety argument

Additive008_coalesced_deferred_validation.sql retains every original005/006/007 body/invariant/trigger,
including all47 z_model_contract triggers and y_active_row checks. It changes only the shared serializer/
dispatcher behavior and adds protected infrastructure state plus post-statement scheduling:

1. BEFORE every domain row mutation, the unchanged READ COMMITTED guard/global advisory lock apply;
   actual pg_current_xact_id() keys/increments a generation in private dpt_ops.validation_pending.
2. AFTER each domain statement, scheduled_generation advances and queues a deferred internal trigger.
   This handles BEFORE attempts skipped by ON CONFLICT DO NOTHING without leaking committed queue rows.
   Scheduling after the statement prevents queue-only IMMEDIATE from checking before the domain write.
3. The first deferred callback for dirty state executes both exact existing global validators against
   final rows. Only after both succeed does it delete the matching generation. Other queued callbacks
   return cheaply. A later write recreates/re-arms state, so a prior flush cannot exempt future changes.
4. Native transaction/savepoint rollback restores state/trigger events; a caught failed flush cannot mark
   invalid rows clean. Generation comparison avoids erasing a new mutation during a validation pass.
5. State/helpers have no client/curator/domain-owner grants, use fixed qualified paths and xid8 rather
   than editable GUCs, temporary objects, backend PID or32-bit transaction identity.

The new table is private operational infrastructure, not a48th logical domain table. No FK/RLS/rights/
conflict/materialization condition is weakened. Choosing complete coalesced scans preserves the approved
cross-table dependency coverage instead of prematurely narrowing alias/source/image impact graphs.

## Regression and independent review

Focused10-test correction suite passes: bulk INSERT/UPDATE/DELETE, one scan/dirty epoch, later invalid
INSERT/UPDATE/DELETE after IMMEDIATE→DEFERRED, actual commit/rollback cleanup, no-op replay/zero rows,
queue-only and domain-only IMMEDIATE, savepoint rollback, caught failed flush, direct client state/helper
access/GUC/temp spoofing and concurrent independent transactions. Full regression `python database/verify.py` passed79/79, failed0/errors0/skipped0, exit0,
103.266s at2026-11-10T20:09:53.851047+00:00 (2026-11-11 Asia/Bangkok). Exact test IDs/source
hashes are in database/evidence/test_results.json. Inventory retains47 tables, FK141/PK47/UNIQUE91/
CHECK93/deferred59/RLS203/FORCE RLS47;243 domain user triggers (47 new statement triggers), plus one
private operational deferred trigger excluded from domain counts. Foundation additive migrate passed:8
migrations,53 field definitions, zero other domain rows, zero pending markers. Exact SHA independent review completed as recorded below.

An initial benchmark setup missed dpt_ops creation in the pre-008 harness; corrected before measurements.
A readback command had PowerShell quoting errors; rerun successfully through a literal Python here-string.
Neither error was a SQL invariant failure, and no validator was disabled. Original001–007 hashes match
before/after. Published-migration/receipt immutability checks were added to documentation validation.

## Remaining costs and boundaries

- One full-model/image scan per dirty epoch remains; note/alias/selection/lineage complexity still matters.
- Per-row dispatcher and protected marker MVCC/WAL/index churn remain O(row events); long transactions
  retain native deferred event queues and locks. Post-statement events add O(statements) dispatches.
- Global writer advisory serialization is retained for correctness; multi-writer throughput is not solved.
- Frequent explicit immediate flushes legitimately cause repeated validation of successive dirty epochs.
- Synthetic draft brands exercise this risk, not complete ETL/source claims, real image bytes, worst-case
  aliases or large image graphs. Broader capacity/size/object restore remains IMP-P1-04, NOT RUN here.
- No cloud/provider/UI/ETL runtime/deployment, source-rights expansion or receipt rewrite. PR stays Draft.

References: [PostgreSQL16 deferred constraint timing](https://www.postgresql.org/docs/16/sql-set-constraints.html),
[row/statement triggers](https://www.postgresql.org/docs/16/sql-createtrigger.html),
[function statistics](https://www.postgresql.org/docs/16/monitoring-stats.html).

## Independent review / correction checkpoint

REVIEWED_SOURCE_HEAD=aa59b3d9e29e88697124d78e2f30e97271360586. Separate reviewer found no blocking
correctness/integrity/security/performance-correction issue. Eight bounded independent checks passed:
bulk12 brand/entity pairs plus updates (model1/images1/dispatcher61), pre-flush savepoint rollback,
named queue IMMEDIATE after no-op, caught failed flush, client state access, client helper execution,
concurrent valid rollback/invalid flush, and cleanup pending0/users0/entities0. Invalid final states failed
23514 and unauthorized access42501. Only dpt_schema_test live probes; no reset/foundation changes.
Reviewer verified47 trigger memberships, private postgres ownership/ACLs, published SQL immutability,
all16 source hashes and79/79 evidence, without rerunning full suite/benchmarks. Full detail:
`database/evidence/independent_review.md`. Source unchanged after review; closeout is metadata only.

Published START_HEAD3d377e0d78ec3af86e4c6ca03302b633c4ff11a7; original receipt
[[2026-11-11_000730_IMP-P1-01_Local_PostgreSQL]] remains historical and unchanged. No new receipt.
Existing PR #2 remains OPEN/DRAFT. Final published metadata HEAD is verified in GitHub/final report;
source checkpoint above remains the exact tested/reviewed implementation, avoiding a self-reference.

## Exact correction files changed

23 files relative to published reviewed head3d377e0 (whole-PR manifest is separate):

- `Structure DB Obsidian/00_Home/Project_Status.md`
- `Structure DB Obsidian/03_Data/Data_Quality_and_Provenance.md`
- `Structure DB Obsidian/06_Engineering/Security_and_Privacy.md`
- `Structure DB Obsidian/07_Delivery/Backlog.md`
- `Structure DB Obsidian/07_Delivery/P1_Pilot_Implementation_Plan.md`
- `Structure DB Obsidian/07_Delivery/Roadmap.md`
- `Structure DB Obsidian/07_Delivery/Tasks/IMP-P1-01_Local_PostgreSQL_Schema.md`
- `Structure DB Obsidian/08_Operations/Agent_Run_Log.md`
- `Structure DB Obsidian/08_Operations/Change_Log.md`
- `Structure DB Obsidian/08_Operations/Test_Evidence/IMP-P1-01_Implementation_Evidence.md`
- `Structure DB Obsidian/08_Operations/Test_Evidence/IMP-P1-01_Performance_Correction.md`
- `database/README.md`
- `database/evidence/documentation_checks.json`
- `database/evidence/independent_review.md`
- `database/evidence/performance_after.json`
- `database/evidence/performance_before.json`
- `database/evidence/schema_inventory.json`
- `database/evidence/test_results.json`
- `database/migrations/008_coalesced_deferred_validation.sql`
- `database/performance.py`
- `database/schema_findings.md`
- `database/tests/test_deferred_performance.py`
- `database/validate_docs.py`
