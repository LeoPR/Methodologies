#!/usr/bin/env python3
"""
fim_latency.py — Estágio 4 / C1: latência de autocomplete (FIM) do modelo local.

Mede a latência model-side de um completion fill-in-the-middle (o que o
Continue.dev envia ao Ollama no autocomplete), via /api/generate com `suffix`.
Isola a latência do MODELO da camada de editor (C2 mede o overhead da extensão).

Métricas (da API, não wall-clock de transporte):
  TTFT  ≈ load + prompt_eval_duration  (tempo até começar a gerar — o que pesa no autocomplete)
  total ≈ total_duration               (até a sugestão completa)
Critério do plano (C1): TTFT p50 < 500ms, p90 < 800ms (modelo já residente).

Custo ZERO (local). Uso:
    python fim_latency.py --model qwen2.5-coder:7b --n 12
"""
from __future__ import annotations
import argparse, json, statistics, urllib.request

GEN = "http://localhost:11434/api/generate"

# Cenário realista de autocomplete: completar o corpo de uma função entre prefixo e sufixo.
PREFIX = """def fibonacci(n: int) -> int:
    \"\"\"Return the n-th Fibonacci number (iterative).\"\"\"
    if n < 2:
        return n
    a, b = 0, 1
    """
SUFFIX = """
    return b


def main():
    print(fibonacci(10))
"""


def call(model, num_ctx, num_predict):
    body = {"model": model, "prompt": PREFIX, "suffix": SUFFIX, "stream": False,
            "options": {"temperature": 0, "seed": 7, "num_ctx": num_ctx, "num_predict": num_predict}}
    req = urllib.request.Request(GEN, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def pctl(xs, p):
    xs = sorted(xs)
    k = (len(xs) - 1) * p
    f = int(k)
    return xs[f] if f + 1 >= len(xs) else xs[f] + (k - f) * (xs[f + 1] - xs[f])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen2.5-coder:7b")
    ap.add_argument("--num-ctx", type=int, default=4096)
    ap.add_argument("--num-predict", type=int, default=48, help="tokens de sugestão (autocomplete é curto)")
    ap.add_argument("--n", type=int, default=12)
    a = ap.parse_args()

    print(f"== C1 FIM latency | model={a.model} num_ctx={a.num_ctx} num_predict={a.num_predict} n={a.n}")
    w = call(a.model, a.num_ctx, a.num_predict)
    print(f"warm-up: load={w.get('load_duration',0)/1e6:.0f}ms (descartado)")
    ttft, total, outs = [], [], []
    for i in range(a.n):
        r = call(a.model, a.num_ctx, a.num_predict)
        t_ttft = (r.get("prompt_eval_duration", 0)) / 1e6   # ms; modelo residente => load~0
        t_total = (r.get("total_duration", 0) - r.get("load_duration", 0)) / 1e6
        ttft.append(t_ttft); total.append(t_total); outs.append(r.get("eval_count", 0))
    print(f"TTFT (prefill) ms : p50={pctl(ttft,.5):.0f} p90={pctl(ttft,.9):.0f} "
          f"min={min(ttft):.0f} max={max(ttft):.0f}")
    print(f"total (sugestão) ms: p50={pctl(total,.5):.0f} p90={pctl(total,.9):.0f} "
          f"(out mediano {statistics.median(outs):.0f} tok)")
    ok = pctl(ttft, .5) < 500 and pctl(ttft, .9) < 800
    print(f"C1 GATE-4: TTFT p50<500 & p90<800ms? {'SIM' if ok else 'NAO'}")


if __name__ == "__main__":
    main()
