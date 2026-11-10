---
id: DPT-DEL-004
project: DoomParfum By TK
type: implementation_plan
status: proposed
owner: project
updated: 2026-11-10
tags: [doomparfum, planning, pilot]
source_of_truth: "../../README.md"
---

# P1 Pilot Implementation Plan — After Human Planning Merge

OWNER-APPROVED BOUNDED LOCAL SCOPE; NOT AUTHORIZED TO START IN THIS DOCUMENTATION ROUND OR BEFORE HUMAN PLANNING MERGE. Each future task must verify the owner's merge event and approved
plan SHA, branch from current main, open its own Draft Implementation PR and update Obsidian evidence.
All criteria below are proposed tests, NOT RUN results. No Dockerfile, Compose, SQL, migration or ETL
script is included in the planning PR.

## Task map and dependencies

| Task / responsible role | Scope / requirements | Dependency | Acceptance evidence |
|---|---|---|---|
| IMP-P1-01 / implementation + owner review | Disposable local PostgreSQL, reviewed migrations; R01–R03, R21 | Owner merged plan; approves identity/provenance design | Empty DB → schema → downgrade/recreate rehearsal; named PK/FK/CHECK/unique constraints and subtype triggers tested |
| IMP-P1-02 / data implementation + owner review | Sample Python ETL, source adapters/staging/validation; R19–R22, R06 | 01; approved source snapshot/rights | Idempotent sample import, unknowns/conflicts preserved; no network to restricted hosts |
| IMP-P1-03 / implementation + rights review | Image metadata and bounded acquisition; R13, R21 | 01–02; per-image permissions | MIME/dimension/size/hash/attribution/derivative tests; no rendering when rights unknown |
| IMP-P1-04 / implementation + independent review | Size benchmark and database/object backup/restore; R21, foundation for R10/R26/R28/R29 | 01–03 | Measured row/heap/index/TOAST/object sizes; independent restore plus negative controls |
| IMP-P1-05 / owner + implementation | Supabase readiness decision, optional separately authorized staging migration | 04 plus separately approved cloud/provider/resource scope (currently DEFERRED) | Rechecked quotas, version/extension/region/auth/RLS/pooling compatibility, budget and successful rehearsal; no implied production approval |

Web catalogue screens, matching algorithms, cart UI and ownership actions remain later TSK-104+,
TSK-201+ and TSK-301+ tasks, not pilot scope. The schema reserves their relationships without building them.

## Local environment and bounded sample

PROPOSED: pin a stable PostgreSQL major/container digest compatible with the eventual host; bind only
loopback, use a disposable named volume and separate secrets outside Git. Choose exact version after
host compatibility review, not an unpinned latest image. No provider SDK is required for core data tests.

Start with 12 licensed Scento rows: `dior-jadore`, `dior-hypnotic-poison`, `dior-poison`,
`parfums-de-marly-layton`, `parfums-de-marly-delina`, `lattafa-khamrah`, `lattafa-yara`, `lattafa-asad`,
`amouage-reflection-man`, `lattafa-fakhar-black`, `balmain-bleu-infini`, `balmain-bleu-infini-toilette`,
plus their referenced houses and reviewed note vocabulary. Retain attribution and revision/hash evidence.
Do not import the official-site product content observed during research without a use grant.
Thai/Indonesian import acceptance remains pending until owner supplies owned/licensed samples or grants
are verified; target at least two real profiles per regional group when available, never fabricated rows.
Synthetic malformed records may be used in isolated future tests, clearly labeled and excluded from
product data. They do not count as regional coverage evidence.

## Proposed test matrix and measurable expectations

