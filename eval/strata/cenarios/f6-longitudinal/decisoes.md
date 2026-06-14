# Decisões do projeto

- **D1** — Parsing dos arquivos feito manualmente (função própria).
- **D2** — Trocamos para a biblioteca `fastparse` (mais rápida que o parser manual).
- **D3** — Voltamos ao parsing manual: a `fastparse` quebrou com entradas em Unicode
  e foi removida das dependências. Mantemos o manual até achar uma alternativa estável.
