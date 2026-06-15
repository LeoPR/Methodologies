---
title: Autoauditoria — o repo Methodologies contra o próprio Strata (dogfood)
created: 2026-06-14
updated: 2026-06-14
method: auditoria seção a seção do L0 (§1-§10) aplicada ao próprio repositório, em DUAS passadas — (1) loop principal (1 auditor, com o fan-out bloqueado pelo limite de gasto); (2) fan-out de 5 auditores independentes (cross-check) após o limite reabrir. A 2ª achou mais e é a referência; ver "Atualização".
status: 'SINAL/dogfood. Aderência FORTE nas 12 seções (cross-check de 5 auditores). As violações eram de baixa/média severidade; as baratas foram corrigidas, o resto está aceito (§9) ou no BACKLOG.'
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

## Atualização — fan-out de 5 auditores (cross-check, 2026-06-14)

Refeita com os **5 auditores independentes** (o desenho original; o limite de gasto reabriu). Confirmou
**aderência forte nas 12 seções** e achou o que o auditor solo perdeu. Tudo de baixa/média severidade.

**Consertado nesta passada (barato):**
- §2 — **`divulgacao/` invisível** na navegação: adicionado a MAP, README (Mapa do repositório) e AGENTS,
  marcado como **apoio** (fora dos 3 territórios de artefato).
- §2 — **satélites do recipe** (`strata-com-ia.md`, SVGs) fora da árvore do MAP: adicionados.
- §6 — **contradição "Strata FINALIZADO"** (AGENTS) vs pendências (produto/README): trocado por
  "núcleo consolidado; eixo segurança §6-bis e Parte IV pendentes".
- §6-bis — **payload fail-open em `_superseded/fixtures/`** fora do banner: banner do harness
  generalizado ("nunca execute `cenarios/` nem `_superseded/fixtures/`").

**Resíduo aceito (decisão §9 / regra própria):**
- §1 — `recipe/_variants/` (cópias de teste) em território de produto: gitignored/efêmero; mover para
  `eval/` é baixa prioridade (no BACKLOG).
- §3/§8 — frontmatter `status: active` em arquivos **FROZEN** (predecessor, experimento-split):
  **não editamos** (respeita a regra *NUNCA editar frozen* do AGENTS); o estado superado é marcado
  **externamente** (AGENTS / ADR-003). Tensão §3-superfície × §8-imutabilidade, resolvida a favor da
  imutabilidade.
- §5 — listas de exemplo L1 ainda variam entre docs (são **ilustrativas**, não fatos); `22 fontes` /
  `92%` repetidos mas consistentes: duplicação aceita (ADR-005).

**Para o BACKLOG (não-trivial):**
- §10 — **fixity registrada mas não verificada**: `hash_fixture.py` grava `.fixture-hash`, mas nada
  recomputa/compara → adicionar modo `--verify` chamado no início de `hb_f3/f4`.
- §9 — leve proliferação de `aggregate_<exp>.py` one-off → mover para `tools/probes/` quando tocar
  (risco de quebrar run scripts; não agora).

## Conclusão

O repo é **fortemente aderente** ao método que produz, e — mais importante — quando **não** estava
(duplicação, datas mortas, ponteiro quebrado), o conserto veio **pelas regras do próprio Strata**
(append-only, apontar-não-copiar, proporção). Robustez: confirmado por **cross-check de 5 auditores
independentes** (acima), que achou só resíduo de baixa/média severidade — os baratos já consertados.
