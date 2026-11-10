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
source_of_truth: "../../README.md"
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
  - *ข้อดี:* อธิบายเหตุผลได้ชัดเจน (Explainable AI), ตรวจสอบเส้นทางการคำนวณได้ แต่ยังต้องทดสอบความถูกต้องของข้อมูลและตรรกะ
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


## P1 Proposed ADRs — 2026-11-10

These ADRs supplement ADR-001/002 and DEC-008; none is accepted by this PR. Research evidence is
[[P1_Data_Profiling_Findings]]. Human owner decides; implementation waits for merge and accepted scope.

### ADR-003: Evidence-backed portable relational catalogue

- Status: PROPOSED; DEC-012.
- Context: missing country/concentration, flat notes, source taxonomies and conflicting note claims
  contradict a single-source, mandatory-field schema.
- Alternatives: flatten one publisher into perfumes; JSON-only catalogue; normalized SQL plus claims.
- Proposal: normalized PostgreSQL plus typed entity registry, field definitions, immutable source
  observations, explicit canonical selections and conflict memberships. Concentration/edition identifies
  a perfume profile; volume/SKU identifies packaging. Unknowns remain nullable.
- Consequences: more joins/claim storage and trigger/transaction tests, but new sources/mappings can be
  added without replacing canonical IDs or destroying evidence. Core data is provider-independent.
- Acceptance: owner approves identity/provenance complexity; local migration, wrong-kind/cross-source
  negative controls and full claim-to-canonical round-trip verified in IMP-P1-01/02.

### ADR-004: Local pilot before managed PostgreSQL hosting

- Status: PROPOSED; DEC-013.
- Context: no measured database size, runtime or restore evidence exists; free allowance is not capacity proof.
- Alternatives: Vercel + Supabase; Docker/VPS; other managed PostgreSQL (not evaluated in depth).
- Proposal: disposable PostgreSQL pilot first; Vercel web + Supabase PostgreSQL candidate afterwards.
  Keep Python ETL separate from web request lifetimes.
- Consequences: fewer initial cloud mutations, but pilot and eventual host versions/extensions/connection
  behavior must be verified; self-hosting adds server/security/backup operations.
- Acceptance: [[P1_Pilot_Implementation_Plan]] readiness evidence; owner selects region, budget and providers.

### ADR-005: Provider-independent image metadata; storage selection deferred

- Status: PROPOSED; DEC-014.
- Context: dataset has no images; bottle rights and image sizes are unverified.
- Alternatives: Supabase Storage, Cloudflare R2 Standard, local/private object service.
- Proposal: SQL metadata + portable object adapter; choose Supabase for simplicity if capacity fits,
  R2 if measured storage/egress justifies another provider. No external hotlink as storage strategy.
- Consequences: independent asset-rights checks, signing and manifest backups; R2 adds integration work,
  Supabase free storage/egress is smaller. No image acquisition until per-asset grant.
- Acceptance: metadata/rights/hash/derivative tests and measured object workload; owner approves choice.

### ADR-006: Separate DB and object recovery with Docker exit

- Status: PROPOSED; DEC-015.
- Context: a database dump/managed DB backup cannot restore missing image bytes.
- Alternatives: DB-only backups; provider-managed recovery only; independent DB + object exports.
- Proposal: PostgreSQL logical archive, migration/role/auth mapping, separate encrypted bytes and
  manifest, rehearsal on fresh PostgreSQL/container + separate object target.
- Consequences: additional backup cost and consistency boundary, but portable recovery evidence.
  Proposed RPO 24h/RTO 2h and retention remain owner decisions, not verified service guarantees.
- Acceptance: full restore, corrupt/missing object and tenant/RLS negative controls; record timings.

Primary technical references and dated costs: [[P1_Storage_Hosting_and_Recovery]]. Source access/reuse
choices are governed by [[Source_Registry]] and [[Rights_and_Attribution]], not a technology ADR.


## Post-review refinements to ADR-003 / ADR-005 — PROPOSED

ADR-003 now requires claim_locator + claim_key identity within one source record, scoped overlay
selections and exact conflict-member resolution. access_scopes/scope_members make public/shared/private
ownership explicit; FK/RLS/authorization rules preserve private claims even about public catalogue entities.
ADR-005 now requires asset_permissions binding exact asset/source/capture/assessment, separate parent
transformation rights and child output-license/use checks, plus authenticated private/shared delivery.
Proposal grows from 44 to 47 logical tables. This increases migration/trigger/RLS/restore tests; it does
not finalize the schema or approve shared-mode activation. Existing alternatives and research remain.
DEC-016/017 record the refinements; owner recommendations OD-01..06 are in [[P1_Data_Foundation_Plan]].
