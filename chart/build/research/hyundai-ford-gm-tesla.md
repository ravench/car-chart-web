# Hyundai Motor Group / Ford / General Motors / Tesla — research notes

## PROGRESS (final, 2026-10-22)
- DONE: nameplate + status pass for all 7 brands (59 models: 56 on_sale, 3 runout; 1 announced; 21 discontinued entries);
  twin pass with fetched sources (14 same-row groups: 5 × tier 1 Ford/VW, 9 × tier 2); JSON validated.
- STOPPED on coordinator instruction: carsized image lookups and Commons verification (a separate pipeline will do them).
  carsized_* fields are null except Hyundai i10 (confirmed entry hyundai-i10-2019-5-door-hatchback, 2019-2023, side view
  https://www.carsized.com/resources/hyundai/i10/h5/2019/sl_251098072_hyundai-i10-2019-side-view_4x.png).
  Convention learned from carsized's trending page for the image pipeline: slugs are `make-model-year-body` with body = `suv`,
  `minivan`, `van-l2`, `coupe`, `5-door-hatchback`, pickups vary (`4-door-pickup`, `pickup-crew-cab…`); facelifts have their own
  year entries (tesla-model-y-2025-suv, skoda-enyaq-iv-2025-suv, kia-ev3-2024-suv, hyundai-ioniq-5-2021-suv, volkswagen-id4-2020-suv).
  Guessed slugs with "5-door-suv"/"4-door-sedan"/"2-door-coupe" return empty templates. The sitemaps are gzipped (unreadable via WebFetch).
- commons_category values are from memory except Category:Kia PV5 and Category:Ford Transit Connect (verified via Wikipedia links)
  and Category:Volkswagen T7 Transporter (for the VW twin). commons_file is null everywhere.
- Lengths/platforms verified from Wikipedia this session: Ioniq 3 (4,155–4,170 mm), Staria (5,255 mm, N3), PV5 (4,695/4,890 mm),
  Lyriq (4,996 / wb 3,094), Vistiq (5,222 / wb 3,094), G70 (4,685, M2), Ranger (5,225–5,370), Tourneo Connect (4,500/4,859),
  Ioniq 6 (4,855). Others are from memory and flagged "verify" in `notes`.

## What was checked (official overview pages)
- hyundai.com/ch/de/modelle.html (24 entries) and hyundai.com/de/de/modelle.html (leasing-example list incl. Nexo, Ioniq 3, Staria
  Elektro/Cargo Elektro); hyundai.ch i10, i20, i30, new-staria-hybrid pages; hyundai.com/uk i10 page.
- kia.ch (26 entries incl. K4 (+Sportswagon), Seltos, EV2, EV5, PV5 Cargo/Passenger/Crew/Chassis Cab) and kia.com/de navigation
  (no Ceed/ProCeed; "Niro Hybrid" only; PV5 WAV); kia.ch new-niro page.
- genesis.com/ch (Electrified GV70, GV60 + Magma, Electrified G80, G90; GV90 "Demnächst"), genesis.com/de (adds GV70, GV80, G70,
  G70 Shooting Brake, G80, G90) and the DE model pages for GV80, G70, G80, G90; electrive 2026-06-16 (European expansion).
- de.ford.ch, ford.de, ford.de/fahrzeuge, ford.de/fahrzeuge/ford-bronco, ford.co.uk (+ cars, cars/mustang, cars/tourneo-connect,
  cars/tourneo-courier, vans-and-pickups/transit-connect, /transit-courier, /transit-city); Ford Authority (Transit City, Bronco,
  Mustang GTD via AutoGuide), Motor1 DE (Focus). Ford Swiss model pages are JavaScript-only / return errors.
- cadillaceurope.com (markets FR, DE, IE, SE, CH, rest of Europe), ch-de and de-de pages (Optiq, Lyriq, Lyriq-V, Vistiq; no Escalade IQ).
- chevroleteurope.com eu-en and de-de Corvette pages (Stingray €106,900 / E-Ray €169,900 / Z06 €209,900; dealers; regions DE/EU/UK only);
  GM Authority (UK RHD launch July 2026).
- tesla.com/de_ch (Model 3 / Model Y offers for orders to 2026-12-31); Electrek 2026-04-01 (Model S/X production over, zero EU stock);
  Drive Tesla Canada / speedme.ru (Model Y L not orderable in Europe as of Aug 2026).
- Wikipedia: E-GMP, Hyundai-Kia platform page (K1/K2/K3), MEB, Transit Custom, Transporter (T7), Ranger (T6), Tourneo Connect,
  Transit City, Lyriq, Vistiq, i10, i20, Picanto, Seltos, Ioniq 3, Ioniq 6, Nexo, PV5, Staria, G70, GV90, Kia Ceed, Genesis Motor.

## Model counts
Hyundai 15 (i10 runout, i20, Bayon, Inster, Kona, Tucson, Santa Fe, Ioniq 3, Ioniq 5, Ioniq 6, Ioniq 9, i30, Staria, Staria Cargo, Nexo)
Kia 16 (Picanto, Stonic, XCeed, K4, Niro, Seltos, Sportage, Sorento, EV2, EV3, EV4, EV5, EV6, EV9, PV5 Passenger, PV5 Cargo)
Genesis 6 (GV60, GV70, GV80 runout, G70 runout, G80, G90) + GV90 announced
Ford 16 (Puma, Kuga, Explorer, Capri, Mustang Mach-E, Mustang, Bronco, Tourneo Courier, Transit Courier, Tourneo Connect,
  Transit Connect, Tourneo Custom, Transit Custom, Transit, Transit City, Ranger)
Cadillac 3 (Optiq, Lyriq, Vistiq); Chevrolet 1 (Corvette); Tesla 2 (Model 3, Model Y)

## Key 2026 status findings
- Hyundai Ioniq 3: orders open DE 2026-09-02 (€28,950), NL 2026-07-31; on hyundai.ch. Nexo II: on sale DE since Jan 2026 (€69,900),
  NOT on hyundai.ch. i10: European production ended Jan 2026 → runout (still listed CH/UK). i30: CHF 31,700, configurator live.
  Staria: 2026 facelift, Hybrid (CHF 55,000) + Electric (84 kWh); diesel no longer shown in CH/DE.
- Kia: Ceed hatch/SW ended Jan 2026, ProCeed Dec 2024 → K4 / K4 Sportswagon on sale 2026 (Mexico-built). Seltos new to Europe
  (DE from €34,190, deliveries from June 2026; hybrid end 2026). EV2 orders open DE 2026-03-17 (€26,600). EV5 since Sept 2025.
  PV5 Passenger + Cargo on sale (EU sales from Nov 2025; L1H1/L2H2 added spring 2026; Crew, Chassis Cab, WAV). XCeed second
  facelift (production from 2026-05-29; not sold in France). Niro facelift is hybrid-only (EV/PHEV dropped).
- Genesis: DE, CH, UK since 2021; FR, IT, NL added Feb–Mar 2026 (BEV-only line-ups there), ES Q4 2026, AT/DK/PL/PT 2027.
  CH: GV60, Electrified GV70, Electrified G80, G90 (consultation). DE: also ICE GV70, GV80, G70 (+SB), G80, G90 — GV80 and G70 pages
  point to stock/used cars only (→ runout), petrol G80 and G90 have configurator links. GV90 "coming" (unveiled 2026-08-19).
- Ford: Focus ended 2025-11-14 (excluded). Bronco on ford.de (Outer Banks/Badlands, 2.7 V6, leasing ab €569) — limited volumes.
  Mustang GT orderable UK (£58,670); GTD European order window 2026-09-14 → 10-16 (500 units). Transit City (JMC-built EV van,
  56 kWh LFP): order banks open since May/Aug 2026, UK from £24,000 excl. VAT, deliveries from Dec 2026. Transit/Tourneo Connect
  (Caddy twins) and Courier range confirmed current with UK prices.
- GM: Cadillac Optiq/Lyriq/Vistiq on sale CH + DE (+FR, IE, SE); Escalade IQ not offered. Corvette: dealers in DE/EU, UK RHD since
  July 2026; no Swiss site (ch_on_sale null).
- Tesla: Model S/X production ended (Musk 2026-04-01), zero EU inventory → excluded. Model Y L: EU type-approved, in configurator
  code, not orderable as of 2026-08-19 (same tile anyway). Cybertruck never offered.

## Twin groups (all members in one row)
tier 1: Tourneo Connect = VW Caddy (mpv-small); Transit Connect = VW Caddy Cargo (van-small); Tourneo Custom = VW Caravelle
(mpv-large); Transit Custom = VW Transporter (van-mid); Ranger = VW Amarok (pickup).
tier 2: i10/Picanto (a-city); Bayon/Stonic (b-suv); Ioniq 5/EV6/GV60 (c-suv, E-GMP); Explorer/Capri + ID.4/ID.5/Enyaq/Q4 e-tron/
Tavascan (c-suv, MEB); Kona/Niro/Seltos (c-suv, K3); Tucson/Sportage (c-suv, N3); Santa Fe/Sorento (d-suv, N3); Ioniq 9/EV9 (e-suv,
E-GMP); Lyriq/Vistiq (e-suv, BEV3, identical 3,094 mm wheelbase).
Dropped after checking: EV3/EV5 (Wikipedia: 400 V cars on K3-/N3-derived chassis, not one platform); Ioniq 3/EV4 (wheelbase 2,680 vs
2,820 mm, different packs). Cross-row sharing noted in `twin_note` (Ioniq 6 with the E-GMP trio; EV2/EV3 with Ioniq 3; K4 with the K3
group; i30/XCeed; Puma/Courier; Bronco/Ranger; Optiq with Lyriq/Vistiq).

## Judgement calls
- E-GMP trio Ioniq 5 / EV6 / GV60 all in c-suv (EV6 4,695 mm is the borderline one; GV60 4,515 and Ioniq 5 4,655 are clearly C).
- Ioniq 3 (4,155–4,170 mm) placed in c-hatch by Hyundai's compact positioning and 2,680 mm wheelbase, although by length it is
  borderline b-hatch.
- XCeed in c-suv (Kia positions it as a crossover; 4,395 mm). Nexo in d-suv by length (4,750 mm, from memory).
- Staria / Staria Cargo and PV5 Passenger / PV5 Cargo split into mpv-large / van-mid tiles as in the brief's row examples.
- Same-brand platform pairs Lyriq/Vistiq kept as tier 2; verifier may drop. Bayon/Stonic kept as tier 2 (same K1/K2-P2 platform,
  wheelbase and 1.0 T-GDi 48V).
- Transit City row = van-small provisionally (length unknown; 6.4/8.5 m³, payload 1,085–1,275 kg).
- Focus excluded (last built 2025-11-14) rather than "runout"; i10, GV80, G70 marked runout.
- Puma powertrains = MHEV + BEV (all petrol Pumas are 48V mild hybrids); Transit = diesel + MHEV + BEV.

## Open questions for the verifier
- Transit City overall length (not published in fetched sources) → row van-small vs van-mid.
- Swiss availability of Ford Mustang, Bronco, Tourneo/Transit Courier, Tourneo/Transit Connect, Tourneo Custom, Transit City
  (de.ford.ch model pages unreadable) and of the Corvette (no Swiss Chevrolet site).
- Genesis petrol GV70 orderability in DE (page not fetched); whether GV80/G70 "runout" reading of the DE pages is right.
- Hyundai i10 runout: whether CH/UK stock is still orderable in late 2026 (production ended Jan 2026).
- Lengths flagged "verify" in notes (Nexo 4,750; Puma 4,214; Bronco 4,811; Sportage 4,540; K4 Sportswagon; Ioniq 6 facelift).
- Commons category names (from memory) — to be checked by the image pipeline.
- Kia PV7 (E-GMP.S, 2026 per Wikipedia) was not added: not on kia.ch / kia.com/de in Oct 2026; Hyundai "Ioniq V" likewise (Korea).
