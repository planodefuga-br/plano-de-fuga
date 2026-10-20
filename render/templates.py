"""HTML dos dois mundos do Plano de Fuga.
POL  = recorte de jornal sombrio (política)
GUIA = página de passaporte (marca / guias)
Paralelo mínimo: os dois têm a linha MRZ no rodapé e o carimbo de SAÍDA no fim.
"""
import html, math, random, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONTS = (ROOT / "assets" / "fonts").as_uri()

def esc(s): return html.escape(s or "")

FONT_CSS = f"""
@font-face{{font-family:Play;src:url({FONTS}/playfair-display-latin-900-normal.woff2);font-weight:900}}
@font-face{{font-family:Play;src:url({FONTS}/playfair-display-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:Osw;src:url({FONTS}/oswald-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:Osw;src:url({FONTS}/oswald-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:Mono;src:url({FONTS}/ibm-plex-mono-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:Mono;src:url({FONTS}/ibm-plex-mono-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:Type;src:url({FONTS}/special-elite-latin-400-normal.woff2)}}
@font-face{{font-family:Serif;src:url({FONTS}/dm-serif-display-latin-400-normal.woff2)}}
@font-face{{font-family:Nar;src:url({FONTS}/archivo-narrow-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:Nar;src:url({FONTS}/archivo-narrow-latin-700-normal.woff2);font-weight:700}}
"""

NOISE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
GRUNGE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='200'>"
          "<filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.045' numOctaves='4' seed='7'/>"
          "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.6 2.1'/></filter>"
          "<rect width='100%' height='100%' filter='url(%23g)'/></svg>")

def torn(seed, jag=10, steps=26):
    r = random.Random(seed)
    pts = []
    for i in range(steps + 1): pts.append((i / steps * 100, r.uniform(0, jag) / 10))
    for i in range(1, 8): pts.append((100 - r.uniform(0, .6), i / 8 * 100))
    for i in range(steps, -1, -1): pts.append((i / steps * 100, 100 - r.uniform(0, jag) / 10))
    for i in range(7, 0, -1): pts.append((r.uniform(0, .6), i / 8 * 100))
    return "polygon(" + ",".join(f"{x:.2f}% {y:.2f}%" for x, y in pts) + ")"

def guilloche(w, h, color):
    paths = []
    for k in range(22):
        amp = 18 + 6 * math.sin(k)
        ph = k * 0.55
        y0 = h * (k + .5) / 22
        d = "M0," + f"{y0:.1f}"
        for x in range(0, w + 12, 12):
            y = y0 + amp * math.sin(x / 70 + ph) + 7 * math.sin(x / 23 + ph * 2)
            d += f" L{x},{y:.1f}"
        paths.append(f"<path d='{d}' fill='none' stroke='{color}' stroke-width='1.1'/>")
    for k in range(9):
        cx, cy = w * .78, h * .3
        paths.append(f"<ellipse cx='{cx}' cy='{cy}' rx='{140+k*26}' ry='{90+k*17}' fill='none' stroke='{color}' stroke-width='1' transform='rotate({k*9} {cx} {cy})'/>")
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>{''.join(paths)}</svg>"
    return "data:image/svg+xml;utf8," + svg.replace("#", "%23").replace("<", "%3C").replace(">", "%3E")

def mrz(label):
    a = "P<BRA<PLANO<DE<FUGA"
    b = "<".join(label.upper().replace("·", "").split())
    b = "".join(c for c in b.replace("Ç", "C").replace("Ã", "A").replace("Á", "A").replace("É", "E").replace("Ê", "E").replace("Í", "I").replace("Ó", "O").replace("Õ", "O").replace("Ú", "U") if c.isalnum() or c == "<")
    return (a + "<<" + b + "<" * 60)[:44]

