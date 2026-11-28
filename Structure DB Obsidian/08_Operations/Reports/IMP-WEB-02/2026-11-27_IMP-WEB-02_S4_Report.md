---
id: IMP-WEB-02-S4-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-27
tags: [doomparfum, frontend, review, verification, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S4 — independent review, review fixes, acceptance reconciliation

PUBLIC_SAFE. Agent: Claude Code. Intake class A (continuation of [[IMP-WEB-02_Frontend_V1_1]], same branch, no PR). Owner instruction of 2026-11-27: "Final Independent Review and Acceptance Reconciliation". Verified at start: branch HEAD `d7a9e7f` (S3 records) on code `689b177`, worktree clean except the Owner's untracked `CP4.zip`, branch not on the remote, remote `main` = `3e87027`, preview image `a324a06d…`, the four protected containers stopped. Matches the instruction.

Final candidate **`c3f968853b64b4ee65df2d9cf8c6b94e0b13014b`**. Preview image **`sha256:48748b9cc0ffb413d270a2cd75a5fcefac0a9b92796bafa67250c6d12f2e33cf`**, built `--no-cache` from that commit.

## 1. Independent review

**Invocation.** The session was still in auto mode; the Owner's preferred route (manual approval outside auto mode) was not available to the agent. The first Agent call was again not judged by the auto-mode classifier because the context-mode plugin appends text to sub-agent prompts. The harness's own instruction for that case is to re-issue the call once with exactly the hook-modified input so the classifier reviews what will run; that was done and the call was approved. No hook, plugin, permission setting or security control was disabled, modified or bypassed. The same route served the two delta reviews.

**Reviewer type.** Three reviews, each a same-vendor (Anthropic Claude) general-purpose sub-agent with a fresh context, read-only (no edits, installs, Docker actions, test runs or external requests), commissioned by the implementer. Not human, not cross-vendor, not authenticated independent acceptance. Reports are filed verbatim:

| Review | Scope | Verdict | Report |
|---|---|---|---|
| R1 | `76dcb1c..689b177` in full; `3e87027..689b177` web/ diff spot-checked (83 files); live GETs on the preview | CONDITIONAL: N1, N2 spec deviations; N3–N7 nits | [[2026-11-27_IMP-WEB-02_S4_Independent_Review_689b177]] |
| R2 | `689b177..bfb7210` in full; live GETs on the candidate | PASS: F1 non-blocking; F2–F4 nits | [[2026-11-27_IMP-WEB-02_S4_Delta_Review_bfb7210]] |
| R3 | `bfb7210..c3f9688` in full; served CSS on the candidate | PASS: two optional nits | [[2026-11-27_IMP-WEB-02_S4_Delta_Review_c3f9688]] |

**Coverage of the final candidate.** S2's fresh-context review covered `3e87027..76dcb1c` (CONDITIONAL; its blockers fixed in `5d63f88`). R1 covered `76dcb1c..689b177` in full and re-read the whole `3e87027..689b177` web diff at spot-check depth, finding two deviations the S2 review had missed. R2 and R3 cover every later line. Every commit from the merged base to `c3f9688` has therefore been read by at least one fresh-context reviewer. Limits: all reviewers are same-vendor; none ran a browser or the suites (geometry and focus claims were judged from code and served CSS, then checked by this session's suites); the OFL texts were not compared with upstream; no human or cross-vendor review exists. Assessment: adequate as agent-side review evidence for the Owner's decision; not a substitute for Owner acceptance.

## 2. Findings and responses

R1's verdict asked for N1 and N2 to be fixed or accepted by the Owner. Both contradict written clauses of the merged contract (5.1 "Not sticky … when the header reflows to two rows" with V07 "documented non-sticky fallbacks work"; 3.1 "The V1 values `#AD9361` and `#75613A` retire"), so they were treated as acceptance-blocking and fixed in this branch rather than passed on.

