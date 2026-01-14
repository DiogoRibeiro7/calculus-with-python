from __future__ import annotations

from typing import Callable

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.floating]


def poly(*coeffs: float) -> Callable[[FloatArray], FloatArray]:
    """
    Polynomial factory using Horner's method.

    Example:
        f(x) = 1 + 2x + 3x^2 -> poly(1, 2, 3)

    Args:
        coeffs: Coefficients in increasing order.

    Returns:
        Callable f(x) that supports numpy arrays.
    """
    c = np.asarray(coeffs, dtype=np.float64)

    def f(x: FloatArray) -> FloatArray:
        x_arr = np.asarray(x, dtype=np.float64)
        y = np.zeros_like(x_arr)
        for a in c[::-1]:
            y = y * x_arr + a
        return y

    return f


def sin(x: FloatArray) -> FloatArray:
    return np.sin(np.asarray(x, dtype=np.float64))


def cos(x: FloatArray) -> FloatArray:
    return np.cos(np.asarray(x, dtype=np.float64))


def exp(x: FloatArray) -> FloatArray:
    return np.exp(np.asarray(x, dtype=np.float64))


def logistic(x: FloatArray) -> FloatArray:
    """
    Numerically stable logistic function.
    """
    x_arr = np.asarray(x, dtype=np.float64)
    out = np.empty_like(x_arr)
    pos = x_arr >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-x_arr[pos]))
    expx = np.exp(x_arr[~pos])
    out[~pos] = expx / (1.0 + expx)
    return out


def sqrt(x: FloatArray) -> FloatArray:
    return np.sqrt(np.asarray(x, dtype=np.float64))


def log(x: FloatArray) -> FloatArray:
    return np.log(np.asarray(x, dtype=np.float64))
