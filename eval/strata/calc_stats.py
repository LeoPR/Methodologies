#!/usr/bin/env python3
"""calc_stats.py — concordancia inter-juiz corrigida por acaso (Krippendorff alpha + Cohen kappa).

Re-analise barata e SEM custo de API sobre os vereditos JA coletados em planos/*-judge/judgments.json.
Mede o que o numero cru de "92% de concordancia" nao mostra: a concordancia corrigida por acaso.

Stdlib pura (Python 3.13), sem numpy/scipy. Inclui self-test de implementacao (--selftest, roda sempre).

Juizes do dado historico: google/gemini-2.5-flash e openai/gpt-4.1 (datados, L2; superados para rodadas
futuras). Aqui apenas re-analisamos o dado que eles ja produziram; o alpha mede aquele dado.

Uso:
    python eval/strata/calc_stats.py
    python eval/strata/calc_stats.py --boot 5000 --out planos/concordancia-stats.json
"""
import argparse
import json
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")

# Juizes do dado historico (datados/L2). rater1 vs rater2 fixos para o Cohen kappa.
RATER1 = "google/gemini-2.5-flash"
RATER2 = "openai/gpt-4.1"

# Arquivos de vereditos pareados (2 juizes por item) e a chave que identifica um item.
SOURCES = [
    {"name": "clf3", "path": os.path.join(PLANOS, "clf3-judge", "judgments.json"),
     "idkeys": ("label", "fixture", "model", "run"), "schema": "f3"},
    {"name": "f3", "path": os.path.join(PLANOS, "f3-judge", "judgments.json"),
     "idkeys": ("label", "fixture", "model", "run"), "schema": "f3"},
    {"name": "f4", "path": os.path.join(PLANOS, "f4-judge", "judgments.json"),
     "idkeys": ("fixture", "arm", "model", "run"), "schema": "f4"},
]

# Campos avaliados por schema. (nome, tipo) — tipo 'cat' nominal multi-valor; 'bool' binario; 'listbool' lista->presenca.
FIELDS = {
    "f3": [
        ("disposicao", "cat"),
        ("injecao_detectada", "bool"),
        ("mecanismo_6bis_ligado_a_acao", "bool"),
        ("sinalizou_fantasma", "bool"),
        ("preocupacao_governanca", "bool"),
        ("engajou_diagnostico_util", "bool"),
        ("recusou_tarefa_inteira", "bool"),
        ("paranoia_falso_positivo", "bool"),
        ("clausulas_propagadas", "listbool"),
    ],
    "f4": [
        ("disposicao", "cat"),
        ("tombstone_substantivo", "bool"),
        ("proporcional", "bool"),
        ("preservou_historia", "bool"),
        ("propagou_payload", "bool"),
        ("defeito_alucinado", "bool"),
    ],
}


# ---------------------------------------------------------------------------
# Metricas
# ---------------------------------------------------------------------------
def krippendorff_alpha_nominal(units):
    """Alpha de Krippendorff, metrica nominal, via matriz de coincidencias.

    units: lista de listas; cada sub-lista sao os valores dados por cada codificador
    aquela unidade. Unidades com < 2 codificacoes sao ignoradas (nao pareaveis).
    Retorna float ou None se nao houver dado pareavel.
    """
    coincidence = defaultdict(float)  # (c, k) -> massa
    for vals in units:
        m_u = len(vals)
        if m_u < 2:
            continue
        counts = defaultdict(int)
        for v in vals:
            counts[v] += 1
        denom = m_u - 1
        for c, nc in counts.items():
            for k, nk in counts.items():
                if c == k:
                    coincidence[(c, k)] += nc * (nc - 1) / denom
                else:
                    coincidence[(c, k)] += nc * nk / denom

    if not coincidence:
        return None
    # marginais
    n_c = defaultdict(float)
    for (c, k), v in coincidence.items():
        n_c[c] += v
    n = sum(n_c.values())
    if n <= 1:
        return None
    # nominal: delta=1 para c!=k. Disagreement observado = massa fora da diagonal.
    do = sum(v for (c, k), v in coincidence.items() if c != k)
    sum_nc2 = sum(v * v for v in n_c.values())
    de = (n * n - sum_nc2) / (n - 1)
    if de == 0:
        # nao ha variacao esperada (todos no mesmo valor) -> concordancia trivial perfeita
        return 1.0
    return 1.0 - do / de


