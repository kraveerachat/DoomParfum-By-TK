---
id: DPT-DOC-002-DATA-CONTRACT
project: DoomParfum By TK
type: proposed_transition_contract
status: proposed
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, normalization, closure, provenance, rollback]
source_of_truth: "../../README.md"
---

# Normalization, closure and materialization transition contract

This is Workstream C preparation under the Post-PR13–17 prompt. No policy, schema, SQL, observation,
selection, materialization, hold or eligibility changes occur. [[Post_Merge_Data_Readiness_Matrices]],
[[Matching_Data_Readiness_and_Closure_Gates]] and [[Matching_Nonadmin_Session_and_Publication_Proposal]]
remain the source of existing facts and proposed gates. This supplement specifies how a future
accepted choice must move safely between those stages; it does not repeat or approve the old queue.

## Observed inventory and exact review sets

Fresh operator aggregate audit at2026-11-13T15:10:10.679095Z:1,479 private profiles,1,435 approved,
44 held,matching eligibility0;160brands,420notes,11,972links. All49table/security/role fingerprints
match before/after and the previous audit. No actual application principal can be inferred from an
operator query. Canonical accord/family/image/pair/listing/price availability remains0. Source
three-column/list shape and raw family/country claims are not selected completeness assertions.

Re-executed frozen offline review accounting:34/34checks,44 exact held profiles,43 proposed
duplicate-membership sidecars,44 repeated groups and45 extra occurrences. The matrix bytes remain
SHA256`443b7212817b405deda2b75cbbf11f99ef985bca26fba7c4e0f43fc4804b8193`. Candidate/reviewer/rights
queues each have64 mixed-unit entries(44profiles+15media+5pairs); reviewers remain unassigned.
Exact row-level inventory/ordinals/source hashes stay in the existing ignored local matrix and
local Master Handoff evidence. No private rows are copied into this public document.

The43 projections comprise39layered and4general profiles. Khamrah is the remaining separate
structured/prose conflict. Neither generic deduplication nor a larger vote can resolve it. The
database's0conflict rows do not close the external conflict or release any of44holds.

## Four independent approvals

| Boundary | Exact decision required | What it does not approve |
|---|---|---|
| Projection | OP03 versioned within-domain repeated-membership policy and reviewer mapping | source rewrite, intensity, cross-layer collapse, closure or hold release |
| Closure | OP02 accepted complete-as-reported assertion for exact source/edition/domain | chemical completeness, perception completeness, other layers or future captures |
| Canonical selection | OP04 permitted field/use, reviewed mapping and conflict/lineage contract | public publication, a different source/asset grant or application ownership |
| Application eligibility | OP05/06 genuine nonadmin binding plus accepted method/domain/use requirements | operator impersonation, blanket access, all-method eligibility or public ranking |

Approval of one row does not select another. Record actual Owner/date/reference/scope/version,
and merge any required Planning Amendment before implementation. No assertion is accepted here.

## Proposed domain assertion, not an existing table

A future design must bind each assertion to the entity and exact edition certainty, access scope,
source record/capture identity, source revision/content hash, observation/field and section locator,
canonical vocabulary/mapping/transform version, declared layer/domain, accepted member set, reviewer,
review time, evidence and rights version. Its identity must distinguish new captures and decisions.
This is a conceptual contract; no closure table or schema fields are claimed to exist in current SQL.

Suggested states remain PROPOSED: UNKNOWN; REPORTED_MEMBERS_ONLY; COMPLETE_AS_REPORTED; WITHHELD.
Empty/null/omitted source values start UNKNOWN unless exact usable evidence and accepted policy
support a complete empty domain. A source-provided list is not automatically complete-as-reported.
Exact-layer absence requires that layer's accepted closure. Any-layer absence requires all searched
domains closed under the method's accepted domain mask. Presence in one layer does not prove absence
elsewhere. A later capture, changed selection, vocabulary, conflict or grant invalidates the old
assertion's applicability; retain the old event as history rather than silently extending it.

Complete empty domains still need explicit comparability/zero-denominator rules in the selected
method. Unknown must remain distinguishable from an accepted empty set and numeric0 in DTOs/results.

## Future transition and transaction specification

1. **Freeze a review manifest.** Pin the exact source files/captures, all original arrays/strings/
   ordinals, hold membership, mapping/vocabulary, sidecar and policy version, permissions, baseline
   catalogue/security/roles, and reviewer authority. Reject drift before preparing a write plan.
