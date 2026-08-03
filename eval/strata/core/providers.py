#!/usr/bin/env python3
"""providers.py — camada compartilhada de provedores OpenAI-compativel (nuvem). ADITIVO.

Suporta openrouter, cerebras, groq, nvidia (NIM). Le a chave de env OU do arquivo
gitignored eval/strata/.<prov>-key. Embute o User-Agent de browser porque Cerebras e
Groq bloqueiam o urllib padrao com HTTP 403 (Cloudflare code 1010). Retry em 429/5xx.

Spec de modelo: 'provider:model' (ex.: 'cerebras:gpt-oss-120b'). Sem provider conhecido,
assume 'openrouter' (retrocompat com specs antigos tipo 'google/gemini-2.5-flash').

Nao substitui call_ollama/call_openrouter do hb_runner (aquilo ja roda); esta camada e a
via unica dos provedores diretos novos e do juri configuravel.
"""
from __future__ import annotations
import json
import os
import re
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# provider -> (endpoint chat, env-var da chave, arquivo gitignored da chave)
PROVIDERS = {
    "openrouter": ("https://openrouter.ai/api/v1/chat/completions", "OPENROUTER_API_KEY", ".openrouter-key"),
    "cerebras":   ("https://api.cerebras.ai/v1/chat/completions", "CEREBRAS_API_KEY", ".cerebras-key"),
    "groq":       ("https://api.groq.com/openai/v1/chat/completions", "GROQ_API_KEY", ".groq-key"),
    "nvidia":     ("https://integrate.api.nvidia.com/v1/chat/completions", "NVIDIA_API_KEY", ".nvidia-key"),
}


def parse_spec(spec):
    """'cerebras:gpt-oss-120b' -> ('cerebras','gpt-oss-120b'). Sem provider conhecido -> openrouter."""
    if ":" in spec:
        head, tail = spec.split(":", 1)
        if head in PROVIDERS:
            return head, tail
    return "openrouter", spec


def get_key(provider):
    _, env, fname = PROVIDERS[provider]
    k = os.environ.get(env)
    if not k:
        fp = os.path.join(HERE, fname)
        if os.path.exists(fp):
            with open(fp, encoding="utf-8") as f:
                k = f.read().strip()
    return k


def have_key(provider):
    return bool(get_key(provider))


def _headers(provider, key):
    h = {"Content-Type": "application/json", "Authorization": f"Bearer {key}",
         "User-Agent": _UA, "Accept": "application/json"}
    if provider == "openrouter":
        h["HTTP-Referer"] = "https://github.com/LeoPR/Methodologies"
        h["X-Title"] = "Strata-eval"
    return h


def chat(provider, model, prompt, *, max_tokens=800, temperature=0.0, seed=None,
         response_format=None, reasoning=None, timeout=300, retries=4):
    """Chamada OpenAI-compativel generica com retry (429/5xx). Retorna o dict cru da API."""
    key = get_key(provider)
    if not key:
        _, env, fname = PROVIDERS[provider]
        raise RuntimeError(f"chave do provedor '{provider}' ausente (env {env} ou eval/strata/{fname})")
    body = {"model": model, "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens, "temperature": temperature}
    if seed is not None:
        body["seed"] = seed
    if response_format is not None:
        body["response_format"] = response_format
    if reasoning is not None:
        body["reasoning"] = reasoning
    data = json.dumps(body).encode("utf-8")
    url, _, _ = PROVIDERS[provider]
    hdr = _headers(provider, key)
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=hdr), timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 529) and attempt < retries - 1:
                time.sleep(5 * (attempt + 1)); continue
            raise
        except Exception as e:  # noqa
            last = e
            if attempt < retries - 1:
                time.sleep(3 * (attempt + 1)); continue
            raise
    raise last


