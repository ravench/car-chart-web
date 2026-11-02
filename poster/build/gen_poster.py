#!/usr/bin/env python3
"""A0 print poster of the Identical Car Chart: only the twin / platform families.
usage: gen_poster.py <chart dir> <img dir> <out.html> [--tier1-only] [--W mm] [--landscape]"""
import json, sys, html, argparse, collections, os, re

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('imgdir'); ap.add_argument('out')
ap.add_argument('--W', type=float, default=50.0)        # tile width in mm
ap.add_argument('--imgh', type=float, default=19.0)    # max picture height in mm
ap.add_argument('--landscape', action='store_true')
ap.add_argument('--version', default='')
ap.add_argument('--widths', default='')
ap.add_argument('--bleed', type=float, default=0)
ap.add_argument('--url', default='https://car-chart.forestraven.net')   # QR target: the interactive chart (Raven, 2026-11-01)
ap.add_argument('--post-url', default='https://blog.forestraven.net/index.php/same-car-different-badge-a-chart-of-every-car-on-sale-in-europe/')   # blog post, printed in the footer
a = ap.parse_args()
E = lambda s: html.escape(str(s or ''))
here = os.path.dirname(os.path.abspath(__file__))

d = json.load(open(a.src + '/build/data.json'))
drive = json.load(open(a.src + '/build/drive.json'))
caps = json.load(open(here + '/captions.json'))
sizes = json.load(open(here + '/imgsizes.json'))
# pictures too poor for print size (none since chart v1.13 Version 23: cleaned Opel Rocks cut-out accepted)
for _k in (): sizes.pop(_k, None)
M = {m['id']: m for m in d['models']}
# brand country flags (chart v1.12+): reuse the chart's own flag drawings from gen.py
CB = {}; FLAG_SVG = {}; COUNTRY_NAME = {}
_cp = a.src + '/build/research/countries/brand_countries.json'
if not os.path.exists(_cp) and os.path.exists(a.src + '/research/countries/brand_countries.json'): _cp = a.src + '/research/countries/brand_countries.json'
if not os.path.exists(_cp):   # chart copies from v1.14 on ship without research/: use the newest earlier copy that has it
    import glob
    _c = sorted(glob.glob(os.path.dirname(os.path.abspath(a.src)) + '/chart-v*/build/research/countries/brand_countries.json'), key=lambda x: [int(n) for n in re.findall(r'v(\d+)\.(\d+)', x)[0]])
    if _c: _cp = _c[-1]; print('countries from', _cp)
    else: sys.exit('no brand_countries.json found: flags would be missing')
if os.path.exists(_cp):
    import math
    CB = json.load(open(_cp)).get('brands') or {}
    _g = open(a.src + '/build/gen.py').read()
    _blk = _g[_g.index('# ---------- brand countries (flags) ----------'):_g.index('def flag_svg_use')]
    _ns = {'math': math, 'json': json}; exec(_blk, _ns)
    FLAG_SVG, COUNTRY_NAME = _ns['FLAG_SVG'], _ns['COUNTRY_NAME']
def flag(code, cls='fl'):
    if not code or code not in FLAG_SVG: return ''
    return f'<svg class="{cls}" viewBox="0 0 60 40"><use href="#fl-{code.lower()}"/></svg>'
def brand_flags(b):
    cb = CB.get(b) or {}
    if not cb.get('country'): return ''
    return '<span class="flags">' + flag(cb['country']) + (flag(cb.get('second_flag'), 'fl sec') if cb.get('second_flag') else '') + '</span>'
rows = {r['code']: r for r in d['rows']}
row_order = [r['code'] for r in d['rows']]
ROW_ORDER = [r for r in row_order if r != 'd-car']; ROW_ORDER.insert(ROW_ORDER.index('e-car'), 'd-car')
group_order = [g['label'] for g in d['groups']]
brand_order = [b for g in d['groups'] for b in g['brands']]

OWNER_OVERRIDE = {'g-pickup-1': 'Ford', 'g-mpv-large-1': 'Ford', 'g-van-mid-1': 'Ford',
                  'g-b-suv-5': 'Suzuki', 'g-d-suv-3': 'Changan'}
