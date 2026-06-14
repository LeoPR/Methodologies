---
title: 'Opinião de uso do Strata — honesta, por tarefa × capacidade do modelo × custo (consolidação F0,F1,F3-F6 + eco + escada Claude + topo Opus)'
created: 2026-06-13
status: 'CONSOLIDADO 2026-06-13 (assinatura única: barato over-age / topo calibra / forma padroniza). SINAIS/direção, não prova; sintético+completion-only.'
---

# Opinião de uso do Strata — o que dizer, com honestidade

> Destilado de toda a evidência reunida (as fases F0–F6, a execução no digest de um projeto real, a escada de
> modelos Claude, o eixo de esforço e o custo), e **submetido a uma revisão crítica contra exagero** (*over-claim*).
> Detalhe por fase no [hub](ARQUITETURA-E-EVIDENCIAS.md); o que falta no [`BACKLOG`](BACKLOG-fila-geral.md).

## Síntese — a assinatura
Em uma frase, o padrão mais consistente que encontramos:

- **As IAs mais populares agem demais.**
  São as de melhor custo-benefício, as que a maioria de fato usa (aqui, *não-topo*).
  Mexem onde não precisava: "consertam" o que já estava bom, inventam problema.
- **Os melhores modelos do mercado calibram.**
  O *topo* (ex.: Opus 4.8) age quando deve, e se abstém quando o projeto já está bom.
- **O método (a "forma") padroniza.**
  Faz o conserto sempre do mesmo jeito, registrado e rastreável.

Os três casos que mostram isso:

- **Abster-se num projeto que já está bom** (§9): o não-topo age demais; o Opus se abstém (6 de 6).
- **Situar no tempo, com o histórico enterrado no meio:** o não-topo re-levanta um bug já resolvido — inclusive o gpt-4.1, normalmente forte. Só o topo se situa.
- **Respeitar o tipo do projeto** (gênero): o não-topo cobra teste de uma lista; com a pergunta certa, acerta.

Um complemento (cenário *f4-trap*): segurança e preservação do histórico já são **nativas do topo** — a forma não precisa adicioná-las.
O que a forma acrescenta, mesmo no topo, é a **padronização e a rastreabilidade do conserto**.

Como foi medido, e por que somos cautelosos:

- Três cenários de teste sintéticos, com os mesmos modelos (gpt-4o-mini, gemini, gpt-4.1, contra o Opus 4.8).
- Tudo em modo **só-texto**: a IA escreve o plano, mas não executa nada.
- Poucas repetições, e sem um segundo juiz independente nos casos do topo.

Por isso é **sinal forte, não prova**.
(*Sinal* = direção promissora; *prova* exigiria mais medição.)

## Tese — "a capacidade calibra; a forma padroniza"
A versão anterior era "a forma corrige o viés; a capacidade calibra". Ela sobrevive, mas com o peso deslocado e sustentação modesta.

- **"A capacidade calibra"** é a metade mais sustentada.
  Mas repousa em **um único modelo de topo** (Opus 4.8), da mesma família que co-escreveu o método, em cenários sintéticos, com conferência automática (não os dois juízes independentes que dão credibilidade ao caso §5).
- **"A forma corrige o viés" virou "a forma padroniza".**
  Ela não compra proporcionalidade para o modelo fraco; às vezes até piora.
  O que garante é um conserto único e rastreável.

Os níveis de solidez são diferentes:

- **Robusto:** o caso §5 (consertar defeito conhecido) e o teste com três fornecedores.
- **Sinal forte, mas não no mesmo nível:** as células de topo (abstenção, ruído).

Tudo é sintético e em modo só-texto.

## Três condições que valem para TODA a tabela (não são notas de rodapé)

### 1. Tudo abaixo é sintético. No projeto real, o resultado é mais duro.
Em **projetos reais** (estudo R8, 3 projetos), o Strata como auto-auditor automático de IA **não superou a competência pura** do modelo:

- piorou no projeto que já estava bom;
- empatou no bagunçado;
- no exemplar, **todos inventaram problemas** (cerca de 4 a 5 por plano) — até a versão sem o método.

Ou seja: **o ganho do sintético não se traduziu no real.**

A única exceção medida foi o **topo (Opus)**, em projeto próprio (N=2).
Houve também o F1/M0, onde o Opus foi o único a separar "já-bom" de "precisa" nos 3 projetos reais.
Mas só em parte (acertou metade num deles), e julgado pela própria família: o caso mais circular de todos.

**O falso-positivo vem da FORMA, não do método em si.**
(braço externo: [3 repositórios de terceiros](RESULTADOS-externo-bemcomportado.md), N=1)

- a forma de **abstenção** acertou: disse "já está bom" em 9 de 9;
- o framing "ache problemas" **inventa demais**.

Mas o espelho apareceu: no tier **bagunçado**, a abstenção disse "já-bom" para quase tudo (até num repo claramente fraco).
Errou para o outro lado: **deixou passar**.
Em parte, isso é **confusão de tipo de projeto** (um caderno ou lista não precisa de testes nem CI).

