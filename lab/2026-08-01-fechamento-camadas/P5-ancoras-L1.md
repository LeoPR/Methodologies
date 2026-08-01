---
title: P5 — Âncoras da Parte II (L1) — pendências editoriais de mapeamento
created: 2026-08-01
updated: 2026-08-01
status: aplicada (2026-08-01) — editorial/mecânico; autorização "pode finalizar" do dono.
---

# P5 — Âncoras do L1: o que faltava mapear

Parte editorial (sem literatura nova — usa o que as partes anteriores já
verificaram). Inventário real da Parte II (EN): âncoras para §2, §3, §3-bis,
§4, §5, §6, §6-bis, §7, §8, §10 e "publishing". Pendências e resolução:

1. **§1 sem âncora; Cookiecutter sob §8.** A linha *Cookiecutter Data Science*
   ("layout que separa fisicamente dado/código/saída — sinal vs ruído") estava
   na tabela de §8 (versionamento), mas o que ela formaliza é **§1** (os três
   tipos de artefato, separados). → **Movida** para a nova âncora
   `## For §1 — the three kinds, physically separated` (primeira seção da
   Parte II). A tabela de §8 fica só com versionamento de fato (Conventional
   Commits, SemVer/Keep a Changelog).
2. **"For generating and prioritizing work from knowledge" sem âncora.** A
   tabela (Kanban/OKR/MoSCoW) é a continuação operacional de §7 (o pipeline
   gera trabalho; aqui se prioriza). → **Re-ancorada** como
   `## For §7 (cont.) — generating and prioritizing work from knowledge`.
   Nenhuma linha muda.
3. **§11 (entrou na P1) sem âncora L1.** O Grounding de §11 já carrega a
   teoria; a Parte II é o lugar das **formalizações consolidadas**. → Nova
   âncora `## For §11 — classification schemes`, 3 linhas (enumerativo,
   facetado, domínio/literary warrant) com as mesmas fontes `[WEB ✓
   2026-08-01]` da P1 — sem duplicar a teoria (ADR-005: a tabela aponta, o
   Grounding fundamenta).
4. **§9 sem âncora — e fica assim, declarado.** §9 é um **regulador** (quanto
   organizar), não uma operação com formalizações próprias: sua expressão L1
   já existe **distribuída** — são as notas de **Adherence** dentro de cada
   seção do L0 e os "change-signal" das tabelas. Criar tabela para §9 seria
   duplicar Knuth/YAGNI/Grice, que já estão no Grounding de §9. Resposta
   honesta registrada, nada muda (preservar o negativo, §4).

## Decisão (dono, 2026-08-01)

- [x] "ok, pode finalizar" — aplicado EN-first + PT derivado no mesmo ciclo;
  guardas passando. Com isto **o ciclo P1–P5 fecha** e o L0 fica editorialmente
  fechado; a questão macro seguinte é a declarada pelo dono: **como testar o
  L0 fechado**.
