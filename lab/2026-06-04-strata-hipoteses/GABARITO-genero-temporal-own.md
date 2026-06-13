---
title: 'GABARITO PRE-REGISTRADO — eixos GENERO + TEMPORAL (2 projetos de curso do dono)'
created: 2026-06-13
status: 'PRE-REGISTRADO antes de qualquer modelo-sujeito rodar (gravado/commitado antes de pontuar a sonda)'
nota: 'NAO entregar aos modelos testados — uso exclusivo da pontuacao cega.'
ressalva: 'projeto + analista + autor-do-metodo da MESMA familia (Leonardo + Claude) — NAO e braco independente.'
---

# Gabarito pré-registrado — gênero esperado, padrões que importam, veredito esperado

> Construído por agentes-analistas (Claude) lendo **apenas o digest de organização** de AulaQuantum e
> DeepLearning (conteúdo acadêmico excluído), **antes** de qualquer modelo-sujeito rodar a sonda. Os
> artefatos citados foram conferidos por existência na árvore. **Leia a ressalva de circularidade no fim.**

## Regra-mãe (eixo GÊNERO)
Ambos são **acompanhamento-de-aula (caderno de curso)**, **não** software nem pesquisa. Logo a barra de
software (CI, LICENSE, tests, packaging) **não se aplica** (§9). O placar que conta é o **score_GÊNERO**,
não o score_SW. Um modelo gênero-cego que penaliza por CI/LICENSE/tests ausentes, ou marca pares
fonte→derivado como "duplicação", comete **FALSO POSITIVO** — e é exatamente isso que medimos.

## Projeto 1 — own-aulaquantum (AulaQuantum)
- **Gênero esperado:** caderno de acompanhamento de disciplina (híbrido **leve** notas+software; sw subordinado).
- **Padrões que importam p/ o gênero (presentes):**
  - **§5 fonte única:** `CURSO.yaml` (SSOT de metadados) + `PRESENTATION.md` como FONTE de PPTX/PDF (md-as-hub via `tools/convert/cli.py`).
  - **L0/L1/L2:** `pesquisa_geral/` (atemporal) / `TEMPLATE_SEMANA.md` + estrutura por semana (padrões) / `tools/convert/` (ferramentas).
  - **§3/§8 história:** `.git` presente (T001 git_init), ledger de tickets `{open..closed,_archive}` append-only, `REVIEW` cumulativo, datas reais.
  - **tombstone:** `old/` por semana + tickets `closed/_archive` + ponteiro datado pdf2md (preservar/apontar, não apagar).
  - **§9:** pesquisa `pbr_theorem` marcada "não coberto nas semanas 1-7"; "o que vale propagar vs o que NÃO vale refazer".
- **NÃO exigir (gênero-cego erraria):** CI/CD, LICENSE, unit-test das práticas, tratar PPTX/zip versionados como "binário que não devia estar no git", marcar PRESENTATION.md+PPTX como duplicação.
- **Veredito gênero-consciente esperado:** **JÁ-BOM-PARA-O-GÊNERO** (forte nos dois eixos; densidade temporal alta).

## Projeto 2 — own-deeplearning (DeepLearning / UDL)
- **Gênero esperado:** caderno de estudo do livro UDL (híbrido pontual na "assets 6": pipeline de treino real + entrega ao professor).
- **Padrões que importam p/ o gênero (presentes):**
  - **§5 fonte única:** `padrao_respostas_e_programas.md` (convenções) + `md_para_docx.py` (.md fonte, .docx derivado).
  - **tombstone (FORTE):** "[dataset/] DELETADO — recriável (Kaggle)", "[.venv/] DELETADO — recriável", "artefatos_estudo_week6 → Z: via link file:///", "outputs/ MANTER".
  - **§9 abstenção:** código só quando o enunciado pede (só 5.2 pede plot); "Programas opcionais (se quiser praticar)".
  - **§6 honestidade de fonte:** "perguntas em inglês (livro) / respostas em português"; nomeia origem Kaggle.
  - **§3 história (PARCIAL):** `robust_train_log.txt` = único registro cronológico real (25 epochs, test_acc=0.9273).
- **NÃO exigir (gênero-cego erraria):** pkg_meta/tests/CI/LICENSE; CHANGELOG/história append-only datada (`datas_rastreio=false` **não** é defeito aqui); reabrir exercícios marcados como não-necessários; cobrar reidratação do dataset/.venv deletados.
- **Veredito gênero-consciente esperado:** **JÁ-BOM-PARA-O-GÊNERO** (tombstone forte; história-imutável fraca, aceitável p/ gênero).

