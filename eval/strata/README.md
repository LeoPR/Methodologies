---
title: H-B kit — aferir se IAs entendem e aplicam o Strata
created: 2026-06-05
status: pronto para o dono executar (rodar modelos) → avaliação cega volta aqui
strata_testado: v1.1.0 · SHA256 F678F235C338F13657371650CD3C02B1F124D5831B50588ADE04C899ED570A80 · 658 linhas
---

# H-B kit — os modelos entendem o Strata?

Mede empiricamente o claim "qualquer IA lê e aplica o Strata". **Variável isolada =
o modelo**; tudo o mais é fixo (o Strata congelado + o `projeto-alvo/` + o prompt).
Avaliação **cega** contra um gabarito de 7 problemas plantados.

## O que tem aqui

- `RASTREAMENTO-E-MELHORIA.md` — estado consolidado (o que ja era oficial, o que foi
  feito agora, onde houve confusao de trilha e como melhorar os proximos ciclos sem
  redescoberta).
- `projeto-alvo/` — projeto **deliberadamente bagunçado** (Lumen). É o que cada
  modelo avalia. Tem 7 problemas plantados (mapeados a seções do Strata).
- `gabarito.md` — a chave de respostas. **NÃO entregue aos modelos testados.** Só
  para a avaliação aqui.
- (você gera) `planos/` — a saída de cada modelo; `cego/` — versão anonimizada.

## Protocolo

> **Divisão de execução**: o **tier local** (Ollama) é rodado **automaticamente** pela
> sessão Claude (API `localhost:11434`); o **tier nuvem** (Copilot Chat + Claude
> frontier) é rodado **por você** (GUI). Eu não dirijo o Copilot Chat.
>
> **Prompt fixo = controle (F1)**: o prompt abaixo é mantido constante para isolar a
> variável *modelo*. A sensibilidade ao prompt é o **H-B′** (ver
> `../README.md`) — ablação à parte (1 modelo × vários framings). O resultado do H-B
> vale "sob o prompt F1".

### Modelos (rode/rodo cada um **2 vezes** p/ ver variância)
**Local (automático, eu rodo):** llama3.1:8b, qwen3:14b, qwen2.5-coder:7b,
deepseek-r1:8b, gemma3:12b, phi4 (spread de famílias/tamanhos).
**Nuvem (você roda):**
1. **Copilot Chat — GPT-4.1** (multiplier-0)
2. **Copilot Chat — GPT-5-mini ou Gemini** (outro multiplier-0)
3. **Copilot Chat — Claude Sonnet 4.6** (1x)
4. **Claude** (chat novo no app, OU sessão nova do Claude Code) — frontier
5. *(opcional, baseline fraca)* **Ollama local** — `llama3.1:8b` ou `qwen3:14b`

### Em cada modelo (chat NOVO, sem contexto prévio)
Anexe/cole o `knowledge-architecture.md` **e** os arquivos de `projeto-alvo/`, e dê
**exatamente** este prompt:

```
Você vai avaliar a organização de um projeto contra uma metodologia.

1. Leia o documento de metodologia anexo (knowledge-architecture.md — "Strata").
2. Leia os arquivos do projeto (pasta projeto-alvo/).
3. Produza um relatório com EXATAMENTE três partes:
   (a) ENTENDIMENTO — explique, em suas palavras, o que é o método e como ele se
       estrutura.
   (b) DIAGNÓSTICO — liste os problemas de organização do projeto e, para cada um,
       cite a seção do método que ele viola.
   (c) PRIMEIRO PASSO — o que você faria PRIMEIRO. Priorize; não mande aplicar tudo.

Não invente informação que o projeto não fornece. Se algo não dá para saber, diga.
```

Salve a saída como `planos/plano-<modelo>-r<N>.md` (ex.: `plano-gpt41-r1.md`).

### Anonimizar (para a avaliação ser cega)
Copie os planos para `cego/` renomeando para letras: `plano-A-r1.md`,
`plano-B-r1.md`, … Guarde um `chave.txt` (letra → modelo) que você **não me mostra**
até eu terminar de pontuar. Cole os planos anonimizados aqui no chat.

