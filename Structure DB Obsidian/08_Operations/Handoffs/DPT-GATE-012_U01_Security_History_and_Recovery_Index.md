---
id: DPT-GATE-012-RECOVERY-INDEX
project: DoomParfum By TK
type: continuity_handoff
status: proposed
owner: human-owner
updated: 2026-11-20
tags: [doomparfum, handoff, security-gate, p30-u01, documentation-recovery]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# DPT-GATE-012 / U01 — Security History and Recovery Index

Recovery task `DPT-DOC-RECOVERY-001`, 2026-11-20 (Asia/Bangkok). Canonical task record: [[DPT-GATE-012_U01_Security_Gate]].

> [!IMPORTANT]
> DOCUMENTATION RECOVERY ONLY. SECURITY DESIGN APPROVAL: NO. IMPLEMENTATION AUTHORIZATION: NO. U01 RUNTIME TESTS: NOT RUN. G-IND: NOT SATISFIED. Q-F: PENDING. BATCHA: NOT AUTHORIZED. Q-H: NOT AUTHORIZED. OWNER MERGE: REQUIRED.

## 1. Recovery method

- **Recorder:** Claude Code session `6d422490-cc14-4dba-84e9-361d29ffc278` (`claude-opus-5-5`). The same session wrote the advisory r11 review. This index is agent-produced evidence, not an independent authentication.
- **Discovery (read-only):** Owner-workstation download folders (root and per-revision folders), the `DPT-DOC-RECOVERY-001` staging folder, the agent temporary-file tree, both local repository checkouts, and `origin/main` history. The Owner-named folder `DPT-GATE-012-Recovery-Inputs` does not exist.
- **Reading coverage:** every contract r3–r11, Gate Packages r5–r11, READMEs r8–r11, reviews r7/r9/r10/r11, review requests r3/r4 and the consolidated handoff were read in full. Successive revisions were read by line-level delta: a line byte-identical to a line already read counts as read. A working coverage record was kept outside the repository.
- **Hashing:** SHA-256 over exact file bytes (`sha256sum`), file sizes by `stat`, 2026-11-20.
- **Repository baseline:** fetched `origin/main` = `183f1d857d83b64819762a2237c908fb95e36cb4` (confirmed by `ls-remote`). Before this change, `git grep DPT-GATE-012` on that commit found no vault record.

## 2. Evidence classes

| Class | Meaning in this index |
|---|---|
| `VERIFIED_ORIGINAL` | File at the output location its author recorded, bytes equal to a SHA-256 recorded by a later document or an Owner assignment. Proves location and byte identity only. Custody is **not** independently authenticated: the folders are writable by every agent session on the shared account, and the reference hashes travelled through the agent chat channel. |
| `HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED` | A copy outside the original location (original location gone), bytes equal to a recorded SHA-256. Who placed it is not established. |
| `UNVERIFIED_COPY` | Present, no recorded reference value. |
| `HASH_MISMATCH` | Present, bytes differ from the recorded value. |
| `MISSING` | Recorded by size and hash, not found. |
| `RECONSTRUCTED_REFERENCE_ONLY` | Content known only from descriptions in later documents. Nothing was reconstructed as a file. |

## 3. Artifact inventory

Locations are given relative to the Owner's download folder; absolute paths are omitted for publication (§7).

