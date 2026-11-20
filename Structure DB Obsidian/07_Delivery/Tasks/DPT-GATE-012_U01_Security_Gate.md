---
id: DPT-GATE-012
project: DoomParfum By TK
type: task
status: blocked
owner: human-owner
updated: 2026-11-20
tags: [doomparfum, security-gate, p30-u01, field-review, documentation-recovery]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
planning_pr: null
implementation_pr: null
---

# DPT-GATE-012 / P30-U01 — Field-Review Contract Security Gate

> [!WARNING]
> **Documentation recovery record only.** This note records the history of a *proposed* security contract. It is not security-design approval, Q-F acceptance, BatchA, Q-H, BatchB, implementation authorization, a runtime test result or a receipt. No U01 code exists. Every authority path is fail-closed **UNAVAILABLE**.

## 1. Identity and scope

| Field | Value |
|---|---|
| Task ID | `DPT-GATE-012` (security gate for packet unit `P30-U01`; `P30-U01` is a packet alias, not an allocated implementation task) |
| Parent planning | [[DPT-PLAN-011_Post_PR30_Data_App_Media_Readiness]] (PR31, Owner-merged at `183f1d857d83b64819762a2237c908fb95e36cb4`) |
| Packet dependencies | [Post_PR30_Dependency_Model.json](../../08_Operations/Test_Evidence/Post_PR30_Dependency_Model.json): U01 gates `DATA-01` and `DATA-04` of [[Post_PR30_Owner_Decision_Packet]]; data scope is [[Post_PR30_Canonical_Field_Review_Packet]] (46 claims: 43 DEFER / 3 UNKNOWN / 0 ACCEPT) |
| Subject | `PROPOSED-U01_Field_Review_Contract_Task_r<N>.md`: a contract for an offline validator that derives per-claim human field-review state from an Owner-signed ledger in Git, without touching the database (`review_state`, `canonical_selections`, `selection_guard` stay untouched) |
| Out of scope (all revisions) | DB writes, migrations, API/UI, real ranking, source acquisition, normalization, hold changes, Production, agent merge, agent signing, key handling, OP-1/OP-2 preparation |
| Contract artifacts location | Outside the repository, in Owner-workstation staging folders (absolute paths omitted for publication; see [[DPT-GATE-012_U01_Security_History_and_Recovery_Index]]) |
| Recovery task that wrote this note | `DPT-DOC-RECOVERY-001`, branch `docs/dpt-gate-012-security-history`, base `183f1d857d83b64819762a2237c908fb95e36cb4` |

## 2. Current status (verified 2026-11-20, Asia/Bangkok)

```text
LATEST CANDIDATE:        PROPOSED r11 (325441 B, sha256 1fdc33f97737a2c2066f88fc07422d2ed60e68ed9c0621b778e365bd1ce0d9c3)
LATEST REVIEW:           r11 review — CONDITIONAL, NOT READY (0 HIGH / 2 MEDIUM / 7 LOW open) — ADVISORY ONLY
G-IND (independent READY):            NOT SATISFIED (never satisfied for any revision)
Q-F (review provenance acceptance):   PENDING
BatchA / Q-H / Planning PR for U01:   NOT GIVEN / NOT AUTHORIZED / NOT CREATED
BatchB / implementation:              NOT GIVEN / NOT AUTHORIZED
OP-1 / OP-2 / RE / consumer verifier: UNAVAILABLE (design only; nothing established)
OPR-1 credential separation:          NOT IMPLEMENTED (observed 2026-11-20)
ACCEPTANCE SPECIFICATIONS RUN:        0 of 162 (all NOT RUN)
r12:                                  NOT STARTED
```

r11 must not be treated as READY. R11-IR-01 and R11-IR-02 are **OPEN** and are not resolved by anything in this note.

## 3. Historical timeline (summary)

| Rev | Date | Author (session) | Review | Verdict | Spec IDs | Specs run |
|---|---|---|---|---|---:|---:|
| r1 | before 2026-11-18 | UNVERIFIED | none | — | — | — |
| r2 | before 2026-11-18 | UNVERIFIED | separate security/data review (author UNVERIFIED) | not recorded | — | — |
| r3 | 2026-11-18 | "same author as r1/r2" (UNVERIFIED) | requested, NOT RUN | — | T-* SPECIFIED | 0 |
| r4 | 2026-11-18 | same author (UNVERIFIED) | requested, NOT RUN | — | T-* SPECIFIED | 0 |
| r5 | 2026-11-18 | same author (UNVERIFIED) | attempted twice, NOT RUN | — | T-* SPECIFIED | 0 |
| r6 | 2026-11-18 | same author (UNVERIFIED) | NOT RUN | — | T-* SPECIFIED | 0 (fixture probes only) |
| r7 | 2026-11-18 | coordinator in session directory `b62e346b…` (agent identity disputed) | `6bfdc7e4-570c-4c0e-91ff-334dca7e3976` | **BLOCKED** 1 H / 2 M / 5 L | T-* SPECIFIED | 0 (probes only) |
| r8 | 2026-11-18 | same as r7 (README: "Codex") | `f42e8e52-86fc-4ac0-a0c2-43796e4d448f` (file MISSING) | CONDITIONAL 0 / 2 / 5 | 75 | 0 |
| r9 | 2026-11-19 | `f42e8e52-…` | `f4126736-b419-42ab-be4d-412cf2ae0ffa` | CONDITIONAL 0 / 3 / 3 | 115 | 0 |
| r10 | 2026-11-19 | `f4126736-…` | `84b008e3-b4f4-4728-9b69-6de6b25b4767` | CONDITIONAL 0 / 4 / 6 | 147 | 0 |
| r11 | 2026-11-20 | `cabbc3b4-01ac-4fce-a7e9-8ad4ba375500` | `6d422490-cc14-4dba-84e9-361d29ffc278` (advisory) | CONDITIONAL 0 / 2 / 7 | 162 | 0 |

