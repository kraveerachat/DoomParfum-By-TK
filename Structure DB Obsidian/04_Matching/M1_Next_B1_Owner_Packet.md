---
id: M1-NEXT-B1-OWNER-PACKET
project: DoomParfum By TK
type: local_owner_decision_draft
status: proposed-not-accepted
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, matching, synthetic, b1, owner-decisions]
source_of_truth: "../../README.md"
---

# Next separate B1 task — Owner decision packet

Packet reference: **B1-OWNER-PACKET-1**. This is a local, untracked preparation draft in the detached
main checkout at `0da217671ec6473716eea5947f013d44e6fd91cb`. It does not allocate an implementation
branch, select a runtime configuration, create a PR or record Owner acceptance. The coordinator
verified Owner merges of PR22–25; those merges do not select the exact proposals below.

The requested first implementation milestone concerns `mc-a-notes-layered-p1` only. This packet
prepares the existing separate B1 task, **IMP-MATCH-03**, without adding B1 code to that M1 task.
An M1 approval must not be read as approval of B1's proposed 80/20 formula, query normalization,
hard-rule or domain-completeness choices. Independent synthetic work does not require new source,
image, application-session or real-catalogue permissions; its inputs must remain synthetic.

## Normative proposal references and unchanged behavior

Use the existing merged proposal unchanged unless the Owner explicitly modifies it:

- [[Matching_Method_Contracts_and_Golden_Cases]], `mc-b1-pyramid-positive-domain-p1`, shared
  input/result rules, B1 gate/denominator rules, MC-B01–MC-B15 and rounding/boundedness sections.
  Canonical Git SHA-256: `f09999add47c820dab0ccb96db0ed0876b80f92a05f198237201ef39187158a8`.
- [[Synthetic_Implementation_Unlock_Checklist]], B1 second-answer and unresolved typed-boundary
  sections. Canonical Git SHA-256:
  `fb6d181e0348f6860e06873a55ded801e3e30ba447dd01d5223235c27defff96`.

These are canonical Git LF hashes, not raw Windows checkout-byte hashes. This packet summarizes
the existing proposal and exposes the remaining binding choices; it does not replace the merged
golden table or silently create a new scoring method.

## Exact existing B1 choice for the Owner

**Recommended selection, still PROPOSED:** `mc-b1-pyramid-positive-domain-p1`, synthetic-only, as
the separate IMP-MATCH-03 task. Keep full Mode A, flat B1, automatic fallback, real-data ranking,
API serialization, database access, public APIs and UI publication outside that task unless a
later exact accepted contract explicitly adds them.

| Decision surface | Existing exact proposal to accept or modify | Operational consequence / acceptance controls |
|---|---|---|
| Canonical identity | Explicit canonical fixture note IDs, reviewed fixture vocabulary/domain/transform versions and an unambiguous fixture alias mapping/version | Unknown or ambiguous vocabulary/aliases are validation errors; no fuzzy best guess or real-alias approval |
| Required notes | Every required clause must be witnessed in its accepted complete requested domain | An observed positive in an incomplete preview remains unverified; it cannot satisfy this conservative hard rule |
| Optional notes | Soft positive clauses; not every optional clause must match | Require at least one positive clause and at least one matched positive; unmatched optional weights remain in the coverage denominator |
| Excluded notes | Exclusions carry no scoring weight; an observed excluded member fails the candidate | Absence passes only when every searched domain is accepted complete; excluded-only layers affect hard gates without enlarging the positive focus domain |
| Exact selectors | Exact `top`, `heart` or `base` | A note in Base cannot witness a required Top clause; distinct layer memberships remain distinct occurrences |
| Any-layer selector | `any_pyramid` searches all three accepted closed pyramid layers | It is not whichever joins exist; one missing/incomplete searched layer cannot disappear; General/flat is a separate method |
| Duplicate query clauses | After reviewed alias resolution, normalize by canonical ID/selector/role/weight; identical clauses collapse once | No repeated-term score boost; apply the raw clause bound before this collapse |
| Contradictory queries | Same ID/selector with different weights or roles is invalid; same ID with `any_pyramid` plus any exact selector is invalid | Do not sum weights, choose max or turn optional into required; reject before scoring |
| Cross-layer roles | Different exact selectors are independent: required(x,top) plus excluded(x,base) is compatible under this version | Each requested domain must independently pass; a global same-ID role ban is a separate, unselected alternative |
| Positive search domain D | Distinct reviewed `(note ID,layer)` memberships in the union of positive exact layers; any positive `any_pyramid` expands D to all three layers | Excluded-only layers do not enlarge D; all-clause-domain focus is a different alternative, not an implementation choice |
| Positive assignment | Each positive clause uses at most one same-ID compatible occurrence; each occurrence is used at most once | For multiple any-layer witnesses, choose Top, then Heart, then Base for explanation; no occurrence reuse or intensity inference |
| Completeness | All numeric-fit domains and every strict requested domain must be complete and usable | Missing/incomplete/unusable domains give an unranked preview or unavailable result with null fit, not a ranked zero |
| Empty query/domain | At least one positive clause and positive total query weight are required; at least one positive must match | Excluded-only/empty-positive queries are invalid. Complete-empty D has diagnostic H=0 but fails positive minimum1; it is not a perfect or admitted zero-fit match |
| Numeric method | Exact rational query coverage Q and focus H; proposed fit `(4/5)Q + (1/5)H` | Explicit 80/20 acceptance is required. Coverage-only fit=Q needs a separately named version with the same hard gates |
| Output separation | Keep Query Fit, query coverage, Data Confidence and pair evidence distinct | Q is neither source Data Confidence nor Mode A support coverage; no confidence/evidence multiplier or invented Dupe badge for a custom query |

