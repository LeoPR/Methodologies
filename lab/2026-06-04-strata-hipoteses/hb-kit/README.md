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

- `projeto-alvo/` — projeto **deliberadamente bagunçado** (Lumen). É o que cada
  modelo avalia. Tem 7 problemas plantados (mapeados a seções do Strata).
- `gabarito.md` — a chave de respostas. **NÃO entregue aos modelos testados.** Só
  para a avaliação aqui.
- (você gera) `planos/` — a saída de cada modelo; `cego/` — versão anonimizada.

## Protocolo (você roda)

### Modelos sugeridos (≥4; rode cada um **2 vezes** p/ ver variância)
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

## O que decidimos com o resultado
- **Todos pontuam alto** (detecção + compreensão) → o claim de portabilidade-para-IA
  está **validado**; remover o "ainda não comprovado" do `recipe/README.md`.
- **Buraco sistemático** (ex.: todos perdem P7/§6-bis, ou tratam P1 como "arquivo
  duplicado" e não §5) → o Strata precisa de GATES mais explícitos ali → **H-C**.
- Variância intra-modelo alta → o texto é ambíguo naquele ponto.
