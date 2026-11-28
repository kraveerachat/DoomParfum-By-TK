---
id: IMP-WEB-02-DRAFT-PR-PACKAGE
project: DoomParfum By TK
type: publication_package
status: prepared-not-published
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, publication, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 — Draft Implementation PR package (not published)

PUBLIC_SAFE. Prepared locally (S3, revised in S4–S9). **Ready to publish as a Draft once the Owner authorizes it.** The S7 404 defect is fixed (S9). The final receipt waits for the Owner's answer on the physical Notes shortcut test (confirm or defer). Nothing is pushed and no PR exists. Publishing needs fresh, scoped Owner authorization and the agent publishing identity (`DEVELOPMENT_WORKFLOW.md` §5.6).

- Base: `main` at `3e87027fbdbbb016c148a84ca33775e64cccf3e0` (PR #37 merge; remote `main` re-verified 2026-11-28, S9)
- Head: `feat/frontend-v1-1-design-upgrade`, final code candidate `53d01265962059655764f8d65be5b71329e600c4` plus the S9 records commit (no code after `53d0126`)
- State on creation: **Draft**. No auto-merge. The Owner merges.

## Title

feat(frontend): IMP-WEB-02 Frontend V1.1 — bilingual luxury editorial upgrade (DPT-PLAN-013)

## Body

Implements merged DPT-PLAN-013 (PR #37) on the mock-only Next.js frontend.

**Scope:** `web/` only, plus this task's Obsidian records and evidence, and the post-merge status lines of DPT-PLAN-013 in `PRODUCT.md` and the vault. No database, matching, ETL, API, authentication or deployment change.

**What changed**
- Gold–bronze semantic tokens and R1–R5 rules; retired V1 gold removed from the favicon and drawings. English and Thai route trees (`/th`) over one shell, typed dictionaries and a server-only Thai overlay.
- Stable sticky header, static where it reflows to two rows, on short screens, without scripting below 1024px, and in print. Language control after Profile; compact language link on narrow layouts; BY TK at 11px.
- Owner CP4 selections: T1 Fahkwang 300 for Thai display (SIL OFL 1.1, self-hosted, 9,816 bytes); T2 centred hero; T3 record sheet; T4 compact Explore toolbar; T5 stable header; T6 compact language link; T7 equal Featured columns; T8 square corners.
- Thai wording approved by the Owner (192 entries: 159 kept, 33 replaced); fixture prose marked reviewed, so English pages also find it for a Thai query (DPT-PLAN-013 4.5). A unit test pins the approved wording. Family and accord labels stay English.
- Heading focus follows navigation modality: no ring after pointer, ring after keyboard, kept after a screenshot tool takes window focus.
- Server-rendered localized 404 documents (S9): every unknown address returns a real 404, with server `<html lang>`, a localized title, heading and notice, readable without JavaScript. This uses `app/global-not-found.tsx` and the proxy, which sets the locale from the path only and rewrites malformed addresses and unknown slugs to `/_unavailable` or `/th/_unavailable`. The catch-all and `/unavailable` routes are removed.

**Experimental dependency (Owner-authorized, S9):** `experimental.globalNotFound` in `web/next.config.ts`. It is authorized only for the pinned Next.js 16.4.6 and this local mock frontend. **A compatibility reassessment is required before any Next.js upgrade, live data or production deployment.** Next.js 16.4.6 runs the proxy a second time on an unmatched rewrite target; the per-locale targets depend on that behavior. No other experimental feature and no dependency change.

**Verification (local, final candidate `53d0126`)**
- Unit 122/0; Playwright Chrome 305/0/0 and Edge 305/0/0 on the production-style image `sha256:568cc3b3…`. The new 404 regression tests fail on the S6 candidate.
- Clean clone `npm ci` + build; uncached image build; output isolation scan clean; `npm audit` 0.
- Initial JS 171–175 KiB (budget 200); CLS ≤ 0.019; no external requests, cookies or storage.
- A11 Docker drills (S5): failed build keeps the preview serving; dev/preview and port conflicts refused safely; dev hot reload 0.8 s without reload at `http://localhost:3000`; dev syntax-error recovery without restart; stop/start/teardown clean. No runtime configuration changed since.

**Owner acceptance (2026-11-28):** the Owner accepted this visual design as the initial frontend baseline; further visual refinement is deferred until the app has real data and working features. The Owner's Notes screenshot shows no unwanted heading outline. That is an Owner observation: the physical shortcut test (click Notes, Win+Shift+S, Escape) was **not performed**.

**Not verified:** physical Notes shortcut test (not performed; Owner to confirm or defer); screen reader, physical phone, Safari, Firefox (A05 PARTIAL, deferred by the Owner for this stage); second-machine LAN probe. No WCAG conformance claim.

**Resolved (S9):** the S7 defect (every 404 was the framework's error document without `lang`, blank without JavaScript) is fixed and covered by regression tests.

**Review:** same-vendor fresh-context sub-agent reviews (not human or cross-vendor): S2 of `76dcb1c` (CONDITIONAL, fixed); S4 of `689b177` (CONDITIONAL, fixed) and deltas `bfb7210`, `c3f9688` (PASS); S6 of the translation delta `2f8b78a` (CONDITIONAL: stale browser tests, fixed) and `253bf48` (PASS); S9 of the 404 delta `3b93945` (CONDITIONAL: runtime unreachable, one diagnosis asked) and `53d0126` (PASS at runtime).

**Records:** `Structure DB Obsidian/07_Delivery/Tasks/IMP-WEB-02_Frontend_V1_1.md`; S1–S9 reports and summaries; review reports; evidence under `08_Operations/Test_Evidence/IMP-WEB-02/`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Before publishing

1. Owner authorizes publication of this branch (scoped, one-time).
2. Re-verify the head SHA, `git status`, and that `main` is still `3e87027` (otherwise rebase decision by the Owner).
3. Exclude the untracked `Test_Evidence/IMP-WEB-02/CP4.zip` and any local-only file.
4. Push the branch, open the PR as Draft with the body above, and record the PR number in the task note.
5. Before the receipt or merge: record the Owner's answer on the Notes physical test (confirmed or explicitly deferred), then write the single final receipt.
