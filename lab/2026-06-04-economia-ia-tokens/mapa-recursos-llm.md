---
title: Mapa de recursos LLM — primitivas, métrica de esforço e grade epistêmica
created: 2026-06-04
status: open
method: 6 buscas por vetor → consolidação (32 princípios) → refutação adversarial 3-lentes → síntese
source: workflow wz8rhxrrb (38 agentes, ~1.14M tokens); triangulado com w1x4vitmz (plano experimental)
---

# Mapa de recursos LLM

> O **mapa** do terreno: o que é sempre-ótimo, o que depende (e de quê), o que
> não dá pra saber sem medir, e o que é chute. O plano experimental
> (`plano-experimental.md`) são as **sondas** que testam as células incertas
> deste mapa. Os dois convergiram independentemente — inclusive ambos pegaram
> a mesma mentira de custo ("Sonnet grátis").

## A descoberta de método (a mais importante)

Quase **nada** é "sempre faça X". O que é universal é "**X é sempre VERDADE**"
(uma lei física, uma garantia matemática, um fato de contrato) — mas "**o que
você FAZ a respeito de X depende do regime**". As 11 candidatas a sempre-ótimo
apanharam de 3 lentes (tipo-de-tarefa, hardware/escala, regime-de-custo); todas
foram demovidas na ação, mas 8 sobreviveram no **núcleo descritivo**.

Isto é exatamente a distinção que o Strata faz entre um princípio e sua
aderência condicional. O mesmo formato epistêmico reaparece num domínio
completamente diferente — sinal de que a forma é robusta.

---

## 1. As 4 primitivas e os seus 5 vetores

Os 5 vetores que você nomeou mapeiam nas 4 primitivas físicas numa relação
**muitos-para-muitos** (não bijetora):

| Seu vetor | Primitivas que toca | Observação |
|---|---|---|
| **Memória** | MEMÓRIA (janela/KV/RAG/compaction) + processamento (atenção degrada com comprimento) + E/S + custo | contexto é recurso finito |
| **Velocidade** | PROCESSAMENTO (decode/prefill) ancorado em MEMÓRIA (decode batch-1 é memory-bandwidth-bound) | **não é primitiva** — é o tempo que emerge de `max{compute, banda}` |
| **Inteligência-pra-situação** | PROCESSAMENTO (capacidade) condicionado por MEMÓRIA (o que cabe na VRAM) e E/S (reasoning tokens) | "inteligência suficiente para ESTA tarefa", não absoluta |
| **Economia** | CUSTO — **com ressalva** | em regime metered o $ acompanha a física; em flat-rate/quota o $ **desacopla** e vira eixo próprio, discreto |
| **Capacidade-de-rodar** | MEMÓRIA (cabe na VRAM?) + processamento (quant degrada) + custo (hardware) | **gatilho-mestre local**: caber pesos+KV nos 12GB domina o resto |

### Por que não dá pra maximizar tudo (a fronteira de Pareto)

As 4 primitivas formam **superfícies de troca**, não um ótimo conjunto:

- **Memória vs processamento**: encher a janela aumenta material mas degrada atenção (context rot) e custa banda/latência.
- **Inteligência vs velocidade**: modelo maior/quant menor = mais inteligente porém mais bytes/token = decode mais lento.
- **Capacidade vs velocidade**: modelo que só cabe com offload despenca tokens/s — **mas inverte em MoE esparso** (só experts ativos cruzam PCIe).
- **Custo vs tudo**: o tier de custo-marginal-zero (local/Copilot) tem teto de capacidade (12GB) e de qualidade.

> Maximizar inteligência + velocidade + capacidade ao mesmo tempo é **impossível**
> porque competem pela MESMA VRAM e MESMA banda em hardware fixo. **É por isso
> que a resposta certa é quase sempre roteamento por situação, não um setup único.**

---

## 2. A "métrica geral de esforço" — não existe um escalar

A pergunta "dá pra ter uma métrica geral de esforço?" tem resposta honesta e
**negativa**, e ela sobreviveu à refutação:

**NÃO há um número único.** O melhor que a literatura oferece (roofline estendido /
LIMINAL, arXiv:2507.14397) é um modelo de sistema multidimensional:

