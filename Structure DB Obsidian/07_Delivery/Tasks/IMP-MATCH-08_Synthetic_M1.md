---
id: IMP-MATCH-08
project: DoomParfum By TK
type: implementation_task
status: in-progress
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, synthetic, matching, m1]
source_of_truth: "../../../README.md"
---

# IMP-MATCH-08 — exact synthetic notes-layered M1

## Current session — IN PROGRESS

Human Owner approval: [[M1_Exact_Owner_Acceptance]], 2026-11-14 Asia/Bangkok.
Contract M1-NL-TYPED-1 SHA-256 a57f4c56e1068a3d86a99e562b31e5c3923e2d369cb4e812c1dd5f5550a5ada3;
method mc-a-notes-layered-p1/config m1-nl-typed-config-1; no contract modification.
Branch `codex/imp-match-08-synthetic-m1`, starting/base main `0da217671ec6473716eea5947f013d44e6fd91cb`.
Latest fetch confirms PR22–25 Owner merges included. Existing clean PR8 checkout and all other
worktrees are preserved. All five preparation drafts remain byte-exact; their old pending wording
is superseded only by the new exact Owner decision, not rewritten.

Plan: write genuinely failing golden/negative/property tests; implement the exact pure typed
function; run focused tests and existing math/research/adapter offline regressions; inspect
source/diff/docs/common secrets and all protected main files; obtain independent review at an
explicit source commit; resolve actual findings and rerun affected tests; prepare one scoped
receipt and one Draft PR only after agent acceptance criteria pass. No automatic merge.

Own only new M1 code/tests/evidence, this task, acceptance/documentation records and essential
additive shared status/log/roadmap reconciliation. Existing primitives, adapter, database,
migrations, receipts, raw/private data, rights, normalization, 44 holds and matching eligibility
are protected. No DB/Docker/network calls from scorer or tests; no source acquisition.

Current evidence: pre-implementation merged-main62 regression and contract75 checks are historical
preparation evidence, not M1 feature acceptance. Actual M1 RED/GREEN, property/regression and
independent implementation results will be recorded below and in [[IMP-MATCH-08_Synthetic_M1_Evidence]].
No final receipt or PR exists at session start. No application/publication/real-data activation.

## Actual TDD and regression checkpoint — 2026-11-14

Actual RED before scorer creation:43methods/43setup failures/0errors; feature/property bodies did
not execute at RED. First GREEN43/43 passed. Added malformed-field negative coverage then exposed
one AttributeError; that failed49-method run and its source snapshots remain preserved. The
targeted correction converts missing required fields during validation into a fixed bounded
ValueError; no formula, input scope, acceptance artifact or security check was weakened.

Final focused45 plus4bounded-property methods:49/49 PASS,0failures/errors/skips,1.3121664s.
Properties executed4096complete-pyramid pairs,250seeded missing/incomplete/domain pairs,
24candidate permutations and5unsupported configurations; case counts are not method counts.
Combined111/111 PASS,0failures/errors/skips,1.9161620999802835s: existing24math+7invariants+
17research+14offline adapter, plus new45focused+4properties. Python3.11.9; Hypothesis unavailable,
so no dependency was installed. Existing53protected base blobs and5preparation documents match.
Public m1_red_results/m1_shape_red_results/m1_focused_results/m1_regression_results JSON files
contain exact commands, timings, limitations and source bindings; private logs/snapshots stay ignored.
Source inventory hashes do not claim every database module was exercised. No DB/network calls.

Documentation pre-review check:20Markdown/frontmatters,325Wiki/4local links,49protected document-
validator blobs and47logical-table parity;0errors/common-secret candidates. The broader53 count
also includes existing matching Python sources. These are separate static and runtime units.
Independent exact-source review is still PENDING at this checkpoint; no final receipt or PR yet.
Full Mode A/B1/B2,real data,API/UI,DB/live RLS/replay/recovery/transport/rights tests NOT RUN.
