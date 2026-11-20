---
id: DPT-GOV-WORKFLOW-001
project: DoomParfum By TK
type: governance
status: acceptance-pending
owner: human-owner
updated: 2026-11-20
tags: [doomparfum, governance, workflow, obsidian, github]
source_of_truth: "../../../README.md"
---

# DPT-GOV-WORKFLOW-001 — Task-to-PR routing and mandatory Obsidian reporting

## Current Task

- Type: PLANNING (docs-only governance amendment)
- Owner / Agent: Human Owner / Claude Code (documentation and governance agent)
- Branch: `plan/agent-workflow-pr-routing`, isolated worktree `.local/worktrees/agent-workflow-pr-routing`
- Base: verified `origin/main` `183f1d857d83b64819762a2237c908fb95e36cb4` (PR31 merge)
- PR / Target branch: **PR_NOT_CREATED** → `main`. The branch is LOCAL_ONLY / NOT_PUSHED, and publication is `AGENT_CREDENTIAL_REQUIRED` (see Blockers and Session S3).
- Current state: ACCEPTANCE PENDING. The agent-side docs checkpoint (S3: dual execution reports and agent publishing identity) is complete. Publication, independent review and Owner merge are pending.
- Production mutation allowed: NO. Application code change: NO.

## Goal / Why

The Owner wants every meaningful agent activity recorded in Obsidian and tied to the correct GitHub PR, so that history, decisions, evidence and task continuity are not lost between sessions and agents.

## In Scope

- `AGENTS.md`: new §2.1 (intake and routing summary) and §8.1 (session records, read-only reviews, public evidence, publication).
- `DEVELOPMENT_WORKFLOW.md`: new §3.6, §5.6, §5.7 and §6.2.1; extensions to §4.3, §4.4 and §4.5; frontmatter version 1.1.0.
- This note, plus dated entries in Agent_Run_Log, Change_Log, Decision_Log, Project_Status and Project_Index.
- S3 (Owner directive, 2026-11-20): dual execution reports (DW §4.7 new; §4.4, §4.5 and the §1 tree; vault README tree; AGENTS §8.1), the agent/Owner responsibility split, and the agent publishing identity (DW §5.6; AGENTS §8.1), plus this task's first execution report under `08_Operations/Reports/DPT-GOV-WORKFLOW-001/`.

## Out of Scope

- Application source, tests, migrations, data and configuration.
- Any change to the DPT-DOC-RECOVERY-001 branch or its PR scope.
- Any DPT-GATE-012 approval (Q-F, Q-H, BatchA), U01 implementation, or security runtime tests.
- Fixing the pre-existing documentation-check baseline errors in unrelated notes.

## Existing-rule audit (before this change)

| Topic | Already defined | Where |
|---|---|---|
| One task → one branch → one PR → one receipt; sub-sessions stay on the same branch/PR | Yes | AGENTS §2; DW §0 rule 1, §3.1 |
| Planning PR before implementation; Planning Amendment PR for scope change | Yes | AGENTS §2; DW §3.2–§3.4 |
| Defect fixes stay in the same PR | Yes (implementation review only) | DW §3.3 step 8, §3.4 |
| Obsidian update before/after a meaningful session | Yes | AGENTS §2; DW §0 rule 4, §4.5 |
| Meaningful session definition | Partly: code, schema, data, UI, security/config, integration tests, defect fixes | DW §4.3 |
| Session record template | Partly: no agent/role, PR reference, decisions, tests not run, security/privacy | DW §4.4 |
| Change_Log / Agent_Run_Log entry per meaningful session | Yes | DW §7.2 |
| Handoff / continuity pack | Yes | AGENTS §8; DW §10 |
| Report `PR_NOT_CREATED` when Git is unavailable | Planning-agent prompt only | DW §9.1 |
| Never claim push/PR without verification | Yes | AGENTS §3 |
| No credentials in commits | Yes | AGENTS §2; DW §5.2 |

## Gap analysis (why the existing wording was insufficient)

