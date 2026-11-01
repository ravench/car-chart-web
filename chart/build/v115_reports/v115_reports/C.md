# v1.15 picture search: Group C report
(byd-ti-7, byd-shark, byd-sealion-5, denza-z9-gt, denza-d9, xpeng-l03, xpeng-g9l). Run 2026-11-01, 21:46 to 22:05 UTC.

## Read this first: nothing could be downloaded or viewed
- The container's egress proxy refuses CONNECT (policy 403) to every host needed here: www.byd.com, www.denza.com, www.xpeng.com, s.xiaopeng.com, xps01.xiaopeng.com, www.xiaopeng.com, www.bydauto.com.cn, www.fangchengbao.com, en.wikipedia.org, images.unsplash.com and others (proxy status `recentRelayFailures: connect_rejected`). Per the proxy README I did not retry or route around it.
- WebFetch cannot fetch binary images (SERVER_ERROR on byd.com and s-cdn.xpeng.com image URLs). So I could not view any picture, and `ext/unpacked/v115/C/` is **empty**.
- So every status below is CANDIDATE (URL found, angle not confirmed) or NONE. None of the angle claims comes from my own viewing. The evidence is file names, captions, alt text and page context only.
- A trick that works: XPeng's CDNs (Aliyun OSS) answer `?x-oss-process=image/info` with JSON (width, height, size), and WebFetch can read that. I used it to check the colour-section PNGs on the Chinese XPeng pages: they are 84x84 swatches, not car renders. For full size or re-scaled copies, the main thread can try `?x-oss-process=image/resize,w_2000`.
- 360 viewers and configurators: none of the static HTML holds frame URLs. byd.com/uk and denza.com/de render everything client-side (WebFetch sees only `byd-share.jpg`). xpeng.com and xiaopeng.com load the colour-selector car renders by JS. I found **no 360 URL pattern or side frame number**. The main thread would have to read them from the browser's network panel.

---

## byd-ti-7
- status: **NONE**
- Chinese twin: Fangchengbao Tai 7 (钛7), launched in China 9 Sep 2025 (IT之家). The UK car is the DM-p PHEV.
- checked / rejected:
  - https://www.byd.com/uk/hybrid-cars/ti-7: client-rendered. WebFetch sees only the share image, and curl is blocked by the proxy. **Recommend the main thread opens it in the browser** and checks the colour picker and dimension sections.
  - zigwheels.ae gallery https://www.zigwheels.ae/new-cars/byd/ti-7/images: 8 exterior images (front angle low, full front, headlight, wheel, grille, logo, medium-angle front, tilted front). No side view. The 7 colour images (`https://imagecdn.zigwheels.ae/large/gallery/color/107/2523/byd-ti7-color-*.jpg`, e.g. -562219 Obsidian Black) do not state their angle; zigwheels colour images are normally 3/4. Rejected (third-party, no side).
  - autoevolution UK launch article (6 photos credited "BYD", lead photo "BYD / edited"): `https://s1.cdn.autoevolution.com/images/news/gallery/new-byd-ti-7-targets-three-row-crossover-buyers-with-47995-starting-price_{1..6}.jpg`. Angles unknown and third-party. Only a last resort if one of them happens to be a profile.
  - carmagazine.co.uk "first official pictures": WebFetch got no image data.

## byd-shark
- status: **NONE**
- checked / rejected:
  - https://www.byd.com/uk/hybrid-cars/shark: client-rendered, same as above. Its meta description even refers to the Dolphin G DM-i. **Recommend checking it in the browser.**
  - BYD's official launch release (Mexico City, 15 May 2024, Business Wire): https://www.businesswire.com/news/home/20240515408443/ja. Main photo `https://mms.businesswire.com/media/20240515408443/ja/2132851/5/BYD_SHARK.jpg?download=1` (official, current body; caption only "Photo: Business Wire", so the angle is unknown). The other photos are Venue, Stella, platform, V2L, NFC and camera shots, so they are not exterior profiles. Worth one look in the browser.
  - Australian Shark 6 (same body): only third-party pages (carsguide, carexpert dimensions, chasingcars colours). vehiclesizes.com "front and side view" = 3/4 (and Cloudflare per earlier notes).
  - zigwheels.ae "Front Side View" was already rejected as 3/4 (brief).

