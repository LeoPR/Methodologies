---
title: Execucao local endurecida (8B + 4B)
date: 2026-06-06
status: parcial (4B concluido, 8B em execucao interrompida por limite de sessao)
---

# Execucao local endurecida (passo 1)

Escopo desta rodada: executar protocolo local em 2 modelos-alvo (um 8B e um 4B),
com N=5 e 3 cenarios (`s03-simples`, `s01-comum-brownfield`, `s04-bem-formatado`).

## Parametros usados

- metodo: `strata-an-v1.md`
- ctx: fixo 4096 (para reduzir tempo de resposta e manter comparabilidade)
- runs: 5
- target_pass_rate: 0.8
- timeout por chamada: 60s

## Modelo 4B (concluido)

Comando:

```powershell
c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/.venv/Scripts/python.exe hb_limit_search.py --method strata-an-v1.md --only-model gemma3-4b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --ctx-min 4096 --ctx-max 4096 --runs 5 --target-pass-rate 0.8 --timeout-s 60
```

Saida:
- `planos/limit-search/20260606-201531/limit-search-summary.md`
- `planos/limit-search/20260606-201531/limit-search.json`

Resultado:
- best_ctx = 0
- pass_full_rate = 0.00
- mean_score = 0.00
- veredito desta rodada: REPROVADO para fechamento local forte

## Modelo 8B (parcial)

Comando:

```powershell
c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/.venv/Scripts/python.exe hb_limit_search.py --method strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --ctx-min 4096 --ctx-max 4096 --runs 5 --target-pass-rate 0.8 --timeout-s 60
```

Progresso observado:
- `CTX search -> llama3.1-8b (llama3.1:8b)`
- `best_ctx=4096`
- `EVAL -> llama3.1-8b (llama3.1:8b)`

Estado:
- avaliacao iniciou, mas nao concluiu dentro da janela operacional da sessao.
- pasta criada e aguardando artefato final: `planos/limit-search/20260606-201642/`

## Proximo disparo recomendado (retomar 8B)

```powershell
Set-Location "c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/lab/2026-06-04-strata-hipoteses/hb-kit"
c:/Users/leona/OneDrive/Documents/Projects/Acadêmicos/Methodologies/.venv/Scripts/python.exe hb_limit_search.py --method strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --ctx-min 4096 --ctx-max 4096 --runs 5 --target-pass-rate 0.8 --timeout-s 60
```

Ao concluir, usar `limit-search-summary.md` para preencher o placar de aceite local
(N>=5, gates de borda e estabilidade intercenario).

## Investigacao adicional (contexto/timeout/defaults) — 2026-06-06

Motivo: validar se o bloqueio era timeout pequeno e se o harness estava forçando
contexto/predicao em vez de usar defaults do modelo.

### Achados

1. **Defaults reais do Ollama (confirmados com `ollama show`)**:
	 - `qwen3:8b`: context length 40960
	 - `llama3.1:8b`: context length 131072
	 - `gemma3:4b`: context length 131072
2. O `hb_limit_search.py` forçava `num_ctx`/`num_predict` em toda chamada; nao havia
	 modo explicito para usar defaults.
3. O probe de contexto estava descartando execucoes validas por exigir JSON perfeito,
	 confundindo erro de parse com falha de contexto/tempo.

### Ajustes aplicados no harness

Arquivo: `lab/2026-06-04-strata-hipoteses/hb-kit/hb_limit_search.py`

- `--use-model-default-context`
- `--use-model-default-num-predict`
- `--num-predict-override`
- `--probe-timeout-s` e `--eval-timeout-s` (separados)
- `--dry-run` para auditar payload antes de rodar
- `--force-json-format` (payload Ollama `format=json`)
- `--verbose` com parametros efetivos por run
- diagnostico expandido em erro (`error_type`, `raw_preview`, `elapsed_s`, `decode_tps`)

### Evidencia de validacao dos ajustes

- Dry-run auditavel salvo em:
	`planos/limit-search/20260606-224918/limit-search-dry-run.json`
- Smoke run concluido com defaults de contexto + parametros explicitos:
	`planos/limit-search/20260606-225121/limit-search.json`
	`planos/limit-search/20260606-225121/limit-search-summary.md`
- Smoke run apos correcoes de fluxo e serializacao:
	`planos/limit-search/20260606-225036/` e `planos/limit-search/20260606-225121/`

### Conclusao desta investigacao

