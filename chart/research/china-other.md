# china-other — research report (Chinese makers other than Geely Holding and Leapmotor)

## Progress note (keep at top)
- 2026-10-22, FINAL for this pass. `china-other.json` is valid: 73 models, 13 announced, 11 discontinued,
  ~75 sources. Line-ups/statuses: done from official sites + 2026 press. Twins: done with sources.
  carsized: 22 side views + 3 front views captured before the coordinator stopped image work (the
  separate image pipeline takes over; probed-but-blank slugs are listed in `carsized_china_other.json`).
  Commons categories are best-guess names (NOT verified) unless the notes say otherwise.
- Constraints hit: the shared WebSearch quota ran out early and the WebFetch quota was exhausted
  repeatedly, so some official sites could not be read (robots-blocked: bydauto.ch, saicmaxus.eu/.de,
  maxus.ch, voyah.eu, omodajaecoo.ch model pages, gwmora.co.uk, elaris.de, lepas.com; wrong/absent
  domains: gwm.de, gwm.ch, gwm.co.uk, chery.co.uk, omoda.de). Everything marked VERIFY in the JSON
  notes is a judgement call made without a direct official confirmation.
- Build: `python3 -I build_china_other.py` regenerates the JSON from the script (data lives there);
  `carsized_china_other.json` holds the image results keyed "Brand Model".

## 1. Which brands sell through official channels in Europe (Oct 2026)

Included (official brand/importer site with current line-up in at least one of DE/FR/UK/IT/ES/NL/CH/NO/SE/BE/AT):

| group | brand (column) | evidence | models in JSON |
|---|---|---|---|
| SAIC Motor | MG | mgmotor.ch / mgmotor.eu model menus (Oct 2026) | 11 (MG3, MG4, MG4 Urban, MGS5 EV, ZS, HS, MGS6 EV, MGS9 PHEV, Cyberster, IM5, IM6) |
| SAIC Motor | Maxus | saicmaxus.co.uk range (10 models) + carwow.de listings | 9 (eDeliver 3, eDeliver 5, Deliver 7/eDeliver 7, Deliver 9/eDeliver 9, eTerron 9, T90 EV, T60 Max, Mifa 7, Mifa 9) |
| SAIC Motor | IM | sold as "MG IM5 / MG IM6" through MG dealers (UK/NO/CH since Jul 2025, DE/FR/BE/NL since Jul 2026) | filed under MG (see judgement calls) |
| BYD | BYD | byd.com/uk menu (14 models) + German price list Sept 2026 + Swiss sources | 13 (Dolphin Surf, Dolphin, Dolphin G, Atto 2, Atto 3, Seal, Seal 6, Seal U, Sealion 5, Sealion 7, Ti 7, Tang, Shark) |
| BYD | Denza | denza.com/de (Z9GT, D9, Z, BAO 5), UK orders open Jul 2026 | 1 on sale (Z9 GT) + 3 announced (D9, BAO 5, Z) |
| Chery | Omoda | omodaauto.co.uk (Oct 2026) | 3 (Omoda 5, 7, 9) + Omoda 4 announced |
| Chery | Jaecoo | jaecoo.co.uk (Oct 2026) | 3 (Jaecoo 5, 7, 8) |
| Chery | Chery | UK (carwow Oct 2026), ES/IT/PL importers; DE 1H 2027 | 4 (Tiggo 4, 7, 8, 9) + Chery Q announced |
| Chery | Lepas | European roll-out Q3/Q4 2026, UK dealer page live, no price list found | 0 on sale, L8 announced |
| Great Wall Motor | Ora / Wey / Haval | German dealer/leasing listings (Oct 2026), Haval DE launch Mar 2026, UK carwow | Ora 2 (03, 07) + Ora 05 announced; Wey 2 (03, 05); Haval 2 (Jolion Pro, H6) + H7/Jolion Max announced |
| XPeng | XPeng | xpeng.com/de with configurators (Oct 2026); CH via Emil Frey | 6 (G6, G9, G9L, P7+, X9, L03) |
| NIO | NIO | nio.com/de_DE lists 6 models, but no factory orders since 2026 -> all RUNOUT | 5 tiles (ET5/ET5 Touring, ET7, EL6, EL7, EL8) |
| NIO | Firefly | NL/NO/BE/DK/GR/AT/PT since 2025, UK 2026 | 1 |
| Changan | Deepal | DE/IT/ES/UK/NO/DK (electrive Dec 2025) | 2 (S05, S07) |
| Dongfeng | Voyah | voyah.nl (NL) and voyah.no (NO) Oct 2026; CH via Noyo | 3 (Free, Dream, Courage) |
| Dongfeng | Dongfeng / Mhero | listed by the Dutch importer on voyah.nl (Oct 2026) | Dongfeng Box 1, Mhero I 1 (both VERIFY) |
| FAW | Hongqi | hongqi.no/biler (Oct 2026): EHS5, EH7, EHS7, E-HS9 with NOK prices | 4 |

