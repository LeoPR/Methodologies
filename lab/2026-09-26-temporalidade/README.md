---
title: 'Temporalidade: estudo próprio (LLMs e documentação)'
created: 2026-09-26
updated: 2026-09-27
status: 'Aberto. Fase: ontologia v0 + protótipo; nada medido contra modelo.'
tags: [temporalidade, perecibilidade, llm, documentacao]
---

# Temporalidade

Pergunta: por que LLMs (e agentes) erram com o tempo, e que método ajuda a errar menos?
Frente separada do Comporta (economia de recursos) e ligada ao §6 do Strata (perecibilidade).

**Enquadramento do dono (2026-09-26).** Temporalidade não é olhar datas (`getdate()` + busca).
É **inferir a ordem pelos estados**: um estado é consequência lógica de outro, então vem depois,
mesmo sem timestamp ou com timestamps trocados. Exemplo: pessoa no ar de paraquedas; entrando no
avião; no ar se preparando para saltar → embarque, voo, salto, paraquedas abre. E, quando falta um
elo, **perceber que falta** e buscar antes de concluir. Há testes humanos disso; IAs vão mal, e o
erro apareceu nas próprias conversas deste projeto.

Camadas (da mais rasa à mais profunda):
1. Relógio: contagem de um processo periódico; datas, corte, perecibilidade.
2. Ordem sem relógio: causalidade, pré-condições, "aconteceu-antes".
3. Construção da ordem: scripts, modelos de situação, inferência de ponte, sensação de tempo.
4. Metacognição: notar a lacuna e decidir buscar.

A revisão de LLMs cobre sobretudo a camada 1. O mapa amplo (quatro mapas + síntese) cobre as quatro.

- [REVISAO-LITERATURA.md](REVISAO-LITERATURA.md) (camada 1: datas e defasagem em LLMs): 55 fontes primárias; consenso, controvérsias,
  lacunas. Lacuna central: nenhum protocolo de processo para fato perecível foi avaliado.
- **[ONTOLOGIA.md](ONTOLOGIA.md): comece por aqui.** Ontologia v0 (primitivas, relações, regras, o que
  cabe em computação), construída sobre os mapas 1–8. Demonstrador em [prototipo/](prototipo/README.md).
- [MAPA-5-fisica.md](MAPA-5-fisica.md): Aristóteles a Page–Wootters; ordem causal, causal sets, seta.
- [MAPA-6-matematica.md](MAPA-6-matematica.md): teoria da ordem, instantes de eventos, ramificado,
  sistemas de transição, bitemporal, estruturas de eventos.
- [MAPA-7-ontologias-formais.md](MAPA-7-ontologias-formais.md): OWL-Time, PROV, BFO, DOLCE, Vendler,
  Moens & Steedman, Galton, VerbNet, FrameNet.
- [MAPA-8-computacao-aproximacoes-e-limites.md](MAPA-8-computacao-aproximacoes-e-limites.md): limites
  (TC⁰), representações internas, modelos de mundo, neuro-simbólico, memória de agente.
- [SINTESE-mapa-amplo.md](SINTESE-mapa-amplo.md): síntese dos mapas 1–4. Junta os quatro mapas; lacunas e
  hipóteses de método (não testadas).
- [MAPA-1-artefato-e-ordem-formal.md](MAPA-1-artefato-e-ordem-formal.md): relógio, Lamport, Allen,
  STRIPS, cálculo de eventos, causalidade.
- [MAPA-2-filosofia-e-cognicao.md](MAPA-2-filosofia-e-cognicao.md): McTaggart, percepção e memória do
  tempo, scripts, modelos de situação, causa e ordem, desenvolvimento.
- [MAPA-3-testes-humanos.md](MAPA-3-testes-humanos.md): Picture Arrangement, Story Completion, teoria
  da mente, scripts em lesão frontal, inferência-ponte.
- [MAPA-4-IA-ordem-estado-lacuna.md](MAPA-4-IA-ordem-estado-lacuna.md): IA ordenando sem data, por
  estado, e detectando lacuna.
- [PRECOS-E-VALORES-VOLATEIS.md](PRECOS-E-VALORES-VOLATEIS.md): o mesmo problema dentro dos nossos
  documentos (preço, tok/s, s/run inline). Práticas de terceiros e proposta; nada aplicado ainda.

Casos próprios documentados: DeepSeek V4.1 em GB10
(`../2026-06-04-economia-ia-tokens/instrumento/STAGE5.md`); eixo `f5-recente` do banco
(`../2026-09-26-banco-modelos/`).
