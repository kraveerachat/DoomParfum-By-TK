---
id: IMP-WEB-02-S6-REVIEW-2F8B78A
project: DoomParfum By TK
type: independent_review
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, localization, review, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S6 — independent delta review of `c3f9688..2f8b78a` (verbatim)

PUBLIC_SAFE. Reviewer: same-vendor (Anthropic Claude) general-purpose sub-agent, fresh context, read-only, commissioned by the implementer in S6 on 2026-11-28. It was invoked the same way as in S4: the first Agent call was not judged by the auto-mode classifier because the context-mode hook appends text, and it was re-issued once with exactly the hook-modified input. No hook, plugin or permission changed. Not human, not cross-vendor, not Owner acceptance. Its blocking finding refers to commit `2f8b78a`; the responses (`4633f21`, `253bf48`) and the follow-up review are in [[2026-11-28_IMP-WEB-02_S6_Report]]. The report follows unedited.

---

I'm a same-vendor (Anthropic Claude) sub-agent with a fresh context, reviewing read-only.

**Verdict: CONDITIONAL.** The translation content is correct. But the e2e tests committed at 2f8b78a still expect the old search results, so 2f8b78a should not be accepted as the candidate as it stands.

**Scope**
- `git diff --stat c3f9688 2f8b78a`: 31 files. Code changed in only three files, all in commit 2f8b78a:
  - `web/src/fixtures/th.ts`
  - `web/src/i18n/messages.ts`
  - `web/tests/locale.test.ts`
- The other 28 files are docs and evidence from commits 9f78099 and 9088837. I read only their stat, plus the DPT-PLAN-013 header change, which is status only.
- I extracted both commits with `git archive` into my scratch folder and ran comparison scripts there.

**Verified**
1. **Strings.** All 192 rows match, in `translation-sheet.ts` order (160 interface, 32 fixture prose).
   - The 159 KEEP entries are byte-identical to c3f9688.
   - The 33 changed IDs are exactly the approved list, and each equals the approved string exactly.
   - The review file's "Current Thai" column matches c3f9688 on all 192 rows. Its KEEP/REPLACE split is 159/33.
   - U46 still contains U+2060.
   - U74, U75, U103 and U124 keep their leading spaces.
   - U123 changed from `"ดู{count}"` to `"ดู {count}"`. On `/th/notes` it renders as "ดู แบบศึกษาจำลอง 5 รายการ" with sr-only " ที่มี Ivrel", so the visible text and the accessible name both compose correctly.
2. **Nothing else changed.**
   - The English dictionary and `fixtures` are deep-equal to c3f9688.
   - The Thai dictionary's deep key paths are unchanged.
   - The overlay structure is unchanged apart from `th`, `review` and `reviewRecord`.
   - In `messages.ts`, 58 lines changed: 26 strings plus the 3-line header comment.
3. **Moving the 32 prose texts to reviewed is a faithful implementation, not an unauthorized behavior change.**
   - DPT-PLAN-013 4.3 (line 161) lets only the Owner mark text reviewed. 4.5 (line 189) says reviewed text joins English-page search only for a query containing a Thai character.
   - The resulting behavior is the one the contract designed. Latin queries still give the same results on English pages (`''`, `paper`, `ink`, `late ink`, `a`, `unknown`).
   - Thai queries now return more on English pages. For example, "หมึก" returns paper-study-c and mock-note-007, and "กระดาษ" returns B, C and L.
   - I put every text back to draft in a probe: results were then identical to V1 on all 13 queries, so the gate still works.
   - The review record does not reach the client: it is in no chunk and no HTML.
   - The changed review-record test is justified: the old test fails on the new data only because a record now exists. With the record removed, the validator is still exercised correctly.
4. **Meaning and data truth.**
   - F15 ("น้ำหนักเชิงการบรรยาย…เป็นหลัก") stays figurative, with no quantity.
   - F22 makes no real-product, ingredient or wear claim. "makes no claim about wear" is rendered more faithfully than before.
   - The difference between "not supplied" (ไม่ได้ระบุ) and "authored empty" (ไม่มีรายการ) is kept in U56, U57, U84, F13, F28 and F30.
   - Mock disclosures are kept: all 7 Thai content pages have `lang="th"` and the new footer disclosure.
   - Font and license names in U160 are unchanged.
