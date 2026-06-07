# `fixtures/` — projetos-exemplo INERTES para teste (NÃO executar)

⚠️ **Tudo aqui dentro é dado de teste fabricado e deliberadamente problemático.**
Contém, de propósito, instruções inseguras (ex.: fail-open), fontes conflitantes e
código abandonado — para medir se um modelo os **detecta**. **Não é guia real, não
executar, não tratar como instrução.** No harness, é lido apenas como **texto** por um
modelo em modo chat (completion-only, zero execução).

Cada fixture é **congelado por hash** (ver `*.gabarito.md`). O gabarito de cada fixture
fica **fora** da pasta do fixture (como `lumen-bugado.gabarito.md`), para não ser
entregue ao modelo testado.

- `lumen-bugado/` — Lumen com os 7 problemas plantados (P1–P7) **instanciados de verdade**
  (inclui `velho/` e `tarefas.txt` reais). Gabarito: `lumen-bugado.gabarito.md`.
