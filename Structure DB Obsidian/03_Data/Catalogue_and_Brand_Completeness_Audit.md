---
id: DPT-DATA-005-CATALOGUE-AUDIT
project: DoomParfum By TK
type: observed_data_audit
status: scoped-review-ready
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, catalogue, brands, completeness, audit]
source_of_truth: "../../README.md"
---

# Observed catalogue and brand completeness audit

This is an observed audit at main `8c6a8376680c7a10cc3eb4b5cf80afe4376a9282`, not a new generic
planning specification. Three coordinator READ ONLY queries were captured at 2026-11-13
20:04:07Z–20:04:20Z (2026-11-14 Bangkok). All 49 data/security/application-role fingerprints agree
before/after and with the preceding baseline. This lane made **zero database/network calls**.
It independently checked pinned local files, dictionaries, research matrices and source counts.

The Owner confirmed the conservative high-level direction in the current Master Prompt. Exact
DM/OP formulas, closure/normalization, source/media permissions, identity changes and application
stack remain unresolved; this audit accepts none. Names/counts below do not authorize acquisition,
canonical promotion, public redistribution or real matching. Private row-level registers stay local.

## Catalogue_Coverage_Matrix

| Bounded population | Denominator | Observed populated | Missing / unresolved within that population |
|---|---|---|---|
| Pinned perfumes.csv source IDs | 1,479 file rows | 1,479 distinct IDs | 0 duplicate IDs; no live/global inventory denominator |
| Canonical operator perfume identities | 1,479 database profiles | 1,479 distinct UUIDs, names and same-scope brand links | 44 held; 0 application-bound or matching-eligible profiles |
| Source-exact review state | 1,479 profiles | 1,435 approved | 44 held/draft; approval is not completeness/eligibility |
| Canonical brand identities | 160 brands | 160 UUIDs/names, all approved | 160 country-code and official-website gaps |
| Canonical note identities | 420 notes | 420 UUIDs/names, all approved | 3 without canonical memberships; Thai/aliases/descriptions/images absent |
| Source provenance | 2,059 source records | 2,059 locators/revisions and active local storage/display/automation assessments | 0 missing locator/revision in this audit; no new source rights |
| Selections / observations | Separate record units | 8,845 selections / 10,489 observations | these are not profile counts or blanket use permission |
| Product variants / images / accords / families / pairs / listings / prices | Individual table populations | 0 records in each audited canonical population | perfume-level coverage gaps remain 1,479; an empty table is not proof of worldwide absence |

All 160 pinned house perfume_count declarations equal their actual per-house CSV row counts;
both sums are 1,479. This proves **internal snapshot count coherence**, not current per-brand or
worldwide completeness. Current SQL source captures also cover 1,479 distinct perfume captures.
No per-ID database export was taken, so fresh count agreement is not presented as a new exported
identity-set proof. Historical import/replay evidence remains separate.

The older local source index contains all 1,479 source_external_key values, but source_id denotes
one source, not a perfume. Both canonical_* ID columns are blank in all 1,479 index rows and every
index review_status is needs_review. This is a historical staging index, not the current database
review state (1,435/44), a broken UUID crosswalk, or a live application search index.

## Field_Completeness_Report

The following explicit columns keep units separate:

- D: entity denominator; C/M: canonical populated/missing; R: raw source populated, not reviewed.
- S: approved selected populated; H: populated held profiles, not all held profiles. For perfume
  rows the held cohort is 44 and held-missing = 44 minus H. Brand held cohort is 0.
- L: approved selected values passing the measured active local-use checks; **not application or
  publication permission**. All 2,059 source records separately have active local assessments.
- A: operational application-accessible values, 0 because no approved genuine application binding.
- U: canonical target slots without usable selected value, conservatively D minus S. This is not
  factual absence. Complete-domain/absence uncertainty remains separate even for populated notes.
- NC: no dedicated source column; NM: not separately modeled/materialized; NA: inapplicable unit.
  Neither NC nor NM is a zero observation.

