---
title: P3 — Sigilo / autoridade-para-VER como candidato ao L0 (o ato simétrico ao §6-bis)
created: 2026-08-01
updated: 2026-08-01
status: aprovada pelo dono (2026-08-01) — expansão do §6-bis aplicada ao
  canônico EN-first, com tradução PT derivada; flip de autoridade do par
  formalizado (adendo ADR-008). Ver §7.
---

# P3 — §6-bis protege a *execução*; quem protege a *leitura*?

## 1. Hipótese (declarada antes, §4)

> **H:** §6-bis cobre **autoridade-para-agir** (executar uma instrução lida de
> um artefato). O ato simétrico — **servir** o artefato a um leitor — não tem
> portão no L0: o método pressupõe que todo leitor que chega é bem-vindo (§2).
> Se "verificar o direito do leitor antes de servir" é uma operação **não
> derivável** e atemporal, ela falta ao repertório — e o lugar natural é o
> próprio §6-bis (mesmo princípio-mãe *autoridade ⊥ conteúdo*, segundo ato).
> **Refutaria H:** mostrar que §6-bis ou §9 já derivam o portão de leitura, ou
> que sigilo é fora de escopo do Strata.

## 2. O argumento lógico (por quê)

Dois atos incidem sobre um artefato: **ler/servir** e **executar**. §6-bis
porta o segundo ("Dever do executor: quem detém poder verifica a origem e o
direito de um pedido **antes de exercê-lo**"). O primeiro está aberto:

- §2 ("quatro perguntas a quem chega") — o leitor que chega é sempre servido;
  não há pergunta "isto é para você?".
- §1 — a tabela tem coluna "**Para quem**" (audiência), mas audiência é
  destinação, não autorização: não há regra para o que **não** se serve.
- §9 — o regulador é a *distância* do leitor (quanto declarar), não a
  *permissão* dele (se se serve).
- §3-bis — manda a chave de decifração ser **redundante e co-localizada**...
  exceto quando o ponto é justamente que não leiam. O texto não resolve essa
  tensão hoje.

O princípio-mãe de §6-bis (*autoridade não se auto-declara; atesta-se por
canal fora-da-banda*) vale igualmente para o direito de **ler**: a autoridade
do leitor também não se auto-declara. Logo não é princípio-mãe novo — é o
mesmo aplicado a um **segundo ato que o repertório não porta**. Sob a régua
axiomática: operação faltante, não apresentação. E o lar natural é a expansão
do §6-bis (tightening, como na P1), não seção nova (§9).

## 3. Evidência interna (o próprio repo como caso)

- **O repo pratica retenção sem princípio que a explique:** `eval/strata/planos/`
  é gitignored ("projetos reais são PRIVADOS") e
  `lab/.../snapshot-fonte/` é gitignored ("não publicar"). O L0 atual **não
  consegue descrever** o próprio comportamento da oficina — o mesmo padrão que
  justificou o §11 (o `eval/` não cabia nos 3 tipos de §1).
- **O L1 já pressupõe a regra que o L0 não tem** — padrão P1: a tabela L1 do
  §6-bis lista **PKI, zero-trust, RBAC/ABAC** — formalizações de *controle de
  acesso* (leitura!), não só de execução. E **ISAD(G)** (L1 do §3-bis) tem a
  área "condições que regem o acesso". Duas formalizações de portão-de-leitura
  sem âncora no núcleo.
- **A tensão §3-bis × sigilo já morde na prática do repo:** a chave redundante
  (glossário, mapa) é publicada; o que se retém são os **dados** (planos
  privados, snapshot) — ou seja, o repo já resolveu na prática a tensão que o
  texto não resolve: o método é público, a chave/dado é o que se retém.

## 4. Literatura (web-verificada 2026-08-01)

- **Kerckhoffs 1883** — *La Cryptographie militaire* (Journal des sciences
  militaires): o sistema **não deve exigir segredo**; a segurança reside **na
  chave**, não no método. É a resolução atemporal da tensão §3-bis × sigilo:
  redundância para o método, retenção para a chave. `[WEB ✓ 2026-08-01]`
- **Shannon 1949** — "Communication Theory of Secrecy Systems" (*Bell System
  Technical Journal*): "o inimigo conhece o sistema" — a forma de Shannon do
  mesmo princípio. `[CANÔNICO]`
- **Compartimentalização moderna** — Executive Order 8381 (EUA, 1940):
  classificações *Restricted/Confidential/Secret*; need-to-know e compartimentos
  na WWII. O *default* institucional passa a ser **não-servir** salvo direito
  declarado. `[WEB ✓ 2026-08-01]`
- **Bell & LaPadula 1973** — modelo formal de confidencialidade: *simple
  security property* ("**no read up**") — a primeira formalização matemática do
  portão de leitura. `[WEB ✓ 2026-08-01]`
- **Brewer & Nash 1989** — *Chinese Wall* (IEEE S&P): o direito de ler é
  **dinâmico** (ler X revoga o direito de ler Y) — prova de que "o leitor tem
  direito?" é regra própria, não corolário trivial. `[CANÔNICO]`
- **Saltzer & Schroeder 1975** — menor privilégio (já citado em §6-bis): o
  princípio cobre leitura tanto quanto ação — a fundamentação do §6-bis já
  *tocava* o sigilo; só o texto não. `[WEB ✓ 2026-06-03]`

## 5. Ameaças à validade (§4)

- **"É corolário de §6-bis."** O princípio-mãe é o mesmo, mas a **operação**
  não se deriva do texto: §6-bis fala de *instruções executadas*; servir um
  artefato não é executar instrução. (Se o dono julgar que §6-bis "lê-se"
  cobrindo os dois atos, H vira tightening de redação, não expansão — o texto
  candidato abaixo serve nos dois casos.)
- **Escopo: Strata é sobre conhecimento compartilhado.** Contra: o repo retém
  coisas hoje (evidência interna acima); e "organizar" inclui decidir **para
  quem** — biblioteconomia e arquivística tratam condições de acesso como parte
  da descrição desde sempre (ISAD(G)).
- **Patologia do excesso:** Bell-LaPadula induziu *over-classification*
  institucional ("classifica-se tudo, acumula-se poder de leitura"). A nota de
  Aderência precisa carregar isso: portão demais é o §9 falhando por outro
  eixo — o espelho exato do regulador de gênero.
- **Antecipar o Eixo 5:** §6-bis tem varredura própria pendente (colofão do
  produto). Expandir agora não a substitui: a adição é conceitual (mesmo
  princípio-mãe), não depende da evidência frágil do F3.

## 6. Texto candidato (EN-first; PT seria tradução derivada)

Inserção no §6-bis, após o "Dever do executor":

> - **Authority to read is gated by the same rule.** An artifact is not only
>   *acted upon* — it is *served*. Whoever holds information checks the
>   reader's right **before serving it**, through the same out-of-band
>   channel: the reader's authority does not self-declare either. Every
>   artifact has a declared sphere of readers; serving beyond it is the mirror
>   breach of acting without authority. When in doubt, **withhold and
>   escalate** — the same fail-closed default, for the same reason (a leak
>   does not un-leak).
> - **The method is public; the key is what is withheld.** Secrecy does not
>   contradict §3-bis: what must be redundant and co-located is the *method*
>   of decipherment; what may be withheld is the *key* (or the payload).
>   (Kerckhoffs: the system needs no secrecy; the key does.)

E a nota de Aderência:

> **Adherence** (proportional to the number of reader spheres — §9): a solo
> project has one sphere (oneself); the gate bites when there is more than one
> reader with different rights. Over-gating is the failure in the mirror
> direction — §9 again, on the access axis.

## 7. Decisão (dono, 2026-08-01)

- [x] **Aprovada a expansão do §6-bis** — os dois bullets (autoridade-para-ler;
  método público/chave retida) e a nota de Aderência entraram no canônico
  EN-first, com tradução PT derivada no mesmo commit; a linha L1 de RBAC/ABAC
  passou a declarar que formaliza o portão nos dois atos (executar e servir).
  Fundamentação incorporada ao **Grounding** do §6-bis; Brewer & Nash 1989 e
  Shannon 1949 promovidos a `[WEB ✓ 2026-08-01]` antes da ida ao canônico.
- [x] **Flip formal de autoridade aprovado na mesma decisão** — o par
  `strata-knowledge-architecture` inverteu: EN canônico, PT tradução derivada
  (adendo datado no ADR-008; cólofons l10n trocados; `check_l10n.py` inalterado).
