---
id: DPT-OPS-TOOLS-001
project: DoomParfum By TK
type: tool_registry
status: proposed
updated: 2026-11-13
tags: [doomparfum, operations, tools]
source_of_truth: "../../README.md"
---

# Agent Tool Registry

## Post-PR13–17 verified integration — 2026-11-13

New health check: ContextMode2.1.10(877eebc),Nodev24.22.1,doctor11PASS/1WARN/0FAIL;
SYNTHETIC_POST_PR13_17_SMOKE_OK passed. Caveman installed guidance read/applied. No installation,
upgrade,hook/config/account/service change. Host restart not verified; gatePARTIAL. Old temp/data
warning is retained safely, not cleaned. Full observation/evidence:[[DPT-DOC-002_Post_PR13_17_Preflight]].


## Post-merge Waves 0–2 — 2026-11-13

Fresh functional observation: ContextMode2.1.10(877eebc),Nodev24.22.1,codex0.167.0-alpha.4.1;
doctor11PASS/1WARN/0FAIL and bounded pure synthetic ctx_execute PASS. Warning is safe legacy/temp
state; no cleanup or upgrade performed. All3observed relevant Codex/code-mode processes started
before PR12merge05:59:01Z. Post-merge restart NOT VERIFIED; host-reload gate remains PARTIAL.
Do not stop this active app or manufacture a PR12receipt. Owner may restart after safe handoff,
then obtain fresh host observation. Actual machine paths/process details remain private.
[[DPT-DOC-001_Post_Merge_Tool_Observation]] records the sanitized evidence. No installation,
global config, hook, model, cloud gateway, credential or paid-service change in these waves.


Initial registry addition for Human Owner documentation review. Availability below is observed on this Windows host, not a requirement that other contributors install tools. The approved catalogue remains `AGENTS.md`; unlisted inventory entries are NOT VERIFIED.

| Tool | Actual integration and location | Version/ref | Verified state and scope |
|---|---|---|---|
| TOOL-02 Caveman | Existing `~/.codex/skills/caveman/SKILL.md`; default preference in `~/.codex/AGENTS.md` | Skill byte-identical to v4.1.0 / `1e91f1306d602d4ca23618701b1185575ae1869b` | User-level concise-response skill; defaults loaded into current chat. No Caveman CLI, proxy, automatic model routing or cloud gateway setup performed. |
| TOOL-04 Context Mode | Existing enabled Codex plugin at `~/.codex/plugins/cache/context-mode/context-mode/2.1.8`; four trust entries in `~/.codex/config.toml` | 2.1.8 / doctor ref `92c1ad2` | Local MCP/hooks; fresh-process execution and diagnostics verified. Restart Codex to restore its old closed transport. Index data scoped per project under `~/.context-mode`. |
| Node.js | MSI-managed `C:/Program Files/nodejs` | 24.22.3; npm 11.19.1 | Explicit owner-approved machine-wide update; affects other programs using this Node/PATH. MSI exit 0, version readback verified. |
| Portable Node.js | Ignored root `.agent-tools/runtime/node-v24.22.3-win-x64` | 24.22.3 | Diagnostic runtime retained; not added to permanent PATH. |
| Caveman source | Ignored root `.agent-tools/external/caveman` | Detached v4.1.0 / `1e91f1306d602d4ca23618701b1185575ae1869b` | Source inspection only; no downloaded installer/hooks executed. |

Caveman reduces response verbosity; Context Mode filters/indexes tool output. The integrations serve different sides of the conversation. No competing Caveman input-compression layer was enabled. No savings percentage was measured for DoomParfum.

The defaults apply to this user's local Codex chats/projects that load these settings. They do not automatically configure ChatGPT web, another computer, Claude Code or another user's account. Same-project local indexes can support retrieval between sessions; project indexes do not merge entire conversations or automatically become a cloud memory.

## Permissions, caveats and rollback

All setup changes were bounded by explicit owner approvals recorded in [[DPT-OPS-004_Agent_Tooling_Setup]]. User settings/hooks were backed up outside Git before mutation. System Node update needed a separate machine-wide approval and Windows UAC. No credentials, paid API, cloud gateway or production access was used.

Context Mode license: Elastic-2.0 (local use; hosted-service limitations apply). Caveman v4.1.0 source: Apache-2.0, retaining applicable MIT notices. Node artifacts were verified against official checksums and valid OpenJS Foundation signatures.

Known limits: Context Mode has an available 2.1.10 update and safe legacy-data warnings; 2.1.8's direct PowerShell child environment needs uppercase PATH for correct Git Bash diagnostics. The actual Codex host needs a post-restart check; do not infer recovery from a fresh standalone process.

Paths, exact hashes, tests, failed attempts and rollback precautions: [[DPT-OPS-004_Agent_Tooling_Setup]]. Change events: [[Tool_Usage_Log]]. Do not commit runtime archives, cloned sources, installer logs, local databases, backups or complete user configuration.

## Primary documentation

- [Caveman v4.1.0 installation guide](https://github.com/JuliusBrussee/caveman/blob/1e91f1306d602d4ca23618701b1185575ae1869b/INSTALL.md)
- [Context Mode v2.1.8 README](https://github.com/mksglu/context-mode/blob/v2.1.8/README.md)
- [Official Node downloads](https://nodejs.org/en/download)
- [Node 24.22.3 official checksums](https://nodejs.org/dist/v24.22.3/SHASUMS256.txt)
