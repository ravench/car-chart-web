# v1.15 picture search: Group H report (Chrome pass)
Models: byd-ti-7, byd-shark, byd-sealion-5. Run 2026-11-01, about 22:10 to 22:27 UTC, through Raven's Chrome (own tabs only, all closed at the end; no downloads to disk, no cookie banners touched).
All files are in `ext/unpacked/v115/H/`. They were fetched same-origin from www.byd.com with the hx worker (WebP q 0.92, scale 1) and unpacked with unpack2.py. I opened every saved file with the Read tool.

Main finding: the byd.com/uk model pages use BYD Europe's "eu-v3" asset folders. On the Shark and Sealion 5 pages, each colour in the "exterior-gallery" picker has two frames: `1.webp` is a front 3/4 view and **`2.webp` is a true side view on white or transparent**. The Ti 7 UK page has only `1.webp` per colour (3/4). Its true side is the "Three-part silhouette" card picture.

---

## byd-ti-7
- status: **FOUND**
- file: `ext/unpacked/v115/H/byd-ti-7-side.webp`
- image URL (best): https://www.byd.com/material/byd-site/eu-v3/model/ti7/pc/exterior-detail/1.webp (972x1346, portrait)
- same photo, smaller: https://www.byd.com/material/byd-site/byd-uk/models/ti-7/model-page/TI-7%20_Side%20_%201.0.png (540x960; car only about 517 px long). Saved as `byd-ti-7-side-png540.webp`. Also https://www.byd.com/material/byd-site/eu-v3/model/ti7/mob/exterior-detail/1.webp (540x960).
- page: https://www.byd.com/uk/hybrid-cars/ti-7 , exterior-detail card "Three-part silhouette". The UK card JSON uses the PNG as pcImage. The 972 px webp is the eu-v3 asset for the same card and is referenced in the page HTML.
- source type: brand's own site (BYD UK), UK market. This is the European Ti 7 DM-p with BYD badges (not the Fangchengbao-badged Chinese Tai 7).
- verified by viewing the file:
  - true 90-degree side: both wheels are full circles, no front or rear face visible; the spare wheel on the tailgate shows in profile
  - faces RIGHT
  - Jade Green
  - studio photo: smooth pink-grey gradient backdrop, grey floor with a soft reflection and shadow, so it **needs background removal (rembg)**
  - the car spans about x=15 to 950, so it is about 935 px long and fully inside the frame (left-edge check: background at x 0-12, spare wheel starts at x 14)
- checked and rejected:
  - UK colour gallery `.../__EU/byd-site/byd-uk/models/ti-7/pc/exterior-gallery/{jadegreen,mountaingreen,obsidianblack,starlightsilver,titaniumgrey}/1.webp` (2816x1440): front 3/4 on a studio backdrop. There is no `2.webp` side frame: HEAD returns 404 for 2-12, and also in the eu-v3 and __EU/eu-v3 ti7/ti-7 folders.
  - herobanner `car-1.webp` (3840x720): 3/4. exterior-detail/2 (straight front) and /3 plus `TI-7 _Back _ 1.0_.png` (straight rear): not side views.
  - https://www.byd.com/uk/configurator/ti-7 shows the BYD error page "No related pages found". There is no Ti 7 configurator or 360 viewer on byd.com/uk.
  - Fangchengbao China https://www.fangchengbao.com/tai7 : colour picker `.../tai7chexiangye/3waiguan/chese/chese1/{lv,yin,lan,hei,cui,hui}-pc.jpg` (3840x1328) shows a front 3/4 in a scenic background with Fangchengbao badges, so it is rejected. `.../3waiguan/yinglangwaiguan/sanduanshi-pc.jpg` (the Chinese "three-part silhouette" card, probably the same side photo with Chinese badges) was **not viewed**: the tab froze twice on the large JPEG. It is not needed, because the UK picture has the European badges.

## byd-shark
- status: **FOUND**
- primary file: `ext/unpacked/v115/H/byd-shark-side.webp`
  - image URL: https://www.byd.com/material/__EU/byd-site/eu-v3/model/shark/pc/exterior-gallery/atlantisblue/2.webp
  - 2816x1440, RGB. Atlantis Blue on a **white background** with a soft grey floor shadow running out to the right.
  - true side, faces LEFT. The car is about 1712 px long (x 600 to 2312).