1. **No intake step.** Nothing required an agent to classify a new prompt as a continuation, a new task, a scope change, or a read-only review *before* creating a branch or PR. The rules said what one task looks like, not how to decide which task a prompt belongs to.
2. **PR reuse was implicit.** "Sub-sessions remain on the same branch/PR" did not say that a cleared context, a new review revision, new findings, or another test run must not create a new PR. It also did not say when same-initiative work must *not* reuse a PR (a separate gate or phase).
3. **PR existence was not tied to GitHub evidence.** A local branch or a drafted PR body could be mistaken for a PR.
4. **Activity coverage was incomplete.** §4.3 omitted planning, documentation, independent/security reviews, findings remediation, handoffs, infrastructure operations and final reports.
5. **Session fields were incomplete.** §4.4 lacked agent/role, PR reference, decisions made, tests not executed, security/privacy implications and current status.
6. **No read-only reviewer exception.** The "update Obsidian every meaningful session" rule conflicted with reviewers who are forbidden to write. There was no rule for later reconciliation or for keeping review states distinct from Owner approval.
7. **No public-repository evidence rule.** The rules covered secrets in commits, not sanitized summaries, hashes, private retention, or the limit of hash matching.
8. **No credential boundary or blocked-publication rule.** Nothing said that an available credential is not authorization, or how to report and hand off a blocked push.

## Exact governance changes

| File | Section | Change |
|---|---|---|
| `AGENTS.md` | §2.1 (new) | Intake steps 1–4, classes A–D, no-new-PR and no-reuse rules, duplicate/unrelated PR ban; points to DW §3.6 as the full procedure |
| `AGENTS.md` | §8.1 (new) | Mandatory Obsidian record; read-only review exception; public-repository evidence; publication and credential boundary |
| `DEVELOPMENT_WORKFLOW.md` | frontmatter | `version` 1.0.0 → 1.1.0, `updated` → 2026-11-20 |
| `DEVELOPMENT_WORKFLOW.md` | §3.6 (new) | Full intake procedure, routing table, Gate P preservation, DPT-GATE-012 example |
| `DEVELOPMENT_WORKFLOW.md` | §4.3 | Adds the activity types that count as meaningful sessions |
| `DEVELOPMENT_WORKFLOW.md` | §4.4 | Adds required session fields; one canonical note and one receipt per task |
| `DEVELOPMENT_WORKFLOW.md` | §4.5 | Table of required record locations |
| `DEVELOPMENT_WORKFLOW.md` | §5.6 (new) | 10-step checkpoint publication, credential boundary, blocked-publication reporting |
| `DEVELOPMENT_WORKFLOW.md` | §5.7 (new) | Public-repository evidence handling |
| `DEVELOPMENT_WORKFLOW.md` | §6.2.1 (new) | Read-only independent review exception and distinct review states |
| `DEVELOPMENT_WORKFLOW.md` | §4.7 (new, S3) | Dual execution reports: private and vault copies, file naming, never-overwrite rule, SHA-256 parity for public-safe reports, sanitized copies for sensitive ones, a Reports index in the task note, prospective only |
| `DEVELOPMENT_WORKFLOW.md` | §1 tree, §4.4, §4.5 (S3) | `08_Operations/Reports/<TOPIC_ID>/` added to the tree and the location table; new §4.4 field "Execution report" |
| `DEVELOPMENT_WORKFLOW.md` | §5.6 (S3) | Responsibility split (agent publishes, Owner reviews and merges); publishing is not approval; agent publishing identity requirements; `AGENT_CREDENTIAL_REQUIRED`; Owner-run publication reworded as an exception |
| `AGENTS.md` | §8.1 (S3) | New "Dual execution report" bullet; the publication bullet now states the responsibility split and points to the agent identity in DW §5.6 |
| `Structure DB Obsidian/README.md` | folder tree (S3) | `Reports/<TOPIC_ID>/` line |

No existing accepted sentence was deleted or reworded. S3 rewords only two sentences that this unmerged PR added in S1 (the "give the Owner the exact next commands" fallback in AGENTS §8.1 and DW §5.6). The Owner directive of 2026-11-20 makes Owner-run publication an exception, not the normal path. AGENTS.md states each new rule briefly and defers to DEVELOPMENT_WORKFLOW.md for detail, so the two files cannot diverge on substance.

