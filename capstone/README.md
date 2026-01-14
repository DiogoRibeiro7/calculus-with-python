# Capstone Project

## Project goal
Design and carry out an open-ended computational calculus investigation that demonstrates how the numerical techniques, diagnostic plots, and helper functions provided in this repository can answer a real-world-inspired question. Choose a topic that invites analysis of convergence, robustness of step size, and trade-offs between model fidelity and computational effort.

## Required deliverables
- A `capstone.ipynb` or similar notebook that walks through your experimentation, leveraging the repo's helper functions from `src/` and scripts in `scripts/` without introducing SciPy as a dependency.
- Structured numerical experiments showing how parameter choices (step size, grid resolution, solver iterations, etc.) affect the solution, accompanied by verbal reasoning in markdown cells.
- Visualizations (plots or diagrams) that highlight key behaviors, along with written interpretation of what the visuals reveal.
- A short written report (inline markdown or separate Markdown file) that reflects on your objectives, methodology, and findings, including a section that connects your answers back to calculus concepts.
- Tests or assertions (in the notebook or supporting scripts) that prove your numerical results are internally consistent and reproducible.

## Constraints
- Do not import or rely on SciPy anywhere in the capstone. Use only the utilities already available in this repository or standard library modules.
- Reuse existing repository functions for integration, differentiation, plotting, or solving wherever they make sense; write new helpers only when a gap exists.
- Keep the analysis reproducible: document every external parameter and random number seed, and keep datasets or grids in version control-friendly formats (CSV, JSON, etc.) if they need to be saved.
- Respect computational limits: avoid expensive global searches—focus on a few well-reasoned parameter sweeps guided by calculus intuition.

## Evaluation criteria
The capstone will be graded according to the rubric in `capstone/rubric.md`. Students should be able to start the capstone with only this README and the rubric by following the deliverables and constraints listed above.
