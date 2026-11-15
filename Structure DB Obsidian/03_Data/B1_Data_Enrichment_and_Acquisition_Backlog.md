---
id: B1-DATA-ENRICHMENT-BACKLOG
project: DoomParfum By TK
type: data_enrichment_and_acquisition_preparation
status: prepared-rights-and-implementation-gated
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, data-enrichment, acquisition, source-rights, gaps, independent-workstream]
source_of_truth: "../../README.md"
---

# Current Workstream B — data enrichment and bounded acquisition backlog

This is current independent preparation work, not a task deferred behind synthetic B1 approval.
Human Owner has NOT approved B1 implementation. Agreement with B1's direction does not accept its
exact contract/hash. This lane completes licensed local-source aggregation and prepares separate
permission/mapping decisions without beginning any import, source adapter, normalization or ranking.

Base main604d447e599aa8359d3427dfbfbceaac85373e48 includes Owner-merged M1 PR26. All M1 source/tests,
contract and22receipts/8migrations stay unchanged. [[B1_Parallel_Preparation_Checkpoint]] and its
64artifact/10static checks remain frozen. The checks and research below are new, separate evidence.
The lane adds to [[Incremental_Source_Adapter_and_Media_Intake_Plan]],
[[Source_Acquisition_Permission_Research]] and [[P1_Source_to_Canonical_Mapping]]; it does not
recreate or approve those plans and does not create a second source-index, raw export or runtime.

## Counting contract and exact local denominators

All1479perfume,160house and420material CSV records from the existing licensed local Scento revision
086769ecf1add770ea6646bd4d88d39f0e7cddeb were inspected in place outside public Git. A populated
scalar is a nonempty trimmed source string; a source list uses the publisher's semicolon delimiter.
Only aggregates are written. Source IDs, rows, proposed canonical UUIDs and private queues are not
exported here. Literal/casefold collision counts are diagnostics only; no normalized record is saved.

The resulting18local integrity/count assertions pass. They verify CSV pins/counts, field-count
balance, source identity uniqueness/house referential coverage, shape totals, retained hold manifest
and unchanged source bytes. They are not B1, adapter, ETL, closure or current database tests.

For every table below, populated/missing counts describe the pinned raw CSV only. Current canonical
DB populations, selected-field rights, genuine app access and B1 eligibility are UNKNOWN/NOT QUERIED.
No global/regional universe denominator is known. A raw nonempty pyramid does not prove completeness.

