---
title: 'Mapa 6: estruturas matemáticas e formais do tempo e da ordem'
created: 2026-09-27
updated: 2026-09-27
status: 'Varredura v1 por agente (2026-09-27). Fishburn 1985 não verificado; Fishburn 1970, Thomason, Yosida, NPW 1981 e Russell 1936 só via metadados ou secundária.'
tags: [temporalidade, teoria-da-ordem, extensoes-lineares, ordens-de-intervalo, tempo-ramificado, sistemas-de-transicao, bitemporal, estruturas-de-eventos]
---

# Mapa 6: estruturas matemáticas e formais do tempo e da ordem

"sim (texto)" = texto lido. "sim (resumo)" = resumo. "parcial" = metadados ou secundária.
"(glosa nossa)" = conhecimento do agente, não da fonte.

## 1. Teoria da ordem: quanta ambiguidade resta

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Szpilrajn, *Fund. Math.* 16 | 1930 | Toda ordem parcial se estende a uma ordem total | https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/16/0/92870/sur-l-extension-de-l-ordre-partiel | sim (texto) |
| Dilworth, *Ann. Math.* 51 | 1950 | Largura (maior anticadeia) = mínimo de cadeias | https://mathweb.ucsd.edu/~asuk/dilworth.pdf | sim (texto) |
| Kahn, CACM 5(11) | 1962 | Ordenação topológica de redes grandes | https://doi.org/10.1145/368996.369025 | sim (resumo) |
| Brightwell & Winkler, *Order* 8 | 1991 | **Contar extensões lineares é #P-completo**; estimar é viável | https://link.springer.com/article/10.1007/BF00383444 | sim (resumo) |
| Talvitie & Koivisto, *JAIR* 81 | 2024 | Contagem aproximada prática para centenas de elementos | https://www.jair.org/index.php/jair/article/view/16374 | sim (resumo) |
| Li et al., BPOP, arXiv:2602.02806 | 2026 | Infere a **ordem parcial latente** de traços lineares de agentes de IA | https://arxiv.org/abs/2602.02806 | sim (resumo; sem revisão por pares) |

**Síntese.** Toda ordem parcial tem linearização (Szpilrajn); Kahn dá uma e detecta ciclos. Dilworth
mede a concorrência. Quantas linearizações existem (a ambiguidade) é #P-completo, mas estimável.

## 2. Instantes a partir de eventos

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Wiener, *Proc. Camb. Phil. Soc.* 17 | 1914 | "Precede totalmente"; instantes construídos de eventos que se sobrepõem | https://archive.org/details/proceedingsofcam1718191316camb | sim (texto) |
| Russell, *Our Knowledge of the External World*, IV | 1914 | Instante = grupo maximal de eventos mutuamente simultâneos; "só podemos apontar para um evento" | https://www.gutenberg.org/ebooks/37090 | sim (texto) |
| Whitehead, *The Concept of Nature*, III–IV | 1920 | Abstração extensiva; "o tempo serial é resultado de abstração intelectual" | https://www.gutenberg.org/files/18835/18835-h/18835-h.htm | sim (texto) |
| Russell, "On order in time", *Proc. Camb. Phil. Soc.* 32 | 1936 | "A existência de instantes requer hipóteses que não há razão para supor verdadeiras" | https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/on-order-in-time/25EED467B6B60A88575A10286C8FD877 | parcial |
| Anderson, "Russell on Order in Time" | ~1989 | Formaliza sobreposição S e precedência P de Russell | https://conservancy.umn.edu/server/api/core/bitstreams/832f7981-c0de-4fa2-9db7-e302c957e008/content | sim (texto) |
| Linsky, SEP "Logical Constructions" | ref. | Postulados de Russell para instantes em série | https://plato.stanford.edu/entries/logical-construction/ | sim (texto) |
| Fishburn, *J. Math. Psych.* 7 | 1970 | Ordem de intervalos ⟺ sem 2+2 induzido | https://doi.org/10.1016/0022-2496(70)90062-3 | parcial |
| Boyadzhiyska & Isaak, arXiv:1707.08093 | 2017 | Enuncia Fishburn, "antecipado por Wiener em 1914" | https://arxiv.org/abs/1707.08093 | sim (texto) |
| Fishburn, *Interval Orders and Interval Graphs* | 1985 | Monografia | — | não verificado |
| Kamp, "Events, Instants and Temporal Reference" | 1979 | Eventos × instantes na semântica | https://link.springer.com/chapter/10.1007/978-3-642-67458-7_24 | parcial |
| van Benthem, *The Logic of Time* | 1983/91 | Pontos, períodos e eventos | https://link.springer.com/book/10.1007/978-94-015-7947-6 | parcial |
| Allen, CACM 26(11) | 1983 | Intervalos primitivos, 13 relações; critica o tempo "grosseiro" do espaço de estados | https://cse.unl.edu/~choueiry/Documents/Allen-CACM1983.pdf | sim (texto) |

