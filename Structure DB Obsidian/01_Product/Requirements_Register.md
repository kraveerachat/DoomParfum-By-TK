---
id: DPT-PRD-002
project: DoomParfum By TK
type: requirements_register
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - requirements
  - traceability
source_of_truth: "../README.md"
---

# Requirements Register — DoomParfum By TK

> **Document Type:** Traceability Matrix (R01 – R31)
> **Source Baseline:** `../README.md` (Section 2)
> **Status:** Draft / Active Traceability Matrix

---

## 1. Overview & Legend

เอกสารนี้รวบรวมข้อกำหนดเชิงฟังก์ชันและไม่ใช่ฟังก์ชันทั้งหมดของโครงการ DoomParfum By TK จำนวน 31 ข้อ เพื่อใช้เป็นเกณฑ์ในการออกแบบสถาปัตยกรรม ฐานข้อมูล ส่วนต่อประสานผู้ใช้ และการทดสอบ

### สถานะข้อกำหนด:
- `[CONFIRMED]` ยืนยันจากความต้องการของผู้ใช้
- `[PROPOSED]` ข้อเสนอทางเทคนิค/กระบวนการ รอยืนยัน
- `[RESEARCH]` ต้องศึกษาความเป็นไปได้และข้อกฎหมาย/สิทธิ์ก่อน
- `[DEFERRED]` วางโครงสร้างรองรับไว้ แต่ยังไม่ทำใน MVP

---

## 2. Requirements Matrix (R01 – R31)