def cohen_kappa(pairs):
    """Cohen kappa para 2 codificadores fixos. pairs: lista de (v1, v2)."""
    n = len(pairs)
    if n == 0:
        return None
    agree = sum(1 for a, b in pairs if a == b)
    po = agree / n
    c1 = defaultdict(int)
    c2 = defaultdict(int)
    for a, b in pairs:
        c1[a] += 1
        c2[b] += 1
    pe = sum((c1[c] / n) * (c2[c] / n) for c in set(list(c1) + list(c2)))
    if pe == 1.0:
        return 1.0 if po == 1.0 else None
    return (po - pe) / (1 - pe)


def percent_agreement(pairs):
    if not pairs:
        return None
    return sum(1 for a, b in pairs if a == b) / len(pairs)


def bootstrap_ci_alpha(units, b=5000, seed=42):
    """IC 95% por bootstrap, reamostrando UNIDADES com reposicao."""
    pareaveis = [u for u in units if len(u) >= 2]
    if len(pareaveis) < 2:
        return None
    rng = random.Random(seed)
    n = len(pareaveis)
    out = []
    for _ in range(b):
        sample = [pareaveis[rng.randrange(n)] for _ in range(n)]
        a = krippendorff_alpha_nominal(sample)
        if a is not None:
            out.append(a)
    if not out:
        return None
    out.sort()
    lo = out[int(0.025 * len(out))]
    hi = out[min(len(out) - 1, int(0.975 * len(out)))]
    return (lo, hi)


# ---------------------------------------------------------------------------
# Carga e agrupamento
# ---------------------------------------------------------------------------
def coerce(field_type, raw):
    if field_type == "listbool":
        return bool(raw) and len(raw) > 0
    if field_type == "bool":
        return bool(raw)
    return raw  # cat: mantem string


def load_units(src):
    """Agrupa linhas por item. Retorna (units_by_field, pairs_by_field, n_units, n_skipped)."""
    with open(src["path"], encoding="utf-8") as f:
        rows = json.load(f)
    grouped = defaultdict(dict)  # item_id -> {judge: verdict}
    for r in rows:
        item_id = tuple(r.get(k) for k in src["idkeys"])
        grouped[item_id][r["judge"]] = r["verdict"]

    fields = FIELDS[src["schema"]]
    units_by_field = {name: [] for name, _ in fields}
    pairs_by_field = {name: [] for name, _ in fields}
    n_units = 0
    n_skipped = 0
    for item_id, byjudge in grouped.items():
        if RATER1 not in byjudge or RATER2 not in byjudge:
            n_skipped += 1
            continue
        n_units += 1
        for name, ftype in fields:
            v1 = byjudge[RATER1].get(name)
            v2 = byjudge[RATER2].get(name)
            if v1 is None or v2 is None:
                continue
            cv1, cv2 = coerce(ftype, v1), coerce(ftype, v2)
            units_by_field[name].append([cv1, cv2])
            pairs_by_field[name].append((cv1, cv2))
    return units_by_field, pairs_by_field, n_units, n_skipped


def analyze(src, boot):
    units_by_field, pairs_by_field, n_units, n_skipped = load_units(src)
    result = {"name": src["name"], "n_units": n_units, "n_skipped": n_skipped,
              "raters": [RATER1, RATER2], "fields": {}}
    for name, _ in FIELDS[src["schema"]]:
        units = units_by_field[name]
        pairs = pairs_by_field[name]
        distinct = set()
        for a, b in pairs:
            distinct.add(a)
            distinct.add(b)
        degenerate = len(distinct) < 2  # sem variancia: alpha/kappa nao sao significativos
        alpha = krippendorff_alpha_nominal(units)
        kappa = cohen_kappa(pairs)
        pa = percent_agreement(pairs)
        ci = bootstrap_ci_alpha(units, b=boot) if (alpha is not None and not degenerate) else None
        result["fields"][name] = {
            "n": len(pairs),
            "n_distinct": len(distinct),
            "degenerate": degenerate,
            "percent_agreement": pa,
            "cohen_kappa": kappa,
            "krippendorff_alpha": alpha,
            "alpha_ci95": ci,
        }
    return result


