---
id: DPT-ARCH-RESEARCH-UX
project: DoomParfum By TK
type: technical_research_record
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, research, accessibility, nextjs, c4]
source_of_truth: "../../README.md"
---

# Official technical research — UX, UI boundaries and C4

Research supports the proposed [[Unified_Information_Architecture]], [[State_and_Error_Contracts]] and [[System_Architecture_Refinement]]. It does not select Next.js, React, an authentication provider, ORM, port, Docker image or deployment platform. Documentation retrieval is evidence of source guidance only; no framework/package is installed or tested here. Existing Python domain functions stay independent of UI/HTTP and cannot be treated as browser services merely because a page needs an answer.

Official documentation was opened using the existing `mcp__codex_apps__search_service_web_run` connector. Completed retrieval-batch recording checkpoint: **2026-11-16 13:31:05 UTC**; the common timestamp records the completed batch, not an invented per-page request or publication time. No paid Firecrawl, installation, account flow, image download or perfume-source acquisition occurred. Source facts, project inferences and limits are separated below. The ignored research scratch record is `.local/post28-architecture/ux/RESEARCH.json`; the table below is the durable review record.

## Source record and implications

### S-UX-01 — Web Content Accessibility Guidelines (WCAG) 2.2

- **URL:** [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/2024/REC-WCAG22-20241212/)
- **Observed document version:** WCAG 2.2; Recommendation 2024-12-12
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** Normative accessibility criteria cover keyboard operation, text alternatives, focus, errors and status semantics; they are technology independent.
- **Project inference (PROPOSED):** Propose WCAG 2.2 AA acceptance for future pages; document concrete keyboard, screen-reader and responsive checks.
- **Limits:** This research is not a conformance audit; the future UI does not exist.

### S-UX-02 — Read Me First — ARIA Authoring Practices Guide

- **URL:** [Read Me First — ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)
- **Observed document version:** LIVING; APG guidance for ARIA 1.2, no immutable page release observed
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** ARIA roles do not supply native keyboard behavior. Examples require browser and assistive-technology interoperability testing.
- **Project inference (PROPOSED):** Prefer native HTML controls and labels; explicitly test custom tabs, comboboxes and chip controls.
- **Limits:** Informative widget guidance does not prove cross-browser support or WCAG conformance.

### S-UX-03 — Tabs Pattern — APG

- **URL:** [Tabs Pattern — APG](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)
- **Observed document version:** LIVING; no immutable page release observed
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** The pattern defines tab/panel relationships, selected state and arrow-key navigation; automatic activation assumes panels appear without noticeable latency.
- **Project inference (PROPOSED):** Use manual activation for remote protected panels; focus movement must not demand private prefetch.
- **Limits:** A widget pattern is not application authorization or an implemented control.

### S-UX-04 — Combobox Pattern — APG

