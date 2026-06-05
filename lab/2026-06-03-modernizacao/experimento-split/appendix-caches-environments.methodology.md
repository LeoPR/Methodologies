---
title: Apendice — caches e ambientes em pasta dedicada
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [versioning-git-hygiene.methodology.md, 00-core.methodology.md, bibliography.methodology.md]
---

# Apendice — caches e ambientes em pasta dedicada

> **Quando aplicar**: dia zero, qualquer projeto que produza arquivos
> efemeros/regeneraveis durante desenvolvimento. Vale tanto pra
> compilacao GCC (object files, ccache), quanto LaTeX (.aux, .log,
> .out, .bbl), Python (`__pycache__`, .pytest_cache, pip cache), R
> (renv), Rust (target/), Node (node_modules), datasets PyTorch /
> HuggingFace, Docker layers, Jupyter checkpoints, ou qualquer outra
> ferramenta que gere arquivo intermediario.

## Conceito universal — abstracao independente de ferramenta

### Definicao

Um **cache** (em sentido amplo) e qualquer artefato:

- **Regeneravel** — pode ser recriado a partir de fontes versionadas
- **Efemero** — vive enquanto util, descartavel depois
- **Nao-pertinente ao output** — meio, nao fim
- **Especifico de ambiente** — depende da maquina / OS / versao da ferramenta

Categorias universais:

| Categoria | Exemplos cross-tool |
|---|---|
| **Cache de fetch** | downloads de dependencias, datasets baixados |
| **Cache de parsing/analise** | `.pyc`, ASTs cacheados, type-check cache |
| **Build artifacts** | `.o`, `.class`, `dist/`, `build/`, `.aux` |
| **Ambiente isolado** | venv, conda env, `node_modules/`, `target/`, `.bundle/` |
| **Scratch / swap / temp** | reordenacao de arquivos massivos, dump intermediario, scratch space |
| **State de ferramenta** | `.idea/workspace.xml`, `.vscode/.ropeproject`, `.history/` |
| **Logs / instrumentation** | timing, profile, coverage |

### Principio FORTE — separar do projeto versionado

**Regra**: nada efemero/regeneravel entra no working tree versionado.
Tres niveis de separacao, ordenados por preferencia:

| Nivel | Estrategia | Quando |
|---|---|---|
| 1. **Pasta dedicada fora do projeto** | `Z:\caches\<tool>\`, `~/.cache/<tool>/`, drive separado | Maquina dedicada / single-user; melhor isolamento |
| 2. **Pasta dentro do projeto + `.gitignore`** | `.pytest_cache/`, `node_modules/` na raiz; ignorado | Padrao mais comum; tools default |
| 3. **Configuracao explicita do tool pra redirect** | env vars (`PIP_CACHE_DIR`, `XDG_CACHE_HOME`), config files | Quando nivel 1 nao e default mas voce quer |

**Por que importa**:
- Working tree limpo → `git status` mostra so o que importa
- Backup / sincronizacao (OneDrive, Dropbox) **nao** sincroniza cache
- Multiplos projetos compartilham mesma cache (pip, uv, npm shared)
- Limpeza trivial: `rm -rf <cache-dir>` sem risco pra fonte
- Reprodutibilidade: cache pode ser recriado; perde nada

> **Por que NAO commitar cache**: e' o mesmo "Signal vs ruido" definido em
> [versioning-git-hygiene](versioning-git-hygiene.methodology.md#signal-vs-ruido)
> — nao re-derivado aqui. Cache e' ruido (regeneravel/nao-pertinente).

### Cross-OS — onde caches "deveriam" viver por padrao

| OS | Convencao | Var de ambiente |
|---|---|---|
| Linux / BSD | `$XDG_CACHE_HOME` (default `~/.cache/<tool>/`) | XDG Base Dir Spec |
| macOS | `~/Library/Caches/<tool>/` | (XDG nao e nativo) |
| Windows | `%LOCALAPPDATA%\<tool>\Cache\` ou drive dedicado (Z:\) | `LOCALAPPDATA`, `TEMP` |

**Tools modernos respeitam XDG** mesmo em macOS/Windows quando voce
seta `XDG_CACHE_HOME`. Tools antigos plantam em `~/`. Tools de Windows
puro plantam em `%LOCALAPPDATA%`.

## Implementacoes praticas — per-tool (resumo + ponteiro)

> **Principio editorial aplicado**: cada tool ja' documenta suas env vars
> melhor que qualquer parafrase aqui (e elas mudam). Abaixo, so' a env var
> canonica de redirect por ecossistema. Implementacao concreta validada
> (Windows + Python; todos os caches em `Z:\caches\<tool>\`, venvs em
> `Z:\venvs\<proj>\` com junction `.venv` local):
> [`../../../dev-environment/README.md`](../../../dev-environment/README.md)
> (scripts `Initialize-ZPython.ps1` + `New-ZPythonProject.ps1`).

| Ecossistema | Env var de redirect / estrategia |
|---|---|
| Python interp / pip / uv | `PYTHONPYCACHEPREFIX`, `PIP_CACHE_DIR`, `UV_CACHE_DIR` |
| pytest / mypy / ruff / coverage | `cache_dir`, `MYPY_CACHE_DIR`, `RUFF_CACHE_DIR`, `COVERAGE_FILE` |
| venv / jupyter | path explicito + junction `.venv`; gitignore `.ipynb_checkpoints/` |
| LaTeX | `latexmk -outdir=build/` / `-auxdir=.aux/` |
| C/C++ | `CCACHE_DIR`; out-of-source `cmake -S . -B build/` |
| PyTorch / HuggingFace | `TORCH_HOME`, `HF_HOME` — datasets 100GB+ NUNCA no working tree |
| Node | npm/yarn `cache`/`cacheFolder`; pnpm store content-addressable |
| R / Rust / JVM | `R_LIBS_USER` / `CARGO_TARGET_DIR`,`CARGO_HOME` / `GRADLE_USER_HOME`,`-Dmaven.repo.local` |
| Docker | `dockerd --data-root=` + `docker system prune` |
| IDE | commit so' config compartilhavel; gitignore `.vscode/.history/`, `.idea/` (exceto `*.iml`/`vcs.xml`) |

**Regra unica** = "Signal vs ruido" (ver
[versioning-git-hygiene](versioning-git-hygiene.methodology.md#signal-vs-ruido))
aplicado a caches: nada efemero/regeneravel no working tree; redirecionar via
env var pra pasta dedicada (`Z:\caches\`, `$XDG_CACHE_HOME`/`~/.cache/`,
`%LOCALAPPDATA%`) ou gitignore. Detalhe operacional por tool: doc oficial de cada um.

## .gitignore — templates oficiais

Pra qualquer linguagem / tool, comece pelo template oficial em
[github.com/github/gitignore](https://github.com/github/gitignore).
Cobre 200+ ecossistemas (`Python.gitignore`, `Node.gitignore`,
`Rust.gitignore`, `LaTeX.gitignore`, `R.gitignore`, etc.).

**Pratica**: copie o template da linguagem principal + adicione
custom no final. Nao reinvente — comunidade ja iterou.

## Pre-commit hooks contra ruido

Adicione hook que falha commit se detectar:
- arquivos cache nao-ignorados (`__pycache__`, `.pytest_cache`, etc.)
- segredos em `.env` (ferramentas: `detect-secrets`, `git-secrets`)
- arquivos > limite (Git LFS sugere 100MB)

Ver [pre-commit.com](https://pre-commit.com/) +
[versioning-git-hygiene](versioning-git-hygiene.methodology.md).

## Antipatterns

| Antipattern | Sintoma | Antidoto |
|---|---|---|
| **Cache commitado** | `__pycache__/` em git log | `.gitignore` template oficial |
| **Venv commitado** | `.venv/` ou `venv/` no repo | `.gitignore` + recriar via `requirements.txt` / `pyproject.toml` |
| **Build commitado** | `dist/`, `build/`, `target/` no repo | `.gitignore` + script de build documentado |
| **Dataset gigante commitado** | clone leva 10min+ | LFS / storage externo / script de fetch |
| **Multiplos venvs por maquina** | `.venv1/`, `venv2/`, etc. | um por projeto; nome canonico `.venv` |
| **Cache global poluido** | `~/.cache/` cresce sem bound | `du -sh ~/.cache/*` + limpar periodicamente |
| **Tool config ignorado** | tool planta em working tree | env vars / config oficial pra redirect |
| **`gitignore` infla sem fim** | adiciona pattern toda semana | sintoma de tool plantando errado; redirect via config |

## Caso de uso real — referencia Windows + Python

Implementacao concreta validada:
[`../../../dev-environment/README.md`](../../../dev-environment/README.md)

- Setup global da maquina: `Z:\bin\Initialize-ZPython.ps1` (1x)
- Setup por projeto: `Z:\bin\New-ZPythonProject.ps1` (1x por projeto)
- Caches todos em `Z:\caches\<tool>\` (pip, uv, ruff, mypy, pytest, ipython, jupyter, etc.)
- Venvs em `Z:\venvs\<projeto>\` com junction `.venv` local
- Working tree do projeto **fica limpo** — so fontes + configs versionaveis

Outras stacks (Linux, macOS, R, Rust, Node) seguem mesmo principio
com paths diferentes — adapte das tabelas acima.
