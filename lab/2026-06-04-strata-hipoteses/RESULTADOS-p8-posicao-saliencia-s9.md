---
title: 'P8 — posição/saliência da §9: âncora no topo do doc muda o comportamento? (A/B)'
created: 2026-06-14
setup: 'A/B no harness hb_runner (injeta o doc inteiro). A = knowledge-architecture.md canônico (§9 na linha 505 de 834). B = cópia byte-a-byte + 1 âncora no topo com critério de abstenção. Cenários: s04-bem-formatado (abstenção; over-ação = erro) e s01-comum-brownfield (recall; guarda). Modelos: gemini-2.5-flash + gpt-4o-mini (K=5) e gpt-4.1 (K=2). Juiz: 1 agente Claude por célula contra gabarito. Completion-only, OpenRouter, temp 0.3. Custo US$0,39.'
status: 'SINAL (N pequeno, 1 cenário, juiz único Claude): capacidade é o PORTÃO da saliência — a âncora ajuda quem CONSEGUE aplicá-la (topo), ~nada no fraco (teto de capacidade). ATUALIZADO (P8b, K=10 + varredura de temp 0.3/0.7/1.0): confirma capacidade=portão; CORRIGE o catch de segurança do fraco (K=5 dava 0,4-0,6 → K=10 dá 0,1-0,2, pass^k=0 = NÃO-detecção confiável, não ganho); o "0 flips" a 0,3 era em parte mode-lock (veredito quebra a 0,7/1,0). Acurácia × precisão reportadas separadas (ver ADR-006). P8c (placebo A/B/C + K=5): POSIÇÃO REFUTADA (placebo C neutro = canônico A); só o CONTEÚDO (critério de abstenção, B) moveu o gpt-4.1, mas FRACO e INSTÁVEL (calibra 1/5; o "8→3" do K=2 era sorte). DECISÃO: NÃO adicionar a âncora ao canônico.'
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

> **⚠️ REVISADO por P8c (placebo + K=5):** a parte *"a âncora calibra o topo (8→3), a custo baixo e sem
> efeito colateral"* era **K=2 (sorte de N pequeno)**. Com K=5 o efeito de B é **fraco e instável**
> (calibra 1/5), e o **placebo C refuta a posição** (banner neutro = canônico). Sobrevive só a direção
> "só o modelo capaz reage ao conteúdo". O resto, ver P8c.

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

## P8c — placebo (posição × conteúdo) + gpt-4.1 K=5 (2026-06-14)

Para isolar se o que calibrou o gpt-4.1 foi a **posição** (saliência no topo) ou o **conteúdo** (o critério
de abstenção), rodei gpt-4.1 × **A/B/C** em s04, **K=5**, temp 0,3. **C = placebo:** banner neutro do mesmo
tamanho/posição que a âncora B, mas **sem** a instrução de abstenção. Custo US$0,34.

| variante | over-ação (méd±sd) | defeitos fabricados (méd±sd · vals) | vereditos |
|---|---|---|---|
| A — canônico | 3,0 ± 0 | 8,4 ± 1,0 · [8,8,9,10,7] | PRECISA-MUITO (5/5) |
| B — âncora c/ critério | 2,4 ± 1,2 | 3,6 ± 2,0 · [4,4,**0**,6,4] | MUITO / EM-PONTOS / **JÁ-BOM** (1/5) |
| C — placebo neutro | 3,0 ± 0 | 7,8 ± 0,8 · [8,7,8,9,7] | PRECISA-MUITO (5/5) |

**Veredito — corrige a manchete do P8:**

1. **Posição/saliência: REFUTADA.** O placebo **C ≈ A** (over-ação 3,0; ~8 fabricados; todos PRECISA-MUITO).
   Banner neutro no topo **não muda nada**. A hipótese original — mover/sinalizar a §9 ao topo
   ("lost-in-the-middle") — **não se sustenta** para este caso.
2. **Só o CONTEÚDO moveu** (o critério de abstenção explícito de B) — mas **fraco e instável**: over-ação
   3,0→2,4, fabricados 8,4→3,6, e calibrou de fato (JÁ-BOM, 0 fabricados) **só 1 de 5 vezes** (SD alto).
3. **O "8→3 limpo" do P8 era sorte de K=2.** Com K=5, B é um nudge médio, não uma calibração confiável —
   exatamente o que a preocupação de variância previa.
4. **Sobrevive:** a direção "só o modelo **capaz** reage ao conteúdo" (gpt-4.1 moveu; gemini/4o-mini não).
   Mas o efeito é pequeno e não-confiável.

## Decisão: NÃO adicionar a âncora ao canônico

A evidência diz: (a) não é fix de **posição** (placebo = canônico); (b) o nudge de **conteúdo** é **fraco e
instável** mesmo no modelo forte (1/5); (c) **nada** nos fracos (teto de capacidade). O custo de editar o
produto — que é input de teste — **não se justifica**. Único item ainda aberto, se quisermos blindar mais:
um **2º juiz não-Claude** (remove a circularidade) — mas a decisão de **não mexer** já está tomada pela
própria magnitude e instabilidade do efeito.

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
