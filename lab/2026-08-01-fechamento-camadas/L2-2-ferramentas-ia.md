---
title: L2-2 — Revisão das ferramentas de IA da Parte III (Órganon, §1 AI agents)
created: 2026-08-01
updated: 2026-08-01
status: **FECHADA — APLICADA EN-first (2026-08-01)** — escopo total aprovado
  pelo dono: correção C2PA, reescrita layered memory, nota de estado
  atualizada (MCP 2026-07-28; Skills cross-tool + aviso; base legal da
  transição; Code of Practice), nuance OTel na linha, carimbo `[2026-08-01]`
  / re-verify-by 2026-11-01. PT derivado pendente (fim do ciclo).
---

# L2-2 — A matriz de ferramentas de IA ainda está fresca?

Origem do pedido: na avaliação inicial (2026-08-01) o dono apontou *"as
ferramentas de IA pedidas me parecem que precisam de revisão"*. A Parte III §1
(AI agents) foi capturada em **2026-06-03** e se declara semi-viva
(`re-verify-by: 2026-09-01`). Esta parte é a re-verificação antecipada — o
eixo de maior cadência do documento.

## 1. Hipótese (declarada antes, §4)

> **H:** 2 meses depois, a matriz está **majoritariamente fresca**, com três
> classes de achado: (a) **precisões de adoção** — ferramentas que passaram a
> suportar os padrões nativamente (AGENTS.md, MCP, Skills) ou mudaram de
> comportamento; (b) **adições canônicas novas** — formas que surgiram/
> estabilizaram entre jun–ago 2026 e que um revisor notaria faltando;
> (c) **nota regulatória correta** — EU AI Act Art. 50 (entra em vigor
> **2-ago-2026**, amanhã) e C2PA 2.x (= ISO/IEC 22144) com prazos certos.
> **Refutaria H:** ferramenta da matriz morta/renomeada, afirmação factual
> errada, ou mudança de paradigma (ex.: vector DB retomando o lugar do grep).

## 2. Método

Swarm de 3 agentes (read-only, WebSearch/FetchURL), cobrindo as 10 linhas da
matriz + a nota "State of the matrix":

- **A — padrões e adoção**: AGENTS.md/CLAUDE.md, MCP, Agent Skills + a nota de
  estado (Agentic AI Foundation/Linux Foundation 2025; lista de ferramentas
  nativas; Claude Code e CLAUDE.md).
- **B — práticas de agente**: layered memory, context engineering + prompt
  caching, subagents/fan-out, agent evals — "a prática descrita ainda é a
  forma 2026?" (menos identidade, mais vigência).
- **C — proveniência/observabilidade/busca + regulação**: C2PA, OTel GenAI,
  grep-first; EU AI Act Art. 50 (datas exatas), C2PA = ISO/IEC 22144, prazo
  de transição 2-Dec-2026.

Cada agente devolve: linha | ainda verdade em 2026-08? (evidência) | mudou?
(correção) | ausente? (adição canônica). Verificações datadas de 2026-08-01.

## 3. Escopo declarado (limites)

- **Só a Parte III §1** (AI agents). As seções 2–5 (editor, git, filesystem,
  trackers SaaS) são de cadência baixa e não foram apontadas pelo dono.
- O objeto é **frescor factual**, não re-fundamentação (a coluna "Expresses"
  já foi alinhada ao L0 fechado na L2-1; não reabrir).
- A fronteira Comporta (economia/roteamento de IA) está declarada na L2-1 —
  fora desta parte.

*(Resultados, ameaças e decisão: a preencher após o swarm.)*

## 4. Resultados do swarm (3 agentes, fonte primária, 2026-08-01)

