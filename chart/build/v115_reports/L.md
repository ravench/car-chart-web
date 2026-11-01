# v1.15 picture search: Group L report (second, deeper pass with Raven's Chrome)

Session: 2026-11-01, 22:44-23:15 UTC (container clock). I worked in one tab of my own, which is now closed, and touched no other tab. I used no download buttons and no `?download=1` links, accepted no cookie banners, did not log in, and loaded no external scripts. Originals were fetched into memory with the hx worker (plus a raw-bytes variant for one PDF and one PNG), moved with read_page and unpacked with `unpack2.py`.

All finds are in `ext/unpacked/v115/L/`, each with a `<name>.meta.json`. I viewed every saved file: the contact sheet is `xfer/L/L_final_sheet.png`, and I also viewed each file at a larger size.

---

## ligier-js60: FOUND (brand press photo; scene, needs rembg)
- **File:** `L/ligier-js60-side-press89.webp`, 2560x1707 (WebP q0.92, scale 1). The car is about 1490 px long.
- **URL:** https://media.ligier.fr/app/uploads/2026/09/NOUVELLE-JS60-ULTIMATE-89-scaled.jpg
- **Page:** https://media.ligier.fr/communique-de-presse/nouvelle-ligier-js60-la-ligier-qui-voit-plus-grand/ (photo gallery of the Sept 2026 press release; also in the médiathèque gallery https://media.ligier.fr/mediatheque/nouvelle-js60/).
  - Source type: brand press (Ligier Group media site). Market: FR.
- **Viewed:** near-true side, **faces LEFT**.
  - Car: **Nouvelle JS60 (2026) Ultimate**, blue with a black roof and black alloys. This is the current body.
  - Both wheels are round. The front face is not visible. The camera is a few degrees towards the rear, so the wrap-around tail lamp shows.
  - Background: outdoor scene (gravel courtyard, stone building, trees, a Ligier flag behind the roof). It needs rembg.
- **Checked and rejected (same shoot):**
  - Method: by probing the upload folder I found **27 files** of this shoot: `NOUVELLE-JS60-ULTIMATE-{2,18,23,36,37,42,45,46,48,56,63,64,66,68,70,71,74,75,76,77,78,81,84,86,88,89,90}-scaled.jpg`. Only 8 of them are linked from the release.
  - I viewed all 27 on two contact sheets:
    - 90: rear 3/4.
    - 2, 23, 36, 46: 3/4 views and groups.
    - 18, 42, 45, 48: driving shots.
    - 37, 74-78: details.
    - 81: front-quarter detail.
    - 84, 86: front 3/4 and straight front.
    - 56-71: interiors.

