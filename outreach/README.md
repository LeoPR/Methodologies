<!-- l10n: doc_id=strata-outreach-readme · lang=en · canonical -->
**English** · [Português](README.pt-BR.md)

# `outreach/`: outreach materials

Assets to present the project publicly. This is support material, not part of the
methodology itself (which lives in [`recipe/`](../recipe/)) and not part of the research
corpus ([`lab/`](../lab/)). It does not publish new metrics: every number comes from the
dated lab documents.

## How it is organized

The **root** holds the dated **news source**: one file per update, with the conclusions
compressed and the links. The **subfolders** are the **channels**: each formats that
source into a publication, respecting the limits of the medium. Rule: never edit a
channel text without updating the dated source first.

| Path | What it is |
|---|---|
| [`2026-08-03-update.en.md`](2026-08-03-update.en.md) / [`2026-08-03-atualizacao.md`](2026-08-03-atualizacao.md) | the current news source (EN / PT): state, headlines, cost, honesty |
| [`linkedin/`](linkedin/) | LinkedIn channel: `post.*` (short), `artigo.*` (long technical), `2026-06-post.*` (previous edition), images |
| [`medium/`](medium/) | Medium channel: `historia.*` (narrative long-form story) |

Each dated file is the **publication itself** for its channel, not a brief about one.

## Channel limits (what each medium accepts)

- **LinkedIn post** (`linkedin/post.*`): short text (~3,000 character limit); the first
  2-3 lines show before "see more", so the hook comes first; attach the matching
  `.png` (do not paste the link as a preview; the image is the visual, the link stays
  clickable in the text); hashtags at the end.
- **LinkedIn article** (`linkedin/artigo.*`): free long-form, headings and lists render;
  good for the technical version with the full numbers; end with the repository link.
- **Medium story** (`medium/historia.*`): free long-form with title + subtitle;
  markdown imports cleanly; no hashtag block (Medium uses up to 5 tags set in the
  publisher, e.g. Knowledge Management, Artificial Intelligence, Methodology);
  first-person narrative works better than lists there.
- For a shorter LinkedIn post, cut middle items; the core (hook + best 2-3 findings +
  honesty line + link) stands on its own.

**Re-render PNG from SVG** (after editing an `.svg`): everything stays inside the
project venv (`playwright` + Chromium in `.venv/pw-browsers`):

```bash
.venv/Scripts/python -m pip install playwright   # once
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python -m playwright install chromium   # once
PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" .venv/Scripts/python tools/render_svg_png.py outreach/linkedin/strata-linkedin.svg outreach/linkedin/strata-linkedin.pt-BR.svg
```

Browser-faithful rendering (same engine as the VS Code preview), 2400x2400 px.
