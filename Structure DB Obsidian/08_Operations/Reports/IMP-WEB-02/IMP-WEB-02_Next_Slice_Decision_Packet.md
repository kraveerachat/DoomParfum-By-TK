---
id: IMP-WEB-02-NEXT-SLICE-DECISION-PACKET
project: DoomParfum By TK
type: decision_packet
status: proposed-unanswered
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, handoff, read-only-catalogue, owner-decisions, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# Decision packet: the smallest real-data read-only catalogue slice

PUBLIC_SAFE. For the Owner. Prepared at the close of IMP-WEB-02 (S9, 2026-11-28) under the instruction "IMP-WEB-02 — Final 404 Resolution and Closeout", §5. It **consolidates** existing merged planning into one ordered list of decisions. It creates no new design, answers no decision, allocates no task ID and authorizes no implementation. **The next implementation task is not started.**

## What this packet reuses

| Source | State |
|---|---|
| [[Post_PR30_Owner_Decision_Packet]] (POST30-ODP-1, revision 1, frozen SHA-256 `e828e0942037793b6d86c73de95b3c3511cba96b25eb267e13fb4f64ae1ed27c` in `Test_Evidence/Post_PR30_Packet_Freeze.json`) | Merged with DPT-PLAN-011 (PR #31). **All 15 rows PROPOSED / UNANSWERED** |
| [[Post_PR30_Dependency_and_Gate_Map]], [[Post_PR30_First_Readonly_Web_Slice_ADR]], [[Post_PR30_Principal_and_Authorization_Plan]] | Merged; define the slice P30-U03 → U05 → U06 → U07, fed by U01, U02 and U04 |
| DPT-GATE-012 (PR #32, documentation snapshot) | P30-U01 field-review contract: latest r14 **PROPOSED**, independent review (G-IND) **not satisfied**, Q-F pending, 0 of 169 acceptance specifications run |
| [[IMP-WEB-02_Next_Development_Handoff]] (S8) | Current-state table and gate order; still accurate except the 404 item, now fixed (S9) |
| IMP-WEB-02 V1.1 frontend, final candidate `53d0126` | Visual baseline accepted by the Owner; 404 documents server-rendered in both languages (S9). Mock-only, local only, not merged |

Current data remains **43 DEFER / 3 UNKNOWN / 0 ACCEPT**. Nothing is accepted for display, so the first live catalogue may honestly show zero items.

## The slice in one line

A real login subject with least-privilege read grants (U03) → a read-only repository over reviewed, selected, rights-current fields (U05) → a strict read-only service with versioned DTOs and the READ-V1 bounds (U06) → a private catalogue and detail UI with text placeholders and honest unknown states (U07). Data prerequisites: U01 human field review, U02 canonical identity and edition mapping, U04 bounded transition of reviewed claims. Matching, media, Cart/Collection and deployment are **not** part of it.

## Decisions in the Owner's priority order

Each row names the POST30-ODP-1 decision, its recommended option (a recommendation, not an answer), the alternatives, and what an answer would unlock. Dispositions: ACCEPT-DESIGN, REJECT, DEFER, REQUEST-REVISION.

### 1. Outstanding security review (gates everything that touches real data)

| Item | Needed | Unlocks | Blocked by |
|---|---|---|---|
| **G-IND for P30-U01 r14** | Owner commissions an independent review of the r14 field-review contract (DPT-GATE-012), then makes the security-design decision; Q-F answered | Execution of U01 human field review under an accepted contract | Owner action only |

No agent can satisfy G-IND for its own work. Until it passes, no claim can be reviewed, so no real field can be displayed.

### 2. Data field acceptance

| Decision | Recommended | Alternatives | Unlocks |
|---|---|---|---|
| **DATA-01** | DATA01-REVIEW46-NO-PROMOTION | DEFER-REVIEW; NARROW-CLAIMS (revised exact subset) | U01: human review of the 46 slots, without promotion |
| **DATA-03** | DATA03-SELECTED-USE-GATE | PROVENANCE-REVIEW-ONLY; DEFER-DISPLAY | U04/U05: only claims accepted *and* selected for display can reach the repository |
| **DATA-04** | DATA04-UNKNOWN-NO-CLOSURE | DEFER-ABSENCE-SENSITIVE-METHODS; REVISE-DOMAIN-POLICY | U01: unknown stays unknown; absence is never read as "none" |

After the decisions, the actual per-claim review is human work by the Owner; the agent prepares, never decides.

### 3. Canonical mapping

| Decision | Recommended | Alternatives | Unlocks |
|---|---|---|---|
| **DATA-02** | DATA02-EXPLICIT-IDENTITY-EDITION | DEFER-IDENTITY; NARROW-ENTITY-SUBSET | U02: explicit perfume identity and edition mapping |
| **DATA-05** | DATA05-PRESERVE-HOLDS-VERSIONED | DEFER-ALL-TRANSITIONS; NARROW-REVIEW-ONLY | U02/U04: the 44 holds and 43 proposals stay versioned; no silent release |

### 4. Least-privilege application principal

| Decision | Recommended | Alternatives | Unlocks |
|---|---|---|---|
| **APP-04** | APP04-PER-SUBJECT-LOGIN-CLEAN | SEPARATELY-REVIEWED-ISSUER-AMENDMENT; DEFER-APPLICATION-ACCESS | U03: a genuine per-subject login and its own read grants in a new private scope |

The existing `dpt_runtime` role and `read_profile` are explicitly **not** acceptable application authority (principal plan). An optional read-only revalidation of the current database roles, grants and schema contract can be run first, as evidence for this decision, if the Owner wants it (no new authority needed for a read-only check, but it is a separate session).

### 5. Repository

| Decision | Recommended | Alternatives | Unlocks |
|---|---|---|---|
| **APP-05** | APP05-READONLY-CATALOGUE-DETAIL | STATIC-SHELL-ONLY; NARROW-ACCEPTED-FIELDS; DEFER-SLICE | U05: catalogue and detail projections only; authorize before lookup, count or filter |

### 6. Read-only API

| Decision | Recommended | Alternatives | Unlocks |
|---|---|---|---|
| **APP-01** | APP01-C-PYTHON-SEPARATE | APP01-A-CLI; APP01-B-PYTHON-INTEGRATED; APP01-D-TS-BRIDGE | Backend direction for U03/U06/U07 |
| **APP-02** | APP02-EVALUATE-FASTAPI | EVALUATE-OTHER-NAMED-PYTHON-FRAMEWORK; DEFER-BACKEND-SELECTION | A framework *evaluation* (not an install) |
| **APP-06** | APP06-READ-V1-BOUNDS | REVISE-EXACT-DTO-BUDGET; DEFER-TRANSPORT | U06 request/response bounds (POST30-READ-1 / READ-BUDGET-1) |
| **APP-07** | APP07-NOSTORE-NOOFFLINE | SEPARATE-EXACT-CACHE-PROPOSAL; DEFER-APPLICATION | no-store and no offline copies end to end |

### 7. UI hosting and the existing Next.js frontend (APP-03)

| Decision | Recommended in POST30-ODP-1 | Alternative that uses V1.1 | Third option |
|---|---|---|---|
| **APP-03** | APP03-COHOSTED-MINIMAL (small presentation cohosted with the backend, logically separate UI) | **SEPARATE-UI-SERVER (new contract)**: the accepted Next.js V1.1 frontend becomes the separate live UI server | DEFER-UI |

This instruction states the Owner's preference: **treat the Next.js V1.1 frontend as the preferred candidate for the separate UI server, pending the exact APP-03 decision.** That is the packet's alternative, not its recommendation, so choosing it means answering APP-03 with SEPARATE-UI-SERVER and then accepting a new UI contract. What that contract would have to settle, from the IMP-WEB-02 evidence:

| Topic | Why it matters for V1.1 as the live UI |
|---|---|
| Data path | The UI reads only the U06 service DTOs, server side; no database driver, SQL or adapter DTO in Next.js; nothing private in client chunks (today's `scan:output` check extends to this) |
| Session and login | U03/APP-04 subject login handled without new auth SDKs until accepted; no private prefetch (`prefetch={false}` is already the pattern) |
| Caching | APP-07: `no-store` and nonce CSP already on every response; must stay so with live data |
| 404 for live records | S9 sends unknown detail slugs to the global 404 by checking the **fixture** slug list in the proxy. With live data the proxy cannot know valid slugs; the contract must choose how an unknown live record is answered (for example a service lookup before rendering) so 404s stay server-rendered and localized. `notFound()` inside a page still produces the framework error document with two root layouts |
| Experimental dependency | `experimental.globalNotFound` is Owner-authorized only for the pinned Next.js 16.4.6 and the local mock; it must be reassessed before any framework upgrade, live data or deployment |
| Unknown states and rights | Text placeholders for images; honest unknown/empty states (already in the mock); real matching disabled |
| Localization | Thai wording of live records is not reviewed; the Thai overlay covers fixtures only |

If APP-03 stays COHOSTED-MINIMAL instead, V1.1 remains the visual reference, and its components would be re-used only through a separate contract.

### Sequence

| Decision | Recommended | Alternatives |
|---|---|---|
| **SEQ-01** | SEQ01-SMALL-READONLY-UNITS | CLI-ONLY-DEFER-WEB; OWNED-MOCK-UI-FIRST; REVISE-SEQUENCE |

Not needed for this slice: **MEDIA-01**, **MEDIA-02** (the slice uses text placeholders).

## Suggested order of Owner actions

1. Commission G-IND for U01 r14 (item 1).
2. Answer SEQ-01, DATA-01 to DATA-05 (items 2–3).
3. Answer APP-04, APP-05, APP-01, APP-02, APP-06, APP-07 (items 4–6).
4. Answer APP-03; if SEPARATE-UI-SERVER, ask for the new UI contract that settles the table above.
5. Allocate the first implementation task (U03 principal and grants contract), with fresh registry and PR checks.

Answer each row separately in the POST30-ODP-1 format (packet, revision 1, the SHA-256 above, decision ID, disposition and exact option, scope, "Operational / implementation authorization: NONE in this design reply", date). Do not answer "approve all"; unanswered rows stay PROPOSED / UNANSWERED.

## What this packet does not do

No decision is answered or preselected; no task, branch or PR is created; no database, role, grant, schema, API, dependency, framework or deployment change; no source or image acquisition; PR #8, U01/r14, matching and ETL untouched. Every implementation node still needs its accepted contract, rights, Owner task authorization, isolated branch, tests, independent review, Draft PR and Human Merge.
