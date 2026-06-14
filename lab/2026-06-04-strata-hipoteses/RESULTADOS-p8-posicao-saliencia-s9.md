---
title: 'P8 — posição/saliência da §9: âncora no topo do doc muda o comportamento? (A/B)'
created: 2026-06-14
setup: 'A/B no harness hb_runner (injeta o doc inteiro). A = knowledge-architecture.md canônico (§9 na linha 505 de 834). B = cópia byte-a-byte + 1 âncora no topo com critério de abstenção. Cenários: s04-bem-formatado (abstenção; over-ação = erro) e s01-comum-brownfield (recall; guarda). Modelos: gemini-2.5-flash + gpt-4o-mini (K=5) e gpt-4.1 (K=2). Juiz: 1 agente Claude por célula contra gabarito. Completion-only, OpenRouter, temp 0.3. Custo US$0,39.'
status: 'SINAL (N pequeno, 1 cenário, juiz único Claude): capacidade é o PORTÃO da saliência — a âncora ajuda quem CONSEGUE aplicá-la (topo), ~nada no fraco (teto de capacidade). ATUALIZADO (P8b, K=10 + varredura de temp 0.3/0.7/1.0): confirma capacidade=portão; CORRIGE o catch de segurança do fraco (K=5 dava 0,4-0,6 → K=10 dá 0,1-0,2, pass^k=0 = NÃO-detecção confiável, não ganho); o "0 flips" a 0,3 era em parte mode-lock (veredito quebra a 0,7/1,0). Acurácia × precisão reportadas separadas (ver ADR-006).'
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

> **⚠️ Correção (ver P8b, abaixo):** a coluna de segurança acima é **K=5** e **enganou por otimismo**. Com
> **K=10** (varredura, variante A), o catch de segurança do gpt-4o-mini é **0,1–0,2** (não 0,4–0,6), com
> `pass^k=0`. A "subida" A→B era **ruído de fronteira**, não ganho da âncora. Trate as tabelas K=5 como
> sinal grosso; os números firmes de precisão estão no P8b.

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

## P8b — varredura de temperatura: acurácia × precisão (K=10, 2026-06-14)

Motivado pela observação do dono: *"conseguiu 1× ≠ estável; o hiperparâmetro mexe na estabilidade, não
na inteligência; o modelo fraco oscila na fronteira de competência."* Re-rodei só o **gpt-4o-mini** (o
fraco que oscilou), variante **canônica (A)**, nos dois sinais, a **temp 0,3 / 0,7 / 1,0, K=10** cada
(flag `--temp` novo, aditivo). Eixos separados conforme **ADR-006**. Custo US$0,14.

**s01 — detecção de segurança (§6-bis):**

| temp | catch (acurácia) | Wilson 95% | pass^k (10/10) | recall geral /4 (méd±sd) |
|---|---|---|---|---|
| 0,3 | **1/10 = 0,10** | 0,02–0,40 | 0 | 2,0 ± 0,63 |
| 0,7 | 2/10 = 0,20 | 0,06–0,51 | 0 | 2,8 ± 0,40 |
| 1,0 | 2/10 = 0,20 | 0,06–0,51 | 0 | 2,2 ± 0,40 |

**s04 — over-ação no projeto limpo:**

| temp | over-ação (méd±sd) | defeitos fabricados (méd±sd) | vereditos distintos |
|---|---|---|---|
| 0,3 | 3,0 ± 0 | 3,4 ± 0,49 | **1 (mode-lock)** |
| 0,7 | 3,0 ± 0 | 3,4 ± 0,49 | 2 (quebrou) |
| 1,0 | 3,0 ± 0 | 3,1 ± 0,30 | 2 (quebrou) |

**Leitura — responde as 3 perguntas do dono:**

1. **"Conseguiu 1×" superestima — comprovado no nosso dado.** Mesma temp (0,3), mesma variante: o K=5
   dava segurança 2/5 (40%); o **K=10 dá 1/10 (10%)**. O K=5 era ruído otimista. A segurança do fraco é
   **não-detecção confiável** (`pass^k = 0` em toda temp; Wilson de ~2% a ~51%), não "às vezes pega".
2. **Os dois modos de falha aparecem SEPARADOS — exatamente o eixo acurácia × precisão:**
   - **Over-ação (s04) = confiavelmente errada** (*preciso e errado*): travada em **3,0 (SD 0) em TODAS
     as temps**. Temperatura **não move** — confirma "temp = precisão, não inteligência". Falha de
     **capacidade estável**, não de fronteira.
   - **Segurança (s01) = fronteira**: taxa baixa e **oscilante mesmo a 0,3** — a distribuição do fraco
     cruza o limiar bom/ruim. É aqui que a variância vive.
3. **Mode-lock confirmado:** o veredito categórico de s04 era **unânime a 0,3** e **se dividiu a 0,7/1,0**
   — a estabilidade a 0,3 era em parte **travamento**, não confiabilidade. (O *nível* de over-ação, porém,
   ficou estável: o fraco over-age sempre; só o rótulo varia.)

**O que o P8b corrige no P8 (acima):** a "segurança 0,4→0,6 (melhorou)" estava errada como ganho (ruído de
fronteira; real ~0,1–0,2, `pass^k=0`) — **o fraco NÃO detecta segurança de forma confiável**, o que
*reforça* o teto de capacidade. O "veredito grosso estável a 0,3" era em parte mode-lock. A tese central
**sobrevive** (capacidade é o portão — é sobre acurácia, independe da estabilidade).

## Próximo passo (antes de editar o canônico)

Feito: varredura de temperatura no fraco (P8b). **Falta** para decidir se a âncora entra no produto:
**placebo C** (isolar posição × conteúdo), **gpt-4.1 com K≥5** (hoje K=2 = não-atestável), e um **2º juiz
não-Claude**. Reportar sempre **acurácia E precisão** (ADR-006). Só então mexer no `knowledge-architecture.md`.

## Reprodução

```
# A = canônico ; B = recipe/_variants/ka-B-anchor.md (cópia + âncora; gitignored)
python eval/strata/hb_runner.py --provider openrouter --mode main \
  --strata <A|B> --target eval/strata/cenarios/<s04-bem-formatado|s01-comum-brownfield> \
  --label pos<A|B>-<s04|s01> --models "google/gemini-2.5-flash openai/gpt-4o-mini" --runs 5 --num-predict 2000
# topo: --models openai/gpt-4.1 --runs 2  (mesmos labels)
# P8b — varredura de temperatura (acurácia × precisão):
python eval/strata/hb_runner.py --provider openrouter --mode main \
  --strata recipe/knowledge-architecture.md --target eval/strata/cenarios/<s01|s04> \
  --label var-<s01|s04>-t<03|07|10> --models openai/gpt-4o-mini --runs 10 --num-predict 2000 --temp <0.3|0.7|1.0>
```
Saídas em `eval/strata/planos/` (gitignored). Julgamento: agente contra os gabaritos de s04/s01.
