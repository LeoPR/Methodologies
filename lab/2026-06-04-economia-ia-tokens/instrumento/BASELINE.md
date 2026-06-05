---
title: Baseline congelada — Estágio 1 (A1 + A3)
created: 2026-06-04
status: frozen
window: until=2026-06-04T00:00:00Z (fase Strata, 2026-06-03 — imutável)
sha256_total: b804afeb5109e29d7d349ee1ec14ff1c05de80b9ac9d421f661495d6d35c2c29
---

# Baseline congelada — Estágio 1

> Régua de medição do plano experimental. Tudo que vier depois mede **delta**
> contra isto. Reproduzível: re-rodar o comando abaixo dá o mesmo SHA256.

## Como reproduzir (verificação do GATE-1)

```powershell
$py = "..\..\..\.venv\Scripts\python.exe"   # venv do projeto
& $py parse_usage.py --include-sidechain --until "2026-06-04T00:00:00Z" `
      --out baseline_frozen_2026-06-03.csv --snapshot
# Deve imprimir: SHA256(...) = b804afeb5109e29d7d349ee1ec14ff1c05de80b9ac9d421f661495d6d35c2c29
```

## Janela e método

- **Janela fechada**: `timestamp < 2026-06-04T00:00:00Z`. O projeto tem **uma
  única sessão** (`443991ed`), de 2026-06-03 a 2026-06-04; congelar por timestamp
  no dia 2026-06-03 (imutável) é a única forma reproduzível, pois a sessão ativa
  ainda cresce.
- **Dedup por `message.id`** (== requestId): a mesma resposta aparece em até 12
  linhas (streaming/relog); contar por linha inflaria **6,87×**. Verificado.
- **Custo USD é PROXY** à tabela 2026-06-04, **não faturado**: ambiente é Claude
  Max (quota), o JSONL grava `service_tier: standard`. Preço de Opus 4.8
  ($5/$25) **pendente de confirmação do dono**.
- Hash em memória (lê bytes do CSV) — evita lock do OneDrive durante o hashing.

## Números congelados (2026-06-03, total c/ sidechains)

| Grupo | n_msg | input | output | cache_creation | cache_read | custo proxy |
|---|---|---|---|---|---|---|
| opus-4-8 (main) | 93 | 11.849 | 368.637 | 1.201.705 | 27.369.566 | $34,98 |
| opus-4-8 (sidechain) | 148 | 34.904 | 3.070 | 1.220.915 | 15.382.722 | $15,57 |
| sonnet-4-6 (main) | 16 | 24 | 21.534 | 50.111 | 878.241 | $0,89 |
| **TOTAL** | **257** | **46.777** | **393.241** | **2.472.731** | **43.630.529** | **$51,44** |

- message.id distintos (dedup global): 267 · sintéticos excluídos: 10 · **parse-fails: 0**
- **cache_hit_rate** = cache_read / (cache_read + cache_creation + input) = **0,9454** ∈ [0,1] ✓

## Leitura da baseline (já é um achado)

O **cache_read (43,6M) domina tudo** — 94,5% dos tokens de contexto vêm de cache
a 0,1× do input. O input "novo" é minúsculo (46,7k). Ou seja: **o prompt caching
do Claude Code já está fazendo o trabalho pesado** — qualquer otimização de
contexto compete contra um cache que já está 94% quente. Isso ecoa P6 do
mapa-recursos (cache comprovado 41-80% de economia) e recalibra a expectativa:
no regime atual, "encher contexto cacheado" já é barato (confirma o gatilho de P3
onde curadoria não compensa sob cache quente).

## Status do GATE-1

- [x] **A1** — parser extrai os 6 campos canônicos com dedup por message.id; 0
  parse-fails em 7.680 linhas; reconferência independente bate (arquivo pequeno,
  3 ids, números limpos). Custo = função determinística dos tokens dedup × tabela.
- [x] **A3** — snapshot com janela absoluta fechada, SHA256 reproduzível (idêntico
  em 2 execuções), cache_hit_rate ∈ [0,1], gravado/hasheado sem lock de OneDrive.
- [ ] **A2** — validação cruzada contra `cc-statistics` (após normalização).
  Requer `uv tool install cc-statistics`. Próximo passo do Estágio 1.

> GATE-1 abre o Estágio 2 quando A2 também fechar. A1 e A3 já estão verdes.
