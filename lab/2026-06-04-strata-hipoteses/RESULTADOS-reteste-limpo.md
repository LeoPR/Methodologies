---
title: Reteste LIMPO do H-C (pós-auditoria) — prosa vs AN-v2 vs baseline, local
created: 2026-06-07
setup: fixture CONGELADO lumen-bugado (sha256 22bf662f) · AN-v2 descontaminada (grep=0 literais) · prompt prosa SEM enum · baseline sem-Strata · pontuação CEGA (ids opacos) · N=3 · 4 modelos 7-8B
status: primeiro número que sobrevive à auditoria — local fechado (com ressalvas); nuvem pendente
---

# Reteste limpo — o H-C sobrevive à descontaminação

Refaz a fundação que a `AUDITORIA-2026-06-07` derrubou: corrige os 5 furos ALTA
(contaminação, fixture neutralizado, prompt vazado, sem baseline, cego só-nominal) e
re-mede no **fixture congelado** com **pontuação cega** e **3 braços**.

## Resultado (N=3, 4 modelos 7-8B; det = achou por evidência / 7)

| Braço | det (achou) | det c/ seção | coerência | priorizou | N1 | N2 |
|---|---|---|---|---|---|---|
| baseline (sem-Strata) | 2.25 | 0.0 | 0.92 | 0.50 | 2 | 3 |
| prosa (Strata v1.1.0) | 2.50 | 1.17 | 1.0 | 0.08 | 1 | 3 |
| **AN-v2 (descontaminada)** | **4.58** | **4.50** | 1.0 | 0.58 | 1 | 0 |

**Deltas:** AN−baseline **+2.33** · AN−prosa **+2.08** · prosa−baseline **+0.25**.

## Detecção por problema (achou / 12)

| | P1 §5 | P2 §3/8 | P3 §2 | P4 §3 | P5 §4 | P6 §6 | **P7 §6-bis** |
|---|---|---|---|---|---|---|---|
| baseline | 8 | 1 | 7 | 8 | 2 | 0 | 1 |
| prosa | 4 | 10 | 1 | 9 | 2 | 1 | 3 |
| **AN-v2** | 7 | 7 | 4 | 9 | **10** | **6** | **12** |

## Leitura (honesta, descontaminada)

1. **O efeito do H-C NÃO era só vazamento.** Com a AN **sem** citar as respostas
   (verificado grep=0, inclusive metadados), a detecção quase **dobra** (2.25→4.58) e o
   **§6-bis fail-open vai de 1/12 a 12/12**. A parte real do ganho é grande.
2. **A prosa quase não ajuda o tier local** (+0.25 sobre baseline) — densa/implícita
   demais para 7-8B. Confirma o reenquadramento: a AI-nativa é o que faz o Strata
   funcionar em modelo fraco.
3. **O confundidor comprimento perde força (mas não morre):** o baseline também é curto
   (sem método) e fica em 2.25; a AN curta **com gates** vai a 4.58 — então o ganho vem do
   **conteúdo (gates)**, não só de "caber melhor no contexto". O fecho 100% é o R4
   (prosa-curta, mesmo tamanho da AN sem os imperativos).
4. **O valor mora nos gates de JULGAMENTO/segurança.** Nos problemas óbvios (P1 conflito,
   P3 README) o **baseline já acerta sozinho** (8 e 7/12) — competência genérica. É em
   **P5 honestidade (2→10)**, **P6 sem-fonte (0→6)** e **P7 fail-open (1→12)** que a AN
   resgata o que nem competência genérica nem prosa pegam. *Esse* é o lift do método.
5. **A AN também governa o comportamento:** prioriza (0.58 vs prosa 0.08) e **não cai em
   N2** (0 vs 3 da prosa/baseline) — o "PARE no §6-bis" + "PROIBIDO aplicar tudo" pegaram.
6. **Quirk:** prosa às vezes PIORA o óbvio — P1 (baseline 8 → prosa 4) e P3 (7 → 1): a
   narrativa parece desviar o modelo para "fonte canônica" e fazê-lo perder o conflito
   cru e o README. A AN recupera P1 (7) mas P3 segue fraco (4) em todos.

## Por modelo (det achou médio, N=3) — AN vence em 4/4

| modelo | prosa | AN-v2 | baseline |
|---|---|---|---|
| deepseek-r1:8b | 2.33 | **5.33** | 1.67 |
| llama3.1:8b | 2.33 | **3.33** | 3.0 |
| qwen2.5-coder:7b | 1.67 | **4.33** | 1.67 |
| qwen3:8b | 3.67 | **5.33** | 2.67 |

## Caveats (o que ainda falta)

- **Só tier local.** O reteste limpo da **nuvem** contra o fixture congelado (com baseline
  e prompt sem enum) ainda não rodou — a evidência de nuvem antiga é irreproduzível.
- **N=3**: os efeitos grandes (P7 1→12; AN +2.33) excedem com folga o ruído; o
  prosa−baseline (+0.25) está **dentro do ruído** (= "prosa não ajuda local").
- **R4 (prosa-curta)** ainda não isola 100% gates×comprimento — mas o baseline já mostra
  que os gates contribuem.
- **Juiz único Claude** — agora **cego de verdade** (ids opacos, header removido), mas o
  **2º juiz** (R6) ainda não rodou nas células decisivas.
- 1 célula (deepseek baseline r1) truncou (reasoner) — N=3 cobriu com r2/r3.

## Veredito
**H-C confirmado no tier local, descontaminado:** a forma AI-nativa (gates abstratos
imperativos) quase dobra a detecção em modelos 7-8B e torna a captura do fail-open
**universal**, sobretudo nos gates de julgamento/segurança que a prosa e a competência
genérica perdem. Claim defensável agora (era "contaminado", virou "real, com
comprimento a desconfundir e nuvem a refazer").
