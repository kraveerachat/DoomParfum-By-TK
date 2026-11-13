---
id: DPT-PLAN-007-METHOD-CONTRACTS
project: DoomParfum By TK
type: matching_contract_proposal
status: proposed
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, matching, exact-arithmetic, proposed-methods]
source_of_truth: "../../README.md"
---

# Matching method contracts and golden cases

## Authority and the remaining gap

This is a **PROPOSED contract supplement**, not installed configuration or a scorer implementation.
Base `1f2f53f97dff39bc4f3094e4ad82653e8b03f52c` includes Owner-merged PR4 and PR13–17, including
the private architecture plan. No exact DM01–07/OP01–06 answer is recorded. Merging a packet of
choices does not select its constants or methods. Every candidate below needs an explicit Owner
answer identifying version, domain, scope and alternatives, plus the applicable merged Planning
Gate before implementation. Synthetic arithmetic never authorizes real catalogue ranking.
Traceability: R03/R05/R07/R14/R15/R16/R17/R18/R21; this supplement changes no requirement status.

[[Dual_Mode_Matching_Architecture]] already proposes formulas and
[[Dual_Mode_Matching_Acceptance_Tests]] already lists50future cases. [[Post_Merge_Owner_Decision_Packet]]
already supplies the answer sheet. This supplement addresses the following exact gaps rather than
replacing those documents or creating another approval register.

| Existing boundary | Missing executable decision supplied here as a proposal |
|---|---|
| Generic weighted_mean requires all explicit components; architecture also describes available-component division | separate strict full-component, notes-only and legacy available-component contracts; no implicit fallback |
| Scores depend on comparable layers and fallback | exact comparable-layer mask, original coverage denominator and partition key |
| B1 has must, positive clauses and match-all wording | required-all plus optional-soft semantics, positive minimum and explicit alternatives |
| B1 focus uses a comparable candidate domain | whether excluded-only domains enlarge the denominator, with a concrete counterexample |
| One-to-one assignment and any-layer occurrences | exact occurrence identity, duplicate/weight/role conflicts and deterministic witness choice |
| Rounded fit, confidence and pair evidence | exact rational output/rounding, independent policy-pending confidence and evidence |

Existing source remains unchanged: the generic primitives do not establish domain closure, source
rights, aliases, eligibility, full Mode A/B1 or any ranking route. Their `complete` Boolean is a
mathematical assertion. An application must establish an accepted closure contract independently.

## Shared proposed input and result contract

All examples use **SYNTHETIC S-* symbols**, standing for already canonical, reviewed IDs in a
future fixture; none is a real perfume fact or permission. Actual identity is exact canonical
perfume/edition ID. Same names, different concentrations/editions, spelling aliases and duplicate
identities are not merged by scoring. Reject a self-comparison by the same canonical ID; preserve
distinct edition IDs. Raw repeated source occurrences are not accepted by these set contracts.
Any unique-membership transform needs its separately approved version and original lineage.

Every method requires explicit method/configuration, vocabulary/domain/transform versions and
source-selection snapshot identifiers. A missing policy field is an error, never a default.
Comparison requires the same reviewed note vocabulary and compatible source-domain semantics.
Each layer/domain carries its accepted complete-as-reported assertion, exact selected claim and
scope/revision lineage. A populated three-column pyramid does not supply those assertions.

Before any real candidate lookup/count or output, enforce authorized identity/scope, active
operation-specific rights, exact effective selection/materialization, no relevant unresolved
conflict/hold and accepted eligibility. An inaccessible field is not a zero or an explanatory
private-source leak. All44holds,43proposed projections, Khamrah and all current eligibility flags
remain unchanged. This task performs no database or application-session test.

Proposed result fields are `method_id`, exact rational `fit` or null, `reason`, component values,
component/layer denominators, `coverage`, comparable-domain mask, and separate confidence/evidence
states. A null fit is never rendered as0. Coverage measures support under declared weights, not
accuracy. Data Confidence stays `not_evaluated_policy_pending` until its separate policy is accepted.
Pairwise evidence stays an independently permissioned exact-pair claim, never a multiplier. A
custom query has no real perfume reference and receives no invented pair/dupe badge.