- **URL:** [Combobox Pattern — APG](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
- **Observed document version:** LIVING; no immutable page release observed
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** The pattern specifies labeled input/popup semantics, option navigation, Enter selection, Escape dismissal and standard text-editing behavior.
- **Project inference (PROPOSED):** Reference and vocabulary pickers must preserve editing/focus while selecting explicit authorized identities.
- **Limits:** Authorization, exact domain validation and suggestion-query bounds remain project requirements.

### S-UX-05 — Understanding SC 4.1.3: Status Messages

- **URL:** [Understanding SC 4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- **Observed document version:** WCAG 2.2 Understanding; LIVING informative page
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** Status messages can be programmatically exposed without focus; concise search completion/count messages differ from the entire result list.
- **Project inference (PROPOSED):** Announce loading/completion summaries without moving focus or repeatedly reading result cards.
- **Limits:** Live announcements must themselves avoid unauthorized counts or private hidden details.

### S-UX-06 — Understanding SC 2.4.7: Focus Visible

- **URL:** [Understanding SC 2.4.7: Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)
- **Observed document version:** WCAG 2.2 Understanding; LIVING informative page
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** Keyboard-operable interfaces need a visible focus indicator; it must remain visible while keyboard focus is shown.
- **Project inference (PROPOSED):** Retain visible focus across local results, dialogs and tab/combobox interaction.
- **Limits:** Actual styling, contrast and browser behavior need later testing.

### S-UX-07 — Understanding SC 2.4.11: Focus Not Obscured (Minimum)

- **URL:** [Understanding SC 2.4.11: Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)
- **Observed document version:** WCAG 2.2 Understanding; LIVING informative page
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** Author-created content must not entirely hide a component when it receives keyboard focus.
- **Project inference (PROPOSED):** Test sticky navigation, notices and dialogs against focus visibility on narrow layouts.
- **Limits:** AA minimum partial visibility differs from the stronger AAA enhanced criterion.

### S-UX-08 — Understanding SC 3.3.1: Error Identification

- **URL:** [Understanding SC 3.3.1: Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)
- **Observed document version:** WCAG 2.2 Understanding; LIVING informative page
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** Detected input errors identify the affected item and describe the error in text; no single error-layout arrangement is mandated.
- **Project inference (PROPOSED):** Use linked error summary and field descriptions after explicit failed submit; preserve safe inputs.
- **Limits:** Summary focus behavior is a project choice; native validation and security still need independent tests.

### S-UX-09 — Server and Client Components — Next.js App Router

- **URL:** [Server and Client Components — Next.js App Router](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- **Observed document version:** LIVING; observed documentation selector Latest v16.4.6; installed project version NOT VERIFIED
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** App Router defaults pages/layouts to Server Components. Interactive handlers use Client Components; payloads include client props and navigation can prefetch/cache.
- **Project inference (PROPOSED):** If selected later, keep interactive drafts separate from authorized server projections; review serialized props, streaming, prefetch and caches.
- **Limits:** Reading documentation selects no framework or version and proves no private-cache behavior.

### S-UX-10 — How to implement authentication — Next.js

- **URL:** [How to implement authentication — Next.js](https://nextjs.org/docs/app/guides/authentication)
- **Observed document version:** LIVING; observed documentation selector Latest v16.4.6; installed project version NOT VERIFIED
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** The guide separates authentication, sessions and authorization; recommends authorization near data in a DAL and limited DTOs, beyond optimistic route checks.
- **Project inference (PROPOSED):** A hidden route or UI component is insufficient; enforce session/object/field rights at service/data access and preserve genuine PostgreSQL identity.
- **Limits:** Guide examples do not solve this repository's nonadmin session binding, RLS, pool reuse or revocation contracts.

### S-UX-11 — Container — C4 model

- **URL:** [Container — C4 model](https://c4model.com/abstractions/container)
- **Observed document version:** LIVING; no versioned specification observed
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** A C4 container is an application or data store runtime boundary; Docker and physical deployment are separate concerns.
- **Project inference (PROPOSED):** Label future UI/service, existing CLI runtime, PostgreSQL and asset store by responsibility without choosing Docker images.
- **Limits:** Conceptual container separation is not proof of network, process or permission isolation.

### S-UX-12 — Container diagram — C4 model

- **URL:** [Container diagram — C4 model](https://c4model.com/diagrams/container)
- **Observed document version:** LIVING; no versioned specification observed
- **Retrieved:** `2026-11-16T13:31:05Z`
- **Source finding:** Container diagrams describe system-level responsibility distribution and communication; deployment topology is better documented separately.
- **Project inference (PROPOSED):** Keep the proposed container view distinct from implementation/deployment evidence and component-level dependencies.
- **Limits:** A diagram is not a deployed service, security test or framework decision.

## Architecture consequences and alternatives

These are project inferences, not new vendor claims or accepted Owner choices.

| Design question | Proposed direction | Alternative and constraint |
|---|---|---|
| UI/framework choice | Keep the logical IA/event/DTO/state contracts framework independent; consider interactive islands only after stack ADR. | Server-rendered templates or another frontend can implement the same contracts. Next.js documentation is a comparison input, not selection authority. |
| Server/client boundary | Treat any serialized props, streamed markup, prefetched route response or hidden panel as a possible data disclosure. Return minimal authorized DTOs. | A thin browser frontend with a separate Python service may reduce scoring duplication, but adds transport/session/CORS/CSRF/operation concerns that need their own accepted contracts. |
| Local UI state | Keep private query drafts/results transient; explicit submit/cancel; ignore stale response and clear best effort on logout/revocation. | Persistent offline results or shared result links require separate rights, cache-key, revocation, retention and security review; not enabled here. |
| Widget complexity | Native controls/semantic HTML first; custom tabs and searchable comboboxes only where product interaction needs them. | Rich custom widgets increase keyboard, focus and assistive-technology testing cost; role attributes alone supply no interaction implementation. |
| Private review | Separate permissioned review DTOs/forms from owner-only shopping and operator CLI/admin sessions. | Browser-driven operator execution adds an unnecessary trust bridge and is excluded. Current CLI-only operation remains available within its historical authorization. |
| C4 views | Distinguish system context, runtime/data-store container view, component/dependency view and dynamic sequences. | A Docker-compose diagram alone cannot substitute for responsibilities, authorization/data boundaries or a separately reviewed deployment topology. |

The smallest safe proposed UI slice is an authenticated read-only catalogue/detail projection after genuine nonadmin principal and selected-field/rights contracts are approved and tested. A shell without those dependencies can demonstrate accessibility only with explicitly labeled synthetic layout fixtures in a later approved task; it cannot display the real private catalogue or call exact synthetic scorers with relabeled real records.

## Acceptance and evidence limits

Page/state acceptance IDs are predictable `UAT-<route>-NN`, `UAT-STATE-*`, `UAT-EVENT-*`, `UAT-A11Y-*` and `UAT-JOURNEY-*` design identifiers, not runnable tests or completed implementation evidence. All such feature/browser/security tests are **NOT RUN**. Document/JSON consistency validation is separate from them. No live database count, current role/rights test, API response, timing-equivalence test, PWA/offline behavior or assistive-technology run is claimed by this research.

Review the current [[Architecture_Owner_Review_Packet]] together with [[Function_Interface_and_DTO_Contracts]] and [[UI_Element_Function_Matrix]]. POST27-ODP-1 stays unchanged at SHA-256 `0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c`; exact A/B/I acceptance is unrecorded and IMP-ENR-01 is not started. M1/B1 remain synthetic-only, 44 holds/43 normalization proposals/Khamrah conflict are preserved and PR8 remains blocked. Research does not grant data acquisition, application implementation, normalization, eligibility, media or Production approval.