Every review from r7 onward was an AI agent under the same Windows account and harness as the authors, and r8 review → r11 review all used the same model (`claude-opus-5-5`). Reviews are therefore session-independent only. None satisfies G-IND.

## 4. Revision records (12 items each)

Evidence class labels refer to [[DPT-GATE-012_U01_Security_History_and_Recovery_Index]] §2. "Author-reported" means received evidence that this recovery could not re-verify.

### r1 — RECONSTRUCTED_REFERENCE_ONLY

1. **Purpose:** first reconciliation of the U01 field-review contract (`DPT-GATE-012_Reconciliation_Report.md`).
2. **Design changes / 3. Security architecture:** unknown; original MISSING.
4. **Findings addressed / 5. independently reviewed / 6. open:** unknown.
7. **Tests executed:** none recorded. **8. Not executed:** all.
9. **Owner decisions:** none verified.
10. **Files:** report 25470 B, `c9cd1d7ecd90883a6d70866913b7a2fb691178f41714433520a69fce213a9c4e`. MISSING; hash known from r3/r4 requests and r7. Not reconstructed.
11. **Git/PR:** none. **12. Remaining:** original can only be restored from an Owner backup.

### r2 — RECONSTRUCTED_REFERENCE_ONLY

1. **Purpose:** second draft; a separate Security/Data Review (`DPT-GATE-012_Security_Data_Review.md`) raised H-01…H-03, M-01…M-06 and L-01…L-03 against it (per r3).
2–3. **Design / security:** unknown beyond r3's statement that r3 corrects r2 per "Owner items 1–5" and those findings.
4–6. **Findings:** H/M/L set raised; reviewer identity UNVERIFIED.
7–8. **Tests:** none recorded.
9. **Owner decisions:** "Owner items 1–5" are reported by the r3 author only; NOT VERIFIED as Owner events.
10. **Files:** r2 20769 B `7ad15f2c40b52fbbc231f212dd7b2e31b9f0a401a9f7f40edbfa54d31e2b5cc5`; review 10947 B `855f66590ce2ed137e815f4545200ccba7b092f552b36c444f0fca5cfafa1d94`. Both MISSING.
11. **Git/PR:** none. **12. Remaining:** restore from Owner backup if any.

### r3 — 2026-11-18

1. **Purpose:** correct r2 per Owner items 1–5 and H/M/L findings.
2. **Design changes:** 46-claim scope, single facet `SOURCE_ASSERTION_FAITHFUL`; contract `dpt-field-review-1`; DB boundary; global `seq` / `prev_entry` chain with per-claim supersession.
3. **Security architecture:** S1 = SSH-signed ledger revisions; trust anchor bootstrap T1–T5; fixed Git argv G1–G5 based on `%G?`/`%GF`/`%GS`; reviewer salt.
4. **Findings addressed (author claim):** H-01 at contract level by S1; others re-rated. New author items N-01 (MEDIUM), N-02 independence (MEDIUM, open), N-03…N-05 (LOW).
5. **Independently reviewed:** none. Review request (3392 B) issued; NOT RUN.
6. **Open:** N-02 and all findings pending review.
7. **Executed:** none. **8. Not executed:** all T-MAN/T-DEF/T-SIG 1–16/T-LED/T-HEAD/T-REC/T-SEC/T-PRES/T-PROP.
9. **Owner decisions:** Q-A1…Q-A5, Q-B…Q-G posed; none answered.
10. **Files:** 35510 B `3fc9b120472c331136135fd0e7e03244ae9488619da1fd8e9fa84b5809c75c7a`; request 3392 B `04f8f9191d66e8de40796912db40d7edd7c4fba867d17d9694821787f27c4f1d`.
11. **Git/PR:** none. **12. Remaining:** independent review.

### r4 — 2026-11-18

