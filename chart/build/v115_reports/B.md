# v1.15 picture search - Group B report

## Read this first
- **No originals were downloaded.** From this container, `curl` gets `CONNECT tunnel failed, response 403` (proxy policy denial) for every car host tried: galaxy.geely.com, www.geely.com, lepas.co.uk, lepasauto.com, farizonauto.co.uk, farizon.eu, wey.com, voyah.com.cn, voyah.nl, mhero.com, and also en.wikipedia.org, zigwheels.ae, carsized.com and google.com. WebFetch cannot open image files either (it returns a server error).
- So I checked every candidate in Claude in Chrome, in my own tab. I loaded the original URL, read `naturalWidth` and `naturalHeight`, and looked at it in a screenshot.
- The files in `ext/unpacked/v115/B/` are **screenshot previews only**: JPEG, downscaled, not the original files. They show what I saw and are not for the chart. Please fetch the originals listed below through the browser.
- Because nothing was downloaded, "CANDIDATE (verified in Chrome)" means: I saw the image itself at its original URL, and the view, body, size and background are confirmed.

---

## geely-starray-em-i
- **Status: CANDIDATE (verified in Chrome)**: a true side view from the brand's own 360-degree viewer. It is better than the zigwheels side currently in the chart.
- **360-viewer URL pattern** (geely.de model page, Nuxt `FrameSequence` component):
  `https://assets.geelyauto.eu/__frames__/exterior/starray-em-i/lhd/23f/<colour>/<NN>.jpg`
  - Colours: `silver`, `white`, `grey`, `black`, `green`, `blue`.
  - Frames: `00`-`23` (24 frames, 15 degrees apart). `24` and above do not exist.
  - Every frame is **2100x1050 JPG on a white studio background** with a soft shadow. The page itself adds `?x-oss-process=image/format,webp`, but the plain `.jpg` without it opens at full size.
  - Positions: **frame 18 = true side, facing LEFT**; **frame 06 = true side, facing RIGHT**; 00 = straight front; 12 = straight rear.
- **Best URL:** `https://assets.geelyauto.eu/__frames__/exterior/starray-em-i/lhd/23f/white/18.jpg`
  - Car: silver-white with two-tone 5-twin-spoke wheels.
  - The car's bounding box is about x 192-1540 by y 280-750, so the car is about 1350 px long. It sits left of centre in the frame.
  - Both wheels are full circles and there is no front or rear face. I viewed it large.
  - Preview: `B/geely-starray-em-i-side_f18_PREVIEW-screenshot.jpg`. Contact sheet of all 24 frames: `B/geely-starray-em-i-360-contactsheet_PREVIEW.jpg`.
- **Bonus front view:** `.../23f/white/00.jpg` is a straight front on white, 2100x1050. It could replace the current zigwheels front.
- **Page:** https://www.geely.de/models/geely-starray-em-i (section "DREHEN SIE IHN, WIE SIE WOLLEN"). Brand-own site, DE market. The car shown is the EU Starray EM-i.
- **Checked and rejected:**
  - geely.de colour-picker files `starray-emi-colours-ext-*.png` are 160x160 swatch spheres.
  - `*-1.png` files are 192x192 swatches.
  - `front-side-interior*.jpg` (1920x1148) are interior shots.
  - `starray-hero-motiv_*` is the hero image, not a side view.

## lepas-l8
- **Status: CANDIDATE (verified in Chrome)**: a true side studio shot from the brand's international site.
- **URL:** `https://www.lepasinternational.com/data/cms/archive/202509(4)/1758526033549513.jpg`
  - The parentheses may need encoding: `202509%284%29`.
  - Size and background: **742x450 JPG**, grey studio wall, light floor with a reflection of the car.
  - View: true side, **faces RIGHT**. Teal-green car, multi-spoke two-tone wheels. The car is about 670 px long, so it meets the minimum but is below the ideal 800 px.
  - It shows the current Lepas L8 nose (slim LED strip and vertical intake). I viewed it at about 1:1.
  - Preview: `B/lepas-l8-side_PREVIEW-screenshot.jpg`.
