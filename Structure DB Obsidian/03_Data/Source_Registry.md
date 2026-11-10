---
id: DPT-DAT-003
project: DoomParfum By TK
type: source_registry
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - sources
  - rights
  - registry
source_of_truth: "../README.md"
---

# Source Registry — DoomParfum By TK

> **Document Type:** External Data Sources & Rights Governance Registry
> **Source Baseline:** `../README.md` (Section 6 & 12)
> **Status:** Draft / Active Evaluation

---

## 1. Purpose / Scope

เอกสารนี้รวบรวมรายชื่อแหล่งข้อมูลภายนอกทั้งหมดที่อยู่ในการพิจารณาเพื่อนำมาใช้ในระบบ DoomParfum By TK พร้อมระบุประเภทข้อมูล สถานะการตรวจสอบสิทธิ์ (Rights Verification Status) และข้อจำกัดในการจัดเก็บหรือประมวลผล

> [!WARNING]
> **นโยบายความถูกต้องของข้อมูลและลิขสิทธิ์ [CONFIRMED]:**
> ห้ามระบุว่าแหล่งข้อมูลใดได้รับอนุญาตหรือตรวจสอบแล้ว (Verified / Licensed) หากยังไม่ได้ตรวจข้อกำหนดการให้บริการ (Terms of Service) หรือสัญญาอนุญาตจริง การพบโค้ด Scraper บน GitHub **ไม่เท่ากับ** ได้รับอนุญาตให้ดึงข้อมูล

---

## 2. Source Evaluation Matrix

| Source Name | Source Type | URL / Reference | จุดประสงค์การใช้งาน | สิทธิ์การใช้งาน (Rights Status) | วันที่ตรวจสอบ | ข้อจำกัด / เงื่อนไขสำคัญ |
|---|---|---|---|---|---|---|
| **User Direct Input** | User Generated | - | บันทึกส่วนตัว, ลิงก์ Shopee, รูปตะกร้า | `[CONFIRMED / ALLOWED]` | 2026-11-10 | ข้อมูลส่วนบุคคลของผู้ใช้เอง นำเข้าได้ทันที |
| **Scento Dataset** | Open Dataset | `https://github.com/Scento-com/perfume-dataset` | Seed ข้อมูลแคตตาล็อกและโน้ตสากล | `[RESEARCH / PENDING]` | 2026-11-10 | ต้องตรวจสอบ License (MIT/CC/ODbL) และความครอบคลุม |
| **Scento API** | Commercial / Freemium API | `https://www.scento.com/developers/perfume-api` | ข้อมูลน้ำหอมและพีระมิดโน้ต | `[RESEARCH / PENDING]` | 2026-11-10 | ตรวจสอบ Rate limits, API Pricing, และข้อห้าม Caching |
| **Openverse API** | Open Media API | `https://api.openverse.org/v1/` | ภาพประกอบวัตถุดิบโน้ต (Creative Commons) | `[RESEARCH / PENDING]` | 2026-11-10 | มี License ชัดเจน ต้องบันทึก Creator Attribution |
| **Fragrantica** | Community Web | `https://www.fragrantica.com/` | Discovery & Verification ด้วยมือ | `[RESTRICTED / NO SCRAPE]` | 2026-11-10 | **ห้าม Automated Scraping** / อนุญาตเฉพาะการดูอ้างอิงด้วยมือ |
| **Thai Brand Official Sites** | Official Web / Social | Facebook/IG/Website ของแต่ละแบรนด์ | ข้อมูลโน้ตและรุ่นทางการของแบรนด์ไทย | `[CONFIRMED / MANUAL]` | 2026-11-10 | บันทึกจากข้อมูลที่แบรนด์เผยแพร่เป็นสาธารณะ |
| **Shopee Thailand** | Marketplace | `https://shopee.co.th/` | บันทึกลิงก์ร้านค้าและราคาอ้างอิง | `[CONFIRMED / LINK-ONLY]` | 2026-11-10 | เก็บเป็น URL และสแนปช็อตที่ผู้ใช้บันทึก ไม่ดึงข้อมูลอัตโนมัติฝืนเงื่อนไข |
| **TikTok / YouTube** | Social Media | คลิปรีวิวของครีเอเตอร์ | สรุปคำรีวิวและข้อคิดเห็นเรื่องความคล้าย | `[RESEARCH / PENDING]` | 2026-11-10 | เก็บเป็น Reference Link + ข้อความสรุปสั้น ไม่คัดลอกไฟล์วิดีโอ |

---

## 3. Detailed Source Notes

### 3.1 Scento Perfume Dataset & API
- **โอกาส:** เป็นชุดข้อมูลน้ำหอมที่มีโครงสร้าง Top/Heart/Base และ Accords พร้อมใช้งานสำหรับระบบสากล
- **สิ่งที่ต้องทำต่อ:** ตรวจสอบไฟล์ `LICENSE` ใน GitHub repository เพื่อดูว่าอนุญาตให้นำมาใช้ในแอปพลิเคชันส่วนตัวหรือเชิงพาณิชย์อย่างไร

### 3.2 Fragrantica & Web Scraping Rules
- **จุดยืนของโครงการ:** ไม่ทำ Scraper ดึงข้อมูลขนาดใหญ่ (Mass Scraping) จาก Fragrantica
- **เหตุผล:** นโยบาย Terms of Service ของ Fragrantica ไม่อนุญาตให้ใช้บอทหรือสคริปต์อัตโนมัติ และระบบของพวกเขามีกลไกป้องกัน (Cloudflare/Anti-bot)
- **แนวทางทดแทน:** ใช้เป็นแหล่งค้นคว้าและตรวจสอบด้วยสายตา (Manual lookup) แล้วบันทึกข้อมูลเฉพาะที่จำเป็น

### 3.3 Note Illustration Images (ภาพประกอบโน้ต)
- ภาพโน้ตในระบบ (เช่น มะนาว, วานิลลา, ไม้จันทน์) ต้องไม่ใช้วิธี Hotlink จากเว็บภายนอกโดยไม่มีสิทธิ์
- แหล่งที่อนุญาต:
  1. Openverse / Wikimedia Commons (ระบุ License และชื่อผู้สร้าง)
  2. ชุดภาพ Artwork ที่โครงการจัดเตรียมหรือสร้างขึ้นเองภายใต้สิทธิ์ถูกต้อง

---

## 4. Requirements Covered

- [[Requirements_Register#R06|R06]], [[Requirements_Register#R09|R09]], [[Requirements_Register#R17|R17]]
- [[Requirements_Register#R21|R21]] — Source Attribution and Rights Logging
- [[Requirements_Register#R22|R22]] — Thai Brand Official Registry

---

## 5. Dependencies & Links

- นโยบายสิทธิ์และลิขสิทธิ์: [[Rights_and_Attribution]]
- ไปป์ไลน์การนำเข้า: [[Ingestion_and_ETL]]
- ความน่าเชื่อถือของข้อมูล: [[Data_Quality_and_Provenance]]

---

## 6. Change Notes

- `2026-11-10`: บันทึกทะเบียนแหล่งข้อมูลตั้งต้น แยกสถานะ Allowed / Pending / Restricted ชัดเจน
