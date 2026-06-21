---
title: 'Fundamento epistêmico do juiz: escala mensurável, não binário perfeito/impossível'
created: 2026-06-21
updated: 2026-06-21
status: 'REGISTRO conceitual. Verificação adversarial completa (2026-06-21, dois runs): TODOS os eixos verificados. A/D/E/H: 3-0, 1 refutado informativo. B/C/F + instrumentos E/G (Condorcet, Aumann, Simon, Brier, Tetlock): 3-0 NUANCED em todos — verificados com ressalva de formulação/atribuição/escopo; nenhum refutado.'
nota: 'Responde à falácia "se não é perfeito, não serve". O alvo é distância mensurável ao melhor-possível-dado-o-input, não toque no absoluto.'
---

# Fundamento epistêmico do juiz: escala mensurável, não binário

> Por que "o juiz não é perfeito, logo não serve" é falácia, e qual é o alvo correto.
> Complementa o [DOSSIE-judge](DOSSIE-judge-justificativa-cientifica.md) §1-2 (ideal regulativo) e a
> leitura da [Fase B](RESULTADOS-juiz-sem-gabarito.md). Levantamento por harness de pesquisa
> (filosofia da ciência, lógica, computação, teoria da informação, estatística).

## A tese, em uma frase

Não existe juiz perfeito nem acesso a verdade absoluta.
O que existe é **convergência no melhor possível dentro do universo de informação mostrado**.
Avaliar um juiz não é perguntar "acertou a verdade?" (binário), e sim **medir, numa escala, quão perto
ele chega do melhor que qualquer agente competente alcançaria com a MESMA informação**.

## As duas distâncias que se medem (e não se confundem)

O experimento mental do "1+1=3" separa duas coisas que a falácia funde.

**Teto epistêmico por informação (irredutível).**
Se o universo dado a todos é "1+1=3", sem contexto nem verificação possível, convergir em "1+1=3" **é** a
melhor verdade disponível. Ninguém a falsifica dali. Isso não é defeito do juiz; é o limite que a informação
impõe. A literatura nomeia esse piso:
- **Incerteza aleatória vs epistêmica** (Hüllermeier & Waegeman, 2021): a aleatória é o ruído irredutível dado
  o que se sabe; a epistêmica é a parte que mais informação/capacidade reduz. [verificado 3-0]
- **Erro de Bayes** (Devroye, Györfi & Lugosi, 1996; Duda, Hart & Stork, 2001; resumo em arXiv:2506.03159):
  piso inferior de erro que **nenhum** classificador supera, fixado pela sobreposição das densidades de classe,
  isto é, uma propriedade dos **dados**, não da capacidade do agente. [verificado 3-0]
  *Ressalva verificada:* o erro de Bayes é difícil de **estimar** na prática (precisa de muitas amostras) e o
  piso é relativo a uma **representação de features fixa** — features melhores reduzem a sobreposição. Mas a
  tentativa de dizer que "o piso de Bayes só existe relativo a uma classe de modelos" foi **refutada (0-3)**:
  no limite de uma classe irrestrita com features fixas, o piso **permanece irredutível**; só o *rótulo*
  "irredutível" é relativo ao modelo, não a existência do piso.
- **Desigualdade de processamento de dados** (Shannon; Cover & Thomas, 2006): para a cadeia de Markov
  X→Y→Z, I(X;Y) ≥ I(X;Z) — nenhum pós-processamento, determinístico ou estocástico, cria informação sobre a
  fonte que não estava na entrada. O juiz não extrai o que o input não contém. [verificado 3-0]

**Deficiência de capacidade (redutível, em escala).**
Outra coisa é quando um par competente, **com a mesma informação**, julga melhor. Aí há deficiência real do
juiz, mas medida numa escala (quão perto do par ele chega), não num binário "serve/não serve".

