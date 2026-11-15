---
id: B1-PD-TYPED-1
project: DoomParfum By TK
type: exact_owner_contract_proposal
status: proposed-not-accepted
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, synthetic, b1, matching, exact-contract, owner-gate]
source_of_truth: "../../README.md"
---

# B1-PD-TYPED-1 — exact synthetic positive-domain B1 contract

**PROPOSED. Owner acceptance NOT RECORDED. No policy-dependent B1 implementation is authorized.**
This document is one complete proposed binding for `mc-b1-pyramid-positive-domain-p1`,
configuration `b1-pd-typed-config-1`, schema `b1-pd-typed-schema-1`. The proposed Coverage80% /
Focus20% formula is not an existing approved default. Every field, policy and limit below is part
of the proposed exact acceptance, including binding details that the merged method left open.

## 1. Authority, task and scope

Verified preparation base/main: `604d447e599aa8359d3427dfbfbceaac85373e48`. Human Owner merged
PR26 at2026-11-14T21:33:25Z (2026-11-15 04:33:25 Asia/Bangkok). Its tree is identical to reviewed
M1 head63cb56c54aacef99fa8937e7a5211acca8ae6a63. M1 approval/merge does not approve B1.
All M1 code/tests, its exact contract and immutable receipt are preserved. No M1 work is repeated.

Normative policy proposal: [[Matching_Method_Contracts_and_Golden_Cases]], canonical Git LF
SHA-256 `f09999add47c820dab0ccb96db0ed0876b80f92a05f198237201ef39187158a8`, shared/B1 rules and
MC-B01–15. [[M1_Next_B1_Owner_Packet]], [[Synthetic_Implementation_Unlock_Checklist]] and
[[Next_Wave_Owner_Decision_Form]] supply the existing decision/task boundary. Their dated pending
M1/merge statements remain historical. This contract proposes the same B1 mathematical method;
it does not silently select flat, all-clause focus, match-all or a coverage-only alternative.

Proposed implementation task: **IMP-MATCH-03, synthetic B1 typed scorer/query gates only**, on its
own future implementation branch and Draft PR after exact Owner acceptance and applicable gates.
This does not complete Full Mode A, a real-data B1 application, B2, transport/API/UI, source alias
approval, catalogue normalization, acquisition, DB access/mutation, authentication, storage/cloud
or Production. It creates no perfume/reference identity or direct-pair evidence. PR8 stays blocked.

The sole proposed public operation is:
`score_synthetic_b1(query, candidates, *, vocabulary, config) -> B1BatchResult`.
All four arguments are required. It is a pure typed-input Python function with no environment,
filesystem, database, network, clock, randomness, external AI, mutable global state or fallback.
There is no serializer, transport DTO/parser, rational-string parser or8KiB request-byte check.
Caller object construction, Python argument binding and memory already allocated by the caller
are outside the in-function resource boundary. Typed bounds do not prove a request-byte budget.

## 2. Complete immutable typed input

Every declared record is a frozen dataclass with all listed fields required and no constructor
defaults. Accept exact declared classes and exact builtin tuple/frozenset/str/int/bool types as
specified; reject subclasses, duck types, mappings, lists, iterators/generators and coercion.
Existing `matching_math.primitives.SetInput` is reused unchanged, not extended with B1 behavior.

| Record | Complete required fields and types |
|---|---|
| B1Query | clauses:tuple[B1Clause,...] |
| B1Clause | note_id:str,selector:str,role:str,weight:int-or-None |
| B1Profile | perfume_id:str,top:B1Layer-or-None,heart:B1Layer-or-None,base:B1Layer-or-None |
| B1Layer | notes:SetInput,completeness_assertion_id:str-or-None,selected_claim_id:str,capture_id:str,revision_id:str,selection_snapshot_id:str,scope_id:str |
| B1LayerDomain | layer:str,domain_id:str |
| B1Vocabulary | vocabulary_version:str,vocabulary_fingerprint:str,domain_version:str,transform_version:str,alias_version:str,normalization_version:str,selection_snapshot_id:str,scope_id:str,layer_domains:tuple[B1LayerDomain,...],note_ids:frozenset[str] |
| B1Config | method_id:str,config_id:str,schema_id:str,role_policy_id:str,selector_policy_id:str,clause_weight_policy_id:str,closure_policy_id:str,assignment_policy_id:str,focus_domain_policy_id:str,positive_minimum:int,formula_weights:tuple[int-or-Fraction,...],max_raw_clauses:int,max_normalized_clauses:int,max_candidates:int,max_memberships_per_candidate:int,max_vocabulary_notes:int,min_positive_weight:int,max_positive_weight:int,max_identifier_chars:int,max_numeric_bits:int,max_total_memberships:int |

