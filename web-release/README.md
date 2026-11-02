# Identical Car Chart: web release for WordPress

Build: `python3 build_release.py` (takes the newest `../chart-vX.Y/`; pass a folder to pick another,
`--base-url /path/` if the chart is not uploaded to `/wp-content/uploads/car-chart/`).
Output lands in `out/<version>/`. The chart itself is unchanged; the script only adds a proper
`<!doctype html>` skeleton (viewport, description, Open Graph tags), self-hosts the Barlow fonts
(no Google Fonts request, nothing loads from third parties) and, for the single file, inlines all pictures.

| Output | Size | Use |
|---|---|---|
| `car-chart-<v>.zip` / `folder/` (files at the top level of the zip, no parent folder) | 30 MB zipped, 37 MB unpacked (13 MB of it the poster PDF) | Upload the `car-chart` folder by FTP / hosting file manager. Pictures load lazily, so the first view is light. |
| `single/car-chart.html` | 28 MB | One file with everything inside. Works opened from disk or uploaded anywhere that serves HTML. |
| `wordpress-embed.html` | – | Paste into a **Custom HTML** block on an empty page: the chart covers the whole window, with a small "← Blog" button. |
| `page-car-chart.php` | – | Alternative: a theme page template that outputs only the full-screen chart (keeps `wp_head`/`wp_footer`, so analytics still run). |

## Self-hosted WordPress (recommended)
1. Unzip `car-chart-<v>.zip` into the folder that should serve the chart (the zip has no parent folder; for
   car-chart.forestraven.net that is the subdomain's web root). That URL already works on its own.
2. Create a page (e.g. "Car chart"), add a **Custom HTML** block, paste `wordpress-embed.html`, publish.
   Or copy `page-car-chart.php` into your child theme and pick "Car chart (full screen)" as the page template.
3. Updating later: replace the folder; the page needs no change.

## WordPress.com / no file access
Host the folder elsewhere (GitHub Pages, Netlify, Cloudflare Pages are free) and change the iframe `src` in
the embed snippet to that URL. Custom HTML blocks with iframes need a plan that allows them.

## Tested (v1.11 to v1.17, Chromium)
Standalone page, inside the embed snippet on a mock blog page, and the single file from `file://`: 537 tiles,
side and front views load, no console errors, zero requests to other hosts, no horizontal scroll at 390 px.

## A0 poster
If `../poster-a0/identical-car-chart-A0.pdf` exists, the build copies it into the folder release and adds an
"A0 poster · PDF" download link to the chart header. The blog post links to it at
`/wp-content/uploads/car-chart/identical-car-chart-A0.pdf`. Rebuild after the poster changes. (The single-file
release has no poster link.)

## Current hosting (2026-11-01)
The chart lives at https://car-chart.forestraven.net/ (contents of the `car-chart` folder at that subdomain's
web root). The build's default `--base-url` and the blog post links point there.

## Caching (.htaccess, since v1.17)
The folder ships an Apache `.htaccess` that sends `Cache-Control: no-cache` for `index.html`, the JSON data files
and the poster PDF, so browsers revalidate them on every visit (a cheap 304 when unchanged) and a new upload shows at
once. Without it the server sent no Cache-Control and browsers kept the old page for hours. Pictures and fonts keep
the server's default caching. It is wrapped in `<IfModule mod_headers.c>`, so it does nothing where that module is
missing. It is a dot-file: make sure your FTP client / file manager uploads hidden files.

## GitHub Actions (since v1.17)
`.github/workflows/web-release.yml` builds the release on every push to `main`, on `v*` tags and by hand
(Actions → Web release → Run workflow). The run's artifact `car-chart-<version>` holds the release files; its
download is the flat zip (no parent folder, `.htaccess` included). On a tag push the zip is also attached to the
GitHub release of that tag. Local build in this repository: `python3 web-release/build_release.py` (picks up
`chart/` and `poster/` by itself; `--out DIR` to choose the output folder).
