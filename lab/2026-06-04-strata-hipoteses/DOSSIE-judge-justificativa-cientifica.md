---
title: 'Dossiê: justificativa científica do LLM-as-judge no Strata'
created: 2026-06-16
updated: 2026-06-16
status: 'REGISTRO — argumento + plano para defender o judge (literatura + evidência interna). A executar: gráficos/testes da §6.'
nota: 'Âncoras internas (F0/R6/F4/P1P2, scripts) conferidas por existência. Citações de literatura a reconferir antes de uso EXTERNO (publicação).'
---

# Registro: justificativa científica do LLM-as-judge no Strata

> Registro de pesquisa. Responde à crítica recorrente de que "o judge não é perfeito, logo não serve".
> Âncoras internas: `RESULTADOS-f0-confronto-juizes.md`, `RESULTADOS-r6-2o-juiz.md`, `RESULTADOS-f4-execucao.md`,
> `RESULTADOS-p1p2-anv3.md`, `GABARITO-genero-temporal-own.md`; scripts `eval/strata/compare_judges_ladder.py`,
> `eval/strata/verify_f4.py`; definição de método em `GLOSSARIO.md` e `ARQUITETURA-E-EVIDENCIAS.md`.
> Tudo abaixo é sinal/direção forte, não prova. Regime completion-only, N pequeno. Ver caveats no fim.

## 1. A pergunta científica e a crítica que ela responde

A crítica.
Alguém diz: "vocês pedem o julgamento ideal. O judge LLM não é perfeito. Logo a medida não serve."

A confusão por trás dela.
Confunde-se **ideal regulativo** com **critério de aceitação**.
O argumento crítico trata "perfeição" como condição de entrada.
Mas nenhuma medida científica passa nesse teste — nem régua, nem termômetro, nem anotador humano.

A pergunta que de fato respondemos.
Não é "o judge é perfeito?".
É: **dá para saber o quanto, em que direção e em que tarefas o judge erra — e isso é suficiente para confiar nas conclusões que tiramos dele?**

A resposta curta.
Sim. Com lógica + testes, mede-se:
- se os juízes se **alinham** entre si (convergência cross-vendor);
- o quão **adequado** é o julgamento de uma **tarefa-átomo** num uso comum de IA;
- e como isso **herda logicamente** para o peso/credibilidade do julgamento de **projeto** (o agregado).

E mede-se a estrutura do erro: se o juiz **tende a um centro** rumo ao ideal, fica **perdido**, ou **sai do centro (drift)**.
Saber que erra, e como erra, é **informação científica válida** — não fracasso.

## 2. O argumento do ideal-regulativo (com a literatura de medida)

### 2.1 O ideal é guia, não meta atingível
Em Kant (via SEP, Williams 2023), princípios **regulativos** orientam a investigação sem garantir nada sobre os objetos.
A unidade/objetividade da ciência é norte, não ponto de chegada — porque a experiência é sempre finita.
Aplicado aqui: "julgamento perfeito" guia o trabalho; o progresso é **afastamento do erro reconhecido**, não toque no absoluto.

### 2.2 O baseline correto NÃO é o oráculo, é o piso de ruído humano
Humanos discordam.
Em tarefas subjetivas, a discordância é **sinal**, não só ruído (Aroyo & Welty, 2015 — *crowd truth*: o ground-truth é distribucional).
Juízes LLM fortes batem ~80%+ de concordância com preferências humanas em MT-Bench/Chatbot Arena — o **mesmo patamar** da concordância humano-humano (~81%; GPT-4 vs humano ~85%) (Zheng et al., 2023).
Em NLG, o juiz LLM com chain-of-thought correlaciona Spearman 0.514 com humanos, batendo BLEU/ROUGE (Liu et al., G-Eval, 2023).
A régua justa, portanto, é o **piso de ruído humano-humano**, não um avaliador perfeito.

### 2.3 Validade e confiabilidade são erros distintos — e ambos se caracterizam
Teoria de medida (Bhattacherjee, 2012):
- **erro aleatório** reduz a **confiabilidade** (dispersa em torno da média);
- **erro sistemático/viés** reduz a **validade** (desloca a tendência central).
São independentes: dá para ser confiável e inválido (tiro agrupado fora do alvo).
Confiabilidade é necessária, não suficiente.

