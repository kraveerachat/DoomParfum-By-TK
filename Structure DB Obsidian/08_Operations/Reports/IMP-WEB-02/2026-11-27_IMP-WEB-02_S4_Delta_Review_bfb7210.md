---
id: IMP-WEB-02-S4-REVIEW-BFB7210
project: DoomParfum By TK
type: independent_review
status: final
owner: human-owner
updated: 2026-11-27
tags: [doomparfum, frontend, review, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S4 — independent delta review of `689b177..bfb7210` (verbatim)

PUBLIC_SAFE. Reviewer: same-vendor (Anthropic Claude) general-purpose sub-agent, fresh context, read-only, commissioned by the implementer in S4 on 2026-11-27 (invoked as in [[2026-11-27_IMP-WEB-02_S4_Independent_Review_689b177]]). Not human, not cross-vendor, no Owner acceptance. The implementer's response (F1–F4 fixed in `c3f9688`) is in [[2026-11-27_IMP-WEB-02_S4_Report]]. Report unedited below.

---

Verdict: **PASS**. I found no blocking issues. There is one non-blocking finding and three nits.

I am a same-vendor (Anthropic Claude) sub-agent with a fresh context. I worked read-only: no edits, installs, Docker actions or test runs.

**Scope reviewed**
- `git diff 689b177 bfb7210 -- web/`, all 7 files: `header-offset.tsx`, `globals.css`, `icon.svg`, `hero.svg`, `build-studies.mjs`, `locale.spec.ts`, `s3-alignment.spec.ts`.
- Context read: the header CSS in `web/src/app/globals.css` (lines 110–117, 728–760, 852–918) and the header markup in `web/src/components/site-header.tsx`.
- Authority: DPT-PLAN-013 §3.1 (line 74), §5.1 (lines 195–211), V07 and V13.
- Read-only GETs to 127.0.0.1:3100: `/about` (headers and HTML), the served CSS chunk `3fp73uro7ejf-.css`, `/icon.svg` and `/studies/hero.svg`.

**Answers to the checks**
1. **Two-row detection is correct in every layout.**
   - With scripting, the header has three layouts: narrow one-row ("menu brand utils"), the two-row fallback below 19rem ("brand brand" / "menu utils"), and desktop ("brand nav utils").
   - One-row headers cannot misfire. Items are centred (`align-items: center`). For a non-brand part to start at or below `brand.bottom - 1` in the same row, the two heights together would have to be 2px or less. Zero-height parts are filtered out: the hidden nav, and the menu button on desktop. The BY TK line sits inside the brand, so it only makes the brand taller.
   - The real two-row case is detected: below 19rem, menu and utils start below the brand.
   - The no-script layouts never reach this code.
   - No oscillation. Static versus sticky does not change the header's own size, and the attribute is removed and re-added in the same task. So the ResizeObserver does not re-fire, and `--header-h` only affects other elements.
2. **Cascade is correct, with no regression on the script path.**
   - The served CSS has `@media (scripting:none){html{--header-h:5.875rem}}` and `@media (scripting:none) and (not (min-width:64em)){.site-header{position:static}}`.
   - Both come after `@layer base` (which holds `--header-h:4.875rem`) and after the sticky `.site-header` rule, so they win.
   - The with-script path is untouched because `scripting:none` is false there.
   - 5.875rem (94px) matches the one-row desktop height: 5.5rem minimum plus 6px bottom padding.
3. **N2 is fixed.** `git grep -niE "AD9361|75613A" bfb7210 -- web/` finds nothing. The `hero.svg` word-diff is a single change (`stroke="#AD9361"` to `#A8875A`). The served `icon.svg` and `hero.svg` both use `#A8875A`.
4. **Tests are non-vacuous**, apart from nits F2–F4.
   - The two-row test fixes the height at 200px or less, so only the two-row rule can make the header static.
   - The 320 sticky test now asserts one row.
   - The 390 test checks six rows unstacked first, then stacked.
5. **Nothing else affected.** The delta does not touch T1–T8, localisation, focus code or CSP. The served CSP and COOP headers are unchanged in form.

**Findings**
- **F1 (non-blocking), `web/src/app/globals.css:752`.** The no-script static rule uses `width < 64em`. The one-row layout it should match needs `min-width: 1024px` plus a header container of at least 62.5rem.
  - These agree only when the browser's default font size is 16px, because media-query `em` follows the user's default size.
  - With a smaller default, such as Chrome "Small" at 12px, `64em` is 768px. At 768–1023px without scripting, the header is then two rows ("brand utils" / "nav nav") but stays sticky. That breaks §5.1 "not sticky when the header reflows to two rows".
  - In that case `--header-h` (5.875rem, 70.5px) can also be shorter than the real two-row header.
  - A larger default font only makes some one-row headers static, which is harmless.
  - Suggested fix: `@media (scripting: none) and ((width < 1024px) or (width < 64em))`.
- **F2 (nit, possible flake), `web/e2e/locale.spec.ts` ~229–241.** `expect.poll(headerRows)` can return 2 as soon as layout runs after the font change, before the ResizeObserver has fired. The `position === "static"` read straight afterwards could then still see `sticky`. Polling on position (or on the `data-header-static` attribute) would avoid this.
- **F3 (nit), `web/e2e/locale.spec.ts` ~453–457.** `ring()` returns false whenever the h1 is no longer the active element. If the key presses moved focus, the test would pass vacuously. Add `await expect(page.locator("main h1")).toBeFocused()` before the final check. The comment that a non-modifier key makes Chromium re-evaluate `:focus-visible` is not verified here.
- **F4 (nit), the no-script 768px test.** Once the static header scrolls off, its bottom is clamped to 0, so the "target clears header" assertion is trivially true. It effectively only proves the header is static. The 1280px case is meaningful (target top about 118px against a header of about 94px).
- **Observation, not introduced by this delta.** With scripting enabled, a two-row header below 19rem is sticky until hydration runs `HeaderOffset`, or indefinitely if the script bundle fails. In that window the 4.875rem fallback applies.

**Could not verify**
- I ran no Playwright tests, browser renders or layout measurements, so all geometry above comes from reading the CSS.
- I did not check the implementer's claim that the new tests fail on the 689b177 image and pass on bfb7210.
- Not checked: Chromium's actual `:focus-visible` behaviour after pressing "a", heights with a non-default font size, wrapping of the Thai desktop nav without scripting, and real Windows classic-scrollbar widths at 320px.
- Image identity: I did not confirm that :3100 is serving image `b776d5c1`.
