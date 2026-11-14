---
id: DPT-DATA-006-SOURCES
project: DoomParfum By TK
type: source_inventory_audit
status: scoped-review-ready
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, sources, audit, media, permissions]
source_of_truth: "../../README.md"
---

# Source inventory and operation audit — actual local evidence

## Result and scope

Task [[DPT-DATA-006_Source_Media_Operation_Audit]], base `8c6a8376680c7a10cc3eb4b5cf80afe4376a9282`. This is an
operational audit of existing licensed files, indexes and permission evidence. No duplicate adapter,
generic Planning PR, catalogue acquisition or new rights assessment is created. It builds on merged
[[Regional_Source_and_Media_Permission_Dossiers]], [[Source_Registry]], [[Rights_and_Attribution]]
and [[Incremental_Source_Adapter_and_Media_Intake_Plan]], preserving their dated history.

Actual result: **1,479/1,479 pinned source records indexed; 25 dossiers / 275 distinct operation
classifications; 22 historical rights rows separately reconciled; zero newly executable source/sample
tasks with exact approval.** The existing 220-brand registry and all 15 Thai A-priority entries are
unchanged. The source-visible worldwide/live/brand/edition universe remains UNKNOWN. We cannot
claim every perfume model, current brand catalogue, regional market or edition was collected.

No DB/network call in this task. Current counts come from the coordinator's separately executed
READ ONLY public aggregate, SHA-256 `3480c8da292ee633b28bad6e4955b0890b175cbc392b13782fd2b0682ca6d09d`, core as of
`2026-11-13T20:04:07.96486+00:00`, supplement `2026-11-13T20:04:20.234038+00:00` and completeness
`2026-11-13T20:04:20.489428+00:00`. It reports 1,479 profiles / 1,435 approved / 44 held /
matching 0, 160 brands, 420 notes, 11,972 links, one source and one current rights assessment. All
1,479 profiles are private. All 49 data/security/role fingerprints equal before/after and the prior
baseline; this worker consumed that evidence, not a new database execution. Image assets, accords,
selected families, pair evidence, listings and prices remain 0. Application access remains gated.

## Full pinned source inventory — newly checked offline

Pinned Scento revision `086769ecf1add770ea6646bd4d88d39f0e7cddeb`. Verified all six source artifact
hashes and all eight existing staging/index output hashes, plus the original index's byte-identical
prior replay. The index has 1,479 unique source keys, covers exactly the local pinned perfume set,
and its names/house IDs/revision/license match those source records. Shapes: 1,388 layered and 91
general-only profiles. Observing this shape does not accept closure, absence, intensities or editions.
End-of-file completes only that immutable source snapshot; cursor/pagination is NOT APPLICABLE.
No live API cursor, source product total or scheduled update was measured or assumed.

Existing index `08_OUTPUTS_APPROVED/staging/index/run_001/D2_Source_Perfume_Index_1479.csv`, SHA-256
`3e24904ade3bc32a29246be40d9e143b7b0a72f224d5e43f703f92224dcef1da`. Its historical `review_status` is needs_review on all
1,479 rows. Both `canonical_perfume_id` and `canonical_brand_id` columns are blank on all rows:
**missing mapping, not conflicting UUIDs**. These preserved review/index values are not the current
canonical ledger's 1,435 approved /44 held state. No old file was rewritten to disguise that gap.

The existing 1,479-row progressive review sidecar supplies deterministic perfume UUID targets.
All 1,479 source-field hashes and target IDs match the current merged importer derivation offline.
This proves target derivation, not current per-row DB existence, selected provenance, permissions,
application ownership or eligibility. This worker performed zero individual DB-binding checks.

Ignored `PINNED_SOURCE_AUDIT_INDEX_1479.json` now cross-references each existing source key with
file/revision/SHA-256, logical CSV record ordinal, parsed-field hash, observed field availability,
publisher locator, code-derived perfume/brand targets and historical review bucket. It explicitly
marks targets as not DB/authorization proof and edition/closure unknown. Primary index lacks a
capture timestamp/current checked-at and row-specific effective operation/audience evidence; the
audit records today's local check separately. File modification time is not retrieval time. Detailed
rows stay ignored locally and must be excluded from public Git and the consolidated ZIP.

## Eleven operations — no permission inherited from missing columns

Operations are discovery, automated access, storage, local research, internal display, image
acquisition, transformation, caching, redistribution, public publication and scheduled updates.
The prior eight-column matrix is preserved, not overwritten. A generic update field does not
authorize a scheduler; metadata storage does not grant images; local research/display does not
grant publication. These are audit classifications, not new SQL rights flags or legal verdicts.

Table states: **A** APPROVED FOR EXACT OPERATION; **C** CONDITIONAL; **U** UNKNOWN; **R** RESTRICTED;
**D** DENIED; **N** NOT VERIFIED. A is limited to the existing local pinned metadata pilot; it does
not authorize a new application read, media, revision, acquisition or public use. C is a documented
possible path with missing exact task/source/asset/use requirements, not execution permission.
R retains an explicit published/project restriction; N marks unavailable identity/current terms
evidence. U/N/R/D all stop the affected action. Local review of our own dossiers is allowed but is
not remote catalogue discovery permission. Discovery below means source inventory enumeration.

