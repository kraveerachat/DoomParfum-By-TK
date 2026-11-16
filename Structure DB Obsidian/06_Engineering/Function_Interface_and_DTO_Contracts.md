---
id: DPT-PLAN-010-INTERFACES
project: DoomParfum By TK
type: architecture_contract_proposal
status: proposed
owner: human-owner
updated: 2026-11-16
tags: [doomparfum, architecture, interfaces, dto, evidence]
source_of_truth: "../../README.md"
---

# Function, interface and DTO contracts

This note separates existing source from future logical contracts. It supports [[System_Architecture_Refinement]], [[Component_and_Dependency_Registry]], [[UI_Element_Function_Matrix]], [[Architecture_Technical_Research_Python]] and [[Architecture_Owner_Review_Packet]]. All new interfaces, handlers, services, transport bindings and types below are **PROPOSED**, not implemented. No HTTP endpoint is declared.

## Source evidence and status semantics

Static inventory base: `168715bc9bc5fff968524074257dc106a8a63638`, observed branch `plan/post-pr28-architecture`. [Architecture_Source_Inventory.json](../08_Operations/Test_Evidence/Architecture_Source_Inventory.json) records every Python definition under `database/` and `matching_math/`, normalized AST signature, declared return annotation, dataclass fields, imports, source lines, canonical Git blob/SHA-256 and raw checkout SHA-256. Signatures preserve parameter order/default semantics through `ast.unparse`; source lines remain the authority for literal spelling. Unannotated returns are marked UNANNOTATED, not guessed. Generated dataclass methods are not invented as explicit source functions.

**IMPLEMENTED** means a definition/schema exists in the pinned source. **TESTED** is limited to the specifically recorded historical execution evidence. **NOT VERIFIED** marks current runtime/live DB/application behavior not executed in this task. **PROPOSED** marks the separate application registry and future typed boundaries. **BLOCKED** describes an operation whose required accepted policy, rights, principal or implementation is absent; it does not erase its proposal status.

Inventory contains26 Python files:13 runtime/operator modules and13 test/helper modules;593 AST definitions,538 public by spelling and55 internal by spelling, including nested functions and test methods;40 explicit dataclasses. These are **not538 application APIs**. Each symbol has separate `classification`, `scope` and `visibility` fields. Eight existing migrations are hashed. All26 canonical Python files are byte-identical between historical source `8eef8f13265adc14db0cae82ff77cfc4863853ce` and this base. Canonical Git hashes and raw checkout hashes are deliberately separate because checkout line endings can differ.

The unchanged [Post_PR27_Offline_Tests.json](../08_Operations/Test_Evidence/Post_PR27_Offline_Tests.json) reports194 offline methods,0 failures/errors/skips on Python3.11.9: primitives24, invariants7, research17, adapter14, M1 focused45 plus properties4, B1 focused48 plus properties8, images20 and Scento7. This is **historical suite-level evidence**, not current rerun, per-function coverage, DB/RLS/session acceptance, real matching or application acceptance. No current runtime tests, source acquisition, image tests, SQL or services were run here.

## Five required implemented bindings

### `database.matching_input.read_profile` — IMPLEMENTED

```python
read_profile(execute: Callable[[str], dict], profile_id: str) -> ProfileInput
```

Source: [matching_input.py](../../database/matching_input.py), lines270–282. Internal version: `matching-input-local-v2`. The callback must execute the entire generated READ COMMITTED READ ONLY transaction on one genuinely authenticated PostgreSQL connection, stop at the first error and return only its sole JSON object. Source enforces canonical UUID/shape/bounds, same `session_user`/`current_user`, runtime membership, rejection of owner/superuser/BYPASSRLS and bounded selected-field/provenance decoding. It distinguishes usable/incomplete/unknown/held/rights/eligibility states and keeps `ranking_allowed=False`.

The callable trusts the callback transport; it does **not** establish a DB login or independently prove a callback executed SQL. A forged callback result is not authenticated evidence. No callback, browser UUID/header/GUC/role choice, default admin executor or operator connection may substitute for a genuine principal. The future service must own the callback and session lifetime; no browser-supplied SQL/callback/identity. Callback failures become safe adapter errors; missing/hidden/malformed profile IDs share a safe unavailable response.

The internal decoded DTO bound is2MiB, each selected payload64KiB, eight fields and512 memberships with bounded lookahead. These are internal adapter bounds, **not HTTP budgets**. No approved8KiB transport parser exists. Source DTO fields/locators can contain protected evidence; future projection must allowlist what the authorized caller receives. The local adapter is not an application catalogue service or real-matching wrapper.

### `matching_math.synthetic_m1.score_synthetic_notes_layered` — IMPLEMENTED

```python
score_synthetic_notes_layered(
    reference: FixtureProfile,
    candidates: tuple[FixtureProfile, ...],
    *, vocabulary: FixtureVocabulary, config: M1Config,
) -> M1BatchResult
```

Source: [synthetic_m1.py](../../matching_math/synthetic_m1.py), lines371–397. Implements only accepted `M1-NL-TYPED-1`: pure bounded notes-layered synthetic comparison, explicit fixed config/context, exact rational fit/support/coverage, deterministic compatible partitions and approved display strings. No DB/network/UI/transport or real-source verification occurs. Caller-declared fixture lineage is not rights, completeness or eligibility evidence. Current fixed synthetic vocabulary/domain/transform/snapshot/scope values are validated; real records cannot be renamed into them.

`M1Config`, fixture vocabulary/profile/layer/lineage, layer explanations, partition keys and batch results are explicit frozen dataclasses. Unknown/incomplete/mismatched layers preserve unavailable reasons. Accepted64-candidate and512-membership fixture bounds remain their exact synthetic contract, not future real-dataset truncation policy. Ranking is exact within a partition before wire conversion/display rounding; no global rank across incompatible partitions.

### `matching_math.synthetic_b1.score_synthetic_b1` — IMPLEMENTED

```python
score_synthetic_b1(
    query: B1Query,
    candidates: tuple[B1Profile, ...],
    *, vocabulary: B1Vocabulary, config: B1Config,
) -> B1BatchResult
```

Source: [synthetic_b1.py](../../matching_math/synthetic_b1.py), lines560–593. Implements only accepted `B1-PD-TYPED-1` revision2: pure required/optional/excluded clauses, exact/any-pyramid selectors, canonical query deduplication, explicit positive-domain closure gates, Coverage4/5 plus Focus1/5, exact rational results/explanations and compatible partitions. Count/shape bounds precede member/token scans as corrected in its retained implementation evidence. It validates fixed synthetic context/config; it has no real-catalogue callback or application orchestration.

`B1Query`/`B1Clause`, profile/layer/vocabulary/config, query/context/partition keys, lineage, clause/gate/layer explanations and results remain their own typed dataclasses. Required/excluded absence requires accepted closure; unknown is not absent. Repeated occurrences and assignment follow the accepted synthetic contract, not a newly invented real normalization. Data Confidence and Direct Pairwise Evidence are separate unavailable/evidence channels, not inferred smell similarity.

### `database.image_validation.inspect_png` — IMPLEMENTED

```python
inspect_png(content: bytes, limits: Limits = Limits()) -> ImageMetadata
```

Source: [image_validation.py](../../database/image_validation.py), lines50–116. Pure technical inspection with no I/O or rights decision. Supports only bounded static non-interlaced8-bit RGB/RGBA PNG without ancillary chunks. Verifies signature, chunk structure/CRC, dimensions, pixel/decoded bounds, compressed-stream completeness, filter bytes and exact SHA-256. Rejects metadata/animation/palette/interlace/unknown chunks instead of silently stripping them. Technical success neither approves acquisition/display/derivatives nor proves a project asset binding.

Existing `Limits` defaults:5MiB bytes,4096 width/height,4,000,000 pixels,20MiB decoded bytes and1024 chunks; all supplied limits must be positive exact integers. These are the existing validator defaults, not new transport policy. `ImageMetadata` contains MIME, size, dimensions and hash. Rejection stays `ImageRejected`; no private locator should reach user errors.

### `database.image_validation.validate_registered_asset` — IMPLEMENTED

```python
validate_registered_asset(
    asset_id: str, read_content: Callable[[], bytes], *,
    operation: str, db: str, user: str,
    limits: Limits = Limits(),
) -> ImageMetadata
```

Source: [image_validation.py](../../database/image_validation.py), lines145–176. Local registered-asset validation first obtains an authorized exact-use registered snapshot, then invokes a **trusted bounded local owned-object** callback, inspects PNG, compares registered metadata/hash and rereads current authorization plus full relevant binding. Changed/missing/denied/expired/revoked bindings fail closed. Later use must authorize again; metadata is not a grant/token.

The callback must not be HTTP/downloader/arbitrary path or an unbounded reader. This existing module uses local operator SQL tooling and explicit local `db`/`user` arguments; it is not an application identity boundary or HTTP asset service. Normal application handlers must never expose its operator login choice or `local.sql` as a browser capability. A separately reviewed infrastructure adapter/principal design is required; dynamic imports/CLI execution are not an approved bridge.

## Existing layers, types and database responsibilities

The exact inventory below includes operator and offline utilities because source presence alone does not make a function safe for normal application calls. Migrations001–008 own SQL identity, canonical/provenance/private/media integrity and RLS. They are not newly generated application migrations. SQL remains authoritative for genuine `session_user` identity, immutable subjects/scope owners, selected source rights and asset-use lineage. Application authorization/error masking/pooling remain separate work.

| Existing source | Responsibility and boundary |
|---|---|
| `database/local.py` | Guarded Docker/local PostgreSQL admin lifecycle, migration/recreate helpers and SQL execution. Operator-only; never expose through browser. |
| `database/scento_etl.py` | Pinned licensed-source parsing, deterministic import/mapping/provenance SQL and guarded local import. Trusted operator ETL; no new execution/acquisition here. |
| `database/research_audit.py` | Offline metadata crosswalk, held proposals, asset/pair queues and evidence output; proposals do not promote canonical data. |
| `database/matching_input.py` | Read-only trusted callback SQL/DTO adapter with selected facts/provenance, source rights and uniform errors. No application login, real scorer or public serializer. |
| `database/image_validation.py` | Pure bounded PNG inspection plus local registered binding/rights callback workflow; no HTTP/acquisition/storage. |
| `database/performance.py` | Local benchmark preparation/workload/measurement CLI. Operator-only, not capacity acceptance for a future service. |
| `database/verify.py`, `verify_images.py`, `validate_docs.py` | Local evidence, test collection and documentation verification entry points. Not product APIs. |
| `matching_math/primitives.py` | Exact pure set/vector Jaccard, weighted mean, coverage and stable order; caller completeness/domain declarations are not rights/eligibility proof. |
| `matching_math/synthetic_m1.py`, `synthetic_b1.py` | Separately accepted fixed synthetic contracts only. |
| `matching_math/__init__.py` | Package marker/documentation; no public functions. |

| Migration | Existing responsibility |
|---|---|
| 001 | Identity, scopes/membership, registry and public vocabulary foundation. |
| 002 | Brand/perfume/packaging/note/accord identities and relationships. |
| 003 | Source rights/captures, typed claims, selections/conflicts, staging/audit. |
| 004 | Canonical joins, exact asset permissions, evidence/matching and private history. |
| 005 | Scope/claim/reviewer/materialization/immutable evidence functions and genuine `session_user` principal resolution. |
| 006 | Asset lineage/use/revocation and deferred final-state contracts. |
| 007 | RLS/grants/invoker projections and fixed field allowlist. |
| 008 | Protected transaction dirty generations and coalesced complete deferred validators. |

