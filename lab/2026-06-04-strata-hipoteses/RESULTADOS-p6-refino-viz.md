---
title: P6 — refino do piso portátil (F1.5) + suíte de visualizações
created: 2026-06-08
status: F1.5 NÃO levantou os break-even (a fronteira é dura); 4 gráficos consolidam todos os dados coletados
---

# P6 — refino #1 (F1.5) e a suíte de gráficos

## Refino #1 — F1.5 "checklist+" (etapas forçadas num único prompt)

**Hipótese:** forçar o modelo a escrever as etapas (forças → linha-do-tempo → gates → priorizar)
DENTRO de um único prompt captura o ganho do guiado (F4) sem perder portabilidade. **Alvo:**
tirar gpt-4.1-mini / gemini-flash de ~0 para positivo.

**Resultado — NÃO funcionou** (qualidade média, 2 projetos, N=2):

| modelo | F1 (checklist) | **F1.5 (checklist+)** | F4 (multi-turn) |
|---|---|---|---|
| gpt-4.1-mini | 0.00 | **−0.25** | 0.00 |
| gemini-2.5-flash | −0.25 | **−0.25** | 0.00 |
| deepseek-v3 | −2.25 | **−1.00** | +0.50 |

Forçar as etapas num prompt **não** levou os break-even ao positivo — gemini segue bimodal
(pdf2md +1.5 / NNN −2.0; não ganha a RESTRIÇÃO no projeto limpo). Só o **F4 multi-turn de
verdade** captura o ganho (deepseek +0.5).

**Conclusão (importante):** o benefício das etapas vem da **separação em TURNOS** — obrigar o
modelo a *comprometer-se* com "o que é bom" e "a linha do tempo" em respostas separadas antes
de diagnosticar — **não das instruções em si**. Isso **não cabe num prompt portátil**. A
fronteira "cheap + portátil + bom = escolha dois" é **dura**: prompt-engineering sozinho não
fura o teto dos baratos. O **checklist (F1) é o piso portátil**; além dele, ou multi-turn (F4)
ou capacidade (Opus).

## Suíte de visualizações (4 gráficos, SVG sem dependências)

| arquivo | tipo | o que mostra |
|---|---|---|
| [VIZ-p6-scatter.svg](VIZ-p6-scatter.svg) | scatter | custo × qualidade (12 modelos) + setas verdes do ganho F4. **A fronteira de Pareto.** |
| [VIZ-p6-candle.svg](VIZ-p6-candle.svg) | candlestick | **faixa de variação** por modelo (min..max nas 4 células) + pontos por projeto (vermelho=NNN, azul=pdf2md). Revela a **bimodalidade** que a média esconde. |
| [VIZ-p6-bubble.svg](VIZ-p6-bubble.svg) | bubble | custo × qualidade × **inconsistência** (tamanho da bolha = amplitude/risco) × operadora (cor). 5 vetores num gráfico. |
| [VIZ-p6-forms.svg](VIZ-p6-forms.svg) | linhas | **vetor orientação**: qualidade × forma (F0→F4) por modelo. O salto é F0→F1; depois, retorno decrescente (exceto deepseek no F4). |

**O que os gráficos novos acrescentaram ao scatter:**
- **Candlestick:** a "qualidade" de um modelo é **bimodal por tipo de projeto** — quase todos
  são piores no exemplar limpo (NNN, onde qualquer achado é falso-positivo) do que no messy
  (pdf2md, com problemas reais). O **gpt-4.1-mini** tem amplitude **0** (consistente, sempre
  neutro = o "piso seguro"); o **gemini-flash** tem amplitude **4** (aposta: ótimo no messy,
  péssimo no limpo); o **gpt-4.1-nano** amplitude **7** (caótico). **Opus** é o único positivo
  e consistente.
- **Bubble:** torna a **inconsistência/risco** uma dimensão de 1ª classe — bolhas grandes
  (gemini, gemini-lite, deepseek-r1, gpt-nano) = imprevisíveis; bolha pequena perto de 0
  (gpt-4.1-mini) = seguro; bolha pequena alta (Opus) = bom e estável.
- **Forms:** a tutoria tem **retorno decrescente** — o ganho real é largar o texto cru (F0)
  por um checklist (F1); F1.5/F2 não melhoram; F4 só ajuda quem tem capacidade de aproveitá-lo
  (deepseek).

## Caveats
- F0/F1/F2/F4 (no gráfico de formas) são N=1 (Fase A); F1/F1.5 N=2 — há ruído de N pequeno.
- Custo = proxy $/M (in×0.9 + out×0.1). Qualidade = genuíno − falso-positivo (gabarito corrigido).
- SVGs gerados por `gen_scatter.py` / `gen_charts.py` / `gen_forms.py` (puro Python, sem deps).
