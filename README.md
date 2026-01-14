# calculus-with-python

A small, educational repository to learn how to:
- plot mathematical functions in Python,
- approximate derivatives numerically,
- approximate integrals numerically,
- and build visual intuition with simple, well-tested code.

The focus is clarity and correctness, not maximum performance.

## What you’ll learn

### Plotting
- Build x-grids and evaluate functions safely
- Plot single and multiple functions
- Add labels, legends, limits, and annotations

### Numerical differentiation
- Forward / backward / central differences
- Step size trade-offs and numerical error
- Visualize the tangent line and derivative curves

### Numerical integration
- Riemann sums
- Trapezoidal rule
- Simpson’s rule
- Visualize area under the curve

## Repo layout
- `notebooks/`: guided lessons
- `src/`: small reference implementation
- `scripts/`: command-line demos
- `tests/`: correctness tests for numerical methods
- `assets/figures/`: generated images for README or docs

## Setup

### Option A: Poetry
```bash
poetry install
poetry run python -c "import calculus_with_python as c; print(c.__version__)"
```

### Option B: pip (editable)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## Run notebooks
```bash
pip install jupyter
jupyter lab
```

## Run demos
```bash
python scripts/plot_function.py
python scripts/derivative_demo.py
python scripts/integration_demo.py
```

## License
MIT.
