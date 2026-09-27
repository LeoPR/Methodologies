---
title: 'Temporalidade: síntese do mapa amplo (camadas 1 a 4)'
created: 2026-09-27
updated: 2026-09-27
status: 'Síntese dos quatro mapas e da revisão de LLMs. Hipóteses de método NÃO testadas.'
tags: [temporalidade, sintese, ordem-parcial, estado, lacuna, metodo]
---

# Temporalidade: síntese do mapa amplo

Fontes: [MAPA-1](MAPA-1-artefato-e-ordem-formal.md) (relógio e ordem formal),
[MAPA-2](MAPA-2-filosofia-e-cognicao.md) (filosofia e cognição),
[MAPA-3](MAPA-3-testes-humanos.md) (testes humanos),
[MAPA-4](MAPA-4-IA-ordem-estado-lacuna.md) (IA),
[REVISAO-LITERATURA](REVISAO-LITERATURA.md) (datas e defasagem em LLMs).
Cada afirmação abaixo aponta ao mapa que a sustenta; os mapas têm as fontes.

## 1. O que as quatro áreas dizem em comum

**A ordem vem da dependência, não do relógio.** Quatro tradições chegaram nisso sem se citar:

| área | forma da ideia | mapa |
|---|---|---|
| computação distribuída | *happened-before* (Lamport 1978): ordem pelo fluxo de causa; o relógio físico deriva e pode inverter causa e efeito | 1 |
| IA clássica | STRIPS, planejamento de ordem parcial: precondição e efeito forçam a ordem; o resto é concorrente | 1 |
| psicologia cognitiva | scripts e redes causais (Bower 1979; Trabasso 1985): "uma ação habilita a seguinte"; texto embaralhado é lembrado na ordem canônica | 2 |
| desenvolvimento | relações habilitadoras organizam a memória aos 1–2 anos; aos 3–4 a criança preenche o estado que falta (Gelman 1980) | 2 |

**A ordem é parcial.** Lamport, Sacerdoti, Chambers & Jurafsky, proScript e os aglomerados
hierárquicos de Farag (2010) dizem o mesmo: sequência de eventos é grafo, não lista. Totalizar
exige desempate declarado.

**O timestamp é evidência revogável.** É leitura de instrumento com convenção e incerteza (MAPA-1).
Humanos também reconstroem datas, e erram de modo previsível: telescoping, "conhecido parece
recente" (MAPA-2). Quando o horário contradiz a cadeia causal, o horário é o suspeito.

## 2. O que humanos fazem que as IAs não fazem

| capacidade | humanos | IA (evidência) | mapa |
|---|---|---|---|
| ordenar por estado | aos 3–5 anos | "Rastrear estado não emerge só de texto"; Mystery Blocksworld despenca sem nomes familiares | 2, 4 |
| coerência global | natural (modelo de situação) | ordem local sim, global não; ≥27% de incoerência | 4 |
| resistir à ordem de apresentação | iconicidade só sem marcador | permutar premissas: −30%; Test of Time: 73,6% → 45,7% | 2, 4 |
| ordenar imagens | fluência aos 5–6 anos (cultural) | GPT-4o 23,9% em reordenar sequências | 3, 4 |
| inferir o passo omitido | inferência-ponte sem custo; aos ~5 anos | αNLI 68,9% × 91,4%; LMs não acham "A omitido" menos estranho que "A negado" | 3, 4 |
| **notar que falta** | detecção depende do papel do passo (clímax ausente é o mais notado) | AbsenceBench 69,6% F1 mesmo com o original ao lado; QuestBench 40–50% em planejamento | 3, 4 |
| abster quando impossível | checagem de plausibilidade (falha em lesão frontal) | o1: só 27% dos problemas insolúveis reconhecidos; raciocínio piora a abstenção | 3, 4 |

## 3. Onde os humanos também falham (e o método não deve copiar)

- **Preenchimento vira falsa memória.** Ações implícitas no script são "lembradas" como ditas
  (Bower 1979). É o análogo humano da alucinação de passo.
