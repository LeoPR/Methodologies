---
title: P6 #2 — grid de valor (não-Opus forte) + grátis (remoto/local) + eixo think
created: 2026-06-08
setup: forma F1-checklist × {value-tier pago, free remoto, free/local Ollama} × NNN+pdf2md · pontuação CEGA (gabarito corrigido) · qualidade = genuíno − falso-positivo · MERGE com Phase B no gen_delivery.py
status: define a fronteira de USO; o grátis-LOCAL (deepseek-r1:8b) é a surpresa positiva — só visível após corrigir a captura de thinking
---

# P6 #2 — preencher a entrega (value / grátis / local / think)

Objetivo (do dono): para fechar a conclusão de USO, ver quanto cada opção **acessível**
atende — sem re-rodar Opus (já é a prova de teto). Mostrar o que funciona; o resto vira nota.

## Resultado (qualidade média, gabarito corrigido)

| config | ambiente | $/M | qualidade | faixa |
|---|---|---|---|---|
| claude-opus-4.8 (ref) | pago | 7.00 | **+1.75** | [+1,+2] |
| deepseek-v3 +etapas | pago | 0.26 | **+0.50** | [0,+1] |
| glm-4.6 | pago | 0.56 | **+0.50** | [−1,+2] |
| **deepseek-r1:8b** | **local 🖥️** | **0** | **+0.50** | [0,+1] |
| o4-mini | pago | 1.43 | +0.25 | [−1,+1] |
| gpt-5 | pago | 2.12 | +0.25 | [0,+1] |
| gpt-4.1-mini | pago | 0.52 | 0.00 | [0,0] |
| qwen3:4b-thinking | local 🖥️ | 0 | 0.00 | [0,0] |
| gemini-2.5-pro | pago | 2.12 | −0.25 | [−3,+2] |
| kimi-k2 | pago | 0.74 | −2.25 | [−5,−1] |
| glm-4.5-air:free | grátis ☁️ | 0 | −2.25 | [−4,+1] |
| llama3.1:8b (local) | local 🖥️ | 0 | −4.00 | [−4,−4] |

## Achados

1. **O grátis-LOCAL funciona — deepseek-r1:8b (+0.50).** É o melhor do ambiente "na minha
   máquina, de graça", empatado com as opções pagas baratas. **Só apareceu depois de corrigir
   um erro meu** (ver abaixo). qwen3:4b-thinking fica neutro (0.0). Os locais não-reasoner
   (qwen3:8b −1.5, llama3.1:8b −4.0) são fracos.
2. **Não há vantagem em pagar caro acima do barato-que-funciona.** gemini-2.5-pro ($2.12) deu
   −0.25 e gpt-5 ($2.12) +0.25 — **piores ou iguais** ao glm-4.6 ($0.56) e ao deepseek-v3+etapas
   ($0.26). Acima do tier barato-bom, só o Opus compra qualidade real. A curva custo→qualidade
   **não é monotônica**.
3. **Grátis REMOTO não entregou:** glm-4.5-air:free −2.25; gpt-oss-120b:free e qwen3-next-80b:free
   morreram em **429 (rate-limit)** — inutilizáveis para esta tarefa em volume. O grátis útil é
   o **local**.
4. **Eixo think (parcial):** deepseek-r1:8b (think, local) +0.50 vs llama3.1:8b (no-think, local)
   −4.0 — think ajudou MUITO no local. No pago, deepseek-v3 (no-think) −2.25 vs deepseek-r1
   (think) −1.0; gpt-4.1-mini (no-think) 0.0 vs o4-mini (think) +0.25 — think ajuda de leve.
   **Conclusão:** raciocínio ajuda, e é decisivo justamente nos modelos pequenos/locais.

## O erro metodológico corrigido (registro honesto)

Na 1ª rodada, conclui que deepseek-r1:8b/qwen3-thinking eram "incapazes" (saída vazia). **Erro
clássico:** o Ollama retorna o raciocínio em `message.thinking` e a resposta em
`message.content` (campos **separados**); meu runner lia só `content`. Em prompt grande o
reasoner despejava tudo em `thinking` (às vezes com `done_reason=length`) e eu **descartava o
trabalho do modelo**. Corrigido (`think:true` + fallback p/ thinking; diag empírico +
docs confirmam). Re-rodado → deepseek-r1:8b virou a melhor opção local. **Apontado pelo dono.**
Limite real associado: o reasoner local é **lento** e pode **não terminar** (truncar) projetos
grandes — precisa de orçamento de tokens alto.

## Entrega (separada)
O guia de USO positivo-only (tabela de decisão + fronteira) está em
[`recipe/strata-com-ia.md`](../../recipe/strata-com-ia.md). Este arquivo é o registro de
pesquisa (tem tudo, inclusive o que não funciona).

## Caveats
- N=2 (pago) / N=1 (local); 2 projetos. Local truncou no NNN (score sobre o trace parcial).
- Custo = proxy $/M. Qualidade pelo juiz Claude cego (consistente com os 2º juízes anteriores).
