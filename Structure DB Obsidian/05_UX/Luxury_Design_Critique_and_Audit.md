---
id: DPT-UX-LUXURY-REVIEW
project: DoomParfum By TK
type: planning_critique
status: proposed
owner: human-owner
updated: 2026-11-23
tags: [doomparfum, critique, audit, planning]
source_of_truth: "../../README.md"
---

# Luxury planning critique and audit

Target: [[Luxury_Routes_and_Wireframes]], [[Luxury_Design_Tokens_and_Components]] and the mock/runtime contracts. This is a design-specification review. No rendered DoomParfum frontend exists. Source/UI score, runtime accessibility conformance, animation performance and Docker verification are NOT ASSESSED. Method: independent read-only design assessment A and evidence/accessibility-contract assessment B, followed by parent reconciliation; exact reports/checkpoint identities will be recorded in the task's S1 report. No UI detector result is substituted for a review of unbuilt screens.

## Independent planning review reconciliation

Assessment A (`design_review`) found three P2 gaps: Explore's heading conflicted with the page token; Search lacked virtual-keyboard handling; history navigation lacked a focus/scroll exception. All three were corrected and independently rechecked as RESOLVED IN PROPOSED DESIGN. Original PUBLIC_SAFE report SHA-256 `915b77271064767a44f09e3b63b897e83bdc7154cea744edff49f3e536dcb012`; separate closure addendum `185163bc9526c7cfaa0f4e63afb0316e3550c500bfbe3dda036d9a2bc2d969fc`. The original was not rewritten.

Assessment B (`evidence_audit`) found a MEDIUM sequencing gap (render evidence preceded Docker setup) and LOW missing text-spacing acceptance. LF-01 now supplies the minimal Docker runtime before LF-02 rendering; A08 includes WCAG 1.4.12 spacing overrides. Both were independently rechecked; no open planning finding remains in that review. PUBLIC_SAFE report SHA-256 `4cff2c48058159dd53b5290ea3cc6028109e1e4cac591b14344c9f528f3d6bb3`.

Each reviewer used isolated context and snapshot hashes; the source checkpoint/retention verification is recorded in the S1 report. Reviews assess the specification, not implementation acceptance. Assessment B attempted `impeccable detect --json web/` exactly once: exit 1, `Warning: cannot access web/`, `[]`. No markup exists. Detector NOT AVAILABLE FOR THIS TARGET; no clean-design result. No overlay, injected script, local live server or generated critique snapshot was created. Reference research used read-only browser APIs only. Missing rendered measurements remain NOT RUN, not waived.

## Critique

The brief's strongest move is treating perfume exploration as an editorial knowledge tool. Its main risk is borrowing a storefront's purchase language and cinematic behavior while omitting the information needed to explore. The proposed five-route shell retains the editorial tone but makes Search, notes and catalogue state directly operable. Signature detail: the open Top / Heart / Base folio. It must carry readable layer distinctions rather than suggest chemical proportions.

| Priority | Initial proposal / risk | Proposed correction | Why / verification |
|---|---|---|---|
| P1 | Muted gold `#AD9361` as unspecified accent could become text or control boundary on ivory | Restrict decorative gold; use `#75613A` for readable gold text and `#817B70` for essential borders | Gold/ivory = 2.706:1, below both normal-text and 3:1 indicator thresholds; corrected gold = 5.464:1. |
| P1 | “Centered header” could be implemented with space-between despite unequal sides | Equal outer grid tracks with explicit center measurement and fit fallback | A09 specifies ≤1px center error and asymmetric-content stress. Not executed. |
| P1 | Luxury storytelling could present a note pyramid as a recipe or evidence of real products | Label every study; preserve unknown versus empty and general/layered distinctions; use text-first folio | A02/A04 and fixture negative controls; no inferred notes, real claims or percentages. |
| P1 | Client-side catalogue convenience could quietly add persistent fixture caching | Server-only fixtures, ephemeral serialized view, no-store delivery; scan client chunks and storage | A06 verifies implementation; no no-store claim based solely on framework defaults. |
| P2 | Overdrive plus animate/delight could add competing effects and scroll dependence | One compositional signature, restrained transform/opacity, no cinematic arrival gate | Reduced-motion and rapid-state tests A12; normal document flow survives without motion. |
| P2 | Home Journal preview could add unrequested routes or dead links | Two local original sample pieces on About with working anchors | Five route types remain exact; A01 checks destinations. |

