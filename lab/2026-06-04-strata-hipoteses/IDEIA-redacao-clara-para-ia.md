---
title: 'Ideia: a clareza para uma IA pode pedir um estilo de redação próprio'
status: 'registrado — hipótese a pensar depois; não executado'
created: 2026-06-20
updated: 2026-06-20
---

# Ideia: a clareza para uma IA pode pedir um estilo próprio

Este é o registro de uma hipótese do dono, para pensarmos depois.
Não é um experimento feito. É uma direção a investigar.

## A semente

Os documentos que uma pessoa lê seguem a Linguagem Simples (ver `../../ESTILO-REDACAO.md`).
A frase é completa, com artigos e conectivos, e a página é fácil de varrer.

Mas o Strata também é lido por uma IA.
E o ideal do Strata é ficar pequeno e, ao mesmo tempo, servir a máquina.
Daí a pergunta do dono: se uma IA lê a mesma coisa com menos texto, será que fica mais claro para ela?

A hipótese é que a clareza para uma IA tenha um estilo próprio, diferente do humano.
O ponto de vista muda. Não é "como fica claro para mim", é "como fica claro para ela".

## Duas ideias para pensar

1. A clareza de redação pode virar um complemento do Strata.
   Escrever claro faz parte de organizar bem o conhecimento.
   Talvez o `ESTILO-REDACAO.md` deva ser referenciado pelo método, e não só pelo repositório.

2. O texto que a IA consome pode ser comprimido, quase truncado.
   Para a pessoa, truncar piora a leitura.
   Para a máquina, a hipótese é que comprimir pode ajudar.

## Perguntas a responder depois

- Menos texto deixa a tarefa mais clara para a IA? E para qual nível de modelo?
- Existe um "estilo de redação para IA"? Como ele seria?
- O que quer dizer "tokens completos", e isso seria uma forma de medir a clareza para a IA?
- Dá para um texto só servir bem ao humano e à máquina?
- Ou o Strata precisa de duas superfícies: uma em Linguagem Simples para a pessoa, e uma densa para a IA?

## O que já sabemos que toca nisto

Já há sinal de que a forma densa ajuda o modelo pequeno.
Nos testes P1, P2 e P6, a forma densa e a checklist em etapas renderam mais nos modelos médios e econômicos do que a prosa canônica longa.
O guia `../../recipe/strata-com-ia.md` diz o mesmo: a prosa longa afoga os modelos de ~8B, que precisam da versão densa ou da checklist.
O modelo de topo, ao contrário, lê a prosa canônica direto.

Então a compressão parece ajudar mais o tier econômico do que o topo.
Isso já sugere que "claro para a IA" depende do modelo, e não é um alvo único.

## A tensão a respeitar

O Strata exige ser autossuficiente.
Cada cópia carrega a fundamentação inline (§5 fonte única, §3 rastreabilidade).
Comprimir demais pode tirar essa fundamentação e quebrar a capacidade de o arquivo viajar sozinho.
Então a compressão para a IA precisa preservar o que torna o arquivo autossuficiente.

## Liga-se a

Esta ideia toca o **Comporta**, a segunda metodologia, que estuda economia de recurso de IA.
Menos tokens no método é, ao mesmo tempo, mais clareza possível para a IA e menos custo por uso.

## Um rascunho de como testar

Medir a mesma tarefa, com o mesmo modelo, variando só a forma do texto.
Comparar a prosa em Linguagem Simples, a forma densa atual, e uma versão comprimida nova.
Olhar over-ação, recall e segurança, separados por tier.
Definir "tokens completos" antes de medir, para saber o que se está contando.
