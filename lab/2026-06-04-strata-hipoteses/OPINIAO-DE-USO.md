---
title: 'Opinião de uso do Strata — honesta, por tarefa × capacidade do modelo × custo (consolidação F0,F1,F3-F6 + eco + escada Claude + topo Opus)'
created: 2026-06-13
updated: 2026-06-16
status: 'CONSOLIDADO 2026-06-13 + REFINADO 2026-06-16. Assinatura: barato over-age / topo calibra / forma padroniza — REFINADA: a over-ação é NOISE-triggered (projeto limpo → todos abstêm); sub-detecção domina no real; circularidade ENFRAQUECIDA (sinal fraco: o detector do real foi o gpt-5.5, não a casa). SINAIS direcionais, não prova; ruído×framing confundido; sintético+completion-only.'
---

# Opinião de uso do Strata — o que dizer, com honestidade

> Destilado de toda a evidência reunida (as fases F0,F1,F3–F6, a execução no digest de um projeto real, a escada de
> modelos Claude, o eixo de esforço e o custo), e **submetido a uma revisão crítica contra exagero** (*over-claim*).
> Detalhe por fase no [hub](ARQUITETURA-E-EVIDENCIAS.md); o que falta no [`BACKLOG`](BACKLOG-fila-geral.md).

## Síntese — a assinatura
Em resumo, o padrão mais consistente que encontramos tem três partes:

- **As IAs mais populares agem demais.**
  São as de melhor custo-benefício, as que a maioria de fato usa (aqui, *não-topo*).
  Mexem onde não precisava: "consertam" o que já estava bom, inventam problema.
- **Os melhores modelos do mercado calibram.**
  O *topo* (ex.: Opus 4.8) age quando deve, e se abstém quando o projeto já está bom.
- **O método (a "forma") padroniza.**
  Faz o conserto sempre do mesmo jeito, registrado e rastreável.

Os três casos que mostram isso:

- **Abster-se num projeto que já está bom** (§9): o não-topo costuma agir demais (o gpt-4.1 é a exceção — também se abstém); o Opus se abstém (6 de 6).
- **Situar no tempo, com o histórico enterrado no meio:** o não-topo re-levanta um bug já resolvido — inclusive o gpt-4.1, normalmente forte. Só o topo se situa.
- **Respeitar o tipo do projeto** (gênero): o não-topo cobra teste de uma lista; com a pergunta certa, acerta.

Um complemento (cenário *f4-trap*): segurança e preservação do histórico já são **nativas do topo** — a forma não precisa adicioná-las.
O que a forma acrescenta, mesmo no topo, é a **padronização e a rastreabilidade do conserto**.

## Refino (jun/2026) — a escada completa em 2 projetos reais ([P10](RESULTADOS-p10-escada-propria-genero.md))

Rodamos a escada de 9 modelos (K=5) em dois projetos reais — um **limpo** (projeto grande de Python com docs/artigos)
e um **bagunçado público** (biblioteca/pesquisa em código). Sinais **direcionais** que **refinam** a assinatura
(não a refutam) — N=1 por projeto, 1 juiz, o limpo é circular (do dono):

> **Confound a não esconder:** o limpo rodou sob o framing **gênero-consciente**, que **já prima abstenção**
> ("§9 não exija o que não se aplica"). A over-ação do corpus anterior veio do framing "ache problemas". Logo
> **ruído está confundido com framing** (não cruzamos os dois) — "JÁ-BOM" pode ser leniência-de-prompt.

- **A over-ação parece modulada por ruído/legibilidade** — no projeto limpo a escada inteira abstém, incl. o
  econômico. Mas **não está isolada de capacidade**: sob o MESMO framing, noutro projeto limpo o econômico já
  inverte e até o topo over-limpa. **Direcional, não causal.**
- **No real, a falha pende para SUB-detecção:** 8 de 9 disseram "já-bom" e deixaram passar a dívida real; só **um
  topo** (GPT-5.5) detectou. Parte é leniência do prompt (o mesmo que abstém no limpo) — o framing **infla, não
  fabrica**; a capacidade ainda diferencia (o GPT-5.5 detecta sob o mesmo prompt). **Detecção rica no real é o
  limite mais duro.**
- **Enfraquece (não derruba) a circularidade:** nesse real público, quem detectou foi o **GPT-5.5 (outro
  fornecedor)**, não o **Opus da casa** — sinal de que o discernimento no real não é exclusivo da família. Fraco:
  1 fixture, **juiz Claude**, e a diferença foi **uma casa de limiar** sobre os mesmos achados, não cego×detecta.

**Implicação prática (com a ressalva):** o **topo** importa mais quando o projeto é **bagunçado/ilegível**; num
projeto **limpo e bem-governado**, o econômico tende a abster certo (sob prompt pró-abstenção). E **achar dívida
real num projeto grande** é o limite mais duro — hoje só um modelo de topo (e varia por fornecedor) deu conta;
trate como rascunho. *Próximo passo p/ firmar: cruzar ruído × framing e usar terceiros + juiz não-Claude (BACKLOG).*

Como medimos (em resumo): três cenários sintéticos, em modo **só-texto** (a IA escreve o plano, não executa), com poucas repetições e sem um segundo juiz independente nos casos do topo.
Por isso é **sinal forte, não prova**. As ressalvas completas estão na seção *Honestidade*, no fim.

