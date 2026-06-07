# ADR-001 — Fonte canônica de configuração e execução segura por agente

- Status: aceito
- Data: 2026-06-06

## Contexto

Havia instrução para execução cega de comandos e download/execução de código remoto,
além de ambiguidade sobre a fonte de configuração (`parametros.yaml` vs `config-final.json`).

## Decisão

- `config-final.json` é a fonte canônica de parâmetros.
- `parametros.yaml` permanece apenas por compatibilidade legada.
- O agente opera em fail-closed: sem execução arbitrária, sem download+execução sem validação,
  e com aprovação humana para ações com efeito colateral.

## Consequências

- Reduz risco de execução maliciosa e prompt injection operacional.
- Evita drift de configuração por dupla autoridade.
- Exige disciplina de validação e aprovação antes de executar.