| # | Artifact | Location | Bytes | SHA-256 | Reference | Class |
|---|---|---|---:|---|---|---|
| 1 | r11 review (advisory) | `DPT-GATE-012-U01-r11-review/` | 76768 | `6bdef91eb4f0d3a1b3eeeb6bf292065079d6c230ab5273bff017bdbf2af7cf80` | Owner recovery update; self-recorded at handoff | VERIFIED_ORIGINAL |
| 2 | Contract r11 | `DPT-GATE-012-U01-r11/` | 325441 | `1fdc33f97737a2c2066f88fc07422d2ed60e68ed9c0621b778e365bd1ce0d9c3` | Owner r11-review assignment | VERIFIED_ORIGINAL |
| 3 | Gate Package r11 | `DPT-GATE-012-U01-r11/` | 21550 | `fdd037f7b50f075c74452dfb67be0671004f615a765075d4aff20082363093c3` | same | VERIFIED_ORIGINAL |
| 4 | README r11 | `DPT-GATE-012-U01-r11/` | 22437 | `2354036b13222647e730eff8f7482a0c14083d64589e214390b26fa58a62734e` | same | VERIFIED_ORIGINAL |
| 5 | r10 review | `DPT-GATE-012-U01-r10-review/` | 74707 | `d2626bb50b56d4aa431a53041a8b08a853dc14dce69b87a6202a9acde3bbb546` | same | VERIFIED_ORIGINAL |
| 6 | Contract r10 | `DPT-GATE-012-U01-r10/` | 213977 | `53ebf7ed0d001f6308f90ef6826a3ef0546e5cba8a0e27ae1eec34abd38fb104` | same | VERIFIED_ORIGINAL |
| 7 | Gate Package r10 | `DPT-GATE-012-U01-r10/` | 20247 | `67df94f282f667a66663a12d3106730dd67f0042d504f9ae5f69d07b8b7c9469` | same | VERIFIED_ORIGINAL |
| 8 | README r10 | `DPT-GATE-012-U01-r10/` | 21390 | `25b76e047d8f3658508166bfe600e3e84bd5184924259e1179364beae936498a` | same | VERIFIED_ORIGINAL |
| 9 | r9 review | `DPT-GATE-012-U01-r9-review/` | 50649 | `f1e6fa2b424f7d35bd222b66831a67491f73c6e08eec0d0e5989168fc17d3326` | Gate r10 §1; Contract r11 §0.2 | VERIFIED_ORIGINAL |
| 10 | Contract r9 | `DPT-GATE-012-U01-r9/` | 142018 | `f2d72f6cee0e6e5c8d4c5d50d4359fe87e101d4769653c544087c8f58ef36179` | same | VERIFIED_ORIGINAL |
| 11 | Gate Package r9 | `DPT-GATE-012-U01-r9/` | 32089 | `e112decb22204a3807c140ec9100432404fabe0d85751e820b455b39063aa309` | same | VERIFIED_ORIGINAL |
| 12 | README r9 | `DPT-GATE-012-U01-r9/` | 27000 | `6a273bd7be1911af29938e926a5813f1436f67dfdfeae0904b7a3013422b563a` | same | VERIFIED_ORIGINAL |
| 13 | Contract r8 | folder root | 56187 | `8d2bf6a92116c179fe45aa3a15e37d665851f194322e40374c0adbc90eefd6de` | Contract r11 §0.2 | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 14 | Gate Package r8 | folder root | 18652 | `faad28cb8f374a9df09c8ac685d578be22edc0b37705f73e78ba9d5eec6a8e53` | same | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 15 | README r8 | folder root | 28581 | `799981715138ab0fe2be1c7f47ea9d68318a26be7ee3d1933c35e91e50641b34` | same | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 16 | Consolidated Handoff Report (r7 era) | folder root | 37208 | `57210a21bcd524465c49dc1125d567fc73a40498893e92f46aa630bc4da92be4` | Contract r11 §0.2; r7 review | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 17 | r7 review (pasted text) | folder root | 38514 | `5cba0946a05fc02759b3b75836cfeb587c0e378bf9a64b9e57a084bfae4fa0f8` | Contract r11 §0.2 | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 18 | Contract r7 | folder root | 69456 | `f12fc56bd5b40aa769bc5f4987ebc3fb2beb168989c62a6c49ad9e0115cfec7c` | Contract r11 §0.2; r7 review | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 19 | Gate Package r7 | folder root | 19178 | `119ec8ad486c3b05676ebcc641e331cb16ee130744983a5b0618866eedbe294c` | same | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 20 | Contract r6 | folder root | 57901 | `f290b2f2ee35de4d5791a325333b3f3e81064554407bcc978a007c2a34f39ec0` | Contract r7 artifact table | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 21 | Gate Package r6 | folder root | 18710 | `3e1d9d8e5ef6628a2c86e36ed1c859b2e925e7964a391e41ebdaa04742f89d43` | same | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 22 | Gate Package r5 (unsuffixed name) | folder root | 19785 | `3cdc44031140ea88f1320c3318a861912d81b0d9980498493c73a82133af0e4f` | same | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 23 | Contract r5 | folder root | 49272 | `e3f53a83a878bd6ca9953217dc9210b13ac24b20b0d305d05dd3443916370538` | same | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 24 | r4 review request | folder root | 6106 | `cd76bd5a6915a95394df7ad5ac8645ad82b387be865c82173619923051861a80` | same | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 25 | Contract r4 | folder root | 41630 | `aaf80a68244607ab2134f62ad767c14d56ee11b6daee268c6a10b95861e99dbd` | same; r4 request | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 26 | r3 review request | folder root | 3392 | `04f8f9191d66e8de40796912db40d7edd7c4fba867d17d9694821787f27c4f1d` | Contract r7; r4 request | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 27 | Contract r3 | folder root | 35510 | `3fc9b120472c331136135fd0e7e03244ae9488619da1fd8e9fa84b5809c75c7a` | same; r3/r4 requests | HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED |
| 28 | r8 review | — | 42283 | `61cafef96c8eba372143bfd984225f75b36c76232f42ee9b9cdb585c7308881c` | Contract r11 §0.2 | MISSING (findings RECONSTRUCTED_REFERENCE_ONLY from r9) |
| 29 | Contract r2 | — | 20769 | `7ad15f2c40b52fbbc231f212dd7b2e31b9f0a401a9f7f40edbfa54d31e2b5cc5` | r3/r4 requests; Contract r7 | MISSING; RECONSTRUCTED_REFERENCE_ONLY |
| 30 | Security/Data Review (on r2) | — | 10947 | `855f66590ce2ed137e815f4545200ccba7b092f552b36c444f0fca5cfafa1d94` | same | MISSING; RECONSTRUCTED_REFERENCE_ONLY |
| 31 | r1 Reconciliation Report | — | 25470 | `c9cd1d7ecd90883a6d70866913b7a2fb691178f41714433520a69fce213a9c4e` | same | MISSING; RECONSTRUCTED_REFERENCE_ONLY |
| 32 | Master Handoff used as r7 input | — | 16975 | `96b71c1b…` (prefix only recorded) | Consolidated Handoff | MISSING |
| 33 | r7-era evidence JSONs (technical, docs recheck, docs r7, source registry, final verification) and harness scripts | — | 89054 / 9888 / 10538 / 13162 / 39882 | prefixes `6fe5b61d…`, `2ec65365…`, `5cac1a36…`, `828b47c6…`, `317bed2d…` | Consolidated Handoff | MISSING |
| 34 | r7 reviewer harness scripts | — | — | not recorded | r7 review | MISSING |

