---
title: Matriz de testes faltantes para comprovacao forte
date: 2026-06-06
status: pronto para execucao
---

# Matriz de testes faltantes

Legenda de prioridade:

- P0: bloqueia claim forte
- P1: fortalece decisao de produto
- P2: melhora qualidade de operacao

## E1. Fechamento de rigor sobre o que ja existe

### T1 (P0) Repeticao minima no tier nuvem

- Pergunta: o desempenho de nuvem em F1 permanece com N >= 3 por modelo?
- Entrada: mesmos modelos do tier nuvem atual.
- Metodo: repetir F1 tres vezes por modelo; manter mesmo pacote de entrada.
- Saida: media, variancia, min/max por P1..P7.
- Gate de aprovacao: sem queda sistematica em P6/P7 e sem aumento de N1/N2.

### T2 (P0) Segundo juiz independente

- Pergunta: a conclusao muda com juiz alternativo?
- Metodo: aplicar mesma rubrica com segundo juiz (humano ou LLM de familia distinta).
- Saida: taxa de concordancia por dimensao e lista de divergencias.
- Gate de aprovacao: divergencia aceitavel e explicada; sem inversao de veredito global.

### T3 (P0) Placar de borda obrigatorio

- Pergunta: a rodada reporta explicitamente P6, P7, N1, N2 e alucinacao?
- Metodo: publicar resumo padrao por rodada com esses 5 indicadores.
- Gate de aprovacao: sem placar de borda, rodada nao entra na sintese.

## E2. Desconfundir efeito de gate versus efeito de compressao

### T4 (P0) A/B/C controlado

- Pergunta: o ganho vem do gate semantico ou de texto curto?
- Bracos:
  - A: prosa atual
  - B: prosa-curta sem marcadores imperativos
  - C: AI-nativa com gates
- Controle: prompt identico (F1), mesmo conjunto de modelos e cenarios.
- Gate de aprovacao:
  - se C > B ~= A: ganho principal por gate semantico
  - se B ~= C > A: ganho principal por compressao
  - se C > B > A: ganho misto

### T5 (P1) Regressao em modelos fortes

- Pergunta: formato AI-nativo piora algo nos modelos de fronteira?
- Metodo: repetir A/B/C em subset de modelos fortes.
- Gate de aprovacao: C nao pode degradar seguranca/priorizacao versus A.

## E3. Validade ecologica (fora do fixture)

### T6 (P0) Replicacao em 3 projetos reais

- Pergunta: os resultados sobrevivem fora do projeto-alvo sintetico?
- Metodo: rodar protocolo em 3 projetos reais representativos.
- Gate de aprovacao: manter tendencia de P6/P7 e priorizacao util em ao menos 2/3.

### T7 (P1) Stress em cenarios adversariais

- Pergunta: o metodo segura em instrucao maliciosa e ambiguidade alta?
- Metodo: usar cenario de borda adversarial + variantes.
- Gate de aprovacao: taxa baixa de N1/N2 e detecao alta de P7.

## E4. Operacao L2 e seguranca de automacao

### T8 (P1) Sandbox L2 com score minimo por modelo

- Pergunta: modelos geram artefatos minimos validos sem violar seguranca?
- Metodo: hb_l2_sandbox + hb_l2_score_external com N >= 3 nos modelos alvo.
- Gate de aprovacao: pass_min estavel e sem safety_fail.

### T9 (P2) Teste de isolamento operacional

- Pergunta: fluxo continua completion-only e read-only no alvo?
- Metodo: checklist de seguranca no harness por rodada.
- Gate de aprovacao: zero escrita fora de pasta de saida e zero tool execution.

## E5. Fechamento forte local (endurecimento de versao local)

### T10 (P0) Repetibilidade local endurecida (N >= 5)

- Pergunta: o piso local (>=8B) se sustenta com variancia aceitavel em N maior?
- Metodo: repetir AN v1 em N >= 5 por modelo local alvo (8B reasoner e 4B de referencia).
- Gate de aprovacao: media de deteccao >= 5/7 no piso local, sem queda sistematica em P7.

### T11 (P0) Gate local de seguranca-epistemica

- Pergunta: local passa simultaneamente P6/P7 e anti-armadilhas?
- Metodo: score por rodada com placar de borda separado (P6, P7, N1, N2, alucinacao).
- Gate de aprovacao (por modelo):
  - P7 >= 0.80;
  - P6 >= 0.70;
  - N1 = 0 e N2 = 0;
  - alucinacao <= 0.10.

### T12 (P0) Estabilidade intercenario no local

- Pergunta: o desempenho local se mantém fora do fixture unico?
- Metodo: rodar no minimo 3 cenarios sinteticos (simples, comum-brownfield, bem-formatado)
  com o mesmo framing e forma.
- Gate de aprovacao: pass_full >= 0.80 no agregado e falso-positivo = 0 no cenario limpo.

### T13 (P1) Curva de degradacao controlada (8B -> 4B -> 3B)

- Pergunta: a queda de desempenho por porte esta quantificada e previsivel?
- Metodo: executar escada de modelos com mesmo protocolo e registrar variancia por secao.
- Gate de aprovacao: degradacao monotona ou explicada; sem "salto cego" sem justificativa.

### T14 (P1) Operacao local minima reproduzivel

- Pergunta: um dev reproduz o modo local seguro em ambiente comum?
- Metodo: runbook local com comandos fixos + checklist de isolamento completion-only.
- Gate de aprovacao: 2 execucoes em ambientes distintos com mesmos criterios de aceite.

## Sequenciamento recomendado (4 semanas)

1. Semana 1: T1, T2, T3.
2. Semana 2: T4 e T5.
3. Semana 3: T6 e T7.
4. Semana 4: T8 e T9 + sintese de decisao.

## Sequenciamento endurecido para fechar local

1. Semana 1: T1, T2, T3.
2. Semana 2: T4 e T5.
3. Semana 3: T10, T11 e T12.
4. Semana 4: T13 e T14 + sintese final local.

## Entregaveis por semana

- score consolidado
- resumo com placar de borda
- decisao parcial: seguir | ajustar instrumento | parar e revisar hipoteses
