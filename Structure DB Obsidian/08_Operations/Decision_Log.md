---
id: DPT-OPS-001
project: DoomParfum By TK
type: decision_log
status: draft
owner: project
updated: 2026-11-23
tags:
  - doomparfum
  - operations
  - decisions
  - governance
source_of_truth: "../../README.md"
---

# Decision Log — DoomParfum By TK

## Post-PR13–17 verified integration — 2026-11-13

Owner merge13–17 is verified, including private architecture PR15. No exact individual answer to
DM01–07/OP01–06 has been recorded or inferred. [[Next_Wave_Owner_Decision_Form]] is this wave's single
answer-entry surface, retaining canonical definitions from [[Post_Merge_Owner_Decision_Packet]].
Only actual Owner/date/reference/version/scope answers can change a decision. Source licensor rights
must still be independently evidenced; Owner task approval cannot create third-party copyright.
Current implementation gates remain blocked, independent research/planning continues. No accepted
OD/DEC/ADR is changed; changed recommendations require the appropriate Planning Amendment.


## Post-merge Waves 0–2 — 2026-11-13

Owner merge events9–12 are verified artifact-scope acceptance events, not individual answers to
DM01–07, normalization/closure, app identity, stack/cache/publication or new source/media rights.
Every unanswered choice remains PROPOSED. No accepted OD/DEC/ADR record is changed. A separate
DPT-PLAN-004 answer packet presents recommended options, alternatives, operational impacts and
unchecked answers. Only an actual Owner reply identifying choice/version/scope may update a decision.
DPT-PLAN-005 and006 remain separate Planning Gates. Current facts: [[Post_Merge_Owner_Review_Matrix]].


## 2026-11-13 — Explicit DM and operational proposals, no new acceptance

No individual DM01–07approval text/date/version is recorded. Owner-merged PR4 and the current
review request authorize bounded work, not the proposed numeric weights, closure/fallbacks, lifecycle,
stack/auth/publication/provider or source/image permissions. [[Matching_Owner_Decision_Register]]
states recommendation, alternative, operational effect and exact unapproved status for every row.

[[Matching_Nonadmin_Session_and_Publication_Proposal]] records actual immutable auth_subject and
scope owner/kind constraints: no private membership shortcut or administrative impersonation.
Recommended clean separately approved application-private pilot and alternative auth-model amendment
are proposals only; no current pilot owner, role or assessment changed. [[Matching_Data_Readiness_and_Closure_Gates]]
separates complete-as-reported from chemical/perceptual absence,43proposed duplicate membership views
from retained occurrence evidence, Khamrah conflict, selected-field rights and eligibility.

Independent source acceptance of PR11is not Owner merge, data rights or real-data matching approval.
PR9needs explicit bounded-milestone acceptance before its full-task closeout can change; otherwise
ModeA remains gated. Commons revision bindings authenticate page metadata availability only, not
ownership/effective asset rights. Existing OD/DEC rows and allDM PROPOSED statuses remain unchanged.

## 2026-11-13 — Owner merge event versus individual DM decisions

Verified origin/main aa55f8b59acb0872b3b40273a8cdd25198f3ba27. Human Owner merged PRs1–7;
PR4 GateP is merged, but DM01–07 remain PROPOSED. Historical OPEN/DRAFT/pending statements below
are dated snapshots. No source/asset/publication right, numeric default or application stack is
accepted by inference. All8migrations and every pre-existing immutable receipt remain exact.

Record the Planning Gate merge event only. The explicit post-PR4 request authorizes scoped local
adapter implementation, conservative audits, generic synthetic mathematical primitives and
application-readiness specifications. It does not accept proposed50/30/20,25/37.5/37.5,80/20,
completeness/currentness/freshness thresholds, accord presence/strength fallback, stack/auth,
public sharing, providers or new rights. All DM01–07 remain PROPOSED; no OD/DEC row changes.

[[Post_PR4_Application_Readiness]] records the concise seven-row recommendation/gate matrix.
Selected-field/rights/closure/eligibility/auth gates keep real matching disabled.43duplicate-hold
normalization sidecars are unapproved; Khamrah and21identity conflicts remain unresolved.

## DPT-PLAN-003 decision review — 2026-11-11 / PROPOSED

[[Dual_Mode_Matching_Decisions]] records DM-01..07 for independent modes, labels/weights/coverage,
accord scale/fallback, custom-query rules, current-first grouping and read-only architecture. Confirmed
owner intent is distinct from numerical proposals. No DEC/OD/ADR status or approved source grant changes.
PR #3 NEW-08/09/11 semantic overlap is reconciled against merged upstream context in
[[P2_Post_PR5_Matching_Reconciliation]] after PR #5. DM-01..07 remain PROPOSED; this feature Gate P
is pending. Intake merge does not approve weights, completeness/absence, matching flags or publication.

## Current execution event — verified planning merge / IMP-P1-01

PR #1 owner merge verified at `bffb2fab1918dc5221a6c5da7920168bcae263ca` on 2026-11-10. Gate P is satisfied;
local SQL implementation now belongs to [[IMP-P1-01_Local_PostgreSQL_Schema]], pending its own Human
Owner review/merge. Prior S1/S2/S3 gate/status statements below are historical snapshots. OD-01..06
approval rows are unchanged; no deferred decision is accepted by this event. PostgreSQL 16.15 image
is pinned for this disposable pilot only. Conservative machine-contract findings are documented in
`database/schema_findings.md`; actual SQL/RLS evidence is [[IMP-P1-01_Implementation_Evidence]].
Shared SQL tests do not activate a shared product mode. No cloud/provider/storage/retention/RPO/RTO,
external backup, regional import or unlicensed asset approval is inferred.


> **Document Type:** Architectural & Product Decision Register
> **Source Baseline:** `../README.md` (Section 10)
> **Status:** Active Decision Register

---

## 1. Overview & Rules of Decision Governance

เอกสารนี้รวบรวมการตัดสินใจระดับโครงการ ทั้งในมิติผลิตภัณฑ์ (Product Decisions) และสถาปัตยกรรมทางเทคนิค (Architectural Decisions)

> [!IMPORTANT]
> **กฎการบันทึกสถานะ:**
> - `[CONFIRMED]` คือการตัดสินใจที่ได้รับความเห็นชอบอย่างเป็นทางการจากผู้ใช้แล้ว
> - `[PROPOSED]` คือข้อเสนอทางเทคนิคที่อยู่ในระหว่างรอการรีวิวหรือทดลอง **ห้ามเปลี่ยนเป็น CONFIRMED เอง**
> - ทุกการตัดสินใจต้องระบุบริบท (Context), ทางเลือกที่พิจารณา (Alternatives), และผลกระทบ (Consequences)

---

## 2. Master Decision Register (DEC-001 ถึง DEC-009)

