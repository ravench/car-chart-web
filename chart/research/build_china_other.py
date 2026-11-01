#!/usr/bin/env python3
"""Generates china-other.json (research data for the Chinese makers other than Geely/Leapmotor).
Edit the MODELS / ANNOUNCED / DISCONTINUED lists, then run:  python3 -I build_china_other.py
"""
import json, os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "china-other.json")

# --- shared source URLs -------------------------------------------------------
MG_CH = "https://www.mgmotor.ch/de"
MG_EU = "https://www.mgmotor.eu/"
MG_INSIDEEVS_DROP = "https://insideevs.de/news/758153/mg-5-zs-marvel-ausgelaufen/"
MG4U_ELECTRIVE = "https://www.electrive.net/2026/02/13/neuer-mg4-ev-urban-startet-in-oesterreich-bei-unter-20-000-euro/"
MG4U_ECOMENTO = "https://ecomento.de/2026/01/30/neuer-mg4-in-europa-zunaechst-nur-in-grossbritannien/"
MGS6_INSIDEEVS = "https://insideevs.de/news/786425/mgs6-ev-2026-daten-preise/"
MGS9_AMS = "https://www.auto-motor-und-sport.de/neuheiten/mg-qs9-phev-bei-euroncap-crashtest-enthuellt-neuen-fuenfmeter-suv-aus-china/"
IM_ELECTRIVE = "https://www.electrive.com/2026/06/01/mg-brings-electric-premium-models-im5-and-im6-to-germany/"
CARIFY_CH = "https://www.carify.com/en/blog/chinesische-elektroautos-in-der-schweiz"
MAXUS_UK = "https://www.saicmaxus.co.uk/"
MAXUS_CARWOW_DE = "https://www.carwow.de/maxus"
BYD_UK = "https://www.byd.com/uk"
BYD_DE_OVERVIEW = "https://elektronik-zeit.de/byd-e-autos-2026/byd-modelle/"
BYD_CH_MONEYCAB = "https://www.moneycab.com/mobilitaet/byd-startet-mit-kleinwagen-in-der-schweiz/"
DENZA_DE = "https://www.denza.com/de"
DENZA_CHINAEVHOME = "https://chinaevhome.com/2026/04/09/denza-z9gt-hits-7-european-markets-at-101k-eur/"
DENZA_AUTOEVO_UK = "https://www.autoevolution.com/news/denza-z9-gt-executive-shooting-brake-lands-in-the-united-kingdom-with-arid-prices-for-phev-and-ev-273367.html"
OJ_CH = "https://www.omodajaecoo.ch/"
OMODA_UK = "https://www.omodaauto.co.uk/"
JAECOO_UK = "https://www.jaecoo.co.uk/"
OJ_CARGURUS = "https://www.cargurus.co.uk/research/articles/best-jaecoo-and-omoda-cars-and-suvs"
CHERY_CARWOW_UK = "https://www.carwow.co.uk/chery"
CHERY_ELECTRIVE_DE = "https://www.electrive.com/2026/08/chery-makes-its-german-market-debut-with-four-hybrids/"
CHERY_HYE = "https://www.hibridosyelectricos.com/coches/grupo-chery-anuncia-como-sera-su-2026-mas-puntos-ventas-nuevos-modelos-electrificados-mas-marcas-chinas_83716_102.html"
LEPAS_AUTOIT = "https://www.auto.it/news/anteprime/2026/08/27-9056932/lepas_debutta_l8_pronti_altri_tre_modelli/3"
LEPAS_FLEET = "https://www.fleetmagazine.com/nuovi-brand-auto-cinesi-in-italia-chery-lepas-icaur-ed-exlantix/"
GWM_GOLEASY = "https://www.goleasy.de/leasing/marken/gwm"
GWM_AUTOHAUS = "https://www.autohaus.de/nachrichten/autohersteller/offensive-im-suv-volumensegment-gwm-bringt-haval-nach-deutschland-3785068"
GWM_AUTONOTIZEN = "https://autonotizen.de/neuigkeiten/gwm-haval-ora-wey-2026"
GWM_CARWOW_UK = "https://www.carwow.co.uk/gwm/poer300-lcv"
XPENG_DE = "https://www.xpeng.com/de"
XPENG_GOINGELECTRIC = "https://www.goingelectric.de/elektroautos/xpeng/"
XPENG_FLEETWORLD = "https://fleetworld.co.uk/xpeng-accelerates-2026-product-roadmap-for-uk/"
NIO_DE = "https://www.nio.com/de_DE"
NIO_EV_STATUS = "https://eletric-vehicles.com/nio/nio-running-out-of-vehicles-to-sell-in-its-direct-eu-markets/"
FIREFLY_ELECTRIVE = "https://www.electrive.com/2025/08/15/first-firefly-evs-delivered-in-europe"
FIREFLY_CNC = "https://carnewschina.com/2025/12/10/nios-firefly-enters-greece-denmark-austria-and-portugal-as-it-pushes-its-overseas-strategy/"
ONVO_DELAY = "https://eletric-vehicles.com/nio/onvo/nio-delays-onvo-europe-launch-to-2028-2029/"
CHANGAN_ELECTRIVE_DEC = "https://www.electrive.com/2025/12/17/changan-expands-into-italy-spain-and-denmark"
CHANGAN_ELECTRIVE_AVATR = "https://www.electrive.com/2025/12/05/changan-to-bring-avatr-and-nevo-to-europe-by-2027"
VOYAH_GASGOO_COURAGE = "https://autonews.gasgoo.com/articles/market-industry/voyah-launches-courage-suv-model-in-norway-sweden-finland-70034976"
VOYAH_GASGOO_EU = "https://autonews.gasgoo.com/articles/market-industry/dongfeng-motors-voyah-expands-market-presence-in-more-european-countries-70023756"
HONGQI_NO = "https://www.hongqi.no/"
HONGQI_NO_BILER = "https://hongqi.no/biler"
HONGQI_EHS5_SPEC = "https://hongqi.no/biler/ehs5/spesifikasjoner/"
DENZA_DE_BAO5 = "https://www.denza.com/de/modelle/bao-5"
DENZA_DE_D9 = "https://www.denza.com/de/d9"
XPENG_DE_L03 = "https://www.xpeng.com/de/model/L03"
XPENG_DE_G9L = "https://www.xpeng.com/de/model/G9L"
VOYAH_NO = "https://voyah.no/"
BYD_UK_TI7 = "https://www.byd.com/uk/hybrid-cars/ti-7"
BYD_UK_DOLPHIN_G = "https://www.byd.com/uk/hybrid-cars/dolphin-g-dm-i"
BYD_UK_SEALION5 = "https://www.byd.com/uk/hybrid-cars/sealion-5-dm-i"
BYD_UK_SHARK = "https://www.byd.com/uk/hybrid-cars/shark"
WIKI_JAECOO7 = "https://en.wikipedia.org/wiki/Jaecoo_7"
WIKI_TIGGO9 = "https://en.wikipedia.org/wiki/Chery_Tiggo_9"
WIKI_EZ60 = "https://en.wikipedia.org/wiki/Mazda_EZ-60"
FIREFLY_EVPOWERED = "https://evpowered.co.uk/news/nio-firefly-rhd-squares-up-to-renault-5-ahead-of-uk-2026-debut/"
WIKI_TAI7 = "https://en.wikipedia.org/wiki/Fangchengbao_Tai_7"
WIKI_OMODA7 = "https://en.wikipedia.org/wiki/Omoda_7"
WIKI_OMODA5 = "https://en.wikipedia.org/wiki/Chery_Omoda_5"
WIKI_TIGGO7 = "https://en.wikipedia.org/wiki/Chery_Tiggo_7"
WIKI_TIGGO8 = "https://en.wikipedia.org/wiki/Chery_Tiggo_8"
WIKI_JAECOO5 = "https://en.wikipedia.org/wiki/Jaecoo_5"
VOYAH_NL = "https://www.voyah.nl/"
VOYAH_NL_BOX = "https://voyah.nl/dongfeng-box?hsLang=nl"
VOYAH_NL_MHERO = "https://voyah.nl/mhero?hsLang=nl"
LEPAS_UK_DEALER = "https://www.lepas.co.uk/"
HONGQI_GASGOO = "https://autonews.gasgoo.com/articles/news/faws-hongqi-brand-to-foray-into-norwegian-market-70033334"
HONGQI_FLEETWORLD = "https://fleetworld.co.uk/hongqi-reveals-prices-for-luxury-evs-in-europe-ahead-of-uk-arrival/"
XIAOMI_MOTOR1 = "https://fr.motor1.com/news/769666/xiaomi-voitures-electriques-lancement-europe-2027/"

NOT_FETCHED = "carsized entry not fetched/verified (web-fetch budget exhausted in this session)"

def m(brand, group, model, display, row, body, generation, length_mm, platform, powertrains,
      status, status_note, status_sources, *, other_names=(), ch_on_sale=None, ch_source=None,
      twin_tier=None, twin_members=(), twin_note="", twin_sources=(),
      carsized_slug=None, carsized_side=None, carsized_front=None, carsized_years=None,
      commons_category=None, commons_file=None, wikipedia_en=None, notes=""):
    return {
        "brand": brand, "group": group, "model": model, "display": display,
        "other_names": list(other_names), "ch_on_sale": ch_on_sale, "ch_source": ch_source,
        "row": row, "body": body, "generation": generation, "length_mm": length_mm,
        "platform": platform, "powertrains": list(powertrains),
        "status": status, "status_note": status_note, "status_sources": list(status_sources),
        "twin_tier": twin_tier, "twin_members": list(twin_members), "twin_note": twin_note,
        "twin_sources": list(twin_sources),
        "carsized_slug": carsized_slug, "carsized_side": carsized_side,
        "carsized_front": carsized_front, "carsized_years": carsized_years,
        "commons_category": commons_category, "commons_file": commons_file,
        "wikipedia_en": wikipedia_en, "notes": notes,
    }

# carsized results: key -> dict(slug, side, front, years)  (filled in as fetches succeed)
CARSIZED = {}
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "carsized_china_other.json")) as f:
        CARSIZED = json.load(f)
except FileNotFoundError:
    pass

SAIC = "SAIC Motor"
MODELS = []
A = MODELS.append

# =============================== MG ==========================================
A(m("MG", SAIC, "MG3", "MG3", "b-hatch", "5-door hatchback", "II (2024–)", 4113, "SAIC SIGMA",
    ["petrol", "HEV"], "on_sale", "MG3 and MG3 Hybrid+ listed on the Swiss and EU model pages (Oct 2026)",
    [MG_CH, MG_EU], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG3 (2024)", wikipedia_en="MG3",
    notes="Sold as MG3 (1.5 petrol) and MG3 Hybrid+. Shares the SIGMA platform with the ZS (different row, no group). Commons category name is a best guess, not verified."))

