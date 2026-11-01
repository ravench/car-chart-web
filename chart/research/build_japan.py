#!/usr/bin/env python3
"""Builds japan.json for the car line-up chart (Toyota Motor, Subaru, Suzuki, Mazda, Honda).
Edit the MODELS / ANNOUNCED / DISCONTINUED lists, then run:  python3 -I build_japan.py
"""
import json, os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "japan.json")

KEYS = ["brand", "group", "model", "display", "other_names", "ch_on_sale", "ch_source", "row", "body",
        "generation", "length_mm", "platform", "powertrains", "status", "status_note", "status_sources",
        "twin_tier", "twin_members", "twin_note", "twin_sources", "carsized_slug", "carsized_side",
        "carsized_front", "carsized_years", "commons_category", "commons_file", "wikipedia_en", "notes"]

# ---- frequently used sources -------------------------------------------------------------------
TOYOTA_CH = "https://de.toyota.ch/neuwagen-kaufen"            # all models + CHF prices, fetched 2026-10-21
TOYOTA_DE = "https://www.toyota.de/neuwagen"                  # DE model filter list, fetched 2026-10-21
TOYOTA_UK = "https://www.toyota.co.uk/new-cars"               # UK range list, fetched 2026-10-21
LEXUS_CH = "https://de.lexus.ch/"                             # footer model list, fetched 2026-10-21
LEXUS_DE = "https://www.lexus.de/modelle"                     # fetched 2026-10-21
LEXUS_UK = "https://www.lexus.co.uk/"                         # fetched 2026-10-21
SUBARU_CH = "https://www.subaru.ch/de/modelle"                # fetched 2026-10-21
SUBARU_DE = "https://www.subaru.de/"                          # fetched 2026-10-21
SUBARU_UK = "https://www.subaru.co.uk/"                       # fetched 2026-10-21
SUZUKI_CH = "https://www.suzuki.ch/de/auto"                   # fetched 2026-10-21
MAZDA_CH = "https://de.mazda.ch/modelle/"                     # fetched 2026-10-21 (only meta keywords readable)
MAZDA_DE = "https://www.mazda.de/modelle/"                    # fetched 2026-10-21 (only meta keywords readable)
HONDA_CH = "https://www.de.honda.ch/cars.html"                # fetched 2026-10-21, CHF prices
HONDA_DE = "https://www.honda.de/cars.html"                   # fetched 2026-10-21
HONDA_UK = "https://www.honda.co.uk/cars.html"                # fetched 2026-10-21

def m(**kw):
    """Model entry with defaults; every key of the brief's schema is present."""
    d = {k: None for k in KEYS}
    d.update({"other_names": [], "powertrains": [], "status": "on_sale", "status_sources": [],
              "twin_tier": None, "twin_members": [], "twin_note": "", "twin_sources": [], "notes": ""})
    d.update(kw)
    unknown = set(kw) - set(KEYS)
    if unknown:
        raise SystemExit(f"unknown keys {unknown} in {kw.get('brand')} {kw.get('model')}")
    return {k: d[k] for k in KEYS}

T = dict(brand="Toyota", group="Toyota Motor")
L = dict(brand="Lexus", group="Toyota Motor")
SB = dict(brand="Subaru", group="Subaru")
SZ = dict(brand="Suzuki", group="Suzuki")
MZ = dict(brand="Mazda", group="Mazda")
H = dict(brand="Honda", group="Honda")

MODELS = []
ANNOUNCED = []
DISCONTINUED = []
SOURCES = []

# ================================================================================================
# TOYOTA
# ================================================================================================
MODELS += [
m(**T, model="Aygo X", display="Aygo X", ch_on_sale=True, ch_source=TOYOTA_CH, row="a-city",
  body="5-door crossover hatchback", generation="I (2022–; facelift 2025 with hybrid)", length_mm=3700,
  platform="TNGA GA-B", powertrains=["HEV"],
  status_note="On sale: toyota.ch lists Aygo X from CHF 19'900 (Oct 2026); toyota.de lists Aygo X Pure/Active/Teamplayer/Lounge/GR Sport from EUR 21'990; UK range list. 2025 facelift introduced the 1.5 hybrid (Aygo X Hybrid).",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  wikipedia_en="Toyota Aygo X", commons_category="Category:Toyota Aygo X",
  notes="Powertrain to verify: after the 2025 facelift the European Aygo X is marketed as hybrid (1.5 HEV); whether the 1.0 petrol remains in some markets could not be confirmed within the budget."),

m(**T, model="Yaris", display="Yaris", ch_on_sale=True, ch_source=TOYOTA_CH, row="b-hatch",
  body="5-door hatchback (GR Yaris: 3-door)", generation="IV / XP210 (2020–; facelift 2024)", length_mm=3940,
  platform="TNGA GA-B", powertrains=["HEV", "petrol"],
  status_note="On sale in CH (from CHF 22'400), DE (from EUR 25'500), UK. GR Yaris (3-door, 1.6 turbo petrol; CHF 44'900) is a performance version and counts as the same tile per brief rule 4.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Mazda Mazda2 Hybrid"],
  twin_note="Mazda2 Hybrid is a rebadged Yaris hybrid built by Toyota Motor Manufacturing France (Valenciennes) with Mazda badges.",
  twin_sources=["https://en.wikipedia.org/wiki/Mazda2_Hybrid"],
  wikipedia_en="Toyota Yaris (XP210)", commons_category="Category:Toyota Yaris (XP210)",
  notes="GR Yaris folded into this tile per the brief's performance-version rule (it has its own 3-door body; verifier may split it)."),

m(**T, model="Yaris Cross", display="Yaris Cross", ch_on_sale=True, ch_source=TOYOTA_CH, row="b-suv",
  body="5-door crossover SUV", generation="I / XP210 (2021–; facelift 2024)", length_mm=4180,
  platform="TNGA GA-B", powertrains=["HEV"],
  status_note="On sale in CH (from CHF 27'900), DE, UK.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=2, twin_members=["Lexus LBX"],
  twin_note="Lexus LBX uses the same GA-B platform and 1.5 hybrid system with a distinct body (tier 2 per assignment).",
  twin_sources=["https://en.wikipedia.org/wiki/Lexus_LBX"],
  wikipedia_en="Toyota Yaris Cross", commons_category="Category:Toyota Yaris Cross"),

m(**T, model="Urban Cruiser", display="Urban Cruiser", ch_on_sale=True, ch_source=TOYOTA_CH, row="b-suv",
  body="5-door electric SUV", generation="I (2025–)", length_mm=4285,
  platform="Heartect-e (Suzuki/Toyota BEV platform)", powertrains=["BEV"],
  status_note="On sale: toyota.ch from CHF 31'900 (Oct 2026); toyota.de list; toyota.co.uk 'New Urban Cruiser'.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Suzuki e Vitara"],
  twin_note="Rebadged Suzuki e Vitara, both built by Suzuki Motor Gujarat (India); Toyota-specific front/rear styling.",
  twin_sources=["https://en.wikipedia.org/wiki/Suzuki_e_Vitara"],
  wikipedia_en="Toyota Urban Cruiser (2025)", commons_category="Category:Toyota Urban Cruiser (2025)"),

m(**T, model="Corolla", display="Corolla", ch_on_sale=True, ch_source=TOYOTA_CH, row="c-hatch",
  body="5-door hatchback + Touring Sports estate (saloon in some markets; Corolla Commercial van in UK)",
  generation="XII / E210 (2019–; facelift 2023)", length_mm=4370,
  platform="TNGA GA-C", powertrains=["HEV"],
  status_note="On sale: toyota.ch Corolla from CHF 29'900, Touring Sports from CHF 30'500; DE and UK lists. Touring Sports is 4650 mm.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=None, twin_members=[],
  twin_note="Former tier-1 twin Suzuki Swace (rebadged Corolla Touring Sports) was withdrawn from Europe in 2025, so no current twin is listed. Platform (GA-C) shared with Corolla Cross, C-HR, Prius, Lexus UX (different rows).",
  twin_sources=["https://www.motor1.com/news/725920/why-suzuki-stops-selling-swace-ignis-jimny/"],
  wikipedia_en="Toyota Corolla (E210)", commons_category="Category:Toyota Corolla (E210)"),

m(**T, model="Corolla Cross", display="Corolla Cross", ch_on_sale=True, ch_source=TOYOTA_CH, row="c-suv",
  body="5-door SUV", generation="I / XG10 (2020–; Europe 2022–; facelift 2024)", length_mm=4460,
  platform="TNGA GA-C", powertrains=["HEV"],
  status_note="On sale: toyota.ch from CHF 37'200; toyota.de list. Not in the UK range.",
  status_sources=[TOYOTA_CH, TOYOTA_DE],
  twin_tier=2, twin_members=["Toyota C-HR", "Lexus UX"],
  twin_note="GA-C platform siblings with 2640 mm wheelbase (C-HR II, UX); distinct bodies.",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_Corolla_Cross"],
  wikipedia_en="Toyota Corolla Cross", commons_category="Category:Toyota Corolla Cross"),

m(**T, model="C-HR", display="C-HR", ch_on_sale=True, ch_source=TOYOTA_CH, row="c-suv",
  body="5-door coupé-SUV", generation="II / AX50 (2023–)", length_mm=4362,
  platform="TNGA GA-C", powertrains=["HEV", "PHEV"],
  status_note="On sale: toyota.ch 'Toyota C-HR (Hybrid/Plug-in)' from CHF 32'900; DE, UK.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=2, twin_members=["Toyota Corolla Cross", "Lexus UX"],
  twin_note="GA-C platform siblings (same 2640 mm wheelbase); distinct bodies.",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_C-HR"],
  wikipedia_en="Toyota C-HR", commons_category="Category:Toyota C-HR (AX50)"),

m(**T, model="C-HR+", display="C-HR+", ch_on_sale=True, ch_source=TOYOTA_CH, row="c-suv",
  body="5-door electric SUV", generation="I (2025–)", length_mm=4520,
  platform="e-TNGA", powertrains=["BEV"],
  status_note="On sale: toyota.ch 'Toyota C-HR+' from CHF 39'900 (Oct 2026); toyota.de list; UK menu 'New Toyota C-HR+'.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Subaru Uncharted"],
  twin_note="Subaru Uncharted is the Subaru-badged version of the C-HR+ (same body, Subaru fascia, AWD focus), built by Toyota.",
  twin_sources=["https://en.wikipedia.org/wiki/Subaru_Uncharted"],
  wikipedia_en="Toyota C-HR+", commons_category="Category:Toyota C-HR+"),

m(**T, model="bZ4X", display="bZ4X", ch_on_sale=True, ch_source=TOYOTA_CH, row="d-suv",
  body="5-door electric SUV", generation="I / XEAM10 (2022–; facelift 2025)", length_mm=4690,
  platform="e-TNGA", powertrains=["BEV"],
  status_note="On sale: toyota.ch from CHF 37'900; DE, UK (facelifted 2025 model with 57.7/73.1 kWh batteries).",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Subaru Solterra"],
  twin_note="Solterra is the Subaru-badged twin (same body shell, built by Toyota at Motomachi). Lexus RZ is an e-TNGA platform sibling (tier 2, same row).",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_bZ4X"],
  wikipedia_en="Toyota bZ4X", commons_category="Category:Toyota bZ4X",
  notes="Row: 4690 mm sits on the c-suv/d-suv boundary; Toyota positions bZ4X as a D-segment SUV, so d-suv (with Solterra and RZ)."),

m(**T, model="bZ4X Touring", display="bZ4X Touring", ch_on_sale=True, ch_source=TOYOTA_CH, row="d-suv",
  body="5-door electric estate-SUV", generation="I (2026–)", length_mm=4830,
  platform="e-TNGA", powertrains=["BEV"],
  status_note="On sale: toyota.ch from CHF 44'900 (Oct 2026); toyota.de list; toyota.co.uk 'All-New bZ4X Touring' in range list.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Subaru E-Outback"],
  twin_note="Subaru E-Outback (Trailseeker in North America) is the Subaru-badged twin of the bZ4X Touring.",
  twin_sources=["https://en.wikipedia.org/wiki/Subaru_Trailseeker"],
  wikipedia_en="Toyota bZ4X Touring", commons_category="Category:Toyota bZ4X Touring"),

m(**T, model="RAV4", display="RAV4", ch_on_sale=True, ch_source=TOYOTA_CH, row="c-suv",
  body="5-door SUV", generation="VI / XA60 (2025–; Europe 2026)", length_mm=4600,
  platform="TNGA GA-K", powertrains=["HEV", "PHEV"],
  status_note="Sixth generation: UK orders opened early May 2026, deliveries from June 2026 (Toyota UK press release 7 Apr 2026, PHEV range from GBP 43'845); toyota.ch RAV4 from CHF 43'900; toyota.de list.",
  status_sources=["https://media.toyota.co.uk/?p=66870", TOYOTA_CH, TOYOTA_DE],
  twin_tier=1, twin_members=["Suzuki Across"],
  twin_note="Suzuki Across is a rebadged RAV4 plug-in hybrid (new Across based on the 6th-gen RAV4, 'NEW' on suzuki.ch). Lexus NX is a GA-K platform sibling (tier 2, same row).",
  twin_sources=["https://en.wikipedia.org/wiki/Suzuki_Across", SUZUKI_CH],
  wikipedia_en="Toyota RAV4 (XA60)", commons_category="Category:Toyota RAV4 (XA60)",
  notes="UK launch range is PHEV-only; HEV availability in continental Europe to verify (CHF 43'900 base price suggests a hybrid)."),