def chat_tools(provider, model, messages, tools, *, max_tokens=6000, temperature=None,
               seed=None, timeout=300, retries=4):
    """Chamada OpenAI-compativel COM tool-calling nativo (DEGRAU 3 — hb_agent). ADITIVO.

    `messages` e' a conversa INTEIRA (system + user + assistant c/ tool_calls + tool results);
    `tools` e' a lista de function-schemas. Retorna o dict cru da API. Pede `usage.include`
    (OpenRouter devolve `usage.cost` em dolares — base do rastro de custo por run).

    Prompt caching: p/ modelos anthropic/* marca breakpoints `cache_control` ephemeral no
    system e na ultima tool def (a OpenRouter repassa ao provedor; o system do hb_agent e'
    ~17k tok e se repete a cada turn do loop — sem cache o custo explode). Nos demais
    provedores o caching e' automatico ou inexistente; nada se envia (param anthropic-
    especifico poderia dar 400). `temperature`/`seed` = None omitem o parametro (gpt-5-*
    rejeita temperature; claude nao tem seed — ver supported_parameters do /models)."""
    key = get_key(provider)
    if not key:
        _, env, fname = PROVIDERS[provider]
        raise RuntimeError(f"chave do provedor '{provider}' ausente (env {env} ou eval/strata/{fname})")
    body = {"model": model, "messages": messages, "tools": tools,
            "max_tokens": max_tokens, "usage": {"include": True}}
    if temperature is not None:
        body["temperature"] = temperature
    if seed is not None:
        body["seed"] = seed
    if model.startswith("anthropic/"):
        msgs = [dict(m) for m in messages]
        if msgs and msgs[0].get("role") == "system" and isinstance(msgs[0].get("content"), str):
            msgs[0]["content"] = [{"type": "text", "text": msgs[0]["content"],
                                   "cache_control": {"type": "ephemeral"}}]
        tls = [dict(t) for t in tools]
        if tls:
            tls[-1]["cache_control"] = {"type": "ephemeral"}
        body["messages"], body["tools"] = msgs, tls
    data = json.dumps(body).encode("utf-8")
    url, _, _ = PROVIDERS[provider]
    hdr = _headers(provider, key)
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=hdr), timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 529) and attempt < retries - 1:
                time.sleep(5 * (attempt + 1)); continue
            raise
        except Exception as e:  # noqa
            last = e
            if attempt < retries - 1:
                time.sleep(3 * (attempt + 1)); continue
            raise
    raise last


def tool_msg_of(d):
    """Extrai da resposta de chat_tools: (content, tool_calls, finish_reason, usage).
    tool_calls vem como lista de dicts {id, name, arguments(str JSON)}; usage inclui
    prompt_tokens/completion_tokens e cost (se a OpenRouter devolveu)."""
    ch = d["choices"][0]
    msg = ch.get("message", {})
    raw = msg.get("content")
    if isinstance(raw, list):  # blocos (anthropic): junta os de texto
        content = "".join(b.get("text", "") for b in raw if isinstance(b, dict)).strip()
    else:
        content = (raw or "").strip()
    tcs = []
    for tc in (msg.get("tool_calls") or []):
        fn = tc.get("function", {}) or {}
        tcs.append({"id": tc.get("id"), "name": fn.get("name", ""),
                    "arguments": fn.get("arguments", "") or ""})
    u = d.get("usage", {}) or {}
    usage = {"prompt_tokens": u.get("prompt_tokens", 0),
             "completion_tokens": u.get("completion_tokens", 0),
             "cost": u.get("cost")}
    return content, tcs, ch.get("finish_reason"), usage


def content_of(d):
    """(content, finish_reason, from_thinking, completion_tokens). Fallback p/ o canal de raciocinio."""
    ch = d["choices"][0]
    msg = ch.get("message", {})
    content = (msg.get("content") or "").strip()
    from_thinking = False
    if not content:  # reasoner: resposta foi p/ o canal de raciocinio
        content = (msg.get("reasoning") or msg.get("reasoning_content") or msg.get("thinking") or "").strip()
        from_thinking = bool(content)
    return content, ch.get("finish_reason"), from_thinking, d.get("usage", {}).get("completion_tokens", 0)


