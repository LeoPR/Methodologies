---
title: 'Pré-registro: bateria de temporalidade v1 (ordem por dependência, horário errado, lacuna, intruso, ambiguidade, fora do script)'
created: 2026-09-30
updated: 2026-09-30
status: 'Pré-registrado; não rodado.'
tags: [temporalidade, pre-registro, bateria, capacidade]
---

# Pré-registro: bateria de temporalidade v1

## 1. Pergunta

Diante de cenas de um mesmo episódio fora de ordem, um modelo:

- reconstrói a ordem pela dependência entre estados, e não pela ordem em que as cenas aparecem;
- segue a dependência quando um horário anotado a contradiz, e aponta o conflito;
- nota que falta uma mudança que nenhuma cena mostra, e diz qual;
- aponta a cena que não pertence ao episódio;
- deixa sem ordem o que a evidência não ordena;
- segue o que foi observado quando o episódio foge do roteiro esperado?

E um protocolo curto, derivado da [ONTOLOGIA](ONTOLOGIA.md) v0, muda isso sem aumentar o alarme
falso?

É um instrumento de **capacidade**, não um A/B do Strata. Mede o modelo com e sem um protocolo, e
o canônico não muda por causa dele. Se o protocolo ajudar, o que for novo em relação ao §3 do
Strata ("Ler o tempo de volta") vira proposta à parte, com teste próprio no harness do Strata.
Origem do desenho: [AVALIACAO-testes-sinteticos.md](AVALIACAO-testes-sinteticos.md) (esboço T1–T7).

**Conferência do núcleo (2026-09-30).** Reli, no canônico PT:

- o §3, "Ler o tempo de volta": as regras 1, 2 e 5 do protocolo o reescrevem para cenas;
- o §4 inteiro: hipótese antes; registro que se refaz; resultado negativo preservado; ameaças
  explícitas;
- o §6: verificar antes de afirmar;
- o §9: avisar à toa é excesso, e por isso os controles medem o alarme falso.

Este teste não toca o `recipe/`.

## 2. Instrumento

Tudo em `eval/temporalidade/` (congelado no commit que registra este pré-registro):

- `bateria-v1.json`: fixtures, gabarito, tarefa e protocolo.
- `hb_tb.py`: runner. Monta o prompt e chama o provedor pelo `hb_runner` do harness do Strata.
- `score_tb.py`: pontuador mecânico.
- `analise_tb.py`: a análise deste pré-registro (§4–§5), com a revisão manual sobreposta.
- `revisao_tb.py`: sorteio e lista cega da revisão manual (§4), e a concordância.
- `testa_score_tb.py` e `ataque_score_tb.py`: casos de unidade e do red-team do pontuador; a única
  falha conhecida (letra repetida como notação de grafo) é ambígua e vai para a revisão.

**Rótulos.** O modelo vê as cenas rotuladas A, B, C… na ordem em que aparecem, não a letra interna
do gabarito. A letra interna denunciaria a lacuna (A, C, D, E) e o intruso (sempre F). O cabeçalho
de cada saída grava `mapa=` (as letras internas na ordem de apresentação), e o pontuador traduz a
resposta por ele.

**Tarefa** (igual nos dois braços): reconstruir a sequência. As duas últimas linhas são
`SEQUÊNCIA:` (letras separadas por `→`; `|` entre cenas cuja ordem não dá para saber) e `NOTA:`
(ressalvas sobre a reconstrução, se houver, ou "nenhuma"). A redação é neutra: não nomeia lacuna,
intruso nem conflito, para não entregar as famílias ao braço ingênuo.

**Dois domínios.** P é o paraquedas, sem regras: o leitor usa o conhecimento do mundo. O é um
processo inventado (orbe, suporte, selo), com cinco regras dadas no prompt: o leitor só tem as
regras.