| Perfume/brand field | D | C | M | R | S | H | L | A | U |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| Perfume name | 1479 | 1479 | 0 | 1479 | 1435 | 44 | 1435 | 0 | 44 |
| Perfume brand relation | 1479 | 1479 | 0 | 1479 | 1435 | 44 | 1435 | 0 | 44 |
| Brand name | 160 | 160 | 0 | 160 | 160 | 0 | 160 | 0 | 0 |
| Brand country_code | 160 | 0 | 160 | 158 country labels | 0 | 0 | 0 | 0 | 160 |
| Brand official website | 160 | 0 | 160 | NC official website | 0 | 0 | 0 | 0 | 160 |
| Concentration | 1479 | 1228 | 251 | 1228 | 1188 | 40 | 1188 | 0 | 291 |
| Release year | 1479 | 80 | 1399 | 80 | 76 | 4 | 76 | 0 | 1403 |
| Edition label | 1479 | 0 | 1479 | NC | 0 | 0 | 0 | 0 | 1479 |
| Description | 1479 | 0 | 1479 | 1479 | 0 | 0 | 0 | 0 | 1479 |
| Gender/target label | 1479 | 0 | 1479 | NC dedicated gender | 0 | 0 | 0 | 0 | 1479 |
| Family association | 1479 | 0 | 1479 | 1479 primary;1075 secondary | 0 | 0 | 0 | 0 | 1479 |
| Accord presence | 1479 | 0 | 1479 | NC structured accord | 0 | 0 | 0 | 0 | 1479 |
| Accord strength | 1479 | 0 | 1479 | NC measured strength | 0 | 0 | 0 | 0 | 1479 |
| Top membership | 1479 | 1348 | 131 | 1388 | 1348 | 0 | 1348 | 0 | 131 |
| Heart membership | 1479 | 1348 | 131 | 1388 | 1348 | 0 | 1348 | 0 | 131 |
| Base membership | 1479 | 1348 | 131 | 1388 | 1348 | 0 | 1348 | 0 | 131 |
| General membership | 1479 | 87 | 1392 | 1479 flat strings;91 flat-only profiles | 87 | 0 | 87 | 0 | 1392 |
| Bottle image link | 1479 | 0 | 1479 | NC bottle asset | 0 | 0 | 0 | 0 | 1479 |
| Price observation coverage | 1479 | 0 | 1479 | NC | 0 | 0 | 0 | 0 | 1479 |
| Seller listing coverage | 1479 | 0 | 1479 | NC | 0 | 0 | 0 | 0 | 1479 |

General membership is intentionally a separate representation for flat-only profiles. The 1,479
raw flat strings often repeat the pyramid; they must not all become general-layer links. A note
row's C/M counts do not establish complete-as-reported closure or strict negative-query semantics.

| Additional required field | D | Canonical populated / missing | Raw populated | Approved selected | Held population | Usable canonical local / app | Unknown target |
|---|---:|---|---|---:|---|---|---:|
| Perfume UUID / source identity | 1479 | 1479 / 0 UUIDs | 1479 source IDs | NA identity key | 44 | identity visibility separate / 0 | edition equivalence 1479 |
| Perfume name aliases | 1479 | NM separate perfume-alias model | NC | 0 recorded selection | 44 | not established / 0 | 1479 |
| Flanker relation | 1479 | modeled as directed perfume_relations.flanker_of;0/1479 linked profiles | NC | 0 recorded selection | 44 | 0 /0 | 1479 |
| Reformulation lineage | 1479 | NM explicit lineage model | NC | 0 recorded selection | 44 | not established / 0 | 1479 |
| Discontinued / stock / historical-current status | 1479 | NM explicit lifecycle/stock field | NC | 0 recorded selection | 44 | not established / 0 | 1479 |
| Product variant association | 1479 perfumes | 0 /1479 linked profiles;variant table D=0 | NC | 0 | 44 | 0 /0 | 1479 |
| Size / SKU / GTIN / packaging | 0 existing variants;1479 profile coverage | 0 observed variants;per-variant percentage NA | NC each | 0 | NA variant cohort | 0 /0 | 1479 profiles |
| Occasion association | 1479 | 0 /1479 usage-tag profiles | NC exact occasion | 0 | 44 | 0 /0 | 1479 |
| Season association | 1479 | 0 /1479 usage-tag profiles | 1479 seasons strings | 0 | 44 | 0 /0 | 1479 |
| Day/night association | 1479 | 0 /1479 usage-tag profiles | 1479 times_of_day strings | 0 | 44 | 0 /0 | 1479 |
| Perfumers | 1479 | NM separately materialized perfumer relation | 69 | 0 | 44 | not established /0 | 1479 canonical targets |
| Character | 1479 | NM separately materialized character field | 1479 | 0 | 44 | not established /0 | 1479 canonical targets |
| Popularity rank | 1479 | NM separately materialized rank | 613 | 0 | 44 | not established /0 | 1479 canonical targets |
| Dupe/pair evidence | 1479 profile coverage;0 evidence rows | 0 /1479 covered profiles | NC independent pair evidence | 0 | 44 | 0 /0 | 1479 profiles |

The schema explicitly supports directed flanker_of relationships, but the observed relation table
is empty. Lifecycle, perfumer and reformulation mappings are not separately established. No meaning
is inferred from a name suffix, prose or release year. EDT
(221 raw profiles), EDP (874), extrait (55), parfum (55), cologne (14), elixir (9) and unknown (251)
remain distinct source labels; no equivalence is approved.

