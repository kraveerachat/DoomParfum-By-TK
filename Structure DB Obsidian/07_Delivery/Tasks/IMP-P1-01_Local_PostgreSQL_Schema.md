---
id: IMP-P1-01
project: DoomParfum By TK
type: task
status: in-progress
owner: project
updated: 2026-11-11
tags: [doomparfum, implementation, postgres]
source_of_truth: "../../../README.md"
requirements: [R01, R02, R03, R21]
planning_pr: 1
---

# IMP-P1-01 — Local PostgreSQL Schema Foundation

## Current task / session S1

READY FOR HUMAN OWNER REVIEW (Draft). Codex implementation/documentation; independent database review complete at source checkpoint d25083c67ea73384ab13068bf41fb70755c0a0d0.
Branch `impl/p1-01-local-postgres-schema`, base/START_SHA and approved planning merge
`bffb2fab1918dc5221a6c5da7920168bcae263ca`. PR #1 verified MERGED by GitHub and Git;
fresh fetch confirms main contains it. The old planning-branch worktree was clean.
Current user attachment explicitly authorizes this local-only implementation and Draft PR.
PRODUCTION_MUTATION=NO; HUMAN_MERGE_REQUIRED=YES.

## Hierarchical Task Map / scope and expected files

1. Repository/data preflight: read governance, approved model/decisions/receipt; verify 42 local package
   inventory entries and three raw hashes. DONE; dataset stays outside Git.
2. Environment: isolated task-labeled Docker container/volume, loopback PostgreSQL 16.15, pinned digest;
   generated development secret under ignored `.local/`; no global install/host setting changes.
3. Schema: `database/migrations/` in FK dependency order, all 47 approved logical tables; immutable claims,
   scoped FKs, typed/subtype checks, conflicts, rights, media, personal and matching contracts.
4. Evidence: `database/tests/`, local runner and coverage matrix; RED/GREEN, recreate/rollback,
   non-owner two-user RLS, positive/negative contracts, real-data shape checks without full import.
5. Review/docs: independent source/test review; ERD/dictionary/quality/security, backlog/roadmap/status,
   decisions/change/run log, implementation evidence and one final task receipt at readiness.
6. Publication: inspect exact diff/secret scan, commit/push task branch, one Draft PR; STOP for owner.

## Safety / dependencies / acceptance

No restricted-site scrape, raw dataset/private export/dump in Git, existing-container mutation,
production/cloud resources, hosted auth/storage, application/ETL runtime or IMP-P1-02 work.
Source raw arrays and repeated occurrences remain intact; ambiguous mappings need review/quarantine.
Shared DB primitives may be tested; product-facing sharing stays disabled/deferred.
Each logical table and required constraint must be verified against live local PostgreSQL; API/storage/
asset-byte/restore tests outside this task must be NOT RUN. Do not substitute admin-only RLS evidence.
Schema findings and unresolved boundaries must be explicit; no automatic model/decision widening.

## Tool decision / initial evidence

Existing GitHub MCP, Git 2.53.0.windows.2, Python 3.11.9, Docker Desktop 4.43.2 / Engine 28.3.2;
`ecc:postgres-patterns` guidance and PostgreSQL 16 primary documentation. No installer or account change.
Docker initially stopped; existing Desktop launched successfully, no host configuration changed.
Installed image `postgres@sha256:f1c3376c26f2609ab9f29f71f824103fe2fcd8ee0346485cb6122a4f93df6f94`
reports PostgreSQL 16.15. No application integration or Supabase dependency is chosen.
Local package sibling local package `DoomParfum Local Data/P1/20261110-221751/` verified:
1,479 perfumes / 160 houses / 420 materials; exact pilot 12/5/58/93; within-layer repeated labels
40 groups / 39 full profiles, none in pilot. No dataset replacement or canonical import.

## Test/evidence ledger and checkpoint

Local implementation verified: 47 tables, 141 FK / 47 PK / 91 UNIQUE / 93 table CHECK, 59 deferred
constraint triggers, 47 ENABLE/FORCE RLS tables; 69/69 tests passed via python database/verify.py, exit 0.
Actual named inventory/source hashes and full partial/NOT RUN matrix: [[IMP-P1-01_Implementation_Evidence]].
Independent exact-checkpoint review and document checks completed; Draft publication is the final API step after metadata commit/push.
Original [[2026-11-10_201028_DPT-PLAN-001_P1_Planning]] remains immutable and unchanged.
No implementation receipt yet; create once after acceptance/review, not at every checkpoint.


