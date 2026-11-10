---
id: DPT-DAT-009
project: DoomParfum By TK
type: conflict_matrix
status: draft
owner: project
updated: 2026-11-10
tags: [doomparfum, planning, conflicts]
source_of_truth: "../../README.md"
---

# P1 Data Conflict Matrix

Observed cases below are research evidence. Proposed responses are unapproved design choices.
Source revision, acquisition method and denominators: [[P1_Data_Profiling_Findings]].

| ID | Kind / observed evidence | Proposed handling / effect |
|---|---|---|
| CF-01 | Balmain Bleu Infini has two source IDs, same house/name, different EDP/EDT concentrations | Keep two scent identities; name-only unique constraint rejected; not confirmed duplicate |
| CF-02 | Scento Khamrah heart includes Mahonial; [official structured list](https://lattafa.com/product/khamrah/) includes Lily Of The Valley; official prose differs from its structured list | Preserve whole-list claims with section locators; unresolved conflict, no synonym merge or majority vote |
| CF-03 | Khamrah base labels vary: e.g. generic vs origin-specific benzoin/tonka wording | Candidate narrower/broader semantic mappings; require review; not proof of new formula |
| CF-04 | Butterfly home shows 1,395 THB for Agarwood & Benzoin; linked detail shows THB `n/a` | Distinct location/time observations; unknown detail price does not overwrite known homepage amount; no size inference |
| CF-05 | Scento README, developer pages and OpenAPI advertise differing totals | Use pinned observed 1,479/160/420 for this analysis; live marketing totals are dated claims, not measured coverage |
| CF-06 | Scento family system is named; material table includes accord-type labels; no perfume weighted-accord relation | Preserve taxonomy scheme and term meaning; do not invent main accord strengths |
| CF-07 | 91 flat-only profiles; old ERD restricted note layer to top/heart/base | Add general layer and record unknown layering; no arbitrary allocation |
| CF-08 | Two missing countries; old dictionary required country and market position | Make optional; separate country and source-specific positioning tags |
| CF-09 | API example uses spaced concentration labels, export uses hyphenated labels | Versioned normalization map, raw observation retained; no claim of successful live API comparison |
| CF-10 | Materials contain aliases and distinct natural/synthetic/accord concepts | Alias lookup returns candidates; no automatic Ambergris = Ambroxan or broad/narrow note collapse |
| CF-11 | Old rights note implied public facts / personal fair use permit reuse | Replace with content-specific grant assessment; public visibility is not an import/license grant |
| CF-12 | README/status/roadmap still ask for a workflow despite committed AGENTS/workflow and bootstrap SHA | Record baseline discrepancy; retain proposed governance status; this authorized docs-only PR follows human merge gate |

## Unobserved cases to test later

These are proposed negative controls, not defects observed in the snapshot: alias collisions across
languages, reused source keys with changed payloads, invalid URLs, source withdrawal, corrupted image
bytes, mismatched purchase owner/variant, and contradictory independent pairwise review claims.

## Resolution contract

Keep immutable source observations and rights references. A `data_conflicts` row identifies one
entity/field; `conflict_members` reference its competing observations. A human resolution selects an
observation, records rationale/actor/time, and changes the canonical selection in one transaction.
Missing or stale is not disagreement. A newer timestamp is not automatic authority. Whole note lists
must be compared as sets plus recorded order/layer; never union contradictory lists into a fake profile.

No conflict above is marked resolved by this planning PR. See [[Ingestion_and_ETL]].