For normalized positive clauses i, with integer weight `w_i` and match indicator `m_i` in `{0,1}`:

```text
Q = sum(w_i * m_i) / sum(w_i)
H = number_of_distinct_matched_occurrences / size(D)
proposed_fit = (4/5) * Q + (1/5) * H
```

The Q denominator includes unmatched optional clauses. Both numerator and denominator remain
explicit in explanations. If D is accepted complete-empty, H=0 is diagnostic only: positive
minimum1 prevents an admitted numeric fit. A failed or unverified hard rule produces null fit;
known source absence must never be invented from a missing field, an omitted layer or an empty
unverified payload. The formula and these rules are **not accepted by this draft**.

## Exact Owner answers still needed before B1 implementation

The following are one response block in the existing [[Next_Wave_Owner_Decision_Form]], not a
second answer form. A blank remains unanswered. Name this packet and the merged method when
recording an actual answer; do not infer an answer from M1 approval or a PR merge.

| Owner answer | Recommendation / alternative | Scope unlocked only after exact acceptance |
|---|---|---|
| Method and task | Select unchanged `mc-b1-pyramid-positive-domain-p1` for separate synthetic IMP-MATCH-03, or explicitly modify/defer it | B1 typed scorer/query-gate implementation only; no B1 code in the Mode A task |
| Formula and role/domain rules | Accept all rows above, including required-all, optional-soft, positive minimum1, disjoint exact-layer roles and positive-domain focus; alternatives need their own method/config identity | Exact Q/H, hard-rule and assignment tests; no silent 80/20, all-clause focus or match-all substitution |
| Fixture identity and configuration | Name the canonical fixture identity representation, vocabulary/domain/transform/alias and selection-snapshot versions, plus exact method/config version | Deterministic synthetic normalization and comparison partitions; no real source or alias promotion |
| Input representation and bounds | Recommend a pure typed-input Python boundary following the accepted M1 style if suitable; explicitly select concrete types, candidate/query limits, identifier lengths and numeric-size limits | Finite pre-evaluation validation; no serializer/parser or unchosen resource limit |
| Existing proposed clause/membership/weight limits | Explicitly select or modify at most30raw/30normalized clauses,512candidate `(note,layer)` memberships and integer positive-query weights1..5 | Reject raw over-bound input before deduplication; reject Boolean-as-number, floats, expression strings and out-of-range values |
| Excluded-clause representation | Define the exact typed representation of an unweighted excluded clause; the merged rule supplies no scoring weight | No hidden absent/None/zero weight convention in the future DTO/type design |
| Transport separation | For a pure typed milestone, explicitly leave API serialization, rational transport parsing and the proposed8KiB request-byte budget to a later task | Do not claim typed object/count validation proves a byte boundary; transport semantics need their own accepted contract |
| Output, errors and ordering | Accept exact rational fit/null and reason, required/exclusion gate states, Q denominator/matched weight/count, D size, closure mask, unique-note specificity, partition and display contract | Deterministic explanations and no ranking of unavailable outcomes; malformed input errors remain distinct from synthetic gate outcomes |