| Area | Positive control | Negative control / expected result |
|---|---|---|
| Import accounting | Every input becomes promoted/review/quarantined with a reason; totals equal input | Malformed JSON/wrong list or year type → quarantined, no partial canonical write |
| Provenance | Every promoted imported field traces to reviewed selection/source/rights | Unknown/expired/restricted grant → no acquisition/promotion/display for that use |
| Missing | Flat-only records retain general notes; nullable country/concentration/year round-trip | Null must not become 0, empty canonical country, invented note or EDP |
| Duplicate | Same batch run twice: zero additional canonical/source versions/joins | Balmain EDP/EDT remain two profiles; fuzzy match never merges automatically |
| Conflict | Competing same-field claims survive and unresolved review queue is visible | Newer source/majority/family mapping cannot silently overwrite or union lists |
| Alias | Known reviewed aliases resolve; accents preserved | Ambiguous alias returns candidates, no forced synthetic/natural equivalence |
| FK/type | Source/entity/field references validate | Wrong entity kind, unrelated conflict member or cross-source rights ID rejected |
| Transaction | Approved promotion updates selection/materialized joins/audit together | Failure mid-promotion leaves no partial catalogue; rollback retains original claims |
| Images | Approved image validates bytes and export manifest | Wrong MIME, oversized input, corrupt hash, cycle, SSRF redirect/private address, absent credit → reject |
| Tenant isolation | Owner can read own private sources/cart/purchases/images | Other user and anonymous reads/writes blocked, including through joins/signed URL issuance |
| Personal invariants | Two purchases of same perfume remain two events; gift can lack purchase | Wrong-owner source/variant, price without currency, volume ≤0 rejected; cart deletion/bottle finish preserves purchases |
| Matching boundary | Ratings/ranks stored separately; insufficient evidence has null score | No fabricated pairwise percentage or score from stars |
| Restore | DB to fresh PostgreSQL plus bytes to separate object target preserves counts/FKs/rights | DB-only restore with absent object or corrupt manifest fails; missing role/RLS fails private access checks |

Use focused unit/integration tests and meaningful DB-enforced negative controls. A separate independent
reviewer examines exact implementation HEAD and actual evidence before each owner merge. No tests in
this planning PR claim these behaviors are implemented.

## Size benchmark protocol

After sample correctness, use approved licensed real rows up to the pinned 1,479-row snapshot for a local
capacity rehearsal. Measure empty schema, imported canonical data, claim history, staging, indexes,
TOAST and complete database using PostgreSQL size functions. Compare before/after vacuum/analyze and
record row counts and query plans. Record wall time, machine/container versions, input hashes and
bytes per perfume under the actual association distribution. Any larger synthetic stress workload is
clearly labeled and excluded from real-data coverage totals.

Images: record actual originals/derivatives/counts/bytes and measured request/egress traces; do not use
JSONL size as DB size or an assumed image size as measured cost. Proposed host criteria: selected free
allowances remain below 70% for the measured projected workload and retention; 85% import stop threshold.
If not, reduce retention, revisit indexes/storage choice or request an owner-approved paid budget.

## Supabase migration readiness and exit criteria

- [ ] Planning PR is owner-merged; accepted decisions and exact plan SHA recorded.
- [ ] Rights, regional sample gaps and image grants resolved for the specific import scope; denied sources excluded.
- [ ] Reviewed migrations reproduce schema; all positive/negative tests above have actual evidence.
- [ ] Measured size/egress/request budget fits chosen tier with headroom; quotas rechecked.
- [ ] PostgreSQL major, extensions, collation, migration role, transaction pooling and connection policy verified.
- [ ] Private-first auth, RLS/private schemas and service-role separation proven; no secrets in browser/Git.
- [ ] Independent DB + object export/restore passes; proposed RPO ≤24h, pilot RTO ≤2h measured or revised by owner.
- [ ] Object/provider adapters and auth-subject mapping documented for Docker exit; no Supabase-only domain FK.
- [ ] Owner approves provider, region, budget, backup retention and any staging/production operation separately.

Completion of local tests is not permission to deploy. Hosting alternatives and detailed recovery plan:
[[P1_Storage_Hosting_and_Recovery]]. Stop on missing approval, rights ambiguity, data loss or failed restore.


## Post-review constraint and access tests — specifications only, NOT RUN

Use synthetic authorization/invalid-grant fixtures only as clearly labeled isolated test inputs; they do
not count as product facts, real third-party permission or regional coverage. Exercise actual non-owner
runtime roles AND API/storage paths; testing only an admin/service role is insufficient.