The local socket/admin harness and passwordless test logins do not prove an application-private TCP login exists. No new role, subject, scope owner, migration or current principal was created or inspected live. Existing operator-private records must not be impersonated by an admin connection accepting a browser user ID. Cross-user/rights state is NOT VERIFIED live in this task.

### Existing top-level public source inventory — IMPLEMENTED

Every exact field/default/return annotation, internal definition and test/helper method is in the JSON inventory. Tables below list only top-level public runtime/operator definitions. They are source entry points/types, not an application interface registry. Internal helpers remain internal even where Python permits imports; nested helper functions are not new top-level APIs.

#### `database/image_validation.py`

Canonical Git SHA-256: `d50bb159e0223e21c74d10b64176190569c9889f88726706df3ece143d54f29f`. Raw checkout SHA-256: `d50bb159e0223e21c74d10b64176190569c9889f88726706df3ece143d54f29f`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 23 | class | `ImageRejected` | `type definition` |
| 28 | dataclass | `Limits` | `type definition` |
| 42 | dataclass | `ImageMetadata` | `type definition` |
| 50 | function | `inspect_png(content: bytes, limits: Limits=Limits()) -> ImageMetadata` | `ImageMetadata` |
| 145 | function | `validate_registered_asset(asset_id: str, read_content: Callable[[], bytes], *, operation: str, db: str, user: str, limits: Limits=Limits()) -> ImageMetadata` | `ImageMetadata` |

#### `database/local.py`

Canonical Git SHA-256: `fa5ede50172fd435ec643d31b9902cf34c9d8a872e397f0adf41d27a6373c0ed`. Raw checkout SHA-256: `fa5ede50172fd435ec643d31b9902cf34c9d8a872e397f0adf41d27a6373c0ed`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 21 | function | `docker(*args: str, input: str \| None=None, check: bool=True)` | `UNANNOTATED` |
| 26 | function | `guard()` | `UNANNOTATED` |
| 43 | function | `sql(text: str, db: str='dpt_schema_test', user: str='postgres', check=True)` | `UNANNOTATED` |
| 56 | function | `assert_local_endpoint()` | `UNANNOTATED` |
| 62 | function | `start()` | `UNANNOTATED` |
| 95 | function | `recreate(db: str)` | `UNANNOTATED` |
| 102 | function | `reset_empty_foundation()` | `UNANNOTATED` |
| 115 | function | `migration_digest(file: Path)` | `UNANNOTATED` |
| 120 | function | `migrate(db: str='dpt_foundation', extra: Path \| None=None)` | `UNANNOTATED` |
| 141 | function | `main()` | `UNANNOTATED` |

#### `database/matching_input.py`

Canonical Git SHA-256: `e4b4b761e1bcaa64a1ed0c19372545d232ddf5e7626e58666d4ea76edd97ab1b`. Raw checkout SHA-256: `e4b4b761e1bcaa64a1ed0c19372545d232ddf5e7626e58666d4ea76edd97ab1b`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 23 | class | `State` | `type definition` |
| 32 | class | `InputUnavailable` | `type definition` |
| 36 | class | `AdapterUnavailable` | `type definition` |
| 41 | dataclass | `Provenance` | `type definition` |
| 62 | dataclass | `Field` | `type definition` |
| 70 | dataclass | `Note` | `type definition` |
| 77 | dataclass | `ProfileInput` | `type definition` |
| 96 | function | `canonical_id(value)` | `UNANNOTATED` |
| 108 | function | `normalized(value)` | `UNANNOTATED` |
| 122 | function | `query(profile_id)` | `UNANNOTATED` |
| 270 | function | `read_profile(execute: Callable[[str], dict], profile_id: str) -> ProfileInput` | `ProfileInput` |

#### `database/performance.py`

Canonical Git SHA-256: `409f5d24ff2fc8be20a50d79cc8a3bde972d87855eb3afeeea057dd1d4029952`. Raw checkout SHA-256: `409f5d24ff2fc8be20a50d79cc8a3bde972d87855eb3afeeea057dd1d4029952`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 18 | function | `prepare(phase)` | `UNANNOTATED` |
| 30 | function | `workload(count)` | `UNANNOTATED` |
| 37 | function | `measure(count, operation='insert')` | `UNANNOTATED` |
| 65 | function | `main()` | `UNANNOTATED` |

#### `database/research_audit.py`

Canonical Git SHA-256: `fbbf4bf3cb253547feb8e8b0a71a5ea0d41347793a858edf2130396001a9cf93`. Raw checkout SHA-256: `fbbf4bf3cb253547feb8e8b0a71a5ea0d41347793a858edf2130396001a9cf93`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 33 | function | `canonical(value)` | `UNANNOTATED` |
| 37 | function | `sha(raw)` | `UNANNOTATED` |
| 41 | function | `require_equal(actual, expected, label)` | `UNANNOTATED` |
| 46 | function | `read_csv(path)` | `UNANNOTATED` |
| 51 | function | `safe_path(path)` | `UNANNOTATED` |
| 59 | function | `brand_crosswalk(seed, additions, houses)` | `UNANNOTATED` |
| 100 | function | `proposed_membership(row, note_lookup)` | `UNANNOTATED` |
| 134 | function | `held_proposals(snapshot, plan, prior)` | `UNANNOTATED` |
| 157 | function | `false_flag(value)` | `UNANNOTATED` |
| 161 | function | `asset_audit(candidates, extras)` | `UNANNOTATED` |
| 208 | function | `pair_queue(candidates)` | `UNANNOTATED` |
| 230 | function | `enrichment_index(snapshot, plan)` | `UNANNOTATED` |
| 251 | function | `run(bundle, output)` | `UNANNOTATED` |
| 344 | function | `main()` | `UNANNOTATED` |

#### `database/scento_etl.py`

Canonical Git SHA-256: `a9a392ab6c17b01f937a313536cd002f4e0446af2370518d8084fd28f3031be0`. Raw checkout SHA-256: `a9a392ab6c17b01f937a313536cd002f4e0446af2370518d8084fd28f3031be0`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 46 | function | `canonical(value)` | `UNANNOTATED` |
| 50 | function | `digest(value)` | `UNANNOTATED` |
| 54 | function | `entity_id(kind, key)` | `UNANNOTATED` |
| 62 | function | `tokens(text)` | `UNANNOTATED` |
| 66 | function | `normalize(text)` | `UNANNOTATED` |
| 71 | function | `optional_year(text)` | `UNANNOTATED` |
| 78 | function | `load_snapshot(path)` | `UNANNOTATED` |
| 101 | function | `note_lists(row)` | `UNANNOTATED` |
| 106 | function | `classify(row, snapshot)` | `UNANNOTATED` |
| 122 | function | `build_plan(snapshot, cohort)` | `UNANNOTATED` |
| 141 | function | `mapping_proposal(plan, snapshot)` | `UNANNOTATED` |
| 152 | function | `validate_mapping(mapping, plan, snapshot)` | `UNANNOTATED` |
| 166 | function | `q(value)` | `UNANNOTATED` |
| 174 | function | `insert(table, values)` | `UNANNOTATED` |
| 180 | function | `capture_rows(snapshot, plan)` | `UNANNOTATED` |
| 193 | function | `batch_identity(snapshot, plan, mapping)` | `UNANNOTATED` |
| 198 | function | `import_sql(snapshot, plan, mapping=None, transaction=True)` | `UNANNOTATED` |
| 256 | function | `promotion_sql(snapshot, plan, rows, batch, mapping)` | `UNANNOTATED` |
| 350 | function | `prepare_database(db)` | `UNANNOTATED` |
| 357 | function | `inventory_expression()` | `UNANNOTATED` |
| 363 | function | `inventory(db)` | `UNANNOTATED` |
| 368 | function | `run_import(snapshot, cohort, db, mapping=None)` | `UNANNOTATED` |
| 391 | function | `main()` | `UNANNOTATED` |

#### `database/validate_docs.py`

Canonical Git SHA-256: `d72844ce8db0660656d5e653dbcdb60b79e823c8fe48a72f056037fd49c7f127`. Raw checkout SHA-256: `d72844ce8db0660656d5e653dbcdb60b79e823c8fe48a72f056037fd49c7f127`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 17 | function | `git(*args)` | `UNANNOTATED` |
| 21 | function | `changed_paths()` | `UNANNOTATED` |
| 27 | function | `without_fences(text)` | `UNANNOTATED` |
| 40 | function | `main()` | `UNANNOTATED` |

#### `database/verify.py`

Canonical Git SHA-256: `bdddbe68611807a88fc8c3eac4e083ad4d1a23413102a17331b4fef8256c18bc`. Raw checkout SHA-256: `bdddbe68611807a88fc8c3eac4e083ad4d1a23413102a17331b4fef8256c18bc`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 15 | function | `inventory()` | `UNANNOTATED` |
| 37 | function | `investigate_duplicates()` | `UNANNOTATED` |
| 59 | function | `main()` | `UNANNOTATED` |

#### `database/verify_images.py`

Canonical Git SHA-256: `2f433d44eb874249616aac71f2c320502a915c5db3a52b865401e17296c131b1`. Raw checkout SHA-256: `2f433d44eb874249616aac71f2c320502a915c5db3a52b865401e17296c131b1`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 36 | function | `collect(suite)` | `UNANNOTATED` |
| 44 | function | `main()` | `UNANNOTATED` |

#### `matching_math/primitives.py`

Canonical Git SHA-256: `c1b69bdc74a4a060f6559a182306618f02c595b16e27f3ebb5e4bcca4ff7b735`. Raw checkout SHA-256: `b683304e3e8c0e4c4969594e8aa57c7eed8aff031a500357476e35afdbedb5d1`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 42 | dataclass | `SetInput` | `type definition` |
| 56 | dataclass | `VectorInput` | `type definition` |
| 80 | dataclass | `Measure` | `type definition` |
| 101 | function | `set_jaccard(left: SetInput \| None, right: SetInput \| None) -> Measure` | `Measure` |
| 116 | function | `weighted_jaccard(left: VectorInput \| None, right: VectorInput \| None) -> Measure` | `Measure` |
| 156 | function | `weighted_mean(values, weights) -> Measure` | `Measure` |
| 166 | function | `coverage(reliabilities, weights) -> Fraction` | `Fraction` |
| 174 | dataclass | `RankItem` | `type definition` |
| 186 | function | `stable_order(rows: tuple[RankItem, ...]) -> tuple[RankItem, ...]` | `tuple[RankItem, ...]` |

#### `matching_math/synthetic_b1.py`

Canonical Git SHA-256: `3fe584ac87862e80469823e9643c5a20b933b4913b4efe0ca20a55bc4b7f1746`. Raw checkout SHA-256: `9ae2b7de97c0afb8060ac35b330a9d014c34a5cf5ebd6f5f59184b0daf777f22`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 16 | dataclass | `B1Query` | `type definition` |
| 21 | dataclass | `B1Clause` | `type definition` |
| 29 | dataclass | `B1Profile` | `type definition` |
| 37 | dataclass | `B1Layer` | `type definition` |
| 48 | dataclass | `B1LayerDomain` | `type definition` |
| 54 | dataclass | `B1Vocabulary` | `type definition` |
| 68 | dataclass | `B1Config` | `type definition` |
| 93 | dataclass | `B1ContextKey` | `type definition` |
| 106 | dataclass | `B1QueryKey` | `type definition` |
| 113 | dataclass | `B1Lineage` | `type definition` |
| 123 | dataclass | `B1LayerStatus` | `type definition` |
| 133 | dataclass | `B1Occurrence` | `type definition` |
| 139 | dataclass | `B1ClauseEvaluation` | `type definition` |
| 148 | dataclass | `B1GateSummary` | `type definition` |
| 156 | dataclass | `B1PartitionKey` | `type definition` |
| 165 | dataclass | `B1CandidateResult` | `type definition` |
| 195 | dataclass | `B1PartitionResult` | `type definition` |
| 201 | dataclass | `B1BatchResult` | `type definition` |
| 560 | function | `score_synthetic_b1(query: B1Query, candidates: tuple[B1Profile, ...], *, vocabulary: B1Vocabulary, config: B1Config) -> B1BatchResult` | `B1BatchResult` |

