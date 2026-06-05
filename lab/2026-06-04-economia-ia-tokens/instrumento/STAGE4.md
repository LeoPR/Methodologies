---
title: Estágio 4 — integração de editor (autocomplete e chat local)
created: 2026-06-04
status: C1 medido (objetivo); C2/C3 preparados e entregues p/ uso real
instrumento: fim_latency.py + continue-config-sugerida.yaml
---

# Estágio 4 — integração de editor

> O que é mensurável por mim (latência model-side) eu medi. O que exige a extensão
> instalada + digitação real (overhead do editor, taxa de aceitação, fricção de
> setup) é entregue ao dono — são dados de **uso**, não de bancada.

## Achado de ambiente: perfis do VSCode

`code --list-extensions` mostra só `markdown-preview-github-styles`, mas a pasta
`~/.vscode/extensions` tem `windows-ai-studio-1.4.2` e há perfis (`49ff4a83`,
`builtin`) com associações por workspace. **O VSCode usa perfis** — instalar uma
extensão pela CLI cai no perfil default, possivelmente NÃO o que o dono usa. Por
isso NÃO forcei a instalação do Continue.dev; preparei a config e as instruções.

Pré-condições OK: **VSCode 1.123** (>1.113, caminho Copilot Chat+Ollama disponível),
**Ollama 0.30** (>0.18.3).

## C1 — latência de autocomplete (FIM) — MEDIDO

`fim_latency.py` envia o que o Continue.dev manda (fill-in-the-middle via
`/api/generate` com `suffix`), qwen2.5-coder:7b residente, n=12:

| Métrica | p50 | p90 | nota |
|---|---|---|---|
| **TTFT (prefill)** | **68 ms** | 199 ms | tempo até a sugestão começar |
| total (~20 tok) | 1431 ms | 2205 ms | sugestão completa (streama) |

**GATE-4 C1: PASSA** (TTFT p50<500, p90<800ms). A sugestão **começa** em 68ms — o
autocomplete local é responsivo; o corpo streama. (O total de ~1,4s p/ 20 tokens é
maior que os 55 t/s do B1 prediriam — há overhead de prefill do suffix + sync por
request no caminho FIM; não afeta o TTFT, que é o que pesa na percepção.)

## C2 — overhead da integração do editor — ENTREGUE (precisa da extensão)

Medir `t_render − t_enter` (atraso que a extensão adiciona sobre a latência
model-side de C1) exige a extensão instalada + instrumentação de eventos do editor.
**Não mensurável sem uso real.** Caminho: instalar Continue.dev no perfil ativo,
aplicar `continue-config-sugerida.yaml`, usar e comparar a percepção contra os 68ms
de C1.

## C3 — Copilot Chat + Ollama — ENTREGUE (setup GUI)

VSCode 1.123 + Ollama 0.30 suportam. Setup (≈5 min, GUI): Copilot Chat → engrenagem
→ "Manage Models"/"Add Models" → Ollama → endpoint `http://localhost:11434`. Baseline
de comparação a custo zero = **GPT-4.1** (multiplier-0), **NÃO Sonnet** (que é 1×
multiplier = consome quota). Fricção e taxa de sucesso = dados de uso.

## Como o dono fecha C2/C3 (hand-off)

1. No VSCode (perfil que você usa): instalar **Continue** (`Continue.continue`).
2. Copiar `continue-config-sugerida.yaml` → `~/.continue/config.yaml`.
3. Usar autocomplete local por alguns dias; registrar: parece fluido? quantas vezes
   escalou para cloud? (taxa de aceitação — a célula "não-sabível, só medindo" P17/P25).
4. (Opcional) Habilitar Copilot Chat + Ollama e comparar chat local vs GPT-4.1.

## GATE-4: status
- [x] C1 — TTFT autocomplete local 68ms p50 (<500ms). Responsivo.
- [~] C2 — preparado (config + caminho); precisa de uso real p/ medir overhead.
- [~] C3 — preparado (pré-condições OK + passos); precisa de setup GUI + uso.

**Parte objetiva do Estágio 4 concluída.** O resto é dado de uso, entregue ao dono.
A stack local recomendada (Estágios 2-4) está pronta para ser exercitada.
