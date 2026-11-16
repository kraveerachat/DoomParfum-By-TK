---
id: DPT-ARCH-UX-STATE
project: DoomParfum By TK
type: architecture_state_contract
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, ux, accessibility, privacy, proposed]
source_of_truth: "../../README.md"
---

# State and error contracts — proposed

These thirteen state names are canonical within the proposed DPT-PLAN-010 package. They are presentation contracts for a future application, not implemented exception classes, HTTP status choices or working UI. Exact transport DTOs belong to [[Function_Interface_and_DTO_Contracts]], page contracts to [[Unified_Information_Architecture]], and individual event/handler bindings to [[UI_Element_Function_Matrix]]. All future feature, security, keyboard, screen-reader and browser tests listed here are **NOT RUN**.

The application must first authenticate, bind the genuine nonadmin principal and authorize the operation/object/fields/current rights. Only then may it project a detailed state. Unauthorized and nonexistent private objects must remain indistinguishable, including counts, suggestions, hidden DOM, media, accessible text and logs. An internal held/revoked reason is not automatically a safe browser message. Only a caller authorized to know the object and reason may see that detail; otherwise return the same generic unavailable/denied presentation. Transport code/size/timing equivalence needs explicit later tests and is not proven by this plan.

## State registry

### Idle

- **Meaning:** No request submitted; query or page is awaiting explicit action.
- **Presentation:** Give labels and task guidance; no invented results or default 100%.
- **Recovery:** Edit controls or submit after validation.
- **Accessibility:** Leave focus at current control; status may be silent until an action.
- **Future acceptance:** `UAT-STATE-IDLE` — NOT RUN.

### Loading

- **Meaning:** Authorized bounded operation is pending.
- **Presentation:** Retain safe draft; label progress; skeleton is not data; no old results presented as current.
- **Recovery:** Cancel locally or wait; ignore response after cancellation, query replacement or session change.
- **Accessibility:** Announce short loading status once; preserve focus and avoid repeated live announcements.
- **Future acceptance:** `UAT-STATE-LOADING` — NOT RUN.

### Ready

- **Meaning:** Authorized operation completed with usable data under current rights/snapshot.
- **Presentation:** Render only DTO fields the caller may see; display coverage/source/method where applicable.
- **Recovery:** Inspect, edit, compare or explicitly submit another action.
- **Accessibility:** Announce completion/count summary without moving focus; route navigation focuses main heading.
- **Future acceptance:** `UAT-STATE-READY` — NOT RUN.

### Valid Empty

- **Meaning:** Authorized successful completed operation returned a valid empty set.
- **Presentation:** Explain no matching records and active filters; valid empty is not unknown notes, missing capability or a closed-domain emptiness claim.
- **Recovery:** Clear or narrow filters, or add own first record through authorized flow.
- **Accessibility:** Announce no results, retain search focus, offer labeled recovery button.
- **Future acceptance:** `UAT-STATE-VALID-EMPTY` — NOT RUN.

### Partial / Incomplete

- **Meaning:** Authorized subset is usable but coverage, layering, completeness or search completion is limited.
- **Presentation:** Show known facts and explicit gaps; do not imply absent notes, full search or measured intensity.
- **Recovery:** Inspect allowed metadata; change query/filters or await separately approved review.
- **Accessibility:** Associate each gap label with its section; announce concise partial-result summary.
- **Future acceptance:** `UAT-STATE-PARTIAL` — NOT RUN.

### Unknown

- **Meaning:** Authorized field or condition has no reliable known value.
- **Presentation:** Use Unknown/not recorded; general notes remain All Listed Notes; unknown price and no valid score are never zero.
- **Recovery:** Inspect permitted provenance or record optional own data explicitly.
- **Accessibility:** Expose text alternatives; do not encode uncertainty through color alone.
- **Future acceptance:** `UAT-STATE-UNKNOWN` — NOT RUN.

### Unavailable

- **Meaning:** Operation, method, domain, rights-safe value or media cannot be supplied.
- **Presentation:** Show generic unavailable; give dependency reason only if independently authorized; real matching remains blocked without synthetic fallback.
- **Recovery:** Offer permitted factual view or another supported task; no unsafe auto retry.
- **Accessibility:** Label disabled controls and explain why without private existence leakage.
- **Future acceptance:** `UAT-STATE-UNAVAILABLE` — NOT RUN.

### Unauthorized

