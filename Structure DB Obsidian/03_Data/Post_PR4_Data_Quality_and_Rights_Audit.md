---
id: DPT-DATA-002-REPORT
project: DoomParfum By TK
type: research_evidence
status: review-pending
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, research, normalization, rights]
source_of_truth: "../../README.md"
---

# Post-PR4 research reconciliation and proposed normalization

Base main aa55f8b59acb0872b3b40273a8cdd25198f3ba27 includes Owner-merged PR4/6/7.
Planning merge does not accept DM choices or this normalization policy. The current explicit Owner
request authorizes offline research preparation. [[DPT-DATA-002_Post_PR4_Data_Quality]] tracks the task.
Original [[Post_PR5_Held_and_Permission_Review]], [[Bounded_Note_Media_Candidate_Increment]], sources,
all44held profiles and previous receipts remain unchanged.

## Brand/source identity reconciliation

The offline audit retains226research rows (220seed+6new),160pinned Scento houses and21existing
identity-conflict rows. The current conservative NFKC+lower exact text suggests publisher-house/
deterministic imported-brand ID targets for92candidate primary labels;134have no exact suggestion.
No explicit alias string generates a new exact suggestion in this pass. No identity is accepted.

All97previous publisher crosswalk claims are retained. The historical normalizer stripped accents/
punctuation, giving93literal+4lexical-alias candidates; current92exact-primary results are a different
rule, not a correction of97identities. Dolce & Gabbana literal spacing/punctuation accounts for one;
Maison Margiela, Initio, Zoologist and Comme des Garçons Parfums remain prior alias-review proposals.
No prior claim is silently discarded. Raw candidate aliases, parent/related relationships, country,
positioning and intended catalogue role are retained separately from each publisher claim. Shared
publisher, name similarity or differing country strings cannot establish identity/parenthood.

Canonical UUIDs are targets derived from the merged deterministic importer and pinned source IDs,
not newly queried database identities. This lane performs0DBcalls and approves0semantic merges.

## Proposed policy DPT-NOTE-MEMBERSHIP-PROPOSAL-1

All43repeated-list holds are represented externally with source URL/revision, parsed-field hash,
logical CSV record ordinal, exact original note strings, selected lists and every labelled occurrence
ordinal.44repeated groups/45extra occurrences remain visible;39profiles have layered repetitions and
4general-list profiles have5extras. Same note in different layers is never collapsed across layers.

The sidecar proposes one material membership per layer while linking all original occurrences. It
creates no observation, selection, note association or canonical record. Every membership is
accepted=false; policy=PROPOSED_NOT_APPROVED, completeness=UNKNOWN, hold=UNCHANGED. No absent-note
or matching-eligibility inference is possible. Unknown or ambiguous material identity rejects the
proposal rather than choosing a convenient ID.

Khamrah has no duplicate-list normalization proposal: its independent field/section claims remain
unresolved and require permissioned evidence. It is not unioned, renamed or promoted by this policy.
The old hash-bound canonical mapping is not rewritten.

Recommended decision: retain all44holds now; review the sidecar as a candidate transformation only.
Before any future application, Owner must decide whether repetition is redundant membership or
meaningful publisher intent, approve exact transform scope/version, require independent source-bound
mapping review, preserve immutable original occurrence claims, and run SQL/FK/uniqueness/conflict/
rights/rollback tests with new precise derived locators. Separate completeness/absence and matching
eligibility review remains required. This research proposal accepts none of those decisions.

## All15media candidates audited, no acquisition

The retained historical RESEARCH46 vocabulary has15candidate metadata rows, not58P1pilot/420full-note
coverage or15display grants.14filenames end in JPEG extensions and1in PNG; these are source filename
hints, not actual decoded content. No SVG is present; a synthetic SVG negative confirms it remains
unsupported. Current static-PNG limits are unchanged.

Only the3recent candidates have recorded dimension metadata;2reported pixel products exceed
4000000and12candidates have no recorded dimensions in this input set. The1PNG-named candidate is not
approved or byte-validated. All15downloaded-file hashes are absent; original MIME/dimensions/size/
contents, visual subject and ownership remain unverified by this offline audit. Existing source
reported SHA1 and license/creator/attribution/derivative annotations are preserved, never substituted
for acquired-byte SHA256 or proof of permission.

All operations remain UNKNOWN_NOT_APPROVED_BLOCKED: automate/cache/store/display/transform/AI/
commercial/redistribute/retain. License alternatives and derivative obligations remain separate.
No fresh web request or ownership/legal conclusion is made. The3recorded immutable-revision fetch
failures remain NOT_VERIFIED; current-page observations do not authenticate those snapshots.
Asset bytes/acquisition/display approvals/new source or image grants=0.

## Progressive indexing and pairwise evidence

A1479source-profile enrichment index preserves source IDs/revision/URL/parsed-field hashes and
reported representation: only this pinned local export, not global perfume-model discovery. Its
no-activation state is a research authorization statement, not a fresh DB eligibility read. It
requires selected-field/domain completeness, explicit eligibility, permissioned accord/family/
alias/currentness facts where needed, per-asset rights and permitted direct evidence before use.
All12448selected-list note occurrences reconcile; source strings and licensed files are unchanged.

Five existing publisher inspiration leads remain blocked in two publisher grouping IDs. This is
not two independent sensory sources, five usable relations or any verified Dupe. Exact pair/edition,
source-field-use permissions, permitted independent comparison/opposition evidence and explicit review
are queued separately. No note-overlap percentage, fabricated relation or full-world completeness claim.

## Evidence and safety

[Offline audit guide](../../database/RESEARCH_AUDIT.md) and
[sanitized results](../../database/evidence/research_audit_results.json).
External outputs:08_OUTPUTS_APPROVED/post_PR4/research/audit_003 and audit_004_replay.
Eight output files are byte-identical across both runs.17synthetic offline methods pass; source/
input hashes are frozen and checked before publication. Existing brand/media manifests and six pinned
Scento artifact identities pass. Early001/002runs remain explicitly superseded projection-label
evidence; no input/canonical mutation occurred. No shared DB regression or live-origin/image tests.

Scento attribution, revision and CC BY4.0 link/change notice are in each summary. Row-level/private
arrays, candidates and queues stay outside public Git. This branch contains only code, synthetic
tests and sanitized summaries. Shared logs/status/decision integration and D1-D9/ZIP are coordinator
owned. See [[DPT-DATA-002_Research_Evidence]] for exact source/replay/testing evidence.
