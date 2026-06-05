---
title: Versionamento e higiene de repositorio
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [00-core.methodology.md, appendix-caches-environments.methodology.md, bibliography.methodology.md]
---

# Versionamento e higiene de repositorio (foundational)

> **Quando aplicar**: dia zero. Mesmo solo sem publicar remoto,
> **`git init`** — ganha auditoria, branching, recuperabilidade.
> Custo: 0.
>
> **Tool-agnostico**: doc usa "git" por dominancia 2026; principios
> valem pra mercurial / fossil / svn / jj / sucessores. Sintaxe muda;
> disciplina continua.

## Signal vs ruido — o que entra no repo

<a id="signal-vs-ruido"></a>

> **Fonte unica deste conceito.** Outros docs da suite (ex:
> [appendix-caches-environments](appendix-caches-environments.methodology.md))
> linkam para ca' em vez de re-derivar.

**Entra** (signal — define o projeto):
codigo, docs, configs, lock files (`uv.lock`, `package-lock.json`,
`Cargo.lock`), datasets pequenos representativos, scripts pra
**recriar** o que nao entra.

**Nao entra** (ruido — regeneravel ou nao-pertinente):
builds (`dist/`, `*.o`, `*.pyc`), caches (`__pycache__/`,
`node_modules/`, `.pytest_cache/`), outputs regeneraveis pelo
`run.py`, datasets gigantes externos, logs/dumps, credentials/`.env`,
arquivos de editor (`.vscode/` pessoal, `.idea/`, `*.swp`),
**versoes manuais** (`relatorio_v2.md`, `script_old.py`).

## Antipattern critico — versionamento manual

**Nao crie** `arquivo_v2.md`, `script_old.py`, `backup_2026_05_10/`.
Git ja' versiona: `git log` mostra historico; `git show` recupera;
`git diff` compara; `git tag` marca versao. Versoes manuais poluem
repo + duplicam conteudo + geram drift inevitavel.

**Excecao**: artefato explicitamente imutavel (ADR aceito, EXP-NNN
frozen, release publicada). Ai' "v2" e' **nova decisao formal**,
nao backup informal.

## .gitignore como contrato