COL = {  # platform-owner colours (print-safe, distinguishable)
    'Volkswagen Group': '#1f6fd1', 'Stellantis': '#0b8f7c', 'Renault Group': '#e3a300',
    'Hyundai Motor Group': '#7a4fb3', 'Toyota Motor': '#d7332b', 'Geely Holding': '#3d9a3a',
    'Chery': '#c8287a', 'Ford': '#22337f', 'BMW Group': '#5b6b78', 'Suzuki': '#ef7417',
    'Changan': '#8a5a2b'}
OWNER_NAME = {'Toyota Motor': 'Toyota', 'Hyundai Motor Group': 'Hyundai Motor Group', 'Ford': 'Ford',
              'Chery': 'Chery', 'Changan': 'Changan', 'Suzuki': 'Suzuki'}
PT = {'BEV': 'EV', 'PHEV': 'PHEV', 'HEV': 'HEV', 'MHEV': 'MHEV', 'petrol': 'Petrol', 'diesel': 'Diesel',
      'CNG': 'CNG', 'LPG': 'LPG', 'FCEV': 'H₂'}
PT_ORDER = ['petrol', 'diesel', 'LPG', 'CNG', 'MHEV', 'HEV', 'PHEV', 'BEV', 'FCEV']

def owner(g):
    if g['id'] in OWNER_OVERRIDE: return OWNER_OVERRIDE[g['id']]
    return collections.Counter(M[i]['group'] for i in g['members']).most_common(1)[0][0]

def sortkey(i):
    m = M[i]
    return (group_order.index(m['group']) if m['group'] in group_order else 99,
            brand_order.index(m['brand']) if m['brand'] in brand_order else 99, m['display'])

def clusters(g):
    adj = collections.defaultdict(set)
    for e in g.get('edges', []):
        if e['tier'] == 1: adj[e['a']].add(e['b']); adj[e['b']].add(e['a'])
    seen, out = set(), []
    for i in sorted(adj, key=sortkey):
        if i in seen: continue
        comp, st = set(), [i]
        while st:
            x = st.pop()
            if x in comp: continue
            comp.add(x); st += list(adj[x])
        seen |= comp; out.append(sorted(comp, key=sortkey))
    return out

fams = collections.defaultdict(list)
for g in d['twin_groups']:
    g['owner'] = owner(g); g['clusters'] = clusters(g)
    fams[g['row']].append(g)

# --- per-class scale: the longest vehicle of the class fills the picture width, unless a tall one would overflow
PAD = 2.2
iw = a.W - 2 * PAD
scale, boxh = {}, {}
for r, gs in fams.items():
    ids = [i for g in gs for i in g['members']]
    L = [M[i]['length_mm'] for i in ids if M[i].get('length_mm')]
    s = iw / max(L)
    for i in ids:
        if i in sizes and M[i].get('length_mm'):
            w, h = sizes[i]; s = min(s, a.imgh / (M[i]['length_mm'] * h / w))
    scale[r] = s
    hs = [M[i]['length_mm'] * s * sizes[i][1] / sizes[i][0] for i in ids if i in sizes and M[i].get('length_mm')]
    boxh[r] = max(hs) + 0.6

def tile(i, r):
    m = M[i]
    L = m.get('length_mm')
    if i in sizes and L:
        w = L * scale[r]
        pic = f'<img src="{a.imgdir}/{i}.jpg" style="width:{w:.2f}mm">'
    else:
        pic = '<span class="nopic">no picture</span>'
    pts = [PT[p] for p in sorted(m.get('powertrains') or [], key=lambda p: PT_ORDER.index(p) if p in PT_ORDER else 9)]
    awd = (drive.get(i) or {}).get('awd')
    meta = []
    if L: meta.append(f'<b>{L/1000:.2f}</b>&thinsp;m')
    if pts: meta.append(' · '.join(pts))
    if awd: meta.append('<i class="awd">AWD</i>')
    name = m['display']
    brand = m['brand']
    if name.lower().startswith(brand.lower() + ' '): pass
    return (f'<div class="tile"><div class="pic" style="height:{boxh[r]:.2f}mm">{pic}</div>'
            f'<div class="brand">{brand_flags(brand)}{E(brand)}</div><div class="model">{E(name)}</div>'
            f'<div class="meta">{" &nbsp;".join(meta)}</div></div>')

