---
id: DPT-PLAN-009-DATA-READINESS
project: DoomParfum By TK
type: data_readiness_and_pilot_proposal
status: proposed
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, data-readiness, provenance, source-rights, planning]
source_of_truth: "../../README.md"
---

# Post-PR27 data readiness and five-record pilot proposal

Workstream A of [[DPT-PLAN-009_Post_PR27_Next_Wave]] consolidates the existing
[[B1_Data_Enrichment_and_Acquisition_Backlog]] and
[[IMP_MATCH_03_Data_Research_Continuation]]. It does not duplicate or approve their intake tasks.
Current coordination and exact unanswered choices belong to
[[Post_PR27_Consolidated_Next_Wave_Plan]] and [[Post_PR27_Owner_Decision_Packet]].

Starting main is `8eef8f13265adc14db0cae82ff77cfc4863853ce`, after Owner-merged synthetic M1 PR26
and synthetic B1 PR27. Those accepted synthetic contracts remain unchanged. Their merges do not
approve real-source completeness, new mappings, normalization, acquisition, application access or
real-data ranking. Historical statements in frozen B1 preparation documents retain their original
dates and scope; the separate exact Owner acceptances supersede only the synthetic-code gate.

## Actual work and evidence boundary

The existing licensed local files were read in place, outside the public repository. Six exact
file hashes and all 34 raw-field populated/missing counts were freshly checked. The A-lane verifier
passed **72/72 assertions**, with zero DB calls, network calls, source/image acquisitions, new
permission grants, canonical writes, normalization changes, hold releases or eligibility changes.
These are local aggregate/provenance checks, not independent review, runtime mapping, ETL,
database/security tests or real-data scoring. No source index or raw rows are published.

The sanitized [execution evidence](../08_Operations/Test_Evidence/Post_PR27_Data_Readiness.json)
contains each field's explicit source, revision, rights, closure, mapping, selection, eligibility
and Owner-decision status. Its verifier hash and local input hashes support reproduction without
exposing the complete source index. The ignored command is
`python .local/post27-planning/A/build_data_readiness.py` from the repository root.

| Population | Fresh local observation | What it does not establish |
|---|---:|---|
| Pinned `perfumes.csv` | 1,479 records | Current canonical perfume count, reviewed edition identity or eligible ranking candidates |
| Pinned `houses.csv` | 160 records | Verified brand identity, current canonical brands or global coverage |
| Pinned `materials.csv` | 420 records | Approved alias normalization, canonical vocabulary compatibility or actual ingredients |
| Retained projection nonheld review bucket | 1,435 records | New approval, selection, real-source closure or current DB materialization |
| Retained projection held bucket | 44 records | Permission to release any hold |
| Retained normalization proposals | 43, all `PROPOSED_NOT_APPROVED` | Accepted deduplication or alias policy |
| Independent Khamrah conflict exclusion | 1 separate source conflict | A conflict winner or a normalization shortcut |
| Retained projection activation flags | 1,479 false | Fresh DB flags; the canonical DB was not queried |
| Current canonical DB / selected rights / genuine app principal / eligibility | UNKNOWN / NOT QUERIED | No zero, availability or authorization claim is inferred |

The retained 43 repeated-note proposals still describe 44 repeated groups and 45 extra occurrences.
Khamrah remains on its independent conflicting-source route. The verifier reads those sidecars
without changing their content. A nonheld sidecar bucket is not a field-level review or a matching
permission. All 44 holds and their evidence remain intact.

## Raw-field gap matrix

A populated value is a nonempty trimmed source string. Missing means an empty source string in
that field. Neither category is a scientific truth, selected canonical fact or closed note domain.
The following counts are newly recomputed from the pinned CSV files, not copied from a database.

