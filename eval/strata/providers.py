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
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
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
    i, j = raw.find("{"), raw.rfind("}")
    if i < 0 or j <= i:
        raise ValueError("sem objeto JSON na resposta")
    return json.loads(raw[i:j + 1])


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
