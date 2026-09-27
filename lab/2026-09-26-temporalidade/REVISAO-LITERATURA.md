---
title: 'Temporalidade em LLMs: revisão de literatura (fontes primárias)'
created: 2026-09-26
updated: 2026-09-26
status: 'Varredura v1. Achados pelo resumo dos autores (PDFs não lidos na íntegra).'
tags: [temporalidade, llm, agentes, rag, perecibilidade, revisao-literatura]
---

# Temporalidade em LLMs, agentes e RAG: revisão de literatura

**Como foi feita (2026-09-26).** Cada artigo foi aberto pelo registro do próprio artigo: título,
autores, ano, venue e resumo, via API do Semantic Scholar. "sim (resumo)" = o achado vem do resumo
dos autores; números que só aparecem no corpo do texto não foram conferidos. EvolveBench pela ACL
Anthology; fontes de fabricante pelas páginas oficiais. Arbesman só pela listagem do editor.
55 fontes. Varredura feita por agente; próximo passo é ler na íntegra as fontes que sustentarem
decisão de método.

## 1. Consciência do próprio corte e da data atual

| referência | ano | tipo | achado principal | URL | verificado? |
|---|---|---|---|---|---|
| Cheng et al., "Dated Data", arXiv:2403.12958 | 2024 | artigo | Corte efetivo ≠ declarado, varia por tópico; causas: dados antigos em dumps novos do CommonCrawl, deduplicação | https://arxiv.org/abs/2403.12958 | sim (resumo) |
| Pęzik et al., "LLMLagBench", arXiv:2511.12116 | 2025 | benchmark | Estima a fronteira temporal do treino por eventos recentes, inclusive sem corte declarado | https://arxiv.org/abs/2511.12116 | sim (resumo) |
| Zhao et al., "Set the Clock", arXiv:2402.16797 (ACL 2024) | 2024 | artigo | LLaMa2 (corte 2022) responde com conhecimento de ~2019; alinhar melhora até 62% | https://arxiv.org/abs/2402.16797 | sim (resumo) |
| Li et al., "Simulated Ignorance Fails", arXiv:2601.13717 (IJCAI 2026) | 2026 | artigo | "Finja que seu corte é X" deixa 52% de gap; CoT não suprime; modelos de raciocínio pioram | https://arxiv.org/abs/2601.13717 | sim (resumo) |
| Asai et al., "Can LLMs Be Constrained to the Past?", arXiv:2606.05804 | 2026 | método | Self-Recall e Question-Recall superam resposta direta e CoT; varia com a distância ao corte | https://arxiv.org/abs/2606.05804 | sim (resumo) |
| Reizinger & Brendel, "HALLMARK", arXiv:2607.18360 | 2026 | artigo | Verificadores LLM marcam como suspeitos artigos posteriores ao próprio corte | https://arxiv.org/abs/2607.18360 | sim (resumo) |
| Price et al., "Future Events as Backdoor Triggers", arXiv:2407.04108 | 2024 | artigo | Existe representação interna da "data atual" (steering altera o comportamento) | https://arxiv.org/abs/2407.04108 | sim (resumo) |
| Anthropic, system prompt Claude Opus 5.5 (entrada de 22/09/2026) | 2026 | doc de fabricante | claude.ai injeta a data e declara o corte; não vale para a API | https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5-5 | sim |
| OpenAI, Harmony Response Format | 2025 | doc de fabricante | System message canônica tem `Knowledge cutoff:` e `Current date:` | https://developers.openai.com/cookbook/articles/openai-harmony | sim |

**Síntese.** Corte declarado não é o efetivo, e o modelo responde "no passado". A data é contexto
injetado pelo fabricante, não conhecimento do modelo. Instrução em prompt controla pouco (52% de
gap). Não há A/B publicado do efeito isolado de injetar a data em perguntas perecíveis.

## 2. Conhecimento defasado nos pesos e atualização