Cada projeto declara explicitamente o que **nao** versiona. Templates
oficiais por linguagem em
[github.com/github/gitignore](https://github.com/github/gitignore)
(cobre Python, Node, Rust, R, Julia, MATLAB, LaTeX, etc.).

**Regra**: se voce sempre ignora o mesmo arquivo em `git status`,
**adicione ao `.gitignore`**. Working tree limpo = sinal saudavel.

## Arquivos grandes — escolher estrategia, nao commitar por reflexo

| Caso | Estrategia |
|---|---|
| Dataset reproduzivel via download | script `scripts/fetch_data.py` + `.gitignore`; repo so' tem o script |
| Dataset intermediario processado | storage externo (S3, NAS, drive separado) referenciado via `config/storage.json` |
| Binario unico nao-reproduzivel (HW especifico, medicao unica, build de toolchain rara) | **Git LFS** ou archive externo + checksum + README do artefato (data, ambiente, como foi gerado) |
| Modelo ML treinado (~GB) | LFS, HuggingFace Hub, ou **DVC** (Data Version Control) |

(2026: alem de DVC, considerar **lakeFS** / **Quilt** para versionamento
de dados/modelos em escala — object storage versionado tipo git; ver
[bibliography](bibliography.methodology.md).)

**Regra**: artefato grande **so'** entra se for unico-irrecuperavel.
Tudo que pode ser recriado fica fora; **o script de recriacao entra**.

## Higiene de commits

Refs em [bibliography](bibliography.methodology.md) (Pro Git; Tim Pope;
Conventional Commits). Operacional:

- **1 commit = 1 mudanca atomica logica**. Refator + feature + fix
  juntos = ruim; separe.
- **Commit message**: tipo (`feat:`, `fix:`, `docs:`...) + titulo
  curto + paragrafo com *por que* (o *que* esta no diff).
- **Nao commitar codigo quebrado em main**. WIP vai em branch.
- **Squash vs merge**: time decide; documente politica.

## Branching — escolha um modelo, documente

| Modelo | Quando usar | Ref |
|---|---|---|
| **Trunk-based development** | Equipe pequena, CI forte, deploy continuo | [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/) |
| **GitHub Flow** | Open source / SaaS com releases simples | [GitHub docs](https://docs.github.com/en/get-started/using-git/github-flow) |
| **Git Flow** | Releases com hotfix branches, versionamento forte | [Driessen 2010](https://nvie.com/posts/a-successful-git-branching-model/) |

Documente a escolha em `CONTRIBUTING.md` ou ADR — evita drift quando
entra colaborador novo.

## Colaboracao multi-pessoa — minimo viavel

- **PR / MR review** pra mudancas em main (humano + opcional review por IA)
- **Branch protection** em main (forca PR; bloqueia direct push; CI passa antes)
- **CODEOWNERS** — quem revisa o que automaticamente
- **Pre-commit hooks** ([pre-commit.com](https://pre-commit.com/))
  — lint / format / test antes de commit local; evita CI falhar por trivialidade
- **Signed commits** (GPG/SSH) — em academico publicavel ou regulatorio
- **Docs no repo, com o codigo** — nao em Drive/Notion separado; doc
  e' artefato versionado igual a codigo, sofre PR review igual

## Reprodutibilidade — o teste fundamental

**Pergunta**: posso clonar este repo em maquina nova e reproduzir o
estado de trabalho em **≤ 3 comandos**?

```
git clone <repo>
cd <repo>
./scripts/setup.sh && ./scripts/run.py
```

Se sim → repo saudavel. Se nao → tem dependencia implicita em algo
nao-versionado (config local, dataset perdido, ambiente
nao-documentado, toolchain especifica). Identifique e enderece — ou
documente como excecao legitima (ver "arquivos grandes" acima).

## Mesmo solo, sem remoto: use git

Recomendacao **forte** mesmo em projeto de 1 pessoa, sem publicacao remota:

- `git init` + `.gitignore` desde dia 1
- Commits frequentes = save points implicitos
- Branch pra experimento arriscado (`git checkout -b try-X`) — descartar
  e' barato
- `git log` vira diario tecnico automatico, ordenavel/buscavel
- `git reflog` salva apos desastre (arquivo deletado, branch perdida,
  reset acidental)

**Push remoto opcional**: GitHub / GitLab / Codeberg / self-hosted
adicionam backup off-site + colaboracao + CI. Sem publicar, repo
local + backup do disco continua util.

## Antipatterns de versionamento

| Antipattern | Sintoma | Antidoto |
|---|---|---|
| **"Final final v3"** | nome manual de versao | `git tag` + commit message |
| **Commit gigante "wip"** | 200 arquivos sem foco | atomic commits |
| **`git push --force` em main** | reescreve historia compartilhada | so' em branch propria; nunca em main |
| **Segredo commitado** | API_KEY em git log | `.env` + `.gitignore` + git-secrets / detect-secrets pre-commit |
| **Dataset gigante commitado** | clone leva 10min | LFS / storage externo + script de fetch |
| **Cache/build versionado** | `dist/` em git | `.gitignore` (ver [appendix-caches-environments](appendix-caches-environments.methodology.md)) |
| **Branch eterna** | feature-X com 6 meses sem merge | merge ou descarte (drift cresce com tempo) |
| **Commit message vago** | "fix stuff", "wip", "." | tipo + descricao |
| **Doc em Drive separado do codigo** | drift; review duplicado | doc no repo, sempre |
| **Toolchain implicita** | "funciona na minha maquina" | `pyproject.toml` + lock file + Dockerfile / nix / devcontainer |

## Referencias

Ver [bibliography](bibliography.methodology.md) → "Versionamento e
higiene de repositorio".