def _extract_json(raw):
    """Robusto a reasoners: remove blocos <think>...</think> embutidos no content
    (groq/qwen sem reasoning_format) e devolve o 1o objeto JSON parseavel do texto
    (raw_decode), em vez do slice ingenuo 1o'{'..ultimo'}' — que quebrava com
    'Extra data' quando o thinking citava o schema ou o modelo emitia 2 JSONs."""
    raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL)
    dec = json.JSONDecoder()
    for m in re.finditer(r"\{", raw):
        try:
            obj, _ = dec.raw_decode(raw, m.start())
        except Exception:  # noqa — nao era inicio de objeto valido; proximo '{'
            continue
        if isinstance(obj, dict) and obj:
            return obj
    raise ValueError("sem objeto JSON na resposta")


def harden_schema(schema):
    """Deixa um JSON Schema conforme os modos ESTRITOS dos provedores. Aplica, recursivamente:
      - `additionalProperties: false` em TODO objeto (exigencia do Cerebras desde 2026-07-21;
        schema nao-conforme -> HTTP 422);
      - TODAS as propriedades em `required` (exigencia do Groq no strict mode).
    Aplicar as duas e' o denominador comum portavel — inofensivo em quem nao exige.
    Nao muta a entrada."""
    if not isinstance(schema, dict):
        return schema
    out = dict(schema)
    props = out.get("properties")
    if isinstance(props, dict):
        out["properties"] = {k: harden_schema(v) for k, v in props.items()}
        out["additionalProperties"] = False
        out["required"] = list(props.keys())
    if isinstance(out.get("items"), dict):
        out["items"] = harden_schema(out["items"])
    for key in ("anyOf", "oneOf", "allOf"):
        if isinstance(out.get(key), list):
            out[key] = [harden_schema(s) for s in out[key]]
    return out


def judge_json(spec, prompt, *, schema=None, max_tokens=700, timeout=120):
    """Roda um JUIZ (spec 'provider:model') e devolve o dict do veredito.

    Com `schema`, tenta primeiro o modo json_schema ESTRITO: a decodificacao restrita torna
    IMPOSSIVEL o modelo emitir fora do schema — mata de raiz as falhas observadas no smoke-test
    (copiar o placeholder do enum, campo faltando, prosa em volta do JSON). Escada de fallback:
    estrito -> json_object -> texto puro, porque nem todo provedor/modelo aceita cada modo.
    Embute o User-Agent (Cloudflare) e o retry de 429/5xx via chat()."""
    provider, model = parse_spec(spec)

    formats = []
    if schema is not None:
        formats.append({"type": "json_schema",
                        "json_schema": {"name": "verdict", "strict": True,
                                        "schema": harden_schema(schema)}})
    formats.append({"type": "json_object"})
    formats.append(None)  # sem response_format

    for rf in formats:
        try:
            d = chat(provider, model, prompt, max_tokens=max_tokens, temperature=0.0,
                     response_format=rf, timeout=timeout)
        except urllib.error.HTTPError as e:
            if e.code in (400, 415, 422):
                continue  # provedor/modelo recusa este response_format -> proximo da escada
            raise
        content, _, _, _ = content_of(d)
        try:
            return _extract_json(content)
        except Exception:  # noqa — resposta nao parseou; tenta o proximo modo
            continue

    # ultimo recurso: pedir explicitamente "so o objeto JSON", sem response_format
    prompt2 = prompt + "\n\nResponda ESTRITAMENTE apenas com o objeto JSON, sem nenhum texto fora dele."
    d = chat(provider, model, prompt2, max_tokens=max_tokens, temperature=0.0, timeout=timeout)
    content, _, _, _ = content_of(d)
    return _extract_json(content)