| ID | Finding (verified first) | Response | Commit |
|---|---|---|---|
| R1-N1 | Two-row header could stay sticky. Measured on the 689b177 preview: without scripting the header is two rows (110px) and sticky at 390–1023px, and the `--header-h` fallback (78px) is shorter than the header both there and on desktop (94px). With scripting, a two-row header under 20% of the viewport stayed sticky | Script marks the header static whenever a header part starts below the brand; without scripting the header is static below 1024px or 64em and `--header-h` is 5.875rem (the one-row height) | `bfb7210`, `c3f9688` |
| R1-N2 | Retired `#AD9361` in favicon, home hero drawing, drawing generator | Changed to gold-500 `#A8875A`; generator re-run: only the one hero stroke changed; no retired value left in `web/` or the built app | `bfb7210` |
| R1-N3 | Folio rules on navy use `color-mix` of two tokens, not a token | Not changed: decorative, built from approved tokens. **Owner design decision** if strict token use is wanted | — |
| R1-N4 | Some focus tests could pass vacuously | V13 synthetic-blur test now presses a non-modifier key and asserts the heading still holds focus; it fails on the CP4 image (ring drawn) and passes on the candidate. The weaker `focus-paths.spec.ts` checks (tab switch, after Forward, language switch, mobile drawer) are left as they are and recorded as weak | `bfb7210`, `c3f9688` |
| R1-N5 | 200% record-sheet test only at 320px | New 390px test: six rows side by side at 100%, all stacked at 200%, no sideways scroll | `bfb7210` |
| R1-N6 | Overlay unit test matches source text | Recorded, not changed | — |
| R1-N7 | Footer alignment relies on label width over 44px | Accepted as a guard (the test fails if a shorter label appears) | — |
| R2-F1 | `width < 64em` misses 768–1023px when the browser default text is below 16px | Rule widened to `(width < 1024px) or (width < 64em)`. Fixed by reasoning; no test sets a smaller browser default | `c3f9688` |
| R2-F2 | Two-row test could read position before the observer ran | Waits for `data-header-static` | `c3f9688` |
| R2-F3 | Blur test could pass if focus moved | Asserts the heading is focused | `c3f9688` |
| R2-F4 | Static 768px clearance check trivially true | Clearance asserted only for the sticky 1280px case | `c3f9688` |
| R2 obs. | With scripting, a two-row header is sticky until hydration (pre-existing) | Recorded | — |
| R3-N1/N2 | No test with a browser default text below 16px; the blur test's `:focus-visible` premise is not proven inside the test | Open nits. The second is evidenced outside the test: the same test fails on the pre-fix CP4 image because the ring is drawn | — |

Sensitivity: the two-row and no-script-768 tests fail on the `689b177` image and pass on both candidates.

## 3. Verification of the final candidate (`c3f9688`, image `48748b9c…`)

| Check | Result |
|---|---|
| `tsc --noEmit`, `eslint . --max-warnings 0`, `validate:fixtures` | Exit 0; 12 studies, 9 notes, 3 families, 4 accords, 2 articles |
| `npm test` | 117 / 0 (worktree; clean clones of `bfb7210` and `c3f9688`) |
| Playwright 1.65.1 Chrome, full suite on the candidate image | 283 passed / 0 failed / 0 skipped / 0 flaky (279 + 4 new) |
| Playwright Edge, full suite on the candidate image | 283 / 0 / 0 / 0 |
| Clean clone, `npm ci` with an empty cache, `next build` | PASS at `bfb7210` and `c3f9688` |
| `docker build --no-cache --target runner` | PASS (`b776d5c1…` for `bfb7210`, `48748b9c…` for `c3f9688`) |
| `scan-output` on the image `/app` | 325 of 1448 files outside node_modules, 22 immutable scripts, no boundary violation |
| `npm audit` (all; `--omit=dev`) | 0 vulnerabilities each |
| Initial JS (Chrome suite, English routes) | 171.5–175.2 KiB (budget 200) |
| CLS | ≤ 0.0234 (budget 0.1) |
| Headers, CSP, no-store, noindex, methods, isolation, no-script, reduced motion, forced colours, widths 320–1920, 200% text | Covered by the passing suites |

Evidence: [S4 verification](../../Test_Evidence/IMP-WEB-02/S4/IMP-WEB-02_S4_Verification.json).

## 4. Acceptance reconciliation