- **Page:** https://www.lepasinternational.com/models/lepasl8/lepasl8phev/index.shtml (exterior design carousel, all 742x450). Brand-own international site. Wikipedia lists lepasinternational.com as the official site and describes the L8 as a rebadged second-generation Chery Tiggo 8.
- **Checked and rejected:**
  - www.lepas.co.uk now redirects to the Bassetts dealer page (bassettsgroup.co.uk/lepas/), which has 3/4 and scene slides only.
  - lepasauto.com and lepas.com show a Chrome error page (no site).
  - On lepasinternational.com, the colour images (1920x960: 1766559614980106.jpg, 1766559653071360.jpg, 1785315621955139.jpg, 1785314839558335.jpg, 1766559823722284.jpg) are 3/4 front shots on a seaside set.
  - Other images on that site are 3/4 views, lifestyle scenes, details and interiors.
  - Arnold Clark: already rejected earlier (nose, rear and swatches only).

## farizon-sv
- **Status: CANDIDATE (verified in Chrome)**: brand UK site (farizonauto.co.uk, run by the official importer Jameel Motors). Studio cut-outs on a **transparent background**, one per body version.
- **Best URL (L1 H1 = 4990 mm, which matches the chart length):**
  `https://d2e4u25u6oksl8.cloudfront.net/farizon/d1574736daac0f095ab5955352652dfd19cc4082_18d3276967.png`
  - 4096x2116 PNG, alpha background. White van, true side, **faces LEFT**, both wheels full circles, soft floor shadow.
  - Page card text right before the image: "L1 H1 L4990 x H1980 mm, 6.95 m3"; alt text "Featured Version".
  - Preview: `B/farizon-sv-L1H1-side_PREVIEW-screenshot.jpg`.
- **Other versions** on the same page, all true sides facing left on transparent backgrounds:
  - L1 H2 (4990 x 2180): `.../farizon/ce17dfc364988d928cfcd34d39f9e0ff88ffbc46_ce2ffff535.png`, 4096x2116. It looked almost identical to the L1H1 image.
  - L2 H2 (5490 x 2180): `.../farizon/c51aa166bd1ca0feabf26a5a8e881ad8d00d8673_901ed16fe2.png`, 4096x1917.
  - L2 H3 (5490 x 2500): `.../farizon/1da508ee263347023a67a224b2001ab57bc6077a_45ca333a8c.png`, 4096x1917.
  - SV Sport (L4990, black alloys and skirts): `.../farizon/f98849a9d32e6cc66b3d803f9ae8a26cedd42942_1_1fabca3a3f.png`, 4096x2732. A smaller copy, `SV_Sport_Side_view_WHITE_1_3b0115c715.png` (880x410), is in the configurator.
- **Page:** https://farizonauto.co.uk/our-range/sv-range/product-detail/ (UK market).
- **Checked and rejected:**
  - `L3_H3_Configurator_NEW_fd6af33b66.png` is 3/4.
  - `Group_21510_3_1_a4e99219f9.png` is a graphic with orange stripes.
  - `l1_e3da8e7913.webp` is 424x242, too small.
  - Other images on the page are hero, driving, detail and interior shots.

## farizon-v7e
- **Status: CANDIDATE (verified in Chrome)**: brand UK configurator image.
- **URL:** `https://d2e4u25u6oksl8.cloudfront.net/farizon/Mask_group_c782cac494.png`
  - **878x534 PNG, transparent background** with a soft shadow. Alt text "FARIZON V7E".
  - Shows the configurator model card "FARIZON V7E - BUILT FOR THE CITY. MAXIMUM AGILITY. Starting from GBP 28,000".
  - White/silver van, true side, **faces LEFT**, about 860 px long.
  - This is the V7E nose, not the SV's black mask; I checked it against the V7E page shots.
  - Preview: `B/farizon-v7e-side_PREVIEW-screenshot.jpg`.
- **Page:** https://farizonauto.co.uk/configurator/ (redirects to `?step=1&configurator=farizon-v7e`). UK market. I did not open the later configurator steps (5. DESIGN might hold larger colour sides).
- **Fallback:** on https://farizonauto.co.uk/our-range/farizon-v7e/, `hotspot_new_af2738343e.png` (2100x1082) is a true side facing right, but with the sliding door open and an outdoor scene behind it.
- **Checked and rejected:**
  - `Mask_group_7c36f61a24.webp` and `sk_group_1_da29a5cbab.webp` (2220x1024 cut-outs) are 3/4 front.
  - Other V7E page images are hero, driving, interior, rear-doors and charging shots.

