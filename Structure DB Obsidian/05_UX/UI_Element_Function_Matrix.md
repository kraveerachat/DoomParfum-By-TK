---
id: DPT-PLAN-010-ELEMENT-MATRIX
project: DoomParfum By TK
type: ui_element_function_matrix
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, contracts, planning]
source_of_truth: "../../README.md"
---

# UI element–function matrix

This complete interaction inventory belongs to the proposed [[Unified_Information_Architecture]], not an implemented frontend or API. Every handler below is a proposed logical UI handler. IF identifiers reference [[Function_Interface_and_DTO_Contracts]] and its exact `.input.v1` / `.output.v1` schemas; no URL endpoint is invented. `UI-LOCAL-STATE-1` means an explicitly local presentation transition with no application call, data lookup, write or permission grant.

The authoritative structured rows are in `08_Operations/Test_Evidence/Architecture_Unified_Model.json`. Each expanded row supplies all 19 required matrix fields plus route, schema, gate and propagation bindings. Shared controls have explicit route lists. Static/dumb containers such as headings are not hidden interactive operations; meaningful disclosures, navigation, forms, selectors, submits, retry/cancel/reset and private/admin actions are inventoried below.

All feature/security/accessibility assertions here are **SPECIFIED / NOT RUN**. Every application operation is currently unimplemented; synthetic M1/B1 code does not make a real matching button usable. Required-all synthetic B1 semantics are not weakened by older all/any/minimum UI proposals; those alternative controls remain blocked pending a distinct exact contract. All real matching, B2, acquisition, intake, authentication and private writes retain separate gates.

### Async and privacy rule

Authenticate/lease/authorize before any restricted lookup, count, pagination, scoring or byte loading. A response may update a page only if the current session/view/query generation still matches; reset, logout, revocation and cancellation invalidate old generations. This is presentation race protection, not authorization. Private unknown/missing/denied/hidden revoked objects are not distinguished to a caller lacking the specific metadata right. When no valid fit exists the state is Unavailable, not 0%; a genuine computed zero may be displayed only after every method gate passes. In-memory cleanup is best-effort, not erasure of already delivered bytes.

## Index

| Element | Page/component | Event | Proposed operation | Status |
|---|---|---|---|---|
| EL-NAV-01 | Global navigation / R-CATALOGUE | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-02 | Global navigation / R-DETAIL | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-03 | Global navigation / R-PYRAMID | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-04 | Global navigation / R-MATCH | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-05 | Global navigation / R-RESULTS | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-06 | Global navigation / R-COMPARE | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-07 | Global navigation / R-CART | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-08 | Global navigation / R-COLLECTION | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-09 | Global navigation / R-COLLECTION-ITEM | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-10 | Global navigation / R-DASHBOARD | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-11 | Global navigation / R-SYSTEM | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-12 | Global navigation / R-SOURCES | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-13 | Global navigation / R-REVIEWS | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-14 | Global navigation / R-RIGHTS-MEDIA | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-15 | Global navigation / R-OPERATIONS | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-16 | Global navigation / R-SETTINGS | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-NAV-17 | Global navigation / R-SIGNIN | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-D01 | GlobalSearch | input/submit | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D02 | OriginFilter | change | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D03 | BrandPositionFilter | change | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D04 | UsageFilters | change | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D05 | ObservedPriceFilter | submit | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D06 | CatalogueSort | change | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D07 | CataloguePagination | activate | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D08 | PerfumeCard | activate | IF-PROFILE-READ-1 | PROPOSED |
| EL-D09 | DetailTabs | select tab | IF-PROFILE-READ-1 | PROPOSED |
| EL-D10 | IdentityEvidence | expand | IF-PROFILE-READ-1 | PROPOSED |
| EL-D11 | FindSimilar | activate | IF-CAPABILITY-READ-1 | PROPOSED |
| EL-D12 | SeedB1Query | activate | IF-CAPABILITY-READ-1 | PROPOSED |
| EL-D13 | SaveToCart | activate | IF-PERSONAL-STATE-WRITE-1 | PROPOSED |
| EL-D14 | PyramidLayers | expand/select | IF-PROFILE-READ-1 | PROPOSED |
| EL-D15 | CanonicalNoteChip | activate | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D16 | CompletenessBadge | expand | UI-LOCAL-STATE-1 | PROPOSED |
| EL-D17 | MediaAttribution | expand | IF-MEDIA-RESOLVE-1 | PROPOSED |
| EL-D18 | EvidenceExplanation | expand | IF-PROFILE-READ-1 | PROPOSED |
| EL-M01 | ModeSelector | change | IF-CAPABILITY-READ-1 | PROPOSED |
| EL-M02 | ReferenceSelector | select | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-M03 | RequiredNotes | select/change | IF-VOCABULARY-READ-1 | PROPOSED |
| EL-M04 | OptionalNotes | select/change | IF-VOCABULARY-READ-1 | PROPOSED |
| EL-M05 | ExcludedNotes | select/change | IF-VOCABULARY-READ-1 | PROPOSED |
| EL-M06 | LayerSelector | change | IF-MATCH-VALIDATE-1 | PROPOSED |
| EL-M07 | AlternativeRuleControls | inspect capability | IF-MATCH-VALIDATE-1 | PROPOSED |
| EL-M08 | AccordPreferenceControls | change/inspect capability | IF-CAPABILITY-READ-1 | PROPOSED |
| EL-M09 | AddClause | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-M10 | RemoveClause | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-M11 | SearchSubmit | submit | IF-MATCH-EXECUTE-1 | PROPOSED |
| EL-M12 | ResetQuery | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-M13 | CancelSearch | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-M14 | ResultCard | activate | IF-PROFILE-READ-1 | PROPOSED |
| EL-M15 | FitExplanation | expand | UI-LOCAL-STATE-1 | PROPOSED |
| EL-M16 | ConfidenceAndEvidence | expand | UI-LOCAL-STATE-1 | PROPOSED |
| EL-M17 | ResultCompare | activate | IF-COMPARISON-READ-1 | PROPOSED |
| EL-M18 | ResultSave | activate | IF-PERSONAL-STATE-WRITE-1 | PROPOSED |
| EL-M19 | NarrowOrRetry | activate | IF-MATCH-EXECUTE-1 | PROPOSED |
| EL-C01 | TwoProfileSelectors | select | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-C02 | SwapColumns | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-C03 | CompareFields | select/expand | IF-COMPARISON-READ-1 | PROPOSED |
| EL-C04 | CompareSave | activate | IF-PERSONAL-STATE-WRITE-1 | PROPOSED |
| EL-P01 | PersonalListViews | change | IF-PERSONAL-STATE-READ-1 | PROPOSED |
| EL-P02 | InterestStateEditor | submit | IF-PERSONAL-STATE-WRITE-1 | PROPOSED |
| EL-P03 | SavedSourceAdd | submit | IF-BUYING-SOURCE-WRITE-1 | PROPOSED |
| EL-P04 | SavedSourceEdit | submit | IF-BUYING-SOURCE-WRITE-1 | PROPOSED |
| EL-P05 | SavedSourceRemove | confirm | IF-BUYING-SOURCE-WRITE-1 | PROPOSED |
| EL-P06 | BuyingLink | explicit activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-P07 | ManualOrdered | submit | IF-PURCHASE-STATUS-WRITE-1 | PROPOSED |
| EL-P08 | ManualReceived | submit | IF-COLLECTION-WRITE-1 | PROPOSED |
| EL-P09 | DuplicateWarning | confirm choice | IF-PERSONAL-STATE-WRITE-1 | PROPOSED |
| EL-P10 | MissingPerfumeProposal | submit | IF-SOURCE-INTAKE-REQUEST-1 | PROPOSED |
| EL-P11 | ScreenshotOrURLIntakeRequest | submit | IF-ASSET-INTAKE-REQUEST-1 | PROPOSED |
| EL-P12 | InventoryLifecycleTabs | change | IF-COLLECTION-READ-1 | PROPOSED |
| EL-P13 | BottleCard | activate | IF-COLLECTION-READ-1 | PROPOSED |
| EL-P14 | OptionalPurchaseFields | submit | IF-PURCHASE-RECORD-WRITE-1 | PROPOSED |
| EL-P15 | PersonalNotes | submit | IF-COLLECTION-WRITE-1 | PROPOSED |
| EL-P16 | RemainingAmount | submit | IF-COLLECTION-WRITE-1 | PROPOSED |
| EL-P17 | FinishBottle | confirm | IF-COLLECTION-WRITE-1 | PROPOSED |
| EL-P18 | SellBottle | confirm | IF-COLLECTION-WRITE-1 | PROPOSED |
| EL-P19 | GiftBottle | confirm | IF-COLLECTION-WRITE-1 | PROPOSED |
| EL-P20 | Rebuy | activate | IF-PERSONAL-STATE-WRITE-1 | PROPOSED |
| EL-P21 | DashboardFilters | change | IF-DASHBOARD-READ-1 | PROPOSED |
| EL-P22 | DashboardMetricDisclosure | expand | IF-DASHBOARD-READ-1 | PROPOSED |
| EL-P23 | DashboardChartDrilldown | activate | IF-COLLECTION-READ-1 | PROPOSED |
| EL-P24 | DeferredSpendingAnalytics | inspect | UI-LOCAL-STATE-1 | PROPOSED |
| EL-S01 | ReviewQueueNavigation | activate | IF-REVIEW-QUEUE-READ-1 | PROPOSED |
| EL-S02 | SourceMetadataDisclosure | expand | IF-REVIEW-QUEUE-READ-1 | PROPOSED |
| EL-S03 | SourceIntakeRequest | submit | IF-SOURCE-INTAKE-REQUEST-1 | PROPOSED |
| EL-S04 | ReviewQueueFilters | change | IF-REVIEW-QUEUE-READ-1 | PROPOSED |
| EL-S05 | ProposalDiff | expand | IF-REVIEW-QUEUE-READ-1 | PROPOSED |
| EL-S06 | ApproveReviewDecision | submit | IF-REVIEW-DECISION-WRITE-1 | PROPOSED |
| EL-S07 | RejectReviewDecision | submit | IF-REVIEW-DECISION-WRITE-1 | PROPOSED |
| EL-S08 | HoldReviewDecision | submit | IF-REVIEW-DECISION-WRITE-1 | PROPOSED |
| EL-S09 | AssetUseScopeEditor | submit | IF-RIGHTS-REVIEW-1 | PROPOSED |
| EL-S10 | AttributionReview | submit | IF-RIGHTS-REVIEW-1 | PROPOSED |
| EL-S11 | AssetIntakeRequest | submit | IF-ASSET-INTAKE-REQUEST-1 | PROPOSED |
| EL-S12 | WithdrawAssetUse | submit | IF-RIGHTS-REVIEW-1 | PROPOSED |
| EL-S13 | OperatorStatusRefresh | activate | IF-OPERATOR-STATUS-READ-1 | PROPOSED |
| EL-S14 | RunbookLinks | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-S15 | OwnPreferences | submit | IF-PRIVATE-SETTINGS-1 | PROPOSED |
| EL-S16 | CachePrivacyDisclosure | expand | UI-LOCAL-STATE-1 | PROPOSED |
| EL-S17 | SignOut | activate | IF-SESSION-END-1 | PROPOSED |
| EL-S18 | AuthenticationForm | submit | IF-AUTH-SESSION-1 | PROPOSED |
| EL-M20 | ClearCurrentInput | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-P25 | RecordPurchase | submit | IF-PURCHASE-RECORD-WRITE-1 | PROPOSED |
| EL-P27 | PurchaseHistoryPanel | load/filter/page | IF-PURCHASE-RECORD-READ-1 | PROPOSED |
| EL-D20 | CurrentnessFilter | change | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-D21 | CanonicalBrandFilter | change | IF-CATALOGUE-QUERY-1 | PROPOSED |
| EL-P26 | CartRemoveOrMove | confirm | IF-PERSONAL-STATE-WRITE-1 | PROPOSED |
| EL-UI-01 | DialogDismiss | activate | UI-LOCAL-STATE-1 | PROPOSED |
| EL-D19 | FutureResearchAssistance | inspect | UI-LOCAL-STATE-1 | PROPOSED |
| EL-MEDIA-01 | OriginalMediaView | authorized load | IF-MEDIA-DELIVER-1 | PROPOSED |
| EL-MEDIA-02 | MediaRetry | activate | IF-MEDIA-RESOLVE-1 | PROPOSED |

## Expanded contracts

