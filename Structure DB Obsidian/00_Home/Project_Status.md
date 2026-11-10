---
id: DPT-HOM-002
project: DoomParfum By TK
type: status
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - status
  - planning
source_of_truth: "../README.md"
---

# Project Status — DoomParfum By TK

> **Current Phase:** `P0 — Documentation & Knowledge Base Bootstrap`
> **Updated:** `2026-11-10` (Asia/Bangkok)
> **Source of Truth Baseline:** `../README.md` (v0.2.0-planning)

---

## 1. Executive Summary

โครงการ **DoomParfum By TK** อยู่ในระยะ **P0 (Documentation & Knowledge Base Architecture)** โดยมุ่งเน้นการสร้างฐานข้อมูลเอกสารที่มีโครงสร้างใน Obsidian Vault เพื่อแปลงวิสัยทัศน์และข้อกำหนดเชิงฟังก์ชัน (R01–R31) ให้เป็นแบบจำลองทางโดเมน ข้อมูล การจับคู่กลิ่น UX และข้อกำหนดทางวิศวกรรมที่พร้อมต่อยอดสู่การพัฒนาจริง

ยังไม่มีการเขียนโค้ดระบบจริง (Implementation) ไม่มีการ Deploy และไม่มีการสร้าง GitHub Actions อัตโนมัติ โดยรอการอนุมัติสถาปัตยกรรมและเวิร์กโฟลว์ของผู้ใช้

---

## 2. Phase Breakdown & Current Status

| Phase | Description | Status | Progress | Blockers / Dependencies |
|---|---|---|---|---|
| **P0** | **Documentation & Knowledge Base** | **COMPLETED** | 100% | Initial Baseline Bootstrap สำเร็จ เตรียมสู่ First Planning PR |
| **P1** | Core Foundation & Catalogue Schema | NOT STARTED | 0% | ขึ้นกับ Planning PR ของ P1 และการตรวจสิทธิ์ Data Sources |
| **P2** | Scent DNA Matching Engine | NOT STARTED | 0% | ขึ้นกับการสรุปเกณฑ์น้ำหนักการจับคู่กลิ่น |
| **P3** | My Cart & Ownership Tracking | NOT STARTED | 0% | ขึ้นกับ P1 (Schema) และ P2 |
| **P4** | Collection Dashboard & Analytics | NOT STARTED | 0% | ขึ้นกับ P3 (Purchase/Inventory Data) |
| **P5** | AI Research Assistant & Ingestion | NOT STARTED | 0% | ขึ้นกับข้อตกลงเรื่อง Rights และ API limits |
| **P6** | Expansion (Thai/Middle East/Indo) | NOT STARTED | 0% | ขึ้นกับ P5 และการรวบรวมแคตตาล็อก |

---

## 3. Current Blockers & Pending Decisions

1. **GitHub & Workflow Specification (RESOLVED FOR BOOTSTRAP):**
   - ได้รับเอกสารเวิร์กโฟลว์ `DEVELOPMENT_WORKFLOW.md` และกำหนด `AGENTS.md` เรียบร้อยแล้ว
   - การ Push Initial Documentation Baseline ขึ้นสู่ `origin/main` เป็น **ข้อยกเว้นที่ได้รับอนุมัติเพียงครั้งเดียว** (DEC-011) เนื่องจาก Remote ว่างเปล่า
   - งานหลังจากนี้ต้องเปิดผ่าน Planning PR ตาม Two-Gate Workflow ปกติ
   - ดูเอกสาร: [[GitHub_and_Workflow_PENDING]]
2. **Data Source Licensing & Rights (PENDING REVIEW):**
   - แหล่งข้อมูลเปิด เช่น Scento Dataset, Fragrantica Discovery, Openverse ต้องผ่านการทดสอบและตรวจสอบนโยบายสิทธิ์การใช้งาน
   - ดูเอกสาร: [[Source_Registry]] และ [[Rights_and_Attribution]]
3. **Similarity Weight Confirmation (PROPOSED):**
   - สูตรน้ำหนักคะแนนความคล้าย 40/25/15/20 (Notes / Accords / Family / Evidence) ยังเป็นร่างข้อเสนอ
   - ดูเอกสาร: [[Scent_Matching_Spec]]

---

## 4. Next Steps & Actions

1. ตรวจสอบความครบถ้วนของเอกสารทั้งหมดใน `Structure DB Obsidian/`
2. ให้ผู้ใช้ตรวจสอบ [[Requirements_Register]], [[Domain_Model]], [[ERD_Draft]], [[My_Cart_and_Ownership]]
3. รอผู้ใช้ส่งแนวทาง/ตัวอย่างเวิร์กโฟลว์การทำงาน GitHub/ChatGPT เพื่อปลดล็อก [[GitHub_and_Workflow_PENDING]]
4. เริ่มเตรียมสภาพแวดล้อม P1 (Next.js + PostgreSQL + Drizzle ORM) เมื่อผู้ใช้อนุมัติ
