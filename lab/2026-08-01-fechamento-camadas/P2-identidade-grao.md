---
title: P2 — Identidade e grão como candidatos a princípio L0 (o que é "um" artefato)
created: 2026-08-01
updated: 2026-08-01
status: FECHADA (2026-08-01) — H REFUTADA pela régua axiomática do dono; nenhuma mudança
  no canônico (negativo registrado, §4). Ver seção 8.
---

# P2 — Identidade e grão: o L0 rastreia unidades, mas nunca diz o que é uma unidade

## 1. Hipótese (declarada antes, §4)

> **H:** O L0 exige rastreabilidade (§3), fonte única (§5), classificação (§11) e
> pipeline de maturação (§7) — todas operações **sobre unidades** ("todo artefato",
> "cada fato", "UM achado", "cada objeto") — mas nenhuma seção diz **o que
> constitui uma unidade**: onde ela começa e acaba (grão) e o que a mantém sendo
> "a mesma" quando o conteúdo muda (identidade). Se a lacuna é real e a teoria é
> atemporal, falta um princípio (candidato a §12). **Refutaria H:** mostrar que
> §3 ("identidade estável" como mecanismo derivado) + §5 (FRBR por altitude) já
> cobrem a constituição da unidade, não só a sua exigência.

## 2. O argumento lógico (por quê)

Toda a maquinaria do L0 é **quantificada sobre unidades**: §3 quer "todo artefato"
rastreável; §5 quer "uma só autoridade por fato"; §7 sobe "UM achado" de nível;
§11 dá a cada objeto "exatamente um lugar". Mas "artefato", "fato", "achado" e
"objeto" aparecem como primitivos **indefinidos**. E dois problemas distintos se
escondem nesse indefinido:

1. **Grão** — onde cortar: uma decisão e suas alternativas são uma unidade ou
   várias? Um parágrafo que mudou de arquivo é o mesmo artefato? Sem grão
   declarado, dois leitores fatiam diferente e §3/§5/§11 operam sobre conjuntos
   **diferentes** de coisas — a rastreabilidade diverge na unidade, não no dado.
2. **Identidade** — o que persiste: se o conteúdo de uma unidade muda 100%, ela
   é "a mesma"? Se um ID é reutilizado para outra coisa, houve uma unidade ou
   duas? Sem regra de identidade, "superado" (§3) e "nova versão" (§8) não têm
   critério: superar o quê?

Nota de fronteira honesta: §3 **exige** identidade estável (lista como mecanismo
derivado da rastreabilidade) e §5 já traz **FRBR** (obra ≠ expressão ≠
manifestação) como fundamento do corte autoridade ⊥ materialização. Ou seja, o
L0 já *usa* os dois conceitos — a questão de H é se usá-los basta, ou se a
**constituição** da unidade precisa de princípio próprio. (Este é um H
deliberadamente mais fraco que o da P1; a resposta pode ser "reforçar §3/§5",
não uma seção nova — ambos os desfechos são resultado.)

## 3. Evidência interna (o próprio repo como caso)

- **O dogfooding mais limpo é o incidente que corrigimos hoje:** o ADR-003 dizia
  "abrir ADR-004 para Parte IV" — o identificador "ADR-004" **designou duas
  decisões diferentes em dois tempos** (a reservada, imaginada; a real, sobre
  `eval/`). É uma **colisão de identidade** clássica: o nome era estável, o
  referente não. A errata que escrevemos ("número é ID estável, não reserva") é
  exatamente uma regra de identidade — mas ela não existe no L0, só no folclore
  dos ADRs (ADR-005, consequências: "os números de seção são identificadores
  imutáveis... adições por sufixo `-bis`, nunca renumerar").
- **O L1 tem duas regras de grão sem âncora no L0** — o mesmo padrão da P1:
  "ADR: 1 decisão por arquivo" e "Zettelkasten: notas atômicas (1 ideia)". Duas
  formalizações de granularidade, zero fundamentação no núcleo.
- **§7 quantifica sem definir:** "resultado (registro imutável e reproduzível de
  UM achado)" — UM é o conceito inteiro da seção, e não está definido.
- **§8 pratica identidade nova-ato:** "artefato declaradamente imutável — onde
  'v2' é um novo registro formal, não um backup informal" — criar identidade
  nova em vez de editar é a regra de identidade em ação, não nomeada.
- **`eval/` usa as duas identidades ao mesmo tempo:** `.fixture-hash` (identidade
  **por conteúdo** — o hash muda, é outra coisa) vs nomes de ADR/seção
  (identidade **por designação** — persiste sob mudança de conteúdo). O repo
  opera a distinção sem que o L0 a ensine.

## 4. Literatura (web-verificada 2026-08-01)

- **Cutter 1876** — *Rules for a Dictionary Catalog* (GPO, Washington): os
  "objects" do catálogo — **find** (achar o item conhecido por autor/título/
  assunto), **collocate** (mostrar tudo do mesmo autor/assunto), **choose**
  (distinguir edição/caráter). É a primeira formalização de que **identidade
  bibliográfica existe por altitude**: "o mesmo livro" é uma coisa para find,
  outra para collocate, outra para choose. `[WEB ✓ 2026-08-01]`
