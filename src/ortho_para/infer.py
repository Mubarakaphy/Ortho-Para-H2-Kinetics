import numpy as np
from scipy.optimize import curve_fit
from .physics import f_ortho_eq

def _relaxation_model(t, k, T, f0):
    f_eq = f_ortho_eq(T)
    return f_eq + (f0 - f_eq) * np.exp(-k * t)

def fit_k(t_s, f_obs, T, f0):
    """Return (k_hat, k_std)."""
    t_s = np.asarray(t_s, dtype=float)
    f_obs = np.asarray(f_obs, dtype=float)
    (k_hat,), pcov = curve_fit(lambda tt, kk: _relaxation_model(tt, kk, T, f0),
                               t_s, f_obs, p0=[1e-3], bounds=(0, np.inf))
    k_std = float(np.sqrt(pcov[0, 0])) if pcov.size else np.nan
    return float(k_hat), k_std
