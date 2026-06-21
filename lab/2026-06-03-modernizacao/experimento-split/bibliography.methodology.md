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

## LLM-as-judge / meta-avaliacao (alta cadencia — re-verificar a cada auditoria)

> **Aviso de cadencia**: campo que muda em meses. As obras de 2026 sao
> **preprints** (Apple, RAND) — tratar numero especifico como melhor-atual,
> nao assentado. Usada pelo [DOSSIE-judge](../../2026-06-04-strata-hipoteses/DOSSIE-judge-justificativa-cientifica.md)
> e pelo [RESULTADOS-confronto-literatura](../../2026-06-04-strata-hipoteses/RESULTADOS-confronto-literatura.md).

Fundacionais (juiz e concordancia):
- Lianmin Zheng et al. — "Judging LLM-as-a-Judge with MT-Bench and Chatbot
  Arena" (NeurIPS 2023; arXiv:2306.05685). Juiz forte ~80%+ vs preferencia
  humana; catalogo de position/verbosity/self-enhancement bias.
- Yang Liu et al. — "G-Eval: NLG Evaluation using GPT-4 with Better Human
  Alignment" (EMNLP 2023; arXiv:2303.16634). Juiz com chain-of-thought
  correlaciona melhor que BLEU/ROUGE.
- Arjun Panickssery, Samuel R. Bowman, Shi Feng — "LLM Evaluators Recognize
  and Favor Their Own Generations" (NeurIPS 2024; arXiv:2404.13076).
  Self-preference; GPT-4 reconhece a propria saida ~73,5%.
- Pat Verga et al. — "Replacing Judges with Juries: Evaluating LLM
  Generations with a Panel of LLMs" (PoLL; arXiv:2404.18796). Juri
  cross-vendor como mitigacao de self-preference.
- Jiawei Gu et al. — "A Survey on LLM-as-a-Judge" (arXiv:2411.15594, 2024).
- Lin Shi et al. — "Judging the Judges: position bias em LLM-as-a-Judge"
  (arXiv:2406.07791 / 2024). Position bias e' dirigido pelo gap de qualidade.

Erro correlacionado / limite do consenso (2025-2026 — confrontam o cross-vendor):
- Kohli et al. (Apple) — "Nine Judges, Two Effective Votes: correlated errors
  em paineis de LLM" (arXiv:2605.29800, 2026, preprint). neff~2,18 em 9 juizes /
  7 familias; pares mais correlacionados sao cross-familia.
- Kim et al. — correlated errors em 350+ LLMs (arXiv:2506.07962, ICML 2025).
  Erro correlacionado cresce com acuracia, mesmo entre fornecedores distintos.

Reference-guided vs reference-free:
- "No Free Labels: ground-truth dependence em LLM-as-judge"
  (arXiv:2503.05061, 2025). Juiz so concorda com especialista onde ele mesmo
  saberia responder; referencia mitiga.
- "RevisEval: response-adapted references" (ICLR 2025; arXiv:2410.05193).
- "Judge's Verdict: de correlacao para Cohen's kappa" (arXiv:2510.09738, 2025).
  Correlacao/% cru e' insuficiente; usar concordancia corrigida por acaso.

Vieses (atualizacao 2025):
- "Breaking the Mirror: self-preference justificado vs injustificado"
  (NeurIPS 2025; arXiv:2509.03647). Favorecer a propria saida nem sempre e' vies.

Confiabilidade dependente de tarefa:
- RAND — "Judge Reliability Harness" (arXiv:2603.05399, 2026, preprint).
  Nenhum juiz e' uniformemente confiavel entre benchmarks.

Metrica de concordancia (correcao por acaso):
- Klaus Krippendorff — *Content Analysis: An Introduction to Its Methodology*
  (Sage, 2004). alfa de Krippendorff; heuristica >=0,800 confiavel /
  0,667-0,800 preliminar (heuristica classica, nao consenso atual verificado).
- Mary L. McHugh — "Interrater reliability: the kappa statistic"
  (*Biochem Med* 22(3):276-282, 2012).
- A. Zapf et al. — "Measuring inter-rater reliability for nominal data —
  which coefficients and confidence intervals are appropriate?"
  (*BMC Med Res Methodol* 16:93, 2016). Paradoxo do kappa sob desbalanceamento.

Calibracao (eixo ortogonal — plausivel, nao reconfirmado no confronto 2026-06-21):
- Chuan Guo et al. — "On Calibration of Modern Neural Networks" (ICML 2017;
  arXiv:1706.04599). ECE; redes modernas mal calibradas.
