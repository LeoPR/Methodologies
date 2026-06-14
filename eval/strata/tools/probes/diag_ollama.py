#!/usr/bin/env python3
"""Diagnostico: como o Ollama /api/chat retorna saida de modelo THINKING?
Verifica se 'thinking' vem em campo separado de 'content', e o done_reason."""
import json
import urllib.request

OLLAMA = "http://localhost:11434/api/chat"
PROMPT = "Liste 3 forças de um projeto bem documentado e diga qual a mais importante. Seja breve."


def call(model, think=None, num_predict=1200):
    body = {"model": model, "messages": [{"role": "user", "content": PROMPT}],
            "stream": False, "options": {"num_predict": num_predict, "temperature": 0.3}}
    if think is not None:
        body["think"] = think
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode())


for model, think in [("deepseek-r1:8b", None), ("deepseek-r1:8b", True), ("qwen3:8b", True)]:
    print(f"\n===== {model} (think={think}) =====")
    try:
        d = call(model, think)
        msg = d.get("message", {})
        print("  top-level keys:", list(d.keys()))
        print("  message keys  :", list(msg.keys()))
        print("  done_reason   :", d.get("done_reason"), "| eval_count:", d.get("eval_count"))
        print("  len(content)  :", len(msg.get("content", "")))
        print("  len(thinking) :", len(msg.get("thinking", "") or ""))
        print("  content[:120] :", repr(msg.get("content", "")[:120]))
        print("  thinking[:100]:", repr((msg.get("thinking", "") or "")[:100]))
    except Exception as e:  # noqa
        print("  ERRO:", e)