m(**T, model="Prius", display="Prius", ch_on_sale=True, ch_source=TOYOTA_CH, row="c-hatch",
  body="5-door liftback", generation="V / XW60 (2023–)", length_mm=4600,
  platform="TNGA GA-C", powertrains=["PHEV"],
  status_note="On sale as plug-in hybrid only in Europe: toyota.ch from CHF 41'400; DE 'Prius Plug-in Hybrid'; UK.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  wikipedia_en="Toyota Prius (XW60)", commons_category="Category:Toyota Prius (XW60)"),

m(**T, model="Mirai", display="Mirai", ch_on_sale=True, ch_source=TOYOTA_CH, row="e-car",
  body="4-door saloon", generation="II / JPD20 (2020–)", length_mm=4975,
  platform="TNGA GA-L", powertrains=["FCEV"],
  status_note="On sale: toyota.ch from CHF 68'800; DE, UK lists (hydrogen fuel cell).",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  wikipedia_en="Toyota Mirai", commons_category="Category:Toyota Mirai (JPD20)"),

m(**T, model="Land Cruiser", display="Land Cruiser", ch_on_sale=True, ch_source=TOYOTA_CH, row="offroad",
  body="5-door 4x4 (Land Cruiser Commercial van in UK)", generation="J250 (2024–)", length_mm=4925,
  platform="TNGA GA-F (ladder frame)", powertrains=["diesel"],
  status_note="On sale: toyota.ch from CHF 74'900; DE; UK (incl. Land Cruiser Commercial). 2.8 D-4D, 48V mild-hybrid version added 2025.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  wikipedia_en="Toyota Land Cruiser (J250)", commons_category="Category:Toyota Land Cruiser (J250)",
  notes="Lexus GX is the platform twin but is not sold in Europe."),

m(**T, model="Hilux", display="Hilux", ch_on_sale=True, ch_source=TOYOTA_CH, row="pickup",
  body="pickup, double cab", generation="IX (2026–)", length_mm=None,
  platform="TNGA GA-F derived (IMV ladder frame)", powertrains=["MHEV", "BEV"],
  status_note="All-new Hilux: UK orders open 1 June 2026, BEV deliveries mid-June, Diesel 48V deliveries July 2026 (Toyota UK, 13 May 2026); toyota.ch Hilux from CHF 53'900; toyota.de list. Europe gets Double Cab only, 2.8 diesel 48V mild hybrid and a BEV (59.2 kWh).",
  status_sources=["https://media.toyota.co.uk/?p=67442", "https://www.electrifying.com/blog/article/prices-announced-for-electric-toyota-hilux", TOYOTA_CH],
  wikipedia_en="Toyota Hilux", commons_category="Category:Toyota Hilux (ninth generation)",
  notes="Length of the new generation not yet confirmed from a fetched source (approx. 5.3 m). Commons category name for the 9th generation to be verified."),

m(**T, model="Proace City", display="Proace City", ch_on_sale=True, ch_source=TOYOTA_CH, row="van-small",
  body="panel van (L1/L2)", generation="II (2019–; facelift 2024)", length_mm=4403,
  platform="Stellantis EMP2 (K9)", powertrains=["petrol", "diesel", "BEV"],
  status_note="On sale: toyota.ch from CHF 26'214; DE, UK lists (Proace City / Proace City Electric).",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Peugeot Partner", "Citroën Berlingo", "Opel/Vauxhall Combo", "Fiat Doblò"],
  twin_note="Rebadged Stellantis K9 small van (Berlingo/Partner/Combo/Doblò), built by Stellantis in Vigo/Mangualde with Toyota fascia.",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_ProAce_City"],
  wikipedia_en="Toyota ProAce City", commons_category="Category:Toyota ProAce City",
  notes="Twin group in van-small: Berlingo Van / Partner / Combo Cargo / Doblò Cargo; use the canonical names your Stellantis colleagues use."),

m(**T, model="Proace City Verso", display="Proace City Verso", ch_on_sale=True, ch_source=TOYOTA_CH, row="mpv-small",
  body="leisure activity vehicle (5/7 seats, L1/L2)", generation="II (2019–; facelift 2024)", length_mm=4403,
  platform="Stellantis EMP2 (K9)", powertrains=["petrol", "diesel", "BEV"],
  status_note="On sale: toyota.ch from CHF 28'400; DE, UK lists.",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Peugeot Rifter", "Citroën Berlingo", "Opel/Vauxhall Combo", "Fiat Doblò"],
  twin_note="Passenger version of the Stellantis K9 (Rifter / Berlingo / Combo Life / Doblò).",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_ProAce_City"],
  wikipedia_en="Toyota ProAce City", commons_category="Category:Toyota ProAce City Verso"),

m(**T, model="Proace", display="Proace", ch_on_sale=True, ch_source=TOYOTA_CH, row="van-mid",
  body="panel van (Compact/Medium/Long)", generation="II (2016–; facelift 2024)", length_mm=4959,
  platform="Stellantis EMP2 (K0)", powertrains=["diesel", "BEV"],
  status_note="On sale: toyota.ch from CHF 36'780; DE, UK lists (Proace / Proace Electric).",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Peugeot Expert", "Citroën Jumpy", "Opel/Vauxhall Vivaro", "Fiat Scudo"],
  twin_note="Rebadged Stellantis K0 mid-size van built in Hordain (FR) / Luton; Toyota-specific grille.",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_ProAce"],
  wikipedia_en="Toyota ProAce", commons_category="Category:Toyota ProAce (2016)",
  notes="Length given for Medium (L2); Compact 4609 mm, Long 5309 mm."),

m(**T, model="Proace Verso", display="Proace Verso", ch_on_sale=True, ch_source=TOYOTA_CH, row="mpv-large",
  body="people carrier (Medium/Long)", generation="II (2016–; facelift 2024)", length_mm=4959,
  platform="Stellantis EMP2 (K0)", powertrains=["diesel", "BEV"],
  status_note="On sale: toyota.ch from CHF 41'600; DE, UK lists (incl. Proace Verso Electric).",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Peugeot Traveller", "Citroën SpaceTourer", "Opel/Vauxhall Zafira", "Fiat Ulysse"],
  twin_note="Passenger version of the Stellantis K0 van family.",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_ProAce"],
  wikipedia_en="Toyota ProAce", commons_category="Category:Toyota ProAce Verso"),

m(**T, model="Proace Max", display="Proace Max", ch_on_sale=True, ch_source=TOYOTA_CH, row="van-large",
  body="large panel van / chassis cab", generation="I (2024–)", length_mm=5413,
  platform="Stellantis Ducato (X290, 2024 facelift)", powertrains=["diesel", "BEV"],
  status_note="On sale: toyota.ch from CHF 45'834; DE, UK lists (Proace Max / Proace Max Electric).",
  status_sources=[TOYOTA_CH, TOYOTA_DE, TOYOTA_UK],
  twin_tier=1, twin_members=["Fiat Ducato", "Peugeot Boxer", "Citroën Jumper", "Opel/Vauxhall Movano"],
  twin_note="Rebadged Stellantis Ducato (Sevel Sud, Atessa) with Toyota badging; launched 2024.",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_ProAce_Max"],
  wikipedia_en="Toyota ProAce Max", commons_category="Category:Toyota ProAce Max",
  notes="Length given for L2H2 (approx.); range 4963–6363 mm."),

m(**T, model="GR Supra", display="GR Supra", ch_on_sale=False, ch_source=TOYOTA_CH, row="sports",
  body="2-door coupé", generation="V / J29/A90 (2019–2026)", length_mm=4379,
  platform="BMW CLAR (built by Magna Steyr, Graz)", powertrains=["petrol"],
  status="runout",
  status_note="Production ends in 2026 with the A90 Final Edition; still listed in the toyota.de model filter (1 configuration) in Oct 2026, but no longer offered on toyota.ch or in the toyota.co.uk range. Treat as runout; verifier should check whether toyota.de still allows orders.",
  status_sources=[TOYOTA_DE, "https://www.auto123.com/en/news/amp/2026-toyota-gr-supra-final-edition/72608", TOYOTA_CH],
  twin_tier=2, twin_members=["BMW Z4"],
  twin_note="Developed jointly with BMW; shares the CLAR platform, engines and Magna Steyr assembly with the BMW Z4 (G29), distinct coupé body (tier 2 per brief).",
  twin_sources=["https://en.wikipedia.org/wiki/Toyota_GR_Supra"],
  wikipedia_en="Toyota GR Supra", commons_category="Category:Toyota GR Supra",
  notes="Open question: whether any European importer still takes orders in Oct 2026."),
]

ANNOUNCED += [
m(**T, model="GR GT", display="GR GT", ch_on_sale=False, ch_source="https://de.toyota.ch/neuwagen-kaufen/coming-soon/gr-gt", row="sports",
  body="2-door front-engined GT / supercar", generation="I (expected 2027)", length_mm=None,
  platform="all-aluminium frame, carbon bonnet/roof (Toyota GR)", powertrains=["petrol"],
  status="announced",
  status_note="Listed as 'Demnächst: Der GR GT' (coming soon) on toyota.ch with a 'subscribe for information' form only; no price, no order date. Expected market launch 2027 (to verify).",
  status_sources=["https://de.toyota.ch/neuwagen-kaufen/coming-soon/gr-gt", "https://de.toyota.ch/neuwagen-kaufen/sportwagen"],
  wikipedia_en="Toyota GR GT", commons_category=None,
  notes="Front-engine, rear-wheel drive, >320 km/h per toyota.ch. Hybrid V8 reported in press; powertrain not confirmed from an official source here."),
]

DISCONTINUED += [
 {"brand": "Toyota", "model": "GR86", "note": "Withdrawn from Europe (limited 2-year run 2022–2024; GSR2 safety/emissions rules). Not on toyota.ch/.de/.co.uk in Oct 2026.", "source": "https://foro3d.com/en/2026/january/the-toyota-gr86-bids-farewell-to-the-european-market-due-to-emissions-regulations.html"},
 {"brand": "Toyota", "model": "Camry", "note": "UK sales ended Nov 2021; the XV80 generation was not launched in Western Europe. Listed under 'Previous Models' on toyota.co.uk; absent from toyota.ch/.de.", "source": "https://www.autocar.co.uk/car-news/new-cars/toyota-camry-goes-sale-just-months-after-facelift"},
 {"brand": "Toyota", "model": "Highlander", "note": "Fourth-generation Highlander (Europe 2021–2024) is a 'Previous Model' on toyota.co.uk and absent from toyota.ch/.de (filter shows 0 results). The 2026 Highlander BEV is US-only.", "source": "https://www.toyota.co.uk/new-cars"},
 {"brand": "Toyota", "model": "Corolla Sedan", "note": "Saloon body not offered in CH/DE/UK (UK lists 'Corolla Saloon' as previous model); same nameplate as Corolla anyway.", "source": "https://www.toyota.co.uk/new-cars"},
]

