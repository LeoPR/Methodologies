---
title: Grande revisão — primitivas v2, disco/duplicação, hardware real do dev médio
created: 2026-06-04
status: síntese (workflow w53h8gy3p, 7 agentes + evidência de 1ª mão da máquina do dono)
relates: [mapa-recursos-llm.md, arvore-decisao.md, observacao-disco.md, prototipo/]
---

# Grande revisão — primitivas, disco e hardware real

> Re-análise das primitivas com **disco/duplicação em 1ª classe**, a **realidade
> do hardware do dev médio 2026** (com viés corrigido), dois caminhos felizes, e a
> influência do **estilo de projeto**. Apoiado em pesquisa (5 frentes, confrontada)
> + medição de 1ª mão (118,5 GB de modelos na máquina do dono).

## 1. Primitivas v2 (disco e modalidade promovidos)

| Primitiva | Sub-recursos | Novidade deste ciclo |
|---|---|---|
| **PROCESSAMENTO** | CPU · GPU | a **arquitetura** da GPU importa tanto quanto a VRAM (Turing/Ampere c/ Tensor cores ≫ Pascal; Ampere sem 4-bit nativo dá +30-45% latência batch=1) |
| **MEMÓRIA** | RAM · VRAM · **DISCO-persistente** · cache-KV | **DISCO promovido**: pesos são arquivo imutável, mas cada framework o embrulha numa convenção de store diferente; é a única sub-primitiva que **persiste e acumula silenciosamente** |
| **ENTRADA/SAÍDA** | tokens/s · contexto · **conversão-de-modalidade** | **modalidade promovida**: imagem→tokens / vídeo→tokens consome janela + VRAM + **disco** (VLMs são arquivos separados e mais pesados) |

**O vetor de esforço ganha a 6ª coordenada**: `{TTFT, TPOT, throughput, $/tarefa,
fit-VRAM, DISCO-livre}`. **Duplicação** não é primitiva nova — é relação de 2ª ordem
sobre disco: custo de manter o mesmo peso conceitual em K representações.

## 2. A condição esquecida — disco e duplicação (medido)

**Evidência de 1ª mão**: 25 modelos Ollama = **118,5 GB**, num bind-mount Docker em
`M:\ollama\models`, com `~/.ollama` (default) **vazio**. Quem procurasse no caminho
óbvio veria 0 GB — o custo está deslocado e invisível.

**Footprint por formato/quant** (a maior alavanca, antes de duplicar): qwen2.5-coder:7b
varia ~3,3× só por quant — Q4_K_M ~4,7 GB / Q8 ~8,1 / FP16 ~15,2. gpt-oss ~13 GB.

**Duas barreiras de duplicação, por gravidade:**
1. **Formato incompatível → duplicação INEVITÁVEL.** Ollama/LM Studio/llama.cpp = GGUF;
   Foundry/.aitk = ONNX. Mesmo modelo no Foundry **E** no Ollama = 100% duplicado, sem
   symlink possível. (Confirmado: `.aitk` do dono tem 0,32 GB — baixar o qwen pelo
   Foundry seria arquivo separado do GGUF.)
2. **Convenção de store no mesmo formato → duplicação EVITÁVEL.** Ollama = blob
   content-addressed (sha256, sem `.gguf`); LM Studio = árvore publisher/model. Symlink
   resolve (mas é dependência, não redundância; Windows exige Developer Mode).

**Consolidar (ordem)**: (a) escolher **1 store GGUF**; (b) redirecionar para fora do
SSD do sistema (`OLLAMA_MODELS=D:\…`; cuidado: `OLLAMA_HOME` é ignorado no Windows);
(c) symlink entre stores GGUF quando 2 clientes; (d) higiene (remover mortos +
`docker system prune` = ~15 GB recuperáveis no dono). **NÃO** fazer `ollama create
FROM ./x.gguf` esperando compartilhar — isso COPIA para blob novo (duplica).

## 3. Hardware real do dev médio 2026 (com viés corrigido)

**Descoberta-mãe**: **não existe survey de dev com distribuição de RAM/GPU/VRAM.**
Stack Overflow e JetBrains medem só o SO. Todo "X% dos devs tem 8GB VRAM" é
extrapolado de gamer (Steam, enviesado) ou mercado. A pergunta-chave não tem fonte
primária.

