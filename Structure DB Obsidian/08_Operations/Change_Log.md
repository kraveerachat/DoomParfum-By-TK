---
id: DPT-OPS-002
project: DoomParfum By TK
type: change_log
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - operations
  - changelog
  - history
source_of_truth: "../../README.md"
---

# Change Log — DoomParfum By TK

> **Document Type:** Project Evolution & Specification Change History
> **Source Baseline:** `../README.md`
> **Status:** Active Change Log

---

## 1. Version History

### [Version 0.2.0-planning] — 2026-11-10
**ผู้บันทึก:** TK & Agent Architecture Team
**ประเภทการเปลี่ยนแปลง:** Major Requirement & Architecture Expansion

#### รายการเปลี่ยนแปลงสำคัญ:
1. **เพิ่มข้อกำหนดกลุ่ม Shopping & Ownership (R23 ถึง R31):**
   - **R23:** ยืนยันการเพิ่มน้ำหอมทุกแบรนด์เข้าสู่ `My Cart` ภายในแอป
   - **R24:** อนุญาตให้บันทึกลิงก์ร้านค้าภายนอก (Shopee) หลายร้านต่อหนึ่งน้ำหอม พร้อมโน้ตความน่าเชื่อถือ
   - **R25:** กำหนดกระบวนการเปลี่ยนสถานะเป็น "สั่งซื้อแล้ว (Ordered)" ด้วยมือของผู้ใช้เอง (Manual Transition)
   - **R26:** รับรองการเก็บบันทึกประวัติการซื้อถาวร แม้น้ำหอมขวดนั้นจะถูกใช้หมด ขายต่อ หรือยกให้ผู้อื่น
   - **R27:** กำหนดสเปกหน้าจอ Collection Dashboard แสดงข้อมูล Ever Purchased vs Currently Owned
   - **R28:** แยกโครงสร้างตาราง `purchase_records` ออกจาก `inventory_items` เพื่อรองรับการซื้อซ้ำหลายครั้ง
   - **R29:** กำหนดฟิลด์ข้อมูลการซื้อจริง (ราคา, ขนาด, ร้าน, วันที่) เป็นฟิลด์เสริมที่ไม่บังคับ (Optional)
   - **R30:** เพิ่มระบบแจ้งเตือนเมื่อผู้ใช้พยายามบันทึกน้ำหอมเดียวกันซ้ำใน Cart และแนะนำให้เพิ่มลิงก์ร้านค้าแทน
   - **R31:** วางโครงสร้างสถิติการใช้จ่ายเฉลี่ยต่อ mL เป็นฟีเจอร์ระยะยาว (Deferred)
2. **ขยาย Thai Brand Registry (R22):**
   - บรรจุ 4 แบรนด์ไทยหลักอย่างเป็นทางการ: **La Palette (lapalette), SCENTERY, BE CHERIE PARFUM, SÚNDALO**
   - บันทึกตัวอย่างรุ่นโฟกัสจากผู้ใช้: `BE CHERIE White Instinct`, `SÚNDALO Rhapsody Sky`
3. **จัดตั้งโครงสร้าง Obsidian Vault (Structure DB Obsidian):**
   - แยก 11 โฟลเดอร์ (00_Home ถึง 90_Templates) พร้อมเชื่อมโยง MOC และ Internal Links ครบถ้วน
   - จัดทำสัญญาการทำงาน (Operating Contract) และข้อห้ามเรื่อง Mass Scraping / Auto-Deploy

---

### [Version 0.1.0-discovery] — 2026-11-09
**ผู้บันทึก:** TK
**ประเภทการเปลี่ยนแปลง:** Initial Discovery & Baseline Blueprint

#### รายการเปลี่ยนแปลง:
- กำหนด Product Vision เบื้องต้น: เว็บแอปส่วนตัวสำหรับการศึกษาวิจัยและเปรียบเทียบน้ำหอม
- ร่างข้อกำหนดเริ่มต้น R01 ถึง R22 (Catalogue, Search, Pyramid Notes, Scent Matching)
- กำหนดหลักการ Non-goals: ไม่ทำระบบชำระเงินจริง ไม่ใช่ Marketplace
- กำหนดกรอบงบประมาณเริ่มต้น <= ฿2,000 ต่อขวด

---

## 2. Governance Rules for Future Changes

1. ทุกการปรับเปลี่ยนข้อกำหนด (Requirements), แบบจำลองข้อมูล (ERD/Schema), หรือการตัดสินใจ (Decisions) จะต้องถูกบันทึกในเอกสารนี้เสมอ
2. ระบุเลขเวอร์ชัน, วันที่, เหตุผล, และรายการข้อกำหนดที่ได้รับผลกระทบ
3. หากมีข้อขัดแย้งกับเอกสารเดิม ให้ทำบันทึกชี้แจง (Reconciliation Note) ไม่แก้เอกสารเงียบๆ


### P1 discovery and foundation proposal — 2026-11-10 / DPT-PLAN-001

Docs-only planning change, not a product/runtime release. Profiled pinned CC BY 4.0 Scento export;
added research findings, source-to-canonical mapping and observed conflict matrix. Replaced draft data
contracts with a 44-table logical proposal covering catalogue, provenance/rights/conflicts/staging,
media/evidence, personal listings/cart/purchases/inventory. Added hosting/object-vs-DB recovery evaluation,
ADRs 003–006, pilot task/test/readiness plan and canonical planning/task notes.

