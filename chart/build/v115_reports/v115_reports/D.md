# v1.15 picture search - Group D (vans) report

Run: 2026-11-01, 21:46-22:35 UTC (about 50 min; went over the 25 min budget because of the download problem below).

## How the files were obtained (important for the main thread)
- In this session `curl` cannot reach any web host: the egress proxy answers 403 to CONNECT for every host (also google.com and wikipedia.org; see `recentRelayFailures` in the proxy status). WebFetch works for HTML but not for image files.
- So the pictures were fetched in Claude in Chrome (my own tab, closed at the end) with the existing `ext/hx_worker.js` method: fetch the image in the page, convert it to WebP (q 0.9, alpha kept) in a canvas, store it in sessionStorage, render chunked `data:` link nodes, `read_page`, then `python3 -I unpack2.py`.
- The Sanity CDN (`cdn.sanity.io`) and `www.saicmaxus.co.uk` allow this (CORS / same origin). `images.piaggio.com` blocks cross-origin fetch, so I opened those images as top-level pages.
- Every file named `*-side.webp` was viewed (Read tool) after unpacking: I checked the whole picture and a crop of the front end, and the wheels are full circles.
- Files in `ext/unpacked/v115/D/`:
  - `<id>-side.webp`: the chosen picture.
  - `*-alt.webp`: alternates.
  - `_rejected/`: contact sheets of what I looked at and rejected.

---

## maxus-mifa-7
- **status: NONE**
- Checked www.saicmaxus.co.uk/our-range/new-vans/mifa-7/ in Chrome. It loads in a real browser; WebFetch only gets the bot page. All images are Umbraco `/media/...`. Contact sheet: `_rejected/sheet-mifa7-uk.webp`. Rejected:
  - `/media/aonhjhkt/mifa-7-exterior-side-view.jpg` (1200x800): 3/4 front, dark studio, despite the file name.
  - `/media/wkxdltw3/mifa-7-exterior-rear-side-view.jpg`: 3/4 rear.
  - `/media/pdqhbxn5/mifa-7-exterior-side-view-door-open.jpg` (1200x800): a true side view, faces left, dark studio, but the front and sliding doors are open. Rejected (silhouette broken). This is the only true-side official image found; it is a last resort only if the main thread accepts open doors.
  - `/media/4hwlz5xo/mifa-7-exterior-side-view-boot-open.jpg`: 3/4 rear with the tailgate open.
  - `/media/1cpjexqh/mifa-7-thumbnail.png` (720x640): cut-out true side, but cropped to the front half only.
  - `/media/5vjo3leh/mifa-7-lg.png`, `mifa-7-md.png`, `xbulgxiv/mifa-7-large-banner.jpg`, `yiugzdje/mifa-7-medium-main-image.jpg`: forest-road scene photos, near-front.
- maxus.no lists only the MIFA 9, not the Mifa 7. ldvautomotive.com.au does not list the Mifa 7.
- Not reached in time: the SAIC Maxus China site (大家7 / MIFA 7 colour picker), maxus.ie, and Maxus NL/BE.

## maxus-edeliver-3
- **status: FOUND**
- Image (SWB, 4.8 m3, 4.56 m, which matches the chart length of 4555 mm): `https://cdn.sanity.io/images/mcx434c9/production/561b88ad2ff575f8a361b48b7ace754c48638fe0-1920x1200.png`
- Page: https://maxus.no/modeller/e-deliver-3-el-varebil. It is in the model spec block "e-Deliver3 4,8m3 SWB 50,2 kWh".
- Source type: brand-own national site (Maxus Norway, run by the importer RSA). Market: NO.
- Verified by viewing `maxus-edeliver-3-side.webp`:
  - 1920x1200, transparent background with a soft ground shadow (crop the shadow).
  - True side, faces left, white van.
  - Solid-body aspect 2.37, which matches the SWB (4555 x ~1900 mm).
