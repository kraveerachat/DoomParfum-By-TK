---
title: DoomParfum Unified Development Workflow
aliases:
  - DoomParfum Agent Workflow
  - DoomParfum Git PR Obsidian Workflow
  - DoomParfum Development Governance
project: DoomParfum By TK
type: governance
status: accepted
version: 1.1.0
updated: 2026-11-20
timezone: Asia/Bangkok
owner: human-owner
source_documents:
  - AEGIS_Unified_Development_Workflow.md
  - AEGIS_Multi_Agent_Development_Workflow_Prompt_v2.md
  - README.md
  - Structure DB Obsidian/README.md
tags:
  - doomparfum
  - workflow
  - multi-agent
  - git
  - github
  - obsidian
  - governance
---

# DoomParfum By TK — Unified Development Workflow

> **เอกสาร Workflow กลางเพียงไฟล์เดียว** สำหรับการวางแผน, การทำงานของ ChatGPT/Codex/Claude Code/Gemini, การเขียนโค้ด, การทดสอบ, GitHub Pull Requests, Obsidian documentation, การตรวจรับโดยเจ้าของโปรเจกต์ และการส่งต่อระหว่างแชต/Agent
> **สถานะ `accepted`:** Human Owner merged Planning PR #1 on 2026-11-10 at `bffb2fab1918dc5221a6c5da7920168bcae263ca`. Gate P is verified for the bounded local pilot; every Implementation PR still requires owner review/merge. Production/cloud/deferred decisions are not approved by inference.
> **เอกสารนี้เป็นกฎการทำงาน ไม่ใช่หลักฐานว่าได้สร้าง Repository, Branch, Pull Request, Obsidian Vault หรือเขียนโค้ดแล้ว**

## 0. TL;DR — กฎหลักที่ต้องทำตาม

**DoomParfum ใช้ Workflow สองประตู (two-gate) โดยแยกการอนุมัติแผนออกจากการพัฒนาโค้ดจริง:**

```text
IDEA / REQUEST
   ↓
CHATGPT + OWNER: REQUIREMENTS, TASK MAP, RISKS, ACCEPTANCE
   ↓
PLANNING BRANCH + PLANNING PR (docs-only)
   ↓
OBSIDIAN PLAN / ARCHITECTURE / DECISIONS UPDATED
   ↓
OWNER REVIEWS & MERGES PLANNING PR  ← GATE P (mandatory)
   ↓
CODING AGENT: BRANCH FROM LATEST MAIN + IMPLEMENTATION PR
   ↓
TDD / TEST / REVIEW + OBSIDIAN CHECKPOINTS
   ↓
PR READY FOR REVIEW + EXACTLY ONE FINAL RECEIPT
   ↓
OWNER REVIEWS & MERGES IMPLEMENTATION PR ← GATE I
   ↓
POST-MERGE RECONCILIATION + NEXT TASK
```

กฎพื้นฐาน:

1. **หนึ่งงานที่ตรวจรับได้ (`reviewable task`) → หนึ่ง branch → หนึ่ง PR → หนึ่ง final immutable receipt**; สำหรับงานพัฒนาฟีเจอร์ใหม่ **มีอย่างน้อยสองงานที่แยกกัน** คือ *Planning Task/PR* และ *Implementation Task/PR*. อย่ารวมสอง PR เป็นก้อนเดียว หรือถือว่าหนึ่งฟีเจอร์ต้องมีเพียงหนึ่ง PR ตลอดอายุงาน.
2. **Planning PR ห้ามสร้างหรือแก้ runtime/source code** ยกเว้น scaffolding ด้านเอกสารที่ประกาศไว้ใน Scope; รวม Requirements, ADR, ERD Draft, Acceptance และ Implementation Plan. แผนยังใช้เขียนโค้ดไม่ได้จนเจ้าของโปรเจกต์ Merge แผนที่อนุมัติแล้ว.
3. **Implementation PR ต้องเริ่มจาก `main` หลัง Planning PR ถูก Merge และอ้างอิง Planning PR/commit SHA ที่อนุมัติ**; Agent สามารถตัดสินใจเปิด/แยก Implementation PR ภายในแผนที่อนุมัติได้หากมีสิทธิ์ GitHub แต่ห้าม Merge เอง.
4. **ทุก meaningful change ต้องบันทึกลง Markdown ใน `Structure DB Obsidian/`** ก่อนหรือระหว่าง checkpoint ที่เกี่ยวข้อง และก่อนประกาศว่างานจบ; Obsidian กับโค้ดต้องอธิบายสถานะเดียวกัน.
5. **สิ่งที่ลง PR ต้องมาจากหลักฐาน**: รายงานเปลี่ยนไฟล์อะไร, ทดสอบอะไร, ผ่าน/ล้ม, ข้อจำกัด, branch/commit SHA, และสิ่งที่ยังไม่ทำ. `SOURCE IMPLEMENTED` ไม่เท่ากับ `VERIFIED`, `DEPLOYED` หรือ `CLOSED`.
6. **Human Owner เป็นคนอนุมัติ Scope สำคัญ, Planning PR, Production mutation และการ Merge ทุก PR**. Agent ห้าม force-push, ลบข้อมูล, เปลี่ยน Production, ตั้งค่า GitHub protection หรือเปิดเผยข้อมูลลับเอง.
7. **เอกสารและ Source Code อยู่ใน Git Repository เดียวกันเป็นค่าเริ่มต้น** เพื่อให้ PR หนึ่งรายการตรวจสอบความสัมพันธ์ของ Code/Docs ได้. ถ้าต้องแยก Vault เป็นอีก Repo ให้จัดทำ ADR และรับอนุมัติก่อน.
8. **ใช้ AI/ETL/Scraping เฉพาะแหล่งที่สิทธิ์และเงื่อนไขอนุญาต**. การพบ GitHub Scraper ไม่ใช่การอนุญาตให้ Scrape Fragrantica, Shopee หรือรีวิวบุคคลที่สาม.

> [!NOTE]
> **One-time Initial Empty-Repository Bootstrap Exception (2026-11-10):**
> การสร้างและ Push Initial Documentation Baseline ขึ้นสู่ `origin/main` โดยตรงในครั้งแรกนี้ เป็น **ข้อยกเว้นพิเศษที่ได้รับความเห็นชอบและอนุมัติจาก Human Owner เพียงครั้งเดียว** เนื่องจากคลัง Remote บน GitHub ยังว่างเปล่า การทำงาน งานวางแผน และงานพัฒนาฟีเจอร์หลังจากนี้ทั้งหมด ต้องปฏิบัติตามกระบวนการ Two-Gate PR Workflow (Planning PR $\rightarrow$ Gate P $\rightarrow$ Implementation PR $\rightarrow$ Gate I) อย่างเคร่งครัด

---

## 1. ขอบเขตและเอกสารอ้างอิงของ DoomParfum

### 1.1 Product context ที่ต้องรักษา

DoomParfum By TK เป็น **Private-first perfume research and collection web app** สำหรับค้นหาน้ำหอม, Perfume Pyramid (Top/Heart/Base พร้อมภาพ), Scent DNA Matching จาก Notes/Accords และหลักฐานรีวิว, ทางเลือก Designer/Niche → ไทย/อาหรับ/อินโดนีเซีย, Personal Cart, Buying Sources, Manual Ordered/Owned/Purchase History และ Collection Dashboard.

**ไม่ใช่แพลตฟอร์ม Checkout หรือระบบจัดการออเดอร์ใน Shopee จริง**. ห้าม Coding Agent แปลง `My Cart` เป็นระบบชำระเงินเพราะเห็นคำว่า `Cart`. ดู Requirements `R01–R31` และสถานะการยืนยันใน `README.md` ก่อนเสนอ Feature ใหม่.

### 1.2 Paths ที่ใช้ร่วมกัน (case-sensitive และมีช่องว่าง)

```text
DoomParfum By TK/
├── README.md                                # Product blueprint / requirement baseline
├── DEVELOPMENT_WORKFLOW.md                  # THIS FILE: canonical workflow after owner approval
├── AGENTS.md                                # Recommended agent entry point (to be created by approved PR)
├── Structure DB Obsidian/                   # Canonical Obsidian vault; part of same Git repository
│   ├── README.md                            # Original vault bootstrap / structure contract
│   ├── 00_Home/Project_Index.md
│   ├── 00_Home/Project_Status.md
│   ├── 01_Product/Requirements_Register.md
│   ├── 02_Domain/...
│   ├── 03_Data/...
│   ├── 04_Matching/...
│   ├── 05_UX/...
│   ├── 06_Engineering/...
│   ├── 07_Delivery/Roadmap.md
│   ├── 07_Delivery/Backlog.md
│   ├── 07_Delivery/Tasks/                    # NEW WHEN BOOTSTRAPPED: per-task canonical notes
│   ├── 07_Delivery/Planning_PRs/             # NEW WHEN BOOTSTRAPPED: planning PR specifications
│   ├── 08_Operations/Decision_Log.md
│   ├── 08_Operations/Change_Log.md
│   ├── 08_Operations/Agent_Run_Log.md
│   ├── 08_Operations/Receipts/                # NEW WHEN BOOTSTRAPPED: immutable final receipts
│   ├── 08_Operations/Reports/<TOPIC_ID>/      # per-session execution reports (§4.7)
│   ├── 08_Operations/Handoffs/                # NEW WHEN BOOTSTRAPPED: continuity packs
│   ├── 09_References/...
│   └── 90_Templates/...
├── web/                                     # FUTURE, only after approved implementation plan
├── data-pipeline/                           # FUTURE
├── database/                                # FUTURE
└── .github/                                 # FUTURE, only after repository/GitHub approval
```

