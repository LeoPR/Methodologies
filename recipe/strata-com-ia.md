---
title: Strata com IA — guia prático de uso
status: active
created: 2026-06-08
updated: 2026-06-14
purpose: responder ao desenvolvedor "funciona no meu ambiente? vai sair caro?" — só o que funciona
nota: a pesquisa completa (inclusive o que NÃO funciona e por quê) está em lab/2026-06-04-strata-hipoteses/RESULTADOS-p6..p9 (p8 = posição/variância; p9 = modelos novos / churn de L2)
---

# Strata com IA — guia prático

O texto do método é o mesmo para todos. O que muda o resultado é **quem executa e como**.
Duas regras de ouro antes de qualquer modelo:

1. **NÃO entregue o método canônico cru a um modelo barato** — é a pior opção.
   Dê a **checklist** (`../lab/2026-06-04-strata-hipoteses/strata-ai-native/strata-checklist.md`).
2. **Saída de IA = rascunho a revisar**, nunca veredito automático.

## Decisão rápida — o que usar

| Eu quero… | Use | Custo | Como |
|---|---|---|---|
| **o melhor, confiável** | **Claude Opus** + checklist | 💳 $$$ · ~$7/M | 1 prompt; o **único** positivo *e* consistente nos dois tipos de projeto |
| **barato (aceitando variância)** | **deepseek-v3 + aplicação em ETAPAS** | 💳 $ · ~$0,26/M | 4 turnos: reconheça o bom → situe no tempo → gates com evidência → priorize. Ajuda **em média**, mas varia — sempre revise |
| **barato, 1 prompt só** | **glm-4.6** + checklist | 💳 $ · ~$0,56/M | rápido; resultado **inconsistente** entre projetos |
| **peneira inicial do óbvio** | gpt-4.1-mini / gpt-5 + checklist | 💳 $–$$ · ~$0,5–2/M | não inventa, mas acha pouco |
| **grátis / na minha máquina** | *(sem opção confiável hoje)* | 🖥️ 🆓 · $0 | os modelos locais ou **alucinam** ao concluir (deepseek-r1:8b) ou **acham nada** (qwen3:4b-thinking ≈ neutro). Veja "Limites" |

*Faixa de custo: **$** = barato (≤ ~$0,6/M) · **$$** = médio (~$0,6–3) · **$$$** = caro (> ~$3) · **🆓** = grátis. 💳 pago · 🖥️ local. Valores **aproximados** — preço de modelo muda com o tempo (é L2).*

![Strata por IA — por vendor × custo](strata-com-ia-fronteira.svg)

*(Agrupado por **vendor × pago/grátis** (jun/2026). Dois testes: **LIMPO** = age demais num projeto
já-bom? (menos = melhor; 0 = abstém) · **BAGUNÇADO** = pega os problemas reais + a instrução de
segurança? Leitura: **no limpo quase todos agem demais** — o Opus é o mais calibrado (2,0), o glm vem
depois (2,4), o resto crava em 3,0 (o gpt-4.1 chega a inventar 8,4); **ninguém se abstém 100%, nem o
topo**. No **bagunçado** a maioria pega o real (4/4) + segurança; o barato da OpenAI (gpt-4o-mini) e o
grátis falham.)*

> **Leia pelo TIER/vendor, não pelo nome (snapshot jun/2026).** Nomes de modelo são L2 e churnam
> (`gpt-5`→`gpt-5.4` em semanas). O que **dura** é o padrão: no limpo o custo **não compra abstenção**
> (até o topo age um pouco demais); no bagunçado quase todos vão bem, e o **barato falha na segurança**.
> Os *reasoners* novos da OpenAI (gpt-5-mini/nano) ainda **nem rodam** no nosso modo completion-only.
> Método e dados: [`RESULTADOS-p9`](../lab/2026-06-04-strata-hipoteses/RESULTADOS-p9-modelos-novos-jun.md).

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
