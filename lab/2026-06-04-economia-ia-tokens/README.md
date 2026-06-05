---
title: Economia de IA — tokens, hardware local e fornecedores
status: open
created: 2026-06-04
updated: 2026-06-04
tags: [economia-tokens, local-llm, ollama, copilot, rtx3060, vscode, hardware, fornecedores, rag, prompt-compression]
phase: lab-sujo (coleta concluída — hipóteses confrontadas — decisões pendentes com dono)
---

# Economia de IA — tokens, hardware local e fornecedores

> **Fase de lab sujo**: hipóteses confrontadas com literatura e documentação
> oficial. Nenhuma metodologia nova foi decidida. Nada aqui toca o
> knowledge-architecture.md enquanto não houver evidência suficiente e
> decisão explícita do dono.

## Documentos deste lab (ordem de leitura)

1. [`README.md`](README.md) — este: contexto, hipóteses iniciais, resultado ciclo 1
2. [`observacoes-ambiente.md`](observacoes-ambiente.md) — evidência primária (tela + curl) do ambiente real
3. [`hipoteses-ciclo2.md`](hipoteses-ciclo2.md) — bolo de 16 hipóteses (H1–H16) em 3 blocos
4. [`resultado-ciclo2.md`](resultado-ciclo2.md) — Foundry Local, Ollama HF/cloud, Claude Code + Copilot
5. [`mapa-recursos-llm.md`](mapa-recursos-llm.md) — **o MAPA**: primitivas, métrica de esforço, grade sempre-ótimo/depende/não-sabível, caminho feliz, chutes
6. [`plano-experimental.md`](plano-experimental.md) — **as SONDAS**: plano de ablação faseado (6 estágios, gates, custo zero até a Fase 2)

> **Mapa × Sondas**: o mapa (5) classifica o terreno por certeza; o plano (6)
> testa as células incertas. Dois workflows independentes (38 + 26 agentes)
> convergiram nas mesmas sondas E ambos pegaram a mesma mentira de custo
> ("Sonnet grátis no Copilot" = falso, é 1× multiplier). A recipe final destila
> o caminho feliz + os vereditos dos experimentos. **Nada executado ainda.**

## Contexto e pergunta

Ciclo 2 da pesquisa de metodologias modernas para IA. O ciclo 1 (task wv98wzzb8,
`lab/2026-06-04-aderencia-portabilidade/`) respondeu grau de aderência do Strata.
Este ciclo foca em **economia prática de uso de IA**: como reduzir custo de tokens
e tempo de conversa combinando fornecedores, planos, hardware local e ferramentas
de ecossistema, sem degradar qualidade.

**Hardware de referência**: NVIDIA RTX 3060 12 GB VRAM (Ampere, sm_86).

## Método

3 agentes de pesquisa paralelos (totalizando ~96k tokens, ~12 min):
- Agente A: planos GitHub Copilot e modelos com multiplier 0
- Agente B: benchmarks RTX 3060 + integração Ollama/VSCode
- Agente C: compressão de contexto, métricas de tokens, frameworks de decisão local/cloud

Fontes classificadas: `[Oficial]` = docs/blog oficial do fornecedor ou paper
peer-reviewed; `[Blog]` = análise de terceiros; `[Comunidade]` = benchmark ou
guia da comunidade.

## Hipóteses × resultado

| Hipótese | Veredito | Confiança |
|---|---|---|
| H1 — Copilot tem modelos "multiplier 0" | **Confirmada, mas a descoberta mais importante é outra** | Alta |
| H2 — RTX 3060 roda modelos úteis sem custo por token | **Confirmada** com números concretos | Alta |
| H3 — Ollama + VSCode pipeline sem fricção | **Confirmada** — integração oficial existe | Alta |
| H4 — Métricas de economia instrumentáveis | **Confirmada** para Claude Code; lacunas em Continue.dev | Alta |
| H5 — Compressão local reduz tokens cloud | **Confirmada academicamente** (LLMLingua, MCCom) | Média-alta |
| H6 — Framework de decisão local/cloud existe | **Confirmada** — MCCom, SolidGPT, HybridFlow publicados | Alta |

