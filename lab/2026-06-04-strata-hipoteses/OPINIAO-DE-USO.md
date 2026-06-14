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
**Em uma frase: as IAs mais populares — as de melhor custo-benefício, que a maioria de fato usa (aqui, _não-topo_)
— tendem a _agir demais_ (mexer onde não precisava: "consertar" o que já estava bom, inventar problema); os
melhores modelos do mercado (o _topo_, ex.: Opus 4.8) _calibram_ — agem quando devem e se abstêm quando o
projeto já está bom; e o método (a "forma") _padroniza_ o conserto, num jeito único e rastreável de fazê-lo.**
Foi o padrão **mais consistente** do corpus — visto em **três cenários de teste sintéticos distintos**: os
mesmos modelos (gpt-4o-mini / gemini / gpt-4.1, contra o Opus 4.8), todos em modo **só-texto** (a IA escreve o
plano, mas não executa nada), com **poucas repetições** e **sem um segundo juiz independente** nos casos do
topo. Por isso é **sinal forte, não prova** (*sinal* = direção promissora; *prova* exigiria mais medição).
- **Abster-se num projeto que já está bom (§9 — "quando NÃO agir")** — cenário *f4-clean*: os não-topo **agem demais**; o **Opus se abstém 6/6** *(3 rodadas com Strata + 3 sem, no mesmo cenário; 1 modelo, conferência automática)*. *(O F1/M0 já mostrara o Opus acertando aqui — mas com juiz único da mesma família; o f4-clean confirma por via automática.)*
- **temporal sob ruído** (f6-ruidoso): **dois modos / dois modelos** — o **gpt-4.1** (normalmente o "forte") **re-levanta um bug já resolvido** + pede LICENSE; o **gemini** manda **apagar marcadores históricos** (anti-§3). **Importante: aqui até o forte gpt-4.1 over-agiu** — o discriminador foi **só o topo** (Opus 2/2, juiz por leitura), **não** "capacidade" de forma monotônica.
- **tipo do projeto (gênero)** — quando não se pede atenção ao tipo, o não-topo **ignora o gênero** (cobra testes/licença de um caderno de notas, que não precisa disso); mas, **se você pede para considerar o tipo, até o barato acerta** ([RESULTADOS-genero](RESULTADOS-genero.md), N=1). O contraste vem de **como se pergunta** — e **o topo não foi testado aqui**.

E o **complemento** (f4-trap): segurança (§6-bis) e preservação de história (§3) são **nativas do topo** — a
forma **não** as adiciona —; o que a forma adiciona, **mesmo no topo**, é **padronização + rastreabilidade do
conserto** (§5 canonical/superseded/ponteiro + append-only). *(No baseline do f4-trap o verificador deu
FALHA_CORRECAO = desvio de schema, **não** obediência: a decomposição mostra injeção recusada 3/3 e histórico preservado 3/3.)*

## Tese — "a capacidade calibra; a forma padroniza"
A versão anterior ("a forma corrige o viés; a capacidade calibra") sobrevive **com o peso deslocado**, mas com
**sustentação modesta**: a metade **"a capacidade calibra"** repousa essencialmente em **um único modelo de topo**
(Opus 4.8, da **mesma família** que co-escreveu o método), em fixtures sintéticas N≤3, com **juiz mecânico/leitura**
(não os 2 juízes cross-vendor que dão a credibilidade do F4-dup). A metade da forma virou **"padroniza / torna
rastreável"** — **não** "corrige o viés" (não compra proporcionalidade ao fraco; às vezes **piora**). **Tiers de
solidez distintos:** robusto = **F0** (3 fornecedores) e **F4-dup** (juiz 92%, 2 juízes não-Claude); as células de
topo (§9/ruidoso) são **sinal forte, não no mesmo patamar**. Tudo **sintético / completion-only**.