| referência | ano | tipo | achado principal | URL | verificado? |
|---|---|---|---|---|---|
| Lazaridou et al., "Mind the Gap", arXiv:2102.01951 (NeurIPS 2021) | 2021 | fundacional | Desempenho cai com a distância temporal; escala não resolve | https://arxiv.org/abs/2102.01951 | sim (resumo) |
| Dhingra et al., "Time-Aware LMs", arXiv:2106.15110 (TACL 2022) | 2021 | fundacional | Timestamp no treino melhora memorização e calibração futura | https://arxiv.org/abs/2106.15110 | sim (resumo) |
| Luu et al., "Time Waits for No One!", arXiv:2111.07408 (NAACL 2022) | 2021 | artigo | Desalinhamento temporal maior que o relatado; pré-treino continuado ajuda pouco | https://arxiv.org/abs/2111.07408 | sim (resumo) |
| Loureiro et al., "TimeLMs", arXiv:2202.03829 | 2022 | modelos | LMs diacrônicos; aprendizado contínuo ajuda | https://arxiv.org/abs/2202.03829 | sim (resumo) |
| Jang et al., "Continual Knowledge Learning", arXiv:2110.03215 (ICLR 2022) | 2021 | benchmark | Reter o invariante, atualizar o obsoleto, adquirir o novo | https://arxiv.org/abs/2110.03215 | sim (resumo) |
| Jang et al., "TemporalWiki", arXiv:2204.14211 (EMNLP 2022) | 2022 | benchmark | Treinar só no diff iguala o snapshot com ~12× menos compute | https://arxiv.org/abs/2204.14211 | sim (resumo) |
| Liška et al., "StreamingQA", arXiv:2205.11388 (ICML 2022) | 2022 | benchmark | Índice atualizado adapta rápido, mas não iguala LM retreinado | https://arxiv.org/abs/2205.11388 | sim (resumo) |
| Kim et al., "EvolvingQA", arXiv:2311.08106 (NAACL 2024) | 2023 | benchmark | Aprendizado contínuo não remove o obsoleto; pior em numérico/temporal | https://arxiv.org/abs/2311.08106 | sim (resumo) |
| Meng et al., "ROME", arXiv:2202.05262 (NeurIPS 2022) | 2022 | edição | Fatos localizados em FFNs médias, editáveis | https://arxiv.org/abs/2202.05262 | sim (resumo) |
| Zhong et al., "MQuAKE", arXiv:2305.14795 (EMNLP 2023) | 2023 | benchmark | Edição não propaga consequências multi-hop; memória externa escala melhor | https://arxiv.org/abs/2305.14795 | sim (resumo) |
| Mousavi et al., "DyKnow", arXiv:2404.08700 (EMNLP 2024) | 2024 | benchmark | 24 LLMs defasados; editores não reduzem a defasagem | https://arxiv.org/abs/2404.08700 | sim (resumo) |
| Tang et al., "EvoWiki", arXiv:2412.13582 | 2024 | benchmark | Respostas obsoletas; RAG + aprendizado contínuo sinérgicos | https://arxiv.org/abs/2412.13582 | sim (resumo) |
| Park et al., "ChroKnowledge", arXiv:2410.09870 (ICLR 2025) | 2024 | benchmark | Conhecimento cronológico parcial, "corta" nas fronteiras | https://arxiv.org/abs/2410.09870 | sim (resumo) |
| Nakshatri et al., "evolveQA", arXiv:2510.19172 | 2025 | benchmark | AWS/Azure/OMS; queda de até 31% contra perguntas estáticas | https://arxiv.org/abs/2510.19172 | sim (resumo) |
| Guan et al., arXiv:2605.13045 | 2026 | benchmark | Diretrizes médicas 2001–2026; busca agêntica só −3% a +14% | https://arxiv.org/abs/2605.13045 | sim (resumo) |

**Síntese.** Degradação com o tempo é o achado mais replicado (2021–2026). Atualizar pesos
funciona para o fato isolado e falha nas consequências e na remoção do obsoleto. Nem busca
agêntica resolve em domínio especializado.