Dataset attribution: Scento — [Scento Perfume Database](https://www.scento.com/perfume-database),
revision086769ecf1add770ea6646bd4d88d39f0e7cddeb, [CC BY4.0](https://creativecommons.org/licenses/by/4.0/).
This note derives aggregate counts and proposed mappings; the original source files remain unchanged.


## Perfume fields — denominator1479

| Raw field | Populated | Missing |
|---|---|---|
| id |1479|0|
| name |1479|0|
| house_id |1479|0|
| house |1479|0|
| year |80|1399|
| perfumers |69|1410|
| concentration |1228|251|
| family |1479|0|
| secondary_family |1075|404|
| character |1479|0|
| seasons |1479|0|
| times_of_day |1479|0|
| top_notes |1388|91|
| heart_notes |1388|91|
| base_notes |1388|91|
| notes |1479|0|
| description |1479|0|
| popularity_rank |613|866|
| url |1479|0|


## House fields — denominator160

| Raw field | Populated | Missing |
|---|---|---|
| id |160|0|
| name |160|0|
| country |158|2|
| founded |97|63|
| type |160|0|
| portrait |160|0|
| perfume_count |160|0|
| url |160|0|


## Material fields — denominator420

| Raw field | Populated | Missing |
|---|---|---|
| id |420|0|
| name |420|0|
| aliases |327|93|
| material_family |420|0|
| origin |402|18|
| smell |420|0|
| url |420|0|


## Identity, layers, aliases and unsupported fields

There are1479unique source perfume IDs and160unique house IDs; all1479house links resolve inside
the pinned source. Explicit edition identity is absent from the schema. Concentration is populated
for1228records and missing251; concentration/name/source ID do not alone prove edition equivalence.
A diagnostic house+casefolded-name grouping has1collision group; adding concentration produces0
collision groups. These are future identity-review candidates, not authority to merge editions.

Raw shapes are1388pyramids with all three layer lists,91flat-only/general records and0partial
pyramids. Top/Heart/Base each have1388populated/91missing rows. The all-notes `notes` column is
populated for all1479records; it is a flat summary for the entire source and is not1479general-only
profiles. The flat-only/general subset has91records/420source token occurrences.

| Source list | Token occurrences | Distinct literal labels | Within-field repeated extras |
|---|---|---|---|
| Top |3850|268|16|
| Heart |3873|296|12|
| Base |4305|207|12|
| Flat all-notes summary |12448|420|177|

These count different representations. The177flat-summary extras do not replace the independently
retained43normalization proposals/44groups/45extras; source cross-layer memberships and ordinals
are untouched. Material aliases are populated327/420, missing93;1635literal alias tokens are all
distinct literally, while casefold diagnostics yield1626distinct tokens and9within-material repeated
extras. No alias collapse, translation, canonical membership change or hold release is performed.

Primary perfume family is populated1479, secondary family1075/missing404. These are source taxonomy
claims, not approved canonical family associations. Material-family420, origin402/missing18 and
smell420 are different fields.190materials carry the source origin label `accord`; this supplies
neither a perfume accord-presence profile nor a numeric accord-strength vector.

| Requested capability | Pinned source coverage / limitation |
|---|---|
| Structured perfume accords/strengths | No perfume accord/presence/strength field exists;0structured profile vectors supplied across1479records. Do not infer strengths from material category, order, duplicates or prose. |
| Explicit editions | No edition/parent-edition field; source IDs/concentration are observations requiring review. |
| Official brand websites | No official-website field; house `url` is source provenance, not an official-brand URL grant. |
| Images and image rights | No asset-binary/per-asset permission/derivative manifest in these CSVs. Source URLs or house portrait prose are not usable images. |
| Dupe evidence | No typed pairwise comparison-evidence field; prose/community links must not become canonical Dupe claims. |
| Seller links/prices | No listing/price/currency/observed-at schema; source popularity rank is not price, sales or availability. |
| Chemical INCI/ingredients | Never map chemical ingredient declarations into perceived Top/Heart/Base/general notes, accords or family. A cosmetic product dataset is useful only after actual perfume identity/brand fields and applicable rights are verified. |

All2059source records have nonempty provenance URL fields. This audit makes0requests to those
product URLs and does not establish URL liveness, active rights, freshness or application access.

## Retained holds and current-vs-historical state

The existing1479-entry review manifest still contains1435 SOURCE_PROMOTABLE_UNDER_MERGED_RULES_NOT_NEW_APPROVAL
and44 PRESERVED_HELD_SOURCE_PROFILE entries. The44held source records comprise40pyramid/4general;
nonheld source records comprise1348pyramid/87general. All1479manifest activation flags remainFalse.
These are stored manifest counts, not a fresh database query or a new promotion/approval decision.
The43unapproved membership proposals and Khamrah's separate conflict remain preserved. Current DB
hold/eligibility counts and real-data B1 eligibility are NOT DETERMINED by this lane.

## Brand/regional priorities — no global completeness claim

Country claims exist for158/160houses;2are empty. Source country claims include France56houses/
485perfumes,United States30/151,Italy24/247,United Kingdom15/133 andUnited Arab Emirates14/302.
There is no source house with the literal country claim Thailand. This is a dataset gap, not proof
that no Thai brand exists. Country of origin is distinct from seller market, stock and app coverage.
The largest source house has189profiles; the next53. Size does not confer identity or source priority.

The retained220-candidate research seed has the following stored suggestion coverage. Suggestions
are research crosswalk hints and are not accepted identity joins or true regional market denominators.

| Research cohort | Candidates | With stored Scento house suggestion | Without stored suggestion |
|---|---|---|---|
| Cambodia |1|0|1|
| China |8|0|8|
| Global |103|82|21|
| Indonesia |16|0|16|
| Japan |8|0|8|
| Malaysia |11|0|11|
| Middle East |31|14|17|
| Philippines |5|0|5|
| Singapore |7|0|7|
| South Korea |9|0|9|
| Thailand |15|1|14|
| Vietnam |6|0|6|

Priority is: exact Thai/regional identity dossiers first; then licensed country/official-identity
mapping, year/concentration gaps, and note/family vocabulary review. Thai15candidates include14
without a stored suggestion; the remaining suggestion is not approval. Indonesia16,Malaysia11,
Vietnam6,Singapore7,Philippines5 andCambodia1all lack stored suggestions. Japan's source country
coverage and the seed's unmatched Japanese candidate names are different populations. No population
percentage is claimed and no new candidate identity or research-source permission is invented.

## Permission dossiers — current research, not acquisition approval

Five official URL opens were attempted:2usable reference pages,1explicit crawler restriction and
2fetch failures, plus1bounded discovery search. No product-data API, catalogue endpoint, image,
feed or sample was requested. These outcomes are separate from the earlier A–G3reference-page reads.

| Source | Read / automation | Storage / display / redistribution | Updates / attribution | Current readiness |
|---|---|---|---|---|
| Existing pinned Scento | Existing local inspection; pinned README confirms the snapshot and semicolon lists. No live API/new-revision request. | CC BY4.0 evidence retained; existing local-pilot use only is the current project scope. Operator/publication row remains separately restricted/unapproved; no application/media grant added. | New revision/scheduled sync needs its own scope. Retain Scento origin,revision,license and change notices. | LICENSE PATH VERIFIED; exact new mapping/reviewer task still pending. |
| Wikidata structured entities | Official documentation identifies structured CC0 data access and responsible interfaces; User-Agent, bounded calls and429/backoff apply. No entity retrieved. | Structured-data reuse path documented; linked article text/logos/images have separate rights. Project identity/source-use and field scope still need approval. | Entity revision must be pinned; no polling approved. CC0 attribution is not required, but project provenance retains origin/revision. | GENERIC LICENSE/ACCESS EVIDENCED; actual brand entities, API field schema and adapter scope unverified. |
| Open Beauty Facts | Data page returned explicit crawler restriction; stopped without alternate route. | Beauty-instance terms and actual perfume identity sample unverified; do not inherit food-instance licenses or grant image reuse. | Update/retention/attribution duties unresolved. | BLOCKED/INSUFFICIENT; not a fragrance-note/accord/family gap-fill source. |
| SIAM1928 first-party export candidate | Retained TH01official terms URL timed out. No permitted feed/API/automation method established. | Exact publisher field/use/audience/export permission unresolved; public product visibility is not an intake grant. | Negotiate revision/cadence/replacement/retention/credit; no request sent. | RIGHTS UNKNOWN; permission/export dossier preparation only. |

Specific primary references: [pinned Scento README](https://raw.githubusercontent.com/Scento-com/perfume-dataset/086769ecf1add770ea6646bd4d88d39f0e7cddeb/README.md)
confirms this snapshot's1479/160/420rows, list delimiter and CC BY4.0 attribution. The separate live
API has its own contract and must not wholesale reconstruct the catalogue. [Wikidata data access](https://www.wikidata.org/wiki/Wikidata:Data_access)
documents CC0structured data and responsible programmatic access; it does not prove any particular
perfume edition/brand match, country or note claim. [Open Beauty Facts data page](https://world.openbeautyfacts.org/data)
returned its crawler restriction, so no deployment-license or sample claim is made. [SIAM1928 terms](https://siam1928.com/term-condition/)
was unavailable during this attempt; prior TH01dossier remains historical. An exploratory PAÑPURI
terms path also failed; one domain search did not establish a product-data reuse license and it is
not selected as a permission-ready adapter. No retry around the OBF access restriction occurred.

## Bounded current acquisition/mapping backlog — all execution gated

These packages extend existing source/intake plans. Each cap is a future review target, not an
executed sample, intake authorization, retention rule or automatic canonical selection.

| Priority / package | Exact proposed mapping and sample cap | Required permission/planning contract | Future acceptance controls — NOT RUN |
|---|---|---|---|
| P0 ENR-PINNED-SCENTO-1 | Existing local2perfume+1house+2material records,max5total. family/secondary_family -> separate unselected taxonomy claims; year/concentration -> typed candidate observations; country -> raw house-origin claim, not automatic ISO; aliases/material_family/origin/smell -> distinct candidate material/alias/description claims. | Accept exact IDs/fields,target claim types/vocabulary, transform version,reviewer,use scope and replay boundary under existing pinned local rights before any mapping runtime. | Raw bytes/ordinals preserved; null/unknown distinctions; alias ambiguity/repeats/edition conflicts/Khamrah stay held; idempotent replay/rollback; no inferred closure/eligibility or source-country-to-market conversion. |
| P1 ENR-WIKIDATA-BRAND-ID-1 | At most5Owner-reviewed brand entities from the existing seed. Proposed entity ID -> external identifier; revision -> source-record revision; language-labelled name -> unselected brand-name/alias observation. Country/website/inception statement property map remains an additional explicit field choice. | Exact entity-match rationale,API/schema/version,field list,request budget(max5entities),cache/use/attribution and permitted audience; applicable Planning/Implementation Gate. | No name-only auto join; conflicting/missing/deprecated statements and unsupported fields retained unknown; pin revision; no linked image fetch, edition merge or inferred real-note completeness. |
| P1 ENR-SIAM1928-FEED-PERMISSION-1 | Prepare request scope for at most5publisher-selected SKUs with exact SKU/edition/concentration,declared layer or explicit general notes,lifecycle/source revision; assets separate. No contact or sample acquisition executed. | Actual publisher export/feed permission for exact methods,fields,storage/display/transform/redistribution/update/retention and audience, then approved bounded adapter task. | Verify publisher authority,edition identity and note-domain semantics; conflicting source sections retained; no chemical ingredient-to-note conversion; original provenance and exact replay/rollback preserved. |
| P2 ENR-HOLD-REVIEW-1 | At most5existing held source records per proposed review unit;43membership projections and independent Khamrah route stay separate. This is reviewer dossier preparation,not ingestion. | Exact reviewer/projection/version/outcome scope; separate closure/selection/materialization and hold/eligibility decisions before any mutation. | Accepted/rejected/unknown/explicit-defer tracked separately; no majority/newest fallback; no automatic release, transform or rewritten original observation. |
| P3 ENR-OBF-IDENTITY-REVIEW-1 | Only if permitted deployment terms and actual perfume records are later verified: at most5identity/barcode/brand/quantity records. Reject candidate if sample lacks relevant perfume identity. | Resolve restriction through a legitimately permitted route/permission,instance-specific licenses and source contract; no bypass or broad dump. | Unknown perfume coverage fails readiness; no mapping INCI to notes/family/accords; database/content/image licenses isolated; no price/availability or scent-data inference. |

No source/asset acquisition, import/ETL runtime, DB or normalization mutation is performed. New
candidate source rights are not authorized by agreement with this backlog. B1 approval is neither
required for this research nor sufficient to authorize these later data tasks. Public UI/API,
redistribution, source images and matching eligibility remain separate gates.

## Deliverable status and next Owner actions

| Deliverable | Actual status | Evidence / next action |
|---|---|---|
| Full pinned local field/brand/note/alias/provenance gap aggregates | DONE |18fresh local assertions and complete aggregate JSON; no raw exports or canonical completeness claims. |
| Four specific source/operation dossiers | PARTIAL | Scento/Wikidata license/access paths evidenced; OBF blocked and SIAMterms unavailable; no new publisher grants or actual product samples. |
| Bounded mapping/acquisition/reviewer backlog | DONE as preparation | Owner chooses exact first independent data package and scope; no adapter implementation approved here. |
| New acquisition/import/promotion | BLOCKED/NOT ATTEMPTED | Requires applicable Planning/Implementation Gate and usable operation-specific permission; does not wait on synthetic B1 but cannot bypass source/data gates. |
| Current canonical DB/rights/app/B1 eligible populations | NOT RUN/UNKNOWN | No DB call or application principal created. Raw1479/160/420counts are not fresh canonical populations. |

Recommended next Owner data action is a separately bounded existing-pinned-field mapping review
(ENR-PINNED-SCENTO-1,max5local records), then an exact Wikidata brand-identity scope if useful. Resolve
regional manufacturer export permission and OBF applicability independently. Keep all44holds and
unselected taxonomy/normalization proposals unchanged. This recommendation approves none of them.

Sanitized aggregate and permission evidence lives under ignored `.local/b1-contract/enrichment/`:
`RAW_FIELD_COVERAGE.json` and `SOURCE_PERMISSION_DOSSIERS.json`. Detailed pinned source and private
review artifacts remain in their original external Local Data locations. Only aggregate counts,
source references and proposed contracts enter this note. M1/B1/scorer,ETL,DB/RLS/replay/recovery,
source-adapter and media tests are NOT RUN. Existing failures and unresolved permissions are retained.

TOOL EXECUTION REPORT: existing Context Mode/Python/read-only Git for full local CSV aggregates;
built-in web for the bounded official-reference attempts/search. No tool/config/account/paid-service
change. New source records/assets/grants/imports/normalizations/hold releases/eligibility changes0;
DB/Docker/service/Git/Handoff mutations0. Only this new note and ignored sanitized aggregates were
written. Parent owns shared status,Owner review summary,ledger and the single consolidated LATEST.
