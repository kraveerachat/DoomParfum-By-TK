---
id: DPT-DATA-002-EVIDENCE
project: DoomParfum By TK
type: test_evidence
status: review-pending
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, research, tests, provenance]
source_of_truth: "../../../README.md"
---

# DPT-DATA-002 — Offline audit execution evidence

Base/start aa55f8b59acb0872b3b40273a8cdd25198f3ba27; branch codex/post-pr4-data-quality.
Approved planning context: Owner-merged PR3/4 and explicit post-PR4 WorkstreamB request. No DM,
normalization, identity or source/asset permission is accepted by this research execution.

Actual command: python -m unittest discover -s database/tests -p test_research_audit.py
Result17/17PASS0.014s,0failure/error/skip. Controls cover preserved parent/country/alias claims,
ambiguous primary labels, no punctuation/fuzzy merge, repeated occurrence/order preservation,
same-note cross-layer separation, unknown/ambiguous materials, held-array/membership drift,
PNG filename versus byte validation, SVG/rights fail-closed behavior, fake grants/downloaded
identities, dimension arithmetic/source-scheme refusal, fabricated pair scores/approvals, output
boundary, fail-closed research eligibility semantics, deterministic Unicode serialization and
accounting checks independent of Python assertions. No RED-before-code claim.

Two real-input offline executions:

    python database/research_audit.py --bundle-root EXISTING_HANDOFF_ROOT --output EXISTING_HANDOFF_ROOT/08_OUTPUTS_APPROVED/post_PR4/research/audit_003
    python database/research_audit.py --bundle-root EXISTING_HANDOFF_ROOT --output EXISTING_HANDOFF_ROOT/08_OUTPUTS_APPROVED/post_PR4/research/audit_004_replay

Eight files compared, all byte-identical: brand_review_226.json, membership_policy_43_PROPOSED.json,
held_conflict_exclusion.json, media_review_15.json, pairwise_evidence_queue_5.json,
progressive_enrichment_index_1479.json, AUDIT_SUMMARY.json and OUTPUT_MANIFEST.json.
FINAL_REPLAY_CHECK.json retains hashes and actual17-method evidence outside public Git.
Earlier001/002runs remain unchanged, superseded because final labels distinguish no research
authorization from a live DB eligibility read and add explicit attribution/source lineage.

Executed sourceSHA256 fbbf4bf3cb253547feb8e8b0a71a5ea0d41347793a858edf2130396001a9cf93.
TestSHA256 bf1999b0c6dacb788eb872d9e3d8f32c2d111fcd4ba149cd548d62cf9bdcb5ab.
Actual counts and six-source/nine-research-input hash manifest:
[sanitized report](../../../database/evidence/research_audit_results.json).
Source hashes refer to the executed UTF8/LF bytes; committed-byte verification follows checkpoint.

No network request, DB call, asset byte acquisition, rights grant, canonical mutation, hold
resolution, alias/parent merge or usable pair created. All original source/research inputs frozen;
original code/migrations/receipts/shared logs protected.17methods cover only this standalone offline
module; shared DB/runtime/full application regression NOT RUN because no shared implementation changed.

Independent parent source review completed:203/203 assertions and17/17 independently rerun unit
methods pass,0failure/error/skip. Complete actual changed source/tests/guide reviewed, all8replay
artifacts and nine preserved research inputs plus six pinned sources verified, every proposed hold's
raw fields/arrays/occurrences retained; every existing base blob unchanged. No blocking finding in
this standalone offline scope. Review record SHA256
2975518fc56716d348c3db4fb1fd60324e36da693ac51ba122f6b05b027e445f
at external post_PR4/research/PARENT_INDEPENDENT_REVIEW.json. Parent is distinct from research author;
this is not Human Owner approval of policy, identity or rights. Final diff/doc checks follow.
[[Post_PR4_Data_Quality_and_Rights_Audit]] and
[[DPT-DATA-002_Post_PR4_Data_Quality]] record policy/rights/coverage limitations and next Owner actions.

Published source checkpoint276a081d2cfba5251135a35d6fda1019ce9f37ca; PR10 verified OPEN/DRAFT.
Final metadata adds one research receipt, with final doc/diff/common-secret checks recorded in
database/evidence/research_audit_documentation_checks.json. No rerun of equivalent dataset processing
or any DB experiment was needed after this documentation-only closeout.
