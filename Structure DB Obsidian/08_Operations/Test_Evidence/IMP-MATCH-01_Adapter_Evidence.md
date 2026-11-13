---
id: IMP-MATCH-01-EVIDENCE
project: DoomParfum By TK
type: test_evidence
status: reference-adapter-review-ready
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, matching, tests, security]
source_of_truth: "../../../README.md"
---

# IMP-MATCH-01 — Adapter execution evidence

## Current independent correction closeout — 2026-11-13

Independent reviewer /root/pr11_exact_review, distinct from implementer /root, reviewed corrected
exact checkpoint9be247a5ec724b4c0d057446610b31eacf3bceb2. Final verdict COMPLETED with no blocking
source finding in the authorized trusted-local-transport reference scope. Original report SHA256
ccc1f3b0561177ef65655792f7f65c19242e924e13dd748cc159ed770c53f0f5.
[Independent structured report](../../../database/evidence/matching_input_final_independent_review.json)
and [current correction results](../../../database/evidence/matching_input_review_correction_results.json)
retain exact source, tests, scope and remaining gates. The following19/148test and quota statements
are historical baseline evidence, superseded only for current readiness; none is overwritten.

IR11-01 HIGH was demonstrated using two genuine sessions: old REPEATABLE READ READ ONLY snapshot
returned a revoked SYNTHETIC selected fact, while a fresh session uniformly denied it. Explicit
READ COMMITTED READ ONLY plus isolation gate now rejects incompatible old snapshots. IR11-02 MEDIUM
malformed nested DTOs were demonstrated and fixed: strict schemas/types, qualified required times,
nullable text, internal UUID errors, valid states/layers,512unique bound members and payload bounds.
No migration, RLS/FK/grant, source observation, clock/timestamp guard or actual rights were weakened.
This is not PR8's historical23514diagnosis or a fresh-session RLS bypass claim.

Actual parent tests: RED14offline methods (8failing methods,34failed assertions/7errors) retained;
GREEN14/14PASS; focused28/28PASS35.5s; full157/157PASS178.812s,0failure/error/skip. Main129plus28adapter
methods, including new two-session rights and shared-membership stale-snapshot controls. Original
fixture assertions/mocks and historical failures preserved.22executed source/migration Git bindings
verified; all49persistent pilot data/security/application-role manifests unchanged.

Independent actual execution:14/14offline,8original adversarial cases all now AdapterUnavailable,
6/6live security methods PASS23.594s overall; reviewer verified the157report/raw tails and22Git
bindings, rather than rerunning the full suite. Source SHAe4b4b761e1bcaa64a1ed0c19372545d232ddf5e7626e58666d4ea76edd97ab1b;
test SHA0b16716d7b76b1190434d01e7a7d8c26c3454952df0ba8ab0df8da5696ac74e2.
Docker engine initially offline and a reviewer exception-class harness failure are preserved as
failed instrumentation attempts, not claimed runtime failures or erased observations. Existing
Docker Desktop/task container were started locally, with no installation/config/auth change.

Scoped source acceptance covers the reference adapter and aggregate cohort capability audit only:
all1479private profiles remain ranking-disabled,44holds unchanged, no approved nonadmin application
binding or per-profile app evaluation. DM01–07, accepted closure/absence/normalization, selected
rights/eligibility, app stack/auth/publication and real-data A/B1 remain separate gates. B2 data is
absent. Human Owner alone reviews/merges; no Production change or full application acceptance.

Base aa55f8b59acb0872b3b40273a8cdd25198f3ba27; branch codex/imp-match-01-input-adapter.
Owner-merged PR4 and explicit post-PR4 request authorize this bounded local adapter; DM01–07 remain
PROPOSED. [Guide](../../../database/MATCHING_INPUT.md),
[sanitized results](../../../database/evidence/matching_input_results.json),
[[IMP-MATCH-01_Read_Only_Input_Adapter]], [[Post_PR4_Application_Readiness]].

## Actual tests and protected surfaces

Focused `python .local/run_adapter_tests.py` under common lease:19/19PASS23.516s,0failure/error/skip.
Seven offline methods cover malformed/SQL-injection IDs before transport, uniform denial, unknown
versus empty complete domains, eligibility not authorization, explicit bounds/redacted errors, query
gate ordering and malformed DTOs. Twelve real PostgreSQL methods use explicitly SYNTHETIC private/
shared/public fixtures and genuine logins: admin refusal, private owner selected provenance, other-user
denial, private overlays on public entities, held profiles, automation-right denial, expiry, one-way
rights revocation, shared-member revocation, conflicts, read-only transaction and no catalogue writes.

