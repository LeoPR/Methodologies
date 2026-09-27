---
title: 'Mapa 4: IA ordenando eventos sem timestamp, por estado, e detectando lacuna'
created: 2026-09-26
updated: 2026-09-27
status: 'Varredura v1 por agente; fontes abertas nesta data. Números valem para os modelos que cada artigo testou.'
tags: [temporalidade, ordem-de-eventos, estado, scripts, abducao, lacuna, llm]
---

# Mapa 4: IA ordenando eventos sem timestamp, por estado, e detectando lacuna

Habilidade-alvo: dado o paraquedas, o embarque e a preparação para saltar, embaralhados e com
horários errados ou ausentes, inferir embarque → voo → salto → paraquedas abre pelas pré-condições;
e, faltando um passo, notar que falta e buscar.

"sim" = página primária aberta em 2026-09-26 (arXiv, ACL Anthology, AAAI, PDF do autor). O
desempenho dos modelos de fronteira de 2026 nessas tarefas **não foi verificado**.

## 1. Extração de relações temporais

| referência | ano | tipo | achado | URL | verificado? |
|---|---|---|---|---|---|
| Pustejovsky et al., *The TIMEBANK Corpus*, Corpus Linguistics 2003 | 2003 | corpus (TimeML) | Notícias anotadas com eventos, expressões e relações temporais | https://ucrel.lancs.ac.uk/publications/CL2003/papers/pustejovsky.pdf | sim (contagens não) |
| Ning, Wu, Roth, MATRES, ACL 2018, arXiv:1804.07828 | 2018 | anotação | Eixos + só o ponto de início: κ de ~0,6 para ~0,8 | https://arxiv.org/abs/1804.07828 | sim |
| Naik et al., TDDiscourse, SIGDIAL 2019 | 2019 | dataset | Pares distantes (várias sentenças): sistemas pioram muito | https://aclanthology.org/W19-5929/ | sim |
| Zhou et al., MC-TACO, EMNLP 2019, arXiv:1909.03065 | 2019 | senso comum temporal | Ordem típica, duração; ~20 p.p. abaixo do humano | https://arxiv.org/abs/1909.03065 | sim |
| Ning et al., TORQUE, EMNLP 2020, arXiv:2005.00242 | 2020 | QA de ordem | RoBERTa-large 51% EM, ~30 p.p. abaixo do humano | https://arxiv.org/abs/2005.00242 | sim |
| Zhou et al., TRACIE, NAACL 2021, arXiv:2010.12753 | 2021 | eventos implícitos | Início + duração → fim (SymTime): +5% a +11% | https://arxiv.org/abs/2010.12753 | sim |

**Síntese.** Depende de pistas linguísticas locais (tempo verbal, conectivos). Cai com distância e
com eventos implícitos. Mede pares, não reconstrução global; nada ordena *estados* sem marcador.

## 2. Scripts, procedimentos e ordenação

| referência | ano | tipo | achado | URL | verificado? |
|---|---|---|---|---|---|
| Chambers & Jurafsky, ACL-08:HLT | 2008 | não supervisionado | Cadeias narrativas = **ordens parciais** de eventos com protagonista comum | https://aclanthology.org/P08-1090/ | sim |
| Barzilay & Lapata, Comp. Ling. 34(1) | 2008 | coerência (entity grid) | Distingue ordem original de permutações | https://aclanthology.org/J08-1001/ | sim |
| Wanzare et al., DeScript, LREC 2016 | 2016 | corpus | 40 cenários cotidianos, ~100 sequências cada | https://aclanthology.org/L16-1556/ | sim |
| Mostafazadeh et al., ROCStories/Story Cloze, NAACL 2016 | 2016 | corpus | Histórias de 5 sentenças com causalidade de senso comum | https://arxiv.org/abs/1604.01696 | sim |
| Huang et al., VIST, NAACL 2016 | 2016 | multimodal | 20.211 sequências de fotos com histórias | https://arxiv.org/abs/1604.03968 | sim |
| Zhang et al., WikiHow goals/steps, EMNLP 2020 | 2020 | benchmark | Ordem de passos; 10–20% abaixo do humano | https://arxiv.org/abs/2009.07690 | sim |
| Sakaguchi et al., proScript, Findings EMNLP 2021 | 2021 | scripts como DAG | Ordem parcial; F1 de arestas 75,7, abaixo do humano | https://arxiv.org/abs/2104.08251 | sim |
| Wu et al., manuais multimodais, ACL 2022 | 2022 | multimodal | Modelos mal usam a imagem para ordenar | https://arxiv.org/abs/2110.08486 | sim |
| Yuan et al., CoScript, ACL 2023 | 2023 | planejamento com restrição | 55 mil scripts | https://arxiv.org/abs/2305.05252 | sim |