## byd-sealion-5
- status: **CANDIDATE (weak)**. The current byd.ch dimension drawing stays the fallback.
- candidates:
  1. zigwheels.ph gallery https://www.zigwheels.ph/new-cars/byd/sealion-5-dm-i/images lists exterior image #4, alt "Sealion 5 DM-i Side view", caption "Side View (Left)". The real URL is lazy-loaded and not in the HTML (the only CDN image is `https://imgcdn.zigwheels.ph/medium/gallery/exterior/64/3766/byd-sealion-5-dm-i-82451.jpg`, the hero). The side file should sit under `https://imgcdn.zigwheels.ph/large/gallery/exterior/64/3766/` but I could not get its name. Third-party (manufacturer studio photo per zigwheels practice), Philippine market. zigwheels.ph was geo-blocked for the main browser per the brief.
  2. Official BYD Belgium press site (Prezly, Inchcape Belgium), album "BYD Song Pro 2026", 14 images named 1.jpg-14.jpg: https://press.bydauto.be/media/album/3c9494e4-80e0-434f-9832-9b4646c01f9e (e.g. `https://cdn.assets.prezly.com/643825c0-8ea4-4c34-b1e3-7d207cc2a699/-/preview/-/format/auto/1.jpg`, a ZIP via the page's Download button). **Unsure** whether "Song Pro 2026" is the European Sealion 5 DM-i body. China launched a new Sealion 05 DM-i in April 2026 (carnewschina 2026-04-16), so check the body against the UK car before using any picture.
- checked / rejected: byd.com/uk/hybrid-cars/sealion-5-dm-i (client-rendered); zigwheels.ph brochure page (no PDF link in the HTML).

## denza-z9-gt
- status: **CANDIDATE (good source, angle unconfirmed)**
- source: the official Denza Europe launch press kit on the BYD Belgium press site (press, EU): https://press.bydauto.be/denza-goes-global-with-technology-drives-elegance, gallery "DENZA Z9GT" (56 images, 48 shown before "Show more").
- most likely side candidates are the static shots `DENZA_Z9GT_02STATIC_0xx`. Preview URLs (Prezly/Uploadcare; drop `-/preview/-/format/auto/` for the original):
  - 035 `https://cdn.assets.prezly.com/d43612d1-4945-45a6-a071-f86a394507dd/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_035.jpg`
  - 038 `https://cdn.assets.prezly.com/0adf40d6-260c-4c1a-95d6-cb8717c9bc3b/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_038.jpg`
  - 040 `https://cdn.assets.prezly.com/60911875-04a8-4951-8290-86c1016b9633/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_040.jpg`
  - 041 `https://cdn.assets.prezly.com/d85135cd-2417-40c5-838f-5a88921ae9d2/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_041.jpg`
  - 043 `https://cdn.assets.prezly.com/853b6b2d-0bbc-4437-97e8-d6cbcf7ce451/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_043.jpg`
  - 046 `https://cdn.assets.prezly.com/916df04a-43d4-4cae-a792-9d6372a6068f/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_046.jpg`
  - 047 `https://cdn.assets.prezly.com/24872abf-aa3d-4f29-aecf-42b1569d067c/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_047.jpg`
  - 048 `https://cdn.assets.prezly.com/02bb53ce-c5aa-4d04-9821-14e70f64104e/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_048.jpg`
  - 051 `https://cdn.assets.prezly.com/ab909891-be51-4c50-bdc9-ddd4343fcdae/-/preview/-/format/auto/DENZA_Z9GT_02STATIC_051.jpg`
  - All assets as ZIP: `https://cdn.uc.assets.prezly.com/6c49fc21-ffff-425d-bce9-aa98e238a5fd~73/archive/zip/denza-goes-global-with-technology-drives-elegance.zip`
  - The rest of the kit is 01DYNAMIC_* (driving), 03DETAIL_* and 004INTERIOR_*, so skip those.
- verification: none (not viewable). This is a 2025 kit from the Milan/Paris European launch of the Z9GT. The European car is the same body, but check it.
- checked / rejected: denza.com/de (client-rendered, no images); zigwheels.my Z9 GT gallery (only front-angle, front-cross-side 3/4, headlight, tail light).

