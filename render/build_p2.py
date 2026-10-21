import pathlib, asyncio, html
from playwright.async_api import async_playwright
from build_m1 import doc, torn

OUT = pathlib.Path("/home/claude/posts/out/p2-condenados"); OUT.mkdir(parents=True, exist_ok=True)

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

LULA = ("Supremo condena Dirceu por compra de voto no Congresso","Folha de S.Paulo","10.10.2012")
FLAVIO = ("STF condena Bolsonaro a 27 anos e três meses de prisão","Diário do Comércio","11.09.2025")

S1 = doc(clip(*LULA,"CONDENADO",2,-3,40,70,700,68,"left:300px;top:540px;font-size:58px")
       + clip(*FLAVIO,"CONDENADO",8,2.5,330,640,710,64,"left:480px;top:1130px;font-size:58px;transform:rotate(-8deg)"))
S2 = doc(clip(*LULA,"CONDENADO",4,-1.5,46,110,988,104,"right:70px;top:760px;font-size:70px")
       + '<div class="fita" style="left:70px;right:110px;top:940px;transform:rotate(1deg)">José Dirceu era o chefe da Casa Civil no 1º governo Lula. Foi condenado pelo STF por corrupção ativa no mensalão. Lula não foi denunciado: a Procuradoria deixou ele de fora.</div>')
S3 = doc(clip(*FLAVIO,"CONDENADO",12,1.3,46,140,988,104,"right:60px;top:720px;font-size:74px")
       + '<div class="fita" style="left:70px;right:110px;top:930px;transform:rotate(-1deg)">Jair Bolsonaro, pai do Flávio, foi condenado pela 1ª Turma do STF por tentativa de golpe de Estado e outros crimes. Flávio não foi réu nesse processo.</div>')
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
