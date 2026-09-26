---
title: Estágio 5 — encaixe de modelo por placa (poucos pontos medidos, projeção para o mercado)
created: 2026-09-26
updated: 2026-09-26
status: executado 2026-09-26 (5 modelos × 2 contextos na RTX 3060; projeção para 9 placas)
hardware: NVIDIA RTX 3060 12GB, Windows 10, desktop vivo (~1,1 GB de VRAM de fundo), 64 GB de RAM
instrumento: fit_encaixe.py (mede) + projeta_encaixe.py (projeta); pontos em encaixe_pontos_2026-09-26.json
---

# Estágio 5 — encaixe por placa

> **Pergunta:** "se alguém tem uma 4090, qual modelo cabe?". Responde-se sem comprar placas:
> mede-se **poucos pontos** na placa que existe (a 3060) e projeta-se para o resto pelas
> primitivas do [mapa](../mapa-recursos-llm.md): **capacidade de rodar = pesos + KV cabem na
> VRAM?**, e **velocidade de decode batch-1 = limitada pela banda de memória**.

## Por que existe (a separação capacidade × viabilidade)

Decidido pelo dono em 2026-08-02 ([PLANO §3-bis do reteste](../../2026-08-02-reteste-L0-fechado/PLANO.md),
[NOTAS](../../2026-08-02-reteste-L0-fechado/NOTAS-shakedown.md)): a **capacidade** de um modelo (o
que ele entrega) é propriedade dos **pesos** e se mede na nuvem, barato e rápido, num substituto
com os mesmos pesos; a máquina local mede só a **viabilidade** (cabe? a que velocidade?) e serve de
**contra-prova** numa ponte de 1–2 células rodadas nos dois lados. Este estágio fecha o lado da
viabilidade: "o projeto rodou bem no modelo X" (medido na nuvem) vira "e o modelo X cabe na placa Y
a tal velocidade" (medido aqui ou projetado).

## Método

1. `fit_encaixe.py` carrega cada modelo no Ollama em **dois contextos** (8k e 32k), gera 200 tokens
   com pensamento desligado e lê: `size` e `size_vram` (`/api/ps`), decode e prefill
   (`eval_count/eval_duration`, como o [`bench_decode.py`](bench_decode.py)), a arquitetura
   (`/api/show`) e a VRAM do desktop antes de carregar. Descarrega entre medições.
2. `projeta_encaixe.py` ajusta, por modelo medido, a reta `memória(ctx) = base + KV × ctx`
   (Achado 1 do [STAGE2](STAGE2.md): o KV cresce linear com o contexto), calibra a eficiência de
   banda nos pontos que cabem inteiros, e projeta para placas de mercado a 32k (o método inteiro
   no prompt pede ~32k).

## Achados

- **O KV depende da arquitetura de atenção, não do tamanho.** qwen3:8b (atenção completa) ganha
  3,5 GB de 8k para 32k; gemma4:12b (janela deslizante) praticamente não cresce; qwen3.8:27b e
  qwen3.6:35b-a3b (atenção híbrida) crescem pouco. Uma regressão única "KV ~ tamanho" dá R² 0,24:
  não serve. Modelo não medido herda o KV da família medida; sem família, vira faixa.
- **Na 3060, o método inteiro no prompt tem teto em ~12B denso.** qwen3:14b a 32k ocupa 15 GB,
  faz offload e cai de 34 para 14 tok/s.
- **Denso grande com offload é inviável; MoE com offload é viável.** qwen3.8:27b (denso) cai para
  ~5 tok/s; qwen3.6:35b-a3b (MoE, ~3B ativos) mantém ~30 tok/s com 14 GB fora da GPU.
- **Eficiência de banda nos densos que cabem: 0,82** (mediana de 5 pontos). Não vale para MoE: o
  modelo "banda / bytes ativos" superestima muito a velocidade deles, que fica só a medida.

## Pontos medidos e projeção (saída de `projeta_encaixe.py`)

## Ajuste (placa de referencia RTX 3060 12GB, banda 360 GB/s)

- fundo do desktop medido: 1.10 GB de VRAM antes de carregar o modelo
- fator base (memoria fixa / arquivo): 0.98
- KV por token ~ arquivo (so para mostrar que NAO serve de regra): R2 = 0.24, n=5; o KV depende da arquitetura de atencao
- eficiencia de banda (mediana, 5 pontos que cabem inteiros): 0.82

