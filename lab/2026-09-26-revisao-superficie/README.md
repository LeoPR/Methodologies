---
name: revisao-superficie-strata
type: registro
status: blocos 1 e 2 executados (commits 1-5); bloco 3 (camada de evidência) aguarda o dono
created: 2026-09-26
updated: 2026-09-26
audience: ai-primary
---

# Revisão de superfície do Strata (2026-09-26)

Pedido do dono: revisar o Strata pela **superfície** (a proposta raiz e o refinamento do L0),
e, antes de mexer, conferir se o que está **feito** bate com o que está **declarado feito**.

## Conferência do núcleo

Antes de propor mudança no produto, o L0 foi relido inteiro na expressão inglesa (as 13 seções,
§1 a §11 mais §3-bis e §6-bis) sob a régua que ele declara para si: "sem produto, sem data" (lead
da Parte I), "se a IA e o computador sumissem, ainda valeria?" (teste do L0), §5 (fonte única) e
§9 (proporção) aplicados ao próprio texto.

## Achados da revisão (antes da auditoria)

Proposta raiz (lead + camadas): sólida. Dois defeitos:

- o "teste" do L1 ("é *uma* boa forma, não a única") é definição, não teste decidível;
- restos de conversa com o dono no núcleo neutro: §3 ("You named this as a central goal") e §7
  ("The 'how to generate' you asked for").

Refinamento (L0 fechado):

- a instância de era do §9 carrega diário de pesquisa (modelos, K, percentuais) dentro do L0;
- o §3-bis declara um defeito do §8 ("a distinction §8 today conflates") que nunca foi corrigido
  nem rastreado;
- o §10 repete por inteiro o argumento "autoridade única ≠ cópia única" do §5;
- caminhos citados nos Groundings inconsistentes (`Strata/lab/...` × `lab/...`).

Superfície:

- `recipe/README` promete "guia completo dentro do arquivo" para brownfield; o canônico declara
  o brownfield lacuna conhecida;
- `recipe/README` repete a mesma ressalva cerca de cinco vezes, com trechos em tom de diário;
- `o-que-voce-ganha` afirma "your affordable AI yields much more with the method", o que o §9
  testado não sustenta para a proporção.

## Auditoria declarado × feito

Registro completo, com destino por achado: [`AUDITORIA-sync.md`](AUDITORIA-sync.md).
Resultado: **não estava sincronizado**. Três blocos:

1. **Wayfinding** (versão, ponteiros, status de registros encerrados): mecânico.
2. **Superfície do produto** (capa, `recipe/README`, `o-que-voce-ganha`, o canônico): onde
   caem as recomendações acima, e mais três achados que as agravam:
   - o texto medido como "v1.2.2" no A/B do §9 não é a v1.2.2 commitada (`method_sha` do braço B
     não bate com nenhum commit; o texto testado não foi retido);
   - o A/B rodou só em PT, embora o portão da PROPOSTA-S9 pedisse PT+EN;
   - o parêntese do §9 ("4 models, K=5") descreve só o braço naive; o braço Strata veio de outra
     grade (7 modelos, K=2), sem pareamento.
3. **Camada de evidência** (OPINIAO-DE-USO, tabela-fonte do hub, propagação do vazamento do
   `f4-clean`, outreach, docs do eval, trabalho não commitado do controle negativo): pede
   **decisão do dono**, porque reescreve o que a evidência diz. Fica listada como pendente.

## Execução

Um commit por etapa, cada um com as guardas (`check_stamps`, `check_l10n`) e par EN/PT no mesmo
commit quando a fonte é multilíngue.

| # | Escopo | Achados |
|---|---|---|
| 1 | wayfinding: versão, ponteiros, status de registros encerrados, inventário | ver coluna destino |
| 2 | superfície: brownfield, "não mexer" na capa, frase do `o-que-voce-ganha` | idem |
| 3 | canônico: §9 enxuto (ponteiro, não diário) + errata do traço do A/B | idem |
| 4 | canônico: §3-bis/§8, §5/§10, persona, teste do L1, caminhos, itens abertos | idem |
| 5 | `recipe/README`: uma ressalva só, sem diário, evidência por ponteiro | idem |

### Log

- commit 1 (wayfinding): `fefd82c`.
- commit 2 (superfície): brownfield alinhado ao canônico (princípio no §9, guia passo a passo =
  Parte IV não escrita) na capa e no `recipe/README`; a capa deixa de prometer acerto em "quando
  não mexer"; `o-que-voce-ganha` troca "rende muito mais" pelo ganho medido (agir: o conserto que
  sozinha não faria; não-agir: redação do pedido e modelo pesam mais que o método).
