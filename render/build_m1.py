"""m1-vorcaro: recorte de jornal exagerado (papel de verdade)."""
import pathlib, asyncio, html, random
from playwright.async_api import async_playwright

F = pathlib.Path("/home/claude/repo/assets/fonts")
OUT = pathlib.Path("/home/claude/posts/out/m1-vorcaro"); OUT.mkdir(parents=True, exist_ok=True)

NOISE = ("data:image/svg+xml;utf8,"
 "<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'>"
 "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
 "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter>"
 "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
FIBRA = ("data:image/svg+xml;utf8,"
 "<svg xmlns='http://www.w3.org/2000/svg' width='600' height='600'>"
 "<filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.012 .09' numOctaves='4' seed='7'/>"
 "<feColorMatrix values='0 0 0 0 .35  0 0 0 0 .27  0 0 0 0 .12  0 0 0 .5 0'/></filter>"
 "<rect width='100%' height='100%' filter='url(%23f)'/></svg>")

def torn(seed, jag=1.6, steps=34):
    r = random.Random(seed); top, bot = [], []
    for i in range(steps + 1):
        x = 100 * i / steps
        top.append((x, r.uniform(0, jag)))
        bot.append((x, 100 - r.uniform(0, jag)))
    pts = top + list(reversed(bot))
    return "polygon(" + ",".join(f"{x:.2f}% {y:.2f}%" for x, y in pts) + ")"

CSS = f"""
@font-face{{font-family:Play;font-weight:900;src:url(file://{F}/playfair-display-latin-900-normal.woff2)}}
@font-face{{font-family:Play;font-weight:700;src:url(file://{F}/playfair-display-latin-700-normal.woff2)}}
@font-face{{font-family:Osw;font-weight:700;src:url(file://{F}/oswald-latin-700-normal.woff2)}}
@font-face{{font-family:Type;src:url(file://{F}/special-elite-latin-400-normal.woff2)}}
@font-face{{font-family:Mono;font-weight:700;src:url(file://{F}/ibm-plex-mono-latin-700-normal.woff2)}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;background:#0D0C0B}}
body:before{{content:"";position:absolute;inset:0;background:url("{NOISE}");opacity:.35;mix-blend-mode:screen}}
body:after{{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 45%,rgba(0,0,0,.75) 100%);pointer-events:none}}
.sombra{{position:absolute;filter:drop-shadow(0 28px 40px rgba(0,0,0,.75))}}
.papel{{position:relative;background:#E8E0CB;color:#171512;padding:58px 56px 70px;overflow:hidden}}
.papel:before{{content:"";position:absolute;inset:0;background:url("{FIBRA}"),radial-gradient(rgba(0,0,0,.07) 1px,transparent 1.6px) 0 0/7px 7px;mix-blend-mode:multiply;opacity:.9}}
.papel:after{{content:"";position:absolute;inset:0;box-shadow:inset 0 0 140px rgba(120,88,30,.45);
background:linear-gradient(90deg,transparent 61%,rgba(255,255,255,.35) 61.4%,rgba(0,0,0,.16) 62%,transparent 64%)}}
.mast{{position:relative;z-index:1;display:flex;justify-content:space-between;align-items:baseline;border-top:2px solid #171512;border-bottom:5px double #171512;padding:10px 0 12px;margin-bottom:26px}}
.mast b{{font:700 44px/1 Play,serif;letter-spacing:.04em;text-transform:uppercase}}
.mast span{{font:700 24px/1 Mono,monospace;letter-spacing:.12em}}
.hd{{position:relative;z-index:1;font:900 98px/1.0 Play,serif;letter-spacing:-.015em;text-shadow:0 0 1px rgba(23,21,18,.65)}}
.cols{{position:relative;z-index:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;margin-top:34px;border-top:1px solid #171512;padding-top:18px}}
.cols div{{height:150px;background:repeating-linear-gradient(180deg,rgba(23,21,18,.38) 0 5px,transparent 5px 15px)}}
.stamp{{position:absolute;z-index:3;color:#C8102E;border:9px solid #C8102E;outline:3px solid #C8102E;outline-offset:7px;
font:700 92px/1 Osw,sans-serif;letter-spacing:.06em;padding:12px 26px 4px;transform:rotate(-10deg);opacity:.9;mix-blend-mode:multiply}}
.fita{{position:absolute;z-index:4;background:#EFE9DA;color:#1A1815;font:400 38px/1.3 Type,monospace;padding:22px 28px;box-shadow:0 10px 24px rgba(0,0,0,.45)}}
.fita:before{{content:"";position:absolute;inset:0;background:url("{NOISE}");opacity:.18;mix-blend-mode:multiply}}
.durex{{position:absolute;z-index:5;width:170px;height:46px;background:rgba(235,230,210,.55);box-shadow:0 2px 6px rgba(0,0,0,.25)}}
"""

def doc(body):
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'

def recorte(head, veiculo, data, nota, stamp=None, seed=1, rot=-1.6, top=150, nota_top=1010, hs=98, stamp_top=780):
    st = f'<div class="stamp" style="right:80px;top:{stamp_top}px">{stamp}</div>' if stamp else ""
    return doc(f"""
<div class="sombra" style="left:46px;top:{top}px;width:988px;transform:rotate({rot}deg)">
 <div class="papel" style="clip-path:{torn(seed)}">
  <div class="mast"><b>{html.escape(veiculo)}</b><span>{html.escape(data)}</span></div>
  <div class="hd" style="font-size:{hs}px">{html.escape(head)}</div>
  <div class="cols"><div></div><div></div><div></div></div>
 </div>
</div>
{st}
<div class="durex" style="left:110px;top:{top-14}px;transform:rotate(-8deg)"></div>
<div class="fita" style="left:70px;right:120px;top:{nota_top}px;transform:rotate(1deg)">{html.escape(nota)}</div>
""")

S1 = recorte("Polícia Federal prende Daniel Vorcaro em escândalo do Banco Master","O Povo","04.03.2026",
             "O Banco Master deixou R$ 40,6 bilhões em dívidas com cerca de 800 mil investidores.","PRESO",seed=3,rot=-1.8,top=120,nota_top=1060,stamp_top=800)
S2 = doc(f"""
<div class="sombra" style="left:90px;top:300px;width:900px;transform:rotate(2deg)">
 <div class="papel" style="clip-path:{torn(9,2.2)};padding:70px 64px 80px">
  <div class="hd" style="font-size:132px;line-height:.98">“Amigos de todos os poderes.”</div>
 </div>
</div>
<div class="durex" style="right:150px;top:286px;transform:rotate(9deg)"></div>
<div class="fita" style="left:110px;right:200px;top:920px;transform:rotate(-1.2deg)">Daniel Vorcaro, em depoimento à Polícia Federal.</div>
""")
S3 = recorte("Lula recebeu Vorcaro, dono do Master, sem registro na agenda","Poder360","26.01.2026",
             "Foi em 4 de dezembro de 2024, no Planalto, fora da agenda oficial. Lula não comentou o encontro.",seed=5,rot=1.4,top=170,nota_top=1010,hs=112)
S4 = recorte("Flávio Bolsonaro admite cobrança a Vorcaro, mas nega crime","Agência Brasil","13.05.2026",
             "R$ 134 milhões pedidos pra um filme sobre o pai. Ele diz: “Não ofereci vantagens em troca.”",seed=11,rot=-1.2,top=170,nota_top=1010,hs=112)
S5 = doc("""
<div style="position:absolute;left:80px;top:330px;background:#C8102E;color:#F3EFE6;font:700 124px/1 Osw,sans-serif;letter-spacing:.02em;padding:26px 40px 18px;white-space:nowrap;transform:rotate(-2deg)">FALTAM 5 DIAS</div>
<div class="fita" style="left:100px;right:110px;top:600px;transform:rotate(1.2deg);font-size:46px">Lula recebeu Vorcaro no Planalto em dezembro de 2024.<br>Flávio pediu R$ 134 milhões a ele pra um filme sobre o pai.</div>
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, h in enumerate([S1, S2, S3, S4, S5], 1):
            f = OUT/"tmp.html"; f.write_text(h, encoding="utf-8")
            await pg.goto(f"file://{f}"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(OUT/f"{i:02d}.jpg"), type="jpeg", quality=92)
        (OUT/"tmp.html").unlink(); await b.close()
if __name__ == "__main__":
    asyncio.run(main())
