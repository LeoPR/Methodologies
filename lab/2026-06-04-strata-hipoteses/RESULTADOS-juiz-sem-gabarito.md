---
title: 'O gabarito no prompt do juiz infla a concordância? (ablação com juízes atuais)'
created: 2026-06-20
updated: 2026-06-20
status: 'FEITO (Fase B) — sim, infla. Sem o gabarito, juízes atuais caem abaixo do baseline. Confirma a ressalva com número.'
---

# O gabarito no prompt do juiz infla a concordância?

## A pergunta

A concordância alta entre juízes no F4 (α = 0,918, ver [RESULTADOS-concordancia-juizes.md](RESULTADOS-concordancia-juizes.md)) pode vir, em parte, de dois juízes que **já receberam o resumo da resposta** no prompt.
Esta é a Fase B do bloco barato: medir o quanto o gabarito no prompt sustenta o acerto.

## O desenho

Rodamos juízes de **geração atual**, não os datados gemini-2.5-flash e gpt-4.1, sobre os **mesmos 36 planos do F4**, em duas condições:
- **com resumo**: o juiz recebe o resumo da situação, como antes;
- **sem resumo**: o juiz vê só o fix emitido pelo modelo.

Cada veredito é comparado com o **gold mecânico objetivo** (`verify_f4`), num eixo binário: o juiz acerta se a sua disposição "correto" bate com o gold "correto" (PASS ou ABSTENCAO_CORRETA).
Juízes: gemini-3-flash-preview e gpt-5-mini. Código em [`eval/strata/judge_f4_ablation.py`](../../eval/strata/judge_f4_ablation.py). Custo: US$0,20.

A taxa-base importa para ler o número.
Dos 36 itens, 14 são gold-correto (0,389), então **o baseline da classe majoritária é 0,611**: um juiz burro que sempre diz "incorreto" acerta 61%.

## O resultado

| Juiz (atual) | Condição | Acerto vs gold | κ vs gold |
|---|---|---|---|
| gpt-5-mini | com resumo | **0,806** | **0,625** |
| gpt-5-mini | sem resumo | 0,556 | 0,226 |
| gemini-3-flash | com resumo | 0,667 | 0,393 |
| gemini-3-flash | sem resumo | 0,556 | 0,226 |

Concordância **entre os dois juízes** (não com o gold): com resumo κ = 0,700; sem resumo κ = 0,600.

## A leitura honesta

**O gabarito no prompt infla o acerto, e bastante.**
Tirar o resumo derruba o κ contra o gold dos dois juízes: o gpt-5-mini cai de 0,625 para 0,226, e o gemini cai de 0,393 para 0,226.
Sem o gabarito, os dois pousam no mesmo lugar fraco.

**Sem o gabarito, o juiz fica abaixo do baseline burro.**
A 0,556 de acerto, os dois juízes cegos ficam **abaixo** do 0,611 que se obtém só chutando "incorreto" sempre.
Cegos de contexto, eles não são informativos neste eixo binário.

**A concordância entre juízes não prova que eles estão certos.**
Mesmo sem o gabarito, os dois juízes ainda concordam um com o outro (κ = 0,600), mas concordam nas respostas **erradas**.
Isto é o aviso metodológico central: o α alto de 0,918 da Fase A mede juízes que **convergem**, e parte dessa convergência vem do gabarito compartilhado e de pontos cegos compartilhados, não de acerto.
Concordar não é o mesmo que acertar. Quem revela o acerto é a comparação com o gold.

**Com o gabarito, o juiz forte é genuinamente útil.**
O gpt-5-mini com resumo tem κ vs gold de 0,625 e acerto de 0,806, bem acima do baseline.
O gabarito não é trapaça: é o contexto que um avaliador justo precisa ter. O ponto é que a confiabilidade é **condicional** a esse contexto.

## A ressalva que limita a conclusão

Tirar o resumo remove a dica **e** o contexto legítimo da tarefa ao mesmo tempo.
Nos casos f4-clean e f4-trap, sem saber a situação do projeto, o juiz **não tem como** saber se abster-se era o certo, ou se havia uma armadilha a evitar.
Por isso a queda é um **limite superior** do "vazamento de gabarito", não a medida pura.
O teste mais justo daria ao juiz o **fixture original** (o contexto da tarefa) sem a resposta esperada. Fica registrado como o próximo refino.

## O que isto muda, e o que não muda

Isto **confirma com número** a ressalva que o corpus já carregava: a concordância dos juízes é medida com o gabarito no prompt, então não é julgamento cego.
A Fase A media a concordância; a Fase B mostra que ela é, em parte, condicional ao gabarito.

Isto **não** derruba o núcleo sólido (§5-conserto, §3-tombstone).
Esse núcleo não repousa no juiz, e sim no **gold mecânico** (o GOLD-gate de 100%, ação de arquivo objetiva).
O juiz entra só como refinador do resíduo, e no pipeline real ele sempre tem o gabarito.
A lição é sobre **o que o juiz sozinho prova**, não sobre a solidez do conserto.

## Reprodução

```
OPENROUTER_API_KEY=... python eval/strata/judge_f4_ablation.py
```

Grava `eval/strata/planos/f4-ablation-gabarito.json` com a disposição por (plano, juiz, condição) e imprime a concordância com o gold por juiz e condição.
