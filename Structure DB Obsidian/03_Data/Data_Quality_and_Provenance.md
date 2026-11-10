---
id: DPT-DAT-005
project: DoomParfum By TK
type: data_governance
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - quality
  - provenance
  - integrity
source_of_truth: "../../README.md"
---

# Data Quality and Provenance — P1 Proposed Contract

Observed denominators and source hashes: [[P1_Data_Profiling_Findings]]. All enforcement described here
is PROPOSED and unimplemented. Unknown is a valid state; no AI completion of product facts.

## Claim and canonical layers

- `sources` identifies a publisher/feed. `source_records` identifies one immutable source-key/payload
  version with URL, section/row locator, retrieval time and rights assessment.
- `source_observations` identifies entity, field path, raw/permitted normalized value, value status and
  source record. A record points to Scento if that is all the export supplies; do not claim the upstream
  house URL or independent verification exists when it does not.
- `canonical_selections` chooses a reviewed observation for an entity field. Canonical columns/joins
  are transactionally derived from those selections, with audit history and transform version.
- `data_conflicts` and `conflict_members` retain competing observations. Do not merge conflicting note
  lists into an artificial superset. A reviewer records a rationale for any selection/resolution.

## Missing-value states

| State | Meaning | Canonical treatment |
|---|---|---|
| present | Actual recorded value | Use only after rights/identity review |
| not_recorded | Source explicitly null/blank or empty without verified absence semantics | Nullable; preserve original shape in permitted staging |
| not_supplied | Field absent from this schema | Nullable; do not count as source asserting absence |
| explicit_none | Source affirmatively asserts no value and that meaning is verified | Record claim; distinct from unknown |
| withheld | Privacy/rights prevent retention/display | Null public field with restricted evidence locator |
| not_applicable | Reviewer establishes field does not apply | Record rationale |

A conflict is a separate state across observations, not a replacement for value status. Never use
zero price, zero year, empty country string or a guessed note to represent missing. Empty flat-note
lists and missing pyramids have different meanings. No image rights means no acquired/rendered image.

## Identity, taxonomy and quality metrics

Use canonical UUIDs; external slugs are source IDs. Dedup by source crosswalk first; compare name,
brand, concentration, edition and evidence before linking sources. Similar names produce review
candidates only. Names/aliases may collide; Unicode/diacritics retained. Country and positioning are
independent; source type `arabian` must not decide designer/niche/inspired positioning.

Replace the baseline arbitrary 30/60/90/100 coverage ladder with measured, versioned metrics:
field missing counts with denominators by source and research group; pyramid availability; unresolved
identity/claim counts; provenance/rights completeness; image metadata completeness; duplicate candidates;
and catalogue-vs-matching eligibility. Coverage is not truth or similarity. No numeric confidence model
is accepted by this PR. Matching weights remain PROPOSED in [[Scent_Matching_Spec]].

Review stars, popularity rank, brand performance claims, pairwise human comparisons and algorithm
scores are separate kinds. Dataset/API from the same publisher are not independent evidence.
No reusable comparison dataset was obtained in this task; missing evidence must reduce what can be
claimed rather than create a fake zero or similarity percentage.

## Audit and deletion integrity

Imported facts require source provenance; user-authored facts have private source/actor records.
Canonical mutation records actor, timestamp, old/new observation IDs and reason. Source versions are
append-only except owner-approved rights/privacy removal. Restrict hard deletion of catalogue identities
referenced by purchases/inventory; archive/tombstone instead. Private records are tenant-scoped, excluded
from public Git and must retain history after a cart item or bottle is removed.

Future acceptance: every promoted imported field has a valid selection, no dangling FK, no duplicate
source version, all unresolved conflicts retained, missing statuses survive export/restore, source rights
changes block new imports. Tests and enforcement are NOT RUN. See [[P1_Pilot_Implementation_Plan]].
