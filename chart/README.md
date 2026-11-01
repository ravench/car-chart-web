# Identical Car Chart v1.14 — self-contained copy (2026-11-01)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 25 = v1.14a)
- `img/`, `img_manifest.json` — side-view pictures (WebP) and `img/fronts.json` (front views); 5 pictures new since v1.13a, see below
- `research/` — model research files, incl. `research/countries/brand_countries.json` (brand countries for the flags; the poster build needs it)
- `build/` — generator (`gen.py`), merge pipeline, overrides, picture tooling (`build_ext.py`, `ext_JUDGED.md` = source and treatment of every external picture, `ext_manifest.json`), drive data, `check_align.js`, and `research/` with the model research files

v1.14 (2026-11-01), published as Version 24. What changed since v1.13a: the last five name tiles got side views, so every tile now has a picture.
- DR 8 (data id dr-dr-7): DR's own "modellino" cut-out of the DR 7 Collection (1200 px, drautomobiles.com), which the site lists as DR 8 Collection since October 2026; true side view, brand-own.
- Mitsubishi Eclipse Cross: Mitsubishi Motors Europe press photo Eclipse-Cross_004 (premiere press kit, 17 September 2025; static, true side), background removed, mirrored to face left; brand-own press photo.
- Fiat Ulysse: Fiat's own configurator render (lb.assets.fiat.com, angle 4 = true side view, rendered at 3840 px) of the 2024-facelift Ulysse Combi M in white; background and ground shadow removed; brand-own render.
- Zeekr 9X: Zeekr's own studio side view from the zeekr.eu 9X page (exterior colour section, Onyx Black, 2880 px), studio backdrop removed; brand-own.
- Iveco eJolly: Iveco studio side view as published by the Dutch dealer Iveco Schouten (768 px copy; the Iveco original and press kit could not be reached) — flagged in the detail panel as a dealer copy. The only picture of the five that is not taken from a brand site.

Sources, alternatives checked and treatments: `build/ext_JUDGED.md` (section v1.14) and the detail panels in the chart (section "Pictures").

v1.14a (2026-11-01), published as Version 25. Only two files changed against v1.14: `index.html` and `img/skoda-peaq-side.webp`.
- Skoda Peaq (data id skoda-peaq): Raven reported that the side view faced right. The Skoda brand render already faces left as published, so the earlier mirroring is removed (`build/build_ext.py`, mirror flag False). Detail panel text updated.
- Every other side picture (504 files: cars, vans, pickups, quadricycles, including the five v1.14 additions) re-checked on contact sheets: none faces right.
- The `research/` folder (incl. `countries/brand_countries.json`) was missing from the v1.14 copy; it is now included here and under `build/research/`, so a poster build from this folder shows the brand flags again.


Superseded by chart-v1.15 (2026-11-01, Version 26): 34 more side pictures, see ../chart-v1.15/README.md.