### EL-NAV-01 — Global navigation / R-CATALOGUE

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-01 |
| Page/Component | Global navigation / R-CATALOGUE |
| Element Type | link |
| User Intent | Navigate to the proposed /catalogue page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-01 / proposed.ui.handle_el_nav_01 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-01: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-02 — Global navigation / R-DETAIL

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-02 |
| Page/Component | Global navigation / R-DETAIL |
| Element Type | link |
| User Intent | Navigate to the proposed /perfumes/:id page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-02 / proposed.ui.handle_el_nav_02 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-02: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-02-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-02-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-03 — Global navigation / R-PYRAMID

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-03 |
| Page/Component | Global navigation / R-PYRAMID |
| Element Type | link |
| User Intent | Navigate to the proposed /perfumes/:id/notes page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-03 / proposed.ui.handle_el_nav_03 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-03: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-03-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-03-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-04 — Global navigation / R-MATCH

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-04 |
| Page/Component | Global navigation / R-MATCH |
| Element Type | link |
| User Intent | Navigate to the proposed /matching page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-04 / proposed.ui.handle_el_nav_04 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-04: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-04-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-04-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-05 — Global navigation / R-RESULTS

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-05 |
| Page/Component | Global navigation / R-RESULTS |
| Element Type | link |
| User Intent | Navigate to the proposed /matching/results page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-05 / proposed.ui.handle_el_nav_05 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-05: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-05-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-05-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-06 — Global navigation / R-COMPARE

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-06 |
| Page/Component | Global navigation / R-COMPARE |
| Element Type | link |
| User Intent | Navigate to the proposed /compare page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-06 / proposed.ui.handle_el_nav_06 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-06: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-06-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-06-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-07 — Global navigation / R-CART

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-07 |
| Page/Component | Global navigation / R-CART |
| Element Type | link |
| User Intent | Navigate to the proposed /my-cart page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-07 / proposed.ui.handle_el_nav_07 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-07: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-07-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-07-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-08 — Global navigation / R-COLLECTION

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-08 |
| Page/Component | Global navigation / R-COLLECTION |
| Element Type | link |
| User Intent | Navigate to the proposed /collection page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-08 / proposed.ui.handle_el_nav_08 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-08: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-08-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-08-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-09 — Global navigation / R-COLLECTION-ITEM

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-09 |
| Page/Component | Global navigation / R-COLLECTION-ITEM |
| Element Type | link |
| User Intent | Navigate to the proposed /collection/:id page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-09 / proposed.ui.handle_el_nav_09 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-09: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-09-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-09-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-10 — Global navigation / R-DASHBOARD

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-10 |
| Page/Component | Global navigation / R-DASHBOARD |
| Element Type | link |
| User Intent | Navigate to the proposed /dashboard page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-10 / proposed.ui.handle_el_nav_10 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-10: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-10-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-10-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-11 — Global navigation / R-SYSTEM

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-11 |
| Page/Component | Global navigation / R-SYSTEM |
| Element Type | link |
| User Intent | Navigate to the proposed /system page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-11 / proposed.ui.handle_el_nav_11 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-11: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-11-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-11-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-12 — Global navigation / R-SOURCES

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-12 |
| Page/Component | Global navigation / R-SOURCES |
| Element Type | link |
| User Intent | Navigate to the proposed /system/sources page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-12 / proposed.ui.handle_el_nav_12 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-12: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-12-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-12-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-13 — Global navigation / R-REVIEWS

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-13 |
| Page/Component | Global navigation / R-REVIEWS |
| Element Type | link |
| User Intent | Navigate to the proposed /system/reviews page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-13 / proposed.ui.handle_el_nav_13 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-13: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-13-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-13-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-14 — Global navigation / R-RIGHTS-MEDIA

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-14 |
| Page/Component | Global navigation / R-RIGHTS-MEDIA |
| Element Type | link |
| User Intent | Navigate to the proposed /system/rights-media page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-14 / proposed.ui.handle_el_nav_14 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-14: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-14-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-14-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-15 — Global navigation / R-OPERATIONS

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-15 |
| Page/Component | Global navigation / R-OPERATIONS |
| Element Type | link |
| User Intent | Navigate to the proposed /system/operations page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-15 / proposed.ui.handle_el_nav_15 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-15: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-15-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-15-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-16 — Global navigation / R-SETTINGS

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-16 |
| Page/Component | Global navigation / R-SETTINGS |
| Element Type | link |
| User Intent | Navigate to the proposed /settings page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-16 / proposed.ui.handle_el_nav_16 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-16: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-16-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-16-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-NAV-17 — Global navigation / R-SIGNIN

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R01, R11, R27.

| Field | Contract |
|---|---|
| Element ID | EL-NAV-17 |
| Page/Component | Global navigation / R-SIGNIN |
| Element Type | link |
| User Intent | Navigate to the proposed /sign-in page |
| Triggered Event | activate |
| Proposed Handler | H-EL-NAV-17 / proposed.ui.handle_el_nav_17 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted route and non-sensitive return target; existing authenticated-view generation if present |
| Validation | Route visibility follows the accepted role policy; no private counts/prefetch. Reject arbitrary return URLs and route parameters as proof of access. Hiding admin navigation is not server authorization. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Loading target shell; authorized route then invokes its own interfaces. |
| Empty State | Static navigation does not claim an empty data set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-NAV-17: Direct URL bypass still fails server gates; hidden admin nav is not the authorization check.; UAT-EL-NAV-17-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-NAV-17-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-D01 — GlobalSearch

Routes: R-CATALOGUE. Requirement trace: R01, R06.

| Field | Contract |
|---|---|
| Element ID | EL-D01 |
| Page/Component | GlobalSearch |
| Element Type | search input |
| User Intent | Search visible perfume names/brands |
| Triggered Event | input/submit |
| Proposed Handler | H-EL-D01 / proposed.ui.handle_el_d01 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Explicit bounded text, query version, cursor reset and accepted resource policy. |
| Validation | Reject unbounded/coerced text; no request until policy and session exist; suggestions and counts are scoped. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready bounded authorized page. |
| Empty State | Valid Empty only for a successful scoped query, never inferred missing source facts. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D01: Injection, hidden private hits/counts, late-response races and unknown query policy fail.; UAT-EL-D01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D02 — OriginFilter

Routes: R-CATALOGUE. Requirement trace: R02, R06, R22.

| Field | Contract |
|---|---|
| Element ID | EL-D02 |
| Page/Component | OriginFilter |
| Element Type | select |
| User Intent | Filter reviewed brand origin independently of position/market |
| Triggered Event | change |
| Proposed Handler | H-EL-D02 / proposed.ui.handle_el_d02 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Canonical reviewed country/region IDs and vocabulary version. |
| Validation | Country claim is not market availability; no raw-country-to-ISO coercion. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready/Partial labelled scoped filter result. |
| Empty State | No authorized result is not no brand in the world. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D02: Country and positioning dimensions remain independent.; UAT-EL-D02-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D02-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D03 — BrandPositionFilter

Routes: R-CATALOGUE. Requirement trace: R02, R06.

| Field | Contract |
|---|---|
| Element ID | EL-D03 |
| Page/Component | BrandPositionFilter |
| Element Type | select |
| User Intent | Choose designer/niche/value positioning separately |
| Triggered Event | change |
| Proposed Handler | H-EL-D03 / proposed.ui.handle_el_d03 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Reviewed positioning/tag IDs; no default from country. |
| Validation | Unverified positioning stays unknown; reject unsupported IDs. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready scoped result. |
| Empty State | Valid Empty after authorized query only. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D03: Origin must not imply niche/designer or value category.; UAT-EL-D03-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D03-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D04 — UsageFilters

Routes: R-CATALOGUE. Requirement trace: R04.

| Field | Contract |
|---|---|
| Element ID | EL-D04 |
| Page/Component | UsageFilters |
| Element Type | checkbox group |
| User Intent | Filter day/night/season/audience claims |
| Triggered Event | change |
| Proposed Handler | H-EL-D04 / proposed.ui.handle_el_d04 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Explicit reviewed usage/audience IDs and unknown-handling policy. |
| Validation | Missing usage is not false or a gender inference; source-specific selected claims required. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready/Partial with unknown labels. |
| Empty State | Authorized empty page only. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D04: Unknown usage is not silently mapped to an option.; UAT-EL-D04-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D04-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D05 — ObservedPriceFilter

Routes: R-CATALOGUE. Requirement trace: R08, R29.

| Field | Contract |
|---|---|
| Element ID | EL-D05 |
| Page/Component | ObservedPriceFilter |
| Element Type | range form |
| User Intent | Apply an explicit observed-price budget |
| Triggered Event | submit |
| Proposed Handler | H-EL-D05 / proposed.ui.handle_el_d05 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Currency, exact amount/size/date/source policy and explicit range; R08 THB2000 intent is not an implemented default. |
| Validation | Finite exact amounts; no FX/size/date inference, live quote or null-to-zero; authorize listing data before filtering/counts. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready with observed-price coverage and date. |
| Empty State | No qualifying visible observations is not cheapest/zero price. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D05: Unpriced records, foreign currency and stale observations cannot pass by coercion.; UAT-EL-D05-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D05-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D06 — CatalogueSort

Routes: R-CATALOGUE. Requirement trace: R01, R16.

| Field | Contract |
|---|---|
| Element ID | EL-D06 |
| Page/Component | CatalogueSort |
| Element Type | select |
| User Intent | Choose a reviewed stable catalogue ordering |
| Triggered Event | change |
| Proposed Handler | H-EL-D06 / proposed.ui.handle_el_d06 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Explicit allowlisted order/version and authorized cursor. |
| Validation | No real-fit sort unless an accepted matching capability exists; reset incompatible cursor. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready stable scoped order. |
| Empty State | Successful authorized empty page. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D06: No client float ranking or stale cursor reuse.; UAT-EL-D06-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D06-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D07 — CataloguePagination

Routes: R-CATALOGUE. Requirement trace: R01, R21.

| Field | Contract |
|---|---|
| Element ID | EL-D07 |
| Page/Component | CataloguePagination |
| Element Type | button |
| User Intent | Load next authorized page |
| Triggered Event | activate |
| Proposed Handler | H-EL-D07 / proposed.ui.handle_el_d07 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Opaque cursor bound to caller/scope/query/order/revisions. |
| Validation | Reauthorize before count/lookahead/page; cursor is not a rights grant. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready next page with explicit completeness. |
| Empty State | End-of-visible-page is not source completeness. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D07: Cross-user/revoked/scope-changed cursors rejected uniformly.; UAT-EL-D07-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D07-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D08 — PerfumeCard

Routes: R-CATALOGUE. Requirement trace: R01, R06.

| Field | Contract |
|---|---|
| Element ID | EL-D08 |
| Page/Component | PerfumeCard |
| Element Type | link |
| User Intent | Open one visible perfume identity |
| Triggered Event | activate |
| Proposed Handler | H-EL-D08 / proposed.ui.handle_el_d08 |
| Application Use Case | IF-PROFILE-READ-1 |
| Required Input | Canonical perfume UUID from the visible projection and selection context. |
| Validation | UUID is not authorization; edition uncertainty stays labelled. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-PROFILE-READ-1.output.v1 |
| Success State | Ready/Partial authorized profile. |
| Empty State | No private-object existence hint on hidden/missing identity. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D08: Hidden card/profile cannot be guessed via route or thumbnail.; UAT-EL-D08-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D08-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PROFILE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D09 — DetailTabs

Routes: R-DETAIL. Requirement trace: R03, R07, R17, R21.

| Field | Contract |
|---|---|
| Element ID | EL-D09 |
| Page/Component | DetailTabs |
| Element Type | tablist |
| User Intent | Switch overview/notes/accord/evidence/source sections |
| Triggered Event | select tab |
| Proposed Handler | H-EL-D09 / proposed.ui.handle_el_d09 |
| Application Use Case | IF-PROFILE-READ-1 |
| Required Input | Explicit section enum, current selection snapshot and profile ID. |
| Validation | Authorize each requested field/provenance section; do not pass private source details in client props. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-PROFILE-READ-1.output.v1 |
| Success State | Ready/Partial selected section. |
| Empty State | Explicit authorized no facts versus Unknown clearly separate. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D09: Unselected/conflicting/unlicensed source tabs do not leak; keyboard tabs follow state contract.; UAT-EL-D09-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D09-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PROFILE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D10 — IdentityEvidence

Routes: R-DETAIL. Requirement trace: R01, R21.

| Field | Contract |
|---|---|
| Element ID | EL-D10 |
| Page/Component | IdentityEvidence |
| Element Type | disclosure |
| User Intent | Inspect source/edition uncertainty for visible identity |
| Triggered Event | expand |
| Proposed Handler | H-EL-D10 / proposed.ui.handle_el_d10 |
| Application Use Case | IF-PROFILE-READ-1 |
| Required Input | Authorized evidence projection and exact source/capture/review refs. |
| Validation | Show only permitted provenance; source title/URL alone is not a grant. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-PROFILE-READ-1.output.v1 |
| Success State | Ready labelled evidence or Partial. |
| Empty State | No selected evidence means Unknown, not verified identity. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D10: Private provenance denied independently of public perfume identity.; UAT-EL-D10-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D10-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PROFILE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D11 — FindSimilar

Routes: R-DETAIL. Requirement trace: R05, R07, R16.

| Field | Contract |
|---|---|
| Element ID | EL-D11 |
| Page/Component | FindSimilar |
| Element Type | button |
| User Intent | Prepare a reference-based matching query |
| Triggered Event | activate |
| Proposed Handler | H-EL-D11 / proposed.ui.handle_el_d11 |
| Application Use Case | IF-CAPABILITY-READ-1 |
| Required Input | Accessible perfume ID and explicit intended real method/config versions. |
| Validation | Capability first; no synthetic fixture disguise or fallback method. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CAPABILITY-READ-1.output.v1 |
| Success State | Ready query builder only if future capability allowed. |
| Empty State | Unavailable is not a zero-score result list. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D11: Held/unknown closure/rights/real contract prevents candidate expansion.; UAT-EL-D11-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D11-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CAPABILITY-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D12 — SeedB1Query

Routes: R-DETAIL. Requirement trace: R03, R14.