**Todos os vieses apontam na mesma direção — SUPERESTIMAR o hardware do dev**: Steam =
gamers (93,85% Windows vs ~32% macOS entre devs; sobre-representa NVIDIA); SO/JetBrains
= auto-seleção de entusiastas; blogs comerciais pró-hardware-forte; viés de sobrevivência
(quem escreve "rode local" já tem a máquina).

**Baseline defensável**: laptop, **16GB RAM** (fatia relevante ainda 8GB soldado/
corporativo), **SEM GPU NVIDIA útil** (só iGPU Iris Xe/Radeon que não acelera 7B
interativo), SSD **512GB** (budget 256) dividido com SO+IDE+Docker+node_modules.

**A métrica honesta é "confortável" (≥30 t/s), não "usável".** Defensável: **~25-40%
dos devs** rodam um 7B Q4 confortavelmente; **a maioria não**. (CPU a 7-10 t/s é
"batch/assíncrono", não autocomplete.)

> **Corolário de design — INVERTER O DEFAULT**: para o dev médio, o caminho confiável
> é **CLOUD/managed** (Copilot inline multiplier-0 ilimitado, já medido). O 7B local é
> **minoria** com HW adequado OU experimento consciente. Como não há estatística
> populacional, o default operacional é o **caminho guiado (auto-detectar a máquina)**,
> nunca presumir capacidade local.

## 4. Faixas de hardware (cada uma com seu ótimo)

| Faixa | Hardware | Modelo local ótimo | Fração (a-confirmar) |
|---|---|---|---|
| **CPU-only / iGPU** | laptop 8-16GB, Iris Xe | **3B Q4** (~2GB, 15-25 t/s); 7B vira batch | **a maior fatia** — default CLOUD |
| **6GB** | RTX 2060/1660/1060 | **3B** (7B só com ctx 2-4k); arquitetura manda | minoria |
| **8GB** | RTX 3050/2070/2080 | **7B-8B Q4** (~30-40 t/s, a-confirmar) | minoria (destrava aqui) |
| **8-12GB WDDM** | **RTX 3060 12GB (MEDIDO)** | qwen2.5-coder:7b @ ≤16k = **55 t/s**; penhasco a 32k/14B | minoria, melhor custo-benefício |
| **16-24GB** | 4070Ti/4080/4090, 4060Ti 16GB | 14B Q4 confortável; **re-medir** (não capar em 16k) | minoria menor (A3/A6) |
| **Apple unified** | M1-M4 (>80% dos Macs de dev) | piso 16GB→8B Q4; M Max ≈ 3060; base-8GB fora | ~20-25% dos devs |

## 5. Caminho feliz OTIMO (motivar o dev e a ferramenta)

Diferente por faixa — o ganho-bandeira de cada uma:
- **Sem-GPU (a maioria)**: ligar JÁ o **Copilot autocomplete inline** (multiplier-0,
  ilimitado) + chat multiplier-0. Ganho imediato, zero disco, zero WDDM. **Não prometer
  7B local** que a máquina não aguenta — isso é o que motiva pela honestidade.
- **6GB**: não force 7B → **3B rápido** (~50 t/s). A sensação de velocidade motiva mais
  que um 7B a 18 t/s.
- **3060 (8-12GB)**: o número-bandeira **medido** — qwen2.5-coder:7b @ ≤16k = **55 t/s,
  TTFT 68ms**. Ollama + Continue.dev, local e privado, de graça.
- **16-24GB**: re-medir e subir o teto — 14B + contexto 32k + agêntico local.
- **Apple 16GB+**: 8B nativo (Metal/MLX) interativo; privacidade + offline + $0.
- **Transversal (motiva a FERRAMENTA)**: emitir o `environment-profile.yaml` para a IA
  parar de sugerir movimento que a máquina não suporta.
- **Anti-armadilha que motiva**: deixar claro que **Sonnet no Copilot NÃO é grátis**
  (1×/300 req) — o dev confia mais quando a recomendação admite o custo escondido.

## 6. Caminho feliz GUIADO (auto-investigar a própria máquina)

