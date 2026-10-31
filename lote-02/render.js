const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const pins=JSON.parse(fs.readFileSync(process.argv[3],'utf8'));const OUT=process.argv[4];
const FOTOS=process.argv[2];const PH={lista:400,pregunta:560,receta:560,curiosidad:540,versus:520,foto:900};
const img=p=>{const b=fs.readFileSync(path.join(FOTOS,p.foto_file));const m=p.foto_file.endsWith('.png')?'png':'jpeg';return `data:image/${m};base64,`+b.toString('base64')};
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
.pin{width:1000px;height:1500px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.photo{flex:0 0 var(--ph);background-size:cover;background-position:center;position:relative;z-index:2}
.photo .kicker{position:absolute;left:84px;bottom:-26px;box-shadow:0 6px 20px #0003}
.content{flex:1;display:flex;flex-direction:column;padding:56px 84px 56px;position:relative;overflow:hidden}
.content>*{position:relative;z-index:1}.content>.blob{position:absolute;z-index:0}
.kicker{font:700 28px Fig;letter-spacing:.14em;text-transform:uppercase;display:inline-block;padding:14px 26px;border-radius:999px}
h1{margin-top:14px}
h1{font-family:Brico;font-weight:800;line-height:.98;letter-spacing:-.02em;text-wrap:balance}
.foot{margin-top:auto;padding-top:28px;display:flex;flex-direction:column;gap:14px}
.brand{display:flex;justify-content:space-between;align-items:center;font:700 30px Fig}
.brand b{font-family:Brico;font-weight:800;font-size:38px;letter-spacing:-.01em}
.disc{font:400 21px Fig;opacity:.75}
.src{font:600 24px Fig;opacity:.85}
.blob{position:absolute;border-radius:50%;z-index:0}
.pin>*{position:relative;z-index:1}
.pin>.blob{position:absolute;z-index:0}
/* lista */
.lista{background:var(--paper)} .lista .kicker{background:var(--pine);color:var(--paper)}
.lista h1{font-size:72px;color:var(--pine)}
.unit{font:700 26px Fig;letter-spacing:.1em;text-transform:uppercase;color:var(--pine);opacity:.7;margin-top:28px;display:flex;justify-content:space-between;border-bottom:4px solid var(--pine);padding-bottom:14px}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:30px;padding:16px 0;border-bottom:2px dashed #16382F55;font:600 36px Fig}
.row span:last-child{font:800 36px Brico;color:var(--pine);text-align:right;white-space:nowrap}
.row.long span:last-child{white-space:normal;font-size:34px;max-width:52%}
.lista .blob{width:420px;height:420px;background:var(--leaf);right:-160px;top:-160px}
/* pregunta */
.pregunta{background:var(--squash)} .pregunta .kicker{background:var(--ink);color:var(--squash)}
.pregunta h1{font-size:96px;color:var(--ink)}
.ans{margin-top:36px;background:var(--paper);border-radius:36px;padding:44px 48px;display:flex;flex-direction:column;gap:26px}
.ans div{font:600 38px/1.2 Fig;display:flex;gap:22px}
.ans div:before{content:"";flex:0 0 22px;height:22px;border-radius:50%;background:var(--pine);margin-top:13px}
.ans div:first-child{font-weight:700}
.pregunta .blob{width:600px;height:600px;background:#F7BE63;left:-220px;bottom:-200px}
/* receta */
.receta{background:var(--pine);color:var(--paper)} .receta .kicker{background:var(--leaf);color:var(--pine)}
.receta h1{font-size:84px;color:var(--paper)}
.chips{display:flex;flex-wrap:wrap;gap:14px;margin-top:28px}
.chips span{font:700 30px Fig;border:3px solid var(--leaf);color:var(--leaf);padding:10px 24px;border-radius:999px}
.ing{margin-top:30px;font:700 26px Fig;letter-spacing:.12em;text-transform:uppercase;color:var(--leaf)}
.ing ul{list-style:none;margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:12px 24px}
.ing li{font:600 32px Fig;letter-spacing:0;text-transform:none;color:var(--paper);padding-left:42px;position:relative}
.ing li:before{content:"";position:absolute;left:0;top:18px;width:20px;height:20px;border-radius:6px;background:var(--squash)}
.tip{margin-top:28px;background:var(--mint);color:var(--pine);border-radius:28px;padding:22px 30px;font:600 30px/1.25 Fig}
.receta .blob{width:520px;height:520px;background:#1F4A3E;right:-180px;bottom:120px}
/* curiosidad */
.curiosidad{background:var(--leaf)} .curiosidad .kicker{background:var(--pine);color:var(--leaf)}
.curiosidad h1{font-size:76px;color:var(--pine)}
.body{font:600 34px Fig;margin-top:26px;color:var(--pine)}
.xl{list-style:none;margin-top:24px;display:flex;flex-direction:column;gap:14px}
.xl li{background:var(--paper);border-radius:24px;padding:18px 28px;font:600 34px/1.2 Fig;display:flex;gap:24px;align-items:center}
.xl li i{font:800 40px Brico;font-style:normal;color:var(--paper);background:var(--pine);width:58px;height:58px;border-radius:50%;display:grid;place-items:center;flex:0 0 58px}
/* versus */
.versus{background:var(--paper)} .versus .kicker{background:var(--squash);color:var(--ink)}
.versus h1{font-size:72px;color:var(--pine)}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:34px}
.card{border-radius:34px;padding:30px 30px;display:flex;flex-direction:column;gap:10px}
.card .n{font:800 46px Brico}.card .d{font:600 30px Fig;opacity:.8}.card .g{font:800 68px Brico;white-space:nowrap;margin-top:14px;line-height:1}.card .e{font:600 30px Fig}
.c1{background:var(--mint);color:var(--pine)}.c2{background:#F6D7A4;color:#5A3A0E}
.note{margin-top:26px;font:600 34px Fig;color:var(--pine)}
.versus .blob{width:380px;height:380px;background:#F7E3B8;left:-140px;top:-120px}
/* foto */
.foto{background:var(--pine);color:var(--paper)} .foto .kicker{background:var(--squash);color:var(--ink)}
.foto h1{font-size:92px;color:var(--paper);margin-top:30px}
.foto .sub{font:600 40px/1.2 Fig;color:var(--leaf);margin-top:22px}
`;
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
function foot(p,dark){return `<div class="foot">${p.source?`<div class="src">${esc(p.source)}</div>`:''}<div class="brand"><b>AlimentaNatura</b><span>alimentanatura.com</span></div><div class="disc">Información divulgativa. No sustituye la consulta con un profesional sanitario.</div></div>`}
function body(p){
 const k=`<h1>${esc(p.title)}</h1>`;
 if(p.tpl==='foto')return `${k}<div class="sub">${esc(p.sub)}</div>`;
 if(p.tpl==='lista')return `${k}<div class="unit"><span>${esc(p.unit)}</span></div>${p.rows.map(r=>`<div class="row ${r[1].length>14?'long':''}"><span>${esc(r[0])}</span><span>${esc(r[1])}</span></div>`).join('')}`;
 if(p.tpl==='pregunta')return `${k}<div class="ans">${p.answer.map(a=>`<div>${esc(a)}</div>`).join('')}</div>`;
 if(p.tpl==='receta')return `${k}<div class="chips">${p.chips.map(c=>`<span>${esc(c)}</span>`).join('')}</div><div class="ing">Ingredientes clave<ul>${p.ing.map(i=>`<li>${esc(i)}</li>`).join('')}</ul></div>${p.tip?`<div class="tip">${esc(p.tip)}</div>`:''}`;
 if(p.tpl==='curiosidad')return `${k}${p.body?`<div class="body">${esc(p.body)}</div>`:''}<ul class="xl">${p.list.map((l,i)=>`<li><i>${i+1}</i><span>${esc(l)}</span></li>`).join('')}</ul>`;
 if(p.tpl==='versus')return `${k}<div class="vs">${[['c1',p.a],['c2',p.b]].map(([c,a])=>`<div class="card ${c}"><div class="n">${esc(a[0])}</div><div class="d">${esc(a[1])}</div><div class="g">${esc(a[2])}</div><div class="e">${esc(a[3])}</div></div>`).join('')}</div><div class="note">${esc(p.note)}</div>`;
}
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1000,height:1500}});
for(const p of pins){await pg.setContent(`<html><head><style>${css}</style></head><body><div class="pin ${p.tpl}" style="--ph:${p.ph||PH[p.tpl]}px"><div class="photo" style="background-image:url(${img(p)})"><span class="kicker">${esc(p.kicker)}</span></div><div class="content">${body(p)}${foot(p)}</div></div></body></html>`);
await pg.evaluate(()=>document.fonts.ready);
await pg.evaluate(()=>{const pin=document.querySelector('.pin');const ph=parseFloat(getComputedStyle(pin).getPropertyValue('--ph'));
const meas=()=>{const f=document.querySelector('.foot').getBoundingClientRect();const c=document.querySelector('.content');const kids=[...c.children].filter(e=>!e.classList.contains('foot'));const sc=c.scrollHeight-c.clientHeight;return sc>0?sc+40:Math.max(...kids.map(e=>e.getBoundingClientRect().bottom))-f.top};
const o=meas();const np=Math.max(300,Math.min(940,ph-o-40));pin.style.setProperty('--ph',np+'px');});
const over=await pg.evaluate(()=>{const f=document.querySelector('.foot').getBoundingClientRect();const kids=[...document.querySelector('.content').children].filter(e=>!e.classList.contains('foot')&&!e.classList.contains('blob'));const c=document.querySelector('.content');return [Math.max(...kids.map(e=>e.getBoundingClientRect().bottom))-f.top, c.scrollHeight-c.clientHeight, Math.max(...[...document.querySelectorAll('h1,.sub,li,.row,.ans div,.card *')].map(e=>e.scrollWidth-e.clientWidth))]});
console.log(p.id,p.tpl,over.map(Math.round).join(','));
await pg.screenshot({path:`${OUT}/pin-${p.id}.jpg`,type:'jpeg',quality:90});}
await b.close();})();
