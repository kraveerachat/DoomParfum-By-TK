---
id: DPT-ENG-002
project: DoomParfum By TK
type: tech_stack_adrs
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - engineering
  - adr
  - decisions
source_of_truth: "../README.md"
---

# Tech Stack and Architecture Decision Records (ADRs) — DoomParfum By TK

> **Document Type:** Technical Choices & ADR Registry
> **Source Baseline:** `../README.md` (Sections 7 & 10)
> **Status:** Draft / Proposed Framework

---

## 1. Purpose / Scope

เอกสารนี้รวบรวมสถานะของสแต็กเทคโนโลยีและบันทึกการตัดสินใจเชิงสถาปัตยกรรม (Architectural Decision Records - ADRs) เพื่อบันทึกบริบท ทางเลือกที่พิจารณา เหตุผลที่เลือก และผลกระทบที่ตามมา

> [!WARNING]
> **กฎการปรับสถานะการตัดสินใจ [CONFIRMED]:**
> ห้าม Agent หรือผู้พัฒนาเปลี่ยนสถานะจาก `[PROPOSED]` เป็น `[ACCEPTED]` โดยพลการ การอนุมัติการตัดสินใจทางสถาปัตยกรรมต้องได้รับความเห็นชอบจากผู้ใช้โดยตรงเท่านั้น

---

## 2. Tech Stack Evaluation Summary

| Layer | Proposed Technology | Alternative Considered | Status | Justification / ADR Reference |
|---|---|---|---|---|
| **Frontend** | **Next.js (App Router)** | Vite + React SPA, Remix | `[PROPOSED]` | รองรับ SSR/SSG สำหรับค้นหาง่าย และมี Server Actions ในตัว |
| **Styling** | **Tailwind CSS + shadcn** | Material UI, CSS Modules | `[PROPOSED]` | ปรับแต่ง UI ง่าย สไตล์โมเดิร์น โค้ดเบา ไม่ผูกมัด Library สำเร็จรูป |
| **Language** | **TypeScript** | JavaScript | `[CONFIRMED]` | ความปลอดภัยเรื่อง Type ของข้อมูลน้ำหอมและโน้ตที่ซับซ้อน |
| **Backend** | **Next.js Route Handlers** | Express / NestJS แยกส่วน | `[PROPOSED]` | รวมศูนย์ในโปรเจกต์เดียว ลดความซับซ้อนในการ Deploy สำหรับ MVP |
| **Database** | **PostgreSQL 16+** | MongoDB, MySQL, SQLite | `[PROPOSED]` | ความสัมพันธ์ของโมเดลข้อมูลสูง รองรับ Trigram และ ACID ครบถ้วน |
| **ORM** | **Drizzle ORM** | Prisma, TypeORM | `[PROPOSED]` | เบากว่า Prisma ไม่มี Binary Engine รันบน Serverless/Edge ได้ดี |
| **Search** | **Postgres Trigram (pg_trgm)** | Meilisearch, Elasticsearch | `[PROPOSED]` | ไม่ต้องตั้งเซิร์ฟเวอร์ Search Engine แยกในระยะแรก |
| **Documentation**| **Obsidian (Markdown Vault)**| Notion, Confluence | `[CONFIRMED]` | [[Decision_Log#DEC-009\|DEC-009]]: เก็บใน Git ควบคุมเวอร์ชันได้ โปร่งใส |

---

## 3. Active Architecture Decision Records (ADRs)

### ADR-001: Selection of Monolithic Next.js + PostgreSQL Architecture
- **Status:** `PROPOSED` (เชื่อมโยง [[Decision_Log#DEC-008|DEC-008]])
- **Context:** ต้องการสร้างเว็บแอปส่วนตัวที่พัฒนาได้รวดเร็ว มีหน้าบ้านสวยงาม และจัดการข้อมูลสัมพันธ์ได้ดี
- **Decision:** เสนอใช้ Next.js เป็น Fullstack App Router เชื่อมต่อกับ PostgreSQL ผ่าน Drizzle ORM
- **Consequences:**
  - *ข้อดี:* โค้ดอยู่ในที่เดียว (Monorepo), แชร์ Types ระหว่างหน้าบ้าน-หลังบ้านได้ 100%, ประหยัดทรัพยากรเซิร์ฟเวอร์
  - *ข้อควรระวัง:* ต้องระวังการเขียนโค้ดที่ผูกติดกับ Next.js มากเกินไปหากในอนาคตต้องการแยก API Service

### ADR-002: Rule-Based Scent Matching over Vector Embedding / ML Training
- **Status:** `PROPOSED` (เชื่อมโยง [[Decision_Log#DEC-006|DEC-006]])
- **Context:** ในช่วงเริ่มต้น ไม่มีชุดข้อมูล Pairwise Labeled Dataset ที่ถูกต้องตามลิขสิทธิ์มากพอที่จะเทรนโมเดล ML
- **Decision:** เริ่มต้นด้วยอัลกอริทึมเชิงโครงสร้างแบบ Rule-Based (Pyramid + Accords + Evidence)
- **Consequences:**
  - *ข้อดี:* อธิบายเหตุผลได้ชัดเจน (Explainable AI), ปราศจาก Hallucination, ควบคุมผลลัพธ์ได้ 100%
  - *ข้อควรระวัง:* ความแม่นยำขึ้นอยู่กับคุณภาพและความสมบูรณ์ของการจัดระเบียบโน้ต

---

## 4. ADR Governance & Lifecycle

เมื่อมีการตัดสินใจทางเทคนิคใหม่ ให้ใช้เทมเพลต [[ADR_Template]] ในการร่าง และบันทึกสถานะตามลำดับ:
1. `DRAFT` (ร่างโดยทีมหรือ Agent)
2. `PROPOSED` (นำเสนอต่อผู้ใช้)
3. `ACCEPTED` (ผู้ใช้อนุมัติ) หรือ `REJECTED` (ปฏิเสธ)
4. `SUPERSEDED` (ถูกแทนที่ด้วยการตัดสินใจใหม่)

---

## 5. Requirements Covered

- [[Requirements_Register#R01|R01]], [[Requirements_Register#R16|R16]]
- การควบคุมการตัดสินใจ: DEC-001 ถึง DEC-009 ใน [[Decision_Log]]

---

## 6. Dependencies & Links

- สถาปัตยกรรมระบบ: [[Proposed_System_Architecture]]
- บันทึกการตัดสินใจ: [[Decision_Log]]
- แม่แบบ ADR: [[ADR_Template]]

---

## 7. Change Notes

- `2026-11-10`: รวบรวมสรุปการเลือกเทคโนโลยีและร่าง ADR-001, ADR-002
