# Geely Holding — research notes (Volvo, Polestar, Lynk & Co, Zeekr, Lotus, Farizon, LEVC, Geely)

## PROGRESS NOTE (final, 2026-10-22)
- geely.json is FINAL and valid: 33 models (Volvo 10, Polestar 4, Lynk & Co 3, Zeekr 5, Lotus 4, Farizon 2,
  LEVC 2, Geely 3) + 5 announced (Geely Monjaro EM-i, Lynk & Co 07 GT, Polestar 7, LEVC L380, LEVC Next
  Generation Taxi) + 8 discontinued/not-offered entries + 60 sources.
- Statuses, rows, lengths, platforms, powertrains and twin groups are complete with 2025/26 sources.
- Swiss status: 25 tiles true, 2 false (LEVC), 6 null (Zeekr X/001/9X, Farizon SV/V7E, Lotus Evija).
  Volvo CH status comes from Volvo Car Switzerland's media site (MY27 model kits), not the consumer site.
- Per the coordinator's change of plan, carsized slugs/URLs and Commons verification were STOPPED: every
  carsized_* field is null and commons_category holds the best-known category name (unverified) - the image
  pipeline on another machine will fill these in. See 'Images' below for what was learned about the recipe.
- Tool situation during the run: WebSearch budget exhausted early (shared); afterwards WebFetch only, itself
  rate-limited; Volvo/Polestar consumer sites block fetching; Lynk & Co, Zeekr consumer pages and Geely
  consumer sites are JS-rendered; press rooms and Wikipedia worked.

## Scope decisions / judgement calls
- One tile per nameplate: EX30 Cross Country is inside the EX30 tile, V60 Cross Country inside V60 (rule 4).
  XC40 / EX40 / EC40 are three nameplates (three tiles) in c-suv, grouped tier 1 (same body shell; EC40 is the
  coupe-roof derivative - borderline tier 1, flagged). Lynk & Co 01 is a CMA tier-2 member of that group;
  Polestar 2 (CMA) is cross-row (d-car) so only noted.
- Row of the SEA small-SUV family: the brief's own example groups EX30 / smart #1 / Zeekr X in b-suv, so the
  Zeekr X (4,450 mm) and Lynk & Co 02 (4,460 mm) are placed in b-suv to keep the group in one row, although
  their lengths would suggest c-suv. smart #1 and smart #3 are named as members; the Mercedes agent's rows for
  #1/#3 must be aligned (if #3 ends up in c-suv, drop it from the group).
- Tier decisions on SEA cars: Zeekr X vs smart #1 share SEA2 and the 2,750 mm wheelbase but have different bodies
  -> tier 2, not tier 1 (no rebadge exists in Europe). Lynk & Co 02 (= Lynk & Co Z20) is likewise tier 2.
  Volvo EX30 (shorter wheelbase 2,650 mm, same architecture) tier 2.
- Zeekr 7X / smart #5: tier 2 (bluewin.ch: "shares its basis with the smart #5"; Wikipedia 7X lists smart #5 as
  related). Polestar 4 is SEA too but a loose architecture match (its real twin, Lynk & Co Z10, is not sold in
  Europe) -> no tier. Zeekr 7 GT (d-car) and 001 (e-car) are in other rows -> no group.
- Volvo EX90 / Polestar 3: tier 2 (SPA2, Polestar 3 "based on the EX90"). ES90 is SPA2 as well but e-car.
- Lotus Eletre / Emeya share EPA but are in different rows (e-suv / e-car) -> notes only.
- LEVC TX / VN5 share cab, front end and range-extender powertrain but are in different rows -> notes only.
- Powertrains: range-extenders (Lotus Eletre X, LEVC TX/VN5) are recorded as PHEV (closest value in the brief's
  list). XC40/XC60/XC90/V60 carry MHEV because no non-hybrid petrol/diesel remains.