`candidates` is an exact tuple of B1Profile; there is no reference perfume. All candidate IDs must
be unique; names/shared notes cannot merge editions. Every present layer uses exact SetInput with
an exact frozenset of canonical note-ID strings, exact Boolean `complete` and explicit domain_id.
None is a missing layer, not an empty complete set. Raw arrays/repeated source occurrences are
not input to this set boundary. A note in two layers is two `(note_id,layer)` memberships.
`heart` is the one canonical Middle/Heart field; selector `middle` is not accepted as an alias.

Canonical fixture UUIDs are exact lowercase36-character strings. Perfume IDs use
`10000000-0000-4000-8000-` plus12lowercase hexadecimal digits with nonzero suffix. Note IDs use
`20000000-0000-4000-8000-` with the same suffix rule. These are synthetic identity conventions,
not real product facts, an authenticity proof or a security mechanism. Suffix magnitude has no
scoring meaning. Vocabulary size, not suffix magnitude, is bounded below. Every query/candidate
note ID must occur in supplied note_ids; unknown IDs are errors, not unmatched optional notes.

All other identifier tokens, including domain and lineage IDs, are exact strings of1..128ASCII
characters matching `[A-Za-z0-9][A-Za-z0-9._:-]*`. Enums have their stricter literal values below;
UUIDs/fingerprint have their stricter widths. No trim, case folding, fuzzy lookup or coercion.

### Proposed fixed fixture context and alias boundary

| B1Vocabulary field | Exact proposed value |
|---|---|
| vocabulary_version | `synth-notes-b1-v1` |
| domain_version | `synth-pyramid-domains-b1-v1` |
| transform_version | `canonical-set-fixture-b1-v1` |
| alias_version | `canonical-id-only-b1-v1` |
| normalization_version | `canonical-clause-set-b1-v1` |
| selection_snapshot_id | `synth-selection-b1-v1` |
| scope_id | `synth-scope-b1-v1` |
| layer_domains | exact3-tuple B1LayerDomain(top,`synth-top-b1-v1`),B1LayerDomain(heart,`synth-heart-b1-v1`),B1LayerDomain(base,`synth-base-b1-v1`), in that order |
| note_ids | exact frozenset of0..512valid fixture note IDs |
| vocabulary_fingerprint | caller-supplied64lowercase hexadecimal SHA-256 of sorted note_ids joined by oneASCII LF, no terminal LF; empty vocabulary hashes empty bytes |

The fingerprint identifies the finite vocabulary, not request serialization, rights or authenticity.
It is supplied and validated, never filled by a default. This milestone accepts **canonical IDs
only**. There is no alias mapping/resolver: real names, unreviewed/ambiguous aliases and textual
labels are invalid note IDs. The alias version explicitly declares identity-only input; it does
not claim aliases have been reviewed or resolved. An actual alias resolver needs its own exact
accepted mapping/version and scope. Query deduplication below is not source normalization or
normalization promotion. The transform declares already canonical fixture sets; it performs none.

Each present layer supplies selected_claim_id,capture_id,revision_id and the call's exact scope_id
and selection_snapshot_id. Complete=True requires a non-null bounded completeness_assertion_id;
complete=False requires that field=None. These are synthetic caller declarations, not acceptance
of real-source completeness, selected rights, eligibility, ownership or provenance review.
A valid but different layer domain_id is an unavailable domain state; malformed lineage/types
still reject the complete call before any candidate result.

## 3. Exact explicit configuration and resource limits

All fields are supplied, checked and equal the following profile. Changing any under the same
config_id is invalid, even when it seems harmless. A different policy/bound requires a separately
versioned accepted profile; missing configuration never chooses defaults.

| B1Config field | Exact proposed value |
|---|---|
| method_id | `mc-b1-pyramid-positive-domain-p1` |
| config_id | `b1-pd-typed-config-1` |
| schema_id | `b1-pd-typed-schema-1` |
| role_policy_id | `required-all-optional-soft-b1-v1` |
| selector_policy_id | `pyramid-exact-any-b1-v1` |
| clause_weight_policy_id | `positive-int-1-5-excluded-none-b1-v1` |
| closure_policy_id | `synthetic-closed-domains-b1-v1` |
| assignment_policy_id | `one-to-one-top-heart-base-b1-v1` |
| focus_domain_policy_id | `positive-layers-only-b1-v1` |
| positive_minimum | exact int1 |
| formula_weights | exact tuple(4/5,1/5), Coverage then Focus; exact int/Fraction values, no floats |
| max_raw_clauses / max_normalized_clauses | exact int30 / int30 |
| max_candidates | exact int64; actual candidate tuple0..64 |
| max_memberships_per_candidate | exact int512, sum of every present layer-set length including incomplete previews and irrelevant layers |
| max_vocabulary_notes | exact int512 |
| min_positive_weight / max_positive_weight | exact int1 / int5 |
| max_identifier_chars | exact int128; UUIDs/fingerprint additionally fixed-width |
| max_numeric_bits | exact int128 for every supplied integer and reduced Fraction numerator/positive denominator |
| max_total_memberships | exact int32768=64*512, sum of candidate memberships |

