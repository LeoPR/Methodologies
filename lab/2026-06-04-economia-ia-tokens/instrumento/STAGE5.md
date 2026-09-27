---
title: Estágio 5 — encaixe de modelo por placa (poucos pontos medidos, projeção para o mercado)
created: 2026-09-26
updated: 2026-09-26
status: executado 2026-09-26 (5 modelos × 2 contextos na RTX 3060; projeção para 9 placas e 2 máquinas de memória unificada)
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

"offload" para a RAM de sistema (PC com GPU dedicada) não é projetado: nesta tabela vira "não"; os
pontos com offload medidos na 3060 estão na primeira tabela.

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

| modelo | memória @ctx GB | origem | RTX 4060 8GB | RTX 3060 12GB | RTX 4070 12GB | RTX 4060 Ti 16GB | RTX 5060 Ti 16GB | RTX 4070 Ti Super 16GB | RTX 3090 24GB | RTX 4090 24GB | RTX 5090 32GB | GB10 128GB unificada | Ryzen AI Max+ 395 (96GB GPU) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3:8b | 9.8 | medido | não | cabe · ~56 tok/s | cabe · ~79 tok/s | cabe · ~45 tok/s | cabe · ~70 tok/s | cabe · ~105 tok/s | cabe · ~146 tok/s | cabe · ~158 tok/s | cabe · ~280 tok/s | cabe · ~43 tok/s | cabe · ~40 tok/s |
| gemma4:12b | 8.4 | medido | não | cabe · ~39 tok/s | cabe · ~54 tok/s | cabe · ~31 tok/s | cabe · ~48 tok/s | cabe · ~73 tok/s | cabe · ~101 tok/s | cabe · ~109 tok/s | cabe · ~194 tok/s | cabe · ~30 tok/s | cabe · ~28 tok/s |
| qwen3:14b | 15.0 | medido | não | não | não | não | não | não | cabe · ~82 tok/s | cabe · ~89 tok/s | cabe · ~158 tok/s | cabe · ~24 tok/s | cabe · ~23 tok/s |
| qwen3.8:27b | 19.4 | medido | não | não | não | não | não | não | cabe · ~43 tok/s | cabe · ~46 tok/s | cabe · ~82 tok/s | cabe · ~13 tok/s | cabe · ~12 tok/s |
| qwen3.6:35b-a3b (MoE) | 23.9 | medido | não | não | não | não | não | não | não | não | cabe | cabe | cabe |
| gemma4:26b (26B-A4B) (MoE) | 18.6 | projetado (KV da família gemma4:12b) | não | não | não | não | não | não | cabe | cabe | cabe | cabe | cabe |
| gemma-4-31b | 19.6 | projetado (KV da família gemma4:12b) | não | não | não | não | não | não | cabe · ~38 tok/s | cabe · ~41 tok/s | cabe · ~73 tok/s | cabe · ~11 tok/s | cabe · ~10 tok/s |
| gpt-oss:20b (MoE) | 13.7–26.4 | projetado (faixa: KV desconhecido) | não | não | não | talvez (medir) | talvez (medir) | talvez (medir) | talvez (medir) | talvez (medir) | cabe | cabe | cabe |
| nemotron-3.5-lightning 30B-A3B (MoE) | 24.5–47.1 | projetado (faixa: KV desconhecido) | não | não | não | não | não | não | não | não | talvez (medir) | cabe | cabe |
| muse-glimmer:30b | 17.6–33.9 | projetado (faixa: KV desconhecido) | não | não | não | não | não | não | talvez (medir) | talvez (medir) | talvez (medir) | cabe · ~12 tok/s | cabe · ~12 tok/s |
| gpt-oss:120b (MoE) | 63.6–122.3 | projetado (faixa: KV desconhecido) | não | não | não | não | não | não | não | não | não | talvez (medir) | talvez (medir) |
| deepseek-v4-flash (284B-A13B), IQ1_S (MoE) | 80.8–155.3 | projetado (faixa: KV desconhecido) | não | não | não | não | não | não | não | não | não | talvez (medir) | talvez (medir) |
| deepseek-v4-flash (284B-A13B), ~3-bit (MoE) | 117.5–225.9 | projetado (faixa: KV desconhecido) | não | não | não | não | não | não | não | não | não | não | não |
| deepseek-v4.1-flash (552B+Engram), Q2_K (MoE) | 258.9–497.9 | projetado (faixa: KV desconhecido) | não | não | não | não | não | não | não | não | não | não | não |

