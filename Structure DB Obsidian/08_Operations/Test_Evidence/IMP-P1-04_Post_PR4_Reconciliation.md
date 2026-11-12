---
id: DPT-EVD-P104-POST-PR4
project: DoomParfum By TK
type: test_evidence
status: merge-reconciled-diagnosis-blocked
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, reliability, reconciliation]
source_of_truth: "../../../README.md"
---

# PR8 after Owner merges PR4/6/7

## Scope and actual Git events

Start6f6b856f1f85395df4d8ae8d48b71080e1181a2e. OwnermergedPR6bc90db423349e13f243524154d64f0b264865050,
PR7cbc8720c547b76fe5e0bd9b93c3cbf54678b4c2a and PR4aa55f8b59acb0872b3b40273a8cdd25198f3ba27.
Newsessionnote65606483af453c4ef98f410f25e5ef876db7d588 precedesnonrewriting two-parentbranchmerge
fd9360650a43d8251c97c706a4811a295dad977b (parents65606483 +aa55f8b). This mergesmainINTOthetask
branch, notPR8intomain; no rebase/forcepush/mainwrite/automaticPRmerge.

Exactly3contentconflicts were append-only Markdown histories inProject_Status/Agent_Run_Log/
Change_Log. Bothsides' completeconflictblocks concatenate. An independentline-preservationoracle
checks every nonblankhistorical line frombothparents remains, excludingcurrentfrontmatterdate.
Newcurrentnotice supersedes historicalDraftwording; no oldreceipt is rewritten.
Allremainingmainchanges apply throughGit, including PNGimplementation andmatching/researchdocs.
No database source or test file was manually edited.

## Source and evidence preservation

86checks bind25priorPR8sources andprotectedmigration/receipt/priorDBsource/evidenceblobs;20merged
imageexecution bindings also matchcurrentworkingfiles. Fullsuite28sourcehashes matchGitblobs.
Original eightmigrations, selectionguard, importer, RLS/permissions/rights, futuretimestampcheck,
oldreports andall siximmutable receipts preserved. Main'smatchingplanstillhasPROPOSEDDM01–07;
Ownermerge provesPlanningGateP, notautomaticnumeric/absence/stackpolicy acceptance.

[Mergeaudit](../../../database/evidence/post_pr4_merge_reconciliation.json),
[combinedregression](../../../database/evidence/post_pr4_merge_regression_results.json).

## Actual combined regression

Command python .local/post-pr4-reliability/run_combined_regression.py callsverify_capacity.run_suite()
under thecommonGit-rootexclusivelease. The ignoredwrapper hasSHA256inthenewreport; it preserves
publiccapacitytest/schema reports andprivatelogs/failurefiles byte-exact afterrun.
218/218methodsPASS188.093s,0fail/error/skip;218discoveredmethodIDs and28sourcehashes recorded.
This exercises the newlycombinedmainimagecode andPR8tooling, ratherthan repeatingan equivalent
timestamp/benchmarkexperiment. Onlydisposable schema_test/scento_test/migration_probe targets
used byexistingtests; persistentpilot isreadonly. Before/aftercompletepilotfingerprint matches:
all49tablemanifests/security/fiveapplication-group-role definitions unchanged.
DBleasewindowreleasedtoparent afterverification. Newmatchingadapter/scorers/API/UI not partofthissuite.

## Reliability stop line

Previousfull1479fresh/replay/inventory, original003strictstaginghashfailure,004exact44updated_at
bookkeepingproof, recovery00515controls andboundedcapture remainvalidseparateevidence.
The deliberatefutureSYNTHETICselftest isnot a naturalhistoricalreproduction. Actualpreviousfailed
operands remainunavailable. Mainmergesaddimagecode/docs withoutchangingguard/ETL/timeconditions;
no genuinelynewclockreproductioncondition demonstrated, so no capture/clock/fullreplay/recovery
experiment is repeated here. No backdate, timestampreplacement, blindretry orvalidationrelaxation.

PR8 remainsOPEN/DRAFT/BLOCKED forhistoricalrootcause/justifiedcorrection, despitepassedcurrentreplay
andcombinedregression. No newfinalreceipt. Nextnewdiagnosticquestion must yieldactualrejected
unforcedoperands underreproducibleisolatedconditions before runtimefix. No sourcegrant, heldprofile
change, Production/cloud mutation or realmatchingactivation. Parent exactreview/readback follows.
