"""Private local byte/metadata validation; no acquisition, HTTP, storage or serving.

Only static PNG, 8-bit RGB/RGBA, non-interlaced, without ancillary chunks is
supported. Other formats/features fail closed. SQL remains the authority for
scope/source/capture/grants/ancestry. A successful result is not a durable grant.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import struct
from typing import Callable
import uuid
import zlib

import local

VERSION = "local-static-png-v1"
SIGNATURE = b"\x89PNG\r\n\x1a\n"


class ImageRejected(ValueError):
    """Uniform local rejection; do not attach source/permission/private locators."""


@dataclass(frozen=True)
class Limits:
    max_bytes: int = 5 * 1024 * 1024
    max_width: int = 4096
    max_height: int = 4096
    max_pixels: int = 4_000_000
    max_decoded_bytes: int = 20 * 1024 * 1024
    max_chunks: int = 1024

    def __post_init__(self):
        if any(type(v) is not int or v <= 0 for v in asdict(self).values()):
            raise ValueError("Image limits must be positive integers")


@dataclass(frozen=True)
class ImageMetadata:
    mime_type: str
    byte_size: int
    width: int
    height: int
    sha256: str


def inspect_png(content: bytes, limits: Limits = Limits()) -> ImageMetadata:
    """Verify bounded PNG structure, compressed scanlines and exact byte hash.

    Reject metadata/animation/palette/interlace rather than silently stripping
    them. Never decompress until dimensions and decoded-size limits pass.
    This function has no I/O and does not make any rights decision.
    """
    if type(content) is not bytes or not content or len(content) > limits.max_bytes:
        raise ImageRejected("Image byte limit or type rejected")
    if not content.startswith(SIGNATURE):
        raise ImageRejected("Unsupported image format")
    offset = len(SIGNATURE)
    width = height = channels = None
    chunks = 0
    compressed = []
    ended = False
    while offset < len(content):
        chunks += 1
        if chunks > limits.max_chunks or len(content) - offset < 12:
            raise ImageRejected("PNG structure rejected")
        length = struct.unpack_from(">I", content, offset)[0]
        kind = content[offset + 4:offset + 8]
        end = offset + 12 + length
        if end > len(content):
            raise ImageRejected("PNG chunk length rejected")
        payload = content[offset + 8:offset + 8 + length]
        crc = struct.unpack_from(">I", content, offset + 8 + length)[0]
        if zlib.crc32(kind + payload) & 0xffffffff != crc:
            raise ImageRejected("PNG checksum rejected")
        if kind == b"IHDR":
            if chunks != 1 or length != 13:
                raise ImageRejected("PNG header rejected")
            width, height, depth, colour, compression, filtering, interlace = struct.unpack(">IIBBBBB", payload)
            if depth != 8 or colour not in (2, 6) or (compression, filtering, interlace) != (0, 0, 0):
                raise ImageRejected("Unsupported PNG feature")
            channels = 3 if colour == 2 else 4
            if not (0 < width <= limits.max_width and 0 < height <= limits.max_height):
                raise ImageRejected("Image dimensions rejected")
            if width * height > limits.max_pixels or height * (1 + width * channels) > limits.max_decoded_bytes:
                raise ImageRejected("Image decoded-size limit rejected")
        elif kind == b"IDAT":
            if width is None:
                raise ImageRejected("PNG header missing")
            compressed.append(payload)
        elif kind == b"IEND":
            if length or not compressed or end != len(content):
                raise ImageRejected("PNG ending rejected")
            ended = True
            break
        else:
            # Includes EXIF, text, ICC, APNG, palettes and unknown critical chunks.
            raise ImageRejected("Unsupported PNG chunk")
        offset = end
    if not ended or width is None:
        raise ImageRejected("Incomplete PNG")
    row_bytes = 1 + width * channels
    expected = height * row_bytes
    decoder = zlib.decompressobj()
    try:
        decoded = decoder.decompress(b"".join(compressed), expected + 1)
    except zlib.error:
        raise ImageRejected("PNG compressed data rejected") from None
    if len(decoded) != expected or not decoder.eof or decoder.unconsumed_tail or decoder.unused_data:
        raise ImageRejected("PNG decoded length or stream rejected")
    if any(decoded[row] > 4 for row in range(0, expected, row_bytes)):
        raise ImageRejected("PNG scanline filter rejected")
    return ImageMetadata("image/png", len(content), width, height, hashlib.sha256(content).hexdigest())


# Compare the full relevant registered binding again after inspection. It is not
# exported or logged; rights are never cached in a successful result.
_COLUMNS = ("id", "access_scope_id", "source_id", "source_record_id", "rights_id",
            "asset_permission_id", "source_page_url", "original_url", "creator",
            "attribution", "state", "provider", "bucket", "object_key", "mime_type",
            "byte_size", "width", "height", "sha256", "parent_asset_id", "transform_spec")


def _authorized_snapshot(asset_id: str, operation: str, *, db: str, user: str) -> dict:
    # UUID + fixed operation allowlist prevent interpolation of SQL expressions.
    asset = str(uuid.UUID(asset_id))
    if operation not in ("acquire", "display", "transform", "redistribution"):
        raise ImageRejected("Image operation rejected")
    if db not in local.DATABASES:
        raise ValueError("Image validation target is outside the local allowlist")
    columns = ",".join(f"'{c}',a.{c}" for c in _COLUMNS)
    result = local.sql(
        f"SELECT json_build_object({columns}) FROM dpt.image_assets a "
        f"WHERE a.id='{asset}'::uuid AND dpt_guard.can_use_asset(a.id,'{operation}');",
        db=db, user=user, check=False)
    if result.returncode or not result.stdout.strip():
        # Missing, hidden, expired, revoked and denied all have the same outcome.
        raise ImageRejected("Image unavailable for requested operation")
    return json.loads(result.stdout)


def validate_registered_asset(asset_id: str, read_content: Callable[[], bytes], *,
                              operation: str, db: str, user: str,
                              limits: Limits = Limits()) -> ImageMetadata:
    """Validate an already-registered local asset for a specific operation.

    The trusted local caller binds read_content to that asset's owned/permitted
    local object. It is invoked only after current SQL authorization. It must not
    be an HTTP/downloader or an unbounded file reader; those are not implemented
    or authorized here. No bytes are persisted and no DB state is advanced.

    Recheck current SQL authorization and exact registered binding after reading
    and validating. Later display/transform/export must reauthorize again; this
    return value is technical metadata, not a serving token or cached grant.
    """
    try:
        before = _authorized_snapshot(asset_id, operation, db=db, user=user)
    except (ValueError, TypeError, AttributeError):
        raise ImageRejected("Image unavailable for requested operation") from None
    if before["mime_type"] != "image/png":
        raise ImageRejected("Unsupported image format")
    try:
        content = read_content()
    except Exception:
        # A future local object adapter must not leak private paths in failures.
        raise ImageRejected("Local image content unavailable") from None
    measured = inspect_png(content, limits)
    if any(before[k] != v for k, v in asdict(measured).items()):
        raise ImageRejected("Image metadata differs from registered object")
    after = _authorized_snapshot(asset_id, operation, db=db, user=user)
    if before != after:
        raise ImageRejected("Image binding changed during validation")
    return measured
