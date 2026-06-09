---
title: Dossiê (IDEIA, para estudar depois) — por que IAs falham com temporalidade, ordem, fonte primária e organização de pesquisa
created: 2026-06-09
status: REGISTRO de ideia/hipótese. NÃO executado. Subsume e amplia a [[H-D temporalidade]]. Estudar adiante.
tags: temporalidade, ordem, fonte-primaria, organizacao-pesquisa, dossie, hipotese
---

# Dossiê — o ponto cego temporal/organizacional da IA

> **Isto é um registro de IDEIA, não um estudo.** Reúne a pergunta, a hipótese e os ponteiros
> para a evidência que já temos — para retomar depois. Não repetir o conteúdo desta página em
> outros docs; quando estudarmos, vira um conjunto de experimentos próprios.

## A pergunta

Por que as IAs — **mesmo as mais sofisticadas** — falham de forma recorrente em um mesmo
*cluster* de tarefas que, para um humano cuidadoso, são naturais?

1. **Temporalidade** — situar um artefato no tempo: o que é *atual* vs *superado/histórico*;
   comprimir anos de produção como se fossem "agora".
2. **Ordem / sequência** — o antes e o depois; reconstruir a cronologia/causalidade a partir
   dos artefatos.
3. **Verificação de fonte primária** — abrir a fonte original em vez de repetir/inferir (a
   degradação tipo "telefone-sem-fio"); distinguir saber de achar.
4. **Organização de pesquisa ao longo do tempo** — manter um corpus navegável e tipado
   enquanto ele *muda* (reauditar o que virou obsoleto).

## A hipótese (a investigar, não resolvida)

Esses quatro podem ter **raiz comum** — não são quatro bugs avulsos. Candidatos a causa
(cada um é uma sub-hipótese testável):

- **H-r1 · Corpus achatado:** o treino é um *snapshot* sem índice temporal — aprende-se *o que
  se diz*, não *quando foi dito* nem *o que veio antes/depois*. Provável raiz da compressão temporal.
- **H-r2 · Sem episódico / sem "quando":** o modelo tem memória semântica, não episódica — não
  registra *quando* "viu" algo, então não ancora artefatos no tempo.
- **H-r3 · Co-presença da janela:** dentro do contexto, há ordem posicional, mas o modelo não
  trata as **datas dos artefatos** como ordem causal — lê tudo como co-presente ("agora").
- **H-r4 · Treino para plausibilidade, não para rastrear:** otimizado a produzir resposta
  plausível, não a abrir a fonte; e, sem ferramentas, **não pode** verificar — repete/infere.
- **H-r5 · Paradigma single-shot:** organizar/reauditar é **longitudinal** (o que mudou desde a
  última vez?), fora do modo "uma passada" em que os modelos operam.

## A evidência que JÁ temos (ponteiros — não repetir aqui)

- **H-D** ([README.md](README.md), seção H-D) + [RESULTADOS-r8-sintese-3-projetos.md](RESULTADOS-r8-sintese-3-projetos.md)
  (e [RESULTADOS-r8-projeto-real.md](RESULTADOS-r8-projeto-real.md)): em projeto real, os modelos
  tratam o **superado/histórico como problema atual** (falso-positivo temporal).
- [VIZ-capacidade-por-secao.md](VIZ-capacidade-por-secao.md) (P4): a seção **§3/§8 (datas/história)
  é o ponto cego de longe** (~33%, a mais fraca) — em todos os modelos.
- [RESULTADOS-p7-camadas-entender-aplicar.md](RESULTADOS-p7-camadas-entender-aplicar.md): na
  **verificação de fonte/conhecimento (§6/L1)**, o modelo médio erra confiante e o pequeno admite
  que "precisaria pesquisar" — toca H-r4.
- [RESULTADOS-f1-m0-abstencao.md](RESULTADOS-f1-m0-abstencao.md): parte do falso-positivo é
  **não situar** (atual vs histórico); só o topo discrimina.
- `~/Documents/NOTA-onedrive-git-observacao.md` (observação do dono — **arquivo externo ao repo**):
  uma análise comprimiu **artefatos com 2 anos de diferença** como se fossem eventos atuais.

## Perguntas de pesquisa (para quando estudarmos)

- A temporalidade melhora com (a) **datas explícitas + instrução de situar** (vimos ganho
  parcial), (b) **ferramentas/pesquisa** (liga ao eixo-pesquisa, F5 do roadmap), (c) **escala/
  capacidade** — ou é **fundamental** da arquitetura (não some no topo)?
- Os 4 problemas têm **raiz comum** (H-r1..r5) ou são distintos? Desenhar para **separá-los**.
- **Benchmark de confusão temporal** (a fixture H-D já registrada): artefatos datados, alguns
  superados, com a armadilha "nome-simples = velho / cópia = novo" — isola o eixo.
- **Modo longitudinal** (F6 do roadmap): reauditar um corpus que **mudou** — o teste natural de
  ordem-no-tempo, ausente da escada single-shot.

## Por que importa para o Strata

§3/§8 (rastreabilidade/história imutável), §5 (fonte única) e §6 (disciplina de fonte) são
**exatamente os antídotos** desse cluster. Se a limitação da IA for **fundamental**, o método
deixa de ser "boa prática" e vira o **andaime externo obrigatório**: o humano/método fornece o
que a IA não tem — situar no tempo, ordenar, e verificar a fonte primária. É a tese mais forte
possível para o Strata; por isso vale estudar a fundo.

## Estado
Hipótese/dossiê registrado. **Não estudar agora** — retomar com experimentos próprios.
Cruza com: **H-D** ([README.md](README.md)), e o roadmap F5 (pesquisa) e F6 (temporalidade/
longitudinal) em [PLANO-geral-modos-fechar-lacunas.md](PLANO-geral-modos-fechar-lacunas.md).
