---
id: DPT-DAT-008
project: DoomParfum By TK
type: field_mapping
status: draft
owner: project
updated: 2026-11-10
tags: [doomparfum, planning, mapping]
source_of_truth: "../../README.md"
---

# P1 Source-to-Canonical Field Mapping

PROPOSED mapping based on [[P1_Data_Profiling_Findings]], not an implemented importer.
R = required for canonical promotion; O = optional nullable; U = unknown/absent; S = source-specific.
All imported claims additionally require source record, rights assessment, retrieval time and adapter version.

| Source / field | Class | Proposed target / transform |
|---|---|---|
| Scento perfume `id` | R | `source_records.external_key`, never canonical UUID |
| `name`, `house_id`, `house` | R | `perfumes.name`, source-house crosswalk → `brand_id`; compare house label against referenced house |
| `year` | O | `perfumes.release_year smallint`; null stays null |
| `perfumers[]` | O | Source claim `perfumers`; defer normalized perfumer feature until needed |
| `concentration` | O | `perfumes.concentration_code`; dictionary e.g. eau-de-parfum → edp; blank → null; elixir retained as source label until reviewed |
| `family`, `secondary_family` | S | `perfume_families` with scheme `scento`, primary/secondary role; no guessed universal mapping |
| `character[]` | S | `source_observations` field `character`; not weighted accords |
| `seasons[]`, `times_of_day[]` | S | Source observations; reviewed vocabulary → `perfume_usage_tags`; evening is not silently replaced with night |
| `top_notes[]`, `heart_notes[]`, `base_notes[]` | O | `perfume_notes` layer top/heart/base after reviewed material crosswalk; retain order and whole-list provenance |
| `notes[]` | R in source, O canonical | Flat-only rows → layer general; with pyramid, validate set union without duplicating general rows |
| `description` | O | Rights-qualified observation; chosen canonical description with attribution, no AI-added facts |
| `popularity_rank` | S | Observation integer with source snapshot date; not rating/confidence/similarity |
| `url` | R | `source_records.source_url`; it points to Scento, not the underlying brand evidence |
| House `id`, `name` | R | Source key crosswalk and `brands.name` |
| House `country` | O | Reviewed country lookup → `countries.code`; blank stays null; origin is not manufacture |
| House `founded`, `portrait` | O/S | Source observations; keep supplied year/description rights |
| House `type` | S | Source taxonomy observation; arabian is not canonical positioning |
| House `perfume_count` | S | Snapshot count claim, not live count of imported rows |
| House `url` | R | House source record URL |
| Material `id`, `name` | R | Source crosswalk → `notes.id`, `notes.name`; material is an olfactory label, not a chemical disclosure |
| Material `aliases` | O | Split CSV `; `; reviewed `note_aliases`; permit ambiguous aliases across notes |
| Material `material_family`, `origin`, `smell` | O/S | Source-qualified observations; origin natural/synthetic/both/accord does not imply actual formula |
| Material `url` | R | Material source record URL |
| Scento API `folio`, `lede`, `detail`, `scento_page`, `further_reading`, `cite`, `continuation` | S | Documented response envelope only; preserve citation and opaque cursor; no wholesale export through API |
| API `detail.pyramid`, `family`, `subfamily`, `year`, `concentration` | O/S | Proposed adapter contract; live request failed, no verified live payload or claim that subfamily equals export secondary_family |
| Official product title / edition / concentration | O | Research-only until permission; identity candidate must distinguish EDT/EDP, flankers and editions |
| Official size / SKU | O | `product_variants.volume_ml numeric(8,3)`, `sku`; volume is packaging, not a scent identity |
| Official price / currency / locale / observed time | O | `price_observations`; decimal parse follows locale; no THB default for unknown currency |
| Official review count / aggregate stars | S | `rating_observations` with scale/time/source; never pairwise evidence |
| Official longevity / sillage / projection | S | Claims with units/author/source; not measured DoomParfum results |
| Official images / alt labels | O | Source-page references; asset acquisition blocked until image-specific rights |
| Commons creator / license / dimensions / MIME / page | O | `image_assets` research metadata; source page is not object key; exact bytes/hash required only after acquisition |
| User CSV/form | O | No sample supplied; future schema version and per-field rights validation required |

## Required minimum and missing semantics

Canonical catalogue minimum: generated UUID, nonempty name, resolved brand, unique application slug,
review status, and an approved provenance selection for imported fields. Brand country, market tags,
release year, concentration, all note layers, images and commerce data may remain unknown.
Unknown concentration blocks automatic identity merge, not the creation of a clearly incomplete draft.
Matching eligibility is a separate reviewed decision; do not force three notes or an image to save a record.

No Scento fields map to prices, volume, bottle photos, note photos, weighted main accords, rating or
review evidence. These require separate permissioned sources. No user product dataset accompanied this request.

See [[Data_Dictionary_Draft]], [[Data_Quality_and_Provenance]] and [[Rights_and_Attribution]].
