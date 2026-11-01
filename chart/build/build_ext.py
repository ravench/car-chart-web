#!/usr/bin/env python3
"""Turn the harvested pictures selected in SEL into carsized-style cut-outs (xfer/in/<id>-side.png, <id>-front.png)
and write ext/manifest.json (provenance shown in the detail panel).
Usage: python3 build_ext.py [ids...]   (no ids = all)"""
import sys, os, json, glob
import numpy as np
from PIL import Image
from collections import deque
from urllib.parse import urlparse
from scipy import ndimage

ZW = 'https://www.zigwheels.ae/new-cars/'
NIS = 'https://de.nissan.ch/fahrzeuge/neuwagen/'
MB = 'https://www.mercedes-benz.ch/'
MORG_SS = 'https://media.morgan-motor.com/images/supersport-studio/'
# id -> view -> (src, treat, mirror, notes, page[, licence])   treat: a=auto w=white-flood r=rembg d=drawing(flood, keep lines)  'c:x0,y0,x1,y1|<treat>' crops first
SEL = {
 # ---- v1.15 (2026-11-01): side views for every tile without a proper picture (Raven) ----
 'ligier-myli': {'side': ('v115/A/myli-profile-green', 'R', False, "Ligier Group press photo '2023_Ligier_Myli_ADV-Photo_R.EBEL-Velvet-Green_Profile' (media.ligier.fr, 2560 px): studio side view of the Myli R.EBEL in Velvet Green, light-grey studio backdrop removed; the Myli LAB/MAX update of January 2026 changed trim details only", 'https://media.ligier.fr/')},
 'ligier-pulse-4': {'side': ('v115/A/pulse4-forgeon-profile', 'c:0,0.111,1,1|R', False, "Ligier Group press photo 'Pulse-4-L3KS-Forgeon-Social-Profile-2' (media.ligier.fr, 2560 px): true side view of the Pulse 4 L3KS with the Forgeon box body, taken in front of a factory; background removed", 'https://media.ligier.fr/')},
 'maxus-edeliver-3': {'side': ('v115/D/maxus-edeliver-3-side-clean', 'a', False, "Maxus studio side view (transparent PNG, 1920 px) from the Norwegian importer site maxus.no (RSA), short-wheelbase eDeliver 3, white; the soft ground shadow removed", 'https://maxus.no/')},
 'maxus-edeliver-7': {'side': ('v115/D/maxus-edeliver-7-side-clean', 'a', False, "Maxus studio side view (transparent PNG, 1920 px) from the Norwegian importer site maxus.no (RSA), eDeliver 7 L1 body, white; the soft ground shadow removed", 'https://maxus.no/')},
 'maxus-edeliver-9': {'side': ('v115/D/maxus-edeliver-9-side-clean', 'a', False, "Maxus studio side view (transparent PNG, 1920 px) from the Norwegian importer site maxus.no (RSA), eDeliver 9 L2H2 body, silver; the soft ground shadow removed", 'https://maxus.no/')},
 'byd-ti-7': {'side': ('v115/H/byd-ti-7-side', 'R', True, "BYD's own studio photo from the byd.com/uk Ti 7 page ('three-part silhouette' section, 972 px wide, Jade Green, UK car with European badges): true side view, studio gradient background removed, mirrored to face left", 'https://www.byd.com/uk/hybrid-cars/ti-7')},
 'xpeng-l03': {'side': ('v115/F/xpeng-l03-side-cfg-white', 'R', False, "XPeng's own configurator render (store.xpeng.com/de L03 configurator, exterior view 2 of 3, transparent PNG 2048 px, car about 1640 px): true side view of the European L03 in white with a black roof, facing left; the opaque ground shadow of the render removed", 'https://store.xpeng.com/de/configurator/L03')},
 'xpeng-g9l': {'side': ('v115/F/xpeng-g9l-side-cfg-white', 'R', False, "XPeng's own configurator render (store.xpeng.com/de G9L configurator, exterior view 2 of 3, transparent PNG 2048 px, car about 1500 px): true side view in silver-white, facing left; the opaque ground shadow of the render removed", 'https://store.xpeng.com/de/configurator/G9L')},
 'denza-z9-gt': {'side': ('v115/F/denza-z9-gt-side-studio', 'R', False, "Denza's own studio picture from the European Z9 GT page (denza.com/de, 'eu-model-introduction' exterior image 2, 2400 px): near-true side view in teal, facing left; light-grey studio background and floor reflection removed", 'https://www.denza.com/de/z9gt')},
 'denza-d9': {'side': ('v115/F/denza-d9-side', 'R', False, "Denza's own studio picture from the European D9 page (denza.com/de, exterior image 2, 2400 px): side view of the European D9 in dark blue, facing left, studio gradient background removed; the camera sits a few degrees towards the front, so the edge of the grille shows (near-side view)", 'https://www.denza.com/de/d9'), 'front': ('v115/F/denza-d9-front-eu', 'R', False, "Denza's own studio front view from the same European D9 page (exterior image 1), background removed", 'https://www.denza.com/de/d9')},
 'chatenet-ch46': {'side': ('v115/J/chatenet-ch46-side-automoto2019', 'R|e:0,0.945,1,1|e:0.245,0.895,0.755,1|e:0,0.86,0.095,1|e:0.905,0.85,1,1', False, "third-party catalogue photo (automoto.it CH46 listing of 2019, 2000 px, soft/upscaled): true side view in white with a black roof, facing left, grey studio background removed; the body is the current CH46 shell (Chatenet's own site has only lifestyle and three-quarter pictures) - placeholder until a brand-own side view is found", 'https://www.automoto.it/catalogo/chatenet/ch46')},
 'wey-wey-03': {'side': ('v115/K/wey-wey-03-side-press66', 'R', False, "GWM Germany press photo 'GWM-WEY-03_-66' (presse.gwm-motor.de, June 2024 set, 2560 px, used at 1536 px): true side view of the white Wey 03 on a lake shore, facing left, background removed", 'https://presse.gwm-motor.de/')},
 'mhero-mhero-i': {'side': ('v115/K/mhero-mhero-i-side-zigwheels', 'R', False, "third-party catalogue photo (zigwheels.ae, 'Side View (Left)', 930 px): true side view of a black Mhero I in a dark architectural scene, facing left, background removed; UAE listing of the same body as the European electric car - placeholder until a brand-own side view is found", 'https://www.zigwheels.ae/newcars/Mhero/1')},
 'mitsubishi-l200': {'side': ('v115/I/mitsubishi-l200-side-clubcab-clean', 'a', True, "Mitsubishi Australia's own configurator render of the Triton (= L200, same sixth-generation body) in Impulse Blue (mitsubishi-motors.com.au, transparent PNG 1920 px): true side view, mirrored to face left, soft ground shadow removed; it shows the Club Cab body (shorter cab, longer tub) because no Double Cab pick-up side render was found - the European Double Cab shares the nose, wheelbase and overall length", 'https://www.mitsubishi-motors.com.au/vehicles/triton.html')},
 'iveco-daily': {'side': ('v115/G/iveco-daily-side-edaily-cab', 'R', False, "Iveco UK's own profile render 'eDaily_cab_MY24_profilo_SW_LHD' (iveco.com/uk eDaily page, 1048 px, vehicle about 890 px): near-true side view of the MY24 eDaily single chassis cab with a dropside body, facing left, white background removed; no side view of the Daily van exists on Iveco's sites, so the cab (shared with the diesel Daily) stands in for the family - placeholder", 'https://www.iveco.com/uk/')},
 'ligier-js60': {'side': ('v115/L/ligier-js60-side-press89', 'R', False, "Ligier Group press photo 'NOUVELLE-JS60-ULTIMATE-89' (media.ligier.fr, September 2026 shoot of the new JS60 Ultimate in blue, 2560 px): near-true side view in a courtyard, facing left, background removed", 'https://media.ligier.fr/communique-de-presse/nouvelle-ligier-js60-la-ligier-qui-voit-plus-grand/')},
 'wey-wey-05': {'side': ('v115/L/wey-wey-05-side-mocha26-white', 'R', False, "Wey's own cut-out render of the Chinese New Mocha Hi4 (2026 model year, black; wey.com model carousel, 1948 px): true side view facing left, ground shadow removed; the Mocha is the Chinese name of the Wey 05 / Coffee 01 and shares its body shell (4,875 mm against 4,871 mm), but bumpers and wheels of the European car differ - GWM's European sites have no side view of the Wey 05", 'https://www.wey.com/mocca.html')},
 'smart-2': {'side': ('v115/L/smart-2-side-earlyorder', 'R', False, "smart's own early-order banner of the production #2 in red (de.smart.com #2 page, 4096 px original used at 2048 px): near-true side view (slight wide-angle lens) in a red studio set, facing left, background removed", 'https://de.smart.com/de/models/hashtag-two/')},
 'maxus-t90-ev': {'side': ('v115/M/maxus-t90-ev-side-cn-white', 'R', False, "SAIC Maxus's own cut-out side view (transparent PNG, 750 px, truck about 610 px - small) from the Chinese T90 EV model page (saicmaxus.com/car/t90ev.shtml, sold there as the Xingji EV; same T90 body as the European T90 EV and the LDV eT60): true side view of the white double cab facing left, the opaque ground shadow of the render removed", 'https://www.saicmaxus.com/car/t90ev.shtml')},
 'maxus-mifa-7': {'side': ('v115/G/maxus-mifa-7-side-clean', 'a', False, "SAIC Maxus's own cut-out side view (transparent PNG, 750 px - small) from the Chinese Maxus site (saicmaxus.com, Mifa 7 = 大家7, same body), own transparency used; wheels may differ from the European trim", 'https://www.saicmaxus.com/car/mifa7.shtml')},
 'voyah-dream': {'side': ('v115/B/voyah-dream-cn-side', 'R', False, "Voyah's own photo from the Chinese Dreamer (= Dream) model page (voyah.com.cn, 3840 px, used at 2304 px): true side view in a dark architectural scene, background removed", 'https://www.voyah.com.cn/dreamer.html')},
 'lepas-l8': {'side': ('v115/B/lepas-l8-side', 'R', True, "Lepas's own studio side view from the brand's international site (lepasinternational.com, 742 px - small), grey studio with floor reflection removed, mirrored to face left", 'https://www.lepasinternational.com/models/lepasl8/lepasl8phev/index.shtml')},
 'farizon-sv': {'side': ('v115/B/farizon-sv-l1h1-side-clean', 'a', False, "Farizon's own cut-out side view (transparent PNG, 4096 px, used at 2048 px) of the SV L1H1 from the UK importer site farizonauto.co.uk (Jameel Motors); soft ground shadow removed", 'https://farizonauto.co.uk/our-range/sv-range/product-detail')},
 'farizon-v7e': {'side': ('v115/B/farizon-v7e-side-clean', 'a', False, "Farizon's own cut-out side view (transparent PNG, 878 px) of the V7E from the UK configurator on farizonauto.co.uk (Jameel Motors); soft ground shadow removed", 'https://farizonauto.co.uk/our-range/farizon-v7e')},
 'fiat-ulysse': {'side': ('v114/ulysse-cfg-a4-clean', 'a', False, "Fiat's own configurator render (lb.assets.fiat.com vl-picker-service, angle 4 = true side view, 3840 px) of the 2024-facelift Ulysse Combi M in white; white background flood-filled and the ground shadow removed", 'https://www.fiat.it/omni/configuratore.pro')},
 'dr-dr-7': {'side': ('v114/dr7-modellino', 'a', False, "DR's own 'modellino' cut-out (dr7-modellino-dealer.png, 1200 px, uploaded February 2026) of the DR 7 Collection, which drautomobiles.com lists as DR 8 Collection since October 2026; true side view, the render's own transparency used", 'https://drautomobiles.com/dr-8-collection/')},
 'mitsubishi-eclipse-cross': {'side': ('v114/eclipse-cross-press-004', 'R', True, 'Mitsubishi Motors Europe press photo Eclipse-Cross_004 (premiere press kit, 17 September 2025; static, seaside terrace), true side view, background removed, mirrored to face left', 'https://media.mitsubishi-motors-europe.com/mitsubishi-motors-europe-electrifies-its-line-up-with-the-premiereof-the-advanced-all-electric-eclipse-cross-compact-suv/')},
 'iveco-ejolly': {'side': ('v114/ejolly-schouten-side', 'a', False, "Iveco studio side view of the eJolly (silver, charging flap open) as published by the Dutch Iveco dealer Schouten (768 px copy; the Iveco press original could not be reached) - true side view facing left, own transparency used; placeholder (dealer copy) until a larger brand-own file is found", 'https://www.iveco-schouten.nl/')},
 # ---- v1.13 (2026-11-01): poster name tiles ----
 'abarth-600e': {'side': ('v113/abarth-600e-2-whr', 'c:0.03,0.33,0.98,0.92|R', False, 'press photo of the 2025 Abarth 600e Competizione (static, graffiti wall), true side view, background removed', 'https://www.media.stellantis.com/de-de/abarth/media-library/press-images/636714'),
                 'front': ('v113/abarth-600e-3-whr', 'R', False, 'press photo (static), straight front, background removed', 'https://www.media.stellantis.com/de-de/abarth/media-library/press-images/636714')},
 'ebro-s400': {'side': ('v113/ebro-s400-cotas', 'c:0,0,0.63,1|a|e:0,0,1,0.035|e:0,0,0.05,1|e:0,0.86,1,1', False, 'official dimension graphic (transparent render) from the ebroauto.com spec page, true side view, dimension lines and markers blanked', 'https://www.ebroauto.com/s400-ficha-tecnica'),
               'front': ('v113/ebro-s400-cotas', 'c:0.645,0,1,1|a|e:0,0.86,1,1|e:0,0,1,0.035', False, 'official dimension graphic (render), straight front', 'https://www.ebroauto.com/s400-ficha-tecnica')},
 'ebro-s700': {'side': ('v113/ebro-s700-cotas', 'c:0,0,0.63,1|a|e:0,0,1,0.035|e:0,0,0.05,1|e:0,0.86,1,1', False, 'official dimension graphic (transparent render) from the ebroauto.com spec page, true side view, dimension lines and markers blanked', 'https://www.ebroauto.com/modelos/s700-phev/especificaciones'),
               'front': ('v113/ebro-s700-cotas', 'c:0.645,0,1,1|a|e:0,0.86,1,1|e:0,0,1,0.035', False, 'official dimension graphic (render), straight front', 'https://www.ebroauto.com/modelos/s700-phev/especificaciones')},
 'ebro-s900': {'side': ('v113/ebro-s900-cotas', 'c:0,0,0.63,1|a|e:0,0,1,0.035|e:0,0,0.05,1|e:0,0.86,1,1', False, 'official dimension graphic (transparent render) from the ebroauto.com spec page, true side view, dimension lines and markers blanked', 'https://www.ebroauto.com/modelos/s900-phev/especificaciones'),
               'front': ('v113/ebro-s900-cotas', 'c:0.645,0,1,1|a|e:0,0.86,1,1|e:0,0,1,0.035', False, 'official dimension graphic (render), straight front', 'https://www.ebroauto.com/modelos/s900-phev/especificaciones')},
 'volkswagen-crafter': {'side': ('v113/crafter-trendline-side', 'c:0.02,0.26,0.99,0.89|R', False, 'studio render of the Crafter panel van Trendline from the UK trim gallery (volkswagen-vans.co.uk), true side view facing left, background removed', 'https://www.volkswagen-vans.co.uk/en/new-vehicles/crafter-panel-van.html')},
 'iveco-esuperjolly': {'side': ('v113/iveco-esuperjolly-clean', 'a', True, 'dimension render from the eSuperJolly brochure (iveco.com/uk, page 11): dimension labels and lines removed from the PDF before rendering, the ghosted longer/higher body variant cropped away, true side view mirrored to face left', 'https://www.iveco.com/uk/-/media/IVECOdotcom/Content/Products/eJolly/brochure/brochure_eSuperJolly_en.pdf')},
 'opel-rocks': {'side': ('v113/opel-rocks-clean', 'a', True, 'small hero render (576 px) of the 2025 Rocks from opel.de, true side view, mirrored to face left; the render\'s own transparency used and its ground shadow removed (no larger brand-own side view exists: the Stellantis press set, the online-store configurator and the price list only have 3/4 or elevated views)', 'https://www.opel.de/fahrzeuge/rocks/uebersicht.html')},

 'aston-martin-db12': {'side': ('misc2/aston-martin-db12-side', 'r', False, 'press photo, background removed', None),
                       'front': ('zig5/db12-0-FullFrontViewofDB12', 'r', False, 'scene photo, background removed', ZW + 'aston-martin/db12/images')},
 'aston-martin-valhalla': {'side': ('zigwheels/aston-martin-valhalla-side', 'r', False, 'scene photo, background removed', ZW + 'aston-martin/valhalla/images'),
                           'front': ('zigwheels/aston-martin-valhalla-front', 'r', False, 'scene photo, background removed', ZW + 'aston-martin/valhalla/images')},
 'audi-a2-e-tron': {'side': ('batch1/audi-a2-e-tron-side', 'r', True, 'near-side view, mirrored to face left, background removed', None)},
 'audi-q9': {'side': ('batch1/audi-q9-side', 'r', False, 'scene photo, near-side view (slight angle), background removed', None), 'front': ('batch1/audi-q9-front', 'r', False, 'scene photo, background removed', None)},
 'bmw-i3': {'side': ('bmw/bmw-i3-stage', 'r', True, 'studio photo, background removed, mirrored', 'https://www.bmw.com/'), 'front': ('bmw/bmw-i3-front', 'r', False, 'scene photo, background removed', 'https://www.bmw.com/')},
 'bmw-ix4': {'side': ('bmw/bmw-ix4-rear-view', 'r', True, 'scene photo seen slightly from the rear, background removed, mirrored', 'https://www.bmw.com/'), 'front': ('bmw/bmw-ix4-front-view', 'r', False, 'scene photo, background removed', 'https://www.bmw.com/')},
 'byd-sealion-5': {'side': ('v115/H/byd-sealion-5-side-clean', 'a', False, "BYD's own cut-out side view (transparent, 2816 px) from the byd.com/uk Sealion 5 DM-i page (colour picker image 2 = side, Atlantis Blue); soft ground shadow removed; body checked against the byd.ch dimension drawing (European Sealion 5)", 'https://www.byd.com/uk/hybrid-cars/sealion-5')},
 'byd-shark': {'side': ('v115/H/byd-shark-side', 'R', False, "BYD's own studio side view from the byd.com/uk Shark page (colour picker image 2 = side, Atlantis Blue, 2816 px), white background and soft shadow removed", 'https://www.byd.com/uk/hybrid-cars/shark'), 'front': ('zig3/shark6-0-FullFrontViewofShark6', 'r', False, 'scene photo, background removed', ZW + 'byd/shark-6/images')},
 'bugatti-tourbillon': {'side': ('zigwheels/bugatti-tourbillon-side', 'r', True, 'dark studio photo, background removed, mirrored', ZW + 'bugatti/tourbillon/images'), 'front': ('zigwheels/bugatti-tourbillon-front', 'r', False, 'studio photo, background removed', ZW + 'bugatti/tourbillon/images')},
 'chery-tiggo-4': {'side': ('china/chery-tiggo-4-side', 'a', False, None, None)},
 'chery-tiggo-9': {'side': ('china/chery-tiggo-9-side', 'a', False, None, None)},
 'citroen-jumper': {'side': ('citroen/citroen-jumper-bcc576', 'a', False, None, 'https://www.citroen.ch/'), 'front': ('citroen/citroen-jumper-hero', 'r', False, 'scene photo, background removed', 'https://www.citroen.ch/')},
 'dr-dr-1-0-ev': {'side': ('v115/I/dr-dr-1-0-ev-side-clean', 'a', False, "DR's own 'ModelloCut' cut-out render of the DR 1.0 EV (drautomobiles.com media library, DR_ModelloCut_DR1.png, September 2023, 975 px, white car): true side view, own transparency used; the model page itself was removed from drautomobiles.com in spring 2026", 'https://drautomobiles.com/'), 'front': ('ebro/dr-1-motor', 'r', False, 'driving photo, near-front view (slight angle), background removed', 'https://drautomobiles.com/')},
 'dr-dr-3': {'side': ('dr/dr-3-side', 'a', False, 'near-side view', 'https://drautomobiles.com/')},
 'dr-dr-5': {'side': ('dr/dr-5-hev', 'a', False, 'DR 5 HEV', 'https://drautomobiles.com/')},
 'dr-dr-pk8': {'side': ('dr/dr-pk8-side2', 'a', False, 'near-side view, small source image', 'https://drautomobiles.com/')},
 'ds-n-7': {'side': ('dsn7td/dsn7td-0200-whr', 'r', False, 'press photo (media test drive), near-side view seen slightly from the rear, background removed', 'https://www.media.stellantis.com/em-en/ds/media-library/press-images/655422')},
 'dacia-spring': {'side': ('spring2026/spring-057-l', 'r', False, 'studio press photo of the 2026 Spring, background removed', 'https://media.dacia.com/new-dacia-spring-100-per-cent-electric-100-per-cent-dacia/?lang=eng'), 'front': ('spring2026/spring-058-l', 'r', False, 'studio press photo, background removed', 'https://media.dacia.com/new-dacia-spring-100-per-cent-electric-100-per-cent-dacia/?lang=eng')},
 'fiat-doblo': {'side': ('doblo2022/doblo-08-whr', 'r', True, 'press photo of the 2022 Doblo van (K9 before the 2024 facelift, same body), background removed, mirrored', 'https://www.media.stellantis.com/uk-en/fiat-professional/media-library/press-images/506266'), 'front': ('doblo2022/doblo-09-whr', 'R', False, 'press photo of the 2022 Doblo van, background removed (haze above the roof cleaned)', 'https://www.media.stellantis.com/uk-en/fiat-professional/media-library/press-images/506266')},
 'dacia-striker': {'side': ('dacia/striker-xl2', 'a', True, 'mirrored', 'https://www.dacia.ch/'), 'front': ('renault/dacia-striker-front', 'c:0.35,0.12,0.79,0.64|D|e:0.35,0.90,0.65,1.0', False, 'outline drawing from the dimension sheet', 'https://www.dacia.ch/')},
 'deepal-s05': {'side': ('china/deepal-s05-alt1-side', 'r', False, 'background removed', None)},
 'deepal-s07': {'side': ('china/deepal-s07-alt1-side', 'r', False, 'background removed', None)},
 'dongfeng-box': {'side': ('china/dongfeng-box-alt2-side', 'r', False, 'background removed', None)},
 'ebro-s800': {'side': ('ebro/ebro-s800-3', 'R', False, 'scene photo, background removed', None)},
 'ferrari-amalfi': {'side': ('batch1/ferrari-amalfi-side', 'r', False, 'scene photo, background removed', None), 'front': ('batch1/ferrari-amalfi-front', 'r', False, 'scene photo, background removed', None)},
 'ferrari-f80': {'side': ('f80/f80-16', 'r', False, 'press photo, background removed', 'https://www.ferrari.com/'), 'front': ('f80/f80-12', 'r', False, 'press photo, background removed', 'https://www.ferrari.com/')},
 'fiat-ducato': {'side': ('fiat/ducato-s2-a1', 'r', False, 'configurator render, near-side view (slight angle), background removed', 'https://www.fiat.ch/')},
 'fiat-scudo': {'side': ('fiat2/scudo-thermic-s2-a1', 'r', False, 'configurator render, background removed', 'https://www.fiat.ch/')},
 'fiat-qubo-l': {'side': ('fiat3/fiat-qubo-l-s2', 'r', False, 'configurator render, background removed', 'https://www.fiat.ch/')},
 'firefly-firefly': {'side': ('firefly/firefly-side', 'r', False, 'studio photo, background removed', None), 'front': ('firefly/firefly-front', 'r', False, 'studio photo, background removed', None)},
 'ford-transit-city': {'side': ('ford3/tcity-spin-1-ee5eb3fb', 'a', True, 'configurator render, mirrored', 'https://www.ford.de/'), 'front': ('ford3/tcity-spin-8-4eb0e654', 'a', False, 'configurator render', 'https://www.ford.de/')},
 'ford-transit': {'side': ('ford2/transit-car1', 'a', True, 'E-Transit (same body), mirrored', 'https://www.ford.de/nutzfahrzeuge-modelle/ford-e-transit'), 'front': ('ford5/transit-uk-front-blue', 'c:0.29,0,1,1|R', False, 'scene photo, background removed', 'https://www.ford.co.uk/vans-and-pickups/transit')},
 'geely-e2': {'side': ('geely/geely-ex2-7', 'a', False, None, None), 'front': ('geely/geely-ex2-1', 'a', False, None, None)},
 'geely-starray-em-i': {'side': ('v115/B/starray-emi-f18-white', 'w', False, "Geely's own 360-degree viewer render (geely.de, assets.geelyauto.eu frame 18 of 24 = exact side view, 2100 px) of the Starray EM-i in white on a white studio background", 'https://www.geely.de/'), 'front': ('v115/B/starray-emi-f00-white', 'w', False, "Geely's own 360-degree viewer render (geely.de, frame 00 = straight front), white studio background", 'https://www.geely.de/')},
 'honda-super-n': {'side': ('misc2/honda-super-n-side', 'a', False, None, None), 'front': ('misc2/honda-super-n-front', 'a', False, None, None)},
 'hongqi-eh7': {'side': ('china/hongqi-eh7-side', 'a', False, None, None)},
 'hongqi-ehs5': {'side': ('china/hongqi-ehs5-side', 'a', False, None, None), 'front': ('china/hongqi-ehs5-front', 'r', False, 'background removed', None)},
 'hongqi-ehs7': {'side': ('china/hongqi-ehs7-side', 'a', False, None, None), 'front': ('china/hongqi-ehs7-front', 'r', False, 'background removed', None)},
 'hyundai-ioniq-3': {'side': ('hyundai2/ioniq3-unveil-04', 'r', False, 'studio photo, background removed', 'https://www.hyundai.news/'), 'front': ('hyundai2/ioniq3-unveil-08', 'r', False, 'studio photo, background removed', 'https://www.hyundai.news/')},
 'ineos-quartermaster': {'side': ('batch1/ineos-quartermaster-side', 'a', False, None, None)},
 'jaecoo-jaecoo-5': {'side': ('omoda/jaecoo-5-side', 'a', True, 'mirrored', None), 'front': ('omoda/jaecoo-5-front', 'a', False, None, None)},
 'kgm-actyon': {'side': ('kgm2/kgm-actyon-sideR', 'a', True, 'mirrored', None)},
 'kgm-musso': {'side': ('kgm2/kgm-musso-sideR', 'a', True, 'mirrored', None)},
 'kgm-musso-rhino': {'side': ('kgm2/kgm-musso-rhino-sideR', 'a', True, 'mirrored', None)},
 'koenigsegg-cc850': {'side': ('zigwheels/koenigsegg-cc850-side', 'a', True, 'studio photo, mirrored', ZW + 'koenigsegg/cc850/images'), 'front': ('zigwheels/koenigsegg-cc850-front', 'a', False, 'studio photo', ZW + 'koenigsegg/cc850/images')},
 'koenigsegg-gemera': {'side': ('gemera2/gemera-evo-08', 'r', False, 'press photo (car small in frame), background removed', 'https://www.evo.co.uk/koenigsegg/gemera/202315/koenigsegg-gemera-pictures')},
 'koenigsegg-jesko': {'side': ('koenigsegg/jesko-04-KoenigseggJeskoAbs', 'R', False, 'press photo on a runway, background removed', 'https://www.koenigsegg.com/'), 'front': ('koenigsegg/jesko-12-KoenigseggJeskoAbs', 'R', False, 'press photo, background removed', 'https://www.koenigsegg.com/')},
 'levc-tx': {'front': ('levc/levc-tx-exterior-pack', 'r', False, 'scene photo, slight angle, background removed', 'https://www.levc.com/')},
 'lancia-gamma': {'side': ('lancia/gamma-mhev-dim', 'c:0.07,0.28,0.47,0.80|w', False, 'render cut from the manufacturer dimension sheet', 'https://www.lancia.it/')},
 'leapmotor-b03x': {'side': ('misc2/leapmotor-b03x-side', 'a', False, None, None)},
 'lexus-lm': {'side': ('misc2/lexus-lm-side', 'r', False, 'dark studio photo, background removed', None), 'front': ('misc2/lexus-lm-front', 'r', False, 'dark studio photo, background removed', None)},
 'lotus-evija': {'side': ('lotus/evija-6-2f57b496', 'r', False, 'press photo, background removed', 'https://www.lotuscars.com/'), 'front': ('zigwheels/lotus-evija-front', 'r', False, 'background removed', ZW + 'lotus/evija/images')},
 'man-tge': {'side': ('man/man-tge-kastenwagen-navi', 'a', False, None, 'https://www.man.eu/ch/de/van/')},
 'mazda-mazda2-hybrid': {'side': ('mazda/m2h-cgi-01', 'r', False, 'white car, background removed', 'https://www.mazda.ch/'), 'front': ('mazda/m2h-cgi-10', 'a', False, None, 'https://www.mazda.ch/')},
 'mclaren-750s': {'side': ('zigwheels/mclaren-750s-side', 'r', False, 'scene photo, background removed', ZW + 'mclaren/750s/images'), 'front': ('zigwheels/mclaren-750s-front', 'r', False, 'scene photo, background removed', ZW + 'mclaren/750s/images')},
 'mclaren-gts': {'side': ('zigwheels/mclaren-gts-side', 'r', False, 'scene photo, background removed', ZW + 'mclaren/gts/images'), 'front': ('zigwheels/mclaren-gts-front', 'r', False, 'scene photo, background removed', ZW + 'mclaren/gts/images')},
 'mclaren-w1': {'side': ('zigwheels/mclaren-w1-side', 'R', True, 'background removed, mirrored', ZW + 'mclaren/w1/images')},
 'mercedes-benz-amg-gt-suv': {'side': ('mercedes/mercedes-benz-amg-gt-suv-BE270', 'a', False, 'configurator image', MB), 'front': ('mercedes/mercedes-benz-amg-gt-suv-BE000', 'a', False, 'configurator image', MB)},
 'mercedes-benz-vle': {'side': ('mercedes/mercedes-benz-vle-BE270', 'a', False, 'configurator image', MB), 'front': ('mercedes/mercedes-benz-vle-BE000', 'a', False, 'configurator image', MB)},
 'mercedes-benz-sprinter': {'side': ('mercedes/sprinter-907645-BE270-1600', 'a', False, 'configurator image', MB), 'front': ('mercedes/sprinter-907645-BE000-1600', 'a', False, 'configurator image', MB)},
 'mitsubishi-grandis': {'side': ('mitsubishi/grandis-g00', 'a', False, None, 'https://www.mitsubishi-motors.ch/')},
 'morgan-plus-four': {'side': ('v115/N/morgan-plus-four-side-cfg', 'R', True, "Morgan's own 3D configurator (configure.morgan-motor.com, Plus Four, manual, default dark blue), real-time render captured at 2380 px with the camera turned to a true side view (slightly elevated, so the seat tops show); grey studio background and floor shadow removed, mirrored to face left", 'https://configure.morgan-motor.com/plusfour/'), 'front': ('morgan/morgan-plus-four-side', 'r', False, 'studio photo, near-front view (slight angle), background removed', 'https://media.morgan-motor.com/images/new-plus-four-images/')},
 'morgan-supersport': {'side': ('morgan/morgan-supersport-side', 'r', False, 'studio photo, background removed', MORG_SS), 'front': ('morgan2/ss-sportStudio008', 'r', False, 'dark studio photo, background removed', MORG_SS)},
 'nissan-townstar-kombi': {'side': ('nissan/nissan-townstar-kombi-side', 'a', True, 'mirrored', NIS + 'townstar-kombi.html'), 'front': ('nissan/nissan-townstar-kombi-front', 'c:0.5,0,1,1|d', False, 'outline drawing (technical data page)', NIS + 'townstar-kombi.html')},
 'nissan-primastar-kombi': {'side': ('v115/L/nissan-primastar-kombi-side-eutile', 'R', True, "Nissan's own packshot of the Primastar Kombi L1 (nissan.de vehicle-page asset 'Primastar-combi_de.jpg', 600 px - small): true side view on white, mirrored to face left; replaces the v1.13 dimension drawing", 'https://www.nissan.de/fahrzeuge/neuwagen/primastar/primastar-kombi.html'), 'front': ('nissan/nissan-primastar-van-mid-front', 'd', False, 'dimension drawing of the Primastar van (identical front end)', NIS + 'primastar/technische-daten.html')},
 'nissan-townstar-van-small': {'side': ('v115/K/nissan-townstar-van-small-side-37afe1', 'R', True, "Nissan Europe press photo from the 2021 Townstar reveal gallery (europe.nissannews.com, photo 6, public 928 px copy, van about 580 px): true side view of the white L1 van in a city scene, background removed, mirrored to face left; small source", 'https://europe.nissannews.com/'), 'front': ('nissan/nissan-townstar-van-small-front', 'a', False, None, NIS + 'townstar.html')},
 'nissan-primastar-van-mid': {'side': ('v115/L/bonus-nissan-primastar-van-mid-side-eutile', 'R', True, "Nissan's own packshot of the Primastar panel van L1H1 (nissan.de vehicle-page asset 'Primastar fourgon.jpg', 600 px - small): true side view on white, mirrored to face left; replaces the v1.13 dimension drawing (a 2021 press photo of the van was the alternative)", 'https://www.nissan.de/fahrzeuge/neuwagen/primastar.html'), 'front': ('nissan/nissan-primastar-van-mid-front', 'd', False, 'dimension drawing (technical data page)', NIS + 'primastar/technische-daten.html')},
 'nissan-interstar': {'side': ('nissan/nissan-interstar-side', 'r', True, 'white van, background removed, mirrored', NIS + 'interstar.html'), 'front': ('batch1/nissan-interstar-front', 'r', False, 'background removed', None)},
 'omoda-omoda-7': {'side': ('omoda/omoda-7-side', 'a', True, 'mirrored', None)},
 'omoda-omoda-9': {'side': ('omoda/omoda-9-side', 'a', True, 'mirrored', None)},
 'opel-movano': {'side': ('opel2/opel-movano-bev-side576', 'a', False, None, 'https://www.opel.ch/')},
 'ora-ora-5': {'side': ('ora5full/ora5full-044', 'r', False, 'event photo (CarBase.my watermark), background removed', 'https://www.carbase.my/great-wall/ora-5/ec15s/exterior/211735'), 'front': ('ora5full/ora5full-005', 'r', False, 'event photo (CarBase.my watermark), background removed', 'https://www.carbase.my/great-wall/ora-5/ec15s/exterior/211735')},
 'pagani-utopia': {'side': ('pagani/pagani-utopia-side', 'r', False, 'Utopia Roadster, studio photo, background removed', None), 'front': ('pagani/pagani-utopia-front', 'r', False, 'studio photo, background removed', None)},
 'peugeot-boxer': {'side': ('peugeot/peugeot-boxer-sideview', 'a', True, 'mirrored', 'https://www.peugeot.ch/')},
 'piaggio-porter-np6': {'front': ('piaggio/np6-veicolo', 'a', False, None, 'https://commercial.piaggio.com/')},
 'polestar-5': {'side': ('polestar/ps4966m', 'r', False, 'studio photo, background removed', 'https://media.polestar.com/')},
 'renault-master': {'side': ('misc2/renault-master-side-xl-white', 'R', True, 'Renault configurator cut-out (renault.ch), ground shadow removed, mirrored', 'https://www.renault.ch/')},
 'renault-trucks-master': {'side': ('v115/G/renault-trucks-master-side', 'R', True, "Renault Trucks press photo 'Renault Trucks E-Tech Master (4)' (renault-trucks.com press set of November 2023, 5000 px, used at 3000 px): true side view of the grey E-Tech Master IV L3H2 panel van on white, mirrored to face left", 'https://www.renault-trucks.com/en/renault-trucks-light-commercial-vehicules'), 'front': ('rtrucks/rtm-p042754', 'c:0.33,0,0.67,1|r', False, 'centre van cropped from a three-van press photo, background removed', 'https://www.renault-trucks.ch/')},
 'rimac-nevera': {'side': ('misc2/rimac-nevera-side', 'r', False, 'background removed', None)},
 'subaru-uncharted': {'side': ('subaru/uncharted-006', 'a', False, '360° view frame', 'https://www.subaru.ch/'), 'front': ('subaru/uncharted-000', 'a', False, '360° view frame', 'https://www.subaru.ch/')},
 'subaru-e-outback': {'side': ('subaru/eoutback-006', 'a', False, '360° view frame', 'https://www.subaru.ch/'), 'front': ('subaru/eoutback-000', 'a', False, '360° view frame', 'https://www.subaru.ch/')},
 'suzuki-e-vitara': {'side': ('batch1/suzuki-e-vitara-side', 'r', True, 'studio photo, mirrored to face left, background removed', None), 'front': ('batch1/suzuki-e-vitara-front', 'r', False, 'studio photo, background removed', None)},
 'toyota-c-hr-plus': {'side': ('batch1/toyota-c-hr-plus-front', 'r', False, 'scene photo, background removed', None), 'front': ('batch1/toyota-c-hr-plus-side', 'r', False, 'scene photo, background removed', None)},
 'toyota-bz4x-touring': {'side': ('batch1/bzthi-27', 'a', False, '360° view frame', 'https://www.toyota.ch/'), 'front': ('batch1/bzthi-00', 'a', False, '360° view frame', 'https://www.toyota.ch/')},
 'toyota-proace-max': {'side': ('batch1/pmxhi-27', 'a', False, '360° view frame', 'https://www.toyota.ch/'), 'front': ('batch1/pmxhi-00', 'a', False, '360° view frame', 'https://www.toyota.ch/')},
 'vinfast-vf-6': {'side': ('vinfast/vinfast-vf6-3', 'a', False, None, None), 'front': ('vinfast/vinfast-vf6-4', 'a', False, None, None)},
 'volkswagen-id-cross': {'side': ('vw/vwn-514', 'r', False, 'studio photo, near-side view, background removed', 'https://www.volkswagen-newsroom.com/')},
 'volkswagen-id-tiguan': {'side': ('vw2/idt-side-b64', 'r', False, 'scene photo, background removed', 'https://www.volkswagen-newsroom.com/')},
 'voyah-courage': {'side': ('china/voyah-courage-side', 'r', False, 'studio photo, background removed', None)},
 'xpeng-x9': {'side': ('china/xpeng-x9-alt1-side', 'a', False, 'near-side view (slight angle)', None)},
 'zeekr-9x': {'side': ('v114/zeekr9x-eu-side-galaxy', 'R', False, "Zeekr's own studio side view from the zeekr.eu 9X page (exterior colour section: Onyx Black, Galaxy wheels, 2880 px), light-grey studio background removed", 'https://www.zeekr.eu/models/9x'),
              'front': ('zig4/zeekr9x-0-FullFrontViewof9X', 'r', False, 'scene photo, background removed', ZW + 'zeekr/9x/images')},
 'skoda-peaq': {'side': ('skoda/peaq-d1', 'a', False, 'brand render, faces left as published (v1.14a: the earlier mirroring made it face right)', 'https://www.skoda-auto.com/'), 'front': ('skoda/peaq-g1', 'r', False, 'scene photo, background removed', 'https://www.skoda-auto.com/')},

}