A(m("MG", SAIC, "MG4", "MG4", "c-hatch", "5-door hatchback", "I (2022–), updated 2026 MY", 4287, "SAIC MSP (Modular Scalable Platform)",
    ["BEV"], "on_sale", "Original RWD MG4 EV continues alongside the new MG4 Urban: Luxury 64 kWh, Trophy Extended Range 77 kWh and XPower remain (Austria price list Feb 2026; Germany from EUR 34,990 Jan 2026); still listed on mgmotor.ch and mgmotor.eu (Oct 2026)",
    [MG_CH, MG_EU, MG4U_ELECTRIVE, MG4U_ECOMENTO], other_names=["MG4 EV", "MG4 Electric (DE)"],
    ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG4 EV", wikipedia_en="MG4 EV",
    notes="Two different MG4 generations are sold side by side in Europe since 2026 (see separate 'MG4 Urban' tile). XPower is a trim of this tile."))

A(m("MG", SAIC, "MG4 Urban", "MG4 Urban", "c-hatch", "5-door hatchback", "II (China 2025–; Europe 2026–)", 4395, "new SAIC FWD platform (cell-to-body, solid-state ready)",
    ["BEV"], "on_sale", "Second-generation MG4 sold in Europe as 'MG4 EV Urban': UK orders from Jan 2026 (GBP 23,495), Austria orderable Feb 2026 (deliveries from Apr 2026); listed as NEW on mgmotor.ch and mgmotor.eu (Oct 2026)",
    [MG4U_ELECTRIVE, MG4U_ECOMENTO, MG_CH, MG_EU], other_names=["MG4 EV Urban", "MG4 (China)"],
    ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG4 (2025)", wikipedia_en="MG4 EV",
    notes="FWD, 43/54 kWh LFP, ~11 cm longer than the 2022 MG4; replaces the small-battery versions of the old car. Judgement call: treated as a separate tile because both generations are on sale at once under different names. Commons category name unverified."))

A(m("MG", SAIC, "MGS5 EV", "MGS5 EV", "c-suv", "SUV", "I (2025–)", 4476, "SAIC MSP",
    ["BEV"], "on_sale", "Successor of the ZS EV; UK from spring 2025, Germany from Sept 2025; listed on mgmotor.ch and mgmotor.eu (Oct 2026)",
    [MG_CH, MG_EU, MG_INSIDEEVS_DROP], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG S5 EV", wikipedia_en="MG S5 EV",
    notes="RWD, 49/64 kWh. Commons category unverified."))

A(m("MG", SAIC, "ZS", "ZS", "b-suv", "SUV", "II (2024–)", 4430, "SAIC SIGMA",
    ["petrol", "HEV"], "on_sale", "ZS (petrol) and ZS Hybrid+ listed on mgmotor.ch and mgmotor.eu (Oct 2026); the ZS EV was dropped in 2025 (replaced by MGS5 EV)",
    [MG_CH, MG_EU, MG_INSIDEEVS_DROP], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG ZS (2024)", wikipedia_en="MG ZS",
    notes="4.43 m is long for the B-SUV row; kept in b-suv per MG's own small-SUV positioning (Captur/2008 rivals). Commons category unverified."))

A(m("MG", SAIC, "HS", "HS", "c-suv", "SUV", "II (2024–)", 4655, "SAIC SIGMA",
    ["petrol", "HEV", "PHEV"], "on_sale", "HS, HS Hybrid+ and HS PHEV listed on mgmotor.ch and mgmotor.eu (Oct 2026)",
    [MG_CH, MG_EU], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG HS (2024)", wikipedia_en="MG HS",
    notes="4.66 m sits at the c-suv/d-suv boundary; MG positions it against Qashqai/Sportage, so c-suv. Commons category unverified."))

A(m("MG", SAIC, "MGS6 EV", "MGS6 EV", "d-suv", "SUV (fastback)", "I (2026–)", 4708, "SAIC MSP",
    ["BEV"], "on_sale", "Orderable in the UK since Nov 2025, Austria Feb 2026 (EUR 34,990), Germany from 16 Mar 2026 (EUR 49,990); listed as NEW on mgmotor.ch (Oct 2026)",
    [MGS6_INSIDEEVS, MG_CH, MG_EU], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG S6 EV", wikipedia_en="MG S6 EV",
    notes="4,708 mm / 2,836 mm wheelbase, 74.3 kWh, RWD 180 kW or AWD 266 kW. MG calls it compact, press calls it mid-size; placed in d-suv by length (Enyaq-size). Commons category unverified."))

A(m("MG", SAIC, "MGS9 PHEV", "MGS9 PHEV", "e-suv", "SUV, 7 seats", "I (Europe 2026–)", 4983, "SAIC (Roewe RX9 / MG QS)",
    ["PHEV"], "on_sale", "Listed as NEW ('MGS9 Plug-in Hybrid') on mgmotor.ch and mgmotor.eu (Oct 2026); UK dealers announce arrival 2026",
    [MG_CH, MG_EU, MGS9_AMS, "https://www.invictamotors.co.uk/mg/news/mgs9-phev-arrives"], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:Roewe RX9", wikipedia_en="Roewe RX9",
    notes="European version of the Roewe RX9 (sold as MG QS in Australia); 4,983 mm, seven seats, HS-derived 1.5T PHEV. Exact European order date/price not verified (fetch budget). Commons: no MG-specific category known; parent Roewe RX9 given."))

A(m("MG", SAIC, "Cyberster", "Cyberster", "sports", "2-door roadster", "I (2024–)", 4535, "SAIC MSP",
    ["BEV"], "on_sale", "Listed on mgmotor.ch and mgmotor.eu (Oct 2026); Swiss price from CHF 63,990 (carify, Apr 2026)",
    [MG_CH, MG_EU, CARIFY_CH], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:MG Cyberster", wikipedia_en="MG Cyberster",
    notes=""))

A(m("MG", SAIC, "IM5", "IM5", "d-car", "4-door saloon (fastback)", "I (Europe 2025–)", 4931, "IM Motors 800 V platform",
    ["BEV"], "on_sale", "Sold as 'MG IM5' through MG dealers: UK, Norway and Switzerland since July 2025; Germany, France, Belgium, Netherlands from July 2026; listed on mgmotor.ch from CHF 41,990 (Oct 2026)",
    [IM_ELECTRIVE, MG_CH, MG_EU], other_names=["MG IM5"], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:IM L6", wikipedia_en="IM L6",
    notes="= IM L6 (Zhiji L6). Brief lists 'IM' as its own SAIC column; in Europe it is marketed as 'MG IM5' under the MG umbrella, so filed under MG here — move to an IM column if preferred. 4.93 m is on the d/e boundary; placed d-car because MG prices/positions it against Model 3 / BYD Seal."))

A(m("MG", SAIC, "IM6", "IM6", "d-suv", "SUV", "I (Europe 2025–)", 4904, "IM Motors 800 V platform",
    ["BEV"], "on_sale", "Sold as 'MG IM6' through MG dealers: UK, Norway and Switzerland since July 2025; Germany/France/Belgium/Netherlands from July 2026; listed on mgmotor.ch from CHF 49,990 (Oct 2026)",
    [IM_ELECTRIVE, MG_CH, MG_EU], other_names=["MG IM6"], ch_on_sale=True, ch_source=MG_CH,
    commons_category="Category:IM LS6", wikipedia_en="IM LS6",
    notes="= IM LS6. See IM5 note on the MG/IM column question."))

# =============================== Maxus =======================================
MAXUS_NOTE_CH = "Swiss importer page (maxus.ch) could not be fetched in this session; Swiss status unknown."
A(m("Maxus", SAIC, "eDeliver 3", "eDeliver 3", "van-small", "compact panel van (SWB/LWB)", "I (2020–)", 4555, "SAIC Maxus EV30",
    ["BEV"], "on_sale", "Listed in the UK range (saicmaxus.co.uk, Oct 2026) and on the German dealer listings (carwow.de)",
    [MAXUS_UK, MAXUS_CARWOW_DE], other_names=["LDV eDeliver 3 (AU/NZ)"],
    commons_category="Category:Maxus EV30", wikipedia_en="Maxus EV30",
    notes="4,555 mm (SWB) / 5,145 mm (LWB). " + MAXUS_NOTE_CH))

A(m("Maxus", SAIC, "eDeliver 5", "eDeliver 5", "van-small", "compact/medium panel van", "I (2024–)", 4800, "SAIC Maxus",
    ["BEV"], "on_sale", "Listed in the UK range (saicmaxus.co.uk, Oct 2026)",
    [MAXUS_UK],
    commons_category="Category:Maxus eDeliver 5", wikipedia_en="Maxus eDeliver 5",
    notes="4.8 m, 1-tonne-class FWD electric van sized between eDeliver 3 and 7 (Transit Connect L2 / Caddy Maxi length) - row is a judgement call (van-small). Commons category unverified. " + MAXUS_NOTE_CH))

A(m("Maxus", SAIC, "Deliver 7", "Deliver 7 / eDeliver 7", "van-mid", "mid-size panel van (L1/L2)", "I (2023–)", 4998, "SAIC Maxus",
    ["diesel", "BEV"], "on_sale", "eDeliver 7 (BEV) and Deliver 7 (2.0 diesel) listed in the UK range (saicmaxus.co.uk, Oct 2026); eDeliver 7 on German listings",
    [MAXUS_UK, MAXUS_CARWOW_DE], other_names=["eDeliver 7 (BEV)", "LDV Deliver 7 (AU)"],
    commons_category="Category:Maxus Deliver 7", wikipedia_en="Maxus eDeliver 7",
    notes="One tile for the diesel 'Deliver 7' and electric 'eDeliver 7' (same body, powertrain-variant naming). 4,998 mm (L1) / 5,366 mm (L2). " + MAXUS_NOTE_CH))

A(m("Maxus", SAIC, "Deliver 9", "Deliver 9 / eDeliver 9", "van-large", "large panel van / chassis cab", "I (2019–)", 5546, "SAIC Maxus V90",
    ["diesel", "BEV"], "on_sale", "eDeliver 9 and Deliver 9 listed in the UK range (saicmaxus.co.uk, Oct 2026) and on German listings",
    [MAXUS_UK, MAXUS_CARWOW_DE], other_names=["eDeliver 9 (BEV)", "LDV Deliver 9 (AU)"],
    commons_category="Category:Maxus V90", wikipedia_en="Maxus V90",
    notes="One tile for diesel 'Deliver 9' and electric 'eDeliver 9'. 5,546 mm (L2) / 5,940 mm (L3). " + MAXUS_NOTE_CH))

A(m("Maxus", SAIC, "eTerron 9", "eTerron 9", "pickup", "double-cab pickup", "I (2025–)", 5500, "SAIC Maxus (Interstellar X)",
    ["BEV"], "on_sale", "Listed in the UK range (saicmaxus.co.uk, Oct 2026); UK launch 2025",
    [MAXUS_UK], other_names=["LDV eTerron 9 (AU)", "Maxus Interstellar X (China)"],
    commons_category="Category:Maxus Interstellar X", wikipedia_en="Maxus Interstellar X",
    notes="Dual-motor electric pickup, 102 kWh. European markets beyond the UK not verified (fetch budget). Commons category unverified. " + MAXUS_NOTE_CH))