**Síntese.** Já formalizado que sequência cotidiana é **ordem parcial**. Mas a ordem é aprendida
por coocorrência; ninguém usa **pré/pós-condição de estado** como mecanismo explícito.

## 3. Abdução, causalidade e rastreamento de estado

| referência | ano | tipo | achado | URL | verificado? |
|---|---|---|---|---|---|
| Roemmele et al., COPA, AAAI Spring 2011 | 2011 | causal | Causa/efeito com duas alternativas | https://aaai.org/papers/02418-2418-choice-of-plausible-alternatives-an-evaluation-of-commonsense-causal-reasoning/ | sim (sem abstract) |
| Dalvi Mishra et al., ProPara, NAACL 2018 | 2018 | estado | Estado de entidades passo a passo | https://arxiv.org/abs/1805.06975 | sim |
| Sap et al., ATOMIC, AAAI 2019 | 2019 | grafo se-então | 877 mil; causas, efeitos, **pré-condições** | https://arxiv.org/abs/1811.00146 | sim |
| Bhagavatula et al., ART/αNLI, ICLR 2020 | 2020 | abdução | **Evento do meio**: modelo 68,9% × humano 91,4% | https://arxiv.org/abs/1908.05739 | sim |
| Bisk et al., PIQA, AAAI 2020 | 2020 | físico | Humano 95%, modelo 77% | https://arxiv.org/abs/1911.11641 | sim |
| Mostafazadeh et al., GLUCOSE, EMNLP 2020 | 2020 | explicação causal | 10 dimensões, incluindo **estados** | https://arxiv.org/abs/2009.07758 | sim |
| Tandon et al., OpenPI, EMNLP 2020 | 2020 | estado aberto | Antes/depois por entidade; SOTA 16,1% F1 | https://aclanthology.org/2020.emnlp-main.520/ | sim |
| Storks et al., TRIP, Findings EMNLP 2021 | 2021 | avaliação em níveis | Acerta o final **sem** evidência de estado válida | https://arxiv.org/abs/2109.04947 | sim (qualitativo) |
| Du et al., e-CARE, ACL 2022 | 2022 | causal + explicação | Explicar continua difícil | https://aclanthology.org/2022.acl-long.33/ | sim |

**Síntese.** Família mais próxima da habilidade-alvo. Lição do TRIP: **acertar a resposta não
implica raciocínio de estado correto**. Nenhum combina N estados embaralhados com timestamp enganoso.

