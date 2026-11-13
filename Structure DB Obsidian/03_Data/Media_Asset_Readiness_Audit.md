---
id: DPT-DATA-006-MEDIA
project: DoomParfum By TK
type: media_readiness_audit
status: independent-review-pending
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, sources, audit, media, permissions]
source_of_truth: "../../README.md"
---

# Media asset readiness audit — bytes and permissions remain absent

## Actual inventory and denominators

Source [[Source_Inventory_and_Operation_Audit]] binds coordinator's current public aggregate/hash/
timestamps. It reports image_assets 0, asset_permissions 0, perfume_images 0 and note_images 0. Thus
**1,479/1,479 perfume profiles have no canonical bottle image and 420/420 canonical notes have no
usable linked illustration**. This is catalogue coverage, not a claim about worldwide media.
Existing 20 records are **15 historical note-illustration candidates plus 5 bottle identity leads**,
not 20 assets, grants or confirmed canonical associations. The empty bottle intake template has 0
rows; an empty template does not reduce the separate five-lead queue. No DB/image call here.

## Exact existing queues checked

| Queue / unit | Records | Source file SHA-256 |
|---|---:|---|
| Note metadata review CSV |15|`2691c69f9018bc3c9f280e3170e77b027cf80dd09dc361057f3152ad3ca9e13a`|
| Bottle rights/identity lead CSV |5|`d7b86e7fdcadc5fc45c5b7377d62f8194f9126538c64902858f94dc6e6b691f7`|
| Frozen15-media offline audit |15|`4185c30474385ed9c2f205a703e728f4f5ed5e8b43cefcbff73e7f87603744db`|
| Later exact-page metadata summary |3 bindings|`dfaa45318c99d53528befa0d619a0730a4d69723e651f20ca0e8d949e11c546a`|

The note CSV describes 15 labels in the historical RESEARCH46 vocabulary. That is not 15/420 approved
canonical note coverage, a chemical/formula assertion or a current access scope. Detailed local
`MEDIA_READINESS_20.json` preserves each original candidate and logical record ordinal, exact
source-page/claim/revision locator, input hash, asserted creator/license, intended subject/use,
rights/attribution/revocation and format uncertainties. No raw candidate rows or asset bytes enter
public Git/ZIP. No permission flag or original queue is edited.

| Requirement |15note candidates|5bottle leads|Operational conclusion|
|---|---:|---:|---|
| Source-page/reference and checked/reviewer metadata |15|5|lead/evidence locators, not per-file permission|
| Exact description revision ID recorded |15|0|recorded is not verified binding; bottle file revision unknown|
| Creator/license assertion recorded |15|0|all ownership/use grants remain unverified|
| Exact asset URL / per-asset grant evidence in bottle queue |not byte-verified|0/5 each|no bottle file identity or grant|
| Note field/section locator and permission-page URL recorded |15|0 exact file locators|page evidence cannot authenticate actual file rights|
| Source-reported SHA1 metadata |7|0 known file hashes|not downloaded SHA256; no byte identity proof|
| Downloaded binary SHA256 / MIME/dimensions verified |0|0|all 20 NOT ACQUIRED / NOT VERIFIED|
| Authenticated ownership / approved reuse/display |0|0|all 20 blocked|
| Note attribution text recorded |15|0 complete file attribution|asserted text must be checked against selected valid license|
| Note territorial text / explicit license-expiry value |12 /0|unknown|blank expiry is not expired, perpetual or permission|
| Verified exact perfume edition/canonical association |0 approved by this task|0|name/size/concentration lead is not a binding|

All15 note and5 bottle rows explicitly record bytes_acquired=False; note reuse/application-display
approvals are False. Bottle creator/license/asset URL/permission-evidence URL are each blank5/5;
terms URLs, checked-at and reviewer fields are populated5/5, but do not grant file usage. Bottle
states remain blocked_no_asset_reuse_grant / identity_lead_only. All candidate operations remain
blocked: note use states are UNKNOWN NOT APPROVED; bottle flags explicitly retain not_authorized /
image_bytes_not_authorized and no-grant values for acquire/store/display/derive/redistribute/retain.
Missing bottle cache/publication permissions remain UNKNOWN, not silently allowed. No-grant is not
a legal finding that no permission could ever be obtained.

