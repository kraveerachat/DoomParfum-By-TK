---
id: DPT-DAT-SCENTO-AUDIT-2026-11-11
project: DoomParfum By TK
type: read_only_research_audit
status: research_complete_not_imported
updated: 2026-11-11
timezone: Asia/Bangkok
source_revision: 086769ecf1add770ea6646bd4d88d39f0e7cddeb
---

# Pinned Scento Full Snapshot — Read-only Data Quality Audit (2026-11-11)

> Research counts from the **entire** CC BY 4.0 published pinned snapshot, via connected GitHub read-only source. This audit is not a database import, not canonical review and not approval to import third-party imagery.

## Reproducible source files

- Repository pinned revision: https://github.com/Scento-com/perfume-dataset/tree/086769ecf1add770ea6646bd4d88d39f0e7cddeb
- `perfumes.csv` Git blob SHA: `4dc99cc840566f98c57be5aa02437960371ca7de`
- `houses.csv` Git blob SHA: `797d58078969e63fad109bc84f400d5614255d3c`
- `materials.csv` Git blob SHA: `60fa5f70a22bbe46de57f18ee59b2e61d134ab6a`
- Attribution: **Scento — https://www.scento.com/perfume-database**; CC BY 4.0: https://creativecommons.org/licenses/by/4.0/ . All numbers computed from source CSV content rather than README totals alone.

## Actual source profiling

| Audit measure | Observed |
|---|---:|
| Perfume source records | **1,479** |
| Unique publisher perfume IDs | **1,479** (0 duplicate IDs) |
| Perfume houses | **160** (0 orphan house foreign IDs) |
| Material/note source records | **420** |
| Profiles with **all three** Top/Heart/Base layers | **1,388** (93.8%) |
| Profiles with general notes only | **91** |
| Profiles with no source notes | **0** |
| Source records with descriptions | 1,479 |
| Source records with a release year | **80** |
| Source records with concentration | **1,228** |
| Primary families present | 1,479 |
| Secondary families present | 1,075 |
| Popularity rank present | 613 |
| Top-note occurrences (reported layers) | 3,850 |
| Heart-note occurrences (reported layers) | 3,873 |
| Base-note occurrences (reported layers) | 4,305 |
| General flattened `notes` entries | 12,448 |
| Distinct normalized raw note labels | 420 |
| Raw note labels unmatched to `materials.name` or listed aliases | 0 (text match only, not canonical review) |
| Records with repeated note labels in flattened `notes` | **149** (177 repeated occurrences) |
| Records with source URL | 1,479 |

**Important:** flattened `notes` includes the pyramid entries when provided. Its 12,448 occurrences MUST NOT be added again as independent note-layer associations. Preserve raw duplicate observations (e.g. repeated Oud) while defining normalized display policy. Blank release years and missing layers must remain unknown rather than fabricated.

## House types in this source snapshot

| Publisher `houses.type` | Houses |
|---|---:|
| Designer | 72 |
| Niche | 52 |
| Heritage | 18 |
| Arabian | 16 |
| Artisan | 2 |
| **Total** | **160** |

These are **publisher-specific labels** and cannot replace DoomParfum's independent country, market positioning and reference/alternative roles. The 160 houses must not be summed with the separate 220 research candidates to claim 380 unique brands. A safe crosswalk must handle duplicates, naming aliases and parent relationships before merge.

High-coverage house examples in this snapshot (number of perfume source records, not market totals): Armaf 189; Afnan 53; Creed 34; Acqua di Parma 32; Tom Ford 31; Dior 31; Parfums de Marly 29; Guerlain 26; Yves Saint Laurent 25; Amouage 25; Prada 24; Montale 24; Byredo 23; Lattafa 23. Publisher record counts are not independent verification of every currently marketed edition.

## Research fixture and explicit stop-line

A separate local 12-record fixture from the pinned file includes 84 note association rows, 46 raw labels, 7 complete pyramids and 5 source-general-only note lists. This tests shape and extraction readability; **does not include a full 1,479-row normalized import**, does not run PostgreSQL and includes **zero verified Dupe claims or approved bottle images**.

Source status: original owner OD-01/06 permits bounded local pinned licensed research; implementation into local PostgreSQL requires the accepted plan and approved implementation workflow. No data has been committed to public project GitHub, except these aggregate audit findings in Markdown.

## Next dependent tasks

1. Owner accepts revised D1–D9 full Product Index / progressive enrichment scope (NEW-07..11) in Draft Planning PR #3.
2. IMP-P1-02 licensed staging test from current merged P1 schema: begin 12 source records and replay, then bounded 1,479-source pilot; require stable external source keys and canonical crosswalk.
3. Searchable index / missing data flags; never require image and all three note layers for a basic search row.
4. Normalize source materials and note aliases with a reviewed synonym/ambiguity policy; do not assume string equality means semantic equality.
5. Separate structural similarity (notes/accords/family) from documented Dupe claims, evidence and confidence.

Related: [[P1_Source_to_Canonical_Mapping]], [[P1_Data_Profiling_Findings]], [[Data_Dictionary_Draft]], [[DPT-PLAN-002_Catalogue_Coverage_Images_Matching_Addendum]].

IMPLEMENTATION_NOT_STARTED=YES
POSTGRESQL_IMPORT_COMPLETED=NO
MEDIA_ACQUISITION_PERFORMED=NO