## Rubrica (eu pontuo cada plano cego, contra o `gabarito.md`)

| Dim. | Critério | Pontos |
|---|---|---|
| **A. Compreensão** | captou L0/L1/L2? (0–2) · captou §9 como régua? (0–2) · captou §6-bis/§4 (autoridade/honestidade)? (0–2) | 0–6 |
| **B. Detecção** | 1 ponto por problema plantado (P1–P7) detectado **com a seção certa**; ½ se achou mas errou a seção | 0–7 |
| **C. Priorização** | priorizou os de maior risco×menor custo (P7/P1) em vez de "tudo igual" / "refaça tudo"? | 0–2 |
| **D. Armadilhas** | −2 se caiu em N1 (mandar **apagar** a história/`velho/`) · −2 se caiu em N2 (aplicar as 12 seções) | penalidade |
| **E. Profundidade** | +1 honestidade (sinalizou o que não dá p/ saber) · +1 por sinal profundo (P7=prompt injection; P1=§5; lexicon=traço a tombstone) | bônus 0–2 |

**Total** ≈ A + B + C − D + E (máx ~17). O número importa **menos** que o **padrão**:
onde TODOS os modelos erram a mesma coisa, é o **texto do Strata** que precisa de
gate mais explícito → alimenta o H-C (versão AI-nativa).

## Conflito de interesse (Claude é juiz E participante)
Mitigação: (1) **cego** — pontuo sem saber qual é o Claude; (2) **rubrica objetiva**
contra o gabarito, não "qual é o melhor"; (3) *opcional* — peça a um modelo de outra
família para pontuar os mesmos planos cegos com esta rubrica, como 2º juiz.

## Coleta de saídas + segurança (read-only)

**Onde as saídas vão** — `eval/strata/planos/` (criada pelo `hb_runner.py`), uma subpasta
por alvo:
- `planos/lumen/` — tier local sobre o fixture (F1).
- `planos/lumen-hb-prime/` — H-B′ (qwen3:8b × F1–F4).
- `planos/<projeto>/` — quando rodar em projeto real.

Você e eu visualizamos os arquivos localmente. **`planos/` é gitignored**: as
avaliações de projetos REAIS (NNN/TCF/pdf2md/project_ia) são **privadas** — não vão
ao GitHub. Publicamos só um **resumo curado** depois.

**Garantias read-only (o risco de "modelo surtar e modificar")**:
- **Completion-only**: `hb_runner.py` chama `/api/chat` (texto entra, texto sai). O
  modelo **não tem ferramenta** — não executa comando nem toca em arquivo. O pior de
  um modelo surtado é escrever texto no arquivo de saída.
- O projeto-alvo é lido com `open('r')` (read-only). **Nada** é escrito fora de `--out`.
- **Guard**: o runner recusa `--out` fora do `eval/strata/` (não deixa escrever em projeto
  alheio).
- **Nunca usar modo agente** (Claude Code / Copilot agent com tools de escrita) para o
  H-B. O modelo só recebe contexto e devolve um plano.

## Generalizar para projetos reais (NNN, TCF, pdf2md, project_ia)

O fixture `lumen` tem gabarito (scoring objetivo). Projetos reais **não** têm gabarito
— testam validade ecológica (a avaliação é útil/sensata para um projeto de verdade?),
julgada por mim + por você que conhece o projeto.

- **Tier local (eu rodo)**: `python hb_runner.py --target <caminho-do-projeto> --label <nome>`.
  O runner lê o projeto **read-only** (amostra de arquivos de texto, pula binários e
  arquivos grandes; trunca no limite de contexto) e escreve em `planos/<nome>/`.
- **Tier nuvem (você roda)**: no Copilot Chat / Claude, use **modo chat** (não agente);
  anexe/cole os arquivos do projeto + o Strata. Nunca dê a um agente com escrita.
