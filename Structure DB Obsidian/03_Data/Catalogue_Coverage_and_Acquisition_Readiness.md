---
id: DPT-PLAN-006-COVERAGE
project: DoomParfum By TK
type: data_readiness
status: research-only
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, coverage, provenance, workstream-g]
source_of_truth: "../../README.md"
---

# Catalogue coverage and acquisition readiness

## Actual read-only evidence and counting rules

Main58ceafe72129b70f0333c7c4f2c6f38dba855272; G consumes WorkstreamD's separately leased operator
aggregate audit. Core counts as of2026-11-13T08:09:30.147499Z; corrected family/note/raw-shape
supplement as of2026-11-13T08:17:53.752609Z. Both transactions READ ONLY / REPEATABLE READ;
all49table,security and application-role fingerprints unchanged. This is an inventory audit, not
proof that a genuine application user can access this operator-owned catalogue. No database change.

Denominator is1479existing private perfumes unless explicitly160brands or420notes. Populated means
canonical field/link nonempty; missing means not populated in this local canonical model. Held is
an intersecting review-state subset, not an extra denominator. All44held profiles are unapproved;
all1435other profiles are source-exact-approved. A present, selected field with active local
storage/display/automation rights is still not an accepted complete domain or app matching input.
Actual nonadmin runtime-owner-bound profiles0 and matching eligibility0: all1479are unavailable
for real application matching under current gates. Unknown global/regional universes are not0.

## Canonical population, holds and selected local uses

| Field | Denominator | Populated | Missing | Populated approved | Populated held | Missing held | Selected present + active local uses |
|---|---:|---:|---:|---:|---:|---:|---:|
| accord_presence | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| accord_strength | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| bottle_image_link | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| brand.country_code | 160 | 0 | 160 | 0 | 0 | 0 | 0 |
| brand_id | 1479 | 1479 | 0 | 1435 | 44 | 0 | 1435 |
| brand.name | 160 | 160 | 0 | 160 | 0 | 0 | 160 |
| brand.website_url | 160 | 0 | 160 | 0 | 0 | 0 | 0 |
| concentration_code | 1479 | 1228 | 251 | 1188 | 40 | 4 | 1188 |
| description | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| edition_label | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| family | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| gender_label | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| name | 1479 | 1479 | 0 | 1435 | 44 | 0 | 1435 |
| notes.base | 1479 | 1348 | 131 | 1348 | 0 | 44 | 1348 |
| notes.general | 1479 | 87 | 1392 | 87 | 0 | 44 | 87 |
| notes.heart | 1479 | 1348 | 131 | 1348 | 0 | 44 | 1348 |
| notes.top | 1479 | 1348 | 131 | 1348 | 0 | 44 | 1348 |
| price | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| release_year | 1479 | 80 | 1399 | 76 | 4 | 40 | 76 |
| seller_listing | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |

Every perfume-field row has44unapproved entities irrespective of whether that field is populated.
Brand rows have0unapproved entities. All420canonical notes are approved; usable note images0,
missing note images420. There are160brands with selected names and1479perfume-brand links;
country_code and website_url0/160canonical, even though the raw house file contains country claims.
Variants0: editions/volumes/GTIN completeness is unknown, not a claim that all1479products have no
editions. Edition label0/1479means absent from the canonical snapshot, not a resolved identity rule.

| Note layer | Profiles with canonical membership | Links | Missing profiles |
|---|---:|---:|---:|
| top | 1348 | 3693 | 131 |
| base | 1348 | 4150 | 131 |
| heart | 1348 | 3742 | 131 |
| general | 87 | 387 | 1392 |

Total note links11972. The same1348approved profiles have layered top/heart/base memberships;
87approved profiles have general memberships.91flat profiles is a source-shape cohort, not87
selected approved flat profiles:4flat profiles remain among44holds. All44held notes are unselected.
Raw arrays/prose remain immutable, including duplicate occurrences. A nonempty pyramid or selected
field never proves accepted note-list closure or absence. No accord strengths are inferred.