5. **Rendered pages on :3100.**
   - All 26 changed interface strings and all 32 prose texts are in the served build. The 6 interface strings not in the fetched HTML (U84, U87, U123, U124, U129, U134) are in the client bundles. No retired prose string appears anywhere.
   - On English pages, Thai prose appears only inside `<script>` payloads, never outside them.
   - None of the 32 prose texts is in the 19 immutable `/_next/static` chunks (`max-age=31536000, immutable`). I checked raw text and `\u` escapes; one mid-fragment hit was a false positive from an interface string. All 160 interface strings are in the chunks, as expected for the client dictionary.
6. **Unit tests.** `node --test tests/*.test.ts` in the worktree: 118 passed, 0 failed. Note that the worktree has uncommitted edits, described in finding 1.

**Findings**
1. **Blocking (for this SHA): the e2e expectations are stale and contradict the new behavior.**
   - `web/e2e/content.spec.ts:137-138` expects "กระดาษ" on English `/explore` to return only `["paper-study-l"]`. It now returns paper-study-b, paper-study-c and paper-study-l.
   - `web/e2e/locale.spec.ts:166-169` ("English pages are not widened by draft Thai text") expects 0 results for "หมึก". It now returns paper-study-c.
   - I derived this with the same `filterEntries` the app uses; I did not run Playwright.
   - The worktree (HEAD 2f8b78a) has **uncommitted** fixes for both specs, plus a draft-again unit assertion in `tests/locale.test.ts`. They are not part of the candidate. They need to be committed, the e2e suite run, and that commit's diff reviewed.
2. **Non-blocking: the committed tests no longer cover the draft path.**
   - At 2f8b78a, `web/tests/locale.test.ts` lines 94-117 no longer check that draft text stays out of English results. The old Thai queries in the V06 test (`ไม่`, `แบบ`, `หมึก`) used to cover this implicitly.
   - Also, the `every … /[฀-๿]/` assertion at line 105 is close to vacuous, and the expected sets mirror the implementation's `includes` logic. Only the "หมึกยามดึก"/mock-perfume-003 checks pin real behavior.
3. **Non-blocking: the header comments are accurate but nothing enforces them.**
   - `web/src/i18n/messages.ts:3-5` and `web/src/fixtures/th.ts:3-6` say a changed text needs the Owner's review again or goes back to draft.
   - Nothing in the code does this. Someone could edit a reviewed string and it would stay reviewed, which now also affects search. A test pinning a digest of the approved strings to the `OWNER_REVIEW` record would close the gap.
4. **Nit: the review-sheet script is now out of date.**
   - `web/scripts/translation-sheet.ts` (not changed in this delta) still prints `draft` for every interface row, and its header says "Every Thai text is a draft".
5. **Nit: English HTML is heavier.**
   - English pages now carry 10–19 reviewed Thai prose strings inside script payloads. This follows from 4.5 and is not visible.
6. **Nit: wording, both Owner-approved, no data-truth breach.**
   - U116 adds "จริง" ("real"), which narrows "any ingredient or material".
   - In F22, "ไม่ค่อยเหมาะกับการใช้งานทั่วไปนัก" is ambiguous: it can be read as describing the boulder rather than its description.

**Not verified**
- Playwright e2e runs, axe, visual layout and wrapping of the longer Thai strings.
- That the :3100 image (sha256:69806fd3…) was built from 2f8b78a. I inferred it from the served content, not from image metadata.
- The Owner's approval itself. I have only the instruction text; the source file still says "ADVISORY / OWNER APPROVAL PENDING".
- The content of the docs commits 9f78099 and 9088837.

The 404 pages at `/th/does-not-exist` and `/does-not-exist` are served as `<html id="__next_error__">` without a `lang` attribute. Nothing in this delta changes that; I did not assess it.

My scripts and outputs are in the reviewer scratch folder outside the repository. I modified no repository file.
