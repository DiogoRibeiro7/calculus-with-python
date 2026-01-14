"""Ensure scripts can import the package even when PYTHONPATH is not set."""

from __future__ import annotations

import sys
from pathlib import Path


def ensure_src_path() -> None:
    """Guarantee :mod:`src` is first on :data:`sys.path` for scripts."""
    root = Path(__file__).resolve().parents[1]
    src_path = str(root / "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)


ensure_src_path()
