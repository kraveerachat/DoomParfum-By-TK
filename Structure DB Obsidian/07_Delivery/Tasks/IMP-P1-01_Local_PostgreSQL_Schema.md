---
id: IMP-P1-01
project: DoomParfum By TK
type: task
status: in-progress
owner: project
updated: 2026-11-10
tags: [doomparfum, implementation, postgres]
source_of_truth: "../../../README.md"
requirements: [R01, R02, R03, R21]
planning_pr: 1
---

# IMP-P1-01 — Local PostgreSQL Schema Foundation

## Current task / session S1

IN PROGRESS. Codex implementation/documentation; independent database review before publication.
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
Independent exact-checkpoint review, document validation and Draft publication remain pending.
Original [[2026-11-10_201028_DPT-PLAN-001_P1_Planning]] remains immutable and unchanged.
No implementation receipt yet; create once after acceptance/review, not at every checkpoint.


## S1 implementation and actual remaining work

Seven migration groups, local-only runner, synthetic positive/negative fixtures, rollback-only actual
12/5/58 package shape tests, aggregate duplicate investigation and machine-readable schema/test evidence
implemented. Empty foundation migrated with 53 field definitions and zero other rows. No ETL/full import.
Observed REDs/setup/report failures and targeted fixes are recorded in the evidence note.
Documentation reconciliation records PR #1 merge while retaining original research/receipt/Task Map.
Remaining: exact source checkpoint independent review, final doc/secret/diff checks, one receipt and
commit/push/Draft PR publication; Human Owner decides merge. IMP-P1-02 remains NOT STARTED.


## Independent review / correction checkpoint

Initial exact source review at 42ae1df46285b1f42772d92e13181dc16a55ac89 required five bounded fixes:
selected-rights reads in every scope, unrelated-write expiry isolation, non-finite numerics, canonical
LF migration/source checksums and per-operation local endpoint enforcement. All implemented; 69/69
full tests pass, exit 0. Unpublished empty foundation safely recreated and migration replay is no-op.
New exact-source checkpoint/re-review pending; no final receipt or Draft publication yet.
