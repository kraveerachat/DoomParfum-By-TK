---
id: DPT-DATA-REGISTRY-002
project: DoomParfum By TK
type: brand_research
status: research
updated: 2026-11-11
timezone: Asia/Bangkok
tags: [doomparfum, dpt-plan-002, planning]
---

# Brand Registry Research — DPT-PLAN-002

## Candidate universe, exact seed list provenance
The owner-provided 2026-11-11 handoff §3.1–3.5 yielded **220 unique candidate names**, not 220 approved active brands. Designer+Niche=103 (global reference); Middle East=31; TH=15, ID=16, MY=11, SG=7, VN=6, PH=5, KH=1, JP=8, KR=9, CN=8 (86 regional candidates total). Group labels and priority are research proposals.
Research source CSV remains **outside the public repo initially**, available to owner as ChatGPT research-pack attachment; do not commit raw private third-party material.

## Candidate registry contract
`candidate_code,canonical_name,name_as_seen,aliases,origin_country,region,market_position,catalogue_role,priority_research,parent_brand_candidate_code,official_url,identity_status,product_type_verified,source_reference_url,source_rights_status,discovery_date,last_verified_at,notes`.
Codes `REF-D-###`, `REF-N-###`, `ALT-ME-###`, `ALT-TH-###`, `ALT-ID-###` etc are **research IDs**, not canonical UUIDs or API record identifiers.
Every candidate begins `needs_review` until enough evidence exists. `official_presence_observed` proves a first-party page was seen, NOT a data-use licence; `third_party_mention_only` is weaker. Origin country remains NULL if not independently confirmed.

## First-party presence observed, 2026-11-11 (15)
- Reference: Dior https://www.dior.com/en_th/beauty/fragrance/women%27s-fragrance ; Le Labo https://www.lelabofragrances.com/our-creations.html .
- Middle East: Lattafa https://lattafa.com/about-us/ .
- Thailand: SÚNDALO https://sundaloofficial.com/ .
- Indonesia: HMNS https://hmnsperfume.com/id/products ; Mykonos https://officialmykonos.com/ .
- Malaysia: Malaya Perfumery https://malayaperfumery.com/ ; Rirana https://riranaparfume.com/contact-us .
- Singapore: Scent by SIX https://scentbysix.com/pages/our-story .
- Vietnam: d'Annam https://dannam.co/en-eu/pages/about .
- Philippines: first-party `Tadhana` https://www.tadhana.co/pages/press ; handoff calls it `Tadhana Fragrance`. Exact alias, jurisdiction vs origin must be reviewed.
- Cambodia: SAARTI https://saarti-cambodia.com/en-kh/pages/about-us .
- Japan: J-Scent/producer LUZ https://luzfragrance.com/j-scent/ .
- South Korea lane: TAMBURINS perfume category https://www.tamburins.com/th/ (country of origin not confirmed by this read).
- China lane: To Summer / 观夏 https://tosummer.cn/cn .
None are approved for automated acquisition, imagery or bulk republishing by this first pass.

## Specific Thai owner priority
- **SÚNDALO**: first-party catalogue present; product lifecycle, exact SKU and rights still unknown.
- **SCENTERY**: third-party marketplace/brand mention only https://www.lazada.co.th/tag/%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AB%E0%B8%AD%E0%B8%A1-scentery/ ; official identity/use rights unresolved.
- **BE CHERIE PARFUM**: third-party mirrored posts only https://www.beautynailhairsalons.com/TH/Sam-Phran/1440246102858525/Be-cherie-Parfum ; first-party evidence/rights unresolved.
- **La Palette**: retained in A research lane; trustworthy official site not confirmed this pass. Never silently discard.
- Verify perfume-vs-retailer/home-fragrance scope and Lattafa–Maison Alhambra, Fragrance World–French Avenue parent/subbrand links before generating canonical brand IDs.

## Decision and sample protocol
Do not equate `Another 13` (Le Labo perfume) with a house, split EDT/EDP/reformulation/edition by real scent identity, and retain `unknown` rather than inferring `discontinued` from release year.
Use one source/time/rights/evidence citation per verified field; do not turn a candidate recommendation into a source grant. Continue region-balanced research after Gate P; no fixed brand-count ceiling.