**H CONFIRMADA no essencial** — nenhuma linha morreu, nenhum paradigma mudou
(grep-first segue dominante, com estudo arXiv mai/2026 "Is Grep All You
Need?"). Achados por classe:

### (a) Erro factual (1)

- **"C2PA 2.x (= ISO/IEC 22144)" é errado duas vezes**: na fonte primária ISO
  o projeto é **ISO/CD 22144** (TC 171/SC 2, estágio 30.99 "under
  development") — ainda **não** é International Standard; e a designação é
  **ISO 22144**, não "ISO/IEC" (esse prefixo seria JTC 1). Correção: "C2PA 2.x
  (on its way to becoming ISO 22144 — ISO/CD, still under development) is
  today's de facto path".

### (b) Mudança de desenho (1)

- **Layered memory**: o desenho vigente mudou — **auto memory nativa**
  (`MEMORY.md`, escrito pelo agente, default-on desde ~fev/2026 — já existia
  na captura de jun/2026, logo foi **omissão**, não drift) e **hooks foram
  reposicionados como enforcement**, não como camada de memória. O aviso de
  "drift opaco" passa a valer também para a camada (2). Reescrever a célula.

### (c) Precisões e atualizações de estado

- **MCP**: spec nova **2026-07-28** (3 dias antes da verificação) — núcleo
  stateless; Roots/Sampling/Logging/HTTP+SSE legado deprecados; DCR→CIMD;
  governança AAIF/Linux Foundation. A linha da tabela (genérica) não muda;
  a nota de estado ganha a frase.
- **Agent Skills**: saiu de "promessa" para **padrão aberto cross-tool de
  facto** (agentskills.io, dez/2025; ~40 plataformas, incl. Codex/Copilot/
  VS Code/Cursor) — registrar + aviso: auditar skills de terceiros como
  servidores MCP (341 maliciosas detectadas em hubs).
- **Transição Art. 50**: a base legal mudou após a captura — **Art. 111(4) do
  Reg. (UE) 2026/1744** (Digital Omnibus, em vigor 27-jul-2026), e o escopo é
  estreito: **só o dever de marcação do Art. 50(2)**, só p/ sistemas no
  mercado antes de 2-ago-2026. Datas confirmadas: aplicação 2-ago-2026;
  technology-neutral; transição a 2-dez-2026.
- **OTel GenAI**: as semconv `gen_ai.*` **não estabilizaram** (tudo
  "Development"; migraram para o repo `semantic-conventions-genai`) — a linha
  não prometia estabilidade; a nuance protege o leitor ("pin the generation
  used").
- **Adição regulatória canônica**: **EU Code of Practice on Transparency of
  AI-Generated Content** (Comissão, 10-jun-2026 — uma semana após a captura):
  multi-camada C2PA (L1) + watermarking (L2) + rótulo visível (L3), voluntário
  com presunção de conformidade. É o que operacionaliza o Art. 50.
- **Carimbo**: com a re-verificação, o capture da Parte III sobe para
  `[2026-08-01]` e `re-verify-by: 2026-11-01` (cadência trimestral mantida).

### Válidas sem edição (registro)

AGENTS.md (formato aberto sob AAIF/Linux Foundation; lista de ferramentas só
cresceu), Claude Code/`@AGENTS.md` (confirmado na doc oficial de hoje), nota
de segurança MCP (reforçada pela própria spec), context engineering + prompt
caching (referência Anthropic set/2025 segue canônica), subagents/fan-out
(institucionalizado), agent evals (ganhou guia oficial OpenAI jan/2026),
grep-first (ver acima).

### Não propostas (registradas)

A2A v1.0 (Linux Foundation) — padrão real mas adoção desigual: watchlist, não
linha. MCP Apps/Tasks/EMA — fresco demais (3 dias). Nuance "established
standard" → "open format" — opcional, não aplicada. W3C/IETF `aicdh` —
embrionário. California SB 942 — fora do recorte EU da nota.

## 5. Ameaças à validade

- Verificação por agentes com web — mitigada por fonte primária em cada
  veredito (aaif.io, blog oficial MCP, code.claude.com/docs, ISO, EUR-Lex,
  digital-strategy.ec.europa.eu). O erro C2PA↔ISO foi confirmado no catálogo
  ISO, não em blog.
- A spec MCP 2026-07-28 tem 3 dias — detalhes finos dela podem ainda estar
  em digestão pela imprensa; o que entra na nota é só o estrutural (stateless,
  deprecações, governança).
- A cadência trimestral do re-verify-by é convenção do próprio documento —
  mantida sem discussão.

## 6. Decisão (dono, 2026-08-01)

**Aprovado: aplicar tudo.** Aplicado ao canônico EN nesta data: (a) correção
C2PA ("on its way to becoming ISO 22144 — ISO/CD, still under development");
(b) linha layered memory reescrita (auto memory `MEMORY.md` na camada 2,
hooks como enforcement, aviso de drift opaco nas camadas 2+4); (c) nota de
estado reescrita (`[VERIFY: 2026-08-01]`: MCP 2026-07-28; Skills cross-tool
~40 plataformas + aviso de auditoria; transição com base legal Art. 111(4)
Reg. (UE) 2026/1744, escopo só Art. 50(2); EU Code of Practice Jun-2026);
(d) nuance OTel GenAI "Development" na linha; (e) cabeçalho da Parte III:
capture `[2026-08-01]`, `re-verify-by: 2026-11-01`, e aponte para este doc.
PT derivado: pendente para o fim do ciclo.
