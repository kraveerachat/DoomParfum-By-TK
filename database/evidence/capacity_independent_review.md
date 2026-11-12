# IMP-P1-04 independent review and execution boundaries

The delegated benchmark reviewer identified lease/cancellation/report-reservation/resource-attestation
gaps in the initial harness. They were corrected, independently inspected and exercised by30offline
tests while retaining original importer/migrations/timed SQL. Final benchmark source SHA-256
`bfcf0418eef26f4c26bf06cdbe74f67730a93d45b27f5457ddc1bdc6b55e254c`.
Independent benchmark-evidence review44checks passed; report SHA-256
`1670570bd60f273fcf34fb326d16c1ea80a037f9d8a369abd8d95bfd4f32e93e`.
It explicitly retains both23514failures and no completed full-replay measurement.

Independent recovery review required safe role/ACL mapping, persisted archive readback, specific
rollback-safe42501 controls, repeatable missing-role restore and shared owned reporting/lease.
Live execution found empty ACL deconstruction and a known associative-OR CHECK deparse difference.
An independent three-space evidence-URL counterexample invalidated a generic finite-sampling waiver.
Final code requires the two exact approved source/observed-restore definition hashes before an
additional8748-case proof on both servers. Unknown predicates reject before SQL; no real constraint
or permission was changed. All other security fields require exact equality.

Final pinned recovery source SHA-256
`bb2cc0a9d282d09c3a717cab66fdb3b2f6ba1683c09d43f378af105078494107`;
independent14checks/37offline tests passed, no blocking source finding within the local subset.
Report SHA-256 `e195412c8dd5c5ba830fa19314b90cc5ac3ee5368cf6688517fb19361adf041a`.
Test-file CRLF→LF normalization preserves reviewed logical content; final complete suite170/170
passed on the canonical publishable LF source. Exact source-file hashes are in capacity_test_results.json.

Reviewer made no DB/Docker/network/Git calls and did not claim live execution. Coordinator ran the
actual recovery004:15controls pass, all49table manifests/security/source preserved, two owned
synthetic objects9896bytes; zero actual images. Final170/170 regression passed126.110s,0fail/error/skip.
Earlier development failures and superseded comparator execution remain separately identified.

No overall merge readiness: full replay23514 and actual-image/offsite/provider gates remain blocked.
No final task receipt is created prematurely. Exact checkpoint verification follows source commit;
Human Owner alone decides next scope and merges. No production/cloud/force/main operation.
