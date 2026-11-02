const {chromium}=require('playwright');const fs=require('fs');
const [,,inp,out,W]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:3179,height:3000}});
await p.goto('file://'+require('path').resolve(inp));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
await p.addStyleTag({content:`.card{flex:none!important}.tile{flex:none!important;width:${W}mm!important}.same{flex:none!important}.line{width:auto!important}.cards{overflow:visible}`});
const r=await p.evaluate(()=>{const o={};const mm=96/25.4;document.querySelectorAll('.card').forEach(c=>o[c.dataset.id]=c.getBoundingClientRect().width/mm);return o});
fs.writeFileSync(out,JSON.stringify(r));console.log(Object.keys(r).length, Math.max(...Object.values(r)));await b.close();})();
