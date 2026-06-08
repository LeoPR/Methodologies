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

## Plano P0 — PROVA DE TETO (a IA mais avançada consegue?) — pedido do dono

**Pergunta:** existe **prova cabal** de que ao menos UMA IA muito avançada aplica o Strata
a um projeto real **sem** o falso-positivo que derrubou os modelos médios/baratos? O dono
roda no máximo **Opus 4.8** (e nem todos terão isso) — então é o **teto** a confirmar.

**Lacuna:** o R8 testou modelos **médios/baratos** (gpt-4.1-mini, haiku, gemini-flash,
deepseek, llama) — **nunca o topo (Opus 4.8)** como participante. Logo não sabemos se o
falso-positivo é **limite de capacidade** (some no topo) ou **do modo auto-auditor** (vale
até no topo).

**Método (automatizável, limpo):**
- Participante: **`anthropic/claude-opus-4.8`** via OpenRouter (confirmado disponível) —
  instância **fresca**, fora desta conversa (não viu o gabarito). (E/ou o `claude.exe` do
  dono, mesmo Opus 4.8, como segunda via.)
- Alvos: os 3 digests reais — com ênfase em **NNN (exemplar = controle de falso-positivo)**
  e **pdf2md (problemas reais claros)**. Braços: **baseline + AN**, N=2.
- Juiz: **gpt-4.1-mini (não-Claude)** do R6 — evita o viés Claude-julga-Claude.

**Interpretação:**
- Se Opus 4.8 tem falso-positivo **<<** os médios (que deram 4.4-4.9 no NNN) **E** acha os
  problemas reais → **prova de teto positiva**: *uma IA avançada consegue; o desafio é
  orientar as menores.*
- Se Opus 4.8 **também alucina** ~5 no NNN → o problema é o **modo auto-auditor**, não a
  capacidade — e nem o topo salva sem mudar a forma (reforça H-E/forma/modo).

**Confirma também** se o Opus 4.8 "executa em todas as condições" (bom/exemplar/messy) —
os 3 tipos de projeto cobrem isso. **Custo:** Opus é mais caro (~$2-4 a rodada); confirmar
antes de disparar.
