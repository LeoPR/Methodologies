---
title: Estágio 2 — capacidade bruta de inferência local (RTX 3060 12GB)
created: 2026-06-04
status: B1+B2 concluídos (GATE-2 do 7B passa); B4a pendente (Foundry Local)
hardware: NVIDIA RTX 3060 12GB, Windows 10, desktop vivo (~2.5GB VRAM de fundo)
instrumento: bench_decode.py (decode de compute via API Ollama, não wall-clock)
---

# Estágio 2 — inferência local raw

> Medições no hardware real. `bench_decode.py` usa `eval_count/eval_duration` da
> API do Ollama (decode de **compute**, não wall-clock). temperature=0, seed=42,
> 1 warm-up descartado + N medições. GPU quiescente no início (5-6% util,
> ~2,5 GB de fundo). **Custo zero** (inferência 100% local).

## B1 + B2 — qwen2.5-coder:7b (Q4_K_M) × contexto

| num_ctx | decode (t/s) | IQR | prefill | VRAM modelo (ollama ps) | nvidia used | livre | PROCESSOR |
|---|---|---|---|---|---|---|---|
| 4.096 | **55,53** | 0,3% | 45 | 4,9 GB | 7201 MiB | 4915 | 100% GPU |
| 16.384 | **50,72** | 0,1% | 45 | 5,9 GB | 8160 MiB | 3956 | 100% GPU |
| 32.768 | 13,90 | 39,6% | 5 | 6,9 GB | 9333 MiB | 2783 | 100% GPU* |

`*` ollama reporta 100% GPU, mas o regime é instável (ver penhasco abaixo).

### GATE-2 (qwen2.5-coder:7b @ 4k–16k): PASSA
- decode mediana 55,5 / 50,7 t/s ≥ 40 ✓
- IQR 0,3% / 0,1% < 15% ✓ (reprodutibilidade altíssima)
- `size_vram == size`, zero offload de CPU ✓

### Achado 1 — VRAM cresce LINEAR com o contexto (confirma P7 do mapa)
4,9 → 5,9 → 6,9 GB de 4k → 16k → 32k. **O footprint a 32k é 6,9 GB** — bate
exatamente a previsão da verificação adversarial, e refuta os "4,8 GB
weights-only" da literatura (que ignora o KV cache). O KV é a variável.

### Achado 2 — PENHASCO de VRAM-pressão a 32k (não é offload de CPU)
Decode despenca 50,7 → **13,9 t/s** e a variância explode (IQR 40%, faixa
10,9–21,9) ao passar de 16k para 32k. `ollama ps` ainda diz 100% GPU, mas só
restam **2,7 GB livres** num desktop vivo. Diagnóstico: **WDDM shared-memory
fallback** do Windows — quando a VRAM livre fica escassa, o driver migra páginas
GPU↔RAM do sistema, tankando o throughput. Não é offload declarado (ollama não
vê), é contenção do driver. A instabilidade (IQR 40%) é a assinatura.

## Capacidade — qwen3:14b (Q4, 9,3 GB) @ 4k

| | decode | IQR | VRAM | livre |
|---|---|---|---|---|
| qwen3:14b @ 4k | 13,44 t/s | 28,9% | 11787 MiB | **329 MiB** |

### Achado 3 — o 14B "cabe" mas NÃO tem regime estável (refina P14)
ollama diz 100% GPU, mas sobram **329 MiB** — VRAM essencialmente esgotada. Cai
no mesmo penhasco WDDM: 13,4 t/s, IQR 29%. A literatura cita ~30 t/s para o 14B,
mas isso é em GPU limpa; **num desktop compartilhado o 14B não tem folga**.

> **Refinamento de P14** ("menor que cabe > maior que vaza"): no 3060 com
> desktop vivo, "cabe pelo ollama" ≠ "tem regime estável". O gatilho real não é
> `size_vram == size`, é **VRAM livre suficiente para o WDDM não thrashar**
> (empiricamente, > ~2,7 GB livres). O 14B e o 7B@32k violam isso.

## Conclusão do Estágio 2 (para a recipe)

**Sweet spot medido nesta máquina (RTX 3060 12GB + desktop Windows vivo):**
- **qwen2.5-coder:7b @ contexto ≤ 16k** → 50–55 t/s, estável (IQR <0,5%), 100% GPU.
- **Evitar ≥ 32k no 7B e o 14B inteiro** → penhasco WDDM (~13 t/s, instável).
- Regra prática: manter **≥ 2,7 GB de VRAM livres**; quiescer apps de fundo
  pesados (Broadcast, Edge, Docker) sobe o teto de contexto utilizável.

Isto é exatamente uma célula "**não-sabível a priori, só medindo**" do mapa
(P16/P1/P7): nenhum paper dá o teto de contexto da SUA máquina com SEU desktop —
só a medição dá. O número (~16k para o 7B) entra na recipe como pré-condição
de hardware.

## B4a — Ollama vs Foundry Local