# ================================================================================================
# LEXUS
# ================================================================================================
MODELS += [
m(**L, model="LBX", display="LBX", ch_on_sale=True, ch_source=LEXUS_CH, row="b-suv",
  body="5-door crossover SUV", generation="I (2023–)", length_mm=4190,
  platform="TNGA GA-B", powertrains=["HEV"],
  status_note="On sale: listed on lexus.ch, lexus.de and lexus.co.uk model lists (Oct 2026).",
  status_sources=[LEXUS_CH, LEXUS_DE, LEXUS_UK],
  twin_tier=2, twin_members=["Toyota Yaris Cross"],
  twin_note="GA-B platform sibling of the Toyota Yaris Cross (same 1.5 hybrid, 20 mm longer wheelbase, distinct body).",
  twin_sources=["https://en.wikipedia.org/wiki/Lexus_LBX"],
  wikipedia_en="Lexus LBX", commons_category="Category:Lexus LBX"),

m(**L, model="UX", display="UX", ch_on_sale=True, ch_source=LEXUS_CH, row="c-suv",
  body="5-door crossover SUV", generation="I / ZA10 (2018–; facelift 2024, UX 300h)", length_mm=4495,
  platform="TNGA GA-C", powertrains=["HEV"],
  status_note="On sale as UX 300h hybrid (lexus.ch/.de/.co.uk). The battery-electric UX 300e is listed under 'Previous Models' on lexus.co.uk, i.e. dropped.",
  status_sources=[LEXUS_CH, LEXUS_DE, LEXUS_UK],
  twin_tier=2, twin_members=["Toyota C-HR", "Toyota Corolla Cross"],
  twin_note="GA-C platform sibling of the Toyota C-HR and Corolla Cross (2640 mm wheelbase), distinct body.",
  twin_sources=["https://en.wikipedia.org/wiki/Lexus_UX"],
  wikipedia_en="Lexus UX", commons_category="Category:Lexus UX"),

m(**L, model="NX", display="NX", ch_on_sale=True, ch_source=LEXUS_CH, row="c-suv",
  body="5-door SUV", generation="II / AZ20 (2021–)", length_mm=4660,
  platform="TNGA GA-K", powertrains=["HEV", "PHEV"],
  status_note="On sale (NX 350h, NX 450h+) on lexus.ch/.de/.co.uk.",
  status_sources=[LEXUS_CH, LEXUS_DE, LEXUS_UK],
  twin_tier=2, twin_members=["Toyota RAV4", "Suzuki Across"],
  twin_note="GA-K platform sibling of the Toyota RAV4 (and its Suzuki Across twin); distinct body.",
  twin_sources=["https://en.wikipedia.org/wiki/Lexus_NX"],
  wikipedia_en="Lexus NX", commons_category="Category:Lexus NX (AZ20)",
  notes="4660 mm is on the c-suv/d-suv boundary; kept in c-suv with its RAV4 sibling (brief lists 'NX?' in c-suv)."),

m(**L, model="RX", display="RX", ch_on_sale=True, ch_source=LEXUS_CH, row="e-suv",
  body="5-door SUV", generation="V / AL30 (2022–)", length_mm=4890,
  platform="TNGA GA-K", powertrains=["HEV", "PHEV"],
  status_note="On sale (RX 350h, 450h+, 500h) on lexus.ch/.de/.co.uk.",
  status_sources=[LEXUS_CH, LEXUS_DE, LEXUS_UK],
  wikipedia_en="Lexus RX", commons_category="Category:Lexus RX (AL30)",
  notes="Row per brief guidance (RX listed in e-suv)."),

m(**L, model="RZ", display="RZ", ch_on_sale=True, ch_source=LEXUS_CH, row="d-suv",
  body="5-door electric SUV", generation="I (2023–; facelift 2025)", length_mm=4805,
  platform="e-TNGA", powertrains=["BEV"],
  status_note="On sale (RZ 350e/450e/550e F Sport after 2025 update) on lexus.ch/.de/.co.uk.",
  status_sources=[LEXUS_CH, LEXUS_DE, LEXUS_UK],
  twin_tier=2, twin_members=["Toyota bZ4X", "Subaru Solterra"],
  twin_note="e-TNGA platform sibling of the bZ4X/Solterra twins (same 2850 mm wheelbase), distinct body.",
  twin_sources=["https://en.wikipedia.org/wiki/Lexus_RZ"],
  wikipedia_en="Lexus RZ", commons_category="Category:Lexus RZ"),

m(**L, model="ES", display="ES", ch_on_sale=True, ch_source="https://de.lexus.ch/modelle/es", row="e-car",
  body="4-door saloon", generation="VIII / XZ20 (2025–; Europe 2026)", length_mm=5140,
  platform="TNGA GA-K", powertrains=["HEV", "BEV"],
  status_note="The all-new ES (hybrid ES 300h and battery-electric ES 350e/500e) is listed on lexus.ch ('/new-cars/es/overview'), lexus.de and lexus.co.uk ('All-New ES') in Oct 2026; the previous ES is still shown on lexus.co.uk as well. Order status of the BEV versions to verify.",
  status_sources=[LEXUS_CH, LEXUS_DE, LEXUS_UK],
  wikipedia_en="Lexus ES", commons_category="Category:Lexus ES (XZ20)",
  notes="Generation code and Commons category name to verify; the Commons category may still be 'Category:Lexus ES (XZ10)' for the outgoing car."),

m(**L, model="LM", display="LM", ch_on_sale=True, ch_source=LEXUS_CH, row="mpv-large",
  body="luxury MPV (4/7 seats)", generation="II / TAH40 (2023–)", length_mm=5125,
  platform="TNGA GA-K", powertrains=["HEV"],
  status_note="On sale (LM 350h) on lexus.ch/.de/.co.uk.",
  status_sources=[LEXUS_CH, LEXUS_DE, LEXUS_UK],
  twin_tier=None, twin_members=[],
  twin_note="Based on the Toyota Alphard/Vellfire, which are not sold in Europe.",
  wikipedia_en="Lexus LM", commons_category="Category:Lexus LM (TAH40)"),
]

ANNOUNCED += [
m(**L, model="TZ", display="TZ", ch_on_sale=False, ch_source="https://de.lexus.ch/modelle/tz-world-premiere", row="e-suv",
  body="6-seat three-row electric SUV", generation="I (Europe 2027)", length_mm=5100,
  platform="Toyota BEV platform shared with the US-only Highlander BEV", powertrains=["BEV"],
  status="announced",
  status_note="World premiere 7 May 2026; 'keep me informed' form only on lexus.ch (Oct 2026). European market launch expected 2027 (electrive, t-online). 77 / 95.8 kWh, AWD 230 or 300 kW.",
  status_sources=["https://de.lexus.ch/modelle/tz-world-premiere", "https://www.electrive.com/2026/05/07/toyota-unveils-electric-highlander-alongside-lexus-tz/", "https://www.t-online.de/mobilitaet/aktuelles/id_101245268/lexus-tz-elektro-suv-startet-2027-in-der-oberklasse-in-europa.html"],
  twin_tier=None, twin_members=[],
  twin_note="Sister model of the Toyota Highlander BEV, which is intended for the US market only (no European twin).",
  twin_sources=["https://www.electrive.com/2026/05/07/toyota-unveils-electric-highlander-alongside-lexus-tz/"],
  wikipedia_en="Lexus TZ", commons_category=None),
]

DISCONTINUED += [
 {"brand": "Lexus", "model": "LC", "note": "LC coupé/convertible removed from UK and mainland European sale in 2024 (homologation issues); global production ends after MY2026. Not on lexus.ch/.de/.co.uk.", "source": "https://autos.yahoo.com/lexus-line-goes-electrified-only-113019931.html"},
 {"brand": "Lexus", "model": "RC / RC F", "note": "RC F withdrawn from UK/Europe in 2024 together with the LC.", "source": "https://autos.yahoo.com/lexus-line-goes-electrified-only-113019931.html"},
 {"brand": "Lexus", "model": "LS", "note": "Listed under 'Previous Models' on lexus.co.uk and absent from lexus.ch/.de in Oct 2026.", "source": "https://www.lexus.co.uk/"},
 {"brand": "Lexus", "model": "UX 300e", "note": "Battery-electric UX listed as a previous model on lexus.co.uk; UX continues as UX 300h hybrid.", "source": "https://www.lexus.co.uk/"},
]

# ================================================================================================
# SUBARU
# ================================================================================================
MODELS += [
m(**SB, model="Impreza", display="Impreza", ch_on_sale=True, ch_source=SUBARU_CH, row="c-hatch",
  body="5-door hatchback", generation="VI / GU (2023–; Europe 2024)", length_mm=4475,
  platform="Subaru Global Platform", powertrains=["MHEV"],
  status_note="Listed on subaru.ch and subaru.de (Oct 2026); not in the UK range. 2.0 e-Boxer mild hybrid, AWD.",
  status_sources=[SUBARU_CH, SUBARU_DE],
  twin_tier=None, twin_members=[],
  twin_note="Crosstrek is the raised crossover derivative of the same car (different row: c-suv).",
  wikipedia_en="Subaru Impreza", commons_category="Category:Subaru Impreza (GU)"),

m(**SB, model="Crosstrek", display="Crosstrek", ch_on_sale=True, ch_source=SUBARU_CH, row="c-suv",
  body="5-door crossover SUV", generation="III / GU (2023–)", length_mm=4495,
  platform="Subaru Global Platform", powertrains=["MHEV", "HEV"],
  status_note="On sale: subaru.ch, subaru.de, subaru.co.uk (from GBP 35'995; e-Boxer mild hybrid and new 'Self-Charging Hybrid').",
  status_sources=[SUBARU_CH, SUBARU_DE, SUBARU_UK],
  twin_tier=None, twin_members=[],
  twin_note="Crossover version of the Impreza (different row). Former name XV in Europe until 2023.",
  wikipedia_en="Subaru Crosstrek", commons_category="Category:Subaru Crosstrek (GU)",
  notes="Other name 'XV' no longer used."),

m(**SB, model="Forester", display="Forester", ch_on_sale=True, ch_source=SUBARU_CH, row="c-suv",
  body="5-door SUV", generation="VI / SL (2024–; Europe 2025)", length_mm=4670,
  platform="Subaru Global Platform", powertrains=["MHEV", "HEV"],
  status_note="On sale: subaru.ch, subaru.de, subaru.co.uk (from GBP 39'995; e-Boxer mild hybrid and strong hybrid).",
  status_sources=[SUBARU_CH, SUBARU_DE, SUBARU_UK],
  wikipedia_en="Subaru Forester", commons_category="Category:Subaru Forester (SL)",
  notes="4670 mm is on the c-suv/d-suv boundary; Subaru positions it as a compact/family SUV against the RAV4, so c-suv."),

m(**SB, model="Outback", display="Outback", ch_on_sale=True, ch_source=SUBARU_CH, row="d-car",
  body="5-door raised estate", generation="VI / BT (2019–; Europe 2021–)", length_mm=4870,
  platform="Subaru Global Platform", powertrains=["petrol"],
  status="runout",
  status_note="Still listed on subaru.ch and subaru.co.uk (body type 'Estate'), but subaru.de shows it with a 'Letzte Chance' (last chance) badge in Oct 2026: the seventh-generation Outback is not planned for Europe, where the name passes to the electric E-Outback.",
  status_sources=[SUBARU_DE, SUBARU_CH, SUBARU_UK, "https://carsguide.com.au/car-news/an-outback-ev-next-gen-2026-subaru-outback-could-skip-the-uk-and-europe-but-the-name-might"],
  wikipedia_en="Subaru Outback", commons_category="Category:Subaru Outback (BT)",
  notes="Row: subaru.co.uk classifies it as an estate, hence d-car; verifier may prefer d-suv next to the E-Outback."),

m(**SB, model="Solterra", display="Solterra", ch_on_sale=True, ch_source=SUBARU_CH, row="d-suv",
  body="5-door electric SUV", generation="I (2022–; facelift 2025/26)", length_mm=4690,
  platform="e-TNGA (e-Subaru Global Platform)", powertrains=["BEV"],
  status_note="On sale: subaru.ch, subaru.de, subaru.co.uk (from GBP 52'505); the facelifted Solterra is shown as 'Coming Soon' on subaru.co.uk alongside the current car.",
  status_sources=[SUBARU_CH, SUBARU_DE, SUBARU_UK],
  twin_tier=1, twin_members=["Toyota bZ4X"],
  twin_note="Twin of the Toyota bZ4X (joint development, same body shell, built by Toyota). Lexus RZ is a platform sibling (tier 2).",
  twin_sources=["https://en.wikipedia.org/wiki/Subaru_Solterra"],
  wikipedia_en="Subaru Solterra", commons_category="Category:Subaru Solterra"),

m(**SB, model="Uncharted", display="Uncharted", ch_on_sale=True, ch_source=SUBARU_CH, row="c-suv",
  body="5-door electric SUV", generation="I (2026–)", length_mm=4520,
  platform="e-TNGA (e-Subaru Global Platform)", powertrains=["BEV"],
  status_note="Listed on subaru.ch (Oct 2026) and on subaru.de with a 'new' badge; subaru.co.uk shows it as 'Coming Soon'. Treated as on sale (orders open in CH/DE); verifier should confirm the German order status.",
  status_sources=[SUBARU_CH, SUBARU_DE, SUBARU_UK],
  twin_tier=1, twin_members=["Toyota C-HR+"],
  twin_note="Subaru-badged version of the Toyota C-HR+ (same body shell, Subaru front/rear design), built by Toyota.",
  twin_sources=["https://en.wikipedia.org/wiki/Subaru_Uncharted"],
  wikipedia_en="Subaru Uncharted", commons_category="Category:Subaru Uncharted"),

m(**SB, model="E-Outback", display="E-Outback", ch_on_sale=True, ch_source=SUBARU_CH, row="d-suv",
  body="5-door electric estate-SUV", generation="I (2026–)", length_mm=4830,
  platform="e-TNGA (e-Subaru Global Platform)", powertrains=["BEV"],
  status_note="Listed on subaru.ch and on subaru.de with a 'NEU' badge (Oct 2026); subaru.co.uk 'Coming Soon'. Treated as on sale in CH/DE; order status to be confirmed by the verifier.",
  status_sources=[SUBARU_CH, SUBARU_DE, SUBARU_UK],
  twin_tier=1, twin_members=["Toyota bZ4X Touring"],
  twin_note="Twin of the Toyota bZ4X Touring; sold as Subaru Trailseeker in North America.",
  twin_sources=["https://en.wikipedia.org/wiki/Subaru_Trailseeker"],
  wikipedia_en="Subaru Trailseeker", commons_category="Category:Subaru Trailseeker",
  notes="Spelled 'E-Outback' on subaru.ch; 'E-OUTBACK' on subaru.de."),
]

DISCONTINUED += [
 {"brand": "Subaru", "model": "BRZ", "note": "Second-generation BRZ was never properly launched in Europe (GSR2 rules); only appears in a hero slider on subaru.de, not in the CH/DE/UK model lists. Verify whether a German 'Final Edition' stock sale exists.", "source": "https://www.autoscout24.fr/informer/actualite/la-nouvelle-subaru-brz-fait-ses-debuts-ce-mois-ci-mais-pas-en-europe"},
 {"brand": "Subaru", "model": "Levorg", "note": "Second-generation Levorg was not sold in Europe (ended 2020/21).", "source": "https://www.subaru.ch/de/modelle"},
 {"brand": "Subaru", "model": "XV", "note": "Renamed Crosstrek with the 2023 generation.", "source": "https://www.subaru.ch/de/modelle"},
]

