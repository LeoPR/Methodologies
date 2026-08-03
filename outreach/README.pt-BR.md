<!-- l10n: doc_id=strata-outreach-readme · lang=pt-BR · source_lang=en · translation_of=README.md -->
[English](README.md) · **Português**

# `outreach/`: material de comunicação

Peças para apresentar o projeto publicamente. É apoio, não faz parte da metodologia
(esta vive em [`recipe/`](../recipe/)) nem da pesquisa ([`lab/`](../lab/)). Não publica
métrica nova: todo número vem dos documentos datados do lab.

## Como se organiza

A **raiz** guarda a **notícia-fonte datada**: um arquivo por atualização, com as
conclusões comprimidas e os links. As **subpastas** são os **canais**: cada um formata
essa fonte numa publicação, respeitando os limites do meio. Regra: nunca edite o texto
de um canal sem antes atualizar a fonte datada.

| Caminho | O que é |
|---|---|
| [`2026-08-03-atualizacao.md`](2026-08-03-atualizacao.md) / [`2026-08-03-update.en.md`](2026-08-03-update.en.md) | a notícia-fonte vigente (PT / EN): estado, manchetes, custo, honestidade |
| [`linkedin/`](linkedin/) | canal LinkedIn: `post.*` (curto), `artigo.*` (técnico longo), `2026-06-post.*` (edição anterior), imagens |
| [`medium/`](medium/) | canal Medium: `historia.*` (história narrativa longa) |

Cada arquivo datado é a **própria publicação** do seu canal, não um brief sobre ela.

## Limites dos canais (o que cada meio aceita)

- **Post do LinkedIn** (`linkedin/post.*`): texto curto (limite de ~3.000 caracteres);
  as 2-3 primeiras linhas aparecem antes do "ver mais", então o gancho vem primeiro;
  anexe o `.png` correspondente (não cole o link como prévia; a imagem já é o visual,
  e o link fica clicável no texto); hashtags no final.
- **Artigo do LinkedIn** (`linkedin/artigo.*`): formato longo livre, títulos e listas
  renderizam; bom para a versão técnica com todos os números; termine com o link do
  repositório.
- **História do Medium** (`medium/historia.*`): formato longo livre com título +
  subtítulo; markdown importa bem; sem bloco de hashtags (o Medium usa até 5 tags
  definidas no editor, ex.: Knowledge Management, Artificial Intelligence, Methodology);
  narrativa em primeira pessoa funciona melhor que listas lá.
- Para um post mais curto no LinkedIn, corte itens do meio; o núcleo (gancho + 2-3
  melhores achados + linha de honestidade + link) se sustenta sozinho.

**Re-render do PNG a partir do SVG** (depois de editar um `.svg`): tudo dentro
do venv do projeto (`playwright` + Chromium em `.venv/pw-browsers`):

```bash
.venv/Scripts/python -m pip install playwright   # uma vez
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python -m playwright install chromium   # uma vez
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python tools/render_svg_png.py outreach/linkedin/strata-linkedin.svg outreach/linkedin/strata-linkedin.pt-BR.svg
```

Renderização fiel de navegador (o mesmo motor do preview do VS Code), 2400x2400 px.