| ID | หัวข้อการตัดสินใจ (Decision Summary) | สถานะ | วันที่บันทึก | เอกสารอ้างอิง |
|---|---|---|---|---|
| **DEC-001** | DoomParfum By TK เป็น Research/Comparison/Collection App ไม่ใช่ E-commerce (ไม่มี Checkout หรือ Payment Gateway) | **CONFIRMED** | 2026-11-10 | [[Vision_and_Scope]], [[Domain_Model]] |
| **DEC-002** | `My Cart` เป็น Saved Items + Buying Sources ในแอป ไม่ใช่การเชื่อมต่อหรือซิงก์ตะกร้า Shopee โดยตรง | **CONFIRMED** | 2026-11-10 | [[My_Cart_and_Ownership]], [[Shopping_Tracker]] |
| **DEC-003** | การเปลี่ยนสถานะสั่งซื้อและครอบครองทำด้วยมือ (Manual Ordered / Owned Status) พร้อมแยก Purchase History ออกจาก Inventory | **CONFIRMED** | 2026-11-10 | [[My_Cart_and_Ownership]], [[Collection_Dashboard]] |
| **DEC-004** | กำหนด Designer/Niche เป็น Reference Scent และค้นหาทางเลือกที่คุ้มค่าในงบเริ่มต้น <= ฿2,000 (ปรับตัวกรองได้) | **CONFIRMED** | 2026-11-10 | [[Vision_and_Scope]], [[Scent_Matching_Spec]] |
| **DEC-005** | แยกมิติประเทศต้นกำเนิด (Origin Country) ออกจากตำแหน่งตลาด (Market Position) ไม่เหมารวมทั้งแบรนด์ | **PROPOSED** | 2026-11-10 | [[Brand_Taxonomy]] |
| **DEC-006** | เริ่มต้นด้วย Rule-Based Scent Matching (Pyramid 40%, Accords 25%, Family 15%, Evidence 20%) แทนการเทรนโมเดล ML ใหม่ | **PROPOSED** | 2026-11-10 | [[Scent_Matching_Spec]], [[Tech_Stack_and_ADRs]] |
| **DEC-007** | นำเข้าข้อมูลเฉพาะจากแหล่งที่ได้รับอนุญาต/ชุดข้อมูลเปิด (Open Datasets/APIs) และการบันทึกของผู้ใช้; ห้าม Mass Scraping | **PROPOSED** | 2026-11-10 | [[Source_Registry]], [[Rights_and_Attribution]] |
| **DEC-008** | สแต็กทางเทคนิคเริ่มต้นเสนอเป็น Next.js (App Router) + PostgreSQL + Drizzle ORM + Docker Compose | **PROPOSED** | 2026-11-10 | [[Proposed_System_Architecture]], [[Tech_Stack_and_ADRs]] |
| **DEC-009** | ใช้ Obsidian Markdown Vault สำหรับ Living Documentation และใช้ GitHub สำหรับ Version Control (Workflow exists; proposed governance acceptance pending) | **CONFIRMED** | 2026-11-10 | [[Project_Index]], [[GitHub_and_Workflow_PENDING]] |
| **DEC-010** | ใช้ Two-Gate Development Workflow (Gate P: Planning PR -> Human Merge -> Gate I: Implementation PR -> Human Merge) | **ACCEPTED BY OWNER MERGE PR #1** | 2026-11-10 | `../DEVELOPMENT_WORKFLOW.md`, [[GitHub_and_Workflow_PENDING]] |
| **DEC-011** | ข้อยกเว้นการ Push Initial Documentation Baseline ขึ้นสู่ `main` โดยตรงเพียงครั้งเดียวสำหรับ Remote ที่ว่างเปล่า | **CONFIRMED** | 2026-11-10 | `../AGENTS.md`, `../DEVELOPMENT_WORKFLOW.md` |

---

## 3. Detailed Decision Profiles

### DEC-001: Research App vs. E-Commerce Platform
- **Context:** การสร้างระบบน้ำหอมอาจทำให้เกิดความเข้าใจผิดว่าจะต้องเชื่อมต่อระบบชำระเงิน ตัดบัตรเครดิต หรือสต็อกสินค้า
- **Decision:** [CONFIRMED] มุ่งเน้นเป็นระบบผู้ช่วยวิจัย เปรียบเทียบ และเก็บบันทึกประวัติส่วนตัว ไม่มีฟังก์ชันสั่งซื้อจริง
- **Consequences:** ตัดความซับซ้อนเรื่อง Payment Gateway, PCI-DSS compliance, นโยบายคืนเงิน, และระบบจัดการสต็อกของร้านค้า

### DEC-002: In-App My Cart as a Bookmark/Shopping Tracker
- **Context:** ผู้ใช้ต้องการรวบรวมน้ำหอมที่เล็งไว้จากคลิปรีวิวและร้าน Shopee
- **Decision:** [CONFIRMED] `My Cart` เป็นเพียงกระดานจดโน้ตรายการเตรียมซื้อ และที่เก็บบันทึกลิงก์ร้านค้าภายนอก
- **Consequences:** ผู้ใช้เป็นผู้กดลิงก์ออกไปซื้อเองที่แอป Shopee

### DEC-003: Manual State Transition & Purchase Record Persistence
- **Context:** เมื่อผู้ใช้ซื้อสินค้าภายนอก ระบบไม่มี Webhook แจ้งสถานะการสั่งซื้อ
- **Decision:** [CONFIRMED] ให้ผู้ใช้กดปุ่ม `Mark as Ordered` และ `Mark as Received` ด้วยตนเอง พร้อมทั้งแยกตาราง `purchase_records` ไม่ให้ถูกลบเมื่อขวดน้ำหอมหมดลง
- **Consequences:** ได้ข้อมูลประวัติศาสตร์การซื้อที่ถูกต้องถาวร เพื่อใช้คำนวณในแดชบอร์ดระยะยาว

---

## 4. Change Notes

- `2026-11-10`: บันทึกการตัดสินใจตั้งต้น DEC-001 ถึง DEC-009 คงสถานะ Confirmed/Proposed ตามความจริงใน README


## Historical P1 planning proposals — 2026-11-10 / DPT-PLAN-001 (current resolution below)

| ID | Proposal | Status | Context / alternatives / consequence |
|---|---|---|---|
| DEC-012 | Evidence-backed normalized SQL, nullable unknowns, concentration/edition scent identity, packaging variants, typed source claims/conflicts | PROPOSED | Real source gaps/collisions invalidate complete flat schema; JSON-only and single-source alternatives considered; more validation/storage complexity; ADR-003 |
| DEC-013 | Local PostgreSQL pilot before Vercel/Supabase or Docker hosting choice | PROPOSED | No DB size/runtime/restore proof yet; managed vs self-hosted alternatives; host requires measured readiness; ADR-004 |
| DEC-014 | Portable image metadata; decide Supabase Storage vs R2 after rights/size/traffic evidence | PROPOSED | Source export lacks photos; choose simplicity vs capacity/egress; per-asset permission remains mandatory; ADR-005 |
| DEC-015 | Independent database and image/object backups, PostgreSQL/Docker restore rehearsal | PROPOSED | DB backups exclude bytes; separate manifests/storage/roles/auth mapping adds operations but tests portability; ADR-006 |

Detailed ADR context/options/consequences and acceptance: [[Tech_Stack_and_ADRs]]. Owner decisions
OD-01..OD-06 remain open in [[P1_Data_Foundation_Plan]]. No proposal is accepted through this log.
The owner's current request authorizes only documentation research, planning branch/push/Draft PR.
No historical bootstrap exception is reused and no implementation/production action is authorized.


## Historical post-review refinements — S2 / 2026-11-10 / PR #1 (current resolution below)

