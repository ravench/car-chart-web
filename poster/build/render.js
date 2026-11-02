const {chromium}=require('playwright');
const [,,inp,out,png,land]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:Math.round((841+2*(+(process.env.BLEED||0)))*96/25.4),height:Math.round((1189+2*(+(process.env.BLEED||0)))*96/25.4)}});
await p.goto('file://'+require('path').resolve(inp));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);
const m=await p.evaluate(()=>({sh:document.body.scrollHeight,ih:innerHeight,sw:document.documentElement.scrollWidth,main:document.querySelector('main').scrollHeight,mainc:document.querySelector('main').clientHeight,fonts:[...document.fonts].filter(f=>f.status=='loaded').length}));
console.log(JSON.stringify(m));
if(png) await p.screenshot({path:png,fullPage:true});
const bl=+(process.env.BLEED||0);await p.pdf({path:out,width:(841+2*bl)+'mm',height:(1189+2*bl)+'mm',printBackground:true});
await b.close();})();
