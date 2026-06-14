---
title: 'IDEIA (registro, para estudar depois) — como REGISTRAR/DECLARAR o uso de ferramentas de IA num projeto'
created: 2026-06-14
status: 'REGISTRO de ideia/atividade. NÃO executado, NÃO decidido. Pesquisar e encaixar via ADR depois.'
tags: [proveniencia, autoria, ia-disclosure, rastreabilidade, §3, §3-bis, §6, lei, normas-publicacao, candidato-L1]
---

# Registro & declaração de uso de ferramentas de IA — o que pesquisar e onde encaixar

> **Isto é um REGISTRO de atividade, não um estudo nem uma decisão.** Reúne a pergunta, os eixos a pesquisar e
> os candidatos a encaixe — para retomar depois sem redescobrir. Pedido do dono (2026-06-14): "não é pra fazer,
> é pra registrar o que pesquisar, como fazer, onde encaixar e padronizar — usando o próprio Strata".

## A pergunta
Como **registrar e declarar**, de forma rastreável e padronizada, o **uso de ferramentas de IA** (e de outras
ferramentas) ao longo de um projeto — para satisfazer (a) normas de publicação científica, (b) leis/normas
(UE, Brasil, EUA, propostas) e (c) a própria **rastreabilidade** (§3) e **honestidade de fonte** (§6) do Strata?

## Por que é do Strata (não aleatório)
Já há ganchos no produto — **não inventar do zero**:
- **§3-bis / proveniência** (L1) já cita marcar `authored-by: ai|human|mixed` + C2PA. Esta ideia **aprofunda** isso.
- **§3 rastreabilidade** (fonte/rationale/versão) e **§6 honestidade de fonte** (distinguir saber/inferir/gerar)
  são exatamente o lugar onde "o que foi feito por qual ferramenta" mora.
- **§9 proporcional**: nem todo projeto/etapa precisa do mesmo nível de declaração — a régua é o gênero/contexto
  e a exigência externa (revista, lei).

## Eixos a pesquisar (mapa, não respostas)
1. **Normas de publicação científica** (declaração em etapas, na página publicada):
   - ICMJE (autoria — IA **não** é autor; declarar uso); COPE (position on AI tools); Nature/Springer; Science/AAAS;
     Elsevier; IEEE; ACM; CSE. Granularidade pedida: **por etapa** (concepção, pesquisa, geração de dados/código,
     redação, **correção/edição de texto**, figuras) e **declarativa** ("o que foi feito + qual ferramenta").
2. **Lei / norma / proposta:**
   - **UE:** AI Act (transparência, art. ~50 — conteúdo gerado/assistido por IA); 
   - **Brasil:** PL 2338/2023 (Marco Legal da IA) + borda LGPD; normas CAPES/universidades;
   - **EUA:** US Copyright Office (guidance sobre obras com IA);
   - **Propostas / soft-law:** diretrizes de periódicos, políticas institucionais.
3. **Padrões técnicos de proveniência (como gravar):**
   - **C2PA / Content Credentials** (mídia/figuras — Photoshop já emite); **SPDX** (proveniência de software);
     **schema.org** (`CreativeWork`/contributor); **trailers de commit** (estilo `Co-Authored-By` / Conventional
     Commits — mas atenção: o hook deste repo bloqueia `Co-Authored-By`); frontmatter `authored-by`.

## Camadas de registro (a desenhar)
- **Por ETAPA do trabalho:** dev/código · pesquisa · geração de dado/informação · redação · **correção de texto** ·
  figuras/gráficos. Cada etapa pode ter ferramenta e grau de envolvimento diferentes.
- **Por GRANULARIDADE / obrigatoriedade:** desde **anônimo-agregado** ("usou-se IA assistiva") até **declarativo
  detalhado** ("o que foi feito, com qual ferramenta") — alguns contextos nem exigem dizer *quem*; outros exigem
  *o que* foi feito por *qual* ferramenta (código: VSCode/Claude Code/o próprio humano; gráfico: Photoshop; etc.).
- **Por ARTEFATO/portador:** commit trailer · frontmatter `authored-by`/`ai-assisted` · CHANGELOG · **bloco
  declarativo na página publicada** (paper/site) · sidecar C2PA na figura.

## Candidatos a encaixe (NÃO decidir agora — ADR depois)
- **Strata L1 — formalização de proveniência de autoria/ferramenta** (estende §3-bis): um padrão "declaração de
  uso de IA por etapa" + schema `authored-by`/grau, com sinal-de-troca. *(mais provável)*
- Possível **seção/Parte** do Strata (se recorrer e amadurecer — regra de três do §9).
- **Comporta** tem ângulo (uso/roteamento de ferramenta), mas o **registro/declaração** é proveniência → Strata.
- **Spinoff** se virar grande demais para o L1.

## Estado
**REGISTRO.** Não estudar agora. Quando retomar: pesquisar os 3 eixos (web), propor 1 padrão L1 + um ADR de
encaixe, e dogfoodar no próprio repo (este projeto usa IA o tempo todo — é o primeiro caso de teste).
Cruza com: §3/§3-bis/§6 do [`../../recipe/knowledge-architecture.md`](../../recipe/knowledge-architecture.md),
[`DOSSIE-ia-temporalidade-ordem-fontes.md`](DOSSIE-ia-temporalidade-ordem-fontes.md),
[`IDEIA-exportacao-traducao.md`](IDEIA-exportacao-traducao.md) e [`BACKLOG-fila-geral.md`](BACKLOG-fila-geral.md).
