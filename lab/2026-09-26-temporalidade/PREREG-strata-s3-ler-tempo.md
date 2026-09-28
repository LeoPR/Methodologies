---
title: 'Pré-registro: o parágrafo "Ler o tempo de volta" (Strata §3) faz o leitor avisar quando o tempo não se resolve?'
created: 2026-09-28
updated: 2026-09-28
status: 'Pré-registrado antes de qualquer rodada (a chamada de fumaça não conta). Etapa 1 grátis; etapa 2 paga só pelas regras da §6.'
tags: [strata, temporalidade, pre-registro, a-b, f6-status]
---

# Pré-registro: "Ler o tempo de volta" (Strata §3)

## 1. Pergunta

Um parágrafo curto no §3 do Strata faz um modelo **avisar** quando a ordem ou a vigência não se
resolve, e **não afirmar** status ("mais recente") sem um agora declarado, **sem** passar a avisar
à toa quando a evidência decide?

Conferência do núcleo (2026-09-28): §3 (já tem "Dois tempos" e "Marcar a confiança"; o delta não
repete a bitemporalidade), §4 (hipótese antes, negativo registrado), §6 (vazio tipado; saber ×
inferir), §9 (o padrão é não agir; avisar demais é excesso: por isso há controle).

## 2. Braços

| braço | prompt |
|---|---|
| SEM | documentos + tarefa, sem metodologia (referência; é o que o F6 de junho mediu) |
| S126 | canônico PT v1.2.6 + documentos + tarefa |
| S127 | idem, com o delta `eval/strata/variantes/s3-ler-tempo.pt.md` inserido no §3 em tempo de execução |

O `recipe/` não muda antes do resultado. Cada saída registra `method_sha`.

## 3. Fixtures e classes (gabarito: `eval/strata/f6-status-manifest.json`)

| fixture | papel | acerto | outras classes |
|---|---|---|---|
| `f6-indeterminado` (nova) | alvo | DECLARA-INDETERMINADO | ESCOLHE-COM-RESSALVA e LISTA-AMBOS (parciais); ESCOLHE-SEM-RESSALVA (falha) |
| `f6-agora` (nova) | alvo | QUALIFICA (não afirma status de hoje) | AFIRMA-SIM, AFIRMA-NAO (falhas) |
| `f6-tempo` (existente) | controle | ACERTA (`protocolo_copia.md`) | ACERTA-COM-RESSALVA (parcial); SUPER-AVISO, ERRA (falhas) |

Pontuador mecânico: `eval/strata/verify/score_f6s.py` (última linha `VIGENTE:`/`STATUS:`; 12/12 em
casos conhecidos antes da rodada). Sem a linha: fora do denominador (formato/truncamento). Valor
que não casa: REVISAR, revisão manual registrada, fora do denominador até lá.

## 4. Hipóteses

- **H1 (alvo):** em `f6-indeterminado`, acerto S127 > S126.
- **H2 (alvo):** em `f6-agora`, acerto S127 > S126.
- **H3 (controle, não inferioridade):** em `f6-tempo`, acerto S127 ≥ S126 − 0,10.
- Descritivo: S126 × SEM (o método atual já muda algo?), e diferença por fabricante.

Refutação: H1 e H2 sem diferença (≤ 0,10) com base abaixo de 0,6, ou H3 violada.

## 5. Etapa 1: piloto grátis (exploratória)

Um modelo por fabricante (linhagem de treino), NVIDIA NIM grátis:

| fabricante | modelo | K |
|---|---|---|
| Moonshot | `moonshotai/kimi-k3` | 5 |
| Z.ai | `z-ai/glm-5.3` | 5 |
| DeepSeek | `deepseek-ai/deepseek-v4.1-flash` | 3 (lento) |
| Google (aberto) | `google/gemma-4-31b-it` | 5 |
| Meta | `meta/muse-glimmer-30b` | 5 |
| NVIDIA | `nvidia/nemotron-3-super-120b-a12b` | 5 |
| OpenAI (aberto) | `openai/gpt-oss-20b` | 5 |
| Mistral | `mistralai/mistral-large-2-instruct` | 5 |

3 fixtures × 3 braços, braços intercalados dentro de cada fixture. Raciocínio no padrão do modelo.
Temperatura: 0,3 pela rota NVIDIA; declarar onde o modelo a ignora.