#### `matching_math/synthetic_m1.py`

Canonical Git SHA-256: `07fc33ebf87fc5ba02a55d39b0a2ac0f6a8f58af2ff07db8c943bcea84c3263b`. Raw checkout SHA-256: `6b0edbd42234e223e4e7f844a872f33600bad7a88e9de9d62916c32d2bd88bcd`.

| Line | Kind | Signature/name | Declared return |
|---|---|---|---|
| 30 | dataclass | `M1Config` | `type definition` |
| 46 | dataclass | `FixtureVocabulary` | `type definition` |
| 57 | dataclass | `FixtureProfile` | `type definition` |
| 65 | dataclass | `FixtureLayer` | `type definition` |
| 76 | dataclass | `FixtureLineage` | `type definition` |
| 86 | dataclass | `LayerSide` | `type definition` |
| 94 | dataclass | `LayerExplanation` | `type definition` |
| 106 | dataclass | `LayerDomain` | `type definition` |
| 112 | dataclass | `PartitionKey` | `type definition` |
| 128 | dataclass | `PairResult` | `type definition` |
| 148 | dataclass | `PartitionResult` | `type definition` |
| 154 | dataclass | `M1BatchResult` | `type definition` |
| 371 | function | `score_synthetic_notes_layered(reference: FixtureProfile, candidates: tuple[FixtureProfile, ...], *, vocabulary: FixtureVocabulary, config: M1Config) -> M1BatchResult` | `M1BatchResult` |

### DTO boundaries already present

`matching_input` has four explicit dataclasses: Provenance, Field, Note and ProfileInput; state is an Enum, not a wire state schema. Values and provenance are decoded under its existing local version. `image_validation` has Limits and ImageMetadata. Primitives have SetInput, VectorInput, Measure and RankItem. M1 has12 explicit dataclasses; B1 has18, totaling40 across inventoried source. Full exact annotated field/default lists are in `python_files[].symbols[].fields`; no new DTO version retrofits these classes.

Do not serialize a dataclass blindly with `asdict` as an application response. Frozen dataclasses and Python annotations do not enforce all runtime types or permissions. Existing local strings/errors/paths and private provenance require an authorized output projection. Domain result objects remain separate from proposed transport DTOs.

## Future typed boundaries — PROPOSED

[Architecture_Interface_Registry.json](../08_Operations/Test_Evidence/Architecture_Interface_Registry.json) contains29 logical interface records with separate `status: PROPOSED`, version, caller, component dependencies, input/output typed-field schemas, permission gate, provenance, failure behavior, idempotency, tests and blockers. IDs are exact unsuffixed identities. Schema IDs use `<IF-ID>.input.v1` and `<IF-ID>.output.v1`; status is a separate field. This is an architecture typed-field registry, not executable JSON Schema/OpenAPI or an installed DTO model.

Every proposed operation requires a versioned `TransportBudgetPolicy.v1` with explicit accepted numeric request/response/depth/string/collection/numeric/work/deadline/stream limits. Those numeric choices are **not yet accepted**. Missing or incompatible policy blocks execution; no8KiB, adapter2MiB or synthetic fixture-bound default is imported. Unknown fields, implicit coercion, missing required versions and fallback permissions are forbidden. Internal-only RequestContext and principal lease contain verified server references, not browser-selectable identity/role/SQL/credentials.

All reads authorize before restricted object lookup, counts, pages, scoring or bytes. Write interfaces additionally require a separately approved trusted writer, owner/reviewer capability, origin/CSRF policy, expected version, principal/scope-bound idempotency key and atomic rollback. No normal application interface invokes operator CLI, admin SQL, role switching, container management or an arbitrary URL/file path. Denied/missing/private revoked objects share a safe non-enumerating outcome. Authorized unknown/incomplete/held states remain distinct only when their detail is permitted.

The shared SafeOutcome defines state/request ID/allowlisted reason/payload and exact output version. Ready payload facts require field-specific Provenance; missing data remains Unknown or Unavailable, not zero/empty. Page cursors bind principal, scope, filter, snapshot and rights epoch; stale context fails rather than leaking an old total. ExactRational carries bounded canonical numerator/denominator decimal integer strings **after** exact rational ordering within compatible partitions. Display rounding never feeds ordering. No cross-partition rank is allowed.

Thirty-one explicitly versioned common types describe policy, verified context, provenance, field/profile projection, exact rationals, page/outcome, separately real matching context and mutation preconditions. These types are all PROPOSED. The machine registry is authoritative for their complete required field descriptions; no implicit date/UUID/numeric coercion is assumed. Strict JSON/Python validation differences require explicit tests if a library is later selected.

### Logical operation inventory — every row PROPOSED / future tests NOT RUN

| Logical ID | Responsibility | Input schema | Output schema | Caller |
|---|---|---|---|---|
| `IF-AUTH-SESSION-1` | Verify application session | `IF-AUTH-SESSION-1.input.v1` | `IF-AUTH-SESSION-1.output.v1` | C-UI-SHELL / C-TRANSPORT |
| `IF-PRINCIPAL-LEASE-1` | Lease genuine nonadmin principal | `IF-PRINCIPAL-LEASE-1.input.v1` | `IF-PRINCIPAL-LEASE-1.output.v1` | C-AUTHN / trusted application composition ONLY |
| `IF-CATALOGUE-QUERY-1` | Query authorized catalogue | `IF-CATALOGUE-QUERY-1.input.v1` | `IF-CATALOGUE-QUERY-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-PROFILE-READ-1` | Read authorized profile projection | `IF-PROFILE-READ-1.input.v1` | `IF-PROFILE-READ-1.output.v1` | C-UI-PAGES / C-APP-COMPARE / C-APP-MATCH |
| `IF-VOCABULARY-READ-1` | Read reviewed canonical vocabulary | `IF-VOCABULARY-READ-1.input.v1` | `IF-VOCABULARY-READ-1.output.v1` | C-UI-PAGES / C-APP-MATCH |
| `IF-CAPABILITY-READ-1` | Check bounded operation capability | `IF-CAPABILITY-READ-1.input.v1` | `IF-CAPABILITY-READ-1.output.v1` | C-UI-PAGES / C-APP-MATCH |
| `IF-MATCH-VALIDATE-1` | Validate future real matching request | `IF-MATCH-VALIDATE-1.input.v1` | `IF-MATCH-VALIDATE-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-MATCH-EXECUTE-1` | Orchestrate future real matching | `IF-MATCH-EXECUTE-1.input.v1` | `IF-MATCH-EXECUTE-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-COMPARISON-READ-1` | Project side-by-side facts | `IF-COMPARISON-READ-1.input.v1` | `IF-COMPARISON-READ-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-MEDIA-RESOLVE-1` | Resolve asset use rights | `IF-MEDIA-RESOLVE-1.input.v1` | `IF-MEDIA-RESOLVE-1.output.v1` | C-UI-PAGES / C-APP-MEDIA |
| `IF-MEDIA-DELIVER-1` | Deliver authorized owned media | `IF-MEDIA-DELIVER-1.input.v1` | `IF-MEDIA-DELIVER-1.output.v1` | C-UI-PAGES through C-APP-MEDIA |
| `IF-BUYING-SOURCES-READ-1` | Read personal buying-source bookmarks | `IF-BUYING-SOURCES-READ-1.input.v1` | `IF-BUYING-SOURCES-READ-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-BUYING-SOURCE-WRITE-1` | Write personal buying-source bookmark | `IF-BUYING-SOURCE-WRITE-1.input.v1` | `IF-BUYING-SOURCE-WRITE-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-PURCHASE-STATUS-WRITE-1` | Record manual purchase status | `IF-PURCHASE-STATUS-WRITE-1.input.v1` | `IF-PURCHASE-STATUS-WRITE-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-COLLECTION-READ-1` | Read own collection | `IF-COLLECTION-READ-1.input.v1` | `IF-COLLECTION-READ-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-COLLECTION-WRITE-1` | Record own collection changes | `IF-COLLECTION-WRITE-1.input.v1` | `IF-COLLECTION-WRITE-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-DASHBOARD-READ-1` | Read authorized personal summary | `IF-DASHBOARD-READ-1.input.v1` | `IF-DASHBOARD-READ-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-REVIEW-QUEUE-READ-1` | Read authorized review queue | `IF-REVIEW-QUEUE-READ-1.input.v1` | `IF-REVIEW-QUEUE-READ-1.output.v1` | Authorized reviewer through C-UI-PAGES |
| `IF-REVIEW-DECISION-WRITE-1` | Record bounded review decision | `IF-REVIEW-DECISION-WRITE-1.input.v1` | `IF-REVIEW-DECISION-WRITE-1.output.v1` | Explicit authorized reviewer through C-UI-PAGES |
| `IF-SOURCE-INTAKE-REQUEST-1` | Submit source acquisition request | `IF-SOURCE-INTAKE-REQUEST-1.input.v1` | `IF-SOURCE-INTAKE-REQUEST-1.output.v1` | Own private user or authorized curator through C-UI-PAGES |
| `IF-ASSET-INTAKE-REQUEST-1` | Submit image intake request | `IF-ASSET-INTAKE-REQUEST-1.input.v1` | `IF-ASSET-INTAKE-REQUEST-1.output.v1` | Authorized owner/reviewer through C-UI-PAGES |
| `IF-PRIVATE-SETTINGS-1` | Read or change bounded private preferences | `IF-PRIVATE-SETTINGS-1.input.v1` | `IF-PRIVATE-SETTINGS-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-OPERATOR-STATUS-READ-1` | Read safe operational status projection | `IF-OPERATOR-STATUS-READ-1.input.v1` | `IF-OPERATOR-STATUS-READ-1.output.v1` | Explicit authorized system reviewer through C-UI-PAGES |
| `IF-RIGHTS-REVIEW-1` | Record explicit rights review | `IF-RIGHTS-REVIEW-1.input.v1` | `IF-RIGHTS-REVIEW-1.output.v1` | Explicit authorized rights reviewer through C-UI-PAGES |
| `IF-SESSION-END-1` | End application session | `IF-SESSION-END-1.input.v1` | `IF-SESSION-END-1.output.v1` | C-UI-SHELL via C-TRANSPORT |
| `IF-PERSONAL-STATE-READ-1` | Read own interest and cart state | `IF-PERSONAL-STATE-READ-1.input.v1` | `IF-PERSONAL-STATE-READ-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-PERSONAL-STATE-WRITE-1` | Write own interest and cart state | `IF-PERSONAL-STATE-WRITE-1.input.v1` | `IF-PERSONAL-STATE-WRITE-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-PURCHASE-RECORD-WRITE-1` | Write own manual purchase record and history | `IF-PURCHASE-RECORD-WRITE-1.input.v1` | `IF-PURCHASE-RECORD-WRITE-1.output.v1` | C-UI-PAGES via C-TRANSPORT |
| `IF-PURCHASE-RECORD-READ-1` | Read own manual purchase history and record | `IF-PURCHASE-RECORD-READ-1.input.v1` | `IF-PURCHASE-RECORD-READ-1.output.v1` | C-UI-PAGES on R-CART / R-COLLECTION / R-COLLECTION-ITEM via C-TRANSPORT |

