#!/usr/bin/env python3
"""Second patch: fold the 2026-10-22 official-site verifications into build_lcv.py."""
import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_lcv.py")
s = open(p, encoding="utf-8").read()
def rep(old, new):
    global s
    assert s.count(old) == 1, ("NOT UNIQUE/FOUND", s.count(old), old[:90])
    s = s.replace(old, new)

# constants
rep('FIAT_CH = "https://www.fiat.ch/de"', '''FIAT_CH = "https://www.fiat.ch/de"
FIAT_CH_PRO = "https://www.fiat.ch/de/professional/business-offers/range"
FIAT_CH_QUBO = "https://www.fiat.ch/de/models/fiat-qubo-l"
FIAT_IT = "https://www.fiat.it/professional"
PEUGEOT_CH_PRO = "https://www.peugeot.ch/de/professionell/aktuelle-angebote-fur-gewerbetreibende.html"
TOYOTA_UK = "https://www.toyota.co.uk/new-cars"
VWN_DE = "https://www.volkswagen-nutzfahrzeuge.de/"
VWN_DE_CADDY = "https://www.volkswagen-nutzfahrzeuge.de/de/modelle/caddy.html"
VWN_DE_CRAFTER = "https://www.volkswagen-nutzfahrzeuge.de/de/modelle/crafter.html"
VWN_DE_CARAVELLE = "https://www.volkswagen-nutzfahrzeuge.de/de/modelle/caravelle.html"
FORD_DE = "https://www.ford.de/nutzfahrzeuge"
FORD_DE_CONNECT = "https://www.ford.de/nutzfahrzeuge-modelle/ford-transit-connect"
FORD_DE_CITY = "https://www.ford.de/nutzfahrzeuge-modelle/ford-transit-city"
KGM_UK_RHINO = "https://www.kgm-motors.co.uk/new-cars/all-new-musso-rhino/"
MAXUS_UK_MIFA7 = "https://www.saicmaxus.co.uk/our-range/new-vans/mifa-7/"
LEVC = "https://www.levc.com/"
INEOS_UK = "https://ineosgrenadier.com/en/gb/"
RT_LCV = "https://www.renault-trucks.com/en/renault-trucks-light-commercial-vehicules"
HYUNDAI_DE_STARIA = "https://www.hyundai.com/de/de/modelle/staria.html"
CITROEN_CH_SPACETOURER = "https://www.citroen.ch/de/modelle/new-e-spacetourer.html"
VAUXHALL_UK = "https://www.vauxhall.co.uk/"''')

# Renault Trucks Master / Trafic
rep('''status_note="Renault Trucks (Volvo Group) has sold the Master through its truck network since 2010 (Red Edition) and markets the Master IV / Master E-Tech; the 15 Sep 2026 press release confirms a growing Renault Trucks LCV business (target 40,000 LCVs/yr by 2030) but does not list the Master itself — VERIFY current Master IV listing on renault-trucks.com.",
    status_sources=[RT_PR, W+"Renault_Master"],''',
'''status_note="renault-trucks.com LCV page (fetched 2026-10-22) lists the 'Renault Trucks Master Red EDITION' (panel van, crew van, chassis/platform cab; dCi 2.0 110–170 hp diesel or 100 % electric; 3.5–4.5 t GVW) — the page does not state the generation, assumed to be the Master IV supplied since 2024.",
    status_sources=[RT_LCV, RT_PR, W+"Renault_Master"],''')
rep('''status_note="Renault Trucks Trafic sold since 2022 ('Trafic Red Edition', press release May 2022, referenced in the 15 Sep 2026 release); Wikipedia lists 'Renault Trucks Trafic: from 2022'. Its electric successor, the Renault Trucks E-Tech Trafic, goes on sale in H1 2027 (see announced).",
    status_sources=[RT_PR, W+"Renault_Trafic"],''',
'''status_note="renault-trucks.com LCV page (fetched 2026-10-22) lists the 'Renault Trucks Trafic Red EDITION' (van, crew van, platform cab, combi; dCi 2.0 110–170 hp diesel; 2.8–3.1 t GVW); sold since 2022 (Wikipedia). Its electric successor, the Renault Trucks E-Tech Trafic, goes on sale in H1 2027 (see announced).",
    status_sources=[RT_LCV, RT_PR, W+"Renault_Trafic"],''')
rep('''body="panel van", generation="III (X82, 2014–)", length_mm=4999, platform="Renault X82", powertrains=["diesel","BEV"], status="on_sale",''',
    '''body="panel van, crew van, platform cab, combi", generation="III (X82, 2014–)", length_mm=5080, platform="Renault X82", powertrains=["diesel"], status="on_sale",''')

# Peugeot CH statuses
rep('''status_note="Partner Premium Long featured on peugeot.ch home page (2026-10-21). Facelifted (new face, i-Cockpit) early 2024.", status_sources=["https://www.peugeot.ch/de/"],''',
    '''status_note="Partner / E-Partner listed with business offers (from CHF 20,990 net, valid to 30.11.2026) on peugeot.ch (fetched 2026-10-22). Facelifted (new face, i-Cockpit) early 2024.", status_sources=[PEUGEOT_CH_PRO, W+"Citro%C3%ABn_Berlingo"],''')
rep('''ch_on_sale=True, ch_source="https://www.peugeot.ch/de/professionell/aktuelle-angebote-fur-gewerbetreibende.html",
    row="van-small", body="panel van (Standard / Long), crew van",''',
    '''ch_on_sale=True, ch_source=PEUGEOT_CH_PRO,
    row="van-small", body="panel van (Standard / Long), crew van",''')
rep('''other_names=["E-Expert (electric)", "E-Expert Hydrogen"], ch_on_sale=None, ch_source=None, row="van-mid",''',
    '''other_names=["E-Expert (electric)"], ch_on_sale=True, ch_source=PEUGEOT_CH_PRO, row="van-mid",''')
