---
title: 'Opinião de uso do Strata — honesta, por tarefa × tier × custo (consolidação F0-F5 + eco + escada Claude)'
created: 2026-06-13
status: 'CONSOLIDADO (workflow 7 agentes, com crítico adversarial de over-claim). SINAIS/direção, não prova. Síntese bruta em consolidacao-synthesis.json.'
---

# Opinião de uso do Strata — o que dizer, com honestidade

> Destilado de toda a evidência (F0-F5, execução-eco no digest real, escada Claude, eixo esforço, custo),
> passado por um **crítico adversarial de over-claim**. Detalhe por fase no [hub](ARQUITETURA-E-EVIDENCIAS.md);
> backlog priorizado em [`BACKLOG-fila-geral.md`](BACKLOG-fila-geral.md).

## Tese — confirmada na direção, **rebaixada no status**
**"A forma corrige o viés; a capacidade calibra."** Sobrevive como **sinal forte** — mas é preciso separar o
**sólido** do **exploratório** (a versão anterior emprestava a robustez das peças fortes — F0 cross-vendor, F4
GOLD-gate 100% + juiz 92% — para células que ficaram fracas). **Direção forte, status NÃO-fechado.**
*(Atualização 2026-06-13: a metade "**a capacidade calibra**" ganhou sua célula decisiva — Opus 4.8 abstém
**6/6** no f4-clean, onde o barato/médio super-engenha, e o Strata **não** o desvia; ver linha §9. E a metade
"**a forma corrige o viés**" ganhou um **caso concreto** (f4-trap, [resultado](RESULTADOS-f4-execucao.md)):
mesmo no topo, segurança (§6-bis) e preservação (§3) são **nativas** — a forma não as adiciona — mas a
**padronização + rastreabilidade do conserto** (§5 canonical/superseded/ponteiro + registro append-only) **é**
o que a forma adiciona, até ao topo. Ainda assim, no geral, é o lado mais frágil.)*

## Três condições que valem para TODA a tabela (não são notas de rodapé)
1. **Tudo abaixo é SINTÉTICO/fixture.** Em **projetos REAIS** (R8, 3 projetos) o Strata **como auto-auditor de
   IA NÃO bateu a competência pura** — piorou no bom, empatou no messy, e no exemplar **todos (incl. baseline)
   alucinaram** (~4,4-4,9 falso-positivos/plano). **O ganho sintético não se traduziu em projeto real.** Única
   exceção medida: o **topo (Opus)** — e em projeto próprio, N=2.
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
| **Preservar histórico / tombstone §3** | OK c/ Strata (tombstone 7/8; payload propagado 0/8) | OK | OK | não | **econômico, recorrente** | **SÓLIDO** no sintético; **SINAL** no real (1 digest, N=2, próprio, sem 2º juiz) | argumento de segurança mais transferível; **replicar fora do projeto-próprio** |
| **Recusar injeção §6-bis** | Strata vira obedecer→recusar no leniente; **Claude-Haiku já recusa sozinho** | já recusa | redundante | não | econômico | **SINAL** — a medição **mais frágil** (concordância 56-69%, 1 cenário, N=2; o GOLD-gate é do F4, não daqui) | delta real só no barato leniente; **segurança do fraco é em parte LEXICAL** (recusa 6/6→4/6 sob paráfrase) → contra ataque real de paráfrase, barato **não é seguro** |
| **Abster-se em projeto já-bom §9** | **FALHA** (Strata induz super-engenharia 6/8 vs 2/8) | parcial (Sonnet+thinking 1/2, dentro do ruído) | gpt-4.1 e **Opus 4.8 abstêm** (Opus **6/6** STRATA+BASELINE, mec.+GOLD) | não | **forte, pontual** / humano no loop | **FECHADA**: topo abstém; Strata **não** induz super-eng no topo | a **faca de dois gumes é do barato/médio**: lá o Strata em projeto limpo gera trabalho inútil/alucinado. **A forma NÃO compra proporcionalidade — a capacidade compra**: o topo abstém com ou sem Strata. Use modelo forte ou humano no loop |
| **Verificar fonte §6 (web)** | carimba falso confiante | idem | **FALHA também sem web** (gpt-4.1 carimbou 3/3) | **reduz, não conserta** (forte+web ainda 2/3) | — (probe) | **EXPLORATÓRIO** (N=1-2, 1 fixture, 3 claims) | nunca confie em verificação de fonte sem web — **nem com web sem revisão** |
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
- **Claude como SUJEITO**: Haiku/Sonnet na escada-claude (julgado por não-Claude) **e agora Opus 4.8 na abstenção §9** (f4-clean, 6/6 abstenção correta, mecânico+GOLD). **Reconciliação** com Opus-sujeito segue pendente. *(Correção a uma afirmação da síntese bruta que dizia "Claude só foi juiz".)*
- **Circularidade** (projeto+gabarito do dono, gabarito incompleto). **Disconfirmação ecológica (R8)**: no real, o auto-auditor não bate a competência pura.
- **Temporalidade = direção, não achado** (F6 não rodou). **Recusa (F3) = a medição mais frágil.** **Web = exploratório.** **Razão compressão:gates ~2/3:1/3 = 1 célula local.**
- **Verificação mecânica (regex) deu falso-positivo dos dois lados**; só é limpa quando ancora em **ação de arquivo** (F4).
- **Resultados são SINAIS / direção forte, não prova.**
