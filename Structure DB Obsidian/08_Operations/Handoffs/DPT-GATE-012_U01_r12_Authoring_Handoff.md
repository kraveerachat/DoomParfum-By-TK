---
id: DPT-GATE-012-R12-HANDOFF
project: DoomParfum By TK
type: continuity_handoff
status: proposed
owner: human-owner
updated: 2026-11-20
tags: [doomparfum, handoff, security-gate, p30-u01, r12]
source_of_truth: "../../../DEVELOPMENT_WORKFLOW.md"
---

# DPT-GATE-012 / U01 — r12 Authoring Handoff

Canonical task record: [[DPT-GATE-012_U01_Security_Gate]]. Artifact inventory: [[DPT-GATE-012_U01_Security_History_and_Recovery_Index]].

> [!IMPORTANT]
> HANDOFF BRIEF ONLY. r12: NOT STARTED. This note does not author, review or approve any revision. SECURITY DESIGN APPROVAL: NO. Q-F: PENDING. BATCHA: NOT AUTHORIZED. Q-H: NOT AUTHORIZED. U01 IMPLEMENTATION: NOT AUTHORIZED. U01 RUNTIME TESTS: 0 RUN. G-IND: NOT SATISFIED.

## 1. Identity, routing and provenance

| Field | Value |
|---|---|
| Workstream | DPT-GATE-012 / P30-U01 field-review contract security gate |
| Intake class | A: continuation of the same documentation/review workstream (r11 → r12), recorded on branch `docs/dpt-gate-012-security-history` and its single PR |
| Prepared by | Claude Code session `33a50b45`, `claude-opus-5-5`, 2026-11-20. This is the same model, host and account as every r7–r11 author and reviewer. The session did not author or review any revision, and it must not author or review r12. |
| Sources read | r11 review (full findings §1, §7–§12; Q-R8 to Q-R12), Gate Package r11 §4–§6, contract r11 headings. The canonical task note and the recovery index were read in full. |
| Commissioning | The Owner decides whether to commission r12 and assigns its author (task note §10, action 1). Nothing here assigns it. |

## 2. Inputs (re-hashed 2026-11-20 with `sha256sum`; all match the recorded values)

Locations are relative to the Owner's download folder; absolute paths are omitted (recovery index §7).

| Artifact | Location | Bytes | SHA-256 | Class |
|---|---|---:|---|---|
| Contract r11 (frozen; r12 base) | `DPT-GATE-012-U01-r11/` | 325441 | `1fdc33f97737a2c2066f88fc07422d2ed60e68ed9c0621b778e365bd1ce0d9c3` | VERIFIED_ORIGINAL |
| Gate Package r11 | `DPT-GATE-012-U01-r11/` | 21550 | `fdd037f7b50f075c74452dfb67be0671004f615a765075d4aff20082363093c3` | VERIFIED_ORIGINAL |
| README r11 | `DPT-GATE-012-U01-r11/` | 22437 | `2354036b13222647e730eff8f7482a0c14083d64589e214390b26fa58a62734e` | VERIFIED_ORIGINAL |
| **r11 review (complete; normative source of the corrections below)** | `DPT-GATE-012-U01-r11-review/` | 76768 | `6bdef91eb4f0d3a1b3eeeb6bf292065079d6c230ab5273bff017bdbf2af7cf80` | VERIFIED_ORIGINAL (advisory review) |
| Contract r10 | `DPT-GATE-012-U01-r10/` | 213977 | `53ebf7ed0d001f6308f90ef6826a3ef0546e5cba8a0e27ae1eec34abd38fb104` | VERIFIED_ORIGINAL |
| Gate Package r10 | `DPT-GATE-012-U01-r10/` | 20247 | `67df94f282f667a66663a12d3106730dd67f0042d504f9ae5f69d07b8b7c9469` | VERIFIED_ORIGINAL |
| README r10 | `DPT-GATE-012-U01-r10/` | 21390 | `25b76e047d8f3658508166bfe600e3e84bd5184924259e1179364beae936498a` | VERIFIED_ORIGINAL |
| r10 review | `DPT-GATE-012-U01-r10-review/` | 74707 | `d2626bb50b56d4aa431a53041a8b08a853dc14dce69b87a6202a9acde3bbb546` | VERIFIED_ORIGINAL |