## Três condições que valem para TODA a tabela (não são notas de rodapé)
1. **Tudo abaixo é SINTÉTICO/fixture.** Em **projetos REAIS** (R8, 3 projetos) o Strata **como auto-auditor de
   IA NÃO bateu a competência pura** — piorou no bom, empatou no messy, e no exemplar **todos (incl. baseline)
   alucinaram** (~4,4-4,9 falso-positivos/plano). **O ganho sintético não se traduziu em projeto real.** Única
   exceção medida: o **topo (Opus)** — e em projeto próprio, N=2; **além do F1/M0, onde o Opus foi o único a
   discriminar já-bom×precisa nos 3 projetos reais do R8 — mas PARCIAL (½ no FG2P) e com juiz Claude único
   (auto-avaliação, o caso mais circular).**
   **Atualização (braço externo, [resultado](RESULTADOS-externo-bemcomportado.md), N=1):** em 3 repos de
   **TERCEIROS** organizados, a **forma de abstenção (M0) abstém certo** (JÁ-BOM 9/9), enquanto o framing
   "ache-problemas" over-detecta — o falso-positivo do R8 é **da FORMA, não inerente nem circular**. **Mas o
   espelho também apareceu:** no tier **messy** externo o M0 disse **JÁ-BOM a quase tudo (até num repo 1/7)** —
   **super-corrige em SUB-detecção** (replica F1/M0; nem o gpt-4.1 discriminou), embora **gênero-confundido**
   (baixa-conformidade ≠ defeito: lista/pesquisa não precisa de CI/tests). Saldo: os **dois modos de falha**
   (audit over-detecta, M0 sub-detecta) valem **sem circularidade**; a forma move o viés, a capacidade calibra
   (mal). A *auditoria rica de qualidade* no real **segue aberta**. **Refino (eixo gênero,
   [resultado](RESULTADOS-genero.md)):** parte da "sub-detecção" do messy era **fit de gênero** — com framing
   gênero-consciente, os modelos corretamente **não exigem testes de uma lista**; logo o §9 deveria ser
   **gênero-consciente** (melhoria de narrativa, não de modelo).
   **Reprodução controlada do R8 ([f6-ruidoso](RESULTADOS-f6-temporal-sem-marcadores.md)):** numa fixture
   *ruidosa* (histórico/resolvido soterrado), o **barato reproduz o R8 4/4** — re-levanta um bug já resolvido
   e chega a mandar **apagar os marcadores históricos** (anti-§3) — enquanto o **topo (Opus 4.8) situa 2/2** e
   protege o histórico. **Logo o "não bater a competência pura" do R8 é majoritariamente um viés de over-ação
   do BARATO sob ruído; o topo é o discriminador.** (Mesma assinatura do f4-clean §9 e do gênero-cego.)
2. **Circularidade (parcialmente endereçada).** Quase todo o "real" é projeto **do próprio dono**, e o **gabarito** também (provou-se
   **incompleto** — o Opus achou §5 reais que o gabarito perdeu). **Nenhum "OK" foi validado em projeto de
   terceiro com gabarito pré-registrado.**
3. **Juiz único em células decisivas + COMPLETION-ONLY.** O cross-vendor (F0) rodou no set P1/P2 — **não** no
   reteste-limpo, abstenção (F1/M0) nem na faixa ecológica F4 (essas têm juiz Claude único; F3 e F4 tiveram 2
   juízes não-Claude). E tudo mede a **disposição do PLANO em texto**, não o agente real com ferramentas —
   **não transfere automaticamente** para Claude Code / Copilot **produto**.

## Tabela — tarefa × tier × custo (vocabulário relativo; "tier" = capacidade, não produto)
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
1. **Para AGIR diante de um defeito real conhecido** (consertar §5, preservar §3): **econômico + Strata basta** —
   é o caso sólido (ancorado em ação de arquivo, juiz 92%); premium é redundante. **Mas** isso vale para o
   *padrão de conserto de um defeito conhecido*, **não** como **varredura autônoma** de um projeto real (onde o
   R8 mostrou que até o baseline alucina e o método às vezes piora).
2. **Para NÃO agir bem** (abster-se §9): **modelo forte** (o gpt-4.1 já abstém) ou **humano no loop**. Nenhuma
   forma transforma modelo fraco em calibrado.