**Critério de lacuna, o mesmo nos dois domínios.** Falta um passo quando uma cena pressupõe um
estado que nenhuma cena mostra e que não vinha desde o começo do episódio. Um estado que a própria
cena afirma conta como mostrado. Na linha principal, cada estado pressuposto aparece em alguma
cena: os controles não têm lacuna por esse critério. Na família T3, um estado some (o avião no ar;
o orbe encaixado e carregado).

| família | papel | P | O | acerto |
|---|---|---|---|---|
| T1 | ordem (controle) | 5 cenas: embarque, decolagem, salto, velame até pousar, recolhe | 5 cenas: polido, encaixado e carregado, brilha, selo rompido, guardado | ordem certa; nota sem alarme |
| T2 | horário errado | horário do velame antes do salto | horário do selo rompido antes do brilho | nota fala do horário e da contradição |
| T2c | horário coerente (controle) | mesmas cenas, horários plausíveis | idem | nota sem alarme |
| T3 | lacuna | sem a decolagem: embarca no chão; na cena seguinte, salta da porta | sem o encaixe e a carga: fora do suporte, depois brilhando nele | a nota nomeia o passo e marca que falta, ou um item acrescentado à sequência o nomeia |
| T4 | intruso | quiosque de sorvete na praia | chuva sobre uma igreja numa cidade do litoral | a cena fica fora da sequência, ou a nota a cita com marca de "não pertence" |
| T5 | ambiguidade | vestir o paraquedas × um funcionário encostar a escada: ambos antes do embarque, sem ordem entre si | orbe polido × suporte vazio: ambos antes do encaixe | os dois no mesmo grupo `|`, ou a nota diz que a ordem entre eles não se sabe |
| T6 | fora do script (só P) | o velame abre dentro da cabine e ela desce sem queda livre | — | ordem observada, sem omitir cena; nota sobre o desvio é permitida |

São 13 fixtures, cada uma em duas ordens de apresentação fixas, nenhuma igual à ordem real nem à
inversa. O gabarito de T5 cabe na notação de grupos (conferido por script). O **T7** do esboço
("agora", status contra a data) fica fora da v1: já é medido pelo `f6-agora` no harness do Strata.

## 3. Braços

| braço | prompt |
|---|---|
| ingênuo | [regras do domínio O] + cenas + tarefa |
| protocolo | protocolo de 6 regras + [regras do domínio O] + cenas + tarefa |

O protocolo está no `bateria-v1.json`. Suas seis regras:

1. A ordem sai da dependência.
2. Horário é evidência revogável.
3. Estado pressuposto, não mostrado e que não vinha do começo, é um passo que falta.
4. Cena que não trata das mesmas pessoas ou objetos, nem depende das outras, não pertence.
5. Sem dependência, a ordem não se sabe.
6. O inferido se marca.

Fora da v1:

- o braço com ordenador externo (o [protótipo](prototipo/)), que exige extrair as dependências
  antes;
- um braço-placebo de mesmo comprimento;
- a variação do número de cenas.

## 4. Pontuação

`score_tb.py`, por papel:

- **Ordem:** ORDEM-CERTA quando nenhum par do gabarito vem invertido, nenhum par comparável fica
  no mesmo grupo e nenhuma cena do gabarito é omitida. O intruso não está no gabarito, e deixá-lo
  fora não conta contra a ordem.
- **Nota:**
  - controles: NOTA-LIMPA ou ALARME;
  - T2: CONFLITO-APONTADO ou CONFLITO-OMITIDO;
  - T3: LACUNA-APONTADA ou LACUNA-SILENCIOSA;
  - T4: INTRUSO-APONTADO ou INTRUSO-INCLUIDO;
  - T5: INCOMP-DECLARADO, INCOMP-PARCIAL ou INCOMP-FORCADO;
  - T6: SEGUE-OBSERVADO ou ORDEM-ERRADA.
- **Menção negada não conta** ("não há conflito"; "sem lacunas, contradições ou intrusos").
- **Vocabulário por fixture** fica no JSON: `lacuna_rx` (o passo que falta), `intruso_rx` (a cena
  intrusa) e `incomp_txt` (as cenas sem ordem, pelo conteúdo).
