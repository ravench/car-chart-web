# v1.15 picture search: Group E report

Session: 2026-11-01, 21:46-22:03 UTC.

## Blocker (applies to every model below)
- **No downloads were possible.** The container's agent proxy refused CONNECT (HTTP 403, logged in the proxy status as `connect_rejected ... policy denial`) for every host tried, including control hosts: www.drautomobiles.com, morgan-motor.com, ch.smart.com, www.mitsubishi-motors.co.uk, www.mitsubishi-motors.com.au, www.google.com, en.wikipedia.org, upload.wikimedia.org and www.carsized.com. Per the proxy README this was not retried or worked around.
- **WebFetch cannot read image files.** Both image URLs tested (a morgan-motor.com PNG and a renault-trucks.com JPG) returned `SERVER_ERROR`. WebFetch only sees HTML converted to markdown, and JavaScript-rendered pages (Morgan, smart.com, the configurators) show no images.
- So **nothing could be viewed, and no result is FOUND.** Everything below is a URL with file-name or alt-text evidence, or NONE. The E/ download folder is empty. The main thread needs to open the CANDIDATE URLs in the real browser.
- The URLs below were copied from WebFetch's summaries. They look exact, but check them against the listed page if one fails.

---

## smart-2: CANDIDATE (best lead of this group)
- **New since the earlier check:** media.smart.com now has a smart #2 media-kit category (https://media.smart.com/en-INT/assets/categories/5737/, 2 kits). The **Images kit is https://media.smart.com/en-INT/assets/242460/** (87 images, 561 MB; source type: brand press site, global). Most images are of the April 2026 *Concept #2* (reject: concept). But about 26 Oct 2026 (URL timestamp 1793072xxx) smart uploaded a numbered official render set of the **production** car: **"smart Hashtag2 Premium Laser Red Rgb NN"**. The "Rgb" name and the numbering suggest a studio angle series, so a pure side frame is likely among them. That is not verified: the angles are unknown and nothing was viewed. Originals (CloudFront, `?download=1`):
  - 13 `https://d21buns5ku92am.cloudfront.net/70299/images/713160-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2013%206b57be-f78551-original-1793072781.jpg?download=1`
  - 14 `https://d21buns5ku92am.cloudfront.net/70299/images/713162-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2014%20F6a840-b0f571-original-1793072782.jpg?download=1`
  - 15 `https://d21buns5ku92am.cloudfront.net/70299/images/713165-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2015%2050d649-4ed5f7-original-1793072783.jpg?download=1`
  - 16 `https://d21buns5ku92am.cloudfront.net/70299/images/713161-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2016%20A22b2d-f24bd7-original-1793072782.jpg?download=1`
  - 17 `https://d21buns5ku92am.cloudfront.net/70299/images/713163-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2017%20Ed6c1c-66895c-original-1793072782.jpg?download=1`
  - 18 `https://d21buns5ku92am.cloudfront.net/70299/images/713164-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2018%2054e298-e92531-original-1793072783.jpg?download=1`
  - 19 `https://d21buns5ku92am.cloudfront.net/70299/images/713183-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2019%20Bf8e41-1f6343-original-1793072788.jpg?download=1`
  - 21 `https://d21buns5ku92am.cloudfront.net/70299/images/713170-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2021%20226e98-2e60b1-original-1793072784.jpg?download=1`
  - 22 `https://d21buns5ku92am.cloudfront.net/70299/images/713174-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2022%206047ff-85d246-original-1793072786.jpg?download=1`
  - 23 `https://d21buns5ku92am.cloudfront.net/70299/images/713166-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2023%2094e6e7-17041b-original-1793072783.jpg?download=1`
  - 24 `https://d21buns5ku92am.cloudfront.net/70299/images/713167-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2024%2082ddd2-b339be-original-1793072783.jpg?download=1`
  - 25 `https://d21buns5ku92am.cloudfront.net/70299/images/713168-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2025%201926b5-7962db-original-1793072783.jpg?download=1`
  - 26 `https://d21buns5ku92am.cloudfront.net/70299/images/713171-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2026%20A1ce9d-b0c2be-original-1793072784.jpg?download=1`
  - 27 `https://d21buns5ku92am.cloudfront.net/70299/images/713169-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2027%20312aac-c24a74-original-1793072784.jpg?download=1`
  - A second WebFetch pass confirmed that numbers 01-12 and 20 are **not** on the kit page (only 13-19 and 21-27). The kit has no other production colour or studio series. The other "Exterior" titles are Concept #2 (Rome event, reject).
