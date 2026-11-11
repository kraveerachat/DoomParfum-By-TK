---
id: DPT-MAT-DUAL-DATA
project: DoomParfum By TK
type: data_contract
status: proposed
owner: human-owner
updated: 2026-11-11
tags: [doomparfum, matching, provenance, privacy]
source_of_truth: "../../README.md"
---

# Matching Inputs, Schema Compatibility and Missing Data

This is a proposed read-model contract, not a migration or claim that production data exists.
Inspect exact merged SQL, not the older conceptual table names in README. Preserve all eight migrations,
canonical selections, source occurrences, current rights enforcement and historical receipts.

## Input-to-foundation crosswalk

| Needed concept | Existing merged foundation | Read-model rule / gap |
|---|---|---|
| Exact scent identity | perfumes, brands, product_variants, entities | canonical perfume ID is scent profile; variant is packaging; never name-merge EDT/EDP/flanker/reformulation |
| Note vocabulary/aliases | notes, note_aliases | approved target with reviewed source-backed selection; normalization nfkc-lower-v1 is not arbitrary fuzzy matching; ambiguous aliases require disambiguation |
| Layered notes | perfume_notes with top/heart/base/general, sort_order, source_record_id | canonical set scoring ignores order; immutable observations/staging retain ordinals/repeats; layer completeness is a separate reviewed input descriptor |
| Accord vocabulary/strength | accords(scheme,code), perfume_accords.strength nullable [0,1] | numeric column alone does not prove compatible observed intensity; source scale, rank/presence, completeness and transform must be audited |
| Families | families, perfume_families(role primary/secondary) | same scheme/version or explicit reviewed crosswalk; material_family/character not main accord |
| Pair evidence | perfume_relations, comparison_evidence | relation binds exact pair; claim_type/reported_similarity/independence_group are evidence, not model feature weights |
| Computed pair result | matching_results | relation_id NOT NULL; algorithm_version/input_sha256/coverage/explanation supported, but request-time reads must not manufacture relations |
| Custom query | no approved persisted query entity | B queries/results ephemeral and scope-bound; no fake perfume/relation/claim used to fit existing matching_results |
| Availability/price | perfumes status facts, retail_listings, price_observations and source claims | fresh market/channel/variant/currency evidence; index presence/launch year is not production or stock proof; richer lifecycle contract is a PR #3 dependency |
| Assets | image_assets/asset_permissions/perfume_images/note_images | independently authorize each exact capture/asset/derivative for display; placeholder otherwise |
| Provenance and access | sources/source_records/source_observations/canonical_selections/conflict model and access scopes | use approved effective fields with valid source uses and public-or-authorized scope; overlays never widen through public targets |

No per-asset rights are implied by Scento's dataset license. No persistent custom query/cache schema is
approved by this document. If later SQL cannot represent required completeness, scale or query snapshots
safely, record a gap and propose an additive migration under an approved implementation/amendment;
do not hide new fields inside arbitrary JSON to bypass existing allowlist/materialization rules.
The read model can assemble metadata from approved observations and a versioned policy manifest without
writing catalogue data. Persisting A results must still obey existing relation/materialization/hash
guards; the future adapter must prove compatibility or leave results ephemeral.

## Required canonical input envelope (conceptual, not a database table)

For each effective field retain entity/edition ID, access scope, selected observation/capture IDs,
source record revision/hash, locator, review state, applicable rights/grant and expiry, observed/reviewed
date, normalization/taxonomy version, conflict disposition and transform lineage. For a list add
representation layered/general, complete-as-reported/incomplete/unknown, explicit-empty vs absent and
source enumeration boundary. A blank array is not proof of completeness. Numeric accord inputs also
need original value/scale/range/units, compatible scale contract and transform version; rank/presence
has its own kind and no invented strength. User preference slider values are query inputs, never observations.

An approved canonical ID/selection is necessary but cannot substitute for missing rights or a revoked
capture. Field omission is explicit; do not average contradictory source claims. Preserve competing
claims/locators and reviewers' selections. Only selected, rights-usable fields can score; use
matching_eligible and relevant review/conflict gates. When one dimension is withheld, recompute
coverage and method qualification; if below minimum, return insufficient_data, not the prior cache value.

## Missing/identity policy

| Situation | Required response |
|---|---|
| Missing top/heart/base | unknown; at least two comparable layers for A pyramid; complete general lists (or explicit union of all three complete layers) may use flat fallback; B exact-layer query cannot invent layers |
| Known complete empty list | distinct from missing; empty/empty J is null; empty/nonempty can be zero |
| Partial list or unresolved completeness | explanatory matches allowed, no claim of absence; strict negative rules fail closed; B main fit null |
| Missing accord strength | presence/rank-only path with intensity_unknown; never 0, evenly split, or guessed from bar length/family |
| Different accord/family schemes | reviewed crosswalk required; otherwise null dimension and visible reason |
| Alias maps to multiple IDs | picker disambiguates or returns unresolved; no automatic merge, fuzzy family credit or duplicate score boost |
| Repeated raw note occurrence | keep every claim/ordinal; current canonical note uniqueness stays; ambiguous many-to-one materialization remains review/quarantine |
| Same ID repeated in query | deduplicate after alias resolution; conflicting role/layer semantics require correction |
| Distinct EDT/EDP/version IDs | remain distinct; duplicate identity candidates withheld until reviewed; no duplicate suppression by name alone |
| Relevant source conflict | retain claims; withhold unresolved field; do not choose the source yielding the highest score |
| Unavailable source/data-use right | exclude affected field/candidate, remove cached derived output; no confidence threshold can compensate |
| Only family/rating/brand metadata | may browse indexed perfume, but no numeric scent score |
| Missing image or unusable asset right | authorized text/score may remain; use placeholder, no external hotlink |
| Current/stock unknown | labeled unknown group; strict in-market filter excludes; historical data preserved |

