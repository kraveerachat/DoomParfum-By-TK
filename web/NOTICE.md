# Notices

## Original material

Every fictional record, article and visual study under `src/fixtures/` and `public/studies/` was authored for this project (task IMP-WEB-01). None of it depicts a real fragrance, house, ingredient, price or package.

## Fonts (SIL Open Font License 1.1)

| File in `src/fonts/` | Source package | SHA-256 |
|---|---|---|
| `bodoni-moda-latin-opsz-normal.woff2` | `@fontsource-variable/bodoni-moda` 5.3.0 (Google Fonts v28) | `c032219ef636f7b4932f7d1dc91bdab602c970f090770b546bea4effaab3463c` |
| `noto-sans-thai-latin-wght-normal.woff2` | `@fontsource-variable/noto-sans-thai` 5.3.0 (Google Fonts v29) | `1a66f268c8d76575807979309cbbac3aff7b61919f59ea19fdc821d92fb407f3` |
| `noto-sans-thai-latin-ext-wght-normal.woff2` | same | `49929deb3afa3fea37b19fdd148889ef19b3e44a8452b13568af089a7d5db934` |
| `noto-sans-thai-thai-wght-normal.woff2` | same | `1f5a173641bbcb3ca4fb0a986858b6b07f8cd5dd2ed61236b40548c7a3c7292f` |
| `fahkwang-thai-300-normal.woff2` | `@fontsource/fahkwang` 5.3.0 (Thai subset; npm integrity `sha512-7jNeeht0dV3JlTKhAg3wKTpyZmvU738J/+qo5+8vUotmUL2B56oYQvCv17na2mtY/ovvZQMknro2QoCaRzDFRQ==`); license text from google/fonts `ofl/fahkwang` at `a60a77e14f28abd4ef243a1b5dfc48df0cec5205`. Thai display face selected by the Owner at CP4 (IMP-WEB-02) | `86cb1a4944422c53e628d8174253d483f8226481d8dcd4de24a16adfef5fccda` |

Full license texts: `src/fonts/OFL-BodoniModa.txt`, `src/fonts/OFL-NotoSansThai.txt`, `src/fonts/OFL-Fahkwang.txt` (copied to `licenses/` in the runtime image). They are kept byte-for-byte as published (`src/fonts/.gitattributes`).

## Software

Next.js, React, Radix Dialog and Tailwind CSS are MIT licensed. Lucide icons are ISC licensed. Exact versions are in `package-lock.json`.

The locally built runtime image also contains `sharp` (Apache-2.0) and its `libvips` libraries (LGPL-3.0-or-later), optional Next.js dependencies that this app does not use. `caniuse-lite` data (CC-BY-4.0) is used only while building. The image is not distributed; check these terms before that changes.