| Field | Contract |
|---|---|
| Element ID | EL-D12 |
| Page/Component | SeedB1Query |
| Element Type | button |
| User Intent | Prepare reviewed note criteria from visible facts |
| Triggered Event | activate |
| Proposed Handler | H-EL-D12 / proposed.ui.handle_el_d12 |
| Application Use Case | IF-CAPABILITY-READ-1 |
| Required Input | Reviewed canonical note IDs/domain/version; user confirms explicit criteria. |
| Validation | General notes stay general; do not infer complete domains or excluded notes. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CAPABILITY-READ-1.output.v1 |
| Success State | Ready editable query draft only when permitted. |
| Empty State | No usable reviewed IDs => Unknown/Unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D12: No alias/normalization promotion or implicit required/excluded clauses.; UAT-EL-D12-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D12-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CAPABILITY-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D13 — SaveToCart

Routes: R-DETAIL. Requirement trace: R11, R23, R30.

| Field | Contract |
|---|---|
| Element ID | EL-D13 |
| Page/Component | SaveToCart |
| Element Type | button |
| User Intent | Bookmark a visible perfume in own app list |
| Triggered Event | activate |
| Proposed Handler | H-EL-D13 / proposed.ui.handle_el_d13 |
| Application Use Case | IF-PERSONAL-STATE-WRITE-1 |
| Required Input | Own list intent, accessible perfume reference, expected revision/idempotency key. |
| Validation | Derive owner from verified session; no matching/asset eligibility required just to record a permitted bookmark. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-WRITE-1.output.v1 |
| Success State | Ready private app-cart acknowledgement. |
| Empty State | A missing own list may be created only under an accepted write contract. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D13: No marketplace cart/order/payment or public sharing side effect.; UAT-EL-D13-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D13-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D14 — PyramidLayers

Routes: R-PYRAMID. Requirement trace: R03, R13.

| Field | Contract |
|---|---|
| Element ID | EL-D14 |
| Page/Component | PyramidLayers |
| Element Type | disclosure |
| User Intent | Explore top/heart/base and All Listed Notes |
| Triggered Event | expand/select |
| Proposed Handler | H-EL-D14 / proposed.ui.handle_el_d14 |
| Application Use Case | IF-PROFILE-READ-1 |
| Required Input | Profile ID, explicit note domain/layer and selection version. |
| Validation | Do not distribute general-only notes to layers; show unavailable layers rather than empty. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-PROFILE-READ-1.output.v1 |
| Success State | Ready/Partial with source/domain labels. |
| Empty State | Complete-empty only with explicit reviewed closure; blanks remain unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D14: Incomplete/general/held claims never become absent or layered by UI layout.; UAT-EL-D14-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D14-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PROFILE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D15 — CanonicalNoteChip

Routes: R-PYRAMID. Requirement trace: R14.

| Field | Contract |
|---|---|
| Element ID | EL-D15 |
| Page/Component | CanonicalNoteChip |
| Element Type | link |
| User Intent | Find visible perfumes with a reviewed note |
| Triggered Event | activate |
| Proposed Handler | H-EL-D15 / proposed.ui.handle_el_d15 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Reviewed canonical note ID, vocabulary/domain version and explicit filter. |
| Validation | No literal alias-to-ID inference; source labels without accepted canonical mapping are not enabled filters. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready scoped note-filtered catalogue. |
| Empty State | Authorized empty page, not proof no perfume uses the note. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D15: Unknown labels/general domains/aliases cannot be promoted by a click.; UAT-EL-D15-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D15-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D16 — CompletenessBadge

Routes: R-PYRAMID. Requirement trace: R03, R18, R21.

| Field | Contract |
|---|---|
| Element ID | EL-D16 |
| Page/Component | CompletenessBadge |
| Element Type | disclosure |
| User Intent | Understand available/unknown note coverage |
| Triggered Event | expand |
| Proposed Handler | H-EL-D16 / proposed.ui.handle_el_d16 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Already authorized field-state and domain evidence DTO. |
| Validation | No additional lookup or disclosure of inaccessible hold/review details. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready explanation of present/unknown/incomplete/complete-empty. |
| Empty State | No badge value never means zero coverage. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D16: Field-state explanation must not imply disclosed chemical formula.; UAT-EL-D16-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D16-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-D17 — MediaAttribution

Routes: R-PYRAMID. Requirement trace: R13, R21.

| Field | Contract |
|---|---|
| Element ID | EL-D17 |
| Page/Component | MediaAttribution |
| Element Type | disclosure |
| User Intent | Read permitted illustration credit/license/source |
| Triggered Event | expand |
| Proposed Handler | H-EL-D17 / proposed.ui.handle_el_d17 |
| Application Use Case | IF-MEDIA-RESOLVE-1 |
| Required Input | Scoped asset reference and explicit attribution-view use. |
| Validation | Verify permitted metadata/subject association; oil-vial image is not fruit or actual ingredient proof. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MEDIA |
| Data Source | Scoped image_assets/asset_permissions/rights_assessments and approved original-byte loader; path/db/login/callback are server-owned. |
| Output DTO | IF-MEDIA-RESOLVE-1.output.v1 |
| Success State | Ready permitted attribution or labelled placeholder. |
| Empty State | Unknown credit/license => unavailable asset, not free use. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D17: Hidden asset/source ownership or path cannot leak.; UAT-EL-D17-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D17-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-MEDIA-RESOLVE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MEDIA -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D18 — EvidenceExplanation

Routes: R-DETAIL. Requirement trace: R07, R12, R17, R18.

| Field | Contract |
|---|---|
| Element ID | EL-D18 |
| Page/Component | EvidenceExplanation |
| Element Type | disclosure |
| User Intent | Inspect source-backed facts and separate pairwise evidence |
| Triggered Event | expand |
| Proposed Handler | H-EL-D18 / proposed.ui.handle_el_d18 |
| Application Use Case | IF-PROFILE-READ-1 |
| Required Input | Authorized evidence IDs/fields; no generated review claim. |
| Validation | Only selected licensed facts; no AI-generated similarity or unsupported pair assertion. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-PROFILE-READ-1.output.v1 |
| Success State | Ready/Partial evidence with source and uncertainty. |
| Empty State | Unknown evidence remains unknown, not zero confidence. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D18: R12 assistance remains future P5; no LLM call or paid service is introduced.; UAT-EL-D18-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D18-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PROFILE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M01 — ModeSelector

Routes: R-MATCH. Requirement trace: R05, R16, R18.

| Field | Contract |
|---|---|
| Element ID | EL-M01 |
| Page/Component | ModeSelector |
| Element Type | radio group |
| User Intent | Choose an explicitly available matching method |
| Triggered Event | change |
| Proposed Handler | H-EL-M01 / proposed.ui.handle_el_m01 |
| Application Use Case | IF-CAPABILITY-READ-1 |
| Required Input | Explicit method/config/schema IDs, caller and source/vocabulary context. |
| Validation | No default/fallback or cross-method ranking; real A/B1/B2 remain unavailable today. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CAPABILITY-READ-1.output.v1 |
| Success State | Ready enabled method or safe disabled reason. |
| Empty State | No valid method => Unavailable, not empty matches. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M01: Synthetic implementations do not authorize real-data method selection.; UAT-EL-M01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CAPABILITY-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M02 — ReferenceSelector

Routes: R-MATCH. Requirement trace: R05.

| Field | Contract |
|---|---|
| Element ID | EL-M02 |
| Page/Component | ReferenceSelector |
| Element Type | combobox |
| User Intent | Select one authorized reference perfume |
| Triggered Event | select |
| Proposed Handler | H-EL-M02 / proposed.ui.handle_el_m02 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Bounded query and selected canonical profile ID. |
| Validation | Search/count/selection all scoped; selected UUID is not proof of access. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready reference draft with authorized display label. |
| Empty State | Valid Empty after scoped search only. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M02: Private reference guessing, free-label identity merge and stale selections rejected.; UAT-EL-M02-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M02-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M03 — RequiredNotes

Routes: R-MATCH. Requirement trace: R03, R14.

| Field | Contract |
|---|---|
| Element ID | EL-M03 |
| Page/Component | RequiredNotes |
| Element Type | canonical note selector |
| User Intent | Add required B1 clauses |
| Triggered Event | select/change |
| Proposed Handler | H-EL-M03 / proposed.ui.handle_el_m03 |
| Application Use Case | IF-VOCABULARY-READ-1 |
| Required Input | Reviewed canonical IDs, explicit layer/any domain, accepted query-policy version. |
| Validation | Required means the separately accepted hard-rule policy; unknown membership/domain cannot pass. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-VOCABULARY-READ-1.output.v1 |
| Success State | Ready validated draft, not a result. |
| Empty State | Unknown vocabulary => Unavailable; no arbitrary alias fallback. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M03: Missing/incomplete/held note data never satisfies strict required criteria.; UAT-EL-M03-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M03-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-VOCABULARY-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M04 — OptionalNotes

Routes: R-MATCH. Requirement trace: R16.

| Field | Contract |
|---|---|
| Element ID | EL-M04 |
| Page/Component | OptionalNotes |
| Element Type | canonical note selector |
| User Intent | Add soft B1 preferences |
| Triggered Event | select/change |
| Proposed Handler | H-EL-M04 / proposed.ui.handle_el_m04 |
| Application Use Case | IF-VOCABULARY-READ-1 |
| Required Input | Canonical IDs/domain and explicit exact weight policy. |
| Validation | Unmatched optional notes remain in the declared coverage denominator; no hidden defaults. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-VOCABULARY-READ-1.output.v1 |
| Success State | Ready typed preference draft. |
| Empty State | No optional clause is valid local emptiness, not complete source domain. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M04: No arbitrary float or hidden weight coercion.; UAT-EL-M04-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M04-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-VOCABULARY-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M05 — ExcludedNotes

Routes: R-MATCH. Requirement trace: R03, R16.

| Field | Contract |
|---|---|
| Element ID | EL-M05 |
| Page/Component | ExcludedNotes |
| Element Type | canonical note selector |
| User Intent | Express strict excluded-note constraints |
| Triggered Event | select/change |
| Proposed Handler | H-EL-M05 / proposed.ui.handle_el_m05 |
| Application Use Case | IF-VOCABULARY-READ-1 |
| Required Input | Canonical IDs and exact searched domain/version. |
| Validation | Excluded absence needs accepted closed domain; missing data cannot make exclusion pass. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-VOCABULARY-READ-1.output.v1 |
| Success State | Ready draft only, capability still gated. |
| Empty State | Unknown vocabulary/domain remains unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M05: Positive observed exclusion, incomplete domain and conflicts fail as specified by future exact method.; UAT-EL-M05-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M05-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-VOCABULARY-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M06 — LayerSelector

Routes: R-MATCH. Requirement trace: R03, R16.

| Field | Contract |
|---|---|
| Element ID | EL-M06 |
| Page/Component | LayerSelector |
| Element Type | select |
| User Intent | Choose exact top/heart/base or any-pyramid selector |
| Triggered Event | change |
| Proposed Handler | H-EL-M06 / proposed.ui.handle_el_m06 |
| Application Use Case | IF-MATCH-VALIDATE-1 |
| Required Input | Explicit layer enum/domain/vocabulary/query version. |
| Validation | Any-pyramid searches only accepted pyramid domain; general-only source is not a complete pyramid. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-MATCH-VALIDATE-1.output.v1 |
| Success State | Ready validated query draft. |
| Empty State | Unknown layer/domain is unavailable, not empty. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M06: Exact/any contradictions and unsupported domains are rejected; no fallback.; UAT-EL-M06-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M06-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-MATCH-VALIDATE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M07 — AlternativeRuleControls

Routes: R-MATCH. Requirement trace: R16.

| Field | Contract |
|---|---|
| Element ID | EL-M07 |
| Page/Component | AlternativeRuleControls |
| Element Type | disabled policy control |
| User Intent | Review future all/any/minimum rule alternatives |
| Triggered Event | inspect capability |
| Proposed Handler | H-EL-M07 / proposed.ui.handle_el_m07 |
| Application Use Case | IF-MATCH-VALIDATE-1 |
| Required Input | Explicit separate method/config/policy ID, if later approved. |
| Validation | Never loosen accepted B1 required-all semantics by toggling a generic any/min control. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-MATCH-VALIDATE-1.output.v1 |
| Success State | Ready explanatory disabled control only. |
| Empty State | No accepted alternative contract => Unavailable. |
| Unavailable State | Alternative real query policies need a separate exact contract; current synthetic B1 rules remain unchanged. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M07: Unknown alternative policy never dispatches scoring.; UAT-EL-M07-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M07-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; BLOCKED: Alternative real query policies need a separate exact contract; current synthetic B1 rules remain unchanged. |
| Input schema | IF-MATCH-VALIDATE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M08 — AccordPreferenceControls

Routes: R-MATCH. Requirement trace: R03, R07, R16.

| Field | Contract |
|---|---|
| Element ID | EL-M08 |
| Page/Component | AccordPreferenceControls |
| Element Type | disabled sliders/numeric controls |
| User Intent | Explore a future adjustable accord preference profile |
| Triggered Event | change/inspect capability |
| Proposed Handler | H-EL-M08 / proposed.ui.handle_el_m08 |
| Application Use Case | IF-CAPABILITY-READ-1 |
| Required Input | Explicit reviewed taxonomy/scale and a distinct approved method/config. |
| Validation | User preference is not observed perfume strength; no intensity from note order/repetition/prose. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CAPABILITY-READ-1.output.v1 |
| Success State | Ready only after future compatible evidence/policy. |
| Empty State | No real strengths => Unavailable, never default50 or 0. |
| Unavailable State | B2 remains blocked; compatible strengths/taxonomy/method and Owner approval are absent. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M08: B2/presence fallback not silently enabled.; UAT-EL-M08-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M08-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; BLOCKED: B2 remains blocked; compatible strengths/taxonomy/method and Owner approval are absent. |
| Input schema | IF-CAPABILITY-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M09 — AddClause

