#!/usr/bin/env python3
"""Fold verify/*.corrections.json into overrides.json (from overrides.base.json) and research/verify-additions.json.
Usage: python3 apply_corrections.py [--min-confidence medium]"""
import json, glob, os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(HERE, 'overrides.base.json')))
ov = copy.deepcopy(base)
ov.setdefault('models', {}); ov.setdefault('exclude', []); ov.setdefault('edges_add', []); ov.setdefault('edges_remove', [])
adds = []; sources = []; log = []
minconf = 'medium'
for f in sorted(glob.glob(os.path.join(HERE, 'verify', '*.corrections.json'))):
    try: c = json.load(open(f))
    except Exception as e: log.append(f'ERROR {f}: {e}'); continue
    scope = c.get('scope') or os.path.basename(f)
    for x in c.get('corrections', []):
        key, fld, new = x.get('key'), x.get('field'), x.get('new')
        conf = (x.get('confidence') or 'medium').lower()
        if not key or not fld: log.append(f'{scope}: malformed correction {x}'); continue
        if conf not in ('high', 'medium'): log.append(f'{scope}: skipped low-confidence {key} {fld}'); continue
        if fld == 'exclude':
            if new: ov['exclude'].append(key); log.append(f'{scope}: EXCLUDE {key} — {x.get("note","")}')
            continue
        if fld in ('twin_members', 'twin_tier'):
            # handled via twin_changes preferably; still record on the model
            pass
        ov['models'].setdefault(key, {})[fld] = new
        if x.get('source'):
            ov['models'][key].setdefault('_verify_sources', []).append(x['source'])
        log.append(f'{scope}: {key}.{fld}: {x.get("old")!r} -> {new!r} [{conf}]')
    for t in c.get('twin_changes', []):
        a, b, act = t.get('a'), t.get('b'), t.get('action')
        if not (a and b): continue
        if act in ('add', 'retier'):
            ov['edges_add'].append({'a': a, 'b': b, 'tier': t.get('tier', 2), 'source': t.get('source'), 'note': t.get('note')})
        elif act == 'remove':
            ov['edges_remove'].append({'a': a, 'b': b})
        log.append(f'{scope}: twin {act} {a} ~ {b} tier {t.get("tier")}')
    for m in c.get('add', []):
        m = dict(m); m.setdefault('status', 'on_sale'); m['_verify_scope'] = scope
        adds.append(m); log.append(f'{scope}: ADD {m.get("brand")} {m.get("model")} ({m.get("row")}, {m.get("status")})')
    sources += c.get('sources', [])
# final layer: manual decisions that must win over verifier corrections
for key, changes in base.get('final', {}).items():
    ov['models'].setdefault(key, {}).update(changes); log.append(f'final: {key} <- {changes}')
json.dump(ov, open(os.path.join(HERE, 'overrides.json'), 'w'), ensure_ascii=False, indent=1)
json.dump({'agent': 'verify', 'checked_on': '2026-10-22', 'models': adds, 'announced': [], 'discontinued_recently': [], 'sources': sources},
          open(os.path.join(HERE, '..', 'research', 'verify-additions.json'), 'w'), ensure_ascii=False, indent=1)
open(os.path.join(HERE, 'apply_log.md'), 'w').write('\n'.join(log))
print(f'{len(ov["models"])} model overrides, {len(ov["exclude"])} exclusions, {len(ov["edges_add"])} edge adds, {len(ov["edges_remove"])} edge removes, {len(adds)} additions; log lines {len(log)}')