# ---------------------------------------------------------------- POL
POL_CSS = """
:root{--bg:#0E0D0C;--paper:#E7E1D2;--pink:#141210;--red:#C8102E;--white:#F1ECE2;--mute:#8C867A;--tape:#EFEADF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:var(--W);height:var(--H);background:var(--bg);overflow:hidden}
.f{position:relative;width:var(--W);height:var(--H);padding:var(--pad);display:flex;flex-direction:column;
 background:radial-gradient(120% 80% at 50% 40%,#1E1B18 0%,var(--bg) 70%)}
.f::after{content:'';position:absolute;inset:0;background:url("NOISE");opacity:.33;pointer-events:none;mix-blend-mode:screen}
.bar{display:flex;justify-content:space-between;align-items:center;font:500 var(--mono)/1 Mono,monospace;letter-spacing:.16em;color:var(--mute);text-transform:uppercase}
.bar b{color:var(--white);font-weight:700}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:var(--gap);min-height:0;position:relative;z-index:1}
.kick{align-self:flex-start;background:var(--red);color:var(--white);font:700 var(--kick)/1 Osw,sans-serif;letter-spacing:.04em;padding:.18em .32em .12em;transform:rotate(-1.5deg)}
.hook{font:700 var(--hook)/1.02 Osw,sans-serif;color:var(--white);text-transform:uppercase;letter-spacing:-.005em}
.say{font:700 var(--say)/1.05 Osw,sans-serif;color:var(--white);text-transform:uppercase}
.sub{font:500 var(--sub)/1.3 Nar,sans-serif;color:#BDB6A8;max-width:30ch}
.clipwrap{position:relative;align-self:center;width:100%}
.clip{position:relative;background:var(--paper);color:var(--pink);padding:var(--cpad);clip-path:var(--torn);transform:rotate(var(--rot))}
.clip::after{content:'';position:absolute;inset:0;background:url("NOISE");opacity:.22;mix-blend-mode:multiply}
.clip .mast{display:flex;justify-content:space-between;font:700 var(--mono)/1 Mono,monospace;letter-spacing:.14em;border-bottom:3px double var(--pink);padding-bottom:.7em;margin-bottom:.6em}
.clip .hd{font:900 var(--head)/1.04 Play,serif;letter-spacing:-.012em}
.clip.hs{padding-bottom:calc(var(--stamp)*1.55)}
.stamp{position:absolute;right:5%;bottom:3%;z-index:3;color:var(--red);border:.09em solid var(--red);outline:.03em solid var(--red);outline-offset:.08em;
 font:700 var(--stamp)/1 Osw,sans-serif;letter-spacing:.06em;padding:.12em .3em .06em;transform:rotate(-9deg);
 -webkit-mask-image:url("GRUNGE");-webkit-mask-size:cover;mix-blend-mode:normal;background:rgba(200,16,46,.06)}
.tape{align-self:flex-start;max-width:92%;background:var(--tape);color:#1A1815;font:400 var(--note)/1.32 Type,monospace;padding:.5em .7em;transform:rotate(.8deg);box-shadow:0 8px 20px rgba(0,0,0,.35)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;font:500 var(--mono)/1.4 Mono,monospace;color:var(--mute);letter-spacing:.04em;position:relative;z-index:1}
.mrz{font:500 var(--mono)/1 Mono,monospace;color:#4A463F;letter-spacing:.12em;white-space:nowrap;overflow:hidden;margin-top:14px;position:relative;z-index:1}
.split{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.col{background:var(--paper);color:var(--pink);padding:26px 24px;clip-path:var(--torn);display:flex;flex-direction:column;gap:14px}
.col .tag{font:700 var(--mono)/1.1 Mono,monospace;letter-spacing:.12em;color:var(--red)}
.col .big{font:900 calc(var(--head)*1.05)/1 Play,serif}
.col .txt{font:500 var(--sub)/1.3 Nar,sans-serif}
.col .txt div{padding:12px 0;border-top:2px solid rgba(20,18,16,.18)}
.col .txt div:first-child{border-top:none;padding-top:0}
.exitstamp{align-self:flex-start;color:#E8B23A;border:.08em solid #E8B23A;border-radius:.25em;padding:.25em .45em;font:700 var(--stamp)/1 Osw,sans-serif;letter-spacing:.08em;transform:rotate(-6deg);
 -webkit-mask-image:url("GRUNGE");-webkit-mask-size:cover;display:flex;flex-direction:column;gap:.15em}
.exitstamp small{font:700 calc(var(--stamp)*.32)/1 Mono,monospace;letter-spacing:.2em}
.arrow{color:var(--red);font:700 calc(var(--mono)*2.4)/1 Osw,sans-serif}
""".replace("NOISE", NOISE).replace("GRUNGE", GRUNGE)

SIZES = {
 "post":  dict(W=1080, H=1350, pad="64px 72px 46px", gap="34px", mono="22px", kick="64px", hook="118px", say="98px", sub="34px", cpad="44px 48px 56px", head="86px", stamp="78px", note="34px"),
 "story": dict(W=1080, H=1920, pad="230px 84px 330px", gap="44px", mono="24px", kick="78px", hook="128px", say="112px", sub="38px", cpad="52px 54px 66px", head="104px", stamp="92px", note="42px"),
}

