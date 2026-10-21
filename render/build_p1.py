import pathlib, asyncio, html
from playwright.async_api import async_playwright
from build_m1 import doc, torn

OUT = pathlib.Path("/home/claude/posts/out/p1-processos"); OUT.mkdir(parents=True, exist_ok=True)

def clip(head, veiculo, data, stamp, seed, rot, left, top, width, hs, stamp_pos):
    return f"""
<div class="sombra" style="left:{left}px;top:{top}px;width:{width}px;transform:rotate({rot}deg)">
 <div class="papel" style="clip-path:{torn(seed)}">
  <div class="mast"><b>{html.escape(veiculo)}</b><span>{html.escape(data)}</span></div>
  <div class="hd" style="font-size:{hs}px">{html.escape(head)}</div>
  <div class="cols"><div></div><div></div><div></div></div>
 </div>
</div>
<div class="stamp" style="{stamp_pos}">{stamp}</div>"""

LULA = ("Fachin anula as condenações de Lula na Lava Jato","Migalhas","08.03.2021")
FLAVIO = ("TJ do Rio arquiva denúncia do MP contra Flávio Bolsonaro em caso das “rachadinhas”","InfoMoney / Reuters","17.05.2022")

S1 = doc(clip(*LULA,"ANULADO",2,-3,40,70,700,74,"left:330px;top:475px;font-size:62px")
       + clip(*FLAVIO,"ARQUIVADO",8,2.5,330,600,710,56,"left:520px;top:1120px;font-size:64px;transform:rotate(-8deg)"))
S2 = doc(clip(*LULA,"ANULADO",4,-1.5,46,110,988,112,"right:80px;top:650px")
       + '<div class="fita" style="left:70px;right:110px;top:860px;transform:rotate(1deg)">Condenado em 2017 e em 2018, ficou 580 dias preso em Curitiba. Em 2021, o STF decidiu que a Vara de Curitiba não podia julgar os casos. A decisão tratou de quem podia julgar, não de culpa ou inocência.</div>')
S3 = doc(clip(*FLAVIO,"ARQUIVADO",12,1.3,46,100,988,84,"right:60px;top:740px;font-size:78px")
       + '<div class="fita" style="left:70px;right:110px;top:930px;transform:rotate(-1deg)">Ele era acusado de peculato, lavagem de dinheiro, organização criminosa e apropriação indébita. Em 2022, o TJ do Rio arquivou a denúncia porque o STJ considerou as provas ilícitas. O mérito nunca foi julgado.</div>')
S4 = doc("""
<div class="sombra" style="left:70px;top:250px;width:940px;transform:rotate(-1.2deg)">
 <div class="papel" style="clip-path:""" + torn(21) + """;padding:64px 60px 76px">
  <div class="hd" style="font-size:104px">Um desses dois vai nos governar pelos próximos 4 anos.</div>
 </div>
</div>
<div style="position:absolute;left:90px;top:900px;background:#C8102E;color:#F3EFE6;font:700 82px/1.1 Osw,sans-serif;padding:26px 40px 20px;transform:rotate(1.5deg);max-width:880px">Você já pensou no seu plano de fuga?</div>
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1080,"height":1350})
        for i, h in enumerate([S1, S2, S3, S4], 1):
            f = OUT/"tmp.html"; f.write_text(h, encoding="utf-8")
            await pg.goto(f"file://{f}"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(OUT/f"{i:02d}.jpg"), type="jpeg", quality=92)
        (OUT/"tmp.html").unlink(); await b.close()
asyncio.run(main())
