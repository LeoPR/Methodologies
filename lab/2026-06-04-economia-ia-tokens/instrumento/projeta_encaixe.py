#!/usr/bin/env python3
"""projeta_encaixe.py — extrapola o encaixe (cabe? a que velocidade?) para placas de mercado.

Entrada: os pontos medidos por fit_encaixe.py (dois contextos por modelo) e um catalogo de modelos
nao medidos (tamanho do arquivo Q4 e parametros ativos, de fonte citada). Modelo:

  memoria(ctx)  = base + kv_por_token * ctx                      (reta por modelo, 2 pontos medidos)
  base          = arquivo * fator_base                            (fator ajustado nos medidos)
  kv_por_token  (nao medido) = regressao linear kv ~ arquivo     (ajustada nos medidos; R2 declarado)
  cabe_inteiro  = memoria(ctx) + fundo_desktop <= VRAM
  decode_tps    = eficiencia * banda / bytes_ativos               (so quando cabe inteiro)
  bytes_ativos  = arquivo * (params_ativos / params_totais)       (MoE le so os experts ativos)
  eficiencia    = mediana nos pontos medidos que cabem inteiros na placa de referencia

Hipoteses (declaradas na saida): decode batch-1 limitado por banda; quantizacao Q4_K_M; KV f16;
offload nao e extrapolado (so medido na placa de referencia); prefill fora do modelo.
Uso: python projeta_encaixe.py --pontos encaixe_pontos_2026-09-26.json --ctx 32768
"""
import argparse
import json
import statistics

REF_BW = 360.0  # GB/s, RTX 3060 12GB (placa de referencia medida)

# Placas de mercado: (nome, VRAM GB, banda GB/s). Especificacao de fabricante; conferir antes de
# decisao cara (camada datada).
GPUS = [("RTX 4060 8GB", 8, 272), ("RTX 3060 12GB", 12, 360), ("RTX 4070 12GB", 12, 504),
        ("RTX 4060 Ti 16GB", 16, 288), ("RTX 5060 Ti 16GB", 16, 448),
        ("RTX 4070 Ti Super 16GB", 16, 672), ("RTX 3090 24GB", 24, 936),
        ("RTX 4090 24GB", 24, 1008), ("RTX 5090 32GB", 32, 1792)]

# Modelos nao medidos localmente: arquivo Q4 (GB) e parametros (total, ativos) em bilhoes.
# Fonte: biblioteca Ollama / model cards, via lab/2026-09-26-banco-modelos (relatorio de
# novidades). Valores de tamanho sao da tag Q4 mais comum.
# Quinto campo: familia medida cuja razao KV/arquivo se herda (None = limite conservador da atencao
# completa, o pior caso medido). O KV depende da arquitetura de atencao (completa x janela deslizante
# x hibrida x MLA), nao so do tamanho: por isso nao se usa uma regressao unica.
NAO_MEDIDOS = [
    ("gemma4:26b (26B-A4B)", 19.0, 26, 4, "gemma4:12b"),
    ("gemma-4-31b", 20.0, 31, 31, "gemma4:12b"),
    ("gpt-oss:20b", 14.0, 21, 3.6, None),
    ("nemotron-3.5-lightning 30B-A3B", 25.0, 31.6, 3.6, None),
    ("muse-glimmer:30b", 18.0, 29.6, 29.6, None),
    ("gpt-oss:120b", 65.0, 117, 5.1, None),
    ("deepseek-v4-flash (284B-A13B)", 82.5, 284, 13, None),
]


