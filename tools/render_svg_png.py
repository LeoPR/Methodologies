#!/usr/bin/env python3
"""Renderiza SVG -> PNG com fidelidade de navegador (Chromium via Playwright).

Tudo contido no venv do projeto: exige `playwright` instalado e o Chromium em
`.venv/pw-browsers` (PLAYWRIGHT_BROWSERS_PATH apontando para ele; ver
outreach/README.md para o setup de uma vez).

Uso:
    PLAYWRIGHT_BROWSERS_PATH="$PWD/.venv/pw-browsers" \
        .venv/Scripts/python tools/render_svg_png.py arquivo.svg [outro.svg ...]

Gera <arquivo>.png ao lado de cada SVG, no tamanho declarado no SVG
(width x height) com device_scale_factor=2 (ex.: SVG 1200x1200 -> PNG 2400x2400).
"""
import os
import re
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("sem playwright no venv; ver outreach/README.md (setup).", file=sys.stderr)
        return 2

    jobs = []
    for svg in sys.argv[1:]:
        text = open(svg, encoding="utf-8").read(4000)
        mw = re.search(r'\bwidth="(\d+)"', text)
        mh = re.search(r'\bheight="(\d+)"', text)
        if not (mw and mh):
            print(f"{svg}: width/height nao declarados no SVG", file=sys.stderr)
            return 2
        jobs.append((svg, int(mw.group(1)), int(mh.group(1))))

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for svg, w, h in jobs:
            page = browser.new_page(viewport={"width": w, "height": h},
                                    device_scale_factor=2)
            page.goto("file:///" + os.path.abspath(svg).replace("\\", "/"))
            out = os.path.splitext(svg)[0] + ".png"
            page.screenshot(path=out)
            page.close()
            print(f"OK {out} ({w * 2}x{h * 2})")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
