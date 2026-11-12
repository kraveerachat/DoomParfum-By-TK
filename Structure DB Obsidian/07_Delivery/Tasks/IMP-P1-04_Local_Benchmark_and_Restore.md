---
id: IMP-P1-04
project: DoomParfum By TK
type: implementation_task
status: partial-blocked
owner: human-owner
updated: 2026-11-12
tags: [doomparfum, benchmark, recovery, local]
source_of_truth: "../../../README.md"
---

# IMP-P1-04 — Controlled local ETL benchmark and recovery

## Start / authority / scope

Owner explicitly requested independent post-PR5 workstreams. PR5 owner merge verified at
55d39cd619fa6c1ae70521720aa734d632a2083d; fresh origin/main matches; starting branch
codex/imp-p1-04-local-benchmark-restore from that SHA. PRs1/2/3/5 merged; PR4 remains Draft.
AGENTS/workflow/root and vault README/current status/approved P1 plan, OD03/05, P1 pilot/recovery
specifications, actual migrations/source/test evidence and original receipts inspected.

OD05 approves local DB/object backup and restore testing. The current explicit parallel request
authorizes the independent DB/performance portion using merged01/02 and owned SYNTHETIC test objects.
Full pilot01–03 dependency/image-pipeline acceptance remains incomplete until03's own review/merge
and exact asset permissions. No actual-image/provider recovery or production readiness is inferred.

## Plan / expected evidence / do-not-touch

1. Characterize unchanged full licensed intake/replay using bounded controlled isolated transactions;
   retain the independently reviewed exact12/full1479 mapping cohorts (no forged25/100/250 mapping
   approval), exact input keys/hashes, warmups/repeats,
   wall time and actual validator call counts; no rewrite of immutable migrations/constraints.
2. Measure all relevant table/heap/index/TOAST/database sizes and row counts before/after ANALYZE,
   distinguish empty metadata/drafts/approved materialization from raw file size; no invented capacity.
3. Export a consistent read-only pilot snapshot to a private local custom-format archive; no password/
   private raw dump in public Git. Restore to a separately guarded disposable PostgreSQL target with
   actual roles/ownership/RLS/constraints intact. Never reset the data-bearing pilot/foundation.
4. Compare tables/claims/selected IDs/rights/scopes and non-owner isolation; negative corrupt/truncated
   dump, missing-role/policy and wrong/missing-object/hash controls. Owned SYNTHETIC local objects
   exercise manifest/independent copy integrity, not third-party image grants or HTTP delivery.
5. Publish sanitized exact results/limits, independent review and dedicated Draft PR; parent owns
   external D1-D9 ledger and single LATEST ZIP. Full-suite shared disposable DB use is coordinated.

Resource bound: existing task Docker image PostgreSQL16.15,768MiB/2CPU,loopback only; no new cloud/
host/provider. Parent times dpt_scento_test and restores to the independent no-network
doomparfum-p1-04-restore/dpt_restore_test target; image lane uses
dpt_schema_test only outside the controlled timing window; persistent pilot read-only
for backup/readback. Stop bounded runs on timeout/resource failure, preserve evidence; never disable
validation/security to obtain a passing benchmark. No production/main/old receipt/migration mutation.

TOOL DECISION: existing GitHub MCP/Git/PowerShell/Python/Docker; official PostgreSQL docs for measured
stats/dump semantics when needed. No new dependency, credentials, paid API, source acquisition or
global configuration. PRODUCTION_MUTATION=NO. Results/PR/head remain pending actual execution.

## Observed controlled attempts — 2026-11-12

Original attempt001 stopped at fullfresh with SQLSTATE23514 Future review timestamp. Pilotthreefresh/
replaypairs completed. Independent harnessreview found reusable-run races/resourceattestation gaps;
fixed with commonGit-root exclusivelease/reportownership/atomictemp/perrunapplication/noFORCEreset/
all-clientrefusal/actual768MiB2CPUattestation.30offline tests independently passed. Original benchmark
5d3a77424aaa053faaca413fe3517028250064738ccaa8377a812ee1ca86cbc4 preserved; hardened bfcf0418...
uses unchanged original importer/mapping/timedSQL/rights/constraints. No artificial timestamp offset,
backdating or validator relaxation. Reports001/002 retained separately, failed cases not hidden.

Hardened attempt002: threepilotfresh/replaypairs pass; fullfresh1479 commits246.226887s, complete
model/image validators1call each. Fullreplay again fails23514, so fullreplayperformance acceptance
is BLOCKED. Coreinventory readback equals committedfullfresh and validationmarkers0. Earlier200000
consecutiveclockprobe comparisons observed0backwardsteps; root cause of timestamprejection is NOT
ESTABLISHED. Do not infer a clockfix or disguise it by weakening the future-review guard.

