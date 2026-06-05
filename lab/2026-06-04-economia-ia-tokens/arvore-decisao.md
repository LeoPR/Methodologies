---
title: Árvore de decisão de ambiente — rascunho conceitual
created: 2026-06-04
status: rascunho (confrontado por 6 arquétipos × 15 movimentos, workflow wdoc3jreq)
relates: [mapa-recursos-llm.md, plano-experimental.md, STAGE2/3/4.md, hipotese-visao.md]
---

# Árvore de decisão de ambiente — rascunho

> Como um dev monta o ambiente IA ótimo partindo de estados diferentes. Cada
> "movimento" (ligar X) foi **confrontado** contra 6 arquétipos de ambiente; a
> camada (T0-T5) codifica **em quantos ambientes ele sobrevive**. Tudo apoiado na
> evidência medida (Estágios 1-4). É o rascunho da recipe — ainda lab, não produto.

## Os 6 arquétipos de ambiente

| ID | Persona | Hardware | Plano | Prioridade | Gargalo |
|---|---|---|---|---|---|
| **A1** | Do-zero iniciante | 8GB RAM, iGPU/GPU fraca, sem CUDA útil | Free→Pro | simplicidade | **física + conhecimento** |
| **A2** | Intermediário sem GPU | 16GB, sem GPU NVIDIA útil | Copilot Pro | simplicidade | sem VRAM local |
| **A3** | Power-user, projeto grande | GPU 16-24GB | Max+API+Copilot | performance | complexidade |
| **A4** | Corporativo travado | varia | Enterprise (locked) | conformidade | **policy (DLP/egress/sem-admin)** |
| **A5** | Orçamento apertado, GPU gamer | GPU 8-12GB | Free | economia | teto de qualidade |
| **A6** | Qualidade acima de tudo | GPU forte | Max+API frontier | qualidade | banda de revisão humana |

## As camadas (confrontadas, não opinadas)

O confronto revelou um fato forte: **só 3 movimentos são T0 universais.** O resto
depende do estado da máquina.

### T0 — SEMPRE-GANHA (liga sem perguntar, só ensina o dev) — sobreviveu aos 6
- **M1** Contexto enxuto: incluir só o que tem relevância **causal**; descartar
  distratores. ("Enxuto" = sem ruído, NÃO = poucos tokens a qualquer custo.)
- **M2** Info crítica no início/fim do prompt (lost-in-the-middle); no-op inofensivo
  em prompt <1k ou autocomplete FIM.
- **M4** Right-size do raciocínio (thinking on/off por dificuldade); o limiar é
  parâmetro do perfil, mas o movimento ajuda em todos.
- **Universais de fundo**: output custa 2-6× input; K-quants > legados; decode é
  memory-bound → diagnosticar prefill(TTFT) vs decode(TPOT); esforço é VETORIAL
  `{TTFT, TPOT, throughput, $/tarefa, fit-VRAM}`, nunca escalar.

### T1 — BAIXO-RISCO-DESCONHECIDO (o dev não sabia; ligar é quase sempre bom)
- **Perfil de ambiente legível por agente** (o "deixar a ferramenta ciente") — risco
  ~nulo, ganho provável; o dev raramente sabe que existe.
- **Git desde o dia 1** + `.gitignore` básico (rede de segurança vs "medo de quebrar").
- **`.github/copilot-instructions.md` + content-exclusions + `@workspace` deliberado**
  — melhora muito a resposta, risco nulo.
- **Curadoria humana de `@files`** antes de enviar (não despejar o workspace inteiro).
- **Cross-check entre labs frontier** no problema crítico (A3/A6) — 2ª opinião barata
  onde o custo do erro >> custo do token.

### T4 — DEPENDENTE-DO-ESTADO (a maioria!) — com pré-condição observável
Resumo do confronto (todos quebram em ≥1 arquétipo → NÃO são universais):

