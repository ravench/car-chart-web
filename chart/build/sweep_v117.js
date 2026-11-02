const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + process.argv[2], { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForTimeout(1500);
  const res = await p.evaluate(() => {
    const rI = [...document.querySelectorAll('input[data-row]')], pI = [...document.querySelectorAll('input[data-pt]')];
    const gI = [...document.querySelectorAll('input[data-group]')], dI = [...document.querySelectorAll('input[data-drive]')];
    const tw = document.getElementById('only-twins'), t2 = document.getElementById('show-t2');
    const tiles = [...document.querySelectorAll('.tile')];
    const fire = el => el.dispatchEvent(new Event('change', { bubbles: true }));
    const check = () => {
      const bh = [...document.querySelectorAll('.bhdr:not(.hide)')], rh = [...document.querySelectorAll('.rhdr:not(.hide)')];
      const vis = tiles.filter(t => !t.classList.contains('hide'));
      const brandsWithTile = new Set(vis.map(t => t.dataset.brand)), rowsWithTile = new Set(vis.map(t => t.dataset.row));
      const emptyCols = bh.filter(h => !brandsWithTile.has(h.dataset.brand)).map(h => h.dataset.brand);
      const emptyRows = rh.filter(h => !rowsWithTile.has(h.dataset.row)).map(h => h.dataset.row);
      const visBrandSet = new Set(bh.map(h => h.dataset.brand)), visRowSet = new Set(rh.map(h => h.dataset.row));
      const orphan = vis.filter(t => !visBrandSet.has(t.dataset.brand) || !visRowSet.has(t.dataset.row)).map(t => t.dataset.id);
      const ghdr = [...document.querySelectorAll('.ghdr:not(.hide)')].map(h => h.dataset.group);
      const emptyGroups = ghdr.filter(g => !bh.some(h => h.dataset.group === g));
      const ncol = getComputedStyle(document.getElementById('matrix')).gridTemplateColumns.split(' ').length - 1;
      return { emptyCols, emptyRows, orphan, emptyGroups, ncolMismatch: ncol !== bh.length, vis: vis.length };
    };
    const bad = []; let n = 0;
    const setPt = mask => pI.forEach((i, k) => { i.checked = !!(mask & (1 << k)); });
    const setRows = set => rI.forEach(i => { i.checked = set.has(i.dataset.row); });
    const allRows = new Set(rI.map(i => i.dataset.row));
    const rowSets = [allRows, ...rI.map(i => new Set([i.dataset.row]))];
    for (let k = 0; k + 2 < rI.length; k++) rowSets.push(new Set([rI[k].dataset.row, rI[k + 1].dataset.row, rI[k + 2].dataset.row]));
    rowSets.push(new Set(rI.slice(0, 6).map(i => i.dataset.row)), new Set(rI.slice(12).map(i => i.dataset.row)));
    const record = (label) => { const c = check(); n++; if (c.emptyCols.length || c.emptyRows.length || c.orphan.length || c.emptyGroups.length || c.ncolMismatch) bad.push([label, c]); };
    // powertrain subsets x row sets
    for (let mask = 0; mask < (1 << pI.length); mask++) { setPt(mask); for (const rs of rowSets) { setRows(rs); fire(rI[0]); record('pt' + mask + '/rows' + [...rs].join(',')); } }
    setPt((1 << pI.length) - 1);
    // drive subsets x row sets, twins toggles
    for (let mask = 0; mask < (1 << dI.length); mask++) { dI.forEach((i, k) => { i.checked = !!(mask & (1 << k)); }); for (const rs of rowSets) { setRows(rs); fire(rI[0]); record('dv' + mask + '/rows' + [...rs].join(',')); } }
    dI.forEach(i => { i.checked = true; });
    for (const twv of [true, false]) for (const t2v of [true, false]) { tw.checked = twv; t2.checked = t2v; for (const rs of rowSets) { setRows(rs); fire(rI[0]); record('tw' + twv + 't2' + t2v + '/rows' + [...rs].join(',')); } }
    tw.checked = false; t2.checked = true;
    // single groups x hybrid pts x row sets
    setPt(pI.reduce((m, i, k) => ['phev', 'hev', 'mhev'].includes(i.dataset.pt) ? m | (1 << k) : m, 0));
    for (const g of gI) { gI.forEach(i => { i.checked = i === g; }); for (const rs of rowSets) { setRows(rs); fire(rI[0]); record('g' + g.dataset.group + '/rows' + [...rs].join(',')); } }
    gI.forEach(i => { i.checked = true; }); setPt((1 << pI.length) - 1); setRows(allRows); fire(rI[0]);
    return { n, bad: bad.slice(0, 20), nbad: bad.length };
  });
  console.log(JSON.stringify(res));
  console.log('pageerrors', errs);
  await b.close();
})();
