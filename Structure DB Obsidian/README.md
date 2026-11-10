---
id: DPT-VAULT-001
project: DoomParfum By TK
type: vault_guide
status: active
owner: project
updated: 2026-11-10
tags: [doomparfum, documentation]
source_of_truth: "../README.md"
---

# DoomParfum By TK — Obsidian Knowledge Base Guide & Conventions

> **Target vault:** `DoomParfum By TK/Structure DB Obsidian/`
> **Source of truth:** `../README.md`
> **Version:** `1.0.0-baseline` · Updated: `2026-11-10` (Asia/Bangkok)
> **Status:** **Active Knowledge Base** (Initial Bootstrap Completed)

---

## 0. วัตถุประสงค์และข้อกำหนดการใช้งาน Vault

เอกสารชุดนี้เป็น **Living Knowledge Base** ของโปรเจกต์ `DoomParfum By TK` สำหรับจัดเก็บข้อกำหนด แบบจำลองโดเมน โครงสร้างข้อมูล อัลกอริทึมการจับคู่กลิ่น การออกแบบ UX สถาปัตยกรรมระบบ แผนงานส่งมอบ และประวัติการตัดสินใจ

### นโยบายการอัปเดตและข้อกำหนดความโปร่งใส
1. **Source Precedence:** `AGENTS.md` $\rightarrow$ `DEVELOPMENT_WORKFLOW.md` $\rightarrow$ `../README.md` $\rightarrow$ Accepted Obsidian Notes $\rightarrow$ Git code/evidence
2. **สถานะการตัดสินใจชัดเจน:** แยก `[CONFIRMED]`, `[PROPOSED]`, `[RESEARCH]`, `[DEFERRED]` ทุกครั้ง ห้ามเปลี่ยนสถานะเป็น Accepted หรือ Confirmed โดยพลการ
3. **Data Integrity:** ข้อมูลโน้ตและพีระมิดกลิ่นคือ Olfactory Perception ไม่ใช่สูตรเคมี ห้ามแต่งข้อมูลเท็จ (No Fabricated Data) ห้ามสร้างราคาหรือคะแนนรีวิวลอยๆ
4. **No Direct Push After Bootstrap:** การสร้างคลังเริ่มต้นขึ้น `origin/main` เป็น **ข้อยกเว้นที่ได้รับอนุญาตจาก Human Owner เพียงครั้งเดียว** เนื่องจากคลัง Remote ยังว่างเปล่า การเปลี่ยนแปลงสำคัญหลังจากนี้ทั้งหมดต้องดำเนินตาม **Two-Gate Workflow** (Planning PR $\rightarrow$ Owner Merge $\rightarrow$ Implementation PR $\rightarrow$ Owner Merge) ตามที่ระบุใน `../DEVELOPMENT_WORKFLOW.md`

---

## 1. ผังโครงสร้าง Vault (Vault Directory Map)

