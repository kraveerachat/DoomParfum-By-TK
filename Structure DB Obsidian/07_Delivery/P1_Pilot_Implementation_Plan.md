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

NOT AUTHORIZED TO START in this PR. Each future task must verify the owner's merge event and approved
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
| IMP-P1-05 / owner + implementation | Supabase readiness decision, optional separately authorized staging migration | 04 and decisions OD-01..OD-06 | Rechecked quotas, version/extension/region/auth/RLS/pooling compatibility, budget and successful rehearsal; no implied production approval |

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
