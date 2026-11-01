# jlr-independents — research report (checked 2026-10-21/22)

## PROGRESS NOTE (keep at top)
- FINAL (2026-10-22): research closed per coordinator. JSON = 50 models (41 on_sale, 9 runout) + 3 announced (Jaguar Type 01, Range Rover GT, Ferrari Luce) + 23 recently-discontinued notes + 48 sources; valid JSON, uniform 28 keys.
- Closed in the last pass: Range Rover Electric = on sale (UK orders open, from £154,070, Electrifying 2 Sep 2026) and Range Rover Sport Electric = on sale (orders open, from £110k, Autotrader 30 Sep 2026) → both folded into the Range Rover / Range Rover Sport tiles as BEV powertrains (same body = same nameplate tile); Discovery Sport → `runout` (no longer factory-orderable in FR/DE/ES, production ends Dec 2026, Autocar Oct 2026); Lucid Gravity confirmed configurable on lucidmotors.com/de-de (ab 94.900 €).
- Images: carsized side-view URLs confirmed for 23/50 tiles, front view for 1 (Trafic); the rest were left null on the coordinator's instruction (image lookups move to a separate pipeline). Known-but-unfetched carsized slugs: ferrari-849-testarossa-2026-coupe, aston-martin-vantage-2018-coupe, mclaren-artura-2022-coupe, land-rover-range-rover-velar-2023-suv, aston-martin-dbx-2020-suv (page rendered empty twice). Confirmed absent on carsized: Ineos Quartermaster, Ferrari 296 coupé, Aston DB12, McLaren W1; search found nothing for Actyon, Musso (diesel), Iveco Daily, Renault Master IV, VF 6, Amalfi, F80, 750S, GTS, Valhalla, Plus Four, Supersport, Tourbillon, Mistral, Nevera, Jesko, Gemera, CC850, Utopia, current Caterham. Commons categories are from knowledge, not re-verified (flagged in `notes`).
- Web budget: WebSearch (200/turn) and WebFetch (400/h) are shared and were exhausted several times; no confirmed page was re-fetched.

## What was checked, per brand

### Jaguar (Tata Motors) — 0 on sale, 1 announced
- jaguar.com/de-ch shows only the "Type 01" (newsletter for launch dates, no configurator). autoevolution (5 Jul 2026): no Jaguar built since 19 Dec 2025 (last F-Pace SVR); "you can no longer order a brand-new Jaguar … anywhere in the world". CAR (May 2026): name confirmed 12 May 2026.
- Auto Express (9 Oct 2026): Type 01 unveiled in New York; the event "kicked off the Type 01's commercial introduction before first deliveries in summer 2027"; ~£120,000; 1,015 bhp, ~120 kWh, 435-mile WLTP target; 5.2 m long, JEA platform. No CH price/configurator on 2026-10-21 → kept in `announced` (row e-car). Verifier: if a DE/UK configurator is live, move to `models` as on_sale.
- Discontinued 2024–25: XF, XE, F-Type, E-Pace, I-Pace, F-Pace.

### Land Rover (Tata Motors) — 7 on sale (1 runout), 1 announced
- CH prices (rangerover.com/de-ch, landrover.ch, 2026-10-21): Range Rover 159'600, RR Sport 113'900, Velar 85'100, Evoque 68'900, Discovery 96'600, Discovery Sport 65'700, Defender 90/110/130/OCTA/Hard Top 92'700–220'900.
- Range Rover Electric: "has finally gone on sale … orders are open", from £154,070, 118.5 kWh, 372 mi (Electrifying, 2 Sep 2026); CH page still waitlist/reserve without price → BEV added to the Range Rover tile. Range Rover Sport Electric: "Orders are open now", from £110,000, 374 mi (Autotrader, 30 Sep 2026); CH "personalisieren und reservieren", no price → BEV added to the Range Rover Sport tile. (Judgement: electric versions are the same nameplate/body → same tile, like Kona/Kona Electric; split if the chart wants separate EV tiles.)
- Discovery Sport: JLR "production will end in December 2026"; Autocar (Oct 2026): "can no longer be ordered from the factory in France, Germany or Spain" (EU GSR2), still configurable in UK and CH → `runout`.
- Evoque and Velar "live on" (Autocar, Oct 2026): no end dates; Evoque may run until the EMA-based "Defender Sport" (2027, not yet revealed – not listed). Range Rover GT = "the first car built on our new EMA architecture", pre-series shown on the CH site, no price/dates → `announced` (row provisional d-suv).
- Twins: Range Rover ↔ Range Rover Sport (MLA-Flex, tier 2); Evoque ↔ Discovery Sport (PTA, tier 2). Velar: former D8 sibling F-Pace is gone → no group. Defender (D7x) vs Discovery (D7u): related but different rows → no group. Sources are the Wikipedia generation articles (fetches failed on budget; relationships are well documented).
- Judgement: Defender 90/110/130/Octa/Hard Top = ONE tile (rule 4). Range Rover sub-brands stay in the Land Rover column (rule 5).

