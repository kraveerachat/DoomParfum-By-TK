---
id: DPT-DAT-006
project: DoomParfum By TK
type: legal_and_rights
status: draft
owner: project
updated: 2026-11-11
tags:
  - doomparfum
  - data
  - rights
  - copyright
  - attribution
source_of_truth: "../../README.md"
---

# Rights and Attribution — P1 Proposed Controls

## Local DB implementation evidence — IMP-P1-01

Planning PR #1 is owner-merged. Local SQL now binds exact scope/source/capture/assessment/asset permission,
checks selected content hash/locator and parent permission/derivative obligations, and gates operations
on active source AND asset uses. Revocation/parent changes invalidate descendants; elapsed expiry is
checked at use time. See [[IMP-P1-01_Implementation_Evidence]]. These tests use labeled synthetic grants
and metadata only; they establish no real third-party permission or actual byte acquisition/decoding.
Human review of content scope, evidence applicability and license obligations remains mandatory;
local derivative output-license equality is conservative, not a full legal compatibility engine.
Scento raw/package remains local outside Git with CC BY 4.0 attribution; no new source/image rights,
provider, cloud bucket or regional imports are approved. Acquisition/proxy/storage/restore are NOT RUN.


This revision corrects baseline assumptions that public facts or personal fair use automatically permit
copying site content/images. No universal fair-use grant is asserted. Owner restrictions already apply;
the storage/approval mechanism below is PROPOSED. Source-specific findings: [[Source_Registry]].

## Separate access and reuse decisions

For each source and asset, assess research lookup, automated access, local caching, durable storage,
application display, redistribution and AI processing separately. Each is allowed/restricted/unknown,
with evidence URL, checked time, reviewer, scope and expiry/review date. Unknown is not allowed for
production import/display. A public URL is neither image ownership nor hotlink permission.
User-provided screenshots can contain third-party content; confirm scope before public sharing.
Do not commit private orders, carts, photos with private EXIF or unlicensed raw datasets.

## Verified evidence in this session

- Scento's pinned export declares [CC BY 4.0](https://github.com/Scento-com/perfume-dataset/blob/086769ecf1add770ea6646bd4d88d39f0e7cddeb/LICENSE).
  Credit Scento, link its database and license, identify normalization/changes, retain supplied notices.
  License text: [CC legal code](https://creativecommons.org/licenses/by/4.0/legalcode).
  This does not grant rights to unrelated website photos, trademarks or undisclosed upstream content.
- Scento API [terms §22](https://www.scento.com/terms-of-service#perfume-api) allow reference tools but
  forbid overload, bypass and wholesale rebuilding of a competing catalogue. [Developer FAQ](https://www.scento.com/developers/perfume-api)
  requests reasonable rates and caching. Numeric quotas and durable redistribution scope remain unknown;
  preserve the supplied citation. Prefer the licensed export for a seed pilot.
- HMNS [IP terms](https://hmnsperfume.com/pages/terms-conditions-revamp) require written consent for
  reproduction/distribution/derivatives. No such consent was obtained. No product prose or images imported.
- Butterfly copyright notice was observed; no feed/image grant verified. Lattafa terms fetch returned
  403; no bypass attempted and no reuse permission inferred from the official product page.
- [Commons Local Lemon.jpg](https://commons.wikimedia.org/wiki/File:Local_Lemon.jpg) identifies author
  Gaurav Dhwaj Khadka and CC BY-SA 4.0. Candidate illustration only. Credit author, source and license,
  record modifications, and comply with compatible licensing for adapted images. No binary acquired.
- Fragrantica remains reference-only; automated scraping and internal API use are forbidden for this task
  regardless of scraper availability. No Fragrantica automation occurred.

## Proposed enforcement and attribution output

`rights_assessments` is versioned evidence, not a single permanent `rights_verified` boolean.
Source observations and image assets reference the specific assessment in effect. An expired or changed
assessment stops new processing and queues affected records/assets for review; no destructive deletion
is performed without an owner plan. Store only the minimum permission evidence that may be retained.

A displayed fact can resolve through its selected source observation to source name/URL, retrieved date,
license/terms, attribution and changes. Images additionally expose creator/source/license and derivative
history. Record page URL separately from file URL and object key. For user-authored facts, record a
private owner source record; do not publish private evidence as attribution.

External downloads in the future must allow only approved HTTPS hosts, bounded sizes and types;
reject redirects into private networks and executable/vector content unless sanitized. Network-fetch
security is a future implementation acceptance criterion, not an implemented control.

## Open decisions

Owner approves the seed attribution presentation, rights-review cadence and image license policy.
Unlicensed official-site product feeds require permission or owner-provided licensed alternatives.
No paid subscriptions, account connection or permission request to third parties was sent.


## Post-review image grant consistency — PROPOSED

Source/publisher assessment and asset permission are separate records. image_assets carries source_id,
source_record_id, rights_id and an optional selected asset_permission_id; acquired/validated states
require the selected binding plus metadata. Scoped composite FKs bind source_record and assessment to
the SAME source, and selected permission to the EXACT image/capture/assessment. A same-source grant
for a different image/capture fails that tuple, rather than being accepted through a loose rights_id.
Metadata-only states may point to an unknown assessment but cannot fetch/store/render bytes.

Each asset_permissions row identifies the asset locator/hash evidence, allowed acquire/display/transform/
redistribute uses, reviewer/time, review deadline and one-way revocation. Content rights are immutable
versions; revocation disables use without rewriting evidence. Validate that the external proof genuinely
covers this asset and each intended use; referential integrity alone cannot determine legal permission.

Derivatives have their own image IDs/hashes and selected permission, reference the exact parent asset
AND parent permission, and require parent's transform_use=allowed. For the pilot parent/child must share
scope/source/capture; unknown/denied transformation, mismatched parent, incompatible output license,
missing attribution or expired/revoked ancestor blocks the relevant operation. Parent permission never
automatically grants child public display or redistribution. Adaptation/change notices and output-license
obligations are recorded and revalidated on restore. Cross-scope/source publication requires a separate
reviewed provenance/copy design and permission; it is not enabled here.

A licensed image may still be user-private. Permission evidence/private URLs and EXIF stay scoped;
public catalogue membership does not expose them. Private/shared delivery rechecks auth and effective
rights through the authenticated object proxy. See [[Data_Dictionary_Draft]], [[Security_and_Privacy]],
[[P1_Pilot_Implementation_Plan]] for precise constraints and negative controls. No new grant is claimed.

The acquired/validated transition additionally requires the selected permission's bound content hash to
match image bytes. Finalizing an initially unknown hash uses a new immutable permission version.
Changing an image capture/bytes uses a new asset ID; changing a parent's selected permission invalidates
children for re-review, rather than letting an old parent-binding pointer silently authorize new use.
