#!/usr/bin/env python3
"""
bench_decode.py — instrumento do Estágio 2 (B1): throughput de DECODE de compute.

Mede tokens/s de geração usando os campos de timing da própria API do Ollama
(eval_count / eval_duration), NÃO wall-clock — wall-clock inclui load_duration,
fila e overhead de transporte, que contaminam a medição (exigência da verificação
adversarial do plano).

decode_tps   = eval_count / (eval_duration / 1e9)        # geração (o que importa)
prefill_tps  = prompt_eval_count / (prompt_eval_duration / 1e9)  # TTFT-bound

Faz 1 chamada de warm-up (carrega o modelo; descartada) + N medições. Reporta
mediana, IQR, min/max. temperature=0 e seed fixo para reduzir variância.

NÃO custa tokens pagos (inferência 100% local). Uso:
    python bench_decode.py --model qwen2.5-coder:7b --num-ctx 4096 --n 7
"""
from __future__ import annotations
import argparse
import json
import statistics
import urllib.request

OLLAMA = "http://localhost:11434/api/generate"

DEFAULT_PROMPT = (
    "Write a Python function `merge_sort(arr)` that implements merge sort "
    "recursively, with a docstring and inline comments explaining each step. "
    "Then write three asserts testing it."
)


def call(model: str, prompt: str, num_ctx: int, num_predict: int):
    body = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "seed": 42,
            "num_ctx": num_ctx,
            "num_predict": num_predict,
        },
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(OLLAMA, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read().decode("utf-8"))


def metrics(resp: dict):
    ec = resp.get("eval_count", 0) or 0
    ed = resp.get("eval_duration", 0) or 0
    pc = resp.get("prompt_eval_count", 0) or 0
    pd = resp.get("prompt_eval_duration", 0) or 0
    ld = resp.get("load_duration", 0) or 0
    return {
        "decode_tps": (ec / (ed / 1e9)) if ed else 0.0,
        "prefill_tps": (pc / (pd / 1e9)) if pd else 0.0,
        "eval_count": ec,
        "prompt_eval_count": pc,
        "load_ms": ld / 1e6,
    }


def iqr(xs):
    if len(xs) < 2:
        return 0.0
    qs = statistics.quantiles(xs, n=4, method="inclusive")
    return qs[2] - qs[0]  # Q3 - Q1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--num-ctx", type=int, default=4096)
    ap.add_argument("--num-predict", type=int, default=256)
    ap.add_argument("--n", type=int, default=7, help="medições (além do warm-up)")
    ap.add_argument("--prompt", default=DEFAULT_PROMPT)
    args = ap.parse_args(argv)

    print(f"== bench_decode | model={args.model} num_ctx={args.num_ctx} "
          f"num_predict={args.num_predict} n={args.n}")
    print("warm-up (carrega modelo, descartado)...", flush=True)
    w = call(args.model, args.prompt, args.num_ctx, args.num_predict)
    wm = metrics(w)
    print(f"  warm-up: load={wm['load_ms']:.0f}ms decode={wm['decode_tps']:.1f} t/s "
          f"(out {wm['eval_count']} tok)")

    decode, prefill = [], []
    for i in range(args.n):
        m = metrics(call(args.model, args.prompt, args.num_ctx, args.num_predict))
        decode.append(m["decode_tps"])
        prefill.append(m["prefill_tps"])
        print(f"  run {i+1}: decode={m['decode_tps']:.2f} t/s | "
              f"prefill={m['prefill_tps']:.1f} t/s | out={m['eval_count']} | "
              f"load={m['load_ms']:.0f}ms")

    med = statistics.median(decode)
    _iqr = iqr(decode)
    print("-- DECODE (compute) --")
    print(f"  mediana: {med:.2f} t/s | IQR: {_iqr:.2f} ({100*_iqr/med:.1f}% da mediana) "
          f"| min {min(decode):.2f} | max {max(decode):.2f}")
    print(f"  prefill mediana: {statistics.median(prefill):.0f} t/s")
    print(f"  GATE-2 B1: mediana>=40 t/s? {'SIM' if med>=40 else 'NAO'} | "
          f"IQR<15%? {'SIM' if (100*_iqr/med)<15 else 'NAO'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
