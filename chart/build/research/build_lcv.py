#!/usr/bin/env python3
"""Builds lcv.json (light-commercial cross-brand research) from the data below.
Run: python3 -I build_lcv.py  -> writes lcv.json next to this script.
Fields follow brief.md exactly. Values marked VERIFY in notes still need a 2026 source."""
import json, os, datetime

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lcv.json")

W = "https://en.wikipedia.org/wiki/"
RT_PR = "https://www.renault-trucks.com/en/newsroom/press-releases/new-renault-trucks-etech-trafic"
RENAULT_CH_TRAFIC_EV = "https://de.business.renault.ch/trafic-van-range/trafic-pcx-ph1.html"
TOYOTA_UK_HILUX = "https://www.toyota.co.uk/new-cars/hilux"
KGM_UK = "https://www.kgm-motors.co.uk/"
MAXUS_UK = "https://www.saicmaxus.co.uk/"
FIAT_CH = "https://www.fiat.ch/de"
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
VAUXHALL_UK = "https://www.vauxhall.co.uk/"
RENAULT_CH_VANS = "https://de.renault.ch/vans.html"
RENAULT_CH_HOME = "https://de.renault.ch/"
NISSAN_CH = "https://de.nissan.ch/fahrzeuge/neuwagen.html"
OPEL_CH = "https://www.opel.ch/de/"
CITROEN_CH_LCV = "https://www.citroen.ch/de/professional/nutzfahrzeuge.html"
KIA_CH = "https://www.kia.ch/"

KEYS = ["brand","group","model","display","other_names","ch_on_sale","ch_source","row","body",
        "generation","length_mm","platform","powertrains","status","status_note","status_sources",
        "twin_tier","twin_members","twin_note","twin_sources","carsized_slug","carsized_side",
        "carsized_front","carsized_years","commons_category","commons_file","wikipedia_en","notes"]

def m(**kw):
    d = {k: None for k in KEYS}
    d.update({"other_names": [], "powertrains": [], "status": "on_sale", "status_sources": [],
              "twin_tier": None, "twin_members": [], "twin_note": "", "twin_sources": [],
              "ch_on_sale": None, "ch_source": None, "commons_file": None, "notes": ""})
    d.update(kw)
    missing = [k for k in KEYS if k not in d]
    assert not missing, missing
    extra = [k for k in d if k not in KEYS]
    assert not extra, extra
    return d

# ---------------------------------------------------------------- twin groups (tier 1 unless noted)
G_SMALLVAN_ALLIANCE = ["Renault Kangoo Van", "Mercedes-Benz Citan", "Nissan Townstar"]
G_SMALLMPV_ALLIANCE = ["Renault Kangoo", "Mercedes-Benz T-Class", "Mercedes-Benz EQT", "Nissan Townstar Kombi"]
G_K9_VAN = ["Peugeot Partner", "Citroën Berlingo Van", "Opel/Vauxhall Combo Cargo", "Fiat Doblò Cargo", "Toyota Proace City"]
G_K9_MPV = ["Peugeot Rifter", "Citroën Berlingo", "Opel/Vauxhall Combo", "Fiat Qubo", "Toyota Proace City Verso"]
G_K0_VAN = ["Peugeot Expert", "Citroën Jumpy", "Opel/Vauxhall Vivaro", "Fiat Scudo", "Toyota Proace", "Iveco eJolly"]
G_K0_MPV = ["Peugeot Traveller", "Citroën SpaceTourer", "Opel/Vauxhall Zafira", "Fiat Ulysse", "Toyota Proace Verso"]
G_SEVEL = ["Peugeot Boxer", "Citroën Jumper", "Opel/Vauxhall Movano", "Fiat Ducato", "Toyota Proace Max", "Iveco eSuperJolly"]
G_TRAFIC_VAN = ["Renault Trafic", "Nissan Primastar", "Renault Trucks Trafic"]
G_TRAFIC_MPV = ["Renault Trafic Passenger", "Nissan Primastar Kombi"]
G_MASTER = ["Renault Master", "Nissan Interstar", "Renault Trucks Master"]
G_CUSTOM_VAN = ["Ford Transit Custom", "Volkswagen Transporter"]
G_CUSTOM_MPV = ["Ford Tourneo Custom", "Volkswagen Caravelle"]
G_CADDY_VAN = ["Volkswagen Caddy Cargo", "Ford Transit Connect"]
G_CADDY_MPV = ["Volkswagen Caddy", "Ford Tourneo Connect"]
G_CRAFTER = ["Volkswagen Crafter", "MAN TGE", "Volkswagen Grand California"]
G_RANGER = ["Ford Ranger", "Volkswagen Amarok"]
G_W447_MPV = ["Mercedes-Benz V-Class", "Mercedes-Benz Vito Tourer", "Mercedes-Benz EQV", "Mercedes-Benz Marco Polo"]
G_MULTIVAN = ["Volkswagen Multivan", "Volkswagen California"]
G_FLEXIS = ["Renault Trafic E-Tech", "Renault Estafette E-Tech", "Renault Goelette E-Tech"]  # tier 2
G_TRAFIC4 = ["Renault Trafic E-Tech", "Renault Trucks E-Tech Trafic"]  # tier 1 (2027)

def others(group, me):
    return [x for x in group if x != me]

SRC_KANGOO_TWINS = [W+"Renault_Kangoo", W+"Mercedes-Benz_Citan", W+"Nissan_Townstar"]
SRC_K9_TWINS = [W+"Citro%C3%ABn_Berlingo", W+"Toyota_ProAce_City", W+"Fiat_Dobl%C3%B2"]
SRC_K0_TWINS = [W+"Citro%C3%ABn_Jumpy", W+"Toyota_ProAce", W+"Fiat_Scudo"]
SRC_SEVEL_TWINS = [W+"Fiat_Ducato", W+"Toyota_ProAce_Max", W+"Opel_Movano"]
SRC_TRAFIC_TWINS = [W+"Renault_Trafic", W+"Nissan_Primastar"]
SRC_MASTER_TWINS = [W+"Renault_Master", W+"Nissan_Interstar"]
SRC_CUSTOM_TWINS = [W+"Ford_Transit_Custom", W+"Volkswagen_Transporter_(T7)"]
SRC_CADDY_TWINS = [W+"Ford_Transit_Connect", W+"Volkswagen_Caddy"]
SRC_CRAFTER_TWINS = [W+"Volkswagen_Crafter", W+"MAN_TGE"]
SRC_RANGER_TWINS = [W+"Volkswagen_Amarok", W+"Ford_Ranger_(T6)"]
SRC_W447 = [W+"Mercedes-Benz_Vito", W+"Mercedes-Benz_V-Class"]

models = []
announced = []
discontinued = []

# =================================================================== RENAULT GROUP
models.append(m(brand="Renault", group="Renault Group", model="Kangoo Van", display="Kangoo Van",
    other_names=["Kangoo Van E-Tech (electric)", "Grand Kangoo Van (LWB)"],
    ch_on_sale=True, ch_source=RENAULT_CH_VANS, row="van-small", body="panel van (2 lengths), crew van",
    generation="III (2021–)", length_mm=4486, platform="CMF-C/D (Renault–Nissan–Mitsubishi Alliance)",
    powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Listed with prices and configurator on renault.ch (vans page) on 2026-10-21: Kangoo Van petrol/diesel from CHF 20'900 and Kangoo Van E-Tech electric from CHF 24'453.",
    status_sources=[RENAULT_CH_VANS, W+"Renault_Kangoo"],
    twin_tier=1, twin_members=others(G_SMALLVAN_ALLIANCE, "Renault Kangoo Van"),
    twin_note="Same body shell as Mercedes-Benz Citan (W420) and Nissan Townstar; all three built by Renault at Maubeuge (MCA). Passenger versions form the matching mpv-small group.",
    twin_sources=SRC_KANGOO_TWINS,
    carsized_slug="renault-kangoo-2021-5-door-van",
    carsized_side="https://www.carsized.com/resources/renault/kangoo/d/2021/sm_311134115_renault-kangoo-2021-side-view_4x.png",
    carsized_front=None, carsized_years="2021-present",
    commons_category="Category:Renault Kangoo III", commons_file=None, wikipedia_en="Renault Kangoo",
    notes="Wikipedia (fetched 2026-10-22): revealed 12 Nov 2020, sales early 2021, E-Tech van in production June 2022; lengths 4486 (L1) / 4910 (L2); TCe 130 petrol, Blue dCi 95/115 diesel, 45 kWh E-Tech; built at Maubeuge (MCA). carsized entry is the 5-door van body (same shell). Front image id not fetched (budget)."))

models.append(m(brand="Renault", group="Renault Group", model="Kangoo", display="Kangoo",
    other_names=["Grand Kangoo (7-seat LWB, sold as its own model name in CH)", "Kangoo E-Tech (electric)"],
    ch_on_sale=True, ch_source="https://de.renault.ch/personenwagen/kangoo.html", row="mpv-small",
    body="leisure activity vehicle (5-seat; Grand Kangoo 7-seat LWB)", generation="III (2021–)", length_mm=4486,
    platform="CMF-C/D (Alliance)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Passenger Kangoo (petrol, electric) and Grand Kangoo (petrol, electric) listed in the renault.ch model menu on 2026-10-21 (Kangoo 4.49 m, Grand Kangoo 4.91 m).",
    status_sources=[RENAULT_CH_HOME],
    twin_tier=1, twin_members=others(G_SMALLMPV_ALLIANCE, "Renault Kangoo"),
    twin_note="Same body as Mercedes-Benz T-Class/EQT and Nissan Townstar Kombi (all built at Maubeuge).",
    twin_sources=SRC_KANGOO_TWINS,
    carsized_slug="renault-kangoo-2021-5-door-van",
    carsized_side="https://www.carsized.com/resources/renault/kangoo/d/2021/sm_311134115_renault-kangoo-2021-side-view_4x.png",
    carsized_front=None, carsized_years="2021-present",
    commons_category="Category:Renault Kangoo III", commons_file=None, wikipedia_en="Renault Kangoo",
    notes="Grand Kangoo folded into this tile as the LWB body style (brief rule 4); could be split if the chart wants it."))

models.append(m(brand="Renault", group="Renault Group", model="Trafic", display="Trafic Van",
    other_names=["Trafic Van", "Trafic Van E-Tech (electric, gen III)"], ch_on_sale=True, ch_source=RENAULT_CH_VANS,
    row="van-mid", body="panel van (L1/L2, H1/H2), crew van, platform cab", generation="III (X82, 2014–; facelifts 2019, 2021, 2024)",
    length_mm=5080, platform="Renault X82 (own LCV platform)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Trafic Van (diesel) listed from CHF 33'800 with configurator on renault.ch on 2026-10-21. Gen-III electric 'Trafic Van E-Tech' (52 kWh, presented IAA 2022) no longer listed in CH in Oct 2026 — its successor is the gen-IV Trafic E-Tech (on sale H1 2027, see announced).",
    status_sources=[RENAULT_CH_VANS, W+"Renault_Trafic"],
    twin_tier=1, twin_members=others(G_TRAFIC_VAN, "Renault Trafic"),
    twin_note="Nissan Primastar (2022–) is a rebadged Trafic III built by Renault at Sandouville. Renault Trucks sells the same van through its truck network since 2022 ('Trafic Red Edition'). Former twins Fiat Talento (supply ended Sept 2020) and Mitsubishi Express (AU/NZ, 2020–22) are gone.",
    twin_sources=SRC_TRAFIC_TWINS + [RT_PR],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Renault Trafic III", commons_file=None, wikipedia_en="Renault Trafic",
    notes="Lengths 5080 (L1) / 5480 (L2) per Wikipedia (post-2021 facelift bumpers). Gen III stays on sale until the Flexis-based gen IV (electric only) arrives in 2027."))