Routes: R-MATCH. Requirement trace: R14, R16.

| Field | Contract |
|---|---|
| Element ID | EL-M09 |
| Page/Component | AddClause |
| Element Type | button |
| User Intent | Append a typed query clause locally |
| Triggered Event | activate |
| Proposed Handler | H-EL-M09 / proposed.ui.handle_el_m09 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Local query draft and accepted explicit input bounds if available. |
| Validation | Do not infer IDs, resolve aliases or silently drop duplicates/contradictions. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready edited local draft. |
| Empty State | No clauses => Idle guidance, not a score. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M09: No backend write, query history or permission side effect.; UAT-EL-M09-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M09-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-M10 — RemoveClause

Routes: R-MATCH. Requirement trace: R16.

| Field | Contract |
|---|---|
| Element ID | EL-M10 |
| Page/Component | RemoveClause |
| Element Type | button |
| User Intent | Remove one local clause |
| Triggered Event | activate |
| Proposed Handler | H-EL-M10 / proposed.ui.handle_el_m10 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Stable local clause key and current draft revision. |
| Validation | Remove only selected draft clause; invalidate outstanding result generation. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready/Idle updated draft. |
| Empty State | Empty draft remains Idle. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M10: Late results from previous generation cannot repopulate UI.; UAT-EL-M10-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M10-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-M11 — SearchSubmit

Routes: R-MATCH. Requirement trace: R05, R07, R16, R18.

| Field | Contract |
|---|---|
| Element ID | EL-M11 |
| Page/Component | SearchSubmit |
| Element Type | submit button |
| User Intent | Request the explicitly approved matching operation |
| Triggered Event | submit |
| Proposed Handler | H-EL-M11 / proposed.ui.handle_el_m11 |
| Application Use Case | IF-MATCH-EXECUTE-1 |
| Required Input | Validated query, exact method/config/resource policy and trusted caller context. |
| Validation | Authorization and rights before candidate lookup/counts; require accepted real contract and full eligibility proof. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-MATCH-EXECUTE-1.output.v1 |
| Success State | Ready results grouped within compatible partitions only. |
| Empty State | Authorized zero eligible results differs from capability unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M11: No fake synthetic identity, unknown-to-zero, hidden fallback or cross-partition rank.; UAT-EL-M11-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M11-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-MATCH-EXECUTE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M12 — ResetQuery

Routes: R-MATCH. Requirement trace: R16.

| Field | Contract |
|---|---|
| Element ID | EL-M12 |
| Page/Component | ResetQuery |
| Element Type | button |
| User Intent | Reset local draft and invalidate old results |
| Triggered Event | activate |
| Proposed Handler | H-EL-M12 / proposed.ui.handle_el_m12 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Current local draft/request generation. |
| Validation | Clear local selections/results only; no server mutation or stored history inference. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle clean query with accessible status. |
| Empty State | Empty local draft is not a successful search. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M12: Reset cannot change source selections, rights or method defaults.; UAT-EL-M12-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M12-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-M13 — CancelSearch

Routes: R-MATCH. Requirement trace: R16.

| Field | Contract |
|---|---|
| Element ID | EL-M13 |
| Page/Component | CancelSearch |
| Element Type | button |
| User Intent | Abort own UI fetch and invalidate current result generation |
| Triggered Event | activate |
| Proposed Handler | H-EL-M13 / proposed.ui.handle_el_m13 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Own local abort handle and current view/request generation; no server user/role/request authority claim. |
| Validation | Abort local publication; future server disconnect/timeout cleanup releases or discards its lease under a separate accepted contract. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Ready permitted view without stale publication; server cancellation is not falsely guaranteed. |
| Empty State | No active local request is a no-op. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M13: No cancellation payload is sent to query-validation or a guessed cross-user request endpoint.; UAT-EL-M13-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M13-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-M14 — ResultCard

Routes: R-RESULTS. Requirement trace: R01, R05.

| Field | Contract |
|---|---|
| Element ID | EL-M14 |
| Page/Component | ResultCard |
| Element Type | link |
| User Intent | Open one visible result profile |
| Triggered Event | activate |
| Proposed Handler | H-EL-M14 / proposed.ui.handle_el_m14 |
| Application Use Case | IF-PROFILE-READ-1 |
| Required Input | Authorized candidate ID and result/selection context. |
| Validation | Reauthorize target; result membership is not a perpetual access token. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-PROFILE-READ-1.output.v1 |
| Success State | Ready/Partial current permitted profile. |
| Empty State | Hidden/missing candidate is generic Unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M14: Revocation after scoring invalidates later card access.; UAT-EL-M14-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M14-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PROFILE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M15 — FitExplanation

Routes: R-RESULTS. Requirement trace: R16, R18.

| Field | Contract |
|---|---|
| Element ID | EL-M15 |
| Page/Component | FitExplanation |
| Element Type | disclosure |
| User Intent | Expand the already authorized returned structural/query-fit explanation |
| Triggered Event | expand |
| Proposed Handler | H-EL-M15 / proposed.ui.handle_el_m15 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Current authorized MatchResultProjection.v1, exact partition/method/config and view generation. |
| Validation | Render only the returned FitExplanation.v1; no rescore or additional source lookup, no client float ordering. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Already authorized MatchResultProjection.v1 and separately returned evidence channels from IF-MATCH-EXECUTE-1; local disclosure performs no query/rescore. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready returned explanation distinct from confidence/evidence. |
| Empty State | When no valid fit exists use Unavailable; a genuine computed zero is distinct. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M15: Opening a disclosure never calls IF-MATCH-EXECUTE again or fabricates hidden evidence.; UAT-EL-M15-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M15-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-M16 — ConfidenceAndEvidence

Routes: R-RESULTS. Requirement trace: R07, R17, R18, R21.

| Field | Contract |
|---|---|
| Element ID | EL-M16 |
| Page/Component | ConfidenceAndEvidence |
| Element Type | disclosure |
| User Intent | Expand separately returned confidence and pair-evidence channels |
| Triggered Event | expand |
| Proposed Handler | H-EL-M16 / proposed.ui.handle_el_m16 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Already authorized result DTO channels/coverage and current view generation. |
| Validation | Capability status is not an evidence-read API; no new query, source-count-to-confidence or pair-evidence fabrication. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Already authorized MatchResultProjection.v1 and separately returned evidence channels from IF-MATCH-EXECUTE-1; local disclosure performs no query/rescore. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready/Partial/Unknown for the authorized returned channels. |
| Empty State | Missing evidence remains unknown, not confidence0 or similarity0. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M16: No extra source fragments, new rights or server operation from a local disclosure.; UAT-EL-M16-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M16-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-M17 — ResultCompare

Routes: R-RESULTS. Requirement trace: R15.

| Field | Contract |
|---|---|
| Element ID | EL-M17 |
| Page/Component | ResultCompare |
| Element Type | button |
| User Intent | Prepare exactly two visible factual columns |
| Triggered Event | activate |
| Proposed Handler | H-EL-M17 / proposed.ui.handle_el_m17 |
| Application Use Case | IF-COMPARISON-READ-1 |
| Required Input | Two distinct canonical IDs and explicit selected projection. |
| Validation | Authorize both independently; facts may compare without a valid fit score. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-COMPARE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-COMPARISON-READ-1.output.v1 |
| Success State | Ready/Partial two-column comparison. |
| Empty State | Unavailable profile never becomes an empty column proving absence. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M17: No hidden third-column or automatic scoring dependency.; UAT-EL-M17-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M17-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COMPARISON-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-COMPARE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M18 — ResultSave

Routes: R-RESULTS. Requirement trace: R23, R30.

| Field | Contract |
|---|---|
| Element ID | EL-M18 |
| Page/Component | ResultSave |
| Element Type | button |
| User Intent | Save a visible candidate to own app list |
| Triggered Event | activate |
| Proposed Handler | H-EL-M18 / proposed.ui.handle_el_m18 |
| Application Use Case | IF-PERSONAL-STATE-WRITE-1 |
| Required Input | Own list action, candidate ref, expected revision/idempotency key. |
| Validation | Do not copy source-private facts or overwrite existing source links. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-WRITE-1.output.v1 |
| Success State | Ready private bookmark acknowledgement. |
| Empty State | No known list => proposed accepted creation path only. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M18: No marketplace cart/order side effect.; UAT-EL-M18-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M18-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M19 — NarrowOrRetry

Routes: R-RESULTS. Requirement trace: R16.

| Field | Contract |
|---|---|
| Element ID | EL-M19 |
| Page/Component | NarrowOrRetry |
| Element Type | button/filter |
| User Intent | Refine or retry an allowed query |
| Triggered Event | activate |
| Proposed Handler | H-EL-M19 / proposed.ui.handle_el_m19 |
| Application Use Case | IF-MATCH-EXECUTE-1 |
| Required Input | New explicit query/context and accepted retry/resource policy. |
| Validation | Reauthorize; no blind loop, background acquisition or stale eligibility reuse. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-05 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MATCH |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-MATCH-EXECUTE-1.output.v1 |
| Success State | Loading then Ready/Unavailable. |
| Empty State | No eligible visible results remains scoped Valid Empty only. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M19: Unsupported capability never becomes a retry storm or fallback method.; UAT-EL-M19-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M19-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-MATCH-EXECUTE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MATCH -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-C01 — TwoProfileSelectors

Routes: R-COMPARE. Requirement trace: R15.

| Field | Contract |
|---|---|
| Element ID | EL-C01 |
| Page/Component | TwoProfileSelectors |
| Element Type | paired comboboxes |
| User Intent | Choose exactly two distinct authorized perfume identities |
| Triggered Event | select |
| Proposed Handler | H-EL-C01 / proposed.ui.handle_el_c01 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Two slots, canonical IDs and vocabulary/selection context. |
| Validation | R15 requires two columns; no guessed/private identities or aliases. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready comparison draft. |
| Empty State | Missing slot => Idle guidance, not an empty fact set. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-C01: Both profiles are independently scoped before field comparison.; UAT-EL-C01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-C01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-C02 — SwapColumns

Routes: R-COMPARE. Requirement trace: R15, R17.

| Field | Contract |
|---|---|
| Element ID | EL-C02 |
| Page/Component | SwapColumns |
| Element Type | button |
| User Intent | Swap the two existing visible columns locally |
| Triggered Event | activate |
| Proposed Handler | H-EL-C02 / proposed.ui.handle_el_c02 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Already authorized two-column DTO and view generation. |
| Validation | No new lookup; do not recompute score or invert evidence semantics. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready swapped view. |
| Empty State | No full pair => disabled/Idle. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-C02: Swap preserves provenance and separate direction-sensitive pair evidence.; UAT-EL-C02-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-C02-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-C03 — CompareFields

Routes: R-COMPARE. Requirement trace: R03, R15, R17.

| Field | Contract |
|---|---|
| Element ID | EL-C03 |
| Page/Component | CompareFields |
| Element Type | tabs/disclosure |
| User Intent | Compare notes, accords, families and evidence |
| Triggered Event | select/expand |
| Proposed Handler | H-EL-C03 / proposed.ui.handle_el_c03 |
| Application Use Case | IF-COMPARISON-READ-1 |
| Required Input | Two authorized IDs and explicit permitted section. |
| Validation | Shared/listed-only/unknown labels are not complete absence claims; strength/family compatibility required. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-COMPARE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-COMPARISON-READ-1.output.v1 |
| Success State | Ready/Partial facts, fit shown only if separately valid. |
| Empty State | Unknown or unselected fields stay unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-C03: Incomplete source cannot create a negative difference or0% fit.; UAT-EL-C03-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-C03-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COMPARISON-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-COMPARE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-C04 — CompareSave

Routes: R-COMPARE. Requirement trace: R23, R30.

| Field | Contract |
|---|---|
| Element ID | EL-C04 |
| Page/Component | CompareSave |
| Element Type | button |
| User Intent | Bookmark an alternative without copying private source evidence |
| Triggered Event | activate |
| Proposed Handler | H-EL-C04 / proposed.ui.handle_el_c04 |
| Application Use Case | IF-PERSONAL-STATE-WRITE-1 |
| Required Input | Own list action and accessible alternate ID. |
| Validation | Respect own object scope, duplicate policy and revision. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-WRITE-1.output.v1 |
| Success State | Ready private acknowledgement. |
| Empty State | No source listing is automatically created. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-C04: Comparison never places an order.; UAT-EL-C04-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-C04-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P01 — PersonalListViews

Routes: R-CART. Requirement trace: R11, R23, R26.

