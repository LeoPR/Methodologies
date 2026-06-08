---
title: P0 — prova de TETO (Opus 4.8) — a IA avançada aplica o Strata a projeto real?
created: 2026-06-08
setup: anthropic/claude-opus-4.8 (fresco via OpenRouter, fora desta conversa) × NNN + pdf2md × baseline+AN × N=2 · achados VERIFICADOS contra os arquivos reais (não por juiz)
status: PROVA POSITIVA — capacidade resolve; o falso-positivo dos médios é limite de capacidade, não do modo
---

# P0 — o teto existe: Opus 4.8 aplica o Strata a projeto real, e bem

Pergunta do dono: existe **prova cabal** de que ao menos UMA IA muito avançada aplica o
Strata a um projeto real **sem** o falso-positivo que derrubou os modelos médios? Resposta:
**sim.** E a evidência é **verificada contra a realidade** (conferi as afirmações do Opus nos
arquivos), não por um juiz — a forma mais forte.

## O que o Opus 4.8 fez (NNN exemplar + pdf2md)

- **Achou problemas reais VERIFICADOS** que os médios perderam e que **eu (o gabarito)
  perdi**:
  - NNN: 3 contagens de teste conflitantes no `STATUS.md` (**2070 / 2043 / 2145**, todas
    como atuais) → §5; e `pyproject` diz `github.com/leona/nnn` vs README/AGENTS
    `github.com/LeoPR/nnn` (**mesmo fato, dois valores**) → §5. **Conferido: ambos VERDADE.**
  - pdf2md: cravou as duplicatas `-DESKTOP` (§5), a versão `0.1-dev` vs `0.7.0` (§5/§8),
    e mais reais (PHILOSOPHY.md em dois lugares; `src/*-DESKTOP-*.py` duplicados).
- **Reconheceu o que é BOM** (não alucinou): NNN §2/§4/§6-bis "PASSA com folga"; distinguiu
  uma divergência **sinalizada** (privilege levels com ⚠ + doc de reconciliação = cumpre o
  espírito) de uma **não-sinalizada** (= viola). **Não flagou os 3 arquivos-IA como §5.**
- **Evitou as armadilhas**: prescreveu **tombstone, NÃO apagar** (não caiu em N1) e
  **priorizou por §9** (o de maior risco × menor custo: o conflito de fonte).
- **Recusou inventar**: "não dá para saber, declaro não invento" onde faltavam arquivos.

## O veredito (recalibra o R8)

| modelo | em projeto real | mecanismo |
|---|---|---|
| médios/baratos (R8: gpt-4.1-mini, haiku, gemini-flash, deepseek, llama, qwen) | **alucinam** (falso-positivo ~4.5/plano; criticam o bom; perdem os reais) | **limite de CAPACIDADE** |
| **topo (Opus 4.8)** | **aplica EXCELENTEMENTE** (acha os reais, reconhece o bom, prioriza, não inventa) | **capacidade suficiente** |

**Conclusão:** o Strata **funciona** como auto-auditor de IA — **com um modelo de topo**. O
falso-positivo do R8 é **limite de capacidade dos modelos médios**, não um defeito do modo
auto-auditor em si. A pergunta "como orientar a IA" **se divide**:
- **Modelo de topo (Opus-class):** o método funciona **como está**.
- **Modelos médios/baratos:** precisam de **orientação** (aplicação em etapas H-E, forma
  anti-falso-positivo P1, ou humano-no-loop) para chegar perto.

## Honestidade (importante)
- **Meu gabarito do R8 estava INCOMPLETO.** O Opus achou §5 reais no NNN que eu classifiquei
  como "≈ exemplar, ~zero problemas". Ou seja: nem o estabelecimento da base-de-verdade
  (feito por mim, lendo rápido) foi perfeito — o Opus, fresco e cuidadoso, foi mais rigoroso.
  Isto **fortalece** "o Opus é genuinamente bom" e tempera a confiança no gabarito do R8.
- **Caveat:** N=2; 2 projetos; "Opus 4.8" via OpenRouter pode diferir do Opus do Claude Code
  do dono (ambos topo). Custo da rodada ~$3.
- **Nem todos terão Opus 4.8** (ponto do dono) — por isso P1/P2/P5 (orientar os menores)
  seguem valendo, agora com um alvo claro: **fazer o modelo médio se comportar como o Opus**
  (achar real, reconhecer o bom, não inventar, situar no tempo — H-D).