Validar é **investigação científica sobre o significado do escore**, não consulta a um critério único (Cronbach & Meehl, 1955; Messick, 1995 — validade de construto como conceito unificado, num processo aberto e provisório).

### 2.4 O erro caracterizado é, ele próprio, um resultado
Na metrologia (GUM/JCGM 100:2008), um resultado **só está completo com sua incerteza declarada**.
Viés entra como termo de correção no modelo; até correção zero carrega incerteza residual.
Logo, **mapear o tamanho, a direção e a estrutura do erro é um resultado científico** — não um defeito a esconder.

### 2.5 Métricas de concordância podem enganar
Números altos não bastam.
Correlação mede relação relativa, não acordo absoluto: um juiz pode correlacionar bem e ainda ser sistematicamente severo/leniente (*Judge's Verdict*, 2025).
Kappa é instável sob desbalanceamento (paradoxo do kappa; Zapf et al., 2016; McHugh, 2012).
Medidas corrigidas por acaso são preferíveis; Krippendorff (2004) sugere α ≥ 0.800 para confiar, 0.667-0.800 só para preliminar — heurísticas, não leis.
Calibração é eixo **ortogonal** à concordância: mede se a confiança declarada bate com a acurácia (ECE; Guo et al., 2017). LLMs com RLHF tendem à superconfiança (Tian et al., 2023; Leng et al., 2024).

**Fio condutor.** Porque a medida perfeita é ideal regulativo, o trabalho científico desloca-se de "acertar o alvo" para "caracterizar quão perto se está e em que direção se erra". É exatamente o que os eixos abaixo fazem.

## 3. Os eixos mensuráveis (parâmetros com lógica + testes)

### Eixo A — alinhamento inter-juiz (os juízes concordam?)
Lógica.
Fornecedores diferentes erram de modos mais independentes.
Se juízes de empresas distintas **convergem**, o resultado provavelmente é correto; se divergem, é chamada dependente-de-julgamento.
Isso ataca diretamente o **self-preference bias** — o juiz favorecer a própria saída (Zheng et al., 2023; causa identificada em Panickssery et al., 2024) — e segue a mitigação canônica de **júri cross-vendor** (Verga et al., PoLL, 2024).

Evidência interna (F0, `RESULTADOS-f0-confronto-juizes.md`; script `eval/strata/compare_judges_ladder.py`).
9 juízes de 3 empresas (OpenAI, Google, Anthropic) re-pontuam **cego** o mesmo conjunto P1+P2.
Discriminador objetivo: no fixture NNN, os planos AN-v2 cometem falso-positivo **comprovável** (flagam arquivos-IA como duplicata, criticam navegação boa = fatos textuais). FP ~4 = correto; ~0 = leniência.
7 juízes capazes convergem em NNN-v2 FP **~3.9-4.4**: claude-opus 4.25, gemini-2.5-pro 3.88, gemini-2.5-flash 4.12, gpt-5 3.29, gpt-5-codex 4.38, o3 4.00, gpt-5.5 4.38.
**Todos** mostram a AN-v3 reduzindo o FP (claude 4.25→2.88; gpt-5.5 4.38→3.38; gemini-pro 3.88→2.88; gemini-flash 4.12→1.88).
**Prova-âncora:** o achado central **não** é artefato de "Claude julga Claude" — três empresas o reproduzem.

Sub-achado de capacidade de juiz.
"Maior = melhor juiz" vale **dentro** de um fornecedor (OpenAI: nano 0.0 → mini 1.5 → gpt-5 3.3 → gpt-5.5 4.4), mas é **confundido entre** fornecedores: o gemini-2.5-flash (pequeno, barato) crava 4.12, afiado como os gigantes.
O que importa é **discernimento**, testado **por tarefa**.
OpenAI-small (nano/mini/4.1-mini) são **lenientes** — cegos ao erro. Não usar como juiz; bom-e-barato = gemini-2.5-flash.

Concordância em regime real (R6, `RESULTADOS-r6-2o-juiz.md`).
2º juiz não-Claude (gpt-4.1-mini) re-pontua cego 63 planos.
**Ordenação e deltas idênticos:** AN > prosa > baseline com os dois juízes (det_found: baseline 3.43/4.62; prosa 4.24/5.43; AN-v2 5.67/6.52; AN−prosa +1.43/+1.09; prosa−baseline +0.81 em ambos).
A **divergência é de magnitude, não direção**: MAE(det_found)=1.14 na escala 0-7; viés de leniência ~1 ponto.
Concordância "found" por problema: P1 0.94, P7 0.90, P4 0.89, P5 0.86, P6 0.76, P3 0.71, P2 0.56 — **alta nos gates críticos** (conflito/fail-open/honestidade), baixa nos "moles" (datas, readme).
**Lição transversal:** reportar deltas e ordenação, **nunca absolutos** como verdade.

### Eixo B — adequação do julgamento da tarefa-átomo
Lógica.
Antes de confiar na opinião, prefere-se a **regra objetiva**. Hierarquia: **mecânico > juiz** (`GLOSSARIO.md`; `ARQUITETURA-E-EVIDENCIAS.md`).
Um programa confere por regra objetiva (o valor existe? o arquivo foi preservado?).
Antes de confiar no programa, testa-se contra gabarito conhecido (**GOLD self-test** / casos-disfarce) e só se usa se acerta 100%.
O juiz LLM entra só no **resíduo** que a regra não fecha.

Evidência interna (F4, `RESULTADOS-f4-execucao.md`; verificador `eval/strata/verify_f4.py`).
GOLD-gate **100%** (casos-disfarce: esvaziar=N1, reescrever-histórico=N1, obedecer=INJEÇÃO, rename-tombstone=PASS; 0 falso-neg de injeção).
Concordância inter-juiz cross-vendor (2 não-Claude cegos) = **92%**, contra **56%** no F3.
A diferença não é acaso: vereditos F4 ancoram em **ações concretas de arquivo**; F3 ancora em texto ambíguo.
**Quanto mais objetivo o alvo, mais os juízes concordam** — o que torna a adequação da tarefa-átomo mensurável e regulável (por escolher alvos objetivos).

### Eixo C — herança lógica tarefa → projeto
Tese.
Se o juiz acerta a **tarefa-átomo** (recusar injeção, eleger fonte canônica, preservar histórico), o julgamento de **projeto** (o agregado) **herda** confiança — proporcionalmente.

Por que a herança é válida.
- O julgamento de projeto é composição de tarefas-átomo.
- Cada átomo tem sua adequação medida (Eixo B) e seu alinhamento medido (Eixo A).
- A credibilidade do agregado é **limitada pela** dos átomos que o compõem, não inventada.

Onde a herança é forte e onde é fraca (honesto).
- **Forte** quando o átomo ancora em ação de arquivo: F4 92% inter-juiz, GOLD 100%.
- **Fraca** quando o átomo é texto ambíguo: F3 56%, datas/readme com baixa concordância.
- A herança, portanto, **não é uniforme** — e isso é coerente com a literatura: a concordância juiz-humano varia por tarefa e domínio, não é lei única (Gu et al., 2024; Li et al., 2024).

Limite da forma (`RESULTADOS-p1p2-anv3.md`).
A forma (AN-v3) melhora sinal-ruído (NNN net −4.25→−2.76; pdf2md −0.38→**+0.50**), mas **não fecha o gap de capacidade**: desloca o erro de over-flag para under-flag em alguns modelos, e detectar falso-positivo **exige a mesma capacidade do auditor**. Implicação para a herança: o agregado herda confiança **só até** onde o átomo tem discernimento.

## 4. O modelo centro / ideal / perdido / drift (erro como informação)

A confiança não é binária. Tem linhas cinzentas.
Mas a **forma** do erro é caracterizável em quatro estados:

- **Tende ao centro (rumo ao ideal).** O juiz erra, mas seus erros se concentram em torno do alvo e se reduzem com mais capacidade/forma.
  *Evidência:* convergência cross-vendor em FP ~3.9-4.4 (F0); todos reduzem o FP com AN-v3.
- **Calibrado-mas-deslocado (viés sistemático).** Tende a um centro, porém deslocado do ideal por um offset estável.
  *Evidência:* gpt-4.1-mini ~1 ponto mais leniente (MAE 1.14, R6). Erro de **validade** (Bhattacherjee, 2012): conhecido o offset, corrige-se a leitura (reporta-se delta, não absoluto).
- **Perdido (sem centro).** Não discrimina; ruído domina o sinal.
  *Evidência:* OpenAI-small lenientes/cegos (gpt-5-nano FP 0.00, F0). Diagnóstico operacional: não usar como juiz.
- **Drift (sai do centro para fora).** Move-se sistematicamente para longe do alvo.
  *Mitigação prevista:* fixtures com **hash congelado** (anti-drift) e GOLD self-test que falha quando o verificador deriva.

Por que cada estado é informação, não fracasso.
- Saber que um juiz é **leniente em ~1 ponto** permite reportar deltas e ordenação com segurança (R6).
- Saber que um juiz é **cego ao FP** o desqualifica para a tarefa — e isso é um resultado (F0).
- Saber **onde** os juízes divergem (datas, readme: P2 0.56) localiza a fronteira do método.
- É a metrologia aplicada ao julgamento: caracterizar a dispersão e o viés **é** o resultado (GUM, 2008).

O mapa dos vieses tem nome na literatura, e mitigação correspondente:
- **position bias** (Zheng et al., 2023; Shi et al., 2024 — não é ruído aleatório; dirigido pelo gap de qualidade) → swap/randomização + métricas de consistência;
- **verbosity bias** → rubrica/referência;
- **self-preference** (Panickssery et al., 2024) → **júri cross-vendor** (Verga et al., 2024).
Os três eixos da §3 são a instância concreta dessas mitigações no Strata.

## 5. O que JÁ TEMOS e o que FALTA

### Já temos (com números)
- **F0 fechado, alta confiança.** Convergência cross-vendor FORTE: 7 juízes de 3 empresas em FP ~3.9-4.4; AN-v3 reduz o FP em todos. "Maior=melhor" só dentro de fornecedor. (`RESULTADOS-f0-confronto-juizes.md`; `eval/strata/compare_judges_ladder.py`.)
- **R6 fechado.** 2º juiz não-Claude: ordenação/deltas robustos; MAE 1.14; concordância por problema P1 0.94 … P2 0.56; viés de família **leve** (Claude ~0.87 ponto mais generoso com haiku). (`RESULTADOS-r6-2o-juiz.md`.)
- **Gold-gate mecânico definido e operando.** Hierarquia mecânico > juiz; GOLD self-test 100%; juiz só no resíduo. F4: GOLD 100%, inter-juiz 92% (vs 56% no F3). (`GLOSSARIO.md`; `RESULTADOS-f4-execucao.md`; `eval/strata/verify_f4.py`.)
- **Limite da forma medido.** AN-v3 melhora sinal-ruído mas não instala discernimento (`RESULTADOS-p1p2-anv3.md`).

### Falta (lacunas honestas)
- **Verdade-base independente de qualquer LLM.** A convergência cross-vendor não exclui (em teoria) um viés compartilhado convergindo no "menos-ruim" — improvável, não verificável sem ground-truth externo. (Ressalva F0.)
- **Juiz duplo nas células decisivas do topo.** Reteste-limpo, abstenção §9 e faixa ecológica F4 rodaram com **um juiz só** (`OPINIAO-DE-USO.md`).
- **Quebrar a circularidade.** Projetos de **terceiros** + juiz cego que não viu o Strata + gabarito pré-registrado (`GABARITO-genero-temporal-own.md`).
- **Métricas corrigidas por acaso e calibração.** Hoje reportamos concordância bruta (%), MAE, deltas. Falta α de Krippendorff com IC e ECE como eixo separado (Krippendorff, 2004; Guo et al., 2017).
- **Sair do completion-only.** Validade de agente com ferramentas reais.
- **N ≥ 5 por célula.** Hoje N=2-3; só deltas grandes vs ruído têm poder.

## 6. Plano para ARGUMENTAR

### Gráficos a produzir
- Scatter de **concordância inter-juiz por objetividade do alvo** (F4 92% / F3 56% como pontos): mostra que adequação cresce com objetividade.
- **Escada de juízes por fornecedor** (FP detectado): monotônica dentro de fornecedor, confundida entre fornecedores (gemini-flash pequeno crava 4.12).
- **Centro/ideal/perdido/drift**: dispersão de cada juiz em torno do FP-alvo do NNN, anotando viés (offset) e largura (dispersão).
- **Bland-Altman juiz-Claude × juiz-neutro** (eixo R6): visualiza o viés sistemático de ~1 ponto e seu IC.
- **Delta vs absoluto**: ordenação AN>prosa>baseline preservada nos dois juízes, com bandas — o argumento "reporte deltas, não absolutos".
- **Calibração (ECE)**: confiança declarada do juiz vs acerto, em bins (eixo ortogonal à concordância).
- **Concordância por problema** (R6): barras P1 0.94 … P2 0.56 separando gates críticos dos "moles", localizando a fronteira.

### Testes a rodar
- **Krippendorff α com IC** sobre os vereditos multi-juiz (substituir % bruto; faixa-alvo ≥ 0.800 justificada pelo custo do erro).
- **Swap/randomização de ordem** com métricas de position consistency (Shi et al., 2024) nas tarefas de par.
- **Júri cross-vendor formal (PoLL)** nas células decisivas hoje com juiz único (abstenção §9, reteste-limpo, faixa ecológica).
- **ECE do juiz** com confiança verbalizada + temperature scaling (Tian et al., 2023).
- **Replicar F0 contra IAA humano** num subconjunto: comparar kappa juiz-vs-humano com kappa humano-vs-humano (régua justa, Zheng et al., 2023).
- **N ≥ 5** nas células-âncora; reportar pass@k vs pass^k (ADR-006).
- **Braço de terceiros** com gabarito pré-registrado e juiz cego ao Strata (quebra de circularidade).
- **GOLD self-test periódico** sobre fixtures de hash congelado (detecta drift do verificador).

## 7. Caveats honestos

- **O juiz conhece o gabarito (circularidade).** Nos projetos próprios, projeto-sujeito + analista do gabarito + autor do método são a mesma família (Leonardo + Claude). É quase auto-avaliação; mede no máximo se "o modelo lê como o autor lê", **não** se o autor está certo (*petitio principii*). Quebrar exige terceiros + juiz cego (`GABARITO-genero-temporal-own.md`).
- **N pequeno.** 2-3 runs/célula; nenhuma com N≥5. A variância intra-modelo já virou o próprio sinal. São deltas-grandes-contra-ruído, não significância estatística.
- **Ground-truth ruidoso.** Anotadores humanos discordam; a discordância é parcialmente sinal (Aroyo & Welty, 2015). O baseline correto é o piso humano-humano, não um oráculo.
- **Viés de família leve, não nulo.** Juiz Claude ~0.87 ponto mais generoso com modelo Claude; n minúsculo; mitigado por não ancorar em célula Claude-julga-Claude e manter 2 juízes nas decisivas.
- **2º juiz que estava em uso era fraco.** gpt-4.1-mini é leniente (F0). Conclusões sobrevivem (direção robusta), mas a magnitude anti-FP depende do juiz mais discernente.
- **92% e 56% não são universais.** São, respectivamente, alvo-de-ação-de-arquivo (F4) e texto-ambíguo (F3). Não estender ao corpus inteiro.
- **Completion-only.** Mede intenção no texto, não o agente real com ferramentas — exceto onde o gold-gate inspeciona estado de arquivos (F4).
- **Métrica frágil pode superestimar.** % bruto e correlação não corrigem acaso nem viés absoluto (*Judge's Verdict*, 2025). Migrar para medidas corrigidas por acaso + calibração separada.
- **Não-falseabilidade do viés compartilhado.** Todos os fornecedores partilharem um viés e convergirem no "menos-ruim" é improvável, mas exigiria verdade-base independente de qualquer LLM para descartar.
