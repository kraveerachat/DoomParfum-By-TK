---
id: DPT-EVD-P104-TEMPORAL
project: DoomParfum By TK
type: test_evidence
status: partial-blocked
owner: human-owner
updated: 2026-11-12
tags: [doomparfum, postgres, temporal, diagnosis]
source_of_truth: "../../../README.md"
---

# IMP-P1-04 — Temporal rejection follow-up

## Scope and stop line

Existing PR #8, codex/imp-p1-04-local-benchmark-restore; start6dc15a2e00ef979b0cbc39a72d461ebcd8533d47,
main55d39cd619fa6c1ae70521720aa734d632a2083d. Human Owner requests exact diagnosis before a smallest
justified correction. All original migrations/importer/rights/observations/receipts remain protected.
No backdating, trigger suppression, tolerance/guard change, automatic retries, source grant or merge.

The historical defect remains unresolved. A successful current replay is evidence for that run;
it cannot recover historical timestamp operands or establish a clock repair. No speculative runtime
fix is authorized by a passing later run. Bounded diagnostics and original-guard controls follow.

## Recovered historical failing rows

Read-only existing local PostgreSQL error logs identify:

| Server error log time (UTC, millisecond precision) | Source identity | Field | Entity ID | Observation ID |
|---|---|---|---|---|
| 2026-11-11 16:18:32.241 | armaf-match-point | notes.base | eddf28d2-37bc-56c0-8c3b-9fb38565e2fd | 9474d650-19fd-5496-9a28-479a19f808f8 |
| 2026-11-11 19:29:32.535 | armaf-club-de-nuit-maleka | name | d54fff25-fba7-5edd-888b-2f9d77a8f1bc | 42470420-2092-5fe2-a807-423a99e4bc8b |

Both logged INSERTs use reviewed_at=statement_timestamp(), reviewed_by=postgres and the exact full
reviewed mapping8d3842d452b23c429c0ca46eb6273027571d3270b55c3b3d0528fa59d525c3e9, followed by
ON CONFLICT DO NOTHING. These are actual failing INSERT identities, not invented examples. Raw logs
remain ignored.local, never public Git/ZIP. Exact NEW.reviewed_at, comparison-clock and delta were
NOT logged; error-log timestamps are not either operand and must not be substituted for them.

## Timing and trigger facts

The original selection_guard compares NEW.reviewed_at>clock_timestamp(). reviewed_at is timestamptz
without a rounding typmod; the importer supplies statement_timestamp() directly. The BEFORE trigger
executes before conflict suppression, so replay can reject an attempted duplicate selection.

