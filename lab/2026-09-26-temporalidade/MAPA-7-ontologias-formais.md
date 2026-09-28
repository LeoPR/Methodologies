---
title: 'Mapa 7: ontologias formais e semântica de tempo, eventos, estados e processos'
created: 2026-09-27
updated: 2026-09-27
status: 'Varredura v1 por agente (2026-09-27). Moens & Steedman lido na íntegra; Hayes, Dowty, Comrie, Allen 1983, Galton 1990, Davidson original e ISO 21838-2 não.'
tags: [temporalidade, ontologia, owl-time, prov-o, bfo, dolce, vendler, moens-steedman, galton, verbnet, framenet]
---

# Mapa 7: ontologias formais e semântica do tempo

"sim (texto)" = texto lido pelo agente. "sim (resumo do texto)" = texto aberto, resumo do extrator.
"sim (resumo)" = só o abstract. "parcial" = metadados ou secundária. O extrator da web inventou
conteúdo com PDF binário em três casos; foram relidos localmente e o que não confirmou saiu.

## 1. Padrões e grafos de conhecimento

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| W3C, *Time Ontology in OWL* (CR Draft 2022) | 2017/22 | Instant, Interval, Duration, sistemas de referência; 13 relações de Allen. **Não modela evento nem estado** | https://www.w3.org/TR/owl-time/ | sim (resumo do texto) |
| W3C, *PROV-O* | 2013 | Entity, Activity, Agent; generatedAtTime, invalidatedAtTime | https://www.w3.org/TR/prov-o/ | sim (resumo do texto) |
| W3C, *PROV-DM* | 2013 | Mudança = sucessão de entidades de aspecto fixo | https://www.w3.org/TR/prov-dm/ | sim (resumo do texto) |
| W3C, *PROV-Constraints* | 2013 | `precedes` é pré-ordem de eventos; **"there is no inference that time ordering implies event ordering, or vice versa"** | https://www.w3.org/TR/prov-constraints/ | sim (resumo do texto) |
| ISO/IEC 21838-2:2021 (BFO) | 2021 | BFO como ontologia de topo | https://www.iso.org/standard/74572.html | parcial |
| BFO-2020 `bfo-core.owl` | 2020 | Continuant × occurrent; process, process boundary, temporal region, history; **sem "estado"** | https://github.com/BFO-ontology/BFO-2020 | sim |
| Masolo et al., WonderWeb D18 (DOLCE) | 2003 | Endurants × perdurants; perdurants por cumulatividade: state, process, achievement, accomplishment ("contains its result as a boundary") | http://www.loa.istc.cnr.it/old/Papers/D18.pdf | sim (texto) |
| Borgo et al., *Applied Ontology* 17(1) | 2022 | DOLCE revisto; participação indexada no tempo | https://arxiv.org/pdf/2308.01597 | sim (texto) |
| schema.org `Event` | vivo | Datas, status, subEvent; sem estado, precondição ou resultado | https://schema.org/Event | sim (resumo do texto) |
| Wikidata, *Help:Qualifiers* | vivo | point in time, start time, end time **restringem a validade** | https://www.wikidata.org/wiki/Help:Qualifiers | sim (resumo do texto) |
| Wikidata, *Help:Dates* | vivo | Precisão 0–11; earliest/latest date; circa | https://www.wikidata.org/wiki/Help:Dates | sim (resumo do texto) |
| ISO 24617-1:2012 (ISO-TimeML) | 2012 | EVENT, TIMEX3, TLINK; "nothing happens in infinitesimally small time" | https://cdn.standards.iteh.ai/samples/37331/9c2169b177f3499aba2e72f2e6aaed68/ISO-24617-1-2012.pdf | parcial |

**Síntese.** OWL-Time cuida do eixo, agnóstico ao conteúdo. PROV cuida do registro e diz que **a
ordem dos eventos não se infere dos timestamps**. DOLCE tem a taxonomia mais próxima de Vendler; BFO
não tem "estado". Wikidata e schema.org só anotam validade.

## 2. Metafísica

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Hawley, SEP "Temporal Parts" | 2004/20 | Perdurantismo × endurantismo × estágios | https://plato.stanford.edu/entries/temporal-parts/ | sim (resumo do texto) |
| Seibt, SEP "Process Philosophy" | 2012/22 | Processo (em curso) × evento (completo); parthood não transitiva | https://plato.stanford.edu/entries/process-philosophy/ | sim (resumo do texto) |
| Desmet & Irvine, SEP "Whitehead" | 1996/2022 | Actual occasions; "how an actual entity becomes constitutes what it is" | https://plato.stanford.edu/entries/whitehead/ | sim (resumo do texto) |
| Rescher, *Process Metaphysics* | 1996 | Processo não whiteheadiano | https://sunypress.edu/Books/P/Process-Metaphysics | parcial |
| Casati & Varzi, SEP "Events" | 2002/25 | Objetos existem, eventos ocorrem; critérios de identidade | https://plato.stanford.edu/entries/events/ | sim (resumo do texto) |
| Galton & Mizoguchi, *Applied Ontology* 4(2) | 2009 | Objeto e processo mutuamente dependentes; **processos mudam, eventos não** | https://empslocal.ex.ac.uk/people/staff/apgalton/Preprints/AO-Waterfall-preprint.pdf | sim (texto) |

