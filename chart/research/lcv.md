# LCV cross-brand research — report (final, 2026-10-22, run 3)

## Progress note (top)

STATUS: FINISHED for priorities 1 and 2. `lcv.json` is valid JSON (checked with `python3 -I`), 92 model tiles +
7 announced + 20 recently discontinued entries + 62 sources. Every tile has a 2026 status source except the items
listed under "Still unverified" (they carry the word VERIFY in `status_note`/`notes`). Every tier-1 twin group has
at least one source. Priorities 3 and 4 (carsized image URLs, Commons categories) were STOPPED on the coordinator's
instruction (separate image pipeline): only Renault Kangoo has a confirmed carsized slug/URL, all other
`carsized_*` fields are null and `commons_category` values are best-guess names, not verified.

Files: `build_lcv.py` (generator, single source of truth) -> `lcv.json`; re-run with `python3 -I build_lcv.py`.
`patch2.py` is the applied run-2 patch (kept for traceability, not needed again).
Web access during the work: WebSearch was unavailable (shared 200/turn budget exhausted from the start);
all verification used WebFetch on official pages and Wikipedia, with a final allowance of 25 calls (all used).
Blocked/robots sites (not fetchable): mercedes-benz-vans.ch, vw-nutzfahrzeuge.ch, ford.ch, fiatprofessional.com/ch,
toyota.ch/professional, hyundai.ch, isuzu.ch, iveco.com, man.eu, kgm-motors.ch, saicmaxus.eu, farizonauto.eu;
DE/UK/IT official pages were used instead where they exist.

## Scope and method

Rows covered (authoritative): van-small, van-mid, van-large (<= 3.5 t incl. chassis cabs), pickup, and the
van-derived entries of mpv-small and mpv-large. Switzerland names (Jumpy/Jumper, Opel, Fiat Professional = Fiat).
Method: official CH page where fetchable (renault.ch vans, nissan.ch, opel.ch, citroen.ch, peugeot.ch business
offers, fiat.ch Professional + Qubo L, kia.ch), otherwise DE/UK/IT official pages (volkswagen-nutzfahrzeuge.de,
ford.de, hyundai.com/de, fiat.it, toyota.co.uk, kgm-motors.co.uk, saicmaxus.co.uk, levc.com, ineosgrenadier.com/en/gb,
renault-trucks.com) and Wikipedia model articles (fetched 2026-10-21/22) for generations, twins and
discontinuations. `checked_on` = 2026-10-21 (statuses re-checked 2026-10-22 where noted in `status_note`).

Status rules applied: on_sale = configurable/priced on a 2026 official page; runout = official 2026 end-of-sales
announcement or successor already on sale while the old model is still listed (Citan, T-Class, EQT, EQV, KGM Musso
Q200); announced = revealed with its own official page but not orderable (Trafic E-Tech, Estafette E-Tech,
Goelette E-Tech, Renault Trucks E-Tech Trafic, Ford Transit City, Kia PV7, LEVC L380).

## Tile counts

| row       | on_sale/runout tiles | announced | notes |
|-----------|---------------------:|----------:|-------|
| van-small | 13 | 0 | Kangoo Van, Townstar, Citan (runout), Caddy Cargo, Transit Courier, Transit Connect, Partner, Berlingo Van, Combo Cargo, Doblò Cargo, Proace City, Maxus eDeliver 3, Piaggio Porter NP6 |
| mpv-small | 12 | 0 | Kangoo, Townstar Kombi, T-Class (runout), EQT (runout), Caddy, Tourneo Courier, Tourneo Connect, Rifter, Berlingo, Combo, Qubo, Proace City Verso |
| van-mid   | 19 | 5 | Trafic, Renault Trucks Trafic, Primastar, Vito, Transporter, ID. Buzz Cargo, Transit Custom, Expert, Jumpy, Vivaro, Scudo, Proace, Staria Van, PV5 Cargo, Maxus eDeliver 5, Maxus eDeliver 7 (+Deliver 7), Farizon SV, LEVC VN5, Iveco eJolly; announced: Trafic E-Tech, Estafette E-Tech, Goelette E-Tech, Renault Trucks E-Tech Trafic, Ford Transit City |
| mpv-large | 21 | 1 | Trafic Passenger, Primastar Kombi, Vito Tourer, V-Class, EQV (runout), Marco Polo (optional camper), VLE, Caravelle, Multivan, California (optional camper), ID. Buzz, Tourneo Custom, Traveller, SpaceTourer, Zafira, Ulysse, Proace Verso, Staria, PV5 Passenger, Mifa 7, Mifa 9; announced: LEVC L380 |
| van-large | 16 | 1 | Master, Renault Trucks Master, Interstar, Sprinter, Crafter, Grand California (optional camper), MAN TGE, Transit, Boxer, Jumper, Movano, Ducato, Proace Max, Maxus eDeliver 9 (+Deliver 9), Iveco Daily, Iveco eSuperJolly; announced: Kia PV7 |
| pickup    | 11 | 0 | Amarok, Ranger, Hilux (gen IX), L200, D-Max, KGM Musso (runout), KGM Musso Rhino, KGM Musso EV, Ineos Quartermaster, Maxus T60 Max, Maxus eTerron 9 |
| total     | 92 | 7 | status: on_sale 87, runout 5 |

