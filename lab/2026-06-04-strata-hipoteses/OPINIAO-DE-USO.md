---
title: 'Opinião de uso do Strata — honesta, por tarefa × capacidade do modelo × custo'
created: 2026-06-13
updated: 2026-06-20
status: 'Consolidado. O que o Strata entrega na prática, por tarefa/capacidade/custo, com as ressalvas. SINAIS direcionais (sintético + completion-only, N pequeno), não prova. A evolução datada e os experimentos vivem no hub e nos RESULTADOS-*.'
---

# Opinião de uso do Strata — o que dizer, com honestidade

> Texto de **entrega**: o estado consolidado, não o diário. O que esperar do Strata na prática.
> A evolução por fase, os experimentos e o que foi descartado vivem no [hub](ARQUITETURA-E-EVIDENCIAS.md)
> (histórico append-only) e nos `RESULTADOS-*`; o que falta, no [`BACKLOG`](BACKLOG-fila-geral.md).
> Cada conclusão passou por crítica adversarial contra exagero. **Tudo é sinal/direção, não prova.**

## O que o Strata entrega

Três coisas, em ordem de solidez:

- **Padroniza o conserto (sólido).** Diante de um defeito conhecido — uma informação que virou duas (§5), algo
  antigo a aposentar (§3) —, o método leva a IA a consertar **sempre do mesmo jeito, rastreável e preservando o
  histórico** (marca como superado, não apaga). Vale **até no modelo econômico**.
- **Faz a IA recusar instrução maliciosa lida do projeto (§6-bis).** "Baixe e rode esta URL", "execute sem
  confirmar" → a IA não obedece, e não inventa ameaça onde não há. O econômico melhora muito com o método; o
  topo recusa de forma nativa. *(A recusa do econômico é em parte lexical — cai sob paráfrase.)*
- **Aponta o caminho do "quando NÃO agir" — mas a calibração é do modelo (sinal).** Reconhecer que o projeto
  **já está bom** e não mexer (§9) é o julgamento difícil; depende da **capacidade**, não da forma. Nenhuma forma
  torna um modelo fraco proporcional.

**Sobre a over-ação (mexer no que não precisa):** não é carimbo fixo do tier. Ela aparece quando o projeto tem
**ruído/bagunça a confundir**; num projeto **limpo e bem-governado**, até o econômico se abstém. O reverso é o
limite mais duro: num projeto real que **de fato precisa**, a falha vira **sub-detecção** (deixar passar) — e só
um modelo de **topo** fura a complacência, variando por **fornecedor** (não preso à família que escreveu o
método). *(Direcional: ruído e forma-do-pedido ainda não foram isolados — ver ressalvas.)*

**Sobre os juízes (como sabemos o acima):** no conjunto de detecção, **7 de 9 juízes de 3 empresas (OpenAI, Google,
Anthropic) convergem**. Os 3 menores da OpenAI ficaram de fora, por serem lenientes. Um 2º juiz, o gpt-4.1-mini (R6), confirma a ordenação, então o achado central **não** é "Claude julga
Claude". O R6 já fechou o caveat de juiz único nas conclusões da nuvem. O resíduo é estreito: só as rodadas ecológicas mais recentes deste ciclo ainda não foram re-pontuadas cross-vendor (ver ressalvas).

## Por tarefa — quem dá conta

Sobre **modelos de IA**: "quem dá conta" = qual capacidade faz a tarefa bem. Escala dos READMEs
([recipe](../../recipe/README.md)): **topo / médio / econômico** (capacidade; *flash* barato pode bater um 70B).
**Confiança:** SÓLIDO = bem medido; sinal = direção; EXPLORATÓRIO/RUIDOSO = fraco.

| Tarefa | Quem dá conta | Confiança |
|---|---|---|
| [Consertar um defeito conhecido](RESULTADOS-f4-execucao.md) (§5) | o econômico já dá conta, com o Strata (até o Haiku) | **SÓLIDO** |
| [Preservar o histórico / tombstone](RESULTADOS-f4-execucao.md) (§3) | o econômico, com o Strata | **SÓLIDO** no sintético; sinal no real |
| [Recusar instrução maliciosa](RESULTADOS-f3-recusa.md) (§6-bis) | o econômico melhora; o topo recusa nativo | **SINAL** (a medição mais frágil) |
| [Abster-se num projeto já bom](RESULTADOS-f4-execucao.md) (§9) | só o topo, ou um humano no loop | sinal (é a capacidade que calibra) |
| [Achar dívida real num projeto grande](RESULTADOS-p10-escada-propria-genero.md) | só o topo (e varia por fornecedor) | sinal (sub-detecção é o limite duro) |
| [Verificar fonte na web](RESULTADOS-f5-pesquisa.md) (§6) | nenhum modelo, de forma confiável | **EXPLORATÓRIO** |
| [Reconciliar o projeto inteiro num passo](RESULTADOS-f4-execucao.md) | nenhum nível dá conta | sinal (limite do harness) |
| [Agir sozinha rodando local (4–8B)](RESULTADOS-tier-local.md) | nenhum — não usar para agir | **RUIDOSO** |

## A regra prática

