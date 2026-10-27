const { chromium } = require('playwright');
const CHECK = `(() => {
  const D = JSON.parse(document.getElementById('data').textContent);
  const tiles = [...document.querySelectorAll('.tile')].filter(t => !t.classList.contains('hide'));
  const byId = new Map(tiles.map(t => [t.dataset.id, t]));
  const bad = []; let ok = 0, groups = 0;
  for (const [gid, g] of Object.entries(D.groups)) {
    const mem = g.members.filter(i => byId.has(i)); if (mem.length < 2) continue; groups++;
    const minS = Math.min(...mem.map(i => +byId.get(i).dataset.s));
    const firstTops = mem.filter(i => +byId.get(i).dataset.s === minS).map(i => Math.round(byId.get(i).getBoundingClientRect().top));
    const rows = new Set(mem.map(i => byId.get(i).dataset.row));
    if (new Set(firstTops).size !== 1 || rows.size !== 1) bad.push({gid, firstTops, rows: [...rows]}); else ok++;
  }
  // tiles must stay inside their column: compare with the brand header column box
  const colBox = new Map([...document.querySelectorAll('.bhdr')].map(h => [h.dataset.brand, h.getBoundingClientRect()]));
  const overflow = tiles.filter(t => { const r = t.getBoundingClientRect(); const c = colBox.get(t.dataset.brand); return c && (r.left < c.left - 1 || r.right > c.right + 1); }).map(t => t.dataset.id).slice(0, 5);
  // same sub-row => same top for all tiles in that (row, s)
  const tops = new Map(); const mism = [];
  for (const t of tiles) { const k = t.dataset.row + '/' + t.dataset.s; const top = Math.round(t.getBoundingClientRect().top); if (tops.has(k) && tops.get(k) !== top) mism.push(k); else tops.set(k, top); }
  const m = document.getElementById('matrix').getBoundingClientRect();
  return { groups, ok, bad, ntiles: tiles.length, overflow, subrowTopMismatch: [...new Set(mism)].slice(0, 8), matrix: { w: Math.round(m.width), h: Math.round(m.height) }, stripes: document.querySelectorAll('.stripe:not(.hide)').length };
})()`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  p.on('pageerror', e => console.log('PAGEERROR', e.message)); p.on('console', m => { if (m.type() === 'error') console.log('CONSOLE', m.text()); });
  await p.goto('file://' + process.argv[2]); await p.waitForTimeout(600);
  console.log('default:', JSON.stringify(await p.evaluate(CHECK)));
  await p.screenshot({ path: process.argv[3] + '/align_top.png' });
  await p.evaluate(() => { const wrap = document.getElementById('mwrap'); wrap.scrollIntoView(); const h = document.querySelector('.rhdr[data-row="c-suv"]'); wrap.scrollTop = h.offsetTop - 64; });
  await p.waitForTimeout(300); await p.screenshot({ path: process.argv[3] + '/align_csuv.png' });
  await p.evaluate(() => { document.getElementById('mwrap').scrollLeft = 170 + 156 * 9; }); await p.waitForTimeout(300);
  await p.screenshot({ path: process.argv[3] + '/align_csuv_stellantis.png' });
  await p.click('#only-twins'); await p.waitForTimeout(400);
  console.log('only-twins:', JSON.stringify(await p.evaluate(CHECK)));
  await p.evaluate(() => { const wrap = document.getElementById('mwrap'); wrap.scrollTop = 0; wrap.scrollLeft = 0; }); await p.waitForTimeout(300);
  await p.screenshot({ path: process.argv[3] + '/align_twins.png' });
  await p.click('#only-twins'); await p.evaluate(() => document.getElementById('size-compact').click()); await p.waitForTimeout(400);
  console.log('compact:', JSON.stringify(await p.evaluate(CHECK)));
  await p.screenshot({ path: process.argv[3] + '/align_compact.png' });
  // hide a group and a row, check again
  await p.evaluate(() => { document.getElementById('size-normal').click(); document.getElementById('g-0').click(); document.getElementById('r-c-suv').click(); }); await p.waitForTimeout(400);
  console.log('filtered:', JSON.stringify(await p.evaluate(CHECK)));
  await p.screenshot({ path: process.argv[3] + '/align_filtered.png' });
  await b.close();
})();
