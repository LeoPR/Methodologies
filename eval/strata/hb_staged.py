#!/usr/bin/env python3
"""F4 — runner de ETAPAS (H-E): aplica o Strata em 4 turnos guiados (mapear+reconhecer ->
situar-no-tempo -> gate-a-gate-com-evidencia -> priorizar+relatorio). Multi-turn via OpenRouter,
mesma protecao read-only do hb_runner. O RELATORIO da ETAPA 4 = o plano a pontuar.
Uso: python hb_staged.py --models openai/gpt-4.1-mini ... --target fixtures-real/nnn-digest --label p6f4-nnn"""
import argparse
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request

import hb_runner  # reusa read_target / OPENROUTER

HERE = os.path.dirname(os.path.abspath(__file__))
OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"

STAGES = [
    ("ETAPA 1 — MAPEAR e RECONHECER O BOM",
     "Voce vai avaliar um projeto contra o metodo Strata, EM ETAPAS. NAO corra para achar defeitos.\n"
     "ETAPA 1: leia os ARQUIVOS DO PROJETO abaixo e liste APENAS o que o projeto ja faz CERTO "
     "(forcas: indice/mapa que orienta, fonte unica com ponteiro, registra o que refutou, trata "
     "historico como traco nao-apagavel, fail-closed na leitura de artefatos...). NAO diagnostique ainda.\n\n"
     "## ARQUIVOS DO PROJETO\n{target}"),
    ("ETAPA 2 — SITUAR NO TEMPO",
     "ETAPA 2: situe no tempo. Classifique os artefatos do projeto em: ATUAL (vale agora), "
     "HISTORICO/TRACO (registro legitimo do passado), ou SUPERADO/DATADO/MARCADO. "
     "Conteudo historico, datado ou marcado-obsoleto NAO e problema atual — e o metodo funcionando."),
    ("ETAPA 3 — GATE A GATE, COM EVIDENCIA",
     "ETAPA 3: agora, gate a gate, ha violacao? Avalie cada um e cite TRECHO literal (arquivo+citacao):\n"
     "- §6-bis: instrucao mandando um agente EXECUTAR/baixar-e-rodar de arquivo/URL sem confirmacao? (CLI que um HUMANO digita = NAO)\n"
     "- §5: o MESMO fato com VALORES diferentes em 2 fontes atuais e SEM sinalizacao?\n"
     "- §3: codigo/decisao abandonado apresentado como VIVO, sem tombstone?\n"
     "- §4: relato so-sucesso, sem metodo/o-que-falhou?\n"
     "- §6: numero/afirmacao sem dizer de onde veio E sem ponteiro?\n"
     "- §2: falta indice/mapa que oriente?\n"
     "- §8: da pra saber atual vs antigo e por que mudou?\n"
     "REGRAS: é VALIDO 'nenhuma violacao'; divergencia/coisa antiga que o projeto JA SINALIZA "
     "(aviso, data, tombstone, ponteiro, doc de reconciliacao) = NAO e violacao; sem trecho = NAO; NAO invente."),
    ("ETAPA 4 — PRIORIZAR + RELATORIO",
     "ETAPA 4: entregue o RELATORIO FINAL consolidado com EXATAMENTE tres partes: "
     "(a) ENTENDIMENTO — o que e o metodo Strata, em suas palavras; "
     "(b) DIAGNOSTICO — reconheca primeiro 1+ forca (etapa 1), depois liste SO as violacoes REAIS "
     "confirmadas com trecho (etapa 3); "
     "(c) PRIMEIRO PASSO — priorizado pelo §9 (maior risco × menor custo); tombstone, NAO apagar; "
     "PROIBIDO 'aplicar tudo' ou >3 acoes igualmente urgentes."),
]


def call_multi(model, messages, num_predict, seed):
    key = os.environ.get("OPENROUTER_API_KEY")
    data = json.dumps({"model": model, "messages": messages, "max_tokens": num_predict,
                       "temperature": 0.3, "seed": seed}).encode("utf-8")
    hdr = {"Content-Type": "application/json", "Authorization": f"Bearer {key}",
           "HTTP-Referer": "https://github.com/LeoPR/Methodologies", "X-Title": "Strata-eval-staged"}
    last = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(OPENROUTER, data=data, headers=hdr), timeout=300) as r:
                d = json.loads(r.read().decode("utf-8"))
            return d["choices"][0]["message"]["content"], d.get("usage", {}).get("completion_tokens", 0)
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


def run_one(model, target, run, out_dir, num_predict):
    safe = model.replace(":", "_").replace("/", "_")
    name = f"plano-{safe}-F4-r{run}.md"
    stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    print(f"  -> {model} | F4-staged | r{run} ...", flush=True)
    messages, tok_total, t0 = [], 0, time.time()
    final = ""
    try:
        for i, (title, body) in enumerate(STAGES):
            content = body.format(target=target) if "{target}" in body else body
            messages.append({"role": "user", "content": content})
            out, ntok = call_multi(model, messages, num_predict, seed=run)
            messages.append({"role": "assistant", "content": out})
            tok_total += ntok
            final = out
            print(f"     [{i+1}/4] {title[:22]} ok ({ntok} tok)", flush=True)
        secs = time.time() - t0
        header = (f"<!-- P6-F4 staged | model={model} | run={run} | {stamp} | {secs:.0f}s | "
                  f"{tok_total} tok | 4 etapas -->\n\n")
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write(header + final)
        print(f"     OK {secs:.0f}s, {tok_total} tok -> {name}", flush=True)
    except Exception as e:  # noqa
        with open(os.path.join(out_dir, name + ".ERROR.txt"), "w", encoding="utf-8") as f:
            f.write(f"ERRO: {e}")
        print(f"     ERRO: {e}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--num-predict", type=int, default=1400)
    a = ap.parse_args()
    if not os.environ.get("OPENROUTER_API_KEY"):
        print("RECUSADO: precisa OPENROUTER_API_KEY.", file=sys.stderr); return 2
    out = os.path.join(HERE, "planos", a.label)
    if not os.path.abspath(out).startswith(os.path.abspath(HERE)):
        print("RECUSADO: out fora do eval/strata.", file=sys.stderr); return 2
    os.makedirs(out, exist_ok=True)
    target = hb_runner.read_target(os.path.abspath(a.target))
    if not target.strip():
        print(f"ERRO: nada lido em {a.target}", file=sys.stderr); return 2
    print(f"== F4 staged | alvo='{a.label}' | target={len(target)} chars | {len(a.models)} modelos x {a.runs} run(s)")
    for m in a.models:
        for run in range(1, a.runs + 1):
            run_one(m, target, run, out, a.num_predict)
    print("\n== concluido:", out)


if __name__ == "__main__":
    raise SystemExit(main())
