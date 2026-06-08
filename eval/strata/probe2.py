#!/usr/bin/env python3
"""Lista modelos :free e valida os FORTES (nao-Opus) no OpenRouter, com preco."""
import json
import os
import urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
data = json.loads(urllib.request.urlopen(urllib.request.Request(
    "https://openrouter.ai/api/v1/models", headers={"Authorization": "Bearer " + KEY}), timeout=60).read())["data"]
idx = {m["id"]: m for m in data}

free = sorted(m["id"] for m in data if m["id"].endswith(":free"))
keep = [f for f in free if any(k in f for k in ["deepseek", "llama-3", "qwen", "gemini", "mistral", "glm", "nemotron", "gpt-oss", "kimi"])]
print(f"FREE (:free) relevantes: {len(keep)}/{len(free)}")
for f in keep:
    print("  ", f)

strong = ["anthropic/claude-sonnet-4.5", "anthropic/claude-sonnet-4", "google/gemini-2.5-pro",
          "openai/gpt-4.1", "openai/gpt-5", "x-ai/grok-4", "deepseek/deepseek-r1",
          "qwen/qwen3-235b-a22b", "moonshotai/kimi-k2", "z-ai/glm-4.6"]
print("\nFORTES (nao-Opus) — in/out $/M:")
for s in strong:
    m = idx.get(s)
    if not m:
        print(f"  {s:36} AUSENTE")
        continue
    p = m.get("pricing", {})
    print(f"  {s:36} {float(p.get('prompt', 0))*1e6:>7.2f} {float(p.get('completion', 0))*1e6:>7.2f}")
