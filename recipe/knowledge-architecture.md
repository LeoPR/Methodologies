---
title: Arquitetura do conhecimento — organizar, rastrear e gerar
project: Strata
version: 1.1.0
type: reference
status: active
created: 2026-05-20
updated: 2026-06-04
canonical-source: Acadêmicos/Methodologies/recipe/knowledge-architecture.md (projeto Strata)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
audience: trabalhadores do conhecimento (pesquisadores, engenheiros) e agentes de IA — neutro
camadas: L0 núcleo atemporal · L1 padrões consolidados · L2 adaptação à era atual
supersedes: organization-methodology.md (arquivado em lab/2026-06-03-predecessor/)
how-to-use: consulta sob demanda; a Parte I é autônoma e independe de qualquer ferramenta
decisions: decisions/
---

# Arquitetura do conhecimento — organizar, rastrear e gerar

> Método para **organizar, rastrear e gerar** conhecimento e informação ao
> longo de um projeto — de pesquisa, software científico ou qualquer trabalho
> intelectual que acumula artefatos. O problema é **anterior** ao computador,
> à internet e à IA: bibliotecários, cientistas e engenheiros o enfrentam há
> séculos. As ferramentas de cada era (hoje: agentes de IA, editores, controle
> de versão) são **formas** que expressam esse método — moldam, mas não fundam.

## Como ler — as três camadas de durabilidade

Tudo aqui está classificado por **durabilidade**. Isso decide o que é estável
e o que você deve esperar trocar.

| Camada | O que é | Cadência | Teste |
|---|---|---|---|
| **L0 — Núcleo atemporal** | método científico, arquitetura da informação, epistemologia, rastreabilidade | décadas/séculos | "se a IA e o computador sumissem, continua verdadeiro?" |
| **L1 — Padrões consolidados** | formalizações nomeadas, maduras, mas substituíveis (Diataxis, ADR, FAIR, IMRaD, Conventional Commits) | ~décadas | "é *uma* boa forma de fazer o L0, não a única" |
| **L2 — Adaptação à era atual** | como as ferramentas de hoje expressam L0/L1 (agentes de IA, IDE/VSCode, git, caches) | meses | "trocável sem tocar no L0" |

- A **Parte I** (este documento, abaixo) é o **L0** — completa e autônoma. Lê
  sozinha, sem mencionar nenhuma ferramenta.
- A **Parte II** mapeia padrões **L1** a cada necessidade do L0.
- A **Parte III** é a camada **L2**: datada, com prazo de revalidação,
  destacável. Quando uma ferramenta morre, só a Parte III muda.

> **Convenção FORTE / LOCAL** (usada no texto): **FORTE** = ligado ao L0/L1
> (princípio, não renomeável); **LOCAL** = exemplo da camada L2 (nome de pasta,
> ferramenta, metáfora — troque à vontade). Convenções locais do seu projeto
> vencem os nomes daqui.

---

# PARTE I — NÚCLEO ATEMPORAL (L0)

> Princípios que precedem e sobrevivem a qualquer ferramenta. Nenhum nome de
> produto, nenhuma data. Se um trecho aqui depende de uma ferramenta
> específica, ele está no lugar errado — pertence à Parte III.
>
> **Fundamentação**: cada seção lista suas fontes primárias. No repositório de
> origem (`Strata/lab/2026-06-03-fundamentacao-L0/`), 22 fontes web-verificadas
> (2026-06-03) — **todas anteriores à IA e ao VSCode** (de Pacioli, 1494, à
> engenharia de software clássica), o que confirma a tese das camadas. As seções
> acrescentadas depois (§3-bis, §6-bis, §10 e os refinos de §3/§5/§6/§7/§9)
> tiveram suas fundamentações verificadas num segundo ciclo `[WEB ✓ 2026-06-03]`
> (`Strata/lab/2026-06-03-future-proof-sweep/`).

## 1. O problema invariante: três tipos de artefato que conflitam

Todo projeto que dura acumula **três tipos de artefato** com cadências e
audiências diferentes. Misturá-los gera entropia — é a causa-raiz da maioria
dos sintomas de desorganização.

| Tipo | Natureza | Cadência | Para quem |
|---|---|---|---|
| **Produto** | o resultado estável, publicável | muda devagar, com cuidado | o usuário / o futuro |
| **Exploração** | tentativas, rascunhos, experimentos | alta rotatividade, descartável | você mesmo daqui a meses |
| **Conhecimento** | o que se aprendeu, decidiu, concluiu | semi-estável | revisor, colaborador, sucessor |

**Princípio FORTE — separação física**: cada tipo vive em um lugar próprio,
com regras próprias. O resultado estável não se polui com rascunho; o rascunho
não trava sob as regras do estável; o conhecimento não se perde no meio dos
dois. Isto é arquitetura da informação aplicada — anterior a qualquer mídia.

**Sintomas de mistura** (universais): refazer o que já existe; refazer
decisões já tomadas; documento estável poluído com trabalho-em-progresso;
quem chega depois se perde.

> **Fundamentação**: separação de preocupações — Dijkstra 1974 (EWD447);
> modularidade / *information hiding* — Parnas 1972 (*CACM*); arquitetura da
> informação — Rosenfeld & Morville 1998.

## 2. As quatro perguntas que toda base de conhecimento precisa responder

Independentemente de mídia ou ferramenta, um corpo de trabalho precisa
responder, a quem chega (humano ou máquina), quatro perguntas. Estas são as
**necessidades** — as formalizações que as atendem (na Parte II) são
substituíveis.

| Pergunta | Necessidade L0 | (formalização L1 → Parte II) |
|---|---|---|
| **"Onde está X?"** | achabilidade: um ponto de entrada, um mapa, sinais de trilha (*scent*) que guiam ao alvo | arquitetura da informação; mapas/índices |
| **"Como eu uso / entendo isto?"** | documentação que distingue *aprender* de *resolver*, e *prática* de *teoria* | Diataxis (4 quadrantes) |
| **"Por que decidimos X?"** | registro de decisões com o *porquê*, imutável, superável mas não apagável | ADR / registros de decisão |
| **"Isto é confiável / reproduzível?"** | validação: o resultado pode ser refeito e foi obtido honestamente | método científico, compêndio reprodutível |

A achabilidade merece nota: o custo de **não achar** é refazer. Por isso o
ponto de entrada e o mapa não são luxo — são o que impede o trabalho de ser
recriado por ignorância de que já existe. **FORTE**: antes de criar, verifique
se já existe.

> **Fundamentação**: *information scent* — Pirolli & Card 1999 (*Psychological
> Review*); achabilidade como problema de design — Rosenfeld & Morville 1998 /
> Morville 2005.

## 3. Rastreabilidade — o princípio de primeira classe

> Você nomeou isto como meta central ("organização **e** rastreamento"). É um
> princípio L0 por si só, não um detalhe espalhado.

**Todo artefato, afirmação e decisão deve ser rastreável até três coisas:**