Count fields require exact int, not bool. Formula weights accept exact int or fractions.Fraction,
not subclasses, bool, float, Decimal, NaN/infinity or expression strings. Check numeric bit lengths
before arithmetic/equality. Formula values are in[0,1] and exactly4/5,1/5. Clause positive weights
are exact int1..5; excluded weight is exactly None, not0, a missing field or a default weight.
Fraction numerator/denominator must themselves be exact int and denominator positive, including
malformed objects constructed outside normal constructors; reject bad internal types as TypeError
and nonpositive denominator as Unsupported configuration before arithmetic, never divide by zero.
At most150normalized positive weight is possible. Derived fractions use exact arithmetic; finite
size follows the bounded counts/weights. Do not clip, truncate, reinterpret or silently normalize
alternative input weights. A raw0-clause tuple is size-bounded but invalid as an empty-positive
query. The total membership cap is redundant with64*512: no independent over-total fixture can
keep both other caps valid. Future tests must not pretend such an independent negative exists.
These are bounded-work controls, not latency, throughput, memory already allocated, capacity or SLA claims.

## 4. Validation, normalization and exact query identity

Entry order is normative. First check exact top-level classes/tuple and raw candidate/clause counts;
reject a raw31st clause before deduplication and a65th candidate before scanning either collection.
Then validate configuration identifier/count/numeric types, bit lengths and prescribed values;
vocabulary container/count before any member scan or fingerprint hashing; all candidate/layer/
SetInput shapes, set lengths/total memberships and every token length before member validation,
sorting or set arithmetic. Clause record/field types and weight bit lengths precede query arithmetic.
Only then validate token/UUID syntax, fixed context/fingerprint, membership, candidate identities,
lineage consistency and clause semantics. All candidates, including irrelevant present layers and
the last candidate, must validate before returning any result. Builtin len checks precede scans.
Missing fields on an exact forged/malformed record must raise the bounded shape error below.

Role literals are `required`,`optional`,`excluded`. Selector literals are `top`,`heart`,`base`,
`any_pyramid`; general/flat/middle/any_flat are unsupported. Positive means required or optional.
Validate positive weight integer type/bits first. Negative or>5positive weights are invalid queries.
No positive clauses, or positive clauses whose weights are all0, are invalid_empty_positive_query.
A mixture of0and otherwise positive weights is invalid_query; zero is never accepted as a valid
weight. This error-label binding preserves MC-B10 without granting weight0. An excluded clause
must have weight=None; any other value is invalid_query after its declared type is checked.

After these checks normalize already canonical clauses, without alias resolution:

1. Identical `(note_id,selector,role,weight)` duplicates collapse once, including excluded duplicates.
2. Same note_id/selector with different roles or different weights is invalid. Do not sum, select
   max, turn optional into required, or make an exclusion weighted.
3. Same note_id with any_pyramid plus any exact selector is invalid, regardless of roles/weights.
4. Different exact selectors are independent: required(x,top) and excluded(x,base) are compatible.
5. Sort normalized clauses by note_id ascending, selector ordinal top0/heart1/base2/any_pyramid3,
   role ordinal required0/optional1/excluded2, then weight with None represented only for ordering
   by sentinel0. This sentinel does not become a score weight or stored excluded weight.

At least one normalized positive is required. Normalized count is at most30; deduplication never
rescues an over-bound raw tuple. Unique positive-note specificity counts distinct positive note IDs,
not raw terms, clauses, layers or exclusions. x requested at both Top and Base still has specificity1.

`B1QueryKey` is an exact immutable structural identity, not a hash or transport encoding. It consists
of the validated entire B1Config, metadata-only B1ContextKey and canonical normalized B1Clause tuple.
Thus method/config/schema, role/selector/weight/closure/assignment/focus versions, normalization,
alias/vocabulary/fingerprint/domain/transform/snapshot/scope and every clause/weight are explicit.
Do not persist Python hash(), use repr as identity, or introduce an unspecified serialization hash.
Raw duplicate counts and input order are diagnostics, not identity. No candidate ID, selected claim,
capture/revision/assertion ID, candidate membership set or source payload belongs in the query key.

### Fixed error surface

These are validation exceptions, distinct from well-formed synthetic candidate gate outcomes.
No fallback, partial results, input repr, clause contents or private source reason is returned.