The existing method requires explicit policy fields; missing method/configuration/version fields
are errors, never defaults. A future typed contract must state validation precedence and its exact
error surface. This packet does not invent the missing concrete type/count/numeric-size binding.
Material changes to the merged policy proposal need the applicable Planning Gate review rather
than a hidden implementation exception.

Output ordering follows the merged comparability contract: partition by exact method/configuration,
relevant domain/layer mask, vocabulary and transform versions before ordering numeric results.
Within an accepted partition, sort by exact unrounded fit descending then canonical UUID ascending.
Unavailable outcomes stay in a separate unranked section. Render display-only `100*fit` using exact
half-up rounding to one decimal; null is not rendered as0. The proposal's example `1/16` displays
6.3, while `50001/100000` and `1/2` both display50.0 but retain their distinct exact sort order.
No lifecycle, popularity, coverage-band, confidence or pair-evidence sorting is selected here.

## Future TDD acceptance inventory — NOT RUN

Reuse MC-B01–MC-B15 unchanged for the selected pyramid method; MC-B15 is the separate flat-method
counterexample and must not silently add flat behavior to the pyramid task. Before B1 runtime code:

1. Record the exact accepted synthetic-only contract/configuration, fixture versions and task scope;
   verify current main and merged applicable plans again. M1 approval does not satisfy this step.
2. Write failing tests for absent B1 behavior: MC-B01–14; exact/any-layer witnesses; all required
   versus optional-soft; exclusions and incomplete domains; invalid contradictions/ambiguous aliases;
   positive minimum; same-role duplicate collapse; raw and normalized bounds; unknown/empty inputs.
3. Test rational Q/H and explicit denominators, unmatched optional weights, positive-domain versus
   all-clause-domain discrimination, occurrence non-reuse, unique-note specificity, permutation/
   explanation determinism, UUID ties, rounding, wrong-method rejection and missing configuration.
4. Implement only the accepted B1 behavior, then run focused/math/adapter regressions and meaningful
   property/boundary checks. B1 is directional; Mode A symmetry is not a B1 acceptance requirement.
5. Complete independent exact-source code review and the task's actual acceptance before its one
   receipt and Draft implementation PR. No retrospective receipt or invented execution evidence.

These scorer, query-normalization, hard-rule, property, bounds and explanation tests are all
**SPECIFIED / NOT RUN** by this packet. No historical arithmetic result is relabelled a B1 feature
PASS. There is no new runtime/test code, scorer, alias map, canonical query normalizer or parser.

## Real-data and operational boundaries retained

Synthetic fixture complete/incomplete flags do not prove completeness of any real source capture.
Real use separately needs reviewed canonical identity, selected observations and materialization,
operation-specific active source/field/scope rights, no relevant held/conflicting data, accepted
closure/normalization/eligibility, genuine authorized nonadmin session and relevance/security review.
An eligibility Boolean alone is insufficient. Preserve the44-held-profile operating boundary,
43projection proposals and independent Khamrah disagreement; no new current DB count is asserted.

No source scraping, asset acquisition, rights expansion, SQL/database mutation, app-session bridge,
API/UI publication, public endpoint, cloud resource, Production mutation or PR8 diagnostic experiment
is involved. Application/source decisions must not artificially block isolated synthetic work, but
remain mandatory for their separate real-data/application tasks. Real B2 remains unavailable until
compatible reviewed accord observations and its exact method/scale/domain choices are accepted.

## Tool execution and local verification

TOOL DECISION: existing Caveman, Context Mode for bounded full-document retrieval, read-only Git and
Python/static documentation checks. No new tool/configuration/account or paid service. Worker owns
this one untracked Markdown draft only; coordinator owns M1 contract, task, decision and shared logs.
GIT_WRITE:NO; OBSIDIAN_WRITE:local untracked draft only; PRODUCTION_MUTATION:NO.

Actual source/format checks are recorded separately under ignored `.local/m1-contract/B1/` after
execution. They verify this draft's provenance and form, not a B1 implementation. No commit, push,
branch, PR, receipt, database call or network request was made by this worker. Exact Owner B1
acceptance and independent contract/code review remain future gates.
