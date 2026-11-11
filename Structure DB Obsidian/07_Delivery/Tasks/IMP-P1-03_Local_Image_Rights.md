---
id: IMP-P1-03
project: DoomParfum By TK
type: implementation_task
status: IN PROGRESS
owner: human-owner
updated: 2026-11-11
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