- **Meaning:** Session/scope/object/field authorization does not permit operation.
- **Presentation:** Use the same safe presentation for denied and nonexistent private objects; no protected count, hold, source or asset detail.
- **Recovery:** Authenticate if appropriate or return to permitted navigation; retry reauthorizes from start.
- **Accessibility:** Generic accessible message and permitted recovery; no hidden DOM/private announcement details.
- **Future acceptance:** `UAT-STATE-UNAUTHORIZED` — NOT RUN.

### Conflicted / Held

- **Meaning:** Known authorized review object has a conflict or hold preventing a particular use.
- **Presentation:** Show safe blocked capability generally; disclose hold/conflict reason only to a user allowed to know object and review evidence.
- **Recovery:** Use factual permitted fields or submit authorized review proposal; never release hold through a display action.
- **Accessibility:** Text label with authorized reason; offer review link only when role and object permission permit.
- **Future acceptance:** `UAT-STATE-HELD` — NOT RUN.

### Expired / Revoked

- **Meaning:** Session, membership, snapshot or rights are no longer current.
- **Presentation:** For unknown/unauthorized objects use generic denial; only previously known and still authorized context may show safe expiry detail. Stop display/delivery of protected stale content.
- **Recovery:** Reauthenticate or restart with new authorization/snapshot; no silent replay or stale membership reuse.
- **Accessibility:** Announce safe session/content change once; focus recovery heading when current context is removed.
- **Future acceptance:** `UAT-STATE-EXPIRED` — NOT RUN.

### Timeout

- **Meaning:** Operation exceeded budget or completion cannot be established.
- **Presentation:** State incomplete search/action status; do not claim valid empty, completed mutation or exhaustive ranking.
- **Recovery:** Narrow query; explicit safe retry. For uncertain writes re-read authorized state/idempotency outcome before replay.
- **Accessibility:** Announce timeout; preserve safe inputs and focus recovery summary when user action is needed.
- **Future acceptance:** `UAT-STATE-TIMEOUT` — NOT RUN.

### Validation Error

- **Meaning:** Explicit input contract rejects unknown, malformed, contradictory, unbounded or stale-version data.
- **Presentation:** Show field-specific actionable errors without raw request payloads, SQL, stack traces or private existence.
- **Recovery:** Correct inputs, refresh stale version, or cancel; no hidden coercion/default permission.
- **Accessibility:** Focus linked error summary on failed submit; mark/describe invalid fields and retain safe user input.
- **Future acceptance:** `UAT-STATE-VALIDATION` — NOT RUN.

### Offline

- **Meaning:** Network/service connectivity is unavailable; browser connectivity hint alone does not prove server state.
- **Presentation:** Show unavailable private operation, never cached protected result as current; no persistent private offline data or queued writes.
- **Recovery:** Reconnect then explicitly retry with fresh session/rights; static shell may remain only if separately safe.
- **Accessibility:** Announce connectivity once; keep retry keyboard accessible; do not trap focus or claim a write succeeded.
- **Future acceptance:** `UAT-STATE-OFFLINE` — NOT RUN.

## Truth-preserving display rules

1. `None`/no valid fit is Unavailable, never `0%`. A mathematically valid score of exact zero may display `0%` after the accepted method evaluates compatible authorized complete-enough inputs. A displayed rounded percentage does not determine ranking; preserve exact rationals until ordering. Show method/version and coverage.
2. Valid Empty is a successful authorized query with no returned rows under its declared bounds/filters. It says nothing about note absence. A complete empty note domain needs an independently reviewed closure assertion tied to source/capture/edition/domain/version. Missing, incomplete, rights-withheld or unselected notes do not prove absence or satisfy exclusion.
3. General-only notes render as All Listed Notes; do not distribute them into top/heart/base or infer temporal scent strength. Exact canonical match, cross-layer occurrence and listed-only difference need separate text. No scent formula, molecule content, longevity or scientifically measured smell claim follows from a note illustration or score.
4. Structural/Query Fit, Data Confidence and Direct Pairwise Evidence are independent fields with independent unavailable states. Review popularity/overall rating is not pair evidence or structural fit. Do not fabricate a second percentage, confidence badge or absence of contradiction when evidence is missing.
5. A real candidate never becomes a synthetic fixture to obtain a result. Exact synthetic M1/B1 remain source-bound test capabilities. Accepted B1 required-all semantics stay unchanged; historical all/any/minimum UX controls are blocked future alternatives until a separate exact method contract is accepted. No generic future real contract may disguise real inputs as synthetic. Real A/B1 and B2 stay unavailable until their own identity/rights/selection/domain/completeness/normalization/method/eligibility approvals and implementation tests pass. Partial factual comparison may remain available if authorized; unsupported scoring does not erase lawful known facts.
6. Prices and user-recorded remaining amounts are optional observations with unit, date and source; unknown is not zero. Aggregate known-price coverage and currency separately. Currently Owned and Ever Purchased stay distinct even after a bottle is Finished/Sold/Gifted. Manual Ordered stamp uses IF-PURCHASE-STATUS-WRITE-1; separately explicit purchase-history record/edit and optional paid price/date/volume/seller use IF-PURCHASE-RECORD-WRITE-1. Bounded caller-own history reads use IF-PURCHASE-RECORD-READ-1, including history without inventory links; no collection foreign key or paid fact is inferred. Physical bottle notes/remaining units/lifecycle use IF-COLLECTION-WRITE-1. No stamp or click automatically creates an order, purchase or bottle, and none initiates payment/commerce. All application operations remain PROPOSED; R31 remains deferred.

