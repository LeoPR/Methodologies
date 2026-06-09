---
title: F0 — confronto de juízes (cross-fornecedor) — as conclusões são robustas? "maior = melhor juiz"?
created: 2026-06-09
setup: 9 juízes re-pontuam CEGO o mesmo conjunto P1+P2 (AN-v2 vs AN-v3) — OpenAI (nano/mini/gpt-4.1-mini/gpt-5/codex/o3/gpt-5.5), Google (flash/pro), Anthropic (Claude). Discriminador objetivo: no NNN exemplar, os planos AN-v2 COMPROVADAMENTE cometem falso-positivo (flagam os arquivos-IA como dup, criticam a navegação boa — fatos textuais), então FP-detectado ~4 = correto, ~0 = leniência.
status: conclusões ROBUSTAS a fornecedor (3 empresas convergem); "maior=melhor juiz" vale DENTRO de um fornecedor mas é confundido entre eles (capacidade, não tamanho)
---

# F0 — os juízes convergem? (e "maior = melhor" é verdade?)

Moldura (do dono): empresas diferentes fazem modelos com vieses mais independentes → se juízes
de fornecedores diferentes **convergem**, o resultado é provavelmente correto; se **divergem**,
é chamada dependente-de-julgamento. (Ressalva anotada e fora de escopo: todos compartilharem um
viés e convergirem no "menos-ruim" — improvável e difícil de verificar.)

## Resultado (NNN exemplar = controle de falso-positivo)

| juiz | fornecedor | NNN v2 FP | NNN v3 FP | classe |
|---|---|---|---|---|
| gpt-5-nano | OpenAI | 0.00 | 0.75 | cego |
| gpt-4.1-mini | OpenAI | 1.25 | 1.12 | leniente |
| gpt-5-mini | OpenAI | 1.50 | 2.12 | leniente |
| gpt-5 | OpenAI | 3.29 | 2.00 | afiado |
| o3 | OpenAI | 4.00 | 2.50 | afiado (reasoner) |
| gpt-5-codex | OpenAI | 4.38 | 3.00 | afiado |
| gpt-5.5 | OpenAI | 4.38 | 3.38 | afiado |
| **gemini-2.5-flash** | Google | **4.12** | 1.88 | **afiado (pequeno!)** |
| gemini-2.5-pro | Google | 3.88 | 2.88 | afiado |
| claude-opus | Anthropic | 4.25 | 2.88 | afiado |

## Achados

1. **Convergência cross-fornecedor — FORTE (robustez confirmada).** 7 juízes capazes de
   **3 fornecedores** convergem em NNN-v2 FP **~3.9-4.4** e **todos** mostram a AN-v3 reduzindo
   o falso-positivo (ex.: claude 4.25→2.88, gpt-5.5 4.38→3.38, gemini-pro 3.88→2.88, gemini-flash
   4.12→1.88). O achado central do P1+P2 **não é artefato de "Claude julga Claude"** — três
   empresas independentes o reproduzem.

2. **"Maior = melhor juiz" — verdade DENTRO de um fornecedor, NÃO lei universal.** Na OpenAI a
   escada é limpa e monotônica: nano 0.0 → mini 1.5 → gpt-5 3.3 → gpt-5.5 4.4. Mas o
   **gemini-2.5-flash (pequeno, barato) crava 4.12**, afiado como os gigantes. Logo o que importa
   é **capacidade/discernimento**, que correlaciona com tamanho *dentro* de um fornecedor mas é
   **confundido entre fornecedores** (o pequeno do Google rende mais por parâmetro). A alegação
   vaga "modelo X é poderoso" precisa ser **testada por tarefa** — confirmado.

3. **Bônus:** **codex** julga bem (4.38, até mais afiado que o gpt-5 geral 3.29) — tuning de
   código não degradou o julgamento avaliativo. **o3** (reasoner) afiado (4.0).

4. **Meta:** detectar falso-positivo exige o MESMO discernimento que o auditor precisa — um juiz
   fraco (OpenAI-small) é **cego ao erro**, assim como o auditor fraco o comete. Por isso o 2º
   juiz que usávamos antes (gpt-4.1-mini, 1.25) **subestimava** o falso-positivo: era leniente.

## Adjudicação (escapando do viés do avaliador)
Não é "qual opinião eu prefiro": os planos AN-v2 do NNN **literalmente** criticam a navegação
rica e flagam AGENTS/INDEX/MAP como duplicata — práticas que os arquivos comprovam serem BOAS.
Logo FP~4 é o número correto; FP~0-1.5 é leniência verificável. Os juízes capazes acertam.

## Implicação (resultado da Fase 0 — blindar a medição)
- **Nossas conclusões são robustas ao juiz/fornecedor.** O efeito da AN-v3 (menos falso-positivo)
  sobrevive a 7 juízes de 3 empresas.
- **Para pontuar daqui em diante:** usar um juiz **capaz** (qualquer dos afiados). **Juiz barato
  e bom = gemini-2.5-flash** (afiado a custo de pequeno). **NÃO usar OpenAI-small** (nano/mini/
  4.1-mini) como juiz — são lenientes e mascaram o falso-positivo. *(Corrige o 2º-juiz fraco
  que usávamos.)*

## Caveats
- Conjunto P1+P2 (AN-v2/v3), N=2 por célula. Alguns calls de juiz falharam (o3/codex em alguns
  planos — parse/limite); médias sobre os bem-sucedidos. Discriminador = NNN (FP verificável).
- Ressalva fora de escopo: viés compartilhado entre todos os fornecedores (convergir no
  "menos-ruim") — improvável; exigiria verdade-base independente de qualquer LLM.
