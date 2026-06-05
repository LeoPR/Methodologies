---
title: Resultado — Ciclo 2 (Foundry Local, Ollama cloud/HF, Claude Code + Copilot)
created: 2026-06-04
status: open
---

# Resultado — Ciclo 2

> Lab sujo. Hipóteses confrontadas com documentação oficial.
> Decisões pendentes com o dono.

---

## H7 — Foundry Local é a alternativa Microsoft ao Ollama

**Veredito: CONFIRMADA, com diferenças importantes.**
**Fonte**: Microsoft Learn (oficial, jun/2026).

Foundry Local é uma runtime de inferência local embarcada, não um servidor
standalone como o Ollama. Runtime: ONNX (não GGUF). Usa CUDA automaticamente
na RTX 3060 — nenhuma configuração manual.

| Dimensão | Foundry Local | Ollama |
|---|---|---|
| Formato de modelo | ONNX (catálogo curado ~20–30 modelos) | GGUF (milhares na comunidade) |
| Integração Copilot | Nativa — aparece direto no picker do Chat | Via extensão ou config manual |
| GPU RTX 3060 | CUDA auto-detectado | CUDA |
| Custo | **Grátis, sem conta** | Grátis |
| Modelos disponíveis | Phi-4, Qwen 2.5, DeepSeek destilado, Mistral | Tudo que tem GGUF |
| Uso principal | Embarcado em apps + VSCode integrado | Servidor local universal |

**O que é cada item da screenshot**:
- **Foundry Local via Foundry Toolkit**: modelos ONNX rodando na GPU local
- **GitHub Models via Foundry Toolkit**: catálogo cloud do GitHub (free com limite,
  pay-as-you-go depois de jun/2025) — bom para prototipagem sem API key
- **Microsoft Foundry via Foundry Toolkit**: Azure AI Foundry (requer conta Azure;
  free trial $200/30 dias, mas inferência é pay-per-token)

**Nota de rebrand**: "AI Toolkit for VS Code" = "Foundry Toolkit for VS Code"
(renomeado em abril/2026 no GA). A extensão já instalada é a mesma.

**Não são mutuamente exclusivos**: Foundry Toolkit suporta Ollama como fonte
de modelos ao lado do Foundry Local.

---

## H8 — Ollama cloud models e HuggingFace

**Veredito: CONFIRMADA parcialmente — mais nuanced do que a hipótese.**
**Fonte**: docs.ollama.com e blog oficial Ollama.

### HuggingFace integration (`ollama run hf.co/...`)

Oficial desde outubro/2024. Funciona com qualquer modelo **GGUF** no Hub:

```bash
ollama run hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:Q4_K_M
ollama run hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:Q8_0
```

- **Safetensors NÃO funciona** pelo shorthand `hf.co/` — precisa converter para
  GGUF via llama.cpp (`convert_hf_to_gguf.py`)
- ~45.000 checkpoints GGUF públicos no Hub (bartowski, MaziyarPanahi etc.)
- Chat template auto-detectado dos metadados do arquivo GGUF

### Cloud models do Ollama (v0.12.0, set/2025)

**NÃO é proxy para OpenAI/Anthropic/Gemini** — é a própria infra do Ollama:

```bash
ollama signin
ollama run qwen3-coder:480b-cloud    # 480B parâmetros na cloud do Ollama
ollama run gpt-oss:120b-cloud        # "gpt-oss" = modelo open-source da OpenAI
ollama run deepseek-v3.1:671b-cloud
```

O daemon local em `localhost:11434` roteia automaticamente para local ou cloud
pelo sufixo `:cloud` no nome do modelo. **Roteamento explícito por convenção
de nome**, não automático por VRAM.

Para roteamento multi-provider real (Ollama local + Claude API + OpenAI): usar
**LiteLLM Proxy** (ferramenta de terceiros, não nativo do Ollama).

---

## H9 — Claude Code + Copilot Pro: coexistência e colaboração

**Veredito: CONFIRMADA — e melhor do que esperávamos.**
**Fonte**: docs oficiais Anthropic, Ollama, GitHub.

### Não há conflito

Claude Code opera no terminal/sidebar (sem autocomplete inline). Copilot é
o autocomplete inline. As duas ferramentas não compartilham nenhum recurso de
UI. Workflow complementar recomendado: Copilot para sugestões momento-a-momento,
Claude Code para tarefas autônomas multi-arquivo.

### Claude Code → Ollama local (sem MCP, sem proxy)

Desde Ollama v0.14.0 (jan/2026), Ollama expõe a Anthropic Messages API:

```bash
export ANTHROPIC_BASE_URL=http://localhost:11434
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
```

Claude Code passa a falar com Ollama local. Modelos recomendados pelo Ollama:
`qwen3-coder`, `qwen3.5`, `glm-4.7-flash`.

**Mapeamento de alias**:
```bash
export ANTHROPIC_DEFAULT_SONNET_MODEL=qwen3-coder
export ANTHROPIC_DEFAULT_HAIKU_MODEL=gemma3:4b
```

**Requisito de contexto** — ponto de falha mais comum:

| Janela | Viabilidade |
|---|---|
| 8k–16k | Só chat; Claude Code falha em tarefas agênticas |
| 32k | Mínimo para edição multi-arquivo |
| 64k | Sweet spot recomendado |

Se `ANTHROPIC_BASE_URL` está definido mas o servidor não responde corretamente,
**Claude Code falha sem fallback para cloud**.

### Subagent routing no Claude Code

