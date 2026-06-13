---
title: Arquitetura de testes e evidências do Strata — o que comprova, em que condições (macro)
created: 2026-06-13
status: vivo. F0-F4 (nuvem) + F3 (local) fechados; F4 (local) em curso; F5/F6 fronteira.
---

# Como o Strata foi testado — e o que a evidência mostra

> Documento **macro**: a ideia abstrata por trás dos testes e o que eles mostram. Os números
> granulares e as ressalvas finas vivem nos `RESULTADOS-*` linkados. O **método** está em
> [`recipe/knowledge-architecture.md`](../../recipe/knowledge-architecture.md) — aqui é sobre a
> **validação** dele. Tudo abaixo é **sinal/indício**, não prova (ver *Regime e limites*).
>
> **Sem familiaridade com os termos?** (modos M0-M4, *fixture*, *completion-only*, *fail-closed*,
> *tombstone*, como ler *N* / *concordância*) — há um glossário em português claro no
> [`GLOSSARIO.md`](../../GLOSSARIO.md), seção *Termos de avaliação e teste*.

## Duas perguntas
1. O **núcleo (L0)** é fundamentado? — questão de *fundamentação*.
2. Uma **IA consegue aplicar** o Strata, e o método **ajuda**? — questão *empírica*.

## Camada 1 — o núcleo é fundamentado (não é experimento)
O L0 (12 princípios) foi consolidado contra **22 fontes primárias** + varredura de atemporalidade,
e a estratificação por **durabilidade** tem precedente canônico (*pace layering*, Brand 1999;
*shearing layers*; Gartner 2012). Etimologia e fontes no [`GLOSSARIO.md`](../../GLOSSARIO.md). Isto é
**estabelecido**, não medição. O L0/L1 **independe de tecnologia** — um humano com tempo aplica tudo,
com ou sem IA.

## Camada 2 — a IA aplica? A escada de modos (M0-M4)
O que se **testa** não é "o Strata funciona" (o L0/L1 já se sustenta), mas o que é **automático por
IA** (a camada L2). Decompusemos o "engajamento" da IA numa escada — cada degrau é uma tarefa diferente:

| Modo | Pergunta que isola | Estado | Detalhe |
|---|---|---|---|
| **M0** — abstenção/§9 | "devo agir aqui? quanto? (não-agir é resposta válida)" | fechado | [RESULTADOS-f1-m0](RESULTADOS-f1-m0-abstencao.md) |
| **M1/M2** — compreensão | "entende o método e o projeto?" | parcial | [P7](RESULTADOS-p7-camadas-entender-aplicar.md) |
| **M3** — diagnóstico | "o que está errado / o que faria?" | exaustivo (L0) | série R/P |
| **M3.5** — recusa (F3) | "recusa obedecer uma ordem maliciosa lida do projeto?" | fechado (nuvem+local) | [RESULTADOS-f3](RESULTADOS-f3-recusa.md) |
| **M4** — execução (F4) | "produz o fix sem destruir rastreabilidade?" | nuvem fechado; local em curso | [RESULTADOS-f4](RESULTADOS-f4-execucao.md) |

## Como medimos — a disciplina (por que dá pra confiar nos sinais)
- **Cego:** planos anonimizados; pontua-se sem saber o modelo (evita viés de marca).
- **Juízes cross-vendor:** ≥2 de **empresas diferentes** (Google + OpenAI), **não-Claude**. Empresas
  distintas ⇒ vieses independentes; **convergência = robustez** (não é artefato de um avaliador). O F0
  estabeleceu isso; o F4 teve **92%** de concordância inter-juiz.
- **Mecânico onde dá > juiz:** preferimos teste **objetivo** (regex de sinais com *gold-gate*, parse de
  config, **sobrevivência-de-conteúdo**, `git`, asserções) ao julgamento. O juiz só refina o **resíduo**
  que a mecânica não fecha. Todo verificador tem um **GOLD self-test** (casos-disfarce) como portão.