**Totals:** 12 VERIFIED_ORIGINAL, 15 HASH_VERIFIED_COPY_CUSTODY_UNVERIFIED, 0 UNVERIFIED_COPY, 0 HASH_MISMATCH, 7 MISSING rows (four of them also RECONSTRUCTED_REFERENCE_ONLY).

**Custody notes.**
- Rows 13–16 and 18–27 were created in the download folder on 2026-11-20 between 10:24 and 10:38 local time, after r11 was written. The originals lived in an agent temporary directory that no longer exists. Contract r11 §0.2 therefore correctly recorded r7/r8 as unavailable when it was written.
- Row 17 dates from 2026-11-18 21:54 local. The r9 review recorded it as absent on 2026-11-19; the r10 review found it present. That gap is unexplained.
- Row 1 was written by the recorder session. Its hash match only shows that it is unchanged since that session's handoff.
- No file was moved, renamed, modified or committed. Raw contracts and reviews are **not** added to the repository (§7).

## 4. Reviewer limitations

- No review satisfied G-IND. Every review was an AI agent under the same Windows account, harness, plugins and hooks as the authors; r8 review through r11 review all used `claude-opus-5-5`.
- The r8 review is MISSING; its findings are known only as reproduced in r9, which was written by the same session that wrote the r8 review.
- Every expected hash given to reviewers travelled through the agent chat channel; no Owner-custody record exists (OPR-2).
- Context-injection hooks were observed in several sessions (r4/r5 review attempts blocked; r9 authoring tool input changed; r10/r11 reviews saw injected guidance).
- Agent identity of the r7/r8 author is disputed (§5 of the task note).

## 5. Coverage record (summary)

