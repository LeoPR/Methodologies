---
title: 'Avaliação: os testes sintéticos cobrem a ontologia da temporalidade?'
created: 2026-09-28
updated: 2026-09-28
status: 'Avaliação (leitura das fixtures, manifestos, runners e resultados). Nenhum teste alterado ou rodado.'
tags: [temporalidade, eval, fixtures, cobertura, f5, f6]
---

# Os testes sintéticos cobrem a ontologia da temporalidade?

**Resposta curta: não.** Os testes atuais cobrem a camada rasa (fato perecível e busca na web) e uma
fatia estreita da ordem: situar a **versão atual × a superada de um mesmo artefato** quando o
conteúdo deixa isso legível. O núcleo da [ONTOLOGIA](ONTOLOGIA.md) não tem teste nenhum: ordem por
dependência de estado, horário contra dependência, lacuna não avisada, passo intruso, várias ordens
válidas e passo inferido marcado como tal.

## O que existe hoje (eval/strata)

| fixture | o que mede | como pontua | última rodada |
|---|---|---|---|
| `f6-tempo` | qual de dois protocolos está em vigor, por casamento semântico com os resultados, contra nome e README enganosos | leitura (sem pontuador mecânico) | jun/2026, 2 modelos, 8/8 |
| `f6-longitudinal` | decisão em vigor após reversão (D1→D2→D3) e o documento desatualizado | leitura | jun/2026, 4/4 |
| `f6-ambiguo` | abster quando a escolha está **declarada** pendente | leitura | jun/2026, 4/4 |
| `f6-ruidoso` | separar histórico/resolvido de pendência atual (falha R8) | leitura | jun/2026; README entrega parte da resposta |
| `f5-recente` | três afirmações cuja verdade mudou em 2024–2026; com e sem web | mecânico (`score_f5`, gate GOLD) | set/2026 (banco) |
| `f5-verif` | verificar fonte primária (§6) | mecânico | set/2026 |
| `s04`, `f4-dup` | histórico datado com "supersede" não é conflito | juiz / `verify_f4` | set/2026 |

Fontes: `eval/strata/cenarios/README.md`, os `f6-*-manifest.json`, `f5-recente-manifest.json`,
`runners/hb_f6.py`, `lab/2026-06-04-strata-hipoteses/RESULTADOS-f6-temporal-sem-marcadores.md`.

## Cobertura contra a ontologia

| regra ou capacidade (ONTOLOGIA §4) | coberta? | onde / por que não |
|---|---|---|
| 1. ordem pela **dependência de estado** (paraquedas) | **não** | F6 ordena *versões de um artefato* (supersessão), não uma cadeia de eventos em que um habilita o outro |
| 2. **horário contra a cadeia** | **não** | F6 *remove* marcadores; nenhum fixture traz marcador **errado**. O nome enganoso do `f6-tempo` é o análogo mais próximo |
| 3. prior do script contra evidência (ordem real fora do canônico) | **não** | nenhum caso em que o observado contraria o esperado |
| 4. **lacuna não avisada** → pergunta/busca | **não** | `f6-ambiguo` avisa que falta ("pendente"); nada tira um passo em silêncio |
| 5. **passo intruso** | **não** | `f6-ruidoso` tem ruído *histórico*, que é outro erro (tempo, não pertinência) |
| 6. passo **observado × inferido** | **não** | nenhum pontuador pede ou confere essa marca |
| 7. "agora" local; fato mudou depois do corte | **parcial** | `f5-recente` (3 afirmações); não controla se a data de hoje é dada no prompt; não tem o caso "fonte do dia do lançamento" |
| 8. status calculado (série A × B) | **parcial** | `f6-tempo`, `f6-longitudinal`, `f6-ruidoso` (atual × superado de artefatos) |
| 9. duas datas (valeu × registrado) | **não** | `f6-ruidoso` tem "CORRIGIDO em ..." mas não separa as duas datas |
| 10. **várias ordens válidas** (incomparáveis; ambiguidade) | **não** | todo gabarito tem resposta única; nenhum mede se o modelo inventa ordem entre incomparáveis |
| 11. estados permitem, não causam | não | fora do alcance de fixture simples; baixa prioridade |
| 12. preparação sem culminação ("estava abrindo" ⇏ "abriu") | **não** | nenhum caso de falha no meio do núcleo |
| coerência global com N > 4 eventos | **não** | todos os F6 têm 2 a 4 arquivos |
| efeito da ordem de apresentação | **não** | nenhuma permutação controlada da entrada |
| controle por domínio ofuscado (sem script familiar) | **não** | todos os domínios são familiares; não separa raciocínio de memória |

## Problemas de método nos testes que existem

- **Pontuação por leitura no F6.** Não há gabarito mecânico: não escala para o banco de modelos nem
  aguenta K alto. O F5 e o F4 já têm pontuador com gate GOLD.
- **Teto.** O `f6-tempo` saiu 8/8 com modelos de junho; o próprio registro diz que é sobre-determinado
  (quatro sinais convergentes). Não separa os modelos de hoje.
- **Vazamento.** O `f6-ruidoso` entrega parte da resposta no README (já registrado, sem sucessora).
- **Defasagem.** O F6 rodou em junho, com dois modelos e K=2, e ficou fora do banco de setembro.
- **Alcance da conclusão de junho.** "O ponto cego temporal se desconfirma em parte" vale para o que
  o F6 mede: ordem *local* e *legível*. É o que a literatura também acha (MAPA-4: ordem local sim,
  global e por estado não). A conclusão continua certa no seu escopo, mas não se estende ao núcleo.

## Dois instrumentos diferentes, não um

- O **F6 é regressão do Strata**: um modelo, com o método, situa artefatos de um projeto no tempo
  ao auditar? Continua útil e deve ficar (com sucessora do `f6-ruidoso` e pontuador mecânico).
- A **temporalidade** pede um instrumento de **capacidade**: o modelo ordena por dependência, nota a
  lacuna, desconfia do horário? Isso vale com e sem o Strata, e com e sem um ordenador externo.
  Pela regra do projeto, vai para `eval/` como família nova, reusando runner e estatística.

## Esboço do que uma bateria mínima nova precisaria (para decidir, não feito)

Cada item com gabarito mecânico e sem atalho (a fixture não afirma o veredito):

| família | caso | gabarito mecânico |
|---|---|---|
| T1 ordem por estado | N cenas embaralhadas, sem horário | conjunto de pares ordenados e de pares incomparáveis |
| T2 horário errado | igual, com um horário trocado | a ordem de T1 + o par em conflito apontado |
| T3 lacuna silenciosa | um passo removido sem aviso | o fluente sem produtor; se pediu/buscou antes de concluir |
| T4 intruso | um passo sem ligação | o id do intruso |
| T5 ambiguidade | cenas com pares incomparáveis | não inventar ordem entre eles |
| T6 fora do script | ordem real incomum (acidente, falha no meio do núcleo) | relata o observado e marca o conflito com o esperado |
| T7 "agora" | fato de status com data de hoje dada × não dada; fonte do dia do lançamento | pede verificação ou data antes de afirmar status |

Controles: domínio familiar × ofuscado (nomes trocados); permutações da ordem de apresentação;
N pequeno × maior. Braços: ingênuo × com protocolo da ontologia × com ordenador externo (o
[protótipo](prototipo/)). Reporte com acurácia e precisão em colunas separadas, k e K (ADR-006).
