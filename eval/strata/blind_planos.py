#!/usr/bin/env python3
"""Anonimiza planos para pontuacao CEGA: remove o header <!-- model=... -->, embaralha
de forma deterministica (por hash do conteudo) e grava ids opacos + uma chave a parte.
Uso: python blind_planos.py clean-prose clean-an clean-baseline
Saida: planos/clean-blind/<id>.md (sem metadado)  +  planos/clean-key.json (id->arm/model)."""
import glob
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
OUT = os.path.join(PLANOS, "clean-blind")
KEY = os.path.join(PLANOS, "clean-key.json")
HEADER = re.compile(r"^<!--.*?-->\s*", re.DOTALL)
NAME = re.compile(r"plano-(.+)-F1-r(\d+)\.md$")


def main():
    arms = sys.argv[1:] or ["clean-prose", "clean-an", "clean-baseline"]
    items = []
    for arm in arms:
        for p in glob.glob(os.path.join(PLANOS, arm, "plano-*-F1-r*.md")):
            m = NAME.search(os.path.basename(p))
            txt = open(p, encoding="utf-8").read()
            body = HEADER.sub("", txt).strip()
            items.append({"arm": arm, "model": m.group(1), "run": int(m.group(2)), "body": body})
    # ordem estavel e embaralhada: por hash do corpo (esconde a ordem arm/model)
    items.sort(key=lambda it: hashlib.sha256(it["body"].encode("utf-8")).hexdigest())
    os.makedirs(OUT, exist_ok=True)
    key = {}
    for i, it in enumerate(items, 1):
        oid = f"P{i:02d}"
        open(os.path.join(OUT, f"{oid}.md"), "w", encoding="utf-8").write(it["body"])
        key[oid] = {"arm": it["arm"], "model": it["model"], "run": it["run"], "bytes": len(it["body"])}
    json.dump(key, open(KEY, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{len(items)} planos anonimizados -> {OUT}")
    print(f"chave -> {KEY} (NAO dar aos pontuadores)")


if __name__ == "__main__":
    main()
