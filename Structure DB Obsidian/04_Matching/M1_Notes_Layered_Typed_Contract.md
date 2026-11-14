---
id: M1-NL-TYPED-1
project: DoomParfum By TK
type: exact_owner_contract_proposal
status: awaiting-owner-acceptance
owner: human-owner
updated: 2026-11-14
tags: [doomparfum, synthetic, matching, exact-contract, owner-gate]
source_of_truth: "../../README.md"
---

# M1-NL-TYPED-1 — exact synthetic notes-layered contract

**PROPOSED / NOT ACCEPTED. No policy-dependent implementation is authorized yet.**
Owner-requested target method `mc-a-notes-layered-p1`; proposed typed configuration `m1-nl-typed-config-1`;
input/result schema `m1-nl-typed-schema-1`. This complete proposal selects the existing merged
notes-layered method unchanged and makes previously unspecified Python/fixture/resource boundaries
explicit. Those new binding choices require the Owner's acceptance too; they are not old defaults.

## 1. Authority, scope and task boundary

Verified base main0da217671ec6473716eea5947f013d44e6fd91cb includes Owner-merged22–25.
Normative mathematical proposal: [[Matching_Method_Contracts_and_Golden_Cases]], canonical Git
SHA256f09999add47c820dab0ccb96db0ed0876b80f92a05f198237201ef39187158a8; selected row
mc-a-notes-layered-p1,common layered notes,comparability and rounding sections. See also merged
[[Synthetic_Implementation_Unlock_Checklist]]. Merge is not this exact contract's acceptance.

M1 is synthetic fixture comparison only. It does not complete Full Mode A or the old full
IMP-MATCH-02 milestone. Proposed task allocation upon acceptance: **IMP-MATCH-08**, one isolated
implementation branch and one Draft implementation PR. PR9 remains its merged generic-primitives
milestone; do not issue a retrospective receipt or reuse its completed branch. No B1/B2,accord,
family,flat,automatic fallback,normalizer,real-data ranking,source acquisition,database/API/UI,
transport serialization/parser,8KiB byte-boundary,cache,cloud or app-auth implementation in M1.

The sole public operation is a pure typed-input Python batch scorer:
`score_synthetic_notes_layered(reference, candidates, *, vocabulary, config) -> M1BatchResult`.
The batch envelope is proposed here to make synthetic partition/order/tie behavior testable;
it is not an application route. All four arguments are required. No default configuration,
environment lookup,filesystem,network,database,clock,randomness or mutable global state.

## 2. Exact immutable input schema — proposed Python binding

Value objects are frozen dataclasses. Accept exact declared classes and exact builtin containers,
not subclasses,custom mappings,iterators,generators,coercible objects or attribute-based duck types.
These shape descriptions are specifications,not implemented classes or a DTO/parser.

| Object | Required fields,with no constructor defaults |
|---|---|
| M1Config | method_id,config_id,schema_id,layer_weights,min_comparable_layers,note_support_budget,max_candidates,max_memberships_per_profile,max_vocabulary_notes,max_identifier_chars,max_numeric_bits,max_total_memberships |
| FixtureVocabulary | vocabulary_version,vocabulary_fingerprint,domain_version,transform_version,selection_snapshot_id,scope_id,note_ids |
| FixtureProfile | perfume_id,top,heart,base |
| FixtureLayer | notes,completeness_assertion_id,selected_claim_id,capture_id,revision_id,selection_snapshot_id,scope_id |

`candidates` is an exact tuple of FixtureProfile; `reference` is an exact FixtureProfile.
Each top/heart/base is an exact FixtureLayer or None. FixtureLayer.notes is an exact existing
matching_math.primitives.SetInput: exact frozenset of note-ID strings,explicit Boolean complete,
explicit domain_id. A raw repeated list is not accepted or deduplicated; raw source arrays are out
of scope. A note in Top and Base remains two layer memberships and counts twice against the cap.
`heart` is the canonical field name for Middle/Heart;this typed API introduces no alias parser.

FixtureVocabulary declares one common context for the entire call:

| Field | Exact proposal |
|---|---|
| vocabulary_version | `synth-notes-m1-v1` |
| domain_version | `synth-pyramid-domains-m1-v1` |
| transform_version | `canonical-set-fixture-m1-v1`;declares already canonical fixture sets,performs no transform |
| selection_snapshot_id | `synth-selection-m1-v1` |
| scope_id | `synth-scope-m1-v1` |
| note_ids | exact frozenset of0..512valid synthetic note IDs |
| vocabulary_fingerprint | caller-supplied64lowercase hex SHA256,matching the sorted note_ids joined by oneASCII LF,with no terminalLF;empty vocabulary hashes empty bytes |

