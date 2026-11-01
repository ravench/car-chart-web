# Renault Group / Nissan / Mitsubishi Motors — research notes (checked 2026-10-21/22)

## PROGRESS NOTE (keep at top)
- DONE: nameplate lists for all 6 brands from the official CH/DE/FR/ES/UK sites (fetched 2026-10-21/22); every status verified with a 2026 page; twins + tiers assigned with sources; JSON valid (44 models, 5 announced, 16 discontinued).
- carsized pass: 26 of 44 tiles have verified side+front URLs (copied verbatim from the compare pages). 18 tiles have none — each has an explicit `notes` entry saying which slugs were tried and which twin's images can be reused (Grandis→Symbioz, Eclipse Cross→Scenic, Townstar Combi/Kangoo Van→Kangoo). No carsized entry exists yet for Dacia Spring II, Striker, Leaf (2025), A390, Grandis, Eclipse Cross BEV, L200 (2026 Europe); the van entries (Kangoo Van, Trafic, Master, Townstar, Primastar, Interstar) could not be located because carsized's panel-van slug pattern is unknown (tried `-van`, `-panel-van`, `-5-door-van`).
- Commons: category names are given from memory and flagged "unverified (budget)" in `notes`; NOT verifiable from this sandbox: every Commons category URL (including `Category:Renault_Master`, which certainly exists) came back `url_not_found` from the fetcher, so Commons appears unreachable here; the earlier 'does not exist' readings for Striker/A390/Townstar were withdrawn and all Commons names stay best guesses flagged in `notes`. The shared web-fetch pool (400/h) ran out three times; the Commons verification pass could not be completed.
- Nothing else open on the status side. Verifier to-do list at the end.

## 1. What was checked (official pages, all fetched 2026-10-21/22)
- Renault: de.renault.ch (home + personenwagen + vans), renault.de/modelle, renault.fr, business.renault.co.uk/van-range, business.renault.ch Trafic E-Tech page, R5 Turbo 3E pages (CH/DE).
- Dacia: de.dacia.ch (+ Striker, Spring pages), dacia.de/modelle (+ neuer Spring), dacia.es.
- Alpine: de.alpinecars.ch (+ A110 Future), alpinecars.fr.
- Mobilize: mobilize.com now redirects to renaultgroup.com (brand wound down); Duo in renault.ch "old models hub"; renault.fr still shows "Mobilize Duo – voir le stock".
- Nissan: de.nissan.ch/fahrzeuge/neuwagen, nissan.de/fahrzeuge/neuwagen (+ Pixo, Ariya, X-Trail pages).
- Mitsubishi: mitsubishi-motors.ch/de/modelle (+ Eclipse Cross BEV, Space Star), mitsubishi-motors.de/modelle (+ Colt, L200), mitsubishi-motors.fr, mitsubishi-motors.co.uk (+ CV Show L200 article).
- Trade press / references: Autocar (final A110; Micra = R5 twin), electrive (Twingo orders, Leaf orders, Pixo, A110 successor, A390 UK), Inovev (Mobilize end; Express end; Korean imports end), Planète Renault (Arkana end), L'argus (Express Van), What Car? (Flexis vans), Motor1 (Space Star end), auto motor und sport (2026 Navara not for Europe), Wikipedia (Dacia Striker, Dacia Spring II, Mitsubishi Colt discontinuation, Renault Twingo).

