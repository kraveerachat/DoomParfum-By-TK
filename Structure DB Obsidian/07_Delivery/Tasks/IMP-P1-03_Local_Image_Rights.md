---
id: IMP-P1-03
project: DoomParfum By TK
type: implementation_task
status: ready-for-human-review
owner: human-owner
updated: 2026-11-12
tags: [doomparfum, images, rights, local]
source_of_truth: ../../../README.md
---

# IMP-P1-03 — Local image metadata and rights validation

Owner authorized bounded implementation after PR5 merge. Branch
`codex/imp-p1-03-image-rights`; START_SHA/base main
`55d39cd619fa6c1ae70521720aa734d632a2083d`.
Approved scope: merged P1 plan/OD-04 and [[P1_Pilot_Implementation_Plan]], R13/R21,
with the current owner restriction to portable local metadata/rights validation.
PR4 matching remains a separate Draft. Human Owner alone merges.

## Scope and expected evidence

1. Inspect actual SQL image contracts and identify the remaining delta.
2. Implement an offline, dependency-free strict static PNG validator and private local
   validation facade that reuses database operation authorization before reading bytes.
3. Test type/signature, CRC/compression, dimensions, byte/pixel/decompression limits,
   exact metadata/hash, source/capture/grant/ancestry/expiry/revocation and privacy.
4. Record focused and coordinated regression evidence; obtain independent exact-source
   review before the single final receipt and Draft PR publication.

Existing migrations already enforce exact scope/source/capture/assessment/permission
tuples, hash/locator, lineage, current per-use grants and RLS. This task will not
duplicate those rules or change migrations001–008.

Byte scope is only agent-authored, clearly SYNTHETIC in-memory PNG fixtures. No
third-party image acquisition, HTTP fetch, rendering/decoder service, provider/cloud,
filesystem image loader, product image association, hosted API/UI or deployment.
Unsupported PNG features, JPEG/WebP/AVIF/SVG/GIF fail closed; schema MIME vocabulary
does not imply this local validator supports all formats. No tool install needed.

## Do-not-touch surfaces and coordination

Preserve all migrations, prior receipts, Scento fixtures/pilot, owner decisions and
other worktrees. Latest coordinator allocation supersedes the initial target:
database tests may use ONLY disposable `dpt_schema_test`, with
explicit target arguments and the existing local container guards. Parent owns
`dpt_migration_probe` and `dpt_scento_test` capacity work plus coordinated full regression. No timed/SQL tests while the
parent's controlled capacity measurements run. External evidence, if required, is
restricted to the delegated `post_PR5/image_rights` handoff output; parent owns
shared progress and ZIP packaging.

## Preflight and status

Clean branch/head and existing Docker28.3.2 observed. Default `py -3` is
Python3.12.10; Pillow is NOT INSTALLED in that interpreter. The parent uses a
different Python3.11.9 interpreter; exact executables will be recorded in evidence.
`03_Data/P1_Pilot_Implementation_Plan.md`: NOT FOUND at that assumed path;
actual canonical `07_Delivery/P1_Pilot_Implementation_Plan.md` located/read.
Historical Project_Status/receipt still say PR5 Draft; owner merge/base above
supersedes that snapshot without rewriting its immutable receipt.

`Agent_Tool_Registry.md`: NOT FOUND in this checkout. No tool installation or
configuration change is performed; existing-tool usage is recorded here.

Source implemented in `database/image_validation.py`, with focused verifier,
usage contract and tests. `py -3 database/verify_images.py`:20/20 offline tests
passed,0fail/error/skip,0.015s, exit0; `git diff --check` exit0. Sanitized source
hashes/results: `database/evidence/image_offline_results.json`. Actual executable
`C:\Program Files\Python312\python.exe`, Python3.12.10. No Docker/SQL calls in
this implementation session yet. DB integration, full regression, independent
review and publication remain NOT RUN/pending. Parent's controlled timing window
is active; next action is exact-source static review, then granted DB window.

## Resumed verified checkpoint — 2026-11-12 Bangkok

