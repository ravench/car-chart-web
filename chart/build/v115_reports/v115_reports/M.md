# v1.15 picture search - Group M (second, deeper pass) report

Run: 2026-11-01, 22:44-23:11 UTC. Raven's Chrome, own tabs only (all closed at the end). No logins, no forms, no download buttons. The LEVC cookie banner was left untouched (not accepted or rejected); my contact-sheet canvas was layered above it.

Method: page HTML and JSON were read in the page (including JSON-escaped `/` paths and lazy/CSS images). Candidates were judged on contact sheets drawn in the page. Finds were moved with the hx worker and `unpack2.py`. PDFs were scanned in the browser by cutting the image streams out of the PDF bytes. The AU Iveco van brochure uses JPEG 2000 (JPX) streams, which Chrome cannot draw, so 12 of those raw streams were moved and decoded with Pillow in the container. Every saved file was opened and viewed with the Read tool.

Files are in `ext/unpacked/v115/M/`:
- `maxus-t90-ev-side-cn.webp`: the T90 EV find (lossless, alpha kept).
- `maxus-t90-ev-side-cn-scene.webp`: T90 EV fallback, scene photo.
- `levc-tx-side-access-dooropen.webp`: TX candidate (door open).
- `.meta.json` for each.
- `_rejected/sheet-iveco-au-van-brochure-jpx.png`: the decoded AU brochure images.

One operating note: my first Iveco URL-guess probe was far too large (about 16,000 HEAD requests). It froze the tab and was stopped by navigating away after only a small part had run. I then reran targeted lists of 24 names (below).

---

## maxus-t90-ev
- **status: FOUND** (official China twin; studio side is small, a larger scene side exists)
- Best file: `maxus-t90-ev-side-cn.webp`
  - Image: `https://www.saicmaxus.com/uploads/month_202603/images/cb2db8373e3de36cfbbc49273349f06b.png` (750x320 RGBA PNG, transparent background with a soft ground shadow)
  - Page: https://www.saicmaxus.com/car/t90ev.shtml (SAIC Maxus China, model "星际EV"; the URL slug is `t90ev`; 26MY)
  - Source type: brand-own site (manufacturer, China). Market: CN.
- Viewed:
  - True side: both wheels are full circles; only the headlamp corner shows at the nose.
  - Faces **left**, white double-cab pickup.
  - Vehicle about 607x216 px (alpha bbox 77,28-684,244). That is just above the 600 px minimum and below the 800 px target.
  - Same T90 body as the European Maxus T90 EV and the LDV eT60 (the chart marks it as a run-out model; a 2022-2026 picture of the same body is fine). The wheel design may differ from the EU trim.
- Fallback: `maxus-t90-ev-side-cn-scene.webp`
  - Image: `https://www.saicmaxus.com/uploads/month_202603/images/a79e72ef976235587956a3020a2f9e31.png` (1200x800), same page.
  - True side, faces left, vehicle about 860 px wide.
  - It is a composite render on a container-port scene with a motion-blurred road, so it needs a cut-out. It has different multi-spoke wheels.
- Rejected on the same page:
  - `83be8ac0…png` (1920x1020 hero): 3/4.
  - `37ae277a…png`: rear 3/4.
  - `d0cb995d…png`: off-road front 3/4.
  - `c4e03dc9…png`: hangar 3/4.
  - 280x130 menu thumbnail `/uploads/cars/images/090beb80…png`: the same side, too small.
  - The page has no colour picker. The only other link is `/configure?seriesId=36` (spec table, not opened).
- Dead leads:
  - ldvautomotive.com.au: `/et60` and the other guessed paths (`/vehicles/ldv-et60/`, `-ute`, etc.) give 404. The sitemap (`sitemap-0.xml`) lists only T60 MAX, Terron 9 and offers; the `/electric/` page has no eT60 images.
  - ldv.co.nz: menu has no eT60; `/models/ute/et60/` and variants give 404.
