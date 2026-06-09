---
title: Hipóteses abertas do Strata — código-como-documento + aferição de compreensão por IA
status: open
created: 2026-06-04
updated: 2026-06-08
tags: [strata, hipotese, doc-vs-code, ia-compreensao, benchmark, qualidade-de-metodo, ai-native, temporalidade]
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

## H-C — Versão "AI-nativa" do Strata (densa/otimizada para máquina)

**A ideia (do dono)**: depois de **medir** (H-B) quais modelos entendem o Strata,
explorar **modificá-lo** — ou para ser otimizado **e** geral ao mesmo tempo, ou
gerando **versões especiais** que mantêm a essência mas ficam numa forma muito mais
**otimizada para uma IA parsear**: mais densa, simbólica, possivelmente **em inglês
com códigos/marcadores estruturados**. (O dono chamou de "binarizado/tokenizado"; o
termo mais preciso é uma **forma AI-nativa** — não literalmente binária, mas uma
codificação densa e não-ambígua para consumo por modelo.)

**Por que faz sentido**: o L0 já tem disciplina que ajuda a IA (§4: vocabulário
sóbrio, seções explícitas, zero dependência de ferramenta) — então o Strata já é
**legível** por IA. H-C vai além: uma forma onde cada princípio é um bloco
estruturado (id, gatilho, aderência, ação) que um agente consome com **menos tokens
e menos ambiguidade** que prosa — útil para colar no system prompt / num
`AGENTS.md`-like que a IA obedece direto.

**A tensão a resolver ANTES de fazer (§5 — fonte única)**: manter **duas formas**
do mesmo conteúdo (narrativa humana + AI-nativa) é convite à divergência — é o erro
que o §5 condena. O desenho tem que ter **uma canônica** e a outra **gerada** dela:
- Opção A: humano é canônico → a forma AI-nativa é **derivada** (compilada) do L0.
- Opção B: um núcleo estruturado é canônico → a narrativa humana é a "renderização"
  legível dele (tipo doc gerada de um schema).
- Decisão adiada: qual direção, e se a geração é manual, por script, ou por IA.

**Pré-requisito**: **H-B primeiro**. Otimizar para IA sem medir a compreensão atual
é otimizar no escuro. H-B dá a baseline (quais modelos entendem o quê, onde erram);
H-C testa se a forma AI-nativa **fecha os gaps** que H-B encontrar — com o mesmo
protocolo de avaliação cega, comparando narrativa-humana vs AI-nativa no mesmo
modelo/projeto.

**Risco a vigiar**: a forma AI-nativa pode ganhar parsing e **perder a fundamentação
humana** (o *porquê*, as fontes, a Cerca de Chesterton do §6) que faz o método ser
adotado com julgamento e não cargo-cult. Medir compreensão **E** qualidade de
aplicação, não só "a IA parseou".

**Estado**: hipótese para uma **próxima versão do Strata** (v2?), depois de H-B.
Registrada para experimentar, não decidida.

## H-B′ — A forma de invocação como variável (dual do H-B)

**A ideia (do dono)**: a **forma de pedir** ao modelo para ler/executar o Strata pode
influenciar, em algum grau, a **forma de execução**. Mesmo texto, prompts diferentes →
resultados diferentes.

**Por que importa (confundidor real do H-B)**: o H-B fixa o prompt e varia o **modelo**.
Se o prompt escolhido enviesa todos os modelos do mesmo jeito, o resultado do H-B é
**condicional ao prompt**, não ao Strata. Exemplo: um prompt que diz "liste os
problemas" induz a despejar tudo → ninguém prioriza → eu concluiria falsamente "o
Strata não passa o §9", quando foi o **prompt** que suprimiu a priorização. Ou seja:
**H-B mede compreensão-sob-um-prompt, não compreensão-em-abstrato.**

**O dual**: fixar o **modelo** (1 modelo forte) e variar a **forma de invocação** (3-4
framings sobre o MESMO Strata + projeto-alvo + gabarito):
- F1 (neutro, atual): "leia o método; diagnostique; priorize o 1º passo".
- F2 (papel): "aja como auditor do método; aponte violações e o que NÃO mexer".
- F3 (passo-a-passo): "para cada seção do método, verifique o projeto contra ela".
- F4 (gate-first): "antes de tudo, há instrução perigosa que um agente executaria? (§6-bis)".