rep('''status_note="VERIFY peugeot.ch listing (fetch budget).", status_sources=[W+"Peugeot_Expert"],''',
    '''status_note="Expert / E-Expert listed with business offers (from CHF 26,990 net, valid to 30.11.2026) on peugeot.ch (fetched 2026-10-22).", status_sources=[PEUGEOT_CH_PRO, W+"Citro%C3%ABn_Jumpy"],''')
rep('''other_names=["E-Boxer (electric)"], ch_on_sale=None, ch_source=None, row="van-large",''',
    '''other_names=["E-Boxer (electric)"], ch_on_sale=True, ch_source=PEUGEOT_CH_PRO, row="van-large",''')
rep('''status_note="VERIFY peugeot.ch listing. 2024 facelift brought new front, interior and 110 kWh E-Boxer.", status_sources=[W+"Peugeot_Boxer"],''',
    '''status_note="Boxer / E-Boxer listed with business offers (from CHF 37,990 net, valid to 30.11.2026) on peugeot.ch (fetched 2026-10-22). 2024 facelift brought new front, interior and 110 kWh E-Boxer.", status_sources=[PEUGEOT_CH_PRO, W+"Fiat_Ducato"],''')
rep('''status_note="VERIFY peugeot.ch listing (home page did not list it; model pages not fetched).", status_sources=[W+"Peugeot_Rifter"],''',
    '''status_note="Rifter/E-Rifter is a current K9 passenger model (Wikipedia Berlingo article, fetched 2026-10-22; 2024 facelift); not shown on the Swiss pages fetched (home, business offers) — Swiss listing unverified.", status_sources=[W+"Citro%C3%ABn_Berlingo"],''')
rep('''status_note="Since Jan 2022 Stellantis sells the Traveller/SpaceTourer/Zafira Life passenger vans in Europe only as electric (E-Traveller), except in Switzerland and the Balkans where diesel continues (Wikipedia Jumpy article, fetched 2026-10-22). VERIFY peugeot.ch listing.", status_sources=[W+"Citro%C3%ABn_Jumpy"],''',
    '''status_note="Since Jan 2022 Stellantis sells the Traveller/SpaceTourer/Zafira Life passenger vans in Europe only as electric (E-Traveller), except in Switzerland and the Balkans where diesel continues (Wikipedia Jumpy article, fetched 2026-10-22). Not shown on the Swiss pages fetched — Swiss listing unverified.", status_sources=[W+"Citro%C3%ABn_Jumpy"],''')

# Citroën SpaceTourer CH confirmed
rep('''other_names=["ë-SpaceTourer (electric)"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="5–9-seat people carrier (M / XL)", generation="I (K0, 2016–; facelift 2024)", length_mm=4981,''',
    '''other_names=["ë-SpaceTourer (electric)"], ch_on_sale=True, ch_source=CITROEN_CH_SPACETOURER, row="mpv-large",
    body="5–9-seat people carrier (M / XL)", generation="I (K0, 2016–; facelift 2024)", length_mm=4983,''')
rep('''status_note="Sold in most of Europe only as ë-SpaceTourer (electric) since Jan 2022; diesel continues in Switzerland/Balkans (Wikipedia Jumpy article, fetched 2026-10-22). Not shown on the citroen.ch home/LCV pages fetched on 2026-10-21 — VERIFY the Swiss listing.", status_sources=[W+"Citro%C3%ABn_Jumpy"],''',
    '''status_note="citroen.ch ë-SpaceTourer page (fetched 2026-10-22): M (4,983 mm) and XL (5,333 mm), 8–9 seats, 49/75 kWh, from CHF 47,800 with configurator and an offer valid 1 Sep–31 Oct 2026; diesel SpaceTourer mentioned for CH. In most of Europe electric-only since Jan 2022 (Wikipedia Jumpy article).", status_sources=[CITROEN_CH_SPACETOURER, W+"Citro%C3%ABn_Jumpy"],''')

# Fiat CH statuses
rep('''other_names=["E-Doblò (electric)", "Doblò Van"], ch_on_sale=None, ch_source=None, row="van-small",''',
    '''other_names=["E-Doblò (electric)", "Doblò Van"], ch_on_sale=True, ch_source=FIAT_CH_PRO, row="van-small",''')
rep('''status_note="Doblò III (K9 rebadge) since 2022 incl. E-Doblò (Wikipedia Berlingo article, fetched 2026-10-22); fiat.ch links Fiat Professional's business range (fetch of the Swiss Professional site failed) — VERIFY CH listing.", status_sources=[W+"Citro%C3%ABn_Berlingo", FIAT_CH],''',
    '''status_note="Fiat Professional CH range page (fetched 2026-10-22) lists Doblò / E-Doblò (diesel, petrol or electric; E-Doblò from CHF 26,390 net, offer 1 Apr–30 Sep 2026); fiat.it lists Doblò (diesel/petrol) and E-Doblò. Doblò III = K9 rebadge since 2022 (Wikipedia Berlingo article).", status_sources=[FIAT_CH_PRO, FIAT_IT, W+"Citro%C3%ABn_Berlingo"],''')
rep('''other_names=["E-Scudo (electric)"], ch_on_sale=None, ch_source=None, row="van-mid",''',
    '''other_names=["E-Scudo (electric)"], ch_on_sale=True, ch_source=FIAT_CH_PRO, row="van-mid",''')
rep('''status_note="Scudo (K0 rebadge) since 2022 (Wikipedia Jumpy article, fetched 2026-10-22). Swiss Fiat Professional site could not be fetched — VERIFY CH listing.", status_sources=[W+"Citro%C3%ABn_Jumpy"],''',
    '''status_note="Fiat Professional CH range page (fetched 2026-10-22) lists Scudo / E-Scudo (E-Scudo from CHF 28,440 net); fiat.it lists Scudo (diesel) and E-Scudo. K0 rebadge since 2022 (Wikipedia Jumpy article).", status_sources=[FIAT_CH_PRO, FIAT_IT, W+"Citro%C3%ABn_Jumpy"],''')