> โครงสร้างที่ขึ้นคำว่า `NEW WHEN BOOTSTRAPPED` หรือ `FUTURE` เป็น *ตำแหน่งที่กำหนดไว้สำหรับ Agent สร้างใน PR ที่ได้รับมอบหมาย* ไม่ได้แปลว่ามีไฟล์จริงแล้ว. ถ้าโฟลเดอร์ยังไม่มี ให้สร้างภายใต้ Planning/Bootstrap PR ตามสิทธิ์ที่ได้รับ. ในคำสั่ง Shell ให้ quote paths ที่มีช่องว่าง เช่น `"Structure DB Obsidian/07_Delivery/Tasks"`.

### 1.3 ลำดับแหล่งความจริงและการแก้ความขัดแย้ง

1. Repository policy ที่ใช้ได้จริง (`AGENTS.md`, branch protection, security rules) และสิทธิ์เครื่องมือที่ได้รับ.
2. คำสั่งล่าสุดที่เจ้าของโปรเจกต์ให้โดยชัดเจน ภายในขอบเขตที่ไม่ขัด repository policy หรือข้อกำหนดความปลอดภัย.
3. Git state ปัจจุบัน, PR ที่ใช้งานจริง, source/tests และ evidence ที่ตรวจสอบย้อนกลับได้.
4. `README.md` และ Obsidian docs ที่ได้รับอนุมัติ/ผ่าน Planning PR แล้ว.
5. Workflow นี้ (เมื่อถูกยอมรับเป็น canonical) และ accepted ADRs/receipts.
6. Draft/Proposed docs, คำตอบ AI และแชตเก่าเป็นข้อมูลประกอบ ไม่ใช่หลักฐานว่าโค้ดพร้อมใช้งาน.

ถ้าเอกสาร/แผนขัดกับ code หรือ PR ล่าสุด **อย่าแก้เงียบ ๆ**; ระบุ conflict + evidence + เสนอ reconciliation PR หรือขอการตัดสินใจ. ห้ามเปลี่ยน `[PROPOSED]` เป็น `[CONFIRMED]` เพียงเพราะ Agent เห็นว่าเหมาะสม.

---

## 2. บทบาทและสิทธิ์ของ Agent

| ผู้ดำเนินการ | งานหลัก | ขอบเขตที่ห้ามข้าม |
|---|---|---|
| **Human Owner** | กำหนดทิศทาง/Scope, ตรวจและ Merge Planning PR, ตรวจและ Merge Implementation PR, อนุมัติ Production/Data Source/Secrets | ไม่จำเป็นต้องเขียนโค้ดเอง แต่เป็น final approval gate |
| **ChatGPT** | Planner, Architect, Requirements/Task Map, Risk & Acceptance Gate, Independent Review, Agent Prompt, Chat Continuity | ไม่อ้างว่ารัน tests/เปิด PR/อ่าน repo ล่าสุดแล้ว หากไม่มี evidence/เครื่องมือเข้าถึง |
| **Codex** | Primary Implementation Agent, TDD, code, unit/integration test, debugging, source commit/push/PR ตามสิทธิ์ | ไม่ Merge, ไม่ Force Push, ไม่แก้ Production โดยปริยาย, ไม่ออกนอก approved plan |
| **Claude Code** | Alternative Implementation/Debug Agent สำหรับอ่านหลายไฟล์, trace bug, targeted fix | ห้ามแก้ worktree/ไฟล์เดียวกันพร้อมกับ Codex โดยไม่แบ่ง scope |
| **Gemini / Documentation Agent** | Obsidian status, ERD/Docs/Session Register/PR description reconciliation, research summary ที่มี source | โหมด Docs-only ห้ามแก้ app code หรืออ้างผลทดสอบที่ไม่ได้ตรวจ |
| **ETL / Research Agent** | ตรวจ schema แหล่งข้อมูล, import licensed datasets, validate provenance, deduplicate | ห้าม ingest เนื้อหาที่ไม่มีสิทธิ์, เก็บ session token, bypass anti-bot, ตีค่าข้อมูลที่หายเอง |

**Routing by complexity (S5 of DPT-GOV-WORKFLOW-001):** prefer Claude Code for high-complexity architecture, security and cross-document history work, and Codex for bounded implementation, tests and fixes. The choice never waives an approval gate, the Owner-only merge, or reviewer independence.

> Agent แต่ละตัวทำหลายบทบาทได้เมื่อผู้ใช้มอบหมาย แต่ **บทบาทและ permissions ต้องระบุใน Task Map ทุกครั้ง**. งานเล็กใช้ Agent เดียวสำหรับ code+docs ได้; งานเสี่ยงสูงให้แยก Coding/Review/Docs.

### 2.1 Tool recommendation block (ต้องมีใน handoff ที่สั่ง Agent ทำงาน)

```text
TOOL RECOMMENDATION
TASK: <task-id/title>
AGENT: CHATGPT / CODEX / CLAUDE CODE / GEMINI / ETL AGENT / HUMAN OWNER
MODE: planning / implementation / review / docs / data / production
WHY: <specific capability>
APPROVED_PLAN_PR: <# / NA>
PRODUCTION_MUTATION_ALLOWED: NO (default)
GIT_WRITE_ALLOWED: YES/NO (per granted access)
OBSIDIAN_WRITE_ALLOWED: YES/NO
HUMAN_MERGE_REQUIRED: YES
```

---

## 3. Two-Gate GitHub Workflow — ส่วนที่ปรับเฉพาะ DoomParfum

### 3.1 นิยามและข้อบังคับ

- **Planning Task**: งานที่สร้าง/ปรับ Requirement, Domain Model, Architecture, ADR, UI screen specification, Data Source Policy, Data Dictionary, Acceptance. Review unit เป็นเอกสาร.
- **Planning PR**: PR `plan/...` → `main`; **docs-only**; เป็นจุดที่ Human Owner ตรวจให้แผนใช้งานจริงก่อนเขียน Code.
- **Implementation Task**: งานทำ Source/Test/Migration ตาม approved plan; แยกเป็นหน่วยเล็กที่ทดสอบและรีวิวได้.
- **Implementation PR**: PR `feat/...`, `fix/...`, `data/...`, `test/...` → `main`; โค้ด + tests + Obsidian evidence ใน branch เดียวกัน.
- **Checkpoint**: commit ที่อธิบายผลจริงของ sub-session; **checkpoint ไม่ได้สร้าง PR ใหม่เสมอ**.
- **Immutable Receipt**: รายงานปิดงานหนึ่งใบต่อ reviewable task/PR; ไม่สร้างทุก session, ไม่แก้ไฟล์ receipt เดิมย้อนหลัง.

**ความสัมพันธ์ที่ต้องรักษา:**

```text
DPT-PLAN-001 → plan/p0-domain-model → Planning PR #P
   │  Owner merges PR #P to main
   └─ approved_plan_commit=<SHA>
       ├─ DPT-IMP-001 → feat/perfume-catalogue → Implementation PR #I1
       ├─ DPT-IMP-002 → feat/note-pyramid → Implementation PR #I2 (if independent)
       └─ DPT-IMP-003 → feat/scent-matching → Implementation PR #I3 (after dependency)
```

ค่า `#P/#I1` เป็นตัวอย่าง placeholder เท่านั้น. **การอนุมัติ Planning PR ไม่ใช่การอนุมัติ Merge Implementation PR ล่วงหน้า**.

### 3.2 Gate P — Planning PR lifecycle (ก่อน coding)

1. **Read**: `AGENTS.md` ถ้ามี, Workflow นี้, root `README.md`, Obsidian status/requirements/ADR/roadmap, PR/receipts ล่าสุด และ Git state.
2. **Verify**: repo path, remote/visibility, target `main`, HEAD, worktree, active PR, permissions; ถ้า repository ยังไม่พร้อม ให้ทำไฟล์แผนเฉพาะเครื่องและรายงานว่า PR ไม่ได้สร้าง.
3. **Scope**: ทำ hierarchical Task Map; ระบุ impacted `Rxx`, current decision statuses, technical choices ที่ยัง proposed, dependencies, data-license risks, Acceptance Criteria.
4. **Branch**: สร้าง `plan/<slug>` จาก `origin/main` ล่าสุดภายหลังยืนยัน worktree ปลอดภัย. ห้ามทับ branch ที่มีงานอื่นอยู่.
5. **Docs**: สร้าง/อัปเดต canonical Planning Note + เอกสาร Obsidian ที่เกี่ยวข้อง: Requirements, ADR, ERD draft, data source/permissions, UI/UX, roadmap, backlog, test plan, scope และ known unknowns.
6. **Validate**: consistency check ระหว่าง README/Obsidian/Task Map; links, frontmatter, Mermaid/Markdown ถ้าตรวจได้; `git diff --check`; ตรวจไม่ให้มี secrets/copyrighted raw dumps.
7. **Checkpoint + PR**: stage exact paths, commit docs, push branch และเปิด **Draft Planning PR** ถ้าได้สิทธิ์. PR body ต้องมี Plan Summary, Requirements, Alternatives, Architecture, Acceptance, Risks, Open Decisions, Source Links และ `IMPLEMENTATION_NOT_STARTED=YES`.
8. **Owner decision**: เจ้าของรีวิวและขอแก้ใน PR เดิมได้; เมื่อแผนได้รับการยอมรับจึงเปลี่ยน Ready และ **เจ้าของเป็นผู้ Merge**.
9. **Gate proof**: ก่อนส่งให้ Coding Agent ต้องยืนยัน `planning_pr=MERGED`, `approved_plan_sha`, `target_main_sha`, `accepted_scope`. ถ้าไม่ได้ยืนยัน ห้ามเริ่ม feature implementation.

