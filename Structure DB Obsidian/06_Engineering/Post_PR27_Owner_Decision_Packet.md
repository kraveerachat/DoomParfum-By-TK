---
id: DPT-PLAN-009-OWNER-PACKET
project: DoomParfum By TK
type: owner_decision_packet
status: proposed
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, decisions, gates, rights, security]
source_of_truth: "../../README.md"
---

# Post-PR27 consolidated Owner decision packet

Packet version: **POST27-ODP-1**. Planning task: [[DPT-PLAN-009_Post_PR27_Next_Wave]]. This packet is a proposal, not an Owner response. The exact file SHA-256 is recorded in the verification evidence after the final file is frozen. Do not edit an accepted packet in place or infer acceptance from a Planning PR merge.

The exact proposed data contract is `ENR-PINNED-SCENTO-1 revision 1`, transform `enr-pinned-scento-preview-1`, schema `enr-pinned-scento-preview-schema-1`, in [[Post_PR27_Data_Readiness_and_Pilot]], SHA-256 `053a7583d33beaa103e4cb94781991504aa6eee4b380fefe7cc1d2095f2c71d5`. Its five input records expose 46 allowlisted review slots, not 46 additional source records. A/B/I approval must bind this exact proposal as well as this packet; material changes require a new version/hash and acceptance.

In the media lane, this packet's `E-VERIFY-ONLY` corresponds to the note's metadata/rights-verification-only recommendation; neither identifier authorizes image-byte intake.

## Already approved and what remains open

| Register row | Verified authority at main `8eef8f13265adc14db0cae82ff77cfc4863853ce` | Residual approval status |
|---|---|---|
| OD-01 / pinned Scento | CC BY 4.0 pinned local pilot with attribution, under the recorded original scope | New mapping fields/tasks, wider source uses and other publishers are not approved by that license alone |
| DM-01 / OP01 | Separate exact synthetic M1 and B1 implementation units were explicitly approved and Owner-merged through PR26/27 | Full Mode A, B2 and wider feature milestones remain PROPOSED or deferred |
| DM-02 | Separate Fit, Data Confidence and pair evidence is an explicit Owner constraint; no scientific smell percentage | Wider confidence/freshness/banding/display policy remains PROPOSED |
| DM-03 | M1-NL-TYPED-1, SHA-256 `a57f4c56e1068a3d86a99e562b31e5c3923e2d369cb4e812c1dd5f5550a5ada3`, exact notes-only synthetic method/config | Full Mode A 50/30/20 components and real-source use are not accepted by M1 |
| DM-04 | No compatible real accord strengths established by this wave | Taxonomy, observed strength scale and any presence fallback remain PROPOSED; B2 BLOCKED |
| DM-05 | B1-PD-TYPED-1 revision 2, SHA-256 `77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977`; exact synthetic Coverage 4/5 + Focus 1/5 | Real-source closure, exclusions and actual catalogue eligibility remain separately gated |
| DM-06 | Preserve current/unknown/historical distinctions | Lifecycle/freshness/market thresholds remain PROPOSED; release year is not availability |
| DM-07 / OP05 / OP06 | Private-first and genuine nonadmin boundaries constrain planning | Exact application identity, stack, sessions, transport/cache/publication and deployment remain PROPOSED |
| OP02 | Only accepted synthetic fixture/domain completeness exists for the scorers | Real-list completeness and absence policy remain PROPOSED; current assertions UNKNOWN |
| OP03 | Original occurrences, Khamrah conflicts, 43 proposals and all 44 holds must be preserved | No normalization promotion, conflict winner or hold release accepted |
| OP04 | Selected-field provenance and active use-specific rights must independently pass | Per-field/app/media use and exact eligibility are not established by catalogue visibility |
| OD-03 / OD-05 | Original disposable local PostgreSQL pilot and local backup/restore testing authority | No new database work in this wave; cloud/provider/retention/RPO/RTO/external backup choices remain deferred |

Historical PROPOSED/NOT APPROVED snapshots remain dated history. The separate exact M1/B1 acceptances supersede only their own earlier synthetic proposals. Existing wider DM/OP cells are not silently converted to ACCEPTED.

## Exact proposed choices A–I

All nine rows currently have **OWNER STATUS: PROPOSED / UNANSWERED**. UNKNOWN facts and external-permission blockers are explicitly listed; a source URL or Owner design approval cannot supply a licensor grant.

