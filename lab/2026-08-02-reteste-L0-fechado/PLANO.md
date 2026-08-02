---
title: PLANO — Reteste do Strata contra o L0 fechado (perspectiva temporal)
created: 2026-08-02
updated: 2026-08-02
status: executado 2026-08-02 (ver NOTAS-shakedown e OPINIAO-DE-USO)
---

# PLANO — Reteste do L0 fechado: núcleo → gerais → brands → manual

## 1. Contexto e a tese temporal

O L0 fechou editorialmente em 2026-08-01 (ciclo P1–P5 + V1/V2). O corpus v1
(`lab/2026-06-04-strata-hipoteses/`) testou um L0 de **12 seções**; o fechado
tem **11 + §11 novo (classificação)** — variável nova declarada desta rodada.

Tese do dono (2026-08-02): as conclusões **negativas** do corpus eram limitadas
pela tecnologia de junho (llama3.1:8b, qwen2.5-coder:7b, deepseek-r1:8b,
qwen3:8b). A prateleira local de hoje é outra (Qwen3.6-27B denso,
Qwen3.6-35B-A3B MoE, Llama 4 Scout 17B, gpt-oss 20B). **Conclusão negativa
datada não se refuta pelo calendário — se retesta.** E: os testes contínuos
alimentam o **manual datado (L2/Órganon: `OPINIAO-DE-USO.md` + Parte III §1)**,
nunca o L0 — o Strata seria executável por um humano, mais devagar.

## 2. Tabela temporal — o que é candidato a reteste

| Conclusão do corpus | Era tecnologia da época? | Destino |
|---|---|---|
| F4-local negativo (zero PASS; local 4-8B destrói/obedece) | **Sim** (8B de junho) | **Reteste #1** |
| Recusa lexical do fraco (F3 cai sob paráfrase) | Provável | Reteste c/ 17-27B |
| §9: nenhuma forma torna modelo fraco proporcional | Provável | Reteste |
| F5/web: alucinação sem web; exploratório | Sim (tool-use amadureceu) | Reteste |
| "Método+topo de uma vez; econômico = etapas+humano" | Fronteira entre tiers moveu | Remediar datado → manual |
| §5-fix, §3-tombstone sólidos (âncora mecânica, α=0,918) | **Não** | Não retestar por calendário |
| Falhas de instrumento (leakage, juiz único) e os ❌ da retroativa | **Não** (defeito de método) | Nunca reabrir |

## 3. Matriz `[2026-08]` — instalada e verificada (2026-08-02)

Ambiente medido: RTX 3060 12GB; ollama com `qwen3.6:27b` (17GB, q4_K_M — roda
com offload parcial GPU+CPU, lento — confirmado pelo dono), `qwen3.6:35b-a3b`
(23GB, MoE 3B ativos), `qwen3:14b` (9,3GB — **maior que cabe inteiro na GPU**),
`qwen3:8b` e `deepseek-r1:8b` (ponte temporal — têm resultados no corpus);
chave OpenRouter presente.

| Tier | Modelo | Papel |
|---|---|---|
| local-ponte | `qwen3:8b`, `deepseek-r1:8b` | **controle temporal** — separa "mudou o modelo" de "mudou o instrumento (L0 12→11+§11)" |
| local-prático | `qwen3:14b` | maior sem offload (rápido; o que cabe num dia comum) |
| local-possível | `qwen3.6:27b` | o mais capaz que roda (lento; hipótese: sanha o negativo F4-local) |
| local-MoE (opcional) | `qwen3.6:35b-a3b` | hipótese velocidade×qualidade (3B ativos); 1 célula-curiosidade |
| cloud-econômico | `gemini-2.5-flash` (OpenRouter) | ponte cloud do corpus; centavos |

Lista **congelada por rodada** (não perseguir release; tier×vendor×geração
datada — disciplina herdada). Tiers médio/topo/cloud só na fase "brands" (§6).