Exact input numbers are int/Fraction values; reject Boolean-as-number, floats, strings containing
expressions, NaN/infinity, negatives and values outside the declared domain. Future transport may
encode a rational as numerator/positive denominator under its separately reviewed DTO contract;
this document creates no parser. Propose at most30raw and30normalized note clauses, an8KiB UTF-8
request budget before expensive normalization, integer query weights1..5 and512candidate (note,layer)
memberships, all explicit configuration fields. Reject the raw bound before collapsing duplicates.
These are review
targets, not measured capacity or accepted defaults. Reject over-bound input before evaluation;
no silent truncation or claim of global best matches.

### Missing, empty and zero

| State | Comparison / hard-rule consequence |
|---|---|
| Missing, inaccessible, conflicting or incomplete domain | no numeric set comparison; retain an unavailable reason; cannot satisfy a strict required/excluded rule |
| Accepted complete empty versus accepted complete nonempty, same domain | Jaccard0 with a nonzero union; valid known mismatch |
| Both accepted complete empty | Jaccard null/empty_union; not a perfect match or a contributing layer |
| Complete, nonempty, disjoint sets | Jaccard0; contributes its declared layer weight |
| Complete numeric all-zero accord vectors | weighted Jaccard null/empty_union; not strength0 similarity |

## Mode A candidate contracts — none selected

These proposal IDs deliberately differ from the older draft dm-* names. Selecting one must not
silently change the meaning of a previously stored method/version.

**Common layered notes:** for accepted comparable layers L within top/heart/base, propose original
weights p=(1/4,3/8,3/8). J[l]=intersection/union; a layer is in L only when both same-domain complete
inputs produce a numeric J, including known0. Unknown and both-empty layers are excluded with
different reasons. Require |L|>=2. Then N=sum(p[l]*J[l])/sum(p[l]) and n_cov=sum(p[l]). Keep the
original denominator1 for support coverage. If fewer than2layers compare, N=null and scoring
note reliability0; report observed comparable-layer weight separately as an unranked diagnostic.
This proposed layer division is explicit method policy, not behavior hidden in weighted_mean.

**Numeric accords:** compatible complete vectors, identical explicit full key domains and scale
version, observed finite values in[0,1]; A=sum(min)/sum(max), denominator>0. No zero extension or
presence fallback is performed by these candidates. The older absent-means-zero/presence options
remain separate unanswered DM04choices. Source rank, note repetition and family prose are not values.

**Family:** same reviewed taxonomy/version and accepted complete primary/secondary domain. F=1
when primaries equal; otherwise1/2when either primary is a reviewed secondary of the other;
otherwise0when those complete domains establish no such match. Missing/incomplete/cross-scheme
family information gives F=null. No fuzzy crosswalk, chemical inference or inferred family label.

| Proposed method | Exact fit and gate | Coverage under the original full-model support budget |
|---|---|---|
| mc-a-full-strict-p1 | numeric N,A,F all required; fit=(1/2)N+(3/10)A+(1/5)F; denominator1; otherwise null, no fallback | C=(1/2)n_cov+3/10+1/5 when all components usable; diagnostic availability coverage separately if fit unavailable |
| mc-a-notes-layered-p1 | numeric N with at least2comparable layers; fit=N; excludes accord/family terms by declared method, not missing-value substitution | C=(1/2)n_cov; absent full-model components never disappear from its support interpretation |
| mc-a-notes-flat-p1 | both accepted complete flat domains in the same version; fit=J(flatA,flatB); both-empty gives null | C=1/4 when numeric, from original note budget1/2 times proposed flat reliability cap1/2 |
| mc-a-available-legacy-p1, ALTERNATIVE ONLY | older proposal: K=numeric available components; require usable N or A; fit=sum(w[k]*value[k])/sum(w[k]); exact K disclosed; family alone gives null | C=sum(original w[k]*reliability[k]); no reduced coverage denominator |

