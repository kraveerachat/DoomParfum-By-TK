---
id: DPT-DATA-005-NOTE-AUDIT
project: DoomParfum By TK
type: observed_data_audit
status: scoped-review-ready
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, notes, vocabulary, pyramid, closure, audit]
source_of_truth: "../../README.md"
---

# Observed note vocabulary and matching-input readiness

Same observed baseline as [[Catalogue_and_Brand_Completeness_Audit]]: main
`8c6a8376680c7a10cc3eb4b5cf80afe4376a9282`; fresh coordinator aggregate at 2026-11-13 20:04Z,
source revision `086769ecf1add770ea6646bd4d88d39f0e7cddeb`. This lane reads local artifacts only,
with zero DB/network calls and no canonical/normalization/permission change. Public tables are
aggregates; the420-row vocabulary and44-row hold queue remain ignored local files, outside Git/ZIP.

## Note_Vocabulary_Audit

All420 canonical note UUIDs are unique and approved; all420 have source display names. The source
name field is used for the English-facing label; no new language verification/translation is
asserted. There are0 Thai names,0 canonical alias rows,0 typed material_origin values,0 canonical
descriptions and0 note images. These missing values are actual target gaps, not chemical absence.

| Note field | D | Canonical populated / missing | Raw populated | Approved selected | Held note entities | Selected local-use / app | Unknown target |
|---|---:|---|---|---|---:|---|---:|
| UUID | 420 | 420 /0 | 420 IDs | NA identity | 0 | identity scope separate /0 | chemical/semantic equivalence not measured |
| Source/English-facing display name | 420 | 420 /0 | 420 | 420 | 0 | 420 source grant linkage;field-local use not separately re-executed /0 | 0 source-name slots |
| Thai display name | 420 | 0 /420 | NC dedicated Thai field | 0 | 0 | 0 /0 | 420 |
| Aliases | 420 | 0 /420 with canonical aliases | 327 records | 0 | 0 | 0 /0 | 420 canonical alias targets |
| Description | 420 | 0 /420 | smell420;not an accepted description mapping | 0 | 0 | 0 /0 | 420 |
| Typed material_origin | 420 | 0 /420 | origin402 free-text records | 0 | 0 | 0 /0 | 420 typed classifications |
| Material family | 420 | NM dedicated canonical column;contract path exists | 420 | 0 | 0 | not established /0 | 420 canonical targets |
| Raw smell | 420 | NM separately materialized smell column | 420 | 0 | 0 | not established /0 | 420 canonical targets |
| Illustration/asset | 420 | 0 /420 with image links | NC licensed asset bytes | 0 | 0 | 0 /0 | 420 |
| Source record/locator/revision | 420 | source record bindings420 /0 missing in source cohort | 420 source URLs | NA provenance identity | 0 | active source-local assessment;not public or app permission /0 | no new right inferred |
| Canonical membership use | 420 | 417 /3 with memberships | all420 used in raw flat lists | approved-source lookup uses417 | 0 note entities;44perfumes held | not matching eligibility /0 | 3 without canonical links |

The audit counted1,635 alias tokens in327 source material records,1,626 distinct normalized tokens
and9 repeated tokens within their own material records. Under the **offline NFKC+lower literal
predicate**, duplicate primary-name groups=0, cross-material alias groups=0, combined name/alias
ambiguity groups=0. All12,448 raw perfume flat-list occurrences resolve unambiguously within this
dictionary; unmatched labels=0 and ambiguous labels=0. This narrow syntactic result does not
establish semantic synonymy, language, safe fuzzy mappings, material identity or accepted aliases.
No alias token or source occurrence was deleted or promoted.

All420 raw materials appear in the full source. Source analysis confined to the1,435 non-held
profiles uses417 materials;3 occur only among held profiles. This reconciles the canonical417
membership count without deleting the unused dictionary entries. Count agreement is not a new
row-level database export or a grant to make held notes canonical.

