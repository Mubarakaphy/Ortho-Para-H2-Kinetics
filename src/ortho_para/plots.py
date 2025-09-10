import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from .physics import f_ortho_eq, ortho_rhs
import argparse
from .infer import fit_k

def plot_equilibrium_curve(Tmin=2.0, Tmax=300.0, nT=300, show=True, save=None):
    Ts = np.linspace(Tmin, Tmax, nT)
    f_eqs = np.array([f_ortho_eq(T) for T in Ts])
    plt.figure()
    plt.plot(Ts, f_eqs)
    plt.xlabel("T (K)")
    plt.ylabel(r"$f_{\mathrm{ortho}}^{\mathrm{eq}}$")
    plt.title("Equilibrium ortho fraction vs T")
    plt.grid(True)
    plt.tight_layout()
    if save is not None:
        plt.savefig(save, dpi=200)
    if show:
        plt.show()
    plt.close()

def plot_relaxation(T=20.0, k_values=(1e-6, 1e-4, 1e-2, 1.0),
                    t_span=(0, 3600), npts=500, f0=0.75,
                    show=True, save=None):
    t_eval = np.linspace(*t_span, npts)
    plt.figure()
    for k in k_values:
        sol = solve_ivp(lambda t, y: ortho_rhs(t, y, T, k), t_span, [f0], t_eval=t_eval)
        plt.plot(sol.t/60, sol.y[0], label=f"k={k:.1e} s$^{{-1}}$")
    plt.xlabel("Time (min)")
    plt.ylabel(r"$f_{\mathrm{ortho}}(t)$")
    plt.title(f"Ortho relaxation at T={T} K")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if save is not None:
        plt.savefig(save, dpi=200)
    if show:
        plt.show()
    plt.close()

def cli_fit_k():
    """
    CLI: Fit k from a CSV with header 't_s,f' (time in seconds).
    Example:
      ortho-fitk --csv data/relax_synth.csv --T 20 --f0 0.75 --plot
    """

    p = argparse.ArgumentParser(description="Fit k from relaxation data (CSV with columns: t_s,f)")
    p.add_argument("--csv", required=True, help="Path to CSV (header: t_s,f)")
    p.add_argument("--T", type=float, required=True, help="Temperature [K]")
    p.add_argument("--f0", type=float, required=True, help="Initial ortho fraction at t=0")
    p.add_argument("--k0", type=float, default=1e-3, help="Initial guess for k [s^-1]")
    p.add_argument("--plot", action="store_true", help="Show data + fitted curve")
    args = p.parse_args()

    t, f = np.loadtxt(args.csv, delimiter=",", skiprows=1, unpack=True)
    k_hat, k_std = fit_k(t, f, args.T, args.f0, k0=args.k0)
    print(f"k_hat = {k_hat:.3e} s^-1  (± {k_std:.1e})")

    if args.plot:
        feq = f_ortho_eq(args.T)
        t_dense = np.linspace(t.min(), t.max(), 400)
        f_fit = feq + (args.f0 - feq) * np.exp(-k_hat * t_dense)
        plt.figure()
        plt.plot(t, f, "o", label="data")
        plt.plot(t_dense, f_fit, "-", label="fit")
        plt.xlabel("t (s)"); plt.ylabel("f_ortho"); plt.grid(True); plt.legend(); plt.tight_layout()
        plt.show()