A(m("Maxus", SAIC, "T90 EV", "T90 EV", "pickup", "double-cab pickup", "I (Europe 2022–)", 5365, "SAIC Maxus T90",
    ["BEV"], "on_sale", "Still listed on German dealer listings (carwow.de, Oct 2026); not in the UK range any more (replaced there by eTerron 9)",
    [MAXUS_CARWOW_DE], other_names=["LDV eT60 (AU/NZ)"],
    twin_tier=1, twin_members=["Maxus T60 Max"], twin_note="Electric derivative of the T60 pickup (same cab/body).",
    twin_sources=["https://www.ultimatespecs.com/car-specs/Maxus-models"],
    commons_category="Category:Maxus T90", wikipedia_en="Maxus T90",
    notes="Status weak: only a dealer-listing source; could be runout in 2026. Verify. " + MAXUS_NOTE_CH))

A(m("Maxus", SAIC, "T60 Max", "T60 Max", "pickup", "double-cab pickup", "I (facelift 2024–)", 5365, "SAIC Maxus T60",
    ["diesel"], "on_sale", "Listed in the UK range (saicmaxus.co.uk, Oct 2026)",
    [MAXUS_UK], other_names=["LDV T60 Max (AU)", "Maxus T60 (other markets)"],
    commons_category="Category:Maxus T60", wikipedia_en="Maxus T60",
    notes="Diesel sister of the T90 EV (same cab/body) - treated as separate nameplates (two tiles), tier 1 twins of each other; verifier may merge. " + MAXUS_NOTE_CH,
    twin_tier=1, twin_members=["Maxus T90 EV"], twin_note="T60 and T90 share body and cab; T90 EV is the electric derivative",
    twin_sources=["https://www.ultimatespecs.com/car-specs/Maxus-models"]))

A(m("Maxus", SAIC, "Mifa 7", "Mifa 7", "mpv-large", "MPV, 7 seats", "I (2024–)", 4907, "SAIC Maxus",
    ["BEV"], "on_sale", "Listed in the UK range (saicmaxus.co.uk, Oct 2026)",
    [MAXUS_UK], other_names=["LDV Mifa 7 (AU)", "Maxus Dana 7 (China)"],
    commons_category="Category:Maxus Mifa 7", wikipedia_en="Maxus Mifa 7",
    notes="Commons category unverified. " + MAXUS_NOTE_CH))

A(m("Maxus", SAIC, "Mifa 9", "Mifa 9", "mpv-large", "MPV, 7 seats", "I (2022–)", 5270, "SAIC Maxus",
    ["BEV"], "on_sale", "Listed in the UK range (saicmaxus.co.uk) and German listings (carwow.de) (Oct 2026)",
    [MAXUS_UK, MAXUS_CARWOW_DE], other_names=["LDV Mifa 9 (AU)"],
    commons_category="Category:Maxus Mifa 9", wikipedia_en="Maxus Mifa 9",
    notes=MAXUS_NOTE_CH))

# =============================== BYD =========================================
BYDG = "BYD"
A(m("BYD", BYDG, "Dolphin Surf", "Dolphin Surf", "a-city", "5-door hatchback", "I (2025–)", 3780, "BYD e-Platform 3.0",
    ["BEV"], "on_sale", "Listed on byd.com/uk (Oct 2026) and German price list (EUR 22,990, Sept 2026); Switzerland from CHF 20,990 (May 2025)",
    [BYD_UK, BYD_DE_OVERVIEW, BYD_CH_MONEYCAB], other_names=["BYD Seagull / Dolphin Mini (other markets)"],
    ch_on_sale=True, ch_source=BYD_CH_MONEYCAB,
    commons_category="Category:BYD Seagull", wikipedia_en="BYD Seagull",
    notes="European version of the Seagull."))

A(m("BYD", BYDG, "Dolphin", "Dolphin", "b-hatch", "5-door hatchback", "I (2021–; Europe 2023–)", 4290, "BYD e-Platform 3.0",
    ["BEV"], "on_sale", "Listed on byd.com/uk (Oct 2026) and German price list (EUR 33,990, Sept 2026)",
    [BYD_UK, BYD_DE_OVERVIEW], ch_on_sale=None, ch_source=None,
    commons_category="Category:BYD Dolphin", wikipedia_en="BYD Dolphin",
    notes="Swiss status not verified (bydauto.ch blocks fetches)."))

A(m("BYD", BYDG, "Dolphin G", "Dolphin G DM-i", "b-hatch", "5-door hatchback / crossover", "I (2026–)", 4000, "BYD DM-i",
    ["PHEV"], "on_sale", "UK: 'The Long-Range Plug-in Hybrid Hatchback' - finance offer applies to orders placed 7 Oct-31 Dec 2026, so UK orders are open (byd.com/uk model page, Oct 2026); German press (Sept 2026) still lists it as coming, price pending, possibly built in Hungary",
    [BYD_UK_DOLPHIN_G, BYD_UK, BYD_DE_OVERVIEW],
    commons_category=None, commons_file=None, wikipedia_en=None,
    notes="Length approx. (~4.0 m per German press; UK page gives no dimensions) - verify. No Commons category known yet."))

A(m("BYD", BYDG, "Atto 2", "Atto 2", "b-suv", "SUV", "I (2025–)", 4310, "BYD e-Platform 3.0 Evo / DM-i",
    ["BEV", "PHEV"], "on_sale", "Atto 2 (BEV) and Atto 2 DM-i (PHEV) listed on byd.com/uk (Oct 2026) and German price list (EUR 31,990 / 35,990, Sept 2026); Switzerland from CHF 30,990 (May 2025)",
    [BYD_UK, BYD_DE_OVERVIEW, BYD_CH_MONEYCAB], other_names=["BYD Yuan Up (China)"],
    ch_on_sale=True, ch_source=BYD_CH_MONEYCAB,
    commons_category="Category:BYD Yuan Up", wikipedia_en="BYD Atto 2",
    notes="BEV and DM-i versions in one tile."))

A(m("BYD", BYDG, "Atto 3", "Atto 3", "c-suv", "SUV", "I (2022–), 'Atto 3 Evo' facelift 2026", 4455, "BYD e-Platform 3.0",
    ["BEV"], "on_sale", "'Atto 3 Evo' listed on byd.com/uk (Oct 2026); Germany EUR 44,990 (Sept 2026); Switzerland from CHF 39,900 (carify, Apr 2026)",
    [BYD_UK, BYD_DE_OVERVIEW, CARIFY_CH], other_names=["BYD Yuan Plus (China)"],
    ch_on_sale=True, ch_source=CARIFY_CH,
    commons_category="Category:BYD Yuan Plus", wikipedia_en="BYD Atto 3",
    notes=""))

A(m("BYD", BYDG, "Seal", "Seal", "d-car", "4-door saloon", "I (2022–; Europe 2023–)", 4800, "BYD e-Platform 3.0",
    ["BEV"], "on_sale", "Listed on byd.com/uk (Oct 2026); Germany EUR 47,990 (Sept 2026); Switzerland c. CHF 49,990 (carify, Apr 2026)",
    [BYD_UK, BYD_DE_OVERVIEW, CARIFY_CH], ch_on_sale=True, ch_source=CARIFY_CH,
    commons_category="Category:BYD Seal", wikipedia_en="BYD Seal",
    notes=""))

A(m("BYD", BYDG, "Seal 6", "Seal 6 DM-i", "d-car", "4-door saloon and 'Touring' estate", "I (Europe 2025–)", 4840, "BYD DM-i",
    ["PHEV"], "on_sale", "Seal 6 DM-i saloon and Seal 6 DM-i Touring both listed on byd.com/uk (Oct 2026); Germany sells the Touring (EUR 42,990, Sept 2026)",
    [BYD_UK, BYD_DE_OVERVIEW], other_names=["BYD Qin L DM-i (China, saloon)"],
    commons_category="Category:BYD Seal 6", wikipedia_en="BYD Seal 6",
    notes="Saloon 4,840 mm, Touring 4,850 mm - one tile. Swiss status unknown. Commons category unverified."))

A(m("BYD", BYDG, "Seal U", "Seal U DM-i", "d-suv", "SUV", "I (Europe 2024–; facelift 2026)", 4775, "BYD DM-i",
    ["PHEV"], "on_sale", "Listed on byd.com/uk (Oct 2026); Germany EUR 39,990 (Sept 2026); on sale in Switzerland (May 2025)",
    [BYD_UK, BYD_DE_OVERVIEW, BYD_CH_MONEYCAB], other_names=["BYD Song Plus (China)"],
    ch_on_sale=True, ch_source=BYD_CH_MONEYCAB,
    commons_category="Category:BYD Song Plus", wikipedia_en="BYD Song Plus",
    notes="The BEV Seal U was dropped in Europe in 2025 (not on the UK/DE lists any more); only the DM-i PHEV remains. Facelift 2026 announced in Germany."))

A(m("BYD", BYDG, "Sealion 5", "Sealion 5 DM-i", "d-suv", "SUV", "I (Europe 2026–)", 4735, "BYD DM-i",
    ["PHEV"], "on_sale", "UK 'BYD Super Hybrid SUV' - finance offer for orders 7 Oct-31 Dec 2026 'subject to availability at participating retailers' (byd.com/uk model page, Oct 2026); not on the German list",
    [BYD_UK_SEALION5, BYD_UK], other_names=["BYD Song Pro DM-i (China)"],
    commons_category="Category:BYD Song Pro", wikipedia_en="BYD Sealion 5",
    notes="Length approx. (Song Pro 2024 = 4,735 mm; UK page gives no dimensions) - verify. Placed in d-suv by length (sits just below the Seal U)."))

A(m("BYD", BYDG, "Sealion 7", "Sealion 7", "d-suv", "SUV coupé", "I (2024–; Europe 2025–)", 4830, "BYD e-Platform 3.0 Evo",
    ["BEV"], "on_sale", "Listed on byd.com/uk (Oct 2026); Germany EUR 44,990 (Sept 2026); on sale in Switzerland (May 2025)",
    [BYD_UK, BYD_DE_OVERVIEW, BYD_CH_MONEYCAB], other_names=["BYD Sealion 07 EV (China)"],
    ch_on_sale=True, ch_source=BYD_CH_MONEYCAB,
    commons_category="Category:BYD Sealion 07 EV", wikipedia_en="BYD Sealion 07 EV",
    notes="Commons category unverified."))

A(m("BYD", BYDG, "Ti 7", "Ti 7 DM-p", "e-suv", "boxy SUV, 5 seats ('Urban Box Family SUV')", "I (China 2025–; UK 2026–)", 4999, "BYD / Fangchengbao (range-extender)",
    ["PHEV"], "on_sale", "UK model page describes an 'Urban Box Family SUV' DM-p; finance offer applies to orders from 1/7 Oct 2026, so orders are open (byd.com/uk, Oct 2026)",
    [BYD_UK_TI7, BYD_UK, WIKI_TAI7], other_names=["Fangchengbao Tai 7 / Ti7 (China)"],
    commons_category="Category:Fangchengbao Tai 7", wikipedia_en="Fangchengbao Tai 7",
    notes="= Fangchengbao Ti7 (production from Aug 2025, shown as 'BYD Ti7' global model in Bangkok 2025; 1.5T range-extender EREV, 5 seats; BEV version added 2026 in China). Length 4,999 mm is from general knowledge of the Chinese model, not from the fetched pages - verify; row e-suv by that length although BYD UK calls it a family SUV. Commons category unverified."))