rep('''other_names=["E-Ducato (electric)"], ch_on_sale=None, ch_source=None, row="van-large",''',
    '''other_names=["E-Ducato (electric)", "Fiat Camper (motorhome base)"], ch_on_sale=True, ch_source=FIAT_CH_PRO, row="van-large",''')
rep('''status_note="Wikipedia (fetched 2026-10-22): X290 since 2014, facelifts 2021 and 2024 (revealed 23 Oct 2023; 2.2 Multijet 120/140/180 PS, E-Ducato 110 kWh/200 kW). Swiss Fiat Professional site could not be fetched — VERIFY CH listing.", status_sources=[W+"Fiat_Ducato"],''',
    '''status_note="Fiat Professional CH range page (fetched 2026-10-22) lists Ducato / E-Ducato (E-Ducato from CHF 49,581 net); fiat.it lists Ducato (diesel) and E-Ducato. Wikipedia: X290 since 2014, facelifts 2021 and 2024 (2.2 Multijet 120/140/180 PS, E-Ducato 110 kWh/200 kW).", status_sources=[FIAT_CH_PRO, FIAT_IT, W+"Fiat_Ducato"],''')
rep('''status_note="fiat.ch (fetched 2026-10-22) lists 'Ulysse' (thermic) and 'E-Ulysse' under Professional with quote requests. Ulysse (K0 rebadge) sold since 2022 (Wikipedia Jumpy article).", status_sources=[FIAT_CH, W+"Citro%C3%ABn_Jumpy"],''',
    '''status_note="fiat.ch (fetched 2026-10-22) lists 'Ulysse' (thermic) and 'E-Ulysse' under Professional with quote requests; fiat.it lists Ulysse Elettrica and Diesel. Ulysse (K0 rebadge) sold since 2022 (Wikipedia Jumpy article).", status_sources=[FIAT_CH, FIAT_IT, W+"Citro%C3%ABn_Jumpy"],''')
# Qubo
rep('''other_names=["Qubo L (long, 7 seats, CH listing)", "Doblò (passenger, 2022–2025 predecessor name)", "E-Doblò"], ch_on_sale=True, ch_source="https://www.fiat.ch/de/models/fiat-qubo-l",''',
    '''other_names=["Qubo L (CH/IT model name)", "Doblò (passenger, 2022–2025 predecessor name)", "E-Doblò"], ch_on_sale=True, ch_source=FIAT_CH_QUBO,''')
rep('''status_note="New for 2026: Wikipedia's Berlingo article (fetched 2026-10-22) lists 'Fiat Qubo, 2026–present' among the K9 rebadges and fiat.ch lists 'Qubo L' with a promotion and model page on 2026-10-22. It takes over the passenger role of the Doblò (the E-Doblò passenger version appears in CH only via the stock locator = runout). Powertrains to VERIFY (likely 1.2 petrol/MHEV, 1.5 diesel, electric).",
    status_sources=[FIAT_CH, W+"Citro%C3%ABn_Berlingo"],''',
    '''status_note="New for 2026: fiat.ch Qubo L page (fetched 2026-10-22) — 5 or 7 seats, electric 100 kW, automatic diesel 96 kW, manual petrol 81 kW, MY26 price list, 'Konfigurieren' button; fiat.it lists 'Qubo L' (Benzina, Elettrica, Diesel) in the passenger-car menu. Wikipedia's Berlingo article lists 'Fiat Qubo, 2026–present' among the K9 rebadges. It takes over the passenger role of the Doblò (no passenger Doblò/E-Doblò on fiat.it any more; in CH only via stock locator = runout).",
    status_sources=[FIAT_CH_QUBO, FIAT_IT, W+"Citro%C3%ABn_Berlingo"],''')
rep('''notes="Revives the Qubo name (2008–2024 Fiorino-based MPV). Lengths assumed 4403 / 4753 mm (K9 M/XL). VERIFY exact name/variants on fiat.it and whether a short 'Qubo' exists beside 'Qubo L'."''',
    '''notes="Revives the Qubo name (2008–2024 Fiorino-based MPV). Only 'Qubo L' is listed in CH and IT (5/7 seats) — probably the long K9 body (4753 mm); the standard K9 body is 4403 mm."''')
rep('''row="mpv-small", body="5/7-seat leisure activity vehicle (K9 body)", generation="III (K9, 2026–)", length_mm=4403,''',
    '''row="mpv-small", body="5/7-seat leisure activity vehicle (K9 body, 'Qubo L')", generation="III (K9, 2026–)", length_mm=4753,''')

