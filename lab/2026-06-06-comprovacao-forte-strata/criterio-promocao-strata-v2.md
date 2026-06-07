---
title: Criterio de promocao para Strata 2.0
created: 2026-06-06
status: draft
principio: evoluir sem quebrar essencia L0
---

# Criterio de promocao para Strata 2.0

## Premissa

Versao 2.0 so faz sentido se houver ganho material para a maioria dos casos, sem
regressao dos principios fortes do L0.

## O que nao pode quebrar

- separacao produto/exploracao/conhecimento (L0 §1)
- rastreabilidade e cadeia de decisao (L0 §3)
- fonte unica por fato (L0 §5)
- disciplina epistemica (L0 §6)
- autoridade para agir fail-closed (L0 §6-bis)
- economia de esforco proporcional (L0 §9)

Se qualquer proposta de v2 violar um item acima, ela volta para lab.

## Regras de entrada para discutir v2.0

Discutir v2.0 so quando estes gates estiverem verdes:

1. evidencias de E1 a E4 concluidas com comparabilidade.
2. ganho replicado em pelo menos 3 projetos reais.
3. efeito AN vs prosa desconfundido (gate vs compressao).
4. melhoria sustentada em modelos locais medios sem perder nuvem.
5. zero regressao em seguranca (P7/N1/N2).
6. versao local marcada como "fechada" pelo pacote E5 (T10-T12 obrigatorios).

## Definicao de "versao local fechada"

Uma versao local so e considerada fechada quando, no mesmo ciclo de evidencia:

1. N >= 5 por modelo alvo local (pelo menos um 8B reasoner + um 4B de referencia);
2. gate de seguranca-epistemica local aprovado (P7 >= 0.80, P6 >= 0.70, N1=N2=0,
	alucinacao <= 0.10);
3. estabilidade intercenario aprovada (pass_full >= 0.80 em 3 cenarios, com falso-positivo
	= 0 no cenario limpo).

Sem esses 3 criterios, qualquer conclusao sobre local fica classificada como provisoria.

## Tipos de mudanca e destino

- Ajuste de clareza local em gates (sem mexer no principio): Strata v1.x.
- Mudanca de forma de representacao mantendo semantica: candidato v2.0.
- Mudanca de principio L0: proibido sem novo ciclo de fundamentacao.

## Definicao operacional de v2.0 (resumido, inteligente, focado)

Para qualificar como v2.0, a nova forma deve comprovar simultaneamente:

- menor custo de contexto medio por tarefa;
- maior ou igual score de aplicacao em P6/P7;
- menor variancia intermodelo;
- sem regressao em priorizacao e em anti-armadilhas.

## Procedimento de decisao

1. Publicar dossie comparativo v1.x versus candidato v2.
2. Rodar revisao adversarial com rubrica fixa.
3. Emitir ADR de promocao ou adiamento.

## Saida esperada

- se aprovado: abrir trilha de migracao para v2.0 mantendo v1 como referencia.
- se nao aprovado: incorporar apenas melhorias pontuais em v1.x e registrar lacunas.