- **Cuidado de contexto**: um projeto real pode exceder a janela; o runner amostra e
  trunca. Para projetos grandes, a leitura precisa ser seletiva (estrutura + arquivos-
  chave) — refinamento futuro.

## O que decidimos com o resultado
- **Todos pontuam alto** (detecção + compreensão) → o claim de portabilidade-para-IA
  está **validado**; remover o "ainda não comprovado" do `recipe/README.md`.
- **Buraco sistemático** (ex.: todos perdem P7/§6-bis, ou tratam P1 como "arquivo
  duplicado" e não §5) → o Strata precisa de GATES mais explícitos ali → **H-C**.
- Variância intra-modelo alta → o texto é ambíguo naquele ponto.

## Matriz automatica (modelos x cenarios)

Para fechar o "menor modelo que resolve totalmente" e reduzir inferencia manual,
este kit agora inclui uma malha automatica:

- `matrix_models.json` — catalogo de modelos online/offline (do mais forte ao mais barato).
- `scenario_manifest.json` — cenarios e expectativa por cenario (P1..P7).
- `hb_matrix_runner.py` — executa matriz em batch (completion-only, sem tools).
- `hb_matrix_score.py` — pontua automaticamente e marca `pass_full`.
- `cenarios/` — projetos sinteticos: comum, pesquisa, simples, bem-formatado e borda.

### Criterio de "resolve totalmente"

Um teste passa em `pass_full=true` quando:

1. detecta **todos** os problemas esperados do cenario com seção correta;
2. nao cai nas armadilhas N1/N2;
3. respeita o teto de alucinacao do cenario.

### Como rodar (offline primeiro)

```bash
python hb_matrix_runner.py --channels offline --framing F1 F4 --runs 2
```

Isso cria uma pasta timestamp em `planos/matrix/` com `index.json` + saidas brutas/json.

Depois pontue:

```bash
python hb_matrix_score.py --run planos/matrix/<timestamp>
```

Saidas do score:

- `score.csv` (linha por teste)
- `score-summary.md` (agregado por modelo)

### Como ligar online (frontier ate barato)

1. Ative os modelos desejados em `matrix_models.json` (`enabled: true`).
2. Defina as chaves de API (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`).
3. Rode por canal:

```bash
python hb_matrix_runner.py --channels online --framing F1 F4 --runs 1
python hb_matrix_score.py --run planos/matrix/<timestamp-online>
```

### Observacoes importantes

- O harness e completion-only; nao executa comandos do projeto-alvo.
- `planos/` segue gitignored (dados brutos ficam locais).
- O menor modelo confiavel e definido por **taxa de pass_full** ao longo de todos os
  cenarios, nao por um unico fixture.

## Caminho feliz revisado (auto calibragem por divisao)

Objetivo: mapear limite de contexto e limite de capacidade do modelo sem explosao
combinatoria, no estilo de testador de limite de equipamento.

### Etapa A — Tatear possivel/impossivel rapidamente

1. Rode com metodo curto (`strata-an-v1.md`) e 1 cenario simples para validar pipeline.
2. Confirme que o modelo responde JSON valido no runner.
3. Se falhar aqui, o modelo fica marcado como inviavel para o Strata operacional.

### Etapa B — Buscar maior contexto viavel por modelo (binaria)

Para cada modelo local:

1. teste `ctx_min` e `ctx_max`;
2. aplique busca binaria ate achar o maior `num_ctx` que ainda responde com qualidade minima;
3. salve o `best_ctx` por modelo.

Isso separa limites fisicos (contexto/memoria) de limites cognitivos (qualidade).

### Etapa C — Buscar menor modelo que ainda resolve totalmente (binaria)

Com `best_ctx` fixado por modelo:

1. ordene modelos do mais forte ao mais fraco;
2. rode extremos (maior e menor) para criar bracket de possivel/impossivel;
3. rode busca binaria no eixo de modelos para achar a fronteira;
4. valide vizinhos da fronteira para reduzir risco de nao-monotonia.

### Etapa D — Escolha otima no cobertor curto

Entre os que passam no target:

1. maximize `pass_full_rate`;
2. maximize score medio;
3. maximize throughput (decode_tps);
4. minimize tamanho/uso de memoria.

### Comando pronto (offline)

```bash
python hb_limit_search.py --method strata-an-v1.md --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --ctx-min 4096 --ctx-max 32768 --runs 1 --target-pass-rate 1.0 --timeout-s 240
```

### Execucao em RTX 3060 12GB (um modelo por vez)

Se a GPU nao comporta dois modelos grandes ao mesmo tempo, rode o limite em modo
serial. Regra pratica:

1. aquece e mede **um** modelo;
2. descarrega o modelo (`ollama stop <modelo>`);
3. so depois carrega o proximo.

Exemplo por modelo (offline):

```bash
python hb_limit_search.py --method strata-an-v1.md --only-model qwen3-1.7b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --ctx-min 4096 --ctx-max 12288 --runs 1 --target-pass-rate 1.0 --timeout-s 120
```

Depois descarregue explicitamente antes do proximo:

```bash
ollama stop qwen3:1.7b
```

Para reduzir cold start de disco, priorize esta ordem de trabalho:

1. modelo pequeno para validar pipeline;
2. modelo medio principal;
3. modelos maiores por ultimo.

O kit inclui um orquestrador serial pronto: `run_limit_search_serial.ps1`.

## Protocolo de evidencia (foco em "funciona e entende")

Para responder com evidencia forte se o Strata funciona em IAs modernas, use 3 etapas.

### Etapa 1: entendimento (diagnostico)

Medimos se o modelo entende e diagnostica com base no Strata.

1. rode limit-search em modo serial (um modelo por vez);
2. registre `best_ctx`, `pass_full_rate`, score e throughput.

Exemplo:

```bash
pwsh -NoProfile -File eval/strata/run_limit_search_serial.ps1 -CtxMin 4096 -CtxMax 12288 -TimeoutS 120
```

### Etapa 2: acao proposta (o que ele faria)

Avaliamos se o primeiro passo e os artefatos propostos sao concretos e coerentes.

- local (Ollama): use o `hb_l2_sandbox.py` para pedir entendimento + pacote minimo L2.
- nuvem (Copilot/Claude): execute o mesmo prompt, salve a resposta em JSON e pontue com os mesmos criterios.

Exemplo local:

```bash
python hb_l2_sandbox.py --model qwen3:1.7b --timeout-s 180
```

Para modelos de nuvem (ex.: Copilot GPT-5-mini), rode no chat e salve a resposta
em arquivo texto. Depois pontue com o mesmo criterio:

```bash
python hb_l2_score_external.py --input <resposta-modelo.txt> --label copilot-gpt5mini
```

### Etapa 3: sandbox isolado com controle de versao

Verificamos se o modelo gera arquivos de controle/versionamento sem tocar no projeto real.

- a escrita ocorre somente em `planos/l2-sandbox/<timestamp>/<modelo>/generated`;
- o script inicializa git local no sandbox e grava commit de evidencia;
- criterio minimo: cobertura de grupos (controle, versionamento, decisao, operacao) + entendimento L0/L1/L2.

### Inventario consolidado de testes

Para ver rapidamente o que ja foi testado:

```bash
python hb_test_inventory.py
```

Saida em `planos/evidence/<timestamp>/` com:

- `inventory.json`
- `inventory.md`

Saidas:

- `planos/limit-search/<timestamp>/limit-search.json`
- `planos/limit-search/<timestamp>/limit-search-summary.md`

### Quando subir para metodo completo

So depois de fechar fronteira no metodo curto. Em seguida, re-rodar com
`knowledge-architecture.md` nos modelos candidatos para medir a queda real de capacidade.

Isso documenta explicitamente onde o Strata e util para o dev dado o ambiente dele,
sem exigir que o proprio modelo "fraco" saiba se autoavaliar.
