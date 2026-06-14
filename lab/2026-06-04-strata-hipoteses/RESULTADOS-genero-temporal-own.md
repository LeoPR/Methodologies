---
title: 'RESULTADOS — GÊNERO + TEMPORAL em 2 projetos de curso do dono (sonda cega vs gabarito pré-registrado)'
created: 2026-06-13
status: 'probe (2 projetos próprios, 2 modelos, 1-2 runs). Sinal FORTE com framing+marcadores explícitos — mas CIRCULAR (quase auto-avaliação). Ver ressalva.'
---

# Gênero + Temporal — AulaQuantum & DeepLearning (sonda cega contra gabarito pré-registrado)

> **Leia primeiro a ressalva de circularidade** ([gabarito](GABARITO-genero-temporal-own.md)): projeto +
> analista + autor-do-método são da mesma família (Leonardo + Claude). Isto **não é braço independente**;
> mede se o modelo **lê gênero/tempo como o autor lê**, **não** se o método é válido.

## Setup
Digest só da **camada de organização** (sem conteúdo acadêmico, gitignored) dos dois projetos de
acompanhamento-de-aula → gabarito **pré-registrado e commitado ANTES** da sonda (gênero esperado, padrões
que importam, veredito esperado **JÁ-BOM-PARA-O-GÊNERO** nos dois, 5 armadilhas negativas N1–N5). Sonda
cega = gemini-2.5-flash + gpt-4.1, tarefas **gênero** e **temporal** (o gabarito **não** vai no prompt).

## Eixo GÊNERO (4 saídas)
| Projeto × modelo | gênero inferido | exige CI/tests/LICENSE? | veredito |
|---|---|---|---|
| AulaQuantum × gemini | notas/aula/tutorial ✓ | **NÃO** (explícito) ✓ | JÁ-BOM-PARA-O-GÊNERO ✓ |
| AulaQuantum × gpt-4.1 | notas/aula/tutorial ✓ | **NÃO** (explícito) ✓ | JÁ-BOM-PARA-O-GÊNERO ✓ |
| DeepLearning × gemini | notas/aula/tutorial ✓ | **NÃO** (explícito) ✓ | JÁ-BOM-PARA-O-GÊNERO ✓ |
| DeepLearning × gpt-4.1 | notas/aula/tutorial ✓ | **NÃO** (explícito) ✓ | JÁ-BOM-PARA-O-GÊNERO ✓ |

**4/4 batem o gabarito**: gênero certo, veredito certo, **nenhum** exigiu CI/LICENSE/tests (N3 evitado).

## Eixo TEMPORAL (4 saídas — gemini re-rodado a 4000 tok p/ não truncar)
| Projeto × modelo | N1 DELETADO≠perda | N2 9e10≠duplicata | N5 preserva old/ | tombstone lido como organização | veredito temporal |
|---|---|---|---|---|---|
| AulaQuantum × gemini | n/a | ✓ (não chamou dup) | ✓ (old/=arquivo; só o *conteúdo* sensível sai) | ✓ (tickets/old/REORG/tools retirados) | COERENTE (c/ lacunas menores) |
| AulaQuantum × gpt-4.1 | n/a | ✓ | ✓ (histórico mantido p/ rastreio) | ✓ | COERENTE |
| DeepLearning × gemini | ✓ ("tombstone eficaz/ponteiro") | n/a | n/a | ✓ (dataset/.venv/week6/derivados) | COERENTE |
| DeepLearning × gpt-4.1 | ✓ ("correto, rastreável") | n/a | n/a | ✓ ("nenhum defeito evidente") | COERENTE |

**Nenhuma das 5 armadilhas negativas (N1–N5) foi acionada em nenhuma das 8 sondas.** Tombstone/arquivamento/
supersessão foram lidos como **organização correta**, não como defeito — o ponto-cego §3/§8 **não disparou**
quando o framing pede situar-no-tempo **e** o projeto tem marcadores explícitos.

## True positives (não são falso-positivo gênero-cego)
Os modelos **não ficaram cegos nem paranoicos** — pegaram coisas reais:
- **`[arquivo-redigido]` em `[redigido]/`** (dado pessoal sensível) — gemini achou nos dois eixos. **E**
  notou que o ticket `T010_apagar_[redigido]_e_duplicatas` está **fechado** → provavelmente **já resolvido na
  árvore viva** (o digest está velho). ⚠️ **Vale você conferir** (ver nota de ação abaixo).
- **PDF duplicado na raiz** (`Semana1_1st_Overview_Part1a.pdf`) — ticket `T213` aberto.
- **Drift de status na Semana 1** (gemini): ticket `T201` fechado, mas `VERIFICACAO_SEMANA1.md` (posterior)
  diz "incompleta" → "completude pode ter sido só administrativa". Achado temporal **fino e legítimo**.

## Assimetria pré-registrada (AulaQuantum > DeepLearning no tempo) — captada implicitamente
As timelines de AulaQuantum saíram **muito mais ricas** (ticket-a-ticket, datas, detecção do drift de status),
porque o projeto tem **VCS + ledger de tickets + datas**; as de DeepLearning ficaram em **nível de fase**
(assets 1-5 vs 6 + README + train_log), e **nenhum** modelo inventou um CHANGELOG/VCS que DL não tem.
A assimetria aparece na **granularidade** — consistente com o gabarito. *(Caveat: cada run viu só um projeto;
não houve juiz cross-projeto comparando-os de frente.)*

## Leitura honesta — o que isto mostra e o que NÃO mostra
- **Mostra:** com **framing gênero/tempo-consciente** + **marcadores explícitos** (`DELETADO — recriável`,
  datas, estados de ticket, `old/`), os modelos leem gênero e tempo **corretamente** e **não** super-exigem
  software-standards nem confundem tombstone com defeito. Reforça [`RESULTADOS-genero`](RESULTADOS-genero.md).
- **NÃO mostra (3 limites duros):**
  1. **Circularidade** — projeto+analista+autor da mesma família; é quase auto-avaliação. Convergência
     gabarito↔sonda é esperada **por construção** (o dono organizou os cadernos no estilo do método). **Não
     valida o Strata.**
  2. **Bar baixo** — aqui os marcadores temporais são **explícitos**. O ponto-cego original (DOSSIÊ/H-D) é
     **inferir o tempo SEM marcadores** ("nome-simples=velho / cópia=nova"). Ler `DELETADO — recriável` certo
     é bem mais fácil que isso — **esse teste mais duro segue não feito** (F6).
  3. **N pequeno** (2 projetos, 2 modelos, 1-2 runs); sem juiz independente; completion-only.
- **Saldo:** sinal **forte mas restrito** — "modelos fazem leitura gênero/tempo-consciente de projetos
  bem-marcados quando perguntados". Útil como *capability check*, não como prova de método nem de generalização.

## Nota de ação (mundo real, fora da metodologia)
⚠️ Há indício de **[redigido] (dado pessoal) versionado** em `[redigido]/` no digest.
O ticket `T010` aparece **fechado** (provável remoção já feita), mas **confirme** que `[arquivo-redigido]`
não está mais rastreado no git (inclusive no **histórico** — se já foi commitado, precisa de purge, não só rm).
