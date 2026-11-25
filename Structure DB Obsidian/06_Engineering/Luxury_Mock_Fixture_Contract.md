---
id: DPT-ENG-LUXURY-MOCK
project: DoomParfum By TK
type: fixture_contract
status: proposed
owner: human-owner
updated: 2026-11-26
tags: [doomparfum, synthetic, fixtures, boundaries]
source_of_truth: "../../README.md"
---

# Mock fixture contract and isolation boundaries

PROPOSED under [[DPT-PLAN-012_Luxury_Frontend_Editorial]]. This is not a real catalogue DTO, canonical schema, matching input or U01 security contract. Existing [[State_and_Error_Contracts]] and [[Cache_Offline_and_Privacy_Policy]] remain future-application context; no rights or private-data approval follows.

## Fixture ownership and identity

Later implementation may author at most 12 fictional perfume studies, 9 fictional note labels, 3 fictional families and 2 short original editorial articles. Proposed names use unmistakable study naming: “Paper study A”, “Paper study B”, fictional house “DoomParfum mock atelier”; IDs start `mock-`. Do not reuse a real perfume, house identity, bottle shape, packaging, review, price, quote or product claim. A real botanical name alone does not justify assigning it as a fact about a fictional or real fragrance; use invented facet labels for this demonstration.

Every record carries `synthetic: true`, `provenance.kind: locally_authored_fixture`, fixture version, and `rights: project_owned_synthetic`. That rights string describes only original fixture material authored for this task; it cannot be set on third-party content. Do not attach an acquisition date or source URL pretending to be real perfume provenance. Authored file revision and Git SHA establish fixture history. Abstract art is original geometric/material work, visibly a visual study, never a counterfeit commercial packshot.

## Proposed fields (schema specification, not application code)

| Field | Type / rule |
|---|---|
| `id` | Unique string, `mock-perfume-001` pattern, immutable within fixture revision |
| `slug` | Unique lowercase ASCII segments, 1–80 chars, no real product slug |
| `synthetic` | Literal true; reject false/missing |
| `name` | Required authored string, 1–120 Unicode code points; plain text |
| `houseLabel` | Required fictional string, visibly mock; no lookup into real brands |
| `description` | Known string or unknown; at most 600 Unicode code points; explicitly fictional |
| `family` | Known reference to local fictional family ID, or unknown |
| `top`, `heart`, `base` | Independently known lists of local mock note IDs, or unknown. Known empty list is allowed and distinct from unknown. Never infer one layer from another. |
| `generalNotes` | Separate known list or unknown; cannot backfill missing top/heart/base |
| `accords` | Separate known list of fictional descriptor IDs or unknown; no weights/percentages |
| `visual` | Owned local study ID or unavailable; no URL field, download, remote image or data URI |
| `provenance` | Local fixture kind, fixture version, authored-for task ID; no real source permission implication |

Field state uses a discriminated value: `known` with value, `unknown` without value; visual may be `unavailable`. An empty array inside known is authored emptiness. Do not encode unknown as `null`, zero, empty string or empty list and then guess its meaning in the view. Unknown description/family/layer remains readable text. Per-field unknown never makes an otherwise valid fixture disappear. Invalid references or duplicate IDs/slugs fail fixture validation rather than silently remove data.

Mock note record: unique `mock-note-*` ID, invented label, short fictional descriptor, optional known family, synthetic provenance. Mock family record: stable `mock-family-*` ID and label. Relationship membership is explicit in the perfume lists. Example conceptual record: Paper study A has known top `[mock-note-001]`, unknown heart, known empty base, unknown general notes and no visual. It must render those four distinctions accurately; it is not a real perfume fact.

No price, currency, stock, SKU, seller, external listing, personal identifier, purchased/owned status, review, score, confidence percentage, rating, similarity value or matching eligibility field is allowed. No links from fixture values are fetched. Do not import historical Scento payloads, database files or matching tests as convenient sample data.

## Search/filter behavior

Only locally authored fields listed in [[Luxury_Routes_and_Wireframes]] are searchable. Family and note use exact local IDs; AND across groups. Layer membership may be unioned for a note filter but the detail still preserves each layer. General notes can participate only as explicit `generalNotes` membership; do not convert to layered membership. Unknown membership never matches. Name sorting is deterministic with ID tie-break. Counts mean “N mock studies” only; no confidence, quality or ranking inference. No personalization, analytics or hidden recommendation service.

## Runtime and cache boundary

Proposed application root `web/` is isolated from `database/`, `matching_math/`, private files and the vault. Fixtures are server-only local modules. Deliver an ephemeral serialized view model with no-store HTML/RSC responses to the client for local filtering. Client JavaScript bundles must not embed the catalogue fixture payload; inspect the production bundle and framework output to verify this. Framework same-origin document, JS, CSS, RSC/navigation and owned asset requests are permitted; external requests, live APIs and server-side URL fetches are not.

Do not write catalogue payloads or queries to localStorage, sessionStorage, IndexedDB, Cache Storage, service workers, cookies or an application disk cache. No offline mode or write queue. Rendered in-memory state may persist within the same tab/router session and must reset on hard reload. Route-level recognized synthetic IDs may be encoded in URL filters; typed query remains in memory. HTTP no-store is a delivery rule, not a guarantee of forensic browser erasure. Hashed framework code/owned static assets may use normal immutable caching only after verifying they contain no fixture payload or private material.

No form posts, route handlers, API server, auth provider or account session. The Profile button opens a local explanation. No environment files or secrets required. Disabling a feature does not justify shipping a private SDK or credential code behind it. Build/runtime telemetry must be disabled; fonts/icons/assets are local. Record any dependency install networking separately during later approved setup; it is not a runtime-data exception.

## Negative controls required later

Reject a fixture with synthetic false, a real-looking external source field, a price/score/review field, duplicate slug/ID, unknown note reference, unsafe HTML, oversized text, remote visual URL or a missing provenance tag. Test known-empty versus unknown and an unavailable visual independently. Verify no imports traverse into existing database/matching sources. Scan source and built output; network inspection must show no cross-origin request from any route or interactive action. Test search input resembling HTML as literal text. No new production security acceptance is implied by these mock-specific controls.

## Amendment DPT-PLAN-013 — Thai overlay (PROPOSED until merged)

Contract: [[DPT-PLAN-013_Frontend_V1_1_Amendment]], 4.3 and 4.5. Nothing above is removed and English fixture records stay byte-identical.

- A separate server-only overlay, keyed by existing IDs, may hold Thai text for descriptions, descriptors, article text and captions. Each text is `draft` or `reviewed`; only the Owner marks text reviewed. The overlay carries the same synthetic, provenance and rights marks.
- It adds no record, name, note, relationship or state, and gives no text to an unknown field. Length and plain-text limits are those above.
- Negative controls to add: unknown ID, new name, text on an unknown field, over-long text, markup, URL, a `reviewed` mark without an Owner review record, overlay text in a client chunk.
- Search on English pages uses overlay text only when it is reviewed and the query has a Thai character.
- No language preference is stored anywhere.
