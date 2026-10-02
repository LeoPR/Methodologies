---
title: 'Pré-registro: bateria de temporalidade v2 (regra 3 por estado, não por ação; placebo; teto de 32k; etapas por dedução)'
created: 2026-10-01
updated: 2026-10-01
status: 'Pré-registrado em 2026-10-01, depois de uma revisão adversarial (§11). Nenhuma chamada da v2 foi feita antes deste registro.'
tags: [temporalidade, pre-registro, bateria, capacidade, placebo]
---

# Pré-registro: bateria de temporalidade v2

## 1. Pergunta

A v1 ([PREREG](PREREG-bateria-v1.md), [RESULTADOS](RESULTADOS-bateria-v1.md)) mostrou duas coisas:

- o protocolo faz notar horário errado, lacuna, intruso e ambiguidade:
  - no modo principal, o H1 vale em 4 de 4 famílias;
  - na sensibilidade, com o teto de 8000, em 2 de 4;
  - com o teto de 32k, em 4 de 4, por dedução e sem revisão manual;
- mas faz avisar à toa nos controles (H2 violada: alarme falso de 0,02 para 0,21).

A v2 pergunta:

1. Reescrever a regra 3 (pensar em estados, não em ações) traz o alarme falso de volta à margem e
   mantém o ganho na lacuna (o critério do H1 no T3)?
2. O ganho do protocolo vem do conteúdo, ou só de um prompt mais longo?

Continua sendo um instrumento de **capacidade**, não um A/B do Strata. O canônico não muda por causa
dele.

**Conferência do núcleo (2026-10-01).** Reli, no canônico PT:

- o §3, "Ler o tempo de volta": as regras 1, 2 e 5 do protocolo o reescrevem para cenas; a regra 3
  trata da lacuna, que o §3 não cobre;
- o §4 inteiro: hipótese antes; registro que se refaz; negativo preservado; ameaças explícitas;
- o §9: avisar à toa é excesso; é o que o H2 mede.

Este teste não toca o `recipe/`.

## 2. Por que a regra 3 muda assim

O diagnóstico da v1: 24 dos 34 alarmes falsos do protocolo apontavam "transição trivial", como "falta
a abertura da porta do avião" ou "falta o ato de encaixar". O RESULTADOS deixou uma hipótese para a v2:
"falta um passo quando o estado que uma cena pressupõe é incompatível com o último estado mostrado".

Antes de escrever a regra, confrontei essa hipótese com o texto das fixtures:

- **O critério da v1 já separava os casos.** Pelo §2 da v1, "um estado que a própria cena afirma conta
  como mostrado".
  - A cena do salto afirma "da porta aberta": a porta não é lacuna.
  - No controle T1-O, a cena B afirma "encaixado": o encaixe não é lacuna.
  - Falta só o que nenhuma cena afirma: o avião no ar (T3-P); a carga do orbe (T3-O; o gabarito aceita
    também o encaixe, §9.5 da v1).
- **A maior parte dos alarmes apontava ações** cujo estado resultante a própria cena já mostra. Outra
  parte vinha dita em estados ("estado de porta aberta pressuposto … não é mostrado em nenhuma cena"),
  quando a própria cena descreve esse estado.
- **A redação da v1 deixava as duas leituras.** A regra 3 dizia "um estado que nenhuma cena mostra", sem
  dizer que a própria cena conta, nem que ação e estado são coisas diferentes. A regra 1 dizia "vem
  depois da cena que o **produz**": nenhuma cena "produz" a porta aberta, e um leitor da v1 usou isso
  para apontar falta.
- **"Incompatível com o último estado", ao pé da letra, marcaria um controle.** No T1-O, o orbe está
  fora do suporte (A) e depois encaixado (B): os estados são incompatíveis, e não há lacuna, porque B
  descreve o estado novo. Por isso a incompatibilidade não vira o critério operante.

A v2 mantém o critério da v1 e muda a redação:

