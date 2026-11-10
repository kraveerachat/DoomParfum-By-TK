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
  source record plus mandatory claim_locator/claim_key and transform_version. Multiple claims from the same record/field survive independently. A record points to Scento if that is all the export supplies; do not claim the upstream
  house URL or independent verification exists when it does not.
- `canonical_selections` chooses an observation UUID per access_scope/entity/field. Public canonical columns/joins
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


## Post-review identity and privacy correction — PROPOSED

A captured source document is not one claim. Structured and prose assertions use different locators;
multiple assertions at one locator use stable claim keys. Observation identity includes access scope,
record, entity/kind/field, locator/key and transform version. Same identity with different extraction
output is rejected, not overwritten. Agreeing claims at different locators remain distinct evidence.
Conflict membership and resolution/selection FKs bind scope/entity/kind/field and exact observation ID;
a resolution must be a conflict member. Full contract: [[Data_Dictionary_Draft]].

Access scope belongs to sources, captures, observations, permissions, images, links, conflicts,
staging/audits and computation outputs, independently of the referenced perfume's visibility.
Private/shared selections are overlays; only public claims can materialize public catalogue data.
No private conflict flag/count, locator, photo, rating, matching input or cache result may leak through
a public entity. Shared access needs active explicit membership; personal purchase/history remains
private. Publication requires a reviewed new sanitized public copy, never in-place scope widening.
Rights and application authorization both apply. Enforcement/test specification:
[[Security_and_Privacy]], [[P1_Pilot_Implementation_Plan]]. No runtime checks have run.