That bounded fingerprint defines vocabulary identity only; it is not API request serialization
or a rights/security signature. It must be supplied and verified,never silently filled. Include
both vocabulary version and fingerprint in comparisons so different fixture vocabularies cannot
masquerade as one version. The scorer validates only these declared synthetic inputs,not real
licensing,selection review,authenticity,closure,ownership or eligibility. No real adapter is called.

Canonical fixture IDs are exact lowercase36-character UUID strings with fixed test namespaces:
perfume IDs `10000000-0000-4000-8000-` followed by12lowercase hexadecimal digits representing a
nonzero value; note IDs use prefix `20000000-0000-4000-8000-` with the same nonzero suffix rule.
These are declared test identities,not real product/note facts. Do not claim the prefix proves a
real source cannot forge an ID. Real-data activation remains absent by scope and integration.
Every layer note ID must belong to the supplied vocabulary. Reference/candidate IDs must differ;
candidate IDs must be unique. Same names/shared notes never collapse identities or editions.

All other identifier tokens(including SetInput.domain_id and lineage IDs) are exact strings of
1..128ASCII characters matching `[A-Za-z0-9][A-Za-z0-9._:-]*`;no trimming,case-folding,aliases or
coercion. The fingerprint has its stricter64hex rule. No arbitrary prose,URLs,paths or raw records.
Layer scope_id and selection_snapshot_id must equal the call context. Complete=True requires a
non-null bounded completeness_assertion_id;complete=False requires that field=None. Each present
layer needs bounded selected_claim_id,capture_id andrevision_id. These are caller-declared fixture
lineage,not evidence that real source rights or closure passed. Missing layers are represented
only by None,not fabricated empty complete sets.

## 3. Exact configuration,counts and numeric limits

Every field below is caller-supplied and must equal the accepted profile; changing one under the
same config_id is invalid. A different policy/bound needs a separately versioned accepted profile.

| Config field | Exact proposed value |
|---|---|
| method_id | `mc-a-notes-layered-p1` |
| config_id | `m1-nl-typed-config-1` |
| schema_id | `m1-nl-typed-schema-1` |
| layer_weights | exact tuple(1/4,3/8,3/8),Top/Heart/Base in that order |
| min_comparable_layers | exact int2 |
| note_support_budget | exact1/2 |
| max_candidates | exact int64;actual tuple count0..64 |
| max_memberships_per_profile | exact int512,sum of all present layer-set lengths,including incomplete previews;reference and each candidate independently bounded |
| max_vocabulary_notes | exact int512 |
| max_identifier_chars | exact int128;UUIDs/fingerprint additionally fixed-width |
| max_numeric_bits | exact int128 for each supplied integer or reducedFraction numerator/positive denominator |
| max_total_memberships | exact int33280=(64+1)*512;sum of actual reference plus all candidates |

Config count fields require exact int,not bool. Numeric weights/support require exact int or
fractions.Fraction,not subclasses,bool,float,Decimal,NaN/infinity or expression strings. Check
input numeric bit lengths before arithmetic/config equality. Values must be finite/in the declared
unit interval and equal the prescribed weights/support. No float conversion,eval,clipping or
implicit renormalization of a caller-supplied alternative. Derived result fractions use exact
arithmetic;their finite size follows the bounded cardinalities and fixed three weights.

Entry validation order: exact top-level types and tuple length;config identifier/count/numeric
types/bit sizes/equality;vocabulary count before member/fingerprint work;profile/layer types and
all set lengths,total counts and token lengths before member validation/set arithmetic;identity,
vocabulary membership and fixture-lineage consistency;then scoring. Reject an overlong raw tuple
before any duplicate reconciliation(there is none). Validate all profiles before returning any
result. Builtin len checks precede scans; no over-bound set unions/intersections/sorting. This bounds
scorer work,not memory/time already spent constructing caller objects outside the function.

Use TypeError for invalid declared types and ValueError for invalid shape/value/config/ID/bounds/
lineage. Errors use bounded fixed category text,not object repr,source data or partial scores.
There is no fallback on error,unsupported method or missing config. Empty candidates returns an
empty groups/unranked result after validating reference,vocabulary andconfig;it is not a match.
No latency/capacity/SLA claim follows from64/512;future bounded fixtures test the limits.

