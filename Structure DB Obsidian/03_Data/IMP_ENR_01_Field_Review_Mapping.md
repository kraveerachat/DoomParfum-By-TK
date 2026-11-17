---
id: IMP-ENR-01-FIELD-MAP
project: DoomParfum By TK
type: implementation_field_review_mapping
status: LOCAL VERIFIED
owner: human-owner
updated: 2026-11-17
tags: [doomparfum, scento, offline-preview, provenance]
source_of_truth: "../../README.md"
---

# Exact five-record / 46-slot review mapping

Exact ENR-PINNED-SCENTO-1 revision1 and A/B/I authority remain frozen in [[Post_PR27_Data_Readiness_and_Pilot]] / [[Post_PR27_Owner_Decision_Packet]]; dated acceptance is in [[IMP-ENR-01_Pinned_Scento_Offline_Preview]]. This note records implementation evidence, not new SQL field definitions or canonical truth. Source artifacts are the exact six pins, total905307bytes; source populations1479/160/420 are not canonical DB counts.

Identity is `(source revision, file SHA256, logical ordinal, source key, field locator, transform version, schema version)`. Source key is not a canonical UUID. Exact manifest order is two perfumes, house, mint, bergamot; field order follows the approved13/6/7 allowlists. Every field remains unselected/unmapped, closure UNKNOWN, reviewer outcome UNKNOWN and reviewed_at null in the private payload. No source capture/review time is inferred. Semicolon raw slices retain spaces, order and repeats; layer/general and aliases stay separate. Blank raw source means MISSING/null with no known-empty/zero/false inference; nonempty values are literal unverified claims, not automatically parsed dates/numbers/taxonomy.

The independent literal/provenance comparison matched46/46; semantic dossier43DEFER/3UNKNOWN and Human/canonical acceptance PENDING. Three actual missing fields are perfume years at644/645 and house founded at3. Selected concentration/aliases are present; missing concentration/alias and repeated-list controls are synthetic. General/layer equality in these two samples does not authorize derivation or closure. Material aliases/categories never become accepted equivalents/accord strengths.

| Source file | Source key | Logical ordinal | Field locator | Raw source state | Literal/provenance | Semantic dossier |
|---|---|---:|---|---|---|---|
| perfumes.csv | afnan-9-am | 644 | id | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | name | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | house_id | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | house | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | year | MISSING | MATCH / MATCH | UNKNOWN |
| perfumes.csv | afnan-9-am | 644 | concentration | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | family | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | secondary_family | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | top_notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | heart_notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | base_notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am | 644 | url | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | id | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | name | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | house_id | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | house | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | year | MISSING | MATCH / MATCH | UNKNOWN |
| perfumes.csv | afnan-9-am-dive | 645 | concentration | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | family | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | secondary_family | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | top_notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | heart_notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | base_notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | notes | PRESENT | MATCH / MATCH | DEFER |
| perfumes.csv | afnan-9-am-dive | 645 | url | PRESENT | MATCH / MATCH | DEFER |
| houses.csv | afnan | 3 | id | PRESENT | MATCH / MATCH | DEFER |
| houses.csv | afnan | 3 | name | PRESENT | MATCH / MATCH | DEFER |
| houses.csv | afnan | 3 | country | PRESENT | MATCH / MATCH | DEFER |
| houses.csv | afnan | 3 | founded | MISSING | MATCH / MATCH | UNKNOWN |
| houses.csv | afnan | 3 | type | PRESENT | MATCH / MATCH | DEFER |
| houses.csv | afnan | 3 | url | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | mint | 257 | id | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | mint | 257 | name | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | mint | 257 | aliases | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | mint | 257 | material_family | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | mint | 257 | origin | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | mint | 257 | smell | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | mint | 257 | url | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | bergamot | 46 | id | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | bergamot | 46 | name | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | bergamot | 46 | aliases | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | bergamot | 46 | material_family | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | bergamot | 46 | origin | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | bergamot | 46 | smell | PRESENT | MATCH / MATCH | DEFER |
| materials.csv | bergamot | 46 | url | PRESENT | MATCH / MATCH | DEFER |

Private payload33953bytes SHA256 `16d1d1af8a875d342756b4431da0844eef65787d81de130372250d9a0a387cf9`. No raw field literals, complete rows or private tokens are published here. [[IMP_ENR_01_Independent_Data_Review]] supplies independently bound outcomes; [[IMP_ENR_01_Private_Publication.json]] supplies sanitized local publication metadata. CSV extra fields remain excluded; no sixth record or linked expansion.