1. **Fonte** — de onde veio (quem/qual evidência/qual dado de origem).
2. **Rationale** — por que existe / por que se decidiu assim (a intenção, as
   alternativas rejeitadas).
3. **Versão** — em que estado isto era verdade (qual momento, qual revisão).

Disto derivam vários mecanismos que, no fundo, são o mesmo princípio:
**proveniência** de um dado, **supersedência** de uma decisão (a nova aponta
para a que substitui), **identidade estável** de um artefato (um nome/ID que
não muda), **autoria** (quem — ou o quê — produziu), e **cadeia de custódia**
(a história não se reescreve; corrige-se adiante).

**Princípio FORTE — o traço é append-only**: corrige-se adicionando, não
apagando. Um resultado refutado **permanece** (refutação é conhecimento). Uma
decisão revogada **permanece**, marcada como superada. Apagar furtivamente o
passado destrói a rastreabilidade. (O mecanismo que torna isso praticável —
histórico recuperável por estado — está em §8.)

Mas *append-only* governa o **traço**, não a **superfície de leitura**. Três
planos que o registro ingênuo confunde num só:

- **Traço** (o que aconteceu) — **imutável e recuperável**; nunca se destrói.
- **Superfície** (o que o leitor encontra primeiro) — **decai por desuso e
  obsolescência**: `ativo → superado-mas-visível → silenciado` (retido,
  recuperável, fora do caminho de leitura por padrão) `→ disposto`. Rebaixar o
  **acesso** não é destruir o **traço**. Sem essa distinção, cada afirmação
  morta pesa na superfície igual à viva e a auditabilidade vira ruído: quem lê
  paga por varrer o que já não vale (§9).
- **Conhecimento vivo** (a narrativa que se ensina adiante) — **re-narrável** a
  cada novo leitor, com a versão anterior **encadeada**. Re-expressar com
  proveniência ≠ edição furtiva.

**Duas regras opostas, não uma**: ao **traço**, só se acrescenta (nunca apague nem
edite — é o histórico, as decisões aceitas); à **superfície**, rebaixe **ativamente**
o que morreu (silencie, deixando tombstone). Aplicar *append-only* à superfície é o
erro que faz a leitura apodrecer sob o peso do que já não vale.

**O fim do ciclo é governado, não ausente.** A oposição real não é
apagar-vs-nunca-apagar; é **edição furtiva** (sempre proibida — corrompe a
história em silêncio) vs **disposição autorizada** (legítima e ela própria um
registro). A disposição **deixa um tombstone**: o quê, quando, por quê, sob que
autoridade — a lacuna fica **legível**, não silenciosa. Reter tudo para sempre,
indistinto, é um modo de falha, não a virtude máxima.

**Dois tempos, não um.** Distinga *quando algo era verdade/vigente no mundo*
(tempo-de-vigência) de *quando o registro o capturou* (tempo-de-registro):
reconstruir "que regra valia **quando** o fato ocorreu" é diferente de recuperar
"o estado do arquivo naquela data" (§8). Emendar ≠ revogar ≠ corrigir o que
sempre foi assim.

**Marcar a confiança junto ao claim** é parte da rastreabilidade: afirmação de
fonte forte ≠ afirmação a confirmar ≠ hipótese pessoal ≠ conteúdo gerado por
um agente. Cada uma carrega sua etiqueta (a forma da etiqueta é L2).

> **Fundamentação**: proveniência de dados — Buneman, Khanna & Tan 2001 (ICDT);
> registro de quem/quando/onde/porquê + versão — Rochkind 1975 (SCCS, *IEEE
> TSE*; o primeiro controle de versão); registro auditável append-only —
> Pacioli 1494 (partida dobrada; analogia ancestral); rationale na documentação
> — Parnas & Clements 1986.
>
> Acréscimos (gradiente traço/superfície, disposição, bitemporal) `[WEB ✓
> 2026-06-03]`: acesso decai mas traço permanece (força de recuperação ≠ força
> de armazenamento) — Bjork & Bjork 1992 (*From Learning Processes to Cognitive
> Processes*, vol. 2, pp. 35–67); disposição e cronograma de retenção como ato
> governado — Schellenberg 1956 (*Modern Archives: Principles and Techniques*);
> bitemporalidade (tempo-de-vigência ≠ tempo-de-registro) — Snodgrass 1999
> (*Developing Time-Oriented Database Applications in SQL*, Morgan Kaufmann).

## 3-bis. Força do artefato: que ato isto é

Ao lado de *de onde veio* e *quão confiável é* (§3), todo artefato carrega uma
terceira marca — **ortogonal** às duas: **que ato ele executa**. "Acho que X" e
"faça X" podem ter a **mesma** confiança e a **mesma** proveniência e exigir do
leitor ações **opostas**. Confundi-los é erro de leitura, não de grau.

O corte de maior carga prática:

- **Dispositivo** — o artefato **constitui** o que diz: uma decisão, uma
  definição, um compromisso, uma diretiva. Não há fonte externa a conferir —
  ele **é** a fonte. Desfazê-lo é um **novo ato**, não uma edição (é por isto, e
  não por custo de recriação, que uma decisão aceita é imutável — distinção que
  §8 hoje funde).
- **Probatório** — o artefato **registra** algo verdadeiro alhures: uma medição,
  uma observação, uma crônica. Tem fonte externa — e por isso **se revalida na
  fonte** (§6). Marcar isto como dispositivo seria fingir que o artefato cria o
  fato que apenas testemunha.

> **FORTE**: marque o tipo de ato. Um leitor — humano ou agente — que ingere um
> corpus sem saber o que é diretiva, o que é hipótese descartável e o que é
> registro de fato lê tudo no mesmo plano e erra.

**Declare o referencial, não só o instante.** §3 carimba *quando* algo era
verdade; falta o gêmeo espacial-métrico: **contra que origem / unidade /
referencial** um valor se lê. "3 medidas", "coordenada Y", "custo Z" só
significam contra um padrão declarado — número sem unidade é ruído com aparência
de sinal. (A sonda *Mars Climate Orbiter*, 1999, perdeu-se por libra-força lida
como newton.)

**Declare também a chave de decifração — e torne-a redundante.** Antes mesmo de
*ler* o conteúdo, o receptor precisa saber *em que língua / esquema / codec* ele
está e *onde está o dicionário*. Essa chave (vocabulário, unidade, formato) é ela
própria um artefato de primeira classe — e, **ao contrário do conteúdo** (§5, que
minimiza repetição), a chave **deve** ser redundante e co-localizada: uma legenda
que só vive numa fonte distante é ponto único de falha de decifração. Um registro
cuja chave se perdeu fica tão mudo quanto tábua cuneiforme sem dicionário — e a
Pedra de Roseta é o contraexemplo célebre: carrega a própria chave.