**Planning PR Acceptance Gate:** requirements traceability, decisions approved/explicitly deferred, architecture feasibility, data rights, schema/UX proposals, task breakdown, test expectations, security/privacy, migration/rollback considerations (เมื่อเกี่ยวข้อง) และ reviewer-ready documentation.

### 3.3 Gate I — Implementation PR lifecycle (หลัง Planning PR Merge)

1. Fetch และยืนยัน `main` มี Planning PR ที่ Merge แล้วจริง; เช็ก SHA/approved plan revision. ไม่เริ่มจาก branch แผนที่ยัง Draft.
2. Agent เลือกหน่วยงาน Implementation ที่ review ได้ตาม Dependency DAG ใน approved plan. **Agent สามารถเปิด Implementation PR เองได้** หากได้รับ write permission และอยู่ใน approved scope; ไม่ต้องขออนุญาตทุก PR ย่อยที่เป็นไปตามแผน แต่ต้องรายงาน ID/branch/PR ให้เจ้าของทราบ.
3. สร้าง `feat/<slug>`/`fix/<slug>`/`data/<slug>` จาก updated `main` (หากใช้ stacked PR ต้องระบุ base/dependency และได้รับอนุมัติเป็นกรณี).
4. Update task/session note ใน Obsidian เป็น `IN PROGRESS` ก่อน meaningful edits, ใส่ branch, starting SHA, plan ref, planned tests, safety boundary.
5. ทำ TDD/Implementation, focused test, regression, build/lint/type-check, data validation/security negative controls ที่เกี่ยวข้อง.
6. Checkpoint: Code/Test และ Obsidian ต้องเคลื่อนตามกัน. Agent เดียวทำพร้อมกันได้; หากมี Docs Agent ต้อง sync docs จาก exact code commit/test evidence ก่อนปิด session.
7. Push task branch; สร้าง/อัปเดต Draft Implementation PR พร้อม test evidence, changed files, known limitations, Obsidian links, Planning PR link และ reference SHA.
8. Independent review ตรวจ source จริง, tests semantics, migration/data-rights/security และ PR SHA. ถ้าพบ defect ให้แก้ใน PR/branch เดิม ไม่สร้าง PR ใหม่โดยไร้เหตุผล.
9. หลังครบ acceptance สร้าง **final immutable receipt หนึ่งใบ**, reconcile docs+PR, validation ผ่าน จึง Ready for Review.
10. **Human Owner review/merge**. เมื่อ Merge แล้วให้บันทึกผลการ Merge และ post-merge checks ใน canonical status note ผ่านการเปลี่ยนแปลงที่ traceable; ไม่กลับไปแก้ immutable receipt เก่า.

**Implementation PR ≠ automatic deployment:** หลัง Merge ยังเป็น repository code; deployment ที่เปลี่ยนระบบจริงต้องผ่าน Production Gate ต่างหาก.

### 3.4 เมื่อแผนเปลี่ยนระหว่าง Implementation

- การเปลี่ยนเล็กน้อยที่ **ยังอยู่ใน intent/acceptance เดิม**: อัปเดต Task Note/ADR/Obsidian พร้อมเหตุผลใน implementation PR เดิม และให้ Reviewer ตรวจ.
- การเปลี่ยน Domain Model, architecture, UX flow, data ingestion rights, matching score semantics, app cart/purchase semantics หรือ scope สำคัญ: **หยุดงานที่ขยายขอบเขต**, เปิด **Planning Amendment PR** (docs-only) ใหม่ก่อน แล้วรอ Human Merge; หลังจากนั้นจึง implement งานส่วนเปลี่ยน.
- Bugfix ที่จำเป็นเพื่อให้ acceptance เดิมผ่าน: ทำได้ใน implementation PR เดิมถ้าอยู่ใน scope พร้อม regression test.
- ห้าม silently rewrite approved plan เพื่อให้ตรงกับโค้ดที่เขียนเกิน scope.

### 3.5 Split / Umbrella / Successor PR

- 1 initiative อาจมีหลาย planning/implementation PR; ใช้ `PR Workstream Index` ใน Obsidian เพื่อ map dependency.
- PR ใหญ่ที่ review ยากต้องแยก successor/sibling task ที่ชัดเจน; update scope/remaining ใน Umbrella PR และ canonical notes.
- **ห้าม claim ว่า feature ใน successor PR เสร็จ** ก่อนมี evidence ของ successor จริง.
- ทุก implementation PR ต้องอ้าง `approved_plan_pr`/`approved_plan_sha` และ `requirements` ที่ตนรับผิดชอบ.
- อย่าให้สอง Agent commit concurrent บน branch เดียวกันโดยไม่มี explicit handoff และการแบ่ง ownership ของไฟล์.

### 3.6 New Task Intake and PR Routing

Run this intake for every new meaningful prompt **before** creating a branch, commit, or PR. `AGENTS.md` §2.1 summarizes it; this section is the full procedure.

**Step 1 — Identify.** Record the project, task ID (or `UNALLOCATED`), objective, scope, and major workstream.

**Step 2 — Inspect actual state.** Check the current repository, the approved/merged plans, the canonical Obsidian task note and status, the relevant branches and worktrees, and the GitHub PRs (open, Draft, and relevant merged ones). Verify a PR on GitHub. A local branch, a local commit, or a `Draft_PR_Body.md` file does not prove that a PR exists.

**Step 3 — Classify** the request as exactly one of these classes:

| Class | When | Route |
|---|---|---|
| **A. Continuation of an existing reviewable task** | The same reviewable scope and acceptance as an existing task | Reuse the task ID, branch, and open/Draft PR. Append a session to the existing canonical note, update the applicable logs, then checkpoint and update the same PR. |
| **B. New reviewable task** | A distinct, independently reviewable unit | Allocate or verify the task ID, responsible agent, approved plan, and dependencies. Create the canonical task note with scope and acceptance, create a new branch from verified latest `main` (§5.1 naming), open a new Draft PR, and link related tasks and PRs. |
| **C. Scope change requiring a planning amendment** | The work exceeds the approved plan's intent or acceptance (§3.4) | Stop the out-of-scope work, open a docs-only Planning Amendment PR, and wait for Human Merge before implementing the change. |
| **D. Read-only review or audit** | The assignment is review/audit only | No branch or PR. Follow §6.2.1 if the reviewer is forbidden to write. |

**Step 4 — Route** as in the table, and record the class in the session record (§4.4).

**Do not create a new PR** merely because a new agent session started, the context was cleared, the task has a new review revision number, new review findings arrived, an in-scope bug was fixed, or another test was run.

**Do not reuse an existing PR** when the new work needs a separate governance gate, a separate implementation phase, or an independently reviewable scope. Belonging to the same initiative is not enough. Planning work stays docs-only (§3.1). Implementation still requires a merged Planning PR (Gate P), and a new implementation task cannot bypass Gate P by attaching itself to an existing PR of the same initiative.

*Example:* DPT-GATE-012 / U01 revisions r11 → r12 → r13 can stay in one documentation/review workstream while the reviewable task and scope are unchanged (class A). U01 implementation is a separate task that needs its own approved Planning PR first (class B or C).

Never create a duplicate PR for the same reviewable task, and never combine unrelated tasks in one PR for convenience.

---

## 4. Session & Task Governance

### 4.1 Task states

| Task state | ความหมาย |
|---|---|
| `NOT STARTED` | มี Backlog แต่ยังไม่เปิดงาน |
| `PLANNED` | มีแผน Draft/Approved แต่ยังไม่เริ่ม implementation |
| `IN PROGRESS` | Agent กำลังทำงานใน branch/PR |
| `BLOCKED` | มี dependency/permission/error ขัดขวาง |
| `SOURCE IMPLEMENTED` | เขียน source แล้ว แต่ยังไม่ครบ evidence |
| `LOCAL VERIFIED` | local tests ที่กำหนดผ่าน |
| `ACCEPTANCE PENDING` | evidence พร้อมบางส่วน แต่ยังไม่ครบ acceptance หรือรอ Human Review |
| `READY FOR REVIEW` | ผ่าน gates ฝั่ง Agent และส่ง Human Review |
| `MERGED` | Human Merge แล้วตาม GitHub evidence |
| `CLOSED` | acceptance/merge/post-merge steps ที่กำหนดเสร็จและ docs reconcile แล้ว |

**ต้องไม่ใช้ `PASS/CLOSED/DEPLOYED` แทนกัน:** `READY FOR REVIEW` ยังไม่ใช่ `MERGED`; `MERGED` ยังไม่ใช่ `PRODUCTION DEPLOYED`.

### 4.2 Task overview (Obsidian note)

