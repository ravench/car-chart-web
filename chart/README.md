# Identical Car Chart v1.5 — self-contained copy

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc)
- `img/<id>-side.webp` — 399 carsized.com side views, trimmed, half resolution, to scale with each other
- `img/fronts.json` — the 381 carsized.com front views as one base64 WebP pack (the artifact host serves no raw binary files)
- `img_manifest.json` — which model has which view
- the data, generator and measurement check are one level up (`../gen.py`, `../data.json`, `../measurement-check/`)

v1.5 (2026-10-25): 10 tiles show the previous model ("2025 model" badge) because carsized has no entry for the current
generation; only carsized entries whose year range covers 2025 were used. Their pairings are listed, not checked.

v1.5.1 (2026-10-25): Škoda Octavia corrected after Raven's re-check: the plug-in hybrid tag was removed (the Octavia iV was dropped with the 2024 facelift; skoda.ch lists petrol, diesel and mild-hybrid only), the status note records the full hybrid announced on 5 Oct 2026. Manual data corrections live in `../overrides.base.json` under "final" (key "brand model|row"); `apply_corrections.py` + `merge.py` reproduce them.

v1.6 (2026-10-25, evening): Raven allowed older carsized images ("use older images if needed"). Six more tiles now show the newest previous model of the same line that carsized has (BMW 2 Series Gran Coupé 2019–2024, Lexus ES 2018–2021, Toyota Hilux 2020–2024, Lancia Ypsilon 2015–2017, Fiat Doblò 2015–, Mitsubishi L200 2019–); the badge gives the pictured model's year (last year of carsized's range, capped at the current generation's start year). Revived or renamed nameplates (Lancia Gamma, BMW i3, Mitsubishi Grandis, Fiat Qubo/Ulysse, Nissan Townstar, Fiat Scudo) keep name tiles. 405 of 525 tiles have pictures.