| Document set | Coverage |
|---|---|
| Governance: `AGENTS.md`, `DEVELOPMENT_WORKFLOW.md`, root `README.md`, vault `README.md` | read in full at `183f1d8` |
| Vault: `Project_Status`, `Decision_Log`, `Agent_Run_Log`, `Change_Log`, `Pending_Questions`, `Project_Index` | read in full at `183f1d8` (logs de-duplicated by identical paragraphs) |
| Contracts r3–r11 | read in full (delta method) |
| Gate Packages r5–r11; READMEs r8–r11 | read in full (delta method) |
| Reviews r7, r9, r10, r11; requests r3, r4; consolidated handoff | read in full |
| r1, r2, r2 review, r8 review, r7-era evidence | NOT AVAILABLE |
| Earlier `DPT-DOC-RECOVERY-001` staging package | reviewed; superseded by this index (its MISSING rows for r3–r5 and r8 files are corrected here) |

## 6. Documentation checks for this change

Executed 2026-11-20 in the isolated worktree, before the local commit:

| Check | Result |
|---|---|
| `git diff --check` (new files included with intent-to-add) | PASS, no output |
| Append-only: `Agent_Run_Log`, `Change_Log`, `Decision_Log`, `Project_Index` equal their `183f1d8` blob (with only the `updated` line changed) followed by the new section | PASS ×4 |
| Insert-only: `Project_Status` equals its `183f1d8` blob with one section inserted above the previous top section, plus the `updated` line | PASS |
| New notes: 8 frontmatter fields, `source_of_truth` resolves, balanced fences, LF, no trailing whitespace | PASS ×2 |
| Wiki links in added text resolve to vault files | PASS |
| Bounded secret and private-path scan of added lines (local paths, host/account names, token and key patterns, e-mail) | PASS; 2 benign word matches ("Scope:", the omissions row naming private keys) |
| `python database/validate_docs.py --task IMP-P1-02` | exit 1: 52 errors, **all pre-existing** unresolved wiki links to `.json` evidence files already present in the `183f1d8` versions of the touched shared notes; 0 introduced by this change; secret-pattern candidates 0; historical evidence, migrations and receipts unchanged. The tracked output `database/evidence/scento_documentation_checks.json` was restored afterwards. |
| `git status --porcelain=v1 -z` | exactly the 7 allowlisted vault paths |

The validator's `.json` wiki-link behaviour is a pre-existing condition of the shared logs and is not changed here.

## 7. Publication policy and recorded omissions

The repository is public. The following were deliberately **not** committed:

| Omitted | Reason |
|---|---|
| Raw contracts r3–r11, Gate Packages, READMEs, reviews, requests, consolidated handoff | Large raw security material; contains host-specific paths, account details and detailed bypass analysis. Hashes and summaries only. |
| Absolute local paths, user-profile and temporary-directory paths, attachment paths | Private workstation layout |
| Host name, Windows account name, group membership details, credential scopes and key-file observations | Security-sensitive environment facts. Summarized as "the observed environment does not meet the principal-separation conditions" and "OPR-1 not implemented". |
| Step-by-step reproduction of R7-IR-01 and other bypass findings; probe outputs | Exploit detail. Findings are described at design level only. |
| Primary-source copies fetched by reviewers | Third-party content; only names and versions are cited by the reviews themselves. |
| Token values, private keys, signatures | None were read, exported or created. |

## 8. Continuation instructions

1. **Same branch, same PR.** Future r12 and r13 history for DPT-GATE-012 is added to branch `docs/dpt-gate-012-security-history` and its single Draft PR, as dated sections appended to [[DPT-GATE-012_U01_Security_Gate]], this index and the shared logs. Do not open a second PR.
2. For each new revision, record the 12 items of task note §4, the session register row, file sizes and SHA-256, and the review verdict with the exact finding IDs.
3. Do not mark any finding resolved without a review that states it, and never mark runtime closure without executed acceptance evidence.
4. Do not create the immutable final receipt until the Owner accepts the gate (G-IND, Q-F and the Owner batches). This PR contains no receipt.
5. Before writing, re-verify `origin/main`, the branch head and every artifact hash; record new MISSING or HASH_MISMATCH results instead of repairing them.
6. Keep raw security reports out of the repository unless the Owner approves a redacted copy.

## 9. Re-verification, 2026-11-20 S2

Claude Code session `33a50b45` re-hashed inventory rows 1–8 (r11 review, contract r11, Gate Package r11, README r11, r10 review, contract r10, Gate Package r10, README r10) with `sha256sum` and `stat`. **8/8 match** the recorded bytes and SHA-256. No new MISSING or HASH_MISMATCH result. Rows 9–34 were not re-hashed in this session. No r12 artifact exists. Next step: [[DPT-GATE-012_U01_r12_Authoring_Handoff]].
