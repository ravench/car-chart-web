#!/usr/bin/env python3
"""Match chart models to carsized.com car slugs.

Usage: python3 match_slugs.py data.json slugs.txt out_dir
  slugs.txt: one carsized slug per line (e.g. volkswagen-golf-2019-5-door-hatchback), optionally followed by
             a TAB and the side-view image URL and another TAB and the front-view URL.
Writes out_dir/map.tsv (id, slug, score, how, side_url, front_url) for accepted matches,
       out_dir/review.tsv (id, brand, model, generation, row, best candidates) for weak/none matches.
"""
import json, re, sys, os, unicodedata
from collections import defaultdict

data = json.load(open(sys.argv[1]))
slug_lines = [l.rstrip('\n') for l in open(sys.argv[2], encoding='utf-8') if l.strip()]
OUT = sys.argv[3]; os.makedirs(OUT, exist_ok=True)
OV = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else {}
HINTS = OV.get('hints', {}); NOIMG = set(OV.get('no_image', []))

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
def squash(s):
    return re.sub(r'[^a-z0-9]+', '', strip_accents(s).lower())

MULTI_MAKES = ['mercedes-benz', 'land-rover', 'aston-martin', 'alfa-romeo', 'rolls-royce', 'ssang-yong', 'lynk-and-co', 'lynk-co',
               'renault-trucks', 'great-wall', 'range-rover', 'mercedes-amg', 'mercedes-maybach', 'de-tomaso', 'ds-automobiles', 'dr-automobiles', 'lynk-co', 'mini-classic', 'polar-stone']
BRAND_MAKES = {  # chart brand -> candidate carsized make tokens (first that exists in the slug universe wins)
 'Mercedes-Benz': ['mercedes-benz', 'mercedes'], 'Land Rover': ['land-rover', 'range-rover'], 'Škoda': ['skoda'], 'Citroën': ['citroen'],
 'KGM': ['kgm', 'ssang-yong', 'ssangyong'], 'MINI': ['mini'], 'Lynk & Co': ['lynk-and-co', 'lynk-co', 'lynk'], 'Microlino': ['micro', 'microlino'],
 'Rolls-Royce': ['rolls-royce'], 'Aston Martin': ['aston-martin'], 'Alfa Romeo': ['alfa-romeo'], 'Renault Trucks': ['renault-trucks', 'renault'],
 'DS': ['ds'], 'smart': ['smart'], 'Cupra': ['cupra', 'seat'], 'Abarth': ['abarth'], 'XPeng': ['xpeng'], 'BYD': ['byd'], 'MG': ['mg'],
 'Volkswagen': ['volkswagen'], 'MAN': ['man'], 'Maxus': ['maxus', 'saic-maxus', 'ldv'], 'Genesis': ['genesis'], 'Leapmotor': ['leapmotor'],
 'Lepas': ['lepas'], 'Ebro': ['ebro'], 'DR': ['dr-automobiles', 'dr'], 'Omoda': ['omoda'], 'Jaecoo': ['jaecoo'], 'Chery': ['chery'], 'Lucid': ['lucid'],
 'Denza': ['denza'], 'Deepal': ['deepal'], 'Voyah': ['voyah'], 'Hongqi': ['hongqi'], 'Zeekr': ['zeekr'], 'Firefly': ['firefly'], 'Ora': ['ora', 'gwm-ora'],
 'Wey': ['wey'], 'Haval': ['haval'], 'Iveco': ['iveco'], 'Isuzu': ['isuzu'], 'Ineos': ['ineos'], 'VinFast': ['vinfast'], 'LEVC': ['levc'],
 'Farizon': ['farizon'], 'Piaggio': ['piaggio'], 'Mobilize': ['mobilize', 'renault'], 'Cadillac': ['cadillac'], 'Chevrolet': ['chevrolet'],
}

