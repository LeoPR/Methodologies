---
title: L2-1 — Alinhamento estrutural da Parte III (Órganon) com o L0 fechado
created: 2026-08-01
updated: 2026-08-01
status: aprovada pelo dono (2026-08-01) — (a)+(b)+(c) aplicadas ao canônico
  EN-first; PT derivado PENDENTE por decisão (fim do ciclo L2; tradução será
  verificada contra §1–§6 deste doc). Ver §7.
---

# L2-1 — O que a Parte III deve ao L0 fechado?

## 1. Escopo e hipótese (declarada antes, §4)

> **H:** fechado o L0 (P1–P5), a Parte III tem **três** tipos de pendência, não
> um: (a) **frescor datado** — em grande parte JÁ resolvido (a matriz de IA
> carrega `[re-verified: 2026-08-01]`); (b) **alinhamento estrutural** — o
> §6-bis ganhou um 2º ato (*servir*) que **não tem forma L2 declarada**; §11
> pode ou não pedir expressão L2; (c) **fronteira Comporta** — linhas da matriz
> de IA são de *economia/roteamento* de recursos de IA, território da 2ª
> metodologia: a Parte III deve **apontar**, não duplicar (ADR-005).
> **Refutaria H:** mostrar que a forma do portão-de-servir já está declarada,
> ou que a fronteira Comporta já está clara para o leitor.

## 2. Achado (b.1) — o portão-de-servir (§6-bis, 2º ato) não tem forma L2

A P3 provou que o repo **pratica retenção sem forma declarada**:
`eval/strata/planos/` e `snapshot-fonte/` são gitignored por sigilo. A Parte
III cita `.gitignore` — mas **sob §8 (sinal vs ruído)**, que é outro ato: ruído
é o que não vale versionar; **retenção é o que não pode ser servido**. A forma
L2 do portão-de-servir falta. Candidatas (todas praticadas hoje, sem âncora):

- **Caminhos privados/ignorados por construção** — o que nunca entra no
  versionado não pode vazar (Kerckhoffs operacional: a chave fica fora do
  alcance do canal).
- **Permissões/ACL do repositório** (roles de GitHub etc.) — o portão-de-leitura
  institucional da era.
- **Esfera de leitores declarada no artefato** (frontmatter `audience:` e
  afins) — a "esfera declarada" que o L0 agora exige.

## 3. Achado (b.2) — §11 não pede expressão L2 (negativo declarado)

Formar o esquema é **trabalho de julgamento** (declarar eixo, dividir, revisar),
não de ferramenta. Ferramentas de tag/faceta de domínio (fotos, e-commerce,
sistemas de arquivos) são L2 **de outro domínio** — o mesmo argumento da
fronteira de cobertura ("qualidade de código é L2 de outro domínio").
**Decisão proposta: nenhuma linha L2 para §11** — registrado como negativo (§4),
espelhando o "§9 sem tabela L1" da P5.

## 4. Achado (c) — fronteira Comporta: 2 linhas da matriz de IA são de economia

Na tabela "AI agents" (Parte III §1): **"Context engineering + prompt caching"**
e **"Observability (OTel GenAI)"** carregam conteúdo de *economia e roteamento*
de IA (custo, cache, tokens) — que é o objeto do **Comporta**
(`lab/2026-06-04-economia-ia-tokens/`, ainda não destilado). O leitor de hoje
não tem como saber que existe uma 2ª metodologia dona desse território. Risco
real: quando o Comporta destilar, **duplicação** (proibida pelo AGENTS.md) ou
deriva entre as duas fontes (ADR-005).

**Proposta:** nada se move agora. Acrescenta-se **uma linha de fronteira** sob
a seção de IA declarando que a *economia/roteamento* de recursos de IA é a
metodologia Comporta (em pesquisa), e que, destilada, esta seção a **cita**
(ADR-005). Custa 2 linhas, fecha a fronteira, não antecipa o produto.

## 5. Texto candidato (EN-first; PT no fim do ciclo, verificado contra §1–§4)

**a) Parte III §3 (version control)** — nova linha na tabela:

> | **Private / ignored paths** (`.gitignore`, private repos, ACLs) | §6-bis **authority-to-read** — retention by construction: what never enters the versioned surface cannot be served (not §8-noise: deliberate withholding) | the sphere of readers is declared (frontmatter `audience:`), not implied |

**b) Parte III §1 (AI agents)** — nota de fronteira após a tabela:

> **Boundary**: the *economy and routing* of AI resources (which model, local
> vs cloud, cost, caching strategy) belongs to the **Comporta** methodology —
> in research (`lab/2026-06-04-economia-ia-tokens/`). When distilled, this
> section **points** to it (ADR-005); the rows above stay about *expressing*
> timeless needs, not *pricing* them.

**c) Colofão "Open items"** — ajuste de uma linha (o Eixo 5 continua aberto do
lado da **evidência**, mas o princípio agora cobre os dois atos):

> - **Axis 5 (security/adversariality)**: §6-bis now gates **both** acts
>   (executing and serving); the axis still deserves its own sweep on the
>   **evidence** side (today: completion-only signal).

## 6. Ameaças à validade (§4)

- **"L2 vira depósito":** toda linha nova precisa EXPRESSAR um ato do L0 — a
  régua aplicada ao L2. A linha (a) expressa o ato de servir (provado na P3);
  a nota (b) não é linha de ferramenta, é fronteira (barata, declarada).
- **Frescor não re-verificado hoje:** os itens datados restantes ("1M context",
  MCP, OTel) não foram re-checados nesta parte — o `re-verify-by: 2026-09-01`
  já governa; forçar re-verificação total agora seria §9 falhando.
- **Antecipar Comporta:** a nota (b) cita pesquisa em andamento; se o Comporta
  morrer no lab, a nota se remove com ele (L2 é destacável — é pra isso que a
  camada existe).

## 7. Decisão (dono, 2026-08-01)

- [x] **Aprovado (a)+(b)+(c)** — aplicado ao canônico EN-first: linha "Private /
  ignored paths" na tabela de version control (§6-bis-ver); nota de fronteira
  **Comporta** sob a seção de IA; colofão "Open items" agora diz que o Eixo 5
  é pendência de **evidência** (o princípio cobre os dois atos).
  **PT derivado fica para o fim do ciclo** (decisão do dono) — a tradução será
  verificada contra §1–§6 deste doc; o commit da aplicação EN usa `--no-verify`
  intencional (a guarda l10n exige par sincronizado — divergência declarada e
  temporária, com prazo: o fim da série L2).