- **SEM-LINHA** (sem a linha SEQUÊNCIA) fica fora do denominador e é reportado por braço, separando
  o corte por tamanho (`stop=length`) do erro de formato. Na análise de sensibilidade, SEM-LINHA
  conta como falha.

**Revisão manual cega ao braço e ao modelo.** O red-team mostrou que o vocabulário das notas vaza
de qualquer lista de palavras. Por isso a revisão é a salvaguarda, não um enfeite. Ela é feita em
etapas:

1. **Amostra.** Cada família × braço é um estrato.
   - Das saídas cuja nota diz algo além de "nenhuma", sorteiam-se 25% por estrato, com mínimo de 20
     (ou todas, se houver menos).
   - Das saídas com nota "nenhuma", sorteiam-se 5%, para conferir a leitura da SEQUÊNCIA.
   - A semente é 20260930.
2. **Revisão.** A lista sai embaralhada, sem braço nem modelo. Para cada saída, classifico o que o
   leitor fez, com o gabarito à mão.
3. **Concordância.** Reporta-se a concordância entre pontuador e revisão por família (fração e
   kappa de Cohen).
4. **Ampliação.** Família com concordância abaixo de 0,90 nas notas não triviais tem **todas** as
   notas não triviais revisadas.

A revisão fica em `planos/tb-v1-revisao.csv`, sobrepõe a classe do pontuador e é transcrita no
RESULTADOS. A análise usa a classe revisada onde houver; nas demais, a do pontuador.

**Colunas** (ADR-006), sempre com k/K:

- **acerto**: fração de saídas com a classe certa, por família × domínio × braço;
- **consistência**: fração de células (modelo × fixture × braço) em que as 2 apresentações × K
  execuções dão a mesma classe;
- **efeito de apresentação**: acerto na apresentação 0 × na 1.

## 5. Hipóteses

- **H1 (o protocolo ajuda a notar).** Nas famílias T2, T3, T4 e T5, o acerto da nota no braço
  protocolo supera o do ingênuo. Critério por família: diferença ≥ 0,15 e intervalo de 95% (bootstrap
  por modelo, 2000 reamostragens, semente 20260930) acima de zero. H1 vale se isso ocorre em pelo
  menos 3 das 4 famílias.
- **H2 (sem custo nos controles, não inferioridade).** Em T1 + T2c (P e O juntos):
  - o alarme falso no protocolo não passa do ingênuo + 0,10;
  - a ordem certa no protocolo não fica abaixo do ingênuo − 0,10.
- **Regra de teto.** Família com acerto ≥ 0,90 no ingênuo não discrimina: H1 fica "sem poder (teto)"
  nela, e o critério de 3 de 4 passa a valer sobre as famílias restantes (maioria delas).
- **Descritivo** (sem decisão):
  - ingênuo por família × domínio: onde a capacidade falta sem ajuda;
  - P × O por família (conhecimento de mundo × só regras);
  - T6;
  - efeito de apresentação e consistência;
  - SEM-LINHA por braço;
  - leitura por modelo e por fabricante.

## 6. Decisão

1. **H2 violada:** o protocolo, como está escrito, faz avisar à toa. Não vira recomendação; o
   texto se revisa numa v2 com novo pré-registro.
2. **H1 e H2:** o protocolo vira material da frente de temporalidade (método próprio, separado do
   Strata). As regras que o §3 do Strata não tem (3, lacuna; 4, intruso; 6, marcar o inferido)
   viram uma proposta com A/B próprio no harness do Strata; nada entra no canônico por este teste.
3. **H2 sem H1:** registra-se em quais famílias o protocolo ajuda e em quais não. Onde instrução
   não resolve, a falta é de capacidade, e o próximo braço a testar é o ordenador externo (v2).
4. Em qualquer caso, o ingênuo por família é o mapa de capacidade da v1, e se registra com o
   negativo.

