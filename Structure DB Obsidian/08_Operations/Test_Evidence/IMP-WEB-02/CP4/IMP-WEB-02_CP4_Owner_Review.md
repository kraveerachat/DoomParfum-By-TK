---
id: IMP-WEB-02-CP4-REVIEW
project: DoomParfum By TK
type: owner_review_packet
status: awaiting-owner
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, frontend, owner-review, typography, localization]
source_of_truth: "../../../../../DEVELOPMENT_WORKFLOW.md"
---

# Frontend V1.1 — one Owner review (CP4)

For the Owner. Task [[IMP-WEB-02_Frontend_V1_1]]; contract [[DPT-PLAN-013_Frontend_V1_1_Amendment]] section 8. The site at **http://127.0.0.1:3000/** already runs V1.1 with every default below; refresh it and use **TH · EN** in the header to switch language.

How these were made: T1 is a separate local specimen (not a site page). T2–T8 alternatives are **browser-injected prototypes** on the running V1.1 preview: a stylesheet or small page change applied only in the test browser. None of the alternatives exists in the application code, so whatever is not chosen leaves nothing behind. Defaults stay until you answer.

## T1 — Thai display font

No Thai display face is shipped. Thai headings use Noto Sans Thai 500 (the V1 control) until you choose. Candidates are pinned Fontsource 5.3.0 WOFF2 Thai subsets (npm `sha512` integrity verified), each under the SIL Open Font License 1.1, license texts from google/fonts at pinned commits. Each is paired with Bodoni Moda for Latin in one font stack.

| Candidate | Added bytes (Thai page only) | Darkness beside Bodoni 400, hero / card | Marks at page size 50/1.35 (ink ÷ line height) | Notes |
|---|---|---|---|---|
| Control: Noto Sans Thai 500 | 0 | 1.9× / 1.7× | 0.96 | Current. Sans beside a Didone |
| A: Chonburi 400 | 10,560 | 2.3× / 2.17× | 0.98 | Closest to the Didone idea, but much darker than Bodoni 400; single weight |
| B: Fahkwang 300 | 9,816 | 1.29× / 1.16× | 1.05 | Closest in darkness. Marks need a little more height at page size |
| B: Fahkwang 400 | 9,888 | 1.5× / 1.37× | 1.07 | As 300, slightly darker |
| C: Taviraj 300 | 15,892 | 1.38× / 1.35× | 1.03 | Looped (with heads), more traditional; secondary |
| C: Taviraj 400 | 16,040 | 1.63× / 1.61× | 1.03 | As 300, darker |
| D: Chonburi hero and page, Fahkwang 400 below | 20,448 | — | — | Two display families in one language |

Measured in Chrome 158 and Edge 158 on Windows with the same results; no mark is clipped (nothing hides overflow). A value above 1.0 means stacked marks need more height than one line, so wrapped lines could touch; Fahkwang or Taviraj at page size would get line height 1.45 instead of 1.35. Darkness is a pixel-coverage ratio, a guide only. Not run: physical phone. Measurements: [T1_measurements.json](T1/T1_measurements.json), faces: [T1_faces.json](T1/T1_faces.json).

![Hero](T1/T1_hero.png)
![Page title](T1/T1_page.png)
![Section title](T1/T1_section.png)
![Card title](T1/T1_card.png)
![Card title on a phone](T1/T1_card-mobile.png)
![Marks stress](T1/T1_stress.png)
![Mixed Latin and Thai](T1/T1_mixed.png)
![On navy](T1/T1_navy.png)
![Hybrid D](T1/T1_hybrid.png)
![Page title at 200% zoom](T1/T1_page_zoom200.png)

## T2 — Home hero

A: V1 (default). B: masthead. Its top line "Vol. I — Mock edition" is **new copy** that needs your approval, and it is a label above a heading, which the Impeccable craft floor advises against. C: headline centred on the art.

![T2 A](T2_hero_a_default.png)
![T2 B](T2_hero_b_masthead.png)
![T2 C](T2_hero_c_centred.png)

## T3 — Perfume detail

A: V1 7/5 (default). B: record sheet built only from fields already in the record (layers, general notes, accords). It repeats what the layer section shows lower down. C: balanced 6/6 with the picture capped at 80% of the viewport height.

![T3 A](T3_detail_a_default.png)
![T3 B](T3_detail_b_record_sheet.png)
![T3 C](T3_detail_c_balanced.png)

## T4 — Explore controls

A: boxed controls (default; visible labels and help kept, spacing already tightened). B: compact toolbar, one row of inline labels, full borders kept. The first catalogue picture now starts at 554px in English and 563px in Thai at 1440×900 (V1: 653; target 560).

![T4 A](T4_explore_a_boxed.png)
![T4 B](T4_explore_b_compact.png)

## T5 — Header while scrolling

A: stable height, signature always shown (default, Owner-directed). B: compact 64px with "BY TK" hidden.

![T5 A](T5_header_a_stable.png)
![T5 B](T5_header_b_compact.png)

## T6 — Language control on narrow screens (390px)

A: one compact link to the other language after Profile (default). B: both TH and EN in the header. C: drawer and footer only, no header control.

![T6 A](T6_narrow_a_compact.png)
![T6 B](T6_narrow_b_both.png)
![T6 C](T6_narrow_c_drawer_only.png)

## T7 — Featured

A: three equal columns (default). B: 6/3/3.

![T7 A](T7_featured_a_equal.png)
![T7 B](T7_featured_b_633.png)

## T8 — Corners

A: V1 2px buttons, 4px fields, 8px dialogs (default). B: square everywhere.

![T8 A](T8_corners_a_v1.png)
![T8 B](T8_corners_b_square.png)

## Translations

[[IMP-WEB-02_Translation_Review]]: 159 interface strings and 32 fixture texts, all draft.

## Answer form

Copy, fill in and send back. Anything left blank keeps its default.

```text
T1 Thai display font:        Control / A Chonburi / B Fahkwang 300 / B Fahkwang 400 / C Taviraj 300 / C Taviraj 400 / D hybrid
T2 Hero:                     A default / B masthead (approve "Vol. I — Mock edition"? yes/no) / C centred
T3 Detail:                   A default / B record sheet / C balanced
T4 Explore controls:         A boxed / B compact
T5 Header:                   A stable / B compact
T6 Narrow language control:  A compact link / B both labels / C drawer and footer only
T7 Featured:                 A equal / B 6/3/3
T8 Corners:                  A V1 / B square
V11-OD-03 Top/Heart/Base:    ชั้นบน/ชั้นกลาง/ชั้นฐาน  or  ท็อปโน้ต/ฮาร์ตโน้ต/เบสโน้ต  (and other glossary edits)
V11-OD-04 Family/accord labels: keep Latin / translate (give wording)
V11-OD-08 "BY TK" size:      10px / 11px
V11-OD-10 English Paper study L: none / provide wording
Translations:                accept all drafts / corrections attached
```
