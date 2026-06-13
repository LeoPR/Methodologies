---
title: 'Revisão retroativa — a técnica de análise evoluiu; o que dos resultados antigos sobrevive, enfraquece ou caiu'
created: 2026-06-13
status: 'AUDITORIA do próprio corpus. Aplica os padrões novos retroativamente. Anota, não reescreve (§3/§8).'
---

# Revisão retroativa do corpus Strata

> Conforme aperfeiçoamos a **técnica de análise**, achados antigos podem ter ficado **obsoletos ou errados**.
> Esta é a auditoria que reavalia tudo contra o **padrão atual** — e fixa o **"ótimo até o momento"** (campeão)
> como ponto de partida, evitando re-testar tudo-em-tudo. Fonte da opinião atual: [`OPINIAO-DE-USO.md`](OPINIAO-DE-USO.md).

## A técnica que evoluiu (a régua nova — contra a qual auditamos)
1. **Juiz cross-vendor** (≥2, empresas diferentes), nunca **Claude único**; nunca OpenAI-small (leniente). *(F0)*
2. **Scorer mecânico (regex) é FP-prone** → precisa de **GOLD-gate** + **juiz** no resíduo; nunca regex cru. *(F3/F4)*
3. **Falso-zero por truncamento/thinking** — marcar INDETERMINADO; conferir `stop_reason`. *(deepseek +0,50→−1,50)*
4. **Completion-only ≠ agente** com ferramentas — não transfere ao produto.
5. **Circularidade**: projeto+gabarito do próprio dono (gabarito provou-se **incompleto**) → exige **braço externo**.
6. **Gabarito gênero-consciente**: baixa-conformidade **≠ defeito** (lista/pesquisa não precisa de CI/tests).
7. **Falso-positivo é FRAMING-dependente** (ache-problemas over-detecta; abstenção sub-detecta) — não inerente.
8. **N pequeno** (nenhuma célula N≥5) → tudo é **sinal**; só deltas-grandes-vs-ruído.
9. **Custo = duplo propósito**; vocabulário **relativo** no relatório.
10. **Rastreabilidade datada / append-only** (o hub) — anotar, não reescrever.

## Status retroativo por achado (✅ sobrevive · ⚠️ enfraquecido · ❌ obsoleto/errado · 🔁 re-analisar)
| Achado / doc | Status agora | Por quê (régua nova) | Correção |
|---|---|---|---|
| **F0** juízes cross-vendor | ✅ **sobrevive** (é a fundação) | É a própria régua nº1; 3 empresas convergem | nenhuma — vira a base |
| **F1/M0** abstenção | ⚠️ enfraquecido, **direção confirmada** | juiz **Claude único**; mas o **braço externo REPLICOU** (forma corrige FP, super-corrige em sub-detecção) | número single-judge é sinal; a **direção está externamente validada** |
| **P4 / datas §8 ~33%** | ❌ **over-claim derrubado** | "~33% em todos os tiers" era **média com variância enorme** (gemini=100%, vários=0%), juiz único, pior concordância (0,56) | **não é achado** — vira **hipótese F6**; a "tese-mãe" da temporalidade está **rebaixada** |
| **P6** free-local | ✅ sobrevive (já auto-corrigiu o truncamento) | só single-judge | "sem free-local confiável" mantém; ⚠️ juiz único |
| **P7** camadas | ⚠️ enfraquecido | N=1, 1 prompt, juiz único | "entender não é a barreira" = **sinal**, não "todos os tiers" |
| **R8** ecológico (real) | ⚠️ **reinterpretado** (maior impacto retroativo) | a over-detecção é **FRAMING** (audit), **não falha inerente** — o **braço externo** mostrou que a forma de abstenção corrige; + **circularidade** | R8 vira "*o framing ache-problemas over-detecta, até no real/baseline*", não "Strata falha no real". Reler com a lente de framing |
| **reteste-limpo** R0-R4 | ⚠️ enfraquecido | local-only, juiz único, nuvem pendente | o efeito grande (prosa **piora** o óbvio: P1 8→4) **sobrevive**; o resto = sinal |
| **F3/F4** (estados mecânicos crus) | ✅ **corrigido** | eram FP-prone (cita≠propaga) | já **resolvidos** com GOLD-gate + juiz + guarda de FP. Vereditos finais valem |
| **Dossiê temporalidade** | ⚠️ **reenquadrado** | a "tese-mãe" é o sinal **mais ruidoso** | continua **hipótese registrada** (estudar via F6); **não** "o argumento de valor mais forte" |

## Os "ótimos até o momento" (campeões — ponto de partida, não re-testar tudo)
Em vez de combinatória (tudo×tudo), mantemos um **campeão por eixo**; testes novos são **desafiantes vs o campeão**:
- **Juiz:** gemini-2.5-flash + gpt-4.1 (cross-vendor). *(Desafiante só se houver suspeita de viés conjunto.)*
- **Scorer:** GOLD-gated + juiz no resíduo. *(Nunca regex cru de novo.)*
- **Forma do método:** densa/curta AI-nativa para o degrau fraco; prosa para o topo.
- **Tier por tarefa:** econômico p/ consertar §5/§3; **forte/humano** p/ abster (§9).
- **Fixtures:** hash-congelado; **sintético (validade interna) + externo (circularidade) + gênero-consciente**.
- **Achados-campeão (sólidos):** §5-fix e §3-tombstone por execução. Tudo o mais = **sinal**.

## O que RE-ANALISAR (sem re-rodar tudo) — prioridade
1. **P4/datas e a "tese-mãe":** já rebaixada aqui; **não citar os ~33% como achado** em lugar nenhum. *(feito neste doc; anotar P-docs.)*
2. **R8:** reler sob a lente de **framing** (não "Strata falha no real", e sim "o framing ache-problemas over-detecta"). Anotar.
3. **Células de juiz-único decisivas** (F1/M0, reteste-limpo, R8): **2º juiz cross-vendor** quando/se re-rodadas (P2 do backlog) — re-análise barata sobre dados existentes onde houver raw.
4. **Genre-consciência:** o messy externo é inconclusivo sem gabarito por gênero — não cravar sub-detecção lá.

## Conclusão da auditoria
Nada do **núcleo sólido** caiu (§5-fix, §3-tombstone, F0). O que **caiu/rebaixou** foi **over-claim**: a tese-mãe
da temporalidade (❌ como achado) e a leitura de R8 (⚠️ reinterpretado como framing). A direção geral
("a forma corrige o viés; a capacidade calibra") **sobreviveu e ganhou validação externa**. O corpus está
**mais honesto e menos inflado** — e agora com **campeões** definidos para não re-testar tudo-em-tudo.
