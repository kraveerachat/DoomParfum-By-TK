---
id: DPT-DOC-001-TOOL-OBSERVATION
project: DoomParfum By TK
type: tool_observation
status: partial-host-restart-unverified
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, tools, post-merge, evidence]
source_of_truth: "../../../README.md"
---

# Wave1F — Fresh tool health versus post-restart acceptance

PR12Owner-merged ate10ed2dc177d29837755d5a9173dd33d274f20a6,2026-11-13T05:59:01Z.
Merge does not establish its pending host-restart acceptance. Fresh process observation at
2026-11-13T08:02:32.4778285Z found relevant Codex/code-mode-host processes whose observed starts
predate that merge. It does not demonstrate a postmerge host restart. Gate remains NOT VERIFIED;
no claim that all possible host identities were exhaustively identified. Raw PIDs/start records
and machine-local details stay ignored.local; no private config, environment or credentials copied.

Fresh ctx_doctor actual result: ContextMode2.1.10(877eebc), agentcodex0.167.0-alpha.4.1,
Nodev24.22.1;11PASS/1WARN/0FAIL. MCP/hooks/project/database/shell checks pass. Warning concerns old
data/temp entries described as safe to keep. No upgrade, cleanup, Node/npm/hook/binary/global
configuration change was authorized or performed. No retroactive PR12receipt created.

One bounded synthetic ctx_execute Python call printed exactly SYNTHETIC_POSTMERGE_CONTEXT_SMOKE_OK.
It read no dataset/config, wrote no repository data and used no credentials/network service.
Current transport/execution is AVAILABLE/HEALTHY, unlike the historical Transport closed event.
This is a fresh current observation, not proof that the required host restart happened.

Caveman remains an installed chat-style preference; technical negations/commands and durable docs
retain complete meaning. ContextMode is used for long analysis/retrieval, ordinary tools for short
output/edits. No model/gateway/paid API is selected. If transport later fails, use bounded native
fallback and report the failure, not an invented full-mode activation.

Result: FUNCTIONAL TOOL CHECK PASS; HOST-RESTART ACCEPTANCE PARTIAL/NOT VERIFIED. Owner may restart
Codex after this execution has a safe handoff, then request a fresh doctor/synthetic check. The
coordinator will not restart the running app or close this gate on the Owner's behalf.
