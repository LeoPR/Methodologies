---
name: status-methodologies-project
type: status
status: active
created: 2026-06-03
updated: 2026-06-07
---

# STATUS — 2026-06-07

## Foco atual

- **AUDITORIA (2026-06-07) REBAIXOU os vereditos do H-B/H-C** — ver
  `eval/strata/AUDITORIA-2026-06-07.md`. Auditoria adversarial multi-agente achou furos
  ALTA que invalidam os numeros: (1) **H-C contaminado** (a `strata-an` cita os fixtures
  verbatim; a prosa nao — o "ganho da AN" mede vazamento, nao compreensao); (2) **fixture
  neutralizado != gabarito** (projeto-alvo sem P1/P7; `velho/`+`tarefas.txt` nunca em disco;
  tudo irreproduzivel, sem hash); (3) **prompt vaza a taxonomia** P1..P7; (4) **online
  automatico NUNCA rodou** (enabled:false, sem keys; "nuvem" foi chat manual N=1 contra
  fixture antiga; sabor Anthropic quebrado); (5) **sem baseline/controle**. Sobrevivem so
  como DIRECAO: AN→§6-bis no local (com asterisco), "nuvem detecta o obvio", P6 ponto-cego
  universal. **Claim honesto unico:** "a forma AN ajuda modelos locais fracos no fail-open —
  sinal forte mas confundido (leakage+comprimento)". Resto = preliminar. recipe/README ja
  rebaixado p/ "em comprovacao, NAO comprovado". **Proximo:** fundacao R0+R1+R2 (congelar
  fixture + descontaminar H-C + scorer unico sem enum) JUNTOS, depois baseline (R3).
- **RETESTE LIMPO (R0+R1+R2+R3 local) FEITO** (2026-06-07,
  `lab/2026-06-04-strata-hipoteses/RESULTADOS-reteste-limpo.md`): fixture congelado
  (sha 22bf662f) + AN-v2 descontaminada (grep=0) + prompt sem enum + baseline +
  pontuacao CEGA + N=3. **O H-C SOBREVIVE a descontaminacao**: det medio baseline 2.25 /
  prosa 2.50 / **AN-v2 4.58**; o **§6-bis fail-open vai de 1/12 a 12/12** com a AN. A
  prosa quase nao ajuda o local (+0.25 vs baseline); o lift do metodo mora nos gates de
  julgamento/seguranca (P5 2→10, P6 0→6, P7 1→12) — os obvios (P1/P3) ate competencia
  generica acha.
- **R4 (prosa-curta) FEITO** — desconfunde comprimento×gate: det baseline 2.25 / prosa-longa
  2.50 / **prosa-curta 3.92** / AN 4.58. **A COMPRESSAO domina** (+1.42 so por encurtar; o
  fail-open vai de 3→11/12) e os **gates somam +0.66** (polimento: priorizacao + atribuicao
  + o ultimo ponto). Correcao honesta: o doc inicial superestimou os gates. Implicacao de
  produto: um Strata **destilado/curto** ja resgata a maior parte do tier local. **Pendente:**
  nuvem limpa (fixture congelado), R6 2o juiz, R5 N>=5.
- **NUVEM = OpenRouter** (decidido 2026-06-07). Investigacao: extensoes de editor
  (Gemini Code Assist, Copilot) **nao sao scriptaveis externamente**; so o Claude Code tem
  binario (`...\anthropic.claude-code-*\resources\native-binary\claude.exe`). Sem node, sem
  API keys, Copilot nao-instalado. Escolha: **OpenRouter** (1 key -> todos os sabores
  openai_compat; resolve o bug do sabor Anthropic). `hb_runner.py` ganhou `--provider
  openrouter` (mesmo prompt limpo/baseline/fixture do local -> paridade).