def card(g):
    r = g['row']; col = COL.get(g['owner'], '#666')
    cl = g['clusters']; incl = {i for c in cl for i in c}
    whole = len(cl) == 1 and len(incl) == len(g['members'])
    body = []
    if whole:
        body.append(''.join(tile(i, r) for i in cl[0]))
    else:
        for c in cl:
            body.append(f'<div class="same" style="flex:{len(c)} 0 auto"><div class="tag">Same vehicle</div><div class="tiles">{"".join(tile(i, r) for i in c)}</div></div>')
        rest = sorted([i for i in g['members'] if i not in incl], key=sortkey)
        body.append(''.join(tile(i, r) for i in rest))
    own = OWNER_NAME.get(g['owner'], g['owner'])
    kind = 'Same vehicle, different badges' if whole else 'Shared platform'
    w = WID.get(g['id'])
    fl = f';flex:{w:.1f} 1 {w:.1f}mm' if w else ''
    return (f'<div class="card {"whole" if whole else "plat"}" data-id="{g["id"]}" style="--c:{col}{fl}">'
            f'<div class="head"><span class="plat-name">{E(g["label"])}</span>'
            f'<span class="own">{E(own)}</span><span class="kind">{kind}</span></div>'
            f'<div class="cap">{E(caps.get(g["id"], ""))}</div>'
            f'<div class="tiles">{"".join(body)}</div></div>')

WID = json.load(open(a.widths)) if a.widths else {}
PW0 = 1189 if a.landscape else 841
LAB = 44.0; GAP = 3.0; CAP = PW0 - 32 - LAB

def famsort(gs):
    return sorted(gs, key=lambda g: (group_order.index(g['owner']) if g['owner'] in group_order else 99, -len(g['members'])))

def ffd(gs, cap):
    lines = []
    for g in sorted(gs, key=lambda g: -WID[g['id']]):
        for ln in lines:
            if sum(WID[x['id']] for x in ln) + GAP * len(ln) + WID[g['id']] <= cap:
                ln.append(g); break
        else: lines.append([g])
    return lines

