---
id: DPT-DAT-003
project: DoomParfum By TK
type: source_registry
status: draft
owner: project
updated: 2026-11-11
tags:
  - doomparfum
  - data
  - sources
  - rights
  - registry
source_of_truth: "../../README.md"
---

# Source Registry — P1 Discovery

## Current local pilot source state

Planning PR #1 is owner-merged at `bffb2fab1918dc5221a6c5da7920168bcae263ca`. The external local preparation
package was reverified for IMP-P1-01 (three raw hashes and full 42-entry manifest, exact 12/5/58/93).
No raw dataset is committed or fully imported. Only rollback-only schema shape fixtures are exercised;
actual source capture/import adapter/idempotency work is IMP-P1-02 after owner merge of 01.
CC BY 4.0 attribution and OD-01/06 international scope persist. API/official-site/image grants are not
expanded; Thai/Indonesian imports remain blocked by usable rights AND real samples.


Reviewed 2026-11-10 (Asia/Bangkok). Source status records observed permission scope. Owner OD-01 now approves the pinned Scento CC BY 4.0 export for the local international pilot with attribution; execution waits for Human Owner planning merge. Production/broader source adoption is not approved. Other research reads do not authorize imports. See [[P1_Data_Profiling_Findings]] and [[Decision_Log]].

