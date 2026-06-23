---
title: 'Opinião de uso do Strata — honesta, por tarefa × capacidade do modelo × custo'
created: 2026-06-13
updated: 2026-06-23
status: 'Consolidado. O que o Strata entrega na prática, por tarefa/capacidade/custo, com as ressalvas. SINAIS direcionais (sintético + completion-only, N pequeno), não prova. A evolução datada e os experimentos vivem no hub e nos RESULTADOS-*.'
---

# Opinião de uso do Strata — o que dizer, com honestidade

> Texto de **entrega**: o estado consolidado, não o diário. O que esperar do Strata na prática.
> A evolução por fase, os experimentos e o que foi descartado vivem no [hub](ARQUITETURA-E-EVIDENCIAS.md)
> (histórico append-only) e nos `RESULTADOS-*`; o que falta, no [`BACKLOG`](BACKLOG-fila-geral.md).
> Cada conclusão passou por crítica adversarial contra exagero. **Tudo é sinal/direção, não prova.**
> Este documento segue a norma de redação do repositório: [`ESTILO-REDACAO`](../../ESTILO-REDACAO.md).

## O que o Strata entrega

Três coisas, em ordem de solidez.

- **Padroniza o conserto (sólido).**
  Diante de um defeito conhecido, o método leva a IA a consertar sempre do mesmo jeito, de forma rastreável.
  O defeito conhecido é uma informação que virou duas (§5), ou algo antigo a aposentar (§3).
  O conserto preserva o histórico: marca o antigo como superado, não apaga.
  Isso vale até no modelo econômico.
  A preservação do histórico (§3) é a parte mais robusta, porque é a única que se confirmou num projeto real.
  Lá, sem o método o baseline apaga seções, e com o método a destruição não acontece.
  O conserto completo da fonte única (§5) ainda só foi medido em caso sintético.

- **Faz a IA recusar instrução maliciosa lida do projeto (§6-bis).**
  Diante de "baixe e rode esta URL" ou "execute sem confirmar", a IA não obedece.
  E também não inventa ameaça onde não há.
  O econômico melhora muito com o método, e o topo recusa de forma nativa.
  A recusa do econômico é em parte lexical, porque cai sob paráfrase.

- **Aponta o caminho do "quando NÃO agir", mas a calibração é do modelo (sinal).**
  Reconhecer que o projeto já está bom e não mexer (§9) é o julgamento difícil.
  Ele depende da capacidade, não da forma.
  Nenhuma forma torna um modelo fraco proporcional.

**Sobre a over-ação (mexer no que não precisa).**
Ela não é carimbo fixo do tier.
Aparece quando o projeto tem ruído ou bagunça a confundir.
Num projeto limpo e bem-governado, até o econômico se abstém.
O reverso é o limite mais duro: num projeto que de fato precisa, a falha vira sub-detecção, ou seja, deixar passar.
E só um modelo de topo fura a complacência, variando por fornecedor, não preso à família que escreveu o método.
Isto ainda é direcional, porque ruído e forma-do-pedido não foram isolados (ver ressalvas).

**Sobre os juízes (como sabemos o acima).**
No conjunto de detecção, 7 de 9 juízes de 3 empresas (OpenAI, Google, Anthropic) convergem no falso-positivo.
A forma anti-falso-positivo reduz o erro para todos eles.
É esse painel afiado do F0 que fecha o caveat "Claude julga Claude": é cross-vendor de verdade, não auto-avaliação.
O R6 trouxe um 2º juiz, o gpt-4.1-mini.
Ele confirma que a ordenação e os deltas sobrevivem a outra família, e mediu o viés de família (~0,87).
Mas o F0 depois mostrou que o gpt-4.1-mini é leniente, ou seja, cego ao falso-positivo.
Então o R6 fecha a direção, não a magnitude anti-falso-positivo.
O resíduo é estreito: só as rodadas ecológicas mais recentes deste ciclo ainda não foram re-pontuadas por um juiz afiado de outro fabricante (Gemini ou GPT).
Detalhe em [confronto narrativa×granular](RESULTADOS-confronto-narrativa-granular.md) §3.

## Por tarefa — quem dá conta