1. **Purpose:** consolidated canonical draft.
2. **Design changes:** trust schema `-1`, ledger `-3` with RECORD/VOID, output `state-2`; first gate order (review → Q-H Planning PR → Owner reply → Planning merge → implementation).
3. **Security architecture:** Owner-only genesis Γ (G-01); full DAG walk with `GIT_NO_REPLACE_OBJECTS`, no shallow/grafts (G-02); run-time `--expected-owner-fingerprint` (G-03); immutable trust per version; salt removed.
4. **Findings addressed:** author-found G-01…G-16 (G-01/G-02/G-03 HIGH) and W-01 HIGH (contract outside the repo; needs docs-only Planning PR and Human Merge).
5. **Independently reviewed:** none; a 12-item consolidated request (6106 B) issued; NOT RUN.
6. **Open (author):** W-01 HIGH; N-02 MEDIUM (review not run because a plugin hook rewrote the agent input); M-02; N-05; G-10.
7. **Executed:** none. **8. Not executed:** all T-ANCHOR/T-GEN/T-DAG/T-SIG.
9. **Owner decisions:** Q-H added; none answered.
10. **Files:** 41630 B `aaf80a68244607ab2134f62ad767c14d56ee11b6daee268c6a10b95861e99dbd`; request 6106 B `cd76bd5a6915a95394df7ad5ac8645ad82b387be865c82173619923051861a80`.
11. **Git/PR:** none. **12. Remaining:** review; W-01 Planning PR.

### r5 — 2026-11-18

1. **Purpose:** consolidated canonical candidate.
2. **Design changes:** per-field manifest sources (R5-01); two-hash binding of the contract note (R5-02); diagnostics to stderr (R5-03); one `cat-file --batch-check` (R5-04); read-once TOCTOU rule (R5-05); VOID head (R5-06). Planning-PR file set defined.
3. **Security architecture:** first appearance of **OP-1** (Owner signing readiness) as a prerequisite (R5-07, MEDIUM, open).
4. **Findings addressed:** R5-01…R5-06 (author).
5. **Independently reviewed:** none. Gate Package r5 records two agent-review attempts, both blocked by a context-injection hook → INDEPENDENT_REVIEW_NOT_RUN.
6. **Open:** N-02, W-01, R5-07.
7. **Executed:** read-only Git observations only (author-reported). **8. Not executed:** every test.
9. **Owner decisions:** consolidated packet (DATA-01, DATA-04, D3, CONTRACT, TASK-ID, Q-A1…A5, Q-B…Q-H, OP-1, UNTRACKED, N-05); nothing selected.
10. **Files:** 49272 B `e3f53a83a878bd6ca9953217dc9210b13ac24b20b0d305d05dd3443916370538`; Gate Package r5 19785 B `3cdc44031140ea88f1320c3318a861912d81b0d9980498493c73a82133af0e4f`.
11. **Git/PR:** Planning PR manifest prepared, NOT created. **12. Remaining:** review, Owner packet.

### r6 — 2026-11-18

1. **Purpose:** apply verified fixture findings.
2. **Design changes:** G5c mode audit via `log --raw -m --full-history --no-renames` (V-06); exact note byte construction (V-07a); four distinct hash fields (V-07b); `validate_docs.py` tracked-output restore and `--task IMP-P1-02` mode (V-08, V-08b); `git status -z` (V-09).
3. **Security architecture:** unchanged trust model.
4. **Findings addressed:** V-06…V-09 (author). PRE-01 (stale P1-01 evidence on main) recorded, not fixed.
5. **Independently reviewed:** none.
6. **Open:** N-02, W-01, OP-1; author states no design HIGH/MEDIUM remains (later superseded by r7).
7. **Executed (author-reported, no surviving logs):** Git-primitive fixture checks in disposable repositories with ephemeral keys (T-MAN1 46/46, T-M, T-D, T-N, T-H, T-S, T-A1, T-P1). Not executions of a U01 validator.
8. **Not executed:** validator, regression suites, review.
9. **Owner decisions:** none.
10. **Files:** 57901 B `f290b2f2ee35de4d5791a325333b3f3e81064554407bcc978a007c2a34f39ec0`; Gate r6 18710 B `3e1d9d8e5ef6628a2c86e36ed1c859b2e925e7964a391e41ebdaa04742f89d43`.
11. **Git/PR:** none. **12. Remaining:** review (Q-F).

### r7 — 2026-11-18

