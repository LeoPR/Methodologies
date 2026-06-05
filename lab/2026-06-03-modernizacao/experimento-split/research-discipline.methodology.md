---
title: Disciplina de pesquisa e revisao critica
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [00-core.methodology.md, ai-instrumentation.methodology.md, bibliography.methodology.md]
---

# Disciplina de pesquisa — hierarquia de fontes (cross-cutting)

> **Quando aplicar**: sempre que voce (ou IA) for afirmar X, decidir
> A vs B, citar referencia, ou "lembrar" fato. Aplica-se a todos os
> pilares — especialmente ADRs, registry de hipoteses, qualquer claim
> em doc/codigo.

**Problema**: humanos e IAs aceitam a primeira resposta plausivel —
pior, a primeira que confirma crenca ja' havida. Em projeto longo isso
compoe: claim de 2014 sem revalidacao; blog tratado como spec; IA
inventando referencia que "soa certa".

## Frameworks canonicos

| Framework | Pra que serve | Origem |
|---|---|---|
| **Evidence hierarchy / pyramid** | Hierarquizar forca de evidencia (meta-analise > RCT > case > opiniao) | Evidence-Based Medicine (Sackett 1996); GRADE |
| **CRAAP test** | Avaliar fonte: **C**urrency, **R**elevance, **A**uthority, **A**ccuracy, **P**urpose | Blakeslee 2004 |
| **SIFT method** | Web literacy: **S**top, **I**nvestigate, **F**ind better coverage, **T**race claims | Caulfield 2017 |
| **Primary / Secondary / Tertiary** | Dado bruto vs analise vs sumario | Library science classica |
| **Triangulation** | Validar via N fontes independentes | Denzin 1978 |
| **Chesterton's fence** | Nao descartar algo antigo sem entender porque existia | Chesterton 1929 |

Combine — cada um cobre angulo diferente. Detalhe em cada fonte (ver
[bibliography](bibliography.methodology.md)).

## Sequencia sugerida de pesquisa

Aplique em ordem; pare quando suficiente pro caso. **Em dominios
maduros, comece em (1); em dominios novos/efemeros, (3)-(4) podem
ser primarios**.

1. **Fonte primaria autoritativa**: paper peer-reviewed, spec
   oficial, manual do fabricante, RFC, ISO, codigo-fonte canonical
2. **Secundaria consolidada**: livro de referencia, survey paper,
   textbook (checar data de publicacao)
3. **Documentacao oficial atual**: site oficial do projeto, docs
   versionadas, changelog (checar versao vs versao no seu projeto)
4. **Comunidade tecnica curada**: SO respostas com votos altos
   recentes; GitHub issues fechadas; mailing lists tecnicas
5. **Blogs, opinioes, threads**: ultimo recurso. Util pra intuicao
   e padroes emergentes — **nunca substitui (1)-(3)** quando estas
   cobrem o tema

## Recencia vs autoridade — quando cada vence

**Recencia > autoridade** em cadencia rapida (software, ML, AI tools,
web frameworks). Conferir data + versao da fonte; se a primaria mais
recente contradiz a antiga, usar a nova.

**Autoridade > recencia** em cadencia lenta (matematica, fisica
fundamental, classicos da ciencia da computacao, principios de
engenharia). Fonte antiga frequentemente continua canonica.

## Dados vivos vs consolidados — meia-vida e revalidacao

**Recencia vs autoridade (acima) e binario por dominio**; este bloco
refina pra **espectro de meia-vida do dado**, frequentemente DENTRO do
mesmo item. Critico quando a IA usa ferramenta de busca pra preco,
estoque, noticia, cotacao, disponibilidade.

**Espectro de perecibilidade**:

| Classe | Meia-vida | Exemplo |
|---|---|---|
| Consolidado | anos | spec/ficha tecnica, teorema, dimensao fisica, principio |
| Semi-vivo | meses | versao corrente de lib, modelo a venda, linha de produto |
| Vivo | horas/dias | preco, estoque, frete, promocao, noticia, cotacao |

Mesmo objeto carrega classes diferentes: a ficha tecnica de um produto
e consolidada; o preco dele e vivo. **Nao trate igual.** (Refs:
Arbesman 2012, *The Half-Life of Facts*; Machlup 1962.)

**A ferramenta de busca NAO e neutra** — e intermediario falivel,
sobretudo pra dado vivo:
- Resultado de busca e **ponteiro possivelmente velho**, nao a fonte.
  Pagina antiga com SEO alto ranqueia acima da atual; snippet pode vir
  de cache stale.