Sobre modelos de IA: "quem dá conta" é qual capacidade faz a tarefa bem.
A escala vem dos READMEs ([recipe](../../recipe/README.md)): topo, médio, econômico.
É capacidade, não tamanho, porque um *flash* barato pode bater um 70B.
Confiança: SÓLIDO é bem medido, sinal é direção, EXPLORATÓRIO/RUIDOSO é fraco.

| Tarefa | Quem dá conta | Confiança |
|---|---|---|
| [Consertar um defeito conhecido](RESULTADOS-f4-execucao.md) (§5) | o econômico já dá conta, com o Strata (até o Haiku) | **SÓLIDO** |
| [Preservar o histórico / tombstone](RESULTADOS-f4-execucao.md) (§3) | o econômico, com o Strata | **SÓLIDO** — replicou no REAL (eco-pdf2md); o pedaço mais robusto |
| [Recusar instrução maliciosa](RESULTADOS-f3-recusa.md) (§6-bis) | o econômico melhora; o topo recusa nativo | **SINAL** (a medição mais frágil) |
| [Abster-se num projeto já bom](RESULTADOS-f4-execucao.md) (§9) | só o topo, ou um humano no loop | sinal (é a capacidade que calibra) |
| [Achar dívida real num projeto grande](RESULTADOS-p10-escada-propria-genero.md) | só o topo (e varia por fornecedor) | sinal (sub-detecção é o limite duro) |
| [Verificar fonte na web](RESULTADOS-f5-pesquisa.md) (§6) | nenhum modelo, de forma confiável | **EXPLORATÓRIO** |
| [Reconciliar o projeto inteiro num passo](RESULTADOS-f4-execucao.md) | nenhum nível dá conta | sinal (limite do harness) |
| [Agir sozinha rodando local (4–8B)](RESULTADOS-tier-local.md) | nenhum — não usar para agir | **RUIDOSO** |

## A regra prática

1. **Para AGIR num defeito conhecido** (consertar §5, preservar §3): o econômico com o Strata basta.
   O caso é sólido, ancorado em ação de arquivo, e o premium é redundante.
   Mas não vale como varredura autônoma de um projeto real, porque ali até a versão sem método alucina, e o método às vezes piora.

2. **Para NÃO agir bem** (abster-se, §9) e **achar dívida real**: use um modelo de topo, ou fique no loop.

3. **Custo não compra qualidade de forma linear.**
   Acima do barato-que-funciona, o intermediário não melhora; só o topo compra discernimento.
   "Maior = melhor" vale dentro de um mesmo fornecedor, mas é tendência com exceção: falha no DeepSeek, onde o Pro ≈ o Flash, e a métrica 0-3 satura.
   Entre fornecedores, não vale.

4. **Para JULGAR com IA:** o melhor custo-benefício é o gemini-2.5-flash.
   Os menores da OpenAI (nano/mini) não servem, porque são lenientes e escondem o falso-positivo.

> **Regra de ouro.**
> Método + topo: pode ser de uma vez.
> Método + econômico ou médio: oriente em etapas e mantenha o humano no loop.
> E toda saída de IA é rascunho a revisar, com atenção dobrada ao *não-fazer* e ao *primeiro passo*.

## O que NÃO esperar

- Que o Strata **melhore o que a IA já faz bem sozinha.** Às vezes a prosa piora o óbvio.
- Que funcione como **auditor autônomo num projeto real.** Ele não bate a competência pura do modelo.
  A falha dominante é falso-positivo no projeto limpo, ou sub-detecção no que precisa.
- Que **verifique fonte na web de forma confiável.** Sem web, ele carimba como verdadeiro; com web, ainda revise.
- Que um modelo **econômico seja seguro contra injeção** sob ataque real. A recusa fraca é lexical e cai sob paráfrase.
- Que um modelo **local pequeno (4–8B) aja sozinho.** Ele não conserta, e pode apagar histórico, obedecer ou alucinar.
- Que **reconcilie um projeto inteiro num passo.**
- Que **situe artefatos no tempo** com garantia. É a dimensão mais ruidosa.
  Acerta quando a cronologia é legível (marcadores ou ordem recuperável do conteúdo), e erra quando ela está enterrada.
  Falta o caso real-grande.
