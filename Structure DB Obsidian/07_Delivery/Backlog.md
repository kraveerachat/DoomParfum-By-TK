---
id: DPT-DEL-002
project: DoomParfum By TK
type: product_backlog
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - delivery
  - backlog
  - tasks
source_of_truth: "../../README.md"
---

# Product Backlog — DoomParfum By TK

> **Document Type:** Work Breakdown Structure & Task Backlog
> **Source Baseline:** `../README.md` (Sections 2 & 8)
> **Status:** Draft / Active Backlog

---

## 1. Overview

เอกสารนี้รวบรวมรายการงาน (Backlog Items) สำหรับการพัฒนาโครงการ DoomParfum By TK โดยเชื่อมโยงกับข้อกำหนดความต้องการ (Requirement IDs) และระบุความสัมพันธ์ขึ้นต่อกัน (Dependencies)

---

## 2. Epics & Backlog Tasks

### Epic 0: Documentation & Specifications (Phase P0)
| Task ID | งานที่ต้องทำ | Requirement ID | สถานะ | ข้อมูลเชื่อมโยง | ขึ้นต่อกัน |
|---|---|---|---|---|---|
| **TSK-001** | จัดตั้งโครงสร้าง Obsidian Vault 11 โฟลเดอร์ | - | DONE | [[Project_Index]] | - |
| **TSK-002** | บันทึกทะเบียนข้อกำหนด R01 ถึง R31 | R01–R31 | DONE | [[Requirements_Register]] | TSK-001 |
| **TSK-003** | ร่างผัง Bounded Context และ Taxonomy | R02, R03 | DONE | [[Domain_Model]], [[Brand_Taxonomy]] | TSK-001 |
| **TSK-004** | ร่าง ERD และ Data Dictionary 10 ตารางหลัก | R01, R10, R28 | DONE | [[ERD_Draft]], [[Data_Dictionary_Draft]] | TSK-003 |
| **TSK-005** | ร่างสูตรและตรรกะ Scent DNA Matching | R05, R16, R18 | DONE | [[Scent_Matching_Spec]] | TSK-003 |
| **TSK-006** | สเปก No-Checkout Cart และแบบจำลองการครอบครอง | R23, R25, R26 | DONE | [[My_Cart_and_Ownership]] | TSK-003 |
| **TSK-007** | ออกแบบ Wireframe และสเปก 6 หน้าจอหลัก | R13, R15, R27 | DONE | [[Site_Map_and_Screens]] ถึง [[Collection_Dashboard]] | TSK-006 |
| **TSK-008** | สรุปบันทึกการตัดสินใจ DEC-001 ถึง DEC-009 | - | DONE | [[Decision_Log]] | TSK-002 |

---

### Epic 1: Database & Catalogue Core (Phase P1)
| Task ID | งานที่ต้องทำ | Requirement ID | สถานะ | ข้อมูลเชื่อมโยง | ขึ้นต่อกัน |
|---|---|---|---|---|---|
| **TSK-101** | สร้าง Next.js + PostgreSQL + Drizzle ORM Setup | - | PLANNED | [[Proposed_System_Architecture]] | DPT-PLAN-001 owner merge + IMP-P1-04 evidence |
| **TSK-102** | สร้าง Database Schema และ Drizzle Migrations | R01, R03 | PLANNED | [[Data_Dictionary_Draft]] | TSK-101 |
| **TSK-103** | นำเข้า Master Data แบรนด์ไทย 4 แบรนด์หลัก | R22 | PLANNED | [[Brand_Taxonomy]] | TSK-102 |
| **TSK-104** | พัฒนาระบบค้นหาและกรอง (Explore Screen) | R01, R04, R08 | PLANNED | [[Site_Map_and_Screens]] | TSK-102 |
| **TSK-105** | พัฒนาหน้า Perfume Detail พร้อมพีระมิดโน้ตและภาพ | R03, R13 | PLANNED | [[Perfume_Detail_Pyramid]] | TSK-102 |
| **TSK-106** | พัฒนาระบบคลิกที่ Note เพื่อค้นหาความสัมพันธ์ | R14 | PLANNED | [[Perfume_Detail_Pyramid]] | TSK-105 |
| **TSK-107** | ฟอร์มเพิ่มน้ำหอมด้วยตนเอง (Manual Add) | R20 | PLANNED | [[Domain_Model]] | TSK-102 |

---

### Epic 2: Matching Engine & Compare View (Phase P2)
| Task ID | งานที่ต้องทำ | Requirement ID | สถานะ | ข้อมูลเชื่อมโยง | ขึ้นต่อกัน |
|---|---|---|---|---|---|
| **TSK-201** | พัฒนาฟังก์ชันค้นหาน้ำหอมทางเลือกจากรุ่นอ้างอิง | R05 | PLANNED | [[Scent_Matching_Spec]] | TSK-104 |
| **TSK-202** | พัฒนาอัลกอริทึม Rule-Based Multi-Dimension Match | R16, R18 | PLANNED | [[Scent_Matching_Spec]] | TSK-201 |
| **TSK-203** | พัฒนาหน้าจอเปรียบเทียบ Side-by-Side ไฮไลต์สีโน้ต | R15 | PLANNED | [[Compare_View]] | TSK-202 |
| **TSK-204** | ระบบแสดงหลักฐานรีวิวและ Confidence Badge | R17, R18 | PLANNED | [[Review_Evidence_and_Confidence]] | TSK-203 |

---