สร้าง `Structure DB Obsidian/07_Delivery/Tasks/<TASK_ID>_<slug>.md` ภายใน Planning/Implementation branch ตามชนิดงาน:

```markdown
---
id: DPT-TASK-001
project: DoomParfum By TK
type: task
status: in-progress
updated: YYYY-MM-DD
requirements: [R01, R03]
planning_pr: null
implementation_pr: null
---

# TASK-ID — Task Title

## Current Task
- Type: PLANNING / IMPLEMENTATION / DOCS / DATA / OPERATIONS
- Owner / Agent:
- Branch:
- PR / Target branch:
- Approved Planning PR + SHA (implementation only):
- Current state:
- Started / Last checkpoint:
- Production mutation allowed: NO

## Goal / Why
## In Scope
## Out of Scope
## Dependencies
## Safety / Do-not-touch
## Acceptance Criteria + Evidence Needed
## Task Map (Major Topics + numbered subtasks)
## Session Register
## Planned / Completed / Remaining
## Test / Evidence Ledger
## Issues / Risks / Known Limitations
## Latest Git Checkpoint / SHA
## Handoff / Next Action
```

### 4.3 Meaningful session คือเมื่อไร

นับเป็น meaningful session เมื่อมี source code/migration/test change, schema/architecture decision, data import/source license decision, UI flow/semantics change, security/deployment/config change, integration testing, หรือ defect fix ที่กระทบ accepted behavior.

These also count as meaningful sessions: requirements and planning work, architecture and design documents, unit/integration/security testing, independent (security) reviews, review findings and their remediation, documentation changes, data and database changes, configuration and infrastructure operations, bug fixes, agent handoffs, and final task reports. An independent reviewer under a read-only restriction is covered by §6.2.1 instead.

**ไม่ต้องเปิด session ใหม่ทุกข้อความหรือทุก commit**. เปิด session เมื่อ scope/results เป็นหน่วยงานที่ตรวจสอบได้. Sub-session อยู่บน task branch เดิมและ PR เดิม.

### 4.4 Session Register และ Start/End Update

```markdown
## Session Register
| Session | Purpose | State | Result | Checkpoint SHA | Evidence |
|---|---|---|---|---|---|
| S1 | ... | CLOSED | PASS | `<sha>` | test/report |
| S2 | ... | IN PROGRESS | PENDING | — | — |

### Session S<n> — <purpose>
State: IN PROGRESS
Task ID / Session ID:
Agent / Role:
Started (date):
Intake class (§3.6): A / B / C / D
Applicable plan:
Branch / PR (verified state):
Starting SHA:

#### Plan / Why / Scope
#### Expected changes / Expected evidence
#### Dependencies / Do-not-touch

<!-- On end of session -->
#### Work performed / Implementation details
#### Exact files/systems changed
#### Decisions made (proposed vs Owner-verified)
#### Findings / Defects discovered / Fixes applied
#### Tests & Evidence (commands, counts, exit, logs)
#### Tests not executed (and why)
#### Result (PASS / PARTIAL / BLOCKED)
#### Security / privacy implications
#### Known limitations / Remaining work
#### Current task status / Next recommended action
#### Git checkpoint SHA / Next session / Handoff
#### Execution report and session summary (files, SHA-256, PUBLIC_SAFE or SANITIZED; a private report by SHA-256 only; §4.7)
```

End-of-session note ต้องสอดคล้องกับ evidence จริง; failure ต้องระบุ `introduced / pre-existing / environmental / blocked by dependency / not tested`.

Every meaningful session must fill all of these fields; write `NONE`, `NOT RUN`, or `NOT AVAILABLE` rather than leaving one out. The session record is appended to the task's **existing** canonical note, so the task does not get a new canonical note or a new receipt per session (§4.6 stays one receipt per reviewable task).

### 4.5 ความถี่ของการอัปเดต Obsidian

```text
SESSION START / PLAN APPROVED OR REVISED
  → canonical task note + relevant spec/decision updated

MEANINGFUL CODE/TEST CHECKPOINT
  → session result + evidence/status + impacted design/requirements updated

SCOPE CHANGE / NEW PR / DEPENDENCY CHANGE
  → Backlog + Task/PR index + Decision Log updated

IMPLEMENTATION COMPLETE BUT DOCS STALE
  → NOT CLOSED; reconcile canonical docs before Ready for Review

FINAL ACCEPTANCE
  → latest canonical status + final immutable receipt + PR checklist

POST-MERGE (if required)
  → merged SHA / deployment distinction / next task updated
```

**Where each meaningful session is recorded** (canonical root `Structure DB Obsidian/`):

| Location | Update when |
|---|---|
| `07_Delivery/Tasks/<TASK_ID>_<slug>.md` | Always: the session record (§4.4), appended to the one canonical task note |
| `08_Operations/Agent_Run_Log.md` and/or `Change_Log.md` | Always: one dated entry linking the task note (§7.2) |
| `08_Operations/Reports/<TOPIC_ID>/` | Always: the session's full execution report, public-safe or sanitized (§4.7) |
| `08_Operations/Summaries/<TOPIC_ID>/` | Always: the session's short summary, public-safe or sanitized (§4.7) |
| `08_Operations/Decision_Log.md` | A decision was proposed, changed, or verified as an Owner decision |
| `08_Operations/Handoffs/` | The work is handed to another agent or chat, or a major topic ends (§10) |
| `00_Home/Project_Status.md` | The task's state, PR state, or the project's current truth changed |
| `00_Home/Project_Index.md` | A new canonical note was created and needs navigation |

- **Agent ผู้ทำงานรับผิดชอบให้ Obsidian current แม้จะแบ่ง Gemini เป็น Docs Agent**; ห้ามโยนภาระจนเอกสารล้าหลังหลาย session.
- การเปลี่ยน requirement → `01_Product/Requirements_Register.md`, relevant domain/data/UX, `08_Operations/Decision_Log.md`, `Change_Log.md`, root `README.md` ถ้ากระทบ baseline.
- การเปลี่ยน schema → `03_Data/ERD_Draft.md`, `Data_Dictionary_Draft.md`, `Data_Quality_and_Provenance.md` และ migration-related notes.
- การเปลี่ยน matching → `04_Matching/*`, test cases, evidence model, algorithm version/assumptions.
- การเปลี่ยน cart/ownership → `02_Domain/My_Cart_and_Ownership.md`, `05_UX/Shopping_Tracker.md`, `Collection_Dashboard.md`, Data Dictionary และ R09–R11/R23–R31.
- การเปลี่ยน data source → `03_Data/Source_Registry.md`, `Rights_and_Attribution.md`, `Ingestion_and_ETL.md` พร้อม legal/permission status.

### 4.6 Immutable Receipt (หนึ่งต่อ Task/PR)

ตำแหน่ง: `Structure DB Obsidian/08_Operations/Receipts/YYYY-MM-DD_HHMMSS_<TASK_ID>_<slug>.md`

สร้าง **เมื่อ task ผ่าน acceptance ฝั่ง Agent พร้อมส่ง Human Review**; สำหรับ Planning Task ให้บันทึก `planning_review_ready`, สำหรับ Implementation Task ให้บันทึก test/evidence ของโค้ด. ถ้ายังมี blockers ให้ checkpoint และรายงาน `ACCEPTANCE PENDING` แทน; ห้ามสร้าง final receipt เกินหนึ่งใบหรือแก้ใบเดิมย้อนหลัง. Human Merge event/ผลตรวจหลัง Merge เขียนใน canonical task status หรือ new event log แบบ append-only ไม่แตะ final receipt.

Receipt minimum fields:

```text
TASK_ID / TYPE / PURPOSE
APPROVED_PLAN_PR / APPROVED_PLAN_SHA (if implementation)
BRANCH / BASE_SHA / FINAL_REVIEW_SHA
PR_URL / PR_STATE_AT_RECEIPT
SCOPE / EXACT_CHANGED_FILES
IMPLEMENTATION_OR_PLANNING_DECISIONS
TEST_COMMANDS / RESULTS / EVIDENCE
SECURITY_DATA_RIGHTS / PRODUCTION_SAFETY
NEGATIVE_CONTROLS (if applicable)
KNOWN_LIMITATIONS / DEFERRED_WORK
OBSIDIAN_FILES_UPDATED
REVIEW_READINESS / NEXT_OWNER_ACTION
```

### 4.7 Session records: execution report, session summary and task overview (one set per meaningful session)

Every meaningful writable session (§4.3) leaves three records in the canonical vault `Structure DB Obsidian/`. **Replaced in S5 of DPT-GOV-WORKFLOW-001 (2026-11-22):** the earlier "dual report" rule, which also kept a private copy in the Owner's `Downloads` folder, is withdrawn by Owner decision; no new persistent `Downloads` copy or ad-hoc handoff folder is created.

| Record | Holds | Location |
|---|---|---|
| Full execution report | One session, complete: TOOL DECISION and TOOL EXECUTION REPORT, the work performed, exact paths, the tools actually used, the files changed, the checks run with their results and the checks NOT RUN, hash and evidence identity, task, session, branch, PR and commit, failures, limitations, and the verified current state | `08_Operations/Reports/<TOPIC_ID>/` (public-safe or sanitized) |
| Session summary | The same session in a few lines: what, where, checks, status, Git state, next action | `08_Operations/Summaries/<TOPIC_ID>/` (public-safe or sanitized) |
| Canonical task overview | The living task summary, its session register (§4.4) and an index of its reports and summaries | `07_Delivery/Tasks/` (§4.2, §4.4); one note per task |
| Private full report and private artifacts | Only when content is sensitive (§5.7): the complete report, raw security contracts, raw reviews | A separately Owner-approved private vault, outside every Git repository; never in GitHub; its path is never published |
| Project status | Project-wide current truth | `00_Home/Project_Status.md` |
| Immutable receipt | One per completed reviewable task, at acceptance; never one per session | `08_Operations/Receipts/` (§4.6) |

