#!/usr/bin/env python3
"""Merge the per-agent research JSON files into one normalised data.json.

Usage: python3 merge.py <research_dir> <out_dir>
Writes <out_dir>/data.json and <out_dir>/merge_report.md.
Applies <research_dir>/../build/overrides.json if present.
"""
import json, re, sys, glob, os, unicodedata, difflib
from collections import defaultdict, OrderedDict

RESEARCH, OUT = sys.argv[1], sys.argv[2]
OVERRIDES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overrides.json')

ROWS = OrderedDict([
 ('quadricycle', ('Light quadricycles', 'L6e/L7e microcars such as the Citroën Ami')),
 ('a-city',      ('City cars', 'A-segment, up to about 3.8 m')),
 ('b-hatch',     ('Superminis', 'B-segment hatchbacks and small saloons')),
 ('b-suv',       ('Small SUVs', 'B-segment crossovers, about 4.0–4.35 m')),
 ('c-hatch',     ('Compact cars', 'C-segment hatchbacks, saloons and estates')),
 ('c-suv',       ('Compact SUVs', 'C-segment SUVs, about 4.35–4.65 m')),
 ('d-car',       ('Mid-size cars', 'D-segment saloons, estates and fastbacks')),
 ('d-suv',       ('Mid-size SUVs', 'D-segment SUVs, about 4.65–4.9 m')),
 ('e-car',       ('Executive & luxury cars', 'E- and F-segment saloons and estates')),
 ('e-suv',       ('Large SUVs', 'E- and F-segment SUVs, 4.9 m and up')),
 ('offroad',     ('Off-road 4×4s', 'Purpose-built off-roaders, mostly ladder-frame')),
 ('sports',      ('Sports cars & coupés', 'Two-door sports cars, GTs, convertibles and supercars')),
 ('mpv-small',   ('Compact MPVs', 'Leisure activity vehicles and compact people carriers')),
 ('mpv-large',   ('Large MPVs', 'Van-derived people carriers and minivans')),
 ('van-small',   ('Small & compact vans', 'Car-derived and Kangoo/Berlingo/Caddy-class vans')),
 ('van-mid',     ('Mid-size vans', 'One-tonne vans of the Transporter/Vito/Trafic class')),
 ('van-large',   ('Large vans', '3.5 t vans and chassis cabs of the Sprinter/Ducato class')),
 ('pickup',      ('Pickups', 'One-tonne pickups')),
])

GROUPS = OrderedDict([
 ('Volkswagen Group', ['Volkswagen','Audi','Škoda','SEAT','Cupra','Porsche','Bentley','Lamborghini','MAN']),
 ('Stellantis', ['Peugeot','Citroën','DS','Opel','Fiat','Abarth','Alfa Romeo','Lancia','Jeep','Maserati','Leapmotor']),
 ('Renault Group', ['Renault','Dacia','Alpine','Mobilize']),
 ('Nissan', ['Nissan']),
 ('Mitsubishi Motors', ['Mitsubishi']),
 ('Mercedes-Benz Group', ['Mercedes-Benz','smart']),
 ('BMW Group', ['BMW','MINI','Rolls-Royce']),
 ('Toyota Motor', ['Toyota','Lexus']),
 ('Subaru', ['Subaru']),
 ('Suzuki', ['Suzuki']),
 ('Mazda', ['Mazda']),
 ('Honda', ['Honda']),
 ('Hyundai Motor Group', ['Hyundai','Kia','Genesis']),
 ('Ford', ['Ford']),
 ('General Motors', ['Cadillac','Chevrolet']),
 ('Tesla', ['Tesla']),
 ('Geely Holding', ['Volvo','Polestar','Lynk & Co','Zeekr','Lotus','Farizon','LEVC','Geely']),
 ('SAIC Motor', ['MG','Maxus','IM']),
 ('BYD', ['BYD','Denza']),
 ('Chery', ['Omoda','Jaecoo','Chery','Exeed','Lepas']),
 ('Ebro (EV Motors)', ['Ebro']),
 ('DR Automobiles', ['DR']),
 ('Great Wall Motor', ['Ora','Wey','Haval','GWM']),
 ('XPeng', ['XPeng']),
 ('NIO', ['NIO','Firefly','Onvo']),
 ('Changan', ['Changan','Deepal','Avatr']),
 ('Dongfeng', ['Voyah','Dongfeng','Mhero']),
 ('FAW', ['Hongqi']),
 ('Xiaomi', ['Xiaomi']),
 ('Tata Motors', ['Jaguar','Land Rover']),
 ('KG Mobility', ['KGM']),
 ('Isuzu', ['Isuzu']),
 ('Ineos', ['Ineos']),
 ('Iveco Group', ['Iveco']),
 ('Volvo Group', ['Renault Trucks']),
 ('Lucid', ['Lucid']),
 ('Ferrari', ['Ferrari']),
 ('Aston Martin', ['Aston Martin']),
 ('McLaren', ['McLaren']),
 ('Morgan', ['Morgan']),
 ('Caterham', ['Caterham']),
 ('Bugatti Rimac', ['Bugatti','Rimac']),
 ('Koenigsegg', ['Koenigsegg']),
 ('Pagani', ['Pagani']),
 ('VinFast', ['VinFast']),
 ('Micro Mobility', ['Microlino']),
 ('Piaggio', ['Piaggio']),
])
BRAND2GROUP = {b: g for g, bs in GROUPS.items() for b in bs}

