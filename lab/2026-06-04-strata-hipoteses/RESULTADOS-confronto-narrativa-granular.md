---
title: 'Confronto narrativa × evidência granular — reafirmação honesta, lacunas, realidade e envelope de uso'
created: 2026-06-21
updated: 2026-06-21
status: 'AUTO-AUDITORIA. Confronta a narrativa consolidada (OPINIAO/hub/FECHAMENTO) contra os RESULTADOS-* granulares, por confronto adversarial em 8 clusters + crítico de completude. Achado: o núcleo sólido sobrevive; sobram over/under-claims pontuais nos docs de entrega, contradições entre docs a reconciliar, e um viés sistemático de atribuição (rotular falha-do-método como teto-de-capacidade). Tudo aqui é sinal/direção, salvo onde marcado SÓLIDO.'
---

# Confronto: a narrativa consolidada bate com a evidência granular?

> Esta é a auditoria que vira a régua para dentro.
> Pega cada afirmação da [OPINIAO](OPINIAO-DE-USO.md), do [hub](ARQUITETURA-E-EVIDENCIAS.md) e do
> [FECHAMENTO](FECHAMENTO-avaliacao-strata.md) e confronta com o que os `RESULTADOS-*` realmente medem.
> Método: 8 leitores céticos em paralelo (um por cluster), cada um confrontando claim × granular,
> seguidos de verificação adversarial da honestidade e de um crítico de completude.
> É o mesmo gesto do [confronto com a literatura](RESULTADOS-confronto-literatura.md), agora interno.

## 1. Reafirmação honesta — o que sobrevive ao granular

### SÓLIDO (ancorado em ação-de-arquivo + gold mecânico)

- **Consertar defeito §5 conhecido + preservar histórico §3, por execução.** Único sólido do corpus.
  f4-dup/Strata = PASS 6/6 células; baseline NÃO-FIX 6/6. Inter-juiz 92% (vs 56% no F3), por ancorar
  em estado git, não em juízo. Réplica em 3 fabricantes + 2 juízes não-Claude. GOLD-gate 100% contra
  casos-semente. ([F4](RESULTADOS-f4-execucao.md), [escada-claude](RESULTADOS-escada-claude.md))
- **A §3-preservação é o componente MAIS robusto, não par igual da §5.** É o único que replicou de
  sintético para projeto REAL: no eco-pdf2md, sem Strata o gpt-4.1 apagou seções reais (N1 nas 2 runs);
  com Strata, zero destruição. **UNDER-CLAIM a corrigir:** a OPINIAO trata §3 e §5 como pares; a §3 tem
  evidência ecológica que o §5-conserto-completo não tem.

### SINAL (direção real, N pequeno, juiz quase sempre Claude, 1 tarefa/gênero)

- **A FORMA corrige o falso-positivo na raiz; a CAPACIDADE calibra.** FP cai de ~5,4 (AUDIT) para 1,0 (M0).
  **Nuance honesta:** "corrige na raiz" esconde que a mesma forma INTRODUZ o erro simétrico (over-abstenção).
  O honesto é "DESLOCA o viés", que é a própria conclusão do F1/F4.
- **Só o topo discrimina "já-bom" de "precisa" — e mesmo o topo de forma instável (~1/5).** (P8c, SD alto.)
- **P8 REFUTOU posição/saliência da §9** (placebo neutro ≈ canônico; o "8→3 do K=2 era sorte"). Decisão:
  não adicionar âncora ao canônico. Honestidade exemplar.
- **Recusa de injeção §6-bis: o econômico vira de obedecer para recusar.** Medição mais frágil do corpus.
  α=0,467 é FRACO pela própria régua (corte 0,67), não "moderado"; IC inferior 0,252 encosta no acaso.
  A recusa do fraco é LEXICAL (cai sob paráfrase).
- **Assinatura por tier persiste entre gerações** (P9): barato over-age / topo calibra / forma padroniza.
  **OVER-CLAIM a corrigir:** "maior=melhor dentro do fornecedor (robusto)" falha no DeepSeek e a métrica
  0-3 saturou (SD=0, virou contagem-de-invenções). É tendência com exceção, não invariante.