| ID / owner | Entry point / evidence | Rights and access | Actual execution / decision |
|---|---|---|---|
| SRC-01 Scento dataset | [Repository](https://github.com/Scento-com/perfume-dataset), pinned ref `086769ecf1add770ea6646bd4d88d39f0e7cddeb` | [LICENSE](https://github.com/Scento-com/perfume-dataset/blob/086769ecf1add770ea6646bd4d88d39f0e7cddeb/LICENSE): CC BY 4.0; credit, license link and change indication; no image grant inferred | Read three small data files in temp, aggregate profile and selected examples only; OWNER-APPROVED local seed under OD-01 with attribution; no new import in S3 |
| SRC-02 Scento API | [Docs](https://www.scento.com/developers/perfume-api), [OpenAPI](https://www.scento.com/api/perfume/v1/openapi.json), [terms §22](https://www.scento.com/terms-of-service#perfume-api) | Free anonymous read-only lookup; reasonable cached requests requested; no published numeric quota; no overload/limit bypass/wholesale competing catalogue; code MIT does not license content | Docs/spec/terms read; one portrait fetch failed via web tool. Live API NOT VERIFIED; bounded lookup proposed, bulk import NO-GO through API |
| SRC-03 Butterfly Thai Perfume | [Home](https://www.butterflythaiperfume.com/) and linked Agarwood & Benzoin detail | Copyright notice observed; public reuse/feed grant NOT VERIFIED; robots/automation permission NOT VERIFIED | Bounded page research only; import, image download and automated collection blocked pending grant |
| SRC-04 HMNS | [Alpha](https://hmnsperfume.com/products/alpha-100ml), [terms §7](https://hmnsperfume.com/pages/terms-conditions-revamp) | Content reproduction/distribution/derivatives requires prior written consent; no grant obtained; robots not inspected because no crawler proposed | Field-shape research and source reference only; NO product-text/image seed import; owner may later obtain consent |
| SRC-05 Wikimedia Commons contributor | [Local Lemon.jpg](https://commons.wikimedia.org/wiki/File:Local_Lemon.jpg) | File page states CC BY-SA 4.0, author Gaurav Dhwaj Khadka; per-asset verification required | Metadata-only image candidate, no binary downloaded. Adapted image obligations and suitability review remain |
| SRC-06 Openverse | [API docs](https://docs.openverse.org/api/), [API](https://api.openverse.org/v1/) | Discovery metadata is not an upstream asset grant; rate/auth terms and each result's license must be checked before future acquisition | Docs reviewed, no image API query or asset ingestion run |
| SRC-07 Fragrantica | [Reference entry](https://www.fragrantica.com/designers/) | REFERENCE ONLY / NO AUTOMATION by owner instruction. ToS, caching, storage, AI-use grants NOT VERIFIED in this run | No page extraction, scraping, internal API or Apify actor executed; do not treat as licensed catalogue |
| SRC-08 User input | Future user CSV/form/photos | User-owned content only; screenshot/private possession does not transfer third-party rights; private exports excluded from public Git | No product sample file supplied in this request; rights checked per field/asset before later import |
| SRC-09 Shopee | User-saved public listing links | LINK-ONLY/manual observations within authorized scope; API/automation rights NOT VERIFIED | No account/session access, sync, order placement or scraper |
| SRC-10 TikTok / YouTube / review creators | Future evidence URLs | Per-content permission/terms required for excerpts/transcripts; no blanket reuse grant | No review dataset acquired; no evidence text harvested |
| SRC-11 SAFF & Co. | [Home](https://saffnco.com/) | Public storefront observed; identity/feed/image reuse permission NOT VERIFIED | Discovery only; not an approved extraction source |

The four priority Thai brands in [[Brand_Taxonomy]] remain targets, not verified feeds. No new samples
for La Palette, SCENTERY, BE CHERIE PARFUM or SÚNDALO were acquired. A search result for `hmnpure.com`
was inspected then excluded because publisher identity was not established; never infer an official
source solely from its title. Sources are independent only if underlying claims are independent;
Scento dataset/API are one publisher, not corroboration from two sources.

## Rights record required before another source is enabled

Owner, source URL, content category, license URL/version, terms URL/version or digest, reviewed date,
permitted research/automation/cache/store/display/redistribute/AI uses, attribution, commercial limits,
request caps, retention/deletion obligations, permission proof locator, reviewer and next review date.
Unknown flags fail closed for that use. Robots is an access signal, not a content license.

See [[Rights_and_Attribution]], [[P1_Source_to_Canonical_Mapping]], [[P1_Data_Conflict_Matrix]].


S3 boundary: OD-06 approves an international licensed-data pilot only. Regional imports remain blocked
until usable rights AND samples are verified; no grant is inferred for official-site texts, images or APIs.
OD-04 approves image metadata/rights design, not unlicensed image acquisition. No source acquisition or
runtime ingest is performed during this owner-decision documentation session.


## New DPT-PLAN-002 source acquisition research — 2026-11-11 (RESEARCH ONLY)
See [[Source_Permission_Matrix_DPT_PLAN_002]] and [[Brand_Registry_Research]] for first-party observed samples across 15 brand/publisher presences and permissions-by-use. `official_url` is an identity observation, not `automated_access=true` or store/display/image rights. Terms and rights must be evaluated per source/field/asset. Existing OD-01/OD-06 Scento local-only approval is NOT extended to regional imports. Fragrantica automated acquisition remains prohibited absent written authorization. No new adapter or import created.


## WP-03 source observations and no-auto-reuse boundary (2026-11-11)

Three first-party storefronts were observed as **brand existence/product-type evidence only**:
- SAFF & Co. official pages https://saffnco.com/ and https://saffnco.com/collections/shop-all ; perfumes are mixed with other kinds of items.
- Scent Journer https://scentjourner.com/ ; named Eau de Parfum products and region-specific shipping policy.
- Szindore https://szindore.com/ and https://szindore.com/shop/ ; mixed fragrance, toiletries, promotions, merchandise and air-freshener products. Storefront result counts are not counts of distinct perfume identities.

For each source: `official_presence_observed=YES`; automated page access / caching / storage / display / redistribution / commercial content reuse / AI dataset and all media asset rights = `UNKNOWN_NOT_APPROVED`. No per-source permission escalated. No external adapter or asset download performed.

The **pinned licensed Scento** read-only full snapshot counts are now documented in [[Pinned_Scento_Full_Snapshot_Audit_2026-11-11]] (1,479 perfume rows, 160 houses, 420 materials, 1,388 reported full pyramids); this does NOT assert 1,479 local database imports. This source audit does not change published third-party source permission statuses.

## IMP-P1-02 later execution evidence — 2026-11-11

The historical read-only audit above is preserved. Subsequent approved pinned CC BY4.0 private-local
intake now verified1479 catalogue identities/1435 exact-source approved/44 held and zero-growth replay.
Six artifacts include LICENSE/descriptor; claims/captures bind file hashes/logical CSV record ordinals.
Attribution: Scento — https://www.scento.com/perfume-database ; https://creativecommons.org/licenses/by/4.0/ .
Data transformations are local exact transcription/normalization, not new publisher claims. Full raw
files and research queues stay external; source image URLs grant no image rights. No regional/official
site/source automation permission is expanded. [[IMP-P1-02_Licensed_Scento_Evidence]] records tests/limits.

## Post-PR5 permission research — 2026-11-12

[[Post_PR5_Held_and_Permission_Review]] records3new factual locators for6existingbrandcandidates and
5additional Commonsnote-illustrationcandidates, exactcreator/license/subjectqueueexternal. Total12/46
RESEARCHlabelcandidates;0bytes/displayapprovals/bottlegrants. Officialpresence/websiteoperator doesnot
approve canonicalparentidentity or automatedreuse. The third-party-derived description-preference
dataset opportunity wasrejected;0new usablepairwiseevidence. All44Scentoholds persist. No permission
flag, originalsourceclaim, rawdataset or ownerdecision ischangedbythis researchPR.


## Bounded illustration queue increment — 2026-11-12

[[Bounded_Note_Media_Candidate_Increment]] records3additional public file-page metadata candidates.
Proposed queue15/46historicalRESEARCHlabels only; allper-use statesUNKNOWN_NOT_APPROVED_BLOCKED.
All3JPEG are unsupported by currentPR6;2reportedpixelcounts exceed itsbound;3immutablepins
NOT_VERIFIED. No sourcegrant/assetbytes/displayapproval or acquisition authorization. Old12queue
records remain unchanged; all44holds and pairwise/source evidence boundaries preserved.
