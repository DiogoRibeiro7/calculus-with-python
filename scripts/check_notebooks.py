"""Validate capstone notebooks and figure outputs."""
from __future__ import annotations

import sys
from pathlib import Path

import nbformat

CAPSTONE_ROOT = Path("capstone")
ASSETS_FIGURES = Path("assets/figures")
REQUIRED_SUMMARY_KEYWORDS = ("conclusion", "summary", "reflection", "interpretation")


def _ensure_path(path: Path, *, message: str) -> None:
    if not path.exists():
        raise FileNotFoundError(message)


def _check_notebook(path: Path, track_name: str) -> list[str]:
    errors: list[str] = []
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    has_capstone_heading = False
    has_setup_heading = False
    has_summary_heading = False
    has_savefig = False

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            for line in cell.source.splitlines():
                stripped = line.strip()
                if stripped.startswith("#"):
                    header_text = stripped.lstrip("#").strip()
                    if "capstone" in header_text.lower():
                        has_capstone_heading = True
                    if stripped.startswith("##") and "setup" in header_text.lower():
                        has_setup_heading = True
                    if stripped.startswith("##") and any(keyword in header_text.lower() for keyword in REQUIRED_SUMMARY_KEYWORDS):
                        has_summary_heading = True
        elif cell.cell_type == "code":
            if "savefig(" in cell.source:
                if (
                    "assets/figures" in cell.source
                    or f"capstone/{track_name}/figures" in cell.source
                    or "FIG_DIR" in cell.source
                ):
                    has_savefig = True
    if not has_capstone_heading:
        errors.append(f"{path.name} is missing a '# Capstone' heading.")
    if not has_setup_heading:
        errors.append(f"{path.name} is missing a '## Setup' heading.")
    if not has_summary_heading:
        errors.append(f"{path.name} needs a summary-style heading (Conclusion/Summary/Reflection/Interpretation).")
    if not has_savefig:
        errors.append(f"{path.name} does not save any figures into assets/figures or capstone/{track_name}/figures.")
    return errors


def main() -> None:
    if not CAPSTONE_ROOT.is_dir():
        raise SystemExit("The capstone/ directory is missing.")
    if not ASSETS_FIGURES.is_dir():
        raise SystemExit("Create assets/figures/ so notebooks can write their images there.")

    errors: list[str] = []
    for track_dir in sorted(p for p in CAPSTONE_ROOT.iterdir() if p.is_dir()):
        starter_path = track_dir / "starter.ipynb"
        solution_path = track_dir / "solution.ipynb"
        if not starter_path.exists():
            errors.append(f"Missing starter notebook for {track_dir.name}.")
            continue
        if not solution_path.exists():
            errors.append(f"Missing solution notebook for {track_dir.name}.")
            continue
        errors.extend(_check_notebook(starter_path, track_dir.name))
        errors.extend(_check_notebook(solution_path, track_dir.name))

        figure_dir = ASSETS_FIGURES / track_dir.name
        local_fig_dir = track_dir / "figures"
        if not figure_dir.exists() and not local_fig_dir.exists():
            errors.append(
                f"{track_dir.name} needs a figures folder under assets/figures/ or {track_dir}/figures/.")

    if errors:
        message = "\n".join(errors)
        raise SystemExit(f"Notebook validation failed:\n{message}")

    print("Notebook structure and figure locations appear healthy.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover - guard script entry points
        raise SystemExit(exc)
