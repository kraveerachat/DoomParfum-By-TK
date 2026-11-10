---
id: DPT-ENG-005
project: DoomParfum By TK
type: architecture_evaluation
status: proposed
owner: project
updated: 2026-11-10
tags: [doomparfum, planning, storage, recovery]
source_of_truth: "../../README.md"
---

# P1 Storage, Hosting and Recovery Evaluation

All alternatives are PROPOSED. Prices/quotas checked 2026-11-10; USD before taxes. No accounts,
projects, buckets, Docker environment or deployments were created. Verify terms again before provisioning.

## Alternatives and constraints

| Component / alternative | Published allowance or cost | Fit / limitation / proposed decision |
|---|---|---|
| [Vercel Hobby](https://vercel.com/docs/plans/hobby) web application | Free; 100 GB fast transfer, 10 GB origin transfer, 1M CDN requests, 1M function invocations, 4 CPU-hours, 360 GB-hours memory monthly | Personal noncommercial restriction; application authentication still required; evaluate for web/API only |
| [Supabase Free](https://supabase.com/pricing) PostgreSQL + Storage | 500 MB DB, 1 GB files, 5 GB uncached plus separate 5 GB cached egress; two active projects; pauses after one week inactivity | Small pilot candidate; index/provenance/staging overhead counts; free image transformations unavailable per billing docs |
| Supabase Pro | From $25/month; 8 GB DB disk, 100 GB storage, 250 GB each cached/uncached egress; daily DB backups retained 7 days | Paid capacity option, not authorized; additional compute/projects/add-ons can change bill |
| [Cloudflare R2 Standard](https://developers.cloudflare.com/r2/pricing/) objects | Free 10 GB-month, 1M Class A and 10M Class B operations/month; internet egress free; beyond allowance $0.015/GB-month, $4.50/M A, $0.36/M B | Separate provider/account/access controls; object operations cost even with free egress; no free tier for Infrequent Access |
| Supabase Storage | Same project access model, signed URLs and fewer services to operate | Simpler initial private asset integration; smaller free file allowance and egress accounting; backup bytes separately |
| R2 Storage | Portable S3-compatible object access and larger published free allowance | Extra auth/signing/manifest/backup integration; S3 compatibility is not full feature equivalence |
| Python ETL worker | No hosting service selected or free runtime assumed | Local manual job first; later bounded container/job host. Keep long ETL separate from web request lifetimes |
| Docker server / self-hosted PostgreSQL and objects | No included free cloud allowance; server/disks/network/operations cost UNKNOWN | Maximum operator control and export target; owner handles TLS, patching, monitoring, backup and availability |

Further primary references: [Supabase billing](https://supabase.com/docs/guides/platform/billing-on-supabase),
[egress accounting](https://supabase.com/docs/guides/platform/manage-your-usage/egress),
[Vercel terms](https://vercel.com/legal/terms), [R2 S3 compatibility](https://developers.cloudflare.com/r2/api/s3/api/).
Regions, actual network latency, payment-method requirements, connection caps and worker compute prices
were not measured/settled. No free-tier guarantee or approval to spend is implied.

PROPOSED decision path: local PostgreSQL pilot first; Supabase PostgreSQL candidate after measured size
and restore checks. Choose Supabase Storage for operational simplicity if measured images/egress fit;
choose R2 if measured storage/traffic justify the second integration. Docker remains the exit path.
Do not create empty provider projects merely to evaluate this plan.

## Capacity model — assumptions, not benchmark results

The observed perfume JSONL is 1.21 MB; this is not PostgreSQL size. Heap/TOAST, joins, UUIDs, indexes,
field claims, staging history and provider overhead must be measured separately.

| Hypothetical workload | Arithmetic / implication |
|---|---|
| 1,500 bottle originals at 300 KB each | 450 MB before derivatives/versions/backups |
| 420 shared note illustrations at 100 KB each | 42 MB; reference same asset rather than duplicate per perfume |
| Three stored renditions equal to original size, illustrative upper planning assumption | Total originals + two renditions ≈ 1.476 GB for the above assets, exceeds 1 GB allowance |
| 10,000 monthly image views at 200 KB | ≈ 2 GB delivered bytes, excludes API/web traffic and cache behavior |

These are decimal units and explicit assumptions, not acquired-image measurements. Do not extrapolate
row-count capacity from raw JSON bytes. Future benchmark records heap/index/TOAST/total DB, staged and
canonical bytes, object originals/derivatives, requests and cached/uncached transfer separately.
Proposed alerts: 70% of chosen allowance; pause further import at 85% until reviewed. Owner must approve
thresholds and budget. A provider's quotas do not enforce this application's spending policy by themselves.

## Separate backup contracts

Database export contains catalogue, provenance, rights, tenant records, migrations and object metadata.
Image/object backup contains the actual bytes plus manifest. [Supabase backup documentation](https://supabase.com/docs/guides/platform/backups)
explicitly excludes Storage API object bytes from database backups. Neither cache nor second URL is a backup.

PROPOSED initial targets: daily encrypted DB logical export and object incrementals; 7 daily + 4 weekly
copies outside the primary failure domain; RPO ≤24 hours and rehearsal RTO ≤2 hours for the pilot scale.
These targets/retention are awaiting owner approval and have not been achieved/tested. Shorter source
retention/privacy requirements take precedence. Private exports and keys never enter public Git.

## PostgreSQL/Docker export and restore plan — future execution only

1. Quiesce writes or establish a common backup boundary; record schema revision, PostgreSQL/client
   version, extensions/collations, row counts and selected-claim IDs. Dump the core app schema/data with
   `pg_dump` custom archive format and retain warnings. [PostgreSQL dump guidance](https://www.postgresql.org/docs/current/app-pgdump.html).
2. Record role/privilege mapping separately. Provider-managed auth/storage schemas are adapters, not
   portable domain requirements. Export app-user/auth-subject mapping securely; plan reauthentication
   and replacement RLS helper functions before leaving Supabase. Do not assume password/session portability.
3. Export each required object via permitted object API to an encrypted independent destination.
   Manifest includes provider/bucket/key, source/rights/attribution, exact byte size, MIME, dimensions,
   SHA-256 and derivative ancestry. Record absent/restricted objects explicitly; no secret signed URLs.
4. Restore the archive with `pg_restore` into an empty disposable PostgreSQL container compatible with
   the source major version; remap roles/ownership, install required extensions, apply migrations and
   authorization policies. Validate before considering a different major version; no downgrade assumption.
5. Restore objects to a separate test bucket or local object service. Verify every manifest hash/size,
   asset relation, access restriction and attribution. Missing/corrupt object must fail the rehearsal.
6. Reconcile counts, FKs, canonical selections, conflict/missing states, purchase history, tenant access
   and authorized image-proxy delivery. Measure recovery time; retain evidence and restore manifest privately.
7. Production cutover requires a separate owner-approved bounded plan, final sync, smoke checks and
   rollback to old DB/bucket. No destructive cutover, credential migration or cloud operation is authorized here.

Rollback for local pilot: discard only its disposable DB/test objects after verified export; preserve
approved records/evidence. Never treat dropping a real hosted schema as a routine rollback.
See [[P1_Pilot_Implementation_Plan]] for acceptance and [[Tech_Stack_and_ADRs]] for proposed ADRs.


Post-review restore boundary: manifests include access_scope_id, exact asset/capture/assessment/permission
IDs, locator/hash and parent permission lineage. Restore validates source/selection/conflict scopes and
RLS/membership/rights before serving data or bytes. Public-only exports exclude private/shared claims
and metadata; DB/object backup copies stay restricted. No cloud resource is approved; OD-01..06 owner
recommendations distinguish local tests, blocked source rights and separately approved provisioning.