## 2. Line-up as of October 2026 (status in brackets)
**Renault (17 tiles):** Twingo E-Tech [on sale, orders since Dec 2025] · Renault 5 · Renault 4 · Clio VI [new Sept 2025] · Captur (2024 facelift) · Symbioz · Austral (2025 facelift) · Espace VI (2025 facelift) · Rafale · Mégane E-Tech (2026 facelift "Nouvelle Mégane") · Scenic E-Tech · Kangoo (incl. Grand Kangoo) · Kangoo Van · Trafic (Combi/Passenger/SpaceClass/campers) · Trafic Van (diesel X82) · Trafic E-Tech new generation [ANNOUNCED — listed on CH/UK sites without price/configurator, "stay informed", homologation pending] · Master IV (van, chassis cab, tipper, box; diesel + E-Tech).
Announced: Renault 5 Turbo 3E (reservations open for 1,980 units; DE site: "noch nicht zum Verkauf angeboten"), Estafette E-Tech, Goelette E-Tech (Flexis trio due 2026; none orderable on CH/UK sites as of 2026-10-22).
Discontinued/runout: Arkana (Dec 2025), Express Van (Jul 2024), Clio V (stock), Zoe, Koleos (never in Europe since 2023), X82 Trafic E-Tech Electric (no longer listed).
**Dacia (6):** Spring II [new Sep 2026, Novo Mesto, orders open] · Sandero (+Stepway) · Jogger · Duster III · Bigster · Striker [NEW crossover estate, announced 8 Jul 2026, orders open CH/DE/ES]. Logan: not sold in DE/FR/UK/IT/ES/NL/CH → excluded (note). Spring I: runout on DE/ES sites.
**Alpine (3):** A110 [RUNOUT — last car built Jul 2026, 28,701 made; alpinecars.fr still configures A110/GTS/R 70 from stock] · A290 · A390. Announced: 3rd-gen electric A110 (APP platform, Dieppe from 2027; waiting list).
**Mobilize (1):** Duo [RUNOUT — brand ended Dec 2025, production stopped; stock on renault.fr]. Bento (never really produced) and Limo (cancelled 2023) in discontinued.
**Nissan (11 tiles / 8 nameplates):** Micra (2025, EV) · Juke · Qashqai · X-Trail · Leaf (2025) · Ariya (MY26) · Townstar Combi · Townstar Van · Primastar Combi · Primastar Van · Interstar (2024). Announced: Pixo (Twingo twin, revealed 23 Sep 2026, prices Dec 2026). Not in Europe: Navara (2026 Triton-based, AU/Asia/Africa only), Pathfinder, Z, GT-R.
**Mitsubishi (6):** Colt [RUNOUT — production ended end-2025 with Clio V; DE "Auslaufmodell", still on FR/CH sites] · ASX · Grandis (2025) · Eclipse Cross BEV (2025/26; CH "jetzt kaufen" CHF 40,998) · Outlander PHEV · L200 (6th gen; UK on sale from Mar 2026 with May deliveries, Italy priced, DE "Coming Soon", not CH). Space Star: discontinued early 2025.

## 3. Judgement calls the verifier should look at
Rows:
- Dacia Striker → **c-suv** (Dacia calls it a crossover; 4.62 m, 1.53 m tall estate body; grouped with its platform siblings Duster/Bigster). Alternative: c-hatch (estate).
- Nissan Leaf (2025) → **c-hatch** (4.35 m, 1.55 m; Nissan says "crossover"; grouped with its CMF-EV sibling Mégane E-Tech). Alternative: c-suv.
- Nissan Ariya (4.595 m) and Alpine A390 (4.615 m) → **c-suv** by the brief's length bands; both could be argued into d-suv.
- Dacia Duster III (4.34 m) → c-suv as the brief lists it; Jogger → mpv-small as listed.
- Renault 4 → b-suv (4.14 m crossover; carsized calls it a 5-door hatchback).
- Goelette → van-mid with its Flexis siblings (it is a 3.5 t chassis cab, so van-large is defensible).
- Renault 5 Turbo 3E → separate nameplate, sports row, in `announced` (reservations open but not homologated/priced; deliveries 2027). Could be shown as on_sale.
- Renault Trafic E-Tech (2026 Flexis generation) is listed as its own entry in `announced` because it is a different vehicle sold alongside the diesel Trafic III; the builder may merge both into one "Trafic" tile.
Tiers:
- Tier 1 groups: Twingo/Pixo (Pixo announced); Renault 5/A290/Micra (Micra: shares platform, wheelbase, batteries, motors and dashboard, built on the same Douai line, but Nissan restyled the outer panels — downgrade to tier 2 if "rebadge" is read strictly); Captur/ASX; Symbioz/Grandis; Scenic/Eclipse Cross; Kangoo/Townstar Combi/Mercedes T-Class; Kangoo Van/Townstar Van/Mercedes Citan; Trafic/Primastar/Renault Trucks Trafic (both rows); Master/Interstar/Renault Trucks Master.
- Tier 2 groups: Clio VI/Colt/Sandero (Colt is a tier-1 rebadge of the *previous* Clio V, which is no longer sold new, so against the Clio VI it is only a CMF-B sibling); Captur(+ASX)/Juke; Austral/Qashqai; Espace/Rafale/X-Trail/Outlander (CMF-CD); Mégane E-Tech/Leaf (CMF-EV); Scenic(+Eclipse Cross)/Ariya/A390 (CMF-EV); Duster/Bigster/Striker (CMF-B); Trafic E-Tech/Estafette/Goelette (Flexis).
- Left at null: Dacia Spring II vs Twingo (same RGEV Small platform, same 27.5 kWh/60 kW drivetrain, different body) — tier 2 would be defensible; Renault 4 (its AmpR Small siblings are all in b-hatch/a-city).
- Twin sources: the Renault–Mitsubishi rebadges, Townstar/Primastar/Interstar and Citan/T-Class are cited with official model pages + Wikipedia; no manufacturer press release could be fetched because the search budget ran out. Nissan Navara (2026) is a Triton rebadge but not sold in Europe, so L200 has no European twin.
Tile splits: Kangoo vs Kangoo Van, Trafic vs Trafic Van, Townstar Combi vs Townstar Van, Primastar Combi vs Primastar Van are separate tiles (brief rule 4, Citan/T-Class analogy). Grand Kangoo, Sandero Stepway, Trafic SpaceClass/Escapade/SpaceNomad, Master chassis/tipper/box, L200 Commercial are folded into their nameplate tile.