## Diferença pré-registrada entre os dois (a sonda DEVE captar)
**AulaQuantum > DeepLearning no eixo TEMPORAL:** AulaQuantum tem VCS+ledger+datas (append-only real);
DeepLearning tem tombstone forte mas SEM VCS/CHANGELOG (só o `train_log` é cronológico). Uma sonda que
der o **mesmo** veredito temporal aos dois sem notar essa assimetria **leu raso**.

## Armadilhas NEGATIVAS (um bom modelo NÃO cai)
- **N1** — ler "[dataset/] DELETADO — recriável" como **PERDA/defeito** (é tombstone+ponteiro).
- **N2** — ler "semana9e10" como **duplicata** de semana9/semana10 (é **FUSÃO**/consolidação temporal).
- **N3** — exigir **CI/LICENSE/tests** p/ caderno de curso (viola §9).
- **N4** — marcar par **fonte→derivado** (.md/.docx, PRESENTATION.md/PPTX) como **duplicação** de §5.
- **N5** — mandar **apagar `old/`** ou itens da "Lista de Lixo" já agora (apaga o tombstone; o certo é preservar+marcar).

## Itens concretos de teste temporal (artefato → leitura correta vs erro gênero/tempo-cego)
| Projeto | Artefato | Leitura CORRETA | Erro gênero/tempo-cego |
|---|---|---|---|
| aulaquantum | `semana9e10/` (zips QFT_Shor, S7S8_Recarga) | fusão/consolidação de 2 semanas; zips = snapshots de entrega | "duplicata de semana9/10 → unificar/remover" |
| aulaquantum | `semana1/old/` + "Lista de Lixo" (rev 2026-04-25) enumerando old/ e VERIFICACAO_SEMANA1.md | tombstone físico: enumera candidatos mas NÃO apagou (preservar+marcar) | "execute a limpeza: delete old/ e VERIFICACAO agora" (apaga história) |
| aulaquantum | `CURSO.yaml`+`PRESENTATION.md` → PPTX/PDF via cli.py | fonte única §5 com derivados regeneráveis (edita a fonte, nunca o derivado) | "mesmo conteúdo em 3 formatos = viola fonte única → apagar 2" |
| deeplearning | README "[dataset/] DELETADO — recriável (Kaggle)", "[.venv/] DELETADO — recriável" | tombstone textual: marcado+instrução de recriação (ponteiro, não conteúdo) | "dataset ausente, projeto quebrado, reidratar" (perda, não tombstone) |
| deeplearning | "outputs/ … MANTER" ao lado dos DELETADO; "week6 → Z: via file:///" | retenção deliberada vs arquivamento com ponteiro (política temporal consciente) | "207 MB de binário no repo, remover" OU "link Z: quebrado/dependência inválida" |
| deeplearning | `robust_train_log.txt` (25 epochs) único cronológico; sem CHANGELOG/git | log append-only é registro temporal suficiente p/ o gênero; falta de CHANGELOG não é defeito | "sem versionamento/datas = sem rastreabilidade" OU "test_acc=0.9273 = teste de software" |

## ⚠️ Ressalva de circularidade (honesta e limitante)
Os **projetos-sujeito** (AulaQuantum, DeepLearning), o **analista** que produziu este gabarito e o **autor
do método** são da mesma família/dono — Leonardo (projetos) + Claude (analista e co-autor do método). Isto
**não é um braço independente**; é quase **auto-avaliação**.
- **Permite concluir:** (a) que os artefatos descritos **existem** na árvore (verificável; foram conferidos) e (b) que **são interpretáveis** como instâncias dos princípios do Strata.
- **NÃO permite concluir:** (c) que os princípios do Strata são "válidos/bons" porque estes projetos os encarnam — seria *petitio principii* (o dono que escreveu o método organizou os cadernos no mesmo estilo; convergência é esperada **por construção**, não descoberta). E se gabarito (mesma família) e sonda (modelo) concordarem, isso mede no máximo se **o modelo lê gênero/tempo como o autor lê** — **não** se o autor está certo.
- **Para quebrar a circularidade de verdade:** projetos de **terceiros** + juiz cego que não viu o Strata.
- **Valor real (restrito):** teste de **leitura gênero/tempo-consciente** de modelos (detectar o falso-positivo gênero-cego), **não** validação do método nem evidência de generalização.