## 4. LLMs, 2023–2026

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Yuan et al., arXiv:2304.05454 | 2023 | ChatGPT zero-shot bem atrás do supervisionado; inconsistente em dependências longas | https://arxiv.org/abs/2304.05454 | sim |
| Kim & Schuster, ACL 2023 | 2023 | Rastrear estado **não emerge** só de texto; GPT-3.5 (muito código) sim | https://arxiv.org/abs/2305.02363 | sim |
| Valmeekam et al., NeurIPS 2023 | 2023 | GPT-4 planejando sozinho: ~12% | https://arxiv.org/abs/2305.15771 | sim |
| Valmeekam et al., PlanBench | 2022/23 | Ordenar ações por pré-condições: muito aquém | https://arxiv.org/abs/2206.10498 | sim |
| Valmeekam et al., "Can LRMs?", arXiv:2409.13373 | 2024 | o1-preview: Blocksworld 97,8%, Mystery 52,8% (LLMs < 5%); insolúveis: só 27% reconhecidos, 54% com plano falso | https://arxiv.org/abs/2409.13373 | sim |
| Wang & Zhao, TRAM | 2024 | Ordering: GPT-4 69,5% × humano 86,0% | https://arxiv.org/abs/2310.00835 | sim |
| Chu et al., TimeBench | 2024 | Lacuna significativa para humanos | https://arxiv.org/abs/2311.17667 | sim |
| Qiu et al., arXiv:2311.08398 | 2023 | Incoerentes em ≥27,23%; escala e CoT ajudam pouco; ordem do texto ≠ ordem dos eventos | https://arxiv.org/abs/2311.08398 | sim |
| Chen et al., Premise Order, ICML 2024 | 2024 | Permutar premissas: −30% | https://arxiv.org/abs/2402.08939 | sim |
| Lal et al., CaT-Bench, EMNLP 2024 | 2024 | Dependência entre passos de receita: F1 0,59–0,73; inconsistente no mesmo par | https://arxiv.org/abs/2406.15823 | sim |
| Fatemi et al., Test of Time | 2024 | Com datas explícitas, embaralhar derruba Claude de 73,6% para 45,7% | https://arxiv.org/abs/2406.09170 | sim |
| Wang et al., StripCipher, arXiv:2502.13925 | 2025 | Reordenar imagens: GPT-4o 23,9%, 56 p.p. abaixo do humano | https://arxiv.org/abs/2502.13925 | sim |
| Ryan et al., PixelHumor, Findings EMNLP 2025 | 2025 | Sequenciar painéis de quadrinhos: melhores 61% | https://arxiv.org/abs/2509.12248 | sim |
| Wongchamcharoen & Glasserman, arXiv:2511.14214 | 2025 | Ordem local sim, global não; GPT-5 com raciocínio acerta, mas com datas históricas já memorizadas | https://arxiv.org/abs/2511.14214 | sim |
| Li & Carenini, BeDiscovER, EACL 2026 | 2025/26 | Aritmética temporal ok; discurso no nível do documento, não | https://arxiv.org/abs/2511.13095 | sim |
| "Stories Refuse to Follow a Straight Line" (OpenReview) | 2025? | narrativa não linear | https://openreview.net/forum?id=jogKc4OluB | não verificado |

**Síntese.** Ordem local sim, global coerente não. Inconsistência ≥27%. Forte efeito da ordem de
apresentação. Sem pistas de superfície, despenca (Mystery Blocksworld). Imagem muito pior que
texto. Raciocínio estendido ajuda quando a ordem está na memória, mas não reconhece o impossível.

## 5. Detectar lacuna e decidir buscar

