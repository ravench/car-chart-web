# Identical Car Chart v1.8 — self-contained copy (2026-10-26)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 15)
- `img/<id>-side.webp` — 486 side views (405 from carsized.com, 81 from other sources), trimmed and to scale
- `img/fronts.json` — 440 front views as one base64 WebP pack
- `img_manifest.json` — which model has which view
- `build/` — the generator (`gen.py`; 7th argument = `drive.json`), the cut-out script for non-carsized pictures
  (`build_ext.py`, `ext_manifest.json`, `JUDGED.md`) and the drive data:
  - `build/drive.json` — per model: drives (FWD/RWD/AWD), awd flag, the brand's AWD term, note, confidence, source page
  - `build/drive/result-1..9.json` — the nine Opus 5.5 research batches (`batch-1.json` shows the input format)
  - `build/drive/verified.json` — 21 entries re-checked by hand on manufacturer/importer pages (overrides the batches)
  - `build/drive/merge_drive.py` — merges batches + verified entries into `drive.json` (`--write`), checks consistency

v1.8 (2026-10-26): AWD badge and filters. 302 of 525 models are sold with all-wheel drive or 4x4 in at least one
version (Europe, Swiss/German line-ups first). Each tile carries an "AWD" chip; the detail panel's "Drive" row names
the drive layouts, the brand's term (quattro, 4MATIC, xDrive, 4x4, e-4ORCE …), the versions AWD is limited to and the
page checked. Two new filter rows: Powertrain (BEV, PHEV, full hybrid, mild hybrid, petrol incl. LPG/CNG, diesel,
hydrogen) and Drive (front, rear, all-wheel); brands and rows without a visible model collapse.
Confidence: 418 entries rest on a manufacturer/importer page, price list or ADAC/press-portal entry ("high");
107 rest on trade press or product knowledge and are marked "(not checked on a manufacturer page)" in the detail panel.
Dangel 4x4 conversions of Stellantis and Toyota vans are not counted as factory AWD (noted in those panels).
Corrections from the hand check: ID. Buzz Cargo, ID. Tiguan, Audi Q5, Maxus eDeliver 7, Ebro s900, Voyah Courage
gained AWD/FWD versions; Farizon V7E is front-wheel drive.
Earlier versions: `../chart-v1.7/` (pictures from other sources, v1.7 notes), `../chart-v1.5/`.