# Toyota UK sources
for old, new in [
 ('''status_note="VERIFY with toyota.ch/professional (fetch failed).", status_sources=[W+"Toyota_ProAce_City"],
    twin_tier=1, twin_members=others(G_K9_VAN, "Toyota Proace City"),''',
  '''status_note="Listed as 'Proace City' on toyota.co.uk new-cars overview (fetched 2026-10-22); K9 rebadge since 2019 (Wikipedia Berlingo article). toyota.ch/professional could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_VAN, "Toyota Proace City"),'''),
 ('''status_note="VERIFY with toyota.ch (fetch failed).", status_sources=[W+"Toyota_ProAce_City"],
    twin_tier=1, twin_members=others(G_K9_MPV, "Toyota Proace City Verso"),''',
  '''status_note="Listed as 'Proace City Verso' on toyota.co.uk (fetched 2026-10-22). toyota.ch could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_MPV, "Toyota Proace City Verso"),'''),
 ('''status_note="VERIFY with toyota.ch/professional (fetch failed).", status_sources=[W+"Toyota_ProAce"],
    twin_tier=1, twin_members=others(G_K0_VAN, "Toyota Proace"),''',
  '''status_note="Listed as 'Proace' on toyota.co.uk (fetched 2026-10-22); K0 rebadge (Wikipedia Jumpy article). toyota.ch/professional could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_VAN, "Toyota Proace"),'''),
 ('''status_note="VERIFY with toyota.ch (fetch failed).", status_sources=[W+"Toyota_ProAce"],
    twin_tier=1, twin_members=others(G_K0_MPV, "Toyota Proace Verso"),''',
  '''status_note="Listed as 'Proace Verso' and 'Proace Verso Electric' on toyota.co.uk (fetched 2026-10-22); Toyota kept diesel passenger versions after Stellantis' 2022 electric-only decision (Wikipedia Jumpy article). toyota.ch could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_MPV, "Toyota Proace Verso"),'''),
 ('''status_note="Wikipedia (fetched 2026-10-22): Toyota-badged Ducato (Sevel Sud) listed 2023–present, 2.2 diesel 120/140/180 PS (8-speed auto) and Proace Max Electric 110 kWh/200 kW. toyota.ch/professional could not be fetched.", status_sources=[W+"Toyota_ProAce_Max"],''',
  '''status_note="Listed as 'Proace Max' on toyota.co.uk (fetched 2026-10-22). Wikipedia: Toyota-badged Ducato (Sevel Sud) 2023–present, 2.2 diesel 120/140/180 PS and Proace Max Electric 110 kWh/200 kW. toyota.ch/professional could not be fetched.", status_sources=[TOYOTA_UK, W+"Toyota_ProAce_Max"],'''),
]:
    rep(old, new)
rep('''status_sources=[TOYOTA_UK_HILUX, "https://de.wikipedia.org/wiki/Toyota_Hilux", W+"Toyota_Hilux"],''',
    '''status_sources=[TOYOTA_UK_HILUX, TOYOTA_UK, "https://de.wikipedia.org/wiki/Toyota_Hilux", W+"Toyota_Hilux"],''')

# VW
rep('''body="panel van (SWB / Maxi)", generation="Typ SB ('Caddy 5', 2020–)", length_mm=4500,
    platform="MQB (VW Group)", powertrains=["petrol","diesel","CNG","PHEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): unveiled Feb 2020, on sale Nov 2020; TGI CNG added July 2022; 5-star Euro NCAP 2025. Caddy eHybrid PHEV (2024/25) not in Wikipedia — VERIFY. Swiss site robots-blocked.", status_sources=[W+"Volkswagen_Caddy"],''',
    '''body="panel van (SWB / Maxi)", generation="Typ SB ('Caddy 5', 2020–; 'Caddy 2026' facelift-level update, launch autumn 2026)", length_mm=4500,
    platform="MQB (VW Group)", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) shows 'Der neue Caddy Cargo' alongside the 'Caddy 2026' (facelift-level product upgrade, 'bereits bestellbar', market launch autumn 2026; eHybrid PHEV up to 122 km electric). Wikipedia: on sale since Nov 2020, TGI CNG added 2022 (CNG availability in 2026 unverified, not listed). Swiss site robots-blocked.", status_sources=[VWN_DE, VWN_DE_CADDY, W+"Volkswagen_Caddy"],''')
rep('''body="5/7-seat leisure activity vehicle; Caddy California camper", generation="Typ SB ('Caddy 5', 2020–)", length_mm=4500,
    platform="MQB (VW Group)", powertrains=["petrol","diesel","CNG","PHEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): on sale since Nov 2020 (Caddy, Life, Move, Style, Maxi, California). PHEV eHybrid to VERIFY. Swiss site robots-blocked.", status_sources=[W+"Volkswagen_Caddy"],''',
    '''body="5/7-seat leisure activity vehicle (Caddy / Caddy Maxi); Caddy California camper", generation="Typ SB ('Caddy 5', 2020–; 'Caddy 2026' facelift-level update, launch autumn 2026)", length_mm=4500,
    platform="MQB (VW Group)", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de Caddy page (fetched 2026-10-22): 'Der neue Caddy' = Caddy 2026 product upgrade (new bumper, 12.9-inch display, Travel Assist 3.0), 'bereits bestellbar', market launch autumn 2026, 75–90 kW engines plus eHybrid plug-in hybrid (up to 122 km electric), from €34,201. Swiss site robots-blocked.", status_sources=[VWN_DE_CADDY, W+"Volkswagen_Caddy"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): unveiled Aug 2024, based on the Ford Transit Custom; e-Transporter 64 kWh, PHEV 16.5 kWh; first tests Feb 2025. Swiss site robots-blocked.", status_sources=[W+"Volkswagen_Transporter_(T7)"],''',
    '''status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) lists the Transporter as diesel, plug-in hybrid or fully electric. Wikipedia: unveiled Aug 2024 on the Ford Transit Custom basis; e-Transporter 64 kWh, PHEV 16.5 kWh. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_Transporter_(T7)"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): Caravelle and e-Caravelle unveiled Aug 2024 with the Transporter (Tourneo Custom basis). Swiss site robots-blocked.", status_sources=[W+"Volkswagen_Transporter_(T7)"],''',
    '''status_note="volkswagen-nutzfahrzeuge.de Caravelle page (fetched 2026-10-22): 'neueste Generation', two wheelbases, up to 9 seats, 81–210 kW, diesel / plug-in hybrid (later) / fully electric, from €53,830. Wikipedia: unveiled Aug 2024 with the Transporter (Tourneo Custom basis). Swiss site robots-blocked.", status_sources=[VWN_DE_CARAVELLE, W+"Volkswagen_Transporter_(T7)"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): Multivan T7 debuted mid-2021 on MQB (sold 2022–). Swiss site robots-blocked.", status_sources=[W+"Volkswagen_Transporter_(T7)", W+"Volkswagen_California"],''',
    '''status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) promotes 'Der neue Multivan' (updated model). Wikipedia: Multivan T7 debuted mid-2021 on MQB. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_Transporter_(T7)", W+"Volkswagen_California"],''')
