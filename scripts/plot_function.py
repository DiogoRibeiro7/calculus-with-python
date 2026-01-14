from __future__ import annotations

import _bootstrap  # noqa: F401
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from calculus_with_python.examples import sin, cos
from calculus_with_python.grids import make_grid
from calculus_with_python.plotting import plot_many


def main() -> None:
    x = make_grid(-2.0 * np.pi, 2.0 * np.pi, 1000)
    ax = plot_many({"sin(x)": sin, "cos(x)": cos}, x, title="Basic function plotting")
    fig = ax.figure  # type: ignore[attr-defined]

    out_dir = Path(__file__).resolve().parents[1] / "assets" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "plotting_demo.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
