---
id: DPT-PLAN-002
project: DoomParfum By TK
type: planning_pr
status: proposed
updated: 2026-11-11
timezone: Asia/Bangkok
tags: [doomparfum, dpt-plan-002, planning]
---

# DPT-PLAN-002 — Focused Catalogue Acquisition and Automation

> PLANNING ONLY. Owner has not accepted these decisions. This document does not authorize scraping, source import, image downloads, database migrations, deployment, or automatic publication. IMPLEMENTATION_NOT_STARTED=YES.

## Verified baseline and dependencies (read-only preflight, 2026-11-11)
- Public repository: https://github.com/kraveerachat/DoomParfum-By-TK; main `bffb2fab1918dc5221a6c5da7920168bcae263ca` from merged Planning PR #1 (merged 2026-11-10). GitHub truth supersedes historical notes that still say PR #1 is open.
- Implementation PR #2 https://github.com/kraveerachat/DoomParfum-By-TK/pull/2 is OPEN/DRAFT, unmerged at preflight. No edits to PR #2, no reuse of its branch or unmerged tables as an approved production schema.
- OD-01..06 in [[Decision_Log]] approve the pinned Scento CC BY 4.0 **local licensed pilot** and bounded data design/testing only, not broader third-party acquisition or hosting.
- Dependency order: PR #1 merged -> PR #2 foundation reviewed/merged -> IMP-P1-02 Scento 12-profile to pinned 1,479-row licensed pilot -> new-source implementation only after this separate Planning PR has human Gate P approval plus source-use rights.

## Goal and requirements
- R01/R02/R03/R05/R06/R07/R08/R12–R22: Discover Designer/Niche **reference** perfumes and Middle East, Southeast Asian and East Asian **alternatives**; regional emerging houses must not be dropped because sales metrics are unavailable.
- Current-first catalogue, retaining historical profiles relevant to known references and documented matching.
- Source-backed popularity/demand selection for both reference and alternative candidates. Separate `selection_priority`, `scent_similarity`, `evidence_confidence` and `market_availability`.
- Future owner/admin one-click catalogue update, with explainable delta/approval report and permitted incremental imports only.

## Work packages and acceptance ledger
| Package | Scope and deliverable | Gate |
|---|---|---|
| WP-00 | 220 candidate first-pass audit, external research CSV, source-use rights matrix. See [[Brand_Registry_Research]] | RESEARCH; identity not fully verified |
| WP-01 | Verify A-lane official identity/catalogue, product type, parent/alias/duplicate and current-vs-stock source cues | RESEARCH; no automated page extraction |
| WP-02 | Popularity source coverage, cohort bias, missing-value rules and weights proposal; see [[Popularity_Signal_Matrix]] | OWNER DECISION |
| WP-03 | Docs-only planning PR, task, rights, normalized identity/state, adapters, one-click ADR, acceptance, task dependencies | HUMAN Gate P |
| WP-04 | Separate source adapter + incremental pipeline PRs using individually authorized feeds/datasets after Gate P / foundation dependencies | NOT STARTED |
| WP-05 | Separate asset-rights/image, admin update center, worker/scheduler, size/restore benchmark and hosting decisions | NOT STARTED |

## Data / domain invariants
- Brand != Perfume Profile != Product Variant/SKU != Retail Listing; concentration/flanker/reformulation need evidence, not name-only merges. **Another 13 belongs to Le Labo**.
- `origin_country`, `market_position`, `catalogue_role` are separate. Brand role may be both, and `inspired_by` is supported **pairwise perfume evidence**, not a house-wide claim.
- `production_status`: in_production / discontinued / unknown. `market_availability`: in_stock / out_of_stock / preorder / not_listed / unknown with market/seller/timestamp.
- Store source claims with `observed_at`, `effective_at`, `source_ref`, permission, evidence locator, reviewer; unknown != false and sold out != discontinued.
- Research candidate codes are not canonical UUIDs. Any proposed fields must be reconciled against the existing 47-logical-table approved plan / real merged implementation before any migration.

