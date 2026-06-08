#!/usr/bin/env python3
"""Busca preço (in/out $/M tokens) + contexto dos modelos candidatos do P6 Fase B no OpenRouter.
Valida IDs e dá o eixo X (custo) do scatterplot. Saida: planos/p6-pricing.json"""
import json
import os
import urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
HERE = os.path.dirname(os.path.abspath(__file__))
req = urllib.request.Request("https://openrouter.ai/api/v1/models",
                             headers={"Authorization": "Bearer " + KEY})
data = json.loads(urllib.request.urlopen(req, timeout=60).read())["data"]
idx = {m["id"]: m for m in data}

CANDS = [
    "openai/gpt-4.1-mini", "openai/gpt-4.1-nano", "google/gemini-2.5-flash",
    "google/gemini-2.0-flash-001", "google/gemini-2.5-flash-lite",
    "deepseek/deepseek-chat-v3-0324", "meta-llama/llama-3.3-70b-instruct",
    "meta-llama/llama-3.1-8b-instruct", "qwen/qwen-2.5-72b-instruct",
    "mistralai/mistral-small-3.2-24b-instruct", "deepseek/deepseek-r1",
    "qwen/qwq-32b", "openai/o4-mini", "x-ai/grok-3-mini-beta",
    "anthropic/claude-opus-4.8",
]
out = {}
print(f"{'model':44} {'in$/M':>8} {'out$/M':>8}  ctx")
for c in CANDS:
    m = idx.get(c)
    if not m:
        print(f"{c:44} {'--AUSENTE--':>18}")
        continue
    p = m.get("pricing", {})
    pin = float(p.get("prompt", 0)) * 1e6
    pout = float(p.get("completion", 0)) * 1e6
    out[c] = {"in": pin, "out": pout, "ctx": m.get("context_length")}
    print(f"{c:44} {pin:>8.3f} {pout:>8.3f}  {m.get('context_length','?')}")
json.dump(out, open(os.path.join(HERE, "planos", "p6-pricing.json"), "w", encoding="utf-8"), indent=2)
print(f"\n-> planos/p6-pricing.json ({len(out)} validos)")
