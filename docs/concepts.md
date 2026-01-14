# Concepts

This page highlights the core numerical ideas that the codebase and notebooks reinforce. Read it before diving into the notebooks if you want to understand why the helpers behave the way they do.

## Grids and sampling

Most helpers build on 1D grids created by `calculus_with_python.grids.make_grid`. The grid enforces
strict monotonicity, finite endpoints, and uniform spacing when the method requires it. Keeping the
grid logic centralized makes the numerical methods easier to reason about and debug.

## Domain restrictions

Numerical differentiation and integration assume a well-defined domain:

- Inputs must be finite scalars or arrays and the domain must be strictly increasing.
- The derivative helpers raise when `h` is non-finite, non-positive, or so small that adding it to
  a float64 value yields the same value.
- Integrals rely on monotonically increasing `x` values so that rules like trapezoid and Simpson
  can compute meaningful arc lengths.

These restrictions prevent subtle bugs and make it safe to reuse the helpers across notebooks.

## Numerical error

Every finite-difference estimate trades truncation error (from approximating derivatives or areas)
against rounding error (from floating-point arithmetic). Central differences cancel leading terms,
yielding `O(h²)` truncation error, but shrinking `h` too far exposes rounding noise. Integration rules
have their own orders: Riemann sums are `O(1/n)`, trapezoids improve to `O(1/n²)`, and Simpson’s
rule is `O(1/n⁴)` on smooth functions.

Understanding the interplay between `h`/`n` and the error is why the notebooks include convergence
plots and why there are tests for different ordering strategies.

## Stability

Stable procedures keep errors from exploding when the input is perturbed. The codebase promotes
stability by:

- Validating inputs early and raising helpful errors rather than silently returning `nan`.
- Vectorizing evaluations via `safe_eval` while falling back to scalar loops when necessary.
- Keeping the numerical kernels small so that their contracts are easy to verify.

When you add new examples or extend the helpers, mirror these patterns to preserve the teaching
quality of the repository.
