from __future__ import annotations

import numpy as np
import pytest

pytest.importorskip("calculus_with_python.symbolic", exc_type=ImportError)

from calculus_with_python.compare import compare_derivative, compare_integral


def test_compare_derivative_sin_matches_cos() -> None:
    x = np.linspace(-np.pi, np.pi, 201)
    result = compare_derivative("sin(x)", x, h=1e-6, method="central")
    assert np.allclose(result["symbolic"], np.cos(x), atol=1e-8)
    assert np.max(result["abs_error"]) < 1e-5


def test_compare_integral_sin_zero_pi() -> None:
    result = compare_integral("sin(x)", 0.0, float(np.pi), n=801, method="simpson")
    assert abs(result["symbolic"] - 2.0) < 1e-12
    assert abs(result["numerical"] - 2.0) < 1e-8
    assert result["abs_error"] < 1e-7
