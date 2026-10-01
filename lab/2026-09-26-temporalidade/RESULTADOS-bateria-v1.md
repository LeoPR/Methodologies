---
title: 'Resultados: bateria de temporalidade v1'
created: 2026-09-30
updated: 2026-10-01
status: 'Executado. H1 vale no modo principal (4 de 4 famílias); a queda na sensibilidade (2 de 4) era o teto de 8000 tokens: com orçamento adequado, 4 de 4. H2 violada nos dois modos. Regra 1 do §6: o protocolo, como está, não vira recomendação; texto vai para uma v2.'
tags: [temporalidade, bateria, resultados, capacidade]
---

# Resultados: bateria de temporalidade v1

Pré-registro: [PREREG-bateria-v1.md](PREREG-bateria-v1.md), com os desvios datados no §9.
Instrumento: `eval/temporalidade/`.

Rodada de 2026-09-30:

- 8 modelos de 6 fabricantes (Google e OpenAI com dois cada);
- 156 saídas por modelo (13 fixtures × 2 apresentações × 2 braços × K = 3), 1248 no total;
- zero erro de chamada;
- cada modelo num provedor e numa rota só.

As saídas brutas ficam em `eval/temporalidade/planos/tb-v1/` (fora do git).

## Resposta curta

Nesta bateria (8 modelos, português, 13 fixtures sintéticas):

- **Sem ajuda, a ordem sai certa, mas o que falta quase nunca é notado.**
  - A ordem sai certa em 549 de 593 saídas (0,93).
  - O passo que falta é notado em 1 de 92 saídas.
  - A cena intrusa é apontada em 0,29.
  - Entre cenas sem dependência, 0,53 das saídas forçam uma ordem.
- **O protocolo da ontologia aumenta o acerto da nota.** No modo principal (pré-registrado):

  | família | sem protocolo | com protocolo |
  |---|---|---|
  | T3, lacuna | 0,01 | 0,48 |
  | T4, intruso | 0,29 | 0,99 |
  | T2, horário errado | 0,72 | 0,93 |
  | T5, ambiguidade | 0,47 | 0,82 |

  O H1 vale nas 4 famílias. Contando as saídas cortadas como falha, só T3 e T4 cumpriam (2 de 4), mas
  os cortes eram do teto de tokens: refeito com orçamento adequado, o H1 vale nas 4 (seção abaixo).
- **O mesmo protocolo faz avisar à toa nos controles.** O alarme falso sobe de 0,02 para 0,21, e o
  H2 é violado nos dois modos.
- **Decisão (regra 1 do §6):** a decisão não depende do modo, porque o H2 é violado nos dois. O
  protocolo, como está escrito, não vira recomendação. O texto se revisa numa v2, com novo
  pré-registro. Nada muda no Strata.

## Saídas sem resposta (SEM-LINHA)

O §4 manda ler isto antes do H1.

- As 116 saídas sem resposta são todas cortadas por tamanho (`stop=length`); não há erro de
  formato.
- Elas se dividem em 31 no braço ingênuo e 85 no protocolo.
- Nenhuma resposta de modelo que terminou saiu do canal de raciocínio. As 107 com `ft=1` estão
  entre as cortadas.
- No modo principal, os braços são comparados com denominadores diferentes. Por isso a
  sensibilidade, que conta as cortadas como falha, vem ao lado.

| modelo | cortadas, ingênuo | cortadas, protocolo |
|---|---|---|
| glm-5.3 | 16 | 44 |
| deepseek-v4.1-flash | 10 | 35 |
| nemotron-3-super | 3 | 3 |
| muse-glimmer-30b | 1 | 2 |
| gpt-oss-20b | 1 | 1 |
| gemini, gemma, luna | 0 | 0 |

Com o protocolo, GLM e deepseek raciocinam mais e batem no teto de 8000 tokens. A mediana de tokens
de raciocínio, ingênuo × protocolo, é 1710 × 8000 no GLM e 2970 × 6426 no deepseek.

## Capacidade sem ajuda (braço ingênuo)

É o mapa de capacidade da v1 (regra 4 do §6). Modo principal; acerto da nota e consistência (as duas
apresentações × K com a mesma classe) em colunas separadas (ADR-006).

