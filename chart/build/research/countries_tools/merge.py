#!/usr/bin/env python3
"""Merge a fragment JSON ({"brands": {...}, "groups": {...}}) into brand_countries.json.
Brand and group keys are ordered as in the chart's brand/group list."""
import json, sys, os
OUT = '/tmp/claude-0/-home-claude/c03e5d25-fa35-5e56-bec4-c8f6a276081e/scratchpad/carchart/research/countries/brand_countries.json'
BRANDS = ["Volkswagen","Audi","Škoda","SEAT","Cupra","Porsche","Bentley","Lamborghini","MAN","Peugeot","Citroën","DS","Opel","Fiat","Abarth","Alfa Romeo","Lancia","Jeep","Maserati","Leapmotor","Renault","Dacia","Alpine","Mobilize","Nissan","Mitsubishi","Mercedes-Benz","smart","BMW","MINI","Rolls-Royce","Toyota","Lexus","Subaru","Suzuki","Mazda","Honda","Hyundai","Kia","Genesis","Ford","Cadillac","Chevrolet","Tesla","Volvo","Polestar","Lynk & Co","Zeekr","Lotus","Farizon","LEVC","Geely","MG","Maxus","BYD","Denza","Omoda","Jaecoo","Chery","Lepas","Ebro","DR","Ora","Wey","Haval","XPeng","NIO","Firefly","Deepal","Voyah","Dongfeng","Mhero","Hongqi","Land Rover","KGM","Isuzu","Ineos","Iveco","Renault Trucks","Lucid","Ferrari","Aston Martin","McLaren","Morgan","Caterham","Bugatti","Rimac","Koenigsegg","Pagani","VinFast","Microlino","Piaggio","Aixam","Ligier","Chatenet","Casalini"]
GROUPS = ["Volkswagen Group","Stellantis","Renault Group","Nissan","Mitsubishi Motors","Mercedes-Benz Group","BMW Group","Toyota Motor","Subaru","Suzuki","Mazda","Honda","Hyundai Motor Group","Ford","General Motors","Tesla","Geely Holding","SAIC Motor","BYD","Chery","Ebro (EV Motors)","DR Automobiles","Great Wall Motor","XPeng","NIO","Changan","Dongfeng","FAW","Tata Motors","KG Mobility","Isuzu","Ineos","Iveco Group","Volvo Group","Lucid","Ferrari","Aston Martin","McLaren","Morgan","Caterham","Bugatti Rimac","Koenigsegg","Pagani","VinFast","Micro Mobility","Piaggio","Polaris","Ligier Group","Chatenet","Casalini"]
BKEYS = ["country","country_name","origin","hq","hq_entity","built_in","second_flag","note","confidence","sources"]
GKEYS = ["country","country_name","hq","hq_entity","sources"]
def load():
    if os.path.exists(OUT):
        return json.load(open(OUT, encoding='utf-8'))
    return {"checked_on": "2026-11-01", "brands": {}, "groups": {}}
def main(frag_path):
    data = load()
    frag = json.load(open(frag_path, encoding='utf-8'))
    for k, v in frag.get('brands', {}).items():
        if k not in BRANDS: sys.exit(f'unknown brand key {k!r}')
        miss = [x for x in BKEYS if x not in v]
        if miss: sys.exit(f'{k}: missing {miss}')
        data['brands'][k] = {x: v[x] for x in BKEYS}
    for k, v in frag.get('groups', {}).items():
        if k not in GROUPS: sys.exit(f'unknown group key {k!r}')
        miss = [x for x in GKEYS if x not in v]
        if miss: sys.exit(f'{k}: missing {miss}')
        data['groups'][k] = {x: v[x] for x in GKEYS}
    data['brands'] = {k: data['brands'][k] for k in BRANDS if k in data['brands']}
    data['groups'] = {k: data['groups'][k] for k in GROUPS if k in data['groups']}
    tmp = OUT + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump({"checked_on": "2026-11-01", "brands": data['brands'], "groups": data['groups']}, f, ensure_ascii=False, indent=1)
    os.replace(tmp, OUT)
    print(f"brands {len(data['brands'])}/96, groups {len(data['groups'])}/50")
    print('missing brands:', [b for b in BRANDS if b not in data['brands']][:12], '...')
if __name__ == '__main__':
    main(sys.argv[1])