announced.append(m(brand="Renault", group="Renault Group", model="Trafic E-Tech", display="Trafic E-Tech (new, 2027)",
    other_names=["Neuer Trafic Van E-Tech (CH)", "Trafic E-Tech electric"], ch_on_sale=False, ch_source=RENAULT_CH_TRAFIC_EV,
    row="van-mid", body="panel van (L1/L2) and platform cab, electric only", generation="IV (2027–)", length_mm=4870,
    platform="Flexis 'FlexEVan' SDV skateboard (Renault/Ampere/Volvo Group JV, 800 V)", powertrains=["BEV"], status="announced",
    status_note="Listed as 'NEUER TRAFIC VAN E-TECH' on the Swiss vans page on 2026-10-21 but without price or configurator ('Händler kontaktieren', 'Homologation noch ausstehend'). The Renault Trucks press release of 15 Sep 2026 says the twin E-Tech Trafic 'will go on sale in Europe in the first half of 2027'. Expected on sale H1 2027.",
    status_sources=[RENAULT_CH_VANS, RENAULT_CH_TRAFIC_EV, RT_PR],
    twin_tier=1, twin_members=others(G_TRAFIC4, "Renault Trafic E-Tech"),
    twin_note="Renault Trucks E-Tech Trafic (2027) is the badge-engineered version (same body, rear motor, 800 V). Tier-2 platform siblings on the same skateboard: Estafette E-Tech (high-roof van) and Goelette E-Tech (chassis cab).",
    twin_sources=[RT_PR, W+"Renault_Estafette"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Renault Trafic",
    notes="4.87 m (L1) / 5.27 m (L2), height under 1.90 m, 5.1–5.8 m³, payload up to 1,250 kg, up to 470 km WLTP (pending homologation), 15–80 % in ~20 min. Kept separate from the diesel Trafic III tile because the twin relationships differ."))

models.append(m(brand="Renault", group="Renault Group", model="Trafic Passenger", display="Trafic Passenger / SpaceClass",
    other_names=["Trafic Combi (DE/FR)", "Trafic SpaceClass (premium version)", "Trafic Passenger (UK)"],
    ch_on_sale=True, ch_source="https://de.renault.ch/personenwagen/trafic.html", row="mpv-large",
    body="8/9-seat people carrier (Combi) and SpaceClass lounge version", generation="III (X82, 2014–; facelifts 2019, 2021)",
    length_mm=5080, platform="Renault X82", powertrains=["diesel"], status="on_sale",
    status_note="'Trafic Passenger' (5.1 m) and 'Trafic SpaceClass', both diesel, listed in the renault.ch model menu on 2026-10-21.",
    status_sources=[RENAULT_CH_HOME, W+"Renault_Trafic"],
    twin_tier=1, twin_members=others(G_TRAFIC_MPV, "Renault Trafic Passenger"),
    twin_note="Nissan Primastar Kombi is the rebadged passenger Trafic III.", twin_sources=SRC_TRAFIC_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Renault Trafic III", commons_file=None, wikipedia_en="Renault Trafic",
    notes="SpaceClass treated as a trim of the passenger Trafic (one tile)."))

models.append(m(brand="Renault", group="Renault Group", model="Master", display="Master",
    other_names=["Master E-Tech (electric)", "Master Kastenwagen / Fahrgestell / Plattform / Brücke / Kipper / Koffer (CH body names)"],
    ch_on_sale=True, ch_source=RENAULT_CH_VANS, row="van-large",
    body="panel van, chassis cab, platform cab, tipper, box van, minibus (3.1–4.0 t; 3.5 t class)", generation="IV (2024–)",
    length_mm=5050, platform="Renault Master IV (new 'Aerovan' architecture)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Master Kastenwagen (diesel from CHF 42'550), Master electric (from CHF 62'100), chassis/platform, tipper and box versions all listed with configurators on renault.ch on 2026-10-21. Gen IV unveiled 21 Nov 2023 (Solutrans, Lyon), International Van of the Year 2025. Hydrogen H2-Tech version (Hyvia) not available after Hyvia's 2025 liquidation — VERIFY.",
    status_sources=[RENAULT_CH_VANS, W+"Renault_Master"],
    twin_tier=1, twin_members=others(G_MASTER, "Renault Master"),
    twin_note="Nissan Interstar (2024–) and Renault Trucks Master are rebadges of the Master IV, all built at Batilly.", twin_sources=SRC_MASTER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Renault Master IV", commons_file=None, wikipedia_en="Renault Master",
    notes="Length 5050 (L1) to ~6300 mm (L3); heavier >3.5 t variants exist but the 3.5 t versions dominate."))

announced.append(m(brand="Renault", group="Renault Group", model="Estafette E-Tech", display="Estafette E-Tech",
    other_names=[], ch_on_sale=False, ch_source=RENAULT_CH_VANS, row="van-mid",
    body="high-roof (2.6 m) walk-through delivery van, electric only", generation="I (2026–)", length_mm=5270,
    platform="Flexis SDV skateboard (Renault/Ampere, 800 V)", powertrains=["BEV"], status="announced",
    status_note="Shown as the Estafette concept at IAA Transportation 2024 (Hanover) as the first FlexEVan-platform vehicle (Flexis = Renault/Volvo Group JV), production 'in two years', i.e. 2026/27. Not on the Swiss vans page on 2026-10-21 and the sister Trafic E-Tech only goes on sale in H1 2027, so the Estafette is treated as announced (expected 2027).",
    status_sources=[RENAULT_CH_VANS, W+"Renault_Estafette"],
    twin_tier=2, twin_members=others(G_FLEXIS, "Renault Estafette E-Tech"),
    twin_note="Flexis skateboard shared with Trafic E-Tech (gen IV) and Goelette E-Tech; distinct tall body.", twin_sources=[W+"Renault_Estafette"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Renault Estafette",
    notes="Length 5.27 m, height 2.60 m, ~3.1–3.5 t GVW; last-mile delivery van."))

announced.append(m(brand="Renault", group="Renault Group", model="Goelette E-Tech", display="Goelette E-Tech",
    other_names=[], ch_on_sale=False, ch_source=RENAULT_CH_VANS, row="van-mid",
    body="chassis cab / platform cab (tipper, box, flatbed), electric only", generation="I (2026/27–)", length_mm=5300,
    platform="Flexis SDV skateboard (Renault/Ampere, 800 V)", powertrains=["BEV"], status="announced",
    status_note="Announced with the Estafette/Trafic E-Tech family (Flexis skateboard); scheduled after the Trafic E-Tech (H1 2027), i.e. 2027. Not listed in CH on 2026-10-21.",
    status_sources=[RENAULT_CH_VANS, W+"Renault_Estafette"],
    twin_tier=2, twin_members=others(G_FLEXIS, "Renault Goelette E-Tech"),
    twin_note="Chassis-cab sibling of the Trafic E-Tech / Estafette E-Tech on the Flexis skateboard.", twin_sources=[W+"Renault_Estafette"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Renault Goélette",
    notes="Placed in van-mid with its Flexis siblings (twin groups must share a row); it is a mid-size chassis cab, not a 3.5 t Master-class one."))

# =================================================================== VOLVO GROUP (Renault Trucks)
models.append(m(brand="Renault Trucks", group="Volvo Group", model="Master", display="Master (Renault Trucks)",
    other_names=["Master Red Edition", "Master E-Tech"], ch_on_sale=None, ch_source=None, row="van-large",
    body="panel van, chassis cab, platform cab (3.5 t class)", generation="IV (2024–)", length_mm=5050,
    platform="Renault Master IV", powertrains=["diesel","BEV"], status="on_sale",
    status_note="renault-trucks.com LCV page (fetched 2026-10-22) lists the 'Renault Trucks Master Red EDITION' (panel van, crew van, chassis/platform cab; dCi 2.0 110–170 hp diesel or 100 % electric; 3.5–4.5 t GVW) — the page does not state the generation, assumed to be the Master IV supplied since 2024.",
    status_sources=[RT_LCV, RT_PR, W+"Renault_Master"],
    twin_tier=1, twin_members=others(G_MASTER, "Renault Trucks Master"),
    twin_note="Identical to the Renault Master IV apart from badging and Renault Trucks-specific packs.", twin_sources=SRC_MASTER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Renault Master IV", commons_file=None, wikipedia_en="Renault Master",
    notes="Use the Renault Master images (same vehicle)."))

models.append(m(brand="Renault Trucks", group="Volvo Group", model="Trafic", display="Trafic (Renault Trucks)",
    other_names=["Trafic Red Edition"], ch_on_sale=None, ch_source=None, row="van-mid",
    body="panel van, crew van, platform cab, combi", generation="III (X82, 2014–)", length_mm=5080, platform="Renault X82", powertrains=["diesel"], status="on_sale",
    status_note="renault-trucks.com LCV page (fetched 2026-10-22) lists the 'Renault Trucks Trafic Red EDITION' (van, crew van, platform cab, combi; dCi 2.0 110–170 hp diesel; 2.8–3.1 t GVW); sold since 2022 (Wikipedia). Its electric successor, the Renault Trucks E-Tech Trafic, goes on sale in H1 2027 (see announced).",
    status_sources=[RT_LCV, RT_PR, W+"Renault_Trafic"],
    twin_tier=1, twin_members=others(G_TRAFIC_VAN, "Renault Trucks Trafic"),
    twin_note="Rebadged Renault Trafic III.", twin_sources=SRC_TRAFIC_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Renault Trafic III", commons_file=None, wikipedia_en="Renault Trafic",
    notes="Use the Renault Trafic III images (same vehicle)."))

announced.append(m(brand="Renault Trucks", group="Volvo Group", model="E-Tech Trafic", display="E-Tech Trafic (2027)",
    other_names=[], ch_on_sale=None, ch_source=None, row="van-mid",
    body="electric panel van (L1/L2) and platform cab", generation="I (2027–; Renault Trafic IV based)", length_mm=4870,
    platform="Flexis FlexEVan skateboard (800 V)", powertrains=["BEV"], status="announced",
    status_note="Press release 15 Sep 2026: new Renault Trucks E-Tech Trafic 'will go on sale in Europe in the first half of 2027' (up to 470 km WLTP pending homologation, 4.87/5.27 m, 5.1/5.8 m³).",
    status_sources=[RT_PR],
    twin_tier=1, twin_members=others(G_TRAFIC4, "Renault Trucks E-Tech Trafic"),
    twin_note="Rebadged new Renault Trafic E-Tech (gen IV).", twin_sources=[RT_PR],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Renault Trafic", notes=""))

# =================================================================== NISSAN
models.append(m(brand="Nissan", group="Nissan", model="Townstar", display="Townstar",
    other_names=["Townstar Van", "Townstar EV / Townstar Elektro"], ch_on_sale=True, ch_source=NISSAN_CH, row="van-small",
    body="panel van (L1/L2)", generation="I (2022–)", length_mm=4488, platform="CMF-C/D (Alliance)",
    powertrains=["petrol","BEV"], status="on_sale",
    status_note="Townstar and Townstar Elektro listed under Nutzfahrzeuge on nissan.ch on 2026-10-21. Revealed Sept 2021 as the Kangoo III rebadge replacing NV200/NV250/e-NV200.",
    status_sources=[NISSAN_CH, W+"Nissan_Townstar"],
    twin_tier=1, twin_members=others(G_SMALLVAN_ALLIANCE, "Nissan Townstar"),
    twin_note="Rebadged Renault Kangoo III built at Maubeuge (replaced NV250/e-NV200).", twin_sources=SRC_KANGOO_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Nissan Townstar", commons_file=None, wikipedia_en="Nissan Townstar",
    notes="No diesel (petrol 1.3 DIG-T or 45 kWh EV)."))

models.append(m(brand="Nissan", group="Nissan", model="Townstar Kombi", display="Townstar Kombi",
    other_names=["Townstar Combi (UK/FR)", "Townstar EV Kombi"], ch_on_sale=True, ch_source="https://de.nissan.ch/fahrzeuge/neuwagen/townstar-combi.html",
    row="mpv-small", body="5-seat leisure activity vehicle", generation="I (2022–)", length_mm=4488, platform="CMF-C/D (Alliance)",
    powertrains=["petrol","BEV"], status="on_sale",
    status_note="'Townstar Kombi' listed under Personenwagen on nissan.ch on 2026-10-21.", status_sources=[NISSAN_CH],
    twin_tier=1, twin_members=others(G_SMALLMPV_ALLIANCE, "Nissan Townstar Kombi"),
    twin_note="Passenger Kangoo III twin (with Mercedes T-Class/EQT).", twin_sources=SRC_KANGOO_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Nissan Townstar", commons_file=None, wikipedia_en="Nissan Townstar", notes=""))

models.append(m(brand="Nissan", group="Nissan", model="Primastar", display="Primastar",
    other_names=["Primastar Van"], ch_on_sale=True, ch_source="https://de.nissan.ch/fahrzeuge/neuwagen/primastar.html", row="van-mid",
    body="panel van (L1/L2, H1/H2), crew van, platform cab", generation="I (2022–; Trafic III based)", length_mm=5080,
    platform="Renault X82", powertrains=["diesel"], status="on_sale",
    status_note="Primastar listed under Nutzfahrzeuge on nissan.ch on 2026-10-21. Diesel only (no EV version in Europe).", status_sources=[NISSAN_CH, W+"Nissan_Primastar"],
    twin_tier=1, twin_members=others(G_TRAFIC_VAN, "Nissan Primastar"),
    twin_note="Rebadged Renault Trafic III (successor of the NV300), built at Sandouville.", twin_sources=SRC_TRAFIC_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Nissan Primastar (2021)", commons_file=None, wikipedia_en="Nissan Primastar",
    notes="Wikipedia (fetched 2026-10-21) lists it as 2022–present; VERIFY Commons category name."))

models.append(m(brand="Nissan", group="Nissan", model="Primastar Kombi", display="Primastar Kombi",
    other_names=["Primastar Combi (UK)"], ch_on_sale=True, ch_source="https://de.nissan.ch/fahrzeuge/neuwagen/primastar/primastar-kombi.html",
    row="mpv-large", body="8/9-seat people carrier", generation="I (2022–)", length_mm=5080, platform="Renault X82",
    powertrains=["diesel"], status="on_sale",
    status_note="'Primastar Kombi' listed under Personenwagen on nissan.ch on 2026-10-21.", status_sources=[NISSAN_CH],
    twin_tier=1, twin_members=others(G_TRAFIC_MPV, "Nissan Primastar Kombi"),
    twin_note="Rebadged Renault Trafic Combi/Passenger.", twin_sources=SRC_TRAFIC_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Nissan Primastar (2021)", commons_file=None, wikipedia_en="Nissan Primastar", notes=""))

models.append(m(brand="Nissan", group="Nissan", model="Interstar", display="Interstar",
    other_names=["Interstar-e (electric)"], ch_on_sale=True, ch_source="https://de.nissan.ch/fahrzeuge/neuwagen/neuer-interstar.html", row="van-large",
    body="panel van, chassis cab, platform cab (3.5 t class)", generation="I (2024–; Master IV based)", length_mm=5050,
    platform="Renault Master IV", powertrains=["diesel","BEV"], status="on_sale",
    status_note="'Interstar' (page slug 'neuer-interstar') listed under Nutzfahrzeuge on nissan.ch on 2026-10-21; new generation unveiled Feb 2024 (France launch 24 Feb 2024), incl. Interstar-e.", status_sources=[NISSAN_CH, W+"Nissan_Interstar"],
    twin_tier=1, twin_members=others(G_MASTER, "Nissan Interstar"),
    twin_note="Rebadged Renault Master IV built at Batilly (replaced the NV400/previous Interstar).", twin_sources=SRC_MASTER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Nissan Interstar (2024)", commons_file=None, wikipedia_en="Nissan Interstar",
    notes="VERIFY Commons category name."))

discontinued.append({"brand": "Nissan", "model": "Navara", "note": "European production (Barcelona) ended December 2021 and the model was withdrawn from Europe; the new 2025 Mitsubishi Triton-based Navara is sold in Oceania/other markets only. Not on nissan.ch (2026-10-21).", "source": NISSAN_CH})

# =================================================================== MERCEDES-BENZ GROUP
models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="Citan", display="Citan / eCitan",
    other_names=["eCitan (electric)"], ch_on_sale=None, ch_source=None, row="van-small",
    body="panel van (standard / long), crew van (Tourer)", generation="II (W420, 2021–2026)", length_mm=4498,
    platform="CMF-C/D (Alliance)", powertrains=["petrol","diesel","BEV"], status="runout",
    status_note="In April 2025 Mercedes-Benz executives announced the discontinuation of the Citan, eCitan, T-Class and EQT in 2026 (Motor1, cited on Wikipedia; infobox 'production to 2026'). Treated as runout in Oct 2026 — whether order books are still open could not be checked (mercedes-benz-vans.ch blocks fetching).",
    status_sources=[W+"Mercedes-Benz_Citan", W+"Mercedes-Benz_T-Class"],
    twin_tier=1, twin_members=others(G_SMALLVAN_ALLIANCE, "Mercedes-Benz Citan"),
    twin_note="Co-developed with Renault; same body as Kangoo III/Townstar, built at Maubeuge with Mercedes-specific front, interior and chassis tuning.", twin_sources=SRC_KANGOO_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz W420", commons_file=None, wikipedia_en="Mercedes-Benz Citan",
    notes="Long version 4922 mm."))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="T-Class", display="T-Class",
    other_names=["T-Klasse (DE/CH)", "Classe T (FR/IT)"], ch_on_sale=None, ch_source=None, row="mpv-small",
    body="5-seat leisure activity vehicle (standard / long)", generation="I (W420, 2022–2026)", length_mm=4498,
    platform="CMF-C/D (Alliance)", powertrains=["petrol","diesel"], status="runout",
    status_note="Launched April 2022; Mercedes announced in April 2025 that the T-Class and EQT (with Citan/eCitan) are discontinued in 2026 (Motor1 via Wikipedia). Treated as runout in Oct 2026.",
    status_sources=[W+"Mercedes-Benz_T-Class"],
    twin_tier=1, twin_members=others(G_SMALLMPV_ALLIANCE, "Mercedes-Benz T-Class"),
    twin_note="Passenger Kangoo III twin (built at Maubeuge).", twin_sources=SRC_KANGOO_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz T-Class", commons_file=None, wikipedia_en="Mercedes-Benz T-Class", notes=""))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="EQT", display="EQT",
    other_names=[], ch_on_sale=None, ch_source=None, row="mpv-small",
    body="5-seat electric leisure activity vehicle (standard / long), also Marco Polo Module camper", generation="I (W420, 2022–2026)", length_mm=4498,
    platform="CMF-C/D (Alliance)", powertrains=["BEV"], status="runout",
    status_note="Production EQT unveiled Dec 2022 (45 kWh, 90 kW, Kangoo E-Tech drivetrain); discontinuation in 2026 announced April 2025 (see T-Class). Treated as runout.", status_sources=[W+"Mercedes-Benz_T-Class"],
    twin_tier=1, twin_members=others(G_SMALLMPV_ALLIANCE, "Mercedes-Benz EQT"),
    twin_note="Electric T-Class = Kangoo E-Tech twin; separate nameplate kept as its own tile (same logic as EQV).", twin_sources=SRC_KANGOO_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz EQT", commons_file=None, wikipedia_en="Mercedes-Benz T-Class", notes=""))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="Vito", display="Vito / eVito",
    other_names=["eVito (electric)", "Vito Mixto (crew van)"], ch_on_sale=None, ch_source=None, row="van-mid",
    body="panel van (compact/long/extra-long), crew van", generation="III (W447, 2014–; facelifts 2020, 2024)", length_mm=5140,
    platform="Mercedes-Benz W447 (FWD/RWD/4MATIC)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): W447 launched March 2014, facelifts 2020 and MY2024 (revealed 27 Jul 2023), eVito with 90 kWh battery from March 2025; no end of production announced (only the US Metris ended 2023). Swiss site robots-blocked.",
    status_sources=[W+"Mercedes-Benz_Vito"],
    twin_tier=None, twin_members=[], twin_note="No other-brand twin. Same body as the V-Class/EQV/Vito Tourer, which sit in mpv-large.", twin_sources=SRC_W447,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz W447", commons_file=None, wikipedia_en="Mercedes-Benz Vito",
    notes="Lengths 4895 / 5140 / 5370 mm."))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="Vito Tourer", display="Vito Tourer",
    other_names=["eVito Tourer"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="up to 9-seat people carrier (Tourer Base/Pro/Select)", generation="III (W447, 2014–; facelifts 2020, 2024)", length_mm=5140,
    platform="Mercedes-Benz W447", powertrains=["diesel","BEV"], status="on_sale",
    status_note="VERIFY (site blocked). Passenger body style of the Vito; listed as a separate tile because the brief's mpv-large row names it.",
    status_sources=[W+"Mercedes-Benz_Vito"],
    twin_tier=1, twin_members=others(G_W447_MPV, "Mercedes-Benz Vito Tourer"),
    twin_note="Same body as V-Class/EQV with Vito trim.", twin_sources=SRC_W447,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz W447", commons_file=None, wikipedia_en="Mercedes-Benz Vito",
    notes="Could be merged into the Vito tile if one tile per nameplate is enforced strictly."))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="V-Class", display="V-Class",
    other_names=["V-Klasse (DE/CH)", "Classe V (FR/IT)"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="luxury MPV (compact/long/extra-long), Marco Polo camper derivative", generation="II (W447, 2014–; facelifts 2019, 2024)", length_mm=5140,
    platform="Mercedes-Benz W447", powertrains=["diesel"], status="on_sale",
    status_note="MY2024 facelift (revealed 27 Jul 2023); the electric VLE (VAN.EA, production since June 2026) is listed on Wikipedia as successor of the EQV only — the diesel V-Class is assumed to continue in 2026 (VERIFY on mercedes-benz.ch).",
    status_sources=[W+"Mercedes-Benz_V-Class", W+"Mercedes-Benz_VLE"],
    twin_tier=1, twin_members=others(G_W447_MPV, "Mercedes-Benz V-Class"),
    twin_note="Same body as Vito Tourer and EQV (electric).", twin_sources=SRC_W447,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz V-Class (W447)", commons_file=None, wikipedia_en="Mercedes-Benz V-Class", notes=""))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="EQV", display="EQV",
    other_names=[], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="electric luxury MPV (long/extra-long)", generation="I (W447-based, 2020–; facelift 2024)", length_mm=5140,
    platform="Mercedes-Benz W447 (eVito/EQV electric drive)", powertrains=["BEV"], status="runout",
    status_note="EQV (2020–; 90 kWh usable, facelift 2024) is named as the predecessor of the VLE, whose series production started in June 2026 — treated as runout; VERIFY whether EQV orders are still open.", status_sources=[W+"Mercedes-Benz_V-Class", W+"Mercedes-Benz_VLE"],
    twin_tier=1, twin_members=others(G_W447_MPV, "Mercedes-Benz EQV"),
    twin_note="Electric V-Class (same body).", twin_sources=SRC_W447,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz EQV", commons_file=None, wikipedia_en="Mercedes-Benz EQV", notes=""))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="Marco Polo", display="Marco Polo (camper)",
    other_names=["V-Class Marco Polo"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="factory camper van (pop-up roof) on the V-Class", generation="W447 (2014–; facelift 2024)", length_mm=5140,
    platform="Mercedes-Benz W447", powertrains=["diesel"], status="on_sale",
    status_note="FACTORY CAMPER — optional tile; drop if campers are out of scope. VERIFY 2026 listing.", status_sources=[W+"Mercedes-Benz_V-Class"],
    twin_tier=1, twin_members=others(G_W447_MPV, "Mercedes-Benz Marco Polo"),
    twin_note="V-Class body with camper interior.", twin_sources=SRC_W447,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz Marco Polo", commons_file=None, wikipedia_en="Mercedes-Benz V-Class", notes=""))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="Sprinter", display="Sprinter / eSprinter",
    other_names=["eSprinter (electric)", "Sprinter Tourer (minibus)"], ch_on_sale=None, ch_source=None, row="van-large",
    body="panel van, chassis cab, platform cab, crew van, minibus (3.0–5.5 t; 3.5 t class)", generation="III (W907/W910 'VS30', 2018–; eSprinter 2.0 from 2023)", length_mm=5931,
    platform="Mercedes-Benz W907 (RWD/AWD; FWD W910 dropped in Europe spring 2024)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): debuted 6 Feb 2018, sales June 2018; petrol and FWD versions discontinued 2024; eSprinter 2.0 (81/113 kWh, RWD) since 2023. No successor announced. Swiss site robots-blocked.", status_sources=[W+"Mercedes-Benz_Sprinter"],
    twin_tier=None, twin_members=[], twin_note="No twin since the VW Crafter split in 2017.", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz W907", commons_file=None, wikipedia_en="Mercedes-Benz Sprinter",
    notes="Lengths 5931 / 6967 / 7366 mm (plus compact 5267). Commons category name to be confirmed."))

models.append(m(brand="Mercedes-Benz", group="Mercedes-Benz Group", model="VLE", display="VLE",
    other_names=["VLE 300", "VLE 400 4MATIC"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="electric large luxury MPV (SWB/LWB), up to 8 seats", generation="I (2026–)", length_mm=5309,
    platform="VAN.EA (800 V)", powertrains=["BEV"], status="on_sale",
    status_note="Production VLE revealed 10 March 2026 (concept Vision V 22 Apr 2025); series production started June 2026 (electrive, cited on Wikipedia). Order opening date not found — treated as on sale from the production start; VERIFY on mercedes-benz.de/.ch.",
    status_sources=[W+"Mercedes-Benz_VLE"],
    twin_tier=None, twin_members=[], twin_note="Successor of the EQV; the longer, more luxurious VLS is sold alongside; a VAN.EA Vito successor is expected later. Petrol/diesel VLE versions planned later in the lifecycle.", twin_sources=[W+"Mercedes-Benz_VLE"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mercedes-Benz VLE", commons_file=None, wikipedia_en="Mercedes-Benz VLE",
    notes="5309 mm (SWB) / 5484 mm (LWB). VLE 300 FWD, VLE 400 4MATIC dual motor."))

# =================================================================== VOLKSWAGEN GROUP
models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Caddy Cargo", display="Caddy Cargo",
    other_names=["Caddy Cargo Maxi (LWB)"], ch_on_sale=None, ch_source=None, row="van-small",
    body="panel van (SWB / Maxi)", generation="Typ SB ('Caddy 5', 2020–; 'Caddy 2026' facelift-level update, launch autumn 2026)", length_mm=4500,
    platform="MQB (VW Group)", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) shows 'Der neue Caddy Cargo' alongside the 'Caddy 2026' (facelift-level product upgrade, 'bereits bestellbar', market launch autumn 2026; eHybrid PHEV up to 122 km electric). Wikipedia: on sale since Nov 2020, TGI CNG added 2022 (CNG availability in 2026 unverified, not listed). Swiss site robots-blocked.", status_sources=[VWN_DE, VWN_DE_CADDY, W+"Volkswagen_Caddy"],
    twin_tier=1, twin_members=others(G_CADDY_VAN, "Volkswagen Caddy Cargo"),
    twin_note="Ford Transit Connect (2024–) is a rebadged Caddy Cargo built by VW in Poznań (Ford–VW alliance).", twin_sources=SRC_CADDY_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Caddy V", commons_file=None, wikipedia_en="Volkswagen Caddy",
    notes="Maxi 4859 mm. Commons category name to be confirmed (Wikipedia counts this as the 4th generation, Typ SB)."))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Caddy", display="Caddy",
    other_names=["Caddy Maxi (LWB, 7 seats)", "Caddy California (micro-camper)", "Caddy Life"], ch_on_sale=None, ch_source=None, row="mpv-small",
    body="5/7-seat leisure activity vehicle (Caddy / Caddy Maxi); Caddy California camper", generation="Typ SB ('Caddy 5', 2020–; 'Caddy 2026' facelift-level update, launch autumn 2026)", length_mm=4500,
    platform="MQB (VW Group)", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de Caddy page (fetched 2026-10-22): 'Der neue Caddy' = Caddy 2026 product upgrade (new bumper, 12.9-inch display, Travel Assist 3.0), 'bereits bestellbar', market launch autumn 2026, 75–90 kW engines plus eHybrid plug-in hybrid (up to 122 km electric), from €34,201. Swiss site robots-blocked.", status_sources=[VWN_DE_CADDY, W+"Volkswagen_Caddy"],
    twin_tier=1, twin_members=others(G_CADDY_MPV, "Volkswagen Caddy"),
    twin_note="Ford Tourneo Connect (2022–) is the rebadged passenger Caddy built in Poznań.", twin_sources=SRC_CADDY_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Caddy V", commons_file=None, wikipedia_en="Volkswagen Caddy", notes=""))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Transporter", display="Transporter (T7)",
    other_names=["Transporter Kastenwagen / Kombi / Pritsche", "e-Transporter (electric)"], ch_on_sale=None, ch_source=None, row="van-mid",
    body="panel van (L1/L2, H1/H2), kombi, single/double-cab chassis", generation="'T7' (2024/25–; Ford-built; VW does not officially use the T7 code for it)", length_mm=5050,
    platform="Ford Transit Custom (2023) platform", powertrains=["diesel","PHEV","BEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) lists the Transporter as diesel, plug-in hybrid or fully electric. Wikipedia: unveiled Aug 2024 on the Ford Transit Custom basis; e-Transporter 64 kWh, PHEV 16.5 kWh. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_Transporter_(T7)"],
    twin_tier=1, twin_members=others(G_CUSTOM_VAN, "Volkswagen Transporter"),
    twin_note="Rebadged Ford Transit Custom built by Ford Otosan in Kocaeli (Ford–VW alliance); the MQB Multivan T7 is NOT related.", twin_sources=SRC_CUSTOM_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Transporter (T7)", commons_file=None, wikipedia_en="Volkswagen Transporter (T7)",
    notes="Lengths 5050 / 5450 mm."))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Caravelle", display="Caravelle (T7)",
    other_names=["e-Caravelle"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="up to 9-seat people carrier", generation="'T7' (2024/25–; Ford-built)", length_mm=5050,
    platform="Ford Transit Custom (2023) platform", powertrains=["diesel","PHEV","BEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de Caravelle page (fetched 2026-10-22): 'neueste Generation', two wheelbases, up to 9 seats, 81–210 kW, diesel / plug-in hybrid (later) / fully electric, from €53,830. Wikipedia: unveiled Aug 2024 with the Transporter (Tourneo Custom basis). Swiss site robots-blocked.", status_sources=[VWN_DE_CARAVELLE, W+"Volkswagen_Transporter_(T7)"],
    twin_tier=1, twin_members=others(G_CUSTOM_MPV, "Volkswagen Caravelle"),
    twin_note="Rebadged Ford Tourneo Custom (Kocaeli).", twin_sources=SRC_CUSTOM_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Transporter (T7)", commons_file=None, wikipedia_en="Volkswagen Transporter (T7)", notes=""))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Multivan", display="Multivan (T7)",
    other_names=["Multivan eHybrid"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="7-seat MPV (standard / long)", generation="T7 (2021–; MQB)", length_mm=4973,
    platform="MQB evo (VW Group)", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) promotes 'Der neue Multivan' (updated model). Wikipedia: Multivan T7 debuted mid-2021 on MQB. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_Transporter_(T7)", W+"Volkswagen_California"],
    twin_tier=1, twin_members=others(G_MULTIVAN, "Volkswagen Multivan"),
    twin_note="Own MQB body (not the Ford-based Transporter/Caravelle T7). The California T7 is a Multivan with camper interior.", twin_sources=[W+"Volkswagen_Multivan_(T7)"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Multivan (T7)", commons_file=None, wikipedia_en="Volkswagen Multivan (T7)",
    notes="Long version 5173 mm."))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="California", display="California (T7)",
    other_names=["California Beach / Coast / Ocean"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="factory camper van (pop-up roof) on the long Multivan T7", generation="T7 (2024–)", length_mm=5173,
    platform="MQB evo (VW Group)", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="FACTORY CAMPER — optional tile; drop if campers are out of scope. volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) lists 'Der neue California'; Wikipedia: California (Multivan-based) launched 2024, LWB only, PHEV/diesel/petrol.", status_sources=[VWN_DE, W+"Volkswagen_California"],
    twin_tier=1, twin_members=others(G_MULTIVAN, "Volkswagen California"),
    twin_note="Multivan T7 body with camper fit-out.", twin_sources=[W+"Volkswagen_Multivan_(T7)"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen California (T7)", commons_file=None, wikipedia_en="Volkswagen California", notes=""))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="ID. Buzz", display="ID. Buzz",
    other_names=["ID. Buzz LWB (7-seat)", "ID. Buzz GTX"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="electric MPV (SWB 5-seat / LWB 6–7-seat)", generation="I (2022–)", length_mm=4712,
    platform="MEB (VW Group)", powertrains=["BEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) lists ID. Buzz / ID. Buzz Pro. Wikipedia: production since June 2022 (Hanover), LWB (4962 mm, 86 kWh) and GTX added 2024. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_ID._Buzz"],
    twin_tier=None, twin_members=[], twin_note="Cargo version shares the body (van-mid row). MEB platform siblings (ID.4 etc.) are in other rows. An ID. Buzz California camper was announced (2025/26).", twin_sources=[W+"Volkswagen_ID._Buzz"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen ID. Buzz", commons_file=None, wikipedia_en="Volkswagen ID. Buzz",
    notes="LWB 4962 mm."))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="ID. Buzz Cargo", display="ID. Buzz Cargo",
    other_names=[], ch_on_sale=None, ch_source=None, row="van-mid",
    body="electric panel van (SWB)", generation="I (2022–)", length_mm=4712,
    platform="MEB (VW Group)", powertrains=["BEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de (fetched 2026-10-22) names the ID. Buzz Cargo. Wikipedia: first Cargo delivered 15 Nov 2022; SWB only, 3.9 m³, 3.0 t GVW. Swiss site robots-blocked.", status_sources=[VWN_DE, W+"Volkswagen_ID._Buzz"],
    twin_tier=None, twin_members=[], twin_note="Panel-van body style of the ID. Buzz (mpv-large).", twin_sources=[W+"Volkswagen_ID._Buzz"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen ID. Buzz", commons_file=None, wikipedia_en="Volkswagen ID. Buzz", notes=""))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Crafter", display="Crafter / e-Crafter",
    other_names=["e-Crafter (electric, new 2025)"], ch_on_sale=None, ch_source=None, row="van-large",
    body="panel van, chassis cab, platform cab, kombi (3.0–5.5 t; 3.5 t class)", generation="II (SY/SZ, 2017–; facelift 2024)", length_mm=5986,
    platform="Volkswagen Crafter II (FWD/RWD/4MOTION)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="volkswagen-nutzfahrzeuge.de Crafter page (fetched 2026-10-22): 'Der neue Crafter' (2024 facelift with Digital Cockpit Pro; technical data file 'crafter_2024'), panel van / dropside / chassis cab in three lengths, from €43,920 net; the page lists only 2.0 TDI — e-Crafter not named there (BEV kept from the 2024/25 e-Crafter announcement, unverified). Swiss site robots-blocked.", status_sources=[VWN_DE_CRAFTER, W+"Volkswagen_Crafter"],
    twin_tier=1, twin_members=others(G_CRAFTER, "Volkswagen Crafter"),
    twin_note="MAN TGE is the badge-engineered Crafter II (both built in Września); Grand California is the Crafter camper.", twin_sources=SRC_CRAFTER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Crafter II", commons_file=None, wikipedia_en="Volkswagen Crafter",
    notes="Lengths 5986 / 6836 / 7391 mm."))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Grand California", display="Grand California (camper)",
    other_names=["Grand California 600 / 680"], ch_on_sale=None, ch_source=None, row="van-large",
    body="factory motorhome on the Crafter (3.5 t)", generation="I (2019–; facelift 2024)", length_mm=5986,
    platform="Volkswagen Crafter II", powertrains=["diesel"], status="on_sale",
    status_note="FACTORY CAMPER — optional tile; drop if campers are out of scope. Grand California 600/680 on sale since 2019 (Wikipedia Crafter/California articles, fetched 2026-10-22); 2026 listing not separately verified.", status_sources=[W+"Volkswagen_California", W+"Volkswagen_Crafter"],
    twin_tier=1, twin_members=others(G_CRAFTER, "Volkswagen Grand California"),
    twin_note="Crafter body with motorhome fit-out.", twin_sources=SRC_CRAFTER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Grand California", commons_file=None, wikipedia_en="Volkswagen California", notes=""))

models.append(m(brand="Volkswagen", group="Volkswagen Group", model="Amarok", display="Amarok",
    other_names=["Amarok PanAmericana / Aventura"], ch_on_sale=None, ch_source=None, row="pickup",
    body="double-cab (and single-cab in some markets) pickup", generation="II (2023–; Ford Ranger based)", length_mm=5350,
    platform="Ford T6.2 (body-on-frame)", powertrains=["diesel"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): released 7 July 2022, built by Ford in Silverton (Pretoria) on the Ranger P703 platform; 'Dark Label' edition reintroduced for Europe Nov 2025. Swiss site robots-blocked.", status_sources=[W+"Volkswagen_Amarok"],
    twin_tier=1, twin_members=others(G_RANGER, "Volkswagen Amarok"),
    twin_note="Developed with and built by Ford (Silverton, South Africa) on the Ranger T6.2; VW-specific styling.", twin_sources=SRC_RANGER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Volkswagen Amarok II", commons_file=None, wikipedia_en="Volkswagen Amarok",
    notes="Europe: 2.0 TDI and 3.0 V6 TDI only; the 2.3 TSI petrol is for other markets; no PHEV/electrified Amarok (Wikipedia)."))

models.append(m(brand="MAN", group="Volkswagen Group", model="TGE", display="TGE / eTGE",
    other_names=["eTGE (electric)"], ch_on_sale=None, ch_source=None, row="van-large",
    body="panel van, chassis cab, platform cab, kombi (3.0–5.5 t; 3.5 t class)", generation="I (2017–; facelift 2024)", length_mm=5986,
    platform="Volkswagen Crafter II", powertrains=["diesel","BEV"], status="on_sale",
    status_note="MAN Truck & Bus sells the Crafter II as the TGE (panel van, tipper, dropside, crew cab) — Wikipedia Crafter article (fetched 2026-10-22); eTGE since July 2018, new eTGE on the e-Crafter basis from 2025 — VERIFY. man.eu home page lists trucks/buses only.", status_sources=[W+"Volkswagen_Crafter", W+"MAN_TGE"],
    twin_tier=1, twin_members=others(G_CRAFTER, "MAN TGE"),
    twin_note="Badge-engineered VW Crafter II (MAN grille/badges), built in Września.", twin_sources=SRC_CRAFTER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:MAN TGE", commons_file=None, wikipedia_en="MAN TGE", notes=""))

# =================================================================== FORD
models.append(m(brand="Ford", group="Ford", model="Transit Courier", display="Transit Courier",
    other_names=["E-Transit Courier (electric)"], ch_on_sale=None, ch_source=None, row="van-small",
    body="compact panel van", generation="II (2023/24–)", length_mm=4337,
    platform="Ford B2E (Puma-derived)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="ford.de Nutzfahrzeuge page (fetched 2026-10-22) lists the E-Transit Courier; Wikipedia: E-Transit Courier unveiled 6 Apr 2023, production from late 2024 at Craiova; 1.0/1.5 engines. ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Transit_Courier"],
    twin_tier=None, twin_members=[], twin_note="Ford-only (Puma/B2E based), built in Craiova.", twin_sources=[W+"Ford_Transit_Courier"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Transit Courier II", commons_file=None, wikipedia_en="Ford Transit Courier", notes=""))

models.append(m(brand="Ford", group="Ford", model="Tourneo Courier", display="Tourneo Courier",
    other_names=["E-Tourneo Courier (electric)"], ch_on_sale=None, ch_source=None, row="mpv-small",
    body="5-seat compact leisure activity vehicle", generation="II (2023/24–)", length_mm=4337,
    platform="Ford B2E (Puma-derived)", powertrains=["petrol","BEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): Tourneo Courier unveiled 15 May 2023 (incl. Active trim and E-Tourneo Courier). ford.ch could not be fetched.", status_sources=[W+"Ford_Transit_Courier"],
    twin_tier=None, twin_members=[], twin_note="Ford-only.", twin_sources=[W+"Ford_Transit_Courier"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Tourneo Courier II", commons_file=None, wikipedia_en="Ford Transit Courier", notes=""))

models.append(m(brand="Ford", group="Ford", model="Transit Connect", display="Transit Connect",
    other_names=["Transit Connect L2 (LWB)", "Transit Connect PHEV"], ch_on_sale=None, ch_source=None, row="van-small",
    body="panel van (SWB / LWB)", generation="III (2024–; VW Caddy based)", length_mm=4500,
    platform="MQB (VW Group), built by VW in Poznań", powertrains=["diesel","PHEV"], status="on_sale",
    status_note="ford.de Transit Connect page (fetched 2026-10-22): current model with configurator, price list and stock vehicles (from €209/month); EcoBlue diesel 102/122 PS (optional AWD) and plug-in hybrid (110 kW, up to 117 km electric); L1 3.1 m³ / L2 3.7 m³, Kastenwagen and FlexCab. Wikipedia: Caddy-based generation released late 2024. The 'Connect to be axed' rumour is not supported by the German site.",
    status_sources=[FORD_DE_CONNECT, W+"Ford_Transit_Connect"],
    twin_tier=1, twin_members=others(G_CADDY_VAN, "Ford Transit Connect"),
    twin_note="Rebadged VW Caddy Cargo (Ford–VW alliance) with Ford front/interior details.", twin_sources=SRC_CADDY_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Transit Connect III", commons_file=None, wikipedia_en="Ford Transit Connect",
    notes="Lengths 4500 / 4859 mm (Wikipedia)."))

models.append(m(brand="Ford", group="Ford", model="Tourneo Connect", display="Tourneo Connect",
    other_names=["Grand Tourneo Connect (LWB, 7 seats)", "Tourneo Connect PHEV"], ch_on_sale=None, ch_source=None, row="mpv-small",
    body="5/7-seat leisure activity vehicle", generation="III (2022–; VW Caddy based)", length_mm=4500,
    platform="MQB (VW Group), built in Poznań", powertrains=["petrol","diesel","PHEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-21): launched Oct 2021 as a rebadged Caddy, 2021–present; the sister Transit Connect is a current model on ford.de (Oct 2026) with diesel and PHEV, so the Tourneo Connect is assumed current too (its own 2026 page not fetched).",
    status_sources=[W+"Ford_Transit_Connect", FORD_DE_CONNECT],
    twin_tier=1, twin_members=others(G_CADDY_MPV, "Ford Tourneo Connect"),
    twin_note="Rebadged passenger VW Caddy.", twin_sources=SRC_CADDY_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Tourneo Connect III", commons_file=None, wikipedia_en="Ford Transit Connect", notes=""))

models.append(m(brand="Ford", group="Ford", model="Transit Custom", display="Transit Custom",
    other_names=["E-Transit Custom (electric)", "Transit Custom PHEV", "Transit Custom Nugget (camper)"], ch_on_sale=None, ch_source=None, row="van-mid",
    body="panel van (L1/L2, H1/H2), double-cab-in-van, kombi, chassis (Trail/Sport/MS-RT trims)", generation="II (2023–)", length_mm=5050,
    platform="Ford Transit Custom (2023) platform", powertrains=["diesel","MHEV","PHEV","BEV"], status="on_sale",
    status_note="ford.de (fetched 2026-10-22) lists the E-Transit Custom; Wikipedia: unveiled Sept 2022, built by Ford Otosan from 2023; diesel, mild-hybrid, PHEV and E-Transit Custom (74 kWh usable). ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Transit_Custom"],
    twin_tier=1, twin_members=others(G_CUSTOM_VAN, "Ford Transit Custom"),
    twin_note="VW Transporter T7 is the rebadged Transit Custom (both built by Ford Otosan, Kocaeli).", twin_sources=SRC_CUSTOM_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Transit Custom II", commons_file=None, wikipedia_en="Ford Transit Custom",
    notes="Lengths 5050 / 5450 mm."))

models.append(m(brand="Ford", group="Ford", model="Tourneo Custom", display="Tourneo Custom",
    other_names=["E-Tourneo Custom (electric)", "Tourneo Custom PHEV"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="8/9-seat people carrier (L1/L2)", generation="II (2023–)", length_mm=5050,
    platform="Ford Transit Custom (2023) platform", powertrains=["diesel","PHEV","BEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): Tourneo Custom revealed 22 Nov 2022 (Active, Nugget camper, E-Tourneo Custom). ford.ch could not be fetched.", status_sources=[W+"Ford_Transit_Custom"],
    twin_tier=1, twin_members=others(G_CUSTOM_MPV, "Ford Tourneo Custom"),
    twin_note="VW Caravelle T7 is the rebadged Tourneo Custom.", twin_sources=SRC_CUSTOM_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Tourneo Custom II", commons_file=None, wikipedia_en="Ford Transit Custom", notes=""))

models.append(m(brand="Ford", group="Ford", model="Transit", display="Transit / E-Transit",
    other_names=["E-Transit (electric)", "Transit Van / Kombi / Chassis Cab / Minibus"], ch_on_sale=None, ch_source=None, row="van-large",
    body="panel van, chassis cab, double cab, minibus (2.9–4.7 t; 3.5 t class)", generation="IV (V363, 2014–; facelift 2019; E-Transit 2022; updates 2024/25)", length_mm=5981,
    platform="Ford Transit V363 (FWD/RWD/AWD)", powertrains=["diesel","MHEV","BEV"], status="on_sale",
    status_note="ford.de (fetched 2026-10-22) lists the E-Transit (incl. skeletal chassis); Wikipedia: 4th generation since 2013/14, 2020 revision (2.0 EcoBlue incl. 48 V mHEV), E-Transit for Europe built at Ford Otosan since April 2022, 89 kWh from 2024; no successor named. ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Transit"],
    twin_tier=None, twin_members=[], twin_note="No twin.", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Transit (2014)", commons_file=None, wikipedia_en="Ford Transit",
    notes="Lengths 5530–5590 / 5980–6040 / 6700 mm (regular/long/extended). Commons category name to be confirmed."))

models.append(m(brand="Ford", group="Ford", model="Ranger", display="Ranger",
    other_names=["Ranger Raptor", "Ranger PHEV", "Ranger Wildtrak / Platinum / Tremor / MS-RT"], ch_on_sale=None, ch_source=None, row="pickup",
    body="double-cab (also super/regular cab) pickup", generation="T6.2 (2022/23–)", length_mm=5370,
    platform="Ford T6.2 (body-on-frame)", powertrains=["diesel","petrol","PHEV"], status="on_sale",
    status_note="ford.de (fetched 2026-10-22) lists the Ranger Plug-in-Hybrid; Wikipedia: European launch Nov 2022; 2.0 EcoBlue / 3.0 V6 diesel, Raptor 3.0 EcoBoost petrol (210 kW in EU); Ranger PHEV (2.3 EcoBoost + 11.7 kWh) unveiled Sept 2023; Ranger Super Duty planned for Europe before end-2026 (same nameplate). ford.ch could not be fetched.", status_sources=[FORD_DE, W+"Ford_Ranger_(T6)"],
    twin_tier=1, twin_members=others(G_RANGER, "Ford Ranger"),
    twin_note="VW Amarok II shares body-in-white/platform (co-developed, built by Ford Silverton).", twin_sources=SRC_RANGER_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ford Ranger (T6.2)", commons_file=None, wikipedia_en="Ford Ranger (T6)",
    notes="Raptor and Super Duty are the same tile. Length 5225–5370 mm (Raptor 5381). Commons category name to be confirmed."))

announced.append(m(brand="Ford", group="Ford", model="Transit City", display="Transit City (new)",
    other_names=[], ch_on_sale=None, ch_source=None, row="van-mid",
    body="electric panel van (short / medium wheelbase, 6–8 m³) and chassis cab", generation="I (2026/27–)", length_mm=None,
    platform="Ford/JMC (related to the JMC E-Fushun; built with Jiangling Motors)", powertrains=["BEV"], status="announced",
    status_note="ford.de (fetched 2026-10-22) presents 'Der neue Ford Transit City': 56 kWh LFP battery, 110 kW, up to 254 km, payload up to 1,085 kg (SWB) / 1,275 kg (MWB) / 1,600 kg (chassis), 10–80 % in 33 min, financing 'ab 279 €'; only 'Angebot anfragen' / newsletter, video tagged 'pre-launch', no order date — treated as announced (launch 2026/27). Wikipedia Transit article: 'In 2026 Ford, partnering with Jiangling Motors, will release the Transit City'.",
    status_sources=[FORD_DE_CITY, FORD_DE, W+"Ford_Transit"],
    twin_tier=None, twin_members=[], twin_note="JMC-built; no European twin. Positioned between Transit Custom and Transit (6–8 m³).", twin_sources=[W+"Ford_Transit"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Ford Transit", notes="Length not published on the DE page; row provisional (8 m³ MWB is at the mid/large boundary)."))

# =================================================================== STELLANTIS — PEUGEOT
models.append(m(brand="Peugeot", group="Stellantis", model="Partner", display="Partner",
    other_names=["E-Partner (electric)", "Partner Premium Long (CH)"], ch_on_sale=True, ch_source=PEUGEOT_CH_PRO,
    row="van-small", body="panel van (Standard / Long), crew van", generation="III (K9, 2018–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Partner / E-Partner listed with business offers (from CHF 20,990 net, valid to 30.11.2026) on peugeot.ch (fetched 2026-10-22). Facelifted (new face, i-Cockpit) early 2024.", status_sources=[PEUGEOT_CH_PRO, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_VAN, "Peugeot Partner"),
    twin_note="K9 family: Partner/Berlingo/Combo/Doblò/Proace City share body and EMP2 front end (built at Vigo, Mangualde, Ellesmere Port, Bursa). Wikipedia Berlingo article (fetched 2026-10-22) lists all rebadges incl. the 2026 Fiat Qubo.", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Peugeot Partner III", commons_file=None, wikipedia_en="Peugeot Partner",
    notes="Lengths 4403 / 4753 mm."))

models.append(m(brand="Peugeot", group="Stellantis", model="Rifter", display="Rifter",
    other_names=["E-Rifter (electric)", "Rifter Long (7 seats)"], ch_on_sale=None, ch_source=None, row="mpv-small",
    body="5/7-seat leisure activity vehicle", generation="I (K9, 2018–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Rifter/E-Rifter is a current K9 passenger model (Wikipedia Berlingo article, fetched 2026-10-22; 2024 facelift); not shown on the Swiss pages fetched (home, business offers) — Swiss listing unverified.", status_sources=[W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_MPV, "Peugeot Rifter"),
    twin_note="Passenger K9 twin of Berlingo/Combo/Doblò/Proace City Verso.", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Peugeot Rifter", commons_file=None, wikipedia_en="Peugeot Rifter", notes=""))

models.append(m(brand="Peugeot", group="Stellantis", model="Expert", display="Expert",
    other_names=["E-Expert (electric)"], ch_on_sale=True, ch_source=PEUGEOT_CH_PRO, row="van-mid",
    body="panel van (Compact / Standard / Long), crew van, platform cab", generation="III (K0, 2016–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Expert / E-Expert listed with business offers (from CHF 26,990 net, valid to 30.11.2026) on peugeot.ch (fetched 2026-10-22).", status_sources=[PEUGEOT_CH_PRO, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_VAN, "Peugeot Expert"),
    twin_note="K0 family (Hordain/Lieu-Saint-Amand; Luton until 2025, Ellesmere Port from 2026): Expert/Jumpy/Vivaro/Scudo/Proace + Iveco eJolly (2025, electric). e-Expert Hydrogen (FCEV) shown 2021 but Stellantis ended its hydrogen programme in 2025.", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Peugeot Expert III", commons_file=None, wikipedia_en="Peugeot Expert",
    notes="Lengths 4609 (Compact) / 4959 (Standard) / 5309 (Long) mm per Wikipedia (post-2024-facelift brochures quote 4981/5331). 2026 engines: 1.5 BlueHDi 120 and 2.2 BlueHDi 150/180."))

models.append(m(brand="Peugeot", group="Stellantis", model="Traveller", display="Traveller",
    other_names=["E-Traveller (electric)"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="5–9-seat people carrier (Standard / Long)", generation="I (K0, 2016–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Since Jan 2022 Stellantis sells the Traveller/SpaceTourer/Zafira Life passenger vans in Europe only as electric (E-Traveller), except in Switzerland and the Balkans where diesel continues (Wikipedia Jumpy article, fetched 2026-10-22). Not shown on the Swiss pages fetched — Swiss listing unverified.", status_sources=[W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_MPV, "Peugeot Traveller"),
    twin_note="Passenger K0 twin of SpaceTourer/Zafira/Ulysse/Proace Verso.", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Peugeot Traveller", commons_file=None, wikipedia_en="Peugeot Traveller", notes=""))

models.append(m(brand="Peugeot", group="Stellantis", model="Boxer", display="Boxer",
    other_names=["E-Boxer (electric)"], ch_on_sale=True, ch_source=PEUGEOT_CH_PRO, row="van-large",
    body="panel van (L1–L4, H1–H3), chassis cab, platform cab, minibus (3.0–4.0 t; 3.5 t class)", generation="III (X250/X290, 2006–; facelifts 2014, 2024)", length_mm=5413,
    platform="Sevel X290 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Boxer / E-Boxer listed with business offers (from CHF 37,990 net, valid to 30.11.2026) on peugeot.ch (fetched 2026-10-22). 2024 facelift brought new front, interior and 110 kWh E-Boxer.", status_sources=[PEUGEOT_CH_PRO, W+"Fiat_Ducato"],
    twin_tier=1, twin_members=others(G_SEVEL, "Peugeot Boxer"),
    twin_note="Sevel Sud (Atessa) large-van family: Boxer/Jumper/Ducato + Movano (since 2021) + Proace Max (2023/24) + Iveco eSuperJolly (2025, electric).", twin_sources=SRC_SEVEL_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Peugeot Boxer III", commons_file=None, wikipedia_en="Peugeot Boxer",
    notes="Lengths 4963 / 5413 / 5998 / 6363 mm. VERIFY Commons category name."))

# =================================================================== STELLANTIS — CITROËN
models.append(m(brand="Citroën", group="Stellantis", model="Berlingo Van", display="Berlingo Van",
    other_names=["ë-Berlingo Van (electric)"], ch_on_sale=True, ch_source=CITROEN_CH_LCV, row="van-small",
    body="panel van (M / XL), crew van", generation="III (K9, 2018–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Berlingo Van and ë-Berlingo Van listed with configurator on citroen.ch Nutzfahrzeuge page on 2026-10-21 (two lengths, up to 4.4 m³). 2024 facelift revealed 23 Oct 2023; 1.2 PureTech 110 (122 PS MHEV from mid-2025), 1.5 BlueHDi 100/130, electric.", status_sources=[CITROEN_CH_LCV, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_VAN, "Citroën Berlingo Van"),
    twin_note="K9 family (Vigo/Mangualde).", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Citroën Berlingo III", commons_file=None, wikipedia_en="Citroën Berlingo", notes=""))

models.append(m(brand="Citroën", group="Stellantis", model="Berlingo", display="Berlingo",
    other_names=["ë-Berlingo (electric)", "Berlingo XL (7 seats)"], ch_on_sale=True, ch_source="https://www.citroen.ch/de/",
    row="mpv-small", body="5/7-seat leisure activity vehicle (M / XL)", generation="III (K9, 2018–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="'Berlingo' listed under 'Modelle kennenlernen' on citroen.ch on 2026-10-21 (passenger range).", status_sources=["https://www.citroen.ch/de/"],
    twin_tier=1, twin_members=others(G_K9_MPV, "Citroën Berlingo"),
    twin_note="Passenger K9 twin.", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Citroën Berlingo III", commons_file=None, wikipedia_en="Citroën Berlingo", notes=""))

models.append(m(brand="Citroën", group="Stellantis", model="Jumpy", display="Jumpy",
    other_names=["Dispatch (UK)", "ë-Jumpy (electric)", "ë-Jumpy Hydrogen"], ch_on_sale=True, ch_source=CITROEN_CH_LCV, row="van-mid",
    body="panel van (XS / M / XL), crew van, platform cab", generation="III (K0, 2016–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Jumpy and ë-Jumpy listed with configurator on citroen.ch on 2026-10-21. 2024 facelift (revealed 23 Oct 2023); new 1.5/2.2 BlueHDi engines from 2026; ë-Jumpy 75 kWh.", status_sources=[CITROEN_CH_LCV, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_VAN, "Citroën Jumpy"),
    twin_note="K0 family (Hordain/Luton).", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Citroën Jumpy III", commons_file=None, wikipedia_en="Citroën Jumpy", notes=""))

models.append(m(brand="Citroën", group="Stellantis", model="SpaceTourer", display="SpaceTourer",
    other_names=["ë-SpaceTourer (electric)"], ch_on_sale=True, ch_source=CITROEN_CH_SPACETOURER, row="mpv-large",
    body="5–9-seat people carrier (M / XL)", generation="I (K0, 2016–; facelift 2024)", length_mm=4983,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="citroen.ch ë-SpaceTourer page (fetched 2026-10-22): M (4,983 mm) and XL (5,333 mm), 8–9 seats, 49/75 kWh, from CHF 47,800 with configurator and an offer valid 1 Sep–31 Oct 2026; diesel SpaceTourer mentioned for CH. In most of Europe electric-only since Jan 2022 (Wikipedia Jumpy article).", status_sources=[CITROEN_CH_SPACETOURER, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_MPV, "Citroën SpaceTourer"),
    twin_note="Passenger K0 twin.", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Citroën SpaceTourer", commons_file=None, wikipedia_en="Citroën SpaceTourer", notes=""))

models.append(m(brand="Citroën", group="Stellantis", model="Jumper", display="Jumper",
    other_names=["Relay (UK)", "ë-Jumper (electric)"], ch_on_sale=True, ch_source=CITROEN_CH_LCV, row="van-large",
    body="panel van (L1–L4), chassis cab, platform cab, minibus (3.5 t class)", generation="III (X250/X290, 2006–; facelifts 2014, 2024)", length_mm=5413,
    platform="Sevel X290 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Jumper and ë-Jumper (420 km WLTP, 150 kW charging, 17 m³, 1,900 kg payload) listed with configurator on citroen.ch on 2026-10-21; 2024 facelift (revealed 23 Oct 2023).", status_sources=[CITROEN_CH_LCV, W+"Fiat_Ducato"],
    twin_tier=1, twin_members=others(G_SEVEL, "Citroën Jumper"),
    twin_note="Sevel Sud family.", twin_sources=SRC_SEVEL_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Citroën Jumper III", commons_file=None, wikipedia_en="Citroën Jumper", notes="VERIFY Commons category name."))

# =================================================================== STELLANTIS — OPEL/VAUXHALL
models.append(m(brand="Opel", group="Stellantis", model="Combo Cargo", display="Combo Cargo",
    other_names=["Vauxhall Combo / Combo Panel Van (UK)", "Combo Cargo Electric"], ch_on_sale=True, ch_source="https://www.opel.ch/de/vans/combo-models/cargo/model-overview.html",
    row="van-small", body="panel van (M / XL), crew van", generation="E (K9, 2018–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Combo Cargo and Combo Cargo Electric listed under Vans on opel.ch on 2026-10-21.", status_sources=[OPEL_CH],
    twin_tier=1, twin_members=others(G_K9_VAN, "Opel/Vauxhall Combo Cargo"),
    twin_note="K9 family (PSA-based since the 2018 'Combo E').", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Opel Combo E", commons_file=None, wikipedia_en="Opel Combo", notes=""))

models.append(m(brand="Opel", group="Stellantis", model="Combo", display="Combo (Life)",
    other_names=["Combo Life (pre-2024 name; still used by Vauxhall UK)", "Combo Electric", "Vauxhall Combo Life Electric (UK)"],
    ch_on_sale=True, ch_source="https://www.opel.ch/de/personenwagen/combo-modelle/combo/uebersicht.html", row="mpv-small",
    body="5/7-seat leisure activity vehicle", generation="E (K9, 2018–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="'Combo' and 'Combo Electric' listed under Personenwagen on opel.ch on 2026-10-21 (no 'Life' suffix any more).", status_sources=[OPEL_CH],
    twin_tier=1, twin_members=others(G_K9_MPV, "Opel/Vauxhall Combo"),
    twin_note="Passenger K9 twin.", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Opel Combo E", commons_file=None, wikipedia_en="Opel Combo", notes="Canonical twin name used across files: 'Opel/Vauxhall Combo'."))

models.append(m(brand="Opel", group="Stellantis", model="Vivaro", display="Vivaro",
    other_names=["Vauxhall Vivaro / Vivaro Panel Van (UK)", "Vivaro Electric"], ch_on_sale=True, ch_source="https://www.opel.ch/de/nutzfahrzeuge/vivaro-modelle/panel-van/uebersicht.html",
    row="van-mid", body="panel van (S / M / L), crew van, platform cab", generation="C (K0, 2019–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Vivaro and Vivaro Electric listed under Nutzfahrzeuge on opel.ch on 2026-10-21.", status_sources=[OPEL_CH],
    twin_tier=1, twin_members=others(G_K0_VAN, "Opel/Vauxhall Vivaro"),
    twin_note="K0 family (Luton builds the Vivaro).", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Opel Vivaro C", commons_file=None, wikipedia_en="Opel Vivaro", notes=""))

models.append(m(brand="Opel", group="Stellantis", model="Zafira", display="Zafira",
    other_names=["Zafira Life (pre-2024 name)", "Zafira Electric", "Vauxhall Vivaro Life Electric (UK)"], ch_on_sale=True,
    ch_source="https://www.opel.ch/de/personenwagen/zafira-modelle/zafira/uebersicht.html", row="mpv-large",
    body="5–9-seat people carrier (M / L)", generation="Zafira Life/K0 (2019–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="'Zafira' (diesel) and 'Zafira Electric' listed under Personenwagen on opel.ch on 2026-10-21 — Switzerland is one of the few markets that kept the combustion version after Stellantis' Jan 2022 electric-only decision for passenger K0 vans.", status_sources=[OPEL_CH, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_MPV, "Opel/Vauxhall Zafira"),
    twin_note="Passenger K0 twin.", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Opel Zafira Life", commons_file=None, wikipedia_en="Opel Zafira Life", notes=""))

models.append(m(brand="Opel", group="Stellantis", model="Movano", display="Movano",
    other_names=["Vauxhall Movano / Movano Panel Van (UK)", "Movano Electric"], ch_on_sale=True,
    ch_source="https://www.opel.ch/de/nutzfahrzeuge/movano-modelle/movano/uebersicht.html", row="van-large",
    body="panel van (L1–L4), chassis cab, platform cab (3.5 t class)", generation="C (X290-based, 2021–; facelift 2024)", length_mm=5413,
    platform="Sevel X290 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Movano and Movano Electric listed under Nutzfahrzeuge on opel.ch on 2026-10-21.", status_sources=[OPEL_CH],
    twin_tier=1, twin_members=others(G_SEVEL, "Opel/Vauxhall Movano"),
    twin_note="Since 2021 a Ducato/Boxer/Jumper rebadge (previously Renault Master based). Movano Hydrogen (announced Nov 2023) did not reach series sale after Stellantis ended its hydrogen programme in 2025.", twin_sources=SRC_SEVEL_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Opel Movano C", commons_file=None, wikipedia_en="Opel Movano", notes=""))

# =================================================================== STELLANTIS — FIAT (Fiat Professional)
models.append(m(brand="Fiat", group="Stellantis", model="Doblò Cargo", display="Doblò (Cargo)",
    other_names=["E-Doblò (electric)", "Doblò Van"], ch_on_sale=True, ch_source=FIAT_CH_PRO, row="van-small",
    body="panel van (L1 / L2), crew van", generation="III (K9, 2022–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Fiat Professional CH range page (fetched 2026-10-22) lists Doblò / E-Doblò (diesel, petrol or electric; E-Doblò from CHF 26,390 net, offer 1 Apr–30 Sep 2026); fiat.it lists Doblò (diesel/petrol) and E-Doblò. Doblò III = K9 rebadge since 2022 (Wikipedia Berlingo article).", status_sources=[FIAT_CH_PRO, FIAT_IT, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_VAN, "Fiat Doblò Cargo"),
    twin_note="Since 2022 the Doblò is a K9 (Berlingo) rebadge built at Vigo; previous Doblò was a Fiat design.", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Fiat Doblò III", commons_file=None, wikipedia_en="Fiat Doblò", notes=""))

models.append(m(brand="Fiat", group="Stellantis", model="Qubo", display="Qubo",
    other_names=["Qubo L (CH/IT model name)", "Doblò (passenger, 2022–2025 predecessor name)", "E-Doblò"], ch_on_sale=True, ch_source=FIAT_CH_QUBO,
    row="mpv-small", body="5/7-seat leisure activity vehicle (K9 body, 'Qubo L')", generation="III (K9, 2026–)", length_mm=4753,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="New for 2026: fiat.ch Qubo L page (fetched 2026-10-22) — 5 or 7 seats, electric 100 kW, automatic diesel 96 kW, manual petrol 81 kW, MY26 price list, 'Konfigurieren' button; fiat.it lists 'Qubo L' (Benzina, Elettrica, Diesel) in the passenger-car menu. Wikipedia's Berlingo article lists 'Fiat Qubo, 2026–present' among the K9 rebadges. It takes over the passenger role of the Doblò (no passenger Doblò/E-Doblò on fiat.it any more; in CH only via stock locator = runout).",
    status_sources=[FIAT_CH_QUBO, FIAT_IT, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_MPV, "Fiat Qubo"),
    twin_note="Passenger K9 twin (Berlingo/Rifter/Combo/Proace City Verso).", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Fiat Qubo",
    notes="Revives the Qubo name (2008–2024 Fiorino-based MPV). Only 'Qubo L' is listed in CH and IT (5/7 seats) — probably the long K9 body (4753 mm); the standard K9 body is 4403 mm."))

models.append(m(brand="Fiat", group="Stellantis", model="Scudo", display="Scudo",
    other_names=["E-Scudo (electric)"], ch_on_sale=True, ch_source=FIAT_CH_PRO, row="van-mid",
    body="panel van (L1 / L2), crew van, platform cab", generation="III (K0, 2022–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Fiat Professional CH range page (fetched 2026-10-22) lists Scudo / E-Scudo (E-Scudo from CHF 28,440 net); fiat.it lists Scudo (diesel) and E-Scudo. K0 rebadge since 2022 (Wikipedia Jumpy article).", status_sources=[FIAT_CH_PRO, FIAT_IT, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_VAN, "Fiat Scudo"),
    twin_note="Rebadged K0 van (replaced the Renault-based Talento in 2022).", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Fiat Scudo III", commons_file=None, wikipedia_en="Fiat Scudo", notes="VERIFY Commons category name."))

models.append(m(brand="Fiat", group="Stellantis", model="Ulysse", display="Ulysse",
    other_names=["E-Ulysse (electric)"], ch_on_sale=True, ch_source="https://www.fiat.ch/de/professional/models/ulysse-thermic", row="mpv-large",
    body="5–9-seat people carrier", generation="III (K0, 2022–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="fiat.ch (fetched 2026-10-22) lists 'Ulysse' (thermic) and 'E-Ulysse' under Professional with quote requests; fiat.it lists Ulysse Elettrica and Diesel. Ulysse (K0 rebadge) sold since 2022 (Wikipedia Jumpy article).", status_sources=[FIAT_CH, FIAT_IT, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_MPV, "Fiat Ulysse"),
    twin_note="Passenger K0 twin (SpaceTourer rebadge).", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Fiat Ulysse III", commons_file=None, wikipedia_en="Fiat Ulysse", notes="VERIFY Commons category name."))

models.append(m(brand="Fiat", group="Stellantis", model="Ducato", display="Ducato",
    other_names=["E-Ducato (electric)", "Fiat Camper (motorhome base)"], ch_on_sale=True, ch_source=FIAT_CH_PRO, row="van-large",
    body="panel van (L1–L4, H1–H3), chassis cab, platform cab, minibus, motorhome base (3.0–4.25 t; 3.5 t class)", generation="III (X250/X290, 2006–; facelifts 2014, 2021, 2024)", length_mm=5413,
    platform="Sevel X290 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Fiat Professional CH range page (fetched 2026-10-22) lists Ducato / E-Ducato (E-Ducato from CHF 49,581 net); fiat.it lists Ducato (diesel) and E-Ducato. Wikipedia: X290 since 2014, facelifts 2021 and 2024 (2.2 Multijet 120/140/180 PS, E-Ducato 110 kWh/200 kW).", status_sources=[FIAT_CH_PRO, FIAT_IT, W+"Fiat_Ducato"],
    twin_tier=1, twin_members=others(G_SEVEL, "Fiat Ducato"),
    twin_note="Sevel Sud family lead model (Atessa).", twin_sources=SRC_SEVEL_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Fiat Ducato III", commons_file=None, wikipedia_en="Fiat Ducato", notes="VERIFY Commons category name."))

# =================================================================== TOYOTA
models.append(m(brand="Toyota", group="Toyota Motor", model="Proace City", display="Proace City",
    other_names=["Proace City Electric"], ch_on_sale=None, ch_source=None, row="van-small",
    body="panel van (Short / Long), crew van", generation="I (K9, 2019/20–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Listed as 'Proace City' on toyota.co.uk new-cars overview (fetched 2026-10-22); K9 rebadge since 2019 (Wikipedia Berlingo article). toyota.ch/professional could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_VAN, "Toyota Proace City"),
    twin_note="K9 rebadge supplied by Stellantis (Vigo) under the Toyota–PSA LCV agreement.", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Toyota ProAce City", commons_file=None, wikipedia_en="Toyota ProAce City", notes=""))

models.append(m(brand="Toyota", group="Toyota Motor", model="Proace City Verso", display="Proace City Verso",
    other_names=["Proace City Verso Electric"], ch_on_sale=None, ch_source=None, row="mpv-small",
    body="5/7-seat leisure activity vehicle", generation="I (K9, 2019/20–; facelift 2024)", length_mm=4403,
    platform="EMP2 (Stellantis)", powertrains=["petrol","diesel","BEV"], status="on_sale",
    status_note="Listed as 'Proace City Verso' on toyota.co.uk (fetched 2026-10-22). toyota.ch could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Berlingo"],
    twin_tier=1, twin_members=others(G_K9_MPV, "Toyota Proace City Verso"),
    twin_note="Passenger K9 twin.", twin_sources=SRC_K9_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Toyota ProAce City Verso", commons_file=None, wikipedia_en="Toyota ProAce City", notes=""))

models.append(m(brand="Toyota", group="Toyota Motor", model="Proace", display="Proace",
    other_names=["Proace Electric"], ch_on_sale=None, ch_source=None, row="van-mid",
    body="panel van (Compact / Medium / Long), crew van, platform cab", generation="II (K0, 2016–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Listed as 'Proace' on toyota.co.uk (fetched 2026-10-22); K0 rebadge (Wikipedia Jumpy article). toyota.ch/professional could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_VAN, "Toyota Proace"),
    twin_note="K0 rebadge (Hordain).", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Toyota ProAce II", commons_file=None, wikipedia_en="Toyota ProAce", notes="VERIFY Commons category name."))

models.append(m(brand="Toyota", group="Toyota Motor", model="Proace Verso", display="Proace Verso",
    other_names=["Proace Verso Electric"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="5–9-seat people carrier (Medium / Long)", generation="II (K0, 2016–; facelift 2024)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Listed as 'Proace Verso' and 'Proace Verso Electric' on toyota.co.uk (fetched 2026-10-22); Toyota kept diesel passenger versions after Stellantis' 2022 electric-only decision (Wikipedia Jumpy article). toyota.ch could not be fetched.", status_sources=[TOYOTA_UK, W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_MPV, "Toyota Proace Verso"),
    twin_note="Passenger K0 twin.", twin_sources=SRC_K0_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Toyota ProAce Verso", commons_file=None, wikipedia_en="Toyota ProAce", notes=""))

models.append(m(brand="Toyota", group="Toyota Motor", model="Proace Max", display="Proace Max",
    other_names=["Proace Max Electric"], ch_on_sale=None, ch_source=None, row="van-large",
    body="panel van (L2–L4), chassis cab, platform cab (3.5 t class)", generation="I (X290, 2024–)", length_mm=5413,
    platform="Sevel X290 (Stellantis)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Listed as 'Proace Max' on toyota.co.uk (fetched 2026-10-22). Wikipedia: Toyota-badged Ducato (Sevel Sud) 2023–present, 2.2 diesel 120/140/180 PS and Proace Max Electric 110 kWh/200 kW. toyota.ch/professional could not be fetched.", status_sources=[TOYOTA_UK, W+"Toyota_ProAce_Max"],
    twin_tier=1, twin_members=others(G_SEVEL, "Toyota Proace Max"),
    twin_note="Rebadged Fiat Ducato (Atessa/Gliwice).", twin_sources=SRC_SEVEL_TWINS,
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Toyota ProAce Max", commons_file=None, wikipedia_en="Toyota ProAce Max", notes=""))

models.append(m(brand="Toyota", group="Toyota Motor", model="Hilux", display="Hilux (all-new)",
    other_names=["Hilux BEV (electric)", "Hilux Hybrid 48V"], ch_on_sale=None, ch_source=None, row="pickup",
    body="double-cab (also single/extra cab) pickup", generation="IX (2026–; replaces the 2015–2025 eighth generation)", length_mm=5320,
    platform="Toyota IMV (body-on-frame, updated)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="toyota.co.uk (fetched 2026-10-22) sells the 'All New Hilux' ('Build your All-New Hilux', from £34,670 ex VAT) with diesel (payload 1,065 kg, 3,500 kg towing) and battery-electric versions (up to 159 miles WLTP, £5,000 Electric Van Grant); '48V hybrid' appears only in page keywords. Eighth generation (Europe mid-2016–; facelift June 2020; 48 V mild hybrid from 2024) is therefore in runout/replaced — VERIFY in CH/DE.",
    status_sources=[TOYOTA_UK_HILUX, TOYOTA_UK, "https://de.wikipedia.org/wiki/Toyota_Hilux", W+"Toyota_Hilux"],
    twin_tier=None, twin_members=[], twin_note="No current twin in Europe.", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Toyota Hilux IX", commons_file=None, wikipedia_en="Toyota Hilux",
    notes="Length ~5.32 m (gen VIII double cab 5,320–5,325 mm; gen IX similar — VERIFY). Commons category for gen IX to be confirmed (gen VIII: Category:Toyota Hilux VIII). Land Cruiser Commercial (UK) is a body variant of the Land Cruiser (offroad row, other agent)."))

# =================================================================== OTHER PICKUPS
models.append(m(brand="Mitsubishi", group="Mitsubishi Motors", model="L200", display="L200",
    other_names=["Triton (other markets)"], ch_on_sale=None, ch_source=None, row="pickup",
    body="double-cab (and club-cab) pickup", generation="VI (2024– in Europe)", length_mm=5360,
    platform="Mitsubishi (ladder frame, 2023 Triton)", powertrains=["diesel"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): sixth-generation Triton sold in Europe as L200 (2.4 diesel 150/184/204 PS, 4WD); a UK 'L200 Commercial' two-seat double cab was introduced in response to the April 2025 BIK tax change (article dated 11 Sep 2026) — sales continuing in 2026.", status_sources=[W+"Mitsubishi_Triton"],
    twin_tier=None, twin_members=[], twin_note="The Triton-based Nissan Navara (D27, 2026–) is not sold in Europe.", twin_sources=[W+"Mitsubishi_Triton", W+"Nissan_Navara"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Mitsubishi Triton (2023)", commons_file=None, wikipedia_en="Mitsubishi Triton", notes="Double cab 5,320–5,360 mm. Commons category name to be confirmed."))

models.append(m(brand="Isuzu", group="Isuzu", model="D-Max", display="D-Max",
    other_names=["D-Max EV (electric, 2025)", "D-Max V-Cross / Arctic Trucks AT35"], ch_on_sale=None, ch_source=None, row="pickup",
    body="single/extended/double-cab pickup", generation="III (RG, 2020/21– in Europe; facelift 2023/24)", length_mm=5280,
    platform="Isuzu Dynamic Drive (body-on-frame)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): third generation since Oct 2019, UK sales from April 2021, facelift 2023/24; D-Max EV unveiled at the 2025 CV Show, production from April 2025 for selected European markets, UK deliveries Feb 2026. isuzu.ch is JS-only (not readable).", status_sources=[W+"Isuzu_D-Max"],
    twin_tier=None, twin_members=[], twin_note="Mazda BT-50 (D-Max twin) is not sold in Europe.", twin_sources=[W+"Isuzu_D-Max"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Isuzu D-Max III", commons_file=None, wikipedia_en="Isuzu D-Max", notes="Double cab 5,195–5,285 mm. Commons category name to be confirmed."))

models.append(m(brand="KGM", group="KG Mobility", model="Musso", display="Musso",
    other_names=["Musso Grand (LWB; not listed in UK Oct 2026)", "SsangYong Musso (pre-2023 brand name)", "Rexton Sports (Korea)"], ch_on_sale=None, ch_source=None, row="pickup",
    body="double-cab pickup (standard / Grand long bed)", generation="I (Q200/Q250, 2018–)", length_mm=5095,
    platform="SsangYong/KGM body-on-frame (Rexton-based)", powertrains=["diesel"], status="runout",
    status_note="Still listed and priced on kgm-motors.co.uk on 2026-10-22 ('Musso', from £32,980 ex VAT) alongside the 'All-new Musso Rhino' (Q300) — the Q200 is therefore in runout. kgm-motors.ch is robots-blocked.", status_sources=[KGM_UK, W+"SsangYong_Musso"],
    twin_tier=None, twin_members=[], twin_note="Rexton (offroad row) shares the chassis — different body, cross-row.", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:SsangYong Musso (Q200)", commons_file=None, wikipedia_en="SsangYong Musso", notes="Musso Grand 5405 mm. Commons category name to be confirmed."))

models.append(m(brand="KGM", group="KG Mobility", model="Musso Rhino", display="Musso Rhino (all-new)",
    other_names=["KGM Musso (Q300, Korea name)"], ch_on_sale=None, ch_source=None, row="pickup",
    body="double-cab pickup (Rhino / Rhino+ extended wheelbase 3,210 mm)", generation="II (Q300, 2026–)", length_mm=5400,
    platform="KGM body-on-frame (new Musso Q300)", powertrains=["diesel"], status="on_sale",
    status_note="kgm-motors.co.uk Musso Rhino page (fetched 2026-10-22): 'the all-new Musso Rhino', 2.2 turbo diesel 202 PS / 400 Nm, payload 1,090 kg (Rhino+ 1,200 kg), 3,500 kg towing, from £38,995 ex VAT; the Q300-generation Musso debuted in Korea in December 2025 (Wikipedia). Name in other European markets unverified.", status_sources=[KGM_UK_RHINO, KGM_UK, W+"SsangYong_Musso"],
    twin_tier=None, twin_members=[], twin_note="", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:KGM Musso", commons_file=None, wikipedia_en="SsangYong Musso", notes="Length approximate (not published). Could be merged with the Musso tile once the Q200 is gone."))

models.append(m(brand="KGM", group="KG Mobility", model="Musso EV", display="Musso EV",
    other_names=["KGM Musso EV (O100)"], ch_on_sale=None, ch_source=None, row="pickup",
    body="electric double-cab pickup", generation="I (O100, 2025–)", length_mm=5160,
    platform="KGM (unibody-style EV pickup, 80.6 kWh LFP blade battery)", powertrains=["BEV"], status="on_sale",
    status_note="Launched in Korea 5 March 2025 (Wikipedia); on sale in the UK — kgm-motors.co.uk (fetched 2026-10-22) lists 'Musso EV' from £39,995 inc VAT incl. £5,000 Plug-in Van Grant, tagged 'All-new'. Other European markets to VERIFY (kgm-motors.ch blocked).", status_sources=[KGM_UK, W+"KGM_Musso_EV"],
    twin_tier=None, twin_members=[], twin_note="Separate vehicle from the diesel Musso despite the shared name.", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:KGM Musso EV", commons_file=None, wikipedia_en="KGM Musso EV", notes="5160 mm, wheelbase 3150 mm; FWD 152 kW (420 km WLTP) or AWD 266 kW (380 km)."))

models.append(m(brand="Ineos", group="Ineos", model="Quartermaster", display="Grenadier Quartermaster",
    other_names=["Grenadier Quartermaster"], ch_on_sale=None, ch_source=None, row="pickup",
    body="double-cab pickup (also chassis cab)", generation="I (2023/24–)", length_mm=5400,
    platform="Ineos Grenadier ladder frame (BMW B57/B58 engines, ZF 8-speed)", powertrains=["petrol","diesel"], status="on_sale",
    status_note="ineosgrenadier.com UK page (fetched 2026-10-22) lists the 'GRENADIER Quartermaster' (double-cab off-road pickup) with test-drive link and offers for orders 1–31 Oct 2026; Wikipedia: introduced July 2023, 5,400 mm, 3,227 mm wheelbase.", status_sources=[INEOS_UK, W+"Ineos_Grenadier"],
    twin_tier=None, twin_members=[], twin_note="Pickup body of the Grenadier (offroad row, other agent) — cross-row, not grouped.", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Ineos Grenadier Quartermaster", commons_file=None, wikipedia_en="Ineos Grenadier", notes="VERIFY Commons category name."))

# =================================================================== HYUNDAI MOTOR GROUP
models.append(m(brand="Hyundai", group="Hyundai Motor Group", model="Staria", display="Staria",
    other_names=["Staria Wagon / Staria Premium (Signature)", "Staria Hybrid (not Europe)"], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="7/9-seat MPV / people carrier (Staria, Staria Premium/Lounge)", generation="I (US4, 2021–; facelift revealed 17 Dec 2025)", length_mm=5255,
    platform="Hyundai-Kia N3 (FWD/AWD, shared with Kia Carnival IV)", powertrains=["diesel","BEV"], status="on_sale",
    status_note="hyundai.com/de (fetched 2026-10-22) sells the 'neue STARIA Elektro' (160 kW, 84 kWh, up to 430 km, from €57,450, 'NEU'); the diesel 2.2 CRDi is not on the German page any more (diesel availability per market unverified). Wikipedia: facelift unveiled 17 Dec 2025, Staria Electric unveiled 9 Jan 2026. hyundai.ch could not be fetched.", status_sources=[HYUNDAI_DE_STARIA, W+"Hyundai_Staria"],
    twin_tier=None, twin_members=[], twin_note="Staria Van (cargo) shares the body — van-mid row.", twin_sources=[W+"Hyundai_Staria"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Hyundai Staria", commons_file=None, wikipedia_en="Hyundai Staria", notes=""))

models.append(m(brand="Hyundai", group="Hyundai Motor Group", model="Staria Van", display="Staria Van",
    other_names=["Staria Cargo", "Staria Kombi (crew van)"], ch_on_sale=None, ch_source=None, row="van-mid",
    body="3/6-seat panel/crew van (Staria Van / Cargo / Load)", generation="I (US4, 2021–; facelift 2025/26)", length_mm=5255,
    platform="Hyundai-Kia N3", powertrains=["diesel","BEV"], status="on_sale",
    status_note="hyundai.com/de (fetched 2026-10-22) sells the 'STARIA Cargo Elektro' (160 kW, 84 kWh, up to 450 km, from €57,454, 'NEU'); diesel Staria Van availability per market unverified. hyundai.ch could not be fetched.", status_sources=[HYUNDAI_DE_STARIA, W+"Hyundai_Staria"],
    twin_tier=None, twin_members=[], twin_note="Cargo body style of the Staria.", twin_sources=[W+"Hyundai_Staria"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Hyundai Staria", commons_file=None, wikipedia_en="Hyundai Staria", notes=""))

models.append(m(brand="Kia", group="Hyundai Motor Group", model="PV5 Cargo", display="PV5 Cargo",
    other_names=["PV5 Crew", "PV5 Chassis Cab"], ch_on_sale=True, ch_source="https://www.kia.ch/de/kia-pbv/fahrzeuge/pv5-cargo", row="van-mid",
    body="electric panel van (L2H1 / L2H2), crew van, chassis cab", generation="I (2025–)", length_mm=4695,
    platform="E-GMP.S (Hyundai-Kia PBV)", powertrains=["BEV"], status="on_sale",
    status_note="PV5 Cargo, PV5 Crew and PV5 Chassis Cab listed in the PBV section of kia.ch on 2026-10-21; European sales began November 2025 (>10,000 European sales by June 2026; Wikipedia fetched 2026-10-22).", status_sources=[KIA_CH, W+"Kia_PV5"],
    twin_tier=None, twin_members=[], twin_note="PV5 Passenger shares the body (mpv-large row).", twin_sources=[KIA_CH],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Kia PV5", commons_file=None, wikipedia_en="Kia PV5", notes=""))

models.append(m(brand="Kia", group="Hyundai Motor Group", model="PV5 Passenger", display="PV5 Passenger",
    other_names=["PV5 WAV (wheelchair accessible)"], ch_on_sale=True, ch_source="https://www.kia.ch/de/kia-pbv/fahrzeuge/pv5-passenger", row="mpv-large",
    body="5–7-seat electric MPV", generation="I (2025–)", length_mm=4695,
    platform="E-GMP.S (Hyundai-Kia PBV)", powertrains=["BEV"], status="on_sale",
    status_note="PV5 Passenger listed in the PBV section of kia.ch on 2026-10-21; European sales since November 2025 (Wikipedia).", status_sources=[KIA_CH, W+"Kia_PV5"],
    twin_tier=None, twin_members=[], twin_note="Passenger body of the PV5.", twin_sources=[KIA_CH],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Kia PV5", commons_file=None, wikipedia_en="Kia PV5",
    notes="4695 mm (standard) / 4890 mm (long); 43.3 kWh LFP (Europe), 51.5 / 71.2 kWh NCM. Below the mpv-large guide (~4.7 m) but the brief places PV5 Passenger in mpv-large."))

announced.append(m(brand="Kia", group="Hyundai Motor Group", model="PV7", display="PV7",
    other_names=[], ch_on_sale=False, ch_source="https://www.kia.ch/de/kia-pbv/fahrzeuge/pv7", row="van-large",
    body="electric large van (PBV)", generation="I (2027–)", length_mm=None,
    platform="E-GMP.S (Hyundai-Kia PBV)", powertrains=["BEV"], status="announced",
    status_note="kia.ch home page promotes the 'Weltpremiere des Kia PV7' (2026-10-21) with a teaser page; production/sales expected 2027 — VERIFY.", status_sources=[KIA_CH],
    twin_tier=None, twin_members=[], twin_note="", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Kia PV7", notes="Row provisional (size between van-mid and van-large)."))

# =================================================================== SAIC MOTOR — MAXUS
def maxus(model, display, row, body, gen, length, platform, pts, note, wiki, cat, extra=""):
    return m(brand="Maxus", group="SAIC Motor", model=model, display=display, other_names=[], ch_on_sale=None, ch_source=None,
        row=row, body=body, generation=gen, length_mm=length, platform=platform, powertrains=pts, status="on_sale",
        status_note=note+" saicmaxus.eu is robots-blocked; the UK range page is the 2026 source.",
        status_sources=[MAXUS_UK, MAXUS_UK_MIFA7, W+wiki] if model == "Mifa 7" else [MAXUS_UK, W+wiki], twin_tier=None, twin_members=[], twin_note="", twin_sources=[],
        carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
        commons_category=cat, commons_file=None, wikipedia_en=wiki.replace("_"," "), notes=extra)

models.append(maxus("eDeliver 3", "eDeliver 3", "van-small", "electric panel van (SWB / LWB), chassis cab", "I (2020–)", 4555,
    "SAIC Maxus EV30", ["BEV"], "Listed in the UK electric range (saicmaxus.co.uk, fetched 2026-10-22).", "Maxus_eDeliver_3", "Category:Maxus eDeliver 3", "LWB 5145 mm."))
models.append(maxus("eDeliver 5", "eDeliver 5", "van-mid", "electric panel van (L1 / L2), crew van", "I (2024–)", 4800,
    "SAIC Maxus", ["BEV"], "Listed in the UK electric range (saicmaxus.co.uk, fetched 2026-10-22).", "Maxus_eDeliver_5", "Category:Maxus eDeliver 5", "Compact mid-size van; L2 ~5100 mm."))
models.append(maxus("eDeliver 7", "eDeliver 7 / Deliver 7", "van-mid", "panel van (L1 / L2, H1 / H2): electric eDeliver 7 and diesel Deliver 7", "I (2023–; diesel Deliver 7 2025–)", 4998,
    "SAIC Maxus", ["diesel","BEV"], "UK site lists both 'DELIVER 7' (diesel) and 'eDELIVER 7' (electric) (fetched 2026-10-22).", "Maxus_eDeliver_7", "Category:Maxus eDeliver 7", "L2 5364 mm. One tile for both powertrains (same body)."))
models.append(maxus("eDeliver 9", "eDeliver 9 / Deliver 9", "van-large", "panel van (L2 / L3, H2 / H3), chassis cab (3.5 t class): electric eDeliver 9 and diesel Deliver 9", "I (2020–)", 5940,
    "SAIC Maxus V90", ["diesel","BEV"], "UK site lists both 'DELIVER 9' (diesel) and 'eDELIVER 9' (fetched 2026-10-22).", "Maxus_eDeliver_9", "Category:Maxus eDeliver 9", "L2 5546 mm."))
models.append(maxus("T60 Max", "T60 Max", "pickup", "double-cab diesel pickup (2.0 turbo diesel, 4x4, 1,050 kg payload, 3,500 kg towing)", "I (T60 facelift, UK 2025–)", 5365,
    "SAIC Maxus T60 (body-on-frame)", ["diesel"], "Listed in the UK diesel range as 'T60 MAX' (saicmaxus.co.uk, fetched 2026-10-22); availability in other European markets to VERIFY.", "Maxus_T60", "Category:Maxus T60", "Length approximate (T60 ~5365 mm)."))
models.append(maxus("eTerron 9", "eTerron 9", "pickup", "electric double-cab pickup (dual motor)", "I (2025–)", 5500,
    "SAIC Maxus Interstellar X (electric)", ["BEV"], "Listed in the UK electric range (fetched 2026-10-22); launched in Europe 2025.", "Maxus_eTerron_9", "Category:Maxus eTerron 9", "Electric twin of the Maxus Interstellar X / MG U9 (neither sold in Europe as of Oct 2026 — VERIFY)."))
models.append(maxus("Mifa 7", "Mifa 7", "mpv-large", "7-seat electric MPV", "I (2025–)", 4907,
    "SAIC Maxus Mifa (electric)", ["BEV"], "UK Mifa 7 page (fetched 2026-10-22): electric MPV, 6 or 7 seats (2-1-3 / 2-2-3), up to 298 miles WLTP; length not published (~4.9 m from launch data).", "Maxus_Mifa_7", "Category:Maxus Mifa 7", "Smaller sibling of the Mifa 9."))
models.append(maxus("Mifa 9", "Mifa 9", "mpv-large", "7-seat electric luxury MPV", "I (2022–)", 5270,
    "SAIC Maxus Mifa", ["BEV"], "Listed in the UK electric range (fetched 2026-10-22).", "Maxus_Mifa_9", "Category:Maxus Mifa 9", ""))

# =================================================================== GEELY HOLDING
models.append(m(brand="Farizon", group="Geely Holding", model="SV", display="SV",
    other_names=["Farizon SuperVan"], ch_on_sale=None, ch_source=None, row="van-mid",
    body="electric panel van (L1 / L2 / L3; H1–H3), chassis cab", generation="I (2024–)", length_mm=4990,
    platform="Geely GXA-M (drive-by-wire electric van architecture)", powertrains=["BEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): European launch 2025 via importer Jameel Motors (UK pricing ~£45,000–56,000, plug-in van grant eligible), UK reviews Jan–Feb 2026; L1H1–L3H3 bodies. farizonauto.eu could not be fetched.", status_sources=[W+"Farizon_SV"],
    twin_tier=None, twin_members=[], twin_note="", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Farizon SV", commons_file=None, wikipedia_en="Farizon SV",
    notes="L1 4990 / L2 5490 / L3 5995 mm; 67/83 kWh LFP or 106 kWh NMC; 169 kW. The L3 is large-van sized; row per brief = van-mid."))

models.append(m(brand="LEVC", group="Geely Holding", model="VN5", display="VN5",
    other_names=[], ch_on_sale=False, ch_source=None, row="van-mid",
    body="range-extender panel van", generation="I (2020–)", length_mm=5233,
    platform="LEVC/Geely eCity (TX taxi, aluminium)", powertrains=["PHEV"], status="on_sale",
    status_note="levc.com (fetched 2026-10-22) still lists the 'VN5 Van' among its models (dealer pages for DE, ES, NL, FR, SE, PL, HU, GR, AT, BE, MT); Wikipedia: UK sales since Nov 2020, rest of Europe since July 2021, production 2020–present.", status_sources=[LEVC, W+"LEVC_VN5"],
    twin_tier=None, twin_members=[], twin_note="Van body on the LEVC TX taxi platform.", twin_sources=[W+"LEVC_VN5"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:LEVC VN5", commons_file=None, wikipedia_en="LEVC VN5",
    notes="Plug-in series hybrid (31 kWh battery + 1.5 petrol range extender) — recorded as PHEV."))

announced.append(m(brand="LEVC", group="Geely Holding", model="L380", display="L380",
    other_names=[], ch_on_sale=None, ch_source=None, row="mpv-large",
    body="6–8-seat electric luxury MPV", generation="I (2024 China; Europe 2026)", length_mm=5316,
    platform="Geely SOA/SEA-derived electric MPV architecture", powertrains=["BEV"], status="announced",
    status_note="levc.com home (fetched 2026-10-22) lists 'The all New L380 MPV' with its own model page, but the page did not render and no UK price/order information was obtained — treated as announced for Europe; VERIFY order status.",
    status_sources=[LEVC],
    twin_tier=None, twin_members=[], twin_note="", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="LEVC L380", notes="Length from the Chinese launch data (5,316 mm), unverified for Europe."))

# =================================================================== IVECO GROUP
models.append(m(brand="Iveco", group="Iveco Group", model="Daily", display="Daily / eDaily",
    other_names=["eDaily (electric)", "Daily Natural Power (CNG)"], ch_on_sale=None, ch_source=None, row="van-large",
    body="panel van, chassis cab, minibus (3.3–7.2 t; 3.5 t versions)", generation="VI (2014–; facelifts 2019, 2024 'MY24')", length_mm=6000,
    platform="Iveco Daily ladder frame (RWD)", powertrains=["diesel","CNG","BEV"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): current Daily since July 2014, facelift April 2019 (MY2024 update not on the page), eDaily electric and eDaily FCEV (unveiled 19 Sep 2022). iveco.com global page lists no products — VERIFY CH listing on iveco.com/switzerland.", status_sources=[W+"Iveco_Daily"],
    twin_tier=None, twin_members=[], twin_note="No twin. Iveco's smaller 2025 electric vans eJolly/eSuperJolly are Stellantis rebadges (separate tiles).", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Iveco Daily VI", commons_file=None, wikipedia_en="Iveco Daily",
    notes="Length 5.2–7.5 m depending on body; only the ≤3.5 t versions are in scope."))

models.append(m(brand="Iveco", group="Iveco Group", model="eJolly", display="eJolly",
    other_names=[], ch_on_sale=None, ch_source=None, row="van-mid",
    body="electric panel van (K0 body)", generation="I (2025–)", length_mm=4981,
    platform="EMP2 (Stellantis)", powertrains=["BEV"], status="on_sale",
    status_note="Iveco eJolly (2025–) is listed among the rebadged versions of the Citroën Jumpy/K0 family on Wikipedia (fetched 2026-10-22), part of the Iveco–Stellantis LCV supply agreement; sold through Iveco dealers in Europe from 2025 — VERIFY market coverage on iveco.com.", status_sources=[W+"Citro%C3%ABn_Jumpy"],
    twin_tier=1, twin_members=others(G_K0_VAN, "Iveco eJolly"),
    twin_note="Rebadged electric K0 van (ë-Jumpy / e-Expert).", twin_sources=[W+"Citro%C3%ABn_Jumpy"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Citroën Jumpy", notes="Use K0 images (same body)."))

models.append(m(brand="Iveco", group="Iveco Group", model="eSuperJolly", display="eSuperJolly",
    other_names=[], ch_on_sale=None, ch_source=None, row="van-large",
    body="electric large panel van (Ducato body, 3.5 t)", generation="I (2025–)", length_mm=5413,
    platform="Sevel X290 (Stellantis)", powertrains=["BEV"], status="on_sale",
    status_note="Iveco eSuperJolly (2025–) is listed among the Ducato rebadges on Wikipedia (fetched 2026-10-22); Iveco–Stellantis supply agreement — VERIFY market coverage on iveco.com.", status_sources=[W+"Fiat_Ducato"],
    twin_tier=1, twin_members=others(G_SEVEL, "Iveco eSuperJolly"),
    twin_note="Rebadged E-Ducato (110 kWh).", twin_sources=[W+"Fiat_Ducato"],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category=None, commons_file=None, wikipedia_en="Fiat Ducato", notes="Use Ducato images (same body)."))

# =================================================================== OTHER (fringe)
models.append(m(brand="Piaggio", group="Piaggio Group", model="Porter NP6", display="Porter NP6",
    other_names=[], ch_on_sale=None, ch_source=None, row="van-small",
    body="cab-forward micro truck: flatbed (fixed/tipping), chassis cab for upfits (N1, ≤2.8 t)", generation="II (NP6, 2021–)", length_mm=4300,
    platform="Piaggio/Foton Gratour V3-derived ladder frame (RWD)", powertrains=["petrol","LPG","CNG"], status="on_sale",
    status_note="Wikipedia (fetched 2026-10-22): NP6 presented Jan 2021, Foton Gratour V3-derived but re-engineered and built in Pontedera; 1.5 petrol/LPG or petrol/CNG, GVW ≤2.8 t, flatbed and chassis-cab bodies. 2026 listing not verified (Piaggio site not fetched). Included because it is a four-wheel N1 vehicle under 3.5 t; group label = parent company (Piaggio Group).", status_sources=[W+"Piaggio_Porter"],
    twin_tier=None, twin_members=[], twin_note="", twin_sources=[],
    carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
    commons_category="Category:Piaggio Porter NP6", commons_file=None, wikipedia_en="Piaggio Porter", notes="Fringe tile — verifier may drop."))

# =================================================================== discontinued / checked-and-excluded
discontinued += [
    {"brand": "Renault", "model": "Express Van", "note": "Ceased to be marketed in the EU in July 2024 (GSR2 safety rules not worth the investment); not on renault.ch vans page 2026-10-21.", "source": W+"Renault_Express_(2020)"},
    {"brand": "Renault", "model": "Trafic Van E-Tech (gen III, 52 kWh)", "note": "Gen-III electric Trafic (IAA 2022) no longer listed in CH in Oct 2026; replaced by the Flexis-based Trafic E-Tech gen IV (on sale H1 2027).", "source": RENAULT_CH_VANS},
    {"brand": "Mercedes-Benz", "model": "Citan / eCitan / T-Class / EQT", "note": "Discontinuation in 2026 announced April 2025; kept as runout tiles (production ends 2026).", "source": W+"Mercedes-Benz_T-Class"},
    {"brand": "Mercedes-Benz", "model": "EQV", "note": "Replaced by the VAN.EA VLE (production since June 2026); kept as runout tile.", "source": W+"Mercedes-Benz_VLE"},
    {"brand": "Jeep", "model": "Gladiator", "note": "Withdrawn from the European market at the end of 2023 (EcoDiesel phased out).", "source": W+"Jeep_Gladiator_(JT)"},
    {"brand": "Fiat", "model": "Fiorino / Qubo (2008 Sevel-Tofaş generation)", "note": "Old Fiorino/Qubo ended 2024; Wikipedia shows no new European Fiorino as of Oct 2026 (the 2025 'new Fiorino' is the Brazilian Uno-based model). The Qubo name returned in 2026 on a K9/Berlingo-based MPV (see models).", "source": W+"Fiat_Fiorino"},
    {"brand": "Fiat", "model": "Doblò (passenger, 2022–2025)", "note": "Passenger role taken over by the 2026 Fiat Qubo; E-Doblò passenger listed in CH only via the stock locator (runout).", "source": FIAT_CH},
    {"brand": "Maxus", "model": "T90 EV", "note": "No longer in the UK range (replaced by the eTerron 9); may linger in some EU markets.", "source": MAXUS_UK},
    {"brand": "Stellantis (Peugeot/Citroën/Opel)", "model": "e-Expert / ë-Jumpy / Vivaro Hydrogen, Movano Hydrogen", "note": "Fuel-cell versions announced 2021–2023; Stellantis ended its hydrogen programme in 2025, so FCEV is not listed as a current powertrain.", "source": W+"Citro%C3%ABn_Jumpy"},
    {"brand": "Fiat", "model": "Talento", "note": "Renault Trafic rebadge; Renault stopped supplying it in Sept 2020; replaced by the Scudo (2022).", "source": W+"Renault_Trafic"},
    {"brand": "Nissan", "model": "e-NV200 / NV250 / NV300 / NV400", "note": "Replaced 2021–2024 by Townstar / Primastar / Interstar.", "source": W+"Nissan_Townstar"},
    {"brand": "Nissan", "model": "Navara", "note": "European production (Barcelona) ended Dec 2021; the Triton-based D27 Navara (2026–) is not sold in Europe. Not on nissan.ch (2026-10-21).", "source": W+"Mitsubishi_Triton"},
    {"brand": "Peugeot", "model": "Landtrek", "note": "Not sold in Europe (Latin America/Africa only).", "source": W+"Peugeot_Landtrek"},
    {"brand": "Fiat", "model": "Titano", "note": "Not sold in Europe (South America only).", "source": W+"Fiat_Titano"},
    {"brand": "Mitsubishi", "model": "Express", "note": "Trafic rebadge sold only in Australia/NZ (2020–2022).", "source": W+"Renault_Trafic"},
    {"brand": "Dacia", "model": "Dokker", "note": "Ended 2021; Dacia sells no van or pickup in Europe (Spring Cargo / Duster Commercial are body variants of passenger tiles).", "source": W+"Renault_Express_(2020)"},
    {"brand": "BYD", "model": "Shark", "note": "No European launch as of 2026 (markets: Mexico, Brazil, Australia, NZ, South Africa, SE Asia).", "source": W+"BYD_Shark"},
    {"brand": "GWM", "model": "Poer / Cannon", "note": "No European market listed on Wikipedia as of 2026 (China, Australia, South Africa, LatAm...).", "source": W+"Great_Wall_Pao"},
    {"brand": "JAC", "model": "T9 / Hunter", "note": "No European sales confirmed; sold in Italy as the importer-branded 'ICH-X K4' only.", "source": W+"JAC_T9"},
]

doc = {
    "agent": "lcv (cross-brand light-commercial deep dive)",
    "checked_on": "2026-10-21",
    "models": models,
    "announced": announced,
    "discontinued_recently": discontinued,
    "sources": [
        {"url": RENAULT_CH_VANS, "what": "Renault CH vans page (fetched 2026-10-21): Kangoo Van, Trafic Van, new Trafic Van E-Tech, Master range with prices"},
        {"url": RENAULT_CH_HOME, "what": "Renault CH model menu (fetched 2026-10-21): Kangoo, Grand Kangoo, Trafic Passenger, Trafic SpaceClass"},
        {"url": NISSAN_CH, "what": "Nissan CH new-car overview (fetched 2026-10-21): Townstar, Townstar Kombi, Primastar, Primastar Kombi, Interstar; no Navara"},
        {"url": OPEL_CH, "what": "Opel CH navigation (fetched 2026-10-21): Combo/Combo Electric, Zafira/Zafira Electric, Combo Cargo, Vivaro, Movano"},
        {"url": CITROEN_CH_LCV, "what": "Citroën CH Nutzfahrzeuge page (fetched 2026-10-21): ë-C3 Van, Berlingo Van, Jumpy, Jumper"},
        {"url": "https://www.citroen.ch/de/", "what": "Citroën CH home (fetched 2026-10-21): Berlingo in passenger model list"},
        {"url": "https://www.peugeot.ch/de/", "what": "Peugeot CH home (fetched 2026-10-21): Partner Premium Long offer"},
        {"url": KIA_CH, "what": "Kia CH home (fetched 2026-10-21): PV5 Cargo/Passenger/Crew/Chassis Cab pages; PV7 world premiere teaser"},
        {"url": W+"Ford_Transit_Connect", "what": "Wikipedia (fetched 2026-10-21): Caddy-based Transit Connect/Tourneo Connect dates and lengths"},
        {"url": W+"Nissan_Primastar", "what": "Wikipedia (fetched 2026-10-21): Primastar 2022–present, Trafic III based"},
        {"url": "https://www.carsized.com/en-us/cars/compare/renault-kangoo-2021-5-door-van-vs-ford-f/", "what": "carsized compare page (fetched 2026-10-21): Kangoo 2021 side image URL, 'Gen. 3 | 2021 - present'"},
        {"url": RT_PR, "what": "Renault Trucks press release 15 Sep 2026: new E-Tech Trafic on sale in Europe H1 2027; Trafic Red Edition since 2022"},
        {"url": RENAULT_CH_TRAFIC_EV, "what": "Renault CH page for the new Trafic Van E-Tech (fetched 2026-10-22): no price, homologation pending"},
        {"url": TOYOTA_UK_HILUX, "what": "Toyota UK Hilux page (fetched 2026-10-22): 'All New Hilux' diesel + BEV, from £34,670 ex VAT"},
        {"url": KGM_UK, "what": "KGM UK home (fetched 2026-10-22): Musso, All-new Musso Rhino, Musso EV, Rexton Commercial prices"},
        {"url": MAXUS_UK, "what": "Maxus UK home (fetched 2026-10-22): Deliver 7/9, T60 Max, eDeliver 3/5/7/9, eTerron 9, Mifa 7/9"},
        {"url": "https://www.saicmaxus.co.uk/our-range/new-vans/t60-max/", "what": "Maxus T60 Max page (fetched 2026-10-22): 2.0 diesel 4x4, 1,050 kg payload, 3,500 kg towing"},
        {"url": FIAT_CH, "what": "Fiat CH home (fetched 2026-10-22): Ulysse/E-Ulysse (Professional), E-Doblò stock, Qubo L"},
        {"url": W+"Mercedes-Benz_T-Class", "what": "Wikipedia (fetched 2026-10-22): T-Class Apr 2022, EQT Dec 2022; April 2025 announcement of discontinuation in 2026 (Motor1)"},
        {"url": W+"Mercedes-Benz_VLE", "what": "Wikipedia (fetched 2026-10-22): VLE revealed 10 Mar 2026, production since June 2026, 5309/5484 mm, VAN.EA, EQV predecessor"},
        {"url": W+"Kia_PV5", "what": "Wikipedia (fetched 2026-10-22): PV5 European sales from Nov 2025; 4695/4890 mm; E-GMP.S"},
        {"url": W+"Mitsubishi_Triton", "what": "Wikipedia (fetched 2026-10-22): L200 gen VI in Europe, UK L200 Commercial (Sept 2026), Navara D27 twin 2026 (not Europe)"},
        {"url": W+"Jeep_Gladiator_(JT)", "what": "Wikipedia (fetched 2026-10-22): Gladiator withdrawn from Europe end of 2023"},
        {"url": W+"Renault_Express_(2020)", "what": "Wikipedia (fetched 2026-10-22): Express Van no longer marketed in the EU from July 2024"},
        {"url": W+"Citro%C3%ABn_Jumpy", "what": "Wikipedia (fetched 2026-10-22): K0 family rebadges incl. Iveco eJolly 2025; combustion passenger versions dropped Jan 2022 except CH/Balkans; Luton closed 2025"},
        {"url": W+"Citro%C3%ABn_Berlingo", "what": "Wikipedia (fetched 2026-10-22): K9 rebadges incl. Fiat Doblò III (2022) and Fiat Qubo (2026–)"},
        {"url": W+"Fiat_Ducato", "what": "Wikipedia (fetched 2026-10-22): Ducato lengths, 2024 facelift, rebadges Boxer/Jumper/Movano (2021)/ProAce Max/Iveco eSuperJolly (2025)"},
        {"url": W+"Renault_Trafic", "what": "Wikipedia (fetched 2026-10-22): Trafic III 5080/5480 mm, facelifts 2019/2021/2024, Primastar 2022–, Renault Trucks Trafic 2022–"},
        {"url": W+"Volkswagen_Transporter_(T7)", "what": "Wikipedia (fetched 2026-10-22): Transporter/Caravelle unveiled Aug 2024 on Ford Transit Custom basis; Multivan on MQB"},
        {"url": W+"Volkswagen_Amarok", "what": "Wikipedia (fetched 2026-10-22): Amarok II on Ranger P703, built by Ford Silverton"},
        {"url": W+"Volkswagen_Crafter", "what": "Wikipedia (fetched 2026-10-22): Crafter II (Września) sold by MAN as TGE; Grand California"},
        {"url": W+"Ford_Transit_Custom", "what": "Wikipedia (fetched 2026-10-22): Transit Custom II (Ford Otosan) — VW Transporter is its rebadge"},
        {"url": W+"Volkswagen_Caddy", "what": "Wikipedia (fetched 2026-10-22): Caddy Typ SB on sale Nov 2020; Ford Tourneo Connect rebadge 2021"},
        {"url": W+"Renault_Kangoo", "what": "Wikipedia (fetched 2026-10-22): Kangoo III dates, lengths, Maubeuge, Townstar/T-Class/EQT rebadges"},
        {"url": W+"Isuzu_D-Max", "what": "Wikipedia (fetched 2026-10-22): D-Max III, UK Apr 2021, D-Max EV UK deliveries Feb 2026"},
        {"url": W+"Hyundai_Staria", "what": "Wikipedia (fetched 2026-10-22): Staria 5255 mm, N3 platform, facelift Dec 2025, Staria Electric Jan 2026"},
        {"url": W+"Farizon_SV", "what": "Wikipedia (fetched 2026-10-22): SV lengths, European launch 2025 via Jameel Motors"},
        {"url": W+"LEVC_VN5", "what": "Wikipedia (fetched 2026-10-22): VN5 5233 mm, UK Nov 2020, Europe July 2021, range-extender"},
        {"url": W+"KGM_Musso_EV", "what": "Wikipedia (fetched 2026-10-22): Musso EV launched 5 Mar 2025, 5160 mm, 80.6 kWh"},
        {"url": W+"Ineos_Grenadier", "what": "Wikipedia (fetched 2026-10-22): Quartermaster introduced July 2023, 5400 mm"},
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
        {"url": W+"Piaggio_Porter", "what": "Wikipedia (fetched 2026-10-22): Porter NP6 Jan 2021, Foton-derived, petrol/LPG/CNG, ≤2.8 t"},
    ],
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)
print("wrote", OUT, len(models), "models,", len(announced), "announced,", len(discontinued), "discontinued")
