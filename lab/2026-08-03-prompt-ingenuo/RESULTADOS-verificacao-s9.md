---
name: resultados-verificacao-s9
type: lab-resultados
status: fechado
created: 2026-08-06
updated: 2026-08-06
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
