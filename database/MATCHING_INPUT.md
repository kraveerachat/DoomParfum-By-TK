# Local read-only matching input adapter

`matching_input.py` is a Python standard-library reference adapter over the merged PostgreSQL
contracts. It implements no scorer, API, application authentication, public serializer or cache.
Python here is an existing local test/runtime tool, not an accepted web stack decision.

Current correction version is `matching-input-local-v2`. Independent exact-source review demonstrated
that a reused REPEATABLE READ READ ONLY snapshot could retain revoked synthetic rights despite the
transport's documented fresh-transaction requirement. The script now explicitly requests READ
COMMITTED READ ONLY and checks both settings before catalogue access. An incompatible used snapshot
fails rather than returning stale facts. This is a demonstrated adapter correction, not a change
to migration005's historical timestamp guard or a proposed fix for PR8's unrelated23514failure.

Call `read_profile(trusted_execute, canonical_uuid)` only through a trusted transport that executes
the entire generated script on one genuine authenticated connection, stops at the first error and
returns the single JSON object. Never inject a request-supplied transport/SQL, set a role/GUC to
impersonate someone, retry as administrator, or reuse the connection inside an existing transaction.
The script starts READ ONLY, checks real session/current principal, rejects superuser/BYPASSRLS/
owner membership and role changes before reading the catalogue, and relies on existing RLS.

The adapter reads one authorized identity. It selects only effective, same-entity-scope canonical
fields and matching source captures; a private overlay on a public entity is not public provenance.
Storage, display and automation permissions, permission evidence, expiry and revocation are checked
before projecting selected values. It never reads raw staging or chooses a newer/conflicting claim.
Relevant open conflicts withhold values and provenance. Unreviewed profiles return no fact values.
Revocation/expiry may hide the identity through RLS: missing and unauthorized are uniformly unavailable.

Selected scalars and canonical note memberships carry internal observation/capture/locator/transform/
revision/hash, publisher and rights/attribution provenance. This is private internal metadata, not a
publication authorization. Reported note arrays are used only to check exact ordered membership;
raw labels are not returned. No accepted complete-as-reported closure exists, so even a matching
reported list is known-incomplete. Absent lists, inaccessible vocabulary and ambiguous membership
are unknown, never proof of absence. No alias equivalence, family taxonomy, accord presence/strength,
lifecycle, confidence or pair evidence is inferred.

States are known-usable, known-incomplete, unknown, conflicted/held, rights-unavailable and
eligibility-unavailable. Even a database eligibility boolean cannot enable ranking: `ranking_allowed`
is always false pending the remaining decision/data/application gates. All real 1479 flags and44holds
are unchanged. Similarity, confidence and pairwise evidence remain separate future contracts.

## Bounds and current compatibility gaps

One exact UUID only; no enumeration/count/pagination endpoint. A deterministic513-row lookahead
rejects more than512 note links. Selected payloads are at most64KiB, variable provenance strings
8KiB and serialized transport output2MiB. Oversized/unusable fields become unknown; relationship/
response overflow fails explicitly. These are local defensive limits, not accepted search-query
caps. SQL timeouts are3s statement/1s lock; a used read/write transaction cannot be adopted.

The decoder independently enforces exact nested object keys, allowed field states/layers, canonical
internal UUIDs, required qualified review/rights timestamps, nullable text types, per-payload and
provenance bounds,512members and unique bound memberships. Malformed internal data raises uniform
AdapterUnavailable; missing/unauthorized profiles retain InputUnavailable. rights usage_scope is
free-form nonempty text under the schema, not an invented enum. The trusted transport must still
open a fresh genuine session/transaction and enforce its wire-size boundary; no API caller may
provide that callback. READ COMMITTED revalidates each statement snapshot, not revocations committed
after that statement's snapshot was established. A later request must reauthorize again.

Current RLS exposes public provenance to curators, not ordinary runtime sessions. Ordinary sessions
may see a public identity with all selected fields unknown. The adapter does not expand permissions
to hide this gap. Curator membership still cannot read another user's private scope. The persistent
Scento pilot is operator-private with a PostgreSQL administrator binding; that binding is rejected
for application reads. Do not reassign its owner or grant application access to manufacture readiness.

The separate operator-only aggregate cohort audit is an inventory/capability diagnostic, not an
administrator fetch followed by application filtering. No per-profile application capability claim
is made without an approved nonadministrator owner/session contract. No anonymous/public search
or sharing of this local catalogue is authorized.

## Verification

Focused tests: `python -m unittest discover -s database/tests -p test_matching_input.py`.
They use explicitly SYNTHETIC records and genuine test login sessions. Integration resets only
`dpt_schema_test`; run under the common exclusive PostgreSQL lease, with no other DB task running.
The executed wrapper, fixture resolution, source hashes and results are retained in the external
handoff; it uses existing PR8 tooling only for test coordination, never as an adapter dependency.
Do not run database tests on the persistent pilot or Production.

See [current correction evidence](evidence/matching_input_review_correction_results.json), the
preserved [historical baseline](evidence/matching_input_results.json) and the Obsidian
[task](../Structure%20DB%20Obsidian/07_Delivery/Tasks/IMP-MATCH-01_Read_Only_Input_Adapter.md).
Final independent source review completed at9be247a5ec724b4c0d057446610b31eacf3bceb2 after both
demonstrated findings were fixed.28focused and157full methods pass; the reviewer independently
passed14offline and6live methods plus all8original malformed cases. Historical pending-review,
failed probes and test attempts remain preserved. One scoped reference-adapter receipt records the
closeout after documentation checks; real application/session/closure/DM/publication gates remain separate.
