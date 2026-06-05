---
title: Hipóteses — Ciclo 2 (ambiente, experimentos, visão de produto)
created: 2026-06-04
status: open
---

# Hipóteses — Ciclo 2

> Lab sujo. Nenhuma decisão tomada. Bolo de hipóteses para confrontar
> com evidência antes de propor qualquer experimento ou produto.

---

## Bloco 1 — O ambiente que já existe (observações da tela)

### H7 — Foundry Local é a alternativa Microsoft ao Ollama, sem custo por token

O painel de Language Models mostra "Foundry Local via Foundry Toolkit" junto com
Ollama. Hipótese: é uma camada de inferência local da Microsoft, possivelmente
com melhor integração com Copilot do que o Ollama externo.

**O que queremos saber**: é de fato local (usa GPU)? É gratuito? Quais modelos
suporta? É superior/inferior ao Ollama para RTX 3060?

### H8 — Ollama agora roteia para cloud (HuggingFace + APIs externas)

Documentação recente do Ollama menciona integração com Hugging Face e modelos
de nuvem. Hipótese: Ollama pode agir como roteador transparente — local para
modelos que cabem na VRAM, cloud para os que não cabem — via mesma API.

**O que queremos saber**: é roteamento automático ou manual? Quais clouds?
Tem custo adicional ou é só um proxy?

### H9 — Claude Code e Copilot Pro podem colaborar sem conflito

Ambos estão ativos no mesmo VSCode. Hipótese: dá para usar Copilot Pro para
autocomplete (ilimitado, GPT-4.1 free) + Claude Code para tarefas complexas
(API Anthropic) + Ollama via Copilot Chat para chat privado — três camadas sem
conflito técnico.

**O que queremos saber**: há conflito de keybindings/sugestões? Claude Code
pode usar Ollama local como backend? Copilot Chat BYOK pode apontar para
Claude API diretamente?

### H10 — GPT-5 mini + Raptor mini são os modelos mais baratos "úteis" do Copilot

Screenshot mostra ambos em 25 créditos/MTok input (= $0.25/MTok) — os mais
baratos da lista, mais baratos que Gemini Flash ($0.50/MTok).

**O que queremos saber**: qual a qualidade real de Raptor mini para código?
É um modelo próprio do GitHub ou rebrand? Vale mais que GPT-4.1 (free)?

---

## Bloco 2 — Experimentos de custo zero (o que dá pra testar já)

### H11 — Continue.dev + qwen2.5-coder:7b já instalado no Ollama

Ollama está rodando com modelos carregados (deepseek-r1, gemma3). Hipótese:
instalar Continue.dev + `ollama pull qwen2.5-coder:7b` → autocomplete local
funcional em 15 minutos, zero custo adicional.

**Experimento**: instalar, usar por N dias, observar satisfação subjetiva e
quantas vezes o dev escalou para cloud. Custo: $0.

### H12 — Ativar Copilot Chat + Ollama para chat privado

VSCode ≥1.113 + Ollama 0.18.3 = integração oficial. Hipótese: habilitar isso
cria uma sessão de chat local sem consumir créditos, útil para perguntas sobre
código privado/sensível.

**Experimento**: ativar, testar com arquivo real, medir latência percebida vs
Sonnet/GPT. Custo: $0.

### H13 — Modo Auto do Copilot economiza na prática

Usuário tem Auto ativo (10% desconto). Hipótese: para uso misto (código simples
+ perguntas complexas), Auto escolhe modelos baratos para as simples e Sonnet
só para as complexas.

**Experimento**: instalar AgentsRoom ou cc-statistics para ver qual modelo o
Auto escolheu por sessão. Custo: $0.

### H14 — OllamaClaude MCP reduz tokens de leitura de arquivo no Claude Code

Claude Code lê arquivos via API (cada Read = tokens). Se o MCP server
redirecionar leituras de arquivo para Ollama local, o Claude principal
recebe o sumário e não o arquivo inteiro.

**Experimento**: instalar OllamaClaude, testar com tarefa de leitura de
múltiplos arquivos, medir tokens antes/depois com AgentsRoom. Custo: $0
(não aumenta chamadas Anthropic se o MCP funcionar como esperado).

---

## Bloco 3 — Visão de produto (o que pode nascer daqui)

### H15 — O resultado deste lab pode virar um "recipe" autônomo

A missão não é criar métricas para o knowledge-architecture.md. É criar
**um documento operacional separado** que diz:

> "Para configurar um ambiente de desenvolvimento IA-assistido eficiente,
> faça X, Y, Z. Aqui está como verificar que funcionou."

Esse documento seria um **recipe** novo, paralelo ao knowledge-architecture.md:
- `recipe/ai-dev-environment.md` (ou nome melhor)
- Descreve como montar a pilha: Ollama + Continue.dev + Copilot + Claude Code
- Inclui tabela de decisão: qual ferramenta para qual tarefa
- Inclui como verificar/medir se está funcionando
- É **acionável** (não teórico) — uma receita, não uma metodologia

### H16 — O recipe de ambiente pode ser o primeiro teste de vendoring do Strata

O Strata tem `prototype/` vazio esperando o primeiro experimento de vendoring.
Hipótese: criar `recipe/ai-dev-environment.md` usando o próprio
knowledge-architecture.md como metodologia base (§5 fonte única, §9 economia,
§6-bis fail-closed para decisões de agente) seria o primeiro teste empírico
real de que o Strata funciona fora de si mesmo.

Isso fecha o loop: o método ajuda a criar o próximo recipe; o recipe testa o método.

---

## Experimentos ordenados por custo

### Zero custo (fazer primeiro)

1. `cc-statistics` ou `AgentsRoom` — baseline de uso atual (instalar, observar
   por 2–3 dias sem mudar nada)
2. Continue.dev + `qwen2.5-coder:7b` — autocomplete local (pull do modelo,
   config YAML, usar por 1 semana)
3. Copilot Chat + Ollama — chat privado local (ativar integração, testar
   com arquivo real)
4. Verificar Foundry Local — ver o que é, se usa GPU local, se modelos são úteis

### Custo baixo (pequenos testes se os de cima confirmarem valor)

5. OllamaClaude MCP — verificar redução de tokens em tarefa específica
   (custo: o que já se gastaria em tokens de Read, potencialmente zero)
6. Usar Gemini 3 Flash via Copilot para tarefas de chat médio — $0.50/MTok
   in, capaz de substituir Sonnet em alguns casos

### Custo zero para o produto final

7. Escrever `recipe/ai-dev-environment.md` baseado nos resultados dos
   experimentos acima — o documento que viaja para outros projetos

---

## O que este ciclo NÃO vai decidir

- Qual recipe específico criar (ainda em hipótese H15/H16)
- Se o Strata precisa mudar para acomodar o novo recipe
- Fine-tuning ou treinamento de modelos
- Infra de produção, multi-GPU, Kubernetes