## S1 implementation and actual remaining work

Seven migration groups, local-only runner, synthetic positive/negative fixtures, rollback-only actual
12/5/58 package shape tests, aggregate duplicate investigation and machine-readable schema/test evidence
implemented. Empty foundation migrated with 53 field definitions and zero other rows. No ETL/full import.
Observed REDs/setup/report failures and targeted fixes are recorded in the evidence note.
Documentation reconciliation records PR #1 merge while retaining original research/receipt/Task Map.
Remaining at that checkpoint: review/checks/receipt/publication. Current closeout below supersedes that snapshot; Human Owner alone decides merge. IMP-P1-02 remains NOT STARTED.


## Independent review / correction checkpoint

Initial exact source review at 42ae1df46285b1f42772d92e13181dc16a55ac89 required five bounded fixes:
selected-rights reads in every scope, unrelated-write expiry isolation, non-finite numerics, canonical
LF migration/source checksums and per-operation local endpoint enforcement. All implemented; 69/69
full tests pass, exit 0. Unpublished empty foundation safely recreated and migration replay is no-op.
That correction snapshot preceded independent re-review; final outcome follows below.


## Final review / publication handoff

START_SHA and approved planning merge: bffb2fab1918dc5221a6c5da7920168bcae263ca.
FINAL_REVIEW_SHA / implementation source checkpoint: d25083c67ea73384ab13068bf41fb70755c0a0d0.
Independent review confirms five fixes, no remaining code/security blocker in reviewed fixes. The last
LOW document count is corrected to93. No source/migration change in closeout; final HEAD/actual PR URL
are verified from Git/GitHub after publication, not invented inside their own tracked commit.
All task acceptance in local scope is evidenced:69/69 tests, named constraints/RLS, source package/shape/
duplicate investigation, reset/recreate/rollback, docs/secret checks. API/ETL/bytes/storage/restore/cloud
remain explicitly NOT RUN/deferred. Source hashes match; original planning research/receipt unchanged.
Receipt: [[2026-11-11_000730_IMP-P1-01_Local_PostgreSQL]]. Implementation evidence: [[IMP-P1-01_Implementation_Evidence]].
At authoring, implementation PR NOT CREATED; final step is push this task branch and create one OPEN/
DRAFT PR to main, then STOP. Find it via [head-branch lookup](https://github.com/kraveerachat/DoomParfum-By-TK/pulls?q=is%3Apr+head%3Aimpl%2Fp1-01-local-postgres-schema).
Owner action: review/merge this PR; only afterward separately authorize/start IMP-P1-02. No auto-merge.
TOOL EXECUTION REPORT: existing GitHub/Git/PowerShell/Python/Docker, ecc:postgres-patterns, PostgreSQL
primary docs and independent reviewer used; no installation/host/account/cloud/production changes.
Exact changed-file manifest: database/evidence/documentation_checks.json. .local raw-derived details,
credentials and test logs ignored; no private data/dumps/backups committed. PRODUCTION_MUTATION=NO.


## S2 — Performance Review Correction / IN PROGRESS / 2026-11-11

START/REVIEWED_PR_HEAD=3d377e0d78ec3af86e4c6ca03302b633c4ff11a7. Existing PR #2 verified OPEN/DRAFT;
same branch impl/p1-01-local-postgres-schema; tree clean, origin/main bffb2fa; PR #1 merged verified.
Current owner explicitly authorizes bounded synthetic performance testing and same-PR correction.
Plan: measure25/100/250 draft synthetic records with actual deferred flush/call counts, add008 correction
migration if confirmed (do not edit published001–007), preserve every invariant/dynamic active-rights check,
add transaction-mode/no-op/savepoint/rollback/concurrency/privilege regressions, rerun full suite and
independent exact-source review, update evidence/docs/PR, non-forced branch push. No new PR/receipt.
Original immutable implementation receipt is historical and will remain byte-identical.
TOOLS: existing GitHub/Git/PowerShell/Python/Docker/PostgreSQL and primary PG16 docs; independent reviewer.
No install/host/cloud/production mutation, raw/private dataset publication or IMP-P1-02 runtime.
Performance DB uses disposable dpt_migration_probe only; 768MiB/2CPU task container, loopback only.
All fixtures synthetic and clearly marked; no capacity/production benchmark claim.