| Source file / field | Populated | Missing | Denominator |
|---|---:|---:|---:|
| `perfumes.csv` / `id` | 1479 | 0 | 1479 |
| `perfumes.csv` / `name` | 1479 | 0 | 1479 |
| `perfumes.csv` / `house_id` | 1479 | 0 | 1479 |
| `perfumes.csv` / `house` | 1479 | 0 | 1479 |
| `perfumes.csv` / `year` | 80 | 1399 | 1479 |
| `perfumes.csv` / `perfumers` | 69 | 1410 | 1479 |
| `perfumes.csv` / `concentration` | 1228 | 251 | 1479 |
| `perfumes.csv` / `family` | 1479 | 0 | 1479 |
| `perfumes.csv` / `secondary_family` | 1075 | 404 | 1479 |
| `perfumes.csv` / `character` | 1479 | 0 | 1479 |
| `perfumes.csv` / `seasons` | 1479 | 0 | 1479 |
| `perfumes.csv` / `times_of_day` | 1479 | 0 | 1479 |
| `perfumes.csv` / `top_notes` | 1388 | 91 | 1479 |
| `perfumes.csv` / `heart_notes` | 1388 | 91 | 1479 |
| `perfumes.csv` / `base_notes` | 1388 | 91 | 1479 |
| `perfumes.csv` / `notes` | 1479 | 0 | 1479 |
| `perfumes.csv` / `description` | 1479 | 0 | 1479 |
| `perfumes.csv` / `popularity_rank` | 613 | 866 | 1479 |
| `perfumes.csv` / `url` | 1479 | 0 | 1479 |
| `houses.csv` / `id` | 160 | 0 | 160 |
| `houses.csv` / `name` | 160 | 0 | 160 |
| `houses.csv` / `country` | 158 | 2 | 160 |
| `houses.csv` / `founded` | 97 | 63 | 160 |
| `houses.csv` / `type` | 160 | 0 | 160 |
| `houses.csv` / `portrait` | 160 | 0 | 160 |
| `houses.csv` / `perfume_count` | 160 | 0 | 160 |
| `houses.csv` / `url` | 160 | 0 | 160 |
| `materials.csv` / `id` | 420 | 0 | 420 |
| `materials.csv` / `name` | 420 | 0 | 420 |
| `materials.csv` / `aliases` | 327 | 93 | 420 |
| `materials.csv` / `material_family` | 420 | 0 | 420 |
| `materials.csv` / `origin` | 402 | 18 | 420 |
| `materials.csv` / `smell` | 420 | 0 | 420 |
| `materials.csv` / `url` | 420 | 0 | 420 |

All 1,388 raw layered profiles have nonempty top/heart/base fields; 91 have general-only notes and
blank layer fields. No partially populated pyramid shape occurs in this pinned CSV. This shape
check does **not** establish complete pyramids or absence in any blank or nonempty field. Never
distribute the 91 general-only lists among top/heart/base layers. `materials.origin` values that
say “accord” are material-category claims, not perfume accord observations or strengths.

| Additional gap | Actual pinned-source status | Required treatment |
|---|---|---|
| Explicit perfume edition field | Absent from the pinned schema | Keep name/concentration/source identity separate; exact edition is unverified |
| Real perfume accord presence/strength profile | Fields absent; zero numeric profiles available from this schema | Do not derive strengths from note order, family, descriptions or material categories; real B2 remains unavailable |
| Closure and complete-empty assertions | Not established by the raw export or this audit | UNKNOWN until an accepted source/domain/reviewer contract supplies evidence |
| Field-level current canonical selections and rights | UNKNOWN / NOT QUERIED | Require exact selected observation, source revision, caller/use rights and materialization proof |
| Seller links/prices, direct dupe evidence and image-use grants | No such fields in this pinned schema | Separate permitted evidence and intake workstreams; a source URL grants no linked-content rights |
| 93 missing material alias fields | Raw missing values | Do not infer no aliases or generate aliases automatically |
| 251 missing concentration and 1,399 missing year fields | Raw missing values | Keep unavailable, not a default edition, current year or zero |

## State vocabulary and real Matching readiness

| State | Meaning for a future reviewed input | Prohibited interpretation |
|---|---|---|
| MISSING | The source field supplies no value | “The perfume has no such note” |
| UNKNOWN | No supported conclusion, including unestablished closure | Known zero, false, empty set or complete domain |
| UNVERIFIED | A source assertion exists but its relevant identity/rights/review requirements have not passed | Selected or eligible fact |
| INCOMPLETE | Accepted evidence explicitly describes only part of the searched domain | Use as a complete negative/exclusion witness |
| CONFLICTING | Incompatible source claims remain unresolved and separately retained | First/newest/majority claim wins |
| EXPLICITLY COMPLETE-EMPTY | Accepted closed-domain evidence verifies an empty set | A blank, omitted or general-only layer |
| VERIFIED PRESENT | Exact reviewed claim, identity, selected provenance, compatible domain and usable rights pass | A globally complete list or a scientifically measured ingredient/formula |

This wave establishes raw population and retained review-state counts only. It establishes no
new real-source VERIFIED PRESENT, INCOMPLETE or EXPLICITLY COMPLETE-EMPTY canonical state. An
observed nonempty source list may still be unverified or conflict with another section/source.
M1/B1 synthetic masks/closure cannot be applied to these records as evidence of real completeness.

