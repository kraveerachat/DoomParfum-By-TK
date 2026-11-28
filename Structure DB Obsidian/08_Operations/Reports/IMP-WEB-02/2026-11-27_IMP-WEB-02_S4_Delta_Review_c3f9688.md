---
id: IMP-WEB-02-S4-REVIEW-C3F9688
project: DoomParfum By TK
type: independent_review
status: final
owner: human-owner
updated: 2026-11-27
tags: [doomparfum, frontend, review, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S4 — independent delta review of `bfb7210..c3f9688` (verbatim)

PUBLIC_SAFE. Reviewer: same-vendor (Anthropic Claude) general-purpose sub-agent, fresh context, read-only, commissioned by the implementer in S4 on 2026-11-27 (invoked as in [[2026-11-27_IMP-WEB-02_S4_Independent_Review_689b177]]). Not human, not cross-vendor, no Owner acceptance. Its two optional nits stay open; see [[2026-11-27_IMP-WEB-02_S4_Report]]. Report unedited below.

---

Reviewer identity: I am a same-vendor (Anthropic Claude) sub-agent with a fresh context. I made no changes: I only read files, ran read-only git and made HTTP GETs to :3100.

**VERDICT: PASS.** F1–F4 are fixed. No blocking findings and no regressions found. Only nits remain.

**Scope**
- Worktree HEAD is c3f968853b64b4ee65df2d9cf8c6b94e0b13014b. Its parent is bfb7210.
- `git diff --stat bfb7210 c3f9688` shows 2 files changed, 11 lines added and 5 removed:
  - `web/src/app/globals.css`: comment plus one media query.
  - `web/e2e/locale.spec.ts`: three test edits.
- Nothing outside `web/` changed in the commit. `git diff --check` is clean.
- Separately, the worktree has uncommitted Obsidian/PRODUCT.md changes, including the DPT-PLAN-013 note itself. They are not in c3f9688 and I did not review them. I checked 5.1 (line 200: "not sticky … when the header reflows to two rows"), V07 and V13 against the committed (HEAD) version.

**(1) Media query: valid and served correctly**
- The source at `globals.css:753` is `@media (scripting: none) and ((width < 1024px) or (width < 64em))`. This is valid Media Queries Level 4: an `or` condition wrapped in brackets is allowed after `and`.
- The served CSS is `/_next/static/chunks/1cokl1ka3w2qx.css`, found from the `/about` HTML on :3100. The build rewrote the rule as `@media (scripting:none) and ((not (min-width:1024px)) or (not (min-width:64em))){.site-header{position:static}}`. It means the same thing.
- Browsers that support `(scripting)` also support range syntax and nested `not`/`or`, so the rule cannot be silently dropped where it matters.
- The served rule matches c3f9688, not bfb7210. That shows :3100 runs the candidate CSS. I could not check the image digest itself.

**Does the rule match when the header actually has two rows?** The header goes to one row only when both of these hold (`globals.css:904`): `@media (min-width:1024px)` and `@container header (min-width:62.5rem)`. The container is `.site-header-inner`, which has no padding, so its width is the viewport minus the scrollbar.
- Default text below 16px: the 1024px media gate decides. The new `width < 1024px` branch covers this case (fixes F1).
- Default text at 16px or above: the 62.5rem container width decides. The `64em` branch covers it, assuming a scrollbar of at most 1.5rem.

**(2) No regressions**
- With scripting: the rule only applies under `scripting: none`. The ResizeObserver path in `header-offset.tsx` is unchanged.
- Without scripting, default text 16px or above: 64em is at least 1024px, so the new rule matches exactly where the old one did. The 1280px no-script case is still sticky with one row.
- Without scripting, default text below 16px: the header is now static only between 64em and 1023px. There the nav really does take two rows because of the 1024px media gate, so this is the intended correction, not a regression.

**(3) Test edits: real behaviour, not vacuous (judged from code; I did not run Playwright)**
- **F2** (`locale.spec.ts:231-232`): the test now waits for `data-header-static=""` before reading position and offset. The attribute is not present beforehand: the 320px one-row case is not too tall (≤20%) and not two rows (see the test at :219). So the wait only passes after the observer runs on the 125% two-row layout. The `offset === "0px"` check is also real.
- **F3** (`locale.spec.ts:459-462`): `ring()` already returned false whenever focus had left the h1. The new `toBeFocused()` closes that gap. A false `ring()` now means the outline really is none.
  - This lines up with the fix in `route-memory.tsx:26-31`, which keeps `data-pointer-focus` while the heading is still the active element.
  - On the pre-fix code, the synthetic blur would remove the attribute. The `a` key press would then let `h1:focus-visible` (`globals.css:167`) draw the ring. So the implementer's report (fails on CP4, passes on candidate) is plausible from the code.
- **F4** (`locale.spec.ts:246-262`): the static 768px case now asserts only two rows and static position, then returns `context.close()` (a promise, which the runner awaits). The clearance check now runs only for the sticky 1280px case, where it means something.

**Findings**
- **N1 (nit), `globals.css:753`:** no test covers the F1 case itself (no script, default text below 16px, 768–1023px). The 768px no-script test uses the 16px default, so it passed under the old rule too. The fix is verified by reasoning, not by a test. Optional: a Chromium context with a smaller default font-size preference, at 1000px.
- **N2 (nit), `locale.spec.ts:459-462`:** the F3 test assumes that pressing `a` makes Chromium match `:focus-visible` on a heading focused by script. Nothing in the test proves that assumption. Optional: after the check, remove `data-pointer-focus`, press `a` again and assert `ring() === true`.

**Not verified**
- I did not run Playwright, so I cannot confirm pass/fail on the candidate or on the CP4 image.
- I did not check the computed position in a real no-script browser below 16px default text.
- I did not check the :3100 image digest (sha256:48748b9c…). Only the matching served CSS supports that it is the candidate build.
- Scrollbar width over 24px on real Windows browsers, near 1024px at 16px default text, is untested. This edge case predates this commit.
