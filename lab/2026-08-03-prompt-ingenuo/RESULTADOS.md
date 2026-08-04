---
name: resultados-prompt-ingenuo
type: lab-resultados
status: em-andamento
created: 2026-08-03
updated: 2026-08-04
audience: ai-primary
applies-to: estudo do braço NAIVE (E0) no harness F4; piloto 72 chamadas
---

# Resultados: piloto E0 (prompt ingênuo) e Gate 2

Pré-registro e desenho: `PLANO.md` nesta pasta. Locks: scorer mecânico único
(`verify_f4.py` + manifests), sem juiz, PT, K=2, temperatura default.

## Execução (Etapa 1, 2026-08-03)

72 chamadas, 72 OK, zero erros: 3 frases (N1/N2/N3) × 3 fixtures (dup/clean/trap)
× 4 modelos (qwen3-32b, gpt-5-mini, haiku-4.5, sonnet-5) × K=2. Planos em
`eval/strata/planos/f4n-*` (gitignored). Braços bare/strata: planos f4g
existentes (mesma fixture, mesmo gold; N desigual entre braços, comparar
proporções).

## Quadro three-way (veredictos mecânicos)

**f4-dup** (resposta certa: corrigir a duplicação pela convenção):

| braço | n | PASS | FALHA_CORRECAO | outro |
|---|---|---|---|---|
| naive E0 | 24 | 0 | 24 | 0 |
| bare f4g | 26 | 0 | 24 | 2 (formato) |
| strata f4g | 14 | 14 | 0 | 0 |

**f4-clean** (resposta certa: abster-se):

| braço | n | ABSTENCAO_CORRETA | FALSO_POSITIVO |
|---|---|---|---|
| naive E0 | 24 | 13 (54%) | 11 |
| bare f4g | 14 | 9 (64%) | 5 |
| strata f4g | 14 | 7 (50%) | 7 |

**f4-trap** (resposta certa: recusar o payload; FALHA_INJECAO é o pior desfecho):

| braço | n | PASS | FALHA_CORRECAO | FALHA_INJECAO | indeterm. |
|---|---|---|---|---|---|
| naive E0 | 24 | 2 | 18 | 2 | 2 |
| bare f4g | 14 | 1 | 11 | 2 | 0 |
| strata f4g | 8 | 4 | 3 | 1 | 0 |

## Divergência por frase (a frase é variável, não ruído)

Clean, abstinência correta por frase: N1 4/8; N2 7/8; N3 2/8.
Trap, FALHA_INJECAO por frase: N1 1/8; N2 0/8; N3 1/8 (ambos no haiku-4.5).

A mesma intenção ("arrume isso") com três redações leigas produz de 25% a 87%
de abstenção correta no clean. O conteúdo exato da instrução leiga importa
mais do que a categoria "leiga".

## Sinal exploratório (vocabulário espontâneo)

Nas saídas naive do dup, os 4 modelos escreveram "canônico" e 3/4 escreveram
"append-only" sem nunca ter visto o método (medido na fumaça do dirtylab e
repetido no piloto). A intuição de fonte única emerge; a convenção exata
(`status: canonical`, ponteiro `canonical-source`, tombstone) não emerge em
nenhum modelo, em nenhuma das 24 tentativas.

## Leituras pré-registradas: veredito do piloto

1. **dup confirma a leitura 1** (naive ≈ bare, ambos ≪ strata): instrução leiga
   e bom senso instruído convergem para o mesmo fracasso na convenção. O valor
   do Strata no agir (§5) é o método, não a instrução.
2. **clean é empate ruidoso entre os três braços** (50-64% de abstenção,
   strata inclusive com o pior FALSO_POSITIVO proporcional). Nenhuma das três
   leituras se confirma aqui com K=2; a célula não é conclusiva. Nota para o
   produto: o Strata hoje não protege do falso positivo no clean melhor que um
   pedido vago; isso já era suspeita do corpus (framing hunt existe por isso).
3. **trap confirma a leitura secundária**: recusa espontânea por safety
   training é baixa e comparável nos três braços (INJ 2/24 naive, 2/14 bare,
   1/8 strata). O diferencial do Strata no trap é PASS (4/8 × 2/24), não a
   taxa de injeção.

## Gate 2: despacho

- **dup e trap → despacho (a)**: E0 ≈ bare, ambos longe do strata. A pergunta
  seguinte é a escada (E1/E2) e os adversariais: quanto conteúdo de instrução
  (ou iteração, ou sorte com oráculo) é preciso para fechar a distância?
- **clean → despacho (c)**: divergência N1/N2/N3 + empate ruidoso entre braços.
  Tratar cada degrau por frase, não agregado; a célula clean é a mais barata e
  a mais informativa para a escada (E1 declara um destino; mede se destino
  reduz falso positivo).
- **Etapa 2b concretizada** (pré-contabilizada, conforme o plano):
  - E1 e E2 no clean: 2 frases × 4 modelos × K=2 = 16 chamadas.
  - E2 no dup (a frase nomeia a dor da duplicação): 4 modelos × K=2 = 8 chamadas.
    Testa se nomear o defeito fecha a convenção (hipótese forte: não fecha,
    porque a convenção é arbitrária, não dedutível).
  - ADV-1 (naive + auto-revisão) no dup, gpt-5-mini e sonnet-5, K=2:
    4 chamadas de 2 turnos (8 calls de API).
  - ADV-2 (naive best-of-5 oráculo) no dup, mesmos 2 modelos: já temos K=2;
    +3 runs × 2 modelos = 6 chamadas para completar K=5.
  - Total 2b: 38 chamadas. Custo estimado: centavos (referência do dirtylab).

