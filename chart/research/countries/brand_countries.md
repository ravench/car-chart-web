# Brand countries – summary (checked 2026-11-01)

Data: `brand_countries.json` (96 brands, 50 groups). Sources: English Wikipedia (lead sentence + infobox + production
sections, model pages for the ambiguous brands); brand legal notices or registries only where Wikipedia gives no head
office (Citroën/DS, Alpine, Chatenet); one trade-press item each for DR (antitrust ruling) and Isuzu (D-Max EV).
About 165 WebFetch calls in all.

**Rule applied:** `country` = the country of the head office that Wikipedia gives for the company running the brand.
`second_flag` = the single foreign country where (nearly) all European-market models are assembled, otherwise null.
`built_in` = the assembly countries of the European-market models, most important first. Where Wikipedia does not
name the plant supplying Europe, every candidate plant is listed and the note says so (Polestar 4, Cadillac Optiq, Lucid).

## Second flags (6)
| Brand | Flag | Second flag | Why |
|---|---|---|---|
| MAN | DE | PL | The TGE is a VW Crafter built in Września |
| Mobilize | FR | MA | Duo (runout, production ended Dec 2025) built at Renault Tangier |
| DR | IT | CN | Rebadged Chinese cars; the Italian antitrust authority (AGCM, 2024) found them "predominantly manufactured in China", with only finishing done in Italy |
| Isuzu | JP | TH | D-Max from Isuzu Motors Thailand (the European source is from trade press; Wikipedia lists TH/CN/ZA plants) |
| Ineos | GB | FR | Grenadier/Quartermaster built in Hambach |
| Microlino | CH | IT | Built in Micro's own Turin factory (developed with Cecomp) |

