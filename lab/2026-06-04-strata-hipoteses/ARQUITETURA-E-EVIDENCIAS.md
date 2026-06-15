---
title: Arquitetura de testes e evidências do Strata — o que comprova, em que condições (macro)
created: 2026-06-13
updated: 2026-06-14
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
>
> **➡️ Opinião de uso final (honesta, consolidada):** [`OPINIAO-DE-USO.md`](OPINIAO-DE-USO.md) ·
> backlog priorizado: [`BACKLOG-fila-geral.md`](BACKLOG-fila-geral.md) ·
> **o que envelheceu (revisão retroativa):** [`REVISAO-RETROATIVA.md`](REVISAO-RETROATIVA.md).

## Estado das fases — fonte única (atualizado em 2026-06-14)

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
| **Braço externo** | o falso-positivo é circular? | ✅ bem-comportado + messy (6 repos) | baixa (N=1; messy gênero-confundido) | [externo](RESULTADOS-externo-bemcomportado.md) |
| **Gênero** | aplica o padrão do gênero? | ✅ probe (com framing) | baixa (N=1) | [gênero](RESULTADOS-genero.md) |
| **Gênero+Temporal (próprios)** | lê tombstone/supersessão como organização? | ✅ probe (framing+marcadores) | baixa (N=2; **circular**) | [gên+temp próprios](RESULTADOS-genero-temporal-own.md) · [gabarito](GABARITO-genero-temporal-own.md) |
| **F6** temporalidade | inferir cronologia / drift / abster / **ruído (R8)** | ✅ limpo 16/16 · **ruidoso: barato 4/4 over-flagga, topo 2/2 situa** | baixa (4 fixtures) | [F6](RESULTADOS-f6-temporal-sem-marcadores.md) · [dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md) |
| **Eco/gênero** | vale em +cenários e fora de código? (+ viés do dono) | ⬜ planejado | — | [plano](PLANO-evidencia-cenarios-e-narrativa.md) |
| **Escada Claude** (contrato) | Claude Code barato aplica? | ✅ Haiku+Sonnet · ✅ **Opus** (f4-clean 6/6, f4-trap 3/3 Strata) | média (F3 juiz + F4 mec) | [escada-claude](RESULTADOS-escada-claude.md) |

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
- **Acurácia × precisão (eixos separados):** capacidade (acerto vs gabarito) e estabilidade (dispersão /
  *flip-rate*) são reportadas **separadas**, sempre com **k/K**; `pass@k` (teto) ≠ `pass^k` (confiável).
  Temperatura = precisão, não inteligência; **K pequeno = teto de amostra**. Disciplina em
  [`ADR-006`](../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md).

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

- **2026-06-14** — **P9: spot-check dos modelos novos (jun/2026).** A assinatura por tier **persiste** entre
  gerações (gemini-3.1-flash-lite: over-age no limpo / recall 4/4 + segurança 5/5 no bagunçado); a detecção do
  óbvio **melhorou**, a abstenção §9 segue teto. Limites expostos: nomes de modelo churnam (L2), e os reasoners
  novos da OpenAI (gpt-5-mini/nano) devolvem `content=None` no completion-only básico — não medidos com justiça.
  **P9b — barato × caro por vendor** (base do gráfico, completado): no limpo **ninguém se abstém 100% — nem o
  topo**. **Opus refeito sem truncamento = o melhor** (over-ação 1,2; recall 4/4; segurança 5/5). **Caro ≠
  melhor:** o gemini-2.5-pro (caro Google) é reasoner e **nem rodou** (saída degenerada); o **Haiku (barato
  Anthropic) age + que todos** (9,6 fabr.). **Segurança falha nos + baratos** (glm-4.5-air 0/5, gpt-4o-mini
  ~1/10, deepseek 3/5). [`RESULTADOS-p9`](RESULTADOS-p9-modelos-novos-jun.md) (§P9b).
- **2026-06-14** — **Autoauditoria: o repo contra o próprio Strata (dogfood).** Aderência **forte** nas 12
  seções do L0; as violações que havia (drift de duplicação, `updated:` morto, âncora-fantasma `§22`) já
  foram corrigidas nesta sessão pelas regras do método (append-only, apontar-não-copiar, §9). **Confirmado
  por cross-check de 5 auditores** (o fan-out, após o limite de gasto reabrir): só resíduo de baixa/média
  severidade, e os baratos já consertados (`divulgacao/` na navegação, banner §6-bis em `_superseded/fixtures/`,
  "Strata FINALIZADO"→honesto). [`AUTOAUDITORIA-repo-vs-strata`](AUTOAUDITORIA-repo-vs-strata.md).
