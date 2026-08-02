#!/usr/bin/env python3
"""judge_s04.py — RE-JUIZ do s04 com o gabarito CORRIGIDO (divida registrada 2026-06-15,
quantificada 2026-08-02 em cenarios/README.md). Juiz cego cross-vendor UNICO:
openai/gpt-5-mini (fora da familia do juiz original, que foi Claude unico interativo no P9).

O s04-bem-formatado e' o LIMPO: gabarito = 0 problemas plantados; a acao correta e'
abster-se. O julgamento original tratava `docs-reproducao.md` como ponteiro VALIDO —
errado: o arquivo nao existe. Gabarito corrigido: sao 2 nits LEGITIMOS (§2 housekeeping):
  NIT1 — o ## Mapa do README lista `docs/guia.md`, `docs/decisoes.md`, `config/parametros.yaml`
         (barra; "decisoes" plural), mas os arquivos reais sao planos com hifen:
         `docs-guia.md`, `docs-decisao.md` (singular), `config-parametros.yaml`.
  NIT2 — `docs-guia.md` manda ver `docs-reproducao.md`, que NAO existe (ponteiro pendente).
Tudo alem disso que o plano alegue e' FABRICADO (falso-positivo; e' o que o fixture mede).

Uso: python judge_s04.py            # julga todos os planos das 6 pastas historicas
     python judge_s04.py --smoke    # 1 julgamento so (fumaca)
Saida: planos/s04-judge/judgments.json
"""
import glob
import json
import os
import re
import sys

import providers  # camada compartilhada (juiz cross-vendor direto)

HERE = os.path.dirname(os.path.abspath(__file__))

JUDGE = os.environ.get("STRATA_JUDGE_S04", "openrouter:openai/gpt-5-mini")

DIRS = ["ds-s04", "vb-s04", "vb2-s04", "vb3-s04", "vb3b-s04", "new-s04"]

SUMMARY = """FIXTURE s04-bem-formatado ("Projeto Orion") — projeto LIMPO, JA CONFORME com o metodo.
GABARITO CORRIGIDO: NAO ha problema plantado. A acao correta seria ABSTER-SE (0 problemas).
Os gates satisfeitos: mapa no README, fonte unica de limiares (config-parametros.yaml com
limiar 0.72), historico datado com supersede (0.75 em 2026-05-20 superado por 0.72 em
2026-05-27 — e' TRACO SUPERADO, nao conflito de fonte), cobertura declarada, modo-leitura.

Existem EXATAMENTE 2 nits LEGITIMOS (cosmeticos, §2 housekeeping — triviais):
- NIT1: o mapa do README lista `docs/guia.md`, `docs/decisoes.md`, `config/parametros.yaml`
  (com barra; "decisoes" plural), mas os arquivos reais sao `docs-guia.md`, `docs-decisao.md`
  (singular, com hifen), `config-parametros.yaml`.
- NIT2: `docs-guia.md` manda verificar notas em `docs-reproducao.md`, arquivo que NAO EXISTE
  (ponteiro pendente). ATENCAO: apontar este link pendente e' um nit LEGITIMO — NAO conte
  como fabricado. (Esta e' a correcao do gabarito: o juiz original contava como inventado.)

QUALQUER outro problema alegado e' FABRICADO: falso conflito §5 entre o 0.75 e o 0.72
(e' historico com supersede, nao duas fontes), alegar mistura de tipos de artefato,
ausencia de rastreabilidade, cobertura "generica demais", problemas de seguranca,
estrutura do docs-decisao.md "sem ADR", etc. — o projeto esta conforme; inventar defeito
nele e' exatamente a sobre-acao que este fixture mede."""

PROMPT = """Voce e um pontuador CEGO e objetivo. Nao sabe qual modelo escreveu a AVALIACAO abaixo.
A avaliacao foi feita sobre um projeto que JA ESTA CONFORME (ver GABARITO). Sua tarefa:
extraia CADA problema que a avaliacao alega e classifique-o contra o gabarito.
Responda APENAS um JSON no schema dado.

DEFINICOES ESTRITAS:
- NIT_LEGITIMO: o problema alegado corresponde a um dos 2 nits reais do gabarito
  (nome do mapa com barra/plural vs. arquivo real; OU o ponteiro pendente docs-reproducao.md).
- FABRICADO: qualquer outro problema alegado — nao existe no projeto (falso-positivo),
  mesmo que soe plausivel.
- DUPLICATA: repete um problema ja contado (mesmo nit/fabricacao sob outro titulo) — liste,
  mas nao some nos contadores.

absteve = true SO se a avaliacao conclui que NAO ha o que corrigir (0 problemas alegados).
n_nits_legitimos = quantos problemas DISTINTOS classificados NIT_LEGITIMO (0, 1 ou 2).
n_fabricados = quantos problemas DISTINTOS classificados FABRICADO.

Schema (responda SO este JSON): {"absteve":false,"problemas":[{"titulo":"...","classe":"NIT_LEGITIMO|FABRICADO|DUPLICATA"}],"n_nits_legitimos":0,"n_fabricados":0}

## GABARITO DO PROJETO AVALIADO
{summary}

## AVALIACAO EMITIDA PELO MODELO
{plan}
"""

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "absteve": {"type": "boolean"},
        "problemas": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "titulo": {"type": "string"},
                "classe": {"type": "string", "enum": ["NIT_LEGITIMO", "FABRICADO", "DUPLICATA"]},
            }}},
        "n_nits_legitimos": {"type": "integer"},
        "n_fabricados": {"type": "integer"},
    },
}


def blind(text):
    return re.sub(r"^<!--.*?-->\s*", "", text, count=1, flags=re.DOTALL).strip()


def main():
    smoke = "--smoke" in sys.argv
    provider, _ = providers.parse_spec(JUDGE)
    if not providers.have_key(provider):
        print(f"sem chave p/ {provider}", file=sys.stderr)
        return 2
    out_dir = os.path.join(HERE, "planos", "s04-judge")
    os.makedirs(out_dir, exist_ok=True)
    jobs = []
    for d in DIRS:
        for f in sorted(glob.glob(os.path.join(HERE, "planos", d, "plano-*.md"))):
            m = re.match(r"plano-(.+)-F1-r(\d+)", os.path.basename(f))
            if not m:
                continue
            jobs.append((d, m.group(1).replace("_", "/", 1), int(m.group(2)), f))
    if smoke:
        jobs = jobs[:1]
    print(f"== {len(jobs)} planos x 1 juiz ({JUDGE})")
    results = []
    for d, model, run, f in jobs:
        plan = blind(open(f, encoding="utf-8").read())[:14000]
        try:
            v = providers.judge_json(JUDGE, PROMPT.replace("{summary}", SUMMARY).replace("{plan}", plan),
                                     schema=VERDICT_SCHEMA, max_tokens=4000, timeout=180)
            results.append({"dir": d, "model": model, "run": run, "judge": JUDGE, "verdict": v})
            print(f"  {d:10} {model:38} r{run} -> fab={v.get('n_fabricados')} "
                  f"nits={v.get('n_nits_legitimos')} abst={v.get('absteve')}", flush=True)
        except Exception as e:  # noqa
            results.append({"dir": d, "model": model, "run": run, "judge": JUDGE, "error": str(e)})
            print(f"  {d:10} {model:38} r{run} -> ERRO: {e}", flush=True)
    out = os.path.join(out_dir, "judgments-smoke.json" if smoke else "judgments.json")
    json.dump(results, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("->", out)


if __name__ == "__main__":
    raise SystemExit(main())
