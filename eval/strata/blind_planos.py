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
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", nargs="+", default=["clean-prose", "clean-an", "clean-baseline"])
    ap.add_argument("--out", default="clean-blind")
    ap.add_argument("--key", default="clean-key.json")
    ap.add_argument("--prefix", default="P")
    a = ap.parse_args()
    out_dir = os.path.join(PLANOS, a.out)
    key_path = os.path.join(PLANOS, a.key)
    items = []
    for arm in a.arms:
        for p in glob.glob(os.path.join(PLANOS, arm, "plano-*-F1-r*.md")):
            m = NAME.search(os.path.basename(p))
            txt = open(p, encoding="utf-8").read()
            body = HEADER.sub("", txt).strip()
            items.append({"arm": arm, "model": m.group(1), "run": int(m.group(2)), "body": body})
    # ordem estavel e embaralhada: por hash do corpo (esconde a ordem arm/model)
    items.sort(key=lambda it: hashlib.sha256(it["body"].encode("utf-8")).hexdigest())
    os.makedirs(out_dir, exist_ok=True)
    key = {}
    for i, it in enumerate(items, 1):
        oid = f"{a.prefix}{i:02d}"
        open(os.path.join(out_dir, f"{oid}.md"), "w", encoding="utf-8").write(it["body"])
        key[oid] = {"arm": it["arm"], "model": it["model"], "run": it["run"], "bytes": len(it["body"])}
    json.dump(key, open(key_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{len(items)} planos anonimizados -> {out_dir}")
    print(f"chave -> {key_path} (NAO dar aos pontuadores)")


if __name__ == "__main__":
    main()