Earlier revisions, reviews and MISSING items: recovery index §3. Hash matches prove byte identity only, not independent custody. The expected values travelled through the agent channel (no OCD / OPR-2 exists yet). The r12 author must re-hash before use, and must record any mismatch instead of repairing it.

## 3. Mandatory remediation (blocks READY)

The exact required corrections and acceptance criteria are in r11 review §8. This table is a design-level summary; when the two differ, the review text governs.

| Finding | Problem (design level) | Required outcome in r12 | Acceptance evidence to specify |
|---|---|---|---|
| **R11-IR-01** MEDIUM: verifier revocation / replacement freshness | An already-installed verifier stays in use after the Owner revokes or supersedes it, because the only enforcement of that revocation is the revoked verifier itself. The pre-check binds a host to *an* Owner-signed readiness statement, not to the *current, unrevoked* one. | (1) A trusted-tool **currency step** in the verifier pre-check, either by Owner human-to-human conveyance of the current readiness statement hash with each fresh head (the review's preferred option) or by a closed revocation-scan procedure. (2) Mandatory human-to-human notice of every revocation and every new validator acceptance to the affected host operators, with reinstallation. (3) State that self-enforcement inside the verifier is defence in depth only. (4) Hash checks for the interpreter and signing-tool paths in the pre-check, or narrow the claim. | A new procedural row: a revoked or superseded but otherwise matching readiness stops the host **without executing U01 code**, plus a positive control with the current readiness. The next independent review finds no revocation path whose only enforcement is the revoked code. |
| **R11-IR-02** MEDIUM: Owner statement byte construction, canonical validation, `issued_at` controls | Statement bytes in practice come from agent drafts. The Owner verification commands compare decoded values, not exact canonical bytes. `issued_at` has no provenance and no real-time bound, so it can stretch the compiled validity ceilings. A signed non-canonical statement would make the authority chain unusable and force full anchor recovery. | (1) A mandatory **pre-signing canonical-byte gate** on an installed verifier host over the exact statement file, with the result conveyed human-to-human, before any signing; or a reviewed byte-comparing verification script. (2) Envelope provenance rows: `issued_at` from the signing-environment clock within a tight skew, a fresh unique `statement_id`, and constant `schema` / `contract_id` / `contract_revision` / `kind`. (3) A verifier binding rule: `issued_at` is not in the future beyond skew and is non-decreasing. (4) Either a defined byte-producing authoring method, or a normative statement that every statement is an agent draft validated byte-for-byte, with the "compose" wording removed. | New rows: non-canonical draft variants are rejected before signing; a future `issued_at` fails the pre-signing check and the verifier rule; a duplicate `statement_id` fails before signing. "No Owner statement value has an agent record as its source" holds for **every envelope field**. |

## 4. LOW findings: each needs a recorded disposition

For each one, r12 must either **FIX** it or record **ACCEPTED WITH REASONS** for explicit Owner consideration. Silence is not a disposition. The exact text is in r11 review §8.

| Finding | Subject | Required correction (summary) |
|---|---|---|
| R11-IR-03 | The trusted tool set is closed only at the top-level command layer | Pin the signing program; list helper binaries as trusted-tool members; neutralise system Git configuration (credential helper, filters); publish from a non-key-capable context; add an environment-baseline check and its E-fact; restrict the module path; compare the code-signing subject; correct the inaccurate "no module loaded" statement. Must be fixed before E6 can be honestly confirmed. |
| R11-IR-04 | Some verification-command forms can pass without comparing | Strict mode for every verification session; type-and-format guards on every comparison; `--verify` object forms; a parseable input for the allowed-signers check; clarify that the fail-closed claim covers mistyped values, not mistyped paths, unless guarded. |
| R11-IR-05 | Binding-table and verification-order precision | Add "unrevoked" to the two staleness rows; a consumer-after-rollback positive case; bind or explicitly classify every field; move the existence check before the closure check. |
| R11-IR-06 | Gate-order contradiction around verifier installation, pre-flight and readiness | One consistent order across the contract gate order, the Gate Package, the preparation section, the installation procedure and the chain-order row. |
| R11-IR-07 | Owner options can remove mandatory custody and independence requirements | Declining the Owner-custody record makes governance ratification (and therefore validator acceptance) UNAVAILABLE. If the Owner is the sole reviewer, require a second reviewer or an explicit recorded non-independence acknowledgement. |
| R11-IR-08 | Reviewer-environment tooling and scan precision | Define the reviewer tool set with publisher integrity and hashes; specify the exact historical-vector derivation so that two reviewers reproduce it; label reviewer-only assertions; extend the process-function and dynamic-loader negatives. |
| R11-IR-09 | Evidence-accuracy nits | A change-register row for every changed section; source hashes of the bytes as fetched, or the normalisation stated; correct the inaccurate statement. |

**Optional simplifications** (r11 review Q-R12; proposals only, and they must not reopen any finding): run the verification commands as one reviewed, hash-pinned script in a non-key-capable account (this addresses R11-IR-02 and R11-IR-04 together); merge the two readiness statement kinds; optionally fold ratification into acceptance. The review notes that procedural complexity is now a security risk in its own right.

## 5. Frozen requirements r12 must preserve

The r11 review §11 found no weakening in r11. r12 must keep all of the following:
- **r11 bytes stay frozen.** r12 is a new file set with an **r11 → r12 delta register** and no unrelated edits. Changing normative bytes after a review restarts the review.
- U01 scope: one facet, 46 claims. DB boundary: `review_state`, `canonical_selections` and `selection_guard` are untouched; no DB writes, migrations, API/UI, ranking, acquisition or normalization.
- Rights, privacy and reviewer-data rules. The historical vector comes from the authenticated review manifest. The 44 holds, 43 proposals and Khamrah are unchanged.
- Receipts never create approval. Human Merge is workflow, not proof of a decision (PG-1). BatchA and BatchB stay provisional (PG-2). Q-F and Q-H are Owner decisions.
- OP-1 / OP-2 separation; Planning PR / Implementation PR separation; every gate fails closed; reviewer-authentication unavailability cannot be waived by Q-F.
- Independent-review requirements: at least as strong as r11.
- All 147 r10 and all 162 r11 acceptance-specification IDs are retained. A changed or retired ID needs a register row.
- Out of scope for every revision: agent signing, agent key handling, agent preparation of OP-1/OP-2, Production, agent merge.

## 6. Security invariants (must hold in r12 text)

1. **Stated attacker:** any `P_AGENT`, including the author of the verifier source. No requirement may be weakened to reach READY.
2. All **seven trust roots** (Owner identity, reviewer identity, reviewed source, signing environment, verifier environment, authoritative runtime inputs, consumer verification) stay **UNAVAILABLE** until they are established outside the agent account.
3. Agent-authored code never runs in the key-capable principal (TE-1).
4. No authority derives from a GitHub event, comment, merge or chat message (PG-1).
5. **New in r12:** no revocation or supersession path relies only on the revoked code (R11-IR-01).
6. **New in r12:** no signed value, including envelope fields, comes from an agent record without byte-level validation before signing (R11-IR-02).
7. Unavailable or unverifiable states fail closed, and are recorded as UNAVAILABLE / NOT RUN, never as PASS.

## 7. Expected acceptance specifications

- Retain the r11 inventory (162 IDs, 34 groups) and declare every changed and new ID.
- Add rows for each property that the r11 review §9 lists as missing: revoked/superseded readiness under the pre-check (with a positive control); non-canonical drafts, future `issued_at` and duplicate `statement_id`; path-shadowed signing tool, system Git configuration with a credential helper or filter, and an unexpected helper/module path; a mistyped verification path and a nonexistent object ID; a consumer after state rollback; ratification without an Owner-custody record; historical-vector reproduction across two reviewer environments.
- Every row stays **NOT RUN**. The r12 author must not report any row as executed.
- The total r12 count is for the author to declare and the reviewer to reproduce. It is not predicted here.

## 8. Required static validation (r12 author)

- Re-hash every §2 input and record the results.
- A delta register that covers every changed section (R11-IR-09).
- Spec inventory: unique count, groups, duplicates, references to undefined IDs, retention of the r10/r11 IDs, and every result token registered with an oracle.
- Source-reference hashes reproduce from the fetched bytes, or the normalisation is stated.
- A stale-text and contradiction scan, including the R11-IR-06 order check.
- Produce the contract, Gate Package and README r12 in a **new folder outside the repository**. The author does not write to the repository or the vault unless separately authorized.

## 9. Tests explicitly NOT RUN (and not runnable now)

All r11 (162) and future r12 acceptance specifications; any U01 validator or verifier (none exists); OP-1, OP-2, reviewer-environment and consumer-host ceremonies; any signing or key operation; feasibility of the verification commands on the target shells; security-key and stdin parity; ACL feasibility; the run-time budget. The r11 reviewer ran read-only standard-tool behaviour probes only; those are not U01 tests.

## 10. Independent review conditions for r12

- The reviewer must be a **different model family or a human security reviewer**, on a **machine and account that agents do not use** (r11 review §12 item 3).
- The reviewer must not be the r12 author, any r7–r11 author or reviewer session, or the session that prepared this handoff.
- IND-00 provenance comes first; shared authority is disclosed. Inputs are verified against hashes that the Owner provides through a channel other than the agent chat, ideally the Owner-custody record (OPR-2).
- A READY verdict requires **0 open HIGH / 0 open MEDIUM**. Even then, G-IND also needs the Owner's Q-F decision. A review on the authoring account is advisory only.
- If the reviewer is read-only, the report is delivered outside the repository with its hash. A separately authorized documentation session reconciles it into [[DPT-GATE-012_U01_Security_Gate]] without modifying the report.

## 11. Owner decisions still pending (none is given by this note)

Commissioning r12 and its author; the r12 reviewer; Q-F; CONTRACT (exact candidate hash, only after an independent READY); DATA-01, DATA-04, D3/SEQ-01, TASK-ID; Q-A1…Q-A8 (Q-A7 reviewer authentication and whether the Owner may be `P_REV`; Q-A8 OPR-1/2/3 status); Q-B…Q-E, Q-G; the three acknowledgements (R7-IR-08 availability, SHA-1 object identity, pre-OP-1 governance residual); Q-H and BatchA; the U01 Planning PR (W-01); BatchB; OP-1 (E1–E11); OP-2 (F1–F12); OP-2-TOOL; consumer hosts.

**Operational prerequisites that need no contract change** (recommendations only): OPR-1, a separate restricted agent GitHub identity with no merge or bypass rights; OPR-2, an Owner-custody record on a non-agent device holding the expected hashes; OPR-3, backups of r9–r11 and their reviews outside the agent account. The r11 review §10 records that the current authoring host cannot meet the principal-separation conditions in any configuration. Host-level details are omitted here (recovery index §7).

## 12. Completion criteria for the workstream

| State | Evidence required | Current state (2026-11-20) |
|---|---|---|
| DOCUMENTATION_RECOVERY_COMPLETE | Recovery records committed and reviewed in a PR | LOCAL COMMITTED; PR NOT CREATED |
| DOCUMENTATION_MERGED | Owner merge of the recovery PR, verified on GitHub | NO |
| GOVERNANCE_AMENDMENT_MERGED | Owner merge of the DPT-GOV-WORKFLOW-001 PR, verified on GitHub | NO |
| SECURITY_DESIGN_REVIEWED | An independent (G-IND-eligible) READY review with 0 HIGH/MEDIUM, plus Owner Q-F | NO (r11: CONDITIONAL, advisory only) |
| SECURITY_GATE_APPROVED | BatchA with Q-H, the U01 Planning PR merged, and the B1b authenticated design review | NO |
| RUNTIME_SECURITY_TESTED | Executed acceptance specifications with outputs, from an authorized implementation | NO (0 of 162) |
| IMPLEMENTATION_COMPLETE | Gate I with all of the above, implementation review in a reviewer environment, validator acceptance | NO |

Merging documentation never advances any state below DOCUMENTATION_MERGED.

## 13. Publication omissions

Not included here, deliberately: the raw review and contract text, attack walk-throughs, host and account facts, credential details, and local paths. The exact correction wording is available to the r12 author in the r11 review (hash above).
