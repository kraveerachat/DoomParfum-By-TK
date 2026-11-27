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

PUBLIC_SAFE. Prepared locally (S3, revised in S4, S5, S6 and S7). **Not ready to publish:** the S7 404 decision is open. Nothing is pushed and no PR exists. Publishing needs fresh, scoped Owner authorization and the agent publishing identity (`DEVELOPMENT_WORKFLOW.md` §5.6).

- Base: `main` at `3e87027fbdbbb016c148a84ca33775e64cccf3e0` (PR #37 merge)
- Head: `feat/frontend-v1-1-design-upgrade`, code candidate `253bf485d40a9e4367db8968cf0d0d59faf8f127` plus the S6 records commit (no code after `253bf48`)
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

**Verification (local, final candidate)**
- Unit 119/0; Playwright Chrome 283/0/0 and Edge 283/0/0 on the production-style image.
- Clean clone `npm ci` + build; uncached image build; output isolation scan clean; `npm audit` 0.
- Initial JS 171–175 KiB (budget 200); CLS ≤ 0.019; no external requests, cookies or storage.
- A11 Docker drills (S5): failed build keeps the preview serving; dev/preview and port conflicts refused safely; dev hot reload 0.8 s without reload at `http://localhost:3000`; dev syntax-error recovery without restart; stop/start/teardown clean. No runtime configuration changed since.

**Not verified:** screen reader, physical phone, Safari, Firefox (A05 PARTIAL, deferred by the Owner for this stage); second-machine LAN probe; the Owner's physical Notes screenshot-shortcut check (pending). No WCAG conformance claim.

**Known open defect (S7):** every 404 has the right status and headers, but the server sends the framework's empty error document without `lang`; the localized view appears only after JavaScript (blank without it). Not compliant with DPT-PLAN-013 4.2 ("server `lang` on first byte") and V01; awaiting the Owner's decision on the tested correction (experimental `globalNotFound` plus proxy rewrites) or a recorded deviation.

**Review:** same-vendor fresh-context sub-agent reviews (not human or cross-vendor): S2 of `76dcb1c` (CONDITIONAL, fixed); S4 of `689b177` (CONDITIONAL, fixed) and deltas `bfb7210`, `c3f9688` (PASS); S6 of the translation delta `2f8b78a` (CONDITIONAL: stale browser tests, fixed) and `253bf48` (PASS).

**Records:** `Structure DB Obsidian/07_Delivery/Tasks/IMP-WEB-02_Frontend_V1_1.md`; S1–S6 reports and summaries; review reports; evidence under `08_Operations/Test_Evidence/IMP-WEB-02/`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Before publishing

1. Owner authorizes publication of this branch (scoped, one-time).
2. Re-verify the head SHA, `git status`, and that `main` is still `3e87027` (otherwise rebase decision by the Owner).
3. Exclude the untracked `Test_Evidence/IMP-WEB-02/CP4.zip` and any local-only file.
4. Push the branch, open the PR as Draft with the body above, and record the PR number in the task note.
5. Add the Owner's Notes check result to the body when reported.
6. Resolve the S7 404 item first (fix on a new reviewed candidate, or the Owner's recorded deviation), then update the head SHA and the "Known open defect" line.