- Alternate: LWB 6.3 m3 (5.15 m), `.../5730b343707f88927165ffcb9a9afbaf518a63e4-1920x1200.png`. Also true side, faces left. Saved at half size as `maxus-edeliver-3-lwb-alt.webp`.
- Rejected on the same page: the colour images `01d76443...png` and `c5d3326d...png` (3/4 front cut-outs), the chassis-flatbed `c19c2588...png` (3/4), and all JPG gallery images (scenes, details, interior).

## maxus-edeliver-7
- **status: FOUND**
- Image: `https://cdn.sanity.io/images/mcx434c9/production/dc314999820ac5e6c83244e0dcd192d8096a05e3-1920x1200.png`
- Page: https://maxus.no/modeller/e-deliver-7. The page is titled "e-Deliver 7 4x4", the version sold in Norway; the body is the same as the eDeliver 7.
- Source type: brand-own national site (Maxus Norway / RSA). Market: NO.
- Verified by viewing `maxus-edeliver-7-side.webp`:
  - 1920x1200, transparent background with a soft shadow.
  - True side, faces left, white van, standard roof.
  - Only the wrap-around headlamp and the dotted bumper corner show at the nose; no front face.
  - Aspect 2.45, so most likely L1 (chart length 4998 mm).
- Alternate: `.../d326dca5294a7fd0ade37a8a76f30e851c212dcc-1920x1200.png`. Longer body (aspect 2.62, probably L2), true side, faces left. Saved as `maxus-edeliver-7-l2-alt.webp`.
- Rejected:
  - `35fd806f...png`: eDeliver 5, 3/4 front.
  - `1dba6693...png`: MIFA 9, 3/4.
  - The 3000x2001 gallery JPGs: scenes, interior, details.
  - `eab0b939...png`: 3/4.

## maxus-edeliver-9
- **status: FOUND**
- Image: `https://cdn.sanity.io/images/mcx434c9/production/d2b85cb73b93cb3aab0672d2241535117fdea290-1920x1200.png`
- Page: https://maxus.no/modeller/e-deliver-9-elektrisk-varebil
- Source type: brand-own national site (Maxus Norway / RSA). Market: NO.
- Verified by viewing `maxus-edeliver-9-side.webp`:
  - 1920x1200, transparent background with a soft shadow.
  - True side, faces left, silver/white panel van, medium roof.
  - Aspect 2.35, which matches L2H2 (5940 x ~2530 mm).
- Unsure: the side profile does not show whether the render is the 2024 facelift front or the earlier front; the body is unchanged.
- Rejected (`_rejected/sheet-edeliver9-png.webp`):
  - `5a00be42...png`: high-roof 3/4 front.
  - `0c054dac...png`: eTerron 9 3/4.
  - `1dba6693...png`: MIFA 9 3/4.
  - `65ceba13...png`: warehouse scene.

## maxus-t90-ev
- **status: NONE**
- Checked: no T90 EV model page on maxus.no (current model list), saicmaxus.co.uk (current range) or ldvautomotive.com.au (no eT60 in the model list).
- Web searches (T90 EV side view / official / maxus.no) returned only press and dealer articles.
- Not reached in time: archived T90EV pages, maxusmotors.ch, and dealer stock photos.

## piaggio-porter-np6
- **status: NONE**
- commercial.piaggio.com/en_EN/ links only the Porter NPE. The Italian site has the NP6 model pages: /it_IT/modelli/fisso/, /ribaltabile/, /ribaltabile-con-sovrasponde/, /chassis/.
- Their version images are `https://images.piaggio.com/np6/vehicles/<code>/<code>/<code>-01-s.png` for the codes ecs90000 (chassis, yellow), eps80000 (`eps8000-01-s.png`, fixed deck, white), etsp0000 (tipper, blue) and eos20000 (`eos2000-01-s.png`, tipper with over-sides, orange).
- The files come in three sizes: `-01-s.png` (750x500), `-01-l.png` (3000x2000) and `-01.png` (3000x2254).
- All of them are **3/4 front on white**. Only view `01` exists (`-02-s` and `-03-s` give 404). Sheet: `_rejected/sheet-piaggio-np6.webp`.
- Not reached in time: the NP6 brochure/spec PDF and press.piaggiogroup.com.

