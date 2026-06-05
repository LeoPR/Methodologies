---
title: Aderência, brownfield, IA-compreensibilidade e portabilidade de Strata
status: closed
created: 2026-06-04
updated: 2026-06-04
tags: [strata, aderencia, brownfield, portabilidade, ia-compreensao, multi-lente, fan-out, auto-revisao]
outcome: confirmed (1 arquivo mantido; carimbos leves aplicados; brownfield adiado; empacotamento leve)
---

# Aderência, brownfield, IA-compreensibilidade e portabilidade de Strata

> **Ciclo de auto-revisão** (dogfood): aplica §4 (registro científico), §6
> (disciplina de fonte) e §9 (economia) do próprio L0 sobre a **aplicabilidade**
> do produto. Precedente: `lab/2026-06-03-future-proof-sweep/`. É pesquisa
> SOBRE Strata, não conteúdo DE Strata — por isso vive aqui e não viaja.

## Pergunta

Quatro eixos pedidos pelo dono: (1) **grau de aderência** — o que se aplica em
100% dos casos e o que é condicional, com o como/onde/quando/porquê; (2) como um
projeto **brownfield** (que já se organiza) se adapta; (3) uma **IA** será
esperta o suficiente para aplicar; (4) **portabilidade/segmentação** — dividir o
arquivo ou não, para ele viajar a outros projetos.

## Método

Fan-out multi-lente via `Workflow` (4 lentes paralelas) → **verificação
adversarial por lente** (refutar, não confirmar; default cético) → síntese que
só admite o que sobreviveu. 9 agentes, ~664k tokens, ~10 min. O adversarial
**derrubou 2 achados estruturais** por over-engineering / erro factual — sinal de
que o ceticismo funcionou (ver "Lição de método" abaixo).

## Resultado

### 1. Segmentação — MANTER 1 arquivo (medido, não opinado)
Acoplamento L0/L1 → L2 é genuinamente baixo: **3 ponteiros abstratos**
parametrizados ("a forma de X é L2") e **ZERO nomes de ferramenta** no corpo dos
princípios. A alegação "quando uma ferramenta morre, só a Parte III muda"
verifica-se. As Fundamentações de §1–§10 carregam proveniência **inline** — não
dependem de links `../lab/` (há só 4 no doc, todos no enquadramento). Vendorar =
copiar **1 arquivo**. As fronteiras `# PARTE I/II/III` já tornam uma extração
trivial no dia em que houver dor. Strata foi transportado **0 vezes** (prototype/
vazio) → extrator/lock-file agora é antecipação que §9 condena.

### 2. Grau de aderência — tabela
**Universais** (~100% dos casos): §1 (três tipos de artefato), §2 (as quatro
perguntas), §5 (fonte única), §9 (o meta-regulador).
**Condicionais** (com gatilho):

| Seção | Gatilho |
|---|---|
| §3-bis | IA/sucessor ingere sem o autor · quantidades cross-contexto · arquivamento de séculos |
| §4 | só se gera afirmações empíricas/reproduzíveis (núcleo de honestidade é universal; aparato é condicional) |
| §6 | afirmações sobre o mundo via fontes externas / leitor-terceiro / dado perecível |
| §6-bis | contexto adversarial: forjador de diretiva + executor com poder irreversível |
| §7 | recorrência N≥3 + projeto dura o bastante |
| §8 | reprodução-por-terceiro OU vida-longa-auditável |
| §10 | vida-longa / atravessar anos (já bem carimbada — serviu de template) |

**Árvore de auto-aderência** (rascunho de navegação — NÃO virou reescrita de 12
cabeçalhos; isso foi derrubado como over-engineering): §1+§2+§5 sempre → outro
humano/IA lê sem você? → gera dados empíricos? → algo recorre 3×? → atravessa
anos? → existe adversário com poder de ação? **§9 modula a intensidade de cada
ramo, exceto §6-bis** (fail-closed).

