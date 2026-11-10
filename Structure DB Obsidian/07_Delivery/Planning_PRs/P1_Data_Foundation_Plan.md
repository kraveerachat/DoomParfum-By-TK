---
id: DPT-PLAN-SPEC-001
project: DoomParfum By TK
type: planning_specification
status: draft
owner: project
updated: 2026-11-10
tags: [doomparfum, planning, p1]
source_of_truth: "../../../README.md"
---

# P1 Data Discovery & Database Foundation Planning PR

## Verified owner merge and implementation event

Planning PR #1 is MERGED at `bffb2fab1918dc5221a6c5da7920168bcae263ca` (2026-11-10 22:12:07 Asia/Bangkok).
Gate P is satisfied for the bounded OD-01..06 local approvals. The original Task Map and historical
planning scope below are retained; they describe that earlier docs-only task. Current implementation
is [[IMP-P1-01_Local_PostgreSQL_Schema]] with actual evidence in [[IMP-P1-01_Implementation_Evidence]].
It has its own branch/Draft PR/human merge gate. No source grant, cloud/storage/provider, regional import,
production recovery policy or web/CI scope is expanded. IMP-P1-02..05 remain NOT STARTED.


TASK: DPT-PLAN-001. Mode: PLANNING_PR_ONLY. Branch: `plan/p1-data-discovery-schema-foundation`.
START_SHA / base: `03481f7066487c44631cb9065899894ee8db71fb`. Target: main. Human merge only.
IMPLEMENTATION_NOT_STARTED=YES. PRODUCTION_MUTATION_PERFORMED=NO. No approved prior plan found.

## Problem and outcome

The bootstrap schema assumed complete country/position, three-layer notes, concentration on bottle
variants and coarse source rights. Real source profiling contradicts those assumptions. This proposal
defines a portable catalogue and evidence model, describes source gaps, and specifies a bounded local
pilot before final schema/hosting adoption. It is not approval to import every source or deploy a service.

## Task map and traceability

Codex acts as planning/research/documentation agent in this task. Human owner reviews decisions and
merges. Future implementation/review roles below are responsibilities, not agents launched in this session.

| Major topic / numbered subtasks | Requirements | Deliverable / evidence | Dependency |
|---|---|---|---|
| 1. Repository truth: 1.1 policy/workflow; 1.2 requirements/vault; 1.3 branch/SHA/PR and stale status | Governance; R01–R31 context | Task note, Git state, baseline reconciliation | Owner's planning request |
| 2. Sources: 2.1 dataset license; 2.2 API terms; 2.3 regional pages; 2.4 asset rights | R06, R19–R22 | [[Source_Registry]], [[Rights_and_Attribution]] | 1 |
| 3. Profiling: 3.1 aggregate completeness; 3.2 selected profiles; 3.3 mapping; 3.4 conflicts/media/commerce | R01–R04, R06, R08, R13, R14, R17, R21 | [[P1_Data_Profiling_Findings]], [[P1_Source_to_Canonical_Mapping]], [[P1_Data_Conflict_Matrix]] | 2 |
| 4. Schema: 4.1 catalogue/aliases; 4.2 claims/rights/conflicts/staging; 4.3 images/evidence; 4.4 listings/cart/purchases/inventory | R01–R03, R07, R10, R16–R21, R23–R30 | [[ERD_Draft]], [[Data_Dictionary_Draft]], [[Data_Quality_and_Provenance]] | 3 |
| 5. Hosting/recovery: 5.1 current allowances; 5.2 storage tradeoffs; 5.3 portable DB/object recovery | R13, R21, foundation for R26/R28 | [[P1_Storage_Hosting_and_Recovery]], ADR-003..006 | 4 |
| 6. Pilot: 6.1 environment; 6.2 ETL/validation; 6.3 image tests; 6.4 benchmark/restore; 6.5 host gate | R19–R22 and future relational invariants | [[P1_Pilot_Implementation_Plan]] | 4–5 and owner merge |
| 7. Publication: 7.1 Obsidian sync; 7.2 doc checks; 7.3 docs-only commit/push/Draft PR; 7.4 receipt/handoff | Workflow | Task/log/status and one immutable final receipt when review-ready | 1–6 |

