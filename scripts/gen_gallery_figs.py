from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

assets_dir = Path("assets/figures")
assets_dir.mkdir(parents=True, exist_ok=True)

x = np.linspace(-3.0, 3.0, 400)
polys = {
    "x^2": x ** 2,
    "x^3": x ** 3,
    "x^2 - x": x ** 2 - x,
}
fig, ax = plt.subplots(figsize=(7, 4))
for label, values in polys.items():
    ax.plot(x, values, label=label)
ax.set_title("Polynomial family")
ax.set_ylim(-15, 15)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)
fig.savefig(assets_dir / "gallery_polynomials.png", dpi=150, bbox_inches="tight")
plt.close(fig)

x = np.linspace(-2 * np.pi, 2 * np.pi, 600)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)")
ax.plot(x, np.tan(x), label="tan(x)", linestyle="--")
ax.set_ylim(-4, 4)
for n in [-np.pi / 2, np.pi / 2]:
    ax.axvline(n, color="gray", linestyle=":" , alpha=0.6)
ax.set_title("Trigonometric functions")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)
fig.savefig(assets_dir / "gallery_trig.png", dpi=150, bbox_inches="tight")
plt.close(fig)

x = np.linspace(0.1, 3.0, 400)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, np.exp(x), label="exp(x)")
ax.plot(x, np.log(x), label="log(x)")
ax.set_title("Exponential vs logarithm")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)
fig.savefig(assets_dir / "gallery_exp_log.png", dpi=150, bbox_inches="tight")
plt.close(fig)

x = np.linspace(-4.0, 4.0, 400)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, 1 / (x - 1), label="1/(x - 1)")
ax.plot(x, 1 / (x ** 2 + 1), label="1/(x^2 + 1)")
ax.set_ylim(-4, 4)
ax.axvline(1, color="gray", linestyle=":" , alpha=0.6)
ax.set_title("Rational functions with asymptotes")
ax.legend()
ax.grid(True)
fig.savefig(assets_dir / "gallery_rational.png", dpi=150, bbox_inches="tight")
plt.close(fig)

x = np.linspace(-3.0, 3.0, 400)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, np.abs(x), label="|x|")
piece = np.where(x < 0, x ** 2, np.sqrt(np.clip(x, 0, None)))
ax.plot(x, piece, label="piecewise (x<0 -> x^2, x>=0 -> sqrt(x))", linestyle="--")
ax.set_title("Absolute & piecewise functions")
ax.legend()
ax.grid(True)
fig.savefig(assets_dir / "gallery_piecewise.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("Gallery figures generated.")
