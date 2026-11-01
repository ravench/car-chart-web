# Light quadricycles (L6e/L7e): classic makers

Research notes for the "quadricycle" row. Agent: quadricycle research (Claude). Checked 2026-10-27.
Output: `research/quadricycles.json`, 12 records. As the task asked, the file is a plain JSON list of records (other research files wrap their records in an object with a `models` key). Each record also has a `pictures` list.

## Result in brief

| Brand | Group label | Tiles | Models |
|---|---|---|---|
| Aixam | Polaris | 6 | Easy, City, Coupé, Crossover, e-Scouty, D-Truck / e-Truck |
| Ligier | Ligier Group | 4 | JS50, JS60, Myli, Pulse 4 |
| Microcar | Ligier Group | 0 | Brand ended at the end of 2024 |
| Chatenet | Automobiles Chatenet | 1 | CH46 |
| Casalini | Casalini | 1 | 650 |

- **Group labels.** These brands are not in the brief's canonical table, so the label is the parent company, per the brief's rule: Polaris Inc., Ligier Group SAS, Automobiles Chatenet SA and Casalini S.r.l.
- **Twins.** There are no tier-1 pairs. Two tier-2 groups:
  - Aixam Easy, City, e-Scouty, Coupé and Crossover;
  - Ligier JS50 and JS60.
- **Pictures.** Nothing was downloaded. Every image host refused the container (the proxy answered CONNECT with 403), so all pictures are marked "needs browser fetch".
  - Only three likely side views were identified, from file names and gallery titles (not seen): the Aixam Easy and the two Aixam Pro D-Truck bodies.
  - The angle of every other candidate is unknown.

## Method and limits

- **How pages were read.** Manufacturer sites were read first, then trade press, then Wikipedia. Pages were read as text, which cannot show images. So angle, facing, background and width are known only where a filename or alt text gives them.
- **Images were not downloaded.** curl got "CONNECT tunnel failed, response 403" from every host, and none were retried, as instructed. The hosts were:
  - aixam.com, aixam.de, aixam-pro.com, aixam-mega.com and steck-automobile.ch;
  - s3.ligier.fr and media.ligier.fr;
  - automobiles-chatenet.com, casalini.eu and bellier.fr;
  - cdn.motor1.com, upload.wikimedia.org, commons and carsized.com.
- **Pages that could not be read:**
  - ligier.ch and vision-mobility.de (client error);
  - chatenet.com, estrima.com and lejournaldesentreprises.com (robots.txt);
  - xev-global.com (JavaScript only);
  - pappers.fr, the Commons model categories, and automobile-propre's full sans-permis catalogue.
- **Domains that point elsewhere:**
  - aixam.ch redirects to Steck Automobile AG.
  - chatenet.fr is a parked hosting page; the maker's site is automobiles-chatenet.com.
  - casalini.it now redirects to a bookseller, casalinilibri.com; the maker's site is casalini.eu.
  - microcar.fr redirects to ligier.fr.
- **Spam on bellier.fr.** The home page carries an unrelated online-pharmacy spam paragraph. It was treated as data and ignored; the site may be compromised.
- **carsized.com.** No entries for these makers were found. vehiclesizes.com has pages for "Ligier JS50 II (2025)", "Ligier JS60 (2021)" and "Aixam Ambition Coupé (2024)", but they returned a client error.
- **Commons.** Only "Category:Aixam vehicles" (6 subcategories, 65 files) was confirmed to exist. No model categories were confirmed.
- **Category codes.** The manufacturers' pages say "voiture sans permis", 45 km/h, or B1/75 km/h. They do not print the L6e/L7e codes, so the codes in `body` are inferred from those statements.

## Aixam (group: Polaris)

### Ownership

