"""Generate noisy samples for Capstone A."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path

import numpy as np
import pandas as pd


def target_function(x: np.ndarray) -> np.ndarray:
    """Base function behind the synthetic measurements."""
    return np.sin(1.5 * x) + 0.3 * np.cos(2.0 * x) + 0.05 * (x - 5) ** 2


def build_dataset(*, num_points: int, noise_std: float, seed: int, output_path: Path) -> None:
    """Sample the function, add noise, and write to CSV."""
    rng = np.random.default_rng(seed)
    x = np.linspace(0.0, 10.0, num=num_points)
    y_clean = target_function(x)
    y_noisy = y_clean + rng.normal(scale=noise_std, size=x.shape)
    df = pd.DataFrame({"x": x, "y": y_noisy})
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def parse_args() -> ArgumentParser:
    parser = ArgumentParser(description="Create Capstone A dataset")
    parser.add_argument("--num-points", type=int, default=200, help="Number of samples to generate.")
    parser.add_argument("--noise-std", type=float, default=0.12, help="Standard deviation of added noise.")
    parser.add_argument("--seed", type=int, default=42, help="PRNG seed for reproducible noise.")
    parser.add_argument("--output", type=Path, default=Path("capstone/a_function_from_data/dataset.csv"), help="Target CSV path.")
    return parser


def main() -> None:
    parser = parse_args()
    args = parser.parse_args()
    build_dataset(
        num_points=args.num_points,
        noise_std=args.noise_std,
        seed=args.seed,
        output_path=args.output,
    )


if __name__ == "__main__":
    main()
