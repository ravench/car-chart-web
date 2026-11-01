# Stellantis group – research report (Europe, as of 2026-10-21/22)

## PROGRESS NOTE (for resume)
- STATUS: research COMPLETE for priorities 1–2 (nameplates, status, Swiss status, twin groups). Image work
  (carsized/Commons) was STOPPED on the coordinator's instruction (handled by a separate pipeline); only 6 side
  images / 13 slugs were captured before the stop (see `carsized_*` fields; everything else is null).
- Data lives in `stellantis_build.py`; run `python3 -I stellantis_build.py` to regenerate `stellantis.json`
  (68 models, 4 announced, 14 discontinued, 44 sources, `twin_groups` helper key).
- Swiss status unknown (null) only for: DS 7 (run-out), Opel Combo Life (passenger Combo), Jeep Wrangler (run-out).
- Web access notes: WebSearch budget (200/turn, shared) and WebFetch budget (400/h, shared) were exhausted several
  times; opel.ch, dsautomobiles.ch, lancia.ch, leapmotor.ch and fiatprofessional.com could not be read (blocked /
  JS-only), so the Swiss Stellantis press rooms (media.stellantis.com/ch-de/<brand>/press) were used instead.

## Model count per brand (current = `models`)
Peugeot 11 · Citroën 10 · DS 5 · Opel 11 · Fiat 10 · Abarth 2 · Alfa Romeo 4 · Lancia 2 · Jeep 4 · Maserati 4 ·
Leapmotor 5 = **68**. Announced: Fiat Grizzly/Grizzly Fastback, Jeep Recon, Leapmotor B03, Leapmotor D19.

## What was checked
Official Swiss sites that could be read: citroen.ch (model overview), peugeot.ch (homepage), fiat.ch (homepage),
alfaromeo.ch, abarth.ch, jeep.ch, maserati.com/ch. Blocked/empty: opel.ch, dsautomobiles.ch, lancia.ch (robots),
leapmotor.ch (robots), fiatprofessional.com. For these the Swiss press rooms were used – they give 2026
"ab sofort bestellbar" statements and CHF prices (DS N°7, Leapmotor B05/B03X/C10, Jeep Compass/Avenger, Fiat 500
Hybrid/Grande Panda/600/Topolino/Qubo L/Ulysse, Peugeot 408/E-208 GTi/208/2008, Alfa Tonale/Junior, Opel Corsa GSE,
Abarth 600e Competizione). German/Italian official overviews (peugeot.de, dsautomobiles.de, fiat.de, fiat.it,
alfaromeo.de, jeep.de, lancia.it, lancia.de, Opel DE press navigation) gave the complete nameplate lists.
Status checks from 2026 trade press are cited per model (Wikipedia used for platform/dimension facts).

## Judgement calls the verifier should look at
1. **Fiat 500 / 500e** – one tile ("500 / 500e"): the 2025 500 Hybrid uses the 500e body. Old 2007-body 500 ended 2024.
2. **Fiat Panda** – sold as "Pandina" (fiat.ch/.de/.it). Tile model = "Panda", display "Pandina (Panda)".
3. **Fiat Qubo L** (new 2026, Doblò-based 5/7-seater, CH from CHF 25,990) is the mpv-small tile; Fiat Doblò stays
   the van-small tile (passenger Doblò Kombi superseded). Toyota Proace City Verso named as out-of-group twin.
4. **Citroën Berlingo** appears twice (Berlingo = mpv-small, Berlingo Van = van-small), likewise Opel Combo (Life) /
   Combo Cargo, Peugeot Rifter / Partner – per the brief's row table.
5. **Opel Combo naming**: the Opel DE press site lists the passenger version simply as "Combo / Combo Electric"
   (Pkw) and the van under Nutzfahrzeuge; JSON keeps model "Combo Life" (display "Combo (Life)") with the DE name
   in `other_names`. Swiss name could not be verified (opel.ch unreadable).
6. **ë-C3 Van, Pandina Van, Jumpy Combi, SpaceTourer "Holidays", Topolino Sport/Vilebrequin, Corsa GSE, Mokka GSE,
   Giulia/Stelvio Quadrifoglio, Abarth 600e Turismo/Competizione, Maserati MCPura Cielo and GT2 Stradale** are
   treated as versions of their base nameplate (same tile) – noted in `notes`.