| Field | Contract |
|---|---|
| Element ID | EL-P01 |
| Page/Component | PersonalListViews |
| Element Type | tabs/filter |
| User Intent | Browse own wishlist/research/app-cart/tried/skipped state without conflating purchases or inventory |
| Triggered Event | change |
| Proposed Handler | H-EL-P01 / proposed.ui.handle_el_p01 |
| Application Use Case | IF-PERSONAL-STATE-READ-1 |
| Required Input | Explicit own personal-list/state filter and page policy. |
| Validation | Owner scope before counts; this response contains personal-list state only. Ordered bookmarks and purchase history use their separate read contracts. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-READ-1.output.v1 |
| Success State | Ready/Partial private list view. |
| Empty State | Valid Empty only for own scoped personal-list view. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P01: No purchase/Ordered/inventory fields or cross-user badges in this contract.; UAT-EL-P01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P02 — InterestStateEditor

Routes: R-CART. Requirement trace: R11, R23, R30.

| Field | Contract |
|---|---|
| Element ID | EL-P02 |
| Page/Component | InterestStateEditor |
| Element Type | select/submit |
| User Intent | Manually change wishlist/research/app-cart/tried/skipped intent |
| Triggered Event | submit |
| Proposed Handler | H-EL-P02 / proposed.ui.handle_el_p02 |
| Application Use Case | IF-PERSONAL-STATE-WRITE-1 |
| Required Input | Allowed personal intent transition, own item, expected revision/idempotency key. |
| Validation | Interest transition is not a purchase or bottle; owner is server-derived. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-WRITE-1.output.v1 |
| Success State | Ready saved intent. |
| Empty State | Missing own item follows accepted creation policy, not another user lookup. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P02: No silent move to Ordered/Owned and no duplicate list item.; UAT-EL-P02-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P02-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P03 — SavedSourceAdd

Routes: R-CART. Requirement trace: R09, R10, R24, R29.

| Field | Contract |
|---|---|
| Element ID | EL-P03 |
| Page/Component | SavedSourceAdd |
| Element Type | form |
| User Intent | Add one private buying-source reference |
| Triggered Event | submit |
| Proposed Handler | H-EL-P03 / proposed.ui.handle_el_p03 |
| Application Use Case | IF-BUYING-SOURCE-WRITE-1 |
| Required Input | Accessible perfume, platform/store/URL and optional observed price/size/date/note. |
| Validation | Bounded URL/scheme/value fields; no credentials/private account export, remote preview or scraper. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized user-private saved_buying_sources / retail_listings / price_observations projection; never live shop scraping. |
| Output DTO | IF-BUYING-SOURCE-WRITE-1.output.v1 |
| Success State | Ready private saved source. |
| Empty State | Optional price/size/date missing remain unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P03: New saved link is not license, availability or chemical/source-fact proof.; UAT-EL-P03-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P03-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-BUYING-SOURCE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P04 — SavedSourceEdit

Routes: R-CART. Requirement trace: R10, R24, R29.

| Field | Contract |
|---|---|
| Element ID | EL-P04 |
| Page/Component | SavedSourceEdit |
| Element Type | form |
| User Intent | Edit own recorded source observation |
| Triggered Event | submit |
| Proposed Handler | H-EL-P04 / proposed.ui.handle_el_p04 |
| Application Use Case | IF-BUYING-SOURCE-WRITE-1 |
| Required Input | Own source ID, exact changed fields and expected revision. |
| Validation | Preserve observation versus paid price and source/date history; no unapproved coercion. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized user-private saved_buying_sources / retail_listings / price_observations projection; never live shop scraping. |
| Output DTO | IF-BUYING-SOURCE-WRITE-1.output.v1 |
| Success State | Ready revised private record. |
| Empty State | Unset optional field remains null/unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P04: Cross-user/stale write rejected; no live price update inferred.; UAT-EL-P04-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P04-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-BUYING-SOURCE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P05 — SavedSourceRemove

Routes: R-CART. Requirement trace: R24, R26.

| Field | Contract |
|---|---|
| Element ID | EL-P05 |
| Page/Component | SavedSourceRemove |
| Element Type | confirmation |
| User Intent | Remove/detach an own saved reference under accepted retention policy |
| Triggered Event | confirm |
| Proposed Handler | H-EL-P05 / proposed.ui.handle_el_p05 |
| Application Use Case | IF-BUYING-SOURCE-WRITE-1 |
| Required Input | Own source/action/revision and explicit confirmation. |
| Validation | No deletion of source provenance, purchase history or other users data; exact withdrawal policy required. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized user-private saved_buying_sources / retail_listings / price_observations projection; never live shop scraping. |
| Output DTO | IF-BUYING-SOURCE-WRITE-1.output.v1 |
| Success State | Ready own reference removed/withdrawn as permitted. |
| Empty State | Already absent own reference follows accepted idempotency contract. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P05: No cascade erasure of purchases or licensed captures.; UAT-EL-P05-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P05-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-BUYING-SOURCE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P06 — BuyingLink

Routes: R-CART. Requirement trace: R09, R10, R24, R25.

| Field | Contract |
|---|---|
| Element ID | EL-P06 |
| Page/Component | BuyingLink |
| Element Type | outbound link |
| User Intent | Open a manually saved external buying page |
| Triggered Event | explicit activate |
| Proposed Handler | H-EL-P06 / proposed.ui.handle_el_p06 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Already authorized allowlisted external URL; no server fetch. |
| Validation | No javascript/data/file/userinfo URL, credentials or account extraction; safe browser navigation/no opener/referrer as selected later. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Browser navigates by user intent only. |
| Empty State | Unknown/invalid URL => safe disabled guidance. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P06: No prefetch, SSRF, checkout/payment/order/cart sync or price promise.; UAT-EL-P06-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P06-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-P07 — ManualOrdered

Routes: R-CART. Requirement trace: R25, R26.

| Field | Contract |
|---|---|
| Element ID | EL-P07 |
| Page/Component | ManualOrdered |
| Element Type | manual confirmation form |
| User Intent | Record that the user reports placing an order elsewhere |
| Triggered Event | submit |
| Proposed Handler | H-EL-P07 / proposed.ui.handle_el_p07 |
| Application Use Case | IF-PURCHASE-STATUS-WRITE-1 |
| Required Input | Own bookmark ID, explicit accepted manual-status enum, recorded-at known/unknown and MutationPrecondition.v1. |
| Validation | Only status/time are changed; no purchase-history, price, bottle or actual order is implicitly created. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Own bookmark/manual Ordered-status projection under an exact accepted repository mapping; no purchase-record, physical-bottle or marketplace operation. |
| Output DTO | IF-PURCHASE-STATUS-WRITE-1.output.v1 |
| Success State | Ready private manual Ordered-status acknowledgement. |
| Empty State | Unknown recorded-at remains explicit unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P07: Idempotent repeat cannot create purchases/bottles; no payment/shipping API.; UAT-EL-P07-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P07-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PURCHASE-STATUS-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P08 — ManualReceived

Routes: R-CART. Requirement trace: R11, R26, R28.

| Field | Contract |
|---|---|
| Element ID | EL-P08 |
| Page/Component | ManualReceived |
| Element Type | manual form |
| User Intent | Record reported physical inventory under accepted rules |
| Triggered Event | submit |
| Proposed Handler | H-EL-P08 / proposed.ui.handle_el_p08 |
| Application Use Case | IF-COLLECTION-WRITE-1 |
| Required Input | Own profile ID, collection-item ID or explicit create-null, accepted ownership value, physical personal fields and mutation precondition. |
| Validation | No undeclared purchase linkage or paid fields; purchased history and physical ownership are distinct, with no supplier confirmation. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-WRITE-1.output.v1 |
| Success State | Ready private inventory acknowledgement only. |
| Empty State | Unknown optional physical attributes remain unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P08: No automatic purchase creation/linkage or external order lookup.; UAT-EL-P08-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P08-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P09 — DuplicateWarning

Routes: R-CART. Requirement trace: R30.

| Field | Contract |
|---|---|
| Element ID | EL-P09 |
| Page/Component | DuplicateWarning |
| Element Type | decision dialog |
| User Intent | Choose an existing own item or add a source instead of duplicate bookmark |
| Triggered Event | confirm choice |
| Proposed Handler | H-EL-P09 / proposed.ui.handle_el_p09 |
| Application Use Case | IF-PERSONAL-STATE-WRITE-1 |
| Required Input | Own visible duplicate decision and explicit allowed action. |
| Validation | Scope duplicate detection before lookup/count; no cross-user existence clue. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-WRITE-1.output.v1 |
| Success State | Ready selected own item or permitted update. |
| Empty State | No authorized duplicate is not global identity uniqueness proof. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P09: No silent identity merge, new purchase or hidden list overwrite.; UAT-EL-P09-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P09-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P10 — MissingPerfumeProposal

Routes: R-CART. Requirement trace: R20, R22.

| Field | Contract |
|---|---|
| Element ID | EL-P10 |
| Page/Component | MissingPerfumeProposal |
| Element Type | metadata request form |
| User Intent | Prepare a private manual missing-perfume proposal |
| Triggered Event | submit |
| Proposed Handler | H-EL-P10 / proposed.ui.handle_el_p10 |
| Application Use Case | IF-SOURCE-INTAKE-REQUEST-1 |
| Required Input | User-provided bounded facts/claims, provenance and private scope; no acquired bytes. |
| Validation | Manual claim is unverified; no canonical promotion, external fetch, source permission or curator role granted. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-SOURCE-INTAKE-REQUEST-1.output.v1 |
| Success State | Ready private review-request acknowledgement. |
| Empty State | Unknown edition/brand/source facts remain explicit. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P10: R20 intent retained without bypassing acquisition/selection gates.; UAT-EL-P10-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P10-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-SOURCE-INTAKE-REQUEST-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P11 — ScreenshotOrURLIntakeRequest

Routes: R-CART. Requirement trace: R09, R21.

| Field | Contract |
|---|---|
| Element ID | EL-P11 |
| Page/Component | ScreenshotOrURLIntakeRequest |
| Element Type | metadata-only request |
| User Intent | Request future review of own URL/screenshot intake |
| Triggered Event | submit |
| Proposed Handler | H-EL-P11 / proposed.ui.handle_el_p11 |
| Application Use Case | IF-ASSET-INTAKE-REQUEST-1 |
| Required Input | Metadata/permission request only; no file bytes/cookies/account export. |
| Validation | R09 future import is gated; private data/rights/format/size/consent and task approval required before any later capture. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-ASSET-INTAKE-REQUEST-1.output.v1 |
| Success State | Ready request status, not imported content. |
| Empty State | No approved intake => unavailable upload. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P11: Request cannot download, upload binaries, call external accounts or authorize acquisition.; UAT-EL-P11-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P11-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-ASSET-INTAKE-REQUEST-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P12 — InventoryLifecycleTabs

Routes: R-COLLECTION. Requirement trace: R11, R26, R27, R28.

| Field | Contract |
|---|---|
| Element ID | EL-P12 |
| Page/Component | InventoryLifecycleTabs |
| Element Type | tabs/filter |
| User Intent | Browse active/finished/sold/gifted physical inventory independently of ever-purchased history |
| Triggered Event | change |
| Proposed Handler | H-EL-P12 / proposed.ui.handle_el_p12 |
| Application Use Case | IF-COLLECTION-READ-1 |
| Required Input | Own inventory lifecycle/status/filter/page policy. |
| Validation | Physical lifecycle history only; purchase records use a separate read contract and survive inventory transitions. Authorize before counts. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-READ-1.output.v1 |
| Success State | Ready/Partial own inventory records. |
| Empty State | Valid Empty only for the requested authorized inventory view. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P12: No purchase-record or paid-fact fields from this inventory contract; distinct denominators.; UAT-EL-P12-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P12-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P13 — BottleCard

Routes: R-COLLECTION. Requirement trace: R11, R28.

| Field | Contract |
|---|---|
| Element ID | EL-P13 |
| Page/Component | BottleCard |
| Element Type | link |
| User Intent | Open one own physical inventory item |
| Triggered Event | activate |
| Proposed Handler | H-EL-P13 / proposed.ui.handle_el_p13 |
| Application Use Case | IF-COLLECTION-READ-1 |
| Required Input | Own inventory UUID and explicit current/history projection. |
| Validation | UUID is not owner proof; foreign record returns uniform unavailable. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-READ-1.output.v1 |
| Success State | Ready/Partial bottle detail. |
| Empty State | Unknown values remain unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P13: No other-user bottle or paid-price disclosure.; UAT-EL-P13-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P13-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P14 — OptionalPurchaseFields

Routes: R-COLLECTION-ITEM. Requirement trace: R26, R28, R29.

| Field | Contract |
|---|---|
| Element ID | EL-P14 |
| Page/Component | OptionalPurchaseFields |
| Element Type | purchase-record form |
| User Intent | Edit an independently authorized own purchase record and optional paid facts |
| Triggered Event | submit |
| Proposed Handler | H-EL-P14 / proposed.ui.handle_el_p14 |
| Application Use Case | IF-PURCHASE-RECORD-WRITE-1 |
| Required Input | Own purchase-record ID/profile, optional own saved-source reference, Money/Quantity/PurchaseDate/SellerValue known-unknown values, field-policy ref and mutation precondition. |
| Validation | Paid facts never mutate through an inventory endpoint; listing price is not paid price; no null-to-zero or assumed currency/unit. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Own private purchase_records and separately authorized optional saved-buying-source linkage; no inventory mutation or actual order/payment. |
| Output DTO | IF-PURCHASE-RECORD-WRITE-1.output.v1 |
| Success State | Ready own purchase-record/history-version acknowledgement. |
| Empty State | Unknown optional paid facts remain explicit unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P14: Cross-user/FK/stale/idempotency/retention conflicts fail without bottle/order/cascade side effects.; UAT-EL-P14-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P14-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PURCHASE-RECORD-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P15 — PersonalNotes

