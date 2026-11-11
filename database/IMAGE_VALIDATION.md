# Local image metadata and rights validation — IMP-P1-03

This private local module fills the byte-validation gap after the existing image
SQL contracts. It adds no tables, migration, storage provider, download endpoint,
HTTP client, image renderer, public export or product-facing sharing.

`image_validation.inspect_png(bytes)` has no I/O or authorization. It accepts only
static PNG, 8-bit RGB/RGBA, non-interlaced, with IHDR/IDAT/IEND chunks. It validates
CRC, dimensions, zlib stream completion, exact scanline count/filter codes, size and
SHA-256. Ancillary chunks (including EXIF/text/ICC), APNG, palettes, interlacing,
trailing/concatenated data and unsupported formats fail closed. JPEG/WebP/AVIF
remain valid schema MIME labels but are unsupported by this validator. SVG/GIF
and executable content are rejected. This is a narrow structural validator, not
a general-purpose image decoder or sanitizer. It does not strip metadata or make
thumbnails.

Default local limits: 5 MiB input, width/height at most4096,4million pixels,
20 MiB decoded scanlines and1024chunks. Check dimensions/decoded size before zlib;
cap decompression at expected scanline bytes plus one. A trusted caller may supply
a tighter `Limits` policy. No web-upload or global decompression setting exists.

`validate_registered_asset(asset_id, read_content, operation=..., db=..., user=...)`
first queries current `dpt_guard.can_use_asset` as the explicit local non-owner DB
login. Missing/hidden/denied/expired/revoked assets are rejected before the callback
runs. It validates bytes against the exact registered MIME, size, dimensions and
hash, then rechecks current SQL authorization and the exact asset binding. Source,
capture, assessment, selected permission, parent permission, per-use grants and
ancestry remain database-enforced rather than being copied into Python policy.

The callback is trusted local integration code bound to that asset's already
owned/permitted object; tests use only in-memory agent-authored synthetic PNGs.
There is no filesystem or network loader. Input limits apply to the returned byte
buffer; a future untrusted upload/file adapter must also bound reads before
allocation. No reader is implemented or authorized here. Callback failures suppress
private locator text. Return values contain only technical metadata; internal SQL
snapshots/locators/permission evidence are neither returned nor logged.

A result is a point-in-time technical check, not a cached grant/serving token.
Later display/transform/export must reauthorize at actual use. The function neither
stores bytes nor advances an asset to `validated`. Local Docker/PostgreSQL admin
and the caller's choice of DB login are trusted developer capabilities, not app
authentication. No runtime API should accept a client-supplied database/user.

## Checks

```powershell
py -3 database/verify_images.py
# Only after the coordinator grants an exclusive DB window:
py -3 database/verify_images.py --include-db
```

Offline mode needs standard-library Python only. DB mode recreates only disposable
`dpt_schema_test`, retains the existing container/volume/image/loopback guards, and
runs new integration checks plus13original image SQL tests. It does not use the
capacity/migration probe or persistent Scento pilot. DB fixtures are explicitly
SYNTHETIC authorization/metadata and never establish real media rights. Existing
full-regression tests depend on external data paths; run the coordinator's portable
fixture-path wrapper instead of substituting invented data or editing those tests.

Sanitized test evidence is in `database/evidence/image_*_results.json`; detailed
logs remain ignored under `.local/image-rights`. Full regression, independent
review and publication are recorded in [[IMP-P1-03_Local_Image_Rights]] in the vault.
No third-party image bytes/permission, HTTP/proxy/SSRF, provider, restore, cloud or
production completion is claimed.