- O indice nao distingue "atualizado agora" de "criado ha anos e ainda
  ranqueando".
- **Regra**: pra dado vivo, abrir a fonte e ler o timestamp do dado LA
  (data do preco, "atualizado em", header HTTP `Last-Modified`) — nao
  confiar no snippet nem na ordem dos resultados.

(Refs: Introna & Nissenbaum 2000, *Shaping the Web*; *freshness* em
Information Retrieval — Croft, Metzler & Strohman 2009.)

**Protocolo de revalidacao por classe** (TTL emprestado de cache
invalidation, RFC 7234; "cache invalidation" e um dos dois problemas
dificeis de CS — Karlton):

| Classe | Acao da IA |
|---|---|
| Consolidado | citar uma vez; tratar como verdade ate nova evidencia |
| Semi-vivo | `[VERIFICAR: data]`; revalidar se claim > 1-3 meses |
| Vivo | **nunca** servir de cache/memoria sem timestamp; revalidar na fonte primaria antes de afirmar; anexar `capturado_em` |

**Antipattern critico — "dado vivo tratado como consolidado"**: servir
preco/estoque/noticia de cache, memoria ou resultado de busca antigo
como se fosse atual. Sintoma: "achei R$X" sem dizer QUANDO o R$X foi
capturado. Antidoto: todo dado vivo carrega `capturado_em`; sem isso,
e suspeito ate prova de frescor.

## Manual oficial vs internet — regra geral e excecao

**Feijao com arroz (cobre maioria dos casos)**: manual oficial da
versao atual vence opiniao de internet aleatoria. Spec / paper /
docs versionadas > Stack Overflow / blog / thread.

**Excecao rara mas real**: as vezes uma resposta de forum/blog **excede**
a documentacao oficial — autor pode ter especialidade que o time
documentador nao tem; pode ser bug nao-documentado; pode ser uso
avancado nao previsto pelo manual. **As duas fontes sao validas**;
ignorar a internet completamente perde sinal.

**Como navegar a excecao**:
- Triangule com ≥ 2 fontes independentes
- Avalie por logica interna (a sugestao faz sentido tecnico?)
- **Usuario humano e' o juiz final** — IA nao deve afirmar
  unilateralmente que forum supera doc; deve **trazer ambas as fontes
  e pontuar a divergencia**, deixando a decisao com quem tem contexto
  do projeto

**Casos em que forum/comunidade legitimamente supre lacuna**:
- Bug efemero em versao especifica (docs nao cobrem)
- Caso de uso incomum (literatura cobre caso geral; sua config esta no forum)
- Padrao emergente (comunidade ja' usa, livro ainda nao documentou)

Em todos, marque `[VERIFICAR: YYYY-MM-DD]` ate' confirmar via fonte
mais forte (ou via teste empirico no proprio projeto).

## Marcacao de claims em docs

<a id="marcacao-de-claims"></a>

- **Fonte primaria forte**: cite uma vez; trate como verdade ate'
  nova evidencia
- **Secundaria/recente nao confirmada**: `[VERIFICAR: YYYY-MM-DD]`
- **Forum/opiniao**: `[fonte: forum; nao confirmado]`
- **Sua, sem fonte externa**: `[hipotese pessoal]` ou formalize via
  registry de hipoteses (ver [lab-work](lab-work.methodology.md))
- **Gerado/assistido por IA** (proveniencia): marcar
  `authored-by: ai | human | mixed` no frontmatter quando relevante —
  ver "Revisao critica" abaixo e
  [ai-instrumentation](ai-instrumentation.methodology.md) → Proveniencia

## Para IAs lendo este documento

Voce **nao e' onipresente**. Quando o usuario pergunta:

1. **Distinga**: voce *sabe* (pos-treinamento) vs *infere* (raciocinio)
   vs *acha* (pattern matching). Expresse a categoria.
2. **Cadencia**: se conhecimento e' rapido-mutavel (ML libs, AI
   tools, web frameworks pos-treinamento), assuma desatualizado;
   ofereca WebFetch.
3. **Conflito interno**: se duas fontes que voce conhece
   contradizem, **diga isso** — nao escolha silenciosamente.
4. **Lacuna**: se nao tem dado pra resposta confiavel, **diga e
   proponha caminho de pesquisa** — inventar e' pior que admitir.
