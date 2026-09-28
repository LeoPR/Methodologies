---
title: 'Ontologia da temporalidade (v0): primitivas, relações e o que cabe em computação'
created: 2026-09-27
updated: 2026-09-27
status: 'Proposta v0, construída sobre os mapas 1–8. Não testada contra modelo. Cada escolha aponta para o mapa que a sustenta.'
tags: [temporalidade, ontologia, ordem-parcial, estado, evento, bitemporal, lacuna, metodo]
---

# Ontologia da temporalidade (v0)

Esta é a síntese das oito perspectivas (filosofia, cognição, testes humanos, física, matemática,
ontologias formais, computação e IA em LLMs). Os mapas trazem as fontes; aqui fica a construção.
É uma proposta de modelagem: onde uma área só oferece **analogia**, está dito.

## 1. A tese

**O tempo que importa para raciocinar é a ordem de dependência entre estados, não a leitura de um
relógio.** A ordem é parcial; o relógio, o instante e a duração são derivados; o "agora" é local; e
toda afirmação sobre o passado é um registro presente, com data própria.

Oito áreas chegaram a isso sem se citarem:

| área | forma da tese | mapa |
|---|---|---|
| filosofia | Aristóteles: tempo é "número da mudança segundo o antes e o depois"; Leibniz: "ordem de sucessões"; McTaggart separa ordem fixa (B) de status relativo ao agora (A) | 2, 5 |
| cognição | scripts e redes causais: "uma ação habilita a seguinte"; ordem reconstruída, não lida | 2 |
| desenvolvimento | aos 1–2 anos a memória se organiza por relações habilitadoras; aos 3–4 a criança preenche o estado que falta | 2 |
| física | a ordem causal é o que todo observador compartilha; a métrica sai de "ordem + contagem" | 5 |
| matemática | eventos primitivos, instantes construídos (Wiener, Russell, Whitehead); estruturas de eventos | 6 |
| ontologias formais | Moens & Steedman: ontologia "baseada em causação e consequência, não em primitivas temporais"; PROV: timestamp não implica ordem | 7 |
| computação | Lamport: ordem pelo fluxo de informação; STRIPS: precondição e efeito forçam a ordem | 1 |
| IA atual | o que funciona é "o LLM estrutura, algo simbólico calcula" | 8 |

## 2. Primitivas

| primitiva | definição operacional | de onde vem |
|---|---|---|
| **Fluente** (estado) | proposição que *vale* ou não num trecho (holds); homogênea; **permite**, não causa | Allen 1984; Galton 2012; DOLCE *state* |
| **Evento** | ocorrência fixa, histórica; não muda depois de registrada | Davidson; Galton 2008/2009 |
| **Processo** | algo em curso, que pode mudar (acelerar, parar) | Allen *occurring*; Galton; DOLCE/BFO *process* |
| **Núcleo** | processo preparatório → culminação → estado consequente | Moens & Steedman 1988; DOLCE *accomplishment* |
| **Transição** | evento lido como `pré-condições → (adiciona, remove)` | STRIPS; Plotkin (sistema de transição); VerbNet-GL (¬P(e1) → P(e2)) |
| **Participante** | quem ou o que toma parte, indexado no tempo | Davidson/Parsons; DOLCE PC(x,y,t) |
| **Configuração** | conjunto de eventos já ocorridos, fechado para trás e sem conflito; é o "estado do mundo" derivado | Winskel (estruturas de eventos) |
| **Relógio** | subsistema de mudança regular usado como referência | NIST; Einstein 1905; Page–Wootters; Barbour |
| **Registro** | estado presente que carrega traço de um estado anterior | Agostinho; Callender/Albert; Rovelli 2020 |
| **Agente-observador** | quem sabe; tem o próprio passado causal e o próprio "agora" | Hartle 2005; Lamport (processos) |

## 3. Relações

| relação | significado | propriedade | de onde vem |
|---|---|---|---|
| `habilita(e1, e2)` | um efeito de e1 satisfaz uma pré-condição de e2 | gera ordem | STRIPS/Weld; Bower 1979; Bauer & Mandler |
| `antes(e1, e2)` | fecho transitivo de `habilita` (e de fontes explícitas) | ordem parcial estrita | Lamport; Winskel |
| `incomparável(e1, e2)` | nenhum antes do outro | **≠ simultâneo** | Robb 1914; Lamport (concorrência) |
| `conflito(e1, e2)` | não podem ambos ocorrer na mesma história | herdado pela causalidade | Winskel; Belnap (pontos de escolha) |
| `contingente(e1, e2)` | e2 depende de e1 no episódio | **intransitiva** | Moens & Steedman; Galton 2012 |
| `inicia / termina / perpetua` | como um evento afeta um fluente | — | Galton 2012 |
| relações de Allen | entre intervalos, quando há duração | 13 relações; propagação | Allen 1983; OWL-Time |
| `traço_de(r, e)` | o registro r contém marca de e | e antes de r | seta por registros (Mapa 5) |
| `vale_em(f, intervalo)` | tempo de validade no mundo | corrigível | *valid time* (Snodgrass) |
| `registrado_em(f, t)` | quando o agente soube | só acréscimo, imutável | *transaction time*; PROV |

## 4. Regras

1. **A ordem sai da dependência.** `antes` é o fecho de `habilita`. Sem dependência, o par fica
   `incomparável`, nunca "ao mesmo tempo" por padrão. (Mapas 1, 5, 6, 7)
2. **O timestamp é evidência revogável.** Quando contradiz a cadeia de dependência, **o timestamp é
   o suspeito**: vira conflito registrado, não reordenação silenciosa. (Mapas 1, 5, 7)
