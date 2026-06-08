---
title: Strata com IA — guia prático de uso
created: 2026-06-08
purpose: responder ao desenvolvedor "funciona no meu ambiente? vai sair caro?" — só o que funciona
nota: a pesquisa completa (inclusive o que NÃO funciona e por quê) está em lab/2026-06-04-strata-hipoteses/RESULTADOS-p6-*
---

# Strata com IA — guia prático

O texto do método é o mesmo para todos. O que muda o resultado é **quem executa e como**.
Duas regras de ouro antes de qualquer modelo:

1. **NÃO entregue o método canônico cru (53KB) a um modelo barato** — é a pior opção.
   Dê a **checklist** (`../lab/2026-06-04-strata-hipoteses/strata-ai-native/strata-checklist.md`).
2. **Saída de IA = rascunho a revisar**, nunca veredito automático.

## Decisão rápida — o que usar

| Eu quero… | Use | Custo | Como |
|---|---|---|---|
| **grátis, na minha máquina** | **deepseek-r1:8b** (Ollama) + checklist | $0 / local 🖥️ | `think:true`, `num_predict` alto (8000+), contexto grande |
| **barato e bom (API)** | **deepseek-v3 + aplicação em ETAPAS** | ~$0.26/M 💳 | em 4 turnos: reconheça o bom → situe no tempo → gates com evidência → priorize |
| **barato, 1 prompt só** | **glm-4.6** + checklist | ~$0.56/M 💳 | rápido, mas o resultado varia mais entre projetos |
| **o melhor, direto** | **Claude Opus** + checklist | ~$7/M 💳 | 1 prompt; positivo e **consistente** |
| **filtro barato do óbvio** | gpt-4.1-mini / gpt-5 + checklist | ~$0.5–2/M 💳 | não inventa, mas acha pouco — bom como peneira inicial |

![fronteira custo × qualidade × ambiente](strata-com-ia-fronteira.svg)

*(Verde = local, azul = grátis remoto, roxo = API paga. Eixo Y = problemas reais achados −
falso-positivos; só aparecem as configurações que ajudam.)*

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
  bagunçado). Os demais variam — por isso a coluna "como" acima.

## Notas finais

- **Grátis remoto** (gateways `:free`): rate-limit pesado e os modelos testados não alcançaram
  qualidade útil nesta tarefa — preferível o **grátis local** (Ollama) ou um **pago barato**.
- A análise completa — incluindo as configurações que **não** funcionam, os experimentos e os
  gráficos de pesquisa — está em `lab/2026-06-04-strata-hipoteses/` (`RESULTADOS-p6-*`).
