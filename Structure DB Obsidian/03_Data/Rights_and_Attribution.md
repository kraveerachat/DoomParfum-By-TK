---
id: DPT-DAT-006
project: DoomParfum By TK
type: legal_and_rights
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - rights
  - copyright
  - attribution
source_of_truth: "../README.md"
---

# Rights and Attribution Policy — DoomParfum By TK

> **Document Type:** Intellectual Property, Copyright & Responsible Usage Policy
> **Source Baseline:** `../README.md` (Sections 1.2, 6.2 & 6.4)
> **Status:** Draft / Strict Compliance Policy

---

## 1. Purpose / Scope

เอกสารนี้กำหนดแนวทางปฏิบัติทางกฎหมายและจริยธรรมเกี่ยวกับการจัดเก็บ การแสดงผล และการอ้างอิงเนื้อหาข้อความ รูปภาพ ฐานข้อมูล และรีวิวจากบุคคลภายนอก เพื่อปกป้องโครงการ DoomParfum By TK จากการละเมิดลิขสิทธิ์หรือข้อกำหนดการให้บริการ (Terms of Service)

---

## 2. Policy by Content Category

```mermaid
flowchart TD
    Content["ประเภทเนื้อหาที่ใช้งานในระบบ"]

    subgraph TextPolicy["1. ข้อความและโน้ตกลิ่น (Facts & Notes)"]
        T1["รายชื่อโน้ต / พีระมิด = ข้อเท็จจริง (Facts)<br/>นำมาจัดระเบียบและแสดงผลได้"]
        T2["คำอธิบายกลิ่นยาวๆ = สรุปความ / Paraphrase<br/>ไม่คัดลอกบทความทั้งหมด"]
    end

    subgraph ImagePolicy["2. รูปภาพ (Images)"]
        I1["ภาพวัตถุดิบโน้ต: ใช้ Creative Commons / Openverse<br/>พร้อมระบุชื่อผู้สร้างและ License"]
        I2["ภาพขวดน้ำหอม: บันทึกเฉพาะ URL / Fair Use ส่วนตัว<br/>ห้าม Hotlink แบนด์วิดท์ผู้อื่นโดยไม่มีสิทธิ์"]
    end

    subgraph ReviewPolicy["3. รีวิวและหลักฐาน (Reviews & Claims)"]
        R1["ข้อความสรุปสั้น: เช่น 'เปิดคล้าย A ท้ายคล้าย B'<br/>อ้างอิง URL แหล่งที่มา + วันที่"]
        R2["ห้ามกวาดบทวิจารณ์ฉบับเต็มมาเผยแพร่ซ้ำ"]
    end

    Content --> TextPolicy
    Content --> ImagePolicy
    Content --> ReviewPolicy
```

---

## 3. Strict Rules on Web Scraping & APIs

1. **เคารพเงื่อนไข Terms of Service (ToS):**
   - แหล่งข้อมูลใดที่ระบุใน ToS ห้ามการดึงข้อมูลอัตโนมัติ (Automated Scraping) ระบบจะไม่เขียนสคริปต์ดึงข้อมูลจากแหล่งนั้นโดยเด็ดขาด
2. **ไม่หลบหลีกกลไกป้องกัน (No Bypass of Safeguards):**
   - ไม่เขียนคำสั่งหลบเลี่ยง CAPTCHA, Cloudflare, ระบบ Login หรือข้อจำกัด Rate Limit ของเว็บไซต์ใดๆ
3. **การเข้าถึงบัญชี Shopee:**
   - ระบบ **ไม่เข้าถึงบัญชี Shopee ของผู้ใช้**, ไม่ใช้คุกกี้/เซสชันส่วนบุคคล และไม่มีการจำลองคำสั่งซื้ออัตโนมัติ การทำงานกับ Shopee ทำผ่านการแปะลิงก์ (URL Bookmark) เท่านั้น
4. **การตรวจสอบสิทธิ์อย่างสม่ำเสมอ:**
   - ข้อมูลและรูปภาพทุกชุดต้องมีฟิลด์ `rights_verified: boolean` และ `checked_at: timestamp` หากยังไม่ได้รับการตรวจสอบ จะต้องไม่เผยแพร่สู่สาธารณะ

---

## 4. Attribution Record Standards

เมื่อบันทึกข้อมูลจากแหล่งภายนอก ต้องเก็บบันทึกในตาราง `source_records` ดังนี้:
- `source_name`: ชื่อแหล่งข้อมูล (เช่น Openverse, Scento Dataset, Official Press Release)
- `source_url`: URL ต้นทางที่สามารถตรวจสอบย้อนหลังได้
- `license_type`: สัญญาอนุญาต (เช่น `CC-BY-4.0`, `CC0`, `Public Domain`, `Fair Use Personal`)
- `attribution_text`: ข้อความระบุเกียรติคุณเจ้าของผลงานตามเงื่อนไขสัญญา
- `checked_at`: วันและเวลาที่ทำการตรวจยืนยัน

---

## 5. Requirements Covered

- [[Requirements_Register#R17|R17]] — External Review Evidence with Permitted Rights
- [[Requirements_Register#R21|R21]] — Rights & Attribution Logging

---

## 6. Dependencies & Links

- ทะเบียนแหล่งข้อมูล: [[Source_Registry]]
- การประกันคุณภาพข้อมูล: [[Data_Quality_and_Provenance]]

---

## 7. Change Notes

- `2026-11-10`: จัดทำนโยบายสิทธิ์และการอ้างอิงอย่างเคร่งครัดตามข้อกำหนดใน README
