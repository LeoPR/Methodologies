---
title: F1 / M0 — abstenção: foregrounding do gate §9 conserta o falso-positivo (mas calibrar exige capacidade)
created: 2026-06-09
setup: forma M0 (abstenção-primeiro: veredito JÁ-BOM/PRECISA + só-se-precisar) vs AUDIT (controle "ache problemas") × 4 modelos (Opus, gemini-flash, gpt-4.1-mini, llama-70b) × 3 projetos reais (NNN exemplar=controle de abstenção, pdf2md, FG2P) × N=2 · pontuação CEGA (juiz Claude) contra gabaritos com veredito-verdade
status: M0 elimina o falso-positivo no exemplar (universal), mas super-corrige em sub-detecção nos fracos; abstenção CALIBRADA é capacidade (só Opus discrimina)
---

# F1 — a raiz do falso-positivo é a MOLDURA; calibrar é capacidade

O painel adversarial apontou que a falha dominante (falso-positivo em projeto real) é **não se
abster** — agir onde não devia. A Fase 1 testa: foregrounding do gate de abstenção (§9: "é
válido não achar nada") conserta isso?

## Resultado — NNN (exemplar, veredito-verdade = JÁ-BOM)

| forma | falso-pos | #ações | veredito JÁ-BOM | reconhece-bom |
|---|---|---|---|---|
| **M0 (abstenção)** | **1.00** | 1.62 | **8/8 ✓** | 1.00 |
| AUDIT (controle) | **5.38** | 5.62 | 0/8 | 0.50 |

**O M0 elimina a super-aplicação — e em TODOS os tiers**, inclusive os que mais alucinavam:
gpt-4.1-mini FP 8.0→1.0; llama-70b 4.5→**0.0**; gemini 5.5→2.5; Opus 3.5→0.5. Ou seja: **a
falha dominante do R8/P0/P6 era, em boa parte, a moldura "ache problemas"** forçando o modelo
a violar o próprio §9. Trocar a moldura conserta na raiz.

## O custo — sub-detecção (o "seguro e inútil")

Nos projetos que PRECISAM de trabalho, o M0 super-corrige:

| projeto (verdade) | M0 verdito-ok | AUDIT verdito-ok | M0 genuíno | AUDIT genuíno |
|---|---|---|---|---|
| pdf2md (PRECISA) | 0.38 | 1.00 | 1.00 | 1.88 |
| FG2P (PRECISA) | 0.12 | 1.00 | 0.25 | 1.75 |

Os modelos fracos passam a dizer "JÁ-BOM" para **tudo** (5/8 e 7/8 abstêm errado). O M0 trocou
um viés (agir-em-tudo) por outro (abster-em-tudo). É exatamente o "seguro e inútil" previsto.

## A discriminação é CAPACIDADE (o achado central)

Veredito sob M0, por modelo × projeto (certo: NNN=JÁ-BOM, pdf2md/FG2P=PRECISA):

| modelo | NNN | pdf2md | FG2P | discrimina? |
|---|---|---|---|---|
| **Opus** | JÁ-BOM ✓ | **PRECISA ✓✓** | JÁ-BOM/PRECISA (½) | **SIM** |
| gemini-flash | JÁ-BOM ✓ | PRECISA/JÁ-BOM (½) | JÁ-BOM ✗ | parcial |
| gpt-4.1-mini | JÁ-BOM ✓ | JÁ-BOM ✗ | JÁ-BOM ✗ | não (abstém em tudo) |
| llama-70b | JÁ-BOM ✓ | JÁ-BOM ✗ | JÁ-BOM ✗ | não (abstém em tudo) |

**Só o Opus usa a moldura M0 para genuinamente discriminar** (abster no bom, agir no que
precisa). Os fracos não distinguem — apenas invertem o viés. **Abstenção calibrada = capacidade**,
não moldura. (Mesmo tema do projeto inteiro, agora no eixo da abstenção.)

## Veredito (Fase 1)
1. **A moldura importa muito** — "ache problemas" é uma armadilha que força o falso-positivo;
   "abstenção-primeiro" (M0) o elimina no projeto bom, universalmente.
2. **Mas moldura desloca o viés; não instala discernimento.** Modelo fraco vai de over-aplicar
   a over-abster. **Calibrar (agir sse precisa) é capacidade** — só o topo (Opus) faz.
3. **Implicação de uso:** com modelo de topo, use M0/abstenção (dá julgamento calibrado). Com
   modelo fraco, escolha a moldura pelo RISCO: medo de ruído → M0; medo de perder coisa → audit;
   o ideal (ambos) exige o topo.

## Caveats
- N=2 por célula; 4 modelos; 3 projetos. Juiz Claude (cross-fornecedor validado no F0 — usar
  gemini-flash como 2º juiz é um próximo barato). "veredito" no audit é inferido pelo juiz.