**Complicação honesta (não ignorar).**
A divisão limpa entre os dois não é gratuita. A classificação de uma incerteza como aleatória ou epistêmica é
**relativa ao modelo e à informação considerados**, não uma propriedade absoluta do mundo (Der Kiureghian &
Ditlevsen, 2009; ICLR 2025 blogpost). O que parece irredutível a um modelo fraco pode ser reduzido por um mais
forte. E os métodos que tentam **separar** as duas são "fundamentalmente incompletos" (Jimenez, Jurgens &
Waegeman, ICML 2025, arXiv:2505.23506, verificado 3-0): o viés não-contabilizado **superestima a aleatória e
subestima a epistêmica**, ou seja, pode **rotular como teto irredutível o que é lacuna de capacidade redutível**.
Logo: a distinção é uma **lente útil**, não uma régua que se lê sem ruído — e o erro de atribuição cai sempre
para o lado de absolver o juiz. Por isso medimos o teto por um piso empírico (ruído entre avaliadores
competentes), não por estimadores de desemaranhamento.

## Por que evidência finita não fixa verdade única

**Subdeterminação (Quine-Duhem; SEP, "Underdetermination of Scientific Theory"). [verificado com ressalva]**
Evidência finita é compatível com mais de uma teoria. Nenhum conjunto de dados força uma leitura única.
Duhem (1906/1954) mostrou que nenhuma hipótese enfrenta o teste empírico em isolamento — apenas conjuntos de
hipóteses mais auxiliares são testáveis; quando uma previsão falha, a lógica não localiza o erro. Quine (1951,
1975) estendeu o holismo a todo o conhecimento: qualquer enunciado pode ser mantido verdadeiro diante de
qualquer experiência recalcitrante, com ajustes suficientes no restante da teia de crenças.
*Ressalva verificada:* a formulação forte — "múltiplas teorias incompatíveis existem sempre para qualquer
conjunto finito de dados" — excede o que Duhem e Quine provaram. Quine (1975, Erkenntnis 9:313-328) apresentou
a tese forte como conjectura condicional, não resultado estabelecido. A versão que as fontes sustentam é:
**é em princípio sempre possível construir uma teoria rival compatível com o mesmo conjunto finito de dados**,
embora Quine reconheça que critérios pragmáticos (simplicidade, coerência, fertilidade) restringem a escolha
mesmo quando a lógica subdetermina. A SEP distingue subdeterminação holista (o que Duhem e Quine argumentaram)
da subdeterminação contrastiva (a afirmação mais forte). A implicação normativa permanece intacta:
pedir ao juiz que "ache a verdade" a partir de input finito pede o que a própria ciência não tem.
O alvo viável é a melhor leitura **sustentável** pelo input, com a incerteza declarada.

## Verdade como convergência — e suas críticas [verificado com ressalva]

**Peirce (CP 5.407, 1878; Misak 2004): verdade = "a opinião fadada a ser, no fim, aceita por todos que
investigam".** Citação verbatim confirmada. Convergência é **esperança regulativa**, um norte teleológico, não
uma linha de chegada onde tudo se assenta. Peirce reformulou em 1908: "esperança regulativa", não "fadada" —
o movimento assintótico é deliberado. Misak (2004, Oxford Philosophical Monographs) defende leitura
neo-pragmatista: crença é verdadeira quando "resistiria à dúvida, se investigássemos até onde fruitivamente
podemos" — formulação condicional que evita o peso metafísico da versão forte.

Mas a teoria da convergência **tem críticos**, e é honesto carregá-los:
- Rorty: não existe "audiência ideal" — posição documentada em *Consequences of Pragmatism* (1982) e
  *Science as Solidarity* (1987); a analogia do "maior inteiro" é uma paráfrase da posição de Rorty, não
  uma citação verificada como sua.
- Quine: "mais perto da verdade" é mal definido entre teorias — confirmado pela subdeterminação (ver eixo B)
  e pelo deflacionismo quineano (convergir para um limite não faz sentido entre mudanças de paradigma).
- Russell: crítica documentada é **semântica** (*Philosophical Essays*, 1910): pragmatismo confunde
  *indicador* de verdade com o *significado* de "verdadeiro". A formulação "por que UM estado-final e não
  convergências plurais?" é atribuída a Russell com imprecisão — esse argumento é mais adequado a críticos
  pluralistas que ao Russell documentado.
- "Fatos perdidos" (Field 1982, *Journal of Philosophy* 79(10):553-567; Smart 1984): há verdades sobre as
  quais a investigação não pode, em princípio, convergir (ex.: número exato de dinossauros). [verificado]