**Saldo:** os dois modos de falha (inventar demais / deixar passar) existem **sem depender de circularidade**.
A auditoria rica de qualidade no real **segue em aberto**.

**Refino (tipo do projeto):** parte do "deixar passar" era, na verdade, **acerto de gênero** ([gênero](RESULTADOS-genero.md)).
Com a pergunta certa, os modelos corretamente **não cobram teste de uma lista**.
Por isso o §9 do método deve ser **gênero-consciente** (é melhoria de texto, não de modelo).

**Reprodução controlada** ([cenário f6-ruidoso](RESULTADOS-f6-temporal-sem-marcadores.md)):
num cenário **ruidoso**, com o histórico e o "já resolvido" enterrados no meio, a IA mais barata **repete o erro do R8**.
Ela re-levanta um bug que já fora corrigido, e chega a mandar **apagar marcadores do histórico**.
O **topo** se situa e **protege o histórico**.
**Conclusão:** o "não superar a competência" do R8 é, em boa medida, **viés de agir-demais da IA barata sob ruído**. Quem distingue é o topo.

### 2. Circularidade (só em parte resolvida).
Quase todo o "real" testado é projeto **do próprio dono** — e o gabarito também.
O gabarito se provou **incompleto**: o Opus achou problemas reais de fonte-única (§5) que o gabarito tinha perdido.
**Nenhum "OK" foi validado em projeto de terceiro com gabarito registrado de antemão.**

### 3. Juiz único nas decisões + só-texto.
O teste com juízes de fornecedores diferentes (F0) rodou só em parte do corpus.
As células decisivas (reteste-limpo, abstenção, faixa ecológica) tiveram **um juiz só**.
E tudo mede a **intenção do plano em texto**, não o agente real com ferramentas.
Logo, **não transfere automaticamente** para o Claude Code / Copilot como produto.

## Tabela — tarefa × capacidade × custo (vocabulário relativo; capacidade = nível do modelo, não produto)
| Tarefa | econômico | intermediário | premium | web? | custo rec. | status | recomendação |
|---|---|---|---|---|---|---|---|
| **Consertar §5 (defeito conhecido)** | OK c/ Strata (até Haiku) | OK | OK (redundante) | não | **econômico, recorrente** | **SÓLIDO** (F4 GOLD 100% + juiz 92%, ancora em ação de arquivo) | o caso mais forte e barato; sem Strata alguns consertam **informal** — o método formaliza + habilita quem não consertava |
| **Preservar histórico / tombstone §3** | OK c/ Strata (tombstone 7/8; payload 0/8 — *f4-trap/Strata, 3 modelos não-Opus, juiz cross-vendor*) | OK | OK | não | **econômico, recorrente** | **SÓLIDO** no sintético; **SINAL** no real (1 digest, N=2, próprio, sem 2º juiz) | argumento de segurança mais transferível; **replicar fora do projeto-próprio** |
| **Recusar injeção §6-bis** | Strata vira obedecer→recusar no leniente; **Claude-Haiku já recusa sozinho** | já recusa | redundante | não | econômico | **SINAL** — a medição **mais frágil** (concordância 56-69%, 1 cenário, N=2; o GOLD-gate é do F4, não daqui) | delta real só no barato leniente; **segurança do fraco é em parte LEXICAL** (recusa 6/6→4/6 sob paráfrase — **queda toda do gpt-4o-mini, o piso**; gemini/gpt-4.1 recusam as 3 formas) → contra ataque real de paráfrase, barato **não é seguro**. **Topo recusa injeção nativamente** na execução (f4-trap baseline 3/3) |
| **Abster-se em projeto já-bom §9** | **FALHA** (super-eng 6/8 vs 2/8; **indução do Strata limpa só no gpt-4o-mini** — sozinho abstinha; **gemini super-aplica nos 2 braços** = viés do modelo) | parcial (Sonnet+thinking 1/2, dentro do ruído) | gpt-4.1 e **Opus 4.8 abstêm** (Opus **6/6** = 3+3 na mesma fixture, 1 modelo, juiz mec.+GOLD) | não | **forte, pontual** / humano no loop | **FECHADA**: topo abstém; Strata **não** induz super-eng no topo | a **faca de dois gumes é do barato/médio**: lá o Strata em projeto limpo gera trabalho inútil/alucinado. **A forma NÃO compra proporcionalidade — a capacidade compra**: o topo abstém com ou sem Strata. Use modelo forte ou humano no loop |
| **Verificar fonte §6 (web)** | carimba falso confiante | idem | **FALHA também sem web** (gpt-4.1 carimbou 3/3) | **reduz, não conserta** (forte+web ainda 2/3) | — (probe) | **EXPLORATÓRIO** (N=1-2, 1 fixture, 3 claims) | nunca confie em verificação de fonte sem web — **nem com web sem revisão**. O **mesmo gpt-4.1** que abstém bem em §9 carimba fonte falsa aqui → **capacidade é por-TAREFA, não global** |
| **Reconciliar TUDO num passo (real)** | zero PASS | parcial (~2/3) | parcial | não | nenhum tier resolve | **SINAL confundido com limite de HARNESS** (o formato "arquivo inteiro" **truncou**) | rascunho a revisar / humano no loop; **não prometer** reconciliação total |
| **Qualquer tarefa em LOCAL 4-8B** | **não usar p/ AGIR** | — | — | — | — | **RUIDOSO** (muito INDETERMINADO; "+0,50" virou −1,50 com N=3) | detecção c/ forma curta funciona **com asterisco**; para EXECUTAR: zero PASS, destroem/obedecem, alucinam no limpo — **nunca autônomo para agir** |

