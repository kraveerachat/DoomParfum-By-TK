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