## denza-d9
- status: **CANDIDATE (weak)**
- **body warning**: zigwheels.my calls its gallery "D9 2021 exterior images" (Malaysian D9 EV) and also runs "New Denza D9 facelift leaked in China ahead of debut". motor1.de captions the European photos "Denza D9 DM-i (2026)" and one older photo "Denza D9 (2024)". Confirm which nose the European D9 DM-i has before using any Asian picture.
- candidates:
  1. zigwheels.my FAQ (https://www.zigwheels.my/new-cars/denza/d9/faq/what-are-the-colors-options-available-in-denza-d9) says the 13 exterior images include a "Side View". Gallery https://www.zigwheels.my/new-cars/denza/d9/images, but its HTML exposes no image URLs. Files sit under `https://imgcdn.zigwheels.my/large/gallery/exterior/181/2540/` (hero: `.../medium/gallery/exterior/181/2540/denza-d9-53072.jpg`). Third-party, and geo-blocked for the main browser per the brief.
  2. km77.com "DENZA D9 (2025) - Fotos Exteriores" (19 images, caption only "DENZA"): https://www.km77.com/coches/denza/d9/2025/imagenes. The 2026-06-29 set `https://imagenes.km77.com/fotos/bbtcontent/clippingnew/KM7KPH20260629_0038/full.jpg` … `_0047/full.jpg` is probably the European DM-i launch material. There are also `KM7KPH20260408_0009…0012` and `KM7KPH20240226_0183…0187` (older). Angles unknown; third-party.
  3. de.motor1.com (credit "Bild von: Denza", "Denza D9 DM-i (2026)"): `https://cdn.motor1.com/images/mgl/1Zw2KL/s3/denza-d9-dm-i-2026.jpg`. Angle unknown; third-party.
- checked / rejected: denza.com/de/d9 (client-rendered; only the energy-label PDF `https://www.byd.com/material/__EU/byd-site/de/preview/DENZA_D9_DM_Energy-Label_0926.pdf`); BYD Belgium press (no D9 gallery; search "D9" finds nothing).

## xpeng-l03
- status: **CANDIDATE (good official source, angle unconfirmed)**
- twin confirmed: XPeng **MONA L03**, launched in China and Europe at the same time (cnevpost 2026-07-16; 4,650 x 1,920 x 1,600 mm, 2,850 mm wheelbase, matching the chart). Swiss name "XPENG L03", from CHF 35'600 (XPeng Switzerland release, 16 Jul 2026).
- source: **XPeng Switzerland newsroom (pr.co), CH market**. Media kit https://xpengswitzerland.pr.co/assets/240537/ has 93 originals. Official numbered shots are "XPENG L03_001" to "_040" (likely the studio/location set), e.g.:
  - _001 `https://d21buns5ku92am.cloudfront.net/70232/images/688176-XPENG%20L03_001-4743c5-original-1783951574.jpg`
  - _002 `https://d21buns5ku92am.cloudfront.net/70232/images/688175-XPENG%20L03_002-7bc435-original-1783951571.jpg`
  - _003 `https://d21buns5ku92am.cloudfront.net/70232/images/688183-XPENG%20L03_003-9bab03-original-1783951666.jpg`
  - _004 `https://d21buns5ku92am.cloudfront.net/70232/images/688177-XPENG%20L03_004-e01153-original-1783951611.jpg`
  - _005 `https://d21buns5ku92am.cloudfront.net/70232/images/688184-XPENG%20L03_005-5ccd3f-original-1783951716.jpg`
  - _006 `https://d21buns5ku92am.cloudfront.net/70232/images/688182-XPENG%20L03_006-60f1c3-original-1783951656.jpg`
  - (_007 to _040 are listed on the asset page. `_MOPxxxx` files are Munich launch-event photos, and named files such as Panoramadach and Mittelkonsole are details.)
  - The release images `XPENG L03_1`…`_3` (e.g. `https://d21buns5ku92am.cloudfront.net/70232/images/689077-XPENG%20L03_1-11aa56-original-1784207665.jpg`) are on https://xpengswitzerland.pr.co/268276-alternatives-einstiegsmodell-in-die-xpeng-produktfamilie-suv-coupe-xpeng-l03-startet-in-der-schweiz-ab-chf-35-600/
- also: the XPeng global pressroom album "L03" (https://www.xpeng.com/pressroom/image) has "L03 Shots: Rock Gray" `https://s-cdn.xpeng.com/xpwebsite/prod/2026-09-17/975c4e035c1045c29889db3a2115616d.jpg` and "Silver Frost" `.../23e0ba3d9e934394a1094ea5bed138e7.jpg`. Angles unknown.
- unchecked lead: the German spec sheet PDF `https://s-cdn.xpeng.com/commoncms/prod/2026-10-08/065b977dab264145b5a928143fae2f97.pdf?name=Germany_L03_SpecsSheet_092026` may have a side render (note the page number if so).
- checked / rejected: xpeng.com/de/model/L03 (colour section = icon swatches "L03icon"; car images are JS-loaded labels PC-P2…P11); xiaopeng.com/l03.html (colour images are 84x84 swatches, checked via OSS image/info); cnevpost MIIT filing article 2026-04-09 (5 images, angles unknown, third-party).

## xpeng-g9l
- status: **CANDIDATE (good official source, angle unconfirmed)**
- twin: the G9L is sold in China under the same name (5-seat; launched 17 Sep 2026, BEV and EREV). Same 5,120 mm length and 3,100 mm wheelbase (cnevpost 2026-10-12). Caution: the EU G9L page's image labels include "GX PC …" and "G02 PC …" entries, so some page pictures may be reused from the XPeng **GX**, a different car. Do not take a picture from that page without checking.
- source: **XPeng Switzerland newsroom (pr.co), CH market**, release 12 Oct 2026 https://xpengswitzerland.pr.co/273192-neuer-xpeng-g9l-feiert-europapremiere-auf-dem-pariser-automobilsalon/ with 14 official images (alt "XPENG G9L"):
  - _001 `https://d21buns5ku92am.cloudfront.net/70232/images/710037-XPENG%20G9L_001-0647f2-original-1791808258.jpg`
  - _002 `https://d21buns5ku92am.cloudfront.net/70232/images/710030-XPENG%20G9L_002-f64e66-original-1791808253.jpg`
  - _003 `https://d21buns5ku92am.cloudfront.net/70232/images/710038-XPENG%20G9L_003-75bc09-original-1791808258.jpg`
  - _004 `https://d21buns5ku92am.cloudfront.net/70232/images/710031-XPENG%20G9L_004-109a27-original-1791808253.jpg`
  - _005 `https://d21buns5ku92am.cloudfront.net/70232/images/710033-XPENG%20G9L_005-738888-original-1791808255.jpg`
  - _006 `https://d21buns5ku92am.cloudfront.net/70232/images/710032-XPENG%20G9L_006-cd7460-original-1791808254.jpg`
  - _007 `https://d21buns5ku92am.cloudfront.net/70232/images/710034-XPENG%20G9L_007-50f426-original-1791808256.jpg`
  - _008 `https://d21buns5ku92am.cloudfront.net/70232/images/710036-XPENG%20G9L_008-c29391-original-1791808257.jpeg`
  - _009 `https://d21buns5ku92am.cloudfront.net/70232/images/710035-XPENG%20G9L_009-161b81-original-1791808256.jpeg`
  - earlier set: 703023 _007 `https://d21buns5ku92am.cloudfront.net/70232/images/703023-XPENG%20G9L_007-4548ae-original-1789719900.JPG`, 703024 _008 (…-823050-original-1789719911.JPG), 703025 _011 (…-7cde20-original-1789719912.jpg), 703026 _009 (…-3a560f-original-1789719912.jpg), 703027 _010 (…-2038ce-original-1789719912.JPG)
- third-party fallback: sina "小鹏G9L珠峰白/峡湾灰车身配色官图" (official colour pictures re-posted, 800 px wide). Image 9 sits right after the side-design paragraph: `https://k.sinaimg.cn/n/sinakd20260805s/534/w800h534/20260805/b9e2-3b9e94b6e8ebfe686cb4561ef28cf938.jpg/w700d1q75cms.jpg` (page https://cj.sina.com.cn/articles/view/1912222221/71fa320d02001mnb6). Angle inferred from placement only.
- checked / rejected: xpeng.com/de/model/G9L (swatches only; the "G9L PC 2-2" image is on `s-cdn.uat.xpeng.com`, robots-disallowed); xiaopeng.com/g9l.html (84x84 swatches; the "Logo" PNG is 860x560 and 11 KB, so a graphic, not a car); cnevpost Paris image 6 (side view, but on a show stand with visitors, so rejected as a scene); XPeng global pressroom (no G9L album).

---

## Summary
| model | status | best URL |
|---|---|---|
| byd-ti-7 | NONE | (check https://www.byd.com/uk/hybrid-cars/ti-7 in the browser; no side found elsewhere) |
| byd-shark | NONE | (maybe https://mms.businesswire.com/media/20240515408443/ja/2132851/5/BYD_SHARK.jpg?download=1, angle unknown) |
| byd-sealion-5 | CANDIDATE (weak, third-party) | https://www.zigwheels.ph/new-cars/byd/sealion-5-dm-i/images (#4 "Side View (Left)", file URL not exposed); keep the byd.ch drawing otherwise |
| denza-z9-gt | CANDIDATE (official press, angle unconfirmed) | https://press.bydauto.be/denza-goes-global-with-technology-drives-elegance (check DENZA_Z9GT_02STATIC_035…051) |
| denza-d9 | CANDIDATE (weak, third-party; body to check) | https://www.zigwheels.my/new-cars/denza/d9/images ("Side View" listed) / km77 KM7KPH20260629_0038…0047 |
| xpeng-l03 | CANDIDATE (official CH press, angle unconfirmed) | https://xpengswitzerland.pr.co/assets/240537/ (XPENG L03_001…_040) |
| xpeng-g9l | CANDIDATE (official CH press, angle unconfirmed) | https://xpengswitzerland.pr.co/273192-neuer-xpeng-g9l-feiert-europapremiere-auf-dem-pariser-automobilsalon/ (XPENG G9L_001…_011) |