*Ressalvas verificadas:* (a) A analogia do "maior inteiro" deve ser apresentada como paráfrase, não citação
direta de Rorty. (b) A objeção de Russell como documentada é semântica, não sobre singularidade da
convergência; a reformulação plural seria mais precisa se atribuída a críticos pluralistas em geral.

Tradução para o nosso caso: **convergência não prova correção**. Ela é direção e estimativa, não posse.
Por isso o corpus ancora o núcleo sólido no **gold mecânico**, não no consenso dos juízes.

## Há proposições que nenhum procedimento decide a partir do dado

**Limites formais.** Gödel (incompletude: há verdades não deriváveis dos axiomas dados), Turing/Church
(indecidibilidade, halting problem), Rice (propriedades semânticas não-triviais são indecidíveis), Tarski
(indefinibilidade da verdade: nenhuma linguagem rica o bastante representa a própria semântica). [verificado 3-0]
**Nuance verificada:** a incompletude é **relativa ao sistema**, não absoluta. A sentença de Gödel é improvável
em F, mas provável em F+Con(F), e é genuinamente **verdadeira** no modelo padrão. A verdade pode **ultrapassar**
um sistema fixo. Isto afina a tese: o teto é fixado pelo universo de axiomas/informação dado, não é um
"inconhecível" absoluto.

O ponto que **fundamenta a tese da escala** (Brčić & Yampolskiy, "Impossibility Results in AI: A Survey",
ACM Computing Surveys, 2023, doi:10.1145/3603371): as impossibilidades de IA se organizam em cinco famílias
(Dedução, Indução, Indistinguibilidade, Tradeoffs, Intratabilidade). A família da **Dedução** (Gödel/Turing/
Chaitin/Rice) nega garantia **100%**. Mas — e isto é o eixo do seu argumento — **garantias probabilísticas são
atingíveis**: "as impossibilidades são bem menos estritas sob inferência incerta; mas, quanto basta?".
[verificado 3-0]. A pergunta deixa de ser "possível ou impossível?" e passa a ser "**quanto basta?**".
Isto **é** a passagem do binário para a escala mensurável.

## Convergência de júri: a garantia depende de independência

**Teorema do Júri de Condorcet (Condorcet, 1785; SEP, "Jury Theorems", Dietrich & Spiekermann).** Votantes
com competência p > 0,5 e **independentes** convergem à resposta correta com mais votantes (P → 1 quando N
→ ∞). Duas condições, não uma. [verificado com ressalva]

**Sob dependência, a garantia degrada.**
- Ladha (1992, *American Journal of Political Science* 36(3):617-634): com correlação positiva de pares, a
  eficácia da regra de maioria diminui; a garantia de Condorcet se preserva apenas com correlação suficientemente
  baixa.
- Dietrich & List (2004, *Synthese* 142:175-202): sob causa comum (evidência compartilhada), o limite assintótico
  é travado **abaixo de 1** — a maioria não alcança quase-certeza de correção.
- Kaniovski (2010): em júris homogêneos com correlação extremamente positiva, o desempenho da maioria pode
  cair abaixo de qualquer limiar fixo em casos limite.
- Empírico em LLM (Kim, Garg, Peng & Garg, "Correlated Errors in LLMs", ICML 2025, arXiv:2506.07962; 350+
  modelos): pares concordam na **mesma resposta errada ~60% das vezes**, contra ~33% esperado se os erros fossem
  independentes. A correlação **cresce com a acurácia**, mesmo entre arquiteturas e fornecedores distintos. Juiz
  correlacionado **infla** o acerto medido. Efeito ligado à **monocultura algorítmica** (Kleinberg & Raghavan,
  PNAS, 2021). [verificado 3-0]
- Enquadramento explícito em painel LLM (arXiv:2605.29800, "Nine Judges, Two Effective Votes"): painel de
  9 juízes (7 famílias de modelos) tem neff ≈ 2,2 votos independentes efetivos; correlação média de pares de
  erro φ = 0,391; 51 itens onde todos os 9 falharam juntos vs. <1 esperado sob independência. Invoca
  explicitamente o Teorema de Condorcet. [sourced]
- Viés compartilhado de familiaridade/perplexidade: juízes super-recompensam texto de baixa perplexidade,
  um viés **não-aleatório e comum**, que fere a independência (arXiv:2410.21819). [sourced]
