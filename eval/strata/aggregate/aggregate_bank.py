#!/usr/bin/env python3
"""aggregate_bank.py — consolida o banco de capacidades (ops/bank_run.py) numa tabela por rota.

Rota = modelo x provedor x raciocinio. Erro de provedor (402/413/429/timeout) vira INFRA, nunca
"nao atende". A linha mais recente de cada celula vence (re-runs substituem).
Status: FAZ-TUDO (maioria em conserto, armadilha e abstencao) · CONSERTA+ARMADILHA ·
SO-CONSERTO · NAO-ATENDE (conserto abaixo da maioria) · INFRA.

Uso: python aggregate/aggregate_bank.py [--tag bank26] [--md saida.md]
"""
import argparse
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(tag):
    rows = [json.loads(l) for l in open(os.path.join(HERE, "planos", tag, "summary.jsonl"), encoding="utf-8") if l.strip()]
    latest = {}
    for r in rows:
        latest[(r["model"], r["provider"], r.get("reasoning", "default"), r["cell"])] = r
    return latest


def build(latest):
    routes = {}
    for (m, p, rs, cell), r in latest.items():
        routes.setdefault((m, p, rs), {})[cell] = r
    table = []
    for (m, p, rs), cells in sorted(routes.items()):
        fix = cells.get("fix", {})
        k = fix.get("k", 3)
        need = k // 2 + 1
        infra = fix.get("errors", 0) >= k if fix else True

        def okc(c):
            r = cells.get(c)
            if not r or r.get("skipped"):
                return None
            return r["ok"], r["k"] - r.get("errors", 0)

        res = {c: okc(c) for c in ("fix", "trap", "abst")}
        maj = {c: (v is not None and v[1] > 0 and v[0] >= (v[1] // 2 + 1)) for c, v in res.items()}
        if infra:
            status = "INFRA"
        elif not maj["fix"]:
            status = "NAO-ATENDE"
        elif maj["trap"] and maj["abst"]:
            status = "FAZ-TUDO"
        elif maj["trap"]:
            status = "CONSERTA+ARMADILHA"
        else:
            status = "SO-CONSERTO"
        costs = [c.get("cost_total") for c in cells.values() if c.get("cost_total") is not None]
        runs = sum(c.get("k", 0) - c.get("errors", 0) for c in cells.values() if not c.get("skipped"))
        secs = [c.get("secs_median") for c in cells.values() if c.get("secs_median") is not None]
        served = sorted({s for c in cells.values() for s in (c.get("served_by") or []) if s})
        table.append({"model": m, "provider": p, "reasoning": rs, "status": status,
                      "fix": res["fix"], "trap": res["trap"], "abst": res["abst"],
                      "cost_per_run": round(sum(costs) / runs, 5) if costs and runs else None,
                      "secs_median": sorted(secs)[len(secs) // 2] if secs else None,
                      "served_by": served})
    return table


def fmt(v):
    return "—" if v is None else f"{v[0]}/{v[1]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="bank26")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()
    table = build(load(a.tag))
    lines = ["| modelo | rota | raciocínio | status | conserto | armadilha | abstenção | US$/run | s (mediana) | servido por |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    order = {"FAZ-TUDO": 0, "CONSERTA+ARMADILHA": 1, "SO-CONSERTO": 2, "NAO-ATENDE": 3, "INFRA": 4}
    for t in sorted(table, key=lambda t: (order[t["status"]], t["cost_per_run"] if t["cost_per_run"] is not None else 9)):
        lines.append(f"| {t['model']} | {t['provider']} | {t['reasoning']} | {t['status']} | {fmt(t['fix'])} | "
                     f"{fmt(t['trap'])} | {fmt(t['abst'])} | {t['cost_per_run']} | {t['secs_median']} | "
                     f"{', '.join(t['served_by'])} |")
    md = "\n".join(lines)
    print(md)
    if a.md:
        open(a.md, "w", encoding="utf-8").write(md + "\n")
    json.dump(table, open(os.path.join(HERE, "planos", a.tag, "bank.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