## Ambiguous cases and how the rule decided them
- **MG → CN, no second flag** (medium). Wikipedia's lead calls MG Motor "a British automotive manufacturer owned by SAIC", but its infobox gives *Shanghai (main office)*, with Birmingham only as the European office, and says MG is a division of SAIC's passenger-car branch. All European MGs come from China. If the chart prefers marque origin, use GB with second flag CN.
- **smart → CN, no second flag.** The marque is German (Swiss-born), but Smart Automobile Co. (Mercedes/Geely 50:50) has its head office in Ningbo and builds the cars in Xi'an. Smart Europe GmbH in Stuttgart only handles sales.
- **Lynk & Co → CN, no second flag.** Wikipedia's lead and infobox give Hangzhou. Gothenburg is the European office, and Volvo Cars has been the exclusive importer since March 2026. Wikipedia lists only Chinese plants (01 and 08 in Meishan/Ningbo, 02 in Zhangjiakou) and does not mention Ghent, so the "01 from Ghent" assumption is not supported.
- **Polestar → SE, no second flag.** The 2, 4 and 5 are built in China. Since March 2026 the 3 has been built only in Ridgeville (US), and the 4 is also built in Busan (KR). Three Chinese-built models out of four is not "nearly all"; CN would be the majority-rule answer.
- **Lotus → GB, no second flag.** Emira and Evija are built in Hethel; Eletre and Emeya in Wuhan. Wikipedia still gives Hethel as head office, although Lotus Cars was folded into the Wuhan-based Lotus Technology in August 2026.
- **Volvo → SE**: Torslanda, Ghent, China and Ridgeville. **Tesla → US, no second flag**: Model Y from Grünheide (DE), Model 3 from Shanghai (CN), so two foreign countries.
- **Cupra → ES**: Martorell (Formentor, Leon, Raval), Zwickau (Born), Győr (Terramar) and Anhui (Tavascan). **Dacia → RO**: Mioveni, Tangier (Jogger since July 2024, part of Sandero), Bursa (Striker), Novo Mesto (Spring II) and China (runout Spring I).
- **Mitsubishi → JP**: ASX and Grandis from Valladolid, Eclipse Cross from Douai, runout Colt from Bursa, Outlander from Japan, L200 from Thailand. **Nissan → JP**: Sunderland, Renault plants in France, and Japan.
- **MINI → GB** (medium; Wikipedia gives "Country: United Kingdom" and no head-office row, so Oxford is used): Oxford, China (Spotlight JV) and Leipzig. **Land Rover → GB**: no head-office row for the brand, so JLR's Whitley, Coventry office is used. Solihull and Halewood build most models; Defender and Discovery come from Nitra (SK).
- **Jeep → US, no second flag**: Avenger from Tychy (PL), Compass from Melfi (IT); only the runout Wrangler and Grand Cherokee come from the US.
- **Leapmotor → CN**: imported from China, except the B05 (and the B10 from 2026) from Zaragoza. T03 assembly in Tychy ended in March 2025.
- **Ebro → ES, no second flag**: Chery designs assembled from CKD kits in Barcelona Zona Franca, so the assembly country is Spain. The same reasoning gives **Piaggio → IT** (Porter NP6 assembled in Pontedera from Foton components).
- **XPeng → CN**: Wikipedia says European cars are built with Magna Steyr in Graz (the G6 lists Graz), but the X9 lists only Asian plants, so the range is mixed.
- **Bugatti → FR** (Molsheim), owned by Bugatti Rimac (HR). Rimac Group holds 55 % and HOF Capital 45 % since Porsche sold its stake in April 2026. **Rimac → HR.** **Caterham → GB** (Dartford; Japanese-owned by VT Holdings). **Renault Trucks → FR** (Saint-Priest; Volvo Group). **Aixam → FR** (Polaris-owned; the infobox now shows Polaris with 44 %).
- **Groups:** Stellantis is NL (Hoofddorp). Iveco Group is IT (Turin HQ, incorporated in Amsterdam; the Tata sale was due to close in H1 2026). Tata Motors is IN (Mumbai; demerged on 1 Oct 2025). Ebro (EV Motors) is ES (Wikipedia's Ebro infobox lists Chery as owner). McLaren is GB (owned by CYVN, Abu Dhabi).

## Not verified, or verified only partly (the reason for the 8 "medium" entries)
- **Head office not on Wikipedia, inferred from the parent:** Mobilize (Renault, Boulogne-Billancourt), Maxus (SAIC, Shanghai), Lepas (no article; Chery, Wuhu), MINI (Oxford). Also Genesis, Ora, Wey, Haval and Firefly, where the country is certain. Farizon's city is not given ("China").
- **European supply plant not stated:** Cadillac Optiq (Ramos Arizpe MX or Wuhan CN), Polestar 4 (Ningbo or Busan), diesel Isuzu D-Max (Thailand assumed), Lucid (Casa Grande assumed; KAEC final assembly serves Saudi Arabia), Honda HR-V, Toyota Hilux (not listed), Kia EV5, Deepal (Thai plant serves right-hand-drive Asia-Pacific markets), BYD Szeged (start of production not confirmed; Rayong has exported the Dolphin to Europe since August 2025), Omoda/Jaecoo Barcelona assembly (planned, not confirmed).
- **Plants taken from the chart's model notes or the group plant lists, not from a model page:** Iveco eJolly/eSuperJolly (Stellantis K0/Ducato plants), Toyota Proace family, Suzuki Swift (Japan), Nissan X-Trail (Japan), Mercedes G-Class (Graz; the Wikipedia page lags a generation), and VW Transporter T7 (a Transit Custom twin; Ford Otosan Gölcük per the Ford factory list).
- **Fetches that failed or returned nothing useful:** the batch Wikipedia API (URL rejected / not found), a category page, wrong titles (Citroën Ami (2020), Smart #1, Xpeng_* in lowercase; later retried with the correct titles), "Dacia" (the ancient region; retried as Automobile Dacia), and Outlander/Triton/Transporter T7/Iveco Daily, whose fetched text had no assembly field.