1. **Purpose:** author-verified correction of r6 defects.
2. **Design changes:** C7-01 G5c separator grammar; C7-02 `%GS` terminal LF; C7-03 genesis limited to agent-authored commits; C7-04 INVALID before EVIDENCE_MISSING; C7-05 manifest bound to trust digest (MANIFEST_BINDING); C7-06 finite allowlist; C7-07 S1/S2 wording.
3. **Security architecture:** still Git-status-based S1 rule (`%G?`).
4. **Findings addressed:** C7-01…C7-07 (author).
5. **Independently reviewed:** **first independent review** (session `6bfdc7e4-…`), verdict **BLOCKED**: R7-IR-01 HIGH (signature-status rule bypassable through repository-controlled configuration), R7-IR-02 MEDIUM (acceleration data can hide history), R7-IR-03 MEDIUM (ledger structural precedence undefined), R7-IR-04…R7-IR-08 LOW.
6. **Open after review:** all R7-IR findings.
7. **Executed:** author-reported probe set 52 PASS / 2 EXECUTED FAIL / 3 HARNESS FAILURE (152 commands) plus 7 and 8 PASS docs checks; reviewer-run ephemeral harness reproductions of R7-IR-01/-02/-03/-04. Evidence JSONs and harness scripts MISSING.
8. **Not executed:** full validator, ledger/genesis/VOID, Owner signing, SQL/RLS.
9. **Owner decisions:** none.
10. **Files:** 69456 B `f12fc56bd5b40aa769bc5f4987ebc3fb2beb168989c62a6c49ad9e0115cfec7c`; Gate r7 19178 B `119ec8ad486c3b05676ebcc641e331cb16ee130744983a5b0618866eedbe294c`; Consolidated Handoff 37208 B `57210a21bcd524465c49dc1125d567fc73a40498893e92f46aa630bc4da92be4`; r7 review 38514 B `5cba0946a05fc02759b3b75836cfeb587c0e378bf9a64b9e57a084bfae4fa0f8`.
11. **Git/PR (verified then):** main `183f1d8`; PR31 MERGED 2026-11-17T14:02:10Z; PR8 OPEN/DRAFT/BLOCKED. **12. Remaining:** r8 for R7-IR-01…03.

### r8 — 2026-11-18

1. **Purpose:** address R7-IR-01…R7-IR-08.
2. **Design changes:** contract `dpt-field-review-2`, output `state-3`; staged first-failure model; Q-H rows with change kinds; two Owner batches (BatchA / BatchB); §8 acceptance table.
3. **Security architecture:** **S1-R8** direct `ssh-keygen -Y verify` over the raw commit payload (Git signature status retired); sealed bare verification repository with exact config; raw object closure; strict SSHSIG envelope; first **OP-2** trusted-runtime prerequisite.
4. **Findings addressed:** R7-IR-01…08, each "ADDRESSED IN PROPOSED TEXT; INDEPENDENT CLOSURE PENDING; RUNTIME NOT RUN".
5. **Independently reviewed:** session `f42e8e52-…`; CONDITIONAL 0 HIGH / 2 MEDIUM / 5 LOW (R8-IR-01 governed trust path, R8-IR-02 OP-2 objective, R8-IR-03…07). R7-IR-01 PARTIALLY RESOLVED; R7-IR-02…08 RESOLVED IN DESIGN. Review file MISSING (content known only as reproduced in r9).
6. **Open:** R8-IR-01…07.
7. **Executed:** author static assertions 21/21 and 25/25; input hashes 4/4. **8. Not executed:** 75 spec rows.
9. **Owner decisions:** none.
10. **Files:** 56187 B `8d2bf6a92116c179fe45aa3a15e37d665851f194322e40374c0adbc90eefd6de`; Gate r8 18652 B `faad28cb8f374a9df09c8ac685d578be22edc0b37705f73e78ba9d5eec6a8e53`; README r8 28581 B `799981715138ab0fe2be1c7f47ea9d68318a26be7ee3d1933c35e91e50641b34`; r8 review 42283 B `61cafef96c8eba372143bfd984225f75b36c76232f42ee9b9cdb585c7308881c` (MISSING).
11. **Git/PR:** read-only GitHub check: PR31 MERGED, PR8 only open PR. **12. Remaining:** r9.

### r9 — 2026-11-19

1. **Purpose:** address R8-IR-01…07.
2. **Design changes:** governed-path registry `GP_MANIFEST` / `GP_TRUST` / `GP_LEDGER`; exact schemas; historical vector HV; total execution order S0–S8; failure classes incl. `OPERATIONAL` exit 4; gate order A0–B6.
3. **Security architecture:** OP-2 runtime trust boundary (principals P_OWNER/P_OP/P_V/P_ADMIN/P_AGENT, C1–C4, OP2-A/B/C, runtime profile); G5c multiset audit; SHA-1 residual added.
4. **Findings addressed:** R8-IR-01…07 (proposed text).
5. **Independently reviewed:** session `f4126736-…`; CONDITIONAL 0 / 3 / 3: R9-IR-01 OP-1 signing boundary, R9-IR-02 Owner channel, R9-IR-03 validator provenance (MEDIUM); R9-IR-04…06 (LOW). R8-IR-02 PARTIALLY RESOLVED, others RESOLVED IN DESIGN.
6. **Open:** R9-IR-01…06.
7. **Executed:** author static checks 100/100. **8. Not executed:** 115 specs.
9. **Owner decisions:** none.
10. **Files:** 142018 B `f2d72f6cee0e6e5c8d4c5d50d4359fe87e101d4769653c544087c8f58ef36179`; Gate r9 32089 B `e112decb22204a3807c140ec9100432404fabe0d85751e820b455b39063aa309`; README r9 27000 B `6a273bd7be1911af29938e926a5813f1436f67dfdfeae0904b7a3013422b563a`; r9 review 50649 B `f1e6fa2b424f7d35bd222b66831a67491f73c6e08eec0d0e5989168fc17d3326`.
11. **Git/PR:** GitHub not queried. **12. Remaining:** r10.

