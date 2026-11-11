---
id: IMP-P1-03-EVIDENCE
project: DoomParfum By TK
type: implementation_evidence
status: ready-for-human-review
owner: human-owner
updated: 2026-11-12
tags: [doomparfum, images, rights, evidence]
source_of_truth: ../../../README.md
---

# IMP-P1-03 — Local byte and rights evidence

Task [[IMP-P1-03_Local_Image_Rights]], owner-approved P1/OD-04; base55d39cd619fa6c1ae70521720aa734d632a2083d.
Source checkpoint `ad27cc5c6f54c85703bd2d324a3a54b2401bed21` on
`codex/imp-p1-03-image-rights`; [Draft PR6](https://github.com/kraveerachat/DoomParfum-By-TK/pull/6).
No new schema, provider, acquisition permission or owner decision.

## Result and exact checks

| Check | Observed result | Evidence |
|---|---|---|
| New offline checks |20/20 pass,0fail/error/skip,0.015s, exit0 | `database/evidence/image_offline_results.json` |
| Same offline source, second interpreter |20/20 pass,0.012s | Python3.11.9 explicit executable; tool output |
| Focused combined suite |44/44 pass,0fail/error/skip,67.922s, exit0 | `database/evidence/image_test_results.json` |
| Composition |20offline +11new live +13existing image SQL contracts | Exact test IDs in JSON |
| Source freshness |14/14 recorded source hashes match current bytes | Resumed readback,2026-11-12 Bangkok |
| Existing migrations/harness/importer/receipts | No diff against base | Scoped Git diff inspection |
| Full regression |129/129 pass,0fail/error/skip,164.922s, exit0 | `database/evidence/image_full_regression_results.json` |
| Independent review | No blocking finding in declared scope;20offline tests independently rerun | Parent review SHA256 below |

Primary interpreter `C:\Program Files\Python312\python.exe`, Python3.12.10.
Portability interpreter `C:\Program Files\Python311\python.exe`, Python3.11.9.
Existing Docker28.3.2, guarded local PostgreSQL image
`postgres@sha256:f1c3376c26f2609ab9f29f71f824103fe2fcd8ee0346485cb6122a4f93df6f94`.
Only disposable `dpt_schema_test` was recreated. No persistent catalogue or
capacity/migration probe was modified.67.922s is one focused test-run duration,
not a performance or capacity claim. Parent coordinated exclusive DB access.

The subsequent separately granted full regression used the existing suite's
disposable `dpt_schema_test`, `dpt_migration_probe` and `dpt_scento_test` sequentially.
It preserved persistent Scento pilot/foundation. Existing98tests plus31new =129;
all passed in164.922s under Python3.11.9. This is regression timing, not controlled
capacity evidence. To locate existing external fixtures from an isolated worktree,
the ignored runner temporarily patches `local.ROOT` only inside the two original
FoundationTests package-reading methods, restores it immediately, and points
`test_scento_etl.SOURCE` at the verified pinned folder. All assertions, migrations,
source files and other worktree-local paths are unchanged; no symlinks or copies.
Exact workaround, test IDs and source hashes are recorded in the full-suite JSON.

## Independent exact-source review

Primary coordinator independently reviewed four files at exact sourcead27cc5,
reran20offline tests successfully under Python3.11.9 and found no blocking issue
in the declared static PNG/private local metadata scope. Reviewer made0DB calls
and only inspected the recorded44-test evidence. External report SHA256
`7553e49a6da7234a8040c7b587c3d3e197250b11a02db7bec8dac5565b60d91d`;
four recorded source/document hashes match the tested, current source. No source
change after review. Limits remain explicit; technical checks grant no new rights.

Documentation checks verify task/evidence/usage links, frontmatter, source hashes,
unchanged original protected files and0common-secret-pattern candidates. Source
review readiness and passing tests do not imply owner merge or production readiness.

## What is implemented

Strict in-memory PNG structure validation accepts only static8-bit RGB/RGBA,
non-interlaced IHDR/IDAT/IEND. Tests measure real synthetic bytes and SHA-256,
verify CRC/zlib completion, correct row length/filter codes, and reject corrupt
streams, wrong signatures, oversized chunks/dimensions/pixels/decoded output,
truncation, trailing/concatenated data, EXIF/text/ICC/APNG and unsupported formats.
Default bounds:5MiB input,4096each dimension,4million pixels,20MiB decoded rows,
1024chunks. No global decoder setting/dependency installed.

The local registered-asset facade invokes the current SQL authorization before
the trusted synthetic content reader, compares MIME/bytes/dimensions/hash and
reauthorizes plus compares full registered binding afterward. New live checks
exercise all four operations, exact byte mismatch, declared-dimension mismatch,
private owner versus Bob/guest/missing uniform denial, selected-grant revocation,
expiry during read, revocation during read, binding change, revoked ancestors,
metadata-only unknown-source denial, and schema-supported but unsupported MIME.
No successful result advances DB state or serves/stores bytes.

Original SQL tests additionally exercise exact source/capture/assessment/asset
binding, unknown acquire use, derivative parent/output license/credit/change
obligations, capture/hash/locator integrity, revocation/elapsed expiry, public-to-
private link rejection, null MIME, cycles, parent selected-permission changes,
same-source wrong-capture permission, and expired private asset isolation.
SQL remains the authority; Python does not duplicate legal permission logic.

## Limits and negative claims

All PNG fixtures are agent-authored SYNTHETIC pixel buffers, all DB grants are
explicit synthetic test permissions. Real acquired/catalogue images0; actual new
source/asset permission grants0. Neither synthetic bytes nor metadata count as
perfume/note image coverage. Existing Scento fixtures/pilot are preserved.

The callback is a trusted local integration hook with pre-existing owned/permitted
bytes; there is no HTTP/filesystem downloader or upload endpoint. Returned-buffer
limits do not replace bounded reads in a future acquisition adapter. No actual
photo decoding/rendering, thumbnailing, metadata stripping, JPEG/WebP/AVIF/SVG/GIF
support, HTTP SSRF/redirect/proxy/cache/signed URL/provider, independent object
restore, public API/UI/build/E2E/cloud or production behavior was tested.
Reauthorization is point-in-time: a technical result is not a cached permission
or serving token; every subsequent operation needs current authorization.

## Tools, failures and rollback

Existing PowerShell/Git/rg/Python/Docker/PostgreSQL and connected GitHub MCP;
security-review skill used for input/authorization/privacy checks. No install,
account authentication/global config/paid service or external image request.
Initial unprivileged Docker inspect failed before SQL; approved scoped escalation
ran the same guarded harness. Quota interruption did not erase the completed
verifier: existing session/result read back instead of rerunning it. No validation
bypass or altered time/rights policy. Detailed logs stay ignored under `.local`.

Rollback is removal/revert of this additive module/runner/tests/docs after normal
review, with no migration/down-migration, real-data deletion or storage cleanup.
Disposable synthetic test DB may be recreated only inside its existing bounded
harness and coordination window. Human Owner alone reviews/merges PR6.
