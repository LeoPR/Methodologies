---
title: Strata em português ou inglês (guia de confiança)
status: active
created: 2026-08-03
updated: 2026-08-03
purpose: responder, objetivamente, "em qual idioma rodar o Strata?". Só as conclusões; o porquê vive na evidência linkada
---

<!-- l10n: doc_id=strata-idiomas · lang=pt-BR · source_lang=en · translation_of=strata-idiomas.en.md -->
[English](strata-idiomas.en.md) · **Português**

# Strata em português ou inglês: o que funciona onde

**Resposta curta: rode o Strata no idioma de quem lê e aplica.** As duas versões são de
primeira classe: `knowledge-architecture.en.md` é a fonte canônica e
`knowledge-architecture.pt-BR.md` é a tradução derivada, atualizada no mesmo commit
(ADR-008). O método foi medido nos dois idiomas em 2026-08-03 com rosters idênticos;
o comportamento do núcleo é o mesmo.

## O que vale nos DOIS idiomas (medido)

- **O conserto de defeito conhecido (§5) satura**: dos modelos econômicos de nuvem ao topo
  de fronteira, todos executam o conserto no padrão com Strata, em PT e em EN igualmente
  (6/6 e 6/6). Sem Strata, os mesmos modelos falham na grade inteira nos dois idiomas.
- **A abstenção (§9) é a borda, e é propriedade de modelo**: não de preço, não de tier, não
  de idioma. Os mesmos modelos superagem ou se calam calibrados nos dois idiomas.
- **O topo fecha os dois lados nos dois idiomas** (conserto/armadilha/abstenção, 6/6): o
  modo de auto-auditoria autônoma é seguro em qualquer um dos dois.
- **O idioma do seu PROJETO não importa**: método em EN × projeto em PT pontuou igual a
  método EN × projeto EN.

## O que é sensível a idioma (sinais datados, 2026-08-03)

- **Inglês NÃO é melhor.** Trocar o método para inglês esperando ganho não tem suporte: a
  borda de recusa mediu igual ou levemente pior em EN (dois instrumentos independentes,
  mesma direção).
- **Modelos médios/abertos recusam injeção um pouco pior em EN** (payload propagado 5/8 em
  EN × 1/8 em PT no tier GPU; sinal K=2, datado). Não muda a recomendação, que já é
  "médio/econômico = checklist + revisão humana" nos **dois** idiomas.
- **NÃO misture idiomas.** A receita "método em inglês, resposta em português via instrução"
  foi testada e **rejeitada**: teve a pior obediência ao payload malicioso de todo o estudo
  (4/6). Um idioma de ponta a ponta.

## Tabela prática

| Sua situação | Faça isto |
|---|---|
| Você lê/trabalha em português | Use `knowledge-architecture.pt-BR.md`. Cobertura plena; nada perdido. |
| Você lê/trabalha em inglês | Use `knowledge-architecture.en.md`. Mesma cobertura de prova. |
| Modelo médio/econômico ou local | Qualquer um dos idiomas + **checklist + humano confirmando cada achado** |
| Modelo topo, auto-auditoria autônoma | Qualquer um dos idiomas (6/6 nos dois) |
| Projeto em idioma diferente do método | Tudo bem assim; não precisa traduzir o projeto |

## Custo de token: um idioma é mais barato?

Medido em 2026-08-03 (mesmo roster, células pareadas; tokenizer cl100k para a contagem
de entrada):

- **Lado da entrada: português custa ~22% mais tokens.** O documento do método tokeniza
  em 20.610 tokens em PT × 16.928 em EN, embora o arquivo PT tenha *menos* caracteres.
  É a desigualdade de tokenização entre idiomas, documentada na literatura
  ([Ahia et al., EMNLP 2023](https://aclanthology.org/2023.emnlp-main.614.pdf);
  [NeurIPS 2023](https://openreview.net/pdf?id=Pj4YYuxTq9)): texto não-inglês fragmenta
  em mais tokens para o mesmo conteúdo; o PT é um caso leve (~1,2×; há idiomas com 4-15×).
- **Lado da saída: respostas em inglês saíram ~9% mais curtas** (mediana das células
  pareadas da nossa grade), mas o comprimento da saída varia com o comportamento do
  modelo; leia como sinal suave.
- **Efeito líquido: real, mas de segunda ordem.** No nosso harness, runs em EN usaram
  ~15-20% menos tokens no total. A preços de nuvem, isso é fração de centavo por
  auditoria; só importa em escala (milhares de runs) ou como tempo de GPU em modelo
  local (~20% a mais de processamento do prompt).

Duas ressalvas honestas:

- **Token mede custo, não valor.** A contagem de tokens é exatamente o que o provedor
  cobra, então é uma boa métrica de *custo*; não diz nada sobre a qualidade do
  resultado. Nossa paridade mostra que os resultados são os mesmos nos dois idiomas,
  então escolha o idioma pelo leitor, não pelo delta de ~20% na entrada. E a escolha
  do *modelo* move o custo em ordens de grandeza a mais que a escolha do idioma: um
  modelo pequeno e eficiente contra um modelo topo de linha ofusca qualquer diferença
  PT×EN.
- **"A IA traduz para inglês internamente?"** Parcialmente apoiado pela pesquisa de
  interpretabilidade: muitos LLMs processam entrada não-inglesa num espaço latente
  inclinado ao inglês
  ([Do Multilingual LLMs Think in English?, 2025](https://arxiv.org/html/2502.15603v1)),
  com contra-evidência recente de raciocínio abstrato além de idioma
  ([arXiv 2506.09890](https://www.arxiv.org/pdf/2506.09890)). Essa tradução interna
  *não é cobrada*; o que você paga a mais em PT é a fragmentação do tokenizer acima,
  não uma etapa de tradução.

**Conclusão: escolha o idioma pelo leitor.** O delta de tokens existe, favorece EN em
~15-20% por run, e é pequeno demais para dirigir a decisão.

## Por quê (ponteiros, não repetição)

- Piloto de idioma, recusa (F3): [`lab/2026-08-03-idioma-en/RESULTADOS-idioma-f3.md`](../lab/2026-08-03-idioma-en/RESULTADOS-idioma-f3.md)
- Grade de paridade, conserto/abstenção/armadilha (F4): [`lab/2026-08-03-idioma-en/RESULTADOS-f4-en.md`](../lab/2026-08-03-idioma-en/RESULTADOS-f4-en.md)
- A grade honesta completa (qual modelo para qual tarefa): [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md)

*Sinais datados (2026-08-03) e gerações de modelo envelhecem rápido. Reconfira a evidência
linkada antes de ancorar uma decisão cara nesta página.*
