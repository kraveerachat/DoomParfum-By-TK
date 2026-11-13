---
id: DPT-DATA-003-MATRICES
project: DoomParfum By TK
type: data_readiness
status: review-pending
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, evidence, coverage, rights]
source_of_truth: "../../README.md"
---

# Post-merge data readiness and review matrices

## Scope and evidence boundary

Task [[DPT-DATA-003_Post_Merge_Readiness]] prepares evidence under the Owner's post-merge prompt, Wave D and G1. Base main is `58ceafe72129b70f0333c7c4f2c6f38dba855272`; branch is `codex/plan-offline-data-readiness`. This is a docs-only readiness proposal. No source acquisition, policy acceptance, data promotion, matching activation, schema or runtime change occurred. See [[DPT-DATA-003_Audit_Evidence]] for exact checks and preserved diagnostic errors.

Operator READ ONLY aggregate inventory at 2026-11-13 08:09:30.147499 UTC, with exact family/note/raw-shape supplement at 08:17:53.752609 UTC, found 1,479 perfume records: 1,435 approved and 44 held draft. All 1,479 are user-private; none are matching-eligible. There are 160 brands, 420 approved note concepts, 11,972 canonical note links, 2,059 source captures, 10,489 observations and 8,845 selections. No verified edition registry or product variants exist (variant rows 0); perfume identity records are not independently verified edition coverage.

Before/after fingerprints across all 49 application tables, security definitions and application roles were identical. These operator aggregates do not demonstrate an authorized application session, RLS read or publication grant.

## Canonical field coverage

Each perfume field has denominator 1,479; brand fields have denominator 160. Populated/missing partition that denominator. Held/unapproved and rights/review are separate overlapping dimensions: every perfume field has 44 unapproved entities, including held rows whose identity scalars are populated. The final column requires a present same-scope selected observation and the current local storage/display/automation grant; it does not establish completeness, accepted normalization, edition identity, owner-bound application access or matching eligibility. Consequently all 1,479 perfume profiles remain unavailable for real application matching, independently of these field counts.

| Field | Denominator | Populated | Missing | Approved populated | Held populated | Held missing | Selected present + active local rights |
|---|---:|---:|---:|---:|---:|---:|---:|
| brand.country_code | 160 | 0 | 160 | 0 | 0 | 0 | 0 |
| brand.name | 160 | 160 | 0 | 160 | 0 | 0 | 160 |
| brand.website_url | 160 | 0 | 160 | 0 | 0 | 0 | 0 |
| accord_presence | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| accord_strength | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| bottle_image_link | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| brand_id | 1479 | 1479 | 0 | 1435 | 44 | 0 | 1435 |
| concentration_code | 1479 | 1228 | 251 | 1188 | 40 | 4 | 1188 |
| description | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| edition_label | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| family | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| gender_label | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| name | 1479 | 1479 | 0 | 1435 | 44 | 0 | 1435 |
| notes.base | 1479 | 1348 | 131 | 1348 | 0 | 44 | 1348 |
| notes.general | 1479 | 87 | 1392 | 87 | 0 | 44 | 87 |
| notes.heart | 1479 | 1348 | 131 | 1348 | 0 | 44 | 1348 |
| notes.top | 1479 | 1348 | 131 | 1348 | 0 | 44 | 1348 |
| price | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |
| release_year | 1479 | 80 | 1399 | 76 | 4 | 40 | 76 |
| seller_listing | 1479 | 0 | 1479 | 0 | 0 | 44 | 0 |

Top/heart/base link counts are 3,693 / 3,742 / 4,150 across 1,348 profiles each. General links number 387 across 87 profiles. Zero accord concepts/links means both accord presence and strengths are unavailable; no synthetic intensity may stand in for source strengths. Family concepts/links and selected `family`, `families.primary`, `families.secondary` values are all 0, despite the family field contract existing. Bottle assets/links, ingredient image links, per-asset permission records, pairwise evidence/relations, retail listings and price observations are all 0. Pairwise relations are evidence leads, not measured smell similarity or confirmed Dupe relationships.

## Raw shape versus reviewed availability

The 1,479 unique raw perfume captures contain nonempty top/heart/base lists in 1,388 each, while all 1,479 contain nonempty general `notes`; these representations overlap. The import plan chooses 91 flat representations. General source text is not limited to those 91 and is not automatically canonical. The canonical approved populations are 1,348 layered and 87 flat; 39 layered plus 4 flat repeat-note holds and Khamrah account for the 44 held profiles. No raw list shape establishes reviewed closure or absence.