## ligier-js50: NONE
Checked and rejected:
- **Mondial 2024 press kit** (https://media.ligier.fr/app/uploads/2024/11/Mondial-2024-Dossier-de-presse-FR.pdf, 18 pages, 1.3 MB).
  - Transferred whole; all pages rendered and viewed (contact sheet `xfer/L/mondial_sheet.png`); embedded images listed with pdfimages.
  - Pages 5-18 hold no side view. Page 6 (Select/Elite/Ultimate) and page 11 (stand line-up) are 3/4 cut-outs; the rest are scenes, people and text. All embedded images are 150 ppi and small.
  - The kit's "KIT MEDIA" links point to https://extranet.ligiergroup.com/index.php/s/3CK4fbBQSxjwLS3, which now answers "Share not found".
- **media.ligier.fr WordPress library.**
  - The REST API shows only 17 of 226 uploads made since 2024-09; the rest are not public.
  - Médiathèque gallery https://media.ligier.fr/mediatheque/js50-2/ (12 photos): the `202407_Ligier-Europe_JS50-Ultimate-Asphalt-Grey_*` studio set (3-4-Front, Tail-light, dashboard, phone mat, Social_2/4) and the `202506_..._Summer_JS50-*_Social-Photo_*` lifestyle set. Viewed; no side view.
  - Probed hidden files of the 202407 set: 7 colour/trim names x 23 view names (Side, Profile, Profil, Lateral, 3-4-Rear, Rear, Configurator_*, Social_1-6, ...).
    - Hits: Asphalt-Grey Social_1, Intense-Black Social_2 and Rims, Blue-Reef Social_1/4, Green-Velvet Social_3.
    - All viewed: lifestyle scenes and a wheel detail (Rims, on white, so a white-background studio set probably exists, but no side file was found).
  - Probed the 202506 Summer set numbers 01-045 (Horizontal/Vertical). The new hits are Blue-Reef Social-Photo_03 and _04, both lifestyle with people.
  - Probed the 202511 Autumn set (`202511_Ligier-Europe_Autumn_JS50-Ultimate-Asphalt-Grey_Social-Photo_N`, N = 1-40) on media.ligier.fr (2025/11-2026/03) and on s3.ligier.fr (2025/11-2026/01): no files.
  - Nürburgring gallery (8 photos, 2025, racing livery): details and 3/4 views.
  - Press releases: the electric range release (2026/04) has only battery images; the Nürburgring release has only logos.
- **Importer sites.** ligier.se uses the same `s3.ligier.fr` bucket and a mirror of the main library.
  - Same counts as www.ligier.fr for Social-Photo/Shooting/Studio; 0 hits for sida/profil/sidovy/side.
  - On www.ligier.fr: 0 hits for Profil, Lateral, Side, Cote, Packshot, Detoure.
  - Numbered images `JS50-Ultimate_Reef-Blue_Revo-D_{3,11,13}`, `JS50-Ultimate_Toledo-Red_EV-11_{10,11,13}`, `JS50-Elite_White_Revo-D-_3`: viewed. These are shoot numbers of lifestyle scenes, not packshot angles. `js60-lp`, `js60-arriere-lp`, `JS60-VIT-EV`, `range_js60` and `JS60-Select_Black` are 3/4 cut-outs.
  - I did not open ligier.no, .fi, .es, .it, .pt, .be or .at. By the same pattern they are very likely mirrors of the shared bucket.
- **Dealers (viaBOVAG NL).** 24 JS50 listings. I listed the photo URLs of 8 new-body listings and viewed the first 4-8 photos of 6 of them.
  - Zieleman (lf91gv8, 54vz2et): turntable studio with a "zieleman" logo watermark and banners. The views seen are 3/4 front and rear; rejected (watermark).
  - TOP/RIDA (3y7x0d9): 3/4 views in a showroom with logos.
  - Ligier Partner (75ac69l, wz3z75j): outdoor forecourt, 3/4 views.
  - No clean true side.
- **Leads not opened:**
  - The remaining photos of the Zieleman listings: there are 23-27 per listing, and a turntable set may include a 90-degree frame, but every frame carries the watermark logo.
  - mobile.de, autoscout24, marktplaats, leboncoin, automobile.it.
  - Finnish and Nordic dealers.

## wey-wey-05: FOUND (brand-own site, China; transparent cut-out; flag "China model")
- **File:** `L/wey-wey-05-side-mocha26.webp`, 1948x710, lossless WebP **with alpha**. The car's bounding box is x 26-1926, y 103-688, so the car is about 1900 px long.
  - The source PNG is kept as `xfer/L/wey-wey-05-side-mocha26.source.png`.
- **URL:** https://res.gwm.com.cn/weysite/static/src/views/index/img/models/xmk-hi4-renew-26.png
- **Page:** https://www.wey.com/, the home-page model carousel (slide "魏牌新摩卡Hi4"; model page https://www.wey.com/mocca.html).
  - Source type: brand-own site, WEY China. Market: CN.
- **Viewed:** true side, **faces LEFT**.
  - Car: black **New Mocha Hi4** with black multi-spoke wheels.
  - Both wheels are full circles, with no front or rear face visible.
  - Background: transparent, with a soft semi-transparent floor shadow. The windows are semi-transparent.
  - The site also has separate wheel overlays `-26-q.png` and `-26-h.png` (242x242) for a rolling animation. The body PNG already contains the wheels.
- **Caveat:** this is the Chinese "renew/26" model year of the Mocha. It has the same body shell as the EU WEY 05 (= Mocha DHT-PHEV = Coffee 01), and the CN length of about 4875 mm matches the chart's 4871 mm. Bumper and wheel details may differ slightly from the German car, so flag it as a China-market render.
- **Checked and rejected:**
  - presse.gwm-motor.de WP media: search=Coffee gives 0 hits, Mocha 0, Seite/Profil 0; WEY gives 164. The WEY 05 items not listed by group K:
    - `2024/02/WEY-05-exterior-presskit-highres1.jpg` (567x378, 3/4 front).
    - `2024/02/GWM-WEY-05_-3.jpg` (and -3-1): **567x378 only**. A white EU WEY 05 in front of a white villa, facing right, near-side but slightly from the rear. It is too small. No full-size original exists in 2022/10, 2022/11, 2022/12, 2023/01, 2023/02, 2023/10, 2023/11 or 2024/02; only _-1/-5/-7/-8 have 13-36 MB originals, and those are 3/4 or front views.
    - `2022/10/GWM-WEY-05_-8.jpg`, 9504x6336: straight front at dusk.
    - The press-kit PDFs are all under 1 MB, so I did not open them.
  - gwm-motor.de/wey-05: `2023_02_19-24_WEY_STILLS_DAY_01_LOC_2_CRANE_1917_WF01 Sideshots.jpg` (848x848) is a **rear 3/4** despite the name.
    - `hubfs/Testing/WEY00005 Kopie 1.png` (270x125) and `Navi_Bilder/GWM Web_Freisteller_Navigation_Mobile_WEY05.png` (900x453) are slight 3/4 front cut-outs.
    - `P24705_GWM_WEY_05_2024_{Snow_White,Deep_Sea_Blue}.jpg`, `Bild4x1`, `Headerbild_Update0112` and `Extras950x660_x1` are 3/4 views or scenes.
- **Leads not opened:**
  - wey.com/mocca.html colour picker, which may have the same render in lighter colours.
  - GWM export sites (gwm-global, IL, TH, BR, Gulf).

## nissan-primastar-kombi: FOUND, small (brand-own packshot, white background, 600x320)
- **File (preferred):** `L/nissan-primastar-kombi-side-eutile.webp`, 600x320 (WebP q0.95). The car is about 545 px long.
  - URL: https://www.nissan.de/content/dam/Nissan/nissan_europe/vehicles/TDIEU_MY21_PRIMASTAR_FULL_PES_VLP-PLUS/Primastar-combi_de.jpg (a 36 KB JPEG; also served from www-europe.nissan-cdn.net).
  - Page: model menu tile on https://www.nissan.de/fahrzeuge/neuwagen.html and https://www.nissan.de/fahrzeuge/neuwagen/primastar/primastar-kombi.html.
  - Source type: brand-own (Nissan Europe DAM). Market: DE/EU.
- **Same picture (alternate copy):** `L/nissan-primastar-kombi-side-chmenu.webp`, from https://www-europe.nissan-cdn.net/content/dam/Nissan/ch/vehicles/primstar-combi/Primastar-combi_de.jpg. It is the mega-menu tile on https://de.nissan.ch/fahrzeuge/neuwagen/primastar/primastar-kombi.html (CH; 22 KB JPEG).
- **Viewed:** true side, **faces RIGHT**.
  - Car: silver **Primastar Kombi L1** (short), with side glazing, a sliding door and alloys.
  - Body: the current 2021-facelift nose with C-shaped LED lamps.
  - Both wheels are round. Only the headlamp corner of the nose shows.
  - Background: white, with a soft floor shadow.
- **Limit:** it is small, at about the brief's minimum. There is no larger copy:
  - `/jcr:content/renditions/original` returns 404, and `cq5dam.web.1280.1280.jpeg` exists but is not larger than the 600 px original.
  - `_fr`, `_it`, `_en`, `_nl` and `_es` variants all return 404.
  - Decide whether this clean 600 px side render beats the larger v113 dimension drawing (which has dimension lines).
- **Checked and rejected:**
  - Nissan Europe newsroom photo search "Primastar Combi" (10 results): only 2021 range photos (rear 3/4, 3/4 front at the lake, the already rejected 70ef85) plus old NV300/Primastar views.
  - The primastar channel: old (pre-2016) releases only.
  - nissan.ch/nissan.de Kombi page images (`21TDIEU_NV300_brochure_2021_0xx_pace50x`, `PE-023..028`, `TDIEU_MY24_PRIMASTAR_VLP_UPDATE/combi/...`): 3/4 at the lake, interiors, boot, and seat-layout top views.
- **Bonus (not my group), nissan-primastar-van-mid:** `L/bonus-nissan-primastar-van-mid-side-eutile.webp`, 600x320.
  - Grey Primastar panel van L1H1, current nose, true side, faces right, white background.
  - URL: https://www.nissan.de/content/dam/Nissan/nissan_europe/vehicles/TDIEU_MY21_PRIMASTAR_FULL_PES_VLP-PLUS/Primastar%20fourgon.jpg. It is the same style of tile as the Kombi.

## smart-2: FOUND (brand-own site; studio scene, needs rembg)
- **File:** `L/smart-2-side-earlyorder.webp`, 2048x1536. This is a scale 0.5 copy of the 4096x3072 original (WebP q0.92); the car is about 1470 px long.
- **URL:** https://d3us6q6u6nvlci.cloudfront.net/storyblok/g/190233663367975/52e17d7308/hashtag-two-early-order-teaser-mid-banner.jpg
- **Page:** https://de.smart.com/de/models/hashtag-two/ ("early order" teaser banner). Source type: brand-own site, smart Europe. Market: DE.
- **Viewed:** near-true side, **faces LEFT**.
  - Car: smart #2 production car, red ("Laser Red", as in the press-kit Rgb series) with a black roof and two-tone bronze wheels.
  - Both wheels are round. There is a slight wide-angle perspective (the front wheel is marginally larger), and only the lamp edges show.
  - Background: studio scene (red walls, curtain, gold "smart" and "#2" lettering, red floor), so it needs rembg.
- **Checked and rejected:**
  - media.smart.com category 5737 still has only the two kits (Images 561 MB, Video 1.24 GB), so nothing new since the E and I passes.
  - de.smart.com #2 page:
    - `hashtag-two-navi.png` (3840x3840): 3/4 front.
    - `hashtag-two-specs-teaser-mid-banner.jpg`: top view.
    - `hashtag-two-brabus-teaser`: detail.
    - The hero fallback was rejected before.
- **Not opened:** smart.cn and uk.smart.com.

---

## Summary
| model | status | best file / URL |
|---|---|---|
| ligier-js50 | NONE (press kit p. 5-18, media.ligier.fr incl. hidden-file probes, ligier.se/.fr libraries, viaBOVAG dealers: no clean true side; dealer turntable sets are watermarked) | - |
| ligier-js60 | FOUND (brand press photo, 2560x1707, Nouvelle JS60 Ultimate blue, faces left, near-true side, courtyard scene, needs rembg) | `L/ligier-js60-side-press89.webp` <- https://media.ligier.fr/app/uploads/2026/09/NOUVELLE-JS60-ULTIMATE-89-scaled.jpg |
| wey-wey-05 | FOUND, flag China model (wey.com transparent cut-out, 1948x710, New Mocha Hi4 black, faces left, true side) | `L/wey-wey-05-side-mocha26.webp` <- https://res.gwm.com.cn/weysite/static/src/views/index/img/models/xmk-hi4-renew-26.png |
| nissan-primastar-kombi | FOUND, small (brand packshot 600x320, silver Kombi L1, white bg, faces right, true side) | `L/nissan-primastar-kombi-side-eutile.webp` <- https://www.nissan.de/content/dam/Nissan/nissan_europe/vehicles/TDIEU_MY21_PRIMASTAR_FULL_PES_VLP-PLUS/Primastar-combi_de.jpg |
| smart-2 | FOUND (de.smart.com banner, 4096x3072 original, red production #2, faces left, near-true side, studio scene, needs rembg) | `L/smart-2-side-earlyorder.webp` <- https://d3us6q6u6nvlci.cloudfront.net/storyblok/g/190233663367975/52e17d7308/hashtag-two-early-order-teaser-mid-banner.jpg |
| (bonus) nissan-primastar-van-mid | FOUND, small (brand packshot 600x320, grey van, white bg, faces right) | `L/bonus-nissan-primastar-van-mid-side-eutile.webp` <- https://www.nissan.de/content/dam/Nissan/nissan_europe/vehicles/TDIEU_MY21_PRIMASTAR_FULL_PES_VLP-PLUS/Primastar%20fourgon.jpg |
