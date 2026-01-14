from __future__ import annotations

from typing import Callable, cast

import argparse
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from .differentiation import Method as DiffMethod, difference_quotient
from .integration import Method as IntegrationMethod, integrate_f
from .examples import sin, cos, exp, log
from .grids import FloatArray, make_grid

try:
    from .symbolic import lambdify_expr, to_symbol

    SYMPY_ENABLED = True
except ImportError:
    SYMPY_ENABLED = False

PREDEFINED: dict[str, Callable[[FloatArray], FloatArray]] = {
    "sin(x)": sin,
    "cos(x)": cos,
    "exp(x)": exp,
    "x**2": lambda xs: xs ** 2,
    "log(x)": log,
}


def resolve_function(expr: str) -> Callable[[FloatArray], FloatArray]:
    if expr in PREDEFINED:
        return PREDEFINED[expr]
    if not SYMPY_ENABLED:
        raise RuntimeError(
            "SymPy is required for custom expressions; install the symbolic extra."
        )
    return lambdify_expr(to_symbol(expr))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="calcwithpy")
    subparsers = parser.add_subparsers(dest="command", required=True)

    plot = subparsers.add_parser("plot")
    plot.add_argument("--expr", default="sin(x)")
    plot.add_argument("--a", type=float, default=-2 * math.pi)
    plot.add_argument("--b", type=float, default=2 * math.pi)
    plot.add_argument("--n", type=int, default=400)
    plot.add_argument("--out", type=Path, default=Path("assets/figures/cli_plot.png"))

    diff = subparsers.add_parser("diff")
    diff.add_argument("--expr", default="sin(x)")
    diff.add_argument("--x0", type=float, default=0.0)
    diff.add_argument("--h", type=float, default=1e-5)
    diff.add_argument("--method", choices=["forward", "backward", "central"], default="central")

    integrate = subparsers.add_parser("integrate")
    integrate.add_argument("--expr", default="sin(x)")
    integrate.add_argument("--a", type=float, default=0.0)
    integrate.add_argument("--b", type=float, default=math.pi)
    integrate.add_argument("--n", type=int, default=1001)
    integrate.add_argument("--method", choices=["riemann", "trapezoid", "simpson"], default="simpson")

    return parser.parse_args()


def run_plot(expr: str, a: float, b: float, n: int, out: Path) -> None:
    fn = resolve_function(expr)
    x = make_grid(a, b, n)
    y = fn(x)
    plt.figure()
    plt.plot(x, y, label=expr)
    plt.title(f"Function: {expr}")
    plt.legend()
    plt.grid(True)
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()


def run_diff(expr: str, x0: float, h: float, method: DiffMethod) -> None:
    fn = resolve_function(expr)
    rediff = difference_quotient(fn, x0, h=h, method=method)
    print(f"{method} derivative of {expr} at {x0} ≈ {rediff}")


def run_integrate(expr: str, a: float, b: float, n: int, method: IntegrationMethod) -> None:
    fn = resolve_function(expr)
    value = integrate_f(fn, a, b, n=n, method=method)
    print(f"{method} integral of {expr} over [{a}, {b}] with n={n} ≈ {value}")


def main() -> None:
    args = parse_args()
    if args.command == "plot":
        run_plot(args.expr, args.a, args.b, args.n, args.out)
    elif args.command == "diff":
        run_diff(args.expr, args.x0, args.h, cast(DiffMethod, args.method))
    elif args.command == "integrate":
        run_integrate(
            args.expr,
            args.a,
            args.b,
            args.n,
            cast(IntegrationMethod, args.method),
        )
