---
title: 'Fila geral — backlog PRIORIZADO (pós-consolidação)'
created: 2026-06-13
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
- **Claude como SUJEITO — fechar o topo:** **Opus** em **f4-clean** (abstenção por execução, célula decisiva
  **não rodada**) + **f4-trap** (reconciliação), julgado por não-Claude. *(Haiku/Sonnet já rodaram — escada-claude.)*
  Decisão de gasto: testar Opus **só** como sujeito-Claude, **não** como teste isolado de §9 (o mapa-de-bordas já
  diz que gpt-4.1 basta → Opus isolado é redundante). Mitigar viés-de-família (R6) com juízes neutros.
- **Eixo ESFORÇO (econômico):** Sonnet+thinking na abstenção com **N≥3 + 2º juiz** (hoje 0/2→1/2 está dentro do ruído).
- **Strata CURTO AI-nativo (design) + replicar R4** (razão compressão:gates ~2/3:1/3) na nuvem com 2º juiz.

## P2 — blindar e melhorar
- **Fechar a medição:** 2º juiz cross-vendor nas células **decisivas** (abstenção, compressão, datas, eco) +
  **reteste-limpo da NUVEM** contra fixture congelado (remove o asterisco "juiz único" de várias linhas).
- **Reescrita de NARRATIVA (loop):** reforçar **§9** ("quando NÃO agir" / permitir "nada a corrigir" / situar
  no tempo antes de julgar) e **des-lexicalizar §6-bis** (recusa menos dependente de keyword). *(Os padrões que
  NÃO somem com mais modelo — super-engenharia, falso-positivo no real, segurança lexical — são design da orientação.)*
- **Posição/saliência da §9 — confirmar antes de editar o produto** ([P8](RESULTADOS-p8-posicao-saliencia-s9.md)):
  o A/B inicial deu sinal de que uma âncora-§9 no topo **calibra o modelo capaz** (gpt-4.1: 8→3 defeitos
  fabricados) mas **~nada no fraco** (teto de capacidade), e é **segura** (recall mantido). Falta a rodada que
  decide se a âncora entra no `knowledge-architecture.md`: **A/B/C** (incluir placebo p/ separar posição de
  conteúdo) + **K≥5 no topo** + 2º cenário limpo + 2º juiz não-Claude. *(N pequeno; juiz único Claude.)*
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
