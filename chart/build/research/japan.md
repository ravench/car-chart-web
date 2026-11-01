# Japan group report — Toyota Motor (Toyota, Lexus), Subaru, Suzuki, Mazda, Honda

## PROGRESS NOTE (final, 2026-10-22)
- japan.json is valid and final for nameplates, status, rows, twins and sources: 57 models (Toyota 21, Lexus 7, Subaru 7, Suzuki 5, Mazda 10, Honda 7), 4 announced (Toyota GR GT, Lexus TZ, Honda 0 SUV, Honda 0 Saloon), 21 discontinued_recently, 70+ sources.
- Image work was STOPPED on the coordinator's instruction (separate pipeline). State of the image fields: 34 models carry a carsized slug + years confirmed from carsized search results; 6 of them also have a verified side-view URL (Lexus RZ, Toyota Proace, Toyota GR Supra, Subaru Solterra, Suzuki Swift, Mazda3); no front views. 13 models are marked "no carsized entry found" in notes (C-HR+, bZ4X Touring, new Hilux, Proace City Verso, Proace Max, new ES, LM, Uncharted, E-Outback, new Across, e Vitara, Mazda2 Hybrid, new CX-5); 10 were never searched (CX-60, CX-80, MX-5, 6e, CX-6e, Civic, ZR-V, CR-V, Prelude, Super-N). Commons categories are best-guess names (not fetched) except those taken from Wikipedia links (Mazda6e, Mazda CX-6e, Honda Prelude, Honda N-One); `commons_file` is null everywhere.
- Helper: `build_japan.py` in this folder regenerates japan.json (`python3 -I build_japan.py`).

## What was checked (sources fetched 2026-10-21/22)
- Official Swiss overviews: de.toyota.ch all-models page with CHF prices (+ Aygo X, RAV4, Hilux-less, GR GT pages), de.lexus.ch (model list, TZ premiere page, ES page), subaru.ch/de/modelle (+ Uncharted page), suzuki.ch/de/auto (+ Across page), de.mazda.ch (JavaScript site: only meta keywords readable), de.honda.ch/cars.html (CHF prices).
- German/UK overviews: toyota.de/neuwagen, toyota.co.uk/new-cars, lexus.de/modelle + ES page, lexus.co.uk, subaru.de (+ e-outback page; /brz not reachable), subaru.co.uk, cars.suzuki.co.uk, mazda.de/modelle (keywords), mazda.co.uk Mazda2 page, honda.de/cars.html, honda.co.uk/cars.html (+ Super-N page).
- 2026 press: Toyota UK press releases on the 6th-gen RAV4 (7 Apr 2026) and the all-new Hilux incl. BEV (13 May 2026); electrive (Lexus TZ May 2026, Honda e:Ny1 Apr 2026, Mazda MX-30 Jan 2026); ecomento (CX-6e orderable Feb 2026); motor1 (Lexus LC dead after MY2026); foro3d (GR86 gone, Jan 2026); t-online (TZ Europe 2027); Fleet World (Mazda2 axed/runout); InsideEVs (Honda 0 Saloon delayed to 2027); Wikipedia articles for lengths/platforms/twins (bZ4X, GR GT, GR Supra, e Vitara, Uncharted, Trailseeker, LBX, ES, EZ-6, EZ-60, Deepal, N-One/Super-N, Prelude, CX-5).

## Nameplate decisions
- Toyota (21): Aygo X, Yaris (incl. GR Yaris), Yaris Cross, Urban Cruiser, Corolla (hatch + Touring Sports + Corolla Commercial), Corolla Cross, C-HR, C-HR+, bZ4X, bZ4X Touring, RAV4 (new gen), Prius (PHEV), Mirai, Land Cruiser (J250, incl. Commercial), Hilux (new gen, diesel 48V + BEV), Proace City, Proace City Verso, Proace, Proace Verso, Proace Max, GR Supra (runout). Announced: GR GT (2027).
- Lexus (7): LBX, UX (300h only), NX, RX, RZ, ES (8th gen), LM. Announced: TZ (Europe 2027). Dropped: LC, RC F, LS, UX 300e.
- Subaru (7): Impreza, Crosstrek, Forester, Outback (runout, 'Letzte Chance'), Solterra, Uncharted, E-Outback. Dropped: BRZ (never launched in Europe), Levorg, XV name.
- Suzuki (5): Swift, Vitara, S-Cross, Across (new RAV4-based gen, continental only), e Vitara. Dropped: Ignis, Swace, Jimny, Swift Sport (all used-only on cars.suzuki.co.uk).
- Mazda (10): Mazda2 Hybrid, Mazda2 (runout — Fleet World: production for Europe stopped, dealer stock only), Mazda3, CX-30, CX-5 (new gen), CX-60, CX-80, MX-5, Mazda 6e, CX-6e. Dropped: MX-30 (BEV and R-EV), Mazda6, CX-3.
- Honda (7): Jazz, Civic (Type R folded in; Swiss listing looks like stock), HR-V, ZR-V, CR-V, Prelude, Super-N (GB only so far). Announced: 0 SUV, 0 Saloon (Europe named at CES 2025, no order date; low confidence). Dropped: e:Ny1 (Apr 2026), Honda e, Civic Type R (Ultimate Edition 2025).