O experimento agora roda de forma **lenta, explicita e auditavel**. O gargalo atual
nao e "contexto automatico" em si, mas robustez de JSON de saida no scoring; por isso
foi adotada subida gradual de `num_predict`/timeouts e coleta de `raw_preview` antes de
abrir lote N>=5.

## Incremento controlado (passo 1) — num_predict 512 e 1024

Rodadas executadas no mesmo setup:

- modelo: `llama3.1-8b`
- cenario: `s03-simples`
- runs: 1
- contexto: default do modelo
- `force_json_format`: ativo

### Rodada A — num_predict=512

Artefato: `planos/limit-search/20260606-225600/limit-search.json`

Resumo:
- probe: `probe_json_ok=false` (parse falhou no probe)
- avaliacao: `status=ok` (parse valido no eval)
- tempo eval: ~11.62s
- decode_tps: ~44.39

### Rodada B — num_predict=1024

Artefato: `planos/limit-search/20260606-225628/limit-search.json`

Resumo:
- probe: `probe_json_ok=true`
- avaliacao: `status=ok`
- tempo eval: ~11.58s
- decode_tps: ~44.48

### Conclusao operacional

Para este modelo e cenario, `num_predict=1024` estabilizou o parse (probe+eval) sem
aumento relevante de latencia versus 512. Proximo passo recomendado: manter 1024 e abrir
3 cenarios com `runs=1` antes de subir para `runs=5`.

## Rodada 3 cenarios (runs=1) — executada

Comando executado (baseline estabilizado):

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 1 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 45 --eval-timeout-s 180 --force-json-format --verbose
```

Artefatos:
- `planos/limit-search/20260606-232756/limit-search.json`
- `planos/limit-search/20260606-232756/limit-search-summary.md`

### Resultados

- probe contexto (default): `ok=true`, `probe_json_ok=true`
- tests: 3
- pass_full_rate: 0.00 (0/3)
- mean_score: 0.17
- median_decode_tps: ~46.00
- median_elapsed_s: ~13.03

Detalhe por cenario:
- `s01-comum-brownfield`: score 3.0, detection_correct 1/5, hallucinated 2, sem N1/N2
- `s03-simples`: score -0.5, detection_correct 0/2, hallucinated 5, caiu em N2
- `s04-bem-formatado` (limpo): score -2.0, hallucinated 6, caiu em N2

### Deducoes para reavaliacao posterior

1. A trilha de **execucao** esta estavel (sem timeout/travamento) com contexto default
	+ `num_predict=1024`; o problema principal migrou para qualidade de julgamento.
2. O modelo apresenta **falso-positivo alto** no cenario limpo (`s04`) e ativacao de
	N2 em cenarios que nao deveriam induzir "aplicar tudo".
3. Em `s01`, houve alguma tracao (1/5) sem armadilhas N1/N2, indicando que o modelo
	nao esta totalmente "cego", mas ainda longe do criterio de fechamento forte.
4. A reavaliacao deve focar primeiro em reduzir N2/falso-positivo antes de escalar
	para N>=5 (caso contrario, so amplifica erro sistematico).

## Mitigacao pre-escala (anti-N2/falso-positivo) — executada

Objetivo: validar uma mitigacao simples antes de escalar `runs`.

Mudanca no harness:
- novo flag `--anti-n2-guard` em `hb_limit_search.py`, adicionando regra conservadora:
  evitar "aplicar tudo", exigir evidencia textual e permitir findings vazio em cenario limpo.

Comando executado:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 1 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 45 --eval-timeout-s 180 --force-json-format --anti-n2-guard --verbose
```

Artefato:
- `planos/limit-search/20260606-233300/limit-search.json`

Comparacao direta (vs rodada base `20260606-232756`):

1. `mean_score`: **0.17 -> 1.50** (melhora)
2. `penalty_n2`:
	- `s03`: **2 -> 0**
	- `s04`: **2 -> 0**
3. alucinacao:
	- `s03`: **5 -> 3**
	- `s04`: **6 -> 3**
4. `pass_full_rate`: manteve **0.00**

### Deducoes

1. A mitigacao conservadora funcionou para reduzir armadilha N2 e parte do falso-positivo.
2. Ainda nao fecha criterio forte: continua sem passar `pass_full` e com alucinacao acima do
	aceitavel no cenario limpo.
3. Para escalar com utilidade, faz sentido subir para `runs=5` **com o guard ativo** e avaliar
	variancia do erro residual (nao voltar ao prompt sem guard).

## Investigacao de contexto/default com observacao externa (Ollama Docker)

