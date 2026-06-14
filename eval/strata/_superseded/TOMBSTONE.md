---
title: 'TOMBSTONE — arco antigo do harness (lumen → matrix → limit-search)'
created: 2026-06-14
status: 'SUPERSEDED / arquivado (append-only). NÃO usar — registro histórico.'
---

# Arco antigo do harness — arquivado, não usar

Estes arquivos são o **primeiro arco** do harness do Strata (2026-06-05 a 06-07): o fixture **lumen**
(`projeto-alvo/`, `fixtures/lumen-bugado/`, `gabarito.md`, `scenario_manifest.json`), a **matriz** automática
(`hb_matrix_runner/score`, `matrix_models.json`), a **busca de limite** (`hb_limit_search`,
`run_limit_search_serial.ps1`), scorers por-seção/nuvem/inventário (`hb_section_score`, `hb_cloud_score`,
`hb_test_inventory`), agregadores de experimentos encerrados (`aggregate_{p6,p1p2,clean,cloud}.py`) e os
scorers-workflow (`score_*.workflow.js`).

## Por que foi aposentado
A **AUDITORIA-2026-06-07** (adversarial multi-agente) refutou este arco por furos que invalidavam os números:
1. o **prompt vazava a taxonomia** P1..P7 (media vazamento, não compreensão);
2. **fixture neutralizado ≠ gabarito** (`projeto-alvo` sem P1/P7; `velho/`+`tarefas.txt` nunca em disco; irreproduzível, sem hash);
3. **scorers por-id** (P1..P7) produziam **zeros artefatuais**;
4. **online automático nunca rodou** (sem keys; "nuvem" era chat manual N=1);
5. **sem baseline/controle**.

## O que o substituiu (pipeline VIVO)
`hb_f3/f4/f5/f6` + `hb_genre/temporal/m0` sobre `cenarios/*` com **gabarito FORA da fixture**
(`f4-manifests/`, `f6-*-manifest.json`), verificação **mecânica + GOLD-gate** (`verify_f4.py`) e **juízes
cross-vendor** (`judge_f3/f4`). Ver [`../README.md`](../README.md).

## Por que preservado (não apagado)
§3/§8 do Strata (append-only): um instrumento **refutado** é conhecimento — registra **como** a pontuação cega
foi feita e **por que** foi abandonada. `hb_runner.py` **não** está aqui: virou a **biblioteca-base viva**
(`call_ex`/`read_target`) que os runners atuais importam.