RES = {}
for f in glob.glob('ext/results/*.json'):
    for r in json.load(open(f, encoding='utf-8')): RES[r['id']] = r

def res_page(mid, view):
    r = RES.get(mid) or {}
    v = r.get(view)
    if isinstance(v, dict) and (v.get('page') or v.get('url')): return v.get('page') or v.get('url')
    for a in r.get('alternates') or []:
        if a.get('page'): return a['page']
    v = r.get('side' if view == 'front' else 'front')
    if isinstance(v, dict) and (v.get('page') or v.get('url')): return v.get('page') or v.get('url')
    return None

def source_text(page):
    host = urlparse(page or '').netloc.replace('www.', '')
    if not host: return 'manufacturer website', 'manufacturer copyright'
    if 'zigwheels' in host: return 'zigwheels.ae (third-party catalogue photo)', 'copyright of the manufacturer / zigwheels; third-party placeholder'
    if 'automoto.it' in host: return 'automoto.it (third-party catalogue photo)', 'copyright of the manufacturer / automoto.it; third-party placeholder'
    if 'carbase' in host: return 'CarBase.my (third-party event photo)', 'copyright CarBase.my; watermarked third-party placeholder'
    if 'evo.co.uk' in host: return 'evo.co.uk (Koenigsegg press photo)', 'copyright Koenigsegg; press photo via evo.co.uk'
    if 'motor.es' in host: return 'trade press (motor.es), EBRO press photo', 'EBRO press photo republished by motor.es; third-party placeholder'
    if 'autocarindia' in host: return 'autocarindia.com (third-party gallery photo)', 'copyright Autocar India / Ferrari; third-party placeholder'
    if 'evspecs' in host: return 'evspecs.org (third-party spec site photo)', 'copyright of the manufacturer / evspecs.org; third-party placeholder'
    if 'electrive' in host: return 'electrive.com', 'copyright of the manufacturer; third-party placeholder'
    if any(k in host for k in ('media.', 'press', 'newsroom', 'news.', 'mynewsdesk')): return f'manufacturer press site ({host})', 'manufacturer copyright; press/editorial use'
    return f'manufacturer website ({host})', 'manufacturer copyright; editorial use'