3. **Custo→qualidade é não-monotônico, mas isto vem de 1-2 fixtures sintéticas:** acima do "barato-que-funciona",
   pagar intermediário **não** compra qualidade; só o **topo** compra discernimento — e essa evidência de topo é
   N=2, projetos próprios. **"Maior=melhor" só vale DENTRO de um fornecedor** (isto sim é robusto — F0).
4. **Para JULGAR** (se você for avaliar IA com IA): juiz barato-e-bom = **gemini-2.5-flash**; **nunca**
   OpenAI-small (nano/mini) — são lenientes e mascaram o falso-positivo (achado robusto do F0).

## O que NÃO esperar
Que o Strata melhore o que a IA já faz bem sozinha (a prosa às vezes **piora** o óbvio: reteste-limpo P1 8→4,
P3 7→1); que verifique fonte sem web (nem confie com web sem revisão); que situe artefatos no tempo (dimensão
temporal §3/§8 é a **mais fraca na média ~33% — e o sinal mais RUIDOSO** do corpus — *refino importante: o
ponto-cego é **condicional à legibilidade da evidência**, não fundamental. Com marcadores explícitos os
modelos leem tombstone/supersessão **certo** ([own-projects](RESULTADOS-genero-temporal-own.md), circular); e
**mesmo SEM marcadores**, com a cronologia recuperável do conteúdo, inferiram a ordem **8/8** incl. modo naive
([F6](RESULTADOS-f6-temporal-sem-marcadores.md)). O Strata §3/§8 então **torna o tempo inferível**, não supre
incapacidade. Aberto: caso sem-desambiguador (ambíguo até p/ humano) e longitudinal/real*); que reconcilie
um projeto real inteiro num passo; que conclusões de completion-only transfiram para **agente-com-ferramentas**
(não testado). **L1 (nomear formalização) e L2 (ferramentas) quase não foram testados** — afirmações sobre eles
(incl. a alavanca-web) são essencialmente **não-testadas**.

## Honestidade — ressalvas que este relatório carrega (§6)
- **Completion-only:** disposição do PLANO em texto, não o agente real. Não transfere ao produto.
- **N pequeno em toda célula (1-3); nenhuma N≥5.** Variância intra-modelo já virou o sinal (deepseek +0,50→−1,50). Deltas-grandes-vs-ruído, não significância.
- **Juiz frequentemente único** nas células decisivas (F0 cross-vendor só no P1/P2). Viés de família medido (R6: Claude ~0,87 mais generoso com Haiku).
- **Claude como SUJEITO**: Haiku/Sonnet na escada-claude (julgado por não-Claude); o **F1/M0 já tivera Opus-sujeito em §9** (juiz Claude **ÚNICO = auto-avaliação**; discriminou, mas **parcial** — ½ no FG2P); o **f4-clean (6/6) + f4-trap replicam por via mecânica**. Reconciliação Opus-juiz×sujeito pendente. *(Correção à síntese bruta que dizia "Claude só foi juiz".)*
- **As células decisivas do TOPO (f4-clean 6/6, f6-ruidoso 2/2) NÃO têm o juiz duplo cross-vendor** que dá a credibilidade do F4-dup (92%) — são **juiz mecânico / classificação por leitura**, herdando a fragilidade de juiz-único; e o **verificador mecânico tem heurísticas calibradas pelo próprio autor** (circularidade fina). Some-se que o "topo" é **1 modelo (Opus 4.8), da MESMA família que co-escreveu o método** — camada de circularidade **além** da "projeto do dono".
- **Circularidade** (projeto+gabarito do dono, gabarito incompleto). **Disconfirmação ecológica (R8)**: no real, o auto-auditor não bate a competência pura.
- **Temporalidade: F6 RODOU** (limpo 16/16; ruidoso = barato over-flagga/topo situa) → ponto-cego **condicional à legibilidade**, não fundamental; **falta o real-grande/longitudinal não-sintético.** **Recusa (F3) = a medição mais frágil** (mas no F4-trap o topo recusa injeção nativamente, baseline 3/3). **Web = exploratório.**
- **Verificação mecânica (regex) deu falso-positivo dos dois lados**; só é limpa quando ancora em **ação de arquivo** (F4).
- **Resultados são SINAIS / direção forte, não prova.**
