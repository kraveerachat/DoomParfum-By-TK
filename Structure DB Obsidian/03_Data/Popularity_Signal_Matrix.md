---
id: DPT-DATA-POPULARITY-002
project: DoomParfum By TK
type: research_spec
status: proposed
updated: 2026-11-11
timezone: Asia/Bangkok
tags: [doomparfum, dpt-plan-002, planning]
---

# Popularity & Evidence Coverage Matrix — DPT-PLAN-002

## Why and separation
Popularity helps decide **which perfume profiles to research first**. It does NOT measure `scent_similarity`, make a perfume `inspired_by`, prove quality, or grant content rights. Separate `selection_priority`, `evidence_confidence`, `similarity_result`, and source-specific `market_availability`.

| Feature | Minimum evidence | Cohort / pitfalls | Permission |
|---|---|---|---|
| Verified sales | units/revenue, time range, country, channel, publisher | One platform != global market; never infer from reviews | Partner/allowed source only |
| Review count / rating | platform, sample count, scale, snapshot, buyer/spam quality | 4.8/2 != 4.6/2000, not similarity | Source grant needed |
| Video/product views | platform, uniqueness/total, posting age, period | Ads/bot spikes distort, never guess | Approved export/API |
| Search interest | term/topic, geo, query cohort, window | Trends UI 0-100 **relative**, not absolute volume; API alpha separate | Manual reference until grant |
| Awards / mentions | publisher, category, year, criteria | Reader voting != audited sales; no bulk copyrighted text | Citation / licensed aggregate |
| Availability / price | seller, market, size/SKU, checked_at | Store stock != brand production; platform-specific | Approved feed for automation |
| Launch / relevance | official release/edition or pairwise evidence | release year != discontinued; dupe rumor != inspired_by | Exact source evidence |
| Completeness | notes/source/rights coverage, conflict flags | Missing info NULL, not 0 or a negative popularity judgment | Internal QA |

Required metric observation: `source_id,source_page_or_feed,source_record_key,brand_candidate_id,perfume_candidate_key,metric_type,value,unit,scale,geo,platform,period_start,period_end,observed_at,license_or_grant,collection_method,quality_flag,evidence_locator,calculation_version`.
Store raw source-specific observations append-only; display only explicitly permitted fields. Review provenance, period, source cohort, and independent evidence.

## Proposed weights — NOT OWNER APPROVED
Reference discovery: use-case relevance 30%, demand 20%, evidence coverage 20%, availability 15%, diversity 15%.
Alternative discovery: documented reference relation 25%, price/availability 20%, data-and-rights quality 20%, demand 20%, diversity 15%.
Do not compute a score when evidence coverage is insufficient. Separate discovery lanes `mainstream`, `regional`, `emerging`, `niche-small` to avoid popularity monopoly; missing regional sales is not zero market demand.

## Concrete coverage limitations and independent sources
- Google Trends documentation https://support.google.com/trends/answer/4365533 normalizes per geography/time; its 0-100 UI scale is not count. Google Trends API alpha https://developers.google.com/search/blog/2025/07/trends-api has different consistent scaling but current API permission/access has NOT been established.
- Official product pages can show stock/price or labels, but read-only research does NOT authorize scheduled scraping/republishing.
- Fragrantica https://www.fragrantica.com/terms-of-service.phtml forbids unapproved automated extraction and AI/dataset creation; no metric ingestion from it.
- Wikidata structured metadata CC0 https://www.wikidata.org/wiki/Wikidata:Licensing may help identity, not product-popularity or official stock.
No verified `units_sold` or comprehensive rating metric observed in this work; research CSV deliberately leaves the metric table empty.
