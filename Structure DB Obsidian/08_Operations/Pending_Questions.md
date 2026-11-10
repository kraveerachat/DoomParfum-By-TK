---
id: DPT-OPS-004
project: DoomParfum By TK
type: pending_questions
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - operations
  - questions
  - blockers
source_of_truth: "../../README.md"
---

# Pending Questions & Uncertainties — DoomParfum By TK

> **Document Type:** Active Tracking of Unresolved Design & Technical Questions
> **Source Baseline:** `../README.md` (Section 11)
> **Status:** Active Tracking

---

## 1. Overview

เอกสารนี้ทำหน้าที่เป็นสมุดจดประเด็นคำถาม ความคลุมเครือ (Uncertainties) และข้อตัดสินใจที่ยังคงค้างอยู่ เพื่อให้ทีมงานและผู้ใช้สามารถติดตามและตอบข้อซักถามก่อนที่จะเริ่มการพัฒนาจริงใน Phase P1

---

## 2. Summary of Open Questions by Category

```mermaid
flowchart TD
    Pending["ประเด็นคำถามที่ค้างอยู่ (Pending Questions)"]

    subgraph Cat1["1. Scent Matching & Algorithm"]
        PQ_01["PQ-01: สูตรน้ำหนักความคล้าย 40/25/15/20 เป็นที่น่าพอใจหรือไม่?"]
        PQ_02["PQ-02: รีวิวจาก TikTok ถือเป็น Primary หรือ Supporting Evidence?"]
    end

    subgraph Cat2["2. Data Sourcing & Rights"]
        PQ_03["PQ-03: การนำเข้า Scento Dataset ผ่านการตรวจสอบสิทธิ์หรือยัง?"]
        PQ_04["PQ-04: ข้อมูลภาพถ่ายขวดแบรนด์ไทยจะจัดเตรียมอย่างไรให้ถูกสิทธิ์?"]
    end

    subgraph Cat3["3. Personal Cart & Scope"]
        PQ_05["PQ-05: ต้องการฟิลด์บันทึกราคาส่วนลด/ค่าส่งใน Purchase Record หรือไม่?"]
        PQ_06["PQ-06: ใน Cart ต้องการรองรับการแยกแท็บร้านค้าหลายแพลตฟอร์มหรือไม่?"]
    end

    subgraph Cat4["4. Git & Workflow Automation"]
        PQ_07["PQ-06: Workflow exists; owner review and CI scope remain pending"]
    end

    Pending --> Cat1
    Pending --> Cat2
    Pending --> Cat3
    Pending --> Cat4
```

---

## 3. Detailed Tracking Table

| ID | ประเด็นคำถาม | ระดับผลกระทบ | เอกสารที่เกี่ยวข้อง | สถานะปัจจุบัน | ทางเลือกที่เสนอ |
|---|---|---|---|---|---|
| **PQ-01** | สัดส่วนการถ่วงน้ำหนัก Notes (40%), Accords (25%), Family (15%), Evidence (20%) เหมาะสมหรือไม่? | High | [[Scent_Matching_Spec]] | รอยืนยัน | ใช้เป็น Proposed baseline และทดสอบในระยะ P2 |
| **PQ-02** | สถานะทางกฎหมายและการจัดเก็บรีวิว TikTok/YouTube | Medium | [[Review_Evidence_and_Confidence]], [[Rights_and_Attribution]] | รอรีวิวสิทธิ์ | บันทึกเฉพาะลิงก์ต้นทางและข้อความสรุปสั้นๆ ห้ามเก็บไฟล์วิดีโอ |
| **PQ-03** | การใช้งาน Scento Dataset เพื่อเป็น Initial Seed ใน Phase P1 | High | [[Source_Registry]], [[Ingestion_and_ETL]] | CC BY 4.0 verified; pilot adoption pending | See OD-01 and [[Source_Registry]]; no runtime import yet |
| **PQ-04** | สิทธิ์ของรูปภาพขวดน้ำหอมและโลโก้แบรนด์ | Medium | [[Rights_and_Attribution]], [[Perfume_Detail_Pyramid]] | รอแนวทาง | ใช้ภาพถ่ายจริงของผู้ใช้เอง หรือบันทึกเฉพาะ URL อ้างอิง |
| **PQ-05** | ความละเอียดของแบบฟอร์มการซื้อจริง (R29) | Low | [[My_Cart_and_Ownership]], [[Shopping_Tracker]] | รอยืนยัน | ให้ฟิลด์ส่วนใหญ่เป็น Optional เพื่อไม่ให้ผู้ใช้เสียเวลากรอก |
| **PQ-06** | Existing public repository/workflow; governance acceptance and future CI scope | High | [[GitHub_and_Workflow_PENDING]], [[Backlog]] | OWNER REVIEW PENDING | PR #1 exists and stays Draft/Open; no missing-workflow blocker, no CI creation |

---

## 4. How to Resolve Questions

เมื่อผู้ใช้ให้คำตอบสำหรับประเด็นใด:
1. ปรับปรุงสถานะในเอกสารนี้เป็น `RESOLVED`
2. บันทึกผลการตัดสินใจลงใน [[Decision_Log]]
3. ปรับปรุงข้อกำหนดและสเปกในโฟลเดอร์ที่เกี่ยวข้อง (`01_Product`, `02_Domain`, `04_Matching`, `06_Engineering`)


Post-review note: OD-01..06 LOCAL/test/rights/CLOUD recommendations are in [[P1_Data_Foundation_Plan]]. No PROPOSED decision is accepted by this update.
