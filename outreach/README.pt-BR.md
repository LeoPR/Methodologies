<!-- l10n: doc_id=strata-outreach-readme · lang=pt-BR · source_lang=en · translation_of=README.md -->
[English](README.md) · **Português**

# `outreach/`: material de comunicação

Peças para **apresentar o projeto publicamente** (posts, imagens). É **apoio**, não faz parte
da metodologia (esta vive em [`recipe/`](../recipe/)) nem da pesquisa ([`lab/`](../lab/)).

| Arquivo | O que é |
|---|---|
| [`LINKEDIN-post.md`](LINKEDIN-post.md) | o post do LinkedIn em si (inglês) |
| [`LINKEDIN-post.pt-BR.md`](LINKEDIN-post.pt-BR.md) | o mesmo post em português |
| `strata-linkedin.png` / `.svg` | imagem em inglês e fonte editável |
| `strata-linkedin.pt-BR.png` / `.svg` | imagem em português e fonte editável |

**Notas de produção (publicação):**
- Cada arquivo de post é a própria publicação: anexe o `.png` correspondente e cole
  o texto abaixo dela (texto puro; a primeira linha é o gancho antes do "ver mais").
- Poste imagem + texto juntos (não cole o link como prévia; a imagem já é o visual,
  e o link fica clicável no texto).
- Para um post mais curto, corte o parágrafo da Mnemósine e/ou os 2 últimos sobre IA;
  o núcleo (gancho + 3 camadas + propósito + link) se sustenta sozinho.
- Os 3 emojis coloridos casam com as cores do gráfico (azul/verde/laranja).

**Re-render do PNG a partir do SVG** (depois de editar um `.svg`): tudo dentro
do venv do projeto (`playwright` + Chromium em `.venv/pw-browsers`):

```bash
.venv/Scripts/python -m pip install playwright   # uma vez
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python -m playwright install chromium   # uma vez
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python tools/render_svg_png.py outreach/strata-linkedin.svg outreach/strata-linkedin.pt-BR.svg
```

Renderização fiel de navegador (o mesmo motor do preview do VS Code), 2400x2400 px.