- **Teorema do Acordo de Aumann** (ver próxima alínea): agentes racionais com priores comuns convergem —
  convergência pode vir de **prior compartilhado**, não de acerto.

*Ressalvas verificadas:* (a) A linguagem "inversão para quase-certeza" exagera o que Ladha (1992) e Dietrich &
List (2004) provam como resultado principal: eles mostram degradação e teto assintótico abaixo de 1, não
maioria levada a quase-zero. A inversão forte é possível em casos limite (correlação extremamente positiva), mas
não é o teorema central dessas fontes. (b) arXiv:2307.04709 (Romaniega 2023) critica o Teorema da Diversidade
de Hong-Page, **não** o Teorema do Júri de Condorcet — essa citação foi removida desta seção.

Consequência direta para o Eixo 1 do DOSSIE: convergência cross-vendor é **proxy de independência parcial,
medida em escala** (ex.: votos efetivos independentes, neff), **não prova de correção**. É exatamente a nossa
Fase B: dois juízes seguem concordando nas respostas erradas sem o gabarito.

## Falibilismo: ciência é aproximação, não posse [verificado com ressalva]

**Popper** (*Conjecturas e Refutações*, 1963, cap. 10; *Objective Knowledge*, 1972, cap. 9; SEP "Karl Popper"):
falibilismo + **verossimilhança/truthlikeness** — teorias são mais ou menos próximas da verdade, numa
**escala**, sem nunca a possuírem. A definição formal (conteúdo-de-verdade vs. conteúdo-de-falsidade, via
Tarski) foi refutada por Miller e Tichý em 1974 (*British Journal for the Philosophy of Science* 25(2):155-177):
nenhuma teoria falsa pode ser mais próxima da verdade que outra, na definição original. Popper aceitou a
refutação. Successor theories (Oddie 2019, SEP "Truthlikeness"; Niiniluoto 1987, Reidel) rehabilitaram o
conceito por abordagens de similaridade entre mundos possíveis e métricas de distância sobre constituintes.
O ponto que sobra: o **conceito** de distância escalar à verdade é sólido; o problema era a formalização
específica, não a ideia. [verificado 3-0]

