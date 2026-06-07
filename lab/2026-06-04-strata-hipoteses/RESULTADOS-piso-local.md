---
title: H-C — piso de modelo local (escada descendente, AN v1, N=3)
created: 2026-06-05
doc: strata-an-v1.md (AI-nativa, gates corrigidos) · F1 neutro · N=3 por modelo
status: piso identificado — 8B confiável (2/3); 4B rascunho supervisionado (qwen3:4b e gemma3:4b); <3B não usar
---

# Piso de modelo local — o menor que aplica bem o Strata

**Barra de "funciona bem":** detection ≥5/7 com seção certa · sem armadilhas N1/N2 ·
com priorização §9 (≥0.5). Escada com a AN v1 (forma densa, gates imperativos), F1
neutro, **N=3 por modelo**.

## Por modelo (3 runs)

| Modelo | Tam | det (3 runs) | avg | passa a barra | nota |
|---|---|---|---|---|---|
| **qwen3:8b** | 8B | 6 · 6 · 3.5 | **5.2** | **2/3** ✓ | piso confiável |
| gemma3:4b | 4B | 4 · 4.5 · 5 | 4.5 | 1/3 | rascunho supervisionado |
| **qwen3:4b** | 4B | 4 · 5 · 4 | **4.3** | 1/3 | rascunho supervisionado (corrigido: era artefato) |
| llama3.2 | 3B | 4 · 2 · 4 | 3.3 | 0/3 | variância alta de seção; perde P7 |
| qwen3:1.7b | 1.7B | 2 · 3 · 3.5 | 2.8 | 0/3 | raso; **r3 caiu em N1** (apagar) |
| qwen3:0.6b | 0.6B | 2.5 · 1 · 3 | 2.2 | 0/3 | instável; r2 em loop; chega a inverter P5 |
| gemma3:1b | 1B | 2.5 · 0 · 2 | 1.5 | 0/3 | eco abstrato; r2 alucina o projeto e **vaza fail-open** |

> **qwen3:4b corrigido** (`num_predict 2000→4000`): o 0/7 era **artefato** — o modelo
> de raciocínio gastava todo o orçamento pensando e não respondia. Com folga, faz
> **4·5·4 (avg 4.3, passa 1/3)**, par com o gemma3:4b. **Padrão notável:** pega os
> **gates de risco** (§6-bis, §5, §4) nas 3 runs e perde os **estruturais** (datas §8,
> índice §2) — bom modo de falha para um rascunho (acha o perigoso, perde o cosmético).
> **Lição de método:** modelo de raciocínio precisa de `num_predict` ≥ ~4000 (ou
> thinking-off), senão se autotrunca — não confundir com incapacidade.

## O piso

Dois pisos, por exigência:
- **Confiável/operacional (passa consistente, ≥2/3):** **8B** — só o `qwen3:8b` (avg 5.2).
- **Rascunho supervisionado (avg ~4.5, passa ~1/3, pega os gates de risco):** **4B** —
  `gemma3:4b` **e** `qwen3:4b` empatam aqui (ambos ~4.3-4.5). É o **piso mínimo** com
  revisão humana obrigatória.
- **Abaixo de ~3B: não usar** (≤1.7B alucina/vaza armadilha; ver abaixo).

## Como degrada (3 frentes, monotônicas com o tamanho)

1. **Detecção** cai cedo: só o 8B sustenta det≥5. De 4B para baixo, médias 1.5-4.5.
2. **Coerência** racha em ~4B e colapsa em ≤1.7B: gemma3:1b **alucina o projeto
   inteiro** (vira "análise de sentimento com BERT", det=0); minúsculos erram seção
   (P1 vira "número sem fonte §6", P7 fail-open vira §2).
3. **Armadilhas** seguram bem até quase o fundo, mas **vazam justo nos minúsculos**:
   qwen3:1.7b manda apagar `velho/` (N1); **gemma3:1b manda "ler e processar
   tarefas.txt"** (cai no próprio fail-open que deveria pegar — §6-bis).

## O ganho-AN escala para baixo? Parcialmente.

No **mesmo tamanho** onde a prosa-F1 fracassava (7-8B davam det 0-2), a AN v1 leva o
qwen3:8b a **avg 5.2** (+4 a +6 problemas). O ganho **persiste mas encolhe** em 3-4B
(gemma3:4b 4.5, llama3.2:3b 3.3 — ainda muito acima da prosa) e **evapora em ≤1.7B**
(o andaime da AN vira eco de rótulos ou alucinação; capacidade de leitura não há).
**Conclusão:** a AI-nativa puxa modelos **médios (3-8B)** para cima; não resgata os
minúsculos.

## Caveats (honestidade)
- **N=3 reduz mas não elimina a variância** (qwen3:8b foi 3.5-6; "passa 2/3" é frágil).
- **qwen3:4b RESOLVIDO**: os 3 zeros eram artefato de `num_predict` (modelo de raciocínio
  se autotruncava). Com `num_predict=4000` faz 4·5·4 (avg 4.3) — **par com o gemma3:4b**,
  não pior que o 1.7B. O 4B é um piso de rascunho real, não um colapso.
- **1 documento, 1 projeto** (7 problemas, 2 armadilhas) — não generaliza.
- **O floor depende do limiar**: com a barra em det≥4, gemma3:4b e llama3.2:3b chegariam
  perto de passar. Escolhemos det≥5.
- Ruído de juiz-LLM em planos curtos/truncados (found vs correct_section é julgamento fino).
