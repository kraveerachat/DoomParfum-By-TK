---
id: IMP-WEB-02-S5-SUMMARY
project: DoomParfum By TK
type: session_summary
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, docker, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S5 summary

PUBLIC_SAFE. With the Owner's authorization the A11 Docker drills ran on the reviewed candidate `c3f9688`: a failed preview build kept the old preview serving; dev and preview refused to start while the other ran; a taken port stopped dev safely; dev mode hot-reloaded a component in 0.8 s without a reload and recovered from a syntax error without a restart; stop, start and teardown left no task container. **A11 PASS.** Hot reload works at the documented `http://localhost:3000`, not at `127.0.0.1` (Next.js dev origin rule); recorded.

The preview was restored without a rebuild: `sha256:48748b9c…` at http://127.0.0.1:3000/, healthy, same hardening, Chrome suite 283 passed. Volumes, unrelated containers and rollback images unchanged; the rebuilt dev image's predecessor is kept as `dev-pre-a11`. The navy-folio rule colour was checked and meets the contracts (decoration only, approved tokens on navy).

Open, all with the Owner: A05 deferral, the physical Notes check, Thai line review, publication authority. Not pushed; no receipt. Full report: [[2026-11-28_IMP-WEB-02_S5_Report]].