2. **Review membership.** Within an accepted layer/domain, reference every original occurrence that
   supports a proposed canonical membership. Preserve Top and Base occurrences independently. Do
   not fuzzy-map ambiguous aliases or derive intensity from occurrence count/order.
3. **Create new derived claims only if authorized.** Use a new transform/version and field/section
   locator with complete source lineage. Never UPDATE/DELETE immutable source observations or raw
   captures to make a unique set appear source-original. Do not reuse an old observation identity
   for a different meaning or merge editions by name.
4. **Plan conflict handling separately.** Khamrah requires permissioned independent exact-edition,
   structured/prose field evidence and a recorded reviewer resolution. A duplicate policy has no
   authority to choose between contradictory source claims.
5. **Atomic selection/materialization.** In an approved local implementation, recheck reviewer,
   source/field/scope/rights, relevant conflicts and expected source/selection versions before a
   derived selection and its materialization change together. Preserve FK, deferred end-transaction
   checks, immutable audit history and genuine identity. A failed invariant rolls back the whole
   proposed unit; do not leave partially selected notes or orphaned derived claims.
6. **Separate closure and hold decisions.** A successful projection or SQL commit does not assert
   completeness, resolve a hold or change matching eligibility. Each requires its separately
   accepted evidence and bounded task. Do not promote1,435approved records en masse by review state.
7. **Replay and concurrent review.** Bind idempotency to the exact capture/claim/transform/decision
   version. Same input replay adds0new source/canonical records. Two reviewers using stale expected
   versions must not both overwrite the same decision silently. Specify deterministic locking or
   equivalent reviewed conflict behavior in implementation; no lock strategy is installed here.
8. **Rollback/reversal.** Before commit, rollback restores exact data/security/role fingerprints.
   After commit, use an authorized new reversal/selection event and revalidate materialization;
   do not erase audit history or immutable original claims. Rights revocation is never undone by
   restore/replay. Retain withheld artifacts and invalidate dependent eligibility/results.

The existing operator-private ownership is immutable. Copying a public catalogue identifier does
not make its private source/derived claims public. A new clean application-private pilot or auth
model amendment needs its own Owner approval/security review; this contract creates neither.

## Required negative, concurrency and rollback specifications — NOT RUN

| Case | Required future assertion |
|---|---|
| NC01 | unknown/omitted/null list never becomes complete-empty or satisfies strict exclusion |
| NC02 | an accepted layer assertion cannot prove any-layer absence when another searched domain is unknown |
| NC03 | repeated source tokens retain every ordinal; one versioned within-layer membership does not imply strength |
| NC04 | same note in Top and Base stays in both domains; cross-layer collapse requires a separate named projection |
| NC05 | ambiguous aliases, mixed editions or a changed vocabulary cannot reuse an old closure/selection |
| NC06 | Khamrah conflict remains held under duplicate-only normalization; no majority/newest-source shortcut |
| NC07 | unrelated/expired/revoked/unknown source or asset permissions fail before selection/materialization/use |
| NC08 | another tenant, forged reviewer, admin impersonation or immutable-owner rewrite fails without count leakage |
| NC09 | a change to source hash/capture/selection/conflict between review and commit aborts rather than uses stale approval |
| NC10 | conflicting concurrent review decisions produce the accepted deterministic conflict outcome, not lost updates |
| NC11 | derived-claim identity collision, foreign lineage, field mismatch and partial materialization fail deferred checks |
| NC12 | same versioned replay adds0new canonical/source rows; intentionally changed input creates new reviewed lineage |
| NC13 | a forced mid-unit failure/ROLLBACK leaves catalogue/security/roles and all44holds/eligibility exactly unchanged |
| NC14 | a permitted compensating reversal preserves original source/audit evidence and invalidates dependent outputs |
| NC15 | restoring an older backup cannot reactivate revoked rights, stale closure or old eligible/public results |

No case above was implemented or executed by this documentation task. Existing55offline methods
and34offline evidence checks are separate actual results, not these future SQL/RLS test passes.

## Next reviewable task boundaries

READY NOW: evidence review, source hashes, proposed assertions/golden cases and permission dossiers.
AFTER OWNER DECISION + applicable Gate: exact versioned projection/closure design and synthetic tests.
AFTER SOURCE RIGHTS: permissioned conflict samples and source/asset intake in separately bounded tasks.
AFTER AUTH APPROVAL: a clean application-private pilot or accepted identity amendment, then genuine
nonadmin access tests. BLOCKED: real matching/promotion, unrestricted/public API/UI and PR8correction
without its new causal evidence. No migration file or ETL/scoring runtime is authorized by this note.