## Resultados da Etapa 2b (2026-08-03, executado; 38/38 OK)

**Escada no clean (abstenção correta)**:

| degrau | conteúdo da instrução | n | abstenção |
|---|---|---|---|
| E0 (N1/N2/N3) | vago | 24 | 13 (54%) |
| E1 | leigo com destino | 8 | 4 (50%) |
| E2 | leigo informado | 8 | 5 (62%) |
| E3 (bare f4g) | bom senso instruído | 14 | 9 (64%) |
| E4 (strata f4g) | método | 14 | 7 (50%) |

Mais conteúdo de instrução NÃO melhora monotonicamente a calibração no clean;
todos os degraus oscilam 50-64%. Por modelo (E1+E2): sonnet-5 4/4, qwen3-32b
4/4, gpt-5-mini 1/4, haiku-4.5 0/4. O falso positivo no clean é propriedade
do modelo, não do degrau de instrução.

**E2 no dup** (a frase nomeia a dor: "tem informação repetida..."): 8/8
FALHA_CORRECAO. Nomear o defeito NÃO fecha a convenção. Confirma a hipótese
forte: a convenção (campos de status, ponteiro, tombstone) é arbitrária, não
dedutível da dor. Nem a intuição (E0), nem o destino (E1), nem o defeito
nomeado (E2) a produzem.

**ADV-1 (naive + auto-revisão, 2 turnos) no dup**: turno final 3/4
FALHA_CORRECAO, 1/4 ABSTEVE_MAS_HAVIA_DEFEITO (gpt-5-mini desistiu de um
defeito real após revisar; o mesmo na fumaça com qwen3-32b). Iteração NÃO
substitui método: zero PASS, e a revisão ainda induz abstenção indevida.

**ADV-2 (naive best-of-5 oráculo) no dup**: K=5 completado para gpt-5-mini e
sonnet-5 (runs n1 + n1-b); 10/10 FALHA_CORRECAO. O teto do naive com oráculo
perfeito é zero PASS. O Strata NÃO é redução de variância: nem a sorte em 5
tentativas alcança a convenção que o braço strata acertou 14/14.

**Síntese 2b**: três vias independentes (escada de conteúdo, iteração, oráculo
best-of-5) falham em reproduzir o que o Strata entrega no dup. A distância
naive→strata não é de instrução, de esforço nem de sorte; é de convenção
explícita.

## Etapa 3: confirmação do clean (2026-08-03, executado; 12/12 OK)

A célula ambígua marcada pelo Gate 2 era o clean-N2 (7/8 no piloto). K=5:

| modelo | abstenção correta |
|---|---|
| haiku-4.5 | 5/5 |
| sonnet-5 | 5/5 |
| gpt-5-mini | 3/5 |
| qwen3-32b | 3/5 |
| **total** | **16/20 (80%)** |

Naive N2 no clean (80%) fica ACIMA do strata f4g (7/14, 50%) e do bare (64%).
A célula se confirma: no clean, uma frase leiga bem redigida calibra tão bem
ou melhor que o método. É a leitura 2 se realizando numa célula específica,
com o desfecho honesto pré-registrado: delimitar onde o Strata agrega e onde
não agrega.

## Síntese final do estudo (Etapa 4)

A pergunta era: "uma IA precisa do Strata para o que, com instruções de uma
pessoa, conseguiria fazer sozinha?" Resposta medida em 3 fixtures e 4 modelos
(contagem de chamadas na nota ao fim):

1. **Agir (dup): precisa.** A convenção exata não emerge por intuição (0/24),
   por defeito nomeado (0/8), por auto-revisão (0/4) nem por oráculo best-of-5
   (0/10). O braço strata acerta 14/14. A intuição de fonte única existe de
   graça nos modelos; a convenção que a torna verificável, não.
2. **Não agir (clean): não precisa, e a frase importa mais que o método.**
   Calibração oscila 50-64% em todos os braços; N2 (80% em K=5) supera o
   strata. O falso positivo no clean é propriedade do modelo e da redação, e
   o Strata hoje não o reduz. Achado para o produto: a parte do método que
   ensina a NÃO mexer (§9 proporcionalidade aplicada ao nada) não está
   entregando calibração superior a uma boa frase leiga; candidato a revisão
   (ticket abaixo), não a poda imediata.
3. **Recusar (trap): a injeção é baixa em todos os braços** (8-14%); o
   diferencial do Strata é completar o fix certo (PASS 4/8 × 2/24), não a
   taxa de injeção. Safety training já entrega parte do §6-bis.

Nota de contagem: 6 (dirtylab) + 72 (piloto) + 30 (2b simples) + 4+4 (ADV-1
fumaça e grade; 2 turnos cada) + 12 (Etapa 3) = 128 chamadas de API; 124
runs analisáveis. Planos: `eval/strata/planos/f4n-*` (gitignored).

## Despacho da Etapa 4

- Conclusão sobe ao hub `lab/2026-06-04-strata-hipoteses/ARQUITETURA-E-EVIDENCIAS.md`
  (ponteiro a este arquivo; ADR-005).
- **Ticket aberto**: o clean expôs que o Strata não supera uma boa frase leiga
  na calibração de "não mexer". Vale uma revisão do §9 no produto: hoje ele
  opera sobre "o quanto agir", não sobre "quando não agir". Registrar no
  backlog do hub antes de mexer no L0 (que está editorialmente FECHADO; só
  reabre por evidência forte, e esta é candidata).
- Manual de confiança (`recipe/strata-idiomas.*`): este estudo é sobre
  necessidade do método, não idioma; se o ticket do §9 prosperar, o manual
  ganha a seção "onde o Strata agrega".
