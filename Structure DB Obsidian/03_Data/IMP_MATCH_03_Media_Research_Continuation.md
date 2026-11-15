---
id: IMP-MATCH-03-MEDIA-CONTINUATION
project: DoomParfum By TK
type: media_pre_intake_feasibility_review
status: METADATA_FEASIBILITY_REVIEW_COMPLETE_INTAKE_BLOCKED
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, media, png, rights, pre-intake, b1]
source_of_truth: "../../README.md"
---

# IMP-MATCH-03 media pre-intake feasibility continuation

Owner-authorized metadata-only continuation. The parent-confirmed current branch is
`codex/imp-match-03-synthetic-b1` in the existing `.local/worktrees/b1-contract-prep` checkout,
starting from main `604d447e599aa8359d3427dfbfbceaac85373e48`.
Exact B1 revision 2 acceptance is recorded separately in `.local/b1-implementation/OWNER_APPROVAL.json`
and `matching_math/evidence/b1_owner_contract.json`; it approves synthetic B1 code only.
It does not approve image intake, media acquisition, source permissions or application delivery.

Scope: inspect retained metadata for B1-MEDIA-021 and B1-MEDIA-022 against current
`database/image_validation.py`, document what cannot be inferred, and produce an exact reviewer
checklist and original-only rejection policy. No new asset/source acquisition or network reference
is needed. This note supplements [[B1_Media_Rights_Inventory_and_Sample_Proposal]] and the merged
[[Incremental_Source_Adapter_and_Media_Intake_Plan]], without changing frozen preparation files.

Expected evidence: source-file hashes, metadata-only arithmetic, static source-to-checklist mapping,
local document assertions and exact limitations in ignored `.local/b1-implementation/mediaresearch`.
No images, thumbnails, downloads, decoder/runtime tests, DB/Docker, Git operations, other docs/code,
rights grants, normalization, 44-hold or eligibility changes. Parent owns coordination and delivery.

`OWNER_IMAGE_INTAKE_APPROVAL=NOT_GRANTED`; binary intake remains `BLOCKED_ON_OWNER_NOT_STARTED`.


## Feasibility finding

No additional network reference was needed. Existing metadata cannot establish that either selected
original is admissible to `local-static-png-v1`. Both reported sizes/dimensions fit numeric defaults;
actual bytes, PNG features and current operation-specific rights remain unverified. This is a new
operational feasibility check, not another acquisition plan or a repeat of the existing rights inventory.

The separate exact B1 code approval records revision 2 and contract SHA256
`77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977`.
Its explicit exclusions include source/image acquisition. Prior dated proposed/not-approved wording
in frozen B1 preparation is historical; this continuation does not alter those files. Image intake
approval remains **NOT_GRANTED**, independently of the accepted synthetic-code scope.

## Two retained originals against numeric limits

Only retained public metadata is used; its observation date remains 2026-11-14T22:13:56Z. No remote
description was refreshed and no original, thumbnail or private object was opened.