### Operation-level contracts

The following sections make each interface reviewable without opening JSON. All schemas inherit the common strict policy, safe outcome and pending explicit budget. Dependencies are proposed component IDs, not current imported modules. Future tests are SPECIFIED / NOT RUN.

#### `IF-AUTH-SESSION-1` — Verify application session

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-AUTHN`, `C-CONFIG`, `C-AUDIT`.

Input (`IF-AUTH-SESSION-1.input.v1`): `auth_proof`: opaque bounded proof under later approved provider/session ADR; never DB username; `audience`: exact approved application audience; `budget_policy_ref`: TransportBudgetPolicy.v1.

Output (`IF-AUTH-SESSION-1.output.v1`): `outcome`: SafeOutcome.v1; `verified_session_ref`: server-created opaque reference; `audience`: verified exact audience; `expiry`: UTC expiry; `allowed_scope_choices`: authorized opaque scope references only.

Authorization: Validate authentic proof, audience, expiry, revocation and anti-CSRF/origin policy before any private resource access.

Provenance: Approved session issuer evidence; no source facts returned.

Idempotency/failure: Read validation is repeatable; never cache revocation decisions beyond approved policy. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Provider/session architecture, secret handling and exact policy not approved. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PRINCIPAL-LEASE-1` — Lease genuine nonadmin principal

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-PRINCIPAL`, `C-AUTHZ`, `C-CONFIG`, `C-AUDIT`.

Input (`IF-PRINCIPAL-LEASE-1.input.v1`): `verified_session_ref`: server-verified reference from IF-AUTH-SESSION-1; `scope_binding`: server-validated immutable audience/scope association; `budget_policy_ref`: TransportBudgetPolicy.v1.

Output (`IF-PRINCIPAL-LEASE-1.output.v1`): `outcome`: SafeOutcome.v1; `principal_lease_ref`: opaque server-only handle; no browser credentials; `verified_database_binding`: server-only immutable genuine session_user binding; `transaction_policy`: explicit approved read-only/writer-separated policy; `expiry`: bounded UTC expiry.

Authorization: SERVICE ONLY. Establish approved genuine nonadmin login; verify session_user=current_user, effective privileges, no superuser/BYPASSRLS/owner/writer inheritance. No browser login/role choice, SET ROLE/GUC impersonation or admin fallback.

Provenance: Server-reviewed immutable session-to-principal mapping and live effective-role evidence; no change to existing operator identity.

Idempotency/failure: Lease creation/release tied to one principal and request; clean cancellation, rollback, reset and discard on reuse ambiguity; never share across users. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Principal ADR, genuine login provisioning, pool/ownership/reset tests not implemented or authorized. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-CATALOGUE-QUERY-1` — Query authorized catalogue

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-CATALOGUE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-CATALOGUE-QUERY-1.input.v1`): `context`: RequestContext.v1; `query_text`: bounded literal string; no expressions; `filters`: explicit allowlisted typed filters; `page_size`: positive integer within approved policy; required; `cursor`: opaque string or null; `sort`: explicit approved stable sort.

Output (`IF-CATALOGUE-QUERY-1.output.v1`): `outcome`: SafeOutcome.v1; `page`: Page.v1 of ProfileProjection.v1.

Authorization: Authorize session/scope and each selected field before lookup, filter counts, pagination or totals.

Provenance: Reviewed selected accessible facts, source rights and authorized private overlays remain distinct.

Idempotency/failure: Read-only; deterministic within bound snapshot; stale rights/epoch invalidates cursor. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Catalogue principal, selected-field projection, pagination and transport policies pending. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PROFILE-READ-1` — Read authorized profile projection

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-CATALOGUE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-PROFILE-READ-1.input.v1`): `context`: RequestContext.v1; `profile_id`: canonical UUID string; `projection_fields`: bounded explicit allowlisted field paths.

Output (`IF-PROFILE-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `profile`: ProfileProjection.v1 or null.

Authorization: Authenticate/authorize scope before restricted lookup; object and field rights AND selection gates; UUID is not permission.

Provenance: Selected observation/capture/revision/transform/review/rights references; adapter DTO must not be returned raw.

Idempotency/failure: Read-only; reauthorize for each operation; missing/hidden/denied object same safe outcome. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Existing read_profile is local callback adapter; no application session or public serializer exists. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-VOCABULARY-READ-1` — Read reviewed canonical vocabulary

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-CATALOGUE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-VOCABULARY-READ-1.input.v1`): `context`: RequestContext.v1; `vocabulary_version`: explicit requested real or approved fixture version; no mixing; `domain_version`: explicit version; `page_size`: bounded positive integer; `cursor`: opaque string or null.

Output (`IF-VOCABULARY-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `page`: Page.v1 of canonical note ID, authorized label and compatible layer-domain membership; `vocabulary_fingerprint`: exact digest; `alias_normalization_version`: explicit accepted version or unavailable.

Authorization: Authorize vocabulary/source projection before labels/counts/pages; do not infer alias acceptance.

Provenance: Reviewed vocabulary, alias and normalization evidence with exact fingerprints.

Idempotency/failure: Read-only; version mismatch fails; no latest/fallback substitution. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Real vocabulary/domain/alias/normalization approvals pending;43 proposals remain unpromoted. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-CAPABILITY-READ-1` — Check bounded operation capability

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-MATCH`, `C-AUTHZ`, `C-PORTS`, `C-PG-READ`, `C-DTO`.

Input (`IF-CAPABILITY-READ-1.input.v1`): `context`: RequestContext.v1; `operation`: explicit method/use case string; `object_refs`: bounded permitted references; `requested_context`: RealMatchContext.v1 or explicit synthetic contract reference.

Output (`IF-CAPABILITY-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `capability`: available | unavailable | unknown; `required_versions`: exact permitted version references; `safe_blockers`: bounded permitted reason codes; no hidden object counts.

Authorization: Authorize objects before checking their policy/capability details; recheck again at execution.

Provenance: Separate data, policy, rights, identity and testing prerequisites; no capability from nonempty notes alone.

Idempotency/failure: Read-only advisory result; never an authorization token or durable grant. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Real matching remains unavailable; capability reader unimplemented. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-MATCH-VALIDATE-1` — Validate future real matching request

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-MATCH`, `C-DTO`, `C-DOMAIN-TYPES`, `C-DOMAIN-REAL`, `C-AUTHZ`.

Input (`IF-MATCH-VALIDATE-1.input.v1`): `context`: RequestContext.v1; `real_context`: RealMatchContext.v1; `mode`: explicit approved real reference | real required-optional-excluded method; `reference_id`: authorized canonical UUID or explicit null for custom query; `clauses`: bounded explicit canonical note ID, selector, role, positive weight or null where allowed; `layer_policy`: explicit compatible policy/version.

Output (`IF-MATCH-VALIDATE-1.output.v1`): `outcome`: SafeOutcome.v1; `validated_query_ref`: server-bound immutable digest/reference or null; `canonical_query`: exact separately approved real query shape or null; `capability`: explicit available/unavailable state.

Authorization: Authorize scope/note/reference access before evidence lookup; strict shape and budget validation never grants eligibility.

Provenance: Preserve real note identity and versioned closure/domain policy; no SYNTHETIC context relabeling.

Idempotency/failure: Pure validation given fixed context; no writes, scoring, auto-normalization or fallback modes. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Separate real query/method/closure/normalization contract not accepted; no wrapper around synthetic scorers authorized. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-MATCH-EXECUTE-1` — Orchestrate future real matching

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-MATCH`, `C-DOMAIN-REAL`, `C-DOMAIN-TYPES`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-MATCH-EXECUTE-1.input.v1`): `context`: RequestContext.v1; `validated_query_ref`: server-bound exact query/context reference; `real_context`: RealMatchContext.v1; `candidate_scope`: explicit authorized bounded snapshot policy; `pagination_policy`: explicit partition-preserving approved policy.

Output (`IF-MATCH-EXECUTE-1.output.v1`): `outcome`: SafeOutcome.v1; `partitions`: bounded sequence of MatchPartitionProjection.v1; ordering exact within key only; `unranked`: bounded sequence of MatchResultProjection.v1 with null fit/partition where unavailable and safe authorized reason; `completeness`: full_authorized_snapshot | partial; exact authorized scope explicit; no global ranking; `projection_policy_ref`: exact accepted result/explanation/confidence/evidence/budget versions; no policies selected here.

Authorization: Genuine principal and current membership/source-field rights/selection/closure/hold/eligibility gates precede candidate counts/pages/scoring. Revalidate stale input context.

Provenance: Canonical real perfume/note IDs, selected evidence snapshot, reviewed vocabulary/domain/normalization/closure/method/config versions; no synthetic IDs/lineage.

Idempotency/failure: Read-only reproducible only for identical authorized snapshot/config; exact rational ordering inside partition before serialization/rounding; never cross-partition rank. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Real matching, input contract, current eligible data, closure policy and performance limits unapproved/unimplemented. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-COMPARISON-READ-1` — Project side-by-side facts

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-COMPARE`, `C-APP-CATALOGUE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-COMPARISON-READ-1.input.v1`): `context`: RequestContext.v1; `profile_ids`: bounded distinct canonical UUID sequence; `field_paths`: explicit allowlisted sequence.

Output (`IF-COMPARISON-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `profiles`: bounded ProfileProjection.v1 sequence; `differences`: typed factual differences with unknown/partial markers; no chemical equivalence; `matching`: separately gated projection or unavailable.

Authorization: Authorize every object/field/overlay before projection; missing another private object remains masked.

Provenance: Selected comparable facts; source assertions and personal overlays stay separate.

Idempotency/failure: Read-only; deterministic permitted projection; no automatic scoring side effect. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Private read service pending; real scoring remains separately blocked. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-MEDIA-RESOLVE-1` — Resolve asset use rights

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-MEDIA`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-MEDIA-RESOLVE-1.input.v1`): `context`: RequestContext.v1; `asset_ref`: opaque asset reference; `operation`: explicit display; other uses require separate approved interface policy; `projection_binding`: authorized profile/note and asset association.

Output (`IF-MEDIA-RESOLVE-1.output.v1`): `outcome`: SafeOutcome.v1; `authorized_media_ref`: short-lived principal/scope/operation-bound opaque reference or null; `attribution`: authorized required credit/license text or null; `state`: shared safe state; placeholder where denied.

Authorization: Authorize object association and current source/capture/per-asset exact-use/parent/derivative/expiry/revocation before any locator/bytes.

Provenance: Exact registered asset hash/lineage/rights version and current authorization; public URL/license label alone insufficient.

Idempotency/failure: Read-only short-lived resolution; not reusable cached permission; delivery must reauthorize. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Application media binding, owned storage, sample rights and intake not approved;0 canonical assets historically. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-MEDIA-DELIVER-1` — Deliver authorized owned media

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-MEDIA`, `C-ASSET-VALIDATOR`, `C-ASSET-STORE`, `C-PORTS`, `C-AUTHZ`, `C-DTO`.

Input (`IF-MEDIA-DELIVER-1.input.v1`): `context`: RequestContext.v1; `authorized_media_ref`: opaque exact-use reference from resolver; `delivery_budget_ref`: approved stream/response bound policy.

Output (`IF-MEDIA-DELIVER-1.output.v1`): `outcome`: SafeOutcome.v1; `content`: bounded verified image/png bytes only if approved; no source URL/proxy; `metadata`: exact hash/dimensions/byte count; `attribution`: authorized required credit/license projection; `cache_policy`: explicit private no-store direction pending exact transport ADR.

Authorization: Reauthorize before owned object read and immediately before delivery; reject changed binding/rights; no arbitrary URL/file path/user login input.

Provenance: Exact owned registered binary, verified technical metadata, active current display rights/lineage; technical PNG success is not a grant.

Idempotency/failure: Read-only bounded stream; stop on revocation/deadline; no acquisition, transform or stored derivative side effect. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: No HTTP/media service or safe owned-object adapter exists; registered callback validator is local tooling. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-BUYING-SOURCES-READ-1` — Read personal buying-source bookmarks

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-BUYING-SOURCES-READ-1.input.v1`): `context`: RequestContext.v1; `profile_id`: authorized canonical UUID or null for all own bookmarks; `page_size`: bounded positive integer; `cursor`: opaque string or null; `projection_policy_ref`: exact accepted own bookmark/observed fields/withdrawn visibility/page/bounds policy; unselected, missing blocks.

Output (`IF-BUYING-SOURCES-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `page`: Page.v1 of BuyingSourceProjection.v1 including explicit platform/store/URL/observed Money/observed Quantity/observed ManualDateValue/own note and revision; `price_currentness`: manual observed timestamp/unknown only; not live current price, paid price or availability.

Authorization: Authenticate owner binding before object lookup/count/page; no other user cart exposure.

Provenance: User-entered seller-specific link and recorded price; source listing facts require separate rights.

Idempotency/failure: Read-only own records; no live price or cart synchronization. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Private write/read service and personal operation policy not implemented. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-BUYING-SOURCE-WRITE-1` — Write personal buying-source bookmark

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-BUYING-SOURCE-WRITE-1.input.v1`): `context`: RequestContext.v1; owner derived from verified actor only; `operation`: proposed create | update | withdraw; exact action/retention policy unselected and required; `bookmark_id`: own canonical UUID for update/withdraw; explicit null for create; `profile_id`: independently authorized canonical perfume UUID for create/update; existing binding must match unless exact rebind policy accepted; `mutation`: MutationPrecondition.v1; expected revision or exact accepted create-absence semantics, principal-bound idempotency; `changed_fields`: explicit bounded allowlisted field-name set; create/update/withdraw required sets require accepted action policy; reject undeclared fields and non-null inactive fields; `platform`: PlatformValue.v1 or explicit null only when inactive/unchanged under action policy; `store`: SellerValue.v1 or explicit null only when inactive/unchanged; `url`: bounded explicit permitted http(s) bookmark link or null only when inactive/unchanged; URL/bounds policy required; `observed_price`: Money.v1 known/unknown or null only when inactive/unchanged; observed listing price, never paid price; `observed_size`: Quantity.v1 known/unknown or null only when inactive/unchanged; observed size, never inferred physical capacity; `observed_at`: ManualDateValue.v1 known/unknown or null only when inactive/unchanged; `own_note`: OwnNoteValue.v1 known/unknown or null only when inactive/unchanged; `confirmation`: explicit withdraw confirmation under exact accepted policy; null for other operations; `field_policy_ref`: exact accepted field/URL/platform/observed values/action/withdraw-retention/bounds policy; unselected, missing blocks.

