# v1.15 picture search - Group G (second pass, real browser) report

Run: 2026-11-01, about 22:10-22:32 UTC. Raven's Chrome, two own tabs, both closed at the end. No download buttons, no logins; the one cookie banner (levc.com) was left untouched.

Method: pages and PDFs fetched in the page (fetch + arrayBuffer); images judged on contact sheets drawn in the page, then the chosen originals moved with the hx worker (WebP) and `unpack2.py`. Every saved file was opened and viewed with the Read tool.

Brochure PDFs were scanned in the browser, not transferred:
- The DCTDecode image streams (embedded JPEGs) were cut out of the PDF bytes and drawn on contact sheets.
- The few large FlateDecode images were only small masks or gradients.
- So no PDF needed to be transferred to the container.

Files are in `ext/unpacked/v115/G/`:
- `renault-trucks-master-side.webp`
- `maxus-mifa-7-side.webp`
- `iveco-daily-side-edaily-cab.webp`
- `_rejected/iveco-daily-vanthird-tiny.webp`, a 97x44 reference only.

---

## renault-trucks-master
- **status: FOUND**
- Image: `https://www.renault-trucks.com/sites/default/files/2023-11/Renault%20Trucks%20E-Tech%20Master%20(4).jpg`. The original is 5000x3332.
- Page: renault-trucks.com newsroom, 2023 press release "New generation Renault Trucks Master Red EDITION" (photo set 2023-11, N = 1-11).
- Source type: brand press photo (Renault Trucks corporate), global.
- Verified by viewing `renault-trucks-master-side.webp`. It is saved at scale 0.6 (3000x1999, WebP q0.92); the URL above gives the full-resolution original.
  - True side: both wheels are full circles. Only the wrap-around headlamp and red light bar show at the nose, as on any Master IV profile. No front or rear face.
  - Faces right, grey (dark slate) panel van, pure white studio background, soft ground shadow.
  - Current Master IV (2024) body with the Renault Trucks diamond and red accent. It is the E-Tech (electric) van; the body is the same as the diesel.
  - Vehicle bounding box in the saved file: x 94-2888, y 418-1581 (includes antenna and shadow).
- **Size caveat:** wheelbase / overall length measures about 0.69, which fits **L3** (Master IV L3: about 4,330 / 6,280 mm). Roof H2.
  - The chart length is 5,050 mm (an L1-type figure).
  - If the picture is scaled to 5,050 mm, the height will come out too low. Either scale it to its own length (about 6.3 m) or adjust the chart length.
- Rejected:
  - E-Tech Master (1): three-van group shot, scene.
  - (2): dark studio 3/4 front.
  - (3), (5), (6): 3/4 front on white.
  - (7): charger scene, 3/4.
  - (8): roof/camera detail.
  - (9)-(11): interior.
  - LCV page images (renault-trucks.com/en/renault-trucks-light-commercial-vehicules):
    - `renault-trucks-master-red-edition.jpg` (700x394): box-body truck 3/4 front, scene.
    - `renault-trucks-master-chassis-cab-version.jpg` (1280x771): dropside 3/4.
    - `...master-4-bricklayer.jpg`, `...master-4-messaging-service.jpg` (person in front), `banner-renault-trucks-master-trafic.jpg`: scenes.

## maxus-mifa-7
- **status: FOUND (low resolution, China-market twin)**
- Image: `https://www.saicmaxus.com/uploads/month_202505/images/55ebd9e0c04293932fb1f406699f71f7.png`. 750x320, transparent PNG.
- Page: https://www.saicmaxus.com/car/mifa7.shtml (SAIC Maxus China, model page "大家7" = MIFA 7).
- Source type: brand-own site (manufacturer, China).
- Verified by viewing `maxus-mifa-7-side.webp` (750x320, alpha kept):
  - Near-true side: both wheels are circles; the vertical corner headlamp at the nose is visible, as it wraps round the corner.
  - Faces left, mint green, transparent background.
  - Car bounding box 674x252 px (alpha bbox 38,43-712,295), so above the 600 px minimum but below the 800 px target.
- Same body as the European Mifa 7 (EU Mifa 7 = China 大家7 BEV). The wheel design may differ from the EU trim.
- Fallback: the UK image `https://www.saicmaxus.co.uk/media/pdqhbxn5/mifa-7-exterior-side-view-door-open.jpg` (1200x800). It is also a true side but has the doors open; I did not download it again.
- Rejected on the China page:
  - `43a8292f...jpg` (1920x1020): side silhouette with a light streak, the lower body fades out, no wheels.
  - All other 1920x1020 slides: scenes, interior, cutaways, front/rear views.
  - The menu thumbnails of all Maxus models (280x130): true sides but too small.
- Not useful:
  - www.maxus.ie: does not resolve (chrome error).
  - rivervale.co.uk Mifa 7 leasing page: no Mifa images in the HTML.

## iveco-daily
- **status: FOUND (weak: eDaily chassis cab with dropside, not the van; near-side)**
- Image: `https://www.iveco.com/uk/-/media/IVECOdotcom/UK/Products/eDaily/eDaily_cab_MY24_profilo_SW_LHD.png` ("profilo" = profile). 1048x1310 canvas, white background.
- Page: the iveco.com/uk eDaily page.
- Source type: brand-own site (Iveco UK).
- Verified by viewing `iveco-daily-side-edaily-cab.webp`:
  - MY24 eDaily single cab with an aluminium dropside body and headboard rack.
  - Faces left, pale blue-green cab; vehicle bounding box 887x355 px (x 83-970, y 466-821).
  - Near-true side: both wheels look round, but the headlamp and the bumper corner with the fog lamp show a little (about 5-10 degrees of front perspective).
  - Same cab as the diesel Daily MY24.
