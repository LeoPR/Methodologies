<!-- l10n: doc_id=strata-outreach-readme · lang=en · canonical -->
**English** · [Português](README.pt-BR.md)

# `outreach/`: outreach materials

Assets to present the project publicly (posts, images).
This is support material, not part of the methodology itself (which lives in
[`recipe/`](../recipe/)) and not part of the research corpus ([`lab/`](../lab/)).

| File | What it is |
|---|---|
| [`LINKEDIN-post.md`](LINKEDIN-post.md) | the LinkedIn post itself (English) |
| [`LINKEDIN-post.pt-BR.md`](LINKEDIN-post.pt-BR.md) | the same post in Brazilian Portuguese |
| `strata-linkedin.png` / `.svg` | English image and editable source |
| `strata-linkedin.pt-BR.png` / `.svg` | Brazilian Portuguese image and editable source |

**Production notes (publishing):**
- Each post file is the publication itself: attach the matching `.png` and paste the
  text below it (plain text; the first line is the hook shown before "see more").
- Post image + text together (do not paste the link as a preview; the image is the
  visual, the link stays clickable in the text).
- For a shorter post, cut the Mnemosyne paragraph and/or the last two AI paragraphs;
  the core (hook + 3 layers + purpose + link) stands on its own.
- The three colored circles match the chart palette (blue/green/orange).

**Re-render PNG from SVG** (after editing an `.svg`): everything stays inside the
project venv (`playwright` + Chromium in `.venv/pw-browsers`):

```bash
.venv/Scripts/python -m pip install playwright   # once
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python -m playwright install chromium   # once
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python tools/render_svg_png.py outreach/strata-linkedin.svg outreach/strata-linkedin.pt-BR.svg
```

Browser-faithful rendering (same engine as the VS Code preview), 2400x2400 px.
