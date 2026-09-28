---
title: 'Mapa 8: o que computação e IA aproximam do raciocínio temporal, e os limites'
created: 2026-09-27
updated: 2026-09-27
status: 'Varredura v1 por agente (2026-09-27). Maioria pelo resumo; Park, Packer, Zep, Taatgen e Laird pelo texto.'
tags: [temporalidade, expressividade, tc0, estado, modelos-de-mundo, neuro-simbolico, memoria-de-agente, bitemporal]
---

# Mapa 8: computação e IA, aproximações e limites

"sim (texto)" = trecho do corpo lido. "sim (resumo)" = abstract ou página oficial. "parcial" = só
metadados. "Chain-of-timeline" não existe com esse nome (o mais próximo é TISER, TG-LLM e NoT).

## 1. Limites teóricos para rastrear estado

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Hahn, TACL 8 | 2020 | Self-attention não modela linguagens periódicas nem hierarquia sem crescer com a entrada | https://aclanthology.org/2020.tacl-1.11/ | sim (resumo) |
| Merrill & Sabharwal, "Parallelism Tradeoff", TACL | 2023 | Transformers de precisão log ⊆ **TC⁰** | https://arxiv.org/abs/2207.00729 | sim (resumo) |
| Merrill, Petty & Sabharwal, "Illusion of State in SSMs", ICML 2024 | 2024 | SSMs também em TC⁰; "o estado é uma ilusão" | https://arxiv.org/abs/2404.08819 | sim (resumo) |
| Liu et al., "Shortcuts to Automata", ICLR 2023 | 2023 | Simulam autômatos por **atalhos** que generalizam mal | https://arxiv.org/abs/2210.10749 | sim (resumo) |
| Strobl et al., survey, TACL 12 | 2024 | Harmoniza os resultados de expressividade | https://arxiv.org/abs/2311.00208 | sim (resumo) |
| Merrill & Sabharwal, "Transformers with CoT", ICLR 2024 | 2024 | n passos de CoT → todas as regulares; poli(n) → P | https://arxiv.org/abs/2310.07923 | sim (resumo) |
| Feng et al., NeurIPS 2023 | 2023 | CoT dá tamanho constante para aritmética e DP | https://arxiv.org/abs/2305.15408 | sim (resumo) |
| Li et al., "CoT ... Serial Problems", ICLR 2024 | 2024 | Sem CoT, AC⁰; com T passos, circuitos de tamanho T | https://arxiv.org/abs/2402.12875 | sim (resumo) |
| Grazzi et al., ICLR 2025 | 2025 | Autovalores negativos destravam estado em RNNs lineares | https://arxiv.org/abs/2411.12537 | sim (resumo) |

**Síntese.** Numa passada, transformer e SSM não rastreiam estado sequencial arbitrário. Passos
explícitos (CoT, scratchpad) ou arquitetura diferente alargam o limite. Inferência nossa: fecho
transitivo sobre N eventos **deve ser externalizado**, não pedido "de cabeça".

## 2. Representações internas

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Li, Nye & Andreas, ACL 2021 | 2021 | Estado de entidades linear e manipulável | https://arxiv.org/abs/2106.00737 | sim (resumo) |
| Toshniwal et al., AAAI 2022 | 2022 | Tabuleiro de xadrez rastreado; depende do histórico completo | https://arxiv.org/abs/2102.13249 | sim (resumo) |
| Li et al., Othello-GPT, ICLR 2023 | 2023 | Tabuleiro interno causal | https://arxiv.org/abs/2210.13382 | sim (resumo) |
| Nanda, Lee & Wattenberg | 2023 | Estado linear ("minha cor/oponente") | https://arxiv.org/abs/2309.00941 | sim (resumo) |
| Kim & Schuster, ACL 2023 | 2023 | Entity tracking só em modelos com código | https://arxiv.org/abs/2305.02363 | sim (resumo) |
| Gurnee & Tegmark, ICLR 2024 | 2024 | Representação linear de **tempo de calendário** | https://arxiv.org/abs/2310.02207 | sim (resumo) |
| Vafa et al., arXiv:2406.03689 | 2024 | Modelos de mundo muito menos coerentes do que os diagnósticos sugerem | https://arxiv.org/abs/2406.03689 | sim (resumo) |
| Li, Guo & Andreas, arXiv:2503.02854 | 2025 | Dois mecanismos de estado: "associative scan" e heurística de paridade | https://arxiv.org/abs/2503.02854 | sim (resumo) |
| Pink et al., arXiv:2607.22575 | 2026 | Memória de **ordem no contexto** com efeito de distância humano, via código temporal numa cabeça | https://arxiv.org/abs/2607.22575 | sim (resumo) |