Reconciled roadmap/status/root overview with actual public repository/bootstrap and two-gate request.
Aligned domain concentration/packaging and matching-result semantics; corrected public-info/fair-use
assumptions and required-country/three-note defaults. Preserved existing confirmed requirements and
proposed matching weights. No raw dataset, code, SQL, cloud configuration, secret, merge or deployment.
Research gaps/permission constraints remain explicit, especially priority Thai samples, HMNS reuse,
image acquisition and live API response verification. Exact files/checkpoints: [[DPT-PLAN-001_P1_Data_Foundation]].


### Post-Review Correction S2 — 2026-11-10 / DPT-PLAN-001 / existing PR #1

Review start/current verified HEAD: `46c4a85309c408b3de7612d4853b166b84917359`; main unchanged at
`03481f7066487c44631cb9065899894ee8db71fb`. Same planning branch, PR OPEN/DRAFT.
R1: locator/occurrence identity preserves multiple claims per source record; scoped exact selection
and conflict-member resolution constraints. R2: non-null access_scope_id throughout provenance/assets,
public/shared/private ownership, RLS/API/storage rules, private overlays never materializing public data.
R3: scoped per-asset/capture/assessment grant, derivative parent/output rights and expiry/revocation checks.
Logical proposal grows 44 → 47 tables; original source profiling/mapping/conflict evidence and Task Map
retained. R4: public repository/existing workflow facts corrected in security/workflow/questions;
separate documentation CI backlog proposal only. Added 18 future OBS/ACL/IMG/REC negative/positive case
specifications and four-column OD-01..06 local/test/rights/cloud owner recommendations. No runtime tests.

Original immutable receipt [[2026-11-10_201028_DPT-PLAN-001_P1_Planning]] remains the single receipt;
no rewrite/second receipt. Exact correction paths and resulting checkpoint/evidence are in
[[DPT-PLAN-001_P1_Data_Foundation]]. No code, schema/database, Actions, cloud resources, deployment or merge.


S2 CURRENT_VERIFIED_HEAD_SHA / reviewed correction checkpoint: `83f13599a1b531229f22e0a68d35f86edd19278a`.
Observed after `docs(p1): address architecture review findings` committed 25 Markdown files. This
append-only event is included in the following documentation closeout checkpoint; final published branch/PR SHA is
in PR #1/final report. No rewrite of the original immutable receipt and no second receipt. Verified
25 docs, 23 vault frontmatters, 47 ERD/dictionary tables, 18 future cases; links/fences/diff/secret-pattern
checks succeeded. Runtime tests NOT RUN; R1–R4 resolved as proposals, owner decisions/rights still pending.


### Owner Decision Recording S3 — 2026-11-10 / DPT-PLAN-001 / PR #1

START/verified PR HEAD: `88de01f8cdf42680f50696350abdb9fd80f6c4c2`; main remains
`03481f7066487c44631cb9065899894ee8db71fb`. Authority is the Human Owner's current explicit decision
message, not an agent-inferred acceptance. OD-01..06 approved only for bounded local international
licensed-data pilot and model/metadata/rights/recovery targets. ADRs and planning/current status now
separate local approval, pending SQL/RLS tests, deferred permanent cloud/storage/final retention/RPO/RTO/
external backups, and regional imports blocked by usable rights plus samples. Existing source dataset
license evidence is not altered; local adoption approved with attribution, no wider content/image grant.
Source registry, pilot/backlog and overview/handoff scope summaries synchronized to prevent stale gates.

Gate P remains unsatisfied until Human Owner merges PR #1. This round is docs only; no SQL, database,
application code, cloud resources, Actions, provisioning/deployment/merge. Original immutable receipt
and research/Task Map preserved; no second receipt or new PR. Current exact paths and verification
are in [[DPT-PLAN-001_P1_Data_Foundation]]. Final published head recorded by existing PR/final report.

S3 validation result: 12 Markdown / 11 vault frontmatters / six matching owner-decision rows / 47-table
parity / zero errors; links/fences/source paths and common secret patterns checked; git diff check exit 0.
Receipt/research/schema-document hashes and original Task Map preserved; one receipt. Documents ready
for Owner Review, not runtime-verified/merged. Final same-branch commit/push and existing PR description
readback provide published SHA/state; no implementation or automatic merge.


## 2026-11-10 — IMP-P1-01 — local schema implementation / review checkpoint

Planning PR #1 owner-merge bffb2fab1918dc5221a6c5da7920168bcae263ca verified; implementation branch
impl/p1-01-local-postgres-schema starts there. Seven local migration groups implement all 47 logical
names, named constraints, scoped claims/private owners, whole-field/conflict/asset gates and RLS.
Actual current evidence: 63/63 tests via python database/verify.py, exit 0; 47 PK / 141 FK / 91 UNIQUE /
82 table CHECK / 58 deferred constraint-trigger constraints; 47 FORCE RLS tables, 203 policies.
Five domain checks/396 NOT NULL columns/244 indexes/195 user triggers measured separately.
Local foundation contains 53 field definitions and zero other domain rows; no full import or ETL.
Raw package hashes verified; 40 repeated-note groups/39 profiles preserved for review, exact real 12/5/58
shape fixtures roll back. Conservative findings, partial/not-run coverage and observed RED/fixes are in
[[IMP-P1-01_Implementation_Evidence]] and database/schema_findings.md.
Current planning-merge status reconciled; original research/Task Map/immutable planning receipt retained.
No new source rights, cloud/provider/storage, final retention/RPO/RTO, regional import or CI approval.
No main push, production mutation, merge, deployment, raw/private/dump/backup publication.
Independent exact-checkpoint review and final task receipt/Draft PR publication are next, not claimed done.
Exact resulting SHA will be recorded after commit, never invented self-referentially.
