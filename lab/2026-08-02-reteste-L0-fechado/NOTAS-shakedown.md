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

## 2026-08-02 — Estratégia nuvem×local (decisão do dono): nuvem carrega o volume

**Contexto:** créditos OpenRouter medidos — **$33,18 livres**; surrogates de
todas as classes de GPU disponíveis a ~1-2¢/run (tabela no PLANO §3-bis).

**Decisão:** a **nuvem mede capacidade** (volume, K maior, brands — barato e
rápido); o **local ancora viabilidade** (probes tok/s + 1-2 células por classe).
A fumaça 2 (27b local) ganha **papel duplo**: primeira medida do 27b **e**
âncora da ponte nuvem×local da classe 12GB — ao completar, roda-se a mesma
célula (`f4-dup`, Strata, K=1) no `qwen/qwen3.6-27b` do OpenRouter e compara-se
o veredito: convergência = ponte calibrada; divergência = efeito-quantização
medido (fp8/bf16 nuvem × q4_K_M local), que o manual declara.

**Consequência operacional:** GPU local livre na maior parte do tempo; a matriz
de núcleo sai por ~$1-3 na nuvem em minutos. Local só para âncoras e para o
que a nuvem não mede (viabilidade real na 3060).

## 2026-08-02 — Primeira célula nuvem: Strata PASS × baseline FALHA (K=1)

**Física reasoner-budget (registrada para a matriz):** `num_predict 5000` →
`INDETERMINADO-TRUNCADO` no 27b nuvem (o thinking consumiu o orçamento; scorer
aplicou a regra herdada corretamente). Com `num_predict 12000`: stop limpo.
**Reasoner-sujeito exige budget maior** — mesma nota que o corpus já tinha para
juízes (700→1500). A matriz nuvem usa 12000 daqui em diante.

**Resultado (f4-dup, §5 fonte-única, `qwen/qwen3.6-27b`, K=1 por braço):**

| Braço | Veredito mecânico | Tempo | Tokens |
|---|---|---|---|
| STRATA | **PASS** | 81s | 3615 |
| BASELINE (sem Strata) | **FALHA_CORRECAO** | 35s | 2698 |

Leitura (direção, não prova — K=1): no **mesmo modelo, mesma célula**, o método
decide — capacidade (27b) põe o modelo na zona de competência; a forma (Strata)
corrige o conserto. Coerente com a tese-mãe do corpus ("a forma corrige o viés;
a capacidade calibra") e **primeiro dado da hipótese temporal**: o corpus
registrava zero PASS no F4-local 4-8B de junho.

**Pendentes:** âncora local (fumaça 2, 27b q4_K_M na 3060) para fechar a ponte
nuvem×local; K maior para firmeza; juiz cross-vendor sobre os planos.

## 2026-08-02 — Âncora local PASS: ponte nuvem×local CONVERGE (K=1)

**Run local completou** (fix do timeout validado): `f4-dup × qwen3.6:27b`
(q4_K_M, RTX 3060 12GB, offload parcial) — **1334s (22 min), 4134 tok,
stop=stop**, veredito mecânico **PASS**.

| f4-dup, braço Strata, K=1 | Veredito | Tempo | Tokens |
|---|---|---|---|
| Nuvem (`qwen/qwen3.6-27b`, fp8) | PASS | 81s | 3615 |
| Local (`qwen3.6:27b` q4_K_M, 3060) | PASS | 1334s | 4134 |

Três leituras (K=1, direção):

1. **Ponte calibrada**: mesmo veredito nos dois lados — o efeito-quantização
   (fp8 nuvem × q4 local), se existe, não moveu o veredito nesta célula. A
   nuvem pode carregar o volume da classe 27b; a ponte se fortalece com mais
   células-âncora (K>1, outros cenários).
2. **Viabilidade medida para o manual**: na 3060 12GB, o 27b **funciona** mas
   custa ~22 min/run com offload — serve para poucas ações-chave por dia, não
   para volume. É a coluna "o que esperar" da classe 12GB.
3. **Hipótese temporal confirmada na condição original**: o 27b **local** PASSA
   onde os 4-8B locais de junho zeravam — mesma condição (local, 12GB) que
   produziu o negativo do corpus. "Local não age" (2026-06) → "local-2026-08
   age, devagar" (K=1).

**Opcional em aberto:** baseline local (mais ~22 min de GPU) fecharia o desenho
também no lado local; a prioridade segue para o núcleo nuvem.
