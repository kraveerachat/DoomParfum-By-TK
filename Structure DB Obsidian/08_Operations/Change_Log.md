---
id: DPT-OPS-002
project: DoomParfum By TK
type: change_log
status: draft
owner: project
updated: 2026-11-12
tags:
  - doomparfum
  - operations
  - changelog
  - history
source_of_truth: "../../README.md"
---

# Change Log — DoomParfum By TK

## 2026-11-12 — DPT-PLAN-003 S2 source-checkpoint review closeout

Authored2026-11-11; continued after quota2026-11-12. Parent /root independently reviewed the author's
matching reconciliation, found no blocking semantic issue, and accepted explicit IMP-MATCH-04 real
presence-label/closure/Gate-P prerequisites. DM-01..07 remain PROPOSED. Final local docs/arithmetic/
merge-file/preservation checks precede exact18-Markdown-path staging/commit; parent must verify the
resulting checkpoint before push/update of existing Draft PR #4. No second receipt, matching code,
source/DB/production change, merge/rebase or shared handoff/ZIP mutation. Current SHA/publication
are recorded only after verified events; older IN PROGRESS snapshots below remain historical.

## 2026-11-11 — DPT-PLAN-003 S2 post-PR5 correction in progress

Reconcile existing Draft PR #4 with merged acquisition PR #3 and local-intake PR #5 at55d39cd.
New [[P2_Post_PR5_Matching_Reconciliation]] centralizes actual private catalogue/44holds/matching0,
absent accord/family/status/completeness capabilities, DM recommendations and existing task gates.
Dedicated plan/data/architecture/UX/acceptance/ADR/handoff/task and current status are corrected;
old snapshots remain historical. No weight/DM approval, runtime, merge/rebase, receipt replacement
or second receipt. Checks/independent review and same-PR publication are next, not inferred.


## 2026-11-11 — DPT-PLAN-003 / S1 docs-only dual-mode proposal

Fresh base9636ee740cdcd3d60633ac11745366814d1af05c after verified owner PR #2 merge; new branch
plan/p2-dual-mode-matching, separate from Draft PR #3 inspected69255b0. [[DPT-PLAN-003_Dual_Mode_Matching]]
records checkpoints; [[P2_Dual_Mode_Scent_Matching_Plan]] links dedicated architecture/data/UX/tests/ADR.
Only additive documentation navigation/status reconciliation in shared files, original bodies retained.
[[DPT-PLAN-003_Documentation_Evidence]] records exact manifest/checks/overlap. No code/migration/DB,
source acquisition, AI service, production or original decision/receipt edits. Publication not yet
performed at this start entry; actual event follows in task/evidence. Human Owner alone reviews/merges.

> **Document Type:** Project Evolution & Specification Change History
> **Source Baseline:** `../README.md`
> **Status:** Active Change Log

---

