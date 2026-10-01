---
title: 'M2b: diário curto de uso interativo'
created: 2026-10-01
updated: 2026-10-01
status: 'Aberto. Duas semanas de uso normal, de 2026-10-02 a 2026-10-15.'
---

# M2b: diário curto de uso interativo

Parte do M2 que só o uso mede (ver o [PLANO-v2](PLANO-v2.md) e o [M2a](instrumento/M2A.md)). O custo
do Claude Code já sai dos transcripts; este diário cobre o que nenhum log registra.

## O que ele responde

1. **Copilot Pro+ × Pro:** quanto do crédito do Copilot o chat e o agente gastam por semana. Abaixo de
   US$ 15 por mês, o Pro pode bastar.
2. **Local no chat (BYOK, Ollama no Docker):** em que tarefas resolve, em quais escala para a nuvem.
3. **Autocomplete:** se o do Copilot atende ou se falta algo que o local daria.
4. **Rota escolhida:** o que vai para o Claude Code (Max) e por quê.

## Como preencher

- **Uma linha por tarefa** que usou IA no editor, fora do Claude Code. As do Claude Code, só quando você
  tentou outra rota antes.
- **Uma linha por dia** com o saldo de créditos do Copilot (painel de cobrança do GitHub).
- Palavras curtas. Nenhum conteúdo de código ou de projeto é necessário.
- Para usar o local, ligue antes o contêiner do Ollama no Docker Desktop (ele está parado).

Campos:
- **classe:** C1 pergunta · C2 investigação · C3 edição pontual · C4 multi-arquivo (as do M2a);
- **rota:** copilot-chat · copilot-agente · local-chat · claude-code · autocomplete;
- **modelo:** o que estava selecionado;
- **desfecho:** resolveu · escalou (para qual rota) · desistiu;
- **nota:** opcional, poucas palavras (atrito, lentidão, erro).

## Registro

| data | classe | rota | modelo | desfecho | nota |
|---|---|---|---|---|---|

## Saldo do Copilot por dia

| data | créditos usados no mês até hoje (US$) |
|---|---|
