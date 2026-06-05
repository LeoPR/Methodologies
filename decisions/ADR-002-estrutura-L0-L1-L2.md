---
status: accepted
date: 2026-06-03
deciders: [Leonardo Marques, Claude Code]
project: Strata
---

# ADR-002 — Estrutura em camadas de durabilidade L0 / L1 / L2

## Contexto

A metodologia poderia ser escrita como (a) **camada única** misturando princípios
atemporais e ferramentas de hoje, ou (b) **camadas explícitas** separadas por
durabilidade esperada, como alternativa que permite trocar ferramentas sem tocar
no núcleo.

A análise em `lab/2026-06-03-modernizacao/` mostrou que o monolito original
(~97 KB) misturava invariantes de séculos com nomes de versão de ferramentas que
mudam em meses — custo de atualização alto e perda de clareza epistêmica.

## Decisão

**Três camadas explícitas**:
- **L0** — núcleo atemporal (décadas/séculos): princípios e fundamentos que
  antecedem o computador.
- **L1** — padrões consolidados (décadas): formalizações nomeadas, maduras, mas
  substituíveis.
- **L2** — adaptação à era atual (meses): ferramentas de hoje, datadas, destacáveis.

## Razão

- A separação torna o **custo de troca explícito**: mudar de ferramenta = só
  editar L2. Hoje, trocaria Claude Code por outra IA sem tocar L0/L1.
- O teste de altitude L0 ("se o computador sumisse, continua verdadeiro?")
  permite verificar onde uma ideia pertence — disciplina editorial.
- A varredura future-proof (`lab/2026-06-03-future-proof-sweep/`) confirmou que
  o L0 tem lacunas identificáveis quando visto como camada independente — o que
  uma camada única tornaria invisível.

## Consequências

- ADRs, STATUS e lab READMEs devem mencionar a camada afetada (L0/L1/L2).
- Acréscimos ao produto começam pelo L0 — sem ancorar o princípio, não sobe.
- **Sinal de troca**: se a distinção L0/L1/L2 gerar atrito mais do que clareza
  (ex.: todo princípio precisar de 3 entradas), colapsar L0+L1 em uma única
  camada de núcleo.