**Síntese.** 3D/4D não é neutro. **Processo em curso ≠ evento registrado**: um salto em curso e "o
salto" são categorias diferentes.

## 3. Semântica de eventos e aspecto

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Davidson, "Logical form of action sentences" | 1967 | Argumento de evento; advérbios como predicados do evento | https://user.phil-fak.uni-duesseldorf.de/~filip/Davidson.67.pdf | parcial |
| Parsons, *Events in the Semantics of English* | 1990 | Neo-davidsoniano; Cul (culminar) × Hold | https://verbs.colorado.edu/~mpalmer/Ling7800/Parsons.pdf | parcial |
| Vendler, "Verbs and Times", *Phil Rev* 66 | 1957 | Estados, atividades, accomplishments, achievements | https://semantics.uchicago.edu/scalarchange/vendler57.pdf | parcial (p. 149) |
| Comrie, *Aspect* | 1976 | Perfectivo (todo) × imperfectivo (estrutura interna) | https://archive.org/details/aspectintroducti0000comr_v0y4 | parcial |
| Dowty, *Word Meaning and Montague Grammar* | 1979 | Accomplishment = atividade + estado resultante; paradoxo imperfectivo | https://link.springer.com/book/10.1007/978-94-009-9473-7 | parcial |
| Hamm & Bott, SEP "Tense and Aspect" | 2014/24 | "Estava construindo" ⇏ "construiu" | https://plato.stanford.edu/entries/tense-aspect/ | sim (resumo do texto) |
| **Moens & Steedman, *Comp. Ling.* 14(2)** | 1988 | Ver abaixo | https://aclanthology.org/J88-2003.pdf | **sim (texto completo)** |
| Steedman, *The Productions of Time* (rascunho) | 2005 | Não é sobre tempo, é sobre **dependência causal e teleológica**; STRIPS; frame, qualification, ramification | https://homepages.inf.ed.ac.uk/steedman/papers/temporality/temporality2.pdf | sim (texto) |
| Galton, *J Logic Comput* 18(3) | 2008 | EXP (processos, dinâmico) × HIST (eventos, estático) | https://academic.oup.com/logcom/article-abstract/18/3/323/1746650 | sim (resumo) |
| Galton, FOIS 2012 | 2012 | initiate, terminate, perpetuate, allow, prevent; **estados não causam, permitem** | https://empslocal.ex.ac.uk/people/staff/apgalton/Preprints/fois2012-galton-final.pdf | sim (texto) |

**Moens & Steedman 1988 (lido na íntegra).** É a peça mais próxima do paraquedas.
- Ontologia "based on such notions as causation and consequence, rather than on purely temporal
  primitives".
- **Núcleo:** processo preparatório → culminação → estado consequente.
- Cinco tipos: culminação, ponto, processo culminado, processo, estado.
- Coerção: o progressivo tira a culminação; o perfeito devolve o estado consequente.
- Estado consequente é **seletivo** (só o relevante no discurso).
- "When" exige elo de contingência, não só tempo. **Contingência é intransitiva.**
- Literal: "only events that are contingently related necessarily have well-defined temporal
  relations in memory." A ordem parcial sai "quite incidentally".

**Síntese.** Davidson/Parsons dão o evento reificado com papéis. Vendler/Comrie/Dowty: a classe
aspectual decide que inferências valem. Moens & Steedman, Steedman e Galton convergem: **ordenar
cenas é raciocinar sobre contingência; a linha do tempo é subproduto.**

