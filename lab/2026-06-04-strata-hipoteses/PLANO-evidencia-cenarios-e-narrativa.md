---
title: 'Plano — mais cenários reais, novos gêneros, o viés do "projeto próprio", e o loop narrativa↔resultado'
created: 2026-06-13
status: 'REGISTRO de plano/raciocínio. NÃO executado — encaixe na fila de evidências. Rodar/estudar adiante.'
---

# Plano — expandir a evidência sem se enganar (a estudar, não executado)

> Registro de raciocínio (não execução). Liga-se ao [hub de evidências](ARQUITETURA-E-EVIDENCIAS.md)
> e ao [roadmap de modos](PLANO-geral-modos-fechar-lacunas.md). Endereça o limite mais citado dos
> resultados: **"1-2 cenários-mãe → pode ser idiossincrasia"**.

## Os candidatos na fila
| Sujeito | Gênero | Por que interessa | Eixo/§ que estressa |
|---|---|---|---|
| **PatchCraft** (repetir) | software/ferramenta | replicação num 2º projeto real de código | ecológico (F4/R8); §3/§5 |
| **AulaQuantum** | **acompanhamento de aula** (notas) | NÃO é projeto — material de aprendizado sequencial | generalização de gênero · **temporalidade** (F6); §7, §1 |
| **DeepLearning** | **acompanhamento de aula** (notas) | idem; corpus que evolui com o entendimento | idem |

### O que os "acompanhamentos de aula" testam de NOVO (e por que valem)
Não são projetos com config/injeção — são **conhecimento em formação**. Estressam eixos diferentes:
- **Generalização de gênero:** o Strata vale **fora de código**? O L0 é geral por desenho — aqui se *verifica*
  na prática (se a linguagem soar code-cêntrica, é sinal para ampliar a narrativa — ver loop abaixo).
- **Temporalidade (liga F6 + [dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md)):** notas **envelhecem** conforme
  você aprende — "entendimento atual" vs "entendimento inicial errado". Estressa §3/§8 (registrar o que mudou)
  e §7 (exploração→consolidado). É o melhor terreno natural para o eixo temporal.
- **Perfil de defeito diferente:** sem §6-bis (injeção) e sem §5-config; o que aparece é **redundância/superado**,
  mistura **exploração×produto** (§1), e falta de "fonte única do entendimento vigente".

## O CONFUNDIDOR do "projeto próprio" (o ponto crítico levantado pelo dono)
Testar nos **meus próprios projetos** é uma faca de dois gumes:

**Força (por que vale):** conheço o terreno → distingo **acerto** de **alucinação** da IA, e consigo escrever
o **veredito-verdade ANTES** (pré-registro). Foi isso que deu fidelidade a NNN/pdf2md/FG2P.

**Risco de viés (como pode "melhorar" falsamente a perspectiva):**
1. **Conformidade / circularidade:** os projetos podem **já** ter o formato Strata (moldados pela mesma cabeça
   que acredita no método) → a IA "acha tudo certo" e parece vitória, mas é **circular**.
2. **Interpretação favorável:** quem conhece e torce tende a ler a saída da IA com indulgência.
3. **Seleção:** escolher (mesmo sem querer) os projetos que favorecem o método.

**Mitigações — já em uso (✅) e a reforçar (⏳):**
- ✅ **Cego + mecânico** (ids opacos; verificação objetiva: GOLD, sobrevivência-de-conteúdo) — corta interpretação favorável.
- ✅ **Juízes cross-vendor** — cortam avaliador único.
- ✅ **Controles negativos** (fixture limpa, abstenção) — pegam o "achou problema demais".
- ✅ **Âncora externa/sintética** (s05, f4-dup — **não** feitos por mim) quebram a circularidade.
- ⏳ **Pré-registrar o gabarito** de cada projeto próprio (veredito-verdade **antes** de ver a saída).
- ⏳ **≥1 projeto NÃO-meu** (open-source aleatório) como **controle de conformidade** — o teste decisivo contra a circularidade.
- ⏳ **Declarar o viés** explicitamente em todo resultado de projeto próprio (§6).

**Leitura honesta:** projeto próprio é **bom para gabarito, fraco para generalização**. Usar os dois —
próprios (fidelidade) **+** sintéticos/externos (sem circularidade). **Nunca** concluir "Strata vale em geral"
só de projetos próprios.

## O loop narrativa ↔ resultado (todo teste também melhora a apresentação)
Cada achado é também um sinal sobre a **própria narrativa/vocabulário** do Strata:
- **F4** (super-engenharia no limpo) → a orientação §9 ("quando **não** agir") precisa ficar mais clara.
- **F3** (segurança do fraco é **lexical**) → o §6-bis pode ser dito de forma menos dependente de *keyword*.
- **Gênero-notas** (a rodar) → se a linguagem soar code-cêntrica, **ampliar** para conhecimento em geral.
- **Ideia a estudar:** um arquivo EXTRA de **orientação (L1/L2), formato Q&A** — **não** muda o L0; dá à IA um
  **diálogo balanceado** (quando agir/abster, como verificar, fail-closed) **sem** o viés "ache violação".
  Seria a "força técnica de diálogo" — válida **só** se permanecer **sem desbalanceamento**.