Output (`IF-BUYING-SOURCE-WRITE-1.output.v1`): `outcome`: SafeOutcome.v1; `bookmark`: BuyingSourceProjection.v1 for accepted own change or explicit null for safe failure/withdraw under exact policy; `record_state`: explicit accepted active/withdrawn state; never silently delete retained history; `revision`: exact new record/tombstone revision; `operation_receipt`: safe principal/scope/key/digest/version reference.

Authorization: Derive owner from verified actor. Authorize profile and own bookmark BEFORE lookup/create/update/withdraw; source ID/URL is not permission. Independently check unchanged profile binding, explicit action/field/withdraw/retention policy, expected revision/create-absence, idempotency and origin/CSRF. No arbitrary owner/scope or mass assignment; no admin/operator fallback.

Provenance: User manually observed platform/store/URL/price/size/date and own note, with explicit known/unknown typed values. Observed facts are separate from paid purchase facts and current canonical seller data.

Idempotency/failure: Same actor/scope/action/key/request digest has one effect; changed digest or stale revision conflicts atomically. Withdraw only under exact accepted retention/visibility policy. No fetch, seller-network access, checkout/payment/order/cart sync, purchase-record/ordered-state change or inventory cascade. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Exact field/platform/URL/observed Money/Quantity/date/note grammars, limits, action/withdraw/retention policy and private writer unselected/unapproved; no R31 activation. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PURCHASE-STATUS-WRITE-1` — Record manual purchase status

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-PURCHASE-STATUS-WRITE-1.input.v1`): `context`: RequestContext.v1; `bookmark_id`: own canonical UUID; `mutation`: MutationPrecondition.v1; `manual_status`: explicit approved state enum; later policy must enumerate values; `recorded_at`: explicit user-supplied bounded timestamp or unknown marker.

Output (`IF-PURCHASE-STATUS-WRITE-1.output.v1`): `outcome`: SafeOutcome.v1; `status`: own manually recorded value and timestamp; `version`: new record version; `operation_receipt`: safe idempotency/version reference.

Authorization: Owner check before lookup/write; CSRF/origin and exact transition validation; no merchant session/account access.

Provenance: User intent and manual timestamp only; not payment/order confirmation.

Idempotency/failure: Key/digest/version protected; retries cannot place any order because no order operation exists. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Exact manual state-transition contract and trusted private writer not approved. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-COLLECTION-READ-1` — Read own collection

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-COLLECTION-READ-1.input.v1`): `context`: RequestContext.v1; owner derived from verified actor; `operation`: proposed list | detail | lifecycle_history | aggregate_drilldown; exact accepted projection policy required; `collection_item_id`: own canonical UUID for detail/history or explicit null for list/drilldown; `profile_filter`: explicit authorized canonical UUID filter or null; `lifecycle_filter`: bounded explicit accepted lifecycle/status set or null; enum/unknown behavior unselected; `projection_fields`: bounded exact allowlisted current/history field mask; `snapshot_ref`: exact authorized physical-inventory snapshot/version or explicit null for fresh accepted query; `authorized_metric_context_ref`: previously authorized dashboard metric/aggregate bucket/context reference for drilldown; explicit null otherwise; reauthorize before use; `drilldown_filter`: explicit accepted bounded bucket filter bound to authorized metric/context/snapshot; null otherwise; never browser authority; `page_size`: explicit positive integer within accepted page/work budget or null for single-detail policy; `cursor`: opaque owner/scope/operation/filter/order/snapshot/rights-bound cursor or null; `projection_policy_ref`: exact accepted lifecycle/current/history/filter/drilldown/temporal/page/retention/bounds policy; unselected, missing blocks.

