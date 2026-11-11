---
id: DPT-UX-DUAL-SEARCH
project: DoomParfum By TK
type: ux_specification
status: proposed
owner: human-owner
updated: 2026-11-11
tags: [doomparfum, ux, matching, accessibility]
source_of_truth: "../../README.md"
---

# Dual-Mode Scent Search — Proposed UX

No frontend, screenshot copy or live prototype is implemented. The handoff reports an owner screenshot
with adjustable accord bars, add/remove/reset, copy link and result cards; the actual screenshot is NOT
AVAILABLE in this task. Its second percentage, bar units, ranking and endpoint behavior are unknown.
Those observations are functional reference only; this design defines its own formulas and labels.
No Fragrantica access, scraping, JavaScript/internal-endpoint inspection or ranking replay is authorized.

## Navigation and independent flows

Catalogue/Perfume Detail gains Find similar and Use reviewed notes/accords as starting point.
Explore navigation exposes two modes, Similar to a perfume and Build a scent profile. Existing Compare
continues side-by-side display; it is not the only entry to either search mode. Proposed routes:
/explore/similar?perfume=<public-id> and /explore/scent-profile?tab=notes|accords. These are conceptual
routes, not a chosen framework or an authorization mechanism. Private IDs never belong in public URLs.

| Mode | Controls | Results / states |
|---|---|---|
| A | search name/brand; choose exact concentration/edition; select any visible profile; optional region/role/brand/price/currentness filters | score components per layer, compared IDs, coverage/confidence, independent pair evidence, compare action |
| B1 Notes | searchable approved canonical vocabulary per top/heart/base; Heart/Middle label; explicit Any Layer; must/prefer/exclude; match-all/any; minimum matches | weighted requested-term coverage and reported-list focus; unknown-domain preview without percentage; single-note specificity notice |
| B2 Accords | approved taxonomy; add/remove; independent 0..100 preference sliders; numeric value edit; must/exclude; minimum matched accords | compatible observed-intensity fit OR separate presence-only results; unknown strengths never drawn as numeric bars |

Optional combined B3 is deferred. Switching tabs keeps local draft values separately and indicates
which tab is active; the inactive tab does not silently affect scoring. Clear empties the active query,
Reset restores that tab's initial seed/defaults, Remove deletes one clause. Search is an explicit submit;
sliders update preview values locally without background queries to third-party services. Cancel discards
in-flight local search. Loading retains query, rejects stale responses and indicates snapshot/time.

Copy from perfume includes only caller-authorized approved canonical IDs. Numeric accord values copy
only with an approved compatible scale; presence/rank-only profiles copy labels with user preference
defaults visibly labeled user-set defaults, NOT observed intensity. User must review before submitting.
Missing values remain missing. Seeding from a private profile keeps the entire draft private even if
some selected vocabulary happens to be public; no automatic declassification through copying.

## Search result presentation

```text
Mode: Similar to perfume / Build profile
Query controls     [Search] [Reset] [Clear] [Copy safe link]
Filters: current-first | include historical | strict in-market | region/brand/price
Results grouped by currentness, coverage and scoring method
  Perfume / brand / exact edition         Licensed image or placeholder
  Catalogue structural fit: 87.5%         Method: dm-a-pyramid-v1
  Data confidence: Medium                 Coverage: 50%; accords unavailable
  Pair evidence: none/supporting/disputed  Separate from score and confidence
  Known shared/different notes by layer    Unknown: general-only or rights-withheld
  [Why this result] [Compare]              Attribution and status checked-at
```

The numbers above are synthetic layout examples, not real perfume results. B labels replace
Catalogue structural fit with Requested-note fit or Accord preference fit / Desired-accord presence fit.
Always show method, coverage, confidence reasons and the tooltip: “Calculated from catalogue metadata
and method vX; this percentage does not measure how similarly the perfumes smell.” No unexplained
second percentage, verified-smell badge, clone claim or inferred intensity. Difference templates say
Listed only in this profile, not Stronger/longer lasting unless separate permitted evidence says so.

Current-first groups verified current/in-market, then unknown with an explicit badge; historical
candidates are opt-in. Show market/channel/date for stock and currency/size/date for price; no inferred
currency conversion, zero price for unknown or global availability from one retailer. Region/role
selection is optional. Popular/Newest sorts appear only with authorized usable metrics and explicit
missing-value treatment; they never overwrite the scent percentage or masquerade as default Best fit.

## State and accessibility requirements

- Empty query: teach note/accord selection; no fabricated100. No candidates: summarize active filters
  and offer Clear filters; an unavailable field or blocked permission is not a system error.
- Reference visible but insufficient: allow metadata inspection, state score unavailable and exact
  missing domains. Unresolved alias/edition asks for a choice; never choose highest-scoring identity.
- Partial pyramid: render All Listed Notes separately. Known absence, unknown and listed mismatch have
  distinct text/icons. Exact match uses canonical ID and layer, not similar spelling/family color.
- Errors: invalid bounded query is actionable; unavailable/unauthorized identity shares a generic state;
  timeout/query_too_broad asks to narrow filters, never claims complete search. Expired snapshot restarts.
- Mobile: stacked controls and cards, no horizontal dragging required. Tab/slider/button keyboard
  operation, arrow-key/typed numeric slider changes, visible focus, labeled ranges/current values,
  removable chips, announced result count/status and no focus loss on results. Color is supplementary;
  contrast and reduced-motion behavior require browser/accessibility tests after implementation.
- Image gaps: placeholder and descriptive alt text; source rights/attribution respected per asset.
  Missing image is not a missing-note state. No third-party hotlink or copied screenshot asset.

## Sharing, compare and private drafts

Copy safe link is enabled only for a deliberately public query containing public vocabulary/identity
IDs, method, bounded sliders/rules and non-sensitive filters. Validate all IDs again on open. Never
serialize private notes, profile/observation IDs, source URLs, user IDs, signed asset URLs, prices from
private listings or server-side hashes. Link serialization limited to8KiB. A private/mixed/seeded-private
draft shows Sharing unavailable for private inputs; public sharing requires an explicit new public
query authored independently, not silent stripping. Authentication is still required where configured.

Custom queries are ephemeral; no save/share backend or history persistence is implied. Keep private
drafts in memory, not service-worker/shared local storage or analytics query strings. Referrer policy
and log redaction must protect queries; no protected results offline after revocation. Compare two
authorized real profiles with separate score/data-confidence/evidence fields; a B query is not a fake
perfume column. Cart/purchase/collection screens remain unchanged.

See [[Dual_Mode_Matching_Acceptance_Tests]] and [[Dual_Mode_Matching_Data_Contract]]. Older
[[Compare_View]]/[[Perfume_Detail_Pyramid]] mockups remain illustrative drafts, not product facts or
this policy's authority for evidence-blended scores, chemical claims or unknown accord bars.