| Row | Recommended choice and exact scope | Alternative | Benefit / risk | Prerequisites and acceptance |
|---|---|---|---|---|
| A — first data pilot | `A-PREVIEW-5`: ENR-PINNED-SCENTO-1, exactly afnan-9-am, afnan-9-am-dive, house afnan, materials mint/bergamot from the pinned CSV revision; five records maximum, local unselected candidate preview only | `A-DEFER`: no mapping runtime | Small auditable field/provenance unit; source identity and taxonomy may remain unverified | Exact A-note fields/claim types/transform version, B/I answer and merged plan; fifth/sixth-record bounds, altered pins, replay/rollback and no-source/DB-write controls |
| B — selected fields and rights | `B-PINNED-PREVIEW`: approve only the A note's explicit raw-field allowlist and unselected candidate claim types under the pinned local CC BY 4.0 attribution contract | `B-NARROW`: Owner supplies a smaller exact field list; or defer | Reuse existing permitted bytes; a source URL does not license linked pages/images and a preview is not a selection | File/source/field/revision/ordinal binding, notices and transform log; reject extra source/field/use, inferred strength, canonical selection or redistribution; current canonical selection/eligibility NOT VERIFIED |
| C — real completeness/absence | `C-UNKNOWN-UNTIL-ASSERTED`: design target requires explicit reviewed source/capture/edition/domain/version closure before absence/exclusion; preserve unknowns and general-only notes | `C-DEFER-ABSENCE`: do not implement absence-sensitive real matching | Prevents false negative/exclusion passes; many real inputs will remain unavailable | Separate exact real-source assertion schema/reviewer contract and tests for missing/incomplete/empty/conflicting domains; no current closure assertion or eligibility is created |
| D — normalization and held records | `D-DEFER-PROMOTION`: retain all 43 proposals and 44 holds, including independent Khamrah conflicts; allow only separately bounded reviewer dossier planning | `D-REVIEW-PACKET`: later name exact records/version/reviewer for a review-only task; no promotion by this answer | Preserves evidence and prevents silent deduplication; usable coverage remains limited | Explicit per-claim reviewer outcomes and accepted transition contract before any later mutation; occurrences/provenance unchanged and held input denied; no hold release requested |
| E — two-PNG sample | `E-VERIFY-ONLY`: evaluate exactly B1-MEDIA-021 BergamotEssOil.png and B1-MEDIA-022 Ginger.png against retained evidence and the proposed intake checklist; no download authority yet | `E-DEFER`; later distinct exact conditional intake request after rights gaps close | Two bounded candidates; actual original-file identity, rights-holder authority and PNG features remain NOT VERIFIED | Per-file creator/license/source/file-version/use evidence; actual download requires separate explicit intake approval and implementation task; binary/SHA-256/PNG tests remain NOT RUN now |
| F — media use/storage/display | `F-PRIVATE-ORIGINAL-DESIGN`: architecture target is immutable original-only local files with scoped DB metadata, attribution, quarantine and authorization; all acquisitions/displays still gated per asset | `F-METADATA-ONLY`: retain references/placeholders only | Keeps lineage and private overlays; storage/display/backup/retention cannot be inferred from public URLs | Exact per-file acquire/store/private-display/backup/retention terms and authority must be answered before intake; derivatives/public redistribution/remote delivery are excluded; rights/expiry/revocation/restore controls required |
| G — application stack | `G-PYTHON-TARGET`: recommend local Python as a future service target to reuse reviewed scorers; retain current CLI-only runtime until its own contract/task is accepted | `G-CLI`: remain CLI; or `G-TYPESCRIPT`: separate backend/port design with parity proof | Python avoids duplicate scoring implementations; service/auth/transport maintenance and security remain new work | ADR choice is design-only; no framework install, endpoint/UI, ORM/vendor/cloud selection; later explicit auth/transport/budget/testing contract and implementation gate |
| H — genuine nonadmin session | `H-CLEAN-PILOT-DESIGN`: future separately approved clean application-private scope with genuine nonadmin identity established before any authorized intake | `H-AMEND`: separately review a revocable binding-model amendment; or `H-DEFER` | Avoids rewriting immutable operator ownership; requires new exact roles/intake/provenance and effective-privilege proof | No SET ROLE/GUC/header identity, superuser impersonation or curator workaround; owner/other-user/shared/revoked/admin/pool/read-only/rights tests; no role/schema/data mutation authorized by design selection |
| I — first future implementation | `I-IMP-ENR-01`: implement only the A/B-approved five-record offline preview, after this Planning PR merge and exact proposed preview contract acceptance | `I-DEFER`: continue planning/rights review only | Independent of application/media gates; does not create a usable real matching catalogue | TDD or appropriate contract-first tests for the new runtime, focused negatives/regression/independent review and one Draft Implementation PR; no API/UI/DB/image/source acquisition/normalization/holds/eligibility changes |