For every input below, source version R1 is `086769ecf1add770ea6646bd4d88d39f0e7cddeb`; source files
and exact SHA-256 are pinned below. Rights P1 means the existing pinned CC BY 4.0 local metadata
pilot, not the proposed transformation, application/public display or image intake. These common
definitions apply to each field, and the JSON evidence expands them individually for all 34 fields.

| Proposed input / source fields | Version / rights | Completeness | Canonical mapping | Selection snapshot | Matching eligibility | Outstanding Owner choice |
|---|---|---|---|---|---|---|
| Perfume identity: `perfumes.id,name,house_id,house,concentration` | R1 / P1; new preview PROPOSED | Edition identity unverified | UNKNOWN current mapping; source keys are not canonical IDs | UNKNOWN / not queried | Not authorized by this task | A exact five records; B exact field/use scope |
| Year/taxonomy: `perfumes.year,family,secondary_family` | R1 / P1; new target semantics PROPOSED | Missing year stays unknown; no closed taxonomy inference | No new release-year or family mapping accepted | UNKNOWN | Not authorized | B typed field meaning; D taxonomy/normalization decisions |
| Layer notes: `top_notes,heart_notes,base_notes` | R1 / P1 | Closure UNKNOWN even when populated | Canonical note/domain compatibility unverified | UNKNOWN | Not authorized | C source/layer closure contract; B selected claims and rights |
| General notes: `notes` | R1 / P1 | General-domain closure UNKNOWN | Cannot become pyramid memberships | UNKNOWN | Not authorized | B separate field/domain selection; C accepted completeness |
| Brand: `houses.id,name,country,founded,type,url` | R1 / P1 | Country/founding gaps remain unavailable | Country is a raw origin claim, not ISO/market classification; founding is not perfume release | UNKNOWN | Not authorized | A/B identity and field semantics |
| Material identity/aliases: `materials.id,name,aliases` | R1 / P1 | Alias-field population is not exhaustive coverage | Alias ambiguity and normalization remain unresolved | UNKNOWN | Not authorized | D versioned reviewer outcomes; no automatic acceptance |
| Material descriptions: `material_family,origin,smell` | R1 / P1 | Description/category assertions only | No perfume accords or ingredient crosswalk | UNKNOWN | Not authorized | B exact allowed claim types; D taxonomy interpretation |
| Provenance: file SHA, record ordinal, field locator, `url` | R1 / existing source rights | Capture/review timestamps not supplied by file mtime | No new entity/observation ID is created | Must later bind an actual selected observation and conflict snapshot | Not authorized | B per-field proof and permitted audience |
| Accords, direct pair evidence, image assets | Not supplied by this schema | UNKNOWN / unavailable | No invented data | No selection created | Not authorized | Separate source/asset and method approvals |

Future real-data readiness is conjunctive: exact canonical identity and vocabulary/domain version;
accepted source completeness for the searched domain; immutable selected-claim snapshot and source
provenance; active caller/use/field rights; unresolved conflict/hold rejection; approved normalization
and materialization where required; explicit matching eligibility; and genuine authorized nonadmin
access. None can substitute for another. Keep Structural Fit, Data Confidence and Direct Pairwise
Evidence separate. Do not run or publish real-data ranks, fabricate synthetic fixture identities for
real rows, weaken synthetic guards or relabel their fit as measured smell similarity.

## Exact proposed pilot: ENR-PINNED-SCENTO-1 revision 1

Status: **PROPOSED, NOT APPROVED**. Recommended first future task label is `IMP-ENR-01`, verified
unallocated in starting-main Markdown. This label reserves no implementation permission. The task
would create only a local, unselected candidate-claim review preview from existing local files.
It would not acquire a source, call a URL, change a schema/DB, promote claims or construct scorer input.

Maximum scope is exactly two perfume records, one house record and two material records: five
source records total, no additional house/material expansion while resolving tokens.

| Source file | Exact source key / source label | Data ordinal | Proposed review state |
|---|---|---:|---|
| `perfumes.csv` | `afnan-9-am` / 9 AM | 644 | Unselected preview only; canonical identity UNKNOWN |
| `perfumes.csv` | `afnan-9-am-dive` / 9 AM Dive | 645 | Unselected preview only; canonical identity UNKNOWN |
| `houses.csv` | `afnan` / Afnan | 3 | Unselected preview only; canonical identity UNKNOWN |
| `materials.csv` | `mint` / Mint | 257 | Unselected preview only; canonical identity UNKNOWN |
| `materials.csv` | `bergamot` / Bergamot | 46 | Unselected preview only; canonical identity UNKNOWN |

