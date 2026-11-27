---
id: IMP-WEB-02-NEXT-DEV-HANDOFF
project: DoomParfum By TK
type: handoff
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, handoff, roadmap, read-only-catalogue, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# Next development handoff: from the accepted mock frontend to real read-only catalogue data

PUBLIC_SAFE. For the Owner and the next planning agent. Written at the end of IMP-WEB-02 (2026-11-28). It plans nothing new: it points at merged planning and says which decisions are still open. **No next task is started or allocated by this note.**

## Where the project stands

| Area | State |
|---|---|
| Frontend | Next.js mock-only frontend (IMP-WEB-01 merged PR #36; V1.1 IMP-WEB-02 on `feat/frontend-v1-1-design-upgrade`, candidate `253bf48`, local only). The Owner accepted the visual design as the initial baseline (2026-11-28). Synthetic fixtures only, no API, no database |
| Database | Local PostgreSQL schema, migrations 001–008 and `database/schema_contract.json` (IMP-P1-01, merged PR #2). Current DB, roles, grants, selections and rights are **not revalidated** since the planning snapshot |
| Data | Licensed Scento staging (IMP-P1-02, PR #5), local image rights (IMP-P1-03, PR #6) and the offline preview IMP-ENR-01 (PR #30): five records, 46 review slots, **43 DEFER / 3 UNKNOWN / 0 ACCEPT**. Nothing is accepted for display |
| Matching | Read-only input adapter, synthetic primitives, B1 and M1 (IMP-MATCH-01/02/03/08, PRs #11, #9, #27, #26). No real ranking |
| Records hygiene | Several merged task notes still carry pre-merge `status` values (IMP-P1-01/02/03, IMP-MATCH-01/02); Git history above is authoritative. Worth a docs-only reconciliation, not part of this handoff |
| Security | P30-U01 field-review contract: latest **r14 PROPOSED, not approved**; independent review (G-IND) not satisfied; Q-F pending; 0 of 169 acceptance specifications run (DPT-GATE-012, PR #32 documentation snapshot) |
| Planning | DPT-PLAN-011 merged (PR #31): [[Post_PR30_Dependency_and_Gate_Map]], [[Post_PR30_First_Readonly_Web_Slice_ADR]], [[Post_PR30_Principal_and_Authorization_Plan]]. **All 15 POST30-ODP-1 decisions are PROPOSED / UNANSWERED** ([[Post_PR30_Owner_Decision_Packet]]) |
| Other | PR #8 OPEN/DRAFT/BLOCKED. The primary checkout holds uncommitted matching planning (`plan/p2-dual-mode-matching`, `04_Matching/Dual_Mode_Matching_Architecture.md`), not reviewed here |

## The smallest real-data slice (already planned)

The merged map names it: **P30-U03 → U05 → U06 → U07**, fed by U01/U02 reviews and the U04 transition.

1. **U03** genuine application principal: a real login subject with least-privilege grants in a new private scope. The existing `dpt_runtime` role and `read_profile` are explicitly *not* acceptable application authority.
2. **U05** minimal read-only catalogue repository: catalogue and detail projections of reviewed, selected fields with current rights; authorize before lookup, count or filter.
3. **U06** strict read-only service: versioned request and response schemas, the proposed READ-V1 budgets, safe errors, no-store.
4. **U07** private shell with catalogue and detail views: sign-in, catalogue, detail, logout; text placeholders for images; honest unknown states.

Data prerequisites: **U01** human field review (accept/reject/defer per claim) and **U02** canonical identity and edition mapping, then **U04** a bounded transition of reviewed claims into the new scope. Matching (U10–U11), media (U08–U09), Cart/Collection (U12) and deployment (U13) are separate branches, not prerequisites of factual display.

Expectation set by the ADR: the first live catalogue may honestly show **zero items** until human review accepts claims; DEFER is never shown as ACCEPT to fill the page.

## What has to happen before any implementation starts

| Order | Gate | Needed from |
|---|---|---|
| 1 | Answer the slice decisions in POST30-ODP-1: **SEQ-01** (sequence), **APP-01** (backend direction; recommended Python backend with separate UI), **APP-02** (framework evaluation, recommended FastAPI), **APP-03** (UI hosting), **APP-04** (per-subject login), **APP-05** (read-only catalogue/detail scope), **APP-06** (READ-V1 bounds), **APP-07** (no-store, no offline) | Owner |
| 2 | Decide whether the accepted Next.js frontend becomes the UI of the live slice. APP-03's recommended option is a cohosted minimal UI; using this Next.js app is the "separate UI server" alternative and needs its own contract | Owner |
| 3 | U01: commission the independent r14 review (G-IND), then the Owner's security-design decision; only then can field review be executed | Owner (reviewer), then agent |
| 4 | DATA-01 to DATA-03 (review without promotion, explicit identity and edition, selected-use gate), then the actual human review of the five records | Owner |
| 5 | Allocate one implementation task for U03 (principal and grants contract, then migration task if approved), with fresh registry and PR checks | Planning agent, then Owner merge |

Each implementation node still needs its accepted contract, rights, Owner task authorization, isolated branch, tests, independent review, Draft PR and Human Merge (DEVELOPMENT_WORKFLOW).

## What can run now without new authority

- Read-only revalidation of the current database state (roles, grants, schema contract) as evidence for U03, if the Owner wants it before deciding APP-04.
- Owner decisions on the packet above (no agent work needed).
- Merging the IMP-WEB-02 Draft PR once publication is authorized and its open items are settled.

## Carried over from IMP-WEB-02

- The 404 documents are sent without server `lang` and are blank without scripting (S7). A tested correction exists (experimental `globalNotFound` plus proxy rewrites) and awaits the Owner's decision; the same 404 pattern will apply to any live route that calls `notFound()`, so decide it before U07.
- Dev hot reload works only at `http://localhost:3000` (S5).
- A05 manual accessibility checks (screen reader, phone, Safari, Firefox) are deferred, not done.
