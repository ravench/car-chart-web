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
 'aston-martin-db12': {'side': ('misc2/aston-martin-db12-side', 'r', False, 'press photo, background removed', None),
                       'front': ('zig5/db12-0-FullFrontViewofDB12', 'r', False, 'scene photo, background removed', ZW + 'aston-martin/db12/images')},
 'aston-martin-valhalla': {'side': ('zigwheels/aston-martin-valhalla-side', 'r', False, 'scene photo, background removed', ZW + 'aston-martin/valhalla/images'),
                           'front': ('zigwheels/aston-martin-valhalla-front', 'r', False, 'scene photo, background removed', ZW + 'aston-martin/valhalla/images')},
 'audi-a2-e-tron': {'side': ('batch1/audi-a2-e-tron-side', 'r', False, 'near-side view, background removed', None)},
 'audi-q9': {'side': ('batch1/audi-q9-side', 'r', False, 'scene photo, near-side view (slight angle), background removed', None), 'front': ('batch1/audi-q9-front', 'r', False, 'scene photo, background removed', None)},
 'bmw-i3': {'side': ('bmw/bmw-i3-stage', 'r', True, 'studio photo, background removed, mirrored', 'https://www.bmw.com/'), 'front': ('bmw/bmw-i3-front', 'r', False, 'scene photo, background removed', 'https://www.bmw.com/')},
 'bmw-ix4': {'side': ('bmw/bmw-ix4-rear-view', 'r', True, 'scene photo seen slightly from the rear, background removed, mirrored', 'https://www.bmw.com/'), 'front': ('bmw/bmw-ix4-front-view', 'r', False, 'scene photo, background removed', 'https://www.bmw.com/')},
 'byd-sealion-5': {'side': ('china/byd-sealion-5-side', 'c:0.33,0,0.67,1|d', False, 'dimension drawing (side view cropped from the three-view figure)', None)},
 'byd-shark': {'front': ('zig3/shark6-0-FullFrontViewofShark6', 'r', False, 'scene photo, background removed', ZW + 'byd/shark-6/images')},
 'bugatti-tourbillon': {'side': ('zigwheels/bugatti-tourbillon-side', 'r', True, 'dark studio photo, background removed, mirrored', ZW + 'bugatti/tourbillon/images'), 'front': ('zigwheels/bugatti-tourbillon-front', 'r', False, 'studio photo, background removed', ZW + 'bugatti/tourbillon/images')},
 'chery-tiggo-4': {'side': ('china/chery-tiggo-4-side', 'a', False, None, None)},
 'chery-tiggo-9': {'side': ('china/chery-tiggo-9-side', 'a', False, None, None)},
 'citroen-jumper': {'side': ('citroen/citroen-jumper-bcc576', 'a', False, None, 'https://www.citroen.ch/'), 'front': ('citroen/citroen-jumper-hero', 'r', False, 'scene photo, background removed', 'https://www.citroen.ch/')},
 'dr-dr-1-0-ev': {'front': ('ebro/dr-1-motor', 'r', False, 'driving photo, near-front view (slight angle), background removed', 'https://drautomobiles.com/')},
 'dr-dr-3': {'side': ('dr/dr-3-side', 'a', False, 'near-side view', 'https://drautomobiles.com/')},
 'dr-dr-5': {'side': ('dr/dr-5-hev', 'a', False, 'DR 5 HEV', 'https://drautomobiles.com/')},
 'dr-dr-pk8': {'side': ('dr/dr-pk8-side2', 'a', False, 'near-side view, small source image', 'https://drautomobiles.com/')},
 'ds-n-7': {'side': ('ds2/dsn7-3112476', 'c:0.28,0,1,1|r', True, 'press photo, background removed, mirrored', None)},
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
 'geely-starray-em-i': {'front': ('zig2/starray-front', 'r', False, 'dark studio photo, background removed', ZW + 'geely/starray/images')},
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
 'morgan-plus-four': {'front': ('morgan/morgan-plus-four-side', 'r', False, 'studio photo, near-front view (slight angle), background removed', 'https://media.morgan-motor.com/images/new-plus-four-images/')},
 'morgan-supersport': {'side': ('morgan/morgan-supersport-side', 'r', False, 'studio photo, background removed', MORG_SS), 'front': ('morgan2/ss-sportStudio008', 'r', False, 'dark studio photo, background removed', MORG_SS)},
 'nissan-townstar-kombi': {'side': ('nissan/nissan-townstar-kombi-side', 'a', True, 'mirrored', NIS + 'townstar-kombi.html'), 'front': ('nissan/nissan-townstar-kombi-front', 'c:0.5,0,1,1|d', False, 'outline drawing (technical data page)', NIS + 'townstar-kombi.html')},
 'nissan-primastar-kombi': {'front': ('nissan/nissan-primastar-van-mid-front', 'd', False, 'dimension drawing of the Primastar van (identical front end)', NIS + 'primastar/technische-daten.html')},
 'nissan-townstar-van-small': {'side': ('nissan/nissan-townstar-van-small-side', 'd', True, 'outline drawing (technical data page), mirrored', NIS + 'townstar.html'), 'front': ('nissan/nissan-townstar-van-small-front', 'a', False, None, NIS + 'townstar.html')},
 'nissan-primastar-van-mid': {'side': ('nissan/nissan-primastar-van-mid-side', 'd', False, 'dimension drawing (technical data page)', NIS + 'primastar/technische-daten.html'), 'front': ('nissan/nissan-primastar-van-mid-front', 'd', False, 'dimension drawing (technical data page)', NIS + 'primastar/technische-daten.html')},
 'nissan-interstar': {'side': ('nissan/nissan-interstar-side', 'r', True, 'white van, background removed, mirrored', NIS + 'interstar.html'), 'front': ('batch1/nissan-interstar-front', 'r', False, 'background removed', None)},
 'omoda-omoda-7': {'side': ('omoda/omoda-7-side', 'a', True, 'mirrored', None)},
 'omoda-omoda-9': {'side': ('omoda/omoda-9-side', 'a', True, 'mirrored', None)},
 'opel-movano': {'side': ('opel2/opel-movano-bev-side576', 'a', False, None, 'https://www.opel.ch/')},
 'ora-ora-5': {'side': ('ora5full/ora5full-044', 'r', False, 'event photo (CarBase.my watermark), background removed', 'https://www.carbase.my/great-wall/ora-5/ec15s/exterior/211735'), 'front': ('ora5full/ora5full-005', 'r', False, 'event photo (CarBase.my watermark), background removed', 'https://www.carbase.my/great-wall/ora-5/ec15s/exterior/211735')},
 'pagani-utopia': {'side': ('pagani/pagani-utopia-side', 'r', False, 'Utopia Roadster, studio photo, background removed', None), 'front': ('pagani/pagani-utopia-front', 'r', False, 'studio photo, background removed', None)},
 'peugeot-boxer': {'side': ('peugeot/peugeot-boxer-sideview', 'a', True, 'mirrored', 'https://www.peugeot.ch/')},
 'piaggio-porter-np6': {'front': ('piaggio/np6-veicolo', 'a', False, None, 'https://commercial.piaggio.com/')},
 'polestar-5': {'side': ('polestar/ps4966m', 'r', False, 'studio photo, background removed', 'https://media.polestar.com/')},
 'renault-master': {'side': ('misc2/renault-master-side-xl', 'a', True, 'mirrored', 'https://www.renault.ch/')},
 'renault-trucks-master': {'front': ('rtrucks/rtm-p042754', 'c:0.33,0,0.67,1|r', False, 'centre van cropped from a three-van press photo, background removed', 'https://www.renault-trucks.ch/')},
 'rimac-nevera': {'side': ('misc2/rimac-nevera-side', 'r', False, 'background removed', None)},
 'subaru-uncharted': {'side': ('subaru/uncharted-006', 'a', False, '360° view frame', 'https://www.subaru.ch/'), 'front': ('subaru/uncharted-000', 'a', False, '360° view frame', 'https://www.subaru.ch/')},
 'subaru-e-outback': {'side': ('subaru/eoutback-006', 'a', False, '360° view frame', 'https://www.subaru.ch/'), 'front': ('subaru/eoutback-000', 'a', False, '360° view frame', 'https://www.subaru.ch/')},
 'suzuki-e-vitara': {'side': ('batch1/suzuki-e-vitara-side', 'r', False, 'studio photo, background removed', None), 'front': ('batch1/suzuki-e-vitara-front', 'r', False, 'studio photo, background removed', None)},
 'toyota-c-hr-plus': {'side': ('batch1/toyota-c-hr-plus-front', 'r', False, 'scene photo, background removed', None), 'front': ('batch1/toyota-c-hr-plus-side', 'r', False, 'scene photo, background removed', None)},
 'toyota-bz4x-touring': {'side': ('batch1/bzthi-27', 'a', False, '360° view frame', 'https://www.toyota.ch/'), 'front': ('batch1/bzthi-00', 'a', False, '360° view frame', 'https://www.toyota.ch/')},
 'toyota-proace-max': {'side': ('batch1/pmxhi-27', 'a', False, '360° view frame', 'https://www.toyota.ch/'), 'front': ('batch1/pmxhi-00', 'a', False, '360° view frame', 'https://www.toyota.ch/')},
 'vinfast-vf-6': {'side': ('vinfast/vinfast-vf6-3', 'a', False, None, None), 'front': ('vinfast/vinfast-vf6-4', 'a', False, None, None)},
 'volkswagen-id-cross': {'side': ('vw/vwn-514', 'r', False, 'studio photo, near-side view, background removed', 'https://www.volkswagen-newsroom.com/')},
 'volkswagen-id-tiguan': {'side': ('vw2/idt-side-b64', 'r', False, 'scene photo, background removed', 'https://www.volkswagen-newsroom.com/')},
 'voyah-courage': {'side': ('china/voyah-courage-side', 'r', False, 'studio photo, background removed', None)},
 'xpeng-x9': {'side': ('china/xpeng-x9-alt1-side', 'a', False, 'near-side view (slight angle)', None)},
 'zeekr-9x': {'front': ('zig4/zeekr9x-0-FullFrontViewof9X', 'r', False, 'scene photo, background removed', ZW + 'zeekr/9x/images')},
 'skoda-peaq': {'side': ('skoda/peaq-d1', 'a', True, 'mirrored', 'https://www.skoda-auto.com/'), 'front': ('skoda/peaq-g1', 'r', False, 'scene photo, background removed', 'https://www.skoda-auto.com/')},

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
