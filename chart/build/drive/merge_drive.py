#!/usr/bin/env python3
"""Merge drive/result-*.json into drive.json and report problems. Usage: python3 drive/merge_drive.py [--write]"""
import json, glob, sys, collections
d = json.load(open('data.json')); models = {m['id']: m for m in d['models']}
res = {}; src_of = {}
for f in sorted(glob.glob('drive/result-*.json')):
    try: r = json.load(open(f))
    except Exception as e: print('BAD JSON', f, e); continue
    for k, v in r.items():
        if k in res: print('DUP', k, f, src_of[k])
        res[k] = v; src_of[k] = f
ver = json.load(open('drive/verified.json')) if __import__('os').path.exists('drive/verified.json') else {}
chg = 0
for k, v in ver.items():
    if k not in models: print('VERIFIED unknown id', k); continue
    if k in res and (sorted(res[k].get('drives') or []) != sorted(v['drives']) or bool(res[k].get('awd')) != bool(v['awd'])): chg += 1; print('VERIFIED changes', k, res[k].get('drives'), '->', v['drives'])
    res[k] = v; src_of[k] = 'drive/verified.json'
print(f'{len(ver)} verified entries applied, {chg} with changed drives')
missing = [i for i in models if i not in res]; extra = [k for k in res if k not in models]
print(f'{len(res)} entries from {len(glob.glob("drive/result-*.json"))} files; missing {len(missing)}; unknown ids {len(extra)}')
if missing: print('MISSING:', ', '.join(missing[:60]))
if extra: print('EXTRA:', ', '.join(extra[:30]))
ok = {}; probs = []
for k, v in res.items():
    if k not in models: continue
    m = models[k]
    drives = [x for x in (v.get('drives') or []) if x in ('FWD', 'RWD', 'AWD')]
    awd = bool(v.get('awd'))
    if not drives: probs.append((k, 'no drives'))
    if awd != ('AWD' in drives): probs.append((k, f'awd={awd} but drives={drives}')); awd = 'AWD' in drives or awd; 
    if awd and 'AWD' not in drives: drives.append('AWD')
    if v.get('confidence') not in ('high', 'medium', 'low'): probs.append((k, f'confidence={v.get("confidence")}'))
    if m['row'] == 'quadricycle' and awd: probs.append((k, 'AWD on a quadricycle?'))
    if 'BEV' not in (m.get('powertrains') or []) and (v.get('awd_term') or '').lower() in ('dual motor',): probs.append((k, 'dual motor on a non-BEV?'))
    ok[k] = {'drives': drives, 'awd': awd, 'awd_term': v.get('awd_term') or None, 'note': v.get('note') or None, 'confidence': v.get('confidence') or 'low', 'source': v.get('source') or None}
print('problems', len(probs)); [print(' ', k, p) for k, p in probs[:80]]
conf = collections.Counter(v['confidence'] for v in ok.values()); print('confidence', dict(conf))
print('awd models', sum(1 for v in ok.values() if v['awd']), 'of', len(ok))
byrow = collections.defaultdict(lambda: [0, 0])
for k, v in ok.items(): byrow[models[k]['row']][0] += v['awd']; byrow[models[k]['row']][1] += 1
print('AWD by row:', {r: f'{a}/{n}' for r, (a, n) in sorted(byrow.items())})
low = [k for k, v in ok.items() if v['confidence'] == 'low']; print('LOW confidence:', ', '.join(low))
if '--write' in sys.argv:
    json.dump(ok, open('drive.json', 'w'), ensure_ascii=False, indent=1); print('wrote drive.json', len(ok))
