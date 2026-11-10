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
source_of_truth: "../README.md"
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
| **TSK-101** | สร้าง Next.js + PostgreSQL + Drizzle ORM Setup | - | PLANNED | [[Proposed_System_Architecture]] | TSK-008 |
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