### Epic 3: My Cart & Shopping Tracker (Phase P3)
| Task ID | งานที่ต้องทำ | Requirement ID | สถานะ | ข้อมูลเชื่อมโยง | ขึ้นต่อกัน |
|---|---|---|---|---|---|
| **TSK-301** | พัฒนาหน้าจอ Shopping Tracker (`My Cart`) | R23 | PLANNED | [[Shopping_Tracker]] | TSK-105 |
| **TSK-302** | ระบบบันทึกลิงก์ Shopee หลายร้านต่อหนึ่งน้ำหอม | R10, R24 | PLANNED | [[Shopping_Tracker]] | TSK-301 |
| **TSK-303** | ฟังก์ชันแจ้งเตือนรายการซ้ำใน Cart (Duplicate Warning) | R30 | PLANNED | [[Shopping_Tracker]] | TSK-301 |
| **TSK-304** | ฟังก์ชันเปลี่ยนสถานะเป็น Ordered ด้วยตนเอง | R25 | PLANNED | [[Shopping_Tracker]] | TSK-301 |
| **TSK-305** | ฟังก์ชัน Mark as Received ย้ายเข้า Inventory | R11, R28 | PLANNED | [[My_Cart_and_Ownership]] | TSK-304 |
| **TSK-306** | บันทึกประวัติการซื้อถาวรลงใน `purchase_records` | R26, R29 | PLANNED | [[Data_Dictionary_Draft]] | TSK-305 |

---

### Epic 4: Collection & Dashboard (Phase P4)
| Task ID | งานที่ต้องทำ | Requirement ID | สถานะ | ข้อมูลเชื่อมโยง | ขึ้นต่อกัน |
|---|---|---|---|---|---|
| **TSK-401** | พัฒนาหน้าจัดการขวดในคอลเลกชัน (`My Collection`) | R11 | PLANNED | [[Collection_Dashboard]] | TSK-305 |
| **TSK-402** | ระบบเปลี่ยนสถานะขวดเป็น Finished, Sold, Gifted | R26 | PLANNED | [[Collection_Dashboard]] | TSK-401 |
| **TSK-403** | พัฒนา Analytics Dashboard แยก Ever vs Current | R27 | PLANNED | [[Collection_Dashboard]] | TSK-402 |
| **TSK-404** | แผนภูมิสรุปแนวกลิ่น สัดส่วนแบรนด์ และโน้ตโปรด | R27 | PLANNED | [[Collection_Dashboard]] | TSK-403 |
| **TSK-405** | ระบบวิเคราะห์ราคาเฉลี่ยต่อ mL ย้อนหลัง (Deferred) | R31 | DEFERRED | [[Collection_Dashboard]] | TSK-403 |

---

## 3. Dependencies & Links

- แผนการส่งมอบระยะยาว: [[Roadmap]]
- เกณฑ์ตรวจรับงาน: [[Acceptance_Criteria]]
- ทะเบียนข้อกำหนด: [[Requirements_Register]]

---

## 4. Change Notes

- `2026-11-10`: แปลงข้อกำหนด R01–R31 เป็น 25 งานย่อยใน Backlog พร้อมระบุ Dependencies


## P1 planning and pilot workstream index — 2026-11-10

This dependency sequence refines TSK-101/102/103; those items are not implementation authorization.
No implementation PR exists. All pilot choices are PROPOSED; the owner must merge the accepted plan.

| Task | Type / branch | Plan dependency | State | PR / checkpoint | Next action |
|---|---|---|---|---|---|
| DPT-PLAN-001 | PLAN / plan/p1-data-discovery-schema-foundation | baseline 03481f7066487c44631cb9065899894ee8db71fb | planning_review_ready / acceptance pending | PR #1 OPEN/DRAFT; S2 post-review corrections in [[DPT-PLAN-001_P1_Data_Foundation]] | Owner review of updated proposal |
| IMP-P1-01 | Local schema/migrations | Owner-merged DPT-PLAN-001 + OD-02 | NOT STARTED | NOT CREATED | Verify merge SHA first |
| IMP-P1-02 | Sample Python ETL | 01 + OD-01/OD-06 accepted scope | NOT STARTED | NOT CREATED | Licensed sample only |
| IMP-P1-03 | Image metadata | 01–02 + OD-04 | NOT STARTED | NOT CREATED | Per-asset grant |
| IMP-P1-04 | Benchmark + independent DB/object restore | 01–03 + OD-05 | NOT STARTED | NOT CREATED | Measure, test, independent review |
| IMP-P1-05 | Optional managed-host readiness/migration | 04 + OD-03 and separate operation approval | NOT STARTED | NOT CREATED | No provisioning implied |

Pilot task/test breakdown: [[P1_Pilot_Implementation_Plan]]. TSK-103's four Thai brands remain targets,
not available licensed seed records. Preserve R22 without fabricating product facts or substituting
Butterfly research for those required brands. P2/P3 schema support does not bring their UI into pilot scope.


## Separate documentation CI proposal — NOT STARTED

| Task | State / approval | Scope | Acceptance / boundary |
|---|---|---|---|
| TSK-DOC-001 | PROPOSED, separate future implementation task/PR after owner authorizes CI scope | Markdown/frontmatter/local/wiki-link checks, ERD-dictionary entity/contract parity, immutable receipt and evidence preservation, docs-only scope and secret-pattern checks | Reproduce local checks on a known revision; report actual limits; read-only least-privilege job; no secrets/private exports, deployment, source ingestion or auto-merge |

No GitHub Action, workflow file, branch rule, app permission or CI setting is created by PR #1 corrections.
Owner approval of this proposal alone is not execution approval; future CI implementation defines pinned
tooling, trigger/permission boundaries and test evidence. R1–R3 test cases remain future database/runtime
work, not assertions that documentation CI proves SQL/RLS behavior. OD recommendations: [[P1_Data_Foundation_Plan]].
