---
title: 'Fila geral — backlog PRIORIZADO (pós-consolidação)'
created: 2026-06-13
updated: 2026-06-14
status: 'PRIORIZADO pela consolidação (workflow + crítico de over-claim). O defrag que esta fila esperava — feito.'
---

# Fila geral — backlog priorizado (o que fazer, em ordem)

> Pós-**[consolidação](OPINIAO-DE-USO.md)** (que foi o "defrag" pedido). Estado do que já foi FEITO:
> [hub](ARQUITETURA-E-EVIDENCIAS.md). Opinião de uso: [OPINIAO-DE-USO.md](OPINIAO-DE-USO.md).

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
- **Completar o gráfico: barato E caro POR VENDOR** (amanhã; precisa **top-up OpenRouter**, saldo ~US$0,04).
  Regra do dono: o gráfico tem que mostrar **o barato e o caro de cada vendor**. Hoje incompleto:
  - **Anthropic** só com o caro (Opus) → **adicionar o Haiku** (barato).
  - **Google** só com baratos → adicionar um **caro** (gemini-2.5-pro / 3.x-pro).
  - **DeepSeek / Z-ai** com 1 modelo só → adicionar o par barato/caro.
  - **Refazer o Opus SEM truncamento** (foi cortado em 1500 tok → recall do s01 subestimado; usar `--num-predict ≥2500`).
  Mesmo protocolo (s04/s01, K=5, temp 0,3); reaproveitar o que já existe.
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
- **Caminho reasoning-aware no harness** ([P9](RESULTADOS-p9-modelos-novos-jun.md)): os modelos novos da OpenAI
  (gpt-5-mini/nano e a família codex) são **reasoners** e devolvem `content=None` no fluxo F1 completion-only
  (`call`). Usar `call_ex(think=True)` + orçamento de tokens maior no `hb_runner` p/ medi-los com justiça. Sem
  isso, "como os reasoners se saem" fica **em aberto** (o gpt-5-mini deu sinal promissor mas truncado).
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
