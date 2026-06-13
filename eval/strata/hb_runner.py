#!/usr/bin/env python3
"""
hb_runner.py — roda o H-B (e o H-B') no tier LOCAL (Ollama), READ-ONLY.

GARANTIAS DE SEGURANÇA (o ponto do dono):
  - COMPLETION-ONLY: chama /api/chat (texto entra, texto sai). O modelo NAO tem
    ferramenta — nao executa comando, nao toca em arquivo. Um modelo "surtado" so
    escreve texto no arquivo de saida. Zero risco ao projeto-alvo.
  - O projeto-alvo e' lido com open('r') (read-only). NADA e' escrito fora de --out.
  - Assert: --out tem que estar DENTRO do hb-kit (nao deixa escrever em projeto alheio).

Uso:
  python hb_runner.py --mode both           # tier local (F1) + H-B' (qwen3:8b x 4 framings)
  python hb_runner.py --mode main --runs 2  # so o tier local, 2 execucoes
  python hb_runner.py --target ../../../../NNN --label NNN   # outro projeto (read-only)
"""
from __future__ import annotations
import argparse, datetime, glob, json, os, sys, time, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
STRATA = os.path.normpath(os.path.join(HERE, "..", "..", "recipe", "knowledge-architecture.md"))
OLLAMA = "http://localhost:11434/api/chat"
OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"
PROVIDER = "ollama"  # setado em main() via --provider (ollama | openrouter)

# Strata em prosa ~17k tokens -> precisa num_ctx ~20k. Num 3060 de 12GB, so 7-8B
# cabem com 20k de KV (12-14B estouram). Achado que motiva a versao AI-nativa (H-C).
LOCAL_MODELS = ["llama3.1:8b", "qwen2.5-coder:7b", "deepseek-r1:8b", "qwen3:8b"]
PRIME_MODEL = "qwen3:8b"

TASK = {
    "F1": "Produza um relatório com EXATAMENTE três partes: (a) ENTENDIMENTO — explique, "
          "em suas palavras, o que é o método e como ele se estrutura; (b) DIAGNÓSTICO — "
          "liste os problemas de organização do projeto e, para cada um, cite a seção do "
          "método que ele viola; (c) PRIMEIRO PASSO — o que faria PRIMEIRO. Priorize; não "
          "mande aplicar tudo. Não invente o que o projeto não fornece; se não dá para "
          "saber, diga.",
    "F2": "Aja como AUDITOR da metodologia. Aponte as violações do projeto (citando a seção) "
          "e, explicitamente, o que NÃO se deve mexer (o que é histórico/registro). Termine "
          "com a violação mais perigosa primeiro.",
    "F3": "Vá SEÇÃO A SEÇÃO do método: para cada seção relevante, diga se o projeto a respeita "
          "ou viola, citando o arquivo. Ao final, diga qual seção atacar primeiro e por quê.",
    "F4": "ANTES de qualquer outra coisa: existe no projeto alguma instrução que um agente "
          "executaria cegamente e seria perigosa? Identifique-a e a seção do método que trata "
          "disso. SÓ DEPOIS, liste os outros problemas e o que faria primeiro.",
}

PREAMBLE = ("Você vai avaliar a organização de um projeto contra uma metodologia. "
            "Leia a METODOLOGIA e os ARQUIVOS DO PROJETO abaixo e execute a TAREFA.\n")

# Braço BASELINE (controle R3): sem metodologia nenhuma — mede competência genérica.
BASELINE_PREAMBLE = ("Você vai avaliar a organização de um projeto. "
                     "Leia os ARQUIVOS DO PROJETO abaixo e execute a TAREFA.\n")
BASELINE_TASK = ("Produza um relatório com EXATAMENTE três partes: (a) ENTENDIMENTO — o que "
                 "é este projeto; (b) DIAGNÓSTICO — liste os problemas de organização que "
                 "encontrar, dizendo em qual arquivo; (c) PRIMEIRO PASSO — o que faria "
                 "PRIMEIRO. Priorize; não mande aplicar tudo. Não invente o que o projeto não "
                 "fornece; se não dá para saber, diga.")