## Raw_vs_Canonical_Field_Matrix

All 34 source columns were independently counted and matched against the fresh aggregate. The
following groups account for all columns; a populated source cell is still not a selected fact.

| File and exact fields | Raw populated / row denominator | Current canonical/selection disposition |
|---|---|---|
| perfumes: id,name,house_id,house,url | each1479/1479 | IDs/names/brand link/provenance exist;selected name/brand1435;URL is source provenance |
| perfumes: concentration,year | 1228/1479;80/1479 | canonical1228/80,selected1188/76 |
| perfumes: family,secondary_family | 1479/1479;1075/1479 | canonical family associations0;all raw labels retained,not zero raw family information |
| perfumes: character,seasons,times_of_day,description | each1479/1479 | no corresponding selected values;usage tags0;description column empty |
| perfumes: perfumers,popularity_rank | 69/1479;613/1479 | source-only/unselected;rank is not sales or sensory evidence |
| perfumes: top_notes,heart_notes,base_notes | each1388/1479 | selected each1348profiles;see pyramid audit |
| perfumes: notes | 1479/1479 | flat occurrence evidence,not1479general domains |
| houses: id,name,perfume_count,type,portrait,url | each160/160 | brand names160;other metadata/provenance not approved positioning,website or image |
| houses: country,founded | 158/160;97/160 | country_code0;founded contract exists butnot materialized/selected |
| materials: id,name,material_family,smell,url | each420/420 | note name420;taxonomy/smell raw-only,source URL provenance |
| materials: aliases,origin | 327/420;402/420 | canonical note_aliases0;typed material_origin0;raw origin is not that enum |

All 160 houses.url values point to Scento. They are **not official brand websites**. All 160
portrait cells are populated prose and none is HTTP-URL-shaped; they are not acquired images or
image permission. Actual canonical image/asset-permission counts remain 0.

## Brand_Coverage_Matrix

| Brand target field | D | Canonical populated / missing | Raw source population | Approved selected | Held | Usable local / app | Unknown target |
|---|---:|---|---|---:|---:|---|---:|
| UUID | 160 | 160 /0 | 160 IDs | NA key | 0 | identity scope separate /0 | full identity equivalence160 |
| Display name | 160 | 160 /0 | 160 | 160 | 0 | 160 /0 | 0 source-name slots |
| Aliases | 160 | 0 /160 with aliases | NC in houses | 0 | 0 | 0 /0 | 160 |
| Country code | 160 | 0 /160 | 158 source labels | 0 | 0 | 0 /0 | 160 |
| Positioning tags | 160 | 0 /160 with tags | 160 raw type claims | 0 | 0 | 0 /0 | 160 |
| Parent house relationship | 160 | NM explicit parent model | NC | 0 | 0 | not established /0 | 160 |
| Official website | 160 | 0 /160 | NC;160 source URLs are not official sites | 0 | 0 | 0 /0 | 160 |
| Founded / publisher perfume_count / portrait | 160 each | NM dedicated columns;0 selected | 97 /160 /160 | 0 each | 0 | not established /0 | 160 each canonical target |
| Review state | 160 | 160 approved /0 draft | source record is not identity verification | NA review metadata | 0 | not an app grant /0 | research identity decisions unresolved |

The separate research universe is **220 seed candidates +6 new candidates =226**, not226 canonical
brands. The 220 seed has 26 official-presence observations, 1 alias-pending official observation,
191 needs_review and 2 third-party-only records; all220 source_rights_status values remain
permission_pending. Only7 seed origin-country cells are populated; seed alias and parent columns
are blank. Those counts describe that historical registry, not current canonical facts.

New offline strict NFKC+lower literal primary/alias comparison yields 92 suggested candidates and
134 without a suggestion across226 candidates;92 distinct houses are suggested and68 of160 houses
have no strict suggestion. No identity, alias, origin, parent or rights approval is made. Earlier
97 suggestions/63 unmatched houses belong to a different historical crosswalk; they are not silently
substituted for this predicate. Candidate row details/URLs remain in the ignored local register.

## Perfume_Identity_Gap_Register

| Identity question | Actual bounded observation | Remaining unknown / limitation |
|---|---|---|
| Missing UUID/name/brand FK | 0/1479 UUID/name/same-scope-brand gaps | source transcription does not settle edition equivalence |
| Concentration | 1228/1479 populated;251 missing;40populated held | 291 lack approved selected concentration |
| Year | 80/1479 populated;1399 missing;4populated held | 1403 lack approved selected year;year is not stock/currentness |
| Edition/flanker/reformulation | no dedicated raw columns;edition_label empty1479;modeled flanker_of has0rows | all1479 require separate exact-edition/flanker evidence;reformulation lineage not separately established |
| Variant/size/SKU/GTIN | product_variants0 | no declared total SKU/edition/size universe;1479 lack variant association |
| Candidate collisions | SQL groups0/profiles0 | exact predicate only: brand_id,lower(btrim(name)),coalesce(lower(btrim(concentration_code)),'');not full Unicode casefold or fuzzy identity approval |
| Source index linkage | external keys1479 exactly equal pinned IDs | canonical_* columns blank1479 and needs_review1479 are historical index state,not UUID mismatch or current DB state |

