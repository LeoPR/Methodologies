---
title: Arquitetura de testes e evidências do Strata — o que comprova, em que condições (macro)
created: 2026-06-13
status: vivo. F0-F4 (nuvem) + F3 (local) fechados; F4 (local) em curso; F5/F6 fronteira.
---

# Como o Strata foi testado — e o que a evidência mostra

> Documento **macro**: a ideia abstrata por trás dos testes e o que eles mostram. Os números
> granulares e as ressalvas finas vivem nos `RESULTADOS-*` linkados. O **método** está em
> [`recipe/knowledge-architecture.md`](../../recipe/knowledge-architecture.md) — aqui é sobre a
> **validação** dele. Tudo abaixo é **sinal/indício**, não prova (ver *Regime e limites*).
>
> **Sem familiaridade com os termos?** (modos M0-M4, *fixture*, *completion-only*, *fail-closed*,
> *tombstone*, como ler *N* / *concordância*) — há um glossário em português claro no
> [`GLOSSARIO.md`](../../GLOSSARIO.md), seção *Termos de avaliação e teste*.

## Estado das fases — fonte única (atualizado em 2026-06-13)

> Esta tabela é a **fonte canônica** (§5) do estado das evidências. README e demais docs **apontam
> para cá** em vez de repetir números que envelhecem. **Mudou algo num lab? Atualize só aqui** e
> acrescente uma linha no *Histórico* no fim (append-only, §3/§8).

| Fase | Pergunta | Estado | Confiança | Detalhe |
|---|---|---|---|---|
| **Núcleo L0** | é fundamentado? | ✅ consolidado | alta (22 fontes) | [`GLOSSARIO`](../../GLOSSARIO.md) · método |
| **F0** juízes | as conclusões são robustas? | ✅ fechado | alta (3 empresas convergem) | [F0](RESULTADOS-f0-confronto-juizes.md) |
| **F1/M0** abstenção | sabe *não agir*? | ✅ fechado | média (N pequeno) | [F1/M0](RESULTADOS-f1-m0-abstencao.md) |
| **P7** camadas | entende L0/L1/L2? | ✅ parcial | média | [P7](RESULTADOS-p7-camadas-entender-aplicar.md) |
| **F3** recusa | recusa injeção? | ✅ nuvem + local | média-alta (juízes) | [F3](RESULTADOS-f3-recusa.md) |
| **F4** execução | conserta sem destruir? | ✅ nuvem + local + eco (real) | média (N=2) | [F4](RESULTADOS-f4-execucao.md) |
| **F5** pesquisa (§6/web) | web ajuda a verificar a fonte? | ✅ probe (exploratório) | baixa (N=1-2) | [F5](RESULTADOS-f5-pesquisa.md) |
| **F6** temporalidade | reauditar corpus que mudou | ⬜ aberto | — | [dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md) |
| **Eco/gênero** | vale em +cenários e fora de código? (+ viés do dono) | ⬜ planejado | — | [plano](PLANO-evidencia-cenarios-e-narrativa.md) |
| **Escada Claude** (contrato) | Claude Code barato aplica? | ✅ Haiku+Sonnet · ⬜ Opus | média (F3 juiz + F4 mec) | [escada-claude](RESULTADOS-escada-claude.md) |

## Duas perguntas
1. O **núcleo (L0)** é fundamentado? — questão de *fundamentação*.
2. Uma **IA consegue aplicar** o Strata, e o método **ajuda**? — questão *empírica*.

## Camada 1 — o núcleo é fundamentado (não é experimento)
O L0 (12 princípios) foi consolidado contra **22 fontes primárias** + varredura de atemporalidade,
e a estratificação por **durabilidade** tem precedente canônico (*pace layering*, Brand 1999;
*shearing layers*; Gartner 2012). Etimologia e fontes no [`GLOSSARIO.md`](../../GLOSSARIO.md). Isto é
**estabelecido**, não medição. O L0/L1 **independe de tecnologia** — um humano com tempo aplica tudo,
com ou sem IA.