Hipóteses: decode batch-1 limitado por banda (velocidade só para densos: a eficiência foi calibrada em densos e superestima MoE, cuja velocidade fica só a medida); Q4_K_M; KV f16; offload não extrapolado (lento; medido só na 3060); RAM p/ offload 0 GB; 'cabe' exige memória + fundo do desktop ≤ VRAM. Projetados: KV da família medida quando há; senão uma faixa de só-pesos até pesos + pior KV medido (atenção completa); 'talvez (medir)' = cabe no limite inferior e não no superior: é caso para uma sonda local.

## Parcimônia (o que se mede e o que se aceita)

Gemma 4 tem tabela oficial de memória (docs do Google, 2026-07-08; Q4_0 com 20% de folga): 12B
6,7 GB, 26B-A4B 14,4 GB, 31B 17,5 GB. As tags padrão do Ollama são maiores (gemma4:26b, 19 GB); a
projeção usa as tags do Ollama porque é o que se roda.

Especificação de fonte primária notória se aceita sem re-medir: tamanho do arquivo, janela de
contexto, arquitetura de atenção, contagem de parâmetros. Mede-se só o que nenhuma documentação dá
para esta máquina: o fundo do desktop, o overhead do runtime e a inclinação do KV que calibra a
fórmula. Por isso bastaram cinco modelos em dois contextos. Onde o fabricante já declara o encaixe,
vale a declaração: a OpenAI anunciou o gpt-oss-20b como capaz de rodar com 16 GB de memória (anúncio
de 2025-08-05); com o fundo do desktop medido aqui, ele fica no limite de uma placa de 16 GB. Uma
sonda local só se justifica se isso for decidir uma compra.

## Máquinas de memória unificada (GB10, Ryzen AI Max+ 395)

Máquinas em que CPU e GPU dividem um pool grande de memória lenta: o **NVIDIA GB10** (DGX Spark e
similares de outros fabricantes; 128 GB LPDDR5x, pool inteiro disponível à GPU, 273 GB/s; a NVIDIA
suporta ligar até quatro unidades, para modelos de até 700B parâmetros) e o **AMD Ryzen AI Max+ 395** ("Strix Halo"; até 128 GB, dos quais até
96 GB viram VRAM, 256 GB/s). Fonte: páginas dos fabricantes (NVIDIA DGX Spark; AMD Ryzen AI Max+
395), acesso em 2026-09-26.

- **Muita memória, pouca banda.** Cabe muito mais que numa placa de 24 GB, mas um denso decodifica
  ~3–4× mais devagar que numa 4090 (qwen3.8:27b: ~12–13 tok/s projetados, contra ~46). O ponto forte
  dessas máquinas são os **MoE grandes com poucos parâmetros ativos**.
- **Parcimônia nas faixas.** Onde a coluna mostra faixa, vale a declaração primária quando existe: o
  gpt-oss-120b cabe numa GPU de 80 GB (OpenAI), logo cabe nas duas; o DeepSeek V4 usa atenção
  comprimida e KV em FP4 (model card), logo o KV é pequeno e vale o limite inferior da faixa.
- **DeepSeek.** V4-Flash em 1-bit (82,5 GB) cabe numa unidade; um relato de campo confirma experts em
  2 bits num nó só a 29,9 tok/s. O V4.1-Flash roda em aglomerados de GB10 (ver a correção no caso
  abaixo).
