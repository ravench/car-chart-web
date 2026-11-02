#!/usr/bin/env python3
"""Generate out/index.html from data.json. Usage: gen.py data.json out_dir [img_manifest.json]"""
import json, re, sys, os, html, re
from collections import defaultdict, OrderedDict

DATA = json.load(open(sys.argv[1]))
OUT = sys.argv[2]
MANIFEST = json.load(open(sys.argv[3])) if len(sys.argv) > 3 and os.path.exists(sys.argv[3]) else {}
DIMS = json.load(open(sys.argv[4])) if len(sys.argv) > 4 and os.path.exists(sys.argv[4]) else {}
FLAGS = json.load(open(sys.argv[5])) if len(sys.argv) > 5 and os.path.exists(sys.argv[5]) else {'edges': [], 'groups': {}, 'img_notes': {}, 'summary': {}, 'length_check': []}
EXT_PATH = sys.argv[6] if len(sys.argv) > 6 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ext', 'manifest.json')
EXT = json.load(open(EXT_PATH)) if os.path.exists(EXT_PATH) else {}
DRIVE_PATH = sys.argv[7] if len(sys.argv) > 7 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'drive.json')
DRIVE = json.load(open(DRIVE_PATH)) if os.path.exists(DRIVE_PATH) else {}   # id -> {drives, awd, awd_term, note, confidence, source}   # id -> {side: {url, page, source, licence, notes}, front: {...}} for pictures not from carsized
PREV = set(FLAGS.get('prev_model', []))   # models pictured with a previous model because carsized has no entry for the current one
for _i in [k for k, v in DIMS.items() if v.get('prev_model') and k not in PREV]: DIMS.pop(_i)   # carsized has only a previous model and the tile no longer shows it: drop its measurements and attribution
PREV_YEAR = {k: int(v) for k, v in (FLAGS.get('prev_year') or {}).items()}   # id -> badge year (last year of carsized's range, capped at 2025)
COUNTRIES_PATH = sys.argv[8] if len(sys.argv) > 8 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'research', 'countries', 'brand_countries.json')
COUNTRIES = json.load(open(COUNTRIES_PATH)) if os.path.exists(COUNTRIES_PATH) else {'brands': {}, 'groups': {}}   # brand -> {country, hq, built_in, second_flag, note, sources}
CHART_VERSION = '1.17'   # shown in the page header so a reader (and a stale browser cache) can be told apart from the newest release
import random, math
def full_name(brand, display):
    """'DR' + 'DR 6' -> 'DR 6'; 'Polestar' + 'Polestar 4' -> 'Polestar 4'; 'BMW' + 'X5' -> 'BMW X5'."""
    b, d = brand.lower(), display.lower()
    return display if d == b or d.startswith(b + ' ') else f'{brand} {display}'
def cs_label(slug):
    """'volkswagen-golf-2024-5-door-hatchback' -> '5-door hatchback, 2024'; 'citroen-berlingo-2024-van-xl' -> 'van XL, 2024'."""
    mm = re.search(r'-(\d{4})(?:-(.*))?$', slug or '')
    if not mm: return slug or ''
    toks = [t for t in (mm.group(2) or '').split('-') if t]
    out = []
    for t in toks:
        if out and re.fullmatch(r'\d', out[-1]) and t == 'door': out[-1] = out[-1] + '-door'
        elif t in ('xl', 'l1', 'l2', 'l3', 'h1', 'h2', 'lwb', 'swb', 'suv', 'mpv', 'ev', 'phev', 'bev', 'gt', 'rs', 'gti', 'amg', 'm', 'l'): out.append(t.upper())
        else: out.append(t)
    body = ' '.join(out)
    return (body + ', ' if body else '') + mm.group(1)
os.makedirs(OUT, exist_ok=True)
E = html.escape

rows = DATA['rows']; groups = DATA['groups']; models = DATA['models']; tgs = {g['id']: g for g in DATA['twin_groups']}
brands = [b for g in groups for b in g['brands']]
by_cell = defaultdict(list)
for m in models: by_cell[(m['row'], m['brand'])].append(m)
mid = {m['id']: m for m in models}
rowmax = defaultdict(int)
for m in models:
    if m.get('length_mm'): rowmax[m['row']] = max(rowmax[m['row']], m['length_mm'])
import statistics
_wr = defaultdict(list)
for m in models:
    dd = DIMS.get(m['id']) or {}
    if (dd.get('widm') or dd.get('wid')) and dd.get('len'): _wr[m['row']].append((dd.get('widm') or dd.get('wid')) / dd['len'])
ROWRATIO = {r: statistics.median(v) for r, v in _wr.items() if v}   # width (with mirrors) / length per class: front-view scale for models without a carsized width

PT_MAP = [('BEV','EV'),('PHEV','PHEV'),('HEV','HEV'),('MHEV','MHEV'),('FCEV','H₂'),('petrol','ICE'),('diesel','ICE'),('LPG','ICE'),('CNG','ICE')]
def pt_tags(pts):
    out = []
    for k, v in PT_MAP:
        if k in (pts or []) and v not in out: out.append(v)
    return out

PT_FILTER = [('BEV', 'ev'), ('PHEV', 'phev'), ('HEV', 'hev'), ('MHEV', 'mhev'), ('petrol', 'petrol'), ('LPG', 'petrol'), ('CNG', 'petrol'), ('diesel', 'diesel'), ('FCEV', 'h2')]
PT_FILTER_LABEL = [('ev', 'Electric (BEV)'), ('phev', 'Plug-in hybrid'), ('hev', 'Full hybrid'), ('mhev', 'Mild hybrid'), ('petrol', 'Petrol (incl. LPG, CNG)'), ('diesel', 'Diesel'), ('h2', 'Hydrogen')]
DRIVE_LABEL = [('FWD', 'Front-wheel drive'), ('RWD', 'Rear-wheel drive'), ('AWD', 'All-wheel drive / 4x4'), ('unknown', 'Drive not researched')]
def pt_keys(pts):
    out = []
    for k, v in PT_FILTER:
        if k in (pts or []) and v not in out: out.append(v)
    return out or ['other']
def drive_keys(m):
    d = DRIVE.get(m['id']) or {}
    return [x for x in d.get('drives') or [] if x in ('FWD', 'RWD', 'AWD')] or ['unknown']
def awd_title(d):
    t = 'Sold with all-wheel drive' + (f' ({d["awd_term"]})' if d.get('awd_term') else '')
    if d.get('note'): t += ' — ' + d['note']
    return t

def tile(m, s=0, place='', above=None):
    g = m.get('twin_group'); style = m.get('twin_style')
    cls = ['tile']
    attrs = [f'data-id="{E(m["id"])}"', f'data-row="{E(m["row"])}"', f'data-brand="{E(m["brand"])}"', f'data-s="{s}"']
    st = [place] if place else []
    if g:
        cls.append('t1' if style == 1 else 't2'); attrs.append(f'data-g="{E(g)}"')
        st.append(f'--gc:var(--c{tgs[g]["slot"]+1})')
    if above: cls.append('stack'); attrs.append(f'data-above="{E(above)}"')   # second member of the same family in this brand column: stub up to the member above
    if st: attrs.append(f'style="{";".join(st)}"')
    L = ((DIMS.get(m['id']) or {}).get('len') if MANIFEST.get(m['id']) else None) or m.get('length_mm')
    if L: attrs.append(f'data-len="{L}"')
    if L:   # real width for the front-view scale modes (carsized width with mirrors, else the class ratio)
        dd = DIMS.get(m['id']) or {}
        W = (dd.get('widm') or dd.get('wid')) if MANIFEST.get(m['id']) else None
        if not W and ROWRATIO.get(m['row']): W = round(L * ROWRATIO[m['row']])
        if W: attrs.append(f'data-wid="{W}"')
    attrs.append(f'data-pt="{" ".join(pt_keys(m.get("powertrains")))}"'); attrs.append(f'data-drive="{" ".join(drive_keys(m))}"')
    img = MANIFEST.get(m['id'], {})
    side = img.get('side'); front = img.get('front')
    if side and img.get('sw') and img.get('sh'): attrs.append(f'data-sar="{img["sw"] / img["sh"]:.3f}"')
    if front and img.get('fw') and img.get('fh'): attrs.append(f'data-far="{img["fw"] / img["fh"]:.3f}"')
    chip = f'<span class="chip" title="{E(tgs[g]["label"])}">{E(tgs[g]["label"])}</span>' if g else ''
    tags = ' '.join(f'<span class="tag">{E(t)}</span>' for t in pt_tags(m.get('powertrains')))
    dv = DRIVE.get(m['id']) or {}
    if dv.get('awd'): tags += f' <span class="tag awd" title="{E(awd_title(dv))}">AWD</span>'
    flags = ''
    if m.get('status') == 'runout': flags += '<span class="tag warn">run-out</span>'
    if m.get('ch_on_sale') is False: flags += '<span class="tag off">not in CH</span>'
    imgs = ''
    if side: imgs += f'<img class="v-side" loading="lazy" src="{E(side)}" data-sid="{E(m["id"])}" onerror="sideFallback(this)" alt="{E(full_name(m["brand"], m["display"]))}, side view">'
    if front: imgs += f'<img class="v-front" data-fid="{E(m["id"])}" alt="{E(full_name(m["brand"], m["display"]))}, front view">'
    if side and not front: cls.append('nofront')
    if side and m['id'] in PREV:
        yr = PREV_YEAR.get(m['id'], 2025)
        cls.append('prev'); imgs += f'<span class="yr" title="carsized has no entry for the current generation; the picture and the measurements are those of the previous model, the one sold in {yr}">{yr} model</span>'
    if not side and not front: imgs = f'<span class="noimg">{E(m["display"])}</span>'
    return (f'<button class="{" ".join(cls)}" {" ".join(attrs)} type="button">'
            f'{chip}<span class="img">{imgs}</span>'
            f'<span class="name">{E(m["display"])}</span>'
            f'<span class="tags">{tags}{flags}</span></button>')

# ---------- brand countries (flags) ----------
COUNTRY_NAME = {'DE':'Germany','FR':'France','IT':'Italy','ES':'Spain','GB':'United Kingdom','CZ':'Czechia','RO':'Romania','SE':'Sweden','CH':'Switzerland','HR':'Croatia','US':'United States','JP':'Japan','KR':'South Korea','CN':'China','VN':'Vietnam','NL':'Netherlands','IN':'India','TH':'Thailand','TR':'Türkiye','BE':'Belgium','PL':'Poland','SK':'Slovakia','HU':'Hungary','PT':'Portugal','MA':'Morocco','MX':'Mexico','AT':'Austria','ZA':'South Africa','MY':'Malaysia','ID':'Indonesia','TW':'Taiwan','BR':'Brazil','AR':'Argentina','CA':'Canada','RS':'Serbia','SI':'Slovenia','FI':'Finland','NO':'Norway','DK':'Denmark','IE':'Ireland','AU':'Australia','UZ':'Uzbekistan','EG':'Egypt','RU':'Russia','UA':'Ukraine','BG':'Bulgaria','GR':'Greece','LU':'Luxembourg','PH':'Philippines','PK':'Pakistan','SA':'Saudi Arabia','AE':'United Arab Emirates','IR':'Iran','KZ':'Kazakhstan','NG':'Nigeria','GH':'Ghana','ET':'Ethiopia','KE':'Kenya','CL':'Chile','CO':'Colombia','PE':'Peru','UY':'Uruguay','VE':'Venezuela','NZ':'New Zealand','SG':'Singapore','HK':'Hong Kong','MO':'Macau','KH':'Cambodia','LA':'Laos','MM':'Myanmar','BD':'Bangladesh','LK':'Sri Lanka','NP':'Nepal','IL':'Israel','JO':'Jordan','QA':'Qatar','KW':'Kuwait','OM':'Oman','BH':'Bahrain','DZ':'Algeria','TN':'Tunisia','LY':'Libya','SD':'Sudan','LT':'Lithuania','LV':'Latvia','EE':'Estonia','BY':'Belarus','MD':'Moldova','MK':'North Macedonia','AL':'Albania','BA':'Bosnia and Herzegovina','ME':'Montenegro','XK':'Kosovo','IS':'Iceland','MT':'Malta','CY':'Cyprus','LI':'Liechtenstein','MC':'Monaco','AD':'Andorra','SM':'San Marino'}
def _h(*cols):
    n = len(cols); h = 40 / n
    return ''.join(f'<rect y="{k*h:.2f}" width="60" height="{h+0.05:.2f}" fill="{c}"/>' for k, c in enumerate(cols))