- Not opened: maxusmotors.ch, maxus.no/.nl/.dk/.ie and the archived saicmaxus.co.uk T90EV page. Not needed after the find.

## levc-tx
- **status: CANDIDATE** (true side, studio, current body, but the passenger door is open and the ramp is out)
- File: `levc-tx-side-access-dooropen.webp` (saved at 2400x1600; the original is 6886x4591)
  - Image: `https://images.netdirector.co.uk/gforces-auto/image/upload/auto-client/4e56fa3a95451e27335c5c9d3a5f52cf/tx_access_side_flipped.jpg`
  - Fetched as `.../upload/q_auto:best,c_scale,w_2400/auto-client/...` (a Cloudinary transform; the full size works without it).
  - Page: https://www.levc.com/new-models/tx-shuttle/ (in the "TX Access" block)
  - Source type: brand-own site (LEVC UK, GForces/netdirector CDN). Market: UK.
- Viewed:
  - True 90-degree side: both wheels are full circles; no front or rear face.
  - Faces **right**. White TX on a light-grey studio background.
  - Current TX body (TX Access).
  - **But** the rear-hinged passenger door is open (its top edge pokes slightly above the roof line) and the wheelchair ramp is deployed on the ground. The silhouette needs retouching, or accept it like the Mifa 7 door-open fallback.
- Checked and rejected:
  - The "country sites" are not sites: levc.com/de redirects to the UK home page, and the country entries are only `/dealer-contact/levc-germany/` etc.
  - Every image on /new-models/tx-access/, /tx-shuttle/, /technology/, /soa/, /company/, /licencing/, /electric-charging/, all scenes, 3/4 views or details:
    - `main_banner.png` and `accessible_to_all_1_.png`: front with the ramp.
    - `example_01-04.jpg`: toys and diecast models.
    - `transport.png`: liveried 3/4.
    - `highres_extra_1.jpg`: grille detail.
    - `soa_cms_1/2.png`: chassis.
  - All 40 articles under /news/: the only "side" file is `tx_ch01_side_landscape.png` in "LEVC confirms next generation black cab". It is a dark teaser silhouette of the **next-generation** taxi, not the TX.
- Not reached: Geely/ZGH media, LEVC China/Japan, dealers, third-party catalogues.

## levc-vn5
- **status: NONE**
- Checked: all 40 LEVC news articles; no VN5-, van- or studio-named images. The tx-shuttle page's `vn5_eu_shoot.jpg` is a badge close-up. The VN5 model page was already rejected by G (3/4, scenes, cutaway).
- Not reached (time): Geely/ZGH media, LEVC dealers (DE/NL/NO), third-party catalogues.

