---
id: DPT-UX-LUXURY-TOKENS
project: DoomParfum By TK
type: design_system_proposal
status: proposed
owner: human-owner
updated: 2026-11-23
tags: [doomparfum, tokens, typography, components, motion]
source_of_truth: "../../README.md"
---

# Luxury design tokens and component inventory

PROPOSED, documentation only. [[DPT-PLAN-012_Luxury_Frontend_Editorial]] / [[Luxury_Routes_and_Wireframes]]. The Owner confirmed the attached direction. No existing design token system or DESIGN.md was found. This note owns proposed values until implementation establishes verified visual authority; it does not claim a shipped design system.

## Color and surfaces

| Token | Value | Semantic role / restriction |
|---|---|---|
| `--color-paper` | `#F7F5F0` | Primary ivory background |
| `--color-surface` | `#FFFFFF` | Dialogs and occasional elevated functional surfaces |
| `--color-surface-muted` | `#EEEAE2` | Abstract visual field, disabled surface; never implies data state by itself |
| `--color-ink` | `#161719` | Main text and primary action fill |
| `--color-text-secondary` | `#5C5A55` | Secondary text on paper/white |
| `--color-gold` | `#AD9361` | Owner's muted gold; decorative fine rule/material detail only on ivory/white. Not normal text, not sole control boundary. |
| `--color-gold-readable` | `#75613A` | Textual gold accent on paper/white if needed; underline still required for links |
| `--color-navy` | `#14253D` | One optional editorial story background; subordinate to ink, never a competing primary CTA |
| `--color-on-dark` | `#F7F5F0` | Text on ink/navy |
| `--color-divider` | `#DDD9D0` | Decorative divider only; insufficient for an essential input border |
| `--color-control-border` | `#817B70` | Functional input outline on paper/white |
| `--color-focus` | `#14253D` | Visible ring on paper/white |
| `--color-error` | `#9A302C` | Error text/icon on paper/white, always with words |
| `--color-success` | `#365E47` | Success text/icon on paper/white if an actual local action warrants it |
| `--color-scrim` | `rgba(22,23,25,0.50)` | Modal background separation; validate composed result |

Gold and divider are part of the brief, not permission to use low-contrast text. Exact contrast calculations and accepted pair roles are recorded in the task's validation evidence. Required thresholds: ≥4.5:1 normal text, ≥3:1 large text and meaningful control boundaries/indicators. Use ink primary buttons with paper text; hover fill navy. Selected filters retain text and check/underline, not color alone. Never put gold text on gold fill. Navy/ink surfaces use paper text and paper focus ring. Only these light and dark regions are proposed; a full dark-mode toggle is out of scope and untested.

Neutral surfaces dominate. Gold appears at most in one story rule, a small brand/material detail and a selected decorative marker per viewport. Navy is a bounded story panel rather than a second accent scattered across controls. No gradients, glow, glass panels, ornamental blobs or fake material textures.

## Typography

Proposed display: Bodoni Moda, roman 400/500, only for English editorial display ≥32px. Proposed body/control face: Noto Sans Thai, 400/500/600, with system sans fallback for missing glyphs. Thai headings use the body face at corresponding scale, normal letter spacing and line-height ≥1.35; never force Latin display tracking onto Thai. Use no third decorative/mono family. Numerals in counts use tabular figures where supported.