**Síntese.** Wiener, Russell e Whitehead invertem a ontologia: **eventos primitivos, instante
construído**. A estrutura que sai é a ordem de intervalos (sem 2+2). O próprio Russell duvida dos
instantes: dá para operar só com eventos e intervalos.

## 3. Linear × ramificado, denso × discreto

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Goranko & Rumberg, SEP "Temporal Logic" (rev. 2024) | ref. | Árvore com "passado fixo, futuro aberto"; discreto × denso; Prior; LTL | https://plato.stanford.edu/entries/logic-temporal/ | sim (texto) |
| Copeland, SEP "Arthur Prior" | 2020 | Carta de Kripke (1958): tempo ramificado | https://plato.stanford.edu/entries/prior/ | sim (texto) |
| Thomason, *Theoria* 36 | 1970 | Supervaluação: futuro verdadeiro se verdadeiro em todas as continuações; lacunas de verdade | https://doi.org/10.1111/j.1755-2567.1970.tb00427.x | parcial |
| Belnap, "Branching Space-Time", *Synthese* 92 | 1992 | Ordem causal entre eventos possíveis; histórias e pontos de escolha | https://link.springer.com/article/10.1007/BF00414289 | sim (texto) |

**Síntese.** Escolher o frame é decisão ontológica. Belnap troca "momentos" globais por ordem causal
entre eventos locais com pontos de escolha. Supervaluação dá o "ainda indeterminado".

## 4. Sistemas dinâmicos, estado e transição

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Kolmogoroff, *Math. Ann.* 104 | 1931 | Processo determinado × estocasticamente definido (Markov contínuo) | https://archive.org/details/kolmogoroff-1931-analytische-methoden-der-wahrscheinlichkeitsrechnung | sim (texto) |
| Yosida, *J. Math. Soc. Japan* 1 | 1948 | Semigrupos de um parâmetro (glosa: tempo irreversível) | https://doi.org/10.2969/jmsj/00110015 | parcial |
| Misra, Prigogine & Courbage, *PNAS* 76 | 1979 | Grupos unitários → semigrupos de Markov; irreversibilidade | https://pmc.ncbi.nlm.nih.gov/articles/PMC383881/ | sim (resumo) |
| Willems, *IEEE CSM* 27(6) | 2007 | **Estado = o que torna futuro e passado independentes** | https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Articles/JournalArticles/2007.1.pdf | sim (texto) |
| Plotkin, "Structural Operational Semantics" | 1981/2004 | Sistema de transição rotulado γ –a→ γ′ | https://homepages.inf.ed.ac.uk/gdp/publications/sos_jlap.pdf | sim (texto) |
| Keller, CACM | 1976 | Estados e transições para programas paralelos | https://doi.org/10.1145/360248.360251 | sim (resumo) |
| Clarke, Emerson & Sistla, TOPLAS | 1986 | Model checking sobre estruturas de Kripke | https://doi.org/10.1145/5397.5399 | sim (resumo) |

**Síntese.** "Estado → evento → estado" é o sistema de transição rotulado. **Irreversibilidade =
semigrupo, sem inversa.** Critério de Willems para "estado". Allen avisa que só estados é pobre para
duração e sobreposição.

