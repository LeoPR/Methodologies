#!/usr/bin/env python3
"""aggregate_f4.py — cruza juiz (judge_f4) x mecanico (verify_f4) no F4. Confirma os achados-cabeca:
SUPER-ENG = defeito_alucinado? tombstone substantivo? propagou payload? + concordancia inter-juiz.
Uso: python aggregate_f4.py
"""
import collections
import glob
import json
import os

import verify_f4 as v

HERE = os.path.dirname(os.path.abspath(__file__))
J = json.load(open(os.path.join(HERE, "planos", "f4-judge", "judgments.json"), encoding="utf-8"))
MODS = ["gpt-4o-mini", "gemini-2.5-flash", "gpt-4.1"]


def msh(m):
    return m.split("/")[-1]


# juiz: agrupa por fix (nao-self preferido)
by = collections.defaultdict(list)
for r in J:
    if "verdict" in r:
        by[(r["fixture"], r["arm"], msh(r["model"]), r["run"])].append(r)


def disp(rows):
    ns = [x for x in rows if not x["is_self"]] or rows
    ds = [x["verdict"].get("disposicao") for x in ns]
    return ds, ns


print("=== (A) JUIZ x MECANICO por fixture x arm x modelo ===")
for fix in ["f4-dup", "f4-clean", "f4-trap"]:
    for arm in ["strata", "base"]:
        line = f"{fix:9} {arm:6} "
        for m in MODS:
            mech, jud = [], []
            for f in sorted(glob.glob(os.path.join(HERE, "planos", f"f4-{fix}-{arm}", f"plano-{m.replace('/','_')}*-F4-r*.md"))):
                mr = v.classify(os.path.join(HERE, "cenarios", fix), v._manifest(fix), open(f, encoding="utf-8").read())
                mech.append(mr["verdict"].replace("FALHA_", "").replace("INDETERMINADO-", "IND-")[:8])
            for run in (1, 2):
                rows = by.get((fix, arm, m, run))
                if rows:
                    ds, _ = disp(rows)
                    jud.append("/".join(sorted({d[:8] for d in ds})))
            line += f"{m[:7]}: mec[{','.join(mech)}] juiz[{','.join(jud)}]  "
        print(line)

print("\n=== (B) CONFIRMACAO DOS ACHADOS-CABECA ===")


def frac(fixture, arm, key):
    rows = [r for r in J if "verdict" in r and r["fixture"] == fixture and r["arm"] == arm and not r["is_self"]]
    n = len(rows)
    t = sum(1 for r in rows if r["verdict"].get(key))
    return t, n


# 1. SUPER-ENG na clean+Strata = defeito alucinado?
t, n = frac("f4-clean", "strata", "defeito_alucinado")
print(f"  f4-clean/Strata defeito_alucinado (super-eng real): {t}/{n}")
t, n = frac("f4-clean", "base", "defeito_alucinado")
print(f"  f4-clean/baseline defeito_alucinado:                {t}/{n}")
# 2. tombstone substantivo no trap+Strata
t, n = frac("f4-trap", "strata", "tombstone_substantivo")
print(f"  f4-trap/Strata tombstone_substantivo:               {t}/{n}")
# 3. propagou payload (trap) — deve ser baixo no Strata
t, n = frac("f4-trap", "strata", "propagou_payload")
print(f"  f4-trap/Strata propagou_payload (deve ~0):          {t}/{n}")
t, n = frac("f4-trap", "base", "preservou_historia")
print(f"  f4-trap/baseline preservou_historia:                {t}/{n}")
# 4. proporcional na dup+Strata
t, n = frac("f4-dup", "strata", "proporcional")
print(f"  f4-dup/Strata proporcional:                         {t}/{n}")

print("\n=== (C) CONCORDANCIA INTER-JUIZ (gpt-4o-mini, 2 juizes nao-self) ===")
agr = tot = 0
for key, rows in by.items():
    ns = [x for x in rows if not x["is_self"]]
    if len(ns) < 2:
        continue
    ds = [x["verdict"].get("disposicao") for x in ns]
    tot += 1
    agr += len(set(ds)) == 1
print(f"  disposicao: {agr}/{tot} = {agr / tot:.0%}" if tot else "  (sem pares nao-self)")
err = sum(1 for r in J if "error" in r)
print(f"  (self: {sum(1 for r in J if r.get('is_self'))} | erros: {err} | total: {len(J)})")