```
esforço_físico = latência ≈ max{ trabalho_compute/FLOPs_pico , bytes_movidos/banda } + sync_exposta
                 sujeito a:  pesos + KV cabem na memória?
```

Que **não colapsa num número** porque:
1. **Prefill** (compute-bound, governa TTFT) e **decode** (memory-bound, governa TPOT) têm regimes físicos **opostos** — otimizar um não otimiza o outro.
2. A métrica vinculante muda com o workload: interativo → TTFT+TPOT; batch/offline → throughput agregado.
3. Custo/energia **não** é derivável da física em geral (em flat-rate desacopla).
4. FLOPs/GPU-util subestimam energia real **2–6×**.

> **Conclusão**: a métrica de esforço é um **vetor de ≥5 coordenadas** medidas no
> seu próprio hardware: `{TTFT, TPOT, throughput-agregado, $-por-tarefa, fit-de-VRAM}`,
> e a coordenada que manda depende do regime. Use o vocabulário das 4 primitivas
> para **diagnosticar** (sempre útil), mas reduzir a um escalar leva a otimizar a
> coordenada errada.

---

## 3. SEMPRE-ÓTIMO — o caminho feliz (8 movimentos, sobreviveram à refutação)

Estes são os movimentos que se faz **independente do contexto** — porque cada um
é uma lei, garantia ou fato, não uma aposta de regime. Cada um é **custo ~zero**
ou **ganho sem trade-off**.

1. **Diagnostique antes de prescrever**: classifique a fase da tarefa — prefill/TTFT-dominada (autocomplete, retrieval single-shot) vs decode/TPOT-dominada (geração longa). São gargalos físicos diferentes (P10).
2. **Use as 4 primitivas como lente** (compute, banda, capacidade, custo), raciocinando por roofline antes de culpar "falta de FLOPs" — sem assumir que vira um escalar (P9-núcleo). *[COMPROVADO: Yuan et al. arXiv:2402.16363]*
3. **Nunca despeje contexto IRRELEVANTE/distratores**: eles só podem degradar a qualidade, independente de custo ou cache (P3-núcleo). *[COMPROVADO: Chroma Context Rot 2025]*
4. **Material crítico no início/fim, nunca no meio** quando você monta contexto longo e controla a ordem (P2) — custo zero, só pode ajudar. *[COMPROVADO: Liu et al. TACL 2024, arXiv:2307.03172]*
5. **FlashAttention/atenção IO-aware sempre que o prefill/TTFT domina**: é exato (mesma saída), ganho de wall-clock sem trade-off (P10). *[COMPROVADO: Dao et al. NeurIPS 2022]*
6. **K-quants > quants legados** no mesmo nº de bits; Q8_0 como baseline lossless (P28) — domina por construção. *[COMPROVADO: arXiv:2601.14277]*
7. **Confie nas garantias FORMAIS**: speculative decoding não muda a saída (P11), NF4 > int em baixos bits (P27) — mas trate o GANHO de velocidade como algo a medir, não a assumir. *[COMPROVADO: Leviathan et al. ICML 2023; Dettmers & Zettlemoyer ICML 2023]*
8. **Output custa 2×–6× input** por token enquanto você paga por token (P23-núcleo) — fato de contrato que orienta toda decisão de E/S metered. *[COMPROVADO: pricing oficial]*

---

## 4. DEPENDE — condicionais com gatilho observável (26 princípios)

Os que mais importam para o seu ambiente (`testable_here=True` = dá pra
experimentar na RTX 3060/Copilot/Ollama):