def parse_slug(slug):
    toks = slug.split('-')
    year_i = None
    for i in range(len(toks) - 1, 0, -1):
        if re.fullmatch(r'(19|20)\d\d', toks[i]): year_i = i; break
    if year_i is None: return None
    make = toks[0]
    for mm in MULTI_MAKES:
        if slug.startswith(mm + '-'): make = mm; break
    mtoks = toks[len(make.split('-')):year_i]
    return {'slug': slug, 'make': make, 'model': '-'.join(mtoks), 'msq': ''.join(mtoks), 'year': int(toks[year_i]), 'body': '-'.join(toks[year_i+1:])}

universe = {}
for l in slug_lines:
    parts = l.split('\t')
    p = parse_slug(parts[0].strip())
    if not p: continue
    p['side'] = parts[1] if len(parts) > 1 else ''
    p['front'] = parts[2] if len(parts) > 2 else ''
    universe[p['slug']] = p
by_make = defaultdict(list)
for p in universe.values(): by_make[p['make']].append(p)
makes = set(by_make)

ROW_BODY = {  # body keywords that fit a row (soft preference)
 'quadricycle': ['microcar', 'quadricycle', 'hatchback'], 'a-city': ['hatchback'], 'b-hatch': ['hatchback', 'sedan'], 'b-suv': ['suv', 'crossover'],
 'c-hatch': ['hatchback', 'sedan', 'wagon', 'liftback', 'estate'], 'c-suv': ['suv', 'crossover'], 'd-car': ['sedan', 'wagon', 'liftback', 'fastback', 'estate', 'hatchback'],
 'd-suv': ['suv', 'crossover'], 'e-car': ['sedan', 'wagon', 'liftback', 'fastback', 'estate', 'hatchback'], 'e-suv': ['suv'], 'offroad': ['offroader', 'suv', 'off-road'],
 'sports': ['coupe', 'cabriolet', 'roadster', 'convertible', 'targa', 'liftback', 'hatchback'], 'mpv-small': ['van', 'minivan', 'mpv', 'life'],
 'mpv-large': ['minivan', 'van', 'mpv', 'bus', 'kombi', 'tourer'], 'van-small': ['van', 'panel'], 'van-mid': ['van', 'panel'], 'van-large': ['van', 'panel', 'chassis'], 'pickup': ['pickup', 'pick-up', 'cab'],
}

def gen_year(m):
    g = m.get('generation') or ''
    ys = re.findall(r'(19|20)(\d\d)', g)
    return int(ys[0][0] + ys[0][1]) if ys else None

def model_variants(brand, model):
    """Candidate squashed model strings for a chart model."""
    base = model
    vs = set()
    def add(x):
        x = squash(x)
        if x: vs.add(x)
    add(base)
    add(re.sub(r'\s*\(.*?\)', '', base))               # drop parentheses
    add(re.sub(r'\s*/.*$', '', base))                  # 'XC40 / EX40' -> XC40
    add(re.sub(r'\b(e-?tech|e-?hybrid|hybrid|electric|ev|bev|plug-?in|cargo|van|kombi|tourer|life|passenger|combi|cargo van)\b', '', base, flags=re.I))
    add(re.sub(r'\bclass\b', '', base, flags=re.I))    # 'A-Class' -> 'A'
    add(re.sub(r'-?klasse|-?class', '', base, flags=re.I))
    add(base.replace('ID.', 'ID ').replace('ID. ', 'ID '))
    add(brand + ' ' + base)                            # 'Mazda2' style
    if brand.lower() in base.lower(): add(re.sub(re.escape(brand), '', base, flags=re.I))
    m = re.match(r'^(\d+)\s*(e|d)?$', base.strip(), re.I)
    if m: add(m.group(1))
    # BMW-style '3 Series', '2 Series Gran Coupé', '2 Series Active Tourer' -> '3', '2'
    m = re.match(r'^(i?\d+)\s*series\b', base.strip(), re.I)
    if m: add(m.group(1))
    add(re.sub(r'\b(series|gran coup[eé]|active tourer|coup[eé]|cabrio(let)?|touring|sportback|avant|estate|kombi)\b', '', base, flags=re.I))
    if '+' in base: add(base.replace('+', ' plus'))
    add(re.sub(r'\s*\d\.\d\s*(ev)?$', '', base, flags=re.I))   # 'DR 1.0 EV' -> 'DR'
    return {v for v in vs if v}