Excluded (one line each):
- **Xiaomi** — Europe launch announced for 2027 (SU7/YU7); nothing on sale. Listed under `announced`.
- **Avatr / Nevo (Changan)** — planned for Europe by 2027; not on sale. Listed under `announced`.
- **Onvo (NIO)** — Europe pushed to 2028-29 (eletric-vehicles.com, Sept 2026).
- **Exeed / Exlantix (Chery)** — European entry "on hold through 2026" (Nov 2025); iCaur due Italy 2027.
- **GWM pickups (Poer/Cannon) and Tank** — no evidence of official European sales found (UK carwow page
  exists for a "Poer 300 LCV" but showed no such model); not included.
- **JAC** — carify (Apr 2026) names e-JS1/e-JS4 as available in Switzerland and JAC vans/pickups are sold
  by importers in IT/ES/DE, but no official-network evidence could be fetched; excluded (verifier may add).
- **Seres/DFSK, Skywell/Elaris, BAIC, Jetour, Forthing** — importer-only or unverifiable in this session
  (no search quota); excluded. Elaris and DFSK/Seres were importer-driven in DE/IT; status unknown for 2026.
- **Aiways** — collapsed 2023-24; no official sales.
- **MG iEV12** (commercial-vehicles.mgmotor.eu) — a 12 m electric bus, outside the 3.5 t scope.
- **Ebro (Spain), DR / Sportequipe (Italy)** — not Chinese brands but they sell tier-1 rebadges of the
  Chery Tiggo 7/8 (and Tiggo 4); named in `twin_members` only. If the chart wants them as columns, the
  group label would be "EV Motors (Ebro)" and "DR Automobiles Groupe".

## 2. Model counts and notable line-up findings
- MG: two MG4 generations are sold side by side: the 2022 RWD "MG4 EV" (64/77 kWh, XPower) and the
  2025 FWD second generation sold as "MG4 EV Urban" (UK Jan 2026, AT Feb 2026, CH/EU menus Oct 2026).
  Treated as two tiles ("MG4", "MG4 Urban"). New in 2026: MGS6 EV (4.71 m, DE orders 16 Mar 2026),
  MGS9 PHEV (= Roewe RX9, 4.98 m, 7 seats, marked NEW on the CH/EU sites), MG IM5/IM6 (DE Jul 2026).
  Dropped (May 2025): MG5 Electric, ZS EV (-> MGS5 EV), Marvel R.
- Maxus: UK range = eDeliver 3/5/7/9, eTerron 9, Mifa 7/9, Deliver 7/9 (diesel), T60 Max. "Deliver 7 /
  eDeliver 7" and "Deliver 9 / eDeliver 9" are one tile each (same body, powertrain-variant names).
  T90 EV kept (German listings) but weak; T60 Max / T90 EV are tier-1 twins of each other.
- BYD: UK menu Oct 2026 adds several nameplates not yet in Germany: Ti 7 DM-p (= Fangchengbao Ti7,
  ~5.0 m EREV "Urban Box" SUV), Dolphin G DM-i (PHEV hatch, DE "coming"), Sealion 5 DM-i, Shark DMO
  pickup, Seal 6 DM-i saloon (DE has only the Touring). BEV Seal U and Han are gone. Denza: Z9 GT on
  sale (EU pre-orders Apr 2026, UK orders Jul 2026); D9 pre-orderable (EUR 80-90k, configurator "soon");
  BAO 5 has a configurator but "no EU type approval yet" -> announced; Denza Z listed, status unknown.
- Chery group: Omoda 5/7/9, Jaecoo 5/7/8 on sale (UK official sites); Chery Tiggo 4/7/8/9 on sale in
  the UK, Germany 1H 2027; Omoda 4 (Paris Oct 2026, UK 2027) and Chery Q announced; Lepas L8 announced.
  Switzerland: omodajaecoo.ch is still "Coming soon" (Grand Automotive) -> ch_on_sale=false.
