"""Gera review/index.html (página de aprovação) + previews leves dos Reels."""
import json, html, subprocess, pathlib, shutil, datetime as dt
ROOT = pathlib.Path(__file__).resolve().parents[1]
REV = ROOT / "review"; REV.mkdir(exist_ok=True)
m = json.loads((ROOT / "docs" / "manifest.json").read_text())
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
files = []
days = {}
for p in m:
    t = dt.datetime.fromisoformat(p["publish_at"].replace("Z", "+00:00")) - dt.timedelta(hours=3)
    days.setdefault(t.date(), []).append((t, p))
rows = []
for d in sorted(days):
    cards = []
    for t, p in sorted(days[d], key=lambda x: x[0]):
        if p["type"] == "reel":
            prev = f"reels/{p['id']}.mp4"; (REV / "reels").mkdir(exist_ok=True)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(ROOT / "docs" / p["media"][0]), "-vf", "scale=360:640",
                            "-c:v", "libx264", "-crf", "28", "-preset", "fast", "-an", "-movflags", "+faststart", str(REV / prev)], check=True)
            files.append(prev)
            media = f'<video src="{prev}" controls muted playsinline preload="metadata" width="216" height="384"></video>'
            kind, mode = "Reel", "você posta no app, com Happy Nation"
        else:
            media = "".join(f'<img src="{f}" alt="slide {i+1}" loading="lazy" width="216" height="270">' for i, f in enumerate(p["media"]))
            files += p["media"]
            for f in p["media"]:
                (REV / f).parent.mkdir(parents=True, exist_ok=True); shutil.copy(ROOT / "docs" / f, REV / f)
            kind = "Guia" if p["id"].startswith("g") else "Carrossel"
            mode = "automático"
        cards.append(f'''<article class="post {'pol' if not p['id'].startswith('g') else 'guia'}">
<header><span class="time">{t:%H:%M}</span><span class="kind">{kind}</span><span class="mode">{mode}</span></header>
<div class="strip">{media}</div>
<details><summary>Legenda</summary><pre>{html.escape(p["caption"])}</pre></details></article>''')
    rows.append(f'<section class="day"><div class="date"><b>{d.day:02d}/{d.month:02d}</b><span>{DIAS[d.weekday()]}</span></div><div class="posts">{"".join(cards)}</div></section>')

page = f'''<title>Plano de Fuga · Semana do 2º turno</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=IBM+Plex+Mono:wght@500;700&family=Archivo+Narrow:wght@500&display=swap">
<style>
/* Layout: quadro de embarque, uma linha por dia, com os posts lado a lado e faixas roláveis de slides */
:root{{--bg:#E3EBE5;--fg:#14284A;--mute:#55667A;--line:#B9CBC0;--card:#D4DFD8;--acc:#A3203A;--pol:#141210;
--d:'Oswald','Arial Narrow',sans-serif;--m:'IBM Plex Mono',ui-monospace,monospace;--b:'Archivo Narrow','Arial Narrow',sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0F1114;--fg:#EDE7DA;--mute:#8E949D;--line:#2A2F36;--card:#181B20;--acc:#E0485F;--pol:#000;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0F1114;--fg:#EDE7DA;--mute:#8E949D;--line:#2A2F36;--card:#181B20;--acc:#E0485F;--pol:#000;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:500 16px/1.5 var(--b)}}
.wrap{{max-width:1200px;margin:0 auto;padding-block:36px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.top{{display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:end;padding-bottom:18px;border-bottom:2px dashed var(--line)}}
.eye{{font:700 12px/1 var(--m);letter-spacing:.18em;color:var(--acc);text-transform:uppercase;margin-bottom:10px}}
h1{{font:700 clamp(30px,5vw,50px)/1 var(--d);margin:0;text-transform:uppercase;text-wrap:balance}}
.top p{{margin:0;max-width:52ch;color:var(--mute)}}
.day{{display:grid;grid-template-columns:84px 1fr;gap:18px;padding-block:22px;border-bottom:1px solid var(--line)}}
.date{{font-family:var(--m);display:flex;flex-direction:column}}
.date b{{font-size:22px;font-variant-numeric:tabular-nums}}
.date span{{color:var(--mute);font-size:12px;letter-spacing:.14em;text-transform:uppercase}}
.posts{{display:flex;flex-direction:column;gap:18px;min-width:0}}
.post{{min-width:0;display:flex;flex-direction:column;gap:8px}}
.post header{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;font:500 12px/1 var(--m);letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}}
.time{{background:var(--fg);color:var(--bg);padding:3px 7px;border-radius:3px;font-weight:700}}
.kind{{color:var(--fg);font-weight:700}}
.pol .kind{{color:var(--acc)}}
.strip{{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px}}
.strip img,.strip video{{flex:0 0 auto;width:min(216px,58vw);height:auto;border-radius:6px;border:1px solid var(--line);background:var(--card)}}
.strip img{{aspect-ratio:4/5}} .strip video{{aspect-ratio:9/16;background:var(--pol)}}
summary{{cursor:pointer;font:500 12px/1 var(--m);letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}}
summary:focus-visible{{outline:2px solid var(--acc);outline-offset:2px}}
pre{{white-space:pre-wrap;font:500 14px/1.45 var(--b);background:var(--card);padding:12px 14px;border-radius:6px;margin:8px 0 0}}
@media (max-width:560px){{.day{{grid-template-columns:1fr}} .date{{flex-direction:row;gap:10px;align-items:baseline}}}}
</style>
<div class="wrap"><div class="top"><div><div class="eye">✈ Plano de Fuga · revisão</div><h1>Semana do 2º turno</h1></div>
<p>De 20 a 25/10, em horário de Brasília. Os carrosséis e os guias saem sozinhos. Os Reels você posta pelo app com Happy Nation. Toda manchete é literal e tem veículo e data.</p></div>
{"".join(rows)}</div>'''
(REV / "index.html").write_text(page)
(REV / "files.json").write_text(json.dumps(files))
print(len(files), "arquivos")