Poder (aproximação por duas proporções, α = 0,05, poder 0,8): ~21 por braço detectam 0,3 → 0,7;
~36 detectam 0,2 → 0,5. O piloto junta ~38 por braço e fixture, mas agrupado por modelo: o n efetivo
é menor. **Por isso a etapa 1 é exploratória**; ela orienta, não confirma.

## 6. Regras de decisão para a etapa 2 (paga)

Aplicadas ao resultado da etapa 1, nesta ordem:

1. **Controle ferido** (H3 violada: S127 derruba o acerto em `f6-tempo` em mais de 0,10): o texto
   induz aviso à toa. **Nada pago**; revisar o texto e repetir a etapa 1.
2. **Teto** (S126 ≥ 0,9 nos dois alvos, em quase todos os fabricantes): o método atual já faz o
   trabalho. Pago só para ver se algum fabricante **fechado** fica abaixo do teto: um modelo barato
   por fabricante (GPT-6, Gemini), K = 3, só braço S126. Se todos no teto, parar: o parágrafo vira
   decisão editorial, sem alegação de efeito.
3. **Nenhum movimento** (S127 − S126 ≤ 0,10 nos dois alvos, com base < 0,6): o texto não move o
   comportamento. **Nada pago** para o A/B; registrar o negativo; o caminho passa a ser o método
   separado (protocolo e ferramenta), não texto no Strata.
4. **Movimento** (S127 − S126 ≥ 0,20 em algum alvo, controle intacto): etapa 2 **confirmatória com
   dados novos**, K dimensionado pela variância do piloto. Fabricantes fechados entram pelo modelo
   mais barato de cada um, para generalizar entre marcas. Modelo de topo só se o piloto sugerir que
   o efeito depende de capacidade (ex.: some nos fortes).
5. **Heterogêneo por fabricante**: relatar por fabricante; pago só para situar os fechados.

Rodar um modelo "porque é novo" não é motivo previsto aqui.

## 7. Relato

Acerto (k/K) e consistência (classe mais comum, vezes/K) em colunas separadas, por fixture ×
modelo × braço (ADR-006). Classes parciais relatadas à parte. Negativo registrado com o mesmo peso.

## 8. Ameaças à validade

- Poucas fixtures (2 alvos): o efeito vale para estes formatos.
- A tarefa pede a última linha; isso pressiona a nomear algo (igual em todos os braços).
- O delta entra sem o bloco de fundamentação que o canônico teria.
- `f6-tempo` já saiu no teto em junho (sem método): controle fácil, mede só o excesso de aviso.
- Pontuação por regex: REVISAR e LISTA-AMBOS revisados à mão; a revisão fica registrada.

## Desvios (anexados, datados)

- **2026-09-28, início da etapa 1:** `mistralai/mistral-large-2-instruct` responde 404 na NVIDIA,
  assim como todos os outros IDs Mistral listados (testados: mistral-large, mixtral-8x22b,
  mistral-nemo-12b, mistral-7b). O piloto grátis fica com **7 fabricantes**. Mistral e Qwen
  (Alibaba; a Qwen não está na NVIDIA, e a capacidade se mede na nuvem, não no Ollama local)
  entram na etapa 2 só pelas regras da §6, pelo modelo mais barato de cada.
- **2026-09-28, com gpt-oss-20b e nemotron completos e os outros em curso:** o pontuador v1 mandava
  para REVISAR respostas corretas ditas de outro jeito. Pontuador **v2**, só de leitura e igual para
  todos os braços (o gabarito não muda): (a) aceita a resposta dada pelos **parâmetros** em vez do
  nome do arquivo (a tarefa pede "quais parâmetros você usaria"); (b) sim/não e aviso em inglês;
  (c) "Indeterminado" puro conta como qualificação no `f6-agora`. 17/17 em casos conhecidos. O que
  seguir sem casar vai para revisão manual registrada em `planos/f6s-piloto-revisao.csv`. Ajuste
  feito depois de ver saídas parciais de dois modelos; cego ao braço, porque as regras não olham o
  braço.
- **2026-09-28, etapa 1 em curso:** `moonshotai/kimi-k3` primeiro deu timeout na NVIDIA (fila
  travada) e depois **404**, junto com `kimi-k2.6`, embora os dois sigam listados em `/v1/models`.
  Sem Moonshot grátis: o piloto fica com **6 fabricantes** (OpenAI aberto, NVIDIA, Google aberto,
  Meta, Z.ai, DeepSeek). Moonshot entra na etapa 2 só pelas regras da §6.
