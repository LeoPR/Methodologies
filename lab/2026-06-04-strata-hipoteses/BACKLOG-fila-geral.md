---
title: 'Fila geral — backlog PRIORIZADO (pós-consolidação)'
created: 2026-06-13
updated: 2026-06-20
status: 'PRIORIZADO pela consolidação (workflow + crítico de over-claim). O defrag que esta fila esperava — feito.'
---

# Fila geral — backlog priorizado (o que fazer, em ordem)

> Pós-**[consolidação](OPINIAO-DE-USO.md)** (que foi o "defrag" pedido). Estado do que já foi FEITO:
> [hub](ARQUITETURA-E-EVIDENCIAS.md). Opinião de uso: [OPINIAO-DE-USO.md](OPINIAO-DE-USO.md).

> **Fechamento da avaliação (2026-06-20):** o roadmap priorizado do que falta para a tese sair de "direção
> forte" para "prova" está em [FECHAMENTO-avaliacao-strata.md](FECHAMENTO-avaliacao-strata.md). Os passos
> baratos primeiro (re-pontuar com 2º juiz, Krippendorff/ECE sobre dado existente, juiz sem o gabarito no prompt).

## P0 — antes de mais testes
- **Honestidade de produto (redação, econômico):** carregar a **disconfirmação ecológica (R8)** e a
  **circularidade** no **topo** de todo relatório/recipe de uso (não em "abertos"). **Recalibrar
  `recipe/strata-com-ia.md`**: auto-auditor autônomo **só com topo**; médios/baratos = checklist + humano.
  *(O R8 era "o achado mais importante do reteste" e quase não aparecia na opinião de uso — o over-claim mais sério após a tese-mãe.)*
- **Braço EXTERNO (decisivo para generalizar; intermediário):** ≥1 projeto open-source **não-próprio** +
  **pré-registro de gabarito** + declaração de viés, espectro organizado→caótico (ética: repo de terceiro
  local+privado, publicar só agregado). Rodar o auto-auditor (R8) contra ele. *Sem isso, nenhum "vale em geral" é legítimo.*

## P1 — alto valor
- **Cobertura ampla de modelos, com heurística proporcional** (ideia do dono, 2026-06-14): em vez de poucos
  modelos por célula, testar **mais modelos** com uma heurística coerente — amostrar **representantes por
  tier × fornecedor × geração** (não perseguir cada release — §9), **incluir reasoners** (depende do *caminho
  reasoning-aware*, em P2), e **reportar por tier** (o que dura), com acurácia × precisão (ADR-006). Motivação:
  P9 mostrou que a assinatura por tier **persiste**, mas a lista de modelos **churna** (L2); cobertura maior e
  **datada** blindaria a generalização sem virar corrida atrás de release. Custo cresce com nº de modelos →
  orçar antes (curva OpenRouter) e priorizar as células decisivas (abstenção §9, segurança §6-bis).
- **Refazer gabarito do s04 (barato, correção):** o juiz tratava `docs-reproducao.md` como ponteiro válido, mas
  o arquivo **não existe** (nit cosmético legítimo §2). Reprocessar o s04 com o gabarito corrigido (2 nits
  triviais: mapa slash/dash + plural `decisoes`; e o ponteiro pendente). Efeito esperado: "inventados" caem ~1
  em quem apontou o link; ranking não muda. Detalhe: [cenarios/README §s04](../../eval/strata/cenarios/README.md).
- **Firmar os achados do P10 (revisão adversarial, 2026-06-16):** os 4 achados refinados são **direcionais, não
  causais** — o framing gênero-consciente confunde ruído×abstenção. Para isolar: (1) rodar o **TCF-limpo sob o
  framing "ache problemas"** (cruzar ruído × framing); (2) **fixture par-a-par** que varie só a legibilidade do
  tombstone (sem "Lista de Lixo" embutida, sem PII); (3) **múltiplos projetos de terceiros** + gabarito
  gênero-consciente pré-registrado por independente + **juiz não-Claude**. Detalhe em [P10](RESULTADOS-p10-escada-propria-genero.md).