def pack(gs, cap):
    if not WID: return [famsort(gs)]
    T = sum(WID[g['id']] + GAP for g in gs)
    k = max(1, -(-T // cap)); k = int(k)
    while True:
        c = T / k
        while c <= cap:
            ln = ffd(gs, c)
            if len(ln) <= k: return [famsort(l) for l in ln]
            c += 2
        k += 1

def natural(r):
    return LAB + sum(WID.get(g['id'], 60) + GAP for g in fams[r])

def band(r, cap=CAP):
    gs = fams[r]
    n = sum(len(g['members']) for g in gs)
    lines = pack(gs, cap)
    grow = natural(r) if WID else 1
    return (f'<section class="band" style="flex:{grow:.0f} 1 {grow:.0f}mm"><div class="rowlab"><h2>{E(rows[r]["name"])}</h2>'
            f'<p>{E(rows[r]["desc"])}</p><p class="cnt">{len(gs)} {"family" if len(gs)==1 else "families"} · {n} models</p></div>'
            f'<div class="cards">{"".join('<div class="line">' + "".join(card(g) for g in ln) + "</div>" for ln in lines)}</div></section>')

def layout():
    out, small = [], []
    rs = [r for r in ROW_ORDER if r in fams]
    for r in rs:
        if WID and natural(r) - LAB <= CAP:
            if small and sum(natural(x) for x in small) + 8 * len(small) + natural(r) <= PW0 - 32:
                small.append(r); continue
            if small: out.append(small)
            small = [r]; continue
        if small: out.append(small); small = []
        out.append([r])
    if small: out.append(small)
    html_ = ''
    for grp in out:
        if len(grp) == 1: html_ += '<div class="brow">' + band(grp[0]) + '</div>'
        else: html_ += '<div class="brow">' + ''.join(band(r, natural(r) - LAB + 1) for r in grp) + '</div>'
    return html_

n_models = sum(len(g['members']) for g in d['twin_groups'])
n_same = sum(len(c) for g in d['twin_groups'] for c in g['clusters'])
owners_used = [o for o in COL if any(g['owner'] == o for g in d['twin_groups'])]
legend_cols = ''.join(f'<span class="lc"><i style="background:{COL[o]}"></i>{E(OWNER_NAME.get(o, o))}</span>' for o in owners_used)
PW, PH = (1189, 841) if a.landscape else (841, 1189)
BL = a.bleed; PW += 2 * BL; PH += 2 * BL

css = f"""
@page {{ size: {PW}mm {PH}mm; margin: 0 }}
* {{ box-sizing: border-box; margin: 0; padding: 0 }}
html, body {{ width: {PW}mm; height: {PH}mm; background: #fbfaf7; -webkit-print-color-adjust: exact; print-color-adjust: exact }}
body {{ font-family: 'Barlow', sans-serif; color: #1c1d20; padding: {16+BL}mm {16+BL}mm {12+BL}mm; display: flex; flex-direction: column }}
h1, h2, .plat-name, .model, .own {{ font-family: 'Barlow Condensed', sans-serif }}
header {{ display: flex; align-items: flex-end; gap: 14mm; border-bottom: 0.8mm solid #1c1d20; padding-bottom: 5mm; margin-bottom: 5mm }}
h1 {{ font-size: 118pt; line-height: .82; font-weight: 700; letter-spacing: -1.5pt }}
.sub {{ font-size: 17pt; line-height: 1.3; max-width: 330mm; text-wrap: balance; color: #33363b }}
.sub b {{ color: #1c1d20 }}
.stats {{ margin-left: auto; display: flex; gap: 9mm; text-align: right }}
.stats div {{ font-family: 'Barlow Condensed'; font-size: 11pt; letter-spacing: 1pt; text-transform: uppercase; color: #6a6e75 }}
.qr {{ display: flex; gap: 4mm; align-items: flex-end; padding-left: 9mm; border-left: .3mm solid #c9cbcf }}
.qrimg {{ width: 30mm; height: 30mm; display: block }}
.qrcap {{ width: 52mm; font-size: 9.5pt; line-height: 1.25; color: #4a4d52 }}
.qrcap b {{ display: block; font-family: 'Barlow Condensed'; font-size: 16pt; color: #1c1d20; line-height: 1.05; margin-bottom: 1mm }}
.qrcap span {{ display: block; margin-top: 1.5mm; font-size: 11pt; color: #1c1d20; font-weight: 600; word-break: break-all }}
.stats b {{ display: block; font-size: 44pt; letter-spacing: 0; color: #1c1d20; line-height: 1 }}
.legend {{ display: flex; flex-direction: column; gap: 2.2mm; font-size: 11pt; color: #33363b; margin-bottom: 5mm }}
.legend .lrow {{ display: flex; gap: 10mm; align-items: center; white-space: nowrap }}
.legend .k {{ display: flex; align-items: center; gap: 2.5mm }}
.legend .sw {{ width: 13mm; height: 7mm; border-radius: 1.5mm; display: inline-block }}
.legend .sw.d {{ border: .55mm dashed #555 }} .legend .sw.s {{ border: .55mm solid #555; background: #eef0f2 }}
.lcs {{ display: flex; flex-wrap: wrap; gap: 2mm 5mm; align-items: center }}
.lc {{ display: inline-flex; align-items: center; gap: 1.5mm; font-family: 'Barlow Condensed'; font-weight: 600; font-size: 12pt }}
.lc i {{ width: 4.5mm; height: 4.5mm; border-radius: 1mm; display: inline-block }}
main {{ flex: 1; display: flex; flex-direction: column; justify-content: space-between }}
.brow {{ display: flex; gap: 8mm }}
.line {{ display: flex; gap: {GAP}mm; width: 100% }}
.band {{ display: flex; gap: 4mm; border-top: .3mm solid #c9cbcf; padding: 2.4mm 0; min-width: 0 }}
.rowlab {{ width: {LAB-4}mm; flex: none; padding-top: 1mm }}
.rowlab h2 {{ font-size: 19pt; line-height: 1; font-weight: 700 }}
.rowlab p {{ font-size: 8.5pt; color: #6a6e75; line-height: 1.25; margin-top: 1mm }}
.rowlab .cnt {{ font-family: 'Barlow Condensed'; font-size: 9.5pt; text-transform: uppercase; letter-spacing: .6pt; color: #33363b }}
.cards {{ display: flex; flex-direction: column; gap: 3mm; flex: 1; min-width: 0 }}
.card {{ border-radius: 2.4mm; padding: 1.6mm 2mm 2mm; background: color-mix(in srgb, var(--c) 7%, #fff) }}
.card.plat {{ border: .55mm dashed var(--c) }}
.card.whole {{ border: .7mm solid var(--c) }}
.head {{ display: flex; align-items: baseline; gap: 2mm; white-space: nowrap }}
.plat-name {{ font-size: 15pt; font-weight: 700; color: var(--c); filter: brightness(.82) }}
.own {{ font-size: 10pt; font-weight: 600; color: #fff; background: var(--c); padding: .2mm 1.6mm; border-radius: 1mm }}
.kind {{ font-size: 8pt; text-transform: uppercase; letter-spacing: .6pt; color: #6a6e75; margin-left: auto; padding-left: 3mm }}
.cap {{ font-size: 8.6pt; line-height: 1.2; color: #3a3d42; margin: .4mm 0 1.4mm; max-width: 100%; width: 0; min-width: 100% }}
.tiles {{ display: flex; flex: 1; gap: 1.6mm; align-items: stretch }}
.same {{ border: .55mm solid var(--c); border-radius: 1.8mm; padding: 0 1.2mm 1.2mm; background: color-mix(in srgb, var(--c) 16%, #fff) }}
.same .tag {{ font-size: 7pt; text-transform: uppercase; letter-spacing: .8pt; font-weight: 600; color: var(--c); filter: brightness(.75); padding: .5mm 0 .6mm }}
.tile {{ flex: 1 0 {a.W}mm; background: #fff; border-radius: 1.4mm; padding: 1.2mm {PAD}mm 1.4mm; box-shadow: 0 0 0 .2mm #dcdde0 }}
.pic {{ display: flex; align-items: flex-end; justify-content: center; margin-bottom: 1.2mm }}
.pic img {{ display: block }}
.nopic {{ align-self: center; font-size: 7.5pt; color: #9a9da3; text-transform: uppercase; letter-spacing: .8pt; border: .3mm dashed #c9cbcf; border-radius: 1mm; padding: 1.5mm 3mm }}
.flagdefs {{ position: absolute; width: 0; height: 0; overflow: hidden }}
.flags {{ display: inline-flex; gap: .6mm; align-items: center; margin-right: 1mm; vertical-align: -.35mm }}
.fl {{ display: block; width: 3.6mm; height: 2.4mm; border-radius: .3mm; box-shadow: 0 0 0 .12mm rgba(0,0,0,.3) }}
.fl.sec {{ width: 2.7mm; height: 1.8mm }}
.legend .fl {{ display: inline-block; width: 6mm; height: 4mm; vertical-align: -.8mm }}
.legend .fl.sec {{ width: 4.5mm; height: 3mm; margin: 0 .8mm; vertical-align: -.4mm }}
.brand {{ font-size: 7.4pt; text-transform: uppercase; letter-spacing: .7pt; font-weight: 600; color: #5b5f66; line-height: 1.1 }}
.model {{ font-size: 13pt; font-weight: 700; line-height: 1.02; margin-top: .2mm }}
.meta {{ font-size: 7pt; color: #5b5f66; margin-top: .6mm; line-height: 1.15 }}
.meta b {{ color: #1c1d20; font-weight: 600 }}
.awd {{ font-style: normal; font-weight: 700; font-size: 6.2pt; border: .25mm solid #5b5f66; border-radius: .6mm; padding: 0 .6mm; letter-spacing: .3pt }}
footer {{ border-top: .8mm solid #1c1d20; padding-top: 3mm; margin-top: 3mm; display: flex; gap: 10mm; font-size: 8.4pt; line-height: 1.3; color: #4a4d52 }}
footer p {{ flex: 1 }}
footer b {{ color: #1c1d20 }}
"""

used = sorted({'DE', 'PL'} | {c for g in d['twin_groups'] for i in g['members'] for c in ((CB.get(M[i]['brand']) or {}).get('country'), (CB.get(M[i]['brand']) or {}).get('second_flag')) if c})
flagdefs = ('<svg class="flagdefs" width="0" height="0"><defs>' + ''.join(f'<symbol id="fl-{c.lower()}" viewBox="0 0 60 40">{FLAG_SVG[c]}</symbol>' for c in used if c in FLAG_SVG) + '</defs></svg>') if used else ''
flag_leg = (f'<span class="k">{flag("DE")}<span>Flag: country of the brand\'s head office</span></span><span class="k">{flag("DE")}{flag("PL", "fl sec")}<span>Small second flag: the one foreign country that builds the brand\'s cars for Europe (MAN: Poland)</span></span>') if CB else ''
qr_block, url_short = '', ''
post_short = re.sub(r'^(https?://)?(www\.)?', '', a.post_url).rstrip('/')
if a.url:
    import segno, re
    url_short = re.sub(r'^(https?://)?(www\.)?', '', a.url).rstrip('/')
    _q = segno.make(a.url, error='m')
    _svg = _q.svg_inline(scale=1, border=0, dark='#1c1d20', light=None)
    _svg = re.sub(r'(<svg[^>]*?)\s(width|height)="[^"]*"', r'\1', _svg); _svg = re.sub(r'(<svg[^>]*?)\s(width|height)="[^"]*"', r'\1', _svg)
    _n = _q.symbol_size(scale=1, border=0)[0]
    if 'viewBox' not in _svg: _svg = _svg.replace('<svg', f'<svg viewBox="0 0 {_n} {_n}"', 1)
    _svg = _svg.replace('<svg', '<svg class="qrimg"', 1)
    qr_block = f'<div class="qr">{_svg}<div class="qrcap"><b>Interactive version</b>every vehicle, sources and filters<span>{E(url_short)}</span></div></div>'
body = f"""<header><h1>Identical<br>Car Chart</h1>
<div class="sub">The same car under different badges. <b>{len(d['twin_groups'])} families</b> of new cars and vans up to 3.5&nbsp;t that share a body or a platform across brands, as sold in Europe in autumn 2026 (Swiss model names).</div>
<div class="stats"><div><b>{len(d['twin_groups'])}</b>families</div><div><b>{n_models}</b>models</div><div><b>{n_same}</b>same-body twins</div></div>{qr_block}</header>
<div class="legend"><div class="lrow">
<span class="k"><span class="sw s"></span><span><b>Solid frame:</b> the same vehicle under another badge (rebadge / twin)</span></span>
<span class="k"><span class="sw d"></span><span><b>Dashed frame:</b> same platform, own body (platform sibling)</span></span>
<span class="k"><span>Colour: whose platform it is</span><span class="lcs">{legend_cols}</span></span></div>
<div class="lrow">{flag_leg}<span class="k"><span>Pictures to scale within each class · length in metres · <i class="awd" style="font-size:8pt">AWD</i> available with all-wheel drive</span></span></div>
</div>
<main>{layout()}</main>{flagdefs}
<footer>
<p><b>What counts.</b> A family is drawn when models of at least two brands, or of two companies, share a platform in the same vehicle class. Same-brand derivatives (BMW X1/iX1, Volvo XC40/EX40/EC40) share one tile. Platform relatives in other classes (for example the Peugeot 3008 and 5008) are not linked on this poster.</p>
<p><b>Sources.</b> Line-ups from the brands' Swiss and German model pages and press releases, checked against European trade press; twin and platform links cite manufacturer statements or trade press. Brand countries from Wikipedia (head offices, checked 2026-11-01). Checked {E(d['meta'].get('checked_on'))}; errors are possible for models launched or withdrawn shortly before.</p>
<p><b>Pictures</b> from carsized.com, otherwise from manufacturer websites, press libraries and configurators, cut out and scaled. Interactive chart (QR code): <b style="white-space:nowrap">{E(url_short)}</b>. The story behind it: {E(post_short)}</p>
</footer>"""

doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Identical Car Chart poster</title>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style></head><body>{body}</body></html>"""
open(a.out, 'w').write(doc)
print('families', len(d['twin_groups']), 'models', n_models, 'same-body', n_same)
