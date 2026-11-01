# v1.15 picture search: Group F report (browser pass)
Models: xpeng-l03, xpeng-g9l, denza-z9-gt, denza-d9. Run 2026-11-01, 22:11 to 22:33 UTC, through Raven's Chrome (one own tab, now closed).
Downloads: `ext/unpacked/v115/F/` (WebP, q 0.92, each with `.meta.json`). I opened and checked every file listed as FOUND.

Main finding: the brands' own **European websites** have clean studio or configurator side views for all four models. They are better than the press-kit photos from the first pass. The press-kit side photos are saved too, as alternates (location backgrounds).

---

## xpeng-l03
- status: **FOUND**
- **primary: `xpeng-l03-side-cfg.webp`** (2048x1536, RGBA, **transparent background**, car bbox x 246-1887 / y 518-1052, so the car is about 1640 px wide; includes a soft ground shadow in the alpha)
  - image URL: `https://static-resource.xpeng.com/xp-dragon/otd/prod/140377500160704/2026-07-07/c15d9bcaa45947f18ecf8042f9a42710.png` (original PNG, 782 KB)
  - page: https://store.xpeng.com/de/configurator/L03 (the "Jetzt konfigurieren" link on xpeng.com/de/model/L03), exterior carousel frame 2 of 3. Source type: brand configurator, market DE/EU.
  - verified: viewed the saved file (composited on white). White body, black roof, Giti tyres. **Faces left.** Near-true side: both wheels are full circles; only the outer edge of the headlight is visible. Current body (EU launch model 2026).
- **alternate: `xpeng-l03-side.webp`** (2637x1483 RGB = original 8789x4942 scaled 0.3)
  - URL: `https://d21buns5ku92am.cloudfront.net/70232/images/688183-XPENG%20L03_003-9bab03-original-1783951666.jpg` (24.6 MB JPEG)
  - page: XPeng Switzerland newsroom media kit https://xpengswitzerland.pr.co/assets/240537/ ("XPENG L03_003"). Source type: press, market CH.
  - verified: viewed. Purple with yellow calipers, **faces right**, true side with a tiny front sliver. Location shot (corrugated glass façade, asphalt), so it needs rembg.
- checked / rejected (contact sheets of all 40 numbered shots):
  - L03_001/002/005/013: 3/4 views with people
  - L03_004, 006-012, 014-016: 3/4, rear, top or front views
  - L03_017-019, 022, 023, 025-032: 3/4 or front views
  - L03_020: side view, but a person and a dog sit on steps right behind the car
  - L03_021: car small in the frame, slight 3/4
  - L03_024 ("Station Grill"): slight 3/4
  - L03_033-040: details
  - _MOP*: Munich event photos
  - named files: interior details
  - xpeng.com/de/model/L03 images:
    - PC-P2-1: the L03_020 scene with person and dog
    - PC-P5: drag-coefficient visual with streamlines over a side view
    - all other images are 3/4 views, details or interiors
  - configurator frames 1 (`59749cd732524d6da964472d2f406686.png`) and 3 (`1061487f7fc24af5bbf6ba921350e19d.png`): 3/4 views

## xpeng-g9l
- status: **FOUND**
- **primary: `xpeng-g9l-side-cfg.webp`** (2048x1536, RGBA, **transparent background**, car bbox x 249-1746 / y 524-1069, so the car is about 1500 px wide)
  - image URL: `https://static-resource.xpeng.com/xp-dragon/otd/prod/140377500160704/2026-10-02/7bdf37f6c99c413b85b89ff4bf793fc6.png`. The page itself loads the same path from `https://xp-dragon-base-public-prod.oss-eu-central-1.aliyuncs.com/...`, which has no CORS. The static-resource.xpeng.com mirror does allow CORS.
  - page: https://store.xpeng.com/de/configurator/G9L, exterior carousel frame 2 of 3. Source type: brand configurator, market DE/EU.
  - verified: viewed. Silver-white, Michelin tyres, **faces left.** Near-true side: both wheels are full circles; the thin front light bar and a sliver of the front bumper are visible. This is the G9L configurator, so it is not the GX (the risk flagged in C.md). The silhouette matches the official G9L press photo below: D-pillar, rear quarter window, roof spoiler.
- **alternate: `xpeng-g9l-side.webp`** (2600x1463 RGB = original 4000x2250 scaled 0.65)
  - URL: `https://d21buns5ku92am.cloudfront.net/70232/images/710037-XPENG%20G9L_001-0647f2-original-1791808258.jpg`
  - page: https://xpengswitzerland.pr.co/273192-neuer-xpeng-g9l-feiert-europapremiere-auf-dem-pariser-automobilsalon/ ("XPENG G9L_001"). Source type: press, market CH.
  - verified: viewed. Dark green, **faces right**, true side (light-bar edge visible). Street scene, so it needs rembg.
- checked / rejected:
  - G9L_002-_006: 3/4, splash, rear or detail shots
  - G9L_007-_011 (both sets): frunk, wheel, interior
  - configurator frames 1 (`29541c73cde540c3a475dcf82b95b12c.png`) and 3 (`e4efb61abc1c495795f6f80b77c333f3.png`): front 3/4 from either side

## denza-z9-gt
- status: **FOUND**
- **primary: `denza-z9-gt-side-studio.webp`** (2400x1200 RGB, the original size; the car is about 1850 px wide)
  - image URL: `https://www.denza.com/material/denza-overseas/eu/model/z9gt/eu-model-introduction/exterior/2-pc.webp`
  - page: https://www.denza.com/de/z9gt ("eu-model-introduction" exterior image 2). Source type: brand-own site, market DE/EU.
  - verified: viewed. Teal-green, **faces left.** Light blue-grey studio background with a soft floor reflection, inside a rounded-corner card. Near-true side: both wheels are near-full circles; the headlight and a sliver of the front intake are visible.
