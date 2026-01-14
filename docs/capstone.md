# Capstone Projects

This repo hosts three capstone tracks that invite students to explore calculus numerically and narrate their findings.

- **General capstone instructions**: `capstone/README.md` covers the shared goal, deliverables, constraints (no SciPy, reuse repo helpers), and points to the grading rubric in `capstone/rubric.md`.
- **Capstone A – Model a function from data** (`capstone/a_function_from_data/`): start with the provided `dataset.csv` (or run `python capstone/a_function_from_data/make_dataset.py`), fit a polynomial, compare derivatives and integrals, and summarize how the model behaves.
- **Capstone B – Numerical validation against symbolic truth** (`capstone/b_symbolic_truth/`): compare numerical differentiation/integration against SymPy expressions when available, plot error vs `h` and `n`, and defend which methods are best.
- **Capstone C – Motion story** (`capstone/c_motion_story/`): work with a synthetic velocity curve, estimate acceleration, find sign-change intervals, and quantify net displacement vs distance.

Each track ships with a starter and a solution notebook. Figures are stored under `assets/figures/<track_name>/` and checked into Git whenever they represent canonical visualizations. Use `scripts/check_notebooks.py` to ensure the notebooks and figure directories stay healthy before submitting changes.