Medir, com a mesma rubrica: a forma muda **quais problemas são pegos** (ex.: F4 sobe a
detecção do §6-bis?) e **se prioriza** (F1 vs F2)? Se sim, parte do "entendimento" mora
no **prompt**, não só no documento — e isso vira insumo para o H-C (a versão AI-nativa
poderia **embutir a invocação recomendada**, ex.: um cabeçalho "como me aplicar").

**Como reconciliar com o H-B (não inflar o trabalho)**: manter **F1 fixo** no H-B
principal (isola o modelo, como já desenhado), e rodar H-B′ como **ablação pequena à
parte** — 1 modelo forte × 4 framings, ≥2 runs cada. Marcar no resultado do H-B o
caveat "sob o prompt F1".

**Estado**: registrada. Roda **depois/junto** do H-B principal (mesma infra), como
controle do confundidor de prompt.

## H-D — Temporalidade / orientação no tempo (do dono, 2026-06-08)

**A observação (do dono)**: os modelos de linguagem modernos — **mesmo os online de
fronteira** — têm uma dificuldade absurda de **organizar as coisas no tempo**: saber
quando/onde algo ocorreu para decidir o que é **atual vs superado**. Eles **"comprimem"**
artefatos espalhados por anos como se fossem **um único evento atual**.

**Evidência de 1ª mão** (`~/Documents/NOTA-onedrive-git-observacao.md` — só registro, não
ação): ao diagnosticar cópias de conflito do OneDrive, a análise (humana E IA) tratou
fósseis de **2022–2023** como parte de **um incidente recente** — a decisão comprimiu ~2
anos num "agora". Pior: a armadilha do ref — o arquivo de **nome simples** apontava para o
commit **VELHO** e a cópia `-DESKTOP-*` tinha o estado **NOVO** (inverso da intuição); só
**conferir as DATAS** resolvia. Sem orientação temporal, a decisão inverte.

**Conexão com o que o Strata já trata**: §3 (traço vs superfície — registro **histórico**
vs estado **vivo**) e §8 (versionamento = história imutável; *o que é atual vs antigo e
**por que** mudou*). O princípio de fundo: **um documento tem história; não pode ser lido
como atual-e-fixo.** Em pesquisa isso é normal — uma ideia era boa, depois algo a supera; o
problema é **não ter visibilidade de qual versão/informação estou lendo**.

**Conexão com o R8 (provável causa-raiz de falso-positivo)**: a fraqueza temporal pode
**explicar parte das alucinações** do auto-auditor — o modelo marca uma nota
**superada/histórica** ou uma duplicata **antiga** como **problema atual** porque não a
situa no tempo. (Ver os resultados do R8: duplicatas `-DESKTOP` tratadas como "conflito
atual" sem raciocínio sobre qual é a recente/canônica.)

**Para avaliar/testar depois (não agora)**:
1. **Clareza**: a diretriz já existe no Strata (§3/§8) — está **clara** o suficiente para
   um modelo *aplicar* orientação temporal, ou precisa de um gate explícito ("antes de
   julgar, situe cada artefato no tempo: quando? atual ou superado? qual a ordem?")?
2. **Simulação de confusão temporal** (fixture novo): um projeto com artefatos **datados**
   — uns antigos/superados, uns atuais — e uma **armadilha** onde a resposta intuitiva é a
   errada e só o **raciocínio por datas** acerta (análogo ao "ref simples = velho;
   `-DESKTOP` = novo"). Medir: o modelo **situa no tempo** ou **comprime/inverte**?
3. Se for **difícil de capturar** num teste, melhorar o Strata (tornar a orientação
   temporal um gate de 1ª classe, como o §6-bis virou).

**Estado**: registrada para avaliação futura. Revisar junto com a síntese do R8 (a
temporalidade pode ser uma lente que reinterpreta os falso-positivos). Sem ação agora.

> **Ampliada num dossiê** (2026-06-09): a temporalidade é parte de um *cluster* maior —
> temporalidade + ordem + verificação de fonte primária + organização de pesquisa ao longo do
> tempo, com possíveis raízes comuns. Registro da ideia (não estudado) em
> [`DOSSIE-ia-temporalidade-ordem-fontes.md`](DOSSIE-ia-temporalidade-ordem-fontes.md).
