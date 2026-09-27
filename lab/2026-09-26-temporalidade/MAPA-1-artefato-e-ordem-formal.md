---
title: 'Mapa 1: tempo como artefato e ordem formal'
created: 2026-09-26
updated: 2026-09-27
status: 'Varredura v1 por agente; fontes abertas nesta data.'
tags: [temporalidade, relogio, lamport, ordem-parcial, allen, strips, calculo-de-eventos, causalidade]
---

# Mapa 1: tempo como artefato e ordem formal

Do mais básico (relógio = contador de processo periódico) à ordem **sem** timestamp.

"sim" = fonte aberta (página oficial, PDF, abstract da editora). "parcial" = só metadados ou
trecho. "não verificado" = citado via fonte secundária aberta.

## 1. Medição: o relógio

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| NIST, *Walk Through Time: Early Clocks* | 2004 | Relógio = processo regular repetitivo + meio de contar; obelisco, clepsidra, Su Sung (1088) | https://www.nist.gov/pml/time-and-frequency-division/popular-links/walk-through-time/walk-through-time-early-clocks | sim |
| NIST, *A Revolution in Timekeeping* | 2004 | Escape verge-and-foliot (séc. XIV), pêndulo de Huygens (1656), Harrison (1761), quartzo | https://www.nist.gov/pml/time-and-frequency-division/popular-links/walk-through-time/walk-through-time-revolution | sim |
| NIST, *The "Atomic Age"* | 2004 | Relógio de amônia (1949), césio no NPL (1955), segundo atômico (1967) | https://www.nist.gov/pml/time-and-frequency-division/popular-links/walk-through-time/walk-through-time-atomic-age-time | sim |
| BIPM, *SI base unit: second* | 2018 | Segundo fixado por ΔνCs = 9 192 631 770 Hz | https://www.bipm.org/en/si-base-units/second | sim |
| BIPM, *Time metrology* | vigente | UTC = TAI + segundos intercalares; UTC(k) nos institutos | https://www.bipm.org/en/time-metrology | sim |
| IERS, *The Leap Second* | vigente | \|UT1−UTC\| < 0,9 s; 27 intercalares, último em 2017 | https://hpiers.obspm.fr/eop-pc/earthor/utc/leapsecond.html | sim |
| CGPM 2022, Resolução 4 | 2022 | Aumentar a tolerância UT1−UTC até 2035 (intercalares causam falhas) | https://www.bipm.org/en/cgpm-2022/resolution-4 | sim (desfecho da 28ª CGPM não) |

**Síntese.** Relógio é processo periódico + contador; a história é trocar o processo por um mais
estável. UTC é escala negociada, com descontinuidades. **Timestamp é leitura de instrumento com
convenção e incerteza, não dado primitivo.**

## 2. Ordem sem relógio em computação distribuída

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Lamport, "Time, Clocks, and the Ordering of Events", CACM 21(7) | 1978 | *Happened-before* sem relógio físico: mesmo processo; envio antes de recebimento; transitividade. **Ordem parcial**; concorrência = nenhum afeta o outro. Relógio lógico = contador. Ordem total exige desempate arbitrário. Anomalia quando a precedência vem por canal externo | https://lamport.azurewebsites.net/pubs/time-clocks.pdf | sim (PDF) |
| Fidge, ACSC 1988 | 1988 | Timestamps vetoriais preservam a ordem parcial | https://www.semanticscholar.org/paper/e706b8ae2952740cb95c0182c4c44b0d11cc54c1 | parcial |
| Mattern, "Virtual Time and Global States" | 1989 | Vetores representam a causalidade isomorficamente; o escalar de Lamport perde informação | https://www.vs.inf.ethz.ch/publ/papers/VirtTimeGlobStates.pdf | sim (PDF) |
| Ahamad et al., "Causal memory", Distributed Computing 9(1) | 1995 | Concordar só sobre a ordem do que é causalmente relacionado | https://link.springer.com/article/10.1007/BF01784241 | parcial |
| Kulkarni et al., "Logical Physical Clocks" (HLC), OPODIS 2014 | 2014 | Causalidade + proximidade do NTP; tolera as falhas do NTP | https://cse.buffalo.edu/tech-reports/2014-04.pdf | sim |
| Corbett et al., Spanner, OSDI '12 | 2012 | TrueTime expõe a incerteza do relógio como intervalo | https://www.usenix.org/conference/osdi12/technical-sessions/presentation/corbett | sim |
| RFC 5905, NTPv4 | 2010 | Offset, delay, jitter, dispersão; erro cresce com a tolerância de frequência | https://www.rfc-editor.org/rfc/rfc5905 | sim |

