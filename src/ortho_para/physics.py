import numpy as np

kB = 1.380649e-23     # J/K
Theta_rot = 85.4      # K (approx for H2)

def E_J(J: int) -> float:
    """Rotational energy (J) for level J (in Joules)."""
    return kB * Theta_rot * J * (J + 1)

def f_ortho_eq(T: float, Jmax: int = 40) -> float:
    """
    Equilibrium ortho fraction at temperature T (K).
    Uses nuclear spin-statistics: para (even J, g_ns=1), ortho (odd J, g_ns=3).
    """
    Js = np.arange(0, Jmax + 1)
    boltz = np.exp(-np.array([E_J(J) for J in Js]) / (kB * T))
    g_ns = np.where(Js % 2 == 0, 1, 3)          # even J: para=1, odd J: ortho=3
    degeneracy = (2 * Js + 1) * g_ns
    Z = np.sum(degeneracy * boltz)
    ortho_sum = np.sum(degeneracy[Js % 2 == 1] * boltz[Js % 2 == 1])
    return float(ortho_sum / Z)

def ortho_rhs(t: float, f: float, T: float, k_conv: float) -> float:
    """Kinetics ODE for ortho fraction: df/dt = -k_conv * (f - f_eq(T))."""
    return -k_conv * (f - f_ortho_eq(T))
