#!/usr/bin/env python3
"""Congela um fixture: SHA256 combinado de (relpath + conteudo) de todos os arquivos,
em ordem estavel. Grava <dir>/.fixture-hash e imprime o hash. Uso:
  python hash_fixture.py fixtures/lumen-bugado
"""
import hashlib
import os
import sys


def hash_dir(d):
    h = hashlib.sha256()
    files = []
    for root, _, names in os.walk(d):
        for n in sorted(names):
            if n == ".fixture-hash":
                continue
            files.append(os.path.join(root, n))
    for p in sorted(os.path.relpath(x, d).replace("\\", "/") for x in files):
        full = os.path.join(d, p)
        h.update(p.encode("utf-8"))
        h.update(b"\0")
        with open(full, "rb") as f:
            h.update(f.read())
        h.update(b"\0")
    return h.hexdigest(), sorted(os.path.relpath(x, d).replace("\\", "/") for x in files)


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    digest, files = hash_dir(d)
    with open(os.path.join(d, ".fixture-hash"), "w", encoding="utf-8") as f:
        f.write(digest + "\n")
        for p in files:
            f.write(p + "\n")
    print(f"SHA256({d}) = {digest}")
    print(f"{len(files)} arquivos: {', '.join(files)}")