**Síntese.** Há representação de estado e de tempo (calendário; ordem no contexto). **Nada mostra
ordenação por pré-condição.** Decodificar estado não garante modelo de mundo coerente (Vafa).

## 3. Modelos de mundo, predição e segmentação

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Zacks et al., *Psychol Bull* 133 | 2007 | Erro de predição marca fronteira de evento | https://pmc.ncbi.nlm.nih.gov/articles/PMC2852534/ | sim (resumo) |
| Friston, *Nat Rev Neurosci* 11 | 2010 | Energia livre como teoria unificada | https://www.nature.com/articles/nrn2787 | parcial |
| Clark, *BBS* 36 | 2013 | Cérebro preditivo hierárquico | https://www.research.ed.ac.uk/en/publications/whatever-next-predictive-brains-situated-agents-and-the-future-of/ | sim (resumo) |
| Ha & Schmidhuber, "World Models" | 2018 | Treinar "dentro do sonho" | https://arxiv.org/abs/1803.10122 | sim (resumo) |
| Franklin et al., SEM, *Psychol Rev* 127 | 2020 | Esquemas de evento bayesianos; fronteira quando o esquema não prediz | https://gershmanlab.com/pubs/Franklin20.pdf | parcial |
| LeCun, "A Path Towards AMI" | 2022 | H-JEPA: predição latente hierárquica | https://openreview.net/forum?id=BZ5a1r-kVsf | parcial |
| Hafner et al., DreamerV3 | 2023 | Modelo do ambiente, >150 tarefas | https://arxiv.org/abs/2301.04104 | sim (resumo) |
| Michelmann et al., *Behav Res Methods* | 2023/25 | GPT-3 segmenta eventos como humanos | https://arxiv.org/abs/2301.10297 | sim (resumo) |
| Fountas et al., EM-LLM, ICLR 2025 | 2024 | Segmenta por **surpresa bayesiana**; 10M tokens | https://arxiv.org/abs/2407.09450 | sim (resumo) |

**Síntese.** Predição → erro → fronteira tem teoria (EST), modelo (SEM) e engenharia (EM-LLM).
Modelos de mundo preveem o próximo estado, mas não produzem ordem parcial nem apontam lacuna.

## 4. Híbridos neuro-simbólicos

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Liu et al., LLM+P | 2023 | LLM → PDDL → planejador → LLM | https://arxiv.org/abs/2304.11477 | sim (resumo) |
| Guan et al., NeurIPS 2023 | 2023 | GPT-4 gera **modelos de domínio** (pré-condições e efeitos), corrigidos e usados por planejador | https://arxiv.org/abs/2305.14909 | sim (resumo) |
| Valmeekam et al., NeurIPS 2023 | 2023 | GPT-4 autônomo ~12%; melhor com verificador | https://arxiv.org/abs/2305.15771 | sim (resumo) |
| Kambhampati et al., LLM-Modulo, ICML 2024 | 2024 | LLM gera, verificador simbólico testa e critica | https://arxiv.org/abs/2402.01817 | sim (resumo) |
| Xiong et al., TG-LLM, ACL 2024 | 2024 | Texto → grafo temporal | https://arxiv.org/abs/2401.06853 | sim (resumo) |
| Zhang et al., Narrative-of-Thought, Findings EMNLP 2024 | 2024 | Eventos como classe Python + ordenação topológica | https://arxiv.org/abs/2410.05558 | sim (resumo) |
| Ge et al., TReMu, Findings ACL 2025 | 2025 | Linha do tempo + código: GPT-4o de ~30% para >77% | https://arxiv.org/abs/2502.01630 | sim (resumo) |
| Islakoglu & Kalo, ChronoSense, ACL 2025 | 2025 | Relações de Allen inconsistentes nos LLMs | https://arxiv.org/abs/2501.03040 | sim (resumo) |
| Bazaga et al., TISER, ACL 2025 | 2025 | Linha do tempo explícita + autorreflexão | https://arxiv.org/abs/2504.05258 | sim (resumo) |

