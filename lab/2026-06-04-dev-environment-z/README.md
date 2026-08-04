---
title: dev-environment Z:\ — snapshot da plataforma de desenvolvimento
status: open
created: 2026-06-04
updated: 2026-08-04
tags: [dev-environment, python, uv, venv, vscode, caches, metodologia-importada, estudo]
phase: registro lateral de infraestrutura; fora do conteúdo metodológico
canonical-source: fonte operacional externa ao repositório (VIVA — não mover)

# dev-environment Z:\ — snapshot da plataforma de desenvolvimento

> **Isto é uma CÓPIA de estudo, não o original.** A metodologia viva fica em
> fora deste repositório e é operacional: os shims locais e o backup da máquina
> apontam para lá. **Mover quebraria o setup**; por isso foi
> copiada, não movida. Edições aqui são apenas registro e NÃO afetam o ambiente
> real.

> **Revisão da fonte viva (2026-08-03):** a autoridade, os documentos superados e
> as pendências L2 foram reavaliados em
> [`../2026-08-03-dev-environment-revisao/REVISAO-2026-08-03.md`](../2026-08-03-dev-environment-revisao/REVISAO-2026-08-03.md).
> O snapshot abaixo continua a representar somente a captura de 2026-06-04.

## O que está aqui

`snapshot-fonte/` — cópia verbatim (2026-06-04) de:
- `README.md` — caminho feliz operacional (setup, scripts, bugs, critério de pronto)
- `DETALHES-TECNICOS.md` — jornada de 17 turnos, bugs upstream, padrões descartados, ADRs
- `Initialize-ZPython.ps1` — setup global da máquina (1×)
- `New-ZPythonProject.ps1` — setup por projeto
- `Audit-Cleanliness.ps1` — auditoria declarativa de 51 itens

## Relação com o projeto Methodologies

Este ambiente foi usado para desenvolver e executar partes do projeto. Isso o
torna contexto operacional e, quando necessário, informação de reprodução. Não o
torna conteúdo do Strata nem evidência de que o método funciona.

| Organização observada na plataforma | Vocabulário usado para descrevê-la |
|---|---|
| "Caminho feliz" (README, orientado ao que funciona) | núcleo estável / L0 |
| "Padrões já testados e descartados" (tabela com razão) | **sinal-de-troca** invertido (o que NÃO fazer e por quê) |
| "Decisões arquiteturais" (Considerei / Escolhi / Por quê) | **ADR/MADR** (§3 L1) |
| "Bugs upstream conhecidos (Microsoft)" | **vazio-tipado / fronteira-de-cobertura** (§6) — o que a metodologia NÃO controla |
| "Método científico de ablação aplicado" (1 var/vez) | o **dogfood** de §4 (registro científico) |
| "Status: validado por 4 ablações" + "qualquer revisão exige motivo novo" | **append-only ao traço** (§3) + economia (§9) |
| Histórico de revisões (17 turnos) | **versionamento como história imutável** (§8) |

Esta tabela descreve a plataforma com um vocabulário disponível no projeto. Não
é uma comparação de produtos, teste de transporte ou resultado experimental.

## Observações operacionais da configuração (2026-06-04)

`New-ZPythonProject.ps1` foi usado para configurar o projeto Methodologies
(caminho de projeto novo: zero artefatos legados). Funcionou em uma passada. As
observações abaixo pertencem à manutenção da plataforma externa:

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

## Manutenção fora deste projeto

As lacunas de `.gitignore`, `uv init --bare` e coerência entre scripts e
documentação devem ser resolvidas na fonte viva. Este repositório só precisa
registrar mudanças que afetem materialmente a reprodução de seus executáveis.

> **Prioridade atual**: voltar ao Estágio 1 do plano experimental
> (`../2026-06-04-economia-ia-tokens/plano-experimental.md`). O ambiente Python
> que esta metodologia configurou é o substrato em que o parser do Estágio 1 vai
> rodar — a aplicação dela foi pré-requisito, não desvio.
