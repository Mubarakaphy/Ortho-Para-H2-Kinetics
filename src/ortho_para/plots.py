import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from .physics import f_ortho_eq, ortho_rhs

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