## Event and transition rules

| Event | Permitted transition | Side effects and safe presentation | Future test |
|---|---|---|---|
| Enter a protected route | Idle, then Loading only after safe session gate | No protected preload/count/prefetch for anonymous callers. Fresh object/field authorization precedes data. | UAT-EVENT-ENTER, NOT RUN |
| Type, change tab, add/remove clause or move preference slider | Idle or safe local draft; existing results become explicitly stale | No background third-party query. Inactive B1/B2 draft cannot change active scoring; values remain local. | UAT-EVENT-DRAFT, NOT RUN |
| Explicit Search/Submit | Validation Error or Loading | Validate shape, exact edition, IDs, contradictions, bounds and capability. Query body/private IDs do not enter URL, telemetry or share link. | UAT-EVENT-SUBMIT, NOT RUN |
| Successful current read/query | Ready, Valid Empty or Partial / Incomplete | Accept only current request/session/query/snapshot. Do not announce raw protected counts. Failed capability is Unavailable rather than Valid Empty. | UAT-EVENT-RESULT, NOT RUN |
| Clear / Reset / Remove | Idle local draft | Clear active query; Reset active visible initial seed/defaults; Remove one clause. Re-authorize any subsequent submitted seed. Never silently alter inactive clauses. | UAT-EVENT-CLEAR, NOT RUN |
| Cancel or superseding submit | Idle/safe prior view; discard stale responses | Local cancellation does not prove server execution stopped or a mutation rolled back. No stale response may replace current results. | UAT-EVENT-CANCEL, NOT RUN |
| Network error or bounded budget expiry | Offline, Timeout or safe Unavailable | No claim of complete search/empty result. Preserve only safe local inputs; retry explicitly with new checks. | UAT-EVENT-NETWORK, NOT RUN |
| Validated private write confirmed | Ready with updated authorized projection | Owner binding, expected version and idempotency belong to logical interface; no optimistic success before confirmation. | UAT-EVENT-WRITE, NOT RUN |
| Write response lost | Timeout with outcome unknown | Do not blindly repeat Ordered/Received/purchase/decision writes. Resolve operation outcome or use approved idempotency policy, then re-read authorized state. | UAT-EVENT-WRITE-UNKNOWN, NOT RUN |
| Version conflict or hold | Validation Error or authorized Conflicted / Held | Reject stale mutation; refresh permitted version and ask for explicit resubmission. No automatic last-writer-wins or hold release. | UAT-EVENT-CONFLICT, NOT RUN |
| Rights/session/membership changes, logout | Safe Expired / Revoked or generic Unauthorized | Cancel/ignore requests and remove protected display; best-effort clear drafts/results and authorize anew. Never claim erasure of screenshots/downloaded/already viewed bytes. | UAT-EVENT-REVOKE, NOT RUN |
| Open buying source | Explicit browser-only navigation | Validate permitted scheme without server resolution/preview/prefetch. Apply safe referrer/opener policy. Click makes no application purchase, state transition, seller call or transaction. | UAT-EVENT-BUYING-LINK, NOT RUN |

## Component-family state mapping

Every page inherits safe session and request states; each visible subsection may carry its own truthful data state without converting a whole page into a scoring success. The following covers the child component families in [[Unified_Information_Architecture]]. Individual controls and their exact events are enumerated in [[UI_Element_Function_Matrix]].