For the last alternative, w=(1/2,3/10,1/5); numeric note reliability is n_cov, numeric accord/family
reliability1, unavailable component reliability0. Availability reliability0 describes missing
support, not a zero-valued observed feature. Choosing strict full or notes-only does not authorize
this alternative. Owner must explicitly accept its component redistribution and method partition.

For strict full-component diagnostic availability coverage, use exactly
C=(1/2)rho_N+(3/10)rho_A+(1/5)rho_F even when fit=null: rho_N=n_cov only if N is numeric, otherwise0;
rho_A/rho_F=1only when that component is numeric, otherwise0. A diagnostic Cdoes not rescue a null
fit or authorize comparing an unavailable candidate. For a null notes-only fit, scoring C=0while
the separately named observed-layer diagnostic may still be nonzero.

Flat comparison never invents layers. A complete pyramid may enter the flat method only through a
separately accepted read-only union transform with all3layers closed, exact vocabulary/lineage and
no double-counting of general alongside layers. Any unknown layer blocks that transform. Flat and
layered results do not share a ranking partition. Accepted empty flat sets obey the same J rules.

**Comparability/order proposal:** partition by exact method/config version, component mask K,
layer/domain mask, vocabulary/scale/taxonomy and transform version before comparing numeric fits.
Within an approved partition sort by exact unrounded fit descending, then canonical UUID ascending.
Unavailable outcomes are a separate unranked section. Do not compare a100notes-only result with
a100full-component result as if equal evidence. DM06currentness/coverage-band ordering remains a
separate unanswered choice; this synthetic contract proposes no lifecycle/market priority. Pagination,
authorization and real-data relevance acceptance are separate future tasks.

### Mode A synthetic golden cases

Define fixture G: top{x,y}/{x,z}; heart{h}/{h}; base{b1,b2}/{b2,b3}. Domains are complete, compatible
and nonempty. Thus J=(1/3,1,1/3), N=7/12 and n_cov=1. Numeric accords(1,1/2)/(1/5,1/2) give7/15;
matching complete family primaries give1. These declarations are synthetic oracles, not source claims.

| ID | Exact proposed input/change | Exact expected output |
|---|---|---|
| MC-A01 | G, strict full components | fit379/600; percentage379/6; display63.2; C=1 |
| MC-A02 | G top unavailable, other inputs unchanged | N=2/3; fit101/150; display67.3; C=7/8; layer mask heart/base differs from A01 |
| MC-A03 | top complete empty/nonempty; heart/base1; A=F=1 | N=3/4; strict fit7/8/display87.5; C=1 |
| MC-A04 | top unknown; heart/base1; A=F=1 | N=1; strict fit1/display100.0; C=7/8, not1; distinct missing reason |
| MC-A05 | G accord unavailable | strict fit null/missing_accord; explicitly requested notes-layered fit7/12/display58.3,C=1/2 |
| MC-A06 | same A05, Owner instead selects legacy available N+F alternative | fit59/84/display70.2; score denominator7/10 and C=7/10; not the strict result |
| MC-A07 | only top comparable and J=1, notes method | fit null/insufficient_layers; observed layer support1/4; scoring C=0; no fake0fit |
| MC-A08 | top both complete empty; heart/base1, notes method | top null/empty_union, N=1, fit1/display100.0,C=3/8; reason differs from unknown top |
| MC-A09 | flat{x,y}/{x,z}, explicit flat method | fit1/3/display33.3,C=1/4; incomplete pyramid cannot be substituted |
| MC-A10 | full complete components each known0, all relevant denominators nonzero | strict fit0/display0.0,C=1; valid0is distinct from null |
| MC-A11 | same-key all-zero accord vectors; N=F=1 | A=null/empty_union; strict fit null; never A=0or inferred presence |
| MC-A12 | missing family or incompatible scheme, otherwise G | F=null; strict fit null; notes method may be separately requested, never selected silently |

## Mode B1 candidate contracts — none selected