Objetivo: confirmar se "default" de contexto realmente nao envia parametro e se o
servidor escala sozinho para contextos altos, usando `docker logs` para observacao externa.

### Ambiente confirmado

- Ollama em container: `ollama/ollama` (`docker ps`)
- Metodo grande para estressar contexto: `recipe/knowledge-architecture.md`
  (prompt ~52k chars por cenario no dry-run)

### Achados tecnicos

1. **Semantica de default corrigida no harness**:
	- antes: `--use-model-default-num-predict` ainda herdava `num_predict` do catalogo;
	- depois: modo default verdadeiro (nao envia `num_ctx` nem `num_predict`).

2. **Default real observado no servidor (logs)**:
	- em run default verdadeiro (`20260607-004111`), o servidor operou com
	  `n_ctx_slot = 32768` para prompt de ~16841 tokens;
	- ou seja, o "default" efetivo do servidor neste ambiente ficou em 32768, nao 131072.

3. **Forcando `ctx=32768`**:
	- comportamento equivalente ao default observado (`n_ctx_slot = 32768`), sem ganho claro.

4. **Forcando `ctx=65536`**:
	- run anterior (`20260607-004154`) falhou no probe com timeout;
	- logs mostram tentativa de encaixe de memoria com contexto alto e ajuste de camadas
	  (fit agressivo em VRAM/host), sem fechar probe de forma estavel.

5. **Deducao operacional**:
	- no hardware atual (RTX 3060 12GB), o teto pratico para este workload parece estar
	  no regime de 32768 de contexto efetivo.
	- forcar acima disso aumenta risco de timeout/instabilidade sem beneficio comprovado.

### Artefatos relevantes desta etapa

- dry-run metodo grande: `planos/limit-search/20260607-003851/`
- default verdadeiro + logs: `planos/limit-search/20260607-004111/`
- forcado 32768 + logs: `planos/limit-search/20260607-003954/`
- forcado 65536 (falha probe): `planos/limit-search/20260607-004154/`

## Continuidade (proximos runs) — 2026-06-07

Objetivo: executar a escala local com configuracao estavel e abrir varredura de
modelos offline sob o mesmo protocolo.

### Rodada A — escala `runs=5` com defaults totais

Comando:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 5 --target-pass-rate 0.0 --use-model-default-context --use-model-default-num-predict --probe-timeout-s 45 --eval-timeout-s 180 --force-json-format --anti-n2-guard --verbose
```

Artefato:
- `planos/limit-search/20260607-004806/limit-search.json`

Resultado:
- probe: timeout (`best_ctx=0`)
- tests executados: 0

Leitura:
- `num_predict` em default puro neste setup nao foi robusto para abertura de lote
	com `probe_timeout_s=45`.

### Rodada B — escala `runs=5` com `num_predict=1024`

Comando:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 5 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 45 --eval-timeout-s 180 --force-json-format --anti-n2-guard --verbose
```

Artefato:
- `planos/limit-search/20260607-004937/limit-search.json`

Resultado:
- probe: timeout (`best_ctx=0`)
- tests executados: 0

Leitura:
- timeout de probe permaneceu mesmo com `num_predict=1024`, indicando gargalo
	operacional (cold start/latencia inicial) acima de 45s em parte das tentativas.

### Rodada C — scouting multi-modelo local (runs=1)

Comando:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 1 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 45 --eval-timeout-s 180 --force-json-format --anti-n2-guard
```

Artefato:
- `planos/limit-search/20260607-005027/limit-search.json`

Resumo:
- `qwen3-8b`, `qwen2.5-coder-7b`, `llama3.1-8b`, `gemma3-4b`: timeout no probe
	(`best_ctx=0`, sem testes)
- `qwen3-1.7b`: probe e avaliacao concluida (3 testes), `pass_full_rate=0.00`,
	`mean_score=0.75`, com erro de parse em `s04`.

Leitura:
- o protocolo separou dois gargalos independentes:
	1) infraestrutura de abertura de rodada (probe timeout em modelos maiores);
	2) qualidade/JSON em modelos que passam do probe.

### Tentativa D — probe ampliado (`probe_timeout_s=120`)

Comando disparado para `llama3.1-8b` com `num_predict=1024` e `runs=5`:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 5 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 120 --eval-timeout-s 180 --force-json-format --anti-n2-guard --verbose
```

Estado:
- execucao iniciou e entrou em avaliacao (`RUN ... r=1/5` observado), mas foi
	interrompida manualmente antes de persistir artefato final.
