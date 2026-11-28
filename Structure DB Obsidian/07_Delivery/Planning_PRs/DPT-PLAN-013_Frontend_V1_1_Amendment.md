---
id: DPT-PLAN-013-AMENDMENT
project: DoomParfum By TK
type: planning_amendment
status: merged
owner: human-owner
updated: 2026-11-27
tags: [doomparfum, planning-amendment, frontend, localization, typography, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# Frontend V1.1 planning amendment

Amends the merged [[DPT-PLAN-012_Luxury_Frontend_Editorial]] plan under DEVELOPMENT_WORKFLOW §3.4 and §3.6 class C. Documentation only. `IMPLEMENTATION_NOT_STARTED=YES`. Task note: [[DPT-PLAN-013_Frontend_V1_1_Design_Upgrade]].

> Post-merge status (recorded 2026-11-27): merged by the Owner on 2026-11-26, PR #37, merge `3e87027fbdbbb016c148a84ca33775e64cccf3e0`. "Proposed", "until merge" and `IMPLEMENTATION_NOT_STARTED` statements below are historical. Implementation: [[IMP-WEB-02_Frontend_V1_1]]. The contract text is unchanged.

This note is the single V1.1 contract. Where it conflicts with a V1 contract, this note wins **after the Owner merges it**, and only for the clauses listed in section 12. Everything else in V1 stays in force. V1 text is kept as history.

## 1. Inputs and how decisions are classified

| Input | Identity |
|---|---|
| V1 baseline | [PR #36](https://github.com/kraveerachat/DoomParfum-By-TK/pull/36) merged 2026-11-25T18:40:31Z as `ab3351a8432d1d6664a6b4281784cfea56b0b9fa`; code `449178093ed7616570cf651f8b5e4f3cc2d3001e` |
| Owner direction | V1.1 master instruction and Gate B instruction, Owner chat, 2026-11-25/26 |
| Design assessment | `DoomParfum_Design_Upgrade_Proposal_v2.md`, 795 lines, SHA-256 `4ee922fbc8c7acf42fb50b623fb6c2178e9406d26e3812d00e73703ef51c7f21` (exact bytes as supplied). The exact file is retained locally outside Git; its text is not published here (V11-OD-12). Section 13 traces every section |
| Measured V1 facts | [DPT-PLAN-013_V1_Baseline.json](../../08_Operations/Test_Evidence/DPT-PLAN-013/DPT-PLAN-013_V1_Baseline.json) |

Precedence: Owner direction, then this amendment, then V1 contracts, then the proposal. The proposal is an assessment. A proposal item binds only through the rows below.

| Class | Meaning |
|---|---|
| **KEEP** | Must survive V1.1 unchanged. A change needs another amendment |
| **CHANGE** | Build it in V1.1. Exact values are proposed until merge and must be checked in a browser |
| **TEST** | Render the alternatives, show the Owner, then build the selected one. The stated default holds until the Owner selects. The agent does not select |
| **REJECT** / **DEFER** | Not in V1.1 |

## 2. KEEP

| ID | Kept |
|---|---|
| K01 | Luxury Fragrance Editorial identity; ivory, ink and navy as the primary palette |
| K02 | Bodoni Moda for English display; Noto Sans Thai for body and UI in both languages |
| K03 | DOOMPARFUM BY TK wordmark in its current sans form, always in Latin script |
| K04 | Five logical route types and every existing English URL |
| K05 | 12-column foundation, 1440px maximum, 16/24/48px gutters, catalogue 1/2/3/4 columns |
| K06 | Original abstract SVG studies; no shadows or boxes around catalogue cards |
| K07 | Home section order and the full-width navy scent folio |
| K08 | Search, filter and sort semantics, input limits, normalization, stable sorting; fixture IDs, note IDs, slugs and relationships |
| K09 | Known, unknown, authored-empty and unavailable stay four distinct states, visually and semantically |
| K10 | Mock and synthetic disclosures on every route, never dismissible, never only on hover |
| K11 | Skip link, landmarks, one h1, focus trap and return, history restoration, 44px targets, reduced motion |
| K12 | Per-response nonce CSP, request-time rendering, no-store, noindex, read-only methods, no external runtime request, no cookie or browser storage, no service worker |
| K13 | Loopback-only Docker runtime on `127.0.0.1:3000` |
| K14 | Equal three-column Featured grid and true-centered desktop navigation |

## 3. Design foundation

### 3.1 Color (CHANGE, C01)

Ratios are WCAG 2.x contrast, computed from the hex values. They replace the proposal's approximations.

| Token | Value | paper | surface | surface-muted | gold-50 | navy | Permitted role |
|---|---|---|---|---|---|---|---|
| `divider` | `#D6CFC2` (was `#DDD9D0`) | 1.42 | 1.55 | 1.29 | 1.32 | – | Decorative rule only |
| `gold-50` | `#F3ECDF` (new) | – | – | – | – | – | Row hover, active chip and disclosure background |
| `gold-300` | `#D2BE98` (new) | 1.67 | 1.82 | 1.51 | 1.55 | 8.49 | Decoration only |
| `gold-500` | `#A8875A` (new) | 3.07 | 3.34 | **2.79** | **2.85** | 4.61 | Rules and ornament. Never text. Never the only indicator of state: it is under 3:1 on `surface-muted` and `gold-50` |
| `bronze-700` | `#7A5C33` (new) | 5.66 | 6.17 | 5.14 | 5.25 | **2.50** | Gold text on light surfaces only |
| `tobacco-900` | `#3B2C1E` (new) | 12.32 | 13.42 | 11.18 | 11.42 | **1.15** | Warm strong detail and link hover on light surfaces |
| `gold-on-navy` | `#C9A96E` (new) | **2.05** | – | – | – | 6.89 | Text, numerals and rules on navy only |

- Retained exactly: `paper`, `surface`, `surface-muted`, `ink`, `text-secondary`, `navy`, `focus`, `on-dark`, `control-border`, `error`, `success`, `scrim`.
- Aliases for existing components: `gold` becomes `gold-500`, `gold-readable` becomes `bronze-700`. The V1 values `#AD9361` and `#75613A` retire. The token test that pins the V1 values is updated in the same commit, with the reason.
- Control boundaries stay `control-border` (3.85 on paper, 3.57 on `gold-50`). Focus stays navy, 2px, paper on dark.
- Colors come from semantic tokens only. No gradient, metallic text, gold shadow or gold box around cards. Guide proportion: gold and bronze together at most about 3% of a viewport.

### 3.2 Rules R1–R5 (CHANGE, C02)

| Rule | Form | Used for |
|---|---|---|
| R1 masthead | Ink 2px, gap 3px, `gold-500` 1px | Under the header and above the footer, every page |
| R2 section opener | Ink 1px full width with a 48×2px `gold-500` tab at the start | Main page sections |
| R3 strong | Ink 1px | List and table headings |
| R4 item | `divider` 1px | Between rows |
| R5 vertical accent | `gold-500` 1px on paper; `gold-on-navy` on navy | Explore by scent columns, folio |

Only 1px and 2px strokes. One boundary carries one rule; a section never closes with a rule where the footer opens with R1. The reported doubled line at the end of Explore is reproduced before it is fixed. Rules are drawn with borders or pseudo-elements, never a gradient, and survive forced colors. They carry no information.

### 3.3 Typography (CHANGE C03, TEST T1)

| Role | English desktop / mobile | Thai desktop / mobile | Face |
|---|---|---|---|
| Hero | 72/1.04, 44/1.10 (V1) | 64/1.30, 38/1.35 | Display |
| Page | 56/1.10, 36/1.18 (V1) | 50/1.35, 32/1.40 | Display |
| Section | 40/1.15, 30/1.25 (V1) | 36/1.40, 28/1.45 | Display |
| Entry title | 26/1.20, 22/1.30 (was Noto 500 24/22) | 24/1.45, 21/1.50 | Display in English; Thai face follows T1 |
| Body | 16/1.60 | 16/1.75 | Noto Sans Thai |
| Long form | 18/1.65 | 18/1.80 | Noto Sans Thai |
| Meta | 14/1.50 | 14/1.60 | Noto Sans Thai |

- Sizes are rem. Thai values are starting points for the specimen and may move with the selected face.
- Thai text never gets letter-spacing, uppercase or a Latin display line-height. Digits are Arabic in both languages; counts use tabular figures.
- Thai headings wrap at word boundaries. Dictionary text may carry explicit break points; `text-wrap: balance` is an enhancement only.
- The V1 rule "display face only at 32px and above" is relaxed for entry titles. If Bodoni hairlines fail inspection at 22px, entry titles return to the V1 face and the result is recorded.
- Uppercase stays limited to the wordmark. Section numbering is selective: see section 6. Buttons stay in sentence case.

### 3.4 Thai display font comparison (TEST T1)

The Owner rejected the earlier Thai direction (Trirong). **No Thai display font is selected by this plan.** Until the Owner selects one from rendered specimens, Thai headings keep the V1 Noto Sans Thai fallback and no candidate enters `web/src/fonts`.

| Candidate | Thai display | Weights | Standing |
|---|---|---|---|
| Control | Noto Sans Thai | 500 | V1 baseline, for reference |
| A | Chonburi | 400 | Required |
| B | Fahkwang | 300, 400 | Required |
| C | Taviraj | 300, 400 | Secondary comparison |
| D | Chonburi for hero and page, Fahkwang below | – | Only if A and B renderings justify it |

Protocol:

1. Obtain each candidate from an authoritative source at a pinned revision. Record the source URL, revision, license text and its hash, file SHA-256, WOFF2 bytes and subsetting method. A candidate without a confirmed self-hosting license is dropped.
2. Build the specimen outside the application: Git-ignored local tooling on loopback. It is not a route and never enters the preview image. The proposal's `/dev/type-specimen` route is REJECTED for that reason.
3. Render the same project text in every candidate: hero, page, section and card titles; "แผนที่กลิ่นส่วนตัว", "สมุดบันทึกที่บอกตรง ๆ ว่ามันยังไม่รู้อะไร", "แบบศึกษากระดาษลำดับที่สิบสอง"; the mark stress string "ปั้น ฟ้า ญี่ปุ่น ฎีกา ฐ์ ที่สุด น้ำหอม กลิ่นชั้นบน"; mixed Latin and Thai; body and metadata.
4. Sizes 72, 56, 40, 26, 22 and the Thai equivalents; on paper and navy; at 200% zoom; Chrome and Edge on Windows. A physical phone is NOT RUN unless the Owner performs it.
5. Record per candidate: clipped or colliding marks, ink density beside Bodoni Moda 400, metric overrides needed, layout shift on swap, bytes added.
6. Present one comparison sheet. The Owner selects A, B, C, D or the control.

Budget: at most 150 KB of WOFF2 added for all new faces on a Thai page, as a ceiling to verify, not a target. An English page without Thai text downloads no Thai display font. V1 fonts total 119,876 bytes. No CDN and no build-time remote font fetch.

## 4. Localization

### 4.1 Routes (Owner-directed, CHANGE C04)

| Logical route | English | Thai |
|---|---|---|
| Home | `/` | `/th` |
| Explore | `/explore` | `/th/explore` |
| Detail | `/perfume/[slug]` | `/th/perfume/[slug]` |
| Notes | `/notes` | `/th/notes` |
| About | `/about` | `/th/about` |

Exactly two locales. `/en`, `/en/*`, `/TH`, any other locale prefix and every unknown path return a real 404. Slugs, IDs, query keys and fragment IDs are the same in both languages. No language cookie, `localStorage`, `Accept-Language` redirect, tracking or persistence; the proposal's `dp_locale` cookie is REJECTED.

### 4.2 Architecture (CHANGE C05, proven by a spike first)

Preferred: two root layouts, `app/(en)/` and `app/th/`, both rendering one shared shell and shared views with a typed locale. The bundled Next.js 16.4.6 documentation states that multiple root layouts are supported and that moving between them is a full page load. This gives the right `<html lang>` from the server, no wrong-language flash, a structural allowlist and no rewrite in the proxy.

| Concern | Contract |
|---|---|
| Not found | The same documentation says a single global 404 cannot be composed over multiple root layouts. Use a catch-all per tree that calls `notFound()`. The experimental `globalNotFound` flag is not adopted without Owner approval |
| Undecodable address | `proxy.ts` serves the Thai unavailable view for a raw path under `/th/`, otherwise English. No other proxy change is expected |
| Global error | No dependable locale there, so it shows both languages, each with its `lang` |
| Fallback | One `[locale]` root layout with an allowlisted internal rewrite, if the spike fails |
| Spike must show | Server `lang` on first byte; 404 status, nonce CSP, no-store and noindex on both 404 views; no CSP violation; English URLs unchanged; no locale hydration mismatch. If neither layout passes, stop and report |

### 4.3 Text (CHANGE C06)

- UI text lives in typed English and Thai dictionaries with one shared shape; a missing key fails the type check. JSON message files are not used.
- Fixture prose gets a separate **server-only Thai overlay keyed by existing IDs**. English fixture records stay byte-identical. The overlay may translate a description, note or family descriptor, article title, excerpt or body, or an image caption. It may not add records, names, notes or relationships, and may not give text to a field whose state is unknown.
- Each overlay text is `draft` or `reviewed`. The implementer writes faithful drafts and delivers one English/Thai review sheet to the Owner; only the Owner marks text reviewed.
- A missing translation shows the English source with `lang="en"`. No run-time or automatic translation.
- Fictional proper names (perfume, note and house names) stay unchanged. Family and accord labels also stay unchanged until V11-OD-04.
- Paper study L is authored in Thai. English pages keep showing it in Thai with `lang="th"`, as V1 does.
- Localized: navigation, footer, titles and metadata, all five pages, search labels, help and placeholders, filters, sort, counts, chips, mock disclosures, dialogs, drawer, pending and restoration messages, error, 404 and accessible names. A Thai page without its Thai mock disclosure is a failure.

Draft glossary, for Owner correction (V11-OD-03):

| English | Thai draft |
|---|---|
| Home / Explore / Notes / About | หน้าแรก / สำรวจ / โน้ตกลิ่น / เกี่ยวกับ |
| Top / Heart / Base | ชั้นบน / ชั้นกลาง / ชั้นฐาน (alternative: ท็อปโน้ต / ฮาร์ตโน้ต / เบสโน้ต) |
| General notes / Accords / Family | โน้ตทั่วไป / แอคคอร์ด / ตระกูลกลิ่น |
| Mock / mock study | จำลอง / แบบศึกษาจำลอง |
| Not supplied / Family unknown / No entries | ไม่ได้ระบุ / ไม่ทราบตระกูลกลิ่น / ไม่มีรายการ |
| A personal atlas of scent. | แผนที่กลิ่นส่วนตัว |

"Not supplied" (unknown) and "No entries" (authored empty) must stay different phrases in Thai.

### 4.4 Language switch behavior (CHANGE C07)

- Switching keeps the logical page, slug, recognized `family` and `note` filters and a valid fragment. Invalid filters and unsupported keys are dropped.
- It is a normal document navigation. Typed search text, sort and open disclosures reset, exactly as a hard reload does in V1. Scroll position is not carried.
- It works without scripting (the fragment is added only with scripting).
- Every internal link stays inside the current locale. Head `hreflang` alternates use same-origin relative URLs; if the framework forces an absolute origin, omit them and keep `hreflang` on the links.

### 4.5 Search (CHANGE C08)

- English results must not change. Thai overlay text takes part on English pages only when it is `reviewed` **and** the query contains a Thai character.
- On Thai pages the displayed text and the English source are both searched.
- Limit of 120 code points, NFKC, case folding, literal matching, AND across filters, sort and ID tie-break are unchanged. The four result states are unchanged.

## 5. Header and language selector

### 5.1 Sticky header (Owner-directed, CHANGE C09; TEST T5)

- `DOOMPARFUM BY TK | Home Explore Notes About | Search Profile TH EN`. Equal outer tracks keep the navigation centered within 1px, with the wider utilities included.
- Sticky, opaque paper, R1 below. **Stable height, no shrink animation, BY TK always visible.** The compact-on-scroll variant is TEST T5 only.
- Layering: header 20, scrim 40, dialogs 50, focused skip link 100. The proposal's header `z-index: 40` equals the V1 scrim and is REJECTED.
- `scroll-padding-top` is the header height plus 24px. CSS gives a rem fallback per layout; script refines it from the measured height, because text enlargement makes the proposal's fixed px values wrong.
- Anchors, skip link, route headings, restored entries and tabbed controls are never fully hidden under the header. This is an added product criterion (WCAG 2.2 SC 2.4.11); the conformance target stays WCAG 2.1 AA.
- Not sticky when the viewport is at most 31.25rem high, when the header reflows to two rows, in print, or wherever it would cover more than 20% of the viewport height. The reason is recorded with evidence.
- Sticky works without scripting. The header does not hide on scroll.

### 5.2 Language selector (CHANGE C10; TEST T6)

| Width | Contract |
|---|---|
| Desktop | Immediately after Profile, separated by a 1px divider: `TH` and `EN`, each 44×44px. The current one has `aria-current="true"`, heavier weight and underline |
| Narrow | One compact 44px link to the other language, immediately after Profile, wherever it fits without squeezing the wordmark |
| Very narrow or enlarged text | Header reflows to two rows. The control is never removed to keep one row |
| Complementary | Both languages at the top of the drawer and in the footer |

Links, not toggle buttons, each with `hreflang` and `lang`, inside a labelled group. No flags. The visible label stays inside the accessible name (`TH` plus hidden "ภาษาไทย"): the proposal's `aria-label` replacement would fail label-in-name (WCAG 2.5.3).

## 6. Pages

| Page | CHANGE | TEST (default until selected) |
|---|---|---|
| Home | R2 openers and one section rhythm; Entry titles in display; R5 separators, clear counts and one full-area link per scent family; folio Roman numerals I–III and layer copy moved beside its heading; journal rows with one clear link each | **T2 hero**: masthead against vertically centered (default V1). "Vol. I — Mock edition" is new copy and needs Owner approval. **T7 Featured**: 6/3/3 against equal (default equal). Card numerals 01–03 off by default because V1 forbids ranking cues |
| Explore | Catalogue starts higher: first visual top at most 560px at 1440×900 and 1280×900 (V1: 653px). Visible labels and help stay. Full control borders. Chips with 44px targets. Metadata aligned across titles of different length and script | **T4 toolbar**: compact against boxed (default boxed). Underline-only selects and visually hidden help are REJECTED as defaults |
| Detail | Layer rules, headings and Roman numerals consistent with the folio; unknown, authored-empty and unavailable wording distinct in type as well as text; arrow-style family link | **T3 spread**: record sheet from existing fixture fields only, against a simpler balanced spread (default V1 7/5). V1 fact: at 1440×900 the text ends near 570px beside art ending at 1202px. "More in this family" is one plain link to the filtered Explore view; no recommendation list |
| Notes | Larger group letters in `bronze-700`; jump index of **live letters only**, from displayed names; refined search, filter and membership list; counts unchanged | Sticky sidebar where height allows (default off). Thai grouping only where reviewed Thai names exist; none exist now, so grouping stays Latin. No generated initials, no dead letters |
| About | Long-form measure and rhythm; sticky contents with scrollspy (`aria-current="location"`) where height allows; contents disclosure on narrow screens; anchors unchanged | Margin quotes reuse existing sentences and are hidden from assistive technology. Drop cap English only (default off) |

Shared components: buttons, inputs, selects (native stays), chips, cards, links, disclosures, dialogs, drawer, footer, synthetic notice, error and empty states follow the tokens and rules above. Corners: square or nearly square where the rendering benefits (T8). Search input text stays sans. Nothing becomes a related-product feature, score, weight or concentration.

### 6.1 Reported H1 outline (CHANGE C11, reproduced)

V1 already suppresses the outline on programmatic focus with `:focus-visible`. The proposal's CSS is equivalent and would change nothing. Measured in Chrome on the running V1 preview:

| Path to the page | Outline on h1 |
|---|---|
| Mouse: navigation, card, footer, search result; after typing; after paging keys | None (6 cases) |
| Hard load | None, h1 not focused |
| Keyboard: Enter on navigation | Shown, intended |
| Mouse navigation, **then any key press** (Shift, PrintScreen) | Shown |

The last case matches a screenshot taken with a shortcut. Contract: remember whether the navigation was by pointer or keyboard. Keyboard navigation keeps the ring. After pointer navigation a later key press does not draw a ring on the heading. Screen-reader focus on the h1 is unchanged, and interactive elements keep their ring in every case.

## 7. Motion

V1 tokens stay. Optional: link underline color 120ms; image hover scale at most 1.02 over 240ms; one R2 tab draw of at most 480ms on first entry. All off under reduced motion, none block input or hide content. Header animation is not part of the default.

## 8. Owner comparison batch

One review, real browser screenshots, baseline included. V1 behavior stays until the Owner selects.

| ID | Comparison | Default |
|---|---|---|
| T1 | Thai display font: control, Chonburi, Fahkwang, Taviraj, optional hybrid | Noto Sans Thai |
| T2 | Home hero: V1, masthead, centered | V1 |
| T3 | Detail: V1 7/5, record sheet, simpler balanced spread | V1 |
| T4 | Explore controls: boxed, compact toolbar | Boxed |
| T5 | Header: stable, compact on scroll (only if worthwhile) | Stable |
| T6 | Narrow language control arrangements | Compact link after Profile |
| T7 | Featured: equal, 6/3/3 (only if materially better) | Equal |
| T8 | Corners: V1 2/4/8px, square | V1 |

Not every alternative in the proposal is built. A rejected alternative leaves no code behind.

## 9. Implementation task map

One proposed task, `IMP-WEB-02` (ID unallocated until Gate C intake), one branch `feat/frontend-v1-1-design-upgrade` from merged `main`, one Draft PR, internal checkpoints.

| Checkpoint | Work | Exit evidence |
|---|---|---|
| CP0 | Verify merge SHA, rerun the V1 suites on `main`, before screenshots | Recorded counts; no source change |
| CP1 Foundation | C01, C02, C03; T1 specimen | Token, contrast and rule tests; specimen sheet and font record |
| CP2 Language and header | 4.2 spike, then C04–C10 | Spike record; locale, coverage, switch, sticky and focus tests |
| CP3 Pages | Section 6, C11 | Page tests; before and after at the review widths |
| CP4 Owner batch | T1–T8 sheet, translation review sheet | One Owner answer; unselected variants removed |
| CP5 Verification | Section 10, Docker rebuild, independent review, records | V01–V16; exact SHA; PR ready for Owner review |

CP1 and CP2 may proceed while T1 is open. The PR is not Ready for Review until the T1 answer (which may be "keep Noto Sans Thai") and the translation review state are recorded.

Design tools per phase, one primary and at most one complementary, under the project rules: CP1 Impeccable (colorize, typeset) with Taste Skill; CP2 Impeccable (adapt, harden) with UI Craft; CP3 Taste Skill with Impeccable (layout, distill); CP4 critique; CP5 Impeccable (audit, polish, `detect`). `bolder`, `overdrive`, `animate` and `delight` run only if they improve the approved design. `ui-ux-pro-max:brand` is out of scope. No hook, MCP, Live Apply, image fetch or permission bypass.

## 10. Acceptance criteria

A01–A12 in [[Luxury_Frontend_Acceptance_and_Task_Map]] stay in force and are rerun for **both** languages, amended as in section 12. New criteria, all NOT RUN:

| ID | Pass condition |
|---|---|
| V01 | All ten URLs return 200 with correct server `lang`, localized title, one h1 and the mock disclosure; `/en`, `/en/explore`, `/TH`, `/fr`, unknown slugs and paths return 404 in the right language |
| V02 | Missing dictionary key fails the type check. On Thai pages every visible or accessible text is Thai, or inside `lang="en"`, or an allowlisted name, numeral or wordmark |
| V03 | English pages: text, URLs, results, counts and fixture records equal V1 except for listed changes |
| V04 | Overlay validator rejects an unknown ID, an added name or note, text for an unknown field, over-long or unsafe text |
| V05 | Switching keeps page, slug, recognized filters and fragment both ways; drops invalid ones; works without scripting; no cookie or storage write; no internal link leaves the locale |
| V06 | Search: section 4.5 rules with English-unchanged proof, Thai, mixed, combining-mark and 120-code-point cases; four result states distinct in both languages |
| V07 | Header stays in view, stable height, opaque; nothing focused or targeted is fully hidden under it; documented non-sticky fallbacks work |
| V08 | Navigation center within 1px at 1024, 1280, 1440 and 1920 in both languages, with right-side content stressed from 200 to 260px |
| V09 | Language control present and 44px at every width from 320px, at 200% text and 400% zoom; drawer and footer links work; label in name |
| V10 | Every text pair at least 4.5:1 (large 3:1), control and state indicators at least 3:1, computed from tokens; `gold-300`, `gold-500` and `divider` never text; bronze and tobacco never on navy; `gold-on-navy` never on paper |
| V11 | R1 identical on every page; no two adjacent rules at one boundary; forced colors readable |
| V12 | Thai marks unclipped and uncollided in every role at V1.1 line heights; no Thai tracking; no clipped or overflowing Thai at 320, 375, 390, 768, 1024, 1280, 1440 and 1920px, 200% text, 400% zoom and WCAG 1.4.12 spacing |
| V13 | H1 outline behaves as in 6.1 in all listed cases; every interactive element shows focus |
| V14 | Font record complete; license file beside every shipped face; NOTICE and Local credits updated; budgets in 3.4; initial JS at most 200 KiB gzip per route and CLS at most 0.1 in both languages |
| V15 | CSP, noindex, no-store, method refusal, origin and network isolation pass for `/th` and both 404 views; client chunks contain no fixture or overlay prose |
| V16 | Type check, lint, unit, Chrome and Edge suites, clean `npm ci`, uncached image build and preview smoke pass; before and after screenshots at 1920, 1440, 1024, 768 and 390px, English and Thai |

Historical counts (85 unit, 189 Chrome, 189 Edge) are a baseline, not a target. A changed or removed test needs a stated reason. Screen reader, physical phone, Safari, Firefox and the LAN probe are NOT RUN unless someone runs them; A05 stays PARTIAL until then. No WCAG conformance claim.

Detector baseline on V1 (Impeccable `detect`, five routes): `cream-palette` (Owner-approved ivory, not a defect) and `undersized-ui-text` for the 10px "BY TK" (V11-OD-08).

## 11. Owner decisions

| ID | Decision | State |
|---|---|---|
| V11-OD-01 | Thai display font (T1) | OPEN, after specimens only |
| V11-OD-02 | English at existing paths, Thai under `/th`, no cookie | OWNER-DIRECTED; effective on merge |
| V11-OD-03 | Thai glossary, especially Top, Heart and Base | OPEN; drafts in 4.3 |
| V11-OD-04 | Family and accord labels: keep Latin or translate; note transliteration | OPEN; default unchanged. Proper names unchanged is OWNER-DIRECTED |
| V11-OD-05 | Hero, Detail and Explore alternatives (T2, T3, T4) | OPEN, CP4 |
| V11-OD-06 | Header and narrow selector (T5, T6) | Stable header OWNER-DIRECTED as default; rest OPEN, CP4 |
| V11-OD-07 | Wordmark | OWNER-DIRECTED: keep |
| V11-OD-08 | "BY TK" signature: 10px or 11px | OPEN; default 10px |
| V11-OD-09 | Corners and Featured (T7, T8) | OPEN, CP4 |
| V11-OD-10 | English version of Paper study L | OPEN; default none |
| V11-OD-11 | Bounded Gate C setup: download of the pinned candidate fonts for the specimen | OPEN; granted only if stated with the Gate C start |
| V11-OD-12 | Publishing the exact proposal text in this public repository | OPEN, not blocking; default not published, hash and trace only |

## 12. Clauses this amendment supersedes

| V1 contract | Superseded clause | By |
|---|---|---|
| [[Luxury_Design_Tokens_and_Components]] | `gold`, `gold-readable`, `divider` values; gold occurrence limit; display face only at 32px and above; entry type role; Thai headings always in the body face; "No sticky global navigation"; z-index list gains header 20 | 3.1–3.4, 5.1 |
| [[Luxury_Routes_and_Wireframes]] | Single-language routes and titles; header "in normal document flow" with a 1px divider; utilities "Search and Profile"; Notes jump index exclusion (live letters now allowed); Detail and hero compositions where a TEST variant is selected | 4, 5, 6 |
| [[Luxury_Mock_Fixture_Contract]] | Adds the server-only Thai overlay and locale search rules; nothing is removed | 4.3, 4.5 |
| [[Luxury_Frontend_Acceptance_and_Task_Map]] | A01, A08 and A09 extended; V01–V16 added; new task unit | 9, 10 |
| [[Luxury_Docker_Runtime_Proposal]] | None. Undecodable `/th/` addresses get the Thai unavailable view | 4.2 |
| PRODUCT.md | "a full locale switch is not requested" | 4 |

## 13. Proposal traceability

| Proposal section | Disposition |
|---|---|
| §1 KEEP | ADOPTED, K01–K14 |
| §2.1 color | ADOPTED with measured ratios and tighter roles |
| §2.2 rules | ADOPTED |
| §2.3 type | ADOPTED with limits; fonts TEST; specimen route REJECTED; per-section uppercase eyebrows REJECTED |
| §2.4 rhythm | ADOPTED as one section token; V1 phone value 48px may rise to 64px |
| §2.5 components | MODIFIED: sentence-case buttons, selective numbering, focus fix replaced by 6.1, radius TEST |
| §2.6 motion | Optional; header compact TEST |
| §3.1, §8 header | MODIFIED: stable default, layering and measured offsets corrected |
| §3.2 switcher | MODIFIED: control stays beside Profile; label in name corrected |
| §3.3–§3.7 | ADOPTED in the restrained form; search input stays sans |
| §4.1–§4.5 pages | MODIFIED, section 6 |
| §5 responsive | ADOPTED except: sticky is not assumed on phones where 5.1 excludes it; Explore bottom sheet REJECTED (V1 in-flow disclosure stays) |
| §6, §11 checks | ADOPTED in V01–V16 |
| §7 fonts | ADOPTED; 150 KB is a ceiling |
| §9 i18n | MODIFIED: no cookie, typed dictionaries, overlay instead of changed fixture fields |
| §10 A/B | Mapped to CP1–CP4. §10 C real-data items DEFERRED |
| §12 open decisions | Section 11 |
| §13 guardrails | ADOPTED, except one PR per item: one task, one PR, internal checkpoints |

## 14. Boundaries

Mock only. No real catalogue data, API, database, matching, authentication, collection, purchase, price, score, public exposure, tunnel or Production change. PostgreSQL containers and volumes, PR #8, Security U01/r14, ETL, migrations and receipts are untouched. No new twenty-site research. The local, untracked project rule file for design tools still pins V1 token values; after this merge it needs the Owner's update so that tools do not enforce retired values.

Rollback: revert the documentation PR. No runtime effect.