A(m("BYD", BYDG, "Tang", "Tang", "e-suv", "SUV, 7 seats", "II facelift (Europe 2021–, 2024 update)", 4870, "BYD",
    ["BEV"], "on_sale", "Germany EUR 75,000 (price list Sept 2026); Switzerland from c. CHF 69,990 (carify, Apr 2026); not in the UK range",
    [BYD_DE_OVERVIEW, CARIFY_CH], ch_on_sale=True, ch_source=CARIFY_CH,
    commons_category="Category:BYD Tang (second generation)", wikipedia_en="BYD Tang",
    notes="Commons category unverified."))

A(m("BYD", BYDG, "Shark", "Shark DMO", "pickup", "double-cab pickup", "I (2024–; UK 2026)", 5457, "BYD DMO",
    ["PHEV"], "on_sale", "UK model page 'Dual Mode Off-Road Plug-in Hybrid' with a finance offer on orders 7 Oct-31 Dec 2026, i.e. orders open (byd.com/uk, Oct 2026)",
    [BYD_UK_SHARK, BYD_UK], other_names=["BYD Shark 6 (AU)"],
    commons_category="Category:BYD Shark", wikipedia_en="BYD Shark",
    notes="Continental availability not verified."))

# =============================== Denza =======================================
A(m("Denza", BYDG, "Z9 GT", "Z9 GT", "e-car", "shooting brake / estate", "I (Europe 2026–)", 5180, "BYD e³ platform",
    ["BEV", "PHEV"], "on_sale", "Pre-orders opened 8 Apr 2026 in seven European markets incl. FR/DE/IT/ES (EUR 101,000 PHEV / 115,000 BEV); UK orders open since Jul 2026 (GBP 95k/105k); German site offers a Z9GT configurator (Oct 2026)",
    [DENZA_CHINAEVHOME, DENZA_AUTOEVO_UK, DENZA_DE, BYD_DE_OVERVIEW], other_names=["Z9GT"],
    commons_category="Category:Denza Z9 GT", wikipedia_en="Denza Z9",
    notes="Swiss status unknown. Commons category unverified."))


# =============================== Omoda / Jaecoo / Chery / Lepas ===============
CHERY = "Chery"
OJ_NOTE_CH = "Switzerland: omodajaecoo.ch shows only 'Coming soon' (Grand Automotive) as of Oct 2026."
T1X_SRC = [OJ_CARGURUS, CHERY_CARWOW_UK]
A(m("Omoda", CHERY, "Omoda 5", "Omoda 5", "c-suv", "SUV", "I (2022–; Europe 2024–; facelift 2025)", 4400, "Chery T1X",
    ["petrol", "HEV", "BEV"], "on_sale", "Omoda 5 petrol, Omoda 5 SHS-H hybrid and Omoda 5 E5 (BEV) listed on omodaauto.co.uk (Oct 2026); on sale across DE/ES/IT/PL etc.",
    [OMODA_UK, OJ_CARGURUS, CHERY_HYE], other_names=["Omoda E5 (BEV)", "Chery Omoda 5", "Chery Tiggo 5x High Energy (China, since late 2024)"],
    ch_on_sale=False, ch_source=OJ_CH,
    twin_tier=2, twin_members=["Jaecoo 7", "Omoda 7", "Chery Tiggo 7"],
    twin_note="Chery compact (T1X-family) group in c-suv: Omoda 7 is built on a stretched Omoda C5 platform (Wikipedia, Omoda 7); Jaecoo 7 = Chery Tansuo 06, which China also sells as 'Tiggo 7 High Energy' (Wikipedia, Jaecoo 7 / Tiggo 7); all share the 1.6T DCT and 1.5T SHS PHEV drivetrains with the European Tiggo 7. Distinct bodies -> tier 2. In China the Omoda 5 itself was renamed Tiggo 5x High Energy (cosmetic changes), i.e. it is closest to the Tiggo 4/5x line, which sits in b-suv here (cross-row, no group).",
    twin_sources=[WIKI_OMODA7, WIKI_JAECOO7, WIKI_OMODA5, WIKI_TIGGO7],
    commons_category="Category:Chery Omoda 5", wikipedia_en="Chery Omoda 5",
    notes=OJ_NOTE_CH))

A(m("Omoda", CHERY, "Omoda 7", "Omoda 7", "c-suv", "SUV", "I (2025–; Europe 2026–)", 4620, "Chery T1X family (stretched Omoda C5 platform)",
    ["petrol", "PHEV"], "on_sale", "Omoda 7 petrol and Omoda 7 SHS-P (PHEV) listed with finance offers on omodaauto.co.uk (Oct 2026); CarGurus Sept 2026 lists it on sale; European debut Feb 2026",
    [OMODA_UK, OJ_CARGURUS, CHERY_HYE, WIKI_OMODA7], other_names=["Chery Tiggo 7L (China, from Apr 2026)"],
    ch_on_sale=False, ch_source=OJ_CH,
    twin_tier=2, twin_members=["Omoda 5", "Jaecoo 7", "Chery Tiggo 7"],
    twin_note="Built on a stretched Omoda C5 platform; sold in China as Chery Tiggo 7L (Wikipedia). See Omoda 5 for the group.",
    twin_sources=[WIKI_OMODA7, WIKI_OMODA5],
    commons_category="Category:Omoda 7", wikipedia_en="Omoda 7",
    notes="4.62 m, upper end of c-suv. Commons category unverified. " + OJ_NOTE_CH))

A(m("Omoda", CHERY, "Omoda 9", "Omoda 9", "d-suv", "SUV", "I (Europe 2025–)", 4775, "Chery M3X (Exeed RX)",
    ["PHEV"], "on_sale", "Listed with finance offer on omodaauto.co.uk (Oct 2026); 'renewed Omoda 9 PHEV' for Europe (Nov 2025)",
    [OMODA_UK, OJ_CARGURUS, CHERY_HYE], other_names=["Exeed RX / Exeed Yaoguang (China)"],
    ch_on_sale=False, ch_source=OJ_CH,
    commons_category="Category:Exeed RX", wikipedia_en="Exeed RX",
    notes="Rebadged Exeed RX (Exeed is not sold in Europe, so no European twin). 1.5T SHS PHEV 443 bhp. " + OJ_NOTE_CH))

A(m("Jaecoo", CHERY, "Jaecoo 5", "Jaecoo 5", "c-suv", "SUV", "I (2025–)", 4380, None,
    ["petrol", "BEV"], "on_sale", "Listed from GBP 24,555 on jaecoo.co.uk (Oct 2026) incl. Jaecoo 5 EV; UK deliveries since Oct 2025 (Wikipedia); CarGurus Sept 2026 lists it on sale",
    [JAECOO_UK, OJ_CARGURUS, WIKI_JAECOO5], other_names=["Jaecoo E5 (BEV)"],
    ch_on_sale=False, ch_source=OJ_CH,
    commons_category="Category:Jaecoo 5", wikipedia_en="Jaecoo 5",
    notes="4.38 m: b-suv/c-suv boundary; kept with Omoda 5 in c-suv. No platform/sibling information found (Wikipedia gives none) - no tier. Commons category unverified. " + OJ_NOTE_CH))

A(m("Jaecoo", CHERY, "Jaecoo 7", "Jaecoo 7", "c-suv", "SUV", "I (2023–; Europe 2024–)", 4500, "Chery T1X",
    ["petrol", "PHEV", "HEV"], "on_sale", "Listed from GBP 29,210 on jaecoo.co.uk (Oct 2026) with SHS PHEV/HEV; Jaecoo 7 SHS was the group's first official car in Germany (early 2026)",
    [JAECOO_UK, OJ_CARGURUS, CHERY_ELECTRIVE_DE], other_names=["Chery Tansuo 06 / Tiggo 7 High Energy (China)"],
    ch_on_sale=False, ch_source=OJ_CH,
    twin_tier=2, twin_members=["Omoda 5", "Omoda 7", "Chery Tiggo 7"],
    twin_note="Jaecoo 7 = Chery Tansuo 06 (China, 2,650 mm wheelbase; sold there also as Tiggo 7 High Energy PHEV) per Wikipedia; same T1X family as the Omoda 5 and the European Chery Tiggo 7 (different bodies) - tier 2.",
    twin_sources=[WIKI_JAECOO7] + T1X_SRC,
    commons_category="Category:Jaecoo 7", wikipedia_en="Jaecoo 7",
    notes=OJ_NOTE_CH))

A(m("Jaecoo", CHERY, "Jaecoo 8", "Jaecoo 8", "d-suv", "SUV, 6/7 seats", "I (Europe 2025–)", 4820, "Chery T1X/M3X (Tiggo 9)",
    ["PHEV"], "on_sale", "Listed from GBP 45,500 on jaecoo.co.uk (Oct 2026); CarGurus Sept 2026 lists it on sale",
    [JAECOO_UK, OJ_CARGURUS],
    ch_on_sale=False, ch_source=OJ_CH,
    twin_tier=1, twin_members=["Chery Tiggo 9"],
    twin_note="Wikipedia (Chery Tiggo 9): the Tiggo 9 'is also exported under the Jaecoo brand as the Jaecoo J8/8' (first shown as Jaecoo 9); T1X platform, 4,820 mm. Both are sold in the UK - tier 1 rebadge.",
    twin_sources=[WIKI_TIGGO9, CHERY_CARWOW_UK, JAECOO_UK],
    commons_category="Category:Jaecoo 8", wikipedia_en="Chery Tiggo 9",
    notes="Commons category unverified. " + OJ_NOTE_CH))

CHERY_NOTE = "Chery-brand cars are sold in the UK (25+ dealers since 2025), Spain/Italy/Poland (official importers; Spain production with Ebro at the former Nissan Barcelona plant); Germany launch 1H 2027 (announced Aug 2026). No Swiss presence found."
A(m("Chery", CHERY, "Tiggo 4", "Tiggo 4", "b-suv", "SUV", "II (2023–; UK 2025–)", 4318, "Chery T1X",
    ["petrol", "HEV"], "on_sale", "UK new from GBP 17,856 (carwow, Oct 2026); announced for Germany 1H 2027",
    [CHERY_CARWOW_UK, CHERY_ELECTRIVE_DE], other_names=["Chery Tiggo 4 Pro", "Chery Tiggo 5x (China)", "Ebro S400 (ES, unverified)"],
    ch_on_sale=False, ch_source=None,
    twin_tier=None, twin_members=[], twin_note="Spanish Ebro S400 is reported to be a Tiggo 4 rebadge (tier 1) - Ebro not covered here, unverified.",
    commons_category="Category:Chery Tiggo 4 Pro", wikipedia_en="Chery Tiggo 4",
    notes=CHERY_NOTE))