## 4. Layer evaluation — unchanged merged method

Process Top,Heart,Base in fixed order. For each layer use existing set_jaccard semantics and
reason precedence: missing_input before incomplete_input before domain_mismatch before empty_union.
None on either side is missing_input;present incomplete on either side is incomplete_input;
otherwise distinct valid domain_id strings are domain_mismatch. These are unavailable comparison
states,not malformed-type exceptions. Shape-invalid metadata still rejects the whole call first.

When both sides are complete and domain_id equal, J[l]=intersection_count/union_count if union>0.
Complete empty versus nonempty and disjoint nonempty sets give known numeric0 and contribute.
Both complete empty gives null/empty_union and contributes no layer weight. Do not infer empty
from None/incomplete. For unavailable layers,intersection/union numeric fields are None except
both complete empty has known counts0/0;never compute a preview score from incomplete sets.

L is exactly the numeric-J layers,including known0. p=(1/4,3/8,3/8).
Observed layer support=sum(p[l] for l in L),always a separately named diagnostic.
If |L|>=2:

`N = sum(p[l]*J[l] for l in L) / sum(p[l] for l in L)`

`fit=N; scoring_coverage=(1/2)*sum(p[l] for l in L); reason=computed`.

If |L|<2:fit=None,reason=insufficient_layers,scoring_coverage=Fraction(0),andno ranked partition.
Observed support may still be nonzero;it cannot rescue fit or become scoring coverage. N's
denominator is the comparable weight sum;support's original denominator remains1. Fit1 may have
coverage1/2 or3/8;neither is measured smell similarity,accuracy or Data Confidence.

No accord/family values are inputs. Excluding them is a declared notes-only method,not automatic
fallback from full Mode A. No flat method,available-components method or other version is accepted.

## 5. Partition,ordering and exact immutable result

Return M1BatchResult with method_id,config_id,schema_id,vocabulary/domain/transform/snapshot metadata,
tuple of ranked PartitionResult groups,andtuple of unranked PairResult. Groups are a presentation
of incomparable partitions,not one global score ranking. No global rank,best-match or confidence band.

A numeric partition key contains exact method/config/schema versions,component mask(notes,),
numeric layer mask,vocabulary_version/fingerprint,domain_version,transform_version,common fixture
selection snapshot andscope,andthe actual equal domain_id for each comparable layer. Candidate
ID,unique claim IDs,capture/revision IDs andcompleteness assertion IDs are provenance only,not
partition keys;do not create singleton partitions merely because claims differ.

Order group keys deterministically by numeric layer bitmask(Top1,Heart2,Base4),then their bounded
metadata/domain strings lexicographically. Within one exact key sort exact unrounded fit descending,
then canonical perfume UUID ascending. Unavailable candidates appear separately sorted by UUID,
with no rank. Never sort fits across layer/domain/method partitions. All candidate results retain
the reference/candidate IDs and original role-labelled fixture lineage for explanation.

Each PairResult has exact fit Fraction or None,reason,scoring_coverage Fraction,
observed_layer_support Fraction,note_score_denominator Fraction orNone(onlynumericfit),comparable
layer mask,partition_key orNone,structural_fit_percent_display str orNone,confidence_state exactly
`not_evaluated_policy_pending`,andpair_evidence_state exactly `not_evaluated_synthetic_only`.
There are no real pair claims or badges. Each fixed-order layer explanation contains layer name,
left/right declared completeness/missing state,domain IDs,reason,numeric J orNone,intersection/
union counts as allowed above,original weight,andthe exact fixture-lineage fields supplied.
Do not include full note lists,arbitrary prose or opaque user payloads in results.

Percentage is display only. For numeric x=fit,calculate tenths=floor(1000*x+1/2) with exact integer/
Fraction arithmetic;render tenths divided by10 with exactly one decimal digit and no percent sign.
Examples:1/16 -> `6.3`;0 -> `0.0`;1 -> `100.0`. Null display is None. Sort before rounding;never
use float,confidence,pair evidence,input order,lifecycle,market or rounded ties as ranking policy.

### Complete required output schema — no implementer-selected fields

All output records below are exact frozen dataclasses;all sequence fields are exact tuples.
Every numeric result is an exact Fraction or the explicitly permitted None;counts are exact int,
never bool. Metadata-only output does not retain the input FixtureVocabulary object or note_ids.
`LayerName` is one of the literal strings `top`,`heart`,`base`;every layer-mask tuple is in that
fixed order,with no duplicates. Tokens/IDs retain their validated input values without coercion.