- **Redação clara para IA pode ter estilo próprio (hipótese registrada, a pensar depois):** a clareza para a
  IA talvez peça um texto mais comprimido que a Linguagem Simples humana; o Strata quer ficar pequeno e servir a
  máquina ao mesmo tempo. Inclui: a clareza de redação como complemento do Strata; "tokens completos" como
  possível métrica; uma ou duas superfícies (humana × densa); liga-se ao Comporta (menos tokens = menos custo).
  Detalhe em [IDEIA-redacao-clara-para-ia.md](IDEIA-redacao-clara-para-ia.md).
- **Argumentar o JUDGE (registrado, a executar):** o dossiê [DOSSIE-judge-justificativa-cientifica.md](DOSSIE-judge-justificativa-cientifica.md)
  já reúne o argumento (ideal-regulativo; eixos alinhamento/adequação/herança; modelo centro-ideal-perdido-drift) + literatura
  (Zheng/MT-Bench, G-Eval, Messick, Krippendorff, GUM, PoLL) + evidência interna (F0 cross-vendor, R6 2º juiz, F4 92%×F3 56%).
  **Falta produzir** os gráficos (§6: scatter objetividade×concordância, escada de juízes, centro/drift, Bland-Altman, calibração/ECE)
  e rodar os testes (Krippendorff α com IC, PoLL nas células de juiz único, ECE, kappa juiz×humano). Reconferir citações antes de uso externo.
- **Gráfico barato × caro por vendor — FEITO** ([P9 §P9b](RESULTADOS-p9-modelos-novos-jun.md)): Haiku (barato
  Anthropic), **Opus refeito sem truncamento** (= o melhor: over-ação 1,2 / recall 4/4 / seg 5/5), glm-4.5-air
  (barato Z-ai) medidos; gráfico reconstruído por vendor. Achado: **caro ≠ melhor** (gemini-2.5-pro caro nem
  rodou; Haiku barato age + que todos). **Resta:** os **reasoners** (os "caros" novos — gemini-2.5-pro,
  deepseek-R1, gpt-5-mini/nano) só medíveis com o **caminho reasoning-aware** (item acima).
- **Claude como SUJEITO — fechar o topo:** **Opus** em **f4-clean** (abstenção por execução, célula decisiva
  **não rodada**) + **f4-trap** (reconciliação), julgado por não-Claude. *(Haiku/Sonnet já rodaram — escada-claude.)*
  Decisão de gasto: testar Opus **só** como sujeito-Claude, **não** como teste isolado de §9 (o mapa-de-bordas já
  diz que gpt-4.1 basta → Opus isolado é redundante). Mitigar viés-de-família (R6) com juízes neutros.
- **Eixo ESFORÇO (econômico):** Sonnet+thinking na abstenção com **N≥3 + 2º juiz** (hoje 0/2→1/2 está dentro do ruído).
- **Strata CURTO AI-nativo (design) + replicar R4** (razão compressão:gates ~2/3:1/3) na nuvem com 2º juiz.

## P2 — blindar e melhorar
- **Autoauditoria — FEITA com cross-check** ([AUTOAUDITORIA-repo-vs-strata](AUTOAUDITORIA-repo-vs-strata.md)):
  o fan-out de 5 auditores rodou (limite reabriu); aderência **forte**, baratos consertados. Restou **não-trivial**:
  (a) §10 **fixity `--verify`** — `hash_fixture.py` grava `.fixture-hash` mas nada recomputa/compara; adicionar
  modo `--verify` chamado no início de `hb_f3/f4`; (b) §1/§9 mover `recipe/_variants/` e os `aggregate_<exp>.py`
  one-off para `eval/strata/` quando tocar (risco de quebrar run scripts; não agora).
- **Reasoners — PARSE corrigido** (2026-06-15, `hb_runner`): o `content=None` era **bug de parse, não
  incapacidade** do modelo. Agora `call_openrouter`/`_ex` caem p/ `message.reasoning` quando `content` vem vazio
  (espelha o fallback do Ollama) + `--num-predict` folgado (5000). Smoke OK: gpt-5-mini produz plano; gemini-2.5-pro
  devolve o canal de raciocínio. **Resta refinar:** marcar `finish_reason==length` como INDETERMINADO (não
  falso-zero) e o eixo-esforço (`reasoning_effort` low/med/high).
