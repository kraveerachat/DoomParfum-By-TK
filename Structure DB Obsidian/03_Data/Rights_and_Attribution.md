---
id: DPT-DAT-006
project: DoomParfum By TK
type: legal_and_rights
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - rights
  - copyright
  - attribution
source_of_truth: "../../README.md"
---

# Rights and Attribution — P1 Proposed Controls

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