### r10 — 2026-11-19

1. **Purpose:** address R9-IR-01…06.
2. **Design changes:** new §4.9 OP-1, §4.10 Owner Authorization Protocol (OAP), §4.11 validator provenance, §4.12 authority table; 44 execution steps; SHA-256 head binding (S6.4); profile `-2`; Γ as separate Owner-only PR.
3. **Security architecture:** Owner-signed hash-chained statements (namespace `dpt-u01-auth`, 8 kinds), out-of-band anchor ceremony, human-conveyed head; VSS in the root of trust with review manifest and Owner comparison at merge; SHA1DC pin; verified-bytes loader.
4. **Findings addressed:** R9-IR-01…06 (proposed text).
5. **Independently reviewed:** session `84b008e3-…`; CONDITIONAL 0 / 4 / 6: R10-IR-01 reviewer manifest authenticity, R10-IR-02 OP-1 execution boundary, R10-IR-03 signed-data authority, R10-IR-04 consumer verifier (MEDIUM); R10-IR-05…10 (LOW). R9-IR-01/02/03 PARTIALLY RESOLVED; R9-IR-04/05/06 RESOLVED IN DESIGN.
6. **Open:** R10-IR-01…10.
7. **Executed:** author static checks 109/109. **8. Not executed:** 147 specs.
9. **Owner decisions:** output folder and "proceed without frozen r8/r7 copies" directions received through the agent chat channel (not independently verified).
10. **Files:** 213977 B `53ebf7ed0d001f6308f90ef6826a3ef0546e5cba8a0e27ae1eec34abd38fb104`; Gate r10 20247 B `67df94f282f667a66663a12d3106730dd67f0042d504f9ae5f69d07b8b7c9469`; README r10 21390 B `25b76e047d8f3658508166bfe600e3e84bd5184924259e1179364beae936498a`; r10 review 74707 B `d2626bb50b56d4aa431a53041a8b08a853dc14dce69b87a6202a9acde3bbb546`.
11. **Git/PR:** none; GitHub not queried. **12. Remaining:** r11.

### r11 — 2026-11-20

1. **Purpose:** address R10-IR-01…10.
2. **Design changes:** reviewer environment (RE) with reviewer attestation RV-A (namespace `dpt-u01-review`) or human conveyance RV-B; trusted toolsets TP-COMMIT / TP-STATEMENT; `payload-check` demoted to pre-flight PF-1; signed-field provenance table (§4.13) with 14 Owner verification commands OVC-01…14; `LEDGER_STATE` anti-rollback; pre-OP-1 rules PG-1…PG-4 and `GOVERNANCE_RATIFICATION`; verifier bootstrap V-BOOT, pre-check VPC, `VERIFIER_READINESS`; binding table B01–B32; transitive revocation; writer allow-list; closed AST list CL-1…CL-12; feasibility checkpoint (§4.14).
3. **Security architecture:** seven trust roots, all DEFINED IN DESIGN and UNAVAILABLE; credential separation recorded as operational prerequisite OPR-1.
4. **Findings addressed:** R10-IR-01…10 (proposed text).
5. **Independently reviewed (advisory):** session `6d422490-…`; CONDITIONAL 0 / 2 / 7. R10-IR-01/02/05/06/07/08/10 RESOLVED IN DESIGN, R10-IR-09 RESOLVED, R10-IR-03 and R10-IR-04 PARTIALLY RESOLVED.
6. **Open:** R11-IR-01 MEDIUM (verifier revocation/supersession enforced only by the verifier being revoked); R11-IR-02 MEDIUM (statement bytes originate in agent drafts; no pre-signing grammar gate; `issued_at` unbounded); R11-IR-03…R11-IR-09 LOW (TT-1 closure depth; OVC forms that can return True without comparing; binding-table precision; V-BOOT/PF-1/`OP2_READINESS` order contradiction; Owner options removing custody/independence; reviewer tooling precision; evidence nits).
7. **Executed:** author static checks 85/85; reviewer read-only behaviour probes of standard OS/Git tools (not U01 tests, not attack tests). **8. Not executed:** 162 specs.
9. **Owner decisions:** none.
10. **Files:** 325441 B `1fdc33f97737a2c2066f88fc07422d2ed60e68ed9c0621b778e365bd1ce0d9c3`; Gate r11 21550 B `fdd037f7b50f075c74452dfb67be0671004f615a765075d4aff20082363093c3`; README r11 22437 B `2354036b13222647e730eff8f7482a0c14083d64589e214390b26fa58a62734e`; r11 review 76768 B `6bdef91eb4f0d3a1b3eeeb6bf292065079d6c230ab5273bff017bdbf2af7cf80`.
11. **Git/PR:** none for r11; this recovery PR is documentation only. **12. Remaining:** r12 (§10).

## 5. Session register

