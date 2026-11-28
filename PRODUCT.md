# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Status and authority

Documentation-only product context for DPT-PLAN-012, based on main `03e2ab6080373033c02afc7ada7be2ceab5f24e2` and the Owner's attached brief. Read AGENTS.md and DEVELOPMENT_WORKFLOW.md first. This file does not approve a stack, implementation, data display, authentication or deployment. Canonical task: [Luxury frontend planning](Structure%20DB%20Obsidian/07_Delivery/Tasks/DPT-PLAN-012_Luxury_Frontend_Editorial.md).

## Stack

The Owner requests a proposal for Next.js App Router, TypeScript, Tailwind CSS, selective shadcn/ui primitives and Docker Compose. No application exists. Exact versions and dependency setup require a merged planning scope and bounded implementation task. Existing framework-neutral Python/domain architecture remains unchanged.

## Users

The Owner is planning a personal perfume knowledge base and collection/shopping tracker. This task serves the Owner reviewing a fictional frontend before connecting any real data. No audience research or usability study has been conducted.

## Product Purpose

Help a person explore fragrance information, distinguish notes from evidence and eventually track personal interests and bottles. This slice demonstrates discovery, note navigation and readable details using clearly labelled synthetic fixtures only.

## Positioning

Product intent separates fragrance identity, note structure, similarity evidence, seller listings and personal collection records. None may be substituted for another. A note pyramid is perceived/declared olfactory information, never a chemical recipe.

## Operating Context

Proposed first host: Windows Desktop with Docker Desktop, loopback URL `http://localhost:3000`. Later Ubuntu hosting is planned, not deployed. Any public link/Cloudflare work is a separate approval. The public repository must contain only public-safe documentation and fictional fixtures.

## Capabilities and Constraints

Plan exactly five route types: Home, Explore, Perfume Detail, Notes and About. Profile is a non-authenticating placeholder. Search/filter operate only on local synthetic fixture data. No API, DB, authentication, real products, licensed brand imagery, external runtime data calls, scores, matching percentages, cart writes, service worker or persistent catalogue cache. The future Cart is a purchase-source bookmark list, not checkout. U01 security and PR #8 remain independent and unchanged.

## Brand Commitments

Name: DOOMPARFUM with BY TK signature. The Owner confirmed the attached Luxury Fragrance Editorial × Modern Fashion Boutique direction during this session: ivory/ink, muted gold, deep navy, editorial serif headings, readable sans body, generous spacing, thin rules and restrained motion. These are proposal constraints; built design authority does not yet exist.

## Evidence on Hand

Merged requirements and architecture histories exist in the vault. There is no frontend, screenshot baseline or approved product photography. Twenty external sites were inspected read-only as references, with partial views recorded. Reference access grants no asset reuse. No real perfume facts, prices, reviews or performance claims are supplied for this slice.

## Product Principles

1. Truth and source/state distinctions precede visual storytelling.
2. The shortest path from catalogue to a note or detail must work with keyboard and touch.
3. Synthetic demonstration must remain unmistakable at every entry point.
4. The mock shell must remain independent of private data, matching and security implementation.

## Accessibility & Inclusion

WCAG 2.1 AA is the requested target. Require keyboard interaction, visible focus, readable contrast, reduced motion and responsive reflow. Thai-script stress cases belong in verification; a full locale switch is not requested.

## Amendment DPT-PLAN-013 (merged 2026-11-26, PR #37 `3e87027`)

The V1 mock frontend exists on `main` (PR #36, `ab3351a8432d1d6664a6b4281784cfea56b0b9fa`); "No application exists" and "There is no frontend" above describe the planning baseline. For V1.1 the Owner asks for an English and Thai interface, which replaces "a full locale switch is not requested", and for a sticky header, a gold and bronze detail palette and page refinements. Positioning, mock-only limits, brand name and the five route types are unchanged. Contract: [Frontend V1.1 amendment](Structure%20DB%20Obsidian/07_Delivery/Planning_PRs/DPT-PLAN-013_Frontend_V1_1_Amendment.md).

The Owner merged this amendment on 2026-11-26 (PR #37, `3e87027fbdbbb016c148a84ca33775e64cccf3e0`); it is the design authority for V1.1. Its implementation is task IMP-WEB-02; until that task is merged, `main` still serves the V1 frontend.