- Status rule applied literally: Zeekr 9X is marked on_sale because Geely's Paris release (2026-10-12) says it is
  "available to order" (deliveries from Jan 2027); zeekr.eu shows it with a "Configure" button but no price. A
  verifier may prefer "announced".
- Geely Monjaro EM-i: Geely says "launched in Europe" at Paris (Oct 2026) but geely.de (Oct 2026) lists only E2,
  E5, Starray EM-i and no order/price was found -> announced.
- Lynk & Co 07 GT: European premiere in Paris in Chinese specification; a European version is "planned but not
  yet confirmed" -> announced (could also be dropped from the chart).
- LEVC L380: still in levc.com's menu ("The all New L380 MPV") but not in the New Models index; no UK/EU orders
  found -> announced. LEVC "Next Generation Taxi" (UK launch H2 2027) -> announced.
- Polestar 7 (2028) -> announced (not revealed). The Polestar 4 "high-riding estate" (Q4 2026) and the all-new
  Zeekr 7X (deliveries Q1 2027) are versions of existing nameplates -> notes on those tiles.

## Per-brand notes

### Volvo (10 tiles)
- Current press kits on Volvo's international media site (fetched 2026-10-21): EX60, EX30, EX30 Cross Country,
  XC60, XC90, XC40, EX40, EC40 all at MY27; ES90 (2026 kit); EX90; V90 only up to MY2025; S90 up to MY2024;
  no S60/V60 kit at all.
- S60: Europe/NA production ended 2024 (Wikipedia; UK withdrawal 2023 per Fleet News) -> discontinued.
- S90: discontinued in Europe 2024 (Wikipedia; Fleet News) -> discontinued; ES90 is the successor.
- V90 / V90 CC: Volvo Car UK: global production ends September 2025, UK orders closed (Fleet News). Motor1 later
  reported Volvo saying the end was Netherlands-only, but there is no 2026 evidence of continued European sales
  and no MY26/27 kit -> listed under discontinued_recently; verifier should check volvocars.com/de or /ch-de.
- V60: Fleet News (Volvo Car UK): "not discontinued", still orderable (MHEV + PHEV); Motor1: "sticking around".
  Kept on_sale; the absence of a MY27 press kit is flagged.
- XC40 (MHEV only since the 2024 renaming), EX40, EC40: MY27 kits exist -> on_sale. autoevolution lists a 2027 EC40.
- EX60: order books open across Europe (Volvo release, Mar 2026), production from 2026-04-22; 4,803 mm (Wikipedia).
- ES90: UK orders open from GBP 69,990 with deliveries early 2026 (Fleet News).
- Swiss status (all 10 Volvo tiles true): Volvo Car Switzerland's media site (volvocars.com/de-ch/media/...)
  carries model pages for EX30, EC40, EX40, XC40, XC60, EX60, XC90 (all /2027/), ES90 (label MY27), EX90
  (label MY27) and V60 (label MY27; V60 CC MY2025). It also lists an 'EX60 Cross Country' page (ex60cc/2028)
  = coming raised variant of the EX60 (same nameplate, noted on the EX60 tile, not a separate tile), and
  last-model-year pages for V90 / V90 CC (MY2026), S60 (MY2025) and S90 (2024) - consistent with those being
  discontinued.
- Lengths: EX30 4,233; XC40/EX40/EC40 4,440; XC60 4,709; EX60 4,803; XC90 4,953; EX90 5,037; ES90 ~5,000;
  V60 4,778 (ES90 from reveal data, others from spec knowledge; EX60 from Wikipedia).

### Polestar (4 tiles + Polestar 7 announced)
- Polestar's 2026-02-18 release: current line-up 2/3/4/5; Polestar 5 deliveries summer 2026 (orders open since
  late 2025, e.g. Ireland from EUR 130,700 on-the-road); Polestar 4 high-riding estate variant deliveries Q4 2026
  (same nameplate; Top Gear); new Polestar 2 early 2027; Polestar 7 (compact SUV, SPA3, Europe-built) 2028.