| Session | Role(s) | Model / agent | Date | Evidence |
|---|---|---|---|---|
| UNVERIFIED | r1–r6 author(s) | UNVERIFIED | ≤ 2026-11-18 | r3–r6 self-description "same author"; r3/r4 requests point to session directory `b62e346b…` |
| `b62e346b-00fe-4520-a926-25107e5ef706` (directory) | r7 author, r8 author, consolidated handoff | README r8 says "Codex"; directory is a Claude Code harness path — **identity disputed** | 2026-11-18 | README r8; r7 review; r11 §0.1 |
| `6bfdc7e4-570c-4c0e-91ff-334dca7e3976` | r7 reviewer | Claude Code, Opus 5.5 | 2026-11-18 | r7 review header |
| `f42e8e52-86fc-4ac0-a0c2-43796e4d448f` | r8 reviewer; r9 author | Claude Code, `claude-opus-5-5` | 2026-11-18/19 | README r9; r9 §0.1 |
| `f4126736-b419-42ab-be4d-412cf2ae0ffa` | r9 reviewer; r10 author | Claude Code, `claude-opus-5-5` | 2026-11-19 | r9 review §2; README r10 |
| `84b008e3-b4f4-4728-9b69-6de6b25b4767` | r10 reviewer (created by `/clear` after r10 author) | Claude Code, `claude-opus-5-5` | 2026-11-20 (Bangkok) | r10 review §2 |
| `cabbc3b4-01ac-4fce-a7e9-8ad4ba375500` | r11 author | Claude Code, `claude-opus-5-5` | 2026-11-20 (Bangkok) | README r11 |
| `6d422490-cc14-4dba-84e9-361d29ffc278` | r11 reviewer (advisory); DPT-DOC-RECOVERY-001 recorder | Claude Code, `claude-opus-5-5` | 2026-11-20 | r11 review §2; this note |
| `33a50b45-1ffc-4ed1-bd5e-ce239efff4c9` | DPT-DOC-RECOVERY-001 S2/S3 coordinator; r12 handoff preparer (excluded from r12 authoring and review) | Claude Code, `claude-opus-5-5` | 2026-11-20 | §11, §12 of this note |

All sessions above ran on one host and one Windows account with shared harness plugins and hooks. No human or different-model review has occurred.

## 6. Review register

| Review | Reviewer | Verdict | HIGH / MED / LOW | IND-00 | Satisfies G-IND | File |
|---|---|---|---|---|---|---|
| r3 / r4 requests | — | NOT RUN | — | — | NO | requests present |
| r5 attempts (×2) | agent | NOT RUN (hook rewrote input) | — | — | NO | Gate r5 |
| r7 | `6bfdc7e4-…` | BLOCKED | 1 / 2 / 5 | session level | NO | present (copy) |
| r8 | `f42e8e52-…` | CONDITIONAL | 0 / 2 / 5 | session level | NO | **MISSING** |
| r9 | `f4126736-…` | CONDITIONAL | 0 / 3 / 3 | session level | NO | present |
| r10 | `84b008e3-…` | CONDITIONAL | 0 / 4 / 6 | session level | NO | present |
| r11 | `6d422490-…` | CONDITIONAL (advisory) | 0 / 2 / 7 | session level | NO | present |

## 7. Findings register (latest state)

| Set | Raised in | Latest disposition (by whom) | Runtime closure |
|---|---|---|---|
| H-01…H-03, M-01…M-06, L-01…L-03 | r2 security/data review (MISSING) | author claims only (r3–r6); never independently reviewed | NO |
| N-01…N-05, G-01…G-16, W-01, R5-01…R5-07, V-06…V-09, C7-01…C7-07 | r3–r7 author | author claims; C7 set assessed by r7 review; W-01 (Planning PR) still open | NO |
| R7-IR-01…08 | r7 review | R7-IR-01 PARTIALLY RESOLVED, others RESOLVED IN DESIGN (r8 review, MISSING; reproduced in r9) | NO |
| R8-IR-01…07 | r8 review | R8-IR-02 PARTIALLY RESOLVED, others RESOLVED IN DESIGN (r9 review) | NO |
| R9-IR-01…06 | r9 review | 01/02/03 PARTIALLY RESOLVED; 04/05/06 RESOLVED IN DESIGN (r10 review) | NO |
| R10-IR-01…10 | r10 review | 03/04 PARTIALLY RESOLVED; others RESOLVED IN DESIGN or RESOLVED (r11 review, advisory) | NO |
| **R11-IR-01, R11-IR-02 (MEDIUM)** | r11 review | **OPEN** | NO |
| R11-IR-03…R11-IR-09 (LOW) | r11 review | OPEN | NO |
| Residuals needing Owner acknowledgement | r9–r11 | R7-IR-08 availability; SHA-1 object identity; pre-OP-1 governance channel — NOT ACKNOWLEDGED | — |

"RESOLVED IN DESIGN" is a reviewer's design judgement, never runtime evidence.

## 8. Test and evidence ledger