| ID | Recommendation and context | Alternatives / consequence | Status |
|---|---|---|---|
| DEC-016 | Preserve multiple same-record claims via section/field locator + occurrence key; introduce public/shared/private access scopes and scoped overlays | Record/field-only uniqueness loses structured/prose claims; public-entity access inheritance leaks private facts. Non-null scope and composite FKs/RLS/API rules add validation work; shared activation deferred | PROPOSED |
| DEC-017 | Bind image permission to exact scope/asset/source/capture/assessment; own derivative grant and parent transform/output-license review | Source-wide loose rights_id insufficient; new asset_permissions table/expiry/lineage and proxy tests required. No source grant or bucket approval inferred | PROPOSED |
| DEC-018 | Separate TSK-DOC-001 for future documentation CI | Keep current correction Markdown-only; future Actions/tooling/permissions need separate owner-authorized scope | PROPOSED |

Owner recommendations for OD-01..06: [[P1_Data_Foundation_Plan]]. No existing proposed decision is
accepted in S2. At that historical snapshot: repository public, workflow existed, PR #1 was OPEN/DRAFT. Historical bootstrap log
may describe earlier pending states; it does not override these current facts. Immutable receipt
[[2026-11-10_201028_DPT-PLAN-001_P1_Planning]] stays unchanged, no second receipt.


## Current Owner Decisions — S3 / 2026-11-10 / PR #1

Authority: Human Owner's current chat message, “Owner Decision Recording for Planning PR #1”.
Recorded by Codex; approval is explicit owner direction, not agent self-acceptance. This section
supersedes earlier S1/S2 all-PROPOSED/open wording for the bounded scopes below only. Historical
proposal text is retained as history. At S3 recording PR #1 was OPEN/DRAFT and Gate P was pending; the verified owner-merge event above now supersedes that gate status.

| ID | Owner-approved scope | Deferred / blocked boundary | Validation / execution gate |
|---|---|---|---|
| OD-01 | APPROVED — pinned Scento CC BY 4.0 dataset for local pilot with attribution | No broader API/official-site/image grant; no wholesale API catalogue copy | Pin 086769ecf1add770ea6646bd4d88d39f0e7cddeb, preserve attribution/license/change notices; import tests pending; owner merge before implementation |
| OD-02 | APPROVED AS LOCAL IMPLEMENTATION DESIGN TARGETS — perfume identity, source claims, conflict handling and access-scope model | No claim of final SQL/RLS correctness, production readiness or product-facing sharing/auth integration | Actual SQL/FK/uniqueness/conflict/RLS/API isolation tests required, including local public/shared/private primitives; no runtime work in this session |
| OD-03 | APPROVED — disposable local PostgreSQL pilot only | DEFERRED — permanent hosting/provider/region selection and all cloud provisioning | Pin/test local version and disposable environment in a later implementation PR after planning merge; no cloud resources now |
| OD-04 | APPROVED — portable image metadata and rights-validation design | DEFERRED — storage provider; unlicensed asset acquisition NOT AUTHORIZED, blocked until usable rights verified | Exact asset/capture/grant/hash and derivative controls must be tested; design approval grants no new third-party image rights |
| OD-05 | APPROVED — local database/object backup and restore testing | DEFERRED — final retention, RPO/RTO and external backup provisioning | Use local permitted/owned test objects or clearly labeled fixtures; measure restore integrity/time later, no accepted production recovery target |
| OD-06 | APPROVED — international licensed-data pilot | BLOCKED — regional imports until usable rights AND real samples verified | Do not invent Thai/Indonesian facts or use synthetic fixtures as coverage; narrowed pilot need not wait for unavailable regional sources |

Decision crosswalk: DEC-012/016 and ADR-003 accepted as local design targets under OD-02, subject to
actual SQL/RLS tests; DEC-013/ADR-004 accepted only for disposable local PostgreSQL; DEC-014/017 and
ADR-005 accepted for portable metadata/rights design, provider/acquisition excluded; DEC-015/ADR-006
accepted for local recovery testing only. DEC-008's broader web/cloud stack, matching ADR-002 and
DEC-018/TSK-DOC-001 CI proposal are not approved by this decision. Governance status is not changed
by inference. No permanent cloud provider, production schema, source/image grant or recovery target
is accepted beyond the explicit owner scope.

Implementation starts only in a separate task/PR after verified Human Owner merge of the accepted
planning scope. This recording session creates no SQL, database, app code, cloud resource or deployment.
PRODUCTION_MUTATION=NO. Human Owner alone merges. Original immutable receipt remains unchanged;
record this new decision event in task/change/run logs, never create a second receipt.


## DPT-PLAN-002 open decisions — 2026-11-11 (NOT OWNER-APPROVED)
| Decision | Proposed choice | Status |
|---|---|---|
| NEW-01 | Broad regional brand registry, role/taxonomy separated from verified identity, lane priorities/no hard caps | PROPOSED |
| NEW-02 | Source-by-field/use/asset rights gate; unknown=no automation/republish | PROPOSED |
| NEW-03 | Reference/alternative candidate ranking weights + per-region cohorts/min evidence | PROPOSED |
| NEW-04 | Production lifecycle vs per-market availability and historical access | PROPOSED |
| NEW-05 | Owner/admin update job, safe allowlisted promotion, conflict review, bounded scheduling | PROPOSED |
| NEW-06 | Python/Docker/local DB first, measure before choosing hosting/storage | PROPOSED |
Existing OD-01..06 limited approvals retain their current scope. No decision above is accepted by PR creation. See [[DPT-PLAN-002_Focused_Catalogue_Acquisition_and_Automation]].

## 2026-11-11 — verified gates and licensed implementation, no new owner decisions

PR3 is now owner-merged at a908711fb4f37a12fbec3665a461b75c288c7dab after merged PRs1/2. This records
Gate P, not blanket source rights, cloud approval or automatic acceptance of every proposed parameter.
OD-01..06 bounded licensed/local approvals support [[IMP-P1-02_Licensed_Scento_ETL]].1435 source-exact
profiles approved by independently reviewed mapping;44 held. No NEW/DM status is changed here.
PR4 remains Draft; capacity/restore, source-specific regional rights and per-image approval remain
separate. Human Owner reviews/merges implementation. PRODUCTION_MUTATION=NO.

## Owner execution-scope reply — 2026-11-14

Actual Owner reply in the current conversation: “คงทุกข้อ PROPOSED และทำ preparation ต่อ”.
Recorded 2026-11-14T01:59:34.926470+07:00. Execution scope is confirmed as preparation only. No DM01–07/OP01–06 choice,
normalization/closure/source right,session/stack/publication policy or implementation is accepted.
The integrated form remains unanswered for policy choices. Continue authorized independent research,
golden arithmetic,contracts,documentation,review and handoff; stop only dependent implementation.
This records the reply truthfully rather than treating it as acceptance of every recommendation.

## Current explicit Owner direction — post-PR18–21 / 2026-11-14

Authority: full Owner Master Prompt, POST-PR18–21 DEVELOPMENT & CATALOGUE COMPLETENESS WAVE,
1,376 lines/28,635 bytes; SHA256 b459c07e94ff6c68682165c3a166c7965a31b36e39e6a231118c304c1e402b23.
This later instruction supersedes the earlier preparation-only reply **at strategic direction level**.
The earlier reply remains historical evidence. It does not accept unspecified individual options.

**CONFIRMED direction:** prioritize Mode A/B1 before real B2; deterministic/synthetic first; keep
Structural/Query Fit, Data Confidence and Pair Evidence separate; preserve source claims and44holds;
do not infer absence from incomplete lists; initial local-private/no public API/shared cache;
permissioned catalogue enrichment including names,brands,notes andimages; no autonomous Production.

