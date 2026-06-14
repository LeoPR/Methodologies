#!/usr/bin/env python3
"""Smoke test da OpenRouter: credito, modelos disponiveis (filtrados) e 1 chamada barata.
Le a key de OPENROUTER_API_KEY. Nao contem segredo."""
import json
import os
import sys
import urllib.request

KEY = os.environ.get("OPENROUTER_API_KEY")
if not KEY:
    print("OPENROUTER_API_KEY nao setada", file=sys.stderr); sys.exit(2)
H = {"Authorization": f"Bearer {KEY}", "HTTP-Referer": "https://github.com/LeoPR/Methodologies", "X-Title": "Strata-eval"}


def get(url):
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=60).read())


# 1) credito
try:
    k = get("https://openrouter.ai/api/v1/key").get("data", {})
    print(f"KEY: limit={k.get('limit')} usage={k.get('usage')} limit_remaining={k.get('limit_remaining')} free_tier={k.get('is_free_tier')}")
except Exception as e:
    print(f"KEY check falhou: {e}")

# 2) modelos disponiveis (filtra os sabores-alvo)
WANT = ["gpt-4.1", "gpt-4o-mini", "gpt-5", "o4-mini", "claude-3.5-haiku", "claude-3.5-sonnet",
        "claude-3-haiku", "gemini-flash", "gemini-2.0-flash", "gemini-2.5-flash",
        "llama-3.1-8b", "llama-3.3-70b", "deepseek-chat", "deepseek/deepseek-r1",
        "mistral-small", "mistral-nemo", "qwen-2.5"]
try:
    models = get("https://openrouter.ai/api/v1/models").get("data", [])
    ids = sorted(m["id"] for m in models)
    print(f"\nMODELOS total: {len(ids)}")
    print("ALVOS disponiveis:")
    for w in WANT:
        hits = [i for i in ids if w in i]
        if hits:
            print(f"  [{w}] -> {hits[:3]}")
except Exception as e:
    print(f"models falhou: {e}")

# 3) chamada barata de teste
try:
    body = json.dumps({"model": "openai/gpt-4o-mini", "messages": [{"role": "user", "content": "responda só: OK"}], "max_tokens": 5}).encode()
    d = json.loads(urllib.request.urlopen(urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body, headers={**H, "Content-Type": "application/json"}), timeout=60).read())
    print(f"\nSMOKE gpt-4o-mini -> {d['choices'][0]['message']['content']!r} (usage={d.get('usage')})")
except Exception as e:
    print(f"\nSMOKE falhou: {e}")
