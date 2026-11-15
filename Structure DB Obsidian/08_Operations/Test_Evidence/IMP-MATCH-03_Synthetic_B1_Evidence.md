---
id: IMP-MATCH-03-EVIDENCE
project: DoomParfum By TK
type: implementation_evidence
status: in-progress
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, synthetic, b1, implementation]
source_of_truth: "../../../README.md"
---

# Actual B1 implementation evidence

IN PROGRESS under [[B1_Exact_Owner_Acceptance]]; exact contract revision2/hash77bfca59... unchanged.
Base604d447e599aa8359d3427dfbfbceaac85373e48,branchcodex/imp-match-03-synthetic-b1.
Actual RED/GREEN/property/combined regressions and independent exact-source review will be recorded
after execution. No feature PASS/receipt/PR claimed here. Prior contract125/summary24 are document
review evidence, not B1 scorer tests. No DB/network/rights/hold/eligibility or Production mutation.

## Actual RED/GREEN and combined regression checkpoint — 2026-11-15

Actual RED before runtime creation: command python -m unittest matching_math.tests.test_synthetic_b1
matching_math.tests.test_synthetic_b1_properties -v exited1 with2absent-module import errors;
0feature bodies executed. Test source snapshots and private log are preserved; public b1_red_results.json
qualifies the import-stage failure. The first GREEN attempt exposed an uppercase-UUID test fixture
using an all-digit suffix, so uppercasing did not change input. The fixture was corrected to a
hexadecimal letter suffix; failed run/source snapshots are preserved in b1_first_green_attempt_failure.json.
This did not relax the canonical-ID contract or change an approved policy.

Final53/53 methods PASS:45focused golden/negative/schema/boundary plus8property methods.
Recorded443property scorer invocations include192complete exhaustive combinations and128seeded
unavailable cases. Internal case/call counts are not additional unittest methods. Focused command
exited0; unittest reported0.137s,subprocess0.286540s;py_compile exited0. Exact timings/source hashes
are in matching_math/evidence/b1_focused_results.json; no capacity/SLA or scientific smell claim.

Coordinator combined164/164 PASS,0failures/errors/skips,1.3506992000038736s. Components:existing
24math+7invariants+17research+14offline adapter+45M1focused+4M1properties=111,plus45B1focused+8B1properties.
Python3.11.9;Hypothesis absent;bounded stdlib properties used without installation. DB/network calls0.
Public b1_regression_results.json binds raw execution source bytes; canonical Git LF may differ
from existing Windows CRLF. Inventory hashes do not claim every bound database module was exercised.

All57protected base source/governance/receipt files,22existing receipts/eightmigrations and M1
evidence remain unchanged. All19preparation files were snapshotted;8standalone files remain byte-exact;
shared histories are additive. Independent exact-source implementation review is PENDING at this
checkpoint, no final receipt or PR yet. Full Mode A/B2/real-data/API/UI/transport/DB/liveRLS/replay/
recovery/performance/rights/Production tests NOT RUN or outside this scoped task.

Parallel research completed independently: [[IMP_MATCH_03_Data_Research_Continuation]]16staticchecks
with2official property-reference reads(no entity/sample queries), and [[IMP_MATCH_03_Media_Research_Continuation]]
39static checks on retained metadata/current PNG validator(no new network/image bytes). Neither
approves data imports, image intake, source normalization,44holds or eligibility changes.
