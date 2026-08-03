---
name: auditoria-consolidacao-narrativa
type: registro
status: etapa 1 (rastreabilidade) e etapa 2 (tom) executadas 2026-08-02
created: 2026-08-02
updated: 2026-08-02
audience: ai-primary
---

# AUDITORIA: Consolidação narrativa (2026-08-02)

Registro datado da auditoria narrativa do corpus, disparada depois que o
reteste do L0 fechado (lab `2026-08-02-reteste-L0-fechado/`) moveu o estado da
evidência e deixou docs de superfície para trás.

## A régua do dono (4 linhas)

1. Sem tom de diário nos docs publicados: diário vive nas NOTAS dos labs.
2. Toda afirmação segue hipótese → teste → conclusão, com rastreabilidade.
3. Impessoal, mas Plain Language (ver `ESTILO-REDACAO.md`).
4. Rastreabilidade primeiro, tom depois: conserta-se o fato antes do estilo.

## Achados

| Documento | Problema | Tipo | Sev | Correção |
|---|---|---|---|---|
| ARQUITETURA-E-EVIDENCIAS.md | hub se declara fonte canônica mas sem entrada 2026-08-02; F3/F5/agente datados (l33,39-41,113,158-159) | RASTREABILIDADE | alta | entrada datada + recalibrar linhas |
| recipe/documentacao-multilingue.md:123-126 | fila diz recipe/README e o-que-voce-ganha "sem par" (falso hoje) | RASTREABILIDADE | alta | atualizar tabela |
| FECHAMENTO-avaliacao-strata.md:l70+passo9 | gaps já fechados (completion-only, s04) como abertos | RASTREABILIDADE | alta | entrada datada 2026-08-02 |
| recipe/strata-com-ia.md | tabela de decisão + SVG no roster jun/2026 | RASTREABILIDADE | alta | grade 2026-08 |
| lab/2026-08-02-reteste-L0-fechado/PLANO.md | status "shake-down em curso", já executado | RASTREABILIDADE | média | status executado |
| MAP.md | árvore sem lab/2026-08-02-reteste-L0-fechado; trilha "prova" só ao hub | RASTREABILIDADE | média | adicionar + apontar OPINIAO |

## Plano em etapas

- **Etapa 1: RASTREABILIDADE (esta).** Corrigir os 6 achados acima; cada doc
  ganha o fato datado, apontando à fonte (ADR-005), sem duplicar número
  volátil. Estado da evidência 2026-08: fonte única é a
  [`OPINIAO-DE-USO`](../2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) +
  [`NOTAS-shakedown`](../2026-08-02-reteste-L0-fechado/NOTAS-shakedown.md).
- **Etapa 2: TOM (pendente).** Refinamento de estilo nos pontos mapeados
  (ex.: "como a gente" no MAP.md), sem mover fato.

## Etapa 2: TOM + convenção de nomes (executada 2026-08-02)

**Convenção de nomes (dono, 2026-08-02):** o `README.md` da raiz é sempre EN +
`README.pt-BR.md`; nas demais pastas, o par se dá só por sufixo (`README.en.md`
canônico + `README.pt-BR.md` derivado). Executada em 5 pacotes:

- **WP1 (recipe/):** `recipe/README.md` → `recipe/README.pt-BR.md` (git mv); links
  vivos corrigidos (`README.pt-BR.md` raiz, `MAP.md`, `OPINIAO-DE-USO.md`, seletor
  l10n do `recipe/README.en.md`); tabela de `recipe/documentacao-multilingue.md` e
  inventário do `AGENTS.md` atualizados. Par `strata-recipe-readme` segue válido.
- **WP2 (pares EN/PT):** `eval/`, `eval/strata/`, `lab/2026-06-04-strata-hipoteses/`
  e `lab/2026-06-03-fundamentacao-L0/` renomeados para `README.pt-BR.md` + canônico
  `README.en.md` novo (tradução fiel; colofões l10n próprios). Par novo em
  `lab/2026-08-02-reteste-L0-fechado/` (superfície: PLANO = desenho pré-registrado,
  NOTAS = diário, vereditos em 4 linhas, ponteiro à OPINIAO). Reprodutibilidade no
  README do harness: pipeline (runner → fixture hash-congelada → gabarito
  pré-registrado → verificador mecânico GOLD-gate → juiz cross-vendor), comandos
  exatos de entrada e o que NÃO mora ali (conclusões → OPINIAO). Links do repo
  corrigidos (`AGENTS.md`, `eval/README*`, `ARQUITETURA-E-EVIDENCIAS.md`,
  `eval/strata/RASTREAMENTO-E-MELHORIA.md`).