**Noted but not changed (out of scope):** DW §1.2 still describes `AGENTS.md` as "to be created", and DW §3.1/§5.1 list `feat/`, `fix/` and `data/` prefixes while the repository also uses `impl/` and `codex/`. Both are pre-existing inconsistencies to handle separately.

## Acceptance Criteria + Evidence Needed

- [x] Both governance files define the intake procedure, classes A–D and routing, without contradiction.
- [x] The Two-Gate workflow and the Planning/Implementation PR separation are preserved.
- [x] Existing-task PR reuse and new-task PR creation rules are explicit.
- [x] The read-only review exception and the distinct review states are explicit.
- [x] Mandatory Obsidian reporting fields and locations are explicit.
- [x] Public-repository rules are preserved and extended; only the Human Owner merges.
- [x] No application files changed; no secrets committed (see the Test / Evidence Ledger).
- [x] S3: dual execution-report rule and agent publishing identity are defined, additively, without duplicating existing rules.
- [ ] Draft Planning PR published (blocked: `AGENT_CREDENTIAL_REQUIRED`).
- [ ] Independent review of the amendment.
- [ ] Human Owner review and merge.

## DPT-DOC-RECOVERY-001 status (verified in S1, read-only)

| Fact | Verified value |
|---|---|
| Worktree | `.local/worktrees/dpt-gate-012-security-history`, clean |
| Branch | `docs/dpt-gate-012-security-history` |
| Commit | `987279a98cf1a48ee657f0b9f4f78581063c9e01`, single parent `183f1d857d83b64819762a2237c908fb95e36cb4` = current `origin/main` |
| Files | Exactly the 7 documented vault paths (2 new notes; Agent_Run_Log, Change_Log, Decision_Log, Project_Status, Project_Index); `git diff --check` clean |
| Remote branch | NOT PUSHED (`git ls-remote` returns nothing) |
| GitHub PR | NONE (no open, closed or merged PR for this branch) |
| Conflicts with main | None; the branch is one commit ahead of current `origin/main` |

This task did not modify the recovery branch. The two branches append to the same five shared notes. Whichever PR merges second will need a trivial append-only conflict resolution that keeps both sections.

## Session Register

| Session | Purpose | State | Result | Checkpoint SHA | Evidence |
|---|---|---|---|---|---|
| S1 | Audit, amend governance, record, local checkpoint | CLOSED | PARTIAL (publication BLOCKED) | `2903c96537c5eca2c68568b3911a899235b38aea` | Ledger below |
| S2 | Publication-readiness re-verification, integration simulation, sanitization correction | CLOSED | PARTIAL (publication BLOCKED) | `cdb6ff8031b0e7fabfb6ba5c6c8fae3efafe4d46` | Session S2 below |
| S3 | Owner directive: dual execution reports, agent-managed publication, agent identity | CLOSED | PARTIAL (publication BLOCKED: `AGENT_CREDENTIAL_REQUIRED`) | S3 checkpoint commit | Session S3 below; Reports index |

## Reports

Execution reports for this task (DW §4.7). S1 and S2 predate the rule and have no separate report; their records are the session sections below.