| Mov | Pré-condição (gatilho observável) | Quebra em |
|---|---|---|
| M3 cache de prefixo | backend expõe o prefixo (API/Claude Code/Max OU local) | A1/A2 (Copilot abstrai o cache) |
| M5 autocomplete inline | **Copilot pago** (Pro+) ativo | A5 (Free = cota, não ilimitado) |
| M6 chat multiplier-0 | Copilot Pro/Ent com GPT-4.1/5-mini habilitados | A5; condicional A4 |
| M7 preferir mult-0 a Sonnet | regime=créditos E prioridade≠qualidade | **A6** (degradaria) → `default=off` |
| M8 venv/cache fora do sync | sync + volume não-sync + permissão junction | A4 (GPO); overkill A1 |
| M9/M10 Ollama+Continue local | GPU ≥8GB livre + pode instalar | A1/A2 (física), A4 (policy) |
| M11 Claude Code → Ollama | GPU + modelo **tool_use=PASS** (llama3.1:8b) + aceitar ~20 t/s | A1/A2/A4; marginal A5 |
| M12 subagent=haiku | Claude Code + regime Anthropic + fan-out real | inerte A1/A2/A5, bloq A4 |
| M13 visão local pré-filtro | GPU + modelo -vl que cabe + tarefa=OCR/extração | A1/A2/A4; bypass se raciocínio visual fino |
| M14 instrumentar tokens | regime discreto variável (USD/quota) + log parseável | inútil A1/A2/A5, bloq A4 |
| M15 cap contexto ≤16k | GPU **8-12GB WDDM** ativa | **re-medir se ≥16GB** (16k vira teto artificial) |

### T5 — BLOQUEADO-POR-RESTRIÇÃO (policy, não física)
Em A4 (corporativo): bloquear M8-M14 locais/agênticos; **falta de capacidade → escalar
ao IT**, nunca contornar. Ativar só T0 + M5/M6 (se a org habilitou).

## A árvore (heurística, detect → rotear)

```
ETAPA 0  APLICAR KERNEL T0 (M1,M2,M4 + universais)        # sempre, sem perguntar
ETAPA 1  DETECTAR: gpu{none,<8,8-12-WDDM,16-24} · plano{none,free,pro,ent}
         · anthropic{none,max,api} · pode_instalar · sync · prioridade(perguntar)
ETAPA 2  GATE-MESTRE CONFORMIDADE: se !pode_instalar →
         bloquear local/agêntico/parser/junction; ativar T0 + Copilot; escalar ao IT; FIM
ETAPA 3  RAMO LOCAL (gpu utilizável + instalável):
           8-12GB → M15 (≤16k) + M9/M10 (qwen2.5-coder:7b); agente? M11 só llama3.1:8b
           16-24GB → NÃO capar em 16k → RE-MEDIR sweet spot; M11 viável; M13 se OCR
ETAPA 4  RAMO CLOUD/COPILOT:
           pago → M5 (inline ilimitado) + M6 (chat mult-0) + M7 (se prioridade≠qualidade)
           free → autocomplete real = local (se há GPU); faísca cloud p/ caso difícil
           anthropic max/api → M3 (cache) + M12 (se fan-out) + M14 (se log)
ETAPA 5  HIGIENE DISCO: sync+volume+permissão → M8 (+ .gitignore no mesmo passo); senão C:\dev
ETAPA 6  CALIBRAR M4 pela prioridade: qualidade→thinking ON; economia/simplicidade→off; performance→crítico ON
```

## O cobertor curto (alocação de Pareto por prioridade)

Não se maximiza performance + economia + simplicidade + qualidade + privacidade ao
mesmo tempo — competem pela mesma VRAM/banda e pelos **3 regimes de custo não-fungíveis**.

| Prioridade | Ganha | Sacrifica |
|---|---|---|
| **Simplicidade** (A1/A2) | setup-zero, responsivo (nuvem não pesa o laptop) | privacidade, teto de qualidade, independência de internet |
| **Economia** (A5) | $0 + privacidade (local 7B@16k) | topo de qualidade, folga de contexto (penhasco), agêntico multi-arquivo |
| **Performance** (A3) | melhor resultado no caminho crítico | complexidade (multi-tier), $+quota |
| **Qualidade** (A6) | melhor resposta possível (frontier) | economia, simplicidade; gargalo vira revisão humana |
| **Conformidade** (A4) | segurança/data-residency | tudo que exige instalar/egress |

