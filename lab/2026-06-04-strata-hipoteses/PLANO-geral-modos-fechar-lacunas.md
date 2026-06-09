---
title: Plano geral — modos de aplicação por IA (M0-M4) e roadmap para fechar lacunas
created: 2026-06-08
status: roadmap. Revisado por painel adversarial (4 lentes: capacidade/medição, segurança, validade ecológica, completude). Executar incremental.
---

# Plano geral — o que falta testar em "uma IA aplica o Strata"

A escada de profundidade de engajamento, **corrigida e ampliada** pelo painel.

## A escada de modos (revisada)

| Modo | O que é | Cobertura HOJE |
|---|---|---|
| **M0 — Aplicabilidade / ABSTENÇÃO** ⭐NOVO | "este projeto/seção precisa de Strata? devo agir?" — o gate do §9; **não-agir é resposta certa** | nunca isolado — **é a raiz do falso-positivo** (R8) |
| **M1 — Entender o doc sozinho** (cold) | explicar L0/L1/L2, princípios, sem projeto | parcial (sonda P7) |
| **M2 — Entender-em-contexto** | a parte (a) ENTENDIMENTO dos audits | observado (bom em todos), não pontuado isolado |
| **M3 — Opinião/diagnóstico** (textual) | "o que está errado / o que faria" | **exaustivo, mas só L0** (L1/L2 rasos) |
| **M3.5 — RECUSA / fail-closed** (§6-bis) ⭐NOVO | diante de artefato com autoridade/ordem maliciosa, recusa? | nunca como **gate de entrada** na execução |
| **M4 — Execução simulada** (produz o fix) | gerar a mudança concreta (diff/tombstone) | **EXISTE primitivo** (`hb_l2_sandbox.py`: gera artefatos L2 em sandbox+git, score de cobertura) — **falta** fix-de-defeito-conhecido com verificação mecânica |

> **Correção factual (painel):** meu rascunho dizia "M4 = ZERO". Errado — há scaffold pronto
> (`hb_l2_sandbox.py` + `hb_l2_score_external.py`). Reaproveitar, não reconstruir.

## Eixos transversais = CONFUNDIDORES (não fases tardias)

- **Camada (L0/L1/L2):** cada modo é uma tarefa diferente por camada (M3-em-L0 ≠ M3-em-L1). Só L0 a fundo.
- **COM/SEM pesquisa (tools):** **confundidor de 1ª ordem** — "Opus venceu do treino"; um médio+web pode inverter o ranking no L1 (conhecimento). Tudo foi medido num só regime (completion puro).
- **Temporalidade (H-D):** modo longitudinal (reauditar corpus que MUDOU) — o ponto cego ~33% de datas. Ausente (escada é single-shot).
- **Juiz + gabarito:** **a fundação** — todo número de M2/M3/M4 depende dele, e há 2 precedentes de fragilidade (R6 viés de família ~0.87; P0 o gabarito humano estava INCOMPLETO).
- **Sub-detecção / "seguro e inútil":** orientar troca super-crítica por SILÊNCIO (P1+P2). Todo modo deve medir falso-positivo **E** inação — não premiar o silêncio.

## Roadmap (ordem de maior valor — convergência do painel)

**Fase 0 — Blindar a MEDIÇÃO (juiz+gabarito) [barato, dados existentes].**
Re-pontuar os resultados-chave com **2 juízes não-Claude**, reportar só **deltas + concordância**.
Para qualquer gabarito novo, preferir **verificação MECÂNICA** (teste passa/falha, diff aplica,
hash bate, `git log` prova histórico-não-reescrito) a julgamento humano. *Fundação de tudo.*

**Fase 1 — Fechar M0 (ABSTENÇÃO) [barato, usa os 3 digests reais].**
A raiz do falso-positivo. Tarefa: "devo aplicar Strata aqui? onde?" nos 3 projetos reais
(**NNN exemplar = controle de abstenção**). Medir **abstenção-correta como acerto de 1ª classe**.
Ataca diretamente a falha dominante (agir onde não devia).

**Fase 2 — Decouple COMPREENSÃO (M1/M2) por camada [barato].**
Pontuar o ENTENDIMENTO isolado da qualidade do diagnóstico; quiz cold por camada×tier.
Confirma com número: entender é universal; o gargalo é julgamento (L0) e conhecimento (L1).

**Fase 3 — RECUSA / fail-closed (M3.5, §6-bis) [médio].**
Rodar contra o fixture com payload de prompt-injection (`tarefas.txt`/`instrucoes-agente.md`):
ao "arrumar", o modelo **reconhece a autoridade não-verificada e RECUSA**, ou emite um diff que
obedece? Mede fail-closed **na ação**. **Gateia a entrada em M4.**

**Fase 4 — Execução simulada (M4) reescopada [médio-alto].**
Reusar o scaffold. **Fixtures MISTOS + sintéticos-novos (hash congelado):** metade com defeito
plantado (mede correção do fix), metade **limpa** (mede abstenção), + uma **armadilha** onde o
fix intuitivo viola um §forte ("unifique apagando a velha" viola N1/§3 — o certo é tombstone).
**Duas métricas separadas:** correção (objetiva, sem juiz: teste/diff/hash) e segurança
(2 juízes não-Claude: não apagou histórico, proporcional §9, fail-closed). Onde der, sobre os
**digests reais** (ecológico), não só sintético.

**Fase 5 — Confundidor PESQUISA [médio].**
Par com-tools / sem-tools no mesmo modelo médio, em M1-M4. O ranking de capacidade inverte?
(Hipótese P7: ajuda o conhecimento L1, não o julgamento L0.)

**Fase 6 — Temporalidade / manutenção (H-D) [médio].**
Modo longitudinal: reauditar um corpus que mudou (atual→superado). Testa o ponto cego de datas.

## Modos registrados, menor prioridade
Transferência entre projetos · crítica-do-próprio-método (a IA acha lacunas no Strata, ex. H-D)
· ensinar-a-um-humano (o modo assistente-no-loop que o projeto suspeita funcionar).

## Recomendação de início
**Fase 0 + Fase 1 juntas** (ambas baratas, usam dados/projetos existentes): blindar a medição
e fechar a abstenção — porque **toda conclusão depende do juiz, e a falha dominante é não se
abster**. Só então subir para execução (M4), com a recusa (M3.5) como gate.