**Síntese.** Desde Lamport, a ordem vem do **fluxo de informação, não da passagem do tempo**.
Relógio físico deriva; ordenar por timestamp pode inverter causa e efeito. Vetores distinguem
"antes" de "sem relação".

## 3. Representação temporal formal

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| SEP, "Temporal Logic" (rev. 2024) | 1999/2024 | Prior (P, F, H, G); LTL (Pnueli 1977); CTL/CTL*; Halpern & Shoham sobre Allen | https://plato.stanford.edu/entries/logic-temporal/ | sim |
| Prior, *Time and Modality* / *Past, Present and Future* | 1957/67 | Lógica de tempos verbais | — | não verificado |
| Reichenbach, "The Tenses of Verbs" | 1947 | Fala (S), referência (R), evento (E); mais-que-perfeito E < R < S | https://perso.atilf.fr/apotheloz/wp-content/uploads/sites/59/2016/11/Reichenbach3.pdf | sim (PDF) |
| Derczynski & Gaizauskas, IWCS 2013 | 2013 | Tempo verbal restringe as relações entre eventos; ordenar é o mais difícil | https://aclanthology.org/W13-0107.pdf | sim |
| Allen, IJCAI-81 | 1981 | Rede de intervalos com fecho transitivo (i during j, j before k ⇒ i before k) | https://www.ijcai.org/Proceedings/81-1/Papers/045.pdf | sim (PDF) |
| Allen, CACM 26(11) | 1983 | 13 relações, tabela de transitividade | https://dl.acm.org/doi/10.1145/182.358434 | parcial |
| Vilain & Kautz, AAAI-86 | 1986 | Intervalos intratáveis; pontos tratáveis | https://aaai.org/papers/00377-aaai86-063-constraint-propagation-algorithms-for-temporal-reasoning/ | sim |
| Dechter, Meiri, Pearl, AIJ 49 | 1991 | Redes de restrições temporais; STP polinomial | https://cris.technion.ac.il/en/publications/temporal-constraint-networks/ | sim |
| McCarthy & Hayes | 1969 | Cálculo de situações; **problema do quadro** (o que *não* muda) | http://www-formal.stanford.edu/jmc/mcchay69.pdf | sim (PDF) |
| Shanahan, SEP "The Frame Problem" | 2016 | Inércia do senso comum; tiro de Yale; resolvido para IA lógica | https://plato.stanford.edu/entries/frame-problem/ | sim |
| Kowalski & Sergot, "A Logic-based Calculus of Events" | 1986 | Evento mais primitivo que o tempo; **descrições assimiladas em qualquer ordem**; revisão não monotônica | https://www.doc.ic.ac.uk/~rak/papers/event%20calculus.pdf | sim (PDF) |
| Fikes & Nilsson, STRIPS, AIJ 2 | 1971 | Operador = **precondição** + listas de adição e remoção | https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf | sim (PDF) |
| Sacerdoti, "The Nonlinear Nature of Plans", IJCAI-75 | 1975 | Plano = ordem parcial; linearidade é da execução | https://mlanthology.org/ijcai/1975/sacerdoti1975ijcai-nonlinear/ | sim |
| Weld, "Least Commitment Planning", AI Magazine 15(4) | 1994 | Links causais produtor → precondição; ordem só onde necessária | https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1109 | sim |
| Pnueli, FOCS 1977 | 1977 | Lógica temporal para verificar programas | https://alastairreid.github.io/RelatedWork/papers/pnueli:sfcs:1977/ | parcial |
| Clarke & Emerson, LNCS 131 | 1981/82 | CTL e model checking | https://nicolas.markey.fr/cnrs/PDF/Papers/lop1981-CE.pdf | parcial |
| Pustejovsky et al., TimeML, AAAI Spring 2003 | 2003 | Ancorar e **ordenar eventos entre si** (TLINK) | https://aaai.org/papers/0005-ss03-07-005-timeml-robust-specification-of-event-and-temporal-expressions-in-text/ | sim |
| TimeBank 1.2 (LDC2006T08) | 2006 | 183 notícias anotadas em TimeML | https://catalog.ldc.upenn.edu/LDC2006T08 | sim |
| Fatemi et al., Test of Time, arXiv:2406.09170 | 2024 | Fatos embaralhados pioram LLMs; sugerem ordenar pelo fluxo temporal | https://arxiv.org/html/2406.09170 | sim |

