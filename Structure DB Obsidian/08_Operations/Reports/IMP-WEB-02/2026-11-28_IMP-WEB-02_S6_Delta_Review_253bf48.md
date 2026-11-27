---
id: IMP-WEB-02-S6-REVIEW-253BF48
project: DoomParfum By TK
type: independent_review
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, localization, review, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S6 — independent follow-up review of `2f8b78a..253bf48` (verbatim)

PUBLIC_SAFE. Reviewer: the same read-only sub-agent as [[2026-11-28_IMP-WEB-02_S6_Delta_Review_2f8b78a]], resumed with a follow-up request. It is a same-vendor (Anthropic Claude) sub-agent with its own context, separate from the implementer's. Not human, not cross-vendor, not Owner acceptance. The report follows unedited.

---

I'm a same-vendor (Anthropic Claude) sub-agent with a fresh context, doing a read-only follow-up review.

**Verdict for 253bf48: PASS.** Findings 1–3 are resolved. I could not run Playwright, so the two updated e2e specs are checked against the search logic, not in a browser.

**Scope**
- Commits 4633f21 and 253bf48 on top of 2f8b78a.
- `git diff --stat 2f8b78a 253bf48` changes only `web/e2e/content.spec.ts` (+3/−1), `web/e2e/locale.spec.ts` (+11/−2) and `web/tests/locale.test.ts` (+35).
- `web/src` and `web/scripts` are unchanged from 2f8b78a, so the string, overlay and chunk results from my previous review still apply.
- The worktree's `web/` matches 253bf48. The only untracked items are `CP4.zip` and the S6 evidence folder (`Structure DB Obsidian/08_Operations/Test_Evidence/IMP-WEB-02/S6/`), which are outside this scope.

**Finding 1 (blocking): resolved, except for the browser run.**
- The new e2e expectations match the app's search logic at 253bf48, run on a scratch copy. Results on English `/explore`, in the order the app returns them:

| Query | Result |
|---|---|
| "กระดาษ" | `paper-study-b, paper-study-c, paper-study-l` (the expected order) |
| "หมึก" | `paper-study-c` |
| "late ink" | `paper-study-c` |
| "ไม่มีคำนี้เลย" | no results |

- No other committed e2e test sends a Thai query on an English page.
- I did not verify the implementer's report that both specs fail on c3f9688 and pass in Chrome and Edge.

**Finding 2: resolved.**
- `web/tests/locale.test.ts:115-119` returns `mock-perfume-003` to draft and asserts it no longer joins English search.
- In a scratch copy I removed the review check in `view-model.ts`, so draft text would always count. The 4.5 test then fails, so the draft path is now really covered.

**Finding 3: resolved.**
- `web/tests/locale.test.ts:157-184` checks a digest of the Thai text, requires exactly 160 + 32 strings, and requires the Owner record on every prose text.
- I recomputed the digest with my own code. It equals `5638f83b3069aa750d020f3c1ea9c46f505893cd8d16105c6a5786bd7757f61c` at 253bf48. My earlier review showed these strings equal the approved text exactly. The c3f9688 strings give a different digest, `7ec3…4480`.
- Scratch-copy edits, one at a time:

| Edit | Result |
|---|---|
| One character added to the prose text for `mock-note-005` | test fails |
| Trailing space added to the `visual.caption` interface string | test fails |
| One prose text set back to draft, wording unchanged | test fails |
| All edits restored | 21/21 pass |

- In the worktree, `node --test tests/*.test.ts` gives 119 tests, 119 pass, 0 fail.

**Rendered checks on :3100**
All 12 routes return 200:
- The 32 prose texts are on the Thai pages, and no retired prose appears anywhere.
- On English pages, Thai prose appears only inside script payloads, as before.
- None of the prose is in the 19 immutable `/_next/static` chunks. One mid-fragment hit was the known false positive "ละระดับ", which comes from an interface string; a full-string search found nothing.
- The review record is in no chunk.
- Because only tests changed since 2f8b78a, this content cannot tell a 2f8b78a build from a 253bf48 build. I did not verify image sha256:dedbba40… or the `--no-cache` build.

**Non-blocking findings**
- The new pin test contradicts its own instructions. The comment at `web/tests/locale.test.ts:157-160` says that after an edit you should update the digest and, for prose, "return the text to draft until it is approved". But the record check at line 183 fails for any draft prose text, so that workflow cannot keep the suite green. Either reword the comment (the suite stays red until the Owner re-approves) or allow draft texts in that check.
- My earlier findings 4–6 are unchanged and recorded only, as you said:
  - `translation-sheet.ts` still prints "draft".
  - English HTML carries the reviewed Thai prose in its payloads.
  - The U116 and F22 wording nuances.

**What I could not verify**
- Playwright e2e in Chrome and Edge, axe, and visual layout.
- The image identity.
- The Owner approval event itself.
- The S6 evidence files, which are untracked.

My scratch files are in the reviewer scratch folder outside the repository. The digest check is `digest.mjs`; the edit runs were done in the `n3` folder there, which I restored afterwards. I modified no repository file.
