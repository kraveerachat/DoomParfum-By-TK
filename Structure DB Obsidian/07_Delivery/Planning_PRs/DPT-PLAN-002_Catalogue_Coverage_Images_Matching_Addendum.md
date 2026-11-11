---
id: DPT-PLAN-002-CATALOGUE-EXT
project: DoomParfum By TK
type: planning_pr_addendum
status: proposed
updated: 2026-11-11
timezone: Asia/Bangkok
---

# DPT-PLAN-002 — Catalogue Coverage, Note Images, Search and Dupe Matching

PLANNING ONLY. This document does not authorize implementation, unlicensed scraping, third-party imagery, production mutation, additional expense or automatic publication. Human Gate P is pending.

## New scope and change from focused ingestion

The original handoff specified "Broad Discovery, Focused Ingestion" and explicitly did NOT require every perfume of every brand. The owner's newest requirement is wider: capture every model **discoverable in an individually approved source**, even when no detailed profile is available. Keep source-coverage metrics; do not claim universal completeness.

- Maintain every verified brand and alias, with country, designer/niche/independent/inspired market positioning and parent relationships. Geographic region, brand positioning and context-specific reference/alternative role are separate.
- Record every permitted-source-visible perfume identity, edition/flanker/reformulation and concentration in an index, including retired models. A partial profile is not discarded.
- Enrich progressively with fragrance family, accords, Top/Heart/Base notes, usage, descriptions, size/SKU, retailer price/market/stock, note images, bottle images, review/evidence and pairwise Dupe relations.
- Index/search must support known-incomplete entries and show source, last checked date, missing fields and confidence.

## Logical levels; no duplicate database tables

L0 Brand Registry -> L1 Perfume Product Index -> L2 Verified Profile -> L3 Notes/Accords/Family -> L4 Sizes/Market/Price -> L5 Bottle Images and Shared Note Illustrations -> L6 Pairwise Evidence and Versioned Matching.

Existing Data Dictionary already proposes brands, perfumes, product_variants, perfume_notes, perfume_accords, image_assets, asset_permissions, perfume_images, note_images, perfume_relations, comparison_evidence and matching_results. Reconcile with the 47-table merged P1 foundation before migrations. A perfume may be indexed with no pyramid or image.

Olfactory notes are not necessarily actual chemical ingredients. The same licensed note illustration can be shared across many perfumes; bottle pictures must match exact perfume/edition/variant. For each image store a source page, license and rights proof, creator/attribution, permissible acquisition/display/transformation, file hash if downloaded, review state and revocation behavior. Unknown permission blocks usage of that asset, not the whole perfume index.

## Search features

Search by brand/alias, product/edition/concentration, country, brand position, fragrance note/alias, accords, family, season, use, availability/price in target market, current/historical and data completeness. Preserve observed seller/market/timestamp for price and stock. Begin with PostgreSQL normalized text/trigram indexes; vector search is optional later.

## Two complementary Matching paths

A. Evidence graph: documented comparison between two exact perfumes, with source, publisher group, claim type (reported_dupe / similar_profile / inspired_by), source observation timestamp, reviewer, contrary evidence and rights. Never imply official inspired-by admission from community opinion.

B. Structural-candidate search: independently compare reviewed pyramid notes, accord and family data. Return shared/different notes and data coverage; a structural overlap is not proof of perceived scent equivalence. Keep computed similarity and evidence confidence separate.

**Proposed scoring inconsistency requiring owner decision:** existing Scent Matching Spec calls Notes 40% (Top 10 / Heart 15 / Base 15) + Accords 25% + Family 15% + Evidence 20% a Structural Similarity score. The first 80% are structural; the last 20% measures different evidence. Propose separate structural score, community-evidence score, confidence grade and optional combined recommendation rank. No fabricated "95% same scent"; benchmark weights and missing-data thresholds.

## Revised execution work packages

D1 Brand coverage counts and identities (keep existing 220 seed).
D2 All-permitted-source-visible Perfume Index with per-source cursor and totals.
D3 Licensed Scento 12-profile pilot, then 1,479-profile pinned baseline under existing IMP-P1-02.
D4 Canonical note aliases/material kinds and pyramid layer provenance.
D5 Licensed shared note images and exact-profile bottle assets.
D6 Search API/UI with indexed-only and completeness states.
D7 Reviewed Dupe evidence graph and conflict/disagreement handling.
D8 Matching, side-by-side compare, versioned scoring and negative tests.
D9 Admin incremental updates, locks, manual review, rights revocation and size benchmarks.

All post-research implementation requires approved Gate P and individually authorized data/media sources. Fragrantica remains human research/reference only under current ToS, not an approved automated ingestion adapter. Python/Apify/Firecrawl technical access does not itself grant reuse rights.

## Research checkpoint

Local research-only Scento sample, pinned revision 086769ecf1add770ea6646bd4d88d39f0e7cddeb (CC BY 4.0): 12 perfume source records from 11 houses, 84 note occurrences, 46 unique note labels, 7 fully reported pyramids and 5 unlayered-note-only profiles. Two Wikimedia Commons note-image license *page candidates*, zero acquired images, zero verified Dupe pairs, zero PostgreSQL rows imported. No third-party raw dump has been added to the public repo.

Scento attribution: Scento — https://www.scento.com/perfume-database ; license https://creativecommons.org/licenses/by/4.0/ . Example Commons evidence: https://commons.wikimedia.org/wiki/File:Lavender_plant.jpg (CC BY 4.0); https://commons.wikimedia.org/wiki/File:Lemon_fruits.jpg (CC BY-SA 4.0); each needs final review before asset use.

## New owner decisions and acceptance

NEW-07 approve all-visible-model discovery index plus progressive full-profile enrichment.
NEW-08 distinguish structural score, evidence score, confidence and recommendation rank.
NEW-09 allow partial-profile search results and define matching minimum fields.
NEW-10 approve image licensing, attribution, variant identity and reuse/revocation rules.
NEW-11 approve per-pair Dupe claims, contradictions and independent-source review.

Test later: no duplicate IDs on rerun; no mistaken EDT/EDP merges; no invented pyramid; preserve repeated raw note evidence; no bottle on wrong flanker; no inference of Dupe from brand/category alone; blocked images never published; market stock does not mean global product status.

Related Obsidian docs: [[DPT-PLAN-002_Focused_Catalogue_Acquisition_and_Automation]], [[Data_Dictionary_Draft]], [[Scent_Matching_Spec]], [[Source_Registry]], [[Roadmap]], [[Decision_Log]].

IMPLEMENTATION_NOT_STARTED=YES
OWNER_GATE_P=AWAITING_REVIEW
PRODUCTION_MUTATION=NO