> ### ⚠ RETRATAÇÃO (2026-06-04): a 1ª conclusão "Foundry OS-gated no Win10" foi PREMATURA
>
> Eu havia cravado "Windows 10 bloqueia a GPU do Foundry" a partir de **uma**
> sessão CLI que bateu em **dois** problemas e os juntei errado. O dono cobrou
> (corretamente) que eu distinguisse as camadas. Reinvestigando:
>
> 1. **Catálogo vazio na CLI ≠ Windows.** O log da própria extensão VSCode
>    (`.aitk/...openai.service.log`, hoje) mostra **"Loaded cached model info for
>    112 models"** + um erro **`429 TooManyRequests`** na Azure Foundry API. O
>    catálogo funciona (112 modelos cacheados); minha CLI pegou **rate-limit/DNS
>    transitório**, não um bloqueio de SO.
> 2. **WinML pulado ≠ sem GPU.** A mensagem "WinML requer build 26100" é só sobre
>    a **auto-seleção** de EP via Windows ML. O catálogo tem **40 modelos
>    `CUDAExecutionProvider`** e **32 `WebGpuExecutionProvider`** (DirectML/WebGPU,
>    que roda em **Win10 com qualquer GPU DX12** — a 3060 é). Eu confundi
>    "auto-EP WinML off" com "GPU indisponível".
> 3. **Eu nunca rodei um modelo local.** Sem isso, não havia base para o veredito.
>
> **Status correto: EM VERIFICAÇÃO.** Baixando `qwen2.5-coder-0.5b-instruct-cuda-gpu`
> (528 MB) para rodar e medir no nvidia-smi se a GPU engata. Variantes do
> qwen2.5-coder no catálogo Foundry: 0.5b/1.5b/7b/14b × {cuda-gpu, generic-gpu
> (WebGPU), generic-cpu} — o 7b-cuda-gpu (4843 MB) seria o par direto do Ollama.

### Diagnóstico definitivo (2026-06-04): NÃO é Windows 10 — é endpoint de catálogo morto na CLI

O log da CLI (`~/.foundry/logs/foundry20260604.log`) mostra:
```
Fetching model list from Azure Foundry catalog... → System.TimeoutException →
FLException: No models were returned from the Azure Foundry catalog.
```
E a resolução DNS:
```
catalog.azureml.ms   → resolve SEM endereço IP (host sem registro A) = MORTO
eastus.api.azureml.ms → 48.211.42.164 (OK)
management.azure.com  → 4.150.240.10 (OK)
```

**Causa-raiz**: a CLI winget **Microsoft.FoundryLocal 0.8.119.102** busca o catálogo
em `catalog.azureml.ms`, que **não tem registro A** (endpoint desativado/movido). A
extensão VSCode **windows-ai-studio 1.4.2** usa outro caminho (stack `Microsoft.Neutron`)
e tem **112 modelos cacheados** — por isso funciona na UI. **Não tem nada a ver com a
versão do Windows.** O `autoRegistrationStatus` do WinML (build 26100) é um aviso
separado e NÃO-bloqueante (há 32 variantes WebGPU/DirectML que rodam em Win10 DX12 +
40 CUDA no catálogo).

### Estado do teste de GPU: BLOQUEADO na aquisição do modelo (não no SO)
Não consegui baixar um modelo Foundry pela CLI (catálogo morto). Sem modelo, o teste
"a GPU engata no Win10?" fica em aberto — mas a evidência (variantes WebGPU/CUDA no
catálogo, DX12 na 3060) indica que **deveria** funcionar. Para FECHAR empiricamente,
o caminho é baixar 1 modelo pela **extensão VSCode** (que tem o catálogo vivo) e então
medir o nvidia-smi.

### Lição de método (registrada)
Eu cravei "Win10 bloqueia" juntando dois sintomas (WinML-skip + catálogo vazio) sem
isolar nenhum. O dono refutou. A refutação revelou: (a) catálogo = endpoint morto da
CLI, não SO; (b) WinML-skip ≠ sem-GPU. **É a mesma falha que o §6 do Strata previne
(default-cético, isolar variável) — e o mesmo padrão do `lab/aderencia-portabilidade`,
onde o adversarial derrubou achados por erro factual.** Conclusão prematura sem rodar
o artefato = exatamente o que a metodologia condena.

### Para a recipe (o que JÁ é conclusivo)
- **Ollama é o runtime local sem fricção**: CLI funciona, `ollama pull` limpo,
  55 t/s medidos. **Recomendado como default.**
- **Foundry Local via CLI winget (0.8.119) está quebrado** (catálogo morto) — usável
  só pela extensão VSCode. Pré-condição a documentar, NÃO um limite de Windows 10.

## GATE-2: status — ABERTO (por B1+B2; B4a em verificação)
- [x] B1 — decode 7B ≥40 t/s (55,5/50,7), IQR <0,5%, 100% GPU (4k e 16k).
- [x] B2 — VRAM linear medida (4,9/5,9/6,9 GB); penhasco a 32k e no 14B caracterizado.
- [ ] B4a — **em verificação** (retratada a conclusão prematura; testando GPU real
  do Foundry no Win10 via variante CUDA/WebGPU).

**B1+B2 sólidos.** Sweet spot Ollama: **qwen2.5-coder:7b @ ≤16k**. B4a em aberto.
