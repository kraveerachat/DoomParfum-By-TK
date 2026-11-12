# Bounded temporal operand capture — diagnostic only

The full 1,479-profile import/replay and independently checked inventory remain verified.
The historical23514 Future review timestamp defect remains unexplained. This utility adds
observability; it is not an importer/runtime fix, retry policy or permission to change clocks.

## Reproduction contract

Run from the verified repository after reading the task. Use a new ignored report filename:

    python database/temporal_capture.py --report .local/p1-04/NEW_CAPTURE_REPORT.json --trials 8

Do not repeat equivalent experiments after the evidence below. A later run needs a new diagnostic
question or changed, documented reproduction conditions. The default fixture cannot reproduce
the full cohort's scheduling/load. No automatic licensed-cohort import/replay is performed.

The runner creates a fresh nonce-owned PostgreSQL16.15 pinned-image container and volume:
networknone, no hostports,512MiB/1CPU, existing image only (--pull=never). Names already in use are
refused, never adopted/reset. Only this dedicated target can be queried; there is no host/database
argument. Its password stays in an ignored local file, never in a report or public artifact.
The common task lease coordinates cooperating jobs. It cannot exclude arbitrary external operators.

Default8/max128 unforced fixture probes,240s run and45s cleanup budgets,5s statement/1s lock timeouts
and20s command bounds are configuration limits, not measured elapsed times. Failure stops the run;
no generic23514 retry occurs. Finally attempts exact restoration and stops only the attested owned
target, retaining the labelled volume for inspection. Cleanup failure is a failing result requiring
inspection; ownership drift must never trigger writes/stop against an unrelated target.

## Decision-equivalent instrumentation

All8 original migrations are compared with mergedmain before execution in the new target. Source
files are never edited. A minimal, explicitly SYNTHETIC public-scope brand/source/claim/selection
fixture uses actual database statement timestamps. No Scento/raw/private source or image is imported.

The original pg_get_functiondef is pinned to SHA256
c7a0a152b5d6b072168f3c439f9f033fc0e5f6bcf66aebb1104a347959000441.
Exactly one original predicate/declaration may be rewritten in this isolated database:

    comparison_clock := clock_timestamp();
    IF NEW.reviewed_at > comparison_clock THEN
        RAISE EXCEPTION 'Future review timestamp' USING ERRCODE='23514', DETAIL=...;
    END IF;

The single sampled value is the actual comparison operand. Preceding reviewer and active rights
checks/order, strict rejection and original23514/message remain. SECURITY DEFINER/search_path/owner/
ACL remain through CREATE OR REPLACE; the final exact original definition plus complete data/security/
five-application-group-role fingerprint equality is checked. Production-equivalent decision semantics
do not mean identical timing: additional work may alter scheduling or mask a transient.

Safe JSON DETAIL on rejection and NOTICE after a successful comparison contain only synthetic IDs,
operation/field, actual reviewed/comparison/statement/transaction timestamps, equality and exact
microsecond delta. No payload, rationale, credentials or private source content is emitted. The parser
checks all aware clocks, recomputes equality/delta and refuses unknown fields or malformed metadata.

## Actual one-run evidence

[Run report](evidence/bounded_temporal_capture_results.json) and
[test/source bindings](evidence/bounded_temporal_capture_tests.json).
Original and instrumented decision controls match in all5cases:

| Control | Outcome in both modes |
|---|---|
| Current-time duplicate INSERT | COMMIT, unchanged data |
| Deliberate future SYNTHETIC duplicate INSERT |23514 Future review timestamp |
| Revoked SYNTHETIC rights |23514 |
| Genuine separate guest login |42501 |
| Contrary selected scalar at deferred COMMIT |23514 |

Each control verifies unchanged data/security/application-group roles after no-op/rollback.
The instrumented deliberate-future control captures reviewed_at2026-11-13T15:23:41.698598Z versus
comparison_clock2026-11-12T15:23:41.702182Z, delta86,399,996,416microseconds. This proves captureability
and strict rejection; it is NOT a historical failure reproduction or real review.

All8 unforced SYNTHETIC probes have reviewed_at=statement_clock, deltas-4264..-3448microseconds,
zero natural rejection. Exact original function/data/security/application-group roles restored;
owned target stopped/volume retained. Separate read-only Docker inspection confirms actual pin,
networknone/noports/512MiB1CPU/read-only password mount and stopped state; no target restart/rerun.

12new offline methods pass independently with process execution denied; independent live-report
review62/62offline assertions pass. Previous175-method regression/15-control recovery/fullcohort
evidence is retained with all23source hashes unchanged, not rerun. Full187-method discovery NOT RUN.
The two new files have separate executed source/test canonical UTF8/LF hashes, not unspecified
checkout-byte hashes. A malformed-equality parser weakness found before live execution was fixed
and independently retested; it was not run against a database.

## Remaining stop line

HISTORICAL_ROOT_CAUSE=UNRESOLVED. RUNTIME_FIX=NONE. CAPTURE_MECHANISM=VERIFIED_ON_SYNTHETIC_FIXTURE.
Keep PR8 OPEN/DRAFT and blocked for historical diagnosis/correction. Do not infer VM/NTP/host-clock
cause or change timestamp expressions. Next evidence needs reproducible original failure conditions
and an actual rejected unforced pair; only then choose a justified fix. No main/production mutation,
new source/image rights, held-profile resolution, matching enablement or final receipt.