1. `<TOPIC_ID>` names the major workstream, for example `DPT-GATE-012-U01` or `DPT-GOV-WORKFLOW-001`. Reuse an existing topic folder; do not create a parallel one.
2. File names: `YYYY-MM-DD_<TASK_ID>_S<n>[_r<rev>]_Report.md` and `YYYY-MM-DD_<TASK_ID>_S<n>[_r<rev>]_Summary.md`. Once committed, a report or summary is never overwritten or edited. A correction goes in a later record that names the one it corrects.
3. **Public-safe session:** the vault report is the complete report; no second copy is kept anywhere.
4. **Sensitive session** (secrets, credential or host facts, exploit detail, raw security contracts or reviews): the complete report and the raw artifacts stay only in the approved private vault. The canonical vault receives a separately written report marked **SANITIZED**, which gives the private report's SHA-256 and states `PRIVATE_EVIDENCE_NOT_PUBLISHED`. Never describe the two as identical.
5. **No approved private vault:** report `PRIVATE_RETENTION_NOT_CONFIGURED`, write no sensitive material anywhere (not to the repository, not to `Downloads`), stop that part of the work, and ask the Owner for a decision. Sanitized public records may still be written.
6. **Private-vault custody:** the vault's existence, custody and backup status are recorded in the Owner's private OCD record, not in the repository. Public notes say only that an Owner-approved private vault holds the original, never where. Until the Owner has verified custody and backup, record them as **PENDING**, never as complete.
7. Existing files in `Downloads` (earlier reports and revisions) are historical inputs: read them by exact bytes and hash, never move, edit or delete them, and never use `Downloads` as a new destination.
8. Commit the report, the summary and the task-note update on the task's own branch and PR, in the same checkpoint as the session record. A record cannot contain the SHA of the commit that adds it, so the next session or the PR records that SHA.
9. List every report and summary in the **Reports** index of the canonical task note: file, session, SHA-256, and `PUBLIC_SAFE` or `SANITIZED`. A private report is listed by its SHA-256 only.
10. Claim that a record is published only after checking the remote branch and the PR; until then report `LOCAL_ONLY` / `NOT_PUSHED`.
11. A read-only reviewer (§6.2.1) writes nothing to the repository or the vault; it delivers its own report outside the repository with its SHA-256. An authorized documentation session reconciles it later without modifying it.
12. The rule applies from its adoption onward. Earlier reports, including the `Downloads` private copies of S3–S7, stay as they are; they are not republished, rewritten or deleted.

---

## 5. Git / PR Rules and Safety

### 5.1 Naming

```text
plan/p0-vault-and-governance
plan/catalogue-domain-schema
feat/perfume-catalogue
feat/pyramid-notes
feat/scent-matching
feat/personal-cart
fix/duplicate-perfume-match
data/licensed-seed-import
chore/obsidian-reconciliation
```

Commit conventions: `docs(scope): ...`, `feat(scope): ...`, `fix(scope): ...`, `test(scope): ...`, `data(scope): ...`, `chore(scope): ...`.

### 5.2 Before edit/commit/push

```bash
git fetch origin
git branch --show-current
git status --short
git rev-parse HEAD
git rev-parse origin/main
git diff --check
# Inspect exact intended files and diff before staging.
# Example: git add "Structure DB Obsidian/07_Delivery/Tasks/DPT-TASK-001_example.md"
```

- ต้องตรวจว่า repository exists, `origin` exists, branch และ permissions ถูกต้องก่อนรันคำสั่งใด ๆ.
- ถ้า `origin/main` เดินหน้า ให้ประเมิน conflict; merge หรือ update base ตาม collaboration policy โดยไม่ลบประวัติ/เปลี่ยน shared branch เองอย่างเสี่ยง.
- **Never force push, never blindly reset/clean, never silently rebase shared branch**, never commit credentials/.env/export ส่วนตัว/ข้อมูลที่ไม่มีสิทธิ์, never auto merge.
- Stage exact paths; `git add .` ใช้ได้ก็ต่อเมื่อตรวจทุกไฟล์แล้วและตรง scope ทั้งหมด.
- Push หลัง checkpoint ที่ coherent และมี evidence ไม่ใช่หลังทุกข้อความ.
- Draft PR เป็น living review surface: อัปเดตเมื่อ scope/verification/limitations เปลี่ยนอย่างมีสาระ.

### 5.3 Planning PR Body Template

```markdown
# Planning PR — <title>
## Goal and problem
## Requirements covered (Rxx)
## Proposed / Accepted / Deferred decisions
## Major Topics and Subtasks
## Architecture / Data / UX impact
## Source licensing and privacy impact
## Acceptance criteria for implementation
## Implementation PR breakdown and dependencies
## Open questions / Known risks
## Obsidian files updated
## Verification of docs / links / diffs
## Owner approval checklist
- [ ] Scope agreed
- [ ] Data policy agreed
- [ ] Acceptance agreed
- [ ] Ready to merge planning to main

IMPLEMENTATION_NOT_STARTED=YES
PRODUCTION_MUTATION_PERFORMED=NO
```

### 5.4 Implementation PR Body Template

```markdown
# Implementation PR — <title>
## Approved planning PR / merge SHA
## Requirements addressed
## Changes in source/tests/DB/docs
## User-visible behavior & non-goals
## Tests (exact commands, passed/failed/skipped, exit codes)
## Security / data rights / migration / rollback
## Known limitations / Remaining work
## Obsidian task + session + receipt links
## Branch / base / HEAD SHA
## Reviewer checklist
- [ ] Changes within approved scope
- [ ] Focused and full tests accounted for
- [ ] Docs/evidence reflect actual code
- [ ] No secret/private data/copyright dump
- [ ] Human owner reviewed

PRODUCTION_MUTATION_PERFORMED=NO (unless explicitly authorized)
```

### 5.5 Dependency and PR Workstream Index

ใน `Structure DB Obsidian/07_Delivery/Backlog.md` หรือ task status ที่เกี่ยวข้อง:

```markdown
| Task | Type | PR | Branch | Base / Plan dependency | State | HEAD | Next action |
|---|---|---|---|---|---|---|---|
| DPT-PLAN-001 | PLAN | #... | plan/... | main | DRAFT | ... | owner review |
| DPT-IMP-001 | IMPLEMENT | #... | feat/... | approved #... / SHA | IN PROGRESS | ... | test |
```

### 5.6 Checkpoint publication and blocked remote writes

The vault is part of this repository, so a meaningful documentation checkpoint belongs on the task's own branch and PR. When a checkpoint is ready:

1. Verify the branch and worktree.
2. Inspect the exact changed files.
3. Validate documentation consistency (§6.1 docs checks).
4. Run `git diff --check`.
5. Check for secrets and private information (§5.7).
6. Stage only the intended paths.
7. Commit one coherent checkpoint.
8. Push with an authorized credential (below).
9. Create or update the task's Draft PR (§3.6 decides which PR).
10. Record the actual commit SHA and the verified PR state.

**Responsibilities:** the agent carries out steps 1–10, including the branch, commit, push, Draft PR and report, so the Owner does not create branches, commit, push or open Draft PRs in the normal workflow. The Owner reviews, requests corrections, makes the decisions that need Owner authority, and merges. The agent never merges, approves its own work, or enables auto-merge.

**Credential boundary:** push and create or update PRs only with a credential the Owner has authorized for agent use and that is appropriately scoped. Having a credential in the environment, including the Owner's own broad-scope login, is not authorization. Permission to publish a branch or open a Draft PR is never permission to approve a gate, sign an Owner statement, merge, or bypass repository protection.

**Agent publishing identity** (the prerequisite for agent-managed PRs):

- **Identity:** a dedicated identity distinct from the Owner. Preferred: a GitHub App installed only on this repository. Alternative: a dedicated machine-user account that is a collaborator only on this repository, with the Write role and a token limited to this repository.
- **Permissions:** Contents read and write, Pull requests read and write, Metadata read. No Administration, Actions, Workflows, Secrets, Environments, Pages or account-level permission.
- **Secret handling:** the token or key has an expiry and is stored outside the repository. It is never printed or committed. The agent session is configured to use it instead of the Owner's login. On the same operating-system account the Owner's stored login stays technically reachable; the rule above still forbids using it, and full separation needs a separate OS account or machine.
- **Repository rules on `main`:** a pull request is required; force pushes and deletion are blocked; updating `main`, including merging, is restricted to the Owner; the agent identity is never a bypass actor; auto-merge stays disabled.
- **Verification:** push a test branch and open and close a Draft PR with the agent identity. Confirm from the ruleset settings that the agent identity cannot update `main`; do not test this by attempting a merge. Record the identity, permissions, expiry and result in `08_Operations/Agent_Tool_Registry.md`, without the token.

