---
id: DPT-DOC-003-WAVE0
project: DoomParfum By TK
type: test_evidence
status: review-in-progress
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, catalogue, evidence, gates]
source_of_truth: "../../../README.md"
---

# New-main Wave0 evidence — actual bounded execution

Base8c6a8376680c7a10cc3eb4b5cf80afe4376a9282; inputhash
b459c07e94ff6c68682165c3a166c7965a31b36e39e6a231118c304c1e402b23.
Private logs/fingerprints remain ignored outside public Git/ZIP; only aggregate reports are published.

| Command/artifact | Result | Scope/qualification |
|---|---|---|
| python .local/post1821/run_baseline.py | NEW PASS55methods;0fail/error/skip;0DBcalls;0.05639060000248719s | math24,research17,adapteroffline14; current-main cwd/imports verified |
| python .local/post1821/audit_wave0.py | NEW PASS49before/after/prior fingerprints equal | sole-leased aggregate READ ONLY queries; no mutation or raw row export |
| base_audit.sql.txt | d2a5cde6b7844e45a958f8503c733f417cbc7d95c0f0c4285497b13612754bd2 | old20field matrix and security/inventory aggregates |
| supplement_audit.sql.txt | b62c466843d6c01926838cc800b132e905c542836c8d4c25803d0067b3c7ce97 | raw/selected/note metrics |
| completeness_audit.sql.txt | c8fb090e69c96b50a327a9a19d7bcafb997389625d29d9d8cd8c1c60e031ae44 | all raw fields/selected paths,notes,identity collision predicate |
| GitHub connector GET main,open PRs,18/19/20/21/8 | verified new main,4Owner merges,PR8dirty/Draft | no metadata or merge mutation |

Python3.11.9; Docker28.3.2; existing postgres image pin
postgres@sha256:f1c3376c26f2609ab9f29f71f824103fe2fcd8ee0346485cb6122a4f93df6f94.
Only guarded task container127.0.0.1:55431 used; stopped afterward,volume retained,lease released.
No host restart/clock/daemon reconfiguration. Existing PR8RunLease/fingerprint helper was used
strictly for local coordination/inspection; current-main local.py guard validated target. No
unmerged product behavior was introduced into main or any feature task.

Preserved failure: initial PowerShell inline source-copy command had a Python quoting SyntaxError
before file/data mutation; replaced by an inspected standalone helper. It did not execute a partial
baseline or alter data. Earlier failures remain in their original dated evidence and receipts.

Full DB/live/replay/recovery suites are HISTORICAL ONLY/NOT RERUN. Future full A/B1,closure,
normalization,API/UI,source/media ingestion and service tests are NOT RUN.55unit methods,49table
fingerprint comparisons and independent static checks use different units and are never summed.
Common-pattern secret scanning cannot prove absence of every secret; no dedicated scanner or
external-link/Mermaid rendering claim. Final independent review and package results follow separately.
