---
id: IMP-MATCH-01
project: DoomParfum By TK
type: implementation_task
status: reference-adapter-review-ready
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, matching, adapter, security]
source_of_truth: "../../../README.md"
---

# IMP-MATCH-01 — Read-only matching input adapter

## Current scoped closeout — 2026-11-13

Corrected source checkpoint9be247a5ec724b4c0d057446610b31eacf3bceb2 completed independent review by
/root/pr11_exact_review, distinct from implementer. IR11-01 HIGH stale reused snapshot and IR11-02
MEDIUM malformed DTO findings are both RESOLVED; no remaining source blocker in authorized local
reference scope. Final independent report SHA256
ccc1f3b0561177ef65655792f7f65c19242e924e13dd748cc159ed770c53f0f5.
Actual28/28focused PASS35.5s and157/157full PASS178.812s; independent14offline/6live plus8adversarial
cases verified,22Git source bindings and49pilot/security/application-role manifests unchanged.
[[IMP-MATCH-01_Adapter_Evidence]] preserves all failed probes, RED/GREEN and historical19/148runs.

Ready for Human review of the trusted-local-transport reference adapter and aggregate audit only.
A9truthfully reports1479aggregate capabilities disabled/application reads blocked; it does not
claim per-profile real app evaluation. Keep OPEN/DRAFT; Human Owner decides merge. No individual DM,
closure, normalization, nonadmin catalogue binding, publication or real matching is accepted.
Original migrations/receipts/observations/rights and44holds/matching0 remain unchanged. One scoped
receipt is created only after receipt-preflight documentation checks; final metadata descendants
must preserve independently reviewed runtime/test/proposal hashes. The pending-review/quota text
below records earlier checkpoints and is no longer the current source-review status.

## Independent review and next-gate session — 2026-11-13

Starting PR11 head ff9f840e49d54e511e2cd2ca0e7ad4460c25bb0a; main remains
aa55f8b59acb0872b3b40273a8cdd25198f3ba27. Owner explicitly requests final independent exact-source
review, scoped corrections if needed, refreshed DM/nonadmin/completeness/normalization/rights/
real-data/application gate proposals and consolidated handoff. No proposal acceptance inferred.

Plan: independent reviewer examines pinned adapter/tests plus actual authentication/RLS/provenance
contracts; separate agent revalidates PR9/10 offline source/tests and rights boundaries. Coordinator
alone edits adapter/canonical task/common docs, serializes any disposable PostgreSQL tests under the
common lease, preserves failed attempts and rechecks exact source after corrections. Expected evidence:
independent findings/closeout, reproducible regression controls, source hashes, current PR/head registry,
Markdown/diff/secret checks, D1-D9 and one validated LATEST ZIP. No final receipt while review or scoped
acceptance is pending. Protected: original migrations/receipts, all44holds, source observations/rights,
eligibility flags, persistent pilot and Production. No merge, force push, cloud or real-data ranking.
PR12 tooling worktree/branch is separate and untouched. Existing ContextMode tools are healthy again;
use bounded execute/search for long analysis, native tools for short output/edits; no tool installation.

Independent reviewer confirmed IR11-01 HIGH: an established REPEATABLE READ READ ONLY snapshot
returned a revoked synthetic selected fact; a fresh genuine session uniformly denied it. This is a
documented transport-precondition violation, not a fresh-session RLS bypass or PR8clock rootcause.
IR11-02 MEDIUM: malformed nested DTO/provenance cases were accepted, with an additional513member
boundary inconsistency and internal UUID error-class mismatch. Original failed proofs remain intact.

Parent correction v2 explicitly requests/checks READ COMMITTED READ ONLY and strictly validates
nested keys/types/timestamps/UUIDs/states/layers/bounds. rights usage_scope stays free-form nonempty
text. Seven added offline methods plus two two-session rights/member revocation methods make28tests.
RED14offline methods:8failing methods,34failed assertions/7errors, retained separately. GREEN14/14;
focused28/28PASS35.5s,0failure/error/skip; all49pilot/security/application-role manifests unchanged.
Source SHA256e4b4b761e1bcaa64a1ed0c19372545d232ddf5e7626e58666d4ea76edd97ab1b;
test SHA2560b16716d7b76b1190434d01e7a7d8c26c3454952df0ba8ab0df8da5696ac74e2.
Full157-method regression and final independent corrected-source review remain pending at this
checkpoint. No receipt or acceptance claim. New explicit decision/session/closure proposals are
[[Matching_Owner_Decision_Register]], [[Matching_Nonadmin_Session_and_Publication_Proposal]] and
[[Matching_Data_Readiness_and_Closure_Gates]]; every individual DM remains PROPOSED.

Base/start aa55f8b59acb0872b3b40273a8cdd25198f3ba27; branch codex/imp-match-01-input-adapter.
GateP verified: Owner merged PR4 at this SHA, plusPR5/6/7merged. IndividualDM01–07remainPROPOSED.
Latest explicit owner Post-PR4 request authorizes adapter audit/implementation and isolated tests.
Historical merged plan OPEN/DRAFT/NOTSTARTED sentences are stale snapshots; no numeric/policy
proposal is ACCEPTED by inference. Parent coordinator owns sharedstatus/log/decision updates.