`mc-b1-pyramid-positive-domain-p1` proposes required-all plus optional-soft behavior, not an implicit
match-all over optional clauses. Every request explicitly carries this policy, positive minimum1,
query weights, domain/method versions and query normalization version. Required and optional clauses
are positive; excluded clauses have no score weight. Require at least1positive clause. Unknown
vocabulary/ambiguous aliases, contradictory rules and malformed/bounded input are validation errors.
Alias resolution requires a reviewed unambiguous canonical mapping; this plan approves none.

Selectors are exact top/heart/base or any_pyramid. An any_pyramid domain is all3accepted closed
layers, never whichever joins happen to exist. General/flat notes do not become pyramid layers.
An alternative `mc-b1-flat-positive-domain-p1` uses only exact general on accepted complete flat
domains with the same Q/H formula; no implicit pyramid/flat conversion or mixed method ranking.
An any-flat UI label, if desired, needs its own explicit mapping/version; it is not any_pyramid.

Normalize by canonical ID/selector/role/weight after reviewed alias resolution. Identical clauses
collapse once. Same ID/selector with different weights is invalid; do not sum or choose max. Same
ID/selector with different roles is invalid; do not silently turn optional into required. Same ID
with any_pyramid plus any exact selector is invalid. Different exact selectors are independent:
required(x,top)+excluded(x,base) is logically compatible under this proposed version; both domains
must pass their own assertions. A stricter global same-ID role ban remains an explicit alternative.
Two exact-layer positives for one ID require two distinct layer memberships and remain1unique
requested note for specificity reporting. No repeated term or source occurrence boosts intensity.

### Gate and denominator rules

1. Authorize candidates/vocabulary before lookup/counts. Reject relevant holds/conflicts/rights/
   selection/identity problems rather than expose a private reason. Gate results below are internal
   synthetic states; future outward unavailable responses must remain uniform where required.
2. Required clauses must all be witnessed in their accepted complete requested domain. An open/
   incomplete domain remains unverified even with a partial positive preview under this conservative
   proposal. Allowing witnessed presence in an incomplete domain to pass a required rule is a
   separate Owner alternative; it still cannot supply absence or a main numeric fit.
3. An observed excluded member fails the candidate. Excluded absence passes only inside every
   accepted closed requested domain. Any-layer exclusion requires all3closed; an unknown layer
   cannot disappear. Failure/unverified outcome has fit=null, never a0ranked result.
4. Define positive search domain D as distinct reviewed (note ID,layer) memberships in the union
   of positive exact layers; if any positive is any_pyramid, D covers all3layers. Excluded-only
   domains affect hard gating but do not enlarge this proposal's focus denominator. All domains
   used for numeric fit and every strict clause must be complete/usable; otherwise unranked preview
   only, with fit=null. The older all-clause-domain interpretation is a separate alternative below.
5. Match each positive clause to at most1same-ID occurrence with compatible selector; each occurrence
   at most once. Exact different layers are disjoint; any+exact same-ID combinations were rejected,
   so maximum-weight assignment has no cross-role reuse ambiguity. For an any clause with several
   witnesses choose top, then heart, then base for explanation; it still matches only once. Sorting
   candidate membership input cannot change Q, H or that explanation rule.
6. Require at least1matched positive clause in addition to every required/excluded gate. Optional
   clauses need not all match. Match-all-positive or minimum0are separate, unaccepted alternatives;
   component arithmetic with them is not an admitted result under this proposal.
7. For all positive clauses i, Q=sum(w_i*m_i)/sum(w_i), m_i in{0,1}; denominator includes unmatched
   optional clauses. H=number of distinct matched occurrences/|D|. If D is accepted empty define
   diagnostic H=0, but positive minimum1prevents a ranked empty-domain result. Proposed fit=(4/5)Q+
   (1/5)H. Coverage-only alternative fit=Q uses a distinct method version and the same hard gates.