Fullfresh functiontrace: validate_all_deferred109726calls/self132856.747ms; serialize_write65461/
36974.653ms; schedule_validation53110/31782.643ms; check_active_row19736/15163.568ms; validate_model
1/8506.461ms. Remaining rowcallbacks/transaction-state cost dominates this run; no asymptotic or
productionthroughput claim from onefullcohort. Original earlier452s/291s runs are differentconditions,
not a controlledbefore/after optimization comparison. Fresh1479 createsonebatch2059staging/8236
validations; persistentpilot contains75extra historicalpilotstaging/300validations, not duplicatefacts.

Afterfailedreplay inspection: DB56982551bytes beforeVACUUMANALYZE,57662487after; systemcatalogue/
metadata changes mean databasebytes neednotshrink. Relationheap/index/TOAST/rows and read-onlyadmin
EXPLAIN retained privately/sanitized later. This is not a successful replaymeasurement. Independent
DBrestore/syntheticobjectrecovery remain pending actualexecution below. Realimage/provider recovery
is still blocked by03review/perassetgrant/integration, not supplied by an emptyrealimagecount.

Independentfinalrecoveryreview source15b2727d.../34offlinecases passed, no blockingfinding in declared
local subset. Report51a709d5e8eb8a47a4831177413edc2f6e35529bb75191a0b451230ad2d9a0d2.
This is source/test review, not a live restore PASS. Initialtargetplan corrected to separatepinned
networknone restorecontainer, not another DBintheexistingcontainer.

## Recovery and final source review — 2026-11-12

Finalrecovery004 VERIFIED_LOCAL_DB_AND_SYNTHETIC_OBJECT_SUBSET,29.656s,15/15controls. All49table
count/SHA manifests and roles/ACL/RLS/constraints preserved; source unchanged. TwoownedSYNTHETIC
objects9896bytes, missing/corruption negatives pass, realimages0. Independenttarget512MiB1CPU/no
network/ports stopped afterward; volume/dumps retained privately in ignored.local. No acceptedRTO/
offsite/encryption/retention/cloud/imagepipeline claim. Details [[IMP-P1-04_Capacity_and_Recovery_Evidence]].

Recovery001 read-only ACLdeconstructor failed22023;002 strict comparison caught associativeOR text
reparse;003 candidatepositive precededindependent comparatorsecurityfinding. Final004 pins thetwo
exactknownCHECKhashes beforeadditional8748-caseproof; unsampled3spacebypass/unknownpredicate
negative rejects beforeSQL. No constraints/privileges changed. Allfailedreports retained; actual
independentreview e195412c8dd5c5ba830fa19314b90cc5ac3ee5368cf6688517fb19361adf041a has14checks/
37offline methods; reviewer didnotrunDB. Fullbenchmarkevidence44independentchecks pass, not afull
replayPASS. Driverfinalregression/diff/docs/secret checks and Draftpublication follow.

DockerDesktop/sourcecontainer wereoff afterinterruption; onepreflightregressionfailed atguard before
DB setup, rawreportpreserved; existingDesktop/container restarted withoutpilot/foundationreset. No
install/globalconfig/auth change. Final170-methodsuite includes98baseline+30benchmark+42recovery
methods; finalcanonical-LF source/hashes verifiedbeforepublication. No fullreplayfailurewaiver.

Task remains PARTIAL/BLOCKED; no finalreceiptiscreated prematurely. Next: focused diagnosis of23514
Future review timestamp and preservedguard semantics before completing fullreplaycapacityacceptance.
Owner reviews separate DraftPR; realimage/provider recovery waits for03gate/rights/integration.
No source/canonical/held-profile mutation, newmigration, Production operation, mainwrite or merge.

FinalpublishablecanonicalLF regression170/170PASS126.110s,0fail/error/skip. Fullsourcehashesfresh in
capacity_test_results.json; no originalsource/harness/migration changes. Recoverytestlineendingsonly
normalized forGitportablehashes; reviewedlogicalcontent unchanged. Finaldocs/diff/secret-pattern/model
checks and same-taskDraftpublication follow; fullreplay23514BLOCKED remains, no finalreceipt.

## Partial Draft publication — not ready to merge

[PR8](https://github.com/kraveerachat/DoomParfum-By-TK/pull/8) created OPEN/DRAFT on this taskbranch.
Source/evidencecheckpoint53fec48fd73ed4f1574c55e2b5535c56475d85f7 independentlyverified74/74checks;
all22tested sourcehashes match committedbytes. Report5fd8abd4186128dab276aa146abf9fff99c083b631c5e921b37601645c5846dc.
Protectedoriginals preserved; testCRLF→LF normalization independentlyverified text/AST-equivalent.
Finalmetadata source/evidenceblobs unchanged.8Markdown/5frontmatters/35wiki/9local/47table checks
passed0errors/0secretcandidates; exact18changedpaths in capacity_documentation_checks.json.
Fullreplay23514 remainsBLOCKED, no prematurefinalreceipt; recovery004subset/170regression evidence
isnot a waiver. Human Ownerreviews; resultingpublicationHEAD verified afterpush inPR/externalhandoff.