| Record | Complete required field names and exact types/values |
|---|---|
| M1BatchResult | method_id:str,config_id:str,schema_id:str,reference_id:str,vocabulary_version:str,vocabulary_fingerprint:str,domain_version:str,transform_version:str,selection_snapshot_id:str,scope_id:str,groups:tuple[PartitionResult,...],unranked:tuple[PairResult,...] |
| LayerDomain | layer:LayerName,domain_id:str;one equal reference/candidate domain for a numeric layer |
| PartitionKey | method_id:str,config_id:str,schema_id:str,component_mask:tuple[str,...] exactly(notes,),comparable_layer_mask:tuple[LayerName,...],vocabulary_version:str,vocabulary_fingerprint:str,domain_version:str,transform_version:str,selection_snapshot_id:str,scope_id:str,layer_domains:tuple[LayerDomain,...] |
| PartitionResult | key:PartitionKey,results:tuple[PairResult,...];nonempty numeric results,all with that exact key |
| PairResult | method_id:str,config_id:str,schema_id:str,reference_id:str,candidate_id:str,fit:Fraction-or-None,reason:str,scoring_coverage:Fraction,observed_layer_support:Fraction,note_score_denominator:Fraction-or-None,comparable_layer_mask:tuple[LayerName,...],partition_key:PartitionKey-or-None,structural_fit_percent_display:str-or-None,confidence_state:str,pair_evidence_state:str,layers:tuple[LayerExplanation,...] |
| FixtureLineage | completeness_assertion_id:str-or-None,selected_claim_id:str,capture_id:str,revision_id:str,selection_snapshot_id:str,scope_id:str |
| LayerSide | state:str,declared_complete:bool-or-None,domain_id:str-or-None,lineage:FixtureLineage-or-None;left is reference,right is candidate |
| LayerExplanation | layer:LayerName,left:LayerSide,right:LayerSide,reason:str,jaccard:Fraction-or-None,intersection_count:int-or-None,union_count:int-or-None,original_weight:Fraction |

Batch/group/pair method/config/schema values must equal the validated call values. Batchcontext
copies only its validated bounded strings. PartitionKey copies the same shared context plus the
numeric mask/domain tuple. Candidate/claim/capture/assertion IDs never enter that key. Groups are
0..4unique numeric masks(Top/Heart,Top/Base,Heart/Base,all3);each results tuple is length1..64.
Total ranked plus unranked results equals input candidate count;no candidate disappears or repeats.
Unranked length0..64. Each PairResult.layers has exactly3explanations in Top/Heart/Base order.
There is no per-item global rank or undeclared extra payload field.

For group ordering,the exact comparison tuple is(mask_bits,method_id,config_id,schema_id,
component_mask,vocabulary_version,vocabulary_fingerprint,domain_version,transform_version,
selection_snapshot_id,scope_id,tuple((layer,domain_id) for layer_domains)). This only orders group
presentation. All groups belong to one Batch.reference_id;there is no authorized cross-batch merge.

Numeric pair:reason exactly `computed`,fit in[0,1],partition_key non-null,mask length2or3,
note_score_denominator equals observed_layer_support,coverage exactly half that support,anddisplay
is a non-null string from the rounding rule. Null pair:reason exactly `insufficient_layers`,fit/
partition_key/note_score_denominator/display all None,coverage exactly0,mask length0or1;observed
support remains its separately named Fraction. Confidence/evidence states are the exact constants
already specified above in both cases.

LayerSide state `missing`:declared_complete/domain_id/lineage all None. State `incomplete`:
declared_complete=False,domain_id validstr,lineage present with completeness_assertion_id None. State `complete`:
declared_complete=True,domain_id validstr,lineage present with its required assertion string.
Every present lineage copies only the six validated FixtureLineage fields in the table.

Layer reason exactly `computed`:J is Fraction,counts are known integers,union>0,intersection>=0
andJ=intersection/union. Reason exactly `empty_union`:J=None,counts0/0. Reasons `missing_input`,
`incomplete_input` or `domain_mismatch`:J/counts all None,even when preview sets look empty. This
explicit rule obeys reason precedence;domain-mismatched empty sets do not become empty_union.
original_weight is the prescribed Fraction for that layer in every state. No omitted layer record.

## 6. Exact future TDD acceptance oracles — NOT RUN