A(m("Chery", CHERY, "Tiggo 7", "Tiggo 7", "c-suv", "SUV", "II facelift (2024–; UK 2025–)", 4513, "Chery T1X",
    ["petrol", "PHEV", "HEV"], "on_sale", "UK new from GBP 20,732, petrol and PHEV (carwow, Oct 2026); announced for Germany 1H 2027",
    [CHERY_CARWOW_UK, CHERY_ELECTRIVE_DE, WIKI_TIGGO7], other_names=["Chery Tiggo 7 Pro/Plus", "Ebro S700 (ES)", "DR 6.0 / Sportequipe 6 (IT)"],
    ch_on_sale=False, ch_source=None,
    twin_tier=1, twin_members=["Ebro S700", "DR 6.0", "Sportequipe 6"],
    twin_note="Second-generation Tiggo 7 (2020-, facelift 2024), in Europe since June 2025. Wikipedia: Ebro 'produced a licensed-built second-generation Tiggo 7' as the Ebro S700 (Spain); DR Automobiles 'marketed the second-generation Tiggo 7 in Italy as the DR 6.0' and Sportequipe 'sold a version ... as the Sportequipe 6' -> tier-1 rebadges (brands outside this assignment, 2026 availability not re-checked). Additionally a tier-2 platform sibling of Omoda 5 / Jaecoo 7 / Omoda 7 (see Omoda 5) - one tile can carry only one tier here, so the rebadge tier is recorded and the tier-2 link is noted.",
    twin_sources=[WIKI_TIGGO7, WIKI_OMODA7, WIKI_JAECOO7],
    commons_category="Category:Chery Tiggo 7 (second generation)", wikipedia_en="Chery Tiggo 7",
    notes=CHERY_NOTE))

A(m("Chery", CHERY, "Tiggo 8", "Tiggo 8", "d-suv", "SUV, 7 seats", "II (2024–; UK 2025–)", 4722, "Chery T1X",
    ["petrol", "PHEV"], "on_sale", "UK new from GBP 23,959, petrol and PHEV (carwow, Oct 2026); announced for Germany 1H 2027",
    [CHERY_CARWOW_UK, CHERY_ELECTRIVE_DE, WIKI_TIGGO8], other_names=["Chery Tiggo 8 Pro/Plus II", "Ebro S800 (ES)", "DR 7.0 / Sportequipe 7 (IT)"],
    ch_on_sale=False, ch_source=None,
    twin_tier=1, twin_members=["Ebro S800"],
    twin_note="UK/European Tiggo 8 (debut Goodwood Jul 2025) uses Tiggo 8 Plus II styling (petrol) / 2024 export-facelift styling (Super Hybrid), 4,722 mm. Wikipedia: 'The Tiggo 8 is rebadged and sold in Spain by Ebro as the Ebro S800' -> tier 1 (Ebro outside this assignment). DR 7.0 / Sportequipe 7 (Italy) are listed as names of the same model without an explicit rebadging sentence. The Lepas L8 (4,670 mm) derives from the NEW second-generation Tiggo 8 (2025), a different body - no tier.",
    twin_sources=[WIKI_TIGGO8],
    commons_category="Category:Chery Tiggo 8 Plus", wikipedia_en="Chery Tiggo 8",
    notes=CHERY_NOTE))

A(m("Chery", CHERY, "Tiggo 9", "Tiggo 9", "d-suv", "SUV, 7 seats", "I (2023–; UK 2025–)", 4820, "Chery T1X/M3X",
    ["PHEV"], "on_sale", "UK new from GBP 36,513, seven seats (carwow, Oct 2026); announced for Germany 1H 2027",
    [CHERY_CARWOW_UK, CHERY_ELECTRIVE_DE], other_names=["Chery Tiggo 9 PHEV"],
    ch_on_sale=False, ch_source=None,
    twin_tier=1, twin_members=["Jaecoo 8"], twin_note="See Jaecoo 8 (export version of the Tiggo 9).", twin_sources=[WIKI_TIGGO9, CHERY_CARWOW_UK, JAECOO_UK],
    commons_category="Category:Chery Tiggo 9", wikipedia_en="Chery Tiggo 9",
    notes=CHERY_NOTE))

# =============================== GWM: Ora / Wey / Haval =======================
GWM = "Great Wall Motor"
GWM_CH_NOTE = "No Swiss GWM presence found (gwm.ch could not be fetched); ch_on_sale unknown."
A(m("Ora", GWM, "Ora 03", "Ora 03", "c-hatch", "5-door hatchback", "I (2022–)", 4235, "GWM L.E.M.O.N. (ME platform)",
    ["BEV"], "on_sale", "Offered in Germany (GWM leasing/dealer listings, Oct 2026); UK: carwow shows it as 'currently unavailable new' (Oct 2026), so UK may be runout",
    [GWM_GOLEASY, GWM_CARWOW_UK, GWM_AUTONOTIZEN], other_names=["Ora Funky Cat (UK, 2022–24)", "GWM Ora 03 (UK)", "Ora Good Cat (China)"],
    commons_category="Category:Ora Good Cat", wikipedia_en="Ora Good Cat",
    notes="4.24 m: between b-hatch and c-hatch; placed c-hatch (ID.3/MG4 rival). " + GWM_CH_NOTE))

A(m("Ora", GWM, "Ora 07", "Ora 07", "d-car", "5-door fastback saloon", "I (2023–)", 4871, "GWM L.E.M.O.N.",
    ["BEV"], "on_sale", "Offered in Germany (GWM leasing listings, Oct 2026)",
    [GWM_GOLEASY], other_names=["Ora Lightning Cat (China)", "GWM Ora 07 (UK, announced)"],
    commons_category="Category:Ora Lightning Cat", wikipedia_en="Ora Lightning Cat",
    notes="Status based on a German leasing listing; official GWM Germany page not fetched. " + GWM_CH_NOTE))

A(m("Wey", GWM, "Wey 03", "Wey 03", "c-suv", "SUV", "I (2023–)", 4520, "GWM L.E.M.O.N.",
    ["PHEV"], "on_sale", "Offered in Germany (GWM leasing listings, Oct 2026)",
    [GWM_GOLEASY], other_names=["Wey Latte / Wey Lanshan (China)"],
    commons_category="Category:Wey Latte", wikipedia_en="Wey Latte",
    notes="Status based on a German leasing listing; official page not fetched. " + GWM_CH_NOTE))

A(m("Wey", GWM, "Wey 05", "Wey 05", "d-suv", "SUV", "I (2022–)", 4871, "GWM L.E.M.O.N.",
    ["PHEV"], "on_sale", "Offered in Germany (GWM leasing listings, Oct 2026), 476 PS PHEV",
    [GWM_GOLEASY], other_names=["Wey Coffee 01 (DE, 2022–23)", "Wey Mocha (China)"],
    commons_category="Category:Wey Mocha", wikipedia_en="Wey Mocha",
    notes="4.87 m: d-suv (just under 4.9). " + GWM_CH_NOTE))

A(m("Haval", GWM, "Jolion Pro", "Jolion Pro", "c-suv", "SUV", "I facelift (2024–; Europe 2025/26–)", 4470, "GWM L.E.M.O.N.",
    ["petrol", "HEV"], "on_sale", "UK from GBP 23,995 (carwow, Oct 2026, hybrid); Germany from EUR 24,990 (petrol 177 hp; autohaus.de, Mar 2026)",
    [GWM_CARWOW_UK, GWM_AUTOHAUS, GWM_GOLEASY], other_names=["GWM Haval Jolion Pro (UK)"],
    commons_category="Category:Haval Jolion", wikipedia_en="Haval Jolion",
    notes=GWM_CH_NOTE))

A(m("Haval", GWM, "H6", "H6", "d-suv", "SUV", "III facelift (2024–; Germany 2026–)", 4703, "GWM L.E.M.O.N.",
    ["HEV"], "on_sale", "Germany from EUR 31,990, full hybrid 243 hp, launch Jan 2026 (autohaus.de, Mar 2026); on German leasing listings (Oct 2026)",
    [GWM_AUTOHAUS, GWM_GOLEASY, GWM_AUTONOTIZEN],
    commons_category="Category:Haval H6 (third generation)", wikipedia_en="Haval H6",
    notes="UK availability not verified. " + GWM_CH_NOTE))

# =============================== XPeng =======================================
XP = "XPeng"
A(m("XPeng", XP, "G6", "G6", "d-suv", "SUV coupé", "I (2023–; 2025 update)", 4753, "XPeng SEPA 2.0 (800 V)",
    ["BEV"], "on_sale", "Listed on xpeng.com/de (Oct 2026); UK updated version from GBP 39,990 (2026); Switzerland via Emil Frey (carify, Apr 2026)",
    [XPENG_DE, XPENG_FLEETWORLD, CARIFY_CH], ch_on_sale=True, ch_source=CARIFY_CH,
    commons_category="Category:XPeng G6", wikipedia_en="XPeng G6", notes=""))

A(m("XPeng", XP, "G9", "G9", "d-suv", "SUV", "I (2022–; 2025 update)", 4891, "XPeng SEPA 2.0 (800 V)",
    ["BEV"], "on_sale", "Listed on xpeng.com/de (Oct 2026); Switzerland via Emil Frey (carify, Apr 2026)",
    [XPENG_DE, CARIFY_CH], ch_on_sale=True, ch_source=CARIFY_CH,
    commons_category="Category:XPeng G9", wikipedia_en="XPeng G9", notes=""))

A(m("XPeng", XP, "P7+", "P7+", "e-car", "5-door fastback saloon", "I (2024–; Europe 2025–)", 5017, "XPeng SEPA 2.0",
    ["BEV"], "on_sale", "Listed on xpeng.com/de with a EUR 2,500 bonus (Oct 2026); goingelectric.de from EUR 46,600",
    [XPENG_DE, XPENG_GOINGELECTRIC],
    commons_category="Category:XPeng P7+", wikipedia_en="XPeng P7+",
    notes="5.02 m, so e-car by length although priced like a D-car (the old P7 was 4.88 m). Swiss status unknown. Commons category unverified."))

A(m("XPeng", XP, "X9", "X9", "mpv-large", "MPV, 7 seats", "I (2024–; Europe 2025/26–)", 5293, "XPeng SEPA 2.0 (800 V)",
    ["BEV"], "on_sale", "Listed on xpeng.com/de with a EUR 5,000 bonus and configurator (Oct 2026); UK arrival mid-2026 (Fleet World); goingelectric.de from EUR 77,600",
    [XPENG_DE, XPENG_FLEETWORLD, XPENG_GOINGELECTRIC],
    commons_category="Category:XPeng X9", wikipedia_en="XPeng X9",
    notes="Swiss status unknown. Commons category unverified."))

A(m("XPeng", XP, "L03", "L03", "c-suv", "SUV coupé", "I (Europe 2026–)", 4650, "XPeng (800 V; BEV and 'PowerX' range-extender)",
    ["BEV", "PHEV"], "on_sale", "German model page: 4,650 mm, wheelbase 2,850 mm, from EUR 35,600 UVP, 'Jetzt konfigurieren' configurator live, tagged NEU (xpeng.com/de/model/L03, Oct 2026)",
    [XPENG_DE_L03, XPENG_DE, XPENG_GOINGELECTRIC],
    commons_category=None, wikipedia_en=None,
    notes="New European nameplate (Oct 2026). Range-extender 'PowerX' version counted as PHEV. 4.65 m -> c-suv (boundary with d-suv). Chinese source model and Commons category not identified - VERIFY."))

