---
id: DPT-PLAN-006-SPEC
project: DoomParfum By TK
type: planning_specification
status: proposed
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, planning, adapters, media, rights]
source_of_truth: "../../README.md"
---

# Incremental sources and media intake — Planning Gate

This docs-only proposal addresses Workstream G. It creates no adapter, schema, image acquisition,
permission, normalization, catalogue promotion or public UI. Owner merge of this plan is required
before implementation; each concrete source/use also needs usable permission and its own bounded
task. [[Catalogue_Coverage_and_Acquisition_Readiness]] supplies actual coverage rather than a claim
that the intended application already has enough data. [[Source_Acquisition_Permission_Research]]
records current candidate terms and unresolved rights. Existing approved migrations remain exact.

## Intake and field-selection architecture

1. **Proposal:** state target gaps, exact identity/edition, source/version, fields, audience and
   operations. Obtain source-specific permission evidence and Owner task approval. Unknown means stop.
2. **Isolated capture:** only the approved method, bounded request/rate/byte budget and local path
   outside public Git. Record source URI, revision/hash/time, response/capture hash, schema version,
   rights evidence/version and access scope. Never send private catalogue/cart/account data upstream.
3. **Immutable claims:** preserve original string/array/order/repeated notes and section/field
   locators. Distinct prose and structured claims remain independently addressable. New transforms
   have versioned lineage rather than overwriting original observations or source-exact selections.
4. **Review quarantine:** resolve identity/edition ambiguities, aliases, field conflicts, vocabulary
   mappings and rights per intended operation. Do not auto-merge by brand/name or similarity score.
   All44existing holds,43sidecars and Khamrah remain unchanged until their separate decisions/tests.
5. **Explicit selection:** future approved implementation checks selection/entity/scope/source/field/
   materialization consistency and active use-specific rights atomically. Missing rights, a relevant
   conflict or unsupported transform rejects promotion. No source wins merely by being newer.
6. **Eligibility:** an approved canonical field is not proof of completeness, absence or matching
   eligibility. Re-evaluate separately under the accepted method, selected fields, closure and
   nonadmin application binding. Actual accords need compatible reviewed strength/taxonomy data.
7. **Updates:** retain captures/decisions/version lineage and inspect deltas before reselection.
   Revocation stops the affected operations. Retry/replay is idempotent by exact capture/claim/asset
   identity and must not create duplicate source/canonical records. Never silently replace history.

This is a validation contract for later implementation, not a new migration. Reuse and review the
existing source/scope/claim/selection/image/permission contracts before proposing any amendment.

## Rights-gated media workflow

Bottle photos and ingredient illustrations are different assets. A note illustration is an
illustrative aid, never evidence of chemical composition. An image match cannot establish perfume
edition identity. Own photographs require actual authorship and other-rights review; purchased
perfume ownership is insufficient.

| Stage | Required record / behavior | Reject or hold |
|---|---|---|
| Asset proposal | exact source record/capture, asset locator/file revision, creator/rights holder, intended perfume edition or canonical note and private scope | unrelated source-wide license, thumbnail alone, ambiguous edition, private source attached to public entity |
| Permission | per-asset evidence bound to the same source/capture/asset, allowed operations/audience/expiry and derivative conditions | missing, unrelated, unknown, expired/revoked or incompatible permissions |
| Local capture | bounded permitted retrieval outside public Git; content SHA256, byte length, sniffed MIME, dimensions and retrieval time | URL/MIME mismatch, oversized/decompression bomb, malformed/active payload, unsafe redirect or unsupported format |
| Normalization | explicitly permitted derivative, separate new hash/asset and parent lineage, crop/resize/metadata-strip log | derivative prohibited or lineage missing; metadata stripping cannot erase required attribution |
| Binding/review | exact entity/edition or note binding; source-record/rights consistency, access-scope FK/RLS and human review | rights from another source or asset, cross-tenant link, unresolved entity/asset claim |
| Private delivery | only after separate application gate; authorization and active rights checked before bytes or metadata, scoped opaque identifiers, required credit | public bucket/path, direct upstream hotlink without permission, guessed asset existence, shared cache/private URL leakage |
| Revocation/replacement | deny later access, invalidate all derivative/cache references and tombstone links; preserve permitted audit metadata and disposition evidence | deleted history without lineage, reusing revoked bytes under a different name or reactivating parent-derived assets |

**Proposed initial format policy:** original permitted JPEG/PNG/WebP raster files only, sniffing and
decoding required. Defer SVG, animated formats, PDF, HTML and archives; unsupported means quarantine,
not transcoding without permission. Exact compressed-byte, decoded-pixel, dimension and request
limits require a bounded implementation specification and Owner review. No limits or decoder are
installed here. Keep original permitted bytes separate from derivatives; preserve ICC/orientation
handling without exposing EXIF location or private capture paths. No AI service or paid asset tool.

