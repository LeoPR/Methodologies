---
title: 'Comporta: plano v2 (replanejamento)'
created: 2026-10-01
updated: 2026-10-01
status: 'Decidido pelo dono em 2026-10-01 (escopo com uso interativo, cortes, fronteira (a)). Substitui o plano-experimental.md como plano ativo.'
tags: [comporta, plano, replanejamento, roteamento, custo]
---

# Comporta: plano v2

## Decisões do dono (2026-10-01)

1. **Escopo da v1:** inclui a economia no uso interativo (M2), como complemento da escolha de modelo,
   rota e configuração.
2. **Cortes:** aprovados (Foundry Local, o Estágio 6 de junho, a matriz com multiplier 0).
3. **Fronteira:** (a). A recipe do Comporta fica com rota e custo; o guia do Strata aponta para ela.

## Por que replanejar

O plano de junho ([plano-experimental.md](plano-experimental.md)) pôs fatos de fornecedor na
condição de destilar a recipe: a matriz "fornecedor × tarefa" girava em torno dos modelos
"multiplier 0" do Copilot. Esses fatos expiraram.

Verificado em fonte primária em 2026-10-01:

- **Cobrança por uso.** O Copilot cobra por uso (AI Credits, ao preço de API de cada modelo) desde
  2026-06-01. **Nenhum modelo custa zero** nos planos pagos. Premium requests e multiplicadores
  viraram regime legado (só planos anuais antigos).
- **GitHub Models aposentado** em 2026-07-30, inclusive a API de inferência.
- **O que sobrevive:**
  - o **autocomplete continua ilimitado** nos planos pagos;
  - o VS Code aceita **modelo local** (Ollama) no chat e no agente via BYOK, inclusive sem plano do
    Copilot, mas **não** no autocomplete.

Fontes:
- github.blog, 2026-04-27, "GitHub Copilot is moving to usage-based billing";
- changelog de 2026-06-01, "updates to GitHub Copilot billing and plans";
- docs.github.com: models-and-pricing;
- changelog de 2026-07-01, GitHub Models "fully retired on July 30";
- code.visualstudio.com/blogs/2026/06/18/byok-vscode.

O núcleo do Comporta **não** expirou. O [mapa](mapa-recursos-llm.md) continua válido: as 4
primitivas, a falta de um escalar de esforço, o "sempre ótimo / depende / só medindo / chute" e as
leis físicas e de contrato.

## A estrutura em camadas (a mesma do Strata)

O erro de junho foi misturar camadas. A v2 separa:

| camada | o que é | exemplos |
|---|---|---|
| **L0** | o que vale com qualquer fornecedor | as 4 primitivas; não há escalar de esforço; a capacidade é dos pesos e a viabilidade é da máquina; saída custa mais que entrada enquanto se paga por token |
| **L1** | formalizações nomeadas | roofline; roteamento por dificuldade (FrugalGPT, RouteLLM); K-quants; prompt caching; speculative decoding |
| **L2** | fornecedores, planos, preços, rotas, ferramentas | NVIDIA NIM, OpenRouter, Copilot, Ollama; datado, com revalidação |

Consequência: **a condição de destilar depende só de vereditos L0/L1**. A L2 entra como instância
datada e se troca sem mexer no resto.

## A pergunta, reancorada

> Para uma tarefa, qual combinação de **modelo, rota e configuração** entrega o necessário ao menor
> custo de dinheiro e tempo, e o que precisa ficar fixo para o resultado ser confiável?

- A unidade é **(modelo × rota × configuração) × classe de tarefa**.
- A configuração inclui quantização, nível de raciocínio e teto de saída.
- A máquina local é **uma rota entre outras**. Ela mede viabilidade; a capacidade se mede na nuvem,
  nos mesmos pesos (decisão de 2026-08-02).

## O que já tem evidência (colheita, sem rodar nada)

