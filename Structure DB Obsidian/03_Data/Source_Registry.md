---
id: DPT-DAT-003
project: DoomParfum By TK
type: source_registry
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - sources
  - rights
  - registry
source_of_truth: "../../README.md"
---

# Source Registry — P1 Discovery

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
