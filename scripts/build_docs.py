from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

import nbformat
from nbconvert import HTMLExporter

NB_DIR = Path("notebooks")
BUILD_DIR = Path("docs/_build")
BUILD_DIR.mkdir(parents=True, exist_ok=True)

EXPORTER = HTMLExporter(template_name="classic")


def build(paths: Sequence[Path], execute: bool) -> None:
    for nb_path in paths:
        nb = nbformat.read(nb_path, as_version=nbformat.NO_CONVERT)
        if execute:
            from nbconvert.preprocessors import ExecutePreprocessor

            ep = ExecutePreprocessor(timeout=600)
            ep.preprocess(nb, {"metadata": {"path": nb_path.parent}})
        body, _ = EXPORTER.from_notebook_node(nb)
        target = BUILD_DIR / f"{nb_path.stem}.html"
        target.write_text(body, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build HTML docs from notebooks.")
    parser.add_argument("--exec", action="store_true", help="Execute notebooks before converting.")
    parser.add_argument(
        "--notebooks", nargs="*", help="Subset of notebook filenames to convert (without path)."
    )
    args = parser.parse_args()
    nb_paths = list(NB_DIR.glob("*.ipynb"))
    if args.notebooks:
        selected = [NB_DIR / name for name in args.notebooks]
        nb_paths = [path for path in selected if path.exists()]
    build(nb_paths, execute=args.exec)


if __name__ == "__main__":
    main()