| família | domínio | acerto da nota | ordem certa | consistência |
|---|---|---|---|---|
| T1 ordem (controle) | paraquedas | 48/48 (1,00) | 42/48 (0,88) | 8/8 |
| | orbe | 43/46 (0,93) | 43/46 (0,93) | 7/8 |
| T2 horário errado | paraquedas | 36/48 (0,75) | 44/48 (0,92) | 6/8 |
| | orbe | 28/41 (0,68) | 34/41 (0,83) | 5/8 |
| T2c horário coerente (controle) | paraquedas | 48/48 (1,00) | 48/48 (1,00) | 8/8 |
| | orbe | 48/48 (1,00) | 48/48 (1,00) | 8/8 |
| T3 lacuna | paraquedas | 0/48 (0,00) | 42/48 (0,88) | 8/8 |
| | orbe | 1/44 (0,02) | 37/44 (0,84) | 7/8 |
| T4 intruso | paraquedas | 19/45 (0,42) | 42/45 (0,93) | 5/8 |
| | orbe | 6/40 (0,15) | 40/40 (1,00) | 4/8 |
| T5 ambiguidade | paraquedas | 22/48 (0,46) | 46/48 (0,96) | 4/8 |
| | orbe | 20/41 (0,49) | 40/41 (0,98) | 7/8 |
| T6 fora do roteiro | paraquedas | 43/48 (0,90) | 43/48 (0,90) | 6/8 |

Leitura:

- **Ordem.** Sem ajuda, a ordem sai certa entre 0,83 e 1,00 por família e domínio, inclusive no
  domínio inventado e fora do roteiro (T6). Esse critério não pune ordem imposta a cenas sem
  dependência; isso se mede no T5.
- **Lacuna.** A lacuna é apontada em 1 de 92 saídas (uma do gemini, no orbe). Nenhuma saída do
  paraquedas cita a decolagem. A ordem das cenas restantes sai certa em 0,84–0,88, o que é
  compatível com preencher o passo sem dizer.
- **Intruso.** O intruso entra na sequência em 60 de 85 saídas (0,71): 0,85 no orbe e 0,58 no
  paraquedas.
  - Isso é compatível com o enquadramento da tarefa ("um mesmo episódio", §8), mas nenhum braço
    retira o enquadramento.
  - Os intrusos também diferem de conteúdo entre os domínios.
- **Ambiguidade.** No T5, 47 de 89 saídas (0,53) forçam uma ordem entre as cenas sem dependência.

## O protocolo: H1 e H2

H1, protocolo − ingênuo no acerto da nota, com IC 95% por bootstrap de modelos:

| família | modo principal | sensibilidade (cortada = falha) |
|---|---|---|
| T2 horário errado | 0,72 → 0,93, +0,21 [+0,03, +0,42], cumpre | 0,67 → 0,86, +0,20 [+0,00, +0,41], não cumpre |
| T3 lacuna | 0,01 → 0,48, +0,47 [+0,31, +0,65], cumpre | 0,01 → 0,43, +0,42 [+0,29, +0,54], cumpre |
| T4 intruso | 0,29 → 0,99, +0,69 [+0,49, +0,87], cumpre | 0,26 → 0,88, +0,61 [+0,42, +0,78], cumpre |
| T5 ambiguidade | 0,47 → 0,82, +0,35 [+0,10, +0,57], cumpre | 0,44 → 0,61, +0,18 [−0,20, +0,53], não cumpre |
| **H1** | **vale (4 de 4)** | **não vale (2 de 4)** |

Nenhuma família bateu a regra de teto (ingênuo ≥ 0,90).

H2, controles T1 + T2c, não inferioridade com margem de 0,10:

| métrica | modo principal | sensibilidade |
|---|---|---|
| alarme falso | 0,02 → 0,21, +0,19 [+0,07, +0,31], viola | 0,03 → 0,32, +0,30 [+0,14, +0,45], viola |
| ordem certa | 0,95 → 0,96, +0,005 [−0,03, +0,04], dentro da margem | 0,94 → 0,82, −0,12 [−0,30, +0,02], viola |
| **H2** | **violada** | **violada** |

O critério é a diferença pontual contra a margem. Pelo limite do IC, a conclusão é a mesma.

Leitura:

- **T3 e T4 cumprem nos dois modos.**
- **T2 e T5 caem na sensibilidade por motivos diferentes.**
  - No T5, a queda vem dos cortes do protocolo (24 contra 7 no ingênuo), quase todos de GLM e
    deepseek.
  - No T2, os cortes são iguais nos dois braços (7 × 7): a diferença fica em +0,20, e o limite
    inferior do IC cai a 0.
