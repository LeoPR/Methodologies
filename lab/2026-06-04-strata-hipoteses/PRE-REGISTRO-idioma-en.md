---
title: 'Pré-registro — replicação do Strata em inglês (robustez de idioma)'
created: 2026-07-01
status: 'PRÉ-REGISTRADO — desenho + análise travados em 2026-07-01 e confirmados pelo dono (desfecho, margem, escopo). Os hashes das fixtures EN entram no ato do congelamento, antes de rodar qualquer plano.'
---

# Pré-registro — replicação do Strata em inglês (robustez de idioma)

## Pergunta e hipótese

Os efeitos que medimos em português (recusa de injeção, conserto sem destruir histórico, abstenção proporcional)
são **independentes de idioma** ou um artefato do português?

Hipótese em forma de **equivalência** (não de diferença): o contraste método-vs-baseline em inglês é **equivalente**
ao em português, dentro de uma margem pré-fixada. É validade externa — o eixo que a evidência só-PT não cobre.

## O que este estudo NÃO é

Testa **independência de idioma**, não a circularidade estreita (um mantenedor autor de método + gabarito, N=1 gênero).
As duas afirmações ficam separadas.

## Desenho

- **Modelo fixo; varia só o idioma.** Contraste primário = método-vs-baseline **dentro** de cada língua, comparado
  entre línguas. O imposto ~uniforme da tradução (4–11pp) **cancela no contraste** — **nunca** comparar taxa
  **absoluta** PT vs EN.
- **Dois corpora:** (a) OSS **inglês nativo** (`external-fixtures`) = validade externa; (b) pares **PT↔EN traduzidos**
  = contraste controlado, com translationese medido. Respondem perguntas diferentes; ambos entram.
- **Andaime do juiz numa língua só** (inglês) nas duas frentes; **mesmo painel** cross-vendor nos dois; autor ≠ juiz.

## [LOCK 1 — CONFIRMADO] Desfecho primário

**F3 `OBEY_RATE`** (fail-closed / recusa de injeção). Razão: é o elo de **menor concordância** entre juízes e o mais
perigoso para uma afirmação de segurança — uma propriedade que só valesse em português seria uma limitação séria.

## [LOCK 2 — CONFIRMADO] Margem de não-desvio (SESOI)

**±10 pontos percentuais** na diferença de taxa **pareada**.
Justificativa: (a) é da ordem do **imposto uniforme da tradução** (4–11pp) — uma margem menor confundiria
translationese com efeito real; (b) é a **granularidade em que a `OPINIAO-DE-USO` afirma** — ela fala em faixas
grossas ("o econômico recusa a injeção", "só o topo se abstém"), e um desvio abaixo de ~10pp não vira uma faixa
diferente na opinião de uso.
Declara-se "**replica em inglês, sem desvio relevante**" só se o **IC 90%** da diferença pareada couber **inteiro**
em ±10pp; senão, "**indeterminado**" (nunca "sem efeito").

## [LOCK 3 — CONFIRMADO] Escopo: piloto de F3 primeiro

**Piloto:** só **F3** (recusa), ponta-a-ponta num N pequeno, para achar problemas do pipeline barato antes de escalar.
Só depois a **onda 1 completa** (F3 + F4 + F1/M0) e a **onda 2** (F5/F6/GÊNERO).
N do piloto: as fixtures F3 existentes (`s05-clean`, `s05-encoded`, `s05-legit` — as públicas; `s05-tarefas` é
privada) × sujeitos de 2–3 tiers × ≥3 runs; o júri free é fixo.

## Roster fixo

- **Sujeitos (escada):** topo (Opus 4.8 / GPT-5.5), médio (GLM-5.2 / DeepSeek V4), econômico (gpt-oss / Nemotron free),
  local (qwen3:8b…). Versões pinadas.
- **Júri free cross-vendor (fixo):** `cerebras:gpt-oss-120b` + `nvidia:mistralai/mistral-nemotron` +
  `nvidia:.../llama-3.3-nemotron-super-49b-v1` (o que já está no harness; verificado 3/3 no prompt real).

## Análise (pré-especificada, nesta ordem)

1. **Primário:** McNemar **mid-p** sobre os pares PT/EN discordantes + **IC 90% de Newcombe** da diferença pareada
   (nunca o McNemar exato condicional — sem poder com N pequeno).
2. **Não-desvio:** **TOST** de proporções correlacionadas contra a margem do LOCK 2.
3. **Secundário:** logística de **efeitos mistos bayesiana** (idioma fixo; fixture/modelo/juiz aleatórios; prior fraco).
4. **Concordância:** Krippendorff α com IC **bootstrap** (B≥5000) nas duas línguas, sempre ao lado da **prevalência**;
   Gwet AC1/PABAK como sensibilidade. Efeito + intervalo acima de p; IC contra limiar, nunca adjetivo.

## Controles de confound

- **Nativo-primeiro:** traduzir só o que não tem equivalente inglês nativo, com **dupla-tradução + reconciliação**,
  preservando os tokens-gabarito/alvos de regex; **congelar por hash**.
- **Medir translationese** (TTR, densidade lexical, back-translation) e entrar como **covariável**.
- **Revalidar o gate mecânico em inglês** (adaptar o regex F3/F4 e **re-passar o self-test de 0 falsos-negativos**).

## Compromisso de hash

- Ao congelar as fixtures EN, os **SHA-256** entram aqui **antes** de qualquer plano EN. *(placeholder — a preencher)*
- **Tradução por IA registrada** (o `Translator` do DataCite aceita "sistema automatizado").

## Circularidade

Mede se o efeito é do **método/idioma**, dentro do braço próprio; **não** resolve a independência de autoria.
Mesma ressalva de [GABARITO-genero-temporal-own.md](GABARITO-genero-temporal-own.md) e [PRE-REGISTRO-own-tcf.md](PRE-REGISTRO-own-tcf.md).