Full relevant suite `python .local/run_full_adapter_regression.py`:148/148PASS187.078s overall
(184.076s unittest execution),0failures/errors/skips. Main129methods plus19adapter methods.
Existing remote-context/security/FK/RLS/provenance/conflict/materialization/image-rights/ETL/replay/
rollback/concurrency controls remain effective.22source/migration hashes bound to executed code.
No test assertion or original migration/runtime module changed.

Adapter SHA256a33fb8a7ed555a240fb0fd94ac534fc97ec13cc04a57f0bc8f583de5f1ceec46;
test SHA256344272e91d9aaf84bc06de4c6bfa74d047e33a4006e50b859c8e4d11e9d59705.
All49persistent-pilot table manifests, security and application-role metadata equal before/after.
Tests reset only disposable databases, serially under the existing common O_EXCL lease. PR8 lease/
fingerprint tools are test-coordination dependencies only, not imports of the adapter. No new
equivalent timestamp experiment, production operation, benchmark or recovery run.

## Preserved failures and wrapper correction

- Focused00113/13PASS before expanded controls. Focused00218/19PASS: test incorrectly assumed an
  unused BEGIN could not switch to READ ONLY. Corrected test establishes a snapshot first and asserts
  PostgreSQL25001. No runtime relaxation; focused00319/19PASS.
- Full001146/148PASS,2errors: historical local package paths resolve incorrectly from nested worktree.
- Full002145/148PASS,3failing subtests: coordinator's copied module namespace broke existing mocked
  remote-context controls. This was a wrapper defect, not an adapter or security-check relaxation.
- Full003148/148PASS: original local module identity preserved; only ROOT/external SOURCE path
  constants resolve existing external fixtures. Harness/migrations/dictionary byte-equality checked,
  all assertions/mocks retained. Failed results are not overwritten or described as passes.

All six JSON attempt reports and reproducible final wrapper remain external under
08_OUTPUTS_APPROVED/post_PR4/adapter. Raw test/SQL logs remain ignored.local and outside public Git
and the consolidated ZIP. Synthetic baseline timestamps are existing fixture data, not a PR8 fix;
no historical row timestamp, guard, host clock or importer expression changed.

## Cohort capabilities and authorization boundary

Separate genuine operator READ ONLY aggregate audit at2026-11-12T21:54:07.994913Z confirms:
1479private profiles/1435approved/44draft holds/160brands/420notes/11972canonical links,
matching0/pending0/accordlinks0/familylinks0/brandaliases0/notealiases0/comparison evidence0/images0.
Selected note claims:1348top,1348heart,1348base,87general. These are reported memberships, not
accepted completeness domains. This is a bounded inventory audit, not admin candidate-fetch/postfilter.
No raw values or private user identifiers are returned; no publication permission is inferred.

Zero profiles have a bound genuine nonadmin owner-session under current contracts. The operator
binding is an administrator and the application adapter rejects it. Thus aggregate capability is
all1479ranking-disabled; per-profile application evaluation is BLOCKED until a separately reviewed
session/ownership contract exists. No grant/owner reassignment/eligibility flip was made. Ordinary
runtime sessions cannot access public provenance without curatorial policy; unknown output preserves
this gap. No approved closure, alias/family/currentness or compatible accord data is invented.

## Historical baseline review state — before corrected-source closeout

Independent prototype review read actual source and identified read-only transaction, provenance
bounds and DTO-validation concerns; changes were implemented and tested. Final exact-source/test
review is NOT COMPLETE: reviewers hit usage limits with retry07:12local. Self-review is not substituted
for independent acceptance. Keep Draft/ACCEPTANCE PENDING; no final receipt. Remaining gates are
final independent review, approved pilot nonadmin owner/session binding, public-provenance policy,
individual DM choices and selected-field/rights/completeness/eligibility before real matching.

API/UI/scorer/cache/relevance/performance feature acceptance NOT RUN: these do not exist in this
task. No real-data matching, public serializer, framework/auth/provider install or new image/source
acquisition. Common-pattern secret and Markdown checks do not constitute legal approval or a full
security audit. [[Post_PR4_Application_Readiness]] records the Owner matrix and future API tests.