## wey-wey-03
- **Status: NONE.**
- **Identity:** Wikipedia says Wey 03 = **Wey Latte DHT-PHEV**: sold in Europe as "Wey Coffee 02" until the end of 2023 and as "GWM Wey 03" from 2024, length **4,668 mm**. The carnewschina "wey-03-dht-phev" entry redirects to wey-latte-phev.
- **Possible chart data errors:** the chart's 4520 mm is the Wey Macchiato's length, and Lanshan is a 5 m six-seater, so the "Lanshan" alias looks wrong. Please check both.
- **Checked:** wey.com (China) now links only to Lanshan and Gaoshan pages (lanshan.html, lanshan-new.html, gaoshan.html, gaoshan-intelligence.html). No Latte or Mocha page is linked anymore.
- **Not reached in time:** gwm.de and gwm-global.com Wey 03 pages; the Euro NCAP "WEY 03 (Coffee 02)" page.

## wey-wey-05
- **Status: NONE.**
- **Identity:** Wey 05 = Wey Coffee 01 = Wey Mocha (China).
- **Checked:** wey.com (China) has no Mocha page anymore (same as above). gwm.ch was already rejected earlier (3/4).
- **Not reached in time:** gwm.de / GWM Europe Wey 05 pages; Euro NCAP "WEY Coffee 01".

## mhero-mhero-i
- **Status: NONE.**
- **Checked and rejected:**
  - www.mhero.com does not load (Chrome error page).
  - voyah.nl menu image `MHERO I _ 4.jpg` (1920x1280) is a 3/4 off-road scene, as rejected earlier.
  - A Chinese web search ("猛士917 官网 外观 颜色 侧面") found only third-party pages: autohome, sohu, carnewschina.
- **Not tried:** the Chinese M-Hero site under a different domain; the M-Hero Middle East sites.

## voyah-dream
- **Status: CANDIDATE (verified in Chrome)**: an alternative to the existing voyah.nl wooden-wall scene. It is also a scene photo, so it needs rembg.
- **URL:** `https://www.voyah.com.cn/voyah-resources/images/car/dreamer/bg_swiper_25_3.jpg`
  - **3840x2160 JPG.** Dark plum Dream in front of a dark glass building on a stone pavement.
  - View: true side, **faces LEFT**, both wheels full circles. The car is about 2000 px long.
  - Preview: `B/voyah-dream-side_bg_swiper_25_3_PREVIEW-screenshot.jpg`.
- **Page:** https://www.voyah.com.cn/dreamer.html, titled "24款岚图梦想家" (China MY2024 Dreamer). Brand-own site, China market.
- **Body check:** same body and side profile as the EU Dream. The Chinese facelifts changed mostly the lights and grille; please check the nose against the voyah.nl car.
- **Checked and rejected:**
  - voyah.nl/voyah-dream `Voyah Dream 1.webp` (1920x1281) is a side view with the sliding door open in a garden scene; no better than the current image.
  - On voyah.com.cn/dreamer.html: `bg_swiper_27_1.jpg` is a near-side driving shot with the front visible (3/4); `bg_6_1920.jpg` is 3/4 with the door open; `bg_swiper_7_3.jpg` is 3/4 at a distance; everything else is 3/4, scene or interior.
- **Not opened:** newDreamer.html, newDreamer26.html and dreamer-champion.html on voyah.com.cn (newer versions; check whether they have a colour picker).

---

## Summary
| model | status | best URL |
|---|---|---|
| geely-starray-em-i | CANDIDATE (verified in Chrome; 360 frame 18 = side facing left, 06 = side facing right, 00 = front) | https://assets.geelyauto.eu/__frames__/exterior/starray-em-i/lhd/23f/white/18.jpg |
| lepas-l8 | CANDIDATE (verified in Chrome; 742x450, grey studio, faces right) | https://www.lepasinternational.com/data/cms/archive/202509(4)/1758526033549513.jpg |
| farizon-sv | CANDIDATE (verified in Chrome; L1H1, 4096x2116, transparent, faces left) | https://d2e4u25u6oksl8.cloudfront.net/farizon/d1574736daac0f095ab5955352652dfd19cc4082_18d3276967.png |
| farizon-v7e | CANDIDATE (verified in Chrome; 878x534, transparent, faces left) | https://d2e4u25u6oksl8.cloudfront.net/farizon/Mask_group_c782cac494.png |
| wey-wey-03 | NONE (twin = Wey Latte; check the chart's 4520 mm length) | - |
| wey-wey-05 | NONE | - |
| mhero-mhero-i | NONE | - |
| voyah-dream | CANDIDATE (verified in Chrome; dark scene, rembg needed; alternative to the current image) | https://www.voyah.com.cn/voyah-resources/images/car/dreamer/bg_swiper_25_3.jpg |
