#!/usr/bin/env python3
"""fit_encaixe.py — Estagio 5: encaixe de modelo por placa, a partir de poucos pontos medidos.

Mede, no hardware real, quanto cada modelo ocupa (ollama /api/ps: size e size_vram) em dois
tamanhos de contexto e a velocidade de decode (eval_count/eval_duration, como o bench_decode.py).
Com os dois pontos por modelo, ajusta a reta  memoria(ctx) = base + kv_por_token * ctx
(o KV cresce linear com o contexto: Achado 1 do STAGE2). A velocidade de decode batch-1 e
limitada pela banda de memoria (mapa-recursos-llm: "velocidade nao e primitiva"), entao
calibra-se  tps = eficiencia * banda / bytes_ativos  nos pontos que cabem inteiros na GPU e
extrapola-se para outras placas pela banda de cada uma.

Custo zero (100% local). Descarrega o modelo entre medicoes (keep_alive=0).
Uso:
  python fit_encaixe.py --models qwen3:8b gemma4:12b --ctx 8192 32768 --out encaixe_pontos.json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import time
import urllib.error
import urllib.request

API = "http://localhost:11434/api"
PROMPT = ("Explain, in about 150 words, why a canonical single source of truth reduces drift in a "
          "long-lived research project.")


def post(path, body, timeout=1800):
    req = urllib.request.Request(f"{API}/{path}", data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def get(path):
    with urllib.request.urlopen(f"{API}/{path}", timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def nvidia_used_mib():
    try:
        out = subprocess.run(["nvidia-smi", "--query-gpu=memory.used,memory.total",
                              "--format=csv,noheader,nounits"], capture_output=True, text=True).stdout
        used, total = [int(x) for x in out.strip().split(",")[:2]]
        return used, total
    except Exception:  # noqa
        return None, None


def unload(model):
    try:
        post("generate", {"model": model, "keep_alive": 0}, timeout=120)
    except Exception:  # noqa
        pass
    time.sleep(3)


def arch_info(model):
    s = post("show", {"model": model}, timeout=60)
    mi = s.get("model_info", {}) or {}
    arch = mi.get("general.architecture", "")
    g = lambda k: mi.get(f"{arch}.{k}")  # noqa: E731
    return {"arch": arch, "params": mi.get("general.parameter_count"),
            "layers": g("block_count"), "kv_heads": g("attention.head_count_kv"),
            "heads": g("attention.head_count"), "key_len": g("attention.key_length"),
            "embed": g("embedding_length"), "ctx_max": g("context_length"),
            "experts": g("expert_count"), "experts_used": g("expert_used_count"),
            "quant": (s.get("details") or {}).get("quantization_level")}


def measure(model, ctx, think_off=True):
    unload(model)
    base_used, total = nvidia_used_mib()
    body = {"model": model, "prompt": PROMPT, "stream": False, "keep_alive": "2m",
            "options": {"num_ctx": ctx, "num_predict": 200, "temperature": 0, "seed": 42}}
    if think_off:
        body["think"] = False
    t0 = time.time()
    try:
        d = post("generate", body)
    except urllib.error.HTTPError as e:
        if e.code == 400 and "think" in body:
            body.pop("think")
            d = post("generate", body)
        else:
            raise
    wall = time.time() - t0
    ps = [m for m in get("ps").get("models", []) if m.get("name") == model or m.get("model") == model]
    used, _ = nvidia_used_mib()
    size = ps[0]["size"] if ps else None
    size_vram = ps[0]["size_vram"] if ps else None
    ev, evd = d.get("eval_count", 0), d.get("eval_duration", 0)
    pev, pevd = d.get("prompt_eval_count", 0), d.get("prompt_eval_duration", 0)
    return {"model": model, "num_ctx": ctx, "size_gb": round(size / 1e9, 3) if size else None,
            "size_vram_gb": round(size_vram / 1e9, 3) if size_vram else None,
            "offload": (size is not None and size_vram is not None and size_vram < size),
            "decode_tps": round(ev / (evd / 1e9), 2) if evd else None,
            "prefill_tps": round(pev / (pevd / 1e9), 1) if pevd else None,
            "wall_s": round(wall, 1), "gpu_used_before_mib": base_used, "gpu_used_after_mib": used,
            "gpu_total_mib": total}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--ctx", nargs="+", type=int, default=[8192, 32768])
    ap.add_argument("--out", default="encaixe_pontos.json")
    a = ap.parse_args()
    tags = {m["name"]: m["size"] for m in get("tags").get("models", [])}
    out = []
    for m in a.models:
        info = arch_info(m)
        info["file_gb"] = round(tags.get(m, 0) / 1e9, 3)
        pts = []
        for c in a.ctx:
            p = measure(m, c)
            pts.append(p)
            print(json.dumps(p), flush=True)
        unload(m)
        out.append({"model": m, "arch": info, "points": pts})
        json.dump(out, open(a.out, "w", encoding="utf-8"), indent=1)
    print("== fim:", a.out)


if __name__ == "__main__":
    main()
