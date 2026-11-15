---
id: B1-EXACT-OWNER-BATCH-1
project: DoomParfum By TK
type: owner_decision_summary_proposal
status: awaiting-owner-exact-acceptance
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, synthetic, b1, owner-decisions]
source_of_truth: "../../README.md"
---

# One exact B1 Owner Decision Batch

**PROPOSED; Owner acceptance NOT RECORDED.** This is a concise companion summary, not a second
answer form or decision register. Record the actual Owner answer once in the existing
[[Next_Wave_Owner_Decision_Form]] and dated Decision Log. PR26 merged M1 only; its merge selects no B1 policy.

| Exact acceptance binding | Proposed value |
|---|---|
| Complete contract | [[B1_Positive_Domain_Typed_Contract]] |
| Contract ID | B1-PD-TYPED-1 |
| SHA-256 of exact UTF-8 LF file bytes | 77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977 |
| Method / config / schema | mc-b1-pyramid-positive-domain-p1 / b1-pd-typed-config-1 / b1-pd-typed-schema-1 |
| Implementation task | IMP-MATCH-03 — synthetic B1 pure typed scorer/query gates only, separate future branch/Draft PR |
| Preparation base | 604d447e599aa8359d3427dfbfbceaac85373e48; PR26 Owner merged, M1 preserved |

## Recommended one-batch choice

Accept the entire exact contract, including its new Python/schema/bounds/diagnostic bindings,
not only the headline80/20 weights. The proposed rule is **fit=(4/5)Coverage+(1/5)Focus**:

- Coverage Q = matched positive weight / all normalized positive weight, including unmatched optional clauses.
- Focus H = distinct matched positive `(note,layer)` occurrences / all candidate memberships in
  the accepted complete **positive** search domain. Excluded-only layers never enlarge it.
- Required-all and strict exclusions must pass; optional clauses are soft; at least one positive
  must match. Missing/incomplete/incompatible searched domains cannot prove absence or yield fit.
- Exact Top/Heart/Base selectors stay exact. any_pyramid requires all3accepted closed layers.
  Identical query clauses collapse; conflicting role/weight or same-ID any+exact combinations reject.
  Disjoint exact-layer roles remain compatible. Witness priority is Top,Heart,Base without reuse.

| Synthetic numeric example | Q | H | Proposed fit / display |
|---|---|---|---|
| required(x,top,1),optional(y,top,1); Top{x,y,z,w} | 1 | 1/2 | 9/10 /90.0 |
| optional(x,top,1),optional(y,top,1); Top{x,z} | 1/2 | 1/2 | 1/2 /50.0 |
| required(x,top,2),optional(y,heart,1); Top{x,z},Heart{q} | 2/3 | 1/3 | 3/5 /60.0 |
| x observed in incomplete required Top | unavailable | unavailable | null, unverified_required_domain |
| Complete Top{x},excluded y observed in compatible incomplete Base | 1 diagnostic | 1 diagnostic | null, rejected_excluded; no ranked0/100 |

These are proposed arithmetic/semantic examples, not executed B1 feature tests. Focus prefers fewer
unrequested declared notes, which is a model preference rather than measured smell quality. A one-note
query may fit1 but still reports unique-positive-note specificity1. Query Fit, Coverage, Data Confidence
and pair evidence remain separate; confidence/evidence are explicitly not evaluated for this milestone.

## Exact typed boundary and remaining alternatives

The proposed sole operation is `score_synthetic_b1(query,candidates,*,vocabulary,config)`.
All frozen classes/fields/configuration are mandatory. Canonical synthetic UUIDs only; no alias
resolver, transport DTO,8KiB parser or real-source lookup. Explicit limits:30raw clauses before
deduplication/30normalized,64candidates,512memberships per candidate including incomplete previews,
512vocabulary notes,positive integer weights1..5,excluded weight=None,128-character tokens,
128-bit numeric inputs and32768total memberships. The contract pins every input/output field,
query identity, error category, hard-rule precedence, diagnostic null, ordering and rounding rule.

| Alternative, not selected | Implication |
|---|---|
| Coverage-only fit=Q, same hard gates | Removes the extra-note focus penalty; needs a separately named/versioned exact method/config |
| Existing mc-b1-flat-positive-domain-p1 | Uses accepted complete General domains; no inferred pyramid, mixed-method rank or implicit fallback |
| All-clause focus, match-all-positive, global same-ID role ban, or alias resolver | Changes domain/role/input behavior; each needs a revised complete contract and applicable Owner/Planning gates |

No alternative is automatically chosen if input is incomplete. Synthetic completeness does not
establish real-source completeness, rights, selected provenance, normalization, eligibility or
application authorization. Data/media/auth/storage preparation is independent of this pure milestone.

## Proposed acceptance criteria and exact response

After exact Owner acceptance: verify main/hash again; create one isolated IMP-MATCH-03 branch;
write actual RED tests first; implement only the accepted pure B1; run MC-B01–14 and explicit
unsupported-flat MC-B15 negatives, all additional contract goldens/bounds/unknown/contradiction
tests, bounded properties and M1/math/research/adapter offline regressions. Complete independent
exact-source review, preserve original failures, create one scoped receipt and one Draft PR,
then stop for Human Owner. All future B1 runtime/golden/property tests are **NOT RUN** now.

Suggested whole-contract acceptance, only if the Owner chooses it:

> Accept B1-PD-TYPED-1 SHA-256 77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977,
> method mc-b1-pyramid-positive-domain-p1/config b1-pd-typed-config-1, including the proposed80/20
> formula and every exact typed fixture/schema/query/gate/diagnostic/order/bounds/error rule.
> Authorize IMP-MATCH-03 synthetic-only pure Python TDD, independent implementation review and
> one separate Draft PR after acceptance criteria. No Full Mode A/B2/real-data ranking/API/UI/
> transport/8KiB parser/DB or Production mutation, source/image acquisition, normalization promotion,
> 44-hold/eligibility change or agent merge.

This suggested response is not an answer already given. Owner may accept, request explicit changes
or defer; unanswered means unaccepted. A material change requires a revised exact contract/hash
and review before implementation. Existing M1 approval, tests, receipt and merge remain unchanged.
