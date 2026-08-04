#!/usr/bin/env python3
"""F4 ADV-1 — naive + AUTO-REVISAO (2 turnos). Braco adversarial pre-registrado em
lab/2026-08-03-prompt-ingenuo/PLANO.md: testa se ITERACAO substitui metodo.
Turno 1: prompt ingenuo (escada) identico ao braco NAIVE. Turno 2: o modelo revisa a
propria resposta ("resolva sem estragar o que ja funcionava"). O que se verifica e a
resposta FINAL (turno 2); o turno 1 vai para <nome>.turno1.md (auditoria).

Uso:
  python hb_f4_adv1.py --provider openrouter --models gpt-5-mini --target cenarios/f4-dup --label f4n-dup-adv1 --runs 2 --escada E0:N1
"""
import argparse
import datetime
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core"))
import hb_runner
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hb_f4

HERE = hb_runner.HERE

REVISAO = ("Verifique se o que voce fez resolve o problema sem estragar o que ja "
           "funcionava; corrija se necessario. Responda com a versao FINAL, no mesmo "
           "formato (<ABSTAIN> + <FILE>).")


def call_2turnos(model, prompt1, num_predict, seed):
    """Turno 1 = prompt ingenuo; turno 2 = revisao da propria resposta. Mesmo regime do
    hb_runner.call_openrouter_ex (temp 0.3, seed, retries)."""
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY nao setada")
    msgs = [{"role": "user", "content": prompt1}]
    conteudos = []
    secs = tok = 0
    stop = None
    for turno in (1, 2):
        body = {"model": model, "messages": msgs,
                "max_tokens": num_predict, "temperature": 0.3, "seed": seed}
        data = json.dumps(body).encode("utf-8")
        hdr = {"Content-Type": "application/json", "Authorization": f"Bearer {key}",
               "HTTP-Referer": "https://github.com/LeoPR/Methodologies", "X-Title": "Strata-eval"}
        last = None
        d = None
        for attempt in range(4):
            try:
                t0 = time.time()
                with urllib.request.urlopen(urllib.request.Request(hb_runner.OPENROUTER, data=data, headers=hdr), timeout=300) as r:
                    d = json.loads(r.read().decode("utf-8"))
                secs += time.time() - t0
                break
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
        if d is None:
            raise last
        ch = d["choices"][0]
        content = (ch["message"].get("content") or "").strip()
        if not content:
            content = (ch["message"].get("reasoning") or ch["message"].get("reasoning_content") or "").strip()
        conteudos.append(content)
        tok += d.get("usage", {}).get("completion_tokens", 0)
        stop = ch.get("finish_reason")
        msgs = msgs + [{"role": "assistant", "content": content},
                       {"role": "user", "content": REVISAO}]
    return conteudos, secs, tok, stop


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["openrouter"], default="openrouter")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--escada", choices=sorted(hb_f4.ESCADA.keys()), required=True)
    ap.add_argument("--num-predict", type=int, default=4200)
    a = ap.parse_args()

    if not os.environ.get("OPENROUTER_API_KEY"):
        print("sem OPENROUTER_API_KEY", file=sys.stderr); return 2
    out = os.path.join(HERE, "planos", a.label)
    if not os.path.abspath(out).startswith(os.path.abspath(HERE)):
        print("RECUSADO: out fora do eval/strata", file=sys.stderr); return 2
    os.makedirs(out, exist_ok=True)

    target_dir = os.path.abspath(a.target)
    target = hb_runner.read_target(target_dir)
    if not target.strip():
        print(f"ERRO: nada lido em {a.target}", file=sys.stderr); return 2
    sha = hb_f4.fixture_sha(target_dir)
    task_n = hb_f4.ESCADA[a.escada] + "\n\n" + hb_f4.AVISO_DOWNSTREAM + "\n\n" + hb_f4.FORMAT
    prompt = (hb_f4.PREAMBLE_BASELINE + "\n## ARQUIVOS DO PROJETO\n" + target
              + "\n\n## TAREFA\n" + task_n)

    print(f"== F4 ADV-1 | escada={a.escada} | alvo='{a.label}' | fixture_sha={sha} | {len(a.models)} modelos x {a.runs} run(s)")
    for m in a.models:
        for run in range(1, a.runs + 1):
            safe = m.replace(":", "_").replace("/", "_")
            name = f"plano-{safe}-F4-r{run}.md"
            stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            print(f"  -> {m} | ADV1-{a.escada} | r{run} (2 turnos) ...", flush=True)
            try:
                (t1, t2), secs, tok, stop = call_2turnos(m, prompt, a.num_predict, seed=run)
                hdr = (f"<!-- F4 ADV1-{a.escada} | model={m} | run={run} | {stamp} | {secs:.0f}s | "
                       f"{tok} tok | stop={stop} | turnos=2 | fixture_sha={sha} | target={a.label} -->\n\n")
                open(os.path.join(out, name), "w", encoding="utf-8").write(hdr + t2)
                open(os.path.join(out, name + ".turno1.md"), "w", encoding="utf-8").write(
                    f"<!-- turno 1 (pre-revisao) de {name} -->\n\n" + t1)
                trunc = " [TRUNCADO?]" if stop in ("length", "max_tokens") else ""
                print(f"     OK {secs:.0f}s, {tok} tok, stop={stop}{trunc}", flush=True)
            except Exception as e:  # noqa
                open(os.path.join(out, name + ".ERROR.txt"), "w", encoding="utf-8").write(f"ERRO: {e}")
                print(f"     ERRO: {e}", flush=True)
    print("== fim:", out)


if __name__ == "__main__":
    raise SystemExit(main())