**UNRESOLVED exact choices:** DM03/05 formulas/constants/method/domain/fallback versions;
DM04 taxonomy/scale; DM06 lifecycle/freshness thresholds; OP01 full-task milestone scope;
OP02 closure assertions; OP03 repeated-note/Khamrah normalization; OP04 field/use/audience rights;
OP05 genuine nonadmin binding; OP06 stack/auth/transport/budgets. Individual DM/OP policy rows remain
PROPOSED unless their exact text/version/scope is explicitly answered. No third-party permission,
application principal,source acquisition,cloud or public publication is created by this direction.

Merged PR18/19/20/21 establish plan/research integration at main8c6a8376680c7a10cc3eb4b5cf80afe4376a9282,
not hidden policy defaults. Actual Wave0:55offline methods PASS; fresh leased READ ONLY audit;
all49data/security/application-role fingerprints unchanged. Matching0/holds44 remain unchanged.

## Post-PR22–25 continuation checkpoint — 2026-11-14

Actual main8c6a8376680c7a10cc3eb4b5cf80afe4376a9282 unchanged;22–25OPEN/DRAFT/clean,notmerged.
No formalreviews/comments/checkrollups;noCI PASS or exactOwneranswers. Fresh62offlinecandidate
methodsPASS(55baseline+7invariantsincluded),runtime mainbyte-exact;future/full/live testsNOTRUN.
CurrentDBrevalidationBLOCKED Dockerpipeabsent,no restart/query;03:04BangkokcountsHISTORICALONLY.
[[Post_PR22_25_Owner_Review_and_Unlock]] coordinates exact review/gate/sample/normalization/app
preparation onexistingPR25. AllindividualchoicesPROPOSED,strategicdirectionCONFIRMED. Preserve
receipts/migrations/44holds/matching0/PR8;no secondreceipt/newduplicatePR or implementationunlock.

## Exact Owner acceptance and M1 start — 2026-11-14

Human Owner explicitly accepted M1-NL-TYPED-1 SHA-256
a57f4c56e1068a3d86a99e562b31e5c3923e2d369cb4e812c1dd5f5550a5ada3,
mc-a-notes-layered-p1/config m1-nl-typed-config-1, allocating IMP-MATCH-08 to synthetic-only
pure typed Python. [[M1_Exact_Owner_Acceptance]] records the exact dated scope and exclusions.
This is explicit approval, not an inference from merged PR22–25. Other unaccepted DM/OP/B1,
real-data/source/app policies remain PROPOSED or gated in their own scopes.

Verified main/base0da217671ec6473716eea5947f013d44e6fd91cb includes Owner merges21–25.
Isolated branch codex/imp-match-08-synthetic-m1 starts there; [[IMP-MATCH-08_Synthetic_M1]] is
IN PROGRESS. All five preparation documents and existing immutable receipts/migrations are
preserved. New code/test work uses TDD and requires independent exact implementation review
before agent acceptance/one Draft PR. PR8 stays OPEN/DRAFT/BLOCKED; no timestamp experiment.
No database mutation, real ranking, acquisition, hold/eligibility or Production change.

## Owner M1 merge and B1 preparation — 2026-11-15

Verified PR26Owner merge604d447e599aa8359d3427dfbfbceaac85373e48 at2026-11-14T21:33:25Z
(2026-11-15 04:33:25 Asia/Bangkok). M1 head63cb56c54aacef99fa8937e7a5211acca8ae6a63 has exactly
the same complete Git tree as the merge. Existing M1 code/tests/contract/reports and its one receipt
are unchanged; all22receipts and8migrations are preserved. No M1 test rerun or repeated planning.

[[B1_Contract_Preparation]] is IN PROGRESS in a new detached latest-main checkout. The existing
separate IMP-MATCH-03 B1 task remains gated on one exact Owner contract.80/20 remains PROPOSED.
No B1 implementation branch/runtime/PR/receipt, data/rights/hold/eligibility or Production mutation.
PR8 remains OPEN/DRAFT/BLOCKED at84dccb117971ab65e0bf39fa3d1d84a12d344f8d, with no new causal
timestamp evidence/experiment/fix. Current database counts/role/rights are NOT REVALIDATED.
Historical pending statements and immutable receipts are retained, not rewritten.

## Owner holds implementation pending final review — 2026-11-15

Owner explicitly answered “ยังไม่อนุมัติ implementation”, then agreed in principle with method/config/
IMP-MATCH-03 synthetic-only pure typed scope while requesting a13-point final summary before Exact Approval.
[[B1_Final_Owner_Review_Summary]] now records the exact77bfca59... contract, formulas/examples, schemas,
gates, bounds, deterministic output, future tests, independent125review and exclusions. Contract bytes
and125-review artifact are unchanged. Three fresh literal rational example assertions pass; no B1
evaluator/feature test runs. No implementation branch, source, PR or receipt is created.
The previous question is answered NOT APPROVED; do not treat principle agreement as exact acceptance.
Final Owner Approval is proposed only after the summary is reviewable. Workstreams B/C resumed from
their preserved partial evidence and remain independent in this current wave; no import/asset download.

## Exact B1 Owner approval and implementation start — 2026-11-15

Human Owner explicitly accepted B1-PD-TYPED-1 revision2 SHA-256
77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977,
mc-b1-pyramid-positive-domain-p1/configb1-pd-typed-config-1/schemab1-pd-typed-schema-1,
IMP-MATCH-03 synthetic-only pure typed Python, including4/5Coverage+1/5Focus and all exact rules.
[[B1_Exact_Owner_Acceptance]] records the actual dated scope/exclusions. This is a new explicit
decision, not inference from prior NO/principle agreement/PR26merge. Frozen contract and preparation
snapshots remain unchanged; prior statements are retained dated history.
[[IMP-MATCH-03_Synthetic_B1]] is IN PROGRESS on codex/imp-match-03-synthetic-b1 from main604d447.
Actual tests/review are pending, no final receipt/PR. Research B/C continues independently;
no acquisition/import/rights/publication,real ranking,DB/Production/44hold/eligibility or agent merge.

## Post-PR27 consolidated planning checkpoint — 2026-11-15

Verified main `8eef8f13265adc14db0cae82ff77cfc4863853ce` includes Owner-merged PR26 (merge604d447e599aa8359d3427dfbfbceaac85373e48) and PR27 (head3ed276f298c082b7450c4bbe338c8965eacc25a7; merge equals current main). Their exact M1/B1 synthetic contracts remain accepted and implemented. Earlier awaiting-review/NOTAPPROVED snapshots are dated history; no broader policy approval is inferred.

[[DPT-PLAN-009_Post_PR27_Next_Wave]] coordinates one docs-only branch `plan/post-pr27-next-wave` and one Draft Planning PR. See [[Post_PR27_Consolidated_Next_Wave_Plan]] and [[Post_PR27_Owner_Decision_Packet]] version POST27-ODP-1. A/B/C preparation is complete; exact A–I choices remain PROPOSED/UNANSWERED. Future IMP-ENR-01 is only a proposed five-record offline preview after exact A/B/I acceptance and planning merge, not an active implementation task.

Source1479/160/420 are pinned raw-file counts, not current canonical DB counts. All44holds,43unapproved normalization proposals and independent Khamrah evidence remain unchanged. All23media leads (17note/6bottle),fourconditionaldossiers and the two-PNG proposal remain references only; no new binaries or grants. No real-data ranking, Full Mode A/B2, source adaptation/import, database or authentication change, API/UI/transport, cloud or Production operation occurred.

