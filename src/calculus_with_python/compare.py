from __future__ import annotations

from typing import Callable

import numpy as np

from .differentiation import Method as DiffMethod, difference_quotient
from .grids import FloatArray
from .integration import Method as IntegrationMethod, integrate_f
from .symbolic import (
    lambdify_expr,
    symbolic_definite_integral,
    symbolic_derivative,
    to_symbol,
)


def compare_derivative(
    expr: str,
    x: FloatArray,
    *,
    h: float = 1e-5,
    method: DiffMethod = "central",
) -> dict[str, FloatArray]:
    """Compare symbolic derivative with a finite-difference approximation."""
    parsed_expr = to_symbol(expr)
    exact_expr = symbolic_derivative(expr)
    symbolic_fn = lambdify_expr(exact_expr)
    numeric_fn: Callable[[FloatArray], FloatArray] = lambdify_expr(parsed_expr)

    x_arr = np.asarray(x, dtype=np.float64)
    y_sym = np.asarray(symbolic_fn(x_arr), dtype=np.float64)
    y_num = np.asarray(
        difference_quotient(numeric_fn, x_arr, h=h, method=method), dtype=np.float64
    )

    return {
        "symbolic": y_sym,
        "numerical": y_num,
        "abs_error": np.abs(y_sym - y_num),
    }


def compare_integral(
    expr: str,
    a: float,
    b: float,
    *,
    n: int = 401,
    method: IntegrationMethod = "simpson",
) -> dict[str, float]:
    """Compare symbolic definite integral with numeric quadrature."""
    parsed_expr = to_symbol(expr)
    numeric_fn = lambdify_expr(parsed_expr)
    numerical = integrate_f(
        numeric_fn,
        a,
        b,
        n=n,
        method=method,
        riemann_side="midpoint",
    )

    symbolic_value = symbolic_definite_integral(expr, a, b)
    if isinstance(symbolic_value, float):
        symbolic_float = symbolic_value
    else:
        symbolic_float = float(symbolic_value)

    return {
        "symbolic": symbolic_float,
        "numerical": numerical,
        "abs_error": abs(symbolic_float - numerical),
    }
