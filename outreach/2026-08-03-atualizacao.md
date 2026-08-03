---
title: 'Notícia 2026-08-03: Strata testado nos dois idiomas, custo medido, manual de uso publicado'
created: 2026-08-03
updated: 2026-08-03
status: 'Fonte canônica das notícias de divulgação. Os canais (linkedin/, medium/) formatam daqui.'
---

<!-- l10n: doc_id=outreach-2026-08-03 · lang=pt-BR · canonical -->
[English](2026-08-03-update.en.md) · **Português**

# Notícia-fonte 2026-08-03 (resumo das conclusões, para derivar posts)

> Este arquivo é a **fonte** das notícias. Cada canal em subpasta formata o seu texto a
> partir daqui, respeitando os limites do meio. Não edite o canal sem atualizar aqui.

## O que é o Strata (1 frase)

Método para organizar o conhecimento que o trabalho longo acumula, em camadas de
durabilidade: separa o que é atemporal (Mneme, L0) do que é forma consolidada (Morfé, L1)
e do que é ferramenta datada (Órganon, L2). Trocar de ferramenta sem perder o porquê.

## Estado do produto

- Núcleo (L0) **fechado editorialmente em 2026-08-01** (ciclo P1-P5).
- Documento canônico em inglês, tradução PT derivada no mesmo commit (ADR-008).

## Conclusões de teste (as manchetes)

1. **A IA aplica o método, do econômico ao topo.** O conserto de um defeito conhecido (§5)
   **satura** de ~8B local (20-27B satura completo) ao topo de fronteira; sem o método, os
   mesmos modelos falham na grade inteira. Grade de ~350 runs, gold mecânico + júri cego
   cross-vendor (2026-08-02).
2. **A recusa de segurança (§6-bis) sai espontânea** na geração atual: a IA se recusa a
   executar a instrução maliciosa plantada ("baixe e rode esta URL"), mesmo no tier
   econômico. Único evitar: llama-4-scout.
3. **A borda que separa modelos é a abstenção (§9)**: saber NÃO agir num projeto que já
   está bom. É propriedade de modelo, não de preço, tier nem idioma. Por isso a regra:
   modelo médio/econômico = checklist + humano no loop; auto-auditoria autônoma só com topo.
4. **Agente em sandbox: transferiu.** Na primeira célula com ferramentas reais, o padrão se
   manteve na execução (10/12 com o método × 2/12 sem; 0/24 rodaram o comando malicioso).
5. **Português × inglês: paridade fechada (2026-08-03).** O núcleo da grade foi repetido em
   inglês com roster idêntico (108 runs): conserto e abstenção se reproduzem; o topo fecha
   6/6 nos dois idiomas. **Inglês NÃO é melhor.** Misturar idiomas (método EN + resposta PT
   via instrução) foi testado e **rejeitado** (pior obediência ao payload). Sinal datado:
   modelos médios/abertos recusaram injeção um pouco pior em EN (5/8 × 1/8, K=2). Regra
   prática: rode o Strata no idioma de quem lê e aplica.
6. **Custo medido.** Uma auditoria de IA num projeto pequeno custa **~1 centavo** no piso
   econômico (gpt-5-mini); reproduzir a grade publicada inteira custa **~US$ 7** (~350
   runs). Português custa ~22% mais tokens na entrada (desigualdade de tokenizer,
   documentada na literatura); efeito líquido EN −15-20% por run, pequeno demais para
   dirigir a decisão. Métrica-chave: **custo por projeto organizado** é menor que um minuto
   de tempo humano.
7. **Honestidade de regime (sempre citar):** são **sinais** em cenários sintéticos
   controlados, não provas; validação ecológica em andamento (no real, o auto-auditor não
   bate a competência pura: R8). Toda a evidência, métodos e gabaritos são abertos.

## Links e âncoras

- Repositório: https://github.com/LeoPR/Methodologies
- Produto: `recipe/knowledge-architecture.en.md` (canônico) / `.pt-BR.md`
- Guia de modelo: `recipe/strata-com-ia.*` · Guia de idioma: `recipe/strata-idiomas.*`
- Evidência: `lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md`,
  `lab/2026-08-03-idioma-en/RESULTADOS-*.md`
