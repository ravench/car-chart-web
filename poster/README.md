# Identical Car Chart: A0 print poster (v12, 2026-11-01, from chart v1.15a)

- `identical-car-chart-A0.pdf`: A0 portrait (841 x 1189 mm), one page, fonts embedded (Barlow / Barlow Condensed), RGB.
- `identical-car-chart-A0-bleed3mm.pdf`: same with 3 mm bleed on each side (847 x 1195 mm) for print shops.
- `preview.jpg`: screen preview.

Content: only the 78 cross-brand families (242 models) of chart v1.11. One coloured card per family, grouped by vehicle class.
Solid frame = same vehicle under another badge (tier 1), dashed card = platform siblings (tier 2), "Same vehicle"
sub-frame = tier-1 twins inside a platform family. Card colour = the group whose platform it is (overrides in
gen_poster.py OWNER_OVERRIDE: Ford for Amarok/Ranger, Transporter, Caravelle; Suzuki for Heartect-e; Changan for EPA1).
Pictures to scale within each class. Family one-liners in `build/captions.json` (written from the twin notes in data.json).

Rebuild (scratch dir with node + playwright):
  python3 prep.py <chart dir>                       # crops side views to img/*.jpg, writes imgsizes.json
  python3 gen_poster.py <chart dir> img m.html --W 42 --imgh 16 && node measure.js m.html widths.json 42
  python3 gen_poster.py <chart dir> img poster.html --W 42 --imgh 16 --widths widths.json && node render.js poster.html poster.pdf
  (add --bleed 3 and BLEED=3 for the bleed version). render.js prints the body height; it must equal the page height (4494 px).
New families need a caption in captions.json; if the page overflows, lower --W.

v2 (2026-11-01, chart v1.12 / artifact Version 21): brand country flags on every tile (head-office country, small
second flag for the one foreign build country), drawn with the chart's own SVG flags (gen_poster.py reads FLAG_SVG
from the chart's build/gen.py and research/countries/brand_countries.json). Family data unchanged from v1.11.
The chart's v1.12 line layout is not used on the poster (families are cards here). Use <chart dir> = ../chart-v1.12.

v3 (2026-11-01, chart v1.13 / artifact Version 22): 8 new brand pictures (Crafter, Primastar Kombi, eSuperJolly,
Renault Trucks Master line drawing, Abarth 600e, Ebro S400/S700/S900), mirrored e Vitara/A2 e-tron/Compass, DR 8 and
"Ford V710" labels. The new Opel Rocks picture is left out on the poster (576 px source, ragged ground shadow, looks
pixelated at A0); gen_poster.py drops it right after loading imgsizes.json. Use <chart dir> = ../chart-v1.13.

v4 (2026-11-01, chart v1.13 / artifact Version 23): the cleaned Opel Rocks cut-out (render transparency, shadow removed, about 215 dpi at print size) is back on the poster; no tile is excluded any more.

v5 (2026-11-01, chart v1.14 / artifact Version 24): the last five name tiles now have pictures (DR 8, Eclipse Cross, Ulysse, Zeekr 9X, eJolly); every one of the 242 tiles is pictured. Use <chart dir> = ../chart-v1.14.

v6 (2026-11-01): QR code + URL of the interactive version in the header and footer (--url, default https://blog.forestraven.net/wp-content/uploads/car-chart/; needs pip segno; QR checked by decoding the PDF). Fix: chart-v1.14 ships without build/research/, which silently dropped the flags in v5; gen_poster.py now falls back to the newest chart-v*/build/research/countries/brand_countries.json and stops if none exists.

v7 (2026-11-01): URL changed to https://car-chart.forestraven.net/ (Raven), QR verified in both PDFs; URL no longer wraps at its hyphen in the footer.

v8 (2026-11-01): QR code points to Raven's blog post https://blog.forestraven.net/index.php/same-car-different-badge-a-chart-of-every-car-on-sale-in-europe/ (--url); the printed short address is the interactive chart car-chart.forestraven.net (--chart-url). Both QR codes verified by decoding the PDFs.

v9 (2026-11-01): printed addresses without www and without trailing slash (Raven).

v10 (2026-11-01, Raven): QR code points to the interactive chart https://car-chart.forestraven.net (--url); the blog post is printed in the footer (--post-url). Header line breaks fixed: subtitle on two balanced lines, legend in two fixed rows.

v11 (2026-11-01, chart v1.15 / Version 26): new true side views for Renault Trucks Master, Nissan Townstar van, Primastar van and Primastar Kombi (the other new v1.15 pictures are not in a family). Countries now read from <chart>/research/countries/ when build/research is absent.

v12 (2026-11-01, chart v1.15a / Version 27): Renault Master picture without the ground shadow.