- **Convergir ≠ acertar (a tese negativa, a mais forte do cluster de juízes).** Fase B: juízes cegos caem a
  0,556, abaixo do baseline burro (0,611), e seguem concordando entre si nas respostas erradas. O sólido
  ancora no gold mecânico, não no júri. ([juiz-sem-gabarito](RESULTADOS-juiz-sem-gabarito.md))
- **7 de 9 juízes de 3 empresas convergem na DIREÇÃO; não é "Claude julga Claude".** Ver §3 (correção R6).

### EXPLORATÓRIO (1 fixture, sem réplica)

- **Verificação de fonte na web:** sem web carimba falso como verdadeiro; com web melhora mas ainda revise.
- **Situar no tempo:** acerta com cronologia legível, erra quando o ruído soterra marcadores. A "tese-mãe
  temporal" foi corretamente rebaixada a não-achado.

## 2. Correções que o confronto exige (acionáveis)

Cada uma é deriva entre o granular e o doc de entrega. Marcadas como aplicadas ou pendentes.

1. **R6 / juiz único — APLICADA (ver §3).** "R6 fechou o caveat de juiz único" usa um juiz (gpt-4.1-mini)
   que o F0 posterior achou leniente. O caveat é fechado pelo painel afiado do F0, não pela mini.
2. **§3 acima da §5 na OPINIAO — APLICADA (2026-06-21).** A §3-preservação tem evidência ecológica (replicou no
   real, eco-pdf2md); a §5-completa não. Marcada como o pedaço mais robusto na entrega + na tabela por tarefa.
3. **"robusto" → "tendência com exceção" (maior=melhor por vendor) — APLICADA (2026-06-21).** Falha no DeepSeek
   (Pro ≈ Flash); métrica 0-3 satura. Corrigido na regra prática da OPINIAO.
4. **α=0,467: verbete ancorado — APLICADA + APROFUNDADA (2026-06-21).** Não era só trocar a palavra: as réguas
   discordam (McHugh "fraco" 0,40-0,59; Landis-Koch "moderado" 0,41-0,60; Krippendorff "descartar" <0,667).
   Estabelecido um **padrão de verbetes** em `RESULTADOS-concordancia-juizes.md`: verbete primário é a DECISÃO do
   Krippendorff (confiável/preliminar/insuficiente, casada com o nosso α); adjetivo só com escala citada (McHugh
   adotada); e o lastro forte é o **IC contra o limiar** — o IC de F3 [0,252, **0,653**] está **inteiro abaixo**
   do piso 0,667, então "insuficiente" não é corte arbitrário, é o intervalo todo sob a barra. Bibliografia
   atualizada com a família de réguas + críticas (Feinstein & Cicchetti 1990, Sim & Wright 2005, Gwet).
5. **"habilita o fix" → "habilita nos que não consertam + padroniza nos que consertam informalmente" — JÁ
   no granular (F4 L100-102); a OPINIAO usa "padroniza", que é defensável.** Baixa prioridade, não aplicada.

## 3. A correção do R6 (falha de tombstone §3 no próprio corpus)

A mais importante, e é uma ironia: o corpus Strata cometeu a falha que o Strata existe para evitar.

**A cronologia:**
- R6 (2026-06-07) usou o **gpt-4.1-mini** como 2º juiz não-Claude. Concluiu: a ORDENAÇÃO (AN > prosa >
  baseline) e os DELTAS sobrevivem a um juiz de outra família; mediu o viés de família (~0,87 ponto).
- F0 (2026-06-09) descobriu que o **gpt-4.1-mini é leniente** (FP 1,25, cego ao falso-positivo) e escreveu,
  textual: "*NÃO usar OpenAI-small (nano/mini/4.1-mini) como juiz... Corrige o 2º-juiz fraco que usávamos.*"

Ou seja: **o F0 aposentou o juiz do R6.** Mas a entrega nunca propagou a supersessão.
A OPINIAO (L35-37, L89) e o FECHAMENTO (L74) ainda citam "R6/gpt-4.1-mini fechou o caveat de juiz único".
A OPINIAO L36 chega a dizer, no mesmo parágrafo, "os 3 menores da OpenAI ficaram de fora por lenientes" E
"o gpt-4.1-mini confirma a ordenação". A contradição mora numa frase só.