| Presentation family / pages | Relevant data states | Presentation and recovery |
|---|---|---|
| Shell/navigation/search, all routes | Idle, Loading, Unauthorized, Expired / Revoked, Offline | Route links have accessible names and current-page state. Hide unauthorized System entries; direct requests still enforce authorization. Sign-in entry contains no private suggestions/counts/prefetch. |
| Catalogue cards, filters, pagination, R-CATALOGUE | Loading, Ready, Valid Empty, Partial / Incomplete, Unknown, Unavailable, Timeout, Validation Error | Announce authorized result summary; explain active filters; preserve current query. Missing filter inputs are labeled unavailable, not auto-filled. Retry/narrow after timeout. |
| Detail tabs, pyramid/layers/chips, R-DETAIL/R-PYRAMID | Ready, Partial / Incomplete, Unknown, Unavailable, authorized Conflicted / Held | Show known section fields; All Listed Notes stays separate. Disclose only authorized reason. Chip label and text distinguish exact match/listed-only/unknown without color dependence. |
| Reference and vocabulary comboboxes, R-MATCH/R-COMPARE | Idle, Loading, Ready, Valid Empty, Unavailable, Unauthorized, Validation Error, Timeout | Suggestions authorize before lookup/count. Display exact edition and IDs only within permitted context; ambiguous text needs explicit choice. No arbitrary text-to-canonical-ID coercion. |
| Mode/tabs, B1 rules/layers, B2 sliders, R-MATCH | Idle, Validation Error, Unavailable, Partial / Incomplete | Active tab explicit; numeric keyboard alternatives; explain unavailable methods without fabricating values. Known preference values never become observed candidate intensities. |
| Results, fit/coverage/explanation, R-RESULTS | Loading, Ready, Valid Empty, Partial / Incomplete, Unknown, Unavailable, Timeout, Expired / Revoked | Separate compatible partitions and evidence channels; no valid fit is not zero. Stale snapshots require restart. Keep accessible focus while announcing concise completion. |
| Two-profile table, R-COMPARE | Ready, Partial / Incomplete, Unknown, Unavailable, Unauthorized | Factual views and scoring capabilities differ. One inaccessible profile cannot expose its name/source or be inferred through a count. Swap/change preserves separate identities. |
| Bottle/note media across all relevant routes | Loading, Ready, Unknown, Unavailable, Unauthorized, Expired / Revoked | Neutral placeholder for missing/denied/revoked bytes; no third-party fallback hotlink. Attribution and alt text disclose only authorized facts. An image is not proof of chemical formula. |
| Buying source/status/private forms, R-CART | Idle, Loading, Ready, Valid Empty, Unknown, Validation Error, Timeout, Offline | Labeled optional price/source/date inputs and duplicate guidance; browser-only external link. Write outcome unknown gets explicit reconciliation, never blind replay or queued offline transaction. |
| Bottles/history, R-CART/R-COLLECTION/R-COLLECTION-ITEM | Loading, Ready, Valid Empty, Partial / Incomplete, Unknown, Unavailable, Validation Error, Timeout, Unauthorized | Purchase history reads through IF-PURCHASE-RECORD-READ-1, separate from inventory: bind pages/counts/cursors to caller, retain unlinked history and unknown paid facts. Bottle-context history stays Unavailable until a separately accepted linkage policy exists; missing linkage is not empty history. Empty own inventory does not imply empty history. |
| Metrics/charts, R-DASHBOARD | Loading, Ready, Valid Empty, Partial / Incomplete, Unknown, Unavailable | Accessible table/text equivalents and coverage; missing price != zero spending; no data from another user enters aggregates/drill-down. |
| Review/status forms, R-SYSTEM/R-SOURCES/R-REVIEWS/R-RIGHTS-MEDIA/R-OPERATIONS | Loading, Ready, Valid Empty, authorized Conflicted / Held, Unavailable, Validation Error, Timeout | Dedicated reviewer permission, authorized reason/version, no CLI/admin bridge. Intake requests are review data, never acquisition approval or execution. |
| Session/settings forms, R-SIGNIN/R-SETTINGS | Idle, Loading, Ready, Validation Error, Unauthorized, Expired / Revoked, Timeout, Offline | Generic authentication errors and safe same-origin reauthorized return target. Own preferences do not permit identity/role grants. Logout clears memory best effort. |

