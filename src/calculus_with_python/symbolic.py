from __future__ import annotations

from typing import Callable, cast

import numpy as np
import numpy.typing as npt

try:
    import sympy as sp  # type: ignore[import-untyped]
except ImportError as exc:
    raise ImportError(
        "SymPy is required for symbolic helpers. Install it with "
        "`poetry install -E symbolic` (or `pip install -e \".[symbolic]\"`)."
    ) from exc

__all__ = [
    "to_symbol",
    "symbolic_derivative",
    "symbolic_integral",
    "symbolic_definite_integral",
    "lambdify_expr",
]


def to_symbol(expr: str) -> sp.Expr:
    """Parse a string expression into a SymPy expression."""
    return sp.sympify(expr)


def symbolic_derivative(expr: str, *, var: str = "x", order: int = 1) -> sp.Expr:
    """Return the symbolic derivative of an expression."""
    symbol = sp.symbols(var)
    parsed = to_symbol(expr)
    return sp.diff(parsed, symbol, order)


def symbolic_integral(expr: str, *, var: str = "x") -> sp.Expr:
    """Return the indefinite integral of an expression."""
    symbol = sp.symbols(var)
    parsed = to_symbol(expr)
    return sp.integrate(parsed, symbol)


def symbolic_definite_integral(
    expr: str,
    a: float,
    b: float,
    *,
    var: str = "x",
) -> sp.Expr | float:
    """Return the symbolic definite integral (or its numeric value)."""
    symbol = sp.symbols(var)
    parsed = to_symbol(expr)
    result = sp.integrate(parsed, (symbol, a, b))
    if result.free_symbols:
        return result
    try:
        return float(result)
    except (TypeError, ValueError):
        return result


Array = npt.NDArray[np.floating]


def lambdify_expr(
    sym_expr: sp.Expr,
    *,
    var: str = "x",
) -> Callable[[Array], Array]:
    """Turn a symbolic expression into a numpy-backed callable."""
    symbol = sp.symbols(var)
    return cast(Callable[[Array], Array], sp.lambdify(symbol, sym_expr, "numpy"))