**If remote publication is blocked:** keep the local commit, record the exact blocker in the task note, and report `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`. Also report `AGENT_CREDENTIAL_REQUIRED` when the blocker is the missing agent publishing identity. The Owner may publish that checkpoint or explicitly authorize a one-time use, but that is an exception, not the standard workflow. Never present a local commit as a PR.

### 5.7 Public repository evidence handling

Check the repository's visibility before committing evidence. While the repository is public:

- Never commit secrets, private keys, tokens, credentials, sensitive system paths, or exploit details that should remain confidential.
- For sensitive reports, commit only a sanitized summary with the original's hash and provenance, and record whether the original is retained privately. Keep raw sensitive evidence outside the repository, in the Owner-approved private vault (§4.7); without one, report `PRIVATE_RETENTION_NOT_CONFIGURED`.
- Never publish the private vault's path, custody details or backup details; they belong in the Owner's private OCD record.
- Matching hashes show that two copies are identical. They do not prove independent custody.
- Do not silently delete or rewrite existing records.

---

## 6. Testing, Independent Review & Production Gates

### 6.1 TDD and evidence

สำหรับ feature behavior/bugfix ที่ทดสอบได้ ให้ใช้ `RED → minimal implementation → GREEN → focused test → related/full regression`. หากโครงการยังไม่มี tests ให้สร้าง test harness ใน approved scope; **ห้ามแต่ง RED/Green evidence ย้อนหลัง**. สำหรับ docs-only Planning PR ให้ใช้ doc validators/link/schema checks แทน ไม่อ้างว่าได้ทดสอบ runtime.

รายงานอย่างน้อย:

```text
TEST_SCOPE=<unit/integration/e2e/docs/data>
COMMAND=<exact command>
PASSED=<n / N/A>
FAILED=<n / N/A>
SKIPPED=<n / N/A>
EXIT_CODE=<integer / not-run>
ENVIRONMENT=<local/CI/container/version>
EVIDENCE_PATH_OR_RUN_URL=<where verified>
LIMITATIONS=<what was not proven>
```

### 6.2 Independent review

Review exact Git SHA ไม่ใช่เชื่อ agent summary. ตรวจ **source semantics**, changed paths, test behavior, bypass/fail-open paths, permissions/authentication, data provenance, migrations/rollback และ Obsidian claims. Findings: `BLOCKER / HIGH / MEDIUM / LOW / NO ISSUE`; หากมี blocker ให้แก้แบบ targeted ใน PR เดิมและ retest.

#### 6.2.1 Read-only independent reviews (exception to session recording)

Independent reviews, security reviews in particular, keep the reviewer's independence and any declared read-only restriction. If the reviewer is explicitly forbidden to modify the project:

- The reviewer does not modify the repository or the Obsidian vault.
- The reviewer produces the authorized report separately, with the report's hash, the reviewed revision, the findings, the verification status, and the provenance limitations, and marks Obsidian synchronization as **pending**.
- A separately authorized documentation session later reconciles the report into the canonical task note (public-repository rules, §5.7, apply). That session never modifies or overwrites the review report.

The reconciled record keeps these states separate: *review completed*, *findings open*, *findings resolved in proposed design*, *independent closure pending*, *runtime tests not run*, and *gate approved by Owner*. A review report is never automatic security approval. Only a verified Owner decision approves a gate.

### 6.3 Data Source / Scraping gates เฉพาะ DoomParfum

ก่อนออกแบบหรือรัน ETL/Scraper จากเว็บไซต์ภายนอก:

1. ทำ `Source Registry` เก็บ owner, URL, license/ToS, robots (ตามที่เกี่ยวข้อง), API terms, automation permission, caching/storage/redistribution/AI-use limitations และวันที่ตรวจ.
2. ถ้า permission ไม่ชัดหรือห้าม automated access: **NO-GO** สำหรับ crawling; ใช้ licensed dataset, documented API, brand feed ที่อนุญาต, หรือข้อมูลที่ผู้ใช้ป้อนและมีสิทธิ์ใช้งาน.
3. ไม่ใช้บริการ/Agent เพื่อหลบ CAPTCHA, bot protection, login/session restrictions หรือข้อห้ามของแพลตฟอร์ม.
4. เก็บ field-level source/provenance; ตรวจ brand/name/variant, note aliases, copyright/image permissions, duplicate/contradictory evidence. AI ห้ามเติม fact ที่ไม่มีหลักฐาน.
5. แยก perfume profile/notes, review rating, pairwise similarity, Shopee retail listing, app cart, ordered/purchase records และ owned inventory ออกจากกัน.
6. Dry-run with sample data ก่อน bulk import; มี validation report, rollback/backups สำหรับ migrations และทดสอบ unknown/missing/conflicting cases.
7. ห้าม commit screenshot ของบัญชีร้านค้า, personal order history, Shopee cookies, tokens, private exports หรือ raw third-party copyrighted dumps ใน GitHub โดยไม่ผ่านการตรวจสิทธิ์/ข้อมูลส่วนตัว.

### 6.4 Production / destructive operation safety

ค่าเริ่มต้นของทุก Task: `PRODUCTION_MUTATION_ALLOWED=NO`.

หากต้อง Deploy/เปลี่ยน DB จริง/แก้ firewall/Cloudflare/secret/storage:

```text
READ-ONLY PREFLIGHT → BASELINE EVIDENCE
→ EXACT CHANGE PLAN + IMPACT + ABORT CONDITIONS
→ BACKUP/ROLLBACK PLAN
→ HUMAN OWNER EXPLICIT APPROVAL
→ CONTROLLED EXECUTION
→ ACCEPTANCE & NEGATIVE CONTROLS
→ CLEANUP / ROLLBACK PROOF
→ OBSIDIAN + GIT LOGGING
```

ก่อน Human Approval ห้ามดำเนินการจริง. Log เฉพาะชื่อ environment variable ไม่แสดง secret. แยก `SOURCE IMPLEMENTED`, `LOCAL VERIFIED`, `STAGING VERIFIED`, `PRODUCTION DEPLOYED`, `EXTERNAL ACCEPTED`.

---

## 7. Documentation Templates and Change Logs

### 7.1 Architecture Decision Record (ADR)

```markdown
---
id: DPT-ADR-XXX
project: DoomParfum By TK
type: decision
status: proposed
updated: YYYY-MM-DD
---
# ADR-XXX — <decision title>
## Context / Problem
## Decision (proposed / accepted)
## Alternatives considered
## Affected requirements / entities / screens
## Data rights / Security / Privacy impact
## Trade-offs / Consequences
## Review evidence / Planning PR
## Owner acceptance / Date
## Links / Follow-ups
```

### 7.2 Change Log / Agent Run Log (mandatory)

ทุก meaningful session ต้องมี entry ลง `08_Operations/Change_Log.md` หรือ `Agent_Run_Log.md` พร้อม links กลับไปยัง task/session details; ไม่จำเป็นต้องทำบทความใหม่ทุก commit.

```markdown
| Date | Task/Session | Agent | Planning PR | Implementation PR | Changed files | Tests / Evidence | Result | Commit SHA |
|---|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | DPT-IMP-.../S1 | Codex | #... | #... | web/... + vault/... | command/run | PASS/PARTIAL | `<sha>` |
```

### 7.3 Status dashboard

```markdown
| Area | State | Evidence / Next action |
|---|---|---|
| Planning PR | MERGED / PENDING | URL + approved SHA |
| Requirements | ACCEPTED / PROPOSED | docs/ADR |
| Source | NOT STARTED / SOURCE IMPLEMENTED | files + SHA |
| Focused tests | PASS / FAIL / NOT RUN | exact command |
| Full regression | PASS / FAIL / NOT RUN | exact command |
| Obsidian reconciliation | CURRENT / STALE | changed docs |
| Implementation PR | DRAFT / READY / MERGED | PR URL |
| Production | NOT DEPLOYED / DEPLOYED | measured evidence |
```

---

## 8. Operational Patterns for Multiple Agents

### 8.1 Pattern A — Single Coding Agent for small changes

```text
Read governance + accepted plan
→ Task branch + task note IN PROGRESS
→ TDD / implement / test
→ Update Obsidian task, affected docs, run log
→ Validate + checkpoint commits
→ Draft Implementation PR → independent review
→ final receipt → Ready for Human Review
```

### 8.2 Pattern B — Coding Agent + Documentation Agent

```text
ChatGPT / Owner: approve planning PR
→ Codex/Claude: implement + tests + source checkpoint
→ ChatGPT: independent review by exact SHA
→ targeted correction if needed
→ Gemini: DOCS-ONLY reconcile Obsidian/PR based on verified SHA
→ docs checkpoint on same Implementation branch
→ reviewer checks doc/source coherence
→ receipt / Ready for Review → Owner merges
```

Coding Agent ยังคงรับผิดชอบให้ docs updated; Documentation Agent เป็นผู้ช่วย ไม่ใช่เหตุผลให้ commit code โดยปล่อย Obsidian stale. ถ้า Docs Agent ทำงานหลัง Coding Agent จะต้อง sync/checkpoint ก่อนการประกาศ session/task complete.

### 8.3 Large initiative / split decision

ถ้า feature ใหญ่ เช่น Catalogue → Matching → Shopping Tracker มี dependency กัน ให้แบ่ง Implementation PR ตาม reviewable behavior. ถ้าพบ scope ที่อยู่นอกแผน ให้หยุดส่วน scope ใหม่และเปิด Planning Amendment PR; อัปเดต `Backlog`, `Decision_Log`, affected task notes และ `PR Workstream Index`.