# ================================================================================================
# SUZUKI
# ================================================================================================
MODELS += [
m(**SZ, model="Swift", display="Swift", ch_on_sale=True, ch_source=SUZUKI_CH, row="b-hatch",
  body="5-door hatchback", generation="IV / A2L (2024–)", length_mm=3860,
  platform="Heartect", powertrains=["MHEV"],
  status_note="On sale: suzuki.ch (Oct 2026); 1.2 three-cylinder 12V mild hybrid, FWD or AllGrip.",
  status_sources=[SUZUKI_CH],
  wikipedia_en="Suzuki Swift", commons_category="Category:Suzuki Swift (A2L)"),

m(**SZ, model="Vitara", display="Vitara", ch_on_sale=True, ch_source=SUZUKI_CH, row="b-suv",
  body="5-door SUV", generation="IV / LY (2015–; facelifts 2018, 2024)", length_mm=4175,
  platform="Suzuki Global C (Vitara/S-Cross)", powertrains=["MHEV", "HEV"],
  status_note="On sale: suzuki.ch (Oct 2026); 1.4 Boosterjet 48V mild hybrid and 1.5 strong hybrid.",
  status_sources=[SUZUKI_CH],
  wikipedia_en="Suzuki Vitara", commons_category="Category:Suzuki Vitara (LY)"),

m(**SZ, model="S-Cross", display="S-Cross", ch_on_sale=True, ch_source=SUZUKI_CH, row="c-suv",
  body="5-door SUV", generation="II / JY (2021–)", length_mm=4300,
  platform="Suzuki Global C (Vitara/S-Cross)", powertrains=["MHEV", "HEV"],
  status_note="On sale: suzuki.ch (Oct 2026); 1.4 Boosterjet 48V mild hybrid and 1.5 strong hybrid.",
  status_sources=[SUZUKI_CH],
  wikipedia_en="Suzuki S-Cross", commons_category="Category:Suzuki S-Cross (JY)",
  notes="Row judgement: only 4300 mm long (b-suv by length) but positioned by Suzuki as its C-segment SUV above the Vitara; placed in c-suv."),

m(**SZ, model="Across", display="Across", ch_on_sale=True, ch_source="https://www.suzuki.ch/de/modelle/across", row="c-suv",
  body="5-door SUV", generation="II (2025/26–)", length_mm=4600,
  platform="TNGA GA-K", powertrains=["PHEV"],
  status_note="Listed as 'NEW' on suzuki.ch (Oct 2026): second-generation Across, a rebadged sixth-generation RAV4 plug-in hybrid.",
  status_sources=[SUZUKI_CH],
  twin_tier=1, twin_members=["Toyota RAV4"],
  twin_note="Rebadged Toyota RAV4 PHEV (Toyota–Suzuki alliance), Suzuki-specific grille/bumper.",
  twin_sources=["https://en.wikipedia.org/wiki/Suzuki_Across", SUZUKI_CH],
  wikipedia_en="Suzuki Across", commons_category="Category:Suzuki Across",
  notes="Commons category for the second generation may not exist yet; first-generation category is 'Category:Suzuki Across'."),

m(**SZ, model="e Vitara", display="e Vitara", ch_on_sale=True, ch_source="https://www.suzuki.ch/de/modelle/e-vitara", row="b-suv",
  body="5-door electric SUV", generation="I (2025–)", length_mm=4275,
  platform="Heartect-e", powertrains=["BEV"],
  status_note="Listed as 'NEW' on suzuki.ch (Oct 2026); Suzuki's first BEV, built in Gujarat (India); 49 / 61 kWh, 2WD or AllGrip-e.",
  status_sources=[SUZUKI_CH],
  twin_tier=1, twin_members=["Toyota Urban Cruiser"],
  twin_note="Toyota Urban Cruiser is the Toyota-badged twin built on the same line.",
  twin_sources=["https://en.wikipedia.org/wiki/Suzuki_e_Vitara"],
  wikipedia_en="Suzuki e Vitara", commons_category="Category:Suzuki e Vitara"),
]

DISCONTINUED += [
 {"brand": "Suzuki", "model": "Ignis", "note": "Dropped from the European range in 2025 (CO2 fleet targets); not on suzuki.ch in Oct 2026.", "source": "https://www.motor1.com/news/725920/why-suzuki-stops-selling-swace-ignis-jimny/"},
 {"brand": "Suzuki", "model": "Swace", "note": "Corolla Touring Sports twin dropped from Europe in 2025; not on suzuki.ch in Oct 2026.", "source": "https://www.motor1.com/news/725920/why-suzuki-stops-selling-swace-ignis-jimny/"},
 {"brand": "Suzuki", "model": "Jimny", "note": "Two-seat N1 'commercial' Jimny withdrawn from Europe (2024/25 per Suzuki; not on suzuki.ch in Oct 2026). Verifier: check whether any EU importer still lists LCV stock.", "source": "https://www.autocarindia.com/car-news-amp/suzuki-to-stop-selling-jimny-in-europe-this-year-432185"},
 {"brand": "Suzuki", "model": "Swift Sport", "note": "No Swift Sport for the 2024 generation.", "source": "https://www.motor1.com/news/725920/why-suzuki-stops-selling-swace-ignis-jimny/"},
]

# ================================================================================================
# MAZDA
# ================================================================================================
MODELS += [
m(**MZ, model="Mazda2 Hybrid", display="Mazda2 Hybrid", ch_on_sale=True, ch_source=MAZDA_CH, row="b-hatch",
  body="5-door hatchback", generation="I (2022–; facelift 2024)", length_mm=3940,
  platform="TNGA GA-B", powertrains=["HEV"],
  status_note="Listed in the model keywords of mazda.ch and mazda.de (Oct 2026); Toyota Yaris-based hybrid.",
  status_sources=[MAZDA_CH, MAZDA_DE],
  twin_tier=1, twin_members=["Toyota Yaris"],
  twin_note="Rebadged Toyota Yaris hybrid built by Toyota in Valenciennes (France); Mazda-specific grille since the 2024 facelift.",
  twin_sources=["https://en.wikipedia.org/wiki/Mazda2_Hybrid"],
  wikipedia_en="Mazda2 Hybrid", commons_category="Category:Mazda2 Hybrid"),

m(**MZ, model="Mazda2", display="Mazda2", ch_on_sale=None, ch_source=MAZDA_CH, row="b-hatch",
  body="5-door hatchback", generation="III / DJ (2014–; facelift 2023)", length_mm=4080,
  platform="Skyactiv (DJ)", powertrains=["MHEV"],
  status="runout",
  status_note="Japan-built Mazda2 reported to be phased out in Europe by the end of 2025 (Carscoops, 25 Mar 2025); still appears in the mazda.ch and mazda.de model keyword lists in Oct 2026. Status could not be confirmed from the model page within the budget: treat as runout/uncertain.",
  status_sources=["https://www.carscoops.com/2025/03/four-mazda-models-are-being-discontinued-this-year-but-one-could-return/", MAZDA_DE, MAZDA_CH],
  wikipedia_en="Mazda2", commons_category="Category:Mazda Demio (DJ)",
  notes="OPEN QUESTION for verifier: is the Mazda-built Mazda2 (e-Skyactiv G 1.5) still orderable in any European market in Oct 2026? If not, move to discontinued."),

m(**MZ, model="Mazda3", display="Mazda3", ch_on_sale=True, ch_source=MAZDA_CH, row="c-hatch",
  body="5-door hatchback + 4-door saloon", generation="IV / BP (2019–)", length_mm=4460,
  platform="Skyactiv-Vehicle Architecture", powertrains=["MHEV"],
  status_note="Listed on mazda.ch (hatchback and sedan) and mazda.de (Oct 2026); e-Skyactiv G 2.5 mild hybrid in 2026 range.",
  status_sources=[MAZDA_CH, MAZDA_DE],
  wikipedia_en="Mazda3 (BP)", commons_category="Category:Mazda3 (BP)"),

m(**MZ, model="CX-30", display="CX-30", ch_on_sale=True, ch_source=MAZDA_CH, row="c-suv",
  body="5-door crossover SUV", generation="I / DM (2019–)", length_mm=4395,
  platform="Skyactiv-Vehicle Architecture", powertrains=["MHEV"],
  status_note="Listed on mazda.ch and mazda.de (Oct 2026).",
  status_sources=[MAZDA_CH, MAZDA_DE],
  twin_tier=None, twin_members=[],
  twin_note="Platform shared with Mazda3 (different row).",
  wikipedia_en="Mazda CX-30", commons_category="Category:Mazda CX-30"),

m(**MZ, model="CX-5", display="CX-5", ch_on_sale=True, ch_source=MAZDA_CH, row="c-suv",
  body="5-door SUV", generation="III / KJ (2025–; Europe 2026)", length_mm=4690,
  platform="Skyactiv (KJ)", powertrains=["MHEV"],
  status_note="Listed on mazda.ch and mazda.de (Oct 2026). Third generation launched in Europe in 2026 with the 2.5 e-Skyactiv G mild hybrid; generation on the Swiss page could not be verified within the budget.",
  status_sources=[MAZDA_CH, MAZDA_DE],
  wikipedia_en="Mazda CX-5", commons_category="Category:Mazda CX-5 (KJ)",
  notes="Row judgement: new CX-5 is 4690 mm (boundary) but positioned by Mazda as its compact SUV below the CX-60, so c-suv. Verifier: confirm the Swiss/German pages show the new generation."),

m(**MZ, model="CX-60", display="CX-60", ch_on_sale=True, ch_source=MAZDA_CH, row="d-suv",
  body="5-door SUV", generation="I / KH (2022–; update 2025)", length_mm=4745,
  platform="Skyactiv Multi-Solution Scalable Architecture (RWD-based)", powertrains=["petrol", "diesel", "PHEV"],
  status_note="Listed on mazda.ch and mazda.de (Oct 2026); e-Skyactiv D 3.3 (48V), e-Skyactiv PHEV 2.5, 2.5 petrol in some markets.",
  status_sources=[MAZDA_CH, MAZDA_DE],
  twin_tier=None, twin_members=[],
  twin_note="CX-80 is the stretched three-row derivative (different row).",
  wikipedia_en="Mazda CX-60", commons_category="Category:Mazda CX-60"),

m(**MZ, model="CX-80", display="CX-80", ch_on_sale=True, ch_source=MAZDA_DE, row="e-suv",
  body="5-door three-row SUV", generation="I / KL (2024–)", length_mm=4995,
  platform="Skyactiv Multi-Solution Scalable Architecture (RWD-based)", powertrains=["MHEV", "PHEV"],
  status_note="Listed on mazda.de (Oct 2026); e-Skyactiv D 3.3 48V mild hybrid and 2.5 PHEV. Absent from the mazda.ch keyword list (probably stale metadata) - Swiss status to verify.",
  status_sources=[MAZDA_DE],
  twin_tier=None, twin_members=[],
  twin_note="Long-wheelbase derivative of the CX-60 (different row).",
  wikipedia_en="Mazda CX-80", commons_category="Category:Mazda CX-80"),

m(**MZ, model="MX-5", display="MX-5", ch_on_sale=True, ch_source=MAZDA_CH, row="sports",
  body="2-seat roadster (soft-top) and RF (retractable hardtop)", generation="IV / ND (2015–; updates 2019, 2024)", length_mm=3915,
  platform="Skyactiv (ND)", powertrains=["petrol"],
  status_note="Listed on mazda.ch (MX-5 and MX-5 RF) and mazda.de (Oct 2026).",
  status_sources=[MAZDA_CH, MAZDA_DE],
  wikipedia_en="Mazda MX-5 (ND)", commons_category="Category:Mazda MX-5 (ND)"),

m(**MZ, model="Mazda 6e", display="Mazda 6e", ch_on_sale=None, ch_source=MAZDA_CH, row="d-car",
  body="5-door liftback saloon", generation="I (2025–)", length_mm=4921,
  platform="Changan EPA1 (Mazda EZ-6 / Deepal L07)", powertrains=["BEV"],
  status_note="Listed on mazda.de ('Mazda6e'/'6e', Oct 2026); on sale in Europe since 2025 (68.8 / 80 kWh RWD). Not in the mazda.ch keyword list (metadata possibly stale) - Swiss status to verify.",
  status_sources=[MAZDA_DE, "https://www.electrive.com/2026/01/14/mazda-discontinues-the-mx-30-r-ev-from-the-market"],
  twin_tier=1, twin_members=[],
  twin_note="Built by Changan Mazda in Nanjing; it is the Mazda-styled sister of the Changan Deepal L07 (Mazda EZ-6 in China). The Deepal L07 is not confirmed as sold in Europe, so no European twin member is listed; if the Changan agent finds the L07 on sale in Europe, add 'Deepal L07'.",
  twin_sources=["https://en.wikipedia.org/wiki/Mazda_EZ-6"],
  wikipedia_en="Mazda EZ-6", commons_category="Category:Mazda EZ-6"),

m(**MZ, model="CX-6e", display="CX-6e", ch_on_sale=None, ch_source="https://de.mazda.ch/", row="d-suv",
  body="5-door electric SUV", generation="I (2026–)", length_mm=4850,
  platform="Changan EPA1 (Mazda EZ-60 / Deepal S07)", powertrains=["BEV"],
  status_note="Orderable in Germany since 12 Feb 2026 from EUR 49'990 (Takumi), deliveries from summer 2026 (ecomento); listed on mazda.de; the Swiss homepage hero image is a CX-6e (Oct 2026).",
  status_sources=["https://ecomento.de/2026/02/12/mazda-elektroauto-cx-6e-fuer-49990-euro-bestellbar-mazda-cx-6e-in-deutschland-fuer-49990-euro-bestellbar/", MAZDA_DE],
  twin_tier=1, twin_members=["Deepal S07"],
  twin_note="Mazda-styled sister of the Changan Deepal S07 (Mazda EZ-60 in China), same EPA1 platform and body structure; Deepal S07 is sold in Europe (UK and other markets) by Changan.",
  twin_sources=["https://en.wikipedia.org/wiki/Mazda_EZ-60"],
  wikipedia_en="Mazda EZ-60", commons_category="Category:Mazda EZ-60",
  notes="78 kWh LFP, 190 kW RWD, 484 km WLTP. Verifier: confirm the Deepal S07 is on sale in Europe in Oct 2026 before joining the twin group."),
]

