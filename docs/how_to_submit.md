# How to submit exercises

1. **Execute the exercise notebooks** with Jupyter (via `poetry run jupyter lab` or `nbconvert --execute`). Make sure the `assets/figures/` outputs are updated when you generate figures.
2. **Export your filled notebook** as HTML or PDF when submitting to an instructor or repository. Use `jupyter nbconvert --to html exercises/XX_*.ipynb` for convenience.
3. **Add a short reflection** or summary comment in the notebook explaining what you learned or where you struggled; this helps instructors provide targeted feedback.
4. **Commit your Markdown/HTML exports** alongside the updated notebooks or upload them through your LMS. When committing, keep the `exercises/` and `solutions/` folders separate—do not merge solution explanations into the exercise notebooks.
5. **Run the automated checks** (`poetry run pytest`, `poetry run ruff check .`) before submission to catch obvious issues.
