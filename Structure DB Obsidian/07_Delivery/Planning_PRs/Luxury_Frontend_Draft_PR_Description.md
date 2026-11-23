---
id: DPT-PLAN-012-PR
project: DoomParfum By TK
type: draft_pr_description
status: proposed
owner: human-owner
updated: 2026-11-23
tags: [doomparfum, planning-pr, draft, local-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# Proposed Draft Planning PR description — not published

Title: `docs(plan): specify luxury editorial mock frontend and Docker runtime`

Base: `main` at `03e2ab6080373033c02afc7ada7be2ceab5f24e2` (re-verify before publication). Head: `plan/luxury-frontend-editorial`. PR URL: NOT CREATED. No push or publication identity used in this task.

## Plan summary

The repository has no frontend. This documentation-only proposal defines an original luxury editorial mock shell across Home, Explore, Perfume Detail, Notes and About. It makes centered navigation, synthetic provenance, field states, responsive behavior, contrast and local-only Docker operation reviewable before implementation.

`IMPLEMENTATION_NOT_STARTED=YES`. No dependencies, application source, containers, database/API/authentication or deployment are included. New stack/runtime choices remain PROPOSED until the Human Owner accepts this bounded scope through Gate P.

## Requirements and alternatives

Demonstrates only synthetic discovery and note navigation related to R01/R03/R04/R13/R14 and provenance intent R21. Real-data requirements are not completed. Existing unified IA, U01, PR #8 and all architecture/matching/database histories are preserved. Framework-free static HTML remains a prior alternative; this proposal recommends the Owner's Next.js App Router/TypeScript/Tailwind/selective-primitives direction for `web/` only. No real-data backend/ORM/provider choice is made.

## Architecture and deliverables

- [[Luxury_Reference_Research_Matrix]]: all 20 references, desktop/mobile observations, inspected listing/detail coverage and explicit partial/untested fields. No assets copied.
- [[Luxury_Routes_and_Wireframes]]: exact five route contracts, centered header, overlays, desktop/tablet/mobile layouts and field/error states.
- [[Luxury_Design_Tokens_and_Components]]: palette roles/contrast restrictions, type, spacing, grids, surfaces, focus, motion and components.
- [[Luxury_Mock_Fixture_Contract]]: original synthetic fixture contract, local search/filter, no external data or persistent catalogue cache.
- [[Luxury_Docker_Runtime_Proposal]]: loopback Compose runtime, multi-stage standalone output, separate development and production-style preview, future Ubuntu/Cloudflare gates.
- [[Luxury_Frontend_Acceptance_and_Task_Map]]: requirement mapping, A01–A12 acceptance tests and proposed implementation units.
- [[Luxury_Design_Critique_and_Audit]]: separate requested planning passes and evidence limitations.
- PRODUCT.md and canonical task/report/summary/status/decision/tool records establish continuity. Exact changed-file inventory and validation are recorded in the S1 execution report.

## Acceptance and validation

Planning checks: existing documentation validators in both supported modes with evidence writes suppressed; link/frontmatter/fence checks; exact contrast calculation; reference/route coverage; changed-path allowlist; sensitive-content pattern scan; `git diff --check`; independent read-only design and evidence reviews. Exact executed results belong in [[DPT-PLAN-012_Luxury_Frontend_Editorial]] and its S1 report; proposed tests are not test results.

Future implementation evidence: routes, fixture rejection, search/filter truth, keyboard/focus, no-network/storage, no-store payload delivery, contrast, reflow, centered geometry, Docker binding/teardown and bounded visual confirmation. None has been run against a frontend here.

## Risks, open decisions and limitations

Reference media/population and many dedicated product pages were only partially inspected or not inspected; no unseen behavior is invented. Exact dependency/font file pins, target-host behavior, runtime CSP compatibility, complete accessibility and performance remain implementation evidence. Muted gold and fine divider fail functional contrast roles on ivory; use the specified restricted roles. Public access/noindex is a deferred preference, not privacy protection or deployment approval.

LF-OD-01/03/04 require explicit bounded plan acceptance. LF-OD-02 visual direction is confirmed in chat but exact implementation is proposed. LF-OD-05 public exposure remains deferred. The Owner may request more reference inspection before accepting the bounded research coverage.

## Source links

Twenty official storefront sources are linked individually in the research matrix. Technical primary sources are linked in the Docker proposal and font proposal, inspected 2026-11-23. No third-party source license is inferred from public access.

## Human gates and rollback

This text is a proposed PR body, not an opened PR. Obtain new scoped publication authorization/identity before pushing or creating a Draft PR. Human Owner reviews and merges; no auto-merge. Implementation begins only after verifying the merged planning SHA and accepted scope. Planning rollback is reverting this task's documentation checkpoint through a reviewed PR; do not rewrite shared history or modify historical receipts.