Plan: map actual47table/8migration schema; implement bounded exactUUID profile read using real
nonadmin PostgreSQLsession RLS, active storage/display/automation rights and effective selected
claims. Preserve caller-visible identity/conflicts/provenance; no adminfetch/postfilter. Return typed
known/unknown/incomplete/held/rights/eligibility states; no acceptedclosure/alias/accord/family contract
invented. Allreal1479flagsfalse and44holds remain. No writes, scores, rank endpoint, publicserializer,
cache/UI/framework/provider/authselection, sourceacquisition or SQLmigration. Python is a local
reference adapter using existingruntime, not acceptance of an applicationstack.

Expectedfiles: database/matching_input.py, dedicatedtests/guide/evidence and thisTask. Focusedunit/
SYNTHETICreal-session integration incladminrefusal/otheruser/publicoverlay/revocation/held/unknown/
selectedprovenance. Integration sharesoriginaldisposableDBonly undercommonlease afterPR8regression
window; persistentpilot read-onlyaggregate audit separated fromadapter and neverpublishedraw.
Independentreview beforeDraftPRreadiness; preserveallmigrations/receipts/oldreports. NoProduction/main
mutation/merge/eligibilityflip/dedup. Application/API/realranking remainsgated byDM/data/authdecisions.

## Verified implementation checkpoint — 2026-11-13

Local reference adapter and tests implemented without modifying original migrations/code/rights.
Focused19/19PASS23.516s; full main-plus-adapter148/148PASS187.078s,0failures/errors/skips.
22executed source/migration hashes and all49pilot data/security/application-role manifests verified.
Prior failed focused/full attempts and wrapper corrections remain visible in
[[IMP-MATCH-01_Adapter_Evidence]]. Source adapter SHA256
a33fb8a7ed555a240fb0fd94ac534fc97ec13cc04a57f0bc8f583de5f1ceec46.

Read-only operator aggregate confirms1479private/1435approved/44held/matching0, selected note claims
1348perpyramid layer/87general,0aliases/accord/family/comparison/image links. No accepted closure or
approved genuine nonadmin owner-session binding; per-profile Scento application evaluation remains
blocked rather than using an administrator fallback. Public-provenance ordinary-runtime visibility
also remains a policy gap. No source values/rows/counts are published through an API.

Independent prototype review findings addressed; final exact-source independent review remains
NOT COMPLETE due reviewer usage limit (retry07:12local). Keep Draft, ACCEPTANCE PENDING, no final
receipt. [[Post_PR4_Application_Readiness]] records individual DM proposals, stack/auth gaps and
IMP-MATCH-05/06/07dependencies. Coordinator additively updates nine common planning/status/log notes;
all original histories/decision rows/immutable receipts preserved. Draft URL and source checkpoint
are recorded after publication; no merge or Production mutation.

Published source checkpoint715c398e9aa3b2eb25bfc629d4f15da79ab9cda3 in
[Draft PR11](https://github.com/kraveerachat/DoomParfum-By-TK/pull/11), verified OPEN/DRAFT.
No final receipt: acceptance still pending independent exact-source review and the separate data/
authorization gates. Final metadata updates only task/log/check records; all22executed code/migration
hashes remain bound to this checkpoint. Exact17-file manifest and13Markdown/12frontmatter/197wiki/
4local-link checks,47logical-table parity and30protected blobs:0errors/common-secret candidates.
PR9/10 have no changed-path overlap with this task; PR8 shares only3common Markdown histories.
Possible three-way documentation conflicts must be reconciled after whichever Owner merge occurs,
preserving both histories; no cross-PR source conflict or automatic merge is authorized.

Closeout tool preference event: installed Caveman skill read/applied for concise chat, without
installation/config changes. ContextMode exposes only ctx_doctor; actual health call failed
Transport closed, no diagnostic table or execution/search tool available. Bounded native fallback
continues; Agent_Run_Log records exact outcome. No code/test/schema/rights changes or rerun required.


## Scoped immutable receipt event — 2026-11-13T10:35:04.104547+07:00

One new [[2026-11-13_103504_IMP-MATCH-01_Read_Only_Input_Adapter]] receipt created after independent review and pre-receipt doc checks.
No previous receipt amended. Scope is local reference adapter/aggregate audit only; all real-data
session/closure/DM/publication gates remain separate. Receipt-inclusive checks and final Git head
are recorded in current evidence/PR/external registry after publication.

## Post-merge Waves 0–2 — 2026-11-13

Owner mergedPR11 ata2d17b6c336b69e312d7e1e4e559a123bd3f8332; reviewedheadd267118b1afc27dec22fa8dcd52853a1994b356a. Prior scoped receipt unchanged. Fresh14offline methods passed in Wave0; prior28focused/157full and independentlive tests are HISTORICAL / NOT RERUN. Nonadmin real-catalogue binding,closure,selected rights and eligibility remain gated; no API or ranking activation.
