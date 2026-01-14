from __future__ import annotations

import numpy as np
import pytest

pytest.importorskip("sympy")

import sympy as sp  # type: ignore[import]

from calculus_with_python.symbolic import (
    lambdify_expr,
    symbolic_definite_integral,
    symbolic_derivative,
    symbolic_integral,
    to_symbol,
)


def test_symbolic_derivative_cubic() -> None:
    result = symbolic_derivative("x**3")
    expected = 3 * sp.symbols("x") ** 2
    assert sp.simplify(result - expected) == 0


def test_symbolic_second_derivative_sin() -> None:
    result = symbolic_derivative("sin(x)", order=2)
    expected = -sp.sin(sp.symbols("x"))
    assert sp.simplify(result - expected) == 0


def test_symbolic_integral_polynomial() -> None:
    result = symbolic_integral("x")
    expected = sp.symbols("x") ** 2 / 2
    assert sp.simplify(result - expected) == 0


def test_symbolic_definite_integral_sin() -> None:
    result = symbolic_definite_integral("sin(x)", 0.0, float(np.pi))
    assert abs(float(result) - 2.0) < 1e-12


def test_lambdify_expr() -> None:
    expr = to_symbol("x**2 + 1")
    fn = lambdify_expr(expr)
    grid = np.linspace(-2.0, 2.0, 9)
    expected = grid ** 2 + 1
    assert np.allclose(fn(grid), expected)