## Data readiness and PR #3 integration

Merged P1 evidence records Scento revision086769ecf1add770ea6646bd4d88d39f0e7cddeb, CC BY 4.0,
1,479/160/420 raw rows and approved pilot12 perfumes/5 houses/58 material candidates/93 occurrences.
This planning task does not reread/import raw files. IMP-P1-02 ETL completion is not established by PR #2.
No reusable pairwise evidence set or universally numeric accord vectors is established by P1.

PR #3 addendum at inspected69255b0 reports a different research sample:12 profiles/11 houses/46 note
labels/84 links, seven layered/five general. Those are that workstream's reported cohort, not a verified
replacement of the approved pilot. Before implementation reconcile source IDs, manifest/hash, selection
rule, mapping and rights with the P1 pilot. Do not combine the counts or silently replace fixtures.
Keep the two findings separately attributed; this is an integration check, not proof either is invalid.

Upstream request to the Brand Research workstream (recorded here; no message/PR #3 edit): provide
authorized canonical note IDs/layer/source-label/ordinal/alias review; accord scheme/ID/input-kind/
value/scale/rank/presence/completeness/provenance; family scheme; exact pair claims/independent publisher
groups/opposition; market/edition/status/time; per-field and per-asset uses. Do not import missing data
from Fragrantica to fill these gaps. New regional imports, direct pair claims and images need individual
rights and verified samples. Scento local approval is not an API or image acquisition grant.

Attribution must retain publisher Scento, pinned revision, source URL, CC BY 4.0 license link and
change/normalization notice where required, following [[Rights_and_Attribution]] and approved OD-01.
No raw rows/private exports/attribution manifests containing personal data enter public Git here.

## Authorization and output boundaries

Private source records/notes about a public perfume remain private overlays. Match inputs, counts,
filters, explanations, evidence summaries, negative-rule outcomes and facet statistics all use the
same caller-visible data. Another user's overlay must not change any public result or response shape.
Shared membership revocation changes the authorization epoch and blocks later pages/cache hits.
Unauthorized IDs and nonexistent IDs return the same external not-found/invalid-selection category.
No administrator/BYPASSRLS read followed by post-filtering is an acceptable application authorization path.

Response contract (conceptual): mode, method/version, source snapshot, request/policy hash, candidate ID,
score or null+reason, components/effective weights, coverage, confidence+reasons, known/unknown shared
and differing descriptors, permitted source attribution, separate pairwise evidence, availability and
image placeholder/authorized asset reference. Private input hashes/observation IDs stay server-side;
public share URLs contain only validated public vocabulary/identity IDs and safe query values. Evidence
URLs/excerpts require their own display rights; no invented subjective explanation or source citation.

See [[Dual_Mode_Matching_Architecture]] for revocation-aware cache/pagination and
[[Dual_Mode_Scent_Search_UX]] for share behavior. All API/cache/RLS tests are future acceptance, NOT RUN.

## Deterministic current-first filter contract (DM-06 proposal)

Evaluate only caller-visible, selected, rights-usable lifecycle/market facts at request as-of time.
A confirmed discontinued lifecycle is historical even if a retailer still has stock; Include Historical
is needed for candidate results, while an A reference may remain historical. Otherwise group0 is known
in_production OR verified fresh in_stock in the selected market; group1 is the remaining unknown/
unverified-currentness records. Out_of_stock alone does not establish discontinuation. Badges still
show production and stock separately; group0 is not a claim every item can be bought now. Strict
in-market additionally requires fresh in_stock for that market, excludes unknown/out_of_stock/preorder
unless that specific state is selected, and cannot be satisfied by production alone.

Market/price filters require an explicit market and currency/variant-size basis. Source-specific status
freshness TTL must be reviewed; without a configured usable TTL, stock is unknown for strict filtering.
A perfume's data-freshness730-day draft cap is not the stock TTL. No automatic exchange conversion,
global stock inference, or undocumented geo preference enters score. Reconcile richer status/role
contracts with PR #3 rather than inventing a new approved database enum here.

## Parallel-source refresh during publication

PR #3 advanced to0cdfba4504594a888eb2f11947ea2d1dd58b6db8 during this task. Its new full-snapshot
CSV audit reports1,388 layered/91 general profiles and149 profiles with repeated labels in a flattened
list. Those are that PR's reported audit metrics, not this task's raw-data remeasurement. The149
flattened-list metric is not the P1 finding of40 within-layer groups in39 profiles. Keep source format,
revision, counting unit and cohort explicit; do not declare a contradiction or silently change P1
fixtures. The new audit still states no PostgreSQL import or verified Dupe/image acquisition.