- **2013 acquisition.** Polaris Industries announced on 11 Apr 2013 that it had bought Aixam-Mega. The sellers were AXA Private Equity (now Ardian), Euromezzanine, Dentressangle Initiatives and others. Sources: [polaris.com](https://www.polaris.com/en-us/news/company/polaris-acquires-aixam-mega/), [marketscreener](https://www.marketscreener.com/quote/stock/POLARIS-INC-14008/news/Polaris-Industries-Inc-acquired-Groupe-AIXAM-MEGA-from-AXA-Private-Equity-Euromezzanine-5-FCPR-f-39099680/), [Clearwater](https://www.clearwatercf.com/experience/transactions/clearwater-advises-ardian-and-norbert-dentressangle-on-the-sale-of-aixam-mega-group-to-polaris-industries/) and [Wikipedia](https://en.wikipedia.org/wiki/Aixam).
- **No sale found.** Nothing shows that Polaris has sold Aixam.
  - On the Q1 2026 call (28 Apr 2026), Polaris created a new reportable segment, "Aixam & Goupil". It did not announce a sale. Source: [finance.biggo transcript](https://finance.biggo.com/quote/PII/earnings-call/US_PII_2026-04-28).
  - The FY2025 10-K lists Aixam and Goupil as brands. The only divestiture it describes is Indian Motorcycle, agreed in Oct 2025 and closed in Q1 2026. Source: [financialfilings](https://financialfilings.com/filings/polaris-inc/annual-report/2026/25860865/).
  - The Q2 2026 release (28 Jul 2026) still reports the "Aixam & Goupil" segment and mentions no sale. Source: [SEC](https://www.sec.gov/Archives/edgar/data/931015/000162828026049902/pii-q22026earningsrelease.htm).
  - The Q3 2026 release was scheduled for 27 Oct 2026 and was not checked.
- **Still active.** In June 2026 Aixam was investing about €30M in a new plant (Il Sole 24 Ore; journalauto). Aixam exhibited at the Mondial 2026 ([mondial.paris](https://mondial.paris/?p=97704)).
- **Unexplained figure.** The Wikipedia infobox says "Polaris 44%" without explanation. This could not be verified.

### Model list and evidence

The manufacturer's model list ([aixam.com model page](https://www.aixam.com/fr/nos-modeles-de-voitures-sans-permis)) has these families:
- Gamme AIXAM: Easy, City, Coupé and Crossover, with diesel ("thermique") versions;
- Gamme eAixam: the electric Easy, City, Coupé and Crossover;
- Gamme MEGA: e-Scouty;
- Gamme AIXAM PRO: D-Truck and e-Truck, on [aixam-pro.com](https://www.aixam-pro.com).

| Tile | Official versions (FR) | Length, wheelbase | CH (Steck) | DE (aixam.de) |
|---|---|---|---|---|
| Easy | Access, Chic, GT; diesel from €11,499, electric 75 or 113 km | 2,773 mm, 1,795 mm | not listed | Access/Chic, Diesel/Elektro |
| City | Pack, Sport, GTO; e-City Pack (75 km) and Pack/Sport/GTO 7.5 kWh (113 km) | 2,789 mm, 1,795 mm | City Pack (from CHF 16,390), City Sport, E-City Sport | yes, plus eCity on the Welmo list |
| Coupé | Sport (€17,799), GTI; electric versions | 3,000 mm, 2,000 mm | Coupé Sport, E-Coupé Sport | yes |
| Crossover | Pack (€16,699), Premium; Premium électrique | 3,000 mm, 2,000 mm | Crossline Pack, Crossover Premium, E-Crossover Premium | yes |
| e-Scouty | Evo, 5.02 kWh, 75 km, €13,499 ("Gamme MEGA") | 2,650 mm, 1,795 mm | not listed | not listed |
| D-Truck / e-Truck | Plateau ridelles, Fourgon; D-Truck from €15,499 excl. VAT, e-Truck from €16,083 excl. VAT | 3,000 mm, 2,252 mm | D-Truck Van, E-Truck Alu Pritsche | D-Truck/eTruck Pritsche/Van |

- **Switzerland.** aixam.ch redirects to [Steck Automobile AG](https://www.steck-automobile.ch/de/aixam) in Bigenthal, which calls itself an "offizieller Partner" of Aixam.
  - Steck's page does not use the word "Generalimporteur". The official domain redirecting to Steck is taken as evidence of an official channel.
  - Steck lists City, Coupé and Crossover (diesel and E-) and the Pro range. It does not list the Easy or the e-Scouty, so those two have `ch_on_sale = null`.
- **Germany.** aixam.de is run by Leichtmobile GmbH & Co. KG. Its news mentions the new "Modellreihe AIXAM S10-2". Berlin's Welmo subsidy list (dated 21 Sep 2026) includes eCity Pack/Premium, eCoupé Premium/GTi, ePritsche and eVan.
- **Range history.**
  - Ambition range: Oct 2023 ([motor.es](https://www.motor.es/noticias/aixam-gama-ambition-coches-sin-carnet-202398175.html)).
  - S10-2 update: June 2026. It keeps the City, Coupé and Crossover bodies, with "dos longitudes de chasis, corto y largo" ([motor.es](https://www.motor.es/noticias/aixam-gama-s10-2-2026114937.html)).
  - The Easy (April 2026) replaces the Minauto. Wikipedia calls it an updated Minauto with a new front end.
- **Mondial 2026.** Aixam showed a new Easy GT trim (€12,990 electric, €13,599 diesel), the 58 cm panoramic display, and a new 11.01 kWh e-Truck battery (165 km).
- **Tile decisions:**
  - e-versions are powertrains of the same tile.
  - "Crossline" is only the name of the Pack version in CH (and appears in aixam.de file names), so it shares the Crossover tile.
  - D-Truck and e-Truck share one tile: same vehicle, diesel or electric.
  - The 2023 "Tiny Van" camper is no longer in the Pro range and is not tiled.
- **e-Scouty brand column.** aixam.com sells it in the MEGA range, and Wikipedia calls it the "Mega e-Scouty". It is kept in the Aixam column with "Mega e-Scouty" in other_names. The owner may prefer a separate "Mega" brand.

## Ligier Group (Ligier; Microcar)

### Ownership

- **Formation.** Ligier Group was formed in 2008 from Ligier Automobiles and Microcar (press-release boilerplate).
- **Size.** Revenue was €192M in 2024. Ligier says it builds more than 14,000 vehicles a year, 100% in France, at Abrest (Allier).
- **Ownership changes:**
  - 2016: 21 Centrale Partners sold its stake to a pool led by Siparex, with Edify as a minority shareholder ([vichy-economie](https://www.vichy-economie.com/actualite/ligier-change-dactionnaires/); [Lincoln International](https://www.lincolninternational.com/transactions/21-centrale-partners-has-sold-ligier-group-to-edify-and-groupe-siparex/)).
  - January 2021: Edify (formerly Somfy Participations) agreed to buy the group alongside its chief executive, François Ligier ([autoactu, 11 Jan 2021](https://www.autoactu.com/actualites/voitures-sans-permis-le-groupe-ligier-rachete-par-le-fonds-edify)). Siparex exited ([siparex.com](https://www.siparex.com/en/ligier-group-restructures-its-equity-with-siparex-exiting-and-edify-increasing-its-shareholding-interest/)).
  - No later change was found. The current percentage split between Edify and the Ligier family is not published.
- **Microcar factory.** The Microcar plant at Montaigu-Boufféré (Vendée) closed in early 2025 ([journalauto](https://journalauto.com/constructeurs/ligier-se-reorganise-et-ferme-une-usine-en-vendee/); [cleanrider](https://www.cleanrider.com/actus/pionnier-de-la-voiture-sans-permis-ligier-ne-va-pas-fort/)).

### Model list and evidence

- **Passenger range.** [ligier.fr](https://www.ligier.fr/) and [ligier.de](https://www.ligier.de/) list four models: JS50, JS60, Myli LAB and Myli MAX.
- **75 km/h versions.** [ligier.fr/voitures-permis-b1/](https://www.ligier.fr/voitures-permis-b1/) offers 75 km/h L7e electric versions (B1 licence): Myli MAX €14,999, JS50 €15,999, JS60 €16,999.
- **Utility range.** [Ligier Professional](https://www.ligier-professional.fr) lists:
  - Pulse 4, a 4-wheel electric utility vehicle;
  - Pulse 3, which has 3 wheels and is excluded;
  - Pulse 2, a cargo bike, also excluded.
- **JS50.** The "Nouvelle JS50" opened for orders at the Mondial 2024, with first deliveries in November 2024 ([press kit](https://media.ligier.fr/app/uploads/2024/11/Mondial-2024-Dossier-de-presse-FR.pdf)).
  - Trims: Select, Élite and Ultimate, €14,999–18,999.
  - Powertrains: REVO D+ diesel (499.8 cc) or electric with an 11.04 kWh battery (159–164 km WMTC).
  - The new 11 kWh battery was announced on 14 Apr 2026 for the JS50 and Myli MAX ([press release](https://media.ligier.fr/communique-de-presse/ligier-lance-sa-nouvelle-gamme-de-voitures-sans-permis-electriques-ultra-performantes/)).
  - Ligier publishes no dimensions. The length of 2,972 mm comes from motor.es. quecochemecompro gives 2,992 in its table and 2,972 in its text.
- **JS60.** The "Nouvelle JS60" was announced in a press release dated 23 Sep 2026 ([page](https://media.ligier.fr/communique-de-presse/nouvelle-ligier-js60-la-ligier-qui-voit-plus-grand/), [PDF](https://media.ligier.fr/app/uploads/2026/09/2026.09-CP-NOUVELLE-JS60.pdf)).
  - Size: 2,998 × 1,499 × 1,529 mm, with an aluminium monobloc chassis.
  - Trims: Select, Elite and Ultimate. Diesel from €16,499, electric from €16,999.
- **Myli.** The press release of 13 Jan 2026 ([link](https://media.ligier.fr/communique-de-presse/ligier-fait-evoluer-myli-encore-plus-accessible-plus-expressive-et-plus-polyvalente-que-jamais/)) presents LAB and MAX as two versions of the revised Myli.
  - Myli LAB: diesel €12,499; 6 kWh electric €10,999.
  - Myli MAX: diesel and 6 kWh electric €13,999; 11.04 kWh electric €14,999, as L6e or as L7e (75 km/h).
  - Kept as one tile. ligier.fr shows LAB and MAX as separate model pages, so split them if the chart follows the website menu.
  - Length 2,958 mm (motor.es); Caradisiac gives 2.96 m.
- **Pulse 4.** Short body (L6e, 2,600 mm) or long body (L7e, 3,356 mm); box or flatbed bodies.
  - Battery 2 × 5.51 kWh, up to 161 km. Price on quote; configurable on store.ligier.fr.
  - `length_mm` uses the long body (3,356 mm), to match the long-body press pictures.
- **Switzerland.** No evidence either way: ligier.ch could not be read, and swisscarinfo shows only the old JS50 type approval (6LA615, 2013). All Ligier records have `ch_on_sale = null`.

### Microcar: no tiles

- [sans-p.fr](https://sans-p.fr/modeles/microcar/) says the group announced the end of the Microcar brand in 2024. Since 1 Jan 2025 every new vehicle is sold with the Ligier badge, and a Microcar can only be bought used. The last models, the M.Go and the Dué, were built until the end of 2024.
- Wikipedia says the brand was discontinued and the Montaigu factory closed in early 2025.
- [caroom.fr](https://www.caroom.fr/guide/voiture-neuve/voiture-sans-permis) (26 Oct 2026) says "Microcar est désormais vendu sous la marque Ligier".
- microcar.fr redirects to ligier.fr.
- **Rebadges.** None of the current Ligier models is a rebadged Microcar. The Myli has been a Ligier since 2023. The Ligier pages show no M.Go- or Dué-derived model.
- **Microcar Flex.** No 2026 evidence of a "Microcar Flex" utility was found.

## Chatenet (group: Automobiles Chatenet)

- **Company.** Automobiles Chatenet SA, Pierre-Buffière (Haute-Vienne), was founded in 1984 by Louis-Georges Chatenet (Wikipedia).
  - [verif.com](https://www.verif.com/societe/AUTOMOBILES-CHATENET-330763566/) shows the company is active with no collective proceedings. The chief executive (PDG) is David Chatenet; Florence and Marie Chatenet sit on the board. Revenue was €11.89M in 2024.
  - It is described as family-run, but the shareholding itself is not published.
- **Range.** [automobiles-chatenet.com](https://www.automobiles-chatenet.com/) lists only the CH46:
  - CH46 K Series, K SL and K Sportline RR: Kubota Z482 diesel, 480 cc, 6 kW, Euro 5+. A news item about the new engine is dated 07.05.2026.
  - CH46e SL and Sportline RR: 9.4 kWh LiFePO4 battery, Valeo 48 V 6 kW motor, 120 km WMTC.
  - All five versions form one tile. The site shows no prices.
- **Length.** 2,977 mm (width 1,492, height 1,457, wheelbase 1,988) comes from [autocentrum.pl](https://www.autocentrum.pl/dane-techniczne/chatenet/ch46/), a secondary source. In the official owner's manual the dimension table is an image that could not be read.
- **Sales channels.** The site's importers page lists only importers outside Europe. In France the CH46 is sold through multi-brand licence-free-car dealers (Moderne Auto; APH, "distributeur Casalini et Chatenet"), and caroom lists the CH46 K and CH46e as available new. No CH or DE channel was found, so `ch_on_sale = null`.

## Casalini (group: Casalini)

- **Company.** Casalini S.r.l., Piacenza, was founded in 1939 by Giovanni Casalini.
  - casalini.eu and Wikipedia name only the founder; the current owners are not stated.
  - Wikipedia names two related supplier companies, Mech-Plant S.r.l. and Target S.r.l.
- **Range.** [casalini.eu](https://www.casalini.eu/) (image uploads from Sept/Oct 2026) presents only the "Gamma 650": Starter, Xtreme (SUV-styled) and Sportiva.
  - Engine: Kubota twin-cylinder with an SCR and DPF system Casalini developed itself.
  - French dealers list it new and as diesel (Kubota Euro 5+) from June 2026, from €18,900 (Sportiva shown at €21,900) ([example](https://www.annonces-automobile.com/d/6038252)).
  - The Austrian general importer M+B Riedhart lists "M20 650 Sportiva" (€24,580) and "M20 650 Modell" (€21,590), model year 2026 ([autoscout24.at](https://www.autoscout24.at/haendler/m-b-riedhart-casalini-generalimporteur-austria/fahrzeuge?atype=C)).
- **Not tiled.** The same importer lists a new electric "eKERRY MAXXI TR" utility, but casalini.eu does not show the Kerry, so it is not tiled. This was not verified.
- **Length.** Not found; it must be filled in before the tile is drawn to scale.
- **Earlier range.** It is likely, but not verified, that the 650 replaces the M20/550 range (M20, Trofeo, GranSport).
- **Switzerland.** No CH channel was found, so `ch_on_sale = null`.

## Twin reasoning

- **Tier 1.** None.
  - No current Ligier model is a rebadged Microcar.
  - Chatenet and Casalini share nothing found except their engine supplier (Kubota) and some French multi-brand dealers.
  - Aixam also uses Kubota diesels.
  - Under the brief, sharing an engine supplier gives no tier.
- **Tier 2, Aixam:** Easy, City, e-Scouty, Coupé and Crossover.
  - motor.es describes the 2026 range as one line-up with a short and a long chassis.
  - Official spec sheets give the same 1,345 mm tracks and 1,500 mm width, and the same drivetrains, across all five.
  - Short chassis (1,795 mm wheelbase): Easy, City, e-Scouty. Long chassis (2,000 mm): Coupé, Crossover.
  - Wikipedia: Crossline/Crossover are crossover versions of the City; the e-Scouty is "technically very similar to the Aixam e-City".
  - The task brief itself gives City/Crossline/Coupé as an example of a shared platform.
  - **Caveat 1.** brief.md defines tier 2 as "similar wheelbase". The 205 mm gap (about 11%) is larger than in the car examples, so a strict reading gives two groups: {Easy, City, e-Scouty} and {Coupé, Crossover}.
  - **Caveat 2.** For the Easy, the shared chassis is inferred from identical dimensions; Aixam does not say so.
  - The D-Truck/e-Truck (2,252 mm wheelbase) is left out.
- **Tier 2, Ligier:** JS50 and JS60.
  - The JS60 press release describes the car relative to the JS50: roof +5 cm, boot +110 L, sill −15 cm.
  - The two have nearly the same length (2,998 vs 2,972 mm), identical width, and the same powertrains and trims.
  - Ligier never says "same platform", so confidence is moderate.
- **Myli: no tier.** Its wheelbase (1,830 vs 1,828 mm), width and powertrains match the JS50. But Ligier presents it as designed from the start as an electric car with an all-aluminium chassis, and no source says it shares a platform with the JS50.

## Survey: other quadricycle makers (4 wheels, new, official channel in CH, DE or FR)

| Maker / models | Evidence | Recommendation |
|---|---|---|
| **Silence S04** (Acciona): Unico and Vivo (L6e), Plus (L7e), Cargo (L6e or L7e); 2,280 mm | Sold only through Nissan's European dealers, about 50 in DE ([electrive, 31 Oct 2025](https://www.electrive.net/2025/10/31/e-auto-fuer-9-990-euro-silence-bringt-strom-floh-mit-4-kw-nach-deutschland/)). nissan.de lists the "Klein-Elektrofahrzeug S04" (see renault-alliance.md). FR status "Commercialisé" ([automobile-propre](https://www.automobile-propre.com/voitures/silence-s04/), updated Jan 2026). Listed at €9,990 among the cheapest new quadricycles ([mondial.paris, Aug 2026](https://mondial.paris/?p=82006)). On the Welmo list (Sep 2026). | **Include**: brand Silence, group Acciona. Stays Silence-branded at Nissan, so not a Nissan twin. |
| **Linktour Alumi** (Shandong Weiqiao Pioneering): L6e Alumi/Plus/Pro, L7e Elite/Elite+; 2,685 mm | FR importer Modelabs; launched 16 Jun 2026; sold on the Linktour site, Fnac.com and Darty.com, with dealers from Oct 2026 ([journalauto](https://journalauto.com/constructeurs/linktour-choisit-modelabs-pour-importer-ses-minivoitures-en-france/)). "Commercialisé" from €10,690 ([automobile-propre](https://www.automobile-propre.com/voitures/linktour-alumi/)). | **Include** (FR) |
| **Jiayuan**: City Fun (L6e), City Van / City Van 80 (L7e), City Cargo | ASPP e-tech is the exclusive FR distributor ([byaspp](https://www.byaspp.com/details-aspp+e-tech+distributeur+exclusif+de+la+marque+jiayuan+propose+des+vehicules+disponibles+immediatement+partout+en+france-526)). New prices: City Fun €12,980, City Van €20,166 ([voltandgo, Sep 2026](https://voltandgo.com/marques/jiayuan/)). caroom (Oct 2026) lists City Fun and City Van. | **Include** (FR): City Fun as a passenger tile; City Van/Cargo as a utility tile if wanted. Lengths not found. |
| **Bellier**: B8 (Italia, Soft, Série C, S Line), Cabriolet, Docker HDI utility | [bellier.fr](https://www.bellier.fr/) was modified 23 Oct 2026; Docker HDI has a Lombardini 480 cc diesel and 200 kg payload. caroom (Oct 2026) lists B8 and Docker as available new. Bellier Automobiles SAS, Talmont-Saint-Hilaire, created Aug 2010: revenue €1.46M in 2024, loss €453k, 7 staff ([xerfi](https://www.xerfi.com/etudes-par-entreprise/bellier-automobiles_524350204)). lelynx says Sermat has owned it since 2010; not confirmed. | **Include** (FR), small maker. No prices published (dealer contact only). Lengths not found, apart from a Docker dimension drawing. |
| **Kilow La Bagnole** (Savoy International Kilow, Haute-Savoie): buggy, L6e 45 km/h and L7e 80 km/h; Kilow Pro | 15 dealers in France, 20 units/week, 600 deliveries planned for 2026; new features shown at the Mondial 2026 ([automobile-propre, 12 Oct 2026](https://www.automobile-propre.com/articles/kilow-buggy-electrique-nouveautes-mondial-automobile-paris-2026/)) | **Include** (FR). Length and price not found. |
| **XEV Yoyo**: L7e, 2,530 mm | XEV's issuer press release (14 Apr 2026) says sales and deliveries have started in Italy and Germany, through direct customer-to-manufacturer orders. XEV YOYO is on the Welmo list. The website is JavaScript-only, so ordering could not be checked. | **Tentative include** (DE) |
| **Estrima Birò**: 4 wheels, about 1.74 m (Wikipedia), Small/Big 45/60 | Welmo list gives DE net prices (Biro Small 45 €12,601 up to Big 60 €15,962). Birò Deutschland GmbH (Munich) was set up in 2023. H1 2026 results mention a relaunch of Birò sales. In FR only an AD garage listing was found, which is not an official dealer. | **Tentative include** (DE); no official dealer list could be read |
| **ARI Motors** (DE): 452 (45 km/h), 802 (L7e), Bruni 2/4-seater (L7e), 458 Pro utility | On the Welmo list with prices. The ari-motors.com pages give neither wheel counts nor categories for every model; the 458 Pro page mentions N1. | **Borderline**: check wheel counts and categories first |
| **Ipop** (Alsace): Ipop 45 (L6e) €11,000; Ipop 90 (L7e) €15,000/€17,000 4WD | Orders taken with a refundable €1,500 deposit; first deliveries March–September 2027 ([rouleur-electrique, May 2026](https://rouleur-electrique.fr/ipop-le-quadricycle-electrique-francais-a-moteurs-dans-les-roues-qui-defie-la-citroen-ami/)) | **Announced only**: status "announced" if added |
| **Simplici S1** (SimpliciCar, FR; built by an unnamed Chinese maker); 2.61 m, €8,999 | Sold through the franchise network from June 2024. About 40 sites were selling it in March 2025 ([journalauto](https://journalauto.com/distribution/vsp-simplicicar-autorise-des-tiers-a-vendre-la-simplici-s1/)). No 2026 evidence. | **Unverified**: possibly a rebadged Chinese model, maker unknown |
| **Eon Motors Weez**: 3,000 mm | Wikipedia (first deliveries 2023) and older press only; no 2025–26 sales evidence | **Unverified / exclude for now** |
| **Secma** | Status not researched in depth | **Unverified** |
| **Tazzari** | No evidence of current Zero production; the group moved into electric motorcycles (Italian Volt) | **Exclude** |
| **JDM** | No buyer found; liquidated in 2014 ([journalauto](https://journalauto.com/constructeurs/jdm-na-pas-trouve-de-repreneur/)) | **Exclude** |
| **Grecav** | Only used cars and old press | **Exclude** |
| **Zhidou** | Only used cars (otomoto, autosupermarket) | **Exclude** |
| **Microcar** | Brand ended at the end of 2024 (see above) | **Exclude** |
| **"Regis"** | No quadricycle maker of that name could be identified | n/a |
| **Goupil** (Polaris) | Utility EV; left untiled by the LCV research (lcv.md) | Out of scope here |

- **Context sources:**
  - caroom.fr guide (26 Oct 2026). It lists the brands available new in FR: Aixam, Bellier, Casalini, Chatenet, Citroën, Fiat, Jiayuan, Ligier, and Mobilize (stock only).
  - JATO, on the 2025 FR/IT quadricycle market.
  - The Shift Project's note on quadricycles (June 2026).
- **Not researched:** utility light vehicles on the Welmo list (Tropos, Paxster, Kyburz, Alke, EVUM). Kyburz is mostly 3-wheeled. The owner should decide whether these belong in the quadricycle row.

## Discontinued or not tiled (2024–2026)

- **Microcar M.Go and Dué:** brand ended at the end of 2024; sold under the Ligier badge only since 1 Jan 2025 (sans-p.fr).
- **Aixam Minauto:** replaced by the Easy in April 2026.
- **Aixam Tiny Van (2023):** not in the current Aixam Pro range.
- **Ligier Pulse 3 and Pulse 2:** excluded; 3 wheels and a cargo bike.
- **Casalini M20/M14 and 550 names:** apparently replaced by the 650; only used and older listings were found.

## Open questions

1. **Aixam ownership.** The Wikipedia "Polaris 44%" is unexplained, and the Polaris Q3 2026 release (27 Oct 2026) was not checked.
2. **Aixam tier-2 grouping.** Decide whether it stays one group or splits by wheelbase. Also decide whether the e-Scouty belongs in an Aixam or a Mega column.
3. **Swiss availability.** Unknown for the Aixam Easy and e-Scouty, all Ligier models, Chatenet and Casalini.
4. **Lengths.** The Casalini 650 length is unknown. The JS50 length is 2,972 vs 2,992 mm depending on source. The CH46 length (2,977) comes only from a secondary source.
5. **Myli tiles.** Decide between one tile and two (LAB and MAX), and whether the Myli is a tier-2 platform sibling of the JS50.
6. **Survey checks:**
   - ARI wheel counts and categories;
   - whether Simplici S1, Jiayuan or Linktour share a Chinese base vehicle;
   - whether the XEV Yoyo and Estrima Birò can really be ordered in DE.
7. **Picture angles.** No picture was seen. Apart from the three likely side views (and one Casalini file named "front"), angles are unknown. Facing and background are unknown for every picture; widths are known only from size suffixes in four file names.

## Picture URLs (none downloaded; all need a browser fetch)

The target folder `build/ext/unpacked/quad/` exists but is empty.
Suggested file names after fetching follow `<brand>-<model>-<n>.<ext>`: aixam-easy-1.jpg, aixam-d-truck-1.png, aixam-d-truck-2.png, and so on.
"side?" and "front?" below mean the angle is inferred from the file name, gallery title or alt text and has not been seen; "?" means unknown. Widths marked "(from file name)" come from size suffixes in the URL and were not measured.

| Tile | Suggested file | URL | Page | View | Width (px) | Status |
|---|---|---|---|---|---|---|
| Aixam Easy | `aixam-easy-1.jpg` | <https://aixam.de/wp-content/uploads/EASICE_PROF_JAD_PNG.jpg> | <https://aixam.de/fahrzeuge/aixam/chic-diesel/> | side? | ? | needs browser fetch |
| Aixam Easy | `aixam-easy-2.webp` | <https://www.aixam.com/ressources/medias/slide_aixam-easy-access-69dcac65d667c.webp> | <https://www.aixam.com/fr/easy/access> | ? | ? | needs browser fetch |
| Aixam City | `aixam-city-1.webp` | <https://www.aixam.com/ressources/medias/slide_aixam-city-pack-6a19629c12c99.webp> | <https://www.aixam.com/fr/voiture-sans-permis-city/pack> | ? | ? | needs browser fetch |
| Aixam City | `aixam-city-2.webp` | <https://www.aixam.com/ressources/medias/slide_aixam-city-sport-6a1962be1b928.webp> | <https://www.aixam.com/en/licence-free-car-city/sport> | ? | ? | needs browser fetch |
| Aixam City | `aixam-city-3.jpg` | <https://www.steck-automobile.ch/images/aixam/aixam-city-pack/aixam-city-pack-quer.jpg> | <https://www.steck-automobile.ch/de/aixam> | ? | ? | needs browser fetch |
| Aixam Coupé | `aixam-coupe-1.webp` | <https://www.aixam.com/ressources/medias/voiture-sans-permis-essentiel_aixam-coup-sport-6a1963444a185.webp?v2> | <https://www.aixam.com/fr/voiture-sans-permis-coupe/sport> | ? | ? | needs browser fetch |
| Aixam Coupé | `aixam-coupe-2.jpg` | <https://aixam.de/wp-content/uploads/slide_aixam-coup-sport-670c47978f694.jpg> | <https://aixam.de/fahrzeuge/aixam/coupe-sport/> | ? | ? | needs browser fetch |
| Aixam Coupé | `aixam-coupe-3.jpg` | <https://www.steck-automobile.ch/images/aixam/aixam-coupe-sport/aixam-coupe-sport-home-quer.jpg> | <https://www.steck-automobile.ch/de/aixam> | ? | ? | needs browser fetch |
| Aixam Crossover | `aixam-crossover-1.webp` | <https://www.aixam.com/ressources/medias/voiture-sans-permis-essentiel_aixam-crossover-pack-6a196367d8b10.webp?v2> | <https://www.aixam.com/fr/voiture-sans-permis-crossover/pack> | ? | ? | needs browser fetch |
| Aixam Crossover | `aixam-crossover-2.jpg` | <https://aixam.de/wp-content/uploads/slide_aixam-crossover-premium-670c47a72810a.jpg> | <https://aixam.de/fahrzeuge/aixam/crossover-premium/> | ? | ? | needs browser fetch |
| Aixam Crossover | `aixam-crossover-3.jpg` | <https://www.steck-automobile.ch/images/aixam/aixam-crossover-premium/aixam-crossover-premium-quer.jpg> | <https://www.steck-automobile.ch/de/aixam> | ? | ? | needs browser fetch |
| Aixam e-Scouty | `aixam-e-scouty-1.webp` | <https://www.aixam.com/ressources/medias/voiture-sans-permis-essentiel_mega-e-scouty-evo-69cfda952dc06.webp?v2> | <https://www.aixam.com/fr/e-scouty/evo> | ? | ? | needs browser fetch |
| Aixam D-Truck / e-Truck | `aixam-d-truck-1.png` | <https://www.aixam-pro.com/ressources/medias/slide_propla_prof_serie.png?v2> | <https://www.aixam-pro.com/fr/d-truck/plateau-ridelles> | side? | ? | needs browser fetch |
| Aixam D-Truck / e-Truck | `aixam-d-truck-2.png` | <https://www.aixam-pro.com/ressources/medias/slide_profou_prof_serie.png?v2> | <https://www.aixam-pro.com/fr/d-truck/fourgon> | side? | ? | needs browser fetch |
| Ligier JS50 | `ligier-js50-1.webp` | <https://s3.ligier.fr/ligier-prod/uploads/2026/10/Microcar-Ligier-bleute-en-studio-2.webp> | <https://www.ligier.fr/voitures-permis-b1/> | ? | ? | needs browser fetch |
| Ligier JS50 | `ligier-js50-2.webp` | <https://s3.ligier.fr/ligier-prod/uploads/2026/04/REEF.webp> | <https://www.ligier.fr/vehicules/js50/> | ? | ? | needs browser fetch |
| Ligier JS60 | `ligier-js60-1.webp` | <https://s3.ligier.fr/ligier-prod/uploads/2026/10/Microcar-Ligier-en-studio-gris-clair-2.webp> | <https://www.ligier.fr/voitures-permis-b1/> | ? | ? | needs browser fetch |
| Ligier JS60 | `ligier-js60-2.webp` | <https://s3.ligier.fr/ligier-prod/uploads/2026/09/js60-view.webp> | <https://www.ligier.fr/vehicules/js60/> | ? | ? | needs browser fetch |
| Ligier JS60 | `ligier-js60-3.jpg` | <https://media.ligier.fr/app/uploads/2026/09/NOUVELLE-JS60-ULTIMATE-23-scaled.jpg> | <https://media.ligier.fr/mediatheque/nouvelle-js60/> | ? | 2560 (from file name) | needs browser fetch |
| Ligier Myli | `ligier-myli-1.webp` | <https://s3.ligier.fr/ligier-prod/uploads/2026/10/Microcar-rouge-Ligier-en-studio-2.webp> | <https://www.ligier.fr/voitures-permis-b1/> | ? | ? | needs browser fetch |
| Ligier Myli | `ligier-myli-2.webp` | <https://s3.ligier.fr/ligier-prod/uploads/2026/05/LIGIER-MYLI-MAX-2026-Blanc.webp> | <https://www.ligier.fr/vehicules/myli-max/> | ? | ? | needs browser fetch |
| Ligier Myli | `ligier-myli-3.png` | <https://media.ligier.fr/app/uploads/2026/01/MYLI-LAB-ET-MAX-1024x325.png> | <https://media.ligier.fr/communique-de-presse/ligier-fait-evoluer-myli-encore-plus-accessible-plus-expressive-et-plus-polyvalente-que-jamais/> | ? | 1024 (from file name) | needs browser fetch |
| Ligier Pulse 4 | `ligier-pulse-4-1.png` | <https://media.ligier.fr/app/uploads/2024/05/Pulse-4-long-caisson-HD.png> | <https://media.ligier.fr/mediatheque/ligier-professional-pulse-4/> | ? | ? | needs browser fetch |
| Ligier Pulse 4 | `ligier-pulse-4-2.png` | <https://media.ligier.fr/app/uploads/2024/05/Pulse-4-long-plateau-basculant-HD.png> | <https://media.ligier.fr/mediatheque/ligier-professional-pulse-4/> | ? | ? | needs browser fetch |
| Ligier Pulse 4 | `ligier-pulse-4-3.jpg` | <https://www.ligier-professional.fr/wp-content/uploads/sites/118/2023/02/pulse-4-header-1920x793.jpg> | <https://www.ligier-professional.fr/product/pulse-4/> | ? | 1920 (from file name) | needs browser fetch |
| Chatenet CH46 | `chatenet-ch46-1.jpg` | <https://www.automobiles-chatenet.com/files/pack/contenu/Images/Gamme/BASE/VISUEL-V-BLANCHE.jpg> | <https://www.automobiles-chatenet.com/ch46e-sl-electrique.html> | ? | ? | needs browser fetch |
| Chatenet CH46 | `chatenet-ch46-2.jpg` | <https://www.automobiles-chatenet.com/files/pack/contenu/Images/Gamme/CH46%20K%20Series/VISUEL-V-GRISE%281%29.jpg> | <https://www.automobiles-chatenet.com/ch46-k-series.html> | ? | ? | needs browser fetch |
| Chatenet CH46 | `chatenet-ch46-3.jpg` | <https://www.automobiles-chatenet.com/files/pack/contenu/Images/Slider/Chatenet-GAMME%20site%201600x650px.jpg> | <https://www.automobiles-chatenet.com/> | ? | 1600 (from file name) | needs browser fetch |
| Casalini 650 | `casalini-650-1.png` | <https://casalini.eu/wp-content/uploads/2026/09/SPORTIVA-GT-Bianco4.png> | <https://www.casalini.eu/> | ? | ? | needs browser fetch |
| Casalini 650 | `casalini-650-2.png` | <https://casalini.eu/wp-content/uploads/2026/09/XTREME-Black3.png> | <https://www.casalini.eu/> | ? | ? | needs browser fetch |
| Casalini 650 | `casalini-650-3.jpg` | <https://casalini.eu/wp-content/uploads/2026/09/CASALINI-starter-front.jpg> | <https://www.casalini.eu/> | front? | ? | needs browser fetch |

31 picture URLs in total; none downloaded.
