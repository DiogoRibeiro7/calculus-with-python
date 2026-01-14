# Teaching notes

## Emphasis by lesson

- **Lesson 01**: Respect the grid contract—strictly increasing, finite endpoints, dtype control. Ask students why evaluating with vector-safe helpers is better than raw Python loops.
- **Lesson 02**: Highlight the balance between truncation and rounding error. Use the symbolic comparison section to show why central differences converge faster.
- **Lesson 03**: Compare quadrature orders visually (Riemann `O(1/n)`, trapezoid `O(1/n²)`, Simpson `O(1/n⁴)`) and reinforce the need for uniform grids if you rely on Simpson.
- **Lesson 04**: Encourage experimentation with exercises; the mini-projects illustrate how the helpers plug into real tasks.
- **Lesson 05**: Walk through each “common mistake,” explain why it happens, and show the corrected figure to make the failure mode sticky.
- **Gallery & CLI**: Call out the function gallery when introducing new functions, and the CLI demos for quick experimentation between sessions.

## Common student struggles

- Forgetting to set `PYTHONPATH` before running scripts—remind them about `scripts/_bootstrap.py`.
- Using degrees for trig or non-uniform grids for Simpson; refer them to the “common mistakes” notebook.
- Hitting mysterious `ValueError` when `h` is too small; show the guard in `differentiation.py`.

## Pedagogical tips

- Run the CLI demos live to show instant plots; point students to the gallery for reference.
- Encourage students to document “what changed in the output” when they tweak `h` or `n`.