- **Confundidores controlados** (os erros que já nos morderam): falso-zero por **truncamento/thinking**;
  **"seguro e inútil"** (silêncio ≠ recusa); **paranoia** (controles limpos + ação legítima atestada);
  **efeito-método** isolado por **braço baseline**; **fixtures com hash congelado** (anti-drift).
- **§6 (honestidade):** onde o regex confunde *citar* com *propagar*, dizemos e mandamos ao juiz; onde o
  N é pequeno, dizemos. Resultados são reportados como **direção**, não cravo.

## Regime e limites (ler antes de citar números)
- **Completion-only:** o modelo **produz/recusa em TEXTO**; não roda ferramentas. Mede-se a *disposição
  do plano/fix* — **não** o agente real agindo. Um modelo pode escrever fail-closed e, com ferramentas,
  agir diferente (ou vice-versa).
- **N pequeno** por célula (2-3 runs); **1-2 cenários-mãe** (sintéticos + 1 digest real); ladder de
  modelos enxuto (nuvem barata→forte + locais, estes **ruidosos** — pequenos não emitem o formato).
- ⇒ As conclusões valem como **direção forte**, não prova; **generalizar pede mais cenários**.

## O que a evidência mostra (macro)
- **F0 — a fundação (juízes):** juízes de empresas diferentes **convergem** ⇒ as conclusões não são
  artefato. "Maior" **não** é automaticamente "melhor juiz" (um *flash* barato rivaliza com modelos de
  topo); os **OpenAI-pequenos são lenientes** (maus juízes).
- **F1/M0 — abstenção:** a **forma** (framing) corrige o falso-positivo na raiz; a **capacidade** calibra
  (só o topo discrimina "já-bom" de "precisa-de-ponto").
- **F3 — recusa:** com o Strata, modelos recusam de forma **principiada e espontânea** uma injeção lida
  do projeto; o **barato vira de obedecer → recusar**; **0 falso-alarme de ameaça** (não inventou injeção
  onde não havia); a "segurança" do modelo fraco é **em parte lexical** (cai sob paráfrase).
- **F4 — execução:** o Strata **habilita** o conserto correto (fonte única, §5) e **preserva** o histórico
  (*tombstone*, §3) + **fail-closed na execução**; **mas induz super-engenharia** no modelo fraco (ele
  *alucina* defeitos para agir) — **só o topo se abstém** no projeto já-bom.

## A tese (o fio que atravessa tudo)
> **A forma corrige o viés; a capacidade calibra.** O Strata leva a IA a fazer a coisa certa — recusar o
> malicioso, consertar o defeito, preservar o histórico — e o ganho **se concentra no degrau fraco** nas
> tarefas positivas. Mas o **julgamento de proporcionalidade** (§9 — *quando NÃO agir*) depende da
> **capacidade** do modelo, não da forma. Conclusão prática: **método + modelo de topo** (de uma vez),
> ou **método + humano no loop / orientação em etapas** para os demais.

## Fronteira (aberto, honesto)
- **F4 local** (em curso) · **F5** (com/sem ferramentas inverte o ranking de capacidade?) · **F6**
  (temporalidade/longitudinal — ver [dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md)).
- **2º cenário-mãe** (hoje quase tudo deriva de um) e **validade de agente-com-ferramentas-reais** (sair
  do completion-only) são os dois maiores limites a atacar.
- Roadmap: [`PLANO-geral-modos-fechar-lacunas.md`](PLANO-geral-modos-fechar-lacunas.md).

## Índice da evidência granular
Desenhos: [DESIGN-f3](DESIGN-f3-recusa.md) · [DESIGN-f4](DESIGN-f4-execucao.md) (+ `*-synthesis.json`).
Resultados: [F1/M0](RESULTADOS-f1-m0-abstencao.md) · [F0 juízes](RESULTADOS-f0-confronto-juizes.md) ·
[P7 camadas](RESULTADOS-p7-camadas-entender-aplicar.md) · [F3](RESULTADOS-f3-recusa.md) ·
[F4](RESULTADOS-f4-execucao.md). Hipóteses/índice: [`README.md`](README.md).