DISCONTINUED += [
 {"brand": "Mazda", "model": "MX-30", "note": "BEV withdrawn from DE/ES/NL end of 2024; MX-30 R-EV (rotary range extender) discontinued in Europe Jan 2026.", "source": "https://www.electrive.com/2026/01/14/mazda-discontinues-the-mx-30-r-ev-from-the-market"},
 {"brand": "Mazda", "model": "Mazda6", "note": "Discontinued in the UK 2023 and in Europe thereafter; mazda.ch keyword list still mentions Mazda6 (stale metadata).", "source": "https://www.carscoops.com/2025/03/four-mazda-models-are-being-discontinued-this-year-but-one-could-return/"},
 {"brand": "Mazda", "model": "CX-3", "note": "Already discontinued in Europe (2021); production ended Sept 2025.", "source": "https://www.carscoops.com/2025/03/four-mazda-models-are-being-discontinued-this-year-but-one-could-return/"},
]

# ================================================================================================
# HONDA
# ================================================================================================
MODELS += [
m(**H, model="Jazz", display="Jazz", ch_on_sale=True, ch_source=HONDA_CH, row="b-hatch",
  body="5-door hatchback (incl. Crosstar)", generation="IV / GR (2020–; facelift 2023)", length_mm=4045,
  platform="Honda global small car platform", powertrains=["HEV"],
  status_note="On sale: honda.ch from CHF 25'990; honda.de EUR 25'900; honda.co.uk GBP 28'475 (Oct 2026).",
  status_sources=[HONDA_CH, HONDA_DE, HONDA_UK],
  wikipedia_en="Honda Jazz", commons_category="Category:Honda Jazz (GR)"),

m(**H, model="Civic", display="Civic", ch_on_sale=True, ch_source=HONDA_CH, row="c-hatch",
  body="5-door hatchback", generation="XI / FL (2022–; facelift 2025)", length_mm=4550,
  platform="Honda Architecture", powertrains=["HEV"],
  status_note="On sale: honda.ch Civic e:HEV from CHF 35'990 (and Civic Type R from CHF 56'800 still listed); honda.de EUR 37'900; honda.co.uk GBP 34'325. Civic Type R (2.0 turbo petrol) ended European sales with the 2025 'Ultimate Edition' and is no longer on honda.de/.co.uk.",
  status_sources=[HONDA_CH, HONDA_DE, HONDA_UK],
  wikipedia_en="Honda Civic (eleventh generation)", commons_category="Category:Honda Civic (eleventh generation)",
  notes="Type R is the same tile (performance version); its Swiss stock listing may be runout."),

m(**H, model="HR-V", display="HR-V", ch_on_sale=True, ch_source=HONDA_CH, row="b-suv",
  body="5-door crossover SUV", generation="III / RV (2021–; facelift 2024)", length_mm=4340,
  platform="Honda global small car platform", powertrains=["HEV"],
  status_note="On sale: honda.ch from CHF 32'990 ('Neu'); honda.de EUR 33'900; honda.co.uk 'HR-V Hybrid 2026' GBP 32'725.",
  status_sources=[HONDA_CH, HONDA_DE, HONDA_UK],
  wikipedia_en="Honda HR-V", commons_category="Category:Honda HR-V (RV)"),

m(**H, model="ZR-V", display="ZR-V", ch_on_sale=True, ch_source=HONDA_CH, row="c-suv",
  body="5-door SUV", generation="I / RZ (2023–; update 2025)", length_mm=4568,
  platform="Honda Architecture (Civic-based)", powertrains=["HEV"],
  status_note="On sale: honda.ch from CHF 37'490 ('Neu'); honda.de EUR 40'900 ('Neu'); honda.co.uk GBP 36'525.",
  status_sources=[HONDA_CH, HONDA_DE, HONDA_UK],
  wikipedia_en="Honda ZR-V", commons_category="Category:Honda ZR-V"),

m(**H, model="CR-V", display="CR-V", ch_on_sale=True, ch_source=HONDA_CH, row="d-suv",
  body="5-door SUV", generation="VI / RS (2023–)", length_mm=4705,
  platform="Honda Architecture", powertrains=["HEV", "PHEV"],
  status_note="On sale: honda.ch CR-V Hybrid from CHF 47'990 and CR-V Plug-in Hybrid from CHF 48'490; honda.de EUR 46'900 / 54'400; honda.co.uk.",
  status_sources=[HONDA_CH, HONDA_DE, HONDA_UK],
  wikipedia_en="Honda CR-V", commons_category="Category:Honda CR-V (RS)"),

m(**H, model="Prelude", display="Prelude", ch_on_sale=True, ch_source=HONDA_CH, row="sports",
  body="2-door coupé", generation="VI / BC (2025–; Europe 2026)", length_mm=4520,
  platform="Honda Architecture (Civic-based)", powertrains=["HEV"],
  status_note="On sale: honda.ch from CHF 45'900 ('Neu'); honda.de EUR 49'500; honda.co.uk GBP 41'595 (Oct 2026).",
  status_sources=[HONDA_CH, HONDA_DE, HONDA_UK],
  wikipedia_en="Honda Prelude", commons_category="Category:Honda Prelude (sixth generation)"),

m(**H, model="Super-N", display="Super-N", ch_on_sale=False, ch_source=HONDA_CH, row="a-city",
  body="5-door city car", generation="I (2026–)", length_mm=3395,
  platform="Honda N-One e: (kei-car based BEV)", powertrains=["BEV"],
  status_note="On sale in the UK: honda.co.uk lists the Super-N at GBP 18'995 with a 'New Electric' label (Oct 2026). Not yet listed on honda.ch or honda.de.",
  status_sources=[HONDA_UK, HONDA_CH, HONDA_DE],
  wikipedia_en="Honda Super-N", commons_category="Category:Honda Super-N",
  notes="European version of the Japanese N-One e:; length approximate (kei-car body 3395 mm; European bumpers may add a few cm). Verifier: confirm launch in continental markets."),
]

DISCONTINUED += [
 {"brand": "Honda", "model": "e:Ny1", "note": "Removed from Honda's UK, DE, IT, ES and CH websites by April 2026 (still configurable in FR/AT at that time); production for Europe ended. Not on honda.ch/.de/.co.uk in Oct 2026.", "source": "https://www.electrive.com/2026/04/17/honda-withdraws-eny1-from-multiple-markets/"},
 {"brand": "Honda", "model": "Honda e", "note": "Discontinued 2024 (not on any Honda European site).", "source": "https://www.honda.co.uk/cars.html"},
 {"brand": "Honda", "model": "Civic Type R", "note": "European sales ended with the 2025 Ultimate Edition (same tile as Civic anyway); a Swiss listing at CHF 56'800 remained in Oct 2026.", "source": "https://www.de.honda.ch/cars.html"},
]

SOURCES += [
 {"url": TOYOTA_CH, "what": "Toyota Switzerland all-models page with CHF prices (22 models; 'Demnächst: GR GT'), fetched 2026-10-21"},
 {"url": "https://de.toyota.ch/neuwagen-kaufen/sportwagen", "what": "Toyota CH sports-car page: GR Yaris priced, GR GT 'Demnächst', GR86/GR Supra only mentioned in text"},
 {"url": TOYOTA_DE, "what": "Toyota Germany model filter (23 models incl. GR Supra; no GR86/Camry/Highlander)"},
 {"url": TOYOTA_UK, "what": "Toyota UK new-cars range list; Camry/Highlander/GT86 under previous models"},
 {"url": "https://media.toyota.co.uk/?p=67442", "what": "Toyota UK press release 13 May 2026: all-new Hilux range (Diesel 48V + BEV), orders from 1 June 2026"},
 {"url": "https://media.toyota.co.uk/?p=66870", "what": "Toyota UK press release 7 Apr 2026: sixth-generation RAV4 pricing, orders May 2026"},
 {"url": "https://www.electrifying.com/blog/article/prices-announced-for-electric-toyota-hilux", "what": "Electric Hilux UK price/on-sale date, 23 May 2026"},
 {"url": "https://foro3d.com/en/2026/january/the-toyota-gr86-bids-farewell-to-the-european-market-due-to-emissions-regulations.html", "what": "GR86 no longer available in Europe (19 Jan 2026)"},
 {"url": "https://www.motor1.com/news/707700/toyota-gr86-subaru-brz-dead-europe/", "what": "GR86 and BRZ dead in Europe (search result, 2024)"},
 {"url": "https://www.autocar.co.uk/car-news/new-cars/toyota-camry-goes-sale-just-months-after-facelift", "what": "Camry withdrawn from UK sale (Nov 2021)"},
 {"url": LEXUS_CH, "what": "Lexus Switzerland footer model list: LBX, UX, NX, RZ, ES, RX, LM, TZ"},
 {"url": LEXUS_DE, "what": "Lexus Germany models page (no LC/LS/IS/RC)"},
 {"url": LEXUS_UK, "what": "Lexus UK navigation incl. 'All-New ES'; previous models UX electric, CT, IS, RC, GS, LS"},
 {"url": "https://de.lexus.ch/modelle/tz-world-premiere", "what": "Lexus CH TZ world-premiere page: 5100 mm, 77/95.8 kWh, no price/order"},
 {"url": "https://www.electrive.com/2026/05/07/toyota-unveils-electric-highlander-alongside-lexus-tz/", "what": "Lexus TZ reveal, Europe 2027; Highlander BEV US-only"},
 {"url": "https://www.t-online.de/mobilitaet/aktuelles/id_101245268/lexus-tz-elektro-suv-startet-2027-in-der-oberklasse-in-europa.html", "what": "Lexus TZ due in Europe 2027 (5 Aug 2026)"},
 {"url": "https://www.motor1.com/news/786012/lexus-lc-dead-after-2026-model/", "what": "Lexus LC discontinued after MY2026 (30 Jan 2026)"},
 {"url": "https://autos.yahoo.com/lexus-line-goes-electrified-only-113019931.html", "what": "Autocar (12 Apr 2024): LC and RC F withdrawn from UK and mainland Europe"},
 {"url": SUBARU_CH, "what": "Subaru Switzerland models: Impreza, Crosstrek, Forester, Outback, Uncharted, Solterra, E-Outback"},
 {"url": SUBARU_DE, "what": "Subaru Germany navigation: same seven models; Outback 'Letzte Chance', E-Outback 'NEU', Uncharted 'new'; BRZ only in hero slider"},
 {"url": SUBARU_UK, "what": "Subaru UK: Crosstrek, Forester, Outback (estate), Solterra; Uncharted, new Solterra and E-Outback 'Coming Soon'"},
 {"url": "https://www.autoscout24.fr/informer/actualite/la-nouvelle-subaru-brz-fait-ses-debuts-ce-mois-ci-mais-pas-en-europe", "what": "New BRZ not for Europe (search result)"},
 {"url": "https://carsguide.com.au/car-news/an-outback-ev-next-gen-2026-subaru-outback-could-skip-the-uk-and-europe-but-the-name-might", "what": "Seventh-gen Outback may skip Europe; name used for the EV (search result)"},
 {"url": SUZUKI_CH, "what": "Suzuki Switzerland model menu: Swift, Vitara, S-Cross, Across (NEW), e Vitara (NEW)"},
 {"url": "https://www.motor1.com/news/725920/why-suzuki-stops-selling-swace-ignis-jimny/", "what": "Suzuki drops Ignis, Swace, Jimny in Europe from 2025 (9 Jul 2024)"},
 {"url": "https://www.autocarindia.com/car-news-amp/suzuki-to-stop-selling-jimny-in-europe-this-year-432185", "what": "Jimny LCV sales in Europe end 2024 (10 Jul 2024)"},
 {"url": MAZDA_CH, "what": "Mazda Switzerland models page (only meta keywords readable: Mazda2, Mazda2 Hybrid, Mazda3, CX-30, CX-5, CX-60, MX-30, MX-5, Mazda6)"},
 {"url": MAZDA_DE, "what": "Mazda Germany models page (meta keywords: Mazda2, Mazda2 Hybrid, Mazda3, CX-30, CX-5, CX-60, CX-80, MX-5, Mazda6e, CX-6e)"},
 {"url": "https://ecomento.de/2026/02/12/mazda-elektroauto-cx-6e-fuer-49990-euro-bestellbar-mazda-cx-6e-in-deutschland-fuer-49990-euro-bestellbar/", "what": "Mazda CX-6e orderable in Germany from EUR 49'990 (12 Feb 2026), 4850 mm"},
 {"url": "https://www.electrive.com/2026/01/14/mazda-discontinues-the-mx-30-r-ev-from-the-market", "what": "MX-30 R-EV discontinued in Europe; 6e and CX-6e are Changan-based (14 Jan 2026)"},
 {"url": "https://www.carscoops.com/2025/03/four-mazda-models-are-being-discontinued-this-year-but-one-could-return/", "what": "Mazda2, MX-30, CX-3, Mazda6 being discontinued (25 Mar 2025)"},
 {"url": HONDA_CH, "what": "Honda Switzerland cars page with CHF prices: Jazz, Prelude, Civic, Civic Type R, HR-V, ZR-V, CR-V Hybrid, CR-V PHEV"},
 {"url": HONDA_DE, "what": "Honda Germany cars page: Jazz, HR-V, Civic, ZR-V, CR-V, Prelude, CR-V PHEV"},
 {"url": HONDA_UK, "what": "Honda UK cars page: Super-N (GBP 18'995, new electric), Jazz, Civic, HR-V, ZR-V, Prelude, CR-V"},
 {"url": "https://www.electrive.com/2026/04/17/honda-withdraws-eny1-from-multiple-markets/", "what": "Honda e:Ny1 withdrawn from UK/DE/IT/ES/CH sites (17 Apr 2026)"},
 {"url": "https://www.carsized.com/en-us/cars/compare/renault-kangoo-2021-5-door-van-vs-ford-f/", "what": "carsized recipe test (side view URL format confirmed)"},
]