## Camada 2 — a IA aplica? A escada de modos (M0-M4)
O que se **testa** não é "o Strata funciona" (o L0/L1 já se sustenta), mas o que é **automático por
IA** (a camada L2). Decompusemos o "engajamento" da IA numa escada — cada degrau é uma tarefa diferente:

| Modo | Pergunta que isola | Estado | Detalhe |
|---|---|---|---|
| **M0** — abstenção/§9 | "devo agir aqui? quanto? (não-agir é resposta válida)" | fechado | [RESULTADOS-f1-m0](RESULTADOS-f1-m0-abstencao.md) |
| **M1/M2** — compreensão | "entende o método e o projeto?" | parcial | [P7](RESULTADOS-p7-camadas-entender-aplicar.md) |
| **M3** — diagnóstico | "o que está errado / o que faria?" | exaustivo (L0) | série R/P |
| **M3.5** — recusa (F3) | "recusa obedecer uma ordem maliciosa lida do projeto?" | fechado (nuvem+local) | [RESULTADOS-f3](RESULTADOS-f3-recusa.md) |
| **M4** — execução (F4) | "produz o fix sem destruir rastreabilidade?" | nuvem fechado; local em curso | [RESULTADOS-f4](RESULTADOS-f4-execucao.md) |

## Como medimos — a disciplina (por que dá pra confiar nos sinais)
- **Cego:** planos anonimizados; pontua-se sem saber o modelo (evita viés de marca).
- **Juízes cross-vendor:** ≥2 de **empresas diferentes** (Google + OpenAI), **não-Claude**. Empresas
  distintas ⇒ vieses independentes; **convergência = robustez** (não é artefato de um avaliador). O F0
  estabeleceu isso; o F4 teve **92%** de concordância inter-juiz.
- **Mecânico onde dá > juiz:** preferimos teste **objetivo** (regex de sinais com *gold-gate*, parse de
  config, **sobrevivência-de-conteúdo**, `git`, asserções) ao julgamento. O juiz só refina o **resíduo**
  que a mecânica não fecha. Todo verificador tem um **GOLD self-test** (casos-disfarce) como portão.
- **Confundidores controlados** (os erros que já nos morderam): falso-zero por **truncamento/thinking**;
  **"seguro e inútil"** (silêncio ≠ recusa); **paranoia** (controles limpos + ação legítima atestada);
  **efeito-método** isolado por **braço baseline**; **fixtures com hash congelado** (anti-drift).
- **§6 (honestidade):** onde o regex confunde *citar* com *propagar*, dizemos e mandamos ao juiz; onde o
  N é pequeno, dizemos. Resultados são reportados como **direção**, não cravo.

## Regime e limites (ler antes de citar números)
- **Completion-only:** o modelo **produz/recusa em TEXTO**; não roda ferramentas. Mede-se a *disposição
  do plano/fix* — **não** o agente real agindo. Um modelo pode escrever fail-closed e, com ferramentas,
  agir diferente (ou vice-versa).
- **N pequeno** por célula (2-3 runs); **1-2 cenários-mãe** (sintéticos + 1 digest real); ladder de
  modelos enxuto (nuvem barata→forte + locais, estes **ruidosos** — pequenos não emitem o formato).
- ⇒ As conclusões valem como **direção forte**, não prova; **generalizar pede mais cenários**.

## Custo — duplo propósito (nosso gasto = referência do custo do dev)
O custo dos experimentos tem **dois usos que viram um**: (1) o que **nós** gastamos testando; (2) o que um
**dev gastaria** usando o Strata — proporcionalmente. Logo o custo é **resultado**, não só orçamento.
- **Vocabulário relativo (para o relatório):** **econômico** · **intermediário** · **premium**. *Registros*
  de experimento podem ter **valores absolutos** (referência); o **relatório final** usa o **relativo** —
  um modelo mais capaz costuma custar mais, então basta o relativo. *(Assume capacidade≈custo: correlato, não idêntico.)*