| Retained proposal | Reported size/dimensions | Derived pixels | RGB filtered scanline bytes | RGBA filtered scanline bytes |
|---|---|---:|---:|---:|
| B1-MEDIA-021, [BergamotEssOil.png](https://commons.wikimedia.org/wiki/File:BergamotEssOil.png) | 535,064 bytes; 841×1280 | 1,076,480 | 3,230,720 | 4,307,200 |
| B1-MEDIA-022, [Ginger.png](https://commons.wikimedia.org/wiki/File:Ginger.png) | 3,689,052 bytes; 2424×1126 | 2,729,424 | 8,189,398 | 10,918,822 |

The scanline calculation is `height × (1 + width × channels)`, assuming channels 3 or 4, with one
filter byte per row. It is not a decode, observed color mode, peak-memory estimate or rendering test.
Current defaults are 5,242,880 compressed bytes, width/height at most 4096, 4,000,000 pixels,
20,971,520 decoded scanline bytes and 1,024 chunks. Reported byte headroom is 4,707,816 for 021
and 1,553,828 for 022. The two reported originals total 4,224,116 bytes. Accurate metadata would
avoid those numeric rejection branches, while leaving every byte-dependent branch unresolved.

The retained 021 record asserts PD-self dedication with fallback permission; 022 asserts CC BY-SA
4.0. Their creator authority is not authenticated. License metadata is distinct from Owner intake,
current rights assessment, private-use authorization and technical acceptance. Original-only review
does not waive attribution/notices, ShareAlike obligations where applicable, other rights, or the
reviewer's decision on symbolic note association. An oil-vial photograph must not imply a perfume's
actual formula or be relabeled as a bergamot-fruit photograph.

## What the present validator requires and metadata cannot prove

The inspected source is `database/image_validation.py`, version `local-static-png-v1`.
`Limits` is at lines 28–38; `inspect_png` at 50–116. These are static source locations, not test results.

| Actual-byte requirement in current source | What the retained page metadata establishes | Unresolved consequence |
|---|---|---|
| Nonempty exact `bytes` value within the limit; PNG signature | Filename and reported MIME/size only | Wrong bytes, MIME, type, size or polyglot/trailing content may still be rejected |
| First IHDR, exact header length, depth 8, color type 2 or 6, compression/filter method/interlace all 0 | Published dimensions and generic PNG designation | 16-bit, palette, grayscale or interlaced originals can be inadmissible despite the suffix |
| Dimensions, pixels and filtered-scanline bounds before decompression | Arithmetic table above, if accurate | Actual IHDR values and all bounds remain unchecked |
| Bounded chunk count/length and valid CRC for every chunk | No actual chunk listing | Structural corruption or too many chunks remains unknown |
| Only IHDR, IDAT and IEND chunks; every other kind rejected | Ginger page exposes camera/editing metadata | EXIF, text, ICC, APNG, palette or unknown chunks would reject an actual file; the page cannot prove which chunks exist |
| IEND with no payload, required compressed data and no trailing bytes | No actual ending/stream data | Truncation, extra content or missing data remains unknown |
| Complete bounded zlib stream; exact expected decoded length; no unused/unconsumed data; row filters 0–4 | No compressed stream or row data | Decoder/length/filter rejection remains possible |
| Measured SHA256, byte count, dimensions and MIME match registered asset exactly | Source-reported SHA1 and page revision only | Neither identifies downloaded SHA256 or proves the registered object binding |

Ginger has a concrete compatibility warning because its description displayed camera/editing fields.
Those fields might reflect uploaded metadata or retained descriptive extraction; this review cannot
conclude that the current original contains a specific ancillary chunk. Neither rejection nor
acceptance is established. Bergamot has no equivalent proof of ancillary-chunk absence. Public PNGs
often need feature review, but no frequency, probability or guaranteed outcome is asserted here.

`validate_registered_asset` is for an already-registered permitted local object. Static source requires
`can_use_asset` authorization before invoking the bounded local reader; the reader must not be HTTP
or an unbounded file reader. Measured metadata must equal the registered binding. The complete
relevant authorization/binding snapshot is checked again afterward. Later display, transform or
redistribution must reauthorize; a successful technical result would not be a serving token. No SQL,
local-object callback or validator function was invoked in this continuation.

## Exact pre-intake reviewer checklist

All items below are pending gates, not a new authorization or a completed intake checklist.

1. Record a separate Owner decision naming 021 and/or 022, original file/version, request method,
   finite byte/request budget, permitted local retention, intended operation and private audience.
   The B1 scorer contract cannot supply this approval.
2. Accept or reject actual creator authority/evidence sufficiency, the applicable per-file instrument,
   required credit/notices, other rights and symbolic subject association. Keep unresolved provenance
   or failed historical revision reads visible; do not retry those URLs under this task.
3. Bind the selected permission to the same source, capture, original asset and intended operation.
   Confirm current use, expiry/withdrawal, attribution, access scope and ancestry rules; generic Commons
   policy or a license from a different asset is insufficient. Current DB/rights state is not checked here.
4. Establish an explicitly authorized acquisition/local-object path outside this continuation. Current
   validator callbacks are not download adapters. No source/binary acquisition implementation is supplied.
5. Before a separately approved original is examined, retain its exact permitted bytes outside Git,
   establish actual SHA256 and finite read bounds, and reject a source-version/hash/identity mismatch.
   Retained description data and source-reported SHA1 cannot replace that proof.
6. In that later approved task only, verify signature/header/color/depth/interlace, dimensions/pixels,
   decoded limits, each chunk/CRC/count, ending, complete compressed stream and scanline filter bounds.
   Any rejected feature or mismatch stops the sample. This step has not run.
7. Require exact registered source/capture/asset/rights/MIME/bytes/dimensions/hash/private-scope
   consistency and current pre/post authorization. No production or existing catalogue row is changed
   by this checklist; private application binding requires its own permitted task and application gate.
8. Record accepted/rejected/blocked result per original without upgrading an unknown to permission.
   Preserve permitted provenance and reason; leave a neutral permitted placeholder when blocked.

## Accepted-original-only rejection policy

This proposal retains the current original-only, fail-closed lane. A candidate becomes eligible for
later private binding only after rights, Owner task, exact original identity and existing technical
requirements all succeed in the separately approved task. No candidate is accepted by this note.

If an original contains any forbidden chunk or unsupported feature, exceeds a limit, fails a checksum,
has incomplete stream data or differs from registered identity, reject that original from this sample.
Do not strip EXIF/text/ICC, reencode, crop, resize, change extension, swap a thumbnail, silently select
an older file revision or loosen limits. Those actions create another asset/use/technical scope and
cannot turn a rejected original into an accepted one here. No conversion/new codec/provider/cloud/
CDN/publication is proposed. Do not attach a newly permissive child to bypass restricted ancestry.

If rights or Owner scope remain unresolved, keep the candidate blocked before bytes. If current
authorized local binding later changes during validation, stop the operation and keep the existing
uniform unavailable outcome; do not reuse a prior technical result. Revocation/replacement and restore
must preserve lineage and current restrictions under the already-merged plan. This continuation does
not run or revalidate those lifecycle, SQL/RLS, backup or application controls.

## Evidence, limits and next Owner action

New work is limited to source inspection, retained metadata arithmetic and a pre-intake checklist.
No new external source reference was required. No images, thumbnails, source acquisition, decoder/
runtime tests, private-object reads, DB/Docker or Git operations occurred. No new technical image
PASS, creator authentication, canonical binding or active permission is established. All eight frozen
preparation files and the prior inventory/dossiers remain unchanged; parent owns delivery and status.

Ignored evidence: `.local/b1-implementation/mediaresearch/PNG_METADATA_GATE_REVIEW.json`, SHA256
`b613a5c17f582937c21d6eaa90937038b07f72e165b85d0b2184e1b00590a2f3`. Validator source SHA256 is
`d50bb159e0223e21c74d10b64176190569c9889f88726706df3ece143d54f29f`. The source-pin manifest binds the retained metadata,
frozen prior note, merged plan, eight frozen files and actual separate B1 code approval records.


Local static document/source assertions and final hashes are recorded in `CONTINUATION_CHECKS.json`;
they are not image-validator or runtime test results. Required next Owner action is a separate exact
image-intake decision, followed by rights review and an authorized original-byte task if those gates
succeed. The synthetic B1 implementation may continue independently; this note neither blocks nor
expands its accepted code scope. `OWNER_IMAGE_INTAKE_APPROVAL=NOT_GRANTED` remains unchanged.

TOOL EXECUTION REPORT: existing Caveman/Context Mode; local Python AST/text/arithmetic/hash checks;
PowerShell for bounded file inventory; apply_patch for this new note and ignored research helpers.
No tool install, external source checkout, network reference, Git operation or runtime image test.
Only `03_Data/IMP_MATCH_03_Media_Research_Continuation.md` and ignored
`.local/b1-implementation/mediaresearch` were written. Branch is parent-confirmed
`codex/imp-match-03-synthetic-b1`; no branch/PR created by this worker. Parent owns coordination.
