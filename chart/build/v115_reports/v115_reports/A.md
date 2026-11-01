# v1.15 picture search - Group A (quadricycles)

## Blocker (applies to every model)
- curl: the egress gateway answers **403 to CONNECT** for every car host tried: www.ligier.fr, s3.ligier.fr, media.ligier.fr, www.ligier-professional.fr, www.casalini.eu, www.automobiles-chatenet.com (also upload.wikimedia.org). Each host was tried once and not retried (proxy README: policy denial, do not route around).
- WebFetch reads HTML/JSON but **cannot fetch image files** ("There was an error while fetching" on .jpg URLs from two hosts).
- So **nothing was downloaded or viewed**. The directory `.../ext/unpacked/v115/A/` is empty. No status is FOUND. Every angle below comes from file names, titles or page context and is **unverified**. The main thread must open the URLs in a real browser.
- Useful technique: media.ligier.fr, www.ligier.fr (files on s3.ligier.fr) and casalini.eu are WordPress sites, and their **REST media endpoint** lists every upload with title and size. Example: `https://media.ligier.fr/wp-json/wp/v2/media?search=profil&per_page=100&_fields=id,source_url,title,date,media_details`. WebFetch cut each answer off after about 6-17 records, so a browser will show more than I could list.
- The Ligier model galleries (`https://media.ligier.fr/mediatheque/<model>/`) show 12 items, then an "Afficher plus de médias" button. More files exist behind it.

---

## ligier-js50
- **status: NONE** (no file named or described as a side view; candidates below are worth viewing)
- Checked:
  - ligier.fr/vehicules/js50/: the colour images ("JS50 nacre grand format" etc.) are lazy-loaded with no URLs in the text and no angle given.
  - Equipment sheet PDF https://s3.ligier.fr/ligier-prod/uploads/2026/06/2026P1-002_-_FICHE_EQUIP._JS50_EL-TH_P1-2026_V7.pdf: not readable (blocked).
  - media.ligier.fr gallery https://media.ligier.fr/mediatheque/js50-2/: 12 items, all lifestyle or detail shots. Rejected `.../2024/11/202407_Ligier-Europe_JS50-Ultimate-Asphalt-Grey_3-4-Front.jpg` (3/4 by its name).
  - REST searches "JS50", "side", "profil" on both libraries: nothing named profile/side for the JS50.
- Worth viewing (current body, studio-like numbered sets on ligier.fr, angle unknown):
  - https://s3.ligier.fr/ligier-prod/uploads/2026/09/JS50-Ultimate_Toledo-Red_EV-11_13-scaled.webp (2560x1708)
  - https://s3.ligier.fr/ligier-prod/uploads/2026/09/JS50-Ultimate_Toledo-Red_EV-11_10-scaled.webp (2560x1708)
  - https://s3.ligier.fr/ligier-prod/uploads/2026/09/JS50-Ultimate_Reef-Blue_Revo-D_13-scaled.webp (2560x1708)
  - https://s3.ligier.fr/ligier-prod/uploads/2026/09/JS50-Ultimate_Reef-Blue_Revo-D_11-2-1.webp (1920x1280)
  - The same sets probably hold more frame numbers. Query `https://www.ligier.fr/wp-json/wp/v2/media?search=JS50-Ultimate&per_page=100`.
- Reject (old body): `https://media.ligier.fr/app/uploads/2024/05/Ligier-JS50-Rouge-HD-2.png` / `-HD-3.png` and `Ligier-JS50-SU-Rouge-vignette-3.png`. They were uploaded May 2024, before the "Nouvelle JS50" (Mondial, Oct 2024), so they are most likely the previous JS50.

## ligier-js60
- **status: NONE** (no side-named file for the "Nouvelle JS60", Sept 2026)
- Checked:
  - ligier.fr/vehicules/js60/: alt texts only, no side view.
  - Press release https://media.ligier.fr/communique-de-presse/nouvelle-ligier-js60-la-ligier-qui-voit-plus-grand/ and gallery https://media.ligier.fr/mediatheque/nouvelle-js60/: 7 stills and 5 videos, all tagged "Produit, Extérieur", none named by angle. "-90" in NOUVELLE-JS60-ULTIMATE-90 is a frame number, not an angle.
  - Press PDF https://media.ligier.fr/app/uploads/2026/09/2026.09-CP-NOUVELLE-JS60.pdf and equipment sheet https://s3.ligier.fr/ligier-prod/uploads/2026/09/2026P2-004_-_FICHE_EQUIP._JS60_EL-TH_V3.pdf: not readable (blocked).