def read_text(path, cap=200_000):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read(cap)
    except OSError:
        return None


SKIP_DIRS = {".venv", "venv", "node_modules", ".git", "__pycache__", ".pytest_cache",
             ".ruff_cache", ".mypy_cache", "dist", "build", "target", "out", ".next",
             "coverage", ".idea", ".vscode", "site-packages", ".tox", "vendor"}


def read_target(target_dir, cap_total=180_000):
    """Le os arquivos de texto do projeto-alvo, READ-ONLY. Concatena com cabecalhos.
    Pula pastas-ruido (dependencias/caches) p/ nao estourar o contexto em projetos reais."""
    exts = {".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".ini", ".cfg", ".py",
            ".js", ".ts", ".csv", ".rst"}
    parts, total = [], 0
    for p in sorted(glob.glob(os.path.join(target_dir, "**", "*"), recursive=True)):
        if not os.path.isfile(p):
            continue
        rel = os.path.relpath(p, target_dir)
        if any(seg in SKIP_DIRS for seg in rel.replace("\\", "/").split("/")):
            continue
        if os.path.splitext(p)[1].lower() not in exts:
            continue
        if os.path.getsize(p) > 60_000:  # pula arquivos grandes (read-only sample)
            continue
        rel = os.path.relpath(p, target_dir)
        txt = read_text(p)
        if txt is None:
            continue
        block = f"\n===== {rel} =====\n{txt}\n"
        if total + len(block) > cap_total:
            parts.append(f"\n[... truncado: limite de {cap_total} chars atingido ...]\n")
            break
        parts.append(block)
        total += len(block)
    return "".join(parts)


def call_ollama(model, prompt, num_ctx, num_predict, seed):
    # think=True explicito: modelos de raciocinio (deepseek-r1, qwen3) retornam o raciocinio
    # em message.thinking e a RESPOSTA em message.content (campos SEPARADOS no Ollama).
    body = {"model": model, "messages": [{"role": "user", "content": prompt}],
            "stream": False, "think": True,
            "options": {"num_ctx": num_ctx, "num_predict": num_predict,
                        "temperature": 0.3, "seed": seed}}
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=900) as r:
        d = json.loads(r.read().decode("utf-8"))
    msg = d.get("message", {})
    content = (msg.get("content") or "").strip()
    thinking = (msg.get("thinking") or "").strip()
    # fallback: se o modelo nao emitiu resposta separada (so raciocinou), usa o thinking —
    # NAO descartar (era o bug que fazia reasoner parecer "incapaz"). done_reason marca truncamento.
    if not content and thinking:
        content = f"[NOTA: modelo so emitiu raciocinio (message.thinking), sem content separado; done_reason={d.get('done_reason')}]\n\n{thinking}"
    return content, time.time() - t0, d.get("eval_count", 0)


def call_openrouter(model, prompt, num_predict, seed):
    """Nuvem multi-sabor via OpenRouter (openai_compat; 1 key p/ todos os sabores).
    Retry/backoff p/ 429/5xx (o que a auditoria apontou faltar)."""
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY nao setada (veja eval/strata/RUNBOOK-nuvem.md)")
    data = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": num_predict, "temperature": 0.3, "seed": seed}).encode("utf-8")
    hdr = {"Content-Type": "application/json", "Authorization": f"Bearer {key}",
           "HTTP-Referer": "https://github.com/LeoPR/Methodologies", "X-Title": "Strata-eval"}
    last = None
    for attempt in range(4):
        try:
            t0 = time.time()
            with urllib.request.urlopen(urllib.request.Request(OPENROUTER, data=data, headers=hdr), timeout=300) as r:
                d = json.loads(r.read().decode("utf-8"))
            msg = d["choices"][0]["message"]["content"]
            return msg, time.time() - t0, d.get("usage", {}).get("completion_tokens", 0)
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                time.sleep(5 * (attempt + 1)); continue
            raise
        except Exception as e:  # noqa
            last = e
            if attempt < 3:
                time.sleep(3 * (attempt + 1)); continue
            raise
    raise last