**A leitura honesta (o que cada evidência fecha):**
- O **caveat de artefato** ("Claude julga Claude") é fechado pelo **painel afiado do F0**: 7 de 9 juízes de
  3 empresas convergem no falso-positivo, e a AN-v3 reduz o FP para todos eles. Cross-vendor de verdade.
- O **R6** ainda contribui: confirma que a ORDENAÇÃO/DELTAS sobrevivem a um juiz não-Claude, e MEDIU o viés
  de família. Mas, como o gpt-4.1-mini é leniente, o R6 **não** valida a MAGNITUDE anti-falso-positivo.
- Logo: a âncora cross-vendor do achado de FP é o F0 (afiados); o R6 fecha a direção, não a magnitude.

Isto **não** reabre "juiz único Claude" — o caveat segue fechado, por F0 + F4 (92% inter-juiz). Só sharpa
QUAL evidência fecha O QUÊ.

## 4. O que falta — mapa de lacunas

Transversal: **[TETO]** = limite irredutível (o input não contém o que se pede; nenhum trabalho reduz) vs
**[LACUNA]** = redutível por desenho/dado/ferramenta. Moldura: [FUNDAMENTO](FUNDAMENTO-juiz-escala-mensuravel.md).

### (a) NA LISTA — barato (re-análise sobre dado existente) — [LACUNA]
- Computar **neff/φ sobre os vereditos que já existem** (o `calc_stats.py` já roda κ par-a-par).
- **Re-pontuar o braço ecológico recente (R8, P10, próprios, fg2p) com 2º juiz afiado não-Claude.**
- **Re-processar o s04** (gabarito admitidamente errado; "inventados" superestimados em ~1).
- **Test-retest intra-juiz** (ADR-006 ao juiz: K≥5, temp>0, flip-rate). Hoje só há confiabilidade inter-juiz.
- **Ablação de gabarito sobre os 36 planos do F4** (ver §5b — decide se o α=0,918 é em parte gabarito-no-prompt).

### (b) NA LISTA — caro (dado novo) — [LACUNA]
- Cruzar framing AUDIT × abstenção-primeiro no mesmo fixture. Único corte que desconfunde ruído de framing.
- Auditoria rica de qualidade em TERCEIRO, gabarito independente, 2º fabricante, >1 gênero. É o produto-alvo.
- **Ponte texto → agente-com-ferramentas.** Maior gap de validade externa.
- Digest-cru × digest-capado (isolar se a sub-detecção é artefato de curadoria).
- Segunda família de fixture em ≥1 eixo.

### (c) FORA DA LISTA — o que ninguém mapeou
- **A estratificação em camadas — a tese que dá NOME ao método — nunca foi testada como variável.** [LACUNA]
  Todo experimento injeta o doc inteiro. Ninguém embaralhou a ordem das §§, inverteu L0>L1>L2, ou removeu a
  noção de camada mantendo as regras. O pace layering é fundamento bibliográfico não-medido.
- **Manutenção de um projeto que JÁ nasceu Strata** (dogfooding medido). [LACUNA] Toda fixture é projeto SEM
  Strata recebendo o método; o caso de uso real mais provável é célula vazia.
- **Aquisição/usabilidade humana da NOTAÇÃO** (escrever um tombstone correto, saber qual § invocar). [LACUNA]
- **Falso-negativo de segurança operacional:** o §6-bis faz a IA recusar/sabotar uma ação perigosa-porém-
  CORRETA (curl|bash legítimo de CI, rm -rf build/)? Mede-se "não inventa ameaça", não "não bloqueia o certo". [LACUNA]
- **Invariância linguística:** tudo é PT-BR. A recusa lexical §6-bis cai mais em outro idioma? [LACUNA]
- **Auto-sabotagem do andaime:** modelo barato auto-auditando RECOMENDA APAGAR os marcadores §3 que o
  tornariam situável (gemini-flash, F6 2/2). Não está em P0-P3. [LACUNA] de segurança-de-método.

