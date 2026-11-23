---
id: IMP-WEB-01
project: DoomParfum By TK
type: implementation_task
status: acceptance-pending
owner: human-owner
updated: 2026-11-24
requirements: [R01, R03, R04, R13, R14, R21]
planning_pr: 35
implementation_pr: null
tags: [doomparfum, implementation, frontend, docker, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-01 — Luxury editorial mock frontend and Docker runtime

## Current Task

- Type: IMPLEMENTATION (mock-only UI + local Docker). Agent: Claude Code.
- State: ACCEPTANCE PENDING (agent-side implementation and checks done; LF-05 and Owner review open). Session S1, 2026-11-24 Asia/Bangkok.
- Branch: `feat/imp-web-01-luxury-frontend`; base/target `main`.
- Starting/base SHA: `61932bef147816272a06cbe6eba9363940fa4baf` (PR #35 merge, freshly fetched, equals `origin/main`).
- Approved plan: [[DPT-PLAN-012_Luxury_Frontend_Editorial]], Planning PR #35 MERGED 2026-11-23.
- Implementation PR: NOT CREATED. No publication authority in this task (`LOCAL_ONLY` / `NOT_PUSHED`).
- Intake class (DEVELOPMENT_WORKFLOW §3.6): B. LF-01 to LF-04 are consolidated into this one task by the Owner's 2026-11-24 instruction, as the [[Luxury_Frontend_Acceptance_and_Task_Map]] allows. LF-05 (independent review) stays a separate gate.
- ID check: no `IMP-WEB-*` ID, branch or PR existed on any fetched ref or in the PR list before allocation.
- Production mutation allowed: NO.

## Goal / Why

Build the functional, mock-only five-route DoomParfum frontend from the merged plan and run it in Docker at `http://localhost:3000`.

## In Scope

`web/` application, fixtures, original visual studies, fonts with notices, tests, Dockerfile, preview and dev Compose files, and this task's vault records.

## Out of Scope / Do-not-touch

Database, matching, ETL, Security U01/r14, PR #8, existing migrations and receipts, other worktrees, unrelated untracked files, unrelated containers and volumes. No API, authentication, real data, scores, prices, service worker, push, PR, merge or deployment.

## Dependencies

Owner-merged PR #35; bounded dependency-setup and local container authority given in the Owner's 2026-11-24 task instruction.

## Acceptance Criteria + Evidence Needed

A01–A12 in [[Luxury_Frontend_Acceptance_and_Task_Map]]. Every result is recorded as PASS / FAIL / NOT RUN from an executed check.

## Task Map

1. CP1 Foundation and first Docker startup (LF-01)
2. CP2 Header, Home, About, dialogs (LF-02)
3. CP3 Explore, Detail, Notes, interactions (LF-03)
4. CP4 Integration, Docker hardening, acceptance (LF-04)

## Session Register

| Session | Purpose | State | Result | Checkpoint SHA | Evidence |
|---|---|---|---|---|---|
| S1 | Implement CP1–CP4 | CLOSED | PARTIAL (A05 manual checks and independent closure open) | `a5ddd6fe421870d2adeeac70f3e7150eee798890` | [[2026-11-24_IMP-WEB-01_S1_Report]] |

### Session S1 — implement DPT-PLAN-012

State: CLOSED. Agent/role: Claude Code, implementation.

#### Preflight (observed 2026-11-24)

- `origin/main` = `61932be`, contains the PR #35 merge. PR #8 observed OPEN / Draft at `84dccb1`; untouched.
- Protected worktrees observed and left unchanged: root (`9636ee7`), agent-workflow-pr-routing (`dc11d65`), dpt-doc-004 (`5719874`), dpt-gate-012 (`f6bf603`), dpt-ops-design-tools-proposal (`61932be`, detached).
- Docker Desktop was stopped. The Owner authorized one launch in chat. Engine 28.3.2, Linux/amd64, 20 CPUs, 16.6 GB; no existing container auto-started (four existing containers, all still Exited). Host C: 379 GB free; 9.6 GB physical memory free before launch. Port 3000 free before and after.
- `DESIGN.md`, `.ui-craft/` NOT FOUND on main. `PRODUCT.md` present and read.

#### Pinned choices and reasons

| Item | Pin | Reason |
|---|---|---|
| Next.js / eslint-config-next | 16.4.6 | Latest stable; includes the 2026-11-03 advisory fixes (patched in 16.4.5) |
| React / React DOM | 19.3.1 | Latest stable, in the Next peer range |
| TypeScript | 6.0.3 | TypeScript 7 is outside `typescript-eslint`'s peer range (<6.1) |
| Tailwind CSS | 4.3.5 | Latest stable |
| `@radix-ui/react-dialog` | 1.3.1 | The single shadcn-style dialog primitive |
| Node | 24.22.3 | LTS (maintenance, end of life 2028-04-30) |

OSV batch query 2026-11-24 returned no advisories for the queried direct versions.

#### Work performed, findings and fixes

- CP1 `f9dc22f`, CP2/CP3 `f04d912`, CP4 `a5ddd6f` (full SHAs in the report). 94 files; everything outside `web/` is this task's records.
- First acceptance run: 73 PASS / 18 FAIL. Real defects fixed: focus after navigation, no-script content, 200% text overflow, two narrow targets, accessible names, dimmed folio text. One test fault corrected.
- Runtime findings fixed: image optimizer endpoint refused in the proxy, server source maps and package managers removed from the image.
- Two read-only reviews of `f04d912` (no BLOCKER). Findings were turned into 25 browser regressions: 22 RED before, all GREEN after.

## Planned / Completed / Remaining

Completed: CP1–CP4. Remaining: LF-05 independent review of the final commit, A05 manual checks, Owner review, publication decision, Implementation PR, then the single final receipt.

## Test / Evidence Ledger

| Scope | Result |
|---|---|
| Unit, negative-control, boundary, contrast (`npm test`) | PASS 81 / FAIL 0 |
| Browser acceptance against the Docker preview | PASS 117 / FAIL 0 / SKIPPED 0 |
| A01–A04, A06–A12 | PASS within the limits listed in the report |
| A05 | PARTIAL: screen reader, real phone, Safari, Firefox NOT RUN |
| Image scan, `npm audit`, detector | Clean at the time of the run |
| Stock `validate_docs.py` | NOT USABLE on this branch (stops at binary fonts); unmodified |
| Database, matching, ETL, U01 suites | NOT RUN (untouched) |

Machine-readable evidence and screenshots: [IMP-WEB-01_Acceptance.json](../../08_Operations/Test_Evidence/IMP-WEB-01/IMP-WEB-01_Acceptance.json).

## Reports

| File | Session | SHA-256 (LF bytes) | Classification |
|---|---|---|---|
| [[2026-11-24_IMP-WEB-01_S1_Report]] | S1 | `a93e579f8057f696763eee7f30159b9217855f2bf1ff52460141e7ce3eaafaeb` | PUBLIC_SAFE |
| [[2026-11-24_IMP-WEB-01_S1_Summary]] | S1 | `489d3e79b5574adf3518512fd1bb9355d1efe4bfc18096d63e7b725cf251b92f` | PUBLIC_SAFE |

Final receipt: NOT CREATED (acceptance pending).

## Issues / Risks / Known Limitations

Twelve recorded deviations and limitations are in the report, including the route-loading change, hero padding, fixed optical size, ESLint 9 support status and container egress.

## Latest Git Checkpoint / SHA

Code: `a5ddd6fe421870d2adeeac70f3e7150eee798890`. The documentation commit that contains this note follows it on the same branch. LOCAL_ONLY / NOT_PUSHED / PR_NOT_CREATED. `AGENT_CREDENTIAL_REQUIRED`: no approved agent publishing identity was found, and the Owner's login was not used to publish.

## Handoff / Next Action

Owner reviews `http://localhost:3000` (preview left running; stop with `docker compose down` in `web/`), decides the recorded deviations, commissions LF-05 on the final commit, and authorizes publication separately.