Source checkpoint `ad27cc5c6f54c85703bd2d324a3a54b2401bed21` pushed normally;
[PR #6](https://github.com/kraveerachat/DoomParfum-By-TK/pull/6) created/read back
OPEN/DRAFT, merged=false. No duplicate PR or receipt. Historical pending lines
above describe pre-DB state, superseded by this entry.

The existing verifier session4613 completed at2026-11-11T16:21:44.751506Z:
`py -3 database/verify_images.py --include-db`,44/44 passed,0failure/error/skip,
67.922s, exit0. This comprises20offline +11new live +13original SQL contracts.
Actual output `database/evidence/image_test_results.json` hashes14source files;
fresh readback matches all14. No unnecessary rerun after quota interruption.
The initial sandbox attempt failed at Docker inspect before SQL; scoped local
escalation then ran the existing container guards successfully. Test log remains
ignored at `.local/image-rights/db_test_output.log`; no credentials printed.

Live tests used only disposable `dpt_schema_test`; migrations001–008 replayed
unchanged, Scento pilot/foundation/capacity probe untouched. The coordinator's
exclusive DB window is now returned; no further SQL calls while controlled
benchmarks run. This67.922s is test-run wall time, not a capacity measurement.
Additional unchanged-source offline portability check under actual
`C:\Program Files\Python311\python.exe`, Python3.11.9:20/20 passed0.012s.

Exact behavior and limits: [[IMP-P1-03_Local_Image_Evidence]]. Full regression is
coordinator-owned/pending, independent review pending, final receipt NOT CREATED.
Third-party byte acquisition/HTTP/storage/provider/cloud/deployment remain blocked
or out of scope. No real image permissions/assets established. Next action:
independent review of exact source checkpoint and focused evidence; coordinate
remaining regression before one final receipt/publication closeout.

## Verified review and full regression — 2026-11-12 Bangkok

Parent independently reviewed exact `ad27cc5c6f54c85703bd2d324a3a54b2401bed21`
source and reran20offline tests under Python3.11.9: no blocking finding in the
declared static PNG/trusted local-reader scope. Reviewer inspected actual44-test
evidence without claiming a DB rerun. External review report SHA256
`7553e49a6da7234a8040c7b587c3d3e197250b11a02db7bec8dac5565b60d91d`;
four reviewed source/document hashes still match. No source change after review.

Coordinator then granted the sequential full-suite window. Existing98tests plus
31new tests =129/129 passed,0fail/error/skip,164.922s, exit0 under actualPython3.11.9.
`database/evidence/image_full_regression_results.json` records all test IDs and
exact worktree source hashes. The ignored runner redirected only the two original
sibling-package test methods' `local.ROOT` during those calls, and the Scento test
module's SOURCE to the existing verified external folder. All other source/harness/
migration paths stayed worktree-local. No assertion/source edits, fake fixtures,
filesystem links or data copies. Full suite used existing disposable DB targets
under its normal guards; persistent pilot untouched. DB window returned immediately.

Documentation checker passed3Markdown/2frontmatters, links/fences/source freshness,
no changed original migrations/harness/importer/receipts and0common-secret-pattern
candidates. Rechecked after final metadata/receipt below. Scope is ready for Human
Owner review, not merge/deployment. Final receipt is created once after these checks;
publication commit/head is read back after push rather than invented here.

Single final receipt:
[[2026-11-12_022117_IMP-P1-03_Local_Image_Rights]]. Evidence/documentation checkpoint
`a2d5b5276ec0dfc757eeeec15c9525954cc68a53`; final metadata push/readback follows.
Ready for Human Owner review of bounded local functionality; PR6 remains Draft.
No further DB work is running in this lane. Coordinator owns shared ledger/package.

## Owner-review readiness audit started — 2026-11-12 Bangkok

IN PROGRESS: recheck existing PR head against current main, exact source/evidence and independent
review hashes, immutable receipts, rights boundaries, and documentation. Metadata-only checkpoint;
no DB/Docker/runtime rerun, new acquisition or permission grant. Preserve original final receipt.
Current starting head: e9957e579d6639440ee222c5893122c494120c37.
Expected evidence: reproducible local hash/protected-path/doc audit, live GitHub OPEN/DRAFT/mergeability
readback, same-branch metadata commit/push. Parent owns D1–D9 and consolidated ZIP.

## Verified owner-review readiness checkpoint — 2026-11-12 Bangkok

Current main remains `55d39cd619fa6c1ae70521720aa734d632a2083d`; PR6 starting/publication
head `e9957e579d6639440ee222c5893122c494120c37` is based directly on that main. Live GitHub
readback: OPEN/DRAFT, merged=false, mergeable=true. No base change or mergeability regression.
Source checkpoint `ad27cc5c6f54c85703bd2d324a3a54b2401bed21` remains exact: all14 offline,
14 focused and20 full-regression source hashes match current bytes. Independent review report
SHA256 `7553e49a6da7234a8040c7b587c3d3e197250b11a02db7bec8dac5565b60d91d` and its four
reviewed files still match. Recorded20/44/129 passing results are inspected evidence, not reruns.

Fresh read-only readiness audit:140 file/hash/document assertions,0errors;39 existing base
source/governance/decision/receipt blobs unchanged. Four Markdown files/three frontmatters,
local Markdown/wiki targets, balanced fences, whole-PR common-secret patterns and diff checks
passed. Existing final receipt `2026-11-12_022117_IMP-P1-03_Local_Image_Rights.md` unchanged;
no second receipt. Audit output: external `review_readiness/PR6_READINESS_AUDIT.json` within
the coordinator's `pr8_timestamp_correction` evidence folder.

READY FOR HUMAN OWNER REVIEW of the bounded static PNG/trusted-local-reader scope. Real assets,
new source/per-asset grants and acquisitions remain0. No network/HTTP/SSRF/provider/object restore,
hosted authentication/API/UI or general image-format coverage is claimed. SQL authorization remains
authoritative and subsequent operations must reauthorize. Existing receipt's broader limitations remain.
No code/test/migration/evidence JSON/rights changes in this readiness continuation. Metadata-only
commit/push and resulting head are read back in PR/external audit publication metadata; Human Owner
alone reviews/merges. No DB/Docker execution in this audit; no production mutation.
