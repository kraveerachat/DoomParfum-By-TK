---
id: DPT-UX-LUXURY-ROUTES
project: DoomParfum By TK
type: ux_specification
status: proposed
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, routes, wireframes, responsive]
source_of_truth: "../../README.md"
---

# Luxury frontend: sitemap, route contracts and wireframes

All behavior is PROPOSED under [[DPT-PLAN-012_Luxury_Frontend_Editorial]], not implemented. This is a bounded five-route mock presentation alongside [[Unified_Information_Architecture]], not a replacement for that future application IA. PRODUCT.md records the explicit brief. There is no incumbent frontend to preserve or critique visually.

## Surface purpose and direction

Home is an introduction to a tool, with editorial presentation and a single primary browse action. Explore, Detail and Notes are Operate surfaces: finding and understanding fictional records outranks drama. About is Read. Proposed visitor success: enter Explore from Home in one activation, reach any displayed fixture in one further activation, and follow a displayed note to related mock records in one further activation. These are test criteria, not observed usability results.

**Craft Read:** *fragrance discovery shell for the Owner reviewing fictional content, product language, ivory/ink with restrained gold, variance 5, signature bet: an open scent folio with readable Top / Heart / Base layers.*

Thesis: the interface reads like a maintained fragrance notebook, with generous object space and precise field states. Own-world: ivory paper, ink text, hairline grouping, editorial serif display, sparse gold rules and one navy story region. Story: orient, browse, inspect, follow a note. First viewport: 88px solid header; Home headline left and original abstract study right; one Explore mock catalogue action. Form: asymmetric editorial spread on Home; stable grid and semantic reading order inside the tool. No generated comp, concept-seed roll, prototype or rendered authority exists in this planning task. Proposed layouts below are the reviewable artifact; DESIGN.md will describe a built, verified world only after later implementation.

## Sitemap and route contracts

| Route type | Purpose / local input | Primary content and actions | States / links / exclusions |
|---|---|---|---|
| `/` | Introduce the mock study; local editorial fixtures | Hero, Featured Discoveries, Explore by Scent, Top/Heart/Base story, Journal preview, footer | Primary link `/explore`; family links use recognized synthetic family ID; Journal anchors target content on `/about#journal`. No additional Journal route. |
| `/explore` | Browse local synthetic perfume fixtures | Visible search label; family/note filters; count; stable title sort; grid; clear controls | `?family=<id>` and `?note=<id>` accepted only from allowlisted local IDs. q stays in memory. AND across filter groups, one selection per group. Detail links `/perfume/<slug>`. |
| `/perfume/[slug]` | Read exactly one known mock fixture | Breadcrumb, title, visible synthetic marker, abstract visual, fixture description, three note layers, separate general notes/accords, metadata | Unknown/invalid slug uses real 404 and generic unavailable view. No fallback to first record. Note links `/explore?note=<id>`; back link to Explore. No scores, price, seller, reviews, ownership or purchase controls. |
| `/notes` | Understand local invented note labels and navigate relationships | Intro, labelled note search, family filter, alphabetical grouped list, expandable explanation | Each note uses fictional stable ID. Link directly to `/explore?note=<id>` with visible result count labelled mock. No inferred chemistry or claim of botanical ingredients. |
| `/about` | Explain purpose and limits | Purpose, domain distinctions, mock disclosure, journal preview articles, credits and boundaries | Local anchor navigation; no newsletter/contact forms or analytics. No public deployment claim. |

One h1 per route, `<main id="main-content">`, skip link, header navigation landmark, contextual breadcrumb on Detail, and footer on all routes. Titles: “Home · DoomParfum By TK”, “Explore mock fragrances · DoomParfum By TK”, “<fictional name> · Mock study · DoomParfum By TK”, “Notes · DoomParfum By TK”, “About · DoomParfum By TK”. All receive noindex metadata. No product/review structured data or fabricated social proof.

Unsupported query keys are ignored and removed with replace, never forwarded. Invalid family/note IDs produce “This filter is unavailable” plus Reset filters; do not silently reinterpret them as valid filters. Search text limit 120 Unicode code points, trim for matching, compare case-insensitively with Unicode normalization; never evaluate regex or HTML. Search matches only explicit fixture name, fictional house and declared searchable description. Missing fields contribute no match. Sorting uses locale-aware name order plus stable ID tie-break. No relevance ranking or similarity language.

## Header and navigation contract

