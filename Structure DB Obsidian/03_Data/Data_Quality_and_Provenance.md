---
id: DPT-DAT-005
project: DoomParfum By TK
type: data_governance
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - quality
  - provenance
  - integrity
source_of_truth: "../README.md"
---

# Data Quality and Provenance — DoomParfum By TK

> **Document Type:** Data Quality Principles & Provenance Standard
> **Source Baseline:** `../README.md` (Section 6.4)
> **Status:** Draft / Core Governance Principles

---

## 1. Purpose / Scope

เอกสารนี้กำหนดมาตรฐานคุณภาพของข้อมูล (Data Quality) และการตรวจสอบย้อนกลับแหล่งที่มา (Data Provenance) เพื่อให้แน่ใจว่าระบบ DoomParfum By TK เป็นฐานข้อมูลที่เชื่อถือได้ อ้างอิงได้จริง และปราศจากการปลอมแปลงข้อมูล

---

## 2. Core Integrity Principles

> [!CAUTION]
> **หลักการสำคัญที่สุดด้านความถูกต้องของข้อมูล [CONFIRMED]:**
> 1. **ห้ามสร้างข้อมูลเท็จโดยเด็ดขาด (No Fabricated Data):** ห้ามนำ AI หรือโมเดลใดๆ มาคาดเดาหรือกุรายชื่อ Top/Heart/Base Notes, ราคาขาย, หรือคะแนนรีวิวขึ้นมาเองเพื่อเติมช่องว่าง
> 2. **ความไม่รู้คือข้อเท็จจริง (Missing is a Valid State):** หากน้ำหอมรุ่นใดไม่มีข้อมูลโน้ตครบ 3 ชั้น ให้คงสถานะ `NULL` หรือ `Unknown` พร้อมระบุสัดส่วนความสมบูรณ์ (Coverage) ไม่สรุปว่าเท่ากับ 0 หรือแต่งโน้ตเติม
> 3. **ราคาต้องระบุเวลาและร้านเสมอ (Price is an Observation):** ไม่มีคำว่า "ราคาจริงถาวร" มีเพียงราคาที่สังเกตพบ ณ ร้านค้าหนึ่ง ในวันและเวลาที่ระบุชัดเจน

---

## 3. Field-Level Provenance (แหล่งที่มาระดับฟิลด์)

ในระบบบันทึกข้อมูลระดับละเอียด ข้อมูลแต่ละส่วนอาจมาจากต่างแหล่งกัน:

| ส่วนข้อมูล (Field Group) | ที่มาหลักที่ยอมรับได้ | ระดับความเชื่อมั่น (Confidence) | กลยุทธ์เมื่อพบข้อมูลขัดแย้ง |
|---|---|---|---|
| **Brand & Official Name** | เว็บทางการของแบรนด์ / ผู้จัดจำหน่าย | สูงมาก (High) | ยึดตามชื่อบนขวดและกล่องทางการ |
| **Top/Heart/Base Notes** | ประกาศของแบรนด์ / Verified Dataset | สูง (High) | หากแบรนด์ไม่แยกชั้น ให้บันทึกเป็น All Notes |
| **Accords & Families** | Olfactory Analysis / Community Consensus | ปานกลาง (Medium) | บันทึกน้ำหนักความเด่นเฉลี่ย |
| **Comparison Evidence** | รีวิวที่มีสิทธิ์ / บันทึกผู้ใช้ | ปานกลาง (Medium) | บันทึกทั้งสองมุมมอง หากมีความเห็นขัดแย้ง |
| **Price & Marketplace Link**| การสังเกตการณ์ของผู้ใช้ (Observation) | แปรผันตามเวลา | บันทึกพร้อม Snapshot Timestamp |

---

## 4. Handling Conflicting Information (การจัดการข้อมูลขัดแย้ง)

ในวงการน้ำหอม บ่อยครั้งที่ข้อมูลโน้ตจากเว็บไซต์ทางการ, รีวิวบล็อกเกอร์, และชุมชนไม่ตรงกัน:
1. **ไม่ลบข้อมูลที่เห็นต่าง:** บันทึกมุมมองหลักไว้ใน Canonical Table และบันทึกข้อคิดเห็นที่ต่างไว้ในตารางข้อสังเกต (`perfume_notes_annotations`)
2. **แสดงสถานะ Uncertain:** หากรุ่นใดมีข้อโต้แย้งเรื่องส่วนผสม ให้ติดธง `[UNCERTAIN]` ในหน้ารายละเอียดเพื่อแจ้งผู้ใช้
3. **Audit Trail:** ทุกการแก้ไขข้อมูลใน Master Table จะถูกบันทึกประวัติว่าใครเป็นผู้แก้ (User หรือ ETL Job) และแก้เมื่อใด

---

## 5. Data Coverage Metrics

ระบบจะคำนวณดัชนีความสมบูรณ์ของข้อมูล (Data Coverage Score) สำหรับน้ำหอมแต่ละรุ่น:
- **Level 1 (Basic):** มีชื่อรุ่น, แบรนด์, ประเทศ (Coverage 30%)
- **Level 2 (Olfactory):** มีโน้ตอย่างน้อย 1 ชั้น หรือมี Accords (Coverage 60%)
- **Level 3 (Pyramid Complete):** มี Top, Heart, และ Base ครบถ้วน (Coverage 90%)
- **Level 4 (Fully Documented):** มีพีระมิดครบ + มีภาพขวด/โน้ต + มีแหล่งซื้อ + มีรีวิว (Coverage 100%)

ระดับ Coverage นี้จะถูกส่งต่อไปยัง Matching Engine เพื่อคำนวณ **Confidence Score** ใน [[Scent_Matching_Spec]]

---

## 6. Requirements Covered

- [[Requirements_Register#R18|R18]] — Separate Similarity from Confidence
- [[Requirements_Register#R21|R21]] — Source Attribution and Rights Logging

---

## 7. Dependencies & Links

- พจนานุกรมข้อมูล: [[Data_Dictionary_Draft]]
- ทะเบียนแหล่งข้อมูล: [[Source_Registry]]
- นโยบายสิทธิ์: [[Rights_and_Attribution]]

---

## 8. Change Notes

- `2026-11-10`: บันทึกมาตรฐาน Data Quality และข้อห้าม Fabricated Data อย่างเป็นทางการ