def _vars(sz):
    v = SIZES[sz]
    return ";".join(f"--{k}:{val}px" if isinstance(val, int) else f"--{k}:{val}" for k, val in v.items())

def _words(txt, reveal):
    if reveal is None: return esc(txt)
    ws = txt.split(" ")
    return " ".join(esc(w) if k < reveal else f'<span style="visibility:hidden">{esc(w)}</span>' for k, w in enumerate(ws))

def pol_slide(sl, i, n, kicker, sz="post", seed=0, show_stamp=True, reveal=None):
    t = sl["t"]
    parts = []
    if t in ("cover", "title"):
        parts.append(f'<div class="kick">{esc(sl["k"])}</div><div class="hook">{_words(sl["h"], reveal)}</div>')
    elif t == "clip":
        rot = [-1.4, 1.1, -0.6, 1.6, -1.8, 0.7][seed % 6]
        stamp = f'<div class="stamp">{esc(sl["stamp"])}</div>' if sl.get("stamp") and show_stamp else ""
        parts.append(f'''<div class="clipwrap"><div class="clip{' hs' if sl.get('stamp') else ''}" style="--rot:{rot}deg;--torn:{torn(seed*7+3)}">
<div class="mast"><span>{esc(sl["outlet"])}</span><span>{esc(sl["date"])}</span></div>
<div class="hd">{esc(sl["head"])}</div></div>{stamp}</div>''')
        if sl.get("note"): parts.append(f'<div class="tape">{esc(sl["note"])}</div>')
    elif t == "say":
        parts.append(f'<div class="say">{_words(sl["h"], reveal)}</div>')
        if sl.get("s"): parts.append(f'<div class="sub">{esc(sl["s"])}</div>')
    elif t == "split":
        def col(c, s):
            txt = c["txt"]
            inner = "".join(f"<div>{esc(x)}</div>" for x in txt.split("\n")) if "\n" in txt else esc(txt)
            big = f'<div class="big">{esc(c["big"])}</div>' if c.get("big") else ""
            return f'<div class="col" style="--torn:{torn(s,6)}"><span class="tag">{esc(c["tag"])}</span>{big}<div class="txt">{inner}</div></div>'
        parts.append(f'<div class="say" style="font-size:calc(var(--say)*.72)">{esc(sl["h"])}</div><div class="split">{col(sl["l"],seed+1)}{col(sl["r"],seed+2)}</div>')
    elif t == "exit":
        parts.append('<div class="exitstamp"><small>SAÍDA · DEPARTURE</small>PLANO DE FUGA<small>✈ BRASIL → MUNDO</small></div>')
        parts.append(f'<div class="say" style="font-size:calc(var(--say)*.78)">{_words(sl["h"], reveal)}</div>')
        if sz == "post": parts.append(f'<div class="sub">Bolsa, visto e trabalho fora do Brasil. Todo dia aqui.</div>')
    src = sl.get("src")
    if t == "clip" and not src: src = None
    foot_l = f"FONTE · {esc(src)}" if src else ""
    arrow = '<span class="arrow">→</span>' if (sz == "post" and i < n - 1) else ""
    counter = f"{i+1}/{n}" if sz == "post" else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}{POL_CSS}</style></head>