| Invalid condition | Exception and exact in-function message |
|---|---|
| Wrong exact declared type, including bool-as-number/subclass/container | TypeError: `Invalid typed input` |
| Missing required field on an exact malformed object | ValueError: `Invalid typed input shape` |
| Count, token-length or numeric-bit cap exceeded | ValueError: `Input bound exceeded` |
| Config value/policy/method differs, or a Fraction denominator is nonpositive | ValueError: `Unsupported configuration` |
| Fixed vocabulary/context version or expected layer-domain table differs | ValueError: `Unsupported fixture context` |
| Malformed token/UUID syntax or duplicate candidate identity | ValueError: `Invalid identifier` |
| Wrong fingerprint or query/candidate note outside vocabulary | ValueError: `Invalid fixture vocabulary` |
| Wrong scope/snapshot or completeness/assertion consistency | ValueError: `Invalid fixture lineage` |
| Unsupported selector/role, invalid nonzero weight, excluded weight, contradiction | ValueError: `Invalid query` |
| No positive clauses or all-zero positive weight | ValueError: `Invalid empty positive query` |

When several inputs are invalid, the entry-stage order above governs; within bounded collections,
validate candidates in supplied order and fields in the schema order, with Top/Heart/Base fixed.
Error text is category-only and bounded; do not chain an original attribute error containing data.
Omitted required function/constructor arguments are Python TypeError before entry, not a hidden
config default. Host argument-binding text is outside the in-function fixed-message guarantee.
An empty candidate tuple still validates query, vocabulary and config before returning no results.

## 5. Domain state, strict rules and occurrence assignment

Layer order is always Top,Heart,Base. For each candidate, compare every present layer's domain_id
with its corresponding fixed expected B1Vocabulary.layer_domains entry. B1LayerStatus.state is
`missing` for None; otherwise `domain_mismatch` if incompatible, then `incomplete` if complete=False,
otherwise `complete`. This proposed diagnostic precedence is explicit; domain compatibility is
also reported separately. Only state=complete is closed/usable for numeric fit or passing absence.
Present compatible incomplete sets can prove an observed excluded member, never its absence.
Incompatible-domain membership is not an interpretable witness, even when the note ID is known.

Exact selectors search their one layer. any_pyramid searches all3, including missing/incomplete
layers; it never means whichever joins exist. Unmentioned layers are irrelevant to numeric/gate
domains only if no clause searches them. Their input shape/lineage still must validate.

Define positive_layer_mask as the union of layers searched by all positive clauses. Define
strict_layer_mask as the union searched by required and excluded clauses. relevant_layer_mask is
their union. Each is an exact fixed-order tuple with no duplicates. any_pyramid expands to all3.
The positive search domain D contains distinct `(note_id,layer)` candidate memberships from the
positive_layer_mask only. Excluded-only layers affect strict gates, never |D| or the focus score.

Evaluate every normalized clause, preserving all explanations even when one fails:

| Role / domain observation | Exact B1ClauseEvaluation.state and witness |
|---|---|
| Required/optional, every searched layer closed/usable, matching occurrence exists | `matched`, one B1Occurrence witness |
| Required/optional, every searched layer closed/usable, no matching occurrence | `unmatched`, witness=None |
| Required/optional, any searched layer unavailable | `unverified`, witness=None, even if a positive preview is visible |
| Excluded, matching member in a present compatible layer, complete or incomplete | `excluded_present`, one observed witness; known failure dominates unknown searched layers |
| Excluded, no observed compatible member and all searched layers closed/usable | `excluded_absent`, witness=None |
| Excluded, no observed compatible member and any searched layer unavailable | `unverified`, witness=None; no inferred absence |

For multiple compatible witnesses, choose Top then Heart then Base. A positive clause uses at most
one occurrence, and every `(note_id,layer)` occurrence is used at most once across positives. The
query contradiction rules remove any/exact competition for one ID; distinct exact-layer clauses
are disjoint. Therefore no hidden weight-based reassignment, repeated-term intensity or arbitrary
matching tie-break is needed. Exclusion witnesses are not positive assignments or focus numerator.
`unverified_domains` lists every searched layer whose state is not complete in fixed order, even
when an observed exclusion already fails; it does not erase the known excluded-presence witness.

Aggregate gates are exact:

- required: failed if any required is unmatched; otherwise unverified if any is unverified;
  otherwise passed, including no required clauses.
- excluded: failed if any is excluded_present; otherwise unverified if any is unverified;
  otherwise passed, including no excluded clauses.
- positive_domain: complete only if every positive_layer_mask layer is state=complete;
  otherwise unverified.
- positive_minimum: passed if at least one positive clause has a verified matched witness;
  failed if all positives are verified and none matched; otherwise unverified.

Main candidate reason uses this exact precedence: rejected_excluded, rejected_missing_required,
unverified_required_domain, unverified_exclusion_domain, unverified_positive_domain,
rejected_no_positive_match, computed. The first matching gate condition wins in that order;
all other gate/clause states remain visible. This is an explicit proposed multi-failure binding,
not an assertion that the merged supplement already fixed its display precedence.
Unverified positive_minimum with a complete positive domain is impossible under these rules.

