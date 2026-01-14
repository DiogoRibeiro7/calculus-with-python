# Contributing

Thanks for helping make *calculus-with-python* a reliable teaching resource. Follow these steps to keep the repository consistent.

## Testing

- `poetry install` to populate the virtual environment.
- `poetry run pytest` to exercise the unit tests in `tests/`.
- `poetry run ruff check .` enforces the shared linting rules.
- `poetry run mypy src` runs the type checks.
- `make fmt` formats the code via Ruff; run it before pushing so linting stays green.

You can also rely on the convenience targets in the `Makefile` (`make install`, `make test`, `make lint`, `make typecheck`, `make run-demos`) as shortcuts for the commands above.

## Style and tooling

- Ruff is run as part of the CI and through `.pre-commit-config.yaml`; install `pre-commit` and run `pre-commit run --all-files` to verify locally.
- Notebooks should be executed end-to-end (e.g., `jupyter nbconvert --execute notebooks/<name>.ipynb`) so outputs stay fresh. Commit both the notebook and any figures saved in `assets/figures/`.
- When adding new Python modules, follow the existing typing style and add docstrings that focus on the numerical reasoning.

## Adding notebooks

1. Update or create `notebooks/<NN>_name.ipynb` via JupyterLab or `nbformat`.
2. Save any generated plots into `assets/figures/` and reference them from the notebook (and optionally the README).
3. Provide a short “Exercises” section at the end of each notebook segment to prompt students with follow-up tasks.
4. If the notebook introduces new concepts, update `docs/concepts.md` or the README as needed.

## Documentation and learning path

- The `docs/concepts.md` page outlines how the grids, domain restrictions, numerical error, and stability concerns work together.
- The README’s “Learning path” section shows the canonical sequence of notebooks; keep it up to date when you add or rename lessons.

## Ready to contribute?

Fork the repo, implement your changes on a branch, make sure the tests and linters all pass, and open a pull request with a short description of what the update teaches. Reviewers will focus on clarity for future learners, so keep explanations approachable.
