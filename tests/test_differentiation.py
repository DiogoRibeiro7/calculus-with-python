from __future__ import annotations

import numpy as np

import pytest

from calculus_with_python.differentiation import difference_quotient, second_derivative
from calculus_with_python.examples import sin, cos, poly
from calculus_with_python.grids import make_grid


def test_derivative_quadratic_central() -> None:
    f = poly(0.0, 0.0, 1.0)  # x^2
    x = make_grid(-3.0, 3.0, 101)
    d = difference_quotient(f, x, h=1e-6, method="central")
    expected = 2.0 * x
    assert np.max(np.abs(d - expected)) < 2e-4


def test_derivative_sin_matches_cos() -> None:
    x = make_grid(-np.pi, np.pi, 201)
    d = difference_quotient(sin, x, h=1e-6, method="central")
    expected = cos(x)
    assert np.max(np.abs(d - expected)) < 3e-5


def test_scalar_input_returns_float() -> None:
    out = difference_quotient(sin, 0.5, h=1e-6, method="central")
    assert isinstance(out, float)
    assert abs(out - np.cos(0.5)) < 1e-6


def test_second_derivative_quadratic() -> None:
    f = poly(0.0, 0.0, 1.0)  # x^2
    x = make_grid(-3.0, 3.0, 101)
    second = second_derivative(f, x, h=1e-4)
    assert np.max(np.abs(second - 2.0)) < 1e-3


def test_too_small_h_raises() -> None:
    with pytest.raises(ValueError):
        difference_quotient(sin, 1e16, h=1.0)
    with pytest.raises(ValueError):
        second_derivative(sin, 1e16, h=1.0)


def test_nonfinite_input_raises() -> None:
    with pytest.raises(ValueError):
        difference_quotient(sin, float("inf"))
    with pytest.raises(ValueError):
        second_derivative(sin, float("nan"))