## iveco-daily
- **status: NONE** (brochure leads below)
- www.iveco.com/switzerland/ now redirects to /corporate/404, so the CH source in the chart notes is dead; the UK site works.
- https://www.iveco.com/uk/Daily: the images `Daily-furgone.jpg`, `Daily-autocarro.jpg`, `Daily-4x4.jpg` and `daily-cng.jpg` (750x500) are 3/4 front on white (sage-green MY24); the rest are scenes. Sheet: `_rejected/sheet-iveco-daily.webp`.
- https://www.iveco.com/uk/Configurator/Daily (a quote form with reCAPTCHA) shows `DAILY VAN MY24.png`, `DAILY CAB MY24.png`, `DAILY VAN 4X4 MY24.png`, `eDaily VAN.png` and others (1000x750). These were already judged 3/4 in the earlier run (my24-config).
- UK promotions mention a "MY26 Daily" (connectivity update), not a new body.
- **Leads not opened (time):** the MY24 brochures, both HTTP 200 on a HEAD request:
  - `https://www.iveco.com/uk/-/media/IVECOdotcom/docs/brochure/my2024/IVECO-Daily-MY24.pdf` (9.18 MB)
  - `https://www.iveco.com/uk/-/media/IVECOdotcom/docs/brochure/my2024/daily2.pdf` (8.27 MB)
  
  Van brochures usually have a versions / dimensions page with side renders. Check whether they are photo-realistic or line drawings.

## levc-tx
- **status: NONE**
- https://www.levc.com/new-models/tx-taxi-overview/: all 19 large images are scenes, interiors or 3/4 views. Examples: `1_levc_tx_.png` (1920x640, night street scene), `angle_north_5_vertical.jpg`, `image_1/3/4.png`, `large_door.png`, `dsc_1474.jpg`, and a 3/4 front on white. No side view. Sheet: `_rejected/sheet-levc-tx.webp`.
- The page links /new-models/tx-access/, /tx-shuttle/, /vn5/ and /download-a-brochure/enquiry/. The brochure is behind an enquiry form, so I did not use it.
- A web search for TX side / profile images found only press articles and stock photos (rejected by the rules).

## levc-vn5
- **status: NONE**
- Not re-checked: the earlier run already rejected levc.com/new-models/vn5/ (levc2/*: 3/4, scenes, cutaway banner).
- A web search for VN5 side / profile press images found only trade-press articles (taxi-point, fleetnews, chargedevs), no official side view.

---

## Summary

| model | status | best URL |
|---|---|---|
| maxus-mifa-7 | NONE | (last resort: true side with doors open: https://www.saicmaxus.co.uk/media/pdqhbxn5/mifa-7-exterior-side-view-door-open.jpg) |
| maxus-edeliver-3 | FOUND | https://cdn.sanity.io/images/mcx434c9/production/561b88ad2ff575f8a361b48b7ace754c48638fe0-1920x1200.png (maxus.no, SWB, faces left, transparent) |
| maxus-edeliver-7 | FOUND | https://cdn.sanity.io/images/mcx434c9/production/dc314999820ac5e6c83244e0dcd192d8096a05e3-1920x1200.png (maxus.no, L1, faces left, transparent) |
| maxus-edeliver-9 | FOUND | https://cdn.sanity.io/images/mcx434c9/production/d2b85cb73b93cb3aab0672d2241535117fdea290-1920x1200.png (maxus.no, L2H2, faces left, transparent) |
| maxus-t90-ev | NONE | - |
| piaggio-porter-np6 | NONE | - (images.piaggio.com np6 renders are 3/4 only) |
| iveco-daily | NONE | leads: https://www.iveco.com/uk/-/media/IVECOdotcom/docs/brochure/my2024/IVECO-Daily-MY24.pdf , .../daily2.pdf |
| levc-tx | NONE | - |
| levc-vn5 | NONE | - |

Downloaded and viewed files (in `ext/unpacked/v115/D/`):
- `maxus-edeliver-3-side.webp`
- `maxus-edeliver-7-side.webp`
- `maxus-edeliver-9-side.webp`
- alternates `maxus-edeliver-3-lwb-alt.webp` and `maxus-edeliver-7-l2-alt.webp`
