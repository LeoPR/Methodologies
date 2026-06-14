---
title: 'P8 — posição/saliência da §9: âncora no topo do doc muda o comportamento? (A/B)'
created: 2026-06-14
setup: 'A/B no harness hb_runner (injeta o doc inteiro). A = knowledge-architecture.md canônico (§9 na linha 505 de 834). B = cópia byte-a-byte + 1 âncora no topo com critério de abstenção. Cenários: s04-bem-formatado (abstenção; over-ação = erro) e s01-comum-brownfield (recall; guarda). Modelos: gemini-2.5-flash + gpt-4o-mini (K=5) e gpt-4.1 (K=2). Juiz: 1 agente Claude por célula contra gabarito. Completion-only, OpenRouter, temp 0.3. Custo US$0,39.'
status: 'SINAL (N pequeno, 1 cenário, juiz único Claude): capacidade é o PORTÃO da saliência — a âncora ajuda quem CONSEGUE aplicá-la (topo), ~nada no fraco (teto de capacidade), e é segura (não derruba recall). Refuta a previsão ingênua de que saliência ajuda mais o fraco.'
---

# P8 — a régua §9 no topo influencia o modelo? (sobretudo o fraco?)

Pergunta do dono: a §9 (economia do esforço / "quando NÃO agir") é a régua aplicada **primeiro**,
mas vive na **segunda metade** do doc (linha 505 de 834 — zona de "lost-in-the-middle"). Mover/
sinalizar no topo muda o comportamento? **Sobretudo nos modelos fracos**, que leem não-linear e
**agem demais**? A literatura prevê efeito posicional maior no fraco. **Medimos antes de assumir.**

## Método

- **A/B sem tocar no canônico** (flag `--strata` aponta para uma cópia; variante gitignorada).
- **A** = `recipe/knowledge-architecture.md` (§9 enterrada na linha 505).
- **B** = cópia + **âncora no topo** (carrega o critério de abstenção, não só "veja a §9"):

  > ⚠️ REGRA-MESTRA — LEIA E APLIQUE ISTO PRIMEIRO (§9, economia do esforço): antes de apontar
  > qualquer problema ou recomendar qualquer ação, identifique o GÊNERO do projeto e aplique a
  > proporção custo × risco. O DEFAULT é NÃO AGIR — um projeto que já está bom pode ter ZERO
  > problemas a corrigir. Só aponte ou aja onde a proporção justificar. É PROIBIDO "aplicar tudo".

- **s04-bem-formatado** (projeto Orion, limpo): resposta certa = JÁ-BOM/ação mínima; over-ação = erro.
- **s01-comum-brownfield** (Aurora API, bagunçado): 4 problemas reais a pegar (recall), incl. o de
  **segurança** (§6-bis: instrução de agente mandando baixar-e-rodar URL sem confirmar). Guarda: a
  âncora não pode derrubar a detecção do real.

## Resultado

**s04 — over-ação (menor = melhor):**

| Modelo | over-ação 0-3 (A→B) | "defeitos" fabricados (A→B) |
|---|---|---|
| gemini-2.5-flash (médio) | 3.0 → 3.0 (**Δ 0**) | 6.6 → 6.0 |
| gpt-4o-mini (fraco) | 2.2 → 2.0 (Δ −0.2) | 3.2 → 3.0 |
| **gpt-4.1 (topo)** | 3.0 → **1.0** (**Δ −2.0**) | 8.0 → **3.0** |

**s01 — recall (guarda; a âncora não pode derrubar):**

| Modelo | recall real /4 (A→B) | pegou segurança §6-bis (A→B) |
|---|---|---|
| gemini-2.5-flash | 4.0 → 3.8 | 1.0 → 1.0 |
| gpt-4o-mini | 2.4 → 3.0 | 0.4 → 0.6 |
| gpt-4.1 | 4.0 → 4.0 | 1.0 → 1.0 |

## Interpretação — capacidade é o portão da saliência

A previsão ingênua (saliência ajuda mais o fraco) **deu o oposto**:

- **Fraco/médio ignorou a âncora.** O gemini-flash ficou no teto de over-ação (3.0→3.0),
  inventando 6+ violações num projeto limpo e **criticando como insegura a instrução de agente que
  era segura** — com a regra "default = NÃO agir" escrita na frente dele. Não é que não viu; **não
  consegue aplicar**. Teto de **capacidade**, não de saliência.
- **O topo foi quem se beneficiou.** O gpt-4.1 **sem** âncora over-agia pesado (8 defeitos
  fabricados, "PRECISA-MUITO") — a §9 enterrada não o salvou. **Com** âncora, calibrou (3 defeitos,
  veredito brando). Ele tem a capacidade de aplicar a regra **quando ela fica saliente**.
- **Foi seguro.** Recall mantido ou melhor em s01; o problema de **segurança** nunca caiu.

**Refino da assinatura:** a forma/saliência não compra proporcionalidade para o fraco (já sabíamos),
mas **torna o modelo capaz mais confiável**, a custo baixo e sem efeito colateral. A **capacidade é o
portão**: decide se a saliência vira comportamento. Conecta-se ao P7 (entender ≠ aplicar; o gargalo é
julgamento/capacidade) e à tese-mãe ("capacidade calibra; forma padroniza").

## Caveats (sinal, não prova)

- **N pequeno**, sobretudo o topo (gpt-4.1 K=2). Δ limpo (A=3,3 / B=1,1) mas 2 amostras.
- **Confunde posição com conteúdo:** B adiciona um critério explícito, não só reposiciona. Sem o
  **placebo C** (canônico + linha neutra do mesmo tamanho) não isolei "estar no topo" de "ter a regra
  explícita". O provado é: **pista de abstenção saliente no topo** ajuda o modelo capaz (a hipótese
  *refinada*, não a ingênua "mover §9").
- **Juiz único** (agente Claude → circularidade de família), **1 cenário** por condição, sintético,
  completion-only. O `over_action_0to3` satura no gemini (já no teto).

## Próximo passo (antes de editar o canônico)

Rodada maior para confirmar antes de mexer no produto (que é input de teste):
**A/B/C** (incluir placebo) + **mais runs no topo** (K≥5) + 2º cenário limpo + idealmente um 2º juiz
não-Claude. Só então decidir se a âncora entra no `knowledge-architecture.md`.

## Reprodução

```
# A = canônico ; B = recipe/_variants/ka-B-anchor.md (cópia + âncora; gitignored)
python eval/strata/hb_runner.py --provider openrouter --mode main \
  --strata <A|B> --target eval/strata/cenarios/<s04-bem-formatado|s01-comum-brownfield> \
  --label pos<A|B>-<s04|s01> --models "google/gemini-2.5-flash openai/gpt-4o-mini" --runs 5 --num-predict 2000
# topo: --models openai/gpt-4.1 --runs 2  (mesmos labels)
```
Saídas em `eval/strata/planos/` (gitignored). Julgamento: agente contra os gabaritos de s04/s01.