**Síntese.** Duas famílias. **Relacional** (Reichenbach, Allen, pontos, TimeML): relações sem data,
propagadas por transitividade. **Ação/estado** (situações, STRIPS, eventos, planejamento de ordem
parcial): **a ordem decorre de precondições e efeitos**. O cálculo de eventos formaliza "fatos
chegam fora de ordem".

## 4. Causalidade e ordem

| referência | ano | ideia central | URL | verificado? |
|---|---|---|---|---|
| Hitchcock & Rédei, SEP "Common Cause Principle" | 2020 | Garfo conjuntivo; assimetria como base da direção do tempo | https://plato.stanford.edu/entries/physics-Rpcc/ | sim |
| Reichenbach, *The Direction of Time* | 1956 | Teoria causal da direção do tempo | — | não verificado |
| Pearl, "Causal diagrams", Biometrika 82(4) | 1995 | Grafo causal explícito e consultável | https://ics.uci.edu/~dechter/courses/ics-295cr/spring-2021/reading/biometrika_1995.pdf | sim (p. 1–3) |
| Granger, Econometrica 37(3) | 1969 | Causalidade por precedência e previsão; "instantânea" vem de registro atrasado | https://www.econometricsociety.org/publications/econometrica/1969/08/01/investigating-causal-relations-econometric-models-and-cross | sim (abstract) |

**Síntese.** Em Lamport e Reichenbach, **a causalidade define a ordem**. Em Granger, a ordem infere
a causa, e herda os erros do timestamp. Grafo acíclico admite ordenações topológicas (inferência
nossa, não lida em Pearl).

## Exemplo do paraquedas, em STRIPS

| ação | precondição | adiciona | remove |
|---|---|---|---|
| embarcar | no_chão, tem_bilhete | a_bordo | no_chão |
| voar | a_bordo | em_voo, altitude | — |
| saltar | em_voo, altitude, paraquedas_vestido | em_queda | a_bordo |
| abrir_paraquedas | em_queda | paraquedas_aberto | — |

Os links causais forçam embarcar → voar → saltar → abrir, com timestamps embaralhados ou ausentes.
É o *happened-before* de Lamport com "mensagem" trocada por "efeito que satisfaz precondição".
Limites: exige produtor único e estados explícitos; "vestir paraquedas" fica **concorrente** ao
voo. Se um timestamp contradiz a cadeia ("abriu" antes de "saltou"), **o timestamp está errado**.

## O que isso oferece para um método

1. Separar **medição** (relógio), **ordem** (relação) e **datação** (rótulo). Timestamp tem incerteza.
2. **Ordem parcial como default honesto**; totalizar só com desempate declarado; sem dependência =
   concorrente, não chute.
3. **Derivar a ordem de dependências** (precondição/efeito, link causal, happened-before).
4. Representar relações qualitativas e propagar por transitividade.
5. Assimilar fatos em qualquer ordem, com persistência por default e revisão quando chega fato novo.
6. No texto, separar fala, referência e evento (Reichenbach).
7. **Conflito timestamp × dependência: a dependência vence**; o conflito é sinal de erro de registro.
8. Hipótese testável: "reordene por dependência antes de responder" ajuda (Test of Time sugere).
9. Correlação datada (Granger) não é dependência lógica; para ordenar, a dependência declarada é
   mais robusta.

**Lacunas deste mapa:** Prior e Reichenbach 1956 só via SEP; Allen 1983, Fidge, Ahamad, Pnueli e
Clarke & Emerson parciais; desfecho da 28ª CGPM não verificado; evidência de LLM de um estudo só.