- GWM: Germany now has Haval (Jolion Pro from EUR 24,990, H6 hybrid from EUR 31,990, launch Jan-Mar 2026)
  next to Ora 03/07 and Wey 03/05; Ora 05 listed but "not yet on sale"; UK: Jolion Pro on sale, Ora 03
  "currently unavailable new" (UK runout). No Swiss presence found.
- XPeng DE (Oct 2026): L03 (NEW, 4.65 m SUV coupé, EUR 35,600, BEV + PowerX range-extender,
  configurator live), G9L (NEW, 5.12 m 6/7-seat flagship, EUR 85,600, configurator live), G6, G9, P7+, X9.
  The first-gen P7 is gone. CH: G6/G9 via Emil Frey.
- NIO: all six models still listed in Germany, but no build/order function anywhere in Europe since
  2026, Hamburg Nio House closed Jul 2026, stock clearance -> status "runout" for ET5/ET5 Touring (one
  tile), ET7, EL6, EL7, EL8. Firefly on sale (NL EUR 29,900).
- Deepal S05/S07 on sale in DE/IT/ES/UK/NO (PHEV/REEV versions due 2026). No Changan-brand or Avatr
  models yet.
- Voyah: Courage current in NO (NOK 299,990) and NL (EUR 39,990); Free and Dream "utgatt modell" in
  Norway but still priced by the Dutch importer (Free also via Noyo in CH) -> both kept on_sale.
  The Dutch importer also lists Dongfeng Box (Nammi 01, 42.3 kWh) and Mhero I (M-Hero 917, 142.7 kWh,
  showroom cars) -> added as brands "Dongfeng" and "Mhero" under group Dongfeng, flagged VERIFY.
- Hongqi Norway (Motor Gruppen/HBI): EHS5 (new 2026, 4,750 mm, NOK 439,900), EH7 (499,900), EHS7
  (544,900), E-HS9 (1,299,990).

## 3. Twin groups (tier, members, sources)
- **c-suv, tier 2 — Chery compact family**: Omoda 5, Omoda 7, Jaecoo 7, Chery Tiggo 7. Sources:
  Wikipedia Omoda 7 ("stretched version of the Omoda C5 platform"; = Chery Tiggo 7L), Wikipedia
  Jaecoo 7 (= Chery Tansuo 06, sold in China as "Tiggo 7 High Energy"), Wikipedia Chery Tiggo 7.
  Same 1.6T DCT / 1.5T SHS PHEV drivetrains, similar wheelbases (2,630-2,720 mm), distinct bodies.
  NOTE for the verifier: the Omoda 5 is, strictly, the Chinese "Tiggo 5x High Energy", i.e. closest to
  the Tiggo 4/5x line (b-suv, 4,318 mm) — cross-row, so no group with the Tiggo 4.
- **c-suv, tier 1 — Chery Tiggo 7 rebadges**: Chery Tiggo 7 <-> Ebro S700 (ES, licence-built), DR 6.0 and
  Sportequipe 6 (IT). Source: Wikipedia Chery Tiggo 7 (explicit sentences). Recorded on the Tiggo 7 tile
  (twin_tier=1); its tier-2 link to Omoda/Jaecoo is in the note because a tile holds one tier only.
