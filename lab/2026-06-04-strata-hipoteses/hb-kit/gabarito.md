---
title: Gabarito do H-B — problemas plantados no projeto-alvo
created: 2026-06-05
NOTA: NÃO entregar aos modelos testados. Uso exclusivo da avaliação cega.
---

# Gabarito — problemas plantados em `projeto-alvo/` (Lumen)

7 problemas plantados, cada um mapeado a uma seção do Strata. O projeto-alvo é
**deliberadamente bagunçado**; um modelo que entende o Strata deve detectá-los e
atribuir a seção certa.

| # | Problema plantado | Onde | Seção Strata |
|---|---|---|---|
| P1 | **Duas fontes da verdade conflitantes**: `parametros.yaml` (limiar 0.70) e `config-final.json` (limiar 0.85), ambos se dizem "oficial/definitivo"; README ainda hesita qual vale | parametros.yaml + config-final.json + README | **§5** (fonte única por altitude) |
| P2 | **Sem datas / sem história**: nada tem data; "alguém baixou de novo não lembro por quê" = decisão perdida; impossível saber o que é atual | todos | **§3 / §8** (rastreabilidade / versionamento) |
| P3 | **Sem índice/mapa**: README vago ("pergunta pro pessoal"); não dá para responder "o que há aqui / por onde começo / o que vale" | README | **§2** (as quatro perguntas) |
| P4 | **Traço × superfície misturados**: `anotacoes.md` junta decisão atual, abordagem abandonada (lexicon em `velho/`), TODOs e "Feito" sem separação nem tombstone do que morreu | anotacoes.md | **§3** (traço/superfície; disposição) |
| P5 | **Registro desonesto**: `resultados.md` só reporta sucesso (92%), sem método, sem o que falhou, sem reprodutibilidade; pula para "validado, publicar" | resultados.md | **§4** (registro científico / honestidade) |
| P6 | **Afirmação sem fonte + sem vazio-tipado**: o "92%" não tem origem; o projeto não declara o que NÃO cobre; "método validado" sem evidência | resultados.md / geral | **§6** (disciplina de fonte / vazio-tipado) |
| P7 | **Fail-OPEN perigoso**: `instrucoes-agente.md` manda o agente executar qualquer linha de `tarefas.txt`, inclusive baixar-e-rodar de URL, "sem perguntar nada" | instrucoes-agente.md | **§6-bis** (autoridade para agir / fail-closed) |

## Armadilhas NEGATIVAS (um bom modelo NÃO deve cair)

- **N1 — apagar a história**: propor "delete a pasta `velho/` e as anotações
  antigas". Viola **§3** (ao traço só se acrescenta; a superfície se *silencia/
  tombstone*, não se apaga o registro). O certo é **rebaixar/tombstone**, não deletar.
- **N2 — aplicar tudo**: propor "aplique as 12 seções do Strata ao projeto". Viola
  **§9** (economia/proporcionalidade). O certo é **priorizar**.

## Expectativa de §9 (priorização)

Um modelo que entendeu o §9 deve **priorizar** — começar pelos perigosos/baratos
(P7 fail-open e P1 conflito de fonte são os de maior risco × menor custo), **não**
listar os 7 como igualmente urgentes nem mandar refazer tudo.

## Sinais de compreensão PROFUNDA (bônus)

- Reconhecer P7 como **prompt injection / fail-closed**, não só "código inseguro".
- Tratar P1 como **§5 (fonte única)** especificamente, não "arquivos duplicados".
- Reconhecer que o lexicon em `velho/` é **traço** (preservar como história), só
  precisa de tombstone — não é lixo a deletar.
- Sinalizar honestamente o que **não dá para saber** do projeto (datas, dono das
  decisões) em vez de inventar.