Routes: R-COLLECTION-ITEM. Requirement trace: R11.

| Field | Contract |
|---|---|
| Element ID | EL-P15 |
| Page/Component | PersonalNotes |
| Element Type | form |
| User Intent | Edit own bottle/trial notes |
| Triggered Event | submit |
| Proposed Handler | H-EL-P15 / proposed.ui.handle_el_p15 |
| Application Use Case | IF-COLLECTION-WRITE-1 |
| Required Input | Own record, bounded text, version/idempotency contract. |
| Validation | No implicit external publication, AI submission or HTML execution. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-WRITE-1.output.v1 |
| Success State | Ready private note acknowledgement. |
| Empty State | Cleared note is explicit empty personal text, not an absent perfume note. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P15: Sanitize rendering and redact raw private notes in logs/caches.; UAT-EL-P15-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P15-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P16 — RemainingAmount

Routes: R-COLLECTION-ITEM. Requirement trace: R11, R26, R29.

| Field | Contract |
|---|---|
| Element ID | EL-P16 |
| Page/Component | RemainingAmount |
| Element Type | numeric form |
| User Intent | Record known remaining amount with explicit unit |
| Triggered Event | submit |
| Proposed Handler | H-EL-P16 / proposed.ui.handle_el_p16 |
| Application Use Case | IF-COLLECTION-WRITE-1 |
| Required Input | Own item, exact finite amount/unit and optional known capacity. |
| Validation | Bounds/unit conversion only under accepted policy; unknown remains unknown, no inferred finish/purchase deletion. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-WRITE-1.output.v1 |
| Success State | Ready recorded estimate labelled user-reported. |
| Empty State | Missing amount stays Unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P16: Negative/overcapacity/infinite/coerced value rejected; no automatic history erase.; UAT-EL-P16-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P16-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P17 — FinishBottle

Routes: R-COLLECTION-ITEM. Requirement trace: R11, R26, R28.

| Field | Contract |
|---|---|
| Element ID | EL-P17 |
| Page/Component | FinishBottle |
| Element Type | confirmation |
| User Intent | Mark own bottle finished while retaining history |
| Triggered Event | confirm |
| Proposed Handler | H-EL-P17 / proposed.ui.handle_el_p17 |
| Application Use Case | IF-COLLECTION-WRITE-1 |
| Required Input | Own inventory ID, finished action, expected revision/idempotency. |
| Validation | Change physical lifecycle only under accepted transition; purchase history immutable to this action. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-WRITE-1.output.v1 |
| Success State | Ready history/current-owned update. |
| Empty State | No active bottle -> safe own-record guidance. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P17: Finished never removes EverPurchased or creates a negative price.; UAT-EL-P17-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P17-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P18 — SellBottle

Routes: R-COLLECTION-ITEM. Requirement trace: R11, R26.

| Field | Contract |
|---|---|
| Element ID | EL-P18 |
| Page/Component | SellBottle |
| Element Type | confirmation |
| User Intent | Record own bottle sold manually |
| Triggered Event | confirm |
| Proposed Handler | H-EL-P18 / proposed.ui.handle_el_p18 |
| Application Use Case | IF-COLLECTION-WRITE-1 |
| Required Input | Own item, sold action and accepted versioned transition. |
| Validation | No sale/payment/order is executed by app; historical purchase remains. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-WRITE-1.output.v1 |
| Success State | Ready manual lifecycle acknowledgement. |
| Empty State | Unknown sale details remain unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P18: No commerce integration or other-user inventory write.; UAT-EL-P18-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P18-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P19 — GiftBottle

Routes: R-COLLECTION-ITEM. Requirement trace: R11, R26.

| Field | Contract |
|---|---|
| Element ID | EL-P19 |
| Page/Component | GiftBottle |
| Element Type | confirmation |
| User Intent | Record own bottle gifted manually |
| Triggered Event | confirm |
| Proposed Handler | H-EL-P19 / proposed.ui.handle_el_p19 |
| Application Use Case | IF-COLLECTION-WRITE-1 |
| Required Input | Own item, gifted action, expected revision/idempotency. |
| Validation | No recipient personal data or external message needed; preserve historical purchase. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-WRITE-1.output.v1 |
| Success State | Ready manual lifecycle acknowledgement. |
| Empty State | Unknown recipient/details remain unset. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P19: No purchase-history cascade deletion or private export.; UAT-EL-P19-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P19-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P20 — Rebuy

Routes: R-COLLECTION. Requirement trace: R23, R25, R26.

| Field | Contract |
|---|---|
| Element ID | EL-P20 |
| Page/Component | Rebuy |
| Element Type | button |
| User Intent | Return to own shopping research without creating an order |
| Triggered Event | activate |
| Proposed Handler | H-EL-P20 / proposed.ui.handle_el_p20 |
| Application Use Case | IF-PERSONAL-STATE-WRITE-1 |
| Required Input | Accessible perfume ref and explicit own app-cart intent. |
| Validation | No copy of another users sources and no new purchase until separately recorded. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-WRITE-1.output.v1 |
| Success State | Ready own bookmark/research state. |
| Empty State | No known buying source remains Unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P20: Rebuy is not checkout, synchronization or a supplier request.; UAT-EL-P20-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P20-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P21 — DashboardFilters

Routes: R-DASHBOARD. Requirement trace: R27, R29.

| Field | Contract |
|---|---|
| Element ID | EL-P21 |
| Page/Component | DashboardFilters |
| Element Type | select/date controls |
| User Intent | Filter authorized own summary period/status |
| Triggered Event | change |
| Proposed Handler | H-EL-P21 / proposed.ui.handle_el_p21 |
| Application Use Case | IF-DASHBOARD-READ-1 |
| Required Input | Explicit own scope, date/status and denominator policy. |
| Validation | Counts and source-derived classifications gated before aggregation; lifecycle and market availability not inferred. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-DASHBOARD-READ-1.output.v1 |
| Success State | Ready/Partial scoped metrics. |
| Empty State | No authorized records => Valid Empty; missing classifications remain Unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P21: No cross-user totals or silent missing-price0 aggregation.; UAT-EL-P21-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P21-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-DASHBOARD-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P22 — DashboardMetricDisclosure

Routes: R-DASHBOARD. Requirement trace: R26, R27, R28.

| Field | Contract |
|---|---|
| Element ID | EL-P22 |
| Page/Component | DashboardMetricDisclosure |
| Element Type | disclosure |
| User Intent | Explain CurrentOwned versus EverPurchased metrics |
| Triggered Event | expand |
| Proposed Handler | H-EL-P22 / proposed.ui.handle_el_p22 |
| Application Use Case | IF-DASHBOARD-READ-1 |
| Required Input | Authorized metric/coverage/date projection. |
| Validation | Use distinct inventory/purchase records; classify only permitted selected facts. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-DASHBOARD-READ-1.output.v1 |
| Success State | Ready denominator/coverage explanation. |
| Empty State | Unknown coverage is not0% or total-world coverage. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P22: Finished/sold/gifted bottles preserve purchase-history metric.; UAT-EL-P22-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P22-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-DASHBOARD-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P23 — DashboardChartDrilldown

Routes: R-DASHBOARD. Requirement trace: R02, R03, R27.

| Field | Contract |
|---|---|
| Element ID | EL-P23 |
| Page/Component | DashboardChartDrilldown |
| Element Type | chart/table link |
| User Intent | Inspect brand-origin/family/note counts through accessible alternatives |
| Triggered Event | activate |
| Proposed Handler | H-EL-P23 / proposed.ui.handle_el_p23 |
| Application Use Case | IF-COLLECTION-READ-1 |
| Required Input | Own authorized aggregate bucket and explicit allowed drilldown filter. |
| Validation | Charts never imply chemical composition or preference certainty; unknown groups/coverage retained. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-COLLECTION-READ-1.output.v1 |
| Success State | Ready scoped detail list and textual chart equivalent. |
| Empty State | Missing classification remains unknown group, not zero membership. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P23: Keyboard/table alternative matches permitted chart counts without leaking hidden records.; UAT-EL-P23-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P23-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-COLLECTION-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P24 — DeferredSpendingAnalytics

Routes: R-DASHBOARD. Requirement trace: R29, R31.

| Field | Contract |
|---|---|
| Element ID | EL-P24 |
| Page/Component | DeferredSpendingAnalytics |
| Element Type | disabled disclosure |
| User Intent | Explain the deferred optional spending analytics milestone |
| Triggered Event | inspect |
| Proposed Handler | H-EL-P24 / proposed.ui.handle_el_p24 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Static deferred capability explanation only. |
| Validation | R31 stays DEFERRED; missing prices are not0 and no financial statistic is invented. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready accessible unavailable explanation. |
| Empty State | No spending data is not a zero-spend claim. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P24: No hidden implementation or acceptance of R31/paid analysis.; UAT-EL-P24-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P24-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-S01 — ReviewQueueNavigation

Routes: R-SYSTEM. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S01 |
| Page/Component | ReviewQueueNavigation |
| Element Type | link/filter |
| User Intent | Open permitted reviewer task categories and summaries |
| Triggered Event | activate |
| Proposed Handler | H-EL-S01 / proposed.ui.handle_el_s01 |
| Application Use Case | IF-REVIEW-QUEUE-READ-1 |
| Required Input | Genuine authorized reviewer context and explicit queue kind. |
| Validation | No generic admin API, guessed role, privileged browser session or private counts before authorization. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-REVIEW-QUEUE-READ-1.output.v1 |
| Success State | Ready scoped queue metadata. |
| Empty State | Authorized empty queue only. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S01: Reader/operator/curator authorities remain separate.; UAT-EL-S01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-REVIEW-QUEUE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S02 — SourceMetadataDisclosure

Routes: R-SOURCES. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S02 |
| Page/Component | SourceMetadataDisclosure |
| Element Type | disclosure |
| User Intent | Inspect permitted capture/license/revision evidence |
| Triggered Event | expand |
| Proposed Handler | H-EL-S02 / proposed.ui.handle_el_s02 |
| Application Use Case | IF-REVIEW-QUEUE-READ-1 |
| Required Input | Scoped source/capture/evidence reference and view permission. |
| Validation | No public entity shortcut to private raw source records or account data. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-REVIEW-QUEUE-READ-1.output.v1 |
| Success State | Ready/Partial permitted metadata. |
| Empty State | Missing authority/version evidence stays Unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S02: Raw staging/credentials/cookies are not response fields.; UAT-EL-S02-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S02-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-REVIEW-QUEUE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S03 — SourceIntakeRequest

Routes: R-SOURCES. Requirement trace: R19, R20, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S03 |
| Page/Component | SourceIntakeRequest |
| Element Type | form |
| User Intent | Request a bounded future source operation for review |
| Triggered Event | submit |
| Proposed Handler | H-EL-S03 / proposed.ui.handle_el_s03 |
| Application Use Case | IF-SOURCE-INTAKE-REQUEST-1 |
| Required Input | Exact source/method/fields/budget/use/permission evidence and requested task. |
| Validation | Request is not approval; no scraping, account extraction or operator ETL call from submit. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-SOURCE-INTAKE-REQUEST-1.output.v1 |
| Success State | Ready pending review-request acknowledgement. |
| Empty State | Missing permission/budget => unavailable acquisition. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S03: No source import, new source rights or canonical promotion.; UAT-EL-S03-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S03-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-SOURCE-INTAKE-REQUEST-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S04 — ReviewQueueFilters

Routes: R-REVIEWS. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S04 |
| Page/Component | ReviewQueueFilters |
| Element Type | select |
| User Intent | Filter authorized proposals/conflicts/holds |
| Triggered Event | change |
| Proposed Handler | H-EL-S04 / proposed.ui.handle_el_s04 |
| Application Use Case | IF-REVIEW-QUEUE-READ-1 |
| Required Input | Own permitted reviewer scope, queue filter, snapshot/page policy. |
| Validation | All44holds/43proposals/Khamrah remain unchanged by browsing. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-REVIEW-QUEUE-READ-1.output.v1 |
| Success State | Ready scoped review page. |
| Empty State | Authorized empty queue, not no conflicts globally. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S04: No protected identifiers/counts through query filters.; UAT-EL-S04-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S04-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-REVIEW-QUEUE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S05 — ProposalDiff

Routes: R-REVIEWS. Requirement trace: R03, R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S05 |
| Page/Component | ProposalDiff |
| Element Type | disclosure |
| User Intent | Compare an immutable observation with a proposed selected projection |
| Triggered Event | expand |
| Proposed Handler | H-EL-S05 / proposed.ui.handle_el_s05 |
| Application Use Case | IF-REVIEW-QUEUE-READ-1 |
| Required Input | Exact source/observation/proposal/version IDs and allowed fields. |
| Validation | Do not merge structured/prose claims or normalize away occurrence evidence. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-REVIEW-QUEUE-READ-1.output.v1 |
| Success State | Ready/Partial visible evidence diff. |
| Empty State | Unknown or inaccessible claim remains unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S05: Section/field locators and conflict membership remain distinct.; UAT-EL-S05-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S05-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-REVIEW-QUEUE-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S06 — ApproveReviewDecision

