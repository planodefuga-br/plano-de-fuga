"""Gera tudo: carrosséis (docs/<id>/NN.jpg), cards dos Reels e o manifest.
Uso: python render/build.py [ids...]    (sem ids = tudo)
"""
import json, sys, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "render")); sys.path.insert(0, str(ROOT / "content"))
from templates import pol_slide, guia_slide, FIT_JS
import content as C

DOCS = ROOT / "docs"; BUILD = ROOT / "build"; TMP = BUILD / "tmp.html"

def shot(pg, html, out, w, h, scale=1, jpeg=True):
    BUILD.mkdir(exist_ok=True); TMP.write_text(html)
    pg.set_viewport_size({"width": w, "height": h})
    pg.goto(TMP.as_uri(), wait_until="load"); pg.evaluate("document.fonts.ready")
    ok = pg.evaluate(FIT_JS)
    out.parent.mkdir(parents=True, exist_ok=True)
    pg.screenshot(path=str(out), type="jpeg" if jpeg else "png", **({"quality": 92} if jpeg else {}))
    return ok

def main(only=None):
    warn = []; manifest = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg1 = b.new_page(device_scale_factor=1)
        pg2 = b.new_page(device_scale_factor=1.2)   # cards de Reel com folga pra zoom
        for post in C.POL + C.GUIA:
            if only and post["id"] not in only: continue
            is_pol = post in C.POL
            n = len(post["slides"]); files = []
            for i, sl in enumerate(post["slides"]):
                html = pol_slide(sl, i, n, post["slides"][0]["k"], "post", seed=i + len(post["id"])) if is_pol else guia_slide(post, sl, i, n)
                out = DOCS / post["id"] / f"{i+1:02d}.jpg"
                if not shot(pg1, html, out, 1080, 1350): warn.append(f"{post['id']} {i+1}")
                files.append(f"{post['id']}/{out.name}")
            manifest.append({"id": post["id"], "type": "carousel", "auto": True, "publish_at": post["publish_at"], "caption": post["caption"], "media": files})
        for reel in C.REELS:
            if only and reel["id"] not in only: continue
            kick = reel["cards"][0]["k"]; n = len(reel["cards"])
            d = BUILD / "reels" / reel["id"]
            for i, c in enumerate(reel["cards"]):
                html = pol_slide(c, i, n, kick, "story", seed=i * 3 + 1)
                if not shot(pg2, html, d / f"{i:02d}.png", 1080, 1920, jpeg=False): warn.append(f"{reel['id']} card {i}")
                if c.get("stamp"):
                    shot(pg2, pol_slide(c, i, n, kick, "story", seed=i * 3 + 1, show_stamp=False), d / f"{i:02d}_pre.png", 1080, 1920, jpeg=False)
        b.close()
    for reel in C.REELS:
        if only and reel["id"] not in only: continue
        dd, hh = reel["post_at_brt"].split()
        day, mon = dd.split("/"); h = int(hh.rstrip("h")) + 3
        manifest.append({"id": reel["id"], "type": "reel", "auto": False, "publish_at": f"2026-{mon}-{day}T{h:02d}:00:00Z",
                         "caption": reel["caption"], "media": [f"reels/{reel['id']}.mp4"],
                         "note": "Postar pelo app com o áudio Happy Nation. auto=false porque a API não põe música da biblioteca."})
    mpath = DOCS / "manifest.json"
    old = json.loads(mpath.read_text()) if mpath.exists() and only else []
    ids = {m["id"] for m in manifest}
    merged = [m for m in old if m["id"] not in ids] + manifest
    merged.sort(key=lambda m: m["publish_at"])
    DOCS.mkdir(exist_ok=True); mpath.write_text(json.dumps(merged, ensure_ascii=False, indent=1))
    (DOCS / ".nojekyll").touch()
    print(f"ok · {len(manifest)} carrosséis · avisos: {warn or 'nenhum'}")

if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