Ancorado no `prototipo/detect_env.py` (read-only). 8 passos:
0. **detect_env.py** — sonda GPU/VRAM, Ollama, Copilot, regime, pode_instalar, sync, disco.
1. **VRAM/RAM real** (total E livre — jogo/Chrome roubam VRAM). Sem dGPU útil → cloud.
2. **[NOVO] Sonda de DISCO** — `free_gb` por **volume** (não só cwd) + localizar TODOS os
   stores, **incluindo Docker bind-mount** (o caso do dono: `~/.ollama` vazio, store real
   em `M:\`). Sondar só o default daria 0 GB FALSO.
3. **[NOVO] Sonda de DUPLICAÇÃO** — mesmo modelo em >1 store; evitável (GGUF+GGUF→symlink)
   vs inevitável (GGUF+ONNX→custo estrutural); reportar reclaimable + modelos mortos.
4. **Protocolo tool_use** — cruzar modelos baixados com a allowlist (PASS: llama3.1:8b/
   qwen3:14b; FAIL: qwen2.5-coder:7b). Mais VRAM não conserta protocolo.
5. **Regime + policy** — distinguir bloqueio FÍSICO (evolua HW) de POLICY (escale ao IT).
6. **Declarar a PRIORIDADE** (cobertor curto).
7. **Emitir `.ai/environment-profile.yaml`** com tier, disco-livre, stores+duplicação,
   allowlist, regimes separados. **Re-medir t/s** (os 55 t/s são parâmetro, não constante).

## 7. Framework: o ollama-server é necessário?

**Em geral NÃO.** O daemon (`localhost:11434`) só é necessário SE o engine for Ollama.
**Foundry Local não tem daemon** (biblioteca in-process ~20MB). As extensões VSCode são
**clientes**; o engine é o framework por baixo. **Escolha 1.**

**Consolidar em 1 engine: SIM — e a decisão é dominada por DISCO, não por t/s.** Para 1
dev no VSCode (single-user), o t/s é ~idêntico entre engines GGUF (llama.cpp puro é só
3-10% mais rápido que Ollama em NVIDIA — imperceptível). A premissa "todos são wrappers
de llama.cpp" está **desatualizada**: Ollama **forkou** (~mar/2025, build vendorizado) e
**anda atrás do upstream** em Vulkan/AMD (~56% mais lento) — mas **não em CUDA/NVIDIA**.
Foundry/ONNX "3,9× mais rápido"? **Não comprovado de forma justa** (compara ONNX-otimizado
vs GGUF-quantizado). **Veredito**: escolha o engine que minimiza **duplicação + daemon
idle + formato**, não o t/s.

## 8. O estilo do projeto muda as otimizações

| Estilo | O que muda |
|---|---|
| **Monorepo TS/Java** | estratégia de **contexto** domina (grep-first/AST stateless = 0 disco); visão irrelevante; Copilot indexa local só até 2.500 arquivos |
| **Doc-heavy / pesquisa (Strata)** | a **exceção** onde RAG/embeddings vence — mas a alternativa sem disco é long-context + cache; RAG só quando o corpus excede a janela (e aí **duplica** disco) |
| **Data-science / notebooks** | **único** estilo onde VISÃO agrega (VLM lê plots ~90%); favorece iteração rápida; coder+VLM pressiona VRAM **e disco** |
| **Embedded C/Rust** | precisão > velocidade; pede modelo MAIOR (14B) — que na 3060 **cai no penhasco WDDM**; loop de compilador importa mais que t/s |
| **Legado / brownfield** | maior ROI do **agêntico** + modelo mais forte (**frontier/cloud**); CLAUDE.md aninhados; reforça o default cloud |
| **Greenfield / scripts** | tolera modelo menor (3B/7B local); grep-first basta; 0 disco extra; onde o caminho A5-econômico rende mais |

## 9. O que adicionar à árvore e ao protótipo

- **Sonda de disco por volume** (não só cwd) — o store vive fora do SSD do sistema.
- **Sonda de localização de store** incl. **Docker bind-mount** (`~/.ollama` pode estar vazio!).
- **Sonda de duplicação** — evitável vs inevitável; reclaimable; modelos mortos.
- **M16 — consolidar framework** (1 engine GGUF; decida por disco, não t/s).
- **M17 — redirecionar store** para volume não-sistema (análogo ao M8 do venv).
- **M18 — higiene de store** (remover mortos + `docker system prune`).
- **Faixas de HW** além da 3060: bucket 6GB (3B), apple_unified (~72% útil), refinar <8GB.
- **DISCO-livre como 6ª coordenada** no environment-profile.yaml.
- **Inverter o default**: ramo CLOUD é o default do dev médio; ramo LOCAL só após a
  auto-detecção PASSAR. Reportar sempre "confortável" (≥30 t/s), nunca "usável".

## Próximo
- Estender `detect_env.py` com as sondas de disco/store/duplicação (M16-M18).
- Depois: destilar a recipe portável (já há base muito forte).
