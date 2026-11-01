# Identical Car Chart v1.12 — self-contained copy (2026-11-01)

Open `index.html` in a browser (serve the folder over http for the front views, e.g. `python3 -m http.server`;
the side views work from a plain file:// open as well).

- `index.html` — the chart (also published at https://claude.ai/artifact/SQLziPkb5ir5kasuaUEHrc, Version 21; superseded by chart-v1.13)
- `img/`, `img_manifest.json` — pictures (unchanged since v1.11)
- `build/` — generator (`gen.py`), merge pipeline, overrides, picture tooling, measurement check, drive data, `check_align.js`
  (now also checks the family bars), and `research/` with the model research files and `research/countries/`
  (`brand_countries.json` = the country data behind the flags, `brand_countries.md` = the ambiguous cases).

v1.12 (2026-11-01): two requests from Raven.
- Arrangement: "groups stay on the same height and are not interrupted by other groups". Within a class row every family
  now has a line of its own: its members sit on that line, a bar in the family colour joins them (dashed when the family
  consists of platform siblings only), and no other vehicle is placed between the first and the last member on that line.
  Families whose brands lie in different parts of the chart share a line. A brand with two members of one family stacks
  them on adjacent lines with a short stub; the stack is pushed to the top of the column. The order in which families claim
  lines is searched (fixed seed) for the fewest lines, then the fewest columns with an empty top cell, then the fullest top
  lines. Result: 68 lines instead of 58 (the matrix is about 17 % taller); singletons that fell under a family's bar moved
  to a lower line, which leaves empty top cells in the van, MPV and SUV rows where wide families cover many columns.
  Hovering a tile lights its family's bar as well. `check_align.js` verifies in all four layout modes that every visible bar
  spans exactly its members and that nothing else sits between them (78 bars, all clean).
- Brand countries: a flag in every brand header and in every ownership-group header, drawn as inline SVG (no emoji, so
  it renders the same on every system). Rule: the flag is the country of the head office that Wikipedia gives for the
  company running the brand; a smaller second flag marks the one foreign country where (nearly) all of the brand's models
  for Europe are built (MAN → Poland, Mobilize → Morocco, DR → China, Isuzu → Thailand, Ineos → France, Microlino → Italy).
  Hovering a flag shows the office, the legal entity, the plants and a note; the detail panel repeats this with a source
  link. The sources block lists the Wikipedia pages (96 brands, 50 groups, checked 2026-11-01).
  Calls worth a look: MG, smart and Lynk & Co come out as China (Shanghai / Ningbo / Hangzhou head offices, cars built in
  China; the marque origin — British, German — is named in the tooltip); Polestar stays Sweden with no second flag (2, 4
  and 5 from China, 3 from the US); Tesla stays US (Model Y from Grünheide, Model 3 from Shanghai); MINI is Britain
  (Oxford); Ebro and Piaggio assemble Chinese kits at home and keep their flags; Stellantis as a group is the Netherlands
  (Hoofddorp). Eight entries are "medium" confidence (MG, MINI, Mobilize, Maxus, Lepas, Isuzu, Iveco, Cadillac) because
  Wikipedia gives no head office or does not say which plant supplies Europe; `build/research/countries/brand_countries.md`
  explains each.
Earlier versions: `../chart-v1.11/` (new-body pictures, quadricycles, scale option), `../chart-v1.10/`, `../chart-v1.9/`,
`../chart-v1.8/`, `../chart-v1.7/`, `../chart-v1.5/`.