Output (`IF-COLLECTION-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `page`: Page.v1 of CollectionProjection.v1 for list/drilldown; partial/page scope explicit, not full inventory aggregates; `item`: CollectionProjection.v1 for authorized own detail or explicit null; `lifecycle_history`: bounded authorized own versioned physical lifecycle CollectionProjection.v1 sequence or null under accepted history policy; `metric_context`: same reauthorized metric/bucket/snapshot binding or null; no recomputation of complete brand/note counts from a single item page; `completeness`: explicit page_only | partial | full_authorized_snapshot under accepted policy; never infer whole-collection coverage.

Authorization: Owner authorization before item lookup/lifecycle history/count/filter/page or drilldown. Reauthorize previously permitted aggregate bucket/metric context, underlying own rows and related catalogue fields; cursor/filter is not permission. Partial item page never proves complete brand/note counts.

Provenance: Manual ownership/user notes separate from selected product facts and purchase bookmarks.

Idempotency/failure: Read-only; no inferred ownership from shopping status. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Exact inventory operation/lifecycle/filter/history/projection/aggregate drilldown/page/retention policies and principal unselected/unapproved; no collection purchase FK. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-COLLECTION-WRITE-1` — Record own collection changes

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-COLLECTION-WRITE-1.input.v1`): `context`: RequestContext.v1; actor-derived owner; `operation`: proposed create | update | mark_received | mark_finished | mark_sold | mark_gifted | withdraw; exact accepted transition/retention policy required; `collection_item_id`: own canonical UUID for existing item; explicit null for create only under accepted absence policy; `profile_id`: independently authorized canonical UUID; existing binding must match; `mutation`: MutationPrecondition.v1; expected revision/create-absence, principal/action key/digest and user intent; `changed_fields`: explicit bounded accepted physical field set; exact action-required fields; non-null inactive/unknown fields rejected; `ownership`: explicit accepted target ownership or null when unchanged under exact action policy; `lifecycle`: explicit accepted target lifecycle or null when unchanged; action/lifecycle consistency checked; `remaining_amount`: Quantity.v1 known/unknown or null only when inactive/unchanged; no guessed zero; `capacity`: Quantity.v1 manually recorded known/unknown or null only when inactive/unchanged; not derived from purchase record or observed listing size; `own_note`: OwnNoteValue.v1 or null only when inactive/unchanged; `action_date`: ManualDateValue.v1 or null under exact accepted action/date policy; no today default; `confirmation`: explicit lifecycle/withdraw confirmation under exact policy, null otherwise; `field_policy_ref`: exact accepted physical quantity/unit/capacity/date/note/ownership/lifecycle/action/withdraw-retention/bounds policy; unselected, missing blocks.

Output (`IF-COLLECTION-WRITE-1.output.v1`): `outcome`: SafeOutcome.v1; `item`: CollectionProjection.v1 or explicit null under accepted safe failure/withdrawal visibility policy; `revision`: exact new physical inventory/tombstone revision; `history_version`: own physical lifecycle history version, separate from purchase history; `operation_receipt`: safe actor/scope/action/key/digest/version reference.

Authorization: Authorize genuine actor-owned item and profile BEFORE lookup/create/lifecycle/update/withdraw; trusted private writer and origin/CSRF gates. Explicit action, expected revision, accepted ownership/lifecycle/field/retention policy required; no submitted owner/role, automatic purchase link, price or unselected FK.

Provenance: Explicit manual user intent; no canonical product fact mutation.

Idempotency/failure: Actor/scope/action/key/request digest and expected revision; stale/conflicting command atomically fails; exact accepted lifecycle/withdraw retention policy required. No paid-price/history write, inferred ownership, purchase/ordered state change or inventory cascade. Capacity is manual physical projection, never assumed purchase-derived. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Physical inventory action/lifecycle/capacity/remaining/unit/date/note/retention/bounds policies and private writer remain unselected/unapproved; no paid price or collection-purchase FK accepted. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-DASHBOARD-READ-1` — Read authorized personal summary

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-DASHBOARD-READ-1.input.v1`): `context`: RequestContext.v1; `summary_spec`: explicit approved metric set and time range; `snapshot_ref`: own snapshot reference or explicit fresh request.

Output (`IF-DASHBOARD-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `metrics`: bounded own authorized aggregates with definitions, evidence timestamps and unknown states; `catalogue_scope`: explicit authorized scope; no global hidden counts.

Authorization: Authorize owner and underlying rows/fields BEFORE every aggregate/count; hide other-user existence.

Provenance: Own manual records plus separately permitted facts; no fake completeness/rating/smell metrics.

Idempotency/failure: Read-only fixed definitions/snapshot; no materialization or persistent private cache implied. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Dashboard metric definitions, private read path and aggregate policy pending. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-REVIEW-QUEUE-READ-1` — Read authorized review queue

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-REVIEW`, `C-PORTS`, `C-REVIEW-DATA`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-REVIEW-QUEUE-READ-1.input.v1`): `context`: RequestContext.v1 with separately verified reviewer capability/scope; `operation`: proposed queue | source_detail | proposal_detail | evidence_detail; exact action/projection policy required; `queue_kind`: explicit accepted source/normalization/conflict/rights queue; null only for exact detail policy; `subject_ref`: ScopedReviewReference.v1 for detail; explicit null for queue; kind/id/revision/scope binding required; `filters`: bounded explicit allowlisted review state/source/proposal-kind filter values or null; exact filter schema/policy unselected; `snapshot_ref`: exact authorized review snapshot/version or explicit null for fresh accepted queue request; `projection_fields`: bounded exact allowlisted detail/evidence/queue fields; no arbitrary raw payload/private dossier; `page_size`: explicit positive integer within accepted budget for queue or null for detail; `cursor`: opaque reviewer/scope/action/filter/snapshot/rights-bound cursor or null; `projection_policy_ref`: exact accepted action/scoped-reference/queue/detail/evidence/filter/history/page/bounds policy; unselected, missing blocks.

Output (`IF-REVIEW-QUEUE-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `page`: Page.v1 of ReviewDetailProjection.v1 for queue or explicit null for detail; `detail`: ReviewDetailProjection.v1 for exact authorized scoped source/capture/observation/proposal/evidence or explicit null; `snapshot_ref`: exact authorized immutable/current queue/detail snapshot version.

Authorization: Separately verified reviewer capability and exact source/capture/proposal/evidence scope/revision authorization BEFORE detail lookup, evidence dereference, filters/counts/pages. Submitted scoped ref/cursor is not authority. Mask missing/hidden/denied; raw staging/private grant dossiers require their own explicit projection rights.

Provenance: Existing immutable review/proposal/evidence chain;43 proposals/44 holds unchanged.

Idempotency/failure: Read-only; list projection cannot release a hold or select claims. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Exact queue/detail/evidence actions, scoped reference/filter/projection/page/rights policies and genuine reviewer principal unselected/unapproved; no ordinary user/operator privilege inheritance. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-REVIEW-DECISION-WRITE-1` — Record bounded review decision

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-REVIEW`, `C-PORTS`, `C-REVIEW-DATA`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-REVIEW-DECISION-WRITE-1.input.v1`): `context`: RequestContext.v1; `proposal_ref`: authorized exact versioned proposal; `mutation`: MutationPrecondition.v1; `decision`: explicit later-approved decision enum and reason/evidence references.

Output (`IF-REVIEW-DECISION-WRITE-1.output.v1`): `outcome`: SafeOutcome.v1; `decision_record`: immutable audited decision projection; `downstream_status`: separate selection/hold/eligibility states; no automatic activation; `operation_receipt`: safe key/version reference.

Authorization: Explicit reviewer/task authority and evidence rights before access/write; accepted decision policy required. Never expose admin CLI or assume authority to release holds.

Provenance: Exact proposal/reviewer/time/reason/evidence/version; source facts remain immutable.

Idempotency/failure: Append once under principal-bound key and expected proposal version; atomic conflict; no implicit canonical promotion. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: New decision powers and transitions unapproved;43 proposals/44holds/Khamrah untouched. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-SOURCE-INTAKE-REQUEST-1` — Submit source acquisition request

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-REVIEW`, `C-PORTS`, `C-REVIEW-DATA`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-SOURCE-INTAKE-REQUEST-1.input.v1`): `context`: RequestContext.v1; `source_locator`: bounded metadata-only source locator; explicit null for unknown OwnPrivateManualProposal, required known only under exact accepted curator branch policy; `intended_use`: explicit fields/operation/audience/scope; `permission_evidence_ref`: bounded metadata-only evidence ref or explicit null for unknown private manual proposal; unknown grants no rights/acquisition/capture; `request_key`: bounded owner-bound idempotency key; `request_kind`: OwnPrivateManualProposal | CuratorSourceAcquisitionRequest; `manual_proposal`: ManualMissingPerfumeProposal.v1 for own-private manual branch; explicit null for curator branch; `acquisition_proposal`: explicit bounded metadata-only method/fields/budget/use/permission/task proposal for curator branch; null for manual branch; no source capture/network/import; `request_policy_ref`: exact accepted discriminated private-manual/curator metadata/unknown-field/retention/bounds policy; unselected, missing blocks.

Output (`IF-SOURCE-INTAKE-REQUEST-1.output.v1`): `outcome`: SafeOutcome.v1; `request_ref`: metadata-only review request reference; `approval_state`: PROPOSED | BLOCKED; no acquisition performed.

Authorization: OwnPrivateManualProposal: derive owner from session, store private metadata only, no network/acquisition/canonical selection. CuratorSourceAcquisitionRequest: explicit curator scope/evidence access and separate human rights/acquisition/cost approval. Submission fetches no URL.

Provenance: Submitted metadata/evidence; record unknown permission as unknown.

Idempotency/failure: Deduplicate key/digest; metadata request only; no capture/download/import/jobs triggered. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Request workflow unimplemented; acquisition not authorized by this architecture. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-ASSET-INTAKE-REQUEST-1` — Submit image intake request

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-REVIEW`, `C-PORTS`, `C-REVIEW-DATA`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-ASSET-INTAKE-REQUEST-1.input.v1`): `context`: RequestContext.v1; `candidate_locator`: bounded metadata-only locator or explicit null for unknown private screenshot request; no bytes/cookies/local path fetch; `asset_kind`: proposed note illustration | bottle photograph for corresponding metadata branch; explicit null for private_screenshot_metadata, which does NOT assign canonical asset kind; `exact_use`: explicit acquisition/storage/private-display/public-display/derivative scopes; `per_file_rights_evidence_ref`: authorized exact per-file evidence ref or explicit unknown; `request_key`: bounded principal-bound key; `request_kind`: private_screenshot_metadata | note_illustration_metadata | bottle_photo_metadata; `intake_proposal`: bounded explicit metadata-only candidate/revision/format/method/budget/use/task request under accepted policy; no acquisition job or binary action; `request_policy_ref`: exact accepted branch/metadata/evidence/retention/bounds policy; unselected, missing blocks.

Output (`IF-ASSET-INTAKE-REQUEST-1.output.v1`): `outcome`: SafeOutcome.v1; `request_ref`: metadata-only review request reference; `approval_state`: PROPOSED | BLOCKED; no bytes acquired/registered.

Authorization: Exact human asset/use approval required separately; URL or license label is not an approved binding; no fetch/proxy. Private screenshot proposal is metadata/approval only; no screenshot bytes or intake authority.

Provenance: Per-file creator/revision/license/attribution/lineage/operation evidence; unknowns explicit.

Idempotency/failure: Metadata only, key/digest deduplication; no automatic binary intake or technical validation claim. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: No accepted sample asset binding or intake/storage operation approved. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PRIVATE-SETTINGS-1` — Read or change bounded private preferences

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-READ`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-PRIVATE-SETTINGS-1.input.v1`): `context`: RequestContext.v1; `operation`: explicit read | write; `preference_fields`: bounded allowlisted presentation preferences only; `mutation`: MutationPrecondition.v1 for write; explicit null for read.

Output (`IF-PRIVATE-SETTINGS-1.output.v1`): `outcome`: SafeOutcome.v1; `preferences`: own permitted presentation values; `version`: current/new version; `operation_receipt`: safe receipt for write or explicit null for read.

Authorization: Owner binding before lookup/write; write CSRF/origin gates; preferences cannot choose DB login/role/rights/eligibility/cache privilege.

Provenance: User preference intent, separate from security/policy configuration.

Idempotency/failure: Read-only read; key/digest/version for write; no secret or operator configuration change. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Exact preference allowlist and private writer not approved. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-OPERATOR-STATUS-READ-1` — Read safe operational status projection

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-REVIEW`, `C-PORTS`, `C-AUDIT`, `C-AUTHZ`, `C-DTO`.

Input (`IF-OPERATOR-STATUS-READ-1.input.v1`): `context`: RequestContext.v1; `status_scope`: explicit approved safe telemetry projection; `evidence_ref`: bounded immutable report reference or fresh authorized read request.

Output (`IF-OPERATOR-STATUS-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `status`: dated safe states and historical/current qualification; `checks`: bounded safe test/evidence metadata; no SQL execution, credentials, private paths or process controls.

Authorization: Explicit telemetry capability; no application admin/operator CLI connection. Authenticate before private evidence lookup.

Provenance: Immutable report SHA/time/source binding; historical PASS never becomes current service health.

Idempotency/failure: Read-only safe projection; no start/stop/migrate/restore/container execution. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Telemetry projection/role policy unimplemented; DB/service state NOT VERIFIED. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-RIGHTS-REVIEW-1` — Record explicit rights review

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-REVIEW`, `C-PORTS`, `C-REVIEW-DATA`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-RIGHTS-REVIEW-1.input.v1`): `context`: RequestContext.v1; `rights_target_ref`: exact source/field/asset/operation reference; `mutation`: MutationPrecondition.v1; `review_evidence`: bounded authorized revision/license/creator/attribution/expiry evidence refs; `decision`: explicit approved operation-specific review/revocation value.

Output (`IF-RIGHTS-REVIEW-1.output.v1`): `outcome`: SafeOutcome.v1; `review_record`: audited exact-use decision evidence projection; `revocation_epoch`: new version where applicable; `affected_use_state`: safe unavailable/allowed state only under approved policy.

Authorization: Separate explicit rights-review authority, source/asset evidence access and accepted operation policy; no broad source license inheritance or reverse revocation.

Provenance: Source/capture plus per-field/per-asset/use/parent/expiry evidence; historical review cannot grant unrelated uses.

Idempotency/failure: Principal/key/digest/precondition; immutable review history; revocation invalidates grants/cursors/media/results; no implicit acquisition. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Rights review powers/schema transition ADR unapproved; no new source or asset grant in this task. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-SESSION-END-1` — End application session

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-AUTHN`, `C-PRINCIPAL`, `C-AUDIT`, `C-CONFIG`.

Input (`IF-SESSION-END-1.input.v1`): `session_reference`: current authenticated server-bound session or opaque invalid/missing proof; `end_scope`: explicit current session; all-sessions requires later separate accepted policy; `budget_policy_ref`: TransportBudgetPolicy.v1.

Output (`IF-SESSION-END-1.output.v1`): `outcome`: SafeOutcome.v1; `state`: safe ended/unavailable public result without prior-session existence leak; `private_state_policy`: discard in-memory private results/leases and cancel outstanding requests.

Authorization: Session-bound invalidation with origin/CSRF policy; no cross-user session identifiers or DB role choices.

Provenance: Session issuer/revocation epoch only; no product/source facts.