## 4. Uncertainties / open points
- Commons category names were not verified (fetch budget); the names follow Commons conventions (e.g. "Category:Renault Captur II", "Category:Nissan Qashqai J12") but new-model categories (Twingo IV, R5/R4 E-Tech, Micra K15, Leaf ZE2, Grandis 2025, Eclipse Cross 2025, Spring II, A390, Interstar 2024, Master IV, Triton 2023) may be named differently or not exist. Commons could not be reached from the sandbox fetcher at all (url_not_found even for Category:Renault_Master), so NO Commons name in the JSON is verified; the verifier should check them in a browser. Striker (revealed Jul 2026) and A390 may not have categories yet.
- carsized images for Juke, ASX, Outlander, Mégane E-Tech are the pre-facelift entries of the current generation (no facelift entry exists on carsized); Captur, Qashqai, Austral, Espace use the facelift entries ("Gen. 2.1 / 3.1 / 1.1 / 6.1").
- Mitsubishi L200: on sale in the UK/Italy, DE still "Coming Soon" (Oct 2026), not offered in CH. Mitsubishi UK sells only L200 and Outlander PHEV (no ASX/Colt/Grandis/Eclipse Cross).
- Nissan also distributes the Silence S04 L7e nanocar through its German dealers ("Klein-Elektrofahrzeug S04" on nissan.de). It stays Silence-branded, so it is not a Nissan tile; mention if a "Silence" column is wanted.
- Dacia Logan III is still built/sold in Romania and some Eastern EU markets but not in the six reference markets or CH — excluded under the brief's rule; flag if "EU anywhere" is wanted.
- Mobilize: brand ended Dec 2025. Duo is kept as a runout tile; the builder may drop the column.
- Renault Trucks (Volvo Group) retails Master Red EDITION / E-Tech Master / Trafic Red EDITION / new E-Tech Trafic — named as twin members for the Master and Trafic tiles.
- Lengths are manufacturer figures from memory for established models (Clio VI 4.116 m, Captur 4.239, Symbioz 4.413, Austral 4.51 pre-facelift, Espace 4.722, Rafale 4.71, Scenic 4.47, Kangoo 4.486, Trafic 4.999 L1, Master 5.05 L2, Micra 3.974, Juke 4.21, Qashqai 4.425, X-Trail 4.68, Leaf 4.35, Ariya 4.595, Outlander 4.72, L200 5.32, A110 4.178, A290 3.997, A390 4.615, Duster 4.343, Bigster 4.57, Jogger 4.547, Sandero 4.088); fetched figures: Twingo 3.79, Spring II 3.85, Striker 4.62, Trafic E-Tech 4.87 (L1), R5 3.92.

## 5. Discontinued 2024–2026 (see JSON `discontinued_recently`)
Arkana, Express Van, Clio V (stock), Koleos (import stop), X82 Trafic E-Tech, Spring I, Logan (not in reference markets), A110 (runout), Mobilize Bento/Duo/Limo, Leaf ZE1, Navara, Space Star, Colt (runout), Eclipse Cross PHEV.

## 6. Verifier to-do
1. Spot-check the Commons categories flagged "unverified" (one category page each) and pick `commons_file` images for the 18 tiles without carsized URLs.
2. Decide the Striker row (c-suv vs c-hatch) and the Micra tier (1 vs 2).
3. Decide whether Trafic E-Tech (new gen) merges into the Trafic tile and whether Mobilize keeps a column.
4. Re-check in Nov/Dec 2026: Pixo prices (Dec 2026), Trafic E-Tech/Estafette/Goelette order opening, L200 in DE, R5 Turbo 3E homologation.
