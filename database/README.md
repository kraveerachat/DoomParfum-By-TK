# Local PostgreSQL foundation — IMP-P1-01

Approved model: [Planning PR #1](https://github.com/kraveerachat/DoomParfum-By-TK/pull/1), merged at
`bffb2fab1918dc5221a6c5da7920168bcae263ca`. This implementation is a local Draft PR, not production
readiness, deployment, sample ETL or approval to activate application sharing.

## Run on this Windows/Docker Desktop workstation

Requires existing Python 3.11+ and a running local Docker Desktop `desktop-linux` context. No Python
packages, ORM, global tools, host settings, cloud service or provider SDK are installed by the harness.

```powershell
python database/local.py start
python database/local.py migrate
python -m unittest discover -s database/tests -v
python database/local.py status
python database/local.py stop
```

`start` uses PostgreSQL **16.15**, image
`postgres@sha256:f1c3376c26f2609ab9f29f71f824103fe2fcd8ee0346485cb6122a4f93df6f94`.
Container `doomparfum-p1-01`, volume `doomparfum-p1-01-data`, task label `com.doomparfum.task=IMP-P1-01`,
port **127.0.0.1:55431** only. Memory/CPU limits are 768 MiB / 2. No other container is stopped/reset.
The generated development admin password is mounted from ignored `.local/p1-01/postgres-password`;
it is not an argument or logged environment value. Host TCP authentication uses SCRAM. The harness
uses the container's local trusted Unix socket under Docker-admin control. This is a bounded local
test adapter, not evidence of production authentication. Test login roles have no password and cannot
authenticate over TCP; no real user credentials or production connection string exists here.

`dpt_foundation` contains the empty domain schema and field allowlist. Tests recreate only
`dpt_schema_test` and `dpt_migration_probe`, using an exact database allowlist and container/image/
volume/port guards. There is no arbitrary host/database reset option. `stop` retains the disposable
volume for review. Removing that volume is a separate explicit cleanup operation, never a global prune.

## Migration order and recovery

| File | Contents |
|---|---|
| 001_identity.sql | Identity, scopes/membership, entity registry and public vocabularies |
| 002_catalogue.sql | Brand, scent profile, packaging, note, accord and relation identities |
| 003_provenance.sql | Sources/rights/captures, typed claims, selections/conflicts, staging/audit |
| 004_associations_media_personal.sql | Canonical joins, exact asset grants, evidence/matching, private history |
| 005_contract_functions.sql | Scope/claim/reviewer/materialization and immutable evidence validators |
| 006_media_and_deferred_contracts.sql | Asset lineage/use/revocation, final-state triggers and FK indexes |
| 007_security_and_field_contract.sql | RLS/grants/invoker views, fixed field schema; no product seeds |
| 008_coalesced_deferred_validation.sql | Protected per-transaction dirty generations; coalesced complete deferred checks |

There are **47 logical tables in `dpt`**. The separate infrastructure ledger
`dpt_ops.schema_migrations` and `dpt_ops.validation_pending` are not counted as domain tables. `schema_contract.json` maps logical names
to dependency groups. Every migration is transactional and canonical UTF-8/LF checksum-pinned after application; a failed
migration leaves neither its DDL/data nor its ledger entry. Replays are no-ops. Edited applied files
are rejected; use a new migration after merge. Recreate tests provide the disposable reset path;
there is no destructive down-migration interface for a data-bearing database. The unpublished empty
foundation can be recreated only after every non-field-definition domain table is empty and no other
connection exists; that helper refuses data-bearing foundations. Scoped .gitattributes keeps database
source LF across checkouts; external dataset hashes remain byte-exact.

## Trust and enforcement

- Migration admin is isolated. `dpt_owner` is NOLOGIN/non-superuser/non-BYPASSRLS and owns domain tables
  with ENABLE/FORCE RLS. Runtime groups do not own tables or have TRUNCATE/DDL/REFERENCES grants.
- Local identity is authenticated `session_user` → `users.auth_subject`. Mutable GUCs and `SET ROLE`
  do not select another principal. End users have SELECT only; `dpt_writer` is a separate trusted
  transaction capability, withheld from ordinary logins. RLS is also tested under temporary writer
  grants to isolate its WITH CHECK rules. API authorization/error masking remain separate work.
- Scope never widens in place. Scoped composite FKs bind provenance/rights/personal owners; compatible
  catalogue targets are public or exact-same-scope. Private claims about public profiles are overlays.
- Raw staging, public-source captures and sensitive grant evidence are not public-reader data. Public
  invoker views allowlist catalogue/attribution columns. No SQL RPC returns arbitrary protected rows.
- Source captures/claims/audits are append-only. Rights/grants permit only one-way revocation. Raw staging
  payload/key/digest/batch are immutable; retention deletion requires a separately reviewed operation.
- Final-state deferred triggers validate matching subtypes, >=2 conflict members, exact resolution
  membership, scalar/whole-field materialization and mandatory reviewed provenance. Selected scalar
  projection uses a fixed map; raw/source-specific fields cannot become arbitrary executable paths.
- Local cross-row writes serialize through a transaction advisory lock and require READ COMMITTED.
  Repeatable-read writes are rejected. This favors correctness in a small pilot; scale/isolation changes
  need measurement and a reviewed migration. A concurrent conflict-member deletion test checks write skew.
- Image tuple FKs, metadata non-null gates, exact hash/locator, active source AND per-asset uses, parent
  selected permission, same capture/scope, lineage and derivative change/credit/license checks all apply.
  Revocation/parent selection changes invalidate descendants; operation-time checks handle elapsed expiry for every scope. Structural validation of untouched rows
  does not turn an expired private asset into a write outage for another tenant.

## Source occurrences and conservative schema findings

The approved raw files remain outside Git. Tests expect the sibling local package
`DoomParfum Local Data/P1/20261110-221751` and verify every manifest hash. Missing files fail; no substitute
data is generated. The 12/5/58 real-data **shape fixtures** run in test transactions and roll back. They
use explicitly synthetic source/rights records, not claims of actual upstream verification or approved
canonical mappings. Nothing is imported into `dpt_foundation`.

`perfume_notes` remains unique by `(scope,perfume,note,layer)`. Original ordered arrays and individual
locator/key occurrences survive in immutable source claims/staging. Repeated labels, alias ambiguity or
many-to-one mappings must remain review/quarantine with reasons; no silent `DISTINCT`, overwrites,
synthetic weights or guessed notes. See [schema findings](schema_findings.md) for the exact conservative
whole-field format, normalization, validation and output-license contracts.

## Evidence and deferred work

Live tests and coverage are documented in the Obsidian implementation evidence and task note. All
OBS/ACL/IMG/REC specifications have a DB-vs-API/storage/restore breakdown. No HTTP API, cache/export,
object proxy, real image bytes, SSRF/MIME decoder, ETL/importer or independent DB/object restore
is claimed. Shared RLS primitives are tested locally; product-facing shared mode stays disabled.
IMP-P1-02 starts only after Human Owner reviews and merges this implementation PR. Cloud providers,
storage, regional imports and final retention/RPO/RTO remain deferred/blocked as recorded in OD-01..06.

Primary implementation references: [PostgreSQL 16 constraints](https://www.postgresql.org/docs/16/ddl-constraints.html),
[RLS](https://www.postgresql.org/docs/16/ddl-rowsecurity.html),
[safe function execution](https://www.postgresql.org/docs/16/sql-createfunction.html).

All numeric amount/measurement fields reject NaN/infinities; unknowns stay NULL. Direct operations validate the local Docker endpoint each time, not only at start.

## Performance review correction — PR #2

Published migrations001–007 remain unchanged. Additive008 keeps every row constraint trigger and both
complete global validators, coalescing expensive scans once per dirty epoch. Private xid8-keyed state
is dirtied before rows and scheduled after statements; successful validation clears only its generation.
Later writes, failed flushes and savepoint rollback cannot reuse a stale clean flag. No editable GUC or
client-accessible queue is trusted. All original active-rights checks and writer serialization remain.

`python database/performance.py --phase before` / `--phase after` use only disposable dpt_migration_probe
and labeled synthetic fixtures, capped at250 records with45s statement timeouts. Run sequentially with
`python database/verify.py`: both use that probe. Natural-COMMIT evidence in
[evidence/performance_before.json](evidence/performance_before.json) and
[evidence/performance_after.json](evidence/performance_after.json) shows250 INSERT records5.841950s→0.051123s,
500→1 calls each to validate_model/validate_images. Dispatcher callbacks remain O(row events + statements).
One run per case is not a capacity estimate. Full regression79/79 passed; exact source hashes and timings
are in evidence/test_results.json. Full-model scans per dirty epoch, marker MVCC/WAL overhead, deferred
queues and global writer serialization remain limits. Broader IMP-P1-04 capacity/restore work is NOT RUN.

## IMP-P1-02 local licensed intake extension

[SCENTO_ETL.md](SCENTO_ETL.md) documents the separately authorized pinned-source intake, reviewed
private-local exact mappings and strict replay. dpt_scento_test and dpt_scento_pilot are separate
allowlisted targets; only the test DB may be recreated automatically. Original foundation/8migrations/
47-table contract and RLS remain unchanged. Current actual outcomes and not-run boundaries are in
the IMP-P1-02 task/evidence; no search API, matching, images, cloud or production completion is inferred.