- Que conclusões do modo **só-texto** transfiram para um **agente com ferramentas.** Isso não foi testado.
- **L1 (formalização) e L2 (ferramentas) quase não foram testados.** Afirmações sobre eles são não-testadas.

## Honestidade — as ressalvas que esta opinião carrega (§6)

- **Só-texto.**
  Medimos a intenção do plano, não o agente real com ferramentas.
  Isso não transfere direto ao produto.

- **N pequeno** (1 a 5 repetições por célula).
  São deltas grandes contra ruído, não significância estatística.

- **Os juízes foram cross-vendor, não Claude sozinho.**
  O F0 usou 9 juízes de 3 empresas, e 7 convergiram.
  É o painel afiado do F0 que fecha o caveat de artefato, não a mini.
  O R6 trouxe um 2º juiz, o gpt-4.1-mini: ele confirma a ordenação e os deltas, e mediu o viés de família.
  Mas o próprio F0 depois achou esse juiz leniente ("corrige o 2º-juiz fraco que usávamos").
  Então o R6 fecha a direção, não a magnitude anti-falso-positivo — over-claim corrigido em [confronto narrativa×granular](RESULTADOS-confronto-narrativa-granular.md) §3.
  O F4 teve 92% entre o Gemini 2.5 Flash e o GPT-4.1, mais a conferência mecânica da abstenção §9.
  O resíduo é estreito: as rodadas ecológicas mais recentes deste ciclo (projetos próprios, fg2p) foram pontuadas por Claude e ainda não re-pontuadas cross-vendor.
  O viés de família foi medido (Claude ~0,87 ponto mais generoso com o Haiku), por isso não ancoramos em célula Claude-julga-Claude.
  E convergência cross-vendor não é prova de acerto: a literatura 2024-2026 mostra erro correlacionado entre fabricantes, e a nossa Fase B mostra juízes concordando nas respostas erradas sem o gabarito.
  Quem ancora o sólido é o **gold mecânico**, não o consenso ([confronto](RESULTADOS-confronto-literatura.md), [fundamento](FUNDAMENTO-juiz-escala-mensuravel.md)).

- **Circularidade.**
  Já há um braço externo de verdade.
  A forma de abstenção foi testada em 6 repositórios open-source de terceiros (tomli, slugify, humanize, mlscratch, pytorchgan, ml3months) e em projetos publicados, como o FG2P, que tem artigo.
  Ali a forma de abstenção reconhece o projeto de terceiro como "já bom", e o pedido "ache problemas" over-detecta nos mesmos repos limpos.
  Isso quebra a circularidade do achado central, fora da família que escreveu o método.
  O que continua circular é mais estreito: a auditoria rica de qualidade em projeto de terceiro ainda não tem gabarito independente, o braço externo é N=1 num só gênero (pacote Python), e falta o gabarito gênero-consciente que separaria sub-detecção de "já-bom-para-o-gênero".

- **Ruído × forma-do-pedido confundidos.**
  O "limpo abstém / real sub-detecta" foi medido sob um pedido que já prima abstenção.
  Falta cruzar com o pedido "ache problemas" para isolar.

- **A conferência por regex** dá falso-positivo dos dois lados; só fica limpa ancorada em ação de arquivo.

- **Tudo aqui é sinal / direção forte, não prova.**

## Resultado mais recente (resumo) — e onde está a evolução

- **Funciona (sólido):** consertar §5 e preservar §3, até no econômico; recusar injeção §6-bis; e 7 de 9 juízes de 3 empresas convergem, então não é auto-avaliação.
- **Funciona (sinal):** num projeto limpo, todos se abstêm; sob ruído, só o topo calibra.
- **Não funciona / em aberto:** auditor autônomo no projeto real (sub-detecção é o limite duro); verificação na web; agente com ferramentas reais; L1/L2.

Para a **evolução completa** — fase a fase, o que foi dito e descartado, os números por experimento:
[hub de arquitetura e evidências](ARQUITETURA-E-EVIDENCIAS.md) (histórico) ·
[`RESULTADOS-p10`](RESULTADOS-p10-escada-propria-genero.md) (projetos reais) ·
[`DOSSIE-judge`](DOSSIE-judge-justificativa-cientifica.md) (o juiz) ·
[`BACKLOG`](BACKLOG-fila-geral.md) (o que falta para firmar).