Ordinals are one-based logical CSV data records with the header excluded; they are not physical
line numbers or database IDs. Source IDs and labels above identify this bounded proposal, not
canonical matches. Both perfume sidecars are nonheld under the retained review bucket, with exact
edition unverified, closure UNKNOWN and activation false. This does not newly approve either record.
Mint and Bergamot are independent material review samples; their inclusion does not assert they
both occur in each perfume, or that all source note labels have been resolved by this five-record cap.

Do not confuse `afnan-9pm` (source label “9 PM Night Out”) with `afnan-9-pm` (source label “9 PM”).
They are outside this pilot and remain separate source records. Lexically similar IDs/names do not
justify an identity merge, an edition correction or canonical promotion.

| Source records | Exact allowed source fields | Proposed preview claim types / restrictions |
|---|---|---|
| Both perfumes | `id,name,house_id,house,year,concentration,family,secondary_family,top_notes,heart_notes,base_notes,notes,url` | Source identity locator; candidate name/concentration/date assertions; unselected raw taxonomy labels; separate ordered raw note fields with their original layer/general locator. No canonical membership, family choice, release-year inference or conflict winner. |
| House `afnan` | `id,name,country,founded,type,url` | Candidate house identity/origin/founding/type assertions; no ISO conversion, marketing-market coverage or perfume release date. |
| Materials `mint,bergamot` | `id,name,aliases,material_family,origin,smell,url` | Candidate material identity, ordered literal aliases, category/origin/description assertions; no alias merge, perfume accord strength or chemical-to-note mapping. |

These are exact **review-manifest claim categories**, not new SQL `field_definitions` paths. If a
target has no separately accepted canonical definition, keep it explicitly unmapped in the preview.
Do not invent a generic `source_observations` path to bypass schema or field-policy gates. The
allowlist contains 13 fields per perfume, six house fields and seven fields per material: at most
46 review field slots including identities/URLs, not 46 new canonical observations. No description,
popularity, season, perfumer, image, seller, price or linked-page fields are admitted by this pilot.

### Proposed transform and provenance contract

Transform `enr-pinned-scento-preview-1` and schema `enr-pinned-scento-preview-schema-1` are PROPOSED.
All six existing input files must match the exact byte sizes and SHA-256 below before parsing.
Their combined fixed input size is 905,307 bytes. Any changed file, revision, record count, selected
key/ordinal or field allowlist fails closed; do not silently substitute another record or revision.
No new network/input source or directory-wide import is allowed.

For each allowed source field, retain file/revision/hash, logical ordinal, source key, exact field
locator, original value state and source-order/token occurrence evidence. Preserve semicolon list
order and repeated occurrences; a proposed typed view is separate and never replaces raw evidence.
An empty source value has explicit MISSING state and no value, not zero, false, an empty known set
or a complete-domain flag. Unverified numeric/category/date meanings remain unmapped. Do not use
brand founding, Wikidata inception or a manufacturer relation as a perfume release year or brand ID.

The preview identity is the tuple `(source revision, file SHA, logical ordinal, source key,
field locator, transform version, schema version)`. A separate analysis execution time may be
recorded honestly, but file mtime or analysis time must not become a source capture/review time.
No preview auto-approves a reviewer actor, immutable observation, selection or database timestamp.
The target scope is an explicitly authorized private local review bundle; no public UI/API/cache,
external export, source rehosting, image linkage or shared-caller projection follows from it.

### Reviewer, replay and rollback requirements — NOT RUN

Human Owner designates a data reviewer independent of the future preview implementer. The reviewer
checks every selected source field against its pinned locator, edition ambiguity, target meaning,
rights and missing/conflict/repeat semantics. Each proposed claim gets a recorded
ACCEPT / REJECT / UNKNOWN / DEFER review outcome; those are dossier outcomes, not DB selections or
normalization/hold-release instructions. Require Owner acceptance of the preview scope before code,
and separate approval before any later storage/materialization/intake task.

Replay must produce identical canonical review-payload bytes/hash for the same pins, keys, field
allowlist and versions, excluding separately logged execution metadata. It may not add a sixth
source record, duplicate a claim, overwrite a prior review bundle or change a source observation.
Publish a new preview bundle atomically only after every check succeeds. On failure, retain the
failed report and leave the prior active bundle/source files untouched. Rollback means withdrawing
the new preview pointer and retaining its evidence as superseded; it is not a database restore,
source deletion, hold release or mutation of an immutable receipt.