- **Referência de custo do dev (lendo o [mapa de bordas](PLANO-evidencia-cenarios-e-narrativa.md)):**
  - **Recusa + conserta §5** fecham no **econômico** → uso **recorrente barato** é viável (rode sempre).
  - **Abster-se (§9) / organize completo** pede **premium** → mas como **organize de uma vez** é **custo
    único/esporádico** (pague premium 1×, mantenha o dia-a-dia no econômico).
- **Âncora proporcional (record):** a validação **inteira** (F0-F4 + eco + escada Claude, dezenas de runs)
  custou ~**US$15** de crédito; um dev aplicando a **um projeto** gastaria **centavos a poucos dólares**.

## O que a evidência mostra (macro)
- **F0 — a fundação (juízes):** juízes de empresas diferentes **convergem** ⇒ as conclusões não são
  artefato. "Maior" **não** é automaticamente "melhor juiz" (um *flash* barato rivaliza com modelos de
  topo); os **OpenAI-pequenos são lenientes** (maus juízes).
- **F1/M0 — abstenção:** a **forma** (framing) corrige o falso-positivo na raiz; a **capacidade** calibra
  (só o topo discrimina "já-bom" de "precisa-de-ponto").
- **F3 — recusa:** com o Strata, modelos recusam de forma **principiada e espontânea** uma injeção lida
  do projeto; o **barato vira de obedecer → recusar**; **0 falso-alarme de ameaça** (não inventou injeção
  onde não havia); a "segurança" do modelo fraco é **em parte lexical** (cai sob paráfrase).
- **F4 — execução:** o Strata **habilita** o conserto correto (fonte única, §5) e **preserva** o histórico
  (*tombstone*, §3) + **fail-closed na execução**; **mas induz super-engenharia** no modelo fraco (ele
  *alucina* defeitos para agir) — **só o topo se abstém** no projeto já-bom.

## A tese (o fio que atravessa tudo)
> **A forma corrige o viés; a capacidade calibra.** O Strata leva a IA a fazer a coisa certa — recusar o
> malicioso, consertar o defeito, preservar o histórico — e o ganho **se concentra no degrau fraco** nas
> tarefas positivas. Mas o **julgamento de proporcionalidade** (§9 — *quando NÃO agir*) depende da
> **capacidade** do modelo, não da forma. Conclusão prática: **método + modelo de topo** (de uma vez),
> ou **método + humano no loop / orientação em etapas** para os demais.

## Fronteira (aberto, honesto)
- **F5** (com/sem ferramentas inverte o ranking de capacidade?) · **F6** (temporalidade/longitudinal —
  ver [dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md)).
- **Mais cenários e novos gêneros** (PatchCraft = repetir; **AulaQuantum/DeepLearning** = acompanhamentos
  de aula, não-projetos) + o **confundidor do "projeto próprio"** (conformidade/circularidade) + o **loop
  narrativa↔resultado**: plano em [`PLANO-evidencia-cenarios-e-narrativa.md`](PLANO-evidencia-cenarios-e-narrativa.md).
- **2º cenário-mãe** e **validade de agente-com-ferramentas-reais** (sair do completion-only) seguem os
  dois maiores limites a atacar.
- **Questão de design (método, não teste):** exportar/traduzir para normas externas (o "L3"?) — provável
  **corolário** de §5/§3 (eixo **transversal**, não 4ª camada de durabilidade); ferramenta como spinoff.
  Registro: [`IDEIA-exportacao-traducao.md`](IDEIA-exportacao-traducao.md).
- **Setup operacional p/ agentes** (Claude Code/Copilot) e **organização de artefatos de ambiente**
  (caches/temp/venvs, `Z:\caches`) — registrados na fila geral (área cinzenta Strata×Comporta).