Powertrain coverage is in `powertrains`; FCEV was removed everywhere (Stellantis ended its hydrogen programme in 2025,
Hyvia liquidated 2025). ch_on_sale: true 30, false 1 (LEVC VN5), null 61 (brand's CH site not fetchable; see below).

## Twin groups (tier 1 = same body shell / rebadge; groups never cross rows)

Canonical twin names follow the brief: "Brand Model", Opel as "Opel/Vauxhall Model" (same convention as
stellantis.json and japan.json); the Opel tiles themselves carry brand "Opel". All `twin_members` resolve to tiles in
lcv.json (checked), and the passenger versions form separate groups in the mpv rows.

1. van-small — Renault Kangoo Van / Mercedes-Benz Citan / Nissan Townstar (all built by Renault, Maubeuge).
   Sources: Wikipedia Renault_Kangoo, Mercedes-Benz_Citan, Nissan_Townstar.
2. mpv-small — Renault Kangoo / Mercedes-Benz T-Class / Mercedes-Benz EQT / Nissan Townstar Kombi. Same sources.
3. van-mid — Renault Trafic / Nissan Primastar / Renault Trucks Trafic (Sandouville). Sources: Wikipedia Renault_Trafic,
   Nissan_Primastar; renault-trucks.com press release (E-Tech Trafic, 15 Sep 2026, confirms the Red Edition range).
4. mpv-large — Renault Trafic Passenger / Nissan Primastar Kombi. Sources as 3.
5. van-large — Renault Master / Nissan Interstar / Renault Trucks Master (Batilly). Sources: Wikipedia Renault_Master,
   Nissan_Interstar.
6. mpv-large — Mercedes-Benz V-Class / Vito Tourer / EQV / Marco Polo (W447). Sources: Wikipedia Mercedes-Benz_Vito,
   Mercedes-Benz_V-Class. (The Vito panel van is the same shell but sits in van-mid, so it is untwinned by rule.)
7. van-small — Volkswagen Caddy Cargo / Ford Transit Connect (Poznań). Sources: Wikipedia Ford_Transit_Connect,
   Volkswagen_Caddy.
8. mpv-small — Volkswagen Caddy / Ford Tourneo Connect. Same sources.
9. van-mid — Ford Transit Custom / Volkswagen Transporter (T7, Ford Otosan Kocaeli). Sources: Wikipedia
   Ford_Transit_Custom, Volkswagen_Transporter_(T7).
10. mpv-large — Ford Tourneo Custom / Volkswagen Caravelle. Same sources.
11. mpv-large — Volkswagen Multivan / Volkswagen California (MQB T7; not related to the Ford-based Caravelle).
    Source: Wikipedia Volkswagen_Multivan_(T7).
12. van-large — Volkswagen Crafter / MAN TGE / Volkswagen Grand California (Września). Sources: Wikipedia
    Volkswagen_Crafter, MAN_TGE.
13. pickup — Ford Ranger / Volkswagen Amarok (Silverton). Sources: Wikipedia Volkswagen_Amarok, Ford_Ranger_(T6).
14. van-small (K9) — Peugeot Partner / Citroën Berlingo Van / Opel/Vauxhall Combo Cargo / Fiat Doblò Cargo /
    Toyota Proace City. Sources: Wikipedia Citroën_Berlingo, Toyota_ProAce_City, Fiat_Doblò.
15. mpv-small (K9) — Peugeot Rifter / Citroën Berlingo / Opel/Vauxhall Combo / Fiat Qubo (2026) / Toyota Proace City
    Verso. Same sources (Berlingo article lists "Fiat Qubo, 2026–present").
16. van-mid (K0) — Peugeot Expert / Citroën Jumpy / Opel/Vauxhall Vivaro / Fiat Scudo / Toyota Proace / Iveco eJolly.
    Sources: Wikipedia Citroën_Jumpy, Toyota_ProAce, Fiat_Scudo.
17. mpv-large (K0) — Peugeot Traveller / Citroën SpaceTourer / Opel/Vauxhall Zafira / Fiat Ulysse / Toyota Proace Verso.
    Same sources.
18. van-large (Sevel Sud) — Peugeot Boxer / Citroën Jumper / Opel/Vauxhall Movano / Fiat Ducato / Toyota Proace Max /
    Iveco eSuperJolly. Sources: Wikipedia Fiat_Ducato, Toyota_ProAce_Max, Opel_Movano.
19. van-mid (announced) — Renault Trafic E-Tech / Renault Trucks E-Tech Trafic (gen IV, Flexis skateboard, 2027).
    Sources: renault-trucks.com press release; Wikipedia Renault_Estafette.
Tier 2 (platform siblings): van-mid — Renault Trafic E-Tech / Estafette E-Tech / Goelette E-Tech (same skateboard,
different bodies). Source: Wikipedia Renault_Estafette.

Untwinned tiles (no same-row twin in Europe): Transit Courier, Tourneo Courier, Maxus eDeliver 3, Piaggio Porter NP6,
Vito, ID. Buzz Cargo, Staria Van, Kia PV5 Cargo, Maxus eDeliver 5, Maxus eDeliver 7, Farizon SV, LEVC VN5, VLE,
ID. Buzz, Staria, PV5 Passenger, Mifa 7, Mifa 9, Sprinter, Transit, Maxus eDeliver 9, Iveco Daily, Hilux, L200,
D-Max, KGM Musso / Musso Rhino / Musso EV (three different bodies), Ineos Quartermaster, Maxus T60 Max, eTerron 9,
Ford Transit City, Kia PV7, LEVC L380. Rejected twin candidates: Mitsubishi L200 / Nissan Navara (Navara left Europe
2021), Isuzu D-Max / Mazda BT-50 (BT-50 not sold in Europe), Hyundai Staria / Kia Carnival (Carnival not sold in Europe),
Maxus eTerron 9 / MG U9 (not in Europe), KGM Musso EV / Torres EVX (different row).

## Judgement calls

- Panel-van and passenger versions are separate tiles even when the nameplate is shared (Kangoo / Kangoo Van,
  Berlingo / Berlingo Van, Doblò Cargo / Qubo, Caddy / Caddy Cargo, Vito / Vito Tourer, Trafic / Trafic Passenger,
  Primastar / Primastar Kombi, Townstar / Townstar Kombi, Staria / Staria Van, PV5 Cargo / PV5 Passenger,
  ID. Buzz / ID. Buzz Cargo, Combo Cargo / Combo, Transporter / Caravelle). The suffixes "Kombi"/"Passenger" are my
  disambiguation for twin matching, not official CH names (official names are in `display`/`other_names`).
- Mercedes T-Class and EQT, V-Class and EQV are separate tiles (different nameplates); all marked runout per
  Wikipedia/Mercedes 2026 discontinuation (Citan/T-Class/EQT production end 2026; VLE in production since June 2026
  as EQV successor). The diesel V-Class is assumed to continue (VERIFY).
- Factory campers (VW California, Grand California, Mercedes Marco Polo) are included as OPTIONAL tiles flagged
  "FACTORY CAMPER — optional" in `notes`; drop them if the chart should not show campers.
- Fiat Qubo (2026, K9-based, "Qubo L" in CH/IT) replaces the passenger Doblò; passenger Doblò 2022–2025 is in
  `discontinued_recently`. Length 4753 mm = long K9 body (only the L is listed in CH/IT).
- Renault Trafic E-Tech (gen IV, Flexis) is a separate announced tile, not a powertrain of the Trafic III tile; the
  gen-III Trafic Van E-Tech (52 kWh) is listed as discontinued. Goelette E-Tech (chassis cab) is placed in van-mid with
  its siblings although chassis-cab bodies suit van-large; move if the chart prefers.
- Ford Transit City placed in van-mid as announced (ford.de pre-launch page: 56 kWh LFP, 110 kW, SWB/MWB/chassis,
  "Angebot anfragen" only). Length not published; row provisional (8 m³ MWB is at the mid/large boundary).
- Maxus Deliver 7/9 (diesel) and eDeliver 7/9 (electric) share a body: one tile each, named after the electric
  version (`display` shows both).
- Farizon SV kept in van-mid (L1 4.99 m) although the L3 (6.0 m) is large-van sized.
- KGM Musso (Q200) = runout and all-new Musso Rhino (Q300) = on_sale, both from kgm-motors.co.uk (Oct 2026); could be
  merged into one tile once the Q200 is gone. Musso EV is a separate body (Torres EVX-based).
- Iveco eJolly / eSuperJolly (2025 Stellantis rebadges) tiled under Iveco (group label: Iveco is not in the brief's
  brand table; I used group "Iveco Group" — the merger may want to place the Iveco column elsewhere).
- Renault Trucks tiles (Trafic, Master, E-Tech Trafic) use brand "Renault Trucks" with group "Volvo Group" (its
  actual owner) — flag for the column layout: they are pure rebadges of Renault vans and are best shown next to
  Renault, or folded into the Renault tiles as other names.
- Group labels used for brands missing from the brief's table: "Iveco Group" (Iveco), "Volvo Group" (Renault Trucks),
  "Piaggio Group" (Piaggio), "Isuzu" (Isuzu), "Ineos" (Ineos); all other brands use the table's labels (Maxus = SAIC
  Motor, Farizon/LEVC = Geely Holding, KGM = KG Mobility, Mitsubishi = Mitsubishi Motors).