## 5. Bitemporal

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Snodgrass & Ahn, SIGMOD '85 | 1985 | Transaction, valid e user-defined time; rollback × histórico | https://www2.cs.arizona.edu/~rts/pubs/SIGMOD85.pdf | sim (texto) |
| Snodgrass, *SIGMOD Record* 19(4) | 1990 | Transaction e valid são **ortogonais** | https://www2.cs.arizona.edu/~rts/pubs/SIGMODRecordDec90.pdf | sim (texto) |
| Jensen et al., glossário, *SIGMOD Record* 21(3) | 1992 | Valid = verdade na realidade; transaction = armazenamento, **imutável**; *chronon* | https://sigmodrecord.org/publications/sigmodRecord/9209/pdfs/140979.140996.pdf | sim (texto) |
| Jensen, Dyreson et al., glossário de consenso | 1994/98 | Consolidação | https://doi.org/10.1145/181550.181560 | sim (resumo) |
| Snodgrass (ed.), *TSQL2* | 1995 | Extensão temporal do SQL-92 | https://www2.cs.arizona.edu/~rts/tsql2.html | parcial |
| Kulkarni & Michels, *SIGMOD Record* 41(3) | 2012 | SQL:2011: SYSTEM_TIME × application-time; bitemporal | https://sigmodrecord.org/publications/sigmodRecord/1209/pdfs/07.industry.kulkarni.pdf | sim (texto) |

**Síntese.** Tempo do mundo ⊥ tempo do registro. O registro é só-acréscimo e imutável; o do mundo se
corrige retroativamente sem apagar. Já é padrão no SQL:2011.

## 6. Ordem parcial na concorrência

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Petri, *Kommunikation mit Automaten* | 1962 | Origem das redes de Petri | https://edoc.sub.uni-hamburg.de/informatik/volltexte/2011/160/ | sim (resumo) |
| Mazurkiewicz, DAIMI PB-78 | 1977 | Ações **independentes** comutam; traço = ordem parcial de ocorrências; ação = recursos + transformação | https://tidsskrift.dk/daimipb/article/view/7691 | sim (texto) |
| Lamport, CACM 21(7) | 1978 | Happened-before; relógio escalar desempata arbitrariamente | https://lamport.azurewebsites.net/pubs/time-clocks.pdf | sim (texto) |
| Nielsen, Plotkin & Winskel, TCS 13 | 1981 | Redes causais → domínios de configurações | https://doi.org/10.1016/0304-3975(81)90112-2 | parcial |
| Pratt, *IJPP* 15 | 1986 | Pomsets: processos como conjuntos de ordens parciais | https://link.springer.com/article/10.1007/BF01379149 | sim (resumo) |
| Winskel, "Event structures" | 1987/89 | Eventos + **causalidade** + **conflito**; habilitação | https://link.springer.com/chapter/10.1007/3-540-17906-2_31 | sim (resumo) |
| Mattern, "Virtual Time and Global States" | 1989 | Vetores representam a causalidade isomorficamente | https://www.vs.inf.ethz.ch/publ/papers/VirtTimeGlobStates.pdf | sim (texto) |

**Síntese.** Mazurkiewicz: independência = recursos disjuntos; comutar independentes vira ordem
parcial. Estruturas de eventos acrescentam **conflito**; estado = **configuração** (conjunto de
eventos fechado para baixo, sem conflito). Relógio escalar inventa ordem entre concorrentes.

## Lições para a ontologia

1. **Espinha dorsal: estrutura de eventos** (≤ causalidade, # conflito). Estado = configuração;
   transição derivada. Causalidade vinda de leitura/escrita de estado (Mazurkiewicz).
2. **Instantes derivados**; relações de Allen; teste de Fishburn: um 2+2 na ordem inferida sinaliza
   inconsistência ou mais de uma linha do tempo.
3. **Medir a ambiguidade**: log₂ e(P) (extensões lineares), normalizado por log₂ n!; largura de
   Dilworth; P(x antes de y) por amostragem.
4. **Bitemporal em toda asserção**; correção = linha nova; granularidade (*chronon*) declarada.
5. **Linearização não é fato**: ordem entre concorrentes é arbitrária.
6. **Futuro ramificado**; "indeterminado" como valor legítimo (supervaluação).
7. **Estado pelo critério de Willems; semigrupo por padrão**: desfazer é evento novo.
8. **Ordem de adoção:** estrutura de eventos → bitemporal → Allen → métricas de ambiguidade →
   instantes sob demanda → supervaluação.