[PostgreSQL16 time documentation](https://www.postgresql.org/docs/16/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)
distinguishes command-message receipt time from the current wall clock.
[PG16.15 source](https://raw.githubusercontent.com/postgres/postgres/REL_16_15/src/backend/access/transam/xact.c)
and [timestamp.c](https://raw.githubusercontent.com/postgres/postgres/REL_16_15/src/backend/utils/adt/timestamp.c)
show the cached statement clock and clock_timestamp derive from GetCurrentTimestamp.
A later clock read preceding a statement-start read needs temporal evidence; buffering alone is not
proof. Host/VM/NTP regression is a hypothesis, not an established cause. No host time setting changed.
[INSERT semantics](https://www.postgresql.org/docs/16/sql-insert.html#SQL-ON-CONFLICT) describe BEFORE
INSERT effects before ON CONFLICT handling. No skipped row implies skipped authorization here.

## Completed bounded diagnostic variants

Diagnostic001 resets only dpt_scento_test, applies original migrations, and temporarily captures the
comparison clock once before the same strict rejection; all reviewer/rights checks remain unchanged.
Fresh1479 commits311.515 client seconds; full replays153.562/151.375/151.328 seconds all commit,
zero new source/staging records and identical core inventory. No failure branch executed; no operand
trace was obtained. Original guard restored byte-exact. Its whole49table equality flag is false
because baseline was EMPTY before fresh import, not a valid replay-content comparison.

Diagnostic002 retains the original IF predicate byte-for-byte and adds DETAIL only after rejection;
three full replays155.812/157.781/155.110 client seconds commit. No23514 reproduced, original guard
restored exact, security/roles equal. Only staging_records raw content hash changes (2059→2059 rows).
Current conditions are descriptive; no optimization, capacity curve or resolved-defect claim.

## Staging bookkeeping and stronger inventory contract

Merged promotion_sql updates error_codes for held state=review rows even when unchanged.
Merged b_identity BEFORE UPDATE invokes identity_guard, which assigns updated_at=clock_timestamp().
Therefore zero-new-record idempotency is not zero writes. All44 holds must remain unchanged in meaning.

Original-guard fullpair003 commits fresh250.550492s and replay106.022935s (backend timers),
zero new source/staging records on replay and identical core inventory. The subsequent all49raw
content-hash oracle FAILS only on staging_records; this strict-comparison failure is retained.
Both SQL transactions succeeded; the report status FAILED_STOPPED refers to the post-run assertion.
No23514 occurred in this run. Exact original guard and security/roles remained unchanged. The follow-up oracle allows only strictly advancing updated_at on the exact44
held staging IDs independently derived from pinned cohort/reviewed mapping/batch/capture identities.
All2059 staging rows must match in every other column; all49row counts, other48table hashes, security,
roles, source/input hashes and exact original guard must match. It must reject any broader drift.
This changes an evidence comparison only; it changes no importer, validation, database constraint or
persisted record. Actual execution results and independent final readback follow before closeout.

## Verified current-run integrity and tests

Original-guard follow-up004 completes full replay107.147241 backend seconds. All49table row counts
have zero deltas; other48table content hashes match exactly. All2059staging rows match every column
except updated_at, with only the exact44independently derived held IDs strictly advancing. Rights,
source/mapping/importer hashes, security, roles, original guard and pendingmarkers0 verified.
Original observations, selected review times/rationales, canonical facts/links and audit unchanged.
No held source claim is deduplicated, resolved or made matching-eligible. Zero new records is not zero writes.

Full regression175/175 PASS150.422s,0failure/error/skip:170existing methods plus5new meaningful guard
controls. The new file tests current INSERT-conflict no-op, current UPDATE then explicit ROLLBACK,
future INSERT-conflict, future UPDATE and revoked-source-right conflict replay. Full49table/security/
role fingerprint equality and original function required after each no-op/rollback. Positive UPDATE
proves immediate guard acceptance, not committed deferred acceptance. All23source hashes fresh.
Actual command: ignored preservation wrapper run_temporal_regression.py calls verify_capacity.main();
old capacity reports/raw log are restored byte-exact; new report/log remain separately identified.

Recovery005 PASS30.093s,15/15controls: consistent read-only persistent-pilot backup, independent
networknone/512MiB1CPU restore target, all49table counts/hashes, original full validators, roles/ACL/
RLS/constraints, nonowner/missingrole/truncation/corruption controls and source unchanged.
Two owned SYNTHETIC objects9896bytes only; actual imagebytes0. Target stopped, labelledvolume/private
artifacts retained. No acceptedRTO, retention/RPO, encryption/offsite/provider/imagepipeline claim.

Published [follow-up](../../../database/evidence/temporal_followup_results.json),
[175-method regression](../../../database/evidence/temporal_regression_results.json),
[recovery005](../../../database/evidence/temporal_recovery_results.json) and
[independent review](../../../database/evidence/temporal_independent_review.md).
Prior23514and recovery development failures, diagnostic comparison limits and strict003failure
remain retained; new passing evidence never erases them. Original migration/importer/runtime code
unchanged; the only new executable source is the five-control regression test file.

Independent final measurement review15/15offline assertions reconstructs held IDs and validates all
hashes/rows/security/time exceptions. New test file independently statically reviewed, no blocking
finding; reviewer made noDBcalls. Detailed reports/hashes live in the external consolidated handoff
under08_OUTPUTS_APPROVED/pr8_timestamp_correction/independent_temporal_review. Exact committed-source
verification follows publication checkpoint. See [[IMP-P1-04_Local_Benchmark_and_Restore]] and
[[IMP-P1-04_Capacity_and_Recovery_Evidence]].

## Unresolved diagnosis and next action

CURRENT_FULL_REPLAY_ACCEPTANCE=VERIFIED_FOR_REPORTED_RUN_WITH_EXACT_STAGING_BOOKKEEPING.
HISTORICAL_TEMPORAL_OPERANDS=NOT_RECORDED. ROOT_CAUSE=UNRESOLVED. RUNTIME_FIX=NONE.
No23514reproduced across the capped7diagnostic executions and current original-guard pair/replay;
no exact failure-clock trace obtained. Passing runs do not establish a VM/NTP/host-clock repair.

Keep PR8 OPEN/DRAFT/BLOCKED for the requested exact diagnosis and justified correction, despite the
separately passing current full-replay/inventory gate. Stop repeated equivalent experiments at this
bounded checkpoint. Next: capture exact operands under reproducible conditions in a disposable DB;
then select the smallest justified fix and rerun controls/full replay/recovery. Do not backdate,
suppress/relax guards, auto-retry generic23514, change host time or infer new rights. No final receipt.
Human Owner may review PR4/6/7 independently; no agent merge, main write or production mutation.


## Exact source/evidence checkpoint closeout — 2026-11-12

Committed source/evidence checkpoint 571d46fb16fab4a0ae2f8a1395344b61f8f68501 independently verified126/126offline assertions,
0failures. All23testedsource hashes equal Git blobs;27main protected and28priorPR8source/evidence
blobs unchanged. Only new executable is the five-control regression test, reviewed77a2d0f8…86e50930.
Publicreports match raw sanitized results semantically (GitLF normalization only).175/175tests,
005recovery15/15 and004currentfullreplay verified;003strictcomparisonfailure/historical missing
operands remain visible. Independent report SHA256017d98bb406c1a4f19846815d5bda160bd7f1dc37973094ff64e90800ba110b6. Reviewer noDB/Docker/Gitmutation;
parent observed stopped recoverytarget/retainedvolume. Metadata closeout changes no tested code,
schema or execution evidence. Final publicationHEAD belongs in livePR/externalhandoff afterpush.
PR8 remains OPEN/DRAFT/BLOCKED for unresolved historical diagnosis/justifiedfix; no finalreceipt.
