---
title: Fundamentação do núcleo atemporal (L0) — revisão de literatura
status: closed
created: 2026-06-03
updated: 2026-06-03
tags: [knowledge-architecture, L0, literature-review, fontes-primarias, auto-revisao]
outcome: confirmed
---

# Fundamentação do núcleo atemporal (L0) — revisão de literatura

> **Ciclo de auto-revisão**: aplica a **§6 (disciplina de fonte)** e a **§3
> (rastreabilidade)** do próprio L0 sobre as **afirmações do L0**. Para cada
> princípio: a **fonte primária**, o grau de evidência e o **status de
> verificação**. Que o método se sustente quando aplicado a si mesmo é, em si,
> evidência de que funciona.

## Pergunta

As afirmações do núcleo atemporal (`recipe/knowledge-architecture.md`, Parte I)
têm sustentação em **fontes primárias** verificáveis — e cada uma é de fato
*anterior* à IA/ao computador, como a tese das camadas afirma?

## Método

Para cada princípio, buscar a **fonte original** (não o sumário de terceiros —
disciplina primário > secundário). Registrar citação completa, graduar a
evidência e marcar honestamente o status:

- **`[WEB ✓ 2026-06-03]`** — citação e claim conferidos na web nesta rodada
  (fonte primária localizada).
- **`[CANÔNICO]`** — obra consagrada, citada de conhecimento; não re-verificada
  nesta rodada. *Sabe* com alta confiança, mas a etiqueta é honesta (§6).
- **`[ANALOGIA]`** — a ligação é interpretação nossa, não termo do autor.

## Resultado — fundamentação por seção do L0

### §1 — Três tipos de artefato / separação física

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| Separar preocupações/tipos de artefato é a técnica básica de ordenar o pensamento | Dijkstra, E. W. (1974). *On the role of scientific thought* (EWD447) — cunha "separation of concerns" | `[WEB ✓]` |
| Decompor pelo que cada parte **esconde** / pela decisão que tende a mudar | Parnas, D. L. (1972). "On the Criteria To Be Used in Decomposing Systems into Modules." *CACM* 15(12):1053–1058 | `[WEB ✓]` |
| Organização/rotulagem/estrutura de conteúdo é disciplina própria (achabilidade) | Rosenfeld, L. & Morville, P. (1998). *Information Architecture for the World Wide Web*. O'Reilly | `[WEB ✓]` |

### §2 — As quatro perguntas / achabilidade / tipos de documentação

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| "Onde está X?": o leitor segue **rastros (information scent)** até o alvo; o custo de não achar é refazer | Pirolli, P. & Card, S. (1999). "Information Foraging." *Psychological Review* 106(4):643–675 | `[WEB ✓]` |
| Achabilidade é problema de design, não detalhe técnico | Rosenfeld & Morville (1998); Morville, *Ambient Findability* (2005) | `[WEB ✓]` |
| 4 tipos de documentação (aprender/resolver × prática/teoria) | Procida, D. — Diataxis (formalização **L1**; necessidade é atemporal) | `[CANÔNICO]` |

### §3 — Rastreabilidade (fonte + rationale + versão; append-only)

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| **Proveniência**: de onde o dado veio (a "por quê / de onde") | Buneman, P., Khanna, S. & Tan, W.-C. (2001). "Why and Where: A Characterization of Data Provenance." *ICDT 2001*, LNCS 1973:316–330 | `[WEB ✓]` |
| Registrar **quem fez a mudança, quando, onde e por quê** + versão | Rochkind, M. J. (1975). "The Source Code Control System." *IEEE TSE* SE-1(4):364–370 (1º controle de versão; registra literalmente who/when/where/why) | `[WEB ✓]` |
| Registro **append-only e auditável** que não se reescreve (corrige-se adiante) | Pacioli, L. (1494). *Summa de Arithmetica* — "Particularis de Computis et Scripturis" (partida dobrada; livro balanceado e auditável). Como **ancestral** do registro imutável | `[WEB ✓]` `[ANALOGIA]` |
| O **rationale** (porquê/alternativas) vive na documentação, não no código | Parnas, D. L. & Clements, P. C. (1986). "A Rational Design Process: How and Why to Fake It." *IEEE TSE* 12(2):251–257 | `[WEB ✓]` |

