---
id: DPT-REF-001
project: DoomParfum By TK
type: reference_index
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - references
  - links
  - index
source_of_truth: "../README.md"
---

# Reference Index — DoomParfum By TK

> **Document Type:** External References, Libraries, Tooling & Research Links
> **Source Baseline:** `../README.md` (Section 12)
> **Status:** Draft / Unverified Links Registry

---

## 1. Overview

เอกสารนี้รวบรวมลิงก์อ้างอิงทั้งหมด ทั้งในมิติของฐานข้อมูลน้ำหอม เครื่องมือทางเทคนิค แหล่งภาพประกอบ และไลบรารี เพื่อใช้อ้างอิงในโครงการ DoomParfum By TK

> [!WARNING]
> การระบุลิงก์ในเอกสารนี้เป็นไปเพื่อการประเมินและค้นคว้า **ไม่ใช่การรับรองว่าได้รับสิทธิ์หรือสามารถดูดข้อมูลได้อัตโนมัติ**

---

## 2. External References Register

| Name | Type | URL | Rights / Terms Verified? | Last Checked | หมายเหตุ / จุดประสงค์การใช้งาน |
|---|---|---|---|---|---|
| **Fragrantica Designers Index** | Olfactory Community Web | `https://www.fragrantica.com/designers/` | ❌ **No (Scraping Prohibited by ToS)** | 2026-11-10 | ค้นคว้าและตรวจสอบชื่อรุ่น/แบรนด์ด้วยมือเท่านั้น |
| **Scento Perfume Dataset** | Open Dataset Repository | `https://github.com/Scento-com/perfume-dataset` | 🟡 **Pending License Review** | 2026-11-10 | สำรวจโครงสร้างข้อมูลและสิทธิ์นำเข้าเป็น Initial Seed |
| **Scento Perfume API** | Developer API | `https://www.scento.com/developers/perfume-api` | 🟡 **Pending Pricing/ToS Review** | 2026-11-10 | ตรวจสอบข้อจำกัดการเรียกใช้งานและโควต้าฟรี |
| **Openverse API** | Media Search API | `https://api.openverse.org/v1/` | 🟢 **Verified (Creative Commons / Open Access)** | 2026-11-10 | ค้นหาภาพถ่ายวัตถุดิบโน้ตที่ระบุ Attribution ได้ |
| **Scrapy Documentation** | Python Scraping Framework | `https://docs.scrapy.org/` | 🟢 **Verified (Open Source Library)** | 2026-11-10 | เครื่องมือ ETL สำหรับแหล่งที่ได้รับอนุญาต |
| **Playwright for Python** | Browser Automation Tool | `https://playwright.dev/python/` | 🟢 **Verified (Open Source Library)** | 2026-11-10 | จำลองเบราว์เซอร์สำหรับทดสอบระบบ |
| **Drizzle ORM Docs** | TypeScript ORM | `https://orm.drizzle.team/` | 🟢 **Verified (Open Source Tool)** | 2026-11-10 | เอกสารประกอบการเขียน Schema และ Migrations |
| **Next.js Documentation** | Fullstack Web Framework | `https://nextjs.org/docs` | 🟢 **Verified (Open Source Tool)** | 2026-11-10 | เอกสารประกอบการพัฒนา App Router & Server Actions |
| **Tailwind CSS & shadcn/ui** | UI Component Library | `https://ui.shadcn.com/` | 🟢 **Verified (Open Source Primitives)** | 2026-11-10 | ส่วนประกอบ UI พื้นฐานสำหรับเว็บแอป |

---

## 3. Reference Categories & Governance

1. **Olfactory Databases:**
   - ใช้งานเพื่อการอ้างอิงชื่อสามัญของโน้ตและโครงสร้างกลิ่น
   - ไม่เก็บสำเนาข้อความรีวิวขนาดยาวโดยไม่มีการขออนุญาต
2. **Software Libraries:**
   - ตรวจสอบให้แน่ใจว่าเป็นสัญญาอนุญาตแบบเสรี เช่น MIT, Apache 2.0 หรือ BSD
3. **Media Sources:**
   - ทุกภาพที่นำมาใช้งานต้องบันทึก Creator Name และ License Type ในตาราง `note_images`

---

## 4. Dependencies & Links

- ทะเบียนแหล่งข้อมูล: [[Source_Registry]]
- นโยบายสิทธิ์: [[Rights_and_Attribution]]
- แผนผังเนื้อหา: [[Project_Index]]

---

## 5. Change Notes

- `2026-11-10`: รวบรวมดัชนีแหล่งอ้างอิงตั้งต้นจาก README พร้อมระบุสถานะสิทธิ์ชัดเจน
