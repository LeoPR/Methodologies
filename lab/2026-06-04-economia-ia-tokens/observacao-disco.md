---
title: Observação de disco — o custo persistente dos modelos (evidência de 1ª mão)
created: 2026-06-04
source: docker inspect / docker system df na máquina do dono
---

# Observação de disco — a condição esquecida, medida

> Evidência de primeira mão da máquina do dono. Materializa a "condição esquecida"
> (modelos ocupam disco; frameworks duplicam) que motivou o ciclo de revisão.

## O que foi medido

| Item | Tamanho | Onde |
|---|---|---|
| **Modelos Ollama (25 modelos)** | **118,5 GB** | `M:\ollama\models` (bind-mount Docker) |
| Imagens Docker | 25,5 GB (4,9 reclaimable) | data-root Docker |
| Build cache Docker | 15,4 GB (**10,5 reclaimable**) | data-root Docker |
| `.aitk` (Foundry/AI Toolkit) | 0,32 GB (só catálogo, 0 modelos) | C:\Users\leona |
| `~/.ollama` (Windows) | **0 GB** (vazio!) | — |

Volumes: C: 206GB livre · D: 587 · **M: 423** · Z: 1502.

## Os achados que provam o ponto

1. **O store é grande e INVISÍVEL no lugar óbvio.** `~/.ollama` está vazio porque o
   Ollama roda em **Docker** com os modelos **bind-montados em `M:\ollama\models`**
   (118,5 GB). Quem procurasse no caminho default (`~/.ollama`) não acharia nada — o
   custo de disco está deslocado e oculto. O dono fez a coisa CERTA (relocou p/ um
   volume grande); o caminho "automático" teria enterrado isso num `.vhdx` no C:.

2. **118,5 GB mataria o dev médio.** Num SSD de 256-512GB (a norma — ver pesquisa de
   hardware), 118GB de modelos é inviável. É a primitiva **MEMÓRIA-DISCO-PERSISTENTE**
   dominando a decisão, não a VRAM nem os tokens.

3. **Duplicação é risco real, ainda não materializado aqui.** `.aitk` tem só 0,32GB
   (catálogo, nenhum modelo ONNX baixado). SE o dono baixasse o qwen2.5-coder pelo
   Foundry (ONNX), seria um arquivo SEPARADO do GGUF do Ollama — o MESMO modelo,
   disco dobrado, porque ONNX ≠ GGUF (formatos não compartilháveis).

4. **~15 GB recuperáveis agora** (`docker system prune` + build cache) sem perder modelo.

5. **Higiene possível**: dos 25 modelos, quantos são realmente usados? gpt-oss (13GB),
   phi4 (9GB), gemma3:12b (8GB), múltiplos deepseek/qwen — provável "modelo morto"
   ocupando dezenas de GB. A higiene de store (remover não-usados) é um movimento de
   economia de disco análogo ao "rebaixar a superfície" do §3 do Strata.

## Para a síntese (primitiva re-derivada)

Isto vira parte da primitiva **MEMÓRIA** no eixo **DISCO-PERSISTENTE**:
- footprint do modelo (GGUF Q4 ~0,5GB/B de params; gpt-oss 13GB)
- multiplicado por nº de frameworks que NÃO compartilham formato (Ollama-GGUF vs
  Foundry-ONNX vs safetensors)
- menos o que o volume comporta (256GB SSD vs M:/Z: grandes)
- mais o overhead oculto (Docker images + build cache + vhdx que não encolhe sozinho)

Movimento novo para a árvore/protótipo: **sondar disco livre + localizar os stores de
modelo (incl. Docker bind-mounts) + sinalizar duplicação e reclaimable**.
