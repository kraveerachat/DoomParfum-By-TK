---
id: IMP-WEB-02-DRAFT-PR-PACKAGE
project: DoomParfum By TK
type: publication_package
status: final-for-publication
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, publication, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 — Draft Implementation PR package

PUBLIC_SAFE. Prepared locally (S3, revised in S4–S10). Final for publication in S10 under the Owner's one-time authorization of 2026-11-28: one normal push of this branch and exactly one Draft PR to `main`, using the Owner's login as a one-time exception (Decision Log). The PR is created from the body below exactly. Its number is known only after creation, so it is not in this file; see the canonical task note.

- Base: `main` at `3e87027fbdbbb016c148a84ca33775e64cccf3e0` (PR #37 merge; remote `main` re-verified 2026-11-28, S10)
- Head: `feat/frontend-v1-1-design-upgrade`; final reviewed application candidate `53d01265962059655764f8d65be5b71329e600c4`, then records-only commits (S9 records `519ee3f`, S10 closeout with the receipt)
- State on creation: **Draft**. Not Ready for Review. No auto-merge. The Owner merges.

## Title

feat(web): finalize bilingual luxury frontend V1.1 (IMP-WEB-02)

## Body

Implements merged planning amendment **DPT-PLAN-013 (PR #37)**, which amends DPT-PLAN-012, on the **mock-only, local-only** Next.js frontend.

**Scope:** `web/`, this task's Obsidian records and evidence, and the post-merge status lines of DPT-PLAN-013 in `PRODUCT.md` and the vault. No real catalogue data, database, matching, ETL, API, backend service, authentication or deployment. The preview runs on loopback only (`127.0.0.1:3000`).

**Reviewed application candidate:** `53d01265962059655764f8d65be5b71329e600c4` (`web/` tree `be5cea2608eb9e23fba8318d3fc2ea94498dfa6c`). Every later commit on this branch changes records only; the `web/` tree at the head equals the reviewed candidate.

### What changed

- **Design system:** gold–bronze semantic tokens and R1–R5 rules from DPT-PLAN-013; retired V1 gold removed from the favicon and drawings.
- **T1–T8 (Owner selections, CP4):** T1 Fahkwang 300 for Thai display (SIL OFL 1.1, self-hosted, 9,816 bytes); T2 centred hero; T3 record sheet; T4 compact Explore toolbar; T5 stable header; T6 compact language link; T7 equal Featured columns; T8 square corners.
- **English and Thai:** two route trees (`/` and `/th`) over one shell, typed dictionaries and a server-only Thai overlay. All **192 Thai translation decisions** approved by the Owner (159 kept, 33 replaced) and pinned by a unit test. Fictional proper names and family/accord labels stay as approved. Reviewed prose is found by Thai queries on English pages too (DPT-PLAN-013 4.5).
- **Header and accessibility:** stable sticky header. It turns static when it wraps to two rows, on short screens, without scripting below 1024px, and in print. The language control sits after Profile, with a compact language link on narrow layouts. Heading focus follows navigation modality: no ring after a pointer click, a ring after keyboard navigation, and the ring is kept when a screenshot tool takes window focus.
- **404 correction:** every unknown address returns a real 404. The document is rendered on the server with `<html lang>` and a localized title, heading and notice, and it reads without JavaScript. This covers unknown paths and slugs in both locales, unsupported locale prefixes and malformed addresses. It uses `app/global-not-found.tsx`. The proxy takes the locale from the path only, overwriting any client-supplied header, and rewrites malformed addresses and unknown slugs to `/_unavailable` or `/th/_unavailable`. Nonce CSP, `no-store`, `noindex` and the GET/HEAD-only method restriction hold; the ten valid routes are unchanged.

### Experimental dependency (Owner-authorized)

`experimental.globalNotFound` in `web/next.config.ts`, authorized only for the pinned **Next.js 16.4.6**, this local mock frontend and the reviewed scope. **A compatibility reassessment is required before any Next.js upgrade, live-data catalogue integration or production deployment.** The per-locale rewrite targets rely on Next.js 16.4.6 running the proxy again on an unmatched rewrite target. The proxy's fixture slug list is mock-only and is not the live-data route-resolution contract. No other experimental feature and no dependency change.

### Verification

Runs on the final candidate `53d0126` (S9):
- Unit 122/0.
- Type check, lint and build exit 0.
- Playwright Chrome 305/0 and Edge 305/0 on the production-style image `sha256:568cc3b30f8fef993d5db66e2e6f2bbfd5c6536c874b7786d3385d53c66f701e`.
- Raw-HTTP 404 probe and JavaScript-disabled checks pass.
- Output isolation scan clean.
- The new 404 regression tests fail on the previous candidate: e2e 18 of 19, unit 2 of 6.

Inherited:
- S6 on `253bf48`: clean clone `npm ci` + build, uncached image build, `npm audit` 0, initial JS 171.5–175.2 KiB (budget 200), CLS ≤ 0.0187. The lockfile and `package.json` are unchanged since.
- S5 Docker drills (A11 PASS on `c3f9688`): a failed build keeps the preview serving; dev/preview and port conflicts are refused safely; dev hot reload and syntax-error recovery work without a restart; stop, start and teardown are clean. Since then the Dockerfile, Compose and lockfile are unchanged, and `next.config.ts` gained only the experimental flag. The drills were not re-run.

Docker and rollback: the preview runs read-only, non-root, with all capabilities dropped, `no-new-privileges`, on loopback only. Local rollback images are kept: `253bf48-rollback` (`dedbba40…`), `s9-candidate1` (`10ded624…`), `v1-rollback` and older.

### Review

Same-vendor fresh-context sub-agent reviews; these are not human or cross-vendor reviews.
- S2, `76dcb1c`: CONDITIONAL, fixed.
- S4, `689b177`: CONDITIONAL, fixed; deltas `bfb7210` and `c3f9688` PASS.
- S6, `2f8b78a`: CONDITIONAL, fixed; `253bf48` PASS.
- S9, `3b93945`: CONDITIONAL; **`53d0126` PASS at runtime**.

### Owner acceptance (2026-11-28)

The Owner accepts Frontend V1.1 as the initial visual and functional mock baseline. T1–T8, the 192 Thai decisions, the reviewed Thai search behavior and the 404 correction (current pinned local mock scope) are accepted. Further UI/UX refinement is deferred until representative real data and working features exist.

### Not verified / deferred

- **A05 PARTIAL, Owner-deferred:** screen reader, physical phone, Safari and Firefox not run. No WCAG conformance claim.
- **Notes physical shortcut check (click Notes, Win+Shift+S, Escape): NOT RUN / OWNER-DEFERRED.** The Owner's earlier screenshot is a separate observation.
- Second-machine LAN probe not run. Not production-ready.

### Future prerequisites (not in this PR)

Live data needs separate Owner authorization. The prerequisites are:
- the independent U01/r14 security review;
- data field disposition;
- canonical identity and edition mapping;
- a least-privilege application principal;
- a read-only repository and service/API;
- a live-data 404 contract.

They are ordered in `Structure DB Obsidian/08_Operations/Reports/IMP-WEB-02/IMP-WEB-02_Next_Slice_Decision_Packet.md`.

### Records

- Task: `Structure DB Obsidian/07_Delivery/Tasks/IMP-WEB-02_Frontend_V1_1.md`.
- Final receipt: `Structure DB Obsidian/08_Operations/Receipts/2026-11-28_180705_IMP-WEB-02_Frontend_V1_1.md`.
- S1–S10 reports and summaries, review reports, and evidence under `Structure DB Obsidian/08_Operations/`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Before publishing (S10 checklist)

1. Owner authorization, scoped and one-time: received 2026-11-28 (push and one Draft PR; Owner-login exception confirmed in the session).
2. Re-verify the head SHA, `git status`, that `main` is still `3e87027`, that no PR exists for this branch, and that the `web/` tree equals `53d0126`.
3. Exclude the untracked `Test_Evidence/IMP-WEB-02/CP4.zip` and every local-only file.
4. Push the branch normally, open the PR as Draft with the title and body above, and verify it read-only on GitHub.
5. Record the PR number and verified state in the canonical task note as a LOCAL_ONLY reconciliation. No further push or PR change without fresh authorization.