3. **O prior causal também não apaga evidência.** Se a evidência observada contraria a expectativa
   do script, registra-se o conflito; não se "corrige" o observado. (Bechlivanidis & Lagnado, Mapa 2)
4. **Lacuna = pré-condição sem produtor** que também não está no estado inicial. A lacuna é
   **nomeável** e vira pergunta concreta: "o que produz *p*?". (Mapas 3, 4, 8)
5. **Intruso = evento sem ligação com o episódio**: não consome nem produz nada que o resto use. É
   o erro simétrico da lacuna. (Sirigu 1996, Mapa 3)
6. **Cada passo é observado ou inferido.** O que o script preenche é marcado como inferido, para
   não virar "falsa memória". (Bower 1979, Mapa 2)
7. **O "agora" é local.** É a configuração que o agente conhece; o que ele não leu, ou o que mudou
   depois do seu corte, **não é presente para ele**. (Hartle; Stein; Mapa 5)
8. **Status é calculado, não guardado.** "Mais recente", "ainda vale", "atual" são série A:
   calculam-se contra um "agora" declarado e verificado. Guarda-se só a série B. (McTaggart, Mapa 2)
9. **Duas datas por afirmação:** quando valeu no mundo e quando foi registrada. Corrigir é
   acrescentar, nunca reescrever. (Snodgrass; PROV; Zep; §8 do Strata)
10. **A ambiguidade restante se mede.** Número de ordens compatíveis (extensões lineares); zero
    ambiguidade = ordem total. (Brightwell & Winkler; Mapa 6)
11. **Estados não causam; permitem.** Causar e permitir são relações diferentes. (Galton 2012)
12. **"Estava fazendo" não implica "fez".** Preparação sem culminação é um caso legítimo (falha).
    (Paradoxo imperfectivo, Mapa 7)

## 5. O paraquedas, na ontologia

| evento | pré-condições | adiciona | remove |
|---|---|---|---|
| embarcar | no_chão, tem_bilhete | a_bordo | no_chão |
| vestir_paraquedas | tem_paraquedas | paraquedas_vestido | — |
| decolar_e_subir | a_bordo | em_altitude | — |
| saltar | a_bordo, em_altitude, paraquedas_vestido | em_queda | a_bordo |
| abrir | em_queda | velame_aberto | — |

A ordem sai sozinha: embarcar → decolar_e_subir → saltar → abrir. `vestir_paraquedas` fica
**incomparável** a embarcar e decolar (só precisa vir antes de saltar): duas ordens válidas, não uma.
Timestamp que ponha "abrir" antes de "saltar" é conflito. Tirar "embarcar" deixa `a_bordo` sem
produtor: lacuna nomeada. Simulação em [`prototipo/`](prototipo/).

## 6. Como as IAs erram, lido na ontologia

| erro observado | regra violada | mapa |
|---|---|---|
| ordenar pela ordem de leitura | 1 (ordem pela dependência) | 4 |
| confiar no timestamp contra a cadeia | 2 | 4 |
| incoerência global (A<B, B<C, C<A) | fecho transitivo feito "de cabeça" | 4, 8 |
| não notar o passo que falta | 4 (lacuna não enumerada) | 3, 4 |
| preencher o passo e tratar como visto | 6 | 2, 4 |
| "X não roda / X é o mais recente" dito como fato fixo | 7 e 8 (status sem "agora" verificado) | REVISAO, SINTESE §4 |
| responder com o último estado conhecido | 7 (telescoping do corte) | 2 |
| seguir raciocinando num problema impossível | 4 (sem lacuna nomeada, não há gatilho para parar) | 4 |

## 7. O que cabe em computação

| parte | status | por quê |
|---|---|---|
| ordem pela dependência, conflitos, lacunas, intrusos, ambiguidade | **fechável** (algoritmo conhecido) | ordenação topológica, fecho transitivo, contagem (aproximada) de extensões |
| duas datas por afirmação, correção só por acréscimo | **fechável** | bancos bitemporais, SQL:2011, Zep |
| "agora" como configuração conhecida | **fechável** se mantido **fora** do modelo | transformers e SSMs não rastreiam estado arbitrário numa passada (TC⁰) |
| extrair eventos, pré-condições e efeitos de texto ou imagem | **aproximável** (LLM) | Guan et al. 2023; VerbNet-GL; ATOMIC como prior |
| sugerir o que preenche uma lacuna | **aproximável** (LLM + busca) | scripts e conhecimento de mundo |
| segmentar eventos por surpresa | **aproximável** | EST, SEM, EM-LLM |
| granularidade "certa" do evento; notar espontaneamente o que falta; o agora vivido | **só explicável hoje** | teoria existe (EST, predição), reprodução confiável não |

Arquitetura mínima (Mapa 8): **o LLM propõe** a estrutura (eventos, pré-condições, efeitos, datas
observadas); **o simbólico calcula** (ordem, conflitos, lacunas, ambiguidade); **a lacuna vira
busca**; o "agora" e as duas datas ficam **fora do modelo**.

## 8. Limites desta v0

- As analogias com a física são estruturais, não derivações.
- Frame, qualification e ramification: pré-condições são infinitas em princípio; a v0 usa **mundo
  fechado declarado** e inércia (o que não é removido continua valendo).
- Produtor múltiplo e ameaças (um evento remove a pré-condição de outro) exigem planejamento de ordem
  parcial completo; o protótipo trata só o caso simples e sinaliza o resto.
- A parte aproximável (extração) não está no protótipo; as cenas entram já estruturadas.
- Nada aqui foi medido contra modelo. O próximo passo empírico é o instrumento da SINTESE §7.
