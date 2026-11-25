---
id: IMP-WEB-01
project: DoomParfum By TK
type: implementation_task
status: acceptance-pending
owner: human-owner
updated: 2026-11-25
requirements: [R01, R03, R04, R13, R14, R21]
planning_pr: 35
implementation_pr: 36
tags: [doomparfum, implementation, frontend, docker, mock-only]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-01 — Luxury editorial mock frontend and Docker runtime

## Current Task

- Type: IMPLEMENTATION, mock-only. Current recovery/records coordinator: Codex (S4); implementer: Claude Code (S1–S3).
- State: ACCEPTANCE PENDING for Human visual/final local-mock review. Decisions1–10 accepted in PR36 scope;11 explicitly defers unavailable A05manual checks. A05 PARTIAL; A10 second-machine LAN NOT RUN.
- Branch: `feat/imp-web-01-luxury-frontend`; base/target `main`.
- Starting/base SHA: `61932bef147816272a06cbe6eba9363940fa4baf` (PR #35 merge, freshly fetched, equals `origin/main`).
- Approved plan: [[DPT-PLAN-012_Luxury_Frontend_Editorial]], Planning PR #35 MERGED 2026-11-23.
- Implementation PR: [#36](https://github.com/kraveerachat/DoomParfum-By-TK/pull/36), verified OPEN / DRAFT at published `cda91ff7ba00a44d5b8be53a2dbff68553c6736c`. Earlier LOCAL_ONLY / PR_NOT_CREATED statements below are historical snapshots, superseded for current publication state by S4.
- Intake class (DEVELOPMENT_WORKFLOW §3.6): B. LF-01 to LF-04 are consolidated into this one task by the Owner's 2026-11-24 instruction, as the [[Luxury_Frontend_Acceptance_and_Task_Map]] allows. LF-05 (independent review) stays a separate gate.
- ID check: no `IMP-WEB-*` ID, branch or PR existed on any fetched ref or in the PR list before allocation.
- Production mutation allowed: NO.

## Goal / Why

Build the functional, mock-only five-route DoomParfum frontend from the merged plan and run it in Docker at `http://localhost:3000`.

## In Scope

`web/` application, fixtures, original visual studies, fonts with notices, tests, Dockerfile, preview and dev Compose files, and this task's vault records.

## Out of Scope / Do-not-touch

Database, matching, ETL, U01/r14, PR8, existing migrations/receipts, other worktrees, unrelated files/containers/volumes. No API/authentication/real data/scores/prices/service worker/merge/deployment. Only S4 records-only normal push and PR36 description update have the explicit one-time Owner exception below.

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
| S4 | Existing preview recovery and PR36 records reconciliation | CHECKPOINT | ACCEPTANCE PENDING; A05 PARTIAL | containing records-only commit; exact SHA in PR/final delivery | [[2026-11-25_IMP-WEB-01_S4_Report]] |

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

Completed: CP1–CP4/S2/LF-05/S3, publication as Draft PR36, Owner decisions1–10/11deferral, S4 preview recovery/records reconciliation. Remaining: Human visual/final local-mock acceptance; A05 PARTIAL, A10remoteLAN NOT RUN; one final receipt only after acceptance.

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
| [[2026-11-25_IMP-WEB-01_S4_Report]] | S4 | `5bfbc6fa5244b3904670ad54c088e99d2f97c5c7ff3773877130e14b04688256` | PUBLIC_SAFE |
| [[2026-11-25_IMP-WEB-01_S4_Summary]] | S4 | `088edeeca13df3e0ae3e12601490be739a7c214269919a2eff8b8bdb55cb789c` | PUBLIC_SAFE |

LF-05 and S3 review reports: SHA-256 `37852101f9ed8a0b9b4defab2c6d7fd6df0fd4aadc113e1282278a9fc6ade290` and `91c59dcc1e786d13977e00b913bcc54b6d2c1d99f8851497fee9a9eb06667f9c`; PRIVATE_EVIDENCE_NOT_PUBLISHED.

Final receipt: NOT CREATED (acceptance pending).

## Issues / Risks / Known Limitations

Twelve recorded deviations and limitations are in the report, including the route-loading change, hero padding, fixed optical size, ESLint 9 support status and container egress.

## Latest Git Checkpoint / SHA

Code remains `449178093ed7616570cf651f8b5e4f3cc2d3001e`; web tree `2cf8c4f5b384605d0239301e5888318923f6d627`. Published starting HEAD `cda91ff7ba00a44d5b8be53a2dbff68553c6736c` is PR36 OPEN/DRAFT. S4 is one records-only containing commit, exact new local/remote SHA in PR description/final delivery. No approved agent identity is configured; existing Owner authentication is explicitly authorized only for this update. Older LOCAL_ONLY statements are historical.

## Handoff / Next Action

Owner inspects restored healthy http://127.0.0.1:3000/ and explicitly confirms final local-mock acceptance with remaining limitations. Decisions1–10/11deferral are already recorded; A05 is not PASS. No final receipt until acceptance. One-time records publication authority expires on completion.

## Session S4 — runtime recovery and published-record reconciliation (2026-11-25)

Recovery/records work completed; ACCEPTANCE PENDING. Agent: Codex coordinator. Intake A: continuation of this task/branch/PR36, not a new task or Planning PR. Starting/published SHA `cda91ff7ba00a44d5b8be53a2dbff68553c6736c`; fetched main `61932bef147816272a06cbe6eba9363940fa4baf`; reviewed application `449178093ed7616570cf651f8b5e4f3cc2d3001e`. Both application trees equal `2cf8c4f5b384605d0239301e5888318923f6d627` before work.

Owner scope: bounded Docker Desktop/local frontend recovery; verify the recorded S3 image and loopback3000, smoke five route types/unknown404/browser; reconcile current task/status/index/logs and Owner decisions recorded in the actual PR; one records-only commit and one normal branch push plus one PR-description update. Existing Owner authentication is permitted solely if no approved agent identity is available. This permission does not approve final acceptance, source changes, Production, merge or a final receipt.

Do not touch: complete `web/` tree, S1/S2/S3 committed reports/evidence, migrations/receipts, PR8/U01/DB/matching/ETL, protected PostgreSQL containers/volumes, unrelated `eleuthex-hermes` and S2 rollback image. No prune/reset/reinstall/network change/unrelated process termination. A05 remains PARTIAL with explicit manual-test deferral; A10 second-machine LAN check remains NOT RUN. New evidence will describe only checks actually rerun during recovery.

### Verified S4 execution and Owner decisions

Source: actual PR36 description at published cda91ff, read2026-11-25. Later Owner decisions supersede historical PENDING recommendations, not their dated evidence.

| # | Item | Decision |
|---|---|---|
| 1 | Route loading retains the current page | ACCEPTED |
| 2 | Responsive hero padding takes precedence over the conflicting fixed padding and viewport requirements | ACCEPTED |
| 3 | Fixed optical font size | ACCEPTED |
| 4 | No Radix overlay part | ACCEPTED |
| 5 | Accord descriptors and sorting behavior | ACCEPTED |
| 6 | 16px text links | ACCEPTED |
| 7 | House-label position | ACCEPTED |
| 8 | Tablet 4:3 imagery, horizontal third Featured entry, `proxy.ts` redirect architecture | ACCEPTED |
| 9 | No-JavaScript navigation fallback, HTTP 405 for unsupported write methods | ACCEPTED |
| 10 | Documented framework/HTTP-layer header and redirect exceptions | ACCEPTED, loopback-only synthetic preview |
| 11 | Unavailable A05 manual checks | EXPLICITLY DEFERRED for this stage; A05 stays PARTIAL |

Header exceptions accepted only for loopback synthetic preview; reassess before public exposure. No real-data/Production acceptance.

Supported Desktop restart recovered engine28.3.2; existing doomparfum-web/container69d92c01 with recorded S3 image43be51f1 started without rebuild/recreate, fixed127.0.0.1:3000. Running/healthy; five route types200, unknown404, browser Home rendered. Four protected containers stay stopped;32volume metadata and S2rollback fingerprints match across frontend startup. First readable baseline was after Desktop recovery; DB-content integrity NOT RETESTED.

97tracked web files compare byte-for-byte with reviewed4491780, tree2cf8c4f5 unchanged. Full historical suites NOT RERUN. LF-05/S3 were same-vendor implementer-commissioned subagents, not human/cross-vendor/authenticated independent acceptance; S3 final PASS was delta-only and excluded visuals/axe/npmci/Dockerbuild/A10/A11. Review report hashes above stay unchanged.

Environmental failures retained: sandbox pipe denial/timeouts/start-status inconsistency resolved by supported recovery; initial header-case checker corrected, no source fix. New scoped documentation/sensitive-content/diff checks and one records-only publication checkpoint required before handoff; exact outcomes in S4 ledger/PR delivery. No source/DB/Production change or final receipt. Full report [[2026-11-25_IMP-WEB-01_S4_Report]], summary [[2026-11-25_IMP-WEB-01_S4_Summary]], [S4 evidence](../../08_Operations/Test_Evidence/IMP-WEB-01/S4/IMP-WEB-01_S4_Recovery.json).

### Final S4 verification ledger

PASS:97tracked web files byte-equal to reviewed4491780,0mismatches; tree2cf8c4f5 unchanged. Scoped records checks:11allowlisted paths,10Markdown,4relative links,684wikilinks,0errors/0sensitive candidates; pre-existing Tool_Usage_Log missing-owner warning retained. Git diff --check PASS after correcting4new trailing spaces. JSON-wikilink checker inventory corrected, no historical-link edits.146old protected paths unchanged. Full historical suites and A05manual/A10remoteLAN NOT RUN. Actual new records SHA/publication exhaustion verified in PR/final delivery; no final receipt.