| modelo medido | arquivo GB | KV MB/1k tok | memoria @8k | memoria @32k | decode tok/s (3060) | offload? |
|---|---|---|---|---|---|---|
| qwen3:8b | 5.2 | 144 | 6.3 | 9.8 | 56.27 / 57.02 | não |
| gemma4:12b | 7.6 | 0 | 8.4 | 8.1 | 37.01 / 36.16 | não |
| qwen3:14b | 9.3 | 189 | 10.3 | 15.0 | 33.56 / 13.98 | sim |
| qwen3.8:27b | 17.7 | 43 | 18.3 | 19.4 | 5.35 / 4.96 | sim |
| qwen3.6:35b-a3b | 23.9 | 23 | 23.3 | 23.9 | 29.52 / 29.68 | sim |

## Projeção @ 32k de contexto (o Strata inteiro no prompt pede ~32k)

| modelo | memória @ctx GB | origem | RTX 4060 8GB | RTX 3060 12GB | RTX 4070 12GB | RTX 4060 Ti 16GB | RTX 5060 Ti 16GB | RTX 4070 Ti Super 16GB | RTX 3090 24GB | RTX 4090 24GB | RTX 5090 32GB |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3:8b | 9.8 | medido | offload | cabe · ~56 tok/s | cabe · ~79 tok/s | cabe · ~45 tok/s | cabe · ~70 tok/s | cabe · ~105 tok/s | cabe · ~146 tok/s | cabe · ~158 tok/s | cabe · ~280 tok/s |
| gemma4:12b | 8.4 | medido | offload | cabe · ~39 tok/s | cabe · ~54 tok/s | cabe · ~31 tok/s | cabe · ~48 tok/s | cabe · ~73 tok/s | cabe · ~101 tok/s | cabe · ~109 tok/s | cabe · ~194 tok/s |
| qwen3:14b | 15.0 | medido | offload | offload | offload | offload | offload | offload | cabe · ~82 tok/s | cabe · ~89 tok/s | cabe · ~158 tok/s |
| qwen3.8:27b | 19.4 | medido | offload | offload | offload | offload | offload | offload | cabe · ~43 tok/s | cabe · ~46 tok/s | cabe · ~82 tok/s |
| qwen3.6:35b-a3b (MoE) | 23.9 | medido | offload | offload | offload | offload | offload | offload | offload | offload | cabe |
| gemma4:26b (26B-A4B) (MoE) | 18.6 | projetado (KV da família gemma4:12b) | offload | offload | offload | offload | offload | offload | cabe | cabe | cabe |
| gemma-4-31b | 19.6 | projetado (KV da família gemma4:12b) | offload | offload | offload | offload | offload | offload | cabe · ~38 tok/s | cabe · ~41 tok/s | cabe · ~73 tok/s |
| gpt-oss:20b (MoE) | 13.7–26.4 | projetado (faixa: KV desconhecido) | offload | offload | offload | talvez (medir) | talvez (medir) | talvez (medir) | talvez (medir) | talvez (medir) | cabe |
| nemotron-3.5-lightning 30B-A3B (MoE) | 24.5–47.1 | projetado (faixa: KV desconhecido) | offload | offload | offload | offload | offload | offload | offload | offload | talvez (medir) |
| muse-glimmer:30b | 17.6–33.9 | projetado (faixa: KV desconhecido) | offload | offload | offload | offload | offload | offload | talvez (medir) | talvez (medir) | talvez (medir) |
| gpt-oss:120b (MoE) | 63.6–122.3 | projetado (faixa: KV desconhecido) | offload | offload | offload | offload | offload | offload | offload | offload | offload |
| deepseek-v4-flash (284B-A13B) (MoE) | 80.8–155.3 | projetado (faixa: KV desconhecido) | não | não | não | não | não | não | não | não | offload |

Hipóteses: decode batch-1 limitado por banda (velocidade só para densos: a eficiência foi calibrada em densos e superestima MoE, cuja velocidade fica só a medida); Q4_K_M; KV f16; offload não extrapolado (lento; medido só na 3060); RAM p/ offload 64 GB; 'cabe' exige memória + fundo do desktop ≤ VRAM. Projetados: KV da família medida quando há; senão uma faixa de só-pesos até pesos + pior KV medido (atenção completa); 'talvez (medir)' = cabe no limite inferior e não no superior: é caso para uma sonda local.

## Limites

- Uma placa de referência (3060, Windows com desktop vivo). O fundo do desktop e o "penhasco" do
  WDDM ([STAGE2](STAGE2.md), Achado 2) mudam de máquina para máquina.
- Tamanhos de arquivo e parâmetros dos modelos não baixados vêm da biblioteca do Ollama e dos model
  cards (lab/2026-09-26-banco-modelos); bandas das placas são especificação de fabricante.
- "talvez (medir)" é o convite à próxima sonda: carregar o modelo e ler `size` a 32k.
