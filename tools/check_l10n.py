#!/usr/bin/env python3
"""Validate standardized l10n pairs and guard canonical-source updates.

Only Markdown files with an HTML ``l10n: doc_id=...`` colophon are in scope.
Legacy translation schemes remain outside this guard until migrated explicitly.

Usage:
    python tools/check_l10n.py            # validate staged snapshot + pair sync
  python tools/check_l10n.py --working  # validate structure + working-tree sync
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
# The colophon must be the first content in the file — optionally preceded by ONE
# standard YAML frontmatter block (product files like knowledge-architecture.md carry
# real metadata frontmatter; README-style files carry none). Either way, nothing but
# frontmatter may come before it: this keeps the guard's "prominent top-of-file" intent.
COLOPHON_RE = re.compile(
    r"\A\ufeff?(?:---\n.*?\n---\n)?\s*<!--\s*l10n:\s*(.*?)\s*-->", re.DOTALL
)


@dataclass(frozen=True)
class LocalizedDocument:
    path: Path
    doc_id: str
    lang: str
    canonical: bool
    source_lang: str | None
    translation_of: str | None
    text: str
    colophon_end: int


def git_lines(*args: str) -> set[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return {
        line.strip().replace("\\", "/")
        for line in result.stdout.splitlines()
        if line.strip()
    }


def git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        detail = result.stderr.strip() or "unknown git error"
        raise RuntimeError(f"git {' '.join(args)}: {detail}")
    return result.stdout


def changed_paths(working: bool) -> set[str]:
    if working:
        changed = git_lines("diff", "--name-only", "--diff-filter=ACMR", "HEAD")
        changed |= git_lines("ls-files", "--others", "--exclude-standard")
        return changed
    return git_lines("diff", "--cached", "--name-only", "--diff-filter=ACMR")


def parse_colophon(path: Path, text: str | None = None) -> LocalizedDocument | None:
    if text is None:
        text = path.read_text(encoding="utf-8", errors="replace")
    match = COLOPHON_RE.search(text[:4000])
    if not match or "doc_id=" not in match.group(1):
        return None

    fields: dict[str, str] = {}
    canonical = False
    for part in (item.strip() for item in match.group(1).split("·")):
        if part == "canonical":
            canonical = True
        elif "=" in part:
            key, value = part.split("=", 1)
            fields[key.strip()] = value.strip()

    required = {"doc_id", "lang"}
    if missing := required - fields.keys():
        names = ", ".join(sorted(missing))
        raise ValueError(
            f"{path.relative_to(ROOT).as_posix()}: colophon missing {names}"
        )

    return LocalizedDocument(
        path=path,
        colophon_end=match.end(),
        doc_id=fields["doc_id"],
        lang=fields["lang"],
        canonical=canonical,
        source_lang=fields.get("source_lang"),
        translation_of=fields.get("translation_of"),
        text=text,
    )


def markdown_documents(working: bool) -> list[LocalizedDocument]:
    documents: list[LocalizedDocument] = []
    if working:
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", ".venv"} for part in path.parts):
                continue
            document = parse_colophon(path)
            if document:
                documents.append(document)
    else:
        tracked = sorted(
            path for path in git_lines("ls-files", "--cached") if path.endswith(".md")
        )
        for relative_path in tracked:
            path = ROOT / relative_path
            document = parse_colophon(path, git_text("show", f":{relative_path}"))
            if document:
                documents.append(document)
    return documents


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate_group(
    doc_id: str, documents: list[LocalizedDocument], changed: set[str]
) -> list[str]:
    errors: list[str] = []
    canonicals = [document for document in documents if document.canonical]
    translations = [document for document in documents if not document.canonical]

    if len(canonicals) != 1:
        errors.append(
            f"{doc_id}: expected exactly 1 canonical document, found {len(canonicals)}"
        )
        return errors
    canonical = canonicals[0]

    if not translations:
        errors.append(f"{doc_id}: canonical document has no translation")
        return errors

    languages = [document.lang for document in documents]
    if len(languages) != len(set(languages)):
        errors.append(
            f"{doc_id}: duplicate language in pair/group: {', '.join(languages)}"
        )

    for translation in translations:
        expected = (
            translation.path.parent / (translation.translation_of or "")
        ).resolve()
        if not translation.translation_of or expected != canonical.path.resolve():
            errors.append(
                f"{relative(translation.path)}: translation_of must point to {canonical.path.name}"
            )
        if translation.source_lang != canonical.lang:
            errors.append(
                f"{relative(translation.path)}: source_lang={translation.source_lang!r}; "
                f"expected {canonical.lang!r}"
            )
        # The selector link must sit close after the colophon — window is relative to
        # where the colophon ends, not an absolute byte offset, so a product file's
        # (possibly long) frontmatter doesn't push the link out of a fixed-size window.
        SELECTOR_WINDOW = 400
        canonical_window = canonical.text[canonical.colophon_end: canonical.colophon_end + SELECTOR_WINDOW]
        translation_window = translation.text[translation.colophon_end: translation.colophon_end + SELECTOR_WINDOW]
        if f"({translation.path.name})" not in canonical_window:
            errors.append(
                f"{relative(canonical.path)}: missing selector link to {translation.path.name}"
            )
        if f"({canonical.path.name})" not in translation_window:
            errors.append(
                f"{relative(translation.path)}: missing selector link to {canonical.path.name}"
            )

    group_paths = {relative(document.path) for document in documents}
    canonical_path = relative(canonical.path)
    touched = group_paths & changed
    if canonical_path in touched and touched != group_paths:
        missing = ", ".join(sorted(group_paths - touched))
        errors.append(
            f"{doc_id}: canonical update requires every translation; missing: {missing}"
        )
    return errors


def main() -> int:
    working = "--working" in sys.argv
    try:
        documents = markdown_documents(working)
    except (RuntimeError, ValueError) as error:
        sys.stderr.write(f"\n[l10n] {error}\n")
        return 1

    groups: dict[str, list[LocalizedDocument]] = defaultdict(list)
    for document in documents:
        groups[document.doc_id].append(document)

    changed = changed_paths(working)
    errors: list[str] = []
    for doc_id, group in sorted(groups.items()):
        errors.extend(validate_group(doc_id, group, changed))

    if errors:
        sys.stderr.write("\n[l10n] inconsistent translation pairs:\n")
        for error in errors:
            sys.stderr.write(f"  - {error}\n")
        sys.stderr.write(
            "Update every translation with its changed canonical, or use --no-verify intentionally.\n\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
