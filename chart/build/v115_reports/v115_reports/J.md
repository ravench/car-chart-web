# v1.15 picture search - Group J (quadricycles, second pass with Raven's Chrome)

Method: my own two Chrome tabs (both closed at the end; two pages froze while drawing large contact sheets and were closed and replaced). Pages, WordPress REST listings and contact sheets were drawn in the page, and originals were fetched with the hx worker (WebP q0.92, scale 1), moved with read_page and unpacked with unpack2.py into `ext/unpacked/v115/J/`. I viewed every saved file. No download buttons and no ?download=1 links were used.

---

## casalini-650
- **status: FOUND** (brand-own site, real studio photo, true side, current body)
- **Best: https://casalini.eu/wp-content/uploads/2026/09/CASALINI-starter-dx.jpg**
  - saved: `ext/unpacked/v115/J/casalini-650-side-starter-white.webp` (2048x1365)
  - Page: casalini.eu WordPress media library (uploaded 2026-09-03, title "CASALINI-starter-dx"). It belongs to a studio set of the same car: -front, -front-dx, -dx, -back-dx, -back-sx, -back.
  - View: white **650 Starter** with black 10-spoke alloys. It faces **right**, both wheels are full circles, and no front or rear face is visible apart from the wrap-around headlamp and tail-lamp edges seen from the side. Background is white studio with a soft floor shadow, and nothing stands in front of the car.
  - It is a real photo, not a render: the tyre sidewall text (HARMONIC MP270, MILEVER) is sharp and readable, and the 3:2 camera format fits. The camera sits slightly high, so a little of the bonnet top and wiper pivots shows. Cut-out should be easy (white car on white: use rembg or a manual mask on the outline).
- Alternate: https://casalini.eu/wp-content/uploads/2026/09/SPORTIVA-dx-Sienna-Brown.png
  - saved: `ext/unpacked/v115/J/casalini-650-side-sportiva-brown.webp` (1448x1086)
  - View: Sienna Brown **650 Sportiva** with bronze 5-spoke Casalini wheels and a "650 SPORTIVA" side stripe with an Italian flag. It faces right on a white background, and it is also a true side.
  - Caution: the pose and framing are identical to the white Starter photo, so this is most likely a digitally edited version of it (recolour, wheel swap, decal). The image is slightly soft or over-smoothed. Casalini's library also holds `Gemini_Generated_Image_*.jpg` files, so AI-assisted editing is possible. I saw no obvious artefact: the wheel geometry is coherent and the tyre text is plausible. Use it only if the Sportiva look is wanted; the Starter photo is safer.
- Checked and rejected. The library holds **91 items in total, all listed** via `/wp-json/wp/v2/media`:
  - `650.png` (1690x703) and `650-tras.png` (915x323): "650" wordmark logos, not cars.
  - The numbered colour renders (STARTER-*2/3/4/5, CASALINI-STARTER-7, SPORTIVA-*1-8, XTREME-*2/3/4/8; 1448x1086 or 1536x1024) are all 3/4 front views or straight fronts. None is a side view.
  - Colour-picker images `2026/10/{azzurro,arancio,blu-navy,nevy,bronzo,rosso-red,sea,miami,grigio-silver,sienna,nero,casalini-vertigo}.jpg`: straight fronts.
  - `2026/10/Gemini_Generated_Image_*.jpg`: AI street scenes, rejected.
  - `foto-home-1.png`: street scene, 3/4.
  - SPORTIVA-front-dx/-front-sx and starter-front-dx: 3/4 by name. -back-*: rear views.