| Concern | Exact proposal |
|---|---|
| Desktop, ≥1024px | Header in normal document flow, minimum 88px. Horizontal gutter 48px; inner max-width 1440px. CSS grid tracks `minmax(0,1fr) auto minmax(0,1fr)`, 24px inter-track gaps. Nav occupies center track, wordmark left aligned, utilities right aligned. Equal outer tracks keep navigation at the inner container center despite asymmetric content. Do not use `justify-between` as proof of centering. |
| Wordmark | Text DOOMPARFUM 20px sans, medium, tracking .06em; BY TK 10px beneath as a small brand signature, not functional copy. Whole link accessible name “DoomParfum By TK home”. No external logo artwork. |
| Primary nav | Home / Explore / Notes / About in that order; 15px/24px; 32px gap. Current route `aria-current="page"` plus 1px underline and font weight. Detail marks Explore current. Link text stays sentence case. |
| Utilities | Search and Profile in that order. Consistent 20px SVG icons inside 44 × 44 CSS px hit areas, 8px gap. Names: “Search mock catalogue”, “Profile unavailable in this mock”. Search opens the local search dialog described below. Profile is a real button opening a small explanatory dialog, never a login form or network action. |
| Narrow / tablet, <1024px | Minimum 72px row: left Menu 44px; compact wordmark in flexible middle track; right Search 44px and Profile 44px, 8px gaps. Gutter 16px on phones / 24px on tablets. Brand can use 14px text + 10px signature at 320px; no overlap. Menu opens an accessible navigation drawer. Do not maintain a second simultaneous primary nav row. |
| Reflow override | At 200% zoom or larger text, switch to narrow layout as soon as desktop track contents cannot fit. At 320px, allow header to grow in height; if needed put wordmark on its own first row with Menu/Search/Profile below. Never hide the signature or shrink controls below 44px to preserve a single row. |
| Visual integrity | Solid ivory background; 1px fine divider at bottom. No text over unpredictable photography; no sticky shrink animation or hover-only primary navigation. |

Centering acceptance: at 1024, 1280 and 1440 CSS px, compute `abs(nav.centerX - innerHeader.centerX) ≤ 1px` after fonts settle. Change left content width from 150px to 240px and right content from 96px to 144px; centering must remain. If available content width fails fit, use the narrow layout rather than overlap. Also check 200% text and keyboard focus bounds. This is a proposed test, not an executed measurement.

### Drawers, search and focus

Menu: modal dialog with an accessible title “Navigation”, explicit Close button, full four-link list and current state. Width `min(360px,100vw)`, full available dynamic viewport height, scrollable content. On open, focus Close; trap Tab/Shift+Tab, make background inert, lock background scroll with reserved scrollbar gap, Escape closes, scrim click closes, restore focus to Menu. Activating a route closes it and moves focus to destination h1. Back/forward restores route position if supported; no drawer survives a route change. Only one overlay may be open.

Search: labelled modal with 48px input, visible “Search mock catalogue” label, 120-code-point limit, concise helper “Fictional studies only”, result count and title links. Initial focus input. Blank query shows all local fixture names, not fake recent activity. Input filters immediately in memory; announce only a concise debounced result count, not each row. Escape first closes the dialog (no search-key hijacking); focus restores to trigger. Selecting a result closes and navigates. Empty: “No mock fragrances found” with Clear search; retain query. The Explore search field uses the same matching function without opening another dialog. Search changes never steal focus.

On phones the Search dialog uses the available visual viewport, not a fixed full-screen height: Close/title and input remain above the keyboard, while only the result area scrolls. Respect safe-area insets and visual-viewport height changes when the virtual keyboard opens or rotates. Do not lock the input out of view or require keyboard dismissal to reach Close/Clear. Verify real mobile keyboard behavior in portrait and landscape; desktop viewport emulation alone is insufficient. Profile/Menu dialogs follow the same reachable-close rule if a keyboard is already open.

Profile placeholder dialog: “Profile is not available in this mock. No sign-in or account data is used.” One Close button. Do not place a nonfunctional disabled icon in the focus order with no explanation.

## Breakpoint and grid behavior

| Width / test anchors | Grid / gutters / layout |
|---|---|
| 320–639px (375px reference) | 4-column layout framework, 16px gutters, 16px gaps. All page prose/hero/story rows stack. Catalogue one item per row below 480px, two at 480–639px if text/hit areas fit. No horizontal page scrolling. |
| 640–767px | 6-column framework, 24px gutters, 20px gaps; catalogue two columns; Home remains stacked. Narrow header. |
| 768–1023px (tablet) | 8 columns, 24px gutters/gaps; catalogue two columns; Home hero becomes 4/4 split only if each reading area has ≥280px. Detail stays stacked. Notes index has two columns. Narrow header/drawer. |
| ≥1024px | 12 columns, 48px gutters, 24px gaps; max-width 1440px. Catalogue three columns at 1024–1279px, four at ≥1280px. Detail 7/5 split. Home hero 5/7; Notes 3/9. |
| ≥1600px | Content stays at 1440px; hero art may bleed beyond text container within viewport, without changing text measure or adding columns. |