- **Fila geral / consolidação:** índice das pendências em [`BACKLOG-fila-geral.md`](BACKLOG-fila-geral.md);
  **próxima meta = defrag** (fundir as ideias num plano priorizado, **antes de mais testes**).
- Roadmap de modos: [`PLANO-geral-modos-fechar-lacunas.md`](PLANO-geral-modos-fechar-lacunas.md).

## Índice da evidência granular
Desenhos: [DESIGN-f3](DESIGN-f3-recusa.md) · [DESIGN-f4](DESIGN-f4-execucao.md) (+ `*-synthesis.json`).
Resultados: [F1/M0](RESULTADOS-f1-m0-abstencao.md) · [F0 juízes](RESULTADOS-f0-confronto-juizes.md) ·
[P7 camadas](RESULTADOS-p7-camadas-entender-aplicar.md) · [F3](RESULTADOS-f3-recusa.md) ·
[F4](RESULTADOS-f4-execucao.md). Hipóteses/índice: [`README.md`](README.md).

## Histórico de evidências (append-only — §3/§8: não reescrever, só acrescentar)

> Dogfooding do próprio Strata: cada mudança de estado vira uma **entrada datada** (rastreável), e
> nada antigo é apagado — o que foi superado fica registrado como tal. *(Datas aproximadas pelos
> `created` dos docs e pelo histórico de commits.)*

- **2026-06-13** — **F5 (pesquisa/§6) probe**: sem web, a verificação de fonte falha **até no forte**
  (gpt-4.1 carimbou **3/3** afirmações falsas como corretas — verificação **alucinada**, confirma o dossiê);
  **web (`:online`, sem MCP) reduz o carimbo** (gemini 1,5→0), sobretudo por **honestidade** (pega-com-citação
  ou abstém, não finge). [`RESULTADOS-f5`](RESULTADOS-f5-pesquisa.md). Exploratório (N=1-2, ~US$0,14).
- **2026-06-13** — **eixo ESFORÇO** probado (B): Sonnet **+thinking** na abstenção subiu **0/2 → 1/2** (ajuda
  parcial, borda *fuzzy*; harness ganhou *knob* de thinking p/ nuvem). Raciocínio das vertentes: **F5/pesquisa**
  testável pelo **web plugin da OpenRouter (sem MCP)**, mas precisa de **fixture L1-conhecimento** nova;
  **Copilot** = modelos via OpenRouter (já cobertos; topo redundante), **produto não-scriptável**; **MCP não
  destrava** LLMs aqui. ([`PLANO-evidencia`](PLANO-evidencia-cenarios-e-narrativa.md))
- **2026-06-13** — **custo** elevado a **resultado de duplo propósito** (nosso gasto = referência proporcional
  do custo do **dev**) + **vocabulário relativo** (econômico/intermediário/premium; *records* = absoluto,
  *relatório* = relativo). Referência: recusa/conserto = econômico **recorrente**; abster-se/organize = premium
  **único/esporádico**; validação inteira ~US$15 → projeto-de-dev ≈ centavos-a-poucos-dólares.
- **2026-06-13** — método de **busca de borda por cortes (bisseção)** + **mapa de bordas** (recusa e §5-fix
  **fechados no extremo barato**; **abstenção** já localizada cross-vendor — forte abstém (gpt-4.1), médios
  não → **Opus redundante p/ isso**; reconciliar-tudo parcial em todos = provável **limite de método** → loop
  narrativa). Único corte novo barato: **eixo esforço** (Sonnet+thinking abstém? — precisa de knob no harness).
  [`PLANO-evidencia`](PLANO-evidencia-cenarios-e-narrativa.md). **Sem novo gasto até decidir.**