> 1. A ordem sai da dependência: uma cena que pressupõe um estado vem depois da cena que o **descreve**.
> (o resto igual)
>
> 3. Raciocine sobre estados, não sobre ações. Falta um passo quando uma cena pressupõe um estado que
> nenhuma cena descreve e que não vinha desde o começo (o que a primeira cena pressupõe vinha do
> começo): diga qual. Pressupor não é descrever. A ação que leva a um estado que alguma cena já
> descreve (uma gaveta já aberta, uma luz já acesa) não é passo que falta.

- **"Pressupor não é descrever"** fecha a leitura em que a cena do salto "mostra" o avião no ar porque o
  salto o implica.
- **"O que a primeira cena pressupõe vinha do começo"** dá ao "começo" um sentido verificável.
- **O exemplo** usa objetos que não estão em nenhuma fixture.

Na [ONTOLOGIA](ONTOLOGIA.md) (§8), é a inércia do problema do quadro: a ação se infere da mudança de
estado; o que pode faltar é o estado.

## 3. O que muda em relação à v1, e o que fica

**Muda:**

- **Regras 1 e 3 do protocolo**, como acima. As regras 2, 4, 5 e 6 ficam iguais.
- **Domínio O, em todos os braços:**
  - "carregado" vira "carregado de energia" (regras 2 e 3; cena B de cinco fixtures);
  - entra uma linha nas regras: "Cada regra diz o que precisa ter acontecido antes; nenhuma diz o que
    acontece logo em seguida."
  - Por quê: na v1, o portão registrou "carregado" lido como "transportado" e regras "só… depois" lidas
    como suficientes, e a revisão classificou 5 dos 34 alarmes do protocolo como "regra mal lida".
- **Vocabulário da lacuna no pontuador** (`lacuna_rx` do T3-P e do T3-O, só na bateria v2). Ele passa a
  reconhecer a lacuna dita por estado ("o avião no ar", "voando", "sair do chão"; "carga", "energia").
  Com o vocabulário da v1, 7 de 8 notas desse tipo saíam silenciosas.
- **Braço placebo** (§4).
- **Teto de saída de 32 000 tokens**, gravado na bateria (`num_predict`) e no cabeçalho de cada saída
  (`max=`). A análise avisa se houver mistura de tetos. Na v1, o teto de 8000 cortou 116 saídas, e isso
  mede o teto, não o modelo. O nível de raciocínio fica no padrão de cada modelo (não é enviado).
- **Rota do GLM:** `z-ai/fp8`, a do fabricante. A `atlas-cloud/fp8` da v1 entra em laço (20 saídas sem
  conclusão mesmo com 32k); na rota oficial, a mesma fixture concluiu em 8 de 8.
- **Etapas por dedução** (§5).
- **Saídas fora de pasta sincronizada:** o runner escreve onde a variável `TB_PLANOS` mandar (nesta
  máquina, `Z:\outputs\Methodologies\temporalidade`). No repositório ficam só o código e os resultados.

**Fica:** as 13 fixtures (apresentações e gabarito), a tarefa, as regras 2, 4, 5 e 6, o resto do
pontuador, o critério do H1, a semente, K = 3 e o procedimento de revisão, com os acréscimos do §6.

**Instrumento** (`eval/temporalidade/`, congelado no commit que registra este pré-registro):

- `bateria-v2.json`: a v1 com as mudanças acima. Um script conferiu que só mudaram o protocolo, o
  placebo, as regras do domínio O, a cena B das cinco fixtures O, o `lacuna_rx` do T3 e o teto.
- `hb_tb.py`:
  - opção `--bateria` e braço `placebo`;
  - um rótulo usa uma bateria só (`BATERIA.txt` no rótulo e `bat=` no cabeçalho), e o runner recusa
    misturar;
  - a raiz das saídas vem de `TB_PLANOS`.
- `score_tb.py`: lê a bateria do rótulo, interrompe se um cabeçalho trouxer outra e lê o `max=`.
- `analise_tb.py`:
  - na v2, uma semente por comparação;
  - `--etapa A` deixa o placebo selado e imprime a decisão de parada;
  - o H3 e a checagem de manipulação rodam quando há placebo.
