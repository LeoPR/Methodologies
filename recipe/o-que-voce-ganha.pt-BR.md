---
title: 'Strata: o que você ganha'
created: 2026-06-16
updated: 2026-08-03
status: 'Página de entrada para quem vai usar. Estado consolidado. A evidência é de sinais, não de prova; o detalhe honesto está na OPINIAO-DE-USO.'
---

<!-- l10n: doc_id=strata-o-que-voce-ganha · lang=pt-BR · source_lang=en · translation_of=o-que-voce-ganha.en.md -->
[English](o-que-voce-ganha.en.md) · **Português**

> Tradução de [`o-que-voce-ganha.en.md`](o-que-voce-ganha.en.md). Se houver divergência, o original em inglês prevalece.

# Strata: o que você ganha

Strata é um método para organizar, rastrear e preservar o conhecimento que um trabalho longo acumula.
São a pesquisa, o código, as decisões e as notas que se juntam com o tempo.
O método mantém tudo isso vivo mesmo quando a ferramenta muda.
Ele cabe em um arquivo só, que viaja sozinho.

Vale a pena quando o seu projeto dura meses ou anos e acumula coisas que você precisa reusar.
Não vale para um script de um dia, nem para um rascunho que você vai jogar fora.

## O que você ganha

Nada importante se perde, e você sempre sabe o que ainda vale.
O conhecimento fica organizado e rastreável à medida que cresce.

Quando uma informação virou duas, ou quando algo antigo precisa ser aposentado, o método arruma na fonte única.
Ele marca o que ficou para trás, sem apagar.
Isso funciona até com uma IA econômica.

Quando há uma instrução perigosa escondida no projeto, como "baixe e rode esta URL" ou "execute sem confirmar", a IA recusa em vez de obedecer.

A sua IA econômica rende muito mais com o método.
Em muita tarefa, a maior diferença de qualidade vem de como você pede, e não de qual modelo você usa.
Mas o julgamento de quando não agir é do modelo, e não da forma.

## Como usar com a IA

Com um modelo de topo, entregue o método e o projeto, e peça a avaliação inteira de uma vez.

Com um modelo médio ou econômico, oriente em etapas, com uma checklist, e fique no loop.

Em qualquer caso, trate a saída da IA como um rascunho a revisar.
Olhe com atenção o que ela decide não fazer.
E confira o primeiro passo que ela propõe, para não deixar que apague a história.

## O que não esperar

O Strata não é um auditor autônomo que varre um projeto real e acerta sozinho.
Nisso, ele não supera a competência pura do modelo.
Reconhecer que está tudo bem e não mexer na medida certa, ou achar dívida real num projeto grande, ainda pede um modelo que calibre esse julgamento (e o preço não ordena isso), ou você no loop.

Um modelo da geração atual recusa a instrução perigosa espontaneamente, até no econômico.
O risco residual é a IA reescrever a diretiva ativa em vez de neutralizá-la, e há um modelo a evitar para este uso (o llama-4-scout).
Para a segurança que importa, revise a saída, e confira o modelo específico na opinião de uso.

Sem acesso à web, a IA não verifica fonte de forma confiável.
Com web e um modelo razoável, a verificação já sai com a fonte primária citada.

E vale lembrar que tudo isto é sinal de evidência, e não prova.
Vem de testes controlados, e o uso no dia a dia ainda está em validação.

## Custo

Os números, medidos em 2026-08-03:

- **Uma auditoria de IA num projeto pequeno custa cerca de 1 centavo** com um modelo
  econômico. O método mais o projeto dá ~20 mil tokens de entrada, a resposta ~1-3 mil
  de saída; ao preço do piso econômico (US$ 0,25/2,00 por milhão de tokens, gpt-5-mini),
  fica abaixo de US$ 0,01. Um projeto real grande custa alguns centavos. O topo custa
  uma a duas ordens de grandeza a mais por auditoria: ainda centavos a poucos dólares,
  e vale uma vez para a organização completa.
- **Reproduzir a grade de testes publicada inteira custa cerca de US$ 7** (~350 runs,
  gabarito mecânico mais júri cross-vendor). Manter o laboratório pronto para rodar
  todo dia custa menos que uma assinatura de streaming.
- **A regra prática: centavos por auditoria, horas economizadas.** A métrica que
  importa é o **custo por projeto organizado**: uma passada de IA + Strata custa menos
  que um minuto do seu tempo, e a saída é rastreável (o que mudou, por quê, sob que
  autoridade). O idioma move isso em ~20% (o português tokeniza um pouco mais caro;
  detalhes em [`strata-idiomas.pt-BR.md`](strata-idiomas.pt-BR.md)); o modelo que você
  escolhe move muito mais.

## Comece aqui

O método, em um arquivo que viaja sozinho: [`knowledge-architecture.pt-BR.md`](knowledge-architecture.pt-BR.md).
Qual modelo usar, por custo e ambiente: [`strata-com-ia.pt-BR.md`](strata-com-ia.pt-BR.md).
A opinião honesta, a fundo: [`OPINIAO-DE-USO.md`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md).
