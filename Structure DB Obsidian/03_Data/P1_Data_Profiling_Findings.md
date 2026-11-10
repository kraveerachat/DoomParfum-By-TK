---
id: DPT-DAT-007
project: DoomParfum By TK
type: research
status: draft
owner: project
updated: 2026-11-10
tags: [doomparfum, planning, profiling]
source_of_truth: "../../README.md"
---

# P1 Data Profiling Findings

Research date: 2026-11-10, Asia/Bangkok. Findings are observations; schema/hosting choices remain PROPOSED.
No production ingestion, image download or raw dataset commit occurred.

## Method and reproducibility

After inspecting its license, read one small, pinned Scento export, not a crawl of the live catalogue.
Calculated aggregate completeness across all 1,479 JSONL records and inspected selected records in depth.
Read houses/materials CSV with Python standard-library `csv.DictReader`; read JSONL with `json.loads`.
Missing means JSON null, empty string or empty list; whitespace-only and semantic accuracy were not audited exhaustively.
Duplicate ID tests are exact; the name candidate test uses `(house_id, name.casefold())`, without fuzzy matching.
Checked perfume house IDs against house IDs, and flat-note sets against the union of recorded layers.
No database/ETL implementation or database benchmark was run.

- Publisher/release: Scento, `2026.10.29`; source revision `086769ecf1add770ea6646bd4d88d39f0e7cddeb`.
- [Pinned README](https://github.com/Scento-com/perfume-dataset/blob/086769ecf1add770ea6646bd4d88d39f0e7cddeb/README.md), [descriptor](https://github.com/Scento-com/perfume-dataset/blob/086769ecf1add770ea6646bd4d88d39f0e7cddeb/datapackage.json), [license](https://github.com/Scento-com/perfume-dataset/blob/086769ecf1add770ea6646bd4d88d39f0e7cddeb/LICENSE).
- Attribution: Scento — https://www.scento.com/perfume-database; CC BY 4.0, https://creativecommons.org/licenses/by/4.0/.
- Changes here: aggregate analysis and selected factual examples; no source descriptions reproduced.
- Temporary raw files: `C:/Users/User/AppData/Local/Temp/doomparfum-p1-research/`, outside Git; not an application data directory.

| File | Bytes | SHA-256 |
|---|---:|---|
| perfumes.jsonl | 1,207,141 | `695d9e7b5a61bb482ab84e04ae82806ca684bd26fab95b2c8e2931b6d561dfe2` |
| houses.csv | 29,765 | `f076db1629fc1c07fe417811a55891bbfe70991319bf5c520766253f80cc9c18` |
| materials.csv | 87,027 | `9b342c803f0b370e96106a4dff0ae56f1f5340bdc82c6e32d180473a9f31764c` |

Reproduce against the pinned raw URLs: count parsed rows; for each field count null/empty-string/empty-list;
group IDs within each table; group perfume `(house_id, casefold(name))`; subtract house ID sets;
count all-three-layer nonempty and all-three-layer empty; compare flat/layer note sets.
This is an analysis recipe, not a committed executable pipeline.

## Observed completeness

| Table / field | Missing / denominator | Implication |
|---|---:|---|
| Perfume id, name, house_id, house, family, character, seasons, times_of_day, notes, description, url | 0 / 1,479 each | Presence does not prove correctness or independent evidence |
| year | 1,399 / 1,479 (94.59%) | Nullable; do not infer launch dates |
| perfumers | 1,410 / 1,479 (95.33%) | Array, optional; not a mandatory perfume attribute |
| concentration | 251 / 1,479 (16.97%) | Unknown identity dimension must survive staging |
| secondary_family | 404 / 1,479 (27.32%) | Optional source taxonomy |
| top_notes, heart_notes, base_notes | 91 / 1,479 each (6.15%) | Same 91 have flat notes only |
| popularity_rank | 866 / 1,479 (58.55%) | Rank is source-specific; not rating or similarity |
| House country / founded | 2 / 160; 63 / 160 | Country must be nullable; founded year is optional |
| Material aliases / origin | 93 / 420; 18 / 420 | No invented synonyms/material classifications |

1,388 / 1,479 (93.85%) have all three nonempty layers; 91 have only flat notes.
There are no duplicate IDs in any of the three files and no dangling perfume house IDs.
There are zero flat-vs-layer set differences among records with a pyramid. These checks do not prove
all note names resolve to material IDs: note links are strings, not declared material foreign keys.
Material-name/alias disambiguation, alias collisions and fuzzy duplicates remain future pilot checks.

JSONL: year is integer/null, popularity_rank integer/null, list fields are arrays, concentration and
secondary_family use empty strings. CSV list fields are semicolon-delimited strings; its descriptor
does not express all canonical constraints. The export has 19 perfume, 8 house and 7 material fields.

## Coverage and bounded sample selection

Designer/Niche are market dimensions; Middle Eastern/Thai/Indonesian are geography. These groups overlap.
Scento types are designer 72, niche 52, heritage 18, arabian 16, artisan 2 houses. Do not map `arabian`
into a canonical market position automatically. Recorded countries include 14 UAE, 1 Oman and 1 Saudi
house, but zero Thailand or Indonesia. There are also two empty countries (Maison Noir and Rihanna).

| Research group | Selected real record / source | Observed shape / gap |
|---|---|---|
| Designer | Scento `dior-jadore`, `dior-hypnotic-poison`, `dior-poison` | First two have flat notes only; Poison has a pyramid; Dior has 31 rows in snapshot |
| Niche | Scento `parfums-de-marly-layton`, `parfums-de-marly-delina` | Layered notes, EDP, nullable year; house has 29 rows |
| Middle Eastern | Scento `lattafa-khamrah`, `lattafa-yara`, `lattafa-asad`; `amouage-reflection-man` | Unknown concentration occurs; Lattafa 23 / Amouage 25 rows |
| Thai | [Butterfly official home](https://www.butterflythaiperfume.com/) and linked Agarwood & Benzoin detail | Home has name/code and THB amount; detail has bottle image but price `n/a`; no pyramid in retrieved detail |
| Indonesian | [HMNS Alpha](https://hmnsperfume.com/products/alpha-100ml), [terms](https://hmnsperfume.com/pages/terms-conditions-revamp) | Page exposes notes, EDP, 100 ml, IDR price, review count, performance claims and images; no reuse consent verified |

Official pages were bounded research reads to identify field shape, not approved extraction feeds.
For HMNS, do not reproduce its product content in seed data: terms reserve reproduction/derivative rights
to prior written consent. Record the page reference and field availability only. A search-discovered
`hmnpure.com` storefront was rejected as an unverified publisher identity; it is not a canonical source.
Thai priority brands La Palette, SCENTERY, BE CHERIE PARFUM and SÚNDALO are present in project requirements,
but no new permissioned sample files for them were supplied. Their product facts remain unverified;
Butterfly is a regional research example, not a substitute for R22 acceptance.

## Duplicate and conflict observations

The sole repeated `(house_id, casefold(name))` group is Balmain / Bleu Infini: two records with IDs
`balmain-bleu-infini` (EDP) and `balmain-bleu-infini-toilette` (EDT). This is an identity collision
candidate, not proof of a duplicate. Preserve both concentration-specific profiles pending review.

Khamrah illustrates a real source conflict: the Scento row uses Mahonial in the heart list; the
[Lattafa page](https://lattafa.com/product/khamrah/) uses Lily Of The Valley in its structured list
and Mahonial in its prose. No equivalence or reformulation is established by that difference.
Its base-note labels also vary in specificity. See [[P1_Data_Conflict_Matrix]].

## Images, evidence and commerce

The Scento export supplies no bottle/note image fields, image licenses, dimensions, byte sizes, volumes,
SKUs, prices, ratings, review text or pairwise evidence. Absence is structural (not zero-valued data).
Materials include notes and accords, but there is no perfume-to-accord weighted join table.
Family and character must not be rebranded as crowd-voted main accords.

| Asset case | Metadata observed | Unknown / restricted |
|---|---|---|
| Butterfly bottle detail | Image link on external `itp1.itopfile.com` host | Creator, license, dimensions, MIME, bytes, hash unknown; no download/hotlink approval |
| HMNS bottle gallery | Multiple image links with product alt labels | Reuse restricted by terms; dimensions/bytes/hash not measured |
| [Commons Local Lemon.jpg](https://commons.wikimedia.org/wiki/File:Local_Lemon.jpg) | Creator Gaurav Dhwaj Khadka; CC BY-SA 4.0; page reports JPEG, 4,032 × 3,024, 4.47 MB | Candidate note illustration only; binary hash/exact bytes/content suitability not verified; no image downloaded |

The Commons example requires attribution, license link and change indication; distribute adapted image
under the required compatible terms. It does not grant rights to any bottle image. Strip private EXIF
from future derivatives and record the transformation. Openverse is an image-discovery service, not a
blanket license grant; verify each upstream file page.

Lattafa exposes an aggregate rating and HMNS a review count, but neither is pairwise similarity evidence.
No reusable comparison-evidence dataset was obtained. Official retail fields are time/locale-specific;
no observed price becomes a default market value. Never infer a price from reward points.

## Limitations and next evidence

This is a convenience sample plus aggregate profiling of one licensed snapshot, not a balanced quality
study across all brands. Official-site grants, priority Thai products, Indonesian import rights,
image bytes, external claim independence and live API response availability remain unresolved.
API docs/OpenAPI were read; one bounded portrait request failed through the web tool, so the live
payload was NOT VERIFIED. Documented response shape is not reported as a successful API test.
All database constraints, ETL tests, performance and restore claims remain NOT RUN.

Next: owner reviews [[P1_Data_Foundation_Plan]], then a merged-plan implementation task uses only
approved samples and records actual validation/benchmark evidence.
