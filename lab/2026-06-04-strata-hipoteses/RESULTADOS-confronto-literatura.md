---
title: 'Confronto dos achados de juiz com a literatura atual (2024-2026)'
created: 2026-06-21
updated: 2026-06-21
status: 'FEITO — confronto eixo a eixo do DOSSIE-judge com literatura 2024-2026 (deep-research verificado). Um eixo CONTRADITO (cross-vendor), dois CORROBORADOS no centro, três a rebaixar/atualizar.'
nota: 'Fontes 2026 são preprints (Apple, RAND), tratar número específico como melhor-atual, não assentado. IDs arXiv conferidos por existência na busca; reconferir antes de citação externa.'
---

# Confronto dos achados de juiz com a literatura atual

> Traço datado. Registra o que a literatura recente faz com cada eixo do
> [DOSSIE-judge](DOSSIE-judge-justificativa-cientifica.md). Levantamento por harness de
> pesquisa multi-fonte com verificação adversarial (27 fontes, 119 afirmações, 25 verificadas
> por voto 2/3, 21 confirmadas). A leitura de superfície consolidada entra no DOSSIE e na OPINIAO;
> aqui fica o diário do confronto.

## O veredito em uma frase

A literatura de 2024-2026 **corrobora o núcleo epistêmico** (concordância não é correção; gabarito
melhora o juiz; correção por acaso bate o % cru), e **recalibra de binário para escala** a defesa que
tínhamos da convergência cross-vendor: ela não é abolida, é **quantificada** (votos efetivos
independentes, neff), e deixa de valer como prova de correção.
O fundamento filosófico-matemático dessa recalibração (teto de informação vs lacuna de capacidade,
escala mensurável vs binário perfeito/impossível) está em
[FUNDAMENTO-juiz-escala-mensuravel.md](FUNDAMENTO-juiz-escala-mensuravel.md).

## Eixo a eixo

### Eixo 1 — júri cross-vendor: RECALIBRADO (de binário para escala)

Nossa tese antiga, binária: juízes de fabricantes distintos que convergem provavelmente acertam.
A literatura nova não diz "cross-vendor não vale"; diz que **diversidade de fornecedor reduz, mas não
elimina, erro correlacionado**, e dá o instrumento para medir o quanto. Independência vira **quantidade**
(votos efetivos), não chave liga/desliga.

- **Kohli et al. (Apple), 2026 — "Nine Judges, Two Effective Votes"** (arXiv:2605.29800).
  Painel de 9 juízes em 7 famílias rende só **~2,18 votos efetivamente independentes** (IC95% [2,07, 2,31]).
  Os três pares **mais** correlacionados são **cross-família** (Claude×Gemini φ=0,603; GPT-4o×Claude φ=0,588;
  Mistral×DeepSeek φ=0,564). Seleção família-diversa *reduziu* a independência efetiva (1,93 vs 2,18).
  O painel não bateu de forma confiável o melhor juiz único.
- **Kim et al., ICML 2025** (arXiv:2506.07962). Em 350+ LLMs, "modelos maiores e mais acurados têm erros
  altamente correlacionados, mesmo com arquiteturas e fornecedores distintos". Concordam ~60% das vezes
  *quando ambos erram*.

**O que muda:** a frase "convergem → provavelmente correto" sai. A convergência cross-vendor vira
**proxy fraco de independência** que mitiga self-preference (Verga/PoLL 2024, Panickssery 2024 seguem válidos
para isso), **não garantia de correção**. As citações antigas permanecem para a *mitigação de viés*, não para
*correção por consenso*.

### Eixo 2 — convergência ≠ correção: CORROBORADO (nosso ponto mais forte)

A Fase B ([RESULTADOS-juiz-sem-gabarito.md](RESULTADOS-juiz-sem-gabarito.md)) mediu juízes que seguem
concordando (κ=0,600) **nas respostas erradas** sem o gabarito. Isso é o mecanismo de *shared blind spot*
que Kim et al. (2506.07962, §4) medem como "accuracy inflation": o juiz infla o acerto quando os modelos
julgados convergem na mesma resposta errada. Ironia útil: **a mesma literatura que contradiz o Eixo 1
confirma o Eixo 2**.

### Eixo 3 — gabarito no prompt infla o juiz: CORROBORADO (nossa contribuição mais atual)

κ 0,625 (com gabarito) → 0,226 (sem) tem lastro forte e recente:
- **No Free Labels**, 2025 (arXiv:2503.05061): juízes concordam com especialistas só nas questões que eles
  próprios saberiam responder; referências de especialista "largamente mitigam" o gap; LLM-as-judge não
  confiável sem ancoragem humana em domínios de correção/alto risco.
- **RevisEval**, ICLR 2025 (arXiv:2410.05193): referências adaptadas à resposta batem tanto o reference-free
  quanto o reference-based; o gap vem de "falta de oráculos guiados".