## 3.2. A grade de estratos de acesso × escala de capacidade (2026-08-02, dono)

**Pergunta-mãe única** (substitui a fatiada Q1–Q4 — superseded, ver NOTAS):
*qual a combinatória de modelos/tipos/quantizações que fecha a experimentação —
norma, bordas, brands — e que o usuário lê como "na minha máquina ou plano vai
funcionar?"*

Três princípios (a forma cientificamente defensável):

1. **Amostragem estratificada pelo contexto do usuário** — os estratos são os
   contextos de acesso (classe de GPU, faixa de plano), não o espaço de
   modelos. Cada linha da grade responde diretamente ao usuário.
2. **Pontos de fronteira + centro** (lógica de calibração) — mede-se onde a
   curva vira (piso, joelho, topo) + a norma; os degraus intermediários se
   interpolam e a interpolação é **declarada** no manual.
3. **Campeão-por-estrato, desafiante só com razão** — quantização é
   fator-ponte medido (27b q4 local = fp8 nuvem, K=1), não dimensão varrida.

**Regra de fechamento da experimentação:** todas as linhas medidas; piso
delimitado (funciona × quebra); joelho localizado; 1 ponto por brand no tier
consagrado; ponte de quantização medida; topo-controle fechando a prova
funcional. Fechamento = cobertura do espaço de acesso; significância (K
grande, flip-rate) só nas células decisivas, fase seguinte.

**A grade** (medição por linha: f4-dup [norma] + f4-clean [borda-abstenção] +
f4-trap [borda-adversarial, só piso/12GB/24GB/topo] × strata+baseline × K=2):

| Contexto do usuário | Campeão medido | Classe |
|---|---|---|
| <4GB (laptop fraco/CPU) | llama-3.2-1b → 3b (até quebrar) | piso absoluto |
| 4-8GB | gemma-3-4b + qwen3-8b ✓ | piso real |
| 12GB (3060) | qwen3-14b ✓ + gpt-oss-20b | norma popular |
| 16GB | qwen3-32b | norma alta |
| 24GB | qwen3.6-27b ✓ + 35b-a3b | topo local |
| 48GB+ / Mac | gpt-oss-120b | saturação local |
| Cloud econômico | gemini-2.5-flash ✓ + deepseek-v3.2 + gpt-4.1-mini + haiku-4.5 | brands |
| Cloud topo (controle) | sonnet-5 + gpt-5 + gemini-3.1-pro | prova funcional |

✓ = coberto pelo núcleo em curso. Incremental: ~120 runs, $6-12.
Juiz: disciplina F0 (bake-off cross-vendor; topo da grade = candidato, nunca
por decreto).

## 4. Shake-down (passo 1, executado 2026-08-02 — ver NOTAS-shakedown)

- **GOLD-gate**: `verify_f4.py --selftest` → **GOLD 100% (2026-08-02)** ✓
- **Fumaça**: `f4-dup × qwen3.6:27b × K=1`, braço Strata, label `f4s-dup-strata`
  (prefixo `f4s-` = shake-down 2026-08), num_ctx 20480 / num_predict 5000 —
  mede tempo real/run no 27b com offload e confirma o pipeline ollama→scorer.
  **Papel duplo**: também é a âncora nuvem×local da classe 12GB (§3-bis).
- **Núcleo** (depois do fumaça): `f4-dup/trap/clean` × {27b, 14b, 8b-ponte,
  flash} × {strata, baseline} × K=2 → depois família s05 (F3), s01/s04, f6.
  Critério de saída: os oráculos discriminam como o corpus registrou (strata >
  baseline; GOLD discrimina) **e** o 27b é medido onde o 8B zerava.

## 3-bis. Estratégia nuvem×local — capacidade × viabilidade (2026-08-02)

Decisão do dono: usar os créditos OpenRouter (medido: **$33,18 livres**) para
simular os modelos que cabem em cada classe de GPU, sem sacrificar a GPU local.
Separação de perguntas:

- **Capacidade do modelo** (o que ele entrega com o Strata) → medida na
  **nuvem**: volume, K maior, brands — ~1-2¢/run, segundos por run.
- **Viabilidade operacional** (tok/s, offload, latência) → **probes locais
  âncora** + literatura de hardware (ex.: 27b = 4,3 tok/s na 3060 12GB).
- **Confound declarado**: nuvem serve fp8/bf16, local roda q4_K_M — a
  quantização pode superestimar a capacidade. Mitigação: **ponte nuvem×local**
  — 1-2 células âncora por classe nos dois lados (27b = âncora 12GB-offload;
  qwen3:14b = âncora 12GB-cabe; qwen3:8b = ponte temporal). Divergência =
  efeito-quantização medido, reportado no manual.

Tabela GPU→surrogate (verificada em `/api/v1/models`, 2026-08-02):

| Classe GPU | Cabe bem | Surrogate OpenRouter | ~$/run |
|---|---|---|---|
| 8GB | qwen3-8b, gemma-3-12b Q4 | `qwen/qwen3-8b`, `google/gemma-3-12b-it` | <0,01 |
| 12GB (3060) | qwen3-14b, llama-4-scout Q4, gpt-oss-20b | `qwen/qwen3-14b`, `meta-llama/llama-4-scout`, `openai/gpt-oss-20b` | ~0,01 |
| 16GB | gpt-oss-20b, mistral-small-24b Q4 | `openai/gpt-oss-20b`, `mistralai/mistral-small-3.2-24b-instruct` | ~0,01 |
| 24GB | qwen3.6-27b, qwen3-32b, gemma-3-27b, qwen3.6-35b-a3b | todos no OR | 0,01-0,02 |
| 48GB+ / Mac | gpt-oss-120b, llama-3.3-70b | `openai/gpt-oss-120b`, `meta-llama/llama-3.3-70b-instruct` | <0,02 |

## 5. Regras herdadas (não negociáveis)

Gabarito pré-registrado antes de ver saída · fixtures hash-congeladas
(`.fixture-hash`) · juiz cross-vendor (nunca Claude único, nunca OpenAI-small) ·
scorer mecânico com GOLD-gate · falso-zero por truncamento → INDETERMINADO ·
ADR-006: acurácia × precisão em colunas, k e K publicados, distribuição no
regime de uso (não caçar temperatura) · campeões-por-eixo (não combinatória) ·
**o L0 não se retoca com dado de teste** — falha do L0 vira achado registrado
para o próximo ciclo editorial (separação calibração/validação) · K pequeno =
direção, não significância.

## 6. Depois do shake-down (ordem de alavanca)

1. **Reteste dirigido** da tabela §2 (F4-local → F3-encoded → §9 → F5-web).
2. **Dívidas baratas**: gabarito s04 (bug `docs-reproducao.md`); re-pontuar
   rodadas ecológicas com 2º juiz cross-vendor.
3. **Brands**: matriz tier×vendor×geração datada (a matéria-prima do manual).
4. **Degrau 3**: célula texto→agente (tool-use real em sandbox) — viável hoje
   com tool-call nativo dos modelos novos.
5. **Manual**: atualizar `OPINIAO-DE-USO.md` (esqueleto já existente) com o
   desfile por tier — o que cada faixa entrega, com que limite; datado,
   re-verify-by, **sem tocar o L0**.

## 7. Custos e limites declarados

Local = grátis e lento (27b com offload: tempo/run medido no fumaça; se
proibitivo, o peso local cai no 14b e o 27b vira célula-chave). Cloud =
centavos por matriz pequena (checar `/api/v1/credits` antes de matriz grande).
K=2 é fumaça/direção; medição oficial exige K maior + flip-rate (ADR-006).
Grupo 2 das alavancas (ouro humano em escala, transferência agêntica em massa)
segue **fora de alcance solo** — não prometido nesta rodada.