- Rejected from the same kit, by title: "smart Hashtag2 Sketch Exterieur 1-14" and "Sketch Couture Edition 1-3" (sketches); "Sketch Interieur" (interior); the ECA platform PNG and the "Tridion Cell Evo" PNG (technical CGI); the airbags CGI; the world-premiere stage photos (712853/712854/709956, show scene); "Spilt Tailgate" (detail); all "Concept #2" images (concept, Rome/Beijing).
- Also checked and rejected: the media.smart.com Paris premiere release 273151 (8 photos: stage, executives, cabin, tailgate, Couture, platform and Tridion renders; none is a side view). ch.smart.com/de/models/hashtag-two/ is rendered by JavaScript, but its asset host is `s7.future.smart.com/is/image/smarteurope/...`. es.motor1.com/photos/930273 shows the mural campaign (scenes). The carnewschina Paris article has six "EU version" 800x450 images (`.../2026/10/smart-2-makes-global-debut-at-paris-motor-show-starts-at-{fad874,d6b8ae,baf91c,81fce0,3001a8,31cf02}-800x450.jpg`, credit Smart); their angles are unknown, so these are a fallback only.

## mitsubishi-l200: CANDIDATE (weak; angles unknown)
- The Japanese Triton is the same 6th-generation body as the EU L200 (double cab, GLS/GSR). Source: brand-own site, JP (WebFetch works there; curl did not).
  - Design page https://www.mitsubishi-motors.co.jp/lineup/triton/design/index.html: colour-picker images `https://www.mitsubishi-motors.co.jp/lineup/triton/design/img/img_bodycolor_0{1,2,3}_0N.jpg` (01_01-04, 02_01-06, 03_01-03; the alts are only colour names). GSR photos `.../design/img/img_03_01.jpg`, `img_03_03.jpg` ... `img_03_06.jpg`, plus `img_01.jpg` and `img_02.jpg` (alt "外観"). Japanese colour pickers are often 3/4, but some use side views, so check them.
  - 360 viewer: `img_360_01.jpg` and `img_360_02.jpg` on the design page are only teaser tiles. They link to the **accessory 360 viewer https://www.mitsubishi-motors.co.jp/purchase/accessory/lineup/triton/360/index.html**, which loads its frames through JavaScript (the UI assets sit under `.../triton/360/assets/img/`), so the frame URL pattern and count need a browser network capture. Caution: it is a dealer-accessory viewer ("only some dealer options shown"), so the side frame may carry accessories such as a sports bar or tonneau that change the silhouette.
  - UK: `https://mitsubishi-motors.co.uk/wp-content/themes/tailpress-master/images/L200-Cover-scaled-transparent.png` (alt "L200", transparent cut-out on mitsubishi-motors.co.uk/cars/l200; angle unknown, probably 3/4).
- Checked and rejected: media.mitsubishi-motors-europe.com (home, /gallery/, /models/) has no L200 or Triton at all (only Outlander PHEV, Grandis, Eclipse Cross, Colt, ASX, Space Star). zigwheels.ae L200 gallery has front angle, full front, front medium and rear angle shots, no side, and an unclear generation. The Prezly EU kit PDF (FR), `https://cdn.uc.assets.prezly.com/f7d35f2e-ed69-4d7b-8858-4e4a7e419aea/-/inline/no/Mitsubishi-new-L200---EU-kit-FR.pdf`, is text only, with no image or newsroom references. Car Watch 1555766 has only photos of briefing slides ("ボディサイズ" slide 010; colour slides 046/047), so it is not usable. The webCG 49386 captions name no side view.