```text
Structure DB Obsidian/
├── README.md                                # คู่มือและกฎระเบียบของ Vault (เอกสารนี้)
├── 00_Home/                                 # ศูนยกลางและสถานะโครงการ
│   ├── Project_Index.md                     # Map of Content (MOC) และดัชนีนำทางหลัก
│   └── Project_Status.md                    # สถานะปัจจุบัน, Blockers และแผนงานถัดไป
├── 01_Product/                              # ข้อกำหนดเชิงผลิตภัณฑ์
│   ├── Vision_and_Scope.md                  # วิสัยทัศน์, Pain Points, Target Budget และ Non-goals
│   ├── Requirements_Register.md             # ทะเบียนข้อกำหนด R01 ถึง R31 และ Traceability Matrix
│   ├── User_Stories_and_Flows.md            # เรื่องราวผู้ใช้และโฟลว์หลักทั้ง 5 สเต็ป (A ถึง E)
│   ├── Feature_Priorities.md                # การจัดลำดับความสำคัญตามระยะการส่งมอบ
│   └── Open_Product_Questions.md            # รวมคำถามผลิตภัณฑ์ที่รอความเห็นชอบจากผู้ใช้
├── 02_Domain/                               # แบบจำลองเชิงธุรกิจและอนุกรมวิธาน
│   ├── Domain_Model.md                      # 7 Bounded Contexts และ Invariant Rules
│   ├── Brand_Taxonomy.md                    # การจำแนกประเทศและตำแหน่งตลาด + Thai Brand Registry
│   ├── Perfume_and_Note_Taxonomy.md         # Perfume vs Variant vs Listing, ชั้นพีระมิดโน้ต
│   └── My_Cart_and_Ownership.md             # In-App Cart (No Checkout), Ordered, Owned, History
├── 03_Data/                                 # สถาปัตยกรรมข้อมูลและธรรมาภิบาล
│   ├── ERD_Draft.md                         # ผังความสัมพันธ์เอนทิตี (Mermaid ERD)
│   ├── Data_Dictionary_Draft.md             # P1 proposed dictionary (44 logical tables, awaiting owner review)
│   ├── Source_Registry.md                   # ทะเบียนแหล่งข้อมูลภายนอกและสถานะสิทธิ์
│   ├── Ingestion_and_ETL.md                 # ไปป์ไลน์นำเข้า ทำความสะอาด และตรวจสอบคุณภาพ
│   ├── Data_Quality_and_Provenance.md       # ธรรมาภิบาลข้อมูล ที่มาของข้อมูลระดับฟิลด์
│   └── Rights_and_Attribution.md            # นโยบายลิขสิทธิ์ สิทธิ์เข้าถึง และการอ้างอิง
├── 04_Matching/                             # กลไกการจับคู่กลิ่น
│   ├── Scent_Matching_Spec.md               # สูตรคำนวณคะแนนความคล้าย (Proposed: 40/25/15/20)
│   ├── Review_Evidence_and_Confidence.md    # การจัดเก็บหลักฐานรีวิว และค่าความเชื่อมั่น
│   └── Matching_Test_Cases.md               # กรณีทดสอบจำลองเชิงสังเคราะห์
├── 05_UX/                                   # การออกแบบหน้าจอและประสบการณ์ผู้ใช้
│   ├── Site_Map_and_Screens.md              # แผนผังการนำทางและภาพรวม 6 หน้าจอหลัก
│   ├── Perfume_Detail_Pyramid.md            # หน้ารายละเอียดและพีระมิดโน้ตพร้อมภาพ
│   ├── Compare_View.md                      # หน้าจอเปรียบเทียบ Side-by-Side ไฮไลต์สีโน้ต
│   ├── Shopping_Tracker.md                  # หน้าจอจัดการตะกร้าในแอป บันทึกหลายร้าน Shopee
│   └── Collection_Dashboard.md              # หน้าจอจัดการคอลเลกชันและแดชบอร์ดสถิติ
├── 06_Engineering/                          # สถาปัตยกรรมเทคนิคและความปลอดภัย
│   ├── Proposed_System_Architecture.md      # Next.js + PostgreSQL + Drizzle ORM (Proposed)
│   ├── Tech_Stack_and_ADRs.md               # การประเมินสแต็กและทะเบียน ADR
│   ├── Security_and_Privacy.md              # นโยบายความปลอดภัย การคุ้มครองข้อมูลส่วนบุคคล
│   └── GitHub_and_Workflow_PENDING.md       # เวิร์กโฟลว์ Git Two-Gate Development Workflow
├── 07_Delivery/                             # การส่งมอบและติดตามงาน
│   ├── Roadmap.md                           # แผนการส่งมอบระยะ P0 ถึง P6
│   ├── Backlog.md                           # รายการงานย่อยผูกโยงกับ Requirement IDs
│   ├── Acceptance_Criteria.md               # เกณฑ์การตรวจรับงานแบบวัดผลได้จริง
│   ├── Tasks/                               # บันทึกสถานะงานราย Task
│   └── Planning_PRs/                        # ข้อมูลจำเพาะสำหรับ Planning PRs
├── 08_Operations/                           # บันทึกการดำเนินงานและหลักฐาน
│   ├── Decision_Log.md                      # ทะเบียนการตัดสินใจ DEC-001 ถึง DEC-011
│   ├── Change_Log.md                        # ประวัติการปรับปรุงข้อกำหนดและโครงสร้าง
│   ├── Agent_Run_Log.md                     # บันทึกประวัติการทำงานของ Agent แต่ละรอบ
│   ├── Pending_Questions.md                 # บันทึกคำถามที่ยังค้างอยู่
│   ├── Receipts/                            # ใบเสร็จสรุปงานและผลทดสอบ (Immutable Receipts)
│   └── Handoffs/                            # ชุดส่งต่องานระหว่าง Agent (Continuity Packs)
├── 09_References/                           # ดัชนีแหล่งอ้างอิง
│   └── Reference_Index.md                   # ดัชนีลิงก์ เอกสารเทคนิค และสถานะสิทธิ์
└── 90_Templates/                            # แม่แบบมาตรฐาน
    ├── Feature_Spec_Template.md             # แม่แบบข้อกำหนดฟีเจอร์ใหม่
    └── ADR_Template.md                      # แม่แบบบันทึกการตัดสินใจสถาปัตยกรรม (ADR)
```

---

## 2. มาตรฐานการเขียนเอกสาร (Markdown & Frontmatter Conventions)

ทุกไฟล์เอกสารหลักใน Vault ต้องมี YAML Frontmatter ดังนี้:

```yaml
---
id: DPT-XXX-001
project: DoomParfum By TK
type: specification
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - planning
source_of_truth: "../README.md"
---
```

- **Wiki Links:** ใช้ `[[Project_Status]]` สำหรับเชื่อมโยงระหว่างเอกสารภายใน Vault
- **Visuals:** ใช้ Mermaid Diagrams สำหรับผังลำดับขั้นตอน, ERD, และสถาปัตยกรรม
- **No Private Data / Secrets:** ห้ามใส่ API keys, Tokens, คุกกี้ Shopee หรือข้อมูลส่วนบุคคลลงใน Vault
- **No Auto-Generated Plugin Bloat:** ไม่ Commit ไฟล์คอนฟิกส่วนตัวของโปรแกรม Obsidian เช่น `.obsidian/workspace*.json`


## P1 discovery navigation — PROPOSED, 2026-11-10

- [[P1_Data_Foundation_Plan]] — task map, requirements, acceptance and owner decisions.
- [[DPT-PLAN-001_P1_Data_Foundation]] — session/tool/Git evidence and exact changed files.
- [[P1_Data_Profiling_Findings]], [[P1_Source_to_Canonical_Mapping]], [[P1_Data_Conflict_Matrix]].
- [[P1_Storage_Hosting_and_Recovery]], [[P1_Pilot_Implementation_Plan]].

These refine the bootstrap draft; no final schema/hosting approval or implementation is implied.
