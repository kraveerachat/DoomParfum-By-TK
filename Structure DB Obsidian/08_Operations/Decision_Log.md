---
id: DPT-OPS-001
project: DoomParfum By TK
type: decision_log
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - operations
  - decisions
  - governance
source_of_truth: "../README.md"
---

# Decision Log — DoomParfum By TK

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
| **DEC-009** | ใช้ Obsidian Markdown Vault สำหรับ Living Documentation และใช้ GitHub สำหรับ Version Control (รอ Workflow) | **CONFIRMED** | 2026-11-10 | [[Project_Index]], [[GitHub_and_Workflow_PENDING]] |
| **DEC-010** | ใช้ Two-Gate Development Workflow (Gate P: Planning PR -> Human Merge -> Gate I: Implementation PR -> Human Merge) | **PROPOSED-CANONICAL** | 2026-11-10 | `../DEVELOPMENT_WORKFLOW.md`, [[GitHub_and_Workflow_PENDING]] |
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
