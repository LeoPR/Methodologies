---
title: Bibliografia da metodologia (canonical, com links)
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [00-core.methodology.md]
---

# Bibliografia da metodologia (canonical, com links)

> Lista de referencias compartilhada por toda a suite. Os demais docs
> citam autores/anos inline e linkam aqui; **nao duplicam a lista**.
> A subsecao "AI tools / agentes" e' de **alta cadencia** — re-verificar
> a cada auditoria (ver [00-core](00-core.methodology.md) §8).

## Information Architecture & wayfinding

- Peter Morville & Louis Rosenfeld — *Information Architecture for
  the Web and Beyond* (4ª ed., O'Reilly, 2015)
- Peter Morville — *Ambient Findability* (O'Reilly, 2005)
- Donald Norman — *The Design of Everyday Things* (affordances,
  signifiers)

## Documentacao

- Daniele Procida — Diataxis: [diataxis.fr](https://diataxis.fr/)
  + talks WriteTheDocs
- Michael Nygard — "Documenting Architecture Decisions" (2011):
  [cognitect.com/blog/2011/11/15/documenting-architecture-decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- MADR — [adr.github.io/madr](https://adr.github.io/madr/)
- Joel Parker Henderson — ADR collection:
  [github.com/joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record)

## Ciencia aberta / reprodutibilidade

- Ben Marwick, Carl Boettiger, Lincoln Mullen — "Packaging Data
  Analytical Work Reproducibly" (*The American Statistician*, 2018)
- The Turing Way — [book.the-turing-way.org](https://book.the-turing-way.org/)
- FAIR4RS Principles — Chue Hong et al., *Scientific Data* (2022):
  [nature.com/articles/s41597-022-01710-x](https://www.nature.com/articles/s41597-022-01710-x)
- Patrick Mineault — *The Good Research Code Handbook*:
  [goodresearch.dev](https://goodresearch.dev/)
- Cookiecutter Data Science:
  [cookiecutter-data-science.drivendata.org](https://cookiecutter-data-science.drivendata.org/)
- Software Carpentry / Data Carpentry —
  [carpentries.org](https://carpentries.org/)
- Claes Wohlin, Per Runeson, Martin Höst, Magnus C. Ohlsson, Björn
  Regnell, Anders Wesslén — *Experimentation in Software Engineering*
  (Springer, 2012). Threats to validity framework.
- Luciana B. Sollaci & Mauricio G. Pereira — "The introduction,
  methods, results, and discussion (IMRAD) structure: a fifty-year
  survey" (*J Med Libr Assoc* 92(3), 2004).
- Chris Chambers — *The Seven Deadly Sins of Psychology* (Princeton
  University Press, 2017). Pre-registration / Registered Reports.
- Robert A. Day & Barbara Gastel — *How to Write and Publish a
  Scientific Paper* (8ª ed., Cambridge, 2016).
- Imre Lakatos — *The Methodology of Scientific Research Programmes*
  (Cambridge University Press, 1978). Nucleo duro + cinto protetor —
  base teorica do registry de hipoteses.

## Engenharia de software / releases

- Conventional Commits 1.0 — [conventionalcommits.org](https://www.conventionalcommits.org/)
- Semantic Versioning 2.0 — [semver.org](https://semver.org/)
- Keep a Changelog — [keepachangelog.com](https://keepachangelog.com/)
- 12-Factor App (Heroku) — [12factor.net](https://12factor.net/)
- Frederick P. Brooks Jr. — *The Mythical Man-Month* (Addison-Wesley,
  1975; ed. comemorativa 1995). "Plan to throw one away."
- Koen Claessen & John Hughes — "QuickCheck: A Lightweight Tool for
  Random Testing of Haskell Programs" (ICFP 2000). Property-based
  testing — origem do conceito "invariant as acceptance criterion".
- Kent Beck — *Test-Driven Development: By Example* (Addison-Wesley,
  2002). xUnit, unit testing como pratica de design.

## Codigo como documentacao / nao-duplicacao

- Andrew Hunt & David Thomas — *The Pragmatic Programmer* (1999; ed. 20
  anos 2019). Principio DRY: "every piece of knowledge must have a single,
  unambiguous, authoritative representation within a system" — sobre
  conhecimento, nao texto de codigo.
- David L. Parnas & Paul C. Clements — "A Rational Design Process: How and
  Why to Fake It" (*IEEE TSE* SE-12(2):251-257, 1986). Codigo
  under-especifica intencao/rationale; documentacao e' o medium do design.
- David L. Parnas — "Software Aging" (*Proc. 16th ICSE*, 1994, pp. 279-287).
  Doc que nao acompanha o codigo apodrece ("ignorant surgery").
- Donald E. Knuth — "Literate Programming" (*The Computer Journal*
  27(2):97-111, 1984). Fonte unica: weave (doc) + tangle (codigo) — anti-drift
  por construcao.
- Bertrand Meyer — *Object-Oriented Software Construction* (2ª ed., 1997).
  Design by Contract: pre/pos-condicoes + invariantes = spec auto-checavel.
- Gojko Adzic — *Specification by Example* (Manning, 2011). Living
  documentation: o exemplo automatizado vira spec executavel + single source.
- Simon Brown — C4 model: [c4model.info](https://c4model.info/). Altitudes
  Context/Container/Component/Code; nivel Code raramente documentado a mao.
- John Ousterhout — *A Philosophy of Software Design* (2018). Comentario
  captura o que estava "na mente do designer mas nao cabe no codigo".
- Fengcai Wen, Csaba Nagy, Gabriele Bavota, Michele Lanza — "A Large-Scale
  Empirical Study on Code-Comment Inconsistencies" (*ICPC* 2019). Drift
  empirico ligado a refactor que toca codigo, nao a prosa.
- Mouna Dhaouadi, Bentley J. Oakes, Michalis Famelis — "End-to-End Rationale
  Reconstruction" (arXiv:2209.00398, 2022). Extrair o "porque" de
  codigo+commits permanece problema aberto.
- Sandi Metz — "The Wrong Abstraction" (2016) + Kent C. Dodds — "AHA
  Programming" (2020). "Prefer duplication over the wrong abstraction" /
  Rule of Three aplicado tambem a prosa.
- Josiah Ulfers — "Tests versus specs" (2018). Codigo nao e' oraculo da
  propria intencao; precisa de artefato externo que a codifique.

## Versionamento e higiene de repositorio

- Scott Chacon & Ben Straub — *Pro Git* (2ª ed., Apress, 2014;
  livre online): [git-scm.com/book](https://git-scm.com/book).
  Referencia canonica.
- Tim Pope — "A Note About Git Commit Messages" (2008):
  [tbaggery.com](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).
  Padrao de commit message.
- Paul Hammant et al. — Trunk Based Development:
  [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/).
- Vincent Driessen — "A successful Git branching model" (2010):
  [nvie.com](https://nvie.com/posts/a-successful-git-branching-model/).
  Git Flow original — autor publicou nota em 2020 sugerindo
  trunk-based pra muitos casos.
- Pre-commit framework (Anthony Sottile):
  [pre-commit.com](https://pre-commit.com/).
- Git LFS — [git-lfs.com](https://git-lfs.com/). Arquivos grandes
  fora do objeto store.
- DVC (Data Version Control) — [dvc.org](https://dvc.org/).
  Versionamento de dataset / modelo separado do codigo.
- lakeFS — [lakefs.io](https://lakefs.io/). Versionamento "git-like" de
  data lake (object storage), alternativa/complemento ao DVC em escala.
- Quilt — [quiltdata.com](https://www.quiltdata.com/). Versionamento +
  catalogo de datasets em S3.
- GitHub gitignore templates por linguagem:
  [github.com/github/gitignore](https://github.com/github/gitignore).
- detect-secrets (Yelp) — [github.com/Yelp/detect-secrets](https://github.com/Yelp/detect-secrets).
  Pre-commit hook contra commit de credenciais.

## Project management / agile / kanban

- David J. Anderson — *Kanban: Successful Evolutionary Change for
  Your Technology Business* (Blue Hole Press, 2010). Estados de
  workflow + WIP limits.
- John Doerr — *Measure What Matters* (Portfolio, 2018). OKRs
  (Objectives + Key Results) — acceptance criteria mensuravel.
- Jim Benson & Tonianne DeMaria Barry — *Personal Kanban: Mapping
  Work | Navigating Life* (Modus Cooperandi Press, 2011). Kanban
  pra solo / pequena escala.
- DSDM Consortium — MoSCoW prioritization (1994). Must / Should /
  Could / Won't have. Documento original DSDM.
- Steph Ango — "File over app" (2024) — [stephango.com/file-over-app](https://stephango.com/file-over-app). Filosofia
  por tras de markdown-em-git over SaaS tools.

## Conhecimento pessoal

- Vannevar Bush — "As We May Think" (*The Atlantic*, Julho 1945).
  Memex — ancestral conceitual de checkpoints + Zettelkasten + wiki.
- David Allen — *Getting Things Done* (rev. ed., Penguin, 2015).
  Someday/Maybe, Tickler file, weekly review.
- Niklas Luhmann — Zettelkasten (sintese em Sönke Ahrens,
  *How to Take Smart Notes*, 2017)
- Tiago Forte — *Building a Second Brain* / PARA method (2022)
- Andy Matuschak — *Evergreen notes*:
  [notes.andymatuschak.org](https://notes.andymatuschak.org/)

## Avaliacao de fontes / disciplina de pesquisa

- David L. Sackett, William M. C. Rosenberg, J. A. Muir Gray,
  R. Brian Haynes, W. Scott Richardson — "Evidence based medicine:
  what it is and what it isn't" (*BMJ* 312:71, 1996). Origem da
  evidence hierarchy. GRADE methodology (Guyatt et al. 2008)
  formaliza graus de evidencia.
- Sarah Blakeslee — "The CRAAP Test" (*LOEX Quarterly*, 2004),
  Cal State Chico librarians. Currency / Relevance / Authority /
  Accuracy / Purpose.
- Mike Caulfield — *Web Literacy for Student Fact-Checkers*
  (open textbook, 2017). SIFT method (Stop / Investigate / Find /
  Trace) — [hapgood.us](https://hapgood.us/2019/06/19/sift-the-four-moves/).
- Norman K. Denzin — *The Research Act: A Theoretical Introduction
  to Sociological Methods* (McGraw-Hill, 1978). Triangulation
  (data / investigator / theory / methodological).
- Samuel Arbesman — *The Half-Life of Facts* (Current, 2012). Meia-vida
  do conhecimento — base do espectro de perecibilidade de dados.
- G. K. Chesterton — *The Thing* (Sheed & Ward, 1929). Chesterton's
  fence — nao remover/descartar sem entender porque existe.

## AI tools / agentes (alta cadencia — re-verificar a cada auditoria)

> **Aviso de cadencia**: esta secao referencia tooling de IA que muda
> em meses. Datas de captura embutidas; tratar como
> `[VERIFICAR: 2026-06-03]` por default (ver [research-discipline](research-discipline.methodology.md)
> → Dados vivos vs consolidados).

- AGENTS.md — [agents.md](https://agents.md/). Padrao de instrucoes pra
  agentes; em 2025 passou a ser governado pela **Agentic AI Foundation**
  (Linux Foundation): [openai.com/index/agentic-ai-foundation](https://openai.com/index/agentic-ai-foundation/).
- Model Context Protocol (MCP) — [modelcontextprotocol.io](https://modelcontextprotocol.io/);
  roadmap 2026: [blog.modelcontextprotocol.io](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/).
  Padrao aberto de conexao agente ↔ ferramentas/dados/recursos.
- Agent Skills (SKILL.md) — [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills).
  Capacidades empacotadas, progressive disclosure, portaveis entre tools.
- Claude Code — memory + hooks: [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory).
- Memory tool (filesystem-backed) — [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool).
- Context engineering — Anthropic cookbook:
  [platform.claude.com/cookbook](https://platform.claude.com/cookbook/) (context-engineering).
- GitHub Copilot custom instructions:
  [docs.github.com/copilot/customizing-copilot](https://docs.github.com/en/copilot/customizing-copilot)
- Cursor rules: [docs.cursor.com/context/rules](https://docs.cursor.com/context/rules)
- Cline memory bank: [docs.cline.bot/features/memory-bank](https://docs.cline.bot/features/memory-bank)

## Proveniencia / autenticidade de conteudo

- C2PA (Coalition for Content Provenance and Authenticity) —
  [c2pa.org](https://c2pa.org/); C2PA 2.x ratificada como ISO/IEC 22144.
- Content Authenticity Initiative —
  [contentauthenticity.org](https://contentauthenticity.org/).
- SLSA (Supply-chain Levels for Software Artifacts) — [slsa.dev](https://slsa.dev/).
- Sigstore — [sigstore.dev](https://www.sigstore.dev/). Assinatura/atestacao de artefatos.
- RO-Crate — [researchobject.github.io/ro-crate](https://www.researchobject.github.io/ro-crate/);
  CodeMeta — [codemeta.github.io](https://codemeta.github.io/). Metadata de research software.
- OpenTelemetry GenAI — [opentelemetry.io](https://opentelemetry.io/) (semantic conventions de GenAI).

## Comunidade / citacao academica

- Open Source Guides: [opensource.guide](https://opensource.guide/)
- Citation File Format: [citation-file-format.github.io](https://citation-file-format.github.io/)
- JOSS — Journal of Open Source Software: [joss.theoj.org](https://joss.theoj.org/)
- DataCite metadata schema: [datacite.org](https://datacite.org/)
- Dublin Core: [dublincore.org](https://www.dublincore.org/)

## Tool bridges (trackers externos)

- Jira REST API v3: [developer.atlassian.com/cloud/jira/platform/rest/v3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- Jira CSV import: [support.atlassian.com](https://support.atlassian.com/jira-cloud-administration/docs/import-data-from-a-csv-file/)
- Linear API (GraphQL): [developers.linear.app](https://developers.linear.app/)
- Monday GraphQL API: [developer.monday.com](https://developer.monday.com/api-reference/docs)
- Asana REST API: [developers.asana.com](https://developers.asana.com/docs)
- Atlassian Document Format (ADF): formato de description do Jira REST
- `jiracli` (community): [github.com/ankitpokhrel/jira-cli](https://github.com/ankitpokhrel/jira-cli)