- alternates, transparent cut-outs (no background removal needed, but the soft shadow sits in the alpha channel and runs to the right edge):
  - `byd-shark-side-white.webp`: https://www.byd.com/material/__EU/byd-site/eu-v3/model/shark/pc/exterior-gallery/polarwhite/2.webp (1408x720 RGBA, Polar White, faces left, car about 859 px long, x 296 to 1155)
  - `byd-shark-side-black.webp`: https://www.byd.com/material/__EU/byd-site/eu-v3/model/shark/pc/exterior-gallery/obsidianblack/2.webp (1408x720 RGBA, same pose)
  - seen on the contact sheet only, not fetched: `.../greygreen/2.webp` (2816x1440, white background) and `.../sunriseorange/2.webp` (1408x720)
- page: https://www.byd.com/uk/hybrid-cars/shark , colour picker (exterior gallery). Brand's own site (BYD UK, eu-v3 folder), UK market.
- verified by viewing all three files:
  - both wheels full circles, no front or rear face
  - current body: the "BYD" letter grille Shark sold in the UK (Shark 6 in Australia)
- other pictures on the page:
  - colour `1.webp` frames: front 3/4
  - `pc/exterior-detail/2.webp` (1458x2019): a true side of the blue car in a dark studio, usable as a backup but needs rembg
  - `pc/exterior-dimension/1.webp` (2880x1440): photo-real 3-view with dimension lines, not needed
  - herobanner / exterior/1: 3/4 scenes
- not checked: the Business Wire launch photo, because the official UK site already has a better white-background side view.

## byd-sealion-5
- status: **FOUND**. This replaces the byd.ch dimension drawing.
- primary file: `ext/unpacked/v115/H/byd-sealion-5-side.webp`
  - image URL: https://www.byd.com/material/byd-site/eu-v3/model/sealion5-dm-i/pc/exterior-gallery/altantisblue/2.webp ("altantis" is BYD's own spelling in the path)
  - 2816x1440 RGBA, **transparent cut-out** with a soft shadow under the car in the alpha channel
  - Atlantis Blue, faces LEFT, car about 1614 px long (x 624 to 2238)
- alternate: `byd-sealion-5-side-white.webp`: https://www.byd.com/material/byd-site/eu-v3/model/sealion5-dm-i/pc/exterior-gallery/white/2.webp (2816x1440 RGBA, same pose, white car). Contact sheet also shows `.../timegrey/2.webp` and `.../black/2.webp` in the same pose (not fetched).
- page: https://www.byd.com/uk/hybrid-cars/sealion-5-dm-i , colour picker. Brand's own site (BYD UK, eu-v3 folder, the same assets as byd.com/eu), UK market.
- verified by viewing:
  - wheels are round: rims about 195x195 px front and 190x190 px rear in crops
  - no front or rear face; only the grille edge where it wraps round the bumper corner shows, as on any profile of this car
- body check: I put this image next to the byd.ch 3-view drawing already in the chart (`ext/unpacked/china/byd-sealion-5-side`, centre view). Headlamp, grille edge, roof rails, spoiler, D-pillar glass pattern, fuel flap, twin-spoke wheels, tail lamp and rear bumper vents are identical. So it is the European Sealion 5 DM-i body (Song Pro DM-i based), not the 2026 Chinese Sealion 05. I did not open byd.ch itself in this pass.
- other pictures on the page:
  - colour `1.webp` frames: front 3/4. `3.webp` and `4.webp` do not exist (404).
  - exterior-detail 1 and 2: scenes; 3: rear detail; 4: wheel
  - exterior/1: 3/4 studio
  - exterior-dimension/1: the 3-view drawing already used

---

## Processing notes for the main thread
- Ti 7: gradient studio background and floor reflection, so run rembg. Faces right.
- Shark primary: white background with a shadow to the right, so use rembg or a white threshold. Faces left. The 1408 px cut-outs are an alternative with no rembg, but their soft shadow is in the alpha channel and runs to the right edge.
- Sealion 5: already transparent. Drop the low-alpha dark shadow pixels (alpha below about 200) under the sills if the chart wants no shadow. Faces left.

## Summary
| model | status | best URL |
|---|---|---|
| byd-ti-7 | FOUND (brand UK site, studio gradient bg, faces right, 972x1346, car about 935 px) | https://www.byd.com/material/byd-site/eu-v3/model/ti7/pc/exterior-detail/1.webp |
| byd-shark | FOUND (brand UK site, white bg, faces left, 2816x1440, car about 1712 px; transparent 1408 px alternates) | https://www.byd.com/material/__EU/byd-site/eu-v3/model/shark/pc/exterior-gallery/atlantisblue/2.webp |
| byd-sealion-5 | FOUND (brand UK site, transparent, faces left, 2816x1440, car about 1614 px; EU body checked against the byd.ch drawing) | https://www.byd.com/material/byd-site/eu-v3/model/sealion5-dm-i/pc/exterior-gallery/altantisblue/2.webp |