- **Acesso aos modelos do Copilot — decidido (2026-06-15):** testar via **OpenRouter** (tem a lista do Copilot:
  Opus 4.8 / Sonnet 4.6 / Haiku 4.5 / família GPT-5 / Gemini 3.x), limpo e reproduzível. A bridge `copilot-api`
  (usa a licença direto, grátis) é **zona cinza de ToS** — uso automatizado em lote dispara abuse-detection →
  risco de **ban** (casos documentados); só p/ volume mínimo manual. O **GitHub Models API** é sancionado p/ eval
  mas **não cabe** (cap ~4k tok; nosso prompt tem ~17k) e é catálogo diferente. Fatos: **gpt-4.1 aposentou (01/06)
  → GPT-5.5**; **Fable 5 suspenso (12/06) → Opus 4.8 é o teto Anthropic real**; Opus no Copilot costuma exigir Pro+.
- **Fechar a medição:** 2º juiz cross-vendor nas células **decisivas** (abstenção, compressão, datas, eco) +
  **reteste-limpo da NUVEM** contra fixture congelado (remove o asterisco "juiz único" de várias linhas).
- **Reescrita de NARRATIVA (loop):** reforçar **§9** ("quando NÃO agir" / permitir "nada a corrigir" / situar
  no tempo antes de julgar) e **des-lexicalizar §6-bis** (recusa menos dependente de keyword). *(Os padrões que
  NÃO somem com mais modelo — super-engenharia, falso-positivo no real, segurança lexical — são design da orientação.)*
- **Posição/saliência da §9 — RESOLVIDO** ([P8](RESULTADOS-p8-posicao-saliencia-s9.md), seções P8b/P8c):
  o placebo (A/B/C, K=5) **refutou a posição** (banner neutro C = canônico A) e mostrou que o "8→3" do K=2
  era sorte; o conteúdo (critério de abstenção) move o modelo capaz mas é **fraco e instável** (1/5).
  **Decisão: NÃO adicionar a âncora ao canônico.** Aberto só se quiser blindar: **2º juiz não-Claude** (remove
  a circularidade Claude-julga-Claude) — baixa prioridade, a decisão já está tomada.
- **F6 / temporalidade longitudinal:** testar se a limitação temporal/fonte é **fundamental** (some com datas+
  instrução? ferramentas? escala?). Decide a "tese-mãe" — hoje o sinal **mais ruidoso**; alto valor de tese, baixo de uso imediato.

## P3 — cobertura e expansão
- **Decompor L1/L2:** pontuar "nomear formalização" (L1) e "ferramentas datadas" (L2); testar **com-pesquisa**
  num modelo pequeno **bem-calibrado** (onde P7 prevê maior ganho da web). *(Toda a detecção medida é L0.)*
- **Registro/declaração de uso de IA (proveniência §3-bis) — REGISTRO, a pesquisar:** normas de publicação
  científica + lei (UE/BR/EUA/propostas) + padrões técnicos (C2PA/SPDX/trailers); camadas por etapa/granularidade/
  artefato; propor 1 padrão **L1** + ADR de encaixe; dogfood no próprio repo. Desenho em
  [`IDEIA-registro-uso-ia.md`](IDEIA-registro-uso-ia.md). *(Pedido do dono 2026-06-14 — não executar agora.)*
- **Cenários/gêneros:** PatchCraft (2º de código); **AulaQuantum/DeepLearning** (gênero "acompanhamento de aula"
  + temporalidade). Combina com o braço externo.
- **Decisões de design abertas:** exportação/tradução = **corolário L0 curto** (não uma "L3"); arquivo-extra
  **Q&A** L1/L2 **só** se não colapsar em "sempre-ache-problema" (medir pelos controles de abstenção antes);
  **fronteira Strata × Comporta** (aparece em caches E setup-de-agente — resolver de uma vez); classificar
  artefatos de ambiente (canônico×regenerável×efêmero) como princípio L0/L1 em satélite L2.