5. **Premissa do usuario**: usuario pode estar errado. Pergunte
   "por que voce acha X?" antes de assumir X. Aceitacao automatica
   da pergunta = onipresenca falsa.

**Antipattern critico — "soa certo"**: nao infira *soa certo* →
*esta certo*. Familiaridade nao e' verdade.

---

# Revisao critica — dimensoes de avaliacao

> **Quando aplicar**: ao planejar projeto novo, revisar projeto em
> andamento, ou auditar periodo. **NAO e checklist exaustivo** (cada
> dimensao e livro proprio) — e gatilho pra IA / dev **questionar
> criticamente** o projeto antes de seguir.
>
> **Principio**: a metodologia organiza CONTEUDO; estas dimensoes
> questionam DECISOES. Complementares.

| Dimensao | Pergunta-guia | Refs pra profundidade |
|---|---|---|
| **Proposito (jobs-to-be-done)** | Que dor real isso resolve? Pra quem? Se o projeto desaparecesse amanha, quem reclamaria? | Christensen 2003 — *The Innovator's Dilemma*; Ulwick — JTBD framework |
| **Escopo vs tempo (realismo)** | Cabe no runway disponivel? Otimista demais? Onde cortar primeiro? | McConnell 2006 — *Software Estimation: Demystifying the Black Art* |
| **Seguranca** | Auth/authz cobrem o minimo? Secrets fora do codigo? Input validation? Dep scan? Threat model existe? | OWASP Top 10 (2021); NIST CSF 2.0 (2024); STRIDE threat modeling |
| **Compliance / privacidade** | Que dados sensiveis tocamos? LGPD/GDPR aplica? Auditoria de acesso possivel? | LGPD (BR Lei 13.709/2018); GDPR Art. 25 (privacy by design) |
| **ROI / custo** | Compute + storage + network + manutencao + tempo dev. Cabe no budget? Cresce como? | AWS Well-Architected — Cost Optimization pillar |
| **Confiabilidade (SLO)** | Que uptime e suficiente? Falhas toleraveis? Monitoramento ativo? | Google SRE Book (Beyer et al. 2016) — SLO/SLI/SLA |
| **Performance / escala** | Workload-alvo? 10x cabe? Otimizacao prematura vs debito real? | Knuth 1974 ("premature optimization is the root of all evil"); Bondi 2000 — scalability defs |
| **Manutenibilidade** | Bus factor? Onboarding novo dev em quanto tempo? Tech debt acumulando? | Fowler 2018 — *Refactoring* (2ª ed.); SQALE method |
| **Sustentabilidade** | Energy/carbon do compute? Cloud region? Long-term ownership? | AWS Well-Architected — Sustainability pillar (2021) |
| **Acessibilidade (se UX)** | WCAG minimo? Screen reader? Teclado-only? | WCAG 2.2 (W3C, 2023) |
| **Sinal vs ruido de features** | Cada feature serve quem? Tem "todo mundo quer mas ninguem usa"? | YAGNI (XP/Beck); *Lean Startup* (Ries 2011) |
| **Proveniencia / autenticidade** | Conteudo gerado por IA esta marcado (`authored-by: ai\|human\|mixed`)? Artefatos publicaveis tem proveniencia (`git_sha`/manifest hoje; SLSA/Sigstore, RO-Crate/CodeMeta, C2PA quando aplicavel)? | C2PA 2.x (ISO/IEC 22144); EU AI Act Art. 50; ver [ai-instrumentation](ai-instrumentation.methodology.md) |

**Como usar**:
- IA deve **levantar a pergunta** quando relevante (nao silenciar)
- Resposta "nao pensamos nisso" e informacao util — nao falha
- 80% dos projetos descartam >=3 dimensoes deliberadamente (escopo,
  custo, equipe). Explicitar e melhor que ignorar.
- Nao-aplicar uma dimensao deve ser **decisao consciente** (registrada
  em ADR se relevante)

**Anti-pattern**: usar isto como gate-keeping checklist que bloqueia
trabalho. **E gatilho de discussao, nao certificacao.**

**Para IA ao revisar projeto** (greenfield/brownfield): oferecer
"identifiquei dimensoes X/Y/Z que parecem sub-enderecadas — quer
priorizar agora? Ou registrar decisao explicita de nao atacar?"

## Referencias

Ver [bibliography](bibliography.methodology.md) → "Avaliacao de fontes /
disciplina de pesquisa" e "Proveniencia / autenticidade de conteudo".
