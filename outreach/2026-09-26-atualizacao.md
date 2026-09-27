---
title: 'Notícia 2026-09-26: banco de modelos renovado, revisão das fontes, correções'
created: 2026-09-26
updated: 2026-09-26
status: 'Fonte canônica das notícias de divulgação. Os canais (linkedin/, medium/) formatam daqui.'
---

<!-- l10n: doc_id=outreach-2026-09-26 · lang=pt-BR · canonical -->
[English](2026-09-26-update.en.md) · **Português**

# Notícia-fonte 2026-09-26 (resumo das conclusões, para derivar posts)

> Este arquivo é a **fonte** das notícias. Cada canal em subpasta formata o seu texto a partir
> daqui. Todo número vem de um registro datado do `lab/`; nada aqui é métrica nova.

## Estado do produto

- Documento canônico em **v1.2.5**. O núcleo (L0) não mudou de princípio: a prosa foi conferida
  contra as fontes citadas, e citações e atribuições foram corrigidas (ex.: *literary warrant* é de
  Hulme 1911; Saltzer & Schroeder saiu nos *Proc. IEEE*). Registro: `lab/2026-09-26-revisao-temporal/`.

## Manchetes

1. **Banco de modelos renovado (2026-09-26).** O conserto, a recusa da injeção e o "não mexer num
   projeto bom" foram medidos em modelos lançados até setembro. **16 rotas fazem as três coisas.**
   A mais barata custa cerca de **US$ 0,002 por auditoria** (gpt-6-luna); a mais rápida responde
   em **3 s** (gemini-3.5-flash-lite); o menor modelo aberto que faz tudo é o **qwen3.8-27b**.
   Registro: `lab/2026-09-26-banco-modelos/`.
2. **Dá para fazer tudo de graça**, só que devagar: **kimi-k3** e **deepseek-v4.1-flash** pela
   camada grátis da NVIDIA fizeram as três coisas.
3. **Rodar em casa é questão de placa, não de modelo.** Os pesos que fazem tudo (qwen3.8-27b)
   cabem inteiros numa placa de 24 GB, como a 4090. Numa de 12 GB, o melhor encaixe conserta e
   recusa a injeção, e a decisão de não mexer fica com um humano. Capacidade medida na nuvem
   nos mesmos pesos, com contra-prova local.
4. **Pensar mais não ajuda.** Com raciocínio alto, nenhum resultado melhorou, e alguns pioraram (um
   modelo passou a mexer num projeto que já estava bom). Regra: raciocínio padrão ou baixo.
5. **Verificar fonte sem internet é perigoso.** Sem busca na web, modelos de topo confirmaram como
   "correta" uma norma que já tinha sido substituída; com web, corrigiram tudo.
6. **Três modelos propagaram uma instrução maliciosa** plantada no projeto (gpt-oss-120b,
   claude-haiku-4.5, gemma4:12b; este último medido só localmente, porque não tem hospedagem na
   nuvem). Não use esses para ação autônoma.
7. **Honestidade de regime (sempre citar):** sinais em cenários sintéticos, três rodadas por teste,
   não prova. No projeto real, a auditoria autônoma só rende com modelo de topo.

## Correções à notícia de 2026-08-03

A notícia anterior afirmou três coisas que os registros não sustentam:

- **"Sem o método, os mesmos modelos falham na grade inteira."** Exagero. Sem o método, o conserto
  raramente sai no formato rastreável, mas às vezes sai; e no teste de "não mexer" o braço sem
  método empatou com o braço com método.
- **"Inglês não é melhor em nenhuma célula."** Os registros não dizem isso: em algumas células o
  inglês saiu melhor. O que se sustenta é "inglês sem vantagem demonstrada".
- **"Português × inglês: paridade fechada."** O pré-registro exigia uma margem estatística que não
  foi atingida. O certo é: **sem diferença detectada, equivalência não demonstrada.**

Também foi rebaixada a série de "não mexer" de agosto: a fixture usada entregava a resposta no
próprio texto. O teste da mudança no §9 foi re-lido como **inconclusivo** (não tinha poder
estatístico), e não "sem efeito".

## Links e âncoras

- Repositório: https://github.com/LeoPR/Methodologies
- Qual modelo usar: `recipe/strata-com-ia.*` · Banco: `lab/2026-09-26-banco-modelos/`
- Revisão das fontes e dos testes: `lab/2026-09-26-revisao-temporal/`
- Auditoria declarado × feito: `lab/2026-09-26-revisao-superficie/AUDITORIA-sync.md`
