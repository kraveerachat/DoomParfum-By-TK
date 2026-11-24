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

## Post-PR13–17 verified integration — 2026-11-13

New health check: ContextMode2.1.10(877eebc),Nodev24.22.1,doctor11PASS/1WARN/0FAIL;
SYNTHETIC_POST_PR13_17_SMOKE_OK passed. Caveman installed guidance read/applied. No installation,
upgrade,hook/config/account/service change. Host restart not verified; gatePARTIAL. Old temp/data
warning is retained safely, not cleaned. Full observation/evidence:[[DPT-DOC-002_Post_PR13_17_Preflight]].


## 2026-11-13 — DPT-OPS-004 user-level defaults and Context Mode repair

Owner requested Caveman/Context Mode installation and explanation of cross-chat effects. Inventory found the Caveman skill and Context Mode 2.1.8 already installed. Caveman bytes match the pinned v4.1.0 source; no duplicate installation. Context Mode initially had Node 24.14.0 below minimum and four untrusted hooks.

After explicit owner scope approval, wrote default-use instructions to previously empty `~/.codex/AGENTS.md` and used the inspected Context Mode CLI to add precisely four trust entries to `~/.codex/config.toml`. Backups: `~/.codex/tooling-backups/2026-11-13-DPT-OPS-004`, plus Context Mode's own timestamped backup. All backup bytes remain outside Git.

Automatic review rejected the initial system MSI action until the owner explicitly approved machine-wide Node/npm/PATH mutation. Silent MSI then failed with Administrator-required Error 1730/exit 1603. Same checksum/signature-verified MSI via UAC exited 0; actual system Node 24.22.3 and npm 11.19.1 verified. No forced reboot or optional build tools.

Project-local acquisitions: official portable Node archive/runtime and MSI under ignored `.agent-tools/runtime`; pinned Caveman source under ignored `.agent-tools/external/caveman`; diagnostic scripts/reports in ignored `.agent-tools/tooling-audit`. This source clone is not a Caveman CLI installation. No npm install/npx/bootstrap script, account login, paid actor, gateway or model routing used.

Evidence: SQLite FTS5 smoke, successful setup/CLI doctor, MCP tools/list and real local synthetic ctx_execute. Fresh MCP doctor: ten PASS, two WARN after process-only PATH-key normalization. Initial standalone EPERM and Windows Path/PATH casing failures were diagnosed and recorded. Existing chat MCP transport closed after MSI: Codex restart and host recheck remain pending.

Rollback: restore only this task's AGENTS preference and four hook trust entries, comparing backups against current files to preserve later edits. Any MSI-managed Node downgrade needs separate authorization and a verified official installer. Keep safe legacy files; no unsolicited cleanup. Detailed exact hashes/paths/results and next action: [[DPT-OPS-004_Agent_Tooling_Setup]]. Inventory: [[Agent_Tool_Registry]].

Session result: local setup verified; host-reload acceptance pending. Documentation-only review branch `codex/caveman-context-mode-setup`, base `aa55f8b59acb0872b3b40273a8cdd25198f3ba27`; PR publication pending at authoring. Root PR #8 branch/source and all other workstreams preserved. Human Owner alone merges; no final task receipt while host-reload acceptance remains pending.

Publication readback: payload `ce4fa34c95f5d76fa6b467979df0c8d9f37f0067` pushed; [PR #12](https://github.com/kraveerachat/DoomParfum-By-TK/pull/12) OPEN/DRAFT with exactly six Markdown files. Same-branch publication-metadata checkpoint follows. Both worktrees were clean and root HEAD unchanged at readback. No merge or host-restart completion claimed.

## Post-merge Waves 0–2 — 2026-11-13

Fresh functional observation: ContextMode2.1.10(877eebc),Nodev24.22.1,codex0.167.0-alpha.4.1;
doctor11PASS/1WARN/0FAIL and bounded pure synthetic ctx_execute PASS. Warning is safe legacy/temp
state; no cleanup or upgrade performed. All3observed relevant Codex/code-mode processes started
before PR12merge05:59:01Z. Post-merge restart NOT VERIFIED; host-reload gate remains PARTIAL.
Do not stop this active app or manufacture a PR12receipt. Owner may restart after safe handoff,
then obtain fresh host observation. Actual machine paths/process details remain private.
[[DPT-DOC-001_Post_Merge_Tool_Observation]] records the sanitized evidence. No installation,
global config, hook, model, cloud gateway, credential or paid-service change in these waves.

## 2026-11-23 — DPT-PLAN-012 local design planning

Primary Impeccable skill v4.5.2; existing engine pin 0.1.14; `impeccable context` ran once successfully. No PRODUCT.md/DESIGN.md/frontend existed initially. Existing ui-craft guided layout/state review; ui-ux-pro-max local Python searches supplemented style/accessibility/Next.js guidance. Initial Liquid Glass recommendation rejected as off-brief; one narrowed style query used. No installation, update, hooks, pin shortcuts, MCP configuration or external repository checkout. Context Mode executed/indexed long reads and search; one abbreviated source selector returned no hits, corrected by using the exact source label. Brave CUA inspected twenty official reference URLs and mobile attempts, then reset viewport and closed temporary research tabs. No account login, transaction, asset download or protected-source copy. Native web tools checked official framework/Docker/noindex/font-license texts. Tool rollback: no setup/config changes to roll back; documentation rollback only through reviewed Git change. Full outcomes/limits: [[DPT-PLAN-012_Luxury_Frontend_Editorial]].

## 2026-11-24 — IMP-WEB-01 implementation tools

Impeccable primary (context, detector, finish reviewer); `ui-craft-editorial` consulted; `ui-ux-pro-max:brand` requested but not used (out of scope by project rule); Taste Skill not used. No hook, MCP, global install or client setting was changed. New project-local dependencies are pinned in `web/package-lock.json`, installed with lifecycle scripts disabled. Task-created Docker resources: images `doomparfum-web:preview` and `doomparfum-web:dev`, container `doomparfum-web`, volumes `doomparfum-web-dev_dev-node-modules` and `doomparfum-web-dev_dev-next`. Rollback: `docker compose down` in `web/`, then remove those named images and volumes. Details: [[2026-11-24_IMP-WEB-01_S1_Report]].

## 2026-11-25 — IMP-WEB-01 S3 tools

Impeccable primary (hardening reference and detector); other requested design commands not used because the same instruction forbids a broad polish round; `ui-ux-pro-max:brand` out of scope. No hook, MCP, global install, client setting or dependency changed. Docker image tag `doomparfum-web:s2-rollback` (the previous preview) was added; temporary S3 resources were removed by name. Rollback of the preview: tag `s2-rollback` as `preview`, then `docker compose up --force-recreate --detach` without `--build` in `web/`.