def find_src(src):
    p = f'ext/unpacked/{src}.webp'
    if os.path.exists(p): return p
    hits = glob.glob(f'ext/unpacked/*/{os.path.basename(src)}.webp')
    if not hits: raise FileNotFoundError(src)
    return hits[0]

def flood(im, TOL=26.0):
    a = np.asarray(im.convert('RGBA')).astype(np.int16); h, w = a.shape[:2]
    rgb = a[:, :, :3]
    border = np.concatenate([rgb[0, :], rgb[-1, :], rgb[:, 0], rgb[:, -1]])
    med = np.median(border, axis=0)
    bg = np.zeros((h, w), dtype=bool); seen = np.zeros((h, w), dtype=bool); q = deque()
    for y in range(h):
        for x in (0, w - 1):
            if not seen[y, x]: seen[y, x] = True; q.append((y, x))
    for x in range(w):
        for y in (0, h - 1):
            if not seen[y, x]: seen[y, x] = True; q.append((y, x))
    gtol = 2.5 * TOL
    while q:
        y, x = q.popleft(); p = rgb[y, x]
        if np.abs(p - med).max() > gtol: continue
        bg[y, x] = True
        for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= ny < h and 0 <= nx < w and not seen[ny, nx]:
                if np.abs(rgb[ny, nx] - p).max() <= TOL: seen[ny, nx] = True; q.append((ny, nx))
    out = a.copy(); out[:, :, 3] = np.where(bg, 0, 255)
    return Image.fromarray(out.astype(np.uint8), 'RGBA'), {'mode': 'flood', 'border': [int(v) for v in med], 'bg_frac': round(float(bg.mean()), 3)}

