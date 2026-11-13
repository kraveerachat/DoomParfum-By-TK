---
id: DPT-DATA-003-EVIDENCE
project: DoomParfum By TK
type: test_evidence
status: independent-review-complete-owner-review-pending
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, evidence, coverage, rights]
source_of_truth: "../../../README.md"
---

# DPT-DATA-003 — actual evidence

Base/source: `58ceafe72129b70f0333c7c4f2c6f38dba855272`; pinned Scento revision `086769ecf1add770ea6646bd4d88d39f0e7cddeb`. Source attribution: Scento — https://www.scento.com/perfume-database. Existing pinned dataset license: CC BY 4.0. Change notice: aggregate coverage and unapproved review projections only; original observations/arrays and rights remain unchanged. This does not license unrelated images or sources.

## Read-only database audit

Existing guarded disposable task container, loopback 127.0.0.1:55431, database `dpt_scento_pilot`. Used existing main `database/local.py` guard/SQL harness plus existing root recovery fingerprint and common-root exclusive `RunLease` coordination helpers. The helper checkout is the historical PR #8 tree at `3b01c8395d8ce28f426643f104da16090f11844d`; it is audit coordination only, not a new application dependency or PR #8 merge. No reset, migration, binding creation, data/security/role write or production access.

V2 was one repeatable-read READ ONLY aggregate query at 2026-11-13 08:09:30.147499 UTC. V3 supplement was one repeatable-read READ ONLY aggregate query at 08:17:53.752609 UTC. Bounded per-query statement timeouts: 30 seconds and 20 seconds respectively. Fingerprints before/after cover all 49 table inventories plus security and application-role manifests; equality PASS for both successful audit runs. No raw rows, payload values, client-side catalogue export or app admin-fetch/filter was used. SQL is audit-only and remains ignored locally, outside tracked migrations/runtime.

Definitions: populated canonical scalar is non-NULL/nonblank, relation is EXISTS on its scoped association; missing is denominator minus populated. Held/unapproved derive from current review state, not missingness. Selected present requires same entity/scope/kind/path plus a present selected observation. Active local rights requires exact source/assessment binding, checked-at not future, no revocation and no expiry, with storage/display/automation allowed. Query bytes retain the complete predicates; no public interpretation should broaden their use. Raw shape uses DISTINCT source_record_id captures and exact source_file. Raw scalar shape is nonblank source string only. Worldwide brand/market/edition universe is not known.

## Preserved instrumentation failures and corrections

- V1 completed with unchanged fingerprints, but its house-source prefix predicate was incorrect and returned an invalid country-evidence zero. Frozen V1 is retained; V2 corrected the predicate to `raw_payload->>'source_file'='houses.csv'`, yielding denominator160, populated158, missing2 and17distinct origin claims.
- A PowerShell inline quoting attempt failed before Python/DB execution. No database evidence resulted.
- V2 mislabeled the family selected contract by querying `families`; V3 uses actual `family` and separately checks `families.primary` / `families.secondary`. Contract exists; all selected counts0. Original V2 is retained; V3 is the final authoritative combined interpretation.
- First V3 SQL failed42601 at `GROUP BY1,2`; failed query/script/log were retained. Only audit SQL spacing was corrected to `GROUP BY 1,2`, then the supplement and integrity comparisons passed. No runtime fix or validation relaxation was made.
- Offline matrix preparation initially used a nonexistent audit_004 path; failed before output. Corrected to the existing audit_004_replay. No frozen baseline was modified.

These are audit instrumentation errors, not reproductions or resolutions of PR #8's historical 23514 future-review-timestamp failure. That failure remains unexplained and PR #8 remains blocked.

## Offline checks

`python .local/postmerge-D/prepare_readiness.py`: 34/34 PASS. Seven frozen 003 artifact hashes, eight 003/004_replay byte comparisons, nine preserved research input hashes and all six pinned source artifacts verified. Recomputed43 sidecars/exclusion/15 media/5 pairs exactly match frozen outputs; exact44 hold membership, original source arrays,44 repeat groups/45 extras,64/64/64/43 matrix dimensions, no accepted membership and deterministic double-build bytes verified. Network calls0, DB calls0 and canonical/rights/policy writes0 in this offline phase.

Detailed matrices remain ignored `.local/postmerge-D/OFFLINE_READINESS_MATRICES.json`; counts/check manifest `.local/postmerge-D/OFFLINE_READINESS_CHECKS.json`. Public-safe aggregate `.local/postmerge-D/G1_PUBLIC_COVERAGE_SUMMARY.json` strips table fingerprints/private rows. Frozen historical evidence and all failures remain intact.

## Exact artifact hashes

| Ignored local artifact | SHA-256 |
|---|---|
| coverage_query_v2.sql.txt | `8b36ea19bc10f9bb7784da2635cbaf1f68dcf21877d52ebd44be68358865bf50` |
| coverage_supplement_v3.sql.txt | `b62c466843d6c01926838cc800b132e905c542836c8d4c25803d0067b3c7ce97` |
| FRESH_CATALOGUE_COVERAGE_V3.json | `5ea6972f72018412d5cbb318db8874931763e3d471694e318c04b1e10834e33a` |
| G1_PUBLIC_COVERAGE_SUMMARY.json | `961a2a23ccf6379209fb037190f614eb250c483741cc91b13ef213db79a38b19` |
| OFFLINE_READINESS_CHECKS.json | `4a7e35a6b5c940d27e3f346eb3e771911ac305987ac264f11635f3c3b842d59c` |
| OFFLINE_READINESS_MATRICES.json | `443b7212817b405deda2b75cbbf11f99ef985bca26fba7c4e0f43fc4804b8193` |
| prepare_readiness.py | `4659f7cbe71336e01b8e53e74a6b47a95b113ae5b6802495eee174e6b16b8a62` |

## Limits / checks not run

Independent acceptance review is PENDING. No new application-session, RLS integration, SQL/ETL, replay, backup/restore, image acquisition/MIME/byte validation, network-source rights refresh, real-data ranking or production tests were run by this task; no such PASS is claimed. Source/index projections are not production coverage or grants. Full review/publication must use the coordinator's final exact-head and handoff verification. No immutable final receipt created.

## Independent coordinator review — 2026-11-13

Reviewer /root is independent of implementer /root/postmerge_d_evidence_coverage. Read all three
dedicated documents and compared the public aggregate/hold/transform claims to retained source and
offline manifests. Independently reran prepare_readiness.py:34/34PASS, deterministic matrices
SHA256443b7212817b405deda2b75cbbf11f99ef985bca26fba7c4e0f43fc4804b8193 unchanged;0DB/network calls.
Reviewed main matrix SHA25696ddb483fa98cda39ecc61fcd6947af672fd6e788b960530189bb10d3e5dde8f. Counts distinguish canonical/raw/held/selected/local rights/app
availability;43projections do not release44holds,Khamrah remains separate,64mixed-unit entries do
not imply64perfumes, and0conflict rows do not resolve external source conflict. No blocking finding
for this docs-only evidence scope. G's independent reviewer separately checks query/count definitions.
Runtime,appRLS,source acquisition,media and policy acceptance NOT RUN/NOT GRANTED. Final document
validation and source checkpoint follow; receipt records planning/evidence readiness only.

## Post-receipt metadata correction — 2026-11-13

The evidence frontmatter now records the already completed independent review and pending Human
Owner review. Earlier pending statements are authoring history, superseded by the independent
review section. This header correction changes no proposal,reviewed specification,source right,
test result or immutable receipt. Exact new HEAD is in the coordinator publication registry.
