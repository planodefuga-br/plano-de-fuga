"""Publica no Instagram o que já passou do horário no docs/manifest.json.
Roda no GitHub Actions a cada 15 min. Estado em publisher/state.json (commitado pelo workflow).
Env: IG_TOKEN (secret), PAGES_URL (ex.: https://usuario.github.io/plano-de-fuga)
"""
import json, os, sys, time, pathlib, urllib.request, urllib.parse, datetime as dt

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE = ROOT / "publisher" / "state.json"
GRAPH = "https://graph.instagram.com/v23.0"
TOKEN = os.environ["IG_TOKEN"]
BASE = os.environ["PAGES_URL"].rstrip("/")
LATE_H = 6
DRY = os.environ.get("DRY_RUN") == "1"

def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{GRAPH}/{path}"
    req = urllib.request.Request(url + ("?" + data.decode() if method == "GET" else ""), data=None if method == "GET" else data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path}: {e.code} {e.read().decode()[:500]}")

def wait_ready(cid, video=False):
    for _ in range(60 if video else 20):
        s = call("GET", cid, fields="status_code").get("status_code")
        if s == "FINISHED": return
        if s in ("ERROR", "EXPIRED"): raise RuntimeError(f"container {cid}: {s}")
        time.sleep(5 if video else 3)
    raise RuntimeError(f"container {cid} não ficou pronto")

def publish(ig, post):
    if post["type"] == "carousel":
        kids = [call("POST", f"{ig}/media", image_url=f"{BASE}/{m}", is_carousel_item="true")["id"] for m in post["media"]]
        for k in kids: wait_ready(k)
        c = call("POST", f"{ig}/media", media_type="CAROUSEL", children=",".join(kids), caption=post["caption"])["id"]
        wait_ready(c)
    elif post["type"] == "reel":
        c = call("POST", f"{ig}/media", media_type="REELS", video_url=f"{BASE}/{post['media'][0]}", caption=post["caption"], share_to_feed="true")["id"]
        wait_ready(c, video=True)
    else:
        raise RuntimeError("tipo desconhecido " + post["type"])
    if DRY: return "dry-run"
    return call("POST", f"{ig}/media_publish", creation_id=c)["id"]

def main():
    state = json.loads(STATE.read_text()) if STATE.exists() else {"published": {}, "failures": {}}
    me = call("GET", "me", fields="user_id,username")
    ig = me.get("user_id") or me["id"]
    print("conta:", me.get("username"))
    manifest = json.loads((ROOT / "docs" / "manifest.json").read_text())
    now = dt.datetime.now(dt.timezone.utc)
    due = [p for p in manifest if p.get("auto", True) and p["id"] not in state["published"]
           and state["failures"].get(p["id"], 0) < 3
           and dt.datetime.fromisoformat(p["publish_at"].replace("Z", "+00:00")) <= now]
    due.sort(key=lambda p: p["publish_at"])
    for p in due:
        late = (now - dt.datetime.fromisoformat(p["publish_at"].replace("Z", "+00:00"))).total_seconds() / 3600
        if late > LATE_H:
            state["published"][p["id"]] = {"skipped": "atrasado", "at": now.isoformat()}; print("pulado (atrasado):", p["id"]); continue
        try:
            mid = publish(ig, p)
            state["published"][p["id"]] = {"media_id": mid, "at": now.isoformat()}; print("publicado:", p["id"], mid)
            break   # um por execução
        except Exception as e:
            state["failures"][p["id"]] = state["failures"].get(p["id"], 0) + 1
            print("ERRO:", p["id"], e, file=sys.stderr)
            STATE.write_text(json.dumps(state, indent=1)); sys.exit(1)
    if not due: print("nada pra publicar agora")
    STATE.write_text(json.dumps(state, indent=1))

if __name__ == "__main__":
    main()