7. **Maserati GranTurismo / GranCabrio** – two tiles (different nameplates) linked as tier 1 (same body).
8. **Rows**: Peugeot 408 in c-hatch (brief guidance) despite 4.69 m; Jeep Grand Cherokee in d-suv (brief guidance)
   despite 4.91 m; Lancia Gamma (4,660 mm, same wheelbase as DS N°7) in c-suv with the STLA Medium group;
   Leapmotor B05 (4.43 m hatch) in c-hatch; Leapmotor B03X (~4.3 m crossover) in b-suv; Leapmotor C10 (4.74 m)
   in d-suv; Grizzly (<4.5 m) in b-suv with C3 Aircross/Frontera; DS N°7 (4.66 m) in c-suv like the Grandland.
9. **DS 7** marked `runout`: still on dsautomobiles.de with offers, but DS says the N°7 "replaces" it (DS CH press,
   17 Mar 2026) and the N°7 is orderable in FR (Mar 2026) and CH (Jun 2026, CHF 42,900/51,990). Check order books.
10. **Jeep Wrangler / Grand Cherokee** marked `runout`: Jeep declared 2026 the last Wrangler sales year in Europe
    (Fleet Magazine, Jan 2026); Jeep Europe told Automobile Propre (30 Jun 2026) that Wrangler and Grand Cherokee
    sales have stopped and cars come from stock; both still appear on jeep.de / jeep.ch (Oct 2026).
    Jeep Renegade: production ended late 2025 → listed as discontinued (dealer stock into 2026).
11. **Lancia** – on sale only in IT/FR/ES/PT/BE/NL/LU; `ch_on_sale: false`. Gamma: orders opened Europe-wide at the
    Paris show (Oct 2026), Italy from €39,900; Wikipedia says showroom sale from Nov 2026 → counted `on_sale`.
12. **Leapmotor** – grouped under Stellantis (Leapmotor International, 51 % Stellantis). Current: T03, C10 (BEV +
    REEV), B10 (BEV + REEV, CH from CHF 29,900), B05 (launched Jun 2026, CHF 25,900), B03X (= A10; CH launch
    11 Sep 2026, CHF 23,900). Announced: B03 hatch and D19 SUV (Paris Oct 2026, Auto Zürich Nov 2026).
13. **Fiat Tipo** – production ended June 2026, removed from fiat.it/.de/.ch → discontinued (not run-out).
14. **Fiat Fiorino** – absent from the Fiat Professional ranges on fiat.it/fiat.de (only Doblò, Scudo, Ducato,
    Pandina Van) → listed as discontinued; no explicit end-of-production article found.
15. **Powertrain coding**: per brief, "MHEV" only where no non-hybrid petrol/diesel exists (3008/5008/Grandland/
    C5 Aircross/Compass/N°4/N°7/308/408/Frontera/Junior/Tonale/Gamma/Panda/500 Hybrid). Leapmotor C10/B10 REEV
    coded as "PHEV".
16. **Peugeot 408** got a facelift ("new 408", Brussels Jan 2026, orderable CH Apr 2026) – generation field says so.
17. **Opel Astra**: Opel DE calls it "Neuer Astra" (Oct 2026, from €31,890) – a 2026 update; GSE Line from spring 2027.