| Item | Executed by | Result | Evidence available |
|---|---|---|---|
| U01 acceptance specifications (r8 75 → r11 162) | nobody | NOT RUN | — |
| U01 validator / verifier | — | DOES NOT EXIST | — |
| r6 fixture probes (disposable repos, ephemeral keys) | r6 author | author-reported PASS | no logs (MISSING) |
| r7 primitive probe set (152 commands) | r7 author | 52 PASS / 2 EXECUTED FAIL / 3 HARNESS FAILURE | JSONs MISSING |
| r7 review harness reproductions | r7 reviewer | R7-IR-01 reproduced | harness MISSING |
| Author static document checks | r8, r9, r10, r11 authors | 21/21 + 25/25; 100/100; 109/109; 85/85 | in READMEs only |
| Reviewer static checks and source reading | r9, r10, r11 reviewers | recorded in reviews | reviews present |
| Recovery documentation checks | DPT-DOC-RECOVERY-001 | see [[DPT-GATE-012_U01_Security_History_and_Recovery_Index]] §6 | this PR |

## 9. Owner decisions

| Decision | State |
|---|---|
| Any approval of any revision r1–r11 | **NONE VERIFIED** |
| Q-F (review provenance) | PENDING |
| BatchA (incl. three acknowledgements) and Q-H rows | NOT GIVEN |
| BatchB, OP-1 (E1–E10), OP-2 (F1–F12), OP-2-TOOL, Q-A1…Q-A7, Q-B…Q-G, DATA-01, DATA-04, D3/SEQ-01, CONTRACT, TASK-ID | PENDING |
| r10 output folder; proceed without frozen r8/r7 copies | Owner directions **reported** by the r10 author through the agent chat channel; not independently verified |
| PR31 merge (parent planning) | VERIFIED GitHub event: MERGED 2026-11-17T14:02:10Z at `183f1d8`. It is not a U01 decision. |

Recommended defaults inside the contracts (for example OP1-A/OP2-A on a dedicated machine, `sk-ssh-ed25519`, MANUAL preparation) are proposals only.

## 10. Blockers and next actions

**Blockers:** G-IND never satisfied; R11-IR-01/02 open; OPR-1 not implemented; OP-1, OP-2, RE and consumer verifier unavailable; no Owner-custody record of expected hashes (OPR-2); W-01 (no U01 Planning PR).

**Next actions (Owner):**
1. Decide whether to commission r12, scoped to R11-IR-01/02 (mandatory) and R11-IR-03…09, with an r11 → r12 delta register; r11 bytes stay frozen.
2. Commission the r12 review from a different model family or a human reviewer, on an account and machine agents do not use.
3. Consider OPR-1 (separate, restricted agent GitHub identity), OPR-2 (Owner-custody hash record) and OPR-3 (backups of r9–r11 and reviews outside the agent account).
4. Review and, if appropriate, merge this documentation-only PR. Merging it approves nothing in §9.

Future r12/r13 history continues on branch `docs/dpt-gate-012-security-history` and its single PR (see [[DPT-GATE-012_U01_Security_History_and_Recovery_Index]] §8). No final receipt exists or may be created while acceptance is pending.

## 11. Session 2026-11-20 S2 — publication readiness and r12 handoff preparation

- **Task / session:** DPT-GATE-012 (documentation workstream; recovery task DPT-DOC-RECOVERY-001) / S2, Claude Code session `33a50b45`, `claude-opus-5-5`. Role: documentation coordinator. This session is not a reviewer or author of any revision, and is not independent of the earlier sessions (same model, host and account).
- **Intake class:** A (continuation; same branch, same future PR). Owner prompt: DPT-GATE-012-U01-CONTINUATION.
- **Branch / PR:** `docs/dpt-gate-012-security-history`. PR: **PR_NOT_CREATED** (verified on GitHub: none for this head). Remote branch: **NOT_PUSHED**.
- **Starting SHA:** `987279a98cf1a48ee657f0b9f4f78581063c9e01` (parent = current `origin/main` `183f1d857d83b64819762a2237c908fb95e36cb4`).

**Work performed**
1. Re-verified Git and GitHub: `origin/main` unchanged; the branch is 1 ahead / 0 behind; the 987279a diff is exactly the 7 recorded vault paths and is docs-only; `git diff --check` is clean; the sensitive-data scan of added lines found 0 matches. The only open PR is PR8.
2. **Credential boundary unchanged:** the only GitHub credential is the Owner's own broad-scope login (system credential manager). No push or PR creation was attempted, and remote write is OWNER_ACTION_REQUIRED.
3. Re-hashed the r10/r11 inputs (8 files): all match the recorded sizes and SHA-256. No r12 folder exists.
4. Ran an integration simulation against the DPT-GOV-WORKFLOW-001 branch (`git merge-tree`): one append-only conflict hunk in each of the 5 shared notes, resolvable by keeping both sections. No merge was committed.
5. Prepared [[DPT-GATE-012_U01_r12_Authoring_Handoff]] (design-level, sanitized), with inputs, mandatory R11-IR-01/02 remediation, LOW dispositions, frozen requirements, invariants, expected specifications, static validation, the NOT RUN list, review conditions, pending Owner decisions and completion criteria.