## 3. Benchmarks de raciocínio temporal

| referência | ano | tipo | achado principal | URL | verificado? |
|---|---|---|---|---|---|
| Chen et al., "TimeQA", arXiv:2108.06314 | 2021 | benchmark | Melhor modelo 46% contra 87% humano | https://arxiv.org/abs/2108.06314 | sim (resumo) |
| Zhang & Choi, "SituatedQA", arXiv:2109.06157 | 2021 | benchmark | ~16,5% do NQ-Open depende de quando/onde | https://arxiv.org/abs/2109.06157 | sim (resumo) |
| Tan et al., "TempReason", arXiv:2306.08952 (ACL 2023) | 2023 | benchmark | Três níveis de raciocínio temporal | https://arxiv.org/abs/2306.08952 | sim (resumo) |
| Wang & Zhao, "TRAM", arXiv:2310.00835 (ACL 2024) | 2023 | benchmark | Ordem, aritmética, frequência, duração; abaixo do humano | https://arxiv.org/abs/2310.00835 | sim (resumo) |
| Chu et al., "TimeBench", arXiv:2311.17667 (ACL 2024) | 2023 | benchmark | Gap grande e desigual por categoria | https://arxiv.org/abs/2311.17667 | sim (resumo) |
| Fatemi et al., "Test of Time", arXiv:2406.09170 (ICLR 2025) | 2024 | benchmark | Sintético, sem contaminação | https://arxiv.org/abs/2406.09170 | sim (resumo) |
| Ruiz et al., "RATA", arXiv:2504.07646 | 2025 | benchmark | LLM sozinho não basta; precisa de código | https://arxiv.org/abs/2504.07646 | sim (resumo) |
| Bhatia et al., "Date Fragments", arXiv:2505.16088 (EMNLP 2025) | 2025 | artigo | Tokenização de datas custa até 10 pontos | https://arxiv.org/abs/2505.16088 | sim (resumo) |
| Zhu et al., "EvolveBench", ACL 2025 | 2025 | benchmark | Todos sofrem com contexto temporalmente desalinhado | https://aclanthology.org/2025.acl-long.788/ | sim |
| Piryani et al., "It's High Time" (survey), arXiv:2505.20243 (ACL 2025) | 2025 | survey | Corpus × pergunta × capacidade do modelo | https://arxiv.org/abs/2505.20243 | sim (resumo) |

**Síntese.** Gap persistente para humanos, sobretudo em aritmética de datas e contexto implícito.
Raciocínio temporal é problema distinto de conhecimento defasado.

## 4. RAG sensível ao tempo e conflitos de conhecimento

| referência | ano | tipo | achado principal | URL | verificado? |
|---|---|---|---|---|---|
| Longpre et al., arXiv:2109.05052 (EMNLP 2021) | 2021 | fundacional | Modelo confia demais na memória contra o contexto | https://arxiv.org/abs/2109.05052 | sim (resumo) |
| Xie et al., "Chameleon or Sloth", arXiv:2305.13300 (ICLR 2024) | 2023 | artigo | Aceita evidência coerente; viés de confirmação com a memória | https://arxiv.org/abs/2305.13300 | sim (resumo) |
| Wu et al., "ClashEval", arXiv:2404.10198 (NeurIPS 2024) | 2024 | benchmark | Adota contexto errado sobre prior correto em >60% | https://arxiv.org/abs/2404.10198 | sim (resumo) |
| Xu et al., survey de conflitos, arXiv:2403.08319 (EMNLP 2024) | 2024 | survey | Contexto-memória, entre contextos, intra-memória | https://arxiv.org/abs/2403.08319 | sim (resumo) |
| Mallen et al., "PopQA", arXiv:2212.10511 (ACL 2023) | 2022 | artigo | Escala só melhora o popular; recuperar quando preciso | https://arxiv.org/abs/2212.10511 | sim (resumo) |
| Yang et al., "CRAG", arXiv:2406.04744 (NeurIPS 2024) | 2024 | benchmark | LLM 34%, RAG 44%, industrial 63%; pior em fatos dinâmicos | https://arxiv.org/abs/2406.04744 | sim (resumo) |
| Fang et al., "Do LLMs Favor Recent Content?", arXiv:2509.11353 | 2025 | artigo | Rerankers promovem datas "frescas" artificiais | https://arxiv.org/abs/2509.11353 | sim (resumo) |
| Abdallah et al., "TempRetriever", arXiv:2502.21024 (WSDM 2025) | 2025 | método | Data da query + doc no retriever: +6,86% R@1 | https://arxiv.org/abs/2502.21024 | sim (resumo) |
| Chen et al., "ChronoQA", arXiv:2508.12282 | 2025 | dataset | RAG temporal em notícias chinesas 2019–2024 | https://arxiv.org/abs/2508.12282 | sim (resumo) |
| Han et al., "TG-RAG", arXiv:2510.13590 | 2025 | método | Grafo temporal com atualização incremental | https://arxiv.org/abs/2510.13590 | sim (resumo) |
| Sobhani et al., "TIDE", arXiv:2608.08512 | 2026 | benchmark | Detectar versão que não rege a query: 26,7% | https://arxiv.org/abs/2608.08512 | sim (resumo) |