- `revisao_tb.py`: `amostra … anexar` sorteia só os estratos novos; `sem-<braço>` deixa um braço de fora.
- `run_tb.sh`: `TB_PLANOS`, `TB_FIX` e `TB_EXTRA` opcionais.
- **Regressão sobre as saídas da v1:** saem idênticos aos de antes das mudanças:
  - a análise (modo principal, sensibilidade e leitura de 32k);
  - o resumo do pontuador;
  - os itens e a amostra da revisão (estes, conferidos numa cópia em pasta temporária).

  O CSV do pontuador ganha a coluna `max`, vazia na v1.
- **Testes:**
  - casos do pontuador: 84/84, com a bateria v1 e com a v2;
  - leitura de cabeçalho: 17/17;
  - bateria e placebo: 5/5;
  - lacuna dita por estado: 13/13;
  - o red-team mantém a única falha conhecida da v1 (letra repetida como notação de grafo).

## 4. Braços

| braço | prompt | onde roda |
|---|---|---|
| ingênuo | [regras do domínio O] + cenas + tarefa | todas as famílias |
| protocolo | protocolo v2 + [regras do domínio O] + cenas + tarefa | todas as famílias |
| placebo | orientações neutras + [regras do domínio O] + cenas + tarefa | T2, T3, T4 e T5 (P e O) |

O **placebo** tem seis itens numerados, como o protocolo, e 96,6% do comprimento dele em caracteres
(961 × 995). Pede:

- leitura atenta das cenas e regras;
- a mesma letra para a mesma cena;
- português claro, voz ativa, um termo só para cada coisa;
- liberdade para raciocinar no corpo da resposta;
- o formato da tarefa e a revisão de erros de digitação.

Um script conferiu que ele não usa termos de ordem, tempo, dependência, falta, pertencimento,
inferência, fim, limpeza ou formato exato. O texto está no `bateria-v2.json`.

## 5. Etapas (ordem que decide por dedução)

Rótulo único para as duas etapas: `tb-v2`, na raiz `TB_PLANOS`.

0. **Fumaça** (rótulo `tb-v2-smoke`, fora da análise): uma chamada por modelo e braço na fixture T1-O.
   Confere que cada rota aceita o teto de 32k e os parâmetros pedidos, e que os três prompts se montam.
   Ninguém lê taxa por braço nessa etapa.
1. **Etapa A** (84 chamadas por modelo):
   - T1-P, T1-O, T2c-P, T2c-O, T3-P e T3-O, no ingênuo e no protocolo; 2 apresentações; K = 3;
   - o placebo do T3 (P e O), que fica **selado** até a Etapa B: a análise da Etapa A o exclui, e a
     revisão da A também. Assim, o contraste protocolo × placebo no T3 roda ao mesmo tempo.
   - A etapa grátis roda antes da paga, com um **portão**:
     - leitura cega, sem taxa por braço;
     - o portão olha só defeito de fixture; protocolo, placebo e regras ficam congelados;
     - qualquer conserto reinicia a Etapa A, com rótulo novo e desvio registrado.
2. **Decisão depois da A:**
   - **H2 violada → para.** A reescrita da regra não resolveu o alarme. Nada na Etapa B muda isso: o H2
     depende só dos controles, e todos estão na A.
   - **H2 vale, mas o T3 não cumpre o critério do H1 → para.** A reescrita calou a lacuna junto com o
     alarme. (T3 no teto, ingênuo ≥ 0,90, conta como cumpre: o ingênuo já nota.)
   - **H2 vale e o T3 cumpre → Etapa B.**
   - Se parar, o H1 e o H3 ficam **não determinados**, não "não vale". O mesmo vale se a Etapa B não
     rodar por saldo.
   - A decisão usa o modo principal (SEM-LINHA fora). Se a sensibilidade discordar, vale a leitura mais
     conservadora: a que para. Se o H2 virar só porque SEM-LINHA conta como alarme, registra-se essa
     causa (o modelo não terminou), e não "a reescrita não resolve".
   - O resultado do T3 e as classes revisadas da Etapa A ficam congelados para a análise final.
