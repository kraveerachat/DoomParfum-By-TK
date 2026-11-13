---
id: IMP-P1-04-POST-MERGE-DIAGNOSTIC-MATRIX
project: DoomParfum By TK
type: diagnostic_evidence
status: blocked
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, postgres, temporal, diagnostics, post-merge]
source_of_truth: "../../../README.md"
---

# IMP-P1-04 — Post-merge historical timestamp hypothesis matrix

## Verified scope and no-go decision

PR8 source checkpoint remains3b01c8395d8ce28f426643f104da16090f11844d on
codex/imp-p1-04-local-benchmark-restore. Verified main58ceafe72129b70f0333c7c4f2c6f38dba855272
contains Owner-merged PR9–12. PR8 remains OPEN/DRAFT/BLOCKED and conflicts with current main.
The post-merge Master Prompt permits diagnostic preservation, not PR8integration or speculative
runtime repair. Shared Project_Status/log conflicts are coordinator-owned; deleting either history,
merging main here, or treating other PR merges as timestamp acceptance is not authorized.

**Current decision: NO-GO for another experiment.** No distinct reproducible condition or newly
captured historical operand has been identified. The existing bounded capture mechanism already
records the required clocks in isolated synthetic tests. Another future-dated control, normal
clock sample or broad1479-profile replay would repeat existing evidence rather than explain the
historical failure. This session made zero database calls and ran no temporal/import experiment.

[Sanitized machine-readable matrix](../../../database/evidence/postmerge_diagnostic_matrix.json)
contains source/evidence hashes, six hypothesis rows, retained replay facts and future stop criteria.
The original source, raw observations, failures, receipts,44holds and eligibility remain untouched.

## Exact known historical tuples and missing operands

The following identities come from the preserved temporal follow-up report. The logger timestamp
is explicitly not either operand used by the guard; it cannot fill a missing timestamp field.

| Source key / field | Entity UUID | Observation UUID | Recorded error logger time UTC | Actual R / C / delta |
|---|---|---|---|---|
| armaf-match-point / notes.base | eddf28d2-37bc-56c0-8c3b-9fb38565e2fd | 9474d650-19fd-5496-9a28-479a19f808f8 | 2026-11-11 16:18:32.241 | NOT RECORDED / NOT RECORDED / NOT RECORDED |
| armaf-club-de-nuit-maleka / name | d54fff25-fba7-5edd-888b-2f9d77a8f1bc | 42470420-2092-5fe2-a807-423a99e4bc8b | 2026-11-11 19:29:32.535 | NOT RECORDED / NOT RECORDED / NOT RECORDED |

R means the actual NEW.reviewed_at, C the exact single clock_timestamp sample consumed by the
comparison, S the statement clock in that same context, and X the transaction clock. Required delta
is the exact R-C in microseconds. Actual R, C and delta are null/NOT_RECORDED for both failures;
same-event R=S and complete backend/function/statement correlation therefore cannot be established.
Current/preserved source hashes identify the intended code; that is not a substitute for missing
same-rejection operands. This is not a finding that historical function drift actually occurred.

## Actual source semantics

Migration003 declares reviewed_at timestamptz NOT NULL. Migration006 attaches c_selection as a
row-level BEFORE INSERT OR UPDATE trigger. Migration005 line155 retains the strict predicate
NEW.reviewed_at > clock_timestamp() and raises23514/Future review timestamp. Importer lines273–276
construct canonical selections with reviewed_at=statement_timestamp(), using the unchanged
scento-csv-local-v1 transform and pinned source revision086769ecf1add770ea6646bd4d88d39f0e7cddeb.
No timestamp expression, row timestamp, trigger, rights check, clock or original migration changes.

