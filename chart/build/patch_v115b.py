#!/usr/bin/env python3
"""v1.15 data correction: DR 1.0 EV removed from drautomobiles.com (spring 2026) -> runout."""
import json
fix={'status':'runout','status_note':"drautomobiles.com no longer lists the DR 1.0 (menu, pages API and sitemap show DR 3, 5, 6, 8 and PK8 only; the site's last DR 1.0 uploads date from spring 2026, checked 2026-11-01), so it is treated as run-out stock. Italy, September 2026 third-party price list: DR 1.0 EV 61 CV / 31 kWh / 210 km WLTP, EUR 18,900 (il Giornale Digitale, updated 2026-09-10).",
     'status_sources':['https://drautomobiles.com/','https://www.ilgiornaledigitale.it/dr-tutti-modelli-prezzi-gamma-completa-italia-82371.html']}
d=json.load(open('data.json'))
for m in d['models']:
    if m['id']=='dr-dr-1-0-ev': print('old',m['status']); m.update(fix)
json.dump(d,open('data.json','w'),ensure_ascii=False,indent=1)
o=json.load(open('overrides.base.json')); o.setdefault('models',{}).setdefault('dr dr 1.0 ev|a-city',{}).update(fix); json.dump(o,open('overrides.base.json','w'),ensure_ascii=False,indent=1)
open('apply_log.md','a').write("v115: dr dr 1.0 ev|a-city <- {'status': 'runout'} (removed from drautomobiles.com, 2026-11-01)\n"); print('patched')