**Exact files changed:** this note; the new handoff note above; [[DPT-GATE-012_U01_Security_History_and_Recovery_Index]] (re-verification appendix); `08_Operations/Agent_Run_Log.md`; `08_Operations/Change_Log.md`.

**Security status (unchanged; nothing re-reviewed):** r11 CONDITIONAL — NOT READY; R11-IR-01 and R11-IR-02 MEDIUM OPEN; R11-IR-03…09 LOW OPEN; 0 of 162 specifications run; G-IND NOT SATISFIED; Q-F PENDING; BatchA and Q-H NOT AUTHORIZED; OP-1/OP-2 UNAVAILABLE; r12 NOT STARTED (handoff prepared, not commissioned).

**Tests:** `validate_docs.py` and the static checks are recorded in the Agent_Run_Log S2 entry. No U01 or runtime test was run.

**Blockers:** the credential boundary (publication); G-IND; the R11 MEDIUM findings; OPR-1/2/3 not implemented; no environment that meets OP-1/OP-2.

**Next action:** the Owner publishes this branch as a Draft PR and decides whether to commission the r12 author and the r12 reviewer (handoff §10–§11).

**Checkpoint SHA:** the S2 commit that adds this section (recorded by the next session).

## 12. Session 2026-11-20 S3 — agent-managed publication attempt (blocked) and first execution report

- **Task ID / Session ID:** DPT-DOC-RECOVERY-001 (DPT-GATE-012 documentation) / S3, Claude Code session `33a50b45`.
- **Agent / Role:** documentation coordinator; same session as S2, so not independent.
- **Intake class:** A (continuation; same branch and the same PR once it exists).
- **Applicable plan:** recovery scope as recorded in §1; the Owner directive of 2026-11-20 on agent-managed publication.
- **Branch / PR (verified state):** `docs/dpt-gate-012-security-history`, starting SHA `3c97dca83abe508dc070d64bf3e71d10847293d0`, 2 ahead / 0 behind `origin/main` `183f1d857d83b64819762a2237c908fb95e36cb4`; remote branch absent; no PR.

**Work performed**
1. Re-verified the branch, the worktree (clean) and the GitHub state. The only open PR is PR8, and no PR exists for this branch.
2. **Publication not attempted.** The Owner directed that agents push and open Draft PRs with an appropriately authorized agent identity. The only GitHub credential available is still the Owner's own broad-scope login. The Owner's standing instruction for this workstream forbids using it from an agent session, and this directive does not revoke that. The status is therefore `AGENT_CREDENTIAL_REQUIRED`. The prerequisite (a dedicated, repository-scoped agent identity that cannot update `main`) is drafted in the DPT-GOV-WORKFLOW-001 Planning PR, `DEVELOPMENT_WORKFLOW.md` §5.6 on that branch. It is the same measure as OPR-1 in §10 of this note.
3. Wrote this workstream's first execution report under the proposed dual-report rule (§13).

**Exact files changed:** this note; `08_Operations/Reports/DPT-GATE-012-U01/2026-11-20_DPT-DOC-RECOVERY-001_S3_Report.md` (new); `08_Operations/Agent_Run_Log.md`.

**Decisions made:** none. **Findings:** none new.

**Security status (unchanged; nothing re-reviewed):** r11 CONDITIONAL — NOT READY; R11-IR-01 and R11-IR-02 MEDIUM OPEN; R11-IR-03…09 LOW OPEN; 0 of 162 specifications run; G-IND NOT SATISFIED; Q-F PENDING; BatchA and Q-H NOT AUTHORIZED; OP-1/OP-2 UNAVAILABLE; r12 NOT STARTED. The handoff is not recreated.

**Tests:** recorded in the S3 report. **Not executed:** independent review of this documentation; Markdown rendering; any U01 or runtime test.

**Blockers:** `AGENT_CREDENTIAL_REQUIRED` (publication); G-IND; the R11 MEDIUM findings; OPR-1/2/3; OP-1/OP-2.

**Next action:** once an agent publishing identity exists, a class-A session pushes this branch, opens its Draft PR, and records the PR number, URL and SHAs here. Alternatively, the Owner explicitly authorizes a one-time use of the Owner login.

**Checkpoint SHA:** the S3 commit that adds this section (recorded by the next session).

## 13. Reports

Execution reports for this workstream (proposed dual-report rule, DPT-GOV-WORKFLOW-001 `DEVELOPMENT_WORKFLOW.md` §4.7). Applied from S3 onward. Earlier sessions and the raw contract and review files are not republished.

| File | Session | SHA-256 | Kind |
|---|---|---|---|
| `08_Operations/Reports/DPT-GATE-012-U01/2026-11-20_DPT-DOC-RECOVERY-001_S3_Report.md` | S3 | `e1c871388ce06ac0c9d1c26c86a836447ffa47dd38e73a235c40b162705e581e` | public-safe; identical private copy in `Downloads\DPT-GATE-012-U01\Responses\` |
