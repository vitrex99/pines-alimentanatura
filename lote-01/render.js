const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const pins=JSON.parse(fs.readFileSync('pins.json','utf8'));
const f=n=>'data:font/woff2;base64,'+fs.readFileSync(path.join('node_modules/@fontsource',n)).toString('base64');
const css=`
@font-face{font-family:Brico;font-weight:700;src:url(${f('bricolage-grotesque/files/bricolage-grotesque-latin-700-normal.woff2')})}
@font-face{font-family:Brico;font-weight:800;src:url(${f('bricolage-grotesque/files/bricolage-grotesque-latin-800-normal.woff2')})}
@font-face{font-family:Fig;font-weight:400;src:url(${f('figtree/files/figtree-latin-400-normal.woff2')})}
@font-face{font-family:Fig;font-weight:600;src:url(${f('figtree/files/figtree-latin-600-normal.woff2')})}
@font-face{font-family:Fig;font-weight:700;src:url(${f('figtree/files/figtree-latin-700-normal.woff2')})}
:root{--pine:#16382F;--leaf:#A7D16F;--squash:#F3A93C;--paper:#FAF8F2;--ink:#14231E;--mint:#DDEFC6}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1000px;height:1500px;font-family:Fig,sans-serif;color:var(--ink);overflow:hidden}
.pin{width:1000px;height:1500px;padding:90px 84px 70px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.kicker{font:700 30px Fig;letter-spacing:.14em;text-transform:uppercase;display:inline-block;padding:14px 26px;border-radius:999px;align-self:flex-start}
h1{font-family:Brico;font-weight:800;line-height:.98;letter-spacing:-.02em;margin-top:44px;text-wrap:balance}
.foot{margin-top:auto;padding-top:40px;display:flex;flex-direction:column;gap:14px}
.brand{display:flex;justify-content:space-between;align-items:center;font:700 34px Fig}
.brand b{font-family:Brico;font-weight:800;font-size:40px;letter-spacing:-.01em}
.disc{font:400 21px Fig;opacity:.75}
.src{font:600 24px Fig;opacity:.85}
.blob{position:absolute;border-radius:50%;z-index:0}
.pin>*{position:relative;z-index:1}
.pin>.blob{position:absolute;z-index:0}
/* lista */
.lista{background:var(--paper)} .lista .kicker{background:var(--pine);color:var(--paper)}
.lista h1{font-size:92px;color:var(--pine)}
.unit{font:700 26px Fig;letter-spacing:.1em;text-transform:uppercase;color:var(--pine);opacity:.7;margin-top:46px;display:flex;justify-content:space-between;border-bottom:4px solid var(--pine);padding-bottom:14px}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:30px;padding:22px 0;border-bottom:2px dashed #16382F55;font:600 40px Fig}
.row span:last-child{font:800 40px Brico;color:var(--pine);text-align:right;white-space:nowrap}
.row.long span:last-child{white-space:normal;font-size:34px;max-width:52%}
.lista .blob{width:420px;height:420px;background:var(--leaf);right:-160px;top:-160px}
/* pregunta */
.pregunta{background:var(--squash)} .pregunta .kicker{background:var(--ink);color:var(--squash)}
.pregunta h1{font-size:132px;color:var(--ink);margin-top:60px}
.ans{margin-top:60px;background:var(--paper);border-radius:36px;padding:44px 48px;display:flex;flex-direction:column;gap:26px}
.ans div{font:600 42px/1.2 Fig;display:flex;gap:22px}
.ans div:before{content:"";flex:0 0 22px;height:22px;border-radius:50%;background:var(--pine);margin-top:13px}
.ans div:first-child{font-weight:700}
.pregunta .blob{width:600px;height:600px;background:#F7BE63;left:-220px;bottom:-200px}
/* receta */
.receta{background:var(--pine);color:var(--paper)} .receta .kicker{background:var(--leaf);color:var(--pine)}
.receta h1{font-size:112px;color:var(--paper)}
.chips{display:flex;flex-wrap:wrap;gap:14px;margin-top:40px}
.chips span{font:700 30px Fig;border:3px solid var(--leaf);color:var(--leaf);padding:10px 24px;border-radius:999px}
.ing{margin-top:50px;font:700 26px Fig;letter-spacing:.12em;text-transform:uppercase;color:var(--leaf)}
.ing ul{list-style:none;margin-top:18px;display:flex;flex-direction:column;gap:14px}
.ing li{font:600 40px Fig;letter-spacing:0;text-transform:none;color:var(--paper);padding-left:42px;position:relative}
.ing li:before{content:"";position:absolute;left:0;top:18px;width:20px;height:20px;border-radius:6px;background:var(--squash)}
.tip{margin-top:40px;background:var(--mint);color:var(--pine);border-radius:28px;padding:30px 36px;font:600 34px/1.25 Fig}
.receta .blob{width:520px;height:520px;background:#1F4A3E;right:-180px;bottom:120px}
/* curiosidad */
.curiosidad{background:var(--leaf)} .curiosidad .kicker{background:var(--pine);color:var(--leaf)}
.curiosidad h1{font-size:110px;color:var(--pine)}
.body{font:600 38px Fig;margin-top:44px;color:var(--pine)}
.xl{list-style:none;margin-top:30px;display:flex;flex-direction:column;gap:20px}
.xl li{background:var(--paper);border-radius:24px;padding:26px 32px;font:600 38px/1.2 Fig;display:flex;gap:24px;align-items:center}
.xl li i{font:800 40px Brico;font-style:normal;color:var(--paper);background:var(--pine);width:58px;height:58px;border-radius:50%;display:grid;place-items:center;flex:0 0 58px}
/* versus */
.versus{background:var(--paper)} .versus .kicker{background:var(--squash);color:var(--ink)}
.versus h1{font-size:100px;color:var(--pine)}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:60px}
.card{border-radius:34px;padding:40px 34px;display:flex;flex-direction:column;gap:10px}
.card .n{font:800 46px Brico}.card .d{font:600 30px Fig;opacity:.8}.card .g{font:800 96px Brico;margin-top:30px;line-height:1}.card .e{font:600 30px Fig}
.c1{background:var(--mint);color:var(--pine)}.c2{background:#F6D7A4;color:#5A3A0E}
.note{margin-top:40px;font:600 38px Fig;color:var(--pine)}
.versus .blob{width:380px;height:380px;background:#F7E3B8;left:-140px;top:-120px}
`;
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
function foot(p,dark){return `<div class="foot">${p.source?`<div class="src">${esc(p.source)}</div>`:''}<div class="brand"><b>AlimentaNatura</b><span>alimentanatura.com</span></div><div class="disc">Información divulgativa. No sustituye la consulta con un profesional sanitario.</div></div>`}
function body(p){
 const k=`<span class="kicker">${esc(p.kicker)}</span><h1>${esc(p.title)}</h1>`;
 if(p.tpl==='lista')return `<div class="blob"></div>${k}<div class="unit"><span>${esc(p.unit)}</span></div>${p.rows.map(r=>`<div class="row ${r[1].length>14?'long':''}"><span>${esc(r[0])}</span><span>${esc(r[1])}</span></div>`).join('')}`;
 if(p.tpl==='pregunta')return `<div class="blob"></div>${k}<div class="ans">${p.answer.map(a=>`<div>${esc(a)}</div>`).join('')}</div>`;
 if(p.tpl==='receta')return `<div class="blob"></div>${k}<div class="chips">${p.chips.map(c=>`<span>${esc(c)}</span>`).join('')}</div><div class="ing">Ingredientes clave<ul>${p.ing.map(i=>`<li>${esc(i)}</li>`).join('')}</ul></div>${p.tip?`<div class="tip">${esc(p.tip)}</div>`:''}`;
 if(p.tpl==='curiosidad')return `${k}${p.body?`<div class="body">${esc(p.body)}</div>`:''}<ul class="xl">${p.list.map((l,i)=>`<li><i>${i+1}</i><span>${esc(l)}</span></li>`).join('')}</ul>`;
 if(p.tpl==='versus')return `<div class="blob"></div>${k}<div class="vs">${[['c1',p.a],['c2',p.b]].map(([c,a])=>`<div class="card ${c}"><div class="n">${esc(a[0])}</div><div class="d">${esc(a[1])}</div><div class="g">${esc(a[2])}</div><div class="e">${esc(a[3])}</div></div>`).join('')}</div><div class="note">${esc(p.note)}</div>`;
}
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1000,height:1500}});
for(const p of pins){await pg.setContent(`<html><head><style>${css}</style></head><body><div class="pin ${p.tpl}">${body(p)}${foot(p)}</div></body></html>`);
await pg.evaluate(()=>document.fonts.ready);
const over=await pg.evaluate(()=>{const f=document.querySelector('.foot').getBoundingClientRect();const kids=[...document.querySelector('.pin').children].filter(e=>!e.classList.contains('foot')&&!e.classList.contains('blob'));return Math.max(...kids.map(e=>e.getBoundingClientRect().bottom))-f.top});
console.log(p.id,p.tpl,'overlap',Math.round(over));
await pg.screenshot({path:`out/pin-${p.id}.png`});}
await b.close();})();