All grid children shrink with `min-width:0`; labels wrap. Body measure ≤65ch. Controls have 44px hit targets as the product target (not a claim that WCAG 2.1 mandates 44px). Use logical properties. Long Latin names, Thai text, 200% text and 400% browser zoom at 1280px must preserve content and keyboard operation. No forced line break or fixed-height prose boxes.

## Home wireframes

Desktop composition in reading order:

```text
Wordmark             Home Explore Notes About           Search Profile
---------------------------------------------------------------------
Mock-study notice (concise, persistent content, not a blocking banner)
[H1: A personal atlas       ] [Original abstract scent study, 7 columns]
[of scent.                 ] [caption: Synthetic visual study          ]
[short purpose statement   ] [reserved 5:4 visual                       ]
[Explore mock catalogue    ]

Featured Discoveries                      [View all mock fragrances]
[Study A / neutral visual] [Study B / neutral visual] [Study C / visual]

Explore by Scent  [Bright study] [Soft study] [Deep study] (real links)

Top        [short layer text]   [corresponding labelled original visual]
Heart      [short layer text]   (one open scent folio, not three cards)
Base       [short layer text]

Journal preview       [article title + short original excerpt + link]
                      [second article, same destination intent]
---------------------------------------------------------------------
About / Mock scope / local credits                  DoomParfum By TK
```

Home hero proposal: 80px top/bottom padding desktop; headline 72px/1.04 with max 10ch, no uppercase block; body max 38ch and 20 words; one primary action. Art is an original abstract material study authored locally later, never a reference product bottle. No royalty claim, product photo illusion, brand asset or photorealistic commercial packaging. If no owned art is ready, an intentional typographic study occupies the same reserved field with “Synthetic visual study”; no empty image box. At 1440 × 900, show heading, action, visual and beginning of Featured Discoveries without forcing all sections above the fold.

Featured Discoveries: three curated fictional entries in a simple collection grid, no rankings/best-seller badges. Each article has a 4:5 abstract visual, title link, fictional house, family and visible Mock label. No duplicate “View” link with identical destination inside each card; title link and visual share one accessible link. Explore by Scent: three labelled family links as a horizontal ruled index on desktop; stack below 640px. They represent authored fixture groups, not measured fragrance families or matching scores.

Top / Heart / Base: the signature “scent folio” has one vertically ruled reading sequence; headings always visible and ordered in DOM. At wide widths a noninteractive original visual aligns alongside the three layers; on mobile place text and small visual together per layer. Layer descriptions explicitly say mock/illustrative. No proportion chart, concentration axis, durability claim or false scientific diagram. Optional opacity reveal may emphasize the current section once; content remains readable without it.

Journal preview: two short original editorial pieces, visibly mock/sample content. Links “Read the scent notebook” point to `/about#journal` and specific local anchors. No fake publication dates, authors or “read more” route stubs. Footer is two-to-three groups separated by one rule; no newsletter, payments, partner logos or social proof.

Tablet: 4/4 hero split where it fits, two featured entries on first row and third on second, story single column. Mobile: notice, h1, short text, primary action, 5:4 visual, Featured list, scent links, three story rows, Journal, footer. Hero padding 40px; no fixed 100vh gate. Keep content available if images/fonts fail.

## Explore wireframes

Desktop: header; Mock notice; 56px page-token h1 and one-line explanation; full-width 48px search; single toolbar (Family, Note, Sort) and count; active filters with remove controls; three/four-column collection. No persistent filter sidebar for this small dataset. Initial count reflects only actual local fixtures; do not invent inventory scale. “Featured” means authored order only if offered; default Name A–Z. No pricing, ratings, purchase actions or recommendation score.

Tablet: two-column collection, search full width, filters wrap to two rows as needed. Mobile: h1 at 36px, search then expandable filter region in normal flow, count, one column below 480px. Filter region is a disclosure button with `aria-expanded`; native selects/checkboxes remain labelled. Selecting filter preserves input focus and updates count; no automatic navigation to first result. No full-screen filter modal is needed for two simple groups. Clear all resets controls and restores full list.

No-result view takes the grid's place, retains controls and says “No mock studies fit these filters.” Offer Clear filters. No-data fixture view says “No mock studies are available” with link to About; no infinite loading. Broken visual uses the abstract placeholder and readable title. Back from a Detail opened in Explore restores in-memory query/filter/scroll for the same tab session; a hard reload intentionally resets typed query. Deep-linked family/note URL remains interpretable after reload.