rep('''status_note="FACTORY CAMPER — optional tile; drop if campers are out of scope. Wikipedia (fetched 2026-10-22): California (Multivan-based) launched 2024, LWB only, PHEV/diesel/petrol.", status_sources=[W+"Volkswagen_California"],''',
    '''status_note="FACTORY CAMPER — optional tile; drop if campers are out of scope. volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) lists 'Der neue California'; Wikipedia: California (Multivan-based) launched 2024, LWB only, PHEV/diesel/petrol.", status_sources=[VWN_DE, W+"Volkswagen_California"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): production since June 2022 (Hanover), European deliveries H2 2022, LWB (4962 mm, 86 kWh) and GTX added 2024. Swiss site robots-blocked.", status_sources=[W+"Volkswagen_ID._Buzz"],''',
    '''status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) lists ID. Buzz / ID. Buzz Pro. Wikipedia: production since June 2022 (Hanover), LWB (4962 mm, 86 kWh) and GTX added 2024. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_ID._Buzz"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): first Cargo delivered 15 Nov 2022; SWB only, 3.9 m³, 3.0 t GVW. Swiss site robots-blocked.", status_sources=[W+"Volkswagen_ID._Buzz"],''',
    '''status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) names the ID. Buzz Cargo. Wikipedia: first Cargo delivered 15 Nov 2022; SWB only, 3.9 m³, 3.0 t GVW. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_ID._Buzz"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): Crafter II built by VW in Września since 2017 (2.0 TDI 109–179 PS); the 2024 facelift and the new e-Crafter (2025) are not yet on the page — VERIFY. Swiss site robots-blocked.", status_sources=[W+"Volkswagen_Crafter"],''',
    '''status_note="volkswagen-nutzfahrzeuge.de Crafter page (fetched 2026-10-22): 'Der neue Crafter' (2024 facelift with Digital Cockpit Pro; technical data file 'crafter_2024'), panel van / dropside / chassis cab in three lengths, from €43,920 net; the page lists only 2.0 TDI — e-Crafter not named there (BEV kept from the 2024/25 e-Crafter announcement, unverified). Swiss site robots-blocked.", status_sources=[VWN_DE_CRAFTER, W+"Volkswagen_Crafter"],''')
rep('''status_note="FACTORY CAMPER — optional tile; drop if campers are out of scope. VERIFY listing.", status_sources=[W+"Volkswagen_Crafter"],''',
    '''status_note="FACTORY CAMPER — optional tile; drop if campers are out of scope. Grand California 600/680 on sale since 2019 (Wikipedia Crafter/California articles, fetched 2026-10-22); 2026 listing not separately verified.", status_sources=[W+"Volkswagen_California", W+"Volkswagen_Crafter"],''')

# Ford
rep('''status_note="Wikipedia (fetched 2026-10-22): E-Transit Courier unveiled 6 Apr 2023, production from late 2024 at Craiova; 1.0/1.5 engines. ford.ch could not be fetched.", status_sources=[W+"Ford_Transit_Courier"],''',
    '''status_note="ford.de Nutzfahrzeuge page (fetched 2026-10-22) lists the E-Transit Courier; Wikipedia: E-Transit Courier unveiled 6 Apr 2023, production from late 2024 at Craiova; 1.0/1.5 engines. ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Transit_Courier"],''')
rep('''status_note="Wikipedia (fetched 2026-10-21): Caddy-based Transit Connect released in UK/Europe late 2024, 2024–present; no European discontinuation recorded there. VERIFY ford.ch/ford.de listing.",
    status_sources=[W+"Ford_Transit_Connect"],''',
    '''status_note="ford.de Transit Connect page (fetched 2026-10-22): current model with configurator, price list and stock vehicles (from €209/month); EcoBlue diesel 102/122 PS (optional AWD) and plug-in hybrid (110 kW, up to 117 km electric); L1 3.1 m³ / L2 3.7 m³, Kastenwagen and FlexCab. Wikipedia: Caddy-based generation released late 2024. The 'Connect to be axed' rumour is not supported by the German site.",
    status_sources=[FORD_DE_CONNECT, W+"Ford_Transit_Connect"],''')
rep('''platform="MQB (VW Group), built by VW in Poznań", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="ford.de Transit Connect page''', '''platform="MQB (VW Group), built by VW in Poznań", powertrains=["diesel","PHEV"], status="on_sale",
    status_note="ford.de Transit Connect page''')
rep('''status_note="Wikipedia (fetched 2026-10-21): launched Oct 2021 as a rebadged Caddy, 2021–present. VERIFY 2026 listing on ford.ch/ford.de.",
    status_sources=[W+"Ford_Transit_Connect"],''',
    '''status_note="Wikipedia (fetched 2026-10-21): launched Oct 2021 as a rebadged Caddy, 2021–present; the sister Transit Connect is a current model on ford.de (Oct 2026) with diesel and PHEV, so the Tourneo Connect is assumed current too (its own 2026 page not fetched).",
    status_sources=[W+"Ford_Transit_Connect", FORD_DE_CONNECT],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): unveiled Sept 2022, built by Ford Otosan from 2023; diesel, mild-hybrid, PHEV and E-Transit Custom (74 kWh usable). ford.ch could not be fetched.", status_sources=[W+"Ford_Transit_Custom"],''',
    '''status_note="ford.de (fetched 2026-10-22) lists the E-Transit Custom; Wikipedia: unveiled Sept 2022, built by Ford Otosan from 2023; diesel, mild-hybrid, PHEV and E-Transit Custom (74 kWh usable). ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Transit_Custom"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): 4th generation since 2013/14, 2020 revision (2.0 EcoBlue incl. 48 V mHEV), E-Transit for Europe built at Ford Otosan since April 2022, 89 kWh battery from 2024; no successor named. ford.ch could not be fetched.", status_sources=[W+"Ford_Transit"],''',
    '''status_note="ford.de (fetched 2026-10-22) lists the E-Transit (incl. skeletal chassis); Wikipedia: 4th generation since 2013/14, 2020 revision (2.0 EcoBlue incl. 48 V mHEV), E-Transit for Europe built at Ford Otosan since April 2022, 89 kWh from 2024; no successor named. ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Transit"],''')