## 7. Modelos, K e custo

Painel de 8 fabricantes, o mesmo do F6. Temperatura 0,3 (GPT-6 ignora); raciocínio no padrão do
modelo; `num_predict` 8000. K = 3; as 13 fixtures × 2 apresentações × 2 braços dão 156 chamadas por
modelo. Os provedores variam, mas os pesos são os mesmos (o provedor fica gravado no cabeçalho).

1. **Etapa grátis** (NVIDIA): `openai/gpt-oss-20b`, `google/gemma-4-31b-it`,
   `nvidia/nemotron-3-super-120b-a12b`.
2. **Etapa paga** (OpenRouter): `openai/gpt-6-luna`, `google/gemini-3.5-flash-lite`,
   `meta/muse-glimmer-30b`, `z-ai/glm-5.3`, `deepseek/deepseek-v4.1-flash`.

A etapa paga roda depois da grátis, **salvo** se a grátis revelar defeito de fixture: uma família
em que todos erram por causa da redação, confirmada na leitura. Nesse caso se conserta, se registra
desvio e se roda de novo antes de gastar. Teto de gasto: US$ 5 (os prompts são curtos).

## 8. Ameaças à validade

- **P e O diferem em mais que familiaridade.** O tem regras explícitas e P não. A diferença P × O
  não se atribui só ao conhecimento de mundo.
- **Granularidade.** Entre duas cenas sempre há transições miúdas (ir até a porta, abrir a porta).
  Um leitor rigoroso pode apontá-las nos controles. O alarme falso mede isso, e a revisão manual
  separa "apontou transição trivial" de outros alarmes.
- **Pontuador por regex.** Mitigado por testes de unidade, red-team e revisão cega (§4).
  - No red-team, o pontuador acertou 14 de 18 casos reservados, escritos depois das correções.
  - As 4 falhas eram de vocabulário. Os termos foram incorporados, e o conjunto reservado ficou
    gasto.
  - A estimativa honesta de generalização é essa, antes do conserto. A revisão amostral mede a
    concordância real.
- **Comprimento.** O braço protocolo é mais longo. Sem placebo, o efeito pode ser de atenção e não
  de conteúdo.
- **Tarefa.** A tarefa diz "um mesmo episódio", o que puxa contra o T4. É intencional: é o caso real,
  em que o registro não avisa o intruso.
- **Rótulos.** Seguem a ordem de apresentação: responder em ordem alfabética é seguir a apresentação
  (medido no efeito de apresentação).
- **Amostra.** Só português; duas apresentações por fixture; poucas fixtures por família (2, e 1
  no T6); 8 modelos, com bootstrap por modelo.
- **Desenvolvimento.** Antes deste registro, fixtures, protocolo e pontuador foram ajustados em
  três frentes:
  - testes de fumaça (rótulo `tb-smoke`, dois modelos grátis);
  - um solver cego, que resolveu as fixtures sem o gabarito e depois confrontou;
  - um ataque ao pontuador.

  Os consertos foram:
  - rótulos pela apresentação;
  - critério único de lacuna;
  - cenas que produzem o estado da seguinte;
  - gabarito do T5 expressável na notação;
  - regras 3 e 4 do protocolo;
  - regras 4 e 5 do domínio O só como pré-condição (abaixo);
  - negação e vocabulário no pontuador.

  As saídas dos testes de fumaça não entram na análise.
- **Redação das regras do domínio O.** Nos testes de fumaça, um modelo leu duas regras como
  imediatas:
  - "o selo se rompe **quando** brilha" virou "rompe assim que brilha";
  - "**depois que** o selo se rompe, é guardado" virou "guarda-se logo em seguida".

  As regras 4 e 5 foram reescritas só como pré-condição ("só se guarda um orbe cujo selo já se
  rompeu"). Erro de leitura que sobrar é do modelo e conta como erro.

## 9. Desvios

(Anexados com data, se houver.)