Raw primary-family text is populated in 1,479/1,479 and secondary-family text in 1,075/1,479; description, character, seasons and times-of-day in 1,479 each; concentration in 1,228; year in 80; perfumers in 69; popularity rank in 613. These are nonempty-string counts only, not token quality, typed validity, normalization, selected claims, permission to promote or accord strengths. Raw description/family coverage must not be reported as canonical application availability.

House country text is populated in 158/160 captures (2 missing), with 17 distinct publisher origin-country labels. Canonical brand country codes and website URLs are both 0/160. Origin claims do not measure retail markets, regional availability or completeness of worldwide brand coverage. The worldwide/regional target universe and verified edition universe are unknown, so exact global missing totals are NOT AVAILABLE. The pinned perfume schema has no dedicated bottle-image, price, edition-label, lifecycle, stock or market field. House `portrait` metadata is not acquired image bytes or a media license.

## Source rights and selected provenance

One current rights assessment is bound to the one pinned Scento source. All 2,059 captures retain revision and locator (missing 0 each), and qualify for the existing local storage/display/automation scope. Current assessments: research, automation, cache, storage and display allowed 1/1 each; redistribution restricted 1/1; AI use unknown 1/1. Expired, revoked, future-checked and missing-evidence assessments are 0 each at audit time. A current local grant is not public redistribution, arbitrary derivative/media permission, matching activation or a new source-rights approval.

Use-specific eligibility still requires exact source/capture/observation/selection and access-scope binding, accepted reviewer/normalization/completeness semantics, exact edition binding when claimed, permitted operation, evidence locator and revision/hash, and current rights at use. Expired/revoked/unknown/changed grants deny that use; preserve the original immutable evidence, report the reason and require explicit re-review. Do not infer an enum from free-form rights `scope` text. The canonical conflict table currently has 0 rows; this does not resolve the preserved external Khamrah conflict or any hold.

## Separate candidate, reviewer, rights and transform queues

Detailed rows remain in ignored local artifacts, not public Git. Candidate/reviewer/rights matrices each contain 64 mixed-unit entries: 44 held perfume profiles, 15 media candidates and 5 pairwise leads. This is not a 64-perfume cohort. Each queue preserves original source artifact locator/hash, row ordinal where available, pinned source revision/field hash for perfume claims, exact-edition uncertainty and operation boundaries. Reviewers are explicitly NOT ASSIGNED; no approval is inferred.

The transform matrix has 43 unapproved `DPT-NOTE-MEMBERSHIP-PROPOSAL-1` sidecars: 44 repeated groups and 45 extra occurrences, comprising 39 layered and 4 general profiles. Every original array, occurrence, label, order and ordinal is preserved; within-layer candidate membership references all original ordinals. No cross-layer collapse, intensity inference, source rewriting, canonical writes, hold resolution or eligibility change is permitted. Accepting normalization requires a separately approved versioned policy and tested reviewed derivation; closure remains UNKNOWN with no absence inference.

Khamrah is separately excluded from duplicate-only normalization. Its structured/prose claims require permissioned, field/section-specific independent evidence for the exact edition plus explicit conflict review; none was acquired or resolved here.

All 15 media candidates remain metadata-only, unacquired and unusable. Filename hints are 14 JPG and 1 PNG; only 3 have historical reported dimensions, and 2 exceed the proposed 4-million-pixel bound. Extension/dimensions/page metadata cannot authenticate bytes, MIME, authorship, derivative rights or a current per-asset grant. All 5 pairwise candidates remain publisher leads across only 2 independence groups, with no accepted exact-edition, use-specific grant or independent sensory evidence; usable pairs 0. No source has gained rights through this audit.

## Next gates

- Owner review: note-list closure/absence policy, versioned repeated-note treatment, Khamrah evidence requirements, selected-field/use-specific rights, application-session binding and private/public boundary. All proposals remain proposals.
- Independent verification of this docs/evidence package, followed by coordinator reconciliation and a Draft PR; no receipt or acceptance is claimed by this worker.
- Workstream G planning defines permissioned incremental sources/media intake using these gaps. New adapters, ingestion, asset acquisition and promotion wait for the relevant Planning and source-permission gates.
- Real-data A/B1 remains disabled until accepted session/domain/closure/eligibility contracts and their positive/negative tests pass. Structural fit, Data Confidence and pairwise evidence remain separate.
