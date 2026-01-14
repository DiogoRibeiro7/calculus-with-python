.PHONY: install test lint typecheck fmt run-demos

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run ruff check .

typecheck:
	poetry run mypy src

fmt:
	poetry run ruff format .

run-demos:
	poetry run python scripts/plot_function.py
	poetry run python scripts/derivative_demo.py
	poetry run python scripts/integration_demo.py
