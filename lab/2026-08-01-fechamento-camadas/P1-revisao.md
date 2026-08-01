---
title: P1-revisão — o §11 re-analisado sob a régua axiomática (segundo ciclo)
created: 2026-08-01
updated: 2026-08-01
status: FECHADA — §11 enxugado no canônico (2 regras novas + derivações declaradas);
  P2 re-confirmada; questões conceituais do L0 encerradas por convergência
supersedes-nota: revisa a posição da P1 (que propunha 4 regras); a P1 original permanece
  como traço (§3) — este doc é a superfície atual
---

# P1-revisão — o §11 sob a régua que refutou a P2

## 1. Por que este ciclo existe

A P2 foi refutada pela régua axiomática do dono (abstração não precisa de
apresentação; a demanda legítima é completude de **operações**). Justiça exige
re-submeter a P1 à **mesma** régua — se ela só passou por ter sido escrita
antes da régua existir, a aprovação do §11 está contaminada. (Registrado: a
reflexão axiomática **não** existia no repo antes de 2026-08-01 — varredura
grep por Hilbert/Benacerraf/ADT/maçã só encontra os docs deste ciclo.)

## 2. O teste, regra por regra (o §11 como entrou no canônico)

Régua: *derivável de outra seção = teorema (não se repete — §5); operação de
instanciação = fica fora; só entra o que é restrição/operação **não derivável**.*

| Regra do §11 aprovado | Teste de derivabilidade | Veredito |
|---|---|---|
| **1. Eixo declarado** ("por que característica?") | §3 exige rationale de toda decisão; o esquema é dispositivo (§3-bis); o rationale *de um esquema* **é** o seu eixo. | **Derivável** de §3+§3-bis. Não merecia regra própria. |
| **2. Divisão limpa** (exclusiva + exaustiva) | §1 *pratica* a regra num esquema ("cada tipo vive em um lugar próprio" = exclusividade; "acumula três tipos" = pretensão de exaustividade) mas **não a enuncia** para esquemas em geral. Não se deriva de §1 sem circularidade. | **Não derivável. FICA** — é a restrição genuinamente nova. |
| **3. Um eixo não basta → facetas** | Nada no L0 trata de objeto multidimensional; o caso `eval/` (não cabe nos 3 tipos de §1) é a prova de que o repertório não tinha a operação. | **Não derivável. FICA** — é a operação genuinamente nova. |
| **4. Esquema é hipótese de domínio, revisável** | Revisabilidade = supersessão (§3); justificação pelo corpus real = disciplina de fonte sobre o domínio (§6); "o caso que não cabe é evidência" = preservar-o-negativo (§4). | **Derivável** de §3+§4+§6. |

Sobrou também o **FORTE** ("quando um objeto não couber, revise o esquema, não
torture o objeto") — a permissão é derivável (§3), mas a regra operacional do
gatilho tem valor prático: entra como **corolário declarado**, não como
princípio (declarar-se corolário respeita §5).

## 3. Conclusão do ciclo

A régua **não** derruba o §11 — derruba **metade da redação dele**. Das 4
regras aprovadas, 2 eram teoremas re-enunciados (1 e 4) e 2 são o conteúdo
novo (2 e 3). A versão correta do §11 é a enxuta: a operação ("formar o
esquema") + as 2 regras não deriváveis + as derivações **declaradas como
derivações** (o que, aliás, *mostra* o L0 trabalhando: a seção nova se ancora
nas velhas em vez de duplicá-las).

Detalhe que a re-análise melhorou: a regra 1 não some — sobe para a definição
da operação no lead ("formar o esquema = declarar o eixo e dividir"), porque
declarar o eixo é **parte do ato de formar**, não um princípio separado.

## 4. Consequência para a P2 (re-verificação — "até se bastarem")

Re-rodei a P2 contra o §11 enxuto: a única interseção possível era "grão
declarado" (regra 2 da P2) espreitando como pré-condição da divisão limpa. Não
entra: sob Hilbert, os objetos são primitivos do corpus; a restrição da
divisão vale **para o que quer que se instancie** — declarar o grão é ato de
instanciação, não do núcleo. **P2 permanece refutada, agora sem aresta.**

O par se basta: a única operação que faltava ao repertório do L0 era "formar o
esquema"; todo o resto que os dois ciclos levantaram é teorema derivável ou
apresentação de instanciação. **As questões conceituais do L0 estão
encerradas** — não por esgotamento da imaginação, mas porque os dois testes
independentes (P1, P2) sob a mesma régua convergiram para o mesmo ponto e o
ponto parou de se mover.

(O que **permanece** aberto, fora do escopo "conceitual": P3-sigilo = escopo
declarado da varredura do Eixo 5; P4 = coerência interna da Parte I, reforçada
pela régua; P5 = editorial. Nenhum dos três põe em dúvida o fechamento
conceitual.)

## 5. Ação tomada

- §11 reescrito no canônico (PT + espelho EN): lead com a operação; regras
  **Divisão limpa** e **Facetas**; derivações declaradas (§3, §3-bis, §4, §6);
  FORTE rebaixado a corolário declarado; Aderência e Fundamentação intactas
  (as fontes sustentam o conteúdo remanescente; Aristóteles ancora o eixo no
  lead).
- Enumerações inalteradas (seguem 13 princípios).