rep('''status_note="Wikipedia (fetched 2026-10-22): European launch Nov 2022; 2.0 EcoBlue / 3.0 V6 diesel, Raptor 3.0 EcoBoost petrol (210 kW in EU); Ranger PHEV (2.3 EcoBoost + 11.7 kWh) unveiled Sept 2023, on sale 2025; Ranger Super Duty planned for Europe before end-2026 (same nameplate). ford.ch could not be fetched.", status_sources=[W+"Ford_Ranger_(T6)"],''',
    '''status_note="ford.de (fetched 2026-10-22) lists the Ranger Plug-in-Hybrid; Wikipedia: European launch Nov 2022; 2.0 EcoBlue / 3.0 V6 diesel, Raptor 3.0 EcoBoost petrol (210 kW in EU); Ranger PHEV (2.3 EcoBoost + 11.7 kWh) unveiled Sept 2023; Ranger Super Duty planned for Europe before end-2026 (same nameplate). ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Ranger_(T6)"],''')
# Ford Transit City (announced)
anchor = '# =================================================================== STELLANTIS — PEUGEOT'
rep(anchor, '''announced.append(m(brand="Ford", group="Ford", model="Transit City", display="Transit City (new)",
    other_names=[], ch_on_sale=None, ch_source=None, row="van-mid",
    body="electric panel van (short / medium wheelbase, 6–8 m³) and chassis cab", generation="I (2026/27–)", length_mm=None,
    platform="Ford/JMC (related to the JMC E-Fushun; built with Jiangling Motors)", powertrains=["BEV"], status="announced",
    status_note="ford.de (fetched 2026-10-22) presents 'Der neue Ford Transit City': 56 kWh LFP battery, 110 kW, up to 254 km, payload up to 1,085 kg (SWB) / 1,275 kg (MWB) / 1,600 kg (chassis), 10–80 % in 33 min, financing 'ab 279 €'; only 'Angebot anfragen' / newsletter, video tagged 'pre-launch', no order date — treated as announced (launch 2026/27). Wikipedia Transit article: 'In 2026 Ford, partnering with Jiangling Motors, will release the Transit City'.",
    status_sources=[FORD_DE_CITY, FORD_DE, W+"Ford_Transit"],
    twin_tier=None, twin_members=[], twin_note="JMC-built; no European twin. Positioned between Transit Custom and Transit (6–8 m³).", twin_sources=[W+"Ford_Transit"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Ford Transit", notes="Length not published on the DE page; row provisional (8 m³ MWB is at the mid/large boundary)."))

''' + anchor)

# KGM Rhino
rep('''body="double-cab pickup", generation="II (Q300, 2026–)", length_mm=5400,
    platform="KGM body-on-frame (new Musso Q300)", powertrains=["diesel"], status="on_sale",
    status_note="kgm-motors.co.uk (fetched 2026-10-22) lists the 'All-new Musso Rhino' from £38,995 ex VAT; the Q300-generation Musso debuted in Korea in December 2025 (Wikipedia). European name outside the UK and the exact powertrain line-up to VERIFY (likely 2.2 diesel).", status_sources=[KGM_UK, W+"SsangYong_Musso"],''',
    '''body="double-cab pickup (Rhino / Rhino+ extended wheelbase 3,210 mm)", generation="II (Q300, 2026–)", length_mm=5400,
    platform="KGM body-on-frame (new Musso Q300)", powertrains=["diesel"], status="on_sale",
    status_note="kgm-motors.co.uk Musso Rhino page (fetched 2026-10-22): 'the all-new Musso Rhino', 2.2 turbo diesel 202 PS / 400 Nm, payload 1,090 kg (Rhino+ 1,200 kg), 3,500 kg towing, from £38,995 ex VAT; the Q300-generation Musso debuted in Korea in December 2025 (Wikipedia). Name in other European markets unverified.", status_sources=[KGM_UK_RHINO, KGM_UK, W+"SsangYong_Musso"],''')
rep('notes="Length approximate. Could be merged with the Musso tile once the Q200 is gone."', 'notes="Length approximate (not published). Could be merged with the Musso tile once the Q200 is gone."')

# Maxus Mifa 7
rep('''"SAIC Maxus Mifa (electric)", ["BEV"], "Listed in the UK electric range as 'MIFA 7' (fetched 2026-10-22); model page could not be fetched (budget) — dimensions from training knowledge, VERIFY.", "Maxus_Mifa_7", "Category:Maxus Mifa 7", "~4.9 m, 90 kWh; smaller sibling of the Mifa 9."))''',
    '''"SAIC Maxus Mifa (electric)", ["BEV"], "UK Mifa 7 page (fetched 2026-10-22): electric MPV, 6 or 7 seats (2-1-3 / 2-2-3), up to 298 miles WLTP; length not published (~4.9 m from launch data).", "Maxus_Mifa_7", "Category:Maxus Mifa 7", "Smaller sibling of the Mifa 9."))''')
