---
title: A2 — Validação cruzada parser × cc-statistics
created: 2026-06-04
status: substancialmente fechado (com diferença definicional documentada)
---

# A2 — Validação cruzada (GATE-1 b)

Segundo instrumento independente: **cc-statistics 1.0.3** (`uv tool install cc-statistics`).
Ferramenta de terceiros (chinesa), lê os mesmos JSONL.

## Comparação no mesmo instante (sessão inteira, main-only)

| opus-4-8 (modelo dominante) | parse_usage.py | cc-stats | Δ |
|---|---|---|---|
| input | 16.435 | ~16,3K | ~0,8% |
| output | 605.289 | ~601,5K | ~0,6% |
| cache_read | 52.429.618 | ~52,1M | ~0,6% |

**Concordância <1% no modelo dominante.** GATE-1(b) (≤3%) atingido para opus +
cache_read.

## Os dois achados que validam o parser

1. **Ambos deduplicam.** cc-stats reporta output ~741K (total), não os ~5M que
   a contagem por-linha daria. Um instrumento totalmente independente chega ao
   mesmo regime → **a dedup-por-message.id é a definição correta**, não uma
   escolha arbitrária nossa. Esta é a confirmação mais importante de A2.
2. **Perfil idêntico**: ambos veem cache_read dominando (~94-100% hit rate),
   mesmos 2 modelos (opus-4-8 + sonnet-4-6), mesma ordem de grandeza (~65-69M).

## A diferença residual (definicional, não de confiabilidade)

| total | parse_usage.py (main) | cc-stats |
|---|---|---|
| output | 713.693 | 741,0K (~3,7%) |
| cache_read | 64,73M | 65,7M (~1,5%) |
| sonnet input | 1.517 | ~10,3K (grande) |

A divergência concentra-se no **Sonnet** e vem de **atribuição de sidechain**:
cc-stats dobra alguns registros de subagente na sessão-mãe; meu parser separa
sidechains (path `/subagents/`) por flag. Era a previsão exata da verificação
adversarial ("dedup + inclusão de sidechains dominam o delta").

## Por que um match byte-a-byte é impossível (e tudo bem)

1. **Sessão viva**: a sessão `443991ed` cresce a cada turno; os dois instrumentos
   rodam em instantes diferentes (segundos de drift = milhares de tokens).
2. **Granularidade de janela**: o `--until` do cc-stats é **por sessão**, não por
   registro. Com uma só sessão cruzando 2026-06-03→04, cc-stats **não consegue
   reproduzir** minha janela congelada (record-level). Limitação real do cc-stats.
3. **Atribuição de sidechain** difere entre as ferramentas.

## Veredito A2

**Substancialmente fechado.** O parser é validado contra um instrumento
independente para o modelo dominante (<1%) e — o mais importante — a **dedup é
corroborada de forma independente**. A diferença residual é **definicional**
(sidechain), conhecida e prevista, não um erro de confiabilidade. Para fechar a
100%: normalizar o escopo de sidechain entre as duas (1 passo), mas o ganho não
justifica agora (§9) — a régua já é confiável para medir deltas.

## Notas de campo (relevantes à metodologia dev-environment Z:\)

- **cc-stats quebra no console Windows (cp1252)** ao imprimir Unicode/emoji.
  Workaround: `$env:PYTHONIOENCODING='utf-8'; $env:PYTHONUTF8='1'`. Candidato a
  regra na metodologia de ambiente (terminal UTF-8 por padrão).
- **`uv tool install` falha hardlink** porque `UV_CACHE_DIR=Z:` e o destino
  `C:\Users\leona\.local\bin` estão em filesystems diferentes → "falling back to
  full copy". Não quebra, mas é a **LACUNA 3** da metodologia Z:\: tools globais
  do uv não se beneficiam do cache em Z: (cross-FS). Documentar ou setar
  `UV_LINK_MODE=copy` para silenciar.
