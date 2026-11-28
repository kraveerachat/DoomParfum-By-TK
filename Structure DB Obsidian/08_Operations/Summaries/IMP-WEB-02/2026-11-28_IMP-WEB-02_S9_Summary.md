---
id: IMP-WEB-02-S9-SUMMARY
project: DoomParfum By TK
type: session_summary
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, routing, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S9 summary

PUBLIC_SAFE. With the Owner's bounded authorization, the 404 documents are fixed with the experimental Next.js `globalNotFound` flag (pinned 16.4.6, local mock only). Every unknown address, slug, unsupported prefix and malformed address now returns a real 404 that is rendered on the server in the right language and readable without JavaScript. The locale comes from the path only. Nonce CSP, no-store, noindex and the read-only methods hold, and the ten valid routes are unchanged.

Final candidate `53d0126` (image `568cc3b3…`, restored as the preview on `127.0.0.1:3000`): unit 122/0, Chrome 305/305, Edge 305/305, output scan clean. The new tests fail on the old build. Independent review: CONDITIONAL on `3b93945`, then PASS on `53d0126`. The experimental flag must be reassessed before any framework upgrade or production deployment.

Still open: the physical Notes shortcut test (not performed) and publication authority. A05 is deferred. Not pushed; no receipt. A next-slice decision packet is prepared; no task was started. Full report: [[2026-11-28_IMP-WEB-02_S9_Report]].