## Paste-ready Owner answer

Reply with the packet version and its verification-record SHA-256, then a choice and exact scope for each row. Partial approval is valid: unanswered/deferred rows continue to block only their dependent work. Recommended choices are not preselected acceptance. The statements below are proposed wording for a future Owner reply, not approvals recorded by this document.

```text
Packet: POST27-ODP-1
Packet SHA-256: <copy exact frozen hash from DPT-PLAN-009 verification evidence>

A: A-PREVIEW-5 / A-DEFER
If A-PREVIEW-5: approve only the five source records and exact proposed field/claim/transform
contract in Post_PR27_Data_Readiness_and_Pilot, for a local unselected preview; no DB/import.

B: B-PINNED-PREVIEW / B-NARROW(<exact field list>) / DEFER
Approve only specified pinned CC BY 4.0 local field use and attribution. This grants no
linked-page/image acquisition, canonical selection, publication or new source permission.

C: C-UNKNOWN-UNTIL-ASSERTED / C-DEFER-ABSENCE
Design approval only; no real source becomes complete/absent/eligible by this response.

D: D-DEFER-PROMOTION / D-REVIEW-PACKET(<exact future review scope>)
No normalization, conflict winner, original-observation rewrite or 44-hold release.

E: E-VERIFY-ONLY / E-DEFER
Exactly the two named retained PNG candidates; no image-byte retrieval in this approval.

F: F-PRIVATE-ORIGINAL-DESIGN / F-METADATA-ONLY / DEFER
Design approval only. Per-asset permission, allowed use, retention and exact intake approval
remain required before any bytes, storage/display operation or implementation.

G: G-PYTHON-TARGET / G-CLI / G-TYPESCRIPT / DEFER
Design target only; no framework install, API/UI, authentication or public deployment.

H: H-CLEAN-PILOT-DESIGN / H-AMEND / H-DEFER
Design path only; exact principal/privilege/scope/rights/intake contract and separate task
must be approved before any role, schema or database operation.

I: I-IMP-ENR-01 / I-DEFER
Only after merged planning authority and exact A/B/preview-contract acceptance:
five-record offline unselected preview in its own branch/Draft PR, with no DB, new source/
image acquisition, real ranking, API/UI, normalization, hold or eligibility change.

Date/time and Owner reference: <Owner supplied>
No Production mutation. No automatic PR merge. All other gates remain unchanged.
```

If choices change the five IDs, fields, transform semantics, rights/use boundary or proposed future implementation scope, revise and hash the affected exact contract before asking for implementation acceptance. Approval of this consolidation alone is not that exact acceptance.

## External-permission and verification boundaries

- Regional publisher automation/storage/display/update rights: **REQUIRES EXTERNAL PERMISSION** where existing terms do not grant the exact operation. No request was sent; bot restrictions and failed terms retrieval remain recorded, not bypassed.
- Media creator/rights-holder authority, exact original bytes and all other rights: **NOT VERIFIED / INTAKE BLOCKED**. The two PNGs are conditional source assertions; the public URL grants no project operation by itself.
- Current DB counts, roles, scope ownership, active rights and catalogue matching eligibility: **NOT VERIFIED**, because Docker engine is unavailable. Historical counts remain historical.
- M1/B1 pure typed synthetic contracts: **ALREADY APPROVED AND OWNER-MERGED**. They do not authorize a real-data wrapper, source promotion, fabricated fixture identity or application access.
- PR8: **BLOCKED**, unchanged; no equivalent temporal experiment or speculative guard correction is authorized here.

See [[Post_PR27_Consolidated_Next_Wave_Plan]], the three lane notes and [[DPT-PLAN-009_Post_PR27_Verification]] for actual evidence and NOT RUN tests.