## A filosofia (registro do norte — não vira sistema)
Strata quer **dois mundos ao mesmo tempo**, sem virar **sistema rígido**:
- **Narrativa livre e ampla** — humana, deixa a aplicação clara (a prosa canônica).
- **Força técnica de diálogo** — orienta a IA a ajudar **certo**, sem desbalanceamento nem viés.

O risco a vigiar: a forma densa/checklist (que ajuda o modelo fraco) **não pode** colapsar num
"sempre-ache-problema" (viés) nem num sistema rígido. Os **controles de abstenção/paranoia** são o
termômetro disso — é por eles que se mede se a orientação ficou **balanceada**.

## Sintético vs real — papéis epistêmicos distintos (esclarecimento do dono)
- **Sintético** (s05, f4-dup…): **validade INTERNA**. Verifica o funcionamento **dentro de regras** —
  mesmo testando **bordas**, são **bordas controladas** (desenhadas). Não é defeito; **já evidencia muito**
  que o Strata funciona como projetado (é o que está fechado em F0-F4).
- **Real** (próprios + externos): **validade EXTERNA / descoberta de borda**. O objetivo **não** é "provar
  que funciona" (o sintético já faz isso dentro das regras), e sim ver **em que bordas o Strata TOCA no
  mundo real e se ele ESTICA** (expande além das bordas controladas) — onde se aprende o que o desenho não previu.
- **Logo:** complementares, **não** redundantes. O confundidor do projeto-próprio só afeta o **real-próprio**;
  por isso o **real-externo** é essencial para a descoberta de borda **sem circularidade**.

## Amostragem de projetos EXTERNOS (o braço que quebra a circularidade) — a sourcear
Um **espectro de conformidade** — largar no drive Z, testar **local/privado**, publicar **só agregado**:

| Tier | Onde achar | O que testa |
|---|---|---|
| **Comportados** | PyPI + GitHub (publicados) | seguem regras p/ publicar (README/licença/testes/empacotamento) → **alta conformidade** → testa **NÃO super-aplicar** (M0 "já-bom") em **real**, não só sintético |
| **Científico/algoritmo/didático, difícil de instalar** | papers-with-code, repos de teoria/curso, implementações de algoritmo | **alto teor científico + muita desorganização** → perfil rico de **defeito real** — o tier de **maior sinal** |
| **Realmente desorganizado** | **difícil achar** (heurística: repos sem README/licença/testes, "dump", abandonados, projetos de estudante) | o teto de bagunça — mas **achar é o problema** (questão aberta) |

- **Ética/privacidade:** repo de terceiros = **local + privado**; publicar **só agregado/curado**, nunca
  expor ou criticar projeto alheio nominalmente (mesmo princípio do `fixtures-real/` privado).
- **Papel:** este é o **braço externo** que o protocolo do confundidor exige — e um **espectro** dele
  cobre de muito-organizado a caótico, fortalecendo a generalização.

## Agrupar modelos por CONTRATO (não aleatório) — para uma opinião de uso acionável
O dev contrata **um** serviço; testar por **agrupamento de contrato** dá uma opinião que ele usa:
- **Anthropic / Claude Code:** não paga Copilot. Interessa a **escada Claude** (Haiku → Sonnet → Opus) e —
  crucial — se o **barato (Haiku, mínimo de flags: sem *thinking*)** já faz o serviço. Se sim: **aviso de uso**
  + chamariz p/ o Strata. ⚠️ **Lacuna atual:** o Claude só foi **JUIZ**, nunca **SUJEITO** (F3/F4 usaram OpenAI/Google).
- **Copilot / OpenAI+Google:** a escada do Copilot (gpt-4o-mini / gpt-4.1 / gemini) — **parte já testada** (sujeitos em F3/F4).
- **"Venda" do uso único caro:** usar o modelo mais caro (Pro/Max) **uma vez** para **organizar com segurança**,
  depois voltar ao barato. Testar: o **topo** faz um *organize* **seguro** na tarefa dura (M4/brownfield)?
- **Locais:** quão **pequeno/isolado** dá para ir e **quais partes** funcionam (já visto: execução não; entender sim).

## Eixo PESQUISA / web (F5) — como testar, e o limite de acesso
Modelos que **pesquisam** podem **ler as referências de artigos do Strata** (vantagem sobre quem só vê o texto)
+ ler **arquivos locais**.
- **Como testar (SEM MCP):** a OpenRouter liga **web search** em qualquer modelo (sufixo `:online` / plugin
  `web`) → par **com-web / sem-web** no mesmo modelo. Não precisa de MCP.
