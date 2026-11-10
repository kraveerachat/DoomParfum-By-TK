---
id: DPT-PLAN-001
project: DoomParfum By TK
type: task
status: in-progress
owner: project
updated: 2026-11-10
tags: [doomparfum, planning, data]
source_of_truth: "../../../README.md"
---

# DPT-PLAN-001 — P1 Data Discovery & Database Foundation

## Current task

- Agent: Codex, planning/research/documentation only.
- State: IN PROGRESS; session S1, 2026-11-10 Asia/Bangkok.
- Branch: `plan/p1-data-discovery-schema-foundation`, target `main`.
- START_SHA / origin/main: `03481f7066487c44631cb9065899894ee8db71fb`.
- Planning PR: not created yet. Approved planning PR: none; implementation forbidden.
- Production mutation: NO. Human review and merge required.

## Plan and expected evidence

1. Read repository, requirements, existing data/engineering/delivery/operations notes.
2. Verify source licenses; profile a bounded licensed snapshot and regional source coverage.
3. Record field mapping, conflicts, unknowns, proposed ERD/dictionary and hosting alternatives.
4. Specify a future local pilot, validation, size benchmark and separate DB/object restore tests.
5. Synchronize Obsidian; validate docs-only diff, links, frontmatter and Git state.
6. Commit/push this branch and create one Draft Planning PR; stop for owner review.

## Safety / do-not-touch

No runtime source, migrations, database creation, deployment, paid tools, authentication changes,
raw third-party dataset commits, Fragrantica automation/internal APIs, merge or auto-merge.
Keep personal cart, manual purchases and physical inventory distinct. No invented product facts.

## Tool decision and initial findings

GitHub MCP is available and reports repository push permission. Local `gh auth status` fails
with an invalid existing token; no reauthentication performed. Initial sandbox Git network
failed, authorized clone succeeded with scoped escalation. `.git` writes require escalation.
Apify MCP is not exposed in this runtime; no actor executed. PlanetScale skills are not installed
and are optional; no installer executed. Built-in web research and PostgreSQL primary docs are
the fallback. No external tools/configuration installed.

## Session register

| Session | Scope | State | Evidence |
|---|---|---|---|
| S1 | P1 documentation and research | IN PROGRESS | Clean cloned baseline; HEAD = origin/main; no existing PRs returned by GitHub search |

## Next action

Complete read-only profiling and documentation. This note will record actual outcomes before handoff.


## Session S1 findings and planning review readiness

Research/drafting complete; agent review of the documents found no unresolved document-link or entity-name
mismatch. Source/hosting decisions remain open and require owner review. No independent runtime review
is claimed. Planning publication/receipt checkpoint is the remaining session closeout work.

- Reviewed all six original 03_Data notes, architecture/ADRs, roadmap/backlog/acceptance, decisions/logs,
  relevant domain/matching/requirements notes, root/vault READMEs and entire workflow/AGENTS policy.
- At START_SHA: prior merged plan, task note, Planning_PRs directory, Receipts and Handoffs: NOT FOUND.
  GitHub search and direct PR collection both returned no PRs; remote main was rechecked unchanged.
- Actual source results: [[P1_Data_Profiling_Findings]] (hashes, counts, selected real examples and limits).
- Proposed schema: 44 logical tables, three ERD views; keys/FKs/type/tenant guards/nullable unknowns.
- Proposed storage/recovery: [[P1_Storage_Hosting_and_Recovery]]. No actual capacity benchmark.
- Future implementation: IMP-P1-01..05 in [[P1_Pilot_Implementation_Plan]], all NOT STARTED.
- Open decisions: OD-01..06 in [[P1_Data_Foundation_Plan]]; no right is inferred from a generic merge.

## Test / evidence ledger

| Check | Actual result | Limit |
|---|---|---|
| `git status --short --branch`, `git rev-parse HEAD origin/main` | Clean starting checkout; both 03481f7066487c44631cb9065899894ee8db71fb; dedicated branch created | No main mutation |
| GitHub repository metadata / branches/main / pulls GET | Push permission; main unchanged; no prior PRs | No settings changed |
| Inline Python read-only source profile | 1,479/160/420 rows; no duplicate IDs or missing house references; one same-name EDP/EDT group | One snapshot; no full semantic/material alias audit |
| Inline Python + PyYAML document check | Parsed changed frontmatter, resolved wiki/local links, balanced fences; 44 ERD/dictionary names match | No Mermaid rendering or SQL execution |
| `git diff --check` | Exit 0 at document checkpoint | Final staged/commit checks repeated before publication |
| App build, DB migrations, ETL tests, benchmark, restore | NOT RUN | Planning scope only |

Meaningful initial environmental failures: sandbox Git network; read-only .git branch write; invalid
existing gh token; sandbox/host temp mismatch; web API request/Lattafa terms access. Safe fallbacks and
outcomes are recorded in [[Agent_Run_Log]]. No tooling/account/configuration installation/change.

## Exact documentation change manifest

- `README.md`
- `Structure DB Obsidian/00_Home/Project_Status.md`
- `Structure DB Obsidian/02_Domain/Perfume_and_Note_Taxonomy.md`
- `Structure DB Obsidian/03_Data/Data_Dictionary_Draft.md`
- `Structure DB Obsidian/03_Data/Data_Quality_and_Provenance.md`
- `Structure DB Obsidian/03_Data/ERD_Draft.md`
- `Structure DB Obsidian/03_Data/Ingestion_and_ETL.md`
- `Structure DB Obsidian/03_Data/P1_Data_Conflict_Matrix.md`
- `Structure DB Obsidian/03_Data/P1_Data_Profiling_Findings.md`
- `Structure DB Obsidian/03_Data/P1_Source_to_Canonical_Mapping.md`
- `Structure DB Obsidian/03_Data/Rights_and_Attribution.md`
- `Structure DB Obsidian/03_Data/Source_Registry.md`
- `Structure DB Obsidian/04_Matching/Review_Evidence_and_Confidence.md`
- `Structure DB Obsidian/06_Engineering/P1_Storage_Hosting_and_Recovery.md`
- `Structure DB Obsidian/06_Engineering/Proposed_System_Architecture.md`
- `Structure DB Obsidian/06_Engineering/Tech_Stack_and_ADRs.md`
- `Structure DB Obsidian/07_Delivery/Acceptance_Criteria.md`
- `Structure DB Obsidian/07_Delivery/Backlog.md`
- `Structure DB Obsidian/07_Delivery/P1_Pilot_Implementation_Plan.md`
- `Structure DB Obsidian/07_Delivery/Planning_PRs/P1_Data_Foundation_Plan.md`
- `Structure DB Obsidian/07_Delivery/Roadmap.md`
- `Structure DB Obsidian/07_Delivery/Tasks/DPT-PLAN-001_P1_Data_Foundation.md`
- `Structure DB Obsidian/08_Operations/Agent_Run_Log.md`
- `Structure DB Obsidian/08_Operations/Change_Log.md`
- `Structure DB Obsidian/08_Operations/Decision_Log.md`
- `Structure DB Obsidian/README.md`


Closeout adds exactly one receipt and one handoff note to this manifest; their paths and reviewed
checkpoint are recorded in the final closeout entry. No runtime/raw-data/config files are included.