A maior parte da evidência de que o Comporta precisa foi produzida no trabalho do Strata e da
Temporalidade, com o harness de `eval/`.

| decisão que a recipe precisa dar | veredito | evidência | camada |
|---|---|---|---|
| **D1. Onde medir capacidade** | na nuvem, nos mesmos pesos; o local mede viabilidade e serve de ponte | decisão de 2026-08-02; [STAGE5](instrumento/STAGE5.md); ponte do [banco](../2026-09-26-banco-modelos/README.md) | L0 |
| **D2. Quando o local compensa** | quando pesos + KV cabem e a velocidade serve à tarefa; tool_use local é viável com o modelo certo; autocomplete local responde rápido | [STAGE2](instrumento/STAGE2.md), [STAGE3](instrumento/STAGE3.md), [STAGE4](instrumento/STAGE4.md) C1, [STAGE5](instrumento/STAGE5.md) | L0 + L2 |
| **D3. A rota é parte da configuração** | mesmos pesos não garantem mesmo comportamento: a quantização varia por provedor; parâmetros são descartados em silêncio (temperatura, nível de raciocínio); uma implantação entrou em laço onde a oficial concluía. Fixar a rota quando o resultado importa e registrar o provedor servido | [bateria v1](../2026-09-26-temporalidade/RESULTADOS-bateria-v1.md) e §9 do [PREREG](../2026-09-26-temporalidade/PREREG-bateria-v1.md); banco refeito; ressalva nos [resultados F6](../2026-09-26-temporalidade/RESULTADOS-f6-fonte.md) | L0 (princípio) + L2 |
| **D4. Teto de saída e raciocínio** | resposta cortada pelo teto mede o teto, não o modelo; raciocínio alto nunca melhorou uma célula, custou mais e às vezes piorou | eixo de pensamento do banco; leitura complementar da bateria (8k → 32k) | L0 + L1 (P20 do mapa) |
| **D5. Grátis × pago** | há rota grátis que faz tudo, com latência maior; erro passageiro de rota não é propriedade do modelo | [banco](../2026-09-26-banco-modelos/README.md); guia `recipe/strata-com-ia.*` | L2 |
| **D6. Custo por tarefa, não por token** | o custo real vem da chamada; projeção por catálogo errou por fator de algumas vezes | gastos da bateria v1 (projeção × custo real) | L1 (P22 do mapa) |
| **D7. Assinatura × pagamento por uso** | no uso agêntico pesado (perfil do dono), a assinatura sai de 16 a 37 vezes mais barata; pagando por token, a alavanca é o contexto acumulado (cache), não a saída; o local não comporta o contexto do harness agêntico e fica no autocomplete e no chat curto | [M2a](instrumento/M2A.md); verificação de 2026-10-01 (acima) | L0 (princípio) + L2 (preços) |
| **D8. Contexto** (cache, ordem, distratores) | literatura consolidada | [mapa](mapa-recursos-llm.md) §3 | L1 |

## O que falta medir (só o que nenhuma evidência cobre)

- **M1 (opcional).** Variância entre provedores com os mesmos pesos, desenhada e pré-registrada.
  - Hoje há casos, não taxa: um laço, um parâmetro descartado.
  - Se a recipe só precisa dizer "fixe a rota", M1 não é necessário.
- **M2 (no escopo, decidido).** Economia no uso interativo, que era o caso de origem: o dev no
  VS Code. Desenho em rascunho na seção seguinte.

## M2: desenho (fechado com o dono em 2026-10-01)

O Copilot cobra cada token ao preço de API do modelo. Então o custo de uma tarefa de chat ou de
agente se calcula por tokens × preço, sem automatizar o Copilot (a política dele proíbe atividade
automatizada em massa). Isso divide o M2 em duas partes.

