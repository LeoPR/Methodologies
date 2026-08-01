---
title: P4 — Notas datadas na Parte I ("por que importa para IA") × régua axiomática
created: 2026-08-01
updated: 2026-08-01
status: aprovada pelo dono (2026-08-01) — (a)+(b)+(c) aplicadas ao canônico
  EN-first, PT derivado no mesmo ciclo. Ver §7.
---

# P4 — As duas notas "Operational (why this matters for AI)" violam a Parte I?

## 1. Hipótese (declarada antes, §4)

> **H:** as notas datadas em §3 (linha ~150) e §9 (linha ~577) são
> **apresentação dentro da abstração** — a régua as condena. **Mas** carregam
> três funções distintas, e só duas são lixo: (a) persuasão ("por que importa"),
> (b) ponte para evidência datada (lab F6, eixo gênero), (c) **temporalização da
> persona** (a IA como leitora da era). A (c) é o que o dono quer preservar — e
> o L0 já a carrega inline; o que falta é declará-la **uma vez**, no lugar certo.
> **Refutaria H:** mostrar que alguma das notas porta operação não derivável.

## 2. O que as notas carregam (dissecação)

**Nota de §3:** "legible traceability lets a model locate time... (Initial
signal, N=1: lab F6)". **Nota de §9:** "quando o gênero é pedido explicitamente,
modelos param de super-exigir... (evidência: lab, sinal forte mas circular)".

| Função | É L0? | Destino sob a régua |
|---|---|---|
| (a) Persuadir o leitor de que o princípio importa **para IA** | Não — apresentação, exatamente o que a P2 refutou | **morre** |
| (b) Narrar estado de evidência (N=1, "forte mas circular") | Não — é estado volátil de evidência; ADR-005 manda **apontar ao hub**, não copiar literal | **morre como prosa**; o *link* vai pro Grounding (ver abaixo) |
| (c) Dizer que a IA é leitora/aplicante da era | **Já está no L0** — inline, onde morde | **já existe**; falta a declaração única de persona (§3 deste doc) |

## 3. A persona já está no L0 — onde ela morde, não onde persuade

Inventário (EN): `human or agent` aparece inline em **§4** (l.226 — marca o tipo
de ato), **§5/§6** (l.375 — preencher por suposição), **§9** (l.560 — sucessor
que lê em meses), **§10** (l.661 — terceiro que lê). O frontmatter declara
`audience: knowledge workers ... and AI agents — neutral`. E a Parte III já
temporaliza com a fórmula consagrada: "o colaborador sem memória é atemporal;
**o agente de IA é a instância de 2026**" (l.818-819) — o mesmo padrão do
Grounding de §6-bis ("instância de 2026: prompt injection é a violação eterna").

Ou seja: **o produto já tem uma convenção para o datado** — instância-de-era
mora no Grounding ou na Parte III, nunca em nota operacional solta na Parte I.
As duas notas são as únicas que furam a convenção. (O "Operational rule
(fail-closed)" de §6-bis não é contraprova: é regra operativa do princípio, não
comentário sobre uma era.)

## 4. A nuance do dono — e onde ela cabe

Dono (2026-08-01): a persona do L0 é "*um humano com muito tempo e paciência,
capaz de arrumar qualquer biblioteca que já existiu ou existirá*"; no contexto
moderno a IA é **uma dica** de persona — e, depois de fechado o Strata, a IA é
**persona, método e ferramenta em algum grau**. E mais: partes podem se pescar
para vincular raciocínio, mas sem repetir nem super-explicar.

Isso pede **uma declaração de persona, uma vez só, no lead** — temporalizada
(datada), curta, sem tom professoral. É o *audience design* do próprio
documento (Clark & Murphy 1982 — o desenho da fala depende de **para quem** se
fala `[WEB ✓ 2026-08-01]`, *Advances in Psychology* 9:287–299): declarar o
leitor é parte do método (§9 já diz que o regulador é a distância ao leitor),
mas declará-lo **duas vezes por seção** é o que a régua condena.

A fórmula proposta mantém as duas camadas separadas numa frase: persona
**atemporal** (quem tem tempo e paciência de organizar qualquer biblioteca) +
persona **da era** (hoje, também o agente de IA — instância, como o prompt
injection o é em §6-bis). O "IA como método e ferramenta" **não** entra: é
escopo da Parte III (ferramenta da era) e do Comporta (método de economia de
IA), não do L0 — separação de atividades que o dono pediu.

## 5. Ameaças à validade (§4)

- **"Apagar a nota perde a ponte com a evidência."** Mitigado: o link datado
  vai pro Grounding da seção (precedente: §6-bis cita a instância de 2026 no
  Grounding). O hub (`ARQUITETURA-E-EVIDENCIAS.md`) continua a fonte do estado
  (ADR-005).
- **"Declarar persona no lead é apresentação também."** Não sob a régua: o
  lead do documento é o lugar de dizer **para quem** o método opera — §2 abre
  o método perguntando "quem chega"; o lead responder "quem aplica" é simetria,
  não densidade de abstração. E é uma frase, datada — não um parágrafo por seção.
- **"O tom."** O risco real é o professoral (dono). Defesa: o candidato abaixo
  tem 1 frase no lead + 2 linhas de Grounding; nada mais é adicionado, e dois
  blocos inteiros saem da Parte I.
- **Escopo:** a decisão "IA = persona+método+ferramenta pós-fechamento" é do
  **dono e do futuro**; este doc só registra que o L0 não a precisa declarar
  (a Parte III já trata IA-ferramenta; persona-método é Comporta/eval).

## 6. Texto candidato (EN-first; PT seria tradução derivada)

**a) Lead (após o parágrafo de abertura, antes de "How to read")** — 1 frase:

> The applier this method assumes is timeless: anyone with the time and
> patience to organize **any library that ever existed or will exist**. In the
> current era that reader is, often, an AI agent — an instance, not an
> exception (§6-bis applies the same pattern to prompt injection).

**b) §3** — a nota "Operational (why this matters for AI)" **sai**; no
Grounding de §3, acrescenta-se a linha datada:

> Era instance `[2026-06]` — legible traceability lets an AI reader locate
> time (signal, N=1): `lab/2026-06-04-strata-hipoteses/RESULTADOS-f6-temporal-sem-marcadores.md`.

**c) §9** — idem; no Grounding de §9:

> Era instance `[2026-06]` — asked the genre explicitly, AI readers apply the
> right standard and stop over-demanding (strong but circular signal):
> `lab/2026-06-04-strata-hipoteses/RESULTADOS-genero.md`.

(Resultado líquido da Parte I: −2 blocos de nota, +1 frase de persona, +2
linhas de Grounding datadas. Nenhuma operação do L0 muda.)

## 7. Decisão (dono, 2026-08-01)

- [x] **Aprovado (a)+(b)+(c)** — frase de persona no lead (formulação do dono
  mantida literal), notas de §3/§9 removidas, links datados migrados para os
  Groundings como "Era instance `[2026-06]`". Aplicado EN-first, PT derivado
  no mesmo ciclo. Saldo da Parte I: −2 blocos de nota, +1 frase, +2 linhas de
  Grounding; nenhuma operação do L0 mudou.