---

## 9. Copy/Paste Agent Prompts (พร้อมใช้)

> Prompt ด้านล่างเป็น **แม่แบบ**; ค่า `<...>` ต้องแทนด้วยค่าจริงจาก repo/status หรือ `UNKNOWN` หากยังไม่ทราบ. Agent ไม่ควรเดา branch/SHA/PR/permission.

### 9.1 Planning Agent — ออกแบบและสร้าง Planning PR

```text
You are the DoomParfum Planning / Architecture Agent.

READ FIRST:
1. AGENTS.md if it exists.
2. DEVELOPMENT_WORKFLOW.md (entire file).
3. README.md (R01–R31 and decisions).
4. Structure DB Obsidian/README.md, 00_Home/Project_Status.md,
   relevant requirements, ADRs, task notes, most recent receipts.
5. Current Git branch/HEAD/origin/main, existing PRs and repository permissions.

GOAL: <planning objective>
MODE: PLANNING_PR_ONLY
PRODUCTION_MUTATION_ALLOWED=NO
RUNTIME_SOURCE_EDIT_ALLOWED=NO
MERGE_ALLOWED=NO

- Produce Major Topics -> numbered subtasks, scope/out-of-scope,
  requirement IDs, dependencies, security/data-source rights,
  architecture/ERD/UX decisions, acceptance criteria and review checklist.
- Create or update canonical docs in Structure DB Obsidian/.
- Update root README.md only where project-level baseline genuinely changes;
  preserve CONFIRMED/PROPOSED/RESEARCH/DEFERRED distinctions.
- Record open questions instead of inventing decisions.
- Update Change_Log, Decision_Log, Agent_Run_Log and task/status notes.
- Validate Markdown/links/frontmatter/diffs; never include secrets.
- If Git access is granted, create plan/<slug> branch from main,
  commit docs-only, push and open Draft Planning PR. Do not merge.
- If not authorized or Git unavailable, output exact files and a
  PR-ready plan; state PR_NOT_CREATED clearly.

REPORT: TASK, BRANCH, HEAD_SHA, PLANNING_PR_URL, DOCS_CHANGED,
REQUIREMENTS_COVERED, DECISIONS_OPEN, VERIFICATION, BLOCKERS,
OWNER_REVIEW_NEEDED, NEXT_ACTION.
STOP: Do not implement web/database code until Owner merges Planning PR.
```

### 9.2 Implementation Agent — เริ่มหลัง Planning PR Merge

```text
You are the DoomParfum Implementation Agent (Codex or Claude Code).

MANDATORY CHECKS:
- Read AGENTS.md, DEVELOPMENT_WORKFLOW.md, README.md,
  Obsidian task/status and accepted spec.
- Verify Planning PR <id> is MERGED into main and record approved SHA.
- Fetch/inspect branch, HEAD, origin/main, working tree and active PRs.
- If approved plan or permissions cannot be verified: STOP and report BLOCKED.

TASK: <implementation task ID and title>
APPROVED_PLAN_PR: <# / URL>
APPROVED_PLAN_SHA: <sha>
REQUIREMENTS: <Rxx>
IN_SCOPE: <paths/features>
OUT_OF_SCOPE: <excluded features>
PRODUCTION_MUTATION_ALLOWED=NO
MERGE_ALLOWED=NO

FIRST: output hierarchical Task Map, exact files expected, acceptance,
security/data-source rights and focused/full tests.

THEN:
1. Create/reuse one task branch & Draft Implementation PR for this task.
2. Record session IN PROGRESS in canonical Obsidian task note.
3. Use TDD where meaningful (RED -> GREEN); never fabricate evidence.
4. Implement only approved scope; keep separate data/ownership concepts.
5. Run focused tests, full regression, lint/type/build and relevant checks.
6. Update Obsidian impacted spec, session register, Change_Log,
   Agent_Run_Log, status dashboard and handoff from actual evidence.
7. Validate diff/secrets/data rights, commit coherent checkpoints,
   push same branch and update Draft PR.
8. Prepare independent review at exact HEAD; fix verified defects.
9. After acceptance, create exactly one final immutable receipt,
   mark PR Ready for Review and leave final merge to Owner.

FINAL REPORT: TASK, PLAN_PR, BRANCH, START_SHA, END_SHA,
IMPLEMENTATION_PR, EXACT_CHANGED_FILES, TEST_COMMANDS/COUNTS,
NEW/PREEXISTING_FAILURES, OBSIDIAN_FILES, RECEIPT,
PRODUCTION_MUTATION=NO, KNOWN_LIMITATIONS, NEXT_ACTION.
NEVER merge, force push, publish private data, scrape unpermitted sources.
```

### 9.3 Documentation Agent — reconcile Obsidian/PR หลัง Code

```text
You are the DoomParfum Documentation Reconciliation Agent.
MODE=DOCS_ONLY

READ: DEVELOPMENT_WORKFLOW.md, accepted plan PR, current code HEAD,
verified test reports, canonical Obsidian task/status and latest checkpoint.

DO NOT modify web application runtime code, tests, database migration,
production configuration or secrets.

- Confirm exact branch/HEAD and evidence rather than trust summaries.
- Update affected Obsidian requirements/domain/data/matching/UX/engineering docs.
- Update Task Register, Session Register, Change_Log, Agent_Run_Log,
  status dashboard, PR body, remaining work and next action.
- Record failures/limitations honestly; do not claim deployment.
- Never alter old immutable receipts or invent test results.
- Run vault/link/diff checks; commit & push docs-only checkpoint on the
  SAME implementation branch when Git write is authorized.
- If write unavailable, provide exact patch and report NOT_COMMITTED.

REPORT: DOCS_CHANGED, START_SHA, END_SHA, EVIDENCE_USED,
VAULT_VALIDATION, PR_UPDATED, RUNTIME_SOURCE_CHANGED=NO,
GIT_CHECKPOINT, BLOCKERS, NEXT_ACTION.
Do not merge.
```

### 9.4 Independent Review Agent — ตรวจ Implementation PR

```text
You are the independent DoomParfum PR Reviewer.
Read DEVELOPMENT_WORKFLOW.md and the accepted Planning PR.
Verify exact Implementation PR head SHA, changed files, source semantics,
tests, authorization/privacy, import/source rights, migrations/rollback,
Obsidian/README consistency and status claims.

Classify issues as BLOCKER/HIGH/MEDIUM/LOW/NO ISSUE with evidence.
If blocker: produce a narrow correction prompt for the SAME PR; do not
approve deployment/merge. If acceptable: clearly state verified scope,
limitations, doc reconciliation status and owner review gate.
Never infer test PASS from a coding-agent message alone.
```

### 9.5 Obsidian Bootstrap Agent — สร้าง vault สำหรับโปรเจกต์ที่ยังใหม่

```text
You are the DoomParfum Obsidian Bootstrap Agent.
Read README.md, DEVELOPMENT_WORKFLOW.md and
Structure DB Obsidian/README.md completely.

TASK: create the Obsidian documentation skeleton according to the
existing 00_Home ... 90_Templates layout, plus:
- 07_Delivery/Tasks/
- 07_Delivery/Planning_PRs/
- 08_Operations/Receipts/
- 08_Operations/Handoffs/
- 06_Engineering/GitHub_and_Workflow_PENDING.md: update status text to
  reference proposed DEVELOPMENT_WORKFLOW.md; only mark accepted when
  Owner has reviewed/merged the Planning PR that adopts it.

Populate relevant docs with existing R01–R31 without manufacturing
facts or converting PROPOSED to accepted. Link to DEVELOPMENT_WORKFLOW.md.
Create Project_Index and initial status, task/PR templates, Decision_Log,
Change_Log, Agent_Run_Log. Do NOT implement code.
If repo is available and authorized: use a dedicated docs-only Planning PR.
Otherwise: create local Markdown only and report Git actions NOT DONE.
```

### 9.6 ChatGPT Master Prompt — ใช้เริ่มแชตใหม่/ส่งต่อ

```text
This is an existing DoomParfum By TK workstream.
First read the DoomParfum Chat Continuity Pack, if provided, then
AGENTS.md, DEVELOPMENT_WORKFLOW.md, root README.md, accepted Obsidian
status, active PRs and exact source/evidence.
Verify current Git branch/HEAD/origin/main/PR before prescribing edits.

Always separate a docs-only PLANNING PR from implementation.
Do not assign coding until Owner has merged the accepted Planning PR.
After implementation, update canonical Obsidian with exact evidence,
create implementation PR and leave Merge to Human Owner.

Output: CURRENT TRUTH, TASK MAP, APPROVED PLAN STATUS,
ACTIVE PR/BRANCH/SHA, DONE, IN PROGRESS, REMAINING,
RISKS/RIGHTS, NEXT AGENT PROMPT, NEXT ACTION.
Do not invent data, Git states, test outcomes or external permissions.
```

---

## 10. Chat Continuity and Handoff

**เมื่อเปลี่ยน Agent/แชต หรือจบ Major Topic ให้สร้าง Chat Continuity Pack** ถ้าต้องการให้ผู้รับช่วงทำงานต่อโดยไม่ย้อนอ่านแชต. จัดเก็บที่ `Structure DB Obsidian/08_Operations/Handoffs/<timestamp>_<task-id>.md` หรือเตรียม text pack เมื่อยังไม่พร้อม commit.