A(m("XPeng", XP, "G9L", "G9L", "e-suv", "SUV, 6/7 seats", "I (Europe 2026–)", 5120, "XPeng SEPA 2.0 (800 V)",
    ["BEV"], "on_sale", "German model page: 5,120 mm, wheelbase 3,100 mm, 6 or 7 seats, from EUR 85,600 UVP, configurator live, tagged NEU (xpeng.com/de/model/G9L, Oct 2026)",
    [XPENG_DE_G9L, XPENG_DE, XPENG_GOINGELECTRIC],
    commons_category=None, wikipedia_en=None,
    notes="Flagship 3-row SUV above the G9 (its Chinese name may differ, e.g. G01/'G7L' - not verified). No Commons category known."))

# =============================== NIO / Firefly ================================
NIOG = "NIO"
NIO_STATUS = "NIO's own European configurators (DE/NL/SE/NO) no longer offer factory orders - sales are from remaining stock with clearance discounts; Nio House Hamburg and the Weiterstadt hub closed in July 2026 (eletric-vehicles.com, 23 Aug 2026). Model still listed on nio.com/de_DE (Oct 2026)."
NIO_CH = "Switzerland: carify (Apr 2026) lists ET5/ET7/EL7 'from around CHF 60,000' but NIO has no official Swiss network - treated as unknown."
A(m("NIO", NIOG, "ET5", "ET5 / ET5 Touring", "d-car", "4-door saloon and Touring estate", "I (2022–; Touring 2023–)", 4790, "NIO NT2.0",
    ["BEV"], "runout", "ET5 Touring stock available in NO/NL; ET5 saloon sold out in NL and absent from the DE configurator. " + NIO_STATUS,
    [NIO_DE, NIO_EV_STATUS], ch_on_sale=None, ch_source=CARIFY_CH,
    commons_category="Category:NIO ET5", wikipedia_en="NIO ET5",
    notes="Saloon and Touring estate in one tile (body styles). " + NIO_CH))

A(m("NIO", NIOG, "ET7", "ET7", "e-car", "4-door saloon", "I (2022–; 2025 update)", 5101, "NIO NT2.0",
    ["BEV"], "runout", "Appears sold out in NL; no new-build orders. " + NIO_STATUS,
    [NIO_DE, NIO_EV_STATUS], ch_on_sale=None, ch_source=CARIFY_CH,
    commons_category="Category:NIO ET7", wikipedia_en="NIO ET7", notes=NIO_CH))

A(m("NIO", NIOG, "EL6", "EL6", "d-suv", "SUV", "I (2023–)", 4854, "NIO NT2.0",
    ["BEV"], "runout", "Stock available in DE/NO/NL; no new-build orders. " + NIO_STATUS,
    [NIO_DE, NIO_EV_STATUS], other_names=["NIO ES6 (China)"],
    commons_category="Category:NIO ES6 (second generation)", wikipedia_en="NIO ES6", notes=NIO_CH))

A(m("NIO", NIOG, "EL7", "EL7", "e-suv", "SUV", "I (2022–)", 4912, "NIO NT2.0",
    ["BEV"], "runout", "Appears sold out in NL; no new-build orders. " + NIO_STATUS,
    [NIO_DE, NIO_EV_STATUS], other_names=["NIO ES7 (China)"],
    commons_category="Category:NIO ES7", wikipedia_en="NIO ES7", notes=NIO_CH))

A(m("NIO", NIOG, "EL8", "EL8", "e-suv", "SUV, 6/7 seats", "II (2024–)", 5099, "NIO NT2.0",
    ["BEV"], "runout", "Stock available in DE/NO/NL/SE; no new-build orders. " + NIO_STATUS,
    [NIO_DE, NIO_EV_STATUS], other_names=["NIO ES8 (China, 2nd gen)"],
    commons_category="Category:NIO ES8 (second generation)", wikipedia_en="NIO ES8", notes=NIO_CH))

A(m("Firefly", NIOG, "Firefly", "Firefly", "b-hatch", "5-door hatchback", "I (2025–)", 4003, "NIO (Firefly platform)",
    ["BEV"], "on_sale", "Deliveries since Aug 2025 in NL (EUR 29,900) and Norway; also Belgium, Denmark, Greece, Austria, Portugal by Dec 2025; UK debut 2026 with RHD in production (evpowered, Nov 2025)",
    [FIREFLY_ELECTRIVE, FIREFLY_CNC, FIREFLY_EVPOWERED], ch_on_sale=None, ch_source=None,
    commons_category="Category:Firefly (car)", wikipedia_en="Firefly (car)",
    notes="4.0 m: a-city/b-hatch boundary; b-hatch (Renault 5 rival). Germany/Switzerland status not verified. Commons category unverified."))

# =============================== Changan / Deepal =============================
CHG = "Changan"
A(m("Deepal", CHG, "S07", "S07", "d-suv", "SUV", "I (2023–; Europe 2025–)", 4750, "Changan EPA1",
    ["BEV"], "on_sale", "On sale in Germany (EUR 44,990), Italy, Spain, UK, Norway (electrive, Dec 2025); PHEV/REEV version announced for 2026",
    [CHANGAN_ELECTRIVE_DEC, CHANGAN_ELECTRIVE_AVATR], other_names=["Changan Deepal S07", "Deepal S7 (China)"],
    ch_on_sale=None, ch_source=None,
    twin_tier=2, twin_members=["Mazda CX-6e"],
    twin_note="Mazda CX-6e (= Mazda EZ-60, built by Changan Mazda, European launch Brussels Jan 2026) is 'heavily based on the Deepal S07' and shares its BEV/EREV powertrains on the EPA1 platform, with its own body (Wikipedia) - tier 2. The Mazda 6e (= EZ-6) is likewise an EPA1 sibling of the Deepal L07/SL03, which is not sold in Europe, so no European twin for the 6e.",
    twin_sources=[WIKI_EZ60, CHANGAN_ELECTRIVE_AVATR],
    commons_category="Category:Deepal S7", wikipedia_en="Deepal S07",
    notes="Swiss status unknown (no Changan Switzerland found)."))

A(m("Deepal", CHG, "S05", "S05", "c-suv", "SUV", "I (2024–; Europe 2025–)", 4620, "Changan EPA1",
    ["BEV"], "on_sale", "Germany from EUR 38,990, Italy EUR 39,990, Spain; Denmark from Mar 2026 (electrive, Dec 2025); PHEV version announced for 2026",
    [CHANGAN_ELECTRIVE_DEC], other_names=["Changan Deepal S05"],
    ch_on_sale=None, ch_source=None,
    commons_category="Category:Deepal S05", wikipedia_en="Deepal S05",
    notes="Commons category unverified."))

# =============================== Dongfeng / Voyah =============================
DF = "Dongfeng"
VOYAH_NOTE = "Voyah sells through importers with official brand sites in Norway (Electric Way), the Netherlands (Gomes), Switzerland (Noyo Mobility), Finland, Sweden, Denmark; voyah.eu blocks fetches. On voyah.no (Oct 2026) only the Courage is current; Free and Dream are marked 'Utgatt modell' (discontinued) in Norway."
A(m("Voyah", DF, "Free", "Free", "e-suv", "SUV", "I (2021–; facelift 2024)", 4905, "Dongfeng ESSA",
    ["BEV", "PHEV"], "on_sale", "Netherlands: Limited Edition EUR 53,990 'direct uit voorraad' (voyah.nl, Oct 2026); Switzerland: Noyo Mobility from CHF 69,900 (carify, Apr 2026); discontinued in Norway (voyah.no, Oct 2026)",
    [VOYAH_NL, CARIFY_CH, VOYAH_NO, VOYAH_GASGOO_EU], ch_on_sale=True, ch_source=CARIFY_CH,
    commons_category="Category:Voyah Free", wikipedia_en="Voyah Free",
    notes="Offered as BEV and range-extender (EREV counted as PHEV). 4.9 m -> e-suv. NL sells from stock, so possibly late in its run. " + VOYAH_NOTE))

A(m("Voyah", DF, "Dream", "Dream", "mpv-large", "MPV, 7 seats", "I (2022–)", 5315, "Dongfeng ESSA",
    ["BEV", "PHEV"], "on_sale", "Netherlands: listed from EUR 91,857 (Flagship Edition EUR 86,857) on voyah.nl (Oct 2026); discontinued in Norway (voyah.no, Oct 2026)",
    [VOYAH_NL, VOYAH_NO, VOYAH_GASGOO_EU], ch_on_sale=None, ch_source=None,
    commons_category="Category:Voyah Dream", wikipedia_en="Voyah Dream",
    notes="Only the Dutch importer still lists it (with price). " + VOYAH_NOTE))

A(m("Voyah", DF, "Courage", "Courage", "d-suv", "SUV", "I (2024–)", 4725, "Dongfeng ESSA",
    ["BEV"], "on_sale", "Netherlands: 'Nu verkrijgbaar', Business Edition EUR 39,990 (voyah.nl, Oct 2026); Norway from NOK 299,990 via Electric Way (voyah.no, Oct 2026); launched Oct 2024 in NO/SE/FI",
    [VOYAH_NL, VOYAH_NO, VOYAH_GASGOO_COURAGE], ch_on_sale=None, ch_source=None, other_names=["Voyah Zhiyin (China)"],
    commons_category="Category:Voyah Courage", wikipedia_en="Voyah Courage",
    notes=VOYAH_NOTE))

A(m("Dongfeng", DF, "Box", "Box", "b-hatch", "5-door hatchback", "I (2023–; NL 2024–)", 4030, "Dongfeng (Nammi 01)",
    ["BEV"], "on_sale", "Listed by the Dutch Dongfeng/Voyah importer (voyah.nl, Oct 2026: 42.3 kWh, 70 kW, 310 km WLTP, own site dongfengbox.nl); the page gives no price or explicit order status",
    [VOYAH_NL_BOX, VOYAH_NL], other_names=["Dongfeng Nammi 01 (China)"],
    commons_category="Category:Dongfeng Nammi 01", wikipedia_en="Dongfeng Nammi 01",
    notes="Length 4,030 mm from general knowledge of the Nammi 01 (not on the fetched page). Only Dutch evidence found; status should be confirmed on dongfengbox.nl. Dongfeng brand column = group 'Dongfeng'."))

A(m("Mhero", DF, "Mhero I", "Mhero I", "offroad", "ladder-frame luxury off-roader", "I (2022–; NL 2025–)", 4987, "Dongfeng M-Hero (MORA)",
    ["BEV"], "on_sale", "Listed by the Dutch Dongfeng/Voyah importer with a price-list PDF and showroom cars in Alkmaar and Veghel (voyah.nl/mhero, Oct 2026): four motors, 142.7 kWh, 480 km WLTP",
    [VOYAH_NL_MHERO, VOYAH_NL], other_names=["M-Hero 917 (China)"],
    commons_category="Category:Mengshi 917", wikipedia_en="Mengshi 917",
    notes="Length 4,987 mm from general knowledge of the M-Hero 917 (not on the fetched page). Extra brand found during research: Mhero is Dongfeng's off-road luxury brand (group label 'Dongfeng'). Order status not explicitly confirmed - VERIFY."))

