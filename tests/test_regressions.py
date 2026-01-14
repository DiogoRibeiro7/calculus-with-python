from __future__ import annotations

import numpy as np

from calculus_with_python.differentiation import difference_quotient
from calculus_with_python.examples import sin, cos
from calculus_with_python.grids import make_grid
from calculus_with_python.integration import integrate_f


def derivative_error(n: int) -> float:
    x = make_grid(-1.0, 1.0, n)
    approx = difference_quotient(sin, x, h=1e-6, method="central")
    truth = cos(x)
    return float(np.max(np.abs(approx - truth)))


def integration_error(n: int) -> float:
    value = integrate_f(sin, 0.0, float(np.pi), n=n, method="simpson")
    return abs(value - 2.0)


def test_derivative_error_decreases() -> None:
    errors = [derivative_error(n) for n in (201, 401, 801)]
    # allow small numerical fluctuations but expect monotonic improvement
    assert errors[1] < errors[0] * 1.05
    assert errors[2] < errors[1] * 1.05


def test_integration_error_decreases() -> None:
    errors = [integration_error(n) for n in (101, 301, 901)]
    assert errors[1] < errors[0] * 0.6
    assert errors[2] < errors[1] * 0.6
