---
name: resultados-verificacao-s9
type: lab-resultados
status: fechado
created: 2026-08-06
updated: 2026-09-26
audience: ai-primary
applies-to: verificacao A/B do paragrafo §9 "quando nao agir" (PROPOSTA-S9 aplicada em v1.2.2)
---

# Verificação do §9 "quando não agir": A/B v1.2.1 × v1.2.2

A [PROPOSTA-S9](PROPOSTA-S9.md) foi aprovada e aplicada ao par canônico (v1.2.2). Este é o
re-teste dirigido que a própria proposta estipulou como portão. **Resultado: sem efeito medido.**

## Desenho

Único fator manipulado: o **texto do método**. Mesmas fixtures, mesmos modelos, mesmas seeds,
mesmo runner, mesmo scorer.

- **Braço A** = v1.2.1 (sem o parágrafo), `method_sha=68af3a9f6bc1`
- **Braço B** = v1.2.2 (com o parágrafo + a instância de era), `method_sha=4ef1fd5ea98e`
- Fixtures onde o gabarito é ABSTER-SE: `f4-clean` (`fixture_sha=dbd10920150a`) e
  `f4-clean-v2` (`fixture_sha=b3b48a3fe307`)
- 3 modelos de tier econômico/médio, K=3, `hb_f4.py` braço STRATA, framing `audit`
- Pontuação: `verify_f4.py` (scorer mecânico; GATE GOLD 16/16 rodado antes)

`f4-clean-v2` nasceu neste teste: é a sucessora sem vazamento de `f4-clean`, cujo README
afirmava *"Nao ha fontes concorrentes"* sendo o gabarito ABSTER-SE. Config e histórico são
byte-idênticos; só o README mudou para descrever sem afirmar a conclusão.

## Resultado

| fixture | modelo | v1.2.1 | v1.2.2 |
|---|---|---|---|
| `f4-clean` | gpt-oss-120b | 3/3 | 3/3 |
| `f4-clean` | mistral-nemotron | 0/3 (falso-positivo 3/3) | 0/3 (falso-positivo 3/3) |
| `f4-clean` | nemotron-49b | 0/3 (indeterminado 3/3) | 0/3 (indeterminado 3/3) |
| `f4-clean-v2` | gpt-oss-120b | 2/3 | 1/2 |
| `f4-clean-v2` | mistral-nemotron | 0/3 (falso-positivo 3/3) | 0/3 (falso-positivo 3/3) |
| `f4-clean-v2` | nemotron-49b | 0/3 (indeterminado 3/3) | 0/3 (indeterminado 3/3) |

Totais: `f4-clean` **33% → 33%**; `f4-clean-v2` **22% → 12%**.

**Nenhuma célula melhorou.** A hipótese registrada na proposta era subir de ~50% para o regime
da frase leiga (~80%); ela falhou.

## Dois achados laterais, ambos úteis

**O vazamento da fixture era mensurável.** O gpt-oss-120b faz 3/3 no `f4-clean` (que entrega a
resposta em prosa) e cai para 2/3 na `f4-clean-v2`, byte-idêntica exceto por essa frase. Parte do
número histórico de abstenção era leitura da resposta, não calibração. Isso recalibra para baixo
qualquer série que use `f4-clean` como base.

**Abstenção continua sendo propriedade de modelo.** Dois dos três nunca abstiveram em nenhuma
versão: mistral-nemotron deu falso-positivo em 12/12 e nemotron-49b não produziu formato
pontuável em 12/12. Consistente com a assinatura já registrada no corpus.

## Limites

K=3 é triagem, não rodada inferencial. A célula `v122 / f4-clean-v2 / gpt-oss-120b` ficou com 2
runs (Cerebras devolveu 429 repetido; Groq recusa o método completo com 413), então aquele
denominador é menor. Isso não muda a leitura: não houve melhora em **nenhuma** célula, e um efeito
escondido por K pequeno teria de aparecer ao menos como direção.

A v1.2.2 mudou duas coisas juntas (o parágrafo e a instância de era). Como não houve efeito,
isolar qual delas agiu perdeu o sentido; se um teste futuro achar efeito, o terceiro braço volta
a ser necessário.

Três modelos, tier econômico/médio, fixture sintética, PT. Nada aqui fala sobre modelo de topo,
sobre projeto real, nem sobre leitor humano.

## Decisão

O parágrafo **fica** no produto (decisão do dono, 2026-08-06): é norma honesta e útil para leitor
humano, e o L0 é independente de tecnologia — uma norma correta não precisa mover comportamento de
LLM para ser correta. O que cai é a expectativa de que ela *comprasse* calibração de não-agir. O
carimbo no §9 passou de `[NÃO VERIFICADO]` para testado-sem-efeito, apontando para este registro.

## Instrumento destravado por este teste

Três consertos que eram prerequisito e agora estão no harness:
`hb_f4.py --strata` (A/B de versão do método sem trocar arquivo no disco); `method_sha` no header
do plano, derivado do texto injetado e não do caminho (§3 — antes duas rodadas eram
indistinguíveis no traço); e provedores de tier gratuito no `hb_f4.py`, que só o `hb_f3.py` tinha.

## Errata (2026-09-26, acrescentada; o texto acima não foi editado)

Achada pela auditoria declarado × feito de
[`lab/2026-09-26-revisao-superficie/`](../2026-09-26-revisao-superficie/AUDITORIA-sync.md)
(achados C56, C63/C106, C49/C103) e reconferida à mão.

1. **O braço B não é a v1.2.2 commitada.** Os planos `s9ab-v122-*` trazem
   `method_sha=4ef1fd5ea98e`. A v1.2.2 que entrou no git (`3e92195`) tem `6c126752d37a` no PT e
   `d01111ae16df` no EN. O braço A confere com a v1.2.1 PT (`68af3a9f6bc1`). O texto do braço B
   não foi retido (os planos são gitignored e guardam só o hash). Pelo que este registro diz
   acima, o braço B tinha o parágrafo e a instância de era ainda com o carimbo anterior ao
   resultado; o commit trocou essa nota pelo resultado. Que o **parágrafo da norma** é o mesmo
   nos dois textos é afirmação do registro, não verificação por hash.
2. **O A/B rodou só em PT.** Os planos têm `lang=pt`. O portão da PROPOSTA-S9 pedia PT+EN, e a
   expressão inglesa não foi testada. Pela regra do projeto, as duas expressões fazem o mesmo
   trabalho intelectual, então o achado vale para o método. O desvio do portão pré-registrado
   fica declarado aqui.
3. **O parêntese do canônico sobre a comparação com a frase leiga descrevia só um braço.**
   "4 models, K=5" vale para o naive N2. O braço Strata veio da grade f4g (7 modelos, K=2), com 2
   modelos em comum, e os dois braços rodaram na `f4-clean`, que vazava a resposta. A comparação
   não é pareada. A v1.2.3 tirou esses números do produto e aponta para esta pasta.

**Lição de instrumento (não implementada aqui):** o `method_sha` prova que dois textos diferem,
mas não permite recuperar o texto. Para o A/B ser reauditável, o runner deveria reter o texto
injetado, ou o commit e o caminho de onde ele saiu, ao lado do hash.