- **Leitura descritiva, fora do pré-registro, sem GLM e deepseek:**
  - as 4 famílias cumprem nos dois modos (sensibilidade: T2 +0,28 [+0,06, +0,50], T5 +0,46
    [+0,26, +0,67]);
  - o alarme falso ainda sobe +0,20 [+0,07, +0,34].

  A violação do H2 não vem dos cortes.
- **Consistência.** No protocolo, a consistência nos controles cai de 0,88–1,00 para 0,29–0,50.

## Por que o H2 falhou (diagnóstico para a v2)

A revisão registrou o que cada alarme falso aponta (subtipo pelo revisor 1; os dois revisores
divergem em 2 dos 34 alarmes do protocolo):

| braço | transição trivial | regra mal lida | outro |
|---|---|---|---|
| ingênuo | 0 | 0 | 3 |
| protocolo | 24 (26 pelo revisor 2) | 5 | 5 (3 pelo revisor 2) |

- **Transição trivial** é apontar como passo faltante algo como "a abertura da porta do avião", ou
  "o ato de encaixar" quando a cena já mostra o orbe encaixado.
- 24 dos 34 alarmes do protocolo (0,71) são desse tipo. É o que a regra 3 do protocolo ("estado
  pressuposto, não mostrado e que não vinha do começo") pede ao pé da letra.
- A ameaça "Granularidade" do §8 se confirmou.
- **Hipótese para a v2 (não testada):** falta um passo quando o estado que uma cena pressupõe é
  incompatível com o último estado mostrado.
  - Nos exemplos citados, essa regra separaria a decolagem (o avião no chão, depois em voo) da
    porta (que nenhuma cena mostrou fechada).
  - Projeção, não resultado: sem as 24 transições triviais, o alarme do protocolo seria 10/164
    (0,06).
- **Teto de tokens.** Medir um raciocínio cortado mede o teto, não o modelo. Na v2, o teto de
  tokens ou o nível de raciocínio precisa ser decidido antes, no pré-registro.

## Por modelo (descritivo)

Modo principal. Acerto da nota nas famílias T2–T5 e alarme falso nos controles, em k/n (saídas
válidas):

| modelo | nota, ingênuo | nota, protocolo | alarme, ingênuo | alarme, protocolo |
|---|---|---|---|---|
| gpt-6-luna | 16/48 | 41/48 | 3/24 | 1/24 |
| gemini-3.5-flash-lite | 17/48 | 40/48 | 0/24 | 7/24 |
| gemma-4-31b-it | 18/48 | 37/48 | 0/24 | 3/24 |
| muse-glimmer-30b | 29/47 | 42/47 | 0/24 | 11/23 |
| nemotron-3-super | 8/46 | 38/46 | 0/23 | 3/23 |
| gpt-oss-20b | 2/47 | 24/47 | 0/24 | 6/24 |
| deepseek-v4.1-flash | 20/38 | 22/24 | 0/24 | 2/13 |
| glm-5.3 | 22/33 | 23/23 | 0/23 | 1/9 |

- **No modo principal, os oito melhoram a nota.** Contando as cortadas como falha, deepseek
  (0,42 → 0,46) e GLM (0,46 → 0,48) ficam quase iguais.
- **O alarme falso sobe em sete.** O luna é o único que avisa menos com o protocolo.
- **T3 com protocolo:**
  - **orbe:** gemini e luna notam a lacuna em 6 de 6;
  - **paraquedas:** GLM (5/5) e deepseek (4/6) passam da metade, e gemma e gpt-oss ficam em 0/6.

## Descritivo

- **Paraquedas × orbe.** Com o protocolo, a lacuna é notada em 0,68 no orbe e em 0,32 no
  paraquedas.
  - Há uma fixture por domínio, e os domínios diferem em mais que familiaridade (§8).
  - A diferença não se atribui só ao conhecimento de mundo.
- **Apresentação.** As diferenças entre as duas ordens de apresentação não têm direção constante
  (por exemplo, T3 paraquedas com protocolo: 0,42 × 0,22; T2 orbe ingênuo: 0,75 × 0,62).
- **Fora do roteiro (T6).** Os dois braços seguem a ordem observada: 0,90 × 0,89.

## Instrumento e revisão

- **Revisão cega (§4 e §9.8).** Foram revisadas 404 saídas: a amostra de 261 mais a ampliação de
  143.
  - A ampliação foi disparada pela concordância na amostra, abaixo de 0,90: T1 0,79, T2c 0,88,
    T4 0,88.
  - Nessas três famílias, todas as notas não triviais foram revisadas (T1 45, T2c 34, T4 158). A
    análise usa a classe revisada nelas.
  - Os dois revisores concordam em 0,99 na classe e em 1,00 na ordem. Adjudiquei 4 itens.
- **Pontuador × revisão, nas notas não triviais:** 0,87 no total (kappa 0,84).

  | família | concordância | kappa |
  |---|---|---|
  | T4 | 0,78 | 0,41 |
  | T1 | 0,80 | 0,59 |
  | T2c | 0,91 | 0,82 |
  | T2 | 0,95 | 0,00 |
  | T3, T5 e T6 | 1,00 | 1,00 |

  - No T2, o kappa é 0 com 0,95 de concordância, porque quase tudo cai numa classe só.
  - **Os erros do pontuador têm direção.**
    - Nos controles, ele deixa passar alarmes falsos: 9 no T1 e 3 no T2c.
    - No T4, 30 dos 35 erros creditam como apontado o intruso deixado num grupo com "sem relação
      temporal".
    - No T2, os 2 erros são conservadores.
- **Custo.**
  - Etapa grátis (NVIDIA): US$ 0.
  - Etapa paga (OpenRouter, rota fixa por modelo): US$ 2,74.
  - Testes de fumaça: US$ 0,13, dos quais US$ 0,12 foram um erro de operação (13 chamadas do GLM a
    mais).

## Ameaças à validade

- **Revisores.** Os dois revisores e o adjudicador são da mesma família de modelos (Claude).
- **Fabricantes.** São 8 clusters do bootstrap, com dois pares do mesmo fabricante (Google, OpenAI).
  O IC pode sair mais estreito do que seria com 8 fabricantes.
- **Cortes por tamanho.** Dependem do braço em dois modelos. Por isso as duas leituras estão lado a
  lado.
- **Comprimento.** O braço protocolo é mais longo, e não houve braço-placebo. Parte do efeito pode
  ser atenção, e não conteúdo.
- **Desenvolvimento.** As fixtures e o pontuador foram ajustados com dois modelos grátis do próprio
  painel (§8).
- **Critérios de fronteira.** T3 e T4 dependem dos critérios de fronteira da revisão (§9.5).
- **Redação do domínio O.** As leituras de redação do §9.1 ficam para a v2 e podem pesar nos 5
  alarmes de regra mal lida.
- **Rótulos.** Seguem a ordem de apresentação (§8).
- **Precisão servida.** A NVIDIA não declara a precisão que serve, e no OpenRouter a quantização é
  garantida pela rota, não observada (§9.3).
- **Amostra.** Só português, duas apresentações por fixture e uma ou duas fixtures por família.

## Leitura complementar com orçamento adequado

Os 116 cortes vinham do teto de 8000 tokens, uma configuração nossa, não dos modelos. GLM e deepseek
foram refeitos inteiros com teto de 32 000 (`planos/tb-v1-32k/`, mesma rota; pontuador sem revisão
manual nessas saídas).

- **deepseek:** nenhum corte (eram 45).
- **GLM:** 20 respostas ainda sem conclusão. O JSON bruto mostra o texto todo no campo de raciocínio,
  cortado no meio da linha final. Na rota oficial do fabricante (Z.ai), a mesma fixture conclui em
  8 de 8 chamadas: o laço é da implantação da AtlasCloud, não do modelo.
- **Por dedução, sem nova rodada:** com as 20 do GLM fora, contadas como falha ou como acerto, as
  conclusões são as mesmas:

  | leitura | T2 | T3 | T4 | T5 | alarme falso |
  |---|---|---|---|---|---|
  | GLM cortes = falha | +0,23 [+0,06, +0,42] | +0,51 [+0,32, +0,70] | +0,55 [+0,31, +0,75] | +0,34 [+0,15, +0,56] | +0,21 [+0,10, +0,32] |

  H1 vale nas 4 famílias; H2 continua violado. A decisão (regra 1) não muda.

## O que fica

- **Para a pergunta de fundo (por que as IAs erram com o tempo), nesta bateria:**
  - sem ajuda, a ordem por dependência sai certa em 0,93;
  - notar o que falta sai em 1 de 92 sem ajuda e em 0,48 com o protocolo (0,43 contando as
    cortadas).
- **Próximo passo, se o dono quiser (uma coisa por vez):**
  - **v2 do protocolo:** regra 3 por incompatibilidade de estado, teto de tokens e nível de
    raciocínio decididos antes, novo pré-registro;
  - **depois, se a v2 mantiver a lacuna do paraquedas baixa com o H2 dentro da margem:** o braço
    com ordenador externo para essa lacuna.
