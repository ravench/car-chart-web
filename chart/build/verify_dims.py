#!/usr/bin/env python3
"""Check twin/sibling pairings against carsized.com measurements.
Usage: python3 verify_dims.py data.json dims.json match/map.tsv out_dir [dims_notes.json]
dims.json: {model_id: {slug, len, wid, widm, hei, wb, gc, kg, seg, spot, side, front}} (mm / kg)
Writes out_dir/dims_report.md (human report) and out_dir/dims_flags.json (consumed by gen.py)."""
import sys, json, os, csv, re
data = json.load(open(sys.argv[1])); dims = json.load(open(sys.argv[2])); out = sys.argv[4]
notes = json.load(open(sys.argv[5])) if len(sys.argv) > 5 and os.path.exists(sys.argv[5]) else {'pairs': {}, 'img_notes': {}}
PREV = set(notes.get('prev_model', []))   # carsized entry is a previous model: pictured (badge with its model year), but not used to check pairings
def prev_year(i):
    """Badge year of a previous-model entry: the last year of carsized's own range ('present' or 2025+ -> 2025),
    capped at the start year of the current generation (chart `generation` field), i.e. the last year the pictured model was on sale."""
    r = str((dims.get(i) or {}).get('range') or '')
    ys = re.findall(r'(19|20)(\d\d)', r)
    y = 2025 if ('present' in r.lower() or not ys) else min(int(ys[-1][0] + ys[-1][1]), 2025)
    g = re.search(r'(19|20)\d\d', str((models.get(i) or {}).get('generation') or ''))
    if g: y = min(y, int(g.group(0)))
    return y
os.makedirs(out, exist_ok=True)
models = {m['id']: m for m in data['models']}
PREV_YEAR = {i: prev_year(i) for i in PREV}
# only measurements of models that are currently matched to a carsized entry count (map.tsv is the authority)
_matched = set()
with open(sys.argv[3]) as f:
    for line in f:
        if line.strip() and not line.startswith('id\t'): _matched.add(line.split('\t')[0])
dims = {k: v for k, v in dims.items() if k in _matched}
T1 = dict(wb=12, wid=30, hei=45, len=90)      # same body shell
T2 = dict(wb=250, wid=120)                     # platform-level mismatch only
def label(slug):
    """'volkswagen-golf-2024-5-door-hatchback' -> ('2024', '5-door hatchback')"""
    m = re.search(r'-(\d{4})(?:-(.*))?$', slug or '')
    if not m: return ('', slug or '')
    body = (m.group(2) or '').replace('-', ' ')
    return (m.group(1), body)
def d(a, b, k):
    if dims.get(a, {}).get(k) and dims.get(b, {}).get(k): return abs(dims[a][k] - dims[b][k])
    return None
def name(i):
    m = models.get(i)
    if not m: return i
    b, d = m['brand'].lower(), m['display'].lower()
    return m['display'] if d == b or d.startswith(b + ' ') else f"{m['brand']} {m['display']}"
def pairkey(a, b): return '|'.join(sorted([a, b]))
def classify(a, b, tier, dl, dw, dh, dwb):
    """Return (symbol, category, text). category: ok | variant | convention | design | info | check."""
    note = notes['pairs'].get(pairkey(a, b))
    la, lb = label(dims[a]['slug']), label(dims[b]['slug'])
    bodies_differ = la[1] != lb[1]
    if tier == 1:
        over = {k: v for k, v in (('wb', dwb), ('wid', dw), ('hei', dh), ('len', dl)) if v is not None and v > T1[k]}
        if not over: return ('✓', 'ok', 'wheelbase, width, length and height agree within tolerance')
        if note: return ('ℹ', note['cat'], note['text'])
        if 'wb' in over or 'len' in over:
            if bodies_differ and (dw is None or dw <= 120):
                txt = f"carsized lists different body-length versions ({la[1]} {la[0]} vs {lb[1]} {lb[0]}): length differs by {dl} mm" + (f" and wheelbase by {dwb} mm" if 'wb' in over else '')
                txt += (f"; the width figures differ by {dw} mm ({dims[a]['wid']} vs {dims[b]['wid']} mm), the usual gap between body width and width with folded mirrors" if 'wid' in over else "; width is identical") + ", so the shared body shell is consistent"
                return ('ℹ', 'variant', txt)
            return ('⚠', 'check', 'wheelbase or length differ beyond what body versions explain; pairing to be reviewed')
        if 'wid' in over and dw <= 120:
            return ('ℹ', 'convention', f"width figures on carsized differ by {dw} mm ({dims[a]['wid']} vs {dims[b]['wid']} mm), the usual gap between body width and width with folded mirrors; wheelbase and length match" + (f"; height differs by {dh} mm (roof rails or roof version)" if 'hei' in over else ''))
        if 'hei' in over and dh <= 100:
            return ('ℹ', 'design', f"height differs by {dh} mm (roof rails, ride height or roof version); wheelbase, width and length match")
        return ('⚠', 'check', 'measurements do not fit a shared body shell; pairing to be reviewed')
    # tier 2: platform siblings may differ in length, height and (within limits) wheelbase
    if note: return ('ℹ', note['cat'], note['text'])
    if (dwb is not None and dwb > T2['wb']) or (dw is not None and dw > T2['wid']):
        return ('⚠', 'check', 'wheelbase or width differ more than platform variants normally allow; pairing to be reviewed')
    return ('✓', 'ok', 'wheelbase and width within the range of one platform')
