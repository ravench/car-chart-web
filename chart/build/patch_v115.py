#!/usr/bin/env python3
"""v1.15 data corrections (2026-11-01): Wey 03 / Wey 05 facts from gwm-motor.de technical-data pages."""
import json
SRC = 'https://www.gwm-motor.de/technische-daten-wey-03'; SRC5 = 'https://www.gwm-motor.de/technische-daten-wey-05'
fixes = {
 'wey-wey-03': {'length_mm': 4668, 'other_names': ['Wey Coffee 02 (DE, 2023–24)', 'Wey Latte (China)'],
   'status': 'runout', 'status_note': "gwm-motor.de lists the WEY 03 as 'Auslaufmodell' (run-out) on 2026-11-01; length 4,668 mm, wheelbase 2,745 mm per the technical-data page (the chart had 4,520 mm, the Macchiato's length, and a wrong 'Lanshan' alias). Offered in Germany (GWM leasing listings, Oct 2026).",
   'status_sources': [SRC, 'https://www.gwm-motor.de/wey-03', 'https://www.goleasy.de/leasing/marken/gwm'], 'length_note': '4,668 mm (gwm-motor.de technical data, 2026-11-01)'},
 'wey-wey-05': {'length_mm': 4870, 'status': 'runout', 'status_note': "gwm-motor.de lists the WEY 05 Plug-in Hybrid as 'Auslaufmodell' (run-out) on 2026-11-01; length 4,870 mm, wheelbase 2,910 mm per the technical-data page. Germany: new-car offers from EUR 55,499 with configurator on carwow.de (Oct 2026).",
   'status_sources': [SRC5, 'https://www.gwm-motor.de/wey-05', 'https://www.goleasy.de/leasing/marken/gwm'], 'length_note': '4,870 mm (gwm-motor.de technical data, 2026-11-01)'},
}
d = json.load(open('data.json')); n = 0
for m in d['models']:
    if m['id'] in fixes:
        old = {k: m.get(k) for k in fixes[m['id']]}; m.update(fixes[m['id']]); n += 1
        print(m['id'], 'patched:', {k: (old[k], fixes[m['id']][k]) for k in ('length_mm', 'status')})
json.dump(d, open('data.json', 'w'), ensure_ascii=False, indent=1)
o = json.load(open('overrides.base.json')); mo = o.setdefault('models', {})
keys = {'wey-wey-03': 'wey wey 03|c-suv', 'wey-wey-05': 'wey wey 05|d-suv'}
for mid, k in keys.items():
    mo.setdefault(k, {}).update(fixes[mid]); mo[k].setdefault('_verify_sources', []).append(fixes[mid]['status_sources'][0])
json.dump(o, open('overrides.base.json', 'w'), ensure_ascii=False, indent=1)
open('apply_log.md', 'a').write('\n' + '\n'.join(f"v115: {keys[mid]} <- {json.dumps({k: v for k, v in fx.items() if k in ('length_mm','status','other_names')}, ensure_ascii=False)}" for mid, fx in fixes.items()) + '\n')
print('patched', n, 'models; overrides and apply_log updated')