| Future acceptance control | Required result | Current execution |
|---|---|---|
| Exact pins, five keys/ordinals and field allowlist | Positive preview accepts exactly 2+1+2 records and no unlisted fields | SPECIFIED, NOT RUN |
| Hash/revision/count/ordinal mismatch; sixth record; unlisted field | Fail before publishing any bundle; no fallback/retry acquisition | SPECIFIED, NOT RUN |
| Blank year, concentration or aliases; general-only/incomplete/unknown layer | Preserve unavailable state; no default/absence/closure or layer redistribution | SPECIFIED, NOT RUN |
| Repeated/ambiguous note, alias or taxonomy assertion; Khamrah/held input | Preserve ordered original evidence; reject out-of-scope held input and stop unsupported normalization | SPECIFIED, NOT RUN |
| Rights/identity/edition reviewer uncertainty or incompatible mapping | Mark unselected UNKNOWN/DEFER; no canonical writes, ranking or permission inheritance | SPECIFIED, NOT RUN |
| Source URL or image link | Keep a literal reference; perform zero requests or binary fetches | SPECIFIED, NOT RUN |
| Exact replay and interrupted/failed publication | Same payload hash/no duplicates; previous bundle unchanged; failed evidence retained | SPECIFIED, NOT RUN |
| Source/sidecar/DB/hold/eligibility preservation | All six source files and retained review sidecars unchanged; no DB connection or write | SPECIFIED, NOT RUN |

### Source pins and attribution

| Existing local file | Bytes | SHA-256 |
|---|---:|---|
| `perfumes.csv` | 780683 | `726a1a2af8aef42d801b424b086415b50f6ca33dd2189d6fbd2bcbcb442bf8e5` |
| `houses.csv` | 29765 | `f076db1629fc1c07fe417811a55891bbfe70991319bf5c520766253f80cc9c18` |
| `materials.csv` | 87027 | `9b342c803f0b370e96106a4dff0ae56f1f5340bdc82c6e32d180473a9f31764c` |
| `LICENSE` | 188 | `7be5a0aac3f6a1803ae0a950624941a74b4a17c54ab3c9272ef8f61ebb8efc84` |
| `README.md` | 2799 | `c925d4b50cefde8038706125e9296d07270ca98bd6bcafd079ced9a77cf5c688` |
| `datapackage.json` | 4845 | `c4f072d7486a9f64b24502b7b53862e9fad61a2d79943d0ae6525d97f3f30bc2` |

