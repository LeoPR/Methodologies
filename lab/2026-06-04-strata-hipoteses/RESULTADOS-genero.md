---
title: 'RESULTADOS — eixo GÊNERO: gênero-consciência é alcançável com o framing certo (resolve o confundidor do messy)'
created: 2026-06-13
status: 'probe (3 repos externos, 3 gêneros, 2 modelos, N=1). Sinal: com framing gênero-consciente, os modelos NÃO são gênero-cegos.'
---

# Gênero — o modelo aplica o padrão CERTO para o gênero?

O tier **messy externo** levantou o confundidor: **baixa-conformidade ≠ defeito** (lista/pesquisa não precisa
de tests/CI). Aqui, um prompt **gênero-consciente** (identifique o gênero → avalie pelo padrão DELE; não exija
o que não se aplica) em 3 repos **externos** de gêneros distintos: `ml3months` (lista/notas, conf. 1/7), `tomli`
(biblioteca, 6/7), `mlscratch` (pesquisa/lib). × gemini-2.5-flash / gpt-4.1. **N=1.**

## Resultado
| Repo (gênero) | gênero reconhecido | exige tests/CI? | veredito |
|---|---|---|---|
| ml3months (lista/notas) | **lista / notas** ✓ | **NÃO** (ambos) ✓ | JÁ-BOM-para-o-gênero |
| tomli (biblioteca) | **biblioteca** ✓ | sim (apropriado) | JÁ-BOM-para-o-gênero |
| mlscratch (pesquisa) | "biblioteca" (fronteira fuzzy) | gemini sim / gpt-4.1 não | JÁ-BOM-para-o-gênero |

## Leitura — resolve o confundidor do messy
Quando o framing pede o **padrão-do-gênero**, os modelos **não são gênero-cegos**: numa **lista**, dizem
"já-boa" e **não exigem testes/CI**. Logo a ambiguidade do tier messy (o M0 "JÁ-BOM" no repo 1/7 = sub-detecção
**ou** genre-appropriate?) **inclina para genre-appropriate** — o "JÁ-BOM" era, em parte, **reconhecimento de
gênero correto**, não só viés de abstenção. *(Reabilita parcialmente o tier messy: menos "sub-detecção", mais "fit de gênero".)*

## Implicação para o método (loop narrativa↔resultado)
O **§9 deveria ser gênero-consciente** explicitamente: *"aplique o padrão DO GÊNERO; não exija software-standards
(testes/CI/empacotamento) de notas/listas/pesquisa."* É melhoria de **narrativa** (proporcionalidade por gênero),
barata, e ataca o confundidor na raiz — entra no backlog de reescrita do §9.

## Limites (§6)
- **Capability COM framing gênero-explícito** — **não** o default (M0/audit não perguntam gênero; a
  gênero-consciência *por padrão* segue não-testada).
- N=1, 3 repos, 2 modelos; "exige-tests" por regex crua; `mlscratch` gênero-fuzzy (lib vs pesquisa).
- **AulaQuantum / DeepLearning** (gênero *acompanhamento-de-aula*, do dono) precisam de um **digest fornecido
  pelo dono** (não tenho acesso a projetos locais) para testar a **generalização de gênero na prática** + o
  **eixo temporal** (notas evoluem → liga ao F6/dossiê). Protocolo pronto (este runner + gabarito por gênero).