Routes: R-REVIEWS. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S06 |
| Page/Component | ApproveReviewDecision |
| Element Type | form |
| User Intent | Record a specifically approved reviewer decision, not global policy acceptance |
| Triggered Event | submit |
| Proposed Handler | H-EL-S06 / proposed.ui.handle_el_s06 |
| Application Use Case | IF-REVIEW-DECISION-WRITE-1 |
| Required Input | Exact proposal/version/action/reason/evidence and genuine reviewer authority. |
| Validation | Separate review/selection/normalization/eligibility/intake approvals; no44holdrelease or underlying license grant by generic approve. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-REVIEW-DECISION-WRITE-1.output.v1 |
| Success State | Ready recorded decision under future exact task. |
| Empty State | No reviewed proposal => unavailable action. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S06: Stale/cross-scope/conflicting/unauthorized decision fails atomically.; UAT-EL-S06-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S06-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-REVIEW-DECISION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S07 — RejectReviewDecision

Routes: R-REVIEWS. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S07 |
| Page/Component | RejectReviewDecision |
| Element Type | form |
| User Intent | Record a review rejection retaining original source evidence |
| Triggered Event | submit |
| Proposed Handler | H-EL-S07 / proposed.ui.handle_el_s07 |
| Application Use Case | IF-REVIEW-DECISION-WRITE-1 |
| Required Input | Exact reviewed version, reject reason and expected revision. |
| Validation | Append decision; do not rewrite/delete immutable source claim or source rights. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-REVIEW-DECISION-WRITE-1.output.v1 |
| Success State | Ready rejection history. |
| Empty State | Unknown proposal stays unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S07: Rejection preserves earlier evidence and does not silently select another claim.; UAT-EL-S07-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S07-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-REVIEW-DECISION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S08 — HoldReviewDecision

Routes: R-REVIEWS. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S08 |
| Page/Component | HoldReviewDecision |
| Element Type | form |
| User Intent | Record/defer an unresolved review without promotion |
| Triggered Event | submit |
| Proposed Handler | H-EL-S08 / proposed.ui.handle_el_s08 |
| Application Use Case | IF-REVIEW-DECISION-WRITE-1 |
| Required Input | Exact claim/proposal/version, hold/defer reason and actor. |
| Validation | No normalization winner or eligibility change; required separate transition remains blocked. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-REVIEW-DECISION-WRITE-1.output.v1 |
| Success State | Ready held/deferred review history. |
| Empty State | Missing evidence stays unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S08: Held data must not enter real matching as complete/zero.; UAT-EL-S08-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S08-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-REVIEW-DECISION-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S09 — AssetUseScopeEditor

Routes: R-RIGHTS-MEDIA. Requirement trace: R13, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S09 |
| Page/Component | AssetUseScopeEditor |
| Element Type | review form |
| User Intent | Review exact acquire/store/private/public/derivative permission evidence |
| Triggered Event | submit |
| Proposed Handler | H-EL-S09 / proposed.ui.handle_el_s09 |
| Application Use Case | IF-RIGHTS-REVIEW-1 |
| Required Input | Exact asset/source/rights-holder evidence, action/audience/revision and review decision. |
| Validation | Reviewer records evidence; cannot create licensor authority, waive source ancestry or convert public URL into a grant. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-RIGHTS-REVIEW-1.output.v1 |
| Success State | Ready permitted review record, not acquired bytes. |
| Empty State | Unknown authority/use remains unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S09: Public/private/derivative uses are independent; metadata permission is not display permission.; UAT-EL-S09-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S09-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-RIGHTS-REVIEW-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S10 — AttributionReview

Routes: R-RIGHTS-MEDIA. Requirement trace: R13, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S10 |
| Page/Component | AttributionReview |
| Element Type | form/disclosure |
| User Intent | Review creator/license/change notice and subject association |
| Triggered Event | submit |
| Proposed Handler | H-EL-S10 / proposed.ui.handle_el_s10 |
| Application Use Case | IF-RIGHTS-REVIEW-1 |
| Required Input | Exact authorized asset/source/license version and proposed attribution. |
| Validation | Page revision/SHA1 claim is not original-file SHA256 or ownership proof. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-RIGHTS-REVIEW-1.output.v1 |
| Success State | Ready permitted attribution record. |
| Empty State | Unknown attribution/authority blocks use. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S10: Oil vial/illustration is not perfume composition; no creator/source assertion invented.; UAT-EL-S10-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S10-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-RIGHTS-REVIEW-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S11 — AssetIntakeRequest

Routes: R-RIGHTS-MEDIA. Requirement trace: R13, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S11 |
| Page/Component | AssetIntakeRequest |
| Element Type | metadata form |
| User Intent | Request review of exact original PNG sample intake |
| Triggered Event | submit |
| Proposed Handler | H-EL-S11 / proposed.ui.handle_el_s11 |
| Application Use Case | IF-ASSET-INTAKE-REQUEST-1 |
| Required Input | Exact candidate identity, permission/method/budget/format/use proposal; no bytes. |
| Validation | Currentpair021/022notintakeapproved; no new codecs, conversion, resizing or metadata stripping. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-ASSET-INTAKE-REQUEST-1.output.v1 |
| Success State | Ready pending request acknowledgement. |
| Empty State | Rights/technical gaps => unavailable intake. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S11: Request cannot download or publish an image.; UAT-EL-S11-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S11-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-ASSET-INTAKE-REQUEST-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S12 — WithdrawAssetUse

Routes: R-RIGHTS-MEDIA. Requirement trace: R21.

| Field | Contract |
|---|---|
| Element ID | EL-S12 |
| Page/Component | WithdrawAssetUse |
| Element Type | review form |
| User Intent | Record project access withdrawal/revocation evidence for an exact use |
| Triggered Event | submit |
| Proposed Handler | H-EL-S12 / proposed.ui.handle_el_s12 |
| Application Use Case | IF-RIGHTS-REVIEW-1 |
| Required Input | Exact allowed decision/evidence/version and actor. |
| Validation | Do not claim a compliant CC license becomes revocable or erase delivered bytes; stop future project operations as accepted. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-RIGHTS-REVIEW-1.output.v1 |
| Success State | Ready recorded project denial/review state. |
| Empty State | Unknown underlying right remains unknown. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S12: Revoke invalidates next operation/restore access; no silent delete or new grant.; UAT-EL-S12-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S12-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-RIGHTS-REVIEW-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S13 — OperatorStatusRefresh

Routes: R-OPERATIONS. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S13 |
| Page/Component | OperatorStatusRefresh |
| Element Type | button |
| User Intent | Read an explicitly permitted sanitized local status snapshot |
| Triggered Event | activate |
| Proposed Handler | H-EL-S13 / proposed.ui.handle_el_s13 |
| Application Use Case | IF-OPERATOR-STATUS-READ-1 |
| Required Input | Allowed readonly status category and accepted operator-view context. |
| Validation | No browser shell/start/restart/migrate/reset/restore/credentials or raw dump output. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-REVIEW |
| Data Source | Authorized proposal/rights/review/staging/audit metadata only; no browser operator execution or acquisition permission. |
| Output DTO | IF-OPERATOR-STATUS-READ-1.output.v1 |
| Success State | Ready dated sanitized status or Unknown. |
| Empty State | Unavailable engine/current measurement => NOT VERIFIED, not stale counts as fresh. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S13: PR8experiments not repeated; no side-effect operation behind refresh.; UAT-EL-S13-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S13-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-OPERATOR-STATUS-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-REVIEW -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S14 — RunbookLinks

Routes: R-OPERATIONS. Requirement trace: R19, R21.

| Field | Contract |
|---|---|
| Element ID | EL-S14 |
| Page/Component | RunbookLinks |
| Element Type | link |
| User Intent | Read static permitted operator instructions |
| Triggered Event | activate |
| Proposed Handler | H-EL-S14 / proposed.ui.handle_el_s14 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Allowlisted local documentation route; no executable command argument. |
| Validation | View-only; do not execute source/tooling or load arbitrary filesystem paths. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready documentation. |
| Empty State | Missing runbook is safe Unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S14: No privilege escalation or destructive action from a link.; UAT-EL-S14-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S14-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-S15 — OwnPreferences

Routes: R-SETTINGS. Requirement trace: R01, R11.

| Field | Contract |
|---|---|
| Element ID | EL-S15 |
| Page/Component | OwnPreferences |
| Element Type | form |
| User Intent | Change only accepted own display preferences |
| Triggered Event | submit |
| Proposed Handler | H-EL-S15 / proposed.ui.handle_el_s15 |
| Application Use Case | IF-PRIVATE-SETTINGS-1 |
| Required Input | Allowlisted own preference fields and expected revision. |
| Validation | Cannot change roles, auth subject, database scope, source rights, cache/privacy policy or scoring defaults. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Future accepted session authority / owner preferences; no browser-selected database identity. |
| Output DTO | IF-PRIVATE-SETTINGS-1.output.v1 |
| Success State | Ready own preference acknowledgement. |
| Empty State | Unknown preference uses no hidden server default. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S15: No role/cache/realmatching activation through settings.; UAT-EL-S15-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S15-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PRIVATE-SETTINGS-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S16 — CachePrivacyDisclosure

Routes: R-SETTINGS. Requirement trace: R21.

| Field | Contract |
|---|---|
| Element ID | EL-S16 |
| Page/Component | CachePrivacyDisclosure |
| Element Type | disclosure |
| User Intent | Understand conservative ephemeral/private offline behavior |
| Triggered Event | expand |
| Proposed Handler | H-EL-S16 / proposed.ui.handle_el_s16 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Static policy and authorized session-view metadata only. |
| Validation | No persistent private caching enabled by checkbox; no service worker implementation. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready explanation of static-only/offline unavailable behavior. |
| Empty State | Offline private data remains Unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S16: No claimno-store erases already delivered browser content.; UAT-EL-S16-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S16-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-S17 — SignOut

Routes: R-SETTINGS. Requirement trace: R21.

| Field | Contract |
|---|---|
| Element ID | EL-S17 |
| Page/Component | SignOut |
| Element Type | button |
| User Intent | End own future application session and invalidate UI generation |
| Triggered Event | activate |
| Proposed Handler | H-EL-S17 / proposed.ui.handle_el_s17 |
| Application Use Case | IF-SESSION-END-1 |
| Required Input | Verified own session and accepted logout/cancellation contract. |
| Validation | Cancel/rollback/release own lease; clear UI buffers best-effort, never rebind another principal. |
| Authorization Gate | G-SEC-01 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-AUTHN |
| Data Source | Future accepted session authority / owner preferences; no browser-selected database identity. |
| Output DTO | IF-SESSION-END-1.output.v1 |
| Success State | Idle generic signed-out shell. |
| Empty State | Already-ended own session follows explicit idempotency contract. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S17: Late response cannot restore private result; no remote-erasure guarantee.; UAT-EL-S17-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S17-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-SESSION-END-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-AUTHN -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-S18 — AuthenticationForm

Routes: R-SIGNIN. Requirement trace: R21.

| Field | Contract |
|---|---|
| Element ID | EL-S18 |
| Page/Component | AuthenticationForm |
| Element Type | provider-dependent form placeholder |
| User Intent | Establish a future accepted application session |
| Triggered Event | submit |
| Proposed Handler | H-EL-S18 / proposed.ui.handle_el_s18 |
| Application Use Case | IF-AUTH-SESSION-1 |
| Required Input | Exact provider proof/schema/resource policy after Owner selection; no browser database identity. |
| Validation | Provider/session/binding are unselected; no admin login proxy, user-ID/GUC/SETROLE identity shortcut. |
| Authorization Gate | G-SEC-01 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-AUTHN |
| Data Source | Future accepted session authority / owner preferences; no browser-selected database identity. |
| Output DTO | IF-AUTH-SESSION-1.output.v1 |
| Success State | Ready verified server session only after its future contract. |
| Empty State | No provider contract => Unavailable sign-in, not a fabricated session. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-S18: Account/private-object existence not leaked; no token/localStorage/credential logging defaults.; UAT-EL-S18-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-S18-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-AUTH-SESSION-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-AUTHN -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-M20 — ClearCurrentInput

Routes: R-MATCH. Requirement trace: R16.

| Field | Contract |
|---|---|
| Element ID | EL-M20 |
| Page/Component | ClearCurrentInput |
| Element Type | button |
| User Intent | Clear one local reference/search/clause input without changing policy |
| Triggered Event | activate |
| Proposed Handler | H-EL-M20 / proposed.ui.handle_el_m20 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Own local draft field and current view generation. |
| Validation | Clear local draft only; retain explicit method/version policy, invalidate stale results and do not infer an empty source domain. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready/Idle edited draft. |
| Empty State | Empty query input is not an executed search or zero fit. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-M20: No network request, implicit default method, permission or stored-data change.; UAT-EL-M20-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-M20-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-P25 — RecordPurchase

Routes: R-CART, R-COLLECTION, R-COLLECTION-ITEM. Requirement trace: R25, R26, R28, R29.

