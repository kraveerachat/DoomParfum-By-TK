---
id: IMP-ENR-01-INDEPENDENT-DATA-REVIEW
project: DoomParfum By TK
type: independent_data_review
status: IN PROGRESS
owner: human-owner
updated: 2026-11-17
tags: [doomparfum, offline-preview, independent-review, provenance]
---

# IMP-ENR-01 independent data review

Reviewer `/root/enr_independent_data_review` is an independent agent assigned under the current Owner master prompt before implementation. This reviewer does not implement the preview and is not an Owner-designated human. Human Owner approval, canonical acceptance, and implementation payload review remain **PENDING**. This is preflight evidence, not a final review or immutable receipt.

The reviewer read the entire current Owner master prompt and the frozen ENR-PINNED-SCENTO-1 revision 1 / POST27-ODP-1 documents. The private helper uses Python standard library only, independently of production implementation. No Git, network, database, Docker, scorer, package installation, source acquisition, or source mutation was performed by this role. Context Mode 2.2.0 and Python 3.11.9 were used; Caveman governs concise chat wording only.

## Verified preflight scope

All six pinned raw byte buffers match exact expected sizes and SHA-256 before CSV parsing: 905307 bytes combined. The same verified buffers supply strict UTF-8 decoding and strict CSV parsing. Pinned provenance revision `086769ecf1add770ea6646bd4d88d39f0e7cddeb` and all six recorded Git blob identities match local raw bytes. This is local provenance verification, not a new network verification of the publisher.

CSV headers exactly match the verified descriptor; row widths, unique nonempty source IDs and populations 1479 perfumes / 160 houses / 420 materials were checked. These are historical source populations, not current Database counts. Selection checks both one-based logical data ordinal and key for exactly five approved records. The baseline contains exactly 46 allowlisted slots, with no linked-record expansion.

Canonical LF-normalized frozen-document hashes match the accepted contract and packet hashes. Checkout CRLF bytes are separately recorded. The coordinator must independently bind canonical Git blob bytes; this role did not run Git.

## Observed field semantics

Exactly three selected slots are MISSING: `perfumes.csv` data ordinal 644 / `year`, ordinal 645 / `year`, and `houses.csv` ordinal 3 / `founded`. The other 43 slots are source-present candidate assertions. No missing value becomes zero, false, known-empty, current year, reviewed time or canonical fact. Selected concentration and alias fields are present; negative tests for missing concentration/aliases therefore require synthetic fixtures.

Selected perfume layer fields contain 12 and 11 ordered occurrences respectively; their general fields contain 12 and 11. Their literal order currently agrees with concatenated layers, but all original field locators must remain separate. Equality does not establish domain closure or permission to reconstruct layers. No repeated token occurs within these selected fields, so repeated-occurrence tests require synthetic fixtures; original occurrences must remain untouched.

The two alias fields contain 10 and 24 literal ordered occurrences. There is no exact stripped-literal overlap between these two alias lists. Neither observation establishes alias equivalence, exhaustive coverage, canonical normalization, taxonomy acceptance, or resolved ambiguity. Canonical identity and perfume editions remain unverified; present concentration does not verify edition identity. House founding is distinct from perfume release year. Raw families, origin, smell and country stay unmapped source assertions, without chemical, accord-strength, ISO or market-coverage inference.

## Rights and protected state

Verified `LICENSE`, descriptor and README assert CC BY 4.0 and attribution **Scento — https://www.scento.com/perfume-database**. The accepted task allows a private offline unselected review transformation only. Source URLs remain inert references. No rights to linked pages, images, live API replication, other revisions, public application publication or unrelated content are inherited. No license URL was fetched.

All six source files, `VERIFIED_SOURCE_PROVENANCE.json` and the three protected audit sidecars have equal before/after byte sizes and SHA-256. Retained projection shows 44 held / 1435 nonheld review-bucket records, 1479 false activation flags, 43 `PROPOSED_NOT_APPROVED` normalization proposals and one separate conflict exclusion. Selected perfumes are in the nonheld bucket with completeness UNKNOWN; that bucket is not a new approval. No hold, normalization, eligibility or current DB state was changed or inferred.

## Pending exact payload review

The private verified-field baseline is `.local/imp-enr-01/data/PINNED_FIELD_BASELINE_PRIVATE.json`, SHA-256 `c1118322d9d40de4d52a263531c4e726f6d8f823fb2eff22d2590d215d3bbda9`. It contains selected literals and must remain ignored/private. Sanitized details and 46 per-locator state/outcome entries are in [[IMP_ENR_01_Independent_Data_Review.json]].

Preflight dossier outcomes: **ACCEPT 0 / REJECT 0 / UNKNOWN 3 / DEFER 43**. Missing assertions are UNKNOWN; source-present claims are deferred pending the exact implementation payload and final semantic review. These are review-dossier outcomes, never automatic reviewer approval, DB selections or normalization decisions.

Next action: receive the exact implementation commit and private payload, independently compare all 46 slots with pinned raw evidence, source-order occurrences, missing-state encoding, provenance identity, allowed fields and rights notices. Record final literal-accuracy and semantic outcomes separately, recheck protected fingerprints, and preserve initial preflight evidence. Human/canonical acceptance remains PENDING regardless of agent review results.
