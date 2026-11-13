---
id: DPT-QA-001-EVIDENCE
project: DoomParfum By TK
type: test_evidence
status: independent-review-pending
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, qa, exact-arithmetic, invariants, synthetic]
source_of_truth: "../../../README.md"
---

# DPT-QA-001 — Primitive invariant evidence

## Scope and authority

Base/HEAD `8c6a8376680c7a10cc3eb4b5cf80afe4376a9282`; branch `codex/qa-primitive-invariants`.
[[DPT-QA-001_Primitive_Invariants]] records the task. The complete1,376-line current Owner Master
Prompt SHA256 is `b459c07e94ff6c68682165c3a166c7965a31b36e39e6a231118c304c1e402b23`.
Its conservative high-level direction and bounded generic unit/property QA are approved scope.
Exact matching methods, weights, alias/normalization, closure, authorization and source rights
remain separate PROPOSED choices. Merged PR18contains proposed full-scoring contracts, not this
generic mathematical test authorization or proof that a scorer exists.

This task adds seven tests for the already accepted pure primitives. It changes no runtime source,
old test, original unit_results, migration, observation, receipt or source/eligibility decision.
No full A/B1/B2 implementation, request normalization, layer/alias assignment, ranking or real-data
fixture was added. No database/container/network/install/configuration operation occurred.

## Nonduplicate test rationale and deterministic bounds

The original24methods already test arithmetic golden values, pairwise range/symmetry/identity,
numeric rejection, explicit missing/scale/domain states, weight scaling and UUID ordering. The
new tests cover different relations or public call boundaries:

| New method | Mathematical obligation / gap | Internal bounded cases |
|---|---|---:|
| Nonempty set distance triangle | d=1-J across three complete nonempty sets, not just pairwise symmetry/range; all7nonempty subsets of3synthetic symbols | 343triples |
| Weighted Jaccard L1oracle | independent identity J=(sum(x+y)-sum(abs(x-y)))/(sum(x+y)+sum(abs(x-y))); no min/max oracle copied from implementation | 80numeric vector pairs |
| Common vector scaling / joint explicit zero axis | common positive finite scaling preserves a ratio; fully supplied zero coordinates in a separately named synthetic domain leave it unchanged | 6scaling+3zero-axis comparisons |
| Known weighted-mean affine equivariance | mean(a*x+b)=a*mean(x)+b for bounded values, explicit positive weights and maps staying within[0,1] | 81relations |
| Split known component weight | duplicate an explicitly known abstract component value while partitioning only its supplied positive weight; mean stays exact | 27relations |
| Coverage complementarity | C(r)+C(1-r)=1 under unchanged explicit original weights; no default threshold or missing observation inferred | 27relations |
| Public operand-category rejection | set/vector comparisons reject wrong DTO/category even though constructors have their own tests | 4negative calls |

Total571internal cases across7test methods. These are not571unit methods, product features,
catalogue records or matches. The joint all-zero vector pair is outside the numeric L1identity;
existing tests already cover its undefined denominator. The new oracle uses the other80pairs.
Zero-axis fixtures supply both full vectors explicitly; they do not authorize runtime zero-padding,
an absent-means-zero source contract or a real source-scale conversion. Split-weight tests have
no unknown components and do not authorize component redistribution, note deduplication or aliases.
All symbols, coordinates, weights and flags are synthetic math inputs, never scoring defaults.

## NEWLY EXECUTED commands and results

Actual working directory: task checkout root `.local/worktrees/primitive-invariants` under the
verified common checkout. Absolute local cwd and original command logs remain ignored in
`.local/post1821-QA/run_001/RESULT_WITH_LOCAL_CWD.json` and its adjacent logs. Python3.11.9,
CPython64bit; run recorded at2026-11-13T20:13:25.016910Z (2026-11-14Asia/Bangkok).

