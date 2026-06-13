---
title: 'IDEIA (discutir depois) — exportar/traduzir para normas externas (o "L3"?)'
created: 2026-06-13
status: 'REGISTRO de ideia de DESIGN do metodo. NAO decidido: fortificar no Strata ou spinoff? Discutir depois.'
---

# Ideia — exportar/traduzir para a norma externa, sem bifurcar a verdade

> **Questão de design do método** levantada pelo dono. Não é teste nem decisão — é para **discutir
> depois**. Liga-se a §5 (fonte única) e §3 (rastreabilidade).

## A ideia (do dono)
Posso organizar **localmente** no ideal do Strata (denso, rastreável, fonte única); a **empresa/
publicadora não** segue isso. Mas consigo **traduzir** o meu material para a **linguagem/formato que ela
exige** — sem prejuízo do Strata, só um **esforço a mais de entrega**. Analogia: o **artigo científico** —
tenho tudo organizado e rastreável e faço a "tradução e exportação" para as normas da publicadora (arXiv,
template de journal, IMRaD). Uma espécie de **"tradução e exportação da biblioteca"** — mais um tipo de modelagem.

## Raciocínio crítico (preliminar)
1. **Não é uma 4ª camada de durabilidade — é um eixo ORTOGONAL.** Mneme/Morfé/Órganon (L0/L1/L2) é uma
   **escada de durabilidade** (o que perdura → forma → ferramenta). "Exportar para a norma externa" não é
   "menos durável que o L2"; é outra **dimensão**: *fonte canônica interna* vs *renderização externa
   exigida*. Ela **corta** as camadas (exporta-se ideia L0, padrão L1, estado L2 para o formato externo).
   Chamar de "L3" **sobrecarrega** a escada de durabilidade com algo que não é durabilidade → melhor uma
   **preocupação transversal nomeada**, não um 4º andar.
2. **O PRINCÍPIO já é corolário do Strata.** §5 (fonte única) + §3 (rastreabilidade) já implicam: a entrega
   no formato externo é uma **renderização DERIVADA**, **não** uma segunda fonte de verdade. A fonte
   canônica (organizada à Strata) **continua canônica**; você **gera** a vista conforme (PDF do journal,
   doc da empresa) **a partir** dela, rastreável. Regra: **exporte; não bifurque a verdade.** (Anti-padrão
   clássico: a "cópia para a empresa" virar um 2º original que diverge.)
3. **A PRÁTICA/ferramenta é L2 (datada) e pode ser spinoff.** Como traduzir de fato (pandoc, templates
   arXiv, style guide da empresa, geradores) é **Órganon** — datado. Se crescer (um *toolkit* de
   exportação), vira **spinoff**; mantê-lo fora do núcleo evita o Strata **virar sistema**.
4. **Precedente real:** "single source → conforming export" é prática estabelecida (docs-as-code,
   single-source publishing, DITA; e o próprio IMRaD/arXiv na ciência). Não é invenção — dá para apoiar.

## Encaminhamento (a discutir)
- **Fortificar (provável, barato):** um **corolário L0** curto — *"toda entrega em formato externo é uma
  renderização derivada e rastreável da fonte canônica; nunca uma segunda fonte"* — apontando padrões L1
  (IMRaD, templates) e ferramentas L2 (geradores) como **exemplos**, não como núcleo.
- **Spinoff (se a ferramenta crescer):** um *toolkit* de tradução/exportação separado, em `recipe/` próprio.
- **Nome candidato (SE virar coisa nomeada, no mesmo gosto grego):** **Hermeneia** (ἑρμηνεία —
  interpretação/tradução/expressão; raiz de *hermenêutica*; *Peri Hermeneias* de Aristóteles) — combina com
  Mneme/Morfé/Órganon, mas como **eixo transversal**, não como "L3" da escada.
- **Decisão: em aberto.** Quando discutirmos, vira ADR em [`decisions/`](../../decisions/) (fortificar) ou
  um produto novo em [`recipe/`](../../recipe/) (spinoff).