- **M2a. Custo por tarefa (calculável).**
  - Classes de tarefa interativa: pergunta ou explicação curta; edição pequena num arquivo; tarefa
    de agente em vários arquivos; revisão de diff.
  - Perfil de tokens de cada classe, tirado de onde já é registrado (os transcripts do Claude Code,
    via `instrumento/parse_usage.py`) ou de tarefas-modelo rodadas no harness nos mesmos pesos.
  - Custo por rota: créditos do Copilot ao preço publicado; OpenRouter; local (custo marginal zero,
    medido em tempo).
- **M2b. O que só o uso mede.**
  - Autocomplete: aceitação local (extensão própria) × Copilot.
  - Chat e agente locais (BYOK): resolveu, escalou para a nuvem ou desistiu.
  - Atrito percebido.
  - Instrumento: um diário curto (uma linha por tarefa: classe, rota, desfecho) somado aos logs
    automáticos (transcripts do Claude Code; saldo de créditos do Copilot por dia).
  - Duração proposta: duas semanas de uso normal.
- **Limite declarado.** O M2b é observacional: quem usa escolhe a rota pela dificuldade, então as
  conclusões são descritivas. O M2a é o que permite comparar rotas na mesma tarefa.
- **Respostas do dono (2026-10-01):** Copilot Pro+; Claude Max; modelos locais pelo Ollama no Docker
  Desktop; topa o diário.
- **Estado:** M2a executado ([M2A](instrumento/M2A.md)); M2b aberto ([diário](M2B-diario.md)).

## Cortes (aprovados)

- **B4a** (Foundry Local na linha de comando): o catálogo estava inacessível em junho. Sai, salvo se
  o dono usar o Foundry.
- **Estágio 6 antigo** (Claude Code roteado para o local, subagente mais barato, pré-sumarização):
  - foi desenhado para o regime de junho;
  - sai como estágio próprio;
  - com o M2 no escopo, essas ideias entram, se entrarem, como rotas comparadas no M2a, não como
    bateria separada.
- **Matriz "fornecedor × tarefa" com multiplier 0:** sai. Os vereditos D1–D8 a substituem.

## Condição para destilar (v2)

- **Recipe v1:** escolher modelo, rota e configuração, o papel da máquina local e a economia no
  uso interativo.
  - A parte de escolha destila quando D1–D6 e D8 têm veredito com evidência. Pela tabela acima, isso
    **já está perto**.
  - A parte interativa (D7) destila com o M2a, e o M2b a complementa quando o uso real terminar.
- **Critério de descarte:** se a recipe v1 não muda nenhuma decisão em relação ao guia
  `recipe/strata-com-ia.*`, o Comporta não justifica produto próprio. Nesse caso, o conteúdo vira
  seção do guia do Strata.

## Fronteira com o Strata (decidido: opção a)

O guia `recipe/strata-com-ia.*` já carrega rota, custo, grátis e local. A Parte III do canônico diz
que economia e roteamento são do Comporta. Opções:

- **(a)** A recipe do Comporta absorve rota e custo. O guia do Strata fica com "qual modelo faz bem o
  Strata" e aponta para o Comporta. **Recomendada**, se a destilação acontecer.
- **(b)** O Comporta fica só no `lab/`, e o guia do Strata segue como produto prático.

## Próximos passos, em ordem

1. ~~Decisões do dono~~ (feito, acima).
2. ~~Limpar a superfície do README~~ (feito: detalhe de junho fora; "Resultado C" reverificado).
3. ~~Mapa~~ (feito: os achados D3/D4 entraram no [mapa](mapa-recursos-llm.md) como movimento 9,
   P34 e chutes; a tabela D1–D8 acima é o consolidado, sem cópia).
4. ~~Fechar o M2 com o dono e rodar o M2a~~ (feito: [M2A](instrumento/M2A.md)). M2b: diário de 2026-10-02 a
   2026-10-15.
5. **Destilar a recipe v1** (EN primeiro, PT no mesmo commit, como o Strata), com a parte de escolha
   assim que pronta e a parte interativa depois do M2a.
