# Identical Car Chart v1.13 — self-contained copy (2026-11-01) — superseded by chart-v1.14

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 23)
- `img/`, `img_manifest.json` — side-view pictures (WebP) and `img/fronts.json` (front views); 12 pictures changed or new since v1.12, see below
- `build/` — generator (`gen.py`), merge pipeline, overrides, picture tooling (`build_ext.py`, `ext_JUDGED.md` = source and treatment of every external picture, `ext_manifest.json`), drive data, `check_align.js`, and `research/` with the model research files

v1.13 (2026-11-01), published as Version 22. What changed since v1.12:
- Side views that faced right are mirrored to face left: Suzuki e Vitara, Audi A2 e-tron, Jeep Compass. All other 487 side pictures were reviewed; none faces right.
- Platform label of the VW Caravelle / Ford Tourneo Custom and VW Transporter / Ford Transit Custom families: "Ford V710" (Ford program code of the 2023 Transit/Tourneo Custom; neither Ford nor VW publishes a platform name, VW calls the 2024 van the seventh generation, not T7). Detail panels explain the naming.
- New brand-own pictures for former name tiles: VW Crafter (UK trim-gallery studio render), Nissan Primastar Kombi (Nissan dimension drawing), Iveco eSuperJolly (brochure dimension render), Renault Trucks Master (catalogue dimension line drawing), Abarth 600e (press photo, side + front), Ebro S400 / S700 / S900 (dimension renders, side + front), Opel Rocks (opel.de render, small source).
- Still name tiles (no brand-own true side view exists): Mitsubishi Eclipse Cross, Fiat Ulysse, Zeekr 9X, DR 8, Iveco eJolly.
- DR 7 is shown as "DR 8": drautomobiles.com sells the same car (4720 x 1860 x 1705 mm, 2710 mm wheelbase, 1.6 T-GDI, 7 seats, EUR 34,900 / 36,900) as "DR 8 Collection" since October 2026 and no longer lists a DR 7. Not confirmed by a press release; the detail panel notes both names.

v1.13a (2026-11-01, Version 23): Opel Rocks cut-out redone from the same 576 px opel.de render using the render's own transparency, with the ground shadow removed (the old rembg cut left a ragged grey strip under the car and made the car too small for its length). No larger brand-own true side view of the Rocks exists: the Stellantis press set (album 593199), the opel.de galleries, the online-store configurator (visual3d views 001-004 are 3/4 views, the side views are not rendered) and the price list only have 3/4 or elevated views. Details in build/ext_JUDGED.md.

Sources and treatments of every external picture: `build/ext_JUDGED.md` and the detail panels in the chart (section "Pictures").
