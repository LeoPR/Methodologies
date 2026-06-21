---
title: 'Fundamento epistêmico do juiz: escala mensurável, não binário perfeito/impossível'
created: 2026-06-21
updated: 2026-06-21
status: 'REGISTRO conceitual. Fundamenta a §1-2 do DOSSIE-judge com filosofia da ciência + matemática + computação. Fontes autorais (SEP, arXiv, GUM); verificação adversarial da rodada de 2026-06-21 foi interrompida por limite de gasto, então claims marcados [sourced] não passaram pelo voto 2/3 — reconferir antes de uso externo.'
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
  o que se sabe; a epistêmica é a parte que mais informação/capacidade reduz. [sourced]
- **Erro de Bayes** (Bayes error rate): piso inferior de erro que **nenhum** classificador supera, fixado pela
  sobreposição das densidades, isto é, uma propriedade dos **dados**, não da capacidade do agente. [sourced]
- **Desigualdade de processamento de dados** (Shannon; Cover & Thomas, 2006): nenhum pós-processamento cria
  informação que não estava na entrada. O juiz não pode extrair o que o input não contém. [sourced]

**Deficiência de capacidade (redutível, em escala).**
Outra coisa é quando um par competente, **com a mesma informação**, julga melhor. Aí há deficiência real do
juiz, mas medida numa escala (quão perto do par ele chega), não num binário "serve/não serve".

**Complicação honesta (não ignorar).**
A divisão limpa entre os dois não é gratuita. A classificação de uma incerteza como aleatória ou epistêmica é
**relativa ao modelo e à informação considerados**, não uma propriedade absoluta do mundo (ICLR 2025 blogpost).
O que parece irredutível a um modelo fraco pode ser reduzido por um mais forte. E os métodos que tentam
**separar** as duas são "fundamentalmente incompletos" e difíceis de interpretar (arXiv:2505.23506, confirmado
3-0). Logo: a distinção é uma **lente útil**, não uma régua que se lê sem ruído.

## Por que evidência finita não fixa verdade única

**Subdeterminação (Quine-Duhem; SEP, "Underdetermination of Scientific Theory").**
Evidência finita é compatível com mais de uma teoria. Nenhum conjunto de dados força uma leitura única.
Aplicado ao juiz: pedir que ele "ache a verdade" a partir de input finito pede o que a própria ciência não tem.
O alvo viável é a melhor leitura **sustentável** pelo input, com a incerteza declarada.

## Verdade como convergência — e suas críticas

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
(indefinibilidade da verdade). [sourced via SEP/Wikipedia]

O ponto que **fundamenta a tese da escala** (arXiv/ACM:10.1145/3603371): a impossibilidade de garantia
**dedutiva 100%** não torna a tarefa sem esperança. As impossibilidades negam **certeza**; abordagens
probabilísticas/indutivas conseguem muito, e as impossibilidades "enfraquecem substancialmente assim que se
admite incerteza". A pergunta aberta deixa de ser "é possível ou impossível?" e passa a ser "**quanto basta?**".
Isto **é** a passagem do binário para a escala mensurável que você defende.

## Convergência de júri: a garantia depende de independência

**Teorema do Júri de Condorcet (SEP, "Jury Theorems").** Votantes acima de 0,5 de competência e **independentes**
convergem à resposta correta com mais votantes. Duas condições, não uma.

**Sob dependência, a garantia degrada — e pode inverter.**
- Teoremas de inteligência coletiva (Hong-Page, Condorcet, milagre da agregação) pressupõem nível de
  competência; sem controlar capacidade, podem **operar ao contrário** e levar o grupo ao erro quase certo
  (arXiv:2307.04709). [sourced]
- Empírico em LLM (Kim et al., ICML 2025, arXiv:2506.07962): pares de modelos concordam na **mesma resposta
  errada ~60% das vezes**, contra ~33% esperado se os erros fossem independentes. A correlação **cresce com a
  acurácia**, mesmo entre fornecedores distintos. Juiz correlacionado **infla** o acerto medido. [sourced]
- Viés compartilhado de familiaridade/perplexidade: juízes super-recompensam texto de baixa perplexidade,
  um viés **não-aleatório e comum**, que fere a independência (arXiv:2410.21819). [sourced]
- **Teorema do Acordo de Aumann:** agentes racionais com priores comuns convergem — convergência pode vir de
  **prior compartilhado**, não de acerto.

Consequência direta para o Eixo 1 do DOSSIE: convergência cross-vendor é **proxy de independência parcial,
medida em escala** (ex.: votos efetivos independentes, neff), **não prova de correção**. É exatamente a nossa
Fase B: dois juízes seguem concordando nas respostas erradas sem o gabarito.

## Falibilismo: ciência é aproximação, não posse

Popper (SEP): falibilismo + **verisimilitude/truthlikeness** — teorias são mais ou menos próximas da verdade,
numa **escala**, sem nunca a possuírem. Lakatos (já na bibliografia): programas de pesquisa progridem ou
degeneram. Peirce: fallibilismo, nenhum consenso é final.
Tudo aponta para o mesmo: o sucesso é **afastamento mensurável do erro reconhecido**, não toque no absoluto.

## Medir julgamento numa escala contínua

A prática já sabe avaliar julgamento sem oráculo binário:
- **Racionalidade limitada** (Simon; SEP): o agente real **satisfaz** dentro de recursos finitos; o padrão é o
  bom-o-suficiente medido, não o ótimo inalcançável.
- **Regras de pontuação próprias** (Brier score): pontuam a **probabilidade** declarada, premiando calibração,
  numa escala contínua, não em certo/errado.
- **Good Judgment Project** (Tetlock): previsores são rankeados por acurácia probabilística ao longo do tempo —
  julgamento avaliado como **escala**, não como acerto único.

## Teoria de medida: a régua justa não é o oráculo

**GUM (JCGM 100:2008), confirmado 2-0 nesta rodada.** A incerteza é "a dispersão dos valores que podem
razoavelmente ser atribuídos ao mensurando", **deliberadamente desacoplada** do "valor verdadeiro" inacessível
e do "erro". Ou seja: o resultado científico é o melhor valor **mais** sua dispersão, não a distância a uma
verdade que ninguém vê.
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

- A verificação adversarial desta rodada foi cortada por limite de gasto: os claims [sourced] precisam passar
  pelo voto 2/3 antes de citação externa.
- Falta fechar a desigualdade de processamento de dados e o erro de Bayes com a fonte primária (Cover & Thomas;
  Hüllermeier & Waegeman) lida na íntegra, não só pelo resumo.
- A crítica realista à verdade-por-convergência (Rorty/Quine/Russell/fatos-perdidos) merece um parágrafo no
  DOSSIE se o argumento for a público, para não soar ingênuo quanto a "consenso = verdade".