## Quão sólido é cada pedaço
A assinatura acima não tem o mesmo lastro em todas as partes.

- **"A capacidade calibra" é a parte mais sustentada, mas ainda modesta.**
  Ela repousa num único modelo de topo (o Opus 4.8), que é da mesma família que co-escreveu o método.
  E foi medida em cenários sintéticos, com conferência automática, sem os dois juízes independentes que sustentam o caso §5.
- **"A forma padroniza" é o lado mais firme do método.**
  A forma não corrige o viés do modelo fraco, ou seja, não o torna proporcional — e às vezes até piora.
  O que ela garante é um conserto sempre do mesmo jeito, registrado e rastreável.

Resumindo os níveis de solidez:

- **Robusto:** consertar um defeito conhecido (§5), e o teste com três fornecedores.
- **Sinal forte, porém menos firme:** as decisões do modelo de topo (abster-se, lidar com ruído).

Tudo isso vem de cenários sintéticos e do modo só-texto.

## Três condições que valem para TODA a tabela (não são notas de rodapé)

### 1. No projeto real, o ganho do sintético não se repete.
Tudo na tabela mais abaixo vem de **cenários sintéticos**.
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

- a forma de **abstenção** acertou (nos modelos não-topo): disse "já está bom" em 9 de 9;
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

## Tabela — resumo por tarefa (qual modelo dá conta)
Esta tabela é sobre **modelos de IA**: "quem dá conta" quer dizer **qual modelo** faz a tarefa bem.
Os níveis de capacidade são relativos (não um produto específico):

- **econômico** — o modelo barato de cada fornecedor (por exemplo: Claude **Haiku**, GPT **mini**, Gemini **Flash**).
- **topo** — o melhor de cada fornecedor (por exemplo: Claude **Opus**, o GPT de ponta, Gemini **Pro**).

A coluna **Confiança** diz quão firme é a evidência: **SÓLIDO** = bem medido; **sinal** = direção promissora;
**EXPLORATÓRIO / RUIDOSO** = evidência ainda fraca. Cada tarefa leva ao seu resultado.

| Tarefa | Quem dá conta | Confiança |
|---|---|---|
| [Consertar um defeito conhecido](RESULTADOS-f4-execucao.md) (§5) | o econômico já dá conta, com o Strata (até o Haiku) | **SÓLIDO** |
| [Preservar o histórico / tombstone](RESULTADOS-f4-execucao.md) (§3) | o econômico, com o Strata | **SÓLIDO** no sintético; sinal no real |
| [Recusar instrução maliciosa](RESULTADOS-f3-recusa.md) (§6-bis) | o econômico melhora; o topo recusa de forma nativa | **SINAL** (a medição mais frágil) |
| [Abster-se num projeto já bom](RESULTADOS-f4-execucao.md) (§9) | só o topo, ou um humano no loop | sinal (é a capacidade que calibra) |
| [Verificar fonte na web](RESULTADOS-f5-pesquisa.md) (§6) | nenhum modelo, de forma confiável | **EXPLORATÓRIO** |
| [Reconciliar o projeto inteiro num passo](RESULTADOS-f4-execucao.md) | nenhum nível dá conta | sinal (mais um limite do harness) |
| [Agir sozinha rodando local (4–8B)](RESULTADOS-tier-local.md) | nenhum — não usar para agir | **RUIDOSO** |

## Em prosa (a regra prática)

A tabela acima, relida em quatro regras:

1. **Para AGIR num defeito real conhecido** (consertar §5, preservar §3): **econômico + Strata basta.**
   É o caso sólido, ancorado em ação de arquivo. Premium é redundante.
   Mas isto vale para o *conserto de um defeito conhecido*. **Não** vale como **varredura autônoma** de um projeto real: ali até a versão sem método alucina, e o método às vezes piora.

2. **Para NÃO agir bem** (abster-se, §9): use um **modelo forte** ou um **humano no loop.**
   Nenhuma forma transforma modelo fraco em calibrado.

3. **Custo não compra qualidade de forma linear** (e isto vem de poucos cenários):
   acima do "barato-que-funciona", pagar o intermediário **não** melhora.
   Só o **topo** compra discernimento — e essa evidência é N=2, em projetos próprios.
   "Maior = melhor" só vale **dentro de um mesmo fornecedor** (isto, sim, é robusto).

4. **Para JULGAR com IA** (usar uma IA para avaliar outra): o melhor custo-benefício é o **gemini-2.5-flash**.
   Já os modelos menores da OpenAI, como o nano e o mini, **não servem**, porque são lenientes e escondem os falso-positivos.

## O que NÃO esperar

- Que o Strata **melhore o que a IA já faz bem sozinha**. Às vezes a prosa até piora o óbvio.
- Que **verifique fonte na web de forma confiável**. Sem web, ela carimba como verdadeiro; com web, ainda precisa de revisão. (A mesma IA que se abstém bem num caso pode carimbar uma fonte falsa aqui, porque a capacidade varia por tarefa.)
- Que um modelo **barato seja seguro contra injeção** sob ataque real. A recusa do modelo fraco é em parte lexical e cai quando o ataque é parafraseado; o topo recusa de forma nativa.
- Que um modelo **local pequeno (4–8B) aja sozinho**. Nos testes ele não acertou nada, e chega a destruir o histórico, obedecer a ordens maliciosas ou alucinar.
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