3. **Etapa B** (120 chamadas por modelo): T2-P, T2-O, T4-P, T4-O, T5-P, T5-O e T6-P no ingênuo e no
   protocolo, mais o placebo em T2, T4 e T5 (P e O). O H1 usa o T3 da Etapa A.

## 6. Pontuação e revisão

Como na v1 (§4 e §9 dela): SEM-LINHA, resposta do canal de raciocínio (`ft=1`), critérios de fronteira,
dois revisores cegos e adjudicação. Acréscimos:

- **Revisão completa onde a decisão depende dela:**
  - **Etapa A:** todas as notas não triviais de T1, T2c e T3, no ingênuo e no protocolo:
    `amostra tb-v2 sem-placebo`, depois `ampliar tb-v2 <família> sem-placebo` para T1, T2c e T3.
  - **Etapa B:**
    - T4 inteiro e o placebo do T3 inteiro: `amostra tb-v2 anexar`, depois `ampliar tb-v2 T4` e
      `ampliar tb-v2 T3`;
    - nas outras famílias, a amostra da v1 (25%, mínimo de 20; 5% das notas "nenhuma"), com a mesma
      regra de ampliação.
  - Por quê: na v1, o pontuador deixou passar 12 alarmes falsos nos controles e errou 35 vezes no T4;
    e o T3 decide a parada.
- **Livro de códigos dos controles.** É a régua da v1, conservadora, escrita antes de ver dados da v2:
  - **ALARME:** a nota diz que um passo ou estado falta, não aparece, não é descrito, fica implícito ou
    foi inferido; ou aponta conflito, erro, ordem indeterminada ou cena que não pertence. Exemplo da v1:
    "Inferido que a porta do avião foi aberta antes do salto" é ALARME.
  - **NOTA-LIMPA:** "nenhuma", ou só a afirmação de que não há problema, ou um comentário que não diz
    nada daquilo (por exemplo, repetir a dependência usada).
  - **Na dúvida, ALARME.**
- **Livro de códigos do T3:** é LACUNA-APONTADA quando a nota nomeia o passo ou o estado que falta (a
  decolagem ou o avião no ar; a carga ou o encaixe) e diz que ele falta, não aparece, não é descrito,
  fica implícito ou foi inferido. Os critérios de fronteira da v1 (§9.5) continuam.
- **Subtipo de cada alarme nos controles**, registrado pelos dois revisores: transição trivial; estado
  intermediário; regra mal lida; horário; só marca inferência; outro.

## 7. Hipóteses

- **H1 (o protocolo v2 ajuda a notar).** O mesmo critério da v1: nas famílias T2, T3, T4 e T5, protocolo −
  ingênuo ≥ 0,15 na nota, com IC 95% (bootstrap por modelo, 2000 reamostragens) acima de zero, em pelo
  menos 3 das 4. Regra de teto da v1. Decide-se no fim da Etapa B.
- **H2 (sem custo nos controles).** O mesmo critério da v1, com a mesma régua (§6), em T1 + T2c:
  - alarme falso no protocolo até o ingênuo + 0,10;
  - ordem certa no protocolo não abaixo do ingênuo − 0,10.

  O critério é a diferença pontual contra a margem, como a análise da v1 fez; o IC sai ao lado. "Vale"
  se lê como "não se detectou custo acima da margem". Decide-se no fim da Etapa A.
- **H3 (conteúdo, não comprimento).** Nas famílias T2–T5, protocolo − placebo ≥ 0,15 na nota, com IC 95%
  acima de zero, em pelo menos 3 das 4.
  - Teto: família com placebo ≥ 0,90 fica "sem poder", e o critério passa à maioria das restantes.
  - Se nenhuma família for avaliável, o H3 fica "sem poder".
  - **Checagem de manipulação:** se, numa família, o placebo der nota "nenhuma" mais que o ingênuo +
    0,10, o H3 é "não interpretável" nela (o placebo calou a nota) e ela sai da conta.
  - Decide-se no fim da Etapa B.