Query coverage Q is not source Data Confidence or Mode A support coverage C. Report exact query
weight denominator, matched weight/count, |D|, closure mask and specificity. A single unique requested
note, even requested at two layers, remains limited query specificity; it does not prove smell100.
All query/alias/role/layer/weight/method versions belong in the normalized query identity. No custom
query writes a catalogue perfume, relation or direct-pair evidence record.

### Mode B1 synthetic golden cases

Every listed domain is complete and compatible unless explicitly stated. Unmentioned layers are
irrelevant only when no positive or strict any-layer rule searches them; they are never inferred
empty. All IDs are synthetic reviewed stand-ins. Internal rejected/unverified states are not proof
of external error/privacy behavior, which remains NOT RUN.

| ID | Exact proposed request / candidate | Exact expected result |
|---|---|---|
| MC-B01 | required(x,top,1),optional(y,top,1); top{x,y,z,w} | Q=1,H=1/2,fit9/10/display90.0; required gate passes |
| MC-B02 | optional(x,top,1),optional(y,top,1); top{x,z} | Q=1/2,H=1/2,fit1/2/display50.0; positive minimum passes |
| MC-B03 | required(x,top,2),optional(y,heart,1); top{x,z},heart{q} | Q=2/3,H=1/3,fit3/5/display60.0; unmatched weight remains |
| MC-B04 | optional(x,any_pyramid,1); top{x},heart{},base{x} | Q=1,H=1/2,fit9/10; only1witness used; limited unique-note specificity |
| MC-B05 | required(x,top,1); top{},base{x} | rejected_missing_required; fit=null; base is not an exact-top witness |
| MC-B06 | required(x,top,1); x observed in incomplete top | unverified_required_domain; preview may show permitted presence, fit=null |
| MC-B07 | required(y,top,1),excluded(x,base); top{y},base{},heart unknown | exact-base exclusion passes; positive D=top,fit1; changing exclusion to any_pyramid gives unverified/null |
| MC-B08 | required(x,top,1),excluded(x,base); top{x},base{} | compatible disjoint-layer roles; fit1; same-selector required+excluded instead invalid |
| MC-B09 | same-ID any_pyramid+exact, ambiguous alias, duplicate same-key different weights | validation error, no evaluation/highest-scoring guess |
| MC-B10 | only excluded clauses or zero positive total weight | invalid_empty_positive_query; no percentage or100 |
| MC-B11 | repeat identical optional(x,top,1); top{x} | one normalized clause,fit1; no repeated-term boost; different-role duplicate invalid |
| MC-B12 | required(x,top,1),optional(x,base,1); top{x},base{} | Q=1/2,H=1,fit3/5; if base clause required, reject; unique-note specificity remains1 |
| MC-B13 | required(x,top,1),excluded(y,base); top{x},base{z} | positive-domain proposal Q=H=1,fit1; all-clause-domain alternative H=1/2,fit9/10 |
| MC-B14 | optional(x,top,1); top{} | positive minimum fails; diagnostic Q=H=0does not become an admitted0fit |
| MC-B15 | flat method, optional(x,general,1),optional(y,general,1); complete general{x,z} | Q=H=1/2,fit1/2; no inferred pyramid or mixed-method ordering |

## Owner acceptance matrix and downstream gates

All rows are **PROPOSED / OWNER ANSWER NOT RECORDED**. Selecting a formula does not select closure,
normalization, source rights, session binding or publication. Use the existing Owner packet for an
actual dated response; name the exact method IDs and any modifications rather than approving an
ambiguous collection of alternatives.

