# FAQ

## Why does Poetry complain about my Python version?
Poetry honors the `python` constraint in `pyproject.toml` (`>=3.11,<3.13`). Use `poetry env use 3.11` (or 3.12) to create a compatible virtualenv before running the workflow. On Windows you can list installed versions with `py -0p`.

## My scripts fail with `ImportError: No module named calculus_with_python`.
The scripts rely on the helper at `scripts/_bootstrap.py`, which prepends `src/` to `sys.path`. Make sure you run `python scripts/<name>.py` from the repository root. If you add new scripts, import `_bootstrap` near the top before anything else.

## Why is matplotlib defaulting to an interactive backend in CI?
The demos explicitly call `matplotlib.use("Agg")` to ensure headless environments can render plots. If you see backend warnings, confirm you haven’t overridden the setting upstream (e.g., `MPLBACKEND` environment variable) and that `matplotlib` is installed in the virtualenv you created with Poetry.

## Virtual environments and Poetry
Always run `poetry install` (or `poetry install -E symbolic` for the symbolic extras) after switching to a new Python version. Activate the venv via `poetry shell` or prefix commands with `poetry run ...`. If you mutate `pyproject.toml`, regenerate the lock file (`poetry lock`) before installing.
