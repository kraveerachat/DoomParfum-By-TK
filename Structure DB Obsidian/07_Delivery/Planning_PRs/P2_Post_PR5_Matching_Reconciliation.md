---
id: DPT-PLAN-003-POST-PR5
project: DoomParfum By TK
type: planning_reconciliation
status: proposed
owner: human-owner
updated: 2026-11-11
tags: [doomparfum, matching, planning, reconciliation]
source_of_truth: "../../../README.md"
---

# PR #4 Matching Plan — Post-PR5 Reconciliation

This is a docs-only correction to the existing DPT-PLAN-003 task/Planning PR #4, not another plan or
receipt. DM-01..07 remain PROPOSED, matching implementation NOT STARTED and this feature's Owner
Gate P PENDING. The existing immutable S1 receipt is preserved. Source intake approval is not matching
approval, a public-data publication grant, or proof that a structural percentage measures scent perception.

## Verified upstream state and authority

Pinned comparator main: 55d39cd619fa6c1ae70521720aa734d632a2083d. GitHub readback verifies:
PR #3 merged at a908711fb4f37a12fbec3665a461b75c288c7dab; PR #5 merged at55d39cd on
2026-11-11T15:11:16Z, published headce3510ddd43df0de469a89a013537ca04e227859. PR #4 remains OPEN/DRAFT.
This planning branch retains its original9636ee7 base; no merge/rebase was performed for reconciliation.

Merged P1/OD-01..06 and PR #3 govern the bounded private local intake implemented by PR #5. PR #3's
acquisition/evidence separation, partial-index and lifecycle proposals are upstream design context;
their historical pending-review wording does not undo the verified merge. That event does not accept
the additional DM weights, thresholds, absence/completeness or application decisions proposed here.
PR #3's A=evidence graph/B=structural search labels are a different decomposition from this plan's
A=perfume reference/B=custom query. Keep qualified names; neither turns community evidence into a
structural feature or makes a custom query into a real perfume pair.