flags = {'edges': [], 'groups': {}, 'length_check': [], 'img_notes': notes.get('img_notes', {}), 'tolerances': {'tier1': T1, 'tier2': T2}, 'prev_model': sorted(PREV), 'prev_year': PREV_YEAR}
lines = ['# Measurement check of twin and sibling pairings (carsized.com)', '',
         'Measurements in mm from carsized.com: length, width (body, where available), height, wheelbase. Only models with a carsized entry can be checked.',
         f'**Tier 1** (same body shell, different badge): wheelbase within {T1["wb"]} mm, width within {T1["wid"]} mm, height within {T1["hei"]} mm, length within {T1["len"]} mm. Larger gaps are classified: *variant* (carsized lists different body-length versions), *convention* (width quoted with or without folded mirrors), *design* (roof rails, ride height, bumpers), *check* (unexplained).',
         f'**Tier 2** (platform siblings with their own body): only a wheelbase gap above {T2["wb"]} mm or a width gap above {T2["wid"]} mm is flagged; platform siblings legitimately differ in length and height.',
         f'**Previous-model entries:** {len(PREV)} models are pictured with the newest previous model carsized has (tile badge with that model\'s year) because carsized has no entry for the current generation; their measurements are shown but not used to check pairings (marked –).', '']
n_edges = n_checked = 0; cats = {}
for g in data['twin_groups']:
    mem = [i for i in g['members'] if i in models]
    lines.append(f"## {g['label']} — {data['rows'] and next((r['name'] for r in data['rows'] if r['code'] == g['row']), g['row'])} ({len(mem)} members)")
    lines.append(''); lines.append('| Model | carsized entry | Length | Width | Height | Wheelbase | Weight |'); lines.append('|---|---|---|---|---|---|---|')
    for i in mem:
        dd = dims.get(i) or {}
        if dd.get('len'):
            y, body = label(dd['slug'])
            lines.append(f"| {name(i)} | {body} {y} | {dd['len']} | {dd.get('wid', '')} | {dd.get('hei', '')} | {dd.get('wb', '')} | {dd.get('kg', '')} |")
        else: lines.append(f"| {name(i)} | — no carsized entry | | | | | |")
    lines.append('')
    gcats = []
    for e in g.get('edges', []):
        a, b, tier = e['a'], e['b'], e.get('tier', 2); n_edges += 1
        dl, dw, dh, dwb = d(a, b, 'len'), d(a, b, 'wid'), d(a, b, 'hei'), d(a, b, 'wb')
        if dwb is None and dl is None: continue
        if a in PREV or b in PREV:
            p = a if a in PREV else b
            cat = 'prev'; text = f"carsized has only the previous model of {name(p)} (the one sold in {PREV_YEAR.get(p, 2025)}), so this pairing of the current generation cannot be checked against measurements"
            cats[cat] = cats.get(cat, 0) + 1
            flags['edges'].append({'group': g['id'], 'a': a, 'b': b, 'tier': tier, 'd_len': dl, 'd_wid': dw, 'd_hei': dh, 'd_wb': dwb, 'cat': cat, 'text': text})
            lines.append(f"- – **{name(a)} ↔ {name(b)}** (tier {tier}; previous-model entry): {text}.")
            continue
        n_checked += 1
        sym, cat, text = classify(a, b, tier, dl, dw, dh, dwb)
        cats[cat] = cats.get(cat, 0) + 1; gcats.append(cat)
        flags['edges'].append({'group': g['id'], 'a': a, 'b': b, 'tier': tier, 'd_len': dl, 'd_wid': dw, 'd_hei': dh, 'd_wb': dwb, 'cat': cat, 'text': text})
        lines.append(f"- {sym} **{name(a)} ↔ {name(b)}** (tier {tier}; Δ wheelbase {dwb}, length {dl}, width {dw}, height {dh} mm): {text}.")
    verdict = 'check' if 'check' in gcats else ('explained' if any(c not in ('ok',) for c in gcats) else ('ok' if gcats else 'nodata'))
    flags['groups'][g['id']] = {'verdict': verdict, 'n_pairs': len(g.get('edges', [])), 'n_measured': len(gcats)}
    lines.append('')
lines.append('## Chart length vs carsized length (data check)'); lines.append('')
lines.append('Differences above 60 mm between the length researched for the chart and the carsized entry. Most are body-length versions (the chart quotes the short version, carsized has the long one).'); lines.append('')
for i, m in models.items():
    dd = dims.get(i)
    if i in PREV: continue
    if dd and dd.get('len') and m.get('length_mm'):
        delta = dd['len'] - m['length_mm']
        if abs(delta) > 60:
            y, body = label(dd['slug'])
            flags['length_check'].append({'id': i, 'chart': m['length_mm'], 'carsized': dd['len'], 'slug': dd.get('slug')})
            lines.append(f"- {name(i)}: chart {m['length_mm']} mm, carsized {dd['len']} mm ({delta:+} mm; carsized entry: {body} {y})")
summary = (f"**Summary:** {len(data['twin_groups'])} families, {n_edges} pairings, {n_checked} with carsized measurements on both sides. "
           + ', '.join(f"{v} {k}" for k, v in sorted(cats.items(), key=lambda x: -x[1])) + '. '
           + f"{len(flags['length_check'])} chart lengths differ from the carsized entry by more than 60 mm (listed at the end).")
lines.insert(5, summary); lines.insert(6, '')
flags['summary'] = {'groups': len(data['twin_groups']), 'edges': n_edges, 'checked': n_checked, 'cats': cats, 'models_measured': sum(1 for i in models if dims.get(i, {}).get('len'))}
open(os.path.join(out, 'dims_report.md'), 'w').write('\n'.join(lines) + '\n')
json.dump(flags, open(os.path.join(out, 'dims_flags.json'), 'w'), indent=1, ensure_ascii=False)
print(f'{n_edges} edges, {n_checked} checked: {cats}; {len(flags["length_check"])} length mismatches -> {out}')
