---
id: IMP-WEB-02-S7-SUMMARY
project: DoomParfum By TK
type: session_summary
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, routing, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S7 summary

PUBLIC_SAFE. Every 404 of the candidate (unknown paths and slugs in both languages, `/en`, `/TH`, `/fr`, malformed addresses) has the right status and security headers, but the server sends an empty framework error document without `lang`; the localized view appears only after JavaScript runs, and the page is blank without it. That misses DPT-PLAN-013's "server `lang` on first byte" and V01's "404 in the right language", and regresses V1's unknown-path 404. Cause: `notFound()` inside a page cannot render on the server with two root layouts.

No correction exists inside the approved design: the safe-looking changes either lose the 404 status or change nothing. A tested option (in a scratch copy, not applied) fixes every case: the experimental `globalNotFound` flag with a global 404 page in the path's language, plus proxy rewrites for malformed addresses and unknown slugs. It needs the Owner's approval. No code changed; the candidate stays `253bf48` and the preview `dedbba40…`. Full report: [[2026-11-28_IMP-WEB-02_S7_Report]].