Docker client28.3.2 exists but engine pipe is absent: DOCKER_NOT_AVAILABLE / DB_NOT_REVALIDATED. Configured names/mounts and four backup-file metadata hashes are not live service or recovery proof. PR8 stays OPEN/DRAFT/BLOCKED at84dccb117971ab65e0bf39fa3d1d84a12d344f8d, with no new timestamp experiment, speculative fix, integration or receipt. [[DPT-PLAN-009_Post_PR27_Verification]] distinguishes lane checks,194offline regression methods, initial fixture/checker failures, future NOTRUN tests and independent review.

Decision classification: PR26/27 merge events are VERIFIED OWNER EVENTS. The original exact synthetic acceptances remain accepted only in their stated scopes. POST27-ODP-1 A–I recommendations and residual DM/OP choices are PROPOSED, not new Owner decisions. Regional grants require external permission; current DB/role/rights/eligibility facts are NOT VERIFIED. Planning merge alone will not supply those answers.

## Post-PR28 architecture refinement checkpoint — 2026-11-16

Verified main `168715bc9bc5fff968524074257dc106a8a63638` contains Owner-merged PR26, PR27 and PR28. PR28 merged from head `6521c5201f4f4d0e85c4fd8542db222284e96e9e` at UTC `2026-11-15T17:39:38Z`. Its general direction is confirmed; exact POST27 A–I choices are not accepted. POST27-ODP-1 and SHA `0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c` remain unchanged. IMP-ENR-01 is not started.

[[DPT-PLAN-010_System_Architecture_Refinement]] owns one docs-only amendment branch `plan/post-pr28-architecture` and a future Draft Planning PR. [[System_Architecture_Refinement]] joins eight C4-style/sequence diagrams, 30 components and an explicit source dependency DAG, 17 proposed routes retaining the full product roadmap, 28 proposed operation interfaces, strict DTO/state/rights contracts and [[UI_Element_Function_Matrix]]. All UI handlers/application services are PROPOSED, not source APIs. No framework/driver/ORM/auth provider/port/image, numeric transport policy or new rights are selected.

[[Architecture_Alternatives_and_ADR]] recommends retaining CLI now and a Python-first boundary with logically separate UI after exact decisions; [[Architecture_Owner_Review_Packet]] version POST28-ARCH-ODP-1 proposes choices and A–I impacts without answering them. [[Dependency_Based_Implementation_Roadmap]] separates preview, selected fields/eligibility, genuine principal, read service, shell/pages, media, real methods, private records, dashboard and operations. Factual catalogue access does not require real matching eligibility, but it still needs an authorized accessible scope and field rights.

Current code remains approved Python/operator/SQL tooling plus fixed-fixture synthetic M1/B1. Real records must never be relabelled as synthetic. Genuine nonadmin initial LOGIN, object/field/use rights and current snapshots precede restricted lookup/count/page/scoring/bytes; no admin fetch/filter or browser identity claim. Fit, confidence and direct evidence remain separate. Unknown is not zero; incomplete is not absent. No new live DB/source/media/runtime proof is inferred from historical tests or diagrams.

All 24 prior receipts, eight migrations, accepted contracts, 43 proposals, 44 holds and Khamrah evidence are protected. PR8 remains OPEN/DRAFT/BLOCKED at `84dccb117971ab65e0bf39fa3d1d84a12d344f8d`; no temporal/replay experiment or speculative fix. No acquisition, image bytes, normalization, hold/eligibility change, API/UI/auth/cache/service-worker/framework implementation, installation/configuration, database operation, cloud, Production mutation or agent merge. [[DPT-PLAN-010_Architecture_Verification]] records actual research/static/independent evidence and future NOT RUN tests separately.

Decision classification: PR28 merge is a VERIFIED OWNER EVENT. The new request confirms direction but explicitly withholds exact A/B/I implementation approval. POST28-ARCH-ODP-1 choices and ADR-ARCH-POST28-1 are PROPOSED/UNANSWERED, not accepted by the coordinator. Historical offline-first/stack suggestions are not application/privacy/provider defaults. No new source or asset permission exists.

## DPT-PLAN-010 independent architecture checkpoint — 2026-11-16

Source `68488586be1a3e2edf280dd3eb4a3d16dccd5d60` independently re-reviewed: four initial P2 design findings resolved, four companion correction groups reviewed, zero open documentation findings; 13 named static verification groups. See [[DPT-PLAN-010_System_Architecture_Refinement]] and [[Architecture_Independent_Review.json]]. All new design choices remain PROPOSED; no Owner option acceptance, IMP-ENR-01 start, implementation or Production change. Original failed findings/oracles remain retained. Draft/receipt/handoff publication follows separately.

## Draft publication and immutable planning receipt — 2026-11-16