Strengths: an explicit mock boundary, a single clear browse path, and typography/spacing proposals that distinguish editorial Home from functional catalogue screens. Main unresolved evidence is rendering, not another style direction. No user study has validated the proposed task path.

### Heuristic evidence boundary

| Heuristic | Planning evidence | Rendered score |
|---|---|---|
| System status | Mock marker, count, loading/error mapping specified | Not assessable |
| Match with real world | Note layers distinguished from recipe/accords | Not assessable |
| Control and freedom | Reset, Escape, Back and focus restoration specified | Not assessable |
| Consistency | Shared five-route frame, controls and token roles | Not assessable |
| Error prevention | Allowlisted IDs and fixture rejection rules | Not assessable |
| Recognition | Named notes, visible labels, no hover-only information | Not assessable |
| Efficiency | Direct catalogue and note links; no forced animation | Not assessable |
| Minimalist design | One primary action and restrained component set | Not assessable |
| Error recovery | Retained query, clear/reset, unavailable and retry views | Not assessable |
| Help/documentation | About explains mock limitations; inline field states | Not assessable |

No total is calculated. A specification cannot earn a UI health score.

## Layout

Apply 12/8/4-column responsive framework, equal-track header, specific 5/7 Home and 7/5 Detail spreads. Use whitespace and ruled rows, not nested rounded cards. Header grows when text needs space; no wordmark/control collision. Proposed findings are resolved in the contract; actual geometry remains A08/A09 work.

## Bolder

Amplify hierarchy with a 72px editorial headline, clear object field and one open folio. Preserve the pinned palette and quiet utility controls. Do not interpret bolder as larger everything, thick borders or aggressive campaign lettering. Aesthetic distinction remains unverified until rendering.

## Overdrive

The brief's restrained motion overrides the command's optional effects toolkit. Proposed ambition is a distinctive scent-reading composition, with no WebGL, parallax, magnetic pointer or autoplay intro. This is a planning disposition; no overdrive effect was implemented.

## Colorize

Map all five supplied palette colors to explicit roles, with contrast-safe alternatives for text and functional borders. Ink remains the primary action; navy belongs to a bounded story region. Contrast is calculated from exact sRGB values; composed image/scrim states require later render tests.

## Animate

Use 120ms feedback, 240ms optional emphasis and 280ms drawer entrance; faster exits, immediate search/filter response. Reduced motion removes spatial movement while retaining legible state feedback. Final state/focus cannot depend on animation completion. No animation code or runtime testing occurred.

## Adapt

Specify phone/tablet/desktop stacking, collection columns, 320px fallback, long Thai/Latin labels, 200% text, zoom and landscape. Reference mobile captures are inspiration and defect warnings, not tests of DoomParfum.

## Harden

Define unknown/empty/unavailable separately, literal text rendering, bounded search, fixture reference validation, one-overlay focus behavior and recovery actions. No account session, write operation or remote fallback is allowed. Full i18n is not claimed; Thai reflow is a required stress case.

## Audit

Planning checks cover token contrast, reference coverage, route contracts, doc links/frontmatter, scope and sensitive-content patterns. Runtime a11y/performance/CSP/responsive/storage/network/Docker tests are NOT RUN. U01 remains outside this mock audit. No successful empty detector scan may imply a clean implementation.

## Polish

Plan alignment, native control states, consistent caption measures, tabular counts, final type fallback and focus visibility checks together in one bounded render pass and one confirmation pass. No UI polish edits are possible before the Gate P merge and implementation.

## Delight

Precise note cross-links, trustworthy unknown-state language and reliable focus return provide the proposed delight. Avoid false scent simulation, sound, particles or rewards. No extra interaction should delay task completion.

## Distill

Keep four primary destinations, two utility controls, one Home primary action and two filter groups. Omit storefront checkout, promotions, social proof, newsletter and density switch. Deferred product requirements are preserved in the broader IA, not silently deleted. No runtime feature has been removed because none exists yet.

## Tool scope and next step

Impeccable v4.5.2 is the primary design method; ui-craft supplies discovery/anti-template/state-review guidance; ui-ux-pro-max local searches supplement it. Its initial Liquid Glass system recommendation was rejected as off-brief. One narrowed style search returned exaggerated-minimalism/editorial-grid examples; only hierarchy/grid principles were retained. The next valid step is Owner review of the concrete Planning PR package, followed by authorized implementation and then measured critique/audit/polish of the actual screens. Questions skipped: the Owner already confirmed the attached visual direction; publication authorization remains a separate final action.