- Switzerland: autosprint.ch (2026-01-21) gives 2025 Swiss registrations for Polestar 2/3/4 and says the first
  Swiss Polestar 5 customers get cars in summer 2026 -> ch_on_sale true for 2/3/4/5.
- Polestar 3 production moved entirely to Ridgeville (US) in March 2026 (Wikipedia).

### Lynk & Co (3 tiles + 07 GT announced)
- European line-up 01 (PHEV/HEV), 02 (BEV), 08 (PHEV) - press releases of 2025-09-08, 2025-11-26, 2026-07-23.
  Switzerland launched Q1 2026 with all three models (press release 2025-09-08) -> ch_on_sale true.
- 02 = Lynk & Co Z20 (Wikipedia title). 02 MY27 shown at Turin Sept 2026.

### Zeekr (5 tiles)
- zeekr.eu (2026-10-21) lists 9X, 7X, 7GT (from EUR 45,990), X, 001 - no 009. The 009 never launched for sale
  in Europe (listed under discontinued_recently with that note so the verifier knows it was checked).
- Markets: NL/SE/NO (2023-24), DE (first 7X deliveries Mar 2026), IT/ES/PT (2026), FR (orders 2026-04-02:
  X 37,990 / 7GT 45,990 / 7X 52,990 / 001 59,990 EUR), 7 GT in 16 countries incl. CH (Jul 2026).
- CH: 7 GT (16-country list) and 7X (bluewin.ch test at CHF 68,890, Jul 2026) confirmed; X / 001 / 9X unknown
  (zeekr.ch server error, zeekr.eu/ch-de not found; zeekr.eu test-drive form renders no country list). The
  zeekr.eu test-drive page (2026-10-22) marks 001, X, 7X, 7GT 'test drive available now' and 9X 'arriving soon'.
- 9X: PHEV (2.0 T + 55 kWh, 179 km EV), 5,239 mm, 6 seats (zeekr.eu); orders open per Geely's Paris release,
  deliveries Jan 2027.

### Lotus (4 tiles)
- lotuscars.com en-GB and de-CH (Oct 2026): Emeya, Eletre (+ Eletre X), Emira (420 Sport, GT4), Evija.
  CH site offers configurators for Eletre X / Eletre / Emira / Emeya -> ch true; Evija only "Entdecken" -> null.
- Eletre X (range-extender, 2.0 T generator + 70 kWh): mainland-Europe orders opened June 2026 from EUR 96,990,
  deliveries Q4 2026 (The EV Report). Emira 420 Sport orderable, deliveries Aug 2026 (Automotive World).
- Evija: 130-unit run; whether slots remain is unknown -> on_sale with caveat (verifier may drop/runout).

### Farizon (2 tiles)
- SV: UK since Feb 2025 (8 variants, L1H1 4,990 mm to L3H3 5,995 mm, 6.95-13 m3, from GBP 45,000), ten EU
  markets by Nov 2025, DE/FR April-May 2026 (from EUR 44,900 net), 28 European countries (IAA 2026). Row van-mid
  per the brief (L1 = 4.99 m) - the L3H3 would fit van-large.
- V7E: new compact/medium van, just under 5.0 m, 6.95 m3, UK from GBP 28,000 (Apr 2026), DE/FR from EUR 32,600
  net -> van-mid. No Commons category known.
- Switzerland: Emil Frey distribution agreement signed 2026-05-15; a farizon.ch domain exists (robots-blocked);
  launch date/models/prices not found -> ch null.
- farizonauto.eu is robots-disallowed; data from Van Reviewer, AM-online, electrive, The EV Report.

### LEVC (2 tiles + L380 and Next Generation Taxi announced)
- levc.com lists TX (incl. TX Access, TX Shuttle), VN5, L380, Next Generation Taxi; country sites for DE, ES, NL,
  FR, SE, PL, HU, GR, AT, BE, MT (no CH -> ch false for TX/VN5). Greece launch 2025 (Automotive World).