## 6. Coverage, focus, admission and diagnostics

For normalized positive clauses i, exact integer weight w_i and verified match indicator m_i:

```text
query_weight_denominator = sum(w_i) over all normalized positive clauses
verified_matched_weight = sum(w_i) for verified matched positive clauses
Q = query_coverage = verified_matched_weight / query_weight_denominator
H = focus = number_of_distinct_verified_positive_witnesses / size(D)
proposed fit = (4/5)*Q + (1/5)*H
```

The Q denominator includes unmatched optional clauses and required clauses; duplicate raw terms
do not multiply it. Exclusions have no weight. Every positive exact-layer clause for one ID needs
its own layer occurrence; any_pyramid chooses at most one. |D| includes all candidate note/layer
memberships in the positive domain, not only requested notes or any excluded-only domain.

Q,H and positive_domain_size are numeric **only when positive_domain=complete**. Otherwise all
three are None. Counts/weight of verified witnesses may still be reported as a known subset;
they are not a zero-imputed complete score. When D is complete empty, diagnostic Q=0,H=0 and
positive_domain_size=0; this explicit diagnostic convention is not division by zero or a perfect
match. Positive minimum fails, or a required-missing failure wins by precedence. No numeric fit.

Admit numeric fit only when required and excluded gates pass, positive_domain is complete and
positive_minimum passes. Then Q,H,fit are exact Fractions in(0,1], fit has a numeric partition key,
and query_fit_percent_display is non-null. If any gate fails/is unverified, fit/partition/display
are None and the candidate is unranked. Known Q/H diagnostics remain available when their own
positive domain is complete even if an exclusion/required gate fails; diagnostics never rescue fit.
For example, a compatible incomplete excluded-only Base containing an excluded note fails the
candidate although complete Top positives can have diagnostic Q=H=1. It does not become fit0/fit1.

Coverage Q measures weighted query fulfillment, not M1 support coverage, source completeness,
accuracy or Data Confidence. Focus penalizes additional declared notes in the positive domain;
it is a proposed structural preference, not measured smell quality. One unique positive note may
score fit1; unique_positive_note_count remains1 and is not a scientific similarity claim.
Data Confidence stays `not_evaluated_policy_pending`. Pair evidence stays
`not_evaluated_synthetic_only`; a custom query has no real exact-pair/dupe badge.

## 7. Complete immutable output, grouping and display

All result records are exact frozen dataclasses with every listed field required. Sequence fields
are exact tuples; counts exact int, never bool; numeric components exact Fraction or explicit None.
All masks and domain tuples are in Top/Heart/Base order without duplicates. Strings copy only
validated bounded metadata. No full candidate note sets, arbitrary user prose, input vocabulary
object, raw records, URLs, global rank, confidence bands or undeclared payload fields are retained.

| Output record | Complete required fields and exact types |
|---|---|
| B1ContextKey | vocabulary_version:str,vocabulary_fingerprint:str,domain_version:str,transform_version:str,alias_version:str,normalization_version:str,selection_snapshot_id:str,scope_id:str,layer_domains:tuple[B1LayerDomain,...] |
| B1QueryKey | config:B1Config,context:B1ContextKey,clauses:tuple[B1Clause,...] |
| B1Lineage | completeness_assertion_id:str-or-None,selected_claim_id:str,capture_id:str,revision_id:str,selection_snapshot_id:str,scope_id:str |
| B1LayerStatus | layer:str,state:str,declared_complete:bool-or-None,domain_compatible:bool-or-None,domain_id:str-or-None,lineage:B1Lineage-or-None |
| B1Occurrence | note_id:str,layer:str |
| B1ClauseEvaluation | clause:B1Clause,domain_layers:tuple[str,...],state:str,witness:B1Occurrence-or-None,unverified_domains:tuple[str,...] |
| B1GateSummary | required:str,excluded:str,positive_domain:str,positive_minimum:str |
| B1PartitionKey | query_key:B1QueryKey,positive_layer_mask:tuple[str,...],strict_layer_mask:tuple[str,...],relevant_layer_mask:tuple[str,...],layer_domains:tuple[B1LayerDomain,...] |
| B1CandidateResult | method_id:str,config_id:str,schema_id:str,candidate_id:str,query_key:B1QueryKey,reason:str,fit:Fraction-or-None,query_coverage:Fraction-or-None,focus:Fraction-or-None,query_weight_denominator:int,verified_matched_weight:int,verified_matched_positive_count:int,verified_matched_occurrence_count:int,positive_domain_size:int-or-None,positive_layer_mask:tuple[str,...],strict_layer_mask:tuple[str,...],relevant_layer_mask:tuple[str,...],closure_mask:tuple[str,...],unique_positive_note_count:int,gates:B1GateSummary,clauses:tuple[B1ClauseEvaluation,...],layers:tuple[B1LayerStatus,...],partition_key:B1PartitionKey-or-None,query_fit_percent_display:str-or-None,confidence_state:str,pair_evidence_state:str |
| B1PartitionResult | key:B1PartitionKey,results:tuple[B1CandidateResult,...] |
| B1BatchResult | method_id:str,config_id:str,schema_id:str,query_key:B1QueryKey,raw_clause_count:int,normalized_clause_count:int,positive_clause_count:int,query_weight_denominator:int,unique_positive_note_count:int,positive_layer_mask:tuple[str,...],strict_layer_mask:tuple[str,...],relevant_layer_mask:tuple[str,...],groups:tuple[B1PartitionResult,...],unranked:tuple[B1CandidateResult,...] |

