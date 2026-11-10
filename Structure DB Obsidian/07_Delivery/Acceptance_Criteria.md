---
id: DPT-DEL-003
project: DoomParfum By TK
type: acceptance_criteria
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - delivery
  - qa
  - acceptance_criteria
source_of_truth: "../../README.md"
---

# Acceptance Criteria — DoomParfum By TK

> **Document Type:** Quality Assurance & Verifiable Acceptance Tests
> **Source Baseline:** `../README.md` (Sections 2 & 7)
> **Status:** Draft / Active Verification Criteria

---

## 1. Overview

เอกสารนี้ระบุเกณฑ์การตรวจรับงาน (Acceptance Criteria) ที่สามารถทดสอบและวัดผลได้จริง (Verifiable & Testable) สำหรับแต่ละฟังก์ชันหลักของระบบ เพื่อให้ผู้ใช้และทีมงานสามารถตรวจสอบความถูกต้องก่อนการส่งมอบงานในแต่ละระยะ

---

## 2. Verifiable Criteria by Functional Area

### 2.1 Catalogue, Search & Detail (P1)
- [ ] **AC-CAT-01 (Multi-criteria Search):** ผู้ใช้สามารถค้นหาตามชื่อรุ่นหรือแบรนด์ และใช้ตัวกรองช่วงราคา (<= ฿2,000), เพศ (Men/Women/Unisex), และช่วงเวลา (Day/Night) แล้วผลลัพธ์แสดงเฉพาะรายการที่ตรงเงื่อนไข
- [ ] **AC-CAT-02 (Pyramid Visuals):** หน้ารายละเอียดน้ำหอมแสดงโครงสร้าง Top, Heart, และ Base Notes เป็นชั้นรูปภาพการ์ดชัดเจน พร้อมแสดงชื่อสากลและคำแปลไทย
- [ ] **AC-CAT-03 (Interactive Note Click):** เมื่อผู้ใช้คลิกที่การ์ดโน้ตใดๆ (เช่น Bergamot) ระบบต้องนำทางไปยังหน้ารวมน้ำหอมที่มีโน้ตนั้นได้อย่างถูกต้อง
- [ ] **AC-CAT-04 (Thai Brand Presence):** แคตตาล็อกต้องมีแบรนด์ไทยขั้นต่ำ 4 แบรนด์ ได้แก่ La Palette, SCENTERY, BE CHERIE PARFUM, SÚNDALO
- [ ] **AC-CAT-05 (Manual Add):** ผู้ใช้สามารถเพิ่มน้ำหอมรุ่นที่ไม่มีในระบบด้วยตนเองได้ โดยระบุชื่อรุ่น แบรนด์ และโน้ตเบื้องต้น

---

### 2.2 Scent Matching & Comparison (P2)
- [ ] **AC-MAT-01 (Alternative Lookup):** เมื่อเลือกรุ่นอ้างอิง (เช่น Dior Sauvage) ระบบสามารถแสดงรายการน้ำหอมทางเลือกในงบประหยัดที่แนะนำได้
- [ ] **AC-MAT-02 (Side-by-Side Highlight):** หน้าจอเปรียบเทียบแสดง 2 คอลัมน์เคียงข้าง ไฮไลต์สีเขียวที่โน้ตที่ตรงกัน ไฮไลต์สีเหลืองที่โน้ตใกล้เคียง และสีเทาที่โน้ตต่าง
- [ ] **AC-MAT-03 (Metric Independence):** หน้าจอเปรียบเทียบต้องแสดงค่า **Similarity Score** และ **Confidence Badge** แยกกันเด็ดขาด โดยความนิยม (Rating) ต้องไม่มีผลทำให้คะแนนความเหมือนเพิ่มขึ้น
- [ ] **AC-MAT-04 (Explainability Box):** มีข้อความอธิบายเหตุผลภาษาไทยระบุชัดเจนว่าทำไมสองรุ่นนี้จึงคล้ายกัน และมีจุดต่างอะไรที่ควรระวัง

---