Fixture G uses canonical test-note symbols x,y,z,h,b1,b2,b3 as namespace suffix1..7 respectively.
Reference top{x,y},heart{h},base{b1,b2};candidate top{x,z},heart{h},base{b2,b3};all complete,
same per-layer domains and valid declared fixture context/lineage.

| Case | Exact proposed M1 expectation |
|---|---|
| G | J=(1/3,1,1/3);fit7/12,coverage1/2,observed support1,display58.3 |
| G with Top missing | fit2/3,coverage3/8,display66.7,Heart/Base mask;Topreasonmissing_input |
| Top known complete empty/nonempty;Heart/Base identical | fit3/4,coverage1/2,display75.0;knownTop0contributes |
| Top incomplete;Heart/Base identical | fit1,coverage3/8,display100.0;Topreasonincomplete_input |
| OnlyTopnumericJ1 | fitNone/insufficient_layers,scoringcoverage0,observedsupport1/4,displayNone,unranked |
| Topbothcompleteempty;Heart/Base identical | fit1,coverage3/8,display100.0;Topreasonempty_union |
| All3knownnumeric0 | fit0,coverage1/2,display0.0;rankable known mismatch |
| All3bothcompleteempty | allJNone,fitNone,coverage0,observedsupport0;unranked |
| Topdomainmismatch;Heart/Base identical | fit1,coverage3/8;Topdomain_mismatch,not fabricated0 |
| Missing config/cross-method config | reject;no default/fallback result |

Do not use strict-full MC-A01/02/03fit/C as the notes-only oracles. Project only their N/layer
observations into this explicitly selected method; MC-A05/07/08already exercise notes-only cases.

For a feasible sort-before-rounding fixture,use reference Top note suffixes1..339,Heart{341,342},
Base{343,344}. Candidate H Top1..170,Heart{341},Base{343};candidate L has same but adds Top340.
Then H has Jtop170/339,otherJ1/2,fit1357/2712;L has Jtop1/2,fit1/2. Both display50.0 in the same
partition,butH sorts first even if its UUID is greater. Each profile has<=512memberships andthe
vocabulary needs344notes. Equal exact fit ties instead use UUID ascending.

After exact acceptance,write failing tests for absent scorer:these selected-method goldens,
minimum2layers,reason precedence,unknown/zero/empty,candidate tuple/set iteration/labeled-field
construction permutations,UUID ties,
partition isolation,rational precision/display,immutable deterministic explanations,all malformed
type/config/metadata cases,andboundaries0/64/65candidates,512/513memberships(reference too),
512/513vocabulary,128/129token lengths/number bits,33280total cap,no custom iterables/subclasses,
duplicate/self IDs,vocabulary fingerprint mismatch,complete/assertion inconsistency,wrong scope/
snapshot andno hidden defaults. Symmetry applies to pair fit/support under identical configuration;
role-labelled lineage need not be identical when roles swap. Existing regressions and meaningful
bounded property checks follow implementation;no test here is reported as executed scorer PASS.
Permutation invariance never means reassigning a note from Top to Heart/Base. Those are different
weighted domains and may change the fit,mask,coverage or reason;layer roles are fixed by field name.

## 7. One exact Owner acceptance record

Owner/date/reference: **NOT RECORDED**. Accepted version/hash: **NOT RECORDED**.
Recommended response after reviewing the exact file/hash:

> Accept M1-NL-TYPED-1,method mc-a-notes-layered-p1/config m1-nl-typed-config-1,
> synthetic-only pure typed Python scope including its explicit fixture/schema/resource/error/
> partition/explanation rules. Allocate IMP-MATCH-08 to this bounded M1 milestone;authorize one
> isolated implementation branch and Draft PR after fresh baseline verification. No Full Mode A,
> B1/B2,transport/8KiB parser,real data,DB/API/UI,source/image rights or hold/eligibility changes.

This is a suggested answer,not an Owner decision. Owner may modify or defer;then update and
re-review the complete version before implementing. A semantic change must not silently retain
the old method/config identity. Do not treat an elapsed wait,merge or earlier strategic direction
as acceptance. Once accepted,use TDD,focused/fulloffline/appropriateproperty tests,independent
exact-code review andone scoped implementation receipt/one Draft PR;Human Owner alone merges.

Data/media/session work and the separate [[M1_Next_B1_Owner_Packet]] may continue independently.
Their unaccepted gates do not artificially block this isolated synthetic M1. Conversely M1acceptance
does not approve real-source closure/43projections,Khamrah,rights,app principals orstack. PR8remains
blocked without attributable historical operands. Existing receipts/migrations are preserved.