| File | Session | SHA-256 | Kind |
|---|---|---|---|
| `08_Operations/Reports/DPT-GOV-WORKFLOW-001/2026-11-20_DPT-GOV-WORKFLOW-001_S3_Report.md` | S3 | `fe14722af37ed02b71c014fa9fc0ae15f6cce505ddfd7aed14cbc8869f552cad` | public-safe; identical private copy in `Downloads\DPT-GOV-WORKFLOW-001\Responses\` |

### Session S1 — governance amendment and recovery status check

- State: CLOSED (local checkpoint)
- Task ID / Session ID: DPT-GOV-WORKFLOW-001 / S1, Claude Code session `33a50b45`
- Agent / Role: Claude Code, documentation and governance agent. It is not an independent reviewer of this change.
- Date: 2026-11-20
- Intake class: B (new reviewable docs-only governance task). Kept separate from DPT-DOC-RECOVERY-001 on Owner instruction.
- Applicable plan: Owner prompt DPT-GOV-WORKFLOW-001 under existing AGENTS.md / DEVELOPMENT_WORKFLOW.md governance
- Branch / PR: `plan/agent-workflow-pr-routing` / PR_NOT_CREATED
- Starting SHA: `183f1d857d83b64819762a2237c908fb95e36cb4`

**Work performed:** read the governance and vault files listed in the Owner prompt; fetched origin; verified branches, worktrees, PRs (only PR8 is open) and repository visibility (PUBLIC); verified the recovery branch as above; created this isolated worktree from `origin/main`; made the governance amendment and these vault records.

**Exact files changed:** `AGENTS.md`; `DEVELOPMENT_WORKFLOW.md`; `Structure DB Obsidian/07_Delivery/Tasks/DPT-GOV-WORKFLOW-001_Task_PR_Routing_and_Obsidian_Reporting.md` (new); `Structure DB Obsidian/08_Operations/Agent_Run_Log.md`; `Change_Log.md`; `Decision_Log.md`; `Structure DB Obsidian/00_Home/Project_Status.md`; `Project_Index.md`.

**Decisions made:** the agent proposed the governance text only. There are no Owner decisions; the amendment takes effect only when the Owner merges it.

**Findings:** see the gap analysis. The pre-existing documentation-check baseline is recorded below.

**Security / privacy:** the repository is PUBLIC. No credentials, tokens, private keys, e-mail addresses, absolute user paths or exploit details are in the change. The Owner's own broad-scope `gh` login was used only for read-only queries (visibility, PR list). Its scope details are omitted under the publication policy of the DPT-GATE-012 recovery index §7, which is on branch `docs/dpt-gate-012-security-history` (corrected in S2). It was not used to push or to create a PR.

**Tests not executed:** independent review; Markdown rendering; external URL checks; any runtime, database or security test (not applicable to a docs-only change).

**Remaining work / next action:** Owner publication (commands in the session final report), an independent review of the amendment, then Owner review and merge. No final receipt yet: the task is ACCEPTANCE PENDING (DW §4.6).

## Test / Evidence Ledger

All checks ran locally on 2026-11-20, on the S1 working tree before commit.

| Check | Result |
|---|---|
| `python database/validate_docs.py --task IMP-P1-02` | **PRE-EXISTING FAILURE.** Exit 1, 52 errors, all `unresolved wiki` links to `.json` evidence files in the five shared notes (Index 5, Status 11, Agent_Run_Log 14, Change_Log 14, Decision_Log 8). All 52 targets already occur in the `origin/main` versions of those files; **0 introduced**. 8 Markdown files checked, 6 frontmatters parsed (including this note), logical-table parity 47, Owner-decision rows 6 unchanged, secret-pattern candidates 0, historical evidence/migrations/receipts unchanged. The checker writes its JSON only on zero errors, so no tracked file changed. The count equals the 52 recorded by DPT-DOC-RECOVERY-001, re-measured here rather than assumed. |
| Wiki links in added text | PASS. 5 occurrences, all to this note, which exists |
| Section cross-references in the new text (AGENTS ↔ DW) | PASS. Every cited § exists |
| `git diff --check` | PASS |
| Secret / private-data scan of added lines and this note (e-mail, absolute user paths, token and key patterns, password/cookie/Bearer) | PASS. 0 matches |
| Scope (`git status`) | PASS. Exactly the 8 intended paths; no application, database, test or config file |
| Markdown rendering, external URLs | NOT RUN |
| Independent review | NOT RUN (pending) |
| Runtime / DB / security tests | NOT APPLICABLE (docs-only) |
| **S2** `validate_docs.py --task IMP-P1-02` (re-run, not assumed) | **PRE-EXISTING FAILURE.** Exit 1, 52 errors (Agent_Run_Log 14, Change_Log 14, Status 11, Decision_Log 8, Index 5), each target present on `origin/main`; **0 introduced**; secret candidates 0; historical evidence/receipts unchanged |
| **S2** `git diff --check` | PASS |
| **S2** Integration simulation `git merge-tree` with `987279a` | CONFLICT ×5 (expected, append-only; resolution recorded in S2) |
| **S2** Sensitive-fact re-scan of S1 diff | 1 LOW finding (S2-F1), corrected |
| **S3** `validate_docs.py --task IMP-P1-02` (before the report was added) | **PRE_EXISTING.** Exit 1, 52 `unresolved wiki` errors, same per-file split, every target on `origin/main`; **0 introduced**; secret candidates 0 |
| **S3** `validate_docs.py` (with the report and private-copy hash) | **PRE_EXISTING.** Exit 1, 52 errors, every target on `origin/main`; **0 introduced**; 10 Markdown files, 8 frontmatters (the report included), table parity 47, Owner decisions unchanged 6, secret candidates 0, historical evidence and receipts unchanged |
| **S3** `git diff --check` | PASS |
| **S3** Sensitive-data scan of added lines | PASS, 0 matches |
| **S3** Wiki links in added lines | PASS |
| **S3** Report private copy and vault copy SHA-256 | PASS. Both copies `fe14722af37ed02b71c014fa9fc0ae15f6cce505ddfd7aed14cbc8869f552cad`, LF, written without overwriting (the target folders did not exist) |
| **S3** Integration simulation (`git merge-tree`, S3 trees of both branches) | CONFLICT ×5 (expected): the same 5 shared notes, 1 insertion-vs-insertion hunk each, run on temporary commit objects; no branch or index changed |
| **S3** Push / Draft PR | BLOCKED (`AGENT_CREDENTIAL_REQUIRED`) |

## Issues / Risks / Known Limitations

- **Blocker, publication:** GITHUB_CREDENTIAL_BOUNDARY_BLOCKED, reported from S3 as `AGENT_CREDENTIAL_REQUIRED`. The only available credential is the Owner's broad-scope login, so the branch is LOCAL_ONLY / NOT_PUSHED / PR_NOT_CREATED. Prerequisite: the agent publishing identity in DW §5.6.
- Self-authored governance text has had no independent review yet.
- The append-order conflict with the recovery branch is expected and trivial (see above).

### Session S2 — publication readiness and integration check

- State: CLOSED (local checkpoint)
- Task ID / Session ID: DPT-GOV-WORKFLOW-001 / S2, Claude Code session `33a50b45` (same session as S1, after the Owner's continuation prompt DPT-GATE-012-U01-CONTINUATION)
- Agent / Role: Claude Code, documentation and governance agent; author of S1, so this is a self-check and not an independent review
- Date: 2026-11-20
- Intake class: A (continuation of this task; same branch, same future PR)
- Branch / PR: `plan/agent-workflow-pr-routing` / PR_NOT_CREATED (verified on GitHub: no PR for this head)
- Starting SHA: `2903c96537c5eca2c68568b3911a899235b38aea`

**Work performed:**
1. Re-fetched origin: `origin/main` is still `183f1d857d83b64819762a2237c908fb95e36cb4`, and the branch is 1 ahead / 0 behind. The remote branch does not exist. The only open PR is PR8. The credential situation is unchanged (only the Owner's own broad-scope login, through the system credential manager), so the branch is still LOCAL_COMMITTED / NOT_PUSHED / PR_NOT_CREATED / OWNER_ACTION_REQUIRED.
2. Re-checked S1 integrity. The diff is docs-only (8 paths). The only deletions are 7 metadata lines plus 3 renamed §4.4 template fields, and each rename keeps the original field text (`Started:` → `Started (date):`, `Branch:` → `Branch / PR (verified state):`, `Defects discovered / Fixes applied` → `Findings / Defects discovered / Fixes applied`). No accepted rule was removed.
3. **Correction (finding S2-F1, LOW, self-found):** the S1 security line listed the login's credential scopes. That is not a secret, but the DPT-GATE-012 recovery publication policy treats credential scopes as environment facts to omit. S2 replaces them with "broad-scope". The S1 commit itself is kept; the correction is a new commit, not a rewrite.
4. Ran an integration simulation with `git merge-tree --write-tree --merge-base=origin/main 987279a 2903c96`. Result: content conflicts in exactly the 5 shared notes (Project_Index, Project_Status, Agent_Run_Log, Change_Log, Decision_Log), one hunk each. Every hunk is an insertion against an insertion at the same position; the frontmatter `updated:` lines merge cleanly. Resolution: keep both sections. Put the recovery (DPT-GATE-012) section first and the DPT-GOV-WORKFLOW-001 section second in the logs and Index (chronological), and in Project_Status keep both sections at the top with the later-merged task's section above. Delete nothing. No merge was committed: per the Owner's instruction, reconciliation happens after the first PR is merged.

**Exact files changed:** this note; `Structure DB Obsidian/08_Operations/Agent_Run_Log.md`.

**Decisions made:** none. **Tests:** see the S2 rows of the ledger. **Not executed:** independent review (still required); Markdown rendering.

**Security / privacy:** S2-F1 corrected. No other environment facts are in the change.

**Remaining / next action:** Owner publication; independent review; after the first of the two PRs merges, a class-A session on the second branch merges the updated `main` (no rebase, no force-push) using the resolution above.

### Session S3 — dual execution reports and agent-managed publication

- State: CLOSED (local checkpoint)
- Task ID / Session ID: DPT-GOV-WORKFLOW-001 / S3, Claude Code session `33a50b45` (same session as S1/S2; not independent)
- Started (date): 2026-11-20
- Intake class: A
- Applicable plan: this Planning PR's scope, extended by the Owner directive of 2026-11-20 (agent-managed publication; dual Markdown reports)
- Branch / PR (verified state): `plan/agent-workflow-pr-routing`, 2 ahead / 0 behind `origin/main` `183f1d857d83b64819762a2237c908fb95e36cb4`; remote branch absent; no PR
- Starting SHA: `cdb6ff8031b0e7fabfb6ba5c6c8fae3efafe4d46`

**Work performed:** checked existing governance for the dual-report requirement. Session records, receipts, read-only reviewer reports and sanitized public summaries were already covered. These were missing:
- a per-session execution report
- the private and vault copy pair
- SHA-256 parity
- the never-overwrite rule
- the report index

Added DW §4.7 and the references to it, and extended DW §5.6 and AGENTS §8.1 (see "Exact governance changes"). Wrote this task's first execution report and its private copy.

**Publication: `AGENT_CREDENTIAL_REQUIRED`.** The only GitHub login is the Owner's own broad-scope account. Three things forbid using it for an agent push:
- the Owner's standing instruction for this workstream ("Do not use the shared broad-scope Owner credential from the agent session")
- the directive's own requirement for "an appropriately authorized agent identity"
- this PR's credential boundary

No push or `gh pr create` was attempted. The least-privilege prerequisite is now in DW §5.6 and in the S3 report.

**Exact files changed:** `AGENTS.md`; `DEVELOPMENT_WORKFLOW.md`; `Structure DB Obsidian/README.md`; this note; `00_Home/Project_Status.md`; `08_Operations/Agent_Run_Log.md`, `Change_Log.md`, `Decision_Log.md`; `08_Operations/Reports/DPT-GOV-WORKFLOW-001/2026-11-20_DPT-GOV-WORKFLOW-001_S3_Report.md` (new).

**Decisions made:** the Owner directive is recorded; the rules it implies are proposed text, effective on merge. The identity choice (GitHub App or machine user) is open for the Owner.

**Findings:** none new. **Tests:** see the S3 ledger rows. **Not executed:** independent review; Markdown rendering; push and PR creation (blocked).

**Security / privacy:** the identity requirements name permission categories only. They contain no token, scope listing of the Owner login, or host facts.

**Execution report:** see Reports above.

## Latest Git Checkpoint / SHA

S1: `2903c96537c5eca2c68568b3911a899235b38aea`. S2: `cdb6ff8031b0e7fabfb6ba5c6c8fae3efafe4d46`. S3: the commit that adds this text (a commit cannot contain its own SHA; the next session records it).

## Handoff / Next Action

1. Owner: provision the agent publishing identity (DW §5.6), or explicitly authorize a one-time use of the Owner login. Then a class-A agent session pushes and opens the Draft Planning PR.
2. Independent reviewer: review AGENTS.md §2.1/§8.1 and DW §3.6/§4.3–§4.5/§5.6/§5.7/§6.2.1 for clarity and contradiction.
3. Next session (class A): record the actual PR number/URL and the S1 checkpoint SHA here, and apply any review corrections on the same branch/PR.
