# v1.15 picture search: Group I report (second pass, real browser)

Session: 2026-11-01, about 22:12-22:33 UTC, through Raven's Chrome (own tabs only; all closed at the end). Downloads in `ext/unpacked/v115/I/`. All files arrived through the hx worker as WebP q=0.92, scale 1, **with the alpha channel kept** (the corner pixel is fully transparent in all three source PNGs).

---

## dr-dr-1-0-ev: FOUND (true side, brand cut-out)
- **File:** `ext/unpacked/v115/I/dr-dr-1-0-ev-side.webp`, 975x500, transparent background, white car with black roof, **faces left**. Both wheels are full circles, with no front or rear face. It is the current DR 1.0 EV body (Chery eQ1 "Little Ant" based; the same nose and lights as the 2026 campaign image `2026/01/DR1-CORRETTO-copy-scaled.webp`). I viewed the file.
- Source URL (brand-own, IT): https://drautomobiles.com/wp-content/uploads/2023/09/DR_ModelloCut_DR1.png (the "modellino" cut-out, uploaded 2023-09-17).
- Alternate: `dr-dr-1-0-ev-side-mint.webp` (975x500, the same render in mint green, from https://drautomobiles.com/wp-content/uploads/2023/12/DR_ModelloCut_DR1c.png). `2025/04/0007_DR_ModelloCut_DR1c.png` is the same render downscaled (500x500 canvas), and `0007_DR_ModelloCut_DR1c-1.png` is 311x160.
- Found through the WordPress media API on drautomobiles.com (`/wp-json/wp/v2/media?search=modellocut`). The resolution is moderate (car about 960 px wide) but above the 600 px minimum.
- Rejected: `DRAutomobiles_Models_DR_1.0_EV.webp` (2025-12, scene with a person), `DRAutomobiles_Models_DR1.0-Slider-1.webp` (scene), `DR1-CORRETTO` (front 3/4 cut-out with racing livery), `DR1.0EV_PhotoZERODays01.jpg` (scene with a person), and `mod_laterale-1/-2.png` (despite the name, these show a blue SUV, not the DR 1.0).
- **Sales status (evidence):**
  - drautomobiles.com (2026-11-01) **no longer has a DR 1.0 page**. The home menu links only DR 3, DR 5 (Collection / Full Hybrid / Stilnovo), DR 6 (Collection / Stilnovo / Super Hybrid / Full Hybrid / AWD) and DR 8 Collection. The WP pages API (100 most recent pages) and `page-sitemap.xml` contain no slug with dr-1 or dr1.
  - The latest DR 1.0 uploads in the media library are: `DRAutomobiles_Models_DR_1.0_EV.webp` (2025-12-29), `DRAutomobiles_Models_DR1.0-Slider-1.webp` (2026-03-30), `DR1-CORRETTO-copy-scaled.webp` (2026-04-27), and dealer-area tiles `dr1-listini/-schede-tecniche/-fotografie...` (2026-02-20). So the model was on the site at least until spring 2026 and has since been removed from the model menu.
  - **Conclusion:** probably runout (removed from the brand site; dealer stock or price lists may continue; the brief's source is the Sep 2026 il Giornale Digitale price list). I did not check Italian dealers (time).

## mitsubishi-l200: FOUND (true side; caveat: Club Cab body, AU Triton)
- **File:** `ext/unpacked/v115/I/mitsubishi-l200-side-clubcab.webp`, 1920x1080, transparent background, blue (Impulse Blue D23) **Club Cab pick-up** GLX+, **faces right**. Both wheels are full circles, with no front or rear face. It is the 6th-generation (2024+) Triton = EU L200 body. I viewed the file.
- Source URL (brand-own, AU): https://www.mitsubishi-motors.com.au/content/dam/mmal/vehicles/triton/25my/club-cab-pick-up/glx-plus/4wd/diesel/automatic/impulse-blue/25MY_TR_AUS_CCAB_GLX+_side_D23.png (referenced from https://www.mitsubishi-motors.com.au/vehicles/triton.html and /vehicles/triton/range.html).
- **Caveat:** the chart row is the double-cab pickup (5360 mm). The Club Cab has the same wheelbase, overall length class, nose and front doors, but a shorter cab with small rear-hinged doors and a longer tub. The AU pages I read contain **no Double Cab pick-up side render**: the only 26MY double-cab pick-up asset is a GSR 3/4 front (`26my/double-cab-pick-up/gsr/.../dnd-triton-26my-double-cab-pick-up-gsr-4wd-diesel-automatic-yamabuki-orange-3-4-front.png`).
- Alternate (for the double-cab silhouette): `mitsubishi-l200-side-dcab-cc.webp`, 1920x1080, transparent, white **Double Cab cab-chassis** (alloy tray instead of a tub), faces right, true side. Source: https://www.mitsubishi-motors.com.au/content/dam/mmal/vehicles/triton/25my/double-cab-cab-chassis/glx/4wd/diesel/automatic/white/cab-chassis-dcab-triton-25my-glx-white-side.png. The cab and nose are correct for a double cab, but the rear body is wrong.
- Also on the AU DAM: single-cab cab-chassis side renders (`26my/single-cab-cab-chassis/.../26MY_TR_AUS_SCAB_GLX_2WD_CC_side-right_W19_Alloy.png`, 1920x1080, 1.1 MB PNG; `25my/.../cab-chassis-scab-triton-25my-glx-4wd-white-side.png`).
- **Next step if a double-cab pick-up side is needed:** the AU build-and-price/configurator (not opened) probably uses the same DAM tree with `double-cab-pick-up/{glx-plus|gls|gsr}/4wd/diesel/automatic/{colour}/..._side_...png`. I did not guess the file names.
- Rejected: the JP Triton design page (https://www.mitsubishi-motors.co.jp/lineup/triton/design/index.html). All colour-picker images `img_bodycolor_0X_0Y.jpg` (996x560) are **front 3/4** on white, and img_01 ... img_03_06 are scene photos. Not opened (time): the JP accessory 360 viewer, the Thai site and the UK/CH pages.

## morgan-plus-four: CANDIDATE (configurator side view reachable; capture not finished)
- https://configure.morgan-motor.com/plusfour/ (CH region auto-selected; New configuration, then Manual) is a **Wonderland Engine real-time WebGL viewer** (`WonderlandRuntime.wasm`, `Morgan Plus Four.bin`; the `NNNN.webp` files are textures). There are **no pre-rendered frames and no URL pattern.** The engine object is not global (`window._WL` holds only `runtimes`).
- I saw a clean **true side view (car facing right, studio-grey floor, slight top-down camera)** on screen after a horizontal drag. The viewer has strong orbit inertia. Scripted pointer and mouse events are ignored; only real drags work. The Summary page shows only a front-3/4 snapshot.
- **Why the capture failed:** in the shared browser my tab was a background tab, so `requestAnimationFrame` and the engine render ran only while a screenshot was being taken (a 9 s recorder got 2 frames), and the inertia made the stopping angle unpredictable.
- **Capture recipe that works (tested):** the canvas (2380x911 device px, `preserveDrawingBuffer:false`) can be read inside a rAF callback: `requestAnimationFrame(()=>{ctx2d.drawImage(canvas,0,0)})` gives real pixels. In a **foreground** tab: drag (left drag of a few hundred px from the default 3/4 front reaches the near side; small drags keep rotating with inertia), wait until the car settles side-on, then grab the canvas in rAF and `toBlob('image/webp')`. Expect about 1700-1900 px of car length, a grey studio background (needs rembg) and a slight elevated perspective (you see the seat tops).
- Not checked (time): media.morgan-motor.com albums beyond those already rejected, and dealer studio shots.

## smart-2: NONE
- Checked in this pass (viewed in a contact sheet): the remaining production-car items of media kit https://media.smart.com/en-INT/assets/242460/:
  - "picture 3/4/5" and "20260928-113036": Paris show stand, body-in-white on stage, red car 3/4 on the stand.
  - WeChat image 20261012163244 (712852): white car, **front 3/4** on a grey studio set.
  - World Premiere 712853: stage, front views.
  - "Spilt Tailgate" 709556: detail with a person.
- ch.smart.com/de/models/hashtag-two/: images are only `hashtag-two-wp-fallback-hero-stage-desk.jpg` (street scene, red car front 3/4, far away) and four teaser banners (brabus/specs/early-order/stories). There is no configurator, no 360 and no visualizer frames for the #2 (`visualizer-extended-thumbnail-ext.png` is generic).
- Together with the Rgb 13-27 series checked earlier (rear, rear 3/4, interiors), **no smart #2 side view exists on smart's own channels yet** (2026-11-01). The production renders Rgb 01-12 and 20 are not published in the kit.
- Not checked (time): smart.cn #2 pages and other media.smart.com kits or releases (category 5737 had only 2 kits per pass 1).

---

## Summary

| model | status | best URL |
|---|---|---|
| dr-dr-1-0-ev | FOUND (true side, transparent, 975x500, faces left; model no longer on drautomobiles.com, probably runout) | https://drautomobiles.com/wp-content/uploads/2023/09/DR_ModelloCut_DR1.png -> `I/dr-dr-1-0-ev-side.webp` |
| mitsubishi-l200 | FOUND, caveat: Club Cab pick-up (true side, transparent, 1920x1080, faces right); alt Double Cab cab-chassis | https://www.mitsubishi-motors.com.au/content/dam/mmal/vehicles/triton/25my/club-cab-pick-up/glx-plus/4wd/diesel/automatic/impulse-blue/25MY_TR_AUS_CCAB_GLX+_side_D23.png -> `I/mitsubishi-l200-side-clubcab.webp` |
| morgan-plus-four | CANDIDATE (3D configurator reaches a true side; needs a foreground-tab canvas grab, recipe above) | https://configure.morgan-motor.com/plusfour/ |
| smart-2 | NONE (no side view on smart's own channels yet) | - |