### §4 — Registro científico (hipótese-antes, reprodutível, honesto)

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| **Hipótese declarada ANTES** dos dados (distinguir predição de pós-dição) | Nosek, B. A. et al. (2018). "The preregistration revolution." *PNAS* 115(11):2600–2606 | `[WEB ✓]` |
| Registered Reports / pré-registro como prática | Chambers, C. (2017). *The Seven Deadly Sins of Psychology* | `[CANÔNICO]` |
| **Reprodutibilidade**: refazer o resultado a partir do registro | Claerbout, J. F. & Karrenbach, M. (1992). "Electronic documents give reproducible research a new meaning." *SEG Tech. Program Expanded Abstracts* (cunha "reproducible research") | `[WEB ✓]` |
| **Ameaças à validade** (interna/externa/construto/conclusão) | Campbell, D. T. & Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Rand McNally (origem da tipologia) | `[WEB ✓]` |
| ... aplicadas a engenharia de software | Wohlin, C. et al. (2012). *Experimentation in Software Engineering* | `[CANÔNICO]` |
| **Preservar o resultado negativo** (combater viés de publicação) | Rosenthal, R. (1979). "The file drawer problem and tolerance for null results." *Psychological Bulletin* 86(3):638–641 | `[WEB ✓]` |
| Estrutura intro → método → resultado → discussão | Sollaci, L. B. & Pereira, M. G. (2004). "The IMRAD structure: a fifty-year survey." *J Med Libr Assoc* 92(3):364–367 | `[WEB ✓]` |

### §5 — Fonte única por altitude (DRY, oráculo, literate programming)

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| Todo conhecimento tem **uma** representação autoritativa (DRY de conhecimento) | Hunt, A. & Thomas, D. (1999). *The Pragmatic Programmer* | `[CANÔNICO]` |
| **Uma fonte da qual ambas derivam** (weave = doc, tangle = código) | Knuth, D. E. (1984). "Literate Programming." *The Computer Journal* 27(2):97–111 | `[WEB ✓]` |
| O **oráculo** precisa ser artefato externo que decide a correção (código não é oráculo de si) | Weyuker, E. J. (1982). "On Testing Non-testable Programs." *The Computer Journal* 25(4):465–470 (formula o "problema do oráculo") | `[WEB ✓]` |
| O código sub-especifica intenção; a doc é o meio do design | Parnas & Clements (1986) — ver §3 | `[WEB ✓]` |
| Contrato auto-checável (pré/pós-condições + invariantes) | Meyer, B. (1997). *Object-Oriented Software Construction* (2ª ed.) — Design by Contract | `[CANÔNICO]` |

### §6 — Disciplina de fonte (epistemologia)

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| Usar a **melhor evidência disponível** / hierarquia de evidência | Sackett, D. L. et al. (1996). "Evidence based medicine: what it is and what it isn't." *BMJ* 312(7023):71–72 | `[WEB ✓]` |
| Tendência a buscar/interpretar evidência que confirma o que já se crê | Nickerson, R. S. (1998). "Confirmation Bias: A Ubiquitous Phenomenon in Many Guises." *Review of General Psychology* 2(2):175–220 | `[WEB ✓]` |
| Verificar lateralmente / ir à fonte original (parar, investigar, achar, rastrear) | Caulfield, M. (2017/2019). *Web Literacy for Student Fact-Checkers*; "SIFT (The Four Moves)" | `[WEB ✓]` |
| Avaliar a fonte (atualidade/relevância/autoridade/acurácia/propósito) | Blakeslee, S. (2004). "The CRAAP Test." *LOEX Quarterly* | `[CANÔNICO]` |
| Triangular com N fontes independentes | Denzin, N. K. (1978). *The Research Act* | `[CANÔNICO]` |
| Conhecimento tem **meia-vida** (perecibilidade do dado) | Arbesman, S. (2012). *The Half-Life of Facts* | `[CANÔNICO]` |
| Não descartar o que não se entende (descobrir por que existe) | Chesterton, G. K. (1929). *The Thing* (a "cerca de Chesterton") | `[CANÔNICO]` |