### KGM (KG Mobility) — 7 tiles
- kgm.ch lists 9 price lines: Tivoli, Korando, Torres, Torres EVX, Rexton, Actyon, Musso, Musso Grand, Musso EV. kgm.de adds Torres Hybrid, Torres EVX Cargo Van, Actyon Hybrid.
- Judgement calls: Torres + Torres EVX = one tile (same body shell, BEV fascias) — split if preferred; Musso + Musso Grand = one tile; Musso EV separate (unibody, Torres-EVX-based).
- Musso "new" 2026 (Wikipedia list: Q300) — new generation vs facelift unverified. Lengths for Tivoli (4,225) and Musso EV (~5,190) approximate.
- Twins: Torres ↔ Actyon tier 2 (Actyon "based on the Torres"). Rexton/Musso share frame but different rows.

### Isuzu — 1 tile
- D-Max only. isuzu.ch is JS-only (not readable), isuzu.de is a portal. isuzu.co.uk (2026-10-22): D-Max Utility/DL20/DL40/V-Cross/Arctic Trucks AT35 plus the electric **D-Max eDL40 (£54,995) and eV-Cross (£57,495)** priced on the UK range page → BEV added to the D-Max powertrains (same body, same tile). Isuzu N35 3.5 t light truck not on isuzu.co.uk range page → not included.
- Twin Mazda BT-50 not sold in Europe → no group.

### Ineos — 2 tiles
- CH site: Grenadier Station Wagon, Grenadier Quartermaster (+ Arcane Works Detour edition). Utility Wagon/Commercial = trim of the Station Wagon tile. Fusilier postponed.

### Iveco (Iveco Group) — 1 tile
- Daily/eDaily (van-large). iveco.com Swiss/German product pages return client errors to the fetcher. Ownership: Tata Motors deal announced 30 Jul 2025; defence sold to Leonardo Q1 2026; integration with Tata "expected by the third quarter of 2026" (Il Sole 24 Ore, 17 Jun 2026) — closing not verified; label kept "Iveco Group" per brief (verifier: footnote Tata Motors if closed).

### Renault Trucks (Volvo Group) — 2 tiles
- renault-trucks.ch sells Master (Red Edition, E-Tech, OFFROAD) AND Trafic (Red Edition 2024, E-Tech Trafic). Both tier-1 rebadges: Master ↔ Renault Master ↔ Nissan Interstar; Trafic ↔ Renault Trafic ↔ Nissan Primastar. Whether the "neuer E-Tech Trafic" is the all-new 2026 Renault Trafic E-Tech is unverified.

### Lucid — 2 tiles
- lucidmotors.com/de-de (2026-10-22): Air Pure ab 85.900 €, Touring 99.900 €, Grand Touring 130.900 €, Sapphire 250.000 €; Gravity Touring ab 94.900 € (leasing 949 €/month), Grand Touring; a "Gravity Touring Plus 2027" appears in a comparison link. "Konfigurieren" for both → Air and Gravity on_sale. Gravity CH price CHF 125'900 (InsideEVs, Sep 2025).

### VinFast — 2 tiles
- vinfastauto.eu: VF 6 ("New", order now) and VF 8 ("Available for order"), FR/DE/NL; dealer growth news to Sep 2026; new-gen VF 8 unveiled May 2026. No CH presence → ch_on_sale false. VF 7/VF 9/VF 3 not offered.

### Microlino (Micro Mobility) — 1 tile (Microlino incl. Lite, Spiaggina).

### Ferrari — 6 tiles + Luce announced
- Current (Wikipedia list 2026 + Goodwood 2026): 296 (GTB/GTS/Speciale/Speciale A), 849 Testarossa (+Spider), Amalfi (+Spider), 12Cilindri (+Spider, Manuale), Purosangue, F80 (799, sold out → runout). Luce BEV: reveal planned 25 May 2026, shown at Goodwood → announced.
- ferrari.com blocks fetches (robots) → ch_on_sale true on dealer-network knowledge, flagged.
- Ended: SF90 (Stradale 2024; Spider/XX 2026), Roma (2024; Spider 2026), 812 (2024), Daytona SP3 (2025).

### Aston Martin — 5 tiles
- astonmartin.com/en/models: Vantage (+S, Roadster), DB12 (+S, Volante), Vanquish (+Volante), DBX (GT/S/707), Valhalla, plus limited/sold-out Valkyrie, Valour, Valiant and the track-only Valen (excluded).

### McLaren — 4 tiles (750S, Artura, GTS, W1 runout). mclaren.com is JS-rendered; status from Wikipedia/press — verifier spot-check.

