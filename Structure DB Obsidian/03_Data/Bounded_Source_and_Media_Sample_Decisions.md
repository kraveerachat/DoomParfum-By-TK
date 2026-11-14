---
id: DPT-DOC-003-SOURCE-MEDIA-UNLOCK
project: DoomParfum By TK
type: bounded_intake_decision_proposal
status: proposed
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, sources, media, permissions, owner-decisions]
source_of_truth: "../../README.md"
---

# Bounded source and media sample decisions

## Current authority and evidence boundary

This is a focused decision delta within existing Draft PR25, not a new adapter or duplicate
Planning PR. Merged [[Incremental_Source_Adapter_and_Media_Intake_Plan]] already defines intake,
claim/selection, media and revocation contracts. Its Owner merge at
`4560b53945d111a51e231a2b477cb0b8a194546f` did not select every source, sample or format.
The current main is `8c6a8376680c7a10cc3eb4b5cf80afe4376a9282`. Owner direction is confirmed;
the exact SOURCE-01, MEDIA-01/02, APP-01 and PUB-01 choices below remain **PROPOSED**.

PR24 candidate evidence is pinned to `8c04fcdc9384955d2e49eefcd9f54c1ebd462378`, still unmerged:
`Source_Inventory_and_Operation_Audit.md` and `Media_Asset_Readiness_Audit.md`. It reports25dossiers,
275eleven-operation states and a separate22-row historical rights registry. The six approved
states apply only to existing pinned-local metadata uses;20conditional/189unknown/56restricted/
4not-verified states create no executable acquisition task. Do not join colliding SRC codes across
those artifacts without publisher plus artifact/version/hash identity.

The recorded PostgreSQL audit is historical as of2026-11-14 03:04 Bangkok. This wave's Docker
recheck found the daemon unavailable; current DB counts and role state are **NOT REVALIDATED**.
The recorded media denominators remain1479perfumes/420notes, with0canonical image links/assets
and20leads(15note illustrations/5bottle identity leads). These are dated observations, not new
database measurements. Keep all44holds, observations, source permissions and eligibility unchanged.

## Source Acquisition Candidate Matrix — recommended order

The following are source routes, not approved grants or a promise that each route covers a field.
Primary URLs are retained from merged dossiers; this pass made0external requests and does not
claim current remote terms, endpoint availability or coverage verification.