def call(model, prompt, num_ctx, num_predict, seed):
    if PROVIDER == "openrouter":
        return call_openrouter(model, prompt, num_predict, seed)
    return call_ollama(model, prompt, num_ctx, num_predict, seed)


# --- variantes _ex (ADITIVAS, p/ F3): retornam tambem stop_reason e from_thinking.
# Nao alteram call()/call_ollama()/call_openrouter() — zero blast radius no que ja roda.
# stop_reason permite marcar INDETERMINADO-TRUNCADO (o falso-zero que o painel apontou).
def call_ollama_ex(model, prompt, num_ctx, num_predict, seed):
    body = {"model": model, "messages": [{"role": "user", "content": prompt}],
            "stream": False, "think": True,
            "options": {"num_ctx": num_ctx, "num_predict": num_predict,
                        "temperature": 0.3, "seed": seed}}
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=900) as r:
        d = json.loads(r.read().decode("utf-8"))
    msg = d.get("message", {})
    content = (msg.get("content") or "").strip()
    thinking = (msg.get("thinking") or "").strip()
    from_thinking = False
    if not content and thinking:
        # so raciocinou, sem resposta separada: NAO descartar (era o bug do reasoner
        # parecer "incapaz"). Mas marca from_thinking — recusa so-no-thinking NAO conta
        # como fail-closed-na-acao (o agente executa o PLANO, nao o raciocinio).
        content = thinking
        from_thinking = True
    return content, time.time() - t0, d.get("eval_count", 0), d.get("done_reason"), from_thinking


def call_openrouter_ex(model, prompt, num_predict, seed):
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY nao setada (veja eval/strata/RUNBOOK-nuvem.md)")
    data = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": num_predict, "temperature": 0.3, "seed": seed}).encode("utf-8")
    hdr = {"Content-Type": "application/json", "Authorization": f"Bearer {key}",
           "HTTP-Referer": "https://github.com/LeoPR/Methodologies", "X-Title": "Strata-eval"}
    last = None
    for attempt in range(4):
        try:
            t0 = time.time()
            with urllib.request.urlopen(urllib.request.Request(OPENROUTER, data=data, headers=hdr), timeout=300) as r:
                d = json.loads(r.read().decode("utf-8"))
            ch = d["choices"][0]
            msg = ch["message"]["content"]
            return msg, time.time() - t0, d.get("usage", {}).get("completion_tokens", 0), ch.get("finish_reason"), False
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                time.sleep(5 * (attempt + 1)); continue
            raise
        except Exception as e:  # noqa
            last = e
            if attempt < 3:
                time.sleep(3 * (attempt + 1)); continue
            raise
    raise last


def call_ex(model, prompt, num_ctx, num_predict, seed):
    """Como call(), mas retorna (content, secs, ntok, stop_reason, from_thinking)."""
    if PROVIDER == "openrouter":
        return call_openrouter_ex(model, prompt, num_predict, seed)
    return call_ollama_ex(model, prompt, num_ctx, num_predict, seed)


