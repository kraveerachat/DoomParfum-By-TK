---
id: IMP-P1-01-RECEIPT
project: DoomParfum By TK
type: immutable_receipt
status: ready-for-owner-review
owner: project
updated: 2026-11-11
tags: [doomparfum, implementation, receipt, postgres]
source_of_truth: "../../../README.md"
---

# IMP-P1-01 — Immutable Local Schema Review Receipt

Created 2026-11-11T00:07:30.928201+07:00. One receipt for this implementation task/PR; do not rewrite.
Later publication/merge events belong in canonical task/event logs, never a second receipt.
Original planning receipt remains untouched: [[2026-11-10_201028_DPT-PLAN-001_P1_Planning]].

| Field | Verified value at receipt |
|---|---|
| TASK / TYPE / PURPOSE | IMP-P1-01 / IMPLEMENTATION / disposable local PostgreSQL schema contracts before sample ETL |
| APPROVED_PLAN_PR / MERGE_SHA | #1 MERGED / bffb2fab1918dc5221a6c5da7920168bcae263ca |
| BRANCH / BASE / START_SHA | impl/p1-01-local-postgres-schema / bffb2fab1918dc5221a6c5da7920168bcae263ca |
| FINAL_REVIEW_SHA | d25083c67ea73384ab13068bf41fb70755c0a0d0 — independently reviewed source/tests; next commit metadata only |
| PR_URL / STATE_AT_RECEIPT | NOT CREATED; final authorized step after metadata commit/push is one OPEN/DRAFT PR to main |
| REVIEW_READINESS | READY FOR HUMAN OWNER REVIEW; no remaining code/security blocker in reviewed fixes; not owner-accepted/merged |
| PRODUCTION_MUTATION / DEPLOYMENT | NO / NOT PERFORMED |

## Exact scope and file manifest

Seven migration groups,47 logical tables; local runner/guards,69 integration tests, sanitized schema/test/
doc evidence, fixed model/security/quality/decision/status/log documentation and this receipt.
Exact repository-relative changed paths: `database/evidence/documentation_checks.json` changed_paths,
plus live PR file list. No raw dataset, personal export, image binary, secrets, dump, backup or cloud config.
Separate dpt_ops migration ledger is infrastructure, not a48th logical table. No frontend/ETL runtime.

## Actual SQL and evidence

PostgreSQL16.15 image sha256:f1c3376c26f2609ab9f29f71f824103fe2fcd8ee0346485cb6122a4f93df6f94,
local task-labeled container/volume,127.0.0.1:55431 only. Foundation has53 field definitions and zero
other domain rows. Final empty foundation recreated after checking emptiness/no other connection;
canonical UTF8/LF migrations apply/replay no-op. No data-bearing or published migration rewritten.

Actual:47 PK,141 FK,91 UNIQUE,93 table CHECKs,59 deferred constraint-trigger constraints,5 domain checks,
396 NOT NULL columns,244 indexes,203 RLS policies,196 user triggers;47 ENABLE/FORCE RLS tables.
Named definitions/hashes: `database/evidence/schema_inventory.json` and `test_results.json`.
`python database/verify.py`:69/69 passed,0 failures/errors/skips,exit0;105.453 seconds.
`python database/validate_docs.py` and Git diff/staged checks: actual final results recorded in doc evidence.

Non-owner Alice/Bob/guest/curator, actual FORCE owner RLS, WITH CHECK, private overlay/variant/source
isolation, shared reader/editor/revocation, immutable source occurrences, exact selected/conflict membership,
whole-field materialization/deletion, rights expiry in every scope, per-asset tuple/hash/lineage/use,
unrelated-tenant expiry isolation, finite numerics, failure rollback/recreate/write-skew/endpoint/EOL
checks all have actual local tests. Independent reviewer confirmed five fixes using source and bounded
rollback-only probes; did not rerun full suite. Remaining LOW doc count corrected to93 before receipt.

## Data rights / limits / next action

External local package full manifest/raw hashes verified;12/5/58/93 shape fixtures rollback.40 repeated
note groups/39 profiles preserved with original ordinals; no silent dedup or full/sample ETL. Synthetic
rights/users/image metadata are test controls, not real permissions/product facts/physical bytes.
All18 OBS/ACL/IMG/REC cases have honest DB-vs-later coverage in [[IMP-P1-01_Implementation_Evidence]].
API/JWT/cache/search/export/error masking, actual bytes/SSRF/proxy/storage, benchmark, independent
DB/object restore, hosted readiness and application build/e2e remain NOT RUN/not in current scope.

Conservative schema findings remain disclosed; SQL cannot establish legal truth. Cloud/provider/storage,
final retention/RPO/RTO/external backup remain DEFERRED; regional imports blocked by rights AND samples.
No new grants, global installs, host/account changes, main push, merge, auto-merge or deployment.

Next: publish the committed task branch as one Draft PR, verify actual head/URL/open/draft state, STOP.
Human Owner reviews/merges; IMP-P1-02 may start only afterward in a separately authorized task.
Canonical task [[IMP-P1-01_Local_PostgreSQL_Schema]] records publication handoff without inventing its
own resulting commit SHA. Tool paths/versions and full actual failure/fix history: [[Agent_Run_Log]].
