#!/usr/bin/env python3
"""Constroi um DIGEST de um repo EXTERNO (open-source de terceiro) p/ o braco externo do Strata
(quebra a circularidade do projeto-proprio). Clona raso, extrai os arquivos relevantes p/ ORGANIZACAO
(capado), computa SINAIS DE CONFORMIDADE OBJETIVOS (README/LICENSE/tests/pyproject/CI/...) — para
classificar o tier sem julgamento subjetivo —, e grava em external-fixtures/<name>/ (GITIGNORED).
Etica: local/privado; publicar so AGREGADO, nunca expor/criticar o repo nominalmente.
Uso: python build_ext_digest.py --repo <url> --name <name> --tier bem-comportado
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
KEEP = ["README*", "readme*", "LICENSE*", "COPYING*", "pyproject.toml", "setup.py", "setup.cfg",
        "tox.ini", "CHANGELOG*", "CHANGES*", "HISTORY*", "CONTRIBUTING*", "Makefile",
        "requirements*.txt", ".pre-commit-config.yaml", "mkdocs.yml", "Cargo.toml", "package.json"]
CAP_FILE = 18000
CAP_TOTAL = 45000
SKIP_DIRS = {".git", "__pycache__", ".tox", ".venv", "node_modules", ".mypy_cache", "dist", "build"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--tier", default="?")
    a = ap.parse_args()
    tmp = tempfile.mkdtemp()
    src = os.path.join(tmp, "r")
    subprocess.run(["git", "clone", "--depth", "1", "-q", a.repo, src], check=True)

    def has(pat):
        return bool(glob.glob(os.path.join(src, pat)) or glob.glob(os.path.join(src, "**", pat), recursive=True))
    sig = {
        "README": has("README*") or has("readme*"),
        "LICENSE": bool(glob.glob(os.path.join(src, "LICENSE*")) or glob.glob(os.path.join(src, "COPYING*"))),
        "pkg_meta": has("pyproject.toml") or has("setup.py") or has("setup.cfg") or has("Cargo.toml") or has("package.json"),
        "tests": bool(glob.glob(os.path.join(src, "tests")) or glob.glob(os.path.join(src, "test")) or glob.glob(os.path.join(src, "**", "test_*.py"), recursive=True)),
        "CI": bool(glob.glob(os.path.join(src, ".github", "workflows", "*"))),
        "CHANGELOG": has("CHANGELOG*") or has("CHANGES*") or has("HISTORY*"),
        "CONTRIBUTING": has("CONTRIBUTING*"),
    }
    score = sum(1 for v in sig.values() if v)
    out = os.path.join(HERE, "external-fixtures", a.name)
    os.makedirs(out, exist_ok=True)

    total = 0
    for pat in KEEP:
        for f in sorted(glob.glob(os.path.join(src, pat))):
            if not os.path.isfile(f):
                continue
            dst = os.path.join(out, os.path.basename(f))
            if os.path.exists(dst):
                continue
            txt = open(f, encoding="utf-8", errors="replace").read()[:CAP_FILE]
            if total + len(txt) > CAP_TOTAL:
                break
            open(dst, "w", encoding="utf-8").write(txt)
            total += len(txt)

    tree = []
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel = os.path.relpath(root, src)
        if rel != "." and rel.count(os.sep) > 2:
            dirs[:] = []
            continue
        for fn in sorted(files)[:40]:
            tree.append((rel + "/" + fn).lstrip("./").replace("\\", "/"))
    open(os.path.join(out, "STRUCTURE.md"), "w", encoding="utf-8").write(
        "# Estrutura do projeto\n" + "\n".join("- " + p for p in sorted(tree)[:200]))

    # .meta.json e' OCULTO (read_target ignora dotfiles) — nao vaza os sinais no prompt
    json.dump({"repo": a.repo, "name": a.name, "tier": a.tier, "conformidade": sig, "score": score},
              open(os.path.join(out, ".meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"{a.name:24} conformidade {score}/7  {sig}")


if __name__ == "__main__":
    raise SystemExit(main())
