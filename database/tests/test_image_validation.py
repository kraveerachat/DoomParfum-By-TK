"""Owned SYNTHETIC in-memory PNGs; never real catalogue/media coverage.

Offline tests do not need Docker. ImageDatabaseTests use only dpt_schema_test;
run them only in the coordinator's granted, exclusive DB window.
"""
import dataclasses
import hashlib
from pathlib import Path
import struct
import sys
import time
import unittest
from unittest.mock import Mock, patch
import zlib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import image_validation as images
import local
from fixtures import baseline, image, q, uid


def chunk(kind, payload=b""):
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff)


def synthetic_png(width=2, height=3, colour=2, *, raw=None, extra=b"", compressed=None):
    """Agent-authored RGB/RGBA pixels, no acquired photograph/illustration."""
    channels = 4 if colour == 6 else 3
    if raw is None:
        raw = (b"\0" + bytes([37, 83, 149, 255][:channels]) * width) * height
    packed = zlib.compress(raw) if compressed is None else compressed
    return (images.SIGNATURE + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, colour, 0, 0, 0))
            + extra + chunk(b"IDAT", packed) + chunk(b"IEND"))


class ImageOfflineTests(unittest.TestCase):
    def test_owned_rgb_and_rgba_exact_metadata(self):
        for colour in (2, 6):
            with self.subTest(colour=colour):
                data = synthetic_png(colour=colour)
                result = images.inspect_png(data)
                self.assertEqual(dataclasses.asdict(result), dict(mime_type="image/png", byte_size=len(data),
                    width=2, height=3, sha256=hashlib.sha256(data).hexdigest()))

    def test_multiple_idat_chunks_are_supported(self):
        data = synthetic_png()
        compressed = zlib.compress((b"\0" + b"\x01\x02\x03" * 2) * 3)
        header = data[:33]
        result = images.inspect_png(header + chunk(b"IDAT", compressed[:3]) + chunk(b"IDAT", compressed[3:]) + chunk(b"IEND"))
        self.assertEqual((result.width, result.height), (2, 3))

    def test_valid_scanline_filter_codes(self):
        for code in range(5):
            with self.subTest(code=code):
                self.assertEqual(images.inspect_png(synthetic_png(1, 1, raw=bytes([code, 1, 2, 3]))).width, 1)

    def test_nonbytes_empty_and_byte_limit(self):
        for data in (None, "PNG", bytearray(synthetic_png()), b"", synthetic_png()):
            with self.subTest(kind=type(data).__name__):
                with self.assertRaises(images.ImageRejected):
                    images.inspect_png(data, images.Limits(max_bytes=10))

    def test_jpeg_webp_avif_svg_gif_and_spoofed_suffix_bytes_rejected(self):
        for content in (b"\xff\xd8\xff", b"RIFF0000WEBP", b"ftypavif", b"<svg/>", b"GIF89a", b"not an image.png"):
            with self.subTest(content=content):
                with self.assertRaises(images.ImageRejected): images.inspect_png(content)

    def test_crc_corruption_rejected(self):
        data = bytearray(synthetic_png()); data[-1] ^= 1
        with self.assertRaisesRegex(images.ImageRejected, "checksum"): images.inspect_png(bytes(data))

    def test_truncated_headers_chunks_and_missing_end_rejected(self):
        data = synthetic_png()
        for length in (8, 12, 20, 32, len(data)-12, len(data)-1):
            with self.subTest(length=length):
                with self.assertRaises(images.ImageRejected): images.inspect_png(data[:length])

    def test_large_chunk_length_cannot_overrun_input(self):
        with self.assertRaisesRegex(images.ImageRejected, "length"):
            images.inspect_png(images.SIGNATURE + struct.pack(">I", 0x7fffffff) + b"IHDR" + b"\0" * 13)

    def test_duplicate_or_absent_header_rejected(self):
        data = synthetic_png()
        for bad in (images.SIGNATURE + chunk(b"IDAT", b"a") + chunk(b"IEND"), data[:33] + data[8:33] + data[33:]):
            with self.subTest(bad=bad):
                with self.assertRaises(images.ImageRejected): images.inspect_png(bad)

    def test_ancillary_metadata_animation_unknown_chunks_rejected(self):
        for kind in (b"eXIf", b"tEXt", b"iCCP", b"acTL", b"PLTE", b"ABCD"):
            with self.subTest(kind=kind):
                with self.assertRaisesRegex(images.ImageRejected, "chunk"):
                    images.inspect_png(synthetic_png(extra=chunk(kind, b"SYNTHETIC private marker")))

    def test_unsupported_depth_palette_and_interlace_rejected(self):
        for depth, colour, compression, filtering, interlace in ((16, 2, 0, 0, 0), (8, 3, 0, 0, 0),
                (8, 2, 0, 0, 1), (8, 2, 1, 0, 0), (8, 2, 0, 1, 0)):
            with self.subTest(options=(depth, colour, compression, filtering, interlace)):
                bad = images.SIGNATURE + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, depth, colour, compression, filtering, interlace))
                with self.assertRaises(images.ImageRejected): images.inspect_png(bad + chunk(b"IDAT") + chunk(b"IEND"))

    def test_dimension_pixel_and_decoded_limits_precede_decompression(self):
        for data, limits in ((synthetic_png(0, 1), images.Limits()), (synthetic_png(3, 1), images.Limits(max_width=2)),
                (synthetic_png(1, 3), images.Limits(max_height=2)), (synthetic_png(), images.Limits(max_pixels=5)),
                (synthetic_png(), images.Limits(max_decoded_bytes=20))):
            with self.subTest(limits=limits), patch.object(images.zlib, "decompressobj") as decoder:
                with self.assertRaises(images.ImageRejected): images.inspect_png(data, limits)
                decoder.assert_not_called()

    def test_decoded_bomb_and_long_or_short_rows_rejected(self):
        for raw in (b"\0", b"\0" * 8, b"\0" * 1_000_000):
            with self.subTest(length=len(raw)):
                with self.assertRaisesRegex(images.ImageRejected, "decoded"):
                    images.inspect_png(synthetic_png(1, 1, raw=raw))

    def test_bad_filter_or_zlib_checksum_or_trailing_stream_rejected(self):
        for data in (synthetic_png(1, 1, raw=b"\x05abc"), synthetic_png(compressed=b"not zlib"),
                synthetic_png(compressed=zlib.compress(b"\0" * 21) + zlib.compress(b"extra")),
                synthetic_png(compressed=zlib.compress(b"\0" * 21)[:-1])):
            with self.subTest(data=data):
                with self.assertRaises(images.ImageRejected): images.inspect_png(data)

    def test_trailing_bytes_and_nonempty_end_rejected(self):
        data = synthetic_png()
        for bad in (data+b"<script>", data[:-12]+chunk(b"IEND", b"extra")):
            with self.subTest(bad=bad):
                with self.assertRaises(images.ImageRejected): images.inspect_png(bad)

    def test_chunk_count_limit(self):
        with self.assertRaises(images.ImageRejected): images.inspect_png(synthetic_png(), images.Limits(max_chunks=2))

    def test_limits_reject_zero_negative_bool_or_noninteger(self):
        for value in (0, -1, True, "100", 3.5):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): images.Limits(max_bytes=value)

    def test_denied_unknown_operation_or_malformed_id_never_calls_loader(self):
        for value in ("not-a-uuid", "' OR true --", None):
            loader = Mock()
            with self.subTest(value=value), patch.object(images.local, "sql") as sql:
                with self.assertRaises(images.ImageRejected):
                    images.validate_registered_asset(value, loader, operation="display", db="dpt_schema_test", user="dpt_test_alice")
                loader.assert_not_called(); sql.assert_not_called()
        for operation in ("render", "display');SELECT 1;--"):
            with self.subTest(operation=operation), patch.object(images.local, "sql") as sql:
                with self.assertRaises(images.ImageRejected):
                    images.validate_registered_asset(uid("x"), Mock(), operation=operation, db="dpt_schema_test", user="dpt_test_alice")
                sql.assert_not_called()

    def test_disallowed_database_never_calls_sql_or_loader(self):
        with patch.object(images.local, "sql") as sql:
            with self.assertRaises(images.ImageRejected):
                images.validate_registered_asset(uid("x"), Mock(), operation="acquire", db="production", user="postgres")
            sql.assert_not_called()

    def test_loader_failure_hides_private_locator(self):
        with patch.object(images, "_authorized_snapshot", return_value={"mime_type": "image/png"}):
            with self.assertRaises(images.ImageRejected) as error:
                images.validate_registered_asset(uid("x"), Mock(side_effect=OSError("SYNTHETIC private object path")),
                    operation="acquire", db="dpt_schema_test", user="dpt_test_alice")
            self.assertEqual(str(error.exception), "Local image content unavailable")


