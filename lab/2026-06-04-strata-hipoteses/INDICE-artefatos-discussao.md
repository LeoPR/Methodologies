---
title: 'Índice de artefatos para discussão (snapshot 2026-06-16)'
created: 2026-06-16
updated: 2026-06-16
status: 'L2 — snapshot datado para discutir. Só ponteiros (ADR-005: apontar, não propagar). A verdade vive nos docs apontados.'
---

# Índice de artefatos para discussão — 2026-06-16

Reúne, num lugar só, tudo que tocamos nas frentes recentes. **Não duplica conteúdo** — aponta.
Porta de entrada permanente continua sendo [OPINIAO-DE-USO.md](OPINIAO-DE-USO.md) e o hub
[ARQUITETURA-E-EVIDENCIAS.md](ARQUITETURA-E-EVIDENCIAS.md).

## 1. O judge — justificativa científica (registrado)
- [DOSSIE-judge-justificativa-cientifica.md](DOSSIE-judge-justificativa-cientifica.md) — argumento (ideal-regulativo;
  eixos alinhamento/adequação/herança; modelo centro-ideal-perdido-drift) + 22 fontes + plano de gráficos/testes. **Falta executar** os gráficos/testes.
- Evidência interna que ele cita: [RESULTADOS-f0-confronto-juizes.md](RESULTADOS-f0-confronto-juizes.md) (convergência cross-vendor),
  [RESULTADOS-r6-2o-juiz.md](RESULTADOS-r6-2o-juiz.md) (2º juiz), [RESULTADOS-f4-execucao.md](RESULTADOS-f4-execucao.md) (GOLD 100% / 92%),
  [RESULTADOS-p1p2-anv3.md](RESULTADOS-p1p2-anv3.md) (limite da forma).
- Scripts: `../../eval/strata/compare_judges_ladder.py`, `../../eval/strata/verify_f4.py`, `../../eval/strata/judge_*.py`.

## 2. Performances por frente (git externos / reais / próprios)
**Externos open-source (terceiros, quebra circularidade):**
- [RESULTADOS-externo-bemcomportado.md](RESULTADOS-externo-bemcomportado.md) — 6 repos (slugify/tomli/humanize/mlscratch/pytorchgan/ml3months); M0 abstém 9/9 nos bem-comportados; AUDIT over-detecta.

**Reais digeridos (fg2p/nnn/pdf2md) — a frente mais densa:**
- [RESULTADOS-r8-projeto-real.md](RESULTADOS-r8-projeto-real.md) + [RESULTADOS-r8-sintese-3-projetos.md](RESULTADOS-r8-sintese-3-projetos.md) — **o R8** (disconfirmação ecológica: como auto-auditor de IA, não bate a competência pura no real).
- [RESULTADOS-p1p2-anv3.md](RESULTADOS-p1p2-anv3.md), [RESULTADOS-p6-shootout.md](RESULTADOS-p6-shootout.md), [RESULTADOS-p6-scatter.md](RESULTADOS-p6-scatter.md) — forma × modelo.

**Próprios do dono (CIRCULAR):**
- [RESULTADOS-p10-escada-propria-genero.md](RESULTADOS-p10-escada-propria-genero.md) — **NOVO**: escada K=5 gênero-consciente em aulaquantum + deeplearning (+ fg2p parcial). A assinatura por tier replica em parte; achado novo "veredito abstém / ação over-limpa".
- [RESULTADOS-genero.md](RESULTADOS-genero.md) (probe N=1 anterior), [GABARITO-genero-temporal-own.md](GABARITO-genero-temporal-own.md) (pré-registrado), [PRE-REGISTRO-own-tcf.md](PRE-REGISTRO-own-tcf.md) (hash do gabarito do TCF, run pendente de crédito).

## 3. Produto (o que o dev usa)
- [recipe/strata-com-ia.md](../../recipe/strata-com-ia.md) + [recipe/strata-com-ia-fronteira.svg](../../recipe/strata-com-ia-fronteira.svg) — guia + gráfico (barra=inventados, gradiente, DeepSeek V4, linha Local).
- [RESULTADOS-p9-modelos-novos-jun.md](RESULTADOS-p9-modelos-novos-jun.md) — P9/P9b/P9c/P9d (escada por vendor; K=5 derrubou o K=3 do topo).

## 4. Cenários / fixtures (o teor e a lógica de construção)
- [eval/strata/cenarios/README.md](../../eval/strata/cenarios/README.md) — 16 fixtures, lógica limpo↔bagunçado, § mapeada, design anti-falso-positivo; detalhe de s04/s01 (os do gráfico) + nota da correção de gabarito s04.

## 5. Método e decisões (núcleo durável)
- Núcleo L0: `../../recipe/knowledge-architecture.md` (a metodologia testada). Glossário: [../../GLOSSARIO.md](../../GLOSSARIO.md).
- ADRs do ciclo: [../../decisions/ADR-005-duplicacao-fonte-unica-proporcional.md](../../decisions/ADR-005-duplicacao-fonte-unica-proporcional.md), [../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md](../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md).
- Autoauditoria (dogfood): [AUTOAUDITORIA-repo-vs-strata.md](AUTOAUDITORIA-repo-vs-strata.md).

## 6. Harness (como medir)
- `../../eval/strata/` (README) — `hb_runner.py` (F1 brownfield), `hb_genre.py` (gênero), `hb_temporal.py`, `build_local_digest.py` (digest de projeto próprio), `compare_judges_ladder.py`, `verify_f4.py`.

## Estado / aberto (para a conversa)
- **Crédito OpenRouter ESGOTADO** (402). Bloqueados: **TCF** (pronto, pré-registrado) e **completar o fg2p** — ~US$3 num top-up.
- **Circularidade** dos projetos próprios: sinal de consistência, não validação. Quebrar = terceiros + juiz cego.
- **Pendências de argumentação** (no [BACKLOG](BACKLOG-fila-geral.md)): gráficos/testes do judge; refazer gabarito s04; 2º juiz nas células de topo.