- **Plutarco ~100 d.C.** — *Vida de Teseu* 23: o navio de Teseu — peça a peça
  substituída, continua "o mesmo"? É a formulação fundadora do problema da
  **identidade através da mudança de conteúdo**. `[CANÔNICO]`
- **Panizzi 1841** — as 91 regras do catálogo do British Museum: a **forma
  uniforme do nome** como garantia de que a mesma entidade se reúne sob um só
  identificador (raiz do *authority control*). `[CANÔNICO]`
- **FRBR, IFLA 1998** — obra ≠ expressão ≠ manifestação ≠ item: a unidade "o
  que é uma" muda de altitude. Já fundamenta §5 `[WEB ✓ 2026-06-03]` — aqui
  funciona como a regra de **altitude da identidade**.
- **Kimball 1996** — *The Data Warehouse Toolkit*: "**declare the grain**" —
  passo 2 do método: dizer, numa frase inequívoca, **o que uma linha é**. Trinta
  anos de data engineering confirmam: toda patologia de join/agregação rastreia
  a grão não declarado ou divergente. `[WEB ✓ 2026-08-01]`
- **Parnas 1972** — modularidade/*information hiding* (*CACM*; já citado em §1):
  a fronteira correta da unidade é a que **esconde uma decisão / o que muda
  junto**. É o critério de corte: grão não se mede em tamanho, mede-se em
  **fronteira de decisão**. `[WEB ✓ 2026-06-03]`
- **Luhmann / Ahrens 2017** — Zettelkasten (já no L1): nota **atômica** (1
  ideia) + **IDs ramificados** que dão identidade estável e endereçável a cada
  nota, independente de edição. `[WEB ✓ 2026-06-03]`
- **Miller 1956** — "The Magical Number Seven, Plus or Minus Two" (*Psych.
  Review* 63(2)): o *chunk* como unidade cognitiva — o grão certo para o
  **leitor** não é o físico nem o lógico, é o que uma mente segura de uma vez.
  `[CANÔNICO]` (peso baixo: replicação contestada; usado só como âncora do
  conceito de chunk)

## 5. Ameaças à validade (§4)

- **"§3/§5 já cobrem."** Parcialmente verdade — e é a ameaça real a H. §3 exige
  identidade estável; §5/FRBR dá a altitude. O que **não** está coberto: (a) a
  regra de **constituição** do grão (declare-o; corte na fronteira de decisão);
  (b) a distinção **designação vs conteúdo** como dois regimes de identidade
  (o incidente ADR-004 mostra que ela morde na prática); (c) a regra
  "identidade nova = ato novo" (que §8 pratica sem nomear). Se o dono julgar
  (a)-(c) corolários óbvios, H cai para "reforço de redação em §3", não §12.
- **Risco de L0 abstrato demais.** "O que é uma coisa?" flerta com metafísica
  inútil (§9). Defesa: o princípio resultante é operacional — quatro regras
  curtas com sintoma observável (colisão de ID, grão divergente, v2 informal).
- **Miller 1956** é o elo fraco da cadeia (replicação contestada); carrega só
  o conceito de chunk, nenhuma conclusão.

## 6. Posição (duas opções, com recomendação)

**Opção A — §12 novo: "Identidade e grão: o que é *um* artefato"**, 4 regras:

1. **Identidade precede conteúdo** — a unidade persiste através da edição;
   trocar de identidade é um **ato novo** (nunca uma edição furtiva — §3).
2. **Grão declarado** — diga numa frase o que é *uma* unidade do corpus; grão
   divergente entre autor e leitor quebra rastreio (§3) e classificação (§11)
   antes de qualquer dado errado.
3. **Corte na fronteira de decisão** — fatie onde as decisões/mudanças se
   separam (Parnas), não onde o tamanho sugere; para o leitor, o grão é um
   chunk (Miller; Ahrens).
4. **Identidade por altitude e por regime** — nomeie a altitude (obra/expressão/
   manifestação/item — FRBR) e o regime (**designação estável** para atos —
   ADRs, decisões — vs **endereçamento por conteúdo** para evidência — fixtures,
   hashes); misturar os regimes é colisão garantida.

**Opção B — sem seção nova:** reforçar §3 (transformar "identidade estável" de
item de lista em subseção com as regras 1 e 4) e anexar grão ao §11 (regras 2
e 3, como pré-condição da classificação). Menos inchaço (§9), mesma cobertura.

**Recomendação: Opção B.** A P1 fechou porque *nada* no L0 falava de formar
esquema; aqui o L0 já *fala* de identidade (§3) e altitude (§5) — falta
**densidade**, não existência. §9 pesa contra um §12 por enquanto; se o uso
mostrar atrito (regra de três), promove-se a seção com experiência real —
exatamente o caminho que ADR-003 prescreveu para a Parte IV.

## 7. Decisão pendente

- [ ] Dono escolhe: **Opção A** (§12) ou **Opção B** (reforço em §3 + §11)?
- [ ] Se B: redigir o reforço (canônico + espelho `.en.md`); o caso ADR-004 vira
  exemplo citável na subseção de §3.
- [ ] Se A: fundamentação acima vai ao colofão do §12; enumerações passam a 14.

## 8. REVISÃO (2026-08-01) — a objeção axiomática do dono e o desfecho

**A objeção (dono, revisando esta P2):** *abstração não precisa de densidade nem
de apresentação.* "1+1" não fica inexplicado por eu não ter dito que 1 poderia
ser uma maçã. Construída a abstração, ela se explica no instante em que se põe
coisas nela. Há abstrações que não precisam apresentar absolutamente nada. Os
exemplos pertencem ao lado de **fora** — servem para mostrar que o fluxo
funciona, não para completar o princípio.

### 8.1 A literatura que sustenta a objeção (e reformula a régua de revisão)

- **Hilbert 1899** — *Grundlagen der Geometrie*: os primitivos (ponto, reta,
  plano) ficam **indefinidos** e são definidos *implicitamente* pelos axiomas.
  Relato de Blumenthal (estação de trem de Berlim, 1891): deve ser sempre
  possível dizer, em vez de "pontos, retas, planos", "**mesas, cadeiras,
  canecas de cerveja**". A pergunta certa sobre um sistema axiomático nunca é
  "o que *é* um ponto?", e sim "os axiomas **bastam** para as operações?".
  `[WEB ✓ 2026-08-01]`
- **Benacerraf 1965** — "What Numbers Could Not Be" (*Philosophical Review*
  74(1):47–73): números não são nenhum objeto particular (nenhuma redução a
  conjuntos é *a* certa); o que vale é a **estrutura**. Pedir que a aritmética
  diga "1 = esta maçã" é a categoria errada de demanda. `[WEB ✓ 2026-08-01]`
- **Tipos abstratos de dados** — Liskov & Zilles 1974 (*SIGPLAN Notices* 9(4))
  `[CANÔNICO]`; Guttag & Horning 1978 (*Acta Informatica*) `[CANÔNICO]`: um
  tipo é definido pelas **operações**, nunca pela representação. Transportado:
  o L0 é um ADT — "artefato" é definido pelo que as seções fazem com ele
  (rastrear, classificar, superar, versionar). Defini-lo além disso é vazamento
  de representação para a interface.

### 8.2 Reanálise de H sob a régua certa

A régua discrimina: **falta um axioma** (operação/restrição entre primitivos)
ou **falta uma apresentação** (instanciação/exemplo)? Reclassificando as 4
regras propostas:

| Regra proposta | Veredito sob a régua |
|---|---|
| 1. Identidade precede conteúdo; nova identidade = ato novo | **Derivável** de §3 (supersessão encadeada) + §8 ("v2 = novo registro formal"). Teorema, não axioma. |
| 2. Grão declarado | **Operação de aplicação**, não do núcleo: ao instanciar §11 num corpus, o grão se declara ali. Pertence ao guia, não ao L0. |
| 3. Corte na fronteira de decisão (Parnas) | **Orientação de instanciação**; Parnas já fundamenta §1. |
| 4. Identidade por altitude e por regime | Altitude **já é §5** (FRBR); designação-vs-conteúdo é **corolário** de §3 (identidade de atos) + §10 (fixity do portador). |

Nenhuma das quatro é axioma faltante. **H REFUTADA**: a "lacuna" era um pedido
de apresentação disfarçado de lacuna conceitual — exatamente a confusão que a
objeção nomeia.

### 8.3 Por que a P1 passou na mesma régua (consistência)

§11-Classificação não é exemplo nem densidade: é uma **operação** ("formar o
esquema") que o repertório do L0 não tinha — §1/§2 a *usam* sem a *ter*. A
régua axiomática valida retroativamente a P1 e refuta a P2: o critério não é
"o princípio se explica sozinho?", é "**a operação existe no repertório?**".

### 8.4 Desfecho

- **Nenhuma mudança no canônico.** Resultado negativo registrado (§4: preservar
  o que refutou).
- As evidências internas (colisão ADR-004; grão "1 decisão/arquivo" e "nota
  atômica" no L1) **permanecem neste lab** como demonstração externa de que o
  fluxo funciona — o lugar que o dono reservou aos exemplos.
- **Critério que fica para as Partes 3–5:** *"instanciado o método num corpus
  novo, sem computador, a operação existe no repertório do L0?"* Sim →
  candidatura válida (caso P1). A "falta" só aparece como pedido de
  exemplo/definição do primitivo → **não é lacuna** (caso P2).
- Efeito colateral: a régua **reforça a P4** — as notas "Operacional (por que
  importa para IA)" dentro da Parte I são **apresentação dentro da abstração**;
  o lugar delas é fora do L0.