Idempotency/failure: Repeated end requests yield same safe ended result; close/rollback/discard leases and prohibit stale response rendering. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Session provider, transport and invalidation/cancellation policy unimplemented. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PERSONAL-STATE-READ-1` — Read own interest and cart state

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-PERSONAL-STATE-READ-1.input.v1`): `context`: RequestContext.v1; `profile_id`: authorized canonical UUID or null for own list; `state_filter`: explicit bounded subset of wishlist | research | app_cart | tried | skipped or null; `page_size`: bounded positive integer; `cursor`: opaque string or null.

Output (`IF-PERSONAL-STATE-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `page`: Page.v1 of PersonalStateProjection.v1 under exact accepted active/withdrawn visibility policy; `states`: explicit wishlist | research | app_cart | tried | skipped; absent/withdrawn is not coerced to skipped.

Authorization: Derive owner from verified actor and authorize own state before lookup/filter/count/page; no browser owner or role selector.

Provenance: User-recorded interest/cart state distinct from seller-specific buying bookmarks, ordered/purchase state and physical ownership.

Idempotency/failure: Read-only deterministic own-state snapshot; no seller network access or automatic ownership inference. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Private read principal and exact personal transition/retention policies pending. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PERSONAL-STATE-WRITE-1` — Write own interest and cart state

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-PERSONAL-STATE-WRITE-1.input.v1`): `context`: RequestContext.v1; owner derived only from verified actor; `operation`: proposed create | move | update | withdraw; exact accepted action/transition/retention policy required; `entry_id`: own canonical UUID for existing entry or explicit null for create under accepted absence semantics; `profile_id`: independently authorized canonical UUID; existing entry binding must match; `interest_cart_state`: proposed wishlist | research | app_cart | tried | skipped target for active transition; explicit null for withdraw; never coerce remove into skipped; `recorded_at`: ManualDateValue.v1 or explicit null under exact accepted date policy; no invented timestamp; `confirmation`: explicit withdraw confirmation under accepted policy; null for other operations; `mutation`: MutationPrecondition.v1; expected entry revision/create-absence and principal/scope/action-bound key/digest; `transition_policy_ref`: exact accepted action/state/null/withdraw/retention/budget policy; unselected, missing makes remove/move unavailable.

Output (`IF-PERSONAL-STATE-WRITE-1.output.v1`): `outcome`: SafeOutcome.v1; `personal_state`: PersonalStateProjection.v1 or null according to exact accepted safe withdrawal visibility policy; `record_state`: explicit accepted active/withdrawn state; no implicit hard deletion; `revision`: exact new entry/tombstone revision; `operation_receipt`: safe actor/scope/action/key/digest/version reference; `side_effects`: NONE outside own interest/cart state; bookmarks, purchase statuses/history and physical inventory untouched.

Authorization: Authorize verified actor-owned entry/profile before lookup/write; exact explicit operation, transition, withdraw confirmation/retention, expected revision and idempotency required. Reject browser owner/role and invalid null/target combinations; absent policy keeps removal unavailable, never coerces skipped.

Provenance: Explicit manual user intent; separate from buying-source management, IF-PURCHASE-STATUS-WRITE-1 ordered/purchase status and IF-COLLECTION-WRITE-1 physical bottles.

Idempotency/failure: Actor/scope/action/key/request digest and expected revision protect create/move/update/withdraw. Stale or conflicting commands atomically fail. Exact accepted withdrawal retention/tombstone policy required; no bookmark, purchase/order/history or inventory mutation. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Exact operation/state/withdraw/null/retention/date/bounds policies and private writer unselected/unapproved; no inferred deletion or permission. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PURCHASE-RECORD-WRITE-1` — Write own manual purchase record and history

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-WRITE`, `C-AUTHZ`, `C-AUDIT`, `C-DTO`.

Input (`IF-PURCHASE-RECORD-WRITE-1.input.v1`): `context`: RequestContext.v1; owner derived only from verified actor; `operation`: proposed create | update | withdraw; exact transitions/retention policy unselected and required; `profile_id`: authorized canonical UUID string; `purchase_record_id`: own canonical UUID string for update/withdraw; explicit null for create; `own_saved_buying_source_id`: own canonical UUID string or explicit null; optional linkage, independently authorized; `paid_price`: Money.v1; optional fact represented by explicit known/unknown state, never omitted/coerced to zero; `purchased_volume`: Quantity.v1; optional fact represented by explicit known/unknown state; `purchase_date`: PurchaseDate.v1; optional fact represented by explicit known/unknown state; `seller`: SellerValue.v1; optional fact represented by explicit known/unknown state; `mutation`: MutationPrecondition.v1; expected revision/create-absence semantics and principal-bound idempotency required; `field_policy_ref`: exact accepted decimal/currency/unit/date/seller/bounds/enum/retention policy version; currently unselected, absence blocks.

Output (`IF-PURCHASE-RECORD-WRITE-1.output.v1`): `outcome`: SafeOutcome.v1; `purchase_record`: PurchaseRecordProjection.v1 owned authorized projection or null for safe failure; `history_version`: own purchase-history version; no other user existence/count leakage; `operation_receipt`: safe principal/scope/key/request-digest/version reference.

Authorization: Derive owner from genuine verified actor, never request owner/user/role. Authorize profile, own record and optional own saved buying source BEFORE lookup/count/write. Trusted private writer, origin/CSRF, expected revision, exact field/retention policies and atomic audit required; no operator/admin fallback.

Provenance: Explicit manual purchase facts/history with known/unknown Money/Quantity/date/seller; user assertions do not confirm merchant order/payment or canonical price/source facts.

Idempotency/failure: Principal/scope/operation/key/request digest and expected revision; identical retry has one effect, changed digest conflicts; atomic record/history/receipt or rollback. Withdraw only under exact approved retention policy. No inventory cascade, bottle creation, ordered-state update, order/payment/network operation or ownership inference. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Exact money/quantity/date/seller grammars, bounds, currency/unit enums, create/update/withdraw retention transitions and private writer remain unselected/unapproved; no R31 activation. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

#### `IF-PURCHASE-RECORD-READ-1` — Read own manual purchase history and record

Status: **PROPOSED**. Version: `1; incompatible semantics require a new exact schema/policy version; no implicit latest`. Dependencies: `C-APP-PRIVATE`, `C-PORTS`, `C-PG-READ`, `C-AUTHZ`, `C-DTO`.

Input (`IF-PURCHASE-RECORD-READ-1.input.v1`): `context`: RequestContext.v1; owner derived only from verified actor; `operation`: proposed history | detail; exact enum/projection policy unselected and required; `purchase_record_id`: own canonical UUID string for detail; explicit null for history; `profile_id`: canonical UUID filter or explicit null for all caller-own history; detail requires null; linked catalogue access checked separately; `page_size`: positive integer within exact accepted budget for history; explicit null for detail; no hidden default; `cursor`: opaque principal/scope/filter/snapshot/rights-bound cursor or explicit null; detail requires null; `record_state_filter`: explicit accepted active/withdrawn history filter policy; enum/retention visibility unselected, no implicit exposure of withdrawn facts; `field_policy_ref`: exact accepted manual paid-fact/history projection/retention/version/budget policy; absence blocks.

Output (`IF-PURCHASE-RECORD-READ-1.output.v1`): `outcome`: SafeOutcome.v1; `history_page`: Page.v1 of PurchaseRecordProjection.v1 for history or explicit null for detail; include caller-own records with no saved buying-source and no collection/bottle linkage; `purchase_record`: PurchaseRecordProjection.v1 for authorized own detail or explicit null for history/safe failure; `history_version`: exact caller-own purchase-history snapshot/version; `linked_catalogue_state`: explicit separately authorized catalogue projection state or unavailable; own manual facts do not grant current catalogue/source access; `linkage_semantics`: No collection FK/filter/automatic linkage assumed; unlinked purchase history remains discoverable through own history/profile filter.

Authorization: Derive owner from genuine verified actor before any restricted purchase lookup, filtered history count, pagination, detail or linked-object access. Authorize every own record; browser user/owner/role and another user record ID never grant access. Optional profile filter cannot probe hidden catalogue existence. Linked catalogue/seller-source facts require separate current authorization. Missing/denied private record responses are uniform; never use operator/admin fallback.

Provenance: Own manually recorded PurchaseRecordProjection.v1 with explicit Money.v1/Quantity.v1/PurchaseDate.v1/SellerValue.v1 known/unknown states and exact record/history versions; recorded paid facts are private user assertions, not current canonical price, merchant confirmation or live seller facts.

Idempotency/failure: Read-only; repeatable only within the same authorized history snapshot/filter/version. Cursors bind owner/scope/filter/snapshot/rights epoch, stale context fails closed. No writes, order/payment/network access, bottle creation or ordered/cart state coupling. Fail closed on missing/unsupported policy, context/version/budget, permission or dependency. Uniform private missing/denied/expired response; distinguish authorized unknown/incomplete/unavailable only where allowed. Atomic write rollback; no admin/algorithm/default fallback.

Capability blockers: Own-history read principal, exact field/state/retention visibility/pagination/unknown-value/budget policies remain unselected/unapproved. Existing catalogue/profile/collection/bookmark reads do not implement this contract; no collection FK or R31 activation accepted. Exact Human Owner architecture/operation policy and separate implementation approval required. TransportBudgetPolicy.v1 has no accepted numeric values; execution blocked until exact policy accepted.

Test strategy: strict schema/version/coercion/budget controls; forged/stale/admin/cross-user denial before work; operation-specific provenance/revocation failure; safe error projection; exact idempotency/expected-version or snapshot determinism; cancellation/rollback. Exercise the authorization and idempotency conditions above as negative cases. **NOT RUN**.

## Real matching remains a separate contract

`IF-MATCH-VALIDATE-1` and `IF-MATCH-EXECUTE-1` describe future **real** orchestration boundaries. Their existence on paper does not create an adapter-to-synthetic scorer wrapper. Future real types must bind canonical perfume/note identity, reviewed selected observations and field rights, real vocabulary/fingerprint, normalization/version, compatible layer/domain, accepted completeness assertions, review/hold/eligibility state, current scope, selection snapshot and method/configuration. They cannot reuse synthetic fixed fixture IDs/vocabularies/lineage/scope/snapshots as disguised real evidence. Unknown is not zero; incomplete is not absent; unavailable fit is never0%. Structural/Query Fit, Data Confidence and Direct Pairwise Evidence remain separate channels. No measured smell-similarity assertion follows.

`IF-COMPARISON-READ-1` may eventually project authorized facts without granting scoring. `IF-CAPABILITY-READ-1` reports prerequisites only after access checks; it is never a reusable grant. M1/B1 synthetic remain the only accepted exact scorers today; Full Mode A, real Mode A/B1 and B2 accords remain blocked pending their own contracts/data/policy/tests.

## Private product and review boundaries

Interest/cart state (`IF-PERSONAL-STATE-READ-1`/`IF-PERSONAL-STATE-WRITE-1`) remains separate from seller-specific buying-source bookmarks, manual ordered/purchase status and physical collection/ownership records. The Cart is a personal bookmark/list. No interface places orders, pays, checks out, synchronizes Shopee carts, assumes a purchase happened or infers ownership. Private owner is always derived from verified actor, never a submitted user ID. Dashboard aggregates obey the same authorization-before-count rule.

`IF-PURCHASE-RECORD-WRITE-1` separately proposes manually recorded purchase facts and history: own profile/record, optional own saved buying-source linkage, paid Money, purchased Quantity, purchase date and seller. Optional facts use explicit known/unknown states. Unknown price/volume/date/seller never becomes zero, a currency/unit default, today or an inferred seller. `Money.v1`, `Quantity.v1`, `PurchaseDate.v1`, `SellerValue.v1` and `PurchaseRecordProjection.v1` are versioned **PROPOSED** typed-field schemas in the registry. Their exact decimal/scale/range/length/currency/unit/date/seller/enum/retention policies remain unselected; missing accepted policy blocks execution. No R31 activation is inferred.

`IF-PURCHASE-RECORD-READ-1` separately proposes own bounded paginated history and own record detail for Cart, Collection and Collection Item. `history_page` explicitly returns `Page.v1` of `PurchaseRecordProjection.v1`; detail returns the same versioned projection. It includes own manual records without a saved buying-source link or collection/bottle link, through caller-own history or an explicit profile filter. It requires no proposed collection FK. Owner authorization precedes lookup/count/pagination; record/scope/filter/snapshot/rights bind cursors. Hidden/missing/denied records share safe responses. Related catalogue facts remain separately authorized, so an own purchase record is not permission to access a currently hidden profile/source. Known/unknown Money, Quantity, purchase date and seller facts remain manual private assertions, never current live price or order confirmation. Exact history/retention/state visibility, field and numeric/pagination budget policies remain unselected and block execution.

Create/update/withdraw require actor-derived owner, independently authorized optional buying-source link, expected revision/create-absence semantics, principal-bound idempotency and atomic record/history/receipt. Withdrawal requires exact accepted retention policy; it causes no inventory cascade. Purchase records do not automatically create physical bottles, change ordered/cart status or infer ownership. `IF-COLLECTION-WRITE-1` may only include physical remaining quantity/unit, notes and dates after their exact policies are accepted; paid price and purchase history belong to the separate purchase record. Existing manual ordered status remains `IF-PURCHASE-STATUS-WRITE-1`.

Fit explanation and Data Confidence disclosures are UI-local views of already returned authorized `IF-MATCH-EXECUTE-1.output.v1`, not new scoring or capability-as-evidence calls. UI cancellation uses a local abort handle and request-generation invalidation to suppress stale output; server cancellation/rollback/discard is internal cleanup. It is not an `IF-MATCH-VALIDATE-1` cancellation payload or a new logical operation.

The proposed matching output now binds `partitions` to `MatchPartitionProjection.v1` and `unranked` to `MatchResultProjection.v1`. Each result explicitly carries exact method/config IDs and versions, real compatibility context, `MatchPartitionKey.v1` or null, `ExactRational.v1` fit or null, display-only rounded string, `FitExplanation.v1`, `DataConfidenceProjection.v1`, `DirectPairwiseEvidenceProjection.v1` and authorized provenance references. All six new common schemas remain **PROPOSED**; no real weights, formula, confidence bands, evidence thresholds or matching/projection policies are selected. Missing exact policy blocks usable output. Exact ordering precedes rational wire serialization/display rounding inside one compatible partition; null fit never becomes zero and unranked results never acquire a global rank.

`FitExplanation.v1` explicitly includes the exact method/config/compatibility context, authorized matched fact/layer/support references, exact support or unavailable state, safe unavailable reasons, permitted provenance and exact accepted formula-evidence/policy references. This is a projected explanation of the already computed authorized result, not permission to reveal raw source/private locators. Expanding Score Explanation reads the returned result's `fit_explanation` locally. Expanding Data Confidence or Direct Pairwise Evidence reads its separate returned channel locally. None of these disclosure events calls `IF-MATCH-EXECUTE-1` to rescore or `IF-CAPABILITY-READ-1` as if capability were evidence. Unknown evidence remains unknown; structural fit does not manufacture confidence or direct pairwise evidence.

Collection input intentionally does not contain `own_purchase_record_ref`. Its unknown-field policy rejects that field until an explicit accepted field/FK/link policy and contract amendment exist. Receiving or marking an item ordered does not create a purchase record, physical bottle or linkage. Manual Ordered only records its explicit status/time; a separate explicit Record Purchase form would invoke the proposed `IF-PURCHASE-RECORD-WRITE-1` after its exact prerequisites are accepted.

Buying-source commands now explicitly identify create/update/withdraw, own bookmark/create-null, authorized profile binding, changed-field mask, confirmation and expected revision/idempotency/retention policy. `PlatformValue.v1`, `SellerValue.v1`, `Money.v1`, `Quantity.v1`, `ManualDateValue.v1` and `OwnNoteValue.v1` type platform/store/observed price/observed size/observed date/own note. `BuyingSourceProjection.v1` returns the same fields. **Observed** values are not paid purchase facts, live seller facts or physical capacity; unknown does not become zero, today, a currency/unit/platform default or an empty note. All exact field/URL/action/withdraw/retention/bounds policies remain unselected and block the affected operation. No URL is fetched or merchant operation triggered.

Personal-state commands explicitly identify create/move/update/withdraw and actor-owned entry/profile, with target state or explicit null for withdrawal, user confirmation, expected revision, idempotency and exact transition/retention policy. Removal stays unavailable if that policy is absent. It never coerces withdrawal into skipped. `PersonalStateProjection.v1` returns explicit active/withdrawn/state/revision data under the accepted safe visibility policy. Changing/removing personal interest/cart state preserves buying bookmarks, purchase statuses/history and physical inventory.

Physical collection commands explicitly identify create/update/received/finished/sold/gifted/withdraw actions, ownership/lifecycle targets, changed fields and manually known/unknown remaining amount, physical capacity, note and action date. `CollectionProjection.v1` returns those physical fields/history versions without any purchase FK or paid values. Read input explicitly selects list/detail/lifecycle-history/aggregate-drilldown, lifecycle/profile filter, field projection, snapshot, page and prior authorized metric/bucket context. Drilldown reauthorizes its context and underlying rows. A partial item page cannot establish complete brand/note counts or whole-collection aggregates. Exact lifecycle/quantity/unit/capacity/date/retention/drilldown policies remain unselected; no default or cascade is inferred.

Review reading explicitly selects queue/source-detail/proposal-detail/evidence-detail with `ScopedReviewReference.v1`, expected revision, verified scope, snapshot, filters and field projection. `ReviewDetailProjection.v1` contains only separately authorized detail/evidence refs; a returned ref is not permission to dereference it. Authenticate/reviewer-authorize before lookup, filters, counts or pages; no raw staging/private dossier is returned by default. Exact detail/filter/projection policies remain unselected.

OwnPrivateManualProposal in `IF-SOURCE-INTAKE-REQUEST-1` is private missing-perfume metadata; it cannot acquire network data, create canonical records or promote selected facts. Curator acquisition requests retain separate scope, permission and human approval. Private screenshot metadata in `IF-ASSET-INTAKE-REQUEST-1` requests review only; no bytes/intake permission is granted. Earlier AI-assistance/AI-ETL ideas remain future P5-gated work, with no LLM dependency, implicit service or paid call selected by this registry.

The private manual source branch explicitly permits unknown/null source and permission-evidence locators, with `ManualMissingPerfumeProposal.v1` and typed known/unknown `ManualFactValue.v1` assertions. Unknown evidence grants no rights and triggers no capture. The curator branch separately supplies metadata-only method/fields/budget/use/task proposals. Private screenshot metadata is an intake **request kind**, with `asset_kind=null`; it does not classify a canonical asset as a note illustration or bottle photo. Unknown screenshot locators stay explicit metadata unknowns. Accepted discriminated request/bounds policies are still required; no bytes, capture or acquisition are authorized.

Reviewer/rights write contracts are future proposals only. Normal app ownership does not confer curator, reviewer, admin or operator powers. A review UI cannot silently authorize canonical normalization, release44 holds, select Khamrah claims, broaden source uses, acquire images or reverse a revocation. Operational status is a safe dated evidence projection, not a web wrapper over start/migrate/restore/SQL commands.

## Retained architecture review correction

**IR-ARCH-SELF-02 — MEDIUM, design coverage gap:** coordinator cross-matrix review found that R26/R28/R29 purchase-price/volume/date/seller and separate purchase-history requirements were not represented by the original27 logical contracts. Manual bookmark status/time and physical collection ownership/notes/dates could not safely absorb those facts as untyped extra fields. The initial four artifacts and original187-check static report are preserved under local evidence `source/before_purchase_record_refinement/`; those checks did not establish cross-matrix purchase coverage.

Targeted correction adds the coordinator-approved logical identity `IF-PURCHASE-RECORD-WRITE-1`, its input/output schemas and five explicit common field/projection schemas, with separate status PROPOSED. Collection paid-price ambiguity is removed; all exact new field/transition/retention policies remain blocked pending acceptance. This is a documentation design correction, not an accepted implementation or new purchase/data authority. Coordinator evidence records corrected28-interface checks separately from the retained187-check report. Root independent review must verify the cross-matrix requirement mapping before closing the finding; this lane does not self-approve the architecture package.

Final cross-matrix alignment found that the matching output's earlier phrase "ordered real result projections" did not explicitly name the Score Explanation field/type. The corrected201-check artifacts and purchase-history evidence are preserved separately under local `source/before_explanation_projection_refinement/`. The additional six proposed matching projection schemas make the returned explanation, exact compatibility/order and separate evidence channels explicit; logical IF identities remain28. Targeted static checks record this alignment separately from earlier201 checks. No runtime behavior, real contract/weights, paid service or LLM dependency is approved or implemented by this correction.

Independent review then identified a **P2 purchase-history read gap**: the write contract existed, but Personal State Read, Buying Sources Read and Collection Read did not return purchase records or unlinked history. Their source/interface presence could not support the promised purchase-history UI. The213-check artifacts and refinement reports are preserved under local `source/before_purchase_read_refinement/`. The coordinator-approved29th logical identity `IF-PURCHASE-RECORD-READ-1` now explicitly binds caller-own bounded history/detail to `PurchaseRecordProjection.v1`, including records without buying-source or collection linkage. It adds no collection FK, automatic ownership/order transition, network operation or accepted field/retention/budget policy. Targeted author checks are documentation checks only; independent reviewer verification of the corrected cross-matrix read path remains required.

Further independent P2 findings exposed (1) a missing buying-source create/profile/action binding plus omitted platform/observed-size/note fields and (2) missing personal-state withdraw/null/target semantics. Author comparison of **every matrix required-input row against all29 interface schemas** then identified four companion shape gaps: collection actions/capacity/filter/history/drilldown inputs; review detail/evidence/filter/snapshot references; private-screenshot request kind versus asset kind; and unknown locator/evidence handling for private manual missing-perfume proposals. The coordinator explicitly authorized these six documentation corrections without accepting their policies. The227-check artifacts/manifests and prior reports are preserved under `source/before_buying_source_binding_refinement/`. Ten new versioned common projection/value schemas and explicit operation fields close the declared shape gaps; every exact field/action/enum/retention/budget policy remains unselected. Matrix review evidence distinguishes server fields from UI-local selected criteria and navigation/disclosure state; no schema identifier or static count is treated as functional acceptance. Independent review must verify the corrected bindings.

## Preservation and next gate

POST27-ODP-1 remains unchanged at SHA-256`0ccf48fa57401635a3f1b5898f4547978ebdc408e522cd3cc52138f3f341b18c`. New A–I choices remain unapproved. IMP-ENR-01 is **NOT STARTED**;43 proposals/44 holds/Khamrah remain unchanged; PR8 remains **BLOCKED**. The architecture amendment requires exact Human Owner decisions and separate implementation approval. No source/image acquisition, migration/role/session/runtime change, app/API/UI implementation, dependency installation, old receipt rewrite or Production mutation is included.