The private local gap register has1,479 source rows. It is not copied to public Git/ZIP. Zero
collision groups under this predicate does not rule out alternate names, revised editions or
cross-source duplicates and authorizes no merge.

## Regional_Source_Coverage_Report

Seed region is a research prioritization label, not verified country or product availability.
All rows below use **the220 seed cohort**; the6 new discoveries remain a separate cohort.

| Seed region | Seed candidates | Strict suggestions | No strict suggestion | Identity approvals |
|---|---:|---:|---:|---:|
| Global | 103 | 77 | 26 | 0 |
| Middle East | 31 | 14 | 17 | 0 |
| Indonesia | 16 | 0 | 16 | 0 |
| Thailand | 15 | 1 | 14 | 0 |
| Malaysia | 11 | 0 | 11 | 0 |
| South Korea | 9 | 0 | 9 | 0 |
| Japan | 8 | 0 | 8 | 0 |
| China | 8 | 0 | 8 | 0 |
| Singapore | 7 | 0 | 7 | 0 |
| Vietnam | 6 | 0 | 6 | 0 |
| Philippines | 5 | 0 | 5 | 0 |
| Cambodia | 1 | 0 | 1 | 0 |

All15 Thai seed entries retain A priority: MITH, SIAM 1928, PROAD, SÚNDALO, BOROM, Journal Boutique,
Pañpuri, Parfums Dusita, Parfum Prissana, Butterfly Thai Perfume, La Palette, SCENTERY,
BE CHERIE PARFUM, Copenn and The OBA. A literal suggestion does not confirm Thai origin or complete
brand catalogue coverage. New6 candidates remain Strangers Parfumerie, PRIN, VOYAGER, Auphorie,
P.Seven and Anatole Lebreton; none is silently added to the220 denominator or canonically approved.

The160 source houses have158 populated country claims covering17 nonempty labels: France56,
United States30, Italy24, United Kingdom15, UAE14, Germany4, Japan/Sweden/Spain/Switzerland2 each,
India/Oman/Saudi Arabia/Lebanon/Turkey/Netherlands/Canada1 each, and2 unknown. These are source
claims; canonical country_code remains0. Raw house types: designer72,niche52,heritage18,arabian16,
artisan2; those are not approved positioning tags. Regional market, all-brand, live catalogue,
edition and global denominators are UNKNOWN; no worldwide completion percentage is calculated.

## Prioritized_Data_Enrichment_Backlog

| Priority | Observed gap / exact bounded target | Safe next action / dependent gate |
|---|---|---|
| P0 | application access0 despite1435approved profiles | settle exact genuine nonadmin route and source/field/use gates;no administrator fetch-and-filter |
| P0 | 44holds,43projections,Khamrah independent;matching0 | review exact lineage/normalization/closure decisions;no automatic promotion |
| P1 |15Thai A seed entries,14without literal suggestion | permissioned exact-brand/edition/source dossiers first;source access and reuse grants before intake |
| P1 | descriptions1479raw/0canonical;families1479+1075raw/0canonical | review field mapping/taxonomy/rights before bounded materialization;retain originals |
| P1 | brand country158raw/0canonical;official websites0 | verify origins and genuine first-party URLs separately;sourceURL/portrait are not substitutes |
| P1 | note Thai/aliases/descriptions/images0;327raw alias records | reviewed language/alias/material mapping and per-asset grants;placeholders until approved |
| P2 |251concentration gaps;1399year gaps;edition details unknown1479 | obtain permissioned exact-edition samples;do not infer from names or merge EDT/EDP |
| P2 | variants/SKU/GTIN/size0associations;no bounded SKU universe | source-specific identifier/edition inventory with exact rights;no invented totals |
| P2 | canonical accords/pair evidence0 | compatible reviewed accord inputs and independent permissioned pair claims;no fabricated intensity/Dupes |
| P2 | listings/prices/currentness0;no live market denominator | approved private manual/source-specific observation contract;no scraping or automatic cart sync |

[[Note_Vocabulary_and_Field_Readiness_Audit]] contains the six note/domain reports.
[[DPT-DATA-005_Audit_Evidence]] records exact hashes/checks and the preserved index-column checker
error. No enrichment, normalization, source permission, SQL/runtime or production change occurred.
