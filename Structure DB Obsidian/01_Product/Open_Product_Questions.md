---
id: DPT-PRD-005
project: DoomParfum By TK
type: open_questions
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - product
  - open_questions
source_of_truth: "../README.md"
---

# Open Product Questions — DoomParfum By TK

> **Document Type:** Unresolved Product & Design Questions
> **Source Baseline:** `../README.md` (Section 11)
> **Status:** Open / Awaiting User Input

---

## 1. Overview

เอกสารนี้รวบรวมประเด็นคำถามทางผลิตภัณฑ์ที่ยังไม่ได้รับการยืนยันจากผู้ใช้ เพื่อป้องกันไม่ให้ Agent หรือทีมนักพัฒนาแต่งเติมข้อเท็จจริงหรือตัดสินใจแทนผู้ใช้โดยพลการ

---

## 2. Active Open Questions

### Q-PRD-01: น้ำหนักและสมดุลในการจับคู่กลิ่น (Scent Matching Weights)
- **คำถาม:** ควรให้น้ำหนักของโครงสร้าง Notes (Top/Heart/Base) มากกว่าหรือน้อยกว่ารีวิวจากชุมชนอย่างไร?
- **สถานะปัจจุบัน:** เสนอร่างสูตร `40% Notes / 25% Accords / 15% Family / 20% Evidence` (`[PROPOSED]`)
- **ผลกระทบ:** มีผลต่ออัลกอริทึมการคำนวณใน [[Scent_Matching_Spec]]

### Q-PRD-02: สถานะของ Social Media Review (TikTok / YouTube)
- **คำถาม:** รีวิวจาก Creator บน TikTok หรือ YouTube ควรถือเป็น **Primary Evidence** (เทียบเคียงข้อมูลโน้ตทางการ) หรือเป็นเพียง **Supporting Evidence** (ข้อมูลเสริมทางความรู้สึก)?
- **สถานะปัจจุบัน:** ยังไม่กำหนดชัดเจน อยู่ระหว่างการประเมินสิทธิ์และรูปแบบการอ้างอิง
- **ผลกระทบ:** มีผลต่อโครงสร้างตาราง `comparison_evidence` และการให้คะแนนความเชื่อมั่น

### Q-PRD-03: ขอบเขตความเป็นส่วนตัวและการรองรับผู้ใช้ (Single-user vs Multi-user)
- **คำถาม:** ในระยะยาว ต้องการให้เป็นระบบสำหรับคุณ TK เพียงคนเดียว (Private-only) หรือเตรียมความพร้อมสำหรับผู้ใช้ทั่วไปสมัครสมาชิกใช้งานได้ด้วย?
- **สถานะปัจจุบัน:** สถาปัตยกรรมร่างรองรับ Single-user เป็นหลัก แต่แยกตาราง `users` ไว้เพื่อความยืดหยุ่น
- **ผลกระทบ:** นโยบาย Authentication และการป้องกันข้อมูลใน [[Security_and_Privacy]]

### Q-PRD-04: แพลตฟอร์มแหล่งซื้อสินค้า (Buying Platforms Scope)
- **คำถาม:** ในหน้า `My Cart` และ `Buying Sources` ต้องการรองรับเฉพาะร้านค้าใน Shopee หรือต้องการให้แปะลิงก์แพลตฟอร์มอื่นได้อิสระ (เช่น Lazada, TikTok Shop, Official Website, กลุ่ม Facebook)?
- **สถานะปัจจุบัน:** ออกแบบเป็น generic schema (`platform_name`, `url`) เพื่อรองรับได้ทุกแพลตฟอร์ม แต่โฟกัส Shopee ในตัวอย่างแรก
- **ผลกระทบ:** รูปแบบการแสดงผลและฟิลด์ใน [[Shopping_Tracker]]

### Q-PRD-05: ระดับความละเอียดของข้อมูลใน Purchase Record (R29)
- **คำถาม:** ข้อมูลประวัติการซื้อจริง เช่น ราคาที่จ่ายจริง, ปริมาณขวด, ส่วนลด, ค่าส่ง ควรให้ผู้ใช้กรอกแบบละเอียด หรือเป็นฟิลด์สั้นๆ ไม่บังคับเพื่อความสะดวกรวดเร็ว?
- **สถานะปัจจุบัน:** เสนอให้เป็น Optional fields ทั้งหมด (กรอกเพียงชื่อรุ่นก็สามารถบันทึกได้)
- **ผลกระทบ:** UX Form ในหน้าบันทึกการซื้อ [[Shopping_Tracker]]

### Q-PRD-06: การคัดเลือก Open Dataset เริ่มต้น
- **คำถาม:** สำหรับการ Seed ฐานข้อมูลน้ำหอมสากลใน Phase P1 ผู้ใช้สะดวกให้ทดสอบนำเข้าจาก Scento Dataset หรือมีชุดข้อมูลอื่นที่เตรียมไว้แล้ว?
- **สถานะปัจจุบัน:** อยู่ระหว่างการวิจัยสิทธิ์ใน [[Source_Registry]]
- **ผลกระทบ:** ขั้นตอน Data Ingestion ใน [[Ingestion_and_ETL]]

### Q-PRD-07: รูปแบบเวิร์กโฟลว์ GitHub และ CI/CD
- **คำถาม:** เวิร์กโฟลว์การซิงก์เอกสาร Obsidian ขึ้น GitHub, การ Commit, และการเชื่อมต่อกับ ChatGPT/Agent ต้องการให้เป็นรูปแบบใด? (รอไฟล์ตัวอย่างจากผู้ใช้)
- **สถานะปัจจุบัน:** `[BLOCKED / WAITING FOR USER INPUT]`
- **ผลกระทบ:** เอกสาร [[GitHub_and_Workflow_PENDING]]

---

## 3. Review & Resolution Process

เมื่อผู้ใช้ให้คำตอบสำหรับประเด็นใด:
1. ปรับสถานะคำถามเป็น `RESOLVED` พร้อมใส่วันที่และข้อความอ้างอิง
2. อัปเดตเอกสารสเปกที่ได้รับผลกระทบ
3. บันทึกลงใน [[Decision_Log]] และ [[Change_Log]]