## chatenet-ch46
- **status: FOUND, third-party, flag it** (catalogue image from 2019; the body appears unchanged, but the source is not the brand's)
- **Best: https://cdn-img.automoto.it/images/19232729/2000x/chatenet-ch-46-2019-04.jpg**
  - saved: `ext/unpacked/v115/J/chatenet-ch46-side-automoto2019.webp` (2000x1212)
  - Page: https://www.automoto.it/listino/chatenet/ch46/ch46-erre-erre/188806 (automoto.it price-list gallery, 5 images: rear, front, 3/4, **side**, interior). Source type: third-party catalogue (Italy); it looks like Chatenet's own studio or configurator image.
  - View: white body with a black roof and roof spoiler, black 10-spoke wheels with red callipers (Sportline / "Erre Erre" trim). It faces **left**, it is a true side with both wheels full circles, and the background is plain light grey studio.
  - Quality: soft, apparently upscaled from a smaller original, with visible JPEG artefacts. The car fills the frame almost edge to edge.
  - Body check (my inference, not stated anywhere): the 2026 brand images on automobiles-chatenet.com show the same shell. Rear lamps, rear bumper with round reflectors and twin exhausts, fuel flap, door and window lines, and grille shape all match. Only trim and wheels differ by version and year. No CH46 facelift is mentioned on the site.
- Checked and rejected:
  - automobiles-chatenet.com: every CH46 page (ch46-k-series, ch46-k-sl, ch46-k-sportline-rr, ch46e-sl-electrique, ch46e-sportline-rr-electrique, ch46-thermique, ch46e-electrique). That is 10 range images at 1200x800 under `/files/pack/contenu/Images/Gamme/...` (VISUEL-V-GRISE(1), V-GRISE-NUIT(1), V-ROUGE-LYCEE, base-visuel-1, VISUEL-V-BLANCHE, CH46 K SL ARRIERE-2026, CH46 SPORTLINE RR ARRIERE1-2026, CH46E-Arriere, CH46E SPORTLINE RR AVANT/ARRIERE-2026). All are 3/4 lifestyle scenes with people. Several look AI-generated: base-visuel-1_1_1.jpg seems to carry a small sparkle mark in its bottom-right corner, typical of Gemini output.
  - `personnalisez-votre-ch46.html`: 14 customer or dealer photos from 2021 (IMG_23xx/24xx, WhatsApp), all 3/4 views in car parks.
  - No brochure or PDF links on any CH46 page. The folder listing returns 403.
  - WebSearch for a CH46 importer or studio shots (NL, DE) found only used-car portals (autoscout24, viabovag, autobild, theparking, largus).

## ligier-js50
- **status: NONE**
- Checked:
  - Equipment sheet https://s3.ligier.fr/ligier-prod/uploads/2026/07/EN-FICHE-EQUIP.-JS50-EL-TH-P1-2026-1.pdf: 2 pages, both equipment tables, no pictures at all.
  - **store.ligier.fr configurator** (the JS50 "Configurer" button opens `configure?model_id=JS64`): the views are 3/4 front, 3/4 rear and rim. The image API pattern is `https://medias-api-store.ligiergroup.com/images/<config code, e.g. 6844ZZ14Z14>/outside/{front3Quarters|rear3Quarters|rims|top}/visual-<timestamp>.png` (1100x720). The store's own JS bundle declares GraphQL `OutsideImages { front3Quarters rear3Quarters rims top }`, and nothing else. I tried 19 other view names (side, profile, left, right, sideLeft, profil, lateral, ...) and every one fails. **The configurator has no side view.**
  - **ligier.de and ligier.nl** are not separate media libraries. Their `/wp-json/wp/v2/media` answers (ligier.de: 78 JS50 hits; ligier.nl: 157 "JS" hits), but every file is on the same `s3.ligier.fr/ligier-prod/uploads/...` bucket as ligier.fr, so it is the same library the main thread already checked. On ligier.de I viewed the files the earlier checks may have skipped (gamme-JS50, JS50.webp 2324x960, js50.webp 1920x1080, hero-js50, JS50-herobanner_v2, ligier-js50-m / -js50m, js50 620x587, js50-elec, JS50-electrique(-v2), js50-motor, Findomestic_JS50 banner, JS50-Elite_White_Revo-D-_3). All are 3/4 views or lifestyle scenes.
  - Mondial 2024 press kit https://media.ligier.fr/app/uploads/2024/11/Mondial-2024-Dossier-de-presse-FR.pdf (18 pages): pages 1-4 checked, showing 3/4 cut-outs (JS50, Myli) and scenes. **Pages 5-18 not checked** (the PDF viewer was slow and time ran out).
  - REST searches on www.ligier.fr for dimension, cote(s), profil(e), side, lateral(e), gabarit, encombrement, seitenansicht and zijkant: **0 hits**, so there is no dimension or profile image in the library. `lang=all` adds no files.
  - motor.es/ligier/js50: the JATO lead image `https://static.motor.es/fotos-jato/ligier/uploads/ligier-js50-66e33fa1941b9.jpg` (1200x800, viewed) is the **previous JS50** (old front), 3/4 front. The dimensions image `https://static.motor.es/fotos-marca/medidas/ligier-js50_mid66e4abb7c7e33.jpg` is only 450x300 and dates from Sept 2024, so it is probably the old body too. A cookie wall (accept or pay) blocked the rest of the gallery. I did not accept it and did not go further.
  - alvolante.it: placeholder only ("foto in arrivo").
  - www.ligier.ch: "Access forbidden" (403).
  - **Dealer (NL)**: viaBOVAG listing https://www.viabovag.nl/auto/aanbod/ligier-js50-ultimate-elektrisch-nieuw-2025-grootste-actieradius-alle-merken-rn5x5ly. It has 22 photos of a new grey/black JS50 Ultimate (current body) in a white-brick studio, at `https://stsharedprdweu.blob.core.windows.net/vehicles-media/659ef220-5948-4396-b87f-a19cf2a6754a/media.00NN-{640w,1024w,1280w,1920w}.jpg`. There is **no true side view**. The closest frame (17th in page order) is a near-side rear quarter with the tail lamp and part of the tailgate visible; another is a low front quarter with the roof cropped. Rejected.
  - Dealer (NL) 2: viaBOVAG https://www.viabovag.nl/auto/aanbod/ligier-brommobiel-js50-ultimate-12kw-nieuw-v2j9jn7 ("Ligier Partner" dealer, blue JS50 Ultimate, 24 photos). All are taken outdoors at the dealership (3/4 views, interior, details); no studio and no true side. Rejected.
  - viaBOVAG JS60 search hits are almost all the **previous** JS60 ("Chic Sun dCi"), so they are not usable.
- Not reached in time: other dealer listings (DE mobile.de, IT automobile.it, NL marktplaats; many new-car listings exist, and a dealer that shoots a full walk-around may have a pure side frame). ligier.it and ligier.es were not checked; they are probably the same shared library, as .de and .nl are.

## ligier-js60
- **status: NONE**
- Checked:
  - Equipment sheet https://s3.ligier.fr/ligier-prod/uploads/2026/09/EN-2026P2-FICHE-EQUIP.-JS60-EL-TH-1.pdf: 2 pages, equipment tables only, no pictures.
  - Configurator: store.ligier.fr has a JS60 "Configurer" button. It uses the same GraphQL `OutsideImages` type (front3Quarters, rear3Quarters, rims, top only), so it has no side view. I did not open the JS60 configurator separately.
  - ligier.nl and ligier.de libraries: same shared s3.ligier.fr bucket. The JS60 items there (Ligier-JS60-BIG-Tour-768x1024-1.webp, offres-js60.webp 412x368, js60.webp 451x333, Banniere-Ligier-JS60-et-concours-BIG-Tour-1.webp and Ligier-JS60-Ultimate-au-studio-bleu-1.webp, both 1672x941) are the ones the main thread already checked. I did not view them again.
  - Press release PDF https://media.ligier.fr/app/uploads/2026/09/2026.09-CP-NOUVELLE-JS60.pdf (5 pages). Page 1: scene (mountain road). Pages 2-3: lifestyle and detail photos. Page 4: a driving shot plus three small trim cut-outs at the bottom (red, grey, blue) that look like 3/4 front views, the same renders as the press-release photos already rejected. Page 5 not opened. No side view.
  - REST searches for dimension or profile terms on the shared library: 0 hits (see JS50).
- Not reached in time: dealer studio shots (as for JS50; the JS60 is new since Sept 2026, so there are few dealer listings yet).

---

## Summary
| model | status | best URL |
|---|---|---|
| ligier-js50 | NONE (configurator has only front3Quarters/rear3Quarters/rims/top; equipment sheet has no pictures; .de/.nl share the ligier.fr library; one NL dealer set has no true side) | - |
| ligier-js60 | NONE (same reasons; press-release PDF has only scenes and 3/4 cut-outs) | - |
| chatenet-ch46 | FOUND, third-party, flag it (2019 catalogue image, faces left, grey studio, 2000x1212 but soft) | https://cdn-img.automoto.it/images/19232729/2000x/chatenet-ch-46-2019-04.jpg -> `J/chatenet-ch46-side-automoto2019.webp` |
| casalini-650 | FOUND (brand site, real studio photo, faces right, white bg, 2048x1365) | https://casalini.eu/wp-content/uploads/2026/09/CASALINI-starter-dx.jpg -> `J/casalini-650-side-starter-white.webp` (alt Sportiva: `.../2026/09/SPORTIVA-dx-Sienna-Brown.png`, probably an edit of the same photo) |