## Provenance, rights and unavailable application features

Inventory: source1,rights1,source_records2059,observations10489,selections8845; pending validation0.
All2059source captures have locators/revisions and active local storage/display/automation rights.
The one current rights row allows local research,automation,storage,display,cache; redistribution
is restricted and AI use unknown.0expired/0revoked/0future-checked/0missing-evidence rights rows
at the core audit time. These are current database facts, not a newly granted license or accepted
cache/API/publication policy. Source license capability and current recorded project rights differ.

Accord entities/links0,family entities/links0,bottle assets0,note assets0,asset permissions0,
relationships0,comparison_evidence0,retail listings0,prices0. Thus1479/1479perfumes currently have
no canonical accord/family/bottle/pair/listing/price support; all420notes have no usable image.
There are0canonical Dupe/alternative-to claims. The5offline pair candidates and15media candidates
are not database facts or permissions; they remain unreviewed/blocked. No public or shared profiles:
all1479are user_private. Private source data cannot become public through a public catalogue link.

Canonical lifecycle, market/stock support is unavailable; the pinned perfume capture has no
dedicated lifecycle/stock/market/edition_label/price/bottle-image key. This describes the capture
schema only. It does not prove real-world absence or permission to obtain those fields elsewhere.
Country origin is not seller market, stock, currentness or regional catalogue completeness.

## Raw available claims versus approved mappings

Raw perfume captures1479; nonempty top/heart/base1388each, general1479(overlapping publisher fields,
not disjoint canonical layer counts), family1479,secondary_family1075,description1479,year80,
concentration1228,perfumers69,popularity_rank613,seasons1479,character1479,times_of_day1479.
Family/description and these other unmapped raw claims are not automatically approved/selected.
Raw houses160:158nonempty country claims,2missing,17distinct publisher country labels. Canonical
country_code0does not mean raw countries absent. Global brands, Thai/regional perfume universes,
missing edition counts and licensed-image universe are NOT ESTABLISHED; no completeness percentage.

## Audit corrections and preserved failures

V1used an incorrect brand:staging prefix and produced invalid raw-country0; retained, not an absence
claim. V2corrected the source_file=houses.csv denominator but queried families instead of actual
family for the selected-contract label. V3uses family/families.primary/families.secondary: contract
exists, selected0; canonical family0never changed. An audit-only supplement query first failed42601
fromGROUP BY1syntax; its spacing was corrected, failure retained, no product/runtime/schema change.
Final V3projection is authoritative. No new raw rows, SQL or audit runner is committed by this plan.

Public aggregate summary SHA256: 961a2a23ccf6379209fb037190f614eb250c483741cc91b13ef213db79a38b19.
Core SQL SHA256:8b36ea19bc10f9bb7784da2635cbaf1f68dcf21877d52ebd44be68358865bf50.
Supplement SQL SHA256:b62c466843d6c01926838cc800b132e905c542836c8d4c25803d0067b3c7ce97.
Exact ignored runners, originalV1/V2/V3reports and failure logs remain local; public documents and
the handoff carry only sanitized aggregates and provenance. Source record values/private table
fingerprints are excluded. Independent query/count-definition review is still required before
claiming this Planning PR review-ready.

## Readiness judgment

Enough verified licensed data exists for bounded local source-exact inspection and approved offline
research. The intended application is NOT data/media ready: real A/B1eligibility0; B2strengths0;
usable media0; lifecycle/edition/regional/pair/listing gaps remain. Next authorize exact decisions
and a small permissioned source/sample task through [[Incremental_Source_Adapter_and_Media_Intake_Plan]];
candidate terms are in [[Source_Acquisition_Permission_Research]]. Do not promote holds, raw family
claims, source neighbours or unlicensed images to improve a coverage number.