**Síntese.** O que funciona: **o LLM estrutura, algo simbólico calcula.** Guan et al. é o
precedente de "o LLM propõe pré-condições e efeitos". Nenhum testa passo faltante.

## 5. Memória de agente com tempo

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Liu et al., TLogic, AAAI 2022 | 2022 | Regras temporais explicáveis em grafo de conhecimento | https://arxiv.org/abs/2112.08025 | sim (resumo) |
| Park et al., Generative Agents, UIST '23 | 2023 | Recuperação por relevância + importância + recência (decaimento 0,995/h) | https://arxiv.org/abs/2304.03442 | sim (texto) |
| Packer et al., MemGPT | 2023 | Contexto paginado; recall storage consultável | https://arxiv.org/abs/2310.08560 | sim (texto) |
| Rasmussen et al., Zep/Graphiti | 2025 | **Bitemporal**: `t_valid/t_invalid` (mundo) × `t'_created/t'_expired` (ingestão); contradição invalida a aresta antiga sem apagar | https://arxiv.org/abs/2501.13956 | sim (texto) |

**Síntese.** O "agora" fica **fora** do modelo. O bitemporal do Zep separa quando valeu de quando
soube. Mas a ordem vem de timestamp, não de pré-condição, e a contradição é detectada por LLM.

## 6. Arquiteturas cognitivas

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Taatgen, van Rijn & Anderson, *Psychol Rev* 114 | 2007 | ACT-R: pacemaker com ruído escalar → escala logarítmica | http://act-r.psy.cmu.edu/wordpress/wp-content/uploads/2012/12/697interval-published.pdf | sim (texto) |
| Nuxoll & Laird, *Cogn Syst Res* 17–18 | 2012 | Memória episódica do Soar | https://www.sciencedirect.com/science/article/abs/pii/S1389041711000428 | parcial |
| Laird, arXiv:2205.03854 | 2022 | Episódios navegáveis anterior/seguinte; "replay" para achar a causa | https://arxiv.org/abs/2205.03854 | sim (texto) |

**Síntese.** Relógio interno com ruído (duração, não ordem) e episódios encadeados (sequência
explícita). Nenhum deriva ordem de pré-condição.

## O que cabe em computação e IA

**Fechável (simbólico, com garantia):** ordem por links causais e ordenação topológica; passos sem
dependência como concorrentes; conflitos (ciclo, ameaça, timestamp contra a cadeia); lacuna
(pré-condição sem produtor e fora do estado inicial); "agora" como fronteira, guardado fora do modelo
em armazenamento bitemporal. Tudo algoritmo polinomial conhecido.

**Aproximável (aprendido, sem garantia):** extrair estados, eventos, pré-condições e efeitos do
texto; normalizar predicados; sugerir qual ação preenche a lacuna; segmentar por surpresa; rastrear
estado curto (ou longo com CoT).

**Só explicável hoje:** por que humanos escolhem a granularidade do evento e notam espontaneamente
que falta algo; o "agora" vivido; energia livre como arcabouço, não algoritmo.

**Arquitetura mínima para o paraquedas** (proposta nossa, de Guan, Kambhampati, TISER/NoT e Zep):
1. **Extrator (LLM):** fragmento → {ação/estado, pré-condições, adiciona, remove, timestamp?}; o
   timestamp é atributo ruidoso, não chave de ordem.
2. **Normalizador:** unifica sinônimos; o que não unifica fica marcado, não descartado.
3. **Ordenador (simbólico):** links causais e ordem parcial; emite sequências compatíveis, pares
   concorrentes, conflitos e lacunas.
4. **Lacuna → consulta:** pré-condição órfã vira pergunta; LLM propõe, busca externa confirma; volta
   ao passo 1 até fechar ou esgotar o orçamento.
5. **"Agora" externo e bitemporal:** `t_valid` separado de `t_ingest`.
6. **Opcional:** segmentação por surpresa antes do passo 1.

Métrica: ordem parcial correta, conflitos detectados, lacunas detectadas e preenchidas, cada uma em
coluna separada; remover passos de propósito testa "notar a falta".
