# Strata — arquitetura do conhecimento em camadas

Metodologia para **organizar, rastrear e gerar** conhecimento em projetos de
pesquisa, software científico ou qualquer trabalho intelectual que acumula
artefatos. O problema é **anterior ao computador**: bibliotecários, cientistas e
engenheiros o enfrentam há séculos. As ferramentas de cada era (hoje: IA,
editores, controle de versão) são **formas** que expressam esse método — moldam,
mas não fundam.

**Produto**: [`recipe/knowledge-architecture.md`](recipe/knowledge-architecture.md)
— 1 arquivo, ~800 linhas, portável. Licença: **CC BY-SA 4.0**.

---

## Como usar Strata no seu projeto

### 1. Leia a Parte I (L0 — núcleo atemporal)

A Parte I é **autônoma**: não menciona nenhuma ferramenta, não depende de git,
VSCode ou IA. Leia-a primeiro. Ela descreve 12 princípios que valem desde Pacioli
(1494) até qualquer substrato futuro.

```
§1  três tipos de artefato que conflitam
§2  as quatro perguntas que todo corpo de trabalho deve responder
§3  rastreabilidade (traço / superfície / conhecimento vivo)
§3-bis  força do artefato: o que ele constitui vs. o que ele registra
§4  registro científico (condicional ao eixo empírico)
§5  fonte única por altitude
§6  disciplina de fonte
§6-bis  autoridade para agir [eixo segurança]
§7  pipeline de maturação
§8  versionamento como história imutável
§9  economia do esforço — o regulador de todos os outros
§10 durabilidade do portador
```

**Quais seções se aplicam ao seu projeto?** A régua é §9:

| Condição | Seções que ativam |
|---|---|
| Sempre (qualquer projeto) | §1, §2, §5, §9 |
| Outro humano ou IA lê sem você presente | §3-bis (tipo-de-ato), §6 (vazio-tipado), §8 |
| Projeto gera dados empíricos/reproduzíveis | §4 (aparato estatístico) |
| Conhecimento recorre N≥3 vezes + projeto dura meses | §7 (maturação) |
| Artefatos precisam atravessar anos | §10 (redundância), §3-bis (chave de decifração) |
| Agente de IA com poder de execução | §6-bis (fail-closed — exceção: não aplique §9 aqui) |

### 2. Escolha formalizações na Parte II (L1)

A Parte II mapeia cada necessidade do L0 a padrões consolidados: ADR/MADR,
Diataxis, Conventional Commits, OAIS, etc. São recomendações, não obrigações —
cada entrada tem um **sinal de troca** que diz quando aposentar a formalização
sem aposentar o princípio.

### 3. Adapte as ferramentas na Parte III (L2)

A Parte III lista como as ferramentas de 2026 (agentes IA, git, editores) expressam
o L0/L1. **É destacável**: quando uma ferramenta mudar, só esta parte muda. Tudo
carrega `re-verify-by: 2026-09-01` — re-verifique na fonte antes de tratar como
verdade.

---

## Adotar em projeto existente (brownfield)

A metodologia não exige recomeço. A regra é: para cada coisa que seu projeto já
faz, pergunte que necessidade L0 ela cumpre.

- **Se cumpre** → é uma convenção local legítima, vence os nomes daqui. Mantenha.
- **Se nenhuma necessidade L0 é coberta** → acrescente o mínimo que para a dor
  imediata (§9).
- **Se viola um princípio marcado FORTE** → avalie o custo de troca (§9); se
  supera o ganho, registre como exceção com tombstone, não dívida silenciosa.
  Só mude imediatamente na fronteira §6-bis (fail-closed).

Nunca arranque o que funciona antes de entender por que existe (Cerca de
Chesterton, §6).

---

## Transportar para outro projeto

O arquivo `recipe/knowledge-architecture.md` é projetado para viajar sozinho:

- Todas as fundamentações são **inline** — nenhuma depende de link externo.
- As 3 camadas têm fronteiras explícitas (`# PARTE I / II / III`); você pode
  adotar só o L0 e ignorar L1/L2 sem perder coerência.
- O frontmatter declara `canonical-source` e `license` — qualquer cópia sabe
  de onde veio e sob que termos.

**Para usar:**
1. Copie `recipe/knowledge-architecture.md` para o seu repositório.
2. Leia a Parte I. Aplique o que o §9 mandar para a sua escala.
3. Atualize o campo `canonical-source` se fizer uma versão adaptada, e mantenha
   a licença CC BY-SA 4.0 nos derivados.

---

## Estrutura deste repositório

Este repositório é a **cozinha** onde Strata foi desenvolvido. O produto é o
arquivo acima; o resto é pesquisa.

| Pasta | O que é |
|---|---|
| [`recipe/`](recipe/) | **o produto**: `knowledge-architecture.md` |
| [`decisions/`](decisions/) | ADRs das decisões de design do método |
| [`lab/`](lab/) | pesquisa: experimentos, análises, varreduras (modo exploratório) |
| [`prototype/`](prototype/) | futuro: testar a receita em projetos reais |

Principais experimentos em `lab/`:

| Lab | O que documenta |
|---|---|
| [`2026-06-03-fundamentacao-L0/`](lab/2026-06-03-fundamentacao-L0/) | 22 fontes primárias do L0 verificadas na web |
| [`2026-06-03-future-proof-sweep/`](lab/2026-06-03-future-proof-sweep/) | varredura atemporalidade (2 rodadas, 15 agentes) |
| [`2026-06-04-aderencia-portabilidade/`](lab/2026-06-04-aderencia-portabilidade/) | análise de aderência, brownfield, IA e portabilidade |

---

## Licença

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) —
atribuição obrigatória, derivados sob a mesma licença.
