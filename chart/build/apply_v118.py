"""v1.18: add the researched quadricycle drive records to drive/verified.json, rebuild drive.json, bump the version."""
import json, subprocess, sys, ast, re
IDS = ['aixam-city', 'aixam-coupe', 'aixam-crossover', 'aixam-d-truck-e-truck', 'aixam-easy', 'aixam-e-scouty',
       'ligier-js50', 'ligier-js60', 'ligier-myli', 'ligier-pulse-4', 'chatenet-ch46', 'casalini-650']
R = json.load(open('drive/v118_quadricycles.json'))
V = json.load(open('drive/verified.json'))
missing = [i for i in IDS if i not in R]
print('researched', len(R), 'missing', missing)
for k, v in R.items():
    assert k in IDS, k
    drives = v.get('drives') or []
    assert drives and all(d in ('FWD', 'RWD', 'AWD') for d in drives), (k, drives)
    assert v.get('confidence') in ('high', 'medium', 'low'), (k, v.get('confidence'))
    assert not v.get('awd') and 'AWD' not in drives, (k, 'AWD on a quadricycle')
    assert v.get('source', '').startswith('http'), (k, 'no source')
    V[k] = {'drives': drives, 'awd': False, 'awd_term': v.get('awd_term') or None, 'note': v.get('note') or None,
            'confidence': v['confidence'], 'source': v['source'], 'quote': v.get('quote'), 'checked_on': v.get('checked_on', '2026-11-02')}
json.dump(V, open('drive/verified.json', 'w'), ensure_ascii=False, indent=1)
print('verified.json now', len(V), 'entries')
out = subprocess.run([sys.executable, '-I', 'drive/merge_drive.py', '--write'], capture_output=True, text=True).stdout
print(out[-900:])
D = json.load(open('drive.json'))
print('drive.json', len(D), 'entries; quadricycles without record:', [i for i in IDS if i not in D])
s = open('gen.py').read()
s2 = re.sub(r"CHART_VERSION = '1\.17'", "CHART_VERSION = '1.18'", s, count=1)
assert s2 != s; ast.parse(s2); open('gen.py', 'w').write(s2); print('gen.py: CHART_VERSION 1.18')
