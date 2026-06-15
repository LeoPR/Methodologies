---
title: Autoauditoria — o repo Methodologies contra o próprio Strata (dogfood)
created: 2026-06-14
updated: 2026-06-14
method: auditoria seção a seção do L0 (§1-§10) aplicada ao próprio repositório. Feita no loop principal (1 auditor), NÃO pelo fan-out de 5 subagentes planejado — estes bateram no limite mensal de gasto da conta. Logo: 1 olhar, sem o cruzamento independente; menos robusta que o desenhado.
status: 'SINAL/dogfood honesto. Aderência FORTE no geral; as violações que existiam foram corrigidas nesta sessão pelas próprias regras do método.'
---

# Aplicamos o Strata ao repositório que o produz

O produto manda: *"peça a uma IA para auditar o projeto contra o L0"*. Aqui fizemos isso **no nosso
próprio repo** — o teste mais honesto de uma metodologia é ela sobreviver aplicada a si mesma.

> **Ressalva de método (§6):** o desenho era 5 auditores independentes (um por grupo de seções). Eles
> falharam no **limite mensal de gasto da conta Anthropic**; esta versão foi feita por **um** auditor (o
> loop principal). Vale como dogfood honesto, mas **sem o cruzamento** que daria robustez. Refazer com o
> fan-out quando o limite reabrir.

## Veredito por seção

| Seção do L0 | Aderência | Em uma linha |
|---|---|---|
| **§1** três tipos de artefato | **forte** | `recipe/`=produto · `lab/`=ideias · `eval/`=ferramenta, separados (ADR-004). |
| **§2** achabilidade | **forte** | múltiplas portas por intenção (README/MAP/AGENTS/STATUS + hub/OPINIAO). |
| **§3** rastreabilidade | **forte** | ADRs 001-006, sinal-de-troca, `updated:` (após conserto). |
| **§3-bis** força do artefato | **forte** | "sinal não prova", sólido/marcado, ideias rotuladas "não executado". |
| **§4** registro científico | **forte** | hipótese → método → RESULTADOS, com negativos. |
| **§5** fonte única | **forte** (pós-ADR-005) | hub canônico do estado; docs apontam. Resíduo aceito abaixo. |
| **§6** disciplina de fonte | **forte** | crítico de over-claim; honestidade de fonte no GLOSSARIO. |
| **§6-bis** fail-closed | **forte** | fail-open só nos fixtures inertes (marcados, nunca executados). |
| **§7** pipeline/maturação | **forte** | lab→recipe; negativos registrados (P8 refutado; `_superseded/`). |
| **§8** história imutável | **forte** | git, tombstones, Histórico append-only, sem renomear. |
| **§9** proporção | **forte** | recusou build-pipeline e a âncora-§9 (efeito fraco); abstém-se. |
| **§10** durabilidade do portador | **forte** | 1 arquivo portável; regenerável gitignored; formatos padrão. |

## O que o repo faz BEM (forças, com evidência)

- **Separa os três artefatos** e formalizou isso num ADR (`ADR-004`) — a ferramenta de prova (`eval/`)
  não contamina o produto (`recipe/`) nem as ideias (`lab/`).
- **História imutável de verdade:** o arco refutado (lumen/matrix) vive em `eval/strata/_superseded/`
  com tombstone; o P8 mantém o traço K=5 e **acrescenta** P8b/P8c em vez de reescrever; os números de
  seção do produto nunca são renumerados (convenção `-bis`).
- **Honestidade epistêmica:** "sinais, não prova" carimbado em toda parte; a assinatura tem níveis de
  solidez declarados; um crítico adversarial de over-claim rodou sobre os textos.
- **Proporção (§9) exercida contra si mesmo:** recusamos montar build/transclusão (ADR-005, nível 4) e
  recusamos editar o produto pela âncora-§9 quando a evidência a mostrou fraca (P8c). O método mandou
  abster-se, e abstivemos.
- **Fail-closed:** as únicas instruções perigosas são fixtures inertes, marcadas e nunca executadas.

## Violações — e que a maioria já foi consertada nesta sessão

A força aqui **não** é "não houve violação" — é que as violações foram **pegas e corrigidas pelas
próprias regras do método**, o que é o teste de verdade:

- **§5/§3 — drift de duplicação** (contagens `~840`/`53KB` re-copiadas e defasadas; `updated:` do produto
  estagnado): **corrigido** (commit `89f16da`) e a disciplina virou `ADR-005`.
- **§3 — âncora-fantasma `§22`** (ponteiro que eu havia criado para uma seção inexistente): **corrigido**
  (aponta agora a seção pelo nome).
- **§8/§5 — índices stale** (MAP listava só ADR-001..003; hub sem `updated:`): **corrigido** na propagação.

**Resíduo aceito (decisão §9, não-bug):**
- `22 fontes` / `juiz 92%` ainda aparecem como literal em alguns docs públicos. **Consistentes** (não
  driftaram); de-linká-los enfraqueceria o pitch sem ganho. Marcado como duplicação legítima (ADR-005).
- `recipe/_variants/` (cópias de teste do P8) vive em território de produto. É **gitignored e efêmero**,
  então inócuo; um §1 purista o poria sob `eval/`. Baixa prioridade.

## Nota de §9 sobre a própria sessão (meta)

Auditar o próprio método corre o risco de virar excesso de processo — o "excesso de §9 por outro eixo"
que o produto nomeia. Mitigamos: encerramos o fio da âncora-§9 quando o efeito provou-se fraco (em vez de
super-investigar), recusamos infraestrutura desproporcional, e esta autoauditoria é **um** passo datado,
não uma rotina pesada. Se ela mesma começar a custar mais do que rende, é para abster.

## Conclusão

O repo é **fortemente aderente** ao método que produz, e — mais importante — quando **não** estava
(duplicação, datas mortas, ponteiro quebrado), o conserto veio **pelas regras do próprio Strata**
(append-only, apontar-não-copiar, proporção). Caveat de robustez: 1 auditor, não o cruzamento de 5.
