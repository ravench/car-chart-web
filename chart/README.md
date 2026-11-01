# Identical Car Chart v1.11 — self-contained copy (2026-11-01)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 18)
- `img/`, `img_manifest.json` — pictures (carsized.com tiles plus the external pictures listed in `build/ext_manifest.json`;
  every accepted and rejected candidate is logged in `build/ext_JUDGED.md`)
- `build/` — generator (`gen.py`), merge pipeline (`apply_corrections.py` → `merge.py` → data.json), the manual
  overrides (`overrides.base.json`), the research files (`research/`, now with `quadricycles.json`), picture tooling
  (`process_images.py`, `pack_fronts.py`, `build_ext.py`, `match_overrides.json`, `dims_notes.json`), the measurement
  check (`verify_dims.py`), the drive data and `merge_report.md`.

v1.11 (2026-11-01): Raven's decisions of 2026-10-27 applied, plus the scale option.
- Scale option (toolbar): "fill frame" (as before), "scale within class" (every tile of a row at the same scale, so the
  cars of one class can be compared by length) and "scale globally" (one scale for the whole chart, a Rocks-e next to
  a Sprinter at true relative size). Front views scale with the same factor.
- Light quadricycle makers added to the "Micro mobility" row: Aixam (City, Coupé, Crossover, Easy, e-Scouty, D-Truck /
  e-Truck), Ligier (JS50, JS60, Myli, Pulse 4), Chatenet (CH46) and Casalini (650). Aixam pictures come from the Aixam
  3D configurator (true side views, grey studio background removed, mirrored), the D-Truck from aixam-pro.com. Ligier
  and Chatenet publish no side view (the Ligier store configurator has only 3/4, rim and top views) and stay name tiles;
  the Casalini 650 has a front view only and no published length.
- The 13 pictures that showed the previous body of a renewed model were replaced by current-body pictures:
  2 Series Gran Coupé (F74) and X5 (G65) from the BMW configurator, Nexo (2025) studio shots from hyundai.com,
  AMG GT 4-Door from the Mercedes configurator, Hilux (2026) and Lexus ES (2026) from the Toyota/Lexus configurator
  (CCIS frames 27/0), Across (2026) from the Suzuki gallery renders, Seltos (2027) and Cooper Cabrio (F67) cut from
  the manufacturer dimension sheets, DR 6 (2026) product cut-out, Compass (2026) from the Stellantis press library
  (true side view, background removed), Ypsilon (2024) from the Stellantis press library. The Ypsilon HF press photo
  is a near-side view seen slightly from the rear, not a true side view (flagged, like the DS N°7). Mitsubishi publishes
  no side view of the 2025 L200, so that tile now shows the name only. The last "previous model" year badge is gone.
- Bayon / Stonic frame kept (Raven's decision).
- Checks: all 78 family frames aligned in the four layout modes, filter check clean, measurement check unchanged
  (183 consistent pairs, 1 pairing to review: Zeekr 7X ↔ Polestar 4).
Earlier versions: `../chart-v1.10/` (plausibility-check fixes), `../chart-v1.9/` (platform check applied),
`../chart-v1.8/` (AWD badge and filters), `../chart-v1.7/`, `../chart-v1.5/`.