rep('''        status_sources=[MAXUS_UK, W+wiki], twin_tier=None,''', '''        status_sources=[MAXUS_UK, MAXUS_UK_MIFA7, W+wiki] if model == "Mifa 7" else [MAXUS_UK, W+wiki], twin_tier=None,''')

# LEVC VN5 + L380
rep('''status_note="Wikipedia (fetched 2026-10-22): on sale in the UK since Nov 2020 and in the rest of Europe since July 2021; infobox 'production 2020–present', no discontinuation recorded — VERIFY 2026 availability on levc.com.", status_sources=[W+"LEVC_VN5"],''',
    '''status_note="levc.com (fetched 2026-10-22) still lists the 'VN5 Van' among its models (dealer pages for DE, ES, NL, FR, SE, PL, HU, GR, AT, BE, MT); Wikipedia: UK sales since Nov 2020, rest of Europe since July 2021, production 2020–present.", status_sources=[LEVC, W+"LEVC_VN5"],''')
anchor2 = '# =================================================================== IVECO GROUP'
rep(anchor2, '''announced.append(m(brand="LEVC", group="Geely Holding", model="L380", display="L380",
    other_names=[], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="6–8-seat electric luxury MPV", generation="I (2024 China; Europe 2026)", length_mm=5316,
    platform="Geely SOA/SEA-derived electric MPV architecture", powertrains=["BEV"], status="announced",
    status_note="levc.com home (fetched 2026-10-22) lists 'The all New L380 MPV' with its own model page, but the page did not render and no UK price/order information was obtained — treated as announced for Europe; VERIFY order status.",
    status_sources=[LEVC],
    twin_tier=None, twin_members=[], twin_note="", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="LEVC L380", notes="Length from the Chinese launch data (5,316 mm), unverified for Europe."))

''' + anchor2)

# Ineos
rep('''status_note="Introduced July 2023 as the four-door pickup version of the Grenadier (Wikipedia, fetched 2026-10-22; 5,400 mm, 3,227 mm wheelbase); on sale in Europe since 2024 — 2026 listing on ineosgrenadier.com to VERIFY.", status_sources=[W+"Ineos_Grenadier"],''',
    '''status_note="ineosgrenadier.com UK page (fetched 2026-10-22) lists the 'GRENADIER Quartermaster' (double-cab off-road pickup) with test-drive link and offers for orders 1–31 Oct 2026; Wikipedia: introduced July 2023, 5,400 mm, 3,227 mm wheelbase.", status_sources=[INEOS_UK, W+"Ineos_Grenadier"],''')

# Hyundai Staria
rep('''platform="Hyundai-Kia N3 (FWD/AWD, shared with Kia Carnival IV)", powertrains=["diesel"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): sold in several European markets since 2021 (Europe: 2.2 CRDi diesel); facelift unveiled in Korea 17 Dec 2025 (on sale AU 2 Apr 2026) and a Staria Electric (84 kWh, 800 V) unveiled 9 Jan 2026 — European timing of both to VERIFY. hyundai.ch could not be fetched.", status_sources=[W+"Hyundai_Staria"],''',
    '''platform="Hyundai-Kia N3 (FWD/AWD, shared with Kia Carnival IV)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="hyundai.com/de (fetched 2026-10-22) sells the 'neue STARIA Elektro' (160 kW, 84 kWh, up to 430 km, from €57,450, 'NEU'); the diesel 2.2 CRDi is not on the German page any more (diesel availability per market unverified). Wikipedia: facelift unveiled 17 Dec 2025, Staria Electric unveiled 9 Jan 2026. hyundai.ch could not be fetched.", status_sources=[HYUNDAI_DE_STARIA, W+"Hyundai_Staria"],''')
rep('''platform="Hyundai-Kia N3", powertrains=["diesel"], status="on_sale",
    status_note="Cargo versions offered in several regions incl. Europe (Wikipedia, fetched 2026-10-22). hyundai.ch could not be fetched — VERIFY CH listing.", status_sources=[W+"Hyundai_Staria"],''',
    '''platform="Hyundai-Kia N3", powertrains=["diesel","BEV"], status="on_sale",
    status_note="hyundai.com/de (fetched 2026-10-22) sells the 'STARIA Cargo Elektro' (160 kW, 84 kWh, up to 450 km, from €57,454, 'NEU'); diesel Staria Van availability per market unverified. hyundai.ch could not be fetched.", status_sources=[HYUNDAI_DE_STARIA, W+"Hyundai_Staria"],''')

# Opel other names (Vauxhall)
rep('other_names=["Vauxhall Combo Cargo (UK)", "Combo Cargo Electric"]', 'other_names=["Vauxhall Combo / Combo Panel Van (UK)", "Combo Cargo Electric"]')
rep('other_names=["Vauxhall Vivaro (UK)", "Vivaro Electric", "Vivaro Hydrogen"]', 'other_names=["Vauxhall Vivaro / Vivaro Panel Van (UK)", "Vivaro Electric"]')
rep('other_names=["Vauxhall Movano (UK)", "Movano Electric", "Movano Hydrogen"]', 'other_names=["Vauxhall Movano / Movano Panel Van (UK)", "Movano Electric"]')

# Piaggio
rep('''status_note="VERIFY: sold in IT/FR/DE via Piaggio Commercial; included because it is a four-wheel N1 vehicle under 3.5 t. Group label = parent company (Piaggio Group), see .md.", status_sources=[W+"Piaggio_Porter"],''',
    '''status_note="Wikipedia (fetched 2026-10-22): NP6 presented Jan 2021, Foton Gratour V3-derived but re-engineered and built in Pontedera; 1.5 petrol/LPG or petrol/CNG, GVW ≤2.8 t, flatbed and chassis-cab bodies. 2026 listing not verified (Piaggio site not fetched). Included because it is a four-wheel N1 vehicle under 3.5 t; group label = parent company (Piaggio Group).", status_sources=[W+"Piaggio_Porter"],''')