- Worth viewing (angle unknown):
  - https://media.ligier.fr/app/uploads/2026/09/NOUVELLE-JS60-ULTIMATE-{23,36,37,45,46,89,90}-scaled.jpg (press HD stills)
  - https://s3.ligier.fr/ligier-prod/uploads/2026/10/Ligier-JS60-Ultimate-au-studio-bleu-1.webp (1672x941, "au studio bleu" = blue studio set)
  - https://media.ligier.fr/app/uploads/2026/09/JS60-Ultimate_Blue_Revo-D-_7.jpg, .../JS60-Select_Red_Revo-D_7-1024x683.jpg, .../JS60-Elite_Black_EV_1-1-1024x683.jpg (press-release photos)
- Reject (old body): `https://media.ligier.fr/app/uploads/2024/05/Ligier-JS60-Gris-graphite-HD.png` / `-HD-2.png` / `-HD-3.png`. They were uploaded May 2024, so they show the previous JS60.

## ligier-myli
- **status: CANDIDATE** (file name says "Profile"; not viewed)
- Best: **https://media.ligier.fr/app/uploads/2023/03/2023_Ligier_Myli_ADV-Photo_R.EBEL-Velvet-Green_Profile-1-scaled.jpg** (2560x1692; title "2023_Ligier_Myli_ADV Photo_R.EBEL Velvet Green_Profile"; there is also a 1416x936 copy without "-1-scaled").
  - Source: media.ligier.fr (brand press site), found with the REST media search "profil". Velvet Green, R.EBEL trim (2023).
  - "ADV Photo" means advertising photo, so the background may be a scene rather than a studio. Unknown.
- Alternates (both from media.ligier.fr, not viewed):
  - https://media.ligier.fr/app/uploads/2023/03/Ligier-Myli-R.EBEL-X-vert-profil.jpg (1200x800, "Myli R.EBEL X vert profil")
  - https://media.ligier.fr/app/uploads/2022/09/Profil-scaled.jpg (2560x1494, title "Profil"). Sept 2022 is the month the Myli was unveiled, so this is probably a Myli launch image, but that is my inference; it could also be another model.
- Body check: the Jan 2026 press release says "Myli conserve ce qui a fait son succès (design, …)". The changes it lists are cosmetic: new matt grille treatment, tinted rear windows, Ligier logo and stickers on the tailgate, 13" black wheel covers or optional 16" wheels (LAB), 14" black alloys (MAX). The shell is unchanged, so the 2023 profile shows the current body; only the trim details differ (flag it).
- Checked and rejected: the 2026 gallery https://media.ligier.fr/mediatheque/nouvelle-myli/ ("Ligier Lifestyle" and "Talents" shots, none named by angle). The ligier.fr Myli library lists 2026 shoot files (e.g. https://s3.ligier.fr/ligier-prod/uploads/2026/09/Myli-LAB_Intense-Black_Revo-D-12-scaled.webp, 2560x1707) with unknown angles; worth a look if the 2023 profile turns out to be a scene with people.

