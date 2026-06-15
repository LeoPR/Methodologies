#!/usr/bin/env python3
"""Guarda de carimbo (§3/§8 do Strata, dogfood): falha se um .md com frontmatter
'updated:' foi MODIFICADO mas o 'updated:' nao aponta para HOJE.

Existe porque o bump manual do 'updated:' apodrece (propagacao por memoria — o modo de
falha que o ADR-005 nomeia). Mecaniza a checagem em vez de confiar na lembranca.

Uso:
  python tools/check_stamps.py            # checa o que esta STAGED (modo pre-commit)
  python tools/check_stamps.py --working  # checa o working tree vs HEAD

Ativar como hook:  git config core.hooksPath tools/githooks
Burlar 1 commit intencional:  git commit --no-verify
"""
import datetime
import re
import subprocess
import sys


def sh(args):
    return subprocess.run(args, capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


def main():
    working = "--working" in sys.argv
    rng = [] if working else ["--cached"]
    today = datetime.date.today().isoformat()
    diff = sh(["git", "diff", "--name-status"] + rng)
    bad = []
    for line in diff.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, path = parts[0], parts[-1]
        if not path.endswith(".md") or not status.startswith("M"):
            continue  # so .md MODIFICADO (novos/renomeados nao contam)
        try:
            txt = open(path, encoding="utf-8", errors="replace").read(4000)
        except OSError:
            continue
        fm = txt.split("---")
        if len(fm) < 3:
            continue  # sem frontmatter -> sem carimbo a cobrar (datado pelo git)
        m = re.search(r"(?m)^updated:\s*(\d{4}-\d{2}-\d{2})", fm[1])
        if not m:
            continue  # frontmatter sem campo 'updated:' -> fora do escopo
        if m.group(1) != today:
            bad.append((path, m.group(1)))
    if bad:
        sys.stderr.write(f"\n[carimbo §3/§8] .md modificado com 'updated:' nao-hoje ({today}):\n")
        for path, d in bad:
            sys.stderr.write(f"   - {path}  (updated: {d})\n")
        sys.stderr.write("Bumpe o 'updated:' para hoje (ou 'git commit --no-verify' se for intencional).\n\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
