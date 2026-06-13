---
title: 'RESULTADOS F5 — eixo PESQUISA (web/§6): a fonte primária e o carimbo alucinado'
created: 2026-06-13
status: 'probe EXPLORATÓRIO (1 fixture, 2 modelos ±web, N=1-2, ~US$0,14). Sinal forte: web reduz verificação-alucinada.'
---

# F5 — um modelo que pesquisa verifica melhor a fonte (§6)?

**Fixture `f5-verif`:** um projeto com **3 afirmações técnicas FALSAS** sobre formalizações que o Strata
referencia — Diátaxis "= 3 tipos" (erro: são **4**, inclui *explanation*); pace layering "Brand **2001**"
(erro: **1999**, *The Clock of the Long Now*); Conventional Commits "exige `change:`" (erro: usa **feat/fix/…**).
**Tarefa §6:** verificar cada uma contra a fonte → CORRETA / INCORRETA / NÃO-VERIFICÁVEL. **Web** ligado pelo
sufixo `:online` (OpenRouter; **sem MCP**). Probe exploratório (N=1-2). Custo ~US$0,14.

## Resultado — "carimbos" (dizer CORRETA a uma afirmação FALSA = §6 falhou)
| Modelo | sem web | com web |
|---|---|---|
| gemini-2.5-flash | ~**1,5**/3 carimbos | **0** |
| gpt-4.1 | **3/3** (carimbou tudo, até o `change:` fabricado) | **2** |

## Achados
1. **Sem web, a verificação de fonte (§6) FALHA feio — até no forte.** O `gpt-4.1` carimbou as **3** falsas
   como corretas (verificação **alucinada** — "confirmou" o que não checou). É a fraqueza prevista no
   [dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md) (fonte primária), agora demonstrada.
2. **Web REDUZ a verificação-alucinada** (gemini 1,5→0; gpt-4.1 3→2). O ganho é sobretudo **honestidade**:
   com web, o gemini **pega com citação** (Diátaxis=4, com links reais) **ou abstém** (NÃO-VERIFICÁVEL) — em
   vez de carimbar. **Web não torna onisciente; faz parar de fingir.**
3. **Hipótese (P7) parcialmente confirmada:** pesquisa ajuda o eixo **conhecimento/§6**, não o julgamento L0.
   Dá substância à intuição do dono — *modelo que lê as referências tem vantagem* (aqui, deixa de carimbar).

## Limite (§6)
Exploratório: **1 fixture, 3 claims, N=1-2, 2 modelos**. Direção forte, não cravo. Generalizar pede mais
claims/modelos (e o web do `:online` traz fontes de qualidade variável — ver os links citados pelo gemini).