- **d-suv, tier 1 — Chery Tiggo 9 <-> Jaecoo 8**: Wikipedia Chery Tiggo 9 ("also exported under the Jaecoo
  brand as the Jaecoo J8/8"), T1X, 4,820 mm. Both on sale in the UK.
- **d-suv, tier 1 — Chery Tiggo 8 <-> Ebro S800** ("rebadged and sold in Spain by Ebro as the Ebro S800",
  Wikipedia Tiggo 8); DR 7.0 / Sportequipe 7 listed as names without an explicit sentence. Lepas L8 is a
  derivative of the NEW second-gen Tiggo 8 (4,670 mm) -> no tier with the UK Tiggo 8 (gen 1 body).
- **d-suv, tier 2 — Deepal S07 <-> Mazda CX-6e** (Mazda EZ-60 "heavily based on the Deepal S07", EPA1,
  Wikipedia). Mazda 6e (EZ-6) is an EPA1 sibling of the Deepal L07, which is NOT sold in Europe -> the
  6e has no European Deepal twin (tell the Mazda agent).
- **pickup, tier 1 — Maxus T60 Max <-> Maxus T90 EV** (same cab/body, diesel vs electric).
- **Not grouped (deliberately)**: Omoda 9 (= Exeed RX; Exeed not in Europe); MGS9 (= Roewe RX9/MG QS, not
  in Europe); MG IM5/IM6 (= IM L6/LS6); BYD Seal U vs Sealion 7 (different platforms); BYD Seal / Sealion 7
  (same e-Platform 3.0 but different rows); XPeng G6/G9/G9L (same brand, same SEPA 2.0 — treated as a
  range, not twins); Hongqi EH7/EHS7 (different rows); Jaecoo 5 (no platform information found);
  Voyah Free/Courage (no evidence of shared body).

## 4. Row / tier judgement calls the verifier should look at
- MG ZS (4.43 m) kept in b-suv per MG positioning; MG HS (4.66 m) in c-suv; MGS6 EV (4.71 m) in d-suv;
  MGS9 (4.98 m, 7 seats) in e-suv; IM5 (4.93 m) in d-car (Model 3/Seal rival) and IM6 (4.90 m) in d-suv.
- IM5/IM6 are filed under brand "MG" (marketed as "MG IM5/IM6"); move to an "IM" column if wanted.
- BYD Sealion 5 (~4.7 m, "compact" per BYD) placed d-suv by length; Ti 7 (~5.0 m) e-suv; Dolphin G
  (~4.0 m, PHEV hatch) b-hatch with approximate length; Seal 6 saloon + Touring one tile (d-car).
- Jaecoo 5 (4.38 m) c-suv (with Omoda 5) rather than b-suv; Chery Tiggo 4 (4.32 m) b-suv.
- XPeng P7+ (5.02 m) e-car although priced as a D-car; L03 (4.65 m) c-suv; G9L (5.12 m) e-suv.
- Ora 03 (4.24 m) c-hatch; Firefly (4.00 m) b-hatch; Voyah Free (4.905 m) e-suv; Wey 05 (4.87 m) d-suv.
- Maxus eDeliver 5 (4.8 m, 1-t class) placed van-small (between Transit Connect L2 and Transit Custom).
- Two tiles for "MG4" and "MG4 Urban" (different generations sold concurrently under different names).
- NIO ET5 and ET5 Touring merged into one tile (body styles), status runout for the whole NIO range.
- Denza BAO 5 kept as announced despite a live configurator (no EU type approval yet, Oct 2026).

## 5. Open questions / unverified items (search quota was exhausted, fetch quota rationed)
1. Swiss availability: BYD (bydauto.ch blocked) — only Dolphin Surf, Atto 2, Atto 3, Seal, Seal U,
   Sealion 7, Tang confirmed via press; Maxus CH (maxus.ch blocked); GWM, Changan, Hongqi, Denza, XPeng
   P7+/X9/L03/G9L, Firefly in CH unknown (null).
2. Maxus T90 EV: only a German dealer listing — may be runout; eTerron 9 / Mifa 7 / T60 Max continental
   availability unknown (UK confirmed).
3. BYD Ti 7 length (4,999 mm) and Dolphin G / Sealion 5 lengths are from general knowledge, not the
   fetched pages; Ti 7 row (e-suv) depends on it.
4. Lepas L8: UK dealer page exists; whether UK/IT orders are open by late Oct 2026 could not be confirmed.
5. Ora 05 / Haval H7 / Jolion Max launch status in Germany (listed as announced from Oct 2025 press).
6. GWM UK official site could not be read (domain unknown); Ora 07 and Wey models in the UK unverified.
7. Dongfeng Box and Mhero I: listed by the Dutch importer without price/explicit order status.
8. NIO: whether Norway (outside EU) still takes factory orders — the Aug 2026 source says no.
9. Hongqi EH7/EHS7/E-HS9: Norwegian prices confirmed; NL/SE/DK not checked.
10. Commons categories: all best-guess names; none verified (image pipeline to check).
11. carsized: 22 side views (ids copied verbatim) + 3 front views; the entries for MG4 (2022-2025),
    XPeng G6/G9 (2023/2022-2025) and Omoda 5 (2022-2025) are the pre-facelift entries — carsized may hold
    newer entries under slugs not guessed. Blank probes are recorded in `carsized_china_other.json`.

## 6. Sources
See the `sources` array in `china-other.json` (official brand sites: mgmotor.ch/.eu, saicmaxus.co.uk,
byd.com/uk, denza.com/de, omodaauto.co.uk, jaecoo.co.uk, xpeng.com/de, nio.com/de_DE, voyah.nl/.no,
hongqi.no; press: electrive, InsideEVs, ecomento, autohaus.de, autonotizen, auto motor und sport,
carwow, CarGurus, Fleet World, Gasgoo, carnewschina, chinaevhome, autoevolution, carify; Wikipedia for
twin relationships).