## Source permission and popularity guardrails
- Research on official brand pages is NOT an approval for automation, bulk storage, image use, display or commercial reuse. Unknown permission => **NO-GO** for the corresponding action.
- Scento pinned dataset local scope only. Fragrantica terms effective 2026-01-14 §§5.3/5.7 prohibit unapproved automated access, unofficial endpoints and AI/dataset uses; no new adapter. Search results/review pages are citation-only research.
- Record each per-use permission: discover, automated_access, cache, store, display, redistribute, transform, commercial_use, AI_use, retain, share, expiry, attribution and territories.
- Never infer verified sales from rating/reviews/views; Trends UI is relative 0–100, not searches per month. Keep missing metrics NULL. Require per-source/region/period cohorts and feature coverage.

## Proposed one-click update contract
Owner/admin button -> authenticated queued `job_id` -> approved-source discovery -> permitted delta fetch (ETag/Last-Modified/updated-since if supported) -> immutable raw snapshot/hash -> normalize/validate/rights gates -> classify same/new/changed/conflict/quarantined -> allowlisted safe promotion only -> human conflict review -> report/checkpoint.
- Job states: queued/running/paused/completed/partial/failed/cancelled; worker independent from Next.js request, job lock, idempotency key, access-scoped audit.
- Source stable identity `source_id + external_record_key + concentration/edition`; canonical mapping is separate. `raw_sha256`, `normalized_content_hash`, `normalization_version`, append-only observations; rerun unchanged batch => **zero new canonical rows**.
- Rate/time/byte/request limits from rights policy. Honor 429/Retry-After, cancel, lock, expiry and revocation. No CAPTCHA/login/antibot bypass; no universal unattended publish.
- Source disappearance => `not_seen/unverified` pending policy, not destructive delete. Rights expiry blocks further display/promotion until reviewed.

## Proposed follow-on implementation PRs
1. `IMP-P2-01` brand candidate/source registry reconciliation + rights validator (after PR #2 and approved plan).
2. `IMP-P2-02` single permitted pilot adapter + staged delta/idempotency/quarantine (after IMP-P1-02 baseline and IMP-P2-01).
3. `IMP-P2-03` popularity observations + cohort ranking/coverage reporting (after rights-approved observations).
4. `IMP-P2-04` authenticated admin update center/queue/manual approval (after validated adapter).
5. `IMP-P2-05` scheduled refresh, independent image pipeline and hosting benchmarks (separate decisions/PRs).
No PR ID or implementation SHA is reserved by this naming proposal.

## Acceptance and negative controls
- 220 seed names retained without invented sales/status/verified-country labels; first-pass region/verification counts independently checked; focus TH brands La Palette, SCENTERY, BE CHERIE PARFUM, SÚNDALO included.
- Source matrix distinguishes human-read-only from approved automation/store/display/image permission; Fragrantica denied adapter test and rights-unknown negative cases.
- Brand/alias/parent link, concentration/edition same-name negative matches, Scento note repeats, `Another 13` product-vs-brand and private-vs-public access scope tests.
- Deltas: unchanged replay, changed claim, invalid hash/record, absent item, rights revoked/expired, simulated fake views, mismatched market, disputed discontinued, stop/resume cursor, partial transaction rollback.
- API authentication/RLS, single-writer lease and 429/denied source, corrupt/SSRF media, per-asset grants, cost/size tests and independent DB/object restore included as **future** verifications, never claimed PASS here.
- Docs links/frontmatter/diff, no raw third-party dumps/private data/secrets, one docs-only Draft PR. No code/build/runtime tests in this planning work.

## Owner decisions needed (all PROPOSED)
- NEW-01: Brand taxonomy, breadth, and A/B/C lane selection, with no permanent cap.
- NEW-02: Use-by-use source rights review and evidence retention/attribution scope before each new adapter.
- NEW-03: Relative popularity selection weights, minimum evidence coverage and small-brand cohort fairness.
- NEW-04: Production/availability evidence precedence and historical display policy.
- NEW-05: Admin one-click allowlist, human conflict queue, job controls and scheduler boundary.
- NEW-06: Local Python/Docker/PostgreSQL first, then measured provider/storage decision; no paid provisioning.
Human Owner reviews/merges the Planning PR before any new code. Do not merge on agent authority.