**Lakatos** (*The Methodology of Scientific Research Programmes*, 1978; cap. principal: "Falsification and the
Methodology of Scientific Research Programmes", 1970): um programa de pesquisa é progressivo se gera **excesso
de conteúdo empírico** — prevê fatos novos e não antecipados. É degenerante se as modificações teóricas só
acomodam anomalias conhecidas post-hoc, sem gerar novas previsões. Lakatos **retém a verdade como alvo**, mas
substitui aproximação da verdade por **fertilidade preditiva** como critério operacional.
*Ressalva verificada:* a formulação "recuo mensurável a partir do erro reconhecido" sobre-assimila Lakatos ao
quadro poppereano de verossimilhança que ele rejeitou; seu critério real é conteúdo empírico excedente,
não distância do erro. [verificado com ressalva]

**Kant** (*Crítica da Razão Pura*; Apêndice à Dialética Transcendental, **A642–668/B670–696**): as ideias da
razão (alma, mundo, Deus) funcionam apenas regulativamente, não constitutivamente — são diretivas para buscar
unidade sistemática no conhecimento, não afirmações de objetos transcendentes reais. A metáfora-chave é o
*focus imaginarius* (A644/B672): as linhas da razão parecem convergir para um ponto que não existe como objeto
real, mas em direção ao qual a investigação é orientada. A investigação científica se aproxima
assintoticamente de uma completude que nunca alcança.
*Nota:* A569/B597 (citado anteriormente) endereça o conceito formal de ideal (ens realissimum, sábio), não a
função regulativa na investigação empírica; o locus correto é A642–668/B670–696. O termo "assintoticamente"
é uma glosa interpretativa moderna, não terminologia kantiana, mas é a leitura padrão do *focus imaginarius*.
[verificado com ressalva]

*Síntese do eixo F:* os três autores apontam para a mesma estrutura — o sucesso científico é aproximação
mensurável sem posse da verdade absoluta — mas com critérios efetivos distintos que não devem ser fundidos:
Popper usa distância à verdade (escala), Kant usa orientação regulativa assintótica, Lakatos usa fertilidade
preditiva. A unificação como "distância mensurável do erro reconhecido" é filosoficamente defensável como
quadro do argumento, mas representa uma síntese do analista, não posição direta dos três autores.

## Medir julgamento numa escala contínua

A prática já sabe avaliar julgamento sem oráculo binário.

- **Racionalidade limitada / satisficing** (Simon 1955, QJE 69(1):99-118; Simon 1956, *Psychological Review*
  63(2):129-138; Nobel 1978, *AER* 69(4):493-512; SEP "Bounded Rationality"): o agente real opera sob limites
  cognitivos e computacionais; o padrão pertinente não é o ótimo inalcançável, mas o **suficientemente bom
  relativo a um nível de aspiração**. O nível de aspiração se ajusta dinamicamente — não há maximização nem
  mesmo relativa a um conjunto de restrições.
  *Ressalva verificada:* o termo "satisficing" é cunhado no paper de 1956 (não no de 1955); "melhor resultado
  atingível dadas as restrições" conflate satisficing com otimização restrita, que é exatamente o que Simon
  rejeitou. [verificado com ressalva]
- **Teorema do Acordo de Aumann** (Aumann 1976, *Annals of Statistics* 4(6):1236-1239; DOI 10.1214/aos/1176343654):
  agentes Bayesianos racionais com prior comum e conhecimento comum das posterioris não podem divergir — as
  posterioris devem ser iguais. Implicação analógica para juízes LLM: convergência de julgamentos é compatível
  com prior compartilhado (dados de treinamento sobrepostos), não necessariamente com acumulação de evidência
  independente.
  *Ressalva verificada:* o teorema prova impossibilidade de desacordo sob condições idealizadas de conhecimento
  comum; não prova que concordância implica prior compartilhado como causa. A implicação para LLMs é uma
  **analogia com fundamento empírico** (Kim et al. 2025; Balasubramanian et al., arXiv:2601.22336, 2026; Zhao et al.,
  arXiv:2603.00039, 2026), não corolário direto. A condição de conhecimento comum exigida é muito mais restritiva
  do que qualquer coisa que painéis LLM satisfazem. Lederman (2015, *Review of Symbolic Logic* 8(1):11-45) mostra
  que as sub-condições do prior comum podem ser relaxadas individualmente de modo a permitir desacordo.
  [verificado com ressalva]
- **Regras de pontuação próprias / Brier score** (Brier 1950, *Monthly Weather Review* 78(1):1-3, DOI
  10.1175/1520-0493(1950)078<0001:vofeit>2.0.co;2; McCarthy 1956, *PNAS* 42:654-655; Savage 1971, *JASA*
  66(336):783-801; Gneiting & Raftery 2007, *JASA* 102(477):359-378): pontuam a **probabilidade** declarada,
  premiando calibração, numa escala contínua — o agente só maximiza a pontuação esperada reportando a
  probabilidade verdadeira. Instantia o princípio: qualidade do juiz é dimensão mensurável (calibração +
  resolução), não veredicto binário.
  *Ressalvas verificadas:* o intervalo [0,2] aplica-se à formulação multicategoria original de Brier; a forma
  binária moderna dominante tem intervalo [0,1]. McCarthy (1956) tem prioridade formal para a prova de
  propriedade; Savage (1971) estendeu e popularizou. [verificado com ressalva]
- **Good Judgment Project** (Tetlock 2005, Princeton UP; Mellers et al. 2014, *Psychological Science*; Mellers
  et al. 2015, *Perspectives on Psychological Science* 10(3):267-281; Chang et al. 2016, *Judgment and Decision
  Making*; Tetlock & Gardner 2015, Crown): previsores são rankeados por acurácia probabilística (Brier score)
  ao longo do tempo — julgamento avaliado como **escala**, não como acerto único. Superprevisores (~2% superior)
  superaram analistas de IC com acesso a dados classificados em ~25-30% (por Brier score). Habilidade é
  **melhora­vel**: treinamento em raciocínio probabilístico gerou ganhos de 6-12% sustentados por ≥1 ano.
  *Ressalvas verificadas:* (a) a comparação com analistas de IC é ~25-30% **conforme relatório do próprio GJP**,
  não experimento controlado independente (a plataforma de elicitação diferiu no Ano 3 do IARPA-ACE);
  (b) a melhora de habilidade se aplica a horizontes curtos a médios — previsões a 5+ anos regridem em direção
  ao acaso; (c) a superação consistente de analistas de IC é específica ao tier de superprevisores (~2% do
  topo), não ao conjunto geral de voluntários GJP. A base empírica fundacional antecede 2015, originando-se em
  Tetlock (2005). [verificado com ressalva]
- **Confiabilidade do juiz como problema mensurável** (Survey on LLM-as-a-Judge, arXiv:2411.15594): consistência,
  robustez e alinhamento com humano são **dimensões a medir e melhorar**, não correção binária a afirmar.
  [verificado 3-0]

## Teoria de medida: a régua justa não é o oráculo

**GUM (JCGM 100:2008) + Kacker, 2018 (PMC9074737), verificado 3-0.** O "valor verdadeiro" é teórico e
**inacessível em princípio**; o erro relativo a ele é conceitual e desconhecível. A incerteza é "a dispersão dos
valores que podem razoavelmente ser atribuídos ao mensurando", **deliberadamente desacoplada** do valor
verdadeiro. O resultado científico é o melhor valor **mais** sua dispersão, não a distância a uma verdade que
ninguém vê. E há piso irredutível: a **incerteza definicional** (VIM3 2.27) fixa um mínimo que técnica nenhuma
cruza — análogo metrológico do teto de informação.
*Ressalva verificada:* essa é a leitura **operacional/anti-realista oficial** do GUM; o próprio Kacker argumenta
que o GUM retém uma leitura realista latente, então não é tão limpo quanto soa.
Somado a confiabilidade vs validade (Bhattacherjee, já no DOSSIE): a **régua justa** de um juiz é o **piso de
ruído entre avaliadores competentes com a mesma informação** (a concordância humano-humano), não um avaliador
perfeito.

## O que isto fixa para o Strata

1. **A falácia morre.** "Não é perfeito, logo não serve" exige furar o teto epistêmico — o que nem humano faz.
   O alvo legítimo é a distância, em escala, ao melhor-possível-dado-o-input.
2. **Duas distâncias, sempre separadas.** Teto de informação (irredutível, a **nomear**) vs lacuna de
   capacidade (redutível, a **medir e melhorar**). A Fase B mistura as duas quando tira o gabarito: parte da
   queda é informação removida, não juízo que faltou.
3. **Convergência é estimativa, não posse.** Por isso o núcleo sólido ancora no gold mecânico; o consenso entre
   juízes correlacionados não promove sozinho à verdade.
4. **Independência é quantidade, não chave liga/desliga.** Cross-vendor mede-se em votos efetivos (neff), não em
   "independente: sim/não".
5. **O resultado honesto carrega sua incerteza.** Reportar deltas, IC, α corrigido por acaso — não absolutos —
   é a forma metrológica correta, não modéstia.

## Itens abertos que este fundamento deixa

- **Verificação completa.** Todos os eixos (A/B/C/D/E/F/H + instrumentos E/G) foram verificados por voto
  adversarial 3-0. Nenhum refutado. As ressalvas de formulação, atribuição e escopo estão integradas acima.
  Não há `[a-verificar]` remanescentes.
- **Protocolo prático do teto.** Como os estimadores de desemaranhamento aleatória/epistêmica são contaminados,
  falta definir o protocolo operacional para estimar o **piso de ruído entre avaliadores competentes** sem
  depender deles. (É o que o gold mecânico já faz onde existe.)
- **neff real do nosso painel.** Dado o erro correlacionado cross-vendor (φ ≈ 0,39 documentado em
  arXiv:2605.29800), quantos juízes independentes efetivos um painel típico nosso tem, e quanto descontar a
  garantia de Condorcet para fixar a "régua justa".
- A crítica realista à verdade-por-convergência (Rorty/Quine/Russell/fatos-perdidos) merece um parágrafo no
  DOSSIE se o argumento for a público, para não soar ingênuo quanto a "consenso = verdade". O material
  verificado (eixo C, ressalvas de atribuição) já fornece a base.
