---
id: DPT-EVD-IMP-P1-02
project: DoomParfum By TK
type: test_evidence
status: review-pending
owner: human-owner
updated: 2026-11-11
tags: [doomparfum, scento, etl, evidence]
source_of_truth: "../../../README.md"
---

# IMP-P1-02 — Local licensed execution evidence

Task: [[IMP-P1-02_Licensed_Scento_ETL]]. Base main a908711fb4f37a12fbec3665a461b75c288c7dab;
branch impl/p1-02-licensed-scento-staging. P1/OD-01..06 and merged PRs1/2/3 govern the private local
boundary. PR4 matching remains Draft; no matching decision is accepted here. Human Owner alone merges.

## Actual source and canonical counts

Scento revision086769ecf1add770ea6646bd4d88d39f0e7cddeb, CC BY4.0, six pinned artifacts verified.
Attribution: Scento — https://www.scento.com/perfume-database ; license https://creativecommons.org/licenses/by/4.0/ .
Original42-file P1 package hashes and all1479 CSV/JSONL ordered arrays reconciled. Two deterministic
external source-index builds reproduce9 outputs byte-for-byte. No raw files enter the public repo.

| Scope | Perfumes | Brands | Notes | Raw occurrences | Canonical note links |
|---|---:|---:|---:|---:|---:|
| Approved P1 pilot | 12 | 5 | 58 | 93 | 80 |
| Full local cohort | 1479 | 160 | 420 | 12448 | 11972 |
| Historical handoff research fixture, separate | 12 | 11 | 46 | 84 | Not a DB import |

Full cohort1435 exact-source approved/44 draft holds:43 repeated-list profiles plus Khamrah external
conflict. Repeated pyramid scope40 extra occurrences/39 profiles; general-list scope adds5/4, total45/43.
No silent deduplication or fabricated second source claim. Unselected flat-list observations survive.
Full inventory2059 captures/2134 staging/2batches/8536 validations/10489 observations/8845 selections;
staging includes75 pilot and2059 full-batch rows. Matching eligible0; acquired images0; verified Dupe0.

## Tests and measurements

- Focused importer19/19 pass37.060s. Full suite98/98 pass216.297s: original79 plus19 new,0fail/error/skip.
- Positive/negative pinned hashes, missing/tampered license, exact reviewed-policy binding, malformed
  synthetic notes/year, distinct editions, unreviewed promotion refusal, rights revocation/expiry,
  complete rollback, non-owner isolation, held Khamrah, zero-growth replay, contrary canonical row/
  selection/validation evidence, forbidden target/reset/output overwrite, concurrent source intake.
- Full first committed452.016s; current-source full replay291.219s,0new capture/staging, identical whole
  inventory. Replay overlapped regression. Neither result is a controlled capacity benchmark.
- First full/pilot replay source hashc90da7... and later current-source replay a9a392... are separately
  retained. Original pilot-first did not record source hash/time; these fields are not backfilled.
- Source hashes, eight unchanged migrations and47-table schema inventory match. Historical evidence
  and all immutable receipts remain unchanged; new task evidence uses separate scento_* filenames.

Machine-readable evidence: [tests](../../../database/evidence/scento_test_results.json),
[schema](../../../database/evidence/scento_schema_inventory.json),
[execution](../../../database/evidence/scento_execution_summary.json).
Commands: `python -m unittest discover -s database/tests -v` (equivalent unittest discovery/API runner);
`python database/validate_docs.py --task IMP-P1-02`. Full stdout remains ignored/local. No passing
label is inferred for API/UI/bytes/restore/cloud/production.

## Independent research and tooling

D1 preserves220 seed rows, adds6 label candidates (226 total),40 new observations/30 opened first-party
pages for existing candidates; inherited27 presence rows are not reverified. Crosswalk93 literal,
4 alias candidates,63 unmatched houses;21 identity conflicts,0 approved semantic merges. D5 seven note
license candidates cover7/46 research labels;5 blocked bottle leads,0 bytes/display approvals. D7 five
publisher inspiration leads,0 usable independent pairs; restrictive publisher terms block content reuse.
These are external review queues, not canonical brand/media/Dupe facts.

Four provided external utilities hardened;22/22 offline tests pass. Atomic single LATEST ZIP verifies
exact manifest member/hash/size agreement; historical03_CANONICAL_DATA is preserved. D1 QA16 checks,
D5/D7 QA18 persisted plus57 write assertions, deterministic D1 builds and independent mapping review
have separate external evidence. Tool/file manifests and D1-D9 metric links remain in the local handoff.

## Remaining limits / next gate

Generated identities and existing immutable DB contracts bound replay; this is not a generic arbitrary
reconciliation service. Fixed mapping hashes are an offline independent-policy gate, not hosted reviewer
authentication. Local Docker/postgres operator is explicitly trusted; API/JWT/cookie/cache/export
authorization is not implemented. Whole-import deadline/capacity/independent DB-object restore remain
IMP-P1-04 work. Original row callbacks/global final scans and serialized writers remain enabled.

Independent exact-source review and publication checkpoint are recorded in the task/review report.
Owner reviews the Draft PR; then dependent tasks may start under their own gates.44 holds, unverified
regional rights, per-asset permission, PR4 matching gate and separate cloud/budget approvals remain.
PRODUCTION_MUTATION=NO. No new migration, scraper, paid AI job, cloud resource or production deployment.
