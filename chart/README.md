# Identical Car Chart v1.9 — self-contained copy (2026-10-26)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 16)
- `img/`, `img_manifest.json` — pictures as in v1.7/v1.8
- `build/` — generator (`gen.py`), merge pipeline (`apply_corrections.py` → `merge.py` → data.json), the manual
  overrides (`overrides.base.json`: aliases, exclusions, `edges_add`/`edges_remove` keyed "brand model|row",
  `group_labels` keyed by family id, `final` per-model field fixes), the drive data (`drive.json`, `drive/`),
  the external-picture tooling and `merge_report.md`.

v1.9 (2026-10-26): results of the platform check of all 296 unframed tiles (../platform-check/) applied.
- 3 new families: E-GMP (Ioniq 3 + EV4, compact cars), SEA (Zeekr 001 + Lotus Emeya), SEA-S (Zeekr 9X + Lotus Eletre).
- 8 models added to existing families: Dacia Duster, Bigster, Striker (CMF-B), Kia EV3 and EV5 (E-GMP; the
  measurement check flags EV3's 320 mm longer wheelbase against the Ioniq 5 as "to be reviewed"), Polestar 4 (SEA;
  width flag), Jaecoo 5 (Chery T1X), Omoda 9 (Tiggo 9 family, now labelled Chery T1X/M3X).
- DR 5 (2026) removed from the Chery T1X family: it is based on the Changan CS35 Plus (the earlier DR 5.0 was Chery-based).
- 25 platform descriptions corrected (Velar, Q7, Peaq, Ora 03/5, Lepas L8, Denza, BYD Ti 7, Staria, Musso EV, M-Hero, Bugatti …).
- New detail-panel line "Platform relatives in other classes" for 52 models whose platform siblings sit in other rows
  (Aygo X → Mazda2 Hybrid/LBX, Scala → MQB A0 cars, DS 7 → 308/408/Astra …); the links open the relative's panel.
- Not framed (noted in the panels): Wey 05/Haval H6 and Wey 03/Jolion Pro (L.E.M.O.N. link only in secondary
  sources), GR Supra (its Z4 twin is gone; not a CLAR sibling of the 2 Series/4 Series).
- Status questions from the check: GR Supra and petrol Mazda2 were already marked run-out; the AMG GT SUV has had an
  open order book since 20 Oct 2026, so it stays.
Earlier versions: `../chart-v1.8/` (AWD badge and filters), `../chart-v1.7/` (pictures from other sources), `../chart-v1.5/`.