| Choice / existing decision | Explicit alternatives / operational consequence | Required future evidence |
|---|---|---|
| Method availability, DM01/03 | strict full+explicit notes methods versus legacy available-component division; no automatic method switch | MC-A01–12, caller missing-config and wrong-method rejection |
| Layers/flat, DM03+OP02 | proposed minimum2and original support weights/cap versus separately versioned changed minimum/coverage; flat requires its transform | empty/unknown/one-layer/domain mismatch and exact mask partition cases |
| Accord/family, DM04+OP04 | explicit same-key numeric domain and complete family; presence/zero-extension/crosswalk alternatives deferred | all-zero, missing strength/key, scale/taxonomy and active-rights negatives |
| B1 roles, DM05 | required-all/optional-soft/minimum1 versus explicit match-all/minimum policy | MC-B01–06/B10/B14–15 and arbitrary-order invariance |
| B1 scope/conflicts, DM05+OP02 | exact disjoint roles allowed versus global same-ID role ban; positive-domain focus versus all-clause-domain focus | MC-B07–09/B12–13 plus closed/incomplete any-layer tests |
| B1 numeric choice, DM05 | proposed80/20versus coverage-only; separate names/groups and unchanged strict gates | exact Q/H, extra-note penalty and unmatched weight oracles |
| Output/comparability, DM02/03/06/07 | exact-mask partitions and rational ordering; lifecycle/coverage bands require separate explicit policy | tied rounded values, UUID tie, method/mask/version group isolation |
| Real-data activation, OP02–06 | remains blocked until accepted closure/normalization/rights/eligibility/nonadmin and implementation acceptance | independent SQL/RLS/revocation/provenance, DTO and meaningful relevance fixtures |

## Rounding, boundedness and proposed implementation work

All formulas above return a Fraction in[0,1] or null. A percentage is display only:100*fit, round
half up to one decimal with exact arithmetic. For unit rational x, displayed tenths integer is
floor(1000*x+1/2); render that integer divided by10. Example x=1/16 gives6.25%, displayed6.3.
Sort before rounding; values50001/100000 and1/2both display50.0but the former remains greater.
Do not multiply confidence or pairwise evidence into fit or sort secretly by their existence.

| Future separate task, NOT STARTED | Gate before RED tests / implementation | TDD deliverable and remaining boundary |
|---|---|---|
| Mode A follow-on, proposed new IMP-MATCH-08 after OP01task-map approval | exact DM/OP01milestone and selected A method/config/domain/partition/rounding approval; this supplement's applicable Planning Gate | first executable MC-A expectations fail for absent scorer; implement pure method assembly, null reasons and explicit request/config bounds; run focused/property/full offline regression, independent exact-source review; no database/API/real ranking |
| IMP-MATCH-03 B1 synthetic query scorer | exact DM05role/assignment/domain/minimum/Q-H choices and closure semantics; independent task branch/PR | first executable MC-B expectations fail; implement typed normalization, gates, deterministic assignment and arithmetic; adversarial aliases/roles/unknown/bounds/permutation tests; no actual alias approval or canonical promotion |
| Later input integration / application-private pilot | accepted selected-field/source-use/closure/eligibility and genuine nonadmin session choice, safe target and explicit task | fresh rights/selection/hold/materialization/RLS/expiry/revocation/concurrency/replay/rollback tests; real-data route remains off until independent acceptance |
| IMP-MATCH-04 B2 | actual reviewed compatible accord inputs AND accepted DM04/05/07scale/method | still disabled for real numeric AND presence scoring; no slider/source-scale inference or placeholder implementation |

The proposed IMP-MATCH-08ID is not allocated or started here. OP01must first reconcile PR9's merged
primitives milestone with the remaining full ModeA boundary. Do not reopen/reuse a completed PR9,
fabricate a full-task receipt or create a second PR for the same task without the approved task-map
change. B1's existing planned IMP-MATCH-03remains separate. Coordinator records actual future IDs,
branches and approved scopes only after that decision; no placeholder implementation PR is created.

Numerical range/symmetry tests apply to A under the same exact configuration; B1is directional.
Use approved canonical fixture inputs and explicit versions, not a source-derived shortcut. Future
negative tests must prove changing unauthorized/private data cannot affect result IDs/counts/order,
and revocation removes later access. Full scorer, authorization, lifecycle, relevance, performance,
API/UI and these acceptance cases are **NOT RUN** by this docs-only task. Arithmetic document checks
are recorded separately in [[DPT-PLAN-007_Golden_Evidence]]; they are not feature acceptance.