Output invariants are normative:

- Batch/group/candidate keys carry the validated call method/config/schema/context and canonical
  normalized clauses. All fields in copied B1Config remain explicit, with no constructor defaults.
- raw_clause_count1..30, normalized_clause_count1..30, positive_clause_count1..30; unique positive
  count1..positive_clause_count; query_weight_denominator1..150. Batch counts match the query.
- Candidate clauses are exactly one evaluation for every normalized clause in that order; layers
  are exactly3statuses, Top/Heart/Base. Witness note_id equals clause.note_id and lies in its
  searched layer. Verified positive count equals verified positive occurrence count, both0..30;
  verified_matched_weight0..query_weight_denominator. Exclusions add neither count nor weight.
- Missing LayerStatus has declared_complete/domain_compatible/domain_id/lineage all None. Present
  statuses retain exact Boolean flags, validated domain and six-field lineage. state follows §5;
  domain_compatible=False means domain_mismatch even if declared_complete=False. A present complete
  declaration requires its assertion even when domain-incompatible; malformed input is not a gate.
- Gate strings are required/excluded/positive_minimum in passed,failed,unverified; positive_domain
  in complete,unverified. Clause state literals are exactly matched,unmatched,unverified,
  excluded_present,excluded_absent with role restrictions and witness rules in §5. No additional enum.
- closure_mask is exactly the relevant layers in state=complete, not a claim about any real source.
  positive_domain_size is0..512 only when complete; otherwise None. If it is known positive, focus
  numerator is verified_matched_occurrence_count and denominator positive_domain_size. For known0,
  focus is diagnostic Fraction(0). Q numerator/denominator remain the explicitly named integers.
- Numeric candidate reason is computed; fit/query_coverage/focus/display/partition are non-null,
  closure_mask=relevant_layer_mask and every gate permits admission. Unranked reason is one of the
  six other literals in §5; fit/partition/display are None, even if Q/H diagnostics are known.
- Confidence/evidence are the two exact constants in §6 in every state; no multiplier or badge.
- Ranked plus unranked result count equals input candidate count; no disappearance or duplication.

A numeric partition key includes exact normalized query identity, positive/strict/relevant masks
and actual equal expected domain IDs for relevant layers. Candidate identity, capture/claim/revision/
assertion IDs and raw duplicate counts are provenance/diagnostics, not grouping keys. Different
exact query/context/method keys are incomparable. This one-call fixed-domain method has0or1numeric
partition, not a cross-query ranking. groups is empty or a one-item tuple; that group's result
tuple is nonempty length1..64. There is no cross-batch/global merge or best-match promise.

Within the one numeric partition sort exact unrounded fit descending, then canonical candidate
UUID ascending. Unranked candidates are separate, sorted by UUID, never by their gate reason or
diagnostics. Canonical IDs have fixed namespace/width, so lexical UUID order is unambiguous.
For numeric fit x, display tenths=floor(1000*x+1/2), then render one decimal with no percent sign.
Use exact arithmetic, no float; sort before rounding. Null display is None, never0.0. Examples:
1/16 displays6.3,0displays0.0 as a rounding arithmetic example,1displays100.0; fit0 is not an
admitted B1 candidate under positive minimum1. Candidate/query/set input permutations do not
change normalized identity, gate/metric/explanation order or ranked output. Duplicate insertion
changes only the explicitly diagnostic raw_clause_count, provided the raw limit remains valid.

## 8. Golden acceptance specifications — FUTURE TESTS, NOT RUN

Symbols x,y,z,w,q are canonical fixture note UUID suffixes1,2,3,4,5respectively; perfume symbols
are distinct valid fixture IDs. Unless stated, searched layers are complete, compatible and carry
valid declared lineage; unsearched layers may be None. These are synthetic assertions only.