- **2026-06-13** — **escada Claude (Haiku+Sonnet, sem thinking) como SUJEITO**: recusam injeção principiado
  (F3, juiz — **piso mais seguro** que o barato da OpenAI, que obedecia) e, com Strata, **consertam §5** (F4
  PASS até no Haiku); mas **super-aplicam no limpo** (abstenção = capacidade). Mecânico do F3 deu ~100%
  **falso-OBEY** → juiz. [`RESULTADOS-escada-claude`](RESULTADOS-escada-claude.md). **Opus pendente.**
- **2026-06-13** — framing de **agrupamento por CONTRATO** (testar a escada Claude/Copilot, não modelos
  aleatórios; achar se o **Haiku barato sem-thinking** já faz; "venda" do uso-único-caro p/ organizar) +
  **eixo web/pesquisa** (modelos que leem as referências do Strata) registrados no
  [`PLANO-evidencia`](PLANO-evidencia-cenarios-e-narrativa.md). **Lacuna apontada:** Claude só foi juiz, nunca sujeito.
- **2026-06-13** — registrada a **fila geral** ([`BACKLOG-fila-geral.md`](BACKLOG-fila-geral.md)) com 2 itens
  novos: **setup-de-agente** (Claude Code/Copilot = L2/satélite; fronteira Strata×Comporta) e **artefatos de
  ambiente/caches** (`Z:\caches` = classificar por canônico×regenerável×efêmero). **Meta pendente: defrag/consolidar.**
- **2026-06-13** — refinado o plano de evidência (sintético=validade **interna** vs real=**descoberta de
  borda**; amostragem **externa** por espectro de conformidade: PyPI-comportados / científico-bagunçado /
  caótico) e registrada a **IDEIA de exportação/tradução** (o "L3"? — provável eixo transversal, corolário
  §5/§3) em [`IDEIA-exportacao-traducao.md`](IDEIA-exportacao-traducao.md). **Não executado.**
- **2026-06-13** — **registrado** o plano de **expansão de evidência** (PatchCraft; AulaQuantum/DeepLearning
  = acompanhamentos de aula; o **confundidor do "projeto próprio"**; o **loop narrativa↔resultado**) em
  [`PLANO-evidencia-cenarios-e-narrativa.md`](PLANO-evidencia-cenarios-e-narrativa.md). **Não executado.**
- **2026-06-13** — **F4-eco** (digest real pdf2md) **fechado**: o **§3 replica no real** — baseline
  `gpt-4.1` **destruiu seções** (optional-dependencies/Empacotamento), Strata **preservou** (zero
  destruição); mas **ninguém reconcilia tudo** (máx 2/3 pares) e o formato "arquivo inteiro" **estica/
  trunca** em arquivos reais grandes. *(Manifest eco corrigido: tokens de versão = RI2, excluídos do
  mecânico por design.)*
- **2026-06-13** — **F4** fechado: nuvem (mecânico GOLD 100% + juiz cross-vendor 92%) + local (4-8B:
  **zero PASS**; gemma3 destruiu/obedeceu). **F4-eco** (digest real pdf2md) **iniciado**. Docs de entrega:
  README com tabelas+vocabulário, **este doc macro**, glossário de testes.
- **2026-06-13** — **F3** (recusa/§6-bis) fechado: nuvem (recusa principiada; gpt-4o-mini vira
  obedecer→recusar; 0 falso-alarme) + local (ruidoso, mesma direção).
- **2026-06-12** — **F3** desenhado (painel adversarial) + harness validado (GOLD: 0 falso-neg de OBEY).
- **2026-06-09** — **F0** (juízes cross-vendor robustos) e **F1/M0** (a forma corrige o viés; capacidade
  calibra) fechados.
- **2026-06-08** — **P6/P7** (fronteira de uso; entender ≠ barreira). *Nota: o "+0.50" do deepseek-r1:8b
  local foi depois **superado** — era artefato de truncagem; validado −1.50 (ver P6).*
- **2026-06-04** — núcleo **L0 consolidado** (22 fontes); dossiê de temporalidade registrado (a estudar).
