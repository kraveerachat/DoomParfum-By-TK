---
id: DPT-OPS-004
project: DoomParfum By TK
type: operations
status: acceptance-pending
updated: 2026-11-13
tags: [doomparfum, operations, tools]
source_of_truth: "../../../README.md"
---

# DPT-OPS-004 — Caveman and Context Mode setup

## Session S1 — LOCAL VERIFIED / ACCEPTANCE PENDING

- Owner request: inspect/install JuliusBrussee/caveman and mksglu/context-mode; explain scope across chats and automatic activation.
- Agent: Codex; one agent, no delegation.
- Branch: `codex/caveman-context-mode-setup`; starting/base SHA `aa55f8b59acb0872b3b40273a8cdd25198f3ba27`.
- Separate worktree: `.agent-tools/worktrees/tooling-audit`; root worktree remains PR #8 branch at `3b01c8395d8ce28f426643f104da16090f11844d`.
- Approved application plan: PR #1 governs the existing data pilot, but does not approve new global agent configuration. This is an owner-requested tooling operations/audit task, not application implementation.
- PR: NOT CREATED. Repository changes are documentation only, pending Human Owner review/merge. Global setup scope approval is pending in chat.

## Plan and expected evidence

1. Read repository governance, product/vault conventions, current Git/PRs, tool documentation and installed sources.
2. Inventory existing Caveman skills and Context Mode plugin; distinguish presence, connectivity, hook trust and actual operation.
3. Inspect exact setup side effects. Prepare a dry-run, a bounded configuration plan and rollback before changing global settings.
4. Verify runtime, local SQLite, MCP and hook behavior where authorized; record failures and reload requirements.
5. Record exact paths/versions/hashes, actual mutations and remaining owner action; explain cross-chat scope in Thai.

Do not touch application code/tests, perfume data/database, production, credentials, cloud gateways, model routing, other agents' settings, existing receipts, other worktrees/PRs or the root branch. Do not merge or enable auto-merge.

## Initial observations

- Installed user skill: `~/.codex/skills/caveman/SKILL.md`, SHA256 `415d43518f2b1a9498c15a445d4657117b129ee5e81b19454ce348439cc6672b`; version NOT VERIFIED.
- Context Mode `2.1.8` (doctor ref `92c1ad2`) is installed/enabled under `~/.codex/plugins/cache/context-mode/context-mode/2.1.8`. MCP doctor responds.
- Initial doctor: Node `24.14.0` is below `24.15.0`; all four plugin hooks untrusted. MCP/config/project/database checks pass. Update and legacy-data warnings remain.
- `context-mode setup --dry-run --agents codex --json --no-input` under system Node exits before planning because Node is too old. No setup applied.
- `Agent_Tool_Registry.md` and `Tool_Usage_Log.md`: NOT FOUND at baseline; their initial creation is proposed in this separate docs review.
- A project-local portable Node `24.22.3` has been acquired in ignored `.agent-tools/runtime`, with official archive SHA256 `e612af99f626ab415ea225af6bce5c971feb448cb5cae250bb1c3fa50c5f7d9f`. Archive matches official SHASUMS256; node.exe Authenticode signature valid, OpenJS Foundation. Node version and in-memory SQLite FTS5 smoke succeed. No system installation or permanent PATH mutation.

## Evidence and next action

### Owner authorization and bounded changes

The owner explicitly requested both tools as defaults across local Codex tasks. A later explicit response approved the system-wide Node `24.14.0` to `24.22.3` update, including npm/PATH and no forced reboot. This overrides the initial pending scope above; the historical entry is retained.

- `~/.codex/AGENTS.md`: previously empty; now defaults to the existing Caveman skill and appropriate local Context Mode use. New owner-instruction injection into this chat confirms the file is loaded. No `agent.mt.json` file was created.
- `~/.codex/config.toml`: only four Context Mode hook trust entries added. Setup exit 0; parse/list/MCP/hook registration/execution/skills checks pass. Existing plugin remains `2.1.8`; no duplicate MCP server or global context-mode CLI installation.
- System Node: official signed MSI `node-v24.22.3-x64.msi`, SHA256 `4a1ab5bdec5434bae58efae6c3e5077a011f6f1e76d2b47b7b10af043f7db545`. Admin-elevated installer exit 0; actual system Node `24.22.3`, npm `11.19.1`. Scope: NodeRuntime,npm,EnvironmentPath; no optional build tools or forced reboot.
- Caveman skill bytes already equal v4.1.0 at source commit `1e91f1306d602d4ca23618701b1185575ae1869b`. No reinstall was necessary. Source was acquired under ignored `.agent-tools/external/caveman` for inspection; source acquisition is not a CLI installation. Caveman proxy/model routing/cloud gateway were not installed or configured.

### Failures and exact limits