**Síntese.** Conflito nos dois sentidos: ora crédulo com o contexto (ClashEval), ora teimoso com
a memória (TIDE). Rerankers têm viés de recência. Não há regra validada de desempate recência ×
autoridade.

## 5. Calibração e abstenção para fatos perecíveis

| referência | ano | tipo | achado principal | URL | verificado? |
|---|---|---|---|---|---|
| Kadavath et al., arXiv:2207.05221 | 2022 | artigo | P(True) calibrado; P(IK) calibra mal fora da distribuição | https://arxiv.org/abs/2207.05221 | sim (resumo) |
| Yin et al., "SelfAware", arXiv:2305.18153 | 2023 | benchmark | Autoconhecimento existe, com gap para humanos | https://arxiv.org/abs/2305.18153 | sim (resumo) |
| Vu et al., "FreshLLMs/FreshQA", arXiv:2310.03214 | 2023 | benchmark+método | Todos erram em fato volátil e premissa falsa; FreshPrompt ajuda | https://arxiv.org/abs/2310.03214 | sim (resumo) |
| Kasai et al., "RealTime QA", arXiv:2207.13332 | 2022 | benchmark | Responde obsoleto em vez de abster | https://arxiv.org/abs/2207.13332 | sim (resumo) |
| Wen et al., survey de abstenção, arXiv:2407.18418 (TACL) | 2024 | survey | Query, modelo e valores humanos | https://arxiv.org/abs/2407.18418 | sim (resumo) |
| Kirichenko et al., "AbstentionBench", arXiv:2506.09038 (NeurIPS 2025) | 2025 | benchmark | Escala não ajuda; raciocínio piora abstenção em 24% | https://arxiv.org/abs/2506.09038 | sim (resumo) |
| Meem et al., "PAT-Questions", arXiv:2402.11034 | 2024 | benchmark | Gabarito auto-atualizável via SPARQL | https://arxiv.org/abs/2402.11034 | sim (resumo) |
| Wallat et al., "Temporal Blind Spots", arXiv:2401.12078 (WSDM 2024) | 2024 | artigo | Fraco no passado detalhado e no muito recente | https://arxiv.org/abs/2401.12078 | sim (resumo) |
| Kim et al., "TDBench", arXiv:2508.02045 | 2025 | benchmark | "Time accuracy": valida as referências temporais da explicação | https://arxiv.org/abs/2508.02045 | sim (resumo) |

**Síntese.** Abstenção diante de informação defasada é o ponto fraco, e piora com modelos de
raciocínio. Bate com o nosso banco: raciocínio `high` derrubou a abstenção.

## 6. Agentes

