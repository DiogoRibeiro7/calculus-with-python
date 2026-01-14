# Instructor checklist

Before class:

1. Run `python -m pip install -U poetry` (if needed) and `poetry install` (1.11+ for Python 3.11/3.12); optionally `poetry install -E symbolic` for SymPy demos.
2. Execute the notebooks (`jupyter nbconvert --execute notebooks/<NN>_name.ipynb`) or run `poetry run jupyter lab` to preview outputs.
3. Generate CLI plots: `poetry run calcwithpy plot ...`, `calcwithpy diff ...`, `calcwithpy integrate ...`.
4. Update figures in `assets/figures/` if you edit notebooks (run the helper scripts if necessary).
5. Review docs/ (concepts, syllabus, FAQ, gallery) and instructor notes prior to teaching.
