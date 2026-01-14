from __future__ import annotations

import _bootstrap  # noqa: F401
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from calculus_with_python.examples import sin
from calculus_with_python.grids import make_grid, safe_eval
from calculus_with_python.integration import integrate_f


def main() -> None:
    a, b = 0.0, float(np.pi)

    approx_riemann = integrate_f(sin, a, b, n=2001, method="riemann", riemann_side="midpoint")
    approx_trap = integrate_f(sin, a, b, n=2001, method="trapezoid")
    approx_simp = integrate_f(sin, a, b, n=2001, method="simpson")

    print("Integral of sin(x) from 0 to pi (true = 2):")
    print(f"  Riemann (midpoint): {approx_riemann:.12f}")
    print(f"  Trapezoid:          {approx_trap:.12f}")
    print(f"  Simpson:            {approx_simp:.12f}")

    x = make_grid(a, b, 800)
    y = safe_eval(sin, x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.fill_between(x, 0.0, y, alpha=0.2)
    ax.set_title("Area under sin(x) on [0, pi]")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()

    out_dir = Path(__file__).resolve().parents[1] / "assets" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "integration_area.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