[PR29](https://github.com/kraveerachat/DoomParfum-By-TK/pull/29) is OPEN/DRAFT; base `168715bc9bc5fff968524074257dc106a8a63638`, pre-receipt publication `938d0d1c9af89a1d857fef54ff041a55302a8a65`, independently reviewed source `68488586be1a3e2edf280dd3eb4a3d16dccd5d60`. One planning-readiness receipt: [[2026-11-16_223118_DPT-PLAN-010_Architecture_Planning]]. Old24 receipts/eight migrations/source/contracts remain unchanged. This records planning readiness only, not Owner acceptance or implementation. Final publication HEAD is in the live PR description/external handoff registry; the receipt will not be rewritten.

Exact changed paths: [[Architecture_File_Manifest.json]]. Fresh final metadata verification and candidate ZIP validation follow; ZIP readiness is not claimed in this checkpoint. All new Owner ARC/A–I choices remain PROPOSED; IMP-ENR-01 not started. PR8 blocked;44 holds/rights/eligibility unchanged; no Production mutation.

## IMP-ENR-01 exact Owner authority and preimplementation gate — 2026-11-17

Current user-provided master prompt explicitly accepts POST27-ODP-1 **A-PREVIEW-5 / B-PINNED-PREVIEW / I-IMP-ENR-01**, ENR-PINNED-SCENTO-1 revision1, frozen data-note canonical SHA256 `053a7583d33beaa103e4cb94781991504aa6eee4b380fefe7cc1d2095f2c71d5`, packet SHA256 `0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c`, transform `enr-pinned-scento-preview-1` and schema `enr-pinned-scento-preview-schema-1`. Only exact five-record/46-field local unselected preview is authorized. Frozen proposal files remain unchanged; this dated decision supersedes only their earlier A/B/I unanswered state. No separate unseen chat statement, human reviewer identity, other policy/ARC acceptance or new source rights are fabricated.

Merged PR28/29 and actual main81b281 satisfy Planning Gate. Fresh independent `/root/enr_architecture_compatibility` review permits bounded TDD; named `/root/enr_independent_data_review` role was assigned before implementation under the current delegated review instruction. Human/canonical acceptance remains pending. Six source pins/sidecars and25prior receipts/eight migrations verified. Current DB/Docker not probed; no service start. Existing tools only; no install/configuration.

Task/branch/source/tests/results: [[IMP-ENR-01_Pinned_Scento_Offline_Preview]], [[IMP_ENR_01_Preflight.json]], [[IMP_ENR_01_Architecture_Compatibility]]. No runtime PASS or final implementation readiness at this checkpoint. PR8 blocked;43proposals/44holds/Khamrah/rights/eligibility untouched; no API/UI/DB/acquisition/real matching/Production or merge.

## IMP-ENR-01 current delivery checkpoint — 2026-11-17

Exact corrected source 4fdbd29b3f345fcbce3eb08862748672657ef22c: independent implementation finding resolved,249offline methods passed,46data slots match with43DEFER/3UNKNOWNsemantic outcomes. One actual ignored private preview is active; no canonical/DB/rights/hold/eligibility/app activation. See [[IMP-ENR-01_Pinned_Scento_Offline_Preview]], [[IMP_ENR_01_Implementation_Boundary]] and exact review/regression evidence. Draft PR/sole receipt/handoff publication follow as delivery steps; Human Owner alone reviews/merges. A/B/I approved only for boundedpreview; other choices remain proposed.

## Draft PR30 and sole implementation receipt — 2026-11-17

[PR30](https://github.com/kraveerachat/DoomParfum-By-TK/pull/30) OPEN/DRAFT, pre-receipt publication9003d08889785fd7f47e3297abacf8531a5ba1a2, reviewed/tested runtime4fdbd29b3f345fcbce3eb08862748672657ef22c. Source/data agent checks complete; Human/canonical acceptance and merge remain PENDING. Sole immutable receipt [[2026-11-17_040641_IMP-ENR-01_Pinned_Scento_Offline_Preview]], all25old receipts unchanged. [[IMP_ENR_01_File_Manifest.json]] lists exact final paths. Final metadata parity/ZIP delivery proofs live outside the frozen ZIP and in PR description; this checkpoint does not claim future archive verification. No source/rights/hold/eligibility/Production expansion. Human Owner alone merges.

## DPT-PLAN-011 post-PR30 authority and new proposals — 2026-11-17

Confirmed event, not policy inference: Owner merged PR30 at4f23cbc858dd818b149674342bfa504e78930088 (UTC05:51:40Z / Bangkok12:51:40). Its accepted offline preview and historical synthetic M1/B1 scopes remain unchanged. Current Owner master prompt authorizes integrated docs/research/static checks/independent review/one Draft Planning PR and handoff synchronization, not implementation or operational/source rights.

New packet [[Post_PR30_Owner_Decision_Packet]] POST30-ODP-1: DATA-01..05, APP-01..07, MEDIA-01..02 and SEQ-01 all **PROPOSED / UNANSWERED**; Owner answers are null. No generic approve-all. A design answer cannot create canonical ACCEPT, completeness, normalization/hold release, image rights, credentials, runtime framework selection or Production authority. Exact packet/hash freeze follows completed independent review; material change needs a new revision/hash and Owner acceptance.

Current data dossier remains43DEFER/3UNKNOWN/0ACCEPT; all44holds/43proposals/Khamrah unchanged. Existing dpt_runtime broad grants/internal adapter are not accepted minimal app authority. Recommend separately accepted genuine initialLOGIN/new private scope and grant/repository contracts before intake, reviewed factual display independent of real eligibility, and placeholders before media. These are recommendations only; no option accepted on behalf of Owner.

## Independent planning review and proposal freeze — 2026-11-17

Original full planning review416/0 at012859 is preserved in [[Post_PR30_Initial_Planning_Review.json]]. Coordinator pre-freeze guard subsequently found P30-INT-001: a Windows checkout CRLF annex hash was incorrectly labelled canonicalLF. Freeze stopped before writes. The correction normalizes checkout bytes to the unchanged Git blob and updates hash references only; all15decision objects and other annexes are unchanged. [[Post_PR30_Integrity_Correction.json]] retains the failure and original review false negative. Focused independent re-review at exact corrected checkpoint `53555db12f179c490ef5d4adfb7eadde62af0a58` passed81checks/0failed/0openfindings, closing that blocker. [[Post_PR30_Independent_Planning_Review.json]] binds actual original final report SHA256be224671b6f0d5e8d1679614e44755bb53db75f9b619cf14ad3a14a2539dfddf. Sixteen official-text observations/12manual groups belong to initial review and are not rerun or added to focused counts. Original416report, failed freeze, reviewer77/2 stat-only attempt, exact before bytes and coordinator661/1 UNANSWERED-oracle error remain retained. Git stat-only refresh changed no bytes/HEAD/config. No runtime or Owner policy changed.

POST30-ODP-1 revision1 is now integrity-frozen after that review, canonical packet SHA256 `e828e0942037793b6d86c73de95b3c3511cba96b25eb267e13fb4f64ae1ed27c`; [[Post_PR30_Packet_Freeze.json]] binds all9normative annexes. Every one of15newdecisions remains PROPOSED/UNANSWERED, not accepted. Framework/provider/version and exact operational/security/source/media contracts remain unselected/gated. No human ACCEPT or runtime operation follows from freeze.

Actual [Draft PR31](https://github.com/kraveerachat/DoomParfum-By-TK/pull/31) is OPEN/DRAFT, base `4f23cbc858dd818b149674342bfa504e78930088`. Initial published source is the reviewed checkpoint above; later metadata-only commits are recorded in the current PR/handoff registry. Agent-side planning review is complete; one immutable readiness receipt and final metadata/archive verification follow actual checks. No future ZIP PASS is claimed here. Historical249methods NOT RERUN, currentDB NOT REVALIDATED,44holds/43proposals/Khamrah/rights/eligibility unchanged; PR8blocked. Human Owner alone answers decisions and merges.

## DPT-GOV-WORKFLOW-001 — proposed governance amendment, 2026-11-20

**PROPOSED, not an Owner decision.** The agent proposes the task-intake classification (A continuation / B new task / C planning amendment / D read-only review), the PR reuse and non-reuse rules, the required session fields and locations, the read-only reviewer exception, the public-repository evidence rules and the credential boundary for remote writes. All are drafted in `AGENTS.md` §2.1/§8.1 and `DEVELOPMENT_WORKFLOW.md` §3.6/§4.3–§4.5/§5.6/§5.7/§6.2.1. They become governance only when the Human Owner merges the Planning PR. The Two-Gate workflow and every existing rule are unchanged. No DPT-GATE-012 item (Q-F, Q-H, BatchA, U01 implementation) is decided. See [[DPT-GOV-WORKFLOW-001_Task_PR_Routing_and_Obsidian_Reporting]].

### DPT-GOV-WORKFLOW-001 — S3 addition, 2026-11-20

**Owner directive received in the session; proposed governance text, not yet in effect.** The Owner directed, in the 2026-11-20 S3 session prompt, that agents publish their own task branches and Draft PRs and that every meaningful session keep a dual Markdown execution report. The agent drafted these as `DEVELOPMENT_WORKFLOW.md` §4.7 (dual execution reports) and §5.6 (responsibility split, agent publishing identity, `AGENT_CREDENTIAL_REQUIRED`), with summaries in `AGENTS.md` §8.1. The rules take effect when the Owner merges this Planning PR. Still open, for the Owner: which agent publishing identity to provision (GitHub App or dedicated machine user) and the repository rules on `main`. Nothing about DPT-GATE-012 is decided. See [[DPT-GOV-WORKFLOW-001_Task_PR_Routing_and_Obsidian_Reporting]].

## DPT-GOV-WORKFLOW-001 — Owner GitHub publishing policy — 2026-11-21 S4

Owner decisions given in the agent chat on 2026-11-21 (the channel is not independently authenticated):

- **Hybrid GitHub workflow.** The default is a dedicated, appropriately restricted agent GitHub identity whenever one is available. As an exception, the Owner may authorize specific operations through the Owner's own login, case by case. Each exception is limited by repository, branches, allowed operations, duration or session, and prohibited operations, and it is never permanent.
- **First exception (used in S4 here and in DPT-GATE-012 / U01 S7):** Owner login; this branch and `docs/dpt-gate-012-security-history`; push, one Draft PR each to `main` ([PR33](https://github.com/kraveerachat/DoomParfum-By-TK/pull/33), [PR32](https://github.com/kraveerachat/DoomParfum-By-TK/pull/32)), documentation checkpoints, verification. Prohibited: push to `main`, merge, auto-merge, force-push, branch deletion, settings, ruleset or credential changes, production or security-gate operations, unrelated writes. It expires when both PRs and checkpoints are complete.
- **Proceed despite the missing "Restrict updates" rule** (explicit Owner confirmation). It is an **OPEN configuration item**: resolve it before granting any write-capable agent identity and before the final merge.
- **Residual risk:** an administrative Owner credential was used, with its limits enforced by agent procedure rather than technically. Owner-account authorship is not security attestation.
- **Effect on this PR:** DW §5.6 already treats Owner-run publication as an exception. Explicit Hybrid wording is an Owner review point; it is not changed here.

## DPT-GOV-WORKFLOW-001 — Owner reporting model — 2026-11-22 S5

**Owner instruction received in the agent chat (not independently authenticated; provisional until this PR is merged):**

- Every meaningful writable agent session keeps one full execution report, one short session summary and one update of the living canonical task overview, all in `Structure DB Obsidian/`, public-safe or sanitized.
- Sensitive full reports and private security artifacts go only to a separately Owner-approved private vault outside every Git repository, never to public GitHub, and no longer to persistent `Downloads` mirrors. The S3 dual-report rule is withdrawn.
- The private vault's existence, custody and backup status are recorded in the Owner's private OCD record, without publishing its path; until verified they are PENDING.
- The final immutable receipt remains one per completed reviewable task.
- Prefer Claude Code for high-complexity architecture, security and history work and Codex for bounded implementation, tests and fixes, without waiving approval gates or reviewer independence.

Proposed governance text: DW §4.7 and AGENTS §8.1 (S5). In effect only after the Owner merges PR33. See [[DPT-GOV-WORKFLOW-001_Task_PR_Routing_and_Obsidian_Reporting]] Session S5.

## DPT-GOV-WORKFLOW-001 — one-time publication of the S5 checkpoint — 2026-11-22 S6

**Owner decision given in the agent chat on 2026-11-22 (the channel is not independently authenticated):** a second one-time, narrowly scoped exception under the Hybrid policy (2026-11-21 S4 entry above).

- **Allowed:** with the Owner's GitHub login, push the existing S5 commit `8902bb7` to `plan/agent-workflow-pr-routing` and update the [PR33](https://github.com/kraveerachat/DoomParfum-By-TK/pull/33) description from the prepared public-safe body; verify the result.
- **Prohibited:** additional commits or branches, merge, auto-merge, force-push, changes to `main`, repository settings or branch protection, PR32, PR8, the r14 worktree, private security artifacts, and runtime, Docker, database or security tests.
- **Expiry:** immediately after that publication. It was used once (Session S6 records the outcome) and does not cover the S6 checkpoint.
- **Not decided here:** how the one approving review required by the `main` rules is obtained, and whether "Restrict updates" is configured before the merge. Both remain Owner decisions.

## DPT-GATE-012 / U01 decision state, recovered — 2026-11-20

Recorded by `DPT-DOC-RECOVERY-001`. No decision ID is allocated, and nothing here is an Owner decision.

**VERIFIED OWNER EVENTS relevant to U01:** none. The only verified event in this history is the GitHub merge of PR31 (2026-11-17T14:02:10Z at `183f1d857d83b64819762a2237c908fb95e36cb4`), which approved the POST30-ODP-1 planning packet for review only and decided nothing about U01.

**Owner directions reported by agents, not independently verified:** "Owner items 1–5" applied in r3 (reported by the r3 author); the r10 output folder and the instruction to proceed without the frozen r8/r7 copies (reported by the r10 author); the review and recovery assignments for r7–r11. Under r11 PG-1, a chat or GitHub action is not proof of an Owner decision.

**PROPOSED / PENDING (unchanged):** approval of any revision r1–r11; Q-F; BatchA with acknowledgements of the R7-IR-08 availability, SHA-1 object-identity and pre-OP-1 governance-channel residuals; Q-H rows; Planning PR for U01 (W-01); BatchB; OP-1 (E1–E10), OP-2 (F1–F12), OP-2-TOOL; Q-A1…Q-A7, Q-B…Q-G; DATA-01, DATA-04, D3/SEQ-01, CONTRACT, TASK-ID. Contract recommendations (OP1-A/OP2-A dedicated machine, `sk-ssh-ed25519`, validity windows, MANUAL preparation) and the r11 review's recommendations (narrow r12; different-model or human reviewer; OPR-1/OPR-2/OPR-3) are proposals only.

**Gate state:** latest candidate r11; latest review CONDITIONAL, advisory; G-IND NOT SATISFIED; R11-IR-01 and R11-IR-02 OPEN; r12 NOT STARTED; implementation NOT AUTHORIZED. See [[DPT-GATE-012_U01_Security_Gate]].

## DPT-GATE-012 / U01 decision state — 2026-11-20 S4

No decision ID is allocated, and nothing here is an Owner decision.

- **Owner directions reported through the agent chat channel, not independently verified:** commission r12 and prepare it in a new session; keep one main Draft PR for the U01 documentation workstream; Option A, a dedicated GitHub App or agent identity for publication; keep DPT-GOV-WORKFLOW-001 as a separate PR.
- **PROPOSED / PENDING (unchanged):** approval of any revision r1–r12; the r12 reviewer; Q-F; BatchA and its acknowledgements; Q-H; BatchB; OP-1 (E1–E12 in r12); OP-2; Q-A1…Q-A8; CONTRACT.
- **Gate state:** latest candidate r12 (PROPOSED, not reviewed); latest completed review r11, CONDITIONAL and advisory; G-IND NOT SATISFIED; R11-IR-01…09 ADDRESSED IN PROPOSED TEXT only; implementation NOT AUTHORIZED. See [[DPT-GATE-012_U01_Security_Gate]] §7.1.

## DPT-GATE-012 / U01 — Owner publication decision — 2026-11-21 S7

Owner decisions given in the agent chat on 2026-11-21 (the channel is not independently authenticated):

- **Hybrid GitHub workflow.** Agents use a dedicated, restricted GitHub identity when one is available. The Owner's own login may be used only through explicit, case-by-case exceptions limited by repository, branches, operations, duration and prohibitions. An exception is never permanent.
- **One-time publication exception (used in S7).** Owner login, repository `kraveerachat/DoomParfum-By-TK`, branches `docs/dpt-gate-012-security-history` and `plan/agent-workflow-pr-routing` only. Allowed: push both branches; one Draft PR each to `main` (results: [#32](https://github.com/kraveerachat/DoomParfum-By-TK/pull/32), [#33](https://github.com/kraveerachat/DoomParfum-By-TK/pull/33)); documentation checkpoints to the same branches; verification. Prohibited: direct push to `main`, merge, auto-merge, force-push, branch deletion, settings, ruleset or credential changes, production or security-gate operations, unrelated writes. It expires when both PRs and checkpoints are complete, and it does not authorize future sessions or identities.
- **Proceed despite the missing "Restrict updates" rule** (explicit Owner confirmation). The rule is recorded as an **OPEN governance/security configuration item**, to be resolved before granting any write-capable agent identity and before the final merge. Owner-only merge enforcement is not complete.
- **Residual risk accepted by the Owner:** an administrative Owner credential was used, with its limits enforced by agent procedure rather than technically. The PRs are Owner-authored, which is not security attestation (PG-1). No independent trust root is established.

Unchanged: r12 PROPOSED; independent review PENDING; G-IND NOT SATISFIED; Q-F PENDING; BatchA and Q-H NOT AUTHORIZED. See [[DPT-GATE-012_U01_Security_Gate]] §16.

## DPT-GATE-012 / U01 — Owner private-storage decision — 2026-11-22 S8

Owner decision given in the agent chat on 2026-11-22 (the channel is not independently authenticated; provisional under PG-2):

- **Private vault.** Full private U01 contracts, author tooling and complete author reports go to a new, dedicated private Obsidian vault outside every Git repository (path deliberately not published). The public project vault receives only separately written, sanitized summaries that cite hashes.
- **No new Downloads copies.** From r14 onward, no new persistent copy or handoff folder is created in the download folder; existing Downloads files are read only as historical inputs.
- **Open governance item:** the unmerged DPT-GOV-WORKFLOW-001 amendment (Draft PR #33) still names `Downloads\<TOPIC_ID>\Responses\` for private reports; the Owner decides how to align it.

Unchanged: r14 PROPOSED; independent review PENDING; G-IND NOT SATISFIED; Q-F PENDING; BatchA, BatchB and Q-H NOT AUTHORIZED. See [[DPT-GATE-012_U01_Security_Gate]] §17.

## DPT-GATE-012 / U01 — documentation closeout scope — 2026-11-22 S9

**Owner instruction given in the agent chat on 2026-11-22 (the channel is not independently authenticated; provisional under PG-2):**

- [PR #32](https://github.com/kraveerachat/DoomParfum-By-TK/pull/32) is completed as a **SECURITY_DOCUMENTATION_SNAPSHOT / PROPOSED DESIGN / NOT APPROVED**: its criterion is an accurate, public-safe record of the U01 history and continuation plan, not security approval. Merging it confirms only the documentation snapshot.
- Status to record: latest candidate PROPOSED r14, NOT APPROVED; R13-IR-01/02/03 addressed in proposed text, independent disposition pending; R14-AR-01 author-identified LOW, proposed correction, independent disposition pending; G-IND NOT SATISFIED; Q-F PENDING; 0 of 169 acceptance specifications executed; no security implementation authorization.
- Integrate the merged `main` by a non-destructive merge that keeps both histories; no rebase, reset or force-push; no r15, runtime test, Docker or database operation for the closeout.

**Not decided here:** the r14 reviewer, Q-F, every later gate, the PR8 disposition and the overall handoff PR. See [[DPT-GATE-012_U01_Security_Resumption_Handoff]] §5.

## PR8 / IMP-P1-04 disposition — 2026-11-23 (closeout Stage 4)

**Owner decision given in the agent chat on 2026-11-23 (the channel is not independently authenticated; provisional under PG-2):**

- Accept the Stage 3 recommendation ([[2026-11-23_IMP-P1-04_S6_Report]]) to **defer [PR #8](https://github.com/kraveerachat/DoomParfum-By-TK/pull/8) without merging**, but **keep PR #8 OPEN / Draft** instead of closing it. This overrides the closing step of Stage 3 disposition A; the proposed closing comment is not posted.
- Record PR #8 as BLOCKED / DEFERRED / NOT MERGED / NOT ACCEPTED. Its branch, source code and historical evidence stay preserved for future reassessment. No timestamp fix, database experiment, rebase, merge or push.

**Not decided here:** PR #8 reassessment; TSK-101 retirement or re-scoping; any UI, backend or ORM selection (POST30-ODP-1 stays unanswered); the first web task's scope. See [[2026-11-23_DPT-DOC-004_Overall_Project_Handoff]] §7.

## DPT-PLAN-012 design-planning decisions — 2026-11-23

The Owner confirmed the attached luxury editorial direction in chat: ivory/ink, muted gold, deep navy, serif display, readable sans, generous spacing and restrained motion. This confirms the direction to propose, not rendered acceptance. [[Luxury_Frontend_Acceptance_and_Task_Map]] records LF-OD-01…05. Exact routes/tokens, isolated Next.js stack and loopback Docker runtime remain PROPOSED until Gate P. Public link access/noindex is a future preference; Cloudflare deployment remains separately gated. Gold `#AD9361` on ivory measures 2.706:1 and is restricted to decorative use; readable gold is separately proposed. No prior decision, U01 contract or data permission is changed.

## IMP-WEB-01 decisions — 2026-11-24

Owner-verified (chat, 2026-11-24): consolidate LF-01 to LF-04 into one implementation task with LF-05 as a separate gate; one Docker Desktop launch. PROPOSED, awaiting the Owner: the deviations numbered 1 to 7 in [[2026-11-24_IMP-WEB-01_S1_Report]] (route-loading behavior, hero padding, fixed optical size, dialog exit, accord descriptors and sort options, link size, house-label position).

## IMP-WEB-01 S3 decisions — 2026-11-25

Owner-verified (chat, 2026-11-25): one bounded stop and replacement of the `doomparfum-web` preview for A11, ending on the S3 image. PROPOSED and PENDING: deviations 1 to 7, the S2 interpretations, the S3 no-script row and method refusal, the response-header exceptions and A05 deferral, as listed in [[2026-11-25_IMP-WEB-01_S3_Report]].

## 2026-11-25 — IMP-WEB-01 S4 recovery/publication reconciliation

Verified Owner decisions from the actual PR36 body at published cda91ff, plus current explicit recovery/records instruction. Earlier PENDING rows are dated history, not current decisions.

| # | Item | Decision |
|---|---|---|
| 1 | Route loading retains the current page | ACCEPTED |
| 2 | Responsive hero padding takes precedence over the conflicting fixed padding and viewport requirements | ACCEPTED |
| 3 | Fixed optical font size | ACCEPTED |
| 4 | No Radix overlay part | ACCEPTED |
| 5 | Accord descriptors and sorting behavior | ACCEPTED |
| 6 | 16px text links | ACCEPTED |
| 7 | House-label position | ACCEPTED |
| 8 | Tablet 4:3 imagery, horizontal third Featured entry, `proxy.ts` redirect architecture | ACCEPTED |
| 9 | No-JavaScript navigation fallback, HTTP 405 for unsupported write methods | ACCEPTED |
| 10 | Documented framework/HTTP-layer header and redirect exceptions | ACCEPTED, loopback-only synthetic preview |
| 11 | Unavailable A05 manual checks | EXPLICITLY DEFERRED for this stage; A05 stays PARTIAL |

Scope: current loopback synthetic mock only. No full WCAG/final acceptance/Production/public exposure/real-data rights. The initial publication exception was used/exhausted. Current new exception authorizes one records-only commit/normal push plus corresponding PR36 description update, using existing Owner authentication only because no approved agent identity is available; no continuing authority after completion. No final receipt; no agent merge. [[IMP-WEB-01_Luxury_Frontend_Docker]], [[2026-11-25_IMP-WEB-01_S4_Report]], [[2026-11-25_IMP-WEB-01_S4_Summary]].