Primary evidence: [merged PR #3](https://github.com/kraveerachat/DoomParfum-By-TK/pull/3),
[merged PR #5](https://github.com/kraveerachat/DoomParfum-By-TK/pull/5),
[pinned local ETL evidence](https://github.com/kraveerachat/DoomParfum-By-TK/blob/55d39cd619fa6c1ae70521720aa734d632a2083d/Structure%20DB%20Obsidian/08_Operations/Test_Evidence/IMP-P1-02_Licensed_Scento_Evidence.md),
[pinned adapter](https://github.com/kraveerachat/DoomParfum-By-TK/blob/55d39cd619fa6c1ae70521720aa734d632a2083d/database/scento_etl.py).
These merged files are read through the comparator; they are not copied into this older branch or
silently treated as runtime files present in its checkout.

## Actual local availability and boundaries

| Observed upstream artifact | Verified state | Matching implication |
|---|---|---|
| Approved P1 pilot | 12 profiles / 5 houses / 58 notes / 93 raw occurrences / 80 canonical links; 11 approved plus Khamrah held | Use this fixed cohort for later eligible-input audit; historical research12/11/46/84 is a separate fixture |
| Full private local catalogue | 1479 profiles / 160 brands / 420 notes / 12448 raw occurrences / 11972 canonical ordered links | 1435 exact-source approved records are not automatically eligible matching inputs |
| Review holds | 44 draft records =43 repeated-list profiles plus Khamrah external conflict;0 quarantined in the reported cohort | Preserve holds/ordinals and withhold scoring; no DISTINCT, fake resolution or implicit upgrade |
| Eligibility | All1479 matching_eligible flags false | Current real-data matching eligibility is0; no flag changes or read-model bypass in this planning PR |
| Accord inputs | Merged adapter imports no accord labels, links or observed strengths | Usable numeric strengths0; presence fallback is also unavailable until actual reviewed accord labels exist |
| Families/aliases/lifecycle/market | Raw source metadata may exist; this adapter does not materialize selected family, alias, region/position or lifecycle/stock inputs | No raw-field shortcut, family-to-accord inference, semantic alias/country merge or invented currentness |
| Completeness | Exact reported note arrays and selected claims retained; no accepted matching enumeration/absence policy established by PR #5 | Array presence or review_status=approved is not proof of a closed list or safe negative filter |
| Scope and rights | Operator-private catalogue/captures/notes; pinned Scento local rights only; no public publication | Matching adapter must use caller authorization and current uses; no admin read followed by post-filtering |
| Images/direct pairs | Acquired images0, verified usable Dupe pairs0 | Placeholder/none; no bottle, independent-source or Official Inspired By claim inferred from text leads |

The repeated-list totals are45 extra occurrences across43 profiles including general lists. Historical
40 extras/39 profiles counted top/heart/base only; general adds5/4. A flattened-list repeated-label
metric of149 profiles is a different counting unit. None is silently substituted for another.

PR #5's98/98 regression and source/replay review establish bounded ETL evidence, not any of this plan's
50 matching/API/UI/cache/privacy/performance acceptance cases. First import452.016s and current-source
replay291.219s are separate local runs; replay overlapped regression. They do not prove proposed5s
matching request caps, p95 targets, source capacity, restoration or hosted access isolation.

## Proposed capability gates after this plan's Owner merge

1. IMP-MATCH-01 first audits selected-field scope/rights, exact IDs, relevant conflicts, current
   matching_eligible=false state and a versioned complete-as-reported/absence policy. If eligibility
   materialization or allowlisted descriptors need change, use an explicitly scoped implementation
   design/migration review; never flip flags, read raw staging, or manufacture a relation in a read-only adapter.
2. A/B1 remain separate proposed milestones. Their pure scorers can be tested with clearly synthetic
   approved-contract fixtures after Gate P, but real-data results stay disabled until eligible inputs
   and completeness/domain evidence satisfy the contract. Unknown domains can have authorized metadata
   previews without a score; held drafts are not ranking candidates.
3. Notes-only A can later use the existing proposed missing-component formula, with actual coverage
   shown (three comparable layers yield C=0.50; complete flat fallback C=0.25). No absent accord/family
   dimension becomes zero, inferred evidence or high-confidence full-profile fit.
4. B2 numeric AND presence modes are disabled for this current real cohort. A user slider supplies a
   preference only, never missing candidate accord evidence. A synthetic numeric/presence fixture is
   a scorer test input, not a licensed data grant or real catalogue capability.
5. Currentness stays unknown where no selected usable lifecycle/market fact exists; strict market/price/
   region filters cannot be satisfied by raw source metadata or a brand-name guess. Missing image and
   direct evidence remain independent of whether eligible notes can eventually score.
6. The existing local private cohort cannot populate public links, public caches, anonymous results or
   cross-user counts. A private-seeded B draft remains private even if some vocabulary later becomes
   public. Public sharing requires deliberately public authorized inputs and a separately approved
   publication/access path; this plan grants none.

These are implementation acceptance prerequisites, not additional owner approvals for the completed
ETL. They refine existing DM-03/04/05/06/07 choices and IMP-MATCH dependencies; no source grant or
original DEC/OD/NEW table row is altered.

## DM-01..07 review recommendations — still PROPOSED

| Decision | Compatibility/recommendation for Owner review | Remaining choice |
|---|---|---|
| DM-01 | Keep independent A, B1 and B2 milestones; separate synthetic capability from available real data | Enable each only after its data/gate checks; B3 remains deferred |
| DM-02 | Keep structural/query fit, Data Confidence and direct pair evidence separate; compatible with PR #3 NEW-08/11 | Approve labels/tooltips; no sensory-equivalence or automatic Dupe claim |
| DM-03 | Retain50/30/20 and layer25/37.5/37.5 only as the existing proposal; explicitly show notes-only coverage | Owner decides/calibrates weights, comparable-layer/completeness and grouping thresholds |
| DM-04 | Keep compatible observed vectors and separate presence fallback; current real cohort supports neither | Approve scale/absence contract only with actual permissioned data; no invented strength |
| DM-05 | Retain80/20 B1 coverage/focus and strict unknown negatives as proposals; no assumed complete lists | Owner decides requested-domain closure, hard rules, specificity and unknown preview behavior |
| DM-06 | Keep production distinct from market stock, unknown visible, historical opt-in; consistent with merged PR #3 | Define selected status facts/TTL and any needed field/schema gap before real filters |
| DM-07 | Keep framework-neutral read-only ephemeral search, scoped cache/revocation and public-only safe sharing | Stack/API/auth/capacity remain later choices; local postgres-admin intake is not the app auth design |

No matching weights, scale, availability TTL, completeness/absence assumption, runtime stack, hosted
provider or performance target becomes accepted through this reconciliation or PR #5 merge.

## Review, merge simulations and continuity

[[DPT-PLAN-003_Documentation_Evidence]] records exact current document checks, preserved fingerprints
and simulations. The existing seven shared paths are checked with git merge-file in both orders
against pinned main, using the true merge base; simulation is not a branch merge or semantic approval.
Current mergeability must be rechecked before owner action; later branch/main edits can change it.

[[DPT-PLAN-003_Dual_Mode_Matching]] tracks S2 and independent review. The S1 receipt stays immutable;
no second receipt. Remaining action is Human Owner review/decisions and eventual merge of existing
Draft PR #4, followed only by separately scoped implementation work. No matching runtime, DB, tests,
external source acquisition, unlicensed imagery, cloud or production changes occur here.