## Detail wireframes

Desktop: breadcrumb above a 7/5 split. Left: reserved 4:5 abstract visual, caption. Right: Mock marker, fictional house, h1, family, short description and link to Notes. Below, full-width Top/Heart/Base sequence and a separate “General notes / Accords” area. Expandable “About this mock record” exposes fixture provenance without implying a real source. No sticky buy panel, carousel, compare score or seller price.

Tablet/mobile: breadcrumb, Mock marker and h1 first, then visual (4:3 on phone), description, layers, metadata. On mobile each layer is a heading/list; do not draw a narrowing triangle that squeezes labels. Each note is a named link with a 44px hit region. Unknown layer says “Not supplied in this mock”; authored empty list says “No entries in this mock layer”. General notes never populate missing layers automatically. Unknown family is “Unknown”, not a default family. Unknown slug: same header/footer, generic unavailable message, return to catalogue link, actual 404 status.

## Notes wireframes

Desktop: h1/short explanation; labelled search; 3-column filter/index area and 9-column grouped note list. Group headings are the actual first character of local labels, with an optional “All” reset. Avoid a decorative A–Z strip with dead letters. Each note entry is a ruled row: label, fictional descriptor, “Browse N mock studies” link. N counts authored membership only; unknown membership displays “Relationship not supplied”. Expanded explanation uses native details/summary.

Tablet: search full width and two-column note list, compact family controls above. Mobile: search, family select, one-column rows; no sideways alphabet strip; labels wrap and controls stay in flow. Selecting a note opens Explore with an allowlisted note ID. Empty note search has a reset action and does not invent suggestions. No ingredient photographs or chemical assertions.

## About wireframes

Desktop: 8-column reading region with 2-column breathing margins, 60ch prose measure; title at 56px, restrained rule, purpose, What this mock demonstrates, What remains future, and Journal anchors. Optional 3-column local index occupies a side gutter only at ≥1280px; links work without scripting. Journal has two short original sample articles about how to read the mock layers and distinguish unknown data; neither makes fragrance facts or claims about real products.

Tablet/mobile: single reading column, title 36px, local anchor list immediately below intro. No hero that delays the explanation. Footer at natural content end. Clearly explain that real matching, private catalogue, source permissions, account security, cart and collection are later gated workstreams.

## State and accessibility contracts

All routes support default, zero-data, missing-field, visual-unavailable, generic failure and unknown-route states. Loading is reserved only for an actual route transition/dynamic delivery; static local operations must not simulate a slow network for appearance. Route loading reserves final geometry with a non-animated placeholder; set busy state on the relevant region without hiding its accessible name. Error recovery offers Retry for the local render and return to Explore. No silent retries or fake success.

Native links/buttons/selects are preferred. Custom shadcn primitives are restricted to modal dialogs/drawer and only after keyboard and focus behavior is verified. Tooltip content cannot be the sole place containing a label or essential fact. Keyboard order follows DOM reading order. For forward navigation, focus h1 and announce title without duplicating announcements. History Back/Forward is the explicit exception: restore the previous list's filter/query/scroll and originating entry focus after layout settles, without an unconditional h1 focus that scrolls it to the top. If the original entry is unavailable, focus the list heading with a concise explanation. Browser-native restoration may be used only after verifying this behavior. No forced cursor, drag-only control, magnetic CTA, autoplay sound, scroll lock outside overlays or animated page transition.

## Amendment DPT-PLAN-013 — Frontend V1.1 (PROPOSED until merged)

Contract: [[DPT-PLAN-013_Frontend_V1_1_Amendment]]. The five logical route types and every English URL above stay. Superseded on merge:

| V1 clause above | V1.1 |
|---|---|
| One language | Thai mirror of the five routes under `/th`; same slugs, IDs, query keys and fragments; no cookie or redirect by header (4.1–4.4) |
| Titles and copy in English | Typed English and Thai dictionaries; Thai overlay for fixture prose (4.3) |
| Header in normal document flow, 1px divider | Sticky, stable height, R1 rule, with non-sticky fallbacks (5.1) |
| Utilities: Search, Profile | Search, Profile, language selector; compact control on narrow screens (5.2) |
| No alphabet strip in Notes | Jump index of live letters only; no dead letters (6) |
| Search matches declared fields | Same, plus the locale rule that leaves English results unchanged (4.5) |
| Forward navigation focuses the h1 | Same; the outline follows the navigation modality (6.1) |

Home hero, Detail spread, Explore controls and Featured keep the V1 layouts unless the Owner selects a TEST variant (section 8).
