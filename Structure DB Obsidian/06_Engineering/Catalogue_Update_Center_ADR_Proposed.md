---
id: DPT-ADR-007-009
project: DoomParfum By TK
type: proposed_adrs
status: proposed
updated: 2026-11-11
timezone: Asia/Bangkok
tags: [doomparfum, dpt-plan-002, planning]
---

# ADR Proposals — Data Discovery, One-Click Updates and Storage

These ADRs are **owner decision requests**, not accepted architecture or implementation authorization. Link to existing [[Tech_Stack_and_ADRs]] and OD-01..06; do not replace accepted P1 local pilot.

## ADR-007 — Registry + evidence-backed discovery priorities (PROPOSED)
Use open-ended brand candidate registry (Designer/Niche references and ME/SEA/EA alternatives) with region-balanced `mainstream/regional/emerging/niche-small` lanes. Rank perfume profiles, not entire houses, and separate popularity, data coverage/confidence, availability and scent similarity.
Alternative: global top-sellers only. Rejected as a proposal because it excludes regional houses with missing verified sales. Owner to approve weight/coverage policy before usage.

## ADR-008 — Rights-gated Python staged delta adapters (PROPOSED)
Local Python 3.11+ worker/Docker-ready; adapters only for explicitly allowed feeds/APIs or licensed data, immutable hashes, stable source keys, staging, conflict queue, audit, idempotent promotion. Reconcile with 47-table P1 model and PR #2 measured performance before implementation. No new crawler in this PR.
Alternatives: scrape every public page, bulk text/photo download, proxy bypass; **not allowed** absent authorization. Separate source and asset permissions.

## ADR-009 — One-click authenticated job queue and operations (PROPOSED)
Owner/admin creates bounded job -> returns ID -> independent background worker -> visible report, review queue, cancel/retry, audit. Auto-promote only pre-reviewed trusted fields/sources with explicit rights; unknown/conflicts need human approval. Optional schedule later; no request that runs for eight hours in a Next.js handler.
Alternatives: unreviewed one-click universal publish, frequent serverless long-running jobs; unsafe or unsuitable.
Storage choice remains deferred until measurable DB/objects/restore benchmarks: local PostgreSQL first, optional Supabase Free/R2 later **without provisioning now**. No subscription/spend decision is approved.

## Security and test impact
Owner/admin authorization, RLS by access scope, source-specific rate/quotas/rights expiry, single-writer lock and idempotency key, immutable evidence, upload/media SSRF and MIME checks, audit/cancel/rollback, restored data/asset permissions. Negative-control test plan is in [[DPT-PLAN-002_Focused_Catalogue_Acquisition_and_Automation]].
OWNER_APPROVAL=REQUESTED. IMPLEMENTATION_NOT_STARTED=YES.