| Candidate | Discovery | Auto | Store | Research | Internal | Image | Transform | Cache | Redistribute | Public | Schedule |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S01 Pinned Scento snapshot | A | A | A | A | A | R | U | A | R | U | U |
| S02 Scento live reference API | U | C | U | U | U | U | U | U | U | U | U |
| D01 Dior | R | R | R | R | R | U | R | R | R | R | R |
| N01 Le Labo | R | R | R | U | R | U | R | R | R | R | R |
| ME01 Lattafa | U | U | U | U | U | U | U | U | U | U | U |
| ME02 Fragrance World | U | U | R | U | U | U | R | U | R | R | U |
| TH01 SIAM 1928 | U | U | R | U | U | U | R | U | R | R | U |
| TH02 MITH | U | U | U | U | U | U | U | U | U | U | U |
| TH03 SÚNDALO | U | U | U | U | U | U | U | U | U | U | U |
| TH04 SCENTERY | N | U | U | U | U | U | U | U | U | U | U |
| TH05 BE CHERIE PARFUM | N | U | U | U | U | U | U | U | U | U | U |
| TH06 La Palette | N | U | U | U | U | U | U | U | U | U | U |
| ID01 SAFF & Co. | R | R | R | U | R | U | R | R | R | R | R |
| ID02 Mykonos | U | U | U | U | U | U | U | U | U | U | U |
| ID03 HMNS | U | U | U | U | U | U | U | U | U | U | U |
| SG01 Scent by SIX | R | R | R | U | R | U | R | R | R | R | R |
| SG02 Scent Journer | R | R | R | U | R | U | R | R | R | R | R |
| MY01 Rirana | U | U | U | U | U | U | U | U | U | U | U |
| VN01 d'Annam | U | U | U | U | U | U | U | U | U | U | U |
| MD01 Wikidata structured identifiers | C | C | C | C | C | U | C | C | C | C | U |
| MN01 Commons ingredient illustrations | U | U | U | U | U | U | U | U | U | U | U |
| MN02 Smithsonian Open Access | N | U | U | U | U | U | U | U | U | U | U |
| MN03 Met Open Access illustration prospect | C | C | C | C | C | C | C | C | C | C | U |
| MB01 Owner-created bottle photography | U | U | U | U | U | U | U | U | U | U | U |
| MN04 Owner-created or commissioned note illustration | U | U | U | U | U | U | U | U | U | U | U |

Totals across 25 dossiers: A6 / C20 / U189 / R56 / D0 / N4 = 275. All six A states belong only to
S01's existing pinned-local scope. DENIED is not lost: the separately audited 22-row historical
rights matrix retains Fragrantica's explicit NO automated access/bulk storage/content republication/
image use; no exemption or retry is created. Those registry rows are a separate artifact/version,
not 22 new approved sources to add to the 25 dossiers. Their missing research/cache/derivative/public/
schedule columns remain unsupported, not silently granted.

New evidence did not justify re-fetching denied/failed sites. Prior Smithsonian 404, SIAM1928 timeout,
indexed-only Scent Journer evidence and unresolved first-party Thai identities remain in the prior
dossiers. No repeated access, permission request or API/image payload was issued. Underlying primary
terms/license URLs and exact operation reasons are retained in each local matrix row; this is an
offline audit of that evidence, not a current external license or ownership revalidation.

## Registry discrepancies and lineage controls

`Source_Registry.md` contains dated early P1 sections saying no full import, followed by later
approved import evidence. Fresh counts above resolve current inventory, without deleting history.
More seriously, its SRC-03 identifies Butterfly Thai Perfume and SRC-04 HMNS, while the external
22-row rights matrix uses SRC-03 for Wikidata and SRC-04 Fragrantica. These are different historical
namespaces. Do not join, grant rights, choose a publisher or promote data by an unqualified SRC code.
Use exact artifact/version/hash plus publisher/source URL and separately reviewed identity. No
code/registry/alias or canonical-ID correction was performed. A future source-key model must retain
both provenance contexts rather than silently renumber or merge sources.

The older Source Registry retains an HMNS specific IP-terms locator while the newer25-dossier pass
did not verify substantive current HMNS terms. These observations differ in date/coverage; neither
is a new grant. Keep both and require exact current use/terms evidence before any intake. No missing
evidence is resolved by assuming the newer document is authoritative on every historical field.

## Smallest genuinely permissioned next task

**Ready and completed now:** read/verify the already licensed pinned local snapshot and its complete
source inventory, without promotion. Do not create another Scento adapter or duplicate this index.
Current source license/attribution and six-file hashes remain bound to this exact revision; the live
Scento API's keyless lookup terms do not permit wholesale competing-catalogue rebuilding.

**No new source/sample implementation is ready.** Wikidata structured identifiers and a Met OA
illustration have conditional licensing paths, but no accepted exact sample/use/audience/request
budget/activation task; Met also needs separate JPEG technical scope. Regional official feeds and
the20 media leads lack exact use/file permissions. Do not open a placeholder implementation PR.

Priority remains all 15 Thai entries, then Middle Eastern, Indonesian, designer/niche and other
approved groups. The next Owner action is to select one exact source/rightsholder, fields/sample,
method/budget, audience, operations and permission evidence; publisher contact must itself be
explicitly authorized. Template preparation and conservative strategy are not such answers.
Source-specific revision/cursor/hash/total and completeness must then be verified within that task.
For existing data, any current canonical association or app-ready view needs its own accepted
identity/access/selected-rights/closure/normalization gates. No 44 hold or matching flag is changed.
