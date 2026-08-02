---
title: L1-2 — Repesquisa de literatura da Parte II (Morfé) — verificação funda
created: 2026-08-01
updated: 2026-08-01
status: **APLICADA ao canônico EN (2026-08-01)** — escopo aprovado pelo dono:
  classes A (14 erros/precisões) + B (9 reparos editoriais) + selos
  `[WEB ✓ 2026-08-01]` em toda a Parte II. Classe C (8 linhas novas) virou a
  parte **L1-3** (decisão linha a linha, pendente). PT derivado pendente (fim
  do ciclo).
---

# L1-2 — O dono elevou a régua: `[CANONICAL]` não basta; verificar de fato

Contexto: a L1-1 decidiu (c) como política "`[CANONICAL]` + verificar-ao-tocar".
O dono **superou** essa decisão: *"o L1 precisa de repesquisa de literatura e
fundamento — não basta parecer que está bem ou ruim, precisa estar fundamentado
e ter relação lógica e útil com o L0"*. Esta parte é essa repesquisa.

## 1. Hipótese (declarada antes)

> **H:** as fontes da Parte II **existem e estão majoritariamente corretas**,
> com três classes de achado: (A) **erros factuais pontuais** de atribuição/
> venue/edição em linhas `[CANONICAL]`-only (nunca web-verificadas); (B)
> **glosses e change-signals degradados** (sinais que viraram nota de
> aderência — território de §9 — ou glosses que descrevem a formalização
> errado); (C) **lacunas canônicas** que um revisor de domínio notaria.
> **Refutaria H:** encontrar fonte inexistente, relação L0↔L1 quebrada em
> massa, ou necessidade de re-estruturar as tabelas.

## 2. Método

Swarm de **7 agentes** (read-only), um por grupo de âncoras, cobrindo as ~35
linhas da Parte II. Cada agente: (1) verificou na web cada fonte (autor/ano/
título/venue + se sustenta a alegação), preferindo fonte primária (DOI, RFC,
órgão de padrões, editora); (2) avaliou a **relação lógica** formalização ↔
necessidade L0 declarada na âncora; (3) avaliou o change-signal. Todas as
verificações datadas de **2026-08-01**, cada achado com URL de evidência.

## 3. Veredito geral — H CONFIRMADA

- **Nenhuma fonte inexistente** (a única "NÃO ENCONTRADA" é `conventions` na
  linha compendium/changelog — que é honestamente inverificável por desenho).
- **Nenhuma relação L0↔L1 quebrada** — os únicos elos fracos (C4 sob §5; PARA
  sob §7; Lakatos sob §4) já vinham auto-mitigados pelos próprios change-signals
  ou melhoram com ajuste de gloss, não de âncora.
- **Nenhuma re-estruturação** de tabela ou âncora necessária.
- Achados concretos: **14 erros/precisões factuais (A)**, **9 reparos
  editoriais (B)**, **8 candidatas a linha nova (C)**, e direito adquirido de
  subir selos `[CANONICAL]`→`[WEB ✓ 2026-08-01]` nas linhas verificadas.

## 4. Classe A — erros factuais e precisões (corrigir)