- **Velocidade de MoE no GB10 (calibração externa).** Um relato de campo de um colega do dono
  (aglomerado de GB10 em produção, set/2026) dá dois pontos: DeepSeek-V4-Flash, experts em 2 bits,
  1 nó: **29,9 tok/s**; GLM-5.2 (753B, ~45B ativos, experts em 2 bits), 2 nós: **16,2 tok/s**, que
  caía para 1,2 tok/s quando o KV grande empurrava os pesos para o disco. Pela conta de bytes lidos
  por token, os dois dão eficiência de banda de **~0,4** para MoE, contra 0,82 dos densos medidos
  aqui. A conclusão do relato é a mesma deste estágio: no GB10 manda a banda (273 GB/s) e os bytes
  por token, não o tamanho do modelo.

## Caso: DeepSeek V4.1-Flash em casa (consulta de 2026-09-26)

> **Correção (mesma data, horas depois).** A primeira versão desta seção dizia que o V4.1-Flash não
> rodava localmente em placa nenhuma, nem num par de GB10, e que não havia runtime. Estava
> desatualizada: as fontes eram de 10 a 13/09, o próprio dia do lançamento, e o terreno mudou em dias.
> O vLLM passou a suportar o V4.1 (PRs mesclados em 10 e 11/09; primeira versão estável, a v0.30.0,
> em 22/09), e a comunidade publicou
> receitas para GB10 que deixam a memória Engram **no NVMe** em vez de na memória, técnica que a
> estimativa não considerava. Números medidos (receitas da comunidade, set/2026):
>
> | montagem | como cabe | decode | situação |
> |---|---|---|---|
> | 2× GB10 | experts em 2 bits (EXL3), Engram no NVMe, KV de 8 GiB por nó | 33–40 tok/s (com decodificação especulativa) | receita publicada |
> | 3–4× GB10 | experts no formato nativo (MXFP4), Engram no disco | não conferido | receitas vLLM e SGLang |
> | 1× GB10 | experts mais usados residentes (74–87 GB), o resto lido do NVMe (~0,9 GB por token) | ~2,6 tok/s | em andamento; degenera depois de ~2.000 tokens |
>
> Continua valendo: não roda em placa de vídeo de consumo, e não há suporte no llama.cpp nem no
> Ollama local (ver a verificação abaixo; MLX não conferido); não achei receita para o Ryzen AI Max+ 395. O texto abaixo fica como estava, por
> rastreabilidade.
>
> Medições de terceiros: repositórios dos próprios autores
> (github.com/sfxnz/DeepSeek-V4.1-Flash-EXL3-vLLM-2x-DGX-Spark; github.com/0xBakeer/deepseek-v41-flash-spark);
> relato de campo de um colega do dono. Estado dos runtimes e das máquinas: ver a verificação abaixo.

### Verificação em fonte primária (2026-09-26)

A correção acima veio de analisar no lugar de verificar. Por isso cada fato desta seção e da de
memória unificada foi reconferido **só em fonte primária** (repo oficial, model card do fabricante,
página de especificação, docs oficiais):