# ================================================================================================
# POST-PROCESSING: facts gathered after the first draft (2026-10-22) and carsized slugs
# ================================================================================================
UPDATES = {
 ("Toyota","Aygo X"): dict(powertrains=["HEV"], status_sources=[TOYOTA_CH, "https://de.toyota.ch/neuwagen-kaufen/aygo-x", TOYOTA_DE, TOYOTA_UK],
    notes="toyota.ch Aygo X page (fetched 2026-10-22) lists only the 1.5 full hybrid (116 PS, CVT) from CHF 19'900: hybrid-only after the 2025 update."),
 ("Toyota","Urban Cruiser"): dict(wikipedia_en="Toyota Urban Cruiser (BEV)", commons_category="Category:Toyota Urban Cruiser (BEV)",
    status_note="On sale: toyota.ch from CHF 31'900 (Oct 2026); toyota.de list; toyota.co.uk 'New Urban Cruiser'. European release Dec 2025, deliveries from Q1 2026 (Wikipedia, e Vitara article).",
    twin_sources=["https://en.wikipedia.org/wiki/Suzuki_e_Vitara"],
    notes="Length 4285 mm vs 4275 mm for the e Vitara (Wikipedia). Commons category name unverified."),
 ("Toyota","bZ4X"): dict(twin_sources=["https://en.wikipedia.org/wiki/Toyota_bZ4X"],
    twin_note="Solterra is the Subaru-badged twin (e-TNGA co-developed by Toyota and Subaru; Subaru calls it e-Subaru Global Platform). Lexus RZ is an e-TNGA platform sibling (tier 2, same row)."),
 ("Toyota","bZ4X Touring"): dict(twin_sources=["https://en.wikipedia.org/wiki/Toyota_bZ4X", "https://en.wikipedia.org/wiki/Subaru_Trailseeker"],
    status_note="On sale: toyota.ch from CHF 44'900 (Oct 2026); toyota.de list; toyota.co.uk 'All-New bZ4X Touring'. Wikipedia: 140 mm longer bZ4X derivative, European launch 2026 (FWD/AWD), 74.7 kWh.",
    notes="Subaru version is the E-Outback in Europe (Trailseeker elsewhere, 4845 mm)."),
 ("Toyota","GR Supra"): dict(length_mm=4380,
    status_note="Production of the A90 ended in March 2026 (Wikipedia); the A90 Final Edition (300 units, 150 for Europe) was unveiled Nov 2024. Still in the toyota.de model filter (1 configuration) in Oct 2026, not on toyota.ch or in the toyota.co.uk range. Treat as runout; verifier should check whether toyota.de still allows orders.",
    status_sources=[TOYOTA_DE, "https://en.wikipedia.org/wiki/Toyota_GR_Supra", TOYOTA_CH],
    twin_note="Joint Toyota-BMW sports car platform shared with the BMW Z4 (G29); both built by Magna Steyr in Graz (Wikipedia). Distinct coupé body (tier 2 per brief)."),
 ("Toyota","Hilux"): dict(notes="Length of the new generation not confirmed from a fetched source (approx. 5.3 m). carsized has only the previous generation (2016/2020 entries). Commons category name for the 9th generation to be verified."),
 ("Lexus","ES"): dict(ch_on_sale=True, status_sources=["https://www.lexus.de/new-cars/es/overview", LEXUS_CH, LEXUS_UK],
    status_note="Eighth-generation ES on sale: lexus.de shows 'der ES der achten Generation' from EUR 59'600 with configurator (ES 300h hybrid FWD/AWD and ES 350e BEV, 72 kWh net, 531-581 km); listed on lexus.ch and as 'All-New ES' on lexus.co.uk (Oct 2026). Revealed 23 Apr 2025 (Wikipedia; codes AXZH21/XXZM21/XXZM26).",
    generation="VIII (2025–; Europe 2026)", notes="5140 x 1920 x 1560 mm, wheelbase 2950 mm per lexus.de. Commons category name for the new generation unverified."),
 ("Lexus","LBX"): dict(twin_note="GA-B platform sibling of the Toyota Yaris Cross / Yaris (XP210): same 1.5 hybrid, 2580 mm wheelbase, distinct body (Wikipedia)."),
 ("Subaru","Uncharted"): dict(ch_on_sale=True, ch_source="https://www.subaru.ch/de/modelle/uncharted",
    status_note="Orderable in Switzerland: subaru.ch Uncharted page with 'Jetzt kaufen'/'Konfigurieren', Advantage 4x2 from CHF 36'490 to Luxury 4x4 CHF 46'990 (58 / 77 kWh, 168-343 PS, offer valid to 30.09.2026); listed on subaru.de ('new'); subaru.co.uk 'Coming Soon'. Wikipedia: European release Oct 2025, wider availability 2026.",
    status_sources=["https://www.subaru.ch/de/modelle/uncharted", SUBARU_DE, SUBARU_UK, "https://en.wikipedia.org/wiki/Subaru_Uncharted"],
    twin_sources=["https://en.wikipedia.org/wiki/Subaru_Uncharted"]),
 ("Subaru","E-Outback"): dict(status_note="Orderable in Germany: subaru.de E-OUTBACK page shows 'Ab Preis 51.990 EUR', MY26, configurator, 2 x 167 kW AWD, 526 km WLTP (Oct 2026); listed on subaru.ch; subaru.co.uk 'Coming Soon'.",
    status_sources=["https://www.subaru.de/e-outback", SUBARU_CH, SUBARU_UK],
    twin_sources=["https://en.wikipedia.org/wiki/Subaru_Trailseeker", "https://en.wikipedia.org/wiki/Toyota_bZ4X"]),
 ("Suzuki","Across"): dict(status_note="suzuki.ch 'NEW SUZUKI ACROSS' page: Compact Top 2.5 Plug-in Hybrid E-CVT 4x4 from CHF 56'490, 309 PS system output, 22.7 kWh battery, up to 129 km electric range (= the sixth-generation RAV4 PHEV hardware). In the UK the Across is now listed as used-only (cars.suzuki.co.uk), so the new generation is a continental-Europe model.",
    status_sources=["https://www.suzuki.ch/de/modelle/across", SUZUKI_CH, "https://cars.suzuki.co.uk/"],
    other_names=[]),
 ("Suzuki","e Vitara"): dict(status_note="Listed as 'NEW' on suzuki.ch and on cars.suzuki.co.uk from GBP 24'999 (Oct 2026); European release Sept 2025 (Wikipedia); 49 / 61 kWh LFP, 2WD or AllGrip-e.",
    status_sources=[SUZUKI_CH, "https://cars.suzuki.co.uk/", "https://en.wikipedia.org/wiki/Suzuki_e_Vitara"]),
 ("Suzuki","Swift"): dict(status_sources=[SUZUKI_CH, "https://cars.suzuki.co.uk/"], status_note="On sale: suzuki.ch (Oct 2026); cars.suzuki.co.uk from GBP 16'499; 1.2 three-cylinder 12V mild hybrid, FWD or AllGrip."),
 ("Suzuki","Vitara"): dict(status_sources=[SUZUKI_CH, "https://cars.suzuki.co.uk/"], status_note="On sale: suzuki.ch (Oct 2026); cars.suzuki.co.uk from GBP 21'999; 1.4 Boosterjet 48V mild hybrid and 1.5 strong hybrid."),
 ("Suzuki","S-Cross"): dict(status_sources=[SUZUKI_CH, "https://cars.suzuki.co.uk/"], status_note="On sale: suzuki.ch (Oct 2026); cars.suzuki.co.uk from GBP 22'999; 1.4 Boosterjet 48V mild hybrid and 1.5 strong hybrid."),
 ("Mazda","Mazda2"): dict(status_note="Japan-built Mazda2 reported to be phased out in Europe by the end of 2025 (Carscoops, 25 Mar 2025). mazda.co.uk still has a Mazda2 model page ('available in three petrol engines', offers link, no price) and the Mazda2 is still in the mazda.ch / mazda.de keyword lists in Oct 2026, which looks like remaining stock: marked runout.",
    status_sources=["https://www.mazda.co.uk/cars/mazda2/", "https://www.carscoops.com/2025/03/four-mazda-models-are-being-discontinued-this-year-but-one-could-return/", MAZDA_DE, MAZDA_CH]),
 ("Mazda","Mazda 6e"): dict(commons_category="Category:Mazda6e", twin_sources=["https://en.wikipedia.org/wiki/Mazda_EZ-6"],
    status_note="On sale in Europe since mid-2025 (introduced Brussels Motor Show 10 Jan 2025, first 600 cars shipped April 2025; BEV only, 68.8 / 80 kWh) per Wikipedia; listed on mazda.de ('Mazda6e', Oct 2026). Not in the mazda.ch keyword list (metadata possibly stale) - Swiss status to verify.",
    status_sources=["https://en.wikipedia.org/wiki/Mazda_EZ-6", MAZDA_DE, "https://www.electrive.com/2026/01/14/mazda-discontinues-the-mx-30-r-ev-from-the-market"],
    twin_note="Uses the same Changan EPA platform as the Deepal L07 liftback (Wikipedia) and is built by Changan Mazda in Nanjing. The Deepal L07 is not confirmed on sale in Europe (Wikipedia's Deepal article names only UK/Spain/Portugal as markets without listing models), so no European twin member is listed; add 'Deepal L07' if the Changan agent finds it on sale."),
 ("Mazda","CX-6e"): dict(commons_category="Category:Mazda CX-6e", twin_sources=["https://en.wikipedia.org/wiki/Mazda_EZ-60", "https://www.electrive.com/2026/01/14/mazda-discontinues-the-mx-30-r-ev-from-the-market"],
    twin_note="'Heavily based on' the Changan Deepal S07 (Wikipedia: shared BEV/EREV powertrains, EPA platform; EZ-60 in China). Deepal sells in the UK, Spain and Portugal (Wikipedia Deepal article), the S07 being its European model; verifier should confirm the S07 is on sale in Oct 2026 before joining the group.",
    status_note="Orderable in Germany since 12 Feb 2026 from EUR 49'990 (Takumi), deliveries from summer 2026 (ecomento); introduced in Europe at the Brussels Motor Show 9 Jan 2026 (Wikipedia); listed on mazda.de; the Swiss homepage hero image is a CX-6e (Oct 2026)."),
 ("Honda","Prelude"): dict(commons_category="Category:Honda Prelude", notes="Commons: only the parent category 'Category:Honda Prelude' confirmed (sixth-generation subcategory not checked). e:HEV 2.0, 203 PS system output (Wikipedia)."),
 ("Honda","Super-N"): dict(length_mm=3580, wikipedia_en="Honda N-One", commons_category="Category:Honda N-One",
    status_note="On sale in Great Britain: honda.co.uk Super-N page 'available at Honda retailers across GB' from GBP 18'995 OTR, 3.6 m long, up to 128 miles WLTP, 50 kW DC (Oct 2026). Not yet listed on honda.ch or honda.de.",
    status_sources=["https://www.honda.co.uk/cars/new/super-n/overview.html", HONDA_UK, HONDA_CH, HONDA_DE],
    notes="Wikipedia covers it in the Honda N-One article: the Super-N is the right-hand-drive-market name of the Super-One (widebody N-One e:, 3580 mm, 70 kW motor; Japan sales from 21 May 2026). Commons: parent category 'Category:Honda N-One'. Verifier: confirm launch in continental markets."),
}
for mm in MODELS:
    u = UPDATES.get((mm["brand"], mm["model"]))
    if u: mm.update(u)
