---
id: DPT-HANDOFF-002
project: DoomParfum By TK
type: handoff
status: research
updated: 2026-11-11
timezone: Asia/Bangkok
tags: [doomparfum, dpt-plan-002, planning]
---

# DPT-PLAN-002 — Research and Planning Handoff

- Identity: DoomParfum By TK, 2026-11-11 Asia/Bangkok. Research scope defined by owner handoff DPT-PLAN-002, not an accepted ADR.
- Git truth: public repo https://github.com/kraveerachat/DoomParfum-By-TK; `main` `bffb2fab1918dc5221a6c5da7920168bcae263ca`; PR #1 MERGED; PR #2 https://github.com/kraveerachat/DoomParfum-By-TK/pull/2 OPEN/DRAFT/unmerged at preflight. This branch `plan/p2-focused-brand-discovery-automation` is docs-only.
- Source research: 220 seed candidate names; 15 first-party brand/publisher presences observed; zero new permissions to harvest/content/asset storage; first-party URL does not equal data licence. Research CSV/workbook generated separately, kept out of public repository initially.
- Status: proposed architecture and source/score policy. Existing Scento OD-01 limited local CC BY 4.0 pilot remains a separate implementation dependency.
- Decisions: brand scope and identity, source permission matrix, scoring/cohort coverage, production/availability, one-click auto-promotion and storage choices all require Human Owner review.
- Safety: No scraper, bulk import, images, SQL, runtime, PR #2 modification, cloud provisioning, secrets or production mutations. No merge. This handoff does not assert database tests or live API runtime checks.
- Next: human review of Draft Planning PR; resolve owner decisions, source rights and candidate identity gaps; merge Gate P only by Human Owner, then new implementation from latest merged main and required P1 dependencies.
