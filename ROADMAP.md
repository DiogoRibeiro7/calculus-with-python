# Roadmap — calculus-with-python

This roadmap is organized as small milestones. Each milestone should end with:
- at least one notebook section demonstrating the concept,
- one script demo,
- and tests for core numerical routines.

## Milestone 0 — Project scaffold
- [x] Create repo structure (`src/`, `notebooks/`, `scripts/`, `tests/`)
- [x] Add `pyproject.toml` with minimal deps (`numpy`, `matplotlib`)
- [x] Add tests (`pytest`)
- [x] Add basic CI (pytest + ruff + mypy)

Deliverables:
- Clean install (`pip -e .` or Poetry)
- Demos generate figures into `assets/figures/`

## Milestone 1 — Plotting foundations
- [x] `grids.py`: `make_grid(a, b, n)` with validation
- [x] `examples.py`: common functions (poly, sin, exp, logistic)
- [x] `plotting.py`: `plot_function(...)` and `plot_many(...)`
- [x] Notebook `01_plotting_functions.ipynb`

Add demonstrations:
- domain restrictions (e.g., log(x), sqrt(x))
- asymptotes and axis limits
- multiple curves with legend

## Milestone 2 — Numerical differentiation
- [x] `differentiation.py`: forward/backward/central differences
- [ ] Notebook `02_numerical_derivatives.ipynb`
- [x] Script `scripts/derivative_demo.py`: compare methods and plot errors

## Milestone 3 — Numerical integration
- [x] `integration.py`: Riemann, trapezoid, Simpson + `integrate_f`
- [ ] Notebook `03_numerical_integration.ipynb`
- [x] Script `scripts/integration_demo.py`: compare methods and visualize area shading

## Milestone 4 — Mini projects
- [ ] Notebook `04_mini_projects.ipynb`
Projects:
- [ ] Find maxima/minima from derivative sign changes
- [ ] Approximate pi via integral
- [ ] Compare convergence as `n` increases (plots + short explanation)

## Milestone 5 — Packaging polish
- [ ] Improve docstrings and type hints
- [ ] Add usage examples and figures in README
- [ ] Add simple CLI entry points (optional)
- [ ] Add CI (pytest + ruff + mypy)

## Possible extensions
- optional symbolic comparisons with `sympy`
- adaptive step size for differentiation
- adaptive quadrature basics
- numerical stability notes (overflow, cancellation)
