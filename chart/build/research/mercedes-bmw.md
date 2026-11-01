# Mercedes-Benz Group + BMW Group — research report

## Progress note (final, 2026-10-22)

- DONE. `mercedes-bmw.json` is valid: 63 model tiles (Mercedes-Benz 26, smart 3, BMW 26, MINI 4, Rolls-Royce 4),
  1 announced (smart #2), 16 discontinued notes, 60 sources. Status split: 61 on_sale, 2 runout (B-Class, EQE).
- Every status has a 2026-dated official configurator page and/or 2026 press source; all former "VERIFY" flags
  were closed in the second session (AMG GT SUV, electric AMG GT 4-Door, X5 G65, iX4, VLE length, i3 length,
  Citan/T-Class/EQV absence on a third market).
- Twin groups: tiers + sources in place (see table below).
- Per the coordinator (2026-10-22) the carsized/Commons image work was STOPPED — a separate pipeline does it.
  What was captured before the stop stays in the JSON: carsized side-view URLs for 15 tiles, the confirmed slug
  convention, and a list of slugs seen but not fetched. `carsized_front` is null everywhere; Commons category
  names are the standard chassis-code names and are NOT verified.
- Generator: `../build/build_mercedes_bmw.py` (edit → re-run → JSON regenerated and validated).

## Method

1. Official model overview pages (fetched 2026-10-21/22): mercedes-benz.ch (cars, vans), mercedes-benz.de (cars,
   vans), mercedes-benz.fr (vans), ch.smart.com (+ #2 page), bmw.ch all-models, mini.ch range,
   rolls-roycemotorcars.com showroom. On mercedes-benz.de the button set per card was used: "Fahrzeug
   konfigurieren" = orderable, only "Verfügbare Fahrzeuge anzeigen" = stock/runout.
2. 2026 press for every new launch or ending model (electrive, newmobility, Electrek, Electrifying, AutoScout24,
   JESMB, mbpassion, Autocar, Carscoops, BMWBlog, Auto123, automobile.at, Motor1.de, TimesLIVE, CompleteCar,
   Hypebeast, auto motor und sport, Autohaus, auto.it, angurten.de).
3. Wikipedia model lists (BMW, Mercedes-Benz) for generation codes and 2025/2026 end years.
4. carsized via WebSearch (slug discovery) + WebFetch (image URLs copied verbatim) — stopped on instruction.

Constraints: WebSearch (200/turn) and WebFetch (400/h) budgets are shared by all agents and ran out several
times; no page was fetched twice. Nothing post-2025 relies on memory.

## Mercedes-Benz — decisions

| Tile | Row | Status | Key evidence |
|---|---|---|---|
| A-Class | c-hatch | on_sale | DE configurator; production moved to Kecskemét, runs to ~2028 (Carscoops 2025-07-21) |
| B-Class | mpv-small | runout | DE: stock search only; not on CH page; phase-out 2026; Wikipedia W247 2019–2026 |
| CLA (C178) | c-hatch | on_sale | BEV + 48 V hybrid orderable (Fleet World), Shooting Brake 2026, AMG 45 (L'argus) |
| GLA | c-suv | on_sale | NEW gen: electric orderable since end-July 2026 (newmobility, JESMB), hybrids early 2027; old H247 ICE still configurable → one tile |
| GLB | c-suv | on_sale | NEW X244 electric on sale (Electrifying 2026-04-06); old X247 petrol still listed |
| C-Class | d-car | on_sale | W206 facelift ("Neu") + electric W520 orderable since May 2026 (AutoScout24) → one tile |
| CLE / E / S / GLC / GLE / GLS / G / AMG GT / SL | — | on_sale | DE/CH configurators; GLC incl. electric X540 (electrive 2025-10-21); G 580 electric in G tile |
| EQE | e-car | runout | DE: stock only; production ends 2026 (Autocar) |
| EQE SUV | e-suv | on_sale | DE configurator; production ends 2026 (Autocar) |
| EQS / EQS SUV (+Maybach) | e-car / e-suv | on_sale | DE/CH listing |
| AMG GT 4-Door Coupé (C590, electric) | e-car | on_sale | orders since premiere 27 May 2026, GT 55 EUR 154,700 / GT 63 EUR 196,350 (Motor1.de) |
| AMG GT SUV (electric) | e-suv | on_sale | revealed 2026-10-19; GT 53 orderable in Europe from 2026-10-20 at EUR 113,050, GT 55/63 spring 2027 (TimesLIVE) |
| VLE | mpv-large | on_sale | DE orders since April 2026 from EUR 82,260 (electrive); 5,309 mm (Autohaus) |
| V-Class (+Marco Polo), Vito Tourer, Vito (+eVito), Sprinter (+eSprinter) | mpv-large / van-mid / van-large | on_sale | DE/CH/FR van pages with prices |
| Citan, T-Class, EQV, EQA, EQB, X290 AMG GT 4-Door, C118 CLA | — | discontinued | `discontinued_recently` (DE/CH/FR listings + press) |

Judgement calls: same-nameplate electric twins (C-Class Electric, GLC Electric, G 580) are inside the ICE tile
(rule 4) with codes in `generation`; new GLA/GLB share one tile with the outgoing ICE generation; Vito Tourer is a
separate mpv-large tile (tier 1 with V-Class) while Sprinter Tourer stays inside Sprinter; Marco Polo is a
V-Class body variant; Maybach versions sit inside their base tiles; AMG GT (C192) and SL (R232) are tier 1
(same MSA platform, doors, interior — coupé vs roadster; verifier may prefer tier 2); AMG GT 4-Door (electric)
in e-car, AMG GT SUV in e-suv.

## smart

- #1 (b-suv, 4,270 mm), #3 (c-suv, 4,400 mm), #5 (d-suv, 4,695 mm): on sale (ch.smart.com; The Driven 2026-09-12).
- #2: Paris premiere Oct 2026, pre-orders since 2026-10-13 (EUR 19,990–25,690, DE/FR/IT), deliveries 2027 →
  `announced` (coming). 2,750–2,790 mm, ECA platform, 35.7 kWh LFP, two seats. Promote to on_sale if a
  pre-order counts as orderable.
- Twins: #1 tier 2 with Volvo EX30 + Zeekr X (SEA; ArenaEV, InsideEVs); #3 tier 2 with Zeekr X + Lynk & Co 02
  (InsideEVs, electrive). Zeekr X (4,432 mm) is named in both rows — verifier picks one row with the Geely agent.
- EQ fortwo ended 2024 → discontinued list.

## BMW — decisions

| Tile | Row | Status | Key evidence |
|---|---|---|---|
| 1 Series, 2 GC, 2 Coupé, 2 AT, 3, 4, 4 GC, 5, 7, X1, X2, X6, X7 | various | on_sale | Wikipedia model list current gens; series in bmw.ch filter bar (ICE cards did not render) |
| i4, i5, i7, iX1, iX2, iX3, iX4, iX5, iX | various | on_sale | bmw.ch electric cards with CHF prices (iX3/iX4/iX5/i7 "Neu") |
| i3 (NA0) | d-car | on_sale | orders since 2026-06-18 DE / June UK, base model end Sept 2026 (Electrek); production Aug 2026 (newmobility); 4,760 mm |
| X3 (G45) | d-suv | on_sale | Wikipedia list; carsized 2024-present |
| X5 (G65) | e-suv | on_sale | debut 2026 (WapCar); DE prices 40d from EUR 95,750, ICE at dealers end Nov 2026, PHEV/iX5 orders from 2026-10-08 (automobile.at); 4,990 mm |
| iX4 | d-suv | on_sale | revealed Oct 2026 (auto.it 2026-10-08); CH configurator live from CHF 76,600; deliveries 2027 (ams) — could be shown as "coming" |
| XM | e-suv | on_sale | MY2026 Label only; production to ~Nov 2028 (Auto123, Yahoo) |
| 8 Series | — | discontinued | production ended Sept 2025 (US to April 2026), no successor (BMWBlog 2025-12-18) |
| Z4 | — | discontinued | production officially ended spring 2026 (Hypebeast 5/2026; Auto123); absent from bmw.ch filter bar; tier-2 twin of Toyota GR Supra (also ended) |
| X4 (G02), iX3 (G08), X5 (G05) | — | discontinued/replaced | Wikipedia list |

Judgement calls: i-models are separate tiles and tier 1 with their same-body ICE siblings (i4/4 GC, i5/5, i7/7,
iX1/X1, iX2/X2, iX5/X5) — drop these intra-brand groups if only cross-brand twins should be coloured; 4 Series
Gran Coupé split from the 2-door 4 Series so it sits in d-car next to the i4; X1/iX1/X2/iX2/Countryman = one
c-suv family (tier 1 inside each BEV/ICE pair, tier 2 across bodies, UKL2/FAAR 2,692 mm wheelbase); 1 Series /
2 GC tier 2 (FAAR); iX3/iX4 tier 2 (Neue Klasse); X3 G45 (CLAR) not grouped with iX3; X5 G65 vs X6 G06 = different
generations → no tier.

## MINI

- Cooper (F66/F65 ICE + J01 electric), Cooper Cabrio (F67, separate tile in `sports` — merge into Cooper if
  preferred), Aceman (J05), Countryman (U25 ICE + electric): all on mini.ch (2026-10-21).
- Electric Cooper/Aceman are built by Spotlight (BMW–GWM JV); no GWM twin claimed (no source says the body is
  shared with an Ora/GWM model).
- Countryman: tier 2 with BMW X1/iX1/X2/iX2 (BMWBlog 2023-11-10, bimmertoday).

## Rolls-Royce

- Phantom (Series II 2022), Ghost (Series II 2024), Cullinan (Series II 2024), Spectre (Series II announced
  2026-06-02): all in the showroom. No twins (Architecture of Luxury = "same scalable architecture", excluded).
  ch_on_sale null (global site; Swiss dealers not checked). Project Nightingale (coachbuild, 100 cars) not listed.

## Twin groups delivered (for joining with other agents)

| Row | Members (this file) | External members named | Tier | Source type |
|---|---|---|---|---|
| sports | Mercedes-Benz AMG GT, SL | — | 1 | Wikipedia (MSA) |
| mpv-large | Mercedes-Benz V-Class, Vito Tourer | — | 1 | Wikipedia (W447) |
| b-suv | smart #1 | Volvo EX30, Zeekr X | 2 | ArenaEV, InsideEVs |
| c-suv | smart #3 | Zeekr X, Lynk & Co 02 | 2 | InsideEVs, electrive |
| c-hatch | BMW 1 Series, 2 Series Gran Coupé | — | 2 | Wikipedia (FAAR) |
| d-car | BMW 4 Series Gran Coupé, i4 | — | 1 | Wikipedia |
| e-car | BMW 5 Series, i5; BMW 7 Series, i7 | — | 1 | Wikipedia |
| c-suv | BMW X1, iX1, X2, iX2, MINI Countryman | — | 1 (BEV/ICE pairs) / 2 (across bodies) | BMWBlog, bimmertoday, Wikipedia |
| d-suv | BMW iX3, iX4 | — | 2 | bmw.ch, ams |
| e-suv | BMW X5, iX5 | — | 1 | WapCar, automobile.at |
| (discontinued) | Mercedes-Benz Citan / T-Class | Renault Kangoo, Nissan Townstar | 1 | newmobility, t-online |
| (discontinued) | BMW Z4 | Toyota GR Supra | 2 | Auto123, Hagerty, Hypebeast |

## Open questions for the verifier

1. Row placement of Zeekr X (b-suv with smart #1/EX30 or c-suv with smart #3/Lynk & Co 02) — must match the Geely agent.
2. Whether intra-brand BEV/ICE pairs (i5/5 Series etc.) and same-brand platform pairs (AMG GT/SL, V-Class/Vito
   Tourer, 1 Series/2 GC) should be coloured as groups or only cross-brand twins.
3. Separate tiles that could be merged: Vito Tourer (into Vito), 4 Series Gran Coupé (into 4 Series or i4),
   MINI Cooper Cabrio (into Cooper).
4. "Coming" vs "on sale" for models with live configurators but deliveries in 2027: iX4, iX5, AMG GT SUV (GT 53
   orderable now), smart #2 (pre-order only → kept as announced).
5. Runout checks not done in every market: B-Class, EQE (DE stock-only), 8 Series and Z4 (nameplates still in
   the bmw.ch filter bar), EQS SUV button mapping on mercedes-benz.de.
6. Lengths still null: AMG GT 4-Door (C590), AMG GT SUV, iX4.
7. Images: carsized side views exist for 15 tiles (A-Class 2018 entry, C, E, S, GLC, GLE 2019 entry, GLS 2019
   entry, GLA 2020 entry, GLB 2019 entry, EQE, CLE, Cullinan 2018 entry, BMW X3, X1, smart #1); facelift/
   Series II entries and all other tiles are for the image pipeline. Slugs seen but not fetched are in `notes`
   (e.g. `rolls-royce-ghost-2020-sedan`, `smart-5-2024-suv-brabus`, `mercedes-benz-sl-2022-roadster-amg-63`,
   `bmw-2-2023-coupe-m2`). Blank on carsized: `mercedes-benz-g-2024-suv`, `mercedes-benz-eqs-2021-sedan`,
   `mini-countryman-2024-suv`. New-2026 models (GLA, GLB X244, VLE, C590, AMG GT SUV, iX4, X5 G65/iX5, i3,
   smart #2) are probably not on carsized yet → Commons fallback.