| Source/case | Exact proposed expected result |
|---|---|
| MC-B01 required(x,top,1),optional(y,top,1); Top{x,y,z,w} | Q=1,H=1/2,fit9/10,display90.0; required/excluded/minimum pass |
| MC-B02 optional(x,top,1),optional(y,top,1); Top{x,z} | Q=1/2,H=1/2,fit1/2,display50.0 |
| MC-B03 required(x,top,2),optional(y,heart,1); Top{x,z},Heart{q} | Q=2/3,H=1/3,fit3/5,display60.0; denominator3 includes unmatched optional |
| MC-B04 optional(x,any_pyramid,1); Top{x},Heart{},Base{x} | Q=1,H=1/2,fit9/10,display90.0; sole witness Top; specificity1 |
| MC-B05 required(x,top,1); Top{},Base{x} | rejected_missing_required,fit/display/key=None; diagnostic Q=H=0,Dsize0; Base not witness |
| MC-B06 required(x,top,1); x in compatible incomplete Top | unverified_required_domain; Q/H/Dsize/fit=None; no verified positive witness |
| MC-B07 required(y,top,1),excluded(x,base); Top{y},Base{},Heart missing | fit1,display100.0; D is Top only; exact Base exclusion passes. Change exclusion to any_pyramid:unverified_exclusion_domain/null |
| MC-B08 required(x,top,1),excluded(x,base); Top{x},Base{} | compatible disjoint roles; fit1. Same-selector required/excluded is Invalid query |
| MC-B09 same-ID any+exact, ambiguous textual alias, same ID/selector different weight | validation error; no candidate evaluation or highest-scoring guess; canonical-only alias strings fail ID validation |
| MC-B10 excluded-only/empty query or all-zero positive weights | Invalid empty positive query; no percentage/100. Other invalid weights are rejected as §4 specifies |
| MC-B11 duplicate identical optional(x,top,1); Top{x} | normalized count1/weight1; Q=H=fit1; raw count2, no score boost |
| MC-B12 required(x,top,1),optional(x,base,1); Top{x},Base{} | Q=1/2,H=1,fit3/5; specificity1. Making Base required gives rejected_missing_required/null |
| MC-B13 required(x,top,1),excluded(y,base); Top{x},Base{z} | Q=H=fit1; excluded-only Base never enlarges D. All-clause-domain alternative9/10 is not this method |
| MC-B14 optional(x,top,1); Top{} | rejected_no_positive_match; diagnostic Q=H=0,Dsize0; fit/display/key=None |
| MC-B15 supplied flat method or selector general | reject unsupported config/selector; do not implement the separate flat method's1/2 arithmetic as pyramid behavior |
| B1-X01 optional(x,top,1); Top complete domain_mismatch containing x | unverified_positive_domain,fit/Q/H/Dsize=None; no compatible witness |
| B1-X02 optional(x,any_pyramid,1); Top{x},Heart{},Base missing | unverified_positive_domain,fit/Q/H/Dsize=None; any does not shrink to available layers |
| B1-X03 required(x,top,1),excluded(y,base); Top{},compatible incomplete Base{y} | rejected_excluded wins over rejected_missing_required; required=failed,excluded=failed; Q=H=0 diagnostic; fit=None |
| B1-X04 required(x,top,1),excluded(y,base); Top{x},compatible incomplete Base{y} | rejected_excluded; diagnostic Q=H=1,Dsize1; excluded witness retained although Base unclosed |
| B1-X05 same query; Top{x},compatible incomplete Base{} | unverified_exclusion_domain; diagnostic Q=H=1,fit=None; empty preview cannot prove absence |
| B1-X06 optional(x,top,1),optional(y,base,1); Top{x},Base missing | positive_minimum=passed from verified Top; positive_domain unverified; Q/H/Dsize/fit=None; verified count1/weight1 is known subset only |
| B1-X07 empty candidates and valid query/context/config | groups/unranked empty; no match/100; malformed query/config still errors |
| B1-X08 required(x,top,1),required(x,base,1); Top{x},Base{x} | two distinct witnesses,count2,Q=H=fit1,specificity1 |
| B1-X09 repeated excluded(x,base,None) plus optional(y,top,1) | excluded duplicates collapse once; excluded weight remains None; wrong0 weight rejected |
| B1-X10 equal exact fits, different perfume IDs, permuted input | IDs ascending, identical explanations/query key; no input-order tiebreak |

Realizable sort-before-rounding fixture: vocabulary note suffixes1..512; query optional(note1,top,1)
and optional(note512,top,1). H candidate has Top notes1..500; L has Top1..501. Both Q=1/2;
H focuses1/500 and fit1001/2500; L focuses1/501 and fit1003/2505. Both display40.0, but H sorts
first even with the greater UUID. All membership/vocabulary bounds hold. This is not a capacity test.

## 9. Future TDD, properties and delivery criteria — NOT RUN

After exact Owner version/hash/scope acceptance, create one isolated IMP-MATCH-03 branch from the
then-verified main. Write genuinely failing tests for absent B1 behavior before runtime code.
Record actual RED command/results and distinguish import/setup failures from executed feature bodies.
Implement only this selected typed method and preserve all failures/corrections/source bindings.

