---
id: IMP-MATCH-03-DATA-RESEARCH-CONTINUATION
project: DoomParfum By TK
type: source_semantic_contract_proposal
status: proposed-data-intake-gated
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, wikidata, source-semantics, data-research, provenance]
source_of_truth: "../../README.md"
---

# IMP-MATCH-03 parallel data research — Wikidata semantic boundary

This is a new bounded data-research addendum while the separate synthetic B1 implementation task
proceeds. Exact B1 code approval does not approve acquisition, an external adapter, real-source
matching or data promotion. The prior [[B1_Parallel_Preparation_Checkpoint]] and
[[B1_Data_Enrichment_and_Acquisition_Backlog]] remain frozen; their64/10and18/14checks are not rerun
or relabelled as this task's new tests. All eight frozen preparation documents remain untouched.
Parent owns current task/decision/status/handoff reconciliation; this worker changes only this note
and ignored sanitized evidence under `.local/b1-implementation/dataresearch/`.

## Actual new evidence and its limits

Exactly two new official property-reference pages were read on2026-11-15 Asia/Bangkok:

- [Wikidata P571 — inception](https://www.wikidata.org/wiki/Property:P571) describes when an entity
  begins to exist and uses a point-in-time value. Its broad aliases/examples do not establish
  perfume-edition release semantics. No particular brand, perfume or edition was retrieved.
- [Wikidata P176 — manufacturer](https://www.wikidata.org/wiki/Property:P176) describes the product's
  manufacturer/producer, with an item-valued relation. That role alone does not identify the
  marketing brand, license holder, corporate parent or specific edition.

These are property documentation/metadata reads, not product/brand entity samples or API queries.
The existing Wikidata structured-data CC0/access reference remains the prior general license path;
neither this check nor B1 approval adds a project intake/use grant. No linked images, article text,
product-page claims, entity endpoints or new source records were acquired. Actual perfume/brand
coverage and statement quality remain unmeasured. OBF's crawler restriction and earlier manufacturer
terms failures remain preserved; no retry, alternate route or bypass was attempted.

## Proposed semantic review contract — WIKIDATA-IDENTITY-TIME-REVIEW-1

This label identifies a proposed review dossier, not implemented code, accepted field definitions,
an adapter or a canonical mapping. Proposed source observations must pass the existing
[[P1_Source_to_Canonical_Mapping]], [[Data_Dictionary_Draft]] and
[[Incremental_Source_Adapter_and_Media_Intake_Plan]] gates before storage/materialization.

| External evidence | Proposed review output | Direct canonical action prohibited |
|---|---|---|
| Entity identifier, revision and language-labelled name | Candidate identity/crosswalk with explicit entity role: brand, corporate entity, product family or exact edition. Preserve source/language/revision and unresolved alternatives. | No label-only join, alias merge or automatic assignment of a perfume's brand/edition. No product-family-to-edition collapse. |
| P571 on a brand or organization | Candidate inception/founding observation attached to that exact source subject. Keep the subject role explicit. | Do not fill any perfume release_year from a brand/organization founding date. |
| P571 on a fragrance family/product concept | Candidate product-concept inception observation with unresolved edition scope. | Do not assign the date to EDT/EDP,concentration,flanker,reformulation or regional edition without exact evidence. |
| P571 on a reviewed exact edition, plus source/reference/qualifier evidence that identifies edition release | A proposed release-year candidate only after a separately accepted mapping resolves date meaning, precision/calendar and the existing entity match. | No direct canonical selection or update. A generic inception statement alone is insufficient, even if the year looks plausible. |
| P176 manufacturer item relation | Candidate producer/manufacturer relationship in the external review dossier, preserving statement identity and qualifiers. | Do not copy the manufacturer item into perfumes.brand_id or create a brand automatically. A factory, parent, licensing partner or producer role must be independently distinguished. |
| Missing,unknown,no-value,deprecated or contradictory evidence | Explicit unavailable/ambiguous/conflicting review state with original statements retained. | No zero/default/current year, first/preferred/newest/majority shortcut, silent omission of conflicts or overwritten source claim. |

The proposed manufacturer/inception dossier labels above are not new database field definitions.
If no approved target field exists, keep the evidence unmapped in a review manifest. A new field
definition/schema change requires its own applicable Planning/Implementation Gate. Do not invent a
generic source_observations path to bypass allowed field definitions.

The current dictionary gives perfumes.release_year a nullable1000..9999range and keeps edition_label
and concentration separate. That numeric range validates shape, not date meaning. A source date
with unknown meaning, insufficient precision, incompatible/unreviewed calendar, multiple unresolved
values or an ambiguous edition remains unknown/unselected; do not truncate or coerce it into a
valid-looking year. Actual source time/qualifier/reference representation must be verified in an
approved finite sample before an adapter contract defines conversion. No conversion runs here.

## Identity and provenance checklist for at most five future records

The existing ENR-WIKIDATA-BRAND-ID-1 proposal remains the upstream scope. This addendum refines its
semantic review only. No source IDs are selected and no sample request is executed. Any future
review unit has an explicit maximum of5source entities/records, a fixed field/property list and
request budget, and a named permitted reviewer/target scope before retrieval.

1. Owner/reviewer identifies the exact candidate source entities and subject roles. Record why each
   corresponds to an existing brand, producer, product family or edition; keep uncertain matches
   unresolved. Brand names, concentrations and similar labels alone do not prove identity.
2. Pin the source revision/capture, retrieval method/date, applicable source-use/CC0 evidence,
   audience and operation scope. Linked text/images/media require their own rights; an entity link
   is not a license for those objects. No real ranking or public display follows from the sample.
3. Preserve each statement/property identifier, value and status, qualifiers, rank and reference
   locators needed to explain its exact claim. Keep multiple claims from the same record distinct;
   do not replace conflicting assertions with one latest/preferred statement.
4. For P571, decide the event and exact subject before deriving any candidate year. Preserve source
   precision/calendar/context; unknown or unsupported date forms stay unknown. Require explicit
   exact-edition release evidence before even proposing release_year.
5. For P176, review manufacturer versus brand/owner/licensor roles independently. Retain a producer
   relation as unmapped if the existing schema has no permitted field. Do not auto-create or rewrite
   canonical brands, external identity links or edition relationships.
6. Record accepted/rejected/unknown/conflicting review outcomes separately from canonical selection.
   Any later source_observation must retain its record/revision,entity,field,claim locator/key,
   transform version,scope and operation rights. Canonical selection needs its own authorized
   reviewed observation/rationale; source popularity or preferred rank is not that authorization.
7. Preserve43normalization proposals,the independent Khamrah conflict,44holds and matching
   eligibility. A metadata sample cannot establish note-list completeness, note membership,
   accord/family facts or real-data eligibility. Chemical INCI never becomes scent notes/accords.

## Synthetic review examples and future acceptance controls — NOT RUN

These are decision examples, not retrieved product facts, executable tests or B1 golden cases.

| Synthetic review example | Required conservative outcome |
|---|---|
| Brand entity inception1900; perfume edition date absent | Keep brand inception as candidate evidence; perfume release_year remains unknown. |
| Product-family inception2010; EDT/EDP edition unresolved | Do not assign2010to either edition. Retain identity/scope uncertainty. |
| Exact-edition source subject with P571and an explicit edition-release reference | Candidate year may be proposed only after date semantics/precision/calendar and mapping are accepted; canonical selection remains a separate gate. |
| Producer item differs from marketing brand | Preserve producer evidence; do not rewrite brand_id. |
| Two conflicting dates, coarse/unknown date precision, deprecated or no-value statement | Preserve exact unavailable/conflict state; no zero, majority or preferred-rank default. |

Future adapter acceptance must cover those cases plus duplicate/reordered statements, revision
changes,repeated capture replay,source-rights changes,wrong subject/edition,no permitted field,
conflicting references and rollback. It must prove no hold/eligibility or immutable observation
change outside the approved task. All adapter/DB/ETL/source-selection/replay/rights/real-data tests
remain SPECIFIED / NOT RUN. Existing M1/B1 tests and prior raw coverage checks are not repeated.

## Readiness, next exact action and tool execution

The property-role semantic review and bounded checklist are DONE as preparation. Actual data-source
coverage/usable sample is PARTIAL/UNVERIFIED. Acquisition/import/canonical promotion are BLOCKED until
the Owner separately accepts the source/entity/property/method/request-budget/audience/use contract,
usable permission and applicable source-adapter Planning/Implementation Gates. The synthetic B1
implementation may proceed within its own approved contract; it supplies none of these data gates.

Recommended next Owner data action: choose the existing ENR-WIKIDATA-BRAND-ID-1max5entity identity-only
sample scope, or continue the existing local pinned-field mapping review. If a date/manufacturer
extension is desired, accept the explicit semantic mapping above before adding properties to the
finite sample. No permission request was sent and no outside account/service was configured.

TOOL EXECUTION REPORT: existing read-only Git/Python/Context Mode and built-in web used for two
official property-reference pages. New source records/assets/grants/imports/normalizations/hold
releases/eligibility changes0; DB/Docker/service/Git/Handoff/Production mutations0. No source adapter,
runtime/scorer/test implementation, acquisition endpoint or paid service. Only this new note and
ignored sanitized metadata/static-check evidence are written; parent owns shared records/packaging.