## ligier-pulse-4
- **status: CANDIDATE (weak)** (name says "Profile" but also "Social", so probably a lifestyle scene; not viewed)
- Best: **https://media.ligier.fr/app/uploads/2023/07/Pulse-4-L3KS-Forgeon-Social-Profile-2-scaled.jpg** (2560x1692; 1200x800 copy at `.../Pulse-4-L3KS-Forgeon-Social-Profile-2-1.jpg`).
  - Source: media.ligier.fr (brand press site). "L3KS" appears to be the long L7e body (the gallery's long-body videos use the same code). "Forgeon" is a blacksmith scenario; the related videos feature people, so a person may stand in front of the vehicle. Check before use.
- Alternates (PNG, gallery https://media.ligier.fr/mediatheque/ligier-professional-pulse-4/, tagged "Lifestyle, Extérieur", angle unknown; PNG may mean a cut-out):
  - https://media.ligier.fr/app/uploads/2024/05/Pulse-4-long-caisson-HD.png, -HD-2.png, -HD-3.png (long, box body)
  - https://media.ligier.fr/app/uploads/2024/05/Pulse-4-long-plateau-basculant-HD.png, -HD-2.png, -HD-3.png, -HD-4.png (long, tipping flatbed)
- Checked: ligier-professional.fr/product/pulse-4/ (header banner https://www.ligier-professional.fr/wp-content/uploads/sites/118/2023/02/pulse-4-header-1920x793.jpg, angle unknown; other images alt text only). The equipment sheet https://www.ligier-professional.fr/wp-content/uploads/sites/118/2023/07/FICHE-EQUIPEMENT-PULSE-4.pdf was not readable (blocked).

## chatenet-ch46
- **status: NONE**
- Checked:
  - WebSearch "Chatenet CH46 Seitenansicht" and "Chatenet CH46 brommobiel zijaanzicht": only helicopter (CH-46) results and used-car listings.
  - "Chatenet CH46 Importeur Deutschland ... Händler": no importer site found, only used-car portals (autobild, autoscout24, theparking).
  - "Chatenet CH46 catalogue 2026 pdf brochure": nothing relevant.
  - agenceauto.com (Ajaccio): a sold 2019 used car, one photo, angle unknown. Rejected (used car, not current).
  - automoto.it price-list page https://www.automoto.it/listino/chatenet/ch46/ch46-erre-erre/188806: 5 photos `https://cdn-img.automoto.it/images/1923272{6..9}|19232730/2000x/chatenet-ch-46-2019-0{1..5}.jpg`. These are third-party, the file names say 2019, and the angles are not described. Last-resort lead only.
- Not repeated: automobiles-chatenet.com (already rejected in the brief: lifestyle only).

## casalini-650
- **status: NONE** (no side-named file; the library is worth a visual sweep)
- casalini.eu WordPress library, REST searches "650", "starter", "sportiva", "xtreme", "lat":
  - `https://casalini.eu/wp-content/uploads/2026/09/650.png` (1690x703) and `.../650-tras.png` (915x323). The very wide format (2.4:1 and 2.8:1) fits a side view, but these could just as well be a "650" wordmark ("tras" = trasparente?). View them first.
  - Colour renders, 1448x1086 or 1536x1024, with frame numbers: STARTER-*{2,3,7} (e.g. `.../2026/10/CASALINI-STARTER-7.png`, `.../2026/10/STARTER-Grigio-Nardo2-1.png`), SPORTIVA-*{1,2,3,4,6} (e.g. `.../2026/09/SPORTIVA-GT-Grigio-Silver6.png`, `.../2026/10/SPORTIVA-Black1.png`), XTREME-*{2,3,4,8} (e.g. `.../2026/09/XTREME-GT-White8.png`). The colour variants may follow a fixed angle numbering, so one frame number could be a side view.
  - Caution: 1536x1024 is a native output size of common AI image generators, and a small maker producing many colour variants this way is plausible. Check the renders for AI artefacts (brief: reject AI images).
- Already rejected in the brief, not repeated: the front views (CASALINI-starter-front, Xtreme front) and the Sportiva 3/4 renders.
- Checked: dealer search (largus, annonces-automobile, autoscout24.at Riedhart) gave only listings. The Riedhart "M20 650" naming means older M20 photos could be mistaken for the 650. Reject any M20-era image.

---

## Summary
| model | status | best URL |
|---|---|---|
| ligier-js50 | NONE | (to view) https://s3.ligier.fr/ligier-prod/uploads/2026/09/JS50-Ultimate_Toledo-Red_EV-11_13-scaled.webp |
| ligier-js60 | NONE | (to view) https://s3.ligier.fr/ligier-prod/uploads/2026/10/Ligier-JS60-Ultimate-au-studio-bleu-1.webp |
| ligier-myli | CANDIDATE | https://media.ligier.fr/app/uploads/2023/03/2023_Ligier_Myli_ADV-Photo_R.EBEL-Velvet-Green_Profile-1-scaled.jpg |
| ligier-pulse-4 | CANDIDATE (weak, likely scene) | https://media.ligier.fr/app/uploads/2023/07/Pulse-4-L3KS-Forgeon-Social-Profile-2-scaled.jpg |
| chatenet-ch46 | NONE | - |
| casalini-650 | NONE | (to view) https://casalini.eu/wp-content/uploads/2026/09/650.png |