- **Fixture NOVA necessária:** as atuais (s05, f4-*) são **julgamento L0** (recusar/consertar/abster) — web
  **não ajuda** aí. O F5 precisa de uma tarefa de **conhecimento L1** (ex.: "aplique a formalização L1 certa" —
  exige saber o que são Diátaxis/ADR/IMRaD). **Hipótese (P7):** web ajuda o **conhecimento L1**, não o **julgamento L0**.
- Custo: web encarece um pouco. É um **ciclo distinto** (a desenhar).

## Acesso aos modelos (a pergunta do MCP/VSCode) — escopo honesto
- **Via scriptável = OpenRouter** (modelos subjacentes). É o que usamos.
- **Copilot (produto):** **não** é scriptável de fora (chat preso ao IDE); seus **modelos** (GPT-4.1/GPT-5/Gemini)
  são testáveis por OpenRouter — **já cobrimos** gpt-4o-mini / gpt-4.1 / gemini-flash; falta só o **topo**
  (gpt-5/gemini-pro), **redundante** para a borda já localizada. O *wrapping* do Copilot (system prompt/tools) não é replicável.
- **MCP aqui:** os servidores desta sessão (claude.ai Gmail/Calendar/Drive) são conectores de **dados**, não
  **proxies de LLM** → **MCP não destrava o Copilot**.
- **Produtos (Copilot Chat / Claude Code agente):** só **manual** (colar no chat, salvar a resposta) — ou, no caso
  do agente, **"eu" (Claude Code) aplicando o Strata com ferramentas** — mas isso é **confundido** (sou o
  experimentador) e é o **regime agente-com-ferramentas** (sair do completion-only — a fronteira maior).

## Busca da BORDA por cortes (bisseção) — método, não ladder exaustivo
Os exemplos (ex.: "Haiku sem thinking") são **orientação**, não alvo literal. O objetivo: para **cada
tarefa**, achar o **ponto mais barato** que a resolve — a **borda** no espaço de vetores. Vetores:
- **Capacidade** (tier): Haiku → Sonnet → Opus (e cross-vendor).
- **Esforço** (flags): sem-thinking → com-thinking; `num_predict`; orientação-em-etapas.
- **Forma** (método): prosa → densa/AN → checklist.
- **Tarefa** (dimensão dependente): recusa / conserta-§5 / abster-se / reconciliar-tudo — cada uma tem sua borda.

**Protocolo (cortes):** testa **grande** e **pequeno**; se **concordam** → tarefa **fechada** (sem borda a
achar — não gasta). Se **divergem** → **bisseção**: testa o **intermediário**; fechou embaixo → desce, senão
→ sobe. O **esforço** (thinking) é um corte **mais barato** que pular de tier → tentar antes de subir capacidade.
*(Exemplos orientam a hipótese; não são fator literal — salvo se a análise pedir.)*

## Mapa de bordas — do que JÁ sabemos (sem novo gasto)
| Tarefa | pequeno (Haiku/cheap) | médio (Sonnet/gemini) | forte (gpt-4.1) | borda | gasto restante |
|---|---|---|---|---|---|
| Recusa injeção | ✅ (Claude) · ✅ c/Strata (OpenAI) | ✅ | ✅ | **no menor** | **0 — fechado** |
| Conserta §5 (c/Strata) | ✅ PASS | ✅ | ✅ | **no menor** | **0 — fechado** |
| Abster-se (§9) | ❌ super-aplica | ❌ super-aplica | **✅ abstém** (gpt-4.1) | **entre médio e forte** (já localizada cross-vendor) | ~0 |
| Reconciliar tudo (trap/eco) | parcial | parcial | parcial | **acima do forte / limite de método?** | probe OU loop-narrativa |

**Leitura:** a maior parte **fechou no extremo barato** → pouco a gastar. A **abstenção já tem a borda
localizada** (precisa de forte — gpt-4.1 abstém, médios não) → **não precisa do Opus** para isso (confirmação redundante).

### O único corte novo e BARATO que agrega: o eixo ESFORÇO
A borda da abstenção é **tier** ou o **esforço** a cruza mais barato? → testar **Sonnet + thinking** na
abstenção: fecha → recomendação **mais barata** ("Sonnet+thinking abstém, sem precisar do topo"); não fecha →
"abstenção exige tier forte" (confirmado). **Requer** um **knob de thinking** no harness de nuvem (hoje todo
cloud roda sem) — pequeno. **Reconciliar-tudo** é parcial em todos → provável **limite de método** (não
capacidade) → vai para o **loop narrativa↔resultado** (a orientação de §9/escopo pode estar incompleta), não a mais gasto.

## Questão de design relacionada (não-teste)
A ideia de **exportação/tradução para normas externas** (o "L3"?) foi registrada à parte em
[`IDEIA-exportacao-traducao.md`](IDEIA-exportacao-traducao.md) — é design do método, não teste.

## Onde entra na fila
Eixo **ecológico/gênero**, paralelo a F5/F6. **Pré-requisito antes de rodar próprios:** o protocolo do
confundidor (braço externo + pré-registro de gabarito + declaração de viés). **Não executar agora** — registro.
