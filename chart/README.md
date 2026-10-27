# Identical Car Chart v1.10 — self-contained copy (2026-10-27)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 17)
- `img/`, `img_manifest.json` — pictures (carsized.com tiles plus the external pictures listed in `build/ext_manifest.json`)
- `build/` — generator (`gen.py`), merge pipeline (`apply_corrections.py` → `merge.py` → data.json), the manual
  overrides (`overrides.base.json`), picture tooling (`process_images.py`, `pack_fronts.py`, `build_ext.py`,
  `match_overrides.json`, `dims_notes.json`), the measurement check (`verify_dims.py`), the drive data and `merge_report.md`.

v1.10 (2026-10-27): fixes from the plausibility check of v1.9.
- Hyundai-Kia: Hyundai's European IONIQ 3 press kit puts the car on the K3 platform (400 V, front-wheel drive, 2,680 mm
  wheelbase, the same as the Kia EV3). The Kia EV3 therefore moved to the K3 family (Kona, Niro, Seltos) and the EV5 to
  the N3 family (Tucson, Sportage); IONIQ 3 + EV4 are now the "K3 (400 V EV)" family of the compact-car row;
  IONIQ 5 / EV6 / GV60 and IONIQ 9 / EV9 stay E-GMP. The EV3/EV4/EV5 twin notes were rewritten and the
  "platform relatives in other classes" lines link the families. The measurement check's EV3 ↔ IONIQ 5 flag is gone.
- Pictures that showed a different car replaced: Dacia Spring (Spring I → studio press photos of the 2026 Spring II,
  media.dacia.com), Fiat Doblò (2015 Tofaş Doblò → Stellantis press photos of the 2022 K9 van, side mirrored),
  DS N°7 (3/4 view → near-side press photo from the media test-drive set; still seen slightly from the rear).
  Mitsubishi Eclipse Cross (2021 ICE picture): Mitsubishi publishes no side view of the Scenic-based 2025 car, so the
  tile shows the name only. The three "previous model" year badges and the old carsized measurements were removed
  (verify_dims.py / gen.py now drop a previous-model carsized entry as soon as the tile no longer shows it).
- Toyota C-HR+: the check said the side view faces right; it faces left, so it is unchanged.
- `process_images.py` now ignores alpha ≤ 24 when trimming, so the shadow halos of cut-out pictures no longer leave
  white margins (DB12, Q9, Tourbillon, Ducato, Scudo … corrected; about 100 side tiles shifted by a few pixels).
- `merge.py`: new `discontinued_notes` / `discontinued_drop` overrides; the Citan / T-Class and EQV notes no longer
  claim "kept as runout tiles" (both lines are out of the chart).
- Open for Raven: Aixam / Ligier quadricycles, the Bayon / Stonic frame, old-generation pictures for new bodies
  (e.g. AMG GT 4-Door).
Earlier versions: `../chart-v1.9/` (platform check applied), `../chart-v1.8/` (AWD badge and filters), `../chart-v1.7/`, `../chart-v1.5/`.
