---
title: 'Preços e valores voláteis em documentação de método'
created: 2026-09-26
updated: 2026-09-26
status: 'Pesquisa + proposta. Nada aplicado ao guia ainda (decisão do dono).'
tags: [temporalidade, precos, documentacao, perecibilidade]
---

# Preços e valores voláteis em documentação de método

Pergunta do dono (2026-09-26): o guia `recipe/strata-com-ia.*` põe US$ por run, tok/s e segundos
por run inline. Isso vale só para hoje. Como outros tratam isso?

Regra: "sim" = página aberta nesta sessão e o trecho saiu dela.

## Práticas encontradas

| prática | quem usa | como | fonte | verificado? |
|---|---|---|---|---|
| Carimbo "as of" em afirmação volátil | Wikipedia | `{{As of}}` em cada afirmação; nada de "now/currently"; deixa todas localizáveis | https://en.wikipedia.org/wiki/Wikipedia:As_of | sim |
| Data absoluta, não relativa | Wikipedia MOS | "since 2010", não "currently" | https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers | sim |
| Perene × datado separados | Google developer style guide | linguagem temporal só em release notes/blog | https://developers.google.com/style/timeless-documentation | sim |
| Nominal datado + conversão recalculada | Wikipedia `{{Inflation}}` | guarda valor e ano; converte por índice | https://en.wikipedia.org/wiki/Template:Inflation | sim |
| Número-índice sobre base declarada | BLS (CPI) | base 1982-84 = 100; comparar por variação % | https://www.bls.gov/cpi/questions-and-answers.htm | sim |
| Unidade independente de hardware | Green AI (Schwartz et al. 2019) | rejeita tempo, eletricidade e carbono por não serem estáveis entre labs, datas e hardware; adota FPO | https://arxiv.org/abs/1907.10597 | sim |
| Descrever recurso, não preço | NeurIPS Paper Checklist (item 8) | tipo de compute, compute por execução e total | https://neurips.cc/public/guides/PaperChecklist | sim |
| US$ absoluto + data, nova linha quando muda | Aider leaderboard | custo total por execução, datado; "after price reduction" vira nova entrada | https://aider.chat/docs/leaderboards/ | sim |
| Preço vivo + ponderação declarada | Artificial Analysis | preço atual do provedor; blend 7:2:1; tok/s após o 1º token | https://artificialanalysis.ai/methodology | sim |
| Ranking vivo | OpenRouter rankings | por tokens processados até hoje | https://openrouter.ai/rankings | sim |
| Faixas $/$$/$$$ | — | não achado em fonte aberta | — | não verificado |
| Pareto custo × qualidade | — | não confirmado nas páginas abertas | — | não verificado |

Não verificados: GOV.UK, Microsoft Style Guide, Diátaxis, LMArena, HELM, SWE-bench, pricing docs
de Google Cloud e Azure.

## Proposta para o guia

| número | hoje | proposta | por quê |
|---|---|---|---|
| Preço de catálogo por token | às vezes citado | **ponteiro** para a página do fabricante / Artificial Analysis / OpenRouter | é o que mais muda e tem dono externo com fonte viva |
| US$ por run (medido) | absoluto inline | **ordem de grandeza** na entrega ("frações de centavo", "centavos", "dólares") + **razão para uma referência nomeada e datada**; o absoluto datado fica no banco (traço) | razão envelhece mais devagar (Green AI, CPI); absoluto datado segue o padrão Aider |
| tok/s, s/run | absoluto inline | **faixa grossa** (segundos / dezenas de segundos / minutos) + contexto (provedor ou placa, raciocínio); absoluto datado no banco | tempo depende de hardware, carga e provedor (Green AI) |
| Esforço durável | não usado | **tokens de saída por run** como unidade independente de hardware; custo = tokens × preço vivo | análogo ao FPO; declarar o tokenizador |
| Especificação de hardware (GB/s, GB) | inline | **manter** com fonte | é spec de fabricante, não muda para o produto |

Isso é a regra do próprio projeto (§5: número volátil fora da prosa; ADR-005: aponte ao hub) aplicada
a preço e tempo, onde o guia ainda não a cumpria.

## Trade-offs

- **Razão também deriva.** Se a referência muda de preço ou sai de linha, todas as razões mudam.
  Só envelhece mais devagar. Por isso nomear e datar a referência.
- **Ponteiro vivo quebra a reprodução.** O leitor vê o preço de hoje, não o que gerou a conclusão.
  O registro datado fica no traço (banco/RESULTADOS); o ponteiro, na entrega.
- **Absoluto datado mostra que envelheceu, mas não corrige.** Precisa de guarda mecânica que ache
  carimbos velhos (como a categoria "As of" da Wikipedia). Candidata: estender `tools/check_stamps.py`.
- **Tokens não são neutros.** Tokenizadores contam diferente; declarar a unidade.
- **Faixas $/$$/$$$ são escolha nossa**, não padrão encontrado.