Each derivative inherits a permission ceiling from its parent and needs independently permitted
transformation/display uses. A permissive child record cannot override a revoked or restricted
parent. Required creator/title/source/license/version/change notices must survive UI delivery;
attribution itself must not expose a private source URL to another user. If required public credit
and privacy cannot both be satisfied, do not serve that asset in the proposed audience.

Storage design remains portable: opaque local object key and content hash, no provider-specific
public URL as identity; separate metadata and bytes; private storage and manifests; rights-aware
backup and restore. Restore must re-evaluate current revocation before serving old objects.
Retention, external backup, RPO/RTO, cloud provider and public CDN need separate Owner approval.
No storage path, bucket, worker, queue, route or cloud resource is provisioned by this plan.

## Proposed incremental tasks and gates

All following tasks are **PROPOSED / NOT STARTED**, with no fabricated task acceptance or runtime.

| Future task | Prerequisites | Bounded deliverable / exit |
|---|---|---|
| Source dossier and sample | this Planning PR merged; exact publisher/method/use permission | approved sample outside Git with revision/hash/rights and mapping/coverage report; no promotion |
| One source adapter | sample usable; source grant; approved task and request budget | local capture + validation, deterministic replay/rollback/error tests, no automatic canonical selection |
| Reviewer normalization/selection | explicit closure/normalization/identity decisions and permission | versioned derived claims and reviewed selections; all original observations/holds preserved unless individually resolved |
| Metadata-only media intake | approved per-asset rights and exact source binding | validate synthetic then permissioned metadata/bytes in isolated local task; negative cross-source/tenant/expiry tests |
| Local derivative/restore | transformation/storage/retention permission and bounded implementation task | hash/parent/rights manifests, revocation/replacement/backup restore tests; private only |
| Private delivery integration | accepted stack/session/private-public contracts and genuine nonadmin tests | separately reviewed authorized bytes/DTO path and cache policy; no public publication |

Recommended first decision is a small permission/sample investigation for identifiers and missing
regional metadata, plus a separately bounded per-file ingredient illustration dossier. This is a
recommendation only. Do not use the live Scento API to wholesale rebuild the catalogue, assume
Wikidata links confer image rights, or acquire15existing blocked media candidates.

## Acceptance specifications — NOT RUN

| ID | Required future result |
|---|---|
| SG01 | unsupported source/use or unknown permission prevents requests; source denial never triggers bypass |
| SG02 | same-name different edition and ambiguous brand stay separate; invalid mapping never overwrites claims |
| SG03 | structured/prose/repeated-note occurrences remain addressable with versioned locators and transform lineage |
| SG04 | replay adds zero canonical/source/asset duplicates; failed batch/rollback leaves inventory unchanged |
| SG05 | rights record from another source/asset/capture fails; expired/revoked/unknown use fails at operation time |
| SG06 | private source/asset linked to public catalogue entity remains private; second-user, revoked-member and anonymous reads reveal neither bytes nor existence/counts |
| SG07 | malformed MIME/redirect/oversized or active file is quarantined before decode/storage/display |
| SG08 | disallowed derivative and detached parent fail; crop/resize credit/change notices remain correct |
| SG09 | parent revocation disables every descendant/cache/old restored copy before later display |
| SG10 | required attribution is present without private URL leakage; incompatible credit/audience blocks delivery |
| SG11 | no invented accord strength, complete-empty layer, lifecycle/current stock or Dupe evidence is synthesized |
| SG12 | hold44, matching0 and original migrations/receipts remain exact during research/sample-only tasks |
| SG13 | new source update preserves old hash/revision/decisions, isolates conflicts and requires re-review |
| SG14 | private backup/restore retains hashes/bindings and reapplies current rights; no orphan/externally public object |

## Owner review choices

- Approve, modify or defer this plan's source-dossier and media validation design; approval is not
  granted until an explicit Owner decision and applicable merge are verified.
- Name the exact first source, fields, sample budget, audience and operations. Resolve terms first.
- Decide per-asset acceptable licenses/derivatives/attribution and private publication boundary.
- Keep paid feeds, accounts, cloud/external backups/public endpoints as separate explicit approvals.

No choice pre-approves a normalization policy or resolves44holds. Structural fit, Data Confidence
and documented pair evidence remain distinct. Sufficient data for a reviewed local source-exact
catalogue audit does not imply sufficient data/media/rights for the intended private application.
