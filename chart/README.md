# Identical Car Chart v1.16 — self-contained copy (2026-11-02)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 28 = v1.16)
- `img/`, `img_manifest.json` — side-view pictures (WebP) and `img/fronts.json` (front views, packed); 34 side pictures new since v1.14a, see below
- `img/sides.json`, `img/sides_packed.txt` — the 29 new side pictures packed as base64 (only the published artifact needs them, see "Artifact file limit"); this folder has every picture as a single file too
- `research/` — model research files, incl. `research/countries/brand_countries.json` (brand countries for the flags; the poster build needs it)
- `build/` — generator (`gen.py`), merge pipeline, overrides, picture tooling (`build_ext.py`, `ext_JUDGED.md` = source and treatment of every external picture, `ext_manifest.json`, `pack_fronts.py`, `pack_sides.py`), drive data, checks, the v1.15 research brief and target list (`v115_brief.md`, `v115_targets.json`, `v115_chrome_howto.md`), the thirteen research-group reports (`v115_reports/`), and the data patches of this version (`patch_v115.py`, `patch_v115b.py`, `p115c.py`, `p115d.py`, `apply_log.md`)

v1.15 (2026-11-01), published as Version 26. Raven asked for the v1.14 picture process to be applied to every tile that still had no picture or only a drawing/wireframe.
38 such tiles were inventoried. 34 got a true side view of the current body, facing left, cut out on white; 4 keep their name tile.

New side pictures (brand-own unless marked):
- Quadricycles: Ligier Myli (Ligier press photo), Ligier Pulse 4 (press photo, Forgeon box body), Ligier JS60 (press photo, 2026 JS60 Ultimate), Casalini 650 (Casalini studio photo), Chatenet CH46 (third-party catalogue photo from automoto.it, flagged as placeholder)
- Chinese brands, from the brands' European sites or configurators: XPeng L03 and G9L (store.xpeng.com configurator renders), Denza D9 and Z9 GT (denza.com/de studio pictures; the D9 also got a front view), Geely Starray EM-i (geely.de 360 viewer, side and front), Lepas L8 (lepasinternational.com), BYD Shark, Sealion 5 and Ti 7 (byd.com/uk), smart #2 (de.smart.com early-order picture)
- Chinese brands, from the home-market site because no European side view exists (same body; flagged in the detail panel): Voyah Dream (voyah.com.cn), Maxus Mifa 7 and T90 EV (saicmaxus.com), Wey 05 (wey.com New Mocha Hi4 — same shell, bumpers and wheels differ), Mhero I (third-party zigwheels.ae photo, flagged)
- Wey 03 (GWM Germany press photo), Farizon SV and V7E (farizonauto.co.uk importer cut-outs), Maxus eDeliver 3, 7 and 9 (maxus.no importer cut-outs), DR 1.0 EV (DR "ModelloCut" render)
- Vans and pickups: Renault Trucks Master (Renault Trucks press photo), Nissan Townstar van (Nissan Europe press photo), Nissan Primastar van and Primastar Kombi (Nissan packshots, 600 px — small), Mitsubishi L200 (Mitsubishi Australia Triton render — Club Cab body, no Double Cab side render exists; noted in the detail panel), Iveco Daily (Iveco UK eDaily chassis-cab profile render stands in for the family; no side view of the Daily van exists on Iveco's sites)
- Morgan Plus Four: captured from Morgan's own 3D configurator (configure.morgan-motor.com) turned to a true side view

Still without a side view: Ligier JS50 (Ligier publishes only three-quarter views), LEVC TX (LEVC's only side view shows the TX Access with the rear door open and the ramp down) and VN5, Piaggio Porter NP6 (only three-quarter renders).

Data fixes in this version: Wey 03 length 4,668 mm (was 4,520; gwm-motor.de technical data), other names Coffee 02 / Latte, status run-out; Wey 05 length 4,870 mm, status run-out; DR 1.0 EV status run-out (model page removed from drautomobiles.com).

Sources, alternatives checked and treatments: `build/ext_JUDGED.md` (section v1.15), `build/v115_reports/A.md` to `M.md`, and the detail panels in the chart (section "Pictures").

Artifact file limit: the published artifact may hold at most 512 files per version and already holds 506, so from v1.15 on new side pictures are published inside `img/sides.json` (`build/pack_sides.py`). The page loads `img/<id>-side.webp` first and falls back to the packed copy only when the single file is missing (`gen.py`: `sideFallback`). A folder copy like this one has every picture as a file and never uses the pack.

v1.15a (2026-11-01), published as Version 27. Only `index.html`, `img/renault-master-side.webp`, `img_manifest.json` and the build notes changed: the Renault Master side picture (renault.ch configurator cut-out) carried a grey ground shadow, which the poster thread noticed at A0 size; the picture was cut again without the shadow (`build/ext_JUDGED.md`, section v1.15a).

v1.16 (2026-11-02), published as Version 28. Only `index.html` and `build/gen.py` changed (pictures and data as in v1.15a). Raven asked that the web version hide columns that contain no cars once filters are applied: brand columns (and their group headers) now disappear when none of the brand's cars is visible in the selected classes, and class rows disappear when none of their cars belongs to a selected group - under every filter combination (class, group, twins-only, powertrain, drive). Before, the class and group filters left empty columns and rows (choosing only Pickups kept all 96 columns; now 10 remain). Checked with the layout, alignment and filter scripts and in a headless browser.


Superseded by chart-v1.17 (2026-11-02, Version 29): version number shown in the page header, see ../chart-v1.17/README.md.
