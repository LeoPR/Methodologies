---
title: H17 — Custo de visão (imagens) e roteamento por modalidade
created: 2026-06-04
status: hipótese registrada (avaliação adiada — não executada)
tags: [visao, vision, imagens, tokens, roteamento, modalidade, local-llm, ollama]
relates: [mapa-recursos-llm.md (P4/P17/P23), plano-experimental.md (cluster E)]
---

# H17 — Custo de visão e roteamento por modalidade

> **Hipótese para avaliar DEPOIS.** Registrada agora a pedido do dono. Não foi
> executada. Estende o modelo de primitivas do `mapa-recursos-llm.md` com uma
> dimensão nova: **modalidade** (texto vs imagem) como peso de roteamento.

## A pergunta

1. **Quanto custa (em tokens) mandar uma imagem** para os modelos cloud
   (Anthropic / OpenAI / Google) para "ver" algo?
2. **Qual a qualidade de um mecanismo de visão LOCAL** para a mesma tarefa?
3. **Isso otimiza?** No roteamento geral ("o que vale a pena mandar ao modelo
   caro"), a imagem é um peso específico — talvez um modelo de visão local possa
   **pré-processar** a imagem (descrever/OCR/extrair) e mandar só o **texto
   relevante** ao modelo caro, em vez da imagem inteira.

## Por que importa (conexão com o mapa)

Imagens são uma **modalidade de input com estrutura de custo própria**. Isto é o
**análogo visual** do que já vimos comprovado para texto:
- **P23** (reduzir tokens de input) — uma imagem pode custar centenas/milhares de
  tokens; descrevê-la localmente e mandar 50 tokens de texto é a mesma economia.
- **P4 / PROCONSUL / LLMLingua** (pré-filtro local → cloud) — "visão local descreve
  → texto vai pro cloud" é o mesmo padrão de compressão local antes da API cara.
- **P17** (cascata barato→caro) — visão local resolve o trivial (OCR, "tem um gato?"),
  cloud só para o que exige raciocínio visual fino.

Acrescenta ao modelo de primitivas uma **4ª dimensão de roteamento**: além de
*tarefa × hardware × custo*, agora *modalidade* (a imagem entra inteira, ou vira
texto antes?).

## O que avaliar (quando for a hora)

### Eixo 1 — custo de tokens-por-imagem dos providers (factual, citável)
Levantar a fórmula de cada um (todos cobram por "tiles"/blocos, não por arquivo):
- **Anthropic**: tokens ≈ (largura×altura)/750 (aprox.), com teto por imagem.
- **OpenAI**: base + tiles de 512px (low/high detail muda muito o custo).
- **Google Gemini**: custo por imagem/tile próprio.
- Converter para o regime do dono (Max = quota; Copilot = créditos por imagem).

### Eixo 2 — qualidade da visão local (o dono JÁ TEM os modelos)
No Ollama do dono, testáveis na RTX 3060:
- `llama3.2-vision:11b` (7,8 GB) — provável penhasco de VRAM (>11B); medir.
- `qwen3-vl:8b` (6,1 GB) — deve caber estável (faixa do 8B).
Tarefas de bateria graduada: OCR de screenshot, descrição de diagrama, extração
de dados de tabela/gráfico, "o que há de errado nesta UI?". Comparar com cloud.

### Eixo 3 — o padrão "visão local → texto cloud" economiza sem perder qualidade?
Experimento (análogo ao D3 de pré-sumarização): 
- Controle: imagem inteira → cloud (custo de tokens-imagem + resposta).
- Tratamento: imagem → descrição local (qwen3-vl) → texto → cloud.
- Medir: tokens cloud economizados VS perda de qualidade (a descrição local
  perde detalhe que a tarefa precisava?).
- Gatilho de quando vale: tarefa que precisa do **conteúdo semântico** da imagem
  (OCR, "qual o erro no log da screenshot") → local descreve bem; tarefa que
  precisa de **raciocínio visual fino** (layout, estética, diagrama complexo) →
  mandar a imagem inteira ao cloud.

## Veredito provável (a confirmar)
Mesma forma do resto do mapa: **DEPENDE** da tarefa. Visão local como **pré-filtro**
deve ganhar em OCR/extração (alto sinal, baixo raciocínio); cloud-direto ganha em
raciocínio visual fino. O número (quanto economiza, onde quebra) é **não-sabível a
priori — só medindo**. Entra como candidato a experimento no cluster E (matriz de
roteamento), agora com a coluna "modalidade".

## NÃO pesquisar agora
- Fine-tuning de modelos de visão.
- OCR clássico (Tesseract) vs LLM-visão — fora do escopo de "otimizar uso de IA".