rep('''body="cab-forward micro truck: chassis cab, tipper, flatbed, box van (N1, ≤2.8 t)", generation="I (2021–)", length_mm=4300,
    platform="Piaggio (Foton-derived ladder frame)", powertrains=["petrol","LPG","CNG"],''',
    '''body="cab-forward micro truck: flatbed (fixed/tipping), chassis cab for upfits (N1, ≤2.8 t)", generation="II (NP6, 2021–)", length_mm=4300,
    platform="Piaggio/Foton Gratour V3-derived ladder frame (RWD)", powertrains=["petrol","LPG","CNG"],''')

# sources list additions
rep('''        {"url": W+"Ineos_Grenadier", "what": "Wikipedia (fetched 2026-10-22): Quartermaster introduced July 2023, 5400 mm"},''',
'''        {"url": W+"Ineos_Grenadier", "what": "Wikipedia (fetched 2026-10-22): Quartermaster introduced July 2023, 5400 mm"},
        {"url": PEUGEOT_CH_PRO, "what": "Peugeot CH business offers (fetched 2026-10-22): Partner/E-Partner, Expert/E-Expert, Boxer/E-Boxer, offers valid to 30.11.2026"},
        {"url": FIAT_CH_PRO, "what": "Fiat Professional CH range (fetched 2026-10-22): Doblò/E-Doblò, Scudo/E-Scudo, Ducato/E-Ducato with 2026 offers"},
        {"url": FIAT_CH_QUBO, "what": "Fiat CH Qubo L page (fetched 2026-10-22): 5/7 seats, electric 100 kW, diesel 96 kW, petrol 81 kW, MY26, configurator"},
        {"url": FIAT_IT, "what": "Fiat IT (fetched 2026-10-22): Qubo L (petrol/electric/diesel), Ulysse electric+diesel, Professional: Ducato, Scudo, Doblò, Pandina Van, Fiat Camper; no Fiorino"},
        {"url": TOYOTA_UK, "what": "Toyota UK new-cars overview (fetched 2026-10-22): Proace City/Verso, Proace/Verso (+Electric), Proace Max, All-New Hilux, All-New Land Cruiser Commercial, Corolla Commercial"},
        {"url": VWN_DE, "what": "VW Nutzfahrzeuge DE home (fetched 2026-10-22): neue Caddy/Caddy Cargo/Caddy California, neuer Multivan, neuer California, Transporter (diesel/PHEV/electric), ID. Buzz/Cargo"},
        {"url": VWN_DE_CADDY, "what": "VWN DE Caddy page (fetched 2026-10-22): Caddy 2026 facelift-level update orderable, launch autumn 2026, eHybrid PHEV 122 km, from €34,201"},
        {"url": VWN_DE_CRAFTER, "what": "VWN DE Crafter page (fetched 2026-10-22): 'Der neue Crafter' (2024 facelift), van/dropside/chassis, 2.0 TDI, from €43,920 net"},
        {"url": VWN_DE_CARAVELLE, "what": "VWN DE Caravelle page (fetched 2026-10-22): newest generation, 2 wheelbases, 9 seats, diesel/PHEV/electric, from €53,830"},
        {"url": FORD_DE, "what": "Ford DE Nutzfahrzeuge page (fetched 2026-10-22): neuer Transit City, E-Transit Custom, Ranger PHEV, E-Transit Courier, E-Transit"},
        {"url": FORD_DE_CONNECT, "what": "Ford DE Transit Connect page (fetched 2026-10-22): current model, diesel 102/122 PS + PHEV 117 km, configurator"},
        {"url": FORD_DE_CITY, "what": "Ford DE Transit City page (fetched 2026-10-22): electric van 56 kWh LFP, 110 kW, 6/8 m³, pre-launch"},
        {"url": KGM_UK_RHINO, "what": "KGM UK Musso Rhino page (fetched 2026-10-22): all-new Musso Rhino, 2.2 diesel 202 PS, from £38,995 ex VAT"},
        {"url": MAXUS_UK_MIFA7, "what": "Maxus UK Mifa 7 page (fetched 2026-10-22): electric 6/7-seat MPV, up to 298 miles WLTP"},
        {"url": LEVC, "what": "LEVC home (fetched 2026-10-22): TX, Next Generation Taxi, VN5 Van, TX Access/Shuttle, all-new L380 MPV"},
        {"url": INEOS_UK, "what": "Ineos UK home (fetched 2026-10-22): Grenadier Station Wagon, Quartermaster pickup, Arcane Works Detour; Oct 2026 offers"},
        {"url": RT_LCV, "what": "Renault Trucks LCV page (fetched 2026-10-22): Master Red Edition (diesel/electric, 3.5–4.5 t) and Trafic Red Edition (diesel, 2.8–3.1 t)"},
        {"url": HYUNDAI_DE_STARIA, "what": "Hyundai DE Staria page (fetched 2026-10-22): neue Staria Elektro and Staria Cargo Elektro (84 kWh), prices"},
        {"url": CITROEN_CH_SPACETOURER, "what": "Citroën CH ë-SpaceTourer page (fetched 2026-10-22): M 4,983 / XL 5,333 mm, 49/75 kWh, from CHF 47,800, offer Sep–Oct 2026"},
        {"url": VAUXHALL_UK, "what": "Vauxhall UK home (fetched 2026-10-22): Combo/Vivaro/Movano Panel Van names"},
        {"url": W+"MAN_TGE", "what": "Wikipedia (fetched 2026-10-22): TGE = Crafter II sold by MAN, eTGE since July 2018"},
        {"url": W+"Piaggio_Porter", "what": "Wikipedia (fetched 2026-10-22): Porter NP6 Jan 2021, Foton-derived, petrol/LPG/CNG, ≤2.8 t"},''')

open(p, "w", encoding="utf-8").write(s)
print("patched")
