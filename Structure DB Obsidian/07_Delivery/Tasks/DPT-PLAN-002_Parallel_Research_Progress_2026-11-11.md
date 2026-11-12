---
id: DPT-PLAN-002-WP03
project: DoomParfum By TK
type: research_progress_ledger
status: in_progress
updated: 2026-11-11
timezone: Asia/Bangkok
planning_pr: 3
---

# DPT-PLAN-002 — Parallel Workstreams Progress Ledger (WP-03, 2026-11-11)

> This is a **research/status note only**. It does not grant Gate P, change production, import database rows or implement a data pipeline. Owner reviewed/merged status must be checked from GitHub, not inferred from completed research.

## Parallel execution status (do not confuse research with implementation)

| ID | Goal | Done this session / evidence | Remaining implementation |
|---|---|---|---|
| D1 | Brand Discovery | 220 source seed preserved; **27 first-party presence observations** including 3 new: SAFF & Co. (Indonesia), Scent Journer (Singapore), Szindore (Malaysia). Of 220: 191 needs review, 2 third-party only, 26 first-party observed, 1 first-party alias pending. All 220 source use rights remain pending. | Verify identities/parent/aliases and widen regional coverage; no comprehensive market census yet |
| D2 | Product Model Index | **Full pinned Scento source audited: 1,479 perfumes, 160 houses**, 0 duplicate source IDs, 0 orphan house IDs. Local 12-profile searchable research fixture generated; no complete 1,479-row source index serialized in public Git. | Implement approved-source all-model index and staged import after Gate P |
| D3 | Profile/Notes ETL | 12 licensed pilot profiles, 84 note occurrences, 7 full pyramids, 5 unlayered-only in local research fixture. No PostgreSQL imports. | IMP-P1-02 read/normalize/stage/replay into already merged P1 local DB foundation |
| D4 | Notes/Accords | 420 material rows and 420 raw labels audited from full pinned source; **149** full-source profiles contain within-record repeated flattened note labels, requiring normalization rule. | Alias/canonical crosswalk, layer preservation, accord distinctions and conflict review |
| D5 | Bottle/Note Images | 2 Commons note-image metadata candidates (Lavender, Lemon); Lemon source page declares CC BY-SA 4.0; no acquired files. | Asset-specific permissions, proper attribution, note sharing, edition-specific bottle photos |
| D6 | Search | Offline CSV/CLI search fixture for 12 licensed profiles has been generated and checked with exact name/note lookup; **no live Next.js search or API**. | PostgreSQL index/API/UI, source/completeness flags, market-sensitive filters |
| D7 | Dupe Claims | Data fields and empty evidence queue prepared; **0 verified pairwise Dupe claims**. | Obtain permitted sources/claims and manual evidence review |
| D8 | Matching | 21 previous exact note label overlap pairs for QA only; no calibrated similarity engine. NEW-08 proposes separating structural score from claims and confidence. | Owner weight decision, benchmark, explainable side-by-side and negative tests |
| D9 | Admin Updates | States/source permissions/checkpoint/lock/one-click ADR documented. | No worker/scheduler/admin feature code, requires accepted plan and reviewable implementation PR |

## Current independent research lanes

- **Lane A** Brand: official-source discovery with open permissions (user project seeds; three new verified first-party *presence* observations). URLs: https://saffnco.com/collections/shop-all ; https://scentjourner.com/ ; https://szindore.com/shop/ . These stores may contain non-perfume products; shop page listing counts are NOT perfume counts. Official presence does not imply scraping/media rights.
- **Lane B** Licensed source: Scento pinned full snapshot coverage and data quality audit, [[Pinned_Scento_Full_Snapshot_Audit_2026-11-11]], with proper CC BY 4.0 attribution. Full source is inspected read-only. Local extracted research pack contains only 12-profile fixture.
- **Lane C** Media: open-license source page review/asset placeholders only. No third-party image binaries acquired.
- **Lane D** Search/dupe: offline search and comparison fixtures; no unreviewed similarity claims or unsupported 90%-identical figures.
- **Lane E** Implementation: Gate P blocked by open Draft Planning PR #3. Planning docs only on branch.

## Reconciliation of the two progress numbers

The 220-owner research brands are a **candidate discovery registry**. The 160 Scento houses are a **single licensed publisher snapshot**. Overlap is unknown until crosswalk; do not sum them. Similarly, `1,479 examined` is not `1,479 imported`. Having 420 source material labels does not mean image licenses for all 420. Having literal overlapping notes does not mean proven fragrance Dupes.

## Offline tests & limits

Local fixture assertions: 220 unique candidate codes; 27 first-party presence observations; exact 12 source record keys; 84 linked note rows, 46 labels, all note counts per profile consistent; 7 full pyramids; all sample image/dupe statuses pending; searches Aventus and YSL Libre find one each, a Bergamot query finds candidates and a nonexistent query gives zero; 12 PASS, 3 NOT RUN (Postgres import, full 1,479 export and media binary download). **No schema migration tests rerun** in this environment.

## Human Gate P checklist

- [ ] Accept NEW-07 full permitted-source-visible product discovery plus progressive enrichment (not all world perfume editions guaranteed).
- [ ] Accept NEW-08 separate structural similarity vs evidence, confidence and recommendation rank.
- [ ] Accept NEW-09 partial profile index/search model.
- [ ] Accept NEW-10 bottle/notes asset-specific rights and attribution/revocation.
- [ ] Accept NEW-11 pairwise Dupe evidence types/contradictions review.
- [ ] Review Fragrantica reference-only and independent source rights gates.
- [ ] Review and **owner-merge** this Draft Planning PR #3 only after accepting the revised scope.

After Gate P: proposed independent implementation sequence from latest main: IMP-P1-02 Scento ETL (12 replay → bounded 1,479); product/note canonical normalization; authorized media registry; search; vetted Dupe graph + matching; update admin/worker. Any further cloud spend/deployment remains separately gated.

## Owner-visible research deliverables

Research archive `DoomParfum_WP03_Parallel_Research_Progress.zip` (prepared externally to public repo) contains 220-row updated research CSV, 3 first-party observations, per-region status, 11-house literal-name crosswalk, 12-source-profile search fixture, per-profile note readiness, media queue, full-source *aggregate* audit JSON, nine-lane workstream ledger, offline acceptance tests and CLI. Not an application database backup or an image bundle.

IMPLEMENTATION_NOT_STARTED=YES
PRODUCTION_MUTATION=NO
GATE_P=AWAITING_OWNER_REVIEW