- **No true side of the Daily *van* was found anywhere:**
  1. MY24 brochures, scanned in the browser (both HTTP 200):
     - `https://www.iveco.com/uk/-/media/IVECOdotcom/docs/brochure/my2024/IVECO-Daily-MY24.pdf` (9,179,108 B, 430 image XObjects, 89 large JPEGs)
     - `https://www.iveco.com/uk/-/media/IVECOdotcom/docs/brochure/my2024/daily2.pdf` (8,268,641 B, 333 images, 72 large JPEGs)
     - All large embedded JPEGs were checked on contact sheets: 3/4 views, scenes, top-view ADAS diagrams, interior.
     - The only near-side is the load-volume image my24 image #143 / d2 equivalent (649x249): Daily high-roof van, slightly 3/4 front, with white volume lines and m³ labels drawn over the body, too small. Rejected.
     - The dimensions pages evidently use vector drawings, not photo renders.
  2. iveco.com/uk, /france, /germany, /italy Daily pages (166 unique image paths):
     - Hero, teaser, banner and version-banner images (`Daily-furgone.jpg`, `version-banner-van24-1/2.jpeg`, `Daily-Van24.jpeg`, `daily_van_Teaser.jpg`) are 3/4 or scenes.
     - `MY24/01_Img_HTML_Tables/eDaily/vanFirst.png`, `vanSecond.png`, `vanThird.png` are true sides of the van (three roof heights) but only 97x44 px. `first.png` / `second.png` (163x40) are tiny chassis-cab sides.
     - `Daily_Van_Table.jpg` (1558x618, 3/4 rear) and `Daily_Cab_Table.jpg` (1558x525, 3/4 front) are dimension tables. Rejected.
     - Guessed van "profilo" file names in the eDaily folder do not exist (tested about 10 variants).
- Not reached: Iveco dealer sites (iveco-schouten.nl etc.) and Iveco press galleries.

## levc-tx
- **status: NONE**
- levc.com/new-models/tx-taxi-overview/: the images on the live page (`1_levc_tx_.png` 1920x640 night scene, `angle_north_5_vertical.jpg` charging scene, `exterior_pack.jpg`, `passenger_pack.png`, `hackney_pack.jpg` and other 498x664 cards, `banner_bottom.png` bird's-eye view, `tx_ch01_front_landscape.png` front) contain no side view. The images are served from images.netdirector.co.uk (GForces Cloudinary) with hashed folders, so file names cannot be guessed.
- Not usable:
  - media.levc.com: does not resolve.
  - levc.com/wp-json media search: fails.
  - The web search found only diecast models and press articles.

## levc-vn5
- **status: NONE**
- levc.com/new-models/vn5/: all 21 images were drawn from the netdirector CDN at w_600.
  - `vn5_electric_van_commercial_vehicle_studio_28_.jpg` and the second white studio shot: 3/4 front.
  - `vn5_new_electric_van_1_/3_rt_rgb`, `vn5_hero_imagery_1/4/10_`, `vn5_location_shoot_retouched_`, `tx_vn5_in_poland_1_`: scenes, 3/4.
  - `vn5_rear.jpg`, `vn5_loading.jpg`: rear and loading views.
  - `banner.png`: cutaway.
- The linked spec guide `https://levc.com/wp-content/uploads/M29488_VN5_Spec_and_Price_Guide.pdf` returns 404 on www.levc.com, and the bare levc.com host is not reachable by cross-origin fetch.

## piaggio-porter-np6
- **status: NONE**
- commercial.piaggio.com/it_IT/modelli/fisso/: images are the known images.piaggio.com np6 version renders (all 3/4) plus `res-750x500/2024_PorterNP6.png` and `2024_PorterNPE.png.png` (not opened). No brochure PDF link in the page HTML.
- press.piaggiogroup.com: the search and every tag URL tried (porter, porter-np6, commercial-vehicles, veicoli-commerciali …) give 404.
- de.motor1.com/photos/764792 (third-party): only 3 photos (group scene, red dropside 3/4 front, interior).

## maxus-t90-ev
- **status: NONE** (not reached; runout model)
- No time left after the other models. Earlier runs found no T90 EV page on maxus.no, saicmaxus.co.uk or ldvautomotive.com.au.
- The SAIC Maxus China site has a pickup line-up with 280x130 side thumbnails, but I did not identify a T90 EV page there.

---

## Summary

| model | status | best URL |
|---|---|---|
| renault-trucks-master | FOUND (true side, white bg, faces right, L3H2 E-Tech: scale to ~6.3 m, not 5,050 mm) | https://www.renault-trucks.com/sites/default/files/2023-11/Renault%20Trucks%20E-Tech%20Master%20(4).jpg |
| maxus-mifa-7 | FOUND (near-true side, transparent, faces left, only 750x320; China 大家7 = Mifa 7) | https://www.saicmaxus.com/uploads/month_202505/images/55ebd9e0c04293932fb1f406699f71f7.png |
| iveco-daily | FOUND-weak (eDaily MY24 chassis cab + dropside, near-side, faces left; no van side exists in brochures/site) | https://www.iveco.com/uk/-/media/IVECOdotcom/UK/Products/eDaily/eDaily_cab_MY24_profilo_SW_LHD.png |
| levc-tx | NONE | - |
| levc-vn5 | NONE | - |
| piaggio-porter-np6 | NONE | - |
| maxus-t90-ev | NONE (not reached) | - |
