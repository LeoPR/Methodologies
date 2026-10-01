---
title: 'Ferramentas de agentes em 2026-10: arquivos de instrução e camada de garantia'
created: 2026-10-01
updated: 2026-10-01
status: 'Registro da reverificação da Parte III §1 (L2) do canônico v1.2.10. Fontes primárias consultadas em 2026-10-01.'
tags: [l2, agentes, agents-md, guardrails, seguranca]
---

# Ferramentas de agentes em 2026-10

Registro das fontes que sustentam a atualização da Parte III §1 (L2) do canônico. Não é fonte de
estado: o estado está no canônico.

## O que mudou no canônico (e por quê)

- **AGENTS.md no Gemini CLI.** O canônico dizia "nativo". O arquivo padrão do Gemini CLI é o
  `GEMINI.md`; o AGENTS.md entra por configuração (`context.fileName`).
- **AGENTS.md no Claude Code.** Lido quando o projeto não tem CLAUDE.md; uma configuração carrega os
  dois. A redação anterior ("o CLAUDE.md tem precedência") dizia quase isso; ficou exata.
- **Fontes de instrução se combinam de modos diferentes por ferramenta** (somadas em umas, o
  arquivo mais próximo vence em outras). Daí a recomendação de uma fonte com autoridade (§5).
- **Linha nova: camada de garantia.** Permissões, hooks que bloqueiam, sandbox, configuração
  gerenciada e, no forge, proteção de branch, checks obrigatórios e aprovador diferente de quem
  pediu. Os fabricantes passaram a afirmar por escrito que arquivo de instrução é contexto, não
  garantia. É o §5 (o que precisa valer mora numa checagem) somado ao §6-bis (fail-closed, canal fora
  de banda). O L0 não muda.
- **Aprovação por modelo** (modos de autoaprovação com classificador) tem taxa de erro documentada
  pelo próprio fabricante; ação irreversível pede portão determinístico.

## Fontes (consultadas em 2026-10-01)

Instrução:
- AGENTS.md e a Agentic AI Foundation (2025-12-09):
  https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
  · https://agents.md · https://aaif.io/projects/
- Claude Code, AGENTS.md (changelog v2.1.277, 2026-09-18) e regras de carga:
  https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md · https://code.claude.com/docs/en/memory
  ("context, not enforced configuration")
- Gemini CLI, `GEMINI.md` como padrão: https://geminicli.com/docs/cli/gemini-md/
- GitHub Copilot, tipos de instrução e matriz de suporte:
  https://docs.github.com/en/copilot/reference/custom-instructions-support
- VS Code, fontes somadas e precedência por ferramenta:
  https://code.visualstudio.com/docs/copilot/customization/custom-instructions
- Agent Skills: https://agentskills.io/specification

Garantia:
- Claude Code, permissões ("enforced by Claude Code, not by the model"), modos, hooks, sandbox (sem
  Windows nativo), configuração gerenciada: https://code.claude.com/docs/en/permissions ·
  https://code.claude.com/docs/en/permission-modes · https://code.claude.com/docs/en/hooks ·
  https://code.claude.com/docs/en/sandboxing · https://code.claude.com/docs/en/managed-settings
- Auto mode (classificador, taxa de erro do fabricante):
  https://www.anthropic.com/engineering/claude-code-auto-mode
- GitHub, riscos e mitigações do agente na nuvem (aprovador diferente de quem pediu, branch única,
  checks): https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations
- VS Code, aprovações, workspace trust e políticas: https://code.visualstudio.com/docs/agents/run/approvals
  · https://code.visualstudio.com/docs/agents/run/security · https://code.visualstudio.com/docs/enterprise/manage-ai-settings
- MCP, spec 2026-07-28 e boas práticas ("cannot enforce these security principles at the protocol
  level"): https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices

Consenso de segurança (insumo para o item em aberto do eixo de segurança; não promovido à L1):
- OWASP LLM Top 10 2026 e Top 10 for Agentic Applications (2025-12-09): https://genai.owasp.org/
- NCSC (Reino Unido), 2025-12-08: LLMs não separam instrução de dado; reduzir impacto com
  salvaguardas determinísticas.
- Nasr, Carlini et al., "The Attacker Moves Second", arXiv 2510.09023 (2025-10-10).
- CaMeL, arXiv 2503.18813; Beurer-Kellner et al., arXiv 2506.08837; "lethal trifecta" (Willison,
  2025-06-16); "Agents Rule of Two" (Meta, 2025-10-31). Ideias de 2025, ainda sem a maturidade da L1.

## O que ficou de fora

- Detalhes do protocolo MCP e o A2A: nenhuma necessidade do Strata depende deles.
- Promoção de padrões de segurança de 2025 à L1: maturidade insuficiente.
- Configuração por ferramenta no repositório: duplicaria a fonte de instrução (§5).