**Regra do cobertor**: T3-economia verdadeira (cache quente, M3) é o RARO que não
conflita com qualidade — por isso é quase-universal. M7 NÃO é T3 verdadeira (economiza
quota mas pode degradar) → some em A6. **"Grátis" depende do regime**: o que é grátis
em créditos custa em USD; somar os três como bolsa única é o erro estrutural.

## Conceitos novos que o seu framing adiciona (dignos de estudo/confronto)

Fundindo a minha leitura inicial com o que o confronto destilou:

1. **Regimes de custo não-fungíveis** (USD-metada / quota-janela-5h / créditos-Copilot)
   como dimensões **discretas que não se somam**. "Grátis" vira relativo-ao-regime.
   *Confronto futuro*: a aritmética de conversão — quando vale gastar quota pra poupar USD?

2. **As camadas T0-T5 como teste de DURABILIDADE sob refutação multi-ambiente.** Em vez
   de "boa prática" (atemporal), cada conselho ganha um tier que codifica **em quantos
   ambientes sobrevive e onde quebra**. É um teste de falseabilidade aplicado a conselho
   de engenharia — **candidato a virar metodologia genérica** (e a realimentar o Strata).

3. **Cobertor curto = alocação de Pareto explícita por prioridade declarada.** A árvore
   não busca "o melhor setup" — busca "o melhor setup DADA a prioridade".

4. **"Deixar a ferramenta ciente" = o ambiente como artefato legível-por-agente.** Move
   a recomendação de prosa-pra-humano para config-executável-por-IA; o agente vira
   participante do roteamento, não objeto passivo.

5. **Gatilho físico (VRAM/WDDM) vs gatilho de policy (egress/DLP) como eixos ortogonais
   de bloqueio.** A1 é limitado por física+conhecimento; A4 por policy. Causas distintas,
   respostas distintas (A1 evolui com hardware; A4 só destrava via IT). Evita prescrever
   "compre GPU" onde o problema é DLP.

6. **Tool_use como propriedade DO-MODELO, não do hardware.** Mais VRAM não conserta
   protocolo: qwen2.5-coder:7b FALHA tool_use em qualquer GPU; llama3.1:8b/qwen3:14b
   PASSAM. Separa capacidade-de-protocolo de throughput.

## Estratégia de simulação (validar a árvore sem ter as 6 máquinas)

1. **Perfis sintéticos parametrizados**: espaço cartesiano das variáveis-gatilho
   (gpu × plano × anthropic × pode_instalar × sync × prioridade). Rodar a árvore sobre
   cada célula; verificar que todo perfil cai numa folha e nenhum recomenda movimento
   cuja pré-condição ele viola (assert por Mx).
2. **Teste de refutação por movimento**: para cada Mx, confirmar que `breaks_in` bate
   com a saída da árvore (regressão automatizável).
3. **Aos olhos das documentações**: cruzar cada número com a fonte oficial; o que **medimos**
   e a doc não diz (sweet spot 7B@16k=55t/s, TTFT 68ms, qwen-coder FAIL tool_use, penhasco
   WDDM) é "medido, fonte=este estudo" — mais forte que doc.
4. **Perfis-fronteira** (stress): A4-lite (Foundry homologado), A5-Ada (4060Ti 16GB:
   re-mede sweet spot?), A1-sem-sync (M8 vira no-op), A3-jogos-roubam-VRAM.
5. **Roofline (honestidade epistêmica)**: números de A3 extrapolados da única máquina
   medida (3060) via roofline → marcar "a-confirmar", **nunca "medido"**. A autoridade vem
   da execução no HW real — a recipe instrui o dev a **re-medir** antes de cravar.
6. **Loop de calibração**: cada perfil real que roda o protótipo realimenta os limiares
   (16k e 8GB são **parâmetros**, não constantes).

## Próximo
- Protótipo `prototipo/detect_env.py` (detect-and-recommend) — ver pasta.
- Depois: destilar a recipe portável a partir deste rascunho + dados dos Estágios.