- **O prior causal reescreve a ordem observada.** A causa é percebida como mais cedo, mesmo quando
  não foi (Bechlivanidis & Lagnado 2013, 2016, 2022).
- **Humanos constroem a ponte, não pedem a peça** (MAPA-3). Não há teste humano padronizado de
  *buscar* a informação ausente. O comportamento "notar e ir verificar" é raro até em gente.
- **Lesão pré-frontal** preserva o conhecimento do script e perde a organização: ordem, fronteiras,
  exclusão do **passo intruso** (Sirigu 1996). É um modo de falha simétrico ao passo ausente.

## 4. Os casos deste projeto, lidos com o mapa

- **DeepSeek V4.1 em GB10 (2026-09-26).** Tratei um fato de status ("não roda, não há runtime") como
  relação fixa: série A lida como série B (McTaggart). Puxei para o "agora" o último estado que eu
  conhecia, que é o telescoping (Neter & Waksberg). E não notei o elo que faltava (o runtime podia
  ter mudado): lacuna não detectada, preenchida por conta.
- **README do Comporta dizendo "Nada executado ainda"** com os estágios já rodados: status que
  envelheceu no texto, sem carimbo.

## 5. Lacunas da literatura (onde cabe contribuição)

1. **Nenhum benchmark da habilidade do paraquedas:** ordenar estados embaralhados por pré/pós-
   condição. O mais próximo é uma colcha (TRIP, CaT-Bench, PlanBench, StripCipher).
2. **Horário contradizendo estado: nenhuma fonte**, nem em humanos nem em IA.
3. **Detecção não avisada de lacuna**, seguida de busca, não tem teste padronizado em humanos nem
   benchmark em IA (ComicsPAP e αNLI avisam onde está a lacuna).
4. **Nenhum protocolo de processo avaliado** para fato perecível (REVISAO-LITERATURA).
5. Os **controles internos** da clínica (mecânico × intencional; com e sem distrator; passo intruso)
   não foram levados para IA.

## 6. Hipóteses de método (não testadas)

Elementos que aparecem convergentes nas quatro áreas. São candidatos, não conclusões.

1. **Linha do tempo externa**, não a continuação fluente do texto: eventos, relações, fonte, e cada
   passo marcado como observado ou inferido.
2. **Estado explícito antes de ordenar:** pré-condições e efeitos de cada descrição; a ordem sai de
   "efeito de A satisfaz pré-condição de B". Sem dependência, fica concorrente.
3. **Ordem parcial por padrão**; totalizar só com desempate declarado.
4. **Série B guardada, série A calculada** contra um "agora" verificado.
5. **Timestamp abaixo da restrição de estado**; conflito registrado, nunca arbitrado em silêncio. E o
   inverso: prior causal também não apaga evidência (lição de Bechlivanidis).
6. **Lacuna por enumeração:** gerar o script esperado e comparar com o presente; um efeito necessário
   que nenhum passo produz vira pergunta concreta, e a pergunta vira busca. Sem fonte, declarar o
   passo como inferido ou abster.
7. **Coerência global conferida mecanicamente** (transitividade, aciclicidade), fora do modelo.

Expectativa honesta: a literatura mostra que instrução em prompt tem efeito parcial. O que tem mais
chance é o que tira o raciocínio do texto fluente e o põe numa estrutura conferível (itens 1, 2 e 7).

## 7. Próximos passos possíveis (decisão do dono)

- **Aprofundar a leitura:** muitos achados vieram só do resumo. Ler na íntegra as fontes que vão
  sustentar o método (Lamport, Kowalski & Sergot, Bower 1979, Gelman 1980, McCormack & Hoerl,
  AbsenceBench, QuestBench, TRIP).
- **Desenhar um instrumento próprio** para as lacunas 1–3: cenas de estado embaralhadas, com horários
  adulterados, passo removido sem aviso, passo intruso, e controles mecânico × intencional e domínio
  ofuscado. Avaliação em níveis (ordem final, restrições usadas, lacuna notada, busca pedida).
- **Só depois**, testar as hipóteses da seção 6 contra linha de base, pré-registrado e com poder.
