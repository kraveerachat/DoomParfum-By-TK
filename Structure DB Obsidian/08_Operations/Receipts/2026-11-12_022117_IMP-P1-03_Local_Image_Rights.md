---
id: DPT-RCP-IMP-P1-03
project: DoomParfum By TK
type: immutable_receipt
status: ready-for-human-review
owner: human-owner
updated: 2026-11-12
tags: [doomparfum, receipt, images, rights, local]
source_of_truth: ../../../README.md
---

# IMP-P1-03 — Final immutable local image-validation receipt

Authored2026-11-12 02:21:17 Asia/Bangkok. Exactly one final receipt for this task,
branch and PR. No prior receipt rewritten. This is readiness for Human Owner
review, not merge, image acquisition or deployment.

Branch `codex/imp-p1-03-image-rights`, owner-approved base/main
`55d39cd619fa6c1ae70521720aa734d632a2083d` after PR5 owner merge.
[PR #6](https://github.com/kraveerachat/DoomParfum-By-TK/pull/6) verified OPEN/DRAFT;
Human Owner alone merges. Merged P1 plan/OD-04 and explicit owner scope authorize
this bounded local metadata/rights validation. PR4 matching remains separate.
Reviewed source checkpoint `ad27cc5c6f54c85703bd2d324a3a54b2401bed21`;
focused/full evidence and canonical documentation checkpoint
`a2d5b5276ec0dfc757eeeec15c9525954cc68a53`. Final metadata publication HEAD is
verified after push in PR/external handoff, not invented in its own commit.

## Delivered behavior and evidence

- Dependency-free local PNG structural/CRC/zlib/scanline/dimension/size/hash
  validation. Supported subset: static8-bit RGB/RGBA, non-interlaced, only
  IHDR/IDAT/IEND. Default bounds5MiB input,4096per dimension,4million pixels,
  20MiB decoded scanlines,1024chunks. EXIF/text/ICC/APNG/palette/interlace,
  unsupported formats, corrupt/trailing/concatenated streams fail closed.
- Private local registered-asset facade checks SQL operation rights before the
  trusted content-reader callback, compares exact technical metadata, then
  rechecks authorization and full registered binding. Current source/capture/
  assessment/asset/parent/ancestry/expiry/revocation/RLS rules remain SQL-enforced.
  It neither persists bytes, advances state, serves an image nor caches rights.
- Offline20/20 passed,0fail/error/skip,0.015s under actualPython3.12.10;
  same20 tests passed under actualPython3.11.9,0.012s. Focused44/44 passed,
  0fail/error/skip,67.922s:20offline+11new live+13existing SQL image controls.
- Full regression129/129 passed,0fail/error/skip,164.922s underPython3.11.9,
  existing98tests+31new. All20recorded full-suite source hashes matched at
  closeout. Worktree portability wrapper redirects only two existing package-
  reading methods and Scento test SOURCE to real verified external fixtures;
  no assertion/source edits, fake substitutes, links or data copies. Exact
  workaround/test IDs/source hashes are in image_full_regression_results.json.
- Independent parent review of exactad27cc5 found no blocking issue in declared
  scope; independently reran20offline tests, inspected actual44-test evidence,
  made0DB calls. Review report SHA256
  `7553e49a6da7234a8040c7b587c3d3e197250b11a02db7bec8dac5565b60d91d`;
  four reviewed source/document hashes still match; no later code change.
- Documentation checks passed3Markdown/2frontmatters before receipt and repeat
  afterward; links/fences/hash freshness/protected files/secret-pattern scan and
  Git diff checks passed. Original migrations001–008, harness/importer/Scento
  pilot and all prior receipts preserved. Detailed test logs remain ignored.

Focused tests used only disposable dpt_schema_test. Coordinator separately granted
the full-suite window for its existing disposable targets; no persistent pilot or
foundation reset. Windows returned after each run. Test durations are not controlled
capacity evidence. Initial sandbox Docker inspect failed before SQL; the same
guarded harness succeeded with scoped authorization. Quota interruption recovered
the already-finished44-test session/result without duplicate execution.

## Boundaries and remaining work

All image-byte fixtures are agent-authored SYNTHETIC in-memory pixels; DB grants
are synthetic test permissions. Real acquired/catalogue images0; actual new
source/asset grants0. No third-party byte rights inferred from public URLs or the
Scento dataset. Unknown/restricted rights remain blocked for that operation.

This is not a general image decoder, sanitizer, upload endpoint or acquisition
pipeline. No filesystem/network loader, HTTP/SSRF/redirect/proxy/cache/signed URL,
thumbnailing, JPEG/WebP/AVIF/SVG/GIF support, object-provider/storage, restore,
API/UI/build/E2E/cloud or production result is claimed. The trusted callback must
already hold owned/permitted local bytes; future untrusted readers need their own
bounded reads. Reauthorize every later operation; a result is not a serving token.
Actual media rights, provider choices and dependent image delivery retain their
separate gates. Human Owner reviews/merges PR6; no automatic merge or deployment.

TOOL EXECUTION: Existing PowerShell/Git/rg/Python3.12.10 and3.11.9/Docker28.3.2,
guarded pinned PostgreSQL harness, GitHub MCP PR creation/readback and existing
PyYAML6.0.3 documentation checking; security-review skill applied. No installation,
global/account configuration, paid job, third-party image request or production
mutation. External metadata/evidence stays in delegated post_PR5/image_rights;
coordinator owns shared progress and ZIP. Rollback is an ordinary reviewed revert
of additive files, with no migration/data/object deletion.

Canonical task/evidence: [[IMP-P1-03_Local_Image_Rights]],
[[IMP-P1-03_Local_Image_Evidence]].

## Exact changed-file manifest —11 paths

- database/image_validation.py
- database/verify_images.py
- database/IMAGE_VALIDATION.md
- database/tests/test_image_validation.py
- database/evidence/image_offline_results.json
- database/evidence/image_test_results.json
- database/evidence/image_full_regression_results.json
- database/evidence/image_documentation_checks.json
- Structure DB Obsidian/07_Delivery/Tasks/IMP-P1-03_Local_Image_Rights.md
- Structure DB Obsidian/08_Operations/Test_Evidence/IMP-P1-03_Local_Image_Evidence.md
- Structure DB Obsidian/08_Operations/Receipts/2026-11-12_022117_IMP-P1-03_Local_Image_Rights.md