| Route / publisher and exact source reference | Candidate fields / credit | Access, version and refresh | Permission boundary / next decision |
|---|---|---|---|
| S01: Scento, [pinned dataset](https://github.com/Scento-com/perfume-dataset/tree/086769ecf1add770ea6646bd4d88d39f0e7cddeb) | Existing names, house country/founded/type, notes, descriptions and family labels; Scento/source/revision, [CC BY4.0](https://creativecommons.org/licenses/by/4.0/), change notices, no endorsement | Read the existing verified local files only; immutable revision086769ecf1add770ea6646bd4d88d39f0e7cddeb; no live update/cursor or new download | Recommend the exact field-mapping sample below. Existing local pilot approval is not an accepted taxonomy, new app/display right, canonical promotion or image grant |
| MD01: Wikidata, [licensing](https://www.wikidata.org/wiki/Wikidata:Licensing), [data access](https://www.wikidata.org/wiki/Wikidata:Data_access), [API etiquette](https://www.mediawiki.org/wiki/API:Etiquette) | Candidate structured entity IDs and referenced origin claims; preserve entity/revision/statement/reference provenance | Official documented metadata route only after exact entity, namespace, request budget and task approval; store returned revision/hash; no scheduled refresh selected | Historical structured-data CC0 path is conditional project evidence. Identity/edition coverage untested; surrounding text and linked images are separate. Defer entity requests until exact identity/use is accepted |
| Regional first-party publisher, starting with the existing15Thai A-priority research entries | Candidate names, official site, exact edition, concentration, year, pyramid or family claims; publisher-specific credit required | Exact approved publisher URL/feed/version/method and finite sample must be named first; no catalogue/product request or refresh budget is approved | UNKNOWN per intended operation until usable terms/grant and sample verified. A public site or first-party identity does not authorize automation, storage, transformation or display |
| S02: Scento live API, [documentation](https://www.scento.com/developers/perfume-api), [terms](https://www.scento.com/terms-of-service#perfume-api) | Documented lookup metadata; Scento link/credit and selected field-use review | Separate live contract, never inherit pinned snapshot permissions. No route called; revision/refresh and durable storage use unaccepted | Historical terms prohibit wholesale competing-catalogue rebuilding/limit evasion. Defer; do not use this route to recreate the existing1479snapshot |
| MN01: Wikimedia Commons exact file/page evidence | Candidate ingredient illustration attribution/license/creator/file lineage; one selected license and complete credit | Exact revision and upstream file identity per candidate; no automatic image download, image-link traversal or scheduled refresh | Page hosting, search results and metadata license do not establish binary ownership or intended use; metadata-review proposal below only |
| MN03: The Met, [image policy](https://www.metmuseum.org/policies/image-resources), [terms](https://www.metmuseum.org/policies/terms-and-conditions), [FAQ](https://www.metmuseum.org/policies/frequently-asked-questions-image-and-data-resources), [API docs](https://metmuseum.github.io/) | Potential objectID/isPublicDomain/objectURL/creditLine/artist/title/metadataDate and image references; retain credit/license provenance | Future exact object/revision and bounded metadata task needed; no search/object/image endpoint called or refresh selected | Historical conditional OA path requires exact eligible object/file and relevance review. Non-OA and other rights remain separate; JPEG compatibility is not approved |
| MB01/MN04: actual owner-created or commissioned bottle/note image | File-specific author/rightsholder evidence, subject/edition and agreed uses/credit | No file supplied; source URL/local identifier, version/hash and review evidence UNKNOWN; no acquisition/refresh | Ownership of perfume is not authorship of its photo. Obtain an actual license/attestation covering each use and third-party rights; do not preapprove a hypothetical asset |

Fragrantica's historical DENIED restrictions remain intact. Shopee and other unapproved sites
receive no scraping, account/cart access or automation here. No source payload, site crawl, paid
service, contact, login, external tool installation or image acquisition was performed.

### Operation-specific use ceiling

| Operation | S01 exact local sample | New source/asset route now |
|---|---|---|
| Discovery/enumeration | Existing pinned file/key inspection only | Exact inventory/source task and method must be accepted |
| Automated access | No network; existing local read only | UNKNOWN/CONDITIONAL is not execution permission; respect explicit denials |
| Storage | Existing licensed local snapshot, separate proposed review manifest | No new raw/image storage grant inferred |
| Local research | Existing licensed pilot scope | Metadata-only research can document unknown rights without acquiring payloads |
| Internal application display | Existing local-use evidence does not supply an app principal or new use | Source field-use plus genuine authorized nonadmin binding required |
| Image acquisition | Not supplied by dataset grant | All20leads remain blocked until file-specific evidence and exact task pass |
| Transformation | Proposed mapping only; originals untouched; no accepted mapping/selection | Exact derivative/normalization permission and reviewed version required |
| Caching | Existing local pinned-copy scope only | No shared cache; use/audience/retention rights unaccepted |
| Redistribution | No new public raw export or transfer | Existing restrictions retained; do not extend a local grant |
| Public publication | Not authorized by sample/roadmap | PUB-01 and source/privacy approvals required separately |
| Scheduled updates | Not applicable to immutable pin; no scheduler | Separate accepted refresh method/budget/terms and delta review required |

## Field Coverage Gap Matrix — acquisition routing only

Numbers and detailed denominators belong to the coordinator's dated24-field matrix and PR23
candidate audit. This table adds the route and stopping condition; it does not remeasure counts
or claim that an untested source supplies a missing value.

| Field ID / required field | First route or existing raw evidence | Hold before any new canonical/application use |
|---|---|---|
| 01 Perfume name | S01 existing source name/key | Exact edition/identity and selected-use review; do not merge names |
| 02 Brand name | S01 house name/key; regional/MD01 identity prospect | Cross-source identity/alias and provenance review |
| 03 Edition/flanker | No dedicated S01 edition column; flanker model exists but observed rows0 | Exact publisher edition evidence and directed relationship review |
| 04 Concentration | S01 populated claims; licensed exact-edition source for gaps | Keep EDT/EDP/extrait distinctions; no suffix inference |
| 05 Release year | S01 sparse claims; permissioned publisher for gaps | Year is not stock/current production |
| 06 Gender/intended audience | No dedicated S01 field | Source-supported label/use and mapping approval, otherwise unknown |
| 07 Top notes | S01 exact arrays and ordinals | No deduplication, intensity or closure inference |
| 08 Middle notes | S01 heart arrays and ordinals | Retain layer identity and cross-layer occurrences |
| 09 Base notes | S01 exact arrays and ordinals | Preserve holds/conflicting prose and structured claims |
| 10 General notes | S01 flat strings/flat-only representation | Do not add mirrored flat list as another pyramid layer |
| 11 Note aliases | S01 materials aliases | Versioned language/semantic/identity review; literal resolution is not acceptance |
| 12 Note descriptions | S01 smell/origin prose | Description/typed-origin mapping is not yet accepted |
| 13 Main accords | No compatible structured S01 accord observations | New permitted source plus reviewed taxonomy/domain/scale; no invented strength |
| 14 Perfume families | S01 primary/secondary labels retained | Taxonomy/field/materialization approval, not material-family substitution |
| 15 Country of brand | S01 house country labels | Country-code/identity interpretation; no market-availability inference |
| 16 Source provenance | Existing file/key/revision/claim locators | No bare SRC-code join; capture/hash/use/selection identity required |
| 17 Bottle images | Five existing identity leads or actual owner-created file | Exact file/edition/rightsholder/license/use/format checks |
| 18 Note illustrations | Fifteen historical leads; Commons/Met prospect | Illustrative purpose and exact asset rights, never chemical proof |
| 19 Similarity/pair evidence | Five unpromoted leads | Independent permissioned pair claim/provenance; no score invented from a link |
| 20 Purchase-source references | Separate private manual/approved listing contract | Seller-specific provenance/privacy; no checkout/account automation |
| 21 Price observations | Separate dated seller/currency/market observation | Permissioned exact listing/time and update policy; unknown is not0 |
| 22 Regional coverage | Existing15Thai priorities and220seed+6candidate research cohorts | Bounded approved publisher universe; origin/market/brand coverage distinct |
| 23 SKU/edition coverage | S01 lacks dedicated GTIN/SKU/size inventory | Permissioned exact edition/packaging identifiers and source denominator |
| 24 Field-level permissions | Existing local assessments plus per-source/use evidence queue | Active selection/source/field/scope/audience rights and app binding; no inherited grant |

## Small Sample Intake Proposal — SOURCE-01 exact recommendation

**Proposal ID `SRC-SAMPLE-PINNED-FIELDS-P1`, not accepted or executed as an intake.** Prefer a
local review manifest for already licensed metadata before adding a new remote adapter:

- Input: exactly one `houses.csv` record with source key `dior` and two `perfumes.csv` records
  `dior-addict`, `dior-addict-eau-fraiche`, at pinned revision086769ecf1add770ea6646bd4d88d39f0e7cddeb.
  These source keys were checked locally in this documentation pass. Their selection is a
  deterministic bounded proposal, not perfume/brand identity approval or a current DB lookup.
- Fields: house id/name/country/founded/type and source URL; perfume id/name/house_id/family/
  secondary_family/description and source URL. Preserve blanks as unknown. No new note transform,
  catalogue identity, enum assignment, family taxonomy or official-site inference.
- Budget:3existing logical CSV records,0network requests,0new image bytes,0DB calls,0canonical
  writes. These are proposed sample limits, not installed runtime defaults. Keep local working
  output outside public Git and outside the handoff's approved public evidence exports.
- Proposed output: a review-only manifest with file/revision/hash/logical ordinal/field locator,
  original value reference, proposed target, mapping unknowns, intended existing local-research
  use and reviewer decision. No new adapter: the existing full snapshot/index is already present.
- Required acceptance: Owner selects this exact bounded review scope; source/license/change
  attribution verified; reviewers distinguish raw country/type/family labels from accepted
  canonical codes/taxonomies; field-use scope and future implementation task are explicit.
  Actual SQL/materialization/selection waits for its own accepted mapping and tests.
- Stop: any wrong pin/hash/key/house link, missing required provenance, edition ambiguity,
  contradictory claim, unaccepted target mapping/use, app identity request or promotion request.
  Do not substitute records, fetch a newer source or choose the newest claim silently.
- Negative/replay specifications, **NOT RUN**: reject one altered source byte/revision/key or
  wrong house binding; preserve absent secondary family as unknown; reject use as verified
  official URL/current market/accord strength; deterministic identical manifest on replay;
  no writes on rejection. Snapshot hash checks in this documentation pass are not intake tests.

Alternative: explicitly defer this mapping sample and review a single exact Wikidata structured
identifier sample only after its entity/namespace/use/request budget is accepted. Do not swap
to live Scento, expand the record count or infer a regional feed grant. A sample decision does
not release holds or confer application display/publication permission.

### Executed offline field-inventory rehearsal — narrower permitted preparation

Existing licensed-local data-preparation authorization permits inspecting already local records
without acquisition or canonical mapping. This pass actually inventoried the two source profiles
and their one parent-house reference, using the immutable file hashes above. The private output
records exact source/file/revision/logical ordinal, parsed-record SHA256, original-field string
hashes and presence flags. The parsed-record hash is canonical JSON of unchanged parsed strings,
not a claim about lexical CSV row bytes; exact source-file bytes are hashed separately.

Actual result:18/18bounded local artifact assertions PASS,0failures;2profile records,1supporting
house record,0network requests/DB calls/writes/acquisitions/normalization/rights changes. All three
source file hashes were unchanged before/after. Presence detection uses trimmed emptiness only;
it does not modify the stored source strings or their hashes.

| Field group / two-profile denominator | Raw populated | Raw missing |
|---|---:|---:|
| id/name/house_id/house/concentration/family/character/seasons/times_of_day/notes/description/url |2each|0each|
| year/perfumers |0each|2each|
| secondary_family/popularity_rank |1each|1each|
| top_notes/heart_notes/base_notes |1each|1each|

These groups account for all19perfume CSV columns. They do not revalidate1479DB profiles, prove
closure or give missing year/perfumer values. No substitute is inferred from outside knowledge.
Both source house links match the one selected source house; no canonical identity or selection
was checked. The future proposed mapping/intake/SQL/permission decisions remain unaccepted.

Sanitized proof `.local/post2225-CD/SOURCE_FIELD_REHEARSAL_PUBLIC.json` SHA256
`93fccb7866f0e90a24c3758b6575fcd6c8a4eb6fd1dba6bee51f57563417055a`;
checker SHA256 `7fa43504a13010bccaed42215e3151d9dd3298f7fd9f5a74e8a680299d316fa2`.
The detailed two-record payload `SOURCE_FIELD_REHEARSAL_PRIVATE.json` stays ignored and must be
excluded from public Git and the handoff ZIP. The initial helper mistakenly expected20source
columns, confusing an earlier20-field audit matrix with the actual19-column CSV. It stopped
before output/data mutation; failure and correction are preserved locally. Correcting that
checker assumption did not change source values or conceal an intake/runtime failure.

## Media Intake and Rights-Verified Asset Plan — MEDIA-01 recommendation

**Proposal ID `MEDIA-REVIEW-JUNIPER-P1`: one existing note-illustration lead, metadata/rights
review only.** This is a proposed approval request, not an already approved sample or file grant.
Use existing exact description-page evidence for
[File:Juniper berries 777.jpg, revision1142894283](https://commons.wikimedia.org/w/index.php?title=File:Juniper_berries_777.jpg&oldid=1142894283).
Its stored page-text SHA256 is
`9037b3593449e459b86992dad757acbd1bd9db0853883728bdc2c13628a509d2`; that is not an image hash.

| Asset dossier field | Current evidence / proposed required result |
|---|---|
| Subject / association | Proposed ingredient illustration only; exact canonical-note association needs review; no chemical or bottle-edition assertion |
| Source/version | Exact Commons description revision above; actual upstream file version/ownership chain still needs authentication |
| Creator/rightsholder | Historical creator assertion is not authenticated ownership; verify actual author/authority and upstream provenance |
| License | Historical CC BY2.0/FlickreviewR references are not a selected authenticated grant; inspect exact license/conditions and other rights |
| Attribution | Build verified creator/title/source/license/change notice for the selected valid license; do not reuse unverified text as a grant |
| Allowed download/storage | NOT APPROVED;0binary acquisitions. Any later exact file acquisition needs its own explicit task and usable rights |
| Allowed transformations | NOT APPROVED; cropping/resizing/conversion/metadata stripping are separate uses and technical scope |
| Private display | NOT APPROVED; requires exact file/use/audience rights and genuine authorized app binding |
| Public display/redistribution | NOT APPROVED; PUB-01 and source/file/privacy boundaries remain separate |
| Cache/retention/refresh | UNKNOWN/unselected; no shared cache or scheduler; retain evidence under permitted local research policy only |
| Withdrawal/revocation | Verify current project assessment, ownership complaints and restrictions before use; stop affected operation; preserve lineage. A changed page is not automatic revocation of a compliant copyright license |
| Dimensions/MIME | Actual binary values NOT VERIFIED; filename/report metadata is not sniffed MIME, decoding or pixel-budget proof |
| Content hash | Downloaded binary SHA256 NOT AVAILABLE; page-text hash/source-reported SHA1 cannot substitute |

Proposed future dossier budget:1existing candidate, at most2public primary metadata/permission
references if the Owner approves the exact follow-up task,0image payloads,0DB/canonical writes,
0public delivery. A redirect to a binary, authentication, deny/timeout/rate restriction, unresolved
ownership/license, absent exact file binding or an expanded use stops that task. Do not retry a
historically denied source or treat a failed extraction as proof that no license exists.

Only after a dossier passes may an independent future acquisition task name the exact asset,
download/storage/audience/derivative permissions, byte/pixel/MIME budgets and tested format path.
It must bind source/capture/asset/rights/scope and parent lineage as already planned. Future negative
tests must reject wrong capture/file/rightsholder/use/ancestor, expired or withdrawn project grant,
private cross-user access, over-budget bytes/pixels, mismatched MIME/hash and restore reactivation
of restricted assets. These are specifications, **NOT RUN** in this documentation pass.

Alternative bottle sample: exactly one actual owner-created photo, after actual authorship and
other-rights attestation plus allowed uses are supplied. No file, creator identity, source/version,
license, MIME/dimensions or hash is supplied now; ownership of a perfume is insufficient. An
illustration sample never authorizes the five bottle leads, and a bottle approval never grants
the15note leads. No new lead is inserted into those queues here.

## MEDIA-02 format choice and placeholders

Keep the existing `local-static-png-v1` technical boundary: static8-bit RGB/RGBA PNG,
non-interlaced and without ancillary chunks, within existing byte/dimension/pixel/CRC/decompression
limits. A valid PNG still needs valid source/per-asset rights and private authorization.
Historical note filenames hint14JPEG/1PNG; only3have reported dimensions and2exceed4million pixels.
These are dated metadata observations, not downloaded binary/decoder results.

Recommendation: defer JPEG/WebP acquisition/conversion support until one rights-reviewed sample
justifies a separate technical task. Alternative: approve that exact codec task with finite input/
output byte/pixel/frame limits, MIME sniffing, malformed/polyglot/decompression controls, metadata/
attribution preservation, deterministic derivatives, revocation/restore and independent tests.
Do not install a codec/dependency or change suffix/strip metadata to bypass current validation.

All missing images use neutral placeholders. Historical coverage gaps are1479bottle profiles and
420note entities; current counts are unverified because DB revalidation is blocked. Placeholder
graphics must be project-owned/permitted and must not impersonate a product photo, assert an
ingredient's chemical presence or imply source approval. No placeholder/UI/image bytes are built here.

## Source Rights Decision Queue — one Owner batch

| Item / current status | Recommended exact option | Alternative / risk | Approval needed, dependencies and implementation unlocked |
|---|---|---|---|
| SOURCE-01 PROPOSED | SRC-SAMPLE-PINNED-FIELDS-P1,3local records/0requests;review manifest only | Defer or separately approve exact identifier sample; risk is silently treating publisher labels as canonical identity/taxonomy | Owner scope and mapping reviewer/use; enables only isolated review-manifest preparation, not a new adapter/SQL promotion/application use |
| MEDIA-01 PROPOSED | MEDIA-REVIEW-JUNIPER-P1,1candidate,metadata/rights dossier only | Defer or one actual owner-created bottle file with authorship evidence; risk is page/metadata proof being misread as binary rights | Exact follow-up task/metadata references and reviewer; later usable file rights/acquisition approval are separate; no bytes/display unlocked by dossier approval alone |
| MEDIA-02 PROPOSED/DEFER RECOMMENDED | Keep PNG scope;defer new codecs until suitable licensed sample | Separately approved JPEG/WebP technical task; risk is malformed images/unsafe conversion or losing attribution | Exact format/derivative scope,bounds,dependencies and adversarial tests; no installation by inference |
| APP-01 BLOCKED technical / exact choice PROPOSED | Keep internal source research and placeholders while principal/field-use gates unresolved | Clean app-private intake vs reviewed auth amendment vs CLI-only; no admin fetch/filter | Genuine nonadmin model,selected provenance/rights and security tests before private application display |
| PUB-01 OUT OF CURRENT SCOPE; exact policy PROPOSED | Confirmed current no-public-endpoint/media/shared-cache/cloud restriction | A future separately reviewed publication scope; risk is cross-user/private/provenance or licensed-content leakage | Source/file/audience/auth/cache/retention approvals and tests; no exact Owner Defer answer or broader publication policy is inferred |

No unanswered entry is automatically accepted. This queue supplements the coordinator's single
[[Next_Wave_Owner_Decision_Form]], rather than creating another response form. Direction approval
does not create third-party permission. Record actual Owner answers with version/scope/reference;
otherwise continue safe metadata research and stop only the dependent acquisition/implementation.

## Actual execution and limits

This pass read existing merged plans and exact candidate PR24/source/media evidence, executed
the narrower permitted field-inventory rehearsal and preserved operation/asset boundaries. External requests0,
source/image payload acquisitions0,DB calls0,canonical/permission/normalization/hold/flag changes0.
No new candidate raw rows, private matrices, data dumps or image bytes enter Git or the ZIP.
The twenty per-asset detailed records remain in their existing ignored local audit, not duplicated.

TOOL EXECUTION REPORT: existing Context Mode bounded source retrieval, native Git/file reads,
Python/PyYAML and Caveman guidance; no new tool or config. Worker owns this one Markdown file only;
no commit/push/receipt/shared status edit. Local sanitized source/check hashes are under ignored
`.local/post2225-CD`; coordinator handles independent review, Obsidian status, PR25 and handoff.
Future sample-intake,decoder,SQL/rights/RLS/replay/restore/application tests are NOT RUN. Current
DB count/role parity revalidation is BLOCKED by unavailable Docker, not reported as PASS.