- **Semente.** Na v2, cada comparação tem a sua (20260930 + o nome da comparação). Assim, o IC de uma
  família não muda com a ordem ou o número das outras.
- **T3-P à parte** (descritivo, com consequência declarada). Se, no T3-P, o protocolo ficar abaixo do
  ingênuo + 0,05, registra-se que a v2 não nota a lacuna do paraquedas. Para ela, o próximo passo passa
  a ser o ordenador externo, qualquer que seja o resto.
- **Descritivo** (sem decisão):
  - placebo − ingênuo por família;
  - subtipos de alarme na v2 e na v1 (comparação entre versões: teto, rota do GLM, redação e
    vocabulário diferem);
  - T3-P × T3-O; `ft=1` e SEM-LINHA por braço; leitura por modelo.

## 8. Decisão

1. **Parou na Etapa A pelo H2:** esta redação não calibrou o alarme, e o protocolo não vira
   recomendação. O próximo braço a testar é o ordenador externo (o [protótipo](prototipo/)) para a
   lacuna.
2. **Parou na Etapa A pelo T3:** a reescrita calou a lacuna junto com o alarme. Mesmo próximo passo.
3. **H1, H2 e H3:** o protocolo v2 vira material da frente de temporalidade. As regras que o §3 do Strata
   não tem (3, lacuna; 4, intruso; 6, marcar o inferido) viram proposta com A/B próprio no harness do
   Strata. Nada entra no canônico por este teste.
4. **H1 e H2, sem H3:** o ganho pode ser de comprimento ou atenção, não de conteúdo. O protocolo não vira
   recomendação pelo conteúdo; registra-se.
5. **H2 sem H1:** registra-se em quais famílias o protocolo ajuda e em quais não.
6. Em qualquer caso, o ingênuo por família é o mapa de capacidade, e o negativo se registra.

## 9. Modelos, K, orçamento e custo

- **Painel:** os 8 modelos da v1 (6 fabricantes). Temperatura 0,3 (o GPT-6 ignora); raciocínio no padrão;
  teto de saída de 32 000; K = 3.
- **Rotas:** as da v1 (§9.3 dela), com `allow_fallbacks: false` e `require_parameters` (exceto o GPT-6). O
  GLM muda para `z-ai/fp8`. Grátis, na NVIDIA: `openai/gpt-oss-20b`, `google/gemma-4-31b-it`,
  `nvidia/nemotron-3-super-120b-a12b`.
- **Custo projetado** (custo por chamada da v1, ao preço por token de cada rota; projeção, não medida):
  - Etapa A: cerca de US$ 3,6;
  - Etapa B: cerca de US$ 5,2;
  - o GLM é cerca de 80% disso: na Z.ai, o token sai 2,3 vezes mais caro que na AtlasCloud;
  - saldo do OpenRouter em 2026-10-01: US$ 5,79.
- **Tetos:** Etapa A, US$ 4,50. A Etapa B só roda com saldo confirmado. Aos ~25% de cada modelo, projeta-se
  o gasto; se passar do teto, para e volta ao dono.
- **Contingência do GLM.** O dono decide antes de qualquer chamada da v2, só pelo custo:
  - (a) o GLM nas duas etapas, com recarga antes da B; ou
  - (b) o GLM fora do painel da v2 (7 modelos, 5 fabricantes).

  A escolha vale para as duas etapas e se registra no §12.

## 10. Ameaças à validade

- **As da v1 continuam:**
  - P × O diferem em mais que familiaridade;
  - granularidade;
  - pontuador por regex;
  - a tarefa diz "um mesmo episódio";
  - rótulos pela apresentação;
  - só português, com poucas fixtures por família;
  - revisores da mesma família de modelos (Claude);
  - 8 clusters, com dois pares do mesmo fabricante.