| referência | ano | tipo | achado principal | URL | verificado? |
|---|---|---|---|---|---|
| Lin et al., survey de alucinação em agentes, arXiv:2509.18970 | 2025 | survey | 18 causas por estágio do agente | https://arxiv.org/abs/2509.18970 | sim (resumo) |
| Wu et al., "LongMemEval", arXiv:2410.10813 (ICLR 2025) | 2024 | benchmark | Expansão de query com tempo melhora recuperação | https://arxiv.org/abs/2410.10813 | sim (resumo) |
| Du et al., "Memory-T1", arXiv:2512.20092 | 2025 | método | RL com recompensa de consistência temporal | https://arxiv.org/abs/2512.20092 | sim (resumo) |
| Weng et al., "TemporalBench", arXiv:2602.13272 (KDD 2026) | 2026 | benchmark | Frameworks de agente com falhas sistemáticas | https://arxiv.org/abs/2602.13272 | sim (resumo) |

**Síntese.** Evidência escassa. Nenhum benchmark mede os erros clássicos do agente com busca:
assumir que hoje é o corte, confiar em fonte do dia do lançamento, não checar a data da fonte,
estimar quando dava para verificar. (O erro do DeepSeek V4.1 em `../2026-06-04-economia-ia-tokens/
instrumento/STAGE5.md` é um caso desse tipo, documentado.)

## 7. Mitigações com efeito medido

Timestamp no treino (Dhingra); busca datada e ordenada no prompt (FreshPrompt); alinhamento
temporal (Set the Clock, até +62%); timeline + autorreflexão (TISER, arXiv:2504.05258); memória
externa (MeLLo); metadado temporal na recuperação (TempRetriever, TG-RAG); Self/Question-Recall;
system prompt para abstenção (ajuda, não resolve). Injeção de data pelos fabricantes: universal,
sem avaliação publicada. Tudo medido em benchmark, não em trabalho real.

## Literatura não-ML

Arbesman, *The Half-Life of Facts* (Current/Penguin, 2012): fatos têm meia-vida por campo.
Verificação parcial (só listagem do editor). Já citado no §6 do Strata.

## Consenso

- O conhecimento nos pesos envelhece; replicado 2021–2026.
- Corte declarado ≠ efetivo; o modelo responde com conhecimento mais antigo.
- Raciocínio temporal abaixo do humano em todos os benchmarks.
- Recuperação ajuda muito, não resolve (CRAG 44–63%).
- Editar pesos não propaga nem remove o obsoleto.

## Controvérsias

- **Contexto × memória:** crédulo (ClashEval) e teimoso (TIDE), conforme plausibilidade.
- **Recência × autoridade:** viés de recência mesmo com data falsa; sem desempate validado.
- **Prompt como controle:** ganhos medidos e, ao mesmo tempo, prompt não "rebobina" (52% de gap).
- **Raciocínio × abstenção:** raciocínio melhora benchmark temporal e piora abstenção.

## Lacunas

- **Nenhum protocolo de processo avaliado** para humano ou agente lidar com fato perecível
  (classificar perecibilidade, verificar em fonte primária datada, carimbar, revalidar).
- **Agentes:** sem benchmark dos erros temporais típicos com busca.
- **Injeção da data atual:** sem A/B publicado.
- **Hedge seletivo:** o modelo distingue estável de volátil e hedgeia só no volátil? Não medido.
- **Validade externa:** quase tudo é QA sintético/Wikidata.
- **Meia-vida por domínio** nunca usada para calibrar desconfiança.

## Onde um método pode contribuir

- Protocolo agnóstico ao modelo para fatos perecíveis; a literatura só tem componentes isolados.
- Avaliação pré-registrada desse protocolo contra linha de base, com poder estatístico:
  acurácia, taxa de afirmação obsoleta, abstenção apropriada, "time accuracy".
- Regra explícita de desempate recência × autoridade, testável.
- Expectativa honesta: prompt tem efeito parcial; esperar ganho modesto e medir com poder
  (lição do nosso próprio A/B do §9, inconclusivo por falta de poder).
