#!/usr/bin/env python3
"""Exporta a amostra da revisão cega (revisao_tb.py amostra) como itens JSON para revisores: só cenas rotuladas, regras,
gabarito em rótulos de exibição e as linhas SEQUÊNCIA/NOTA. Sem braço, sem modelo e sem a classe do pontuador.
Uso: python revisao_itens.py planos/tb-v1 > itens.json   (lê planos/tb-v1-revisao-chave.json)
"""
import json
import os
import sys

import revisao_tb as R
import score_tb as S

# o que conta como "passo que falta" em cada fixture de lacuna (tabela do §2 do PREREG)
LACUNA = {"T3-P": "a decolagem: o avião sai do chão e sobe (ela embarca no chão e, na cena seguinte, salta da porta em voo)",
          "T3-O": "o encaixe e a carga do orbe (ele está polido e fora do suporte e, na cena seguinte, brilha no suporte)"}
CLASSES = {"ordem": ["NOTA-LIMPA", "ALARME"], "controle-horario": ["NOTA-LIMPA", "ALARME"],
           "horario-errado": ["CONFLITO-APONTADO", "CONFLITO-OMITIDO"], "lacuna": ["LACUNA-APONTADA", "LACUNA-SILENCIOSA"],
           "intruso": ["INTRUSO-APONTADO", "INTRUSO-INCLUIDO"],
           "incomparaveis": ["INCOMP-DECLARADO", "INCOMP-PARCIAL", "INCOMP-FORCADO"],
           "fora-do-script": ["SEGUE-OBSERVADO", "ORDEM-ERRADA"]}


def main():
    indir = sys.argv[1]
    chave = json.load(open(indir.rstrip("/\\") + "-revisao-chave.json", encoding="utf-8"))
    por_arq = {r["arquivo"]: r for r in R.linhas_com_texto(indir)}
    itens = []
    for i, arq in sorted(chave.items(), key=lambda x: int(x[0])):
        r = por_arq[os.path.normpath(arq)]
        f = S.BAT["fixtures"][r["fixture"]]
        d = {k: S.ROTULOS[j] for j, k in enumerate(r["mapa"])}
        gab = {"antes": [f"{d[a]} antes de {d[b]}" for a, b in f["antes"]]}
        if f.get("incomparaveis"):
            gab["sem_ordem"] = [f"{d[a]} e {d[b]}" for a, b in f["incomparaveis"]]
        if f.get("conflito"):
            gab["conflito_de_horario"] = f"o horário anotado de {d[f['conflito'][1]]} vem antes do de {d[f['conflito'][0]]}, contra a dependência"
        if f.get("intruso"):
            gab["intruso"] = d[f["intruso"]]
        if r["fixture"] in LACUNA:
            gab["passo_que_falta"] = LACUNA[r["fixture"]]
        itens.append({"id": int(i), "papel": f["papel"], "classes_validas": CLASSES[f["papel"]] + ["SEM-LINHA"],
                      "regras": S.BAT["dominios"][f["dominio"]]["regras"] or [],
                      "cenas": {d[k]: f["cenas"][k] for k in r["mapa"]}, "gabarito": gab,
                      "sequencia": r["seq_txt"], "nota": r["nota_txt"]})
    json.dump(itens, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