BRAND_ALIASES = {
 'vw': 'Volkswagen', 'volkswagen commercial vehicles': 'Volkswagen', 'volkswagen nutzfahrzeuge': 'Volkswagen',
 'vw nutzfahrzeuge': 'Volkswagen', 'volkswagen (commercial vehicles)': 'Volkswagen', 'vwn': 'Volkswagen',
 'skoda': 'Škoda', 'seat': 'SEAT', 'cupra': 'Cupra', 'man truck & bus': 'MAN', 'man trucks': 'MAN',
 'citroen': 'Citroën', 'ds automobiles': 'DS', 'vauxhall': 'Opel', 'opel/vauxhall': 'Opel', 'opel / vauxhall': 'Opel',
 'fiat professional': 'Fiat', 'alfa': 'Alfa Romeo', 'mercedes': 'Mercedes-Benz', 'mercedes-benz vans': 'Mercedes-Benz',
 'mercedes-amg': 'Mercedes-Benz', 'mercedes-maybach': 'Mercedes-Benz', 'mercedes benz': 'Mercedes-Benz',
 'smart': 'smart', 'mini': 'MINI', 'rolls royce': 'Rolls-Royce', 'toyota professional': 'Toyota',
 'land rover': 'Land Rover', 'range rover': 'Land Rover', 'kg mobility': 'KGM', 'ssangyong': 'KGM', 'kgm motors': 'KGM',
 'lynk&co': 'Lynk & Co', 'lynk & co.': 'Lynk & Co', 'lynk and co': 'Lynk & Co', 'maxus (saic)': 'Maxus', 'saic maxus': 'Maxus',
 'im motors': 'IM', 'mg motor': 'MG', 'omoda & jaecoo': 'Omoda', 'ora (gwm)': 'Ora', 'great wall': 'GWM', 'gwm ora': 'Ora',
 'xpeng motors': 'XPeng', 'nio': 'NIO', 'ineos automotive': 'Ineos', 'ineos grenadier': 'Ineos', 'renault trucks': 'Renault Trucks',
 'micro': 'Microlino', 'micro mobility': 'Microlino', 'microlino': 'Microlino', 'bugatti rimac': 'Bugatti',
 'cadillac europe': 'Cadillac', 'genesis motor': 'Genesis', 'honda motor': 'Honda', 'tesla motors': 'Tesla',
 'alpine cars': 'Alpine', 'dacia': 'Dacia', 'mobilize': 'Mobilize', 'lexus': 'Lexus', 'levc': 'LEVC', 'farizon auto': 'Farizon',
 'geely auto': 'Geely', 'byd auto': 'BYD', 'denza': 'Denza', 'deepal': 'Deepal', 'changan auto': 'Changan',
}

def canon_brand(b):
    if not b: return b
    key = b.strip().lower()
    if key in BRAND_ALIASES: return BRAND_ALIASES[key]
    for g, bs in GROUPS.items():
        for cb in bs:
            if cb.lower() == key: return cb
    return b.strip()

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))

def norm_key(brand, model):
    s = strip_accents(f'{brand} {model}').lower()
    s = s.replace('&', ' and ').replace('+', ' plus ')
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    return s

def slug(s):
    s = strip_accents(s).lower().replace('+', '-plus')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