for mm in ANNOUNCED:
    if (mm["brand"], mm["model"]) == ("Toyota","GR GT"):
        mm.update(length_mm=4820, powertrains=["HEV"],
                  status_note="Listed as 'Demnächst: Der GR GT' (coming soon) on toyota.ch with a 'subscribe for information' form only; no price, no order date (Oct 2026). World premiere 5 Dec 2025; production starts 2027 in Japan (Wikipedia). 4.0 V8 twin-turbo with transaxle hybrid, 650 PS.",
                  status_sources=["https://de.toyota.ch/neuwagen-kaufen/coming-soon/gr-gt", "https://de.toyota.ch/neuwagen-kaufen/sportwagen", "https://en.wikipedia.org/wiki/Toyota_GR_GT"],
                  notes="Front mid-engine RWD, all-aluminium frame, >320 km/h (toyota.ch). 4820 mm (Wikipedia).")

for d in DISCONTINUED:
    if d["brand"]=="Suzuki" and d["model"] in ("Ignis","Swace","Jimny","Swift Sport"):
        d["note"] += " cars.suzuki.co.uk (Oct 2026) lists it under used cars only."
    if d["brand"]=="Subaru" and d["model"]=="BRZ":
        d["note"] = "Second-generation BRZ was never properly launched in Europe (GSR2 rules; Autoscout24 FR 'pas en Europe'); only appears in a hero slider on subaru.de, not in the CH/DE/UK model lists, and https://www.subaru.de/brz could not be fetched (likely removed) on 2026-10-22."

# carsized slugs confirmed via search results (title = years shown by carsized); side/front URLs filled when fetched
CARSIZED = {
 ("Toyota","Aygo X"): ("toyota-aygo-x-2022-5-door-hatchback", "2022-present"),
 ("Toyota","Yaris"): ("toyota-yaris-2020-5-door-hatchback", "2020-present"),
 ("Toyota","Yaris Cross"): ("toyota-yaris-cross-2021-suv", "2021-present"),
 ("Toyota","Urban Cruiser"): ("toyota-urban-cruiser-2025-suv-bev", "2025-present"),
 ("Toyota","Corolla"): ("toyota-corolla-2018-5-door-hatchback", "2018-2023"),
 ("Toyota","Corolla Cross"): ("toyota-corolla-cross-2020-suv", "2020-present"),
 ("Toyota","C-HR"): ("toyota-c-hr-2023-suv", "2023-present"),
 ("Toyota","bZ4X"): ("toyota-bz4x-2022-suv", "2022-2025"),
 ("Toyota","RAV4"): ("toyota-rav4-2025-suv", "2025-present"),
 ("Toyota","Prius"): ("toyota-prius-2022-liftback", "2022-present"),
 ("Toyota","Mirai"): ("toyota-mirai-2020-sedan", "2020-present"),
 ("Toyota","Land Cruiser"): ("toyota-land-cruiser-prado-2023-suv", "2023-present"),
 ("Toyota","Proace City"): ("toyota-proace-city-2024-van-l2", "2024-present"),
 ("Toyota","Proace"): ("toyota-proace-2016-van-l2", "2016-2024"),
 ("Toyota","Proace Verso"): ("toyota-proace-verso-2016-van-l2", "2016-present"),
 ("Toyota","GR Supra"): ("toyota-supra-2019-2-door-liftback", "2019-present"),
 ("Lexus","LBX"): ("lexus-lbx-2023-suv", "2023-present"),
 ("Lexus","UX"): ("lexus-ux-2018-suv", "2018-present"),
 ("Lexus","NX"): ("lexus-nx-2021-suv", "2021-present"),
 ("Lexus","RX"): ("lexus-rx-2022-suv", "2022-present"),
 ("Lexus","RZ"): ("lexus-rz-2023-suv", "2023-present"),
 ("Subaru","Impreza"): ("subaru-impreza-2023-5-door-hatchback", "2023-present"),
 ("Subaru","Crosstrek"): ("subaru-crosstrek-2023-suv", "2023-present"),
 ("Subaru","Forester"): ("subaru-forester-2024-suv", "2024-present"),
 ("Subaru","Outback"): ("subaru-outback-2019-suv", "2019-2025"),
 ("Subaru","Solterra"): ("subaru-solterra-2022-suv", "2022-present"),
 ("Suzuki","Swift"): ("suzuki-swift-2023-5-door-hatchback", "2023-present"),
 ("Suzuki","Vitara"): ("suzuki-vitara-2018-suv", "2018-2024"),
 ("Suzuki","S-Cross"): ("suzuki-s-cross-2021-suv", "2021-present"),
 ("Mazda","Mazda2"): ("mazda-2-2014-5-door-hatchback", "2014-2019"),
 ("Mazda","Mazda3"): ("mazda-3-2019-5-door-hatchback", "2019-present"),
 ("Mazda","CX-30"): ("mazda-cx-30-2019-suv", "2019-present"),
 ("Honda","Jazz"): ("honda-jazz-fit-2020-5-door-hatchback", "2020-2023"),
 ("Honda","HR-V"): ("honda-hr-v-2021-suv", "2021-present"),
}
CARSIZED_NOTES = {
 ("Toyota","Corolla"): "carsized lists the hatchback as 2018-2023 (pre-facelift entry; no separate 2023 facelift entry found); estate entry 'toyota-corolla-2018-estate' is 2018-present.",
 ("Toyota","bZ4X"): "carsized entry covers 2022-2025 (pre-facelift); no separate entry for the 2025 update was found.",
 ("Toyota","Proace"): "carsized entry is the 2016-2024 pre-facelift Proace (L1 variant 'toyota-proace-2016-van-l1' also exists); no 2024-facelift entry found.",
 ("Suzuki","Vitara"): "carsized entry covers the 2018-2024 facelift; no entry for the 2024 update found.",
 ("Mazda","Mazda2"): "carsized entry is 2014-2019 (pre-facelift DJ); no later entry found.",
 ("Honda","Jazz"): "carsized entry 2020-2023 (pre-facelift); a 'honda-jazz-fit-2020-5-door-hatchback-crossover' entry exists for the Crosstar.",
 ("Toyota","Land Cruiser"): "carsized files the J250 as 'Land Cruiser Prado 2023-present'; 'toyota-land-cruiser-2021-suv' is the J300 (not sold in Europe).",
 ("Subaru","Outback"): "carsized classes the Outback as an SUV, 2019-2025.",
}
NO_CARSIZED = {
 ("Toyota","C-HR+"): "No carsized entry found for the C-HR+ (searches return only the C-HR); use Commons fallback.",
 ("Toyota","bZ4X Touring"): "No carsized entry found for bZ4X Touring / bZ Woodland / Trailseeker; use Commons fallback.",
 ("Toyota","Hilux"): "carsized has only the previous generation (toyota-hilux-2016-pickup-double-cab, toyota-hilux-2020-2-door-pickup-extra-cab); no entry for the 2026 Hilux; use Commons fallback.",
 ("Toyota","Proace City Verso"): "No separate carsized entry for the Proace City Verso (the van entry toyota-proace-city-2024-van-l2 shares the body); use Commons fallback or the Proace City image.",
 ("Toyota","Proace Max"): "No carsized entry found for the Proace Max; use Commons fallback (or the Fiat Ducato 2024 entry of the Stellantis agent).",
 ("Lexus","ES"): "carsized has only the previous ES (lexus-es-2018-sedan); no entry for the eighth generation; use Commons fallback.",
 ("Lexus","LM"): "No carsized entry found for the Lexus LM; use Commons fallback.",
 ("Subaru","Uncharted"): "No carsized entry found; use Commons fallback (same body as Toyota C-HR+, also absent).",
 ("Subaru","E-Outback"): "No carsized entry found (nor Trailseeker); use Commons fallback.",
 ("Suzuki","Across"): "carsized has only the first-generation Across (suzuki-across-2020-suv, 2020-present); no entry for the RAV4-XA60-based second generation; use Commons fallback or the Toyota RAV4 2025 entry.",
 ("Suzuki","e Vitara"): "No carsized entry found for the e Vitara; use Commons fallback (Toyota twin toyota-urban-cruiser-2025-suv-bev exists).",
 ("Mazda","Mazda2 Hybrid"): "No carsized entry found for the Mazda2 Hybrid (searches return the Mazda 2 2014); use Commons fallback or the Toyota Yaris 2020 entry.",
 ("Mazda","CX-5"): "carsized has the previous generation only (mazda-cx-5-2017-suv, 2017-2021); new KJ generation not found; use Commons fallback.",
}
for mm in MODELS:
    k = (mm["brand"], mm["model"])
    if k in CARSIZED:
        mm["carsized_slug"], mm["carsized_years"] = CARSIZED[k]
        if k in CARSIZED_NOTES:
            mm["notes"] = (mm["notes"] + " " if mm["notes"] else "") + CARSIZED_NOTES[k]
    elif k in NO_CARSIZED:
        mm["carsized_slug"] = mm["carsized_side"] = mm["carsized_front"] = mm["carsized_years"] = None
        mm["notes"] = (mm["notes"] + " " if mm["notes"] else "") + NO_CARSIZED[k]
    else:
        mm["notes"] = (mm["notes"] + " " if mm["notes"] else "") + "carsized slug not yet searched (search budget exhausted); null for now."

# image URLs copied from fetched carsized pages (side = compare page, front = /front/ page)
CARSIZED_IMAGES = {
 ("Lexus","RZ"): ("https://www.carsized.com/resources/lexus/rz/d/2023/sm_272127132_lexus-rz-2023-side-view_4x.png", None),
 ("Toyota","Proace"): ("https://www.carsized.com/resources/toyota/proace/verso-l2/2016/sm_321119173_toyota-proace-2016-side-view_4x.png", None),
 ("Suzuki","Swift"): ("https://www.carsized.com/resources/suzuki/swift/d/2023/sl_252110085_suzuki-swift-2023-side-view_4x.png", None),
 ("Mazda","Mazda3"): ("https://www.carsized.com/resources/mazda/3/d/2019/sl_242121106_mazda-3-2019-side-view_4x.png", None),
 ("Toyota","GR Supra"): ("https://www.carsized.com/resources/toyota/supra/d/2019/sl_223115135_toyota-supra-2019-side-view_4x.png", None),
 ("Subaru","Solterra"): ("https://www.carsized.com/resources/subaru/solterra/d/2022/sl_273124131_subaru-solterra-2022-side-view_4x.png", None),
}
for mm in MODELS:
    k = (mm["brand"], mm["model"])
    if k in CARSIZED_IMAGES:
        mm["carsized_side"], mm["carsized_front"] = CARSIZED_IMAGES[k]