- **Judge's Verdict**, 2025 (arXiv:2510.09738) reforça reference-guided.

**Nuance (qualificador, não refutação):** com juízes muito fortes (GPT-4) o gap reference-free encolhe para
"comparável", e referência ruidosa pode enganar. Nossa queda é maior que o efeito do RevisEval, mesma direção.

### Eixo 4 — correção por acaso: princípio CORROBORADO, thresholds NÃO verificados

**Judge's Verdict** (2510.09738) estabelece que "correlação sozinha é insuficiente" e progride para κ de Cohen —
confirma o princípio (corrigir por acaso > % cru) e o paradoxo da prevalência.
**Item aberto honesto:** a busca **não** confirmou que os limiares de Krippendorff (≥0,800 confiável;
0,667-0,800 preliminar) sigam sendo consenso para juiz-LLM, nem achou crítica recente a κ/α *específica* para
avaliação de LLM. Tratar os números de corte como heurística clássica, não como consenso atual verificado.

### Eixo 5 — objetividade do alvo prevê concordância: CORROBORADO

**RAND, "Judge Reliability Harness"**, 2026 (arXiv:2603.05399): "nenhum juiz é uniformemente confiável entre
benchmarks"; "nenhum modelo é uniformemente robusto a perturbações". A confiabilidade é **dependente de tarefa**,
não propriedade estável do modelo. Bate com F4 (alvo de ação de arquivo, α=0,918) vs F3 (texto ambíguo, α=0,467).
Caveat: a fonte mede variância por benchmark, não um eixo limpo de "objetividade".

### Eixo 6 — calibração / ECE: NÃO verificado nesta passada

Guo et al. 2017 e Tian et al. 2023 **não** foram confirmados nem atualizados pelos claims sobreviventes da
verificação. A afirmação "ECE é eixo ortogonal à concordância" segue plausível, mas **sem lastro novo** neste
confronto. Rebaixar de "fundamentado" para "plausível, não reconfirmado"; o ECE genuíno segue bloqueado
(juiz emite rótulo, não probabilidade).

### Eixo 7 — vieses de juiz: ATUALIZAR

Self-preference agora se divide em **justificado** (saída própria de fato melhor) **vs injustificado** (viés):
**Breaking the Mirror**, NeurIPS 2025 (arXiv:2509.03647) — *activation steering* reduz o injustificado em até 97%.
Favorecer a própria saída **nem sempre é erro**. Isso **refina** (não refuta) o Eixo 2. Panickssery 2024 e
Zheng 2023 seguem válidos para a *existência* do self-preference (GPT-4 reconhece a própria saída a 73,5%).

### Eixo 8 — discordância humana como sinal: NÃO corroborado nesta passada

Aroyo & Welty 2015 não teve confirmação recente verificada aqui. Não foi refutado; só não foi modernizado.
Fica como item aberto se formos publicar o argumento de ground-truth distribucional.

## O que foi REFUTADO na verificação (não citar como prova)

- "Painel de múltiplos juízes melhora confiabilidade sobre juiz único" (voto 0-3 contra a fonte 2408.09235).
- "Reference-Guided Verdict correlaciona forte com humano em QA livre" (0-3).
- "TALE reference-free com ferramentas bate reference-based" (1-2).
- "Self-preference é causado linearmente pela auto-recognição" (1-2).

Implicação: **não** super-citar PoLL/painel como evidência de *qualidade*; o painel serve a *independência parcial*
e *mitigação de self-preference*, não a "mais juízes = mais acerto".

## Ações no corpus (feitas em 2026-06-21)

1. Eixo A do [DOSSIE-judge](DOSSIE-judge-justificativa-cientifica.md) reescrito: convergência cross-vendor é
   proxy fraco de independência, não correção. Caveat de erro correlacionado cross-família adicionado.
2. Bibliografia canônica atualizada com as obras citadas que faltavam + as novas (ver
   [bibliography.methodology.md](../2026-06-03-modernizacao/experimento-split/bibliography.methodology.md)).
3. [OPINIAO-DE-USO.md](OPINIAO-DE-USO.md): a linha de juízes deixa de sugerir "convergem → correto".
4. Escada de juízes do F0 marcada como snapshot datado (L2).
5. Eixo 6 (ECE) rebaixado para "plausível, não reconfirmado"; thresholds de Krippendorff marcados como
   heurística clássica, não consenso atual verificado.

## Itens abertos que este confronto deixa

- Replicar erro-correlacionado cross-vendor no nosso domínio (QA livre, recusa de injeção): os números da
  literatura são de NLI/segurança, podem não transferir a magnitude.
- Reconferir o consenso atual dos limiares de Krippendorff para juiz-LLM.
- Atualizar o estado de calibração/ECE de juiz (eixo 6) com fonte 2025-2026.
- Modernizar o argumento de ground-truth distribucional (eixo 8) pós-Aroyo & Welty.
