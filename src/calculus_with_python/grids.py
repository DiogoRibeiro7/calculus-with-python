from __future__ import annotations

from typing import Callable, overload, cast

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.floating]
VectorFunction = Callable[[FloatArray], FloatArray]
ScalarFunction = Callable[[float], float]
Function = ScalarFunction | VectorFunction


def make_grid(
    a: float,
    b: float,
    n: int,
    *,
    endpoint: bool = True,
    dtype: npt.DTypeLike = np.float64,
) -> FloatArray:
    """
    Create a strictly increasing grid in [a, b].

    Args:
        a: Left endpoint.
        b: Right endpoint (must be > a).
        n: Number of points (must be >= 2).
        endpoint: Whether to include b.
        dtype: Numpy dtype for the returned array.

    Returns:
        1D numpy array of shape (n,).

    Raises:
        ValueError: If inputs are invalid.
    """
    if not np.isfinite(a) or not np.isfinite(b):
        raise ValueError("a and b must be finite numbers.")
    if b <= a:
        raise ValueError("Require b > a.")
    if n < 2:
        raise ValueError("Require n >= 2.")

    x = np.linspace(a, b, n, endpoint=endpoint, dtype=dtype)

    # Safety: ensure monotonicity
    if not np.all(np.diff(x) > 0):
        raise ValueError("Generated grid is not strictly increasing.")

    return x


@overload
def safe_eval(f: VectorFunction, x: FloatArray) -> FloatArray: ...
@overload
def safe_eval(f: ScalarFunction, x: FloatArray) -> FloatArray: ...


def safe_eval(f: VectorFunction | ScalarFunction, x: FloatArray) -> FloatArray:
    """
    Evaluate a function on a numpy grid.

    This tries direct vectorized evaluation first. If the function is scalar-only,
    it falls back to a `np.vectorize` wrapper.

    Args:
        f: Function accepting either a numpy array or a float.
        x: 1D numpy array.

    Returns:
        1D numpy array of same shape as x.

    Raises:
        ValueError: If evaluation fails.
    """
    x_arr = np.asarray(x, dtype=np.float64)
    if x_arr.ndim != 1:
        raise ValueError("x must be a 1D array.")

    # 1) Try vectorized evaluation
    try:
        y = cast(VectorFunction, f)(x_arr)
        y_arr = np.asarray(y, dtype=np.float64)
        if y_arr.shape != x_arr.shape:
            raise ValueError("Function output shape does not match input shape.")
        return y_arr
    except Exception:
        pass

    # 2) Fallback: scalar evaluation
    try:
        scalar_func = cast(ScalarFunction, f)
        vf = np.vectorize(lambda t: float(scalar_func(float(t))))
        y_arr2 = np.asarray(vf(x_arr), dtype=np.float64)
        if y_arr2.shape != x_arr.shape:
            raise ValueError("Vectorized output shape does not match input shape.")
        return y_arr2
    except Exception as e:
        raise ValueError(f"Function evaluation failed: {e}") from e