- Katherine Tian et al. — "Just Ask for Calibration" (EMNLP 2023;
  arXiv:2305.14975). Confianca verbalizada bate logits sob RLHF.

Teoria de medida / validade (fundamento do argumento ideal-regulativo):
- Lee J. Cronbach & Paul E. Meehl — "Construct Validity in Psychological
  Tests" (*Psychological Bulletin* 52(4):281-302, 1955).
- Samuel Messick — "Validity of Psychological Assessment" (*American
  Psychologist* 50(9):741-749, 1995). Validade de construto unificada.
- Anol Bhattacherjee — *Social Science Research: Principles, Methods, and
  Practices* (2ª ed., 2012). Erro aleatorio (confiabilidade) vs
  sistematico (validade).
- JCGM 100:2008 — *Guide to the Expression of Uncertainty in Measurement*
  (GUM). Resultado so esta completo com incerteza declarada.
- Lora Aroyo & Chris Welty — "Truth Is a Lie: Crowd Truth and the Seven
  Myths of Human Annotation" (*AI Magazine* 36(1):15-24, 2015). Discordancia
  humana como sinal; ground-truth distribucional.
- Immanuel Kant — principios regulativos (via SEP, "Kant's Account of
  Reason", Williams, ed. 2023): [plato.stanford.edu/entries/kant-reason](https://plato.stanford.edu/entries/kant-reason/).

## Fundamento epistemico do juiz (escala mensuravel, nao binario)

> Base de filosofia/matematica/computacao do argumento "nao-perfeito nao e'
> nao-serve". Usada por [FUNDAMENTO-juiz-escala-mensuravel](../../2026-06-04-strata-hipoteses/FUNDAMENTO-juiz-escala-mensuravel.md).
> Verificacao adversarial completa 2026-06-21 (dois runs): TODOS os eixos verificados.
> A/D/E/H: 3-0, 1 refutado informativo. B/C/F + instrumentos E/G (Condorcet, Aumann,
> Simon, Brier, Tetlock): 3-0 NUANCED em todos — verificados com ressalva de
> formulacao/atribuicao/escopo; nenhum refutado.

Teto irredutivel / informacao (eixos A/H — verificados 3-0):
- Eyke Hüllermeier & Willem Waegeman — "Aleatoric and Epistemic Uncertainty in
  Machine Learning" (*Machine Learning* 110:457-506, 2021; arXiv:1910.09457).
- Thomas M. Cover & Joy A. Thomas — *Elements of Information Theory* (2ª ed.,
  Wiley, 2006). Desigualdade de processamento de dados: I(X;Y) >= I(X;Z).
- Luc Devroye, László Györfi & Gábor Lugosi — *A Probabilistic Theory of Pattern
  Recognition* (Springer, 1996); Richard O. Duda, Peter E. Hart & David G. Stork
  — *Pattern Classification* (2ª ed., Wiley, 2001). Erro de Bayes como piso
  irredutivel (resumo recente em arXiv:2506.03159).
- Raghu N. Kacker — "True value and uncertainty in the GUM" (*Metrologia*, 2018;
  PMC9074737). Valor verdadeiro inacessivel em principio.
- JCGM 200 (VIM3), def. 2.27 — incerteza definicional: piso minimo que tecnica
  nenhuma cruza.
- Armen Der Kiureghian & Ove Ditlevsen — "Aleatory or epistemic? Does it matter?"
  (*Structural Safety* 31(2):105-112, 2009). A divisao e' escolha do modelador.
- M. Jimenez, D. Jurgens & W. Waegeman — position paper, ICML 2025
  (arXiv:2505.23506). Metodos de 2ª ordem que separam aleatoria de epistemica sao
  "fundamentalmente incompletos"; vies nao-contabilizado rotula deficiencia
  redutivel como teto irredutivel.
- "Re-examining the aleatoric/epistemic dichotomy" (ICLR 2025 blogpost). A divisao
  e' relativa ao modelo/informacao (confianca media — ancora em blogpost).

Subdeterminacao / verdade por convergencia + criticas: [verificado com ressalva B/C]
- Pierre Duhem — *La Theorie Physique* (1906/Wiener trans. Princeton, 1954, p.187).
  Holismo da confirmacao: hipoteses so enfrentam teste empirico em conjunto.
- W. V. O. Quine — "Two Dogmas of Empiricism" (*Phil. Review* 60:20-43, 1951);
  "On Empirically Equivalent Systems of the World" (*Erkenntnis* 9(3):313-328, 1975).
  SEP "Underdetermination": [plato.stanford.edu/entries/scientific-underdetermination](https://plato.stanford.edu/entries/scientific-underdetermination/).
  Ressalva: tese forte tratada por Quine como conjectura, nao resultado estabelecido.
- Charles S. Peirce — CP 5.407 (1878, *Popular Science Monthly* 12:286-302) —
  verbatim: "The opinion which is fated to be ultimately agreed to by all who
  investigate, is what we mean by the truth". CP 5.565 (1901): reformulacao como
  "limite ideal". Misak, Cheryl — *Truth and the End of Inquiry* (Oxford, 2004,
  ISBN 9780199270590): defesa neo-pragmatista.
  Criticos: Rorty (*Consequences of Pragmatism*, 1982; "Science as Solidarity", 1987)
  — posicao documentada; analogia do "maior inteiro" e' parafrrase, nao citacao direta.
  Russell — "William James's Conception of Truth" (*Phil. Essays*, 1910/Routledge):
  critica semantica (indicador vs. significado de "verdadeiro"), nao singular-vs-plural.
  Field, H. — "Realism and Relativism" (*J. Philosophy* 79(10):553-567, 1982):
  "fatos perdidos" (dinossauros). Smart, J.J.C. — *Ethics, Persuasion and Truth*
  (Routledge, 1984).

Limites formais de decidibilidade:
- Kurt Gödel — teoremas de incompletude (SEP): [plato.stanford.edu/entries/goedel-incompleteness](https://plato.stanford.edu/entries/goedel-incompleteness/).
- Alan Turing / Alonzo Church — indecidibilidade, halting problem.
- H. G. Rice — Rice's theorem (1953). Alfred Tarski — indefinibilidade da verdade.
- Mario Brčić & Roman V. Yampolskiy — "Impossibility Results in AI: A Survey"
  (*ACM Computing Surveys*, 2023; doi:10.1145/3603371). 5 familias; a Deducao
  nega certeza 100%, mas garantias probabilisticas sao atingiveis — "quanto
  basta?" (binario → escala). [verificado 3-0]

Convergencia de juri sob dependencia: [verificado com ressalva E/G-Condorcet/Aumann]
- Marquis de Condorcet — *Essai sur l'application de l'analyse* (Paris, 1785).
  Formalizado em Dietrich & Spiekermann (SEP, "Jury Theorems", Fall 2025 ed.):
  [plato.stanford.edu/entries/jury-theorems](https://plato.stanford.edu/entries/jury-theorems/).
  Competencia p>0,5 **e** independencia — duas condicoes, nao uma.
- Ladha, K.K. — "The Condorcet Jury Theorem, Free Speech, and Correlated Votes"
  (*Am. J. Political Science* 36(3):617-634, 1992). Degradacao sob correlacao
  positiva; garantia preservada apenas com correlacao suficientemente baixa.
- Dietrich, F. & List, C. — "A Model of Jury Decisions Where All Jurors Have the
  Same Evidence" (*Synthese* 142:175-202, 2004). Causa comum → limite assintótico
  travado abaixo de 1.
- Robert J. Aumann — "Agreeing to Disagree" (*Annals of Statistics* 4(6):1236-1239,
  1976; DOI 10.1214/aos/1176343654). Prior comum + conhecimento comum das posterioris
  → concordancia forcada. Nao prova que concordancia implica prior como causa;
  implicacao para LLMs e' analogia com lastro empirico. Ressalva: Lederman, H. —
  "People with Common Priors Can Agree to Disagree" (*Review of Symbolic Logic*
  8(1):11-45, 2015; DOI 10.1017/S1755020314000380): sub-condicoes do prior comum
  sao load-bearing e podem ser relaxadas individualmente.
- Jon Kleinberg & Manish Raghavan — "Algorithmic monoculture and social welfare"
  (*PNAS* 118(22):e2018340118, 2021). Correlacao de erros entre modelos que
  partilham origem; fundamenta o erro correlacionado cross-vendor. [verificado 3-0]
- Balasubramanian, R., Podkopaev, A. & Kasiviswanathan, S.P. — "Dependence-Aware
  Label Aggregation for LLM-as-a-Judge via Ising Models" (arXiv:2601.22336, 2026).
  Correlacao de juizes LLM por dados de treinamento sobrepostos; votacao majoritaria
  padrao descalibrada.
- Zhao et al. — "CARE: Confounder-Aware Aggregation for Reliable LLM Evaluation"
  (arXiv:2603.00039, 2026). Dados de treinamento como confundidor oculto que torna
  concordancia entre juizes enganosa como evidencia de validade ground-truth.

Falibilismo / aproximacao: [verificado com ressalva F]
- Karl Popper — *Conjecturas e Refutacoes* (Routledge, 1963, cap. 10);
  *Objective Knowledge* (Clarendon, 1972, cap. 9). Verossimilhanca: escala de
  proximidade a verdade; SEP "Truthlikeness":
  [plato.stanford.edu/entries/truthlikeness](https://plato.stanford.edu/entries/truthlikeness/).
  Tichý, P. & Miller, D. — refutacao da definicao formal (*BJPS* 25(2):155-177,
  1974). Oddie, G. (SEP 2019); Niiniluoto, I. (*Truthlikeness*, Reidel, 1987):
  abordagens successoras que rehabilitaram o conceito.
- Imre Lakatos — *The Methodology of Scientific Research Programmes*
  (Cambridge, 1978; ensaio principal orig. 1970). Criterio de progresso:
  **excedente de conteudo empirico + previsao de fatos novos**, nao recuo do erro.
  Lakatos reteve a verdade como alvo mas substituiu aproximacao da verdade por
  fertilidade preditiva como criterio operacional.
- Immanuel Kant — *Critica da Razao Pura* (A/B 1781/1787). Ideias regulativas:
  **Apendice a Dialectica Transcendental, A642-668/B670-696** — focus imaginarius
  (A644/B672): investigacao orientada assintoticamente sem posse do objeto
  transcendente. (A569/B597 define o conceito formal de ideal, nao a funcao
  regulativa na investigacao empirica.)

Racionalidade limitada / medir julgamento em escala: [verificado com ressalva E/G]
- Herbert A. Simon — "A Behavioral Model of Rational Choice" (*QJE* 69(1):99-118,
  1955; DOI 10.2307/1884852); "Rational Choice and the Structure of the Environment"
  (*Psych. Review* 63(2):129-138, 1956; PubMed 13310708 — **aqui e' cunhado
  "satisficing"**); Nobel 1978 (*AER* 69(4):493-512). SEP "Bounded Rationality":
  [plato.stanford.edu/entries/bounded-rationality](https://plato.stanford.edu/entries/bounded-rationality/).
  Satisficing = atingir nivel de aspiracao (nao otimizacao restrita).
- John McCarthy — "Measures of the Value of Information" (*PNAS* 42:654-655, 1956).
  Prioridade formal para prova de propriedade de regras de pontuacao.
- Glenn W. Brier — "Verification of forecasts expressed in terms of probability"
  (*Monthly Weather Review* 78(1):1-3, 1950; DOI 10.1175/1520-0493(1950)078
  <0001:vofeit>2.0.co;2). Escore de Brier: [0,2] na formulacao multicategoria
  original; forma binaria moderna dominante: [0,1].
- L.J. Savage — "Elicitation of Personal Probabilities and Expectations" (*JASA*
  66(336):783-801, 1971). Regras de pontuacao proprias como mecanismo de elicitacao.
- Gneiting, T. & Raftery, A.E. — "Strictly Proper Scoring Rules, Prediction, and
  Estimation" (*JASA* 102(477):359-378, 2007). Tratamento moderno rigoroso de
  propriedade estrita; Brier score = caso da regra quadratica (equacao 28).
- Philip E. Tetlock — *Expert Political Judgment* (Princeton UP, 2005); Tetlock &
  Gardner — *Superforecasting* (Crown, 2015). Good Judgment Project:
  Mellers et al. 2014 (*Psych. Science* 25(5):1106-1115); Mellers et al. 2015
  (*Perspectives on Psych. Sci.* 10(3):267-281; DOI 10.1177/1745691615577794);
  Chang et al. 2016 (*Judgment and Decision Making*; DOI 10.1017/S1930297500004599).
  Superprevisores (~2% superior) superaram analistas de IC ~25-30% (relatorio
  proprio GJP, nao ECR controlado independente). Melhora de habilidade (+6-12%)
  documentada para horizontes curtos a medios; degrada para acaso alem de ~5 anos.
- Katsagounos et al. — "Superforecasting reality check" (*EJOR*, 2020; PMC7333631).
  Replicacao com N=195 confirma o fenomeno em escala menor.

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
