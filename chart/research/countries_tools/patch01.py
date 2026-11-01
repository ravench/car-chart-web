import json
P='/tmp/claude-0/-home-claude/c03e5d25-fa35-5e56-bec4-c8f6a276081e/scratchpad/carchart/research/countries/brand_countries.json'
d=json.load(open(P,encoding='utf-8'))
b=d['brands']
vw=b['Volkswagen']
vw['note']="Built mostly in Germany; T-Cross/Taigo/ID. Polo/ID. Cross in Spain, T-Roc in Portugal, Passat/Touareg in Slovakia, Caddy/Crafter in Poland, Polo (Kariega, since Pamplona ended in 2024) and Amarok (Ford Silverton) in South Africa; the Transporter/Caravelle is a rebadged Ford Transit Custom, which Ford Otosan builds in Gölcük (TR)."
for s in ["https://en.wikipedia.org/wiki/Volkswagen_Transporter_(T7)","https://en.wikipedia.org/wiki/List_of_Ford_factories"]:
    if s not in vw['sources']: vw['sources'].append(s)
mb=b['Mercedes-Benz']
if "https://en.wikipedia.org/wiki/Mercedes-Benz_G-Class" not in mb['sources']: mb['sources'].append("https://en.wikipedia.org/wiki/Mercedes-Benz_G-Class")
cad=b['Cadillac']
cad['built_in']=["US","MX","CN"]
cad['note']="Lyriq and Vistiq are built in Spring Hill (US); the Optiq is built in Ramos Arizpe (MX) and Wuhan (CN, SAIC-GM) and Wikipedia does not say which plant supplies Europe, so both are listed; either way no single foreign country."
json.dump(d,open(P+'.tmp','w',encoding='utf-8'),ensure_ascii=False,indent=1)
import os; os.replace(P+'.tmp',P)
print('patched')