# ---------- load ----------
files = sorted(glob.glob(os.path.join(RESEARCH, '*.json')))
report = []
raw = []          # (agent, record)
announced = []
discontinued = []
sources = []
for f in files:
    try:
        d = json.load(open(f))
    except Exception as e:
        report.append(f'ERROR reading {f}: {e}'); continue
    agent = d.get('agent') or os.path.basename(f)
    for m in d.get('models', []):
        m['_agent'] = os.path.basename(f).replace('.json', '')
        raw.append(m)
    for m in d.get('announced', []):
        m['_agent'] = os.path.basename(f).replace('.json', ''); announced.append(m)
    for m in d.get('discontinued_recently', []):
        m['_agent'] = os.path.basename(f).replace('.json', ''); discontinued.append(m)
    for s in d.get('sources', []):
        s['_agent'] = os.path.basename(f).replace('.json', ''); sources.append(s)
report.append(f'Loaded {len(files)} files, {len(raw)} model records, {len(announced)} announced, {len(discontinued)} discontinued notes.')

# ---------- overrides ----------
ov = {'models': {}, 'aliases': {}, 'exclude': [], 'group_labels': {}, 'edges_add': [], 'edges_remove': [], 'merge': {}}
if os.path.exists(OVERRIDES):
    ov.update(json.load(open(OVERRIDES)))
for k, v in ov.get('aliases', {}).items():
    pass

# promote announced entries to on-sale models when the override says so
for spec in ov.get('promote', []):
    pn = norm_key(spec['brand'], spec['model'])
    hit = [a for a in announced if norm_key(canon_brand(a.get('brand')), a.get('model') or '') == pn]
    if not hit: report.append(f'PROMOTE target not found: {spec}'); continue
    a = hit[0]
    for other in hit[1:]: announced.remove(other)
    announced.remove(a)
    a.update({k: v for k, v in spec.items() if k not in ('brand', 'model')})
    a.setdefault('status', 'on_sale')
    raw.append(a); report.append(f"PROMOTED {spec['brand']} {spec['model']} -> {a['status']}")

LCV_ROWS = {'van-small', 'van-mid', 'van-large', 'pickup', 'mpv-small', 'mpv-large'}
LCV_AGENT = 'lcv'

# ---------- normalise & dedupe ----------
# records are keyed by "<norm>|<row>" so that a van and its passenger version with the same name stay separate
recs = {}
by_norm = defaultdict(list)
def merge_into(base, extra):
    for k, v in extra.items():
        if k.startswith('_'): continue
        if base.get(k) in (None, '', [], {}) and v not in (None, '', [], {}):
            base[k] = v

for m in raw:
    m['brand'] = canon_brand(m.get('brand'))
    m['model'] = (m.get('model') or '').strip()
    if not m['brand'] or not m['model']:
        report.append(f"SKIP record without brand/model from {m['_agent']}: {m}"); continue
    norm = norm_key(m['brand'], m['model'])
    norm = ov.get('aliases', {}).get(norm, norm)
    row = m.get('row')
    if m.get('status') not in ('on_sale', 'runout'):
        if m.get('status') == 'announced':
            announced.append(m); continue
        report.append(f"WARN unknown status {m.get('status')!r} for {norm} ({m['_agent']}); keeping")
    # same name, different row: separate tile only if an LCV-row vs non-LCV-row split or the override says so
    key = f'{norm}|{row}'
    if key not in recs and by_norm.get(norm):
        other = by_norm[norm][0]
        orow = recs[other].get('row')
        split_ok = (row in LCV_ROWS) != (orow in LCV_ROWS) or ({row, orow} <= LCV_ROWS and row != orow)
        if not split_ok:
            report.append(f"DUP-ROW {norm}: {orow} (kept, {recs[other]['_agent']}) vs {row} ({m['_agent']}); merged into first")
            key = other
    if key in recs:
        base = recs[key]
        lcv_new = (m['_agent'] == LCV_AGENT and row in LCV_ROWS)
        lcv_base = (base['_agent'] == LCV_AGENT and base.get('row') in LCV_ROWS)
        if lcv_new and not lcv_base:
            m['_agents'] = base['_agents'] + [m['_agent']]
            merge_into(m, base); recs[key] = m; base, m = m, base
        else:
            base['_agents'].append(m['_agent'])
            merge_into(base, m)
        diffs = []
        for fld in ('row', 'status', 'twin_tier'):
            if m.get(fld) not in (None, '') and base.get(fld) != m.get(fld):
                diffs.append(f"{fld}: {base.get(fld)!r} (kept, {base['_agent']}) vs {m.get(fld)!r} ({m['_agent']})")
        if diffs:
            report.append(f"DUP {norm}: " + '; '.join(diffs))
    else:
        m['_agents'] = [m['_agent']]
        recs[key] = m
        by_norm[norm].append(key)

