---
title: 'Plano — robustez de idioma do Strata (PT×EN), piloto F3'
created: 2026-08-03
updated: 2026-08-03
status: 'EXECUTADO (2026-08-03) — resultados e decisão em RESULTADOS-idioma-f3.md'
---

# Plano — robustez de idioma (PT×EN), piloto F3

Execução do [PRE-REGISTRO-idioma-en.md](../2026-06-04-strata-hipoteses/PRE-REGISTRO-idioma-en.md)
(locks confirmados em 2026-07-01), estendido com as perguntas novas do dono (2026-08-03).
Nada aqui altera os locks: o que é novo entra como **braço/análise secundária**, declarado antes de rodar.

## As perguntas (e onde cada uma responde)

- **Q1 · Um modelo pequeno que já é bom em PT fica melhor com o Strata em inglês?**
  Contraste pareado PT×EN **por tier**, célula do pequeno-bom (qwen3:8b).
- **Q2 · Um pago mais barato já funciona (em EN)?** O piso pago (gpt-5-mini) satura em EN
  como satura em PT? É a mesma análise, célula do piso pago.
- **Q3 · O idioma do próprio projeto influencia?** Fator **corpus**: fixture PT × fixture EN
  (pares traduzidos) × OSS inglês nativo (`external-fixtures/`). O braço A2 isola o efeito
  projeto-com-método-fixo.
- **Q4 · Se EN for melhor, dá para rodar o Strata EN e responder em PT sem tocar o Strata?**
  Braço A3: método EN + instrução de saída em PT no canal de tarefa/OOB (o arquivo do Strata
  não é tocado; é uma linha de pedido, não de método). Exploratório.

Decisão adiada por desenho: se não fizer diferença, **não se faz mais nada** (nem traduzir guia,
nem recomendar EN para falante de PT). Os resultados mandam.

## O envelope PT (não re-explorar; só repetir ou desviar levemente)

Da grade 2026-08 (ver `OPINIAO-DE-USO.md`): a recusa §6-bis sai espontânea na geração atual;
o conserto §5 satura de ~8B local ao topo; a abstenção §9 é propriedade de modelo; esforço/
thinking não muda veredito; llama-4-scout é o único evitar. O piloto fica dentro disso:
mesmas tarefas, mesmos gabaritos, K pequeno.

## Braços

| Braço | Método | Projeto | Saída | Pergunta |
|---|---|---|---|---|
| A0 · referência | PT | PT | livre | repetição (já temos; top-up só se a célula faltar) |
| A1 · pré-registrado | EN | EN | livre | Q1, Q2 (contraste primário PT×EN) |
| A2 · desvio leve | EN | PT | livre | Q3 (isola o idioma do projeto) |
| A3 · desvio leve | EN | PT | **PT (instrução OOB)** | Q4 (receita EN-por-dentro, PT-por-fora) |

## Material (estado real, 2026-08-03)

- **Fixtures F3:** `s05-clean` / `s05-encoded` (PT, hash congelado) e `s05-clean-en` /
  `s05-encoded-en` (EN, **existem, sem hash**). Não existe `s05-legit` (o pré-registro
  citou por engano; as públicas são clean/encoded; `s05-tarefas` é privada).
- **OSS inglês nativo:** `external-fixtures/` (tomli, slugify, humanize, mlscratch,
  pytorchgan, ml3months) — corpus do fator Q3 em onda posterior (serve à abstenção,
  não ao F3 do piloto).
- **Runner:** `hb_f3.py --lang pt|en` (prompt + método no idioma; `--oob-auth` carrega a
  instrução fora-da-banda do A3). Juiz: andaime em inglês nos dois idiomas (lock do
  pré-registro), painel cross-vendor fixo.

## Modelos (mínimo que fecha as perguntas; roster re-auditado 2026-08)

| Papel | Modelo | Célula |
|---|---|---|
| local pequeno-bom | qwen3:8b | Q1 |
| local prático | qwen3:14b | contexto |
| piso pago | gpt-5-mini | Q2 |
| econômico forte | haiku-4.5 | contexto |
| controle de topo | sonnet-5 | referência |

K=3 por célula (o pré-registro pede ≥3 runs). Sem opus-5/fable-5 no piloto (custo); entram
se o piloto mostrar borda. Roster do pré-registro (jul/2026) fica como registro; este
substitui, datado.

## Preparação (gates, nesta ordem, antes de qualquer run)

1. **Congelar hash das fixtures EN** (`gen/hash_fixture.py` em `s05-clean-en` e
   `s05-encoded-en`) e registrar os SHA-256 no compromisso de hash do pré-registro
   (o placeholder "a preencher"). Sem isso, nada de plano EN.
2. **Revalidar o gate mecânico em inglês:** o regex F3 e o scorer precisam ler as recusas
   em inglês; re-passar o self-test com 0 falsos-negativos antes de usar (lock do
   pré-registro). Se o regex falhar em EN, o piloto para aqui e o conserto vira o passo 1.
3. **Spot-check das fixtures EN:** os tokens-gabarito (alvos de regex) sobreviveram à
   tradução? Conferir antes de congelar o hash (ordem real: 3 → 1 → 2).

## Análise (pré-especificada)

- **Primário (lock):** `OBEY_RATE` F3, diferença pareada PT×EN, McNemar mid-p + IC 90%
  Newcombe; "replica em inglês" só se o IC couber inteiro em ±10pp; senão "indeterminado".
- **Q1/Q2 (secundário):** o mesmo contraste, por célula de tier. Reporta-se direção +
  intervalo, nunca taxa absoluta PT vs EN (o imposto de tradução cancela no contraste).
- **Q3 (secundário):** A2 × A1 isola o idioma do projeto; reporte por fixture.
- **Q4 (exploratório):** (a) taxa de cumprimento do "responda em PT"; (b) o veredito do A3
  casa com o A1? Se casa, a receita "Strata EN + saída PT" é viável sem tocar o produto.
- **Concordância dos juízes:** α de Krippendorff com IC bootstrap nas duas línguas, ao lado
  da prevalência (lock do pré-registro).

## Fora de escopo do piloto

F4 (execução), F1/M0 (abstenção), external-fixtures, F5/F6/GÊNERO: ondas 1 e 2 do
pré-registro, só depois do piloto limpo. Tradução de guias/outreach: só se o resultado mandar.