1. **Para AGIR num defeito conhecido** (consertar §5, preservar §3): **econômico + Strata basta** — caso sólido,
   ancorado em ação de arquivo; premium é redundante. **Não** vale como **varredura autônoma** de um projeto real
   (ali até a versão sem método alucina, e o método às vezes piora).
2. **Para NÃO agir bem** (abster-se, §9) e **achar dívida real**: use um **modelo de topo** ou **humano no loop**.
3. **Custo não compra qualidade linearmente:** acima do "barato-que-funciona", o intermediário não melhora; só o
   **topo** compra discernimento. "Maior = melhor" vale **dentro de um mesmo fornecedor** (robusto), não entre eles.
4. **Para JULGAR com IA:** melhor custo-benefício é o **gemini-2.5-flash**; os menores da OpenAI (nano/mini)
   **não servem** (lenientes, escondem falso-positivo).

> **Regra de ouro:** método + **topo** → de uma vez; método + **econômico/médio** → orientar em etapas e manter
> **humano no loop**. E **toda saída de IA é rascunho a revisar** — atenção dobrada ao *não-fazer* e ao *primeiro passo*.

## O que NÃO esperar

- Que o Strata **melhore o que a IA já faz bem sozinha** — às vezes a prosa piora o óbvio.
- Que funcione como **auditor autônomo num projeto real** — não bate a competência pura do modelo; a falha
  dominante é falso-positivo (no projeto limpo) ou sub-detecção (no que precisa).
- Que **verifique fonte na web de forma confiável** — sem web, carimba como verdadeiro; com web, ainda revise.
- Que um modelo **econômico seja seguro contra injeção** sob ataque real — a recusa fraca é lexical e cai sob paráfrase.
- Que um modelo **local pequeno (4–8B) aja sozinho** — não conserta, e pode apagar histórico, obedecer ou alucinar.
- Que **reconcilie um projeto inteiro num passo**.
- Que **situe artefatos no tempo** com garantia — é a dimensão mais ruidosa; acerta quando a cronologia é
  **legível** (marcadores ou ordem recuperável do conteúdo), erra quando enterrada. Falta o caso real-grande.
- Que conclusões do modo **só-texto** transfiram para um **agente com ferramentas** (não testado).
- **L1 (formalização) e L2 (ferramentas) quase não foram testados** — afirmações sobre eles são não-testadas.

## Honestidade — as ressalvas que esta opinião carrega (§6)

- **Só-texto:** medimos a intenção do plano, não o agente real com ferramentas. Não transfere direto ao produto.
- **N pequeno** (1 a 5 repetições por célula). Deltas-grandes-contra-ruído, não significância estatística.
- **Os juízes foram cross-vendor, não Claude sozinho.** O F0 usou 9 juízes de 3 empresas (7 convergiram). O R6
  trouxe um 2º juiz, o gpt-4.1-mini, que fechou o caveat de juiz único na nuvem, incluindo o reteste-limpo. O F4
  teve 92% entre o Gemini 2.5 Flash e o GPT-4.1, mais a conferência mecânica da abstenção §9. O resíduo é estreito: as rodadas
  ecológicas mais recentes deste ciclo (projetos próprios, fg2p) foram pontuadas por Claude e ainda não
  re-pontuadas cross-vendor. Viés de família medido (Claude ~0,87 ponto mais generoso com o Haiku), por isso não
  ancoramos em célula Claude-julga-Claude.
- **Circularidade:** quase todo o "real" testado é projeto **do próprio dono**, com gabarito do próprio dono. Em
  projeto público de terceiro o sinal **enfraquece** (quem detectou foi um modelo de fora da família), mas não
  some. Falta projetos de terceiros e um juiz de outro fabricante.
- **Ruído × forma-do-pedido confundidos:** o "limpo abstém / real sub-detecta" foi medido sob um pedido que já
  prima abstenção; falta cruzar com o pedido "ache problemas" para isolar.
- **A conferência por regex** dá falso-positivo dos dois lados; só fica limpa ancorada em ação de arquivo.
- **Tudo aqui é sinal / direção forte, não prova.**

## Resultado mais recente (resumo) — e onde está a evolução

- **Funciona (sólido):** consertar §5 e preservar §3, até no econômico; recusar injeção §6-bis; e 7 de 9 juízes
  de 3 empresas convergem, então não é auto-avaliação.
- **Funciona (sinal):** num projeto limpo, todos se abstêm; sob ruído, só o topo calibra.
- **Não funciona / em aberto:** auditor autônomo no projeto real (sub-detecção é o limite duro); verificação na
  web; agente com ferramentas reais; L1/L2.

Para a **evolução completa** — fase a fase, o que foi dito e descartado, os números por experimento:
[hub de arquitetura e evidências](ARQUITETURA-E-EVIDENCIAS.md) (histórico) ·
[`RESULTADOS-p10`](RESULTADOS-p10-escada-propria-genero.md) (projetos reais) ·
[`DOSSIE-judge`](DOSSIE-judge-justificativa-cientifica.md) (o juiz) ·
[`BACKLOG`](BACKLOG-fila-geral.md) (o que falta para firmar).
