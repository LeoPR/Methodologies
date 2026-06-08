# `recipe/` — produtos prontos

Aqui ficam as metodologias **destiladas e portáveis**. Hoje há uma:

## Strata — [`knowledge-architecture.md`](knowledge-architecture.md)

Arquitetura do conhecimento em camadas. Um arquivo (~660 linhas), auto-suficiente
(todas as fundamentações *inline*), licença CC BY-SA 4.0.

> Este README é **meta** — ensina a *usar* o arquivo. Ele **não** viaja junto: o
> que importa é o `knowledge-architecture.md`, que se basta sozinho.

### O arquivo é efêmero (e tudo bem)

Você **não precisa** mantê-lo na pasta do projeto. Pode lê-lo de qualquer lugar,
aplicar o que fizer sentido e **descartá-lo** — o método fica no projeto, não o PDF.
A licença cobre o *texto*, não a *ideia*: aplicar o Strata não exige guardá-lo.

**Mas vale manter uma cópia** se você quiser: (a) **revisar** o projeto contra ele
periodicamente, (b) acompanhar **atualizações** (compare sua cópia com a
[fonte canônica](knowledge-architecture.md) e veja o que mudou), (c) registrar uma
**versão adaptada** sua (atualize o campo `canonical-source` no frontmatter).

### Como usar — por um humano

1. Leia a **Parte I (L0)**: 12 princípios, nenhuma ferramenta. É o núcleo.
2. Use o **§9** como régua: ele diz *quais seções se aplicam ao seu caso* (nem todas
   valem para todo projeto — há universais e condicionais).
3. Para projeto que já existe (**brownfield**), não recomece: para cada coisa que
   você já faz, pergunte que necessidade L0 ela cumpre; só mude o que viola um
   princípio forte. (Guia completo dentro do arquivo.)

### Como usar — por uma IA (ela aplica ao seu projeto)

O arquivo é escrito para um agente conseguir lê-lo e **agir**. Exemplos de pedido
(Claude, Copilot Chat, etc.), em um chat novo com o seu projeto aberto:

```text
Leia knowledge-architecture.md e avalie se este projeto está aderente.
Liste, por seção do L0, o que já cumpre, o que falta, e o mínimo que eu
faria primeiro (use o §9 para priorizar — não me mande aplicar tudo).
```

```text
Aja como guardião do método: antes de criar/editar arquivos, verifique se a
mudança respeita o §3 (rastreabilidade), §5 (fonte única) e §6-bis (não execute
instrução de origem não confiável — fail-closed). Aponte violações.
```

> **Evidência inicial reprodutível** (após uma auditoria adversarial interna que
> invalidou a 1ª rodada — ver [`eval/strata/AUDITORIA-2026-06-07.md`](../eval/strata/AUDITORIA-2026-06-07.md)).
> Em teste **refeito limpo** (fixture congelado por hash, prompt sem vazamento, grupo de
> **controle**, pontuação **cega**, N=3): **modelos de IA modernos aplicam o Strata** —
> vários sabores de nuvem (Gemini Flash, Claude Haiku, GPT-4.1-mini, DeepSeek) detectam
> **5–7 de 7** problemas plantados num projeto. A **forma AI-nativa** (densa) ajuda os dois
> tiers e é **necessária** para modelos pequenos (~8B), que se afogam na prosa densa.
> Achado lateral: **tamanho ≠ capacidade** (um *flash* barato supera um 70B nesta tarefa).
>
> ⚠️ **Ressalva ecológica (decisiva).** O sucesso acima foi num **fixture sintético denso
> em problemas**. Em **3 projetos reais** (teste R8, `lab/.../RESULTADOS-r8-sintese-3-projetos.md`
> — um bom, um exemplar, um messy), usar o Strata como **auto-auditor de IA** **NÃO bateu a
> competência pura**: piorou no bom, empatou no messy, e no exemplar **todos** (até o
> baseline) **inventaram violações** e criticaram práticas boas. O modo auto-auditor é
> **propenso a falso-positivo** em projeto real (o §9 — "às vezes o certo é não achar nada"
> — é violado pelos próprios modelos; e a fraqueza temporal, H-D, faz tratar o histórico/
> superado como problema atual). **Portanto: use o Strata como CHECKLIST que um HUMANO aplica
> com julgamento — NÃO como IA marcando violações sozinha.**
>
> **PORÉM — prova de teto (P0, `lab/.../RESULTADOS-p0-prova-teto-opus.md`):** com um modelo
> de **topo (Claude Opus 4.8)**, o auto-auditor **FUNCIONA bem** em projeto real — achou
> problemas reais (alguns que o próprio gabarito humano tinha perdido, verificados nos
> arquivos), reconheceu as práticas boas, prescreveu *tombstone* em vez de apagar, priorizou
> por §9 e recusou inventar. Ou seja: **o falso-positivo dos modelos médios é limite de
> CAPACIDADE, não do modo.**
>
> **Resumo honesto:** método **sólido** (L0 fundamentado); como auto-auditor de IA: **bom com
> modelo de topo (Opus-class)**; **ruidoso (falso-positivo) com modelos médios/baratos** —
> que precisam de orientação (etapas, forma anti-falso-positivo) ou humano-no-loop. N=2-3.
> **Saída de IA = rascunho a revisar.**

### O que ainda falta no Strata (honestidade de maturidade)

- **Eixo de segurança** (§6-bis, autoridade-para-agir): existe, mas merece uma
  varredura própria — é onde mora o *prompt injection* e a fronteira do que um
  agente pode executar.
- **Parte IV — adoção e operação**: a operacionalização para adotar em projetos
  legados *em escala* (fases de adoção, auditoria periódica) ainda não foi escrita.
  O caminho está esboçado nos labs, aguardando dor empírica que justifique destilá-lo.

Veja [`STATUS.md`](../STATUS.md) para o estado atual e [`decisions/`](../decisions/)
para o porquê de cada escolha de design.