| referência | ano | achado | URL | verificado? |
|---|---|---|---|---|
| Rao & Daumé III, arXiv:1805.04655 | 2018 | Pergunta de esclarecimento por valor esperado da informação | https://arxiv.org/abs/1805.04655 | sim |
| Min et al., AmbigQA, EMNLP 2020 | 2020 | Mais da metade do NQ-open é ambígua | https://arxiv.org/abs/2004.10645 | sim |
| Press et al., Self-Ask, Findings EMNLP 2023 | 2023 | Subperguntas explícitas + busca > CoT | https://arxiv.org/abs/2210.03350 | sim |
| Mallen et al., ACL 2023 | 2023 | Recuperar só quando necessário (popularidade) | https://arxiv.org/abs/2212.10511 | sim |
| Jiang et al., FLARE, EMNLP 2023 | 2023 | Recupera em token de baixa confiança | https://arxiv.org/abs/2305.06983 | sim |
| Asai et al., Self-RAG | 2023 | Token de reflexão decide recuperar | https://arxiv.org/abs/2310.11511 | sim |
| Zhang & Choi, arXiv:2311.09469 | 2023 | Quando esclarecer | https://arxiv.org/abs/2311.09469 | sim |
| Zhang et al., CLAMBER, ACL 2024 | 2024 | Identifica ambiguidade mal; CoT aumenta a sobreconfiança | https://arxiv.org/abs/2405.12063 | sim |
| Li et al., MediQ | 2024 | Mandar "perguntar" direto piora; abstenção por confiança +22,3% | https://arxiv.org/abs/2406.00922 | sim |
| Wen et al., survey de abstenção, TACL 2024 | 2024 | Subespecificação como categoria central | https://arxiv.org/abs/2407.18418 | sim |
| Li, Kim, Wang, QuestBench, NeurIPS 2025 D&B | 2025 | Qual variável falta: 40–50% em lógica e planejamento; resolver ≠ saber o que perguntar | https://arxiv.org/abs/2503.22674 | sim |
| Fan et al., Missing Premise, arXiv:2504.06514 | 2025 | Modelo de raciocínio "pensa demais" em vez de apontar a lacuna | https://arxiv.org/abs/2504.06514 | sim |
| Kirichenko et al., AbstentionBench | 2025 | Raciocínio piora a abstenção ~24% | https://arxiv.org/abs/2506.09038 | sim |
| Fu et al., AbsenceBench, arXiv:2506.11440 | 2025 | Não sabem dizer o que falta, mesmo com o original ao lado (69,6% F1); a atenção não tem onde "ancorar" a ausência | https://arxiv.org/abs/2506.11440 | sim |

**Síntese.** Perceber ausência e decidir buscar são capacidades separadas, e ambas frágeis. Os
gatilhos de busca existentes são confiança do token, popularidade ou token aprendido; nenhum é
**lacuna estrutural** ("o efeito de A não satisfaz a pré-condição de B").

## Consenso

- Ordem de eventos é ordem parcial, não lista.
- LLMs acertam a ordem local e erram a coerência global (≥27% incoerência).
- Acertar a resposta não implica raciocínio de estado correto (TRIP).
- A ordem de apresentação contamina o raciocínio.
- Sem pistas de superfície, o desempenho despenca.
- Perceber o que falta e saber o que perguntar estão fracos; raciocínio longo piora a abstenção.

## Lacunas

1. Nenhum benchmark testa exatamente a habilidade-alvo (ordenar estados embaralhados por
   pré/pós-condição). O mais próximo é uma colcha: TRIP, CaT-Bench, PlanBench, StripCipher.
2. **Timestamp errado contra evidência de estado: nenhuma fonte.** Em quem o modelo confia quando
   os dois divergem é questão aberta.
3. Notar um passo faltante **inferencial** ≠ achar texto omitido (AbsenceBench) ≠ escolher o meio
   dado (αNLI, onde a lacuna já vem apontada). Nada combina notar, buscar e reordenar.
4. Números de GPT-4/o1/GPT-5; modelos de 2026 não medidos aqui.

## Onde um método pode contribuir

- **Estado explícito antes de ordenar:** para cada descrição, pré-condições e efeitos (ATOMIC,
  ProPara); a ordem parcial sai de "efeito de A satisfaz pré-condição de B", não da ordem de leitura.
- **Timestamp como evidência revogável**, abaixo da restrição de estado; divergência se registra,
  não se arbitra em silêncio (lacuna 2).
- **Coerência global verificada mecanicamente:** transitividade e aciclicidade das decisões par a
  par; o LLM propõe, um verificador externo confere (LLM-Modulo).
- **Lacuna por enumeração, não por "perceber ausência":** gerar o script esperado e comparar; um
  efeito necessário que nenhum passo produz ("no ar" sem "embarcou") é lacuna nomeável.
- **Gatilho de busca = lacuna estrutural**, que vira pergunta concreta; sem fonte, abster ou
  declarar o passo como inferido.
- **Avaliação em níveis (TRIP):** ordem final, restrições usadas, lacuna detectada, separadas;
  controles com domínio ofuscado (Mystery Blocksworld) e timestamps adulterados.