## Accessibility acceptance contract

The proposed target is WCAG 2.2 AA review, not a conformance claim. Normative criteria and informative implementation guidance are distinguished in [[Architecture_Technical_Research_UX]]. WCAG defines testable requirements; browser, keyboard, assistive-technology and responsive checks are needed after approved implementation. [WCAG 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/)

| Contract | Proposed behavior | Future acceptance ID |
|---|---|---|
| Names and native semantics | Use native links for navigation, buttons for actions, labels/fieldset/legend for inputs, genuine tables for comparison/chart alternatives and headings/landmarks. Every icon-only remove/compare control names its object. ARIA does not supply keyboard behavior. | UAT-A11Y-NAMES |
| Keyboard/focus | All controls operable by keyboard with visible focus in logical order, no positive tabindex shortcut and no obscuring sticky region. Route change focuses main heading; local result updates retain focus. | UAT-A11Y-FOCUS |
| Tabs | Active tab/panel relationships and selected state explicit. Arrow keys move tab focus; Enter/Space activates where manual. Choose manual activation for remote/latent panels so focus movement never requires private prefetch. | UAT-A11Y-TABS |
| Combobox | Exact reference/canonical vocabulary has labeled input and popup state. Arrow navigation, Enter selection and Escape dismissal preserve normal text editing; no unexpected submit or focus loss. Native select is preferred when search is unnecessary. | UAT-A11Y-COMBOBOX |
| Sliders/rules | Labeled range/current numeric values with typed input alternative; keyboard adjustment and removable chips. Required/Optional/Excluded and Top/Heart-Middle/Base/Any Layer are text labels, never color-only. | UAT-A11Y-RULES |
| Progress/results | Loading and result-count/completion messages use programmatic status semantics without moving focus. Do not repeatedly announce whole result lists or every skeleton update. | UAT-A11Y-STATUS |
| Errors/recovery | Failed explicit submit focuses a concise error summary with links to invalid controls; provide field text and programmatic association. Recoverable background failures announce briefly and retain control focus. Retry names scope and rechecks authorization. | UAT-A11Y-ERROR |
| Placeholders/media | Describe a missing image semantically without inventing asset or source facts. Approved illustrative note artwork is identified as illustration; decorative art may use empty alt when adjacent text carries meaning. Rights denial cannot leak identity in alt text. | UAT-A11Y-MEDIA |
| Color/layout/motion | Match/mismatch/unknown use text as well as color; test contrast, zoom/reflow and mobile stacking. No dragging required for comparison or sliders; respect reduced motion. | UAT-A11Y-PRESENTATION |

All UAT-A11Y-* scenarios are **NOT RUN**. The APG [native semantic guidance](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/), [tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) and [combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) patterns inform widget behavior. [Status guidance](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), [focus visibility](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html), [focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) and [error identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html) support the proposed acceptance choices; a linked error summary is a project design choice, not the sole W3C-prescribed layout.

## Session, cache and error disclosure limits

Matching drafts/results are ephemeral authenticated in-memory state. No shared cache, service worker, localStorage/IndexedDB persistence, result-history backend or offline write queue is introduced. Reauthorization is required on a new request/page/retry and before media delivery. Logout, expiry and revocation best-effort remove sensitive in-memory presentation and stale response callbacks. This is not a guarantee that a browser, operating system, screenshot or previously received byte can be erased, nor a claim of instantaneous cancellation of an executing database statement.

Static shell assets may be considered separately from protected data; their cacheability does not make catalogue overlays, buying sources, collection, results, rights decisions or private media safe to cache. Restoring a backup must not revive revoked rights. Exact request deadlines, cancellation semantics, cache headers/browser history behavior and transport envelopes remain approval/test dependencies in the architecture security contracts.

Public errors omit raw SQL, filesystem locations, stack traces, cookies/tokens, source URLs and private query bodies. Safe diagnostic correlation IDs must not encode identity or evidence. Security audit retention and internal reason detail require a separate bounded policy; this UI plan does not invent one.

## Preserved gates

POST27-ODP-1 remains unchanged at SHA-256 `0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c`. A/B/I are unapproved, IMP-ENR-01 has not started, synthetic M1/B1 stay synthetic-only, 44 holds/43 normalization proposals/Khamrah conflict remain unchanged and PR8 stays blocked. [[Architecture_Owner_Review_Packet]] records proposed amendments; no state presentation changes database selection, rights or eligibility.