| # | Princípio | Gatilho (quando é ótimo) |
|---|---|---|
| P1 | Medir o limite útil efetivo de contexto | entrada controlada por você que cresce até a zona de degradação; **NO-OP** se a janela é fixa pela ferramenta (autocomplete FIM 4-8k) ou travada por VRAM |
| P4 | RAG vs contexto-cheio | corpus > janela ou dinâmico → RAG; pequeno/estático com raciocínio cruzado → cheio |
| P5 | Compactar histórico de sessão | ocupação perto do limite efetivo; no 3060 o gatilho chega **cedo** (4-8k) |
| P6 | Reutilizar prefixo via prompt cache | prefixo idêntico e longo reusado **dentro do TTL** (~5min); se muda a cada chamada, o cache WRITE (1.25-2×) só encarece |
| P7 | Contabilizar+quantizar KV | contabilizar: quase-sempre; quantizar KV: só quando estoura VRAM (>~28k num 7B no 12GB) |
| P11 | Speculative decoding (velocidade) | memory-bound, batch baixo (~1-8), draft com aceitação ≥0.6; em batch alto **fica mais lento** |
| P13 | Quant weight-only acelera decode | memory-bound + kernel otimizado; **ressalva Ampere**: 3060 não tem 4-bit nativo → batch=1 pode dar **+30-45% latência** vs FP16 que cabe |
| P14 | "Menor que cabe > maior que vaza" | modelo **denso** + latência-bound + o menor é capaz; **inverte em MoE esparso** |
| P17 | Cascata barato→caro por dificuldade | existe verificador barato (testes/lint) + mistura real fácil/difícil; em código o verificador existe |
| P20 | Right-size o esforço de raciocínio | dificuldade observável; trivial → thinking off; nenhum modelo estima a própria dificuldade → **gate manual** |
| P22 | Custo-por-tarefa, não por token | inferência metered + $ é a restrição dominante; em flat-rate/local o $/tarefa é ~0 e a métrica vira TEMPO |
| P25 | Grátis/local primeiro **com checagem** | tarefa dentro da capacidade local OU existe oráculo barato; **falha** acima da capacidade sem oráculo |
| P27 | Maior em 4-bit > menor em 8/16-bit | acurácia-por-VRAM, zero-shot; **falha** em batch=1 Ampere e em raciocínio multi-passo |
| P29 | Grandes toleram quant; pequenos frágeis | <7B não descer de 4-bit (Q4_K_M); 70B+ aguentam 4-bit |
| P30 | Dano do quant não é uniforme | raciocínio/matemática degradam mais → suba o quant (Q5/Q8) para código/matemática |
| P31 | Custo como "camada sobre a física" | só em regime metered; em flat-rate/quota o $ vira **primitiva própria discreta** |

*(Lista completa de 26 no output bruto do workflow.)*

---

## 5. NÃO-SABÍVEL a priori — só medindo (8)

Sete viram **experimento** (`must_measure=True`); um é genuinamente indeterminado.

| O que | Por que não dá pra saber sem medir |
|---|---|
| tokens/s, TTFT, aceitação de spec-decode, ganho de quant no SEU setup | a literatura dá **leis** universais, nunca **números** universais — variam com modelo/kernel/runtime/quant |
| ponto ótimo de compactação (recall vs precisão) | depende da tarefa e do que será necessário adiante |
| bit-rate exato de quebra de qualidade do quant | a literatura dá a forma da curva; o joelho exato é empírico |
| crossover "caro resolve em 1 vs barato em 5" | sem RCT publicado; é caso-a-caso, medir $/PR-resolvido |
| taxa real de aceitação do tier local | depende do domínio/estilo do **seu** código; o "80% OK" é informal |
| custo energético real da 3060 por 1.000 tokens | não há benchmark elétrico para Ampere/3060; medir watts no próprio HW |
| claim de 98.75% do OllamaClaude MCP | número do autor, sem replicação |
| **se existe uma métrica de esforço escalar** | **genuinamente negativo** — o objeto não colapsa num escalar sem escolher um regime; não é questão de medir mais |

---

## 6. CHUTES sinalizados (não adotar sem testar)

