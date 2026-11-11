"""Focused IMP-P1-03 checks. DB mode requires the coordinator's exclusive window."""
import argparse
import datetime
import hashlib
import io
import json
from pathlib import Path
import sys
import time
import unittest

import local

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "database/tests"))

# These original tests exercise actual SQL bindings/ancestry/privacy, rather than
# a second Python implementation of the same rights rules. They use dpt_schema_test.
FOUNDATION_IMAGE_TESTS = (
    "test_img01_exact_capture_asset_assessment_binding",
    "test_img02_metadata_allowed_acquisition_missing_permission_rejected",
    "test_img03_derivative_exact_parent_and_output_obligations",
    "test_img04_hash_locator_and_immutable_capture",
    "test_img05_revocation_descendants_and_expiry_operation_gate",
    "test_img06_public_link_cannot_reference_private_asset",
    "test_image_cycle_rejected",
    "test_null_image_mime_cannot_bypass_acquired_state",
    "test_expiry_is_rechecked_after_clock_passes",
    "test_parent_selected_permission_change_invalidates_derivative",
    "test_same_source_different_capture_permission_rejected",
    "test_two_row_image_cycle_fails_deferred_lineage_validation",
    "test_expired_private_asset_does_not_block_unrelated_user_write",
)


def collect(suite):
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from collect(test)
        else:
            yield test.id()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--include-db", action="store_true", help="Use only disposable dpt_schema_test; run sequentially")
    args = parser.parse_args()
    loader = unittest.TestLoader()
    suite = unittest.TestSuite([loader.loadTestsFromName("test_image_validation.ImageOfflineTests")])
    if args.include_db:
        suite.addTests(loader.loadTestsFromName("test_image_validation.ImageDatabaseTests"))
        for name in FOUNDATION_IMAGE_TESTS:
            suite.addTests(loader.loadTestsFromName("test_foundation.FoundationTests." + name))
    ids = list(collect(suite))
    stream = io.StringIO(); started = time.monotonic()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    state = ROOT / ".local/image-rights"
    state.mkdir(parents=True, exist_ok=True)
    (state / ("db_test_output.log" if args.include_db else "offline_test_output.log")).write_text(stream.getvalue(), encoding="utf-8")
    print(stream.getvalue())
    sources = ["database/image_validation.py", "database/verify_images.py", "database/local.py",
               "database/tests/test_image_validation.py", "database/tests/test_foundation.py", "database/tests/fixtures.py"]
    sources += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT / "database/migrations").glob("*.sql"))]
    report = dict(task="IMP-P1-03", checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        command="python database/verify_images.py" + (" --include-db" if args.include_db else ""),
        python_version=sys.version, python_executable=sys.executable, database="dpt_schema_test" if args.include_db else "NOT RUN",
        container_image=local.IMAGE if args.include_db else "NOT USED", tests_run=result.testsRun,
        passed=result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped),
        failed=len(result.failures), errors=len(result.errors), skipped=len(result.skipped),
        seconds=round(time.monotonic()-started, 3), exit_code=0 if result.wasSuccessful() else 1,
        test_ids=ids, source_file_sha256={s:hashlib.sha256((ROOT / s).read_bytes()).hexdigest() for s in sources},
        fixtures="Only agent-authored SYNTHETIC in-memory RGB/RGBA PNGs and original synthetic DB grants; not real assets or permissions.",
        real_image_assets_acquired=0, catalogue_images_registered=0, source_permissions_obtained=0,
        not_run=["Third-party image acquisition", "HTTP fetching/SSRF/redirect/decoder service", "JPEG/WebP/AVIF/SVG/GIF support",
                 "Provider storage/proxy/signed URLs/cache", "Image restore/capacity", "App API/UI/build/E2E", "Production or cloud"])
    if result.wasSuccessful():
        out = ROOT / "database/evidence"
        name = "image_test_results.json" if args.include_db else "image_offline_results.json"
        temp = out / (name + ".tmp")
        temp.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        temp.replace(out / name)
    print(json.dumps({k:report[k] for k in ("tests_run", "passed", "failed", "errors", "skipped", "seconds", "exit_code")}))
    return report["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
