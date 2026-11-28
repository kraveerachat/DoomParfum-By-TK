---
id: IMP-WEB-02-S5-REPORT
project: DoomParfum By TK
type: execution_report
status: final
owner: human-owner
updated: 2026-11-28
tags: [doomparfum, frontend, docker, verification, public-safe]
source_of_truth: "../../../../DEVELOPMENT_WORKFLOW.md"
---

# IMP-WEB-02 S5 — A11 Docker drills and acceptance reconciliation

PUBLIC_SAFE. Agent: Claude Code. Intake class A (continuation of [[IMP-WEB-02_Frontend_V1_1]], same branch, no PR). Owner instruction "IMP-WEB-02 — Final Acceptance Closure" (2026-11-28 local time): authorizes the A11 Docker development and recovery drills, including temporary stopping and replacement of the preview; keeps T1–T8, names and Thai drafts; accepts the navy-folio colour use if it meets the contrast and token contracts; keeps A05 PARTIAL and the Notes screenshot check pending; no publication.

Verified at start: HEAD `9f78099` (S4 records) on code `c3f9688`, worktree clean except the Owner's untracked `CP4.zip`, branch not on the remote, remote `main` = `3e87027`, preview `48748b9c…` healthy, four unrelated containers stopped, 32 volumes, 11 `doomparfum-web` tags.

No application code changed in S5. `web/` was compared with `c3f9688` after every drill that touched the bind-mounted worktree, and was identical each time.

## A11 results

Criterion (acceptance map, rerun unchanged under DPT-PLAN-013 §10): separate dev config, HMR on a source change, port conflict, failed build, stop/restart modes; same fixed URL, one mode at a time, isolated dependency volumes, conflicts stop safely, preview policy not weakened, explicit teardown leaves no task container. Drills ran 18:09–18:21 UTC on 2026-11-27, each from `web/` with the documented commands.

| Drill | Result | Evidence |
|---|---|---|
| D1 failed preview build while the preview serves | PASS | Untracked file with a type error; `compose up --build --force-recreate` stopped at TS2322 (exit 1). Preview container ID, start time and image unchanged, healthy, 200; `preview` tag still `48748b9c`. File removed |
| D2 dev while the preview runs | PASS | Exit 1, container-name conflict; preview unchanged; no dev container created |
| D3 port conflict | PASS | Preview down; a host process held 127.0.0.1:3000; dev start failed with "ports are not available" (exit 1), nothing running, host process unaffected. The one `Created` container was removed by the explicit `down` |
| D4 dev mode and hot reload | PASS | 200 after 7 s; loopback only, `cap_drop: ALL`, `no-new-privileges`, worktree bind mount plus `doomparfum-web-dev_dev-node-modules` and `_dev-next` only (the preview has no mounts); Next 16.4.6 in the dev volume (lockfile unchanged since the volume was created). A component edit appeared in 817 ms and its revert in 485 ms, in the same document with no navigation; file restored byte for byte |
| D5 failed build recovery in dev | PASS | Syntax error: 500 with the error; after the fix 200 again in 1.3 s; the container was not restarted |
| D6 preview while dev runs; dev stop/start; teardown | PASS | Preview refused (exit 1), dev unchanged; stop freed the port; start served 200 on the same image without a rebuild; `down` left no `doomparfum-web` container; the two dev volumes kept by design |
| D7 restore and cold restart of the preview | PASS | `compose up --no-build --force-recreate`, then `stop` and `start`: image `48748b9c…`, healthy; user `node`, read-only root, all capabilities dropped, `no-new-privileges`, pids 128, 512 MiB, tmpfs `/tmp`, 127.0.0.1:3000 only, no mounts; ten routes 200; full Chrome suite on the restored preview 283 passed, 0 failed, 0 skipped, 0 flaky |
| D8 protected resources | PASS | 32 volumes before and after with identical names; the four unrelated containers stayed stopped; image tags unchanged except `dev`, rebuilt by the documented dev command (`ff8d725a`), with the previous `dev` kept as `dev-pre-a11` (`b86fc521`); no dangling image; no prune |

**A11: PASS.**

Observations (recorded, not changed):
- Hot reload works at the documented dev URL `http://localhost:3000` (README). At `http://127.0.0.1:3000` the dev server logs "Blocked cross-origin request to Next.js dev resource /_next/hmr from 127.0.0.1" (Next.js `allowedDevOrigins` default) and the dev CSP allows `ws://localhost:3000` only, so pages there do not hot-update. The preview is unaffected.
- Editing the shared dictionary `src/i18n/messages.ts` reloads the whole document (1.4 s; revert 1.8 s); component edits hot-swap in place.
- Test-setup error: the first two hot-reload attempts used `127.0.0.1` and timed out on the revert. The log's first explanation (same-second modification time) was wrong; a diagnostic showed the server recompiling each change in about 0.4 s while the browser's socket was refused. The corrected drill is the one reported above.

Evidence: [A11 results](../../Test_Evidence/IMP-WEB-02/S5/IMP-WEB-02_S5_A11_Results.json), [drill log](../../Test_Evidence/IMP-WEB-02/S5/IMP-WEB-02_S5_A11_Drill_Log.txt).

## Navy folio colour (R1-N3)

`.folio-list` rules use `color-mix(in srgb, var(--color-gold-on-navy) 40%, var(--color-navy))`, about `#5C5A51`, 1px, on navy only. Computed against navy `#14253D`: about 2.2:1. They are decorative separators between list rows: not text, not a control boundary and not a state indicator, so V10's 4.5:1 and 3:1 thresholds do not apply. They use only `gold-on-navy` and `navy`, on navy, matching §3.1 ("rules on navy only") and R5. Under the Owner's condition this is **compliant and retained**; no change.

## Acceptance state on `c3f9688`

| ID | State |
|---|---|
| A01–A04, A06–A09, A12, V01–V16 | PASS (automated suites, S4 and the restored preview in S5) |
| A10 | PASS except the second-machine LAN probe, NOT RUN |
| A11 | **PASS (S5)** |
| A05 | **PARTIAL.** Screen reader, physical phone (portrait and landscape virtual keyboard), Safari and Firefox NOT RUN. Waiting for the Owner's stage-specific deferral |
| Notes outline (Owner item 11) | Automated paths PASS; the Owner's physical check (click Notes, Win+Shift+S, Escape) PENDING |
| Thai translation | 192 lines `draft`; the Owner's line review PENDING; family and accord labels stay Latin until the Owner decides |
| Independent review | S4: CONDITIONAL on `689b177`, resolved; deltas `bfb7210` and `c3f9688` PASS. Same-vendor only |

No WCAG conformance claim.

## Preview and resources

`http://127.0.0.1:3000/` runs `sha256:48748b9cc0ffb413d270a2cd75a5fcefac0a9b92796bafa67250c6d12f2e33cf`, healthy. Rollback tags unchanged: `s3-candidate2` (`a324a06d`), `s4-candidate` (`b776d5c1`), `cp5-s2-rollback`, `cp5-candidate1`, `cp4-rollback`, `s3-candidate`, `s2-rollback`, `v1-rollback`. PR #8, U01/r14, database, matching and ETL untouched.

## Result

A11 PASS; the reviewed candidate `c3f9688` and its image are unchanged. **ACCEPTANCE PENDING** on Owner items only: A05 deferral, the physical Notes check, Thai line review (and the family/accord label choice), the Owner's review of the site, and publication authority. No receipt. `LOCAL_ONLY` / `NOT_PUSHED` / `PR_NOT_CREATED`. Package: [[IMP-WEB-02_Draft_PR_Package]].
