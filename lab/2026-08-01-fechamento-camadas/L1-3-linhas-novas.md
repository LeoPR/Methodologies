---
title: L1-3 — Linhas novas na Parte II (lacunas canônicas da L1-2) — decisão
created: 2026-08-01
updated: 2026-08-01
status: **FECHADA — APLICADA EN-first (2026-08-01)** — 2 de 8 candidatas
  aprovadas pelo dono (C1, C2), verificadas em fonte primária e inseridas;
  6 rejeitadas. PT derivado pendente (fim do ciclo).
---

# L1-3 — Quais lacunas canônicas entram na Parte II?

Continuação da L1-2 (que mapeou 8 candidatas a linha nova, classe C). Regra da
casa mantida: expansão não é fundamentação — cada linha entra só por decisão
explícita do dono, linha a linha (§9 contra inflação de tabela).

## 1. Questão

As 8 candidatas da L1-2 §6 — formalizações canônicas que "um revisor de
domínio notaria faltando" — devem virar linhas da Parte II?

## 2. Decisão do dono (2026-08-01), linha a linha

| # | Âncora | Candidata | Decisão |
|---|---|---|---|
| C1 | §3-bis | **RFC 2119/8174** (MUST/SHOULD/MAY — marca a força do ato) | **ENTRA** |
| C2 | §4 | **FAIR-base** — Wilkinson et al. 2016 (*Sci Data* 3:160018) | **ENTRA** |
| C3 | §4 | Reporting guidelines (EQUATOR: CONSORT/STROBE/PRISMA) | não entra |
| C4 | §5 | DRY (Hunt & Thomas 1999) | não entra |
| C5 | §6 | Reference rot (Zittrain et al. 2014; perma.cc) | não entra |
| C6 | §6-bis | Capability-based security (Dennis & Van Horn 1966) | não entra |
| C7 | §6-bis | OAuth 2.0 (RFC 6749) | não entra |
| C8 | publishing | DOI / Zenodo (PID) | não entra |

Registrado sem reabrir: as 6 rejeitadas ficam documentadas aqui e na L1-2 §6
— se recorrerem (regra de três), a candidatura reabre.

## 3. Verificação das aprovadas (fonte primária, 2026-08-01)

- **RFC 2119** — Bradner (Harvard), mar/1997, BCP 14, "Key words for use in
  RFCs to Indicate Requirement Levels"; **RFC 8174** — Leiba, mai/2017,
  "Ambiguity of Uppercase vs Lowercase…" (só maiúsculas carregam o sentido).
  Lidos no rfc-editor.org.
- **Wilkinson et al. 2016** — "The FAIR Guiding Principles for scientific data
  management and stewardship", *Sci Data* 3:160018; lido na nature.com
  (princípios para dados **e** objetos digitais de pesquisa — sustenta o gloss).

## 4. Texto aplicado (EN)

Sob §3-bis (após ISAD(G) — ordem da âncora: tipo de ato → referencial →
autodecodificabilidade):

`| **RFC 2119 / 8174 keywords** | requirement-level keywords (MUST / SHOULD / MAY) that mark the *force* of each statement — normative vs informative; the engineering-scale formalization of declaring the type of act | Bradner 1997 (RFC 2119); Leiba 2017 (RFC 8174) \`[WEB ✓ 2026-08-01]\` | — (stable since 1997; 8174 only clarifies that capitals alone carry the meaning) |`

Sob §4 (antes do FAIR4RS — pai antes do filho):

`| **FAIR** (guiding principles) | Findable/Accessible/Interoperable/Reusable — the base principles for research *data* and digital objects; FAIR4RS is the software offspring | Wilkinson et al. 2016 (*Sci Data* 3:160018) \`[WEB ✓ 2026-08-01]\` | FAIR4RS for research software (next row); apply the subset your project publishes |`

## 5. Ameaças à validade

- Decisão de escopo é do dono, não da literatura — as 6 rejeitadas podem ser
  reavaliadas se um revisor externo recorrer (ameaça aceita; regra de três).
- As 2 inserções foram verificadas individualmente (não só herdadas do swarm).
