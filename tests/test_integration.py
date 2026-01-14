from __future__ import annotations

import numpy as np

from calculus_with_python.examples import sin, poly
from calculus_with_python.grids import make_grid, safe_eval
from calculus_with_python.integration import integrate_f, trapezoid, simpson


def test_trapezoid_constant() -> None:
    x = make_grid(0.0, 10.0, 1001)
    y = np.ones_like(x) * 3.0
    val = trapezoid(y, x)
    assert abs(val - 30.0) < 1e-10


def test_trapezoid_linear_exact_on_uniform_grid() -> None:
    f = poly(2.0, 5.0)  # 2 + 5x
    x = make_grid(-1.0, 3.0, 999)
    y = safe_eval(f, x)
    val = trapezoid(y, x)
    assert abs(val - 28.0) < 2e-10


def test_simpson_sin_0_pi() -> None:
    val = integrate_f(sin, 0.0, float(np.pi), n=2001, method="simpson")
    assert abs(val - 2.0) < 1e-10


def test_simpson_requires_odd_points() -> None:
    x = make_grid(0.0, 1.0, 100)  # even number of points
    y = x**2
    try:
        _ = simpson(y, x)
    except ValueError as e:
        assert "odd number of points" in str(e).lower()
    else:
        raise AssertionError("Expected ValueError for even number of points.")
