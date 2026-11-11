---
id: DPT-MAT-DUAL-TESTS
project: DoomParfum By TK
type: test_specification
status: proposed
owner: human-owner
updated: 2026-11-11
tags: [doomparfum, matching, acceptance, security]
source_of_truth: "../../README.md"
---

# Dual-Mode Matching Acceptance — Future Implementation Tests

Every test below is **NOT RUN** against a matching engine/API/UI; none exists in this PR.
Arithmetic document checks are reported separately in [[DPT-PLAN-003_Documentation_Evidence]].
Use explicitly synthetic S-* IDs/labels and authorized local fixtures; never real brand/dupe claims.
Expected values refer to [[Dual_Mode_Matching_Architecture]] draft methods, with display rounding only.

## Formula and identity oracles

| ID | Fixture / action | Exact expected result / negative control |
|---|---|---|
| DM-A-01 | distinct IDs; identical complete nonempty pyramid, numeric accords and primary family | N=A=F=1; S=100, C=1; pair evidence none remains none |
| DM-A-02 | complete top disjoint, heart/base equal; A=F=1 | N=0.75; S=87.5; top mismatch explained without sensory claims |
| DM-A-03 | notes only, all three layers equal | S=100, C=0.50; limited coverage visible; no inferred accords/evidence |
| DM-A-04 | equal heart/base, top unknown; other components absent | N=1, n_cov=0.75, S=100, C=0.375; limited-coverage group, not C=1 |
| DM-A-05 | only one layered list comparable and family known | N=null; family alone insufficient; S=null, no fabricated0/100 |
| DM-A-06 | complete flat/general lists {x,y} and {x,z} (also test one side as explicit complete three-layer union); other components absent | flat method J=1/3, S=100/3, C=0.25; no fabricated layers |
| DM-A-07 | both sets empty; then one known empty/one nonempty | empty/empty J=null with no coverage; empty/nonempty J=0; unknown is neither |
| DM-A-08 | swap A/B with same selected method and complete inputs | component/structural scores identical; ranking excludes self, distinct editions remain |
| DM-A-09 | two perfumes same name, EDT/EDP or distinct formulation IDs | no name-based merge, no shared observations without correct identity binding |
| DM-A-10 | family scheme differs; then known same-scheme disjoint/equal/primary-to-secondary | F=null /0 /1 /0.5 respectively; crosswalk never guessed |
| DM-BN-01 | two equal-weight requested exact terms; both matched in four listed occurrences in relevant layers | Q=1,H=0.5,S=90; two extra descriptors visibly penalize focus |
| DM-BN-02 | two requested terms, one matched among two listed occurrences; hard gates disabled/min=0 for scorer oracle | Q=0.5,H=0.5,S=50; denominator never drops unmatched request |
| DM-BN-03 | top x requested, candidate x only in base; then Any Layer | exact does not match; any matches; changing policy changes query hash/method input |
| DM-BN-04 | alias and canonical duplicate of same note/layer; repeated input order | dedup to one clause; score/hash unchanged; no repeated-term boost |
| DM-BN-05 | alias maps to two notes or must+exclude same clause / any+exact same note | reject/disambiguate, no highest-scoring guess |
| DM-BN-06 | same note deliberately requested at top and base; only one occurrence | cannot match twice; exact layer assignments respected |
| DM-BN-07 | must-have missing; exclude observed present; exclude absence unknown | each fails strict gate; unknown is unverified, not claimed absent |
| DM-BN-08 | only-exclude, empty query or missing requested layer | first two invalid/no percentage; last partial preview with score=null |
| DM-BN-09 | one note matched in a one-note complete candidate domain | S=100 with Limited query specificity and capped confidence, not measured scent100 |
| DM-BN-10 | conceptual/synthetic-origin note selected | treated as canonical olfactory note, not asserted chemical ingredient |
| DM-BA-01 | q=(1,0.5), c=(1,0.5) compatible complete numeric | WJ=1, fit100; user sliders not ingredient concentration |
| DM-BA-02 | same q; extra candidate accord1 | WJ=1.5/2.5=0.6, fit60; full union includes extra candidate dimension |
| DM-BA-03 | same q; c=(0.2,0.5) | WJ=0.7/1.5=7/15; fit=140/3, displayed46.7; not cosine |
| DM-BA-04 | desired weights1 and0.5; presence-only list contains first, second known absent | separate presence fit=200/3, displayed66.7; no numeric candidate bars |
| DM-BA-05 | rank-only source; then strength=NULL; then incompatible scale | rank/presence fallback only if usable closed list; no invented intensity or fake0 |
| DM-BA-06 | zero sliders, negative/101/NaN/infinite input; duplicated accord alias | empty/invalid rejected; duplicates normalized once; excludes separate from slider0 |
| DM-BA-07 | minimum matched=2, only one distinct positive requested accord matched | candidate fails regardless of high remaining score; requested unknown blocks numeric fit |

## Data, evidence and authorization controls

