---
title: Codigo, prosa e oraculo — o que documentar (e o que deletar)
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [00-core.methodology.md, lab-work.methodology.md, bibliography.methodology.md]
---

# Codigo, prosa e oraculo — o que documentar (e o que deletar)

> **Quando aplicar**: ao escrever prosa que descreve o que o codigo faz, ou
> ao decidir se um doc deve existir. Cross-cutting; refina o principio
> single-source (ver [00-core](00-core.methodology.md) — Pilares 2-3) para o
> caso doc-vs-codigo — critico quando o leitor (humano OU IA) ja' le o codigo.

**Problema**: IAs leem prosa E codigo. Descrever a mesma coisa nos dois e'
redundancia — mas nem toda redundancia e' igual. A util detecta divergencia;
a inutil so' espera pra driftar.

## Os dois artefatos acionaveis (leia primeiro)

### 1. Tabela de altitude — cada fato tem UMA fonte canonica — FORTE

DRY e' sobre **conhecimento**, nao texto de codigo (Hunt & Thomas: "every
piece of knowledge must have a single, unambiguous, authoritative
representation within a system"). E codigo e prosa **nao descrevem a mesma
coisa**: o codigo **over-especifica** (congela uma das N implementacoes
validas como se fosse essencial) e **under-especifica** (nao diz a faixa
permitida, o porque, as alternativas rejeitadas) — Parnas & Clements 1986.

| Tipo de informacao | Fonte canonica | NUNCA em prosa |
|---|---|---|
| **COMO** (mecanica, fluxo, linguagem) | codigo + docstring | re-narrar passo-a-passo |
| **Exemplo / contrato / invariante / numero** | teste, property, doctest, type, config | copiar o valor esperado |
| **PORQUE** (intencao, alternativa rejeitada, restricao, criterio de descarte) | ADR / `explanation/` | — e' o irredutivel; so' vive aqui |
| **Estrutura de sistema / limites** | 1 diagrama (C4-Context) | re-desenhar em cada doc |

O nivel "Code" do C4 raramente se documenta a mao — o codigo ja' e' a fonte;
prosa vive nas altitudes que o codigo nao mostra.

### 2. Teste de reconstrucao bidirecional — gate de admissao de cada doc — FORTE

Antes de escrever um paragrafo, pergunte:
1. **Apagado este texto, regenero do codigo/teste?** SIM -> nao escreva;
   deixe ponteiro (path + nome de funcao/teste) ou gere automatico.
2. **Apagado o codigo, este texto basta pra refazer?** NAO -> ele carrega o
   PORQUE; mantenha, curto.

So' sobrevive prosa que **falha (1) e passa (2)**. Formalmente: guarde so'
`K(doc | codigo)` — o que o doc acrescenta DADO o codigo (Kolmogorov/MDL);
paragrafo com `K~=0` (parafrase do codigo) e' deletavel. A assimetria e'
real: apagado o doc, a IA reconstroi o COMO mas **alucina o PORQUE**
(rationale reconstruction e' problema aberto — arXiv:2209.00398); apagada a
implementacao, a spec under-especificada gera N programas validos, nao O
programa. Ideal (Knuth, literate programming): nao "duas copias
sincronizadas", e' **UMA fonte da qual ambas derivam** — na era LLM, sync
bidirecional codigo<->prosa.

## Teoria de suporte

### Oraculo vs prosa — a redundancia UTIL e' executavel — FORTE

A redundancia entre "conta ate 10" (prosa) e o codigo so' e' UTIL se houver
um **artefato executavel que falha sozinho na divergencia** — teste,
property (Claessen & Hughes 2000), contrato (Meyer), doctest. **`assert
count == 10` e' redundancia util; "conta ate 10" em prosa e' drift
potencial** (22-42% dos comentarios divergem do codigo com o tempo — Wen et
al. ICPC 2019). Codigo **nao e' oraculo de si mesmo**: codigo que conta ate
11 esta "correto" sobre si proprio; so' um artefato que carrega a intencao
de forma independente pega o erro (Ulfers 2018). Em Python, **doctest** e' o
oraculo de menor custo; **tipos** sao doc executavel ("make illegal states
unrepresentable") — divergencia quebra o build.

### Rule of Three aplicado ao FLUXO de documentacao — FORTE

Nao formalize prosa de N=1 (a que mais drifta). Achado de lab fica no
`report.md`/`RESULT.md` (descartavel) ate reaparecer em >=3 labs/tickets;
so' entao consolida em doc formal (ver [lab-work](lab-work.methodology.md)).
AHA / "prefer duplication over the wrong abstraction" (Metz; Dodds): o caro
nao e' a copia de 1 ancora curta (1 numero, 1 nome — auto-corrige por
divergencia), e' o **paragrafo de explicacao que so' um lado vai manter**.

**Antipattern**: prosa-espelho (re-narra o codigo) — drift garantido,
ninguem confia depois (Parnas, *Software Aging*). **Antidoto**: o fato
checavel vira teste; a prosa fica so' com porque / restricao / descarte.

## Referencias

Ver [bibliography](bibliography.methodology.md) → "Codigo como documentacao /
nao-duplicacao".
