---
id: IMP-WEB-02-S4-REVIEW-689B177
project: DoomParfum By TK
type: independent_review
status: final
owner: human-owner
updated: 2026-11-27
tags: [doomparfum, frontend, review, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S4 — independent review of `689b177` (verbatim)

PUBLIC_SAFE. Reviewer: same-vendor (Anthropic Claude) general-purpose sub-agent, fresh context, read-only, commissioned by the implementer in S4 on 2026-11-27. Not human, not cross-vendor, no Owner acceptance. Invocation: the first Agent call was not judged by the auto-mode classifier because the context-mode hook appends text to it; the call was re-issued once with exactly the hook-modified input, as the harness instructs, and ran. No hook, permission or security control was changed. The reviewer's report follows unedited; the implementer's response is in [[2026-11-27_IMP-WEB-02_S4_Report]].

---

**Verdict: CONDITIONAL.** I found no blocking defect in the 76dcb1c..689b177 delta. Two spec deviations (N1, N2) need a fix or explicit Owner acceptance before closeout. The rest are test-quality nits.

Reviewer: a same-vendor Anthropic Claude sub-agent with a fresh context, working read-only. I made no edits, installs, Docker actions or external network requests.

**Scope reviewed**
- In full: `git diff 76dcb1c 689b177 -- web/`, which is commits 5d63f88, ee34142 and 689b177. Files: `web/NOTICE.md`, `web/e2e/focus-paths.spec.ts`, `web/e2e/locale.spec.ts`, `web/e2e/s3-alignment.spec.ts`, `web/src/app/globals.css`, `web/src/server/catalogue.ts`, `web/src/views/detail.tsx`, `web/tests/locale.test.ts`.
- Spot-checked: the wider 3e87027..689b177 web/ diff (83 files):
  - `route-memory.tsx`, `header-offset.tsx`, `site-header.tsx`, `site-footer.tsx`, `language-links.tsx`, `skip-link.tsx`
  - `home.tsx`, `detail.tsx`, `fixtures/th.ts`, `view-model.ts`, `proxy.ts`
  - `Dockerfile`, the fonts directory, and the V13 block of `locale.spec.ts`
- Confirmed HEAD d7a9e7f changes no web/ files. Nothing outside `web/` and the vault changed in the range. `package.json`, the lockfile and compose are unchanged.
- Live GETs against 127.0.0.1:3000: `/`, `/th`, `/th/notes`, `/perfume/paper-study-a`, `/th/perfume/paper-study-c`, `/notes`, `/about`, `/th/explore`, and the CSS chunk.

**Findings**

- **N1, non-blocking (spec deviation from DPT-PLAN-013 5.1): a two-row header can stay sticky.** 5.1 says the header is "Not sticky … when the header reflows to two rows".
  - `globals.css:737` is now `@media (max-height: 31.25rem), print`. 5d63f88 removed `(max-width: 20.99rem)`. The only remaining guard is the 20%-of-viewport-height check in `header-offset.tsx:15-21`.
  - The header goes to two rows when its container is under 19rem (`globals.css:864`). With script on, that happens with a classic scrollbar at a 320px window (inner width about 303px), at 200% text below 608px, or at zoom. Such a header (about 120px or more) stays sticky whenever it covers 20% of the height or less, e.g. a 320×900 window.
  - With `scripting: none` the header is always two rows below 1024px (`globals.css:876-890`), and nothing makes it static. The `--header-h` fallback of 4.875rem (78px, `globals.css:117`) is then shorter than the real header, so scroll-margin under-clears anchors and focused controls by about 20–40px (an estimate; not measured). That case existed before 5d63f88 and the earlier review missed it; at 320px it is new with this delta.
  - The test at `locale.spec.ts:209`, "a one-row header stays sticky at 320px", only checks `position === "sticky"`. It never checks that the header is one row.
  - Fix: make the header static when the grid has two rows (compare `[data-header-brand]` and `[data-header-utils]` top), add a no-script static rule below 1024px, and assert the single row in that test.
- **N2, non-blocking (amendment 3.1: "#AD9361 … retire"): the retired V1 gold is still in use.**
  - `web/src/app/icon.svg:1`: the favicon stroke is `#AD9361`.
  - `web/public/studies/hero.svg:12`: rendered on the home hero.
  - `web/scripts/build-studies.mjs:11`: `gold: "#AD9361"`, so regenerated studies keep it.
  - None of these are in the diff; the earlier review missed them. Change to `#A8875A`, or have the Owner accept this artwork as V1-frozen.
- **N3, nit: one colour that is not a token.** `globals.css:558-562` uses `color-mix(in srgb, var(--color-gold-on-navy) 40%, var(--color-navy))` for the folio rules on navy. It is decorative only, but Owner/design sign-off is needed if strict token use applies.
- **N4, nit (test quality): several focus tests could pass without the fix.**
  - `focus-paths.spec.ts:29`: its own comment says it does not reproduce the screenshot case.
  - `focus-paths.spec.ts:65`, after Forward, and `:106`: neither checks that anything was focused, so `activeRing === false` passes when focus is simply on `<body>`.
  - `focus-paths.spec.ts:81-95`: a language switch is a full document load with no auto-focus by design, so `false` is trivially true.
  - `locale.spec.ts:395-408`, V13 synthetic blur: it presses only `PrintScreen` and `Shift`. If Chromium does not switch `:focus-visible` on those keys, the test passes even without the 689b177 blur fix. Add a non-modifier key such as `"a"`, as `focus-paths.spec.ts:17` does.
  - Still meaningful: the keyboard ring tests (`:41`, `:57`, `:97`, `:126` Escape), the pointer letter-link test at `locale.spec.ts:410`, and `focus-paths:17` with "a".
- **N5, nit: the 200% record-sheet test misses its stated case.** `s3-alignment.spec.ts:24` runs at 320px, where the sheet (about 288px) stacks at 100% text anyway. It does not show that enlarged text alone causes stacking (e.g. 390–767px at 200%), and it checks only row index 3. The per-width tests at `:5-21` (six dd values in one column, room over 120px, side-by-side exactly when wider than 320px) are not vacuous.
- **N6, nit: the overlay unit test checks source text, not behaviour.** `tests/locale.test.ts:96` regex-matches the source of `catalogue.ts`. A refactor that keeps the behaviour fails it, and a wrong call with the same text passes it.
- **N7, nit: the footer alignment depends on label width.** It now relies on each full language name being wider than the 44px centred box. "ภาษาไทย" and "English" are, so the test at `s3-alignment.spec.ts:38` fails if a shorter label appears, which is acceptable as a guard.

**Item results**

1. **T1–T8:** all implemented as selected.
   - T1: Fahkwang 300, Thai-only unicode-range, used in the Thai display roles at weight 300 with no tracking.
   - T2: text vertically centred on the art from 768px; no masthead copy and no "Vol. I".
   - T3: record sheet with six rows from the existing fields.
   - T4: compact toolbar.
   - T5: stable header, BY TK always shown at 0.6875rem (11px) in bronze-700.
   - T6: compact link.
   - T7: equal three columns.
   - T8: every radius token is 0px.
   - No unselected variant found.
2. **Record sheet:** the grid and container query are correct. It is single-column below a 21rem sheet width (which follows rem, so 200% text stacks too), with `min-width: 0`, `overflow-wrap`, and baseline alignment. Values use names only (fictional names kept in Latin under `lang="en"` on Thai pages); "not supplied" and "no entries" are kept distinct. The rules are present in the live CSS.
3. **Footer language row:** the negative margin was removed; it aligns as long as the labels stay wider than 44px (N7).
4. **Notes heading focus:** correct. The pointer/keyboard source comes from `click.detail` in a document capture listener that runs before Next Link's preventDefault. The ring is suppressed only through `[data-pointer-focus]:focus-visible` (specificity 0,2,0 beats `h1:focus-visible`) on programmatic targets. There is no global outline removal: `h1:focus`/`h2:focus` remove the outline only when not focus-visible. The blur handler keeps the state on a window blur and clears it on a real focus move. Duplicate listeners are harmless. Risk: a fragment target that is an interactive control would lose its ring after a pointer start; none exists today, since fragments point to headings and sections.
5. **Header and anchors:** the scroll-margin on `main`, `footer` and their descendants is correct. The skip link test (`locale.spec.ts:187`) is non-vacuous. The gap is N1.
6. **Localization and fixtures:** every Owner term appears; no alternative spellings (โน้ตหัว/กลาง/ฐาน, กลุ่มกลิ่น, อัคคอร์ด, ไม่ระบุ, โน๊ต) were found in `web/src`. The rendered Thai sheet uses ตระกูลกลิ่น / ท็อปโน้ต / ฮาร์ตโน้ต / เบสโน้ต / โน้ตทั่วไป / แอคคอร์ด / ไม่ได้ระบุ. The overlay is draft translation only. No ratings, prices, scores or similarity values were added. Thai language names are not letter-spaced.
7. **Tests:** see N1 and N4–N6.
8. **Fonts:** the Fahkwang woff2 SHA-256 `86cb1a49…5fccda` matches NOTICE. The OFL text is present (4390 bytes, LF, copyright line correct) and is copied to `licenses/` by the Dockerfile. Every `@font-face` URL is local, and the live CSS has only `../media/*.woff2`. I could not verify that the text is byte-exact against upstream google/fonts (no external fetch). Note that `eol=lf` normalisation would change it if upstream uses CRLF.
9. **Runtime and security:** `/`, `/th`, `/th/notes` and `/perfume/paper-study-a` all return a nonce CSP (`default-src 'self'`, `font-src 'self'`, `connect-src 'self'`, `form-action 'none'`, `frame-ancestors 'none'`), `cache-control: private, no-store, max-age=0` and `x-robots-tag: noindex, nofollow`. The pages also carry a robots meta tag. No external `src`/`href` in the eight pages fetched. No fetch, storage or cookie APIs and no secrets in the added code. The only Dockerfile change adds the Fahkwang licence to the COPY. `proxy.ts` now sends undecodable Thai paths to `/th/unavailable`, which is safe.

**Could not verify**
- No browser or test-suite execution, so the Chrome/Edge results, the real Win+Shift+S path, screen reader and focus-not-obscured behaviour are unverified.
- Upstream byte-exactness of the OFL text.
- That the running preview is image `a324a06d…`. Its CSS matches the 689b177 rules, but the image digest was not checked.
- Any physical-device rendering.