## iveco-daily
- **status: NONE** (no new find; G's weak `iveco-daily-side-edaily-cab.webp` remains the best: eDaily cab with dropside, near-side)
- URL guesses next to `UK/Products/eDaily/eDaily_cab_MY24_profilo_SW_LHD.png`: 24 targeted names were loaded as images and **none exist**. They covered:
  - van / Van / minibus / furgone; SW / TW; LHD / RHD; the `-modale` suffix.
  - The `Daily/` and `Daily/daily-van/` folders.
  - `edaily-van-profilo/laterale/side`.
  (A wider 240-name run was cut off.)
- UK eDaily page: full list of 74 paths, including the JSON-escaped ones. Sheet of the 16 likely ones, all 3/4 views, scenes or rear:
  - `Banner/edaily_van1-3.jpg`, `edaily_cab1-3.jpg` (1520x428 banners)
  - `edaily-van-retro.png` and `edaily-van-retro-orizzontale.png` (rear, open doors)
  - `eDaily_van_MY24_3-4_SW_LHD(-modale).png`, `DSC_1660.png`, hero and teaser images
- iveco.com/au (the AU site is www.iveco.com/au/; iveco.com/australia is 404):
  - Model cards `Australia/Products/DailyMy24/Van.png`, `Daily-MY24-Cab.png`, `4x4-Low-Res.png`, `7Ton.png` (1000x750): 3/4 front on white.
  - Promo images (Daily-Van-Run-Out, 35S clearance, cab chassis, New Generation): 3/4 or scenes.
  - `New-2026-Daily-4x2-Van-Spec-Sheet.pdf`: dimension views are greyscale **line drawings** (rejected) plus one 3/4 photo.
  - `New-Daily-Van-Brochure---Web-Edition.pdf` (13.6 MB, JPEG 2000): decoded 12 candidates. They are top-view ADAS diagrams, clusters, and the load-volume image (1352x517, slightly 3/4 front with m³ lines). Rejected; sheet in `_rejected/`.
- Iveco press photogallery: `/au/-/media/IVECOdotcom/global/Press/Photogallery/RangeMY24/Daily/NNDaily{Van,Cab}_MY24_{Low,High}.jpg`.
  - Probed: DailyCab 01-04 and DailyVan 15, 17-22 exist (3000-6400 px).
  - All are location scenes with 3/4 views or people in front (`20DailyVan` and `21DailyVan` are near-side but in arcades with a person or pillars). Rejected.
- Spain, Netherlands, Poland and Portugal Daily pages use the same global picture set as the UK; only 0-3 non-vehicle files differ.
- Not reached: Iveco dealer sites, the eDaily press folder `RangeMY24/eDaily/eDaily_MY24/` (01_eDailyCabMY24 and 02_eDailyMY24 exist; others unprobed), DE/IT brochures.

## piaggio-porter-np6
- **status: NONE**
- commercial.piaggio.com/it_IT:
  - Model pages render on the client. The only vehicle images are the known 3/4 `images.piaggio.com/np6/vehicles/<code>/...-01-s.png` set.
  - 96 view and side name variants were tried (`-02`…`-10`, `-90`, `-00`, `side`, `lato`, `laterale`, `profilo`, `dx`, `sx`) for all four codes: none exist.
  - The ten NP6 news pages load their images by script (no image URLs in the HTML).
  - No brochure PDF link was found.
- Piaggio Group press, piaggiogroup.com:
  - The launch release `/en/archive/press-releases/piaggio-group-new-porter-np6-first-city-truck` has `_01…_05_piaggio_porter_np6*.jpg` (700x390): range group shot, blue tipper 3/4 on white, quarry scene, warehouse scene.
  - The NPE release has `msg_c_carousel_images/01-04_Piaggio Porter NPE.jpg` (3200x2286): front 3/4 and rear 3/4 on white, plus two town scenes.
  - The media gallery holds only logos, people and plants.
  - All rejected.
- Not reached: country sites (de_DE/fr_FR/es_ES), dealers, third-party catalogues.

---

## Summary

| model | status | best URL |
|---|---|---|
| maxus-t90-ev | FOUND (official CN twin "星际EV"; true side, faces left, transparent, but only ~607 px; larger ~860 px scene version as fallback) | https://www.saicmaxus.com/uploads/month_202603/images/cb2db8373e3de36cfbbc49273349f06b.png (scene: .../a79e72ef976235587956a3020a2f9e31.png) |
| levc-tx | CANDIDATE (true side, studio, faces right, 6886x4591, but passenger door open + ramp out) | https://images.netdirector.co.uk/gforces-auto/image/upload/auto-client/4e56fa3a95451e27335c5c9d3a5f52cf/tx_access_side_flipped.jpg |
| levc-vn5 | NONE | - |
| iveco-daily | NONE (no van side; G's eDaily cab profile stays the weak best) | (G) https://www.iveco.com/uk/-/media/IVECOdotcom/UK/Products/eDaily/eDaily_cab_MY24_profilo_SW_LHD.png |
| piaggio-porter-np6 | NONE | - |
