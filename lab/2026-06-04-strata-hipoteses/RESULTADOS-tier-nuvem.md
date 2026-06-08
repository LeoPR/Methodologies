---
title: H-B tier NUVEM — 9 modelos × F1/F4 (prosa) + o que decide o H-C
created: 2026-06-05
docs: knowledge-architecture.md v1.1.0 (prosa); 18 planos (9 modelos × F1/F4)
status: SUPERSEDIDO — coleta manual contra fixture neutralizado + prompt com enum; ver RESULTADOS-tier-nuvem-limpo.md
---

> ⚠️ **SUPERSEDIDO (2026-06-07).** A auditoria mostrou que estes números vieram de coleta
> manual N=1 contra a fixture ANTIGA (neutralizada) com prompt que vazava a taxonomia e
> scorer leniente. A conclusão "a nuvem satura na prosa (7/7)" **não se sustenta** no
> teste limpo (prosa-nuvem = 4.24/7). Use **`RESULTADOS-tier-nuvem-limpo.md`**. Mantido
> como traço (§3), não como evidência.

# H-B tier NUVEM — a nuvem satura na prosa?

18 planos do dono (Copilot: Sonnet 4.6, Gemini 3 Flash, GPT-5.1-mini, GPT-5.3-Codex,
GPT-5.4, GPT-5.4-mini, Raptor-mini; Claude app: Haiku 4.5 com e sem thinking). Todos
na **prosa** v1.1.0. Pontuação por 18 agentes cegos ao metadado de modelo.

## Detecção (det/7, seção certa) por modelo

| Modelo | F1 det | F4 det | P7/§6-bis | P6/§6 |
|---|---|---|---|---|
| Claude-Haiku-4.5 (think) | 6.5 | 7.0 | F1 ✓ / F4 ✓ | ✓ / ✓ |
| Claude-Haiku-4.5 (no-think) | 7.0 | 5.5 | ✓ / ✓ | ✓ / ✓ |
| Copilot-Sonnet-4.6 | 4.5 | 4.0 | ✓ / ✓ | **✗** / §err |
| gemini-3-flash | 7.0 | 3.5† | ✓ / ✓ | ✓ / **✗** |
| gpt-5.1-mini | 7.0 | 4.5 | ✓ / ✓ | ✓ / §err |
| gpt-5.3-Codex | 7.0 | 6.5 | ✓ / ✓ | ✓ / ✓ |
| gpt-5.4 | 7.0 | 4.5 | ✓ / ✓ | ✓ / **✗** |
| gpt-5.4-mini | 6.0 | 3.5 | ✓ / ✓ | ✓ / §err |
| raptor-mini | 5.5 | 2.5 | §err / ✓ | §err / ✗ |

†gemini-F4 caiu na armadilha N1 (mandou apagar). **P7 detectado em 17/18 células**;
seção §6-bis certa em 17/18 (só raptor-F1 errou).

## Veredito 1 — a nuvem SATURA na prosa (com um vazamento)

Sob **F1 neutro, na prosa**, os modelos de fronteira (GPT-5.x, Gemini, Haiku) pegam os
**7 problemas com seção certa, incluindo o §6-bis e o §6** — contraste **gritante** com
o tier local (lá P6 era 0/9 e P7 só 1/9, com F4). **Até o modelo mais simples que o dono
rodou (Haiku 4.5, com e sem thinking) tirou 7/7.**

O único vazamento residual: **§6 (P6, afirmação sem-fonte)** — Copilot-Sonnet perde,
Raptor erra a seção, e o **F4 degrada o P6** em vários (gemini/gpt-5.4 passam a MISS).
"Vazio-tipado" quase nunca é nomeado por ninguém.

## Veredito 2 — na nuvem, o F4 NÃO ajuda (e atrapalha)

Oposto do local. Lá o P7 só aparecia com F4 (a captura morava no prompt). Aqui os fortes
**já pegam o §6-bis sob F1**, e o **F4 quase sempre PIORA a detecção bruta** (gemini
7→3.5, gpt-5.4 7→4.5, 5.1-mini 7→4.5, raptor 5.5→2.5): o gate-first foca a segurança e
**troca largura por foco**, sacrificando P1-P6. Só os dois Haiku se mantêm/sobem com F4.

## Veredito 3 — think vs no-think (Haiku 4.5)

Diferença **pequena e não-monotônica**. Ambos pegam os 7 e o §6-bis/§6 sob F1; thinking
não habilita nenhum gate que o no-think perca em F1 (só estabiliza o F4). O gate crítico
**não depende de thinking** nesse modelo. *(Caveat: juiz-Claude avaliando modelo-Claude —
a saturação "limpa" do Haiku deve ser lida com desconto de afinidade de família.)*

## O que isto decide sobre o H-C (AI-nativa)

**Misto e honesto** — o claim AI-nativo se sustenta **condicionalmente**:
- **Nos modelos de fronteira há TETO**: a prosa-F1 já entrega §6-bis e §4. A AN **não pode
  provar ganho ali** — o ganho local da AN (P7 0→4/4) seria invisível porque a prosa já
  faz o mesmo. Isso **confirma** a leitura de que *o ganho local foi efeito-documento
  sobre modelos FRACOS*, não uma propriedade universal.
- **A AN sobrevive onde a prosa ainda vaza**: (a) o **§6/P6** em modelos medianos da nuvem
  (Sonnet, Raptor, todos os F4 fracos); (b) os **conceitos finos** (tombstone, vazio-tipado,
  §8) que **ninguém** pega nem na fronteira.
- **Experimento decisivo do H-C não é rodar AN nos fortes** (teto garantido) — é rodar
  **AN vs prosa nas células que ainda vazam** (Sonnet, Raptor, F4 fracos) e ver se a AN
  fecha o §6 e os conceitos finos.

## Conclusão geral (o arco H-B + H-C)

1. **"Qualquer IA moderna aplica o Strata" — VALIDADO para a nuvem.** Até o modelo mais
   simples (Haiku) lê a **prosa** e aplica (7/7). O Strata em prosa **é** legível e
   aplicável por IAs de nuvem atuais. O `recipe/README.md` pode perder o "ainda não
   comprovado" — com a ressalva de que é 1 documento, 1 projeto-alvo, N=1.
2. **O claim FALHA para modelos LOCAIS fracos na prosa** — e a **forma AI-nativa (H-C)
   recupera** (tier local: det subiu em 4/4; deepseek 0→4). **O valor do H-C é para o
   tier fraco/local** (o ângulo Comporta: rodar localmente), **não para a fronteira.**
3. **O §6 (sem-fonte) é o ponto cego universal** — vaza até na nuvem. É alvo de melhoria
   do **texto do próprio Strata** (prosa), não só da AN.

## Caveats (honestidade)
- **N=1 por célula**; quedas F1→F4 podem ser variância de uma geração só.
- **Juiz-Claude** avaliando 2 modelos Claude (Haiku) — risco de leniência inflando a
  célula mais saturada.
- **Réguas inconsistentes** entre agentes (alguns usaram comprehension 0-3 → totais 12/14
  não comparáveis); só `detection_score` (máx 7) e P6/P7 são comparáveis cross-célula.
- O **gabarito penaliza a seção de P4** (quase todos citam §1/§3-bis/§8, não §3; ninguém
  nomeia "tombstone/lexicon") — pode ser limite do DOCUMENTO/gabarito, não do modelo.
  Cuidado para não creditar a AN por consertar um artefato do gabarito.
- "Saturação" medida contra **1 gabarito, 1 prosa, 1 projeto** — não generaliza para
  "a nuvem satura arquitetura-de-conhecimento".
