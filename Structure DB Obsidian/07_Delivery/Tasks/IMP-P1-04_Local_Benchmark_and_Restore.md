---
id: IMP-P1-04
project: DoomParfum By TK
type: implementation_task
status: partial-blocked
owner: human-owner
updated: 2026-11-13
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


## Owner-requested temporal diagnosis checkpoint — 2026-11-12

Session starts at 6dc15a2e00ef979b0cbc39a72d461ebcd8533d47; freshly fetched origin/main
55d39cd619fa6c1ae70521720aa734d632a2083d. PR8 OPEN/DRAFT; full replay remains blocked.
Plan: capture exact failing row identifiers, reviewed/statement/transaction timestamps and the
single comparison clock in an equivalent diagnostic guard ONLY in disposable dpt_scento_test.
Preserve every original migration, future-review rejection, source/mapping rights and prior reports.
Only after demonstrated cause: smallest approved-scope ETL correction, independent review, future
review negative/regression controls, full import/replay and recovery. No backdating, disabled
triggers, production/persistent-pilot mutation, new rights, merge or main write. Other reviewers
inspect PR4/6/7 independently without DB workloads during controlled timing. Expected evidence:
raw private diagnostic trace, sanitized cause and tests, exact hashes, full replay zero new
canonical/source records and inventory integrity; D1–D9 and one consolidated ZIP at closeout.


## Temporal diagnosis results — current replay verified, defect unresolved

Recovered actual historical failing INSERTs: armaf-match-point/notes.base at2026-11-11 16:18:32.241UTC
and armaf-club-de-nuit-maleka/name at19:29:32.535UTC. Exact NEW.reviewed_at/comparisonclock values
were not logged and remain unavailable. Capped diagnostics001/002 reproduce0failures; both original
guards restored exact. No speculative importer, clock, migration, rights or validation change.

Original-guard003fresh250.550492s/replay106.022935s bothCOMMIT; strict raw49tablehash oracle fails
only staging_records (report retained, not an SQL failure). Independently reviewed004 comparison
verifies complete fullreplay107.147241s: zero all49rowcountdeltas, all48othercontenthashes exact,
all2059staging substantive rows exact, only exact44heldupdated_at timestamps strictlyadvance,
security/roles/guard/input hashes exact/markers0. Matching0/held44 persist; no silent normalization.

New test_review_timestamps.py supplies5actual guard/rights/noop/rollback controls; full175/175PASS
150.422s,0fail/error/skip,23freshsourcehashes. Independent static source review and15offline
measurement checks pass; reviewer noDBcalls. Recovery00515/15PASS30.093s/all49tables/security/source
unchanged/2SYNTHETICobjects9896bytes/0realimages; independent target stopped, private volume retained.
Previous execution reports/logs/receipts preserved. Details [[IMP-P1-04_Temporal_Diagnosis]].

Current-run fullreplay acceptance VERIFIED; historical intermittent defect/rootcause/correction
UNRESOLVED. Task/PR8 remain partial-blocked OPEN/DRAFT; no finalreceipt. No runtime fix justified by
missing operands. Next bounded diagnosis needs reproducible exact trace before correction; no
backdating/trigger suppression/tolerance/hosttime change. PR4/6/7 ownerreview remains independent.
Publication checkpoint and resultingHEAD recorded after actual commit/push/readback, not invented.


## Exact source/evidence checkpoint closeout — 2026-11-12

Committed source/evidence checkpoint 571d46fb16fab4a0ae2f8a1395344b61f8f68501 independently verified126/126offline assertions,
0failures. All23testedsource hashes equal Git blobs;27main protected and28priorPR8source/evidence
blobs unchanged. Only new executable is the five-control regression test, reviewed77a2d0f8…86e50930.
Publicreports match raw sanitized results semantically (GitLF normalization only).175/175tests,
005recovery15/15 and004currentfullreplay verified;003strictcomparisonfailure/historical missing
operands remain visible. Independent report SHA256017d98bb406c1a4f19846815d5bda160bd7f1dc37973094ff64e90800ba110b6. Reviewer noDB/Docker/Gitmutation;
parent observed stopped recoverytarget/retainedvolume. Metadata closeout changes no tested code,
schema or execution evidence. Final publicationHEAD belongs in livePR/externalhandoff afterpush.
PR8 remains OPEN/DRAFT/BLOCKED for unresolved historical diagnosis/justifiedfix; no finalreceipt.


## Bounded capture mechanism session — 2026-11-12

Start81305bf1f9933cf870f5aa1edecf4eec887b6ddf, fetchedmain55d39cd unchanged. Preserve verified1479
full import/replay/integrity and allprior175tests/15recovery/receipts; no equivalentcohortreruns.
Plan: implement a diagnostic-only bounded runner in a separate pinned no-network/noports512MiB1CPU
cluster with exclusively SYNTHETIC minimal fixtures. Pin original selection_guard definition,
owner/ACL/security and exact8migration hashes; capture a single comparisonclock at originalsite,
retain identical strictpredicate/error/reviewer/rights checks; enrich safeIDs/timeoperands only.
Verify original-versus-instrumented current/future/rights/auth/deferred outcomes, rollback content
integrity and exactfunction/securityrestore; captrials<=128 and walltime; stopownedtarget afterrun.
No hostclock change, timestampbackdate, runtimefix, trigger/validation relaxation, licensedcohort
replay, pilot/foundation mutation, merge/mainwrite/newrights or receipt. Independent source review
and safe capture selftests must precede any claim of readiness. Synthetic future proof is not a
reproduction of historical23514. Parent owns sharedD1–D9/singleZIP; separate agents review PR4/6/7
and new permissioned research withoutDBwork. GitHubMCPinternalerror observed; publicRESTread-only
fallback verifiesall4OPEN/DRAFT/mergeableheads; PRdescriptionupdate mayremainblocked ifconnectorfails.


## Bounded capture package closeout — 2026-11-13

New capture mechanism verified in one isolated all-SYNTHETIC run on2026-11-12. Code/tests canonical
UTF8-LF hashes e452a2e2…c9259 / afde88c2…46bbd.12offline methods independently pass;62independent
report checks pass. Original/instrumented5verdicts identical, including realguest42501/revokedrights/
deferredcontrary23514. Deliberatefuture control captures actualreview/comparison operands and
86399996416microsecond delta; not historicaldefect.8unforcedpairs capture-4264..-3448microseconds,
0naturalrejections. Checked originalfunction/data/security/fiveapplication-group-role restoration;
owned isolatedtarget stopped/volume retained; separate readonlyresourceattestation confirms bounds.
No Scento import/fullcohort rerun or speculativefix. Previous175tests/15restore/fullreplay evidence
and23sourcehashes remain unchanged; full187method discovery NOT RUN. See [[IMP-P1-04_Bounded_Temporal_Capture]].

Capture mechanism ready for review; historical23514rootcause/correction remainsBLOCKED. Do notrepeat
equivalentprobes withoutnewdiagnosticvalue. Need actual rejectedunforcedpair under reproducible
conditions before runtimefix. All44holds/rights/receipts/persistentpilot preserved. PR4matrixnow
explicitODapprovedbasis vsDMproposals; PR6ready/hashreverified; PR7new3metadata candidates remain
permissionblocked/JPEGunsupported, no acquisition. ExistingGitHubCLI2.97.0 fallback works afterMCP
internalerrors; no login/install/credential extraction/configchange. Samebranches/Draft/no merge.
