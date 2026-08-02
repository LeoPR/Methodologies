---
title: L1-1 — Revisão de conteúdo da Parte II (Morfé) — a parte que pulamos
created: 2026-08-01
updated: 2026-08-01
status: aprovada pelo dono (2026-08-01) — (a) aplicada EN-first; (b) e (c)
  decididos como negativo/política (ver §7). PT derivado pendente (fim do ciclo).
---

# L1-1 — O L1 nunca foi revisado; a P5 só ancorou

Confissão de escopo (honestidade §4): o ciclo P1–P5 fechou o **L0**; a P5 tocou
a Parte II apenas **mecanicamente** (âncoras §1/§7-cont/§11). Nenhuma parte
perguntou: *as formalizações estão na camada certa? os mapeamentos ainda valem
pós-fechamento? as fontes `[CANONICAL]` bastam?* Esta parte é essa revisão.

## 1. Hipótese (declarada antes)

> **H:** sob a moldura do dono (**L0 = conceitual/primitivas · L1 = técnicas ·
> L2 = ferramentas**), a Parte II está **majoritariamente bem camadas**, com
> três classes de achado: (a) **mapeamentos que o fechamento do L0 deixou
> para trás** (o §6-bis mudou e a tabela dele não acompanhou inteiro);
> (b) **fronteira L1×L2** — algumas linhas nomeiam instâncias datadas, mas o
> *padrão* é L1 e o change-signal já cobre a aposentadoria (negativo provável:
> nada se move); (c) **política de fontes** — `[CANONICAL]` sem verificação web
> é aceitável *pela convenção declarada do próprio cabeçalho da Parte II*,
> desde que verificado-ao-tocar (§9).
> **Refutaria H:** achar linha que é ferramenta pura (sem padrão durável) ou
> mapeamento errado de fato.

## 2. Achado (a) — a tabela de §6-bis ficou para trás do L0

O §6-bis agora porta **dois atos** (executar e servir — P3). A Parte II:

- o **cabeçalho da tabela** ainda diz *"For §6-bis — authority to act
  (out-of-band channel, fail-closed)"* — só o 1º ato;
- a linha **RBAC/ABAC** foi ajustada na P3 ✓ (declara os dois atos);
- mas a linha **ISAD(G)** (sob §3-bis) carrega a área *"conditions governing
  access"* — a formalização **institucional do portão-de-leitura**, órfã desde
  a P3 (o checklist da P3 a citava; só RBAC/ABAC foi editado).

**Candidatos (mínimos):** (i) cabeçalho → "authority to act **and to serve**";
(ii) linha ISAD(G) ganha: *"; its 'conditions governing access' area formalizes
the **serving gate** (§6-bis) at institutional scale"*.

**Negativo declarado:** NÃO adicionar linhas MAC/DAC/Bell-LaPadula à tabela —
o modelo já está no Grounding do L0 (onde fundamenta), RBAC/ABAC cobre a
prática, e linha a mais é §9 falhando.

## 3. Achado (b) — fronteira L1×L2: instância datada ≠ camada errada

As linhas que **nomeiam instâncias** potencialmente datadas:

| Linha | Instância é ferramenta? | Veredito proposto |
|---|---|---|
| **Cookiecutter Data Science** | sim (template drivendata, ~2016) | **fica** — o padrão ("layout-padrão que separa os tipos") é L1; a instância morre pelo change-signal ("adapt to your stack") sem tocar o mapeamento |
| **PRONOM / DROID** | DROID é software; PRONOM é registro (serviço) | **fica** — o padrão (registro de formatos p/ auto-decifrabilidade) é L1; MIME-type já é dado como caminho curto |
| **CITATION.cff / JOSS** | formatos/plataformas da era | **fica** — mudam por fora, mas o change-signal ("only if publishable") é o controle |
| **C4 / Diataxis / MADR** | frameworks/notações | L1 legítimo (técnicas) |

