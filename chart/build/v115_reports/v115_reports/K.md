# v1.15 picture search (second pass, real browser): Group K report

Session: 2026-11-01, 22:12-22:38 UTC. Route: Raven's Chrome in my own tabs (all closed at the end). I listed image URLs, drew contact sheets in the page, took screenshots, and fetched the chosen originals with the hx worker, then unpack2.py. No download buttons or ?download=1 links were used.
All files are in `ext/unpacked/v115/K/` (WebP q0.92 re-encodes of the originals; scale 1 unless noted). I viewed every saved file with Read.

---

## nissan-townstar-van-small: FOUND (press photo, scene, needs rembg)
- **File:** `K/nissan-townstar-van-small-side-37afe1.webp` (928x619).
- **Image URL:** https://wieck-nissanao-production.s3.amazonaws.com/photos/37afe174c791b552d5a66314b087afc4b8b6114d/preview-928x522.jpg
  - The file is really 928x619, despite the name.
- **Page:** https://europe.nissannews.com/en-GB/releases/nissan-reveals-the-all-new-townstar-van-a-game-changer-within-the-lcv-market, gallery "Photos (50)".
  - Source: Nissan Europe newsroom (brand press), EU market, Sept 2021 reveal of the current (only) generation.
- **Viewed:** true side, **faces RIGHT**.
  - Car: white L1 panel van with sliding side door, blind rear quarter and two-tone alloys.
  - Both wheels are full circles; no front or rear face is visible.
  - Background: outdoor scene (grey asphalt, city skyline), so it needs rembg.
  - The van is about 580 px long (x about 175-757), which is below the 800 px ideal but usable. It replaces the current outline drawing.
- **Resolution limit:**
  - S3 only serves `thumbnail-720x404.jpg` and `preview-928x522.jpg`.
  - I tested `original.jpg/.jpeg/.png`, `full.jpg`, `large.jpg`, `hires.jpg`, `medium.jpg`, `download.jpg`, `preview-1920x1080.jpg`, `preview-1280x720.jpg` and `thumbnail-1440x808.jpg`; none exist.
  - The full-size file is only behind the newsroom's per-photo download button, which I did not use. If a larger copy is wanted, the person could download that photo themselves from the gallery (photo 6 of 50, hash 37afe1...).
- **Rejected from the same gallery (50 photos):**
  - 4ed4a4 (grey van, 3/4 front)
  - f84de2 (white van, rear 3/4)
  - the rest: driving shots, front/rear views and interiors
- **Also checked:** release "nissan-starts-european-production-of-all-new-fully-electric-townstar" (one photo, 3/4 at a charger).
- **Bonus lead, not my group (nissan-townstar-kombi):** https://wieck-nissanao-production.s3.amazonaws.com/photos/f5d1a5b7b9bab78b79f258775b948597a5e0f686/preview-928x522.jpg
  - Red Townstar passenger version in front of a glass building, near side, facing left. Seen only as a thumbnail; my fetch of it hung, so it is unverified (may be slight 3/4).

## nissan-primastar-van-mid: FOUND (press photo, scene, needs rembg)
- **File:** `K/nissan-primastar-van-mid-side-107793.webp` (928x619).
- **Image URL:** https://wieck-nissanao-production.s3.amazonaws.com/photos/10779305ba431013bfe0231985fd10a5981ec6a3/preview-928x522.jpg
- **Page:** https://europe.nissannews.com/en-GB/releases/interstar-primastar-and-all-new-townstar-nissans-van-range-renewed-to-future-proof-businesses, gallery "Photos (52)", photo 14.
  - Source: Nissan Europe newsroom (brand press), 2021 range launch.