Required future golden/negative tests cover every row above, all required fields/output fields,
all gate/diagnostic states and precedence, canonical-ID-only/unknown alias rejection, role/selector/
weight contradictions, excludedNone, raw-before-dedup limits, all profile/layer/metadata errors,
missing config/cross-method rejection, malformed exact objects, and no partial result from a bad
last candidate. Boundary cases include0/30/31raw clauses,30normalized,0/64/65candidates,
512/513memberships including incomplete/irrelevant layers,512/513vocabulary notes,128/129token
characters and numeric bits. Test the reachable32768total maximum and the redundant-cap logic
honestly; no fake independent over-total counterexample. No truncation or default substitution.

Property specifications, with finite recorded case counts, include:

1. Exhaustive small canonical vocabularies/complete domain subsets and bounded seeded unavailable
   states: admitted fit,Q,H exact Fractions in(0,1]; other outcomes have null fit/key/display.
2. Query/candidate/set construction permutations preserve canonical query key, clause/witness order,
   exact metrics and candidate order. Duplicate insertion below raw cap preserves all semantic
   results, with only raw_clause_count allowed to change.
3. Normalization is idempotent on the accepted canonical clause set; conflicts never resolve by
   input order. Distinct exact-layer same-ID clauses require distinct witnesses; any witnesses use
   Top/Heart/Base priority and occurrences are never reused.
4. With query, verified matched assignment and gates fixed, adding one distinct unrequested
   membership within valid bounds inside a complete positive domain leaves Q unchanged and cannot
   increase H. H strictly decreases only when the verified positive-witness count is positive;
   with count0, H remains0, including the complete-empty diagnostic case. Assert fit non-increase
   and strict decrease only for admitted numeric outcomes: fit cannot increase, and strictly
   decreases when that fixed witness count is positive. Unranked fit remains None under fixed
   gates; do not make a numeric monotonicity assertion about null. Adding a non-excluded membership
   only to an excluded-only layer within valid bounds leaves Q,H,fit unchanged when assignment/
   gates remain fixed; a newly observed excluded member fails.
5. Removing or invalidating required closure cannot manufacture absence, a verified required pass
   or a numeric fit. Incomplete observed exclusion still fails; incomplete empty exclusion never passes.
6. Exact unrounded ordering precedes display rounding and UUID only resolves exact ties. Ranked plus
   unranked conserves all candidate identities; no cross-query/method grouping or global rank.
7. Frozen outputs have exact field/type/state invariants and bounded lineage only. No Data Confidence/
   pair-evidence multiplier, arbitrary payload leak, I/O, source lookup, DB call or mutable default.
8. Wrong config versions/parameters never fall back. B1 is directional: Mode A symmetry is not a B1
   requirement. No property relabels real-source completeness or future authorization as verified.

Then run focused/property tests and existing M1/math/research/adapter offline regressions; mark
unexecuted SQL/live RLS/replay/recovery/API/UI/transport/relevance/performance tests NOT RUN.
Independent exact-source implementation review must finish and resolve blockers before one scoped
final receipt and one Draft PR for Human Owner. Preserve all existing M1 artifacts and PR8 history.
No implementation, acceptance PASS, branch/PR/receipt or runtime test result is claimed by this plan.

## 10. One exact Owner decision, alternatives and retained gates

Owner/date/reference and accepted contract hash: **NOT RECORDED**. 80/20 remains **PROPOSED**.
[[B1_Exact_Owner_Decision_Batch]] presents the concise proposed batch and this exact file hash.
It is a companion summary, not a second approval register; actual answers belong in the existing
[[Next_Wave_Owner_Decision_Form]] and dated Decision Log after the Owner responds.

Recommended choice: accept this entire B1-PD-TYPED-1 contract/config and IMP-MATCH-03 synthetic-only
pure typed scope, including all new binding choices, then authorize TDD/independent review/one
Draft implementation PR. Alternatives are explicit separate methods/contracts: coverage-only fit=Q
with unchanged hard gates; the existing mc-b1-flat-positive-domain-p1 for complete General domains;
all-clause focus; match-all-positive; stricter global same-ID role ban; an actual synthetic alias
resolver. None is selected or implemented here. A changed material policy needs a revised exact
contract/identity and the applicable Planning/Owner gates, never the old name with hidden behavior.

Synthetic data/media/auth/storage preparation may continue independently and must not artificially
block this pure task after exact approval. Conversely, B1 synthetic approval cannot establish real
source closure, selected-use rights, no relevant held/conflicting observations, reviewed materialization,
eligibility, genuine nonadmin session, stack/publication choice or relevance/security acceptance.
All44holds,43normalization proposals, Khamrah, source/image rights and existing eligibility remain
untouched. No scraping, unlicensed assets, DB/Production mutation, automatic merge or real ranking.