```bash
export CLAUDE_CODE_SUBAGENT_MODEL=haiku
# Main session: Sonnet (api.anthropic.com)
# Subtarefas spawned: Haiku (mais barato)
```

Alias enum restrito: `["sonnet", "opus", "haiku"]`. IDs de modelo customizados
em subagentes não suportados ainda (feature request #34821, aberto mar/2026).

### Copilot Pro inclui Claude Sonnet 4.6 no Chat (zero custo por token)

Para **tarefas de chat** (explicar código, revisar, perguntas pontuais), usar
Copilot Chat com Claude Sonnet 4.6 selecionado = qualidade Sonnet sem consumir
créditos Anthropic. O GitHub absorve o custo via acordo enterprise.

### BYOK no Copilot Chat: apenas Business/Enterprise

Copilot Pro **não tem** BYOK no VSCode Chat (GA abr/2026). Disponível apenas
para Business ($19/usuário) e Enterprise ($39/usuário). O usuário atual (Pro)
não tem acesso a essa feature no VSCode Chat.

---

## H10 — Raptor mini: qualidade real

**Parcialmente respondida** — o agente encontrou que é um modelo do próprio
GitHub (fine-tuned), custo igual ao GPT-5 mini (25 créditos/MTok in). Qualidade
específica para código não benchmarkada em fonte primária nesta rodada.
Permanece como hipótese aberta para teste empírico.

---

## Stack otimizado emergente (ainda hipótese, não decisão)

Baseado em tudo que foi encontrado, este seria o mapa do ambiente:

```
CAMADA 0 — Sempre disponível, sem custo extra
├── Copilot Pro ($10/mês)
│   ├── Autocomplete inline: ilimitado (GPT-4.1 / GPT-5 mini)
│   └── Chat: Claude Sonnet 4.6 incluído (zero por token)
│
CAMADA 1 — Local com GPU, sem custo por token
├── Ollama (já instalado, já rodando)
│   ├── qwen2.5-coder:7b → Continue.dev autocomplete (a instalar)
│   ├── hf.co/... → qualquer modelo GGUF do HuggingFace
│   └── qwen3-coder:480b-cloud → modelos grandes na cloud Ollama (requer signin)
│
├── Foundry Local (já na extensão, confirmar se usa GPU)
│   └── Phi-4, Qwen 2.5 ONNX → otimizados para Windows/CUDA
│
CAMADA 2 — Claude Code (já instalado)
├── Default: api.anthropic.com (pay-per-token)
│   └── Subagents: CLAUDE_CODE_SUBAGENT_MODEL=haiku (mais barato)
│
└── Alternativa local: ANTHROPIC_BASE_URL=http://localhost:11434
    └── Requer modelo com 32k+ contexto no Ollama
```

---

## Experimentos de custo zero — sequência recomendada

Em ordem de menor para maior fricção:

1. **AgentsRoom** — baseline de custo atual (instalar, observar 2–3 dias, não
   mudar nada). Mostra qual modelo o Copilot Auto está escolhendo.

2. **Foundry Local** — verificar se já tem modelos baixados (a extensão já
   está instalada). Tentar um modelo Phi-4 ou Qwen2.5 local no Copilot Chat.

3. **Continue.dev + qwen2.5-coder:7b** — `ollama pull qwen2.5-coder:7b` (4.8GB),
   instalar Continue.dev, 10 minutos de config. Usar por 1 semana.

4. **Copilot Chat + Ollama** — VSCode ≥1.113 + Ollama ≥0.18.3 (verificar
   versão atual). Habilitar chat privado local.

5. **Claude Code → Ollama local** — `export ANTHROPIC_BASE_URL=http://localhost:11434`.
   Testar com tarefa de leitura de arquivo. Requer modelo com 32k+ no Ollama.

6. **Ollama cloud** — `ollama signin` + `ollama run qwen3-coder:480b-cloud`.
   Acesso a modelo 480B sem hardware. Custo: Ollama cobra por token na cloud,
   mas há free tier (verificar).

---

## Fontes primárias ciclo 2

- [What is Foundry Local — Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry-local/what-is-foundry-local) `[Oficial]`
- [Foundry Toolkit for VS Code — VSCode docs](https://code.visualstudio.com/docs/intelligentapps/overview) `[Oficial]`
- [Foundry Toolkit GA — Microsoft Tech Community](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/microsoft-foundry-toolkit-for-vs-code-is-now-generally-available/4511831) `[Oficial]`
- [GitHub Models billing — GitHub Docs](https://docs.github.com/billing/managing-billing-for-your-products/about-billing-for-github-models) `[Oficial]`
- [Ollama blog: Cloud models (set/2025)](https://ollama.com/blog/cloud-models) `[Oficial]`
- [Ollama docs: Cloud](https://docs.ollama.com/cloud) `[Oficial]`
- [Ollama docs: Anthropic compatibility](https://docs.ollama.com/api/anthropic-compatibility) `[Oficial]`
- [Ollama blog: Claude Code (jan/2026)](https://ollama.com/blog/claude) `[Oficial]`
- [HuggingFace Hub: Ollama docs](https://huggingface.co/docs/hub/en/ollama) `[Oficial]`
- [Claude Code model config](https://code.claude.com/docs/en/model-config) `[Oficial]`
- [BYOK GA changelog (abr/2026)](https://github.blog/changelog/2026-04-22-bring-your-own-language-model-key-in-vs-code-now-available/) `[Oficial]`
- [Copilot plans — GitHub Docs](https://docs.github.com/en/copilot/get-started/plans) `[Oficial]`
