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
- [ ] All hosting choices/ADRs remain PROPOSED with dated primary references and capacity assumptions.
- [ ] DB and image/object backup/restore are separate, with PostgreSQL/Docker exit and auth/role caveats.
- [ ] Future pilot has bounded samples, meaningful negative tests, measurements and migration readiness criteria.
- [ ] Actual docs/link/frontmatter/diff results and exact changed files recorded before publication.
- [ ] Draft Planning PR exists and human review is the next action; no implementation or production mutation.

Checkboxes are owner review items, not self-approval. Runtime acceptance is exclusively future work in
[[P1_Pilot_Implementation_Plan]]; tests, DB size, egress and restore have NOT RUN.

## Open decisions — owner approval required before dependent work

| ID | Decision / recommended proposal | Evidence still needed / consequence |
|---|---|---|
| OD-01 | Use pinned CC BY 4.0 Scento export for local pilot, show source/license/change attribution | Owner confirms attribution policy; API only bounded lookup, not wholesale catalogue copy |
| OD-02 | Approve concentration/edition identity, general notes and typed field-claim model | Review extra schema/trigger complexity; unknown concentration never auto-merges |
| OD-03 | Local pilot first, then decide Vercel + Supabase vs server; region/budget remain open | Actual size, connection/auth compatibility, latency and current quotas |
| OD-04 | Per-asset grant; Supabase Storage vs R2 based on measured workload | Bottle rights unverified; Commons candidate metadata only; exact bytes/hash unmeasured |
| OD-05 | Daily independent DB/object exports; proposed 7 daily + 4 weekly, RPO 24h/RTO 2h | Owner sets cost/retention/privacy targets; rehearsal must prove or revise them |
| OD-06 | Obtain owned/licensed regional samples, including four priority Thai brands | No provided product sample; no verified HMNS reuse grant. Can approve a narrower international pilot while regional imports remain blocked |

Merging this plan must record the accepted decisions/narrowed scope in the PR. Open source rights do not
become permitted through a generic merge. Later provider provisioning needs an explicit bounded scope.

## Implementation breakdown and stop rule

IMP-P1-01 local SQL environment/migrations → IMP-P1-02 sample ETL → IMP-P1-03 image metadata →
IMP-P1-04 size/independent restore → IMP-P1-05 optional separately approved hosting readiness/migration.
See pilot note for roles, tests and dependencies. No implementation task/PR is started in this session.

Next: human owner reviews the Draft Planning PR, decides OD-01..06 and merges when satisfied.
This agent stops after planning publication and its documentation closeout; never merges the PR.


## Architecture review corrections — S2 / PROPOSED

Same task/branch and existing [PR #1](https://github.com/kraveerachat/DoomParfum-By-TK/pull/1), OPEN/DRAFT.
S2 starts at `46c4a85309c408b3de7612d4853b166b84917359`; main stays at original base.
Original profiling/research, Task Map and immutable receipt are retained. No second receipt or new PR.
The logical proposal now has 47 tables: the original 44 plus access_scopes, scope_members and asset_permissions.

| Finding | Revised proposal / documentation | Future acceptance |
|---|---|---|
| R1 observation uniqueness | Same record may contain multiple same-field claims via mandatory section/field locator + occurrence key; select exact observation UUID; scoped conflict/resolution-member FKs | OBS-01..04 in [[P1_Pilot_Implementation_Plan]] |
| R2 private sources/assets | Non-null access_scope_id and public/shared/private ownership, scoped provenance FKs, private overlays about public entities, RLS + server/storage authorization; personal records remain private | ACL-01..07; public outputs must not reveal private existence |
| R3 image rights consistency | Exact scoped image/source/capture/assessment/permission tuple; own derivative binding + parent transform/output-license validation | IMG-01..06 and REC-01 |
| R4 repository/workflow truth | Public repository with existing workflow; private app data/secrets never in Git; separate proposed docs-CI backlog item | Document checks; no Actions/resources created |

## Owner review recommendations OD-01..OD-06 — no acceptance inferred

All entries remain PROPOSED. Local pilot is eligible ONLY after owner review/merge and recorded accepted
scope. This correction request authorizes documentation changes, not the pilot itself.

| Decision | Eligible scope to approve for later LOCAL pilot | Still to test / prove | Source-rights blocks | Separate CLOUD/resource approval |
|---|---|---|---|---|
| OD-01 | Pinned CC BY 4.0 export, 12 selected real profiles and attribution/change metadata | Scoped provenance, idempotency, locator claims, attribution rendering | No wholesale API catalogue copy; official-site content excluded without grant | None needed for local files; paid/API account setup needs own approved scope |
| OD-02 | Concentration/edition identities + locator-based observations + public/private scopes; reserve shared model without enabling it | Composite FKs, resolution membership, RLS/API isolation, overlay/caches, admin-bypass and two synthetic-user tests | No private→public claim promotion without public-use rights and separate review | Auth/provider/host setup not approved; shared-mode activation needs explicit owner scope/tests |
| OD-03 | Disposable loopback PostgreSQL/container design and offline/sample worker only | Pin versions/digest, migration/restore, measured sizes and connections | Import only approved sources; no provider choice overrides license | Vercel/Supabase/server, account, region, budget and any provisioning need explicit bounded approval |
| OD-04 | Metadata-only images and clearly labeled synthetic permission tests; owned/CC asset bytes only if individual grant and intended local use are approved | Exact permission tuple, parent transform/output license, expiry/revocation, authenticated delivery and actual sizes | Bottle/HMNS/unknown assets cannot be acquired/displayed; Commons candidate is not automatic acquisition approval | No bucket/CDN/R2/Supabase Storage/paid image service creation without separate approval |
| OD-05 | Disposable local DB export and separate permitted object-manifest/restore rehearsal | Integrity + private scopes/claims/permissions after restore; measure proposed RPO/RTO | Rights/retention rules still constrain private backup and redistribution | External backup account/bucket, paid storage, retention/cost and production schedule require approval |
| OD-06 | Narrower licensed international pilot; accept regional GAP status and target sample requirements | Obtain real owned/licensed samples and validate country/identity coverage | Four Thai priorities and Indonesian product imports remain blocked until grants/samples verified | No scraper/paid actor/account connection/cloud ETL implied; scope/cost approved separately |

Recommend owner explicitly approve/defer each column rather than a blanket approval of all sources and
hosts. Rights denial cannot be overridden by a generic merge. Tests above are SPECIFIED / NOT RUN.
See [[Data_Dictionary_Draft]], [[Security_and_Privacy]], [[Rights_and_Attribution]] and backlog TSK-DOC-001.
