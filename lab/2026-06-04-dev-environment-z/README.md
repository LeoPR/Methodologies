---
title: Metodologia dev-environment Z:\ — snapshot para estudo e formalização
status: open
created: 2026-06-04
tags: [dev-environment, python, uv, venv, vscode, caches, metodologia-importada, estudo]
phase: importado — estudo e aperfeiçoamento pendentes (prioridade atual é Estágio 1)
canonical-source: C:\Users\leona\OneDrive\Documents\dev-environment\ (VIVO — não mover)
---

# Metodologia dev-environment Z:\ — snapshot para estudo

> **Isto é uma CÓPIA de estudo, não o original.** A metodologia viva fica em
> `OneDrive\dev-environment\` e é operacional: os shims `Z:\bin\*.ps1` e o
> backup do OneDrive apontam para lá. **Mover quebraria o setup**; por isso foi
> copiada, não movida. Edições aqui são para estudo/formalização e NÃO afetam o
> ambiente real até serem deliberadamente promovidas de volta.

## O que está aqui

`snapshot-fonte/` — cópia verbatim (2026-06-04) de:
- `README.md` — caminho feliz operacional (setup, scripts, bugs, critério de pronto)
- `DETALHES-TECNICOS.md` — jornada de 17 turnos, bugs upstream, padrões descartados, ADRs
- `Initialize-ZPython.ps1` — setup global da máquina (1×)
- `New-ZPythonProject.ps1` — setup por projeto
- `Audit-Cleanliness.ps1` — auditoria declarativa de 51 itens

## Por que esta metodologia interessa ao projeto Methodologies

Ela já **evoluiu independentemente a mesma forma do Strata**, sem ter sido
escrita sob ele. Isso é evidência forte de que os padrões do Strata são
convergentes, não inventados:

| Elemento dev-environment | Equivalente no Strata |
|---|---|
| "Caminho feliz" (README, orientado ao que funciona) | núcleo estável / L0 |
| "Padrões já testados e descartados" (tabela com razão) | **sinal-de-troca** invertido (o que NÃO fazer e por quê) |
| "Decisões arquiteturais" (Considerei / Escolhi / Por quê) | **ADR/MADR** (§3 L1) |
| "Bugs upstream conhecidos (Microsoft)" | **vazio-tipado / fronteira-de-cobertura** (§6) — o que a metodologia NÃO controla |
| "Método científico de ablação aplicado" (1 var/vez) | o **dogfood** de §4 (registro científico) |
| "Status: validado por 4 ablações" + "qualquer revisão exige motivo novo" | **append-only ao traço** (§3) + economia (§9) |
| Histórico de revisões (17 turnos) | **versionamento como história imutável** (§8) |

Formalizá-la = mapear explicitamente sobre L0/L1/L2 e nomear as camadas que ela
já tem implícitas. Ela é candidata natural a virar um `recipe/` próprio no futuro
(ao lado do knowledge-architecture.md), OU o segundo caso de teste de transporte
do Strata.

## Achados da aplicação (2026-06-04) — primeira evidência de campo

Apliquei `New-ZPythonProject.ps1` ao projeto Methodologies (caminho feliz de
projeto novo: zero artefatos legados). Funcionou em 1 passada. Observações que
viram **agenda de aperfeiçoamento**:

### LACUNA 1 — git não é tratado (real, encontrada na prática)
A metodologia centraliza venvs em `Z:` para escapar do **OneDrive**, mas não
menciona o **git**. No umbrella Acadêmicos (allowlist com `!/Methodologies/`),
a junction `.venv` seria rastreada pelo git. Tive que criar `Methodologies/.gitignore`
à mão (`.venv/` + caches). **A metodologia deveria: ou o `New-ZPythonProject.ps1`
criar/emendar um `.gitignore`, ou o README documentar a regra.** É a mesma classe
de problema que ela já resolve para OneDrive — falta a simetria para git.

### LACUNA 2 — `uv init` deixa `main.py` stub
`uv init --no-readme` cria um `main.py` hello-world sem propósito num projeto que
é repositório de metodologia/instrumento. Removi à mão. Candidato: `uv init --bare`
(sem stub) quando o projeto não é uma aplicação empacotável, ou o script remover
o stub. **Sinal-de-troca**: `--bare` não cria `[project]` completo — verificar se
quebra o `uv add --dev` posterior.

### CONFIRMAÇÃO — o resto do caminho feliz se sustentou
Junction, pyproject com os 3 blocos canônicos, dev-deps pip/setuptools/wheel,
`.vscode/settings.json` de 1 chave, `uv sync`, pip resolvendo para Z: — tudo OK
sem intervenção. O "status estável" da metodologia se confirmou em campo.

## Agenda de aperfeiçoamento (para DEPOIS — não agora)

1. Mapear a metodologia sobre L0/L1/L2 do Strata explicitamente.
2. Fechar a LACUNA 1 (git) — decisão: script vs documentação.
3. Avaliar LACUNA 2 (`uv init --bare`) com ablação.
4. Formalizar o vocabulário (ela usa "caminho feliz", "ablação", "padrão
   descartado" — alinhar com os termos do Strata onde fizer sentido, sem forçar).
5. Decidir destino: recipe próprio, ou caso de transporte do Strata.

> **Prioridade atual**: voltar ao Estágio 1 do plano experimental
> (`../2026-06-04-economia-ia-tokens/plano-experimental.md`). O ambiente Python
> que esta metodologia configurou é o substrato em que o parser do Estágio 1 vai
> rodar — a aplicação dela foi pré-requisito, não desvio.