| Field | Contract |
|---|---|
| Element ID | EL-P25 |
| Page/Component | RecordPurchase |
| Element Type | manual purchase-record form |
| User Intent | Explicitly record an own purchase history event independently of Ordered or physical inventory |
| Triggered Event | submit |
| Proposed Handler | H-EL-P25 / proposed.ui.handle_el_p25 |
| Application Use Case | IF-PURCHASE-RECORD-WRITE-1 |
| Required Input | Create/update/withdraw intent, own purchase ID/null, permitted profile/source reference, typed optional paid facts, exact field-policy version and mutation precondition. |
| Validation | No actual order/payment; no automatic bottle/status write, no currency/unit/null coercion; exact retention/withdrawal policy required. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Own private purchase_records and separately authorized optional saved-buying-source linkage; no inventory mutation or actual order/payment. |
| Output DTO | IF-PURCHASE-RECORD-WRITE-1.output.v1 |
| Success State | Ready own purchase-record/version/operation receipt. |
| Empty State | Optional paid amount/date/volume/seller unknown is not zero or guessed. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P25: Replay/stale/cross-user/link/field-policy tests preserve EverPurchased through inventory lifecycle changes.; UAT-EL-P25-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P25-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PURCHASE-RECORD-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P27 — PurchaseHistoryPanel

Routes: R-CART, R-COLLECTION, R-COLLECTION-ITEM. Requirement trace: R11, R26, R28, R29.

| Field | Contract |
|---|---|
| Element ID | EL-P27 |
| Page/Component | PurchaseHistoryPanel |
| Element Type | paginated history/detail panel |
| User Intent | Read own purchase history including records with no saved-source or inventory linkage |
| Triggered Event | load/filter/page |
| Proposed Handler | H-EL-P27 / proposed.ui.handle_el_p27 |
| Application Use Case | IF-PURCHASE-RECORD-READ-1 |
| Required Input | Exact own-history query or purchase-record ID, accepted field/page/sort/budget policy and explicit independently authorized profile filter if used. |
| Validation | Authorize purchase-record scope before lookup/count/page; no inferred collection-item FK. Inventory-context panels require a separate accepted linkage policy or stay unavailable. Optional paid facts retain known/unknown values. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Authorized private purchase_records/inventory_items plus separately permitted catalogue classifications; missing paid price stays unknown. |
| Output DTO | IF-PURCHASE-RECORD-READ-1.output.v1 |
| Success State | Ready/Partial bounded own PurchaseRecordProjection history/detail and authorized cursor. |
| Empty State | Valid Empty only for the authorized query; unavailable linkage is not empty history. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P27: Foreign IDs and cursors use uniform unavailable; unlinked purchases remain readable through own history; finished/sold/gifted inventory cannot erase them.; UAT-EL-P27-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P27-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PURCHASE-RECORD-READ-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D20 — CurrentnessFilter

Routes: R-CATALOGUE. Requirement trace: R01, R04, R21.

| Field | Contract |
|---|---|
| Element ID | EL-D20 |
| Page/Component | CurrentnessFilter |
| Element Type | policy-gated select |
| User Intent | Filter only reviewed lifecycle/currentness observations under an exact policy |
| Triggered Event | change |
| Proposed Handler | H-EL-D20 / proposed.ui.handle_el_d20 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Explicit accepted source/currentness/freshness policy and allowed current/unknown/historical selection. |
| Validation | No release-year-to-availability inference or invented TTL; absent policy disables this filter. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready/Partial dated scoped observations only if the future policy permits. |
| Empty State | Unknown currentness is not current, discontinued or out of stock. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D20: Stale/unknown/market/source-rights tests; no silent default freshness threshold.; UAT-EL-D20-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D20-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-D21 — CanonicalBrandFilter

Routes: R-CATALOGUE. Requirement trace: R01, R02, R06, R22.

| Field | Contract |
|---|---|
| Element ID | EL-D21 |
| Page/Component | CanonicalBrandFilter |
| Element Type | select |
| User Intent | Filter one reviewed brand identity separately from origin and positioning |
| Triggered Event | change |
| Proposed Handler | H-EL-D21 / proposed.ui.handle_el_d21 |
| Application Use Case | IF-CATALOGUE-QUERY-1 |
| Required Input | Reviewed canonical brand ID, vocabulary/selection context and explicit filter. |
| Validation | No name-only/alias/country merge; unreviewed brand identity stays unknown. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-CATALOGUE |
| Data Source | Authorized selected observation/materialized catalogue/vocabulary projection under source/field/use rights; raw staging is not a browser data source. |
| Output DTO | IF-CATALOGUE-QUERY-1.output.v1 |
| Success State | Ready scoped brand-filtered page. |
| Empty State | Scoped Valid Empty is not no products from that brand globally. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D21: Brand/origin/position remain independent and hidden/private identities cannot be enumerated.; UAT-EL-D21-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D21-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-CATALOGUE-QUERY-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-CATALOGUE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-P26 — CartRemoveOrMove

Routes: R-CART. Requirement trace: R11, R23, R26, R30.

| Field | Contract |
|---|---|
| Element ID | EL-P26 |
| Page/Component | CartRemoveOrMove |
| Element Type | confirmation/select |
| User Intent | Remove or move only an own personal-list entry under an accepted transition |
| Triggered Event | confirm |
| Proposed Handler | H-EL-P26 / proposed.ui.handle_el_p26 |
| Application Use Case | IF-PERSONAL-STATE-WRITE-1 |
| Required Input | Own entry/list, explicit allowed withdrawal or target-state action, revision/idempotency/retention policy. |
| Validation | No perfume/canonical/source/purchase/bottle deletion; exact list transition and linked-history behavior required. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-06 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-PRIVATE |
| Data Source | Owner-scoped user_lists/user_list_items and approved state projection; distinct from purchase_records and inventory_items. |
| Output DTO | IF-PERSONAL-STATE-WRITE-1.output.v1 |
| Success State | Ready own list transition acknowledgement. |
| Empty State | Already withdrawn own entry follows the accepted idempotency contract. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-P26: No cascade loss of EverPurchased, saved-source evidence or another users entry.; UAT-EL-P26-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-P26-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-PERSONAL-STATE-WRITE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-PRIVATE -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-UI-01 — DialogDismiss

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-MATCH, R-RESULTS, R-COMPARE, R-CART, R-COLLECTION, R-COLLECTION-ITEM, R-DASHBOARD, R-SYSTEM, R-SOURCES, R-REVIEWS, R-RIGHTS-MEDIA, R-OPERATIONS, R-SETTINGS, R-SIGNIN. Requirement trace: R09, R11, R21.

| Field | Contract |
|---|---|
| Element ID | EL-UI-01 |
| Page/Component | DialogDismiss |
| Element Type | cancel/close control |
| User Intent | Dismiss an unsent local form without claiming a transmitted write was rolled back |
| Triggered Event | activate |
| Proposed Handler | H-EL-UI-01 / proposed.ui.handle_el_ui_01 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Own unsaved draft, focus-return target and view/request generation. |
| Validation | Discard local draft only. If a write was transmitted, outcome remains Unknown until an authorized read or accepted same-key replay resolves it; no implicit retry/new key. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Idle/Ready prior permitted view with focus restored. |
| Empty State | No draft is a local no-op. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-UI-01: Modal close does not cancel a committed write, authorize another action or erase history.; UAT-EL-UI-01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-UI-01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-D19 — FutureResearchAssistance

Routes: R-DETAIL. Requirement trace: R12, R19.

| Field | Contract |
|---|---|
| Element ID | EL-D19 |
| Page/Component | FutureResearchAssistance |
| Element Type | disabled disclosure |
| User Intent | Retain the future evidence-backed research-assistance product intent without adding an AI service |
| Triggered Event | inspect |
| Proposed Handler | H-EL-D19 / proposed.ui.handle_el_d19 |
| Application Use Case | UI-LOCAL-STATE-1 |
| Required Input | Static future-capability description only; no perfume/private text submitted externally. |
| Validation | R12/R19 require a separate exact provider/source/privacy/budget contract and task. Deterministic score explanation is not an AI research implementation. |
| Authorization Gate | G-SEC-01. Local-only action grants no permission; next route/data action must pass its own gates. |
| Called Service | UI-local presentation reducer (PROPOSED, no I/O) |
| Data Source | Ephemeral local UI state or an already authorized DTO only; no new lookup, write or authority. |
| Output DTO | LocalViewState.v1 |
| Success State | Ready accessible explanation of a deferred capability. |
| Empty State | No assistant capability remains Unavailable, not fabricated advice. |
| Unavailable State | Future P5 research assistance has no selected provider, interface or implementation approval. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-D19: No LLM call, embeddings, paid API, account extraction or real-ranking dependency.; UAT-EL-D19-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-D19-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; BLOCKED: Future P5 research assistance has no selected provider, interface or implementation approval. |
| Input schema | LocalViewState.v1 |
| Propagation | Browser event -> local presentation state; route guard and declared service boundary apply only if a later data action is dispatched |
| Test execution | NOT RUN |

### EL-MEDIA-01 — OriginalMediaView

Routes: R-CATALOGUE, R-DETAIL, R-PYRAMID, R-RESULTS, R-COMPARE, R-RIGHTS-MEDIA. Requirement trace: R13, R21.

| Field | Contract |
|---|---|
| Element ID | EL-MEDIA-01 |
| Page/Component | OriginalMediaView |
| Element Type | image/authorized preview |
| User Intent | Request a permitted original bottle photo or note illustration |
| Triggered Event | authorized load |
| Proposed Handler | H-EL-MEDIA-01 / proposed.ui.handle_el_media_01 |
| Application Use Case | IF-MEDIA-DELIVER-1 |
| Required Input | Scoped asset ID/use and verified caller; browser supplies no file path, db/user or loader. |
| Validation | Authorize before bytes; exact rights/subject/hash/source ancestry and current PNG-only validator; recheck before response. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MEDIA |
| Data Source | Scoped image_assets/asset_permissions/rights_assessments and approved original-byte loader; path/db/login/callback are server-owned. |
| Output DTO | IF-MEDIA-DELIVER-1.output.v1 |
| Success State | Ready original image with permitted attribution and meaningful alt. |
| Empty State | No approved asset => semantic placeholder, not an empty licensed image. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-MEDIA-01: Private asset guessing/revocation/unsupported PNG return safe placeholder; no JPEG/WebP/AVIF conversion.; UAT-EL-MEDIA-01-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-MEDIA-01-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-MEDIA-DELIVER-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MEDIA -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

### EL-MEDIA-02 — MediaRetry

Routes: R-DETAIL, R-PYRAMID, R-RESULTS, R-COMPARE. Requirement trace: R13, R21.

| Field | Contract |
|---|---|
| Element ID | EL-MEDIA-02 |
| Page/Component | MediaRetry |
| Element Type | button |
| User Intent | Retry permitted image access after a recoverable error |
| Triggered Event | activate |
| Proposed Handler | H-EL-MEDIA-02 / proposed.ui.handle_el_media_02 |
| Application Use Case | IF-MEDIA-RESOLVE-1 |
| Required Input | Same authorized asset/use with fresh context/resource policy. |
| Validation | Reauthorize every retry; no background remote fetch, grant inference or decoder bypass. |
| Authorization Gate | G-SEC-01 -> G-SEC-02 -> G-SEC-03 -> G-SEC-04 -> G-SEC-07 -> G-SEC-08. Verified context is server-derived; never trust a browser UUID/owner or authorize after counting. |
| Called Service | C-APP-MEDIA |
| Data Source | Scoped image_assets/asset_permissions/rights_assessments and approved original-byte loader; path/db/login/callback are server-owned. |
| Output DTO | IF-MEDIA-RESOLVE-1.output.v1 |
| Success State | Ready metadata/placeholder/allowed original. |
| Empty State | Unknown original rights remain Unavailable. |
| Unavailable State | Unavailable when the operation, principal, selected fields, rights, resource policy or required capability is absent. All application interfaces are unimplemented today. |
| Error State | Safe Validation Error/Timeout/Offline as appropriate. Missing, unauthorized and concealed revoked/held private objects share a uniform unavailable envelope; no SQL, paths, private IDs/counts or existence hints. |
| Test Requirements | UAT-EL-MEDIA-02: No unboundedretry or guessed paths; newly revoked rights stay denied.; UAT-EL-MEDIA-02-A11Y: native name/role, keyboard/focus order, status/error announcements and no color-only meaning.; UAT-EL-MEDIA-02-PRIVACY: no unauthorized prefetch, stale-generation publication, private cache or raw-value logging. |
| Implementation Status | PROPOSED; No UI handler, application service or route implemented. |
| Input schema | IF-MEDIA-RESOLVE-1.input.v1 |
| Propagation | Browser event -> strict proposed DTO/session boundary -> genuine principal lease -> scoped object/field/rights gates -> C-APP-MEDIA -> accepted repository/domain port -> safe DTO -> presentation state |
| Test execution | NOT RUN |

## Coverage and boundaries

The matrix retains global navigation/search, independent origin/position/usage/price filters, cards/detail tabs/pyramid/chips, method/reference/strict B1 clauses/layers/blocked alternative and B2 controls, submit/reset/cancel, results/explanations/comparison, original-media/attribution/placeholders, personal states/buying links/manual orders/purchases/bottles, dashboard and private review/operations/settings. R09 private screenshot/URL intake remains metadata-request-only; R20 manual missing-perfume proposals are private and unselected. R12/R19 future AI assistance/intake intent is retained separately, with no model/provider/API/dependency or paid service introduced. R31 spending analytics remains deferred. None of these future controls calls an online shop, checkout, payment, Shopee cart synchronization, arbitrary external fetch, operator shell or database role command.

See [[State_and_Error_Contracts]], [[Authorization_and_Trust_Boundaries]], [[Cache_Offline_and_Privacy_Policy]] and [[Architecture_Owner_Review_Packet]].