| ID | Required setup / positive result | Negative control / exact expected behavior |
|---|---|---|
| OBS-01 | One captured Khamrah-shaped document, same entity/field, structured and prose locators → two observation IDs | Former record/field uniqueness must not reject/drop the second; both can join one conflict |
| OBS-02 | Two occurrences within one locator use different claim_key; agreeing claims at different locators also survive | Replaying same full identity adds zero rows; changed value/status under it fails/quarantines without overwrite |
| OBS-03 | Select the prose observation UUID explicitly and retain structured member | Empty locator/key, wrong field/entity/kind or cross-scope selection/member is rejected by NOT NULL/nonempty/FK checks |
| OBS-04 | Resolve conflict using one of its members in one transaction | Non-member same-field resolution, removal of resolved member, active conflict with fewer than two claims fail at commit; no silent resolved status on selection change |
| ACL-01 | Owner A private source/capture/claim/image targets a public perfume; A sees overlay | User B and anonymous see public facts only; no private locator/count/conflict flag/rating/thumbnail via detail, joins, search, compare, export or cache |
| ACL-02 | Public selection uses public observation; A overlay uses A private observation | Private/shared observation cannot populate public selection/columns/joins or public matching input; different principal/scope cache replay denied |
| ACL-03 | Scope A source→record→observation→batch/validation lineage consistent | Scope B source/rights/record IDs, spoofed owner/scope header or in-place scope/owner widening rejected; no source URL/key/hash global dedup leak |
| ACL-04 | Shared owner grants reader/editor explicitly; members see only that scope | Non-member/revoked user denied; reader mutation, self-enrollment, unrelated group reference or shared membership exposing purchases/inventory rejected; shared mode stays disabled until approved |
| ACL-05 | Private listing/price/cart/purchase/bottle joins agree on scope/user/perfume | Wrong-owner scope, record or listing and other perfume's variant rejected; deletion/finished bottle preserves purchase history |
| ACL-06 | RLS with non-owner/no-BYPASSRLS role; WITH CHECK blocks new-row spoofing; approved public metadata readable | No-policy/default-deny, public raw staging/evidence secrets, unauthorized invoker/definer view/RPC/worker/export paths tested; admin-only PASS cannot satisfy this criterion |
| ACL-07 | Trusted writes authorize referenced IDs before SQL; uniform error response | FK/unique failure cannot reveal existence of B private row/object; direct SQL/table writes and service-role endpoint unavailable to untrusted client |
| IMG-01 | Selected binding matches exact scope/image/source/capture/assessment and verified evidence locator | Unrelated source assessment fails composite FK; different asset or different capture with same source fails binding FK |
| IMG-02 | Metadata-only image may have unknown assessment without bytes | acquired/validated state with null permission, missing technical metadata or unknown/denied acquire use fails; nullable FK must not bypass state gate |
| IMG-03 | Original and derivative each have own permission; parent allows transform and output obligations match | Wrong or no-longer-selected parent permission, parent denies/unknown transform, incompatible output license or missing credit/change notice blocks derivative; source/capture/scope mismatch rejected |
| IMG-04 | Asset/capture locator and known content hash match applicable permission proof | Selected binding missing/mismatched hash in acquired state, or reusing a permission by swapping locator, source record or binary hash is rejected; shared publisher name alone never suffices |
| IMG-05 | Authorize image use at fetch/transform/display/restore; active selected grant and ancestors | Expired/revoked assessment, child/ancestor grant or membership disables new proxy requests; cycles fail; cache invalidated; old private URL replay/direct bucket read denied |
| IMG-06 | Public image link references public approved asset; private link stays private about a public perfume | Public join to private/shared image rejected; no private bytes/EXIF/permission evidence in public manifests/backups/Git |
| REC-01 | Export/restore retains scopes/members, locator identities, selected/member claims, permission tuples and derivative chain | Restored FK/rights/scope mismatch prevents serving/promoting; count parity alone cannot pass; private exports never published |

All row CHECK/FK/unique and deferred-trigger contracts are specified in [[Data_Dictionary_Draft]].
Document-only review cannot prove any of these runtime behaviors. IMP-P1-01..04 must attach exact failing/
passing evidence and independent review before readiness. No SQL/test code or environment is created here.


## S3 recorded Owner approval and remaining gate

OD-01..06 approved for the bounded international licensed-data LOCAL pilot; [[P1_Data_Foundation_Plan]]
and [[Decision_Log]] contain exact scope/deferred/blocked decisions. Local PostgreSQL, model/claims/
conflict/access-scope primitives, image metadata/rights design and local DB/object backup/restore tests
are approved targets for a later implementation PR after verified owner merge. SQL/RLS/18 review test
specifications still require actual evidence; none ran. This documentation round creates no code/DB/SQL.

Permanent cloud hosting/provider/storage and external backup provisioning remain DEFERRED. Final
retention/RPO/RTO are not accepted; prior 7-daily/4-weekly/24h/2h suggestions remain proposals only.
OD-04 does not grant new rights to image bytes; use only permitted/owned local test objects or clearly
labeled fixtures for recovery/negative tests. Regional imports remain blocked until rights AND samples
are verified, without blocking the approved narrower international pilot. IMP-P1-05 cannot provision
anything until a separate cloud scope approval. Product-facing sharing and broad application/CI scope
are not approved by the local access-model target decision.