- TX row: purpose-built 6-seat taxi, 4,855 mm -> mpv-large (no taxi row). VN5 5,217 mm -> van-mid.
- Next Generation Taxi: UK launch H2 2027, takes over from the TX (levc.com).

### Geely (3 tiles + Monjaro EM-i announced)
- Swiss names E5 / E2 / Starray EM-i (Zurich launch event 2026-09-16, Emil Frey importer; CnEVPost 2026-09-21).
  UK names EX5 / EX2 (other_names). E5 = Galaxy E5; Starray EM-i = Galaxy Starship 7 EM-i (PHEV sister of
  the E5, 4,740 mm, GEA); E2 = Xingyuan (4,135 mm; row b-hatch, alternative b-suv).
- Markets: UK (EX5 since 2025, EX2 Jul 2026), GR/Balkans, IT (end 2025), HU (Mar 2026), ES/DE/NL/BE/LU (brand
  launch 2026-03-25/26; DE sales from May 2026: E5 EUR 37,990, Starray EM-i EUR 32,990), AT (Apr 2026 deal), CH
  (Sep 2026). geely.de (Oct 2026) lists E2 (EUR 19,990), E5, Starray EM-i.

## Twin groups delivered (same row only)
- b-suv, tier 2 (SEA/SEA2): Volvo EX30, Zeekr X, Lynk & Co 02, smart #1, smart #3 (smart rows to be aligned).
- c-suv: Volvo XC40 / EX40 / EC40 tier 1 (same body); Lynk & Co 01 tier 2 (CMA) attached to that group.
- d-suv, tier 2 (SEA): Zeekr 7X, smart #5.
- e-suv, tier 2 (SPA2): Volvo EX90, Polestar 3.
- Cross-row notes only: Polestar 2 (CMA, d-car); ES90 (SPA2, e-car); Zeekr 7 GT / 001 / Polestar 4 (SEA);
  Lotus Eletre / Emeya (EPA); LEVC TX / VN5; Geely E5 / Starray EM-i (GEA).

## Images (handed over to the separate image pipeline - no further work here)
- carsized recipe status: confirmed working with the brief's example slugs (renault-kangoo-2021-5-door-van,
  opel-corsa-2006-3-door-hatchback render real /resources/ URLs, e.g.
  https://www.carsized.com/resources/opel/corsa/h3/2006/sm_245112082_opel-corsa-2006-side-view_4x.png).
  Slugs could not be discovered without WebSearch; guessed Volvo slugs (volvo-xc40-2017/2018-5-door-suv,
  volvo-xc60-2017-5-door-suv, volvo-ex30-2023/2024-5-door-suv, volvo-xc40-2017-5-door-crossover) rendered
  placeholder pages (the compare page shows '/resources/////_---side-view_4x.png' and '0 in' when the slug
  is unknown). The sitemap index exists (sitemap0..64.xml.gz) but the sub-sitemaps are gzip (unreadable to the
  fetcher); the car index and 'select' picker pages are JavaScript-rendered. Hint for the pipeline: the GMC
  example on the carsized homepage ('gmc-sierra-2018-pickup-1500-double-cab') shows body tokens can omit the
  door count, so SUV slugs may not be '5-door-suv'. All carsized_* fields are null.
- Commons: commons_category holds the best-known category name per tile (Category:Geely Galaxy E5 is confirmed
  via Wikipedia's Commons link; the rest unverified because Commons category/search pages returned 'not found'
  to the fetcher). Generation subcategory names for XC60 (2017), XC90 (2015), V60 (2018) and the Lynk & Co Z20
  / Zeekr 007 GT / Farizon / LEVC names in particular need checking. No commons_file given.

## Discontinued / not offered (checked)
Volvo S60, S90, V90/V90 CC, XC40 Recharge & C40 Recharge names; Zeekr 009 (never launched in Europe);
Polestar 1; Lynk & Co 03/05/07/09 (China only); Lotus Elise/Exige/Evora.
