---
id: DPT-DATA-ADAPTER-002
project: DoomParfum By TK
type: architecture_spec
status: proposed
updated: 2026-11-11
timezone: Asia/Bangkok
tags: [doomparfum, dpt-plan-002, planning]
---

# Permitted Source Adapter & Incremental ETL — DPT-PLAN-002

## Future architecture, not executable code
Owner-curated Brand Registry -> approved Source/Permission Registry -> approved API/feed adapter -> immutable local source snapshot -> stage/type/identity/rights validation -> classify new/same/changed/conflict/quarantine -> reviewed safe promotion transaction -> PostgreSQL canonical catalogue -> audit/report.
Use Python 3.11+ locally (Docker-ready) after source rights, P1 schema performance and Gate P; Colab optional bounded compute worker, never a workaround for unauthorized website access. Network access only from documented authorizations.

## Permission gates and source limits
Per source and field/asset document `discover,automated_access,cache,store,display,redistribute,transform,commercial_use,AI_use,retain,share`, reviewer, source URL/Terms version, timestamp, territory, request budget, attribution, expiry and revoke/delete obligations. Unknown => deny for that action. No adapters to Fragrantica, unofficial/internal endpoints, private Shopee sessions, CAPTCHA/antibot bypass.
Cost caps `max_duration,max_requests,max_records,max_bytes,per_host_rate,per_source_concurrency,retry_budget,next_cursor` are source-specific and measured. Graceful stop + resumable checkpoint. Respect HTTP 429/Retry-After and access revoked; no aggressive fixed 8-hour harvest assumption.

## Identity and idempotency
- Replay key: `source_id + stable_external_record_key + concentration/edition` when supported; map to separate canonical UUID after identity review, not by string equality.
- `raw_sha256` byte hash + `normalized_content_hash` and `normalization_version` for semantic delta. Metadata/rights changes tracked separately from payload.
- Append-only source observations with source record locators/occurrences and access-scope permissions; no overwrite of source history. If batch is unchanged: 0 new canonical rows.
- New safe and pre-approved data may promote only under transaction/review policy. Changed or ambiguous fields/conflicting claims -> human queue. Revoked/expired rights block display and promotion.
- Report: run/source/cursor/time, seen/new/same/changed/review/quarantined/blocked, failures/retries, permission status and source scope; resume exactly once.

## Admin Update Center (future)
Authenticated owner/admin button `Run Catalogue Update` returns `job_id` quickly. Background worker with single-writer lease and per-source locks; states queued/running/paused/completed/partial/failed/cancelled. Controls: dry-run, source/region filter, cancel, retry failed, diff review, approve/reject, last sync, resource use and permission expiry. Scheduler only after bounded manual dry-run, independent auth/RLS/rollback tests, explicit scope approval.

## Required future tests (NOT RUN HERE)
Replay idempotency; changed claims / normalization-version delta; duplicate perfume names; unknown/revoked/expired grant; skipped source; corrupted snapshot/hash; 429 and cursor restart; source disappearance; cross-scope RLS/data leakage; transaction rollback; fake metric spikes; image SSRF/oversized files; corrupt media/asset grants; independent restore; worker lock/race/cancel; audit and repeatability.
