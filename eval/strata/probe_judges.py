#!/usr/bin/env python3
"""Lista candidatos a JUIZ forte (nao-Claude) no OpenRouter, com preco."""
import json
import os
import urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
data = json.loads(urllib.request.urlopen(urllib.request.Request(
    "https://openrouter.ai/api/v1/models", headers={"Authorization": "Bearer " + KEY}), timeout=60).read())["data"]
idx = {m["id"]: m for m in data}

CANDS = [
    # OpenAI fortes
    "openai/gpt-5", "openai/gpt-5.5", "openai/gpt-5-pro", "openai/o3", "openai/o3-pro",
    "openai/o4-mini", "openai/gpt-4.1",
    # Google fortes
    "google/gemini-2.5-pro", "google/gemini-2.5-pro-preview", "google/gemini-2.0-pro-exp",
    # outros fortes nao-Claude (referencia)
    "x-ai/grok-4", "deepseek/deepseek-r1", "qwen/qwen3-235b-a22b", "moonshotai/kimi-k2",
]
print(f"{'modelo':34} {'in$/M':>8} {'out$/M':>8}  ctx")
avail = []
for c in CANDS:
    m = idx.get(c)
    if not m:
        print(f"{c:34} {'-- ausente --':>18}")
        continue
    p = m.get("pricing", {})
    pin, pout = float(p.get("prompt", 0)) * 1e6, float(p.get("completion", 0)) * 1e6
    print(f"{c:34} {pin:>8.2f} {pout:>8.2f}  {m.get('context_length','?')}")
    avail.append(c)
# tambem: listar QUALQUER gpt-5* e gemini-2.5* presentes
print("\nTodos os openai/gpt-5* e google/gemini-2.5* presentes:")
for mid in sorted(idx):
    if mid.startswith("openai/gpt-5") or mid.startswith("google/gemini-2.5"):
        print("  ", mid)
