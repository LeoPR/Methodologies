---
title: Strata com IA — guia prático de uso
status: active
created: 2026-06-08
updated: 2026-06-15
purpose: responder ao desenvolvedor "funciona no meu ambiente? vai sair caro?" — só o que funciona
nota: a pesquisa completa (inclusive o que NÃO funciona e por quê) está em lab/2026-06-04-strata-hipoteses/RESULTADOS-p6..p9 (p8 = posição/variância; p9 = modelos novos / churn de L2)
---

# Strata com IA — guia prático

O texto do método é o mesmo para todos. O que muda o resultado é **quem executa e como**.
Duas regras de ouro antes de qualquer modelo:

1. **NÃO entregue o método canônico cru a um modelo barato** — é a pior opção.
   Dê a **checklist** (`../lab/2026-06-04-strata-hipoteses/strata-ai-native/strata-checklist.md`).
2. **Saída de IA = rascunho a revisar**, nunca veredito automático.

## Decisão rápida — o que usar (modelos do Copilot, jun/2026)

| Eu quero… | Use (+ checklist) | Por quê |
|---|---|---|
| **o mais confiável** | **Opus 4.8** ou **Gemini 3.1 Pro** | inventam menos no **limpo** (~3, o mínimo) e pegam tudo no bagunçado |
| **bom, mais barato** | **Sonnet 4.6** ou **Gemini 3 Flash** | o "mínimo que serve": pegam tudo no bagunçado; inventam ~4 no limpo → revise |
| **se você usa GPT** | **GPT-5.5** (a melhor da OpenAI) | pega tudo no bagunçado, mas **inventa bastante no limpo** (~6) → trate como rascunho |
| **o mais barato que ainda acha o real** | **Haiku 4.5** · **GPT-5 mini** | pegam o bagunçado (4/4 + segurança), mas **inventam muito no limpo** (7–10) → só rascunho |
| **NÃO usar sozinho** | gpt-4o-mini, glm-4.5-air, locais/grátis | **falham na segurança** (não pegam a instrução perigosa) ou são instáveis |

*Regra: no projeto **bagunçado** quase todos servem; a diferença está no **limpo** (quanto inventam) — sempre **revise** a saída. Detalhe no gráfico abaixo. (Nomes/preços de modelo mudam rápido — é L2; confira a lista atual do Copilot.)*

![Strata por IA — escada por vendor (modelos do Copilot)](strata-com-ia-fronteira.svg)

**Como ler o gráfico** (jun/2026; os modelos do **Copilot**, por vendor, do melhor ao mínimo que serve).
Testamos cada modelo em **dois tipos de projeto**:

- **Projeto limpo** — já bem-organizado, com pouco ou nada a corrigir (o "já-bom").
- **Projeto bagunçado** — desorganizado, com problemas reais (o *brownfield* típico), incluindo uma
  instrução de segurança perigosa.

A descoberta que organiza o gráfico: **todos esses modelos capazes pegam o projeto bagunçado** — acham os
4 problemas reais e a instrução de segurança (4/4 · seg 5/5). **O que os separa é o projeto limpo.**

**No projeto limpo, a barra mede quantos problemas o modelo _inventa_** onde não há nada a corrigir. **0 =
nenhum** (o ideal, num projeto que já está bom); **quanto menos, melhor**. Ninguém zera — nem o topo: o melhor
já inventa ~3. (Antes a nota era 0–3, mas com mais amostras quase todos saturam o topo da escala; o número de
**invenções** é o que de fato diferencia.)

O **◀ "mínimo que serve"** marca, em cada vendor, o modelo mais barato que ainda **não floda** o projeto
limpo. Abaixo dele, o modelo ainda pega o bagunçado, mas no limpo inventa demais — trate como rascunho.

**O que o gráfico diz:**
- Inventam menos no limpo (os melhores): **Opus 4.8** (~2,6) e **Gemini 3.1 Pro** (~2,8) — quase empatados.
- A **OpenAI inventa mais** (GPT-5.5 ~5,8); o **Haiku floda** o limpo (~9,6 — o que mais inventa de todos).
- Ficam **fora do gráfico** (só no caderno científico): os que **falham na segurança** (gpt-4o-mini,
  glm-4.5-air) e o **grátis** (instável). O gráfico mostra só os **usáveis**.

> **Leia pelo padrão, não pelo nome.** Modelos mudam rápido (o **gpt-4.1 já se aposentou → GPT-5.5**); o que
> **dura** é o comportamento por tier. Método e dados:
> [`RESULTADOS-p9`](../lab/2026-06-04-strata-hipoteses/RESULTADOS-p9-modelos-novos-jun.md).

## A forma importa mais que o modelo

A maior diferença de qualidade vem de **como** você pede, não de qual modelo:
- **Checklist** (sim/não por gate, com as 3 regras anti-falso-positivo) >> texto cru.
- **Etapas** (aplicar em turnos separados) é o que mais ajuda os modelos médios/baratos —
  obriga o modelo a reconhecer o que está bom e situar no tempo **antes** de apontar defeito.
- **Reasoners** (deepseek-r1, qwen3-thinking) precisam de `think:true` e bastante orçamento de
  tokens, senão "pensam" e não respondem.

## Limites (o que esperar — não é defeito, é como calibrar)

- **Modelos baratos são bimodais:** bons em achar o problema **óbvio** num projeto bagunçado,
  fracos em **restrição** (tendem a super-criticar um projeto limpo). Trate o resultado como
  rascunho e confirme cada achado com o trecho citado.
- **Ponto cego universal:** a dimensão **temporal** (datas/história, §3/§8) — o modelo marca o
  histórico/datado como problema atual. Revise esses achados com atenção.
- **Padrão-ouro:** só o Opus é positivo **e** consistente nos dois tipos de projeto (limpo e
  bagunçado). Todos os outros **oscilam** entre ajudar e atrapalhar — trate como rascunho.
- **Reasoner local engana:** um modelo de raciocínio pequeno (deepseek-r1:8b) pode parecer
  "limpo" só porque **truncou antes de concluir**; quando ele de fato termina, **alucina** no
  projeto limpo igual aos baratos. Não confie no resultado parcial.

## Notas finais

- **Não há opção grátis confiável hoje** — nem local nem remota. Local: ou alucina ao concluir
  (deepseek-r1:8b) ou acha nada (qwen3:4b-thinking ≈ neutro). Remoto `:free`: rate-limit pesado
  e qualidade baixa. Para um auditor que **ajuda**, hoje é **pago** (barato-variável ou Opus).
- A análise completa — configurações que **não** funcionam, os experimentos e os gráficos
  de pesquisa — está em `lab/2026-06-04-strata-hipoteses/`
  (`RESULTADOS-p6-*`).