### Confusão TETO vs LACUNA (viés sistemático de atribuição)
O corpus aplica o FUNDAMENTO bem ao JUIZ (nomeia o teto do consenso) mas NÃO ao SUJEITO/MÉTODO. Toda falha do
modelo-sujeito é rotulada "capacidade" (teto), nunca "forma mal-desenhada" (lacuna). Três pontos concretos:
- **"Sub-detecção é o limite duro"** é linguagem de [TETO], mas o cruzamento de framing nunca rodou. Pode ser
  [LACUNA] redutível por framing. Reclassificar para "limite candidato, ainda confundido com framing".
- **"Web — nenhum modelo confiável"** vendido como [TETO], mas gemini-com-web=0 aponta [LACUNA] de ferramenta.
- **"Cronologia sem desambiguador de conteúdo"** (nome-simples=velho vs cópia=novo, ambíguo até p/ humano) é o
  ÚNICO [TETO] genuíno — desigualdade de processamento de dados. O corpus tem o aparato para arquivá-lo como
  impossível-por-design, mas o deixa "nem testado nem arquivado". Nomear como teto e fechar.

## 5. Contradições entre docs (a reconciliar)

- **"O topo calibra":** o eixo-tier trata como sólido (f4-clean 6/6 mecânico); a abstenção-s9 confessa 1/5
  instável (P8c). Reconciliar: sólido NA EXECUÇÃO (§5/§3), frágil no FRAMING/conteúdo.
- **gpt-4.1-mini:** o F0 o desqualifica (leniente, excluído do painel); o R6/OPINIAO o promove a validador.
  Resolvido na §3 acima.
- **(b) Abstenção = ausência de output.** O gate do f4-clean define "abstenção correta" = `JA-CONFORME`, zero
  `<FILE>` (F4 L38). Um modelo que abstém por preguiça/timeout pontua igual a um que abstém por juízo. O gate
  verifica silêncio, não calibração. É o mesmo furo do 9/9 externo ("abster certo vs abster sempre"), aplicado
  à célula MAIS forte de abstenção/tier. **Mitigação parcial:** no braço Strata o modelo invoca §9 explícito
  ("aplicar mais estrutura seria excesso"), evidência qualitativa que o SCORE não captura.
- **α=0,918 (F4) × Fase B (cego cai abaixo do baseline):** o número que ancora o sólido e o que prova
  "convergir≠acertar" nunca tocaram a mesma população. A ablação de gabarito nunca rodou sobre os 36 planos do
  F4. Se os juízes do F4 também caem cegos, o 0,918 é em parte gabarito-no-prompt.
- **Destruição de histórico:** o F6 a eleva a auto-sabotagem séria; o F4 L82 a rebaixa a "ocasional, não-
  confirmada". A evidência F6 deveria RE-ELEVAR o que o F4 rebaixou.

## 6. A realidade do Strata — crua, em escala

O que se esperava: um método que faz a IA auditar e manter projetos melhor.

O que o Strata É hoje:
- **É um formalizador de conserto de defeito conhecido.** Defeito já identificado + consumidor mecânico
  downstream que precisa parsear a fonte canônica → entrega o conserto rastreável e impede a destruição de
  histórico, até no econômico, replicado no real para a preservação. Real, e perto do teto. Também estreito.
- **NÃO é um auditor de qualidade.** No projeto real, como auto-auditor, não bate a competência pura do
  modelo. A descoberta de dívida nova é capacidade, não forma; o método ora não adiciona, ora CEVA alucinação
  no fraco (defeito_alucinado 6/8 com Strata vs 2/8 sem). É o produto imaginado e o menos validado fora da família.
- **É um deslocador de viés, não um corretor.** A forma troca over-ação por over-abstenção. Não compra
  discernimento; redistribui o erro. Só o topo escolhe o lado certo, e instável.
- **A distância ao melhor-possível é assimétrica.** No §5/§3-por-execução: PERTO do teto. Na auditoria-rica em
  terceiro: distância DESCONHECIDA (nunca medida com gabarito independente). No agente real: NÃO-MEDIDA. Na
  própria tese de camadas: NÃO-TESTADA.

Veredito justo: um método com **núcleo pequeno e firme, corretamente restrito na entrega**, cercado de sinais
direcionais honestos e de uma tese-mãe (camadas) que ainda é fundamento, não achado. Não é over-claim chamar
o núcleo de sólido. Seria over-claim estender "sólido" à auditoria de qualidade, à abstenção-por-framing, ou
ao agente real.