## Twin groups (tier, row) – see also `twin_groups` in the JSON
| row | tier | members | source |
|---|---|---|---|
| quadricycle | 1 | Citroën Ami, Opel Rocks, Fiat Topolino | Carscoops (Rocks-e = rebadged Ami), motor1 (Topolino) |
| a-city | 1 | Fiat 500/500e, Abarth 500e | Wikipedia Abarth 500e |
| b-hatch | 2 | Peugeot 208, Opel Corsa, Lancia Ypsilon (CMP/e-CMP) | Wikipedia Peugeot 208 / Alfa Junior infobox |
| b-hatch | 2 | Citroën C3, Fiat Grande Panda (Smart Car) | Wikipedia Opel Frontera (2024) infobox |
| b-suv | 2 (600↔600e tier 1) | Peugeot 2008, Opel Mokka, DS 3, Jeep Avenger, Fiat 600, Abarth 600e, Alfa Junior (CMP/e-CMP, STLA Small) | Wikipedia Alfa Romeo Junior (2024) / Peugeot 208 |
| b-suv | 1 | Citroën C3 Aircross, Opel Frontera ("sister model", same body & wheelbase); + Fiat Grizzly tier 2 (announced) | Wikipedia Opel Frontera (2024), Fiat Grizzly |
| c-hatch | 2 | Peugeot 308, Opel Astra, DS N°4, Peugeot 408 (EMP2 V3) | Wikipedia DS No. 4 |
| c-suv | 2 | Peugeot 3008, Opel Grandland, Citroën C5 Aircross, Jeep Compass, DS N°7, Lancia Gamma (STLA Medium) | Wikipedia DS No. 7, Lancia Gamma (2026) |
| d-suv | 2 | Peugeot 5008, DS N°8 (STLA Medium long) | Wikipedia DS No. 7 |
| d-suv | 2 (weak) | Alfa Stelvio, Maserati Grecale, Jeep Grand Cherokee (run-out) – shared Giorgio platform, different wheelbases | Wikipedia Maserati Grecale |
| mpv-small | 1 | Peugeot Rifter, Citroën Berlingo, Opel Combo (Life), Fiat Qubo L, Toyota Proace City Verso (K9) | Wikipedia Stellantis Pro One, Toyota ProAce |
| mpv-large | 1 | Peugeot Traveller, Citroën SpaceTourer, Opel Zafira, Fiat Ulysse, Toyota Proace Verso (K0) | Wikipedia Stellantis Pro One, Toyota ProAce |
| van-small | 1 | Peugeot Partner, Citroën Berlingo Van, Opel Combo Cargo, Fiat Doblò, Toyota Proace City (K9) | Wikipedia Stellantis Pro One |
| van-mid | 1 | Peugeot Expert, Citroën Jumpy, Opel Vivaro, Fiat Scudo, Toyota Proace (K0) | Wikipedia Stellantis Pro One, Toyota ProAce |
| van-large | 1 | Peugeot Boxer, Citroën Jumper, Opel Movano, Fiat Ducato, Toyota Proace Max | Wikipedia Stellantis Pro One |
| sports | 1 | Maserati GranTurismo, GranCabrio | Wikipedia Maserati GranTurismo |
Citroën C4 (CMP, c-hatch), Alfa Tonale (FCA Small Wide, c-suv), DS 7 (EMP2, run-out) and all Leapmotors have no
current same-row sibling. Convention in the JSON: `twin_members` lists ALL same-row siblings; `twin_tier` is the
tier of the closest link and `twin_note` says which members are tier 1 vs tier 2 (only relevant for Fiat 600 /
Abarth 600e inside the CMP group). The Toyota Proace City / Proace City Verso / Proace Max rebadges are asserted from
the Stellantis Pro One list and the Toyota ProAce article (which covers Proace/Proace Verso explicitly only).

## Discontinued 2024–2026 (checked, excluded)
Peugeot 508; Citroën C5 X; DS 9; Opel Crossland; Fiat Tipo, 500X, Fiorino, old-body 500; Abarth 595/695;
Jeep Renegade, Gladiator (EU 2023); Maserati Levante, Ghibli, Quattroporte. Not for Europe: Jeep Cherokee, Wagoneer S.

## Open questions for the verifier
- Swiss status of Opel Combo (Life) passenger version, DS 7 (run-out) and Jeep Wrangler (run-out) – unknown.
- Opel Mokka/Astra/Zafira/Rocks `ch_on_sale: true` rests on the Swiss press-site navigation + DE range (no CHF
  price found); Peugeot Rifter/Traveller/Expert/Boxer likewise (Swiss press-site navigation).
- Opel Combo (Life) and Zafira Swiss names (opel.ch could not be read).
- Lancia Gamma row (c-suv chosen) and status (orders open Oct 2026 vs showroom Nov 2026).
- Frontera ↔ C3 Aircross tier 1 (bodies shared, interiors differ) – could be downgraded to tier 2.
- Stelvio ↔ Grecale ↔ Grand Cherokee tier 2 (Giorgio) – weak; could be dropped.
- Fiat Fiorino end-of-production date (no article found; absent from official ranges).
- Peugeot Rifter/Berlingo/Combo Life combustion engines after the 2024 facelift (coded petrol+diesel+BEV).

## Images
Stopped on instruction. Captured before the stop: carsized side images for Peugeot 208 (2023 facelift entry) and
308, Opel Corsa (2019–2023 entry), Mokka, Combo Life (2018–2023 entry), Fiat 500 (2020); slugs only for 408
(`peugeot-408-2022-liftback-crossover`), 5008 (`peugeot-5008-2024-suv`), Rifter (`peugeot-rifter-2018-van-l2`),
Expert (`peugeot-expert-2016-panel-van-standard`), 2008 (`peugeot-2008-2019-suv`), Avenger (`jeep-avenger-2023-suv`),
Berlingo (`citroen-berlingo-2018-van-xl`). carsized slug conventions learned: SUVs `<make>-<model>-<year>-suv`
(no door count), vans `-van-<variant>` / `-panel-van-<size>`, hatchbacks `-5-door-hatchback`, sedans `-sedan`,
408 `-liftback-crossover`; facelifts get their own entries ("Gen. 2.1"). Commons categories: none captured.
