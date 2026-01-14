from __future__ import annotations

from typing import Literal

import numpy as np
import numpy.typing as npt

from .grids import Function, make_grid, safe_eval

FloatArray = npt.NDArray[np.floating]
RiemannSide = Literal["left", "right", "midpoint"]
Method = Literal["riemann", "trapezoid", "simpson"]


def _as_1d_float_array(x: FloatArray) -> FloatArray:
    x_arr = np.asarray(x, dtype=np.float64)
    if x_arr.ndim != 1:
        raise ValueError("x must be a 1D array.")
    return x_arr


def _validate_xy(y: FloatArray, x: FloatArray) -> tuple[FloatArray, FloatArray]:
    x_arr = _as_1d_float_array(x)
    y_arr = _as_1d_float_array(y)
    if x_arr.shape != y_arr.shape:
        raise ValueError("x and y must have the same shape.")
    if x_arr.size < 2:
        raise ValueError("Need at least 2 points.")
    if not np.all(np.diff(x_arr) > 0):
        raise ValueError("x must be strictly increasing.")
    return y_arr, x_arr


def riemann_sum(y: FloatArray, x: FloatArray, *, side: RiemannSide = "left") -> float:
    y_arr, x_arr = _validate_xy(y, x)
    dx = np.diff(x_arr)

    if side == "left":
        return float(np.sum(y_arr[:-1] * dx))
    if side == "right":
        return float(np.sum(y_arr[1:] * dx))
    if side == "midpoint":
        y_mid = 0.5 * (y_arr[:-1] + y_arr[1:])
        return float(np.sum(y_mid * dx))
    raise ValueError(f"Unknown side: {side}")


def trapezoid(y: FloatArray, x: FloatArray) -> float:
    y_arr, x_arr = _validate_xy(y, x)
    return float(np.trapz(y_arr, x_arr))


def simpson(y: FloatArray, x: FloatArray, *, rtol: float = 1e-8, atol: float = 1e-12) -> float:
    y_arr, x_arr = _validate_xy(y, x)
    n = x_arr.size
    if n % 2 == 0:
        raise ValueError("Simpson requires an odd number of points (even number of intervals).")

    dx = np.diff(x_arr)
    if not np.allclose(dx, dx[0], rtol=rtol, atol=atol):
        raise ValueError("Simpson requires equally spaced x.")

    h = float(dx[0])
    s = y_arr[0] + y_arr[-1] + 4.0 * np.sum(y_arr[1:-1:2]) + 2.0 * np.sum(y_arr[2:-2:2])
    return float((h / 3.0) * s)


def integrate_f(
    f: Function,
    a: float,
    b: float,
    *,
    n: int = 1001,
    method: Method = "trapezoid",
    riemann_side: RiemannSide = "left",
) -> float:
    x = make_grid(a, b, n)
    y = safe_eval(f, x)

    if method == "riemann":
        return riemann_sum(y, x, side=riemann_side)
    if method == "trapezoid":
        return trapezoid(y, x)
    if method == "simpson":
        return simpson(y, x)
    raise ValueError(f"Unknown method: {method}")
