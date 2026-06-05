---
title: Plano experimental de ablação — economia de recursos IA
created: 2026-06-04
status: draft (aguardando aprovação do dono para executar)
method: fan-out 5 clusters → verificação adversarial por experimento → síntese faseada
source: workflow w1x4vitmz (26 agentes, ~1.15M tokens) + screenshot/curl do ambiente real
---

# Plano experimental de ablação

> **Nada aqui foi executado.** É o desenho. Cada experimento foi submetido a
> verificação adversarial (um agente tentando derrubá-lo). Os agentes leram os
> JSONL reais, rodaram diagnóstico do ambiente e corrigiram o desenho. O plano
> abaixo já incorpora as correções.
>
> **Os experimentos são R&D — não entram na recipe final.** A recipe é o manual
> destilado do que sobreviver à evidência. Só se escreve a recipe quando o
> `recipe_trigger` (fim do Estágio 5/6) for atingido.

## Princípio de ablação

A sequência adiciona **exatamente uma camada por estágio** sobre o substrato já
validado, de modo que qualquer delta observado seja atribuível à camada
recém-introduzida. Cada *gate* impede que ruído de uma camada não-validada
contamine a medição da seguinte. **Nenhuma intervenção paga ocorre antes de um
gate de custo zero provar que ela tem chance de passar.**

```
Estágio 1 (régua)      → instrumento de medição + baseline congelada     [custo 0]
Estágio 2 (hardware)   → motor local cru: t/s, VRAM, runtime             [custo 0]
Estágio 3 (GATE tool_use) → o ramo agêntico-local é sequer possível?     [custo 0]
Estágio 4 (editor)     → autocomplete/chat local no VSCode               [custo 0]
Estágio 5 (fornecedor) → matriz tarefa×fornecedor, comparações zero-custo [custo 0]
Estágio 6 (pago)       → só as células ainda indecisas que exigem token pago [custo>0]
```

---

## Achados do ambiente que reescrevem premissas

A verificação investigou o ambiente real e derrubou 4 premissas:

| Premissa original | Realidade verificada | Impacto |
|---|---|---|
| "Sonnet 4.6 é grátis no Copilot Pro" | Sonnet = **1x multiplier** (300/1500 créditos = consome quota). Só **GPT-4.1 / GPT-5 mini** são multiplier-0 | Baseline zero-custo correta = GPT-4.1, **nunca** Sonnet |
| Somar tokens por linha do JSONL | Mesmo `message.usage` repete ~7×/requestId → **inflação 7,33×** | Dedup **por requestId** (fallback message.id) obrigatória |
| Ollama serve tool_use ao Claude Code | Shim `/v1/messages` retorna tool call como `text/end_turn`, **não** `tool_use` estruturado | Ramo Claude-Code-local pode estar **morto** — GATE-3 decide |
| Custo medido em USD | Ambiente é **Claude Max** (quota por janela 5h, não USD/token) | Métrica = redução de input_tokens (proxy de quota), não dólar |

Três unidades de custo distintas precisam ser mantidas **separadas em cada
célula** da matriz: USD (API metada), quota (Max), créditos (Copilot).

---

## Estágio 1 — Instrumentação e baseline (custo zero obrigatório)

**Meta**: construir o instrumento de medição próprio e congelar a baseline
ANTES de qualquer intervenção. Sem régua não há delta.

- **A1** — Parser canônico dos JSONL do Claude Code (`~/.claude/projects/**/*.jsonl`).
  Extrai os 6 campos (input, output, cache_creation, cache_read, custo estimado,
  modelo). **Dedup por requestId** antes de somar. Id de modelo desconhecido →
  custo `NULL` (não 0). Exclui registros `<synthetic>`. Referência primária =
  recontagem manual de 1 sessão pequena (validação via SDK `total_cost_usd` sai
  da Fase 1 por ser custo induzido).
- **A2** — Validação cruzada `cc-statistics` × A1, mas **após normalização**
  (mesma dedup, mesmo escopo de sidechain, janela por timestamp UTC). Mede
  concordância de definição, não "confiabilidade da ferramenta".
- **A3** — Snapshot de baseline com **janela absoluta fechada no passado**
  (não `--since 3d` relativo, que quebra o hash), SHA256 reproduzível, gravado
  **fora do OneDrive** (ou hash em memória). Unidade de amostragem =
  `n_dias_com_uso ≥ 2` ou `n_requests ≥ 30` (não `n_sessions`).

**GATE-1**: parser extrai 6/6 campos com dedup, 0 parse-fails, custo ±2% da
sessão reconferida; A2 concorda ≤3% sobre dados normalizados; A3 com hash
reproduzível e `cache_hit_rate ∈ [0,1]`.

*(A4 absorvido como nota de baseline: o Copilot não escreve em `~/.claude`; sua
observabilidade exige o painel de premium requests do GitHub, não o JSONL.)*