def _v(*cols):
    n = len(cols); w = 60 / n
    return ''.join(f'<rect x="{k*w:.2f}" width="{w+0.05:.2f}" height="40" fill="{c}"/>' for k, c in enumerate(cols))
def _star(cx, cy, r, fill, rot=-90, stroke=None):
    pts = []
    for k in range(10):
        ang = math.radians(rot + k * 36); rr = r if k % 2 == 0 else r * 0.382
        pts.append(f'{cx + rr * math.cos(ang):.2f},{cy + rr * math.sin(ang):.2f}')
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"' + (f' stroke="{stroke}" stroke-width="1.6" stroke-linejoin="round"' if stroke else '') + '/>'
def _tri(cx, cy, rot, broken):
    out = []
    for k, br in enumerate(broken):
        y = -4 + k * 4
        out.append(f'<rect x="-5" y="{y-1}" width="4.2" height="2"/><rect x="0.8" y="{y-1}" width="4.2" height="2"/>' if br else f'<rect x="-5" y="{y-1}" width="10" height="2"/>')
    return f'<g transform="translate({cx},{cy}) rotate({rot})" fill="#000">{"".join(out)}</g>'
FLAG_SVG = {
 'DE': _h('#000', '#dd0000', '#ffce00'), 'FR': _v('#0055a4', '#fff', '#ef4135'), 'IT': _v('#009246', '#fff', '#ce2b37'), 'RO': _v('#002b7f', '#fcd116', '#ce1126'),
 'BE': _v('#000', '#fae042', '#ed2939'), 'IE': _v('#169b62', '#fff', '#ff883e'), 'NL': _h('#ae1c28', '#fff', '#21468b'), 'HU': _h('#ce2939', '#fff', '#477050'), 'PL': _h('#fff', '#dc143c'),
 'AT': _h('#ed2939', '#fff', '#ed2939'), 'RU': _h('#fff', '#0039a6', '#d52b1e'), 'BG': _h('#fff', '#00966e', '#d62612'), 'LU': _h('#ed2939', '#fff', '#00a1de'),
 'ES': '<rect width="60" height="40" fill="#aa151b"/><rect y="10" width="60" height="20" fill="#f1bf00"/>',
 'SE': '<rect width="60" height="40" fill="#006aa7"/><rect x="18" width="8" height="40" fill="#fecc00"/><rect y="16" width="60" height="8" fill="#fecc00"/>',
 'FI': '<rect width="60" height="40" fill="#fff"/><rect x="18" width="8" height="40" fill="#002f6c"/><rect y="16" width="60" height="8" fill="#002f6c"/>',
 'DK': '<rect width="60" height="40" fill="#c8102e"/><rect x="18" width="7" height="40" fill="#fff"/><rect y="16.5" width="60" height="7" fill="#fff"/>',
 'NO': '<rect width="60" height="40" fill="#ba0c2f"/><rect x="16" width="12" height="40" fill="#fff"/><rect y="14" width="60" height="12" fill="#fff"/><rect x="19" width="6" height="40" fill="#00205b"/><rect y="17" width="60" height="6" fill="#00205b"/>',
 'CZ': '<rect width="60" height="20" fill="#fff"/><rect y="20" width="60" height="20" fill="#d7141a"/><polygon points="0,0 30,20 0,40" fill="#11457e"/>',
 'SK': _h('#fff', '#0b4ea2', '#ee1c25'), 'SI': _h('#fff', '#005da4', '#ed1c24'), 'RS': _h('#c6363c', '#0c4076', '#fff'),
 'GB': '<rect width="60" height="40" fill="#012169"/><path d="M0,0 L60,40 M60,0 L0,40" stroke="#fff" stroke-width="8"/><path d="M0,0 L60,40 M60,0 L0,40" stroke="#c8102e" stroke-width="3"/><path d="M30,0 V40 M0,20 H60" stroke="#fff" stroke-width="12"/><path d="M30,0 V40 M0,20 H60" stroke="#c8102e" stroke-width="7"/>',
 'US': '<rect width="60" height="40" fill="#fff"/>' + ''.join(f'<rect y="{k*40/13:.2f}" width="60" height="{40/13+0.05:.2f}" fill="#b22234"/>' for k in range(0, 13, 2)) + '<rect width="24" height="21.6" fill="#3c3b6e"/>' + ''.join(f'<circle cx="{2.5 + (i % 6) * 3.8 + (1.9 if (i // 6) % 2 else 0):.1f}" cy="{2.4 + (i // 6) * 4.2:.1f}" r="0.9" fill="#fff"/>' for i in range(30) if not ((i // 6) % 2 and i % 6 == 5)),
 'CA': '<rect width="60" height="40" fill="#fff"/><rect width="15" height="40" fill="#d80621"/><rect x="45" width="15" height="40" fill="#d80621"/><polygon points="30,8 32.5,13.5 36,12 34.5,18 39,17 33,23 34,27 30,25.5 26,27 27,23 21,17 25.5,18 24,12 27.5,13.5" fill="#d80621"/>',
 'MX': _v('#006847', '#fff', '#ce1126') + '<circle cx="30" cy="20" r="4" fill="#8a6d3b"/>',
 'BR': '<rect width="60" height="40" fill="#009c3b"/><polygon points="30,4 54,20 30,36 6,20" fill="#ffdf00"/><circle cx="30" cy="20" r="9" fill="#002776"/>',
 'AR': _h('#74acdf', '#fff', '#74acdf') + '<circle cx="30" cy="20" r="3.5" fill="#f6b40e"/>',
 'JP': '<rect width="60" height="40" fill="#fff"/><circle cx="30" cy="20" r="12" fill="#bc002d"/>',
 'CN': '<rect width="60" height="40" fill="#de2910"/>' + _star(10, 10, 6, '#ffde00') + _star(20, 4, 2, '#ffde00') + _star(24, 8.5, 2, '#ffde00') + _star(24, 13.5, 2, '#ffde00') + _star(20, 17.5, 2, '#ffde00'),
 'VN': '<rect width="60" height="40" fill="#da251d"/>' + _star(30, 20, 12, '#ffff00'),
 'KR': '<rect width="60" height="40" fill="#fff"/><g transform="rotate(-33.7 30 20)"><path d="M20,20 A10,10 0 0 1 40,20 Z" fill="#cd2e3a"/><path d="M20,20 A10,10 0 0 0 40,20 Z" fill="#0047a0"/><circle cx="25" cy="20" r="5" fill="#cd2e3a"/><circle cx="35" cy="20" r="5" fill="#0047a0"/></g>' + _tri(11, 8.5, -33.7, (False, False, False)) + _tri(49, 8.5, 33.7, (True, False, True)) + _tri(11, 31.5, 33.7, (False, True, False)) + _tri(49, 31.5, -33.7, (True, True, True)),
 'TW': '<rect width="60" height="40" fill="#fe0000"/><rect width="30" height="20" fill="#000095"/><circle cx="15" cy="10" r="5" fill="#fff"/>',
 'IN': _h('#ff9933', '#fff', '#138808') + '<circle cx="30" cy="20" r="5" fill="none" stroke="#000080" stroke-width="1.5"/>',
 'TH': '<rect width="60" height="40" fill="#a51931"/><rect y="6.7" width="60" height="26.6" fill="#fff"/><rect y="13.3" width="60" height="13.4" fill="#2d2a4a"/>',
 'MY': '<rect width="60" height="40" fill="#fff"/>' + ''.join(f'<rect y="{k*40/14:.2f}" width="60" height="{40/14+0.05:.2f}" fill="#cc0001"/>' for k in range(0, 14, 2)) + '<rect width="30" height="22.9" fill="#010066"/><circle cx="12" cy="11.5" r="7" fill="#ffcc00"/><circle cx="14.5" cy="11.5" r="6" fill="#010066"/>' + _star(22, 11.5, 4, '#ffcc00'),
 'ID': _h('#ff0000', '#fff'), 'MC': _h('#ce1126', '#fff'), 'SG': _h('#ed2939', '#fff') + '<circle cx="12" cy="10" r="6" fill="#fff"/><circle cx="14.5" cy="10" r="5.3" fill="#ed2939"/>',
 'TR': '<rect width="60" height="40" fill="#e30a17"/><circle cx="24" cy="20" r="10" fill="#fff"/><circle cx="26.5" cy="20" r="8" fill="#e30a17"/>' + _star(37, 20, 5, '#fff', rot=180),
 'MA': '<rect width="60" height="40" fill="#c1272d"/>' + _star(30, 20, 11, 'none', stroke='#006233'),
 'CH': '<rect width="60" height="40" fill="#da291c"/><rect x="26.5" y="8" width="7" height="24" fill="#fff"/><rect x="18" y="16.5" width="24" height="7" fill="#fff"/>',
 'HR': _h('#ff0000', '#fff', '#171796') + '<rect x="24" y="12.5" width="12" height="15" fill="#fff"/>' + ''.join(f'<rect x="{24 + i*2.4:.1f}" y="{12.5 + j*3:.1f}" width="2.4" height="3" fill="#ff0000"/>' for i in range(5) for j in range(5) if (i + j) % 2 == 0),
 'PT': '<rect width="24" height="40" fill="#006600"/><rect x="24" width="36" height="40" fill="#ff0000"/><circle cx="24" cy="20" r="7" fill="#ffcc00"/><circle cx="24" cy="20" r="4" fill="#ff0000"/>',
 'ZA': '<rect width="60" height="40" fill="#fff"/><rect width="60" height="13.3" fill="#e03c31"/><rect y="26.7" width="60" height="13.3" fill="#001489"/><polygon points="0,0 24,20 0,40" fill="#000"/><polygon points="0,4 20,20 0,36 -8,36 -8,4" fill="#ffb81c"/><polygon points="10,0 60,0 60,10 25,20 60,30 60,40 10,40 0,33 0,7" fill="none"/><path d="M0,7 L21,20 L0,33" fill="none" stroke="#007749" stroke-width="7"/><path d="M14,0 L60,0 M14,40 L60,40" stroke="#007749" stroke-width="0"/><rect x="21" y="16.5" width="39" height="7" fill="#007749"/>',
 'UZ': _h('#1eb53a', '#fff', '#0099b5')[::-1] if False else _h('#0099b5', '#fff', '#1eb53a'), 'EG': _h('#ce1126', '#fff', '#000'), 'IR': _h('#239f40', '#fff', '#da0000'), 'KZ': '<rect width="60" height="40" fill="#00afca"/><circle cx="30" cy="20" r="7" fill="#fec50c"/>',
 'AE': '<rect width="60" height="40" fill="#fff"/><rect width="15" height="40" fill="#ff0000"/><rect x="15" width="45" height="13.3" fill="#00732f"/><rect x="15" y="26.7" width="45" height="13.3" fill="#000"/>', 'SA': '<rect width="60" height="40" fill="#006c35"/>',
 'AU': '<rect width="60" height="40" fill="#012169"/>' + _star(45, 20, 4, '#fff') + _star(42, 8, 2.2, '#fff') + _star(52, 14, 2.2, '#fff') + _star(50, 28, 2.2, '#fff') + _star(40, 32, 2.2, '#fff') + _star(15, 30, 5, '#fff'),
 'NZ': '<rect width="60" height="40" fill="#012169"/>' + ''.join(_star(x, y, 2.6, '#c8102e') for x, y in ((44, 10), (52, 17), (40, 22), (46, 30))),
}
def flag_svg_use(code, cls='fl'):
    if not code: return ''
    name = COUNTRY_NAME.get(code, code)
    if code in FLAG_SVG: return f'<svg class="{cls}" viewBox="0 0 60 40" role="img" aria-label="{E(name)}"><use href="#fl-{code.lower()}"/></svg>'
    return f'<span class="{cls} txt" role="img" aria-label="{E(name)}">{E(code)}</span>'
def country_text(cb):
    name = cb.get('country_name') or COUNTRY_NAME.get(cb.get('country'), cb.get('country'))
    org = (cb.get('origin') or '').split(' (')[0]
    parts = [name + (f' (marque of {org} origin)' if org and org != name else '')]
    if cb.get('hq'): parts.append('head office ' + cb['hq'] + (f" ({cb['hq_entity']})" if cb.get('hq_entity') else ''))
    bi = [COUNTRY_NAME.get(c, c) for c in (cb.get('built_in') or [])]
    if bi: parts.append('models for Europe built in ' + ', '.join(bi))
    t = ' · '.join(p for p in parts if p)
    if cb.get('note'): t += '. ' + cb['note'].strip().rstrip('.') + '.'
    if cb.get('confidence') == 'low': t += ' (not fully verified)'
    return t
CB = COUNTRIES.get('brands') or {}; CG = COUNTRIES.get('groups') or {}
flag_codes = sorted({c for cb in CB.values() for c in (cb.get('country'), cb.get('second_flag')) if c} | {cg.get('country') for cg in CG.values() if cg.get('country')})
flag_defs = ('<svg class="flagdefs" width="0" height="0" aria-hidden="true"><defs>' + ''.join(f'<symbol id="fl-{c.lower()}" viewBox="0 0 60 40">{FLAG_SVG[c]}</symbol>' for c in flag_codes if c in FLAG_SVG) + '</defs></svg>') if flag_codes else ''
def brand_flags(b):
    cb = CB.get(b) or {}
    if not cb.get('country'): return ''
    return f'<span class="flags" title="{E(country_text(cb))}">{flag_svg_use(cb["country"])}{flag_svg_use(cb.get("second_flag"), "fl sec") if cb.get("second_flag") else ""}</span>'
def group_flags(label):
    cg = CG.get(label) or {}
    if not cg.get('country'): return ''
    tip = (cg.get('country_name') or COUNTRY_NAME.get(cg['country'], cg['country'])) + ' · parent company ' + (cg.get('hq_entity') or label) + (', head office ' + cg['hq'] if cg.get('hq') else '')
    return f'<span class="flags" title="{E(tip)}">{flag_svg_use(cg["country"])}</span>'
flag_legend = f'<span>{flag_svg_use("DE")}Flag in the brand header: the country of the brand\'s head office (Wikipedia); a smaller second flag marks the one foreign country where its models for Europe are built. Hover a flag for the office and the plants; the group header carries the parent company\'s flag.</span>' if CB else ''

# ---------- matrix ----------
cells = []
col = 2
cells.append('<div class="corner hdr" style="grid-row:1/3;grid-column:1"><span>Class ↓ / Brand →</span></div>')
for gi, g in enumerate(groups):
    n = len(g['brands'])
    cells.append(f'<div class="ghdr hdr" data-group="{E(g["label"])}" style="grid-row:1;grid-column:{col}/{col+n}"><span>{E(g["label"])}{group_flags(g["label"])}</span></div>')
    for b in g['brands']:
        cells.append(f'<div class="bhdr hdr" data-group="{E(g["label"])}" data-brand="{E(b)}" style="grid-row:2;grid-column:{col}"><span class="bn">{E(b)}</span>{brand_flags(b)}</div>')
        col += 1
NCOL = col - 1
# Sub-row assignment (v1.12): within a class row every twin group gets a line of its own. All its members sit on that line
# (a brand with k members of one group stacks them on k consecutive lines, starting at the group's line) and no tile of
# another group, nor of a brand without a twin, is placed between the first and the last member on that line. Groups whose
# column spans do not overlap share a line. The order in which the groups claim lines is searched (fixed seed) for the
# arrangement with the fewest lines and the fullest top lines.
colidx = {b: i for i, b in enumerate(brands)}
def assign_subrows(rowcode):
    cols = {b: by_cell.get((rowcode, b), []) for b in brands}
    order = {m['id']: k for ms in cols.values() for k, m in enumerate(ms)}
    def by_brand(g):
        mb = defaultdict(list)
        for i in g['members']:
            if i in mid: mb[mid[i]['brand']].append(i)
        for b in mb: mb[b].sort(key=lambda i: order.get(i, 99))
        return mb
    ginfo = [(g, by_brand(g)) for g in DATA['twin_groups'] if g['row'] == rowcode]
    ginfo = [(g, mb) for g, mb in ginfo if mb]
    def place(seq):
        occ = defaultdict(set); sub = {}; spans = defaultdict(list); gcell = defaultdict(dict); home = {}
        for g, mb in seq:
            cs = [colidx[b] for b in mb]; c1, c2 = min(cs), max(cs); s = 0
            while True:   # lowest line whose span is free of foreign tiles and where every brand can stack its members through that line
                ok = not any(c1 < c < c2 for c in gcell[s]); blocks = {}
                if ok:
                    for b, ids in mb.items():
                        k = len(ids); col = colidx[b]; chosen = None
                        for u in range(k - 1, -1, -1):   # a brand's k members form a block of k lines through the family line; the highest free block wins (fills the top of the column)
                            top = s - u
                            if top < 0: continue
                            if all(l not in occ[b] and not any(a < col < z for (a, z, _) in spans[l]) for l in range(top, top + k)): chosen = top; break
                        if chosen is None: ok = False; break
                        blocks[b] = chosen
                if ok: break
                s += 1
            home[g['id']] = s; spans[s].append((c1, c2, g['id']))
            for b, ids in mb.items():
                for k, i in enumerate(ids): sub[i] = blocks[b] + k; occ[b].add(blocks[b] + k); gcell[blocks[b] + k][colidx[b]] = g['id']
        for b, ms in cols.items():
            for m in ms:
                if m['id'] in sub: continue
                c = colidx[b]; s = 0
                while s in occ[b] or any(a < c < z for (a, z, _) in spans[s]): s += 1
                sub[m['id']] = s; occ[b].add(s)
        return sub, home
    def score(sub):   # fewest lines, then fewest brand columns with an empty top cell, then the fullest top lines
        S = max(sub.values()) + 1 if sub else 1; cnt = [0] * S
        for v in sub.values(): cnt[v] += 1
        top = {mid[i]['brand'] for i, v in sub.items() if v == 0}
        holes = sum(1 for b, ms in cols.items() if ms and b not in top)
        return (S, holes, [-c for c in cnt])
    base_seq = sorted(ginfo, key=lambda x: (-len(x[1]), -sum(len(v) for v in x[1].values()), x[0]['slot'], x[0]['id']))
    rnd = random.Random(7); best = None
    for trial in range(301 if len(ginfo) > 1 else 1):
        seq = base_seq[:] if trial == 0 else rnd.sample(base_seq, len(base_seq))
        sub, home = place(seq); sc = score(sub)
        if best is None or sc < best[0]: best = (sc, sub, home)
    sc, sub, home = best
    bars = []; above = {}
    for g, mb in ginfo:
        s = home[g['id']]; cs = sorted(colidx[b] for b in mb)
        if len(cs) >= 2: bars.append((s, brands[cs[0]], brands[cs[-1]], g['id']))
        for b, ids in mb.items():
            for k in range(1, len(ids)): above[ids[k]] = ids[k - 1]
    return sub, (max(sub.values()) + 1 if sub else 1), bars, above

base = 3; sub_report = []
for ri, r in enumerate(rows):
    sub, S, bars, above = assign_subrows(r['code'])
    stack = max([len(by_cell.get((r['code'], b), [])) for b in brands] + [0])
    sub_report.append(f"{r['code']:12s} {S:2d} sub-rows (tallest brand stack {stack})")
    cells.append(f'<div class="rhdr hdr" data-row="{E(r["code"])}" data-sub="{S}" style="grid-row:{base}/{base+S};grid-column:1"><span class="rn">{E(r["name"])}</span><span class="rd">{E(r["desc"])}</span></div>')
    col = 2; tiles_html = []
    for g in groups:
        for b in g['brands']:
            ms = by_cell.get((r['code'], b), [])
            cells.append(f'<div class="cell{" empty" if not ms else ""}" data-row="{E(r["code"])}" data-brand="{E(b)}" data-group="{E(g["label"])}" style="grid-row:{base}/{base+S};grid-column:{col}"></div>')
            for m in ms: tiles_html.append(tile(m, sub[m['id']], f'grid-row:{base+sub[m["id"]]};grid-column:{col}', above.get(m['id'])))
            col += 1
    for s in range(1, S, 2):
        cells.append(f'<div class="stripe" data-row="{E(r["code"])}" data-s="{s}" style="grid-row:{base+s};grid-column:2/{NCOL+1}"></div>')
    for s, b1, b2, gid in bars:   # a bar in the family colour along the family's line, behind the tiles
        g = tgs[gid]; dashed = all(mid[i].get('twin_style') != 1 for i in g['members'] if i in mid)
        cells.append(f'<div class="gbar{" dashed" if dashed else ""}" data-row="{E(r["code"])}" data-s="{s}" data-g="{E(gid)}" style="grid-row:{base+s};grid-column:{colidx[b1]+2}/{colidx[b2]+3};--gc:var(--c{g["slot"]+1})"></div>')
    cells.extend(tiles_html)
    base += S
matrix = '\n'.join(cells)
print('\n'.join(sub_report))

# ---------- group chips for filters ----------
gchips = ''.join(f'<label class="fchip"><input type="checkbox" id="g-{i}" data-group="{E(g["label"])}" checked><span>{E(g["label"])}</span><small>{len(g["brands"])}</small></label>' for i, g in enumerate(groups))
rchips = ''.join(f'<label class="fchip"><input type="checkbox" id="r-{r["code"]}" data-row="{E(r["code"])}" checked><span>{E(r["name"])}</span></label>' for r in rows)
pt_count = {k: sum(1 for m in models if k in pt_keys(m.get('powertrains'))) for k, _ in PT_FILTER_LABEL}
pchips = ''.join(f'<label class="fchip"><input type="checkbox" id="p-{k}" data-pt="{k}" checked><span>{E(lab)}</span><small>{pt_count[k]}</small></label>' for k, lab in PT_FILTER_LABEL if pt_count[k])
dv_count = {k: sum(1 for m in models if k in drive_keys(m)) for k, _ in DRIVE_LABEL}
dchips = ''.join(f'<label class="fchip"><input type="checkbox" id="d-{k}" data-drive="{k}" checked><span>{E(lab)}</span><small>{dv_count[k]}</small></label>' for k, lab in DRIVE_LABEL if dv_count[k])
n_awd = sum(1 for m in models if (DRIVE.get(m['id']) or {}).get('awd'))

# ---------- twin list (text view) ----------
tl = []
for r in rows:
    gs = [g for g in DATA['twin_groups'] if g['row'] == r['code']]
    if not gs: continue
    items = ''
    for g in gs:
        mem = []
        for i in g['members']:
            m = mid[i]; st = m.get('twin_style')
            mem.append(f'<a href="#" class="tw{st}" data-id="{E(i)}">{E(full_name(m["brand"], m["display"]))}</a>')
        items += f'<li><span class="sw" style="--gc:var(--c{g["slot"]+1})"></span><b>{E(g["label"])}</b>: ' + ', '.join(mem) + '</li>'
    tl.append(f'<h4>{E(r["name"])}</h4><ul class="twinlist">{items}</ul>')
twinlist = '\n'.join(tl)

# ---------- sources ----------
src_by_agent = defaultdict(list)
for s in DATA.get('sources', []):
    src_by_agent[s.get('agent','')].append(s)
srcs = ''
AGENT_LABEL = {'vw-group':'Volkswagen Group','stellantis':'Stellantis','renault-alliance':'Renault, Nissan and Mitsubishi','mercedes-bmw':'Mercedes-Benz Group and BMW Group','japan':'Japanese brands','hyundai-ford-gm-tesla':'Hyundai Motor Group, Ford, GM and Tesla','jlr-independents':'JLR and independent makers','geely':'Geely Holding','china-other':'Other Chinese brands','lcv':'Vans, MPVs and pickups','verify-additions':'Verification pass','verify':'Verification pass'}
for a, ss in sorted(src_by_agent.items(), key=lambda x: AGENT_LABEL.get(x[0], x[0])):
    srcs += f'<details><summary>{E(AGENT_LABEL.get(a, a))} ({len(ss)})</summary><ul>' + ''.join(f'<li><a href="{E(s.get("url",""))}" target="_blank" rel="noopener">{E(s.get("what") or s.get("url",""))}</a></li>' for s in ss) + '</ul></details>'

if CB:
    cs = sorted({u for cb in list(CB.values()) + list(CG.values()) for u in (cb.get('sources') or [])})
    srcs += f'<details><summary>Brand countries: head offices and plants ({len(cs)})</summary><p>Checked on {E(COUNTRIES.get("checked_on", ""))}. The flag shows the country of the brand\'s head office; a second flag the single foreign country that builds its models for Europe.</p><ul>' + ''.join(f'<li><a href="{E(u)}" target="_blank" rel="noopener">{E(u.replace("https://", ""))}</a></li>' for u in cs) + '</ul></details>'
meta = DATA['meta']
n_t1 = sum(1 for m in models if m.get('twin_style') == 1)
n_t2 = sum(1 for m in models if m.get('twin_style') == 2)
INTERNAL = re.compile(r"carsized|commons|fetch|budget|verif|slug|guess|researcher|\bagent|scope file|\bbrief\b|merge option|coordinator|builder|i-record|file name|not fetched|todo|\[merge|optional tile|see fields|central decision|decide centrally|harmonise centrally|low priority|judgement call:|\bkey\b", re.I)
def clean_note(t):
    if not t or not isinstance(t, str): return t
    parts = re.split(r"(?<=[.!?])\s+", t.strip())
    keep = [p for p in parts if p and not INTERNAL.search(p)]
    out = ' '.join(keep).strip()
    out = re.sub(r"^\(?FACTORY CAMPER\)?\.?\s*", "", out)
    return out or None
for m in models:
    for k in ('notes', 'status_note', 'twin_note'):
        m[k] = clean_note(m.get(k))

# ---------- announced (coming) and recently discontinued lists ----------
rowname = {r['code']: r['name'] for r in rows}
def _bm(x): return full_name(x.get('brand', '') or '', x.get('model', '') or '').strip()
coming_items = []
for a in sorted(DATA.get('announced', []), key=lambda x: (_bm(x).lower())):
    note = clean_note(a.get('status_note') or a.get('note') or '')
    rn = rowname.get(a.get('row'), '')
    coming_items.append(f"<li><b>{E(_bm(a))}</b>{(' <small>' + E(rn) + '</small>') if rn else ''}{(' — ' + E(note)) if note else ''}</li>")
coming = f'<h2>Announced for Europe, not yet orderable ({len(coming_items)})</h2><p>Shown here for context only; these models are not in the chart.</p><details><summary>Show the list</summary><ul class="plain">' + ''.join(coming_items) + '</ul></details>' if coming_items else ''
seen_gone = set(); gone_items = []
for g in sorted(DATA.get('discontinued', []), key=lambda x: _bm(x).lower()):
    k = _bm(g).lower()
    if not k or k in seen_gone: continue
    seen_gone.add(k)
    note = clean_note(g.get('note') or g.get('status_note') or '')
    gone_items.append(f"<li><b>{E(_bm(g))}</b>{(' — ' + E(note)) if note else ''}</li>")
gone = f'<h2>Recently discontinued or withdrawn from Europe ({len(gone_items)})</h2><p>Models that were on sale in 2024–2026 but could no longer be ordered new in October 2026.</p><details><summary>Show the list</summary><ul class="plain">' + ''.join(gone_items) + '</ul></details>' if gone_items else ''
dims_out = {}
for m in models:
    dd = DIMS.get(m['id'])
    if dd and dd.get('len'):
        dims_out[m['id']] = {k: dd.get(k) for k in ('len', 'wid', 'widm', 'hei', 'wb', 'gc', 'kg', 'slug')}
        dims_out[m['id']]['label'] = cs_label(dd.get('slug'))
        if FLAGS.get('img_notes', {}).get(m['id']): dims_out[m['id']]['note'] = FLAGS['img_notes'][m['id']]
# ---------- measurement check (text) ----------
CAT_LABEL = {'ok': 'consistent', 'variant': 'different body-length versions on carsized', 'convention': 'width quoted with or without folded mirrors', 'design': 'design differences (bumpers, roof rails, ride height)', 'info': 'notes', 'check': 'to be reviewed', 'prev': 'pairings where carsized has only the previous model of one vehicle (not comparable)'}
def mc_name(i): return E(full_name(mid[i]['brand'], mid[i]['display'])) if i in mid else E(i)
mc_sum = FLAGS.get('summary', {}); mc_edges = FLAGS.get('edges', [])
mc_items = defaultdict(list)
for e in mc_edges:
    if e['cat'] != 'ok': mc_items[e['cat']].append(e)
def mc_li(e):
    return (f'<li><b><a href="#" data-id="{E(e["a"])}">{mc_name(e["a"])}</a> ↔ <a href="#" data-id="{E(e["b"])}">{mc_name(e["b"])}</a></b> '
            f'<small>({"same body" if e["tier"] == 1 else "platform siblings"}; Δ wheelbase {e["d_wb"]}, length {e["d_len"]}, width {e["d_wid"]}, height {e["d_hei"]} mm)</small> — {E(e["text"])}.</li>')
if mc_edges:
    t1, t2 = FLAGS.get('tolerances', {}).get('tier1', {}), FLAGS.get('tolerances', {}).get('tier2', {})
    meascheck = (f'<p>Every pairing in the chart was tested against the carsized.com measurements of both vehicles. {mc_sum.get("models_measured", 0)} of {len(models)} models have a carsized entry, so {mc_sum.get("checked", 0)} of the {mc_sum.get("edges", 0)} pairings could be measured on both sides. '
                 f'Same-body pairs (solid frames) must agree in wheelbase (±{t1.get("wb")} mm), width (±{t1.get("wid")} mm), height (±{t1.get("hei")} mm) and length (±{t1.get("len")} mm); platform siblings (dashed frames) have their own bodies, so only a wheelbase gap above {t2.get("wb")} mm or a width gap above {t2.get("wid")} mm would contradict a shared platform. '
                 f'Where a same-body pair exceeds a tolerance, the reason is given: usually carsized lists a different body-length version of one of the two vehicles, or quotes the width with folded mirrors for one and the bare body for the other. Each tile\'s detail panel shows the measured values and the differences to its relatives.</p>')
    counts = mc_sum.get('cats', {})
    meascheck += '<p class="mc-sum">' + ' · '.join(f'<b>{v}</b> {E(CAT_LABEL.get(k, k))}' for k, v in sorted(((k, v) for k, v in counts.items() if k != 'prev'), key=lambda x: -x[1])) + '</p>'
    if counts.get('prev'):
        meascheck += f'<p>{counts["prev"]} further pairings involve a vehicle that is pictured with its previous model (tile badge with that model’s year) because carsized has no entry for the current generation; these pairings are listed but not checked.</p>'
    for cat in ('check', 'variant', 'convention', 'design', 'info', 'prev'):
        if mc_items.get(cat):
            meascheck += f'<details class="mc"{" open" if cat == "check" else ""}><summary>{E(CAT_LABEL[cat][0].upper() + CAT_LABEL[cat][1:])} ({len(mc_items[cat])})</summary><ul class="plain">' + ''.join(mc_li(e) for e in mc_items[cat]) + '</ul></details>'
    lc = FLAGS.get('length_check', [])
    if lc:
        meascheck += (f'<details class="mc"><summary>Chart length vs carsized entry ({len(lc)})</summary><p>Models whose researched length differs from the pictured carsized version by more than 60 mm, mostly because carsized lists the long-body version of a van.</p><ul class="plain">'
                      + ''.join(f'<li><a href="#" data-id="{E(x["id"])}">{mc_name(x["id"])}</a>: chart {x["chart"]:,} mm, carsized {x["carsized"]:,} mm ({E(cs_label(x["slug"]))})</li>' for x in lc) + '</ul></details>')
else:
    meascheck = '<p>No measurements loaded.</p>'
data_json = json.dumps({'ext': {i: {k: {kk: v.get(kk) for kk in ('page', 'source', 'licence', 'notes', 'angle')} for k, v in e.items() if isinstance(v, dict)} for i, e in EXT.items()}, 'models': {m['id']: {k: m.get(k) for k in ('brand','model','display','row','group','body','generation','length_mm','platform','powertrains','status','status_note','status_sources','ch_on_sale','ch_source','other_names','twin_group','twin_style','twin_note','twin_sources','carsized_slug','notes','cross_row_siblings')} for m in models},
                        'drive': {i: {k: v.get(k) for k in ('drives', 'awd', 'awd_term', 'note', 'confidence', 'source')} for i, v in DRIVE.items() if isinstance(v, dict)},
                        'groups': {g['id']: g for g in DATA['twin_groups']},
                        'rows': {r['code']: r['name'] for r in rows},
                        'countries': {b: {k: cb.get(k) for k in ('country', 'country_name', 'origin', 'hq', 'hq_entity', 'built_in', 'second_flag', 'note', 'confidence', 'sources')} for b, cb in CB.items()}, 'country_names': COUNTRY_NAME, 'flag_codes': [c for c in flag_codes if c in FLAG_SVG],
                        'dims': dims_out, 'check': {'edges': FLAGS.get('edges', []), 'groups': FLAGS.get('groups', {})}}, ensure_ascii=False)

page = f'''<meta charset="utf-8">
<title>Identical Car Chart</title>
<script>/* side pictures that are not published as single files (artifact file limit) come from img/sides.json */
window.__sidePack = null;
window.sideFallback = async function (im) {{ try {{ if (!window.__sidePack) window.__sidePack = fetch('img/sides.json').then(r => {{ if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }}); const idx = await window.__sidePack; const b64 = idx[im.dataset.sid]; if (b64) {{ im.onerror = null; im.src = 'data:image/webp;base64,' + b64; return; }} }} catch (e) {{ console.warn('side pack not available', e); }} im.dataset.packFailed = '1'; im.dispatchEvent(new Event('error')); }};
</script>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500;600;700&display=swap">
<style>
/* Layout: a sticky-headed matrix (brands × classes) with image tiles; twin groups framed in categorical hues. */
:root {{
  --bg:#f4f4f1; --surface:#fcfcfb; --surface-2:#ebebe6; --fg:#15171a; --fg-2:#4f524f; --muted:#86877f;
  --line:#dcdcd5; --line-2:#c5c5bd; --accent:#1f2a44; --accent-fg:#ffffff; --tilebg:#ffffff; --imgbg:#ffffff;
  --c1:#2a78d6; --c2:#eb6834; --c3:#1baf7a; --c4:#eda100; --c5:#e87ba4; --c6:#008300; --c7:#6250d6; --c8:#e34948;
  --warn:#b26a00; --off:#86877f; --awd:#2a6f3a;
  --display:"Barlow Condensed","Arial Narrow","Helvetica Neue",Arial,sans-serif;
  --body:"Barlow","Helvetica Neue",Arial,sans-serif;
  --colw:156px; --tileh:auto; --imgratio:2.3;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#141517; --surface:#1b1d20; --surface-2:#24272b; --fg:#ecece8; --fg-2:#bdbdb6; --muted:#8c8d86;
  --line:#2d3034; --line-2:#3b3e43; --accent:#d6deef; --accent-fg:#15171a; --tilebg:#1f2125; --imgbg:#f3f3ef;
  --c1:#3987e5; --c2:#d95926; --c3:#199e70; --c4:#c98500; --c5:#d55181; --c6:#008300; --c7:#9085e9; --c8:#e66767;
  --warn:#e0a24a; --off:#8c8d86; --awd:#7fd08f; color-scheme:dark }} }}
:root[data-theme="dark"] {{
  --bg:#141517; --surface:#1b1d20; --surface-2:#24272b; --fg:#ecece8; --fg-2:#bdbdb6; --muted:#8c8d86;
  --line:#2d3034; --line-2:#3b3e43; --accent:#d6deef; --accent-fg:#15171a; --tilebg:#1f2125; --imgbg:#f3f3ef;
  --c1:#3987e5; --c2:#d95926; --c3:#199e70; --c4:#c98500; --c5:#d55181; --c6:#008300; --c7:#9085e9; --c8:#e66767;
  --warn:#e0a24a; --off:#8c8d86; --awd:#7fd08f; color-scheme:dark }}
* {{ box-sizing:border-box }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--body); font-size:14px; line-height:1.45; margin:0;
  padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:0 32px }}
body::before {{ content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top,0px); z-index:10; background:var(--bg) }}
h1,h2,h3,h4 {{ font-family:var(--display); text-wrap:balance; margin:0; line-height:1.1 }}
h1 {{ font-size:clamp(28px,4vw,42px); font-weight:700; letter-spacing:.01em }}
h2 {{ font-size:22px; font-weight:600; margin-block:28px 8px }}
h4 {{ font-size:16px; font-weight:600; margin-block:14px 4px }}
a {{ color:inherit }}
.top {{ display:flex; flex-wrap:wrap; gap:8px 32px; align-items:end; padding-block:22px 10px; max-width:1200px }}
.lede {{ margin:0; max-width:62ch; color:var(--fg-2); font-size:15px }}
.meta {{ display:flex; flex-wrap:wrap; gap:6px 18px; font-size:12.5px; color:var(--muted); text-transform:uppercase; letter-spacing:.06em; font-family:var(--display); font-weight:600 }}
.meta b {{ color:var(--fg) }}
.panel {{ background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:12px 14px; margin-block:10px }}
.legend {{ display:flex; flex-wrap:wrap; gap:10px 22px; align-items:center; font-size:13px; color:var(--fg-2) }}
.legend .ex {{ display:inline-block; width:34px; height:20px; border-radius:5px; vertical-align:middle; margin-right:6px; background:var(--tilebg) }}
.legend .ex.t1 {{ border:2.5px solid var(--c1) }}
.legend .ex.t2 {{ border:2.5px dashed var(--c3) }}
.legend .ex.t0 {{ border:1px solid var(--line-2) }}
.controls {{ display:flex; flex-wrap:wrap; gap:10px 18px; align-items:flex-start }}
.controls fieldset {{ border:0; padding:0; margin:0; min-width:0 }}
.controls legend {{ font-family:var(--display); font-weight:600; text-transform:uppercase; letter-spacing:.07em; font-size:11.5px; color:var(--muted); margin-bottom:5px; padding:0 }}
.chips {{ display:flex; flex-wrap:wrap; gap:4px }}
.fchip {{ display:inline-flex; align-items:center; gap:5px; border:1px solid var(--line-2); border-radius:999px; padding:2px 9px 2px 6px; font-size:12.5px; cursor:pointer; background:var(--surface); user-select:none }}
.fchip:has(input:checked) {{ background:var(--accent); color:var(--accent-fg); border-color:var(--accent) }}
.fchip input {{ margin:0; width:12px; height:12px; accent-color:var(--accent) }}
.fchip small {{ opacity:.7 }}
.btn {{ font:inherit; font-size:12.5px; border:1px solid var(--line-2); background:var(--surface); color:var(--fg); border-radius:6px; padding:3px 9px; cursor:pointer }}
.btn:hover {{ border-color:var(--fg-2) }}
.seg {{ display:inline-flex; border:1px solid var(--line-2); border-radius:6px; overflow:hidden }}
.seg label {{ font-size:12.5px; padding:3px 9px; cursor:pointer; background:var(--surface) }}
.seg label:has(input:checked) {{ background:var(--accent); color:var(--accent-fg) }}
.seg input {{ position:absolute; opacity:0; width:0; height:0 }}
.tog {{ display:inline-flex; align-items:center; gap:6px; font-size:13px; cursor:pointer }}
.search {{ font:inherit; font-size:13px; padding:4px 8px; border:1px solid var(--line-2); border-radius:6px; background:var(--surface); color:var(--fg); min-width:200px }}
:focus-visible {{ outline:2px solid var(--c1); outline-offset:2px }}

/* ---- matrix ---- */
.mwrap {{ overflow:auto; border:1px solid var(--line); border-radius:10px; background:var(--surface); max-height:calc(100vh - 40px); position:relative; margin-top:12px }}
.matrix {{ display:grid; grid-auto-rows:auto; font-size:12px; min-width:max-content }}
.hdr {{ position:sticky; background:var(--surface-2); z-index:3; display:flex; flex-direction:column; justify-content:center; border-bottom:1px solid var(--line); border-right:1px solid var(--line) }}
.ghdr {{ top:0; height:30px; padding:0 8px; font-family:var(--display); font-weight:700; font-size:14px; letter-spacing:.02em; text-transform:uppercase; border-right:2px solid var(--line-2); overflow:hidden; white-space:nowrap }}
.ghdr span {{ position:sticky; left:180px }}
.bhdr {{ top:30px; height:34px; padding:0 8px; font-family:var(--display); font-weight:600; font-size:15px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis }}
.rhdr {{ left:0; width:170px; padding:8px 10px; z-index:2; border-right:2px solid var(--line-2); justify-content:flex-start }}
.rhdr .rn {{ font-family:var(--display); font-weight:700; font-size:16px; line-height:1.1 }}
.rhdr .rd {{ color:var(--muted); font-size:11.5px; line-height:1.25; margin-top:3px }}
.corner {{ left:0; top:0; z-index:5; width:170px; padding:8px 10px; border-right:2px solid var(--line-2); color:var(--muted); font-size:11px; text-transform:uppercase; letter-spacing:.06em; font-family:var(--display); font-weight:600 }}
.cell {{ border-bottom:1px solid var(--line); border-right:1px solid var(--line) }}
.stripe {{ background:color-mix(in srgb, var(--fg) 4%, transparent); pointer-events:none }}
.gbar {{ position:relative; z-index:0; pointer-events:none }}
.gbar::before {{ content:""; position:absolute; left:calc(var(--colw) / 2); right:calc(var(--colw) / 2); top:50%; height:8px; margin-top:-4px; border-radius:4px; background:color-mix(in srgb, var(--gc) 45%, transparent) }}
.gbar.dashed::before {{ background:repeating-linear-gradient(90deg, color-mix(in srgb, var(--gc) 45%, transparent) 0 14px, transparent 14px 22px) }}
.gbar.lit::before {{ background:color-mix(in srgb, var(--gc) 85%, transparent) }}
.gbar.dashed.lit::before {{ background:repeating-linear-gradient(90deg, color-mix(in srgb, var(--gc) 85%, transparent) 0 14px, transparent 14px 22px) }}
.matrix.focus .gbar:not(.lit) {{ opacity:.2 }}
.tile.stack::before {{ content:""; position:absolute; top:-10px; left:50%; width:8px; height:8px; margin-left:-4px; background:color-mix(in srgb, var(--gc) 45%, transparent) }}
.tile.t1.stack::before, .tile.t2.stack::before {{ top:-10.5px }}
.tile.stack.lit::before {{ background:color-mix(in srgb, var(--gc) 85%, transparent) }}
.bhdr {{ flex-direction:row; align-items:center; justify-content:space-between; gap:6px }}
.bhdr .bn {{ overflow:hidden; text-overflow:ellipsis; white-space:nowrap; min-width:0 }}
.flagdefs {{ position:absolute; width:0; height:0; overflow:hidden }}
.flags {{ flex:none; display:inline-flex; align-items:center; gap:3px; vertical-align:middle }}
.fl {{ display:block; width:21px; height:14px; border-radius:2px; box-shadow:0 0 0 1px color-mix(in srgb, var(--fg) 22%, transparent); flex:none }}
.fl.sec {{ width:16px; height:11px }}
.fl.txt {{ font:700 9px/14px var(--display); text-align:center; background:var(--surface); color:var(--fg-2); letter-spacing:.04em }}
.ghdr .flags {{ display:inline-flex; margin-left:6px }}
.ghdr .fl {{ width:18px; height:12px }}
.legend .fl, .detail .fl {{ display:inline-block; vertical-align:-2px; margin-right:4px }}
.detail .sub.ctry {{ text-transform:none; letter-spacing:0; font-family:var(--body); font-weight:400; font-size:12.5px; line-height:1.4; color:var(--fg-2); margin-top:4px }}
.cell.last-in-group {{ border-right:2px solid var(--line-2) }}
.cell.empty {{ background:repeating-linear-gradient(135deg, transparent 0 6px, var(--surface-2) 6px 7px) }}
.tile {{ position:relative; z-index:1; display:flex; flex-direction:column; gap:3px; width:calc(var(--colw) - 10px); margin:4px 5px; text-align:left; font:inherit; color:inherit; background:var(--tilebg); border:2px solid var(--line); border-radius:8px; padding:4px; cursor:pointer; transition:opacity .15s, box-shadow .15s }}
.tile.t1 {{ border-color:var(--gc); border-width:2.5px; padding:3.5px }}
.tile.t2 {{ border-color:var(--gc); border-style:dashed; border-width:2.5px; padding:3.5px }}
.tile:hover, .tile.lit {{ box-shadow:0 0 0 3px color-mix(in srgb, var(--gc, var(--accent)) 35%, transparent) }}
.matrix.focus .tile:not(.lit) {{ opacity:.28 }}
.tile.hit {{ box-shadow:0 0 0 3px var(--c4) }}
.tile .img {{ display:block; aspect-ratio:var(--imgratio); width:100%; max-width:100%; background:var(--imgbg); border-radius:4px; overflow:hidden; position:relative }}
.tile img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:contain; display:block; transition:width .2s }}
.tile img.v-front {{ display:none }}
.view-front .tile img.v-front {{ display:block }}
.view-front .tile img.v-side {{ display:none }}
.view-front .tile.nofront img.v-side {{ display:block }}
.view-front .tile .img {{ aspect-ratio:1.5 }}
.tile .img.missing img {{ display:none }}
.tile .noimg {{ position:absolute; inset:0; display:grid; place-items:center; color:#6b6c66; font-family:var(--display); font-weight:600; font-size:13px; text-align:center; padding:4px }}
.tile .name {{ font-weight:600; font-size:12.5px; line-height:1.15; color:var(--fg) }}
.tile .tags {{ display:flex; flex-wrap:wrap; gap:3px }}
.tag {{ font-family:var(--display); font-weight:600; font-size:10px; letter-spacing:.04em; color:var(--fg-2); background:var(--surface-2); border-radius:3px; padding:0 4px; line-height:15px }}
.tag.warn {{ color:var(--warn); background:transparent; border:1px solid var(--warn) }}
.tag.off {{ color:var(--off); background:transparent; border:1px dashed var(--off) }}
.tag.awd {{ color:var(--awd); background:transparent; border:1px solid var(--awd) }}
.legend .tag {{ display:inline-block; vertical-align:middle; margin-right:6px }}
.chip {{ position:absolute; top:-2px; left:-2px; z-index:1; background:var(--gc); color:#fff; font-family:var(--display); font-weight:700; font-size:10.5px; letter-spacing:.03em; padding:1px 6px; border-radius:7px 0 7px 0; max-width:85%; overflow:hidden; text-overflow:ellipsis; white-space:nowrap }}
.tile.t2 .chip {{ background:var(--tilebg); color:var(--gc); border:1.5px dashed var(--gc); padding:0 5px }}
.yr {{ font-family:var(--display); font-weight:600; font-size:9.5px; letter-spacing:.03em; color:var(--fg-2); background:var(--surface-2); border:1px solid var(--line-2); border-radius:3px; padding:0 4px; line-height:14px; white-space:nowrap }}
.tile .yr {{ position:absolute; right:2px; bottom:2px; z-index:1 }}
.chk.prev {{ color:var(--muted) }}
.legend .yr-lg {{ position:static; display:inline-block; vertical-align:middle; margin-right:6px }}
.compact {{ --colw:118px }}
.compact .tile .name {{ font-size:11px }}
.compact .tile .tags {{ display:none }}
.compact .tile {{ width:calc(var(--colw) - 6px); margin:3px 3px }}
.scale .tile img {{ left:0; right:auto; top:auto; bottom:0; height:auto; max-height:100%; width:var(--sc,100%) }}
.hidetags .tile .tags {{ display:none }}
.hide {{ display:none !important }}

/* ---- detail panel ---- */
.detail {{ position:fixed; right:max(12px, env(safe-area-inset-right,0px)); bottom:max(12px, env(safe-area-inset-bottom,0px)); width:min(420px, calc(100vw - 24px)); max-height:min(70vh, 640px); overflow:auto; background:var(--surface); border:1px solid var(--line-2); border-radius:12px; box-shadow:0 12px 40px rgba(0,0,0,.25); padding:14px 16px; z-index:20; font-size:13px }}
.detail h3 {{ font-size:22px; margin-bottom:2px }}
.detail .sub {{ color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.06em; font-family:var(--display); font-weight:600 }}
.detail dl {{ display:grid; grid-template-columns:auto 1fr; gap:3px 12px; margin:10px 0 }}
.detail dt {{ color:var(--muted) }}
.detail dd {{ margin:0 }}
.detail .close {{ position:absolute; top:8px; right:8px }}
.detail ul {{ padding-left:18px; margin:4px 0 }}
.detail .twins a {{ cursor:pointer }}
.detail .srcs a {{ display:block; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; color:var(--fg-2) }}
.detail .srcs span {{ display:block }} .detail .srcs span a {{ display:inline; white-space:normal }} .detail .srcs small {{ display:block; color:var(--muted); margin-top:2px }}
.detail .meas {{ color:var(--fg-2) }}
.detail .meas small, .chk {{ color:var(--muted); font-size:11.5px }}
.chk {{ white-space:nowrap; cursor:help }}
.chk.check {{ color:var(--warn); font-weight:600 }}
.chk.ok {{ color:var(--c3) }}
.mc-sum {{ color:var(--fg-2) }}
details.mc {{ margin-block:6px }}
details.mc li {{ margin-block:4px }}
details.mc small {{ color:var(--muted) }}
.sw {{ display:inline-block; width:12px; height:12px; border-radius:3px; background:var(--gc); margin-right:6px; vertical-align:-1px }}
.twinlist {{ columns:2; column-gap:28px; padding-left:0; list-style:none; margin:0; font-size:13px }}
.twinlist li {{ break-inside:avoid; margin-bottom:5px }}
.twinlist a.tw1 {{ text-decoration-style:solid }}
.twinlist a.tw2 {{ text-decoration-style:dashed; color:var(--fg-2) }}
.notes {{ max-width:900px; font-size:14px }}
.notes p, .notes li {{ max-width:70ch }}
.notes ul.plain {{ padding-left:18px }} .notes ul.plain li {{ margin:4px 0 }} .notes ul.plain small {{ color:var(--muted); margin-left:6px }}
details summary {{ cursor:pointer; font-weight:600 }}
@media (max-width:700px) {{ .twinlist {{ columns:1 }} .mwrap {{ max-height:none }} .rhdr, .corner {{ width:120px }} .ghdr span {{ left:130px }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ transition:none !important }} }}
</style>

<header class="top">
  <div>
    <h1>Identical Car Chart</h1>
    <p class="lede">Every car and van up to 3.5 t that can be ordered new in Europe in October 2026, sorted by brand and vehicle class. Vehicles that are the same car under different badges share a coloured frame.</p>
  </div>
  <div class="meta"><span>Market <b>Europe · Swiss names</b></span><span>Checked <b>{E(meta.get('checked_on',''))}</b></span><span>Models <b>{len(models)}</b></span><span>Twin groups <b>{len(DATA['twin_groups'])}</b></span><span>Rebadged <b>{n_t1}</b> · siblings <b>{n_t2}</b></span><span>Version <b>{CHART_VERSION}</b></span></div>
</header>

<section class="panel">
  <div class="legend">
    <span><i class="ex t1"></i>Solid frame + chip: same vehicle under another badge (rebadge / twin)</span>
    <span><i class="ex t2"></i>Dashed frame: same platform, different body (platform sibling)</span>
    <span><i class="ex t0"></i>Plain: no twin on sale in Europe</span>
    <span>Same colour within a row = same family. Each family has a line of its own, joined by a bar in its colour, and nothing else sits between its members on that line; a brand with two members of one family stacks the second below the first (short stub). Hover a tile to light up its relatives; click for details and sources.</span>
    {flag_legend}
    <span><span class="yr yr-lg">2025 model</span> carsized.com has no picture of the current generation, so the tile shows the newest previous model it has; the badge gives that model’s year.</span>
    <span><span class="tag awd">AWD</span> Sold with all-wheel drive or 4x4 in at least one version ({n_awd} models); the detail panel names the manufacturer's term and the versions it is limited to.</span>
  </div>
</section>

<section class="panel controls" id="controls">
  <fieldset><legend>Ownership groups <button class="btn" type="button" id="g-all">all</button> <button class="btn" type="button" id="g-none">none</button></legend><div class="chips">{gchips}</div></fieldset>
  <fieldset><legend>Vehicle classes <button class="btn" type="button" id="r-all">all</button> <button class="btn" type="button" id="r-none">none</button></legend><div class="chips">{rchips}</div></fieldset>
  <fieldset><legend>Powertrain <button class="btn" type="button" id="p-all">all</button> <button class="btn" type="button" id="p-none">none</button></legend><div class="chips">{pchips}</div></fieldset>
  <fieldset><legend>Drive <button class="btn" type="button" id="d-all">all</button> <button class="btn" type="button" id="d-none">none</button></legend><div class="chips">{dchips}</div></fieldset>
  <fieldset><legend>View</legend>
    <div class="chips">
      <span class="seg"><label><input type="radio" name="view" id="view-side" value="side" checked>Side view</label><label><input type="radio" name="view" id="view-front" value="front">Front view</label></span>
      <span class="seg"><label><input type="radio" name="size" id="size-normal" value="normal" checked>Normal</label><label><input type="radio" name="size" id="size-compact" value="compact">Compact</label></span>
      <label class="tog"><input type="checkbox" id="only-twins"> Only vehicles with a twin or sibling</label>
      <label class="tog"><input type="checkbox" id="show-t2" checked> Show platform siblings</label>
      <span class="seg" title="Size the pictures to each other: by real length in the side view, by real width in the front view; the largest vehicle of the class (or of the whole chart) fills its tile"><label><input type="radio" name="scale" id="scale-fill" value="fill" checked>Fill tile</label><label><input type="radio" name="scale" id="scale-row" value="row">To scale in class</label><label><input type="radio" name="scale" id="scale-global" value="global">To scale globally</label></span>
      <input class="search" id="search" type="search" placeholder="Find a model…" aria-label="Find a model">
    </div>
  </fieldset>
</section>

{flag_defs}
<div class="mwrap" id="mwrap"><div class="matrix" id="matrix" style="grid-template-columns:170px repeat({NCOL-1}, var(--colw))">
{matrix}
</div></div>

<aside class="detail" id="detail" hidden></aside>

<section class="notes">
  <h2>How to read the chart</h2>
  <p>Columns are brands, grouped under the company that owns them (joint ventures and alliance partners are noted in the group header). Rows are vehicle classes, roughly by length and body type; the Swiss market name is used where a model is sold under several names in Europe. One tile is one nameplate: body styles, trims and performance versions are not split out.</p>
  <p>A coloured frame marks a family. A solid frame with a filled chip means the vehicle shares its body shell with the other solid tiles of that colour in the same row and is essentially the same car with different badges and fascias (for example the Renault Kangoo, Mercedes-Benz Citan and Nissan Townstar). A dashed frame means the vehicle shares the platform and much of its technology but has its own body (for example the VW Golf, SEAT Leon, Škoda Octavia and Audi A3). Within a class, every family has a line of its own: its members sit on that line, joined by a bar in the family colour, and no other vehicle is placed between them, so a family can be read straight across the brand columns (families whose brands lie in different parts of the chart share a line). A brand with two members of one family, such as the Volkswagen ID.4 and ID.5, stacks the second directly below the first. Colours repeat between rows; only tiles in the same row and colour belong together.</p>
  <p>Scope: four-wheeled vehicles with a permissible gross weight up to 3.5 t, from city cars to Sprinter-sized vans and pickups, that a customer could order new from an official European sales network in October 2026. "Run-out" marks models whose order books are closed or closing while stock is still sold. "Not in CH" marks models sold elsewhere in Europe but not in Switzerland at the time of checking.</p>
  <h2>Twin groups by class</h2>
  {twinlist}
  <h2>Measurement check</h2>
  {meascheck}
  {coming}
  {gone}
  <h2>Sources and method</h2>
  <p>Line-ups were compiled from the brands' official Swiss and German model pages and press releases, then cross-checked against European trade press and verified a second time by an independent pass. Twin and platform relationships cite manufacturer statements or trade-press reporting; each tile's sources are listed in its detail panel. In October 2026 every unframed tile was checked once more against the other brands in the chart; that check added the CMF-B Dacias, the Kia EV3/EV4/EV5 and Hyundai Ioniq 3, Polestar 4, Jaecoo 5, Omoda 9 and the Lotus–Zeekr pairs to their families, took the Changan-based DR 5 out of the Chery family and corrected 25 platform descriptions; a plausibility check on 27 October 2026 then moved the EV3, EV5 and Ioniq 3 out of the E-GMP family into the K3 and N3 families of the Kona and Tucson and their Kia twins, following Hyundai's own Ioniq 3 press kit (400 V, front-wheel drive). Where a model's platform relatives sit in other vehicle classes, the detail panel lists them. Images and the measurements of the measurement check are from <a href="https://www.carsized.com/" target="_blank" rel="noopener">carsized.com</a> (the pictured version is named in each detail panel). Where carsized has no entry for the current generation, a tile shows the newest previous model of the same line that carsized has, badged with that model's year ({len(PREV)} models); where carsized has no entry of the model line at all, the picture comes from the manufacturer's website, press site or configurator, or for a few models from a third-party catalogue site ({len(EXT)} models; the source, its terms and the editing applied are given in the detail panel) and was cut out, mirrored where it faced the wrong way and scaled to match; a few vans are shown as the manufacturer's outline drawing; the remaining tiles show the name only. By default every picture fills its tile; the "To scale" options in the View box size the pictures by real length (side view) or real width (front view) relative to the largest vehicle of the class or of the whole chart (widths come from carsized.com where available, otherwise from the class's typical width-to-length ratio). Drive layouts (front-, rear- or all-wheel drive) were researched from the brands' Swiss and German configurators, price lists and press pages in October 2026; the detail panel gives the versions an all-wheel-drive option is limited to and the page checked, and says so where an entry rests on trade press or product knowledge rather than a manufacturer page ({sum(1 for v in DRIVE.values() if v.get('confidence') != 'high')} of {len(DRIVE)} models). Data were checked on {E(meta.get('checked_on',''))}. Errors are possible, especially for models launched or withdrawn in the weeks before that date.</p>
  {srcs}
</section>

<script id="data" type="application/json">{data_json.replace('</', '<\\/')}</script>
<script>
(() => {{
const D = JSON.parse(document.getElementById('data').textContent);
const matrix = document.getElementById('matrix'), wrap = document.getElementById('mwrap');
const tiles = [...matrix.querySelectorAll('.tile')];
const byId = new Map(tiles.map(t => [t.dataset.id, t]));
const bars = [...matrix.querySelectorAll('.gbar')];
const detail = document.getElementById('detail');
let pinned = null;

// image fallbacks
matrix.querySelectorAll('.tile img').forEach(im => im.addEventListener('error', () => {{
  if (im.dataset.sid && !im.dataset.packFailed) return;  // a packed side view is being tried first (sideFallback)
  const box = im.closest('.img'); const other = box.querySelector('img:not([src="'+im.getAttribute('src')+'"])');
  im.remove(); if (!box.querySelector('img')) {{ box.classList.add('missing'); const s = document.createElement('span'); s.className='noimg'; s.textContent = im.alt.replace(/, (side|front) view$/,''); box.appendChild(s); }}
}}));

// ---- layout / filters ----
const gInputs = [...document.querySelectorAll('input[data-group]')], rInputs = [...document.querySelectorAll('input[data-row]')];
const pInputs = [...document.querySelectorAll('input[data-pt]')], dInputs = [...document.querySelectorAll('input[data-drive]')];
function layout() {{
  const onlyTwins = document.getElementById('only-twins').checked, showT2 = document.getElementById('show-t2').checked;
  const okG = new Set(gInputs.filter(i => i.checked).map(i => i.dataset.group));
  const okR = new Set(rInputs.filter(i => i.checked).map(i => i.dataset.row));
  const okP = new Set(pInputs.filter(i => i.checked).map(i => i.dataset.pt)), okD = new Set(dInputs.filter(i => i.checked).map(i => i.dataset.drive));
  const ptFilt = pInputs.some(i => !i.checked), dvFilt = dInputs.some(i => !i.checked), anyFilt = onlyTwins || ptFilt || dvFilt;
  const rowFilt = rInputs.some(i => !i.checked), grFilt = gInputs.some(i => !i.checked);
  const groupOfBrand = new Map([...matrix.querySelectorAll('.bhdr')].map(h => [h.dataset.brand, h.dataset.group]));
  // tiles: twin, powertrain and drive filters
  const shown = new Map();
  tiles.forEach(t => {{
    let show = true;
    if (onlyTwins) show = !!t.dataset.g && (showT2 || t.classList.contains('t1'));
    if (show && ptFilt) show = (t.dataset.pt || '').split(' ').some(k => okP.has(k));
    if (show && dvFilt) show = (t.dataset.drive || '').split(' ').some(k => okD.has(k));
    shown.set(t, show);
    t.classList.toggle('t2', !!(showT2 && t.dataset.g && !t.classList.contains('t1')));
    if (!showT2 && t.dataset.g && !t.classList.contains('t1')) t.classList.add('plain'); else t.classList.remove('plain');
  }});
  // columns: a brand column stays only if its group is selected and, once any filter is active, at least one of its cars is shown in a selected class
  const bh = [...matrix.querySelectorAll('.bhdr')];
  const visBrands = bh.filter(h => okG.has(h.dataset.group) && (!(anyFilt || rowFilt) || tiles.some(t => t.dataset.brand === h.dataset.brand && shown.get(t) && okR.has(t.dataset.row))));
  const colOf = new Map(); visBrands.forEach((h, i) => colOf.set(h.dataset.brand, i + 2));
  bh.forEach(h => {{ const c = colOf.get(h.dataset.brand); h.classList.toggle('hide', !c); if (c) h.style.gridColumn = c; }});
  // group headers span
  matrix.querySelectorAll('.ghdr').forEach(h => {{
    const cols = visBrands.filter(b => b.dataset.group === h.dataset.group).map(b => colOf.get(b.dataset.brand));
    if (!cols.length) h.classList.add('hide'); else {{ h.classList.remove('hide'); h.style.gridColumn = Math.min(...cols) + '/' + (Math.max(...cols) + 1); }}
  }});
  // rows: each class is a band of sub-rows; the members of a twin group share one sub-row
  const rh = [...matrix.querySelectorAll('.rhdr')];
  const visRows = rh.filter(h => okR.has(h.dataset.row) && (!(anyFilt || grFilt) || tiles.some(t => t.dataset.row === h.dataset.row && shown.get(t) && okG.has(groupOfBrand.get(t.dataset.brand)))));
  const bandOf = new Map(); let base = 3;
  visRows.forEach(h => {{ const S = +h.dataset.sub || 1; bandOf.set(h.dataset.row, [base, S]); base += S; }});
  const span = b => b[0] + '/' + (b[0] + b[1]);
  rh.forEach(h => {{ const b = bandOf.get(h.dataset.row); h.classList.toggle('hide', !b); if (b) h.style.gridRow = span(b); }});
  matrix.querySelectorAll('.cell').forEach(c => {{
    const b = bandOf.get(c.dataset.row), col = colOf.get(c.dataset.brand);
    const vis = b && col; c.classList.toggle('hide', !vis);
    if (vis) {{ c.style.gridRow = span(b); c.style.gridColumn = col; }}
  }});
  matrix.querySelectorAll('.stripe').forEach(s => {{
    const b = bandOf.get(s.dataset.row); s.classList.toggle('hide', !b);
    if (b) {{ s.style.gridRow = b[0] + (+s.dataset.s); s.style.gridColumn = '2/' + (visBrands.length + 2); }}
  }});
  const visible = new Map();
  tiles.forEach(t => {{
    const b = bandOf.get(t.dataset.row), col = colOf.get(t.dataset.brand);
    const vis = !!(shown.get(t) && b && col); t.classList.toggle('hide', !vis); visible.set(t, vis);
    if (vis) {{ t.style.gridRow = b[0] + (+t.dataset.s); t.style.gridColumn = col; }}
  }});
  // stub between stacked members of one family: only when the member above is visible and framed
  tiles.forEach(t => {{ const a = t.dataset.above && byId.get(t.dataset.above); t.classList.toggle('stack', !!(a && visible.get(a) && visible.get(t) && !t.classList.contains('plain') && !a.classList.contains('plain'))); }});
  // family bars: from the first to the last visible member on the family's line
  bars.forEach(bar => {{
    const b = bandOf.get(bar.dataset.row);
    const cols = b ? tiles.filter(t => t.dataset.g === bar.dataset.g && t.dataset.row === bar.dataset.row && t.dataset.s === bar.dataset.s && visible.get(t) && !t.classList.contains('plain')).map(t => colOf.get(t.dataset.brand)) : [];
    const vis = cols.length >= 2; bar.classList.toggle('hide', !vis);
    if (vis) {{ bar.style.gridRow = b[0] + (+bar.dataset.s); bar.style.gridColumn = Math.min(...cols) + '/' + (Math.max(...cols) + 1); }}
  }});
  // last-in-group borders
  const lastBrandOfGroup = new Map(); visBrands.forEach(b => lastBrandOfGroup.set(b.dataset.group, b.dataset.brand));
  matrix.querySelectorAll('.cell').forEach(c => c.classList.toggle('last-in-group', lastBrandOfGroup.get(c.dataset.group) === c.dataset.brand));
  matrix.style.gridTemplateColumns = `170px repeat(${{visBrands.length}}, var(--colw))`;
  scaleImages();
}}
function scaleImages() {{
  const mode = (document.querySelector('input[name="scale"]:checked') || {{}}).value || 'fill';
  matrix.classList.toggle('scale', mode !== 'fill');
  if (mode === 'fill') {{ tiles.forEach(t => t.querySelectorAll('img').forEach(im => im.style.removeProperty('--sc'))); return; }}
  // Side view: pictures are sized by real length; front view: by real width (a tile that falls back to its side view uses its length).
  // One scale per scope (class or whole chart): the largest vehicle fills the tile width, unless a tall picture would then
  // overflow the tile height, in which case that picture sets the scale. Hidden tiles count too, so filtering does not rescale.
  const front = matrix.classList.contains('view-front');
  const box = matrix.querySelector('.tile:not(.hide) .img'); const ratio = box && box.clientHeight ? box.clientWidth / box.clientHeight : (front ? 1.5 : 2.3);
  const useSide = t => !front || t.classList.contains('nofront');
  const dimOf = t => +(useSide(t) ? t.dataset.len : t.dataset.wid) || 0;
  const arOf = t => +(useSide(t) ? t.dataset.sar : t.dataset.far) || 0;
  const scopeOf = t => mode === 'global' ? 'all' : t.dataset.row;
  const k = {{}};
  tiles.forEach(t => {{ const d = dimOf(t), ar = arOf(t); if (!d || !ar) return; const sc = scopeOf(t); const lim = Math.min(1 / d, ar / (ratio * d)); k[sc] = Math.min(k[sc] || Infinity, lim); }});
  tiles.forEach(t => {{ const d = dimOf(t), ar = arOf(t), kk = k[scopeOf(t)]; t.querySelectorAll('img').forEach(im => im.style.setProperty('--sc', d && ar && kk ? (100 * d * kk).toFixed(1) + '%' : '100%')); }});
}}
[...gInputs, ...rInputs, ...pInputs, ...dInputs, document.getElementById('only-twins'), document.getElementById('show-t2'), ...document.querySelectorAll('input[name=scale]')].forEach(i => i.addEventListener('change', layout));
document.getElementById('p-all').onclick = () => {{ pInputs.forEach(i => i.checked = true); layout(); }};
document.getElementById('p-none').onclick = () => {{ pInputs.forEach(i => i.checked = false); layout(); }};
document.getElementById('d-all').onclick = () => {{ dInputs.forEach(i => i.checked = true); layout(); }};
document.getElementById('d-none').onclick = () => {{ dInputs.forEach(i => i.checked = false); layout(); }};
document.getElementById('g-all').onclick = () => {{ gInputs.forEach(i => i.checked = true); layout(); }};
document.getElementById('g-none').onclick = () => {{ gInputs.forEach(i => i.checked = false); layout(); }};
document.getElementById('r-all').onclick = () => {{ rInputs.forEach(i => i.checked = true); layout(); }};
document.getElementById('r-none').onclick = () => {{ rInputs.forEach(i => i.checked = false); layout(); }};
let frontsLoaded = false;
async function loadFronts() {{
  if (frontsLoaded) return; frontsLoaded = true;
  try {{
    const idx = await fetch('img/fronts.json').then(r => {{ if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }});
    document.querySelectorAll('img.v-front[data-fid]').forEach(im => {{ const b64 = idx[im.dataset.fid]; if (!b64) return; im.src = 'data:image/webp;base64,' + b64; }});
  }} catch (e) {{ console.warn('front views not available', e); document.querySelectorAll('.tile:not(.nofront) img.v-front').forEach(im => im.closest('.tile').classList.add('nofront')); }}
}}
document.querySelectorAll('input[name=view]').forEach(i => i.addEventListener('change', () => {{ const f = document.getElementById('view-front').checked; matrix.classList.toggle('view-front', f); if (f) loadFronts(); scaleImages(); }}));
document.querySelectorAll('input[name=size]').forEach(i => i.addEventListener('change', () => wrap.classList.toggle('compact', document.getElementById('size-compact').checked)));

// ---- highlighting ----
function light(g, on) {{
  matrix.classList.toggle('focus', !!(on && g));
  tiles.forEach(t => t.classList.toggle('lit', !!(on && g && t.dataset.g === g)));
  bars.forEach(b => b.classList.toggle('lit', !!(on && g && b.dataset.g === g)));
}}
tiles.forEach(t => {{
  t.addEventListener('mouseenter', () => {{ if (!pinned) light(t.dataset.g, true); }});
  t.addEventListener('mouseleave', () => {{ if (!pinned) light(null, false); }});
  t.addEventListener('click', () => openDetail(t.dataset.id));
}});
const FLC = new Set(D.flag_codes || []);
function flagUse(c, cls) {{ if (!c) return ''; const n = (D.country_names || {{}})[c] || c; return FLC.has(c) ? `<svg class="${{cls || 'fl'}}" viewBox="0 0 60 40" role="img" aria-label="${{esc(n)}}"><use href="#fl-${{c.toLowerCase()}}"/></svg>` : `<span class="${{cls || 'fl'}} txt">${{esc(c)}}</span>`; }}
function countryText(cb) {{ const N = D.country_names || {{}}; const org = (cb.origin || '').split(' (')[0], nm = cb.country_name || N[cb.country] || cb.country; const parts = [nm + (org && org !== nm ? ` (marque of ${{org}} origin)` : '')]; if (cb.hq) parts.push('head office ' + cb.hq + (cb.hq_entity ? ` (${{cb.hq_entity}})` : '')); const bi = (cb.built_in || []).map(c => N[c] || c); if (bi.length) parts.push('models for Europe built in ' + bi.join(', ')); let t = parts.filter(Boolean).join(' · '); if (cb.note) t += '. ' + cb.note.trim().replace(/\\.$/, '') + '.'; if (cb.confidence === 'low') t += ' (not fully verified)'; return t; }}
function fullName(o) {{ const b = o.brand.toLowerCase(), d = o.display.toLowerCase(); return (d === b || d.startsWith(b + ' ')) ? o.display : o.brand + ' ' + o.display; }}
function openDetail(id) {{
  const m = D.models[id]; if (!m) return;
  pinned = id; light(m.twin_group, true);
  const g = m.twin_group ? D.groups[m.twin_group] : null;
  const twins = [], sibs = [];
  const bc = D.countries && D.countries[m.brand];
  const dm = D.dims[id]; const ex = D.ext && D.ext[id]; const dv = D.drive && D.drive[id]; const num = v => (v == null ? '–' : Number(v).toLocaleString('en-US'));
  const DRV = {{FWD: 'front-wheel drive', RWD: 'rear-wheel drive', AWD: 'all-wheel drive'}};
  const driveText = d => {{ const parts = (d.drives || []).filter(k => DRV[k]).map(k => DRV[k] + (k === 'AWD' && d.awd_term ? ` (${{d.awd_term}})` : '')); let t = parts.length ? parts.join(' or ') : 'not researched'; t = t.charAt(0).toUpperCase() + t.slice(1); if (d.note) t += ' — ' + d.note; if (d.confidence === 'low') t += ' (unverified)'; else if (d.confidence === 'medium') t += ' (not checked on a manufacturer page)'; return t; }};
  const SYM = {{ok: '✓', check: '⚠', variant: 'ℹ', convention: 'ℹ', design: 'ℹ', info: 'ℹ', prev: '–'}};
  const chk = (i) => {{ const e = D.check.edges.find(e => (e.a === id && e.b === i) || (e.b === id && e.a === i)); if (!e || !e.cat) return ''; return ` <small class="chk ${{e.cat}}" title="${{esc(e.text)}}">${{SYM[e.cat] || 'ℹ'}} wheelbase Δ${{num(e.d_wb)}} · width Δ${{num(e.d_wid)}} · length Δ${{num(e.d_len)}} mm</small>`; }};
  if (g) g.members.forEach(i => {{ if (i === id) return; const o = D.models[i]; const e = g.edges.find(e => (e.a === id && e.b === i) || (e.b === id && e.a === i)); (e && e.tier === 1 ? twins : sibs).push(`<span class="rel"><a data-id="${{i}}">${{esc(fullName(o))}}</a>${{chk(i)}}</span>`); }});
  const pt = (m.powertrains || []).join(', ');
  const srcs = [...(m.status_sources || []), ...(m.twin_sources || [])].filter((v, i, a) => a.indexOf(v) === i);
  detail.innerHTML = `<button class="btn close" type="button" aria-label="Close">✕</button>
    <div class="sub">${{esc(m.group)}} · ${{esc(D.rows[m.row] || m.row)}}</div>
    <h3>${{esc(fullName(m))}}</h3>
    ${{bc ? `<div class="sub ctry">${{flagUse(bc.country)}}${{bc.second_flag ? flagUse(bc.second_flag, 'fl sec') : ''}}${{esc(countryText(bc))}}${{(bc.sources || []).length ? ` <a href="${{esc(bc.sources[0])}}" target="_blank" rel="noopener"><small>source</small></a>` : ''}}</div>` : ''}}
    <dl>
      ${{m.generation ? `<dt>Generation</dt><dd>${{esc(m.generation)}}</dd>` : ''}}
      ${{m.body ? `<dt>Body</dt><dd>${{esc(m.body)}}</dd>` : ''}}
      ${{m.length_mm ? `<dt>Length</dt><dd>${{(m.length_mm/1000).toFixed(2)}} m</dd>` : ''}}
      ${{dm ? `<dt>Measured</dt><dd class="meas">${{num(dm.len)}} × ${{num(dm.wid)}} × ${{num(dm.hei)}} mm · wheelbase ${{num(dm.wb)}} mm${{dm.kg ? ` · ${{num(dm.kg)}} kg` : ''}}<br><small>carsized.com entry: ${{esc(dm.label)}}${{dm.note ? ' — ' + esc(dm.note) : ''}}</small></dd>` : ''}}
      ${{m.platform ? `<dt>Platform</dt><dd>${{esc(m.platform)}}</dd>` : ''}}
      ${{pt ? `<dt>Powertrains</dt><dd>${{esc(pt)}}</dd>` : ''}}
      ${{dv ? `<dt>Drive</dt><dd>${{esc(driveText(dv))}}${{dv.source ? ` <a href="${{esc(dv.source)}}" target="_blank" rel="noopener"><small>source</small></a>` : ''}}</dd>` : ''}}
      <dt>Status</dt><dd>${{m.status === 'runout' ? 'Run-out' : 'On sale'}}${{m.status_note ? ' · ' + esc(m.status_note) : ''}}</dd>
      <dt>Switzerland</dt><dd>${{m.ch_on_sale === true ? 'On sale' : m.ch_on_sale === false ? 'Not sold' : 'Not checked'}}</dd>
      ${{(m.other_names || []).length ? `<dt>Other names</dt><dd>${{esc(m.other_names.join(', '))}}</dd>` : ''}}
    </dl>
    ${{g ? `<div class="twins"><b><span class="sw" style="--gc:var(--c${{g.slot+1}})"></span>${{esc(g.label)}}</b>
      ${{twins.length ? `<div>Same vehicle, other badge: ${{twins.join('; ')}}</div>` : ''}}
      ${{sibs.length ? `<div>Platform siblings: ${{sibs.join('; ')}}</div>` : ''}}
      ${{m.twin_note ? `<p>${{esc(m.twin_note)}}</p>` : ''}}</div>` : `<div>No twin or platform sibling on sale in Europe.${{m.twin_note && m.twin_note.startsWith('Platform check') ? ' ' + esc(m.twin_note) : ''}}</div>`}}
    ${{(m.cross_row_siblings || []).filter(i => D.models[i]).length ? `<div class="twins xrow"><b>Platform relatives in other classes</b><div>${{m.cross_row_siblings.filter(i => D.models[i]).map(i => `<span class="rel"><a data-id="${{i}}">${{esc(fullName(D.models[i]))}}</a> <small>${{esc(D.rows[D.models[i].row] || D.models[i].row)}}</small></span>`).join('; ')}}</div></div>` : ''}}
    ${{m.notes ? `<p>${{esc(m.notes)}}</p>` : ''}}
    ${{srcs.length ? `<div class="srcs"><b>Sources</b>${{srcs.map(u => `<a href="${{esc(u)}}" target="_blank" rel="noopener">${{esc(u.replace(/^https?:\\/\\//,''))}}</a>`).join('')}}</div>` : ''}}
    ${{dm ? `<div class="srcs"><a href="https://www.carsized.com/en/cars/${{esc(dm.slug)}}/" target="_blank" rel="noopener">Image and measurements: carsized.com (${{esc(dm.label)}})</a></div>` : ''}}
    ${{ex ? `<div class="srcs"><b>Pictures</b>${{['side', 'front'].filter(k => ex[k]).map(k => `<span>${{k === 'side' ? 'Side view' : 'Front view'}}: <a href="${{esc(ex[k].page || '')}}" target="_blank" rel="noopener">${{esc(ex[k].source || 'other source')}}</a>${{ex[k].notes ? ' — ' + esc(ex[k].notes) : ''}}${{ex[k].licence ? ' (' + esc(ex[k].licence) + ')' : ''}}</span>`).join('')}}<small>Not on carsized.com; the picture was cut out and scaled to match the carsized pictures.</small></div>` : ''}}`;
  detail.hidden = false;
  detail.querySelector('.close').onclick = () => {{ detail.hidden = true; pinned = null; light(null, false); }};
  detail.querySelectorAll('a[data-id]').forEach(a => a.onclick = (ev) => {{ ev.preventDefault(); const t = tiles.find(x => x.dataset.id === a.dataset.id); if (t) t.scrollIntoView({{block:'center', inline:'center', behavior:'smooth'}}); openDetail(a.dataset.id); }});
}}
document.querySelectorAll('.twinlist a[data-id], details.mc a[data-id]').forEach(a => a.addEventListener('click', ev => {{ ev.preventDefault(); const t = tiles.find(x => x.dataset.id === a.dataset.id); if (t) {{ wrap.scrollIntoView({{behavior:'smooth'}}); t.scrollIntoView({{block:'center', inline:'center', behavior:'smooth'}}); }} openDetail(a.dataset.id); }}));
document.addEventListener('keydown', e => {{ if (e.key === 'Escape' && !detail.hidden) {{ detail.hidden = true; pinned = null; light(null, false); }} }});

// ---- search ----
const search = document.getElementById('search');
let first = null;
search.addEventListener('input', () => {{
  const q = search.value.trim().toLowerCase(); first = null;
  tiles.forEach(t => {{ const m = D.models[t.dataset.id]; const hit = q.length > 1 && (m.brand + ' ' + m.display + ' ' + (m.other_names||[]).join(' ')).toLowerCase().includes(q); t.classList.toggle('hit', hit); if (hit && !first) first = t; }});
  if (first) first.scrollIntoView({{block:'center', inline:'center', behavior:'smooth'}});
}});
function esc(s) {{ return String(s ?? '').replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}})[c]); }}
layout();
}})();
</script>
'''
open(os.path.join(OUT, 'index.html'), 'w').write(page)
print('wrote', os.path.join(OUT, 'index.html'), len(page), 'bytes;', len(models), 'models;', NCOL-1, 'brand columns')