_sess = None
def rembg_cut(im):
    global _sess
    from rembg import remove, new_session
    if _sess is None: _sess = new_session('isnet-general-use')
    out = remove(im.convert('RGB'), session=_sess)
    return out.convert('RGBA'), {'mode': 'rembg'}

def keep_main(im, frac=0.03):
    """Drop small disconnected blobs (noise, dimension letters); keep components >= frac of the largest."""
    a = np.asarray(im); alpha = a[:, :, 3]
    lab, n = ndimage.label(alpha > 100)
    if n <= 1: return im
    sizes = ndimage.sum(np.ones_like(alpha), lab, range(1, n + 1))
    keep = {i + 1 for i, s in enumerate(sizes) if s >= frac * sizes.max()}
    mask = np.isin(lab, list(keep))
    out = a.copy(); out[:, :, 3] = np.where(mask, alpha, 0)
    return Image.fromarray(out, 'RGBA')

def process(src, treat):
    im = Image.open(find_src(src)); im.load()
    crop = None; erase = []
    parts = treat.split('|'); treat = [q for q in parts if not q.startswith(('c:', 'e:'))][0]
    for q in parts:
        if q.startswith('c:'):
            spec = q[2:]; x0, y0, x1, y1 = [float(v) for v in spec.split(',')]
            im = im.crop((int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height))); crop = spec
        elif q.startswith('e:'): erase.append([float(v) for v in q[2:].split(',')])
    if im.mode in ('RGBA', 'LA') and (np.asarray(im.convert('RGBA'))[:, :, 3] < 250).mean() > 0.02 and treat not in ('r', 'R'):
        out, info = im.convert('RGBA'), {'mode': 'alpha'}
    elif treat == 'r': out, info = rembg_cut(im)
    elif treat == 'R':  # rembg, then drop faint and thin leftovers (poles, lines, haze)
        out, info = rembg_cut(im); a = np.asarray(out).copy(); alpha = a[:, :, 3]
        hard = ndimage.binary_opening(alpha > 110, structure=np.ones((9, 9)))
        hard = ndimage.binary_dilation(hard, structure=np.ones((5, 5)))
        a[:, :, 3] = np.where(hard, alpha, 0); out = Image.fromarray(a, 'RGBA'); info['mode'] = 'rembg+clean'
    elif treat in ('w', 'd'): out, info = flood(im)
    elif treat == 'D':  # drawing: flood, then drop orange dimension lines and text
        out, info = flood(im); a = np.asarray(out).copy(); r, g, b = a[:, :, 0].astype(int), a[:, :, 1].astype(int), a[:, :, 2].astype(int)
        orange = (r > 140) & (g > 50) & (g < 210) & (b < 140) & (r - b > 55)
        orange = ndimage.binary_dilation(orange, structure=np.ones((5, 5)))
        a[:, :, 3] = np.where(orange, 0, a[:, :, 3]); out = Image.fromarray(a, 'RGBA'); info['mode'] = 'flood-drawing'
    else:  # auto
        out, info = flood(im)
        if min(info['border']) < 232 or info['bg_frac'] < 0.25: out, info = rembg_cut(im); info['auto'] = 'rembg'
    if treat not in ('d', 'D'): out = keep_main(out)
    for x0, y0, x1, y1 in erase:  # blank rectangles (relative to the cropped image)
        a = np.asarray(out).copy(); a[int(y0 * a.shape[0]):int(y1 * a.shape[0]), int(x0 * a.shape[1]):int(x1 * a.shape[1]), 3] = 0; out = Image.fromarray(a, 'RGBA')
    bbox = out.getchannel('A').getbbox()
    if bbox:
        l, t, r, b = bbox; mx, my = int((r - l) * 0.02) + 2, int((b - t) * 0.02) + 2
        out = out.crop((max(0, l - mx), max(0, t - my), min(out.width, r + mx), min(out.height, b + my)))
    info['crop'] = crop; info['size'] = out.size
    return out, info