SOURCES += [
 {"url": "https://www.subaru.ch/de/modelle/uncharted", "what": "Subaru CH Uncharted page: 'Jetzt kaufen', CHF 36'490-46'990, 58/77 kWh (fetched 2026-10-22)"},
 {"url": "https://www.subaru.de/e-outback", "what": "Subaru DE E-OUTBACK page: from EUR 51'990, MY26, configurator"},
 {"url": "https://www.lexus.de/new-cars/es/overview", "what": "Lexus DE: eighth-generation ES from EUR 59'600, ES 300h / ES 350e, 5140 mm"},
 {"url": "https://de.toyota.ch/neuwagen-kaufen/aygo-x", "what": "Toyota CH Aygo X page: 1.5 hybrid only, CHF 19'900"},
 {"url": "https://www.suzuki.ch/de/modelle/across", "what": "Suzuki CH 'NEW ACROSS': 2.5 PHEV 309 PS, 22.7 kWh, 129 km EV, CHF 56'490"},
 {"url": "https://cars.suzuki.co.uk/", "what": "Suzuki UK: new = e Vitara, Swift, S-Cross, Vitara; Ignis/Jimny/Swace/Across/Swift Sport used only"},
 {"url": "https://www.mazda.co.uk/cars/mazda2/", "what": "Mazda UK Mazda2 page still live (no price), Oct 2026"},
 {"url": "https://www.honda.co.uk/cars/new/super-n/overview.html", "what": "Honda UK Super-N: GBP 18'995, available at GB retailers, 3.6 m"},
 {"url": "https://newsroom.toyota.eu/", "what": "Toyota Europe newsroom front page 21 Oct 2026 (no Supra/GR GT items on page 1)"},
 {"url": "https://en.wikipedia.org/wiki/Toyota_bZ4X", "what": "bZ4X 4690 mm, e-TNGA co-developed with Subaru; bZ4X Touring 4830 mm, Europe 2026; Trailseeker/E-Outback"},
 {"url": "https://en.wikipedia.org/wiki/Toyota_GR_GT", "what": "GR GT: premiere 5 Dec 2025, production 2027, 4820 mm, 4.0 V8 TT hybrid 650 PS"},
 {"url": "https://en.wikipedia.org/wiki/Toyota_GR_Supra", "what": "Supra/Z4 joint platform, Magna Steyr; A90 Final Edition 300 units; production ended March 2026"},
 {"url": "https://en.wikipedia.org/wiki/Toyota_Urban_Cruiser", "what": "Points to article 'Toyota Urban Cruiser (BEV)', rebadged Suzuki e Vitara"},
 {"url": "https://en.wikipedia.org/wiki/Suzuki_e_Vitara", "what": "e Vitara 4275 mm / Urban Cruiser 4285 mm, Heartect-e, Gujarat-built; Europe Sept 2025 / Dec 2025"},
 {"url": "https://en.wikipedia.org/wiki/Subaru_Uncharted", "what": "Uncharted = rebadged C-HR+, e-TNGA, Europe Oct 2025"},
 {"url": "https://en.wikipedia.org/wiki/Subaru_Trailseeker", "what": "Trailseeker = Subaru version of bZ4X Touring, sold as E-Outback in Europe"},
 {"url": "https://en.wikipedia.org/wiki/Lexus_LBX", "what": "LBX on GA-B shared with Yaris Cross; 4190 mm, 2580 mm wheelbase"},
 {"url": "https://en.wikipedia.org/wiki/Lexus_ES", "what": "Eighth-gen ES codes, reveal 23 Apr 2025, powertrains"},
 {"url": "https://en.wikipedia.org/wiki/Mazda_EZ-6", "what": "Mazda 6e = EZ-6, same Changan EPA platform as Deepal L07; Europe mid-2025; Commons Category:Mazda6e"},
 {"url": "https://en.wikipedia.org/wiki/Mazda_EZ-60", "what": "CX-6e = EZ-60, heavily based on Deepal S07; Brussels Jan 2026; Commons Category:Mazda CX-6e"},
 {"url": "https://en.wikipedia.org/wiki/Deepal", "what": "Deepal serves UK, Spain, Portugal (models not tied to markets)"},
 {"url": "https://en.wikipedia.org/wiki/Honda_Super-N", "what": "Redirects to Honda N-One: Super-N = RHD-market name of the Super-One, 3580 mm; Commons Category:Honda N-One"},
 {"url": "https://en.wikipedia.org/wiki/Honda_Prelude", "what": "Sixth-gen Prelude powertrain; Commons Category:Honda Prelude"},
 {"url": "https://en.wikipedia.org/wiki/Mazda_CX-5", "what": "Third-gen CX-5: 2.5 Skyactiv-G with 24V M Hybrid in Europe; launches early 2026 (JP/NA/AU)"},
 {"url": "https://www.carsized.com/en/cars/lexus-rz-2023-suv/", "what": "carsized slugs confirmed via domain-filtered searches (see carsized_slug fields); RZ side view fetched"},
]


# ================================================================================================
# FINAL STATUS CLOSURE (2026-10-22, last web batch)
# ================================================================================================
UPDATES2 = {
 ("Mazda","Mazda2"): dict(status="runout",
    status_note="Fleet World (2026): Mazda has ended the petrol Mazda2 in the UK and Europe - production for Europe has stopped, it can no longer be ordered new and dealers are selling remaining stock (runout); the Mazda2 Hybrid becomes Mazda's only B-segment car. mazda.co.uk still shows a Mazda2 page without price (Oct 2026).",
    status_sources=["https://fleetworld.co.uk/?p=119668", "https://auto.everyeye.it/notizie/mazda-cancella-mazda2-europa-rimane-hybrid-realizzata-assieme-toyota-779544.html", "https://www.mazda.co.uk/cars/mazda2/", "https://www.carscoops.com/2025/03/four-mazda-models-are-being-discontinued-this-year-but-one-could-return/"],
    notes="Runout confirmed (Fleet World): included only because dealer stock is still being sold; verifier may move it to discontinued. carsized entry is 2014-2019 (pre-facelift DJ); no later entry found."),
 ("Mazda","Mazda2 Hybrid"): dict(status_note="Listed in the model keywords of mazda.ch and mazda.de (Oct 2026); 2026 model-year update for Europe reported April 2026 (Automotive World / Carscoops: 'Mazda updates 2026 Mazda2 Hybrid for European market'). Toyota Yaris-based hybrid built in Valenciennes.",
    status_sources=[MAZDA_CH, MAZDA_DE, "https://www.automotiveworld.com/news/mazda-updates-2026-mazda2-hybrid-for-european-market/", "https://fleetworld.co.uk/?p=119668"]),
 ("Suzuki","Across"): dict(status_note="Second generation (rebadged sixth-generation RAV4 PHEV): suzuki.ch 'NEW SUZUKI ACROSS' page, Compact Top 2.5 Plug-in Hybrid E-CVT 4x4 from CHF 56'490, 309 PS, 22.7 kWh, up to 129 km electric range; German trade press reports the RAV4 twin 'startet ab 55.490 Euro' (vision-mobility.de) and 'Kooperation in zweiter Generation' (autohaus.de). In the UK the Across is used-only (cars.suzuki.co.uk).",
    status_sources=["https://www.suzuki.ch/de/modelle/across", "https://vision-mobility.de/news/suzuki-across-der-rav4-zwilling-startet-ab-55-490-euro-393980.html", "https://www.autohaus.de/nachrichten/autohersteller/suzuki-across-kooperation-in-zweiter-generation-3767166", "https://cars.suzuki.co.uk/"],
    twin_sources=["https://www.autohaus.de/nachrichten/autohersteller/suzuki-across-kooperation-in-zweiter-generation-3767166", "https://www.cars24.com.au/car-news/suzuki-across-revealed-as-rebadged-new-gen-toyota-rav4/", SUZUKI_CH]),
 ("Toyota","RAV4"): dict(status_note="Sixth generation: toyota.ch 'Der neue Toyota RAV4' with full hybrid and plug-in hybrid (FWD/AWD), from CHF 43'900 for the Trend 2.5 Hybrid, 4600-4646 mm, some figures 'Homologation ausstehend' (Oct 2026); UK orders opened early May 2026, deliveries from June 2026 (Toyota UK press release 7 Apr 2026, PHEV from GBP 43'845); toyota.de list.",
    status_sources=["https://de.toyota.ch/neuwagen-kaufen/rav4", "https://media.toyota.co.uk/?p=66870", TOYOTA_DE],
    notes="UK launch range is PHEV-only; Switzerland offers full hybrid and PHEV. Length 4600 mm (up to 4646 mm for the Adventure/GR Sport variants)."),
 ("Toyota","GR Supra"): dict(status_sources=[TOYOTA_DE, "https://en.wikipedia.org/wiki/Toyota_GR_Supra", "https://torquecafe.com/toyota-axes-supra-for-now", TOYOTA_CH]),
 ("Mazda","CX-5"): dict(status_note="Third generation debuted in Europe 10 July 2025 (Mazda newsroom release 250710a 'All-New Mazda CX-5 debuts in Europe'); listed on mazda.ch and mazda.de (Oct 2026) with the 2.5 e-Skyactiv G 24V mild hybrid; European order status for the new car could not be read from the JavaScript-only Mazda sites.",
    status_sources=["https://newsroom.mazda.com/en/publicity/release/2025/202507/250710a.html", MAZDA_CH, MAZDA_DE, "https://en.wikipedia.org/wiki/Mazda_CX-5"]),
 ("Honda","Super-N"): dict(notes="Wikipedia covers it in the Honda N-One article: the Super-N is the right-hand-drive-market name of the Super-One (widebody N-One e:, 3580 mm, 70 kW motor; Japan sales from 21 May 2026). UK launch reported by electrive 16 Apr 2026; auto motor und sport headline 'Elektro-Kei-Car mit Europastart'. Not on honda.ch/.de in Oct 2026, so continental launch unconfirmed. Commons: parent category 'Category:Honda N-One'. carsized not searched (image work stopped per coordinator)."),
}
for mm in MODELS:
    u = UPDATES2.get((mm["brand"], mm["model"]))
    if u: mm.update(u)
    if (mm["brand"], mm["model"]) == ("Mazda","Mazda 6e"):
        mm["twin_tier"] = None   # no European twin member confirmed (Deepal L07 not sold in Europe)

ANNOUNCED += [
m(**H, model="0 SUV", display="0 SUV", ch_on_sale=False, ch_source=HONDA_CH, row="d-suv",
  body="5-door electric SUV", generation="I (US launch 2026; Europe announced)", length_mm=None,
  platform="Honda 0 Series dedicated BEV architecture", powertrains=["BEV"],
  status="announced",
  status_note="Honda said at CES 2025 that the 0 SUV and 0 Saloon will launch in 2026 'including Europe' (motor1/InsideEVs, Jan 2025); American Honda (InsideEVs, 14 Jan 2026) puts the 0 SUV 'later in 2026' in the US. No European order date or price; only a concept link on honda.ch (Oct 2026).",
  status_sources=["https://www.motor1.com/news/746526/honda-0-suv-saloon-ces-2025/", "https://insideevs.com/news/784312/honda-0-series-saloon-delay/", HONDA_CH],
  wikipedia_en="Honda 0 Series", commons_category="Category:Honda 0 Series",
  notes="Row provisional (mid-size SUV); length unknown. Low confidence that European orders open before 2027 - verifier to decide whether to show it as 'coming'.", carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None),
m(**H, model="0 Saloon", display="0 Saloon", ch_on_sale=False, ch_source=HONDA_CH, row="e-car",
  body="4-door electric fastback saloon", generation="I (delayed to 2027)", length_mm=None,
  platform="Honda 0 Series dedicated BEV architecture", powertrains=["BEV"],
  status="announced",
  status_note="Europe was named as a launch region at CES 2025 (motor1), but American Honda said in Jan 2026 the 0 Saloon is 'pushed into 2027' (InsideEVs). No European order date or price.",
  status_sources=["https://www.motor1.com/news/746526/honda-0-suv-saloon-ces-2025/", "https://insideevs.com/news/784312/honda-0-series-saloon-delay/", HONDA_CH],
  wikipedia_en="Honda 0 Series", commons_category="Category:Honda 0 Series",
  notes="Row provisional; length unknown (approx. 5 m). Low confidence for a 2026/27 European launch.", carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None),
]

for d in DISCONTINUED:
    if d["brand"]=="Lexus" and d["model"]=="LS":
        d["note"] = "Withdrawn from the UK in Jan 2025 after 3 sales in 2024 (Carscoops/motor1); listed under 'Previous Models' on lexus.co.uk and absent from lexus.ch/.de in Oct 2026."
        d["source"] = "https://www.carscoops.com/2025/01/lexus-ls-axed-from-uk-market-after-selling-just-3-units-in-2024/"

SOURCES += [
 {"url": "https://fleetworld.co.uk/?p=119668", "what": "Fleet World (2026): petrol Mazda2 axed in UK/Europe, production stopped, runout stock; Mazda2 Hybrid remains"},
 {"url": "https://www.automotiveworld.com/news/mazda-updates-2026-mazda2-hybrid-for-european-market/", "what": "2026 Mazda2 Hybrid update for Europe (search result, Apr 2026)"},
 {"url": "https://vision-mobility.de/news/suzuki-across-der-rav4-zwilling-startet-ab-55-490-euro-393980.html", "what": "New Suzuki Across from EUR 55'490 in Germany (search result title; page not fetched)"},
 {"url": "https://www.autohaus.de/nachrichten/autohersteller/suzuki-across-kooperation-in-zweiter-generation-3767166", "what": "Autohaus: Across second generation = RAV4 cooperation (search result)"},
 {"url": "https://de.toyota.ch/neuwagen-kaufen/rav4", "what": "Toyota CH new RAV4: full hybrid + PHEV, CHF 43'900, 4600-4646 mm"},
 {"url": "https://www.motor1.com/news/746526/honda-0-suv-saloon-ces-2025/", "what": "Honda 0 SUV / 0 Saloon to launch 2026 incl. Europe (CES 2025)"},
 {"url": "https://insideevs.com/news/784312/honda-0-series-saloon-delay/", "what": "Honda 0 Saloon delayed to 2027; 0 SUV later in 2026 (US), 14 Jan 2026"},
 {"url": "https://www.carscoops.com/2025/01/lexus-ls-axed-from-uk-market-after-selling-just-3-units-in-2024/", "what": "Lexus LS axed from UK market, Jan 2025"},
 {"url": "https://newsroom.mazda.com/en/publicity/release/2025/202507/250710a.html", "what": "All-new Mazda CX-5 debuts in Europe, 10 Jul 2025 (search result)"},
 {"url": "https://torquecafe.com/toyota-axes-supra-for-now", "what": "'Toyota axes Supra for now' (search result, 2026)"},
 {"url": "https://www.auto-motor-und-sport.de/elektroauto/honda-super-n-elektro-kei-car-mit-europastart/", "what": "AMS: Honda Super-N 'mit Europastart' (search result)"},
]

def main():
    data = {"agent": "japan (Toyota Motor, Subaru, Suzuki, Mazda, Honda)", "checked_on": "2026-10-21",
            "models": MODELS, "announced": ANNOUNCED, "discontinued_recently": DISCONTINUED, "sources": SOURCES}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"wrote {OUT}: {len(MODELS)} models, {len(ANNOUNCED)} announced, {len(DISCONTINUED)} discontinued")

if __name__ == "__main__":
    main()
