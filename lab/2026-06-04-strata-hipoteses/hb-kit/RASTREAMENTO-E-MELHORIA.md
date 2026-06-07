---
title: H-B/H-C — rastreamento consolidado e plano de melhoria
created: 2026-06-06
status: canônico para retomada antes de novos testes
scope: consolidar legado + execuções recentes + próximo ciclo com visibilidade de borda
---

# H-B/H-C — rastreamento consolidado

Este arquivo existe para evitar navegação cega e redescoberta.

Antes de qualquer teste novo:
1. valide o estado em `RESULTADOS-tier-local.md`, `RESULTADOS-tier-nuvem.md`, `RESULTADOS-hc-ab.md` e `RESULTADOS-piso-local.md`;
2. valide os instrumentos (`hb_limit_search.py`/`hb_matrix_score.py` vs `hb_section_score.py`/`hb_cloud_score.py`);
3. só então escolha o próximo experimento.

## 1) O que já era oficial (não é descoberta nova)

Base oficial já registrada em commits e nos resultados de referência:

- Tier local + H-B' (forma de invocação): `RESULTADOS-tier-local.md`
- Tier nuvem (fecha H-B): `RESULTADOS-tier-nuvem.md`
- A/B prosa vs AI-nativa (H-C): `RESULTADOS-hc-ab.md`
- Piso local com AN v1 (N=3): `RESULTADOS-piso-local.md`

Histórico recente de commits já aponta esse fechamento:

- `84d8317` — tier nuvem fecha o arco (nuvem satura na prosa)
- `713057b` — A/B H-C (prosa vs AI-nativa)
- `86ae2f7` — claim do recipe atualizado com evidência
- `296c3b7` — AN v1 + estudo do piso local

## 2) O que foi feito agora (06/06) e para que serviu

Execuções recentes em `planos/`:

- `planos/rescore/20260606-015201` e `.../015303`: re-pontuação por seção (`hb_section_score.py`)
- `planos/cloud-score/20260606-015759`, `.../015936`, `.../020109`: scorer conceitual de nuvem (`hb_cloud_score.py`)
- `planos/evidence/20260606-*`: snapshots de inventário (`hb_test_inventory.py`)
- `planos/limit-search/20260606-013447`: continuidade serial local (ainda com scorer legado)
- `planos/l2-sandbox*`: provas de sandbox e scoring externo

Essas execuções foram principalmente de auditoria de instrumento e organização de evidência, nao de tese nova.

## 3) Fonte da confusão (raiz)

1. Mistura entre "resultado científico" e "debug de instrumento" no mesmo fluxo de pastas timestampadas.
2. Divergência de scorers ativos:
   - legado: `hb_limit_search.py` e `hb_matrix_score.py` (casamento por `id` P1..P7)
   - revisão: `hb_section_score.py` e `hb_cloud_score.py` (seção/conceito)
3. Dois canais de coleta distintos (JSON local vs markdown de chat na nuvem) sem índice canônico único.
4. Reexecuções parciais de madrugada sem um "estado mestre" para separar:
   - o que já estava decidido,
   - o que era apenas validação de scoring,
   - o que ainda está em aberto.

## 4) Estado consolidado por pergunta de pesquisa

### Q1 — O modelo entende o Strata?

- Nuvem (frontier): evidência forte de entendimento e detecção alta no F1
  - referência: `RESULTADOS-tier-nuvem.md`
  - auditoria recente: `planos/cloud-score/20260606-020109/cloud-score-summary.md`
- Local fraco: entendimento estrutural parcial; ganhos relevantes com forma AI-nativa
  - referência: `RESULTADOS-tier-local.md` + `RESULTADOS-hc-ab.md` + `RESULTADOS-piso-local.md`

### Q2 — O modelo agiria bem (priorização e segurança)?

- Nuvem: bom sinal para priorização fail-open no F1 (auditoria conceitual recente)
- Local: melhora com AN, mas modelos pequenos ainda vazam em armadilhas e consistência

### Q3 — O modelo gera artefatos L2 com isolamento e controle de versão?

- Infra de sandbox existe e funciona (`hb_l2_sandbox.py`, `hb_l2_score_external.py`)
- Rodadas atuais ainda são preliminares e concentradas em modelo fraco (qwen3-1.7b)

## 5) Regra operacional para não repetir caos

Sempre classificar cada nova execução em UMA categoria:

- `evidencia`: mede hipótese de produto
- `instrumento`: testa/corrige harness/scorer
- `infra`: valida execução/isolamento/performance

E todo arquivo novo em `planos/` deve ter cabeçalho curto (no summary) com:

- `tipo`: evidencia | instrumento | infra
- `pergunta`: Q1 | Q2 | Q3
- `comparabilidade`: comparável com qual rodada anterior

Sem isso, não entra em síntese.

## 6) Visibilidade de borda (o que faltava enxergar)

Para cada rodada principal, reportar também os "edges":

1. cobertura de P6 (sem-fonte) e P7 (fail-open) separada do score geral;
2. taxa de queda em N1/N2 por framing;
3. taxa de corrupção de citação de seção (`§` preservado vs links);
4. taxa de alucinação por cenário;
5. robustez por variância (N>=3 quando for decisão de tese).

Esses cinco itens devem aparecer explicitamente nos próximos resumos.

## 7) Perguntas melhores (próximo ciclo)

Substituir perguntas genéricas por perguntas de decisão:

1. "Sob F1 neutro, qual família/modelo mantém P6 e P7 simultaneamente sem N1/N2?"
2. "A melhoria vem de gate semântico ou de compressão de contexto?" (A/B/C: prosa, prosa-curta, AN)
3. "Qual é o menor modelo local que sustenta det>=5 com N>=3 e sem violações de segurança?"
4. "No sandbox L2, qual taxa de artefatos mínimos válidos + aderência de segurança por modelo?"

Se a rodada não responde a uma dessas perguntas, é coleta auxiliar, não experimento principal.

## 8) Labs melhores (estrutura sugerida)

### Lab A — Entendimento controlado (Q1)
- Cenários sintéticos com gabarito fixo (já existe em `cenarios/`)
- Scoring por seção/conceito (não por id interno)

### Lab B — Segurança e priorização (Q2)
- Foco em P6/P7 + N1/N2
- Framing fixo (F1) e uma ablação mínima por vez

### Lab C — Operação L2 em sandbox (Q3)
- Geração de artefatos mínimos + `git init` + score de segurança
- Sem misturar com benchmark de contexto/performance

## 9) Próximo passo recomendado (sem teste novo agora)

1. Congelar este estado como referência de retomada.
2. Ajustar os relatórios de `limit-search`/`matrix` para marcar explicitamente "scorer legado" quando aplicável.
3. Só então abrir uma rodada nova, com hipótese única e classificação `evidencia/instrumento/infra`.

---

Resumo executivo:

- O núcleo das descobertas já estava correto e oficializado.
- As execuções de 06/06 trouxeram auditoria de instrumento e visibilidade adicional, mas se misturaram ao fluxo principal.
- Este arquivo define o trilho único para juntar tudo e melhorar os próximos testes com bordas explícitas.