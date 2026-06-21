---
title: 'Fundamento epistêmico do juiz: escala mensurável, não binário perfeito/impossível'
created: 2026-06-21
updated: 2026-06-21
status: 'REGISTRO conceitual. Fundamenta a §1-2 do DOSSIE-judge com filosofia da ciência + matemática + computação. Verificação adversarial concluída (2026-06-21, resume): eixos A/D/E/H VERIFICADOS por voto 3-0; eixos B/C/F (Quine-Duhem, Peirce, Popper/Lakatos/Kant) e instrumentos nomeados de E/G (Condorcet, Aumann, Simon, Brier, Tetlock) seguem [a-verificar] — fontes buscadas, mas sem claim aprovado no voto.'
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

**Subdeterminação (Quine-Duhem; SEP, "Underdetermination of Scientific Theory"). [a-verificar]**
Evidência finita é compatível com mais de uma teoria. Nenhum conjunto de dados força uma leitura única.
Aplicado ao juiz: pedir que ele "ache a verdade" a partir de input finito pede o que a própria ciência não tem.
O alvo viável é a melhor leitura **sustentável** pelo input, com a incerteza declarada.

## Verdade como convergência — e suas críticas [a-verificar]

**Peirce (via Philosophy Compass, Misak): verdade = "a opinião fadada a ser, no fim, aceita por todos que
investigam".** Convergência é **esperança regulativa**, um norte teleológico, não uma linha de chegada onde
tudo se assenta. Casa com o ideal regulativo de Kant já citado no DOSSIE §2.1.

Mas a teoria da convergência **tem críticos**, e é honesto carregá-los:
- Rorty: não existe "audiência ideal", como não existe maior inteiro.
- Quine: "mais perto da verdade" é mal definido entre teorias.
- Russell: por que **um** estado-final, e não convergência plural?
- "Fatos perdidos" (Smart, Field): há verdades que podem ficar para sempre indescobríveis.

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

**Teorema do Júri de Condorcet (SEP, "Jury Theorems").** Votantes acima de 0,5 de competência e **independentes**
convergem à resposta correta com mais votantes. Duas condições, não uma.

**Sob dependência, a garantia degrada — e pode inverter.**
- Teoremas de inteligência coletiva (Hong-Page, Condorcet, milagre da agregação) pressupõem nível de
  competência; sem controlar capacidade, podem **operar ao contrário** e levar o grupo ao erro quase certo
  (arXiv:2307.04709). [sourced]
- Empírico em LLM (Kim, Garg, Peng & Garg, "Correlated Errors in LLMs", ICML 2025, arXiv:2506.07962; 350+
  modelos): pares concordam na **mesma resposta errada ~60% das vezes**, contra ~33% esperado se os erros fossem
  independentes. A correlação **cresce com a acurácia**, mesmo entre arquiteturas e fornecedores distintos. Juiz
  correlacionado **infla** o acerto medido. Efeito ligado à **monocultura algorítmica** (Kleinberg & Raghavan,
  PNAS, 2021). [verificado 3-0]
- Viés compartilhado de familiaridade/perplexidade: juízes super-recompensam texto de baixa perplexidade,
  um viés **não-aleatório e comum**, que fere a independência (arXiv:2410.21819). [sourced]
- **Teorema do Acordo de Aumann:** agentes racionais com priores comuns convergem — convergência pode vir de
  **prior compartilhado**, não de acerto.

Consequência direta para o Eixo 1 do DOSSIE: convergência cross-vendor é **proxy de independência parcial,
medida em escala** (ex.: votos efetivos independentes, neff), **não prova de correção**. É exatamente a nossa
Fase B: dois juízes seguem concordando nas respostas erradas sem o gabarito.

## Falibilismo: ciência é aproximação, não posse [a-verificar]

Popper (SEP): falibilismo + **verisimilitude/truthlikeness** — teorias são mais ou menos próximas da verdade,
numa **escala**, sem nunca a possuírem. Lakatos (já na bibliografia): programas de pesquisa progridem ou
degeneram. Peirce: fallibilismo, nenhum consenso é final.
Tudo aponta para o mesmo: o sucesso é **afastamento mensurável do erro reconhecido**, não toque no absoluto.

## Medir julgamento numa escala contínua

A prática já sabe avaliar julgamento sem oráculo binário. *(Instrumentos nomeados [a-verificar]; o enquadramento
"confiabilidade do juiz como problema mensurável" está verificado 3-0 via survey de LLM-as-judge,
arXiv:2411.15594.)*
- **Racionalidade limitada** (Simon; SEP): o agente real **satisfaz** dentro de recursos finitos; o padrão é o
  bom-o-suficiente medido, não o ótimo inalcançável. [a-verificar]
- **Regras de pontuação próprias** (Brier score): pontuam a **probabilidade** declarada, premiando calibração,
  numa escala contínua, não em certo/errado. [a-verificar]
- **Good Judgment Project** (Tetlock): previsores são rankeados por acurácia probabilística ao longo do tempo —
  julgamento avaliado como **escala**, não como acerto único. [a-verificar]
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

- **Eixos A/D/E/H verificados (3-0).** Faltam verificar com fonte primária os eixos **B (Quine-Duhem),
  C (Peirce + críticas realistas), F (Popper/Lakatos/Kant)** e os instrumentos nomeados de E/G (enunciado do
  Teorema de Condorcet e sua degradação sob dependência, Aumann, Simon, Brier, Tetlock): as fontes foram
  buscadas, mas nenhum claim sobreviveu ao voto — entram aqui como [a-verificar]. Pede uma passada de fetch
  dedicada antes de uso EXTERNO.
- **Protocolo prático do teto.** Como os estimadores de desemaranhamento aleatória/epistêmica são contaminados,
  falta definir o protocolo operacional para estimar o **piso de ruído entre avaliadores competentes** sem
  depender deles. (É o que o gold mecânico já faz onde existe.)
- **neff real do nosso painel.** Dado o erro correlacionado cross-vendor, quantos juízes independentes efetivos
  um painel típico nosso tem, e quanto descontar a garantia de Condorcet para fixar a "régua justa".
- A crítica realista à verdade-por-convergência (Rorty/Quine/Russell/fatos-perdidos) merece um parágrafo no
  DOSSIE se o argumento for a público, para não soar ingênuo quanto a "consenso = verdade".