def linreg(xs, ys):
    mx, my = statistics.mean(xs), statistics.mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    a = my - b * mx
    ss_res = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys) or 1e-9
    return a, b, 1 - ss_res / ss_tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pontos", required=True)
    ap.add_argument("--ctx", type=int, default=32768)
    ap.add_argument("--fundo-gb", type=float, default=None,
                    help="VRAM ocupada pelo desktop antes de carregar (default: mediana medida)")
    ap.add_argument("--ram-gb", type=float, default=64.0, help="RAM do sistema p/ offload")
    a = ap.parse_args()
    data = json.load(open(a.pontos, encoding="utf-8"))

    med = []
    fundos = []
    for m in data:
        pts = sorted([p for p in m["points"] if p.get("size_gb")], key=lambda p: p["num_ctx"])
        if len(pts) < 2:
            continue
        (c1, s1), (c2, s2) = (pts[0]["num_ctx"], pts[0]["size_gb"]), (pts[-1]["num_ctx"], pts[-1]["size_gb"])
        kv = max(0.0, (s2 - s1) / (c2 - c1))  # janela deslizante pode dar ~0 (ou ruido negativo)
        base = s1 - kv * c1
        arch = m["arch"]
        tot = (arch.get("params") or 0) / 1e9
        act = tot
        if arch.get("experts") and arch.get("experts_used"):
            act = None  # MoE: ativos declarados no catalogo abaixo
        fit_pts = [p for p in pts if not p["offload"] and p.get("decode_tps")]
        fundos += [p["gpu_used_before_mib"] / 1024 for p in pts if p.get("gpu_used_before_mib")]
        med.append({"model": m["model"], "file": arch["file_gb"], "kv": kv, "base": base,
                    "tot": tot, "act": act, "pts": pts, "fit_pts": fit_pts})
    fundo = a.fundo_gb if a.fundo_gb is not None else (statistics.median(fundos) if fundos else 1.5)

    # MoE medidos: ativos da literatura (arquitetura do ollama nao da o numero direto)
    ATIVOS = {"qwen3.6:35b-a3b": 3.0}
    for x in med:
        if x["act"] is None:
            x["act"] = ATIVOS.get(x["model"], x["tot"])

    fator_base = statistics.median([x["base"] / x["file"] for x in med])
    a_kv, b_kv, r2 = linreg([x["file"] for x in med], [x["kv"] * 1e6 for x in med])  # kv em GB por 1M tok
    effs = []
    for x in med:
        for p in x["fit_pts"]:
            bytes_at = x["file"] * (x["act"] / x["tot"])
            effs.append(p["decode_tps"] * bytes_at / REF_BW)
    eff = statistics.median(effs) if effs else None

    print(f"## Ajuste (placa de referencia RTX 3060 12GB, banda {REF_BW:.0f} GB/s)\n")
    print(f"- fundo do desktop medido: {fundo:.2f} GB de VRAM antes de carregar o modelo")
    print(f"- fator base (memoria fixa / arquivo): {fator_base:.2f}")
    print(f"- KV por token ~ arquivo (so para mostrar que NAO serve de regra): R2 = {r2:.2f}, n={len(med)}; "
          "o KV depende da arquitetura de atencao")
    print(f"- eficiencia de banda (mediana, {len(effs)} pontos que cabem inteiros): {eff:.2f}\n" if eff else "")
    print("| modelo medido | arquivo GB | KV MB/1k tok | memoria @8k | memoria @32k | decode tok/s (3060) | offload? |")
    print("|---|---|---|---|---|---|---|")
    for x in med:
        p8 = x["pts"][0]
        p32 = x["pts"][-1]
        print(f"| {x['model']} | {x['file']:.1f} | {x['kv'] * 1e3 * 1e3 / 1:.0f} | {p8['size_gb']:.1f} | {p32['size_gb']:.1f} | "
              f"{p8.get('decode_tps')} / {p32.get('decode_tps')} | {'sim' if p32['offload'] else 'não'} |")

    # linha = (nome, memoria_min, memoria_max, bytes_ativos, eh_moe, origem)
    rows = []
    for x in med:
        m = x["base"] + x["kv"] * a.ctx
        rows.append((x["model"], m, m, x["file"] * x["act"] / x["tot"], x["act"] < x["tot"], "medido"))
    by_model = {x["model"]: x for x in med}
    kv_por_gb_pior = max(x["kv"] / x["file"] for x in med)
    for nome, arq, tot, act, fam in NAO_MEDIDOS:
        pesos = arq * fator_base
        if fam in by_model:
            m = pesos + by_model[fam]["kv"] / by_model[fam]["file"] * arq * a.ctx
            rows.append((nome, m, m, arq * act / tot, act < tot, f"projetado (KV da família {fam})"))
        else:
            # KV desconhecido: faixa de so-pesos ate pesos + pior KV medido (atencao completa)
            rows.append((nome, pesos, pesos + kv_por_gb_pior * arq * a.ctx, arq * act / tot, act < tot,
                         "projetado (faixa: KV desconhecido)"))

    print(f"\n## Projeção @ {a.ctx // 1024}k de contexto (o Strata inteiro no prompt pede ~32k)\n")
    head = "| modelo | memória @ctx GB | origem | " + " | ".join(g[0] for g in GPUS) + " |"
    print(head)
    print("|" + "---|" * (3 + len(GPUS)))
    for nome, mmin, mmax, bytes_at, moe, origem in rows:
        cells = []
        for _, vram, bw in GPUS:
            if mmax + fundo <= vram:
                # velocidade so para densos: a eficiencia foi calibrada em densos e superestima MoE
                cells.append("cabe" if moe or not eff else f"cabe · ~{eff * bw / bytes_at:.0f} tok/s")
            elif mmin + fundo <= vram:
                cells.append("talvez (medir)")
            elif mmin <= vram + a.ram_gb - 8:
                cells.append("offload")
            else:
                cells.append("não")
        faixa = f"{mmin:.1f}" if abs(mmax - mmin) < 0.05 else f"{mmin:.1f}–{mmax:.1f}"
        print(f"| {nome}{' (MoE)' if moe else ''} | {faixa} | {origem} | " + " | ".join(cells) + " |")
    print("\nHipóteses: decode batch-1 limitado por banda (velocidade só para densos: a eficiência foi "
          "calibrada em densos e superestima MoE, cuja velocidade fica só a medida); Q4_K_M; KV f16; "
          "offload não extrapolado "
          f"(lento; medido só na 3060); RAM p/ offload {a.ram_gb:.0f} GB; 'cabe' exige memória + fundo "
          "do desktop ≤ VRAM. Projetados: KV da família medida quando há; senão uma faixa de só-pesos "
          "até pesos + pior KV medido (atenção completa); 'talvez (medir)' = cabe no limite inferior e "
          "não no superior: é caso para uma sonda local.")


if __name__ == "__main__":
    main()