Source attribution: **Scento — [Scento Perfume Database](https://www.scento.com/perfume-database)**,
dataset revision `086769ecf1add770ea6646bd4d88d39f0e7cddeb`,
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as asserted by the retained pinned
`LICENSE`. This note derives aggregate counts and proposed review mappings; raw files are unchanged.
Retain source/license links and identify any later transformations. This evidence does not grant
rights to live API replication, linked publisher prose/images, new revisions or public application
publication. Per-field source/use/audience review and applicable approvals remain separate.

### Exact proposed Owner approval text

> I approve ENR-PINNED-SCENTO-1 revision 1 and future IMP-ENR-01 only for an offline private review
> preview using the six pinned files at revision 086769ecf1add770ea6646bd4d88d39f0e7cddeb, their exact
> hashes/sizes, the five source keys/data ordinals and field allowlists in the reviewed DPT-PLAN-009
> planning revision. I accept proposed transform enr-pinned-scento-preview-1 and schema
> enr-pinned-scento-preview-schema-1 for unselected candidate-claim output and designate an independent
> data reviewer before implementation. Applicable Planning Gate must be merged before coding.
> This approval excludes network/source acquisition, database/schema/role changes, canonical or
> normalization promotion, hold release, matching eligibility, real-data ranking, media, API/UI,
> publication, cloud and Production. Any changed keys, fields, pins, meanings or scope require a new
> exact decision. Implementation returns as its own Draft PR for Human Owner review.

Alternative: DEFER the preview and continue existing-source dossier review only. Neither choice
approves real completeness, selected-field use beyond the exact preview or any of the 43 proposals.

## Regional evidence and permission backlog

This is an offline reconciliation of [[Regional_Source_and_Media_Permission_Dossiers]],
[[Source_Acquisition_Permission_Research]] and the existing brand registry. The retained seed aggregate
reports 15 Thai, 16 Indonesian and 31 Middle Eastern candidates; those are research-queue counts, not verified
regional brands, canonical population, permitted feeds or a worldwide denominator. The pinned raw
house-country claims contain no Thailand/Indonesia entries; that observation is not proof those
brands are absent from the real market. Current publisher terms and actual grants are NOT
REVALIDATED in this wave. No request, account, API entity sample, product page or permission message
was sent or acquired. All prior access restrictions, endpoint failures and unresolved rights remain.

| Existing candidate / priority | Retained evidence and unresolved boundary | Next bounded proposal; no execution approved |
|---|---|---|
| Thai TH01 SIAM 1928 | Historical official indexed terms locator; direct terms open timed out; retained IP-use restriction and no field/feed grant | Ask Owner whether to authorize an exact publisher/rightsholder contact and at most five publisher-selected SKUs. Need method/field/edition/storage/display/transform/update/retention/audience permission; images separate. No retry/bypass now. |
| Thai TH03 SÚNDALO | Historical first-party presence, exact content-reuse/API terms unresolved | Resolve actual publisher authority and terms before any export/sample request; contact itself needs Owner instruction. |
| Thai SCENTERY / BE CHERIE PARFUM / La Palette | First-party identity/URL insufficient or ambiguous in retained registry | Identity/rightsholder dossier first; marketplace or similarly named-house references are not permission or canonical identity. |
| Indonesian ID01 SAFF & Co. | Retained terms require express written service-use permission and prohibit spider/crawl/scrape | Seek an Owner-authorized permissioned export request; no automated website extraction. |
| Indonesian ID02 Mykonos | Retained terms reserve data/images/descriptions; written-use permission required; applicable catalogue grant not established | Separate exact data and media permission questions and a maximum-five-record export proposal. |
| Indonesian ID03 HMNS | Official contact reference retained; substantive content-use/API terms not verified | Verify rights authority and request scope only after Owner authorizes contact; no product or order payload. |
| Middle Eastern ME01 Lattafa | First-party terms retained; no applicable third-party data/media feed grant | Exact edition/field export and separate image permission; Khamrah conflicts remain held even if new evidence is later obtained. |
| Middle Eastern Fragrance World | Retained terms require prior written reproduction/distribution/modification/derivative permission | Ask for a publisher-selected export and exact operation/use grant, not a website crawl. |
| Existing Wikidata brand-identity proposal | General structured-data CC0/access route; no approved entity sample or verified perfume coverage | At most five reviewed entities only after exact method/budget/field approval. P571 inception is not automatically release year; P176 manufacturer is not automatically brand. Linked text/images have separate rights. |
| OBF applicability proposal | Access restriction and actual perfume-identity/sample relevance unresolved | Keep blocked; no alternate route, bypass, broad dump or INCI-to-note/family/accord conversion. |

No regional queue is promoted, discarded or counted as a licensed catalogue. Any future permission
must identify publisher authority, exact fields/assets/revisions, allowed automation/retrieval,
storage/display/transforms/redistribution/updates, audience, attribution and retention/revocation
conditions. Owner task approval and third-party permission are both necessary where applicable;
neither substitutes for the other. No new contact or acquisition is implied by this backlog.

## Deliverable status and next executable action

| A deliverable | Actual state | Remaining gate |
|---|---|---|
| Fresh local source pins, 34 field counts and retained review-state verification | DONE: 72/72 local assertions | Not a current canonical DB or rights audit |
| Field/state/readiness matrix and exact five-record proposal | DONE as planning | Owner exact A/B decisions and merged planning scope before preview implementation |
| Regional permission/identity backlog reconciliation | DONE as existing-evidence analysis | Current terms/grants/samples and any contact/acquisition require separate approval |
| Current canonical selections, app session, real-source closure and real Matching | UNKNOWN / BLOCKED / NOT RUN | Independent selected-field, source-rights, completeness, normalization/hold, eligibility and genuine-principal gates |
| New preview/adapter/ETL/DB work or image bytes | NOT STARTED | No implementation or acquisition is authorized in this wave |

Recommended first future implementation is the exact five-record **offline unselected preview**,
after Owner acceptance and Planning Gate, independent of media readiness or Docker availability.
Do not couple it to real-data matching, a web stack or an authenticated application. Broader
DM/OP choices remain PROPOSED except the separately accepted synthetic M1/B1 contracts and existing
scoped local-data decisions. The consolidated packet owns the final exact Owner response.