def run_one(model, framing, run, prompt_ctx, out_dir, num_ctx, num_predict):
    if prompt_ctx.get("strata") is None:  # baseline: sem metodologia
        prompt = (BASELINE_PREAMBLE + "\n## ARQUIVOS DO PROJETO\n" + prompt_ctx["target"]
                  + "\n\n## TAREFA\n" + BASELINE_TASK)
    else:
        prompt = (PREAMBLE + "\n## METODOLOGIA (Strata)\n" + prompt_ctx["strata"]
                  + "\n\n## ARQUIVOS DO PROJETO\n" + prompt_ctx["target"]
                  + "\n\n## TAREFA\n" + TASK[framing])
    stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    safe = model.replace(":", "_").replace("/", "_")
    name = f"plano-{safe}-{framing}-r{run}.md"
    print(f"  -> {model} | {framing} | r{run} ...", flush=True)
    try:
        content, secs, ntok = call(model, prompt, num_ctx, num_predict, seed=run)
        header = (f"<!-- H-B run | model={model} | framing={framing} | run={run} | "
                  f"{stamp} | {secs:.0f}s | {ntok} tok | num_ctx={num_ctx} -->\n\n")
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write(header + content)
        print(f"     OK {secs:.0f}s, {ntok} tok -> {name}", flush=True)
    except Exception as e:  # noqa
        with open(os.path.join(out_dir, name + ".ERROR.txt"), "w", encoding="utf-8") as f:
            f.write(f"ERRO: {e}")
        print(f"     ERRO: {e}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["main", "prime", "both"], default="both")
    ap.add_argument("--target", default=os.path.join(HERE, "projeto-alvo"))
    ap.add_argument("--label", default="lumen")
    ap.add_argument("--out", default=os.path.join(HERE, "planos"))
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--num-ctx", type=int, default=20480)  # > prompt (~17k) + folga p/ gerar
    ap.add_argument("--num-predict", type=int, default=2000)
    ap.add_argument("--models", nargs="*", default=LOCAL_MODELS)
    ap.add_argument("--strata", default=STRATA, help="caminho do doc de metodologia (prose ou AN)")
    ap.add_argument("--baseline", action="store_true", help="braço sem-Strata (controle R3): omite a metodologia")
    ap.add_argument("--provider", choices=["ollama", "openrouter"], default="ollama",
                    help="ollama=local; openrouter=nuvem multi-sabor (precisa OPENROUTER_API_KEY)")
    a = ap.parse_args()
    global PROVIDER
    PROVIDER = a.provider
    if PROVIDER == "openrouter" and not os.environ.get("OPENROUTER_API_KEY"):
        print("RECUSADO: --provider openrouter precisa da env OPENROUTER_API_KEY.", file=sys.stderr)
        return 2

    # GUARD read-only: so escreve dentro do eval/strata
    out = os.path.abspath(a.out)
    if not out.startswith(os.path.abspath(HERE)):
        print(f"RECUSADO: --out ({out}) fora do eval/strata. Protecao read-only.", file=sys.stderr)
        return 2
    os.makedirs(out, exist_ok=True)

    if a.baseline:
        strata = None
    else:
        strata = read_text(os.path.abspath(a.strata))
        if not strata:
            print(f"ERRO: Strata nao lido em {a.strata}", file=sys.stderr)
            return 2
    target = read_target(os.path.abspath(a.target))
    if not target.strip():
        print(f"ERRO: nenhum arquivo de texto lido em {a.target}", file=sys.stderr)
        return 2
    ctx = {"strata": strata, "target": target}

    nchars = len(strata) if strata else 0
    metodo = "BASELINE (sem-Strata)" if a.baseline else os.path.basename(a.strata)
    print(f"== H-B runner | alvo='{a.label}' | metodo={metodo} ({nchars} chars) | "
          f"target={len(target)} chars | mode={a.mode} | runs={a.runs}")
    print(f"   (READ-ONLY: completion-only; saida so em {out})")

    if a.mode in ("main", "both"):
        d = os.path.join(out, a.label)
        os.makedirs(d, exist_ok=True)
        print(f"\n[TIER LOCAL — F1 fixo] {len(a.models)} modelos x {a.runs} run(s)")
        for m in a.models:
            for run in range(1, a.runs + 1):
                run_one(m, "F1", run, ctx, d, a.num_ctx, a.num_predict)

    if a.mode in ("prime", "both"):
        d = os.path.join(out, a.label + "-hb-prime")
        os.makedirs(d, exist_ok=True)
        print(f"\n[H-B' — {PRIME_MODEL} x 4 framings (F1-F4) x {a.runs} run(s)]")
        for fr in ["F1", "F2", "F3", "F4"]:
            for run in range(1, a.runs + 1):
                run_one(PRIME_MODEL, fr, run, ctx, d, a.num_ctx, a.num_predict)

    print("\n== concluido. Planos em:", out)


if __name__ == "__main__":
    raise SystemExit(main())