> ### ✅ ESTÁGIO 1 EXECUTADO (2026-06-04) — GATE-1 substancialmente aberto
>
> Artefatos em `instrumento/`: `parse_usage.py`, `BASELINE.md`,
> `CROSS-VALIDATION.md`, `baseline_frozen_2026-06-03.csv`.
> - **A1 ✓** — parser com dedup por `message.id`; 0 parse-fails em 7.680 linhas;
>   inflação de 6,87× evitada (confirmada); 6/6 campos.
> - **A3 ✓** — baseline congelada (`until=2026-06-04T00:00:00Z`), SHA256
>   `b804afeb…` idêntico em 2 execuções; `cache_hit_rate=0,9454 ∈ [0,1]`.
> - **A2 ✓ (com ressalva)** — cc-statistics concorda <1% no opus (modelo
>   dominante); **ambos deduplicam** (corroboração independente). Diferença
>   residual = atribuição de sidechain (definicional, prevista), não erro.
> - **Achado da baseline**: cache_read domina (94,5% hit) — o prompt caching já
>   está quente; otimização de contexto compete contra cache barato (ecoa P3/P6).
> - **Ambiente**: configurado via metodologia dev-environment Z:\ (venv em
>   `Z:\venvs\Methodologies`, Python 3.13). Ver `lab/2026-06-04-dev-environment-z/`.

---

## Estágio 2 — Capacidade bruta de inferência local (custo zero)

**Meta**: o motor local entrega throughput interativo (H2) e cabe na VRAM?
Grandezas físicas isoladas, sem editor nem agente.

- **B1** — Throughput de **decode de compute** do `qwen2.5-coder:7b`
  (`prompt_eval_duration + eval_duration/eval_count`, **não** wall-clock nem
  `load_duration`). GPU quiesced (util <20% via nvidia-smi) **antes** do warm-up.
- **B2** — VRAM real ocupada, isolada do desktop
  (`headroom = 12288 − base − delta_global`), com `num_ctx` **declarado**
  (default já é 32768; a 32k o footprint real é ~6.9GB, **não** os 4.8GB
  weights-only da literatura).
- **B4a** — Ablação Ollama vs Foundry Local no mesmo modelo, **throughput por
  wall-clock idêntico nos dois lados**, declarada honestamente como ablação
  "runtime+quant" (GGUF Q4 vs ONNX) — conclusão restrita ao build específico,
  nunca "runtime X é melhor". Absorve B3 (prova de CUDA por A/B cpu-vs-gpu após
  quiescer a GPU, não por nome de modelo).

**GATE-2**: B1 mediana decode ≥40 t/s, `size_vram == size` (zero offload), IQR
<15%; B2 headroom calculado com num_ctx declarado; B4a ambos completam bateria
graduada (≥10 itens) com qualidade por teste unitário automatizado.

---

## Estágio 3 — GATE de protocolo tool_use (custo zero, destrava ou mata D/E4)

**Meta**: descobrir, a custo zero e ANTES de gastar 1 centavo, se o ramo
agêntico-local é sequer possível.

- **D0** — Pré-condição: provar que o Ollama serve 32k+ contexto 100% na GPU.
  Forçar cold-load (`keep_alive=0` + `ollama ps` vazio) entre settings;
  `OLLAMA_NUM_PARALLEL=1`; métrica = `SIZE/PROCESSOR/CONTEXT` de `ollama ps`.
- **D0.5** (NOVO) — `POST /v1/messages` com `tools[]` retorna
  `content:[{type:tool_use}]` e `stop_reason:tool_use`? **Evidência adversarial
  já indica FALHA** (volta como text/end_turn).

**GATE-3**: se D0.5 falhar para todos os candidatos viáveis (qwen3, llama3.1:8b,
gpt-oss), o ramo agêntico-local (D1/E4) é declarado **inviável por protocolo** e
**nenhum token pago de baseline é queimado** — a célula vira "cloud obrigatório
por incompatibilidade de tool-use".

---

## Estágio 4 — Integração de editor: autocomplete e chat local (custo zero)

**Meta**: adicionar a camada de editor sobre o motor de B já caracterizado.
Baseline de comparação zero-custo = **GPT-4.1 / GPT-5 mini (multiplier-0)**,
nunca Sonnet.

- **C1** — TTFT de **compute** do autocomplete local (descartar amostras com
  `load_duration` alto; residência provada por `size_vram == size`).
- **C2** — Overhead de integração Continue.dev medido **PAREADO por evento**
  (`t_render − t_enter` na mesma requisição), baseline C1 com o **mesmo prompt
  FIM** que o Continue gera. `OLLAMA_KEEP_ALIVE=-1`, versão da extensão fixada.
- **C3** — Fricção de setup do chat local (Copilot Chat + Ollama), escopo só
  H12/chat. Custo pago = 0 confirmado pelo **painel de premium requests do
  GitHub** (o JSONL é cego ao Copilot).