| Req ID | หมวดหมู่ | สถานะ | ข้อกำหนดสั้น | ลำดับความสำคัญ | เอกสารเชื่อมโยง | Acceptance Intent |
|---|---|---|---|---|---|---|
| **R01** | Discovery | CONFIRMED | แคตตาล็อกน้ำหอมหลายประเทศ/หลายปี ไม่จำกัดเฉพาะของที่มี | High (P1) | [[Domain_Model]], [[ERD_Draft]] | ค้นหาและดูรายละเอียดน้ำหอมระดับสากลได้ |
| **R02** | Taxonomy | CONFIRMED | แยก Country/Region และ Brand Positioning คนละมิติ | High (P1) | [[Brand_Taxonomy]] | ฟิลเตอร์แบรนด์ตามประเทศและประเภทได้อิสระ |
| **R03** | Olfactory | CONFIRMED | แสดง Top, Heart/Middle, Base Notes และ Accords | High (P1) | [[Perfume_and_Note_Taxonomy]] | หน้า Detail มีโครงสร้างพีระมิดโน้ตครบถ้วน |
| **R04** | Discovery | CONFIRMED | กรองตาม Day/Night, การใช้งาน, เพศ/Unisex, ฤดูกาล | Medium (P1) | [[Site_Map_and_Screens]] | ตัวกรองหลายเงื่อนไขทำงานถูกต้อง |
| **R05** | Matching | CONFIRMED | เลือกรุ่น Designer/Niche เป็นตัวอ้างอิงเพื่อหากลิ่นใกล้เคียง | High (P2) | [[Scent_Matching_Spec]], [[Compare_View]] | เลือก Reference Scent แล้วแสดง Candidate list |
| **R06** | Catalogue | CONFIRMED | รองรับแบรนด์ Middle Eastern, Thai, Indonesian และกลุ่มคุ้มค่า | High (P1/P6) | [[Brand_Taxonomy]], [[Source_Registry]] | มีแบรนด์ทางเลือกในระบบอย่างน้อยตามลิสต์หลัก |
| **R07** | Matching | CONFIRMED | เทียบโครงสร้าง Notes/Accords และหลักฐานจากรีวิว | High (P2) | [[Scent_Matching_Spec]], [[Review_Evidence_and_Confidence]] | แสดงการจับคู่โครงสร้างและสรุปรีวิวประกอบ |
| **R08** | Discovery | CONFIRMED | กรองงบประมาณเริ่มต้นไม่เกิน ฿2,000 (ปรับช่วงราคาได้) | High (P1) | [[Site_Map_and_Screens]] | ตัวกรองราคากรองตาม retail_listings ที่มีข้อมูล |
| **R09** | Cart | CONFIRMED | นำเข้าข้อมูลส่วนตัวจากลิงก์/ภาพหน้าจอ/บันทึกผู้ใช้ | Medium (P3) | [[Shopping_Tracker]], [[My_Cart_and_Ownership]] | ผู้ใช้กรอก URL ร้านค้า หรือบันทึกโน้ตเองได้ |
| **R10** | Cart | CONFIRMED | บันทึกร้านค้า, แพลตฟอร์ม, ลิงก์, ราคา, ขนาดได้หลายร้านต่อ 1 น้ำหอม | High (P3) | [[Data_Dictionary_Draft]], [[Shopping_Tracker]] | 1 น้ำหอมบันทึกร้าน Shopee ได้หลายรายการ |
| **R11** | Ownership | CONFIRMED | บันทึกสถานะ: สนใจ, วิจัย, ตะกร้าแอป, สั่งแล้ว, มีอยู่, เคยลอง, ข้าม | High (P3) | [[My_Cart_and_Ownership]], [[Shopping_Tracker]] | เปลี่ยนสถานะได้ถูกต้องตาม state machine |
| **R12** | AI Assistant | CONFIRMED | AI ช่วยค้นคว้า/อธิบาย ต้องแสดงหลักฐานและบอกสิ่งที่ไม่รู้ | Medium (P5) | [[Proposed_System_Architecture]] | AI แนะนำกลิ่นพร้อมอ้างอิง source ไม่กุข้อมูล |
| **R13** | UX/UI | CONFIRMED | หน้ารายละเอียดมี Perfume Pyramid พร้อมภาพวัตถุดิบโน้ต | High (P1) | [[Perfume_Detail_Pyramid]] | แสดงภาพโน้ต Top/Heart/Base แยกเป็นชั้น |
| **R14** | Discovery | CONFIRMED | กดที่ Note เพื่อค้นหาน้ำหอมรุ่นอื่นที่มีโน้ตเดียวกัน | High (P1) | [[Perfume_Detail_Pyramid]], [[Site_Map_and_Screens]] | คลิก Note แล้วไปหน้าค้นหาด้วย Note ID นั้น |
| **R15** | UX/UI | CONFIRMED | เปรียบเทียบสองรุ่นแบบ Side-by-Side ไฮไลต์จุดเหมือน/ต่าง | High (P2) | [[Compare_View]] | แสดง 2 คอลัมน์ ไฮไลต์สีโน้ตที่ตรงกัน |
| **R16** | Matching | PROPOSED | ให้คะแนน Structural Similarity จากข้อมูลที่ตรวจสอบได้ | Medium (P2) | [[Scent_Matching_Spec]] | คำนวณคะแนนตามพีระมิดและแอคคอร์ดที่ตรง |
| **R17** | Matching | CONFIRMED | แสดงหลักฐานความคล้าย/ต่างจากรีวิวภายนอกที่มีสิทธิ์ | High (P2) | [[Review_Evidence_and_Confidence]] | แสดงข้อความอ้างอิงที่มาพร้อม URL/แหล่งที่มา |
| **R18** | Matching | PROPOSED | แยก Similarity Score ออกจาก Evidence Confidence | High (P2) | [[Scent_Matching_Spec]], [[Review_Evidence_and_Confidence]] | แสดงแถบคะแนนความคล้าย และแถบความเชื่อมั่นแยกกัน |
| **R19** | ETL | PROPOSED | ใช้ AI/ETL Agent นำเข้าข้อมูลจากแหล่งที่ถูกต้อง | Medium (P5) | [[Ingestion_and_ETL]] | ไปป์ไลน์ตรวจสอบความถูกต้องก่อนบันทึก |
| **R20** | Catalogue | CONFIRMED | เพิ่มน้ำหอมที่ไม่อยู่ในฐานข้อมูลเปิดได้ (โดยเฉพาะแบรนด์ไทย) | High (P1) | [[Domain_Model]], [[Brand_Taxonomy]] | ผู้ใช้เพิ่มรุ่นและแบรนด์ใหม่เข้าฐานข้อมูลได้ |
| **R21** | Governance | PROPOSED | บันทึกแหล่งอ้างอิง สิทธิ์การใช้ และวันที่ตรวจของทุกข้อมูล/ภาพ | High (P1) | [[Data_Quality_and_Provenance]], [[Rights_and_Attribution]] | ทุกแถวมี source_records อ้างอิง |
| **R22** | Catalogue | CONFIRMED | เพิ่ม Thai Brand Registry: La Palette, SCENTERY, BE CHERIE, SÚNDALO | High (P1) | [[Brand_Taxonomy]] | มีรายชื่อแบรนด์และรุ่นโฟกัสในแคตตาล็อก |
| **R23** | Cart | CONFIRMED | เพิ่มน้ำหอมทุกกลุ่มแบรนด์เข้า `My Cart` ในแอปได้ | High (P3) | [[My_Cart_and_Ownership]], [[Shopping_Tracker]] | ปุ่ม Add to Cart ทำงานได้ทุกหน้าสินค้า |
| **R24** | Cart | CONFIRMED | ผูกลิงก์แหล่งซื้อหลายร้านใน Cart พร้อมโน้ตร้านที่ไว้ใจ | High (P3) | [[Shopping_Tracker]] | เพิ่มลิงก์และหมายเหตุในแต่ละรายการตะกร้าได้ |
| **R25** | Ownership | CONFIRMED | เปลี่ยนสถานะเป็น "สั่งซื้อแล้ว" ด้วยมือ ไม่เกิดธุรกรรมในแอป | High (P3) | [[My_Cart_and_Ownership]], [[Shopping_Tracker]] | กดปุ่ม Mark Ordered ย้ายจาก Cart ไป Ordered |
| **R26** | Ownership | CONFIRMED | บันทึกประวัติเคยซื้อ/เคยมี แม้ภายหลังหมดขวด/ขาย/ให้คนอื่น | High (P3) | [[My_Cart_and_Ownership]], [[Collection_Dashboard]] | ลบหรือเปลี่ยนสถานะขวดแล้ว ประวัติซื้อยังคงอยู่ |
| **R27** | Dashboard | CONFIRMED | Dashboard สรุปน้ำหอมที่เคยซื้อ/มีอยู่ แยกแบรนด์ โทนกลิ่น โน้ต | High (P4) | [[Collection_Dashboard]] | มีแผนภูมิและสรุปสถิติตามหมวดหมู่กลิ่น |
| **R28** | Ownership | PROPOSED | แยก purchase record ออกจาก ownership/inventory (ซื้อซ้ำได้) | High (P3) | [[Domain_Model]], [[Data_Dictionary_Draft]] | ซื้อรุ่นเดิม 2 ครั้งมี 2 records ใน purchase history |
| **R29** | Ownership | PROPOSED | เก็บราคาจ่ายจริง ปริมาณ วันที่ซื้อ ร้าน และสถานะรับของ (ไม่บังคับ) | Medium (P3) | [[Data_Dictionary_Draft]], [[Shopping_Tracker]] | ฟอร์มบันทึกการซื้อมีฟิลด์เสริมแต่ไม่บังคับกรอก |
| **R30** | Cart | PROPOSED | แจ้งเตือนเมื่อบันทึกน้ำหอมซ้ำใน Cart และแนะนำให้เพิ่มลิงก์ร้านแทน | Medium (P3) | [[Shopping_Tracker]] | ระบบเตือน duplicate พร้อมตัวเลือก Add Source |
| **R31** | Dashboard | DEFERRED | สรุปค่าใช้จ่าย/ราคาเฉลี่ยต่อ mL/สถิติเชิงลึกย้อนหลัง | Low (P4) | [[Collection_Dashboard]] | แสดงการวิเคราะห์ราคาเฉลี่ยและสถิติเมื่อมีข้อมูล |

---

## 3. Traceability to Delivery Phases

- **Phase P0 (Docs):** บันทึกข้อกำหนดทั้งหมดลงในเอกสารสเปก
- **Phase P1 (Core):** R01, R02, R03, R04, R06, R08, R13, R14, R20, R21, R22
- **Phase P2 (Matching):** R05, R07, R15, R16, R17, R18
- **Phase P3 (Cart & Ownership):** R09, R10, R11, R23, R24, R25, R26, R28, R29, R30
- **Phase P4 (Dashboard):** R27, R31
- **Phase P5 (AI Research & ETL):** R12, R19
- **Phase P6 (Expansion):** R06, R22 (ขยายครอบคลุมแบรนด์เพิ่มเติม)

---

## 4. Change Notes

- `2026-11-10`: เริ่มต้นจัดทำเอกสารและรวม R01–R31 จาก `../README.md`