# apply per-model overrides
for key, changes in ov.get('models', {}).items():
    if key in recs:
        recs[key].update(changes)
    else:
        report.append(f'OVERRIDE target not found: {key}')
excluded_norms = set()
for key in ov.get('exclude', []):
    if key in recs:
        report.append(f'EXCLUDED by override: {key}')
        del recs[key]
    nm = key.split('|')[0]
    excluded_norms.add(re.sub(r'[^a-z0-9]+', ' ', strip_accents(nm).lower()).strip())
# announced: aliases, exclusions, de-duplication against each other and against on-sale models
ANN_ALIASES = {k: v for k, v in ov.get('announced_aliases', {}).items()}
ann_excl = {norm_key(*x.split(' ', 1)) if ' ' in x else x for x in ov.get('announced_exclude', [])}
ann_excl |= excluded_norms
model_norms = {norm_key(m['brand'], m['model']) for m in recs.values()}
seen_ann = {}
new_ann = []
for a in announced:
    a['brand'] = canon_brand(a.get('brand')); a['model'] = (a.get('model') or '').strip()
    n = norm_key(a['brand'], a['model']); n = ANN_ALIASES.get(n, n)
    if n in ann_excl: report.append(f'ANNOUNCED dropped (excluded): {a["brand"]} {a["model"]}'); continue
    if n in model_norms: report.append(f'ANNOUNCED dropped (already an on-sale model): {a["brand"]} {a["model"]}'); continue
    if n in seen_ann:
        merge_into(seen_ann[n], a); report.append(f'ANNOUNCED de-duplicated: {a["brand"]} {a["model"]}'); continue
    seen_ann[n] = a; new_ann.append(a)
announced = new_ann

# row validation
for key, m in recs.items():
    if m.get('row') not in ROWS:
        report.append(f"BAD ROW {m.get('row')!r} for {key} ({m['_agent']})")
    g = BRAND2GROUP.get(m['brand'])
    if g is None:
        report.append(f"UNKNOWN BRAND {m['brand']!r} ({key}); agent group label {m.get('group')!r}")
        g = m.get('group') or m['brand']
        if m['brand'] not in BRAND2GROUP:
            GROUPS.setdefault(g, [])
            if m['brand'] not in GROUPS[g]: GROUPS[g].append(m['brand'])
            BRAND2GROUP[m['brand']] = g
    m['group'] = g
    m['id'] = slug(f"{m['brand']} {m['model']}")
    if len(by_norm.get(norm_key(m['brand'], m['model']), [])) > 1: m['id'] += '-' + m['row']

# ---------- twin edges ----------
keys = list(recs.keys())
by_row_keys = defaultdict(list)
for k, m in recs.items(): by_row_keys[m.get('row')].append(k)

PRE_ALIASES = [('Opel/Vauxhall', 'Opel'), ('Opel / Vauxhall', 'Opel'), ('Vauxhall', 'Opel'), ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Mercedes ', 'Mercedes-Benz '), ('VW ', 'Volkswagen '), ('Skoda', 'Škoda'), ('Citroen', 'Citroën'), ('Lynk&Co', 'Lynk & Co'),
    ('Lynk and Co', 'Lynk & Co'), ('Range Rover ', 'Land Rover Range Rover '), ('Fiat Professional', 'Fiat'), ('Toyota Professional', 'Toyota'),
    ('Mercedes-Benz-Benz', 'Mercedes-Benz')]
