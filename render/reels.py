"""Monta os Reels a partir dos cards (build/reels/<id>/NN.png).
Corte a cada ~2,8 s (84 frames a 30 fps), no passo lento da intro de Happy Nation.
Áudio: faixa muda. A música entra pelo app do Instagram.
"""
import sys, subprocess, pathlib, random
import numpy as np
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "content"))
import content as C

FPS, OW, OH = 30, 1080, 1920
BEAT = 84            # frames por card
OUT = ROOT / "docs" / "reels"

def ease(t): return 1 - (1 - t) ** 3

def frames_for(card, fast):
    if card["t"] == "title": return 96
    if card["t"] == "exit": return 120
    if fast: return 42
    return BEAT

MUSICA = ROOT / "assets" / "audio" / "happy-nation.mp3"

def render(reel):
    total = sum(frames_for(c, reel.get("fast", False)) for c in reel["cards"]) / FPS
    global AUDIO_IN, AUDIO_FX
    if MUSICA.exists():
        AUDIO_IN = ["-i", str(MUSICA)]
        AUDIO_FX = ["-af", f"afade=t=out:st={max(total-1.5,0):.2f}:d=1.5"]
    else:
        AUDIO_IN = ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]; AUDIO_FX = []
    d = ROOT / "build" / "reels" / reel["id"]
    fast = reel.get("fast", False)
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{reel['id']}.mp4"
    rng = np.random.default_rng(4)
    grains = [rng.normal(0, 5, (OH, OW, 1)).astype(np.int16) for _ in range(6)]
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{OW}x{OH}", "-r", str(FPS), "-i", "-",
           *AUDIO_IN, "-shortest",
           "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-maxrate", "9M", "-bufsize", "18M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", *AUDIO_FX, "-movflags", "+faststart", str(out)]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    r = random.Random(1); gi = 0
    for i, card in enumerate(reel["cards"]):
        full = Image.open(d / f"{i:02d}.png").convert("RGB")
        pre = Image.open(d / f"{i:02d}_pre.png").convert("RGB") if (d / f"{i:02d}_pre.png").exists() else None
        SW, SH = full.size
        n = frames_for(card, fast)
        stamp_at = n // 2 - 6 if not fast else n // 3
        is_clip = card["t"] == "clip"
        for f in range(n):
            src = pre if (pre is not None and f < stamp_at) else full
            # zoom: slam nos primeiros frames, depois push lento
            z = 1.0 + 0.045 * (f / n)
            if f < 7 and card["t"] != "exit": z += 0.12 * (1 - ease(f / 7))
            sh = 0.0
            if f < 6: sh = 14 * (1 - f / 6)
            if pre is not None and stamp_at <= f < stamp_at + 6:
                k = (f - stamp_at) / 6; z += 0.03 * (1 - ease(k)); sh = max(sh, 16 * (1 - k))
            cw, ch = SW / z, SH / z
            cx = min(max(SW / 2 + r.uniform(-sh, sh), cw / 2), SW - cw / 2)
            cy = min(max(SH / 2 + r.uniform(-sh, sh), ch / 2), SH - ch / 2)
            box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
            im = src.resize((OW, OH), Image.BILINEAR, box=box)
            a = np.asarray(im, dtype=np.int16)
            a = a + grains[(gi // 2) % 6]; gi += 1
            if is_clip and f < 3: a = a + int((0.42, 0.22, 0.08)[f] * 255)
            if pre is not None and f == stamp_at: a = a + 40
            ff.stdin.write(np.clip(a, 0, 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait()
    return out

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for reel in C.REELS:
        if only and reel["id"] not in only: continue
        o = render(reel); print("ok", o.name)