- **Sem controle novo.** Os exemplos da regra 3 ("uma gaveta já aberta") respondem ao alarme da v1 ("a
  porta aberta") nas mesmas fixtures. Um H2 que passe aqui não mostra que a regra generaliza para
  controles que a v1 não viu.
- **A régua dos controles é conservadora.** A regra 6 continua pedindo "marque como inferido", e marcar
  uma ação trivial como inferida conta como alarme (§6). O H2 mede o protocolo como está escrito, com essa
  tensão interna.
- **Fontes conhecidas de alarme nos controles**, com subtipo próprio na revisão:
  - o estado intermediário "encaixado e ainda não carregado", que nenhuma cena descreve;
  - o minuto entre o salto e a abertura do velame no T2c-P, lido como fim da cena;
  - o paralelo "Ainda no chão" × "Já no chão", que o portão da v1 julgou não ser defeito. Mudar os
    textos do paraquedas alteraria sete fixtures.
- **Placebo:**
  - casado em caracteres, não em tokens;
  - não roda nos controles, então o H2 não separa comprimento de conteúdo;
  - a checagem de manipulação só vê a nota "nenhuma", não outras formas de calar.
- **Mudanças além da regra 3** (regra 1, domínio O, vocabulário, teto, rota do GLM): dentro da v2, valem
  para todos os braços. Comparações entre v1 e v2 são só descritivas.
- **A nova regra diz o que não falta.** Isso empurra para o silêncio. O critério do T3 e a leitura do T3-P
  à parte medem esse custo.
- **Desenvolvimento:**
  - nenhuma saída da v2 informou o desenho;
  - a revisão adversarial (§11) fez o papel do solver cego da v1, sobre as fixtures, o protocolo e o
    placebo.
- **Etapas.** O H2 e o critério do T3 se decidem na A; o H1 e o H3 completos, só depois da B.
- **Preços** são ponto no tempo; a projeção usa os de 2026-10-01.

## 11. Revisão adversarial antes do congelamento (2026-10-01)

Um revisor independente (agente, sem rede, sem editar) aplicou o protocolo às fixtures como leitor
literal e procurou furos no desenho. O que ele achou e o que mudou:

- **Bloqueio:** o `lacuna_rx` não reconhecia a lacuna dita por estado, e o T3 decide a parada. Mudou:
  vocabulário ampliado na bateria v2, com testes; revisão completa do T3 na Etapa A.
- **Regra 3:**
  - a redação deixava a cena do salto "mostrar" o avião no ar por implicação;
  - o "começo" não tinha sentido verificável;
  - a regra 1 dizia "produz".

  Mudou: "pressupor não é descrever"; "o que a primeira cena pressupõe vinha do começo"; "descreve" na
  regra 1.
- **Régua dos controles:** a v1 não tinha livro de códigos, e a primeira versão deste registro mudava a
  régua sem dizer. Mudou: livro de códigos com a régua da v1 e "na dúvida, ALARME".
- **Placebo:**
  - pedia "linhas limpas", "exatamente como descrito" e "sem marcadores extras", o que empurra a nota a
    ficar vazia;
  - usava "antes", "até o fim" e "ao terminar".

  Mudou: o texto foi reescrito, e entrou a checagem de manipulação. O placebo do T3 passou para a Etapa
  A, selado, para o contraste rodar ao mesmo tempo.
- **Reprodutibilidade:**
  - o IC do T3 mudava com a ordem das comparações;
  - uma nova amostra da revisão sobrescreveria a chave da Etapa A.

  Mudou: semente por comparação; amostra só dos estratos novos; rótulo único; decisões da A congeladas.
- **Teto:** não era imposto nem gravado. Mudou: na bateria, no cabeçalho, e aviso de mistura na análise.
- **Portão, H2, T3-P e ramos de parada:** o texto ficou explícito (§5, §7).
- **Afirmações sobre a v1:** foram corrigidas no §1 e no §2.

Ficaram como ameaça declarada (§10): a falta de controle novo e as fontes conhecidas de alarme.

## 12. Desvios

(nenhum até aqui)
