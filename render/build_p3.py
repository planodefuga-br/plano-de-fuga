import pathlib, asyncio, html
from playwright.async_api import async_playwright
from build_m1 import doc, torn

OUT = pathlib.Path("/home/claude/posts/out/p3-inss"); OUT.mkdir(parents=True, exist_ok=True)

def clip(head, veiculo, data, stamp, seed, rot, left, top, width, hs, stamp_pos):
    return f"""
<div class="sombra" style="left:{left}px;top:{top}px;width:{width}px;transform:rotate({rot}deg)">
 <div class="papel" style="clip-path:{torn(seed)}">
  <div class="mast"><b>{html.escape(veiculo)}</b><span>{html.escape(data)}</span></div>
  <div class="hd" style="font-size:{hs}px">{html.escape(head)}</div>
  <div class="cols"><div></div><div></div><div></div></div>
 </div>
</div>
{"" if not stamp else f'<div class="stamp" style="{stamp_pos}">{stamp}</div>'}"""

LULA = ("Fraude de R$ 6,3 bi: presidente do INSS é afastado em operação da PF","Congresso em Foco","23.04.2025")
FLAVIO = ("Fraude do INSS é culpa do governo Lula ou do governo Bolsonaro? O que é fato na batalha de versões","BBC News Brasil / A Gazeta","30.04.2025")

S1 = doc(clip(*LULA,None,2,-3,40,70,700,68,"left:300px;top:540px;font-size:58px")
       + clip(*FLAVIO,None,8,2.5,330,640,710,64,"left:480px;top:1130px;font-size:58px;transform:rotate(-8deg)"))
S2 = doc(clip(*LULA,None,4,-1.5,46,110,988,104,"right:70px;top:760px;font-size:70px")
       + '<div class="fita" style="left:70px;right:110px;top:940px;transform:rotate(1deg)">A PF e a CGU calcularam R$ 6,3 bilhões descontados de aposentados entre 2019 e 2024, em mensalidades de associações. A CGU diz que nem todo desconto era ilegal.</div>')
S3 = doc(clip(*FLAVIO,None,12,1.3,46,110,988,80,"right:60px;top:720px;font-size:74px")
       + '<div class="fita" style="left:70px;right:110px;top:1000px;transform:rotate(-1deg)">2022, governo de Jair Bolsonaro, pai do Flávio: R$ 706 milhões. 2023, governo Lula: R$ 1,3 bilhão. Pra 2024, a CGU projetou R$ 2,6 bilhões. A operação que expôs o esquema foi em abril de 2025, no governo Lula.</div>')
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
