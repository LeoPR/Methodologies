---
title: R8 — síntese dos 3 projetos reais (pdf2md, NNN, FG2P) — validade ecológica
created: 2026-06-08
setup: AN-v2/prosa/baseline × 4 sabores nuvem × N=2, por projeto · pontuação CEGA contra base-de-verdade real estabelecida por leitura · digests gitignored (privados)
status: VEREDITO ECOLÓGICO — o Strata como auto-auditor de IA NÃO generaliza p/ projetos reais
---

# R8 — o Strata-auto-auditor encontra a realidade

Três projetos reais, três "temperaturas" de organização. Pergunta: o método (Strata) faz
um modelo **diagnosticar melhor um projeto real** do que a competência pura (baseline)?

## Os 3 projetos

| projeto | tipo | resultado por braço | veredito |
|---|---|---|---|
| **pdf2md** | bom, com 2 problemas reais claros (duplicatas -DESKTOP, versão) | baseline achou ambos com **0 alucinação** e priorizou; AN/prosa acharam **menos** e **alucinaram mais** (AN 1.0/plano) | método **PIOROU** |
| **NNN** | **exemplar** (~0 problemas; navegação rica, fonte-única, ADRs) | **TODOS** alucinaram muito (baseline 4.88, prosa 4.75, AN 4.38 falso-pos/plano); método reconheceu o-bom **menos** (0.12-0.25 vs 0.38) | framing "ache problemas" **falha**; método não resgata |
| **FG2P** | messy/antigo (sem índice, docs misturado, dicts dup, legacy) | genuínos: baseline 1.38 / prosa 1.62 / AN 1.5 (empate); alucinação 1.6-2.4 em todos; **0.75 criticaram coisas boas** | método **≈ baseline** (não ajudou) |

## A conclusão (dura e honesta)

1. **Em projeto real, o Strata como auto-auditor de IA NÃO bate a competência pura.**
   Piorou no pdf2md, empatou no FG2P, e no NNN todos (inclusive baseline) alucinaram.
2. **A falha dominante é FALSO-POSITIVO / super-crítica** — atravessa os 3 projetos e os 3
   braços: os modelos **inventam violações** e **criticam práticas boas** (CHANGELOG,
   QUICKSTART, .gitignore decente, o padrão fonte-única-com-ponteiro). O prompt "ache
   problemas" induz isso; o método não corrige e às vezes piora.
3. **A hipótese "ajuda onde é denso" NÃO se confirmou.** Mesmo no FG2P messy, o método mal
   passou do baseline — acharam o problema óbvio (sem-índice) e alucinaram o resto.
4. **Contraste com o sintético:** no fixture com problemas **densos, limpos, mapeados a §**,
   a AN ajudava muito. O salto NÃO sobrevive ao real, onde os problemas são esparsos/
   ambíguos e há boas práticas + **conteúdo histórico que o modelo não situa no tempo (H-D)**.

## Por que (mecanismo provável)

- **"Não consigo dizer que está tudo bem":** pedir "ache violações" num projeto limpo faz o
  modelo **fabricar** problemas (sycophancy de tarefa). É o **§9 (economia/proporcionalidade)
  sendo violado pelos próprios modelos** — eles não aplicam "às vezes o certo é não achar nada".
- **Temporalidade (H-D):** em projeto real há decisões superadas, notas históricas,
  duplicatas antigas. O modelo, sem orientação temporal, marca o **superado/antigo como
  problema atual** → falso-positivo. (Ver `~/Documents/NOTA-onedrive-git-observacao.md`: a
  própria análise comprimiu 2 anos num "agora".)

## Implicação de produto (a recalibração)

- **O Strata vale como CHECKLIST que um HUMANO aplica com julgamento**, não como IA marcando
  violações sozinha. O modo auto-auditor é **propenso a falso-positivo** em projeto real.
- O que PODERIA salvar o auto-auditor (futuro): um prompt/forma que (a) **permita "nada a
  corrigir"** explicitamente, (b) mande **situar no tempo antes de julgar** (H-D), (c)
  **reconheça o que já é bom** antes de procurar falha. A testar — não validado.

## Caveats
- N=2 por célula × 4 sabores; 3 projetos (1 bom-com-issues, 1 exemplar, 1 messy).
- "genuíno vs alucinado" é julgado por um juiz Claude contra a base-de-verdade que **eu**
  estabeleci lendo cada digest — há subjetividade; mas o padrão (alucinação alta + crítica
  ao bom em **todos** os braços/projetos) é consistente e forte.
- Digest = camada de organização curada por mim (não o projeto inteiro).

## Veredito
**O sucesso do Strata no benchmark sintético NÃO se traduz em projeto real.** Como
auto-auditor de IA, ele gera ruído (falso-positivo) em projetos reais — sejam bons, sejam
messy. **Isto reposiciona o produto:** Strata = método + checklist humano; o auto-auditor
de IA é um caminho de pesquisa em aberto (depende de resolver falso-positivo e H-C/H-D),
não um claim. É o achado mais importante de todo o reteste.