### Morgan — 2 tiles (Plus Four; Supersport incl. Supersport 400). Super 3 excluded (3 wheels). Plus Six ended 2024; Midsummer sold out.

### Caterham — 1 tile (Seven, all variants)
- caterhamcars.com/en/models (2026-10-22): Seven 170, 310 Encore, 360, 420, 420 CUP, 420 Nürburgring Edition, 620, CSR Twenty, Super Seven 600, Super Seven 2000 (+ race packages); Project V only a nav link (concept). European retailer expansion May 2026. Swiss type approvals exist for Seven 170/275/340/485 (swisscarinfo.ch) → ch_on_sale true (importer not verified).

### Bugatti Rimac — Tourbillon (runout, 250 sold out, deliveries 2026), W16 Mistral (runout, ends 2026), Rimac Nevera/Nevera R (on sale).

### Koenigsegg — Jesko, Gemera, CC850 (all sold out → runout). Sadair's Spear noted under Jesko.

### Pagani — Utopia (coupé/roadster, sold out → runout). Huayra specials noted.

## Other non-Chinese brands considered but NOT tiled (verifier decision)
- Aixam / Ligier-Microcar (French L6e/L7e quadricycles, sold in FR/DE/IT/ES/CH) — not researched (time/budget); would add ~6 tiles in `quadricycle`.
- DR Automobiles Groupe (Italy: DR, EVO, Sportequipe, ICH-X, Tiger brands — rebadged Chery/JAC/BAIC/Dongfeng cars, sold in IT/ES) — not researched.
- Piaggio Porter NP6 (N1 light truck, IT), Goupil G4/G6 (Polaris, FR), Fuso Canter 3.5 t (Daimler Truck), Isuzu N35 — 3.5 t-class commercial vehicles outside the car-brand columns.
- Ariel Atom, BAC Mono, KTM X-Bow GT-XR, Donkervoort F22, Dallara Stradale, Gordon Murray T.33/T.50, Praga Bohema, Zenvo Aurora, Hispano Suiza Carmen, Wiesmann Project Thunderball — low-volume sports-car makers on sale in Europe.
- Alpina → BMW sub-brand (BMW Group agent); Fisker gone; Mobilize → Renault; Pininfarina Battista run ended.

## Image notes
- carsized recipe confirmed: `https://www.carsized.com/en-us/cars/compare/<slug>-vs-ford-f/` returns the side image of car 1 (e.g. `/resources/mercedes-benz/g/d-amg-63/2018/sm_327118128_mercedes-benz-g-2018-side-view_4x.png`); `/front/` for the front view. Slug bodies seen: `offroader`, `5-door-hatchback`, `3-door-hatchback`, `5-door-van`.
- Slugs still to be found (search budget). Commons categories given from knowledge; names flagged as "not re-verified" where applicable.

## Open questions for the verifier
1. Jaguar Type 01: unveiled Oct 2026, "commercial introduction" started, deliveries summer 2027, ~£120k — if a DE/UK configurator is live it qualifies as on_sale (currently `announced`).
2. Range Rover Electric / Sport Electric: UK orders open (Sep 2026) but CH pages show reserve/waitlist without prices — decide whether the chart marks the BEV versions as separate "coming" items for CH.
3. Discovery Sport: `runout` (EU factory orders closed, CH configurator still live, production ends Dec 2026).
4. KGM Torres + Torres EVX kept as one tile; Musso + Musso Grand one tile; new 2026 Musso (Q300) generation-vs-facelift unverified; Tivoli/Musso EV lengths approximate (carsized: Musso EV 5,160 mm).
5. Ferrari: whether the standard 296 GTB/GTS is still orderable beside the Speciale (ferrari.com blocks fetches); F80/W1/Tourbillon/Mistral/Jesko/Gemera/CC850/Utopia set to `runout` because sold out (deliveries continue).
6. Iveco Group ownership: Tata Motors integration "expected by Q3 2026" (Il Sole 24 Ore, Jun 2026) — closing not verified; label kept "Iveco Group".
7. Renault Trucks "neuer E-Tech Trafic": whether it is the all-new 2026 Renault Trafic E-Tech (4th gen) or the current Trafic III — affects the twin group only if the Renault agent lists two Trafic generations.
8. ch_on_sale is null for the exotic brands (Aston Martin, McLaren, Morgan, Bugatti, Rimac, Koenigsegg, Pagani) and Lucid Air — official Swiss dealers exist for most, not re-verified.
9. Not tiled (see list above): Aixam/Ligier quadricycles, DR Automobiles (IT), Piaggio Porter NP6, Fuso Canter/Isuzu N35 3.5 t light trucks, low-volume sports-car makers (Ariel, BAC, KTM, Donkervoort, Dallara, GMA, Praga, Zenvo, Hispano Suiza, Wiesmann).