accepted, review = [], []
def body_score(row, body):
    words = ROW_BODY.get(row, [])
    for i, w in enumerate(words):
        if w in body: return 1.0 - 0.04 * i          # earlier keyword in the row list = better fit
    return 0.0
def extra_tokens(body):
    toks = [t for t in body.split('-') if t]
    base = {'door', '2', '3', '4', '5', 'hatchback', 'sedan', 'estate', 'suv', 'coupe', 'cabriolet', 'roadster', 'liftback', 'fastback', 'minivan', 'van', 'pickup', 'offroader', 'wagon', 'panel', 'microcar', 'crossover', 'targa', 'convertible'}
    return sum(1 for t in toks if t not in base)   # trims, lwb, electric, amg... = further from the base model

for m in data['models']:
    brand, model, row = m['brand'], m['model'], m['row']
    gy = gen_year(m)
    cands = []
    mk_list = BRAND_MAKES.get(brand, [squash(brand), strip_accents(brand).lower().replace(' ', '-')])
    mk_list = [x for x in mk_list if x in makes] or [x for x in [strip_accents(brand).lower().replace(' ', '-').replace('&', 'and')] if x in makes]
    if m['id'] in NOIMG: review.append((m['id'], brand, model, m.get('generation') or '', row, 'no_image (manual)')); continue
    hint = HINTS.get(m['id']) or (m.get('carsized_slug') or '').strip()
    if hint and hint not in universe and m['id'] in HINTS: print('HINT NOT IN UNIVERSE:', m['id'], hint)
    if hint and hint in universe:
        p = universe[hint]; accepted.append((m['id'], hint, 100, 'hint', p['side'], p['front'])); continue
    variants = model_variants(brand, model)
    for mk in mk_list:
        for p in by_make[mk]:
            sc = 0.0; how = ''
            msqs = {p['msq'], re.sub(r'(ev|electric|hybrid|phev|iv)$', '', p['msq']), re.sub(r'ev(?=[a-z])', '', p['msq'])}
            if msqs & variants: sc, how = 60, 'exact'
            else:
                for v in variants:
                    if v and any((q.startswith(v) and len(v) >= 3) or (v.startswith(q) and len(q) >= 3) for q in msqs):
                        sc, how = 35, 'prefix'; break
            if sc == 0: continue
            # year: prefer latest edition that is not before the current generation
            if gy and p['year'] < gy - 1: sc -= 25
            if p['year'] > 2026: sc -= 10
            sc += min(p['year'] - 2000, 26) * 0.5          # newer is better
            sc += 8 * body_score(row, p['body'])
            sc -= 1.0 * extra_tokens(p['body'])
            if p['side']: sc += 3
            cands.append((sc, how, p))
    cands.sort(key=lambda c: -c[0])
    if cands and cands[0][0] >= 55:
        sc, how, p = cands[0]
        accepted.append((m['id'], p['slug'], round(sc), how, p['side'], p['front']))
    else:
        review.append((m['id'], brand, model, m.get('generation') or '', row, ' | '.join(f"{c[2]['slug']} ({round(c[0])},{c[1]})" for c in cands[:5])))

with open(os.path.join(OUT, 'map.tsv'), 'w') as f:
    for r in accepted: f.write('\t'.join(str(x) for x in r) + '\n')
with open(os.path.join(OUT, 'review.tsv'), 'w') as f:
    for r in review: f.write('\t'.join(str(x) for x in r) + '\n')
print(f'{len(universe)} slugs in universe, {len(makes)} makes; matched {len(accepted)} of {len(data["models"])} models; {len(review)} to review')
