from __future__ import annotations

import _bootstrap  # noqa: F401
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from calculus_with_python.differentiation import difference_quotient
from calculus_with_python.examples import sin, cos
from calculus_with_python.grids import make_grid, safe_eval


def main() -> None:
    x = make_grid(-2.0 * np.pi, 2.0 * np.pi, 1200)

    h = 1e-5
    d_sin = difference_quotient(sin, x, h=h, method="central")
    cos_true = safe_eval(cos, x)

    x0 = 1.0
    hs = np.logspace(-12, -1, 60)
    errs = []
    for hh in hs:
        approx = difference_quotient(sin, float(x0), h=float(hh), method="central")
        errs.append(abs(approx - np.cos(x0)))

    out_dir = Path(__file__).resolve().parents[1] / "assets" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots()
    ax.plot(x, d_sin, label="d/dx sin(x) (central diff)")
    ax.plot(x, cos_true, label="cos(x) (ground truth)", linestyle="--")
    ax.set_title("Numerical derivative vs ground truth")
    ax.set_xlabel("x")
    ax.set_ylabel("value")
    ax.grid(True)
    ax.legend()
    fig.savefig(out_dir / "derivative_demo.png", dpi=160, bbox_inches="tight")
    plt.close(fig)

    fig2, ax2 = plt.subplots()
    ax2.loglog(hs, errs)
    ax2.set_title("Central difference error vs step size (sin at x=1)")
    ax2.set_xlabel("h")
    ax2.set_ylabel("|approx - cos(1)|")
    ax2.grid(True)
    fig2.savefig(out_dir / "derivative_error_vs_h.png", dpi=160, bbox_inches="tight")
    plt.close(fig2)


if __name__ == "__main__":
    main()
