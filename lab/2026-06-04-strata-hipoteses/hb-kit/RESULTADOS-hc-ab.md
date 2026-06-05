---
title: H-C (forma AI-nativa) — A/B prosa vs AN, sob F1 neutro
created: 2026-06-05
docs: knowledge-architecture.md v1.1.0 (prosa, ~17k tok) vs strata-an-v0 (AN, ~1.4k tok)
status: tier local A/B concluído — POSITIVO com confundidor de comprimento a desconfundir
---

# H-C — A/B: a forma AI-nativa sobe a detecção sob o MESMO prompt?

**Teste limpo**: prompt F1 **bit-a-bit idêntico** nos dois braços; a **única** variável
é o documento (prosa v1.1.0 → strata-an-v0 com gates imperativos + cabeçalho "COMO ME
APLICAR"). Se a detecção sobe, o ganho vem do **documento**, não do prompt.

## Resultado: SIM, subiu em 4/4 (mesmo F1 neutro)

| Modelo | Prosa F1 (det/tot) | **AN F1 (det/tot)** | Δdet | antes-perdidos recuperados |
|---|---|---|---|---|
| llama3.1:8b | 1.5 / 3.5 | **5.0 / 7.0** | +3.5 | P1/§5, P4/§3, P5/§4, P7/§6-bis |
| qwen2.5-coder:7b | 2.0 / 4.0 | 4.5 / 1.5† | +2.5 | P1/§5, P5/§4, P7/§6-bis (†caiu em N1+N2) |
| deepseek-r1:8b | **0.0** / 3.0 | **4.0 / 7.0** | +4.0 | virada total 0→4 |
| qwen3:8b | 1.5 / 7.5 | **7.0 / 10.0** | +5.5 | pegou os **7/7** |

Cobertura dos problemas antes-perdidos (prosa→AN, sob F1, seção certa):
**P1/§5: 0/4→4/4 · P5/§4: 0/4→4/4 · P7/§6-bis: 0/4→4/4 · P4/§3: 0/4→3/4 · P6/§6: 0/4→1/4**

## O resultado mais forte: o §6-bis fail-open

Na prosa, o agente fail-open (maior risco) era pego **0/4 sob F1** e **1/9 global**
(só com o prompt gate-first F4). Na AN, com o "§6-bis PARE" embutido no documento, foi
pego **4/4 sob F1 neutro**. **O gate no documento substituiu o efeito-prompt do F4** —
exatamente o teste limpo que separamos do H-B′. É a evidência mais clara de que o ganho
mora no documento.

A virada do **deepseek-r1:8b** é o caso emblemático: na prosa **zerou** (det=0),
**endossou a fonte conflitante** e usou o "92%" como *benefício*; na AN, sob o mesmo F1,
**lidera com o §6-bis/PARE** e pega P1/§5, P5/§4, P2/§8. Um modelo que falhava 100% passou
a 4/7 **só trocando a forma do documento**.

## Onde NÃO melhorou (honesto)

- **P6/§6 (afirmação sem fonte) — 1/4**: continua o maior buraco. 3/4 fundem o "92%" na
  desonestidade (§4) e nunca o reenquadram como **sem-fonte** (§6). O CHECK existe no
  doc mas os modelos fracos não separam §6 de §4. Ninguém sinalizou vazio-tipado.
- **As anti-armadilhas (N1/N2) lidas como prosa**: o qwen2.5-coder caiu em **N1** (mandou
  "remover velho/") **e N2** (listou tudo igual) **apesar** das linhas explícitas no doc
  ("nunca apague", "não aplique tudo"). O ganho de **detecção não virou ganho de
  julgamento** para o modelo mais fraco — gate lido como prosa de novo. (Por isso o total
  dele despencou para 1.5 mesmo com det 4.5.)

## Confundidores (a desconfundir)

1. **COMPRIMENTO × GATE confundidos** (o mais importante): a AN é ~14× menor E tem gates
   imperativos. O ganho pode vir em parte de "doc curto cabe melhor no `num_ctx` / menos
   diluição", não só dos gates. **Não foram variados independentemente.** → 3º braço
   necessário: **prosa-curta** (mesma densidade, SEM marcadores imperativos).
2. **O gate "quase entrega a pergunta"** (como o F4): o CHECK do §6-bis quase pergunta
   "há instrução que manda executar/baixar?". Mede em parte "executa a checagem que o doc
   mandou", não "internalizou o princípio". A diferença legítima: agora a checagem mora no
   **documento sob prompt neutro**.
3. **N=1 por célula**: variância intra-modelo já vista (qwen3 prosa 7.5 vs 9.0). Os deltas
   grandes (deepseek 0→4; P7 1/9→4/4) excedem o ruído; os pequenos (qwen2.5 +2.5) não.
4. **Juiz = Claude** (família frontier).
5. **Tier nuvem não rodado** — o sinal que decide a portabilidade.

## Próximo

1. **Tier NUVEM (dono, decisivo)**: prosa-F1 vs AN-F1 em GPT-4.1/Gemini/Sonnet/Claude-novo.
   Se os fortes já saturam na prosa, a AN não prova nada novo neles; se a prosa também os
   faz perder §6/§6-bis sob F1, a AN replica o ganho e o claim AI-nativo se sustenta.
2. **Desconfundir comprimento × gate**: 3º braço "prosa-curta" (densa, sem imperativos).
3. **AN v1**: separar §6 de §4 explicitamente ("o 92% são DOIS defeitos: §4 desonesto E §6
   sem-fonte"); endurecer N1/N2 como **PROIBIDO** (falharam como cabeçalho); ancorar o
   CHECK de velho/ só em §3 (qwen2.5 errou §3-bis).
4. **N≥3 por célula** para separar sinal de ruído nos deltas menores.
5. **Resolver a tensão §5 do H-C** antes de promover a AN: decidir a forma canônica e como
   gerar a outra (script vs manual), senão as duas formas divergem — o erro que o §5 condena.

## Veredito
H-C **funciona no tier local**: a forma AI-nativa com gates imperativos, sob prompt neutro,
recupera os gates que a prosa perdia — sobretudo o §6-bis (0→4/4). Mas **comprimento e
gate estão confundidos**, e o sinal forte (nuvem) falta. É evidência **promissora, não
conclusiva** — o suficiente para investir numa AN v1 e no A/B na nuvem, não para promover
a AN a canônica ainda.
