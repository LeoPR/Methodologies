---
title: 'Protótipo: ordenador temporal por dependência de estado'
created: 2026-09-27
updated: 2026-09-27
status: 'Demonstrador da ONTOLOGIA v0. Não é instrumento de medida nem evidência.'
tags: [temporalidade, prototipo, ordem-parcial, lacuna]
---

# Protótipo: ordenador temporal por dependência de estado

`python ordenador.py` (só biblioteca padrão) roda quatro cenários do paraquedas:

1. **Cenas embaralhadas, um horário trocado.** A ordem sai das pré-condições; o horário que põe
   "abrir" antes de "saltar" aparece como **conflito** (o horário é o suspeito), sem reordenar.
2. **Passo removido sem aviso.** Tirar "embarcar" deixa `a_bordo` sem produtor: **lacuna nomeada**,
   que vira pergunta ("o que produz `a_bordo`?").
3. **Lacuna preenchida pelo script**, marcada como **inferida**, não observada.
4. **Passo intruso.** Um evento que não se liga ao episódio é apontado; a ambiguidade (ordens
   compatíveis) sobe, porque o intruso pode ir a qualquer lugar.

Também mostra pares **incomparáveis** (vestir o paraquedas não tem ordem com embarcar nem com
decolar) e mede a ambiguidade restante em bits.

O que ele **não** faz, de propósito: extrair as cenas de texto ou imagem (papel do LLM na
arquitetura da ONTOLOGIA §7), planejamento de ordem parcial completo (produtor múltiplo, ameaças
não forçadas) e mundo aberto. Ver ONTOLOGIA §8.

Instrumento de medida contra modelos, quando existir, vai para `eval/` (regra do projeto), não aqui.