def resolve_member(name, row, src_key):
    """Map a 'Brand Model' string to a record key."""
    name = name.strip()
    name = re.sub(r'\s*\((?:tier\s*)?[12]\)\s*$', '', name)
    for a, b in PRE_ALIASES:
        if name.startswith(a): name = b + name[len(a):]; break
    cand = None
    for b in sorted(BRAND2GROUP.keys(), key=len, reverse=True):
        if strip_accents(name).lower().startswith(strip_accents(b).lower() + ' ') or strip_accents(name).lower() == strip_accents(b).lower():
            cand = (b, name[len(b):].strip(' -:/')); break
    if cand is None:
        for a, b in sorted(BRAND_ALIASES.items(), key=lambda x: len(x[0]), reverse=True):
            if strip_accents(name).lower().startswith(a + ' '):
                cand = (b, name[len(a):].strip(' -:/')); break
    if cand is None:
        return None, f'no brand match for {name!r}'
    b, mdl = cand
    tries = [norm_key(b, mdl), norm_key(b, f'{b} {mdl}')]
    if strip_accents(mdl).lower().startswith(strip_accents(b).lower() + ' '):
        tries.append(norm_key(b, mdl[len(b):].strip()))
    for k in tries:
        k = ov.get('aliases', {}).get(k, k)
        cands = [c for c in by_norm.get(k, []) if c in recs]
        if cands:
            same = [c for c in cands if recs[c].get('row') == row]
            return (same[0] if same else cands[0]), None
    k = tries[0]
    pool = [x for x in by_row_keys.get(row, []) if recs[x]['brand'] == b]
    cm = difflib.get_close_matches(k, pool, n=1, cutoff=0.78)
    if cm: return cm[0], f'fuzzy {name!r} -> {cm[0]}'
    for x in pool:
        if x.startswith(k + ' ') or k.startswith(x + ' '): return x, f'prefix {name!r} -> {x}'
    # token match: same brand, same numeric tokens and same first word of the model
    kt = k.split()
    for x in pool:
        xt = x.split()
        if [t for t in kt if t.isdigit()] == [t for t in xt if t.isdigit()] and len(kt) > 1 and len(xt) > 1 and kt[1] == xt[1] and [t for t in kt if t.isdigit()]:
            return x, f'token {name!r} -> {x}'
    pool2 = [x for x in recs if recs[x]['brand'] == b]
    cm = difflib.get_close_matches(k, pool2, n=1, cutoff=0.85)
    if cm: return cm[0], f'fuzzy-anyrow {name!r} -> {cm[0]} (row {recs[cm[0]].get("row")} vs {row})'
    return None, f'unresolved member {name!r} (from {src_key})'

edges = {}   # frozenset(a,b) -> list of (tier, src)
for k, m in recs.items():
    tier = m.get('twin_tier')
    members = m.get('twin_members') or []
    if not members: continue
    for name in members:
        tk, note = resolve_member(name, m.get('row'), k)
        if note and tk: report.append(f'NOTE {note}')
        if tk is None:
            nn = re.sub(r'[^a-z0-9]+', ' ', strip_accents(name).lower()).strip()
            for a_, b_ in PRE_ALIASES:
                if name.startswith(a_): nn = re.sub(r'[^a-z0-9]+', ' ', strip_accents(b_ + name[len(a_):]).lower()).strip(); break
            if nn in excluded_norms: continue
            report.append(f'UNRESOLVED {note} [tier {tier}]'); continue
        if tk == k: continue
        if recs[tk].get('row') != m.get('row'):
            report.append(f"ROW MISMATCH in twin claim: {k} ({m.get('row')}) ~ {tk} ({recs[tk].get('row')}) tier {tier}")
            continue
        edges.setdefault(frozenset((k, tk)), []).append((tier if tier in (1, 2) else 2, k))

for e in ov.get('edges_add', []):
    a, b, t = e['a'], e['b'], e.get('tier', 2)
    if a in recs and b in recs: edges.setdefault(frozenset((a, b)), []).append((t, 'override'))
    else: report.append(f'edges_add target missing: {e}')
for e in ov.get('edges_remove', []):
    edges.pop(frozenset((e['a'], e['b'])), None)

# resolve tier per edge: if any override -> that; elif all agree -> that; else report & take max (conservative)
edge_tier = {}
for e, claims in edges.items():
    ts = {t for t, s in claims}
    ovs = [t for t, s in claims if s == 'override']
    if ovs: edge_tier[e] = ovs[-1]
    elif len(ts) == 1: edge_tier[e] = ts.pop()
    else:
        a, b = tuple(e)
        report.append(f'TIER CONFLICT {a} ~ {b}: claims {claims}; using tier 2 (conservative)')
        edge_tier[e] = 2

# union-find
parent = {k: k for k in recs}
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[rb] = ra
for e in edge_tier: a, b = tuple(e); union(a, b)

