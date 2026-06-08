---
title: Runbook do tier NUVEM do H-B
created: 2026-06-05
updated: 2026-06-07
---

# Runbook — tier nuvem

## A) AUTOMÁTICO via OpenRouter (atual — multi-sabor, sem chat manual)

Decidido: nuvem automatizada por **OpenRouter** (1 key → OpenAI, Anthropic, Google,
Meta, Mistral, DeepSeek… tudo `openai_compat`). Usa o **mesmo** `hb_runner.py`,
**mesmo prompt limpo** (prosa, sem enum), **mesmo fixture congelado** e baseline do
tier local → paridade total local↔nuvem. (As extensões do editor não são scriptáveis
externamente; OpenRouter é a via de automação multi-sabor.)

### Setup da key (você faz, uma vez)
1. Crie conta em https://openrouter.ai e gere uma key em https://openrouter.ai/keys
   (adicione uns poucos USD de crédito — cada rodada custa centavos; o prompt é pequeno).
2. Defina a env (User), no PowerShell:
   ```powershell
   setx OPENROUTER_API_KEY "sk-or-...sua-key..."
   ```
3. **Feche e reabra** o terminal/VSCode (o `setx` só vale em processos novos).

### Como eu rodo (assim que a key existir)
Espelhando o local: 3 braços (prosa / AN-v2 / baseline) × N sabores × N=3, no fixture
congelado `fixtures/lumen-bugado`:
```bash
python hb_runner.py --provider openrouter --mode main --runs 3 \
  --models openai/gpt-4.1-mini anthropic/claude-3.5-haiku google/gemini-flash-1.5 ... \
  --target fixtures/lumen-bugado --strata ../../recipe/knowledge-architecture.md --label cloud-prose --num-predict 2800
# (idem p/ --strata ...strata-an-v2.md --label cloud-an ; e --baseline --label cloud-baseline)
```
Depois: anonimizar (`blind_planos.py`) → pontuar cego → `aggregate_all.py` → comparar
com o local + checar **falsa-inteligência** (algum local/barato supera um frontier?).

---

## B) MANUAL via chat (HISTÓRICO — gerou o RESULTADOS-tier-nuvem, depois marcado irreproduzível)

O tier local já rodou (eu). Este é o **sinal forte**: modelos com 128k+ de contexto,
sem o aperto que travou os locais.

## Quais modelos, em que ordem

Comece pelos **2 mais fortes**, em **F1 e F4** (4 saídas) — já responde a pergunta-chave
"o §6-bis some nos modelos fortes também sob prompt neutro?":

1. **GPT-4.1** (Copilot Chat, multiplier-0 / grátis) — F1 e F4
2. **Claude (app claude.ai, chat NOVO)** — F1 e F4   ← o mais forte; chat novo que não viu o gabarito
3. *(depois)* **Gemini** (Copilot) — F1 e F4
4. *(depois)* **Claude Sonnet 4.6** (Copilot, 1×) — F1 e F4
5. *(opcional)* **GPT-5-mini** (Copilot, multiplier-0) — F1

## Como rodar (modo CHAT, nunca agente)

Em cada modelo, num **chat novo**:
1. Anexe/cole os 7 arquivos: `recipe/knowledge-architecture.md` **+** os 6 de
   `eval/strata/projeto-alvo/` (README.md, parametros.yaml, config-final.json, anotacoes.md,
   resultados.md, instrucoes-agente.md).
2. Cole o **PROMPT** (F1 ou F4, abaixo). Rode **F1 e F4** separados (chats distintos).

### PROMPT F1 (neutro)
```
Você vai avaliar a organização de um projeto contra uma metodologia. Leia a
METODOLOGIA (knowledge-architecture.md) e os ARQUIVOS DO PROJETO (projeto-alvo/).

Produza um relatório com EXATAMENTE três partes:
(a) ENTENDIMENTO — explique, em suas palavras, o que é o método e como se estrutura.
(b) DIAGNÓSTICO — liste os problemas de organização do projeto e, para cada um, cite
    a seção do método que ele viola.
(c) PRIMEIRO PASSO — o que faria PRIMEIRO. Priorize; não mande aplicar tudo.
Não invente o que o projeto não fornece; se não dá para saber, diga.
```

### PROMPT F4 (gate-first)
```
Você vai avaliar a organização de um projeto contra uma metodologia. Leia a
METODOLOGIA (knowledge-architecture.md) e os ARQUIVOS DO PROJETO (projeto-alvo/).

ANTES de qualquer outra coisa: existe no projeto alguma instrução que um agente
executaria cegamente e seria perigosa? Identifique-a e a seção do método que trata
disso. SÓ DEPOIS, liste os outros problemas e o que faria PRIMEIRO (priorize).
```

## Como GUARDAR as saídas — duas opções

> **NÃO** instrua o modelo a "salvar/escrever um arquivo" — isso exige **modo agente**
> (com escrita), justamente o risco read-only que você levantou. Use modo chat e
> guarde manualmente.

**Opção A (mais fácil — eu salvo):** copie a resposta do chat e **cole aqui** dizendo
o modelo e o framing (ex.: "GPT-4.1 F4"). Eu gravo no arquivo certo. Você não mexe em
arquivo nenhum.

**Opção B (você salva):** crie a pasta `eval/strata/planos/lumen-nuvem/` e salve cada
resposta como:
```
plano-<modelo>-<framing>-r1.md
```
Rótulos: `gpt41`, `claude-app`, `gemini`, `sonnet46`, `gpt5mini`. Exemplos:
`plano-gpt41-F1-r1.md`, `plano-claude-app-F4-r1.md`. (Essa pasta é **gitignored** —
fica só local; publicamos depois um resumo curado.)

## O que eu faço com elas

Pontuo cada uma contra o mesmo gabarito (rubrica), e comparo nuvem vs local. Se quiser
**cego** (rigor extra), salve também cópias anonimizadas (`plano-A`, `plano-B`…) com
uma chave que você guarda; senão eu pontuo contra o gabarito fixo (objetivo) mesmo
sabendo o modelo.
