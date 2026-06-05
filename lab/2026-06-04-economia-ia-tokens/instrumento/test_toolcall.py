#!/usr/bin/env python3
"""
test_toolcall.py — GATE-3 / D0.5 (plano-experimental.md, Estágio 3).

Testa se o shim Anthropic-compatível do Ollama (/v1/messages, usado pelo Claude
Code via ANTHROPIC_BASE_URL) emite um bloco tool_use ESTRUTURADO quando recebe
`tools[]`, em vez de devolver a chamada como texto/end_turn.

Pré-requisito lógico do loop agêntico do Claude Code sobre backend local:
  SUCESSO  = response.stop_reason == "tool_use" E content tem {"type":"tool_use",...}
  FALHA    = stop_reason "end_turn" + content só texto (o modelo "fala" a chamada)

Custo ZERO (inferência local). Uso:
    python test_toolcall.py qwen2.5-coder:7b llama3.1:8b qwen3:14b
"""
from __future__ import annotations
import json
import sys
import urllib.request

ENDPOINT = "http://localhost:11434/v1/messages"

TOOLS = [{
    "name": "get_weather",
    "description": "Get the current weather for a given city. Always use this tool when asked about weather.",
    "input_schema": {
        "type": "object",
        "properties": {"city": {"type": "string", "description": "City name"}},
        "required": ["city"],
    },
}]

PROMPT = "What is the current weather in Paris? Use the get_weather tool to find out."


def call(model: str):
    body = {
        "model": model,
        "max_tokens": 512,
        "messages": [{"role": "user", "content": PROMPT}],
        "tools": TOOLS,
        "stream": False,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "anthropic-version": "2023-06-01"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode("utf-8", "replace") or "{}")
    except Exception as e:  # noqa
        return None, {"error": str(e)}


def verdict(resp: dict):
    if "error" in resp and "stop_reason" not in resp:
        return "ERRO", resp.get("error", "")[:140]
    stop = resp.get("stop_reason")
    content = resp.get("content")
    has_tooluse = isinstance(content, list) and any(
        isinstance(b, dict) and b.get("type") == "tool_use" for b in content
    )
    if stop == "tool_use" and has_tooluse:
        tu = next(b for b in content if b.get("type") == "tool_use")
        return "PASS", f"tool_use estruturado: name={tu.get('name')} input={tu.get('input')}"
    # falha: descreve o que veio
    text = ""
    if isinstance(content, list):
        text = " ".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    elif isinstance(content, str):
        text = content
    return "FAIL", f"stop_reason={stop!r} has_tool_use={has_tooluse} | texto: {text[:160]!r}"


def main(argv):
    models = argv or ["qwen2.5-coder:7b"]
    print(f"== GATE-3 / D0.5 — tool_use no shim /v1/messages do Ollama ==")
    print(f"endpoint: {ENDPOINT}\n")
    results = {}
    for m in models:
        status, resp = call(m)
        v, detail = verdict(resp)
        results[m] = v
        print(f"[{v}] {m}  (HTTP {status})")
        print(f"      {detail}")
        # dump estrutura crua resumida
        if isinstance(resp, dict) and "content" in resp:
            types = [b.get("type") for b in resp["content"]] if isinstance(resp["content"], list) else type(resp["content"]).__name__
            print(f"      content types={types} stop_reason={resp.get('stop_reason')!r} model={resp.get('model')!r}")
        print()
    npass = sum(1 for v in results.values() if v == "PASS")
    print(f"-- GATE-3: {npass}/{len(results)} modelos emitem tool_use estruturado --")
    if npass == 0:
        print("   => RAMO AGÊNTICO-LOCAL (D1/E4) INVIÁVEL POR PROTOCOLO. Nenhum token pago será gasto.")
    else:
        print("   => Ramo agêntico-local POSSÍVEL nos modelos PASS. Prosseguir só com eles.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
