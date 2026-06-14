---
title: ADR-005 — Duplicação de conteúdo entre docs: fonte única proporcional (apontar, não propagar)
status: aceito
date: 2026-06-14
scope: disciplina de documentação da oficina — dogfood de §5/§3/§9 do Strata; não é conteúdo de uma metodologia
---

# ADR-005 — Apontar, não propagar: como tratar texto repetido entre os docs

## Contexto

Os docs públicos re-contam os mesmos fatos e teses por audiência: o `README.md` (visão),
o `recipe/README.md` (como aplicar), a `OPINIAO-DE-USO.md` (opinião honesta) e o
`strata-modo.svg` (gancho visual). Surgiu a pergunta: **como o Strata trata isso?** Toda vez
que um texto muda, ele teria que propagar para os outros, exigindo rastreabilidade ou
interdependência? Ou isso é exagero para um repo solo que vai estabilizar?

Uma auditoria (2026-06-14: mapa de duplicação + três lentes — §5 purista, §9 pragmático,
doutrina-Strata) achou **drift já materializado**, não hipotético:

- contagem de linhas: `~840` no README/recipe, mas o arquivo tem **834** (e um registro de
  lab cristalizou **658**) — três valores para o mesmo arquivo;
- tamanho: `53KB` na guidance, real ≈ **54,5KB**;
- `updated:` do produto estagnado em 2026-06-04, apesar de edições reais em 06-13/14;
- exemplos do L1 divergindo em seis vias (`OAIS` só no README; `FAIR, IMRaD` no resto);
- o absoluto `"só o topo (Opus)"` apagando a exceção gpt-4.1 que a OPINIAO mede.

A premissa "sou dev, dificilmente altero depois" foi **falsificada pelo próprio working tree**.

## Decisão

**O §5 não diz "não repita texto". Diz que todo conhecimento tem uma representação
autoritativa única — e autoridade única não é o mesmo que instância única.** Re-expressar
por audiência (Diátaxis) é legítimo **se a cópia aponta para a fonte e não finge ser a fonte**.

O método já traz o **teste de admissão mecânico** que separa os dois casos:

- **"Se eu apagar isto, regenero a partir do artefato?"** Se **sim**, é fato volátil derivável
  (linhas, KB, SHA). Não deve estar inline: vira ponteiro, ou some.
- **"Este texto basta para refazer o porquê?"** Se **sim**, é narrativa-tese (a assinatura,
  "capacidade ≠ validade", "rascunho a revisar"). Guarda-se curto e replicado, porque o
  produto precisa viajar sozinho (§10).

O **§3** separa **traço** de **superfície**:

- **traço** (append-only, não se corrige): os snapshots de lab ("658 linhas / SHA F678F235")
  são o estado datado do que foi testado. Divergir do arquivo atual é a função deles.
- **superfície** (rebaixar ativamente o que morreu): `~840`, `53KB`, `updated:` defasado. O
  método manda consertar.

**Postura adotada:** apontar, não propagar; consertar a superfície, não o traço; crescer só
quando a dor pedir. Em níveis (escada proporcional do §9):

- **Nível 1 — cirurgia de superfície:** apagar/corrigir os literais defasados. **Aplicado.**
- **Nível 2 — ponteiro em vez de cópia:** estender o padrão que já existe vivo no hub
  `ARQUITETURA-E-EVIDENCIAS.md` (seção *Estado das fases — fonte única*) (que se declara fonte canônica e pede que os demais
  apontem). Adotado como hábito, sem ferramenta.
- **Nível 4 — build/transclusão/CI: RECUSADO.** Para ~12 docs pequenos é o "excesso de §9 por
  outro eixo" que o próprio §9 do produto nomeia. Reabrir só se o corpus crescer e a dor de
  sincronizar virar contínua.

## Consequências

- Nível 1 aplicado (commit `89f16da`): contagem de linhas e `53KB` removidos; `updated:`
  corrigido para 2026-06-14; o absoluto `"só o topo"` suavizado (SVG → "ex. Opus"; recipe/README
  registra a exceção gpt-4.1); lista L1 marcada como não-exaustiva.
- O hub `ARQUITETURA-E-EVIDENCIAS.md` (seção *Estado das fases — fonte única*) é a **fonte canônica** do estado de evidências; os
  demais docs apontam, não repetem o literal.
- **Convenção nova:** ao editar o produto, bumpe o `updated:` do frontmatter (entrou no
  checklist do `AGENTS.md`). É a proteção barata contra o único drift que reincidiu.
- Os números de seção do produto são **identificadores imutáveis** (§8): adições por sufixo
  `-bis` (§3-bis, §6-bis), nunca renumerar. Por isso o §9 (a régua de proporção) não vira §1,
  mesmo sendo aplicado primeiro — número é ID estável, não ordem de leitura.
- O que foi **deixado como está** (§9 — não driftou ou é re-narrar legítimo): a vitrine do
  README (já hedada), os números `22 fontes / 92% / 5-7` (consistentes), e o mini-glossário do
  recipe (já aponta ao GLOSSARIO).

## Alternativas consideradas

- **Propagar à mão para todos os docs:** rejeitado — é a própria doença que gerou o drift.
- **Build/transclusão/CI de geração:** adiado/recusado — over-engineering para o tamanho atual.
- **Nada fazer:** rejeitado — o custo de não-agir já foi pago (afirmações públicas erradas num
  projeto cuja tese-produto é rastreabilidade e fonte única).