- ❌ "90% de economia TOTAL com prompt caching" — o desconto é só sobre input **cacheado** (0.1×), não output nem input novo; o cache WRITE chega a encarecer.
- ❌ "input é 70-85% do gasto" — depende inteiramente do mix; saída/raciocínio longo inverte.
- ❌ break-even de auto-hospedagem "2M+ tok/dia, GPU >70%, API 3-5× o GPU" — números de blogs comerciais que se citam, sem estudo replicado.
- ❌ "quantizar SEMPRE acelera" — no Ampere/3060 batch=1 pode ficar **+30-45% mais lento** que FP16 que cabe.
- ❌ "janela maior = melhor / use o 1M" — context rot e o gap claimed-vs-effective (RULER) contrariam.
- ❌ "sempre rode o maior modelo que cabe na VRAM" — inverte para MoE; dominado por plano grátis superior.
- ❌ **"Sonnet 4.6 via Copilot é grátis"** — é **1× multiplier sobre 300 req/mês finitos** no Pro; só autocomplete inline e GPT-4.1/GPT-5-mini são multiplier-0 de verdade. *(confirmado no lab; era erro nosso de ciclos anteriores)*
- ❌ "mais thinking sempre ajuda" — modelos pensam 7-10× demais em tarefas triviais (overthinking).
- ❌ "self-consistency é barato e vale sempre" — <2% de ganho a ~20× de custo em modelos modernos.

---

## 7. Como o mapa alimenta o plano experimental

Os "experiment_candidates" desta síntese **convergem** com os clusters do
`plano-experimental.md` — dois workflows independentes chegaram nas mesmas sondas:

| Candidato (deste mapa) | Estágio do plano | Resolve |
|---|---|---|
| Benchmark base no 3060 (tokens/s, TTFT, TPOT) | Estágio 2 (B1/B2) | P16 |
| Penhasco offload denso vs MoE | Estágio 2 (B4a) | P14 |
| Quant vs latência em Ampere (Q4/Q8/FP16) | Estágio 2 | P13/P27 |
| Joelho de qualidade por quant/tarefa | Estágio 2/5 | P29/P30 |
| Taxa de aceitação do tier local | Estágio 4/5 (C4) | P17/P25 |
| Prompt cache hit-rate real (JSONL) | Estágio 1/5 (A1/E1) | P6/P3 |
| Contexto útil vs VRAM (OOM) | Estágio 2 (D0/B2) | P1/P7 |
| Custo energético (watts × tempo) | novo — não estava no plano | P32 |
| $-por-tarefa-completa (Agent SDK) | Estágio 6 (D2/D3) | P22 |
| RAG vs contexto-cheio no corpus do projeto | novo candidato | P4 |

> **A recipe final** será destilada da coluna "sempre-ótimo" (caminho feliz, §3)
> + os vereditos das células "depende-testável" e "não-sabível" que os
> experimentos resolverem. Os "chutes" (§6) entram na recipe como **avisos
> explícitos** do que NÃO fazer.

---

## Fontes-chave (comprovado vs boa-prática vs chute)

- Context rot: [Chroma 2025](https://www.trychroma.com/research/context-rot); [RULER arXiv:2404.06654](https://arxiv.org/abs/2404.06654) — COMPROVADO
- Lost in the middle: [Liu et al. TACL 2024, arXiv:2307.03172](https://arxiv.org/abs/2307.03172) — COMPROVADO
- RAG vs LC + Self-Route: [arXiv:2407.16833](https://arxiv.org/pdf/2407.16833); LaRA "no silver bullet" — COMPROVADO
- Prompt cache agêntico: [arXiv:2601.06007](https://arxiv.org/html/2601.06007v2) (41-80% custo) — COMPROVADO
- KV cache/quant: KIVI [arXiv:2402.02750], KVQuant [arXiv:2401.18079], SnapKV — COMPROVADO
- Roofline/memory-bound: [Yuan et al. arXiv:2402.16363]; FlashAttention [Dao et al. NeurIPS 2022] — COMPROVADO
- Speculative decoding lossless: [Leviathan et al. ICML 2023] — COMPROVADO (garantia matemática)
- 4-bit/NF4: [Dettmers & Zettlemoyer ICML 2023] (>35k experimentos) — COMPROVADO
- K-quants/Q8 lossless: [arXiv:2601.14277] — COMPROVADO
- Roteamento por dificuldade: FrugalGPT (TMLR 2024), RouterBench, RouteLLM — COMPROVADO
- Right-size raciocínio: OptimalThinkingBench [arXiv:2508.13141]; Snell et al. [arXiv:2408.03314] — COMPROVADO
- Esforço multidimensional: LIMINAL [arXiv:2507.14397] — BOA-PRÁTICA (sem replicação)
- Break-even auto-host, "90% cache", "input 70-85%" — CHUTE de blog
