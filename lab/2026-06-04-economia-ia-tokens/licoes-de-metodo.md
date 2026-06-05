---
title: Lições de método — melhorias no processo científico (ciclo economia-IA)
created: 2026-06-04
status: vivo (acumula lições conforme aparecem)
purpose: melhorar COMO pesquisamos; candidato a realimentar o Strata (knowledge-architecture.md)
---

# Lições de método

> Não é sobre o CONTEÚDO (economia de IA) — é sobre o PROCESSO. Cada lição veio de
> um erro real cometido e corrigido nesta sessão. Registradas para aplicar adiante
> e, eventualmente, formalizar no Strata (§4 registro científico, §6 ceticismo).

## L1 — Não concluir de um único caminho de acesso

**Erro cometido (B4a/Foundry)**: cravei "Windows 10 bloqueia a GPU do Foundry
Local" a partir de **uma** sessão CLI que falhou. Eram dois sintomas distintos
(WinML-skip + catálogo vazio) que juntei numa causa errada (SO).

**A correção (do dono)**: distinguir as camadas — o que a CLI fornece vs o que a
extensão VSCode fornece. A investigação revelou: catálogo vazio = **endpoint morto
da CLI** (`catalog.azureml.ms` sem registro A), não Windows; WinML-skip ≠ sem-GPU.

**Regra**: antes de declarar uma limitação ESTRUTURAL (SO, hardware, "impossível"),
confirme por **≥2 caminhos independentes** e **rode o artefato real**. Uma falha num
caminho prova que *aquele caminho* falhou, não que a capacidade não existe.

## L2 — Sintoma ≠ causa; isole a variável antes de atribuir

**Erro previsto (tool_use)**: a verificação adversarial viu indício de que a chamada
de ferramenta "voltava como texto" e generalizou "o shim /v1/messages do Ollama é
quebrado". 

**A realidade (medida em 3 modelos)**: qwen2.5-coder:7b FALHA (texto), mas
llama3.1:8b e qwen3:14b PASSAM (tool_use estruturado). É **dependente do modelo**,
não do shim. O adversarial acertou o sintoma e errou a causa.

**Regra**: ao observar uma falha, varra ≥2-3 valores da variável suspeita (aqui:
trocar o modelo) ANTES de atribuir a causa a um componente. Uma amostra de tamanho 1
não distingue "componente X quebrado" de "esta instância de X".

## L3 — Rodar o artefato é o árbitro final (acima de docs, logs e suposição)

Tanto em L1 quanto em L2, a conclusão só ficou correta depois de **executar (ou
tentar executar) o artefato real**. Ler docs ("Foundry roda em Win10/11") e logs
(EP skip) levou a conclusões erradas; rodar o teste desambiguou.

**Regra**: nenhum veredito de viabilidade fecha sem uma execução. Docs e logs geram
hipóteses, não conclusões. (É o §4 do Strata — registro reproduzível — e ecoa a
lição do `lab/2026-06-04-aderencia-portabilidade`, onde o adversarial derrubou 2
achados "estruturais" por erro factual de evidência.)

## L4 — Custo-zero primeiro responde o essencial

O desenho faseado do plano (gates de custo zero antes de qualquer token pago) se
provou: D0.5 (tool_use) e toda a caracterização local (Estágios 2-3) responderam as
perguntas-chave — "dá pra rodar local?", "o agêntico-local é viável?" — **sem gastar
1 token pago**. O resultado (viável mas lento, ~20 t/s) já torna desnecessário/baixo-
prioridade o teste pago D1/E4.

**Regra**: ordene experimentos para que os gates baratos matem ou destravem os ramos
caros ANTES de gastar. Um "não" de custo zero vale tanto quanto um "sim".

## L5 — O adversarial é necessário MAS pode super-generalizar

A verificação adversarial (workflows) pegou inflações reais (mentira de custo do
"Sonnet grátis", bug de dupla-contagem 7×) — é indispensável. MAS em L2 ela
super-generalizou ("shim quebrado"). 

**Regra**: trate o output adversarial como **hipótese forte a testar**, não como
veredito. O adversarial reduz falsos positivos (achados inflados) mas pode criar
falsos negativos (matar algo viável por generalizar um sintoma). A execução real
arbitra os dois.

## Candidato a realimentar o Strata

L1-L3 são instâncias de um princípio só: **"autoridade-lógica vem da execução do
artefato, não da sua descrição"** — parente do "autoridade-lógica ⊥ instância" já no
§5. L4 é o §9 (economia) aplicado a ordem-de-experimentos. L5 refina o §6 (ceticismo):
o ceticismo deve apontar para AMBOS os lados — contra o achado inflado E contra a
refutação super-generalizada. Avaliar se vale um adendo ao §4/§6 quando este ciclo
fechar (não agora).