### 2.3 My Cart & Shopping Tracker (P3)
- [ ] **AC-CRT-01 (Universal Add to Cart):** ผู้ใช้สามารถกดเพิ่มน้ำหอมทุกแบรนด์เข้าสู่ `My Cart` ได้
- [ ] **AC-CRT-02 (Multiple Buying Sources):** ใน 1 รายการน้ำหอมใน Cart ผู้ใช้สามารถบันทึกลิงก์ Shopee ได้มากกว่า 1 ร้านค้า พร้อมราคาและโน้ตร้าน
- [ ] **AC-CRT-03 (Duplicate Prevention):** หากกดเพิ่มน้ำหอมรุ่นที่มีใน Cart อยู่แล้ว ระบบต้องแสดงการแจ้งเตือนและไม่สร้างแถวใหม่ แต่เสนอให้เพิ่มลิงก์ร้านค้าแทน
- [ ] **AC-CRT-04 (No Checkout):** ไม่มีปุ่มชำระเงินหรือสั่งซื้อในแอป มีเพียงปุ่มเปิดลิงก์ไปยัง Shopee ภายนอก
- [ ] **AC-CRT-05 (Manual Mark as Ordered):** เมื่อกด `Mark as Ordered` รายการต้องย้ายจากแท็บ "To Buy" ไปยังแท็บ "Ordered" พร้อมบันทึกร้านที่เลือกและราคาที่จ่ายจริง (Optional)

---

### 2.4 Ownership & Analytics Dashboard (P4)
- [ ] **AC-OWN-01 (Mark Received to Inventory):** เมื่อกด `Mark as Received` รายการต้องย้ายเข้าสู่ `inventory_items` และสร้างแถวถาวรใน `purchase_records`
- [ ] **AC-OWN-02 (History Persistence):** เมื่อผู้ใช้เปลี่ยนสถานะขวดใน Inventory เป็น `FINISHED` หรือลบขวด ประวัติการซื้อใน `purchase_records` ต้องยังคงอยู่ครบถ้วน
- [ ] **AC-OWN-03 (Dashboard Dual Metrics):** แดชบอร์ดต้องแสดงยอดรวม **Ever Purchased** (ประวัติการซื้อในอดีต) และ **Currently Owned** (ขวดที่มีอยู่จริงในตู้) แยกเป็นคนละตัวเลขอย่างชัดเจน
- [ ] **AC-OWN-04 (Taste Profile Charts):** แดชบอร์ดสรุปสัดส่วนตระกูลกลิ่น (Accords/Families) และโน้ตที่พบบ่อยที่สุดในคอลเลกชันได้อย่างถูกต้อง

---

## 3. Requirements Covered

- ครอบคลุมเกณฑ์ตรวจรับของ R01 ถึง R31 ใน [[Requirements_Register]]

---

## 4. Dependencies & Links

- รายการงาน: [[Backlog]]
- แผนงาน: [[Roadmap]]

---

## 5. Change Notes

- `2026-11-10`: ร่างเกณฑ์การตรวจรับงานแบบทดสอบได้ครอบคลุม 4 หมวดฟังก์ชันหลัก


## P1 foundation pilot acceptance supplement — PROPOSED

Before hosted migration or catalogue rollout, review [[P1_Pilot_Implementation_Plan]] for explicit
rights, idempotency, EDT/EDP identity, missing/conflicting claims, image metadata/security, tenant/FK
integrity, measured size and separate database/object restore tests. None ran in the planning PR.
AC-CAT-02 must truthfully show flat/unknown layers and image placeholders where rights/data are absent;
AC-CAT-04 remains pending until the four priority Thai brands have real permissioned records.


## Architecture review supplement — PROPOSED / NOT RUN

IMP-P1-01..04 must additionally satisfy OBS-01..04, ACL-01..07, IMG-01..06 and REC-01 in
[[P1_Pilot_Implementation_Plan]]. Documentation acceptance checks scope/locator/permission contracts
and schema-name parity; only later runtime/SQL/RLS/object tests can prove enforcement. Owner decisions
OD-01..06 require explicit accepted/deferred LOCAL/test/rights/CLOUD scope in [[P1_Data_Foundation_Plan]].