## renault-trucks-master: CANDIDATE (unverified; angles unknown)
- renault-trucks.com LCV page (https://www.renault-trucks.com/en/renault-trucks-light-commercial-vehicules, Dec 2025 assets, brand-own, global):
  - `https://www.renault-trucks.com/sites/default/files/2025-12/renault-trucks-master-red-edition.jpg` (alt "Renault Trucks Master Red Edition"; product-name alt only, so it may be a packshot)
  - `https://www.renault-trucks.com/sites/default/files/styles/crop_default/public/2025-12/renault-trucks-master-chassis-cab-version.jpg.webp?itok=3zleAH69` (chassis cab; the original is probably `/sites/default/files/2025-12/renault-trucks-master-chassis-cab-version.jpg`)
- 2023 press release "New generation Renault Trucks Master Red EDITION" (renault-trucks.com newsroom): 11 photos at `https://www.renault-trucks.com/sites/default/files/2023-11/Renault%20Trucks%20E-Tech%20Master%20%28N%29.jpg` (N = 1-11) and the press kit `https://www.renault-trucks.com/sites/default/files/2023-11/PR2023%20New%20Renault%20Trucks%20Master_0.zip`. The alts are generic.
- renault-trucks.ch product page: the alts "Renault Trucks Master Red EDITION Panel Van / Platform Cab / Chassis Cab" exist (probably version tiles), but their URLs were not in the fetched content, so they need the browser. The other photos there (p042683, p042655, p042745, p042751, p042639, p042754) were already known or are interior/scene shots.
- Not opened: `https://www.renault-trucks.nl/sites/default/files/2023-11/RT_LEAFLET_MASTER_2024_GB.pdf`.

## nissan-primastar-van-mid: CANDIDATE (weak; probably the same dimension-drawing art as the current tile)
- nissan.co.uk/vehicles/new-vehicles/primastar.html (brand-own, UK):
  - `https://www-europe.nissan-cdn.net/content/dam/Nissan/nissan_europe/vehicles/TDIEU_MY21_PRIMASTAR_FULL_PES_VLP-PLUS/OVERVIEW/TECHNICAL_INFORMATION/LHD/16TDIeu_NV300_074-76_V1_LHD_pace002-d.jpg`, alt "Nissan Primastar Panel Van profile shots"
  - `https://www-europe.nissan-cdn.net/content/dam/Nissan/nissan_europe/vehicles/TDIEU_MY21_PRIMASTAR_FULL_PES_VLP-PLUS/OVERVIEW/TECHNICAL_INFORMATION/LHD/16TDIeu_NV300_077-78_V1_LHD_pace003-d.jpg`, alt "Nissan Primastar Crew Van profile shots"
- These sit in the same TECHNICAL_INFORMATION folder as the v113 Kombi drawing (`16TDIeu_NV300_071_V0_LHD_pace111.jpg`), so they are probably grey renders with dimension lines. "074-76" suggests three profiles in one image. They are only an upgrade if a profile has no dimension lines.
- Note: the newer UK assets sit in a `primastar-2026` folder. Its hero has the alt "3/4 Front View" and is rejected. I could not tell whether "2026" is a campaign or a nose update.
- Checked and rejected: uk.nissannews.com release-12084 (one uncaptioned photo).

## nissan-townstar-van-small: NONE
- nissan.co.uk/vehicles/new-vehicles/townstar.html, dimensions section: `.../TDIEU_MY23_TOWNSTAR_VAN_L2_VLP_UPDATE/overview/dimensions/lhd/23TDIEULHD_TOWNSTAR_EV_VAN_001_pace024-d.jpg`, alt "3/4 Front packshot view". Rejected (3/4).
- europe.nissannews.com/channels/townstar: 14 releases (2021-2024: reveal, order start, EV production, Passenger, L2 long wheelbase 2023-07-19, Evalia, Crew Van 2024-06-13, ...). The gallery tabs do not render through WebFetch; each shows one uncaptioned preview (for example L2 `https://wieck-nissanao-production.s3.amazonaws.com/photos/3665f190352fd8e155039d8dc842349544ce7aa6/preview-928x522.jpg`, reveal `.../photos/94ff49d7153daacbf48a88392f76d2644a7085b0/preview-928x522.jpg`). No caption says profile or side. Opening the "Photos" tabs in the browser (reveal 2021-09-27 and L2 2023-07-19) is the best remaining route.
- townstar-van.html on nissan.co.uk: fetch failed.

## nissan-primastar-kombi: NONE (keep the v113 nissan.de dimension drawing)
- No Kombi/Combi profile turned up. The Crew Van profile above is not a substitute because its glazing differs.

## dr-dr-1-0-ev: NONE, plus a status flag
- drautomobiles.com home links only DR 3, DR 5 (Collection / Full Hybrid / Stilnovo), DR 6 (Collection / Stilnovo / Super Hybrid / Full Hybrid), DR 8 Collection and DR PK8. **There is no DR 1.0 / DR 1.0 EV page**, so there is no "modellino" cut-out. **Please re-check on_sale vs runout:** the line-up rests on the Sep 2026 price list in il Giornale Digitale.
- Twin, from memory and not verified here: the 3,200 mm length fits the Chery eQ1 "Little Ant" (小蚂蚁), not the QQ Ice Cream (about 2.98 m).

## morgan-plus-four: NONE
- morgan-motor.com/plus-four is rendered by JavaScript (only the og card). The configurator at https://configure.morgan-motor.com/plusfour/ (also https://mobile.morgan-motor.com/plusfour/) loads its renders through JavaScript, so no URL pattern is visible. In the browser, rotate to the side camera and read the network requests.
- Rejected: the og:image `https://morgan-motor.com/wp-content/uploads/New_Morgan_Plus_Four_Dynamic_Blue_05.jpg` ("driving on a mountain road", scene). The dealers.morgan-motor.com stock page (Morgan of Naples, 2026 Classic White) had no images in the fetched content.
- Not opened: `https://morgan-motor.com/wp-content/uploads/Plus-Four-manual-Technical-Specification.pdf`, `.../Plus-Four-automatic-Technical-Specification.pdf`.

---

## Summary

| model | status | best URL |
|---|---|---|
| smart-2 | CANDIDATE (official production render set, angles unknown) | https://media.smart.com/en-INT/assets/242460/ : "smart Hashtag2 Premium Laser Red Rgb 13-27", e.g. https://d21buns5ku92am.cloudfront.net/70299/images/713160-Smart%20Hashtag2%20Premium%20Laser%20Red%20Rgb%2013%206b57be-f78551-original-1793072781.jpg?download=1 (full list above) |
| mitsubishi-l200 | CANDIDATE (weak, JP Triton = same body) | https://www.mitsubishi-motors.co.jp/lineup/triton/design/img/img_bodycolor_01_01.jpg (series 01_01-03_03); accessory 360 viewer https://www.mitsubishi-motors.co.jp/purchase/accessory/lineup/triton/360/index.html (frames via JS) |
| renault-trucks-master | CANDIDATE (unverified) | https://www.renault-trucks.com/sites/default/files/2025-12/renault-trucks-master-red-edition.jpg ; 2023-11 "E-Tech Master (1-11)" photos |
| nissan-primastar-van-mid | CANDIDATE (weak, probably the dimension-drawing art) | https://www-europe.nissan-cdn.net/content/dam/Nissan/nissan_europe/vehicles/TDIEU_MY21_PRIMASTAR_FULL_PES_VLP-PLUS/OVERVIEW/TECHNICAL_INFORMATION/LHD/16TDIeu_NV300_074-76_V1_LHD_pace002-d.jpg |
| nissan-townstar-van-small | NONE | (route: europe.nissannews.com Townstar galleries in the browser) |
| nissan-primastar-kombi | NONE (keep v113 drawing) | - |
| dr-dr-1-0-ev | NONE (+ flag: no DR 1.0 on drautomobiles.com) | - |
| morgan-plus-four | NONE | (route: configure.morgan-motor.com/plusfour/ side camera, in the browser) |