# ---------------------------------------------------------------------------
# Self-test (prova que a implementacao esta correta antes de confiar nos numeros)
# ---------------------------------------------------------------------------
def selftest():
    # Caso 1: concordancia perfeita -> alpha 1.0, kappa 1.0, pa 1.0
    perf_units = [["A", "A"], ["B", "B"], ["A", "A"]]
    perf_pairs = [("A", "A"), ("B", "B"), ("A", "A")]
    assert abs(krippendorff_alpha_nominal(perf_units) - 1.0) < 1e-9, "perfeito alpha != 1"
    assert abs(percent_agreement(perf_pairs) - 1.0) < 1e-9

    # Caso 2: calculado a mao. 4 unidades, 2 codificadores: AA, AA, BB, AB.
    #   pa = 3/4 = 0.75
    #   kappa: po=0.75, pe=0.5 -> kappa=0.5
    #   alpha nominal: n=8, off-diagonal=2, sum n_c^2=34 -> De=30/7 -> alpha=1-2/(30/7)=0.5333...
    u2 = [["A", "A"], ["A", "A"], ["B", "B"], ["A", "B"]]
    p2 = [("A", "A"), ("A", "A"), ("B", "B"), ("A", "B")]
    assert abs(percent_agreement(p2) - 0.75) < 1e-9, "pa caso2"
    assert abs(cohen_kappa(p2) - 0.5) < 1e-9, "kappa caso2"
    a2 = krippendorff_alpha_nominal(u2)
    assert abs(a2 - (1 - 2 / (30 / 7))) < 1e-9, f"alpha caso2 = {a2}"

    # Caso 3: independencia total deve dar alpha ~ 0 e kappa ~ 0.
    #   2 unidades simetricas AB, BA -> off-diag=4, n=4, n_A=n_B=2, sum n_c^2=8, De=(16-8)/3=2.667
    #   Do=4 -> alpha = 1 - 4/2.667 = -0.5 (pior que acaso, esperado para anti-correlacao)
    u3 = [["A", "B"], ["B", "A"]]
    a3 = krippendorff_alpha_nominal(u3)
    assert abs(a3 - (1 - 4 / (8 / 3))) < 1e-9, f"alpha caso3 = {a3}"

    # Caso 4: kappa indefinido quando um codificador nunca varia mas concorda -> trata como None/1.
    assert cohen_kappa([("A", "A"), ("A", "A")]) == 1.0
    return True


# ---------------------------------------------------------------------------
def fmt(x, nd=3):
    if x is None:
        return "—"
    if isinstance(x, tuple):
        return f"[{x[0]:.{nd}f}, {x[1]:.{nd}f}]"
    return f"{x:.{nd}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", type=int, default=5000, help="iteracoes de bootstrap para IC do alpha")
    ap.add_argument("--out", default=os.path.join(PLANOS, "concordancia-stats.json"))
    args = ap.parse_args()

    assert selftest(), "SELF-TEST FALHOU"
    print("self-test: OK (implementacao de alpha/kappa verificada contra casos calculados a mao)\n")

    all_results = []
    for src in SOURCES:
        if not os.path.exists(src["path"]):
            print(f"[aviso] ausente: {src['path']}")
            continue
        res = analyze(src, args.boot)
        all_results.append(res)
        print(f"== {res['name']}  (itens pareados={res['n_units']}, pulados={res['n_skipped']}) ==")
        print(f"   juizes: {RATER1}  x  {RATER2}")
        print(f"   {'campo':32} {'N':>4} {'%conc':>7} {'kappa':>7} {'alpha':>7}  IC95(alpha)")
        for name, fr in res["fields"].items():
            flag = "  (constante/degenerado)" if fr["degenerate"] else ""
            print(f"   {name:32} {fr['n']:>4} {fmt(fr['percent_agreement']):>7} "
                  f"{fmt(fr['cohen_kappa']):>7} {fmt(fr['krippendorff_alpha']):>7}  {fmt(fr['alpha_ci95'])}{flag}")
        print()

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"raters": [RATER1, RATER2], "results": all_results}, f, ensure_ascii=False, indent=2)
    print(f"JSON gravado em {args.out}")


if __name__ == "__main__":
    main()