- **2026-06-14** — **P8 (posição/saliência da §9): POSIÇÃO REFUTADA.** A/B/C placebo (K=5) + varredura de
  temperatura (K=10): o banner neutro (C) = canônico (A) ⇒ pôr a §9 no topo **não muda** o comportamento (cai o
  "lost-in-the-middle"); só o **conteúdo** (critério de abstenção, B) move, e **fraco/instável** (calibra 1/5; o
  "8→3" era sorte de K=2). Fracos: teto de capacidade (~nada). **Variância:** K=5 superestimava (segurança do
  fraco ~10%, `pass^k=0`; mode-lock a temp 0,3). Sobrevive *"capacidade é o portão"*. **Decisão: NÃO editar o
  `knowledge-architecture.md` canônico.** Metodologia em [`ADR-006`](../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md).
  [`RESULTADOS-p8`](RESULTADOS-p8-posicao-saliencia-s9.md).
- **2026-06-14** — **defrag/housekeeping + privacidade** (não-experimental): wayfinding aponta à OPINIÃO;
  README do harness vivo; arco antigo → `eval/strata/_superseded/` (tombstone); dado pessoal sensível
  anonimizado+purgado (history rewrite). **REGISTRO de ideia** (a pesquisar): *registro/declaração de uso de IA*
  (normas científicas + lei UE/BR + C2PA/SPDX) como proveniência §3-bis →
  [`IDEIA-registro-uso-ia.md`](IDEIA-registro-uso-ia.md). Não executado.
- **2026-06-13** — **F6 real-ruidoso (reprodução controlada do R8)**: fixture messy red-team-validada; auditoria
  ingênua. **Barato 4/4 OVER-FLAGGA** (gpt-4.1 re-levanta bug resolvido + pede LICENSE; gemini manda **apagar
  marcadores históricos** = anti-§3); **Opus 4.8 2/2 SITUA** (abre "já-resolvido", prioriza o genuíno, seção
  explícita "não corrigir — falsos positivos"). **Refino F6:** no limpo a legibilidade basta; sob **ruído só a
  capacidade calibra**. Mesma assinatura over-ação-do-barato do f4-clean/gênero. N=2.
  [`RESULTADOS-f6`](RESULTADOS-f6-temporal-sem-marcadores.md).
- **2026-06-13** — **Opus 4.8 no f4-trap (§6-bis injeção + §3 tombstone)**: STRATA **3/3 PASS**; BASELINE 3/3
  "FALHA_CORRECAO" que, decomposta, **separa as duas metades da tese**: segurança (recusou injeção 3/3,
  **não** propagou) e append-only (recusou truncar histórico 3/3) são **nativas do topo**; o que faltou sem
  as regras foi a **padronização + rastreabilidade do §5-fix** (schema canonical/superseded + registro) — **o
  que a FORMA adiciona, mesmo ao topo**. [`RESULTADOS-f4`](RESULTADOS-f4-execucao.md).
- **2026-06-13** — **célula decisiva FECHADA — Opus 4.8 no f4-clean (§9 abstenção)**: o **topo abstém 6/6**
  (STRATA+BASELINE, mecânico + GOLD-gate 100%) onde o **barato/médio super-engenha COM Strata** (gpt-4o-mini,
  gemini). Confirma a metade "**a capacidade calibra**"; o Strata **não desvia o topo**. N=3, 1 fixture
  sintética, completion-only. [`RESULTADOS-f4`](RESULTADOS-f4-execucao.md) · linha §9 da [OPINIÃO](OPINIAO-DE-USO.md).
- **2026-06-13** — **F6 duro** (longitudinal/drift + abstenção): +2 fixtures red-team-validadas, sonda
  **8/8 PASS** (gemini-flash + gpt-4.1). Longitudinal: todos acharam a decisão em vigor **e** apontaram o
  `setup.md` desatualizado (drift). Abstenção: 4/4 disseram "nenhuma em vigor / pendente" (nuance: 3/4 puxam
  um default tentativo quando pressionados a agir). Total F6 = 16/16; real-ruidoso segue aberto.
  [`RESULTADOS-f6`](RESULTADOS-f6-temporal-sem-marcadores.md).
