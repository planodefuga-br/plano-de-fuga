"""Publica no Instagram o que já passou do horário no docs/manifest.json.

Usa a "API com Login do Facebook" (graph.facebook.com), que permite anexar
música com a Audio API. Estado em publisher/state.json (commitado pelo workflow).

Env:
  IG_TOKEN   token de usuário de longa duração (secret)
  PAGES_URL  ex.: https://planodefuga-br.github.io/plano-de-fuga
  DRY_RUN    "1" = só testa: confere a conta, busca o áudio e grava publisher/teste.json

No manifest, um Reel pode ter:
  "audio": {"busca": "Happy Nation", "volume_audio": 100, "volume_video": 0}
"""
import json, os, sys, time, pathlib, urllib.request, urllib.parse, urllib.error, datetime as dt

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE = ROOT / "publisher" / "state.json"
TESTE = ROOT / "publisher" / "teste.json"
GRAPH = "https://graph.facebook.com/v22.0"
TOKEN = os.environ.get("IG_TOKEN", "")
BASE = os.environ.get("PAGES_URL", "").rstrip("/")
LATE_H = 6
DRY = os.environ.get("DRY_RUN") == "1"
AUDIO_TESTE = os.environ.get("AUDIO_TESTE", "Happy Nation")


def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params)
    url = f"{GRAPH}/{path}"
    if method == "GET":
        req = urllib.request.Request(url + "?" + data)
    else:
        req = urllib.request.Request(url, data=data.encode(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path}: {e.code} {e.read().decode()[:500]}")


def conta_instagram():
    """Acha a conta do Instagram ligada à página do Facebook."""
    pages = call("GET", "me/accounts", fields="name,instagram_business_account{id,username}")
    for p in pages.get("data", []):
        ig = p.get("instagram_business_account")
        if ig:
            return ig["id"], ig.get("username"), p.get("name")
    raise RuntimeError("nenhuma página com Instagram ligado: " + json.dumps(pages)[:300])


def buscar_audio(ig, busca):
    r = call("GET", "ig_audio", audio_type="music", user_id=ig, search_query=busca)
    return r.get("data", [])


def wait_ready(cid, video=False):
    for _ in range(60 if video else 20):
        s = call("GET", cid, fields="status_code").get("status_code")
        if s == "FINISHED":
            return
        if s in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"container {cid}: {s}")
        time.sleep(5 if video else 3)
    raise RuntimeError(f"container {cid} não ficou pronto")


def publish(ig, post):
    if post["type"] == "carousel":
        kids = [call("POST", f"{ig}/media", image_url=f"{BASE}/{m}", is_carousel_item="true")["id"] for m in post["media"]]
        for k in kids:
            wait_ready(k)
        c = call("POST", f"{ig}/media", media_type="CAROUSEL", children=",".join(kids), caption=post["caption"])["id"]
        wait_ready(c)
    elif post["type"] == "reel":
        params = dict(media_type="REELS", video_url=f"{BASE}/{post['media'][0]}", caption=post["caption"], share_to_feed="true")
        a = post.get("audio")
        if a:
            achados = buscar_audio(ig, a["busca"])
            if not achados:
                raise RuntimeError(f"áudio não encontrado: {a['busca']}")
            params["audio_configuration"] = json.dumps({
                "audio_id": achados[0]["audio_id"],
                "audio_volume": a.get("volume_audio", 100),
                "video_volume": a.get("volume_video", 0),
            })
        c = call("POST", f"{ig}/media", **params)["id"]
        wait_ready(c, video=True)
    else:
        raise RuntimeError("tipo desconhecido " + post["type"])
    return call("POST", f"{ig}/media_publish", creation_id=c)["id"]


def teste():
    """Modo só testar: não publica nada, grava o diagnóstico em publisher/teste.json."""
    out = {"quando": dt.datetime.now(dt.timezone.utc).isoformat(), "token_presente": bool(TOKEN)}
    try:
        ig, user, page = conta_instagram()
        out.update(conta=user, pagina=page, ok_conta=True)
        try:
            achados = buscar_audio(ig, AUDIO_TESTE)
            out["audio_busca"] = AUDIO_TESTE
            out["audio_resultados"] = [
                {k: x.get(k) for k in ("audio_id", "title", "display_artist", "duration_in_ms")} for x in achados[:8]
            ]
        except Exception as e:
            out["audio_erro"] = str(e)[:400]
        try:
            lim = call("GET", f"{ig}/content_publishing_limit", fields="quota_usage,config")
            out["limite_publicacao"] = lim.get("data")
        except Exception as e:
            out["limite_erro"] = str(e)[:300]
    except Exception as e:
        out.update(ok_conta=False, erro=str(e)[:500])
    TESTE.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(json.dumps(out, indent=1, ensure_ascii=False))


def main():
    if DRY:
        return teste()
    state = json.loads(STATE.read_text()) if STATE.exists() else {"published": {}, "failures": {}}
    ig, user, _ = conta_instagram()
    print("conta:", user)
    manifest = json.loads((ROOT / "docs" / "manifest.json").read_text())
    now = dt.datetime.now(dt.timezone.utc)
    when = lambda p: dt.datetime.fromisoformat(p["publish_at"].replace("Z", "+00:00"))
    due = [p for p in manifest if p.get("auto", True) and p["id"] not in state["published"]
           and state["failures"].get(p["id"], 0) < 3 and when(p) <= now]
    due.sort(key=lambda p: p["publish_at"])
    for p in due:
        late = (now - when(p)).total_seconds() / 3600
        if late > LATE_H:
            state["published"][p["id"]] = {"skipped": "atrasado", "at": now.isoformat()}
            print("pulado (atrasado):", p["id"])
            continue
        try:
            mid = publish(ig, p)
            state["published"][p["id"]] = {"media_id": mid, "at": now.isoformat()}
            print("publicado:", p["id"], mid)
            break  # um por execução
        except Exception as e:
            state["failures"][p["id"]] = state["failures"].get(p["id"], 0) + 1
            print("ERRO:", p["id"], e, file=sys.stderr)
            STATE.write_text(json.dumps(state, indent=1))
            sys.exit(1)
    if not due:
        print("nada pra publicar agora")
    STATE.write_text(json.dumps(state, indent=1))


if __name__ == "__main__":
    main()