Requirement statuses remain those of [[Requirements_Register]]; coverage here means design support,
not implemented feature acceptance. R12 AI and R31 spending analytics stay outside this pilot.

## Scope and do-not-touch

In scope: read-only licensed profiling, bounded public research, proposals for schema/constraints/indexes,
field mappings/conflicts/rights, current hosting limits, export/restore and future tests, documentation and
one Draft Planning PR. Runtime scripts, SQL/migrations, Docker configuration, cloud projects, actual ETL,
full catalogue acquisition, private data, paid actors, secrets, deployment, merge and auto-merge are excluded.
Fragrantica is reference-only; no scraping/internal API. The cart remains a bookmark/shopping tracker.

## Evidence-based proposal

Observed Scento snapshot: 1,479 perfumes, 160 houses, 420 materials; 91 flat-only note profiles;
251 missing concentration; 1,399 missing year; two missing house countries. Exact IDs and house links
pass bounded checks. One repeated house/name group is EDP/EDT, not a confirmed duplicate. No Thai or
Indonesian houses; no image/price/rating/pairwise evidence fields. Regional official-page research shows
field diversity and conflicting claims, but provides no blanket import/reuse permission.

PROPOSED: normalized concentration/edition-specific perfume profiles and packaging variants; typed
entity/provenance registry; immutable field claims and reviewed selections; separate taxonomy schemes,
notes/accords, source conflicts, image metadata, ratings and matching evidence. Preserve manual purchase
history and tenant ownership. Core types/keys stay PostgreSQL-portable. New sources add versioned
adapters/mappings; schema changes use reviewed migrations.

Alternatives: flat source copy is simpler but loses conflicts/provenance; JSON-only canonical data weakens
relationships; proposed normalized SQL + qualified JSONB costs more joins/storage and validation work.
Provider alternatives: Vercel/Supabase/Storage, Vercel/Supabase/R2, Docker/server. No host chosen.

## Planning acceptance and future acceptance

- [ ] Reviewer confirms repository/task map/scope and baseline discrepancies are documented.
- [ ] Reviewer can trace field mappings to measured source files or clearly marked documented page shapes.
- [ ] Source Registry distinguishes permitted research, API lookup, seed reuse and image rights; unknowns fail closed.
- [ ] Missing/duplicate/conflicting cases have explicit handling; no product facts fabricated for regional coverage.
- [ ] ERD/dictionary specify keys/types/nullability/constraints/indexes and match each other.
- [ ] Reviewer confirms bounded owner-approved local targets versus deferred cloud/storage/recovery choices; dated references/assumptions do not imply test or provider approval.
- [ ] DB and image/object backup/restore are separate, with PostgreSQL/Docker exit and auth/role caveats.
- [ ] Future pilot has bounded samples, meaningful negative tests, measurements and migration readiness criteria.
- [ ] Actual docs/link/frontmatter/diff results and exact changed files recorded before publication.
- [ ] Draft Planning PR exists and human review is the next action; no implementation or production mutation.

Checkboxes are owner review items, not self-approval. Runtime acceptance is exclusively future work in
[[P1_Pilot_Implementation_Plan]]; tests, DB size, egress and restore have NOT RUN.

## Owner Decisions — recorded for bounded Local Data Foundation Pilot

