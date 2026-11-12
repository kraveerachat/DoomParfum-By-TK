---
id: DPT-DATA-POST5-REVIEW
project: DoomParfum By TK
type: research_evidence
status: review-pending
owner: human-owner
updated: 2026-11-12
tags: [doomparfum, provenance, held-profiles, rights]
source_of_truth: "../../README.md"
---

# Post-PR5 held-profile and permission investigation

[[DPT-DATA-001_Post_PR5_Data_Review]] is a read-only research task based on owner-merged PR5/main
55d39cd619fa6c1ae70521720aa734d632a2083d. This report does not change source claims, canonical
selections, review state, matching eligibility, identity approvals or source/asset rights.

## All44 held source profiles accounted for

Pinned Scento086769ecf1add770ea6646bd4d88d39f0e7cddeb; six artifact hashes verified. Full source
1479/160/420 and12448 selected-list occurrences remain unchanged. Attribution: Scento —
https://www.scento.com/perfume-database ; CC BY4.0 https://creativecommons.org/licenses/by/4.0/ .
Exact arrays, raw labels, logical CSV record and zero-based duplicate ordinals are retained externally.

| Bucket / counting unit | Profiles | Repeated groups | Extra occurrences | Disposition |
|---|---:|---:|---:|---|
| Within Top/Heart/Base lists | 39 | 40 | 40 | Hold; preserve occurrence/order |
| General-only list | 4 | 4 | 5 | Hold; preserve occurrence/order |
| Duplicate-list total | 43 | 44 | 45 | No automatic DISTINCT/deduplication |
| Khamrah external source conflict | 1 | Not this metric | Not this metric | Hold; no fabricated second imported claim |
| Total distinct held profiles | 44 | 44 duplicate groups | 45 duplicate extras | 0 resolved or promoted by this work |

The149 full-source profiles with a repeated flattened label are a different measure: the same label
may legitimately occur across pyramid layers. That count is not149 within-layer violations or new
holds. Every selected-list label maps unambiguously to one pinned material primary name; no alias
ambiguity was found that would justify collapsing repetitions. Absence of identity-key duplicates
under house/name/concentration does not prove absence of semantic duplicates or edition differences.

[[P1_Data_Conflict_Matrix]] CF02/03 already documents Khamrah Mahonial versus Lily Of The Valley,
structured-versus-prose whole-list differences, and generic versus origin-specific base wording.
Existing historical evidence is cited; no restricted page was scraped/refetched or copied here.
These are not proven synonyms, reformulation or chemical-composition differences. Usable source
rights and separate section/field claim locators are prerequisites for importing new conflicting claims.

Owner alternatives, neither executed: retain all43 duplicate-list holds until an upstream correction,
or explicitly review a new derived note-membership transform/version whose selected value is unique
while original ordered occurrence claims remain immutable and auditable. The latter needs its own
mapping review, consistency/negative tests and source lineage; it is not a silent update to PR5's
hash-bound mapping. Khamrah additionally needs rights-backed claim reconciliation, not majority vote,
newer-wins or a union of lists. No held flag is flipped merely to supply matching/performance inputs.

## Incremental brand research

All226 candidate rows and21 prior identity conflicts are retained. Six existing candidates reviewed;
three new factual locators, three unresolved Thai authority gaps;0 new candidates, identity approvals,
semantic merges or conflict closures.

- [SÚNDALO official home](https://sundaloofficial.com/) supplies Thailand-origin wording. This remains
  a source-backed review observation; canonical country/identity and reuse are not auto-approved.
- [Fragrance World legal terms](https://fragranceworld.ae/terms-of-service/) list French Avenue within
  the portfolio; this is narrower than a universally verified legal-parent/canonical-brand decision.
- [Zimaya terms](https://uae.zimayaperfumes.com/pages/terms-and-conditions) identify Afnan as website
  owner/operator. Website operation alone does not settle every brand-parent/identity question.
- La Palette, SCENTERY and BE CHERIE PARFUM remain priority candidates with unresolved authoritative
  first-party identity/evidence. They are retained, not silently discarded or fabricated as verified.

Official presence and a legal-page observation do not grant automated product-content/image reuse.
No private owner data, reviews, prices, feeds or canonical regional perfume records were acquired.

## Note illustration and pairwise evidence research

Five new file-page candidates: [Cardamom](https://commons.wikimedia.org/wiki/File:Cardamom_seeds.jpg),
[Patchouli](https://commons.wikimedia.org/wiki/File:Patchouli.jpg),
[Tonka Bean](https://commons.wikimedia.org/wiki/File:Tonka_Beans.jpg),
[Saffron](https://commons.wikimedia.org/wiki/File:Saffron.JPG),
[Ylang-Ylang](https://commons.wikimedia.org/wiki/File:Ylang-ylang_(Cananga_odorata)_in_the_Philippines_01.jpg).
Exact creator/license/version/selected-license/attribution and subject caveats are in the external
per-file queue. Public-domain self-release is not relabeled CC0; Tonka's selectable licensing is not
merged with unrelated obligations. No blanket image permission is inferred from Commons hosting.

Candidate coverage12/46 applies to the historical research vocabulary, not the approved P1 pilot58
or the full420-note vocabulary.34 research labels lack a candidate; seven general/accord/synthetic
label cases retain placeholder recommendations. A plant/spice illustration is not evidence that an
ingredient occurs in a perfume or that an accord is a literal plant. Actual image files acquired0,
display approvals0, new bottle grants0. IMP-P1-03 local synthetic PNG tests are separate from rights.

D7 reviewed three opportunities and retains the existing five publisher inspiration leads. No new
independent sensory record, usable relation or verified Dupe pair. A
[CC-BY-tagged dataset card](https://huggingface.co/datasets/MrBob23/perfume-description/blob/main/README.md)
was rejected: Fragrantica-derived upstream metadata and preferences between generated descriptions
do not establish authorized perfume-pair sensory evidence. No dataset files or restricted site content
downloaded. Scento's schema has no explicit pairwise evidence field; note overlap cannot manufacture one.
Future owner-authored comparison observations remain a potential source, but none were supplied here.

## Evidence, limits and next actions

External HELD_44_FORENSIC_REPORT.json and QA.json preserve exact claims and eight source-forensic
assertions. Increment package has14 files,28 persisted QA checks; seven
baseline input hashes unchanged. Public Git contains summaries only. No worldwide completeness,
legal-parent proof, new source permission or real application capability is claimed. No runtime/DB
test is inferred from these file checks; prior merged catalogue facts remain separately attributed.

Next: Owner reviews hold-resolution alternatives and source/asset queues; keep all44 holds. PR4
matching decisions/Gate P and PR6 image implementation review remain separate. Further acquisition
requires exact-use rights; no production/cloud/merge authorization. [[DPT-DATA-001_Review_Evidence]].