## 4. Mudança e persistência em representação do conhecimento

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Hayes, "Naive Physics" I e II | 1979/85 | Clusters, entre eles **histories** | https://www.semanticscholar.org/paper/Naive-physics-I:-ontology-for-liquids-Hayes/26ad0567cacd071a3ae71a34e014ffc8104eb64c | parcial |
| Davis, *AI Magazine* 19(4) | 1998 | Balanço do programa de Hayes | https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1424/1323 | sim (texto) |
| McDermott, *Cognitive Science* 6 | 1982 | Fatos, eventos, planos, **histórias ramificadas** | https://doi.org/10.1207/s15516709cog0602_1 | sim (resumo) |
| Allen, CACM 26(11) | 1983 | 13 relações de intervalo | https://doi.org/10.1145/182.358434 | parcial |
| Allen, *AIJ* 23 | 1984 | HOLDS (propriedade), OCCUR (evento), OCCURRING (processo), por comportamento sob subintervalos | http://cs112.org/wp-content/uploads/2013/09/Allen.pdf | sim (texto) |
| Shoham, *AIJ* 33 | 1987 | Custo semântico de reificar TRUE(t1,t2,φ) | https://doi.org/10.1016/0004-3702(87)90052-x | sim (resumo) |
| Galton, *AIJ* 42 | 1990 | Allen falha em mudança contínua; instantes no mesmo nível dos intervalos | https://doi.org/10.1016/0004-3702(90)90053-3 | parcial |

**Síntese.** Distinções obrigatórias: holds × occurs × occurring; instantes para culminações; custo
da reificação; histórias ramificadas para planos. Frame, qualification e ramification são o risco
prático de toda modelagem por precondição e efeito.

## 5. Recursos lexicais e narrativos

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Ruppenhofer et al., *FrameNet II* | 2016 | Subframe e **Precedes**; todo Event tem pré-estado e pós-estado | https://akb89.github.io/myValencer/framenet_book.pdf | sim (texto) |
| Kipper et al., *LRE* 42 (VerbNet) | 2008 | Classificação de verbos ao estilo de Levin | https://link.springer.com/article/10.1007/s10579-007-9048-2 | parcial |
| Brown et al., LREC 2018 | 2018 | VerbNet com **subeventos ordenados** e1<e2<e3 | https://aclanthology.org/L18-1009/ | sim (texto) |
| Brown et al., *Frontiers in AI* 5 | 2022 | Oposição ¬dead(e1) → dead(e2); **precondições e pós-condições extraíveis**; aplicado a ProPara | https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.821697/full | sim (texto) |
| Chambers & Jurafsky, ACL-08 | 2008 | Cadeia narrativa = ordem parcial de eventos | https://aclanthology.org/P08-1090.pdf | parcial |
| Sap et al., ATOMIC | 2019 | xNeed, xEffect, xIntent: pré e pós-condição probabilística | https://arxiv.org/abs/1811.00146 | parcial |

**Síntese.** VerbNet-GL dá subeventos com oposição de estados por verbo: é a operacionalização
lexical do núcleo de Moens & Steedman. FrameNet dá o nível de script. ATOMIC dá conhecimento
probabilístico. **Nenhum está alinhado a OWL-Time, BFO ou DOLCE**: é o vão a preencher.

## O paraquedas como núcleo

| cena | núcleo | estado consequente | habilita |
|---|---|---|---|
| embarcar | culminação | a_bordo(p, avião) | voar, saltar |
| voar até a altitude | processo culminado | em_altitude(avião) | salto seguro |
| saltar | culminação | ¬a_bordo(p); começa caindo(p) (processo) | abrir |
| abrir | culminação | velame_aberto(c) | planar, pousar |

## Lições para a ontologia

**Primitivas candidatas:** estado (holds; permite, não causa); processo (occurring; em curso, muda);
evento (occurs; fixo) com subtipos culminação, ponto, processo culminado; **núcleo** (preparação →
culminação → consequente); fronteira/instante; participante indexado no tempo; região temporal e
relações de Allen (sobretudo *meets*); relações de contingência separadas de *before* (enables,
initiates, terminates, perpetuates, causes; contingência intransitiva; precondição/efeito com
oposição); script/episódio; **registro e proveniência** (tempo do mundo ≠ tempo do registro).

**Reusar:** OWL-Time (eixo e Allen); PROV-O e PROV-Constraints (registro; ordem sem timestamp); uma
ontologia de topo só (DOLCE para linguagem e cognição; BFO para interoperar com ciência).

**Estender:** núcleo; contingência intransitiva; precondição/efeito com oposição; allow, initiate,
terminate, perpetuate; coerção aspectual. Ancoragem lexical em VerbNet-GL e FrameNet; ATOMIC como
fonte probabilística, não axioma.

**Armadilhas:** linha do tempo ≠ ordem; não fechar a contingência por transitividade; aspecto é da
frase em contexto; paradoxo imperfectivo ("estava abrindo" ⇏ "abriu"; crítico para falhas);
instantes para culminações; consequente ≠ todas as consequências; granularidade muda a categoria;
evento não muda, processo muda; estados não causam; frame, qualification, ramification; ciclos e
não ocorrência no FrameNet; custo da reificação; status datado dos padrões.