The source's17 material_family categories are label classifications, not perfume accord strengths:
Floral56,Gourmand55,Fruit49,Wood40,Aromatic herb32,Green29,Spice26,White floral25,Citrus18,
Resin & incense16,Musk15,Earth & moss14,Marine & mineral13,Smoke & leather13,Powdery9,Amber9,Oud1.
The typed canonical enum natural/synthetic/both/accord is unpopulated. No count of natural materials
or accord-like notes is inferred from these source categories; notes are declared/perceived labels,
not a disclosed chemical formula or verified ingredient list.

## Pyramid_Coverage_Report

Profile denominators below are all1,479 source/operator profiles; token/link counts are a different
unit. Held-populated source memberships do not become canonical links. Raw3-layer shape exists in
1,388 profiles;91 are flat-only. Approved selected representations are1,348 layered +87 general.

| Representation | Raw profiles | Canonical selected profiles | Canonical missing profiles | Held source profiles | Raw token occurrences | Canonical links | Held raw tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top | 1388 | 1348 | 131 | 40 | 3850 | 3693 | 157 |
| Heart/Middle | 1388 | 1348 | 131 | 40 | 3873 | 3742 | 131 |
| Base | 1388 | 1348 | 131 | 40 | 4305 | 4150 | 155 |
| General for flat-only profiles | 91 | 87 | 1392 | 4 | 420 | 387 | 33 |
| Representation totals | 1479 distinct profiles | 1435 distinct profiles | 44 unapproved profiles | 44 | 12448 | 11972 | 476 |

Top/Heart/Base profile rows overlap and must not be summed as distinct perfumes. The raw notes
flat column is populated in all1,479 profiles and carries12,448 occurrences, often mirroring the
pyramid. It is not an additional12,448 links to add to the representation totals. The raw-versus-
canonical difference476 is exactly the raw flat occurrences on the44 held profiles; the independent
approved-source representation counts agree with all four canonical layer-link totals.
This is an accounting reconciliation, not a new normalization or claim of complete domains.

No explicit complete-empty or accepted complete-as-reported assertion was established by this audit.
No closure table/accepted policy exists to turn raw presence into that proof. A missing Top/Heart/
Base field, an omitted note, a flat-only profile or a0-valued missing score never proves absence.
Order/repetition is not intensity. Cross-layer repetition must remain distinct layer membership.
All measured selected-layer local-use counts equal their selected-profile counts above; operational
application accessibility is0 for every layer, and actual matching eligibility remains0/1,479.

## Accord_Family_Gap_Report

| Target / denominator | Raw observation | Canonical / selected observation | Remaining gap |
|---|---|---|---|
| Primary family /1479 perfumes | 1479 nonempty family strings | family rows/links/selected field0 |1479 profiles lack canonical family association;taxonomy/mapping review required |
| Secondary family /1479 |1075 nonempty strings,404 raw missing |0 selected values |1479 canonical targets unavailable;raw404missing is a separate measure |
| Accord label/presence /1479 |no dedicated structured accord column |accord rows/links0 |do not infer presence from family or note text |
| Observed accord strength /1479 |no structured measured-strength column |0 canonical values |no compatible reviewed numeric scale/domain;real B2 unavailable |
| Material family /420 notes |420 labels across17 categories |0 selected material_family claims |not interchangeable with perfume family or accord strength |

The measured SQL field contract is perfume family; supplemental families.primary/secondary paths
also exist, but no selection under any of them was found. Zero canonical families must not be
reported as zero raw family information. Notes, family strings, material family, accord presence,
observed strength and pairwise comparison evidence remain separate data classes and separate gates.

## Normalization_Review_Queue