Official Google Fonts license texts list SIL OFL 1.1 for [Bodoni Moda](https://raw.githubusercontent.com/google/fonts/main/ofl/bodonimoda/OFL.txt) and [Noto Sans Thai](https://raw.githubusercontent.com/google/fonts/main/ofl/notosansthai/OFL.txt), inspected 2026-11-23. No font binaries downloaded. A later implementation must pin the exact font files/commit, retain notices and verify glyphs; otherwise ship the system fallback and record the visual difference. No Google Fonts CDN requests or build-time automatic remote font fetch. These fonts are type assets with explicit licenses, not third-party product imagery.

| Role token | Desktop size / line-height | Mobile size / line-height | Weight / tracking |
|---|---|---|---|
| `--type-hero` | 72px / 1.04 | 44px / 1.10 | 400, -.02em Latin; 40px at ≤359px |
| `--type-page` | 56px / 1.10 | 36px / 1.18 | 400, -.015em Latin |
| `--type-section` | 40px / 1.15 | 30px / 1.25 | 400, -.01em Latin |
| `--type-entry` | 24px / 1.30 | 22px / 1.35 | 500, normal |
| `--type-body` | 16px / 1.60 | 16px / 1.60 | 400, normal |
| `--type-control` | 15px / 1.50 | 16px / 1.50 | 500, normal |
| `--type-meta` | 14px / 1.50 | 14px / 1.50 | 400, normal |
| `--type-brand` | 20px / 1.10 | 14–18px / 1.15 | 500, .06em Latin |
| `--type-signature` | 10px / 1.4 | 10px / 1.4 | 500, .10em, brand signature only |

Use rem equivalents at a 16px base, preserving user font scaling. No essential label below 14px. Headline line breaks are natural, `text-wrap:balance` only as progressive enhancement. Body ≤65ch; short hero copy ≤38ch. No uppercase section eyebrows repeated everywhere. The uppercase wordmark is the deliberate identity exception.

## Space, geometry, grid and layers

Spacing tokens in px (implemented as rem): `--space-1=4`, `2=8`, `3=12`, `4=16`, `5=24`, `6=32`, `7=48`, `8=64`, `9=80`, `10=96`, `11=128`. Internal control gap 8; related fields 16; collection gap 24; section gap desktop 96 (story 128), tablet 64, phone 48 (story 64). Do not pad every section equally. Header and grid breakpoints follow [[Luxury_Routes_and_Wireframes]] exactly: 480, 640, 768, 1024 and 1280px; 1440px max content; 16/24/48px gutters.

Radius: visual tiles 0px; buttons 2px; inputs 4px; dialogs 8px. No blanket rounded cards. Borders: 1px rules; 2px focus ring with 3px offset. Dialog shadow only: `0 2px 8px rgba(22,23,25,.08), 0 16px 48px rgba(22,23,25,.12)`. No shadow on catalogue items. Z-index: base 0; local disclosure 10; scrim 40; dialog 50; skip link while focused 100. No sticky global navigation in this proposal.

Minimum target 44 × 44 CSS px, spacing ≥8px between adjacent icon targets. Text links in prose remain inline; standalone note links get padded hit regions. Media aspect ratios: hero 5:4, catalogue 4:5, phone detail 4:3. Dimensions reserved to prevent layout shifts. All visual fields use original local abstract art or an explicitly authored typographic study.

## Motion, delight and overdrive boundary

| Token / interaction | Exact proposal | Reduced-motion behavior |
|---|---|---|
| `--motion-feedback` | 120ms color/opacity, `ease-out` | Immediate state change |
| `--motion-enter` | 240ms opacity + translateY 8px, `cubic-bezier(.2,.7,.2,1)` | No transform, no entrance delay |
| `--motion-exit` | 160ms opacity, `ease-in` | Immediate close |
| `--motion-drawer` | 280ms transform + opacity, same enter ease; exit 180ms | Immediate panel change with focus contract intact |
| Scent folio | At most one 240ms emphasis per layer on first entry; no pinned scrolling, looping or dependency on animation end | All layers fully visible, no observer required |
| Link affordance | Underline/contrast change within 120ms; no moving text baseline | Same readable underline state |

Only transform/opacity/color transitions; no `transition:all`. Search results, typing, selection and counts update immediately. Motion never blocks input. Rapid reopen/close cancels prior transition; final semantic state is explicit. Do not await animation end to unlock scroll, move focus or navigate. No scroll hijack, cursor replacement, magnetic controls, autoplay video/audio, WebGL or new animation dependency. Overdrive is interpreted as compositional ambition inside the Owner's restrained direction: a memorable folio, not effect accumulation. Delight is precise focus return, readable note cross-links and well-written unknown states; no confetti, rewards, fake scent particles or sound.

## Component inventory and contracts

| Component | Elements / states / responsibility |
|---|---|
| AppFrame / SiteHeader / SiteFooter | Landmarks, skip link, current route, centered desktop geometry and narrow drawer |
| WordmarkLink / IconButton | Owned text identity; one SVG icon family, 20px icons, accessible names; no emoji |
| NavigationDrawer / SearchDialog / ProfileNotice | Closed/open; initial focus, trap, Escape, inert background, focus restoration; one overlay at a time |
| SyntheticNotice / MockLabel | Shared concise disclosure at route entry and every fixture card/detail; never dismissed or hidden by hover |
| EditorialHero / ScentFolio / JournalPreview | Authored original content and stable responsive composition; nonessential motion only |
| PerfumeStudyEntry / StudyVisual | One coherent title/visual link, fictional house, explicit field states; default/focus/visual fallback |
| CatalogueControls / ResultCount | Labelled search/selects, all/filtered/zero/invalid states; shared pure filter semantics |
| NoteIndex / NoteLink / NoteLayerList | Explicit note IDs/layer membership; text labels, no color-only meaning; unknown and authored-empty distinct |
| FieldValue / UnavailableView / RenderError | Shared known/unknown/empty/unavailable language; Retry or return action where meaningful |
| Disclosure | Native details/summary for supporting explanations; essential layer text remains visible |

Prefer native HTML plus Tailwind semantic-token utilities. Selective shadcn usage is limited to accessible dialog primitives; no wholesale dashboard theme or component generator run is authorized. Icons: one locally bundled family selected/pinned during implementation; existing project family takes precedence if one appears. No remote icon service. All component names above are proposals, not existing files or installed modules.
