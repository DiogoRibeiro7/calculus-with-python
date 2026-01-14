from __future__ import annotations

from typing import Mapping, Optional

import numpy as np
import numpy.typing as npt

from .grids import Function, safe_eval

FloatArray = npt.NDArray[np.floating]


def plot_function(
    f: Function,
    x: FloatArray,
    *,
    ax: Optional[object] = None,
    label: Optional[str] = None,
    title: Optional[str] = None,
    xlabel: str = "x",
    ylabel: str = "f(x)",
    show_grid: bool = True,
    **line_kwargs: object,
) -> object:
    """
    Plot a single function f over a grid x using matplotlib.

    Args:
        f: Function to plot.
        x: 1D grid.
        ax: Existing matplotlib Axes. If None, creates a new figure/axes.
        label: Curve label.
        title: Plot title.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        show_grid: Whether to show grid.
        **line_kwargs: Forwarded to matplotlib's `plot`.

    Returns:
        Matplotlib Axes object.

    Notes:
        This function imports matplotlib lazily to keep the core import light.
    """
    import matplotlib.pyplot as plt  # local import by design

    x_arr = np.asarray(x, dtype=np.float64)
    y_arr = safe_eval(f, x_arr)

    if ax is None:
        _, ax = plt.subplots()

    ax.plot(x_arr, y_arr, label=label, **line_kwargs)  # type: ignore[attr-defined]
    ax.set_xlabel(xlabel)  # type: ignore[attr-defined]
    ax.set_ylabel(ylabel)  # type: ignore[attr-defined]

    if title is not None:
        ax.set_title(title)  # type: ignore[attr-defined]
    if show_grid:
        ax.grid(True)  # type: ignore[attr-defined]
    if label is not None:
        ax.legend()  # type: ignore[attr-defined]

    return ax


def plot_many(
    functions: Mapping[str, Function],
    x: FloatArray,
    *,
    ax: Optional[object] = None,
    title: Optional[str] = None,
    xlabel: str = "x",
    ylabel: str = "y",
    show_grid: bool = True,
) -> object:
    """
    Plot multiple named functions on the same axes.
    """
    import matplotlib.pyplot as plt  # local import by design

    if ax is None:
        _, ax = plt.subplots()

    for name, f in functions.items():
        plot_function(
            f,
            x,
            ax=ax,
            label=name,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            show_grid=show_grid,
        )

    ax.legend()  # type: ignore[attr-defined]
    return ax
