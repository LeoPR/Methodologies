---
title: NOTAS — Shake-down do instrumento contra o L0 fechado (diário)
created: 2026-08-02
updated: 2026-08-02
status: em curso — fumaça f4-dup × qwen3.6:27b relançada com timeout 3600s
---

# NOTAS — Shake-down (diário append-only)

## 2026-08-02 — Fumaça 1 falhou: timeout 900s × 27b com offload

**Sintoma:** `f4-dup × qwen3.6:27b × K=1` (braço Strata) → `ERRO: timed out`
(arquivo `.ERROR.txt` escrito 15 min após o início — batendo com o timeout).

**Investigação (root cause, medido):**
- O caminho ollama do `hb_runner.py` (`call_ollama` / `call_ollama_ex`) tinha
  `timeout=900` **hardcoded**, calibrado na matriz local de 2026-06 (modelos
  4-8B inteiros na GPU).
- Probe direto no ollama (`/api/chat`, think=true): **geração 4,3 tok/s**,
  prefill 217,7 tok/s, load 27,7s — offload CPU pesado na RTX 3060 12GB
  (o modelo tem 17GB; ~5GB ficam fora da GPU).
- Estimativa do run real: prefill ~12k tok (≈55s) + thinking+arquivos
  ~5-10k tok a 4,3 tok/s → **≈20-40 min/run** ≫ 900s. Confirmado.

**Fix (aditivo, zero blast radius — filosofia declarada do harness):**
`STRATA_OLLAMA_TIMEOUT` (env) com default 900 inalterado, aplicado nas duas
chamadas ollama do `hb_runner.py`. Verificado: import OK, env respeitada.

**Decisões derivadas:**
- O 27b segue na matriz como **local-possível** (lento é medida, não defeito);
  K por célula fica pequeno no 27b (cada run ≈ 20-40 min de máquina ocupada).
- `qwen3:14b` (cabe inteiro na GPU) carrega o peso das células de volume.
- Não se desliga `think` nem se corta `num_predict` para "caber no timeout" —
  truncamento gera falso-zero/INDETERMINADO (regra herdada); o tempo é dado
  do modelo, não defeito do instrumento.

**Pendente:** veredito do run relançado (fumaça 2, timeout 3600s) — scorer
`verify_f4.py` sobre `planos/f4s-dup-strata`.
