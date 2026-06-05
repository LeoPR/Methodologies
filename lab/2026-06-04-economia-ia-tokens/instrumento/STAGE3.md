---
title: Estágio 3 — GATE de protocolo tool_use (D0.5)
created: 2026-06-04
status: GATE-3 PASSA (2/3 modelos) — ramo agêntico-local VIÁVEL com modelo certo
instrumento: test_toolcall.py (custo zero, inferência local)
---

# Estágio 3 — GATE de protocolo tool_use

> O gate mais barato e mais decisivo: o Claude Code, ao rodar sobre Ollama local
> (`ANTHROPIC_BASE_URL=http://localhost:11434`), precisa que o shim `/v1/messages`
> emita blocos **`tool_use` estruturados** (`stop_reason: tool_use`). Sem isso, o
> loop agêntico (ler arquivo → chamar ferramenta → editar) não fecha. A verificação
> adversarial do plano **previa falha** (chamada voltaria como texto/end_turn).

## Resultado — a previsão adversarial foi DERRUBADA (parcialmente)

`POST http://localhost:11434/v1/messages` com `tools[]`, prompt que força chamada:

| Modelo | Veredito | Resposta |
|---|---|---|
| **qwen2.5-coder:7b** | ❌ FAIL | `stop_reason: end_turn`; chamada como **texto**: `{"name":"get_weather","arguments":{"city":"Paris"}}` |
| **llama3.1:8b** | ✅ PASS | `stop_reason: tool_use`; `content:[{type:tool_use, name:get_weather, input:{city:Paris}}]` |
| **qwen3:14b** | ✅ PASS | `stop_reason: tool_use`; `content:[{type:thinking},{type:tool_use,...}]` |

**GATE-3: PASSA (2/3).** O shim do Ollama **não é** quebrado — ele emite `tool_use`
estruturado corretamente para modelos cujo template/treino suporta (llama3.1, qwen3).
O adversarial estava certo **só para o qwen2.5-coder:7b** (que emite a chamada como
texto). **É dependente do modelo, não do shim.** Lição: a refutação adversarial
acertou o sintoma mas generalizou demais a causa — só a execução real desambiguou.

## A tensão central que isto revela

| Eixo | Modelo rápido/estável | Modelo com tool_use |
|---|---|---|
| Autocomplete (B1/B2) | **qwen2.5-coder:7b** (55 t/s, estável) | — (não precisa tool_use) |
| Agêntico (Claude Code) | — (qwen-coder FALHA tool_use) | **llama3.1:8b** ✓ / qwen3:14b ✓ |

O modelo mais rápido **não** serve para agêntico-local; o candidato agêntico é o
**llama3.1:8b** (passa tool_use, 8B ~4,9 GB). O qwen3:14b passa mas bate no penhasco
de VRAM (B2: 13 t/s instável). E o Claude Code agêntico pede **32k+** de contexto —
onde o penhasco WDDM mora. Por isso a viabilidade real depende de medir llama3.1:8b
**no contexto agêntico (32k)**:

## Caracterização do llama3.1:8b (candidato agêntico) — medido

| num_ctx | decode (t/s) | IQR | VRAM (ollama) | livre | regime |
|---|---|---|---|---|---|
| 4.096 | **21,1** | 4,4% | 5,4 GB | 5061 MiB | estável, mas lento |
| 32.768 (agêntico) | **19,5** | 16,9% | 9,2 GB | **1403 MiB** | usável, VRAM apertada |

Dois fatos:
1. **O llama3.1:8b é 2,6× mais lento que o qwen2.5-coder:7b** (21 vs 55 t/s @ 4k).
   O modelo *rápido* não faz tool_use; o modelo *com tool_use* é lento. (Provável
   diferença de quantização/arquitetura — qwen-coder Q4_K_M vs llama3.1 default.)
2. A **32k** (contexto que o Claude Code agêntico exige), roda a **~19,5 t/s** com
   só **1,4 GB livres** — não desabou no penhasco (held 100% GPU), mas está na borda.

## Veredito do Estágio 3 (célula "Claude Code 100% local")

**PROTOCOLO-VIÁVEL, mas PERFORMANCE-MARGINAL nesta máquina.**
- ✅ Protocolo: llama3.1:8b emite tool_use estruturado → o loop agêntico fecha.
- ⚠ Performance: ~19,5 t/s @ 32k. Uma resposta de 256 tokens leva ~13 s; loops
  agênticos têm muitos turnos → sessão lenta. VRAM a 1,4 GB livres = sem folga.
- **Conclusão**: viável para tarefas agênticas LEVES e offline-tolerantes; para
  trabalho multi-arquivo pesado, o Claude Max (cloud) é incomparavelmente melhor.
  Isto NÃO é o "morto por protocolo" que o adversarial previu — é "vivo, porém
  marginal", e a evidência (não a suposição) é que decide.

## GATE-3: status — ABERTO (destrava D1/E4 com ressalva de performance)
- [x] D0.5 — tool_use estruturado confirmado p/ llama3.1:8b e qwen3:14b; FALHA p/
  qwen2.5-coder:7b (emite texto). **Dependente do modelo, não do shim.**
- [x] llama3.1:8b caracterizado @ 4k e 32k: viável mas lento (~20 t/s), VRAM apertada.
- **Recomendação de stack local**:
  - **Autocomplete** → qwen2.5-coder:7b (55 t/s, sem necessidade de tool_use).
  - **Agêntico-local leve** → llama3.1:8b (tool_use ✓, ~20 t/s @ 32k, marginal).
  - **Agêntico pesado** → cloud (Claude Max) — local não compete em velocidade.

> **Decisão para Estágios 5/6**: D1/E4 (Claude Code 100% local pago) só vale a pena
> testar com tokens reais se o dono quiser quantificar a economia VS a lentidão de
> 20 t/s. O gate não os matou, mas a performance medida já sugere que o ganho de
> "tokens economizados" vem ao custo de uma sessão ~3-5× mais lenta. Custo-zero
> já respondeu o essencial.