**GATE-4**: C1 TTFT p50 <500ms, p90 <800ms; C2 overhead pareado isolado de
prefill; C3 setup ≤5 passos, sucesso ≥9/10, ttft p50 <3s. *(C4 — taxa de
escalada — adiado ao Estágio 6 por tocar custo.)*

---

## Estágio 5 — Matriz fornecedor × tipo de tarefa (custo zero)

**Meta**: o **coração da recipe**. Grader objetivo + ablações onde a comparação
é zero-custo.

- **E1** — Grader **100% determinístico** (variância de pass_rate = 0 em 3
  execuções sobre input congelado; 1.0 na referência, 0.0 na vazia). Custo de
  `message.usage` com `cache_read` tratado à parte (é cumulativo por request —
  somar ingênuo infla). venv pinado em `lab/`.
- **E2** — Ablação de fornecedor para **autocomplete**: local vs GPT-4.1.
  Latência por ordem de grandeza, streaming, N≥10.
- **E3** (reescopado de `invalid`) — Ablação **chat/raciocínio**: local vs
  GPT-4.1/GPT-5 mini multiplier-0. Removido gpt-oss 20.9B (não cabe em 12GB →
  trocar por deepseek-r1:8b ou qwen3:14b); janelas de contexto padronizadas;
  N≫5; custo Copilot pelo painel do GitHub.

**GATE-5**: E1 grader determinístico com ≥3 classes ablacionáveis; E2/E3
produzem pass_rate por fornecedor por classe com decisão registrada.

---

## Estágio 6 — Validação paga mínima e justificada (FASE 2, custo>0)

**Meta**: SÓ os experimentos que exigem token pago real, e SOMENTE se os
estágios anteriores não decidiram a matriz e se o GATE-3 passou.

- **D1** — Roteamento total Claude Code → Ollama local. **Só se D0.5 verde.**
  Reenquadrado como decisão sobre o **bundle** (backend+modelo+contexto+quant),
  n≥3 ambos os braços. Custo zero local verificado por **ausência de tráfego a
  api.anthropic.com**.
- **D2** — `CLAUDE_CODE_SUBAGENT_MODEL=haiku`. Subagentes logam em
  `<uuid>/subagents/*.jsonl` (não na JSONL principal) → somar recursivamente.
  Main forçado em `--model sonnet`. ≥3 runs contrabalançados.
- **D3** — Pré-sumarização local de leitura de arquivo. Métrica = **redução de
  input_tokens** (proxy de quota, ambiente é Max), não USD. Condição de controle:
  doc cru **truncado** ao tamanho do sumário (separa eficiência-do-sumário de
  extração-do-7B).
- **E4** — Refatoração multi-arquivo com backend local. **Só se D0.5 verde.**
  Teto de turnos/wall-clock para distinguir erro-duro de loop-infinito.

**GATE-6 (encerramento)**: cada célula `fornecedor × classe-de-tarefa` tem
veredito objetivo (manter local / Copilot multiplier-0 / cloud obrigatório /
inconclusivo), com pass_rate e custo reproduzíveis. **Resultados negativos são
verdicts válidos** e suficientes para fechar a célula.

---

## Riscos abertos do plano

1. **Nenhum instrumento existe ainda** — parser, grader, pasta tasks/,
   cc-statistics não instalado. Estágio 1 e E1 são caminho crítico; bug neles
   invalida silenciosamente tudo a jusante.
2. **Bloqueador de tool_use já evidenciado** — se nenhum modelo local emitir
   tool_use estruturado, D1/E4 morrem inteiros. GATE-3 existe para descobrir a
   custo zero.
3. **Três unidades de custo** (USD/quota/créditos) — misturar invalida qualquer
   comparação de economia.
4. **Contenção de GPU pelo desktop** — 78% util e ~10GB ocupados em idle. Sem
   quiescer, deltas de VRAM/throughput são falsos.
5. **Poder estatístico fraco** — N=5 cai dentro do IC binomial; exige N≥10
   (E1/E2/E3) e n≥3 (loops agênticos). Multiplica tempo e, na Fase 2, custo.
6. **Não-determinismo do Ollama** mesmo com temperature=0/seed (batching de GPU)
   sabota reprodutibilidade de hash e contagem.
7. **Teste de transporte** pode revelar que a config ótima é específica deste
   ambiente (RTX 3060 + Copilot Pro + Claude Max) e não generaliza — a recipe
   precisa declarar suas pré-condições de hardware/assinatura.

---

## recipe_trigger (quando escrever a recipe)

Quando cada célula da matriz fornecedor×classe tiver um veredito objetivo e
reproduzível ao fim do Estágio 5 (e Estágio 6 só para as células que o exigirem).
A recipe destila os vereditos "sempre faça X" — não os experimentos.

## kill_criteria (quando abandonar)

Se o motor local não atingir qualidade aceitável em nenhuma classe de tarefa
(GATE-2/GATE-5 falham em todas), o ramo local morre e a recipe vira "use os
modelos multiplier-0 do Copilot + Claude Max para o resto" — ainda um resultado
válido e útil.
