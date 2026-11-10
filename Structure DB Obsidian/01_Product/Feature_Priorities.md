---
id: DPT-PRD-004
project: DoomParfum By TK
type: feature_priorities
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - product
  - priorities
  - roadmap
source_of_truth: "../README.md"
---

# Feature Priorities — DoomParfum By TK

> **Document Type:** Feature Prioritization & Phasing
> **Source Baseline:** `../README.md` (Sections 2 and 8)
> **Status:** Draft / Proposed Phasing

---

## 1. Overview & Phasing Strategy

โครงการแบ่งการพัฒนาออกเป็น 7 ระยะ (Phase P0 ถึง P6) ตามหลักการ **Documentation-First** โดยเน้นการสร้างฐานรากของข้อมูล (Data Foundation) ก่อนการพัฒนาเครื่องมือคำนวณความคล้าย (Matching) และระบบจัดการตะกร้า/คอลเลกชันส่วนตัว

> [!IMPORTANT]
> ฟีเจอร์ทั้งหมดที่อยู่ในสถานะ `[CONFIRMED]` จะไม่ถูกตัดทิ้ง แต่จะถูกจัดสรรลงในเฟสที่เหมาะสมตามความพร้อมของข้อมูลและสถาปัตยกรรม

---

## 2. Feature Prioritization Matrix

```mermaid
quadrantChart
    title Feature Priority vs Complexity
    x-axis Low Complexity --> High Complexity
    y-axis Low Priority --> High Priority
    quadrant-1 Quick Wins (MVP Core)
    quadrant-2 Major Investments
    quadrant-3 Nice-to-Have / Later
    quadrant-4 Advanced / Long Term
    "Catalogue & Pyramid Notes (P1)": [0.35, 0.90]
    "My Cart & Multi-Source Links (P3)": [0.40, 0.88]
    "Manual Ordered / Owned Tracking (P3)": [0.30, 0.85]
    "Side-by-Side Compare (P2)": [0.45, 0.82]
    "Rule-based Scent Matching (P2)": [0.65, 0.80]
    "Collection Dashboard (P4)": [0.50, 0.75]
    "Thai Brand Registry Expansion (P1/P6)": [0.30, 0.78]
    "AI Research Assistant (P5)": [0.80, 0.60]
    "Spending Analytics per mL (P4 - R31)": [0.55, 0.35]
    "ML Learning-to-Rank (Deferred)": [0.90, 0.25]
```

---

## 3. Detailed Phase Breakdown

### Phase P0: Documentation & Governance (ระยะปัจจุบัน)
- **เป้าหมาย:** สถาปัตยกรรมเอกสาร living documentation ใน Obsidian Vault เชื่อมโยงข้อกำหนด R01–R31
- **ฟีเจอร์หลัก:**
  - ข้อกำหนดและ Traceability Matrix ครบถ้วน
  - Draft ERD & Data Dictionary
  - Scent Matching Formulation (Proposed)
  - UX Site Map & Screen Specs

### Phase P1: Foundation & Catalogue MVP
- **เป้าหมาย:** ระบบค้นหาและแสดงรายละเอียดน้ำหอมพื้นฐาน พร้อมภาพพีระมิดโน้ต
- **ฟีเจอร์หลัก:**
  - แคตตาล็อกน้ำหอมสากลและแบรนด์ไทยนำร่อง (R01, R06, R20, R22)
  - อนุกรมวิธานแยก Country vs Market Position (R02)
  - โครงสร้าง Top/Heart/Base Notes และ Accords (R03)
  - หน้า Perfume Detail พร้อมภาพพีระมิดโน้ต (R13)
  - ฟังก์ชันคลิกที่ Note เพื่อค้นหารุ่นที่มีโน้ตเดียวกัน (R14)
  - ตัวกรองเบื้องต้น: Day/Night, การใช้งาน, เพศ, งบประมาณ (R04, R08)
  - ระบบตรวจสอบสิทธิ์และที่มาของข้อมูล (R21)

### Phase P2: Scent DNA Matching & Comparison
- **เป้าหมาย:** เครื่องมือช่วยค้นหาตัวเลือกกลิ่นใกล้เคียงและเปรียบเทียบเชิงโครงสร้าง
- **ฟีเจอร์หลัก:**
  - เลือกรุ่น Designer/Niche เพื่อหาทางเลือกในงบ (R05)
  - เปรียบเทียบสองรุ่นแบบเคียงข้าง Side-by-Side (R15)
  - คำนวณความคล้ายเชิงโครงสร้างตามสูตร Note Pyramid + Accords + Family (R16, R18)
  - แสดงหลักฐานและรีวิวประกอบที่ตรวจสอบสิทธิ์แล้ว (R17)

### Phase P3: My Cart & Personal Shopping Tracker
- **เป้าหมาย:** จัดการรายการที่สนใจ แหล่งซื้อ Shopee และการเปลี่ยนสถานะด้วยมือ
- **ฟีเจอร์หลัก:**
  - ตะกร้าในแอป `My Cart` สำหรับทุกแบรนด์ (R23)
  - บันทึกลิงก์ร้านค้าภายนอก (Shopee), ราคา, ขนาด ได้หลายร้าน (R10, R24)
  - นำเข้าข้อมูลด้วยตนเอง (Manual import, URL, text notes) (R09)
  - ระบบแจ้งเตือนบันทึกซ้ำใน Cart และแนะนำให้เพิ่มลิงก์ร้านแทน (R30)
  - เปลี่ยนสถานะเป็น `Ordered` และ `Owned` ด้วยมือ (R11, R25)
  - แยก `purchase_records` ถาวรออกจาก `inventory_items` (R26, R28, R29)

### Phase P4: Collection Dashboard & Personal Insights
- **เป้าหมาย:** สรุปข้อมูลภาพรวมการครอบครองและประวัติการซื้อในอดีต
- **ฟีเจอร์หลัก:**
  - แดชบอร์ดสรุป Ever Purchased vs Currently Owned (R27)
  - การแจกแจงสถิติตามแบรนด์ ตระกูลกลิ่น และโน้ตเด่น
  - [DEFERRED / OPTIONAL] สถิติค่าใช้จ่ายและราคาเฉลี่ยต่อ mL (R31)

### Phase P5: AI Research Assistant & Ingestion Pipeline
- **เป้าหมาย:** ไปป์ไลน์นำเข้าข้อมูลที่มีการตรวจสอบคุณภาพ และผู้ช่วย AI
- **ฟีเจอร์หลัก:**
  - ผู้ช่วย AI สรุปข้อมูลและอ้างอิงหลักฐาน (R12)
  - ระบบ Ingestion/ETL นำเข้าข้อมูลจากแหล่งที่ได้รับอนุญาต (R19)

### Phase P6: Expansion & Community Calibration
- **เป้าหมาย:** เพิ่มความครอบคลุมของแบรนด์ไทย อาหรับ อินโดนีเซีย
- **ฟีเจอร์หลัก:**
  - ขยาย Thai Brand Registry อย่างเต็มรูปแบบ (R22)
  - ขยายแคตตาล็อก Middle Eastern & Indonesian Houses
  - ปรับจูนค่าน้ำหนักการจับคู่ตามผลตอบรับผู้ใช้จริง

---

## 4. Change Notes

- `2026-11-10`: กำหนดลำดับความสำคัญและจัดกลุ่มฟีเจอร์ R01–R31 ลงในเฟส P0–P6 ครบถ้วน
