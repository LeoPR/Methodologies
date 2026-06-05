---
title: Observações diretas do ambiente (evidência primária)
created: 2026-06-04
source: screenshot Language Models panel + curl localhost:11434
---

# Observações diretas do ambiente

> Evidência de primeira mão — não inferida, não da web. Data: 2026-06-04.

## Fatos confirmados por observação direta

### 1. Ollama está rodando e conectado ao VSCode

```
curl http://localhost:11434 → "Ollama is running"
```

Modelos Ollama visíveis no painel Language Models do VSCode Copilot:
- deepseek-r1:14b, deepseek-r1:7b, deepseek-r1:8b
- gemma2:9b, gemma3:12b, gemma3:1b
- (lista parcial — scroll incompleto)

### 2. Custo real visível (Credits per 1M Tokens) — plano Copilot Pro

O painel exibe o custo em créditos (1 crédito = $0.01 USD):

| Modelo | In (credits/MTok) | Out (credits/MTok) | Cache |
|---|---|---|---|
| **GPT-5 mini** | **25** | **200** | 2 |
| **Raptor mini** (Preview) | **25** | **200** | 2 |
| GPT-5.4 mini | 75 | 450 | 7 |
| Claude Haiku 4.5 | 100 | 500 | 10 |
| Gemini 3 Flash (Preview) | 50 | 300 | 5 |
| Gemini 3.5 Flash | 150 | 900 | 15 |
| Claude Sonnet 4.5 | 300 | 1.500 | 30 |
| Claude Sonnet 4.6 | 300 | 1.500 | 30 |
| Gemini 2.5 Pro | 125 | 1.000 | 12 |
| Gemini 3.1 Pro (Preview) | 200 | 1.200 | 20 |
| GPT-5.2 ⚠️ | 175 | 1.400 | 17 |
| GPT-5.2-Codex | 175 | 1.400 | 17 |
| GPT-5.3-Codex | 175 | 1.400 | 17 |
| GPT-5.4 | 250 | 1.500 | 25 |

**Observação**: GPT-4.1 (multiplier-0 do ciclo anterior) NÃO aparece na lista
de custos — consistente com ser "incluído" (não cobra créditos). A lista
mostra apenas modelos que cobram.

Em dólares reais:
- GPT-5 mini / Raptor mini: $0.25/MTok in, $2.00/MTok out — mais baratos da lista
- Claude Sonnet 4.x: $3.00/MTok in, $15.00/MTok out — confirmado com preço Anthropic
- Gemini 3 Flash: $0.50/MTok in, $3.00/MTok out

### 3. Três provedores "Foundry" também visíveis

- **Foundry Local via Foundry Toolkit** — parece ser inferência local via Microsoft
- **GitHub Models via Foundry Toolkit** — catálogo de modelos do GitHub
- **Microsoft Foundry via Foundry Toolkit** — Azure-side models

Todos colapsados no screenshot — não foi possível ver modelos ou custos internos.

### 4. Auto mode ativo → desconto de 10% no multiplier

Confirmado pelo usuário (Copilot Pro). Quando "Auto" está ativo, o Copilot
escolhe o modelo por si e aplica coeficiente 0.9 sobre o custo.

### 5. Claude Code e Copilot Pro coexistem no mesmo ambiente

O usuário tem ambos ativos. Não está claro como fazer os dois colaborarem —
é uma hipótese aberta (H7 abaixo).

## O que ainda não sabemos (abre H7, H8, H9)

- O que exatamente é "Foundry Local" e se usa a GPU local
- O que é a integração Ollama → Hugging Face (mencionada na doc recente do Ollama)
- Como fazer Claude Code usar Ollama local como backend de subtarefas
  (OllamaClaude MCP existe, mas não foi testado ainda)
- O warning ⚠️ no GPT-5.2 — o que significa nesse contexto