> **Fundamentação** `[WEB ✓ 2026-06-03]`: a fronteira **dispositivo /
> probatório** é terminologia da diplomática medieval — `charta` (documento
> *é* o ato: primeiro pessoa, tempo presente) vs `notitia` (documento *prova*
> ato consumado alhures: terceira pessoa, perfeito), cláusula dispositiva aberta
> por performativo (`notum sit` / `sciatis`). Formalizada por Brunner 1880
> (*Zur Rechtsgeschichte der römischen und germanischen Urkunde*, Berlim) —
> ~80 anos antes de Austin 1962 (*How to Do Things with Words*) e Searle 1969,
> que apenas a **nomeiam** (= L1). Unidade/origem declarada: pesos-e-medidas
> fisicamente depositados em templos (antiguidade); falha canônica moderna —
> *Mars Climate Orbiter* 1999 (libra-força lida como newton). Chave de
> decifração / redundância-de-codec: Pedra de Roseta (196 a.C.), decifrada por
> âncora externa — Champollion 1822.

## 4. Registro científico: gerar conhecimento confiável

O modo de transformar exploração em conhecimento confiável é o **método
científico** — de Faraday e dos cadernos de laboratório do século XIX, não da
computação. Aplicado a uma unidade de trabalho:

- **Hipótese antes** — declare o que espera (e o que refutaria) **antes** de
  rodar. Senão a narrativa se ajusta ao resultado (*storytelling* post-hoc).
- **Registro imutável e reproduzível** — o que foi feito pode ser refeito por
  outro a partir do registro; uma vez fechado, não se altera (refazer gera uma
  nova versão, não uma edição).
- **Honestidade de resultado** — registre o que confirmou **e** o que refutou;
  preservar o negativo combate o viés de publicação.
- **Ameaças à validade explícitas** — o resultado generaliza? mediu o que
  pretendia? a causalidade se sustenta? a estatística fecha?
- **Vocabulário sóbrio** — descreva o observado ("menor em N no cenário X"),
  não o superlativo ("resultado incrível"). Superlativo é ruído.

A estrutura canônica de um relato (introdução → método → resultado →
discussão) é um **movimento**, não um formato: serve a um experimento tanto
quanto a um artigo. (Formalização — IMRaD — na Parte II.)

> **Aderência** (proporcional ao eixo de trabalho — §9): o **núcleo** é universal —
> honestidade de resultado (registrar também o que refutou), vocabulário sóbrio e
> demarcar o que não se sabe valem para qualquer trabalho intelectual. O **aparato**
> — hipótese-antes formal, registro reproduzível, ameaças-à-validade, "a estatística
> fecha?" — é condicional a **gerar afirmações empíricas/reproduzíveis**; fora desse
> eixo, §4 vale por analogia, sem culpa por hipóteses que você não tem.

> **Fundamentação**: hipótese declarada antes / pré-registro — Nosek et al.
> 2018 (*PNAS*); reprodutibilidade — Claerbout & Karrenbach 1992 (cunha o
> termo); ameaças à validade — Campbell & Stanley 1963; preservar o negativo /
> viés de publicação — Rosenthal 1979 ("file drawer"); estrutura IMRaD —
> Sollaci & Pereira 2004. Tradição: cadernos de laboratório (séc. XIX).

## 5. Fonte única por altitude: conhecimento, código e dado

**Cada fato tem uma única fonte canônica.** O princípio não é "não repita
texto" — é "todo conhecimento tem uma representação autoritativa única". E há
uma divisão por **altitude**:

- O **como** (mecânica, fluxo) é melhor expresso no próprio fazer (código,
  protocolo, procedimento) — não se re-narra em prosa.
- O **exemplo / contrato / número / observação** vive num artefato
  **verificável que sinaliza divergência** (um teste, uma medição, uma
  verificação) — não se copia o valor esperado para a prosa, onde ele apodrece
  em silêncio.
- O **porquê** (intenção, restrição, alternativa rejeitada) é o **irredutível**
  — só vive em prosa, e é a única coisa que justifica escrevê-la.

**Teste de admissão de qualquer documento** (FORTE): *apagado este texto, eu o
regenero do artefato verificável?* Se sim, não escreva — deixe um ponteiro. *E:
apagado o artefato, este texto basta para refazê-lo?* Se sim, ele carrega o
porquê — guarde, curto. Só sobrevive prosa que **falha** a primeira e **passa**
a segunda. O resto é deriva esperando para acontecer.

**Autoridade única ≠ instância única** — o corte que evita o mal-entendido mais
comum desta seção. A regra é sobre **autoridade lógica**: uma só voz canônica
por fato, que resolve **divergência** (duas fontes discordando → deriva). Ela
**não** proíbe múltiplas **materializações** da mesma verdade:

- uma **réplica** verificável-contra-a-origem não é deriva — é o que protege da
  *perda* (§10);
- uma **re-expressão** derivada (resumo, tradução, formalização para outra
  audiência) é legítima **se** aponta para a fonte canônica e **não** vira uma
  segunda autoridade.

O antipadrão é só a cópia que **finge ser fonte**. Por isso o teste de admissão
acima mede duplicação de **autoridade**, não de **conteúdo** — e é o mesmo corte
(voz canônica ⊥ materialização) que reaparece no acesso (§3), na versão (§8) e no
portador (§10). **Este é o princípio-mãe do eixo de durabilidade.**

> **Fundamentação**: fonte única (weave/tangle) — Knuth 1984 (*The Computer
> Journal*); o artefato não contém seu próprio critério de correção (problema
> do oráculo) — Weyuker 1982 (instanciação em software; o princípio generaliza
> a toda verificação formal); intenção sub-especificada pelo procedimento —
> Parnas & Clements 1986; DRY de conhecimento — Hunt & Thomas 1999. Obra ≠
> expressão ≠ manifestação (re-expressão derivada ≠ duplicação de autoridade) —
> FRBR (*Functional Requirements for Bibliographic Records*), IFLA 1998 `[WEB ✓ 2026-06-03]`.

## 6. Disciplina de fonte: a epistemologia do que se afirma

Quem trabalha com conhecimento — pessoa ou máquina — tende a aceitar a primeira
resposta plausível, pior ainda a que confirma o que já se acreditava. Contra
isso, princípios anteriores a qualquer buscador:

- **Hierarquia de evidência** — evidência forte (replicada, primária) pesa mais
  que opinião. Saiba em que degrau está o que você cita.
- **Primário > secundário > terciário** — dado bruto / fonte original vence
  análise de terceiros vence sumário de sumário.
- **Recência vs autoridade** — em domínio de mudança rápida, a fonte recente
  vence a antiga; em domínio estável (matemática, princípios), a antiga
  permanece canônica. Saiba em qual você está.
- **Perecibilidade do dado** — todo dado tem meia-vida. Um princípio dura anos;
  um preço, horas. Não trate igual: dado perecível exige **revalidação na
  fonte** e **carimbo de quando foi capturado**.
