---
id: DPT-OPS-TOOLS-002
project: DoomParfum By TK
type: tool_usage_log
status: proposed
updated: 2026-11-13
tags: [doomparfum, operations, tools]
source_of_truth: "../../README.md"
---

# Tool Usage Log

## 2026-11-13 — DPT-OPS-004 user-level defaults and Context Mode repair

Owner requested Caveman/Context Mode installation and explanation of cross-chat effects. Inventory found the Caveman skill and Context Mode 2.1.8 already installed. Caveman bytes match the pinned v4.1.0 source; no duplicate installation. Context Mode initially had Node 24.14.0 below minimum and four untrusted hooks.

After explicit owner scope approval, wrote default-use instructions to previously empty `~/.codex/AGENTS.md` and used the inspected Context Mode CLI to add precisely four trust entries to `~/.codex/config.toml`. Backups: `~/.codex/tooling-backups/2026-11-13-DPT-OPS-004`, plus Context Mode's own timestamped backup. All backup bytes remain outside Git.

Automatic review rejected the initial system MSI action until the owner explicitly approved machine-wide Node/npm/PATH mutation. Silent MSI then failed with Administrator-required Error 1730/exit 1603. Same checksum/signature-verified MSI via UAC exited 0; actual system Node 24.22.3 and npm 11.19.1 verified. No forced reboot or optional build tools.

Project-local acquisitions: official portable Node archive/runtime and MSI under ignored `.agent-tools/runtime`; pinned Caveman source under ignored `.agent-tools/external/caveman`; diagnostic scripts/reports in ignored `.agent-tools/tooling-audit`. This source clone is not a Caveman CLI installation. No npm install/npx/bootstrap script, account login, paid actor, gateway or model routing used.

Evidence: SQLite FTS5 smoke, successful setup/CLI doctor, MCP tools/list and real local synthetic ctx_execute. Fresh MCP doctor: ten PASS, two WARN after process-only PATH-key normalization. Initial standalone EPERM and Windows Path/PATH casing failures were diagnosed and recorded. Existing chat MCP transport closed after MSI: Codex restart and host recheck remain pending.

Rollback: restore only this task's AGENTS preference and four hook trust entries, comparing backups against current files to preserve later edits. Any MSI-managed Node downgrade needs separate authorization and a verified official installer. Keep safe legacy files; no unsolicited cleanup. Detailed exact hashes/paths/results and next action: [[DPT-OPS-004_Agent_Tooling_Setup]]. Inventory: [[Agent_Tool_Registry]].

Session result: local setup verified; host-reload acceptance pending. Documentation-only review branch `codex/caveman-context-mode-setup`, base `aa55f8b59acb0872b3b40273a8cdd25198f3ba27`; PR publication pending at authoring. Root PR #8 branch/source and all other workstreams preserved. Human Owner alone merges; no final task receipt while host-reload acceptance remains pending.

Publication readback: payload `ce4fa34c95f5d76fa6b467979df0c8d9f37f0067` pushed; [PR #12](https://github.com/kraveerachat/DoomParfum-By-TK/pull/12) OPEN/DRAFT with exactly six Markdown files. Same-branch publication-metadata checkpoint follows. Both worktrees were clean and root HEAD unchanged at readback. No merge or host-restart completion claimed.