class ImageDatabaseTests(unittest.TestCase):
    """Actual database/RLS/rights checks; no mock authorization or real images."""
    DB = "dpt_schema_test"

    @classmethod
    def setUpClass(cls):
        local.recreate(cls.DB)
        local.migrate(cls.DB)
        local.sql(baseline(), db=cls.DB)

    def sql(self, text, **kwargs):
        return local.sql(text, db=self.DB, **kwargs)

    def register(self, *, private=False, parent=None, expires=False):
        data = synthetic_png(); measured = images.inspect_png(data)
        name = "local-image:"+self.id().split(".")[-1]+(":child" if parent else "")
        text = image(name, scope="alice" if private else "public", source_suffix="alice" if private else "public", parent=parent, state="acquired")
        text = text.replace(q("b"*64), q(measured.sha256)).replace("byte_size=1,width=1,height=1", f"byte_size={measured.byte_size},width=2,height=3")
        if expires:
            text = text.replace("reviewer,checked_at)", "reviewer,checked_at,review_after)").replace(
                "'Synthetic test','2026-01-01T00:00:00Z');", "'Synthetic test','2026-01-01T00:00:00Z',clock_timestamp()+interval '8 seconds');")
        self.sql("BEGIN;"+text+"COMMIT;")
        return name, data

    def validate(self, name, loader, *, user="dpt_test_alice", operation="display"):
        return images.validate_registered_asset(uid(name), loader, operation=operation, db=self.DB, user=user)

    def test_registered_owned_bytes_match_all_authorized_operations_without_state_change(self):
        name, data = self.register()
        for operation in ("acquire", "display", "transform", "redistribution"):
            with self.subTest(operation=operation):
                self.assertEqual(self.validate(name, lambda: data, operation=operation), images.inspect_png(data))
        self.assertEqual(self.sql(f"SELECT state FROM dpt.image_assets WHERE id={q(uid(name))};").stdout.strip(), "acquired")

    def test_wrong_content_hash_rejected(self):
        name, _ = self.register()
        with self.assertRaisesRegex(images.ImageRejected, "metadata differs"):
            self.validate(name, lambda: synthetic_png(raw=(b"\0"+b"\x01\x02\x03"*2)*3))

    def test_declared_dimensions_and_size_must_match_actual_bytes(self):
        name, data = self.register()
        self.sql(f"UPDATE dpt.image_assets SET width=3 WHERE id={q(uid(name))};")
        with self.assertRaisesRegex(images.ImageRejected, "metadata differs"): self.validate(name, lambda: data)

    def test_private_asset_hidden_to_bob_guest_and_nonexistent_uniformly(self):
        name, data = self.register(private=True)
        self.assertEqual(self.validate(name, lambda: data).width, 2)
        messages=[]
        for user, key in (("dpt_test_bob", name), ("dpt_test_guest", name), ("dpt_test_bob", "absent-private")):
            loader=Mock(return_value=data)
            with self.subTest(user=user, key=key), self.assertRaises(images.ImageRejected) as error:
                self.validate(key, loader, user=user)
            messages.append(str(error.exception)); loader.assert_not_called()
        self.assertEqual(len(set(messages)), 1)

    def test_revoked_asset_permission_blocks_before_read(self):
        name, data=self.register()
        self.sql(f"UPDATE dpt.asset_permissions SET revoked_at=clock_timestamp() WHERE id={q(uid(name+'-permission'))};")
        loader=Mock(return_value=data)
        with self.assertRaises(images.ImageRejected): self.validate(name, loader)
        loader.assert_not_called()

    def test_expired_grant_blocks_after_loader_and_is_not_cached(self):
        name, data=self.register(expires=True)
        loader=Mock(side_effect=lambda: (time.sleep(9), data)[1])
        with self.assertRaises(images.ImageRejected): self.validate(name, loader)
        loader.assert_called_once()
        denied=Mock(return_value=data)
        with self.assertRaises(images.ImageRejected): self.validate(name, denied)
        denied.assert_not_called()

    def test_revocation_during_read_prevents_success(self):
        name, data=self.register()
        def loader():
            self.sql(f"UPDATE dpt.asset_permissions SET revoked_at=clock_timestamp() WHERE id={q(uid(name+'-permission'))};")
            return data
        with self.assertRaises(images.ImageRejected): self.validate(name, loader)

    def test_changed_registered_binding_during_read_prevents_success(self):
        name, data=self.register()
        def loader():
            self.sql(f"UPDATE dpt.image_assets SET attribution='SYNTHETIC changed credit' WHERE id={q(uid(name))};")
            return data
        with self.assertRaisesRegex(images.ImageRejected, "binding changed"): self.validate(name, loader)

    def test_descendant_rechecks_revoked_ancestor(self):
        parent, data=self.register()
        child, _=self.register(parent=parent)
        self.assertEqual(self.validate(child, lambda: data).width, 2)
        self.sql(f"UPDATE dpt.asset_permissions SET revoked_at=clock_timestamp() WHERE id={q(uid(parent+'-permission'))};")
        loader=Mock(return_value=data)
        with self.assertRaises(images.ImageRejected): self.validate(child, loader)
        loader.assert_not_called()

    def test_metadata_only_state_with_unknown_source_never_reads_bytes(self):
        name="local-image:unknown-source"
        text=image(name, source_suffix="unknown", state="rights_pending")
        self.sql("BEGIN;"+text+"COMMIT;")
        loader=Mock(return_value=synthetic_png())
        with self.assertRaises(images.ImageRejected): self.validate(name, loader)
        loader.assert_not_called()

    def test_supported_schema_mime_is_not_decoder_support(self):
        name, data=self.register()
        self.sql(f"UPDATE dpt.image_assets SET mime_type='image/jpeg' WHERE id={q(uid(name))};")
        loader=Mock(return_value=data)
        with self.assertRaisesRegex(images.ImageRejected, "Unsupported image format"): self.validate(name, loader)
        loader.assert_not_called()


if __name__ == "__main__":
    unittest.main()