Publication event: [PR #4](https://github.com/kraveerachat/DoomParfum-By-TK/pull/4) verified OPEN/DRAFT/unmerged/mergeable at03df0dd;
latest PR #3 inspected0cdfba4504594a888eb2f11947ea2d1dd58b6db8, main9636ee7 unchanged. One immutable
planning receipt [[2026-11-11_160700_DPT-PLAN-003_Dual_Mode_Matching]] created after agent review readiness; no historical receipt edit.
Final metadata HEAD is verified in live PR/final report. Source checkpoint03df0dda8a976945393beeb512768fb841bdc232;
DM decisions remain PROPOSED. No runtime/DB/source acquisition or production changes; Owner Gate P pending.

## 1. Version History

### [Version 0.2.0-planning] — 2026-11-10
**ผู้บันทึก:** TK & Agent Architecture Team
**ประเภทการเปลี่ยนแปลง:** Major Requirement & Architecture Expansion

#### รายการเปลี่ยนแปลงสำคัญ:
1. **เพิ่มข้อกำหนดกลุ่ม Shopping & Ownership (R23 ถึง R31):**
   - **R23:** ยืนยันการเพิ่มน้ำหอมทุกแบรนด์เข้าสู่ `My Cart` ภายในแอป
   - **R24:** อนุญาตให้บันทึกลิงก์ร้านค้าภายนอก (Shopee) หลายร้านต่อหนึ่งน้ำหอม พร้อมโน้ตความน่าเชื่อถือ
   - **R25:** กำหนดกระบวนการเปลี่ยนสถานะเป็น "สั่งซื้อแล้ว (Ordered)" ด้วยมือของผู้ใช้เอง (Manual Transition)
   - **R26:** รับรองการเก็บบันทึกประวัติการซื้อถาวร แม้น้ำหอมขวดนั้นจะถูกใช้หมด ขายต่อ หรือยกให้ผู้อื่น
   - **R27:** กำหนดสเปกหน้าจอ Collection Dashboard แสดงข้อมูล Ever Purchased vs Currently Owned
   - **R28:** แยกโครงสร้างตาราง `purchase_records` ออกจาก `inventory_items` เพื่อรองรับการซื้อซ้ำหลายครั้ง
   - **R29:** กำหนดฟิลด์ข้อมูลการซื้อจริง (ราคา, ขนาด, ร้าน, วันที่) เป็นฟิลด์เสริมที่ไม่บังคับ (Optional)
   - **R30:** เพิ่มระบบแจ้งเตือนเมื่อผู้ใช้พยายามบันทึกน้ำหอมเดียวกันซ้ำใน Cart และแนะนำให้เพิ่มลิงก์ร้านค้าแทน
   - **R31:** วางโครงสร้างสถิติการใช้จ่ายเฉลี่ยต่อ mL เป็นฟีเจอร์ระยะยาว (Deferred)
2. **ขยาย Thai Brand Registry (R22):**
   - บรรจุ 4 แบรนด์ไทยหลักอย่างเป็นทางการ: **La Palette (lapalette), SCENTERY, BE CHERIE PARFUM, SÚNDALO**
   - บันทึกตัวอย่างรุ่นโฟกัสจากผู้ใช้: `BE CHERIE White Instinct`, `SÚNDALO Rhapsody Sky`
3. **จัดตั้งโครงสร้าง Obsidian Vault (Structure DB Obsidian):**
   - แยก 11 โฟลเดอร์ (00_Home ถึง 90_Templates) พร้อมเชื่อมโยง MOC และ Internal Links ครบถ้วน
   - จัดทำสัญญาการทำงาน (Operating Contract) และข้อห้ามเรื่อง Mass Scraping / Auto-Deploy

---

### [Version 0.1.0-discovery] — 2026-11-09
**ผู้บันทึก:** TK
**ประเภทการเปลี่ยนแปลง:** Initial Discovery & Baseline Blueprint

#### รายการเปลี่ยนแปลง:
- กำหนด Product Vision เบื้องต้น: เว็บแอปส่วนตัวสำหรับการศึกษาวิจัยและเปรียบเทียบน้ำหอม
- ร่างข้อกำหนดเริ่มต้น R01 ถึง R22 (Catalogue, Search, Pyramid Notes, Scent Matching)
- กำหนดหลักการ Non-goals: ไม่ทำระบบชำระเงินจริง ไม่ใช่ Marketplace
- กำหนดกรอบงบประมาณเริ่มต้น <= ฿2,000 ต่อขวด

---

## 2. Governance Rules for Future Changes

1. ทุกการปรับเปลี่ยนข้อกำหนด (Requirements), แบบจำลองข้อมูล (ERD/Schema), หรือการตัดสินใจ (Decisions) จะต้องถูกบันทึกในเอกสารนี้เสมอ
2. ระบุเลขเวอร์ชัน, วันที่, เหตุผล, และรายการข้อกำหนดที่ได้รับผลกระทบ
3. หากมีข้อขัดแย้งกับเอกสารเดิม ให้ทำบันทึกชี้แจง (Reconciliation Note) ไม่แก้เอกสารเงียบๆ


### P1 discovery and foundation proposal — 2026-11-10 / DPT-PLAN-001

Docs-only planning change, not a product/runtime release. Profiled pinned CC BY 4.0 Scento export;
added research findings, source-to-canonical mapping and observed conflict matrix. Replaced draft data
contracts with a 44-table logical proposal covering catalogue, provenance/rights/conflicts/staging,
media/evidence, personal listings/cart/purchases/inventory. Added hosting/object-vs-DB recovery evaluation,
ADRs 003–006, pilot task/test/readiness plan and canonical planning/task notes.

Reconciled roadmap/status/root overview with actual public repository/bootstrap and two-gate request.
Aligned domain concentration/packaging and matching-result semantics; corrected public-info/fair-use
assumptions and required-country/three-note defaults. Preserved existing confirmed requirements and
proposed matching weights. No raw dataset, code, SQL, cloud configuration, secret, merge or deployment.
Research gaps/permission constraints remain explicit, especially priority Thai samples, HMNS reuse,
image acquisition and live API response verification. Exact files/checkpoints: [[DPT-PLAN-001_P1_Data_Foundation]].


### Post-Review Correction S2 — 2026-11-10 / DPT-PLAN-001 / existing PR #1

Review start/current verified HEAD: `46c4a85309c408b3de7612d4853b166b84917359`; main unchanged at
`03481f7066487c44631cb9065899894ee8db71fb`. Same planning branch, PR OPEN/DRAFT.
R1: locator/occurrence identity preserves multiple claims per source record; scoped exact selection
and conflict-member resolution constraints. R2: non-null access_scope_id throughout provenance/assets,
public/shared/private ownership, RLS/API/storage rules, private overlays never materializing public data.
R3: scoped per-asset/capture/assessment grant, derivative parent/output rights and expiry/revocation checks.
Logical proposal grows 44 → 47 tables; original source profiling/mapping/conflict evidence and Task Map
retained. R4: public repository/existing workflow facts corrected in security/workflow/questions;
separate documentation CI backlog proposal only. Added 18 future OBS/ACL/IMG/REC negative/positive case
specifications and four-column OD-01..06 local/test/rights/cloud owner recommendations. No runtime tests.

Original immutable receipt [[2026-11-10_201028_DPT-PLAN-001_P1_Planning]] remains the single receipt;
no rewrite/second receipt. Exact correction paths and resulting checkpoint/evidence are in
[[DPT-PLAN-001_P1_Data_Foundation]]. No code, schema/database, Actions, cloud resources, deployment or merge.


S2 CURRENT_VERIFIED_HEAD_SHA / reviewed correction checkpoint: `83f13599a1b531229f22e0a68d35f86edd19278a`.
Observed after `docs(p1): address architecture review findings` committed 25 Markdown files. This
append-only event is included in the following documentation closeout checkpoint; final published branch/PR SHA is
in PR #1/final report. No rewrite of the original immutable receipt and no second receipt. Verified
25 docs, 23 vault frontmatters, 47 ERD/dictionary tables, 18 future cases; links/fences/diff/secret-pattern
checks succeeded. Runtime tests NOT RUN; R1–R4 resolved as proposals, owner decisions/rights still pending.


### Owner Decision Recording S3 — 2026-11-10 / DPT-PLAN-001 / PR #1

START/verified PR HEAD: `88de01f8cdf42680f50696350abdb9fd80f6c4c2`; main remains
`03481f7066487c44631cb9065899894ee8db71fb`. Authority is the Human Owner's current explicit decision
message, not an agent-inferred acceptance. OD-01..06 approved only for bounded local international
licensed-data pilot and model/metadata/rights/recovery targets. ADRs and planning/current status now
separate local approval, pending SQL/RLS tests, deferred permanent cloud/storage/final retention/RPO/RTO/
external backups, and regional imports blocked by usable rights plus samples. Existing source dataset
license evidence is not altered; local adoption approved with attribution, no wider content/image grant.
Source registry, pilot/backlog and overview/handoff scope summaries synchronized to prevent stale gates.

Gate P remains unsatisfied until Human Owner merges PR #1. This round is docs only; no SQL, database,
application code, cloud resources, Actions, provisioning/deployment/merge. Original immutable receipt
and research/Task Map preserved; no second receipt or new PR. Current exact paths and verification
are in [[DPT-PLAN-001_P1_Data_Foundation]]. Final published head recorded by existing PR/final report.

S3 validation result: 12 Markdown / 11 vault frontmatters / six matching owner-decision rows / 47-table
parity / zero errors; links/fences/source paths and common secret patterns checked; git diff check exit 0.
Receipt/research/schema-document hashes and original Task Map preserved; one receipt. Documents ready
for Owner Review, not runtime-verified/merged. Final same-branch commit/push and existing PR description
readback provide published SHA/state; no implementation or automatic merge.


## 2026-11-10 — IMP-P1-01 — local schema implementation / review checkpoint

Planning PR #1 owner-merge bffb2fab1918dc5221a6c5da7920168bcae263ca verified; implementation branch
impl/p1-01-local-postgres-schema starts there. Seven local migration groups implement all 47 logical
names, named constraints, scoped claims/private owners, whole-field/conflict/asset gates and RLS.
Actual current evidence: 63/63 tests via python database/verify.py, exit 0; 47 PK / 141 FK / 91 UNIQUE /
82 table CHECK / 58 deferred constraint-trigger constraints; 47 FORCE RLS tables, 203 policies.
Five domain checks/396 NOT NULL columns/244 indexes/195 user triggers measured separately.
Local foundation contains 53 field definitions and zero other domain rows; no full import or ETL.
Raw package hashes verified; 40 repeated-note groups/39 profiles preserved for review, exact real 12/5/58
shape fixtures roll back. Conservative findings, partial/not-run coverage and observed RED/fixes are in
[[IMP-P1-01_Implementation_Evidence]] and database/schema_findings.md.
Current planning-merge status reconciled; original research/Task Map/immutable planning receipt retained.
No new source rights, cloud/provider/storage, final retention/RPO/RTO, regional import or CI approval.
No main push, production mutation, merge, deployment, raw/private/dump/backup publication.
Independent exact-checkpoint review and final task receipt/Draft PR publication are next, not claimed done.
Exact resulting SHA will be recorded after commit, never invented self-referentially.


### IMP-P1-01 independent review correction (unpublished 42ae1df checkpoint)

One HIGH/three MEDIUM/one LOW findings confirmed by independent read-only source review and three
rollback-only SQL probes. Fixed private/shared/curator materialized-fact rights expiry/revocation,
expired-asset cross-tenant write outage, NaN acceptance, CRLF/LF checksums and endpoint-only-at-start
validation. Added six regression methods: full suite now 69/69 passed, exit 0. Actual revised inventory:
47 PK / 141 FK / 91 UNIQUE / 93 table CHECK / 59 deferred constraint triggers, 196 user triggers;
47 FORCE RLS tables / 203 policies, 5 domain checks / 396 NOT NULL / 244 indexes unchanged.
Scoped .gitattributes/UTF-8 LF checksum policy applied to database source only; raw dataset untouched.
Before unpublished foundation reset, all non-definition domain counts were zero and no other connection;
recreated/migrated foundation has 53 field definitions only and canonical replay no-op. No data loss,
production/global/provider changes or public migration rewrite. Re-review at new checkpoint is next.


### 2026-11-11 — IMP-P1-01 final source review and metadata closeout

Independent re-review of d25083c67ea73384ab13068bf41fb70755c0a0d0 confirms all five findings addressed, no
remaining code/security blocker in reviewed fixes.69/69 full tests pass; independent bounded probes
cleanup verified. LOW count correction82->93 made; current inventory CHECK93/deferred59/triggers196.
Original63-test/checkpoint82 counts above remain historical. Final source/migration hashes unchanged
in this metadata closeout. Receipt [[2026-11-11_000730_IMP-P1-01_Local_PostgreSQL]] is the single IMP-P1-01
receipt, distinct from unchanged DPT-PLAN-001 planning receipt. Final metadata commit/push and one
Draft PR are authorized next; actual published head/URL comes from GitHub readback/final report.
STOP after publication; no merge, production/cloud, actual import/bytes/restore or deferred decision change.

Final metadata validation:26 Markdown files,20 parsed vault frontmatters,47 ERD/dictionary/manifest/live
table names,6 unchanged matching OD rows; zero link/fence/frontmatter/common-secret-pattern errors.
Original receipt/three research blobs and original planning Task Map unchanged; exactly one IMP-P1-01
receipt. Full changed-path manifest44 files in database/evidence/documentation_checks.json. Mermaid,
API/storage/ETL/restore remain NOT RUN. Final staged checks and branch/remote head readback follow.

## S2 performance correction — current checkpoint, 2026-11-11

Existing [PR #2](https://github.com/kraveerachat/DoomParfum-By-TK/pull/2) remains OPEN/DRAFT on
impl/p1-01-local-postgres-schema. START/reviewed head3d377e0d78ec3af86e4c6ca03302b633c4ff11a7;
correction source/evidence checkpoint aa59b3d9e29e88697124d78e2f30e97271360586. Independent exact-source
review completed with no blocking finding. Published001–007 and original immutable receipt unchanged; no second receipt.

Additive008 coalesces full validators once per dirty epoch through private xid8/generation state and
post-statement scheduling. All original FK/RLS/permissions/conflict/provenance/materialization/image
rights and active-row checks remain. Natural-COMMIT synthetic250-record case5.841950s→0.051123s,
500→1 complete calls per validator; row callbacks remain. One run/case is not a capacity claim.
Full suite79/79 passed, failed0/errors0/skipped0, exit0;10 new positive/negative transaction tests.
Foundation8 migrations/53 field definitions/zero other domain rows/zero pending markers. Named
47-table inventory unchanged except243 domain user triggers (47 added statement triggers); one ops
queue trigger is excluded from domain counts. Details: [[IMP-P1-01_Performance_Correction]].

Global scans per dirty epoch, O(row) dispatcher/marker MVCC/WAL/queue cost and serialized writers remain.
IMP-P1-04 capacity/restore, IMP-P1-02 ETL, bytes/API/cloud/production remain NOT RUN. No owner decisions
changed. PRODUCTION_MUTATION=NO. Human Owner alone reviews/merges; no force push/new PR/merge.

TOOL EXECUTION CHECKPOINT: existing GitHub MCP/Git2.53.0.windows.2/PowerShell/Python3.11.9/
Docker/PostgreSQL16.15 and independent performance reviewer. No installation/host/account changes.
Official PG16 constraint/trigger/stats documentation consulted. Bounded synthetic before/after commands
completed five cases each; full verify79/79 exit0; documentation/model/link/frontmatter/secret-pattern
check passes at source checkpoint. Source and original receipt guards added to documentation checker.
No raw/private package/dump/backups committed. Current metadata closeout and PR update still pending.

### S2 review closeout — ready for Human Owner review

Exact correction source HEAD aa59b3d9e29e88697124d78e2f30e97271360586 independently reviewed: no blocking
finding;8 bounded independent checks passed and cleanup verified0. All16 source hashes match79/79
suite evidence. No code changed after source review, and reviewer did not claim full-suite/benchmark
reruns. Same-branch metadata commit/push and existing PR #2 description update follow these checks;
resulting final publication HEAD is verified in PR/final report, not invented inside its own commit.
Current source/checkpoint, exact correction file manifest, measurements, tests and limits:
[[IMP-P1-01_Performance_Correction]]. Original immutable receipt preserved; no second receipt.
Human Owner alone merges. No production/cloud/ETL/UI/main/force-push/auto-merge changes.