## 7. Envelope de uso — ADITIVO / NEUTRO / NOCIVO

Eixos: TAREFA × CAPACIDADE-DO-MODELO × CONTEXTO.

| Tarefa | Modelo | Contexto | Veredito |
|---|---|---|---|
| Consertar §5 conhecido + preservar §3 | econômico/médio (Haiku, gpt-4o-mini, Sonnet) | conteúdo load-bearing + consumidor mecânico downstream | **ADITIVO** — habilita o fix que o baseline não faz e impede a destruição que o baseline comete (réplica no real) |
| Preservar histórico / tombstone (§3) | qualquer, até topo | qualquer | **ADITIVO** — até o Opus baseline esquece de registrar o conserto 2/3 |
| Recusar injeção literal §6-bis | econômico/leniente | injeção legível, geração de plano | **ADITIVO** — flipa de obedecer para recusar |
| Recusar injeção §6-bis | topo | qualquer | **NEUTRO** — já recusa nativo; a forma só padroniza |
| Abster-se / não-agir (§9) | topo (Opus, gpt-4.1) | projeto que PODE já estar bom | **ADITIVO** — elimina o falso-positivo; o topo calibra (instável, ~1/5) |
| Abster-se / achar dívida | fraco/médio | projeto JÁ-LIMPO | **NOCIVO** — ceva super-engenharia e alucinação (6/8 vs 2/8); pior que não usar |
| Gate de abstenção (já-bom/precisa) | médio/alto, não-Claude | terceiro bem-organizado, gênero Python | **ADITIVO** — 9/9 externo |
| Gate de abstenção | médio/barato | projeto que DE FATO precisa | **NOCIVO** — complacência / sub-detecção |
| Auditoria rica / descoberta | topo | projeto real | **NEUTRO** — o topo já faz sozinho |
| Auditoria autônoma sob "ache-problemas" | qualquer | projeto real limpo/exemplar | **NOCIVO** — induz falso-positivo (10-25 issues inventadas) |
| Situar no tempo | topo OU humano no loop | cronologia LEGÍVEL | **ADITIVO** — remove a ambiguidade |
| Situar no tempo | barato | projeto real-RUIDOSO | **NOCIVO** — re-levanta bug resolvido E pode mandar apagar marcadores |
| Verificar fonte na web | qualquer | sem web | **NOCIVO/ILUSÓRIO** — carimba falso como verdadeiro |
| Verificar fonte | modelo que sabe abster | com web | **ADITIVO (exploratório)** — "faz parar de fingir"; ainda revise |
| Executar fix sozinho | local 4-8B não-reasoner | qualquer | **NOCIVO** — zero PASS, destruiu config, propagou injeção |
| Strata CRU (sem tutoria) | barato | qualquer | **NOCIVO** — a pior forma; aumenta ruído |
| Explicar L0/L1/L2 (conceito) | qualquer, até 8B local | qualquer | **NEUTRO** — todos entendem; entender não é a barreira |
| Aplicar L1 (nomear formalização) sozinho | médio/econômico | qualquer | **NOCIVO** — propõe formalização desproporcional, viola o próprio §9 |

**Regra prática (uma linha):** use o Strata para PADRONIZAR o conserto de um defeito que você já conhece
(econômico basta) e para fazer o TOPO se abster num projeto que pode já estar bom; não o use como auditor
autônomo, nem dê a forma a modelo fraco em projeto limpo (ceva alucinação), nem confie em conclusão de
completion-only para prever um agente-com-ferramentas (nunca testado).

## 8. O que esta auditoria fixa

- O núcleo sólido **sobrevive** ao confronto granular. Não está inflado.
- Sobram **derivas pontuais** nos docs de entrega (§2) — uma aplicada (R6), as outras pendentes e listadas.
- Há **contradições entre docs** (§5) a reconciliar, e um **viés de atribuição** (§4) que rotula falha-do-
  método como teto-de-capacidade. É o ponto mais sutil: o FUNDAMENTO foi aplicado ao juiz, falta aplicá-lo ao
  método.
- A novidade prática é o **envelope de uso** (§7): onde o Strata é aditivo, neutro ou nocivo, em escala — não
  "funciona/não funciona".