Template:

```markdown
# DOOMPARFUM CHAT CONTINUITY PACK
## A. Identity: project, task, owner, date
## B. Product / Requirements: Rxx and accepted ADRs
## C. Git Truth: repo URL, main/base SHA, branch, HEAD, PR URLs/states
## D. Planning Gate: approved Planning PR, merge SHA, decisions pending
## E. Implementation Gate: implementation PR, branch, current acceptance
## F. Task Map: major topics/subtasks, completed/current/remaining
## G. Work Completed: exact files and checkpoints
## H. Verified Tests/Evidence: commands, results, environment, links
## I. Known Issues: blockers, pre-existing failures, deferred items
## J. Obsidian Truth: task note, latest session, decision log, receipt
## K. Data Rights / Privacy / Security and Production state
## L. Important design decisions and assumptions
## M. Exact next action / recommended agent / abort conditions
## N. Do not do (no merge, no unauthorized scraping, no production mutation)
## O. Continuity keywords: PRs, SHAs, task IDs, files, errors
## P. Paste-ready bootstrap prompt for next Agent/Chat
```

Quality gate: คนรับช่วงต้องตอบได้ว่า **แผนล่าสุด Merge แล้วหรือยัง, code อยู่ PR ไหน, ทำอะไรจริงแล้ว, มีหลักฐานอะไร, Obsidian อัปเดตถึง SHA ไหน, เหลืออะไร และใครต้องทำต่อ**. อย่าพึ่ง Chat History อย่างเดียว.

### 10.1 Chat-only evidence

ถ้ามี screenshots, manual test results, ChatGPT decisions หรือ error ที่ยังอยู่เฉพาะในแชต ให้ย้ายเฉพาะสาระสำคัญที่ไม่มีความลับไปยัง task note/continuity pack พร้อม timestamp/source. ห้ามส่ง cookies/tokens/account data เพื่อทำ handoff.

---

## 11. Closeout Checklist and Final Report

### 11.1 Planning PR checklist

- [ ] Read current repository and Obsidian truth
- [ ] Defined Task Map, requirements, scope, dependencies and acceptance
- [ ] Identified `PROPOSED` vs accepted decisions
- [ ] Updated canonical docs/ADR/requirements/roadmap/Obsidian log
- [ ] Checked data-source rights and privacy implications
- [ ] Validated Markdown/links/frontmatter and `git diff --check`
- [ ] Created docs-only Planning PR if authorized; otherwise reported why not
- [ ] Created exactly one final receipt when ready for owner review
- [ ] Human Owner reviewed and merged before any implementation starts
- [ ] Captured approved Planning PR and SHA for subsequent coding tasks

### 11.2 Implementation PR checklist

- [ ] Verified planning PR merged and selected branch from current main
- [ ] Created task branch and Obsidian session IN PROGRESS
- [ ] Wrote tests / collected RED-GREEN evidence where applicable
- [ ] Ran focused tests and full regression or explicitly reported NOT RUN
- [ ] Ran build/lint/type-check where applicable
- [ ] Checked security, privacy, data rights, and no forbidden scraping
- [ ] Updated Obsidian spec + task register + session evidence + logs
- [ ] Validated Git diff, secret exposure, unrelated changes
- [ ] Pushed coherent checkpoints and kept PR Draft until ready
- [ ] Completed independent review and resolved blockers
- [ ] Created exactly one final immutable receipt at readiness
- [ ] Requested Human Owner review and merge; never auto-merged
- [ ] Recorded post-merge status when applicable

### 11.3 Mandatory Final Report (ทุก meaningful session)

```text
PROJECT=DoomParfum By TK
TASK_ID=
TASK_TYPE=PLANNING / IMPLEMENTATION / DOCS / DATA / REVIEW
SESSION_ID=
AGENT=
APPROVED_PLAN_PR=
APPROVED_PLAN_SHA=
BRANCH=
START_SHA=
END_SHA=
PR_URL=
PR_STATE=

MAJOR_TOPICS_DONE=
MAJOR_TOPICS_OPEN=
WORK_COMPLETED=
EXACT_FILES_CHANGED=
TEST_COMMANDS_AND_RESULTS=
NEGATIVE_CONTROLS=
DATA_RIGHTS_VERIFICATION=
PRODUCTION_MUTATION_PERFORMED=YES/NO
OBSIDIAN_UPDATED=YES/NO
OBSIDIAN_FILES=
GIT_CHECKPOINT_SHA=
FINAL_RECEIPT=CREATED/NOT_YET_APPLICABLE
KNOWN_LIMITATIONS=
BLOCKERS=
NEXT_RECOMMENDED_AGENT=
NEXT_EXACT_ACTION=
OWNER_ACTION_REQUIRED=
```

Use `NOT APPLICABLE`, `UNKNOWN`, `NOT RUN`, `NOT COMMITTED` หรือ `NOT CREATED` ตามความจริงเมื่อไม่มีหลักฐาน. ห้ามกรอก SHA/PR หรือผลทดสอบที่ไม่ได้ตรวจ.

---

## 12. Adoption Plan — เริ่มใช้ไฟล์นี้กับโปรเจกต์อย่างไร

### 12.1 Bootstrap adoption template (historical sequence; PR #1 was owner-merged)

1. วางไฟล์นี้เป็น `DoomParfum By TK/DEVELOPMENT_WORKFLOW.md` ที่ root โปรเจกต์.
2. ให้ Agent อ่าน `README.md`, `Structure DB Obsidian/README.md` และไฟล์นี้เพื่อสร้าง **Planning PR #แรก** สำหรับตั้งค่า Vault/Governance; ถ้ายังไม่มี repo ให้เตรียม local changes และ PR-ready checklist ก่อน.
3. ภายใน Planning PR ให้เพิ่ม `AGENTS.md` เป็น entry point ที่ชี้มาที่ไฟล์นี้, เพิ่ม links ใน `Structure DB Obsidian/00_Home/Project_Index.md`, ปรับ `06_Engineering/GitHub_and_Workflow_PENDING.md` ให้บอกว่ามี Workflow proposed แล้ว, เพิ่ม Task/PR/Receipt/Handoff templates และเสนอ branch protection/CI ในฐานะ **PROPOSED**.
4. เจ้าของโปรเจกต์ตรวจ README/Schema/Agent authority/PR rules และ Merge Planning PR นี้เอง.
5. เมื่อมี approved plan ที่ระบุฟีเจอร์และ acceptance ครบ จึงเริ่ม Coding Agent จาก main และเปิด Implementation PR.

> **ข้อสำคัญ:** ขั้นตอน Adoption ไม่อนุญาตให้ Agent ตั้งค่า GitHub repository, enable Actions, push, merge หรือแตะ Production โดยไม่มีสิทธิ์ที่ได้รับจากเจ้าของโปรเจกต์จริง.

### 12.2 Snippet สำหรับ `AGENTS.md` (เพิ่มผ่าน approved planning PR)

```markdown
# DoomParfum Agent Entry Point

Before making any plan, source change, database migration, documentation
change, Git commit, push, or Pull Request, read in order:
1. `DEVELOPMENT_WORKFLOW.md`
2. `README.md`
3. `Structure DB Obsidian/README.md`
4. `Structure DB Obsidian/00_Home/Project_Status.md`
5. The current accepted planning docs, active task and latest receipt
6. The actual code/test/PR and current Git state

Mandatory: Planning PR -> Human Merge -> Implementation PR -> Human Merge.
Every meaningful change updates `Structure DB Obsidian/` and task evidence.
Never auto-merge, force push, mutate Production, commit secrets or scrape
unauthorized data sources.
```

### 12.3 Difference from source AEGIS workflows

- **Kept:** one task/branch/PR, coherent checkpoints, immutable receipt, Human Merge, independent code review, TDD, production safety, Truthful Evidence, Chat Continuity, multi-agent roles, Git/Obsidian consistency.
- **Added explicitly for DoomParfum:** mandatory **Planning PR first**; Human Merge is a hard gate before code; multiple Implementation PRs may descend from one merged Plan; permissions-bound Agent autonomy to create PRs; Obsidian update on every meaningful session; perfume data provenance/copyright/scraping gates; domain semantics for App Cart vs Purchase/Owned.
- **Not copied as-is:** AEGIS-specific network topology (MikroTik/firewall gateway), AEGIS repository paths and IDEA naming; instead use DoomParfum paths, domain risks and task IDs.
- **Current repository facts (2026-11-10):** Public GitHub repository exists and this workflow is present. Agent authorization is bounded by the current owner request. CI, deployment, hosting, source adoption and proposed governance acceptance remain owner decisions; workflow existence does not grant account, cloud, source or merge permissions.

---

## 13. Golden Rule

> **แผนต้องตรวจรับก่อนเขียนโค้ด; โค้ดต้องพิสูจน์ก่อนอ้างว่าเสร็จ; Obsidian ต้องตรงกับ Git และหลักฐาน; ทุก PR ให้ Human Owner เป็นคน Merge.**
>
> ถ้า Agent คนถัดไปไม่สามารถตอบได้จาก `Git + PR + Obsidian + receipts + evidence` ว่ากำลังทำอะไร ทำเสร็จจริงแล้วแค่ไหน และควรทำอะไรต่อ — งานนั้นยังไม่ถือว่ามี handoff ที่สมบูรณ์.