| afirmação | veredito | fonte primária |
|---|---|---|
| vLLM suporta o V4.1-Flash | confirmado: PRs #56208, #56214 e #56228 mesclados em 10–11/09 (o #56201 foi **fechado sem merge**); primeira versão estável v0.30.0, 2026-09-22 | github.com/vllm-project/vllm (PRs e release v0.30.0) |
| SGLang suporta o V4.1-Flash | parcial: só imagens de prévia (`dev-dsv41`); o PR #38798 foi mesclado em 18/09 mas não está na v0.5.20 | cookbook oficial do sgl-project; API de comparação do GitHub |
| llama.cpp suporta o V4.1-Flash | não: PR #28696 aberto; o master vai até DeepSeek V4; forks não oficiais existem | github.com/ggml-org/llama.cpp |
| Ollama roda o V4.1-Flash localmente | não: só `deepseek-v4.1-flash:cloud` | ollama.com/library/deepseek-v4.1-flash/tags |
| GB10: 128 GB, 273 GB/s | confirmado; até 200B por unidade; até 4 unidades ligadas para 700B (página do produto); 405B em duas (guia do usuário, 2026-09-10) | nvidia.com (DGX Spark); docs.nvidia.com/dgx/dgx-spark |
| Ryzen AI Max+ 395: 128 GB, 96 GB de VRAM, 256 GB/s | confirmado (LPDDR5x-8000, 256 bits; 96 GB via VGM no Windows) | amd.com (ficha técnica; blogs de 2025-03-17 e 2025-07-29) |
| DeepSeek-V4-Flash: 284B, 13B ativos | confirmado (experts FP4, resto FP8) | huggingface.co/deepseek-ai/DeepSeek-V4-Flash |
| DeepSeek-V4.1-Flash: 552B + 196B Engram, 8B/16B ativos | confirmado | huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash |

Tamanhos de quantização GGUF do V4.1 citados no texto abaixo vêm de guia de terceiros e não têm
valor prático enquanto o llama.cpp não suportar o modelo.

O V4.1-Flash fez tudo no banco (nuvem). Localmente, não roda hoje em nenhuma placa, por dois
motivos independentes:

- **Memória.** 552B de parâmetros no tronco mais 196B de memória "Engram" (763B no checkpoint), com
  8B ativos no prefill e 16B no decode; já sai em FP8/FP4 (fonte primária: model card no Hugging
  Face). As quantizações da comunidade vão de 264,5 GB (Q2_K) a 444,7 GB (Q4_K_M) e 508 GB (Q8_0).
  Em servidor, via SGLang: ~286 GiB nos aceleradores mais ~190 GiB de RAM para o Engram. A maior
  placa de consumo (5090) tem 32 GB; a única máquina de caixa única que comporta o Q2_K é um Mac
  com 512 GB de memória unificada.
- **Software.** Arquitetura nova, sem suporte nos runtimes de uso doméstico: nada no llama.cpp
  principal nem no MLX; o Ollama só oferece a versão na nuvem; vLLM com pull request aberto e
  SGLang só em prévia. Os GGUF publicados têm metadados com defeito.

O antecessor **V4-Flash** (284B/13B ativos) roda hoje via llama.cpp: de 82,5 GB (1-bit) a ~110–135 GB
(3-bit) e ~162 GB (4-bit), ou seja, estação com 128–192 GB de RAM e uma GPU para o offload dos
experts; lento, mas possível. Para usar a capacidade do V4.1 hoje, a rota é a nuvem: grátis na
NVIDIA NIM ou ~US$ 0,009 por run no OpenRouter (banco 2026-09).

Fontes (acesso em 2026-09-26): model card `deepseek-ai/DeepSeek-V4.1-Flash` (Hugging Face);
modemguides.com "DeepSeek V4.1-Flash Hardware Requirements" (2026-09-10); modelfit.io "DeepSeek V4.1
Flash on a Mac"; Unsloth, documentação do DeepSeek-V4. Tamanhos de quantização e suporte de runtime
mudam rápido: reconferir antes de decidir compra.

## Limites

- Uma placa de referência (3060, Windows com desktop vivo). O fundo do desktop e o "penhasco" do
  WDDM ([STAGE2](STAGE2.md), Achado 2) mudam de máquina para máquina.
- Tamanhos de arquivo e parâmetros dos modelos não baixados vêm da biblioteca do Ollama e dos model
  cards (lab/2026-09-26-banco-modelos); bandas das placas são especificação de fabricante.
- "talvez (medir)" é o convite à próxima sonda: carregar o modelo e ler `size` a 32k.