<body style="{_vars(sz)}"><div class="f">
{'' if sz == "story" else f'<div class="bar"><b>✈ PLANO DE FUGA</b><span>{esc(kicker)}{" · " + counter if counter else ""}</span></div>'}
<div class="body">{''.join(parts)}</div>
{'' if sz == "story" else f'<div class="foot"><span>{foot_l}</span>{arrow}</div><div class="mrz">{esc(mrz(kicker))}</div>'}
</div></body></html>"""

# ---------------------------------------------------------------- GUIA
GUIA_CSS = """
:root{--page:#DCE6DF;--guil:#B8CCC1;--navy:#14284A;--red:#A3203A;--teal:#1C6B73;--gold:#9E7C2F;--mute:#4F6170}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:var(--page);overflow:hidden}
.f{position:relative;width:1080px;height:1350px;padding:62px 76px 40px;display:flex;flex-direction:column;background:var(--page) url("GUIL") center/cover no-repeat}
.f::after{content:'';position:absolute;inset:0;background:url("NOISE");opacity:.12;mix-blend-mode:multiply;pointer-events:none}
.bar{display:flex;justify-content:space-between;align-items:center;font:700 22px/1 Mono,monospace;letter-spacing:.18em;color:var(--navy);text-transform:uppercase}
.bar span{color:var(--mute);font-weight:500}
.rule{margin-top:22px;height:2px;background:repeating-linear-gradient(90deg,var(--navy) 0 10px,transparent 10px 16px);opacity:.45}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:30px;min-height:0;position:relative;z-index:1}
.lab{font:700 24px/1 Mono,monospace;letter-spacing:.2em;color:var(--teal)}
.lab i{font-style:normal;color:var(--mute);font-weight:500}
.h{font:400 92px/1.02 Serif,serif;color:var(--navy);letter-spacing:-.01em}
.cover .h{font-size:104px}
.s{font:500 38px/1.3 Nar,sans-serif;color:#2B3D57;max-width:30ch}
.stamp{align-self:flex-start;color:var(--red);border:7px solid var(--red);border-radius:18px;padding:18px 28px 14px;transform:rotate(-7deg);display:flex;flex-direction:column;align-items:center;gap:8px;
 -webkit-mask-image:url("GRUNGE");-webkit-mask-size:cover;opacity:.88}
.stamp .c{font:700 58px/1 Osw,sans-serif;letter-spacing:.06em}
.stamp .l{font:700 22px/1 Mono,monospace;letter-spacing:.22em;border-top:3px solid var(--red);border-bottom:3px solid var(--red);padding:8px 4px}
.stamp .d{font:700 26px/1 Mono,monospace;letter-spacing:.14em}
.stamp.teal{color:var(--teal);border-color:var(--teal)}.stamp.teal .l{border-color:var(--teal)}
.foot{display:flex;justify-content:space-between;align-items:flex-end;font:500 20px/1.4 Mono,monospace;color:var(--mute);position:relative;z-index:1;gap:30px}
.arrow{font:700 54px/1 Osw,sans-serif;color:var(--red)}
.mrz{font:500 24px/1.25 Mono,monospace;color:var(--navy);letter-spacing:.12em;white-space:nowrap;overflow:hidden;opacity:.75;margin-top:16px;position:relative;z-index:1}
.pg{font:500 20px/1 Mono,monospace;color:var(--mute)}
""".replace("NOISE", NOISE).replace("GRUNGE", GRUNGE)

_GUIL = None
def guia_slide(post, sl, i, n):
    global _GUIL
    if _GUIL is None: _GUIL = guilloche(1080, 1350, "#B8CCC1")
    t = sl["t"]
    kicker = post["slides"][0]["k"]
    country, label = post["stamp"]
    parts = []
    if t == "cover":
        parts.append(f'<div class="stamp"><span class="l">{esc(label)}</span><span class="c">{esc(country)}</span><span class="d">OUT · 2026</span></div>')
        parts.append(f'<div class="lab">{esc(kicker)}</div><div class="h">{esc(sl["h"])}</div>')
    elif t == "page":
        parts.append(f'<div class="lab">{esc(sl["lab"])}</div><div class="h">{esc(sl["h"])}</div>')
        if sl.get("s"): parts.append(f'<div class="s">{esc(sl["s"])}</div>')
    elif t == "cta":
        parts.append('<div class="stamp teal"><span class="l">SAÍDA · DEPARTURE</span><span class="c">PLANO DE FUGA</span><span class="d">✈ BRASIL → MUNDO</span></div>')
        parts.append(f'<div class="h" style="font-size:80px">{esc(sl["h"])}</div>')
        if sl.get("s"): parts.append(f'<div class="s">{esc(sl["s"])}</div>')
    src = f'FONTE · {esc(sl["src"])}' if sl.get("src") else ""
    arrow = '<span class="arrow">→</span>' if i < n - 1 else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}{GUIA_CSS.replace('GUIL', _GUIL)}</style></head>
<body><div class="f {t}">
<div class="bar">✈ PLANO DE FUGA<span></span></div><div class="rule"></div>
<div class="body">{''.join(parts)}</div>
<div class="foot"><span>{src}</span>{arrow}</div>
</div></body></html>"""

FIT_JS = """() => {
  const body = document.querySelector('.body');
  const targets = [...document.querySelectorAll('.hd,.hook,.say,.h,.col .big')];
  let guard = 0;
  while (body.scrollHeight > body.clientHeight + 1 && guard++ < 60) {
    targets.forEach(e => { const f = parseFloat(getComputedStyle(e).fontSize); e.style.fontSize = (f * 0.95) + 'px'; });
    document.querySelectorAll('.tape,.sub,.s,.col .txt').forEach(e => { const f = parseFloat(getComputedStyle(e).fontSize); if (f > 24) e.style.fontSize = (f * 0.97) + 'px'; });
  }
  return body.scrollHeight <= body.clientHeight + 1;
}"""
