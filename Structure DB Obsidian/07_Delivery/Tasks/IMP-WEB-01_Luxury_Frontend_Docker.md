---
id: IMP-WEB-01
project: DoomParfum By TK
type: implementation_task
status: acceptance-pending
owner: human-owner
updated: 2026-11-25
requirements: [R01, R03, R04, R13, R14, R21]
planning_pr: 35
implementation_pr: null
tags: [doomparfum, implementation, frontend, docker, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-01 — Luxury editorial mock frontend and Docker runtime

## Current Task

- Type: IMPLEMENTATION (mock-only UI + local Docker). Agent: Claude Code.
- State: ACCEPTANCE PENDING (agent-side implementation, checks and LF-05 reconciliation done; A05 manual checks and Owner decisions open). Sessions S1 and S2, 2026-11-24; S3, 2026-11-25 Asia/Bangkok.
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
| S2 | Bounded UI/UX refinement and verification pass (Owner instruction 2026-11-24) | CLOSED | PARTIAL (A05, A11 in part, LF-05 open) | `9918a387b24b89905b0da82f10894d85051e58cd` | [[2026-11-24_IMP-WEB-01_S2_Report]] |
| S3 | LF-05 corrections, reproducibility, publication readiness (Owner instruction 2026-11-25) | CLOSED | PARTIAL (A05 and Owner decisions open) | `449178093ed7616570cf651f8b5e4f3cc2d3001e` | [[2026-11-25_IMP-WEB-01_S3_Report]] |

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

### Session S2 — bounded UI/UX refinement

State: CLOSED. Agent/role: Claude Code, implementation. Start `94820c289fe4d484b5b2209dbcc19fbb10f6ba4d`, code checkpoint `9918a387b24b89905b0da82f10894d85051e58cd`. Only `web/` and this task's records changed; do-not-touch surfaces as in S1.

- Docker Desktop was stopped; the Owner authorized one launch in chat. The four protected containers were Exited before and after.
- Ten groups of rendered problems corrected; 18 browser regressions added, 16 of them RED first.
- Deviation 2 reduced, the stagger of 5 removed, 6 corrected for action links. 1, 3, 4, the rest of 5 and 7 stay open for the Owner.
- Before/after sheets: `08_Operations/Test_Evidence/IMP-WEB-01/S2/`.

### Session S3 — LF-05 reconciliation

State: CLOSED. Agent/role: Claude Code, implementation. Start `b8383ecb76c4cd72e16129ea319f1f22938be550`, code checkpoint `449178093ed7616570cf651f8b5e4f3cc2d3001e`.

- LF-05 on S2 (same-vendor sub-agent, read-only): CONDITIONAL, no P0 to P2. Review completed, findings reconciled in S3; no human or cross-vendor review. Report hash and limits are in the S3 report.
- S3 review by a fresh sub-agent: CONDITIONAL at `32574e8`, PASS for the code at `4491780`. Not Owner acceptance.
- The Owner approved one bounded stop and replacement of the preview for A11 in chat.
- Deviations 1 to 7, the S2 interpretations, the S3 additions and the header exceptions stay PENDING for the Owner.

## Planned / Completed / Remaining

Completed: CP1–CP4, the S2 refinement, the LF-05 review and the S3 corrections. Remaining: A05 manual checks or explicit deferral, Owner decisions, publication authority, Implementation PR, then the single final receipt.

## Test / Evidence Ledger

Current code (S3, `4491780`):

| Scope | Result |
|---|---|
| Unit, boundary, contrast, proxy (`npm test`) | PASS 85 / FAIL 0 |
| Browser suite on the preview | Chrome PASS 189 / FAIL 0; Edge PASS 189 / FAIL 0 |
| Fresh clone, empty npm cache, uncached image build | PASS |
| A01–A04, A07–A12 | PASS within the limits in the S3 report |
| A05 | PARTIAL: screen reader, real phone, Safari, Firefox NOT RUN |
| A06 | PASS with recorded pre-proxy header exceptions |

Evidence: [IMP-WEB-01_S3_Acceptance.json](../../08_Operations/Test_Evidence/IMP-WEB-01/S3/IMP-WEB-01_S3_Acceptance.json). S2 (`9918a38`): 81 unit, 135 browser. The table below is the historical S1 record.

| S1 scope | S1 result |
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
| [[2026-11-24_IMP-WEB-01_S2_Report]] | S2 | `4ca748a9750ddfd810a5241d26c75cbd1c1028cab203c4ef49792eee8a64663a` | PUBLIC_SAFE |
| [[2026-11-24_IMP-WEB-01_S2_Summary]] | S2 | `48c5b6f524d5960eade3113c956b83979c50432dd042e8bcd425f97ea11664ce` | PUBLIC_SAFE |
| [[2026-11-25_IMP-WEB-01_S3_Report]] | S3 | `0c5ca9764f659aa0a4b4f295c679153cea0fcf95945e68fabff3e4609f4e6315` | PUBLIC_SAFE |
| [[2026-11-25_IMP-WEB-01_S3_Summary]] | S3 | `a453a4b89be70f1b1728ac0a01197d5bfaadcf46a6d39b2a06d4f800d3e5ee1b` | PUBLIC_SAFE |

LF-05 and S3 review reports: SHA-256 `37852101f9ed8a0b9b4defab2c6d7fd6df0fd4aadc113e1282278a9fc6ade290` and `91c59dcc1e786d13977e00b913bcc54b6d2c1d99f8851497fee9a9eb06667f9c`; PRIVATE_EVIDENCE_NOT_PUBLISHED.

Final receipt: NOT CREATED (acceptance pending).

## Issues / Risks / Known Limitations

Twelve recorded deviations and limitations are in the report, including the route-loading change, hero padding, fixed optical size, ESLint 9 support status and container egress.

## Latest Git Checkpoint / SHA

Code: `449178093ed7616570cf651f8b5e4f3cc2d3001e` (S3; S2 was `9918a387b24b89905b0da82f10894d85051e58cd`, S1 was `a5ddd6fe421870d2adeeac70f3e7150eee798890`). The documentation commit that contains this note follows it on the same branch. LOCAL_ONLY / NOT_PUSHED / PR_NOT_CREATED. `AGENT_CREDENTIAL_REQUIRED`: no approved agent publishing identity was found, and the Owner's login was not used to publish.

## Handoff / Next Action

Owner reviews `http://localhost:3000` (preview left running; stop with `docker compose down` in `web/`), decides the items in the S3 report, runs or defers the A05 manual checks, and authorizes publication separately.