- **DPT-PLAN-013 merge recorded.** PR #37 merge `3e87027fbdbbb016c148a84ca33775e64cccf3e0` (2026-11-26) verified from Git. Updated: `PRODUCT.md` (amendment heading and a post-merge sentence; resolves the S3 Impeccable `context` drift), the amendment note (status `merged`, post-merge line; contract text unchanged), the DPT-PLAN-013 task note (status `merged`, post-merge line), and the "PROPOSED until merged" headings in the tokens, routes, Docker runtime, fixture contract and acceptance-map notes. Earlier receipts and reports are unchanged. Backlog rows are dated history and stay as written.
- **A11 Docker development and recovery drills: REQUIRED, NOT RUN.** The merged acceptance map says "A02–A07, A10–A12: Rerun unchanged". Since IMP-WEB-01 the runner stage of the `Dockerfile` changed (Fahkwang licence copy); the dev stage, both Compose files and the lockfile did not. "Compose unchanged" is not a pass, so S2 and S3's "not run" stands as an open item. The drills stop and replace the preview, edit a source file for hot reload and break a build on purpose; IMP-WEB-01 ran them under the Owner's bounded chat approval to stop and replace the preview. This instruction asks for the preview to keep running, so the drills need that approval again (or an explicit Owner deferral for this stage).
- **A10:** preview smoke PASS on the final image; second-machine LAN probe NOT RUN.
- **A05: PARTIAL.** Screen reader, physical phone, Safari and Firefox NOT RUN. The Owner's physical Win+Shift+S check on Notes NOT RUN. No WCAG conformance claim.
- **Thai lines:** all 192 still `draft`. None marked reviewed.
- Translation-sheet generator nit: `web/scripts/translation-sheet.ts` still prints the CP4 glossary line; the CP5 sheet's glossary was rewritten by hand. Dev tooling only, not in the image. Recorded for a later code change.

## 5. Owner review package

Exported to `Downloads` at the Owner's request (both public-safe; copies with the same hashes in `Test_Evidence/IMP-WEB-02/S4/`):

| File | SHA-256 |
|---|---|
| `DoomParfum_IMP-WEB-02_Thai_Translation_Review_2026-11-27.md`: 160 interface and 32 fixture lines, each with an answer box; the Owner terminology; the open family/accord label question. Regenerated from the code and identical, line for line, to the CP5 sheet | `e1b55370459214d236cf40631d9ec2c716c7a92a36196551140d836b62906f16` |
| `DoomParfum_IMP-WEB-02_Final_Comparison_CP4_vs_c3f9688.png`: CP4 image (`177c02e5…`) beside the final candidate: Home EN 1440, detail with record sheet EN 1440, Explore TH 1440, Notes TH 1440, detail TH 390, Home TH 390 | `520a65aeac8b97350496f3f74d03b61095face7afb23063b7f9d079ddcf7e5fa` |

An earlier sheet from `689b177`, made in this session, was replaced by the one above.

## 6. Preview and protected resources

`http://127.0.0.1:3000/` recreated with `docker compose up --no-build --force-recreate --detach web`: image `48748b9c…`, healthy, loopback only, read-only root, user `node`, all capabilities dropped; `/`, `/th`, `/th/notes`, `/about` return 200. Rollback: tag `s3-candidate2` (`a324a06d…`, the S3 preview) as `preview`, then the same compose command. Intermediate image tag `s4-candidate` (`b776d5c1…`) kept. Temporary `--rm` containers on 127.0.0.1:3100 and 3200 (CP4 image for the comparison and the sensitivity run; candidates for the suites) are gone. The four protected containers stayed stopped. No volume, prune, PR #8, U01/r14, database, matching or ETL change.

## 7. Result

Agent side PASS on `c3f9688`; independent review PASS on the final delta (R1 CONDITIONAL resolved). **ACCEPTANCE PENDING**:

1. A11 Docker dev and recovery drills: bounded Owner approval to stop and replace the preview, or an explicit deferral.
2. A05: the Owner's stage-specific deferral of the manual checks.
3. The Owner's physical Notes check (click Notes, Win+Shift+S, Escape).
4. Thai line review (192 drafts) and the family/accord label question.
5. Optional design decision: R1-N3 `color-mix` on navy.
6. The Owner's review of the site and publication authority.

No receipt. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`. Publication package: [[IMP-WEB-02_Draft_PR_Package]].