- pasta criada sem artefatos: `planos/limit-search/20260607-005453/`.

## Deducoes operacionais desta continuidade

1. O ciclo local precisa de regra explicita de aquecimento antes do `probe` para
	 modelos >=4B, ou timeout de probe maior por classe de modelo.
2. Sem estabilizar o probe, a escala em `runs>=5` vira medicao de latencia de
	 inicializacao, nao medicao metodologica.
3. Mesmo quando passa do probe (`qwen3-1.7b`), ainda ha lacuna de qualidade
	 (`pass_full=0`) e robustez de JSON (`s04` com parse invalido).
4. A trilha local deve tratar infraestrutura e julgamento como gates separados,
	 para nao misturar causa de falha.

## Expansao de catalogo e triagem moderna via Ollama — 2026-06-07

Objetivo: incorporar candidatos mais modernos ao catalogo do harness, baixar os que
nao estavam locais e abrir triagem comparavel sem sair do protocolo atual.

### Catalogo ampliado no harness

Arquivo atualizado:
- `lab/2026-06-04-strata-hipoteses/hb-kit/matrix_models.json`

Novos ids adicionados ao catalogo offline:
- `deepseek-r1-8b`
- `granite3.3-8b`
- `mistral-nemo-12b`
- `phi4-14b`
- `qwen3-4b`
- `nemotron-3-nano-4b`
- `gemma3-1b`
- `qwen3-0.6b`
- `granite4.1-8b`
- `lfm2.5-8b`

### Pulls e disponibilidade local confirmada

Comandos relevantes:

```powershell
ollama pull granite4.1:8b
ollama pull nemotron-3-nano:4b
ollama list | Select-String -Pattern "granite4.1|nemotron-3-nano"
```

Resultado:
- `granite4.1:8b` entrou no inventario local (`5.3 GB`)
- `nemotron-3-nano:4b` entrou no inventario local (`2.8 GB`)

Warm-up operacional executado:
- `ollama run granite4.1:8b "Responda apenas: ok"`
- `ollama run nemotron-3-nano:4b "Responda apenas: ok"`
- `ollama run granite3.3:8b "Responda apenas: ok"`
- `ollama run deepseek-r1:8b "Responda apenas: ok"`

### Tentativas amplas de triagem (abortadas)

Rodadas abertas e interrompidas por latencia de probe sem artefato final:
- `planos/limit-search/20260607-020017/`
- `planos/limit-search/20260607-020154/`

Leitura:
- mesmo com aquecimento parcial, a triagem larga continua cara demais quando mistura
  varios modelos pequenos e medios no mesmo lote.
- para scouting inicial, o caminho mais confiavel foi rodar modelos individualmente.

### Smoke individual 1 — `qwen3-0.6b`

Comando:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model qwen3-0.6b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 1 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 60 --eval-timeout-s 180 --force-json-format --anti-n2-guard
```

Artefato:
- `planos/limit-search/20260607-020423/limit-search.json`

Resumo:
- probe: ok (`probe_json_ok=true`)
- tests: 3
- `pass_full_rate=0.00`
- `mean_score=0.00`
- `median_decode_tps ~184.14`

Leitura:
- excelente velocidade e abertura operacional;
- qualidade de julgamento insuficiente, com deteccao nula e alucinacao alta em `s03`.

### Smoke individual 2 — `gemma3-1b`

Comando:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model gemma3-1b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 1 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 60 --eval-timeout-s 180 --force-json-format --anti-n2-guard
```

Artefato:
- `planos/limit-search/20260607-020506/limit-search.json`

Resumo:
- probe: ok (`probe_json_ok=true`)
- tests: 3
- `pass_full_rate=0.00`
- `mean_score=2.50`
- `median_decode_tps ~91.84`
- dois cenarios com `JSONDecodeError`

Leitura:
- o modelo mostra tracao semantica maior que `qwen3-0.6b`;
- porem a robustez de formato ainda e' fraca demais para uso confiavel no scorer atual.

## Deducoes desta triagem moderna

1. Modelos muito pequenos podem ser operacionalmente estaveis e velozes, mas ainda
	insuficientes para fechamento local forte.
2. `gemma3-1b` e' mais promissor que `qwen3-0.6b` em conteudo, mas hoje perde no gate
	de serializacao JSON.
3. `granite4.1:8b` e `nemotron-3-nano:4b` ja estao locais e prontos para triagem
	individual posterior; a proxima rodada deve ser **um modelo por vez**, nao em lote.