Note license labels are historical assertions: CC BY4.0(2), CC BY-SA4.0(1), CC BY-SA3.0(4),
CC BY3.0(1), CC0(5), PD-self(1), CC BY2.0(1). These are not authenticated licenses or a project
license allowlist. Selectable alternatives must be reviewed, not cumulatively invented. A Commons
host, filename extension, parent catalogue entity or CC0 metadata license supplies no universal
image grant. Never infer chemical/botanical identity, creator authority or audience rights.

## Historical revision failures and later observed bindings

Preserve the earlier oldid/client fetch failures and frozen audit pin flags. Later pre-existing
metadata evidence at 2026-11-13T03:00:53.556129Z observed three exact description-page revision/title/
text bindings via official API HTTP200. This task only verified the local evidence/hash; no retry
or API call was made now. The later event supersedes only page-binding availability uncertainty,
not ownership, source chain, selected license, exact file SHA or any use approval.

| Description page | Revision | Stored revision-text SHA-256 |
|---|---|---|
| Nutmeg-spice.jpg |1177424529|`22daf2694c8d95258008eee3f0bd03daed6f8c6a234532f9bb16b063dbabac07`|
| Ribes nigrum-1.jpg |1158951883|`aa254a11458523fdc79d12e90448522f6b6e3c0b2eb0e71075e65df3fe0fb6ea`|
| Juniper berries777.jpg |1142894283|`9037b3593449e459b86992dad757acbd1bd9db0853883728bdc2c13628a509d2`|

These hashes describe page revision text, not image binaries or a license deed. Remaining 12 page
bindings lack equivalent available exact-revision verification in this audit. Narrow extraction
did not resolve the first two license declarations; empty extraction is not proof of absent license.
Juniper's CC-BY2.0/FlickreviewR template names do not authenticate ownership or upstream conditions.
The summary and original direct-attempt hashes/facts matched; all 20 usable assets remain 0.

## Format and technical readiness

Note filename hints: 14 JPG /1 PNG. Only 3 have historical reported dimensions;2 exceed 4,000,000
pixels. These are source metadata, not sniffed MIME, actual dimensions or decoder results. The one
PNG hint is not a technical PASS or a grant. Bottle file/format/dimensions are unknown5/5.

Merged `database/image_validation.py` is `local-static-png-v1`: static 8-bit RGB/RGBA non-interlaced
PNG without ancillary chunks. It checks bounded bytes/dimensions/pixels/decompression/CRC; SQL
separately gates exact scoped source/capture/asset/permission/ancestry. A technical result is not
durable rights. JPEG/WebP/other formats and any conversion/resize/crop/metadata stripping need their
own approved technical/derivative scope and tests. Changing a suffix or stripping attribution is
not a route around that gate. No decoder/conversion/storage/delivery or image acquisition ran.

## Per-asset release blockers and next exact action

Before any candidate can proceed: verify actual creator/rightsholder/selected license and other
rights; exact source/capture/file revision/hash; intended note or perfume edition; audience and
acquire/store/display/derivative/cache/redistribution/publication/retention uses; required credit/
license/change notices; expiry/review/complaint behavior; compatible format/byte/pixel budget and
technical task. Current permission assessments, private authorization and ancestor ceilings must
be checked before every permitted use; a public catalogue association never publishes private media.

Revocation/access withdrawal, a project review deadline and copyright-license validity are separate.
Do not invent expiry for blank fields or claim a compliant CC grant vanishes because a page changes.
Ownership disputes or incompatible evidence stop the affected project operation pending review;
preserve evidence and parent/derivative/replacement lineage. Restore must not reactivate restricted
objects. No such rights, retention or delivery mechanism is implemented by this audit.

No image candidate is ready for acquisition or a placeholder implementation PR. Smallest allowed
work now was this exact local metadata/evidence audit, completed without bytes. Owner must approve
one exact asset/use/format/permission-verification task before the next step. Existing holder,
rights/44holds, source observations and matching eligibility remain unchanged.
