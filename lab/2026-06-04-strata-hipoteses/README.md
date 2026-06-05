---
title: Hipóteses abertas do Strata — código-como-documento + aferição de compreensão por IA
status: open
created: 2026-06-04
tags: [strata, hipotese, doc-vs-code, ia-compreensao, benchmark, qualidade-de-metodo]
---

# Hipóteses abertas do Strata

> Duas hipóteses de refinamento/validação do Strata, registradas para discutir e
> testar depois. Nenhuma decisão tomada.

## H-A — O arquivo de código tratado, em algum grau, como documento

**A ideia (do dono)**: o próprio arquivo de código-fonte de um programa é, em
algum grau, um **documento** — não só um executável. Ele carrega decisões,
intenção e conhecimento; comentários são documentação; a estrutura é um registro.

**Não é totalmente novo** — já foi tocado:
- `lab/2026-06-03-modernizacao/experimento-split/doc-vs-code.methodology.md`
  (a fronteira doc-vs-código no experimento de suíte).
- **§3-bis** do produto (dispositivo vs probatório): o código que **roda** é
  *dispositivo* (constitui o sistema); o código como **registro** do que foi
  decidido é *probatório* (documenta). A hipótese é a mesma distinção, vista do
  outro lado: um único artefato é, ao mesmo tempo, executável E documento.

**O que falta discutir**:
- Até que grau? (comentário = doc óbvio; nomes/estrutura = doc implícito; o binário
  compilado = quase só dispositivo). Há um gradiente, não um binário.
- O Strata trata isso? O §3 (rastreabilidade: traço/superfície) e o §3-bis cobrem
  parte, mas talvez falte nomear explicitamente que **um artefato pode ter as duas
  forças simultaneamente** e que isso muda como você o versiona/preserva (ex.: o
  código precisa do append-only do traço E da manutenção ativa da superfície).
- Conexão prática: literate programming, docstrings, ADRs-no-código, e o fato de
  que uma IA lê o código como contexto/documento tanto quanto um humano.

**Estado**: conceitual, para amadurecer. Candidata a um refino do §3-bis quando
houver clareza (não agora).

## H-B — Aferir empiricamente se *outras* IAs entendem e aplicam o Strata

**O problema**: o Strata afirma ser "legível e aplicável por qualquer IA". Isso é
**suposição, não fato**. O lab `2026-06-04-aderencia-portabilidade` já achou gaps
de compreensão por IA (GATES de autoridade humana lidos como prosa). Falta uma
**prova empírica multi-modelo**.

**O experimento (desenho do dono, formalizado)**:

1. **Fixar** um projeto-alvo real (pequeno, com problemas conhecidos de organização)
   e o `knowledge-architecture.md` (versão congelada por hash).
2. **Variável isolada = o modelo**. Para cada modelo (Copilot Chat em modo
   automático e com modelos configurados manualmente — GPT-4.1, Gemini, etc.; e
   Claude em chat novo):
   - Prompt idêntico: "leia o Strata; produza um arquivo com (a) o que você
     entendeu do método e (b) o que mudaria para organizar ESTE projeto".
   - Salvar a saída de cada um como `plano-<modelo>.md`.
3. **Avaliação** (de volta aqui, Claude no máximo): pontuar a **qualidade de
   compreensão** de cada plano contra um rubrica fixa — não "qual é o melhor".

**Rigor obrigatório (lições L1–L5 deste projeto)**:
- **Avaliação cega**: anonimizar os planos antes de pontuar (remover o nome do
  modelo). Senão o juiz favorece o conhecido.
- **Conflito de interesse**: Claude é participante E juiz. Mitigar com (a) rubrica
  objetiva (não preferência), (b) idealmente um 2º juiz de outra família, (c)
  marcar explicitamente o viés residual no resultado.
- **Rubrica fixa** (exemplos de itens): captou a distinção L0/L1/L2? respeitou o
  §9 (priorizou em vez de mandar aplicar tudo)? reconheceu os GATES de autoridade
  humana (§6-bis) em vez de tratar como prosa? citou seções específicas ou
  generalizou? propôs algo que VIOLA um princípio forte?
- **N>1 por modelo** (estocástico): rodar cada modelo ≥2-3 vezes; a variância
  intra-modelo é dado, não ruído a esconder.

**O que isto mede**: não "qual IA é melhor", e sim **se o Strata é redigido de
forma que a compreensão sobrevive à troca de modelo** — exatamente o claim de
portabilidade-para-IA que ainda não foi provado. Um resultado negativo (algum
modelo entende mal de forma sistemática) aponta onde o texto do Strata precisa de
GATES mais explícitos.

**Conexão**: estende `lab/2026-06-04-aderencia-portabilidade` (que achou os gaps
qualitativamente) com uma medição multi-modelo. Resolve a ressalva do
`recipe/README.md` ("ainda não comprovado que qualquer IA aplica bem").

**Estado**: plano pronto, aguardando execução (precisa do dono rodar os modelos
externos manualmente; a avaliação cega volta para cá).