- Piaggio Porter NP6 (1.1–1.4 m wide, 3.5 t GVW versions exist) kept as a van-small tile; the Porter NP6 is a
  chassis-cab/pickup microvan — drop if the chart wants only "car-like" vehicles.
- Not tiled (body variants of other agents' passenger tiles): Toyota Land Cruiser Commercial, Corolla Commercial,
  Citroën ë-C3 Van, Fiat Pandina Van, Dacia Spring Cargo, Dacia Duster Commercial, Land Rover Defender Hard Top,
  Mitsubishi Outlander commercial (UK). Not tiled (fringe / not car-like / outside brand table): Goupil G4/G6,
  Evum aCar, Fuso Canter (3.5 t), Isuzu Grafter/N35, ICH-X K4, Foton Tunland, DFSK/Seres vans, Aixam/Ligier/Mobilize
  Bento/Citroën Ami Cargo (quadricycle row, other agent).

## Still unverified (VERIFY flags in lcv.json, 23 mentions)

Status-level (one source each still wanted):
- Mercedes-Benz V-Class (diesel continuation into 2027 alongside VLE), EQV (orders still open?), Vito Tourer and
  Marco Polo (2026 listing), VLE (order opening date; treated as on_sale from June 2026 production start) —
  mercedes-benz-vans.ch / .de blocked.
- Toyota Hilux gen IX: on sale per toyota.co.uk (diesel + BEV); CH/DE listing and exact length (5320 mm assumed from
  gen VIII) unverified.
- KGM Musso EV and Musso Rhino: UK only verified; names/availability in CH/DE unverified.
- Maxus T60 Max and eTerron 9: UK only verified; eTerron 9 is the electric twin of the Interstellar X / MG U9 (not
  sold in Europe as far as checked).
- Iveco Daily (CH listing; iveco.com global page shows no products), Iveco eJolly / eSuperJolly (market coverage).
- MAN TGE: new eTGE (e-Crafter basis) availability 2025/26.
- Renault Master H2-Tech: dropped after Hyvia's 2025 liquidation (assumed).
- Kia PV7 (production/sales 2027?), LEVC L380 (order status; page exists, no price).
- Minor: "VERIFY Commons category name" on Primastar, Interstar, Boxer, Jumper, Scudo, Ulysse, Ducato, Proace,
  Quartermaster — out of scope now (image pipeline).
ch_on_sale = null for 61 tiles: Mercedes-Benz, Volkswagen, MAN, Ford, Toyota (except Hilux UK), Hyundai, Peugeot
Rifter/Traveller (not on the business-offers page), Mitsubishi, Isuzu, KGM, Ineos, Maxus, Farizon, Iveco, Piaggio,
Renault Trucks: the CH site was blocked or not checked; status comes from DE/UK/IT pages. All of these brands do sell
in Switzerland; the null only means "not confirmed on a .ch page".

## Open questions for the verifier (incl. conflicts with other agents' files)

Other agents also tiled LCV rows; where they differ from lcv.json (authoritative for these rows), the differences are:
- hyundai-ford-gm-tesla.json: "Ford Transit City" in van-small / on_sale vs lcv.json van-mid / announced (ford.de
  pre-launch page, 2026-10-22) — decide row and status. "Hyundai Staria Cargo" vs my "Staria Van" (hyundai.com/de
  sells "STARIA Cargo Elektro"; CH name unverified) — pick one name.
- china-other.json: Maxus eDeliver 5 in van-small (mine: van-mid, 4.8 m); separate "Deliver 7"/"Deliver 9" diesel
  tiles (mine: merged into eDeliver 7/9); "Maxus T90 EV" on_sale (mine: discontinued — no longer on saicmaxus.co.uk,
  replaced by eTerron 9; may linger in some EU markets); "BYD Shark" pickup on_sale (mine: not launched in Europe per
  Wikipedia BYD_Shark, fetched 2026-10-22) — needs one official BYD Europe source.
- stellantis.json: "Fiat Doblò" (mine: "Doblò Cargo"), "Fiat Qubo L" (mine: "Qubo"), "Opel Combo Life" (mine:
  "Combo" — opel.ch dropped the Life suffix in 2024; Vauxhall UK still uses it). Twin names in that file use
  "Fiat Qubo L"/"Fiat Doblò"/"Opel/Vauxhall Combo Life", so the merger must map them to my tile names.
- renault-alliance.json: "Renault Trafic Van" (mine: "Trafic"), "Renault Trafic" in mpv-large (mine: "Trafic
  Passenger"), "Nissan Townstar"/"Nissan Primastar" used for both rows (mine: "... Kombi" for the passenger tiles),
  "Renault Estafette"/"Goelette" (mine: "... E-Tech").
- jlr-independents.json: KGM Musso on_sale and no Musso Rhino (mine: Musso runout + Rhino on_sale per kgm-motors.co.uk
  2026-10-22).
- geely.json lists "Farizon V7E" (van-mid) — not in lcv.json; I found no 2026 source for a V7E in Europe (farizonauto.eu
  blocked). Verify whether it is a real European model or a China-only name.
- mercedes-bmw.json has no Citan / T-Class / EQT / EQV / Marco Polo tiles; lcv.json shows them as runout (campers
  optional). Decide whether runout tiles appear on the chart.
- Chart-level: should Renault Trucks (Volvo Group) and Iveco get their own columns or be folded as "other names" of the
  Renault / Stellantis tiles? Should LEVC VN5 (not sold in CH) and Piaggio Porter appear at all?
- Kia PV5 Cargo/Passenger lengths (4695 mm) and PV7 row (van-large assumed from the teaser) to confirm once kia.ch
  publishes specs.
- Hilux gen IX length, Musso Rhino length (5400 mm approximate), Transit City length (unknown) are estimates.

## Discontinued recently (20 entries, for the "no longer on sale" footnote)

Renault Express Van (EU withdrawal 2024), Trafic Van E-Tech gen III (52 kWh), Mercedes Citan/eCitan/T-Class/EQT (2026),
EQV (replaced by VLE), Jeep Gladiator (Europe end-2023), Fiat Fiorino/Qubo (2008 generation), Fiat Doblò passenger
(2022–2025), Maxus T90 EV, Stellantis hydrogen vans (e-Expert/ë-Jumpy/Vivaro Hydrogen, Movano Hydrogen), Fiat Talento,
Nissan e-NV200/NV250/NV300/NV400, Nissan Navara, Peugeot Landtrek, Fiat Titano, Mitsubishi Express, Dacia Dokker,
BYD Shark (not launched in Europe), GWM Poer/Cannon (not launched), JAC T9/Hunter (not launched).
