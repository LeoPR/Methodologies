---
title: 'Fila geral: backlog PRIORIZADO (só itens abertos)'
created: 2026-06-13
updated: 2026-10-01
status: 'Vivo. Só itens abertos, por prioridade. O que foi feito sai daqui (o git guarda o traço); o estado das evidências está no hub e na OPINIAO-DE-USO.'
---

# Fila geral: backlog priorizado (o que falta, em ordem)

> Só itens **abertos**. O estado do que já foi medido está no [hub](ARQUITETURA-E-EVIDENCIAS.md)
> (tabela *Estado das fases*) e na leitura honesta de uso, [OPINIAO-DE-USO.md](OPINIAO-DE-USO.md).
> O foco atual e as decisões que aguardam o dono estão no [`STATUS.md`](../../STATUS.md).

## P0: antes de mais testes
- **§9 "quando não agir": o A/B da revisão foi inconclusivo (sem poder).** Registro:
  [RESULTADOS-verificacao-s9](../2026-08-03-prompt-ingenuo/RESULTADOS-verificacao-s9.md) (ver o adendo
  de poder). **Aberto (fila por demanda):**
  - repetir com modelos que pontuam e não estão no piso, com N suficiente para poder (o adendo estima
    cerca de 50 runs por braço);
  - o `f6-ruidoso` lê em parte a resposta, como o `f4-clean`, e ainda não tem sucessora limpa.
- **Estudo de idioma (PT×EN): sem diferença detectada; equivalência não demonstrada.** A margem
  pré-registrada (±10 pp) não foi atingida: o resultado é indeterminado. Registros:
  [RESULTADOS-idioma-f3](../2026-08-03-idioma-en/RESULTADOS-idioma-f3.md) e
  [RESULTADOS-f4-en](../2026-08-03-idioma-en/RESULTADOS-f4-en.md). **Aberto (fila por demanda, não bloqueio):**
  - uma rodada inferencial de idioma pede K≥7 para a margem de ±10 pp;
  - o desvio datado da armadilha §6-bis no tier GPU em EN: re-teste dirigido (K≥5 em qwen3-32b e
    gpt-oss-120b) só com motivo novo;
  - células sem EN: framing de caça, eco/digests, F5/F6, Degrau 3.
- **Braço externo: auditoria rica aberta.** A abstenção já rodou em 6 repos de terceiros e em projetos
  publicados (FG2P, com artigo): [externo](RESULTADOS-externo-bemcomportado.md) ·
  [R8](RESULTADOS-r8-sintese-3-projetos.md). **Resta:** levar a **auditoria rica de qualidade** (domínio R8)
  ao terceiro com **gabarito pré-registrado por independente**, **juiz de outro fabricante**, **mais de um
  gênero** (hoje N=1, só pacote Python) e o **gabarito gênero-consciente** que separa sub-detecção de
  "já-bom-para-o-gênero".

## P1: alto valor
- **Firmar os achados do P10 (revisão adversarial, 2026-06-16):** os 4 achados refinados são **direcionais, não
  causais**: o framing gênero-consciente confunde ruído×abstenção. Para isolar: (1) rodar o **TCF-limpo sob o
  framing "ache problemas"** (cruzar ruído × framing); (2) **fixture par-a-par** que varie só a legibilidade do
  tombstone (sem "Lista de Lixo" embutida, sem PII); (3) **múltiplos projetos de terceiros** + gabarito
  gênero-consciente pré-registrado por independente + **juiz não-Claude**. Detalhe em [P10](RESULTADOS-p10-escada-propria-genero.md).
- **Redação clara para IA pode ter estilo próprio (hipótese registrada, a pensar depois):** a clareza para a
  IA talvez peça um texto mais comprimido que a Linguagem Simples humana; o Strata quer ficar pequeno e servir a
  máquina ao mesmo tempo. Inclui: a clareza de redação como complemento do Strata; "tokens completos" como
  possível métrica; uma ou duas superfícies (humana × densa); liga-se ao Comporta (menos tokens = menos custo).
  Detalhe em [IDEIA-redacao-clara-para-ia.md](IDEIA-redacao-clara-para-ia.md).
- **Disciplina de redação como camada de ensino (hipótese registrada, a desenvolver):** o conhecimento de
  como escrever claro (nomear não negar, frase inteira, quebra de linha) talvez possa ensinar: como comentário
  das normas, no "como usar" com exemplos, ou como uma camada L3/L4 de pedagogia acima do L2. Eixo oposto ao da
  compressão para a máquina. Detalhe em [IDEIA-camada-ensino-redacao.md](IDEIA-camada-ensino-redacao.md).
- **Argumentar o JUDGE (a executar):** o dossiê [DOSSIE-judge-justificativa-cientifica.md](DOSSIE-judge-justificativa-cientifica.md)
  reúne o argumento (ideal-regulativo; eixos alinhamento/adequação/herança; modelo centro-ideal-perdido-drift) e a
  literatura. A concordância corrigida por acaso e a ablação do gabarito já estão medidas
  ([concordância](RESULTADOS-concordancia-juizes.md), `eval/strata/verify/calc_stats.py`;
  [juiz sem gabarito](RESULTADOS-juiz-sem-gabarito.md), `eval/strata/judges/judge_f4_ablation.py`).
  **Falta:** os gráficos (scatter objetividade×concordância, escada de juízes, centro/drift, Bland-Altman,
  calibração), PoLL nas células de juiz único, kappa juiz×humano, e a ablação justa (dar a fixture sem o
  veredito). ECE segue bloqueado: o juiz não emite confiança. Reconferir citações antes de uso externo.