Regra enunciada (já implícita no cabeçalho da Parte II): **o padrão é L1; a
instância nomeada pode ser da era — quem aposenta a instância é o
change-signal, sem tocar o mapeamento nem o L0.** Mover essas linhas para a
Parte III agora seria *thrash* (a P5 acabou de ancorar o Cookiecutter em §1) —
e errado: a Parte III é para o que **só** existe nesta era (MCP, AGENTS.md,
OTel), não para padrões com décadas de forma. **Negativo preservado: nada se
move.**

## 4. Achado (c) — `[CANONICAL]` basta? Política de fontes do L1

Contagem: ~15 linhas da Parte II são `[CANONICAL]`-only (Knuth 1984, Meyer
1997, Adzic 2011, C4, GRADE, CRAAP, triangulação, PKI/RFC 5280, NIST RBAC/ABAC,
PARA, Kanban, OKR, MoSCoW, OAIS, 3-2-1, BagIt, fixity, CITATION.cff, Dublin
Core, JOSS). O cabeçalho da Parte II **já declara a convenção**: `[WEB ✓]` =
verificado na rodada; `[CANONICAL]` = estabelecido, citado de conhecimento.

**Posição proposta:** aceitar — por três razões: (1) o impacto de erro é
**baixo por desenho** (formalização é trocável; errar a data de um padrão não
derruba princípio — o L0, esse sim, exigiu e teve 22 fontes web-verificadas);
(2) varrer ~15 linhas na web hoje é §9 falhando (custo alto, ganho baixo);
(3) a régua certa já existe: **verificar ao tocar** a linha, ou no
`re-verify-by` da camada. Registrado como decisão de política, não preguiça:
a convenção está declarada ao leitor no próprio cabeçalho (não esconde).

## 5. Ameaças à validade (§4)

- **"Revisão de conteúdo deveria re-ler cada linha criticamente, não só
  camadas/fontes."** Justo — mas a Parte II já passou pela varredura
  5-lentes + future-proof (2026-06-03) e pela aderência (2026-06-04); esta
  parte cobre o que **mudou desde então** (o fechamento do L0). Re-revisão
  total seria repetir trabalho datado (§9).
- **"ISAD(G)-acesso é stretch."** Não é: a área 3.4 do ISAD(G) é literalmente
  "condições que regem o acesso" — e a P3 já a citou como formalização órfã;
  isto é o fechamento do checklist da P3, não interpretação nova.
- **"E o `[CANONICAL]` errado?"** Se uma linha citada de conhecimento estiver
  errada, ela se corrige ao tocar — e o erro nunca sobe ao L0 (camadas
  isoladas; é a tese do produto sendo testada nela mesma).

## 6. Texto candidato (EN-first; PT no fim do ciclo)

**a)** Cabeçalho da tabela de §6-bis (Parte II):

> `## For §6-bis — authority to act **and to serve** (out-of-band channel, fail-closed)`

**b)** Linha ISAD(G) (tabela de §3-bis), acréscimo ao "What it is":

> ...operates §3-bis's distinction at institutional scale; its *conditions
> governing access* area formalizes the **serving gate** (§6-bis) at the same
> scale

## 7. Decisão (dono, 2026-08-01)

- [x] **Aprovado tudo** — (a) aplicado ao canônico EN-first: cabeçalho da tabela
  de §6-bis agora cobre **agir e servir**; linha ISAD(G) declara que a área de
  *conditions governing access* formaliza o portão-de-servir (fecha o checklist
  pendente da P3).
- [x] **(b) decidido: nada se move de camada** — instância datada ≠ camada
  errada; quem aposenta a instância é o change-signal (negativo preservado, §4).
- [x] **(c) decidido: `[CANONICAL]` aceito** pela convenção declarada do
  cabeçalho da Parte II, com régua **verificar-ao-tocar** (ou no re-verify-by).
- PT derivado fica para o fim do ciclo (commit EN com `--no-verify` intencional,
  divergência temporária declarada).
