#!/usr/bin/env python3
"""Constroi um DIGEST de um projeto LOCAL do PROPRIO dono (ex.: AulaQuantum, DeepLearning) p/ o eixo
GENERO/TEMPORAL — so a CAMADA DE ORGANIZACAO (README/YAML/padrao/tickets/semanas-README), NUNCA o
conteudo academico (respostas/capitulos/datasets/PDFs). Computa sinais de conformidade de software +
sinais de genero 'acompanhamento-de-aula' (fonte-unica, doc-de-padroes, tickets, estrutura semanal,
tombstone/arquivamento). Grava em own-fixtures/<name>/ (GITIGNORED). NUNCA escreve no projeto-fonte.
Etica/circularidade: projeto do proprio dono -> e' braco NAO-independente; publicar so AGREGADO.
Uso: python build_local_digest.py --src ../AulaQuantum --name own-aulaquantum --genre acompanhamento-aula
"""
import argparse
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# diretorios pesados / de conteudo (nao de organizacao) — pulados inteiros
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", ".mypy_cache", ".ruff_cache",
             ".pytest_cache", "dist", "build", "outputs", "figuras", "dataset", "datasets", "_sources",
             "papers", "livros", "material_aulas", "referencias", "assets", "checkpoints", ".vscode",
             ".claude", "convert"}
# arquivos de CONTEUDO academico — excluidos (queremos organizacao, nao as respostas)
SKIP_NAME = re.compile(r"(respostas?|capitulo|answer|booklet|extracted|_from_pdf|train|test|infer|"
                       r"spaceship|simpsons|common|robust_train|md_para_docx|pptx_to_pdf|"
                       r"presentation_generator|cli)\b", re.I)
KEEP_EXT = {".md", ".yaml", ".yml", ".toml", ".txt", ".cfg", ".ini"}
SKIP_EXT = {".docx", ".pdf", ".pptx", ".png", ".jpg", ".jpeg", ".csv", ".zip", ".7z", ".py",
            ".ipynb", ".lock", ".log", ".html", ".json"}  # .json fora p/ nao vazar overviews pesados
CAP_FILE = 8000
CAP_TOTAL = 42000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--genre", default="acompanhamento-aula")
    a = ap.parse_args()
    src = os.path.abspath(a.src)
    if not os.path.isdir(src):
        print(f"ERRO: {src} nao e' dir"); return 2

    kept, tree, total = [], [], 0
    blob = ""
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not re.fullmatch(r"assets ?\d+", d)]
        rel = os.path.relpath(root, src)
        # registra nomes de subdiretorios na arvore (inclui os que serao pulados — p/ ver a estrutura)
        for d in sorted(dirs) + [d for d in sorted(os.listdir(root))
                                 if os.path.isdir(os.path.join(root, d)) and d not in dirs]:
            relp = (("" if rel == "." else rel + "/") + d + "/").replace("\\", "/")
            if relp not in tree:
                tree.append(relp)
        depth = 0 if rel == "." else rel.count(os.sep) + 1
        if depth > 3:
            dirs[:] = []
            continue
        for fn in sorted(files):
            relp = (("" if rel == "." else rel + "/") + fn).replace("\\", "/")
            tree.append(relp)
            ext = os.path.splitext(fn)[1].lower()
            if ext in SKIP_EXT or ext not in KEEP_EXT:
                continue
            if SKIP_NAME.search(fn):
                continue
            if total >= CAP_TOTAL:
                continue
            try:
                txt = open(os.path.join(root, fn), encoding="utf-8", errors="replace").read()[:CAP_FILE]
            except Exception:  # noqa
                continue
            blob += f"\n\n===== {relp} =====\n" + txt
            total += len(txt)
            kept.append(relp)

    # sinais de conformidade de SOFTWARE
    treelc = [t.lower() for t in tree]
    def any_in(sub):
        return any(sub in t for t in treelc)
    sig_sw = {
        "README": any_in("readme"),
        "pkg_meta": any_in("pyproject.toml") or any_in("setup.py") or any_in("requirements"),
        "tests": any_in("/test") or any_in("test_") or any_in("/tests/"),
        "CI": any(".github/workflows" in t for t in treelc),
        "LICENSE": any_in("license") or any_in("copying"),
    }
    # sinais de GENERO acompanhamento-de-aula (o que importa PARA o genero)
    sig_genre = {
        "fonte_unica": any_in("curso.yaml") or any_in("_overview") or any_in("map.md"),
        "doc_padroes": any_in("padrao") or any_in("template_") or any_in("agents.md"),
        "tickets_sistema": any_in("tickets/"),
        "estrutura_temporal": any_in("semana") or any_in("week") or any(re.search(r"assets ?\d", t) for t in treelc),
        "tombstone_arquivo": bool(re.search(r"(deletad|arquivad|movid|archived|→ z:|snapshot)", blob, re.I)),
        "datas_rastreio": bool(re.search(r"20\d\d-\d\d-\d\d|ultima atualiza", blob, re.I)),
    }
    out = os.path.join(HERE, "own-fixtures", a.name)
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "ORG.md"), "w", encoding="utf-8").write(
        f"# Digest de ORGANIZACAO — {a.name} (genero declarado: {a.genre})\n"
        f"> Apenas camada de organizacao do projeto do proprio dono. Conteudo academico EXCLUIDO.\n" + blob)
    open(os.path.join(out, "STRUCTURE.md"), "w", encoding="utf-8").write(
        "# Estrutura (arvore, capada)\n" + "\n".join("- " + p for p in tree[:300]))
    json.dump({"name": a.name, "genre": a.genre, "kept": kept, "n_tree": len(tree),
               "conformidade_sw": sig_sw, "score_sw": sum(sig_sw.values()),
               "sinais_genero": sig_genre, "score_genero": sum(sig_genre.values())},
              open(os.path.join(out, ".meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{a.name:20} sw {sum(sig_sw.values())}/5 {sig_sw}")
    print(f"{'':20} genero {sum(sig_genre.values())}/6 {sig_genre}  | {len(kept)} arq, {total} chars")


if __name__ == "__main__":
    raise SystemExit(main())