# v1.11 (2026-11-01): new-body pictures replacing old-generation carsized entries, plus quadricycle makers
BMW2GC = 'https://www.bmw.co.uk/en/all-models/2-series/gran-coupe/bmw-2-series-gran-coupe-technical-data.html'
NEXO = 'https://www.hyundai.com/de/de/modelle/nexo.html'
AMG4D = 'https://www.mercedes-benz.ch/de/passengercars/models/coupe/amg-gt-4-door/overview.html'
HILUX = 'https://de.toyota.ch/neuwagen-kaufen/hilux/build'
ACROSS = 'https://www.suzuki.ch/de/modelle/across'
SELTOS = 'https://www.kia.com/de/modelle/seltos/technische-daten/'
SEL.update({
 'bmw-2-series-gran-coupe': {'side': ('v111/bmw-2-series-gran-coupe-0', 'a', False, 'configurator render (BMW CoSy) of the 2025 2 Series Gran Coupe (F74)', BMW2GC), 'front': ('v111/bmw-2-series-gran-coupe-1', 'a', False, 'configurator render (BMW CoSy)', BMW2GC)},
 'bmw-x5': {'side': ('v111/bmw-x5-0', 'a', False, 'configurator render (BMW CoSy) of the 2026 X5 (G65)', 'https://www.bmw.ch/de/bmw-neuwagen/x/suv/bmw-x5-technische-daten.html'), 'front': ('v111/bmw-x5-3', 'R', False, 'scene photo of the iX5 (same G65 body), background removed', 'https://www.bmw.de/de/neufahrzeuge/x/suv/bmw-ix5.html')},
 'hyundai-nexo': {'side': ('v111/hyundai-nexo-0', 'r', False, 'studio product shot of the 2025 Nexo, near-side view, background removed', NEXO), 'front': ('v111/hyundai-nexo-1', 'r', False, 'studio product shot, background removed', NEXO)},
 'mercedes-benz-amg-gt-4-door-coupe': {'side': ('v111/mercedes-benz-amg-gt-4-door-coupe-0', 'a', False, 'configurator image (BE270)', AMG4D), 'front': ('v111/mercedes-benz-amg-gt-4-door-coupe-1', 'a', False, 'configurator image (BE000)', AMG4D)},
 'toyota-hilux': {'side': ('v111/toyota-hilux-0', 'a', False, 'configurator render (Toyota CCIS frame 27) of the 2026 Hilux', HILUX), 'front': ('v111/toyota-hilux-1', 'a', False, 'configurator render (Toyota CCIS frame 00)', HILUX)},
 'suzuki-across': {'side': ('v111/suzuki-across-1', 'a', False, 'configurator gallery render of the 2026 Across, near-side view (slight angle from above)', ACROSS), 'front': ('v111/suzuki-across-11', 'a', False, 'configurator gallery render', ACROSS)},
 'kia-seltos': {'side': ('v111/kia-seltos-0', 'c:0.14,0.06,0.88,0.52|w', False, 'render cut from the manufacturer dimension sheet (2027 Seltos)', SELTOS), 'front': ('v111/kia-seltos-1', 'c:0.27,0.06,0.73,0.75|w', False, 'render cut from the manufacturer dimension sheet', SELTOS)},
 'mini-cooper-cabrio': {'side': ('v111/mini-cooper-cabrio-0', 'c:0.03,0.18,0.93,0.70|w', False, 'render cut from the manufacturer dimension sheet (F67, roof down)', 'https://www.mini.co.uk/en_GB/home/range/mini-cooper-convertible/technical-data.html')},
 'aixam-d-truck-e-truck': {'side': ('v111/aixam-d-truck-e-truck-0', 'a', True, 'product cut-out of the D-Truck pickup (plateau ridelles), mirrored', 'https://www.aixam-pro.com/fr/d-truck/plateau-ridelles')},
 'dr-dr-6': {'side': ('v111/dr-dr-6-0', 'a', False, 'product cut-out from the DR website (2026 DR 6), tightly cropped', 'https://drautomobiles.com/dr-6-collection/')},
 'aixam-easy': {'side': ('v111/aixam-easy-cfgside', 'r', True, '3D configurator render (Easy Access), grey studio background removed, mirrored', 'https://www.aixam.com/en/aixam-configurator')},
 'aixam-crossover': {'side': ('v111/aixam-crossover-cfg-2', 'r', True, '3D configurator render (Crossover Pack), grey studio background removed, mirrored', 'https://www.aixam.com/en/aixam-configurator')},
 'aixam-e-scouty': {'side': ('v111/aixam-e-scouty-cfg40-5', 'r', True, '3D configurator render (Mega e-Scouty Evo), grey studio background removed, mirrored', 'https://www.aixam.com/en/aixam-configurator')},
 'aixam-city': {'side': ('v111/aixam-city-cfg1-02', 'r', True, '3D configurator render (City Pack), grey studio background removed, mirrored', 'https://www.aixam.com/en/aixam-configurator')},
 'aixam-coupe': {'side': ('v111/aixam-coupe-cfg16-02', 'r', True, '3D configurator render (Coupe Sport), grey studio background removed, mirrored', 'https://www.aixam.com/en/aixam-configurator')},
 'lexus-es': {'side': ('v111/lexus-es-f27', 'a', False, 'configurator render (Lexus CCIS frame 27) of the 2026 ES', 'https://de.lexus.ch/modelle/es/build'), 'front': ('v111/lexus-es-f0', 'a', False, 'configurator render (Lexus CCIS frame 0)', 'https://de.lexus.ch/modelle/es/build')},
 'jeep-compass': {'side': ('v111/jeep-compass-16-full', 'R', True, 'press photo of the 2026 Compass (quarry scene), true side view, mirrored to face left, background removed', 'https://www.media.stellantis.com/em-en/jeep/media-library/press-images/637335'), 'front': ('v111/jeep-compass-11-full', 'R', False, 'press photo (driving), straight front, background removed', 'https://www.media.stellantis.com/em-en/jeep/media-library/press-images/637335')},
 'lancia-ypsilon': {'side': ('v111/lancia-ypsilon-h19-full', 'c:0.20,0.30,0.70,0.64|R', False, 'press photo of the 2025 Ypsilon HF (driving), near-side view seen slightly from the rear, background removed', 'https://www.media.stellantis.com/em-en/lancia/media-library/press-images/623277')},
 'casalini-650': {'side': ('v115/J/casalini-650-side-starter-white', 'R|e:0,0.925,1,1|e:0,0.80,0.05,1|e:0.955,0.80,1,1|e:0.26,0.87,0.73,1', True, "Casalini's own studio photo of the 650 Starter in white (casalini.eu media library, CASALINI-starter-dx.jpg, September 2026, 2048 px): true side view, white background removed, mirrored to face left", 'https://casalini.eu/'), 'front': ('v111/casalini-650-2', 'r', False, 'studio product shot of the 650 Starter, background removed', 'https://www.casalini.eu/')},
})

