#!/usr/bin/env python3
"""Guarda de pastas FROZEN (§8 do Strata, dogfood): falha se o commit STAGED cria, altera, apaga ou
renomeia qualquer arquivo dentro de uma pasta listada em tools/frozen-paths.txt.

Existe porque a regra "nunca editar registro congelado" vivia só em prosa (AGENTS.md); prosa orienta,
não garante (§5). A guarda vale para qualquer agente ou pessoa que commite, sem depender de ferramenta.

Uso:
  python tools/check_frozen.py            # checa o que está STAGED (modo pre-commit)
Ativar: chame a partir do pre-commit já configurado (ver tools/githooks/pre-commit).
Burlar 1 commit intencional:  git commit --no-verify
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def congeladas():
    out = []
    for ln in open(os.path.join(HERE, "frozen-paths.txt"), encoding="utf-8"):
        ln = ln.strip()
        if ln and not ln.startswith("#"):
            out.append(ln.rstrip("/") + "/")
    return out


def tocados():
    r = subprocess.run(["git", "diff", "--cached", "--name-status", "-M"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    caminhos = []
    for ln in r.stdout.splitlines():
        partes = ln.split("\t")
        caminhos += partes[1:]  # inclui origem e destino de renomeação
    return caminhos


def violacoes(caminhos, pastas):
    return sorted({c for c in caminhos for p in pastas if c.replace("\\", "/").startswith(p)})


def main():
    v = violacoes(tocados(), congeladas())
    if v:
        print("[frozen §8] o commit mexe em registro congelado (tools/frozen-paths.txt):")
        for c in v:
            print("   -", c)
        print("Abra um novo experimento datado em vez de editar o congelado (ou 'git commit --no-verify'"
              " se o dono decidiu descongelar).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