1. Automatic approval initially rejected the machine-wide Node mutation because the earlier scope covered Codex setup. No rejected command ran. The owner then explicitly approved the exact machine-wide scope.
2. First permitted silent MSI failed: exit 1603, Error 1730 (Administrator required). Existing Node remained `24.14.0`. Same verified MSI via Windows UAC then exited 0.
3. First direct synthetic MCP execution under the filesystem sandbox failed with EPERM creating its normal `~/.context-mode/projects/...` database. Rerun with approved access succeeded: `ctx_execute` JavaScript returned exit 0 and `{"sum":10}`.
4. Direct MCP doctor launched from PowerShell initially reported D11 Git Bash missing despite Git Bash existing. Context Mode 2.1.8 spreads Windows `Path` into an object then reads `PATH`. Normalizing that key only in the test child environment made D11 pass; no Git reinstall, plugin source edit or permanent PATH workaround was applied. The original Codex-hosted doctor had already passed Git Bash detection. This environment caveat remains documented for a future host check.
5. After MSI, the chat's existing MCP tool returned `Transport closed`. Fresh server connections work; the owner must restart Codex and recheck host connectivity. No claim that the old connection recovered automatically.

### Verification

- Official archive/MSI checksum matches and valid OpenJS Foundation Authenticode signatures.
- Portable Node version and in-memory SQLite FTS5 smoke succeeded.
- `node <installed cli.mjs> setup --dry-run --agents codex --json --no-input`: exit 0 under portable Node; plan contains precisely four hook trust additions.
- Same CLI `setup --agents codex --yes --json --no-input`: exit 0; eight setup checks successful (initial hook-seen warning resolved later).
- `node <installed cli.mjs> doctor --agents codex --json --no-input`: exit 0; all eight CLI checks successful, including hook-seen.
- Fresh MCP `tools/list`: nine tools advertised. Fresh `ctx_execute`: successful local synthetic result, no network data or product records.
- Fresh MCP `ctx_doctor` with normalized child PATH: ten PASS rows, D1/D4 WARN, zero FAIL. Warnings: available 2.1.10 update and safe legacy directories/temp files. Kept pinned working 2.1.8 and old files; no unsolicited cleanup/update.
- Caveman SHA256 matches source and installed file. Global default instructions read back and injected into chat.
- Application/database/regression tests NOT RUN: no application change.

Local, ignored evidence lives at root `.agent-tools/tooling-audit/`; raw installer logs and user config backups must not be committed. Evidence SHA256:

| File | SHA256 |
|---|---|
| context-mode-setup-applied.json | 8bb65dedb00e5df45cca0080bdf6385e3888160c54287fda1b412b47e8a224e5 |
| context-mode-final-doctor.json | 65cdf1bdc952f0d39a014b50beeb16f0a250b9bff9e52fbffc87b65701e2b878 |
| context-mode-fresh-mcp-doctor.txt | 02a2b511ca2ff2188129a1f8fd7b14ca731e27d246f1761a812f9b3c8bb3bb41 |
| mcp-smoke-result.json | 41b94d6d0ed71d2ba5ce7fdd1a9411e631607fcf7b7011a339c36942385dc90d |

### Rollback, review and next action

User config backups: `~/.codex/tooling-backups/2026-11-13-DPT-OPS-004/{AGENTS.md.before,config.toml.before}`. Context setup also recorded its own backup at `~/.context-mode/backups/2026-11-12T22-02-17-746Z`.

Restore only this task's four hook trust entries and the prior empty AGENTS content, preserving later unrelated edits; the saved whole-file copies are an audit/reference, not permission to overwrite future changes. No plugin removal is needed to undo the preferences. Node downgrade would be a separate approved system operation with a verified official older installer; do not copy old runtime files over an MSI-managed installation. Ignored source/runtime/evidence may be retained; they are not application dependencies.

Repository documentation changes: this task, [[Agent_Tool_Registry]], [[Tool_Usage_Log]], and append-only operational entries in [[Project_Status]], [[Agent_Run_Log]], [[Change_Log]]. Documentation-only Draft PR publication follows validation. Human Owner alone merges.

Session result: local configuration and fresh-process verification complete; host-reload acceptance remains pending. Restart Codex, run `ctx_doctor`, verify the host sees Caveman defaults and Context Mode tools, and inspect any Git Bash/PATH discrepancy before marking CLOSED. No final immutable receipt yet because host-reload acceptance is pending. No savings claim or production change.

### Publication checkpoint — 2026-11-13

Documentation payload checkpoint `ce4fa34c95f5d76fa6b467979df0c8d9f37f0067` was pushed normally. [Draft PR #12](https://github.com/kraveerachat/DoomParfum-By-TK/pull/12) read back OPEN/DRAFT, base main, exactly six Markdown files. Both worktrees clean at readback; root branch still at `3b01c8395d8ce28f426643f104da16090f11844d`. Publication metadata is added in the next checkpoint on this same branch/PR; resulting HEAD is verified externally rather than self-referenced here.

Local `verify-record.py` confirms the three new notes' required frontmatter/source/wiki links, byte-identical Caveman skill, exact four-entry user config delta, ten PASS/two WARN MCP report and CLI doctor exit 0. Staged and working `git diff --check` succeed. No independent agent review was launched; closeout is documented for Human Owner review. Host restart verification remains the next exact action; PR stays Draft and no final receipt is created.