# =============================== FAW / Hongqi =================================
FAW = "FAW"
HONGQI_NOTE = "Hongqi sells via importers with official sites in Norway (HBI Norge / Motor Gruppen), Netherlands, Sweden, Denmark; Switzerland has service centres (Hongqi, 2024) but no Swiss sales site was found. Norwegian line-up (hongqi.no/biler, Oct 2026): EHS5, EH7, EHS7, E-HS9."
A(m("Hongqi", FAW, "EHS5", "EHS5", "d-suv", "SUV", "I (2025–; Norway 2026)", 4750, "FAW FMEs",
    ["BEV"], "on_sale", "New model ('nyheten EHS5') on hongqi.no, in stock, from NOK 439,900 (Oct 2026); 4,750 mm, wheelbase 2,900 mm, 85 kWh LFP, AWD 563 hp",
    [HONGQI_NO, HONGQI_NO_BILER, HONGQI_EHS5_SPEC], ch_on_sale=None, ch_source=None,
    commons_category="Category:Hongqi EHS5", wikipedia_en="Hongqi EHS5",
    notes="Commons category unverified. " + HONGQI_NOTE))

A(m("Hongqi", FAW, "EH7", "EH7", "e-car", "4-door saloon", "I (2024–)", 4980, "FAW FMEs",
    ["BEV"], "on_sale", "Listed from NOK 499,900 on hongqi.no/biler (Oct 2026); European launch via Norway (Motor Gruppen, 2024) at EUR 49,999",
    [HONGQI_NO_BILER, HONGQI_GASGOO, HONGQI_FLEETWORLD], ch_on_sale=None, ch_source=None,
    commons_category="Category:Hongqi EH7", wikipedia_en="Hongqi EH7",
    notes=HONGQI_NOTE))

A(m("Hongqi", FAW, "EHS7", "EHS7", "e-suv", "SUV", "I (2024–)", 4995, "FAW FMEs",
    ["BEV"], "on_sale", "Listed from NOK 544,900 on hongqi.no/biler (Oct 2026); European launch via Norway (2024) at EUR 53,999",
    [HONGQI_NO_BILER, HONGQI_GASGOO, HONGQI_FLEETWORLD], ch_on_sale=None, ch_source=None,
    commons_category="Category:Hongqi EHS7", wikipedia_en="Hongqi EHS7",
    notes=HONGQI_NOTE))

A(m("Hongqi", FAW, "E-HS9", "E-HS9", "e-suv", "SUV, 6/7 seats", "I (2020–; Europe 2021–)", 5209, "FAW",
    ["BEV"], "on_sale", "Listed from NOK 1,299,990 on hongqi.no/biler (Oct 2026)",
    [HONGQI_NO_BILER], ch_on_sale=None, ch_source=None,
    commons_category="Category:Hongqi E-HS9", wikipedia_en="Hongqi E-HS9",
    notes="Only Norwegian evidence; Dutch/Swedish availability not checked. " + HONGQI_NOTE))

# ============================ ANNOUNCED ======================================
ANNOUNCED = []
B = ANNOUNCED.append
B(m("BYD", BYDG, "Seal U facelift", "Seal U DM-i (facelift)", "d-suv", "SUV", "I facelift (2026)", 4775, "BYD DM-i",
    ["PHEV"], "announced", "Facelift announced for Germany during 2026 (same technical base) - not a new tile, just a note",
    [BYD_DE_OVERVIEW], notes="Informational only; the current Seal U tile stays."))
B(m("Denza", BYDG, "D9", "D9", "mpv-large", "MPV, 7 seats (2+2+3)", "I (Europe 2026/27)", 5250, "BYD DM-i",
    ["PHEV"], "announced", "German site: 'Vorbestellbar ab Preisbereich 80.000-90.000 EUR', configurator 'in Kürze verfügbar' (pre-orders open, not yet orderable; denza.com/de/d9, Oct 2026); introduced at the Apr 2026 Paris launch",
    [DENZA_DE_D9, DENZA_CHINAEVHOME, BYD_DE_OVERVIEW],
    commons_category="Category:Denza D9", wikipedia_en="Denza D9",
    notes="DM-i AWD, ~210 km EV / 950 km combined. Expected on sale late 2026/2027."))
B(m("Denza", BYDG, "BAO 5", "BAO 5", "offroad", "ladder-frame off-road SUV", "I (Europe 2026/27)", 4890, "BYD DMO (Fangchengbao)",
    ["PHEV"], "announced", "German model page offers a 'Gestalten Sie Ihren BAO 5' configurator (400 kW, 760 Nm, 0-100 in 4.8 s) but states there is no EU type approval yet and emission values are pending (denza.com/de/modelle/bao-5, Oct 2026); announced for Europe at the Apr 2026 Paris launch as 'B5'",
    [DENZA_DE_BAO5, DENZA_DE, DENZA_CHINAEVHOME], other_names=["Denza B5", "Fangchengbao Bao 5 (China)"],
    commons_category="Category:Fangchengbao Bao 5", wikipedia_en="Fangchengbao Bao 5",
    notes="Treated as 'announced' because no EU type approval yet; may become orderable within months. Commons category unverified."))
B(m("Denza", BYDG, "Z", "Z", "sports", "2-door sports car", "I (2026/27)", None, "BYD e³",
    ["BEV"], "announced", "Listed on denza.com/de ('Geboren für Performance') without configurator (Oct 2026); production/order status unknown",
    [DENZA_DE], notes="Verify whether this is a production model for Europe."))
B(m("Omoda", CHERY, "Omoda 4", "Omoda 4", "b-suv", "SUV", "I (2027)", None, "Chery",
    ["petrol", "HEV", "BEV"], "announced", "European motor-show debut in Paris (Oct 2026) ahead of a 2027 UK launch (omodaauto.co.uk news, Oct 2026)",
    [OMODA_UK], notes=""))
B(m("Chery", CHERY, "Q", "Q", "c-hatch", "compact EV", "I (2027)", None, "Chery",
    ["BEV"], "announced", "Compact EV to be unveiled at the Paris Motor Show Oct 2026, German launch after the 1H 2027 hybrid launch (electrive, Aug 2026)",
    [CHERY_ELECTRIVE_DE], notes="Name/segment provisional."))
B(m("Lepas", CHERY, "L8", "L8", "d-suv", "SUV", "I (2025–; Europe 2026)", 4670, "Chery (second-generation Tiggo 8 family)",
    ["PHEV"], "announced", "European expansion starts Q3/Q4 2026 (UK first, then IT/ES/GR/HR/SI/RO; auto.it 27 Aug 2026); a UK dealer page ('Bassetts Lepas', lepas.co.uk) already exists (Oct 2026); Italian production from mid-2026, Italian dealers expected 2026 at c. EUR 40,000; no price list / order confirmation found",
    [LEPAS_AUTOIT, LEPAS_FLEET, LEPAS_UK_DEALER, WIKI_TIGGO8, "https://www.autohaus.de/nachrichten/autohersteller/chery-fuehrt-vierte-marke-in-europa-ein-lepas-startet-in-grossbritannien-3765830"],
    commons_category="Category:Lepas L8", wikipedia_en="Chery Tiggo 8",
    notes="4,670 mm (Wikipedia, Tiggo 8 article: L8 is the export-only derivative of the 2025 second-generation Tiggo 8). 4.67 m -> d-suv boundary. Probably orderable in the UK by Nov 2026 - verify; L6 (EV/PHEV) and L4 (EV) to follow."))
B(m("Ora", GWM, "Ora 05", "Ora 05", "c-suv", "SUV", "I (2026)", None, "GWM",
    ["BEV", "PHEV", "petrol"], "announced", "German leasing listing (Oct 2026) shows an Ora 05 'from EUR 262/month' but states it is not yet on sale in Germany; autonotizen (Oct 2025): 'Ora 5' compact SUV from EUR 24,990 in 2026 as petrol/hybrid/electric",
    [GWM_GOLEASY, GWM_AUTONOTIZEN], notes="VERIFY - could be on sale by now."))
B(m("Haval", GWM, "H7", "H7", "d-suv", "SUV", "I (2026/27)", None, "GWM",
    ["PHEV", "HEV"], "announced", "Due in Germany end of 2026 together with the Jolion Max (autonotizen, Oct 2025)",
    [GWM_AUTONOTIZEN], notes=""))
B(m("Haval", GWM, "Jolion Max", "Jolion Max", "c-suv", "SUV", "I (2026/27)", None, "GWM",
    ["HEV", "petrol"], "announced", "Due in Germany end of 2026 (autonotizen, Oct 2025)",
    [GWM_AUTONOTIZEN], notes=""))
B(m("Deepal", CHG, "S07 PHEV", "S07 (PHEV/REEV)", "d-suv", "SUV", "I (2026)", 4750, "Changan EPA1",
    ["PHEV"], "announced", "Plug-in/range-extender versions of S05 and S07 due in Italy/Spain in 2026 (electrive, Dec 2025) - powertrain additions, not new tiles",
    [CHANGAN_ELECTRIVE_DEC], notes="Informational."))
B(m("Avatr", CHG, "Avatr (brand)", "Avatr 11 / 12", "e-suv", "SUV / saloon", "(2027)", None, "Changan CHN",
    ["BEV"], "announced", "Changan plans to launch Avatr and Nevo in Europe by 2027 (electrive, Dec 2025); no European sales yet",
    [CHANGAN_ELECTRIVE_AVATR], notes="Brand not yet on sale; listed for completeness."))
B(m("Xiaomi", "Xiaomi", "SU7 / YU7", "SU7 / YU7", "e-car", "saloon / SUV", "(2027)", None, "Xiaomi Modena",
    ["BEV"], "announced", "Xiaomi confirmed Europe as first export market with a 2027 launch (SU7, YU7); nothing on sale in 2026",
    [XIAOMI_MOTOR1], notes="Brand not yet on sale."))

# ============================ DISCONTINUED ===================================
DISCONTINUED = [
    {"brand": "MG", "model": "MG5 Electric (estate)", "note": "Removed from the German configurator by May 2025; no successor", "source": MG_INSIDEEVS_DROP},
    {"brand": "MG", "model": "ZS EV", "note": "Dropped 2025, replaced by the MGS5 EV", "source": MG_INSIDEEVS_DROP},
    {"brand": "MG", "model": "Marvel R", "note": "Removed from the German configurator by May 2025", "source": MG_INSIDEEVS_DROP},
    {"brand": "Maxus", "model": "Euniq 6 (SUV) / Euniq 5 (MPV)", "note": "No longer in the UK range (Oct 2026); Euniq 6 still appears on carwow.de without offers - treated as discontinued", "source": MAXUS_UK},
    {"brand": "BYD", "model": "Han", "note": "Not in the UK or German line-ups any more (Oct 2026)", "source": BYD_DE_OVERVIEW},
    {"brand": "BYD", "model": "Seal U (BEV)", "note": "Only the Seal U DM-i remains on UK/DE lists (2026)", "source": BYD_UK},
    {"brand": "Ora", "model": "Ora 03 (UK)", "note": "carwow UK shows 'currently unavailable new' (Oct 2026) - UK runout; still offered in Germany", "source": GWM_CARWOW_UK},
    {"brand": "NIO", "model": "ET5 saloon / ET7 / EL7 (NL)", "note": "Sold out in the Netherlands, no factory orders anywhere in Europe (Aug 2026) - whole NIO range is runout", "source": NIO_EV_STATUS},
    {"brand": "XPeng", "model": "P7 (first generation)", "note": "Replaced in Europe by the P7+ (not on xpeng.com/de, Oct 2026)", "source": XPENG_DE},
    {"brand": "Aiways", "model": "U5 / U6", "note": "Company collapsed 2023-24; no official European sales in 2026 (not re-verified - search budget)", "source": None},
    {"brand": "Voyah", "model": "Free / Dream (Norway)", "note": "Both marked 'Utgatt modell' (discontinued) on voyah.no (Oct 2026); both still listed with prices by the Dutch importer and the Free by the Swiss importer", "source": VOYAH_NO},
]