if __name__ == '__main__':
    ids = sys.argv[1:] or list(SEL)
    os.makedirs('xfer/in', exist_ok=True); os.makedirs('ext/out', exist_ok=True)
    man = json.load(open('ext/manifest.json')) if os.path.exists('ext/manifest.json') else {}
    report = {}
    for mid in ids:
        for view, spec in SEL[mid].items():
            src, treat, mirror, notes, page = spec[:5]
            try:
                out, info = process(src, treat)
                if mirror: out = out.transpose(Image.FLIP_LEFT_RIGHT)
                out.save(f'xfer/in/{mid}-{view}.png'); out.save(f'ext/out/{mid}-{view}.png')
                page = page or res_page(mid, view)
                stext, lic = source_text(page)
                if len(spec) > 5 and spec[5]: lic = spec[5]
                man.setdefault(mid, {})[view] = {'url': None, 'page': page, 'source': stext, 'licence': lic, 'notes': notes, 'angle': view,
                                                 'src': src, 'treatment': info.get('mode') + ('/' + info['auto'] if info.get('auto') else ''), 'mirrored': bool(mirror), 'harvested': True}
                report[f'{mid}-{view}'] = info; print('ok', mid, view, info.get('mode'), info.get('auto', ''), info['size'])
            except Exception as ex:
                report[f'{mid}-{view}'] = {'error': str(ex)}; print('FAILED', mid, view, ex)
    json.dump(man, open('ext/manifest.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(report, open('ext/out/_report.json', 'w'), indent=1)
    print(len(man), 'models in manifest')