Human Owner explicitly approved the following in the current “Owner Decision Recording” chat message,
2026-11-10 Asia/Bangkok. This is local scope/design approval, not evidence of SQL/RLS verification or
Planning PR merge. Authoritative decision event/crosswalk: [[Decision_Log#Current Owner Decisions — S3 / 2026-11-10 / PR #1]].

| ID | Owner-approved scope | Deferred / blocked boundary | Validation / execution gate |
|---|---|---|---|
| OD-01 | APPROVED — pinned Scento CC BY 4.0 dataset for local pilot with attribution | No broader API/official-site/image grant; no wholesale API catalogue copy | Pin 086769ecf1add770ea6646bd4d88d39f0e7cddeb, preserve attribution/license/change notices; import tests pending; owner merge before implementation |
| OD-02 | APPROVED AS LOCAL IMPLEMENTATION DESIGN TARGETS — perfume identity, source claims, conflict handling and access-scope model | No claim of final SQL/RLS correctness, production readiness or product-facing sharing/auth integration | Actual SQL/FK/uniqueness/conflict/RLS/API isolation tests required, including local public/shared/private primitives; no runtime work in this session |
| OD-03 | APPROVED — disposable local PostgreSQL pilot only | DEFERRED — permanent hosting/provider/region selection and all cloud provisioning | Pin/test local version and disposable environment in a later implementation PR after planning merge; no cloud resources now |
| OD-04 | APPROVED — portable image metadata and rights-validation design | DEFERRED — storage provider; unlicensed asset acquisition NOT AUTHORIZED, blocked until usable rights verified | Exact asset/capture/grant/hash and derivative controls must be tested; design approval grants no new third-party image rights |
| OD-05 | APPROVED — local database/object backup and restore testing | DEFERRED — final retention, RPO/RTO and external backup provisioning | Use local permitted/owned test objects or clearly labeled fixtures; measure restore integrity/time later, no accepted production recovery target |
| OD-06 | APPROVED — international licensed-data pilot | BLOCKED — regional imports until usable rights AND real samples verified | Do not invent Thai/Indonesian facts or use synthetic fixtures as coverage; narrowed pilot need not wait for unavailable regional sources |

Gate P verified through owner merge above; each implementation agent rechecks merged plan
SHA and accepted local scope before starting a separate implementation PR. This recording session is
DOCS ONLY. Cloud/resources/application code/SQL/database creation and production mutation are excluded.

## Implementation breakdown and stop rule

IMP-P1-01 local SQL environment/migrations → IMP-P1-02 sample ETL → IMP-P1-03 image metadata →
IMP-P1-04 size/independent restore → IMP-P1-05 optional separately approved hosting readiness/migration.
See pilot note for roles, tests and dependencies. No implementation task/PR is started in this session.

Next: Human Owner reviews the recorded OD-01..06 bounded approvals and deferred/blocked boundaries, then merges PR #1 when satisfied. No further approval is needed to record these already-explicit decisions.
This agent stops after planning publication and its documentation closeout; never merges the PR.


## Architecture review corrections — S2 / PROPOSED

Historical planning task/branch and existing [PR #1](https://github.com/kraveerachat/DoomParfum-By-TK/pull/1), now MERGED.
S2 starts at `46c4a85309c408b3de7612d4853b166b84917359`; main stays at original base.
Original profiling/research, Task Map and immutable receipt are retained. No second receipt or new PR.
The logical proposal now has 47 tables: the original 44 plus access_scopes, scope_members and asset_permissions.

| Finding | Revised proposal / documentation | Future acceptance |
|---|---|---|
| R1 observation uniqueness | Same record may contain multiple same-field claims via mandatory section/field locator + occurrence key; select exact observation UUID; scoped conflict/resolution-member FKs | OBS-01..04 in [[P1_Pilot_Implementation_Plan]] |
| R2 private sources/assets | Non-null access_scope_id and public/shared/private ownership, scoped provenance FKs, private overlays about public entities, RLS + server/storage authorization; personal records remain private | ACL-01..07; public outputs must not reveal private existence |
| R3 image rights consistency | Exact scoped image/source/capture/assessment/permission tuple; own derivative binding + parent transform/output-license validation | IMG-01..06 and REC-01 |
| R4 repository/workflow truth | Public repository with existing workflow; private app data/secrets never in Git; separate proposed docs-CI backlog item | Document checks; no Actions/resources created |

## Resolution of S2 owner recommendations — S3

The former recommendation matrix is resolved by the Owner Decisions table above. Approvals are limited
to the international licensed-data LOCAL pilot/design/testing scopes. Permanent cloud/storage providers,
final retention/RPO/RTO and external backup remain DEFERRED; regional imports need both usable rights
and samples; unlicensed assets remain unauthorized. OD-02 requires actual SQL/RLS tests. None ran.

The 47-table dictionary and review corrections remain implementation design targets, not proof of an
executed schema or migration. Local tests may implement/test public/shared/private access primitives;
product-facing sharing, cloud auth/provisioning, web application and CI remain outside these approvals.
TSK-DOC-001 is a separate PROPOSED backlog item. Preserve all original source evidence and the original
Task Map above. No receipt rewrite/new receipt, implementation, provisioning or merge in this session.