### 3. Brownfield — buraco real, ASSIMÉTRICO, bem-localizado
Verificado: `brownfield`/`assessment` = **0 ocorrências** no produto; `migração`
só em §10 (substrato físico). A alegação do ADR-003 de "coberto por L1/L2" é
**falsa no mérito** — L1/L2 catalogam *destinos*, nunca a *transição* de um
estado legado. **MAS** o ADR-003 não errou: dá três razões para adiar; só uma é
fraca, as outras duas (§9-custo; regra-de-três/§7, N=1) sobrevivem. O ADR tomou
uma decisão de **timing** legítima. Assimetria: o produto previne sobre-organizar
(§9) mas nada **simétrico** previne destruir estrutura legada funcional na
adoção, exceto Chesterton (§6), fora do caminho de quem "aplica".

**Reconciliação portável e barata** (sobreviveu inteira; para quando a Parte IV
nascer): operacionalizar a convenção FORTE/LOCAL para brownfield —
> para cada coisa que seu projeto já faz, pergunte que necessidade L0 ela cumpre;
> se cumpre → é LOCAL, vence o nome daqui (MANTER); se nenhuma → ACRESCENTE; só
> MUDE quando viola um FORTE — e mesmo assim, se o custo de troca supera o ganho
> (§9), registre como exceção com tombstone, não dívida silenciosa; troque
> imediatamente só na fronteira §6-bis (fail-closed).

### 4. IA-compreensibilidade — dois gaps reais (de superfície, não de conteúdo)
- **GATES de autoridade humana** (irrefutável): ~5 pontos onde o doc proíbe ação
  autônoma e a IA pode ler como prosa — §6-bis fail-closed (prompt injection),
  §3 disposição/tombstone, §3-bis/§8 imutável, §4 hipótese. → resolvido pela
  linha imperativa fail-closed em §6-bis (aplicada).
- **Limiares qualitativos vs IA stateless**: "regra de três", "sentir falta" não
  são observáveis sem memória entre sessões. Ponte fiel: registrar a contagem de
  recorrência num **artefato versionado**, não na memória do agente.
- *Derrubado*: criar `STRATA-AGENT.md` como 2º arquivo (colide com ADR-001 e §5).

## Lição de método (o adversarial pegou inflação)
Dois achados "estruturais" caíram na refutação por **erro factual de evidência**,
não por opinião:
- "§9 não enumera §6" → **FALSO**: a linha 478 diz literalmente "É a mesma forma
  da perecibilidade (§6) e da durabilidade (§10)".
- "Fundamentações §1–§10 linkam ../lab/ e quebram no transporte" → **FALSO**: 0
  links nas Fundamentações.
Registro como evidência de que o default-cético (§6) encontra inflação em análises
geradas por IA — o passo adversarial não é cerimônia, é o que separa achado real
de plausível-mas-errado.

## Decisões aplicadas (pelo dono)
- **Carimbos leves** em §4/§6/§7/§8 (cláusula "— §9", template de §10) + linha
  fail-closed em §6-bis + regra-dupla TRAÇO/SUPERFÍCIE em §3. Versão → **1.1.0**.
- **§4**: núcleo (honestidade) separado do aparato (estatística) — carimbo aplicado.
- **Brownfield**: **adiar** a Parte IV (régua do ADR-003; prototype/ ainda N=0).
  Caminho FORTE/LOCAL registrado aqui para uso futuro.
- **Empacotamento leve**: `canonical-source` no frontmatter. `license` pendente
  (decisão exclusiva do dono).

## Próximo (gatilho empírico)
O **1º experimento de `prototype/`** deve ser um **teste de vendoring**: aplicar
Strata a 1–2 subprojetos reais e MEDIR o que foi de fato usado vs. carregado-morto
(kernel L0 puro? L0+L1?). Isto precede qualquer extrator de camadas — e é o
gatilho de recorrência que o ADR-001/ADR-003 esperam para reabrir segmentação e
Parte IV.

## Fonte
Saída bruta do workflow (4 análises + 4 refutações + síntese): task `wv98wzzb8`.