### §7 — Pipeline de geração e maturação do conhecimento

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| Dado → informação → conhecimento (maturação por níveis) | Ackoff, R. L. (1989). "From Data to Wisdom." *Journal of Applied Systems Analysis* 16:3–9 (hierarquia DIKW) | `[WEB ✓]` |
| **Não formalize N=1**; consolide na recorrência (regra de três) | Fowler, M. (1999). *Refactoring* — "Rule of Three" (atrib. Don Roberts; cf. Roberts & Johnson 1996) | `[WEB ✓]` |
| Planeje **jogar o primeiro fora** (exploração descartável → produção) | Brooks, F. P. (1975). *The Mythical Man-Month* — "plan to throw one away; you will, anyhow" | `[WEB ✓]` |

### §8 — Versionamento como história imutável e proveniência

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| Histórico recuperável de quem/quando/porquê (controle de versão como conceito) | Rochkind (1975) — ver §3 | `[WEB ✓]` |
| Registro auditável append-only | Pacioli (1494) — ver §3 | `[WEB ✓]` `[ANALOGIA]` |
| Reprodutibilidade como teste do registro | Claerbout & Karrenbach (1992) — ver §4 | `[WEB ✓]` |
| Isolar o que muda (parentesco do "sinal vs ruído" com modularidade) | Parnas (1972) — ver §1 | `[WEB ✓]` |

### §9 — Economia do esforço (quando organizar e quando não)

| Afirmação do L0 | Fonte primária | Status |
|---|---|---|
| Não otimizar (organizar) cedo demais; o overhead precisa compensar | Knuth, D. E. (1974). "Structured Programming with go to Statements." *ACM Computing Surveys* 6(4):261–301 (p. 268) | `[WEB ✓]` |
| Não construa o que ainda não é necessário (YAGNI) | Beck, K. — Extreme Programming | `[CANÔNICO]` |

## Discussão

- **22 fontes primárias web-verificadas** nesta rodada; o restante são obras
  canônicas (`[CANÔNICO]`) citadas de conhecimento.
- **A tese das camadas se sustenta**: as fontes vão de **1494** (Pacioli) e do
  **método científico** (Campbell & Stanley 1963; cadernos de laboratório do
  séc. XIX) a 1972–1999 (engenharia de software) — **todas anteriores** à IA
  moderna e ao VSCode. A camada L2 (ferramentas de hoje) é, de fato, *forma*
  sobre um núcleo que já existia.

## Limitações / ressalvas (honestidade epistêmica — §6)

- **`[ANALOGIA]` Pacioli/partida dobrada → registro append-only**: a ligação
  é nossa; Pacioli não falou em "ledger imutável". É um *ancestral conceitual*
  do registro auditável, não uma citação literal do conceito moderno.
- **IMRaD volume**: uso *J Med Libr Assoc* **92(3):364–367** (consistente com
  PubMed PMID 15243643); uma fonte web grafou "95.3" — descartado por
  triangulação.
- **`[CANÔNICO]`**: itens não re-verificados nesta rodada. Se algum virar
  *load-bearing* numa disputa, re-verificar antes (marcar `[VERIFICAR]`).
- **SIFT**: origem 2017 ("Four Moves and a Habit"); nome "SIFT" consolidado em
  2019 — ambos de Caulfield.

## Próximo passo

Tecer estas citações de volta no `recipe/knowledge-architecture.md`: cada
seção do L0 ganha uma linha **"Fundamentação"** apontando a(s) fonte(s)
primária(s) — tornando o próprio núcleo rastreável (dogfood da §3). Depois,
seguir para as Partes II (L1) e III (L2).