PostgreSQL distinguishes statement-start time from the clock sampled during execution; changing
display precision or timezone does not recover either missing internal value. The documented
semantics support this distinction, not a claim that a clock step caused either historical failure.
[PostgreSQL16 date/time semantics](https://www.postgresql.org/docs/16/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT).

ON CONFLICT DO NOTHING is not a bypass for BEFORE INSERT processing. A replay can propose NEW
values and run validation without inserting a new canonical row. The existing
test_future_insert_is_rejected_before_conflict_suppression records a negative test for this path;
it was inspected, not rerun in this session.
[PostgreSQL16 INSERT semantics](https://www.postgresql.org/docs/16/sql-insert.html#SQL-ON-CONFLICT).
Trigger errors roll back with their statement/transaction; a surviving existing canonical row is
not the rejected NEW tuple. [PostgreSQL16 trigger behavior](https://www.postgresql.org/docs/16/trigger-definition.html).

## Hypotheses and the smallest distinguishing new observation

Every row is a hypothesis or trace-validity check, not an accepted cause. No probability is claimed.

| ID | Question | Smallest new observation | Interpretation / limit |
|---|---|---|---|
| B-H01 | Did wall-clock ordering change between statement capture and comparison? | one unforced rejected tuple with exact R,C,S,X,R=S,delta and attributable server/host clock-event or wall/monotonic context | R=S and R>C would establish reversed wall ordering for that captured context; it would not alone identify an OS, VM or synchronization cause |
| B-H02 | Was the actual NEW value/path different from the assumed statement expression? | R=S plus generated-script hash, backend/database/relation identity and ordered BEFORE-trigger/function hashes in that same rejecting context | R!=S redirects investigation to actual value origin/path; current intended source is not proof of the rejected value |
| B-H03 | Did an error or sampled clock come from another row, backend, statement or later instant? | one marker tying message/SQLSTATE/TG_OP, tuple IDs/field, backend/session and the exact C consumed by the predicate | R<=C with an alleged matching rejection first indicates invalid/misattributed instrumentation; a later clock sample cannot replace the deciding operand |
| B-H04 | Does zero-growth replay imply that guards were skipped or old times reused? | proposed NEW values/TG_OP/conflict context with an existing-row hash, if needed in a future actual rejecting trace | source/tests/docs counter this explanation: conflict suppression does not skip BEFORE validation; zero new records does not mean zero work or zero writes |
| B-H05 | Is apparent future time only display/timezone/precision? | full-precision time-qualified R,C and the exact numeric delta, not logger text | formatting alone cannot establish cause for this timestamptz comparison; investigate coercion only if actual value/SQL provenance warrants it |
| B-H06 | Do PR11snapshot fixes or the latest merges explain PR8? | a real rejecting temporal trace establishing that connection | no such connection is demonstrated; independent adapter security fixes and merged primitives/tools do not supply historical operands |

The useful new information is an **unforced actual23514rejecting tuple** with attributable exact
operands. The existing temporal_capture.py mechanism already samples C once at the comparison,
emits R/S/X and checks delta and R=S consistency. Its original-function definition pin is
c7a0a152b5d6b072168f3c439f9f033fc0e5f6bcf66aebb1104a347959000441. That function-definition digest is
not the whole migration005 file digest below. Instrumentation can change timing/scheduling even
where the tested decision semantics agree; passing parity controls do not eliminate observer effect.

## Retained evidence: what it proves and does not prove

Historical bounded capture recorded8unforced pairs, each R=S, with R-C from-4264to-3448microseconds.
It recorded zero natural rejections. Five original and five instrumented decision controls matched,
including deliberate SYNTHETIC future-time, revoked-rights, unauthorized-reviewer and contrary
materialization controls. These demonstrate the mechanism/guard controls, not the natural bug.
The240seconds value is the configured run budget, not an elapsed-time measurement in this review.

Full original-guard pair003 committed both statements but retained an overstrict staging-hash
comparison failure. Integrity004 then verified zero new rows across49tables,48unchanged non-staging
table hashes and all2059staging substantive rows unchanged. Exactly44held staging updated_at values
advanced as expected. Guard, security/roles and input/mapping/importer hashes remained exact. These
records must stay side by side: passing integrity does not erase the earlier failed oracle or
capture the two historical rejecting clock pairs. Zero-growth replay is not zero writes.

Previous175/218regression, recovery and bounded-capture results are cited as **historical, not rerun**.
Neither successful replay nor recovery guarantees absence of an intermittent time failure. PR11's
separate reused-snapshot revocation finding is not a demonstrated cause of23514at this guard.

## Required future go/no-go and cleanup contract

No run is authorized by this matrix. Before a later observation, require a specific new condition
or actual failure signal, an authorized isolated synthetic target, task identity/image/source pins,
common exclusive lease and baseline data/security/role manifests. Record same-call operands with
correlation metadata; do not import private/licensed profiles merely to search for a failure.

If such a condition later exists, propose at most one original/instrumented pair, at most8total
trials and240seconds run budget, retaining existing command/cleanup budgets. Stop sooner on a useful
capture or no new diagnostic value. Do not backdate, reset clocks, add tolerance, suppress triggers,
swap timestamp expressions, loosen permissions, retry broad imports or run the same control loop.
These bounds are a proposal for independent review, not a new authorization or a claim of execution.

Abort on target/pin/lease ambiguity, unexpected persistent/source/rights/eligibility drift, verdict
parity mismatch, an invalid/incomplete trace or failed restoration. Restore the exact original
function and verify full data/security/roles before/after on the owned isolated target; stop the
owned target and retain evidence if cleanup cannot be verified. Independent causal review of an
actual rejecting trace is required before the smallest justified correction in the same PR.
Integration still requires its explicit gate and Human Owner review; no final receipt while blocked.

## Source binding and checks performed now

| Source | SHA-256 of canonical UTF8/LF bytes |
|---|---|
| migration005 whole file | 3cd97a3fa8943bbdd4649f89a3def036c8b20390d9e2e22c08ee5075c59b7f64 |
| scento_etl.py | a9a392ab6c17b01f937a313536cd002f4e0446af2370518d8084fd28f3031be0 |
| temporal_capture.py on unmerged PR8 | e452a2e2157c809877265cae22d8f68050661b01c68a84eaf084620e529c9259 |
| test_review_timestamps.py on unmerged PR8 | 77a2d0f89768c79ea8c8474d72505a45644fda3b7c01a766a6d5b45686e50930 |

Migration003/005/006 and the importer match verified merged main. Capture/test files remain PR8-only
evidence, not code integrated into main. Six protected evidence files were hashed without editing;
the JSON matrix records exact hashes and distinguishes checkout versus canonical source bytes.
New static document/source consistency checks are separate from old execution results. No database,
clock/import experiment, runtime/test edit, migration, merge/rebase, source grant or Production
mutation occurred. Shared operational files are untouched. Independent parent review follows this
draft checkpoint; no final receipt or root-cause acceptance is claimed.

See [[IMP-P1-04_Local_Benchmark_and_Restore]], [[IMP-P1-04_Bounded_Temporal_Capture]],
[[IMP-P1-04_Temporal_Diagnosis]] and [[IMP-P1-04_Post_PR4_Reconciliation]] for preserved histories.

## Independent coordinator source review — 2026-11-13

Reviewer /root is independent of matrix author /root/postmerge_b_diagnostics. Read the exact JSON,
diagnostic note and task correction; independently matched all6source and6historical evidence
SHA256bindings to actual files and main where asserted. Inspected migration005strictR>Cguard,
migration006media/selection contract and importerstatement_timestamp construction. No blocking
finding in this evidence-only correction;216author static assertions are not runtime tests.
No newDBcall/experiment,source edit or causal evidence. Both historical tuples still lack actual
R/C/delta. Retained003oraclefailure/004integrity distinction and8normalprobes are accurate.
NO-GO for equivalent experiments; PR8remainsOPEN/DRAFT/BLOCKED/CONFLICTING. No integration or final
receipt. Later publication is a same-branch metadata checkpoint, not historical-rootcause acceptance.