## Judgement calls
- Rows: bZ4X/Solterra (4690 mm) and RZ in d-suv (Toyota calls bZ4X a D-SUV); bZ4X Touring/E-Outback d-suv; RAV4/Across/NX c-suv (brief lists RAV4 and 'NX?' there); Forester (4670) c-suv; new CX-5 (4690) c-suv (Mazda's compact SUV below CX-60); S-Cross (4300) c-suv by Suzuki positioning; ICE Outback d-car because subaru.co.uk classes it as an estate (carsized classes it as SUV — verifier may prefer d-suv next to the E-Outback); Mirai e-car (4975 mm); RX e-suv per brief; LM mpv-large; Super-N a-city (3580 mm).
- GR Yaris folded into the Yaris tile (brief rule: GR = performance version) although it has its own 3-door body.
- Tier 1 groups: Yaris/Mazda2 Hybrid; Urban Cruiser/e Vitara; C-HR+/Uncharted; bZ4X/Solterra; bZ4X Touring/E-Outback; RAV4/Across; Proace City & Proace City Verso & Proace & Proace Verso & Proace Max with their Stellantis siblings (Partner/Berlingo/Combo/Doblò, Rifter/Berlingo/Combo/Doblò, Expert/Jumpy/Vivaro/Scudo, Traveller/SpaceTourer/Zafira/Ulysse, Ducato/Boxer/Jumper/Movano); CX-6e/Deepal S07.
- Tier 2 groups: LBX/Yaris Cross (GA-B); NX/RAV4(+Across) (GA-K); RZ/bZ4X+Solterra (e-TNGA); UX/C-HR/Corolla Cross (GA-C, 2640 mm wheelbase); GR Supra/BMW Z4 (CLAR, Magna Steyr).
- Mixed tiers inside one platform family (bZ4X–Solterra tier 1, RZ tier 2; RAV4–Across tier 1, NX tier 2) are recorded per model; the chart builder must decide how to draw a group with two tiers.
- Mazda 6e: EPA-platform sister of the Deepal L07, but no European L07 sale confirmed, so twin_tier null with a note; add 'Deepal L07' if the Changan agent finds it on sale.
- Powertrain lists follow the brief's MHEV rule (MHEV only where every combustion version is a mild hybrid): Hilux, Impreza, Swift, Mazda3, CX-30, CX-5, CX-80, Mazda2.

## Open questions for the verifier
- Toyota GR Supra: production ended March 2026; still in toyota.de's model filter (1 configuration) in Oct 2026 but not on toyota.ch / toyota.co.uk. Marked runout; confirm whether any importer still takes orders.
- Mazda2: runout confirmed by Fleet World (stock only) — keep as runout or move to discontinued.
- Mazda CX-80 and Mazda 6e: not in the (possibly stale) mazda.ch keyword list — Swiss status null. CX-5: new generation confirmed for Europe (Mazda newsroom 10 Jul 2025) but order status not readable on Mazda's JS-only sites.
- Honda Super-N: on sale in GB (honda.co.uk) only; continental launch unconfirmed. Honda 0 SUV / 0 Saloon: listed as announced on the strength of CES-2025 'including Europe' statements; no European order date — decide whether to show as 'coming'.
- Toyota Highlander: status rests on absence from all three official sites (UK 'previous models'); no 2026 article found.
- Subaru Uncharted / E-Outback / Toyota bZ4X Touring / C-HR+: all confirmed orderable in CH or DE (prices on official pages).
- Lengths unverified from a fetched source: new Hilux (approx. 5.3 m, field null), Super-N 3580 (Wikipedia, Super-One body), Proace Max (L2H2 approx.).
- Images: per coordinator, carsized/Commons lookups are handled elsewhere; see the progress note for what is already filled in (slugs for 34 models, 6 verified side-view URLs).