| # | Linha | Hoje | Correção (com evidência) |
|---|---|---|---|
| A1 | FAIR4RS (§4) | `Chue Hong et al. 2022 (Scientific Data 9:622)` | **citação mista**: *Sci Data* 9:622 é **Barker et al. 2022** ("Introducing the FAIR Principles for research software", DOI 10.1038/s41597-022-01710-x); "Chue Hong et al. 2022" é o doc RDA (DOI 10.15497/RDA00068). Corrigir para `Barker et al. 2022 (Sci Data 9:622)` |
| A2 | Registered Reports (§4) | `Chambers 2017` | canônico do formato = **Chambers 2013** (*Cortex* 49(3):609–610); estado-da-arte = **Chambers & Tzavella 2022** (*Nat Hum Behav* 6:29–42). 2017 é o manifesto |
| A3 | Threats-to-validity (§4) | `Campbell & Stanley 1963 / Wohlin et al. 2012` | genealogia pula elo: a taxonomia **quádrupla** (internal/external/construct/conclusion) é de **Cook & Campbell 1979** (*Quasi-Experimentation*); C&S 1963 só tem internal+external → `C&S 1963 → Cook & Campbell 1979 / Wohlin et al. 2012` |
| A4 | C4 (§5) | `c4model.info` | domínio histórico; o site migrou (~2024) → **`c4model.com`**; não há publicação formal além do site + Leanpub (Brown 2023) + InfoQ |
| A5 | OKR (§7-cont) | `Doerr 2018` | origem omitida: **Grove 1983** (*High Output Management*, Intel — iMBO); o próprio Doerr atribui a Grove → `Grove 1983 (origin, Intel); Doerr 2018` |
| A6 | MoSCoW (§7-cont) | `DSDM 1994` | autor nomeado omitido: **Dai Clegg (Oracle UK), 1994**; DSDM é método/consórcio → `Clegg 1994 (Oracle UK); DSDM` |
| A7 | Regra 3-2-1 (§10) | `Carnegie Mellon CERT; widely adopted` | **atribuição inexistente** (fusão de órgão e autora). Origem comprovada: **Peter Krogh**, *The DAM Book* (O'Reilly 2005/2009); o doc CMU p/ US-CERT (Ruggiero & Heckathorn 2012, *Data Backup Options*) **recomenda citando Krogh** → `Krogh 2005/2009 (The DAM Book); recommended by US-CERT (Ruggiero & Heckathorn 2012, CMU)` |
| A8 | RBAC (§6-bis) | `NIST ANSI/INCITS 359-2004` | funde dois órgãos: o padrão é **ANSI/INCITS** 359-2004 (superado pela rev. **2012**, a vigente); a NIST é autora do **modelo** (Ferraiolo et al. 2001, *ACM TISSEC* 4(3)) → `ANSI/INCITS 359-2004 (rev. 2012; NIST model — Ferraiolo et al. 2001)` |
| A9 | ABAC (§6-bis) | `NIST SP 800-162` | edição jan/2014 **retirada** e substituída pela atualização ago/2019 (mesmo número) → `NIST SP 800-162 (2014, updated 2019)` |
| A10 | SIFT (§6) | `Caulfield 2017/2019` | o SIFT (Stop/Investigate/Find/Trace) nasce no **post de 2019**; o livro de 2017 traz moves **diferentes** (precursor) → `Caulfield 2019 (precursor 2017)` |
| A11 | PRONOM change-signal (§3-bis) | `MIME-type (RFC 2045)` | media types são **RFC 2046** (+ registro IANA); RFC 2045 é o formato do corpo da mensagem |
| A12 | ISAD(G) gloss (§3-bis) | "distingue ato dispositivo vs probativo" | **a alegação não se sustenta no padrão**: os termos não constam do ISAD(G); a distinção é da **diplomática** (já no grounding do L0 §3-bis — Brunner 1880). O que se sustenta: 3.4.1 *conditions governing access* (registra as condições do portão de servir; não as *enforça*) → gloss restringido a "archival-description template; its *conditions governing access* area records the serving gate (§6-bis) at institutional scale" |
| A13 | ISAD(G) change-signal (§3-bis) | `RiC-CM as the emerging successor` | RiC-CM **v1.0 (fim 2023)** é recomendação oficial ICA que **substitui** ISAD(G)/ISAAR(CPF)/ISDF/ISDIAH — não é mais "emerging" → `RiC-CM (official ICA successor, v1.0 late 2023); EAD for electronic exchange` |
| A14 | Zettelkasten (§7) | `Luhmann / Ahrens 2017` | comprime originador e popularizador (Luhmann não publicou em 2017) → `Ahrens 2017 (Luhmann's method)` |

Precisões menores registradas (mesma classe, baixo custo): IA — citação dupla
`Rosenfeld & Morville 1998 (1st ed.); 4th ed. w/ Arango 2015`; GRADE — inaugural
peer-reviewed é Atkins et al. 2004 (BMJ 328), Guyatt 2008 é o marco; Sackett
1996 define EBM, a pirâmide estrita é OCEBM 2011.

## 5. Classe B — glosses e change-signals degradados (reparo editorial)

O padrão transversal (achado do agente da faixa §7-cont/§8/publishing):
**a coluna change-signal degradou para nota de aderência** — diz *quando
aplicar* ("only if publishable", "use the necessary subset") em vez de *o que
substitui* a formalização. Aderência é território de §9; a coluna perde a
função declarada no cabeçalho da Parte II.

| # | Linha | Reparo |
|---|---|---|
| B1 | Cookiecutter DS (§1) | gloss erra 2×: "data/code/output" ≠ os três tipos de §1 (produto/exploração/conhecimento) e "(signal vs noise)" é resíduo de §8 (migração P5). Reescrever mapeando pastas→trio §1 (notebooks/≈exploração; src/+reports/≈produto; docs/+references/≈conhecimento); sinal honesto: "a instância morre com o stack; o padrão 'separar tipos em lugares físicos' permanece"; cross-ref: research compendium (For §4) é a expressão acadêmica |
| B2 | C4 (§5) | gloss → "a single model of the system → views at 4 altitudes (consistency by construction)" — fortalece o elo §5 (1 modelo → N vistas, weave/tangle-like) |
| B3 | Dublin Core/DataCite/schema.org (publishing) | gloss "for datasets" só descreve DataCite; DC é recurso genérico, schema.org é web geral → "interoperable metadata schemas (resources/data/web)"; sinal: DCAT/CodeMeta conforme o tipo de artefato |
| B4 | JOSS (publishing) | "a standard" superestima — é *journal* (venue peer-reviewed + critérios de revisão); sinal: SoftwareX/JORS/Zenodo-DOI |
| B5 | OKR (§7-cont) | gloss "(acceptance criteria)" importa termo errado (KR é resultado mensurável); sinal vazio → "FAST goals / KPIs if OKR turns into quarterly theater" |
| B6 | CITATION.cff (publishing) | sinal "only if publishable" é aderência → "CodeMeta if the ecosystem asks for JSON-LD"; opcional: citar Druskat et al. 2021 |
| B7 | PKI/X.509 (§6-bis) | sinal mistura camadas: JWT/PASETO são *formatos de token*, não canal — a distribuição de chaves continua PKI → "JWT/PASETO change the token format; the out-of-band channel remains PKI (GPG web-of-trust without hierarchical CA)" |
| B8 | compendium/changelog/narrative (§7) | `conventions` sem cross-ref → "changelog → see For §8 (Keep a Changelog); decision → see For §3 (ADR)" |
| B9 | Transversal | revisar as células-aderência no espírito acima ao tocar cada linha |

## 6. Classe C — lacunas canônicas (candidatas a linha nova)

| # | Âncora | Candidata | Por que um revisor notaria |
|---|---|---|---|
| C1 | §3-bis | **RFC 2119/8174** (MUST/SHOULD/MAY) | com a reatribuição dispositivo/probativo à diplomática (A12), o lado engenharia da âncora fica sem formalização de "marcar a força do ato"; RFC 2119 é o padrão de facto de força normativa vs informativa |
| C2 | §4 | **FAIR-base — Wilkinson et al. 2016** (*Sci Data* 3:160018) | pai do FAIR4RS, mais citado; o projeto tem dados/fixtures, não só software |
| C3 | §4 | **Reporting guidelines** (rede EQUATOR: CONSORT 2010 / STROBE 2007 / PRISMA 2020) | IMRaD diz *onde* reportar; CONSORT/STROBE dizem *o que* não pode faltar — completam "resultado honesto" |
| C4 | §5 | **DRY** — Hunt & Thomas 1999 (*The Pragmatic Programmer*) | a formulação canônica **nomeada** do próprio princípio de §5 ("single, unambiguous, authoritative representation") |
| C5 | §6 | **Reference rot** — Zittrain, Albert & Lessig 2014 (*Harv. Law Rev. Forum* 127; perma.cc/Wayback) | §6 declara perecibilidade mas a tabela só cobre *avaliação* (CRAAP) e *re-verificação* (SIFT); nada cobre a podridão da própria referência e sua mitigação arquivística |
| C6 | §6-bis | **Capability-based security** — Dennis & Van Horn 1966 (*CACM* 9(3)) | o terceiro modelo clássico de autoridade (token infalsificável que *é* a autoridade); a tabela cobre cadeia-de-confiança (PKI) e autorização (RBAC/ABAC), omite capabilities (sucessores: macaroons, Biscuit) |
| C7 | §6-bis | **OAuth 2.0** (RFC 6749, 2012) | a formalização dominante de autoridade delegada explícita/auditável em APIs; linha própria ou sinal de PKI/RBAC |
| C8 | publishing | **DOI / Zenodo** (PID) | **a lacuna mais crítica**: a âncora promete "tornar citável" mas nenhuma linha cobre o mecanismo que *emite* a identidade citável (DOI via DataCite; Zenodo p/ repos GitHub; Software Heritage/SWHID p/ software). `DOI`/`Zenodo`/`ORCID` não aparecem no documento inteiro |

Registradas e **não propostas** como linha (ficam em change-signals ou fora):
OCFL (sinal do BagIt), PREMIS/ISO 16363 (sinal do OAIS), Hulme 1911 (origem de
literary warrant), LCC fonte 1897+, NDSA datado, SPIFFE/SPIRE, XACML,
SP 800-207A, DITA/Good Docs (sinal Diataxis), notebooks/docs-as-code (sinal
Literate programming), OCEBM 2011 (sinal GRADE), Personal Kanban, GTD,
CalVer/EffVer (sinal SemVer), YADR, ORCID (debater se §3 ou publishing).

## 7. Selos — direito adquirido desta rodada

O cabeçalho da Parte II declara `[WEB ✓]` = verificado na rodada,
`[CANONICAL]` = citado de conhecimento. Esta rodada **web-verificou** as linhas
`[CANONICAL]`-only (era a pendência da política L1-1-(c)). Proposta: subir para
`[WEB ✓ 2026-08-01]` as linhas integralmente verificadas e ajustar o
cabeçalho: "framework identities web-verified 2026-06-03, **re-verified and
corrected 2026-08-01** (see `lab/2026-08-01-fechamento-camadas/L1-2-…`)".

## 8. Ameaças à validade

- **Verificação por agentes com web** — podem ter errado em pontos específicos.
  Mitigação: todo achado classe A traz URL de fonte primária; as 3 correções
  mais caras (A7 3-2-1, A12 ISAD(G), A1 FAIR4RS) foram as mais documentadas
  (cadeia de citação rastreada / texto integral do padrão lido / página da
  Nature conferida). Spot-check manual recomendado antes de aplicar.
- **"Lacuna que um revisor notaria"** é juízo dos agentes — risco de
  sobre-inclusão (§9). Mitigação: classe C é *candidata*; cada linha só entra
  se o dono aprovar, e o formato exige change-signal (que limita a inflação).
- **Cobertura das fontes citadas, não do domínio** — outras lacunas podem
  existir; esta rodada não é exaustiva por desenho (§9).
- **Conflito com L1-1-(c)**: esta parte **supera** a política
  "verificar-ao-tocar" para as linhas verificadas (fica o registro).

## 9. Texto candidato (EN-first) — amostras das edições principais

A1 — FAIR4RS:
`| **FAIR4RS** | Findable/Accessible/Interoperable/Reusable principles for research *software* | Barker et al. 2022 (*Sci Data* 9:622); RDA: Chue Hong et al. 2022 \`[WEB ✓ 2026-08-01]\` | apply only the subset your project publishes |`

A7 — 3-2-1:
`| **3-2-1 rule** | 3 copies, on 2 distinct media, 1 offsite — a minimal heuristic with independent failure modes; operationalizes §10's "N dispersed replicas" at any project scale | Krogh 2005/2009 (*The DAM Book*, O'Reilly); recommended by US-CERT (Ruggiero & Heckathorn 2012, CMU) \`[WEB ✓ 2026-08-01]\` | expand to **3-2-1-1-0** for critical data; LOCKSS for academic publications |`

A12+A13 — ISAD(G):
`| **ISAD(G)** (General International Standard Archival Description) | archival-description template operating §3-bis at institutional scale; its *conditions governing access* area records the **serving gate** (§6-bis) at the same scale | ICA, 2nd ed. 2000 \`[WEB ✓ 2026-08-01]\` | RiC-CM (official ICA successor, v1.0 late 2023); EAD for electronic exchange |`

C8 — DOI/Zenodo (linha nova, publishing):
`| **DOI / Zenodo** | persistent identifier + archival deposit that *mints* the citable object (DOI via DataCite; Zenodo for GitHub repos) | datacite.org / zenodo.org \`[WEB ✓ 2026-08-01]\` | Software Heritage (SWHID) for software source |`

## 10. Decisão (dono, 2026-08-01)

**Aprovado: A+B+selos agora; C vira L1-3** — separa "fundamentar o que existe"
(correções + editorial + selos) de "expandir" (linhas novas, decididas linha a
linha em parte própria). Aplicado ao canônico EN nesta data: cabeçalho da
Parte II (função da coluna change-signal + registro da re-verificação), as 14
correções de A, os 9 reparos de B, e selos `[WEB ✓ 2026-08-01]` em todas as
linhas verificadas — a linha "compendium/changelog/narrative" perdeu o selo
`[CANONICAL]` (`conventions` é honestamente inverificável) e ganhou
cross-references no change-signal. PT derivado: pendente para o fim do ciclo.
