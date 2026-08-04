---
name: proposta-s9-quando-nao-agir
type: lab-proposta
status: proposta-aguardando-dono
created: 2026-08-03
updated: 2026-08-03
audience: ai-primary
applies-to: proposta de revisao pontual do §9 (L0 fechado; requer aprovacao do dono)
---

# Proposta: o §9 precisa dizer "quando não agir"

Origem: ticket do backlog (`lab/2026-06-04-strata-hipoteses/BACKLOG-fila-geral.md`),
aberto pela evidência do estudo do prompt ingênuo (`RESULTADOS.md` nesta pasta).

## A evidência

No clean (fixture sem defeito, resposta certa = não mexer), medido com scorer
mecânico, 4 modelos, K=5 na célula decisiva:

- braço strata: 7/14 de abstenção correta (50%);
- braço bare (bom senso instruído): 9/14 (64%);
- escada de instrução leiga E0-E2: 50-64%;
- frase leiga N2 ("Organize este projeto da melhor forma possível."): 16/20 (80%).

Leitura: o método hoje não entrega calibração de "não agir" superior a uma frase
leiga bem redigida. O falso positivo é propriedade de modelo e de redação. Como o
Strata se propõe a ser o que torna o comportamento confiável, essa lacuna é dele,
não dos modelos.

## A lacuna no texto (§9, `recipe/knowledge-architecture.en.md`)

O §9 ("Economy of effort: when to organize and when not to") regula dois eixos:
quanto organizar (distância ao leitor) e qual padrão exigir (gênero do trabalho).
Ambos operam sobre **produzir/organizar**. Em nenhum ponto o L0 diz o caso
simétrico: ao **avaliar uma base existente para agir sobre ela**, o veredito
default de uma avaliação honesta é **não mudar nada**, a menos que um defeito real
pague o conserto. Hoje essa instrução existe só nas tarefas do harness F4
("ABSTENHA-SE"), não no método; ou seja, o eval cobrava um comportamento que o
produto não ensina. Isso explica por que o braço strata não calibra melhor que o
leigo: nunca dissemos a ele que não-agir é um deliverable.

## Proposta (mínima, aditiva; EN canônico + PT derivado no mesmo commit)

Acrescentar ao §9, após o parágrafo do regulador por gênero:

> **Acting on what already exists obeys the same economy.** Evaluating a base in
> order to change it has the same cost-benefit shape as organizing it: the
> default verdict of an honest evaluation is **no change**, unless a real defect
> pays for the fix. Inventing work where nothing is broken is §9 excess on the
> action axis: it spends the reader's trust and the project's history (§8) on
> noise. Name the defect first; if there is none, the deliverable is the
> statement that there is none.

PT (derivado):

> **Agir sobre o que já existe obedece à mesma economia.** Avaliar uma base para
> alterá-la tem a mesma forma de custo-benefício de organizá-la: o veredito
> default de uma avaliação honesta é **não mudar nada**, a menos que um defeito
> real pague o conserto. Inventar trabalho onde nada está quebrado é excesso de
> §9 no eixo da ação: gasta a confiança do leitor e a história do projeto (§8)
> com ruído. Nomeie o defeito primeiro; se não houver, o entregável é a
> declaração de que não há.

E a linha de era-instance do §9 ganha um ponteiro para este estudo
("`lab/2026-08-03-prompt-ingenuo/RESULTADOS.md`"), marcado como sinal forte não
circular (scorer mecânico, fixtures sintéticas, 4 modelos, K=5).

## Gate

O L0 está editorialmente FECHADO (ciclo P1-P5, `lab/2026-08-01-fechamento-camadas/`).
Esta proposta NÃO aplica a mudança por conta própria: fica aqui registrada com o
texto pronto. Aplicar = decisão do dono; ao aplicar, editar EN + PT no mesmo
commit (ADR-008) e bumpar o `updated:` dos dois. Se aprovada, re-teste dirigido
barato: rodar a grade f4-clean (strata) PT+EN e comparar a abstenção antes/depois
(a expectativa é subir de ~50% para o regime do N2, ~80%).