- **alternate: `denza-z9-gt-side.webp`** (3000x2001 RGB = original 5000x3335 scaled 0.6; the car is about 1480 px wide)
  - URL: `https://cdn.uc.assets.prezly.com/d43612d1-4945-45a6-a071-f86a394507dd/DENZA_Z9GT_02STATIC_035.jpg` (cdn.assets.prezly.com redirects there)
  - page: Denza Europe launch kit https://press.bydauto.be/denza-goes-global-with-technology-drives-elegance (DENZA_Z9GT_02STATIC_035). Source type: press, BE/EU.
  - verified: viewed. Same teal car, **faces left**, true side (only the edges of the head and tail lights are visible). Paris Rue de Rivoli arcade background, so it needs rembg. It may be slightly more exactly side-on than the studio picture, but its background is busier.
- checked / rejected:
  - press kit STATIC_038, 040, 041, 043, 046, 047, 048, 051: 3/4 or two-car shots
  - 0C4A* Paris event photos: 3/4, car tiny in the frame, or person in front
  - EU site eu-model-introduction/exterior/1: front
  - EU site eu-model-introduction/exterior/3: front 3/4 detail
  - EU site cardesign/exterior/1 and model-optionals/1: 3/4
  - no configurator link was found on denza.com/de/z9gt

## denza-d9
- status: **FOUND** (near-true side; a slight front angle, more than the others)
- **primary: `denza-d9-side.webp`** (2400x1200 RGB, the original size; the car is about 1630 px wide)
  - image URL: `https://www.denza.com/material/denza-overseas/eu/model/d9/eu-model-introduction/exterior/2-pc.webp`
  - page: https://www.denza.com/de/d9 ("eu-model-introduction" exterior image 2). Source type: brand-own site, market DE/EU.
  - verified: viewed. Dark blue, Michelin tyres, **faces left.** Studio gradient background (beige to lavender) with a floor shadow. Both wheels are near-full circles, but part of the grille edge and headlight face is visible, an estimated 5-8 degrees off true side. It is usable; the main thread should judge.
- body check: this picture comes from the European site itself, so it shows the European D9 as marketed. **I did not use any Asian picture.** The companion straight front from the same studio set and colour is saved as `denza-d9-front-eu.webp` (eu-model-introduction/exterior/1-pc.webp, 2400x1200). It shows the EU front: large black grille with horizontal slats, slim LED headlights, chrome C-shaped corner intakes, "DENZA D9" plate. It can also serve as the D9 front tile.
- checked / rejected:
  - cardesign/exterior/1-pc.webp (3840x2160): 3/4 front; cardesign/exterior/2-6 do not exist
  - eu-model-introduction/exterior/3: 3/4 front crop
  - eu-model-introduction/exterior/4: does not exist
  - safetyeu/1: scene
  - the D9 page has no colour picker or configurator ("in Kürze")

---

## Configurator / 360 notes (URL patterns)
- **XPeng EU configurator** (`https://store.xpeng.com/de/configurator/<L03|G9L>`): this is not a 360 viewer. Each colour or trim gets a 3-frame carousel of 2048x1536 transparent PNGs with hashed names: `https://static-resource.xpeng.com/xp-dragon/otd/prod/140377500160704/<yyyy-mm-dd>/<32hex>.png`. Frame 2 is the side view for both models. There is no angle or frame parameter in the URL. The same path is on `xp-dragon-base-public-prod.oss-eu-central-1.aliyuncs.com`, which has no CORS; fetch from static-resource.xpeng.com instead.
- **Denza EU site**: `https://www.denza.com/material/denza-overseas/eu/model/<d9|z9gt>/eu-model-introduction/exterior/<n>-pc.webp`. n=2 is the side view for both models, n=1 the front, n=3 a 3/4 detail. `-mob.webp` variants exist for mobile. The same scheme probably applies to the other Denza EU models (z, bao5); I did not check that.
- I did not open the Chinese xpeng.com / denza.com 360 viewers, because the EU sources already gave official clean side views.

## Summary
| model | status | best file (ext/unpacked/v115/F/) | best URL |
|---|---|---|---|
| xpeng-l03 | FOUND (configurator, transparent bg, faces left) | xpeng-l03-side-cfg.webp (alt xpeng-l03-side.webp, press CH, faces right) | https://static-resource.xpeng.com/xp-dragon/otd/prod/140377500160704/2026-07-07/c15d9bcaa45947f18ecf8042f9a42710.png |
| xpeng-g9l | FOUND (configurator, transparent bg, faces left) | xpeng-g9l-side-cfg.webp (alt xpeng-g9l-side.webp, press CH, faces right) | https://static-resource.xpeng.com/xp-dragon/otd/prod/140377500160704/2026-10-02/7bdf37f6c99c413b85b89ff4bf793fc6.png |
| denza-z9-gt | FOUND (brand site, studio bg, faces left) | denza-z9-gt-side-studio.webp (alt denza-z9-gt-side.webp, press EU, Rue de Rivoli) | https://www.denza.com/material/denza-overseas/eu/model/z9gt/eu-model-introduction/exterior/2-pc.webp |
| denza-d9 | FOUND (brand EU site, studio bg, faces left, slight front angle) | denza-d9-side.webp (+ denza-d9-front-eu.webp straight front) | https://www.denza.com/material/denza-overseas/eu/model/d9/eu-model-introduction/exterior/2-pc.webp |