comps = defaultdict(list)
for k in recs: comps[find(k)].append(k)
twin_groups = []
PALETTE_N = 8
# order groups within each row by first column appearance so neighbours get different slots
group_order_in_brand = {b: i for i, b in enumerate([b for g in GROUPS.values() for b in g])}
row_counter = defaultdict(int)
for root, members in comps.items():
    if len(members) < 2: continue
    if len({recs[k]['brand'] for k in members}) < 2:
        report.append('SAME-BRAND group not shown: ' + ' | '.join(members)); continue
    row = recs[members[0]].get('row')
    members.sort(key=lambda k: group_order_in_brand.get(recs[k]['brand'], 999))
    t1 = {k: False for k in members}
    for e, t in edge_tier.items():
        if t == 1:
            for k in e: t1[k] = True
    gid = f"g-{row}-{row_counter[row]+1}"
    slot = row_counter[row] % PALETTE_N
    row_counter[row] += 1
    # label: platform override or lead member
    label = ov.get('group_labels', {}).get(gid)
    if not label:
        plats = [recs[k].get('platform') for k in members if recs[k].get('platform')]
        label = None
        if plats:
            # shortest common platform string
            label = sorted(plats, key=len)[0]
            label = re.split(r'[(,;/]', label)[0].strip()
            if len(label) > 14: label = None
        if not label: label = recs[members[0]]['model']
    twin_groups.append({'id': gid, 'row': row, 'members': [recs[k]['id'] for k in members], 'label': label,
                        'slot': slot, 'tier1_members': [recs[k]['id'] for k in members if t1[k]],
                        'edges': [{'a': recs[a]['id'], 'b': recs[b]['id'], 'tier': t} for e, t in edge_tier.items() if e <= set(members) for a, b in [tuple(e)]]})
    for k in members:
        recs[k]['twin_group'] = gid
        recs[k]['twin_style'] = 1 if t1[k] else 2

# ---------- output ----------
models_out = []
for k, m in recs.items():
    o = {kk: vv for kk, vv in m.items() if not kk.startswith('_')}
    o['key'] = k
    o['agents'] = m.get('_agents', [])
    models_out.append(o)
models_out.sort(key=lambda o: (list(ROWS).index(o['row']) if o['row'] in ROWS else 99, group_order_in_brand.get(o['brand'], 999), o['model']))

data = {
 'meta': {'checked_on': '2026-10-22', 'market': 'Europe (Swiss names)', 'n_models': len(models_out), 'n_groups': len(twin_groups)},
 'rows': [{'code': c, 'name': n, 'desc': d} for c, (n, d) in ROWS.items()],
 'groups': [{'label': g, 'brands': [b for b in bs if any(o['brand'] == b for o in models_out)]} for g, bs in GROUPS.items()],
 'models': models_out,
 'twin_groups': twin_groups,
 'announced': [{kk: vv for kk, vv in a.items() if not kk.startswith('_')} for a in announced],
 'discontinued': [{kk: vv for kk, vv in a.items() if not kk.startswith('_')} for a in discontinued],
 'sources': [{kk: vv for kk, vv in s.items() if not kk.startswith('_')} | {'agent': s.get('_agent')} for s in sources],
}
data['groups'] = [g for g in data['groups'] if g['brands']]
os.makedirs(OUT, exist_ok=True)
json.dump(data, open(os.path.join(OUT, 'data.json'), 'w'), ensure_ascii=False, indent=1)
# per-row / per-brand counts
cnt = defaultdict(int)
for o in models_out: cnt[(o['row'])] += 1
report.append('\nModels per row: ' + ', '.join(f'{r}={cnt[r]}' for r in ROWS))
bc = defaultdict(int)
for o in models_out: bc[o['brand']] += 1
report.append('Models per brand: ' + ', '.join(f'{b}={n}' for b, n in sorted(bc.items())))
report.append(f'Twin groups: {len(twin_groups)}')
for g in twin_groups:
    report.append(f"  {g['id']} [{g['label']}] " + ' | '.join(g['members']))
open(os.path.join(OUT, 'merge_report.md'), 'w').write('\n'.join(report))
print('\n'.join(report[:1]), '->', os.path.join(OUT, 'data.json'))
print(f"{len(models_out)} models, {len(twin_groups)} groups; report lines: {len(report)}")
