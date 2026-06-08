---
title: Virada estratégica — de "o Strata funciona?" para "como orientar uma IA a aplicá-lo?"
created: 2026-06-08
status: registro de direção + hipóteses novas (H-E, modo-de-uso) + alvos de visualização
---

# A virada (do dono, 2026-06-08)

O reteste fechou que o **Strata-auto-auditor de uma vez só NÃO funciona em projeto real**
(falso-positivo nos 3 projetos). A conclusão do dono: **o problema não é mais usar o Strata
para fazer o que deve — é descobrir COMO ORIENTAR uma IA para que o faça.** A pergunta de
pesquisa muda de *"o método funciona?"* para *"qual a forma/modo de invocação que faz a IA
aplicá-lo bem?"*.

## Hipóteses / observações novas a registrar

### H-E — Aplicação em ETAPAS (não de uma vez só)
**Ideia (dono):** "o Strata não ajuda para avaliar de uma vez só, mas talvez em etapas."
Em vez de "leia o método inteiro e ache todas as violações" (que induz fabricar), aplicar
**uma seção/gate por vez**, com checkpoint — ex.: (1) mapeie o que há; (2) situe no tempo
(H-D); (3) só então, gate a gate, pergunte "isto viola §X? evidência?". Hipótese: reduz
falso-positivo (foco) e melhora cobertura. Conecta com F3 (seção-a-seção do H-B′) e com o
§9 (proporcionalidade — não despejar tudo).

### Observação — o MODO DE USO importa (assistente vs auto-auditor)
**Dono:** "os modelos que funcionam como auxiliar no VSCode parecem funcionar bem." Ou
seja: **assistente com humano no loop** (interativo, no editor) ≠ **auto-auditor autônomo**
(que alucina). A hipótese: o valor do Strata aparece no modo **humano-conduz / IA-assiste**,
não **IA-decide-sozinha**. Reforça o reposicionamento "checklist humano".

## Perguntas de análise → alvos de VISUALIZAÇÃO (dados já existem)

Temos planos pontuados por problema (P1-P7) que mapeiam a seções, em sintético + 3 reais +
nuvem/local. Dá para montar:

1. **Capacidade por seção/camada (L0/L1/L2):** quais §/camadas os modelos *atendem* e quais
   *falham*. (Ex. já visto: §6-bis fail-open OK no sintético-AN; §6 sem-fonte = ponto cego
   universal; §8/datas = fuzzy. Mapear isso por camada L0/L1/L2.)
2. **Suficiência por modelo:** qual modelo é "bom o bastante" para avaliar — por *tier* e por
   *modo*. (Sintético: gemini-2.5-flash liderou; real: todos alucinam → "suficiente" depende
   do modo/etapa, não só do modelo.)
3. **Sintético × real (a fronteira):** o contraste que explica tudo (denso/limpo vs esparso/
   histórico).

> Status: registrado para visualização e nova estratégia. A próxima rodada deixa de medir
> "o método" e passa a medir **a forma de orientar a IA** (etapas, modo, situar-no-tempo).
> Ver também [[H-D temporalidade]] e o H-C (forma AI-nativa).