- commit 2: `9c02c0f`.
- commit 3 (§9, v1.2.3): a instância de era do §9 volta ao formato das outras (afirmação curta +
  carimbo + ponteiro), sem modelos, K nem percentuais no L0; os travessões que a v1.2.2
  reintroduzira saíram junto. Errata acrescentada ao registro do A/B (braço B ≠ v1.2.2
  commitada; A/B só em PT; comparação com a frase leiga não pareada) e nota na PROPOSTA-S9.
- commit 3: `76cdea1`.
- commit 4 (L0 editorial, v1.2.4): leads do §3 e do §7 sem a voz do dono; teste do L1 decidível
  (sobrevive à troca de ferramenta e tem substituto nomeado) e teste do L2 que exclui o L1; §3-bis
  e §8 se apontam (o §8 diz por que dispositivo e probatório são imutáveis por razões
  diferentes); §10 deixa de repetir o §5; caminhos `Strata/lab/` → `lab/`; mapa de ciclos da
  Parte I completo; genealogia Campbell & Stanley → Cook & Campbell no §4 (com errata no
  registro do 1º ciclo); nota do Eixo 5 por ponteiro. Antes do commit, três revisores
  adversariais (paridade EN/PT, fidelidade ao L0, exatidão da evidência) acharam cinco defeitos
  nas próprias edições, todos corrigidos, entre eles: a instância de era do §9 da v1.2.3
  generalizava "pedido leigo" quando só vale para o **bem redigido**, e citava "Strata" no L0.
- commit 4: `9c0ef86`.
- commit 5 (`recipe/README`): a ressalva que aparecia cerca de cinco vezes vira uma seção só
  ("How an AI fares"); saem o tom de diário ("What changed in 2026-08") e as tabelas de modelos,
  vocabulário, regra de ouro duplicada e custo, que já vivem em `strata-com-ia`, OPINIAO e
  `o-que-voce-ganha` (§5: apontar, não copiar). A recusa de injeção deixa de ser "sólida e
  espontânea" em todos: "costuma recusar, mas não todo modelo nem toda vez".

## Bloco 3: pendente de decisão do dono

Ver as linhas "pendente (dono)" em [`AUDITORIA-sync.md`](AUDITORIA-sync.md). Os de maior peso:

- **OPINIAO-DE-USO e tabela-fonte do hub** pararam antes do estudo naive, do A/B do §9 e do
  vazamento do `f4-clean`: seguem chamando de SÓLIDA a série de abstenção medida na fixture que
  vazava a resposta (C0, C19, C71, C72, C98, C7, C76).
- **O vazamento também existe no `f4-clean-en`** e no `f6-ruidoso`, sem sucessora e sem aviso
  nos docs do instrumento (C99, K2, C8, C115).
- **STATUS e RESULTADOS do estudo naive** dizem "injeção baixa em todos os braços", mas o braço
  Strata EN propagou 5/14 (C1).
- **outreach/** publicou afirmações que os registros não sustentam (K0, K3, K4).
- **Política de payload**: o `.gitignore` diz manter payloads literais locais, mas o `f4-trap-en`
  e o `f4-isca` estão rastreados e já publicados (C118).
- **Trabalho não commitado** em `eval/strata/` (controle negativo em escala de repositório,
  banco de juiz) sem declaração (C4, C21, C116, C117).
- `strata-com-ia` e `strata-idiomas` herdam números da grade 2026-08 com as mesmas ressalvas
  (C34 a C44, exceto C42, tratado no commit 5).

### Bloco 3: executado em parte

- `2440ca7`: recusa EN corrigida no STATUS (errata no RESULTADOS naive, C1); aviso de vazamento
  no catálogo de fixtures para `f4-clean-en` e `f6-ruidoso` (C99, K2, C8, C115).
- `0e7ec49`: OPINIAO-DE-USO e hub com a ressalva do vazamento, o estudo naive e o A/B do §9
  (C0, C19, C71, C72, C98, C74; parcial em C7/C76: faltam as linhas próprias na tabela do hub).
- commit seguinte: `strata-com-ia` e `strata-idiomas` (par EN/PT + gráfico SVG) sem os números
  de abstenção como se fossem limpos, com a falha do gemini na armadilha, "não medido" onde não
  houve medição, a regra da checklist restrita à avaliação completa, limites de junho
  atualizados e o custo de tokens como razão em vez de contagem; errata no RESULTADOS-f4-en
  (C34, C35, C37 a C41, C43, C44, C52; C36 parcial).
- Seguem pendentes: política de payload (C118), outreach (K0, K3, K4), trabalho não commitado
  do eval e os de severidade baixa.
