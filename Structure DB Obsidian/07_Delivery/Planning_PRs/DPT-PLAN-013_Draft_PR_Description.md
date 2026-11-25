---
id: DPT-PLAN-013-PR
project: DoomParfum By TK
type: draft_pr_description
status: proposed
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, planning-pr, draft, local-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# Planning PR — Frontend V1.1 design upgrade amendment

Not published. PR title: `plan(frontend): DPT-PLAN-013 Frontend V1.1 design upgrade amendment`. Base `main` at `ab3351a8432d1d6664a6b4281784cfea56b0b9fa`, head `plan/frontend-v1-1-design-upgrade`. Re-verify both before publication. The text below is the PR body.

## Goal and problem

Frontend V1 is merged (#36). The Owner wants an upgrade of the same design: English and Thai, a sticky header, a gold and bronze detail palette, a clear rule system, better type and page refinements. These change parts of the merged DPT-PLAN-012 contract, so DEVELOPMENT_WORKFLOW §3.4 requires this docs-only amendment before any code.

Main document: [[DPT-PLAN-013_Frontend_V1_1_Amendment]].

## Requirements covered (Rxx)

Mock demonstration only of R01, R03, R04, R13, R14 and R21, as in V1. No real-data requirement is completed.

## Proposed / Accepted / Deferred decisions

- Owner-directed: upgrade, not redesign; English paths kept and Thai under `/th`; no cookie or storage; stable sticky header; language control after Profile; wordmark and fictional names kept; no Thai display font before rendered comparison.
- Proposed here: measured color roles, two root layouts (spike first), server-only Thai overlay, language switch as a document navigation, search rule that leaves English results unchanged, H1 outline contract.
- Open: V11-OD-01, 03 to 06 and 08 to 12. Deferred: real-data items of the proposal.
- Rejected: preference cookie, specimen route in the app, underline-only selects and hidden help as defaults, uppercase eyebrows on every section, recommendation list, bottom sheet, one PR per item.

## Major Topics and Subtasks

CP0 baseline, CP1 foundation and font specimen, CP2 language and header, CP3 pages, CP4 one Owner comparison batch, CP5 verification.

## Architecture / Data / UX impact

Two document languages with a shared shell and typed dictionaries. Fixture records unchanged. Alternatives considered: query parameter, `/en` plus `/th`, one `[locale]` layout with a rewrite (kept as fallback), changed fixture fields.

## Source licensing and privacy impact

No font or asset added here. Candidate fonts need a confirmed self-hosting license before use. No personal data, cookie, tracking or external request. The exact proposal text is not included; its hash and a section trace are (V11-OD-12).

## Acceptance criteria for implementation

A01 to A12 for both languages plus V01 to V16. All NOT RUN. A05 stays PARTIAL. No WCAG conformance claim.

## Implementation PR breakdown and dependencies

One task, proposed ID `IMP-WEB-02`, one branch and one PR, after this PR is merged by the Owner.

## Open questions / Known risks

The two-layout approach, its 404 behavior and nonce CSP are unproven until the CP2 spike. Thai fit depends on the selected font. Bodoni at 22px may be too fine. The doubled rule reported on Explore is not yet reproduced.

## Obsidian files updated

New: amendment, task note, this text, S1 report and summary, receipt, evidence. Added sections in four V1 contracts and the Docker proposal, PRODUCT.md, DPT-PLAN-012 and IMP-WEB-01 notes, status, index, backlog, roadmap, acceptance criteria, pending questions, decision, change, run and tool logs.

## Verification of docs / links / diffs

See the S1 report: frontmatter, wiki and relative links, fences, scope allowlist, sensitive patterns, contrast recomputation, `git diff --check`. `web/` is unchanged. No independent reviewer.

## Owner approval checklist

- [ ] Scope agreed
- [ ] Data policy agreed
- [ ] Acceptance agreed
- [ ] Ready to merge planning to main

IMPLEMENTATION_NOT_STARTED=YES
PRODUCTION_MUTATION_PERFORMED=NO

🤖 Generated with [Claude Code](https://claude.com/claude-code)
