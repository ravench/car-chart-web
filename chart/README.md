# Identical Car Chart v1.7 — self-contained copy (2026-10-26)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 14)
- `img/<id>-side.webp` — 486 side views: 405 from carsized.com plus 81 from other sources (see below), all trimmed and to scale
- `img/fronts.json` — 440 front views as one base64 WebP pack (the artifact host serves no raw binary files)
- `img_manifest.json` — which model has which view
- `build/` — the generator (`gen.py`), the cut-out script for non-carsized pictures (`build_ext.py`: selection table, treatments), the picture manifest it writes (`ext_manifest.json`: source page, notes, terms per view) and the judgement log of every accepted and rejected candidate (`JUDGED.md`)

v1.7 (2026-10-26): 90 of the 120 tiles that had no carsized picture now show one found on manufacturer, press or
catalogue sites, cut out, mirrored where needed and scaled like the carsized pictures (81 side views, 62 front views;
30 models stay as name tiles because only three-quarter views exist). Each affected detail panel names the source,
the editing applied and the terms. Third-party placeholders (zigwheels.ae, CarBase.my, Autocar India, motor.es,
evspecs.org, evo.co.uk) must be replaced before any publication. Source list and licensing notes:
Claude Doc "Chart v1.7 picture sources" (https://claude.ai/artifact/J3oA7sCD1XEuyCyeSu6jKa).
Earlier versions: `../chart-v1.5/` (v1.5, v1.5.1, v1.6 notes in its README).