- **WP3 (tom impessoal, só as frases mapeadas):** `STATUS.md` (P0: "o gabarito
  humano perdeu/estava incompleto; o modelo superou o gabarito"; fix "identificado
  em revisão humana"), `MAP.md` ("como a pesquisa foi feita"), `GLOSSARIO.md`
  (frontmatter mínimo; mede-se/usam-se/testado/repetido; linha datada Degrau 3),
  `ARQUITETURA-E-EVIDENCIAS.md` (4 frases: linhas 29, 72, 98, 303),
  `OPINIAO-DE-USO.md` ("contrato de ferramentas do laboratório"; âncora não é
  célula Claude-julga-Claude; "a Fase B deste corpus"), `REVISAO-RETROATIVA.md`
  (aperfeiçoada/mantém-se; `updated:` adicionado). Extras da reavaliação: raiz
  `README.md`/`README.pt-BR.md` ("casos medidos"). Snapshots históricos (labs
  datados, `RESULTADOS-*`) mantidos como registro, não reescritos.
- **WP4 (outreach):** `LINKEDIN-post.md`/`.pt-BR.md` ao estado 2026-08 (conserto §5
  e recusa saturam do econômico ao topo; piso local ~8B executa / ~20–27B satura;
  primeira célula agente em sandbox 10/12 × 2/12; evitar llama-4-scout; "sinais,
  não provas" mantido). `outreach/README*` sem claim datado: inalterado. SVGs
  verificados: conteúdo conceitual (camadas), sem roster, sem correção factual.
- **WP5 (reavaliação, esta seção):** varredura de primeira pessoa nas superfícies
  tocadas + relêitura contra a régua.

### Veredito da reavaliação

- **Impessoal:** ok nas superfícies publicadas. Restos conhecidos (registrados, não
  corrigidos por escopo): o hub `ARQUITETURA-E-EVIDENCIAS.md` ainda tem 1ª pessoa
  fora das 4 frases mapeadas (linhas ~82, ~88, ~111, ~120: "Como medimos", "nós
  gastamos"); o mapeamento mandou tocar só as 4.
- **Hipótese → teste → conclusão:** ok; as superfícies apontam a
  ADR/PLANO/NOTAS/OPINIAO para o detalhe; micro-detalhe de harness ficou em
  `eval/strata/README*` e nas NOTAS, não nas superfícies.
- **Reprodutível:** ok; comandos exatos de entrada e convenções no README do
  harness; lab de fundamentação diz como re-verificar (fonte primária citada).

### Pendências registradas

- Tradução EN de `recipe/strata-com-ia.md` (canônico pendente; já constava na fila
  de `documentacao-multilingue.md`).
- Hub `ARQUITETURA-E-EVIDENCIAS.md`: 1ª pessoa residual fora do mapeado (acima).
- PNGs de outreach: renderizar novamente se o texto dos SVGs mudar (não mudou).

### Registro: decisão anti-travessão (2026-08-02)

- **Decisão do dono:** eliminar o travessão (U+2014) dos textos publicados.
  Justificativa: preferência editorial; o sinal não tem função semântica que
  outro não cumpra, para leitor humano ou IA, e o excesso dele é marca
  conhecida de texto gerado por LLM.
- **Régua nova:** `ESTILO-REDACAO.md` (passo 6) agora proíbe o travessão.
  Apartes vão entre parênteses ou aspas; continuidade com ponto final,
  dois-pontos ou ponto-e-vírgula, o que ler melhor em Linguagem Simples.
- **Escopo aplicado:** raiz, `recipe/` (Strata bumpado para v1.2.1, só
  pontuação), READMEs de `eval/` e `eval/strata/`, `outreach/` e as
  superfícies vivas do `lab/`.
- **Exclusões por regra:** `decisions/` (ADRs imutáveis), pastas FROZEN
  (`experimento-split/`, `predecessor/`), fixtures/cenários/manifests de
  `eval/` (hash-congelados), `RESULTADOS-*`/`PLANO.md`/`NOTAS-shakedown.md`
  (registros datados), `_superseded/`, `recipe/_variants/`. Travessões em
  blocos de código (prompts prontos para copiar) foram preservados.
- **Complemento SVG (2026-08-02):** a primeira varredura cobriu `.md`; varredura
  corretiva cobriu os 8 SVGs publicados (outreach 2, recipe 2, VIZ-p6 4).
  Rótulos no padrão "·"; prosa com vírgula/dois-pontos/ponto-e-vírgula. XML
  validado. Os PNGs de outreach (`strata-linkedin*.png`) foram re-renderizados
  dos SVGs corrigidos com svglib+reportlab+rlPyCairo, tudo dentro do `.venv`
  (cadeia Python pura, verificação visual feita).
