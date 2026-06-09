---
title: P7 — por camada (L0/L1/L2): a IA ENTENDE, APLICA, ou precisaria PESQUISAR?
created: 2026-06-08
setup: mineração das saídas F0-bare (método canônico completo) + sonda dedicada (explicar L0/L1/L2 + aplicar L1 a 3 necessidades + auto-reporte de necessidade de pesquisa) em 3 tiers — Opus 4.8, gpt-4.1-mini, deepseek-r1:8b local. Completion puro, SEM ferramentas/web.
status: esclarece a ambiguidade "a IA aplica L0/L1?" — entender NÃO é a barreira; os gargalos são JULGAMENTO (L0) e CONHECIMENTO (L1), distintos e capacidade-graduados
---

# P7 — entender ≠ aplicar, e por camada

Pergunta do dono: a IA não aplicou L0 e L1? Mesmo conceitualmente não entendeu a abstração de
L1/L2? E o eixo **treino vs capacidade de pesquisa** — verificamos? (Opus multimodal pesquisa?)

## O que tínhamos testado (e o que não)

Todos os testes anteriores (7 problemas do fixture; gabaritos reais; matriz P4) eram
**§2-§9 = camada L0**. Mediram **detecção de violação L0**. **L1 (nomear/aplicar formalizações)
e L2 (ferramentas) nunca foram pontuados.** Daí a ambiguidade.

## Quadro por tier × por camada (mineração F0-bare + sonda)

| | Opus (topo) | gpt-4.1-mini (médio) | deepseek-r1:8b (pequeno, local) |
|---|---|---|---|
| **Entende L0/L1/L2** (a abstração) | ✓ preciso | ✓ correto | ✓ correto (até "substituível") |
| **Aplica L0** (achar violação real) | ✓ bom | ✗ alucina/super-critica | ✗ alucina |
| **Aplica L1** (nomear a formalização madura) | ✓ ADR · Diátaxis · pré-registro (+ alternativas; separa L1 de L2) | ✗ **Blockchain** p/ decisões (desproporcional, §9); DITA em vez de Diátaxis | ✗ não NOMEIA — paráfrase genérica ("Fonte Única", "Doc por Padrão") |
| **Auto-reporte "preciso pesquisar?"** | calibrado: "nenhuma — só detalhes de ferramenta **L2** mereceriam verificação" | **overconfiante-errado**: "nenhuma" (mas errou) | **calibrado**: "precisaria PESQUISAR para nomear as formalizações" |

## Os achados

1. **Entender a abstração NÃO é a barreira.** Todos os tiers (até o llama-70b e o deepseek-r1
   pequeno) explicam L0/L1/L2 corretamente. A camada conceitual não é onde a IA falha.
2. **Há DOIS gargalos, distintos e por camada:**
   - **Julgamento (L0):** achar violação real sem inventar. Falha nos médios/pequenos
     (alucinam no projeto limpo). É **discernimento** — só o topo tem.
   - **Conhecimento (L1):** nomear a formalização madura certa. O pequeno **não sabe** (dá
     paráfrase); o médio **sabe mal** (Blockchain) e não percebe; o topo **sabe**.
3. **Treino vs pesquisa — a resposta direta (e diferenciada):**
   - Tudo foi **sem ferramentas/web**. O Opus acertou L0/L1 **do treino**; só **L2** (detalhes
     de ferramenta atual, que mudam) mereceria pesquisa — distinção que ele mesmo fez.
   - **Pesquisa é alavanca real, mas ESPECÍFICA:** ajudaria o **buraco de conhecimento** (o
     pequeno, bem-calibrado, que SABE que não sabe nomear a L1) — não o **buraco de julgamento**
     (o médio no L0, que erra confiante). Pesquisa não conserta discernimento.
   - **Nunca testamos o caminho com-pesquisa.** O Opus do P0 venceu sem ela. (O Opus no Claude
     Code pode pesquisar; não foi esse o caminho avaliado.)

## O que é "automático e garantido, independe de humano/IA"

- **Garantido (independe de tecnologia):** a **validade** do método (L0/L1) — fundamentada na
  literatura, aplicável por um humano cuidadoso **com ou sem IA**. Isso não depende de modelo.
- **Automático (IA sozinha):** **nada é plenamente garantido.** Entender é universal; *aplicar*
  exige julgamento (L0) + conhecimento (L1) que **escalam com capacidade**. Só um modelo de
  topo chega perto de aplicar o L0 de forma confiável — e ainda assim é **rascunho a revisar**.

## Próximo possível (não feito)
- Testar o caminho **com-pesquisa** (dar web/tools a um modelo pequeno bem-calibrado): a sonda
  prevê que ajuda o L1 (conhecimento), não o L0 (julgamento). Hipótese registrada.

## Caveats
- Sonda N=1, 3 tiers, 1 prompt. Mineração qualitativa das saídas F0-bare. Sem ferramentas.