| Exact command from task root | Methods passed / failed / errors / skips | unittest time | Whole command wall time |
|---|---|---:|---:|
| python -m unittest discover -s matching_math/tests -p test_invariants.py -v | 7/0/0/0 | 0.014s | 0.161724s |
| python -m unittest discover -s matching_math/tests -v | 31/0/0/0 | 0.045s | 0.176651s |

The focused7are a subset of the31math regression methods; do not add them to claim38methods.
Both commands exited0. Durations measure this bounded QA run, not matching capacity/SLA or a
performance benchmark. Parent Wave0's55offline/49-fingerprint checks are separate evidence, not
rerun or counted by this worker. Full repository/database/API/security/relevance tests are NOT RUN.

Tests were written before execution. They initially passed the existing accepted implementation;
this is test-only coverage, **not a fabricated RED-to-GREEN runtime fix**. No counterexample or
primitive correction was found. If independent review identifies a mathematical/policy ambiguity,
stop the affected change and preserve the exact result before proposing any correction.

## Exact source and evidence bindings

| Artifact | SHA-256 / binding |
|---|---|
| Unchanged matching_math/primitives.py | c1b69bdc74a4a060f6559a182306618f02c595b16e27f3ebb5e4bcca4ff7b735; canonical base Git bytes |
| Unchanged tests/test_primitives.py | 777b2e2b04d0f67ab32a279940faa2488ba59cc70050cacc4b487fcecacbde30; canonical base Git bytes |
| Unchanged evidence/unit_results.json | aa82385197b6f275f9ce3d0bc35c6458c83f258eedfde24abb2226256d5a3313; canonical base Git bytes |
| New tests/test_invariants.py | 9b285c675c84f98d8328c2dd46ac9d4d33205eacdc3bc709188d9c240c742343; exact UTF-8/LF test source |
| New evidence/invariant_results.json | d9bdb4500cf712015ed894b38681f4fca25784092b9eba171d726a1dd44de203; newly executed sanitized result |
| Focused original output | 16985aaacd08bad5a724bec551f43e1b01088f269b7a08924102bf6c13f242aa; ignored original text |
| Math regression original output | a2f5ef7070a1e6fe662886f2cb97f1d7223fe33291e118b277c82084851e8de4; ignored original text |

Raw checkout newline conversion can change local bytes of old files; old source bindings use Git
blobs at the exact base. New machine-readable evidence is separate from, and does not overwrite,
the original24-method report. The original package README's24-method account remains historical
source evidence; the command with this new test file now executes31methods. No original receipt
is rewritten to retroactively accept a complete ModeA task.

## Review and limitations

Independent exact-source review is PENDING. Author tests do not satisfy independent acceptance.
No new matching method, weights, thresholds, closure, source right, application principal, public
API/UI or real-data route is accepted here. Existing44holds and current eligibility flags remain
unchanged. RLS/rights/revocation/replay/rollback/concurrency and real-data integration are NOT RUN.
The database container remained stopped; no runtime or catalogue mutation was performed.

TOOL EXECUTION REPORT: existing Caveman, functional Context Mode bounded result read, Git/Python/
unittest and static documentation inspection used. Installed/changed tools NONE. Exactly one new
test, one new result JSON and two dedicated Obsidian files are in scope. Logs/helper stay ignored
`.local/post1821-QA`. Worker commit/push/PR/receipt NONE. Coordinator handles independent review,
shared status/publication and Human Owner review; no agent merge or Production change.

Author static verification: `python .local/post1821-QA/check_payload.py` passes41/41assertions,
0failures. It checks exactly four new allowed files, seven test methods/pure imports, focused/full
run counts and retained output hashes, six source bindings,571internal-case accounting,2new
frontmatters/source targets and2resolving Wikilinks, whitespace/conflict/common secret patterns,
no existing tracked changes and git diff --check PASS. These are static assertions, not additional
unit methods. Exact frozen payload manifest is ignored `.local/post1821-QA/PAYLOAD_CHECKS.json`.
Independent review remains pending; no scope acceptance is inferred from author verification.