SOURCES = [
    {"url": MG_CH, "what": "MG Switzerland model overview (15 models, Oct 2026)"},
    {"url": MG_EU, "what": "MG Europe model overview (Oct 2026)"},
    {"url": MG4U_ELECTRIVE, "what": "MG4 EV Urban = 2nd-gen MG4, Austria launch, old MG4 continues (Feb 2026)"},
    {"url": MG4U_ECOMENTO, "what": "New MG4 UK-first, old MG4 continues (Jan 2026)"},
    {"url": MGS6_INSIDEEVS, "what": "MGS6 EV data, DE order start 16 Mar 2026"},
    {"url": MGS9_AMS, "what": "MGS9 PHEV = Roewe RX9, 4,983 mm, 7 seats"},
    {"url": IM_ELECTRIVE, "what": "MG IM5/IM6 markets and dates (Jun 2026)"},
    {"url": MG_INSIDEEVS_DROP, "what": "MG5/ZS EV/Marvel R dropped (May 2025)"},
    {"url": MAXUS_UK, "what": "Maxus UK range (10 models, Oct 2026)"},
    {"url": MAXUS_CARWOW_DE, "what": "Maxus Germany listings"},
    {"url": BYD_UK, "what": "BYD UK model navigation (14 models, Oct 2026)"},
    {"url": BYD_DE_OVERVIEW, "what": "BYD Germany line-up and prices (Sept 2026)"},
    {"url": BYD_CH_MONEYCAB, "what": "BYD Switzerland: Dolphin Surf/Atto 2 launch, Seal/Sealion 7/Seal U on sale (May 2025)"},
    {"url": CARIFY_CH, "what": "Chinese brands/models available in Switzerland (Apr 2026)"},
    {"url": DENZA_DE, "what": "Denza Germany site: Z9GT, D9, Z, BAO 5 (Oct 2026)"},
    {"url": DENZA_CHINAEVHOME, "what": "Denza European launch, Z9GT pre-orders in 7 markets (Apr 2026)"},
    {"url": DENZA_AUTOEVO_UK, "what": "Denza Z9 GT UK prices, orders open (Jul 2026)"},
    {"url": OJ_CH, "what": "Omoda & Jaecoo Switzerland: coming soon (Oct 2026)"},
    {"url": OMODA_UK, "what": "Omoda UK range (Oct 2026)"},
    {"url": JAECOO_UK, "what": "Jaecoo UK range (Oct 2026)"},
    {"url": OJ_CARGURUS, "what": "Omoda/Jaecoo UK models overview (Sept 2026)"},
    {"url": CHERY_CARWOW_UK, "what": "Chery UK: Tiggo 4/7/8/9 prices (Oct 2026)"},
    {"url": CHERY_ELECTRIVE_DE, "what": "Chery Germany launch 1H 2027, Chery Q (Aug 2026)"},
    {"url": CHERY_HYE, "what": "Chery Group 2026 Europe plan (Nov 2025)"},
    {"url": LEPAS_AUTOIT, "what": "Lepas L8 European expansion Q3/Q4 2026 (Aug 2026)"},
    {"url": LEPAS_FLEET, "what": "Lepas/iCaur/Exlantix Italy timing (Nov 2025)"},
    {"url": GWM_GOLEASY, "what": "GWM Germany model list via leasing portal (Oct 2026)"},
    {"url": GWM_AUTOHAUS, "what": "Haval Jolion Pro / H6 Germany prices (Mar 2026)"},
    {"url": GWM_AUTONOTIZEN, "what": "GWM 2026 plans: Ora 5, Haval H6/H7/Jolion (Oct 2025)"},
    {"url": GWM_CARWOW_UK, "what": "GWM UK: Haval Jolion Pro on sale, Ora 03 unavailable new (Oct 2026)"},
    {"url": XPENG_DE, "what": "XPeng Germany line-up: L03, G6, G9, G9L, P7+, X9 (Oct 2026)"},
    {"url": XPENG_GOINGELECTRIC, "what": "XPeng Germany prices/availability"},
    {"url": XPENG_FLEETWORLD, "what": "XPeng UK 2026 roadmap (G6 update, X9)"},
    {"url": NIO_DE, "what": "NIO Germany model list (Oct 2026)"},
    {"url": NIO_EV_STATUS, "what": "NIO Europe runout/restructuring (Aug 2026)"},
    {"url": FIREFLY_ELECTRIVE, "what": "Firefly first European deliveries (Aug 2025)"},
    {"url": FIREFLY_CNC, "what": "Firefly markets Dec 2025"},
    {"url": ONVO_DELAY, "what": "Onvo Europe delayed to 2028-29 (Sept 2026)"},
    {"url": CHANGAN_ELECTRIVE_DEC, "what": "Deepal S05/S07 in DE/IT/ES/DK (Dec 2025)"},
    {"url": CHANGAN_ELECTRIVE_AVATR, "what": "Changan Europe plan, Avatr/Nevo by 2027 (Dec 2025)"},
    {"url": VOYAH_GASGOO_COURAGE, "what": "Voyah Courage launch NO/SE/FI (Oct 2024)"},
    {"url": VOYAH_GASGOO_EU, "what": "Voyah importers NL/CH/Nordics (Jul 2023)"},
    {"url": HONGQI_NO, "what": "Hongqi Norway: EHS5 new, in stock (Oct 2026)"},
    {"url": HONGQI_GASGOO, "what": "Hongqi Norway agreement, EH7/EHS7 (Jun 2024)"},
    {"url": HONGQI_FLEETWORLD, "what": "Hongqi EH7/EHS7 European prices (Oct 2024)"},
    {"url": XIAOMI_MOTOR1, "what": "Xiaomi Europe launch 2027 (Aug 2025)"},
    {"url": HONGQI_NO_BILER, "what": "Hongqi Norway line-up with prices: EHS5, EH7, EHS7, E-HS9 (Oct 2026)"},
    {"url": HONGQI_EHS5_SPEC, "what": "Hongqi EHS5 dimensions"},
    {"url": DENZA_DE_D9, "what": "Denza D9 Germany pre-order, configurator coming soon (Oct 2026)"},
    {"url": DENZA_DE_BAO5, "what": "Denza BAO 5 Germany page, no EU type approval yet (Oct 2026)"},
    {"url": XPENG_DE_L03, "what": "XPeng L03 Germany: 4,650 mm, from EUR 35,600, configurator (Oct 2026)"},
    {"url": XPENG_DE_G9L, "what": "XPeng G9L Germany: 5,120 mm, from EUR 85,600, configurator (Oct 2026)"},
    {"url": VOYAH_NO, "what": "Voyah Norway: Courage on sale, Free/Dream discontinued (Oct 2026)"},
    {"url": BYD_UK_TI7, "what": "BYD Ti 7 DM-p UK page, orders from Oct 2026"},
    {"url": BYD_UK_DOLPHIN_G, "what": "BYD Dolphin G DM-i UK page, orders from 7 Oct 2026"},
    {"url": BYD_UK_SEALION5, "what": "BYD Sealion 5 DM-i UK page"},
    {"url": BYD_UK_SHARK, "what": "BYD Shark DMO UK page, orders from 7 Oct 2026"},
    {"url": WIKI_JAECOO7, "what": "Jaecoo 7 = Chery Tansuo 06 (twin source)"},
    {"url": WIKI_TIGGO9, "what": "Tiggo 9 exported as Jaecoo J8/8, T1X platform (twin source)"},
    {"url": WIKI_EZ60, "what": "Mazda EZ-60 / CX-6e heavily based on Deepal S07, EPA1 (twin source)"},
    {"url": FIREFLY_EVPOWERED, "what": "Firefly UK debut 2026, RHD in production (Nov 2025)"},
    {"url": "https://commercial-vehicles.mgmotor.eu/model/iev12", "what": "MG iEV12 = 12 m electric bus (out of scope)"},
    {"url": WIKI_TAI7, "what": "Fangchengbao Ti7 = BYD Ti7 global model (EREV, 5 seats)"},
    {"url": WIKI_OMODA7, "what": "Omoda 7 on stretched Omoda C5 platform, = Chery Tiggo 7L (twin source)"},
    {"url": WIKI_OMODA5, "what": "Omoda 5 names/facelifts, = Tiggo 5x High Energy in China"},
    {"url": WIKI_TIGGO7, "what": "Tiggo 7 II rebadges: Ebro S700, DR 6.0, Sportequipe 6; Europe since Jun 2025 (twin source)"},
    {"url": WIKI_TIGGO8, "what": "Tiggo 8 rebadged as Ebro S800; Lepas L8 = 2nd-gen derivative, 4,670 mm (twin source)"},
    {"url": WIKI_JAECOO5, "what": "Jaecoo 5 UK deliveries from Oct 2025; no platform info"},
    {"url": VOYAH_NL, "what": "Voyah Netherlands: Courage/Free/Dream prices, Dongfeng Box and Mhero I listed (Oct 2026)"},
    {"url": VOYAH_NL_BOX, "what": "Dongfeng Box NL page (42.3 kWh, 310 km)"},
    {"url": VOYAH_NL_MHERO, "what": "Mhero I NL page (142.7 kWh, showroom cars)"},
    {"url": LEPAS_UK_DEALER, "what": "lepas.co.uk = 'Bassetts Lepas' UK dealer page (Oct 2026)"},
    {"url": "https://www.carsized.com/en-us/trending/car-comparisons/", "what": "carsized slug conventions (make-model-year-body)"},
]

def apply_carsized(entries):
    for e in entries:
        key = e["brand"] + " " + e["model"]
        c = CARSIZED.get(key)
        if c:
            e["carsized_slug"] = c.get("slug")
            e["carsized_side"] = c.get("side")
            e["carsized_front"] = c.get("front")
            e["carsized_years"] = c.get("years")
        elif e["carsized_slug"] is None:
            e["notes"] = (e["notes"] + " " if e["notes"] else "") + "carsized: " + (c.get("note") if c else NOT_FETCHED)

apply_carsized(MODELS)
apply_carsized(ANNOUNCED)

doc = {"agent": "china-other (SAIC/BYD/Chery/GWM/XPeng/NIO/Changan/Dongfeng/FAW/Xiaomi + minor Chinese brands)",
       "checked_on": "2026-10-21", "models": MODELS, "announced": ANNOUNCED,
       "discontinued_recently": DISCONTINUED, "sources": SOURCES}
with open(OUT, "w") as f:
    json.dump(doc, f, indent=1, ensure_ascii=False)
print("wrote", OUT, len(MODELS), "models,", len(ANNOUNCED), "announced")
