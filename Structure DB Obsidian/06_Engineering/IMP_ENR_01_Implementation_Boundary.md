---
id: IMP-ENR-01-BOUNDARY
project: DoomParfum By TK
type: implementation_architecture_binding
status: LOCAL VERIFIED
owner: human-owner
updated: 2026-11-17
tags: [doomparfum, scento, offline-preview, provenance]
source_of_truth: "../../README.md"
---

# Implemented offline preview boundary

Source reviewed at `4fdbd29b3f345fcbce3eb08862748672657ef22c`; two new files only: `database/scento_preview.py` and `database/tests/test_scento_preview.py`. Existing runtime/tests, accepted synthetic contracts, eight migrations and25prior receipts are unchanged. No application interface, route, authentication, principal, transport, schema or scorer bridge is implemented. The old architecture inventory is a dated baseline; these two new Python files are an additive offline task, not29implemented APIs.

The module fits the separately approved local operator/review lane (C-SOURCE-CAPTURE/review responsibility), using independent standard-library types rather than future application/transport DTOs. It consumes six existing files and an explicit trusted workspace; no database, ETL helper, matching-input adapter, M1/B1 scorer, HTTP, ORM or driver import. Source sizes/hash/revision precede parsing; exact headers/logical counts/unique keys/ordinal and field allowlists precede transformation. Parser/extractor helpers support synthetic unit controls but cannot supply a caller payload/pin override to the publisher.

## Actual Python functions, not service endpoints

| Function | Actual typed Python signature |
|---|---|
| `load_snapshot` | `load_snapshot(source: Path, revision: str=REVISION) -> Snapshot` |
| `parse_csv` | `parse_csv(name: str, raw: bytes, expected_count: int) -> tuple[dict[str, str], ...]` |
| `parse_snapshot` | `parse_snapshot(snapshot: Snapshot) -> tuple[tuple[str, tuple[dict[str, str], ...]], ...]` |
| `select_records` | `select_records(tables: tuple[tuple[str, tuple[dict[str, str], ...]], ...], selections: tuple[Selection, ...]=SELECTIONS) -> tuple[tuple[Selection, dict[str, str]], ...]` |
| `field_evidence` | `field_evidence(selection: Selection, field: str, raw: str) -> dict` |
| `transform_snapshot` | `transform_snapshot(snapshot: Snapshot) -> dict` |
| `build_preview` | `build_preview(source: Path, revision: str=REVISION) -> dict` |
| `canonical` | `canonical(payload: dict) -> bytes` |
| `payload_hash` | `payload_hash(payload: dict) -> str` |
| `publish_preview` | `publish_preview(source: Path, workspace: Path, *, execution_time: str \| None=None) -> Publication` |
| `rollback_preview` | `rollback_preview(source: Path, workspace: Path, bundle_name: str \| None) -> None` |

## Resource, replay and publication contract

Six valid input files total905307bytes; known CSV populations1479/160/420 and fixed five-record/46-field output bound the accepted workload. Reads check descriptor regular-file status/exact expected size, then read at most expected_size+1 to detect growth and retain complete SHA256/post-length checks. Canonical payload is UTF-8 without BOM, sorted object keys, fixed comma/colon separators, no volatile timestamp, manifest record/field order and original occurrence order. Current exact payload33953bytes/hash16d1d1af8a875d342756b4431da0844eef65787d81de130372250d9a0a387cf9 is an observed pinned result, not a transport request limit or general application default.

Private publication rebuilds from pinned bytes; it accepts no caller-supplied raw payload or expected-pin override. Output is fixed under explicit workspace `.local/imp-enr-01/preview-private`, independently checked Git-ignored for the actual task. Exclusive lock and unique candidates/history prevent concurrent blind overwrites. Files are closed/fsynced and the payload is read back before same-volume active-pointer replacement. Failure before pointer commit preserves previous pointer and sanitized diagnostics where writable; rollback/withdrawal changes only the pointer and retains history. Rollback payload/manifest reads derive exact bounds from rebuilt canonical expected bytes. Execution metadata is separate from source/review time.

Caller supplies a trusted local workspace; an existing `.git` marker is not browser authentication or a general proof of ignore policy. Symlinks/existing Windows reparse points, UNC/traversal paths are rejected. No hostile process replacing directory ancestors during the operation is assumed. Actual symlink/junction creation probes could not execute under workstation permissions, so those native controls are NOT RUN; mock reparse checks and actual Windows sharing-denial/atomic replacement were tested. Crash can retain a fail-closed lock requiring manual inspection; no auto-steal. Post-commit cleanup failure must not be reported as a rolled-back publication. File fsync/atomic replacement do not prove directory-entry durability under machine/power failure. No ACL change, retention policy, public distribution or cloud storage is selected.

## Rights and state boundary

Scento — https://www.scento.com/perfume-database, pinned revision086769ecf1add770ea6646bd4d88d39f0e7cddeb, retained CC BY4.0 metadata and transformation notice apply only to Owner-approved private preview use. Inert source URLs are not fetched; linked pages/images gain no rights. No canonical identity/selection, reviewed source observation, normalization,44-hold release, eligibility or Fit score results. Structural Fit, Data Confidence and pairwise evidence remain separate future authorities. Factual/raw evidence accuracy is not canonical or Human acceptance. Current DB/RLS/session/rights/roles and application functionality NOT VERIFIED; PR8 remains blocked without experiments.

[[IMP_ENR_01_Architecture_Compatibility]] records the completed pre-code compatibility gate; [[IMP_ENR_01_Implementation_Review.json]] records independent closure of the one read-bound P2 at the exact source commit. [[IMP_ENR_01_Offline_Regression.json]] records249fresh offline methods,55preview methods included (not additional249+55),512preview property iterations separately. No live DB or application security acceptance is claimed.
