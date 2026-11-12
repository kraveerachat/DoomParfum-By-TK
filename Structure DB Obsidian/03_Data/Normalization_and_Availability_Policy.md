---
id: DPT-DATA-STATUS-002
project: DoomParfum By TK
type: data_policy
status: proposed
updated: 2026-11-11
timezone: Asia/Bangkok
tags: [doomparfum, dpt-plan-002, planning]
---

# Normalization, Identity & Availability Policy — DPT-PLAN-002

## Entity and observation rules
`Brand` / `Perfume Profile` / `Product Variant-SKU` / `Retail Listing` are distinct. Stable research candidate code != canonical perfume UUID. Reconcile to 47-logical-table P1 model and actual merged schema before any future SQL.
Normalize source names with provenance and explicit aliases, not silent canonical merge. Do not merge same-name EDT, EDP, Extrait, reformulation, flanker, special edition or region-only variant without reviewed scent-identity evidence. A source record may contain repeated note claims/locators; never collapse P1 occurrence identity.
Pairwise `inspired_by` requires sourced manufacturer/credible support; looser allegations go to `reported_dupe` or `similar_profile`, each with confidence/source/date.

## Orthogonal lifecycle dimensions
- `production_status`: `in_production|discontinued|unknown`. A rumor is an observation, NOT confirmed discontinued.
- `market_availability`: `in_stock|out_of_stock|preorder|not_listed|unknown`, scoped to country/market, seller/channel, observed_at, verified_at and refresh date.
- Temporal evidence: `effective_at, observed_at, source_ref, evidence_kind, confidence, last_reverified_at, next_check_at`.
- A deleted/missing listing alone means `not_seen` pending verification; no destructive removal of canonical/history without review.
- Official brand lifecycle statements are stronger for production than community claims; available inventory should consider trusted local retailer evidence at market/time rather than treating global source as local stock.

## Safe UX default
Display verified/current/available first. Unknown is discoverable and marked as unknown, not filtered as discontinued by accident. Historically meaningful/discontinued profiles remain accessible through `include_historical` or source-backed comparison/relation links. No guarantee of real-time availability without a permitted real-time feed.
Review should explicitly consider same-brand alias, cross-brand sound-alike, different volume SKU, identical scent label but different formulation, and a product whose store is sold out but production is ongoing.