| ID | Fixture / action | Exact expected result / negative control |
|---|---|---|
| DM-DATA-01 | source repeated occurrences and many-to-one alias mapping | raw claims/ordinals retained; ambiguous materialization quarantined; no silent DISTINCT at ingestion |
| DM-DATA-02 | conflicting structured/prose claims in one capture | both preserved; only reviewed selected eligible fields score; unresolved field withheld |
| DM-DATA-03 | only family/rating/brand present | browse may show identity, main scent percentage null |
| DM-DATA-04 | PR #3 research sample manifest differs from approved P1 pilot | keep cohort identity/counts separate; audit before fixture substitution; no overwritten pilot |
| DM-EVI-01 | identical structural inputs; change stars/review count/popularity/direct reported percent | structural fit and Data Confidence unchanged; evidence panel may change independently |
| DM-EVI-02 | one direct reviewed alternative claim; no structural score | evidence can say Documented Alternative (reported); no numeric score fabricated |
| DM-EVI-03 | direct supporting and opposing claims; same publisher reposted3 times | disputed panel retains both; independent groups count once; not Official Inspired By |
| DM-EVI-04 | custom B query with no real reference | no pairwise clone/alternative badge to the invented query; no perfume/relation inserts |
| DM-SEC-01 | Alice private overlay on public perfume; Bob/anonymous search | Bob/anonymous IDs, score/order/components/explanation/counts/facets/cache/export unaffected |
| DM-SEC-02 | shared member loses access between pages/cache hits | invalidate/re-authorize; no protected IDs, counts, evidence or scores after revocation |
| DM-SEC-03 | source expires/revoked, selection/alias revision changes after cached score | derived fields/score/counts removed or recomputed; stale cursor rejected/restarted; TTL not sufficient |
| DM-SEC-04 | missing/unauthorized reference, vocabulary, query ID; logged requests | same external invalid/not-found class; no private existence or query leaks in URL/log/referrer |
| DM-SEC-05 | private seed/query copy link, signed asset URL, private retail filter | sharing blocked; no private IDs/hash/source URL/price/preference serialized; public link revalidated |
| DM-SEC-06 | legal text source but asset/derivative display right absent | text if permitted, image placeholder; no hotlink; revoked parent derivative not delivered |

## UX, versioning and operational acceptance

| ID | Fixture / action | Exact expected result / negative control |
|---|---|---|
| DM-UX-01 | A no builder; B no reference | each usable independently; disabled numeric mode does not disable note route |
| DM-UX-02 | historical reference, current/unknown/discontinued candidates | current-first grouping with explicit unknown; historical opt-in; strict market filter excludes unknown |
| DM-UX-03 | missing accord strengths/flat notes/empty results/timeout/stale response | truthful labels/placeholder/null state; no estimated bar or fake overall percentage |
| DM-UX-04 | keyboard/type numeric slider, chip removal, tabs, mobile and screen reader | all controls reachable/labeled, status announced, focus retained, text not color-only |
| DM-OPS-01 | reorder equivalent clauses/aliases; repeat exact snapshot and policy | identical normalized hash/unrounded score/order; version changes for formula/normalization changes |
| DM-OPS-02 | ties, page boundaries, changed rights/data snapshot | stable full sort tuple + UUID; no duplicates/omissions within snapshot; changed policy requires restart |
| DM-OPS-03 | >30 note clauses, >20 accord IDs, >50 page, >8KiB link or >10k candidate pool | bounded error/query_too_broad; no silent truncation called global best matches |
| DM-OPS-04 | 12 then licensed1,479 then synthetic10k profiles; bounded concurrency | compare latency/memory/top-k to exhaustive eligible baseline; candidate recall1 for exact claim |
| DM-OPS-05 | inspect deps/network and datastore during A/B searches | zero external AI/LLM/vector calls, zero catalogue/relation/query writes for ephemeral search |

## Implementation evidence protocol and exit gate

Future implementation must execute golden formulas, input-order/property/range/symmetry tests (A only),
all hard-rule/unknown negatives, real non-owner DB/API scopes and cache/share/export delivery controls.
Record exact code/approved-plan SHAs, source/rights snapshot, fixture hashes, environment, test IDs,
expected/actual status and cleanup. Do not call a DB-only test proof of API/cache/browser isolation.
All50 rows above are future test specifications; independent review must inspect semantics, not counts.

Proposed benchmark: task-isolated local PostgreSQL, hardware/runtime/resources recorded;12 licensed
pilot first, then full1,479 if rights/ETL ready, then synthetic10k. Warmup5 and30 measured requests per
enabled mode/filter/method; p50/p95/max, DB calls/rows examined, worker RSS, payload bytes and cold-start
separately. Proposed budget p95<=2s at1,479, bounded request<=5s at10k, worker incremental RSS<=256MiB;
not an SLA, not measured here. Test1 and4 concurrent callers, cancellations and rights changes. Shortlist
optimization must match exhaustive top-k (recall1) or explicitly label approximation under a different
owner-approved method. Report timeouts/failures; do not weaken rights to pass. No production load test.

Acceptance requires enabled-mode golden/security tests pass, versioned explainability and privacy UX,
source attribution and lifecycle handling, bounded benchmark evidence or a disclosed blocker. No feature
release before independent implementation review and Human Owner Gate I. Existing SQL security/rights
regression suite must be rerun when integration changes touch it; no migrations/DB tests run in this plan.