---

## Resultado A — GitHub Copilot: planos e modelos

**Fontes**: [GitHub Docs/Blog](https://docs.github.com/en/copilot) `[Oficial]`,
tabelas de multiplier trianguladas de 3 blogs independentes `[Blog]`.

### Planos atuais (jun/2026)

| Plano | Custo/mês | Requests incluídos |
|---|---|---|
| Free | $0 | 50 premium requests + 2.000 completions |
| Pro | $10 | 300 premium requests |
| Pro+ | $39 | 1.500 premium requests |
| Max | $100 | Maior cota individual |
| Business | $19/usuário | 300/usuário |
| Enterprise | $39/usuário | 1.000/usuário |

*Nota: novos sign-ups do Pro/Pro+/Student pausados em mai/2026 por sobrecarga de
agentic workflows. Assinantes existentes não afetados.*

### O dado mais importante — completions são ilimitadas

**Completions inline (autocomplete) são ILIMITADAS em todos os planos pagos**,
sem consumir quota. Só chat, agent mode e code review consomem premium requests.
O "poço artesiano" real do Copilot é o autocomplete, não o chat.

### Modelos multiplier 0 (zero custo, incluídos no plano)

| Modelo | Status |
|---|---|
| **GPT-4.1** (default desde mai/2025) | Incluído em todos os planos pagos |
| **GPT-4o** | Incluído, em processo de deprecação |
| **GPT-5 mini** | Incluído |

### Tabela de multiplier por modelo

| Multiplier | Modelos |
|---|---|
| 0x (grátis) | GPT-4.1, GPT-5 mini |
| 0.33x | Claude Haiku 4.5, Gemini 3 Flash |
| 1x | Claude Sonnet 4/4.5/4.6, Gemini 2.5 Pro, GPT-5.x |
| 3x | Claude Opus 4.5/4.6 |
| 7.5x–10x | Claude Opus 4.7+ |
| 13x | Copilot Code Review (por PR) |

*Enable "Auto" → desconto de 10% nos multipliers premium.*

### Capacidade prática por plano (para dev solo)

| Plano | Claude Sonnet/dia | Claude Opus/mês | Melhor uso |
|---|---|---|---|
| Pro ($10) | ~15 interações | ~100 | Completions ilimitadas + chat moderado |
| Pro+ ($39) | ~100 interações | ~500 | Heavy chat + agent mode |
| Max ($100) | Maior cota | Alto | Sem limites práticos |

**Conclusão**: Copilot Pro ($10/mês) cobre completions ilimitadas (GPT-4.1) +
chat razoável. Claude Sonnet não é grátis (1x multiplier), mas para 10–15
interações/dia é coberto pelo Pro. Não existe plano verdadeiramente ilimitado
para uso interativo.

---

## Resultado B — RTX 3060 12 GB: o que cabe e como roda

**Fontes**: paper oficial Qwen2.5-Coder `[Oficial arxiv]`, benchmarks
hardware-corner.net e singhajit.com `[Comunidade]`, docs Continue.dev e
Ollama `[Oficial]`.

### O que cabe em 12 GB de VRAM

Regra prática Ollama: deixar 2–3 GB de headroom para KV cache + runtime (~500 MB).
Janela usável para pesos: ~9–10 GB.

| Tamanho | Quantização | VRAM (pesos) | Cabe? |
|---|---|---|---|
| 7B / 8B | Q4_K_M | ~4,5–5 GB | Sim, confortável |
| 7B / 8B | Q8_0 | ~8 GB | Sim |
| 13B / 14B | Q4_K_M | ~7,5–8,7 GB | Sim, KV cache apertado |
| 14B | Q5_K_M | ~9,5–10 GB | Marginal |
| 32B+ | Q4_K_M | ~20 GB | Não |

**Phi-4 (14.7B) Q5_K_M: NÃO cabe na prática** — ~12 GB só para os pesos,
zero espaço para KV cache. Usar Q4_K_M (~9 GB) com contexto curto.

### Benchmarks de velocidade (RTX 3060 12 GB)

| Modelo | Quantização | Contexto | Tokens/seg |
|---|---|---|---|
| Qwen3 8B | Q4_K | 4k | **55 t/s** |
| Qwen3 8B | Q4_K | 16k | 42 t/s |
| Qwen3 14B | Q4_K | 4k | 31 t/s |
| Llama 2 7B | Q4_K_M | — | 60 t/s |
| DeepSeek-R1-Distill 14B | Q4_K_M | — | 29 t/s |

Acima de ~20 t/s: chat interativo fluido. Acima de ~40 t/s: autocomplete
responsivo. 7B @ RTX 3060 = ~50 t/s = adequado para ambos.

### Recomendação de modelos de código para RTX 3060

**Qwen2.5-Coder 7B** é o sweet spot confirmado:
- VRAM: ~4,8 GB (Q4_K_M) — espaço generoso para KV cache
- Velocidade: ~50 t/s
- HumanEval Instruct: **84.1%** (oficial, paper Alibaba) — conservador; alguns blogs
  reportam 88.4% (protocolo de avaliação diferente, use 84% como baseline)
- Cobre ~80% dos casos de uso de autocomplete segundo comunidade Continue.dev

**14B se precisar de mais qualidade**: `qwen2.5-coder:14b` Q4_K_M (~8.7 GB),
~30 t/s, mas limite o contexto a 4–8k para evitar OOM.

**Não usar**: CodeLlama (obsoleto; Qwen2.5-Coder 7B supera CodeLlama 70B em
HumanEval — 84% vs 67.8%). DeepSeek-Coder-V2 16B MoE não cabe (~24 GB).

### Gap de qualidade: 7B local vs GPT-4o

| Tarefa | Gap 7B local vs GPT-4o | Recomendação |
|---|---|---|
| Autocomplete (single-line/function) | Mínimo (~80% dos casos OK) | Local |
| Explicação de código (arquivo isolado) | Pequeno | Local |
| Geração de boilerplate | Pequeno | Local |
| Refatoração multi-arquivo | Relevante | Cloud |
| SWE-bench (issues reais no GitHub) | Grande (7B: <5%, GPT-4o: 41%) | Cloud |
| Debugging em base de código grande | Relevante | Cloud |

**Regra de bolso**: local para tarefa de arquivo único ou repetitiva; cloud
para raciocínio que cruza múltiplos arquivos ou requer contexto de projeto inteiro.

---

## Resultado C — Integração Ollama + VSCode

**Fontes**: docs.ollama.com `[Oficial]`, docs.continue.dev `[Oficial]`,
docs.codegpt.co `[Oficial]`, github.com/Jadael/OllamaClaude `[Comunidade]`.

### Extensões que suportam Ollama como backend

| Extensão | Suporte Ollama | Oficial? | Setup | Autocomplete local? |
|---|---|---|---|---|
| **Continue.dev** | Nativo, primeira classe | Sim (ambos os lados) | 5–10 min | Sim (modelo separado) |
| **GitHub Copilot Chat** | Integrado (VSCode 1.113+) | Sim (Ollama docs) | 5 min | Não (completions ficam remotas) |
| **CodeGPT** | Nativo | Sim | 3–5 min | Limitado |
| Cursor | Workaround OpenAI-compat | Não | 5–10 min | Não |

**Continue.dev é a melhor opção**: única que oferece tanto chat quanto
autocomplete inline via Ollama, com injeção de contexto flexível (`@file`,
`@codebase`, `@git`, `@terminal`).

**Configuração recomendada para RTX 3060** (Continue.dev `~/.continue/config.yaml`):
```yaml
models:
  - name: Qwen2.5-Coder 7B
    provider: ollama
    model: qwen2.5-coder:7b
    roles: [chat, edit]
  - name: Qwen2.5-Coder 1.5B
    provider: ollama
    model: qwen2.5-coder:1.5b
    roles: [autocomplete]
```

Falhas comuns:
- `404 model not found` → `ollama pull qwen2.5-coder:7b` com a tag exata
- OOM em 14B → reduzir `contextLength` para 2048–4096
- Porta 11434 bloqueada → verificar com `curl http://localhost:11434`

### Copilot Chat + Ollama (integração oficial)

Requer VSCode ≥1.113 + Copilot Chat ≥0.41.0 + Ollama ≥0.18.3.
Setup: Copilot Chat → engrenagem → Add Models → Ollama.
**Importante**: apenas o chat usa Ollama. As completions inline continuam
chamando os servidores do GitHub. Isso cobre o caso "chat privado / local +
completions ilimitadas do Copilot".

### OllamaClaude MCP — Claude Code + Ollama local

`github.com/Jadael/OllamaClaude` `[Comunidade]`

MCP server que expõe 11 ferramentas para Claude Code: geração de código,
explicação, revisão, refatoração, testes — processadas pelo Ollama local.
Claude Code age como orquestrador; Ollama executa o trabalho pesado.

Modelo default: `gemma3:12b`. Recomenda-se trocar para `qwen2.5-coder:7b`
na RTX 3060 (melhor relação qualidade/VRAM/velocidade).

O projeto reporta "até 98.75% de redução no uso da API Anthropic para tarefas
com muitos arquivos" — número é do autor, sem replicação independente; tratar
como claim plausível mas não verificado.

---

## Resultado D — Compressão de contexto e métricas

**Fontes**: papers peer-reviewed e docs oficiais Claude Code/Ollama.

### Compressão de contexto antes da chamada cloud

**LLMLingua** (Microsoft Research, EMNLP 2023, estendido 2024–2025) `[Oficial arxiv]`
- Um modelo local pequeno (7B ou menor) pontua cada token por perplexidade
- Tokens de baixa informação são descartados antes da chamada cloud
- Resultado: **até 20x compressão** com ~1.5 pp de perda de acurácia (GSM8K, BBH)
- Funciona com qualquer LLM cloud (caixa-preta)

**PROCONSUL** (EMNLP 2024 Industry Track) `[Oficial arxiv]`
- Extrai snippets relevantes e relações entre arquivos localmente
- Envia contexto comprimido e estruturado ao LLM cloud
- Resultado: melhora qualidade E reduz tokens (contexto estruturado supera
  contexto bruto completo)

**MCCom** (arXiv:2603.05974, 2026) `[Oficial arxiv]` — o mais relevante para o caso:
- Cascata: modelo local 121M parâmetros para autocomplete → cloud só se o
  usuário rejeitar/modificar a sugestão local
- Resultado: **47.9% redução de latência**, **46.3% redução no uso de cloud**,
  **8.9% melhora na taxa de acerto do LLM cloud**
- **Valida diretamente a hipótese**: local para autocomplete, cloud para complexo

**C2LLM** (arXiv:2512.21332) `[Oficial arxiv]`
- 7B model treinado para recuperação de código, 80.75 avg em MTEB-Code
- Viável como camada de retrieval antes de enviar ao GPT-4/Claude

### Métricas e instrumentação

**Claude Code** — melhor instrumentado de todos:
- Escreve JSONL completo em `~/.claude/projects/<projeto>/<sessao>.jsonl`
- Cada mensagem inclui `input_tokens`, `output_tokens`,
  `cache_creation_input_tokens`, `cache_read_input_tokens`
- Agent SDK: `result.total_cost_usd`, `result.modelUsage`, `result.usage`
- OTel: 8 métricas exportáveis incluindo custo estimado por sessão

**Continue.dev**: sem tracking de tokens por turno ainda (feature request
aberto, GitHub discussion #10567, PR em revisão)

**Ferramentas de terceiros**:
- **AgentsRoom**: medidor em tempo real por terminal, lê `~/.claude/projects/`
  a cada 10–15s; exibe input/output/cache por mensagem e taxa de cache hit
- **cc-statistics** (`uv tool install cc-statistics`): dashboard CLI + web;
  agrega Claude Code, Gemini CLI, Codex, Cursor; `cc-stats --all --since 7d`
- **Tokscale** (`github.com/junhoyeo/tokscale`): 25+ ferramentas; JSONL local
  para Claude Code/Codex, API autenticada para Cursor; sem visão comparativa
  local/cloud explícita

### Protocolo A/B teste local vs cloud

```
1. Baseline: Agent SDK result.total_cost_usd + result.usage por query(), 
   logar em JSONL com campos: {timestamp, session_id, condition, task_type, 
   input_tokens, output_tokens, cache_*, estimated_cost_usd, latency_ms, 
   model, endpoint}

2. Variante local: apontar client para http://localhost:11434/v1
   (Ollama retorna usage no mesmo formato OpenAI)
   Métricas proxy: latency_ms, tokens da resposta, cloud_calls=0

3. Comparar: total estimated_cost_usd e total tokens entre condições.
   Ollama não retorna custo monetário; usar tokens como proxy ou calcular
   custo equivalente com tabela de preços do fornecedor escolhido.
```

### Framework de decisão local/cloud (sintetizado da literatura)

| Tipo de tarefa | Tier recomendado | Base |
|---|---|---|
| Autocomplete (linha/função) | Local ≤7B (GPU obrigatório) | MCCom (46% redução cloud) |
| Edit de arquivo único, lint | Local ≤7B | SolidGPT (routing por complexidade) |
| Sumarização de arquivo isolado | Local ou compressão local → cloud | PROCONSUL |
| Retrieval em base de código grande | Local 7B (filtro) → cloud (geração) | C2LLM |
| Raciocínio multi-arquivo | Cloud | Mellum (JetBrains, produção) |
| Root cause analysis / debugging complexo | Cloud | SolidGPT (produção, 43 devs) |

**Restrição importante**: local para autocomplete requer GPU. CPU-only →
até modelo 4B pode ter latência >3s (Mellum, JetBrains, produção) — impraticável
para uso interativo.

### Protocolo Ollama OpenAI-compat

Ollama expõe `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings` e
`/v1/models` em `localhost:11434/v1`. Trocar de cloud para local = mudar `base_url`:

```python
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",  # local
    api_key="ollama",  # ignorado pelo Ollama
)
```

Lacunas vs OpenAI: sem log probs, sem `tool_choice`, sem streaming tool calls,
vision requer base64.

---

## Lição de método

O ciclo 1 de pesquisa desta sessão (task wv98wzzb8) falhou na verificação
adversarial por bug do harness (agentes não retornaram schema estruturado).
As 25 claims foram coletadas de fontes primárias reais mas ficaram como "0-0:
3 abstain". Tratadas como "fontes verificadas, adversarial não concluído" neste lab.

Este ciclo (3 agentes sem harness adversarial) produziu material mais rico e
com rastreabilidade por fonte. Cada claim está marcada com `[Oficial arxiv]`,
`[Oficial docs]`, `[Comunidade]` ou `[Blog]`. Claims de source única e
autor-próprio estão marcadas como não replicadas.

---

## Hipóteses abertas (não respondidas nesta rodada)

- **Custo energético real da RTX 3060 por sessão**: 170W TDP × horas de uso.
  Não há benchmark de custo elétrico por 1.000 tokens para Ampere/3060.
- **OllamaClaude MCP na prática**: o claim de 98.75% de redução de tokens é
  do autor, sem replicação. Merece experimento próprio em `prototype/`.
- **LLMLingua + código**: o paper valida em benchmarks de raciocínio (GSM8K, BBH),
  não especificamente para prompts de código. Transferência não garantida.
- **Continue.dev autocomplete quality gap**: benchmark informal da comunidade
  ("80% dos casos OK") sem protocolo controlado.

---

## Fontes primárias desta pesquisa

**Planos/Copilot**
- [GitHub Copilot Plans & Pricing](https://github.com/features/copilot/plans) `[Oficial]`
- [About Premium Requests – GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests) `[Oficial]`
- [Supported AI Models – GitHub Docs](https://docs.github.com/en/copilot/reference/ai-models/supported-models) `[Oficial]`

**Hardware / modelos locais**
- [Qwen2.5-Coder Technical Report (arXiv:2409.12186)](https://arxiv.org/html/2409.12186v3) `[Oficial arxiv]`
- [hardware-corner.net RTX 3060 benchmarks](https://www.hardware-corner.net/gpu-llm-benchmarks/rtx-3060-12gb/) `[Comunidade]`
- [singhajit.com LLM inference speed comparison](https://singhajit.com/llm-inference-speed-comparison/) `[Comunidade]`

**Integração Ollama/VSCode**
- [docs.continue.dev/guides/ollama-guide](https://docs.continue.dev/guides/ollama-guide) `[Oficial]`
- [docs.ollama.com/integrations/vscode](https://docs.ollama.com/integrations/vscode) `[Oficial]`
- [docs.codegpt.co/docs/tutorial-ai-providers/ollama](https://docs.codegpt.co/docs/tutorial-ai-providers/ollama) `[Oficial]`
- [github.com/Jadael/OllamaClaude](https://github.com/Jadael/OllamaClaude) `[Comunidade]`

**Compressão e frameworks**
- [LLMLingua (arXiv:2310.05736)](https://arxiv.org/abs/2310.05736) `[Oficial arxiv]`
- [MCCom (arXiv:2603.05974)](https://arxiv.org/pdf/2603.05974) `[Oficial arxiv]`
- [SolidGPT (arXiv:2512.08286)](https://arxiv.org/html/2512.08286v1) `[Oficial arxiv]`
- [Mellum — JetBrains (arXiv:2510.05788)](https://arxiv.org/html/2510.05788v1) `[Oficial arxiv]`
- [PROCONSUL (EMNLP 2024)](https://aclanthology.org/2024.emnlp-industry.65.pdf) `[Oficial arxiv]`
- [Prompt Compression Survey (arXiv:2410.12388)](https://arxiv.org/abs/2410.12388) `[Oficial arxiv]`

**Métricas**
- [Claude Code Agent SDK — Cost Tracking](https://code.claude.com/docs/en/agent-sdk/cost-tracking) `[Oficial]`
- [Ollama OpenAI Compatibility](https://docs.ollama.com/api/openai-compatibility) `[Oficial]`
- [Tokscale (GitHub)](https://github.com/junhoyeo/tokscale) `[Comunidade]`

---

## Próximo (gatilho empírico)

Nenhuma decisão tomada. Sugestões de experimentos para o dono avaliar:

1. **Instalar Continue.dev + `qwen2.5-coder:7b` no Ollama** e usar por 1 semana
   para autocomplete/chat de arquivo único. Medir: satisfação subjetiva,
   quantas vezes escalou para cloud, latência percebida.

2. **Habilitar Copilot Chat + Ollama** (VSCode 1.113 + Ollama 0.18.3) para ter
   chat privado local paralelo ao Copilot Pro ($10/mês) com completions ilimitadas.

3. **Instalar OllamaClaude MCP** e medir redução de tokens em uma tarefa de
   leitura de múltiplos arquivos (verificar o claim de 98.75% empiricamente).

4. **Instalar AgentsRoom ou cc-statistics** para ter baseline de custo real
   antes de qualquer otimização.

## Decisões aplicadas pelo dono

_A preencher._