- **Triangulação** — afirmação importante se sustenta em fontes independentes.
- **Honestidade epistêmica** — distinga o que você **sabe**, **infere** e
  **acha**; **admitir uma lacuna vale mais que inventar**; familiaridade ("soa
  certo") não é verdade.
- **Cerca de Chesterton** — não descarte o que não entende: descubra por que
  existe antes de remover.

**Demarcar a própria ignorância** é parte da disciplina, não o oposto dela. Um
corpo de conhecimento maduro desenha a **fronteira do que cobre** — silêncio
*fora* dela não é negação, é "não levantado". E todo vazio carrega seu **tipo**:
confirmado-ausente ("varri, não existe") ≠ pendente ≠ ilegível ≠ fora-de-escopo.
Tratar os quatro como a mesma célula em branco induz o leitor — humano ou agente
— a **preencher por suposição**. (Distinto de "admitir uma lacuna" acima: lá é o
grau de confiança *de um claim*; aqui é o contorno do que o corpus
deliberadamente *não* cobre.)

> **Aderência** (proporcional à exposição da afirmação — §9): honestidade epistêmica
> (sei/infiro/acho) e a Cerca de Chesterton valem **sempre**, mesmo solo. Hierarquia
> de evidência, triangulação e a fronteira-de-cobertura/vazio-tipado ativam quando o
> trabalho **afirma sobre o mundo a partir de fontes externas** ou **será lido por
> terceiro** (humano ou agente) que pode preencher por suposição.

> **Fundamentação**: hierarquia de evidência — Sackett et al. 1996 (*BMJ*);
> viés de confirmação — Nickerson 1998; verificação lateral / ir à fonte (SIFT)
> — Caulfield 2017/2019; triangulação — Denzin 1978; meia-vida do conhecimento
> — Arbesman 2012; cerca de Chesterton — Chesterton 1929. Fronteira de
> cobertura declarada / vazio-tipado `[WEB ✓ 2026-06-03]`: *terra incognita*
> — Ptolomeu (*Geographia*, c. 150 d.C.); ausência tipada (confirmada-ausente
> vs não-coletada) — Rubin 1976 (*Biometrika* 63(3):581–592, MCAR/MAR/MNAR)
> e o NULL de Codd 1970.

## 6-bis. Autoridade para agir: diretiva ≠ registro · [eixo SEGURANÇA]

> Eixo distinto dos demais: não é cooperação (organizar para quem quer
> entender), é **adversarialidade** (resistir a quem forja). Entra no núcleo
> porque o invariante é tão antigo quanto o selo — e §3/§6 sozinhos não o cobrem.

Um artefato pode ser **dado a arquivar** ou **diretiva a executar** — e a
diferença é de segurança, não de estilo. Dois princípios:

- **Autoridade não se auto-declara.** Que um texto *diga* "sou uma ordem
  legítima" não o torna uma. Autoridade-para-agir é atestada por um **canal que
  o conteúdo não consegue forjar** (fora-da-banda) e **vinculada ao conteúdo
  exato** — o selo, o lacre *tamper-evident*, a contra-senha trocada em canal
  separado; hoje, a assinatura criptográfica.
- **Dever do executor.** Quem detém poder verifica a **origem e o direito** de um
  pedido **antes** de exercê-lo — nunca aceita a autoexalegação. Proveniência
  impecável (§3) **não** é autoridade-para-comandar: a citação fiel de uma ordem
  não é uma ordem viva.

**Regra operacional (fail-closed)**: antes de **executar** qualquer instrução lida
de um artefato — por mais legítima que pareça — verifique a origem por um canal que
o próprio artefato não controla; na dúvida, **recuse e escale**. Vale para um humano
e, igualmente, para um agente que lê o mesmo corpus que opera — é onde mora o
*prompt injection*.

> **Exceção dura a §9 (economia do esforço)**: aqui o *default* é
> **fail-closed**, não "comece pelo mínimo". Pular a verificação é catastrófico e
> **irreversível** (o portão aberto não se fecha) — é a única fronteira onde o
> cálculo custo-benefício de §9 não se aplica.

> **Fundamentação** `[WEB ✓ 2026-06-03]`: selo-cilindro / bula
> *tamper-evident* — canal-de-autenticação fora-da-banda (Mesopotâmia, ~4º
> milênio a.C.); senha (*tessera*) e contra-senha em canal separado — Políbio,
> *Histórias* VI.34 (~150 a.C.; sistema documentado para o exército romano);
> menor-privilégio e *confused deputy* — Saltzer & Schroeder 1975 (*CACM*
> 17(7)) / Hardy 1988 (*ACM SIGOPS OS Review* 22(4)) — nomes tardios = L1.
> Instância de 2026: *prompt injection* é a violação **eterna** deste
> invariante, não um defeito de uma ferramenta específica.

## 7. O pipeline de geração e maturação do conhecimento

> O "**como gerar**" que você pediu. Conhecimento não nasce pronto — amadurece
> por níveis. O valor está em saber **o que sobe de nível, quando e por quê**.

```
observação / pergunta
      │
      ▼
exploração  (descartável; bagunça permitida; datada; hipótese declarada)
      │   ← fecha com resultado honesto (confirmado / refutado)
      ▼
resultado  (registro imutável e reproduzível de UM achado)
      │   ← quando o mesmo achado reaparece (regra de três)
      ▼
consolidação  (achados de N explorações sobre um tema; conhecimento estável)
      │   ← quando vira escolha que afeta o futuro
      ▼
decisão  (registro imutável + rationale; rastreável; superável)
      │
      ▼
narrativa  (o arco: liga decisões e achados numa história que se entende)
```

**Regras de maturação** (FORTE):
- Não formalize o que aconteceu **uma vez** — é o que mais deriva. Deixe no
  nível descartável até **recorrer** (regra de três). Só então suba.
- Subir de nível é **reescrever**, não copiar — o registro maduro nasce limpo,
  não herda a bagunça da exploração.
- O que sobe ao nível imutável (resultado fechado, decisão aceita) **não volta
  a mudar**: para continuar, abra um novo no nível de exploração.
- **Cole a versão madura contra a fonte antes de fechar.** Reescrever para
  limpar é certo — mas reescrever é a transmissão **mais ruidosa** (passa por
  uma mente que reinterpreta). Confira que o irredutível (o número, o claim, o
  porquê) sobreviveu, não só o estilo. Promover sem conferir é copiar sem
  revisar — o erro entra na *transferência*, não no registro parado.

> **Aderência** (proporcional à recorrência e à vida do projeto — §9): a **regra de
> três** é, ela própria, o regulador — nada sobe de nível sem recorrer (N≥3) e sem o
> projeto durar o bastante para a maturação compensar. Tarefa única, sem evolução,
> vive legitimamente só no nível de **exploração**: não consolidar é o comportamento
> certo, não preguiça.

> **Fundamentação**: regra de três (não formalizar N=1) — Fowler 1999 (atrib.
> Don Roberts) `[WEB ✓]`; "jogar o primeiro fora" (exploração ≠ produto) —
> Brooks 1975 (*Mythical Man-Month*). Ackoff 1989 (DIKW: dado →
> informação → conhecimento → sabedoria) fornece vocabulário analógico, mas
> DIKW é contestado em ciência da informação (Frické 2009) e o pipeline acima
> não é derivado diretamente dele `[ANALOGIA]`. Releitura-de-fidelidade na
> promoção `[WEB ✓ 2026-06-03]`: colação / crítica textual — Lachmann
> (1793–1851, método estemmático, séc. XIX); revisão de alta fidelidade na
> replicação (DNA mismatch repair) — Modrich (Nobel de Química 2015).

## 8. Versionamento como história imutável e proveniência

Versionar é um **princípio**, não uma ferramenta: manter uma **história
auditável e recuperável** do trabalho — o mecanismo que torna o append-only
(§3) praticável no espaço de trabalho inteiro. (A ferramenta que o faz hoje é L2.)

- **Histórico recuperável por estado** — todo estado passado pode ser
  recuperado, comparado e marcado (implementação física do append-only, §3).
  Isto **elimina a versão manual**: nunca
  `relatorio_v2`, `script_antigo`, `backup_da_data` — a história já faz isso, e
  cópias manuais poluem e derivam. (Exceção: artefato declaradamente imutável —
  decisão aceita, experimento fechado, versão publicada — onde "v2" é um novo
  registro formal, não um backup informal.)
- **Sinal vs ruído** — entra no registro o que **define** o trabalho (essência:
  fontes, decisões, o irrecuperável); fica fora o **regenerável** ou
  **não-pertinente** (o que se reconstrói a partir do que entrou). Quando algo
  regenerável precisa existir, versione **o modo de recriá-lo**, não o produto.
- **Separar o efêmero do canônico** — subprodutos transitórios (cache,
  ambiente, build) não contaminam o registro do trabalho. Mesmo princípio do
  sinal-vs-ruído aplicado ao espaço de trabalho.
- **Reprodutibilidade como teste** — a pergunta-prova: *outra pessoa, em outra
  máquina, reconstrói o estado de trabalho em poucos passos?* Se não, há
  dependência implícita não registrada — encontre e registre, ou documente como
  exceção legítima.

> **Aderência** (proporcional à reprodução-por-terceiro e à vida do trabalho — §9): a
> pergunta-prova ("outra pessoa, em outra máquina, reconstrói?") **é** o gatilho —
> versionar morde quando outro precisa reconstruir o estado ou quando o histórico tem
> valor de auditoria. Solo-e-curto não o exige por princípio; se aplicar cedo, é só
> porque hoje custa quase nada (L2), não por universalidade.

> **Fundamentação**: mecanismo de histórico de quem/quando/porquê — Rochkind
> 1975 (ver §3 para o princípio append-only que este §8 implementa);
> reprodutibilidade como teste — Claerbout & Karrenbach 1992; isolar o que
> muda (parentesco com modularidade) — Parnas 1972.

## 9. Economia do esforço: quando organizar e quando não

Organizar tem **custo**. Vale quando o ganho compensa — e não antes.

| Não vale (excesso) | Vale (compensa) |
|---|---|
| poucos artefatos, vida curta | muitos artefatos, vida longa |
| uma pessoa, dias | colaboração (humanos e/ou máquinas) |
| descartável / prova de conceito | meses de duração; retomar custa caro |
| tarefa única sem evolução | volta perde tempo reconstruindo contexto |

**Sintoma de excesso**: gastar mais tempo organizando do que trabalhando.
Comece pelo mínimo que para a dor imediata; cresça só quando sentir falta.

**O regulador é a distância ao leitor previsto.** Quanto declarar, quanto
organizar, quanto replicar — tudo escala com a **distância (no tempo, no espaço,
no contexto) de quem vai ler**. Uma nota efêmera que só você lê hoje deixa o
contexto implícito e não paga redundância; o que um sucessor — humano ou agente
— lerá em meses declara o quadro e dispersa cópias, e aí isso deixa de ser
overhead e vira condição de o artefato ainda **significar** (§3-bis) e
**existir** (§10). É a mesma forma da perecibilidade (§6) e da durabilidade
(§10): organizar **na medida** de uma variável, não em absoluto. (Única exceção:
a fronteira de segurança §6-bis, onde o *default* é *fail-closed*, não "o mínimo".)

> **Fundamentação**: organizar/otimizar cedo demais não compensa — Knuth 1974
> (*ACM Computing Surveys*, "premature optimization…"); não construir o que
> ainda não é necessário (YAGNI) — Beck (Extreme Programming); declarar/organizar
> na medida da distância ao receptor (relevância/proporcionalidade) — Grice
> 1975 (*Logic and Conversation*, in Cole & Morgan eds.) / Sperber & Wilson
> 1986 (*Relevance: Communication and Cognition*) `[WEB ✓ 2026-06-03]`.

## 10. Durabilidade do portador: redundância e dispersão

§8 ensina a sobreviver à **edição** (história recuperável). Falta o par
simétrico: sobreviver à **perda**. São perigos ortogonais — uma autoridade que
deriva (duas vozes discordando) vs um portador que morre (o único que havia,
some).

**Fonte única ≠ cópia única.** §5 manda uma só **autoridade lógica** por fato —
para resolver **divergência**. Isto **não** implica um só **portador físico**.
Contra a **perda**, o invariante é o oposto: **N cópias, dispersas em substratos
com modos de falha independentes**. Lido ao pé da letra, "não copie" empurraria
para um único ponto de falha — exatamente o que consumiu a Biblioteca de
Alexandria e quase apagou Lucrécio (sobreviveu por **um** manuscrito); e o que a
vida evita há bilhões de anos (multicópia, redundância).

A reconciliação é limpa: a redundância nunca cria uma segunda **verdade**, só um
segundo **portador da mesma verdade**. Uma réplica que **se sabe derivada** e se
**verifica contra a origem** (mesmo conteúdo, mesma soma de verificação) é
*backup* legítimo, não a "cópia que deriva" condenada em §8. Só a cópia que
**finge ser fonte** é o antipadrão.

- **Verificável contra a origem** — a réplica prova que ainda é fiel
  (comparação, soma de verificação); cópia que ninguém confere apodrece em
  silêncio.
- **Perda é o *default*; preservar é um verbo** — sem re-investimento periódico
  (re-copiar, migrar de substrato, **verificar integridade**) a trajetória
  natural de qualquer registro é o desaparecimento. O portador decai
  independentemente de o fato continuar verdadeiro — perecibilidade **física**,
  ao lado da epistêmica de §6.

> **FORTE** (proporcional à vida pretendida — §9): efêmero de vida curta não
> paga redundância; o que precisa atravessar anos exige cópias dispersas e
> verificadas. Não há "guardar e esquecer"; há "manter, repetidamente, ou
> perder".

> **Fundamentação** `[WEB ✓ 2026-06-03]`: muitas cópias mantêm o seguro
> (*Lots Of Copies Keep Stuff Safe*) — LOCKSS, Vicky Reich & David Rosenthal,
> Stanford 1999; redundância e correção de erro — Shannon 1948 (*Bell System
> Technical Journal* 27) / von Neumann 1956 (*Automata Studies*); perda por
> falta de migração ("digital dark age") — Kuny 1997 (63ª Conf. Geral da IFLA,
> IFLA Publications); transmissão manuscrita como sobrevivência por cópia
> dispersa — Reynolds & Wilson, *Scribes and Scholars: A Guide to the
> Transmission of Greek and Latin Literature* (Clarendon/Oxford, 1ª ed. 1968;
> 4ª ed. 2013).

---

# PARTE II — PADRÕES CONSOLIDADOS (L1)

> Cada necessidade do L0 tem **formalizações maduras** que a operacionalizam.
> São recomendadas e estáveis há décadas — **mas substituíveis**. Aqui o
> mapeamento `necessidade L0 → formalização`, sempre com o **sinal de troca**:
> quando faz sentido aposentar a *formalização* (nunca o *princípio*).
>
> **Como ler**: cada entrada = o que é · fonte · sinal de troca. As
> **identidades de framework** foram web-verificadas (2026-06-03); `[WEB ✓]`
> marca as verificadas nesta rodada, `[CANÔNICO]` as consagradas citadas de
> conhecimento. Princípio (L0) não se troca; formalização (L1) sim — quando
> outra encaixa melhor no domínio, ou quando o overhead dela supera o ganho na
> sua escala (§9).

## Para §2 "Como uso / entendo isto?" — documentação

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **Diataxis** | 4 tipos de doc ortogonais (tutorial / how-to / referência / explicação), organizados pela necessidade do leitor, não do autor | Procida — diataxis.fr `[WEB ✓]` | se a distinção em 4 quadrantes não couber no material (raro) |

## Para §2 "Onde está X?" — achabilidade

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **Arquitetura da informação** | disciplina de organização / rotulação / navegação / busca de conteúdo | Rosenfeld & Morville 1998 `[WEB ✓]` | — (é teoria de base; a *implementação* — mapa/índice/entrada — é L2) |

## Para §3 — decisões + rastreabilidade

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **ADR** | registro leve e imutável, 1 decisão por arquivo, focado na decisão + contexto | Nygard 2011 `[WEB ✓]` | — (formato muito estável) |
| **MADR** (Markdown Any Decision Records) | evolução comunitária do ADR (template 4.0, 2024) | adr.github.io/madr `[WEB ✓]` | Y-Statement (Zimmermann) se quer 1 frase; ADR-Nygard puro se quer mínimo |
| **Conventional Commits / SemVer** | liga cada mudança a um tipo/significado e a uma identidade de versão (rastro commit→sentido→versão) | conventionalcommits.org / semver.org `[CANÔNICO]` | sem release público, a higiene de commit basta sem o padrão formal |

## Para §3-bis — força do artefato (tipo de ato, referencial, auto-decifrabilidade)

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **ISAD(G)** (Norma Internacional de Descrição Arquivística) | gabarito de descrição arquivística que distingue o ato constitutivo (o registro *é* o ato — dispositivo) do documento evidencial (o registro *relata* o ato — probatório); opera a distinção de §3-bis em escala institucional | ICA/CIA, 2ª ed. 2000 `[CANÔNICO]` | EAD (Encoded Archival Description) se precisar de troca eletrônica; RiC-CM (Records in Contexts) como sucessor emergente |
| **SI / ISO 80000** | sistema internacional de unidades e grandezas — o *datum* formal de referência para ciência e engenharia; operacionaliza "declare o referencial antes de medir" | BIPM / ISO 80000 `[CANÔNICO]` | EPSG/WGS84 para dado geodésico; TAI/UTC para tempo; IEEE 754 para ponto flutuante |
| **PRONOM / DROID** | registro de formatos de arquivo (The National Archives UK) — identifica e documenta codecs e formatos para auto-decifrabilidade de longo prazo; o "dicionário" que §3-bis exige que seja co-localizado | The National Archives UK — pronom.nationalarchives.gov.uk `[CANÔNICO]` | relevante para arquivamento de prazo longo; MIME-type (RFC 2045) basta para prazo curto |

## Para §4 — registro científico

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **IMRaD** (template) | gabarito intro / método / resultado / discussão para um relato | Sollaci & Pereira 2004 `[WEB ✓]` | — (os 4 movimentos são L0; o gabarito é flexível) |
| **Research Compendium** | contêiner único: artigo + análise + dados + ambiente, reproduzível | Marwick, Boettiger & Mullen 2018 (*Am. Statistician* 72(1):80–88) `[WEB ✓]` | adapte a estrutura ao seu stack; o princípio (tudo junto, reproduzível) fica |
| **FAIR4RS** | princípios Findable/Accessible/Interoperable/Reusable para *software* de pesquisa | Chue Hong et al. 2022 (*Scientific Data* 9:622) `[WEB ✓]` | aplique só o subconjunto que seu projeto publica |
| **Pré-registro / Registered Reports** | declarar hipótese + método antes dos dados, formalmente | Nosek et al. 2018 / Chambers 2017 `[WEB ✓]` / `[CANÔNICO]` | versão informal (H1 no README do experimento) basta fora de publicação |
| **Programas de pesquisa** (núcleo duro + cinto protetor) | estrutura para um *registry* de hipóteses cross-experimento | Lakatos 1978 `[WEB ✓]` | qualquer tabela de hipóteses com status serve; Lakatos dá o vocabulário |
| **Threats-to-validity** (checklist) | enumerar ameaças interna / externa / construto / conclusão | Campbell & Stanley 1963 / Wohlin et al. 2012 `[WEB ✓]` / `[CANÔNICO]` | — |

## Para §5 — fonte única / oráculo

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **Literate programming** | uma fonte → doc (weave) + código (tangle), consistentes por construção | Knuth 1984 `[WEB ✓]` | a maioria usa a versão fraca (docstrings + testes), não WEB |
| **Design by Contract** | pré/pós-condições + invariantes = spec auto-checável | Meyer 1997 `[CANÔNICO]` | tipos + testes property-based cobrem boa parte |
| **Specification by Example / living docs** | exemplo automatizado vira spec executável + fonte única | Adzic 2011 `[CANÔNICO]` | — |
| **C4 model** | diagramar a estrutura do sistema em 4 altitudes (uma vez) | Brown — c4model.info `[CANÔNICO]` | qualquer diagrama de contexto consistente serve |

## Para §6 — disciplina de fonte

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **Hierarquia de evidência / GRADE** | graduar a força da evidência | Sackett et al. 1996 / GRADE 2008 `[WEB ✓]` / `[CANÔNICO]` | — (princípio L0; GRADE é o grau formal) |
| **CRAAP test** | checklist de avaliação de fonte (Currency / Relevance / Authority / Accuracy / Purpose) | Blakeslee 2004 `[CANÔNICO]` | SIFT para web rápida; CRAAP para fonte acadêmica |
| **SIFT** (Four Moves) | parar / investigar a fonte / achar melhor cobertura / rastrear à origem | Caulfield 2017/2019 `[WEB ✓]` | — |
| **Triangulação** | validar via N fontes independentes | Denzin 1978 `[CANÔNICO]` | — |

## Para §6-bis — autoridade para agir (canal out-of-band, fail-closed)

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **PKI / X.509** | infraestrutura de chave pública — o canal *out-of-band* padrão: autoridade não se auto-declara no payload, é certificada por cadeia de confiança externa e verificável; operacionaliza §6-bis em sistemas digitais | RFC 5280 (IETF) `[CANÔNICO]` | GPG web-of-trust sem CA hierárquica; PASETO ou JWT com rotação de chave em contextos API |
| **Zero-trust / NIST SP 800-207** | "nunca confiar, sempre verificar" — nenhuma autoridade é assumida por posição, rede ou sessão prévia; cada executor verifica o canal independentemente | NIST SP 800-207 (2020) `[CANÔNICO]` | BeyondCorp (Google) como implementação de referência; o princípio (*verificar, não assumir*) é L0 |
| **RBAC / ABAC** | controle de acesso por papel (role) ou atributo — torna explícita e auditável a autoridade delegada, sem auto-declaração in-band | RBAC: NIST ANSI/INCITS 359-2004; ABAC: NIST SP 800-162 `[CANÔNICO]` | ABAC se granularidade de papel não basta; PBAC (policy-based) em contextos de zero-trust avançado |

## Para §7 — geração e maturação do conhecimento

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **Zettelkasten** | notas atômicas (1 ideia) ligadas em rede; conhecimento que se navega | Luhmann / Ahrens 2017 `[WEB ✓]` | bom p/ conhecimento heterogêneo; índice hierárquico basta p/ pouco volume |
| **PARA** | organizar conhecimento pessoal (Projects / Areas / Resources / Archives) | Forte 2022 `[CANÔNICO]` | só se você gerencia conhecimento além do projeto |
| **Rule of Three** | não consolidar antes da 3ª recorrência | Fowler 1999 (atrib. Roberts) `[WEB ✓]` | — |
| **Compêndio / changelog / narrativa** | consolidar achados (findings), marcos (changelog) e o arco (narrativa de projeto) | convenções `[CANÔNICO]` | escolha o formato pelo público |

## Para gerar e priorizar trabalho a partir do conhecimento

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **Kanban** | estados de workflow + limites de WIP | Anderson 2010 `[CANÔNICO]` | Scrum (epic/story) se há sprints; lista simples se solo |
| **OKR** | objetivos + key results mensuráveis (critério de aceite) | Doerr 2018 `[CANÔNICO]` | — |
| **MoSCoW** | priorização Must / Should / Could / Won't | DSDM 1994 `[CANÔNICO]` | Now/Next/Later, WSJF, etc. |

## Para §8 — versionamento / história imutável

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **Conventional Commits 1.0** | gramática de commit → mudança categorizada → changelog automático | conventionalcommits.org `[CANÔNICO]` | qualquer convenção de commit consistente serve |
| **SemVer 2.0 / Keep a Changelog** | identidade de versão + formato de changelog | semver.org / keepachangelog.com `[CANÔNICO]` | versionar por marco lógico se "release" não é o marco |
| **Cookiecutter Data Science** | layout-padrão que separa fisicamente dado/código/saída (signal vs ruído) | drivendata `[CANÔNICO]` | adapte ao seu stack |

## Para §10 — durabilidade do portador (redundância verificável, preservação ativa)

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **OAIS (ISO 14721)** | modelo de referência para preservação digital de longo prazo — define papéis (produtor / arquivo / consumidor), pacotes de informação (SIP/AIP/DIP) e o ciclo de sustentabilidade de acesso; a âncora conceitual de qualquer estratégia de §10 | ISO 14721:2012 / CCSDS 650.0-M-2 `[CANÔNICO]` | — (é o modelo de referência; toda formalização de preservação digital o instancia) |
| **Regra 3-2-1** | 3 cópias, em 2 mídias distintas, sendo 1 offsite — heurística mínima com modos de falha independentes; operacionaliza "N réplicas dispersas" de §10 em projetos de qualquer escala | Carnegie Mellon CERT; amplamente adotado `[CANÔNICO]` | expandir para **3-2-1-1-0** (+ 1 air-gapped + 0 erros verificados) para dados críticos; LOCKSS para publicações acadêmicas |
| **BagIt (RFC 8493)** | formato de pacote para transferência e armazenamento verificável — manifesto de checksums embutido, payload auto-declarado; implementa a réplica *verificável-contra-origem* de §10 | RFC 8493 (IETF, 2018) / Library of Congress `[CANÔNICO]` | git (com hashes SHA-1/SHA-256) cobre código versionado; BagIt para conteúdo binário ou transferência formal entre instituições |
| **Fixity checking** | verificação periódica de integridade por hash (MD5/SHA-256) — operacionaliza "preservar é um verbo": sem re-verificação ativa, a cópia apodrece em silêncio (bit rot) | NDSA Levels of Digital Preservation; Archivematica; prática padrão da biblioteconomia digital `[CANÔNICO]` | automação via LOCKSS, rsync --checksum, ou ferramentas de backup com verificação embutida |

## Para publicar / tornar citável (rastreabilidade externa — §3)

| Formalização | O que é | Fonte | Sinal de troca |
|---|---|---|---|
| **CITATION.cff** | metadados de citação legíveis por máquina | citation-file-format.github.io `[CANÔNICO]` | só se publicável |
| **Dublin Core / DataCite / schema.org** | esquemas de metadados interoperáveis para datasets | datacite.org `[CANÔNICO]` | use o subconjunto necessário |
| **JOSS** | padrão de software de pesquisa publicável | joss.theoj.org `[CANÔNICO]` | só se for publicar software |

# PARTE III — ADAPTAÇÃO À ERA ATUAL (L2)

> **Camada volátil e destacável.** Como as ferramentas de **hoje** expressam o
> L0/L1. Tudo aqui carrega captura `[2026-06-03]` e `re-verify-by: 2026-09-01`.
> **Quando uma ferramenta morre, só esta parte muda** — Partes I/II ficam
> intactas. Trate como dado semi-vivo (§6): re-verificar na fonte antes de
> tratar como verdade.
>
> A coluna **"expressa"** amarra cada ferramenta a uma necessidade atemporal —
> é o que permite trocá-la sem perder o porquê. A camada de IA abaixo foi
> web-verificada em 2026-06-03 (análise de modernização em
> `Strata/lab/2026-06-03-modernizacao/` no repositório de origem).

## 1. Agentes de IA — a forma de hoje do colaborador sem memória

> **Expressa**: §2 (onboarding de quem chega e não conhece o projeto) + §3
> (rastrear quem/o quê produziu) + a memória em camadas. O "colaborador sem
> memória entre sessões" é atemporal — um humano recém-chegado também é; o
> **agente de IA é a instância de 2026**.

| Forma (2026) | O que é | Expressa |
|---|---|---|
| **AGENTS.md** (+ `CLAUDE.md`) | arquivo de instruções na raiz: inventário + checklist "antes de agir" + lista NUNCA | §2 ponto de entrada p/ o colaborador |
| **MCP** (Model Context Protocol) | padrão de conexão agente↔dados/ferramentas; expor `tickets`/`manifest`/dataset como server local | §3 acesso rastreável a recursos |
| **Agent Skills** (`SKILL.md`) | capacidade empacotada reutilizável (progressive disclosure), cross-tool | operações repetíveis (auditoria, promoção, export) |
| **Memória em camadas** | (1) arquivo versionado · (2) hook · (3) memória user-scope · (4) memória filesystem (memory tool, contexto 1M) | a 4ª camada do §3 (a (4) gera drift opaco não-versionado — auditar) |
| **Context engineering + prompt caching** | curar > encher; rotear via mapa; conteúdo estável (cacheável) antes do volátil | §2 achabilidade por roteamento |
| **Subagents / fan-out** | orquestrador distribui N subagentes paralelos (retornam sumários, não despejam contexto) | revisão/auditoria de projeto são fan-outs naturais |
| **Agent evals** | testar AGENTS.md/Skills/hooks (são prompts que regridem em silêncio) | §5 (o checável vira teste) |
| **Proveniência / C2PA** | marcar `authored-by: ai\|human\|mixed`; assinatura de artefato | §3 rastreabilidade de autoria |
| **Observabilidade (OTel GenAI)** | traces/spans/tokens por sessão de agente | complemento-máquina do diário/manifest (§3) |
| **Busca grep-first** | agentes descobrem por grep/árvore, não vector DB; semântica (FTS5+sqlite-vec) só p/ corpus grande | §2 achabilidade |

**Estado da matriz (`[VERIFICAR: 2026-06-03]`)**: AGENTS.md é padrão
**estabelecido** (Agentic AI Foundation/Linux Foundation, 2025), nativo em
Codex/Copilot/Cursor/Gemini CLI/Aider/Windsurf/Zed; Claude Code auto-carrega
`CLAUDE.md` (importe AGENTS.md com `@AGENTS.md`). **Segurança (NUNCA)**: server
MCP com escrita/ação = superfície de ataque — menor privilégio; ação com
side-effect externo exige aprovação. C2PA torna-se obrigatório ago/2026 (EU AI
Act Art. 50; C2PA 2.x = ISO/IEC 22144).

## 2. Editor / IDE — a forma de hoje do ambiente de trabalho

> **Expressa**: o ambiente onde se escreve, lê e navega o conhecimento. VSCode
> (e Cursor, Zed, JetBrains…) são a forma de 2026.

O que importa pro método: o editor deve **renderizar** o conhecimento (markdown,
links clicáveis, diagramas) e **integrar** wayfinding (mapa, busca) e o agente.
Detalhe de editor muda rápido — **não acoplar o método a um editor específico**
(o conhecimento é texto/markdown portável, legível em qualquer um).

## 3. Controle de versão — a forma de hoje da história imutável

> **Expressa**: §8 (história imutável, proveniência, signal-vs-ruído). git é a
> forma dominante de 2026; os princípios valem p/ mercurial/fossil/jj/sucessores.

| Forma (2026) | Expressa | Nota |
|---|---|---|
| **git** | §8 história recuperável de quem/quando/porquê (sucessor de SCCS, 1975) | tool-agnóstico; sintaxe muda, disciplina fica |
| **`.gitignore`** | §8 signal vs ruído (o que NÃO versiona) | templates oficiais github/gitignore |
| **Git LFS / DVC / lakeFS / Quilt** | §8 arquivos grandes irrecuperáveis | só o irrecuperável entra; o script de recriação entra |
| **Conventional Commits / SemVer / Keep a Changelog** | (L1, §8) gramática do histórico | ver Parte II |
| **Signed commits / branch protection / CODEOWNERS** | §3 autoria + colaboração rastreável | em projeto publicável/regulado |

## 4. Sistema de arquivos — a instanciação física

> **Expressa**: §1 (separação física dos tipos de artefato) e o §8
> efêmero-vs-canônico.

- **Estrutura de pastas** — uma instanciação do §1 em filesystem (ex: `src/`,
  `docs/{tutorials,how-to,reference,explanation}/` [Diataxis, L1], `docs/adr/`,
  `experiments/{dirty,clean}/`, `tickets/`, `data/{raw,interim,processed}/`
  [Cookiecutter DS, L1]). Os nomes são **LOCAIS**; o princípio (separar tipos)
  é **L0**.
- **Caches e ambientes** — redirecionar o efêmero (cache, venv, build) p/ fora
  do working tree (`$XDG_CACHE_HOME`/`~/.cache/`, `%LOCALAPPDATA%`, ou pasta
  dedicada tipo `Z:\caches\`). Working tree limpo = §8. Detalhe por ferramenta
  (env vars `PIP_CACHE_DIR`, `CARGO_TARGET_DIR`, `HF_HOME`, etc.): doc oficial
  de cada uma.

## 5. Rastreadores externos (SaaS) — a forma corp do tracking

> **Expressa**: gestão de trabalho (L1: Kanban/OKR/MoSCoW) quando a organização
> exige uma ferramenta corp (Jira/Linear/Monday/etc.).

- O **canonical** (markdown+git) é a fonte da verdade; o tracker é **destino**.
- **Bridge unidirecional** (export canonical → CSV/API). Bidirecional gera dual
  source of truth e drift.
- Cards retroativos: sempre linkar evidência versionada (commit/ADR/EXP) — sem
  isso, é ficção.

## Re-verificação (esta parte é semi-viva)

A cada auditoria (ou no `re-verify-by`), conferir na fonte. A matriz de
ferramentas de **IA** é a de maior cadência (AGENTS.md/MCP/Skills/memória). Se
um item desta parte virar falso, **corrigir só aqui** — o L0/L1 não muda. Esta
é a prova viva da tese das camadas: a fundação (Partes I/II, de Pacioli 1494 à
engenharia clássica) permanece enquanto a forma (Parte III) é trocada.

---

> **Estado**: Partes I (L0), II (L1) e III (L2) escritas. As citações vivem
> inline (Fundamentação no L0; fonte+sinal-de-troca no L1; captura+re-verify no
> L2); uma bibliografia consolidada por camada é um próximo passo opcional.
>
> **Pendências abertas**:
> - **Eixo 5 (segurança/adversarialidade)**: §6-bis tocou o eixo; merece varredura
>   própria com princípio-mãe *autoridade ⊥ conteúdo*.
> - **Parte IV — Adoção e operação**: caminho brownfield (como adaptar projeto
>   existente) é gap conhecido; aguarda recorrência empírica (N≥3) para formalizar.
