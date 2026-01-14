from __future__ import annotations

from typing import Callable, Literal, Union, overload

import numpy as np
import numpy.typing as npt

from .grids import safe_eval

FloatArray = npt.NDArray[np.floating]
Method = Literal["forward", "backward", "central"]


def _as_1d_float_array(x: Union[float, FloatArray]) -> FloatArray:
    x_arr = np.asarray(x, dtype=np.float64)
    if x_arr.ndim == 0:
        return x_arr.reshape(1)
    if x_arr.ndim != 1:
        raise ValueError("x must be a scalar or 1D array.")
    return x_arr


@overload
def difference_quotient(
    f: Callable[..., object],
    x: float,
    *,
    h: float = 1e-5,
    method: Method = "central",
) -> float: ...
@overload
def difference_quotient(
    f: Callable[..., object],
    x: FloatArray,
    *,
    h: float = 1e-5,
    method: Method = "central",
) -> FloatArray: ...


def difference_quotient(
    f: Callable[..., object],
    x: Union[float, FloatArray],
    *,
    h: float = 1e-5,
    method: Method = "central",
) -> Union[float, FloatArray]:
    """
    Numerical derivative using finite differences.
    """
    if not np.isfinite(h) or h <= 0:
        raise ValueError("h must be a positive finite number.")

    x_arr = _as_1d_float_array(x)

    if method == "forward":
        y1 = safe_eval(f, x_arr + h)
        y0 = safe_eval(f, x_arr)
        out = (y1 - y0) / h
    elif method == "backward":
        y0 = safe_eval(f, x_arr)
        y_1 = safe_eval(f, x_arr - h)
        out = (y0 - y_1) / h
    elif method == "central":
        y1 = safe_eval(f, x_arr + h)
        y_1 = safe_eval(f, x_arr - h)
        out = (y1 - y_1) / (2.0 * h)
    else:
        raise ValueError(f"Unknown method: {method}")

    if np.asarray(x).ndim == 0:
        return float(out[0])
    return out


def derivative(
    f: Callable[..., object],
    x: Union[float, FloatArray],
    *,
    h: float = 1e-5,
    method: Method = "central",
) -> Union[float, FloatArray]:
    """
    Alias for `difference_quotient`, kept for readability.
    """
    return difference_quotient(f, x, h=h, method=method)
