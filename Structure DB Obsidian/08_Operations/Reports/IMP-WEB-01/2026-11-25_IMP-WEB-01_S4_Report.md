---
id: IMP-WEB-01-S4-REPORT
project: DoomParfum By TK
type: execution_report
status: acceptance-pending
owner: human-owner
updated: 2026-11-25
tags: [doomparfum, frontend, docker, records-only, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-01 S4 — preview recovery and PR36 records reconciliation

PUBLIC_SAFE. Agent: Codex coordinator, intake A, continuation of [[IMP-WEB-01_Luxury_Frontend_Docker]], not a new task or Planning PR. Starting published HEAD `cda91ff7ba00a44d5b8be53a2dbff68553c6736c`; branch `feat/imp-web-01-luxury-frontend`; fetched main `61932bef147816272a06cbe6eba9363940fa4baf`. [PR36](https://github.com/kraveerachat/DoomParfum-By-TK/pull/36) is OPEN/DRAFT. Reviewed application `449178093ed7616570cf651f8b5e4f3cc2d3001e`; complete published/reviewed web tree `2cf8c4f5b384605d0239301e5888318923f6d627`. No application source change.

## Scope, plan and authorization

Owner explicitly permits bounded existing Docker Desktop/local frontend recovery; six HTTP smoke requests and browser availability; existing task/status/index/log reconciliation; one local records-only commit, one normal push to this existing branch and one corresponding PR-description update. No approved agent publishing identity is configured; the existing Owner authentication is explicitly permitted for this specified update only. No credential is printed/published. Earlier publication permission used for cda91ff was exhausted. The new records-only exception likewise expires immediately on completion.

No redesign/source/DB/migration/Production/PR8/U01/matching/ETL change, force push, new PR, merge or final receipt. Protected containers/volumes and S2 rollback must stay intact. Report/summary cannot include their own containing SHA; actual new local/remote HEAD and publication completion/exhaustion are verified in the PR description/final delivery. This prepared record alone is not proof that its push succeeded.

## Recovery: executed commands, outcome and failures

Docker CLI28.3.2, desktop-linux. Initial sandbox named-pipe denial was followed by host probes: Desktop status stopped, engine calls timed out. Supported `docker desktop start --detach --timeout45` reported already running despite unavailable engine. One supported `docker desktop restart --timeout60` completed; version probe returned28.3.2. No factory reset/reinstall/network modification/unrelated service restart.

Verified S3 image `sha256:43be51f1cf209ac0a9c4f25960b91e153826d0b4db1c00f688466a6bf30598a6` exists, tagged doomparfum-web:preview. Existing doomparfum-web container `69d92c019079784d63dd2fd72535a49b19b8d5deeac80766b146ff527a81cd6b` had this exact image and `127.0.0.1:3000:3000` binding; no listener occupied3000. `docker start doomparfum-web` restored it without rebuild/recreation. Running/healthy, user node, read-only root, cap_drop ALL, no-new-privileges, no mounts. Leave it running at [preview](http://127.0.0.1:3000/).

| GET | Actual result |
|---|---|
| / | 200 HTML |
| /explore | 200 HTML |
| /perfume/paper-study-b | 200 HTML |
| /notes | 200 HTML |
| /about | 200 HTML |
| /perfume/imp-web-01-unknown-recovery | 404 HTML |

All six case-insensitive header checks observed no-store, noindex/nofollow, nosniff and CSP. An initial checker converted HTTP headers into a case-sensitive dict and falsely printed null for lowercase names; corrected before recording outcomes, no source fix. This is six-response smoke coverage, not universal header acceptance.

CUA in-app browser rendered Home, synthetic disclaimer, title and catalogue link; screenshot observed and preview tab retained. Browser availability only, not A05/accessibility/visual acceptance. Full85unit/189Chrome/189Edge historical S3 suites NOT RERUN. Engine probes, not application regressions, caused the environmental failures above.

## Protected resources

After engine recovery/before frontend start, all four protected/unrelated containers were Exited; after smoke they still were: doomparfum-p1-01, doomparfum-p1-04-restore, existing doomparfum-p104-temporal-* and eleuthex-hermes. No start/stop/delete/rename command targeted them. Historical start/finish timestamps did not advance. Their complete inspect-metadata fingerprint matched `22b04869163a45f975ab022d80e8083c64b7089d80818d98e7e41ebb0e846b7d` before/after frontend start.

All32volume metadata/inventory fingerprint matched `66684538904bc5917c2b8fac7f1561fbb7aa8450c6900b67ae8fb81c6422741f`. S2 rollback image unchanged: `sha256:1c60def43c74af4657d419f6c927653fca9e7b56e2f7ba44485b3cc293309c50`. No prune, volume removal/consolidation, DB connection or contents read.

Limit: first engine-readable snapshot was after Desktop recovery; no pre-recovery inspect snapshot was available. Evidence proves protected state/configuration/inventory preservation across frontend startup plus historical stopped timestamps, not a DB-content/backup integrity re-test. No raw inspect dump, environment values, mount/host paths or credentials are published.

## Decisions, review coverage and acceptance

Actual PR36 at published cda91ff records Owner decisions1–10 ACCEPTED only within current local mock, and Decision11 explicitly defers unavailable A05 manual checks. Exact11-row decision table is reconciled in canonical task/Decision Log. Header/redirect exceptions are accepted only for loopback synthetic preview; reassess before any public deployment. No production/real-data acceptance.

A05 remains PARTIAL; screen readers, physical phones, Safari and Firefox NOT RUN. A10 second-machine LAN probe remains NOT RUN. A bounded Home rendering does not fill those gaps or prove WCAG conformance.

LF-05: CONDITIONAL on S2, SHA256 `37852101f9ed8a0b9b4defab2c6d7fd6df0fd4aadc113e1282278a9fc6ade290`. S3: CONDITIONAL at32574e8 then focused delta-only code PASS at4491780, SHA256 `91c59dcc1e786d13977e00b913bcc54b6d2c1d99f8851497fee9a9eb06667f9c`. Both were same-vendor subagents commissioned by implementer, not human/cross-vendor/authenticated independent acceptance. S3 reviewer did not cover visuals, axe, npm ci, Docker build,A10,A11. S4 does not broaden that review. Historical originals/hashes/custody statements are preserved, not reverified or moved.

## Records and verification

Changed files: existing task, Project_Status, Project_Index, Backlog, Decision_Log, Agent_Run_Log, Change_Log, Tool_Usage_Log; additive S4 report, summary and recovery evidence JSON. All under Structure DB Obsidian. S1/S2/S3 reports/summaries/evidence, plans, migrations/receipts and complete web tree remain untouched. Current sections supersede stale NOT_CREATED/Owner-PENDING statements without rewriting dated history.

Applicable checks: Git reviewed/published/working web-tree and exact byte parity, old protected Git blobs, scoped Markdown/frontmatter/internal links, sensitive-content scan, git diff --check, records-only diff allowlist. Actual results are recorded in the canonical S4 ledger and final delivery. Stock database/validate_docs.py is not claimed clean: S3 recorded binary-file failure and Tool_Usage_Log's pre-existing missing-owner field remain; scoped checks do not rewrite historical evidence or validator.

Public-safe evidence: [S4 Recovery JSON](../../Test_Evidence/IMP-WEB-01/S4/IMP-WEB-01_S4_Recovery.json). No new sensitive full report/private vault artifact is generated.

## TOOL EXECUTION REPORT / handoff

Used installed Caveman/Context Mode, PowerShell/Python, Git/gh read/fetch and authorized records publication, Docker supported Desktop/inspect/start controls, CUA in-app browser. No install/plugin/global-config change. Initial obsolete computer-use skill path NOT FOUND; current installed skill located/read. Native Windows UI was unnecessary. Creating the additive S4 directory required authorized host access; no unrelated directory was touched.

NOT RUN: full unit/browser/accessibility/DB/matching/ETL/U01 suites, second-machine LAN, Ubuntu, human/cross-vendor review. No Owner final acceptance, receipt, merge, deployment or Production mutation. Exact new containing SHA and publication exhaustion are delivered externally after verifying the one normal push and PR update. Next: Human Owner visual review and explicit final acceptance of local mock scope/limitations.

## Actual S4 verification ledger before publication

PASS: all97tracked web files compared byte-for-byte to reviewed4491780, zero mismatches; published/HEAD/reviewed tree2cf8c4f5 equal. Scoped documentation:11exact allowed vault paths,10Markdown/frontmatters,4relative links,684wikilinks,0errors,0sensitive-content candidates. One pre-existing warning: Tool_Usage_Log owner field missing. Stock validator NOT RERUN because its recorded branch binary-file failure remains; no clean stock result claimed. Git diff --check passes;146old protected database/matching/receipt/S1–S3 evidence/report paths unchanged. No test/acceptance/source files are edited.

Initial diff --check failed on four newly added trailing spaces; removed only those spaces. A link-checker draft incorrectly indexed Markdown only and flagged existing JSON wikilinks; corrected its file inventory without modifying those historical links. Both initial checker failures and the earlier case-sensitive header lookup are retained here, not reclassified as application defects. Final checks are repeated on the staged records before the one commit; final local/remote SHA and PR state are verified after the one publication update.

The first staged diff check additionally caught an extra blank EOF line in the three new S4 files; removed before commit. Earlier unstaged diff did not include those then-untracked files. No commit/push occurred on that failed staging check. Final staged validation is required and rerun; this failure is preserved rather than hidden.