- **Viewed:** true side, **faces RIGHT**.
  - Car: grey L1H1 panel van (short body, which matches the chart's 5080 mm) with steel wheels.
  - Body: the current 2021-facelift nose with C-shaped LED lights (same as the current tiles).
  - Both wheels are full circles; no front or rear face is visible.
  - Background: outdoor scene (glass and steel building, paved plaza), so it needs rembg.
  - The van is about 540 px long (x about 210-750). Same 928 px limit as the Townstar (no larger public variant).
  - It replaces the dimension drawing.
- **Rejected:**
  - the other 51 photos of that gallery: group shots of Interstar/Primastar/Townstar, driving 3/4, rear, interiors; 70ef85 is a white Primastar Combi in a landscape, but 3/4 front
  - release "nissan-launches-updated-primastar" (2010, old body, empty gallery)
  - release "new-primastar-and-interstar-vans-from-nissan" (old NV200-era gallery of 165 photos, previous bodies)

## nissan-primastar-kombi: NONE (keep the v113 nissan.de dimension drawing)
- The only Combi photo in the 2021 range gallery (70ef85, white, in a landscape) is 3/4 front.
- I found no other Kombi/Combi release on the Primastar channel of the Europe newsroom.
- The new van photo above is not a substitute, because the side glazing differs.
- Not tried (time): uk.nissannews.com Primastar Combi releases; nissan.co.uk / nissan.de Combi pages in the browser.

## wey-wey-03: FOUND (brand press photo, scene, needs rembg)
- **File:** `K/wey-wey-03-side-press66.webp` (1536x1010, a **0.6-scale** re-encode of the 2560x1683 original to keep the transfer small).
  - Re-fetch at scale 1 if more pixels are wanted. Same-origin fetch works from any presse.gwm-motor.de page.
- **Image URL:** https://presse.gwm-motor.de/wp-content/uploads/2024/06/GWM-WEY-03_-66-scaled.jpg (2560x1683).
  - WordPress "-scaled" means a larger original `GWM-WEY-03_-66.jpg` probably exists.
- **Page:** GWM Deutschland press site https://presse.gwm-motor.de/start/gwm-wey-2/ (WP media library, uploaded 2024-06-10). Brand press, DE market.
- **Viewed:** true side, **faces LEFT**.
  - Car: white Wey 03 (= Coffee 02 / China Wey Latte) with two-tone twin-spoke alloys.
  - Both wheels are full circles; only the wrap-around headlight edge shows at the nose, with no front face.
  - Background: outdoor scene (lake, dark sand ground, cloudy sky), so it needs rembg.
  - The car is about 1180 px long in the saved file (about 1970 px in the original).
- **Rejected:**
  - gwm-motor.de/wey-03 colour-picker PNGs (950x418: "GWM WEY 03 Deep Sea Blue Metallic", "06_Bild-1_Snow-White-1", "GWM_WEY_03_2024_Lava_Black") and `hubfs/Testing/WEY-03_Luxury Kopie 1.png` (only 280x135, alt "WEY 03 Seitenansicht"). All are slight 3/4 front, with inner wheels visible.
  - All other press-library images (about 100 checked on 6 contact sheets): driving 3/4, front, rear, group shots, details, interiors. `WEY_03_Dynamic_030` is near-side but a driving shot with the nose visible.
- **Data note:** gwm-motor.de technical data gives **4668 mm** for the Wey 03; the chart has 4520 mm, as B.md already flagged.

## wey-wey-05: NONE
- **Checked and rejected:**
  - gwm-motor.de colour PNGs "WEY 05 in Snow White / Deep Sea Blue / Lava Black" (950x418) are 3/4 front, as judged before.
  - gwm-motor.de/technische-daten-wey-05 has no car images.
  - Every WEY 05 image in the press library is 3/4, driving, front, rear or interior. That covers WEY05_3275/3295/3604/3643/3672/3683/4216/4286 (2026-01), GWM-WEY-05_Exterior-5/9/10/14/18/31/38/44/46 (2025-07), GWM-WEY-05-1..8 (2024-02), GWM-WEY-05_-1/-5/-7/-8 (2023-11) and the Aktionsrabatt image. WEY05_3604 comes closest, but it is a rear 3/4 with the tail visible.
- **Last resort only (line art, below the brief's bar):**
  - Source: https://presse.gwm-motor.de/wp-content/uploads/2025/12/Technische-Daten_GWM-WEY-05.pdf (6 pages, saved as `K/wey05-techdata-pdf.pdf`).
  - Page 2 has a dimension **line drawing** with a side elevation (upper left of the drawing block). It is not photo-realistic. Page 6 has 3/4 colour renders.
- **Not tried (time):** Euro NCAP "WEY Coffee 01" (third party); Chinese Mocha 360 viewers. wey.com no longer lists the Mocha (B.md).

## mhero-mhero-i: FOUND (third-party catalogue copy, flagged; scene, needs rembg)
- **File:** `K/mhero-mhero-i-side-zigwheels.webp` (930x620).
- **Image URL:** https://imagecdn.zigwheels.ae/large/gallery/exterior/127/2112/mhero-1-side-view-301210.jpg
- **Page:** https://zigwheels.ae/new-cars/mhero/1/colors?amp=1 ("Side View (Left)"). Third-party catalogue, UAE; it looks like a manufacturer press photo.
- **Viewed:** true side, **faces LEFT**.
  - Car: black Mhero I with black off-road wheels. Both wheels are full circles, and there is no front or rear face.
  - Background: dark scene (faceted building, wet asphalt), so it needs rembg. A black car on a dark background makes the cut-out harder.
  - The car is about 590 px long (x about 170-760).
  - Caveat: the UAE listing is tagged "hev" (range extender?). The body looks identical to the NL BEV. A small flap on the rear quarter may be a fuel or charge door; I cannot tell which.
- **Rejected:**
  - dongfeng-global.com/business/mhero: `MHEROI@2x_1781430302507.png` (3440x1720) is a 3/4 snow driving scene. The other images are group, landscape or Mhero II scenes.
  - voyah.nl/mhero (www.mhero.nl redirects there): `MHERO I 2.webp` (3/4 snow), `MHERO I 3.jpg` (straight front, studio-like dark set; a possible FRONT view, not fetched), `MHERO I _ 5.webp` (3/4 off-road), `MHERO I _ 4.jpg` (3/4, as rejected before).
- **Not tried (time):** a Chinese M-Hero 917 brand site under another domain, and Chinese 360 viewers.

---

## Summary
| model | status | best URL |
|---|---|---|
| nissan-townstar-van-small | FOUND (press, 928x619, white L1 van, scene, faces right, rembg) | https://wieck-nissanao-production.s3.amazonaws.com/photos/37afe174c791b552d5a66314b087afc4b8b6114d/preview-928x522.jpg |
| nissan-primastar-van-mid | FOUND (press, 928x619, grey L1H1 van, current nose, scene, faces right, rembg) | https://wieck-nissanao-production.s3.amazonaws.com/photos/10779305ba431013bfe0231985fd10a5981ec6a3/preview-928x522.jpg |
| nissan-primastar-kombi | NONE (keep v113 dimension drawing) | - |
| wey-wey-03 | FOUND (GWM DE press, 2560x1683, white, lake scene, faces left, rembg) | https://presse.gwm-motor.de/wp-content/uploads/2024/06/GWM-WEY-03_-66-scaled.jpg |
| wey-wey-05 | NONE (only a line drawing in the tech-data PDF, p. 2) | (last resort: https://presse.gwm-motor.de/wp-content/uploads/2025/12/Technische-Daten_GWM-WEY-05.pdf) |
| mhero-mhero-i | FOUND, third-party (zigwheels.ae, 930x620, black, dark scene, faces left, rembg) | https://imagecdn.zigwheels.ae/large/gallery/exterior/127/2112/mhero-1-side-view-301210.jpg |
