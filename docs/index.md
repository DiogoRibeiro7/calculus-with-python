# Calculus with Python Mini-Course

## Course overview

This repository is designed as a self-contained mini-course on numerical calculus. It combines a small reference implementation (`src/`), scripted demos (`scripts/`), guarded exercises/tests (`tests/`), and a sequence of notebooks that progressively deepen your understanding of plotting, differentiation, integration, and applied mini-projects.

## Prerequisites

- Python 3.11 or 3.12 (+ pip or Poetry)
- Basic familiarity with NumPy and matplotlib
- Comfortable reading lightly typed Python code and running Jupyter notebooks

## Learning outcomes

By the end of the course you will:

1. Understand how to generate safe, monotonic grids and evaluate functions without leaking numerical issues.
2. Apply finite difference formulas to approximate derivatives and reason about truncation vs. rounding error.
3. Use Riemann, trapezoid, and Simpson quadrature to approximate integrals and compare convergence rates.
4. Blend symbolic and numerical tools to verify results, visualize errors, and build simple projects that reinforce the theory.
