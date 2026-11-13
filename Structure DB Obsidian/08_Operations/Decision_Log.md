---
id: DPT-OPS-001
project: DoomParfum By TK
type: decision_log
status: draft
owner: project
updated: 2026-11-14
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