| Bounded review group | Profiles | Evidence accounting | Current state |
|---|---:|---|---|
| Proposed layered repeated-membership projection |39|source arrays/ordinals preserved |PROPOSED;held unchanged |
| Proposed flat/general repeated-membership projection |4|same within-domain policy proposal |PROPOSED;held unchanged |
| Total projection cohort |43|44 repeated groups /45 extra occurrences |0 transforms applied;no reviewer acceptance |
| Khamrah structured/prose conflict |1|independent contradictory source claims |held;not resolved by projection,majority or newest timestamp |
| All held profiles |44|476 source flat occurrences;separate from alias-token duplicates |0 holds released;eligibility unchanged |

The9 repeated alias tokens in the material vocabulary are a different population from the45
extra occurrences in the43 perfume projection proposals. They must not be conflated. Current
database data_conflicts count0 does not close Khamrah's externally recorded source disagreement.
Required transform/version, exact source/section lineage, reviewer, selected claim, rights binding,
negative/replay/rollback evidence remain unresolved implementation gates; no proposal is applied.

## Completeness_Closure_Decision_Matrix

| Domain / population | Observed positive evidence | Closure/absence assertion | Consequence now |
|---|---|---|---|
| Exact Top/Heart/Base /1479 each |raw1388,selected1348 each |not established by populated list;accepted domain mask/reviewer/version absent |unlisted note cannot satisfy strict exclusion |
| General /1479 |91 source flat-only,87 selected |flat list completeness not accepted |do not reassign to pyramid layers or infer negative membership |
| Any-layer query /1479 |selected positive links across accepted representation only |all searched-domain closure not established |one layer's known presence/missingness cannot prove any-layer absence |
| Complete-empty domain |no accepted explicit empty assertion measured |not established;empty/null/omitted are not equal |no perfect empty-empty fit or automatic strict-rule satisfaction |
| Family/accord domains |raw families exist;canonical associations0 |taxonomy/domain/scale compatibility unresolved |no full-component or B2 capability |
| Changed capture/normalization/rights |original lineage retained |old assertion applicability would require re-review |no silent extension across captures,users or purposes |

These are **observed missing decision/evidence states**, not a claim that an unmodeled closure
table contains0 rows. The Owner's high-level no-inferred-absence direction is confirmed; exact
assertion identity, policy/version/missingness and implementation authorization remain PROPOSED.
Existing transition and method documents define future contracts; this audit executes none.

## Matching_Input_Readiness_Report

| Required input/gate | Actual current evidence | Ready now? |
|---|---|---|
| Bounded pinned source inventory |1479/160/420 files and1,479 index external keys verified |YES for existing local-source audit only |
| Approved selected names/brand links |1435/1479 profiles;44held |partial source-exact input;not all-profile matching |
| Positive selected note representation |1348pyramids+87general;11972links,417notes |available under existing operator/local assessments;closure separate |
| Note language/alias enrichment |Thai/alias/description/image canonical0 |NO accepted enrichment;do not invent translations or merge tokens |
| Family/accord inputs |1479/1075raw family strings;canonical families/accords0 |NO compatible canonical component or strength scale |
| Closure and normalization |43proposals,Khamrah and exact assertion policy unresolved |NO strict absence or promotion |
| Source/use rights |2059 source records active for existing local operations;redistribution restricted |existing local scope only;no new app/public/image right |
| Actual application binding |0 real-catalogue nonadmin-bound profiles |NO;operator query is not application capability |
| Full scorer/exact DM policy |generic primitives and proposed method goldens only |NO full accepted A/B1 method;real B2 unavailable |
| Matching eligibility |0/1479 true |NO activation;flag alone would still be insufficient |

Next observed-data priorities are reviewed source-to-field mappings, Thai-priority permissioned
coverage, alias/language review, explicit closure/normalization decisions and genuine session
binding. No score, alias mapping, family, asset, permission or database row was created. Full method,
SQL/RLS/negative/replay/rollback/app/relevance tests remain NOT RUN in this audit lane.
[[DPT-DATA-005_Audit_Evidence]] contains exact quantitative and documentation evidence.
