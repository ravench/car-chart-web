# Identical Car Chart

Every new car and van up to 3.5 t sold in Europe, by brand and vehicle class, with the models that are the same
vehicle (or share a platform) under different badges framed together. Swiss model names, data checked October/November 2026.

Live: **https://car-chart.forestraven.net** · Story: [Same car, different badge](https://blog.forestraven.net/index.php/same-car-different-badge-a-chart-of-every-car-on-sale-in-europe/)

## What is in this repository

| Folder | Contents |
|---|---|
| `chart/` | The chart itself: `index.html` (self-contained page), `img/` (side views, `fronts.json` with the front views), `img_manifest.json`, `research/` (model research, brand countries) and `build/` (generator `gen.py`, merge pipeline, overrides, picture tooling, checks). `chart/README.md` lists what changed in each version. |
| `web-release/` | `build_release.py`, which turns a chart folder into the WordPress / web release (doctype and Open Graph skeleton, self-hosted Barlow fonts, `.htaccess`, zip, single-file version, embed snippet and page template), plus the blog post. |
| `poster/` | The A0 print poster (`identical-car-chart-A0.pdf`, only the 78 cross-brand families) and its build scripts. |

Open `chart/index.html` in a browser; serve the folder over http (`python3 -m http.server`) for the front views.

## Versions

Each tag `v1.x` is one published chart version (`v1.5` to `v1.17`; there was no separate v1.6 folder). The commit
history follows the chart folders as they were saved during the project; the web release and the poster were added
with v1.17. `git diff v1.16 v1.17 -- chart/build/data.json` shows the data changes of a version.

## Rebuilding

The scripts were written for the project folder layout (`chart-vX.Y/`, `release-web/`, `poster-a0/` side by side):

- Web release: `python3 web-release/build_release.py chart` (pass the chart folder; the poster PDF is picked up from `../poster-a0/` in that layout, so copy `poster/identical-car-chart-A0.pdf` there or skip it).
- Poster: see `poster/README.md` (needs Python with Pillow and segno, Node with Playwright/Chromium).

Pictures come from carsized.com and from the manufacturers' websites, press libraries and configurators
(sources per picture in `chart/build/ext_JUDGED.md` and in each tile's detail panel); they are included here for the
chart to work and remain the property of their owners.