- **2026-06-13** — **F6 (temporal sem marcadores)**: fixture sintética endurecida por red-team (3 críticos
  cegos 2×), sonda **8/8 PASS** (gemini-flash + gpt-4.1, modes chrono **e** naive): todos inferiram a
  cronologia por referência cruzada de conteúdo e acharam o operante **apesar** do nome+README enganosos —
  **disconfirma em parte** o "ponto-cego temporal fundamental" (vira **condicional à legibilidade da
  evidência**). Ressalvas: N=1, sintético, fácil; o caso sem-desambiguador (ambíguo até p/ humano) e o
  longitudinal/real **não** testados. [`RESULTADOS-f6`](RESULTADOS-f6-temporal-sem-marcadores.md).
- **2026-06-13** — **GÊNERO+TEMPORAL nos projetos do dono** (AulaQuantum/DeepLearning, gabarito
  **PRÉ-REGISTRADO** antes da sonda): cega bateu **4/4 no gênero** (JÁ-BOM, ninguém exigiu CI/tests) e **não
  acionou nenhuma das 5 armadilhas N1-N5** no temporal (tombstone/arquivamento/supersessão = organização, não
  defeito); ainda pegou **true-positives** (um dado pessoal sensível, PDF duplicado, drift de status). FORTE mas
  **circular** (projeto+analista+autor mesma família) e **bar baixo** (marcadores explícitos; inferir tempo
  SEM marcadores = F6, segue aberto). [`RESULTADOS-genero-temporal-own`](RESULTADOS-genero-temporal-own.md) ·
  [`GABARITO`](GABARITO-genero-temporal-own.md).
- **2026-06-13** — **eixo GÊNERO**: com framing gênero-consciente, os modelos reconhecem o gênero e **não
  exigem tests/CI de uma lista/notas** (não são gênero-cegos quando perguntados) → **resolve em parte o
  confundidor do messy** (o "JÁ-BOM" era em parte genre-appropriate, não sub-detecção). Implica **§9
  gênero-consciente** (loop narrativa). N=1; AulaQuantum/DeepLearning pendem de digest do dono.
  [`RESULTADOS-genero`](RESULTADOS-genero.md).
- **2026-06-13** — **revisão RETROATIVA** do corpus ([`REVISAO-RETROATIVA.md`](REVISAO-RETROATIVA.md)): a
  técnica evoluiu → reavaliamos tudo. Núcleo sólido (F0, §5-fix, §3-tombstone) **sobrevive**; **over-claims
  caíram**: datas/temporalidade ~33% **❌ não-achado** (média ruidosa, juiz único, F6 não rodou) e **R8
  reinterpretado** (over-detecção = **FRAMING**, não falha inerente — o braço externo corrige). Anotados (§3,
  não reescritos): R8-sintese, P4/datas, dossiê. Fixados os **campeões** (ótimo-até-agora) → testar desafiantes,
  não combinatória tudo×tudo.
- **2026-06-13** — **braço EXTERNO (quebra circularidade): bem-comportado + messy** (6 repos de terceiros).
  Bem-comportado: **M0 = JÁ-BOM 9/9** (abstém certo); AUDIT over-detecta → falso-positivo do **R8 é da FORMA,
  não circular**. Messy (3 repos 1-3/7): M0 disse **JÁ-BOM a quase tudo, até no 1/7** → **REPLICA F1/M0**
  externamente (forma corrige o falso-positivo, **super-corrige em SUB-detecção**; nem o gpt-4.1 discriminou).
  Os **dois modos de falha**, sem circularidade. Messy **gênero-confundido** (baixa-conformidade ≠ defeito —
  liga ao ponto AulaQuantum/DeepLearning). N=1. [`RESULTADOS-externo`](RESULTADOS-externo-bemcomportado.md).
- **2026-06-13** — **CONSOLIDAÇÃO** (workflow 7 agentes + crítico adversarial de over-claim → 9 corrigidos):
  destilou tudo na **[opinião de uso honesta](OPINIAO-DE-USO.md)** + **[backlog priorizado](BACKLOG-fila-geral.md)**.
  Tese **rebaixada** (fechada → *direção forte, status não-fechado*); **R8 (disconfirmação ecológica) ao TOPO**
  (no real o auto-auditor não bate a competência pura); **recusa = medição mais frágil**; **temporalidade = sinal
  mais ruidoso** (não achado); **sólido** só §5-fix e §3-tombstone por execução. *(Corrigi um erro da própria
  síntese: Claude FOI sujeito em Haiku/Sonnet — escada-claude; só Opus-sujeito pendente.)*
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