- **Strata CURTO AI-nativo (design) + replicar o R4 na nuvem com 2º juiz** (o R4 local mostrou que a
  compressão domina; razão compressão:gates ~2/3:1/3): [reteste-limpo](RESULTADOS-reteste-limpo.md).

## P2: blindar e melhorar
- **Fixity `--verify` (§10):** `eval/strata/gen/hash_fixture.py` grava `.fixture-hash`, e os runners só leem
  o hash gravado; nada recomputa e compara. Adicionar um modo `--verify` chamado no início de `hb_f3`/`hb_f4`.
  Origem: [AUTOAUDITORIA-repo-vs-strata](AUTOAUDITORIA-repo-vs-strata.md).
- **Modelos do Copilot (por demanda):** o GitHub Models foi aposentado em 2026-07-30, inclusive a API de
  inferência (verificado em fonte primária em 2026-09-28). O acesso por script ficou só pelo Copilot SDK,
  que não é OpenAI-compatível, e a política de uso proíbe automação em massa. Vale no máximo para uma
  ponte pequena de células de topo, com fixtures sintéticas. Os mesmos modelos rodam pelo OpenRouter.
- **Fechar a medição:** 2º juiz cross-vendor nas células decisivas que ainda têm juiz único (compressão,
  datas, eco).
- **Posição/saliência da §9:** decisão tomada ([P8](RESULTADOS-p8-posicao-saliencia-s9.md)): não adicionar
  a âncora ao canônico. Aberto só para blindar, baixa prioridade: **2º juiz não-Claude** (remove a
  circularidade Claude-julga-Claude).
- **Eixo de segurança (§6-bis), varredura própria de evidência** (item em aberto do canônico):
  - **Insumo externo, datado:** [`lab/2026-10-01-ferramentas-agentes/`](../2026-10-01-ferramentas-agentes/README.md).
    Consenso de fabricantes e órgãos: prompt injection não está resolvido; a garantia vem de controle
    determinístico fora do modelo; privilégio mínimo.
  - **Do nosso lado:** o ato de **agir** tem medição (F3 recusa, `f4-trap`). O ato de **servir** (entregar
    artefato além da esfera de leitores) ainda não tem.
  - **Próximo:** desenhar uma fixture de "servir além da esfera", com controle de excesso de bloqueio (§9).
- **Temporalidade (F6):** segue como frente própria em [`lab/2026-09-26-temporalidade/`](../2026-09-26-temporalidade/);
  o próximo passo está lá e no `STATUS.md`.

## P3: cobertura e expansão
- **Agentes de mercado (Claude Code, Codex CLI etc.), FASE POSTERIOR declarada (2026-08-02, decisão,
  não abandono):** medir agentes de mercado fica para uma fase seguinte por 3 motivos registrados:
  (1) **confound triplo**: mede modelo + agente (loop/prompt do fornecedor) + ferramentas do fornecedor,
  tudo ao mesmo tempo, e o que queremos isolar é o modelo sob a forma Strata; (2) **custo de licença e
  ambiente**: exige licenças e setup dos CLIs de cada vendor, fora da economia atual do laboratório;
  (3) **a pergunta de transferência já foi respondida** pela célula sandbox própria (Degrau 3,
  `hb_agent.py`, contrato nosso declarado como confound): o padrão texto→execução transfere
  (Strata 10/12 × baseline 2/12 no §5-fix executado). Reabrir só se surgir pergunta que a célula
  sandbox não responda.
- **Decompor L1/L2:** pontuar "nomear formalização" (L1) e "ferramentas datadas" (L2); testar **com-pesquisa**
  num modelo pequeno **bem-calibrado** (onde P7 prevê maior ganho da web). *(Toda a detecção medida é L0.)*
- **Registro/declaração de uso de IA (proveniência §3-bis), REGISTRO, a pesquisar:** normas de publicação
  científica + lei (UE/BR/EUA/propostas) + padrões técnicos (C2PA/SPDX/trailers); camadas por etapa/granularidade/
  artefato; propor 1 padrão **L1** + ADR de encaixe; dogfood no próprio repo. Desenho em
  [`IDEIA-registro-uso-ia.md`](IDEIA-registro-uso-ia.md). *(Pedido do dono 2026-06-14, não executar agora.)*
- **Cenários/gêneros:** PatchCraft (repetir num 2º projeto real de código). Os cadernos de aula
  (AulaQuantum/DeepLearning) já têm sinal direcional no P10; firmá-lo está no P1. Combina com o braço externo.
- **Decisões de design abertas:** exportação/tradução = **corolário L0 curto** (não uma "L3"); arquivo-extra
  **Q&A** L1/L2 **só** se não colapsar em "sempre-ache-problema" (medir pelos controles de abstenção antes);
  **fronteira Strata × Comporta**: rota e custo decididos em 2026-10-01 (a recipe do Comporta absorve; o guia
  do Strata aponta; ver o [PLANO-v2](../2026-06-04-economia-ia-tokens/PLANO-v2.md)); resta encaixar caches e
  setup-de-agente; classificar
  artefatos de ambiente (canônico×regenerável×efêmero) como princípio L0/L1 em satélite L2.