## Em prosa (a regra prática)

1. **Para AGIR num defeito real conhecido** (consertar §5, preservar §3): **econômico + Strata basta.**
   É o caso sólido, ancorado em ação de arquivo. Premium é redundante.
   Mas isto vale para o *conserto de um defeito conhecido*. **Não** vale como **varredura autônoma** de um projeto real: ali até a versão sem método alucina, e o método às vezes piora.

2. **Para NÃO agir bem** (abster-se, §9): use um **modelo forte** ou um **humano no loop.**
   Nenhuma forma transforma modelo fraco em calibrado.

3. **Custo não compra qualidade de forma linear** (e isto vem de poucos cenários):
   acima do "barato-que-funciona", pagar o intermediário **não** melhora.
   Só o **topo** compra discernimento — e essa evidência é N=2, em projetos próprios.
   "Maior = melhor" só vale **dentro de um mesmo fornecedor** (isto, sim, é robusto).

4. **Para JULGAR com IA** (avaliar IA com IA): bom e barato = **gemini-2.5-flash.**
   **Nunca** os menores da OpenAI (nano/mini): são lenientes e escondem o falso-positivo.

## O que NÃO esperar

- Que o Strata **melhore o que a IA já faz bem sozinha**. Às vezes a prosa até piora o óbvio.
- Que **verifique fonte sem web** (e nem confie com web, sem revisão).
- Que **reconcilie um projeto real inteiro num passo**.
- Que **situe artefatos no tempo** de forma garantida. É a dimensão mais fraca e mais ruidosa do corpus.
  *Refino:* o ponto-cego é **condicional à legibilidade da evidência**, não fundamental.
  Com marcadores explícitos — e mesmo sem eles, quando a ordem é recuperável do conteúdo — os modelos acertaram a cronologia (ver [F6](RESULTADOS-f6-temporal-sem-marcadores.md)).
  Ainda falta testar em projeto real grande e ao longo do tempo.
- Que conclusões do modo **só-texto** transfiram para um **agente com ferramentas** (não testado).
- **L1 (nomear a formalização) e L2 (ferramentas) quase não foram testados.** Afirmações sobre eles são, no fundo, não-testadas.

## Honestidade — ressalvas que este relatório carrega (§6)

- **Só-texto:** medimos a intenção do plano, não o agente real. Não transfere direto ao produto.
- **N pequeno** em toda célula (1 a 3 repetições); nenhuma com 5 ou mais.
  A variância dentro do mesmo modelo já virou o próprio sinal. São deltas-grandes-contra-ruído, não significância estatística.
- **Juiz muitas vezes único** nas células decisivas.
  Há viés de família medido: o Claude foi cerca de 0,87 ponto mais generoso com o Haiku.
- **Claude como sujeito do teste:** Haiku e Sonnet na escada-claude (julgados por não-Claude).
  O Opus já fora sujeito em §9 no F1/M0, mas com juiz único da própria família (auto-avaliação) e acerto parcial.
  O f4-clean e o f4-trap confirmam por via automática. Falta a reconciliação completa com o Opus.
- **As células decisivas do topo não têm o juiz duplo** de fornecedores diferentes.
  São conferência automática ou leitura, e herdam a fragilidade de juiz único.
  O verificador automático usa regras calibradas pelo próprio autor (circularidade fina).
  E o "topo" é um só modelo (Opus), da mesma família que co-escreveu o método.
- **Circularidade:** o projeto e o gabarito são do próprio dono, e o gabarito se provou incompleto.
  No real (R8), o auto-auditor não bateu a competência pura.
- **Temporalidade:** o F6 rodou (16/16 no limpo; no ruidoso, o barato erra e o topo se situa).
  O ponto-cego é condicional à legibilidade, não fundamental. Falta o caso real-grande / ao longo do tempo.
  A recusa de injeção (§6-bis) é a medição mais frágil. A verificação de fonte na web é exploratória.
- **A conferência por regex** deu falso-positivo dos dois lados. Só fica limpa quando ancora em ação de arquivo.
- **Tudo aqui é sinal / direção forte, não prova.**