- **NUVEM LIMPA FEITA** (2026-06-07, `RESULTADOS-tier-nuvem-limpo.md`): 7 sabores via
  OpenRouter × prosa/AN/baseline × N=3, fixture congelado, cego. det/7: baseline 3.43 /
  prosa **4.24** / AN **5.67**. **2 conclusoes antigas CORRIGIDAS:** (a) "nuvem satura na
  prosa (7/7)" FALSO (limpo=4.24; era contaminacao+enum); (b) "AN so serve pro local"
  FALSO (AN ajuda a nuvem +1.43; resgata P6 sem-fonte 4→19, P5 12→19, P7 13→19).
  **Falsa-inteligencia CONFIRMADA:** gemini-2.5-flash (barato) 7/7 supera llama-3.3-70b
  (3.33 prosa); llama-3.1-8b zera na prosa local E nuvem (e' o modelo, nao o ambiente).
  RESULTADOS-tier-nuvem.md (antigo) marcado SUPERSEDIDO. recipe/README recalibrado p/
  "evidencia inicial reproduzivel".
- **R6 (2o juiz nao-Claude) FEITO** (2026-06-07, `RESULTADOS-r6-2o-juiz.md`): gpt-4.1-mini
  re-pontuou cego os 63 planos nuvem. **AN > prosa > baseline vale com os 2 juizes** (deltas
  ~iguais) -> conclusao ROBUSTA ao juiz. gpt e ~1 ponto mais leniente (MAE 1.14) -> reportar
  DELTAS, nao absolutos. Concordancia alta nos gates criticos (P1 .94, P7 .90, P5 .86),
  baixa nos moles (P2 .56). Vies: Claude foi ~0.87 mais generoso com o haiku que o juiz
  neutro (indicio LEVE de familia, n=9, nao muda a conclusao). Instrumentos: judge_openrouter.py,
  compare_judges.py. **Pendente:** R5 N>=5, R8 projetos reais, R7 sandbox.
- **R8 (projeto REAL pdf2md) FEITO — DISCONFIRMACAO importante** (2026-06-08,
  `RESULTADOS-r8-projeto-real.md`): num projeto real BEM-ORGANIZADO, o Strata como
  auto-auditor de IA PIOROU vs baseline. Baseline achou os 2 problemas reais (RI1 dupes
  -DESKTOP/fonte-unica; RI2 versao 0.1.0-dev vs 0.7.0) 100%, ZERO alucinacao, priorizou
  100%. Prosa/AN acharam menos, ALUCINARAM mais (prosa 0.75, AN 1.0/plano) e criticaram
  docs BONS (DIARIO/CHANGELOG). O metodo prima "cacar violacoes" -> falso-positivo em
  projeto decente (os modelos furam o §9!). Hipotese: ajuda em problemas DENSOS, atrapalha
  onde o projeto ja e bom. recipe/README recalibrado: usar como CHECKLIST humano, NAO
  auto-auditor. **Caveat:** 1 projeto real (bem-organizado); falta um MESSY (NNN/TCF); N=2.
- **R8 SINTESE 3 PROJETOS REAIS FEITA** (2026-06-08, `RESULTADOS-r8-sintese-3-projetos.md`):
  pdf2md (bom), NNN (exemplar), FG2P (messy). **Veredito ecologico:** o Strata como
  auto-auditor de IA **NAO bate a competencia pura** em projeto real — piorou no bom,
  empatou no messy, e no exemplar TODOS (ate baseline) alucinaram (~4.4-4.9 falso-pos/plano).
  Falha dominante = falso-positivo + criticar praticas boas, nos 3 projetos e 3 bracos. A
  hipotese "ajuda onde e denso" NAO se confirmou. Mecanismo: framing "ache problemas" induz
  fabricar (modelos furam o §9) + fraqueza temporal (H-D) marca historico como atual.
  **Reposiciona o produto:** Strata = metodo + CHECKLIST humano; auto-auditor de IA =
  pesquisa em aberto. recipe/README recalibrado. Achado mais importante do reteste.
- **H-D (Temporalidade) registrada** (`README.md` do lab): LLMs nao situam artefatos no
  tempo (atual vs superado); provavel causa-raiz de parte do falso-positivo do R8. A testar.
- **VIRADA ESTRATEGICA** (2026-06-08, `lab/2026-06-04-strata-hipoteses/ESTRATEGIA-orientar-ia.md`):
  a pergunta deixa de ser "o Strata funciona?" e passa a ser "**como ORIENTAR uma IA a
  aplica-lo bem?**". Novas hipoteses: **H-E** (aplicar em ETAPAS, nao de uma vez so) e
  **modo-de-uso** (assistente-no-editor com humano no loop funciona; auto-auditor autonomo
  falha). Alvos de visualizacao: capacidade por secao/camada (L0/L1/L2), suficiencia por
  modelo/modo, sintetico×real. Ciclo de brainstorm (4 lentes) rodando p/ propor planos novos.
- **P0 PROVA DE TETO (Opus 4.8) — POSITIVA** (2026-06-08, `RESULTADOS-p0-prova-teto-opus.md`):
  Opus 4.8 (fresco, OpenRouter) aplicou o Strata a projeto real EXCELENTEMENTE — achou
  problemas reais VERIFICADOS (incl. §5 no NNN que EU, o gabarito, perdi: 2070/2043/2145
  conflitantes; pyproject leona/nnn vs README LeoPR/nnn), reconheceu o bom, tombstone (nao
  N1), priorizou §9, recusou inventar. **O falso-positivo dos medios e' limite de CAPACIDADE,
  nao do modo.** Recalibra o R8: auto-auditor FUNCIONA com modelo de topo; medios precisam de
  orientacao (P1/P2/P5). recipe/README atualizado. (Meu gabarito do R8 estava INCOMPLETO — o
  Opus foi mais rigoroso.)
- **P4 (capacidade por secao) FEITO** (`VIZ-capacidade-por-secao.md`): §5/§3 = 100%, §4/§6/
  §6-bis = 90%, §2 = 62%, **§3/§8 datas = 33% (mais fraca -> confirma H-D)**. Suficiencia:
  gemini-2.5-flash 7/7, gpt-4.1-mini/haiku/deepseek >=6. So L0 testada; melhor caso sintetico.
- **P1+P2 (AN-v3: forma anti-FP + etapas) FEITO** (2026-06-08, `RESULTADOS-p1p2-anv3.md`):
  embutiu as 6 condutas do Opus como processo em etapas; rodada nos 4 medios (NNN+pdf2md,
  N=2), pontuada CEGA (juiz Claude + cross-check nao-Claude) contra gabarito CORRIGIDO.
  RESULTADO: a forma BAIXA falso-positivo (NNN 4.25->2.88; pdf2md 1.88->0.38) e SOBE
  reconhecer-o-bom (0.25->0.62); sinal-ruido melhora nos dois (pdf2md fica +0.50 positivo).
  POReM: troca super-critica por SILENCIO em alguns modelos (gemini/gpt-4.1-mini ficam mudos,
  perdem os reais); haiku IGNORA a forma; so deepseek melhora nos 2 eixos. **Orientar e'
  alavanca real, mas NAO instala a discernancia do Opus -> nao fecha o gap de capacidade.**
  Auto-auditor confiavel = topo (P0) ou humano-no-loop; AN-v3 p/ medios = menos ruido, esperar
  sub-deteccao. PROXIMO: P6 (scatterplot dos eixos de borda) — pedido do dono.
- **P6 (testes de borda + scatterplot) FEITO** (2026-06-08, `RESULTADOS-p6-shootout.md` +
  `RESULTADOS-p6-scatter.md` + `VIZ-p6-scatter.svg`). Fase A (shootout de formas): tutoria
  MONOTONICA — F0-bare (Strata cru 53KB) e o PIOR p/ modelo barato; F4-etapas (multi-turn) o
  unico net-positivo; F1-checklist (2KB) o melhor portatil. Fase B (grid 12 modelos $0.02-$7
  × forma F1 + overlay F4): SO o Opus (+1.75) e claramente positivo; custo NAO compra
  qualidade entre baratos (os mais baratos sao os piores); etapas F4 levantam os baratos
  (deepseek-v3 -2.25->+0.50 a $0.26/M). **Veredito: cheap+portatil+bom = ESCOLHA DOIS.**
  Pontos da fronteira: (1) Opus+F1 max qualidade; (2) gpt-4.1-mini/gemini-flash+F1 = piso
  portatil neutro (~$0.5); (3) deepseek-v3+F4-etapas = barato+positivo, menos portatil.
  Novos: strata-checklist.md, hb_staged.py, gen_scatter.py (SVG puro), price_probe.py.
  Gasto OpenRouter total ~\$7. (P6-A/B caveat: N pequeno; medias incluem NNN exemplar.)
- **P6 #2 (value/free/local) + ENTREGA FEITO** (2026-06-08, `RESULTADOS-p6-grid2-value-free-
  local.md` + `recipe/strata-com-ia.md`). Preencheu a fronteira de USO. [VALIDACAO N=3 DEPOIS:
  o "+0.50" do deepseek-r1:8b LOCAL era ARTEFATO DE TRUNCAGEM; validado = -1.50 (alucina ao
  concluir). NAO ha free-local confiavel; auditor que ajuda = pago.] pago-barato deepseek-v3+etapas $0.26 e
  glm-4.6 $0.56 = +0.50; Opus +1.75 padrao-ouro. Pagar caro acima do barato-bom NAO compra
  qualidade (gemini-pro/gpt-5 piores que glm-4.6). Gratis REMOTO :free nao entregou (429 +
  qualidade baixa). FIX METODOLOGICO (apontado pelo dono): runner descartava message.thinking
  do Ollama -> reasoners locais pareciam 'incapazes'; corrigido (think:true+fallback) ->
  deepseek-r1:8b virou a melhor opcao local. ENTREGA positiva-only: guia-tabela + fronteira
  (recipe/strata-com-ia.md, VIZ-entrega-fronteira.svg). Pesquisa (com negativos) separada em lab/.
- **REORG (2026-06-07): 3 territorios** — separado o LABORATORIO DE PROVA do resto.
  `recipe/` = metodologia (o fim) · `lab/` = IDEIAS (hipoteses + RESULTADOS-*.md +
  `strata-ai-native/`) · **`eval/`** = harness de prova (a "chave de fenda": meio, NAO
  fim). O `hb-kit/` virou `eval/strata/`; variantes AN e RESULTADOS foram para
  `lab/2026-06-04-strata-hipoteses/`. Paths dos scripts corrigidos + smoke-test OK.
  **Pendente** (proximo): doc profunda do `eval/` (ADR ferramenta≠metodologia) e tornar os
  fixtures **inertes/seguros** (o gabarito espera P1/P7, mas o fixture foi neutralizado).
- **Refinar a metodologia de organizacao+rastreamento por camadas de
  durabilidade** (L0 atemporal / L1 padroes consolidados / L2 adaptacao
  datada). Novo produto: `recipe/knowledge-architecture.md`.
- **Feito**: esqueleto L0/L1/L2; Parte I (L0) escrita; **fundamentacao do L0
  verificada** (22 fontes primarias web-verificadas em
  `lab/2026-06-03-fundamentacao-L0/`) e tecida de volta no L0 (linha
  "Fundamentacao" por secao). Auto-revisao = evidencia de que o metodo funciona.
- **Feito tambem**: Parte II (L1) escrita — catalogo `necessidade L0 ->
  formalizacao` com sinal-de-troca; 6 identidades de framework web-verificadas
  (Diataxis, ADR/MADR, FAIR4RS, Research Compendium, Lakatos, Zettelkasten).
- **Feito tambem**: Parte III (L2) escrita — ferramentas de hoje (IA/editor/
  git/filesystem/SaaS) mapeadas ao L0/L1, datadas e destacaveis. As 3 camadas
  do knowledge-architecture.md estao completas.
- **Feito (2026-06-03)**: revisao critica do L0 + **varredura future-proof** em
  2 rodadas multi-lente com verificacao adversarial (registrada em
  `lab/2026-06-03-future-proof-sweep/`). Veredito: L0 NAO era atemporalmente
  completo (ponto cego sistematico: assumia substrato perpetuo + leitor que ja
  decodifica + crescimento monotonico). Principio-mae: "autoridade-logica e'
  ortogonal a instancia/expressao/acesso/portador".
  - **Onda 1 APLICADA** ao knowledge-architecture.md: +§3-bis (tipo-de-ato
    dispositivo/probatorio + referencial), +§6-bis (autoridade-para-agir, eixo
    SEGURANCA), +§10 (durabilidade do portador/redundancia), gradiente
    append-only em §3 (traco/superficie/conhecimento-vivo + disposicao-tombstone
    + bitemporal). Numeracao `-bis` p/ NAO renumerar §4-§9.
  - **Onda 2 APLICADA** (refinos): principio-mae "autoridade-logica ⊥ instancia"
    em §5; auto-decifrabilidade (chave semantica redundante) em §3-bis;
    vazio-tipado / fronteira-de-cobertura em §6; proofreading-na-promocao em §7;
    proporcionalidade-a-distancia como regulador em §9. L0 agora = 12 secoes.
  - **Verificacao concluida** `[WEB ✓ 2026-06-03]`: todas as fundamentacoes
    novas das ondas 1-2 verificadas via web (Bjork&Bjork 1992, Brunner 1880,
    Schellenberg 1956, Snodgrass 1999, Hardy 1988, Kuny 1997, Reynolds&Wilson,
    LOCKSS, FRBR, Grice 1975, etc.).
  - **Eixo 5 (seguranca)** tocado pelo §6-bis: merece varredura propria depois.
  - Aplicados antes: revisao A+B+C (§5 generalizado, §7 DIKW->ANALOGIA, §3/§8 separados).
- **Gap conhecido**: o bloco OPERACIONAL do predecessor (fases de adocao,
  assessment brownfield, auditoria periodica) ainda NAO migrou. Decidir se vira
  "Parte IV — Adocao e operacao" antes de aposentar organization-methodology.md.
- Principio-guia: IA/VSCode/git sao FORMAS (L2) que expressam um nucleo que
  precede o computador; escrever o nucleo atemporal e' completo primeiro.

## Ultimo estado

- Monolito original (`README.methodology.md`, ~97KB) **modernizado** (camada
  IA-2026: MCP, Skills, memoria em camadas, context engineering, evals,
  proveniencia) — verificado na web (5 lentes de analise).
- **Explorado** como suite de 10 docs (experimento de estrutura).
- **Decisao**: o produto e' **1 arquivo** (`recipe/`); a suite de 10 docs
  virou **registro de pesquisa congelado** em `lab/.../experimento-split/`.
- Projeto **reorganizado** nas 3 cozinhas (recipe / lab / prototype) +
  wayfinding (README/AGENTS/MAP/STATUS) — dogfood da propria metodologia.

## Aderencia, brownfield, IA e portabilidade (2026-06-04)

- **Varredura multi-lente** (4 lentes + refutacao adversarial + sintese, 9
  agentes) registrada em `lab/2026-06-04-aderencia-portabilidade/`. Respostas:
  - **Segmentacao**: MANTER 1 arquivo (acoplamento L0->L2 medido = baixissimo;
    0 nomes de ferramenta no corpo dos principios). 1 arquivo e' trunfo de transporte.
  - **Aderencia**: 4 secoes universais (§1/§2/§5/§9), 7 condicionais com gatilho.
  - **Brownfield**: buraco real mas ADR-003 (adiar) nao errou no timing.
  - **IA**: majoritariamente raciocinavel; faltavam GATES de autoridade humana.
- **Aplicado ao produto** (v1.0.0 -> **v1.1.0**): carimbos de aderencia leves
  ("— §9", template de §10) em §4/§6/§7/§8; linha imperativa fail-closed em
  §6-bis; regra-dupla TRACO/SUPERFICIE em §3; split universal/condicional em §4;
  `canonical-source` no frontmatter.
- **Adiado** (decisao do dono): Parte IV brownfield espera dor empirica
  (prototype/ ainda N=0); caminho FORTE/LOCAL registrado no lab.
- **License**: **CC BY-SA 4.0** (copyleft) no frontmatter, com URL — a chave de
  licenca viaja com qualquer copia vendorada.
- **Licao de metodo**: o adversarial derrubou 2 achados "estruturais" por erro
  factual de evidencia — registrado como prova de que o ceticismo (§6) funciona.

## Batismo e auto-aplicacao (2026-06-03)

- Projeto batizado: **Strata**. Nome registrado em frontmatter do produto
  (`project: Strata`, `version: 1.0.0`) e no README.
- **3 ADRs criados** em `decisions/` (dogfood de §3/L1 — MADR):
  - ADR-001: formato 1 arquivo vs suíte
  - ADR-002: estrutura L0/L1/L2
  - ADR-003: aposentadoria predecessor (opção 0b)
- **Fronteira de cobertura** declarada em AGENTS.md (dogfood de §6 vazio-tipado):
  o que Strata NAO cobre (financas, RH, qualidade de codigo, conteudo de dominio).
- MAP.md atualizado com `decisions/`.

## Aposentadoria do predecessor (2026-06-03)

- `recipe/organization-methodology.md` **aposentado** → movido para
  `lab/2026-06-03-predecessor/` (FROZEN, registro histórico).
- Bloco operacional (adoção, brownfield, auditoria periódica) **não migrou**
  (decisão 0b: coberto implicitamente por L1/L2). Matéria-prima preservada em
  `lab/2026-06-03-predecessor/README.md` caso vire "Parte IV" futuramente.
- `recipe/knowledge-architecture.md` promovido de `draft` → **`active`**.
- Wayfinding re-apontado: `README.md`, `AGENTS.md`, `MAP.md` todos atualizados.

## Lacunas L1 fechadas (Passo 2, 2026-06-03)

- **§3-bis → L1**: ISAD(G) (dispositivo/probatório em escala institucional),
  SI/ISO 80000 (datum formal), PRONOM/DROID (auto-decifrabilidade de longo prazo).
- **§6-bis → L1**: PKI/X.509 (canal out-of-band), Zero-trust/NIST SP 800-207,
  RBAC/ABAC (autoridade delegada explícita).
- **§10 → L1**: OAIS/ISO 14721 (modelo de referência de preservação digital),
  Regra 3-2-1 (redundância mínima), BagIt/RFC 8493 (pacote verificável),
  Fixity checking (preservar é um verbo — verificação ativa).

## Economia de IA: tokens, hardware local e fornecedores (2026-06-04)

- Fase de lab sujo (2º ciclo): hipóteses confrontadas, nenhuma decisão tomada.
  Registrado em `lab/2026-06-04-economia-ia-tokens/`.
- **Copilot**: completions inline ilimitadas em todos os planos pagos (sem quota);
  modelos multiplier-0 (GPT-4.1, GPT-5 mini); Claude Sonnet = 1x (não grátis).
  Pro $10/mês cobre uso razoável de chat.
- **RTX 3060 12 GB**: Qwen2.5-Coder 7B Q4_K_M = sweet spot (4.8 GB VRAM,
  ~50 t/s, HumanEval 84.1%). 14B cabe apertado. Phi-4 Q5 não cabe na prática.
- **Ollama + VSCode**: integração oficial via Continue.dev (chat + autocomplete)
  e Copilot Chat (VSCode 1.113+, chat apenas). OllamaClaude MCP conecta Claude
  Code ao Ollama local (claim de 98.75% redução tokens — não verificado).
- **Compressão**: LLMLingua (20× com 1.5% perda, EMNLP 2023) e MCCom (47.9%
  redução latência, 46.3% redução cloud, arXiv 2026) validam local→cloud cascata.
- **Métricas**: Claude Code é o melhor instrumentado (JSONL + SDK + OTel).
  AgentsRoom e cc-statistics como trackers externos.
- **Framework de decisão**: local para autocomplete/arquivo único (GPU necessário);
  cloud para multi-arquivo/raciocínio complexo — validado por MCCom e Mellum.

## Economia de IA: mapa epistemico + plano experimental (2026-06-04, ciclo 2)

- **Mapa de recursos** (`lab/.../mapa-recursos-llm.md`, workflow 38 agentes):
  4 primitivas (memoria/processamento/E-S/custo) + 5 vetores; **NAO existe
  metrica de esforco escalar** (e vetor de 5 coords, coordenada vinculante muda
  com regime). Grade epistemica: **8 sempre-otimo** (caminho feliz — leis/garantias/
  contratos), **26 depende** (com gatilho), **8 nao-savel** (7 viram experimento).
  10 chutes sinalizados.
- **Descoberta de metodo**: quase nada e "sempre faca X"; o universal e "X e
  sempre VERDADE (lei/garantia/fato)" e a ACAO depende do regime. Mesmo formato
  do aderencia-condicional do Strata, em outro dominio.
- **Plano experimental** (`lab/.../plano-experimental.md`, workflow 26 agentes
  com verificacao adversarial): 6 estagios de ablacao, custo zero ate a Fase 2,
  cada um com gate objetivo. A verificacao LEU os JSONL reais e pegou: bug de
  dupla-contagem (7,33x por requestId), bloqueador de tool_use no shim Ollama,
  regime Max (quota nao USD), GPU contaminada (78% util idle).
- **Mentira de custo corrigida** (ambos os workflows): "Sonnet 4.6 gratis no
  Copilot" e FALSO — e 1x multiplier sobre 300 req/mes. So GPT-4.1/GPT-5 mini
  e autocomplete inline sao multiplier-0. Se vazar pra recipe, leitor gasta achando
  que e zero.
- **Status**: NADA executado. Plano aguarda aprovacao do dono para rodar Estagio 1.

## Ambiente Python + Estagio 1 EXECUTADOS (2026-06-04)

- **Ambiente Python** configurado via metodologia dev-environment Z:\
  (`New-ZPythonProject.ps1`): venv em `Z:\venvs\Methodologies`, junction `.venv`,
  pyproject canonico, `.gitignore` criado (lacuna do git que a metodologia nao
  cobria). Metodologia importada para estudo em `lab/2026-06-04-dev-environment-z/`.
- **Estagio 1 do plano experimental EXECUTADO** (custo zero), artefatos em
  `lab/2026-06-04-economia-ia-tokens/instrumento/`:
  - A1: `parse_usage.py` — dedup por message.id, 0 parse-fails, 6,87x inflacao evitada.
  - A3: baseline congelada SHA256 `b804afeb...` reproduzivel; cache_hit_rate 0,9454.
  - A2: cc-statistics concorda <1% no opus; ambos deduplicam (corroboracao independente).
  - Achado: cache_read domina (94,5% hit) — prompt caching ja quente.
- **GATE-1 substancialmente aberto** → Estagio 2 (inferencia local raw, custo zero)
  e o proximo, aguardando OK do dono.

## Estagio 2 EXECUTADO (2026-06-04) — GATE-2 aberto

- **B1 (decode 7B)**: qwen2.5-coder:7b @ 4k = **55,5 t/s**, @ 16k = 50,7 t/s,
  IQR <0,5% (estabilissimo), 100% GPU. Passa GATE-2 (>=40 t/s). Bate a literatura (~50).
- **B2 (VRAM x contexto)**: cresce linear (KV cache) 4,9/5,9/6,9 GB a 4k/16k/32k —
  footprint a 32k = 6,9 GB (confirma previsao adversarial, refuta "4,8 GB weights-only").
- **PENHASCO descoberto**: a 32k (7B) e no 14B inteiro a VRAM livre cai <2,7 GB e o
  decode despenca p/ ~13 t/s instavel (WDDM shared-memory fallback do Windows, nao
  offload de CPU). **Sweet spot: 7B @ <=16k.**
- **B4a (Ollama vs Foundry)**: conclusao "OS-gated" RETRATADA (era prematura — o
  dono cobrou com razao). O catalogo vazio da CLI era rate-limit/DNS (a extensao
  VSCode tem 112 modelos cacheados); WinML pulado != sem GPU (ha 40 variantes CUDA
  + 32 WebGPU/DirectML que rodam no Win10). EM VERIFICACAO: baixando
  qwen2.5-coder-0.5b-cuda-gpu p/ medir GPU real no nvidia-smi.
- Artefatos: `instrumento/bench_decode.py`, `STAGE2.md`. Custo zero.

## Estagio 3 EXECUTADO (2026-06-04) — GATE-3 destrava D1/E4 (com ressalva)

- **GATE tool_use (D0.5)**: o shim /v1/messages do Ollama emite tool_use
  ESTRUTURADO — DERRUBANDO a previsao adversarial de falha total. Dependente do
  MODELO: llama3.1:8b PASS, qwen3:14b PASS, qwen2.5-coder:7b FAIL (emite a chamada
  como texto/end_turn). Instrumento: `instrumento/test_toolcall.py`.
- **Tensao central**: o modelo rapido (qwen2.5-coder:7b, 55 t/s) NAO faz tool_use;
  o modelo agentico (llama3.1:8b) faz tool_use mas roda a ~21 t/s (2,6x mais lento).
- **llama3.1:8b @ 32k** (contexto agentico): ~19,5 t/s, 1,4 GB livres — viavel mas
  MARGINAL. Veredito: ramo Claude-Code-local e PROTOCOLO-VIAVEL, PERFORMANCE-MARGINAL.
- **Stack local recomendada**: autocomplete=qwen2.5-coder:7b; agentico-local-leve=
  llama3.1:8b; agentico-pesado=cloud (Claude Max). Ver `instrumento/STAGE3.md`.
- **Licao**: o adversarial acertou o sintoma (qwen-coder falha) mas generalizou a
  causa (shim quebrado). So a execucao real desambiguou. Mesmo padrao do B4a.

## Estagio 4 + novas hipoteses (2026-06-04)

- **Estagio 4 (integracao editor)**: C1 medido — autocomplete local (FIM) TTFT
  **68ms p50** (<500ms, passa GATE-4); sugestao streama. C2 (overhead editor) e C3
  (Copilot Chat+Ollama) preparados e ENTREGUES p/ uso real (precisam da extensao +
  dias de uso; ha perfis de VSCode em jogo). Config pronta:
  `instrumento/continue-config-sugerida.yaml`. VSCode 1.123 + Ollama 0.30 OK.
- **H17 — visao/imagens** (registrada, avaliacao adiada): custo de tokens-por-imagem
  dos providers vs visao local (dono ja tem llama3.2-vision:11b, qwen3-vl:8b) como
  pre-filtro "imagem->descricao local->texto cloud". Modalidade como 4a dimensao de
  roteamento. Ver `hipotese-visao.md`.
- **Licoes de metodo** registradas (`licoes-de-metodo.md`): L1 nao concluir de 1
  caminho; L2 sintoma != causa (varrer a variavel); L3 rodar o artefato e o arbitro;
  L4 custo-zero primeiro; L5 adversarial pode super-generalizar. Candidatas a
  realimentar o Strata (§4/§6).

## Arvore de decisao de ambiente + prototipo (2026-06-04)

- **Ciclo de arvore de decisao** (workflow wdoc3jreq, 22 agentes): 6 arquetipos de
  ambiente (A1 do-zero ... A6 qualidade-max) x 15 movimentos confrontados. Resultado:
  SO 3 movimentos sao T0 universais (M1 contexto enxuto, M2 info inicio/fim, M4
  right-size); o resto e T4 dependente-do-estado. Registrado em `arvore-decisao.md`
  com: camadas T0-T5, a arvore heuristica, cobertor-curto (Pareto por prioridade),
  6 conceitos novos, estrategia de simulacao.
- **Conceitos novos confirmados**: regimes de custo nao-fungiveis; T0-T5 como
  durabilidade-sob-refutacao (candidato a realimentar Strata); cobertor-curto como
  alocacao-de-Pareto; ambiente como artefato legivel-por-agente; fisico ⊥ policy como
  eixos de bloqueio; tool_use como propriedade-do-modelo.
- **Prototipo `prototipo/detect_env.py`** (funcional): detecta ambiente, classifica
  arquetipo, emite LIGAR/CONSIDERAR/BLOQUEADO + environment-profile.yaml legivel-por-
  agente. Modo `--simulate` teoriza outros ambientes. Validado em 3 casos. Achou e
  corrigiu 2 bugs proprios: admin!=pode_instalar (classificava todo nao-admin como
  corporativo); motivo de bloqueio agora DINAMICO (fisico vs policy). 2 limitacoes de
  deteccao documentadas (Copilot tier offline; pode_instalar heuristico).

## Publicacao + ajustes finos do Strata (2026-06-04)

- **Publicado** no GitHub (LeoPR/Methodologies): repo limpo com Strata na raiz;
  snapshot dev-environment excluido; LICENSE CC BY-SA 4.0 (texto SPDX).
- **README reescrito** apos critica de 4 metodos nomeados (Diataxis, convencoes de
  README, posicionamento/Dunford, arquitetura-de-informacao) — veredito unanime: o
  antigo posicionava o produto (Strata) como se fosse o continente (a oficina). Novo
  README lidera pela abordagem + diagrama mermaid + 2 produtos (Strata pronto /
  economia-IA no forno). Metafora padaria guiou a estrutura, NAO o vocabulario.
- **Licenca analisada** (CC BY-SA vs MIT): MIT e de software (categoria errada p/
  doc); o equivalente permissivo p/ documento e CC BY 4.0. BY-SA (copyleft) mantida
  como recomendada (derivados ficam abertos). Licenca cobre o TEXTO, nao a IDEIA.
- **README ajustado**: explicitado "le-se por humano E por IA"; corrigido overclaim
  de "finalizada" (eixo seguranca §6-bis e Parte IV adocao/operacao PENDENTES).
- **`recipe/README.md` novo**: guia de uso do Strata (humano + IA com prompts de
  exemplo; arquivo EFEMERO — le de qualquer lugar, descarta, mas vale manter p/
  revisao; pendencias de maturidade).
- **2 hipoteses registradas** (`lab/2026-06-04-strata-hipoteses/`): (H-A)
  codigo-como-documento (estende doc-vs-code + §3-bis); (H-B) aferir empiricamente
  se outras IAs entendem/aplicam o Strata — protocolo multi-modelo com avaliacao
  CEGA e rubrica (mitiga Claude-juiz-e-participante).

## Comporta batizado + dogfood (2026-06-05)

- **2a metodologia batizada: COMPORTA** (economia/roteamento de recursos de IA —
  "cada decisao e uma comporta: abre o recurso certo, fecha o caro"). Declarada no
  hub `lab/2026-06-04-economia-ia-tokens/` (`project: Comporta`); propagada em
  README/AGENTS/MAP. Quando destilar, vira `recipe/comporta-*.md`.
- **Dogfood (reaplicar Strata ao projeto)**: AGENTS.md (entrada ai-primary) estava
  com inventario desatualizado (faltava Comporta, aderencia, dev-env, hipoteses,
  decisions/) e `updated:` estagnado — CORRIGIDO. Datas de MAP/STATUS/AGENTS bumpadas.
- **H-C registrada** (`lab/2026-06-04-strata-hipoteses/`): versao AI-nativa/densa do
  Strata p/ proxima versao — depende de H-B; resolver tensao §5 (uma forma canonica,
  a outra gerada). Decidido NAO overclaim "Strata otimizado p/ IA" (so legivel; a
  otimizacao e' H-C futura).
- **Licenca**: confirmada CC BY-SA 4.0 (vs MIT: MIT e' de software, categoria errada;
  equivalente permissivo p/ doc seria CC BY 4.0).

## Comprovação forte do Strata (2026-06-06)

- **Plano executável de comprovação forte** criado em
  `lab/2026-06-06-comprovacao-forte-strata/` com:
  - `README.md`: gates G1..G6 para claim forte;
  - `matriz-testes-faltantes.md`: backlog priorizado (P0/P1/P2) dos testes que faltam;
  - `criterio-promocao-strata-v2.md`: regra de entrada para discutir v2.0 sem quebrar L0.
- Objetivo operacional: separar claramente rodada de **evidência** de rodada de
  **instrumento/infra**, fechar lacunas P6/P7 com N>=3 e preparar decisão v1.x vs v2.0.
- **Síntese de envelope** (`sintese-envelope-operacao.md`): consolida tier nuvem +
  local + A/B prosa-vs-AI-nativa num **envelope de operação** (ótimo = bigtech/prosa/F1
  "ler-e-pronto"; mínimo viável local = reasoner >=8B na forma AI-nativa; fora do
  envelope = local <3B). Inclui a **árvore/grafo de decisão** do Strata (automática /
  situacional / cobertor-curto) e os cenários ótimo-orientativo e ler-e-pronto. Marca
  4 lacunas [aberto] (N>=3 nuvem, braço prosa-curta, falso-positivo, validade ecológica)
  como pré-condição do claim "completo".
- **Fechamento forte local** (`fechamento-forte-local.md` + E5 na matriz): pacote
  endurecido para encerrar a trilha offline com critério objetivo (N>=5 por modelo,
  gate local P6/P7, N1/N2 zerados, alucinação <=0.10, estabilidade intercenário e
  falso-positivo zero no cenário limpo). "Versão local fechada" agora tem definição
  formal também em `criterio-promocao-strata-v2.md`.

## Proximo

- **H-B tier LOCAL + H-B' EXECUTADOS** (2026-06-05) — ver
  `lab/2026-06-04-strata-hipoteses/RESULTADOS-tier-local.md`. Achados:
  - **Tier local 7-8B**: entende a ESTRUTURA (L0/L1/L2 = 2/2) mas NAO os gates;
    detecta 0-2 de 7 problemas; os 5 de maior risco passam batido; deepseek-r1:8b
    ate endossou a fonte conflitante. Doc denso ~17k tokens nao sobrevive a locais fracos.
  - **H-B' (forma de invocacao) VALIDADA** (hipotese do dono): so o prompt muda e muda
    a deteccao. O agente fail-open (§6-bis, maior risco) SO foi pego no framing
    gate-first (F4); em F1/F2/F3 o mesmo modelo declarou o ambiente seguro. A captura
    do gate morava no PROMPT, nao no doc.
  - **Alvos do H-C** (gates a tornar imperativos): §6 sem-fonte (0/9!), §6-bis fail-open
    (1/9), §4 desonestidade, §5 fonte-unica, §3 traco/superficie.
  - Bug corrigido no caminho: num_ctx tinha que ser > prompt (~17k tok); Strata grande
    demais p/ locais = argumento empirico pro H-C (forma AI-nativa densa).
  - **PENDENTE: tier NUVEM** (dono roda GPT-4.1/Gemini/Sonnet/Claude novo) — o sinal forte.
    Runbook em `eval/strata/RUNBOOK-nuvem.md` (modo chat, F1+F4, salvar local/colar aqui).
- **H-C (forma AI-nativa) — A/B local PROMISSOR** (2026-06-05, `lab/2026-06-04-strata-hipoteses/RESULTADOS-hc-ab.md`):
  `strata-an-v0.md` (densa ~1.4k tok, gates imperativos + invocacao embutida) vs prosa,
  MESMO F1 neutro. Deteccao subiu em 4/4 modelos (deepseek 0->4; qwen3 ate 7/7). O killer:
  o §6-bis fail-open, 0/4 na prosa-F1 (so com F4), foi **4/4 na AN-F1** — o ganho vem do
  DOCUMENTO, nao do prompt. AINDA fraco: §6 sem-fonte (1/4); anti-armadilhas N1/N2 lidas
  como prosa pelo modelo fraco. **Confundidor**: comprimento x gate (AN e 14x menor) nao
  desconfundido — precisa 3o braco "prosa-curta". Promissor, NAO conclusivo.
- **H-B tier NUVEM CONCLUIDO** (2026-06-05, `lab/2026-06-04-strata-hipoteses/RESULTADOS-tier-nuvem.md`): 9 modelos
  (Sonnet 4.6, Haiku 4.5 think/no-think, Gemini 3 Flash, GPT-5.1-mini/5.3-Codex/5.4/
  5.4-mini, Raptor) x F1/F4 na prosa. **A nuvem SATURA na prosa-F1**: ate o Haiku (mais
  simples) tirou 7/7, incl. §6-bis e §6 — contraste gritante com o local. **P7/§6-bis em
  17/18 celulas** (local era 1/9 so com F4). **F4 NAO ajuda na nuvem** (piora: troca largura
  por foco). think≈no-think. Vazamento residual: §6 sem-fonte. **CONCLUSAO**: (1) "qualquer
  IA moderna aplica o Strata" VALIDADO p/ nuvem na prosa; (2) H-C/AI-nativo so agrega no
  **tier fraco/local** (fronteira tem teto); (3) §6 sem-fonte = ponto cego universal, alvo
  do texto da prosa. Caveat: N=1, juiz-Claude avalia Haiku, reguas inconsistentes.
- **Comporta — destilar a 1a recipe**: ADIADO ate ter uso real (rodar detect_env.py +
  arvore por ~1 semana). Base ja forte (arvore + prototipo + primitivas v2 + Estagios 1-4).
- Pendentes: C2/C3, H17, B4a (Comporta); H-C (Strata, depende de H-B).
- Calibrar deteccao do prototipo (ler entitlement Copilot; micro-bench local real).
- Pendentes de uso real: C2/C3 (Continue.dev + Copilot Chat); H17 (visao); B4a (Foundry GPU).
- **Cozinha prototipo**: testar a receita em 1-2 subprojetos reais (escala).
- **Economia de IA — experimentos propostos** (dono decide):
  - Continue.dev + qwen2.5-coder:7b por 1 semana (medir satisfação e escalada cloud)
  - Copilot Chat + Ollama habilitado (VSCode 1.113 + Ollama 0.18.3)
  - OllamaClaude MCP: medir redução de tokens em tarefa multi-arquivo real
  - AgentsRoom/cc-statistics: baseline de custo antes de qualquer otimização
- **Novas metodologias** candidatas (da analise): findability/busca
  (FTS5+sqlite-vec, grep-first), economia-de-espaco/arquival do umbrella
  (Borg/restic), catalogo de projetos (Backstage/codemeta).
